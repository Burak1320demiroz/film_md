# 🖼️ THE_FURNACE_GATE — Prompt grubu G01 (çekimler C01–C12)

> Yazan: goruntu-yonetmeni (faz 5, tur 1). Kaynak: `THE_FURNACE_GATE_16MIN_96_CLIPS.md` §10 K01–K12 + §8 R01–R16 (sahip planı, "plana uyarak"). Bu dosya yeniden tasarım değil,
> biçim çevirisidir: kompozisyon, olay, ışık, tasarım ve hareket yönü planın kendisi; cümleler olabildiğince planın İngilizcesi.
> Çıkarılan plan kalıpları (NOTLAR KARARLAR 13.10.2026): olumsuz kapanış ("No readable text… / No new people…"), araç/oran/süre etiketleri, "Animate the uploaded scene still as the first frame",
> "Use the attached reference images only…", "Continuity overrides…" bloğu, "Generate only … sound design / No spoken dialogue…" (bu filmde tersi: replikler model sesi), çekim atfı.
> Prompt gövdesine çekim kodu, referans kodu (R06), başlık satırı, "Clip n of N" YAZILMAZ; bunlar kod bloğunun DIŞINDA durur. Her blok ≤4.300 karakter.
> **Sahip kararı 10.10.2026 (film_dogrula M):** referans dosyası `ref/<No>.<AD>_v1.png`; eklenen her referans görsel promptun başında `Reference <No> (<rol>): …` diye adlandırılır;
> her video promptu 10 s'yi 2-4 vuruşa böler (0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s, son vuruş donmaz). **Özne başına TEK referans sayfası:** açılar ve durumlar panel;
> çekim promptunda her referanstan yalnız TEK panel adı anılır. Panel adları FILM.md §3'ten (değişmez); sayfa üstünde yazı, etiket, ok yok.
> **Sahip kararı 12.10.2026 (kesme sürekliliği · model sesi):** ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunun sonunda birebir; mekân ışığı (FILM §3) görsel promptta birebir;
> mekân ortam sesi (FILM §3) video promptunda birebir; ilk vuruş hareketle başlar. FILM §5 Kaynak = model sesi olan her replik video promptuna birebir yazılır.
> **Replik biçimi: iki nokta** (`… says: <line>`); Vertex rehberi tırnağın ekrana yazı bastırdığını söylüyor, BILINEN_TUZAKLAR §C aynı yönde. SMOKE P9 tırnağı seçerse bu dosyadaki replik cümleleri tırnağa alınır (metin değişmez).
> **Replik vuruşun SON cümlesidir** (betimleme önce, replik sonda). **Ses tarifleri film boyu sabit** (FILM §3 SES KİMLİĞİ): Leon `a low, dry adult man's voice, calm and guarded` · Rhea `a clear, quick adult woman's voice, precise and controlled` ·
> telsiz eki `softened by a light suit-radio filter` (kaynak kadrajda yok: `over the suit radio, …`) · voice-over `Leon's low, dry voice as a calm voice-over`. Konuşan kadrajdaysa ağzı yalnız kendi cümlesinde hareket eder, öteki ağız kapalı yazılır.
> **Kimlik tabanı** (FILM §3 KİMLİK TABANI) kadrajdaki kişi için birebir aynı kelimelerle; arkadan ya da uzaktan görünmeyen parçalar (rozet, askı, yüz izleri, sakal) çıkarılır, kalan kelimeler değişmez.
> Kimlik yığını (yaş + ten + saç + göz + yara) tek kişide üst üste: BILINEN_TUZAKLAR §A son satır (HİPOTEZ, RED 15). Flow "tanınmış kişi" benzeri bir red verirse kimlik yığını söküp yalnız yüzü sayfadan almak (THE_MAYDAY_SEA yolu) ilk denemedir.
> **Dünya cümlesi (T18):** her dış çekimde `Everything hangs in deep black space with sparse stars.` + dış ışık cümlesi birebir; uzayın görünmediği yakın ekte yalnız ışık cümlesi.
> **Kamera sözleşmesi (kokpit/koridor, ekran yönü):** iki kişilik geniş çekimler arkadan (Leon solda, Rhea sağda; konuşanın başı kameraya doğru döner); teklilerde Leon'un bakışı kadrajın sağına, Rhea'nın bakışı kadrajın soluna gider (karşılıklı bakış kesmede korunur).
> Bilek bağlantısı Rhea'nın SAĞ bileğinde, Leon'un bilek birimi SOL bileğinde (1.LEON · 2.RHEA sayfalarında sabit). Kelime güvenliği (BILINEN_TUZAKLAR §A): tarif metinlerinde `body` geçmez (torso · hull · casing · full-length yazıldı);
> yalnız FILM §3'te sabitlenen `… full-body panel` adı panel anahtarlarında kalır (Flow o kelimeyle red verirse tüm gruplarda aynı anda `full-length`'e çevrilir).
> Vuruş iskeletleri çekimden çekime replik anına ve hareketin evresine göre değişir; aynı iskelet en çok iki çekimde.

---

## REFERANS PROMPTLARI (yalnız ilk grupta · özne başına TEK sayfa, sahip kararı 10.10.2026)

> 15 sayfa, plan R01–R16'nın hat biçimi (R03 ikili ana kare KALDIRILDI: iki kişilik çekimler 1.LEON + 2.RHEA ile kurulur). Plan'ın olumsuz kuyruğu ("No readable text, letters, numbers, brand logos or watermark") ve plan adı yazısı çıkarıldı;
> yerine olumlu "plain unmarked surfaces". Sayfaların panel sırası PANELLER satırındaki sıradır (sol→sağ, üst→alt); panel üstünde yazı yok.
> **Üretim sırası (KAYNAK bağımlılığı):** 1 → 2 → 3 → 4 → 6 → 5 → 7 → 8 → 9 → 10 → 11 → 12 → 13 → 14 → 15. Sayfa 4 önce 3'ü, 5 önce 6'yı, 8 önce 7'yi, 12 önce 10'u, 14 önce 9'u ister (KAYNAK satırı).
> Sahip her sayfayı seçip `ref/` altına `<No>.<AD>_v1.png` adıyla kaydeder; yüz/giysi/kıta/kepenk sayısı değiştiren sayfa kullanılmaz, önce o düzeltilir (plan Kullanım).
> Ortak kararlar: ark burnu SAĞDA, kıç SOLDA; kriyo kapakları opak; hiçbir sayfada yolcu yüzü ya da çocuk yok; kapı üç kepenkli; port ve sancak kelepçesi ayrı kollar.

### 1.LEON
```
DOSYA     ref/1.LEON_v1.png
PANELLER  beş panel, bu sırayla: front full-body panel · back full-body panel · side full-body panel (sol yandan) · face close-up panel (¾, sol şakak yarası görünür) · glove panel (tek beyaz eldiven, elin sırtı)
```
```text
A single reference sheet on a plain mid-grey studio background showing exactly the same adult man in five panels, with clear gaps between the panels, in identical soft even light from the front-left, arranged as three panels on the top row and two panels on the bottom row. Top row: full-length from the front; full-length from the back; full-length from his left side. Bottom row: a large head-and-shoulders portrait in three-quarter view from his left front, the small pale scar at his left temple plainly visible through the clear visor; a close view of one white glove with its sleeve cuff and burnt-orange arm band, seen from the back of the hand. He is a 38-year-old pilot with olive skin, short dark brown hair, brown eyes, a short neat beard and a small pale scar at his left temple. He wears an elegant ivory-white pressure suit with graphite chest seams, navy shoulder armor, narrow burnt-orange bands on both upper arms, white gloves, graphite boots and a compact ivory life-support pack on his back, with a round blue-and-gold badge showing an abstract hawk on his left chest, an unmarked ivory wrist-comm unit on his left wrist, and at his belt a compact graphite cutter and a coiled navy safety tether. A closed round ivory helmet with a completely clear visor in every panel that shows his head, so his face is plainly visible. Calm, guarded, competent expression. Identical face, helmet and suit in all panels. Photorealistic, clean panels with plain unmarked surfaces.
```

### 2.RHEA
```
DOSYA     ref/2.RHEA_v1.png
PANELLER  beş panel, bu sırayla: front full-body panel (askı boş) · back full-body panel · side full-body panel (sağ yandan) · face close-up panel (¾, sağ çene yarası görünür) · harness with core panel (çekirdek göğüs askısında kilitli, bel üstü önden)
```
```text
A single reference sheet on a plain mid-grey studio background showing exactly the same adult woman in five panels, with clear gaps between the panels, in identical soft even light from the front-left, arranged as three panels on the top row and two panels on the bottom row. Top row: full-length from the front with the chest harness empty; full-length from the back; full-length from her right side. Bottom row: a large head-and-shoulders portrait in three-quarter view from her right front, the small scar on the right side of her chin plainly visible through the clear visor; a medium view from the front, from the head down to the waist, with one compact power core locked into her chest harness: a rectangular graphite casing with ivory corner guards, one rigid top carry handle and an amber glass center. She is a 34-year-old systems engineer with olive skin, green eyes, dark copper hair in a tight low braid tucked inside her helmet and a small scar on the right side of her chin. She wears an elegant pearl-white pressure suit with graphite joints, navy waist panels, narrow muted-teal bands on both upper arms, white gloves, graphite boots and a compact pearl life-support pack on her back, with a round blue-and-gold badge showing an abstract geometric sun on her left chest and one rigid graphite core-carry harness beneath the badge, empty in the first four panels; at her belt a compact graphite cutter, one small matte-grey fictional EMP puck and a coiled navy safety tether; an unmarked ivory wrist-link on her right wrist. A closed round pearl helmet with a completely clear visor in every panel that shows her head, so her face is plainly visible. Alert, precise, stubborn expression. Identical face, helmet and suit in all panels. Photorealistic, clean panels with plain unmarked surfaces.
```

### 3.KESTREL
```
DOSYA     ref/3.KESTREL_v1.png
PANELLER  dört panel, bu sırayla: side view panel (burun sağda) · three-quarter panel · bow collar open panel (kelepçe açık) · bow collar locked panel (kelepçe kapalı)
```
```text
A single reference sheet showing exactly the same compact salvage tug four times, with clear gaps between the panels, in identical cold white starlight from the upper left with a soft blue fill and a faint warm orange glow from frame-left, against deep black space, arranged as two panels on the top row and two panels on the bottom row. Top row: a full side view level with the tug, its nose pointing to frame-right; the tug in a three-quarter exterior view from its front right. Bottom row: a close side view of the tug's nose showing the round bow docking collar with its flat inner hatch and one broad hinged clamp standing open above the latch; the same close view with the clamp closed around a plain round mating rim seated flush against the collar. In every panel the tug has a broad short ivory wedge hull, a dark graphite underside, one narrow burnt-orange band at the nose, a broad smoked-blue canopy, two recessed circular rear thrusters side by side and four short rigid radiator fins. The round bow maintenance docking collar carries a flat inner hatch and a single broad hinged clamp. A rigid, coherent spacecraft with scuffed ivory paint and plain unmarked panels. Photoreal cinematic production design.
```

### 4.KOKPIT
```
DOSYA     ref/4.KOKPIT_v1.png
PANELLER  üç panel, bu sırayla: wide interior panel (arkadan, koltuklar önde, kanopi uzakta) · pilot side panel (sol konsol kenarı: kısa çift kumanda + yanaşma-bırakma anahtarı) · engineer side panel (sağ konsol kenarı: bilek bağlantısı yuvası)
KAYNAK    ref (yükleme sırası): ref/3.KESTREL_v1.png
```
```text
Reference 3 (tug): take the scuffed ivory finish, the graphite metal and the broad smoked-blue canopy shape from it, using the three-quarter panel. A single reference sheet of the empty two-seat cockpit inside that same tug, in three panels with clear gaps between the panels, in identical warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and cool outside light falling through the broad canopy, arranged as one wide panel on the top row and two panels on the bottom row. Top row: an eye-level wide view from behind the two seats looking forward; the navy pilot seat stands at frame-left and the engineer seat at frame-right, an ivory overhead shell above, a broad forward canopy with two fixed graphite mullions showing deep black space with sparse stars, and a low graphite console with abstract cyan light shapes made only of light; at the left edge of the console sit short paired controls and one broad physical docking-release toggle, and at its right edge a small wrist-link cradle with a dim cyan indicator, all unmarked. Bottom row: a close view of the console's left edge from the pilot seat's side, the short paired controls and the one broad docking-release toggle; a close view of the console's right edge, the small wrist-link cradle empty beneath its dim cyan indicator. The cockpit is empty of people. Photoreal cinematic production design, plain unmarked surfaces.
```

### 6.ARK
```
DOSYA     ref/6.ARK_v1.png
PANELLER  üç panel, bu sırayla: side view panel (burun sağda, kıç solda) · stern panel (iki motor + sancakta kıça yakın tug bakım portu) · port side panel (iskele yanı: yükleme köprüsü bağlantısı)
```
```text
A single reference sheet showing exactly the same enormous colony ark in three panels, with clear gaps between the panels, in identical cold white starlight from the upper left with a soft blue fill, against deep black space, arranged as one wide panel on the top row and two panels on the bottom row. Top row: a full side view level with the ark, its bow pointing to frame-right and its stern at frame-left, the whole length of the hull in view. Bottom row: the stern seen from behind and slightly from the starboard side, showing the two large blue rear engines and, on the starboard flank near the stern, the small round tug maintenance port with a raised round rim; the port flank at mid-length, showing the short sealed telescoping loading bridge attached to the hull and its closed end hatch. In every panel the ark is a long ivory segmented cylindrical hull with a graphite dorsal rail, six low rectangular cryo-habitat blocks along the spine, two large blue rear engines and a broad narrow forward canopy; two reinforced hull flanges sit on opposite flanks of the mid-hull, where the foundry's gantry clamps grip. Rigid, coherent geometry, plain unmarked ivory plating, sealed shapes only. Photoreal cinematic production design.
```

### 5.FOUNDRY
```
DOSYA     ref/5.FOUNDRY_v1.png
PANELLER  dört panel, bu sırayla: wide exterior panel (kepenkler kısmen kapalı, iki kelepçe kilitli) · gate open panel (üç kepenk tamamen açık, mekanik mandal oturmuş) · clamps open panel (iki çene ark'tan açık) · bridge and socket panel (köprü + altında acil soket)
KAYNAK    ref (yükleme sırası): ref/6.ARK_v1.png
```
```text
Reference 6 (ark): take the long ivory segmented hull, the graphite dorsal rail, the six low cryo-habitat blocks and the two blue rear engines from it, using the side view panel. A single reference sheet of a gigantic automated industrial foundry around an unnamed blue gas giant, in four panels with clear gaps between the panels, in identical cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs, arranged as two panels on the top row and two panels on the bottom row. Top row, first panel: a wide exterior view; a fixed black C-shaped processing cradle holds the long ivory colony ark on its centre axis, bow at frame-right and stern at frame-left; two enormous rigid gantry clamp arms grip reinforced flanges on the ark's near flank and far flank, both locked; ahead of the bow at frame-right a colossal circular exit gate shows exactly three rigid radial sliding shutters, partly closed; behind the stern at frame-left an orange furnace trench glows behind heavy blast ribs; the huge curved blue gas giant fills the far background among sparse stars. Second panel: the same view with the three shutters fully open onto open starfield and a heavy mechanical catch seated at the gate rim, the clamps still locked. Bottom row, first panel: the same view with both gantry clamp jaws swung outward and open, clear of the ark, the gate open. Second panel: a closer view of the ark's port flank where a short telescoping sealed loading bridge links the hull to the foundry's control spine, and below the bridge's foundry end a small round emergency tug socket on a short railed catwalk. All structures rigid and coherent, plain unmarked surfaces. Photoreal cinematic production design with stable physical scale.
```

### 7.KORIDOR
```
DOSYA     ref/7.KORIDOR_v1.png
PANELLER  üç panel, bu sırayla: wide corridor panel (tug-erişim hava kilidi ucundan; sol duvarda kriyo penceresi) · junction panel (yükleme köprüsü kapısı SOLDA, komuta kapısı uzak SAĞDA) · cryo window panel (pencere yakın, kapalı kapsül sıraları)
```
```text
A single reference sheet of one empty pressurized corridor inside a colony ark, in three panels with clear gaps between the panels, in identical amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window, arranged as one wide panel on the top row and two panels on the bottom row. Top row: an eye-level wide view from the round tug-access airlock threshold straight down the corridor; the round airlock opening with its rigid hatch recessed open beside the camera, ivory walls, a graphite grating floor, fixed navy handrails along both walls, a wide cryo observation window set in the left wall about a third of the way along and glowing faint green, and a rectangular door closing the far end. Bottom row: a view farther along the same corridor at a junction, a sealed rectangular door in the left wall close by leading to the foundry loading bridge, and the corridor turning slightly right toward a rectangular command doorway at the far right end; a close view of the cryo observation window in the left wall, its reinforced glass showing a dim hall of rows of closed ivory sleeping pods with opaque charcoal lids and dim green status dots, a navy handrail below it. The corridor is empty, human-scale and stable, every surface plain and unmarked. Photoreal cinematic production design.
```

### 8.KRIYO
```
DOSYA     ref/8.KRIYO_v1.png
PANELLER  iki panel, bu sırayla: aisle panel (alçak göz hizası, orta koridor, iki yanda kapsül sıraları) · pod close panel (tek kapalı kapsül yakın)
KAYNAK    ref (yükleme sırası): ref/7.KORIDOR_v1.png
```
```text
Reference 7 (corridor): take the look of the dim hall, the rows of closed ivory pods and the dim green status dots seen through the window from it, using the cryo window panel. A single reference sheet of that same huge pressurized cryo hall in two panels side by side with a clear gap, in identical readable amber aisle lamps, cool blue walls, and dim green status dots on every pod. Left panel: a deep wide view at knee height along the central aisle; hundreds of identical rigid ivory sleeping pods with opaque, sealed charcoal lids stand in repeating rows on both sides and recede toward a vanishing point in the dim distance; each pod carries one dim green status dot and stands between fixed navy rails; thin pale vapor lies along the floor. Right panel: a close view of one sealed pod, its opaque charcoal lid, its single green status dot, the navy rail beside it and the pale floor vapor. Every occupant stays completely hidden inside the sealed pods, and the hall holds only the pods, the rails and the lamps. Photoreal cinematic production design, plain unmarked surfaces.
```

### 9.KOPRU
```
DOSYA     ref/9.KOPRU_v1.png
PANELLER  dört panel, bu sırayla: interior tunnel panel · exterior intact panel · exterior retracted panel (vakum boşluğu, iki uç kapağı kapalı) · end platform panel (foundry ucu platformu, kapak penceresi)
```
```text
A single reference sheet of one rigid sealed loading bridge between a colony ark and a foundry, in four panels with clear gaps between the panels, arranged as two panels on the top row and two panels on the bottom row. Top row, first panel: an eye-level view down the inside of the intact bridge, a square graphite pressure tunnel with waist-high rails, a grated floor and reinforced glass sides, the ark hatch at frame-left and the foundry hatch at frame-right, in cool blue light through the glass sides and amber guide lamps along the rails. Second panel: the bridge seen from outside in cold white starlight from the upper left with a soft blue fill and a faint warm orange glow from frame-left, intact, the ark hatch at frame-left and the foundry hatch at frame-right, and below the foundry end one small round emergency tug socket with a short railed catwalk. Bottom row, first panel: the same exterior view with the rigid center tunnel section withdrawn straight into the foundry housing, leaving a short vacuum gap between two rigid end platforms, both end hatches closed. Second panel: a closer view of the foundry-side rigid end platform, its closed circular hatch with a small reinforced window, the platform rail and the vacuum gap beyond it. Everything rigid and coherent, plain unmarked surfaces. Photoreal cinematic production design.
```

### 10.CEKIRDEK
```
DOSYA     ref/10.CEKIRDEK_v1.png
PANELLER  beş panel, bu sırayla: vault wide panel · cradle close panel (mandal kulp üstünde kapalı) · core object panel (kullanılmamış, amber) · core overheating panel (amber merkez çok parlak, kasa ısı izli) · core spent panel (merkez karanlık, kasa yanık)
```
```text
A single reference sheet of one prototype vault and one portable power core in five panels, with clear gaps between the panels, in identical low amber lamps on graphite walls and the warm amber glow of the core's glass center, arranged as three panels on the top row and two panels on the bottom row. Top row: a wide view of the empty prototype vault, graphite walls, two rigid storage cradles, low amber lamps, one core resting in an open cradle with a single broad hinged retaining latch, and an empty matching rigid carry harness lying beside the cradle; a close view of the cradle with the broad retaining latch closed over the core's rigid carry handle; the unused core alone, a compact rectangular graphite casing with ivory corner guards, one rigid top carry handle and an amber glass center. Bottom row: the same core with its amber center blazing very bright and the casing marked by heat along its upper corners, the shape unchanged; the same core with its center dark and the casing blackened by heat, intact and rigid. The vault holds only the cradles, the core and the harness, and no hands appear in any panel. Photoreal cinematic production design, plain unmarked surfaces.
```

### 11.DRONE
```
DOSYA     ref/11.DRONE_v1.png
PANELLER  üç panel, bu sırayla: drone side panel · drone front panel (kırmızı şerit) · drone inert panel (karanlık, ızgara zeminde bütün)
```
```text
A single reference sheet showing exactly the same autonomous industrial sentry drone three times, side by side with clear gaps between the panels, in identical cool even light against a plain charcoal background. First panel: a side view of the drone floating level. Second panel: a front view of the drone floating, its single narrow horizontal red sensor strip and short forward emitter facing the camera. Third panel: the same drone inert and dark, resting intact on a grated metal floor, its red strip unlit. The drone is entirely mechanical: a rigid compact graphite rectangular casing carrying one narrow horizontal red sensor strip, two recessed maneuvering jets and one short forward emitter, in matte scuffed metal with plain unmarked surfaces. Stable object geometry. Photoreal cinematic production design.
```

### 12.KONTROL_ODASI
```
DOSYA     ref/12.KONTROL_ODASI_v1.png
PANELLER  dört panel, bu sırayla: wide room panel (üç kol dik, yuva boş) · console close panel (yuva + üç kol + bara) · levers down panel (üç kol aşağıda kilitli) · gate-catch pawl panel (pencere yanı kapı desteği, mekanik dişli çentikte)
KAYNAK    ref (yükleme sırası): ref/10.CEKIRDEK_v1.png
```
```text
Reference 10 (core): take the compact rectangular graphite casing with ivory corner guards, the rigid top carry handle and the amber glass center from it, using the core object panel. A single reference sheet of one empty pressurized foundry gate-control room, in four panels with clear gaps between the panels, in identical amber practical lamps, cyan abstract console lights, and cool blue gate light through the rear window, arranged as two panels on the top row and two panels on the bottom row. Top row, first panel: an eye-level wide view; a rear reinforced window overlooks the exit iris and the ivory ark; a low console holds a rectangular core input slot matching the core, empty, a broad blue gate-power lever, a broad teal port-clamp release lever and a separate orange mechanical gate-catch lever, all three standing upright, each with a fixed hinge and a visible end stop and none carrying a label; a small unmarked bus connector sits beside the slot; a doorway to the loading bridge stands at frame-left and a short side airlock at frame-right. Second panel: a close view of the console, the empty input slot, the three upright levers and the bus connector. Bottom row, first panel: the same close view with all three levers swung down to their end stops and latched. Second panel: a close view of the window-side gate support beside the rear window, a broad mechanical pawl seated in its fixed notch. The room is empty of people. Photoreal cinematic production design, plain unmarked surfaces.
```

### 13.KOMUTA
```
DOSYA     ref/13.KOMUTA_v1.png
PANELLER  üç panel, bu sırayla: wide bridge panel · pilot console panel (gümüş B kolu dik, yedek güç anahtarı, bilek bağlantısı yuvası) · lever B down panel
```
```text
A single reference sheet of the empty two-seat emergency command bridge in the stern service block of a colony ark, in three panels with clear gaps between the panels, in identical cyan abstract interface lights, amber emergency lamps, and cool light through the forward canopy, arranged as one wide panel on the top row and two panels on the bottom row. Top row: an eye-level wide view from behind the seats; the pilot chair stands at frame-left and a navigation console at frame-right, a broad forward canopy shows a colossal circular exit gate ahead, navy seats, an ivory shell; a single broad silver starboard-clamp release lever stands upright beside the pilot console, and at the right sits an unmarked wrist-link docking cradle. Bottom row: a close view of the pilot console, the silver lever upright with its fixed hinge and end stop, one broad backup-power toggle and the wrist-link cradle; the same close view with the silver lever swung down to its end stop and latched. The bridge is empty of people, all surfaces plain and unmarked. Photoreal cinematic production design.
```

### 14.ISKELE
```
DOSYA     ref/14.ISKELE_v1.png
PANELLER  üç panel, bu sırayla: catwalk wide panel · socket close panel (yaka kelepçesi açık) · socket locked panel (tug yakası oturmuş, kelepçe kapalı)
KAYNAK    ref (yükleme sırası): ref/9.KOPRU_v1.png
```
```text
Reference 9 (bridge): take the foundry-side end platform, the small round emergency tug socket and the short railed catwalk below it from it, using the end platform panel. A single reference sheet of that same foundry emergency service catwalk and socket, in three panels with clear gaps between the panels, in identical amber battery guide lamps along the catwalk, cold starlight, and a distant orange furnace glow beyond heavy blast ribs, arranged as one wide panel on the top row and two panels on the bottom row. Top row: an exterior wide view below the loading bridge's foundry end; a short rigid railed catwalk with a fixed magnetic boot plate and a single tether anchor point leads from the control-room side airlock to a small round tug docking socket with one broad hinged collar clamp; heavy blast ribs shield it from the distant orange furnace trench. Bottom row: a close view of the socket with its collar clamp open; the same close view with a tug's round collar seated against the socket and the clamp closed around it. The catwalk is empty of people. Photoreal cinematic production design, plain unmarked surfaces.
```

### 15.ARACLAR
```
DOSYA     ref/15.ARACLAR_v1.png
PANELLER  dört panel, bu sırayla: cutter panel · tether panel · emp puck panel · wrist-link panel
```
```text
A single product reference sheet on a plain charcoal background showing four objects in four panels with clear gaps between them, in even soft directional light, arranged as two panels on the top row and two panels on the bottom row. Top row: a compact graphite plasma cutter with a short blue tip; a coiled navy safety tether with one rigid silver magnetic anchor block. Bottom row: one small matte-grey fictional EMP puck with an amber indicator; one unmarked ivory wrist-link with a broad physical toggle and a cyan status light. Each panel holds exactly one object, coherent and sharp, with plain unmarked surfaces. Photorealistic industrial detail.
```

---

## C01 — Fırın kapısındaki esir gemi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C01.png · referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png
```

> Not: Açılış (ILK_30 §2): sorun ilk karede — tutsak ark, kısmen kapanmış kapı, büyüyen fırın ışığı; insan yok ama saf manzara değil. Kapak tabanı ile aynı üçlü (ark + kapı + fırın). Logo ve görüntüde yazı yok; başlık kurguda.
> Replik R01 voice-over, kadraj dışı, 2,0 s'den (ilk 2 s insan sesi yok; plan "ilk saniyede" → düzeltildi), 5,5 s sürer, 7,5 s'de biter. Klip sesi dış çekimde yalnız replik penceresi (T13); yatak Y1 kurguda.
> Referans: FILM §4 10.CEKIRDEK'i de listeler; kasa ve çekirdek bu kadrajda yok (plan da R11'i gerekçelendirmiyor) → çıkarıldı, eklense kadraja kasa nesnesi çağırır. Ark burnu sağda, kıç solda; iki kelepçe kolu (yakın yan + uzak yan), her ikisi kilitli.
> Dev yapılar rijit; kamera yavaş yanal kayma (hızlı kamera yok). Lens 18 mm. Vuruşlar 0-2 · 2-7 · 7-10: replik ikinci vuruşun son cümlesi.

### Görsel
```text
Reference 5 (foundry): take the black C-shaped processing cradle, the two gantry clamp arms, the three-shutter exit gate, the heavy blast ribs and the orange furnace trench from it, using the wide exterior panel. Reference 6 (ark): take the long ivory segmented hull, the graphite dorsal rail, the six low cryo-habitat blocks and the two blue rear engines from it, using the side view panel. Extreme wide exterior view on an 18 mm lens, level with the ark's mid-hull. The long ivory colony ark lies along the centre of the frame, its bow at frame-right and its stern at frame-left, held in the black C-shaped cradle by two enormous rigid gantry clamp arms gripping reinforced flanges on its near flank and its far flank, both clamps locked. At frame-right, ahead of the bow, the colossal circular exit gate shows exactly three rigid radial sliding shutters, partly closed. At frame-left, behind the stern, the orange furnace trench glows behind heavy blast ribs, its light growing along the stern plating. Behind the whole structure a huge curved blue gas giant fills the far background. The frame holds only the ark, the foundry structure and the planet. Everything hangs in deep black space with sparse stars. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-2 s: The camera begins a slow lateral drift to the right along the ark; the near gantry clamp arm slides slowly across the hull behind it, and the orange furnace glow behind the stern starts to swell. 2-7 s: The drift continues steadily across the long hull; at about 2 s Leon's low, dry voice as a calm voice-over says: We came to steal a power core. We left with a ship full of people. 7-10 s: The drift carries on and the furnace glow behind the stern grows stronger, warming the stern plating and the edges of the blast ribs, while both locked clamp arms, the three partly closed shutters and the whole hull stay rigid. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C02 — Hedef ve ilk risk

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C02.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/5.FOUNDRY_v1.png
```

> Not: Açılış, insanın ilk görünüşü (ILK_30 §2); geniş iki kişi (düşük riskli seçim), yakın yüz yok. Replik R02 Rhea, ağız kadrajda, 1,5 s'den 2,5 s (4,0'a kadar); Leon'un ağzı kapalı yazılı.
> Kamera sözleşmesi: kanopideki ark ile iki kişiyi birlikte görmenin tek yolu arkadan çekim; kamera sağ-arkada, Rhea sağ bileğindeki bağlantıya eğilince sağ profili (yara tarafı, yüz ve ağız) kameraya döner; Leon arkadan. Konuşma bittikten sonra başı kanopiye döner (plan: gözünü ark'a kaldırır).
> Referans: FILM §4 6.ARK ve 15.ARACLAR'ı da listeler; ark 5.FOUNDRY'nin geniş dış panelinde zaten beşikte (5, 6'dan türetilir), bilek bağlantısı 2.RHEA sayfasında → ikisi çıkarıldı (dört referans; yüz karışması riski azalır). Ark tug'a yanaşmamış, uzakta (tug C06'da yanaşır).
> Hareket: yumuşak itiş + tek bakış kalkışı; ikisi oturur. Vuruşlar 0-4 · 4-8 · 8-10; Rhea'nın kendi yapısı gereği Leon'un yüzü yok, kimlik tabanı arkadan görünen parçalarla.

### Görsel
```text
Reference 1 (man): take his ivory pressure suit, navy shoulders, orange upper-arm bands, white gloves and clear ivory helmet from it, using the back full-body panel. Reference 2 (woman): take her face, the small right-chin scar, the clear pearl helmet and the pearl pressure suit from it, using the face close-up panel. Reference 4 (cockpit): take the two seats, the ivory overhead shell, the graphite canopy mullions, the low graphite console, the short paired controls and the wrist-link cradle from it, using the wide interior panel. Reference 5 (foundry): take the ark held in the black cradle, the two gantry clamp arms, the three-shutter exit gate and the furnace trench from it, using the wide exterior panel. Wide two-shot on a 28 mm lens from behind and slightly above the two seats, a little right of centre. Exactly two adults sit in the frame. At frame-left, in the pilot seat, sits an adult 38-year-old olive-skinned man with short dark brown hair, in an ivory pressure suit with navy shoulders, orange upper-arm bands and a fully clear closed ivory helmet, seen from behind, both white gloves resting on the short paired controls. At frame-right, in the engineer seat, sits an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands and a fully clear closed pearl helmet; her head is bowed to the right toward her right forearm, which rests along the console edge with an unmarked ivory wrist-link on it showing one steady cyan light, and her helmet is seen in right profile with the clear visor and the scar visible. Ahead, through the broad canopy with its two fixed graphite mullions, the long ivory ark held in the black foundry cradle between two locked gantry clamp arms fills the glass, the orange furnace glow behind its stern at the left and the partly closed three-shutter exit gate at the right. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A gentle slow push-in begins from behind the two seats toward the canopy; the woman, her head bowed to the right toward the wrist-link on her right forearm, reads its steady cyan light. At about 1.5 s her lips move with the sentence as she says in a clear, quick adult woman's voice, precise and controlled: That ark is in the burn cradle. 4-8 s: The push-in continues and she lifts her eyes and head from the wrist-link up through the canopy toward the ark, while the man keeps both gloves on the paired controls and his lips stay closed. 8-10 s: The push-in eases a little closer between the seats as her gaze reaches the ark in the glass; both remain seated, and the ark, its clamp arms and the furnace glow behind its stern stay rigid. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C03 — İşin amacı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C03.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/4.KOKPIT_v1.png
```

> Not: Kapak anı parçası (AÇILIŞ tablosu): Leon'un yüzü ¾ + vizöre yansıyan amber kapı ışığı. Orta plan ¾ (yakın değil); şeffaf vizörde yüz riski (ILK_30 §6): kare kapısında yüz bozulması / göz asimetrisi bakılır, tutmazsa kamera biraz geriye alınır.
> Replik R03 Leon, ağız kadrajda, 1,5 s'den 5,0 s (6,5'e kadar), ≤5 s. T01: sağ eldiven kumandada ilk karede, hareket etmez; tek hareket küçük kask dönüşü (Rhea kadraj dışı, bakış kadrajın sağına).
> Referans: FILM §4 5.FOUNDRY ve 6.ARK'ı da listeler; ¾ orta planda kanopi görünmüyor, amber kapı ışığı yalnız vizör yansıması → ikisi çıkarıldı. Vizör yansıması kare üretiminde kurulur (video yeni yansıma icat etmez).
> Replik ilk vuruşta başlar ve ikinci vuruşa taşar (ikinci vuruş "cümleyi bitirir"). Vuruşlar 0-3 · 3-7 · 7-10.

### Görsel
```text
Reference 1 (man): take his face, the pale left-temple scar, the clear ivory helmet and the ivory pressure suit from it, using the face close-up panel. Reference 4 (cockpit): take the navy pilot seat, the ivory overhead shell, the short paired controls and the graphite console edge from it, using the pilot side panel. Medium three-quarter view on a 50 mm lens of an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet. He sits in the navy pilot seat, seen in three-quarter from the front, his face turned toward the camera with his helmet angled slightly toward frame-right and his eyes directed past the right edge of the frame. His right white glove rests on the short paired controls in front of him, and a soft band of reflected amber light, the glow of the foundry gate beyond the canopy, lies across his closed clear visor. Behind him is the ivory cabin shell with a warm amber lamp, and the cyan console glow touches the lower edge of the frame. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow restrained push-in begins on the man in the pilot seat; the band of reflected amber light drifts gently across his clear visor as his helmet starts to turn a few degrees toward frame-right, his right glove resting on the paired controls. At about 1.5 s his lips move with the sentence as he says in a low, dry adult man's voice, calm and guarded: The spare core is in the foundry. The ark is our way in. 3-7 s: The push-in continues as he finishes the sentence and his helmet turns on a little further toward frame-right, the amber reflection sliding slowly along the visor. 7-10 s: His helmet completes the small turn and his lips close; the push-in ends a little closer on his face, his right glove still resting on the controls. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C04 — Giriş yolu seçilir

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C04.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/4.KOKPIT_v1.png · ref/15.ARACLAR_v1.png
```

> Not: T01: sol eldiven anahtarın ÜSTÜNDE başlar (temas karede kurulu); video yalnız tek kısa bastırma ister ve eldiven anahtarın üstünde kalır. Arayüzde yazı yok: gösterge soyut camgöbeği ışık (T06). Replik R04 Rhea, ağız kadrajda, 1,5 s'den 2,5 s (4,0'a kadar) — flip repliğin bitiminden SONRA (4-7 vuruşu).
> Referans: FILM §4 10.CEKIRDEK'i de listeler; çekirdek kadrajda yok (askı boş) → çıkarıldı. Bilek bağlantısı sağ bilekte, sağ konsol kenarındaki yuvaya oturmuş; sol eldiven anahtarda (çapraz erişim, sahne içinde hareket etmez).
> Ekran yönü: Rhea tek çekimde önden ¾; sağ/sol kelimesi yalnız kendi uzuvları için (konsol kenarı "yanında"). Vuruşlar 0-4 · 4-7 · 7-10.

### Görsel
```text
Reference 2 (woman): take her face, the small right-chin scar, the clear pearl helmet and the pearl pressure suit from it, using the face close-up panel. Reference 4 (cockpit): take the engineer seat, the console edge and the small wrist-link cradle with its cyan indicator from it, using the engineer side panel. Reference 15 (tools): take the unmarked ivory wrist-link with its single broad physical toggle and cyan status light from it, using the wrist-link panel. Medium view on a 50 mm lens of an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet. She sits in the engineer seat, seen in three-quarter from the front, her head bowed slightly toward the link, her core-carry harness empty. Her right forearm lies along the console edge beside her with the unmarked ivory wrist-link seated in its fixed cradle, one cyan indicator lit, and her left white glove rests on top of the link's single broad physical toggle. Abstract cyan light shapes glow on the low graphite console below the frame edge. The light is warm amber practical lamps in the ivory overhead shell, soft cyan console glow from below, and the outside light falling through the broad canopy. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow push-in begins on the woman; her left glove rests on the wrist-link's broad toggle while the cyan light on the link glows steadily. At about 1.5 s her lips move with the sentence as she says in a clear, quick adult woman's voice, precise and controlled: Maintenance berth. Then the loading bridge. 4-7 s: The push-in continues and her left thumb presses the one broad toggle over to its far end stop in a single short motion; the glove stays on top of the link and the cyan light brightens a little. 7-10 s: The push-in eases closer as her head lifts from the link toward the canopy beyond the camera, her glove resting on the flipped toggle. The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmets. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C05 — Küçük gemi büyük gövdeye yaklaşır

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C05.png · referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/6.ARK_v1.png
```

> Not: Replik yok; kadrajda kimse yok (zamir yazılmadı). Tek hareket: tug tek eksende sağa kayar; temas SON vuruşta (son saniye), çarpma yok; sabit kamera. Kelepçe açık kalır (kilit C06'da).
> Geometri: kamera yanaşma eksenine dik, düz seviyede; ark gövdesi sağ kadrajda devasa bir duvar gibi, port ortasında ve sola bakıyor; tug sol kadrajda burnu sağa. Ark'ın burun/kıç yönü bu kadrajda okunmaz (dev ölçek), ışık cümlesindeki fırın ışığı sol kadrajdan gelir.
> Dış çekim: dünya cümlesi + dış ışık birebir; klip sesi AÇILMAZ (T13, replik yok), yatak Y1 kurguda. Vuruşlar 0-3 · 3-6 · 6-10.

### Görsel
```text
Reference 3 (tug): take the broad short ivory wedge hull, the dark graphite underside, the narrow orange nose band, the smoked-blue canopy, the round bow docking collar and its single broad hinged clamp from it, using the side view panel. Reference 6 (ark): take the curved ivory segmented hull plating and the small round starboard maintenance port with its raised rim near the stern from it, using the stern panel. Wide exterior side view on a 35 mm lens, level with the docking axis. At frame-left the compact ivory salvage tug floats with its nose pointing to frame-right, its round bow collar aligned with the small round maintenance port in the ark's starboard stern flank, a short gap about half the tug's length remaining between the collar and the port rim. At frame-right the ark's curved ivory flank rises as a huge wall of segmented plating with the round port at its centre, facing frame-left. The tug's single broad hinged clamp stands open. The frame holds only the tug and the ark's flank. Everything hangs in deep black space with sparse stars. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera is fixed and level; the rigid tug begins to glide slowly to the right along one straight docking axis toward the ark's port, its nose level with the port rim. 3-6 s: The tug keeps gliding level with no roll or yaw, and the gap between its bow collar and the port rim narrows steadily while the ark's flank and the port stay fixed. 6-10 s: The glide slows as the collars approach and the two collars meet gently in the last second, the tug's single hinged clamp still open above the join. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C06 — Yanaşma kilidi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C06.png · referans (yükleme sırası): ref/3.KESTREL_v1.png · ref/6.ARK_v1.png
```

> Not: T01: yakalar ilk karede temasta (C05→C06 kesmesinde temas anı atlanır, GOSTERIM ilke 1); tek hareket tek kelepçe, yukarıdan aşağı; gövdeler rijit. Kelepçe tug'ın yakasına ait, menteşe üstte; karşı yaka ark'ın port halkası.
> Replik R05 Rhea, telsiz (kadrajda kimse yok; konuşan görünmez), 1,5 s'den 1,0 s. Klip sesi dış çekimde yalnız replik penceresi (T13). Yakın ek plan: uzay kadrajda değil → yalnız dış ışık cümlesi, dünya cümlesi yok.
> Tug bu halkadan sonra C80'e kadar ark üzerinde kalır. Vuruşlar 0-3 · 3-8 · 8-10 (kilitleme son iki saniyede tamamlanır).

### Görsel
```text
Reference 3 (tug): take the round bow docking collar with its flat inner hatch and the single broad hinged clamp from it, using the bow collar open panel. Reference 6 (ark): take the small round starboard maintenance port with its raised rim and the ivory hull plating around it from it, using the stern panel. Close exterior side view on an 85 mm lens, level with the docking interface. At frame-left the tug's round bow collar with its flat inner hatch touches the raised rim of the ark's small round maintenance port at frame-right, the two collars flush against each other. The tug's single broad hinged clamp stands open just above its latch, its hinge on the tug side at the top and its closing path from top to bottom clearly visible. The frame holds only the two collars, the clamp and the adjoining hull plating. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: The camera is fixed and the tug's single clamp begins to rotate on its hinge, swinging down from above toward the latch. At about 1.5 s, over the suit radio, a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says: We're attached. 3-8 s: The clamp swings on through its visible closing path, a little quicker mid-swing, and closes around the joined collars; both collars and the hull plating stay rigid and the clamp is the only part that moves. 8-10 s: The clamp seats against the collar rim and locks home at its latch while the ivory hulls stay rigid around it. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C07 — Ark'a giriş

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C07.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png
```

> Not: Geniş koridor, kısa dolly; uzun yürüyüş yok (giriş C06→C07 kesmesinde, ikisi eşikte başlar). T15: tam iki kişi, kimlik arkadan görünen parçalarla (rozet, askı, sakal, yüz izi çıkarıldı).
> Replik R06 Leon, ağız kadrajda, 1,5 s'den 1,5 s. Kamera sol-arkada: Leon sol duvardaki kriyo penceresine dönünce sol profili (sol şakak yarası dahil) kameraya açılır; Rhea'nın ağzı kapalı. Pencere sol duvarda (7.KORIDOR geniş panel).
> Referans: FILM §4 3.KESTREL'i de listeler; tug kadrajda yok (hava kilidinin içinden bakılıyor) → çıkarıldı. Geçiş C06 (dış, Y1) → C07 (koridor, Y3): ses yatağı kurguda 1 s çapraz. Vuruşlar 0-5 · 5-8 · 8-10.

### Görsel
```text
Reference 1 (man): take his ivory pressure suit, navy shoulders, orange upper-arm bands, white gloves and clear ivory helmet from it, using the back full-body panel. Reference 2 (woman): take her pearl pressure suit, navy waist, teal upper-arm bands, white gloves, dark copper braid and clear pearl helmet from it, using the back full-body panel. Reference 7 (corridor): take the ivory walls, the graphite grating, the navy handrails, the amber emergency lamps, the cryo observation window and the far rectangular door from it, using the wide corridor panel. Wide view on a 24 mm lens from behind and slightly above and left of the two siblings, who stand side by side inside the open round tug-access airlock, their boots planted on the airlock threshold. Exactly two adults stand in the frame. At frame-left, nearer the camera, stands an adult 38-year-old olive-skinned man with short dark brown hair, in an ivory pressure suit with navy shoulders, orange upper-arm bands and a fully clear closed ivory helmet, seen from behind, his arms relaxed. At frame-right stands an adult 34-year-old olive-skinned woman with a dark copper low braid tucked inside her helmet, in a pearl pressure suit with a navy waist, teal upper-arm bands and a fully clear closed pearl helmet, seen from behind, her arms relaxed. Ahead of them the empty pressurized corridor runs straight away between ivory walls and navy handrails over a graphite grating; a wide cryo observation window glows faint green in the left wall, and a rectangular door closes the far end. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-5 s: A short slow dolly begins forward behind the two siblings into the corridor, the amber lamps along the ceiling starting to slide past overhead, as the man's helmet turns toward the cryo window in the left wall and the left side of his helmet turns into profile. At about 1.5 s his lips move with the sentence as he says in a low, dry adult man's voice, calm and guarded: No crew. No greeting. 5-8 s: The dolly continues and the empty corridor opens wider ahead; the woman stands planted beside him with her lips closed and her helmet facing down the corridor, while the man's helmet stays turned toward the green glow of the window. 8-10 s: The dolly slows as the window comes level with the man's shoulder; both siblings stay planted on the threshold, the lamps receding down the corridor. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C08 — Yeşil ışıkların fark edilmesi

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C08.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png
```

> Not: T10: ayaklar sabit, yalnız beli hafifçe cama eğilir. Replik R07 Rhea, ağız kadrajda, 1,5 s'den 2,5 s (4,0'a kadar). Kriyo penceresi kadrajın sağ üçte birinde; Rhea ¾ profil, camın solunda, sağ yanağı (yara tarafı) kameraya.
> Pencere yeşil ışığı yanağına ve vizörüne vurur (KORİDOR ışık cümlesi: "faint green status light through the cryo window"). Kapsüller opak ve kapalı; camın ardında yolcu yüzü yok. Askı boş.
> Bakış sözleşmesi: Rhea'nın bakışı kadrajın sağına (cama). Vuruşlar 0-4 · 4-6 · 6-10.

### Görsel
```text
Reference 2 (woman): take her face, the small right-chin scar, the clear pearl helmet and the pearl pressure suit from it, using the face close-up panel. Reference 7 (corridor): take the cryo observation window with the closed pod rows behind its glass, the ivory wall and the navy handrail from it, using the cryo window panel. Medium view on a 50 mm lens of an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, standing in the corridor beside the cryo observation window, which fills the right third of the frame; through its reinforced glass rows of closed ivory pods with dim green status dots recede into a dim hall. She stands in three-quarter profile facing the glass, her right cheek and small right-chin scar toward the camera, her boots planted on the graphite grating and her torso upright, her head and shoulders angled slightly toward the window, her core-carry harness empty. A navy handrail runs along the ivory wall behind her. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow push-in begins toward the woman in three-quarter profile; she starts to lean a little toward the glass from the hips, her boots planted. At about 1.5 s her lips move with the sentence as she says in a clear, quick adult woman's voice, precise and controlled: Those storage units are drawing life-support power. 4-6 s: The push-in continues as her lean deepens slightly toward the window and the dim green pod lights glow steadily across her visor. 6-10 s: She keeps her lean, her breathing calm, and the push-in ends close beside her while her boots remain planted on the grating. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C09 — Yolcuların kanıtı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C09.png · referans (yükleme sırası): ref/8.KRIYO_v1.png
```

> Not: Kadrajda kimse yok; kapaklar opak ve kapalı, yolcu yüzü / siluet / çocuk yok (plan §13.1). Yeşil durum noktaları soyut ışık, yazı yok (T06). Replik R08 Rhea, telsiz (konuşan görünmez), 1,5 s'den 1,5 s.
> Kamera alçak (diz hizası), yavaş ileri takip; kapaklar açılmaz. Zemin buharı pressurize salonda (vakum değil). Zamir yazılmadı (insansız kadraj). Müzik bu çekimde incelir (FILM §7), ses yatağı Y4.
> Vuruşlar 0-3 · 3-5 · 5-10.

### Görsel
```text
Reference 8 (cryo hall): take the rows of identical rigid ivory sleeping pods with opaque charcoal lids, the dim green status dots, the navy rails and the pale floor vapor from it, using the aisle panel. Deep wide view on a 24 mm lens at knee height along the central aisle of a huge pressurized cryo hall: hundreds of identical rigid ivory sleeping pods with opaque, sealed charcoal lids stand in repeating rows on both sides of the aisle and recede toward a vanishing point in the dim distance; each pod carries one dim green status dot and stands between fixed navy rails; thin pale vapor lies along the floor. Every sleeper stays completely hidden inside its sealed pod, and the hall holds only the pods, the rails and the lamps. The light is readable amber aisle lamps, cool blue walls, and dim green status dots on every pod. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow low track begins forward down the central aisle at knee height, the pod rows sliding past on both sides; at about 1.5 s, over the suit radio, a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says: They're sleepers. Still alive. 3-5 s: The track continues and the repeating rows of sealed pods draw steadily past, each dim green status dot gliding by in turn. 5-10 s: The track carries on deeper into the hall and ever more rows open ahead in the dim distance; every lid stays sealed while the thin floor vapor drifts slowly along the aisle. The only ambient sound is a deep, steady refrigeration hum with a faint hiss of floor vapor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C10 — Kurtarılacak sayı

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C10.png · referans (yükleme sırası): ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png · ref/15.ARACLAR_v1.png
```

> Not: T06: bilek bağlantısı göğüs hizasında, tek camgöbeği ışık; okunur ekran yok, sayı yalnız replikte. Replik R09 Rhea, ağız kadrajda, 1,5 s'den 2,0 s (3,5'e kadar); rakam ağız kadrajdaki repliktedir ("Four thousand": sözle yazıldı, rakam yok).
> Bakış sözleşmesi: Rhea'nın bakışı bağlantıdan kadrajın soluna (Leon kadraj dışı; C11 iki kişide Leon solda). Sağ ön kol göğsün önünde kalkık, bilek bağlantısı sağ bilekte. Askı boş.
> Bel üstü yakın plan (kafa-bel); koridorun amber/mavi ışığı. Vuruşlar 0-3 · 3-7 · 7-10.

### Görsel
```text
Reference 2 (woman): take her face, the small right-chin scar, the clear pearl helmet and the pearl pressure suit from it, using the face close-up panel. Reference 7 (corridor): take the ivory wall, the navy handrail and the amber emergency lamps from it, using the wide corridor panel. Reference 15 (tools): take the unmarked ivory wrist-link with its broad physical toggle and cyan status light from it, using the wrist-link panel. Close view on an 85 mm lens, from the top of her helmet down to her waist, of an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, standing in the corridor, seen in three-quarter from the front. Her right forearm is raised across her chest with the unmarked ivory wrist-link at chest height showing one steady cyan light, and her eyes are lowered to it; her core-carry harness is empty. Behind her, softly out of focus, an ivory corridor wall with a navy handrail and warm amber emergency lamps. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-3 s: A slow push-in begins on the woman's face and the wrist-link in front of her chest; her eyes rest on its cyan light, which pulses gently. At about 1.5 s her lips move with the sentence as she says in a clear, quick adult woman's voice, precise and controlled: Four thousand stable life signs. 3-7 s: The push-in continues as her eyes lift from the cyan light and travel to frame-left toward the man standing off-camera, her head turning a few degrees with them. 7-10 s: Her gaze settles on him and the push-in ends slightly closer, the wrist-link still at chest height with its light steady. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C11 — İlk ahlaki karar

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C11.png · referans (yükleme sırası): ref/1.LEON_v1.png · ref/2.RHEA_v1.png · ref/7.KORIDOR_v1.png
```

> Not: İki replik, ağız kadrajda, sırayla: R10 Leon 1,0 s'den 3,0 s (4,0'a kadar) → R11 Rhea 4,5 s'den 1,5 s (6,0'a kadar); her biri kendi vuruşunun son cümlesi, konuşmayan tarafın ağzı kapalı yazılı. T12: duraksama küçük, donmaz (itiş + nefes + bakış hareketi sürer). Plan: "Leon pauses; Rhea holds his gaze, both remain still."
> T15: tam iki kişi. Kimlik: yüzler her ikisinde ¾ ve kameraya açık ("dirty two-shot"; yara taraflarının ikisi de görünür), gözler birbirine. Leon solda, Rhea sağda; kriyo penceresi arkalarında, yeşil kapsül ışıkları camın ardında (opak kapaklar).
> Askı boş. Vuruşlar 0-4 · 4-7 · 7-10 (Rhea'nın cümlesi ikinci vuruşun 4,5. saniyesinde).

### Görsel
```text
Reference 1 (man): take his face, the pale left-temple scar, the clear ivory helmet and the ivory pressure suit from it, using the face close-up panel. Reference 2 (woman): take her face, the small right-chin scar, the clear pearl helmet and the pearl pressure suit from it, using the face close-up panel. Reference 7 (corridor): take the wide cryo observation window with the closed pod rows and dim green status dots, the ivory wall and the navy handrail from it, using the cryo window panel. Medium two-shot on a 50 mm lens at eye level in the corridor, both standing in front of the cryo observation window with their faces angled toward the camera and their eyes directed at each other. Exactly two adults stand in the frame. At frame-left stands an adult 38-year-old olive-skinned man with short dark brown hair, brown eyes, a neat beard and a pale left-temple scar, in an ivory pressure suit with navy shoulders, orange upper-arm bands, a blue-gold hawk badge, and a fully clear closed ivory helmet, his eyes directed across to the woman. At frame-right stands an adult 34-year-old olive-skinned woman with green eyes, a dark copper low braid tucked inside her helmet and a small right-chin scar, in a pearl pressure suit with a navy waist, teal upper-arm bands, a blue-gold geometric-sun badge, a fixed graphite core-carry harness, and a fully clear closed pearl helmet, her eyes directed across to the man, her core-carry harness empty. Behind them the reinforced glass of the window shows rows of closed ivory pods with dim green status dots receding into a dim hall; a navy handrail runs along the ivory wall. The light is amber emergency lamps along the ivory ceiling, cool blue wall light, and faint green status light through the cryo window. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: A slow push-in begins on the two of them, the green pod lights beyond the window glowing steadily, her eyes on him and her lips closed. At about 1 s his lips move with the sentence as he says in a low, dry adult man's voice, calm and guarded: We take the core, then open their clamps. 4-7 s: The push-in continues as he pauses, his eyes dropping slightly and his lips closed; at about 4.5 s her lips move with the sentence as she says in a clear, quick adult woman's voice, precise and controlled: Then we take everyone. 7-10 s: He raises his eyes back to her and she holds his gaze as the push-in closes slightly tighter; both breathe calmly with their lips closed. The only ambient sound is a low, steady ship ventilation hum in a large pressurized corridor. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

## C12 — Fırın işlemi sürüyor

```
FLOW      Frames to Video
EKLE      başlangıç karesi: kare/C12.png · referans (yükleme sırası): ref/5.FOUNDRY_v1.png · ref/6.ARK_v1.png
```

> Not: Plan "contained orange exhaust pulse" der; vakumda egzoz/duman T03 (BILINEN_TUZAKLAR §B sıra 4) → "exhaust" kelimesi yazılmadı, olay KAYBURGALARIN ARKASINDA yükselen turuncu fırın IŞIK atımı olarak çevrildi (parıltı + kaburga kenarlarında aydınlanma), gövdeye ulaşmaz, duman/pus yok.
> Replik R12 Rhea, telsiz (kadrajda kimse yok), 1,5 s'den 3,0 s (4,5'e kadar); dış çekimde klip sesi yalnız replik penceresi (T13). Kamera ark'ın sancak arka çeyreğinde, kıç sol-merkezde, fırın çukuru en solda kaburgaların arkasında; çıkış kapısı sağda uzakta (üç kepenk kısmen kapalı).
> Motorlar sönük (ark C89'dan önce çıkış yakması yapmaz). Dış ışık + dünya cümlesi birebir. Vuruşlar 0-4 · 4-8 · 8-10.

### Görsel
```text
Reference 5 (foundry): take the black C-shaped cradle, the two gantry clamp arms, the three-shutter exit gate, the heavy blast ribs and the orange furnace trench from it, using the wide exterior panel. Reference 6 (ark): take the stern with its two blue rear engine housings and the long ivory segmented hull from it, using the stern panel. Wide exterior view on a 24 mm lens from the ark's starboard rear quarter, level with the stern. The ark's stern with its two large rear engine housings, unlit, stands at centre-left; the long ivory hull runs away toward frame-right, held by its two locked gantry clamp arms, to the colossal circular exit gate far ahead at frame-right, whose three rigid radial sliding shutters are partly closed. At the far left, behind the stern, the orange furnace trench glows behind a row of heavy blast ribs that stand between the trench and the ark. Behind the whole structure a huge curved blue gas giant fills the far background. The frame holds only the ark, the foundry structure and the planet. Everything hangs in deep black space with sparse stars. The light is cold white starlight from the upper left, soft blue fill from a huge curved blue gas giant in the far background, and a warm orange furnace glow from frame-left behind heavy blast ribs. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

### Video
```text
0-4 s: The camera begins a slow glide to the right along the ark's flank while the orange glow behind the heavy blast ribs starts to swell; at about 1.5 s, over the suit radio, a clear, quick adult woman's voice, precise and controlled, softened by a light suit-radio filter, says: We have until the purge reaches this berth. 4-8 s: The glide continues and one contained pulse of orange furnace light rises behind the blast ribs, brightening the rim of each rib and the edge of the stern engine housings; the pulse stays behind the ribs, leaving the hull in cold starlight. 8-10 s: The pulse softens and the glow settles back; the two locked clamp arms, the partly closed shutters and the whole ark stay rigid as the glide carries on. The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of suit-radio static. Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film texture, readable cold charcoal-blue shadows, restrained amber practical light, and coherent metal and sealed glass.
```

---

## FLOW İŞ EMRİ

> **Flow proje ayarları (bir kez, üretimden önce):** Return silent videos **KAPALI** (bu filmde replikler model sesidir; klibin sesi filme girer) · Visible watermarking **KAPALI** (SynthID her çıktıda kalır).
> **Model / süre:** sahip planı görselleri GPT Image, videoları Gemini görselden video 10 s ile hedefler (FILM §0 URETIM). Flow'da Görsel modu aynı promptla ve aynı referans sırasıyla kullanılabilir. Omni'nin Frames to Video süresi,
> kredisi ve repliği videoda üretmesi SMOKE P11 · P14 · P18'de ölçülür (`FLOW_GERCEKLERI.md` §1 · §9); ölçüm gelmeden videolar (sıra 19-39) koşulmaz. Replik biçimi (iki nokta ↔ tırnak) SMOKE P9. Tahmini kredi: Omni kredisi BİLİNMİYOR (P11), sütun ölçümden sonra dolar.
> **Frames to Video'ya referans eklenmez** (yalnız kare); referanslar yalnız referans sayfası ve kare üretiminde. Her referans yüklenirken kare promptunun kendi sırası (EKLE satırı) korunur.
> **Sıra:** 1-15 referans sayfaları (KAYNAK bağımlılığı: 3 → 4, 6 → 5, 7 → 8, 10 → 12, 9 → 14) → **açılış önce (ILK_30 §6): C01-C03 kareleri → C01-C03 videoları** → C04-C12 kareleri → C04-C12 videoları.
> Referanslar onaylanmadan kare, kare onaylanmadan video üretilmez. Açılış kare kapısı (ILK_30 §6): filigran/logo · istenmeyen yazı · el kaynaşması · yüz bozulması / göz asimetrisi · kimlik kayması; biri varsa çekim açılışta kullanılmaz.
> **Vakumda ses (kurgu, F8):** dış klipler C01 · C05 · C06 · C12'de klibin sesi yalnız FILM §5 replik penceresinde (±0,5 s) açık; C05'te replik yok, klip sesi hiç açılmaz (yatak Y1 kurguda).

| Sıra | Çekim | İndirilecek dosya | Mod | Eklenecek | Deneme | Tahmini kredi |
|:--:|:--:|---|---|---|:--:|:--:|
| 1 | 1.LEON | `ref/1.LEON_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 2 | 2.RHEA | `ref/2.RHEA_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 3 | 3.KESTREL | `ref/3.KESTREL_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 4 | 4.KOKPIT | `ref/4.KOKPIT_v1.png` | Görsel | ref/3.KESTREL_v1.png (three-quarter panel) | 2 | |
| 5 | 6.ARK | `ref/6.ARK_v1.png` | Görsel | — (yalnız prompt) · 5.FOUNDRY'den ÖNCE üretilir | 2 | |
| 6 | 5.FOUNDRY | `ref/5.FOUNDRY_v1.png` | Görsel | ref/6.ARK_v1.png (side view panel) | 2 | |
| 7 | 7.KORIDOR | `ref/7.KORIDOR_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 8 | 8.KRIYO | `ref/8.KRIYO_v1.png` | Görsel | ref/7.KORIDOR_v1.png (cryo window panel) | 2 | |
| 9 | 9.KOPRU | `ref/9.KOPRU_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 10 | 10.CEKIRDEK | `ref/10.CEKIRDEK_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 11 | 11.DRONE | `ref/11.DRONE_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 12 | 12.KONTROL_ODASI | `ref/12.KONTROL_ODASI_v1.png` | Görsel | ref/10.CEKIRDEK_v1.png (core object panel) | 2 | |
| 13 | 13.KOMUTA | `ref/13.KOMUTA_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 14 | 14.ISKELE | `ref/14.ISKELE_v1.png` | Görsel | ref/9.KOPRU_v1.png (end platform panel) | 2 | |
| 15 | 15.ARACLAR | `ref/15.ARACLAR_v1.png` | Görsel | — (yalnız prompt) | 2 | |
| 16 | C01 kare | `kare/C01.png` | Görsel | ref/5.FOUNDRY_v1.png (wide exterior panel) · ref/6.ARK_v1.png (side view panel; bu sırayla) · **AÇILIŞ: önce üretilir** | 2 | |
| 17 | C02 kare | `kare/C02.png` | Görsel | ref/1.LEON_v1.png (back full-body panel) · ref/2.RHEA_v1.png (face close-up panel) · ref/4.KOKPIT_v1.png (wide interior panel) · ref/5.FOUNDRY_v1.png (wide exterior panel; bu sırayla) · **AÇILIŞ** | 2 | |
| 18 | C03 kare | `kare/C03.png` | Görsel | ref/1.LEON_v1.png (face close-up panel) · ref/4.KOKPIT_v1.png (pilot side panel; bu sırayla) · **AÇILIŞ** | 2 | |
| 19 | C01 | `ham/C01_d1.mp4` | Frames to Video | kare/C01.png · **AÇILIŞ: önce üretilir** | 2 | |
| 20 | C02 | `ham/C02_d1.mp4` | Frames to Video | kare/C02.png · **AÇILIŞ** | 2 | |
| 21 | C03 | `ham/C03_d1.mp4` | Frames to Video | kare/C03.png · **AÇILIŞ** | 2 | |
| 22 | C04 kare | `kare/C04.png` | Görsel | ref/2.RHEA_v1.png (face close-up panel) · ref/4.KOKPIT_v1.png (engineer side panel) · ref/15.ARACLAR_v1.png (wrist-link panel; bu sırayla) | 2 | |
| 23 | C05 kare | `kare/C05.png` | Görsel | ref/3.KESTREL_v1.png (side view panel) · ref/6.ARK_v1.png (stern panel; bu sırayla) | 2 | |
| 24 | C06 kare | `kare/C06.png` | Görsel | ref/3.KESTREL_v1.png (bow collar open panel) · ref/6.ARK_v1.png (stern panel; bu sırayla) | 2 | |
| 25 | C07 kare | `kare/C07.png` | Görsel | ref/1.LEON_v1.png (back full-body panel) · ref/2.RHEA_v1.png (back full-body panel) · ref/7.KORIDOR_v1.png (wide corridor panel; bu sırayla) | 2 | |
| 26 | C08 kare | `kare/C08.png` | Görsel | ref/2.RHEA_v1.png (face close-up panel) · ref/7.KORIDOR_v1.png (cryo window panel; bu sırayla) | 2 | |
| 27 | C09 kare | `kare/C09.png` | Görsel | ref/8.KRIYO_v1.png (aisle panel) | 2 | |
| 28 | C10 kare | `kare/C10.png` | Görsel | ref/2.RHEA_v1.png (face close-up panel) · ref/7.KORIDOR_v1.png (wide corridor panel) · ref/15.ARACLAR_v1.png (wrist-link panel; bu sırayla) | 2 | |
| 29 | C11 kare | `kare/C11.png` | Görsel | ref/1.LEON_v1.png (face close-up panel) · ref/2.RHEA_v1.png (face close-up panel) · ref/7.KORIDOR_v1.png (cryo window panel; bu sırayla) | 2 | |
| 30 | C12 kare | `kare/C12.png` | Görsel | ref/5.FOUNDRY_v1.png (wide exterior panel) · ref/6.ARK_v1.png (stern panel; bu sırayla) | 2 | |
| 31 | C04 | `ham/C04_d1.mp4` | Frames to Video | kare/C04.png | 2 | |
| 32 | C05 | `ham/C05_d1.mp4` | Frames to Video | kare/C05.png | 2 | |
| 33 | C06 | `ham/C06_d1.mp4` | Frames to Video | kare/C06.png | 2 | |
| 34 | C07 | `ham/C07_d1.mp4` | Frames to Video | kare/C07.png | 2 | |
| 35 | C08 | `ham/C08_d1.mp4` | Frames to Video | kare/C08.png | 2 | |
| 36 | C09 | `ham/C09_d1.mp4` | Frames to Video | kare/C09.png | 2 | |
| 37 | C10 | `ham/C10_d1.mp4` | Frames to Video | kare/C10.png | 2 | |
| 38 | C11 | `ham/C11_d1.mp4` | Frames to Video | kare/C11.png | 2 | |
| 39 | C12 | `ham/C12_d1.mp4` | Frames to Video | kare/C12.png | 2 | |

> Ses ölçümü: replik taşıyan klipler C01-C04 · C06-C12 (C05 yok): ağız kadrajda C02 (R02) · C03 (R03) · C04 (R04) · C07 (R06) · C08 (R07) · C10 (R09) · C11 (R10 · R11); voice-over C01 (R01); telsiz C06 (R05) · C09 (R08) · C12 (R12).
> İlk dört klipte (19-21 ve ardından C04) replik biçimi ve ses profilleri (Leon alçak kuru · Rhea berrak hızlı · telsiz filtresi) SMOKE P9 · P18'e göre kontrol edilir; model aynı sesi iki klipte tutamazsa FILM §5 / NOTLAR yedek yöntemi (kurguda eklenen kayıt) uygulanır.
