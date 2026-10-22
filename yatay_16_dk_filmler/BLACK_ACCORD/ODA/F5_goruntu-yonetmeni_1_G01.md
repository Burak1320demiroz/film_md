# 🖼️ BLACK_ACCORD — Prompt grubu G01 (çekimler C01–C12 · bölüm B1 KAYIP KELİME)

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Kaynak: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahip planı; "plandan asla dışarı çıkma") + `NOTLAR.md` KARARLAR (18.10.2026).
> Bu dosya yeniden tasarım değil, **biçim çevirisidir**: olay, kadraj türü, özne, eylem, nesne durumu, oturma düzeni ve 171 replik planın kendisi; cümleler olabildiğince planın İngilizcesi
> (A01-A09 referans promptları, A10-A13 nesne briefi, C01-C06 görsel/video promptları, stil cümlesi). Plan C07-C12 için promptsuzdur: yalnız plan malzemesi kullanıldı
> (çekim cümlesi · stil cümlesi · kimlik kelimeleri · sabit düzen · nesne durumu · C01-C06 örneği).
> Prompt gövdesine çekim kodu, referans kodu (A02, K1), başlık satırı, "Clip n of N" YAZILMAZ. Her blok ≤4.300 karakter.
> **Plan → hat çevirisi (içerik aynı):** (1) "Use VEKH for …" → `Reference 2 (military envoy): take … from it` · (2) büyük harfli ad ve dosya kodu gövdeye yazılmaz (BT §C): özneler her yerde aynı **tutamaçla** anılır —
> the lavender-ivory clerk (Nem) · the rust-red envoy (Vekh) · the pearl-teal envoy (Ishra) · the amethyst envoy (Silex) · the moss-green consul (Orun) · the jet-black host (Nith) ·
> (3) video promptlarına 10 s vuruş planı (planın kendi hareket sırası bölündü, yeni eylem yok) · (4) replik planın tek tırnağından `says: <line>` biçimine (FILM §5 R-no) · (5) plandaki olumsuz ses cümlesi
> ("no atmospheric engine or explosion sound in vacuum") olumlu ortam cümlesine · (6) "from the first frame" → "already in view" (zincir dili) · (7) kadraj ve objektif (mm) eklendi (plan "restrained anamorphic lens character" verir, mm vermez) ·
> (8) plan A04 "speaking seam" → çekim promptlarında "mouth seam" (Görsel'de konuşma kelimesi film_dogrula hatası); referans promptunda plan metni kalır.
> **Ortak görünüm cümlesi** her Görsel'in sonunda (plan); video promptlarına eklenmez (plan yalnız Görsel'de; NOTLAR KARARLAR "plan korundu"). Model sesi AÇIK: replikler `says:` biçiminde, mekân ortam sesi videoda birebir.
> Sahip talimatı: plan sessiz kaldığı yerde yeni sıfat eklenmez. Eklenen kelimeler **yalnız** biçim kilididir: `the coat's only marking` (plan: "one small cobalt throat light") · `small enough to rest in one palm` (plan C23: "avucuna alır"; K2'ye ölçü).

---

## ROL SÖZLÜĞÜ · MEKÂN IŞIĞI · ORTAM SESİ · SES KİMLİĞİ — Fable §3'e birebir kopyalar; G02-G08 bu bölümü kullanır

```
ROL SÖZLÜĞÜ (referans anahtarındaki parantez, sekiz grupta birebir):
  1 clerk · 2 military envoy · 3 aquatic envoy · 4 mineral envoy · 5 trade consul · 6 station host · 7 chamber · 8 black hole and station · 9 four fleets.

ÖZNE TUTAMAÇLARI (gövdede ad yok; her çekimde aynı kelimeler, ilk kimlik cümlesinde tanımlanır):
  1 the lavender-ivory clerk · 2 the rust-red envoy · 3 the pearl-teal envoy · 4 the amethyst envoy · 5 the moss-green consul · 6 the jet-black host.

MEKÂN IŞIĞI (birebir, mekân başına; Görsel'de):
  SALON (iç hacim) — The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room.
  DIŞ (kara delik, istasyon, filolar) — The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow and sparse cold stars.
  DIŞ DÜNYA (her dış görselde, ışık cümlesinden önce; T18) — Everything hangs in deep black space with sparse stars around one black hole with a tilted golden accretion disk.

ORTAM SESİ (model sesi AÇIK film — aynı mekânın her VİDEO promptunda birebir; yatak yine kurguda, FILM §6):
  SALON — The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
  DIŞ — The only sound is a restrained ominous score with abstract low-frequency tension, entirely non-diegetic design.
  (plan istisnaları, ortam cümlesinin ARDINA eklenir: C01 "with a low tense score beneath it" · C02 "with a faint sound of subtle fluid movement inside the dome")

SES KİMLİĞİ (model sesi — her replikte aynı kelimeler; plan kadro tablosu "Ses" sütunu + plan C01-C06 ses kelimeleri; konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, öteki yanıt kadraj dışı):
  Nem   — a clear, precise adult woman's voice, warm and unhesitating
  Vekh  — a deep, slightly rough adult man's voice, low and controlled
  Ishra — a soft, resonant adult woman's voice with controlled fragility
  Silex — a clean, genderless voice with a light harmonic tone, calm and observant
  Orun  — a husky baritone voice, quick and polished, with dry humour
  Nith  — a low, smooth, near-flawless adult man's voice, calm and quietly contemptuous
  OFFICIAL RELAY — duygusuz, cinsiyetsiz resmî ses; kurguda eklenir, video promptuna YAZILMAZ.
  Replik kalıbı: "<ses cümlesi>, says: <line>" (konuşan adı yazılmaz).

KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6 — plan stil cümlesi "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor. SALON ve DIŞ ışığıyla aynı yönde (sıcak altın kara delik yansıması,
  soğuk gölge); C01-C12'de çelişen su/gezegen/ses yok → cümle sahibin, değişmedi.
```

---

## KİMLİK CÜMLELERİ (plan A01-A13 kelimelerinden · Görsel promptta BİREBİR · Fable FILM.md §3 `### KİMLİK CÜMLELERİ`'ne kopyalar)

> Her satır kadrajda görünen parça için; kadrajda olmayan parça yazılmaz. Nesne satırları `A10-A13` (plan numarası; film referansı değil, `film_dogrula` DERS Y2 yalnız rakamlı numaraları sayar).

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Nem · yüz | The lavender-ivory clerk is an adult nonhuman linguistic clerk with matte pale-lavender and ivory facial plates forming a narrow face, high silver cheek ridges, two long dark-violet eyes and a small vertical mouth seam, with distinctly alien bone geometry and without human ears or hair. |
| 1 | Nem · ceket + işaret | She wears a restrained dark-pewter clerk's coat with one small cobalt throat light at the base of her throat, the coat's only marking. |
| 1 | Nem · alıcı | One thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. |
| 1 | Nem · beden | She has two arms, stable upright proportions and delicate but practical hands. |
| 2 | Vekh · yüz | The rust-red envoy is an adult nonhuman military envoy with broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam, a clearly alien head. |
| 2 | Vekh · zırh | He wears bronze formal military armour over dark-red clothing. |
| 2 | Vekh · alıcı | A thin removable silver translation receiver is fixed at his right temple, separate from his anatomy. |
| 2 | Vekh · beden | His body is upright with two arms and two legs. |
| 2 | Vekh · blaster (kalça görününce) | A single compact dark blaster is holstered at his right hip. |
| 3 | Ishra · yüz | The pearl-teal envoy is an adult aquatic alien diplomat with pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins, a clearly nonhuman face. |
| 3 | Ishra · başlık | A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. |
| 3 | Ishra · giysi | Her dark-teal formal suit has pale pearl shoulder edging. |
| 3 | Ishra · alıcı | A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. |
| 4 | Silex · yüz | The amethyst envoy is an adult nonhuman envoy with a stable living-mineral anatomy: a frosted amethyst face with a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. |
| 4 | Silex · faset | The facets are continuous biological surfaces, not floating shards, with subtle internal violet translucency and no changing crystal growth. |
| 4 | Silex · pelerin | Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. |
| 4 | Silex · alıcı | A thin separate silver translation receiver rests at the right temple. |
| 5 | Orun · yüz | The moss-green consul is an adult nonhuman trade consul with layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw, an unmistakably alien face. |
| 5 | Orun · ceket | He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. |
| 5 | Orun · beden | He has two arms and a substantial but not exaggerated build. |
| 5 | Orun · alıcı | A thin removable silver translation receiver rests at his right temple. |
| 6 | Nith · yüz | The jet-black host is an adult nonhuman diplomatic station host with a polished jet-black face, one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. |
| 6 | Nith · baş sırtı | A low two-pronged cranial crest is part of the same stable head. |
| 6 | Nith · ceket | He wears a long ivory formal coat over black inner panels, with restrained gold trim. |
| 6 | Nith · alıcı | A small silver translation receiver remains at his right temple. |
| 7 | Salon · masa + cam | One rigid black hexagonal table stands before a broad panoramic curved window. |
| 7 | Salon · cam manzarası | Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. |
| 7 | Salon · altı koltuk (geniş plan) | Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. |
| 7 | Salon · masa donanımı | Discreet personal translation speakers and simple physical controls are built into the table. |
| 7 | Salon · kaburgalar | Dark stone-metal ribs line the chamber, with readable cold shadows and warm disk reflections. |
| 7 | Salon · baş koltuk (saat 12) | The far head chair at the twelve o'clock position, facing the camera, is ivory and black. |
| 7 | Salon · bronz koltuk (saat 2) | The chair at the two o'clock position is bronze-red. |
| 7 | Salon · teal koltuk (saat 4) | The chair at the four o'clock position is teal. |
| 7 | Salon · kâtip koltuğu (saat 6) | The smaller near-side clerk chair at the six o'clock position is pewter. |
| 7 | Salon · gümüş-mor koltuk (saat 8) | The chair at the eight o'clock position is pale silver-violet. |
| 7 | Salon · okra koltuk (saat 10) | The chair at the ten o'clock position is ochre-brown. |
| 8 | Kara delik | One enormous supermassive black hole has a truly dark shadow, and a bright tilted golden accretion disk with gravitationally lensed upper and lower arcs wraps around it, one side visibly brighter. |
| 8 | İstasyon | The small advanced alien diplomatic station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows, and lies outside the event horizon, away from the luminous disk material. |
| 9 | Filolar | Four clearly separated alien fleet groups stand in the outer region: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships and ochre ring-shaped merchant carriers. |
| 9 | Koridor + tıbbi gemiler | They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. |
| A10 | K1 özel ticaret rölesi (Orun) | a single palm-sized black octagonal relay body with one pale amber triangular light |
| A11 | K2 bağımsız kayıt taşı (Silex) | a single flat frosted-purple pentagonal recording slab small enough to rest in one palm |
| A12 | Tercüman alıcısı | a single thin silver translation receiver strip, removable and not a life-support part |
| A13 | W1 blaster (Vekh) | a single compact dark blaster, holstered at the right hip of the rust-red envoy |

---

## REFERANS PROMPTLARI (yalnız ilk grupta · plan A01-A09 metni birebir; özne başına TEK dosya)

> Plan referansları **tek görünüş**tür (single-subject three-quarter …); hat panel kalıbı (KIMLIK §7 P17, HİPOTEZ) uygulanmadı, plan korundu (NOTLAR KARARLAR). Panel üstünde yazı/etiket yok (plan: "no writing").
> Tek biçim farkı: "reference of NEM, an adult …" → "reference of an adult …" (büyük harfli ad gövdeye yazılmaz, BT §C). Bağımlılık yok (KAYNAK satırı yok).
> **Üretim sırası (plan: "Önce altı karakter ve salon, sonra dış kara delik ve filo masterı"):** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. Sahip her görseli seçip `ref/` altına `<No>.<AD>_v1.png` adıyla kaydeder;
> yüz, giysi, alıcı tarafı (sağ şakak) ya da koltuk renk sırası değiştiren görsel kullanılmaz, önce o düzeltilir.

### 1.NEM
```
DOSYA     ref/1.NEM_v1.png
PANELLER  tek görünüş (plan A01): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference image of an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. Plain charcoal background, soft neutral reference lighting, photoreal practical-creature cinema, landscape 16:9, no writing or logos.
```

### 2.VEKH
```
DOSYA     ref/2.VEKH_v1.png
PANELLER  tek görünüş (plan A02): three-quarter (blaster kılıfı sağ kalçada görünür)
```
```text
Create a single-subject three-quarter reference of an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing, with a single compact dark blaster holstered at the right hip. A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. Broad calm posture, restrained readable expression. Neutral charcoal reference background, realistic metallic texture, photoreal cinematic alien design, landscape 16:9, no lettering or insignia text.
```

### 3.ISHRA
```
DOSYA     ref/3.ISHRA_v1.png
PANELLER  tek görünüş (plan A03): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. Calm intelligent posture. Plain charcoal background, soft neutral light, tactile photoreal science-fiction reference, landscape 16:9, no writing.
```

### 4.SILEX
```
DOSYA     ref/4.SILEX_v1.png
PANELLER  tek görünüş (plan A04): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central speaking seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. A thin separate silver translation receiver rests at the right temple. Subtle internal violet translucency, restrained expression, no changing crystal growth. Plain charcoal reference backdrop, neutral detailed light, photoreal practical alien cinema, landscape 16:9, no lettering.
```

### 5.ORUN
```
DOSYA     ref/5.ORUN_v1.png
PANELLER  tek görünüş (plan A05): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. A thin removable silver translation receiver rests at the right temple. His expression is calculating and socially polished rather than monstrous. Plain charcoal reference background, neutral soft lighting, tactile photoreal science-fiction design, landscape 16:9, no writing.
```

### 6.NITH
```
DOSYA     ref/6.NITH_v1.png
PANELLER  tek görünüş (plan A06): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh where his calm voice resonates. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. Upright controlled posture, smooth professional menace, no human face or hair. Charcoal reference backdrop, soft neutral light, photoreal alien political thriller design, landscape 16:9, no lettering.
```

### 7.ACCORD_CHAMBER
```
DOSYA     ref/7.ACCORD_CHAMBER_v1.png
PANELLER  tek görünüş (plan A07): boş mekân master, geniş
```
```text
Create an empty master location reference of a monumental alien diplomatic chamber on a space station. One rigid black hexagonal table stands before a broad panoramic curved window. Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. Discreet personal translation speakers and simple physical controls are built into the table. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. No inhabitants, no human architecture details, no rendered writing. Photoreal cinematic 16:9.
```

### 8.BLACK_HOLE_STATION
```
DOSYA     ref/8.BLACK_HOLE_STATION_v1.png
PANELLER  tek görünüş (plan A08): dış master
```
```text
Create a breathtaking exterior master of one enormous supermassive black hole and a small advanced alien diplomatic station located in the surrounding region outside the event horizon and away from the luminous accretion disk material. The black-hole shadow is truly dark. A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The spectacle comes from scale and bent light, not a glowing solid surface or a portal. One black hole only. Photoreal scientific-inspired space cinema, wide 16:9, no lettering.
```

### 9.FOUR_FLEETS
```
DOSYA     ref/9.FOUR_FLEETS_v1.png
PANELLER  tek görünüş (plan A09): dış master
```
```text
Create a wide master reference showing four clearly separated alien fleet groups in the outer region around the same supermassive black-hole system, outside the event horizon and outside the hot accretion disk. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. Smaller escorts may recede as simple silhouettes. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. The black-hole shadow and lensed gold disk establish the background but remain one physical object. Clear geometric silhouettes, realistic metal, restrained lights, photoreal 16:9, no lettering.
```

---

## C01 — İlk kelime kayboluyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C01.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png · ref/8.BLACK_HOLE_STATION_v1.png
```

> Not: **Plan pilotu** (C01 iki ses katmanı) ve açılış (ILK_30 §6): sorun hareket hâlinde (kamera itişi + sözün başlaması), logo/yazı yok, başlık ve SOURCE / OFFICIAL RELAY etiketi kurguda. Şeffaf vizör yok; yüz yakın planı planın kendisi.
> R001 Vekh 2,0 s'den 2,0 s (4,0'da biter); R002 OFFICIAL RELAY ("We fired first.") **kurguda**, videoya yazılmaz; Vekh'in ağzı 4 s'den sonra kapalı. Plan "a low tense score" korundu (NOTLAR KARARLAR; ILK_30 F4 uygulanmadı).
> Kadrajda yalnız yüz, omuz ve zırh: eller ve kılıf kadraj altında, tarif edilmez. BT §A "fire" model sesi repliğinde: red gelirse yalnız R001 kayda geçer, metin değişmez.

### Görsel
```text
Reference 2 (military envoy): take his rust-red facial armour, two amber eyes, short jaw plates, bronze armour and silver receiver from it. Reference 7 (chamber): take the bronze-red chair and the room geometry from it. Reference 8 (black hole and station): take the black-hole shadow and the lensed golden accretion disk from it. Tight three-quarter portrait on an 85 mm lens, seen from the front so that his right temple is turned toward the camera. The rust-red envoy is an adult nonhuman military envoy with broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam, a clearly alien head. He wears bronze formal military armour over dark-red clothing. A thin removable silver translation receiver is fixed at his right temple, separate from his anatomy. He sits in the bronze-red chair at the two o'clock position, his expression calm and controlled, his amber eyes directed along the table past the edge of the frame. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon, a large dark shadow with its bent golden disk already in view, distant and separate from him. The alien face stays tactile and readable. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: The camera begins a restrained slow push toward the rust-red envoy while he draws one calm breath and his amber eyes stay fixed along the table past the edge of the frame. 2-5 s: The push continues; at about 2 s his jaw plates move with minimal natural motion and a deep, slightly rough adult man's voice, low and controlled, says: We did not fire first. By about 4 s he finishes and his mouth closes. 5-10 s: The push carries on and his mouth stays closed; his amber eyes narrow a little as he listens, and the gold light along his bronze armour shifts slightly while the black-hole view in the window behind him stays stable. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room, with a low tense score beneath it.
```

## C02 — Suçlama

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C02.png · referans (yükleme sırası, kare üretiminde): ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Açılış (ILK_30 §6): T05 su başlığı. Plan: "Reflections are restrained so that the face stays readable; life-support connections remain fixed" → yansıma kısıtı Görsel'de. Başlık şeffaf, yüz yakını planın kendisi (risk: göz asimetrisi / yansıma; kare kapısında bakılır).
> R003 Ishra 1,0 s'den 3,2 s (4,2'de biter). Su düzeyi sabit (plan A03); plan ses cümlesi "subtle fluid movement" ortam cümlesinin sonunda korundu.

### Görsel
```text
Reference 3 (aquatic envoy): take her pearlescent teal face, gill fins, water dome, dark-teal suit and receiver socket from it. Reference 7 (chamber): take the teal chair and the room geometry from it. Close three-quarter portrait on an 85 mm lens, her head turned slightly toward frame-left so that the right side of her dome with the receiver socket stays in view. The pearl-teal envoy is an adult aquatic alien diplomat with pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins, a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. She sits in the teal chair at the four o'clock position inside the same rigid transparent water dome and looks toward the rust-red envoy off-camera at frame-left with controlled disbelief; her two dark lateral eyes, pearlescent teal skin and short gill fins are unchanged. Reflections on the dome are restrained so that her face stays readable, and the life-support connections stay fixed. Behind her, softly out of focus, are the dark stone-metal ribs of the chamber. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera drifts in very slightly on the pearl-teal envoy as her eyes narrow while she listens; at about 1 s her head turns a few degrees toward frame-left and a soft, resonant adult woman's voice with controlled fragility, clear and restrained, says: Then you came here to boast about it? 3-6 s: She finishes the sentence by about 4 s, her mouth closes and her gaze stays on the rust-red envoy off-camera at frame-left. 6-10 s: The drift in continues gently; her chin lifts a little and her eyes stay narrowed, while the dome, its constant water level and the life-support connections stay fixed. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room, with a faint sound of subtle fluid movement inside the dome.
```

## C03 — Dışarıdaki filolar

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C03.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Açılış (ILK_30 §6): saf manzara değil, tehlike olayı (silah hatları aydınlanır). Diyalog yok (plan: "Ortam, gerilim ve ölçek için nefes alanı"). T13 vakumda motor/patlama sesi yok: ortam cümlesi yalnız soyut skor.
> T18 tek kara delik. Plan C03 olumsuz cümlesi ("Do not start a major battle or add new ship groups.") korundu (NOTLAR KARARLAR). Ateş/yanma yok: ışıklar gemi üstü lamba şeritleri.

### Görsel
```text
Reference 8 (black hole and station): take the black-hole shadow, the tilted golden accretion disk with its lensed arcs and the small station from it. Reference 9 (four fleets): take the four ship families, the open corridor and the tiny medical craft from it. Extreme wide exterior view on an 18 mm lens. One enormous supermassive black hole has a truly dark shadow, and a bright tilted golden accretion disk with gravitationally lensed upper and lower arcs wraps around it, one side visibly brighter. The small advanced alien diplomatic station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows, and lies outside the event horizon, away from the luminous disk material. Four clearly separated alien fleet groups stand in the outer region: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. The rust-red wedge ships stand at frame-left and the pearl-white and teal fan vessels face them from frame-right across the open corridor, with the silver faceted ships and the ochre merchant carriers farther out. A few weapon lights on the rust-red ships are beginning to brighten. All ships stay outside the event horizon and away from the disk material, and the small station is a distant silhouette. Everything hangs in deep black space with sparse stars around one black hole with a tilted golden accretion disk. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow and sparse cold stars. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slow lateral drift through the wide formation while a few weapon-light strips on the rust-red wedge ships start to brighten. 3-7 s: The drift continues across the formation; the weapon-light strips on the rust-red ships brighten further, while the pearl-white and teal fan vessels, the silver faceted ships and the ochre carriers keep their separated positions and the tiny medical craft wait near the corridor edge. 7-10 s: The drift carries on past the open corridor; the brightened weapon-light strips glow at full strength along the rust-red hulls against the tilted golden disk, and the small station stays a distant silhouette. Do not start a major battle or add new ship groups. The only sound is a restrained ominous score with abstract low-frequency tension, entirely non-diegetic design.
```

## C04 — Kâtibin itirazı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C04.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan: "Nem still at her lower clerk position, her silver temple receiver attached" → alıcı sağ şakakta görünür kalır (üç çeyrek, sağ ön). "Small plain source-monitor surface" → `a small plain dark glass panel` (ekran adı yok, Q6).
> "Not holding a weapon" → olumlu: eller açık masa kenarında. R004 Nem 1,0 s'den 2,0 s (3,0'da biter); R005 Silex kadraj dışı, kurguda (3,6 s). Nem oturuyor (ayağa kalkış C06).

### Görsel
```text
Reference 1 (clerk): take her lavender-ivory face, cheek ridges, dark-violet eyes, pewter coat and silver receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Medium close view on a 50 mm lens, seen in three-quarter from her right front. The lavender-ivory clerk is an adult nonhuman linguistic clerk with matte pale-lavender and ivory facial plates forming a narrow face, high silver cheek ridges, two long dark-violet eyes and a small vertical mouth seam, with distinctly alien bone geometry and without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light at the base of her throat, the coat's only marking. One thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. She has two arms, stable upright proportions and delicate but practical hands. She sits in the smaller near-side clerk chair at the six o'clock position, still at her lower clerk position. She has turned from a small plain dark glass panel set into the table beside her left hand toward the council, her eyes alert, and her two hands rest open on the table edge. The high silver cheek ridges, the pale lavender-ivory face and the narrow vertical mouth seam stay nonhuman and identical. Behind her are the dark stone-metal ribs of the chamber's near wall. The warm gold light falls from the side onto her cheek ridges. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A very small push begins on the lavender-ivory clerk as she lifts her gaze from the table toward the rust-red envoy and the jet-black host off-camera; at about 1 s a clear, precise adult woman's voice, warm and unhesitating, says: That's not what he said. Her mouth motion is subtle and her face geometry stays intact. 3-6 s: She finishes by about 3 s, her mouth closes and she listens, her head lifting a little further while her silver receiver stays at her right temple. 6-10 s: The push eases closer; the warm gold side light slides across her high silver cheek ridges as her eyes move from the envoy to the host. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C05 — Söz hakkı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C05.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Nith cam önündeki baş koltukta (saat 12): pencere ve kara delik arkasında (Q4). Plan: "Preserve the fixed facial ridge and crest" → olumlu: kaş sırtı ve baş sırtı sabit. Menace sakinlikten gelir, bağırma yok.
> R006 Nith 1,0 s'den 2,8 s (3,8'de biter). Eller kadrajda değil.

### Görsel
```text
Reference 6 (station host): take his jet-black face, bone-white brow ridge, ice-blue eyes, gold throat mesh, cranial crest and ivory coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Close portrait on an 85 mm lens, frontal, level with his eyes. The jet-black host is an adult nonhuman diplomatic station host with a polished jet-black face, one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. He sits upright in the far ivory-black head chair at the twelve o'clock position, his ivory coat and black inner panels immaculate, his eyes directed down the table toward the clerk off-camera. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon, softly out of focus. A controlled gold reflection edges his face, and the dark room stays spatially stable. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera eases slightly closer to the jet-black host as he makes one small downward inclination of his head; at about 1 s he speaks through his gold throat mesh and a low, smooth, near-flawless adult man's voice, calm and quietly contemptuous, says: The clerk does not address the council. 3-6 s: He finishes by about 4 s and his head returns upright, his mouth closing; his ice-blue eyes stay on the far end of the table and his composure stays unbroken. 6-10 s: The camera continues closer; a controlled gold reflection slides along the edge of his jet-black face while his bone-white brow ridge and cranial crest stay fixed and his eyes narrow slightly. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C06 — İlk açık suçlama

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C06.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Kalkma tek ve kontrollü (plan); eller masa kenarında başlar, ayakta biter, 7 s'den sonra hareket kamera eğimi. Sandalye arkasında kalır. Nith'in yanıtı (R008) kadraj dışı, kurguda.
> R007 Nem 1,0 s'den 2,4 s (3,4'te biter). Ayakta kalış sonraki çekimlerde sürer (plan: C06 sonrası çoğunlukla ayakta).

### Görsel
```text
Reference 1 (clerk): take her lavender-ivory face, cheek ridges, dark-violet eyes, pewter coat and silver receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the broad black table and the room geometry from it. Medium low view on a 35 mm lens, the camera below eye level, seen in three-quarter from her right side. The lavender-ivory clerk is an adult nonhuman linguistic clerk with matte pale-lavender and ivory facial plates forming a narrow face, high silver cheek ridges, two long dark-violet eyes and a small vertical mouth seam, with distinctly alien bone geometry and without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light at the base of her throat, the coat's only marking. One thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. She has two arms, stable upright proportions and delicate but practical hands. She is at the beginning of rising from the smaller pewter clerk chair, her upper body leaning slightly forward, both hands lightly bracing the edge of the broad black table in front of her. Her face is directed toward frame-right, toward the far end of the table where the host sits outside the crop. Behind her are the pewter clerk chair and the dark stone-metal ribs of the chamber's near wall. Gold black-hole light crosses her cheek plates and her cobalt throat light. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A quiet low-angle camera begins to rise with the lavender-ivory clerk as she starts to stand from the smaller pewter clerk chair, both hands bracing the table edge; at about 1 s she addresses the host without raising her voice, and a clear, precise adult woman's voice, warm and unhesitating, says: Your translator just declared a war. 3-7 s: She completes one controlled rise, her hands leaving the table edge as she reaches full height; the chair stays behind her and her face anatomy stays intact. 7-10 s: Standing, she faces the far end of the table; the camera tilts up gently with her, and the gold black-hole light crosses her cheek plates and cobalt throat light while her mouth stays closed. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C07 — İki düşman

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C07.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **SK1/SK2 varsayılanı** (DURUM): model sesi yalnız Vekh (R009, 1,0 s'den 1,6 s, 2,6'da biter); Ishra'nın yanıtı R010 kadraj dışı, kurguda → Ishra arkadan, flu, ağzı görünmez (plan: "öteki kişilerin arkaları veya flu siluetleri"). Oturma: sabit düzen (Vekh saat 2, Ishra saat 4, komşu), masanın köşesi üzerinden.
> Ishra arkadan: yüz cümlesi yazılmaz (kadrajda yok), başlık + giysi + alıcı yazılır. Kadrajda iki figür; yüz yalnız Vekh'in.

### Görsel
```text
Reference 2 (military envoy): take his rust-red facial armour, two amber eyes, jaw plates, bronze armour and silver receiver from it. Reference 3 (aquatic envoy): take her water dome, dark-teal suit and receiver socket from it. Reference 7 (chamber): take the bronze-red and teal chairs, the table corner and the room geometry from it. Over-the-shoulder medium two-shot on a 50 mm lens across the corner of the black hexagonal table. In the left foreground, softly out of focus, the pearl-teal envoy sits seen from behind in the teal chair at the four o'clock position. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. At frame-right, in sharp focus, sits the second figure. The rust-red envoy is an adult nonhuman military envoy with broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam, a clearly alien head. He wears bronze formal military armour over dark-red clothing. A thin removable silver translation receiver is fixed at his right temple, separate from his anatomy. He sits in the bronze-red chair at the two o'clock position facing the camera in three-quarter view, his amber eyes fixed on the pearl-teal envoy. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle lateral drift over the pearl-teal envoy's shoulder toward the rust-red envoy, who looks at her across the table corner; at about 1 s his jaw plates move and a deep, slightly rough adult man's voice, low and controlled, says: I denied the attack. 3-6 s: He finishes by about 3 s and his mouth closes; the back of her water dome tilts a few degrees and her shoulders draw back as she leans away. 6-10 s: The drift continues; his amber eyes stay fixed on her while her dome turns slightly away from him, and the gold light edges his bronze armour. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C08 — Makinenin otoritesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C08.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: C05'ten farklı kadraj: sağ önden, hafif alttan üç çeyrek (aynı yüz, aynı koltuk, aynı pencere). R011 Nith 1,0 s'den 3,8 s (4,8'de biter); R012 Ishra kadraj dışı, kurguda. Eller kadrajda değil.

### Görsel
```text
Reference 6 (station host): take his jet-black face, bone-white brow ridge, ice-blue eyes, gold throat mesh, cranial crest and ivory coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Close three-quarter portrait on an 85 mm lens from slightly below eye level, seen from his right front. The jet-black host is an adult nonhuman diplomatic station host with a polished jet-black face, one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. He sits upright in the far ivory-black head chair at the twelve o'clock position, his head turned slightly toward frame-left and his ice-blue eyes level. The broad panoramic curved window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon, softly out of focus. A controlled gold reflection edges one side of his jet-black face. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a slight drift toward the jet-black host as he lifts his chin a little; at about 1 s he speaks through his gold throat mesh and a low, smooth, near-flawless adult man's voice, calm and quietly contemptuous, says: The relay has no nation. It cannot take sides. 3-6 s: He continues and finishes by about 5 s, his head steady and his ice-blue eyes level. 6-10 s: His mouth closes; his eyes move toward frame-right while the gold reflection shifts along his jet-black face and the drift eases closer, his brow ridge and cranial crest remaining fixed. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C09 — Kimin onayı?

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Nem **ayakta** (plan: C06 sonrası çoğunlukla ayakta). "Sertifikalı kayıt levhası" → `a flat plain dark glass slab set into the table` (ekran/belge adı yok, yazı yok, Q6). R013 Nem 1,0 s'den 1,2 s (2,2'de biter); R014 Nith kadraj dışı, kurguda.

### Görsel
```text
Reference 1 (clerk): take her lavender-ivory face, cheek ridges, dark-violet eyes, pewter coat and silver receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the broad black table and the room geometry from it. Medium close view on a 50 mm lens, seen in three-quarter from her right front, slightly below eye level because she stands. The lavender-ivory clerk is an adult nonhuman linguistic clerk with matte pale-lavender and ivory facial plates forming a narrow face, high silver cheek ridges, two long dark-violet eyes and a small vertical mouth seam, with distinctly alien bone geometry and without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light at the base of her throat, the coat's only marking. One thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. She has two arms, stable upright proportions and delicate but practical hands. She stands at the near side of the table at the six o'clock position, the smaller pewter clerk chair pushed back behind her, her head bowed toward a flat plain dark glass slab set into the table in front of her, both hands resting on the table edge. Behind her are the pewter clerk chair and the dark stone-metal ribs of the chamber's near wall. The warm gold light falls from the far end of the table onto her cheek ridges. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: The camera begins a slight drift in as the lavender-ivory clerk raises her head from the plain dark glass slab in front of her and turns toward the far end of the table; at about 1 s a clear, precise adult woman's voice, warm and unhesitating, says: Who certified it? 2-6 s: She finishes at about 2 s and her mouth closes; her head settles toward the far end of the table and her shoulders square, her hands resting on the table edge. 6-10 s: The drift continues; the gold side light moves across her cheek ridges and her silver receiver as her eyes stay level. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C10 — Tüccarın küpü

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K1 kurulumu** (A10): tek siyah sekizgen gövde, tek amber üçgen ışık, soluk. T01 el-nesne: küp **açık avuçta** başlar (parmak kavraması yok), video avucu indirir, küp masaya oturur, avuç kayar. Temas kısa ve tek hareket.
> YEDEK (kare ya da video eli bozarsa): kare küpü masada gösterir (sağ el masa kenarında, avuç boş), video yalnız kamera itişi + Orun'un konuşması; bırakma kesmede (plan: "karmaşık parmak hareketi gerekirse kesmeyle sadeleşir").
> R015 Orun 1,0 s'den 3,8 s (4,8'de biter); R016 Vekh kadraj dışı, kurguda. Küp sağ elde (plan taraf vermez; sonraki Orun çekimleri aynı eli kullanır).

### Görsel
```text
Reference 5 (trade consul): take his moss-green bark-like face, amber eyes, folded lower jaw, ochre-brown coat and silver receiver from it. Reference 7 (chamber): take the ochre-brown chair, the black hexagonal table and the room geometry from it. Medium view on a 50 mm lens, seen in three-quarter from the front with his right temple toward the camera. The moss-green consul is an adult nonhuman trade consul with layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw, an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. He has two arms and a substantial but not exaggerated build. A thin removable silver translation receiver rests at his right temple. He sits in the ochre-brown chair at the ten o'clock position behind the black hexagonal table, his right forearm extending from his ochre-brown sleeve over the table toward the centre, and on his open right palm, a hand's width above the table surface, rests a single palm-sized black octagonal relay body with one pale amber triangular light. His expression is calculating and socially polished. Behind him the curved panoramic window glows with the soft gold bend of the lensed disk, and the dark stone-metal ribs frame it. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle drift toward the moss-green consul as his open right palm, carrying the palm-sized black octagonal relay body, lowers toward the table; at about 1 s a husky baritone voice, quick and polished, with dry humour, says: Every delay costs money. Shall we argue more efficiently? 3-6 s: The palm lowers until the relay rests flat on the table surface with its pale amber triangular light plainly visible, and the palm slides away from it while he finishes the sentence by about 5 s. 6-10 s: His hand withdraws to the table edge and his mouth closes; the relay's pale amber light stays lit beside his hand as the drift eases closer and his amber eyes move along the table. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C11 — Silinen şey

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Nem ayakta. C09'dan farklı kadraj: masanın karşı ucundan karşıdan yakın plan (iki şakak görünür, alıcı sağ şakakta). Ellerle jest yok (T01 riski): eller masa kenarında; hareket baş, bakış ve nefes.
> R017 Nem 1,0 s'den 4,4 s (5,4'te biter); R018 Silex kadraj dışı, kurguda.

### Görsel
```text
Reference 1 (clerk): take her lavender-ivory face, cheek ridges, dark-violet eyes, pewter coat and silver receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the broad black table and the room geometry from it. Close frontal view on an 85 mm lens from the far end of the table, looking down the table toward her. The lavender-ivory clerk is an adult nonhuman linguistic clerk with matte pale-lavender and ivory facial plates forming a narrow face, high silver cheek ridges, two long dark-violet eyes and a small vertical mouth seam, with distinctly alien bone geometry and without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light at the base of her throat, the coat's only marking. One thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. She has two arms, stable upright proportions and delicate but practical hands. She stands at the near side of the table at the six o'clock position, her eyes steady on the camera, both hands resting on the table edge below the crop. Behind her are the smaller pewter clerk chair and the dark stone-metal ribs of the chamber's near wall. The warm gold light falls across her face from the far end of the table. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: A gentle push begins on the lavender-ivory clerk as she stands at the near side of the table looking straight down it; at about 1 s a clear, precise adult woman's voice, warm and unhesitating, says: One word vanished. Not. Everything after it became a confession. 3-6 s: The push continues while she goes on, her chin lifting slightly and her eyes steady; she finishes by about 5 s. 6-10 s: Her mouth closes; she lets out a quiet breath and her shoulders settle a fraction, and the gold light shifts across her cheek ridges as the push eases to a close view. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

## C12 — Test önerisi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K2 kurulumu** (A11): tek düz, buzlu mor beşgen levha. T01 aynı yöntem: levha **açık sağ avuçta** başlar, video avucu indirir, levha masaya oturur. K2 ve C10'daki K1 birbirine dönüşmez (biçim: beşgen levha ↔ sekizgen gövde).
> YEDEK: C10 yedeği ile aynı (kare levhayı masada gösterir, video yalnız konuşma + kamera). R019 Silex 1,0 s'den 3,6 s (4,6'da biter); R020 Nith kadraj dışı, kurguda. Silex'in sağ eli (K2 aynı eliyle C23'te alınır).

### Görsel
```text
Reference 4 (mineral envoy): take its frosted amethyst face, broad facets, dark faceted eyes, pale-silver mantle and silver receiver from it. Reference 7 (chamber): take the pale silver-violet chair, the black hexagonal table and the room geometry from it. Medium view on a 50 mm lens, seen in three-quarter from the front with the right temple toward the camera. The amethyst envoy is an adult nonhuman envoy with a stable living-mineral anatomy: a frosted amethyst face with a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards, with subtle internal violet translucency and no changing crystal growth. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. A thin separate silver translation receiver rests at the right temple. The amethyst envoy sits in the pale silver-violet chair at the eight o'clock position behind the black hexagonal table, its right forearm extending from the pale-silver sleeve over the table toward the centre, and on its open right palm, a hand's width above the table surface, rests a single flat frosted-purple pentagonal recording slab small enough to rest in one palm. Its expression is restrained and observant. Behind the envoy are the dark stone-metal ribs of the chamber wall. The light is warm gold black-hole light from the panoramic window across the faces and the table, with cool readable shadows and dark stone-metal ribs around the room. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle drift toward the amethyst envoy as its open right palm, carrying the flat frosted-purple pentagonal recording slab, lowers toward the table; at about 1 s the narrow central mouth seam moves and a clean, genderless voice with a light harmonic tone, calm and observant, says: Then test a sentence none of us can mistake. 3-6 s: The palm lowers until the slab rests flat on the table surface and the palm slides away from it; the envoy finishes the sentence by about 5 s. 6-10 s: The hand withdraws to the table edge and the mouth seam closes, and the facets on its face catch the gold light as the drift eases closer. The ambient sound is quiet chamber ventilation and distant table resonance in a large stone-metal room.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde ön plan repliği model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** plan görselleri GPT Image, videoları görselden video 10 s ile hedefler ("kullanılan arayüzün mevcut oran, süre ve ses seçenekleri uygulanır"). Flow'da Görsel modu aynı promptla ve aynı referans sırasıyla kullanılabilir.
> Omni'nin Frames to Video süresi, kredisi ve repliği videoda üretmesi SMOKE P11 · P14 · P18'de ölçülür (`FLOW_GERCEKLERI.md`); ölçüm gelmeden videolar koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. Omni kredisi BİLİNMİYOR (P11).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız referans sayfası ve kare üretiminde, kare promptunun kendi sırasıyla yüklenir.
> **Sıra (plan: "Önce altı karakter ve salon, sonra dış kara delik ve filo masterı"; plan pilotu C01):** 1-9 referans sayfaları → açılış C01-C03 kareleri → **C01 videosu (plan pilotu)** → C02-C03 videoları → C04-C12 kareleri → C04-C12 videoları.
> Referanslar onaylanmadan kare, kare onaylanmadan video üretilmez. Açılış kare kapısı (ILK_30 §6): filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması / göz asimetrisi (Ishra dome) · kimlik kayması.
> **Ses:** replik taşıyan klipler C01-C02 · C04-C12 (C03 yok): model sesi (ağız kadrajda) R001 · R003 · R004 · R006 · R007 · R009 · R011 · R013 · R015 · R017 · R019; kurguda eklenen R002 (röle) · R005 · R008 · R010 · R012 · R014 · R016 · R018 · R020.
> Kıta/dış klip C03: klibin sesi yalnız soyut skor (T13); yatak Y2 kurguda. Şiddet kelimeli model sesi: C01 "fire" (red gelirse R001 kayda).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | 1.NEM | `ref/1.NEM_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 2 | 2.VEKH | `ref/2.VEKH_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 3 | 3.ISHRA | `ref/3.ISHRA_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 4 | 4.SILEX | `ref/4.SILEX_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 5 | 5.ORUN | `ref/5.ORUN_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 6 | 6.NITH | `ref/6.NITH_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 7 | 7.ACCORD_CHAMBER | `ref/7.ACCORD_CHAMBER_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 8 | 8.BLACK_HOLE_STATION | `ref/8.BLACK_HOLE_STATION_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 9 | 9.FOUR_FLEETS | `ref/9.FOUR_FLEETS_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 10 | C01 kare | `kare/C01.png` | Görsel | ref/2.VEKH_v1.png · ref/7.ACCORD_CHAMBER_v1.png · ref/8.BLACK_HOLE_STATION_v1.png (bu sırayla) · **AÇILIŞ + plan pilotu** | 2 | |
| 11 | C02 kare | `kare/C02.png` | Görsel | ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) · **AÇILIŞ** | 2 | |
| 12 | C03 kare | `kare/C03.png` | Görsel | ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png (bu sırayla) · **AÇILIŞ** | 2 | |
| 13 | C01 | `ham/C01_d1.mp4` | Frames to Video | kare/C01.png · **plan pilotu: önce üretilir** | 2 | |
| 14 | C02 | `ham/C02_d1.mp4` | Frames to Video | kare/C02.png · **AÇILIŞ** | 2 | |
| 15 | C03 | `ham/C03_d1.mp4` | Frames to Video | kare/C03.png · **AÇILIŞ** | 2 | |
| 16 | C04 kare | `kare/C04.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 17 | C05 kare | `kare/C05.png` | Görsel | ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 18 | C06 kare | `kare/C06.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 19 | C07 kare | `kare/C07.png` | Görsel | ref/2.VEKH_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 20 | C08 kare | `kare/C08.png` | Görsel | ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 21 | C09 kare | `kare/C09.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 22 | C10 kare | `kare/C10.png` | Görsel | ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 23 | C11 kare | `kare/C11.png` | Görsel | ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 24 | C12 kare | `kare/C12.png` | Görsel | ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) | 2 | |
| 25 | C04 | `ham/C04_d1.mp4` | Frames to Video | kare/C04.png | 2 | |
| 26 | C05 | `ham/C05_d1.mp4` | Frames to Video | kare/C05.png | 2 | |
| 27 | C06 | `ham/C06_d1.mp4` | Frames to Video | kare/C06.png | 2 | |
| 28 | C07 | `ham/C07_d1.mp4` | Frames to Video | kare/C07.png | 2 | |
| 29 | C08 | `ham/C08_d1.mp4` | Frames to Video | kare/C08.png | 2 | |
| 30 | C09 | `ham/C09_d1.mp4` | Frames to Video | kare/C09.png | 2 | |
| 31 | C10 | `ham/C10_d1.mp4` | Frames to Video | kare/C10.png | 2 | |
| 32 | C11 | `ham/C11_d1.mp4` | Frames to Video | kare/C11.png | 2 | |
| 33 | C12 | `ham/C12_d1.mp4` | Frames to Video | kare/C12.png | 2 | |

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce)

> Q3 (tüm çekimler): ORTAK GÖRÜNÜM "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor → Fable'a `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` notu (bu dosyanın başında); çekimle çelişen su/gezegen/ses yok.
> Q5 (tüm çekimler): `plume · smoke · drip · wet · bubbles` yok; Ishra'nın başlığındaki su plan gereği katı hâl ("constant visible water level"); C03'te silah ışığı = lamba şeridi, ateş/duman yok.
> Q7 (tüm çekimler): her `Reference n` yalnız o tek görünüşte görüneni istiyor (yüz, giysi, alıcı, koltuk, kara delik); C01'de ref 8'den yalnız kara delik/disk (istasyon sayfada küçük, kadrajda yok).
> Q8 (tüm çekimler): model sesi AÇIK film; ses kelimesi yalnız ORTAM SESİ cümlesi ve replikler; zıt iki istek yok (C01 skor "beneath" ortam cümlesi; C03 olumsuz plan cümlesi tek).

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C01 | 2 (kılıf/blaster ve eller kadraj dışı → tarif edilmedi) · 4 (pencere ve kara delik Vekh'in arkası yazıldı) · plan "from the first frame" → "already in view" (zincir dili) | Plan "a low tense score" korundu (ILK_30 F4 "müzik C01'de girmiyor" uygulanmadı, NOTLAR KARARLAR) |
| C02 | 4 (Ishra'nın arkası: kaburgalar) · 5 (dome suyu katı hâl, hareket yok) | "subtle fluid movement" plan ses cümlesi korundu; su düzeyi sabit kalır (Q8 zıt değil: ses yalnız ortam) |
| C03 | 2 · 5 (weapon lights = lamba; alev/duman yok) | Plan olumsuz cümlesi "Do not start a major battle or add new ship groups." korundu (NOTLAR KARARLAR); tek sahne |
| C04 | 2 ("not holding a weapon" → olumlu: eller açık, masa kenarında) · 4 (kişinin arkası: kaburgalar) · 6 ("source-monitor" → `plain dark glass panel`) | — |
| C05 | 4 (pencere ve kara delik Nith'in arkası yazıldı) | — |
| C06 | 1 (boğaz ışığı: sayı + konum + `the coat's only marking`) · 4 (arkası: sandalye + kaburga) | — |
| C07 | 2 (Ishra arkadan: yüz cümlesi çıkarıldı, başlık + giysi + alıcı kaldı) · 4 (Vekh'in arkası: pencere; Ishra'nın arkası kamera) | SK1/SK2 varsayılanı uygulandı (sahip cevabı bekler) |
| C08 | 4 (pencere ve kara delik Nith'in arkası yazıldı) | — |
| C09 | 4 · 6 ("sertifikalı kayıt levhası" → `flat plain dark glass slab set into the table`, yazı yok) | — |
| C10 | 2 (K1: biçim + ölçü + taraf: sağ avuç) · 4 (Orun'un arkası: cam + kaburga) | T01 el-nesne: açık avuç yöntemi + YEDEK satırı |
| C11 | 4 (Nem'in arkası: sandalye + kaburga) | Ellerle jest yok (T01 riski) |
| C12 | 2 (K2: biçim + ölçü `small enough to rest in one palm` + taraf) · 4 (Silex'in arkası: kaburga) | "speaking seam" → "mouth seam" (Görsel'de konuşma kelimesi hata); referans promptunda plan kelimesi kalır |
