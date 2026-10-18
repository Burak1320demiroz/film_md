# 🖼️ MOONMOTHER — Prompt grubu G03 (çekimler C17–C24)

> Yazan: goruntu-yonetmeni (F5 tur 1, 17.10.2026). Denetleyen: devamlilik · teknik-danisman.
> Prompt gövdesine çekim kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Üretim yolu (FILM.md künye URETIM): **GPT Image** (başlangıç kareleri) → **Gemini Omni 1.1 Flash** (10 s video, Gemini uygulaması). Referans sayfaları G01'de (`## REFERANS PROMPTLARI`); bu grupta yazılmaz.
> Omni'ye yalnız onaylı tek başlangıç karesi gider (`kare/Cxx.png`); panel sayfası Omni'ye girdi olmaz (GPT_IMAGE_OMNI §4, §7). Ayrı başlangıç/bitiş karesi yok → zincir yok.
> Model sesi KAPALI: planın "Sound:" satırları ve "Environmental sound and nonverbal alien calls only…" kuyruğu video promptlarına GİRMEZ (ses F4'te kurulur); Video'da `call`, `sound`, `hum` yok.
> Kaynak: `FILM.md` §3 (KİMLİK CÜMLELERİ · ORTAK GÖRÜNÜM) · §4 (C17-C24 + altındaki notlar bloğu; C20 sahip kararı 17.10.2026) · `ODA/F3_yonetmen_2.md` §4 · `ODA/F3p_yonetmen_1.md` · `ODA/SAHIP_PLANI.md` ·
> `PROMPTLAR/G01.md` (örnek grup; kimlik, işaret, yazı kilidi, mekân ışığı ve ortak görünüm cümleleri oradan birebir) · `ODA/F5_birlestirme_1_G01.md` (tur 1 kararları) · `PROMPTLAR/PILOT.md` (`## C20` buraya taşındı) · `NOTLAR.md` KARARLAR 17.10.2026 (C21 · C22 · C23: Oru yüzgecin sığ kıvrımında) ·
> `GPT_IMAGE_OMNI_KILAVUZU` · `KIMLIK_VE_REFERANS_KILAVUZU` · `UZAY_FIZIGI_GORUNTU_KILAVUZU` §3 §8 · `GOSTERIM_COZUMLERI` · `PROMPT_HATA_ATLASI` · `GECIS_VE_SES_SUREKLILIGI` §1 · `BILINEN_TUZAKLAR` §A §C.
> G01 tur 1 birleştirme kararları bu grupta da uygulandı: panel **içeriğiyle** adlandırılır (etiket yok) · çatlaklı çekimde yalnız `cracked left-shin panel`, sağlam panel anılmaz · kamera hareketi ayrı cümle ·
> YEDEK satırı başlangıç durumunu değiştiriyorsa yedek karenin Video'su tam yazılır (sonunda ORTAK GÖRÜNÜM) · `Oru's teal is one shade lighter than the night around it.` Oru'nun görünür olduğu her çekimde (C24 siluet ölçeği hariç) ·
> gaz devi kadrajda değilse `a thin pale rim light from the upper right` ışık cümlesi (C18, C23) · d2 satırında üçüncü deneme kuralı · `body` · `wound(ed)` · `injured` · `screen` · büyük harfli KHEV/ORU hiçbir blokta yok.
> Hat dışı sapma yok; FILM §4 ile ayrılan yerler `## FABLE'A NOTLAR`'da (C21 · C22 referans seti, C24 şafak ışığı, kıvrık uçta Oru cümlesi).

---

## KİMLİK CÜMLELERİ

> Ana kaynak `FILM.md` §3 `### KİMLİK CÜMLELERİ` (yeniden yazılmadı). Kadrajda görünen her parça Görsel promptlara kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (Khev · Oru · the mother manta).
> Aşağıdaki iki satır FILM.md §3 tablosunda henüz yok (F5 tur 1, G03). **Fable FILM §3 tablosuna kopyalar** (No 3 ve No 4 satırı olarak).

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 3 | Oru kıvrık uçta (C21 C22 C23; C20 sonundan) | Oru rests inside the bowl; the rim stays lower than Oru's eyes, crescent crest and three lights, and a thin dark gap separates the rim from Oru all the way round. |
| 4 | ışık — şafak kenarı kadrajda (C24) | The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence and from the one thin warm dawn edge on the horizon at the right. |

---

## C17 — Küçük çağrı: Oru göğe kaldırılıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C17.png)
EKLE      başlangıç karesi: kare/C17.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with the right fin spread open and the left fin half open and drooping, the face close-up panel and the left-fin trailing-edge panel.

A medium-low night shot on the lower ledge, the camera low and a little below Oru, in front of Khev and about forty-five degrees to the left of the direction he is looking, standard lens, shallow depth of field. Khev kneels at the left of the frame on his right knee with his left leg stretched out in front of him, his chest in three-quarter view toward the camera and his face tilted down toward Oru. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. That shin plate lies along the lower edge of the frame. His two forearms carry Oru from beneath, level and steady, and his hands are hidden behind Oru.

Oru rests in the cradle of his forearms at the height of his upper chest, at the right of his face, its head raised and turned toward the camera and its left side toward the camera. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's three lights glow faintly and evenly, and its face, crescent crest and lights stand fully clear of Khev's forearms. Oru's teal is one shade lighter than the night around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. Behind Khev at the left, that rear rock face stands out of focus. At the right, beyond the edge of the ledge, one low broad ridge of dark water lies on the blurred sea.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of Khev's head. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Khev lifts his head from Oru and turns his face up and to the right toward the open sky, and Oru stretches its raised head up in the same direction; Khev's forearms stay level under Oru. 3-7 s: Oru's three amber lights brighten one at a time from left to right and stay bright until all three burn together, while Khev keeps his face turned to the sky. 7-10 s: Oru's three lights stay lit and its head stays up and open toward the camera; in the blurred background the dark ridge swells higher and a fine spray lifts from its crest, and Khev's forearms stay level beneath Oru. The camera makes a very slow push-in toward Oru throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev diz çökmüş: sağ diz yerde, sol bacak önüne uzatılmış; sol kaval plakasında TEK çapraz çatlak (içinde amber parıltı) alt kenarda okunuyor, sağ kavalda çatlak yok · iki ön kol Oru'nun altında düz ve sabit, eller Oru'nun ardında, kadrajda parmak yok ·
             Oru Khev'in ön kolundan kısa, yüzü kameraya dönük, hilal alın ve sol gözün altında TEK sıra üç oval ışık (yan yana, eşit aralıklı, hafif ve eşit parlaklıkta) kolla örtülmüyor · sağ yüzgeç açık, sol yüzgeç yarım açık ve sarkık, sol yüzgeçte tek V çentik · Oru ortamdan bir kademe açık teal ·
             Khev'in yüzü aşağı, Oru'ya dönük başlıyor (göğe bakış videonun işi) · dik arka duvar solda odak dışı, alçak sırt ve deniz sağda odak dışı · gaz devi sağ üstte tek, Khev'in başına değmiyor · yazı yok · 16:9 piksel
YEDEK        (F3 KARAR 9) itme yüzü ya da coğrafyayı esnetirse: d2 aynı promptta yalnız kamera cümlesi değişir, "The camera makes a very slow push-in toward Oru throughout." yerine "The camera stays locked throughout."
             Eller kadrajda belirir ya da parmak kaynaşırsa (T01) tek düzeltme:
             "Edit the supplied frame. Change only Khev's hands: they are hidden behind Oru and no fingers show. Keep Khev's face, forearms, Oru, the ledge, the sky, the light and the camera angle exactly as they are."
             Işık sayısı 2 ya da 4 çıkarsa (T09) tek düzeltme (Video değişmez):
             "Edit the supplied frame. Change only the lights beneath Oru's left eye: exactly three separate, evenly spaced, faintly glowing amber ovals in one row. Keep Oru's face, Khev, the ledge, the sky, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans) ya da yukarıdaki sabit-kamera varyantı; d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C18 — Çağrı cevap buluyor: göz bebeği boş terastan çıkıntıya iniyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C18.png)
EKLE      başlangıç karesi: kare/C18.png · referans (yükleme sırası): ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 3 (mother manta): take her left eye, the pitted silver-grey armour around it and the three oval lights beneath it from it, using the close eye panel with the three lights dim and dark.

An extreme close-up night shot of the left eye of the mother manta, seen from slightly below, the camera a little under eye level so that her thick lower eyelid curves across the foreground, the eye and the armour around it filling the whole frame, medium telephoto lens, shallow depth of field. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. The eyelid is fully open, its thick lower edge curving under the amber iris, and the glossy dark pupil is turned up and to the left of the frame. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At the start the three lights are dim: three separate, evenly spaced, dark copper-toned ovals in one row. A thin curtain of pale spray and cloud drifts across the eye and the armour from right to left, and the surface behind it is clearly organic, with the pits and plate seams of living armour. The eye glows faintly amber against the dark armour.

The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: a thin curtain of spray and cloud flows across the mother manta's eye from right to left while her pupil stays turned up and to the left. 3-6.5 s: her pupil makes one deliberate movement down and comes to rest at the lower left of the centre of the frame, while the spray keeps flowing across the eye. 6.5-10 s: the three oval lights beneath her eye glow amber one at a time from left to right and stay lit, and her thick lower eyelid rises a little and softens. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç AYRI, eşit aralıklı, SÖNÜK (bakır tonlu) oval, tek sıra, gözün altında (iki ya da dört değil) · tek göz, göz bebeği sol üstte (bakış yukarı-sola), kalın alt göz kapağı ön planda ve hafif alttan görünüyor · yüzey organik zırh (çukurlar ve plaka dikişleri; taş yüzey değil) ·
             sprey ve bulut perdesi anatomiyi değiştirmiyor, göz yüzeyinde damla ya da ıslak parıltı yok · ayna çifti C05'ten ayrışır: düz karşı + yatay bulut telleri + göz bebeği ortada (C05) ↔ hafif alttan + sprey perdesi + göz bebeği sol üstte (C18) · kadrajda başka varlık yok (gaz devi, halka, ikinci yuvarlak yok) · yazı yok · 16:9 piksel
YEDEK        (T09) ışık sayısı 2 ya da 4 çıkarsa tek düzeltme (Video değişmez):
             "Edit the supplied frame. Change only the lights beneath the eye: exactly three separate, evenly spaced, dim ovals in one row. Keep the eye, the armour, the spray, the light and the camera angle exactly as they are."
             Göz bebeği inişi tutmazsa (şekil bozulur, ikinci göz bebeği, göz kayar) kare göz bebeği baştan sol alt-ortada başlar, tek düzeltme:
             "Edit the supplied frame. Change only the pupil: it now rests at the lower left of the centre of the eye. Keep the eyelids, the armour, the three dim lights, the spray, the light and the camera angle exactly as they are."
             Video (yedek kare; sonunda ORTAK GÖRÜNÜM birebir): "0-3 s: a thin curtain of spray and cloud flows across the mother manta's eye from right to left. 3-7 s: the three oval lights beneath her eye glow amber one at a time from left to right and stay lit. 7-10 s: her thick lower eyelid rises a little and softens while the spray keeps flowing across the eye. The camera stays locked throughout."
             (bakışın boş terastan çıkıntıya inişi bilgisi yedekte C16→C17 kesmesi ve C19 yüzgecine kalır; tanıma jesti zayıflar, ışık yanışı kalır)
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C19 — Canlı köprü: yüzgeç ucu suyu kabartmadan çıkıntının yanına iniyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C19.png)
EKLE      başlangıç karesi: kare/C19.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the panel with the right fin spread open and the left fin half open and drooping and the face close-up panel. Reference 4 (shore): take the lower rock ledge with its steep rear face, the dark sea and the cupped fin tip beside the ledge from it, using the panel with the fin tip beside the ledge.

A wide low night shot along the lower ledge, the camera close to the rock, wide-angle lens, deep focus. Khev kneels at the left of the frame, about one fifth of the frame height, his face turned to the right toward the fin. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Khev presses Oru against his chest with both forearms, his hands hidden behind Oru. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. At this distance Oru is a small deep-teal shape with its three tiny amber lights on the camera side. Oru's teal is one shade lighter than the night around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. That rear rock face stands behind Khev at the left. At the right of the frame the mother manta's cupped fin tip hangs beside the ledge about as high above the rock as Khev is tall, separated from the ledge by a narrow gap, and the water beneath the fin lies flat. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. The fin continues past the right edge of the frame, joined to the mother far out at sea. Far at the right, a single broad dark wave ridge rises on the horizon.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of the fin. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: the cupped tip of the mother manta's left fin lowers heavily toward the ledge above the flat water. 4-7 s: the fin tip settles until it rests almost level with the ledge, keeping the narrow gap between its edge and the rock and touching neither Khev nor Oru, and its amber veins glow brighter. 7-10 s: the fin tip and the water beneath it stay level and flat while the far wave ridge on the horizon creeps closer; Khev stays kneeling where he is, his face turned toward the fin. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç ayrı beden: Khev (sol kaval çatlağı bu geniş planda küçük ayrıntı, okunması beklenmez), Oru Khev'in göğsünde küçük teal şekil, yüzgeç (gümüş-mavi, dev) · yüzgeç ucu çıkıntının YUKARISINDA (Khev boyu kadar), dar boşluk her yanda, kimseye ve kayaya değmiyor ·
             yüzgeç ucunun yuvarlak kenarı DÜZ yatıyor (kıvrık değil), altındaki su düz ve sakin, sırt kabarmıyor · yüzgeç sağ kenardan devam ediyor, ikinci yüzgeç, el ya da dokunaç yok · ufukta sağ uzakta tek dalga sırtı · gaz devi sağ üstte tek, yüzgece değmiyor · Oru ortamdan bir kademe açık teal · yazı yok · 16:9 piksel
YEDEK        alçalma tutmazsa (yüzgeç suyu kabartır, Khev'e değer ya da kopar): kare yüzgeç ucu baştan çıkıntıyla neredeyse aynı seviyede başlar, tek düzeltme:
             "Edit the supplied frame. Change only the fin tip: it now rests almost level with the ledge, separated from the rock by a narrow gap, and the water beneath it lies flat. Keep Khev, Oru, the ledge, the sea, the sky, the light and the camera angle exactly as they are."
             Video (yedek kare; sonunda ORTAK GÖRÜNÜM birebir): "0-4 s: the amber veins of the fin tip glow brighter while the far wave ridge on the horizon creeps closer. 4-7 s: the broad cupped surface settles with a faint give while the narrow gap to the rock stays and the fin touches neither Khev nor Oru. 7-10 s: the fin tip and the water beneath it stay level and flat while the far wave ridge creeps closer; Khev stays kneeling where he is, his face turned toward the fin. The camera stays locked throughout."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C20 — Yavru annesine ulaşıyor: yüzgeç ucu Oru'yu çanak gibi sarıyor (pilot çekimi)

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C20.png)
EKLE      başlangıç karesi: kare/C20.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with the right fin spread open and the left fin half open and drooping. Reference 4 (shore): take the lower rock ledge with its steep rear face, the dark sea and the cupped fin tip beside the ledge from it, using the panel with the fin tip beside the ledge.

A medium-close night shot on the lower ledge, the camera a little above ledge height in front of Khev and slightly to his left, tilted down about 15 degrees, standard lens, shallow depth of field. Khev sits at the left of the frame with his chest in three-quarter view toward the camera and his face turned to the right toward the fin. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's right leg is folded under him and his left leg is stretched out toward the camera, so that the left shin plate lies along the lower edge of the frame. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Each of Khev's hands has four thick digits in deep-indigo skin. Khev holds both forearms out in front of him, open, palms up, forming an open cradle, both hands fully inside the frame.

Oru hovers on its own fins a hand's breadth above his open forearms without touching them, its torso angled toward the fin and its head turned toward the camera. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's three lights glow steadily. Oru's teal is one shade lighter than the night around it.

At the right of the frame, the mother manta's cupped fin tip rests almost level with the ledge, separated from the rock by a narrow gap, and the water beneath the fin lies flat. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. Seen from slightly above, the cupped upper surface is visible and the rounded edge of the tip lies flat, level with the rest of the surface. The fin tip lies less than a metre beyond Khev's open hands. The fin continues past the right edge of the frame, joined to the mother far out at sea. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. That rear rock face stands behind Khev at the left. Far beyond the fin, a single broad dark wave ridge rises on the horizon at the right.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. The pale rim light reaches the foot of the rear rock face and picks it out from the shadow.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-2.5 s: Oru flutters its right fin and rises a little higher above Khev's forearms, its drooping left fin trembling; Khev keeps his forearms open, palms up, and his gaze follows Oru. 2.5-5 s: Oru slips out from above his forearms, makes one short soft glide across the narrow gap with its head turning toward the fin, and lands with its belly on the cupped surface of the fin as a separate small teal creature. 5-8 s: the rounded edge of the fin tip slowly bends upward and inward behind Oru on the side away from the camera and along both of Oru's sides, curling around it like a shallow bowl as one continuous smooth curve; the rim rises only about halfway up Oru's torso, stays lower than Oru's eyes, crescent crest and three lights, and keeps a thin dark gap from Oru all the way round, while the side facing the camera stays low and open and the water beneath the fin stays flat. 8-10 s: Oru turns its head back toward Khev and its three lights brighten while the amber veins of the fin pulse; Khev keeps his forearms open and empty and stays seated, and the dark wave ridge on the horizon creeps a little closer. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç ayrı beden: Oru kollardan ve yüzgeçten ayrı, kollarla temas yok (bir karış boşluk) · Oru'nun sağ yüzgeci açık, sol yüzgeci yarım açık-sarkık, tek V çentik sol yüzgeçte, üç ışık yan yana · Oru ortamdan bir kademe açık teal ·
             Khev'in sol kaval plakasında TEK çapraz çatlak (alt kenarda okunuyor), sağ kavalda çatlak yok · her elde dört parmak, eller açık, palmlar yukarı, ikisi de tam kadrajda ·
             yüzgeç ucu çıkıntıya yakın, Khev'in ellerinin bir metreden az ötesinde, dar boşluk, altındaki su düz · yüzgecin yuvarlak kenarı DÜZ yatıyor (tüm kenar yüzeyle aynı yükseklikte, kıvrık değil) ve çanak üst yüzey hafif yukarıdan (≈15°) görünüyor ·
             yüzgeç sağ kenardan devam ediyor, ikinci yüzgeç ya da dokunaç yok · arka plan dik duvar solda · yazı yok · 16:9 piksel
YEDEK A      (TD B5 · süzülüş ya da konma kollara/yüzgece kaynaşırsa) konma kesmeye gider: kare "Oru yüzgeçte konmuş, yüzgeç ucu düz"; d1 karesinden tek düzeltmeyle:
             "Edit the supplied frame. Change only Oru: it now rests with its belly on the cupped surface of the fin, a short way in from the rounded edge, its head turned toward the camera, and Khev's open forearms are empty. Keep Khev, the fin with its flat rounded edge, the ledge, the sea, the light and the camera angle exactly as they are."
             Video (yedek kare A; sonunda ORTAK GÖRÜNÜM birebir): "0-3.5 s: the rounded edge of the fin tip begins to bend upward and inward behind Oru on the side away from the camera and along both of Oru's sides, while the side facing the camera stays low and open. 3.5-7 s: the edge curls on into a shallow bowl as one continuous smooth curve, its rim rising only about halfway up Oru's torso, staying lower than Oru's eyes, crescent crest and three lights and keeping a thin dark gap from Oru all the way round; the water beneath the fin stays flat. 7-10 s: Oru turns its head back toward Khev and its three lights brighten while the amber veins of the fin pulse; Khev keeps his forearms open and empty and stays seated. The camera stays locked throughout."
             "Kollardan yüzgece" bilgisini C19→C20 kesmesi taşır (C15/C21 deseni).
YEDEK B      (sarma da tutmazsa: yüzgeç Oru'ya yapışır ya da içinden geçer, uzuv/dokunaç çıkar, tuzak/yutma okunur) sarma da kesmeye gider: kare A karesinden ikinci geçişle türer (üç referans sınırı); EKLE yalnız ref/3.ANNE_v1.png (10. panel, kıvrık uç; yalnız bu düzeltmede, Omni'ye gitmez):
             "Reference 3 (mother manta): take the curled tip of her left pectoral fin from it, using the curled-tip panel. Edit the supplied frame. Change only the fin tip: its rounded edge now bends gently upward and inward behind Oru on the side away from the camera and along both of Oru's sides, forming a shallow bowl, with the side facing the camera low and open and a thin dark gap between the rim and Oru. Keep Oru, Khev, the ledge, the sea, the light and the camera angle exactly as they are."
             Video (yedek kare B; sonunda ORTAK GÖRÜNÜM birebir): "0-3.5 s: the bent edge of the fin tip rises a little higher and further inward around Oru, keeping its thin dark gap, while the side facing the camera stays low and open. 3.5-7 s: Oru turns its head back toward Khev. 7-10 s: Oru's three lights brighten and the amber veins of the fin pulse; Khev keeps his forearms open and empty and stays seated. The camera stays locked throughout."
             En kötü hâlde kıvrım duran bir durum olur; bilgi (Oru çanak yüzgeçte ↔ Khev'in boş kollarının biçimi) duran karede de okunur.
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez: sebep konma/süzülüş (Oru kollara ya da yüzgece erir) → YEDEK A; sebep sarma (yüzgeç Oru'ya yapışır, uzuv çıkar, tuzak okunur) → YEDEK B; ikisi birden → doğrudan YEDEK B.
```

## C21 — Anne Khev'i de bırakmıyor: Khev yüzgeçte, yüzgeç sabit

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C21.png)
EKLE      başlangıç karesi: kare/C21.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the back-view panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the panel with the right fin spread open and the left fin half open and drooping and the face close-up panel. Reference 3 (mother manta): take the curled tip of her left pectoral fin from it, using the curled-tip panel.

A medium over-the-shoulder night shot, the camera behind and a little to the left of Khev at the height of his shoulders, standard lens, shallow depth of field. Khev's back and shoulders fill the left half of the frame in the foreground, seen from behind and slightly from the left, his head turned to the right toward the fin. Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev leans forward over the fin on his forearms, his shoulders held a little above its surface. Both of his forearms lie flat on the fin and run out through the right edge of the frame, so his hands stay outside the frame. The rest of him is below the lower edge of the frame. At the lower left, behind his shoulder, the black basalt of the ledge ends in a ragged edge, and beyond that edge the dark sea shows the first thin line of white foam.

Ahead of him, filling the middle and the right of the frame, lies the mother manta's immense cupped left fin, level and steady. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. The rounded tip of her left pectoral fin is curled into a shallow bowl, its one smooth rounded edge bending gently upward and inward on three sides and staying low and open on the fourth, with the pale silver-blue ridges and thin amber veins running on across the inside of the bowl. A few steps ahead of Khev the bowl opens low toward him. Oru rests inside the bowl; the rim stays lower than Oru's eyes, crescent crest and three lights, and a thin dark gap separates the rim from Oru all the way round. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's head is turned back toward Khev and its three lights glow steadily. Oru's teal is one shade lighter than the night around it. The fin continues past the right edge of the frame, joined to the mother far out at sea.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of Oru and of the fin. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3.5 s: Khev's shoulders and back give one short jolt and lower onto the surface of the fin, his forearms staying where they lie, and the fin surface keeps its shape under his weight. 3.5-7 s: his shoulders rise and fall with his breath and he turns his head back toward the edge of the rock at the lower left while the thin line of foam creeps up the rock. 7-10 s: Khev turns his head forward to Oru in the bowl and the amber veins of the fin pulse with warm light; the fin stays level and steady. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev'in sırtı ve omuzları sol yarıda ön planda (yüz yok); ön kolları yüzgeç yüzeyinde düz, sağ kenardan çıkıyor, eller kadraj dışı, parmak yok · gövdenin ve bacakların kalanı alt kenarın altında, çatlak kadrajda değil (çatlak/sağlam kaval anılmadı) · omuzlar yüzeyin biraz üstünde başlıyor (oturuş videonun işi) ·
             Oru yüzgecin sığ kıvrımının İÇİNDE, birkaç adım ileride, başı Khev'e dönük; kenar Oru'nun gözlerinden, hilal alnından ve ışıklarından alçak, ince koyu aralık her yanda, alçak açık yan Khev'e dönük · Oru ayrı küçük teal beden (yüzgeçten ve Khev'den ayrık), üç ışık sabit ·
             tek yüzgeç: ikinci yüzgeç, el ya da dokunaç yok; Khev yüzgece kaynaşmamış · kayanın kenarı alt-solda, ilk ince köpük çizgisi uzakta · gaz devi sağ üstte tek, Oru'ya ve yüzgece değmiyor · yazı yok · 16:9 piksel
YEDEK        ön kollar yüzgece kaynaşırsa ya da yüzeye gömülürse (T01 · T10) tek düzeltme:
             "Edit the supplied frame. Change only Khev's forearms: they rest flat on top of the fin surface and run out through the right edge of the frame. Keep his back and shoulders, Oru in the bowl, the fin, the ledge edge, the sky, the light and the camera angle exactly as they are."
             Omuz sarsıntısı gövdeyi yüzeye gömer ya da kaynaştırırsa (riskli an) sarsıntı çıkar; aynı karede Video (sonunda ORTAK GÖRÜNÜM birebir): "0-3.5 s: Khev's shoulders rise and fall with his breath while his forearms stay where they lie. 3.5-7 s: he turns his head back toward the edge of the rock at the lower left while the thin line of foam creeps up the rock. 7-10 s: Khev turns his head forward to Oru in the bowl and the amber veins of the fin pulse with warm light; the fin stays level and steady. The camera stays locked throughout."
             ("Kayadan yüzgece" bilgisini C20→C21 kesmesi taşır; kayadan yüzgece çekiş videoda riskli varyanttır, pilotta ayrı denenir, ana prompta girmez.)
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C22 — Saat ödeniyor: dalga boş çıkıntıyı kaplıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C22.png)
EKLE      başlangıç karesi: kare/C22.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the panel with the right fin spread open and the left fin half open and drooping and the face close-up panel. Reference 3 (mother manta): take the curled tip of her left pectoral fin from it, using the curled-tip panel.

A wide low night shot parallel to the shoreline, the camera low and a little above the level of the ledge, wide-angle lens, deep focus. The dark sea fills the right of the frame, and the black shore runs along the left side and the bottom edge of the frame. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The ledge is empty, in the lower left of the middle of the frame. Far at the left, high above the rear rock face, a tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace, very small. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins.

In the foreground at the right of the middle of the frame, the mother manta's immense cupped left fin has just begun to rise above the ledge, separated from the rock by a narrow gap, and the water beneath the fin lies flat; its cupped upper surface is seen at a shallow angle. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. The rounded tip of her left pectoral fin is curled into a shallow bowl, its one smooth rounded edge bending gently upward and inward on three sides and staying low and open on the fourth, with the pale silver-blue ridges and thin amber veins running on across the inside of the bowl. Oru rests inside the bowl; the rim stays lower than Oru's eyes, crescent crest and three lights, and a thin dark gap separates the rim from Oru all the way round. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's teal is one shade lighter than the night around it.

Two or three steps from the bowl, at its left, Khev sits on the cupped surface with his right leg folded under him and his left leg stretched out in front of him, about one eighth of the frame height, his face turned to the right toward Oru. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him.

One single broad dark wave front rolls in from the right toward the empty ledge, a short way from its outer edge. Far small black islands and a layer of cloud lie on the horizon. A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of the fin. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: the cupped fin lifts evenly away from the ledge, rising with a steady heavy motion, while Khev and Oru stay where they sit on it. 3-7 s: the dark wave front strikes the empty ledge, and water and spray cover its rock surface. 7-10 s: the spray thins out and the ledge lies under the water, the arch showing small and far through the spray; the fin keeps rising with Khev and Oru in place on it. The camera stays locked throughout, and the ledge stays at the same place in the frame while the fin rises. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   üç ayrı beden: yüzgeç (gümüş-mavi, dev), Khev (sol kaval çatlağı küçük ayrıntı) ve Oru (kıvrımın içinde, derin teal, küçük); kimse kayada değil · çıkıntı BOŞ ve KURU, dik arka duvar solda, dalga cephesi sağda çıkıntının dış kenarına bir parça kala ·
             yüzgeç ucu çıkıntının üstüne kalkmaya yeni başlamış, altındaki su düz · Oru kıvrımın İÇİNDE, kenar Oru'nun gözlerinden, hilal alnından ve ışıklarından alçak, ince koyu aralık her yanda · Khev kıvrımın solunda iki-üç adım, yüzü Oru'ya dönük ·
             uzak adalar + ufuk bulutu ölçek ipucu (dalga maket su gibi küçük okunmaz) · kemer solda çok uzakta ve küçük, ardı iç duvar · ikinci yüzgeç, el ya da dokunaç yok · gaz devi sağ üstte tek, yüzgece değmiyor · yazı yok · 16:9 piksel
YEDEK        çıkıntıda biri varsa ya da ıslak/su altında başlıyorsa (T09, T14) tek düzeltme:
             "Edit the supplied frame. Change only the lower ledge: it is empty and dry, and the water beside it is dark and undisturbed. Keep the fin with Khev and Oru, the wave front, the sky, the light and the camera angle exactly as they are."
             Dalga maket gibi küçük okunursa (T03) tek düzeltme:
             "Edit the supplied frame. Change only the wave front: it is one very broad, tall dark front, wider than the whole ledge, with the far islands and the layer of cloud small behind it. Keep the fin with Khev and Oru, the ledge, the sky, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C23 — Korkunun yerini güven alıyor: Oru Khev'in koluna yaslanıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C23.png)
EKLE      başlangıç karesi: kare/C23.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with the right fin spread open and the left fin half open and drooping, the face close-up panel and the left-fin trailing-edge panel. Reference 3 (mother manta): take the curled tip of her left pectoral fin from it, using the curled-tip panel.

A close-medium night shot on the fin, the camera at Khev's seated eye height, at his right side and a little in front of him, standard lens, shallow depth of field. Khev sits at the left of the frame with his right leg folded under him and his left leg stretched out in front of him, his face turned to the right toward Oru and his shoulders raised. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. That shin plate lies along the lower edge of the frame. His right forearm lies along the fin in front of him, toward Oru, and runs out through the right edge of the frame, so his hand stays outside the frame.

Under them spreads the mother manta's immense cupped left fin. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. The rounded tip of her left pectoral fin is curled into a shallow bowl, its one smooth rounded edge bending gently upward and inward on three sides and staying low and open on the fourth, with the pale silver-blue ridges and thin amber veins running on across the inside of the bowl. The bowl lies at the right of the frame beside Khev's forearm, its low open side toward Khev. Oru rests inside the bowl; the rim stays lower than Oru's eyes, crescent crest and three lights, and a thin dark gap separates the rim from Oru all the way round. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's head is raised and turned toward Khev, its left side toward the camera, and its three lights glow steadily. Oru's teal is one shade lighter than the night around it. The warm amber glow of the fin's veins from below catches the ivory plates on the side of Khev's head. Below the rim of the fin a pale bank of cloud lies over the dark sea.

The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Oru eases its head a little closer across the low open side of the bowl toward Khev's forearm while his shoulders stay raised, and the pale cloud drifts beneath the fin. 3-6.5 s: Oru rests its head against Khev's forearm, and Khev's raised shoulders lower; his forearm stays where it lies. 6.5-10 s: Khev turns his face to Oru and his shoulders ease fully down while Oru's head stays against his forearm; the amber veins of the fin pulse with warm light. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev oturuyor: sağ bacak altında, sol bacak önüne uzatılmış, sol kaval plakasında TEK çapraz çatlak (içi amber) alt kenarda okunuyor, sağ kavalda yok · omuzlar kalkık · sağ ön kol yüzgeç boyunca sağ kenara uzanıyor, el kadraj dışı, parmak yok ·
             Oru yüzgecin sığ kıvrımının içinde, Khev'in ön koluna bitişik, başı kalkık ve Khev'e dönük, sol yanı kameraya; kenar Oru'nun gözlerinden, hilal alnından ve ışıklarından alçak, ince koyu aralık her yanda, alçak açık yan Khev'e dönük ·
             Oru sağ yüzgeç açık, sol yarım açık-sarkık, sol yüzgeçte tek V çentik, üç ışık yan yana ve sabit; yüz ve ışıklar kolla ya da kenarla örtülmüyor · Oru ortamdan bir kademe açık teal ·
             yüzgeç damarlarının sıcak ışığı Khev'in baş plakalarına vuruyor (tek sıcak kaynak) · yüzgeçin altında bulut katmanı · Khev ve Oru ayrı bedenler, yüzgeç tek: ikinci yüzgeç, el ya da dokunaç yok · yazı yok · 16:9 piksel
YEDEK        (T01) baş-ön kol teması kaynaşırsa ya da başı kola gömülürse: temas çekimden çıkar, Oru yalnız yaklaşıp durur (yaklaşma bilgisi kalır). Video (aynı kare; sonunda ORTAK GÖRÜNÜM birebir):
             "0-3 s: Oru eases its head a little closer across the low open side of the bowl toward Khev's forearm while his shoulders stay raised, and the pale cloud drifts beneath the fin. 3-6.5 s: Oru's head comes to a stop just short of Khev's forearm with a thin gap between them, and Khev's raised shoulders lower. 6.5-10 s: Khev turns his face to Oru and his shoulders ease fully down; the amber veins of the fin pulse with warm light. The camera stays locked throughout."
             Kıvrım (bowl) kenarı Oru'ya yapışırsa ya da ikinci uç çıkarsa tek düzeltme:
             "Edit the supplied frame. Change only the fin tip: one smooth rounded edge bends gently upward and inward around Oru on three sides and stays low and open on the side toward Khev, with a thin dark gap between the rim and Oru. Keep Oru, Khev, the fin, the cloud, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C24 — Kurtarma tamam: anne ikisini yüzgecinde yükseltiyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C24.png)
EKLE      başlangıç karesi: kare/C24.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions and pale ivory chitin plates from it, using the crouching-pose panel and the cracked left-shin panel. Reference 3 (mother manta): take her complete form and her cupped left fin from it, using the high view from behind and above on the left. Reference 4 (shore): take the small black shoreline, the low violet cloud tops, the thin warm dawn edge and the ringed gas giant from it, using the high dawn-view panel.

An extreme wide, high night shot looking out over the cloud tops from behind and above the left side of the mother manta, the camera high above her, wide-angle lens, deep focus. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At this distance her eye and her lights are too small to read. Her head is far away at the upper right of the frame, small, and her thin tail trails toward the camera. She has two immense silver-blue pectoral fins and one thin tapering tail. Her left pectoral fin has a broad gently cupped upper surface with pale silver-blue ridges and thin amber veins along its shallow folds, and a rounded tip. In the lower half of the frame the cupped left fin lies close to the camera, wide and level, its rounded edge flat.

On the cupped surface of the fin Khev sits as a small dark figure about one tenth of the frame height, and beside him Oru is a smaller dark teal shape. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. At this distance neither shows a face.

Low violet cloud tops lie below and beyond her, and a small black shoreline lies far away at the lower left. Along the horizon at the right lies one thin warm dawn edge. A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The gas giant sits clear of her head and her fins. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence and from the one thin warm dawn edge on the horizon at the right.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: the mother manta rises over the cloud tops and holds her cupped left fin level under the two small figures. The camera begins to pull back and rise in one smooth movement. 4-8 s: her two fins make one restrained organic flex while the cupped left fin stays level; the small black shore at the lower left grows smaller. The camera keeps pulling back and rising. 8-10 s: the mother manta moves on toward the horizon with the cupped fin held level, and the thin warm dawn edge brightens a little. The camera stops. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   tek manta: tek baş (uzakta, sağ üst), iki yüzgeç, tek kuyruk kameraya doğru · çanak sol yüzgeç alt yarıda kameraya yakın ve geniş, kenarı DÜZ (kıvrık değil; 3.ANNE yüksek-açı paneli düzeni) · yüzgeçte Khev (kadraj yüksekliğinin ≈ onda biri, oturmuş) ve yanında Oru: küçük koyu şekiller, yüz okunmuyor ·
             yeni uzuv, ikinci baş, dev el ya da dokunaç yok · alçak mor bulut tepeleri, sol altta uzakta küçük siyah kıyı · gaz devi sağ üstte tek, mantaya değmiyor · sağ ufukta TEK ince sıcak şafak kenarı · boş uzay yok: atmosfer içinde, ufuk eğrisi hafif · yazı yok · 16:9 piksel
YEDEK        iki küçük şekil seçilmezse (T15): yüzgeçte tek koyu küme kabul edilir, iki canlı bilgisi C23 yakın planından gelir; kare değişmez, Video değişmez.
             Baş yönü sola dönerse (plan metni: baş sola; kıyı sağ altta) kabul ya da tek düzeltme:
             "Edit the supplied frame. Change only her heading: her head points toward the upper right of the frame and her tail trails toward the camera, with the small shoreline at the lower left. Keep the fin with Khev and Oru, the cloud tops, the dawn edge, the sky, the light and the camera angle exactly as they are."
             Şafak kenarı kalın ya da pembe/kırmızı gökyüzüne yayılırsa tek düzeltme:
             "Edit the supplied frame. Change only the dawn edge: it is one thin warm line along the horizon at the right, and the rest of the sky stays cold indigo-teal. Keep the mother manta, the fin with Khev and Oru, the cloud tops, the shoreline, the gas giant and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

---

## FLOW İŞ EMRİ

> **Araç (Flow değil):** kareler **GPT Image**'da (ChatGPT Images 2.5 ya da API `gpt-image-2.5-sunburst`), video **Gemini Omni 1.1 Flash** (Gemini uygulaması). `FLOW_GERCEKLERI` Ek 2-3.
> Flow ayarları (Return silent videos, watermark) bu yolda yok; Omni klibin yerel sesi üretilir → **indirildikten sonra kurguda atılır** (model sesi KAPALI, `timeline.json` klip_sesi kapalı). Videoda ses isteği yazılmadı.
> Her kare **yeni sohbette**, onaylı çapa referansları yeniden eklenerek üretilir; önceki karenin çıktısı yeni kareye girdi yapılmaz (KIMLIK §3). Çıktı PNG, piksel oranı **16:9** ölçülür (1536×864 · 2048×1152 · 2560×1440);
> 3:2 çıkarsa merkezden 16:9 kırpılır, esnetme/genişletme yok (GPT_IMAGE_OMNI §13). Her denemede `NOTLAR.md` DENEMELER'e: model adı · eklenen numaralar (`ref 1,2,3`) · giriş/çıkış saniyesi (`medya.py al MOONMOTHER --yaz`).
> Omni'ye yalnız `kare/Cxx.png` yüklenir; panel sayfası yüklenmez. Aynı yapısal hata iki kontrollü düzeltmede kalırsa çekim yeniden tasarlanır (AGENTS §4).
> **Tablo sırası üretim önceliğidir:** C20 (pilot adayı; kıvrım sonucu C21-C23 karelerinin kıvrık-uç durumunu belirler) → C21 · C24 (riskli) → C17 · C19 · C18 → C22 · C23. Dosya adları çekim numarasını korur. C21-C23 kareleri C20 sonucu "kıvrım tutuyor" çıkmadan üretilmez; kıvrım tutmazsa YEDEK A/B'ye göre Fable bu üç karenin kıvrık-uç cümlesini yeniden yazdırır.
> Referans sayfaları (G01) onaylanmadan hiçbir kare üretilmez; 3.ANNE ⑩ paneli (kıvrık uç) sayfada yoksa C20 YEDEK B ve C21-C23 kareleri sayfa v2'ye bağlanır.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C20 kare | `kare/C20.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 2 | C20 | `ham/C20_d1.mp4` | Frames to Video (Gemini Omni) | kare/C20.png | 2 | ölçülecek |
| 3 | C21 kare | `kare/C21.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 4 | C21 | `ham/C21_d1.mp4` | Frames to Video (Gemini Omni) | kare/C21.png | 2 | ölçülecek |
| 5 | C24 kare | `kare/C24.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/3.ANNE_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 6 | C24 | `ham/C24_d1.mp4` | Frames to Video (Gemini Omni) | kare/C24.png | 2 | ölçülecek |
| 7 | C17 kare | `kare/C17.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png (bu sırayla) | 2 | ölçülecek |
| 8 | C17 | `ham/C17_d1.mp4` | Frames to Video (Gemini Omni) | kare/C17.png | 2 | ölçülecek |
| 9 | C19 kare | `kare/C19.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 10 | C19 | `ham/C19_d1.mp4` | Frames to Video (Gemini Omni) | kare/C19.png | 2 | ölçülecek |
| 11 | C18 kare | `kare/C18.png` | Görsel (GPT Image) | ref/3.ANNE_v1.png | 2 | ölçülecek |
| 12 | C18 | `ham/C18_d1.mp4` | Frames to Video (Gemini Omni) | kare/C18.png | 2 | ölçülecek |
| 13 | C22 kare | `kare/C22.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 14 | C22 | `ham/C22_d1.mp4` | Frames to Video (Gemini Omni) | kare/C22.png | 2 | ölçülecek |
| 15 | C23 kare | `kare/C23.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/3.ANNE_v1.png (bu sırayla) | 2 | ölçülecek |
| 16 | C23 | `ham/C23_d1.mp4` | Frames to Video (Gemini Omni) | kare/C23.png | 2 | ölçülecek |

Toplam: 8 kare × 2 deneme + 8 video × 2 deneme = en çok 32 üretim (C20 YEDEK A/B ve C21 sarsıntısız yedek ayrı hak sayılmaz; aynı iki deneme içinde kullanılır). İkinci denemeler: `ham/C17_d2.mp4` … `ham/C24_d2.mp4`.

## PİLOT SORUSU

> Pilot ölçülmedi (sahip pilotu beklemeden F5'e geçti, AŞILAN KAPILAR 17.10.2026); soru F7'de bu grubun C20 üretiminde cevaplanır. `PROMPTLAR/PILOT.md` `## C20`'den (tur 2) taşındı.

| Çekim | Bu denemenin cevaplayacağı soru |
|:--:|---|
| C20 | Oru, Khev ve dev yüzgeç üç ayrı beden olarak kalıyor mu — Oru kollardan yüzgece tek kısa süzülüşle geçip yüzgece ya da kollara erimeden konuyor mu; konduktan sonra yüzgeç ucu kenarı Oru'ya değmeden, Oru'nun arkasında ve iki yanında yukarı bükülüp onu sığ bir çanak gibi çevreliyor mu (tek pürüzsüz kenar: parmak, dokunaç ya da ikinci yüzgeç doğmadan; yardım gibi okunuyor, tuzak ya da yutma gibi değil; Oru'nun yüzü, hilal alnı ve üç ışığı kenarın üstünde açık); sarkık sol yüzgeç ve tek çatlak (çatlak paneli seçiliyor mu) video boyunca tutuyor mu ve ≈9. saniye karesi tek başına okunuyor mu (solda Khev'in boş açık kolları, sağda Oru'yu çevreleyen çanak, aynı yükseklikte)? |

---

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · `.claude/agents/goruntu-yonetmeni.md` § Bitirmeden önce)

> Elle tarama (bu ajanda kabuk yok, `film_dogrula.py` koşulmadı; Fable koşar). Kimlik cümlesi sayımı ve DERS taraması Grep ile yapıldı (kod bloklarının içi çok satırlı desenle ayrıca tarandı): Y1 (ISARET kelimesi yok: `patch/badge/emblem/insignia/decal`, kol-omuz-göğüs bandı yok) · Y2 (ekli her referansın en az bir cümlesi Görsel'de birebir) ·
> Y5 (`smoke/steam/mist/fog/vapor/plume/exhaust/drip/splash/bubble/wet/rain/flame/soot/puddle` Görsel ve Video'da yok; `spray` · `foam` · `cloud` · `wave` · `water` listede yok, atmosferli dünyada meşru) · Y8 (ekran/gösterge/`status`/`screen`/`display` yok) · Y10 (`slow` her videoda en çok 1; C17 `very slow push-in`, C20 `slowly`) ·
> Y13 (Video'da `sound/audio/ambient/hum/echo/noise/music/call` yok). `body` · `wound` · `injured` · büyük harfli KHEV/ORU, referans/çekim kodu ve `Clip n of N` hiçbir kod bloğunda yok. Uzunluk: bkz. satır sonu (Grep eşik taraması).
> Pilot çekimi C20: PILOT.md `## C20` birebir taşındı; G01 ortak kilitlerinden değişen tek cümle `Oru's teal …` (aşağıda) ve YEDEK A/B'ye eklenen tam Video metinleri.

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C17 | **1** (Khev çatlağı: `one diagonal crack` + `left shin plate` + `the only crack on him`; Oru çentiği `one … notch … the only notch on either fin`; ışıklar `the only amber lights on it`) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · çentik · yüzgeç durumu birebir; `Oru's teal …` G01 DV B14 kararı) · **4** (Khev'in arkası: dik arka duvar solda odak dışı, yazılı; çıkıntının ötesi sağda bulanık deniz; kemer kadrajda yok) · **7** (Reference 1: ¾ yüz + çömelme + çatlaklı kaval, SAĞLAM panel anılmadı; Reference 2: yalnız kucakta-canlı durum + yüz yakın + sol yüzgeç arka kenarı, ⑥ yatık anılmadı) · **8** (planın `Sound:` satırı ve "clear three-note call" atıldı, ışık yanışı kaldı; `call` kelimesi yok; `slow` 1; son vuruş donmaz; kamera ayrı cümle; zıt istek yok: itme ↔ sabit yalnız d2'de) | **5** akışkan yok (Video'da yalnız `fine spray lifts from its crest`, atmosferli dünyada) · **6** ekran yok · `kucak duruşu` cümlesi (2.g, `both fins half closed`) KULLANILMADI: kucakta-canlı durum cümlesiyle (2.d: sağ açık, sol yarım açık) çelişir; poz ayrı cümleyle yazıldı (Oru'nun yüzü kameraya, sol yanı kameraya) · eller `hidden behind Oru` (C04/C08 yöntemi), ön kol alt kenara taşımadı · Video'da `Khev holds still` yok: `forearms stay level` |
| C18 | **2** (dev manta baş zırhı · göz · üç ışık birebir; yüzgeç ve kuyruk kadrajda değil, yazılmadı) · **3** (ışık: gaz devi kadrajda değil → `a thin pale rim light from the upper right`, FILM §3 No 4 "gaz devi kadraj dışı" satırı birebir) · **5** (`spray` yalnız bulut ile birlikte ince perde; damla/ıslak göz tarifi yok) · **7** (Reference 3 yalnız ⑤ "ışıklar sönük" paneli; ⑥ "yanık" paneli anılmadı: zıt durum aynı üretimde eşit ağırlıkla verilmez) · **8** (planın `Sound:` satırı atıldı; Video'da ses/çağrı kelimesi yok; `slow` yok; zıt istek yok: göz bebeği önce iner, ışıklar sonra yanar) | **1** işaret yok (üç ışık `the only lights on her head`) · **4** açıklık yok (kadrajda yalnız göz ve zırh) · **6** ekran yok · gök/gaz devi cümlesi yazılmadı: kadrajda değil (yakın göz); yalnız ışık cümlesi · C05 ile ayna çifti kare kabulde yazılı |
| C19 | **1** (Khev çatlağı sayı+taraf+konum+`the only crack on him`; Oru ışıkları `the only amber lights on it`) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · yüzgeç durumu birebir; çentik yazılmadı: bu ölçekte okunmaz; dev manta sol yüzgeç ucu birebir) · **3** (ORTAK temiz) · **4** (Khev'in arkası dik arka duvar, sağda deniz ve yüzgeç; yüzgecin sağ kenardan dev mantaya bağlandığı yazıldı) · **5** (su `lies flat`; yüzgeç suya değmez; Video'da `water` yalnız aynı olumlu hâl) · **7** (Reference 4 yalnız "yüzgeç ucu çıkıntı yanında" paneli; Reference 1 çatlaklı panel; Reference 2 yalnız sarkık-sol-yüzgeç + yüz yakın) · **8** (planın `Sound:` satırı atıldı; Video'da `slow` yok; `süzülür` yok → `lowers heavily`, `settles`; zıt istek yok) | **6** ekran yok · kıvrık uç/sarma bu çekimde yok (kenar `flat`) · yüzgeç ucu başlangıçta çıkıntının ÜSTÜNDE: FILM §3 4.g (`rests almost level`) biten durumu anlatır; kare hareketin başı olduğundan `hangs … about as high above the rock as Khev is tall` yazıldı, 4.g Video 4-7 s sonuç hâli (`rests almost level`) olarak geçer · Oru `kucak duruşu` cümlesi kullanılmadı (C17 ile aynı gerekçe) |
| C20 (pilot) | **1** (PILOT.md'den birebir: çatlak sayı+taraf+konum+`the only crack on him`; her elde dört parmak; Oru çentiği) · **2** (kimlik cümleleri birebir; kıvrık-uç durum cümlesi (3.f) ana kareye GİRMEDİ: kare hareketin başı, kıvrım videonun işi) · **3** (ortak cümle) · **4** (dik arka duvar Khev'in ardında; yüzgeç sağ kenardan devam eder; ötesi deniz ve ufuktaki dalga sırtı) · **5** (`the water beneath the fin lies flat` olumlu hâl) · **7** (Reference 4 yalnız "yüzgeç ucu çıkıntı yanında"; Reference 1 yalnız ¾ yüz + çömelme + çatlak; Reference 2 yalnız sarkık-sol-yüzgeç paneli; Reference 3 ana kareye eklenmedi: üç referans sınırı, ⑩ yalnız YEDEK B ikinci geçişinde) · **8** (planın `Sound:` satırı atıldı; son vuruşta `holds still`/`freezes` yok; `slow` 1; zıt istek yok) · **G01 kilidi uygulandı (değişen tek cümle):** `its teal is one shade lighter than the dark stone around it` → ayrı cümle `Oru's teal is one shade lighter than the night around it.` (G01 DV B14 ile aynı biçim) · YEDEK A/B'ye yedek karenin tam Video'su yazıldı (G01 DV B11) | **6** ekran yok · sarma bir durum değişimidir (`GOSTERIM_COZUMLERI` ilke 6): sahip kararı 17.10.2026, iki kademeli yedek A/B hazır · eller açık ve tam kadrajda (sahip kararı: boş kollar çekimin bilgisi) · Video'da `bowl` ve `rim` kıvrım tarifidir (kimlik cümlesiyle aynı sözlük), nesne değil |
| C21 | **1** (çatlak bu çekimde kadraj dışı: sol bacak alt kenarın altında → çatlak cümlesi ve çatlaklı panel yazılmadı, SAĞLAM panel de anılmadı; Oru ışıkları `the only amber lights on it`) · **2** (Khev arkadan baş-omuz + gövde ve uzuvlar birebir; Oru gövde · yüz · yüzgeç durumu birebir; yüzgeç 3.e + 3.f birebir; yeni cümle `Oru rests inside the bowl; …` bu dosyanın `## KİMLİK CÜMLELERİ` satırı, Fable FILM §3'e kopyalar) · **4** (Khev'in arkası: kayanın kenarı alt-solda yazılı, ötesi köpük çizgisi; yüzgecin sağ kenardan dev mantaya bağlandığı; gökyüzü ve deniz yüzgecin ötesinde) · **5** (`foam` yalnız ince çizgi, `spray` yok; kıvrım suyla ilgisiz) · **7** (Reference 3 yalnız ⑩ kıvrık-uç paneli, NOTLAR KARARLAR 17.10 anahtar cümlesi; Reference 1 yalnız arkadan panel; Reference 2 yalnız sarkık-sol-yüzgeç + yüz yakın) · **8** (planın `Sound:` satırı atıldı; Video'da ses kelimesi yok; `slow` yok; `slides from rock onto fin` videodan çıktı; zıt istek yok: omuz oturuşu ↔ forearms sabit) | **6** ekran yok · **eller kadraj dışı** (FILM: `avuçlar yüzeye bastırılmış`): ön kollar sağ kenardan çıkar; kaynama riski (T01) kadraj dışına alındı, kare kabulde "parmak yok" · **EKLE seti 1·2·3** (FILM §4: 1·2·4): üç referans sınırı için 4.KIYI çıktı, kaya kenarı ve köpük metinle yazıldı (Fable'a not) · Oru yüzgeçte kıvrımın içinde (NOTLAR KARARLAR 17.10) |
| C22 | **1** (Khev çatlağı sayı+taraf+konum+`the only crack on him`; Oru ışıkları `the only amber lights on it`) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · durum birebir; çentik bu ölçekte yazılmadı; yüzgeç 3.e + 3.f; kemer 4.a + 4.b birebir; çıkıntı 4.d birebir) · **4** (kemer ağzının ardı iç duvar yazılı (çok uzak ve küçük); Khev'in ardı: yüzgeç/deniz; çıkıntının ardı dik arka duvar) · **5** (dalga ve çıkıntı: `ridge`, `wave front`, `water`, `spray` yalnız Video'da; `swallow`/`engulf` yok → `cover`; ıslaklık kelimesi yok; çıkıntı Görsel'de kuru) · **7** (Reference 3 yalnız ⑩ paneli; Reference 1 çatlaklı panel; Reference 2 sarkık-sol-yüzgeç + yüz yakın) · **8** (planın `Sound:` satırı atıldı; Video'da `slow` yok; `holds still` yok; kamera cümlesi ayrı, çıkıntı kadrajda sabit kalır — itme/takip yok; zıt istek yok) | **3** ORTAK temiz · **6** ekran yok · **EKLE seti 1·2·3** (FILM: 1·2·4): üç referans sınırı; çıkıntı, kemer ve dalga metinle (FILM §3: su durumları kare promptunun işidir); 4.KIYI ⑦ "dalga altında" paneli zaten sonuç durumu, başlangıç karesine girmez · kemer ağzı cümlesi (4.b) çok uzak ölçekte bile yazıldı: Y7 |
| C23 | **1** (Khev çatlağı sayı+taraf+konum+`the only crack on him`; Oru çentiği ve ışıkları `the only …`) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · çentik · durum birebir; yüzgeç 3.e + 3.f) · **3** (ışık: gaz devi kadrajda değil → No 4 "gaz devi kadraj dışı" cümlesi; sıcak kaynak yalnız yüzgeç damarları) · **4** (Khev'in ardı/altı: yüzgecin altında bulut katmanı, yazılı) · **5** (`mist`/`fog` yerine `a pale bank of cloud`; kıvrımda su yok) · **7** (Reference 3 yalnız ⑩ paneli; Reference 1 çatlaklı panel; Reference 2 sarkık-sol-yüzgeç + yüz yakın + sol yüzgeç arka kenarı) · **8** (planın `Sound:` satırı atıldı; Video'da ses kelimesi yok; `slow` yok; `few centimetres` sayısı yok → `a little closer`; zıt istek yok) | **6** ekran yok · **el kadraj dışı**: sağ ön kol sağ kenardan çıkar (T01; temas yalnız Oru'nun başı ↔ ön kol) · temas yedeği YEDEK'te (Oru yaklaşıp durur) · `kucak duruşu` yerine kıvrımın içinde dinlenme · FILM'in "sağ ön kolunun yanında" korundu |
| C24 | **1** (Khev çatlağı sayı+taraf+konum+`the only crack on him`) · **2** (Khev gövde ve uzuvlar birebir; Oru gövde birebir; dev manta baş zırhı · göz · üç ışık · yüzgeç ve kuyruk · sol yüzgeç ucu birebir; yüz cümlesi (1.a) yazılmadı: bu ölçekte yüz yok) · **3** (ışık: C24'te `warm colour coming only from amber bioluminescence` şafak kenarıyla çelişir → eki `and from the one thin warm dawn edge on the horizon at the right`, bu dosyanın `## KİMLİK CÜMLELERİ` No 4 satırı; ORTAK GÖRÜNÜM temiz) · **4** (açıklık yok; dev mantanın arkası: bulut tepeleri, kıyı sol altta, ufuk) · **5** (vakum değil; `cloud tops`; sıvı yok) · **7** (Reference 3 yalnız yüksek-açı arkadan-sol üstten paneli; Reference 4 yalnız yüksek-açı şafak paneli; Reference 1 çömelme + çatlak) · **8** (planın `Sound:` satırı atıldı; Video'da ses yok; `slow` yok; `glide`/`süzülür` yok → `moves on`; kamera ayrı cümleler, son vuruşta kamera durur; zıt istek yok) | **6** ekran yok · Oru tonu cümlesi yazılmadı (siluet ölçeği) · "beside him Oru" ayrı ya da birleşik şekil: YEDEK'te kabul (TD B7) · C24'ün kare dışı hareketi (yüzgeç esnemesi) tek vuruşta kalır (TD B10 riski bilinçli) |

---

## FABLE'A NOTLAR (F5 tur 1)

```
FILM.md'ye KOPYALA (Fable):
  1. §3 KİMLİK CÜMLELERİ: bu dosyanın `## KİMLİK CÜMLELERİ` tablosundaki iki satır (No 3 "Oru kıvrık uçta" · No 4 "ışık — şafak kenarı"). Sahip ONAY gerekmez (cümle, plan değil).
  2. §4 Referans sütunu: C21 `1.KHEV · 2.ORU · 4.KIYI` → `1.KHEV · 2.ORU · 3.ANNE` ; C22 aynı. Neden: NOTLAR KARARLAR 17.10.2026 3.ANNE ⑩ panelini C21-C23 kare promptunda anahtar cümleyle ister; üç referans sınırı için 4.KIYI çıktı (kaya kenarı, köpük, çıkıntı, kemer metinle). §3 tablo "kullanan çekimler": 4.KIYI'dan C21 C22 çıkar, 3.ANNE'ye C21 C22 eklenir.
  3. C21: "avuçlar yüzeye bastırılmış" (FILM ekranda-görünen) → eller kadraj dışı (kareden okunmaz); ön kollar sağ kenardan çıkar. Neden: T01 kaynama riski, G01 "eller ya tam görünür ya kadraj dışı" kararı.
  4. C19: başlangıç karesinde yüzgeç ucu çıkıntının ÜSTÜNDE (Khev boyu kadar), FILM §3 4.g (`rests almost level`) Video 4-7 s sonucu. Plan metni (yüzgeç çıkıntı yüksekliğine yakın) korunur.
  5. C17 / C19: `kucak duruşu` (2.g `both fins half closed`) kucakta-canlı durum cümlesiyle (2.d) çelişir; C15-C23 kare promptlarında yalnız 2.d ve poz ayrı cümlesi kullanılır (G02 yazarı aynı çelişkiyi C15-C16'da görmeli).
  6. C24: kamera/yön FILM'deki gibi (baş sağ üste, arkadan-sol üstten); plan "baş sola" sapması sahip onayında.
Çözemediğim risk: yok. Açık: (a) C21 omuz sarsıntısı gövdeyi yüzeye gömme riski (T10) ana videoda duruyor, yedek nefes-only Video hazır; (b) C20 kıvrım sonucu C21-C23'ün üç karesini etkiler (iş emri notu); (c) 3.ANNE ⑩ paneli sayfada yoksa C21-C23 Reference 3 satırı geçersiz olur → sayfa v2.
```
