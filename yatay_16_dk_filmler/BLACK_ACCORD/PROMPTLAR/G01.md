# 🖼️ BLACK_ACCORD — Prompt grubu G01 (çekimler C01–C12 · bölüm B1 KAYIP KELİME) · tur 2 (uzatma)

> Yazan: goruntu-yonetmeni (faz 5, tur 2; sahip 18.10.2026 "sanki promtlar kısa" → `ODA/F5_uzatma_karari.md`: Görsel hedef 2.400-3.200 kr, Video hedef 1.000-1.500 kr, tavan 4.300; ikisi de uzar). Kararlar: tur 1/1b/1c (`ODA/F5_fable_birlestirme_1_G01.md`) korunur.
> Kaynak: `BLACK_ACCORD_16DK_DIYALOGLU_FILM_SENARYOSU.md` (sahip planı; "plandan asla dışarı çıkma") + FILM.md §3 (KİMLİK CÜMLELERİ · DURUM CÜMLELERİ · NESNE DURUMU · SAHNE DÜZENİ · MEKÂN IŞIĞI · ORTAM SESİ · SES KİMLİĞİ · ORTAK GÖRÜNÜM) + §4 çekim satırı + §5 replik saniyeleri. Eklenen her cümle bu malzemedendir; yeni olay, kişi, nesne, ışık kaynağı, ekran, yazı, renk ya da sıfat yok.
> **C01-C06:** planın Görsel ve Video metni **kelimesi kelimesine** aynen durur (tur 1c hâli: referans anahtarı · "from the first frame" silinmiş · vuruş önekleri · `: <line>`). **Ek, planın ardına:** Görsel'de plan metninin (stil cümlesi dahil, yani ORTAK GÖRÜNÜM plan metninin içinde) ardından yeni paragraf = kamera yeri · KİMLİK CÜMLELERİ (kadrajda görünen parçalar birebir) · poz ve bakış · mekân · ışık · kompozisyon;
> Video'da plan metninin ardından, son vuruşun içinde sabit kalanlar cümlesi + ORTAK GÖRÜNÜM sonda. Plan kendi ses cümlesini taşıdığı için ORTAM SESİ eklenmedi (iki ses cümlesi çelişmesin).
> **C07-C12:** plan promptsuzdur; yalnız plan malzemesi. Görsel: referans anahtarı · kadraj + kamera yeri + öznenin yeri · KİMLİK CÜMLELERİ · poz ve bakış · mekân (masa, cam + §3 cam cümlesi ya da kaburgalar) · ışık · kompozisyon · ORTAK GÖRÜNÜM sonda. Video: vuruş başına kamera · özne · ışık · nesne; replik `<SES KİMLİĞİ>: <line>` + "finishes by about X s"; sabit kalanlar; ORTAM SESİ; ORTAK GÖRÜNÜM sonda. Objektif mm yok.
> Prompt gövdesine çekim kodu, referans kodu (A02, K1), başlık satırı, "Clip n of N" YAZILMAZ. Her blok ≤4.300 karakter. Model sesi AÇIK: replikler `: <line>` biçiminde; kadraj dışı yanıt sırasında kadrajdaki kişinin ağzı kapalı.
> **M'ye takılan 2 plan cümlesi** (Silex "speaking seam", Nith "where his calm voice resonates") **kare promptunda kesildi**; referans promptunda plan metni kalır. DERS uyarısı: C04'te plan kelimesi "source-monitor surface" EKRAN deseni (Y8) tetikleyebilir → plan cümlesi, değiştirilmedi.

---

## ROL SÖZLÜĞÜ · MEKÂN IŞIĞI · ORTAM SESİ · SES KİMLİĞİ — Fable §3'e birebir kopyalar; G02-G08 bu bölümü kullanır

```
ROL SÖZLÜĞÜ (C07-C12 ve G02-G08 referans anahtarındaki parantez, birebir):
  1 clerk · 2 military envoy · 3 aquatic envoy · 4 mineral envoy · 5 trade consul · 6 station host · 7 chamber · 8 black hole and station · 9 four fleets.
  NOT: C01-C06'da planın kendi rol kelimeleri çekime göre değişir (C01 "the single foreground alien" · "bronze seat and room geometry" · "distant view"; C04 "the single foreground clerk" …);
  bunlar plan cümlesidir, sözlükle birleştirilmez. Özne adı: gövdede planın adları (Nem · Vekh · Ishra · Silex · Orun · Nith); tutamaç yok.

MEKÂN IŞIĞI (Görsel'de; C01-C06'da plan cümlesi zaten kendi ışığını taşır, ek yazılmaz):
  SALON (iç hacim) — Warm gold side light and cool readable face shadows.   (plan C04; kamera ışığın geldiği yöne bakıyorsa "Warm gold light from the camera side and cool readable face shadows.")
  DIŞ — The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow.   (plan A08 kelimeleri)
  DIŞ DÜNYA (her dış görselde; T18) — Keep one black hole with its lensed golden disk, realistic stable silhouettes.   (plan C03)

ORTAM SESİ (model sesi AÇIK film — aynı mekânın VİDEO promptunda; C01-C06'da plan kendi ses cümlesini taşır, aynen kalır):
  SALON — Sound: quiet chamber ventilation and distant table resonance.   (plan C01 · C04 kelimeleri)
  DIŞ — Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum.   (plan C03 birebir)

SES KİMLİĞİ (model sesi — her replikte aynı kelimeler; plan C01-C06 ses kelimeleri + plan kadro tablosu "Ses" sütunu; konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, öteki yanıt kadraj dışı):
  Nem   — a precise steady adult female voice                                  (plan C04)
  Vekh  — a low rough controlled voice                                          (plan C01)
  Ishra — a clear restrained female voice with a soft resonant quality         (plan C02)
  Silex — a clean, genderless voice with a light harmonic tone, calm and observant   (plan tablosu)
  Orun  — a husky baritone voice, quick and polished, with dry humour          (plan tablosu)
  Nith  — a smooth low male voice; speaks calmly through his gold throat mesh  (plan C05)
  OFFICIAL RELAY — duygusuz, cinsiyetsiz resmî ses; kurguda eklenir, video promptuna yazılmaz (C01'de plan, röleyi "separate off-screen sound layer" diye anar).
  Replik kalıbı: "<ses cümlesi>: <line>"  (plan: "… voice: 'line'" → tek tırnak yerine iki nokta).

KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6 — plan stil cümlesi "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor. SALON ve DIŞ ışığıyla aynı yönde
  (sıcak altın kara delik yansıması, soğuk gölge); C01-C12'de çelişen su/gezegen/ses yok → cümle sahibin, değişmedi.
```

---

## KİMLİK CÜMLELERİ (planın A01-A13 İngilizce cümleleri BİREBİR · C07-C12 Görsel promptunda kadrajdaki parçalar kelime kelime · Fable FILM.md §3 `### KİMLİK CÜMLELERİ`'ne kopyalar)

> Ad gereken yerde cümleden önce ayrı kısa özne cümlesi. Kadrajda olmayan parça yazılmaz. Üç M kaynaklı kesinti: Silex "speaking seam" → "mouth seam" · Nith "where his calm voice resonates" kesildi (Görsel'de konuşma kelimesi hata) ·
> A02 "… dark-red clothing, with a single compact dark blaster holstered at the right hip." virgülde bölünür (kalça görünmeyen kadrajda ilk yarı). Nesne satırları plan numarasıyla (A10-A13; film referansı değil, DERS Y2 rakamlı numaraları sayar).

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Nem · özne | Nem is an adult nonhuman linguistic clerk. |
| 1 | Nem · yüz | Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. |
| 1 | Nem · kemik | Her face has distinctly alien bone geometry, without human ears or hair. |
| 1 | Nem · ceket + işaret | She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. |
| 1 | Nem · alıcı | A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. |
| 1 | Nem · beden | Two arms, stable upright proportions, delicate but practical hands. |
| 2 | Vekh · özne | Vekh is an adult nonhuman military envoy. |
| 2 | Vekh · yüz | Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. |
| 2 | Vekh · beden | His body is upright with two arms and two legs. |
| 2 | Vekh · zırh (kalça görünmeyen kadraj) | He wears bronze formal military armour over dark-red clothing. |
| 2 | Vekh · zırh + blaster (kalça görününce) | He wears bronze formal military armour over dark-red clothing, with a single compact dark blaster holstered at the right hip. |
| 2 | Vekh · alıcı | A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. |
| 3 | Ishra · özne | Ishra is an adult aquatic alien diplomat. |
| 3 | Ishra · yüz | Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. |
| 3 | Ishra · başlık | A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. |
| 3 | Ishra · giysi | Her dark-teal formal suit has pale pearl shoulder edging. |
| 3 | Ishra · alıcı | A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. |
| 4 | Silex · özne | Silex is an adult nonhuman envoy with a stable living-mineral anatomy. |
| 4 | Silex · yüz | A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. |
| 4 | Silex · faset | The facets are continuous biological surfaces, not floating shards. |
| 4 | Silex · pelerin | Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. |
| 4 | Silex · alıcı | A thin separate silver translation receiver rests at the right temple. |
| 4 | Silex · doku | Subtle internal violet translucency, restrained expression, no changing crystal growth. |
| 5 | Orun · özne | Orun is an adult nonhuman trade consul. |
| 5 | Orun · yüz | Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. |
| 5 | Orun · ceket | He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. |
| 5 | Orun · beden | Two arms, substantial but not exaggerated build. |
| 5 | Orun · alıcı | A thin removable silver translation receiver rests at the right temple. |
| 6 | Nith · özne | Nith is an adult nonhuman diplomatic station host. |
| 6 | Nith · yüz | A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. |
| 6 | Nith · baş sırtı | A low two-pronged cranial crest is part of the same stable head. |
| 6 | Nith · ceket | He wears a long ivory formal coat over black inner panels, with restrained gold trim. |
| 6 | Nith · alıcı | A small silver translation receiver remains at his right temple. |
| 7 | Salon · masa + cam | One rigid black hexagonal table stands before a broad panoramic curved window. |
| 7 | Salon · altı koltuk | Exactly six distinct fixed chair positions surround it: the far head chair facing the camera has ivory and black host colours; clockwise from it are bronze-red, teal, a smaller near-side pewter clerk chair, pale silver-violet, and ochre-brown. |
| 7 | Salon · masa donanımı | Discreet personal translation speakers and simple physical controls are built into the table. |
| 7 | Salon · cam manzarası | Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. |
| 7 | Salon · kaburgalar | Dark stone-metal ribs, readable cold shadows, warm disk reflections. |
| 8 | Kara delik | The black-hole shadow is truly dark. |
| 8 | Disk | A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. |
| 8 | İstasyon | The station has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. |
| 9 | Filolar | Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. |
| 9 | Koridor + tıbbi gemiler | They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. |
| A10 | K1 özel ticaret rölesi (Orun'a ait) | a single palm-sized black octagonal body with one pale amber triangular light |
| A11 | K2 bağımsız kayıt taşı (Silex'e ait) | a single flat frosted-purple pentagonal recording slab small enough to rest in one palm |
| A12 | Tercüman alıcısı | a single thin silver strip, a translation receiver and not a life-support part |
| A13 | W1 blaster (Vekh) | a single compact dark blaster holstered at the right hip |

---

## REFERANS PROMPTLARI (yalnız ilk grupta · plan A01-A09 metni birebir; özne başına TEK dosya)

> Plan referansları **tek görünüş**tür (single-subject three-quarter …); hat panel kalıbı (KIMLIK §7 P17, HİPOTEZ) uygulanmadı, plan korundu (NOTLAR KARARLAR). Panel üstünde yazı/etiket yok (plan: "no writing"). Plan metni aynen; bağımlılık yok (KAYNAK satırı yok).
> **Üretim sırası (plan: "Önce altı karakter ve salon, sonra dış kara delik ve filo masterı"):** 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9. Sahip her görseli seçip `ref/` altına `<No>.<AD>_v1.png` adıyla kaydeder;
> yüz, giysi, alıcı tarafı (sağ şakak) ya da koltuk renk sırası değiştiren görsel kullanılmaz, önce o düzeltilir.

### 1.NEM
```
DOSYA     ref/1.NEM_v1.png
PANELLER  tek görünüş (plan A01): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference image of Nem, an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. Plain charcoal background, soft neutral reference lighting, photoreal practical-creature cinema, landscape 16:9, no writing or logos.
```

### 2.VEKH
```
DOSYA     ref/2.VEKH_v1.png
PANELLER  tek görünüş (plan A02): three-quarter (blaster kılıfı sağ kalçada görünür)
```
```text
Create a single-subject three-quarter reference of Vekh, an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing, with a single compact dark blaster holstered at the right hip. A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. Broad calm posture, restrained readable expression. Neutral charcoal reference background, realistic metallic texture, photoreal cinematic alien design, landscape 16:9, no lettering or insignia text.
```

### 3.ISHRA
```
DOSYA     ref/3.ISHRA_v1.png
PANELLER  tek görünüş (plan A03): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of Ishra, an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. Calm intelligent posture. Plain charcoal background, soft neutral light, tactile photoreal science-fiction reference, landscape 16:9, no writing.
```

### 4.SILEX
```
DOSYA     ref/4.SILEX_v1.png
PANELLER  tek görünüş (plan A04): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of Silex, an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central speaking seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. A thin separate silver translation receiver rests at the right temple. Subtle internal violet translucency, restrained expression, no changing crystal growth. Plain charcoal reference backdrop, neutral detailed light, photoreal practical alien cinema, landscape 16:9, no lettering.
```

### 5.ORUN
```
DOSYA     ref/5.ORUN_v1.png
PANELLER  tek görünüş (plan A05): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of Orun, an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. A thin removable silver translation receiver rests at the right temple. His expression is calculating and socially polished rather than monstrous. Plain charcoal reference background, neutral soft lighting, tactile photoreal science-fiction design, landscape 16:9, no writing.
```

### 6.NITH
```
DOSYA     ref/6.NITH_v1.png
PANELLER  tek görünüş (plan A06): three-quarter waist-up
```
```text
Create a single-subject three-quarter waist-up reference of Nith, an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh where his calm voice resonates. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. Upright controlled posture, smooth professional menace, no human face or hair. Charcoal reference backdrop, soft neutral light, photoreal alien political thriller design, landscape 16:9, no lettering.
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

> Not: **Plan pilotu** (C01 iki ses katmanı) ve açılış (ILK_30 §6). Plan promptu aynen; yalnız anahtar cümlesi, "from the first frame" silinmesi, vuruş önekleri ve `: <line>`. **Tur 2 eki:** Görsel'de plan metninin ardına paragraf (Vekh yüz/zırh/alıcı birebir; kalça kadraj altı olduğundan blaster kılıfı cümlesi yazılmadı, plan "hands rest below the crop" der); Video'da son vuruşa sabit kalanlar + ORTAK GÖRÜNÜM.
> R001 Vekh 2,0 s'den 2,0 s (4,0'da biter); OFFICIAL RELAY R002 kurguda (plan: "separate off-screen sound layer"). Plan "a low tense score" korundu (ILK_30 F4 uygulanmadı). BT §A "fire": red gelirse R001 kayda.

### Görsel
```text
Reference 2 (the single foreground alien): use it for Vekh. Reference 7 (chamber): use it for the bronze seat and room geometry. Reference 8 (distant view): use it for the distant view. Tight three-quarter portrait of Vekh seated at the bronze-red position, calm rather than shouting. His rust-red facial armour, two amber eyes, short fixed jaw plates and small silver translation receiver are clearly readable. Through the panoramic window behind him, a large dark black-hole shadow and its bent golden disk are already visible. His hands rest below the crop; the blaster stays holstered. Keep the alien face tactile and the astrophysical object distant and separate. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera stands at the ochre-brown side of the black hexagonal table at eye level and looks across the table toward the bronze-red seat. Vekh sits in the right half of the frame, his head turned in three-quarter so that his right temple faces the lens, his amber eyes directed down the table toward frame-right, off-camera. The soft dark edge of the rigid black hexagonal table crosses the bottom of the frame. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. He wears bronze formal military armour over dark-red clothing. A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. His expression is calm and controlled, his head level and his jaw plates closed, the bronze shoulder armour sitting square beneath the amber eyes. Behind him the broad panoramic curved window fills the background; through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold of the disk reaches the bronze armour and the edge of the jaw plates from behind and from the side, while the cool shadow side keeps the amber eyes and the central breathing seam readable. His face is the sharp plane in the middle ground, the table edge is soft in the foreground, and the window with the black hole is soft and distant behind him. The black-hole shadow is truly dark.
```

### Video
```text
0-2 s: Use a restrained slow push toward Vekh. 2-5 s: He speaks once, with minimal natural jaw-plate movement and a low rough controlled voice: We did not fire first. 5-10 s: After he stops, hold his listening expression and the stable black-hole view. Quiet chamber ventilation and a low tense score. The altered official relay line is a separate off-screen sound layer added after his original utterance, not a second line spoken by Vekh. Vekh's face geometry and short fixed jaw plates, the silver receiver at his right temple, the bronze-red seat and the rigid table edge stay identical throughout; the single black hole with its lensed golden disk stays distant and unchanged in the curved window behind him, and the gold side light keeps the same direction on his bronze armour and rust-red facial armour. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C02 — Suçlama

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C02.png · referans (yükleme sırası, kare üretiminde): ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Açılış (ILK_30 §6): T05 su başlığı; göz asimetrisi/yansıma ve **Ishra'nın ağzı suyun içinden okunuyor mu** kare kapısında bakılır (tasarım boşluğu sahibe, SK4). Plan cümleleri aynen; replik plan sırasıyla ikinci cümlede (~2 s, FILM §5 R003 2,0 s).
> Vuruş sınırı virgülde bölündü ("…translated admission, | then she answers …"). **Tur 2 eki:** Görsel'e Ishra kimlik cümleleri (yüz · başlık · giysi · alıcı) birebir + kamera yeri + ışık; Video'ya sabit kalanlar + ORTAK GÖRÜNÜM.

### Görsel
```text
Reference 3 (the single aquatic envoy): use it for Ishra. Reference 7 (chamber): use it for the teal chair position. Close three-quarter portrait of Ishra inside her same rigid transparent water dome. Her two dark lateral eyes, pearlescent teal skin, short gill fins and constant water level are unchanged. Her separate translation receiver remains in the right external socket. She looks toward Vekh off-camera with controlled disbelief. Reflections are restrained so that the face stays readable; life-support connections remain fixed. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera stands at the ochre-brown side of the black hexagonal table at eye level and looks across the table toward the teal chair position. Ishra fills the centre-right of the frame, turned in three-quarter so that the external socket at the right side of the dome faces the lens, and her gaze is directed toward frame-left, where Vekh sits off-camera. Ishra is an adult aquatic alien diplomat. Pearlescent teal skin, two glossy dark lateral eyes and short symmetrical gill fins make a clearly nonhuman face. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. Ishra sits upright in the teal chair with her shoulders squared toward the table and her head level inside the dome. The sealed shoulder collar and the pale pearl shoulder edging cross the lower frame, and the dark-teal formal suit falls into soft shadow at the frame edge. The water inside the dome is clear and carries one steady bright line at its visible level, and the discreet life-support connections stay small and fixed. Behind her the dark stone-metal ribs of the chamber fall out of focus. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold arrives from the window side at frame-left and edges the dome rim, while the cool shadow side keeps both lateral eyes and the gill fins readable through the water. Her face is the sharp plane in the middle ground; the dome rim and the water level cross the frame as thin bright lines.
```

### Video
```text
0-2 s: Hold the close view. Ishra's eyes narrow slightly as she listens to the translated admission, 2-6 s: then she answers in a clear restrained female voice with a soft resonant quality: Then you came here to boast about it? 6-10 s: Maintain the water dome, water level and fixed life-support geometry. Sound: subtle fluid movement, quiet room tone, no additional speaker. Ishra's face geometry, pearlescent teal skin, short gill fins and the silver receiver in the right external socket stay identical throughout; the sealed shoulder collar, the teal chair and the dark stone-metal ribs behind her stay in place, and the gold light keeps the same direction along the dome rim; the clear water in the dome holds one steady level line while her shoulders and head make only small natural movements. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C03 — Dışarıdaki filolar

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C03.png · referans (yükleme sırası, kare üretiminde): ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png
```

> Not: Açılış (ILK_30 §6): saf manzara değil, tehlike olayı. Diyalog yok. Plan promptu aynen (olumsuz cümleler dahil: NOTLAR KARARLAR); yalnız anahtar cümleleri (Reference 9 anahtarı plan A09'un tıbbi gemi kelimesini taşır, Görsel'in plan cümleleri aynen) ve vuruş önekleri.
> **Tur 2 eki:** Görsel'e dış kimlik (filolar · koridor + tıbbi gemiler · kara delik · disk · istasyon birebir) + DIŞ ışık + taraf cümlesi (DURUM: rust-red frame-left, pearl-white and teal frame-right, istasyon alt sağ üçte); Video'ya sabit kalanlar + ORTAK GÖRÜNÜM.

### Görsel
```text
Reference 8 (the same single black-hole system): use it for the same single black-hole system. Reference 9 (the four stable ship families): use it for the four stable ship families and the few tiny medical craft waiting at the corridor edge. Extreme wide exterior of the separated outer fleet groups facing an open corridor. Rust-red wedge ships are at one side; white-teal fan vessels are opposite, with silver faceted ships and ochre merchant carriers farther out. A few weapon lights on the rust-red ships are beginning to brighten. All ships remain outside the event horizon and away from disk material. The small diplomatic station is a distant silhouette. Keep one black hole with its lensed golden disk, realistic stable silhouettes. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera floats level with the plane of the open corridor and looks along it, so that the rust-red wedge ships hold frame-left and the pearl-white and teal fan vessels hold frame-right, with the open corridor between them running toward the far background. Each group has one clear dominant design family: rust-red wedge warships, pearl-white and teal fan-shaped vessels, silver faceted ships, and ochre ring-shaped merchant carriers. They face one another across a visible open corridor, with a few tiny medical craft waiting at its edge. The four groups lie fully outside the event horizon and outside the hot accretion disk material, separated by wide empty space, and smaller escorts recede as simple silhouettes. The open corridor stays straight and clear, with the few tiny medical craft waiting at its edge near the middle of the frame as small pale points. The black-hole shadow is truly dark. A bright tilted golden accretion disk and its gravitationally lensed upper and lower arcs wrap around the shadow, with one side visibly brighter. The black hole remains one physical object, its shadow in the centre of the far background and the lensed arcs bending above and below it. The station, a distant silhouette in the lower right third, has a compact hexagonal core with six short shielded arms, physical metal geometry and small cold-blue windows. The light is the bright tilted golden accretion disk with its lensed upper and lower arcs, one side brighter, against the truly dark black-hole shadow; it rims the hull edges that face the disk in warm gold, and the weapon lights stay small points along the rust-red hulls. The foreground ships are large and sharp, the formation recedes in overlapping depth, and the shadow and disk form the soft far background.
```

### Video
```text
0-3 s: Use a slow lateral drift through the wide formation. 3-7 s: A few existing rust-red weapon-light strips brighten while all four fleet groups hold their separated positions. 7-10 s: The medical craft remain waiting near the corridor edge. Do not start a major battle or add new ship groups. Sound: restrained ominous score and abstract low-frequency tension as non-diegetic design; no atmospheric engine or explosion sound in vacuum. The four fleet groups, the open corridor, the single black hole with its lensed golden disk and the small station silhouette in the lower right third keep their separation and shapes throughout; the rust-red wedge ships stay at frame-left, the pearl-white and teal fan vessels at frame-right, and the disk keeps its one brighter side. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C04 — Kâtibin itirazı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C04.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan cümleleri aynen. DERS Y8 olasılığı: plan kelimesi "small plain source-monitor surface" (ekran deseni; yazı kilidi planın stil cümlesindeki "without lettering") — kare üretiminde yazı çıkarsa bu cümle suçlanır. Replik plan sırasıyla ikinci cümlede (~2 s, R004 2,0 s).
> R004 Nem; R005 Silex kadraj dışı, kurguda (4,6 s). **Tur 2 eki:** Görsel'e Nem kimlik cümleleri (özne · yüz · kemik · ceket + işaret · alıcı · beden) birebir, oturan (DURUM: C06 öncesi oturur) + kamera yeri + ışık; Video'ya sabit kalanlar + ORTAK GÖRÜNÜM.

### Görsel
```text
Reference 1 (the single foreground clerk): use it for Nem. Reference 7 (chamber): use it for the near pewter chair and table. Medium close view of Nem still at her lower clerk position, her silver temple receiver attached. She has turned from a small plain source-monitor surface toward the council, eyes alert. The high silver cheek ridges, pale lavender-ivory face and narrow vertical mouth seam remain nonhuman and identical. Her hands are near the table, not holding a weapon. Warm gold side light and cool readable face shadows. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera stands at the teal side of the table at eye level and looks toward the smaller pewter clerk chair where Nem sits. She holds the left half of the frame, turned in three-quarter so that her right temple with the receiver faces the lens, her eyes directed toward frame-right, where Vekh and the host sit off-camera. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. Nem sits at the lower clerk position in the smaller chair, her back upright and her shoulders turned toward frame-right as her head lifts. Her narrow vertical mouth seam is closed, and the one small cobalt throat light shows as a small cool point at her throat. The dark-pewter coat falls plainly over her shoulders and the silver receiver tab is the brightest small detail beside her temple. Her gaze is alert and level, and the high silver cheek ridges carry a thin line of warm gold. The edge of the rigid black hexagonal table crosses the lower frame. Behind her the dark stone-metal ribs of the chamber fall out of focus. The gold arrives from the right of the frame and edges her cheek ridges, while the cool shadow side keeps the two long dark-violet eyes readable. Her face is the sharp plane in the middle ground; the table edge and the ribs behind her are soft. Dark stone-metal ribs, readable cold shadows, warm disk reflections.
```

### Video
```text
0-2 s: Use a very small push as Nem lifts her gaze toward Vekh and the host. 2-6 s: She speaks with a precise steady adult female voice: That's not what he said. Keep her mouth motion subtle and preserve the face geometry. 6-10 s: She then listens, holding her position. Sound: close clean character voice, quiet ventilation and distant table resonance. Nem's face geometry, the silver receiver at her right temple, the one small cobalt throat light, the smaller pewter clerk chair, the rigid table edge and the dark ribs behind her stay identical throughout, and the gold light keeps its direction from the right of the frame across her cheek ridges; her hands stay near the table edge, the cool shadow side keeps her two long dark-violet eyes readable, and the table edge stays soft in the foreground. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C05 — Söz hakkı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C05.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan cümleleri aynen (olumsuz "not shouting" ve "no second speaker" dahil). Replik ikinci cümlede (~2 s, R006 2,0 s). R006 Nith. **Tur 2 eki:** Görsel'e Nith kimlik cümleleri (yüz · baş sırtı · ceket · alıcı) birebir + cam ardı + kamera yeri (masanın Nem ucundan) + ışık; Video'ya sabit kalanlar + ORTAK GÖRÜNÜM.

### Görsel
```text
Reference 6 (the single station host): use it for Nith. Reference 7 (chamber): use it for the far ivory-black head chair. Close portrait of Nith seated upright, his polished black face, fixed bone-white central brow, two narrow ice-blue eyes and gold throat mesh unchanged. His silver translation receiver is still at the right temple. Ivory coat and black inner panels are immaculate. He looks down the table toward Nem off-camera. A controlled gold reflection edges his face; the dark room remains spatially stable. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera stands at Nem's end of the table at eye level, a little right of the long axis of the table, and looks down it toward the far head chair. Nith sits centred in the frame, upright, his eyes directed toward frame-left just beside the lens, where Nem sits off-camera. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple, at frame-left. Nith sits upright with his shoulders square and his chin level, the long ivory coat falling in straight lines over the black inner panels, the gold trim catching one thin line of light along the collar. The high back of the ivory and black head chair is visible beside his shoulders. Behind him stands the broad panoramic curved window; through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. The far end of the rigid black hexagonal table reaches the bottom of the frame as a soft dark edge. Warm gold side light and cool readable face shadows: the gold edges one side of his black face and the ivory shoulder, while the cool shadow side keeps the ice-blue eyes and the bone-white brow ridge readable. The room around him is dark and spatially stable, with the window the one bright plane. His face is the sharp plane in the middle ground; the window and the black hole behind him are soft and distant.
```

### Video
```text
0-2 s: Hold the close camera. 2-6 s: Nith makes one small downward head inclination and speaks calmly through his gold throat mesh: The clerk does not address the council. 6-10 s: The menace comes from composure, not shouting. Preserve the fixed facial ridge and crest. Sound: smooth low male voice, a faint official table tone, no second speaker. Nith's face geometry, the silver receiver at his right temple, the ivory coat, the far head chair and the window view of the single black hole stay identical throughout; the gold edge keeps its side of his face and the ivory coat keeps its straight lines, his shoulders stay square beside the high back of the head chair, his hands stay below the crop, and the dark room stays spatially stable with the window as its one bright plane. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C06 — İlk açık suçlama

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C06.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan cümleleri aynen. Kalkma tek ve kontrollü (plan). Replik ikinci cümlede (~2 s, R007 2,0 s). R007 Nem; R008 Nith plan: "off-screen post-production line", kurguda (5,0 s).
> **Tur 2 eki:** Görsel'e Nem kimlik cümleleri birebir + kamera yeri (alçak, Ishra tarafı) + masa cümlesi + ışık; Video'ya sabit kalanlar + ORTAK GÖRÜNÜM.

### Görsel
```text
Reference 1 (the foreground alien): use it for Nem. Reference 7 (chamber): use it for the same near table position. Medium low view of Nem at the beginning of rising from her smaller pewter clerk chair. Both hands lightly brace the broad table edge, the silver receiver still attached. Her face is directed toward Nith at the far end, outside the crop. Gold black-hole light crosses her cheek plates and cobalt throat light. Keep her two arms, formal coat and rigid table geometry stable. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.

The camera stands low at the teal side of the table, close to table height and looking slightly up, with Nem in the centre of the frame and her face turned toward frame-right, where Nith sits off-camera at the far end. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. Nem is half-risen, her weight forward over the table edge and her back straight, the smaller pewter clerk chair still under her as it begins to move back. The dark-pewter coat pulls slightly at her shoulders, the silver receiver tab catches a thin highlight at her temple, and the one small cobalt throat light is a cool point against the warm gold on her cheek plates. One rigid black hexagonal table runs across the lower frame, with discreet personal translation speakers and simple physical controls built into its surface. Behind her the smaller pewter clerk chair stands at the near end, and the dark stone-metal ribs of the chamber fall out of focus beyond it. Warm gold side light and cool readable face shadows: the gold comes from the window beyond Nith, at the right of the frame, and crosses her cheek ridges, while the cool shadow side holds her two long dark-violet eyes readable. Her face is the sharp plane in the middle ground; the table is the crisp lower plane and the ribs are soft depth. Dark stone-metal ribs, readable cold shadows, warm disk reflections.
```

### Video
```text
0-2 s: Use a quiet low-angle camera as Nem completes one controlled rise to her feet. 2-6 s: She addresses Nith with a steady unraised voice: Your translator just declared a war. 6-10 s: Keep the existing chair behind her and the face anatomy intact. Sound: the clean original character voice and a short stillness in the room. Nith's reply is an off-screen post-production line after she finishes. Nem's face geometry, the silver receiver at her right temple, the one small cobalt throat light, the rigid table and the dark ribs behind her stay identical throughout, and the gold light keeps crossing her cheek plates from the right of the frame; the smaller pewter clerk chair stays at the near end, the table edge stays crisp in the lower frame, and the cool shadow side keeps her two long dark-violet eyes readable as she rises. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C07 — İki düşman

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C07.png · referans (yükleme sırası, kare üretiminde): ref/2.VEKH_v1.png · ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan promptsuz; plan çekim cümlesi "İkili / Vekh-Ishra". **SK1/SK2 varsayılanı:** model sesi yalnız Vekh (R009, ~1 s'den); Ishra'nın yanıtı R010 kadraj dışı, kurguda → Ishra arkadan (plan: "öteki kişilerin arkaları"). Oturma: sabit düzen (Vekh saat 2, Ishra saat 4), masanın köşesi üzerinden.
> Ishra arkadan ve hafif sağ yanından (alıcı soketi ve su düzeyi okunur kalır); yüz cümleleri yazılmaz. Kubbe ve su düzeyi videoda sabit; hareket omuzlarda. Kare kapısı: kamera hangi koltuktan bakıyor, cam nerede. Tur 2: kamera yeri (Ishra'nın sağ omzu arkası), masa cümlesi, Vekh beden cümlesi, ışık ve kompozisyon eklendi; Video'ya vuruş başına ışık/nesne ve sabit kalanlar.

### Görsel
```text
Reference 2 (military envoy): take his face, armour and receiver from it. Reference 3 (aquatic envoy): take her dome, suit and receiver socket from it. Reference 7 (chamber): take the bronze-red and teal chair positions and the room geometry from it. Over-the-shoulder two-shot across the corner of the table, the camera at eye level behind Ishra's right shoulder, looking across the table corner toward the bronze-red seat. In the left foreground, Ishra sits at the teal chair position, seen from behind and slightly from her right side, so the external socket and water level stay readable. Ishra is an adult aquatic alien diplomat. A rigid transparent water-filled head dome extends down to a sealed shoulder collar, with a constant visible water level and discreet life-support connections. Her dark-teal formal suit has pale pearl shoulder edging. A small removable silver translation receiver is attached to an external socket at the right side of the dome, physically distinct from the breathing and water systems. At frame-right, in sharp focus, sits Vekh at the bronze-red position, facing the camera in three-quarter view, his amber eyes fixed on Ishra. Vekh is an adult nonhuman military envoy. Broad rust-red facial armour, two amber eyes, short rigid lateral jaw plates and a central dark breathing seam create a clearly alien head. His body is upright with two arms and two legs. He wears bronze formal military armour over dark-red clothing. A thin removable silver translation receiver is fixed at the right temple, separate from his anatomy. His hands rest below the table corner, outside the frame. One rigid black hexagonal table meets the frame as a diagonal corner between them, with discreet personal translation speakers and simple physical controls built into its surface. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold from the window edges Vekh's bronze armour and the rim of Ishra's dome, while the cool shadow side keeps his amber eyes and jaw plates readable. Ishra is the soft dark shape in the near plane, Vekh is the sharp plane in the middle ground, and the window with the black hole is the soft far plane. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-4 s: The camera begins a gentle lateral drift over Ishra's shoulder toward Vekh, who looks at her across the table corner; at about 1 s his jaw plates move and a low rough controlled voice says: I denied the attack. He finishes by about 3 s and his mouth closes, the gold window light resting on his bronze armour and the table corner staying crisp. 4-7 s: Her shoulders draw back as she leans away, the dome and its water level staying fixed, while Vekh's mouth stays closed and his amber eyes stay on her; the drift continues and the gold light slides slowly along the dome rim. 7-10 s: The drift continues; Vekh's amber eyes stay fixed on her while her shoulders turn slightly away from him, the dome and its water level still fixed, and the gold light edges his bronze armour. Vekh's face geometry, the silver receiver at his right temple, the receiver in the external socket at the right side of Ishra's dome, the bronze-red and teal chairs, the table corner and the single black hole in the window stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C08 — Makinenin otoritesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C08.png · referans (yükleme sırası, kare üretiminde): ref/6.NITH_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan promptsuz; çekim cümlesi "Yakın / Nith. Nith resmî sistemin tarafsızlığını savunur." C05'ten farklı kadraj: sağ önden üç çeyrek. R011 Nith; R012 Ishra kadraj dışı, kurguda. Eller kadrajda değil. Tur 2: kamera yeri (Silex tarafı, göz hizası), duruş ve ışık/kompozisyon eklendi; Video'da vuruş başına ışık/nesne + sabit kalanlar.

### Görsel
```text
Reference 6 (station host): take his face, brow ridge, throat mesh, crest and coat from it. Reference 7 (chamber): take the far ivory-black head chair, the panoramic window and the room geometry from it. Close three-quarter portrait of Nith seen from his right front, the camera at eye level on the pale silver-violet side of the table, with Nith seated upright at the far head chair in the centre-right of the frame. Nith is an adult nonhuman diplomatic station host. A polished jet-black face has one fixed bone-white central brow ridge, two narrow ice-blue eyes and a discreet gold throat mesh. A low two-pronged cranial crest is part of the same stable head. He wears a long ivory formal coat over black inner panels, with restrained gold trim. A small silver translation receiver remains at his right temple. His head is turned slightly toward frame-left, his ice-blue eyes level. He sits upright, his shoulders square and his chin level, the high back of the ivory and black head chair visible beside his shoulders. The cranial crest rises low above the brow ridge and the gold throat mesh shows as a discreet band under the polished jaw. The long ivory coat falls in straight lines over the black inner panels, and the restrained gold trim catches one thin line of light at the collar. His expression is composed and controlled, authority without anger, and the ice-blue eyes are the brightest cool points in the dark face. His hands are below the crop, and the rigid black hexagonal table reaches the bottom of the frame as a soft dark edge. The panoramic window stands behind him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. A controlled gold reflection edges one side of his face. Warm gold side light and cool readable face shadows: the gold from the window rims the ivory coat and the crest, while the cool shadow side holds the ice-blue eyes and the bone-white brow ridge readable. The room around him is dark and spatially stable, with the window the one bright plane. His face is the sharp plane in the middle ground, and the window with the black hole is soft and distant behind him. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-5 s: The camera begins a slight drift toward Nith as he lifts his chin a little; at about 1 s he speaks calmly through his gold throat mesh in a smooth low male voice: The relay has no nation. It cannot take sides. He finishes by about 5 s, his head steady and his ice-blue eyes level, the gold reflection resting along one side of his black face. 5-8 s: His mouth closes and the gold throat mesh is steady; his eyes move toward frame-right while the gold reflection shifts along his face and the window behind him stays soft. 8-10 s: The drift eases closer, his brow ridge and crest remaining fixed and a thin line of gold light catching the trim of his ivory coat. Nith's face geometry, the silver receiver at his right temple, the far ivory-black head chair and the single black hole in the window stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C09 — Kimin onayı?

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan promptsuz; çekim cümlesi "Yakın / Nem. Nem sertifikalı kayıt levhasından Nith'e döner." Nem **ayakta** (plan: C06 sonrası çoğunlukla ayakta). Levha: `a small plain record plate lying flat on the table in front of her` (yazı yok). R013 Nem; R014 Nith kadraj dışı, kurguda. Tur 2: kamera yeri (Ishra tarafı, hafif alttan), masa cümlesi, duruş ve ışık eklendi; Video'ya sabit kalanlar.

### Görsel
```text
Reference 1 (clerk): take her face, coat and receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Close three-quarter portrait of Nem standing, seen from her right front by a camera slightly below eye level on the teal side of the table. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. She stands at her near position in the left half of the frame, the smaller pewter clerk chair behind her, her head bowed toward a small plain record plate lying flat on the table in front of her, both hands resting on the table edge. Her shoulders are level and her back is straight, the dark-pewter coat falling plainly from her shoulders, and the one small cobalt throat light shows as a cool point at her throat. Her narrow vertical mouth seam is closed, and the silver receiver tab is a small bright detail at her right temple, lit by the same gold. The record plate is plain and unmarked, its surface catching a faint warm reflection. One rigid black hexagonal table crosses the lower frame, with discreet personal translation speakers and simple physical controls built into its surface beside the plate. Behind the chair the room falls into soft depth. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold arrives from the right of the frame and crosses her cheek ridges and the silver receiver, while the cool shadow side keeps her two long dark-violet eyes readable. Her face is the sharp plane, the plate and the table edge are crisp in the lower plane, and the chair and ribs are soft depth. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: The camera begins a slight drift in as Nem raises her head from the plain record plate in front of her and turns toward the far end of the table; at about 1 s she speaks in a precise steady adult female voice: Who certified it? 2-5 s: She finishes at about 2 s and her mouth closes; her head settles toward the far end of the table and her shoulders square, her hands resting on the table edge and the record plate lying flat in front of her. 5-7 s: The drift continues; the gold side light moves across her cheek ridges and her silver receiver while the one small cobalt throat light keeps its glow. 7-10 s: Her eyes stay level as the drift eases closer and her shoulders settle a fraction. Nem's face geometry, the silver receiver at her right temple, the smaller pewter clerk chair behind her and the black table edge stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C10 — Tüccarın küpü

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası, kare üretiminde): ref/5.ORUN_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K1 kurulumu** (A10). T01 el-nesne: K1 **açık avuçta** başlar (parmak kavraması yok), video avucu indirir, K1 masaya (Orun'un koltuğunun önüne) oturur, avuç kayar; bırakma eylemi birincil kalır. YEDEK (planın kendi çözümü: "karmaşık parmak hareketi gerekirse kesmeyle sadeleşir"): kare K1'i masada gösterir, video yalnız kamera + konuşma.
> Kare kapısı: el + nesne ayrılıyor mu · kamera hangi koltuktan bakıyor, cam nerede. R015 Orun; R016 Vekh kadraj dışı, kurguda. K1 sağ elde (plan taraf vermez; sonraki Orun çekimleri aynı eli kullanır). Tur 2: kamera yeri (Silex tarafı), masa cümlesi, duruş ve ışık eklendi; Video'da vuruş başına ışık/nesne ve sabit kalanlar.

### Görsel
```text
Reference 5 (trade consul): take his face, coat and receiver from it. Reference 7 (chamber): take the ochre-brown chair position, the table and the room geometry from it. Medium view of Orun seen in three-quarter from the front, the camera at eye level on the pale silver-violet side of the table, with Orun seated at the ochre-brown chair position behind the black hexagonal table in the left half of the frame, his amber eyes directed toward the table centre at frame-right. Orun is an adult nonhuman trade consul. Layered moss-green bark-like facial plates, two horizontal amber eyes and a broad folded lower jaw create an unmistakably alien face. He wears an expensive ochre-brown formal coat with dark metallic edging and a small rigid collar. Two arms, substantial but not exaggerated build. A thin removable silver translation receiver rests at the right temple. His right forearm extends from his sleeve over the table in front of his seat, and on his open right palm, a hand's width above the table surface, rests a single palm-sized black octagonal body with one pale amber triangular light. Orun sits with his shoulders relaxed and his back easy against the ochre-brown chair, the ochre-brown coat with its dark metallic edging and small rigid collar falling in broad folds. His expression is calculating and socially polished. The pale amber triangular light is the one small warm point on the dark body, facing the lens. The rigid black hexagonal table crosses the lower frame, with discreet personal translation speakers and simple physical controls built into its surface. The panoramic window curves behind and beside him. Through the window, the same distant supermassive black-hole shadow and lensed golden accretion disk are visible from outside the event horizon. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold from the window edges his ochre-brown shoulder and the black octagonal body, while the cool shadow side keeps the amber eyes and the folded lower jaw readable. His face is the sharp plane in the middle ground, the palm with the octagonal body is the crisp near plane, and the window with the black hole is soft behind him. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-3 s: The camera begins a gentle drift toward Orun as his open right palm, carrying the palm-sized black octagonal body, lowers toward the table; at about 1 s he speaks in a husky baritone voice, quick and polished, with dry humour: Every delay costs money. Shall we argue more efficiently? 3-7 s: The palm lowers until the octagonal body rests flat on the table surface in front of his seat with its pale amber triangular light plainly visible, and the palm slides away from it while he finishes the sentence by about 5 s; the gold window light glints along the table edge and the dark body. 7-10 s: His hand withdraws to the table edge and his mouth closes; the pale amber light stays lit beside his hand as the drift eases closer and his amber eyes move along the table. Orun's face geometry, the silver receiver at his right temple, the ochre-brown chair, the shape of the black octagonal body and the single black hole in the window stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C11 — Silinen şey

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası, kare üretiminde): ref/1.NEM_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: Plan promptsuz; çekim cümlesi "Yakın / Nem. Nem tartışmayı tek eksik sözcüğe indirir." Nem ayakta. C09'dan farklı kadraj: masanın karşı ucundan karşıdan; ışık kamera tarafından. Ellerle jest yok (T01 riski). R017 Nem; R018 Silex kadraj dışı, kurguda. Tur 2: kamera yeri, masa cümlesi, duruş ve ışık eklendi; Video'ya vuruş başına ışık ve sabit kalanlar.

### Görsel
```text
Reference 1 (clerk): take her face, coat and receiver from it. Reference 7 (chamber): take the smaller pewter clerk chair, the table and the room geometry from it. Close portrait of Nem standing, seen from the far end of the table looking down it toward her, the camera at eye level with her face. Nem is an adult nonhuman linguistic clerk. Matte pale-lavender and ivory facial plates form a narrow face with high silver cheek ridges, two long dark-violet eyes, and a small vertical mouth seam. Her face has distinctly alien bone geometry, without human ears or hair. She wears a restrained dark-pewter clerk's coat with one small cobalt throat light. A thin separate silver translation receiver tab rests at her right temple; it is removable and is not a breathing device. Two arms, stable upright proportions, delicate but practical hands. She stands at her near position in the centre of the frame, her eyes steady on the camera, her right temple with the receiver at frame-left, both hands resting on the table edge below the crop. Her shoulders are level and her back straight, the dark-pewter coat falling plainly from her shoulders. The narrow vertical mouth seam is closed and her expression is steady and controlled. The long dark-violet eyes meet the lens, and the high silver cheek ridges catch the gold. Her gaze is level and unhurried, and the dark-pewter coat shows a thin line of warm gold along the shoulder. The near end of the rigid black hexagonal table spreads across the bottom of the frame as a soft dark edge, with discreet personal translation speakers and simple physical controls built into its surface. Behind her is the smaller pewter clerk chair. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold light from the camera side and cool readable face shadows: the gold falls evenly across her cheek ridges and the one small cobalt throat light, while the cool shadow side gathers under her chin and along the narrow vertical mouth seam. Her face is the sharp plane in the centre, the table edge is soft in the foreground, and the chair and ribs are soft depth. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-6 s: A gentle push begins on Nem as she stands looking straight down the table; at about 1 s she speaks in a precise steady adult female voice: One word vanished. Not. Everything after it became a confession. She goes on with her chin lifting slightly and her eyes steady, and finishes by about 5 s; the gold light from the camera side rests on her cheek ridges and the cobalt throat light holds its glow. 6-8 s: Her mouth closes; she lets out a quiet breath and her shoulders settle a fraction while the push continues. 8-10 s: The gold light shifts across her cheek ridges as the push eases to a close view. Nem's face geometry, the silver receiver at her right temple, the smaller pewter clerk chair behind her and the black table edge stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

## C12 — Test önerisi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası, kare üretiminde): ref/4.SILEX_v1.png · ref/7.ACCORD_CHAMBER_v1.png
```

> Not: **K2 kurulumu** (A11). T01 aynı yöntem: levha **açık sağ avuçta** başlar, avuç iner, levha masaya (Silex'in koltuğunun önüne) oturur; bırakma eylemi birincil, YEDEK planın kendi çözümü (C10 ile aynı). K2 ↔ C10'daki K1 birbirine dönüşmez (beşgen levha ↔ sekizgen gövde).
> Kare kapısı: el + levha ayrılıyor mu · levha kenarı ametist yüzden ayrışıyor mu. R019 Silex; R020 Nith kadraj dışı, kurguda. Silex'in sağ eli (C23'te K2 aynı eliyle alınır). Tur 2: kamera yeri (Ishra tarafı), masa cümlesi, duruş ve ışık eklendi; Video'da vuruş başına ışık/nesne ve sabit kalanlar.

### Görsel
```text
Reference 4 (mineral envoy): take its face, facets, mantle and receiver from it. Reference 7 (chamber): take the pale silver-violet chair position, the table and the room geometry from it. Close three-quarter portrait of Silex seated behind the black hexagonal table at the pale silver-violet chair position, seen from the front with the right temple toward the camera, the camera at eye level on the teal side of the table, Silex in the left half of the frame. Silex is an adult nonhuman envoy with a stable living-mineral anatomy. A frosted amethyst face has a few broad fixed facets, two dark faceted eyes and a narrow central mouth seam. The facets are continuous biological surfaces, not floating shards. Two arms and a calm upright body wear a simple pale-silver diplomatic mantle. A thin separate silver translation receiver rests at the right temple. Subtle internal violet translucency, restrained expression, no changing crystal growth. Silex's right forearm extends from the pale-silver sleeve over the table in front of Silex's seat, and on the open right palm, a hand's width above the table surface, rests a single flat frosted-purple pentagonal recording slab small enough to rest in one palm. Silex sits calm and upright, shoulders level, the pale-silver diplomatic mantle falling in simple folds. The broad facets of the frosted amethyst face carry subtle internal violet translucency, and the narrow central mouth seam is closed. The pentagonal outline of the slab reads clearly against the dark table surface. The rigid black hexagonal table crosses the lower frame, with discreet personal translation speakers and simple physical controls built into its surface. Behind Silex the dark stone-metal ribs of the chamber fall out of focus. Dark stone-metal ribs, readable cold shadows, warm disk reflections. Warm gold side light and cool readable face shadows: the gold arrives from the right of the frame and catches the broad facets and the edge of the slab, while the cool shadow side keeps the two dark faceted eyes and the narrow central mouth seam readable. The face is the sharp plane in the middle ground, the palm with the pentagonal slab is the crisp near plane, and the ribs are soft depth. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

### Video
```text
0-2 s: The camera begins a gentle drift toward Silex as the open right palm, carrying the flat frosted-purple pentagonal recording slab, lowers toward the table; at about 1 s the narrow central mouth seam moves and Silex speaks in a clean, genderless voice with a light harmonic tone, calm and observant: Then test a sentence none of us can mistake. 2-5 s: The palm lowers until the slab rests flat on the table surface in front of Silex's seat and the palm slides away from it; Silex finishes the sentence by about 5 s, the gold light catching the edge of the slab. 5-8 s: The hand withdraws to the table edge and the mouth seam closes. 8-10 s: The facets on the face catch the gold light as the drift eases closer. Silex's face geometry and facets, the silver receiver at the right temple, the pale silver-violet chair, the shape of the pentagonal slab and the dark ribs behind stay identical throughout. Sound: quiet chamber ventilation and distant table resonance. Photoreal live-action alien political thriller, widescreen 16:9, restrained anamorphic lens character, fine 35mm film grain, readable expressive creature faces, cold charcoal and pewter shadows, warm gold black-hole reflections, tactile practical materials. Clean image without lettering, logos or watermarks.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde ön plan repliği model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** plan görselleri GPT Image, videoları görselden video 10 s ile hedefler ("kullanılan arayüzün mevcut oran, süre ve ses seçenekleri uygulanır"). Flow'da Görsel modu aynı promptla ve aynı referans sırasıyla kullanılabilir. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9.
> **C01 denemesi P14 (10 s klip süresi) + P18 (model sesi) ölçümüdür.** Omni kredisi BİLİNMİYOR (P11).
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız referans sayfası ve kare üretiminde, kare promptunun kendi sırasıyla yüklenir.
> **Sıra (plan pilotu):** 1-9 referans sayfaları → **C01 kare + video (plan pilotu)** → G06 C61 · G07 C79 (plan pilotu, kendi dosyalarında) → **dur: Fable + devamlilik kare kararı** → C02-C03 (açılış) → C04-C12.
> Referanslar onaylanmadan kare, kare onaylanmadan video üretilmez. **Kare kapısı** (ILK_30 §6 + G01 maddeleri): filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması / göz asimetrisi · kimlik kayması ·
> **Ishra'nın ağzı suyun içinden okunuyor mu** (C02 ve Ishra'nın konuştuğu her çekim) · **el + nesne ayrılıyor mu, levha kenarı ametist yüzden ayrışıyor mu** (C10 C12) · **kamera hangi koltuktan bakıyor, cam nerede** (C01 C07 C10).
> **Ses:** model sesi (ağız kadrajda) R001 · R003 · R004 · R006 · R007 · R009 · R011 · R013 · R015 · R017 · R019 (C01-C02 · C04-C12; C03 yok); kurguda R002 (röle) · R005 · R008 · R010 · R012 · R014 · R016 · R018 · R020.
> Dış klip C03: klibin sesi yalnız soyut skor (T13); yatak Y2 kurguda. Şiddet kelimeli model sesi: C01 "fire" (red gelirse R001 kayda).

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
| 11 | C01 | `ham/C01_d1.mp4` | Frames to Video | kare/C01.png · **plan pilotu: P14 + P18 ölçümü** | 2 | |
| 12 | C02 kare | `kare/C02.png` | Görsel | ref/3.ISHRA_v1.png · ref/7.ACCORD_CHAMBER_v1.png (bu sırayla) · **AÇILIŞ** (pilot kararından sonra) | 2 | |
| 13 | C03 kare | `kare/C03.png` | Görsel | ref/8.BLACK_HOLE_STATION_v1.png · ref/9.FOUR_FLEETS_v1.png (bu sırayla) · **AÇILIŞ** | 2 | |
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

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · tur 2)

> Q1 (tüm çekimler): kolda/göğüste işaret yok; Nem'in boğaz ışığı A01 cümlesiyle ("one small cobalt throat light") C04 · C06 · C09 · C11'de birebir yazılı (merkez boğaz → taraf yok; `the only marking` plan dışı olduğundan yazılmadı, DERS Y1 tetiklenmez).
> Q3 (tüm çekimler): ORTAK GÖRÜNÜM "cold charcoal and pewter shadows, warm gold black-hole reflections" ışık/yansıma taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` (dosya başında); çekimle çelişen su/gezegen/ses yok. Tur 2'de aynı cümle Video sonlarına da girdi (sahip kararı); sesle çelişmez (görsel cümlesi).
> Q5 (tüm çekimler): `plume · smoke · drip · wet · bubbles` yok; Ishra'nın başlığındaki su plan gereği katı hâl ("constant visible water level"); C03'te silah ışığı = lamba şeridi.
> Q6 (tüm çekimler): ekran ya da gösterge adıyla yazılmadı; tek istisna plan kelimesi C04 "small plain source-monitor surface" (plan cümlesi, değiştirilmedi; yazı kilidi ORTAK GÖRÜNÜM'ün "without lettering" cümlesi).
> Q7 (tüm çekimler): her `Reference n` yalnız o tek görünüşte görüneni istiyor (yüz, giysi, alıcı, koltuk, kara delik, tıbbi gemiler).
> Q8 (tüm çekimler): model sesi AÇIK film; Video'daki ses kelimeleri plan (C01-C06) ya da ORTAM SESİ + SES KİMLİĞİ (C07-C12); zıt iki istek yok (kadraj dışı yanıt sırasında kadrajdaki ağız kapalı, C07 · C08 · C09 yazılı).
> **Uzunluk (karakter, ölçülmüş; hedef Görsel 2.400-3.200 · Video 1.000-1.500 · tavan 4.300):** son sütunun solundaki "Görsel kr · Video kr" sütununda, ±100 hassasiyetle (C01-C06 Görsel iki paragrafın toplamı).

| Çekim | Düzeltilen sorular (1-8) | Görsel kr · Video kr | Bilerek bırakılan + gerekçe |
|:--:|---|:--:|---|
| C01 | 2 (Vekh yüz · zırh · alıcı birebir eklendi) · 4 (cam ardı + kaburgalar) | ≈2.600 · ≈1.150 | Plan metni aynen; Q2: beden ve blaster cümlesi yazılmadı (kalça ve eller kadraj altı, plan "hands rest below the crop"). Plan "a low tense score", röle cümlesi, "calm rather than shouting" korundu |
| C02 | 2 (Ishra yüz · başlık · giysi · alıcı birebir) · 4 (Ishra'nın arkası: kaburgalar) | ≈2.700 · ≈1.100 | Plan "Hold the close view" ilk vuruşta; "subtle fluid movement" + "no additional speaker" plan; DERS Y2 plan gerekçesi |
| C03 | 2 (filolar · koridor · kara delik · disk · istasyon birebir) · 4 (dış plan: arka = disk ve kara delik) | ≈2.900 · ≈1.050 | Plan olumsuz cümleleri ("Do not start a major battle…", "no … explosion sound in vacuum") ve filo içinden kamera korundu |
| C04 | 2 (Nem altı parça birebir) · 4 (Nem'in arkası: kaburgalar) | ≈2.500 · ≈1.100 | Plan "source-monitor surface" (Q6, DERS Y8 olasılığı) ve "not holding a weapon" |
| C05 | 2 (Nith yüz · baş sırtı · ceket · alıcı birebir) · 4 (cam + kara delik Nith'in arkasında) | ≈2.700 · ≈1.150 | Plan "not shouting", "no second speaker" korundu |
| C06 | 2 (Nem altı parça birebir; masa donanımı) · 4 (sandalye + kaburgalar) | ≈2.700 · ≈1.100 | Eller masada kalkış plan cümlesi |
| C07 | 2 (Ishra arkadan: yüz cümleleri çıkarıldı · Vekh beden cümlesi eklendi) · 4 (cam Vekh'in arkasında ve yanında; Ishra'nın arkası kamera) · 8 (kubbe/su düzeyi sabit; Vekh'in ağzı yanıt sırasında kapalı) | ≈3.000 · ≈1.450 | SK1/SK2 varsayılanı (sahip cevabı bekler); referans tek görünüşlü (arka görünüş yok, plan kararı) |
| C08 | 4 (pencere ve kara delik Nith'in arkası) · 8 (yanıt sırasında ağız kapalı, boğaz ağı sabit) · Nith "where his calm voice resonates" kesildi (M) | ≈2.600 · ≈1.150 | Eller kadraj altı |
| C09 | 2 (salon kimlik parçaları: masa donanımı · kaburgalar) · 4 · 6 ("sertifikalı kayıt levhası" → `a small plain record plate`, yazı yok) · 8 (yanıt sırasında ağız kapalı) | ≈2.500 · ≈1.250 | Levha biçimi plan dışı (round vb. eklenmedi) |
| C10 | 2 (K1 biçim + ölçü + taraf; masa donanımı) · 4 (cam arkasında ve yanında) | ≈2.600 · ≈1.350 | T01 el-nesne: açık avuç + YEDEK = planın kendi çözümü; K1 koltuğun önünde (merkez C78'de) |
| C11 | 2 (kaburga cümlesi · masa donanımı) · 4 (Nem'in arkası: sandalye) · ışık "from the camera side" | ≈2.500 · ≈1.150 | Ellerle jest yok (T01) |
| C12 | 2 (K2 biçim + ölçü + taraf; masa donanımı) · 4 (arka: kaburgalar) | ≈2.600 · ≈1.250 | "speaking seam" → "mouth seam" (M); K2 Silex'in koltuğunun önünde |
