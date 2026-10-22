# 🖼️ RAIN_THIEF — Prompt grubu G01 (çekimler C01–C08 · M1 pazar) · tur 1 + Fable sadakat revizyonu + F5 birleştirme

> Yazan: goruntu-yonetmeni (faz 5, tur 1; revizyon: plan cümleleri karakteri karakterine aynen; birleştirme: `ODA/F5_fable_birlestirme_1.md` "## G01" 10 madde). Kaynak: `RAIN_THIEF_4DK_24_KLIP_FILM_PLANI.md` (sahip planı; "plandan asla dışarı çıkma") + FILM.md §3 (ORTAK GÖRÜNÜM · ORTAK HAREKET · SAHNE DÜZENİ · DÜNYA KURALLARI · DEVAMLILIK) + §4 çekim satırı + §5 replik saniyeleri + `ODA/F5_yazim_karari.md`.
> Eklenen her cümle plan malzemesidir (plan R01-R09 istemleri, plan §4 mekân, plan çekim "Kamera" ve "Devamlılık" satırı, plan §8); yeni olay, kişi, nesne, ışık kaynağı, ekran, yazı, renk ya da sıfat yok.
> **Sadakat kuralı:** planın Görsel ve Video istemindeki her cümle aynen durur; tek izinli ekleme vuruş öneki ("0-3 s: ") ve plan cümlesinden SONRA gelen ayrı yeni cümlelerdir. Plan cümlesi uzatılmadı, birleştirilmedi, bağlaçla bağlanmadı.
> **Görsel düzeni:** referans anahtarları → ORTAK GÖRÜNÜM (FILM §3, birebir) → planın Görsel istemi aynen (yalnız M düzeltmesi) → boş satır → ek paragraf (plan Kamera satırı · KİMLİK CÜMLELERİ birebir · plan R06 mekân cümleleri · plan Devamlılık satırı).
> **Video düzeni:** ORTAK HAREKET (FILM §3, birebir) → planın video istemi aynı sırayla 2-4 vuruşa bölünmüş → plan cümlelerinden sonra ayrı ek cümleler (plan Devamlılık satırının İngilizcesi) → plan "Dialogue performance" bloğu aynen (replikli çekimde). Prompt gövdesine çekim kodu, referans kodu, başlık satırı, "Clip n of N" yazılmadı.
> **Model sesi:** FILM §6'ya göre kullanılmaz (plan §7 "modelin ses ürettiği varsayılmaz"); §5 Kaynak "ağız kadrajda — temiz replik ayrı kayıt" olan replikler videoda oyunculuk ve ağız ipucudur, kurguda ayrı kayıt gelir. Planın "Kurgu sesi" satırları FILM §6'dadır, prompta yazılmadı.
> **Biçim düzeltmeleri (M · `ODA/F5_yazim_karari.md`):** C01 "The first frame already reveals" → "The frame already reveals" · C05 "from the previous shot" silindi · Mara kare promptunda "one narrow vertical speaking mouth" → "one narrow vertical mouth" (referans promptunda plan metni kalır) · ORTAK HAREKET'in "spoken lines … recorded separately" cümlesi repliksiz çekimlerde (C03 C05) atıldı · C05 Video'da kadraj dışı konuşma cümlesi ve Dialogue bloğu çıktı.
> **KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6** — FILM §3 ORTAK GÖRÜNÜM "warm late-afternoon … palette" (ışık) ve "one pale ringed planet" (gezegen) taşıyor. Plan §6 birebir olduğu için dokunulmadı (birleştirme P5: plan korundu, SK7). Öneri (uygulanmadı, Fable kararı): `Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm copper and mustard palette with cobalt-blue accents, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character.` (ışık ve gezegen zaten plan R06 mekân cümlesinde: "One pale planet with a thin gold ring hangs in the warm late-afternoon sky."). Makro/yakın planlarda (C05, C07) "one pale ringed planet" kadraja basılabilir: ilk kare denemesinde bakılır.

---

## REFERANS PROMPTLARI (yalnız ilk grupta · plan R01-R09 İngilizce istemleri AYNEN, hat adlarıyla)

> Plan R01-R09 tek görünüşlü istemlerdir; plan metni korundu (panel kalıbı uygulanmadı). ORTAK GÖRÜNÜM referans promptlarına eklenmedi (plan R istemleri kendi arka planını taşır: "warm gray studio background"; SK1, sahibe bilgi). Sıra (plan §10): 1 → 2 (1'in üzerinden düzenleme) → 3 → 4 → 5 → 6 → 7 → 8 → 9. Ponçosuz Kett sıfırdan üretilmez. Sahip her görseli seçip `ref/` altına `<No>.<AD>_v1.png` adıyla kaydeder; yüz, göz sayısı, parmak sayısı, ponço/toka ya da çekirdek biçimi bozuk görsel kullanılmaz.
> Plan R01-R09 "Hedef dosya" adları → hat adları: R01_KETT_COAT → 1.KETT · R02_KETT_NO_COAT → 2.KETT_TULUM · R03_MARA → 3.MARA · R04_VORR → 4.VORR · R05_TULA → 5.TULA · R06_MARKET → 6.PAZAR · R07_ROOFS → 7.CATILAR · R08_WEATHER_CROWN → 8.HAVA_TACI · R09_WEATHER_CORE → 9.CEKIRDEK. R02 metnindeki "R01" plan metnidir (aynen; birleştirme P8: plan korundu).

### 1.KETT
```
DOSYA     ref/1.KETT_v1.png
PANELLER  tek görünüş (plan R01): three-quarter front standing, boş eller
```
```text
Create one full-body cinematic reference portrait of Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. Three-quarter front standing pose, empty hands visible, neutral expression with alert intelligence, warm gray studio background, realistic tactile skin and cloth, cinematic photorealism, no text, no grid, no extra pose, no weather capsule.
```

### 2.KETT_TULUM
```
DOSYA     ref/2.KETT_TULUM_v1.png
KAYNAK    düzenleme: ref/1.KETT_v1.png (R01 üzerinden; yalnız ponço ve toka çıkar) · SAHİP İSTİSNASI 19.10.2026 (iki dosya)
PANELLER  tek görünüş (plan R02): aynı poz, ponçosuz
```
```text
Edit the supplied R01 Kett reference into the exact same adult alien at the exact same scale and pose. Remove only the mustard poncho and its white oval neck clasp, revealing the already established plain dark teal utility under-suit and small belt pocket. Preserve the identical cobalt-blue skin, flattened head, two amber eyes, two folded ear fins, three fingers per hand and padded feet. No redesign, no new costume layers, no body markings added, empty hands, same neutral studio background, one full-body figure, no text.
```

### 3.MARA
```
DOSYA     ref/3.MARA_v1.png
PANELLER  tek görünüş (plan R03): three-quarter front standing, boş eller
```
```text
Create one full-body cinematic reference portrait of Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical speaking mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. Exactly two arms and two legs. Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. Calm irreverent expression, three-quarter front pose, warm gray studio background, realistic skin and fabric, cinematic photorealism, no text, no contact sheet, no extra character.
```

### 4.VORR
```
DOSYA     ref/4.VORR_v1.png
PANELLER  tek görünüş (plan R04): three-quarter front standing, iki boş el
```
```text
Create one full-body cinematic reference portrait of Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. Exactly two arms and two legs, five thick fingers per hand. Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. Intimidating through size and stillness, not a monster. Three-quarter front pose, both empty hands visible, warm gray studio background, realistic mineral skin and aged metal, no text or logos.
```

### 5.TULA
```
DOSYA     ref/5.TULA_v1.png
PANELLER  tek görünüş (plan R05): three-quarter front standing, elinde düz bakır fincan
```
```text
Create one full-body cinematic reference portrait of Tula, an elderly adult nonhuman flower seller, one hundred twenty centimeters tall, broad pearl-lilac shell-ridged head, two dark oval eyes, one small mouth, a few short sensory filaments beneath the cheeks, no human hair or ears. Compact mature body with a slightly stooped adult posture, two arms and two legs, simple muted green robe. Holds one plain small copper cup in both hands. A patient tired expression, never a child. Three-quarter front standing pose, warm gray studio background, cinematic photorealism with tactile skin and cloth, no text, no other character.
```

### 6.PAZAR
```
DOSYA     ref/6.PAZAR_v1.png
PANELLER  tek görünüş (plan R06): M1 ana geniş plan
```
```text
Create one cinematic wide establishing plate of a bustling entirely alien open-air market on a dusty copper-built moon city. Center: one dry copper fountain. Lower right: a small flower stall with one pale closed alien flower and a dry coin-operated water spout; adjacent is a food stall with a folded reinforced blue delivery awning, tension cables and a brass lever. Far left: a dock with one small orange commuter skiff. Upper right: copper weather tower reached by blue service pipes and exterior iron stairs. A huge transparent blue water reservoir curves above the district. Sealed luxury greenhouse terraces receive rain inside, while every public surface is dry. Eight different nonhuman crowd silhouettes in layered depth; no humans. One pale planet with a thin gold ring in the warm late-afternoon sky. Tactile cinematic realism, readable geography, no text, no montage.
```

### 7.CATILAR
```
DOSYA     ref/7.CATILAR_v1.png
PANELLER  tek görünüş (plan R07): M2 çatılar, iki takip rotası
```
```text
Create one cinematic wide environment plate of the roof route above the established copper alien market, about six meters above street level. Keep the weather tower at screen right and the skiff dock far left. Include a sealed glass luxury garden with rain strictly inside, a short sloping reinforced rust-orange canopy dropping less than two meters to a lower service landing, a separate folded blue delivery canopy on visible rails and tension cables able to bridge two nearby service landings, and a continuous exterior iron service staircase providing a parallel route to the weather tower. Thick blue public water pipes connect these structures. The public roof surfaces remain dry. Transparent reservoir arc overhead and one pale ringed planet in the same warm sky. No foreground characters, no text, no multiple views.
```

### 8.HAVA_TACI
```
DOSYA     ref/8.HAVA_TACI_v1.png
PANELLER  tek görünüş (plan R08): M3 hava kulesinin üstü
```
```text
Create one cinematic wide environment plate of a copper weather-control platform eighteen meters above the established alien market. A single central copper console has one empty weather-core socket with three vertical alignment grooves, and one large blue manual handwheel directly beside it. Show a simple physical end-stop latch on the wheel, no electronic screen or readable writing. An exterior iron staircase entrance is visible on the near left. Existing blue distribution pipes connect the console to the large transparent water reservoir arc overhead; closed public rain outlets are visible along the reservoir. Low copper safety rails, dry metal floor, same pale ringed planet and warm late-afternoon light. No characters, no extra consoles, no text, no black hole.
```

### 9.CEKIRDEK
```
DOSYA     ref/9.CEKIRDEK_v1.png
PANELLER  tek görünüş (plan R09): makro ürün referansı, tek nesne
```
```text
Create one cinematic macro product reference of a single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. One tiny water drop may rest at the closed side valve. The base has three alignment ridges matching a mechanical socket. Object lies diagonally on a neutral dark surface, realistic glass and metal, no hand, no text, no labels, no face, no extra capsule, one object only.
```

---

## KİMLİK CÜMLELERİ — plan R01-R09 istemlerinden BİREBİR · Fable FILM.md §3 `### KİMLİK CÜMLELERİ` tablosuna kopyalar

> Her cümle Görsel promptunda kelime kelime geçer (kadrajda görünen parçalar). Kaynak: plan R istemi cümleleri; türev satırlar (†) işaretli.
> † **Türev satırlar:** (a) 1 · işaret: plan R01 "one clearly visible white oval breakaway neck clasp" + FILM §3 işaret kuralı (sayı + konum + `the only marking`); taraf yok (boyun önü ortası, simetrik). (b) 1 · eller (makro): R01 "cobalt-blue body" + "three fingers on each hand" makro kadraj için (C05; kadrajda yalnız eller). (c) 2: R02 "Preserve …" ve "revealing …" cümleleri tanım hâline getirildi (G03 için). (d) 6, 7 ve 8 mekân satırları plan R06-R08 tarif listesinin cümle biçimine çevrilmiş hâlidir; kelimeler plan kelimeleridir. **(e) Birleştirme ekleri:** "6 · yemek tezgâhı (çiçek tezgâhı kadrajda yok)" satırı C07/C08 için eklendi (birleştirme G01 #6: "Adjacent to the flower stall, a food stall" → "A food stall"); Fable §3'e kopyalar.
> Mara "one narrow vertical speaking mouth" → kare/Görsel için "one narrow vertical mouth" (M: Görsel'de konuşma kelimesi hata; planın Türkçesi "ince dikey ağız"). Referans promptunda plan metni kalır.
> Vorr giysi cümlesindeki "no helmet, no cloak, no handheld weapon and no holster" plan R04 cümlesidir ("Vorr silahsız" plan §8 devamlılığı); olumsuz blok kuralına karşı plan korundu (birleştirme P9), olumlu karşılığı ("both hands empty") aynı çekimlerde ayrıca yazıldı.

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Kett · yüz + beden | Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. |
| 1 | Kett · eller + bacaklar | Exactly two arms, two legs and three fingers on each hand. |
| 1 | Kett · giysi (ponço + toka + tulum) | Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. |
| 1 | Kett · ayaklar | Broad padded feet. |
| 1 | Kett · işaret † | The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. |
| 1 | Kett · eller (makro) † | Kett has cobalt-blue skin and three fingers on each hand. |
| 2 | Kett · ponçosuz yüz + beden † | The identical cobalt-blue skin, flattened head, two amber eyes, two folded ear fins, three fingers per hand and padded feet. |
| 2 | Kett · ponçosuz giysi † | Kett wears only the already established plain dark teal utility under-suit with one small belt pocket, with no poncho, no neck clasp and no body markings. |
| 3 | Mara · yüz + beden | Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. |
| 3 | Mara · kollar | Exactly two arms and two legs. |
| 3 | Mara · giysi | Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. |
| 4 | Vorr · yüz + beden | Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. |
| 4 | Vorr · kollar + eller | Exactly two arms and two legs, five thick fingers per hand. |
| 4 | Vorr · giysi | Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. |
| 5 | Tula · yüz + beden | Tula, an elderly adult nonhuman flower seller, one hundred twenty centimeters tall, broad pearl-lilac shell-ridged head, two dark oval eyes, one small mouth, a few short sensory filaments beneath the cheeks, no human hair or ears. |
| 5 | Tula · gövde + cüppe | Compact mature body with a slightly stooped adult posture, two arms and two legs, simple muted green robe. |
| 5 | Tula · fincan | Holds one plain small copper cup in both hands. |
| 6 | Pazar · genel | A bustling entirely alien open-air market stands on a dusty copper-built moon city. |
| 6 | Pazar · çeşme † | One dry copper fountain stands at the center of the market. |
| 6 | Pazar · çiçek tezgâhı † | At the lower right, a small flower stall holds one pale closed alien flower and a dry coin-operated water spout. |
| 6 | Pazar · yemek tezgâhı † | Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. |
| 6 | Pazar · yemek tezgâhı (çiçek tezgâhı kadrajda yok) † | A food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. |
| 6 | Pazar · iskele † | At the far left, a dock holds one small orange commuter skiff. |
| 6 | Pazar · kule + rezervuar † | At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. |
| 6 | Pazar · sera + kuru yüzey † | Sealed luxury greenhouse terraces receive rain inside, while every public surface is dry. |
| 6 | Pazar · kalabalık † | Eight different nonhuman crowd silhouettes stand in layered depth. |
| 6 | Pazar · gezegen † | One pale planet with a thin gold ring hangs in the warm late-afternoon sky. |
| 7 | Çatılar · cam bahçe † | A sealed glass luxury garden has rain strictly inside. |
| 7 | Çatılar · pas turuncusu tente † | A short sloping reinforced rust-orange canopy drops less than two meters to a lower service landing. |
| 7 | Çatılar · mavi yük tentesi † | A separate folded blue delivery canopy on visible rails and tension cables is able to bridge two nearby service landings. |
| 7 | Çatılar · demir merdiven † | A continuous exterior iron service staircase provides a parallel route to the weather tower. |
| 7 | Çatılar · borular + yüzey † | Thick blue public water pipes connect these structures, and the public roof surfaces remain dry. |
| 8 | Hava tacı · konsol + yuva + çark † | A single central copper console has one empty weather-core socket with three vertical alignment grooves, and one large blue manual handwheel directly beside it. |
| 8 | Hava tacı · kilit † | A simple physical end-stop latch sits on the wheel, with no electronic screen or readable writing. |
| 8 | Hava tacı · merdiven girişi † | An exterior iron staircase entrance is visible on the near left. |
| 8 | Hava tacı · borular + rezervuar † | Existing blue distribution pipes connect the console to the large transparent water reservoir arc overhead; closed public rain outlets are visible along the reservoir. |
| 8 | Hava tacı · zemin + korkuluk † | Low copper safety rails, dry metal floor, same pale ringed planet and warm late-afternoon light. |
| 9 | Çekirdek · gövde | A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. |
| 9 | Çekirdek · bulut | Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. |
| 9 | Çekirdek · taban | The base has three alignment ridges matching a mechanical socket. |

---

## C01 — Çalınmış hava

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C01.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/6.PAZAR_v1.png · ref/9.CEKIRDEK_v1.png
```

> Not: **Plan pilotu** (çekirdek tutuşu, plan §10) ve açılış (ILK_30 §6: doğrudan koşunun içinde, yazı/logo yok). Plan Görsel ve Video metni aynen; M düzeltmesi "The frame already reveals". Replik R01 2,2-5,7 s (FILM §5; ilk vuruş 0-6 s). Risk: T01 el-nesne; çekirdek sağ elde sabit, tek nesne, kırılmaz; Kett'in sol eli plan dışı (yazılmadı). **Pilot bozulursa** (birleştirme P10, sahibe): ikinci denemede kamera orta-geniş mesafe.

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 6 (market): take the dry copper fountain and the market stalls from it. Reference 9 (weather core): take the transparent cylinder, the three silver ribs, the dark base and the side test valve from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. One adult cobalt-blue alien Kett, mustard poncho fastened with one white oval neck clasp, dark teal under-suit, mid-stride beside a dry copper fountain. Kett holds one eighteen-centimeter transparent weather core in the right hand, three silver ribs around a tiny storm cloud. Very low close tracking composition, alien market stalls behind, no guard face in focus. The frame already reveals the stolen miniature storm.

The camera is very low and close, tracking beside Kett, who runs from the left of the frame toward the right. A bustling entirely alien open-air market stands on a dusty copper-built moon city. One dry copper fountain stands at the center of the market. Every public surface is dry. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Broad padded feet. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand: a single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. The poncho is fastened; the core is in the right hand; the air is dry.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-6 s: Track laterally alongside Kett running left to right past the dry fountain. Keep the core fixed in the right hand. One small internal lightning flash, no external lightning bolt. Kett says the single assigned line with breathless dry amusement. 6-10 s: Stay in this one continuous shot. Kett keeps running left to right and the tracking move carries on. The poncho stays fastened, the core stays in the right hand, and the air stays dry.

Dialogue performance, in this exact order:
1. KETT: "Just a little bad weather. Worth a whole ship." Voice: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak.
```

## C02 — Takipçi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C02.png · referans (yükleme sırası, kare üretiminde): ref/4.VORR_v1.png · ref/6.PAZAR_v1.png
```

> Not: Açılış (ILK_30 §6): muhafız kalabalığı yararak seslenir. Plan metni aynen. Replik R02 1,0-4,5 s (ilk vuruş). Plan "Kett ekran dışı sağda" video sonunda ve Görsel ekinde. Birleştirme #1: ek paragraftaki sekiz-siluet ve "açılmış koridor" cümleleri sadeleşti (iki bulanık siluet).

### Görsel
```text
Reference 4 (Vorr): take Vorr's face, body, dark brown uniform and copper shoulder armor from it. Reference 6 (market): take the dry copper market street and its crowd silhouettes from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. One massive basalt-skinned alien security officer Vorr in copper shoulder armor, two arms, two narrow gold eyes, planted in a crowded dry copper market aisle. Chest-up low-angle portrait. Blurred tall yellow crest-headed and round teal shell-backed aliens part behind him. Vorr has no handheld weapon. His gaze points toward screen right, following Kett.

The camera is slightly below Vorr, a chest-up medium close view, with two blurred aliens of different species in the background. Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. Exactly two arms and two legs, five thick fingers per hand. Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. Both of Vorr's hands are empty. A bustling entirely alien open-air market stands on a dusty copper-built moon city. Every public surface is dry. Two blurred nonhuman silhouettes of different species part behind Vorr. Kett is off-screen to the right.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-5 s: A short steady push toward Vorr as he plants one heavy foot and shouts the assigned line toward screen right. Only Vorr speaks. 5-8 s: Background alien silhouettes step out of his path without changing species or number. 8-10 s: No cutaway and no weapon appears. The push ends on Vorr, who stays unarmed while Kett stays off-screen at the right.

Dialogue performance, in this exact order:
1. VORR: "Bring back the rain! That forecast belongs to us." Voice: Deep restrained adult bass, slow authority, no monster growls.
```

## C03 — Dünyanın kuralı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C03.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/6.PAZAR_v1.png
```

> Not: Açılış (ILK_30 §6): dünyanın adaletsiz kuralı tek geniş planda. Replik yok → ORTAK HAREKET'te "spoken lines" cümlesi atıldı, Dialogue bloğu yazılmadı. Plan video cümlesi "Atmospheric crowd audio only; no dialogue, no subtitles." plan aynen (Fable: film_dogrula M hatası vermiyor; DERS Y13 yalnız uyarı → plan korunur; birleştirme P6). Plan Görsel'in "interior rain" ve Devamlılık "kamusal alan kuru, özel sera ıslak" bu çekimin konusudur (atmosfer var, vakum yok). R06 "no humans" yazılmadı (INSANSIZ ↔ kişi zamiri tuzağı; "nonhuman" cümleleri kaldı). Birleştirme #5: ek son cümlede "escape skiff" → "orange commuter skiff".

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body and mustard poncho from it, kept small in the wide view. Reference 6 (market): take the market layout, the orange skiff dock, the copper weather tower, the water reservoir and the greenhouse terraces from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Wide elevated cinematic view of the same alien market. Kett is a small cobalt-blue figure with a mustard poncho moving left to right below. Eight visibly different background alien species occupy the stalls, mostly silhouettes and back views. At far left sits one small orange commuter skiff. At upper right a copper weather tower connects to a huge transparent blue water reservoir; enclosed private garden terraces have interior rain, while the public market is dry. One pale ringed planet in the sky.

The camera is high and wide, so that the market, the orange skiff at the left and the copper weather tower at the right sit in one geography. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. Kett carries the core in the right hand: a single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. A bustling entirely alien open-air market stands on a dusty copper-built moon city. One dry copper fountain stands at the center of the market. At the lower right, a small flower stall holds one pale closed alien flower and a dry coin-operated water spout. Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. At the far left, a dock holds one small orange commuter skiff. At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. Sealed luxury greenhouse terraces receive rain inside, while every public surface is dry. Eight different nonhuman crowd silhouettes stand in layered depth. One pale planet with a thin gold ring hangs in the warm late-afternoon sky. The public area is dry, the private greenhouses receive rain inside, the orange commuter skiff is at the left and the tower is at the right.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-5 s: Slowly crane upward from the market to reveal the reservoir and private greenhouse rainfall. Keep Kett small, moving steadily toward screen right. 5-10 s: The orange skiff stays on the left, the copper weather tower on the right. The public market remains completely dry. Atmospheric crowd audio only; no dialogue, no subtitles. The sealed greenhouse terraces keep their rainfall inside. Kett's mustard poncho stays fastened and the core stays in the right hand.
```

## C04 — Bir damlanın bedeli

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C04.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/5.TULA_v1.png · ref/6.PAZAR_v1.png
```

> Not: Plan metni aynen. Replik R03 Tula 1,0-4,5 s (ilk vuruş); Kett konuşmaz. "Tek saksı ve tek fincan kurulur" (plan §8). Fincan boş, musluk su vermez. Birleştirme #8: ek paragrafa Kett'in ekran tarafı ve yönü (plan C01-C03 soldan sağa).

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 5 (Tula): take Tula's shell-ridged head, face, muted green robe and copper cup from it. Reference 6 (market): take the small flower stall and its dry coin-operated water spout from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Two aliens only in sharp focus at a small dry flower stall. Elder Tula has a wide pearl-lilac ridged shell-like head, dark oval eyes and a simple muted green robe, holding an empty cup beneath a dry coin-operated copper spout. Beside Tula, Kett pauses with the weather core still in the right hand. One pale closed alien flower in a cracked ceramic pot. The core cloud is visible. No written prices in the image.

The camera frames Tula and Kett in a restrained medium two-shot, with one pale flower and the empty cup in the foreground. Kett, arriving from screen left, stands at Tula's left and faces screen right. Tula, an elderly adult nonhuman flower seller, one hundred twenty centimeters tall, broad pearl-lilac shell-ridged head, two dark oval eyes, one small mouth, a few short sensory filaments beneath the cheeks, no human hair or ears. Compact mature body with a slightly stooped adult posture, two arms and two legs, simple muted green robe. Holds one plain small copper cup in both hands. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand: a single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. At the lower right, a small flower stall holds one pale closed alien flower and a dry coin-operated water spout. Behind the two, the dry copper market stalls stand out of focus. The stall has one pot and one empty cup; the poncho is fastened and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-5 s: Hold a restrained medium two-shot. Tula tilts the empty cup under the spout and quietly speaks the assigned plea. 5-8 s: Kett slows and looks from the cup to the closed flower without speaking. 8-10 s: Keep the core in Kett's right hand throughout. The spout releases no water. The poncho stays fastened.

Dialogue performance, in this exact order:
1. TULA: "One drop. Please. The flower can't wait for payday." Voice: Soft older adult voice, breath and patience, clear words.
```

## C05 — Hırsızın durması

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C05.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/5.TULA_v1.png · ref/9.CEKIRDEK_v1.png
```

> Not: Plan C05 Referanslar R01 · R05 · R09 korundu (plan listesi). Tula kadrajda yok ve R05 sayfasında çiçek ya da saksı yok; "Reference 5" cümlesi (birleştirme #4) yalnız çiçeğin Tula'nın tezgâhına ait olduğunu söyler, Tula'yı ve fincanını anmaz; sayfadan kadraja bir şey istenmez. DERS Y2 uyarısı olası (ref 5 için kadrajda kimlik cümlesi yok): gerekçe 8 SORU'da.
> Plan C05 Görsel M düzeltmesi: "from the previous shot" silindi. Replik R04 (Kett, kadraj dışı, 5,0 s, kurguda): Video'ya yazılmadı, Dialogue bloğu çıktı; planın "Kett speaks the assigned line off-screen, with regret" cümlesi konuşma kelimesi olduğundan "face stays out of frame … with quiet regret" biçimine çevrildi. Görsel başlangıç anıdır: damla henüz çiçeğe değmedi, çiçek bütünüyle soluk ve kapalı (plan Devamlılık sonucu "bir yaprak renklenir" video sonunda olur). Birleştirme #4: parmak sayısı cümlesinden sonra ayrı "One of the three fingers on each hand is the thumb." Plan Görsel "suspended drop" ↔ Video "Release … drop" çelişkisi plan içidir (birleştirme P1, SK3): plan cümleleri aynen.

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's cobalt-blue skin and three-fingered hands from it. Reference 5 (Tula): the pale flower belongs to Tula's flower stall. Reference 9 (weather core): take the transparent cylinder, the three silver ribs, the dark base and the small side test valve from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Extreme close-up of Kett's cobalt-blue hands holding the same transparent storm core, right hand supporting its body, left thumb resting on its tiny side test valve. A single suspended drop hangs above the pale alien flower. Three silver ribs and the dark base of the capsule are clearly visible. Only one flower and one drop. The weather core is not broken.

The camera is macro, filling the frame with the core's side test valve, the single drop and a part of the flower pot. Kett has cobalt-blue skin and three fingers on each hand. One of the three fingers on each hand is the thumb. A single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Inside is a miniature turbulent gray-blue cloud with a very faint lightning flicker; this is a symbolic control medium, not a creature. The base has three alignment ridges matching a mechanical socket. Below the drop, the one pale closed alien flower sits in a cracked ceramic pot at a small flower stall, with a dry coin-operated water spout and the dry copper stall surface softly out of focus behind it. The flower is still entirely pale and closed. The core is intact and unbroken.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. No built-in captions, subtitles, music or end card.

0-3 s: Release exactly one small drop from the side test valve onto the flower. 3-7 s: One petal slowly gains a soft turquoise color as it absorbs the drop; the flower does not instantly multiply or fully blossom. 7-10 s: Kett's face stays out of frame and the hands stay gentle and unhurried, with quiet regret. No whole cloud escapes. Maintain macro framing. The core stays intact and the one flower stays the only plant in frame.
```

## C06 — Kaçıştan vazgeçiş

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C06.png · referans (yükleme sırası, kare üretiminde): ref/1.KETT_v1.png · ref/3.MARA_v1.png · ref/6.PAZAR_v1.png
```

> Not: Plan metni aynen. İki replik: R05 Mara 1,0-2,5 s (kadraj dışı/yumuşak odak, ağız oynamaz) ilk vuruş (0-3 s) · R06 Kett 3,3 s (Fable FILM §5'te 4,5 s yapar → 4,5-7,0 s) ikinci vuruş (3-7 s). Birleştirme #2: vuruşlar 0-3 / 3-7 / 7-10 s; kamera itmesi son vuruşta. Plan "Kett glances …, answers …, then turns …" tek cümle olarak 3-7 s'te. Plan "do not animate a second detailed mouth" korundu. Plan Görsel "Kett's gaze turns toward the tower" ↔ Video önce gemiye bakış: plan içi (birleştirme P2, SK4) → aynen.

### Görsel
```text
Reference 1 (Kett with poncho): take Kett's face, body, mustard poncho and white neck clasp from it. Reference 3 (Mara): take Mara's coral-red head with four eyes, indigo work clothes and cream apron from it. Reference 6 (market): take the food stall with its folded blue awning and brass lever, the orange skiff dock, the blue service pipes and the copper weather tower from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Kett in a medium foreground portrait at the route fork, weather core in the right hand, mustard poncho still fastened. Behind, tall coral-red four-eyed cook Mara in an indigo outfit and cream apron stands beside a food stall with a blue folded awning and a brass lever. The orange skiff is small on the far left; blue service pipes lead toward the copper tower on the upper right. Kett's gaze turns toward the tower.

The camera holds Kett in the foreground, Mara's stall behind, the orange skiff far to the left and the tower high on the right. Kett, an adult nonhuman alien courier, ninety-five centimeters tall, slender cobalt-blue body, broad flattened head, two large amber eyes, two short folded ear fins, no hair and no human ears. Exactly two arms, two legs and three fingers on each hand. Wears a short mustard-yellow sleeveless poncho secured by one clearly visible white oval breakaway neck clasp, over a plain dark teal utility under-suit with one small belt pocket. The one white oval breakaway neck clasp sits at the center front of the neck and is the only marking on the poncho. Kett holds the core in the right hand: a single eighteen-centimeter transparent weather-control core, an elongated cylinder with softly rounded ends, three evenly spaced vertical silver ribs, one dark base and one small side test valve. Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. Exactly two arms and two legs. Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. Adjacent to the flower stall, a food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. At the far left, a dock holds one small orange commuter skiff. At the upper right, a copper weather tower is reached by blue service pipes and exterior iron stairs, and a huge transparent blue water reservoir curves above the district. The market is dry, Mara stays at her stall and the core is in the right hand.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-3 s: Mara delivers the first assigned line from behind Kett; keep Mara's face soft and do not animate a second detailed mouth. 3-7 s: Kett glances once toward the left-hand skiff, answers the short reply, then turns shoulders toward the right-hand tower. 7-10 s: A restrained camera push ends on Kett's resolved expression. One continuous shot. The poncho stays fastened, the core stays in the right hand, and Mara stays at her stall.

Dialogue performance, in this exact order:
1. MARA: "Your ship's leaving." Voice: Warm adult contralto, dry humor, confident calm, not a narrator.
2. KETT: "Let it. I'm changing the weather." Voice: Alert adult voice, light and slightly rough, quick wit without a cartoon squeak.
```

## C07 — Çözümün kurulması

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C07.png · referans (yükleme sırası, kare üretiminde): ref/3.MARA_v1.png · ref/6.PAZAR_v1.png
```

> Not: Plan metni aynen. Replik R07 Mara 1,0-6,0 s (5,0 s; replik ilk iki vuruşa bölünmesin diye ilk vuruş 0-7 s). Pirinç kol C14'te devreye girer: bu klipte kol hareket etmez, tente katlı kalır (plan). Kett kadrajda yok. Birleştirme #6: R06 yemek tezgâhı cümlesi "A food stall has …" (çiçek tezgâhı kadrajda yok). Kolun tarafı C07 kare onayında seçilip FILM §3'e yazılır (F7 notu).

### Görsel
```text
Reference 3 (Mara): take Mara's coral-red head with four eyes, indigo work clothes and cream apron from it. Reference 6 (market): take the food stall with its folded reinforced blue awning, tension cables and brass lever, and the blue service pipes, from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Medium close portrait of Mara, coral-red alien cook with four fixed eyes in a two-by-two arrangement and a narrow vertical mouth, cream apron over indigo work clothes. Mara points upward along a thick blue service pipe behind the food stall. A brass manual awning lever is clearly visible beside Mara's hip. The reinforced blue awning remains folded above the stall. No Kett in frame.

The camera is a medium close view of Mara, with the thick blue service pipe behind her and the brass awning lever in front, beside her hip. Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. Exactly two arms and two legs. Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. A food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. The folded blue awning with its tension cables hangs above the stall behind Mara, and the dry copper market lies beyond the stall, out of focus. The brass lever has not been moved and the awning is still folded, while Mara points along the pipe.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-7 s: Mara points once along the blue service pipe and speaks the assigned instruction clearly. Keep all four eyes fixed in their original arrangement. 7-10 s: End with the brass awning lever still visible. The lever does not move yet and the awning stays folded. No extra dialogue. The pipe, the stall and Mara's indigo work clothes with the cream apron stay in place.

Dialogue performance, in this exact order:
1. MARA: "Core in. Turn the blue wheel. Once it starts, nobody can stop it." Voice: Warm adult contralto, dry humor, confident calm, not a narrator.
```

## C08 — Kuru mizah

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C08.png · referans (yükleme sırası, kare üretiminde): ref/3.MARA_v1.png · ref/4.VORR_v1.png · ref/6.PAZAR_v1.png
```

> Not: Plan metni aynen. İki replik: R08 Vorr 1,0-2,5 s (ilk vuruş) · R09 Mara 3,3-6,3 s (ikinci vuruş; kadraj dışı ya da yumuşak arka plan, ağız oynamaz, plan). Plan "Do not generate simultaneous speaking mouths" korundu. Fiziksel saldırı yok. Birleştirme #6: anahtar cümlesinde "folded blue awning" (plan cümlesindeki "canopy" aynen kaldı), R06 yemek tezgâhı "A food stall has …"; #7: Video'ya plan cümlelerinden sonra ayrı "The blue service route rises toward the tower at screen right."

### Görsel
```text
Reference 3 (Mara): take Mara's coral-red head with four eyes, indigo work clothes and cream apron from it, kept softly out of focus. Reference 4 (Vorr): take Vorr's basalt face, copper shoulder armor and dark brown uniform from it. Reference 6 (market): take Mara's food stall with its brass lever and folded blue awning from it. Horizontal 16:9 cinematic photorealism, practical creature effects and tactile alien architecture, warm late-afternoon copper and mustard palette with cobalt-blue accents, one pale ringed planet, entirely nonhuman cast, realistic consistent downward gravity, restrained lens bloom, clear silhouettes, no written text, no logos, no collage, no extra main character. Vorr's basalt face and copper shoulder armor dominate a close foreground composition at Mara's food stall. Mara remains a smaller softly focused coral-red shape behind the counter. Brass awning lever and folded blue canopy remain in their established places. Vorr looks impatient, not monstrous. No visible weapon. Kett is off-screen.

The camera keeps Vorr sharp in the foreground and Mara soft behind the counter. Vorr, an adult alien weather-company security officer, two hundred thirty centimeters tall, broad heavy basalt-dark body, block-shaped nonhuman face with mineral skin plates, two narrow pale-gold eyes and one small horizontal mouth. Exactly two arms and two legs, five thick fingers per hand. Wears a dark brown practical uniform with rigid copper shoulder armor and heavy metal boots; no helmet, no cloak, no handheld weapon and no holster. Both of Vorr's hands are empty. Mara, an adult nonhuman street cook, one hundred seventy-five centimeters tall, coral-red skin with a subtly ridged head, four small dark eyes permanently arranged in a two-by-two square, one narrow vertical mouth below the eyes, a short rigid fan-shaped crest, no hair, no human ears. Exactly two arms and two legs. Indigo work clothes beneath a worn cream cook's apron, practical cloth belt, empty hands. A food stall has a folded reinforced blue delivery awning, tension cables and a brass lever. Behind Mara the food stall and the dry copper market continue out of focus. Vorr is unarmed, Mara stays at her stall, and the market is dry.
```

### Video
```text
Use the supplied still as the exact starting composition. Ten-second single continuous shot, no internal cuts, no new location. Preserve face geometry, eye count, limb count, costume state, prop placement, light direction and camera side. One principal physical action and one restrained camera move at most. The spoken lines below are performance cues; final clean dialogue can be recorded separately. No built-in captions, subtitles, music or end card.

0-3 s: Keep the camera on Vorr asking the first line. 3-7 s: Hold on his unimpressed reaction while Mara's reply is heard from off-screen or the soft background. Do not generate simultaneous speaking mouths. 7-10 s: Vorr then directs his gaze up toward the blue service route. No physical attack. The blue service route rises toward the tower at screen right. Vorr stays unarmed and Mara stays behind her counter.

Dialogue performance, in this exact order:
1. VORR: "Where is he?" Voice: Deep restrained adult bass, slow authority, no monster growls.
2. MARA: "Buying an umbrella. You should try it." Voice: Warm adult contralto, dry humor, confident calm, not a narrator.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **AÇIK** (SK2: model sesi kullanılmaz, replik kurguda ayrı kayıt; sahip seçimi) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre (birleştirme #9):** "Model" sütunu sahibin kullandığı araçtır (plan: kare GPT Image → image-to-video). Videolarda "Gemini Omni / Flow, süre ölçülecek": 10 s kare-video Veo'da yok (FLOW_GERCEKLERI §1). **C01 pilotunun İLK işi gerçek klip süresini ölçmektir** (`ffprobe`, SMOKE P14). <10 s çıkarsa video vuruşları ölçeklenir (örn. C07 `0-7 s / 7-10 s` → `0-5.5 s / 5.5-8 s`), §5 saniyeleri kayar ve Fable'a dönülür; ölçüm yapılmadan C02-C08 videosu üretilmez.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız referans sayfası ve kare üretiminde, kare promptunun kendi sırasıyla yüklenir.
> **Sıra (plan §10):** 1-9 referans sayfaları (önce 1, sonra 1'in üzerinden 2) → **C01 kare + video (plan pilotu: çekirdek tutuşu; önce süre ölçümü)** → G03'te C21 ve C23 pilotları → **dur: Fable + devamlilik kare kararı** → C02-C03 (açılış) → C04-C08. Referanslar onaylanmadan kare, kare onaylanmadan video üretilmez.
> **Kare kapısı (ILK_30 §6 + G01):** filigran/logo · istenmeyen yazı (fiyat, tabela) · el-nesne kaynaşması (C01 C04 C05 çekirdek) · **C05 valf teması: başparmak dışında parmak yok, parmak sayısı üç** · parmak/göz sayısı (Kett 3 parmak, Mara 4 göz 2×2) · ikinci çekirdek/saksı/fincan · kimlik kayması · C07 pirinç kol kadrajda ve tente katlı · C03 kamusal pazar kuru, yağmur yalnız cam serada.
> **F7 notları (birleştirme):** 6.PAZAR'da pirinç kol ve çiçek okunmuyorsa sayfa v2 (tezgâh detay paneli; çok panelli sayfada C05 ve C07 anahtarına panel adı); kolun tarafı C07 kare onayında seçilip FILM §3'e yazılır · 3.MARA üretilince parmak sayısı kimlik cümlesine eklenir · her denemede altyazı/etiket yazısı ve dudak açık/kapalı kalıbı not edilir (F8 kayıt zamanlaması).
> **Ses:** model sesi yok; replikler kurguda ayrı kayıt (HUMAN, dört ses kimliği, plan §7 "Voice"): C01 R01 · C02 R02 · C04 R03 · C05 R04 · C06 R05 R06 · C07 R07 · C08 R08 R09.

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi | Model |
|:--:|:--:|---|---|---|:--:|:--:|---|
| 1 | 1.KETT | `ref/1.KETT_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 2 | 2.KETT_TULUM | `ref/2.KETT_TULUM_v1.png` | Görsel (düzenleme) | ref/1.KETT_v1.png (R01 üzerinden düzenleme) | 2 | | GPT Image (plan) / Flow Görsel |
| 3 | 3.MARA | `ref/3.MARA_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 4 | 4.VORR | `ref/4.VORR_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 5 | 5.TULA | `ref/5.TULA_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 6 | 6.PAZAR | `ref/6.PAZAR_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 7 | 7.CATILAR | `ref/7.CATILAR_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 8 | 8.HAVA_TACI | `ref/8.HAVA_TACI_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 9 | 9.CEKIRDEK | `ref/9.CEKIRDEK_v1.png` | Görsel | — (yalnız prompt) | 2 | | GPT Image (plan) / Flow Görsel |
| 10 | C01 kare | `kare/C01.png` | Görsel | ref/1.KETT_v1.png · ref/6.PAZAR_v1.png · ref/9.CEKIRDEK_v1.png (bu sırayla) · **AÇILIŞ + plan pilotu** | 2 | | GPT Image (plan) / Flow Görsel |
| 11 | C01 | `ham/C01_d1.mp4` | Frames to Video | kare/C01.png · **plan pilotu: önce gerçek klip süresi (`ffprobe`, P14), sonra çekirdek tutuşu** | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 12 | C02 kare | `kare/C02.png` | Görsel | ref/4.VORR_v1.png · ref/6.PAZAR_v1.png (bu sırayla) · **AÇILIŞ** (pilot kararından sonra) | 2 | | GPT Image (plan) / Flow Görsel |
| 13 | C03 kare | `kare/C03.png` | Görsel | ref/1.KETT_v1.png · ref/6.PAZAR_v1.png (bu sırayla) · **AÇILIŞ** | 2 | | GPT Image (plan) / Flow Görsel |
| 14 | C02 | `ham/C02_d1.mp4` | Frames to Video | kare/C02.png · **AÇILIŞ** | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 15 | C03 | `ham/C03_d1.mp4` | Frames to Video | kare/C03.png · **AÇILIŞ** | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 16 | C04 kare | `kare/C04.png` | Görsel | ref/1.KETT_v1.png · ref/5.TULA_v1.png · ref/6.PAZAR_v1.png (bu sırayla) | 2 | | GPT Image (plan) / Flow Görsel |
| 17 | C05 kare | `kare/C05.png` | Görsel | ref/1.KETT_v1.png · ref/5.TULA_v1.png · ref/9.CEKIRDEK_v1.png (bu sırayla) | 2 | | GPT Image (plan) / Flow Görsel |
| 18 | C06 kare | `kare/C06.png` | Görsel | ref/1.KETT_v1.png · ref/3.MARA_v1.png · ref/6.PAZAR_v1.png (bu sırayla) | 2 | | GPT Image (plan) / Flow Görsel |
| 19 | C07 kare | `kare/C07.png` | Görsel | ref/3.MARA_v1.png · ref/6.PAZAR_v1.png (bu sırayla) | 2 | | GPT Image (plan) / Flow Görsel |
| 20 | C08 kare | `kare/C08.png` | Görsel | ref/3.MARA_v1.png · ref/4.VORR_v1.png · ref/6.PAZAR_v1.png (bu sırayla) | 2 | | GPT Image (plan) / Flow Görsel |
| 21 | C04 | `ham/C04_d1.mp4` | Frames to Video | kare/C04.png | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 22 | C05 | `ham/C05_d1.mp4` | Frames to Video | kare/C05.png | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 23 | C06 | `ham/C06_d1.mp4` | Frames to Video | kare/C06.png | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 24 | C07 | `ham/C07_d1.mp4` | Frames to Video | kare/C07.png | 2 | | Gemini Omni / Flow, süre ölçülecek |
| 25 | C08 | `ham/C08_d1.mp4` | Frames to Video | kare/C08.png | 2 | | Gemini Omni / Flow, süre ölçülecek |

## 8 SORU (16.10.2026 · goruntu-yonetmeni teslimden önce · tur 1 + Fable sadakat revizyonu + F5 birleştirme)

> **Q1 (kolda/göğüste işaret):** Kett'in tek işareti beyaz oval toka; "one white oval breakaway neck clasp … at the center front of the neck … the only marking on the poncho" C01 C04 C06'da yazılı (merkez → taraf yok; DERS Y1 tetiklenmez). C03'te Kett küçük figür (toka cümlesi yazılmadı, giysi cümlesi tokayı taşır). C05 makro (yalnız eller), C02 C07 C08'de işaret yok. Mara/Vorr/Tula'nın işareti yok (plan).
> **Q3 (tüm çekimler):** ORTAK GÖRÜNÜM "warm late-afternoon … palette" ve "one pale ringed planet" taşıyor → `KAPSAM DIŞI: ORTAK GÖRÜNÜM Y6` (dosya başı, öneri sürümüyle; birleştirme P5 plan korundu). Çekimle çelişen su/gezegen/ses yok (M1 aynı akşamüstü, aynı gezegen); makro C05 ve yakın C07'de gezegen kadraja basılabilir (kare kapısında bakılır). Fable kararına göre ORTAK GÖRÜNÜM Video promptlarına eklenmedi (plan: yalnız Görsel'in başına; Video'nun başına ORTAK HAREKET).
> **Q5 (akışkan kelimeleri):** `plume · smoke · steam · drip · wet · bubbles` yok. `rain` (DERS Y5) yalnız film konusu: C02 Video (Vorr'un repliği), C03 Görsel (plan "interior rain", sera içi; kamusal alan kuru) — atmosferli açık hava, vakum yok; "drop" (C05) planın tek damlası, katı hâl: tek damla, tek yaprak. C04 "The spout releases no water." plan cümlesi (P9).
> **Q6 (ekran/gösterge/yazı) — düzeltildi (TD1 B14):** ekran ya da gösterge adıyla yazılmadı; ancak C04 Görsel "No written prices in the image." ve "dry coin-operated … spout" plan cümleleridir (fiyat/sayaç çağrışımı riski; birleştirme P9: plan korundu), R08 referans promptunda "no electronic screen or readable writing" plan metnidir (P8). Yazı kilidi ORTAK GÖRÜNÜM "no written text, no logos".
> **Q7 (Reference yalnız sayfada görüneni ister):** 1 yüz/ponço/toka/eller · 3 başlık, dört göz, giysi · 4 yüz, uniforma, omuz zırhı · 5 başlık, cüppe, fincan (C05'te sayfadan hiçbir şey istenmez, yalnız "çiçek Tula'nın tezgâhına ait") · 6 çeşme, tezgâhlar, iskele, kule, borular · 9 silindir, kaburgalar, taban, valf. Sayfada olmayan (saksı, çatlak seramik, çiçek, damla) metinle tarif edildi.
> **Q8 (ses) — düzeltildi (TD1 B9):** her Dialogue bloğundaki `Voice:` satırları (C01 C02 C04 C06 C07 C08) ve C08 "is heard" ses tarifidir; model sesi kapalı filmde yalnız ağız ipucu (ORTAK HAREKET "performance cues"; plan "Dialogue performance" bloğu aynen, P7). C03 Video "Atmospheric crowd audio only; no dialogue, no subtitles." plan cümlesi (DERS Y13 uyarısı olası; P6): sessiz dönüş + audio zıt istek C03'te vardır, plan korundu.
> **Uzunluk — GERÇEK karakter sayıları (elle sayıldı, ±20; hedef Görsel 2.000-3.200 · Video 1.000-1.500 · tavan 4.300):** Görsel iki paragrafın toplamı (anahtarlar + ORTAK GÖRÜNÜM 363 + plan + ek, aradaki boş satır dahil); Video ORTAK HAREKET (455; repliksiz 360) + vuruşlar + Dialogue bloğu dahil. Sayılar birleştirme sonrası son hâldir.

| Çekim | Düzeltilen sorular (1-8) | Görsel kr · Video kr | Bilerek bırakılan + gerekçe |
|:--:|---|:--:|---|
| C01 | 1 (toka işareti sayı + konum + `the only marking`) · 2 (Kett yüz/eller/giysi/ayaklar + çekirdek gövde/bulut/taban birebir) · 4 (Kett'in arkası: pazar tezgâhları, çeşme) | 2.461 · 1.092 | M: "first frame" → "The frame"; Q8: "says … line" ve "breathless dry amusement" plan ağız ipucu (§5 Kaynak ağız kadrajda); birleştirme #3: vuruş 0-6 / 6-10 s, not R01 2,2-5,7 s; kamera "very low and close" plan (P10: pilot bozulursa orta-geniş) |
| C02 | 2 (Vorr yüz/kollar/giysi birebir; "both hands empty" olumlu karşılık) · 4 (Vorr'un arkası: kuru pazar koridoru, iki bulanık siluet) | 1.730 · 984 | Birleştirme #1: sekiz-siluet ve "açılmış koridor" ekleri kalktı → Görsel hedefin altında (yeni cümle eklenmedi); Vorr giysi cümlesindeki "no helmet, no cloak, no handheld weapon and no holster", "Vorr has no handheld weapon.", "No cutaway and no weapon appears.", "plants one heavy foot" plan (P9); Q5: `rain` Vorr'un repliğinde |
| C03 | 2 (Kett yüz/giysi/çekirdek + R06 cümleleri birebir) · 4 (ufuk/gök: halkalı gezegen; kule, rezervuar, sera, iskele) · birleştirme #5 ("orange commuter skiff") | 2.894 · 832 | Q5: `interior rain` plan; R06 "no humans" yazılmadı (INSANSIZ ↔ zamir); Kett küçük figür olduğundan eller/ayak cümlesi yazılmadı; Q8: "audio" plan cümlesi (Y13 uyarısı olası, P6); Video hedefin altında (repliksiz: 360 ORTAK HAREKET + plan) |
| C04 | 1 · 2 (Tula 3 parça + Kett + çekirdek birebir; fincan "one plain small copper cup … both hands") · 4 (iki kişinin arkası: kuru pazar tezgâhları, odak dışı) · birleştirme #8 (Kett'in tarafı ve yönü) | 2.867 · 941 | Plan "empty cup" ile R05 "Holds one plain small copper cup" birleşti (çelişmez); "No written prices" ve "The spout releases no water." plan (P9) |
| C05 | 2 (Kett makro eller + "thumb is one of the three" + çekirdek 3 parça birebir) · 4 (damlanın arkası: odak dışı kuru tezgâh yüzeyi) · 7 (ref 5 yalnız "çiçek Tula'nın tezgâhına ait") · 8 (kadraj dışı "speaks the assigned line" → "face stays out of frame … quiet regret"; Dialogue bloğu çıktı) | 1.935 · 794 | M: "from the previous shot" silindi; Görsel "suspended drop" ↔ Video "Release … drop" plan içi çelişki (P1, SK3); "storm core / capsule" adları plan (P9); DERS Y2 olası (ref 5 için kimlik cümlesi yok, çünkü Tula kadrajda değil: kadrajda olmayan tarif edilmez); Video hedefin altında (plan 230 kr + ORTAK HAREKET) |
| C06 | 1 · 2 (Kett 5 parça + çekirdek + Mara 3 parça birebir) · 4 (Kett'in arkası Mara ve tezgâh; kule/iskele plan Kamera) · birleştirme #2 (vuruşlar 0-3 / 3-7 / 7-10 s) | 2.917 · 1.176 | İki replik tek blokta (R05 Mara, R06 Kett); Görsel "gaze turns toward the tower" plan, Video önce gemiye bakış (P2, SK4); Mara "face soft" plan cümlesi; FILM §5 R06 saniyesi 4,5'e Fable'da |
| C07 | 2 (Mara 3 parça birebir; yemek tezgâhı "A food stall has …" satırı) · 4 (Mara'nın arkası: mavi boru, tente) | 1.894 · 1.021 | Q2: pirinç kolun ölçü ve tarafı plan/R06'da yok → uydurulmadı ("brass lever", "beside Mara's hip"; F7 notu: kare onayında seçilir); "No extra dialogue" plan cümlesi (replikli çekimde serbest); ilk vuruş 0-7 s (replik 1,0-6,0 s); "No Kett in frame." plan (P9) |
| C08 | 2 (Vorr 3 parça + Mara 3 parça birebir; "both hands empty"; "A food stall has …") · 4 (Mara'nın arkası: tezgâh + kuru pazar) · 8 (yanıt sırasında Mara ağzı oynamaz: plan "Do not generate simultaneous speaking mouths") · birleştirme #6 (anahtar "folded blue awning") · #7 (bakış hedefi: "The blue service route rises toward the tower at screen right.") | 2.226 · 1.131 | Vorr giysi cümlesindeki olumsuz blok ve "No visible weapon.", "not monstrous" plan (P9); plan Görsel cümlesindeki "folded blue canopy … established places" aynen kaldı; "No physical attack" plan |
| Revizyon (Fable sadakat) | C01 "Stay in this one continuous shot." tek cümle · C02 "No cutaway and no weapon appears." · C03 virgüllü "skiff … tower" aynen, "dry" ayrı, "audio" cümlesi geri · C04 "The spout releases no water." ayrı · C05 "Maintain macro framing." + ref 5 geri · C06 "Kett glances …" tek cümle, "One continuous shot." ayrı | önceki satırların sayımı | Plan cümlesine "while/and/as" ile eklenen yok; ek cümleler plan cümlesinin SONRASINDA ayrı cümledir |
| F5 birleştirme (10 madde) | #1 C02 · #2 C06 · #3 C01 · #4 C05 · #5 C03 · #6 C07 C08 · #7 C08 · #8 C04 · #9 iş emri "Model" sütunu + C01 süre ölçümü · #10 Q6/Q8 düzeltmesi | yukarıdaki satırlar son hâl | Yeni plan cümlesi dokunulmadı; kapsam dışı kalanlar "F5 TUR 1 CEVAPLARI"nda |

## F5 TUR 1 CEVAPLARI (birleştirme: `ODA/F5_fable_birlestirme_1.md` · RED gerekçesi = P1-P10 satırı)

Kural: plan cümleleri karakteri karakterine aynen; ekler ayrı cümle. FILM §5 R06 saniyesini (3,3 → 4,5) Fable değiştirir.

### TD1 — `ODA/F5_teknik-danisman_1_G01.md` (Ö0 · C9 · K6)

| Bulgu | Cevap | Gerekçe / uygulama |
|:--:|:--:|---|
| B1 C05 iki damla | RED (plan) | P1: plan Görsel "A single suspended drop hangs …" ↔ Video "Release exactly one small drop …" plan içi çelişki → SK3. Plan cümleleri aynen. |
| B2 C05 başparmak + üç parmak | KABUL | #4: kimlik cümlesinden sonra ayrı "One of the three fingers on each hand is the thumb."; kare kapısına "valf teması: başparmak dışında parmak yok" eklendi. Valfi kadraj dışına alma önerisi planı değiştirir, uygulanmadı. |
| B3 Ref 6 detay yetersiz | KABUL (F7 notu) | 6.PAZAR'da kol/çiçek okunmuyorsa v2 detay paneli; kolun tarafı C07 kare onayında seçilip FILM §3'e; iş emri F7 notlarında. |
| B4 C05 Ref 5 kadraj dışı | KABUL (kısmen) | #4: anahtar cümlesi "Reference 5 (Tula): the pale flower belongs to Tula's flower stall." (Tula/fincan anılmıyor). Ref 5 plan listesi (R01·R05·R09) olarak kaldı; kare/C04 yükleme önerisi uygulanmadı. |
| B5 Açılış üç risk | RED (plan) | P10: C01 "very low and close" plan; pilot bozulursa ikinci denemede orta-geniş kamera (sahibe). C02 kısmı B6 ile KABUL. C03 değişmedi. |
| B6 C02 sayı çelişkisi | KABUL | #1: "Eight different … silhouettes …" → "Two blurred nonhuman silhouettes of different species part behind Vorr."; "Vorr stands in the open corridor …" → "Both of Vorr's hands are empty." |
| B7 C06 vuruş yükü | KABUL (vuruşlar) | #2: 0-3 / 3-7 / 7-10 s, kamera itmesi 7-10 s'te; R06 saniyesi 4,5 (Fable). RED (plan): Mara plan cümlesinin değiştirilmesi — plan cümlesi aynen (birleştirme kuralı: plan cümlesi değişmez). |
| B8 İş emri model adı | KABUL | #9: "Model" sütunu; C01 pilotunun ilk işi `ffprobe` ile süre ölçümü (SMOKE P14); <10 s ise vuruşlar ölçeklenir, Fable'a dönülür. |
| B9 Replik etiketi büyük harf | RED (plan) | P7: plan `1. KETT: "…" Voice: …` bloğu aynen. Q8 düzeltildi (#10). F7: denemede altyazı/etiket yazısı not edilir. |
| B10 C01 replik saniyesi | KABUL | #3: vuruş 0-6 / 6-10 s; not "R01 2,2-5,7 s". |
| B11 Olmayan şeyi ad vererek yazma | RED (plan) | P9: "Vorr has no handheld weapon." · "No cutaway and no weapon appears." · "not monstrous" · "No Kett in frame." · "no guard face" hepsi plan cümlesi; R04 kimlik cümlesi plan. |
| B12 Referans promptlarında jeton | RED (plan) | P8: R02 "R01", R08 "no electronic screen or readable writing … no black hole", R01 "no weather capsule" plan R metni. |
| B13 Y6 gezegen ve palet | RED (plan) | P5: ORTAK GÖRÜNÜM plan §6 birebir; öneri dosya başında → SK7. |
| B14 C03 ses cümlesi · C04 prices | RED (plan) | P6 (C03 "Atmospheric crowd audio only …") · P9 (C04 "No written prices"). Q6 düzeltildi (#10). |
| B15 Mara parmak sayısı · C07 replik 5,0 s | KABUL (F7 notu) | 3.MARA üretilince parmak sayısı kimlik cümlesine eklenir. RED (plan): C07 replik süresini kısaltma/bölme — replik metni plan, sahip kararı. |

### DV1 — `ODA/F5_devamlilik_1_G01.md` (Ö0 · C9 · K13)

| Bulgu | Cevap | Gerekçe / uygulama |
|:--:|:--:|---|
| B1 C05 damla | RED (plan) | P1 (SK3). |
| B2 C06 bakış | RED (plan) | P2: plan Görsel "Kett's gaze turns toward the tower." aynen (SK4). Vuruşları bölme önerisi #2 ile zaten uygulandı (3-7 / 7-10 s). |
| B3 C03 audio | RED (plan) | P6: "Atmospheric crowd audio only; no dialogue, no subtitles." plan cümlesi (SK8). Q8 düzeltmesi #10. |
| B4 C05 Reference 5 | KABUL (kısmen) | #4: Tula ve fincanı anan kısım silindi; ref 6'ya geçiş ve EKLE değişikliği RED (plan): ref listesi R01·R05·R09 plan. |
| B5 C05 parmak/başparmak | KABUL | #4: ayrı cümle "One of the three fingers on each hand is the thumb." (kimlik cümlesi / FILM §3 satırı değişmedi). |
| B6 C05 kolun girişi | RED | Birleştirme KABUL listesinde yok (yeni bilgi: kolun kadraja giriş kenarı plan ve R istemlerinde yazılı değil); P-satırı yok, Fable'a not. F7 kare kapısında el–çekirdek bağlantısına bakılır. |
| B7 C02 sayı çelişkisi | KABUL | #1. |
| B8 C04 Kett yönü | KABUL | #8: "Kett, arriving from screen left, stands at Tula's left and faces screen right." (ek paragraf). |
| B9 C07/C08 kol tarafı · "established places" | KABUL (F7 notu) · RED (plan) | Kolun tarafı C07 kare onayında seçilip FILM §3'e (F7 notu). C08 plan Görsel "remain in their established places" aynen (P9 "atıf" ailesi, plan korundu). |
| B10 M1 ışık yönü | RED (plan) | P5: ışık yönü cümlesi plan dışı yeni cümle; SK7. |
| B11 ORTAK GÖRÜNÜM yakın planda gezegen | RED (plan) | P5. |
| B12 Son vuruşlar · C01 saniye | KABUL (kısmen) · RED (plan) | #3: vuruş 0-6 / 6-10 s ve not 2,2-5,7 s. "Stay in this one continuous shot." plan cümlesi aynen kaldı (ek cümleler ayrı); cümleyi "tracking move slowly eases closer" ile değiştirme önerisi RED (plan cümlesi değişmez; birleştirme kuralı). |
| B13 C02 "plants one heavy foot" | RED (plan) | P9. |
| B14 C03 "escape skiff" | KABUL | #5: ek cümlede "the orange commuter skiff is at the left". |
| B15 C03 sera konumu | RED | Birleştirme KABUL listesinde yok (konum plan ve R06'da yazılı değil; yeni bilgi, konum Fable/sahip kararı); P-satırı yok, Fable'a not. |
| B16 C04 "no water" | RED (plan) | P9: "The spout releases no water." plan cümlesi. |
| B17 C04 "No written prices" | RED (plan) | P9. |
| B18 C05 çekirdeğe üç ad | RED (plan) | P9: "storm core", "capsule" plan Görsel cümleleri aynen. |
| B19 C07/C08 "flower stall" | KABUL | #6: R06 yemek tezgâhı cümlesi "A food stall has …" (KİMLİK tablosuna ek satır). C06'da kaldı. |
| B20 C08 "canopy" | KABUL | #6: anahtar cümlesinde "folded blue awning"; plan Görsel cümlesindeki "folded blue canopy" aynen. |
| B21 C08 bakış hedefi | KABUL | #7: Video'da plan cümlelerinden sonra ayrı "The blue service route rises toward the tower at screen right." Görsel pipe cümlesi eklenmedi (birleştirme yalnız Video). |
| B22 Referans promptları | RED (plan) | P8: R02 "R01", R09 "may rest" plan R metni. |
