🚀 **NINE MINUTES — Dokuz Dakika**
Yatay Shorts / Reels Production Document
Format: **16:9 (YATAY)** | Sahne: 6 (Hook + 5 Ana Sahne) | Süre: Her sahne 8 saniye, toplam 48 saniye
Prompt yapısı: Her sahne için **1 görsel promptu + 1 video promptu** (tek versiyon)
_"Dokuz dakika. Bir dünyayı geride bırakmak için gereken bütün süre bu."_

---

## ⚠️ Genel Prodüksiyon Kuralları

1. **SIFIR KESME** — Her video 8 saniyelik, kesintisiz tek çekim. Ritim yalnızca kamera hareketiyle ve aracın kendi hareketiyle kurulur.
2. **YATAY SADAKAT (16:9)** — Dikey formatın tersi: ölçek YUKARI değil **GENİŞLİĞE** çalışır. Dikey bir roketi yatay kadrajda çekmenin kuralı: **araç asla ortada değildir** — sol ya da sağ üçte birdedir, kadranın kalan genişliğini alev, buz perdesi, kule, duman düzlüğü ya da Dünya'nın eğrisi doldurur. İç mekan sahnelerinde kadranın bir üçte biri yüz, bir üçte biri penceredir.
3. **ÜÇ LENS KİLİDİ** — İç mekan geniş + araç üstü kamera: **32mm**. İç mekan yakın/duygusal: **75mm**. Yerden dış çekim takibi: **200mm**. Üçü asla tek karede karışmaz. Kamera mesafesi her promptta **metre** olarak yazılır.
4. **GÖSTER, ANLATMA** — Yönetmen notu yok. Ölçek betimlemenin içinde doğal ortaya çıkar.
5. **RENK DİLİ** — **Metan mavi-beyazı + kavruk bakır turuncusu + kırağı beyazı + okyanus ultramarini + mutlak vakum siyahı.** Serideki hiçbir shorts bu paleti kullanmadı (Glass World: buz mavisi/opal/prizma · Last Archive: kireç/pas/arşiv mavisi/altın/lavanta · Remembering Dust: gri toz/indigo/kemik/pas turuncusu · Counting Rain: yosun yeşili/sülfür sarısı/obsidyen/bakır/mercan).
6. **KARAKTER SADAKATİ** — İç mekan sahnelerinde (S0, S4, S5) aynı yüz, aynı suit, aynı yıpranmış detaylar; karakter bloğu üç promptta da birebir tekrarlanır. Dış çekimlerde (S1, S2, S3) **hiçbir insan figürü render edilmez** — karakter mühürlü kapsülün içindedir.
7. **VİRAL ZAMANLAMA (Hook)** — 0-2sn merak (sessizce bağlı oturan bir insan) → 2-5sn ipuçları (gevşek kayış titremeye başlıyor, pencere çerçevesinden kırağı pulları kalkıyor) → 5-7sn tam reveal (ateşleme: mavi-beyaz ışık kapsülü dolduruyor, her şey titriyor) → 7-8sn tek güçlü görüntü (yüzü koltuğa bastırılmış, vizöründe alev).
8. **TEK VİDEO PROMPTU** — Her sahnenin **tek** video promptu vardır, T2V (metin→video) olarak yazılmıştır. Referans görselden üretim (I2V) yapacaksan: baştaki teknik satırı ve `At 0s` beat'ini sil, yerine `"The scene begins exactly as the provided image."` yaz, kalan beat'leri düz nesre çevir. Aracı, kapsülü ya da karakteri asla yeniden tarif etme.
9. **⚠️ SARSINTI İSTİSNASI** — Bu dokümanda "no camera shake" kuralı **değiştirildi.** Fırlatmada titreşim gerçeğin kendisidir. Kural: **kamera araca cıvatalıdır** — titreşim ARACIN titreşimidir, operatörün değil. Promptlarda `no handheld shake, no operator shake — rigid rig-mounted vibration only` yazılır. Kadraj asla savrulmaz, ufuk asla yalpalamaz.

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili 🆕

> Bu doküman 31.07.2026'ya kadar yalnızca **Ders 34**'e atıf yapıyordu.
> `LESSONS_LEARNED.md`'de 49 ders var ve bir roket fırlatma filminin
> tetikleyeceği ders kümesi serinin en tehlikelisi. Aşağıdakiler
> **promptlara zaten yazılı olan** kuralların ders numarasıyla eşlenmiş
> hali + eksik olanların eklenmesi gereken satırları.

```
🔴 EN YÜKSEK RİSK — bu filmin doğasından geliyor

DERS 21  STATİK ATEŞ — "boyama gibi patlama"
         Alev, kadrajda duran bir DOKU değil, saniyede değişen bir OLAY.
         Zorunlu satır: "the exhaust plume evolves continuously frame to
         frame — expanding, curling, shedding shock diamonds; never a
         static painted flame shape."
         → En muhtemel sahne: S1 (kule temiz), S2 (max-Q).

DERS 10  PARTİKÜL FİZİĞİ — donmuş toz ve egzoz
         Kırağı pulları, buz kabuğu, kalkış tozu: hepsi hareket etmeli.
         Zorunlu satır: "every ice flake and dust particle carries its own
         velocity; nothing hangs motionless in air."
         → S0 (kırağı pulları), S1.

DERS 36  VAKUMDA ATMOSFERİK DUMAN
         S3 ayrılma vakumda gerçekleşiyor. Duman KIVRILMAZ, YAYILMAZ,
         yükselmez — düz çizgide dağılır ve kaybolur.
         Zorunlu satır: "in vacuum the plume expands in straight radial
         lines and disperses instantly — no curling, no billowing, no
         atmospheric smoke behaviour."

DERS 23  SIFIR-G KATILIĞI
         S4 kesilme anı = sıfır-g'nin başladığı an. Kayış, saç teli, toz,
         kablo ucu: hepsi bağımsız sürüklenir. Karakter rijit bir model
         gibi asılı kalmaz.
         → S4, S5.

🟡 ORTA RİSK

DERS 3   AI BLOOM — motor parlaması yıkanmış yüzey üretir
DERS 41  YUMUŞAK IŞIK ≠ BLOOM — kapsül içi ışık yumuşak olabilir, yıkanamaz
DERS 5   VİZÖR KAYBOLMASI — S0/S4/S5 arasında vizör hep aynı durumda
DERS 37  EKİPMAN DURUM GEÇİŞİ — kask/kayış sahne arasında aniden belirmez
DERS 16  YÜZ MORPH — kask arkasındaki yüz üç iç mekan sahnesinde aynı kişi
DERS 44  AĞIR ÇEKİM OKUNMASI — fırlatma gerçek zamanlı; "slow motion" yasak

⬛ HER PROMPTTA

DERS 9 · 13 · 34 · 45   EKRANDA METİN YOK
         Kadrajda yazı, rakam, HUD, lens verisi, isim etiketi, jenerik kartı
         olmaz. Telemetri ekranları soyut segment/nabız olarak render edilir.
         ⚠️ DERS 45: prompt gövdesinde `[CHARACTER BIBLE]` gibi köşeli
         parantez etiketi, `CAMERA:` başlıklı sayı-harf satırı ve karakterin
         ADI bulunmaz — model bunları ekrana etiket olarak çiziyor.
         Bu doküman bu üç kurala **zaten uyuyor**; korunmalı.
```

**Negatif bloklara eklenecek kuyruk (her görsel promptun sonuna):**

```
no static painted flame, no frozen exhaust, no motionless particles,
no atmospheric smoke in vacuum, no curling vacuum plume, no rigid
zero-g floating, no bloom, no glow filter, no slow motion, no text,
no digits, no HUD overlay, no lens data, no name label, no watermark
```

---

## 📖 Sabit Referanslar (Bibles)

### 👤 Character Bible

**Kimlik (yalnızca bu dosyada):** DR. SELİN KAYAALP, 38, uçuş mühendisi. Tek kişilik görev.

> ⚠️ **ÜRETİM UYARISI [Ders 34]:** Karakter Türk, ama promptlarda
> **milliyet ifadesi KULLANILMAZ** — geçmişte milliyet ifadesi üretim reddine
> yol açtı. Kimlik bu bölümde kalır; promptlarda yalnızca fiziksel tarif geçer.
> Karakterin adı da hiçbir promptta yazılmaz. Gerçek bir kurum, ülke, bayrak,
> ajans ya da şirket adı hiçbir promptta geçmez.

**Tam tarif — S0, S4, S5 görsel promptlarında birebir, kısaltmasız tekrarlanır:**

```
A 38-YEAR-OLD WOMAN flight engineer — light olive-brown skin with clearly visible pores and a scatter of small dark moles along the left jawline, natural asymmetry with the right nostril sitting slightly wider than the left, a thin pale scar across the bridge of the nose, dark grey-brown eyes with faint fatigue shadows beneath them, a dry lower lip bitten pale at one corner, black hair pulled into a flat low knot with several strands escaped and pressed against her temples. Photographed as a real person, not CGI. She wears a matte ARCTIC-WHITE full-pressure launch suit with CHARCOAL-GREY articulated joints at the shoulders, elbows and knees, thick charcoal five-point harness webbing crossing her chest, scuffed pale wear along both forearms, a faded mission patch on the left chest with NO readable characters on it, and a half-erased serial block on the right thigh with no legible letters or numbers. A slim wrist screen on her left forearm shows abstract drifting segments only. Her helmet is a fully enclosed white shell with a FULLY TRANSPARENT curved visor carrying a faint breath-fog trace along its lower edge and one fine scratch across the upper left. BOTH HANDS ARE EMPTY — she grips nothing and holds no tool.
```

**Hareket imzası (konsepte özgü):** Ağırlık altında yaşamayı bilen birinin
ekonomisi — g yükselirken **hiç direnmez**, ellerini kol dayamalarına bırakır,
çenesini içeri alır, nefesini kısa ve düzenli tutar. Panik yok, çığlık yok,
sıkılı yumruk yok. Ve her önemli anda **önce dışarıya, sonra kendi eline bakar** —
dünyanın değiştiğini kendi bedeninden doğrular.

### 🚀 Vehicle Bible — ARAÇ

```
ARAÇ: İki kademeli fırlatma aracı. İSİMSİZ — gövdesinde hiçbir yazı,
      logo, bayrak, numara ya da marka YOKTUR.
YÜKSEKLİK: 68 metre. ÇAP: 4.2 metre.
GÖVDE: Mat kırağı-beyazı kriyojenik birinci kademe; yüzeyi ateşlemeden önce
       2-3 cm kalınlığında BUZ KABUĞU ile kaplıdır. Kademeler arası bant
       kömür siyahı. Tabanda dört adet siyah stabilizatör kanadı.
MOTOR: 7 adet motor (1 merkez + 6 halka). Metan-oksijen.
       ALEV: neredeyse ŞEFFAF mavi-beyaz bir çekirdek, içinde net görülebilen
       MACH ELMASLARI dizisi. Turuncu renk yalnızca pedden kalkan tozdan ve
       akkor haldeki kırıntılardan gelir — alevin kendisi turuncu DEĞİLDİR.
KAPSÜL: Aracın tepesinde tek kişilik kapsül. İç duvarlar kömür grisi kapitone,
        göstergeler tamamen soyut (yeşil oval nabız, amber çubuk, kayan camgöbeği
        segmentler) — RAKAM YOK, HARF YOK, METİN YOK.
        Kapsülün önünde 1.2 METRE GENİŞLİĞİNDE PANORAMİK GÖZLEM PENCERESİ,
        sol duvarda ayrıca 30 cm çapında yuvarlak bir yan pencere.
ZORUNLU NİTELİK: Asla minyatür/oyuncak görünmez. Kaynak dikişleri, panel
        çizgileri, kelepçe izleri, itfaiye suyu lekeleri, kullanılmış donanım
        dokusu görünür. Gerçek mühendislik oranları.
```

### 🌍 Mission Bible — UÇUŞ PROFİLİ (her sahnenin fizik temeli)

```
T-0.0   Ateşleme. 7 motor. Tutucular 3.1 saniye sonra bırakır.
T+7     Kule temiz. Hız 30 m/s. Buz kabuğu gövdeden bir perde halinde dökülür.
T+72    MAX-Q. Yükseklik 13.5 km, Mach 1.6, dinamik basınç 33 kPa.
        Gövde omuzunda yoğuşma konisi oluşur ve dağılır. En şiddetli titreşim.
T+2:38  Birinci kademe kesme + ayrılma. Yükseklik 68 km, hız 2.3 km/s.
        Hava YOK: ayrılan kademe alev kuyruğu bırakmaz, duman dağılmaz,
        donmuş yakıt kristalleri DÜMDÜZ doğrusal yollarda savrulur.
T+8:44  İkinci kademe kesme (MECO). Kesmeden hemen önce ivme 3.8 g.
        Kesmeden sonra 0 g — GEÇİŞ YARIM SANİYEDEN KISADIR.

⚠️ FİLMİN OMURGASI — SES:
 • Pedde: 165 dB. Ses değil, BASINÇ. Su perdesi, çatırdayan alev, gövde uğultusu.
 • 40 km üstünde: dışarıda ses YOKTUR. Sadece gövdenin içinden gelen yapısal uğultu.
 • MECO'dan sonra: MUTLAK SESSİZLİK. Filmin bütün duygusu bu geçiştedir —
   maksimum şiddetten mutlak sükûnete yarım saniyede.
```

### 🚫 Negative Bible

```
Kesme yok. Elde kamera sarsıntısı yok. Operatör sarsıntısı yok.
Minyatür/oyuncak görünüm yok. CGI havası yok. Hava fırçasız cilt yok.
Mükemmel simetri yok. Elde alet yok. Metin yok. Filigran yok.

KONSEPTE ÖZGÜ EKLER:
Gövdede YAZI YOK, logo YOK, bayrak YOK, marka YOK, seri numarası okunmuyor.
Gerçek bir kurum/şirket/ülke göstergesi YOK.
Alev turuncu-sarı bir ateş topu DEĞİLDİR: metan alevi şeffaf mavi-beyazdır.
Karikatür alev yok, kıvılcım yağmuru yok, patlama yok, hasar yok, arıza yok,
alarm yok, korku yok, çığlık yok, panik yok.
Uzayda: alev kuyruğu YOK, duman bulutu YOK, ses YOK, savrulan kıvılcım YOK,
yıldız kırpışması YOK. Uzay boşluğunda gökyüzü MUTLAK SİYAHTIR.
Lens flare YOK. Anamorfik mavi çizgi parlaması YOK. Yavaş çekim YOK.
```

---

## 🎬 SAHNE 0 — KANCA: T-EKSİ ÜÇ

_"İki saniye önce hiçbir şey oluyordu. Sonra dünya ateş aldı."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 0 of 6. Solo female flight engineer rocket launch film. MAXIMUM VIRAL IGNITION SHOCK.
Lens: 75mm, f/2.0, ISO 800.
Camera Distance: Approximately 0.9 metres, straight on, slightly below eye level, rigidly bolted to the capsule frame.

SUBJECT: A 38-YEAR-OLD WOMAN flight engineer — light olive-brown skin with clearly visible pores and a scatter of small dark moles along the left jawline, natural asymmetry with the right nostril sitting slightly wider than the left, a thin pale scar across the bridge of the nose, dark grey-brown eyes with faint fatigue shadows beneath them, a dry lower lip bitten pale at one corner, black hair pulled into a flat low knot with several strands escaped and pressed against her temples. Photographed as a real person, not CGI. She wears a matte ARCTIC-WHITE full-pressure launch suit with CHARCOAL-GREY articulated joints at the shoulders, elbows and knees, thick charcoal five-point harness webbing crossing her chest, scuffed pale wear along both forearms, a faded mission patch on the left chest with NO readable characters on it, and a half-erased serial block on the right thigh with no legible letters or numbers. A slim wrist screen on her left forearm shows abstract drifting segments only. Her helmet is a fully enclosed white shell with a FULLY TRANSPARENT curved visor carrying a faint breath-fog trace along its lower edge and one fine scratch across the upper left. BOTH HANDS ARE EMPTY. She is strapped into the seat, head back against the rest, chin tucked in, eyes open and steady, both gloved hands resting flat and loose on the armrests.

ENVIRONMENT / BACKGROUND: A cramped single-seat capsule interior. Charcoal-grey quilted padding on the walls, exposed bolt heads and worn panel seams, thick harness webbing. Two indicator panels are visible, both completely abstract — a green oval pulse and an amber bar, no digits, no letters, no text of any kind. On the left wall a round thirty-centimetre side window shows a pale grey pre-dawn sky and one edge of a distant service tower.

THE VIRAL MOMENT / REVEAL: The engines have just lit. Through the round window, hard METHANE BLUE-WHITE light is flooding into the capsule from below, so intense it flattens the shadows on her face and turns the charcoal padding pale. A second, warmer copper-orange glow washes up behind it from incandescent dust kicked off the pad. Every loose thing in frame is caught mid-vibration at high frequency: a slack harness strap end blurred against her chest, a fine haze of dust particles lifted off the padding and hanging in the air, a single bead of condensation crawling sideways along the inside of her visor. Her cheeks and lips have just begun to pull back from the first push of acceleration, and the blue-white light is reflected as two hard vertical bars in her eyes.

COMPOSITION: Horizontal 16:9. Her helmeted head fills the right third of the frame in tight profile-to-three-quarter. The round side window sits in the left third, blazing blue-white. The middle third is charcoal capsule wall crossed by vibrating harness webbing and floating dust.

LIGHTING: Two hard sources fighting inside a small dark box — a blue-white key blasting in through the window from below, and a copper-orange fill bouncing up off the lower wall. Everything keeps texture: skin pores, escaped hair strands, suit weave, quilted padding, scratched visor.

PHYSICS: The light arrives before the sound and before the motion — this is the instant between ignition and hold-down release. The vibration is high-frequency and structural, transmitted through the seat.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no brand marks, no readable digits on any panel, no orange fireball, no cartoon flame, no sparks, no alarm lights, no fear or panic expression, no lens flare, no handheld shake, no tool in her hands, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm, fixed at 0.9 metres, rigidly bolted to the capsule frame, straight on.

At 0s — Interior of a cramped single-seat capsule. A woman in a matte arctic-white pressure suit and clear-visored helmet sits strapped in, hands loose on the armrests, breathing slowly. Through a round side window, a pale grey pre-dawn sky. Everything is completely still and quiet.
At 2s — A slack harness strap end begins to BUZZ against her chest, too fast to follow. Fine dust lifts off the quilted padding and hangs in the air. A bead of condensation on the inside of her visor starts crawling sideways.
At 4s — The whole capsule enters a high-frequency structural vibration — the image shudders as a rigid unit, the frame never swings or tilts. She tucks her chin in and flattens her hands on the armrests. She does not brace.
At 5.5s — IGNITION. Hard methane blue-white light floods in through the round window from below and drowns the interior, flattening every shadow on her face; a copper-orange glow washes up behind it. Two hard vertical bars of light appear in her eyes.
At 7s — The hold-downs release. She is pushed back into the seat — her cheeks and lips pull back, her shoulders press into the rest, the floating dust slams downward all at once. She keeps her eyes open.
By 8s — Hard cut to Scene 1.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted vibration only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 1 — KULE TEMİZ

_"Altmış sekiz metrelik bir şey, buzunu üstünden atarak kalkıyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 1 of 6. Rocket launch film, exterior. MAXIMUM VIRAL ICE-SHEDDING LIFTOFF.
Lens: 200mm, f/5.6, ISO 100.
Camera Distance: Approximately 900 metres from the pad, ground level at 1.2 metres height, tracking upward, rigidly mounted.
(No human figure is visible in this frame — she is sealed inside the capsule at the top of the vehicle. Do not render any person.)

SUBJECT: A sixty-eight metre two-stage launch vehicle, 4.2 metres in diameter, lifting off. Its first stage is matte frost-white and still sheeted in a two-centimetre crust of ICE; the interstage band is charcoal black; four black stabiliser strakes sit at the base. The hull carries NO text, NO logo, NO flag, NO brand mark and no readable numbers anywhere — only weld seams, panel lines, clamp scars and water stains. Seven engine bells at the base burn a near-TRANSPARENT METHANE BLUE-WHITE, with a clear row of Mach diamonds standing inside each exhaust column.

ENVIRONMENT / BACKGROUND: A flat coastal launch site under a pale grey pre-dawn sky. The service tower stands at the right of frame, already falling behind the vehicle, its arms swung back. Below, the flame trench boils with a vast white cloud of water-deluge steam that spreads sideways across the entire width of the frame. Far behind, a flat dark sea line. No crowds, no vehicles, no structures other than the tower.

THE VIRAL MOMENT / REVEAL: The ice crust is coming off the tank ALL AT ONCE — a shimmering curtain of white plates and glittering shards peeling away down the full sixty-eight metres of the body and falling back into the steam, catching the blue-white engine light as they tumble. Where the exhaust hits the pad, a band of COPPER-ORANGE incandescence flares along the ground from burning dust and debris — the only warm colour in the frame, sharply separate from the cold blue flame above it. The vehicle is fifty metres up and perfectly vertical, and the whole lower third of the widescreen frame is boiling white steam.

COMPOSITION: Horizontal 16:9. The vehicle stands in the LEFT THIRD, rising, small enough that its full sixty-eight metres reads as real scale against the tower. The tower occupies the right third. The remaining width is filled by the horizontally spreading steam sheet and the falling ice curtain. Horizon low, in the bottom fifth.

LIGHTING: Flat cold pre-dawn ambient over everything, blown out from below by the blue-white engine light, which throws hard rim highlights up the white hull and lights the underside of the steam cloud. Copper-orange ground incandescence bleeds into the base of the steam only.

PHYSICS: Real thrust-to-weight — the vehicle accelerates slowly and heavily at first, not like a firework. The steam spreads laterally because it is deluge water flashing, not smoke. The ice falls straight down.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no brand marks, no readable numbers on the hull, no orange fireball, no cartoon flame, no explosion, no damage, no debris strike, no crowds, no lens flare, no miniature or toy look, no handheld shake, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 200mm, rigidly mounted at 900 metres from the pad, height 1.2m, tracking upward at the vehicle's rate.

At 0s — A sixty-eight metre frost-white launch vehicle sits on the pad in the left third of frame, service tower at the right, the flame trench below already boiling with white deluge steam. Seven engine bells burn a transparent methane blue-white with visible Mach diamonds.
At 1.5s — It begins to move, slowly and heavily — the acceleration of something enormous, not of a firework. The steam sheet spreads sideways across the full width of the frame.
At 3s — The ice crust lets go all at once: a shimmering curtain of white plates and glittering shards peels away down the whole length of the body and falls straight back into the steam, flashing blue-white as it tumbles.
At 5s — The vehicle clears the top of the tower. The camera tracks up with it, rigid, the horizon staying dead level. A band of copper-orange incandescence flares along the pad where the exhaust hits the ground.
At 6.5s — It rises out of the steam entirely and the exhaust column stretches to a long straight blue-white blade beneath it. The tower falls out of the bottom of frame.
By 8s — No cuts within the shot.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted vibration only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 2 — MAX-Q

_"Havanın seni en sert tuttuğu an. Ve tam orada beyaz bir yaka takıyorsun."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 2 of 6. Rocket launch film, on-vehicle camera. MAXIMUM VIRAL CONDENSATION-CONE SHOCK.
Lens: 32mm Cooke anamorphic, f/8, ISO 200.
Camera Distance: Approximately 0.4 metres from the hull, bolted to the interstage band and looking DOWN the length of the body toward the ground.
(No human figure is visible in this frame — she is sealed inside the capsule above the camera. Do not render any person.)

SUBJECT: The matte frost-white body of a 4.2 metre diameter launch vehicle, seen from a camera bolted to its own interstage, the hull running as a long curved wall diagonally across the frame with weld seams, panel lines and clamp scars in sharp foreground detail. The ice crust is completely gone now; the bare white hull shows fine streaking from the airflow. NO text, NO logo, NO flag, NO brand mark and no readable numbers anywhere on the hull.

ENVIRONMENT / BACKGROUND: Thirteen and a half kilometres below and behind, the ground reads as a flat patchwork of dark coastline, pale sandbanks and a scattered deck of low white cloud, with a faint curve already showing at the far edge. At the top of the frame the sky has already turned from pale grey-blue to deep indigo. No horizon glow, no sunrise gradient.

THE VIRAL MOMENT / REVEAL: A translucent WHITE CONDENSATION CONE has formed around the vehicle's shoulder and is standing off the hull as a smooth vapour collar, thin enough that the panel lines are still visible through it. The airflow drags it backward into fine parallel streaks along the body. The hull itself is visibly SHUDDERING — the near foreground edge of the metal is doubled and blurred by high-frequency vibration while the distant ground stays pin-sharp. Below and behind, the blue-white exhaust column runs away downward to a vanishing point, straight as a drawn line, thirteen kilometres long.

COMPOSITION: Horizontal 16:9. The hull occupies the left third as a huge curved white wall running from the top-left corner to the bottom edge. The condensation collar wraps across the upper middle. The remaining two thirds of the widescreen frame is the falling-away Earth and the long straight exhaust column. Nothing is centred.

LIGHTING: Hard high-altitude sunlight raking across the white hull from one side, blowing the lit edge nearly to pure white while the shadowed side of the body stays cold blue-grey. The vapour collar catches the light as a soft pearl band. The indigo sky at the top of frame is dark enough that the hull edge cuts against it hard.

PHYSICS: The cone is condensation from the local pressure drop at transonic speed — it forms, thins and collapses within seconds. It is a collar of vapour, not smoke and not fire.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no brand marks, no readable numbers, no fire on the hull, no sparks, no smoke trail, no explosion, no damage, no lens flare, no miniature or toy look, no sunrise gradient, no handheld shake, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm anamorphic, bolted to the vehicle's interstage at 0.4 metres from the hull, looking down the body.

At 0s — On-vehicle view. The huge curved white hull of a launch vehicle runs diagonally across the left of frame; thirteen kilometres below, the coastline and a deck of low cloud fall away; the sky at the top of frame is already deep indigo. A long straight blue-white exhaust column runs away downward.
At 2s — A translucent white condensation collar forms around the vehicle's shoulder and stands off the hull, thin enough that the panel lines show through it, dragged backward into fine parallel streaks by the airflow.
At 3.5s — Maximum vibration. The near edge of the hull doubles and blurs at high frequency as a rigid unit while the ground far below stays pin-sharp. The frame never swings, tilts or drifts.
At 5s — The collar thins, tears backward and collapses off the body in under a second, leaving the bare white hull streaking.
At 6.5s — The vibration eases. The sky at the top of the frame darkens further toward black; the Earth's curve becomes clearly visible along the far edge of the widescreen frame.
By 8s — No cuts within the shot.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted vibration only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 3 — AYRILMA

_"Altmış sekiz kilometre. Ses burada kalıyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 3 of 6. Rocket launch film, on-vehicle camera. MAXIMUM VIRAL STAGE SEPARATION IN VACUUM.
Lens: 32mm Cooke anamorphic, f/8, ISO 400.
Camera Distance: Approximately 3 metres, bolted to the second stage and looking BACK along the flight path at the separating first stage.
(No human figure is visible in this frame — she is sealed inside the capsule above the camera. Do not render any person.)

SUBJECT: The spent first stage of a launch vehicle falling away from camera — a sixty-metre matte frost-white cylinder, scorched copper-brown along its last eight metres from the exhaust, its seven engine bells now dark and glowing only a dull deep orange from residual heat. It is beginning a slow, heavy tumble. Its hull carries NO text, NO logo, NO flag, NO brand mark and no readable numbers — only weld seams, panel lines, clamp scars and heat discolouration. In the near foreground, the charcoal-black interstage ring of the second stage frames the bottom corner of the shot.

ENVIRONMENT / BACKGROUND: Sixty-eight kilometres up. The sky is ABSOLUTE BLACK with hard, non-twinkling stars. Across the entire width of the frame below, the Earth's ULTRAMARINE limb curves — deep ocean blue, white cloud swirls, a pale sand-coloured landmass at one edge — bounded by a thin luminous band of atmosphere that fades from cyan to indigo to black in a narrow ribbon.

THE VIRAL MOMENT / REVEAL: The separation is happening in complete airlessness and it looks nothing like an explosion. A ring of soft white gas puffs out from the interstage and pushes the spent stage backward — and that gas does not billow, does not curl and does not form a cloud; it expands in a clean, thinning sphere and is gone. A spray of frozen propellant crystals drifts away in DEAD-STRAIGHT LINES, each one travelling on its own perfectly straight path, glittering in the raw sunlight. There is no flame trail, no smoke, no sparks. The falling stage is utterly silent and already fifty metres away, turning slowly end over end against the blue Earth.

COMPOSITION: Horizontal 16:9. The Earth's curve runs across the FULL WIDTH of the frame in the lower half, filling the widescreen with ultramarine. The falling first stage sits in the upper right third against black. The charcoal interstage ring cuts the bottom-left corner as foreground. The straight crystal trails run diagonally across the empty middle.

LIGHTING: Raw undiffused sunlight from one side — brutally hard, with pure black shadow and no fill of any kind on the shadow sides. A strong cold ultramarine bounce comes UP from the Earth onto the underside of the falling stage. The stars stay hard points and do not twinkle.

PHYSICS: No atmosphere means no drag, no billowing and no sound — separation debris travels in straight lines, gas disperses instantly, and the tumble is slow and constant because nothing damps it.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no brand marks, no readable numbers, no flame trail, no smoke cloud, no billowing gas, no sparks, no explosion, no damage, no debris strike, no twinkling stars, no atmospheric haze in vacuum, no lens flare, no miniature or toy look, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm anamorphic, bolted to the second stage at 3 metres, looking back along the flight path.

At 0s — On-vehicle view looking back. The Earth's ultramarine curve fills the whole width of the lower frame under an absolutely black sky with hard unmoving stars. The charcoal interstage ring frames the bottom-left corner. The first stage is still attached.
At 1.5s — The engines shut down. The long blue-white exhaust column simply STOPS — it does not fade or sputter, it is there and then it is not.
At 3s — Separation. A ring of soft white gas puffs from the interstage and pushes the sixty-metre spent stage backward; the gas expands as a clean thinning sphere and vanishes instead of billowing.
At 4.5s — A spray of frozen propellant crystals drifts out across the frame, every one of them travelling on a dead-straight line, glittering in raw sunlight. Nothing curls. Nothing falls.
At 6s — The spent stage begins a slow heavy tumble end over end, its scorched copper-brown skirt and dull orange engine bells turning against the blue Earth, already fifty metres away and receding. Absolute silence.
At 7.5s — The second stage engine lights behind camera: a soft blue-white glow washes onto the interstage ring in the foreground, with no sound and no shockwave.
By 8s — No cuts within the shot.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted vibration only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 4 — VİRAL DORUK: KESİLME

_"3.8 g. Sonra yarım saniyede sıfır. Kolları kendiliğinden havalanıyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 4 of 6. Solo female flight engineer rocket launch film. MAXIMUM VIRAL ENGINE-CUTOFF ZERO-G SHOCK.
Lens: 75mm, f/2.0, ISO 640.
Camera Distance: Approximately 1.1 metres, slightly above eye level, rigidly bolted to the capsule frame.

SUBJECT: A 38-YEAR-OLD WOMAN flight engineer — light olive-brown skin with clearly visible pores and a scatter of small dark moles along the left jawline, natural asymmetry with the right nostril sitting slightly wider than the left, a thin pale scar across the bridge of the nose, dark grey-brown eyes with faint fatigue shadows beneath them, a dry lower lip bitten pale at one corner, black hair pulled into a flat low knot with several strands escaped and pressed against her temples. Photographed as a real person, not CGI. She wears a matte ARCTIC-WHITE full-pressure launch suit with CHARCOAL-GREY articulated joints at the shoulders, elbows and knees, thick charcoal five-point harness webbing crossing her chest, scuffed pale wear along both forearms, a faded mission patch on the left chest with NO readable characters on it, and a half-erased serial block on the right thigh with no legible letters or numbers. A slim wrist screen on her left forearm shows abstract drifting segments only. Her helmet is a fully enclosed white shell with a FULLY TRANSPARENT curved visor carrying a faint breath-fog trace along its lower edge and one fine scratch across the upper left. BOTH HANDS ARE EMPTY. She is still pressed into the seat from the acceleration that has just ended — but her forearms have LIFTED off the armrests on their own and hang in the air, fingers slightly open, and her face has just begun to release.

ENVIRONMENT / BACKGROUND: The charcoal-grey quilted capsule interior, harness webbing, abstract indicator panels showing only a green oval pulse and an amber bar with no digits and no letters. Through the wide panoramic window at the left of frame: ABSOLUTE BLACK, and across the bottom of that window a curved band of ULTRAMARINE Earth edged with a thin luminous cyan atmosphere line.

THE VIRAL MOMENT / REVEAL: The engine has cut and the acceleration has gone from 3.8 g to ZERO in less than half a second, and everything loose in the capsule is caught at the top of that transition. Her arms float. Her shoulders have risen off the seat until the harness webbing has gone taut across her chest and stopped them. The escaped strands of hair at her temples have lifted away from her skin and stand out from her head. A slack lanyard end, a strap tail and a fine scatter of dust hang motionless in mid-air across the middle of the frame, all of them suspended at the same instant. Her cheeks, dragged back and flattened a second ago, have just relaxed — her mouth is slightly open, her eyes are wide and completely calm.

COMPOSITION: Horizontal 16:9. She is in the RIGHT THIRD, head and shoulders. The panoramic window with black space and the ultramarine Earth band fills the LEFT THIRD. The middle third is the empty air between them, occupied only by the floating lanyard, strap tail and suspended dust.

LIGHTING: Cold ultramarine light from the Earth through the window is now the strongest source in the capsule, laid across the left side of her helmet and jaw. A faint warm amber from the abstract panel fills the other side. No engine light — that source has just gone out, and the interior is noticeably darker and calmer than one second earlier.

PHYSICS: This is not slow motion. The objects are genuinely weightless, drifting at the small speeds they already had — nothing rises fast, nothing spins, nothing bounces.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no readable digits on any panel, no alarm lights, no fear or panic expression, no screaming, no slow-motion look, no fast-rising or spinning objects, no lens flare, no tool in her hands, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 75mm, fixed at 1.1 metres, rigidly bolted to the capsule frame, slightly above eye level.

At 0s — Interior. A woman in an arctic-white pressure suit is pressed hard back into her seat under heavy acceleration: cheeks dragged flat, hands weighted onto the armrests, breathing short. The capsule is vibrating as a rigid unit. Through the panoramic window at the left, black space and a band of ultramarine Earth.
At 2s — The vibration and the load keep building. Her chin is tucked, her eyes stay open. She does not brace, does not grip, does not panic.
At 3.5s — ENGINE CUTOFF. Everything stops at once — the vibration ends, the noise ends, the weight ends. In under half a second the capsule goes from maximum violence to absolute stillness.
At 4.5s — Her forearms float up off the armrests on their own, fingers opening. Her shoulders rise off the seat until the harness webbing pulls taut and stops them. The escaped strands of hair at her temples lift away from her skin and stand out.
At 6s — A slack lanyard end, a strap tail and a fine scatter of dust drift up into the middle of the frame and simply hang there, moving at almost nothing. Nothing spins, nothing bounces.
At 7s — Her face releases: the flattened cheeks relax, her mouth opens slightly, and she turns her head toward the window where the ultramarine Earth is. She looks at the Earth, then down at her own floating hand.
By 8s — Hard cut to Scene 5.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted mounting only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎬 SAHNE 5 — TESLİM: PENCERE

_"Dokuz dakika önce oradaydı. Şimdi ona bakıyor."_

### 📸 GÖRSEL PROMPT

```
Cinematic sci-fi still image — Scene 5 of 6. Solo female flight engineer rocket launch film.
Lens: 32mm Cooke anamorphic, f/4, ISO 800.
Camera Distance: Approximately 2.2 metres, level, rigidly bolted to the capsule frame, wide interior.

SUBJECT: A 38-YEAR-OLD WOMAN flight engineer — light olive-brown skin with clearly visible pores and a scatter of small dark moles along the left jawline, natural asymmetry with the right nostril sitting slightly wider than the left, a thin pale scar across the bridge of the nose, dark grey-brown eyes with faint fatigue shadows beneath them, a dry lower lip bitten pale at one corner, black hair pulled into a flat low knot with several strands escaped and now lifted away from her temples in zero gravity. Photographed as a real person, not CGI. She wears a matte ARCTIC-WHITE full-pressure launch suit with CHARCOAL-GREY articulated joints at the shoulders, elbows and knees, thick charcoal five-point harness webbing now released and floating, scuffed pale wear along both forearms, a faded mission patch on the left chest with NO readable characters on it, and a half-erased serial block on the right thigh with no legible letters or numbers. A slim wrist screen on her left forearm shows abstract drifting segments only. Her helmet is a fully enclosed white shell with a FULLY TRANSPARENT curved visor carrying a faint breath-fog trace along its lower edge and one fine scratch across the upper left. BOTH HANDS ARE EMPTY. She is FLOATING free of the seat, drifting toward the window, her body angled slightly off vertical, one gloved fingertip touching the wall to steady herself, face close to the glass.

ENVIRONMENT / BACKGROUND: The charcoal-grey quilted capsule interior, dark now, with the released harness straps floating out from the empty seat like weeds in water. The abstract indicator panels glow faintly — a green oval pulse and an amber bar, no digits, no letters. A small dust mote drifts past her shoulder.

THE VIRAL MOMENT / REVEAL: The 1.2-metre panoramic window fills the frame with EARTH. The planet's curve runs edge to edge across the widescreen: deep ultramarine ocean, white cloud spirals turning over it, a pale sand-brown coastline, and a thin luminous ribbon of atmosphere along the limb fading cyan to indigo to absolute black. The terminator line crosses the view diagonally, and on the night side of it, webs of warm gold city light spread out across the dark like veins. All of that is reflected, sharp and curved, across the whole surface of her visor — so the Earth appears twice in the same frame, once through the window and once on her face. She is completely still.

COMPOSITION: Horizontal 16:9. The window and its Earth occupy the full width of the upper two thirds. She floats in the lower right third, small against it, back three-quarters to camera. The empty seat and floating harness straps sit at the lower left. The scale relationship — one small human, one whole planet, side by side across the widescreen — is the shot.

LIGHTING: The Earth is the only real light source: a cold ultramarine wash across her helmet, shoulders and the capsule walls, with a faint warm gold touch from the city lights on the night side falling across her visor. Deep soft shadow everywhere the planet does not reach. Everything holds texture: skin pores, escaped hair, suit weave, quilted padding, scratched visor.

PHYSICS: True weightlessness — her hair is lifted, the straps float in slow arcs, her body drifts at a walking-slow rate, and her single fingertip on the wall is the only thing controlling her.

NEGATIVE: See Negative Bible. No text, no logos, no flags, no readable digits on any panel, no stars visible through the daylit side of the window, no twinkling, no lens flare, no fear expression, no fast motion, no tool in her hands, no other figures, no watermark.
Output: 16:9, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Horizontal 16:9. Single continuous shot, 0 cuts, 8 seconds. Lens: 32mm anamorphic, very slow push-in from 2.2 metres, rigidly mounted, level.

At 0s — Wide interior. The harness straps float out from an empty seat. A woman in an arctic-white pressure suit drifts free through the dark capsule toward a 1.2-metre panoramic window that is filled edge to edge with the ultramarine curve of the Earth.
At 2s — She arrives at the glass and stops herself with a single gloved fingertip against the wall. Her body settles at a slight angle and hangs there. The escaped strands of her hair stand out from her temples and move slowly.
At 3.5s — The whole Earth turns beneath the window: cloud spirals rolling, a pale coastline sliding past, the thin luminous atmosphere ribbon holding along the limb.
At 5s — The terminator line crosses into view and the night side comes with it — webs of warm gold city light spreading across the dark, reflected sharp and curved across the entire surface of her visor.
At 6.5s — She goes completely still. Her breath fogs the lower edge of the visor and clears again. A single dust mote drifts past her shoulder. She does not reach out and she does not turn back to the seat.
By 8s — No cuts within the shot. Hold the wide frame.

No dialogue. No speaking. No lip sync. No subtitles. No text. No logos. No watermark. No handheld shake, no operator shake — rigid rig-mounted mounting only. No focus breathing. Kodak Vision3 color science. Photorealistic live-action cinematography.
```

---

## 🎶 Müzik Promptu (Tek Global Tema)

```
Single instrumental track for Suno / Udio, 48 seconds, no vocals, no lyrics.

GENRE: Ambient cinematic minimalism built around one physical event — a slow
crushing build followed by a total, sudden emptiness.

INSTRUMENTATION — FOUR LAYERS ONLY:
1. A sub-bass drone starting at 38 Hz, which SLOWLY RISES in pitch and density
   across the first 32 seconds until it is a wide, physical low roar. This is
   the vehicle. It is felt in the chest, not heard.
2. A dry low pulse — a single damped struck note — beginning at 8 seconds at
   one hit per 2 seconds and accelerating imperceptibly to one hit per second
   by 30 seconds. It never becomes a drum beat and never plays a rhythm.
3. A high sustained string harmonic, entering at 16s, thin and tense, holding
   a single unresolved note that slowly bends a quarter tone upward.
4. From 40s, a soft wide pad — warm, slow, no attack — that simply appears
   underneath everything.

TEMPO: No fixed grid. The pulse's acceleration is the only clock and it must
feel biological rather than metronomic.

KEY: D minor, deliberately unresolved — no final cadence.

DYNAMIC SPREAD:
  0-8s   (Hook)    near-silence, room tone only, then at 5.5s the drone
                   arrives HARD and full.
  8-16s  (Scene 1) drone at full width; the low pulse enters slowly.
  16-24s (Scene 2) high string harmonic enters; drone thickens and grows
                   rougher; the pulse quickens. Maximum pressure begins.
  24-32s (Scene 3) everything stays loud but the texture opens out and gets
                   colder — reverb tail lengthens as the air thins.
  32-40s (Scene 4) VIRAL PEAK — at exactly 35.5s EVERY LAYER STOPS DEAD.
                   Two full seconds of near-total silence, only a faint hiss.
                   Then one single high string note enters alone and hangs.
                   The peak is achieved by CUTTING, not by adding.
  40-48s (Scene 5) the warm pad rises under the single note and widens. The
                   track ends without resolving — it stops the way an engine
                   stops. No fade, no ending chord, no final swell.

REFERENCE FEEL: the restraint of Jóhann Jóhannsson's quieter chamber writing,
and the patience of Hans Zimmer's slowest sustained passages. Do not quote,
sample or reproduce any melody, motif or lyric from either.

NO vocals, NO lyrics, NO conventional melody, NO drums, NO percussion kit,
NO braam, NO riser, NO reversed cymbal, NO countdown voice, NO radio chatter.
```

---

## 🖼️ KAPAK PROMPTU (1280×720) 🆕

Kaynak an: **S1** — buz perdesi. Duygusal zirve S4 (kesilme) ama 120 px'te
okunan şekil bu: *dikey araç + yatay buhar tabakası + dökülen buz.*

```
Cinematic photorealistic still image, 1280x720, 16:9.

A 68-metre methane-fuelled launch vehicle stands perfectly vertical fifty metres above
the pad, matte white hull with visible panel lines and frost scarring. Its ice crust is
peeling away all at once — a shimmering curtain of white plates and glittering shards
falling back into the steam, catching hard methane blue-white engine light as they
tumble. Where the exhaust meets the pad, a narrow band of copper-orange incandescence
flares along the ground from burning dust, sharply separate from the cold blue flame
above it.

The exhaust plume is a continuously evolving event, expanding and shedding shock
diamonds — never a static painted flame shape. Every ice flake carries its own
velocity; nothing hangs motionless.

COMPOSITION: The vehicle stands in the LEFT THIRD, small enough that its full
sixty-eight metres reads as real scale against the launch tower in the right third. The
remaining width is horizontally spreading white steam and the falling ice curtain.
Horizon low, in the bottom fifth. Nothing is centred.

LIGHTING: Methane blue-white from the engines below, copper-orange ground band, frost
white, absolute pre-dawn black sky. Hard-edged light, no bloom, no glow filter, no lens
flare.

NEGATIVE: No static painted flame, no frozen exhaust, no motionless particles, no
miniature or toy-like vehicle, no bloom, no glow filter, no lens flare, no slow motion,
no text, no letters, no digits, no HUD overlay, no lens data, no name label, no
watermark.

Output: 16:9, 1280x720, no text, no watermark.
```

**120 px testi:** okunması gereken tek şekil → *dikey beyaz araç + yatay
buhar tabakası.* Buz parçaları okunmazsa sorun değil; aracın dikeyliği
okunmazsa kapak başarısızdır.

> Kapak denetimi 120 px posta pulu testiyle elle yapılır (KAPAK_QA rubriği 12.08.2026'da kaldırıldı).

---

## 📣 BAŞLIK VE AÇIKLAMA PAKETİ 🆕

**Başlık alternatifleri** (≤ 40 karakter):

```
1. Yörüngeye dokuz dakika
2. Ayrılma anında hiç ses yok
3. Bu dokuz dakikada ne oluyor?
```

**Açıklama:**

```
Fırlatmadan yörüngeye dokuz dakika. Kapsülün içinde tek bir insan, dışarıda
sırayla gerçekleşen dört fizik olayı: buz kabuğunun dökülmesi, max-Q'da
yoğuşma konisi, vakumda sessiz ayrılma ve motor kesilmesiyle başlayan
ağırlıksızlık.

Dayanak: gerçek fırlatma telemetrisi. Vakumda duman kıvrılmaz — düz çizgide
dağılır. Ayrılma sessizdir çünkü ses taşıyacak hava yoktur.
```

**Hashtag paketi:**

```
geniş:    #shorts #space #rocket
niş:      #spaceflight #maxq #stageseparation #orbit #aifilm
özel:     #ninemi̇nutes #methalox #vacuumphysics
```

**Sabitlenecek ilk yorum:**

```
Ayrılma sahnesindeki gaz halkası kıvrılmıyor, düz çizgide dağılıyor —
vakumda duman böyle davranır. Filmlerin çoğu bunu yanlış yapar.
```

> ⚠️ Metin **kareye yazılmaz** — başlık platformda yazılır (Ders 9 / 34 / 45).

---

## 🔒 Master Cinema Lock (bu doküman için uyarlanmış)

```
Ultra-photorealistic live-action cinematography. Natural human motion only.
Perfect anatomical consistency. No CGI look. No game-engine rendering.
No plastic skin. No exaggerated facial expressions. Physically accurate lighting.
Real engineering scale — never miniature, never toy-like.
Slow cinematic pacing. One uninterrupted shot. No focus breathing. No zoom.
All vibration is rigid rig-mounted vehicle vibration — no handheld shake,
no operator shake, no whip pans, no lens flare.
High-end IMAX science fiction cinematography. Kodak Vision3 color science.
Academy Award-level visual effects integrated invisibly into live action.
Every frame should look like a real photograph captured on location rather
than generated.
```

---

## ✅ Tutarlılık Kontrol Listesi

- [x] Format **yatay 16:9** — her görsel promptta `COMPOSITION: Horizontal 16:9` ve `Output: 16:9, 4K`, her video promptunda `Horizontal 16:9` yazılı.
- [x] Yatay kompozisyon bilinçli kullanıldı: dikey bir roket hiçbir sahnede ortada değil — kadranın kalan genişliğini buhar düzlüğü (S1), Dünya'nın düşüşü (S2), Dünya'nın eğrisi (S3), pencere-yüz karşıtlığı (S0, S4) ve edge-to-edge gezegen (S5) dolduruyor.
- [x] Her sahnede **1 görsel + 1 video promptu** — toplam 6 görsel, 6 video promptu.
- [x] Karakter açıklaması **üç iç mekan promptunda (S0, S4, S5) birebir aynı kelimelerle** tekrarlandı. Üç dış çekimde (S1, S2, S3) karakter bloğu bilinçli olarak YOK ve `Do not render any person` talimatı var — model karakteri roketin dışına yerleştirmesin diye.
- [x] Renk paleti bu konsept için özgün: **metan mavi-beyazı + kavruk bakır turuncusu + kırağı beyazı + okyanus ultramarini + mutlak vakum siyahı.** Önceki dört dosyanın paletiyle çakışmıyor.
- [x] Duygu omurgası özgün: **maksimum şiddetten mutlak sessizliğe yarım saniyede geçiş** (MECO). Viral doruk ekleyerek değil, KESEREK kuruluyor — müzik promptu da 35.5s'de tamamen susuyor.
- [x] Diyalog, geri sayım sesi, telsiz konuşması, metin, altyazı yok. Karakterin adı ve milliyeti hiçbir promptta geçmiyor [Ders 34].
- [x] **Gövdede yazı/logo/bayrak/marka yok** — gerçek bir kurum, ülke ya da şirket hiçbir promptta ima edilmiyor. Araç tamamen kurgusal.
- [x] Hook sahnesi Viral Zamanlama kuralına uyuyor: 0-2 merak (sessiz kabin) · 2-5 ipuçları (titreyen kayış, kalkan toz) · 5-7 reveal (ateşleme ışığı) · 7-8 tek güçlü görüntü (koltuğa bastırılan yüz).
- [x] Negative Bible her görsel promptta, Master Cinema Lock kısa formu her video promptunun sonunda mevcut.
- [x] Eller **6 sahnenin 6'sında da boş** — hiçbir promptta alet yok, hiçbir yerde kumandaya yapışmış el yok.
- [x] Lens kilidi karışmadı: 32mm (S2, S3, S5) · 75mm (S0, S4) · 200mm (S1). Kamera mesafesi her promptta metre olarak yazılı.

```
⚠️ ÜRETİM NOTU — EN YÜKSEK RİSKLER

1. MODEL TURUNCU ATEŞ TOPU YAPAR
   "Rocket launch" gören model refleks olarak devasa turuncu-sarı alev,
   kıvılcım yağmuru ve patlama ekler. Bu filmin alevi METAN alevidir:
   neredeyse ŞEFFAF MAVİ-BEYAZ, içinde Mach elmasları. Turuncu SADECE
   pedden kalkan akkor tozdadır. Her promptta hem pozitif ("transparent
   methane blue-white, Mach diamonds") hem negatif ("no orange fireball,
   no cartoon flame, no sparks") yazılı.
   → Turuncu ateş topu çıkarsa AT ve yeniden üret.

2. MODEL UZAYA HAVA KOYAR
   S3'te model ayrılan kademeye alev kuyruğu, kıvrılan duman ve kıvılcım
   ekler. 68 km'de HAVA YOKTUR: gaz kıvrılmaz, küre gibi genişleyip yok
   olur; kristaller DÜMDÜZ doğrusal yollarda gider; ses yoktur.
   "no billowing gas, no flame trail, no smoke cloud" satırı silinmemeli.

3. MODEL SIFIR YERÇEKİMİNİ YAVAŞ ÇEKİM SANIR
   S4 ve S5'te model her şeyi ağır çekim yapar ya da nesneleri hızla
   yukarı fırlatır. Sıfır g YAVAŞ ÇEKİM DEĞİLDİR — nesneler zaten sahip
   oldukları küçük hızla, gerçek zamanda sürüklenir. "This is not slow
   motion" satırı S4 görselinde kalmalı.

4. MODEL GÖVDEYE YAZI YAZAR
   Roket gövdesi modelin en çok metin/logo/bayrak halüsinasyonu yaptığı
   yüzeydir. Her dış çekim promptunda "NO text, NO logo, NO flag, NO brand
   mark, no readable numbers" hem SUBJECT hem NEGATIVE bloğunda tekrarlanıyor.
   → Gövdede herhangi bir karakter belirirse AT ve yeniden üret.

5. PROMPT UZUNLUĞU
   İç mekan görsel promptları ~3.100-3.400 karakter (karakter bloğu tam
   tekrar ediyor), dış çekimler ~2.200-2.500. Video promptları ~1.500-1.900
   — rahat bandda. Görselde hata alırsan kesilecek yer: ENVIRONMENT ve
   PHYSICS satırları. ASLA kesme: karakter bloğu, alev tarifi, "no text on
   the hull" satırı, negatif satırı.
```

---

🚀 **NINE MINUTES — Dokuz Dakika**
_"Dokuz dakika. Bir dünyayı geride bırakmak için gereken bütün süre bu."_
