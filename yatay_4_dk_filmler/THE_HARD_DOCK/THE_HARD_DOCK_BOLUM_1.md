# 🎬 THE_HARD_DOCK — BÖLÜM 1  (S01 – S12)

> **Bu dosyada YALNIZ sahne blokları vardır.** Plan, karakter kartı, çapa üçlüsü,
> Bible'lar ve kilitler `THE_HARD_DOCK_PLAN.md`'de durur. Her prompt self-contained'dır.
> Süre: 12 × 10 s = 120 s (0:00 – 2:00). BÖLÜM 2: `THE_HARD_DOCK_BOLUM_2.md` (S13-S24).
> Üretim: önce IMAGE (t = 0 karesi), onaylanınca I2V VIDEO [D179].

---

## ⚠️ BÖLÜM 1 ÜRETİM NOTLARI (promptlardan önce oku)

```
① VİZÖR TEK NİTELİK [D197 · D79 · D95 · D146]: berrak düz panel, görünür koyu-gri
   çerçeve, üst kenarda tek parlama çizgisi, yaka halkası görünür. "opaque / mirrored /
   pitch-black visor" bu dosyada 0 kez geçer. (Plan §BİLİNÇLİ SAPMALAR ①.)
② KURULUM METNİ HARF BAŞINA BİREBİR [ACI_YAYI §7 ⑥]: A · B · C · D · E kamera
   cümleleri kelimesi kelimesine aynıdır; dönen sahne sonuna "— the same position,
   height and lens as Scene N." ekler. KÜME bu bölümde yok (S14-15 · S22-23 BÖLÜM 2'de).
③ GÜNEŞ SABİT [D201]: istasyonun arkasında, eksenin üstünde, kadraj dışı. Dış çekimde
   istasyon ARKADAN ışıklı (beyaz kontur + alttan gezegen turuncusu); kokpitte turuncu
   ışık pencereden ALÇAKTAN girer, tek beyaz kabin lambası yüzü aydınlatır.
④ İNSANSIZ SAHNE (S01 · S05 · S06 · S07): "Human count in this frame: zero" + NEGATIVE
   bloğu 900 karakterin ALTINDA [KART 10 · Cold Burn S8].
⑤ SAYI SESTE, RAKAM EKRANDA 0 [D82 · D50]: ekran/gösterge/yazı yok. Bilgi kanalı:
   dört lambanın SAYISI · pencere geometrisi · makinenin sesi. Konuşanın adı promptta
   geçmez [D34] — "the ship computer's flat synthetic voice".
⑥ ÖLÇÜ GÖVDEDE YOK [D138]: metre yalnız KAMERA cümlesinde. Oranlar halka eni,
   kask eni, gemi boyu, avuç/parmak eniyle.
⑦ KARAR BEDENDE [D202 · OYUNCULUK §3]: bakış eli önceler (helmet turns first, glove
   follows a second later) · alışkanlık: her girdiden önce işaret parmağı iki tık
   (S02 · S08 · S10) · baş kilidi (S09 · S11) · nefes omuz hattında.
⑧ İMAJ t = 0 [D179]: her IMAGE promptu VIDEO'nun 0.0s satırıyla aynı durumu yazar,
   sahnenin sonucunu asla yazmaz.
⑨ UZUNLUK — BİLİNÇLİ SAPMA [D74 · REHBER §5 ①]: insanlı video promptları bandın
   (2.000-2.600) üstünde, tavanın (4.300) altında — kask bloğu + üç bölgeli deri
   negatifi + diyalog bloğu + kapsamlı metin yasağı bandı tek başına doldurur.
   İnsansız sahneler band içindedir. Ölçüm: prompt_kontrol klasör modu çıktısı.
```

---

## 🎬 SAHNE 1 — YALPALAYAN İSTASYON ⭐ HOOK · KURULUM A

```
SÜRE: 10 s (0:00-0:10)   ·   VURUŞ: S0 anomali reveal   ·   KURULUM: A (32mm · WS · göz hizası frontal) — ilk kullanım
İNSAN: yok (burun kamerası)   ·   REPLİK: yok   ·   ŞERİT: –
S0 SORUSU (ekrana değil plana): "Bu şeye nasıl kenetlenilir?"
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 1 of 24. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

SCENE: the forward view from the nose of a small service craft in orbit. Ahead, at the centre-right of the frame and about a sixth of the frame's width, hangs a derelict industrial relay station: a long dark-grey cylindrical hub seen tilted and nearly end-on, an octagonal docking collar at its near end, two long radiator arms out to the sides, the screen-left arm torn short with its panels bent. The station is not still: its collar end is tipped up and to screen-right, caught in the middle of a slow wide swing. Around the collar its own capture latches are bent flat into useless stubs. Along the bottom edge of the frame runs the near rim of the craft's own round docking ring, softly out of focus, with two of its four spring struts visible and fully extended; the craft's nose points straight at the station. Below everything, filling the lower third, is the molten surface of a volcanic planet — black crust cut by a network of orange fissures. No atmosphere, no clouds, no stars.

CAMERA & LIGHT: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus. The sun is high behind the station and out of frame: the station is backlit — its edges carry a hard white rim, its near faces are lit only by the deep orange light coming up from the planet below; every shadow is absolutely black with razor edges; no haze, no scatter, no flare. The station holds the centre-right, the planet the lower third, the ring rim the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 1 of 24. Fixed locked-off camera. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: the derelict station with its octagonal collar and bent latch stubs, its two radiator arms with the screen-left arm torn short; the craft's own ring rim and two of its four fully extended struts along the bottom edge; the molten planet in the lower third; no figure anywhere.

SCENE (as in the start frame): the forward view from the craft's nose; the station ahead at centre-right with its collar end tipped up and to screen-right; the planet below; the craft's nose pointing straight at the station.

CAMERA: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus.

TIMELINE: 0.0s — the station's collar end is high and to screen-right, mid-swing. 3.0s — the collar end has come down toward the centre; the torn arm rises on the other side. 6.0s — the collar face comes almost square to the camera, its dark opening visible for a moment, then keeps going. 10.0s — the collar end is low and to screen-left, still moving at the same steady rate; over the ten seconds it has swept about a fifth of a full circle. The craft itself does not move; the ring rim at the bottom edge stays exactly where it was.

PHYSICS: zero gravity, hard vacuum. The station wobbles at one constant rate — one full cycle every forty-eight seconds — never speeding up, never slowing, never stopping; nothing on it flexes. No exhaust, no plume, no particles.

AUDIO: no exterior sound — hard vacuum. Only the radio channel: faint carrier hiss, and a low two-tone cabin alert repeating every two seconds. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 2 — KUMANDALAR · KURULUM B

```
SÜRE: 10 s (0:10-0:20)   ·   VURUŞ: kurulum / İSTEK   ·   KURULUM: B (35mm · MS · OTS) — ilk kullanım
İNSAN: 1 (sırttan, OTS)   ·   REPLİK: MIRA #1 · 3,0 s (film 00:13)   ·   ŞERİT: G
KAFİYE: S24 aynı kurulum — pencerede küçük dönen istasyon ↔ pencereyi dolduran sabit port
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 2 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: inside a small single-seat cockpit, seen from behind the pilot's right shoulder. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her back is toward the camera and fully visible: it is that one plain smooth panel, and the plain panel is what this shot shows; the back of her helmet and the side of the dark-grey pane rim fill the left third of the frame. Past her helmet is the round forward window — a helmet-and-a-half wide, thick, in a dark frame, reflection-free — and through it, centred, the derelict station at about two-thirds of the window's width: a long dark-grey cylindrical hub with an octagonal docking collar at its near end and two radiator arms, the screen-left arm torn short, the whole station tipped mid-swing; at the window's right edge a torn radiator panel the size of the collar is just entering, edge-on. Below the window the flat dark console runs along the bottom of the frame: a row of exactly four round white indicator lamps, all dark; at her right hand a T-shaped translation handle, her right glove closed on it; just to screen-right of that handle a single push-button under a hinged red-and-white striped guard, the guard closed; at her left hand a short rotation handle, her left glove closed on it; at the far screen-left end of the console a tall yellow-and-black striped abort bar standing upright. No screens, no displays, no markings anywhere. Through the lower half of the window, below the station, the molten planet's black crust and orange fissures.

CAMERA & LIGHT: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus. The deep orange light of the planet enters low through the round window and lies across the console and the underside of the helmet rim; one small white cabin lamp above the window lights the cabin evenly; the four indicator lamps are dark points; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane or the window. Her helmet holds the left third, the window the upper right, the console the bottom band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the window or the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 2 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, heavy segmented dark-grey gloves one piece with the sleeve at the wrist. Her back is toward the camera and stays one continuous smooth white panel from collar to hip, carrying nothing.

SCENE (as in the start frame): the cockpit from behind her right shoulder; the round forward window past her helmet with the tipped station centred in it at two-thirds of the window's width and a torn radiator panel at the window's right edge; the console along the bottom with its four dark lamps, the T-handle under her right glove, the striped guard closed beside it, the rotation handle under her left glove, the abort bar upright at the far screen-left; the planet through the lower half of the window.

CAMERA: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus.

TIMELINE: 0.0s — both gloves are closed on the two handles; the station sits centred in the window, mid-swing; the torn panel is at the window's right edge. 1.0s — the panel crosses the window from its right edge to its left edge, turning end over end at one steady rate, never pausing. 3.0s — the ship computer's flat synthetic voice says, "Station wobble confirmed. One full cycle every forty-eight seconds." 4.0s — her helmet turns slowly to follow the panel across the window. 5.0s — the panel leaves the window at its left edge; her helmet turns back toward the station in the window. 6.0s — her right index finger rises off the T-handle, taps it twice, and closes on it again. 10.0s — hold; the station in the window has swung on about a fifth of a circle; both gloves closed; the four lamps dark.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated. Outside the window the torn panel keeps a continuous slow rotation about its own centre the whole way across and never freezes. The station wobbles at one constant rate, never speeding up.

AUDIO: low cabin fan; her slow breathing inside the helmet; the ship computer's flat synthetic line at 3.0s, heard only — never shown as text. No music. The spoken line is heard only — never shown as text. No subtitles, no captions, no transcript. The voice is off-screen, from the cabin speaker — her mouth stays closed; no invented on-screen speaker.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 3 — RÖLE KAYBI · KURULUM C

```
SÜRE: 10 s (0:20-0:30)   ·   VURUŞ: yükseliş / İSTEK adlandırılır   ·   KURULUM: C (50mm · CU · alt açı) — ilk kullanım
İNSAN: 1 (yüz, panel berrak)   ·   REPLİK: MIRA #2 · 3,0 s (film 00:23)   ·   ŞERİT: R
İZLEYİCİ CÜMLESİ: "Bir şey kaybetti ve durmayacak."   KANAL: bakış (iner, geri kalkar) + nefes
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 3 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the pilot's face, seen from in front and slightly below, inside a small single-seat cockpit. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her eyes are open and steady, looking up past the camera at the forward window above it; her mouth is closed, the jaw soft; her shoulders sit level. Just inside the bottom edge of the frame is the top of the flat dark console: her right glove closed on a T-shaped translation handle, and to screen-right of that handle the closed red-and-white striped guard over a single push-button; her left glove closed on a short rotation handle at the bottom-left. Behind her the plain dark rear bulkhead of the cabin. No screens, no displays, no markings anywhere.

CAMERA & LIGHT: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus. One small white cabin lamp above the window lights her face evenly inside the pane; the deep orange light of the planet enters low through the round window behind the camera and lies across the console and the underside of the helmet rim; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane. Her helmet holds the centre of the frame, the console the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 3 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, her face readable through the pane, heavy segmented dark-grey gloves one piece with the sleeve at the wrist, her back one continuous smooth white panel carrying nothing.

SCENE (as in the start frame): her face from in front and slightly below; eyes up past the camera at the window; mouth closed; the top of the console along the bottom edge with her right glove on the T-handle, the closed striped guard beside it, her left glove on the rotation handle; the plain rear bulkhead behind her.

CAMERA: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus.

TIMELINE: 0.0s — her eyes are on the window above the camera, mouth closed, shoulders level, both gloves closed on the handles. 3.0s — the ship computer's flat synthetic voice says, "Relay carrier lost." 3.5s — her eyes drop to the console at the bottom of the frame and the jaw sets; the mouth tightens into a straight line. 6.0s — the eyes come back up to the window and stay there. 7.0s — her shoulders rise once, slowly, and settle. 10.0s — hold; the eyes on the window; nothing on the console has moved.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated; only the head, eyes and shoulders move, in real time, no slow motion.

AUDIO: low cabin fan; her slow breathing inside the helmet; the ship computer's flat synthetic line at 3.0s, heard only — never shown as text. No music. The spoken line is heard only — never shown as text. No subtitles, no captions, no transcript. The voice is off-screen, from the cabin speaker — her mouth stays closed the whole shot; no invented on-screen speaker, no lip movement.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing, identical bone structure throughout. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 4 — NEFES · KURULUM B (dönüş S02)

```
SÜRE: 10 s (0:30-0:40)   ·   VURUŞ: yükseliş / SÜKÛNET   ·   KURULUM: B — the same position, height and lens as Scene 2
İNSAN: 1 (sırttan)   ·   REPLİK: yok   ·   ŞERİT: S
KADRAJ ÇİFTİ [YANASMA §1.3]: S02'nin çerçevesi; tek değişken — pencerede istasyon dönmüş, panel yok
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 4 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the same fixed framing as the cockpit shot from behind the pilot's right shoulder, with one difference: the station in the window has swung on — its collar end now points up and to screen-left — and there is no loose panel in the window. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her back is toward the camera and fully visible: it is that one plain smooth panel, and the plain panel is what this shot shows; the back of her helmet and the side of the dark-grey pane rim fill the left third of the frame. Past her helmet is the round forward window — a helmet-and-a-half wide, thick, in a dark frame, reflection-free — and through it, centred, the derelict station at about two-thirds of the window's width: a long dark-grey cylindrical hub with an octagonal docking collar at its near end and two radiator arms, the screen-left arm torn short. Below the window the flat dark console runs along the bottom of the frame: a row of exactly four round white indicator lamps, all dark; her right glove closed on a T-shaped translation handle; just to screen-right of that handle a single push-button under a hinged red-and-white striped guard, the guard closed; her left glove closed on a short rotation handle; at the far screen-left end of the console a tall yellow-and-black striped abort bar standing upright. No screens, no displays, no markings anywhere. Through the lower half of the window, the molten planet's black crust and orange fissures.

CAMERA & LIGHT: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2. The deep orange light of the planet enters low through the round window and lies across the console and the underside of the helmet rim; one small white cabin lamp above the window lights the cabin evenly; the four indicator lamps are dark points; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane or the window. Her helmet holds the left third, the window the upper right, the console the bottom band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the window or the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 4 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, heavy segmented dark-grey gloves one piece with the sleeve at the wrist. Her back is toward the camera and stays one continuous smooth white panel from collar to hip, carrying nothing.

SCENE (as in the start frame): the cockpit from behind her right shoulder; the round forward window past her helmet with the station centred in it at two-thirds of the window's width, its collar end pointing up and to screen-left; the console along the bottom with its four dark lamps, the T-handle under her right glove, the striped guard closed beside it, the rotation handle under her left glove, the abort bar upright at the far screen-left; the planet through the lower half of the window.

CAMERA: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2.

TIMELINE: 0.0s — both gloves closed on the two handles; her helmet is on the window; the station's collar end is up and to screen-left, mid-swing. 2.0s — the collar end moves slowly down toward the centre of the window, which sits screen-right of her helmet, at one steady rate. 4.0s — her right index finger rises off the T-handle, taps it twice, and closes on it again; nothing else moves. 7.0s — her shoulders rise once, slowly, and settle back down. 10.0s — hold; the collar end has moved on about a fifth of a circle; both gloves closed; the four lamps dark; her helmet has not turned.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated. The station wobbles at one constant rate, never speeding up, never stopping.

AUDIO: low cabin fan; her slow breathing inside the helmet — one longer breath at 7.0s; one small dry click as the finger taps the handle. Nothing else. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 5 — PENCERE MEKANİĞİ · KURULUM A (dönüş S01)

```
SÜRE: 10 s (0:40-0:50)   ·   VURUŞ: yükseliş / ENGEL görselleşir   ·   KURULUM: A — the same position, height and lens as Scene 1
İNSAN: yok   ·   REPLİK: yok   ·   ŞERİT: –
KİLİT: port yüzü 4,0-6,0 s arasında tam karşıya bakar (6 s'lik pencerenin görsel kanıtı), sonra kayar
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 5 of 24. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

SCENE: the forward view from the nose of a small service craft in orbit, closer now: the derelict relay station sits at the centre of the frame at about a quarter of the frame's width — a long dark-grey cylindrical hub seen tilted and nearly end-on, an octagonal docking collar at its near end, two long radiator arms out to the sides, the screen-left arm torn short with its panels bent. The collar end is tipped to screen-right, mid-swing, its dark opening seen at a slant; around the collar its own capture latches are bent flat into useless stubs. Along the bottom edge of the frame runs the near rim of the craft's own round docking ring, softly out of focus, with two of its four spring struts visible and fully extended; the craft's nose points straight at the station. Below, filling the lower third, the molten surface of a volcanic planet — black crust cut by a network of orange fissures. No atmosphere, no clouds, no stars.

CAMERA & LIGHT: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus — the same position, height and lens as Scene 1. The sun is high behind the station and out of frame: the station is backlit — its edges carry a hard white rim, its near faces are lit only by the deep orange light coming up from the planet below; every shadow is absolutely black with razor edges; no haze, no scatter, no flare. The station holds the centre, the planet the lower third, the ring rim the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 5 of 24. Fixed locked-off camera. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: the derelict station with its octagonal collar and bent latch stubs, its two radiator arms with the screen-left arm torn short; the craft's own ring rim and two of its four fully extended struts along the bottom edge; the molten planet in the lower third; no figure anywhere.

SCENE (as in the start frame): the forward view from the craft's nose; the station at the centre of the frame at about a quarter of the frame's width, its collar end tipped to screen-right; the planet below; the craft's nose pointing straight at the station.

CAMERA: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus — the same position, height and lens as Scene 1.

TIMELINE: 0.0s — the collar end is tipped to screen-right, its opening seen at a slant. 2.0s — the collar end swings toward the centre at one steady rate. 4.0s — the collar's octagonal face comes square to the camera: its dark opening and all of its bent latch stubs are seen straight on. 6.0s — it is still square; then it begins to tip away to screen-left. 8.0s — the opening is a slant again, narrowing. 10.0s — the collar end is well to screen-left and still moving; the craft itself has not moved; the ring rim at the bottom edge stays exactly where it was.

PHYSICS: zero gravity, hard vacuum. The station wobbles at one constant rate — one full cycle every forty-eight seconds — never speeding up, never slowing, never stopping; nothing on it flexes. The craft holds its distance; no exhaust, no plume, no particles.

AUDIO: no exterior sound — hard vacuum. Only the radio channel: faint carrier hiss, and the low two-tone cabin alert repeating every two seconds. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 6 — ORAN KARESİ (V3) · KURULUM E

```
SÜRE: 10 s (0:50-1:00)   ·   VURUŞ: yükseliş / ölçek   ·   KURULUM: E (32mm · EWS · üst açı) — ilk ve TEK kullanım [D32/D78 · YANASMA V3]
İNSAN: yok   ·   REPLİK: MIRA #3 · 3,0 s (film 00:53) — kadrajda insan yok, en güvenli yerleşim   ·   ŞERİT: –
V3 ÜÇLÜSÜ: ① oran cümlesi (bir yirmide bir — a moth beside a cathedral) ② hangi uç önde (burun sağa) ③ kesir merdiveni (altı gemi boyu boşluk)
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 6 of 24. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft.

SCENE: two bodies in orbit, seen from high to one side. At screen-left, small, a blunt-nosed white service craft with orange bands, its nose pointing toward screen-right, its nose carrying a round docking ring held out on exactly four spring struts, the ring about a third of the craft's width; its short white attitude-thruster plume is not firing — no plume at all. At screen-right, enormous and running off the right edge of the frame, the derelict relay station: a long dark-grey cylindrical hub about twenty times the length of the craft — a moth beside a cathedral — with an octagonal docking collar at its near end pointing back toward the craft, two long radiator arms out to the sides, the screen-left arm torn short with its panels bent. The gap between the craft's ring and the station's collar is about six craft-lengths of empty black. The collar end is tipped mid-swing, its opening at a slant. Below both, filling the lower third, the molten surface of a volcanic planet — black crust cut by a network of orange fissures. No atmosphere, no clouds, no stars.

CAMERA & LIGHT: 32mm spherical lens fixed 60 m from the craft and 20 m above the docking axis, aimed down at the pair — high-angle extreme wide shot, deep focus. The sun is high beyond the station, out of frame at upper screen-right: both hulls are lit hard from upper screen-right; the craft's nose ring catches the light; the station's craft-facing surfaces stay dark with a hard white rim on their far edges; the planet's deep orange light reaches only the undersides; every shadow is absolutely black with razor edges; no haze, no flare. The craft holds the left third, the station the right half, the planet the lower third.

NEGATIVE: Fixed locked-off camera, single frame. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. The craft is one-twentieth of the station — never drawn the same size, never swapped. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on either hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no plume, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 6 of 24. Fixed locked-off camera. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: the small white craft at screen-left with its nose pointing toward screen-right and its four-strut docking ring; the station at screen-right, twenty times the craft's length, its collar pointing back toward the craft, the screen-left arm torn short; six craft-lengths of black between ring and collar; the planet in the lower third; no figure anywhere.

SCENE (as in the start frame): the pair from high to one side; the craft small at screen-left, nose toward screen-right; the station enormous at screen-right and running off the right edge, collar end tipped mid-swing; the planet below.

CAMERA: 32mm spherical lens fixed 60 m from the craft and 20 m above the docking axis, aimed down at the pair — high-angle extreme wide shot, deep focus.

TIMELINE: 0.0s — the craft holds its position at screen-left, nose toward screen-right; the station's collar end is tipped up, mid-swing. 3.0s — the ship computer's flat synthetic voice says over the radio, "Coronal flux rising. Sensor confidence fifty percent." 4.0s — the collar end swings down through the line of the craft's nose at one steady rate. 7.0s — the collar end continues below that line; the torn arm rises. 10.0s — hold; the station has swung on about a fifth of a circle; the craft has not moved and the gap between ring and collar is still about six craft-lengths.

PHYSICS: zero gravity, hard vacuum. The station wobbles at one constant rate — one full cycle every forty-eight seconds — never speeding up, never stopping; nothing on it flexes. The craft holds station with no visible thrust: no plume, no exhaust, no particles.

AUDIO: no exterior sound — hard vacuum. Only the radio channel: faint carrier hiss and the single synthetic line at 3.0s, heard only — never shown as text; the voice is off-screen only — no mouth in frame, no invented on-screen speaker. No music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. The craft stays one-twentieth of the station — never the same size, never swapped. No readable text, letters, digits, numbers or symbols anywhere in the frame; no scale marks, no flag, no logo. No subtitles, no captions, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no plume, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 7 — HALKA · KURULUM A (dönüş S05)

```
SÜRE: 10 s (1:00-1:10)   ·   VURUŞ: birinci manevra başlar   ·   KURULUM: A — the same position, height and lens as Scene 1
İNSAN: yok   ·   REPLİK: yok   ·   ŞERİT: –
KİLİT: halka yakası ve iki dikme artık NET ve TAM UZUNLUKTA (bedelin BEFORE'u) [D179]
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 7 of 24. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

SCENE: the forward view from the nose of a small service craft in orbit, closer again: the derelict relay station's octagonal docking collar alone is about an eighth of the frame's width, at the centre, its dark opening at a slant, its own capture latches bent flat into useless stubs around the rim; behind it the long dark-grey cylindrical hub runs away into the frame, with the two radiator arms out to the sides, the screen-left arm torn short with its panels bent. Along the bottom edge of the frame runs the near rim of the craft's own round docking ring, now sharp and clearly a machined ring, with two of its four spring struts visible, each strut fully extended at its full length; the craft's nose points straight at the collar. Below, filling the lower third, the molten surface of a volcanic planet — black crust cut by a network of orange fissures. No atmosphere, no clouds, no stars.

CAMERA & LIGHT: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus — the same position, height and lens as Scene 1. The sun is high behind the station and out of frame: the station is backlit — its edges carry a hard white rim, its near faces are lit only by the deep orange light coming up from the planet below; every shadow is absolutely black with razor edges; no haze, no scatter, no flare. The collar holds the centre, the planet the lower third, the ring rim the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. Exactly four struts on the craft's ring — never more, never fewer. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the hull, the collar or the station; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 7 of 24. Fixed locked-off camera. Human count in this frame: zero — no human figure; the film's only human is inside the sealed craft behind this camera.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: the station's octagonal collar at the centre with its bent latch stubs, the hub behind it, the screen-left arm torn short; the craft's own ring rim sharp along the bottom edge with two of its four struts fully extended; the molten planet in the lower third; no figure anywhere.

SCENE (as in the start frame): the forward view from the craft's nose; the collar at the centre about an eighth of the frame wide, its opening at a slant; the planet below; the craft's nose pointing straight at the collar.

CAMERA: 32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim, aimed straight ahead along the docking axis — eye-level frontal wide shot, deep focus — the same position, height and lens as Scene 1.

TIMELINE: 0.0s — the collar's opening is at a slant, tipped to screen-right; the ring rim and its two struts are sharp and still at the bottom edge. 3.0s — the collar swings toward square at one steady rate; the craft creeps forward so slowly that the collar grows only a little. 6.0s — the collar face is square to the camera, its stubs seen straight on; the collar is a touch larger than at the start. 8.0s — the collar begins to tip away to screen-left. 10.0s — hold; the collar is at a slant again and a little larger than at the start; the ring rim and struts at the bottom edge have not changed.

PHYSICS: zero gravity, hard vacuum. The station wobbles at one constant rate — one full cycle every forty-eight seconds — never speeding up, never stopping. The craft closes at its slowest rate — about one ring-width over the whole shot; no plume, no exhaust, no particles.

AUDIO: no exterior sound — hard vacuum. Only the radio channel: faint carrier hiss, and the low two-tone cabin alert repeating every two seconds. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Human count zero — no figure, no crew, no invented pilot outside the craft. 0% bloom, no glow filter, no soft focus. Exactly four struts on the craft's ring, all fully extended throughout. No readable text, letters, digits, numbers or symbols anywhere in the frame; no scale marks, no flag, no logo. No subtitles, no title card, no watermark. No atmosphere, no clouds, no sky, no stars, no haze, no dust, no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 8 — MANUEL YANAŞMA · KURULUM B (dönüş S04)

```
SÜRE: 10 s (1:10-1:20)   ·   VURUŞ: birinci manevra / İSTEK   ·   KURULUM: B — the same position, height and lens as Scene 2
İNSAN: 1 (sırttan)   ·   REPLİK: yok   ·   ŞERİT: G
KARAKTER: KONTROL EDER — baş kola döner, bir saniye sonra el gider; iki tık, sonra itiş
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 8 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the same fixed framing as the cockpit shot from behind the pilot's right shoulder, with one difference: the station's octagonal collar now sits centred in the window at about a third of the window's width, its dark opening tipped at a slant. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her back is toward the camera and fully visible: it is that one plain smooth panel, and the plain panel is what this shot shows; the back of her helmet and the side of the dark-grey pane rim fill the left third of the frame. Past her helmet is the round forward window — a helmet-and-a-half wide, thick, in a dark frame, reflection-free — and through it the collar, and behind it the station's dark hub and its radiator arms, the screen-left arm torn short. Below the window the flat dark console runs along the bottom of the frame: a row of exactly four round white indicator lamps, all dark; her right glove closed on a T-shaped translation handle; just to screen-right of that handle a single push-button under a hinged red-and-white striped guard, the guard closed; her left glove closed on a short rotation handle; at the far screen-left end of the console a tall yellow-and-black striped abort bar standing upright. No screens, no displays, no markings anywhere. Through the lower half of the window, the molten planet's black crust and orange fissures.

CAMERA & LIGHT: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2. The deep orange light of the planet enters low through the round window and lies across the console and the underside of the helmet rim; one small white cabin lamp above the window lights the cabin evenly; the four indicator lamps are dark points; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane or the window. Her helmet holds the left third, the window the upper right, the console the bottom band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the window or the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 8 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, heavy segmented dark-grey gloves one piece with the sleeve at the wrist. Her back is toward the camera and stays one continuous smooth white panel from collar to hip, carrying nothing.

SCENE (as in the start frame): the cockpit from behind her right shoulder; the round forward window past her helmet with the station's collar centred in it at about a third of the window's width, its opening at a slant; the console along the bottom with its four dark lamps, the T-handle under her right glove, the striped guard closed beside it, the rotation handle under her left glove, the abort bar upright at the far screen-left; the planet through the lower half of the window.

CAMERA: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2.

TIMELINE: 0.0s — both gloves closed on the two handles; her helmet is on the window; the collar's opening is at a slant, swinging slowly toward square. 2.0s — her helmet turns down toward the T-handle first. 3.0s — a full second later her right glove opens, the index finger taps the handle twice, and the glove closes on it again. 4.0s — the glove pushes the T-handle forward by one finger's width and holds it there; her helmet turns back up to the window. 6.0s — the collar in the window comes square, its dark opening seen straight on, and it is a little larger than at the start. 10.0s — hold; the collar has begun to tip away to screen-left; the T-handle stays forward; the four lamps dark.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated; the arm moves in real time, no slow motion. Outside, the station wobbles at one constant rate; the craft closes at its slowest rate — the collar grows only a little over the shot.

AUDIO: low cabin fan; her slow breathing inside the helmet; two small dry clicks as the finger taps the handle. Nothing else. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 9 — BAŞ KİLİTLENİR · KURULUM C (dönüş S03)

```
SÜRE: 10 s (1:20-1:30)   ·   VURUŞ: birinci manevra sürer   ·   KURULUM: C — the same position, height and lens as Scene 3
İNSAN: 1 (yüz)   ·   REPLİK: yok   ·   ŞERİT: G
İZLEYİCİ CÜMLESİ: "Nefesini sayarak yaklaşıyor."   KANAL: nefes (omuz) + TEL: baş kilitlenir, yalnız gözler
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 9 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the pilot's face, seen from in front and slightly below, inside a small single-seat cockpit. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her eyes are open and fixed, looking up past the camera at the forward window above it; her mouth is closed; her shoulders sit high, drawn up toward the collar ring. Just inside the bottom edge of the frame is the top of the flat dark console: her right glove closed on a T-shaped translation handle pushed a finger's width forward, and to screen-right of that handle the closed red-and-white striped guard over a single push-button; her left glove closed on a short rotation handle at the bottom-left. Behind her the plain dark rear bulkhead of the cabin. No screens, no displays, no markings anywhere.

CAMERA & LIGHT: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus — the same position, height and lens as Scene 3. One small white cabin lamp above the window lights her face evenly inside the pane; the deep orange light of the planet enters low through the round window behind the camera and lies across the console and the underside of the helmet rim; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane. Her helmet holds the centre of the frame, the console the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 9 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, her face readable through the pane, heavy segmented dark-grey gloves one piece with the sleeve at the wrist, her back one continuous smooth white panel carrying nothing.

SCENE (as in the start frame): her face from in front and slightly below; eyes fixed up past the camera at the window; mouth closed; shoulders high; the top of the console along the bottom edge with her right glove on the forward-pushed T-handle, the closed striped guard beside it, her left glove on the rotation handle; the plain rear bulkhead behind her.

CAMERA: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus — the same position, height and lens as Scene 3.

TIMELINE: 0.0s — her eyes are fixed on the window above the camera; her breaths are short and shallow and her shoulders rise a little with each one, about one breath every two seconds. 2.0s — her eyes make one small movement to screen-left and back, tracking something in the window; the head moves with them. 5.0s — the head stops and locks; from here on only the eyes move. 7.0s — the eyes make another small tracking movement, the head does not follow. 8.0s — her lips press together. 10.0s — hold; head locked, eyes on the window, shoulders still high, both gloves closed on the handles.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated; only the head, eyes and shoulders move, in real time, no slow motion.

AUDIO: low cabin fan; her breathing inside the helmet — short, shallow, about one breath every two seconds. Nothing else. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing, identical bone structure throughout. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 10 — ALTI SANİYE · KURULUM D

```
SÜRE: 10 s (1:30-1:40)   ·   VURUŞ: birinci manevra / ENGEL sayısı   ·   KURULUM: D (85mm · ECU · profil) — ilk kullanım
İNSAN: 1 (yalnız sağ eldiven ve kol)   ·   REPLİK: MIRA #4 · 3,0 s (film 01:33)   ·   ŞERİT: G
KARAR MİMARİSİ: seçilecek nesne (koruma kapaklı düğme) ve reddedilecek nesne (iptal kolu) AYNI kadrajda tanıtılır
3c NOTU: yüz yok + el + makro — kamera nesne HİZASINDA (yandan, kalça yüksekliği), parçalar ard arda derinlikte; tepeden değil
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 10 of 24. Exactly one human figure — this film has exactly one human total; only her gloved right hand and the sleeve of her suit are in this frame.

SCENE: a side-on view along the flat dark console of a small single-seat cockpit, at the height of the pilot's hip. Nearest the camera, in the lower-right foreground and sharp, a single push-button under a hinged red-and-white striped guard, the guard closed flat over it. At the centre of the frame, a hand's width beyond the guard, her right glove — heavy, segmented, dark grey, one piece with the white suit sleeve at the wrist — closed on a T-shaped translation handle, the thumb resting along the top of the T, the handle pushed a finger's width forward in its slot; the sleeve runs up out of the top-left of the frame. Farther along the console, in the background at screen-left and softer, a tall yellow-and-black striped abort bar standing upright, and beyond it the dark edge of the cabin wall. Above the console, along the top edge of the frame, the lower part of the round forward window, out of focus, with the deep orange of the planet in it. No screens, no displays, no markings anywhere.

CAMERA & LIGHT: 85mm spherical lens fixed 0.5 m from the right glove at hip height, side-on to the console — profile extreme close-up, shallow focus on the glove and the guard. The deep orange light of the planet enters low through the round window and lies along the console and the top of the glove; one small white cabin lamp above the window adds a thin white edge to the guard and the handle; every shadow is hard-edged black; no haze, no bloom. The guard holds the lower-right foreground, the glove the centre, the bar the left background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — one right hand only, no second hand, no second person. 0% bloom, no glow filter, no soft focus on the glove. The glove is a heavy segmented glove, fully covering the hand, one piece with the sleeve — no bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. Exactly five fingers, no merging with the handle. No readable text, letters, digits or symbols anywhere in the frame — not on the console, the guard, the handle or the bar; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 10 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total; only her gloved right hand and the sleeve of her suit are in this frame.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: her right glove, heavy, segmented, dark grey, one piece with the white suit sleeve at the wrist, closed on the T-shaped handle at the centre; the striped guard closed flat over its button in the lower-right foreground; the yellow-and-black abort bar upright in the left background; the orange of the planet in the window along the top edge; no face, no second hand.

SCENE (as in the start frame): the side-on view along the console at hip height; the guard nearest the camera, the glove on the T-handle at the centre, the abort bar farthest at screen-left.

CAMERA: 85mm spherical lens fixed 0.5 m from the right glove at hip height, side-on to the console — profile extreme close-up, shallow focus on the glove and the guard.

TIMELINE: 0.0s — the glove is closed on the T-handle, the thumb resting along the top; the guard is closed; nothing moves. 3.0s — the ship computer's flat synthetic voice says, "Capture window six seconds per cycle." 4.0s — the grip tightens: the glove's segments draw tight and rise over the knuckles; the thumb shifts a little along the top of the T. 6.0s — the index finger rises off the handle and taps it twice. 7.0s — the glove pushes the T-handle forward by one more finger's width in its slot and holds it there. 10.0s — hold; the guard has not moved; the abort bar has not moved.

PHYSICS: zero gravity inside the cabin; the hand moves in real time, no slow motion; the handle moves only in its slot, with a hard mechanical stop.

AUDIO: low cabin fan; her breathing inside the helmet, short and shallow; the ship computer's flat synthetic line at 3.0s, heard only — never shown as text; two small dry clicks as the finger taps the handle. No music. The spoken line is heard only — never shown as text. No subtitles, no captions, no transcript. The voice is off-screen only — no mouth in frame, no invented on-screen speaker.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — one right hand only, no second hand, no second person. 0% bloom, no glow filter, no soft focus on the glove. The glove stays a heavy segmented glove fully covering the hand, one piece with the sleeve — no bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. Exactly five fingers throughout, no merging with the handle, no extra fingers. The guard stays closed for the whole shot; the abort bar stays upright and untouched. No readable text, letters, digits, numbers or symbols anywhere in the frame; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 11 — KAÇIŞ · KURULUM C (dönüş S09)

```
SÜRE: 10 s (1:40-1:50)   ·   VURUŞ: orta nokta / kriz başlar   ·   KURULUM: C — the same position, height and lens as Scene 3
İNSAN: 1 (yüz)   ·   REPLİK: yok   ·   ŞERİT: T
İZLEYİCİ CÜMLESİ: "Hedef elinden kayıyor ve o bunu görüyor."   KANAL: bakış (yavaş takip, durur) + nefes tutulur
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 11 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the pilot's face, seen from in front and slightly below, inside a small single-seat cockpit. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her head is held still; her eyes are open and fixed, looking up past the camera at the forward window above it; her mouth is closed with the lips pressed together; her shoulders sit high, drawn up toward the collar ring. Just inside the bottom edge of the frame is the top of the flat dark console: her right glove closed on a T-shaped translation handle pushed two finger-widths forward, and to screen-right of that handle the closed red-and-white striped guard over a single push-button; her left glove closed on a short rotation handle at the bottom-left. Behind her the plain dark rear bulkhead of the cabin. No screens, no displays, no markings anywhere.

CAMERA & LIGHT: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus — the same position, height and lens as Scene 3. One small white cabin lamp above the window lights her face evenly inside the pane; the deep orange light of the planet enters low through the round window behind the camera and lies across the console and the underside of the helmet rim; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane. Her helmet holds the centre of the frame, the console the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 11 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, her face readable through the pane, heavy segmented dark-grey gloves one piece with the sleeve at the wrist, her back one continuous smooth white panel carrying nothing.

SCENE (as in the start frame): her face from in front and slightly below; head still, eyes fixed up past the camera at the window; lips pressed; shoulders high; the top of the console along the bottom edge with her right glove on the forward-pushed T-handle, the closed striped guard beside it, her left glove on the rotation handle; the plain rear bulkhead behind her.

CAMERA: 50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched up 15 degrees at her face — low-angle close-up, deep focus — the same position, height and lens as Scene 3.

TIMELINE: 0.0s — head still, eyes on the window, breath held — the shoulders do not move. 2.0s — her eyes begin to track something drifting to screen-left in the window; the head follows them slowly, a little at a time. 5.0s — the head is turned slightly to screen-left, still tracking; the eyes keep going a fraction further than the head. 7.0s — the eyes widen slightly and the head stops dead. 9.0s — a short exhale: the shoulders drop a finger's width and come straight back up. 10.0s — hold; head turned slightly to screen-left, eyes fixed, both gloves closed on the handles.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated; only the head, eyes and shoulders move, in real time, no slow motion.

AUDIO: low cabin fan; inside the helmet no breath at all until 9.0s, then one short exhale. Nothing else. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing, identical bone structure throughout. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the helmet or the console; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 12 — İPTAL · KURULUM B (dönüş S08)

```
SÜRE: 10 s (1:50-2:00)   ·   VURUŞ: orta nokta / BAŞARISIZ DENEME (wave-off — prosedürdür, hata değil)   ·   KURULUM: B — the same position, height and lens as Scene 2
İNSAN: 1 (sırttan)   ·   REPLİK: yok   ·   ŞERİT: D
KADRAJ ÇİFTİ: S08'in çerçevesi; tek değişken — port pencerenin merkezinden sola kayar ve yan döner; T-kol geri çekilir
BÖLÜM SINIRI: S12 (B · MS · iç) ↔ S13 (A · WS · dış) — ardışık çift bant içi
```

### 📸 GÖRSEL PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 12 of 24. Exactly one human figure — this film has exactly one human total.

SCENE: the same fixed framing as the cockpit shot from behind the pilot's right shoulder, with one difference: the station's octagonal collar is now large in the window — about half of the window's width — and it has already slipped off the window's centre toward the window's left edge, its dark opening tipping toward edge-on. She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white pressure suit with one safety-orange band around each upper arm; the helmet is a hard white shell with a single flat front pane set inside a visible dark-grey rim — not a bubble, not a dome — the pane optically clear with zero tint and zero mirror coating, one thin unbroken specular line along the pane's upper edge, the collar seal ring visible where the helmet meets the suit, her face fully readable through the pane. Her gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The back of the suit is one continuous smooth white panel from collar to hip, carrying nothing. Her back is toward the camera and fully visible: it is that one plain smooth panel, and the plain panel is what this shot shows; the back of her helmet and the side of the dark-grey pane rim fill the left third of the frame. Past her helmet is the round forward window — a helmet-and-a-half wide, thick, in a dark frame, reflection-free — and through it the large collar sliding left, and behind it the station's dark hub. Below the window the flat dark console runs along the bottom of the frame: a row of exactly four round white indicator lamps, all dark; her right glove closed on a T-shaped translation handle pushed two finger-widths forward; just to screen-right of that handle a single push-button under a hinged red-and-white striped guard, the guard closed; her left glove closed on a short rotation handle; at the far screen-left end of the console a tall yellow-and-black striped abort bar standing upright. No screens, no displays, no markings anywhere. Through the lower edge of the window, the molten planet's orange fissures.

CAMERA & LIGHT: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2. The deep orange light of the planet enters low through the round window and lies across the console and the underside of the helmet rim; one small white cabin lamp above the window lights the cabin evenly; the four indicator lamps are dark points; every shadow in the cabin is hard-edged black; no haze, no reflection in the pane or the window. Her helmet holds the left third, the window the upper right, the console the bottom band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure — no second person, no clone, no reflected figure in the window or the pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture. The front pane is clear glass with zero tint, zero mirror coating and zero reflection. No back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VİDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 12 of 24. Fixed locked-off camera. Exactly one human figure — this film has exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate it. CONTINUITY LOCKS carried from the frame: exactly one human, a woman of about forty, broad-shouldered, dark brown skin, matte white pressure suit with one safety-orange band on each upper arm, hard white helmet with one flat front pane in a visible dark-grey rim, the pane optically clear with zero tint and zero mirror coating, one thin specular line along its upper edge, the collar seal ring visible, heavy segmented dark-grey gloves one piece with the sleeve at the wrist. Her back is toward the camera and stays one continuous smooth white panel from collar to hip, carrying nothing.

SCENE (as in the start frame): the cockpit from behind her right shoulder; the round forward window past her helmet with the station's collar large in it, already slipping toward the window's left edge and tipping toward edge-on; the console along the bottom with its four dark lamps, the T-handle pushed forward under her right glove, the striped guard closed beside it, the rotation handle under her left glove, the abort bar upright at the far screen-left; the planet's orange at the window's lower edge.

CAMERA: 35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed past her helmet at the round forward window — over-the-shoulder medium shot, deep focus — the same position, height and lens as Scene 2.

TIMELINE: 0.0s — the collar is large in the window and sliding toward the window's left edge at one steady rate, its opening tipping toward edge-on; both gloves closed; her helmet on the window. 3.0s — the collar's opening is edge-on: a dark slot, still sliding left. 5.0s — her right glove draws the T-handle straight back to its rear stop in one movement; the grip tightens as it goes, the glove's segments rising over the knuckles. 6.0s — the collar leaves the window at its left edge; the station's dark hub slides across the window in its place. 8.0s — her helmet stays on the window; her shoulders stay high and do not come down. 10.0s — hold; the hub still sliding slowly across the window; the T-handle at its rear stop; the four lamps dark.

PHYSICS: zero gravity inside the cabin; she is strapped in and her body stays seated; the arm moves in real time. Outside, the station wobbles at one constant rate; the craft's forward creep stops when the handle reaches the rear stop, and the view through the window does not lurch.

AUDIO: low cabin fan; her breathing inside the helmet, short and shallow; one hard mechanical clack as the T-handle meets its rear stop at 5.0s. Nothing else. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change. Exactly one human — no second person, no clone, no reflected figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin with pores — no airbrushing, no waxy texture, no face morphing. Suit, helmet and gloves identical throughout; the helmet stays sealed; the front pane stays optically clear with zero tint, zero mirror coating and zero reflection; the back stays one continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere in frame: none above the collar seal, none at the wrist between glove and sleeve, none at the ankle above the boot cuff. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the console, the window frame or the station; no scale marks, no flag, no logo, no patch. No screens, no displays, no HUD, no subtitles, no title card, no watermark. Hands and controls keep a hard structural boundary — no merging, no extra fingers. No haze, no dust, no lens flare, no anamorphic streak. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

---
