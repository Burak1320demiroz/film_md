# 🖼️ MOONMOTHER — Pilot (faz 3p): C01 · C06 · C20

> Yazan: goruntu-yonetmeni (pilot modu, 16.10.2026). Denetleyen: devamlilik (kare) · teknik-danisman (pilot).
> Prompt gövdesine çekim kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Üretim yolu (FILM.md künye URETIM): **GPT Image** (referans sayfaları + başlangıç kareleri) → **Gemini Omni 1.1 Flash** (10 s video, Gemini uygulaması).
> Omni'ye yalnız onaylı tek başlangıç karesi gider (`kare/Cxx.png`); panel sayfası Omni'ye girdi olmaz (GPT_IMAGE_OMNI §4, §7). Ayrı başlangıç/bitiş karesi yok → zincir yok.
> Model sesi KAPALI: planın "Sound:" satırları ve "Environmental sound and nonverbal alien calls only…" kuyruğu video promptlarına GİRMEZ (ses F4'te kurulur).
> Kaynak: `FILM.md` §3-§4 · `ODA/F3_yonetmen_2.md` §4 (KİMLİK CÜMLESİ GİRDİSİ · F5'E HATIRLATMA · PİLOT GİRDİSİ) · `ODA/SAHIP_PLANI.md` (referans, kare, video promptları) ·
> `GPT_IMAGE_OMNI_KILAVUZU` · `KIMLIK_VE_REFERANS_KILAVUZU` · `UZAY_FIZIGI_GORUNTU_KILAVUZU` · `PROMPT_HATA_ATLASI` · `ILK_30_SANIYE_KILAVUZU` §6 · `FLOW_GERCEKLERI` Ek 2-3.
> Kelime kararları (F3 TD B15, BILINEN_TUZAKLAR §A/§C): `body`, `wound(ed)` ve büyük harfli KHEV/ORU etiketi hiçbir promptta yok; kemer `smooth parallel vertical grooves … no symbols`;
> ölçüler sayıyla değil kadrajla (Oru Khev'in önkolundan kısa; alt çıkıntı Khev boyunun iki katı aşağıda); mavi karın ışığı yalnız referans sayfasında (kare promptlarında anılmaz).

---

## KİMLİK CÜMLELERİ

> FILM.md §3 `### KİMLİK CÜMLELERİ` tablosuna **birebir** taşınır (Fable). Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz
> (Khev · Oru · the mother manta). No = §3 film geneli referans numarası. Her cümlede sayı + taraf + konum, işaretlerde `the only …`. `body` kelimesi yok.

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | baş ve yüz (önden, ¾) | Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. |
| 1 | baş ve omuzlar (arkadan) | Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. |
| 1 | gövde ve uzuvlar | Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. |
| 1 | eller | Each of Khev's hands has four thick digits in deep-indigo skin. |
| 1 | sol kaval — SAĞLAM (C01-C13) | Khev's left shin plate is one smooth unbroken ivory plate. |
| 1 | sol kaval — ÇATLAK (C14-C24) | Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. |
| 2 | gövde ve boy | Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. |
| 2 | baş ve yüz (önden, ¾) | Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. |
| 2 | sol yüzgeç çentiği | Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. |
| 2 | yüzgeç durumu: kucakta-canlı (C15-C23) | Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. |
| 2 | kucak duruşu | Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso. |
| 2 | arkadan siluet | Seen from behind, Oru shows a blunt rounded head with one shallow crescent forehead crest above two broad winglike fins. |
| 3 | baş zırhı | The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. |
| 3 | göz (sol) | She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. |
| 3 | üç ışık | Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. |
| 3 | yüzgeçler ve kuyruk | She has two immense silver-blue pectoral fins and one thin tapering tail. |
| 3 | sol yüzgeç ucu (C19-C24) | Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. |
| 4 | kemer | A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. |
| 4 | kemer ağzı ve gölge sınırı | Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. |
| 4 | teras ve geçit | The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. |
| 4 | alt çıkıntı | The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. |
| 4 | çıkıntı yüksekliği (yalnız geniş planlar) | The lower ledge lies about twice Khev's height below the end of the causeway. |
| 4 | yüzgeç yanında (C19-C22) | The mother manta's cupped fin tip rests almost level with the ledge, separated from the rock by a narrow gap, and the water beneath the fin lies flat. |
| 4 | gök ve ufuk (her dış çekim) | A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. |
| 4 | ışık (her dış çekim) | The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. |

```
ORTAK GÖRÜNÜM (öneri; ışık ve olumsuz yazı kilidi çıkarıldı, DERS Y6):
  Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

ORTAK GÖRÜNÜM ÖNERİSİ — gerekçe: FILM.md §3'te ORTAK GÖRÜNÜM satırı yok. Planın ortak cümlesi (`… cold indigo and teal night light, small amber bioluminescent accents … Clean image without lettering, logos, or watermarks.`)
**ışık** taşıyor (DERS Y6: ışık mekân cümlesine gider → yukarıda 4 · "ışık" satırı, `warm colour only from amber bioluminescence` dahil) ve **olumsuz yazı kilidi** taşıyor (hat: olumsuz blok yazılmaz,
`lettering` kelimesinin kendisi kadraja basılabilir, BILINEN_TUZAKLAR §C → olumlu karşılığı `plain unmarked surfaces`). Kalan: kimlik/stil/doku. Üç Görsel ve üç Video promptunun sonunda bu cümle birebir.
Fable bu cümleyi §3'e `ORTAK GÖRÜNÜM` satırı olarak eklerse prompt sonları zaten aynıdır; değiştirirse altı prompt sonu birebir güncellenir.
KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6 (Fable'a not) — planın kendi cümlesi ışık ve olumsuz kilit taşıyor; sahip planın cümlesini istiyorsa Y6 uyarısı ve yazı-kilidi riski bilinçle kabul edilir.

---

## REFERANS PROMPTLARI (özne başına TEK sayfa · yalnız pilot çekimlerinin referansları = dördü de)

> Sayfa üstünde yazı, etiket, ok yok. Paneller arasında boşluk. Aşağıdaki panel adları çekim promptlarındaki rol cümleleriyle aynı sözcüklerle yazıldı
> (sayfada etiket olmadığı için panel **içeriğiyle** adlandırılır). Üretim sırası: 1 → 2 → 3 (ref 2 eklenir) → 4 (ref 3 eklenir; yalnız fin paneli için).
> Her referans yeni sohbette üretilir; çıktının pikseli ölçülür (16:9 değil, sayfa oranı serbest). Onaylanan dosya `ref/` altına sürüm adıyla kaydedilir.

### 1.KHEV
```
DOSYA     ref/1.KHEV_v1.png
PANELLER  8: önden tam boy · sağ yandan tam boy (digitigrad bacak, topuk havada) · arkadan tam boy (omuz plakaları) · yüz yakın ¾ (baş-omuz) ·
          ön kol + el yakın · çömelme duruşu · sol kaval SAĞLAM yakın · sol kaval ÇATLAK yakın (amber parıltı)
```
```text
A single reference sheet on a plain mid-grey background, even soft studio light from the front-left, no text anywhere. The same alien biped, Khev, appears in eight panels arranged in two rows of four with clear gaps between the panels. Top row, left to right: a full-length front view, standing; a full-length view from his right side, showing the digitigrade leg line with the heel raised; a full-length back view, showing the shoulder plates; head and shoulders in three-quarter view, showing the face. Bottom row, left to right: forearm and hand in close view; a crouching pose with both digitigrade legs folded; a close view of the left shin plate, smooth and unbroken; a close view of the same left shin plate carrying one diagonal crack with a faint amber glow inside it. Every panel shows only Khev, in identical light and the same proportions. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Each of Khev's hands has four thick digits in deep-indigo skin. In the first seven panels Khev's left shin plate is one smooth unbroken ivory plate. In the eighth panel only, Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Photoreal creature design, natural skin and chitin texture, neutral reference lighting.
```

### 2.ORU
```
DOSYA     ref/2.ORU_v1.png
PANELLER  8: sol ¾ süzülürken iki yüzgeç açık · üstten · yandan alçak (ince yarı saydam karın, soluk mavi iç ışık YALNIZ burada) · yüz yakın ·
          sol yüzgeç arka kenarı yakın (V çentik) · DURUM yatık (sol yüzgeç ayrık, ışıklar zayıf) · DURUM kucakta-canlı (sağ yüzgeç açık, sol yarım açık-sarkık, ışıklar eşit) · kucak duruşu
```
```text
A single reference sheet on a plain mid-grey background, even soft studio light from the front-left, no text anywhere. The same small alien creature, Oru, appears in eight panels arranged in two rows of four with clear gaps between the panels. Top row, left to right: a left three-quarter view, hovering with both fins spread open; a view from directly above, showing the crescent forehead crest, both fins and the thin tail; a low side view showing the thin translucent belly with a faint pale-blue glow inside it; a close view of the face. Bottom row, left to right: a close view of the trailing edge of the left fin; Oru lying on dark stone with its left fin held away from its torso at a fixed angle it cannot open from and its three amber lights weak and uneven; Oru hovering upright with its three amber lights equally bright, its right fin spread open and its left fin half open and drooping at a fixed angle; Oru held upright in a cradled posture, head raised, belly turned toward a flat vertical surface behind it, both fins half closed against its torso. Every panel shows only Oru, in identical light and the same proportions, a small juvenile small enough to rest on a person's forearm. Oru is a juvenile celestial manta with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. In the seventh panel only, Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Photoreal creature design, delicate and anatomically stable, neutral reference lighting.
```

### 3.ANNE
```
DOSYA     ref/3.ANNE_v1.png
EKLE      ref/2.ORU_v1.png
PANELLER  9 (3×3): tam boy sol profil · tam boy ¾ önden (baş kameraya, sol yan kameraya) · "ay" biçimli baş, bulut ardında, göz kapağı dar aralık · aynı baş, göz TAM AÇIK ·
          sol göz yakın, ışıklar SÖNÜK · sol göz yakın, ışıklar YANIK · sol yüzgeç ucu yakın (çanak) · yüksek açı arkadan-sol üstten · uzak baş (ufukta, ayrıntısız)
```
```text
Reference 2 (Oru): take the crescent forehead crest, the three amber oval lights beneath the left eye and the winglike fin shape from it, using the left three-quarter panel and the face close-up panel; the new creature is the same animal fully grown and vastly larger.
A single reference sheet on a plain mid-grey background, even soft studio light from the front-left, no text anywhere. The same colossal adult alien creature appears in nine panels arranged in three rows of three with clear gaps between the panels. Row one, left to right: a full-length left side profile with the head at the left; a full-length three-quarter view from the front, head turned toward the viewer and her left side toward the viewer, tail behind her; the upper half of her round head rising out of a bank of pale cloud like a moon, the eyelid open only as a narrow curved slit with the amber eye and dark pupil just visible. Row two, left to right: the same head with the eye fully open; a close view of her left eye seen straight on, showing iris, pupil and lower eyelid, with the three oval lights beneath it dim and dark; the same close view of the eye with the three oval lights glowing amber. Row three, left to right: a close view of the tip of her left pectoral fin, showing the broad cupped upper surface, silver-blue ridges, amber veins and the rounded edge; a high view from behind and above on the left, both fins open, the cupped left fin near the viewer at the left, the head far away at the upper right and the tail toward the viewer; a distant view with only a tiny head and eye above a thin horizon line, the lights dim, no fine detail. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. She has two immense silver-blue pectoral fins and one thin tapering tail. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. Her silver-grey and silver-blue colouring stays distinct from Oru's deep teal. Photoreal creature design, neutral reference lighting.
```

### 4.KIYI
```
DOSYA     ref/4.KIYI_v1.png
EKLE      ref/3.ANNE_v1.png   (yalnız 6. panelin yüzgeç ucu için)
PANELLER  8: master geniş (kemer sol, teras orta, geçit sağa, alt çıkıntı orta-sağda aşağıda, deniz sağda, gaz devi sağ üstte) · kemer ağzı + gölge sınırı · geçit ucu SAĞLAM · geçit ucu KOPTU ·
          alt çıkıntı yandan alçak · alt çıkıntı + yüzgeç ucu yanında · alt çıkıntı dalga altında · yüksek açı şafak
```
```text
Reference 3 (mother manta): for the sixth panel only, take the cupped left fin tip from it, using the close view of the tip of her left pectoral fin.
A single reference sheet of one empty alien shoreline at night, eight panels arranged in two rows of four, separated by thin plain mid-grey gaps, no text anywhere. All panels show the same world in the same light. A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. Every panel is an empty place; the only living thing anywhere is the fin tip in the sixth panel. Top row, left to right: a wide master view diagonally from the land toward the sea, with a tall black-basalt arch at the left, the terrace in the middle, a narrow causeway pointing out to the right, one broad dry lower ledge at the middle right below the causeway, a drop about as deep as the arch is tall, open dark sea at the right, the gas giant at the upper right and a few far small black islands on the horizon; a close view of the arch mouth with the shadow line on the floor; the sea end of the causeway intact, with one deep transverse crack and the end slab separated by the crack; the same sea end broken, the end slab gone, a fresh broken edge and open sea beyond. Bottom row, left to right: the lower ledge in a low side view, dry, with a near-vertical rear rock face, open to the sea, the terrace edge, the arch and the broken causeway end high above; the lower ledge with the mother manta's cupped fin tip beside it, the fin continuing past the right edge of the panel, the water beneath it flat; the lower ledge under a dark wave, covered by water and spray; a high view of a small black shoreline far below, low violet cloud tops, a thin warm dawn edge on the horizon and the gas giant at the upper right. A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The mother manta's cupped fin tip rests almost level with the ledge, separated from the rock by a narrow gap, and the water beneath the fin lies flat. Photoreal location reference, restrained 35mm film look, readable night shadows.
```

---

## C01 — Ay gözünü açıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C01.png)
EKLE      başlangıç karesi: kare/C01.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the back-view panel and the intact left-shin panel. Reference 3 (mother manta): take the pitted silver-grey armoured brow, the eyelid and the amber eye from it, using the moon-shaped head panel with the narrow eyelid opening. Reference 4 (shore): take the black arch, the terrace, the causeway, the dark sea and the ringed gas giant from it, using the wide master panel.

An extreme wide night shot from behind Khev on the black basalt terrace, the camera at human eye height looking diagonally along the shore toward the sea, wide-angle lens, deep focus. Khev is a small figure at the lower left, about one tenth of the frame height, standing upright with both feet planted and his back to the camera, facing the sea. Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev presses Oru against his chest with both forearms. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. At this distance Oru reads only as a small teal shape against his chest.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. It is cut off by the left edge of the frame. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea.

The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. Only her rounded brow is visible, high above the sea in the upper middle of the sky, and it looks like a moon. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. The eyelid is already open as a narrow curved slit through which the amber eye and its dark pupil can be seen. A few thin cloud strands cross in front of the lower edge of the eye. A tall bank of cloud rises from the horizon to just beneath the eye and hides the rest of her. The eye glows faintly amber against the cloud edge.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: Khev takes two measured steps forward and to the right toward the sea and stops on the second step with his foot planted; his shoulders rise and his forearms tighten around Oru. At the same time the mother manta's eyelid begins to lift, widening the amber opening. 4-8 s: the eyelid keeps rising while thin cloud strands drift across the eye, and the pitted armour around it keeps its shape; Khev stays planted. 8-10 s: the amber eye is fully open and its dark pupil turns down and to the left toward the shore while the cloud strands keep drifting across it. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   tek göz (ikinci göz yok) · kapak aralığı + amber göz bebeği karede seçili · yuvarlak yüzey organik zırh dokusu (taş küre değil) · Khev sırtı kameraya, kolları Oru'da · kemer sol kenarda, ardı koyu taş iç duvar ·
             gaz devi sağ üstte, tek · yazı/logo/filigran yok (ILK_30 §6) · 16:9 piksel
YEDEK        (hook'un tek taşıyıcısı) kapak ilk karede yarıdan fazla açık başlar — kareyi "yalnız göz kapağı aralığını genişlet, geri kalan her şey aynı" ile düzelt; video kalan aralığın açılması. Bilgi kalır, hook zayıflar.
             Yürüyüş tutmazsa: Khev baştan durmuş (ayaklar yerde), videoda yalnız omuz kalkışı + kol sıkılaşması.
d2           aynı prompt (varyans). d1 tek bir kusurla bozuksa yalnız o kusur düzeltilir; iki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C06 — Ay değil, anne

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C06.png)
EKLE      başlangıç karesi: kare/C06.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the back-view panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and winglike fins from it, using the cradle-pose panel and the top-view panel. Reference 3 (mother manta): take her complete form from it, using the three-quarter front full-length panel.

A very wide, low night shot looking out to sea from the black basalt terrace, the camera close to the ground, wide-angle lens, deep focus. At the lower left corner Khev stands at the mouth of the arch, seen from behind at a three-quarter angle, his head turned toward the sea and the toes of his feet resting exactly on the shadow line, not yet over it. Khev and Oru together fill about one third of the frame height. Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev cradles Oru in his arms against his chest. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso. Seen from behind, Oru shows a blunt rounded head with one shallow crescent forehead crest above two broad winglike fins. Oru's head and right fin stand out as a clear outline against the night sky beside Khev's right shoulder, the right fin hanging half open and the left fin folded against its side. Oru's teal is one shade lighter than the night around it.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea.

The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She hovers above the water across the sea and fills the right two thirds of the frame, entirely visible, with the horizon passing behind her at about one third of the frame height from the bottom. Her head points toward the shore at the left with her left side toward the camera, and her round pitted head armour is the moon-like shape. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. The three lights are small amber dots at this distance. She has two immense silver-blue pectoral fins and one thin tapering tail. Both fins are spread wide and tilted upward above the water, and the thin tail trails away to the right. Her crescent crest and winged outline match Oru's at a vast scale. Thin cloud strands drift in front of her fins.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of her raised fins. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: Oru lifts its right fin fully open beside Khev's shoulder while its left fin stays folded; the mother manta holds both of her fins spread and tilted upward above the sea, and thin cloud strands drift across in front of her. 4-8 s: Khev raises his head slowly and follows the mother manta's whole form from her head to her tail, his head turning from left to right; his forearms stay around Oru. 8-10 s: the mother manta's fins curl a little and level out while the cloud strands keep drifting; Khev and Oru stay in place. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   dev manta ilk karede BÜTÜN (baş, tek göz, üç ışık, iki yüzgeç, tek kuyruk) · Oru'nun başı + sağ yüzgeci Khev'in omzunun yanında açık siluet, Khev'in gövdesi örtmüyor (TD B4) ·
             hilal alın ve yüzgeç siluetinde Oru ↔ dev manta aynı dil · Khev'in ayak parmakları gölge çizgisinde, çizgiyi geçmemiş · kemer ağzı alt-solda, ardı iç duvar · tek Oru, tek dev manta · yazı yok · 16:9 piksel
YEDEK        siluet/oklüzyon tutmazsa (TD B4): Oru "a small teal manta" metinle anlatılır, 2.ORU atılır, 4.KIYI eklenir (bilgi siluetten okunur). Dev manta bütün çıkmazsa bir yüzgeç ucu bulut kenarında başlar — C06 için önerilmez (açığa çıkış C05→C06 kesmesinin işi).
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir.
```

## C20 — Yavru annesine ulaşıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C20.png)
EKLE      başlangıç karesi: kare/C20.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with the right fin spread open and the left fin half open and drooping. Reference 4 (shore): take the lower rock ledge with its steep rear face, the dark sea and the cupped fin tip beside the ledge from it, using the panel with the fin tip beside the ledge.

A medium-close night shot on the lower ledge, the camera at ledge height in front of Khev and slightly to his left, standard lens, shallow depth of field. Khev sits at the left of the frame with his chest in three-quarter view toward the camera and his face turned to the right toward the fin. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's right leg is folded under him and his left leg is stretched out toward the camera, so that the left shin plate lies along the lower edge of the frame. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Each of Khev's hands has four thick digits in deep-indigo skin. Khev holds both forearms out in front of him, open, palms up, forming an open cradle.

Oru hovers on its own fins a hand's breadth above his open forearms without touching them, its torso angled toward the fin and its head turned toward the camera. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's three lights glow steadily, and its teal is one shade lighter than the dark stone around it.

At the right of the frame, the mother manta's cupped fin tip rests almost level with the ledge, separated from the rock by a narrow gap, and the water beneath the fin lies flat. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. The fin continues past the right edge of the frame, joined to the mother far out at sea. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. That rear rock face stands behind Khev at the left. Far beyond the fin, a single broad dark wave ridge rises on the horizon at the right.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. The pale rim light reaches the foot of the rear rock face and picks it out from the shadow.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Oru flutters its right fin and rises a little higher above Khev's forearms, its drooping left fin trembling; Khev keeps his forearms open, palms up, and his gaze follows Oru. 3-7 s: Oru slips out from above his forearms, makes one short soft glide across the narrow gap with its head turning toward the fin, and lands on the cupped surface of the fin. 7-10 s: Oru settles on top of the fin as a separate small teal creature and turns its head back toward Khev while its three lights brighten; Khev keeps his arms open and stays seated, and the dark wave ridge on the horizon creeps a little closer. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç ayrı beden: Oru kollardan ve yüzgeçten ayrı, kollarla temas yok (bir karış boşluk) · Oru'nun sağ yüzgeci açık, sol yüzgeci yarım açık-sarkık, tek V çentik sol yüzgeçte, üç ışık yan yana ·
             Khev'in sol kaval plakasında TEK çapraz çatlak (alt kenarda okunuyor), sağ kavalda çatlak yok · her elde dört parmak, eller açık, palmlar yukarı · yüzgeç ucu çıkıntıya yakın, dar boşluk, altındaki su düz · arka plan dik duvar solda · 16:9 piksel
YEDEK        (TD B5) süzülüş üretilemez ya da yüzgeçle kaynaşırsa: çekim "Oru yüzgeçte konmuş + Khev'in boş açık kolları" yakın kesmesiyle aynı bilgiyi taşır — yeni kare: Oru yüzgecin üstünde, Khev'in kolları açık ve boş.
d2           aynı prompt (varyans). İki deneme de Oru'yu yüzgece ya da kollara eritirse üçüncü deneme aynı promptla gönderilmez: yedek kareye (Oru yüzgeçte konmuş + boş kollar) geçilir.
```

---

## FLOW İŞ EMRİ

> **Araç (Flow değil):** referans sayfaları ve kareler **GPT Image**'da (ChatGPT Images 2.5 ya da API `gpt-image-2.5-sunburst`), video **Gemini Omni 1.1 Flash** (Gemini uygulaması). `FLOW_GERCEKLERI` Ek 2-3.
> Flow ayarları (Return silent videos, watermark) bu yolda yok; Omni klibin yerel sesi üretilir → **indirildikten sonra kurguda atılır** (model sesi KAPALI, `timeline.json` klip_sesi kapalı). Videoda ses isteği yazılmadı.
> Her kare **yeni sohbette**, onaylı çapa referansları yeniden eklenerek üretilir; önceki karenin çıktısı yeni kareye girdi yapılmaz (KIMLIK §3). Çıktı PNG, piksel oranı **16:9** ölçülür (1536×864 · 2048×1152 · 2560×1440);
> 3:2 çıkarsa merkezden 16:9 kırpılır, esnetme/genişletme yok (GPT_IMAGE_OMNI §13). Her denemede `NOTLAR.md` DENEMELER'e: model adı · eklenen numaralar (`ref 1,3,4`) · giriş/çıkış saniyesi (`medya.py al MOONMOTHER --yaz`).
> Omni'ye yalnız `kare/Cxx.png` yüklenir; panel sayfası yüklenmez. Aynı yapısal hata iki kontrollü düzeltmede kalırsa çekim yeniden tasarlanır (AGENTS §4).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | 1.KHEV | `ref/1.KHEV_v1.png` | Görsel (GPT Image) | — | 2 | ölçülecek |
| 2 | 2.ORU | `ref/2.ORU_v1.png` | Görsel (GPT Image) | — | 2 | ölçülecek |
| 3 | 3.ANNE | `ref/3.ANNE_v1.png` | Görsel (GPT Image) | ref/2.ORU_v1.png | 2 | ölçülecek |
| 4 | 4.KIYI | `ref/4.KIYI_v1.png` | Görsel (GPT Image) | ref/3.ANNE_v1.png (yalnız 6. panel) | 2 | ölçülecek |
| 5 | C01 kare | `kare/C01.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 6 | C01 | `ham/C01_d1.mp4` | Frames to Video (Gemini Omni) | kare/C01.png | 2 | ölçülecek |
| 7 | C06 kare | `kare/C06.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 8 | C06 | `ham/C06_d1.mp4` | Frames to Video (Gemini Omni) | kare/C06.png | 2 | ölçülecek |
| 9 | C20 kare | `kare/C20.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 10 | C20 | `ham/C20_d1.mp4` | Frames to Video (Gemini Omni) | kare/C20.png | 2 | ölçülecek |

Toplam: 7 görsel çıktı × 2 deneme + 3 video × 2 deneme = en çok 20 üretim. İkinci denemeler: `ham/C01_d2.mp4` · `ham/C06_d2.mp4` · `ham/C20_d2.mp4`.

## PİLOT SORUSU

| Çekim | Bu denemenin cevaplayacağı soru |
|:--:|---|
| C01 | Göz kapağı organik açılıyor mu — yuvarlak yüzey taş küre gibi kalıp başka bir yüze dönüşmeden, ikinci göz çıkmadan, tek amber göz tam açılıyor mu (hook'un tek taşıyıcısı) ve Khev ikinci adımda ayağı yerdeyken duruyor mu? |
| C06 | Kare düzeyinde: dev manta ilk karede tam gövde mi ve hilal alın + açık yüzgeç siluetiyle Oru'nun erişkini olarak okunuyor mu (sesi kapalı, başlıksız izleyici "bunlar akraba" diyebiliyor mu — F3 ÖLÜMCÜL); Oru'nun başı ve sağ yüzgeci Khev'in omzunun yanında açık siluet mi? |
| C20 | Oru, Khev ve dev yüzgeç üç ayrı beden olarak kalıyor mu — Oru kollardan yüzgece tek kısa süzülüşle geçerken yüzgece ya da kollara erimeden konuyor mu, sarkık sol yüzgeç ve tek çatlak (çatlak paneli seçiliyor mu) video boyunca tutuyor mu? |

---

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · `.claude/agents/goruntu-yonetmeni.md` § Bitirmeden önce)

> Elle tarama (bu ajanda kabuk yok, `film_dogrula.py` koşulmadı). Kimlik cümlesi sayımı Grep ile yapıldı; DERS taraması elle: Y1 (ISARET kelimesi yok) · Y5 (`smoke/steam/mist/fog/vapor/plume/exhaust/drip/splash/bubble/wet/rain/flame` Görsel ve Video'da yok; `spray`/`cloud`/`wave` listede yok) ·
> Y8 (ekran/gösterge/`status` yok) · Y10 (`slow` en çok 1 kez) · Y13 (Video'da `sound/audio/ambient/hum/echo/noise/music` yok). Y2: ekli her referansın en az bir cümlesi birebir.

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C01 | **2** (Oru ekli referans değil ama kadrajda: 2.a birebir metinle eklendi; plan "tiny teal creature" diyordu) · **3** (planın ortak cümlesi `cold indigo and teal night light` ve `without lettering, logos, or watermarks` taşıyordu → ışık 4 · "ışık" satırına, yazı kilidi `plain unmarked surfaces`e taşındı; Fable'a KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6) · **4** (kemer ağzının ardı `dark stone inner wall` eklendi; Khev'in önü deniz, ardı kamera tarafı) · **7** (Reference 3 plandaki "distant organic eye" yerine yalnız ③ panelini ister: kapak aralığı + amber göz) · **8** (plandaki üç `Sound:` satırı ve "Environmental sound…" kuyruğu atıldı; Video'da ses/çağrı kelimesi yok) | **1** işaret yok (Khev'in giysisi/işareti yok; sol kaval cümlesi sayı+taraf+konum taşır) · **5** akışkan yok (yalnız `cloud strands`) · **6** ekran yok |
| C06 | **2** (Oru parçaları 2.a · 2.e · 2.f birebir; ışıklar/yüz kadrajda olmadığı için 2.b yazılmadı — Oru yüzü denizde, kameradan uzak) · **3** (C01 ile aynı ortak cümle düzeltmesi) · **4** (kemer ağzının ardı iç duvar; Khev'in önü deniz, ardı kemer çukuru; ufuk dev mantanın ardında yazıldı) · **7** (Reference 2 yalnız kucak duruşu + üstten panel; Reference 3 yalnız ¾ önden tam boy panel) · **8** (planın "Sound: … three-note calls overlap" satırı atıldı; `calls` kelimesi yok) | **1** işaret yok · **5** akışkan yok (`cloud strands`, `water` yalnız deniz yüzeyi) · **6** ekran yok |
| C20 | **1** (çatlak: sayı `one diagonal crack` + taraf `left` + konum `shin plate` + `the only crack on him`; eller `four thick digits` her elde; Oru çentiği `one … V-shaped notch … the only notch on either fin`) · **2** (yüzgeç ucu 3.e + 4 · "yüzgeç yanında" birebir; plan "sits or kneels" ikiliydi → tek poz: oturuyor, sağ bacak altında, sol bacak uzatılmış) · **3** (ortak cümle) · **4** (dik arka duvar Khev'in ardında yazıldı; plan C20 karesinde duvarı anmıyordu; yüzgecin sağ kenardan devam edip dev mantaya bağlandığı yazıldı) · **5** (çıkıntı kuru, deniz yalnız `the water beneath the fin lies flat`; sprey/ıslak kelimesi yok, hedef hâl olumlu) · **7** (Reference 4 yalnız "yüzgeç ucu çıkıntı yanında" panelini ister; Reference 1 yalnız ¾ yüz + çömelme + çatlak paneli, SAĞLAM panel anılmadı; Reference 2 yalnız sarkık-sol-yüzgeç paneli) · **8** (planın `Sound:` satırı atıldı; son vuruşta `holds still` yok) | **6** ekran yok · Oru'nun yüzü kameraya dönük başlar (üç ışık görünsün diye); süzülüş yönü yüzgeçtir — baş, konmada tekrar Khev'e döner. Plan "Khev oturur ya da diz çöker" diyordu; oturuş seçildi (FILM §4 C20: "Khev çıkıntıda oturuyor"). |
