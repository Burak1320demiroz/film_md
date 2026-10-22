# 🖼️ RAIN_THIEF — Prompt grubu G02 (çekimler C09–C16 · M2 çatılar + C14 M1) · tur 1

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Kaynak: `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md` (sahip planı; "plandan asla dışarı çıkma") + FILM.md §3 (ORTAK GÖRÜNÜM · ORTAK HAREKET · SAHNE DÜZENİ · DÜNYA KURALLARI · DEVAMLILIK · KİMLİK CÜMLELERİ) + §4 çekim satırı + §5 replik saniyeleri + `ODA/F5_yazim_karari.md` + örnek grup `PROMPTLAR/G01.md`.
> **Görsel düzeni:** referans anahtarları (plan Referanslar listesi, yükleme sırasıyla) → ORTAK GÖRÜNÜM (FILM §3, birebir) → planın Görsel istemi **karakteri karakterine aynen** → boş satır → ek paragraf (yalnız plan cümlesinden SONRA gelen ayrı cümleler: plan Kamera satırının İngilizcesi · kadrajdaki öznelerin KİMLİK CÜMLELERİ birebir · plan R06/R07 mekân cümleleri · plan Devamlılık satırı ve §8 durumu, hareketin BAŞINDAKİ hâliyle).
> **Video düzeni:** ORTAK HAREKET (FILM §3, birebir) → planın video istemi aynı cümleler, aynı sırada, yalnız `a-b s:` vuruş önekiyle 2-4 vuruşa bölünmüş → son vuruşta plan Devamlılık satırının İngilizcesi (bitmiş hâl burada) → replikli çekimde plan "Dialogue performance" bloğu aynen. Prompt gövdesine çekim kodu, referans kodu, başlık satırı, "Clip n of N" yazılmadı.
> **Repliksiz çekimler (C09 C11 C13 C15 C16):** ORTAK HAREKET'ten "The spoken lines below are performance cues; final clean dialogue can be recorded separately." cümlesi atıldı, Dialogue bloğu yazılmadı (yazım kararı Video 1, M). **Replikli (C10 C12 C14):** ORTAK HAREKET tam, Dialogue bloğu plandan aynen.
> **Model sesi:** FILM §6'ya göre kullanılmaz (plan §7 "modelin ses ürettiği varsayılmaz"); replikler "ağız kadrajda — temiz replik ayrı kayıt" ya da kadraj dışı (C12 R12), videoda oyunculuk ve ağız ipucudur, kurguda ayrı kayıt gelir. Planın "Kurgu sesi" satırları FILM §6'dadır, prompta yazılmadı.
> **Biçim düzeltmesi (M):** bu grupta **yok**. Plan cümleleri aynen; Mara kimliği FILM §3 tablosundaki "one narrow vertical mouth" biçimiyle yazıldı (plan C14 Görsel'inde "speaking" kelimesi yok).
> **Plan cümlesi aynen kaldı, Fable kararı bekleyen noktalar (8 SORU'da da var):** (1) C11 Video "Let the engine fade without dialogue." ve C16 Video "His weight produces heavy metallic footsteps." ses kelimesi taşıyor (DERS Y13, model sesi kapalı film) → alternatif: "Let the skiff fade into the distance." / "His weight shows in each heavy step." · (2) C14 Görsel "the same brass awning lever previously shown" yumuşak çekim atfı (film_dogrula ATIF regex'i yakalamıyor) → alternatif: "the same brass awning lever." · (3) **plan içi çelişki, C12:** Video sonu "a short rust-orange canopy beside Kett", plan Devamlılık satırı "alternatif mavi tente rotası görünür" → ikisi de yazıldı (Devamlılık satırı çevirisi aynen); ayrıca C12 R07 pas turuncusu tente + mavi yük tentesi satırları Görsel ekinde; karar: tek tente yeterliyse sahibe sorulur.
> **KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6** — FILM §3 ORTAK GÖRÜNÜM "warm late-afternoon … palette" (ışık) ve "one pale ringed planet" (gezegen) taşıyor. Plan §6 birebir olduğu için dokunulmadı. Öneri G01'deki ile aynı (uygulanmadı): `Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm copper and mustard palette with cobalt-blue accents, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character.` Sıkı kadrajlarda (C10 cam, C11 orta yakın, C14 sıkı orta) gezegen kadraja basılabilir: ilk kare denemesinde bakılır.

---

## C09 — Pazarın üstü

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png
```

> Not: Plan metni aynen. Repliksiz. Kett tek eliyle tırmanır (sol el + ayaklar), çekirdek sağ elde göğse yakın: el-nesne riski T01 (çekirdek sağ elde sabit, tek nesne). Ref 7 sayfasında sabit basamak ve kalabalık yoktur: basamaklar ve kalabalık plan metniyle tarif edildi. Kamera satırındaki "köprü" planın kelimesi (çatı köprüsü); mavi yük tentesi bu çekimde ayrıca tarif edilmedi.

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 7 (roofs): take the copper roofs, the thick blue pipes and the copper weather tower from it. Reference 9 (weather core): take the transparent cylinder, the three silver ribs, the dark base and the side test valve from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Wide side view of Kett climbing fixed metal service rungs attached to a thick blue pipe, rising from the alien market toward six-meter-high copper roofs. One transparent storm core stays cradled in the right hand near the chest; Kett grips with the left hand and uses visible toe pads. Mustard poncho fastened. Crowds of different alien silhouettes below. Copper weather tower at screen right, pale ringed planet above.

The camera is a wide side view, with the alien crowd below and the bridge and the reservoir above. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett cradles the core in the right hand near the chest. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. A bustling entirely alien open-air market stands on a dusty copper-built moon city. Eight different nonhuman crowd silhouettes stand in layered depth. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. One pale planet with a thin gold ring hangs in the warm late-afternoon sky. The poncho is fastened, the core is in the right hand and all surfaces are dry.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-4 s: Track gently upward as Kett climbs a short section of the fixed service ladder using the left hand and feet. 4-7 s: Keep the right hand and weather core against the chest. Do not make Kett jump or change grip rapidly. 7-10 s: One continuous climb, consistent downward gravity and dry surfaces. Kett reaches the six-meter roof level; the core stays in the right hand.
```

## C10 — Yağmur zaten var

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/7.CATILAR_v1.png
```

> Not: Plan metni aynen. Replik R10 Kett 1,0-5,5 s (ağız kadrajda, 4,5 s) → ilk vuruş 0-7 s'ye alındı ki replik bölünmesin. Cam duvar: ardı (özel bahçe, iki odak dışı siluet) ve Kett'in arkası (kuru çatı hattı) bu promptta yazılı. Yağmur yalnız camın arkasında (plan §8: özel sera içi yağışlı, çatı kuru).

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 7 (roofs): take the sealed glass luxury garden, the dry copper rooftop and the thick blue pipes from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Side-on medium composition outside a sealed luxury greenhouse on the copper rooftop route. Kett stands in the dry dusty exterior, mustard poncho and right-held storm core intact. Behind a single clear glass wall, lush alien plants receive steady private rain; two wealthy nonhuman silhouettes stand far inside, out of focus. The public roofs outside remain dry. Emotional contrast through one glass barrier, no readable signage.

The camera is a lateral medium view along the glass, with Kett outside and the private garden inside. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. A sealed glass luxury garden has rain strictly inside. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. Behind Kett the dry dusty copper rooftop route continues under the warm late-afternoon sky. The scene shows closed distribution, not a lack of rain; the poncho is fastened and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-7 s: Move slowly sideways along the glass with Kett. Kett looks through the window at the existing private rainfall and delivers the short line quietly. 7-10 s: Keep exterior dust dry and greenhouse rain strictly behind the glass. No glass break, no new room, no face morphing. The scene shows closed distribution, not a lack of rain.

Dialogue performance, in this exact order:
1. KETT: "So it can rain. Just on the right side of the glass." Voice: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak.
```

## C11 — Bedelin görünmesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/7.CATILAR_v1.png
```

> Not: Plan metni aynen. Repliksiz. Kare başlangıç anı: biniş pulu hâlâ kemerde, sol parmaklar pulda, cep açık; pulun cebe girişi ve geminin gidişi Video'da (son vuruş). Risk T01 el-nesne: sol el küçük pul, sağ el çekirdek (iki ayrı nesne, iki ayrı el). Plan "lifts away from its dock" ile R06 "dock holds" çelişmesin diye iskele satırı yazılmadı. Q8: Video son vuruş "Let the engine fade without dialogue." plan cümlesi aynen (başlık notuna bak).

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 7 (roofs): take the dry copper rooftop and the thick blue pipes from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Medium close shot of Kett on the same dry copper rooftop. Mustard poncho fastened, core held securely in the right hand. Left fingers rest on one small orange boarding token at the belt beside an open pocket. Far to screen left, the single orange commuter skiff lifts away from its dock. Kett is calm but visibly aware of the lost escape. No other ship is foregrounded.

The camera is close on Kett, with the departing orange skiff in the left background. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. Behind Kett the dry copper rooftop continues under the warm late-afternoon sky. The token is still at the belt, the poncho is fastened and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-3 s: The orange skiff slowly departs in the distant left background. 3-8 s: Kett watches it briefly, then uses the left hand to tuck the orange token into the belt pocket. Keep the right hand and weather core motionless against the torso. 8-10 s: Let the engine fade without dialogue. The boarding token goes into the pocket and is not used again; the ship leaves.
```

## C12 — Çatıda yüzleşme

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/4.VORR_v1.png · ref/7.CATILAR_v1.png
```

> Not: Plan metni aynen. İki replik: R11 Vorr 1,0-4,5 s (ağız kadrajda) ilk vuruş · R12 Kett 5,3-6,8 s (kadraj dışı) ikinci vuruş; Vorr tek keskin yüz, Kett arkadan kadraj kenarında (ağzı görünmez). Kett arkadan olduğundan boyun tokası görünmez: işaret cümlesi yazılmadı (giysi cümlesi tokayı taşır). Ref 1 sayfası önden/üç çeyrek; arkadan görünüm sayfadan değil plan metninden ("the back of small Kett's mustard poncho"). Plan çelişkisi: Video sonu "short rust-orange canopy beside Kett", plan Devamlılık "alternatif mavi tente rotası": ikisi de R07 satırlarıyla yazıldı (başlık notu 3). Temas yok ("no physical contact yet").

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's cobalt-blue body and mustard poncho from it. Reference 4 (Vorr): take Vorr's face, body, dark brown uniform and copper shoulder armor from it. Reference 7 (roofs): take the exterior iron service staircase, the short rust-orange canopy, the folded blue delivery canopy and the thick blue pipes from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Vorr stands at the top of a visible exterior iron service staircase, blocking a dry copper rooftop walkway. Foreground edge shows the back of small Kett's mustard poncho and the core in the right hand. Vorr's two empty hands are visible. Blue service pipes continue toward the weather tower on the right. Eye-level medium confrontation, with Vorr as the only sharp face.

The camera is a medium close view of Vorr, with Kett at the edge of the frame from behind. Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. Exactly two arms and two legs, five thick fingers per hand. Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Kett holds the core in the right hand. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. A continuous exterior iron service staircase provides a parallel route to the weather tower. The iron service stair stands behind Vorr and a short sloping reinforced rust-orange canopy lies beside Kett. A separate folded blue delivery canopy on visible rails and tension cables is able to bridge two nearby service landings. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. Vorr comes by the iron staircase, the alternative blue canopy route is visible, and Vorr is unarmed.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-5 s: Vorr steps once from the visible staircase onto the walkway and speaks the first assigned line. 5-8 s: Hold his face while Kett's brief reply is heard off-screen. 8-10 s: No weapon and no physical contact yet. End with both routes visible: a short rust-orange canopy beside Kett and the iron service stair behind Vorr. Vorr's catching up is explained by the staircase.

Dialogue performance, in this exact order:
1. VORR: "That rain is company property. Don't make this expensive." Voice: Deep restrained adult bass, slow authority, no monster growls.
2. KETT: "Little late for that." Voice: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak.
```

## C13 — İlk kaçış hamlesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C13.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png
```

> Not: Plan metni aynen. Repliksiz. Tek oturarak kayma, kısa düşüş (< 2 m), alt sahanlık kadrajda ve ulaşılabilir; atlama, takla, ikinci akrobasi yok (FILM §4 risk). Pas turuncusu tente ≠ C14-C15 mavi yük tentesi (SAHNE DÜZENİ): bu çekimde yalnız pas turuncusu satırı yazıldı. Kett'in arkası: çatı (açık uçurum yok, plan). Kare başlangıç anı: Kett henüz üst kenarda oturuyor; alt sahanlığa varış Video son vuruşta.

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 7 (roofs): take the short sloping rust-orange canopy, the lower service landing, the copper roof and the thick blue pipes from it. Reference 9 (weather core): take the transparent cylinder, the three silver ribs, the dark base and the side test valve from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Wide side composition of a short sloping reinforced rust-orange market canopy between a copper roof and a lower service landing less than two meters below. Kett starts seated at the top edge, core protected in the right hand against the torso, left hand braced on the canopy. Mustard poncho fastened. The landing is clearly visible and safely reachable. No guard in focus, no open abyss.

The camera is a fixed wide side view, with the short sloping canopy and the lower service landing. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand against the torso. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. A short sloping reinforced rust-orange canopy drops less than two meters to a lower service landing. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. The copper roof lies behind Kett. The poncho is intact and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-6 s: Show one simple seated slide down the existing sloped rust-orange canopy onto the visible lower service landing. Kett keeps the core hugged with the right arm and uses the left hand for balance. 6-10 s: Limit the height to the established short drop. Do not add a jump, flip, camera cut or second stunt. Kett ends on the lower service landing; the poncho is intact and the core is in the right hand.
```

## C14 — Pazar yardım ediyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C14.png · referans (yükleme sırası, kare üretiminde): ref/3.MARA_v1.png · ref/6.PAZAR_v1.png
```

> Not: Plan metni aynen. Replik R13 Mara 1,0-2,0 s (ağız kadrajda, 1,0 s) ilk vuruş. Kett kadrajda yok. Mara pazardaki tezgâhında kalır, kuleye ışınlanmaz (plan §8). Kol hâlâ yukarıda, tente katlı (kare başlangıç anı); kolun inmesi ve tentenin uzamaya başlaması Video'da. Plan Görsel cümlesi "the same brass awning lever previously shown" aynen (başlık notu 2). Mara giysi cümlesindeki "empty hands" nesne taşımama anlamında; bir elin kola dayanması planın cümlesi (çelişmez). Kolun ölçü ve tarafı planda yok → uydurulmadı.

### Görsel
```text
Reference 3 (Mara): take Mara's coral-red head with four eyes, indigo work clothes and cream apron from it. Reference 6 (market): take the food stall with its folded reinforced blue awning, tension cables and brass lever, and the dry copper market, from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Mara at the same food stall, coral-red four-eyed alien in cream apron and indigo clothes. One hand rests on the same brass awning lever previously shown. Above, the folded reinforced blue delivery canopy has visible tension cables and a metal nose rail. Background market remains dry. Tight medium shot with the lever and Mara's face readable, no Kett in this frame.

The camera is a medium close view of Mara and the brass lever, with the folded blue canopy at the upper edge. Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. Exactly two arms and two legs. Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. A bustling entirely alien open-air market stands on a dusty copper-built moon city. Behind Mara the dry copper market lies out of focus. The awning is still folded and Mara stays at her stall.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-3 s: Mara pulls the brass lever down once and shouts the assigned short line with playful defiance. 3-6 s: The existing reinforced blue canopy begins to extend overhead on its visible metal rails; keep its full deployment mostly out of frame. 6-10 s: No new gadget appears and Mara stays behind the stall. The awning system comes into use; Mara stays at her stall.

Dialogue performance, in this exact order:
1. MARA: "Free delivery!" Voice: Warm adult contralto, dry humor, confident calm, not a narrator.
```

## C15 — Mavi köprü

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C15.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png
```

> Not: Plan metni aynen. Repliksiz. Tente bu karede **tam açık ve gergin** (plan): R07 sayfasındaki "folded blue delivery canopy" satırı çelişeceği için yazılmadı, Ref 7'den yalnız sahanlıklar, raylar, kablolar, borular, kule alınır; açık tente plan metniyle tarif edilir. Vorr tenteye çıkmaz ve kadrajda değil (plan). Aşağıdaki "large trunk-faced alien porter" ve "floating amber jelly alien" planın cümlesi (FILM §3 kimlik tablosunda satırı yok, plan §3'te aynı tarif).

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 7 (roofs): take the service landings, the visible rails, the tension cables, the thick blue pipes and the copper weather tower from it. Reference 9 (weather core): take the transparent cylinder, the three silver ribs, the dark base and the side test valve from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Wide side view of the fully extended reinforced blue delivery canopy connecting two nearby service landings above the market. Visible support rails and tension cables hold the fabric taut. Small Kett, mustard poncho intact, is at the near edge with the core in the right hand. Below are a large trunk-faced alien porter, a floating amber jelly alien and distant other silhouettes. Weather tower sits beyond the far landing at screen right.

The camera is a wide lateral view, with Kett on the canopy and large and small aliens below. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. A bustling entirely alien open-air market stands on a dusty copper-built moon city. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. The blue bridge is connected, the poncho is intact and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-5 s: Follow one short careful run by Kett across the already deployed canopy to the far landing. 5-8 s: Fabric dips slightly under Kett's small weight but remains supported by rails and cables. Keep the core in the right hand. 8-10 s: Background aliens look up without crowd choreography. No guard follows onto the canopy. Kett reaches the landing on the tower side; the blue bridge stays connected.
```

## C16 — Takip henüz bitmedi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C16.png · referans (yükleme sırası, kare üretiminde): ref/4.VORR_v1.png · ref/7.CATILAR_v1.png
```

> Not: Plan metni aynen. Repliksiz. Vorr iki eli boş, silahsız, mavi kumaş köprüye girmez; küçük hardal figür (Kett) ve mavi tente arka plan nirengi noktasıdır, ikinci eylem odağı değil (kimlik cümlesi Kett için yazılmadı: kadrajda uzak ve çok küçük). Q8: Video ikinci vuruş "His weight produces heavy metallic footsteps." plan cümlesi aynen (başlık notu 1).

### Görsel
```text
Reference 4 (Vorr): take Vorr's face, body, dark brown uniform and copper shoulder armor from it. Reference 7 (roofs): take the exterior iron service staircase, the thick blue pipes and the copper weather tower from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Vorr, massive basalt alien in copper shoulder armor, on the clearly visible exterior iron staircase running parallel to the blue delivery canopy. He climbs toward the same weather tower, both hands empty. The blue canopy and a tiny mustard figure are distant background landmarks, not a second action focus. Compressed telephoto medium framing, dry late-afternoon copper surfaces.

The camera is a long-lens medium view, with Vorr on the separate metal staircase and the tower behind. Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. Exactly two arms and two legs, five thick fingers per hand. Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. A continuous exterior iron service staircase provides a parallel route to the weather tower. Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. Vorr comes by the iron staircase; a route on which he can catch up with Kett is shown.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-3 s: Track Vorr ascending one short flight of the established iron service staircase. 3-6 s: His weight produces heavy metallic footsteps. Keep him off the blue fabric bridge. 6-10 s: He does not teleport, fall or draw a weapon. Maintain the same direction toward the tower on screen right. Vorr comes by the iron staircase; a route on which he can catch up with Kett is shown.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (G01'deki gibi, bir kez):** Return silent videos **AÇIK** · Visible watermarking **KAPALI**.
> **Referanslar G01'de üretilir** (1-9, önce 1, sonra 1'in üzerinden 2); G02 yalnız 1 · 3 · 4 · 6 · 7 · 9'u kullanır ve onların onayından sonra başlar. Frames to Video'ya referans eklenmez (yalnız kare); referanslar kare üretiminde, kare promptunun kendi sırasıyla yüklenir.
> **Sıra:** G01 pilot kararından (C01 · C21 · C23) sonra. Kare kapısı geçmeden video üretilmez.
> **Kare kapısı (G02):** filigran/logo · istenmeyen yazı (cam, tezgâh, tabela) · C09 çekirdek sağ elde göğse yakın + sol el basamakta (el-nesne) · C10 yağmur yalnız camın arkasında, dışarısı kuru · C11 pul sol parmaklarda ve tek turuncu gemi · C12 Vorr tek keskin yüz, iki eli boş, silah yok · C13 kısa düşüş, alt sahanlık görünür, uçurum yok · C14 Mara tezgâhında, kol yukarıda, tente katlı · C15 tente tam açık ve gergin, tek Kett, Vorr yok · C16 Vorr demir merdivende, iki eli boş, mavi tentede değil · parmak/göz sayısı (Kett 3 parmak, Mara 4 göz 2×2, Vorr 5 parmak) · ikinci çekirdek.
> **Ses:** model sesi yok; replikler kurguda ayrı kayıt (HUMAN, dört ses kimliği): C10 R10 · C12 R11 R12 · C14 R13. Repliksiz: C09 C11 C13 C15 C16.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C09 kare | `kare/C09.png` | Görsel | ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png (bu sırayla) | 2 | |
| 2 | C10 kare | `kare/C10.png` | Görsel | ref/1.KETT_v1.png · ref/7.CATILAR_v1.png (bu sırayla) | 2 | |
| 3 | C11 kare | `kare/C11.png` | Görsel | ref/1.KETT_v1.png · ref/7.CATILAR_v1.png (bu sırayla) | 2 | |
| 4 | C12 kare | `kare/C12.png` | Görsel | ref/1.KETT_v1.png · ref/4.VORR_v1.png · ref/7.CATILAR_v1.png (bu sırayla) | 2 | |
| 5 | C13 kare | `kare/C13.png` | Görsel | ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png (bu sırayla) | 2 | |
| 6 | C14 kare | `kare/C14.png` | Görsel | ref/3.MARA_v1.png · ref/6.PAZAR_v1.png (bu sırayla) | 2 | |
| 7 | C15 kare | `kare/C15.png` | Görsel | ref/1.KETT_v1.png · ref/7.CATILAR_v1.png · ref/9.CEKIRDEK_v1.png (bu sırayla) | 2 | |
| 8 | C16 kare | `kare/C16.png` | Görsel | ref/4.VORR_v1.png · ref/7.CATILAR_v1.png (bu sırayla) | 2 | |
| 9 | C09 | `ham/C09_d1.mp4` | Frames to Video | kare/C09.png | 2 | |
| 10 | C10 | `ham/C10_d1.mp4` | Frames to Video | kare/C10.png | 2 | |
| 11 | C11 | `ham/C11_d1.mp4` | Frames to Video | kare/C11.png | 2 | |
| 12 | C12 | `ham/C12_d1.mp4` | Frames to Video | kare/C12.png | 2 | |
| 13 | C13 | `ham/C13_d1.mp4` | Frames to Video | kare/C13.png | 2 | |
| 14 | C14 | `ham/C14_d1.mp4` | Frames to Video | kare/C14.png | 2 | |
| 15 | C15 | `ham/C15_d1.mp4` | Frames to Video | kare/C15.png | 2 | |
| 16 | C16 | `ham/C16_d1.mp4` | Frames to Video | kare/C16.png | 2 | |

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · tur 1)

> **Q1 (kolda/göğüste işaret):** Kett'in tek işareti beyaz oval toka; "The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho." C09 C10 C11 C13 C15'te yazılı (merkez → taraf yok). C12'de Kett arkadan, toka görünmez → işaret cümlesi yazılmadı (giysi cümlesi tokayı taşır). C14 Mara, C16 Vorr: işaret yok (plan R03/R04).
> **Q2 (kimlik birebir):** FILM §3 KİMLİK CÜMLELERİ satırları kelime kelime kopyalandı (Kett yüz/eller/giysi/ayaklar/işaret · çekirdek gövde/bulut/taban · Mara 3 parça · Vorr 3 parça · R06/R07 satırları). Çekirdek gövde cümlesi tablodaki "A single …" biçimiyle bir önceki cümleden ayrı durur (büyük harf korundu). Nesne ölçüsü/tarafı: çekirdek 18 cm + sağ el; pirinç kolun (C14) ölçüsü ve tarafı planda yok → uydurulmadı. Kett'in C12 ayakları görünmediğinden "Broad padded feet" yazılmadı; C15 küçük figür ama kimlik tam.
> **Q3 (ORTAK GÖRÜNÜM):** "warm late-afternoon … palette" ve "one pale ringed planet" taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` (dosya başı, öneriyle). C09-C16 hepsi aynı akşamüstü ve aynı gezegen (§8 "aynı sıcak akşamüstü"); çelişen su/ses yok. Sıkı kadrajlarda (C10 C11 C14) gezegen kadraja basılabilir: kare denemesinde bakılır. ORTAK GÖRÜNÜM Video promptlarına eklenmedi (plan: yalnız Görsel başına).
> **Q4 (açıklığın ardı, kişinin arkası):** C10 cam duvarın ardı (özel bahçe, yağmur, iki odak dışı siluet; plan) + Kett'in arkası (kuru toz çatı hattı, sıcak gök) · C11 Kett'in arkası (kuru bakır çatı), sol arkada gemi · C12 Vorr'un arkası (iron service stair), Kett'in yanı (pas turuncusu tente) · C13 Kett'in arkası (bakır çatı), önü alt sahanlık, uçurum yok · C14 Mara'nın arkası (kuru pazar, odak dışı) · C15 tentenin altı (pazar, taşıyıcı ve jel uzaylı), ötede kule · C16 Vorr'un arkası (kule). C09: arka plan pazar kalabalığı ve rezervuar.
> **Q5 (akışkan kelimeleri):** `plume · smoke · steam · drip · wet · bubbles` yok; `droplet` yok. `rain` yalnız film konusu ve atmosferli açık hava: C10 (özel sera, camın arkası; plan), C12 (Vorr'un repliği "That rain is company property"). `dust` (C10) katı hâl. Vakum yok.
> **Q6 (ekran/gösterge):** hiçbir çekimde ekran ya da gösterge adıyla yazılmadı; "no readable signage" (C10) plan cümlesi; yazı kilidi ORTAK GÖRÜNÜM "no written text, no logos".
> **Q7 (Reference yalnız sayfada görüneni ister):** 1 yüz/ponço/toka/gövde (C12'de arkadan görünüm sayfada yok → "cobalt-blue body and mustard poncho" istendi, arka plan metinle) · 3 başlık, dört göz, giysi · 4 yüz, uniforma, omuz zırhı · 6 yemek tezgâhı, kol, kalabalık · 7 çatı, borular, cam bahçe, pas turuncusu tente, katlı mavi tente, demir merdiven, kule, iskele (tam açık tente C15'te sayfadan istenmedi, yalnız raylar/kablolar) · 9 silindir, kaburgalar, taban, valf. Çiçek, saksı, fincan, damla, jel uzaylı, taşıyıcı: sayfada yok → metinle.
> **Q8 (Video'da ses kelimesi · zıt istek):** model sesi kapalı filmde ses kelimesi **plan cümlesi olarak** iki yerde: C11 "Let the engine fade without dialogue." (ses + `dialogue` olumsuz kalıpta) ve C16 "His weight produces heavy metallic footsteps." Plan cümlesi aynen kalma kuralı gereği korundu; DERS Y13 uyarısı beklenir. Alternatifler: "Let the skiff fade into the distance." / "His weight shows in each heavy step." C12 "Kett's brief reply is heard off-screen" plan cümlesi (G01 C08 ile aynı), replik kurguda. Zıt istek yok; C11 "motionless" orta vuruşta (son vuruş donmaz).
> **Uzunluk (karakter, ölçülmemiş tahmin ±200; hedef Görsel 2.000-3.200 · Video 1.000-1.500 · tavan 4.300):** "Görsel kr · Video kr" (Görsel iki paragrafın toplamı).

| Çekim | Düzeltilen sorular (1-8) | Görsel kr · Video kr | Bilerek bırakılan + gerekçe |
|:--:|---|:--:|---|
| C09 | 1 (toka işareti) · 2 (Kett 5 parça + çekirdek 3 parça + pazar/kule satırları birebir) · 4 (Kett'in arkası pazar kalabalığı, kule, rezervuar) · 7 (Ref 7'den yalnız çatı/boru/kule) | ≈3.250 · ≈1.050 | Kamera satırındaki "bridge" planın kelimesi; "toe pads" plan (Kett'in "padded feet" ile çelişmez) |
| C10 | 1 · 2 (Kett + çekirdek + R07 cam bahçe/boru satırı birebir) · 4 (cam duvarın ardı ve Kett'in arkası) · 5 (`rain` yalnız camın arkasında) | ≈3.400 · ≈1.350 | Replik ilk vuruşa tam sığsın diye ilk vuruş 0-7 s; "delivers the short line" plan ağız ipucu; "no readable signage" plan |
| C11 | 1 · 2 (Kett + çekirdek + R07 boru/yüzey satırı) · 4 (Kett'in arkası) · 8 (başlık notu 1) | ≈3.150 · ≈1.000 | "engine" + "dialogue" plan cümlesi aynen; R06 iskele satırı yazılmadı (plan "lifts away from its dock" ile çelişir); "motionless" orta vuruşta |
| C12 | 2 (Vorr 3 parça + Kett gövde/eller/giysi + çekirdek + R07 satırları; Vorr'un elleri plan cümlesinde boş) · 4 (Vorr'un arkası merdiven, Kett'in yanı tente) · 7 (Ref 1 arkadan görünümü metinle) | ≈3.550 · ≈1.450 | İşaret yazılmadı (Kett arkadan); olumsuz blok Vorr R04 giysi cümlesi (plan); plan içi tente çelişkisi (pas turuncusu ↔ mavi) iki satırla yazıldı; "heard off-screen" plan |
| C13 | 1 · 2 (Kett + çekirdek + pas turuncusu tente satırı) · 4 (Kett'in arkası çatı, alt sahanlık, uçurum yok) | ≈3.250 · ≈1.000 | Mavi yük tentesi satırı yazılmadı (bu çekimde pas turuncusu tente, SAHNE DÜZENİ); "No guard in focus, no open abyss" plan |
| C14 | 2 (Mara 3 parça + R06 yemek tezgâhı/genel birebir) · 4 (Mara'nın arkası kuru pazar) · 7 (kol/tente sayfada, çiçek yok) | ≈2.400 · ≈1.150 | "previously shown" plan cümlesi aynen (başlık notu 2); kol ölçüsü planda yok; "empty hands" + elin kolda olması çelişmez |
| C15 | 1 · 2 (Kett + çekirdek + R06 genel + R07 boru satırı) · 4 (tentenin altı ve ötesi) · 7 (tam açık tente sayfada yok, plan metni) | ≈3.250 · ≈1.050 | Taşıyıcı ve jel uzaylı plan cümlesi (kimlik tablosunda yok); R07 "folded canopy" satırı yazılmadı (tam açık tente ile çelişir) |
| C16 | 2 (Vorr 3 parça + R07 merdiven/boru + R06 kule satırı birebir) · 4 (Vorr'un arkası kule) | ≈2.450 · ≈1.000 | Kett kimliği yazılmadı (uzak, çok küçük, plan "not a second action focus"); "footsteps" plan cümlesi aynen (başlık notu 1); olumsuz blok Vorr R04 giysi cümlesi (plan) |
