# 🖼️ MOONMOTHER — Prompt grubu G01 (çekimler C01–C08)

> Yazan: goruntu-yonetmeni (F5 tur 1, 17.10.2026). Denetleyen: devamlilik · teknik-danisman.
> Prompt gövdesine çekim kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Üretim yolu (FILM.md künye URETIM): **GPT Image** (referans sayfaları + başlangıç kareleri) → **Gemini Omni 1.1 Flash** (10 s video, Gemini uygulaması).
> Omni'ye yalnız onaylı tek başlangıç karesi gider (`kare/Cxx.png`); panel sayfası Omni'ye girdi olmaz (GPT_IMAGE_OMNI §4, §7). Ayrı başlangıç/bitiş karesi yok → zincir yok.
> Model sesi KAPALI: planın "Sound:" satırları ve "Environmental sound and nonverbal alien calls only…" kuyruğu video promptlarına GİRMEZ (ses F4'te kurulur).
> Kaynak: `FILM.md` §3 (KİMLİK CÜMLELERİ · ORTAK GÖRÜNÜM) · §4 (C01-C08) · `ODA/F3_yonetmen_2.md` §4 (KİMLİK CÜMLESİ GİRDİSİ · F5'E HATIRLATMA) · `ODA/SAHIP_PLANI.md` ·
> `PROMPTLAR/PILOT.md` (pilot ölçülmedi, sahip pilotu beklemeden F5'e geçti: `REFERANS PROMPTLARI` dört sayfa, `## C01` ve `## C06` bölümleri BİREBİR; C20 G03'e gider) ·
> `GPT_IMAGE_OMNI_KILAVUZU` · `KIMLIK_VE_REFERANS_KILAVUZU` · `UZAY_FIZIGI_GORUNTU_KILAVUZU` · `PROMPT_HATA_ATLASI` · `ILK_30_SANIYE_KILAVUZU` §6 · `GECIS_VE_SES_SUREKLILIGI` §1 · `FLOW_GERCEKLERI` Ek 2-3.
> Kelime kararları (F3 TD B15, BILINEN_TUZAKLAR §A/§C): `body`, `wound(ed)` ve büyük harfli KHEV/ORU etiketi hiçbir promptta yok; kemer `smooth parallel vertical grooves … no symbols` (kimlik cümlesiyle birebir);
> ölçüler sayıyla değil kadrajla (Oru Khev'in önkolundan kısa; alt çıkıntı Khev boyunun iki katı aşağıda); mavi karın ışığı yalnız referans sayfasında (kare promptlarında anılmaz).
> Sahip kararı 17.10.2026: sapmaların hepsi ONAY (C01 Khev ikinci adımda durur · C02 odak dışı amber göz · C06 sabit kamera, dev manta ilk karede tam gövde · Khev'in solungaç yarıkları koyu indigo).
> Açılış kuralı (ILK_30 §6): C01-C03 ilk üretilen çekimlerdir; hızlı kamera, yazı, logo, kalabalık, karmaşık el-nesne teması yok.

---

## KİMLİK CÜMLELERİ

> Kaynak `FILM.md` §3 `### KİMLİK CÜMLELERİ` (yeniden yazılmadı). Bu grupta kullanılan parçalar Görsel promptlara kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (Khev · Oru · the mother manta).

---

## REFERANS PROMPTLARI (yalnız ilk grupta · özne başına TEK sayfa · `PROMPTLAR/PILOT.md`'den birebir)

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
PANELLER  10 (3+3+4; üçüncü sıra dört dar panel): tam boy sol profil · tam boy ¾ önden (baş kameraya, sol yan kameraya) · "ay" biçimli baş, bulut ardında, göz kapağı dar aralık · aynı baş, göz TAM AÇIK ·
          sol göz yakın, ışıklar SÖNÜK · sol göz yakın, ışıklar YANIK · sol yüzgeç ucu yakın (çanak, kenar DÜZ) · yüksek açı arkadan-sol üstten · uzak baş (ufukta, ayrıntısız) ·
          10. DURUM sol yüzgeç ucu KIVRIK yakın (sığ çanak: kenar üç yanda yukarı ve içe, dördüncü yan alçak ve açık, kameraya dönük; çanağın içi boş)
```
```text
Reference 2 (Oru): take the crescent forehead crest, the three amber oval lights beneath the left eye and the winglike fin shape from it, using the left three-quarter panel and the face close-up panel; the new creature is the same animal fully grown and vastly larger.
A single reference sheet on a plain mid-grey background, even soft studio light from the front-left, no text anywhere. The same colossal adult alien creature appears in ten panels arranged in three rows with clear gaps between the panels: three panels in row one, three in row two and four narrower panels in row three. Row one, left to right: a full-length left side profile with the head at the left; a full-length three-quarter view from the front, head turned toward the viewer and her left side toward the viewer, tail behind her; the upper half of her round head rising out of a bank of pale cloud like a moon, the eyelid open only as a narrow curved slit with the amber eye and dark pupil just visible. Row two, left to right: the same head with the eye fully open; a close view of her left eye seen straight on, showing iris, pupil and lower eyelid, with the three oval lights beneath it dim and dark; the same close view of the eye with the three oval lights glowing amber. Row three, left to right: a close view of the tip of her left pectoral fin with its rounded edge lying flat, showing the broad cupped upper surface, silver-blue ridges, amber veins and the rounded edge; a high view from behind and above on the left, both fins open, the cupped left fin near the viewer at the left, the head far away at the upper right and the tail toward the viewer; a distant view with only a tiny head and eye above a thin horizon line, the lights dim, no fine detail; a close view of the same fin tip in its curled state, showing the empty shallow bowl with its low open side toward the viewer. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. She has two immense silver-blue pectoral fins and one thin tapering tail. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. In the first nine panels the rounded edge of that tip lies flat, level with the rest of the cupped surface. In the tenth panel only, the rounded tip of her left pectoral fin is curled into a shallow bowl, its one smooth rounded edge bending gently upward and inward on three sides and staying low and open on the fourth, with the pale silver-blue ridges and thin amber veins running on across the inside of the bowl. Her silver-grey and silver-blue colouring stays distinct from Oru's deep teal. Photoreal creature design, neutral reference lighting.
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

## C02 — Korunan yavru, göğe bakış

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C02.png)
EKLE      başlangıç karesi: kare/C02.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel and the forearm-and-hand panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the cradle-pose panel, the face close-up panel and the left-fin trailing-edge panel. Reference 3 (mother manta): take only the colour and the round shape of her open amber eye from it, using the panel of the head with the eye fully open.

A medium close-up night shot of Khev from the waist up, the camera at his chest height and about forty-five degrees to the left of the direction he is looking, standard lens, shallow depth of field. Khev fills the left half of the frame in three-quarter view, his face tilted down and a little to the right toward Oru. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. His two forearms form a level cradle in front of his chest and run out through the lower edge of the frame, so his hands stay outside the frame. The thin pale rim light outlines the ivory plates of his head and shoulder.

Oru lies in the cradle of his forearms at the lower right of his face, its head raised and turned toward the camera, its left side and left fin toward the camera. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso. Oru's three lights glow faintly and evenly, and its teal is one shade lighter than the night around it.

Behind Khev the background is blurred black basalt shore in the cold dark. High at the upper right, far out of focus, hangs the eye of the mother manta. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. In this frame it reads only as one soft round amber glow with no sharp detail, and a faint amber reflection lies on the blurred basalt below it.

The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Oru turns its raised head from the camera toward the upper right of the frame, up to the sky, and its notched left fin trembles; Khev keeps his gaze on Oru. 3-6.5 s: Oru's three amber lights glow brighter one at a time from left to right, each fading before the next begins; Khev keeps his gaze on Oru and his forearms keep the cradle firm. 6.5-10 s: Khev slowly raises his head and turns his face to the upper right, the direction Oru looked, while his forearms keep the cradle around Oru; Oru's three lights settle to a faint dim glow. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev yüzü: iki siyah yan göz simetrik, burun ve dudak yok, tek sert ağız çizgisi, boynun iki yanında üçer KOYU İNDİGO solungaç yarığı (amber değil) · iki ön kol Oru'nun altında beşik, eller kadraj dışı ·
             Oru Khev'in ön kolundan kısa, kolların içinde (temas baştan kurulu), başı kameraya dönük, sol yüzgeç kameraya yakın ve V çentik okunuyor, sol gözün altında TEK sıra üç oval (yan yana, eşit aralıklı) ·
             sağ üstte tek, odak dışı, ayrıntısız amber yuvarlak (ikinci göz yok) ve altında bazaltta soluk amber yansıma · renk ayrımı: teal Oru / indigo deri / fildişi plaka · yazı yok · 16:9 piksel
YEDEK        (ILK_30 §6 kare kapısı; kapak karşılığı) Khev yüzünde bozulma ya da göz asimetrisi varsa: ¾ arkadan omuz-baş sürümü (bilgi aynı: korunan yavru, Oru'nun göğe bakışı, kucak teması).
             Odak dışı amber yuvarlak tutmazsa (ikinci göz, ayrıntılı göz) tek düzeltme, bilgi düşmez (tretman metni):
             "Edit the supplied frame. Change only the upper right background: the soft round amber glow is replaced by the same dark blurred night, and the faint amber reflection stays on the blurred basalt. Keep Khev, Oru, the camera angle and the light exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C03 — Yıldızları örten yüzgeç

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C03.png)
EKLE      başlangıç karesi: kare/C03.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the back-view panel and the intact left-shin panel. Reference 3 (mother manta): take her pitted silver-grey armoured head, her fully open amber eye and the curved edge of her silver-blue fin from it, using the panel of the head with the eye fully open and the full-length left-side profile panel. Reference 4 (shore): take the black arch, the terrace, the dark sea, the far black islands and the ringed gas giant from it, using the wide master panel.

An extreme wide night shot looking from the shore out over the dark sea, the camera low near the ground, wide-angle lens, deep focus. The horizon passes at about one third of the frame height from the bottom.

The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. Her round head hovers above the sea in the right half of the frame, her face turned toward the shore at the left and her left side toward the camera. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. The eyelid is fully open and the amber eye glows against the pitted armour. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At this distance the lights are too small and dim to read. A tall bank of cloud rises behind her head and hides the rest of her. She has two immense silver-blue pectoral fins and one thin tapering tail. Of these only the curved tip of one fin is in the frame: it already shows above the edge of the cloud bank behind her head, joined to her hidden torso, while the second fin and the tail stay hidden in the cloud.

At the lower left, on the edge of the terrace just outside the arch, Khev stands with his back to the camera, facing the sea, a tiny dark silhouette about one twentieth of the frame height with a thin pale rim of light along his shoulders. Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev presses Oru against his chest with both forearms. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. At this distance Oru reads only as a tiny teal shape against his chest.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. It is cut off by the left edge of the frame. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. A few far small black islands lie on the horizon.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of the fin tip. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-5 s: the curved tip of the fin climbs out from behind the edge of the cloud bank, rising up and to the left across the sky. 5-10 s: the fin keeps climbing, its long curved edge sweeping across the stars and covering nearly a third of the star field like a mountain range, while the mother manta's head with its open eye stays in place above the sea and the small silhouette at the lower left stays where it stands. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   tek baş, tek açık amber göz (ikinci baş ya da ikinci "ay" yok) · yüzgeç ucu ilk karede bulut kenarında, başın arkasından çıkıyor (gövdeye bağlı, ayrı canlı değil) · gaz devi sağ üstte, tek, yüzgeç ucuna değmiyor ·
             Khev + Oru sol altta küçük koyu silüet, yüz yok; kemer sol kenarda, yivler paralel dikey ve sembolsüz · ufukta uzak küçük adalar · ufuk çizgisi kareden okunuyor · yazı/logo/filigran yok (ILK_30 §6) · 16:9 piksel
YEDEK        yüzgeç ucu karede doğmuyorsa ya da ayrı canlı gibi duruyorsa: yüzgeç ilk karede bulutun üstünde tam görünür başlar, video yalnız yükseliş. Tek düzeltme:
             "Edit the supplied frame. Change only the fin: its curved edge now rises fully above the cloud bank behind her head, still joined to her hidden torso, and covers a small part of the star field. Keep the head, the open eye, the cloud bank, Khev's silhouette, the arch, the sea, the gas giant, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C04 — Kemer sığınak oluyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C04.png)
EKLE      başlangıç karesi: kare/C04.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the right-side full-length panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and winglike fins from it, using the cradle-pose panel and the face close-up panel. Reference 4 (shore): take the black arch with the shadow line on its floor, the terrace, the dark sea and the ringed gas giant from it, using the arch-mouth panel and the wide master panel.

A medium-full night shot from the landward side, the camera at chest height, standard lens, deep focus. Khev stands in the left half of the frame on the open black basalt, just outside the arch and one short step from the shadow line, in three-quarter view with his right side toward the camera, his chest and face turned toward the dark sea at the right of the frame and his shoulders raised high. Both of his feet are fully in the frame, planted on the basalt, each with a clear contact shadow. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev presses Oru against his chest with both forearms, his hands hidden behind Oru. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. It fills the left edge of the frame beside Khev. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea.

High at the upper right the long curved edge of one immense silver-blue fin of the mother manta crosses the star field. She has two immense silver-blue pectoral fins and one thin tapering tail, but only this one curved fin edge is inside the frame.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of the fin edge. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: Khev shifts his weight toward the arch at the left and takes one careful sideways step: the foot nearer the arch lifts, moves toward the arch and plants on the basalt, while his chest and face stay turned toward the sea at the right; the curved fin edge in the sky creeps across the stars. 4-7 s: his second foot comes in beside the first and both feet cross the shadow line into the shade. 7-10 s: he curls both forearms closer around Oru in a protective curve and bows his raised shoulders over it, so that his arms and shoulders form a screen between Oru and the sea. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev kemerin hemen dışında, gölge sınırının bir adım ötesinde, yüzü ve göğsü denize dönük, omuzlar kalkık · iki ayak tam kadrajda, temas gölgeli · kollar baştan Oru'nun çevresinde, eller Oru'nun ardında ·
             kemerin altı koyu ve kapalı, ardı iç duvar, zeminde gölge sınırı net · sağ üstte yıldızları örten dev yüzgeç kenarı, gaz devi ona değmiyor · sol kaval sağlam, tek · yazı yok · 16:9 piksel
YEDEK        (T10) yan adım dönüp yürümeye kayarsa: Khev kemer ağzında yarı gölgede başlar, videoda yalnız omuz-kol hareketi (koruma bilgisi kalır). Tek düzeltme:
             "Edit the supplied frame. Change only Khev's position: he now stands half inside the arch's shade with both feet already behind the shadow line, his chest and face still turned toward the sea. Keep Khev's pose, Oru, the arch, the sea, the sky, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C05 — Aynı üç ışık, bakış kıyıya iniyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C05.png)
EKLE      başlangıç karesi: kare/C05.png · referans (yükleme sırası): ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 3 (mother manta): take her left eye, the pitted silver-grey armour around it and the three oval lights beneath it from it, using the close eye panel with the three lights dim and dark.

An extreme close-up night shot of the left eye of the mother manta, seen straight on at eye level, the eye and the armour around it filling the whole frame, medium telephoto lens, shallow depth of field. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. The eyelid is fully open, its thick lower edge curving under the amber iris, and the glossy dark pupil rests at the centre of the iris. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At the start the three lights are dim: three separate, evenly spaced, dark copper-toned ovals in one row. Sparse high cloud strands drift in thin horizontal lines across the eye and the armour, and the surface behind them is clearly organic, with the pits and plate seams of living armour. The eye glows faintly amber against the dark armour.

The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-5 s: the three oval lights beneath the mother manta's eye glow amber one at a time from left to right, each fading before the next begins, while thin cloud strands drift horizontally across the eye. 5-7 s: all three lights glow brightly together for a short moment. 7-10 s: the mother manta's pupil makes one deliberate movement down and to the left of the frame, toward the shore, and comes to rest there, the three lights staying lit and the cloud strands drifting on across the surface. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç AYRI, eşit aralıklı, SÖNÜK (bakır tonlu) oval, tek sıra, gözün altında (iki ya da dört değil) · tek göz, göz bebeği ortada, alt göz kapağı okunuyor · yüzey organik zırh (çukurlar ve plaka dikişleri; taş yüzey değil) ·
             yatay bulut telleri anatomiyi değiştirmiyor · kadrajda başka varlık yok · yazı yok · 16:9 piksel
YEDEK        (T09) ışık sayısı 2 ya da 4 çıkarsa tek düzeltme:
             "Edit the supplied frame. Change only the lights beneath the eye: exactly three separate, evenly spaced, dim ovals in one row. Keep the eye, the armour, the cloud strands, the light and the camera angle exactly as they are."
             Video tek yanış turu; göz bebeği hareketi tutmazsa 7-10 s yalnız ışıkların yanık kalması + bulut telleri (bilgi: cevap verdi; bakış C06 kesmesinde kıyıya iner).
             Ayna çifti (G03): C05 düz karşı + yatay bulut telleri + ışıklar önce, göz bebeği sonra; çekim başı bu düzene göre.
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
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

## C07 — Yaklaşmanın bedeli: tek geniş sırt

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C07.png)
EKLE      başlangıç karesi: kare/C07.png · referans (yükleme sırası): ref/3.ANNE_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 3 (mother manta): take her complete form from it, using the full-length left-side profile panel. Reference 4 (shore): take the black basalt shore, the arch, the terrace, the dark sea, the far black islands and the ringed gas giant from it, using the wide master panel and the arch-mouth panel.

A wide night shot looking along the coast, the camera low at shore level and parallel to the shoreline, wide-angle lens, deep focus. The dark sea fills the right of the frame, and the black shore runs along the left side and the bottom edge of the frame with loose stones scattered on it. A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The arch, the terrace and the causeway are all very small along the lower left edge of the frame.

The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She hovers above the sea in the right half of the frame, entirely visible, her face turned toward the shore at the left and her left side toward the camera, with the horizon passing behind her at about one third of the frame height from the bottom. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. The three lights are small amber dots at this distance. She has two immense silver-blue pectoral fins and one thin tapering tail. Both fins are spread wide and held level above the sea, and the thin tail trails away to the right. The dark water directly in front of her head has begun to swell into one single low ridge that points toward the shore. Far small black islands and a layer of cloud lie on the horizon.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of her fins. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: the mother manta advances a little toward the shore; the dark water in front of her head swells and grows into one broad ridge that rolls toward the shore, spray leaping from its crest and the loose stones along the shore bouncing. 4-6 s: she lifts both fins up and away from the shore and the arch and stops advancing. 6-10 s: the ridge keeps rolling on alone toward the shore at the left while she stays in place, the spray and the bouncing stones continuing along the shore. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   dev manta BÜTÜN (baş, tek göz, üç ışık, iki yüzgeç, tek kuyruk), başı kıyıya (sola), sol yanı kameraya · sırt TEK, alçak, mantanın başının önünde (ikinci dalga yok) · deniz sağda, kıyı sol ve alt kenarda, gevşek taşlar kıyıda ·
             kemer + teras alt-solda çok küçük, kemer ağzının ardı iç duvar · uzak adalar + ufuk bulutu ölçek ipucu · gaz devi sağ üstte, yüzgeçlere değmiyor · yazı yok · 16:9 piksel
YEDEK        (kurgucu B4; kuralın tek tanıtıcısı) sırt okunmazsa: dev manta yüzgeçlerini kaldırmış ve sırt kabarmış başlar; video yalnız sırtın kıyıya ilerlemesi, 2 vuruş:
             0-5 s sırt kıyıya doğru büyüyerek ilerler, sprey sıçrar, kıyıdaki taşlar zıplar · 5-10 s sırt kıyıya yaklaşmayı sürdürür, dev manta yerinde. Sırt bilgisini G02'de C09 ufuk sırtı ve C10 öncü kıvrımı da taşır.
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C08 — Kurtarma yolunun haritası

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C08.png)
EKLE      başlangıç karesi: kare/C08.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the right-side full-length panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the cradle-pose panel and the face close-up panel. Reference 4 (shore): take the arch with its shadow line, the terrace, the causeway, the lower ledge with its steep rear face and the dark sea from it, using the wide master panel and the arch-mouth panel.

A wide elevated night shot from the land toward the sea, the camera high above the terrace and tilted down about twenty degrees, wide-angle lens, deep focus. A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The end of the causeway is open to the sea. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The lower ledge lies about twice Khev's height below the end of the causeway. The sea breaks against the outer edge of the ledge while the shelf itself stays dry, and open dark sea fills the right of the frame and the background.

Khev stands in the shade beneath the arch at the left of the frame, one step back from the shadow line, in profile with his right side toward the camera and his face turned to the right toward the causeway and the sea. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev presses Oru against his chest with both forearms, his hands hidden behind Oru. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso. At this distance Oru is a small deep-teal shape with its three tiny amber lights on the camera side.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-5 s: Khev turns his head in three stages, first to the sea end of the causeway, then down to the ledge below, then out to the open sea; the camera makes a very slow push-in toward the arch and the causeway, and the sea keeps breaking against the outer edge of the ledge. 5-7 s: Oru flashes its three amber lights once and turns its head toward the sea. 7-10 s: Khev takes one step forward and his toes come to rest on the shadow line, Oru against his chest, while the sea keeps breaking against the ledge. The arch, the causeway and the ledge keep their places in the frame throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç seviye tek kadrajda okunur: yüksek kemer + teras (solda) → geçit (ortada, sağa) → alt çıkıntı (orta-sağda, geçit ucunun Khev boyunun yaklaşık iki katı aşağısında, dik arka duvar, kuru) → deniz sağda ve arkada ·
             kemerin altı koyu ve kapalı, ardı iç duvar, gölge sınırı net, ötesi açık · Khev kemerin altında, gölge sınırının bir adım gerisinde, yüzü sağa; Oru göğsünde, başı yukarı · sörf çıkıntının dış kenarında ·
             gaz devi sağ üstte, tek · sol kaval sağlam · yazı yok · 16:9 piksel
YEDEK        (T04) d1 itme coğrafyayı esnetirse (geçit uzar/kısalır, çıkıntı yer değiştirir): d2 aynı promptta yalnız kamera cümlesi değişir, "the camera makes a very slow push-in toward the arch and the causeway" yerine "the camera stays locked".
             Adım ayak çizgisinde durmazsa (T10): Khev baştan çizgide durur, videoda yalnız üç aşamalı baş çevirişi + Oru'nun ışık atımı.
d2           aynı prompt (varyans) ya da yukarıdaki sabit-kamera varyantı; d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

---

## FLOW İŞ EMRİ

> **Araç (Flow değil):** referans sayfaları ve kareler **GPT Image**'da (ChatGPT Images 2.5 ya da API `gpt-image-2.5-sunburst`), video **Gemini Omni 1.1 Flash** (Gemini uygulaması). `FLOW_GERCEKLERI` Ek 2-3.
> Flow ayarları (Return silent videos, watermark) bu yolda yok; Omni klibin yerel sesi üretilir → **indirildikten sonra kurguda atılır** (model sesi KAPALI, `timeline.json` klip_sesi kapalı). Videoda ses isteği yazılmadı.
> Her kare **yeni sohbette**, onaylı çapa referansları yeniden eklenerek üretilir; önceki karenin çıktısı yeni kareye girdi yapılmaz (KIMLIK §3). Çıktı PNG, piksel oranı **16:9** ölçülür (1536×864 · 2048×1152 · 2560×1440);
> 3:2 çıkarsa merkezden 16:9 kırpılır, esnetme/genişletme yok (GPT_IMAGE_OMNI §13). Her denemede `NOTLAR.md` DENEMELER'e: model adı · eklenen numaralar (`ref 1,3,4`) · giriş/çıkış saniyesi (`medya.py al MOONMOTHER --yaz`).
> Omni'ye yalnız `kare/Cxx.png` yüklenir; panel sayfası yüklenmez. Aynı yapısal hata iki kontrollü düzeltmede kalırsa çekim yeniden tasarlanır (AGENTS §4).
> Üretim önceliği: C01 · C02 · C03 (açılış, ILK_30 §6: deneme hakkı en çok onlarda) → C06 (pilot adayı, akrabalık) → C04 · C05 · C07 · C08. Tablo sırası çekim sırasıdır; referanslar her şeyden önce.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | 1.KHEV | `ref/1.KHEV_v1.png` | Görsel (GPT Image) | — | 2 | ölçülecek |
| 2 | 2.ORU | `ref/2.ORU_v1.png` | Görsel (GPT Image) | — | 2 | ölçülecek |
| 3 | 3.ANNE | `ref/3.ANNE_v1.png` | Görsel (GPT Image) | ref/2.ORU_v1.png | 2 | ölçülecek |
| 4 | 4.KIYI | `ref/4.KIYI_v1.png` | Görsel (GPT Image) | ref/3.ANNE_v1.png (yalnız 6. panel) | 2 | ölçülecek |
| 5 | C01 kare | `kare/C01.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 6 | C01 | `ham/C01_d1.mp4` | Frames to Video (Gemini Omni) | kare/C01.png | 2 | ölçülecek |
| 7 | C02 kare | `kare/C02.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 8 | C02 | `ham/C02_d1.mp4` | Frames to Video (Gemini Omni) | kare/C02.png | 2 | ölçülecek |
| 9 | C03 kare | `kare/C03.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 10 | C03 | `ham/C03_d1.mp4` | Frames to Video (Gemini Omni) | kare/C03.png | 2 | ölçülecek |
| 11 | C04 kare | `kare/C04.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 12 | C04 | `ham/C04_d1.mp4` | Frames to Video (Gemini Omni) | kare/C04.png | 2 | ölçülecek |
| 13 | C05 kare | `kare/C05.png` | Görsel (GPT Image) | ref/3.ANNE_v1.png | 2 | ölçülecek |
| 14 | C05 | `ham/C05_d1.mp4` | Frames to Video (Gemini Omni) | kare/C05.png | 2 | ölçülecek |
| 15 | C06 kare | `kare/C06.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 16 | C06 | `ham/C06_d1.mp4` | Frames to Video (Gemini Omni) | kare/C06.png | 2 | ölçülecek |
| 17 | C07 kare | `kare/C07.png` | Görsel (GPT Image) | ref/3.ANNE_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 18 | C07 | `ham/C07_d1.mp4` | Frames to Video (Gemini Omni) | kare/C07.png | 2 | ölçülecek |
| 19 | C08 kare | `kare/C08.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 20 | C08 | `ham/C08_d1.mp4` | Frames to Video (Gemini Omni) | kare/C08.png | 2 | ölçülecek |

Toplam: 12 görsel çıktı (4 referans sayfası + 8 kare) × 2 deneme + 8 video × 2 deneme = en çok 40 üretim. İkinci denemeler: `ham/C01_d2.mp4` … `ham/C08_d2.mp4`.

## PİLOT SORUSU

> Pilot ölçülmedi (sahip pilotu beklemeden F5'e geçti, AŞILAN KAPILAR 17.10.2026); sorular F7'de bu grubun C01 ve C06 üretiminde cevaplanır. `PROMPTLAR/PILOT.md`'den birebir.

| Çekim | Bu denemenin cevaplayacağı soru |
|:--:|---|
| C01 | Göz kapağı organik açılıyor mu — yuvarlak yüzey taş küre gibi kalıp başka bir yüze dönüşmeden, ikinci göz çıkmadan, tek amber göz tam açılıyor mu (hook'un tek taşıyıcısı) ve Khev ikinci adımda ayağı yerdeyken duruyor mu? |
| C06 | Kare düzeyinde: dev manta ilk karede tam gövde mi ve hilal alın + açık yüzgeç siluetiyle Oru'nun erişkini olarak okunuyor mu (sesi kapalı, başlıksız izleyici "bunlar akraba" diyebiliyor mu — F3 ÖLÜMCÜL); Oru'nun başı ve sağ yüzgeci Khev'in omzunun yanında açık siluet mi? |

---

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · `.claude/agents/goruntu-yonetmeni.md` § Bitirmeden önce)

> Elle tarama (bu ajanda kabuk yok, `film_dogrula.py` koşulmadı; Fable koşar). Kimlik cümlesi sayımı ve DERS taraması Grep ile yapıldı: Y1 (ISARET kelimesi yok) · Y2 (ekli her referansın en az bir cümlesi birebir) ·
> Y5 (`smoke/steam/mist/fog/vapor/plume/exhaust/drip/splash/bubble/wet/rain/flame` Görsel ve Video'da yok; `spray`/`cloud`/`surf`/`ridge` listede yok) · Y8 (ekran/gösterge/`status` yok) ·
> Y10 (`slow` her videoda en çok 2) · Y13 (Video'da `sound/audio/ambient/hum/echo/noise/music` yok). `body` · `wound` · büyük harfli KHEV/ORU ve çekim kodu hiçbir promptta yok.
> C01 ve C06 satırları pilot satırlarıdır (birebir); düzeltme soruları o bölümlerin PILOT'taki hâline aittir.

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C01 | **2** (Oru ekli referans değil ama kadrajda: 2.a birebir metinle; plan "tiny teal creature" diyordu) · **3** (planın ortak cümlesi `cold indigo and teal night light` ve `without lettering, logos, or watermarks` taşıyordu → ışık 4 · "ışık" satırına, yazı kilidi `plain unmarked surfaces`e taşındı; FILM §3 ORTAK GÖRÜNÜM bu hâliyle KABUL) · **4** (kemer ağzının ardı `dark stone inner wall`; Khev'in önü deniz, ardı kamera tarafı) · **7** (Reference 3 plandaki "distant organic eye" yerine yalnız ③ panelini ister: kapak aralığı + amber göz) · **8** (planın üç `Sound:` satırı ve "Environmental sound…" kuyruğu atıldı; Video'da ses/çağrı kelimesi yok) | **1** işaret yok (Khev'in giysisi/işareti yok; sol kaval cümlesi sayı+taraf+konum taşır) · **5** akışkan yok (yalnız `cloud strands`) · **6** ekran yok |
| C02 | **2** (Khev yüz + gövde ve uzuvlar birebir; Oru 2.a · 2.b · 2.c · 2.f birebir; dev mantanın gözü 3 · göz cümlesi birebir, "far out of focus … no sharp detail" cümleyle bağlandı) · **4** (Khev'in arkası: bulanık bazalt kıyı; ön kolların kadraja alt kenardan girdiği ve ellerin kadraj dışı kaldığı yazıldı) · **7** (Reference 3 yalnız açık amber gözün rengi + yuvarlak biçimi, ④ paneli; üç ışık ve zırh istenmedi; Reference 1 yüz + ön kol paneli, sağlam-kaval paneli anılmadı: kaval kadrajda yok; Reference 2 kucak + yüz yakın + sol yüzgeç arka kenarı, sarkık-yüzgeç paneli anılmadı: C15 durumu) · **8** (planın `Sound:` satırları ve ortak ses kuyruğu atıldı; Video'da ses/çağrı kelimesi yok; `slowly` 1; zıt istek yok: ışıklar tek tur parlar, sonra sönükleşir; plandaki "injured left fin" → `notched left fin`, `injured` yazılmadı) | **1** işaret yok (Oru çentiği: sayı `one` + taraf `left fin` + konum `trailing edge` + `the only notch`; ışıklar `the only amber lights on it`) · **3** ortak cümle ışık/su/gezegen/ses taşımıyor · **5** akışkan yok · **6** ekran yok · **gök/gaz devi cümlesi yazılmadı:** kadrajda değil ve sağ üstteki odak dışı amber yuvarlakla aynı köşede çakışıp ikinci göz riski doğururdu; yalnız mekân ışığı cümlesi var (3 · FILM §3 "her dış çekim" ile bilinçli sapma, Fable'a not) |
| C03 | **2** (Khev arkadan baş-omuz + gövde ve uzuvlar + sol kaval birebir; Oru gövde ve boy birebir: ekli değil ama kadrajda; dev manta baş zırhı · göz · üç ışık · yüzgeçler ve kuyruk birebir) · **4** (kemer ağzının ardı iç duvar; Khev'in ardı kemer/kamera, önü deniz; dev mantanın gövdesinin bulut yığınının ardında kaldığı yazıldı; görünen tek açıklık kemer) · **7** (Reference 3 yalnız ④ baş-göz-açık + sol profil panelindeki yüzgeç kenarı; ışık yanık/sönük panelleri istenmedi; Reference 4 yalnız master panel, kemer-ağzı paneli istenmedi) · **8** (Video'da ses kelimesi yok; `slow` yok; "süzülme" kelimesi yok, yüzgeç "climbs/rising"; son vuruşta donma ifadesi yok) | **1** işaret yok · **5** akışkan yok (yalnız `cloud bank`) · **6** ekran yok · yüzgecin gaz devine değmediği cümleyle yazıldı (T15) |
| C04 | **1** (Oru ışıkları `the only amber lights on it`; Khev'de işaret yok) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · kucak duruşu birebir; dev manta yüzgeçleri cümlesi birebir, "only this one curved fin edge is inside the frame" ile kadraja bağlandı; eller yazılmadı: Oru'nun ardında) · **4** (kemer ağzının ardı iç duvar; Khev'in ardı kemer, önü deniz; ayaklar tam kadrajda ve temas gölgeli) · **7** (Reference 1: ¾ yüz + sağ yan tam boy + sağlam kaval; Reference 2: kucak + yüz yakın; Reference 4: kemer-ağzı + master) · **8** (planın `Sound:` satırı atıldı; Video'da ses kelimesi yok; `slow` yok; plandaki "like a shield" nesne doğurmasın diye `in a protective curve … a screen`: kalkan nesnesi değil kolların biçimi) | **3** ortak cümle temiz · **5** akışkan yok · **6** ekran yok · "yana adım" geometrisi: Khev sağ yanı kameraya, yüzü denize; adım kemere doğru geri-yan (tretman: korkudan geri çekiliyor) · Oru'nun çentiği yazılmadı (yüzgeçler yarım kapalı, çentik C04'te bilgi taşımıyor) |
| C05 | **2** (dev manta baş zırhı · göz · üç ışık birebir; yüzgeç ve kuyruk kadrajda değil, yazılmadı) · **4** (açıklık yok; kadrajda yalnız göz ve zırh) · **7** (Reference 3 yalnız ⑤ "ışıklar sönük" paneli; ⑥ "yanık" paneli anılmadı: zıt durum aynı üretimde eşit ağırlıkla verilmez) · **8** (planın `Sound:` satırı atıldı; Video'da ses/çağrı kelimesi yok; `slow` yok; zıt istek yok: ışıklar yanık kalır, göz bebeği son vuruşta iner) | **1** işaret yok (üç ışık `the only lights on her head`) · **3** ortak cümle temiz · **5** akışkan yok · **6** ekran yok · **gök/gaz devi cümlesi yazılmadı:** kadrajda değil (gözün yakını), yalnız ışık cümlesi var (3 · FILM §3 "her dış çekim" ile bilinçli sapma, Fable'a not) |
| C06 | **2** (Oru parçaları 2.a · 2.e · 2.f birebir; ışıklar/yüz kadrajda olmadığı için 2.b yazılmadı — Oru yüzü denizde, kameradan uzak) · **3** (C01 ile aynı ortak cümle düzeltmesi) · **4** (kemer ağzının ardı iç duvar; Khev'in önü deniz, ardı kemer çukuru; ufuk dev mantanın ardında) · **7** (Reference 2 yalnız kucak duruşu + üstten panel; Reference 3 yalnız ¾ önden tam boy panel) · **8** (planın "Sound: … three-note calls overlap" satırı atıldı; `calls` kelimesi yok) | **1** işaret yok · **5** akışkan yok (`cloud strands`, `water` yalnız deniz yüzeyi) · **6** ekran yok |
| C07 | **2** (dev manta baş zırhı · göz · üç ışık · yüzgeçler ve kuyruk birebir; kemer + kemer ağzı + teras birebir) · **3** (plandaki `cold indigo and teal night light` ve yazı kuyruğu ortak cümleden çıkmıştı; ışık 4 · "ışık" satırında) · **4** (kemer ağzının ardı iç duvar, kemer çok küçük; kıyı solda ve altta, deniz sağda, tek sırtın nereden nereye gittiği yazıldı) · **5** (açık deniz ve kıyı: akışkan serbest, ama Y5 listesindeki kelimeler yok — `ridge · spray · stones`; "köpük çoğalması" istenmedi, `wave` yok, tek sırt) · **7** (Reference 3 yalnız sol profil tam boy panel; Reference 4 master + kemer-ağzı) · **8** (planın `Sound:` satırı atıldı; Video'da ses kelimesi yok; `slow` yok; T08 "süzülür" yok → `advances`; zıt istek yok: mantanın ilerlemesi ve duruşu ardışık vuruşlarda) | **1** işaret yok · **6** ekran yok · kıyı sahnesi vakum/kuru kabin değil: atmosferli dünyada deniz ve sprey meşru |
| C08 | **1** (Oru ışıkları `the only amber lights on it`; Khev'de işaret yok) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · kucak duruşu birebir; kemer · kemer ağzı · teras · alt çıkıntı · çıkıntı yüksekliği birebir) · **4** (kemerin ardı iç duvar; çıkıntının arkası dik duvar ve denize açık yan yazıldı; geçidin ucunun denize açık olduğu yazıldı) · **5** (çıkıntı kuru: `the shelf itself stays dry`; deniz yalnız dış kenara vuruyor, `splash/wet` yok) · **7** (Reference 1 sağ yan tam boy + sağlam kaval; Reference 2 kucak + yüz yakın; Reference 4 master + kemer-ağzı) · **8** (planın `Sound:` satırı atıldı; Video'da ses kelimesi yok; `slow` 1 ("very slow push-in"); plandaki "restrained slow push" koşullu: coğrafya bozulursa d2 sabit kamera) | **3** ortak cümle temiz · **6** ekran yok · kamera itmesi plan kararıyla koşullu (FILM §4 C08 · F3 KARAR 9) |
