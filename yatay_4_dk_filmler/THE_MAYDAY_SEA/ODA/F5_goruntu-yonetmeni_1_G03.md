# 🖼️ THE_MAYDAY_SEA — Prompt grubu G03 (çekimler C17–C24)

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Denetleyecek: devamlilik · teknik-danisman.
> Kaynak: `ODA/SAHIP_PLANI.md` K17-K24 + §8 tutarlılık listesi (sahip talimatı: "bunu bozmadan aynı şekilde hazırla"). Bu dosya yeniden tasarım değil, **biçim çevirisidir**:
> kompozisyon, olay, ışık, tasarım, kamera hareketi ve hareketin yönü planındır; yalnız hat biçimi uygulandı
> (numaralı referans anahtarı · 10 s vuruş planı · olumsuz blok yok · zincir/atıf dili yok · araç/oran/süre etiketi yok · ortak görünüm + mekân ışığı + mekân ortam sesi cümlesi birebir · model sesi replikleri video promptunda).
> Cümle kalıpları `PROMPTLAR/G01.md` ile birebir hizalıdır (kimlik cümlesi, "The light is …", "an unseen calm adult man's voice over the pod's comms says:", alıcı sesi, ortam sesi).
> Prompt gövdesine çekim kodu, referans kodu, "Clip n of N", başlık satırı YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. **Karakterin adı prompta yazılmaz** (`the woman`, `she`; büyük harfli ad kadraja basılır, BILINEN_TUZAKLAR §C). ≤4.300 karakter.
> Kelime güvenliği (BILINEN_TUZAKLAR §A): "body", "dead", milliyet, kan/yara fiilleri hiçbir promptta geçmez (full-length · fuselage · hull yazıldı).
> Kumanda sözcüğü (BILINEN_TUZAKLAR §C / A11): kol her yerde "the broad silver lever with its orange grip" diye bir nesneye bağlı; kök sözcük prompt boyunca tekrarlanmaz.
>
> **Referans dosyaları (`FILM.md` §3):** `ref/1.MARA_v1.png` · `ref/2.KAPSUL_v1.png` · `ref/3.KOKPIT_v1.png` · `ref/4.OKYANUS_v1.png` · `ref/5.ISTASYON_v1.png` · `ref/6.KORIDOR_v1.png` · `ref/9.CANLI_SU_v1.png`.
> Referans sayfalarının promptları G01'dedir (bu grupta yazılmaz).
> **Rol etiketleri (film geneli, G01 ile aynı):** 1 "woman" · 2 "rescue pod" · 3 "cockpit" · 4 "ocean" · 5 "station" · 6 "corridor" · 9 "living water".
> **Panel adları (G01 sayfa tanımlarından; çekimde her referanstan yalnız TEK panel adı):**
> ref 1 → `head-and-shoulders portrait panel` (C18 · C23) · `gloved hands panel` (C20) ·
> ref 2 → `nose close panel` (C19) · `side view panel` (C21) · `rear-above panel` (C22) ·
> ref 3 → `wide interior panel` (C18) · `lever upright panel` (C20) · `receiver switch-on panel` (C23) ·
> ref 4 → `wide exterior panel` (C22) · `living network panel` (C24) ·
> ref 5 → `closed-clamp close panel` (C19 · C21) ·
> ref 6 → `reverse low panel` (C17) ·
> ref 9 → `floor-run panel` (C17) · `ring-wrap panel` (C19 · C21) · `membrane panel` (C24). Panel üstünde yazı/etiket yok.
> **Kimlik cümlesi (çekimlerde birebir, G01 ile aynı; yüz ve yaş/ten/saç yığını referanstan gelir):**
> "an adult woman in an ivory-white pressure suit with graphite joint seals and dark navy shoulder armor, narrow burnt-orange forearm bands, [a single circular gold-and-blue mission badge with an abstract triangle on her left chest — yalnız göğüs kadrajdaysa,] and white gloves, and a round ivory helmet with a completely clear closed visor".
> **Ortak sabitler (FILM.md §3, birebir):**
> ORTAK GÖRÜNÜM (her görsel ve video promptunun sonu): "Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail."
> MEKÂN IŞIĞI (görsel promptlarda, "The light is …" kalıbıyla): DIŞ UZAY (C19 · C21 · C22 · C24) "cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary" ·
> KOKPİT (C18 · C20 · C23) "cool blue water reflections from the canopy at frame-left, very faint amber console glow from below" ·
> İSTASYON İÇİ (C17) "faint amber emergency lamps from above, cool cyan light from the wet floor and the window".
> ORTAM SESİ (video promptlarında, vuruşlardan sonra): DIŞ UZAY "The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static." ·
> KOKPİT "The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet." ·
> İSTASYON İÇİ "The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips."
> **Replik biçimi (model sesi, `FILM.md` §5):** iki nokta biçimi (`… says: <line>`), G01 ile aynı; neden: Vertex rehberi tırnağın ekrana yazı bastırabildiğini söylüyor (BILINEN_TUZAKLAR §C), iki biçim de `film_dogrula` için geçerli, SMOKE P9 karar verir. Replik, kendi vuruşunun SONUNDA durur (sonraki cümle konuşmanın devamı sanılmasın); ilk ve son 1 s'ye düşmez.
> **EKLE satırı** tek satır, iki parça: KARE (Görsel adımı: referanslar yükleme sırasıyla) ve VİDEO (Frames to Video adımına yalnız kare girer; referans eklenirse mod Ingredients'e kayar).
> **Kaynak kare YOK:** planın "önceki görüntüyü kaynak yap" bağımlılıkları (C19←C05 · C21←C19 · C22←C21) kaldırıldı. Gerekçe: G01 C05'te aynı bağımlılığı kaldırdı (THE_PLANET_THIEF C08 dersi); geometri artık referans sayfasının panellerinde (ref 5 `closed-clamp close panel` · ref 9 `ring-wrap panel` · ref 2 `nose close panel`/`side view panel`/`rear-above panel`) ve açı/yükseklik/objektif C05 ile aynı kelimelerle yazıldı. Böylece sekiz kare sıra gözetmeden üretilir ve C21 öncelikli önizleme beklemeden koşulur.
> **Vuruş iskeletleri çekimden çekime farklı** (tempo düzlüğü, PROMPT_HATA_ATLASI karantina): C17 0-3·3-8·8-10 · C18 0-4·4-7·7-10 · C19 0-3·3-7·7-10 · C20 0-2·2-7·7-10 · C21 0-3·3-6·6-10 · C22 0-2·2-6·6-10 · C23 0-2·2-5·5-8·8-10 · C24 0-4·4-8·8-10. Her ilk vuruş hareketle başlar, hiçbir son vuruş donmaz.

---

## C17 — Su şeridi hava kilidine ilerliyor

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/6.KORIDOR_v1.png · ref/9.CANLI_SU_v1.png · VİDEO (Frames to Video): yalnız kare/C17.png
```

> Not: Plan K17. Konuşma yok; kadrajda kimse yok (kokpite dönüş koşusu üretilmez, C18 kesmeyle kokpittedir). Tek şerit, çok uzuv yok: "one continuous piece / one unbroken cord" diye pozitif yazıldı; sel/dalga sözcüğü hiç geçmez.
> **Yön (plan "right floor channel" der, burada aynalandı):** kamera hava kilidine BAKAR (gözlem odası ucundan ters açı). Girişte (R06 hava kilidinden iç yöne) kanal sağda, dolap soldadır; ters açıda ikisi aynalanır → kanal kadrajın SOLUNDA, servis dolabı SAĞ duvarda. G01 ref 6 sayfasının `reverse low panel`'i tam bu düzeni tanımlıyor (su solda, dolap sağda); coğrafya giriş koridoruyla aynı kalır. Planın harfi tercih edilirse "frame-left" ↔ "frame-right" yer değiştirir ve panel adı `airlock entry panel` olur.
> Işık cümlesindeki "the window" gözlem odasından sızan camgöbeği ışıktır (kamera arkasında); koridora pencere çizdirmesin diye sahneye ayrı pencere eklenmedi.

### Görsel
```text
Reference 6 (corridor): take the straight narrow graphite passage, the level grated floor, the waist-high handrails, the water channel along the left floor edge, the open service cabinet on the right wall and the round open airlock at the far end from it, using the reverse low panel. Reference 9 (living water): take the single smooth glossy dark teal ribbon of water lying along a grated floor, its leading end flat and rounded and its cross-section unchanged, from it, using the floor-run panel. Low corridor view on a 24 mm lens, the camera a hand's height above the floor grate and looking back along the passage toward the round airlock opening at the far end, which stands fully open with its rigid hatch recessed to one side. One thick, smooth, glossy dark teal ribbon of water lies in one continuous piece along the shallow floor channel at frame-left, its rounded leading end resting on the middle of the level grate and pointing at the airlock. Waist-high handrails run along both sides, the open service cabinet stands in the wall at frame-right, and the scuffed graphite walls recede toward the airlock. The passage is empty. The light is faint amber emergency lamps from above, cool cyan light from the wet floor and the window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: the camera glides slowly forward at floor level, parallel to the ribbon, as its rounded leading end begins to slide across the grate toward the airlock. 3-8 s: the leading end advances steadily across the grate, the ribbon feeding out of the floor channel behind it as one unbroken cord of constant thickness with all the water travelling inside that single cord, the amber lamp reflections running along its glossy surface. 8-10 s: the leading end slides on toward the airlock threshold, the ribbon still one smooth continuous cord, while the handrails, the cabinet and the airlock frame stay rigid and steady. The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C18 — Kokpitte: acil ayrılma ister

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.MARA_v1.png · ref/3.KOKPIT_v1.png · VİDEO (Frames to Video): yalnız kare/C18.png
```

> Not: Plan K18. Replik R14 (Mara, 4.0 s, 2.0 s, **ağız kadrajda**, ≤5 s): "Emergency separation. Now." — 4-7 s vuruşunun içinde; dudaklar net, vizör şeffaf. Kol BU çekimde çekilmez (C20): kol dik, eller kadrajın hemen altında. Koridor→kokpit kesmede (koşu, kask, kapı yok).
> Kokpit ekran düzeni plandan ve G01 ref 3'ten: kol SOLDA (dik), alıcı SAĞDA; yüzün ve dudağın görünmesi için ¾ önden. Sağ elmacık yarası bu açıda görünür olmayabileceğinden yazılmadı (yüz ref 1 portre panelinden gelir). Rozet göğüs kadrajda olduğu için yazıldı.
> Plan sol/sağ gerilimi: "left shoulder near the lever at frame-left" planın kendi cümlesidir; yüzü kameraya dönükse sol omuz kadrajın sağında olur. F7 kare onayında kolun kadrajın SOLUNDA kalması esas alınır (C20 · C23 aynı düzen).

### Görsel
```text
Reference 1 (woman): take her face, the clear visor, the helmet and the ivory-white pressure suit from it, using the head-and-shoulders portrait panel. Reference 3 (cockpit): take the navy seat, the ivory overhead shell, the graphite canopy mullions, the graphite console with its cyan status lights, the receiver at the right edge, and the broad silver lever with its orange grip, its hinge and its stop at the left edge from it, using the wide interior panel. Medium three-quarter shot on a 50 mm lens inside the cockpit of the rescue pod: an adult woman in an ivory-white pressure suit with graphite joint seals and dark navy shoulder armor, narrow burnt-orange forearm bands, a single circular gold-and-blue mission badge with an abstract triangle on her left chest and white gloves, and a round ivory helmet with a completely clear closed visor, strapped into the navy seat. Her face is plainly visible through the visor in three-quarter view, her grey eyes fixed on the broad silver lever with its orange grip, which stands upright at the left edge of the console at frame-left, beside her left shoulder. The receiver's cyan indicator glows at the right edge of the console at frame-right. Her hands rest just below the lower edge of the frame. Faint water reflections drift across the canopy and the cabin is dry. The light is cool blue water reflections from the canopy at frame-left, very faint amber console glow from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-4 s: a slight, slow push-in begins as the woman braces back against the harness and draws one controlled, urgent breath, her chest rising, her grey eyes fixed on the lever. 4-7 s: the push-in continues, her gaze stays on the lever and her lips shape each word clearly as she says in a short, firm, controlled voice: Emergency separation. Now. 7-10 s: her lips close and her shoulders settle forward, her breathing quick but steady and her eyes still on the lever; her hands stay just below the frame and the lever stays upright. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C19 — Canlı su şeridi yanaşma halkasını tutuyor

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.KAPSUL_v1.png · ref/5.ISTASYON_v1.png · ref/9.CANLI_SU_v1.png · VİDEO (Frames to Video): yalnız kare/C19.png
```

> Not: Plan K19 (C05'in aynı açıdaki karşılığı). Replik R15 (AI, telsiz, kadraj dışı, 4.0 s, 2.5 s): "The docking assembly is under load." — 3-7 s vuruşunun sonunda. Kadrajda kimse yok.
> **Açı eşitliği (kaynak kare yerine metin + panel):** C05 ile aynı kelimelerle: 85 mm, arayüzle aynı yükseklik, yan görünüş, kapsül kadrajın sağında burnu sola, kelepçe istasyon tarafında menteşeli ve yukarıdan, altta dar koyu turkuaz su şeridi ve camgöbeği sınır. C05 karesinde kelepçe AÇIK ve halka ile soket arasında ince boşluk vardır; bu karede kelepçe KAPALI, halka oturmuş, su bir kez dolanmış (iki karenin farkı planın gereği). Objektif/mesafe G01 ile değişirse burada eşitlenir (devamlilik).
> Halka, kelepçe ve ara bağlantılar bükülmez/büyümez (plan §8); su "tek tutarlı ıslak halka". Ref 5 `closed-clamp close panel` kapalı kelepçeyi, ref 9 `ring-wrap panel` dolanmış şeridi taşır.

### Görsel
```text
Reference 2 (rescue pod): take the dark-grey cylindrical docking ring on its four short rigid mounts, the orange nose band and the sealed flat hatch behind the ring from it, using the nose close panel. Reference 5 (station): take the round docking socket, the single broad hinged clamp closed around a plain dark-grey ring, the oxidized graphite hull and the strip of dark teal water from it, using the closed-clamp close panel. Reference 9 (living water): take the smooth glossy dark teal ribbon of water wrapped once around a rigid metal ring, its round cross-section kept, from it, using the ring-wrap panel. Close exterior insert on an 85 mm lens, held level with the docking interface and seen from the side: the rescue pod's dark-grey cylindrical docking ring, on its four short rigid mounts, sits seated against the station's round docking socket, the pod at frame-right with its nose pointing left, and the sealed flat inner hatch is visible behind the ring. The station's single broad rigid hinged clamp, its hinge on the station side, is closed around the ring from above. One coherent, smooth, glossy dark teal ribbon of water rises from the narrow strip of dark teal water below the dry connection and is already wrapped once around the ring in a single wet loop of steady round section. The thin cyan field boundary runs along that strip below the interface, and on the pod side the space is dry and black. The light is cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: the camera stays fixed on the interface as the single ribbon of water begins to tighten around the rigid ring, its wet loop drawing slowly in. 3-7 s: the loop closes tighter in one smooth glossy band and the water gathers a little at its base on the station side, as an unseen calm adult man's voice over the pod's comms says: The docking assembly is under load. 7-10 s: the loop settles tighter and glossier around the ring, a few small droplets shaking loose on the station side, while the ring, the clamp and the four mounts stay rigid and unbent. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C20 — Acil ayrılma kolu çekilir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.MARA_v1.png · ref/3.KOKPIT_v1.png · VİDEO (Frames to Video): yalnız kare/C20.png
```

> Not: Plan K20. Replik yok. **T01: el ilk karede kolu zaten tutuyor** (kavrama + çekme aynı klipte değil); tek hareket kolun tek menteşe çevresinde mekanik durdurucuya kadar dönmesi. Yön FILM.md §4 ve G01 ref 3 `lever pulled panel`'i ile aynı: yukarıdan aşağı ve sola; durdurucu bloğu yayın SOLUNDA yazıldı, ön kol kadrajı ALT kenardan terk eder (tutan kadrajda).
> Eldiven aynı kavramada kalır, yeni parmak/kumanda yok; kol sonunda durdurucuda oturur (donma değil: eldiven kavrayışı hafif gevşer). Konsolda yazı yok: "plain, unmarked shapes". Ref 1 yalnız eldiven için (`gloved hands panel`); manşetteki turuncu bant metinde.

### Görsel
```text
Reference 1 (woman): take the white glove from it, using the gloved hands panel. Reference 3 (cockpit): take the broad silver lever with its orange grip, its fixed hinge and its mechanical stop, and the scuffed graphite console edge with its cyan status lights from it, using the lever upright panel. Tight cockpit insert on a 100 mm lens: the broad silver lever with its orange grip stands upright at the left edge of the graphite console, its single fixed hinge plainly visible at its base and a solid mechanical stop block set to the left of the arc it will swing through. A left white glove is already wrapped around the orange grip, and the ivory sleeve with its narrow burnt-orange forearm band continues naturally out of the frame past the bottom edge. The glove, the grip and the lever sit crisp in the foreground while the console's cyan status lights glow softly behind them and amber reflections lie along the scuffed metal; the console surface carries only plain, unmarked shapes. The light is cool blue water reflections from the canopy at frame-left, very faint amber console glow from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-2 s: the camera stays fixed on the insert as the white-gloved hand tightens around the orange grip and the sleeve below the frame tenses, the lever starting to rock out of its upright rest on its hinge. 2-7 s: the glove pulls the rigid lever in one smooth, firm arc down and toward frame-left around its single hinge, staying wrapped around the same orange grip, while amber reflections slide along the scuffed metal as it moves. 7-10 s: the lever reaches the mechanical stop and settles against it, the glove easing slightly on the grip, the hinge and the stop unchanged. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C21 — Kapsül halkayı istasyonda bırakır ve geri çekilir

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.KAPSUL_v1.png · ref/5.ISTASYON_v1.png · ref/9.CANLI_SU_v1.png · VİDEO (Frames to Video): yalnız kare/C21.png
```

> Not: Plan K21. **ÖNCELİKLİ ÖNİZLEME (plan §8 "önce dört zor plan", 4. plan):** halka istasyonda kalırken kapsül bozulmadan uzaklaşmalı. Replik yok.
> **Boşluk ilk karede VAR** (patlama/dönüşüm yok; video yalnız boşluğu genişletir): kare, ayrılmanın başındaki durağan anı gösterir. Halka, kelepçe ve su halkası istasyon tarafında sabit; kapalı iç kapak ve dört çıplak ara bağlantı kapsülde. Uzayan hortum/dokunaç yok: "the water staying gathered in that loop" pozitif yazıldı.
> Plan kaynak K19 isterdi; kaldırıldı (dosya başı). Orta dış yan plan C04'ün düzenindedir: 50 mm yan, arayüzle aynı yükseklik, kapsül sağda burnu sola, istasyon solda (kapsül sağdan sola yanaşmıştı). Ayrılma hareketi ilk karede başlamış durumda; ref 2 `side view panel` halkalı hâli taşır, boşluk metinde.
> Basit kareye geri dönüş seçeneği (plan §8): video kararsız çıkarsa boşluk daha geniş bir kareden başlanır, hareket eklenmez.

### Görsel
```text
Reference 2 (rescue pod): take the wingless ivory-and-graphite hull, the burnt-orange nose band, the four short rigid mounts, the dark-grey docking ring and the sealed flat inner hatch from it, using the side view panel. Reference 5 (station): take the dry right-hand module with its round docking socket, the single broad hinged clamp closed around a plain dark-grey ring, the oxidized graphite hull and the dark teal water from it, using the closed-clamp close panel. Reference 9 (living water): take the smooth glossy dark teal ribbon of water wrapped once around a rigid metal ring, its round cross-section kept, from it, using the ring-wrap panel. Medium exterior side view on a 50 mm lens, the camera level with the docking interface: at frame-left the station's dry right-hand module with its round docking socket, the oxidized graphite hull, the dark teal water below it and the thin cyan field boundary along its wet edge; at frame-right the wingless rescue pod with its nose still pointing left toward the station and its two vertically stacked blue-white rear thrusters at the far right. The pod's dark-grey docking ring is still seated in the socket and locked in the station's single broad clamp, held by one smooth wet loop of dark teal water, while a narrow new gap has just opened between this ring and the pod's four short rigid mounts, the pod's sealed flat inner hatch plainly visible in the gap. Open black space with sparse stars fills the frame to the right. The light is cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-3 s: the camera stays locked on the side view as the rigid rescue pod begins to slide slowly to the right, away from the station, and the narrow gap between the ring and the pod's four mounts starts to widen. 3-6 s: the pod glides on to the right at a steady pace, the gap growing wider, while the dark ring stays locked in the station's clamp inside its single wet loop of water, the water staying gathered in that loop. 6-10 s: the pod eases further from the station, its sealed flat inner hatch and four bare mounts now clearly separate from the ring, which stays seated in the socket with the clamp and the wet loop in place beside it. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C22 — Kapsül okyanusun alanından çıkar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/2.KAPSUL_v1.png · ref/4.OKYANUS_v1.png · VİDEO (Frames to Video): yalnız kare/C22.png
```

> Not: Plan K22. Replik R16 (AI, telsiz, kadraj dışı, 4.0 s, 2.0 s): "We're clear of the field." — 2-6 s vuruşunun sonunda. Kadrajda kimse yok; alanın ötesinde hiçbir şey izlemez ("the space behind the pod stays clear").
> **Kaynak kare (C22 ← C21) kaldırıldı:** C21 karesinde halka hâlâ takılıdır; bu çekimin tek koşulu halkanın yokluğudur, kaynak kare tersini öğretirdi. Kapsül tasarımı ref 2 `rear-above panel`'inden gelir; halkasız burun (düz kapalı iç kapak + dört çıplak ara bağlantı) G01 sayfasında ayrı `nose after separation panel` olarak var, burada metinle de pozitif yazıldı ("a flat sealed inner hatch set among four short bare mounts").
> Devamlilik: C21'de burun istasyona (sola) bakar ve kapsül sağa geri çekilir; burada burun uçuş yönüne (sağa) bakar (itici parlaması itme yönüyle uyumlu) — kapsül iki çekim arasında dönmüş sayılır (C21→C22 kesme, FILM §6). Camgöbeği sınır kapsülün arkasında. Dış halka dışında gövde, cam, iki motor değişmez (plan §8).

### Görsel
```text
Reference 2 (rescue pod): take the wingless boat-shaped graphite hull with its curved ivory armor panels, the burnt-orange band, the broad dark canopy and the two vertically stacked recessed blue-white rear thrusters from it, using the rear-above panel. Reference 4 (ocean): take the enormous flat oval ocean, its three black rectangular containment frames, the thin cyan field boundary and the small half-submerged graphite station from it, using the wide exterior panel. Wide exterior view on a 35 mm lens, from behind and above the pod and slightly to its side: the rescue pod travels alone through open space, its nose pointing toward frame-right and away from the camera, the two vertically stacked blue-white thrusters facing the camera at its rear and the top of its canopy and hull visible from above. At the far end of the nose sits a flat sealed inner hatch set among four short bare mounts. At frame-left, behind the pod, the enormous flat oval ocean hangs within its three black rectangular frames with the small half-submerged station on its rim, all receding; the thin cyan field boundary lies wholly behind the pod, and ahead of it stretches open black space with sparse stars. The light is cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-2 s: the camera tracks with the pod from behind and above as it accelerates smoothly toward frame-right, the ocean behind it beginning to shrink. 2-6 s: the pod keeps pulling away from the field, its two rear thrusters glowing a little brighter without changing shape and the thin cyan boundary sliding farther behind it, as an unseen calm adult man's voice over the pod's comms says: We're clear of the field. 6-10 s: the distance keeps growing, the ocean with its three frames and its station becoming steadily smaller behind the pod, whose course and shape stay steady, and the space behind the pod stays clear. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C23 — Kendi sesini yeniden duyar, kanalı kapatır

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/1.MARA_v1.png · ref/3.KOKPIT_v1.png · VİDEO (Frames to Video): yalnız kare/C23.png
```

> Not: Plan K23. Replik R17 (OCEAN = Mara'nın sesi, alıcıdan, 2.0 s, 2.0 s): "Rescue vessel. I hear you." — 2-5 s vuruşunda; **kadrajdaki kadın KONUŞMAZ, ağzı kapalı** (T16: model onu konuşturabilir, bu yüzden "mouth stays closed" video promptunda yazıldı ve son iki vuruşta da korundu). Ses anahtar hareketinden ÖNCE biter (anahtar 5-8 s). Omni aynı sesi C02'den taşıyamaz → kurguda C02 kaydı yedek (NOTLAR KARARLAR).
> **Plana göre tek küçük fark (T01 gereği):** plan "eldiven anahtarın YANINDA" der; burada eldiven anahtarın geniş kolunun üstünde BAŞLAR (temas karede kurulu), video yalnız bastırır. Planın §8 kuralıyla aynı yön: "el zaten kolu tutmaktadır". Anahtar yukarıda (açık), gösterge camgöbeği yanık; hareket sonunda anahtar aşağıda, gösterge sönük (G01 ref 3 `receiver switch-on panel` başlangıç durumunu taşır).
> Sol kol çekilmiş konumda kadrajın solunda (C20'nin sonucu: aşağı ve sola, durdurucuda); ref 3'ten tek panel (anahtar) alındığı için kolun görünüşü metinde. Sağ elmacık yarası bu açıda garanti edilemediğinden yazılmadı. Rozet göğüs kadrajda olduğu için yazıldı.

### Görsel
```text
Reference 1 (woman): take her face, the clear visor, the helmet and the ivory-white pressure suit from it, using the head-and-shoulders portrait panel. Reference 3 (cockpit): take the receiver's speaker grille, its broad physical toggle raised in the on position beneath the lit cyan indicator, and the graphite console from it, using the receiver switch-on panel. Medium cockpit shot on a 50 mm lens: an adult woman in an ivory-white pressure suit with graphite joint seals and dark navy shoulder armor, narrow burnt-orange forearm bands, a single circular gold-and-blue mission badge with an abstract triangle on her left chest and white gloves, and a round ivory helmet with a completely clear closed visor, strapped into the navy seat, fills the left half of the frame. Her face is plainly visible through the visor, her lips closed and her eyes lowered toward frame-right. In the right foreground her right white glove already rests on the receiver's broad physical toggle, which stands raised in its on position beneath a glowing cyan indicator, her ivory sleeve entering the frame from the bottom edge at frame-right. At the left edge of the console the broad silver lever with its orange grip lies pulled down against its stop. Through the canopy only distant stars and one small faint blue glow of the distant containment field remain. Her posture is still, the cabin dry, the controls plain and unmarked. The light is cool blue water reflections from the canopy at frame-left, very faint amber console glow from below. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-2 s: the camera stays fixed on the medium shot as the woman draws one slow breath, her chest rising, her mouth closed, and the faint blue glow beyond the canopy drifts a little across the glass. 2-5 s: her mouth stays closed and her eyes lower toward the toggle while the receiver at frame-right plays a calm woman's voice, softened by a light radio filter: Rescue vessel. I hear you. 5-8 s: with one small, deliberate movement her gloved hand presses the broad toggle down into its off position and the cyan indicator above it goes dark. 8-10 s: her breath eases out slowly and her shoulders settle as she looks at the dark indicator, her mouth still closed, the pulled lever and the cabin unchanged. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

## C24 — Okyanus ve geçmiş kurbanlar

```
FLOW      Frames to Video
EKLE      KARE (Görsel): referans (yükleme sırası): ref/4.OKYANUS_v1.png · ref/9.CANLI_SU_v1.png · VİDEO (Frames to Video): yalnız kare/C24.png
```

> Not: Plan K24 (final). Replik R18 (Mara, voice-over, kadraj dışı, 4.0 s, 4.5 s): "It wasn't waiting to be rescued. It was waiting to be answered." — 4-8 s vuruşunun SONUNDA yazıldı, söz yaklaşık 8,5. saniyeye uzanır; son 1,5 s'de yalnız ortam ve ışık atımının sönmesi. Kadrajda kimse yok. VO sesi C01'in VO'suyla aynı tarifle yazıldı ("an unseen woman's voice, close and calm").
> Film adı gerekirse son 2 saniyeye KURGUDA eklenir (promptta yazı yok). Yeni araç/kişi/ikinci tehdit yok: bitiş "the whole uncanny ocean … all in place" diye pozitif yazıldı. Kapsül yok; terk edilmiş halka kuru portta. Düzen C01 ile aynı (okyanus merkezde üçte iki, istasyon sağ kenarda, üç çerçeve, camgöbeği sınır); farklar: çok sayıda eski gemi siluetinin görünür olması, ağın silik görünmesi, kapsülün yokluğu.
> Karışım C23→C24 (FILM.md §6 GEÇİŞ). Ref 4 `living network panel` ağlı geniş dışı, ref 9 `membrane panel` kılcal ağın dokusunu taşır.

### Görsel
```text
Reference 4 (ocean): take the enormous flat oval ocean with its rippled top surface and thick translucent hanging underside, the three black rectangular containment frames, the thin cyan field boundary, the small half-submerged graphite station and the faint network inside the water from it, using the living network panel. Reference 9 (living water): take the branching, fixed network of faint cyan-gold capillary lines from it, using the membrane panel. Final extreme wide exterior view on a 24 mm lens in deep black space with sparse stars: the same flat oval ocean hangs within its three black rectangular frames, filling the central two thirds of the frame, with a thin cyan field boundary around the water. The small half-submerged graphite station sits on its rim at frame-right, the abandoned dark-grey docking ring seated in its dry round port and nothing attached to it. Beneath the rippled top surface, inside the translucent water, lie the silhouettes of many old spacecraft of different sizes and eras at different depths, and the immense network of faint cyan-gold capillary lines is faintly visible throughout the whole volume of water. The light is cold white distant starlight from upper left, deep indigo shadows, faint cyan edge light from the containment boundary. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

### Video
```text
0-4 s: the camera begins a slow pullback and the old hull silhouettes beneath the rippled surface slide into clearer view as the whole oval ocean widens in the frame. 4-8 s: the pullback continues and more of the submerged fleet opens up by parallax while one soft cyan-gold pulse of light travels through the faint network from left to right, as an unseen woman's voice, close and calm, says: It wasn't waiting to be rescued. It was waiting to be answered. 8-10 s: the pulse fades out along the network as the pullback reaches its widest, the whole uncanny ocean in view with its three frames, its station and the abandoned ring all in place. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cold blue-teal shadows, faint amber practical lights, readable blacks, and realistic metal and wet-surface detail.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir, klibin içinde) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini Omni 1.1 Flash 10 s ile hedefler; Flow'da Görsel modu aynı promptla ve aynı referans sırasıyla kullanılabilir. Omni'nin Frames to Video süresi ve repliği videoda üretmesi SMOKE P11 · P14 · P18'de ölçülür (`FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar (sıra 9-16) koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız kare üretiminde. Kaynak kare yok: sekiz kare yalnız referans sayfalarından üretilir, aralarında sıra bağımlılığı yoktur (sıra 1-8 herhangi bir sırayla koşulabilir). Önkoşul: `ref/1.MARA_v1.png` … `ref/9.CANLI_SU_v1.png` onaylanmış olmalı (G01 iş emri sıra 1-9).
> Panel isteği yok: kullanılan bütün paneller G01 sayfa tanımlarında mevcut (`rear-above panel` ve `nose after separation panel` ref 2 sayfasında).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | C17 | `kare/C17.png` | Görsel | ref/6.KORIDOR_v1.png (ters alçak panel) · ref/9.CANLI_SU_v1.png (zemin şeridi paneli; bu sırayla) | 2 | |
| 2 | C18 | `kare/C18.png` | Görsel | ref/1.MARA_v1.png (baş-omuz portre paneli) · ref/3.KOKPIT_v1.png (geniş iç panel; bu sırayla) | 2 | |
| 3 | C19 | `kare/C19.png` | Görsel | ref/2.KAPSUL_v1.png (burun yakın paneli) · ref/5.ISTASYON_v1.png (kapalı kelepçe yakın paneli) · ref/9.CANLI_SU_v1.png (halka dolanma paneli; bu sırayla) | 2 | |
| 4 | C20 | `kare/C20.png` | Görsel | ref/1.MARA_v1.png (eldivenler yakın paneli) · ref/3.KOKPIT_v1.png (kol dik paneli; bu sırayla) | 2 | |
| 5 | C21 | `kare/C21.png` | Görsel | ref/2.KAPSUL_v1.png (yan görünüm paneli) · ref/5.ISTASYON_v1.png (kapalı kelepçe yakın paneli) · ref/9.CANLI_SU_v1.png (halka dolanma paneli; bu sırayla). **Öncelikli önizleme (plan: dört zor plan): C21 önce sınanır** | 2 | |
| 6 | C22 | `kare/C22.png` | Görsel | ref/2.KAPSUL_v1.png (arka-üst panel) · ref/4.OKYANUS_v1.png (geniş dış panel; bu sırayla) | 2 | |
| 7 | C23 | `kare/C23.png` | Görsel | ref/1.MARA_v1.png (baş-omuz portre paneli) · ref/3.KOKPIT_v1.png (alıcı anahtar açık paneli; bu sırayla) | 2 | |
| 8 | C24 | `kare/C24.png` | Görsel | ref/4.OKYANUS_v1.png (canlı ağ paneli) · ref/9.CANLI_SU_v1.png (zar paneli; bu sırayla) | 2 | |
| 9 | C17 | `ham/C17_d1.mp4` | Frames to Video | kare/C17.png | 2 | |
| 10 | C18 | `ham/C18_d1.mp4` | Frames to Video | kare/C18.png (replik R14 ağız kadrajda: dudak senkronu dinlenir) | 2 | |
| 11 | C19 | `ham/C19_d1.mp4` | Frames to Video | kare/C19.png (replik R15 telsiz) | 2 | |
| 12 | C20 | `ham/C20_d1.mp4` | Frames to Video | kare/C20.png | 2 | |
| 13 | C21 | `ham/C21_d1.mp4` | Frames to Video | kare/C21.png. **Öncelikli önizleme: ilk bu video sınanır** | 2 | |
| 14 | C22 | `ham/C22_d1.mp4` | Frames to Video | kare/C22.png (replik R16 telsiz) | 2 | |
| 15 | C23 | `ham/C23_d1.mp4` | Frames to Video | kare/C23.png (replik R17 alıcıdan, kadındaki ağız kapalı; Omni sesi tutmazsa kurguda C02 kaydı yedek) | 2 | |
| 16 | C24 | `ham/C24_d1.mp4` | Frames to Video | kare/C24.png (replik R18 voice-over) | 2 | |

> Sıra: 1-8 kareler (sırası serbest; C21 öncelikli) → ancak sonra videolar. Öncelikli önizleme C21 için en kısa yol: sıra 5 → 13.
> Replik doğrulaması video dinlenirken: R14 (C18 4-7 s) · R15 (C19 3-7 s) · R16 (C22 2-6 s) · R17 (C23 2-5 s, kadının ağzı kapalı, anahtardan önce biter) · R18 (C24 4-8 s). Metin `FILM.md` §5 ile birebir; farklı duyulursa `NOTLAR.md` TARAMA/ANLATIM satırına tek cümleyle.
