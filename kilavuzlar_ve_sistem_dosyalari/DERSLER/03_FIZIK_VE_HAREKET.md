# 📚 DERSLER — Fizik ve Hareket

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Fizik ve Hareket** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🟡 DERS 4: FİZİK — KAYMA VE SÜZÜLME

**Kaynak:** The Canopy World QA — Fizik: 5/10
**Sorun:** Karakter yapraklar üzerinde koşarken "süzülüyor" — ayakları zemini gerçekçi bir şekilde etkilemiyor. Sarmaşık sallanma sahnesinde bacaklar "jello" etkisiyle bükülüyor.

**ÇÖZÜM — Her aksiyon/hareket sahnesinin PHYSICS bölümüne eklenecek:**
```
WEIGHT & CONTACT RULE: The character must show VISIBLE WEIGHT on every surface
contact. Footfalls must cause measurable surface reaction (leaf dip, dust kick,
water splash, platform compression). The character must never float, hover, or
glide across a surface — every step must read as a real human foot pressing
against a real physical surface with real mass.

BODY INTEGRITY: The character's limbs, torso, and head must maintain rigid
skeletal proportions throughout all motion. No rubber-banding, no jello effect,
no elastic stretching of limbs during fast movements. Arms and legs bend only
at real joint positions (shoulder, elbow, wrist, hip, knee, ankle).
```

---

## 🟢 DERS 7: SU FİZİĞİ — SIVI ETKİLEŞİMİ

**Kaynak:** The Canopy World QA — Fizik: 5/10
**Sorun:** Su sıçramaları kıyafet ile doğru etkileşmiyor. Köpük statik ve "boyama" gibi görünüyor.

**ÇÖZÜM — Su/sıvı içeren sahnelerin PHYSICS bölümüne eklenecek:**
```
WATER INTERACTION RULE: Water must interact physically and correctly with the
character's suit and body. Splashes must spray outward from contact points,
droplets must bead and run down surfaces, foam must form and dissipate
naturally. Water must never look painted on, static, or frozen mid-splash.
Use reference: real underwater GoPro footage, real river crossing footage.
```

---

## 🔴 DERS 10: PARTİKÜL FİZİĞİ — DONMUŞ TOZ VE EGZOZ

**Kaynak:** The Deep Root QA — Fizik: 4/10
**Sorun:** Gemi iticilerinin altındaki toz ve duman donmuş, hareketsiz — kamerayla birlikte sürükleniyor, dağılmıyor. Kalkış sahnesinde egzoz hacimsel değil, düz ve statik.

**ÇÖZÜM — Her gemi/araç/patlama sahnesinin PHYSICS bölümüne eklenecek:**
```
VOLUMETRIC PARTICLE RULE: All dust, smoke, exhaust, steam, and particle effects
must behave as VOLUMETRIC, PHYSICALLY ACCURATE fluid simulations. Particles must:
- Disperse outward and upward from their source over time
- React to wind, gravity, and nearby surfaces
- NEVER freeze in place, drag with the camera, or remain static
- NEVER appear as flat 2D planes or painted textures
- Show real depth, turbulence, and dissipation
Reference: real rocket launch footage, real helicopter dust-off footage.

EXHAUST PLUME RULE: Engine exhaust must be VOLUMETRIC with visible turbulence,
heat distortion, and directional flow. Never a flat, static glow or a painted
cone shape.
```

---

## 🔴 DERS 11: DOKUNMA MORPHİ — EL YÜZEYE ERİYOR

**Kaynak:** The Deep Root QA — Karakter: 4/10
**Sorun:** Karakter bir yüzeye dokunduğunda (enerji kökleri, zemin) parmaklar yüzeyle birleşiyor, eriyor, yapısal bütünlüğünü kaybediyor. Yüz-boyun bağlantısı da kopuyor.

**ÇÖZÜM — Dokunma/temas içeren her sahneye eklenecek:**
```
CONTACT INTEGRITY RULE: When the character touches, presses, or interacts with
ANY surface (ground, wall, plant, energy source, artifact), the character's
hands, fingers, and body must maintain COMPLETE STRUCTURAL INTEGRITY. Fingers
must NOT merge with, melt into, or be absorbed by the surface being touched.
There must always be a VISIBLE BOUNDARY between skin/glove and surface — a
clear contact line, never a blend or merge.

HEAD-BODY CONNECTION: The character's head/helmet must remain PHYSICALLY
CONNECTED to the neck and torso at all times. No floating heads, no
disconnected neck joints, no gaps between helmet seal and suit collar.
```

---

## 🟡 DERS 12: YAVAŞ ÇEKİM SÜRÜKLENMESİ — DOĞAL OLMAYAN HAREKET

**Kaynak:** The Deep Root QA — Hareket: 4/10
**Sorun:** AI video modelleri bazen "sinematik" görünsün diye tüm hareketi doğal olmayan bir yavaş çekime sokuyor — karakter rüyadaymış gibi süzülüyor, gerçekçi hareket hızı kaybolıyor.

**ÇÖZÜM — Her video prompt'una eklenecek:**
```
MOTION SPEED RULE: All character movement must occur at REAL-TIME, NATURAL
human speed unless explicitly described as slow-motion in the MOTION section.
Walking: ~1.4m/s. Jogging: ~2.5m/s. Running: ~4-6m/s. No unmotivated slow-
motion drift, no dream-like floating movement, no artificial speed reduction.
The character moves like a real human in a real environment with real gravity.
```

---

## 🔴 DERS 14: DONMUŞ SU — BÜYÜK SU KÜTLELERİ STATİK

**Kaynak:** The Slow Tide QA — Çevre: 5/10, Hareket: 4/10
**Sorun:** Dev dalga tamamen donmuş — mikro hareketler yok. Su yüzeyi jel/çamur gibi davranıyor. Arka plandaki okyanus hareketsiz.

**ÇÖZÜM — Su/okyanus/dalga sahnelerine eklenecek:**
```
DYNAMIC WATER RULE: All visible water bodies (ocean, wave, river, puddle)
must show CONTINUOUS MICRO-MOTION throughout the entire 10-second clip:
- Ocean surfaces: subtle rolling swells, foam movement, light refraction
- Waves: spray at crest, foam cascading down face, internal turbulence
- Standing water: subtle ripples, reflections shifting with light
Water must NEVER appear frozen, static, gel-like, viscous, or muddy.
Reference: real ocean drone footage, real wave photography.

WAKE RULE: Any object moving through water must generate a PHYSICALLY
ACCURATE wake — V-shaped for forward motion, radial for vertical entry.
Wake must spread, dissipate, and interact with surrounding water naturally.
```

---

## 🔴 DERS 15: İMKANSIZ FİZİK — YERÇEKİMİNE AYKIRI POZİSYON

**Kaynak:** The Slow Tide QA — Fizik: 3/10
**Sorun:** Karakter dikey su duvarını normal dik duruşla tırmanıyor — yerçekimi tamamen yok sayılmış. Vücudun yerçekimi vektörüne göre doğru açıda olması gerekiyor.

**ÇÖZÜM — Her tırmanma/dikey yüzey sahnesine eklenecek:**
```
GRAVITY VECTOR RULE: The character's body must ALWAYS respond correctly to
the gravity vector. When climbing a vertical surface, the body leans INTO
the surface with visible effort — arms reaching up, legs pushing, torso
angled. The character must NEVER stand upright on a vertical surface as if
gravity doesn't exist. Hair, loose suit elements, and any hanging equipment
must hang DOWNWARD relative to true gravitational down, regardless of the
surface angle the character is on.
```

---

## 🔴 DERS 17: ÇARPIŞMA FİZİĞİ — NESNELER BİRBİRİNDEN GEÇİYOR

**Kaynak:** The Tidal Hunt QA — Fizik: 2/10
**Sorun:** Nesneler ve canlılar birbirinden geçiyor (phasing/clipping). İniş takımı kayaya eriyor, yengenç bacakları kayadan geçiyor, dev yaratık karakterin bacaklarından geçiyor, dokuçlar birbirinden geçiyor.

**ÇÖZÜM — Her sahneye eklenecek:**
```
COLLISION INTEGRITY RULE: ALL objects, creatures, characters, and environmental
elements must obey RIGID BODY COLLISION. Nothing may pass through, phase
through, or clip through any other solid object. Ship landing gear rests ON
rock, not through it. Creature limbs contact surfaces, not penetrate them.
Character limbs interact WITH creature bodies, never through them. Tentacles,
branches, and appendages collide with each other, never pass through.
Every solid object has an impenetrable boundary.
```

---

## 🔴 DERS 21: STATİK ATEŞ — BOYAMA GİBİ PATLAMA

**Kaynak:** The Kaleida Crash QA — Çevre: 4.5/10
**Sorun:** 0:01'de arka plandaki gemi patlaması statik/boyama gibi — ateş hareketsiz, duman donmuş, patlama bir fotoğraf gibi duruyor. Video modelleri ateş/patlama gibi kaotik dinamikleri doğru üretmekte zorlanıyor.

**ÇÖZÜM — Patlama/ateş/yangın içeren her sahneye eklenecek:**
```
DYNAMIC FIRE RULE: All fire, flames, explosions, and combustion events
must show CONTINUOUS, CHAOTIC, PHYSICALLY ACCURATE motion throughout
the entire clip. Fire must flicker, leap, and curl with visible
turbulence — never static, never painted, never a frozen still image.
Explosion debris must fall with correct gravity and tumble realistically.
Smoke must rise, spread, and dissipate volumetrically.
Reference: real explosion footage, real fire from controlled burns.
```

---

## 🔴 DERS 23: SIFIR-G KATILIĞI — SÜZÜLEN KARAKTER RİJİT

**Kaynak:** The Hollow Station QA — Fizik: 4/10, Hareket: 4/10
**Sorun:** Sıfır yerçekimi sahnelerinde karakter havada süzülürken tamamen rijit — statik bir 3D model sürükleniyormuş gibi. Gerçek sıfır-g'de vücut mikro hareketler yapar (hafif dönme, kol/bacak drift, saç hareketi). AI bunu atlıyor.

**ÇÖZÜM — Her sıfır-g / düşük-g sahnesine eklenecek:**
```
ZERO-G MICRO-MOTION RULE: Any character floating in zero gravity or
low gravity must show CONTINUOUS SUBTLE MICRO-MOVEMENTS throughout the
entire clip:
- Slight body rotation (1-2 degrees per second)
- Arms and legs drifting gently, not locked in a static pose
- Hair floating freely with visible strand-level motion
- Loose equipment (tethers, tool belt items) drifting independently
- Occasional small corrective movements (hand touching a surface to
  stabilize, slight push-off adjustment)
The character must NEVER resemble a static 3D model being dragged
through space on an invisible rail. Reference: real ISS astronaut
footage for authentic zero-g body language.
```

---

## 🔴 DERS 24: SIVI ETKİLEŞİM MORPH — SU KÜRESİ DOKUNMA HATASI

**Kaynak:** The Hollow Station QA — Fizik: 4/10, Karakter: 4/10
**Sorun:** 1:30'da astronot sıfır-g'deki su küresine dokunduğunda parmaklar sıvıyla birleşiyor, yapısal bütünlüğünü kaybediyor, ekstra parmaklar beliriyor. AI sıvı-katı temas noktasını çözemedi.

**ÇÖZÜM — Su küresi / sıvı etkileşim sahnelerine eklenecek:**
```
FLUID CONTACT RULE: When a character's hand/finger touches a floating
water sphere or any liquid body in zero gravity:
- The FINGER pushes INTO the sphere surface, creating a visible
  INDENTATION (surface tension deformation) — NOT merging with it
- The finger remains STRUCTURALLY INTACT — correct count (5 fingers),
  correct proportions, clear boundary between glove material and water
- The water sphere DEFORMS around the contact point (concave dimple)
  then REBOUNDS when the finger withdraws (oscillation, wobble)
- Water may adhere to the glove surface as a thin film upon withdrawal
- At NO POINT do the fingers merge with, dissolve into, or phase
  through the liquid. The glove-water boundary must be SHARP and CLEAR.
Reference: real ISS water sphere experiments (astronauts poking
floating water blobs).
```

---

## 🔴 DERS 26: İP/TETHER FİZİK KİLİDİ — HALAT DUVARA GEÇİYOR

**Kaynak:** The Orphan Bloom QA — Fizik: 4/10 — `0:52 — Rappelling rope ignores collision and tension physics.`
**Sorun:** İp (rappel tether/rope) duvarın içinden geçiyor — katı cisim çarpışmasını ihlal ediyor. İp aynı zamanda gerginlik göstermiyor: gevşek, fizik yasaları dışında sallanan bir nesne gibi görünüyor.

**ÇÖZÜM — İp/tether içeren her sahnenin PHYSICS bölümüne eklenecek:**
```
ROPE/TETHER PHYSICS LOCK: Any rope, tether, cable, or line must obey
RIGID BODY COLLISION and CATENARY PHYSICS at all times:

- The rope/tether must NEVER clip through, phase through, or merge with
  any solid surface (rock, wall, hull, ground). It must rest ON surfaces
  it contacts, drape around edges, or hang clear of them.
- The rope must show VISIBLE TENSION — if it bears the character's weight,
  it must be taut, not slack. Slight vibration/oscillation under tension
  is physically correct.
- Attachment points (hip reel, anchor) must remain FIXED and VISIBLE.
  The cable must emerge from the reel at the correct geometry and angle.
- In 0.38g/low-gravity: rope sag is less pronounced, oscillation slower.
  In 1g: rope shows normal catenary curve under its own weight.

NEGATIVE ADDITION: No rope clipping through walls. No loose, untensioned
tether under load. No rope appearing or disappearing at wall surfaces.
```

---

## 🔴 DERS 28: BİYOLÜMİNESAN TEMAS MORPH — PARLAYAN YÜZEYE DOKUNMa

**Kaynak:** The Orphan Bloom QA — Karakter: 5/10
- `0:15 — Fingers glitch and morph against the rock surface.`
- `1:25 — Gloves and fingers morph while touching the bioluminescent flora.`
- `1:55 — Hand geometry breaks down while tracing the glowing lines.`

**Sorun:** Parlayan/biyolüminesan yüzeylere dokunma anlarında el ve parmak geometrisi bozuluyor. Bu, genel temas bütünlüğü sorununu (Ders 11) aşıyor — parlayan yüzeyler özelinde çok daha sık ve ağır morph üretiyor. AI görünür şekilde parlayan bir yüzeyi "yumuşak/geçirgen" olarak yorumluyor.

**ÇÖZÜM — Parlayan veya biyolüminesan yüzey temasını içeren her sahneye eklenecek:**
```
BIOLUMINESCENT CONTACT RULE: When a character's hand, fingers, or any
body part touches a glowing or bioluminescent surface, RIGID CONTACT
GEOMETRY must be maintained with EXTRA precision:

- Fingers/gloves touch the glowing surface at a CLEAR, SHARP BOUNDARY.
  They do NOT sink into, merge with, or phase through the glowing organism
  or material — even though it appears soft or organic.
- The GLOW of the organism does NOT spread onto or "absorb" the character's
  hand. The hand remains its own solid, opaque object with its own surface.
- The contact point may show a brightening RESPONSE from the organism —
  but this is a surface emission change, NOT a geometric merging.
- All five fingers maintain CORRECT COUNT and DISTINCT SEPARATION throughout
  any interaction with glowing surfaces. The glowing light does not obscure
  or create phantom extra digits.
- This applies equally to tracing patterns, pressing palms flat, and
  lifting samples from glowing surfaces.

SPECIFIC NEGATIVE ADDITIONS: No hand morphing near glowing surfaces.
No finger count errors near bioluminescence. No glove-glow merging.
No hand geometry breakdown when touching illuminated organic matter.
No phantom fingers. No extra digits. No hand-surface fusion.
```

---

## 🔴 DERS 30: PARÇACIK YERÇEKİMİ KİLİDİ — KÜÇÜK PARÇALAR YÜZÜYOR

**Kaynak:** The Ring Walker QA — Fizik: 4/10
- `0:35 — Crystal beads liquefy and float unnaturally around the glove without gravity constraints.`
- `0:36 — Glass beads slide and morph across boot prints without grounded weight.`
- `0:58 — Sand particles stream through hands with inconsistent frame pacing.`

**Sorun:** Küçük parçacıklar (cam boncuklar, kum taneleri, kristal kırıntılar) sahnede yerçekimini ihlal ediyor — yüzüyor, sıvılaşıyor, eldivenden geçiyor. AI, küçük gevşek nesneleri fizik kurallarından muaf tutuyor. Bu hata özellikle **yakın çekimlerde** ve **el etkileşimlerinde** ağırlaşıyor.

**ÇÖZÜM — Gevşek parçacık içeren her sahnenin PHYSICS bölümüne eklenecek:**
```
PARTICLE GRAVITY LOCK: ALL loose particles — sand grains, glass beads,
crystal fragments, dust, pebbles, droplets — must obey the scene's
gravity AT ALL TIMES:

- In 0.38g: particles fall in long, flat arcs and settle SLOWLY (2-3x
  Earth duration) — they do NOT float in place, hover, orbit objects,
  or defy gravity.
- In 1g: particles fall directly and settle normally.
- Particles NEVER liquefy, merge into fluid, or change physical state
  (a solid grain remains solid).
- When a character holds/scoops particles and tilts their hand, the
  particles must POUR DOWNWARD under gravity — they do not hover on the
  palm or stream upward.
- Particles in contact with surfaces must REST on those surfaces, not
  slide across them without physical cause.
- Frame pacing on particle motion must be CONSTANT — no speed-up,
  no slow-down, no frame-rate variance within a single continuous shot.

NEGATIVE ADDITION: No floating particles without gravitational cause.
No liquefying solid grains. No particles phasing through hands/gloves.
No anti-gravity particle behavior. No frame-rate variance on particle
motion within a single shot.
```

---

## 🔴 DERS 31: ÇARPMA FİZİĞİ — DÜŞÜK YOĞUNLUKLU ETKİLER

**Kaynak:** The Ring Walker QA — Fizik: 4/10 / Çevre: 5/10
- `1:14 — Meteor impact produces low-density CGI-style particle spray without realistic physical force or terrain deformation.`

**Sorun:** Meteorit (veya herhangi bir cisim) çarpması AI tarafından "hafif", "yoğunluksuz" bir parçacık efekti olarak üretiliyor — gerçek fiziksel kütle, basınç dalgası veya zemin deformasyonu yok. Çarpma sahne dekorasyonu gibi görünüyor, fiziksel olay gibi değil. Bu, volkanik patlama ve tsunami sahnelerinde de tekrarlayabilecek sistemik bir sorun.

**ÇÖZÜM — Çarpma/patlama/etki içeren her sahnenin PHYSICS bölümüne eklenecek:**
```
IMPACT PHYSICS RULE: Any physical impact (meteorite, explosion, collision,
landing, crash) must show REALISTIC PHYSICAL CONSEQUENCES:

- TERRAIN DEFORMATION: The impact point must show a VISIBLE CRATER,
  compression, or indentation proportional to the impacting mass.
  A 15cm meteorite at hypervelocity creates a 3m crater, not a puff.
- MASS-CONSISTENT EJECTA: Ejected material (sand, rock, dust) must have
  PHYSICAL DENSITY and WEIGHT — it arcs outward under gravity, not
  floating as diffuse mist. Ejecta trajectories are flat and fast in
  low gravity, steep and heavy in high gravity.
- PRESSURE WAVE: Large impacts produce a visible ground-level pressure
  disturbance — dust moving radially outward from the impact point at
  visible speed, not instantaneously appearing.
- SOUND CONSISTENCY: Impact sound matches the visual scale — a small
  crack for a small hit, a deep thud for a large one. Never silent
  on a world with atmosphere.
- NO CGI-STYLE EFFECTS: Impacts must NOT look like video game particle
  systems — no uniform spray, no symmetrical patterns, no low-density
  mist in place of physical debris.

REFERENCE: Real-world high-speed impact footage (meteorite impacts,
bullet impacts in sand, controlled demolitions). The impact must feel
like it has MASS behind it.

NEGATIVE ADDITION: No low-density CGI particle spray. No weightless
ejecta. No crater-less impacts. No uniform symmetrical debris patterns.
No missing terrain deformation after impact.
```

---

## 🔴 DERS 36: VAKUMDA ATMOSFERİK DUMAN — EGZOZ HAVA VARMIŞ GİBİ KIVRILIYOR

**Kaynak:** The Dead Approach Compilation QA (Genel 3/10) — Parçacık: 4/10 — `1:15 — Exhaust smoke billows as if in an atmosphere`
**Sorun:** Vakumda çalışan motor egzozu, Dünya'daki roket kalkışı gibi davranıyor: kabarıyor, kıvrılıyor, mantar bulutu yapıyor, yavaşça yükseliyor. Bu tamamen yanlıştır. Ders 10 ve 33 "donmuş partikül" ve "momentum" sorunlarını kapsıyordu; bu ise ters yöndeki hata — parçacıklar hareket ediyor ama YANLIŞ ortam fiziğiyle hareket ediyor.

**Fiziksel gerçek:** Vakumda karşı basınç yoktur. Egzoz plazması çıkış ağzından itibaren **hızla ve düz** genişler, bir koni oluşturur, seyrelir ve kaybolur. Kıvrılmaz, kabarmaz, türbülans yapmaz, yükselmez — çünkü ne sürtünme ne kaldırma kuvveti vardır.

**ÇÖZÜM — PROMPT GÜNCELLEMESİ:**
```
Engine exhaust in vacuum expands rapidly outward in a straight, sharply
defined cone from the nozzle, thinning and disappearing — it does NOT
billow, curl, mushroom, roll, or rise. No turbulence, no smoke plume,
no atmospheric backpressure, no ground-effect cloud.
```
**Negatif bloğa eklenecek:** `billowing exhaust, curling smoke, mushroom cloud, rising plume, turbulent gas in vacuum`

> ⚠️ **AYRIM NOTU:** Bu kural SADECE vakum sahneleri içindir. Atmosferli
> gezegenlerde (örn. Mars, %0.6 basınç) toz ve gaz gerçekten yavaşça
> yayılır ve YERE ÇÖKER. Her filmin World Bible'ındaki atmosfer değeri
> hangi kuralın geçerli olduğunu belirler.

---

## 🔴 DERS 39: PARÇACIKLARIN SIVI GİBİ DAVRANMASI — TOZ SU ALTINDA SÜZÜLÜYOR

**Kaynak:** Low Power QA (Genel 4/10) — Parçacık ve Malzeme Fiziği: 2/10 — `0:05 — Dust drifting like zero-g underwater fluid`
**Sorun:** Ders 30 parçacığın *havada asılı kalmasını*, Ders 33 ise *momentum kaybını* kapsıyordu. Bu üçüncü ve farklı bir hata: parçacık hareket ediyor, momentumu da var — ama **yanlış ortamın** fiziğiyle hareket ediyor. Toz, havada değil suyun içindeymiş gibi davranıyor: yavaş, yoğun, girdaplı, viskoz. Kütlesiz bir sıvı akıntısı gibi süzülüyor.

**Neden oluyor:** "Dust storm swirling", "swirling dust", "drifting particles" gibi ifadeler eğitim verisinde su altı ve duman görüntüleriyle güçlü ilişkili. "Swirl" kelimesi tek başına sıvı hareketi tetikliyor.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **"Swirl" ve türevlerini KULLANMA.** Yerine parçacığın izlediği yolu tarif et.
2. Ortamı ve yerçekimini sayısal olarak yaz:
```
Particles have individual mass and follow discrete ballistic paths under
[X]g gravity. They do NOT swirl, curl, eddy, billow or flow as a
connected mass. No underwater motion, no fluid current, no viscous drift,
no smoke-like curling — each particle moves independently.
```
3. Parçacığın nereye gittiğini açıkça söyle: yükseliyor mu, çöküyor mu, yatay mı.

> ⚠️ **ORTAMA GÖRE DEĞİŞİR — TEK BİR DOĞRU YOK:**
> - VAKUM (Ay, kuyruklu yıldız, uzay): toz düz balistik yollarda gider, çökmez
> - İNCE ATMOSFER (Mars, %0.6): toz yavaşça ama KESİN olarak çöker ve yere oturur
> - YOĞUN ATMOSFER: toz gerçekten savrulur ve asılı kalabilir
> Filmin World Bible'ındaki basınç değeri hangi kuralın geçerli olduğunu belirler.

---

## 🔴 DERS 43: ETKİLEŞİM TETİKLİ GEOMETRİ MORPHU — ALET DEĞDİĞİ YERİ ERİTİYOR

**Kaynak:** The Slow Stone QA — Geçiş 1 (Çevre 3/10) ve Geçiş 2 (Kostüm 7/10) **aynı kök nedeni bağımsız olarak bildirdi**:
`1:22 — Rock texture visibly morphs and swims as the scraper tool interacts with it` ·
`4:42 — Chipped debris floats; scraper tool suffers jello warping` ·
`4:46 — Suit chest emblem warps during rock scraping` ·
`6:25 — Footprints lack depth, appear painted onto the terrain` ·
`7:05 — Cracking ground morphs geometrically rather than fragmenting`

**Sorun:** Ders 27 (mağara dokusu yüzme) **kendiliğinden** oynayan çevre dokusunu kapsıyordu — kimse dokunmuyorken yüzey nefes alıyordu. Bu farklı ve daha ağır bir hata: morph **TEMASLA TETİKLENİYOR**. Model, bir yüzeyin değiştiğini göstermesi gerektiğinde malzemeyi **kaldırmıyor**, yüzeyi **eritiyor**.

Model "değişim" talebini şöyle çözüyor:
```
İSTENEN:  alet kristale değer → pul kalkar → altında yeni yüzey → parça yere düşer
OLAN:     alet kristale değer → temas bölgesi sıvılaşır → doku komşu karelere akar
```

Üç ayrı biçimde çıkıyor ve üçü de aynı kök:
1. **Yüzey morphu** — kazınan kaya eriyor (1:22, 7:05)
2. **Alet morphu** — aletin kendisi jello gibi bükülüyor (4:42)
3. **Boyanmış iz** — ayak izi/çizik yüzeye *çizilyor*, yüzey deforme olmuyor (6:25)
4. **Sıçrama** — temas bölgesinin yakınındaki kostüm detayı da bozuluyor (4:46)

**Neden önemli:** Bu seride alet-yüzey etkileşimi dekoratif değil, **anlatının kendisi**. The Slow Stone'da kazıyıcı Çehov nesnesidir ve novum'un gösterildiği S9 tam olarak bir kazıma sahnesidir. O sahnede yüzey eridiği için **filmin tek novum'u seyirciye ulaşmadı** — QA Geçiş 3 filmi izledikten sonra novum'u yanlış anlattı. Bir morph artefaktı doğrudan hikaye kaybına dönüştü.

Ayrıca Ders 11/28 (temas morphu) **eli** koruyordu; bu ders **yüzeyi** koruyor. İkisi birlikte uygulanmalı.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**

1. Etkileşimi **çıkarma** olarak tarif et, "değişim" olarak değil:
```
❌ "the scraper works the crystal surface, changing it"
❌ "the tool alters the rock as it passes"
✅ "the scraper lifts THIN SOLID FLAKES off the crust; each flake detaches
   as a discrete rigid piece, falls and comes to REST on the ground. The
   rock beneath is revealed, not transformed. The base geometry of the
   surface never moves, bends, flows or re-forms — material is REMOVED
   from a rigid solid, never reshaped."
```

2. Aleti ayrıca kilitle — alet de morph ediyor:
```
✅ "the tool is a rigid solid object of fixed length and shape; it does not
   bend, stretch, wobble or deform at the contact point."
```

3. İz bırakma ayrı yazılır — model izi boyar:
```
✅ "boots press INTO the surface and leave depressions with real depth and
   raised rims; the marks are displaced material, not a pattern drawn onto
   the ground."
```

4. Kırılma ayrı yazılır — model kırığı morph sanıyor:
```
✅ "the ground BREAKS into separate rigid fragments with sharp edges that
   move apart; it never stretches, melts, warps or flows apart."
```

5. Negatif bloğa (kısa tut, Ders 43 satırı):
```
morphing surface at tool contact, melting geometry, flowing rock, jello tool,
painted-on footprints, surfaces reshaping instead of breaking
```

> ⚠️ **Bant uyarısı:** Bu dersin negatif satırı uzun. Etkileşim İÇEREN sahnelere
> eklenir, hepsine değil. Kazıma/dokunma/kırma yoksa satır yazılmaz.

---

## 🔴 DERS 44: DÜŞÜK-AMA-YÜKSEK YERÇEKİMİ AĞIR ÇEKİM OKUNUYOR

**Kaynak:** The Slow Stone QA — iki bağımsız rapor aynı bulguyu verdi:
Geçiş 1 (Hareket 5/10) `Pervasive slow-motion interpolation feel` ·
Rapor 0 (Hareket 5/10) `Pervasive slow-motion feel; jello effects on edges`
Film yerçekimi: **0.7g** — Bible'ın kendi ifadesiyle "yürüyüş normal, biraz daha hafif".

**Sorun:** Ders 15 (yerçekimine uygun hız) *aynı karede karışık yerçekimi vektörlerini* kapsıyordu; Ders 23 sıfır-g'de katılığı. Bu üçüncü ve farklı bir hata: yerçekimi **Dünya'ya yakın** olduğu halde model tüm sahneyi ağır çekime alıyor.

Sebep: model prompt'ta bir yerçekimi sayısı gördüğünde — değeri ne olursa olsun — bunu "uzay = ay yürüyüşü = ağır çekim" kalıbına bağlıyor. 0.7g, 0.12g ile aynı muameleyi görüyor. Oysa 0.7g'de:
```
Düşen cisim hızı    = Dünya'nın %84'ü   → gözle ayırt edilemez
Yürüyüş temposu     = neredeyse aynı    → ağır çekim YANLIŞ
Sıçrama yüksekliği  = %43 fazla         → tek görünür fark BURADA
```

**Neden önemli:** Ağır çekim filmin **temposunu** öldürüyor ve bu formatta tempo zaten en kırılgan şey — QA Geçiş 3, The Slow Stone'da 40 saniyelik ölü nokta bildirdi. Ayrıca ağır çekim hissi, sahne başına düşen bilgi miktarını azaltarak 8 dakikalık filmi 60 sahneye rağmen boş gösteriyor. Bir de yan etkisi var: model ağır çekim yaparken kare arası interpolasyona yükleniyor, bu da kenarlarda jello üretiyor (iki rapor da jello'yu ağır çekimle **aynı cümlede** bildirdi — tesadüf değil).

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**

1. **Yerçekimi sayısını tek başına yazma.** Sayının yanına insan temposunu yaz:
```
❌ "0.7g surface gravity"
✅ "0.7g — she walks at a completely normal human pace, real time. Only a
   jump or a dropped object reads slightly lighter. Everything else moves
   at ordinary Earth speed."
```

2. Gerçek zaman ifadesini açıkça iste:
```
✅ "real-time motion at 24fps, normal playback speed"
```

3. Negatif bloğa:
```
slow motion, slowed footage, floaty movement, dreamlike pacing, time-lapse
```

4. **Eşik kuralı — hangi yerçekiminde ne yazılır:**
```
0.5g ve ÜSTÜ  → "normal human pace, real time" YAZILIR (ağır çekim riski)
0.2g - 0.5g   → yalnızca sıçrama ve düşüş yavaşlar, yürüyüş normale yakın
0.2g ALTI     → ağır çekim DOĞRUDUR, Ders 15 ve 30 devreye girer
```

> 🔗 Ders 15 ile birlikte okunur: Ders 15 "her element aynı yerçekiminde
> hareket etsin" der, Ders 44 "o yerçekimi Dünya'ya yakınsa ağır çekim yapma" der.

---

## 🔴 DERS 90: MİLİMETRİK OLAY ÜRETİLMEZ — SAYISAL KİLİT OLAYI GÜVENLİ YAPARKEN GÖRÜNMEZ DE YAPIYOR

**Kaynak:** THE SECOND SHIP · Faz 7 / BEDEL 1. koşusu (S68) —
`.../FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md` D-AN
**Sorun:** ikinci vaka (F6 S58'de olayın tamamı bir dudak hareketiydi ve
o da düşmüştü — orada şartlıydı, burada kesinleşti)

Sahnenin TEK olayı: cilalı zeminin plakanın 20 cm yanında **2-3 mm**
kabarması ve el kalkınca geri inmesi. Sayı bilerek küçük seçilmişti —
büyük hareket "yarılan zemin" klişesine kayıyor [Ders 3/29]. Ekranda
kabarma **hiç oluşmadı**; rapor: "ground response is entirely absent,
the swelling never rises". Aynı sahnede ikinci mikro-beat (elin halkaya
gitmesi) de düştü.

Mekanizma: modelin hareket eşiği var. Kendi ışığı olmayan, dokusu
değişmeyen, siluete dokunmayan bir yer değiştirme, üretim sırasında
"hiç" ile aynı maliyettedir — ve model "hiç"i seçer.

**ÇÖZÜM — sayıyı koru, ÖLÇEN BİR KENAR ekle:**

```
① OKUNURLUK KANCASI: hareketi doğrudan tarif etme; hareketi ÖLÇEN
   bir görsel referans koy ve onu hareket ettir.
   2s - the long thin highlight lying across the polished floor
   BENDS: the straight reflected line breaks into a shallow arc as
   the stone RISES into a smooth swelling two or three millimeters
   proud. The swelling is read ONLY by that bending highlight and a
   hairline of contact shadow at its foot.
   (kullanılabilir kenarlar: uzanan bir highlight · bir gölge çizgisi ·
    bir yansıma · kadraj içinde duran düz bir kenar)

② KABUL KRİTERİ SAHNEYE YAZILIR: start ve olayın zirvesindeki kare
   YAN YANA konur; fark insan gözüyle ayırt edilmiyorsa kare
   REDDEDİLİR. (Bu koşuda kabul edilen karede olay hiç yoktu.)

③ END FRAME İMAJI OLAYIN ZİRVESİDİR — mikro-olaylı sahne start+end
   imaj çiftiyle üretilir; ara kareler icat edilecek yer bulamaz.
```

⚠️ Ders 44'ün tersi değil, tamamlayıcısı: 44 "hareketi ağırlaştırma"
der, 90 "hareketi ÖLÇÜLEBİLİR kıl" der. Sayı küçük kalır.

---

## 🔴 DERS 127: İVME PROMPT'A YAZILIR, EKRANA GELMEZ — "HER SANİYE +2,16 m/s" 12 PROMPTUN 12'SİNDE VARDI, PARÇA SABİT ~0,15 m/s SÜZÜLDÜ; KİLİTLENEBİLEN ŞEY İVME DEĞİL, KADRAJI TERK ETME SÜRESİDİR

**Kaynak:** THE IRON SLOPE (dikey shorts, 25.08.2026) · ⚖️ FİZİK
`Gravity & Free Fall 3/10 — TWO GRAVITIES` + master ölçümü:
S0'da kopan panel 1,0-4,0 saniye arasında gövdeye göre **sabit ~0,15 m/s**
ilerledi, yana-yukarı doğru, ve 10 saniyelik klibin sonunda **hâlâ kadrajdaydı.**
Kilit 3. saniyede 9,7 metre istiyordu — kadrajın yaklaşık 2,5 katı.

**Sorun:** Sapma tek bir sahnenin kusuru değil, **filmin varlık sebebinin
üretilememesidir.** Bu filmin novum'u ("uzayda aşağı var — aşağısı motor")
tamamen serbest cismin HIZLANARAK düşmesine bağlıydı; hızlanma çıkmayınca
izleyici 60 saniye boyunca "uzayda merdiven çıkan adam" gördü. Bağımsız
mod V hikâye merceği bunu tek cümlede söyledi: `THE ONE THING NOTHING ELSE
DOES: none found` · `Originality 2/10`.

Depoda kanıtlanmış tek mekanizma sayısal kilitti; **burada sayısal kilit
tuttu ama sayı ölçülemez cinstendi.** Model 8-10 saniyelik bir klipte zaman
integrali kurmuyor: "saniyede +2,16 m/s kazanır" cümlesinden bir ivme eğrisi
türetmiyor, "uzay + serbest cisim" önseline düşüyor — sabit hızda süzülme.
Bir izleyici de 2,16 m/s²'yi göremez; görebildiği tek şey **nesnenin kadrajdan
ne kadar çabuk çıktığıdır.**

**ÇÖZÜM — prompt'a eklenecek (ivme cümlesinin YERİNE):**

```
FALL LOCK — WRITTEN AS TIME-TO-EXIT, NOT AS ACCELERATION:
The panel separates at second 2. By second 2.6 its lower edge has crossed
the bottom frame line, and by second 3 it is completely gone from the shot;
it does not return. It travels along the hull line, parallel to the ladder
rails. At the moment it passes him it is already faster than he can climb:
it covers its own length in a quarter of a second.
```

```
① SÜRE YAZ, İVME YAZMA
   ✅ "kadrajı 0,6 saniyede terk eder"      (ekranda ölçülebilir)
   ❌ "her saniye 2,16 m/s hız kazanır"     (ekranda görünmez)
② KENDİ BOYUNU CETVEL YAP — hız, kadraj içindeki bir uzunlukla yazılır:
   "kendi boyunu çeyrek saniyede geçer" [D90'ın ölçen-kenar kuralının
   hız hâli].
③ HIZLANMA GÖSTERİLECEKSE İKİ NESNE KULLAN: model ivmeyi üretmez ama
   FARKLI HIZLARI üretir — önce yavaş geçen bir parça, arkasından onu
   geçen ikinci parça. Fark, ivmenin görünür temsilidir.
④ KABUL KRİTERİ: serbest cisim kadrajda 1 SANİYEDEN UZUN KALAMAZ.
   Kalıyorsa sahne reddedilir — ve bu ölçüm S0 kapısında yapılır:
   ffmpeg -ss <kopuş> -i clip.mp4 -t 1.2 -vf fps=5 k_%02d.png
   son karede parça varsa ⛔ ÜRETİM DURUR.
⑤ NEGATİF BLOK BU İŞİ YAPMAZ: "no floating debris, no hovering,
   no sideways drift" 12 promptun 12'sinde yazılıydı; ekranda üçü de
   oldu [D59 — yasak, ismi kazandırır].
```

> 🔗 Ders 4 · 12 · 30 (süzülme/parçacık ailesi — bu ders onların İVME
> tarafıdır) · Ders 44 (yerçekimi sayısı tek başına yazılmaz) · Ders 90
> (olayı ÖLÇEN bir kenar koy — burada cetvel, kadraj sınırının kendisidir)
> · Ders 73 (novum türetilmiş fenomene yüklenmez; bu ders "üretilemeyen
> harekete de yüklenmez" der) · Ders 74 (S0 kapısı yazılıydı, koşulmadı).
