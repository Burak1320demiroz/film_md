# 🖼️ MOONMOTHER — Prompt grubu G02 (çekimler C09–C16)

> Yazan: goruntu-yonetmeni (F5 tur 1, 17.10.2026). Denetleyecek: devamlilik · teknik-danisman. Örnek grup: `PROMPTLAR/G01.md` (kimlik, ışık, yazı kilidi, ORTAK GÖRÜNÜM oradan birebir; G01 tur 1 kararları geçerli: Oru'nun taşındığı yan, panel adlandırma, sayfa/prompt girişinde ad yok, `screen` yok, kamera ayrı cümle, YEDEK'e yedek kare Video'su).
> Prompt gövdesine çekim kodu, "Clip n of N", başlık satırı, referans kodu YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. ≤4.300 karakter.
> Üretim yolu (FILM.md künye URETIM): **GPT Image** (kareler) → **Gemini Omni 1.1 Flash** (10 s video, Gemini uygulaması). Omni'ye yalnız onaylı tek başlangıç karesi gider (`kare/Cxx.png`); panel sayfası Omni'ye girdi olmaz.
> Model sesi KAPALI: planın "Sound:" satırları ve "Environmental sound and nonverbal alien calls only…" kuyruğu video promptlarına GİRMEZ (ses F4'te kurulur). Videoda ses/çağrı kelimesi yok.
> REFERANS PROMPTLARI G01'dedir; bu grupta yazılmaz. Pilot bu grupta yok (pilot ölçülmedi); C09 grubun ilk üretilecek çekimidir (ÖLÜMCÜL düzeltmesi + iki geçiş yöntemi C11 ve C16'yı da sınar).
> **İki geçişli kare (C09 · C11 · C16, FILM §4 "referans sınırı"):** `### Görsel` bloğu **geçiş 1**'dir (1.KHEV · 2.ORU · 4.KIYI, ufuk ucu boş; çıktı `kare/ara/Cxx_g1.png`). `### Görsel geçiş 2 (düzenleme)` bloğu geçiş 1 çıktısını **3.ANNE uzak-baş paneliyle** düzenler (çıktı `kare/Cxx.png`, Omni'ye giden kare). Geçiş 2 ref'i `EKLE` değil `GEÇİŞ 2` satırında durur (ref/3 yalnız o düzenlemede; PILOT YEDEK B ile aynı gelenek). `kare/ara/` alt klasörüdür: `medya.py` kare/ içindeki ara dosyayı "adsız" saymaz.
> Gaz devinin KADRAJDA olmadığı çekimlerde (C12 · C14 · C15) FILM §3 No 4 "ışık — gaz devi kadraj dışı" satırı kullanılır (FILM'de kullanan çekimler `C02 C05`, genişler: `C02 C05 C12 C14 C15`).
> Açılış kuralı yok (C09-C16 ilk 30 sn dışı).

---

## KİMLİK CÜMLELERİ (G02 önerileri · Fable FILM §3 `### KİMLİK CÜMLELERİ` tablosuna kopyalar)

> Ana kaynak `FILM.md` §3 (yeniden yazılmadı). Aşağıdaki iki satır FILM §3'te yok; ikisi de çekim listesinin kendi durum paneline yazı karşılığıdır (2.ORU ⑥ ve ⑦ sayfa promptlarındaki cümleler).
> Neden gerekli: (a) yatık durum (C12 C13 C14) için cümle yok; (b) FILM'deki "kucak duruşu" (`both fins half closed`) C15-C23'ün durum cümlesiyle (`right fin spread open … left fin half open and drooping`) **çelişir** (zıt iki istek, soru 8); kucaklı ve yüzgeçleri açık durumlar için kucak cümlesi yüzgeç ifadesi olmadan yazıldı.

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 2 | yüzgeç durumu: yatık (C12 C13 C14) | Oru's left fin is held stiffly out to the side, away from its torso, unable to open or fold, and its three amber lights glow weakly and unevenly. |
| 2 | kucak duruşu — yüzgeçleri açık durum (C15 C16) | Oru rests in the cradle with its head raised and its belly turned toward its carrier's chest. |

---

## C09 — Khev gölge sınırını geçiyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image iki geçişte (geçiş 1 ref ile, geçiş 2 düzenleme) · video: Gemini Omni 1.1 Flash (yalnız kare/C09.png)
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
GEÇİŞ 2   düzenleme: kare/ara/C09_g1.png üstüne · referans: ref/3.ANNE_v1.png (yalnız bu düzenlemede; Omni'ye gitmez) · çıktı kare/C09.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the right-side full-length panel, the three-quarter face panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and winglike fins from it, using the cradle-pose panel and the face close-up panel. Reference 4 (shore): take the black arch with the shadow line on its floor, the terrace, the causeway, the dark sea and the far black islands from it, using the arch-mouth panel and the wide master panel.

A medium-wide night shot from the side, the camera at Khev's chest height on his right, standard 35 mm lens, deep focus. Khev stands full length in the left half of the frame, about half the frame height tall, in profile with his right side toward the camera, his chest, toes and face turned to the right toward the open sea. The toes of both his feet rest exactly on the shadow line, not yet over it, and both feet are fully in the frame, each with a clear contact shadow. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Khev presses Oru against his chest with both forearms, his hands hidden behind Oru. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Cradled, Oru keeps its head raised, its belly turned toward its carrier's chest and both fins half closed against its torso. Oru's head is turned toward the camera so that its three lights show. Oru's teal is one shade lighter than the night around it.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. It fills the left edge of the frame behind Khev. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The causeway runs on across the right half of the frame, and the dark sea fills the right of the frame and the background. The horizon passes at about two fifths of the frame height from the bottom. A low bank of cloud lies on the horizon at the far right, and a few far small black islands stand on the horizon. On the sea in front of the cloud bank lies one single low dark ridge of water, still far from the causeway and pointing toward the shore.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Görsel geçiş 2 (düzenleme)
```text
Reference 3 (mother manta): take her pitted silver-grey head and her amber eye from it, using the distant-view panel with only a tiny head and eye above a thin horizon line.
Edit the supplied frame. Change only the far right of the horizon: add the mother manta's small distant head rising just above the low bank of cloud, her face turned toward the shore at the left and her left side toward the camera, tiny and without fine detail, with the rest of her hidden behind the cloud. The single dark ridge of water already on the sea lies in front of her, between her and the shore. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At this distance the lights are too small and dim to read. Keep Khev, Oru, the arch, the shadow line, the causeway, the sea, the sky, the light and the camera angle exactly as they are.
```

### Video
```text
0-3 s: Khev lifts his near foot, carries it forward over the shadow line and plants it on the open basalt, his weight passing over it; Oru turns its raised head from the camera toward the horizon at the right. 3-6 s: Khev lifts his rear foot, carries it forward and plants it ahead of the first; the arch behind him grows smaller as the gap between them opens. 6-10 s: Khev comes to a stop on the open causeway with his head raised toward the distant head on the horizon; Oru's three amber lights flash once; the dark ridge on the sea moves closer to the causeway. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   geçiş 1: Khev yandan tam boy, sağ yanı kameraya, yüzü ve göğsü sağa; iki ayağın parmakları gölge çizgisinin ÜSTÜNDE, çizgiyi geçmemiş; iki ayak tam kadrajda, temas gölgeli; kollar Oru'nun çevresinde, eller Oru'nun ardında ·
             Oru Khev'in önkolundan kısa, kucakta, başı kameraya dönük, sol gözün altında TEK sıra üç oval; kemer sol kenarda, ardı koyu taş iç duvar, gölge sınırı net; geçit sağa uzanıyor, ufukta alçak bulut yığını + uzak adalar + tek alçak karanlık sırt · gaz devi sağ üstte, tek · sol kaval sağlam, tek · yazı yok ·
             geçiş 2: ufuk sağ ucunda TEK küçük, ayrıntısız baş (tek amber göz, yüzü kıyıya/sola), gövdesi bulutun ardında; sırt başın ile kıyı arasında; Khev, Oru, kemer, deniz, ışık geçiş 1 ile aynı (yüz ve kucak bozulmamış) · ikinci baş ya da ikinci göz yok · 16:9 piksel
YEDEK        geçiş 2 Khev/Oru yüzünü bozarsa ya da baş büyür/ikilenirse: geçiş 2 atılır, kare = geçiş 1 (ufukta yalnız karanlık sırt kalır; hedef zayıflar, yön kalır: Khev'in ve Oru'nun başı ufka dönük, gidilen yön C08'in denizinden okunur).
             Video (yedek kare; sonunda ORTAK GÖRÜNÜM birebir): "0-3 s: Khev lifts his near foot, carries it forward over the shadow line and plants it on the open basalt, his weight passing over it; Oru turns its raised head from the camera toward the horizon at the right. 3-6 s: Khev lifts his rear foot, carries it forward and plants it ahead of the first; the arch behind him grows smaller as the gap between them opens. 6-10 s: Khev comes to a stop on the open causeway with his head raised toward the horizon at the right; Oru's three amber lights flash once; the dark ridge on the sea moves closer to the causeway. The camera stays locked throughout."
             Yürüyüş tutmazsa (ayak kayması, T10): kare tek düzeltmeyle "Edit the supplied frame. Change only Khev's position: his near foot now stands just over the shadow line on the open basalt and his rear foot is still on the line. Keep Khev's pose, Oru, the arch, the causeway, the sea, the sky, the light and the camera angle exactly as they are."; Video yalnız ikinci adım + duruş: "0-4 s: Khev lifts his rear foot, carries it forward and plants it ahead of the first; Oru turns its raised head toward the horizon at the right. 4-7 s: the arch behind him grows smaller as the gap between them opens. 7-10 s: Khev comes to a stop on the open causeway with his head raised toward the horizon; Oru's three amber lights flash once; the dark ridge on the sea moves closer to the causeway. The camera stays locked throughout." (sonunda ORTAK GÖRÜNÜM birebir)
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C10 — Geçidin ucu düşüyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C10.png)
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası): ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 4 (shore): take the black basalt causeway, its one deep transverse crack, the separated end slab and the dark sea from it, using the panel of the sea end of the causeway with the crack and the separated end slab, and the wide master panel.

A low close night shot straight along the causeway toward the sea, the camera a hand's breadth above the stone, wide-angle 24 mm lens, deep focus. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. Here the camera looks straight along that causeway, so the causeway runs away from the lens toward the sea and the terrace lies behind the camera. In the foreground lies the solid black basalt floor of the causeway. Ahead of it one deep transverse crack cuts across the full width of the causeway, and beyond the crack one short end slab, separated by the crack, lies tilted slightly down toward the sea. Beyond and below the slab lies the open dark sea, and on it one single broad low ridge of water rolls toward the causeway from far out. The horizon passes at about half of the frame height. The frame is an empty place of stone and sea.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3.5 s: the leading curl of the single broad ridge of dark water rises beneath the end of the causeway, washes against the lower edge of the separated slab and lifts spray. 3.5-7 s: the slab tilts further down toward the sea, its outer edge dipping. 7-10 s: the slab drops into the sea and water bursts up beneath it; as the spray falls away, a gap with a fresh broken edge lies between the solid near stone and the open sea. The stone floor in the foreground stays unchanged. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   kadrajda canlı yok · yakın taş zemin sağlam, TEK enine derin çatlak tüm genişliği kesiyor, çatlağın ötesinde TEK kısa uç levha (ayrık, hafif eğik, henüz düşmemiş, boşluk yok), ötesi açık koyu deniz · denizde uzakta TEK geniş alçak sırt · ufuk yaklaşık kadraj yarısında · gaz devi sağ üstte, tek · terasın kendisi kadrajda değil (kamera geçit ekseninde) · yazı yok · 16:9 piksel
YEDEK        (FILM yedek; TD B9) levha ilk karede daha dik eğik/yarı devrilmiş başlarsa kabul; ya da kareyi tek düzeltmeyle eğ: "Edit the supplied frame. Change only the end slab: it now tilts steeply down toward the sea along the deep crack, its outer edge close to the water. Keep the solid near stone, the crack, the sea, the sky, the light and the camera angle exactly as they are."
             Video (yedek kare; sonunda ORTAK GÖRÜNÜM birebir): "0-3.5 s: the leading curl of the single broad ridge of dark water rises beneath the end of the causeway and lifts spray against the steeply tilted slab. 3.5-7 s: the slab tips over the edge of the crack toward the sea. 7-10 s: the slab drops into the sea and water bursts up beneath it; as the spray falls away, a gap with a fresh broken edge lies between the solid near stone and the open sea. The stone floor in the foreground stays unchanged. The camera stays locked throughout."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir (levha kıvrılıp erirse, taş yerine su görünürse: kare düzeltilir, video promptu değişmez). İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C11 — Oru annesine süzülmeyi deniyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image iki geçişte (geçiş 1 ref ile, geçiş 2 düzenleme) · video: Gemini Omni 1.1 Flash (yalnız kare/C11.png)
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
GEÇİŞ 2   düzenleme: kare/ara/C11_g1.png üstüne · referans: ref/3.ANNE_v1.png (yalnız bu düzenlemede; Omni'ye gitmez) · çıktı kare/C11.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the right-side full-length panel, the three-quarter face panel, the forearm-and-hand panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights, winglike fins and fin notch from it, using the top-view panel, the face close-up panel and the left-fin trailing-edge panel. Reference 4 (shore): take the causeway with its fresh broken end, the lower ledge with its steep rear face and the dark sea from it, using the panel of the sea end of the causeway with the fresh broken edge and open sea beyond, the low side-view panel of the lower ledge and the wide master panel.

A medium night shot from the side, the camera at Khev's head height on his right and tilted down about fifteen degrees, standard 35 mm lens, deep focus. Khev stands at the left of centre on the solid near end of the causeway, in profile with his right side toward the camera, his chest and face turned to the right toward the sea; both feet are fully in the frame, each with a clear contact shadow. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Each of Khev's hands has four thick digits in deep-indigo skin. Khev holds both forearms out level in front of him toward the right, one behind the other seen from the side, open and empty, palms up, both hands fully inside the frame.

Oru hovers flat on its own fins a hand's breadth above his open forearms without touching them, its torso angled toward the right and its head turned toward the camera so that its three lights show, both fins spread open. Seen from slightly above, its right fin lies nearer the camera and its left fin lies beyond its torso with its trailing edge in plain view. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's teal is one shade lighter than the night around it.

Behind Khev the causeway runs back toward the terrace and the shore. Ahead of him the causeway ends in a fresh broken edge, and beyond it lies a gap of open air. The lower ledge lies below and ahead of him at the right of the frame. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The lower ledge lies about twice Khev's height below the end of the causeway. The sea breaks against the outer edge of the ledge while the shelf itself stays dry, and open dark sea fills the right of the frame and the background. A low bank of cloud lies on the horizon at the far right, and a few far small black islands stand on the horizon.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Görsel geçiş 2 (düzenleme)
```text
Reference 3 (mother manta): take her pitted silver-grey head and her amber eye from it, using the distant-view panel with only a tiny head and eye above a thin horizon line.
Edit the supplied frame. Change only the far right of the horizon, beyond the gap: add the mother manta's small distant head rising just above the low bank of cloud, her face turned toward the shore at the left and her left side toward the camera, tiny and without fine detail, with the rest of her hidden behind the cloud. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At this distance the lights are too small and dim to read. Keep Khev, his empty open hands, Oru, the broken causeway end, the ledge, the sea, the sky, the light and the camera angle exactly as they are.
```

### Video
```text
0-4.5 s: Oru flutters its fins, rises a little above Khev's forearms and glides forward away from them toward the right, heading for the ledge below and the horizon beyond; Khev's forearms stay level with the palms open. 4.5-7.5 s: Oru's notched left fin goes slack in the air and the glide curves downward; Oru leaves the frame through the lower right corner while Khev's open hands reach forward after it. 7.5-10 s: Khev's hands stay open and empty with the palms up; he lowers his head and turns his gaze down to the ledge, while the sea keeps breaking against the ledge's outer edge. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   geçiş 1: Khev yandan, sağ yanı kameraya, yüzü sağa, geçidin sağlam yakın ucunda; iki ön kol düz ve açık, avuçlar yukarı, her elde DÖRT parmak, iki el tam kadrajda ve BOŞ · Oru ön kolların bir karış üstünde, temas yok, iki yüzgeç açık, sol yüzgecin arka kenarında tek V çentik okunuyor, sol gözün altında TEK sıra üç oval, Khev'in önkolundan kısa ·
             önünde geçidin taze kırık ucu + boşluk; boşluğun ötesinde ve aşağıda kuru çıkıntı (Khev boyunun yaklaşık iki katı), sörf yalnız dış kenarda; ufukta alçak bulut yığını + uzak adalar · gaz devi sağ üstte, tek · sol kaval sağlam · yazı yok ·
             geçiş 2: ufkun sağ ucunda TEK küçük ayrıntısız baş, yüzü kıyıya; Khev'in elleri, Oru ve çıkıntı geçiş 1 ile aynı · ikinci Oru ya da ikinci baş yok · 16:9 piksel
YEDEK        geçiş 2 yüzleri/elleri bozarsa ya da baş ikilenirse: geçiş 2 atılır, kare = geçiş 1 (bilgi Oru'nun ufka dönük başı + C09 ufku ile kalır). Eller kapanır ya da Oru'dan geçerse (T01): kare tek düzeltmeyle "Edit the supplied frame. Change only Khev's hands: both hands are open and empty, palms up, with four digits each, fully visible and clear of Oru. Keep Oru, Khev's pose, the broken end, the ledge, the sea, the light and the camera angle exactly as they are."
             Süzülüş tutmazsa (Oru sıyrılır, kadraj dışına çıkar; Khev'in boş elleri + aşağı bakış aynı bilgiyi taşır). Video (yedek; sonunda ORTAK GÖRÜNÜM birebir): "0-4.5 s: Oru flutters its fins and rises a little above Khev's forearms. 4.5-7.5 s: Oru drops forward and down out of the frame through the lower right corner while Khev's open hands reach forward after it. 7.5-10 s: Khev's hands stay open and empty with the palms up; he lowers his head and turns his gaze down to the ledge, while the sea keeps breaking against the ledge's outer edge. The camera stays locked throughout."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C12 — Oru çıkıntıda yalnız

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C12.png)
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası): ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with Oru lying on dark stone with its left fin held stiffly out to the side, the face close-up panel and the left-fin trailing-edge panel. Reference 4 (shore): take the lower ledge with its steep rear face and the dark sea from it, using the low side-view panel of the lower ledge.

A low close night shot at ledge level, the camera a hand's breadth above the stone and in front of Oru, standard 50 mm lens, shallow depth of field. One small creature lies in the middle of the frame with its belly resting on the dark stone, its head toward the right of the frame and turned toward the camera so that the three lights beneath its left eye show. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's left fin is held stiffly out to the side, away from its torso, unable to open or fold, and its three amber lights glow weakly and unevenly. The stiff left fin stands tilted up at a fixed angle on the far side of its torso, clear above its back and in plain view, while its right fin rests flat on the stone nearer the camera; all three lights stay visible in one row. A shadow under its belly separates it from the stone. Oru's teal is one shade lighter than the dark stone around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The steep basalt face rises behind Oru and fills the left and the back of the frame. Dark water lies beyond the outer edge of the ledge at the right, with a thin line of sea spray along the right edge of the frame, while the stone under and around Oru stays dry. The ledge holds only this one small creature.

The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. The pale light from the upper right reaches the foot of the rear rock face and picks it out from the shadow.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Oru tries to lift its stiff left fin, and the fin rises a little way from the stone. 3-6 s: the fin falls back and Oru settles onto the stone; its three amber lights pulse weakly and unevenly. 6-10 s: Oru's torso rises and falls once with its breath, its left fin trembles once and its lights pulse weakly; at the right edge of the frame a thin line of spray drifts a hand's breadth inward from the sea, while Oru stays dry. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   tek küçük yaratık (Oru), karnı taşta, altında gölge (zemine gömülmemiş) · sol yüzgeç sert, gövdeden ayrık, açılamayan açıda ve sırtının üstünde okunuyor; sağ yüzgeç taşta; sol gözün altında TEK sıra üç oval, zayıf ve farklı parlaklıkta ama ÜÇ · tek V çentik sol yüzgeçte ·
             dik bazalt duvar solda ve arkada, gaz devi ışığıyla dibi seçilir; denize açık sağ kenar, sprey yalnız kadrajın sağ kenarında ince çizgi; Oru'nun üstü ve altındaki taş kuru · Khev kadrajda yok, mavi karın ışığı yok · yazı yok · 16:9 piksel
YEDEK        (FILM yedek) yüzgeç kalkışı üretilemezse (yüzgeç gövdeye yapışır ya da kopar): Video yalnız ışık atımı, 3 vuruş: "0-3 s: Oru's three amber lights pulse weakly and unevenly, one after another. 3-6 s: its torso rises and falls once with its breath. 6-10 s: its left fin trembles once, its lights pulse weakly, and at the right edge of the frame a thin line of spray drifts a hand's breadth inward from the sea, while Oru stays dry. The camera stays locked throughout." (sonunda ORTAK GÖRÜNÜM birebir) — "zayıf ve tek başına" bilgisi kalır.
             Sprey Oru'ya değerse ya da taş ıslak okunursa: kare tek düzeltmeyle "Edit the supplied frame. Change only the spray: it stays at the very right edge of the frame, and the stone around Oru is dry. Keep Oru, the ledge, the wall, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C13 — Khev yavruyu seçiyor ve atlıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C13.png)
EKLE      başlangıç karesi: kare/C13.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the back-view panel, the crouching-pose panel and the intact left-shin panel. Reference 2 (Oru): take its deep-teal form from it, using the panel with Oru lying on dark stone with its left fin held stiffly out to the side. Reference 4 (shore): take the black arch, the terrace, the causeway with its broken end, the lower ledge with its steep rear face, the dark sea and the ringed gas giant from it, using the panel of the sea end of the causeway with the fresh broken edge and open sea beyond, the low side-view panel of the lower ledge with the terrace edge, the arch and the broken causeway end above, and the wide master panel.

A wide night shot from the land side toward the sea, the camera a little above the terrace and behind-left of Khev, wide-angle 28 mm lens, deep focus. Khev crouches in the right half of the frame at the seaward edge of the terrace, where the causeway now ends in a fresh broken edge, about one sixth of the frame height tall, seen from behind at a three-quarter angle from his left, his face turned down and to the right toward the ledge below. Seen from behind, Khev has a broad flattened head and wide shoulders armoured with pale ivory chitin plates. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate is one smooth unbroken ivory plate. Both his feet are planted at the edge, and his empty hands hang between his knees, out of the camera's sight.

Far below him on the ledge, a little to the left of the spot directly under him, tiny Oru lies still on its belly at the foot of the steep rear face. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's left fin is held stiffly out to the side, away from its torso, unable to open or fold, and its three amber lights glow weakly and unevenly. At this distance Oru reads as a small deep-teal shape.

A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. It stands at the left of the frame, a few steps behind Khev and plainly within his reach. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The lower ledge lies about twice Khev's height below the end of the causeway. Open dark sea fills the right of the frame, and on the horizon at the far right lies one single broad dark ridge of water.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4.5 s: Khev looks down at Oru on the ledge below, then turns his head once to the left toward the arch. 4.5-7.5 s: Khev turns his head back down to Oru and plants both feet at the edge, setting his balance forward. 7.5-10 s: Khev pushes off with his feet and his whole figure drops quickly forward and down out of the bottom of the frame; the edge is left empty, the arch stands in place at the left, Oru lies small on the ledge below, and the dark ridge on the horizon moves closer. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Khev arkadan-sol ¾ çömelmiş, terasın deniz kenarında (geçit burada taze kırık uçla bitiyor), yüzü aşağı-sağa; iki ayak kenarda sabit; eller GÖRÜNMEZ (dizler arasında, kadraj dışı); sol kaval sağlam, tek ·
             kemer sol kenarda, Khev'in birkaç adım gerisinde, açıkça erişilebilir; kemerin altı koyu, ardı iç duvar, gölge sınırı net · Oru küçük, Khev'in hemen altında biraz solunda, çıkıntıda dik duvarın dibinde, kıpırtısız, sol yüzgeç sert ayrık; çıkıntı Khev boyunun yaklaşık iki katı aşağıda, kuru ·
             ufukta sağda TEK geniş karanlık sırt · gaz devi sağ üstte, tek · tek Khev, tek Oru · yazı yok · 16:9 piksel
YEDEK        (kurgucu B8) atlayış 7.5-10 s içinde (≈8 s), son ≈1.2 s boş kenar: bozulursa çekim yeniden üretilir, kırpılmaz. Kemere bakış tutmazsa (baş dönüşü gövdeyi döndürürse) tek yön: Video (yedek; sonunda ORTAK GÖRÜNÜM birebir): "0-5 s: Khev looks down at Oru on the ledge below. 5-7.5 s: Khev plants both feet at the edge and sets his balance forward. 7.5-10 s: Khev pushes off with his feet and his whole figure drops quickly forward and down out of the bottom of the frame; the edge is left empty, the arch stands in place at the left, Oru lies small on the ledge below, and the dark ridge on the horizon moves closer. The camera stays locked throughout."
             Eller görünür çıkarsa ya da kenar yanlış çıkarsa (T01): kare tek düzeltmeyle "Edit the supplied frame. Change only Khev's hands: they are hidden between his knees, out of the camera's sight. Keep Khev's pose, Oru, the arch, the ledge, the sea, the light and the camera angle exactly as they are."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C14 — Atlayışın bedeli: çatlak

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C14.png)
EKLE      başlangıç karesi: kare/C14.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the panel with Oru lying on dark stone with its left fin held stiffly out to the side and the face close-up panel. Reference 4 (shore): take the lower ledge with its steep rear face and the dark sea from it, using the low side-view panel of the lower ledge.

A low medium-full night shot at ledge level, the camera a little below Khev's chest height and in front of him, standard 35 mm lens, deep focus. Khev crouches in the right half of the frame with almost all his weight on his right leg, his chest and face turned to the left toward Oru and his left side toward the camera. His left foot rests lightly on the stone beside the right, and his left hand is braced flat on the rock beside it, its four digits spread on the stone and fully in the frame. His right forearm rests on his right knee, its hand hidden behind the knee. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Each of Khev's hands has four thick digits in deep-indigo skin. The crack on his left shin plate faces the camera.

Oru lies on its belly on the stone at the left of the frame, within his reach. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin is held stiffly out to the side, away from its torso, unable to open or fold, and its three amber lights glow weakly and unevenly. Oru's teal is one shade lighter than the dark stone around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The steep basalt wall rises behind both of them and fills the left and the back of the frame. Dark water lies beyond the outer edge of the ledge at the right, with a thin line of sea spray along the right edge of the frame.

The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. The pale light from the upper right reaches the foot of the rear rock face and picks it out from the shadow.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-3 s: Khev tries to shift his weight onto his left leg; the leg gives no support, and his shoulders and torso draw back. 3-6.5 s: Khev bows his head and looks at the crack on his left shin plate. 6.5-10 s: Khev lifts his eyes from the leg and turns his head to Oru, who lies within reach at the left of the frame, and keeps it turned toward Oru; Oru's three lights pulse weakly and a thin line of spray passes the right edge of the frame. The crack on his left shin plate stays exactly as it is. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   sol kaval plakasında TEK çapraz çatlak, kameraya yakın bacakta, içi amber parıltı; sağ kavalda çatlak YOK (zıt panel anılmadı, model sağa da koyarsa YEDEK) · ağırlık sağ bacakta; sol el taşa yaslı, dört parmak tam görünür, taşa gömülmemiş; sağ el görünmüyor · yüzü sola (Oru'ya) ·
             Oru solda taşta, karnı taşta, sol yüzgeç sert ayrık, üç ışık zayıf ama ÜÇ, tek sıra; dik duvar arkada; sprey yalnız sağ kenarda · gaz devi kadrajda değil, ışık sağ üstten · yazı yok · 16:9 piksel
YEDEK        (çatlak sağa kayarsa ya da iki çatlak çıkarsa) tek düzeltme: "Edit the supplied frame. Change only the shin plates: the only crack is the one diagonal crack with a faint amber glow on his left shin plate, the leg nearer the camera, and his right shin plate is one smooth unbroken ivory plate. Keep Khev's pose, Oru, the ledge, the wall, the light and the camera angle exactly as they are."
             Çatlak kareden hazır ve videoda değişmez/oluşmaz (T05); video çatlağı ilk kareye bağlar. Baş dönüşü gövdeyi döndürürse: Video (yedek; sonunda ORTAK GÖRÜNÜM birebir): "0-4 s: Khev tries to shift his weight onto his left leg; the leg gives no support, and his shoulders and torso draw back. 4-10 s: Khev bows his head and looks at the crack on his left shin plate, then lifts his eyes and turns his head to Oru, who lies within reach at the left of the frame; Oru's three lights pulse weakly. The camera stays locked throughout."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C15 — Khev yavruyu yeniden kucağında tutuyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image (ref ile) · video: Gemini Omni 1.1 Flash (yalnız kare/C15.png)
EKLE      başlangıç karesi: kare/C15.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png
```

### Görsel
```text
Reference 1 (Khev): take his face, proportions, pale ivory chitin plates and deep-indigo skin from it, using the three-quarter face panel, the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest, three amber lights and fin notch from it, using the panel with the right fin spread open and the left fin half open and drooping, and the face close-up panel.

A medium-close night shot on the lower ledge, in front of Khev and about thirty degrees above, standard 35 mm lens, shallow depth of field. Khev sits in the right half of the frame, leaning onto his right hip, in three-quarter view with his chest and face turned to the left, his right leg folded under him and his left leg stretched out toward the camera, so that the left shin plate lies along the lower edge of the frame. Khev has a broad flattened head armoured with pale ivory chitin plates and a smooth flat face whose only features are two glossy black eyes on its sides and one small rigid mouth seam, with three fine dark indigo gill slits on each side of his neck. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. Khev's forearms are already beneath Oru's whole torso, carrying it in a cradle against his chest a hand's breadth above the stone, his hands hidden beneath and behind Oru and not touching its fins.

Oru rests in the cradle with its head raised and its belly turned toward its carrier's chest. Its head is turned toward the camera so that its three lights show. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's left fin has one small dry V-shaped notch in its trailing edge, the only notch on either fin. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's three lights glow steadily and evenly, and its teal is one shade lighter than the night around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The steep rear rock face rises behind them at the left. At the right, a few arm-lengths behind Khev, the seaward front edge of the ledge is darkened by the sea, and a line of white foam lies along it.

The scene is lit only by the cold indigo-teal night and a thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Video
```text
0-4 s: Khev tightens the cradle a little, his forearms pressing closer under Oru; Oru's three amber lights glow once from left to right in order, evenly. 4-7 s: Khev shifts his weight onto his right side while his left leg stays unloaded, and the crack on his left shin plate stays at the lower edge of the frame. 7-10 s: the line of foam along the front edge of the ledge advances a hand's breadth closer; Khev turns his head toward the foam, Oru in his arms. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   Oru BAŞTAN kucakta (taşa değmiyor), kollar Oru'nun bütün gövdesinin altında, parmak kavraması yok, eller Oru'nun ardında, yüzgeçlere dokunmuyor · sağ yüzgeç açık, sol yüzgeç yarım açık ve sarkık, tek V çentik sol yüzgeçte, üç ışık eşit parlaklıkta TEK sıra, kameraya dönük; renk ayrımı teal Oru / indigo deri / fildişi plaka ·
             sol kaval plakasında TEK çapraz çatlak kadrajın alt kenarında; sol bacak kameraya doğru uzanmış, sağ bacak altında · dik duvar sol arkada, ledge ön kenarı koyu, köpük çizgisi sağ arkada · gaz devi kadrajda değil · yazı yok · 16:9 piksel
YEDEK        (T01) kollar Oru'ya kaynaşırsa ya da Oru taşta yatıyorsa tek düzeltme: "Edit the supplied frame. Change only Oru's position: it rests fully in the cradle of Khev's forearms, clear of the stone, and his hands are hidden beneath and behind it. Keep Khev's pose, the cracked left shin plate, the ledge, the foam, the light and the camera angle exactly as they are." Video yalnız beşiğin sıkılaşması + köpüğe bakış (bilgi "taştan kucağa" C14→C15 kesmesinde kalır).
             Köpük çoğalırsa ya da ıslak/akıntı okunursa: Video (yedek; sonunda ORTAK GÖRÜNÜM birebir): "0-4 s: Khev tightens the cradle a little, his forearms pressing closer under Oru; Oru's three amber lights glow once from left to right in order, evenly. 4-10 s: Khev shifts his weight onto his right side while his left leg stays unloaded, then turns his head toward the right of the frame, Oru in his arms. The camera stays locked throughout."
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

## C16 — Çıkış yok, yardım yanlış yere bakıyor

```
FLOW      Frames to Video
ARAÇ      kare: GPT Image iki geçişte (geçiş 1 ref ile, geçiş 2 düzenleme) · video: Gemini Omni 1.1 Flash (yalnız kare/C16.png)
EKLE      başlangıç karesi: kare/C16.png · referans (yükleme sırası): ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png
GEÇİŞ 2   düzenleme: kare/ara/C16_g1.png üstüne · referans: ref/3.ANNE_v1.png (yalnız bu düzenlemede; Omni'ye gitmez) · çıktı kare/C16.png
```

### Görsel
```text
Reference 1 (Khev): take his proportions, pale ivory chitin plates and deep-indigo skin from it, using the crouching-pose panel and the cracked left-shin panel. Reference 2 (Oru): take its deep-teal form, crescent forehead crest and three amber lights from it, using the panel with the right fin spread open and the left fin half open and drooping, and the face close-up panel. Reference 4 (shore): take the lower ledge with its steep rear face, the terrace edge, the arch, the broken causeway end, the dark sea and the ringed gas giant from it, using the low side-view panel of the lower ledge with the terrace edge, the arch and the broken causeway end above, and the wide master panel.

A wide night shot from the side, parallel to the shoreline, the camera low at ledge level, wide-angle 28 mm lens, deep focus. At the left, one flat near-vertical black-basalt wall fills the left half of the frame from the ledge up to the top edge, its face smooth, without handholds or steps. Along the top of the wall runs the edge of the empty terrace. A tall ancient black-basalt arch with smooth parallel vertical grooves and no symbols stands at the left side of the terrace. Beneath the arch the ground is dark and closed, backed by a dark stone inner wall, and a clear shadow line on the floor marks where the shade ends and the open sky light begins. The black basalt terrace extends to the right into a narrow causeway that points out over the dark sea. The causeway ends in a fresh broken edge above the right side of the wall.

At the bottom centre, on the ledge, Khev kneels with both digitigrade legs folded under him, about one sixth of the frame height tall, in three-quarter view with his left side toward the camera, his chest turned toward the wall and his face turned down toward Oru. Khev is a lean biped with two arms and two digitigrade legs with raised heels, his bare torso and limbs made of pale ivory chitin plates joined by flexible deep-indigo skin. Khev's left shin plate carries one diagonal crack with a faint amber glow inside it, the only crack on him. The cracked leg is the one nearer the camera. Oru is carried at chest height in the cradle of his forearms, his hands hidden beneath it. Oru rests in the cradle with its head raised and its belly turned toward its carrier's chest. Oru is a juvenile celestial manta shorter than Khev's forearm, with a compact deep-teal frame, two broad translucent pectoral fins and one gently tapering tail. Oru's blunt rounded head has one shallow crescent forehead crest, two glossy black eyes on its sides, and three amber oval lights in a row beneath its left eye, the only amber lights on it. Oru's right fin is spread open while its left fin hangs half open and drooping at a fixed angle. Oru's three lights glow faintly and evenly, and its teal is one shade lighter than the night around it.

The lower ledge is one broad dry shelf of rock, open to the sea on its right, with a near-vertical rear rock face rising behind it. The dry ledge lies just above the waterline. Dark sea fills the right of the frame, and one single broad dark ridge of water advances across it toward the ledge, much closer than the horizon, with spray lifting from its crest. The horizon passes at about one third of the frame height from the bottom, and a low bank of cloud lies on it at the far right.

A ringed gas giant hangs high at the upper right of the star-filled night sky above the dark sea, with thin violet cloud banks along the horizon. The scene is lit only by the cold indigo-teal night and the gas giant's thin pale rim light from the upper right, with warm colour coming only from amber bioluminescence. The pale rim light reaches the foot of the wall and picks it out from the shadow.

Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

### Görsel geçiş 2 (düzenleme)
```text
Reference 3 (mother manta): take her pitted silver-grey head and her amber eye from it, using the distant-view panel with only a tiny head and eye above a thin horizon line.
Edit the supplied frame. Change only the far right of the horizon: add the mother manta's small distant head rising just above the low bank of cloud, her face turned toward the shore at the left and her left side toward the camera, her amber eye looking level across the sea, tiny and without fine detail, with the rest of her hidden behind the cloud. The mother manta is the full-grown adult of Oru, with a blunt head armoured in pitted silver-grey plates that look like cratered moon stone and one shallow crescent forehead crest. She has one enormous amber eye on the left side of her head, with a glossy dark pupil under a thick organic eyelid. Three amber oval lights sit side by side in a row beneath her eye, the only lights on her head. At this distance the lights are too small to count and read only as dim. Keep Khev, Oru, the wall, the arch, the ledge, the sea, the ridge of water, the sky, the light and the camera angle exactly as they are.
```

### Video
```text
0-3 s: Khev lifts his head from Oru and turns it up along the face of the wall to its top edge, his torso and forearms staying in place; the broad ridge of water advances toward the ledge and spray passes the right edge of the frame. 3-6.5 s: Khev keeps his gaze on the empty top of the wall; the distant head of the mother manta turns slowly, her eye moving up and to the left until it rests on the same empty top of the wall. 6.5-10 s: Khev turns his head to the right and looks at the distant head, while the mother manta keeps her gaze on the top of the wall; the ridge of water comes a little closer and the dry ledge narrows. The camera stays locked throughout. Photoreal live-action science-fantasy cinema, widescreen 16:9, restrained anamorphic lens character, fine 35mm grain, readable shadow detail, immense physical scale, tactile organic surfaces, plain unmarked surfaces.
```

```
KARE KABUL   geçiş 1: düz dik duvar kadrajın sol yarısını dolduruyor, yüzünde tutamak/basamak yok; tepede boş teras kenarı + kemer (altı koyu, ardı iç duvar) + geçidin kopuk ucu; Khev diz çökmüş, alt-ortada, sol yanı (çatlaklı sol kaval, TEK çatlak) kameraya yakın; Oru göğüs hizasında kucakta, sağ yüzgeç açık sol yarım açık sarkık, üç ışık tek sıra ·
             sağda TEK geniş sırt çıkıntıya belirgin yakın, kuru çıkıntı su çizgisinin hemen üstünde; ufuk kadraj üçte birinde, uzak sağda alçak bulut yığını; gaz devi sağ üstte, tek · yazı yok ·
             geçiş 2: ufkun sağ ucunda TEK küçük ayrıntısız baş, yüzü kıyıya, bakışı yatay; ışıklar sayı taşımaz (yalnız sönük okunur); Khev, Oru, duvar, sırt geçiş 1 ile aynı · ikinci baş/ikinci Oru yok · 16:9 piksel
YEDEK        (FILM yedek) model gövdeyi döndürürse ya da iki baş dönüşü tutmazsa: Khev baştan duvarın tepesine bakar — kare tek düzeltmeyle "Edit the supplied frame. Change only Khev's head: it is now raised and turned up along the face of the wall toward its top edge. Keep Khev's pose, Oru, the wall, the arch, the ledge, the sea, the ridge of water, the distant head, the light and the camera angle exactly as they are."
             Video (yedek kare; sonunda ORTAK GÖRÜNÜM birebir): "0-3 s: the broad ridge of water advances toward the ledge and spray passes the right edge of the frame, while Khev keeps his gaze on the empty top of the wall. 3-6.5 s: the distant head of the mother manta turns slowly, her eye moving up and to the left until it rests on the same empty top of the wall. 6.5-10 s: Khev turns his head to the right and looks at the distant head, while the mother manta keeps her gaze on the top of the wall; the ridge of water comes a little closer and the dry ledge narrows. The camera stays locked throughout."
             Dev mantanın baş dönüşü tutmazsa: baş sabit, yalnız göz bebeği yönü boş terasa — yukarıdaki yedek Video'nun 3-6.5 s vuruşunda "the distant head of the mother manta turns slowly" yerine "the mother manta's eye moves up and to the left" yazılır. Geçiş 2 yüzleri bozarsa/baş ikilenirse: geçiş 2 atılır, Oru'nun metinle "small teal manta" olması yedeği FILM'de; bilgi "ufukta yardım" düşer, "çıkış yok" duvar kadrajından okunur.
d2           aynı prompt (varyans); d1 kusuru tek ise yalnız o düzeltilir. İki deneme aynı sebeple bozuksa üçüncüsü aynı promptla gönderilmez.
```

---

## FLOW İŞ EMRİ

> **Araç (Flow değil):** kareler **GPT Image**'da (ChatGPT Images 2.5 ya da API `gpt-image-2.5-sunburst`), video **Gemini Omni 1.1 Flash** (Gemini uygulaması). `FLOW_GERCEKLERI` Ek 2-3.
> Flow ayarları (Return silent videos, watermark) bu yolda yok; Omni klibin yerel sesi üretilir → **indirildikten sonra kurguda atılır** (model sesi KAPALI, `timeline.json` klip_sesi kapalı). Videoda ses isteği yazılmadı.
> Her kare **yeni sohbette**, onaylı çapa referansları yeniden eklenerek üretilir; önceki karenin çıktısı yeni kareye girdi yapılmaz (KIMLIK §3) — **tek istisna iki geçişli karelerin geçiş 2'si** (düzenleme, geçiş 1 çıktısı girdidir). Çıktı PNG, piksel oranı **16:9** ölçülür (1536×864 · 2048×1152 · 2560×1440);
> 3:2 çıkarsa merkezden 16:9 kırpılır, esnetme/genişletme yok (GPT_IMAGE_OMNI §13). Her denemede `NOTLAR.md` DENEMELER'e: model adı · eklenen numaralar (`ref 1,2,4`; geçiş 2'de `ref 3`) · giriş/çıkış saniyesi (`medya.py al MOONMOTHER --yaz`).
> Omni'ye yalnız `kare/Cxx.png` yüklenir; panel sayfası ve `kare/ara/` dosyaları yüklenmez. Aynı yapısal hata iki kontrollü düzeltmede kalırsa çekim yeniden tasarlanır (AGENTS §4).
> **Tablo sırası üretim önceliğidir** (FILM §4 pilot risk sırası, G02 içinde): C09 (ÖLÜMCÜL düzeltmesi; iki geçiş yöntemini ilk sınar) → C11 → C15 → C13 → C16 (iki geçiş) → C14 → C10 → C12. Dosya adları çekim numarasını korur. Önkoşul: `ref/1…4` onaylı (G01'in iş emrinde).
> **Bu grubun sınadığı soru (pilot ölçülmedi):** iki geçiş yönteminde ref 3 düzenlemesi Khev ve Oru'nun yüzünü/elini bozmadan ufka tek küçük baş ekliyor mu (C09 → C11 → C16).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C09 kare (geçiş 1) | `kare/ara/C09_g1.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 2 | C09 kare (geçiş 2) | `kare/C09.png` | Görsel (GPT Image, düzenleme) | kare/ara/C09_g1.png · ref/3.ANNE_v1.png (yalnız uzak-baş paneli) | 2 | ölçülecek |
| 3 | C09 | `ham/C09_d1.mp4` | Frames to Video (Gemini Omni) | kare/C09.png | 2 | ölçülecek |
| 4 | C11 kare (geçiş 1) | `kare/ara/C11_g1.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 5 | C11 kare (geçiş 2) | `kare/C11.png` | Görsel (GPT Image, düzenleme) | kare/ara/C11_g1.png · ref/3.ANNE_v1.png (yalnız uzak-baş paneli) | 2 | ölçülecek |
| 6 | C11 | `ham/C11_d1.mp4` | Frames to Video (Gemini Omni) | kare/C11.png | 2 | ölçülecek |
| 7 | C15 kare | `kare/C15.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png (bu sırayla) | 2 | ölçülecek |
| 8 | C15 | `ham/C15_d1.mp4` | Frames to Video (Gemini Omni) | kare/C15.png | 2 | ölçülecek |
| 9 | C13 kare | `kare/C13.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 10 | C13 | `ham/C13_d1.mp4` | Frames to Video (Gemini Omni) | kare/C13.png | 2 | ölçülecek |
| 11 | C16 kare (geçiş 1) | `kare/ara/C16_g1.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 12 | C16 kare (geçiş 2) | `kare/C16.png` | Görsel (GPT Image, düzenleme) | kare/ara/C16_g1.png · ref/3.ANNE_v1.png (yalnız uzak-baş paneli) | 2 | ölçülecek |
| 13 | C16 | `ham/C16_d1.mp4` | Frames to Video (Gemini Omni) | kare/C16.png | 2 | ölçülecek |
| 14 | C14 kare | `kare/C14.png` | Görsel (GPT Image) | ref/1.KHEV_v1.png · ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 15 | C14 | `ham/C14_d1.mp4` | Frames to Video (Gemini Omni) | kare/C14.png | 2 | ölçülecek |
| 16 | C10 kare | `kare/C10.png` | Görsel (GPT Image) | ref/4.KIYI_v1.png | 2 | ölçülecek |
| 17 | C10 | `ham/C10_d1.mp4` | Frames to Video (Gemini Omni) | kare/C10.png | 2 | ölçülecek |
| 18 | C12 kare | `kare/C12.png` | Görsel (GPT Image) | ref/2.ORU_v1.png · ref/4.KIYI_v1.png (bu sırayla) | 2 | ölçülecek |
| 19 | C12 | `ham/C12_d1.mp4` | Frames to Video (Gemini Omni) | kare/C12.png | 2 | ölçülecek |

Toplam: 11 görsel çıktı (8 kare + 3 geçiş-1 ara kare) × 2 deneme + 8 video × 2 deneme = en çok 38 üretim. İkinci denemeler: `ham/C09_d2.mp4` … `ham/C16_d2.mp4`.

---

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · `.claude/agents/goruntu-yonetmeni.md` § Bitirmeden önce)

> Elle tarama (bu ajanda kabuk yok, `film_dogrula.py` koşulmadı; Fable koşar). Kimlik cümlesi sayımı ve DERS taraması Grep ile yapıldı (kod blokları çok satırlı desenle ayrıca tarandı): Y1 (ISARET kelimesi yok) · Y2 (ekli her referansın en az bir cümlesi birebir) ·
> Y5 (`smoke/steam/mist/fog/vapor/plume/exhaust/drip/splash/bubble/wet/rain/flame/droplet/soot` Görsel ve Video'da yok; `spray`/`foam`/`cloud`/`ridge`/`sea` listede yok, atmosferli dünya) · Y8 (ekran/gösterge/`status`/`screen` yok) ·
> Y10 (`slow` her videoda en çok 1: yalnız C16 `slowly`) · Y13 (Video'da `sound/audio/ambient/hum/echo/noise/music` yok). `body` · `wound` · `injured` · büyük harfli KHEV/ORU, referans/çekim kodu ve `Clip n of N` kod bloklarında (YEDEK düzeltme cümleleri dahil) yok.
> Uzunluk: her `### Görsel` ve `### Video` bloğu 4.000 karakterin altında (eşik taraması aşağıda). Geçiş 2 blokları film_dogrula'nın görmediği başlığı taşır (`### Görsel geçiş 2`): ≤1.800 karakter, elle sınırlandı.

| Çekim | Düzeltilen sorular (1-8) | Bilerek bırakılan + gerekçe |
|:--:|---|---|
| C09 | **1** (sol kaval: sayı `one` + taraf `left` + konum `shin plate`; Oru ışıkları `the only amber lights on it`; dev manta ışıkları `the only lights on her head`) · **2** (Khev yüz + gövde ve uzuvlar + sol kaval birebir; Oru gövde · yüz · kucak duruşu birebir; dev manta baş zırhı · göz · üç ışık geçiş 2'de birebir; kemer · kemer ağzı · teras ve geçit birebir) · **4** (kemer ağzının ardı `dark stone inner wall`; Khev'in önü deniz, ardı kemer; ufuk başının ardı bulut yığını) · **7** (Reference 1 yalnız sağ yan tam boy + ¾ yüz + sağlam kaval, el paneli yok: eller Oru'nun ardında; Reference 2 kucak + yüz yakın; Reference 4 kemer-ağzı + master; geçiş 2'de Reference 3 yalnız uzak-baş paneli) · **8** (planın `Sound:` satırı atıldı; Video'da ses yok; `slow` yok; zıt istek yok: Oru'nun başı kameradan ufka döner, ışıklar son vuruşta bir kez atar) | **3** ortak cümle temiz · **5** akışkan yok (`ridge`, `cloud`) · **6** ekran yok · Oru çentiği yazılmadı (yüzgeçler yarım kapalı, bilgi taşımıyor; C04 · C08 ile aynı) · dev manta adı videoda yok (`the distant head`): gövde çağrılmaz |
| C10 | **2** (kimlik taşıyan canlı yok; mekân: teras ve geçit birebir + geçit ekseni açıklaması, gök ve ışık birebir) · **3** (ışık cümlesi gaz devi ile: gaz devi üst yarıda; ORTAK temiz) · **4** (kadrajın ardı: ötesi açık deniz, terasın kamera ardında kaldığı yazıldı) · **5** (`ridge`, `spray`, `water bursts up beneath it` meşru: atmosferli dünya; `splash`/`wet`/`dust` yok; toz bulutu yazılmadı, levha `drops`) · **7** (Reference 4 yalnız geçit-ucu çatlak+ayrık levha paneli + master; kırık-uç paneli anılmadı: zıt durum) · **8** (planın `Sound:` satırı — taş gıcırtısı, çatlama, su çarpması — atıldı; Video'da `creak/snap/roar` yok; `slow` yok) | **1** işaret yok (canlı yok) · **6** ekran yok · kimlik cümlesi yok (insansız): kişi zamiri yazılmadı (A08) · terasın "to the right" cümlesi kamera ekseni açıklamasıyla birlikte (kimlik birebir korundu) |
| C11 | **1** (Oru çentiği `one small … V-shaped notch … left fin … trailing edge … the only notch on either fin`; ışıklar `the only amber lights on it`; her elde `four thick digits`) · **2** (Khev yüz + gövde + sol kaval + eller birebir; Oru gövde · yüz · çentik · ton birebir; kucak duruşu cümlesi YAZILMADI: Oru kolların üstünde yatay süzülüyor, `both fins half closed` açık yüzgeçle çelişirdi; çıkıntı · çıkıntı yüksekliği birebir) · **4** (Khev'in arkası: geçit teras ve kıyıya geri gidiyor; önü: kırık uç + boşluk; çıkıntı dik arka duvarlı, ardı yazılı) · **5** (`the sea breaks … the shelf stays dry`) · **7** (Reference 2 üstten + yüz yakın + sol yüzgeç arka kenarı; Reference 1 sağ yan + ¾ yüz + önkol-el + sağlam kaval; Reference 4 kırık-uç + alçak-yan çıkıntı + master) · **8** (planın `Sound:` satırı atıldı; Video'da ses/çağrı yok; `slow` yok; zıt istek yok: eller baştan boş ve açık, Oru'dan geçmiyor) | **3** ortak cümle temiz · **6** ekran yok · **Oru'nun sol yüzgeci uzak yanda:** kamera Khev'in sağında ve Oru ufka bakıyor → sağ yüzgeç yakın; kamera 15° yukarıdan olduğu için sol yüzgeç (V çentik) törpülenmeden okunur, 3 ışık için baş kameraya çevrildi (C20 pilot deseni). Taraf ölçülmedi, F7 kare kabulünde bakılır · dev manta adı videoda yok |
| C12 | **1** (çentik: sayı + taraf + konum + `the only notch`; ışıklar `the only amber lights on it`) · **2** (Oru gövde · yüz · çentik birebir; yatık durum cümlesi (sayfa ⑥ ile aynı) KİMLİK ÖNERİSİ olarak yazıldı; çıkıntı birebir) · **3** (gaz devi kadrajda değil → No 4 "kadraj dışı" ışık satırı; gök cümlesi yok) · **4** (çıkıntının ardı: dik bazalt yüz; sağ: denize açık, dış kenar ve ötesi koyu su) · **5** (`dry` olumlu, sprey yalnız sağ kenar `thin line of sea spray`; `wet`/`drip`/`splash` yok; mavi karın ışığı yok) · **7** (Reference 2 yatık panel + yüz yakın + sol yüzgeç arka kenarı; Reference 4 yalnız çıkıntı yan panel) · **8** (planın `Sound:` satırı — kırılgan çağrı, membran, sörf — atıldı; Video'da ses/çağrı yok; `breath` görsel hareket; `slow` yok) | **6** ekran yok · sol yüzgeç kameradan uzak yanda ve yukarı eğik, sırtın üstünde okunur (sert, açılamayan) · Khev anılmadı (kadrajda yok) |
| C13 | **1** (sol kaval: sayı + taraf + konum; Oru yatık cümlesi ışıkları `weakly` taşır) · **2** (Khev arkadan baş-omuz + gövde + sol kaval birebir; Oru gövde + yatık durum; kemer · kemer ağzı · teras ve geçit · çıkıntı · çıkıntı yüksekliği birebir) · **4** (kemerin ardı iç duvar; Khev'in önü çıkıntı ve deniz, arkası kemer ve kara; kopuk uç `fresh broken edge` olumlu) · **5** (`ridge`, `sea` meşru) · **7** (Reference 1 arka + çömelme + sağlam kaval; Reference 2 yalnız yatık panel; Reference 4 kırık-uç + alçak-yan + master, sağlam-uç paneli anılmadı) · **8** (planın `Sound:` satırı — nefes tıkı, sıyrılma, rüzgâr — atıldı; Video'da ses yok; `slow` yok; zıt istek yok: atlayış `quickly`, süzülme yok) | **3** ortak cümle temiz · **6** ekran yok · **eller görünmez** (dizler arasında, kadraj dışı; FILM "dizlerinin önünde" ile uyumlu, T01) · Khev'in yüzü kadrajda okunmaz (arkadan ¾); bakış yönü baş dönüşüyle, kemer solda · FILM "terasın deniz kenarı"nı geçidin kırık ucuyla bağladım (sebep: C10'dan sonra çıkıntı tek aşağı yol) · atlayış 7.5-10 s içinde (≈8 s), son ≈1.2 s boş kenar |
| C14 | **1** (çatlak: sayı `one` + taraf `left` + konum `shin plate` + `the only crack on him`; her elde dört parmak; Oru ışıkları `the only amber lights on it`) · **2** (Khev yüz + gövde + ÇATLAKLI sol kaval + eller birebir; sağlam sol kaval cümlesi YOK; Oru gövde · yüz birebir + yatık durum; çıkıntı birebir) · **3** (gaz devi kadrajda değil → No 4 "kadraj dışı" ışık) · **4** (dik duvar arkada ve solda; sağ: denize açık dış kenar) · **7** (Reference 1 ¾ yüz + çömelme + ÇATLAK panel, sağlam panel anılmadı — TD B1; Reference 2 yatık panel + yüz yakın; Reference 4 yalnız çıkıntı yan panel) · **8** (planın `Sound:` satırı — iniş yankısı, kitin gıcırtısı, tıklama çığlığı — atıldı; Video'da ses yok; `wound`/`injured`/`body` yok; `slow` yok; zıt istek yok: çatlak videoda `stays exactly as it is`) | **5** akışkan yok (`spray` meşru, ince çizgi) · **6** ekran yok · sağ el yazılı olarak görünmez (dizin ardında) ve sol el taşa yaslı tam kadrajda: zemine gömülme riski T01, YEDEK'te yok (kare kabulünde parmak taşa dayalı aranır) |
| C15 | **1** (çatlak: sayı + taraf + konum + `the only crack on him`; çentik + ışıklar `the only …`) · **2** (Khev yüz + gövde + çatlaklı sol kaval birebir; Oru gövde · yüz · çentik · yüzgeç durumu `right fin spread open … left fin half open and drooping` birebir; kucak: KİMLİK ÖNERİSİ satırı (yüzgeç ifadesiz); çıkıntı birebir) · **3** (No 4 "kadraj dışı" ışık) · **4** (dik duvar solda arkada; sağ arkada çıkıntı ön kenarı ve köpük çizgisi, ardı açık deniz — Khev'in arkası yazılı) · **5** (`wet` yok → `darkened by the sea`; köpük `a line of white foam`, çoğalmıyor; `foam advances a hand's breadth`) · **7** (Reference 2 yalnız ⑦ durum paneli + yüz yakın, ⑧ kucak duruşu paneli anılmadı: yüzgeç durumu zıt; `ref/4` EKLE'de yok, mekân metinle) · **8** (planın `Sound:` satırı — nefes, ıslık — atıldı; Video'da ses yok; `gently lifts` videoda YOK: kaldırış kesmeye (FILM T01); `slow` yok; zıt istek yok) | **6** ekran yok · eller Oru'nun altında ve ardında (kapalı), yüzgeçlere dokunma yok · Oru'nun sağ yüzgeci kameraya yakın (Khev sola dönük), sol yüzgeç sarkık ve uzak yanda; baş kameraya çevrildi · FILM'deki "ıslak ön kenar" kelimesi yazılmadı |
| C16 | **1** (çatlak: sayı + taraf + konum + `the only crack on him`; ışıklar `the only …`) · **2** (Khev gövde + çatlaklı sol kaval birebir; Oru gövde · yüz · yüzgeç durumu + kucak (öneri) birebir; kemer · kemer ağzı · teras ve geçit · çıkıntı birebir; dev manta baş zırhı · göz · üç ışık geçiş 2'de birebir) · **3** (ORTAK temiz; ışık cümlesi gaz devi ile, gaz devi sağ üstte) · **4** (kemer ağzının ardı iç duvar; duvarın tepesindeki teras "empty"; Khev'in önü duvar, arkası denize açık yan; kopuk uç `fresh broken edge`) · **5** (`ridge`, `spray`, `sea` meşru; `wave` yazılmadı, tek sırt) · **7** (Reference 1 çömelme + çatlak paneli; Reference 2 ⑦ durum + yüz yakın; Reference 4 alçak yan çıkıntı paneli (duvar+kemer+kopuk uç) + master; geçiş 2'de Reference 3 yalnız uzak-baş paneli) · **8** (planın `Sound:` satırı — kitin tıkı, rüzgâr, sörf kükremesi — atıldı; Video'da ses yok; `slow` 1 (`slowly`); zıt istek yok: Khev'in gövdesi yerinde, yalnız baş dönüşleri; son vuruş donmuyor) | **6** ekran yok · yardım yanlış yere bakıyor bilgisi iki baş dönüşüyle okunur; Khev'in diz çökmüş ve gövdesi yerinde (FILM sahip kararı 17.10) · uzak başın ışıkları sayı taşımaz (`too small to count and read only as dim`) · duvarın tepesindeki terasın üst yüzeyi alçak kameradan görünmez: "boş teras" teras kenarı + kemer olarak kurulu, bakış hedefi tepedir |

**Uzunluk ve kelime taraması (Grep, bu dosya, yazımdan sonra):** `### Görsel`/`### Video` blokları için eşik deseni ```` ```text\n[^`]{4000,}``` ```` eşleşme vermedi (hiçbir blok 4.000 karakteri aşmıyor; 3.300-4.000 aralığında 4 blok); sıvı/ses/ekran/`body·wound·injured·dead` kelime taraması blok içinde 0 (yalnız başlık notlarında ve bu tabloda alıntı olarak geçer).

---

## FABLE'A NOTLAR (G02)

1. **FILM §3'e eklenecek iki kimlik satırı** (yukarıdaki `## KİMLİK CÜMLELERİ` tablosu): yatık durum (C12 C13 C14) ve açık yüzgeçli kucak duruşu (C15 C16). Ayrıca No 4 "ışık — gaz devi kadraj dışı" satırının kullanım listesini `C02 C05 C12 C14 C15` yap. C17-C23'te (G03) kucak/yüzgeç durumu için aynı çelişki geçerli: kucak cümlesi yüzgeçleri `half closed` der, durum cümlesi `right fin open / left half open` der.
2. **İki geçişli kare dosya düzeni:** geçiş 1 çıktısı `kare/ara/Cxx_g1.png`, geçiş 2 çıktısı `kare/Cxx.png`. `EKLE` satırında yalnız 1·2·4 (film_dogrula referans anahtarı kontrolü geçiş 1 bloğuyla eşleşir); ref/3 `GEÇİŞ 2` satırında ve iş emrinde. `### Görsel geçiş 2 (düzenleme)` başlığı film_dogrula'nın `### Görsel\n` kalıbına uymaz, görmez; bloğu el ile taradım (ORTAK GÖRÜNÜM düzenleme bloklarında yok, G01 YEDEK düzenlemeleriyle aynı).
3. **C11 Oru taraf geometrisi (kapsam dışı risk):** kamera Khev'in sağında olduğundan ufka bakan Oru'nun sağ yüzgeci yakın yandır; sol (yaralı) yüzgeç uzak yanda. Kamera 15° yukarıdan ve baş kameraya dönük kuruldu; sol yüzgecin gevşemesi okunmazsa YEDEK (Oru sıyrılıp çıkar) devrede, ya da kamerayı Khev'in önünden ¾ yapmak plan sapması olur (F3 kararı gerekir).
4. **C13:** FILM "terasın deniz kenarında" + "geçidin deniz ucu kopuk" iki yeri birleştirdim (Khev geçidin yeni kırık ucunda çömeliyor); eller görünmez. Karşı görüş çıkarsa C13 kare kabulü ve KIYI ⑤ paneli aynı kalır.
5. **FILM §4 C16:** 17.10.2026 sahip kararı satırı uygulandı (diz çökmüş, yalnız iki baş dönüşü). Eski kalkma/çökme yok.
