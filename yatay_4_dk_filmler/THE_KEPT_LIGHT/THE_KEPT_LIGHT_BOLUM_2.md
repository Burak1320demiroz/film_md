# 🔦 THE KEPT LIGHT — Tutulan Işık | BÖLÜM 2

## AI Production Bible — Self-Contained Prompts
### BÖLÜM 2: Sahne 13-24 (12 sahne) | 16:9 Yatay | Görsel + Video
### _"Burada hiçbir şey geçmişe geçmez; bıraktığın her şey bugünde kalır ve birikir."_

> **BÖLÜM 2 süresi:** 12 sahne × 10 s = 120 saniye (2:09 – 4:09)
> **Toplam film:** 25 sahne = 249 saniye = 4:09
> **BÖLÜM 1:** `THE_KEPT_LIGHT_BOLUM_1.md` (S0-S12) — Bible'lar ve negatif
> çekirdek orada TAM METİN olarak yazılıdır; aşağıdaki promptlar yine de
> SELF-CONTAINED'dir ve hiçbiri "Bible'a bak" atfı taşımaz (kural ③).
> **Plan:** `THE_KEPT_LIGHT_PLAN.md`
> **Replik:** 0 — film konuşma bakımından tamamen sessiz.

> ⚠️ **KURULUM İSKELETİ satırı BÖLÜM 1'dedir ve filmin 25 harfinin
> tamamını kapsar.** Klasör modu iki dosyayı birleştirip iskeleti orada
> bulur. Bu dosyanın kendi payı: `D C B C C B C E E D C A`.
> ⛔ Dosya modunda kapı 25 harfi bu dosyanın 12 promptuyla karşılaştırır
> ve FIX verir; bölünmüş filmde bu kaçınılmazdır ve GEÇERLİ KOŞU KLASÖR
> MODUDUR.

---

## ⚠️ BÖLÜM 2 ÜRETİM NOTLARI (promptlardan önce oku)

```
① BÖLÜM 1'İN ON DÖRT NOTU AYNEN GEÇERLİDİR. Aşağıdakiler yalnız bu
   bölümde DEĞİŞEN ya da YENİ olanlardır.

② KİR MERDİVENİ BİR BASAMAK ÇIKAR [D147 · ⛔ D155]
   S13-S24: eldivenlerin avuç içleri ve dizler + SAĞ ÖN KOL MANŞETİNİN
   dış yüzü mat. Sebep kadrajda görünür: S16-S17'de hattı o kolla çeker.
   Klip İÇİNDE sabit, sahneler ARASI monotonik, hiç azalmaz.
   ⛔ "Wear state: PHASE n" hiçbir prompta yazılmaz.

③ IŞIK — TEK PLANLI DEĞİŞKEN VE SINIRDA DEĞİŞİR [ACI_YAYI §7③]
   Değişen tek şey ALANI HANGİ LAMBANIN AYDINLATTIĞIDIR:
     S13-S19  eski lamba, ağzın on gövde boyu altında (Z1/Z3 aynen)
     S20      eski lamba modülle birlikte AŞAĞI GİDER — bu bir durum
              değişimi DEĞİL, kaynağın YER DEĞİŞTİRMESİDİR ve hareketi
              kadrajda görünür
     S21-S23  alan aydınlatılmıyor; çok aşağıda tek nokta, konisi öteye
     S24      bekçinin YENİ lambası, serin ve parlak
   ⛔ Işık kademesi hiçbir klibin İÇİNDE değişmez.

④ HAT — ⛔ MODELİN REFLEKSİ SARKMAK VE SALLANMAKTIR
   Pozitif cümle, hattın göründüğü her promptta birebir:
   "The thin line is straight and taut from the pin down out of frame —
    it does not sag, it does not curve, it does not sway, it does not
    swing; it holds one exact line for the whole shot."

⑤ MUTLAK SESSİZLİK KURGU İŞİDİR [⛔ D180]
   S21'in AUDIO satırındaki "absolute silence" cümlesi YEDEKTİR. Bıçak
   kurgudadır ve MUZIK dosyasında yazılıdır:
     KURGUDA HARD MUTE: sn 209,0 – 219,0
   Ölçüm üç eşikte koşulur (−50 / −40 / −30 dB) ve teslim öncesi
   `rapor_kontrol.py --olcum-sessizlik 209-219` ile doğrulanır.

⑥ İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [⛔ D179]
   Değişim taşıyan sahnelerde (S17 · S19 · S20 · S24) imaj promptu video
   promptunun `0.0s —` satırıyla KELİME KELİME uyumludur.
   ⭐ S24'te bekçinin lambası imaj karesinde ZATEN YANIYOR; sönük hâli
     S23'ün karesinde kalır. Değişim SINIRDADIR, klip içinde değil.

⑦ FİNAL VURUŞ KANITI [D141] — S24 · 4:07
   Kadrajın altında SAYILABİLİR ALTI parlak nesne vardır: beş kelepçe ve
   bekçinin lambası. Sap (kesilmiş altıncı kelepçenin gövdesi) kadrajın
   üst kenarında, çerçeveye cıvatalı durur ve sayıya girmez.
   ⛔ Bu bir "final duygusu" değil, tek karede sayılabilir bir NESNE
   sayısıdır ve teslimde ffmpeg ile bakılır.

⑧ KURULUM — bu bölümde 5 kurulum (A · B · C · D · E) · F yalnız S10'daydı.
   Dönen her sahne kamera metnini BİREBİR kopyalar ve işaret satırını
   taşır [ACI_YAYI §7 ⑥].

⑨ NOVUM TAŞIYICISI: kelepçe × eldivenli avucun kapak ağzında açılması
   → kelepçe iner ama inişi bitmez [ONERME §2 · plan 🧬].
   TEK KARE testinin nesnesi de KELEPÇEDİR — aynı nesne [D157]:
   S0 · 0:04, açık eldivenin bir karış altında duran kelepçe.
   ⭐ Bu bölümde kural aynı taşıyıcının üçüncü ve dördüncü kanıtını
   verir: hat (S16-S17) ve modül + eski lamba (S20-S21).
```

---

# 🎬 SAHNELER

---

## 🎬 SAHNE 13 (S13) — GERGİN HAT · KURULUM D (dönüş · kaynak S11)
### ⭐ ORTA NOKTA · 2:09 · SAHTE YENİLGİ

> ⭐ **DRAMATİK İRONİNİN ZİRVESİ [HOOK §3.1]:** modül tek kelepçeye kalınca
> hattı yükler; hat karanlıktan çıkıp ışığa kalkar ve GERGİN durur.
> Bekçi modüle bakıyor, hatta değil. İzleyici karakterden ÖNDEDİR.
> ⛔ **DÖNÜŞ:** kamera metni S9/S11'in metnidir; işaret satırı eklendi.
> Kelepçe sayacı: BİR.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 14 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of a small square vacuum work bay, seen from the far
wall. The bay is bare grey metal; its floor carries one open square hatch
about one body-length on a side, set slightly right of centre. Around the
hatch frame sit six clamp seats; five are empty and one matte grey clamp
the length of a hand is still bolted through the sixth, on the far arc,
holding a disused cylinder that now hangs from that single point below the
opening — the module is a little longer than he is tall, matte, dark and
bare, and it hangs steeply from one corner. From that last clamp a thin
line rises out of the dark and runs straight and taut across the lit
opening before dropping away through it. Standing on the near arc, a pace
back from the lip with his weight on both boots, is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable through it, turned down to
the hanging module and not to the line. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. A short
two-jawed cutter hangs in his right glove; a hooded hand-lamp the size of
his fist rides dark in a clip at his right hip. A thin pale scratch runs
along the left forearm sleeve of the suit. His glove palms, his knees and
the outer face of his right forearm sleeve are dulled with wear.

CAMERA & LIGHT: 24mm spherical lens, fixed 5.0 m from him at the far wall
of the bay, eye-level and square on. Wide shot, deep focus. Two hooded work
lamps in the bay ceiling light the room from above with cool neutral white;
the metal walls of the bay throw no second light, and the shadows inside
the bay are absolutely black with razor edges. Nothing lights the opening
from below. A low rim light separates his shoulders and helmet from
whatever is behind him; his silhouette never merges with the background.
The hatch holds the lower centre-right, the figure the left third, the taut
line the lower centre band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no crew, no reflected or doubled figure. 0%
bloom, no glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. Exactly one clamp holds the module and five seats are
empty. The thin line is straight and taut — no sag, no curve, no catenary,
no sway. No screens, no dials, no gauges, no keypads, no indicator lights.
No readable text, letters, digits or symbols anywhere in the frame; no
scale marks, no graduation ticks; no flag, no logo, no patch. No subtitles,
no title card, no watermark. No dust, no haze. No smoke,
no exhaust, no flame, no spark, no rust. No lens flare, no anamorphic
streak. Metal static and solid — no melting, no warping. No Unreal Engine look, no CGI aesthetic. Photorealistic,
35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 14 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. A short two-jawed cutter stays in his right glove;
a hooded hand-lamp stays dark in the clip at his right hip. One clamp holds
the module and five seats stay empty for the whole shot. His glove palms,
knees and right forearm sleeve are dulled with wear.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch, the disused module hanging steeply from its single last clamp, and the
thin line rising out of the dark to run straight and taut across the lit
opening.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus — the same position,
height and lens as Scene 12.

TIMELINE: 0.0s — the module is already settling on its single clamp, still
turning through the last of its swing. 3.0s — it comes to rest hanging from
one corner; the taut line across the opening holds one exact line and does
not move with it. 5.0s — he takes one step back from the lip, his boots
setting down one after the other, and stands square. 8.0s — his helmet
turns slowly along the module from one end to the other. 10.0s — hold; he
is looking at the module, not at the line, and the line is still there.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module is a rigid body hanging from one clamp: it does not stretch, bend or
deform. The thin line is straight and taut from the pin down out of frame —
it does not sag, it does not curve, it does not sway, it does not swing; it
holds one exact line for the whole shot. Everything below the lip of the
hatch keeps moving downward — always the same direction, never rising,
never stopping, never held in place — but each thing moves less the deeper
it already is. Up is the rock ceiling above the base; down is the black
disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; a long low groan through the
deck as the module settles on its last clamp; two dry boot contacts as he
steps back; slow breathing. Nothing else — no sound carries in this vacuum.
No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; the front pane stays
clear and unmirrored; the back stays one continuous smooth panel with no
backpack, tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp count stays one. The thin line never sags, never
curves, never sways and never swings. The module stays a rigid body — no
stretching, no bending — and it does not come free in this shot. No
screens, no dials, no gauges, no indicator lights. No readable text,
letters or digits anywhere in frame; no scale marks, no ticks; no flag, no
logo. No subtitles, no watermark. No dust, no haze. No
smoke, no exhaust, no flame, no spark, no rust. No lens flare, no
anamorphic streak. Metal static — no melting, no warping. No voice, no music. No CGI aesthetic. Photorealistic, 35mm
film grain.
```

---

## 🎬 SAHNE 14 (S14) — GÖRÜR · KURULUM C (dönüş · kaynak S12) ⭐VİRAL

> ⭐ **VİRAL KAPISI [§2.4]:**
> **YÜZ:** baş dönüşün ORTASINDA durur; ağız kapalı, alt dudak içeri
> çekilir, bakış aşağı kayar (1,2 s).
> **HAREKET:** eldiven hattın üstünde kayar; hat gerilip ŞAKLAR ve
> titremesi kadrajın altına doğru koşar.
> ⭐ Dramatik ironi burada KAPANIR: bekçi öğrenir [HOOK §3.1].
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 15 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the far edge of an open square hatch in the floor
of a small grey vacuum work bay, seen from the side. He is a man of
fifty-four, heavy-shouldered, deep brown skin, in a matte dark olive
surface suit with faded sand-white bands at the shoulders and shins; the
helmet is a hard sand-white shell with a single flat front pane set inside
a visible dark rim — not a bubble, not a dome — the pane optically clear
with zero tint and zero mirror coating, his face fully readable in profile
through it. The back of the suit is one continuous smooth panel from collar
to hip, carrying nothing. A thin pale scratch runs along the left forearm
sleeve of the suit. His right glove is open and lowered onto a thin line
that runs from the last clamp on the frame down through the opening; the
line is straight and taut. His left glove is flat on the hatch frame; the
short two-jawed cutter lies on the deck beside his boot. A hooded hand-lamp
the size of his fist rides dark in a clip at his right hip. One clamp holds
the disused module, which hangs steeply from that single corner below the
opening. His glove palms, his knees and the outer face of his right forearm
sleeve are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the last clamp and
its taut line the right foreground.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The thin line is straight and taut — no sag, no curve,
no catenary, no sway. Exactly one clamp holds the module. No screens, no
dials, no gauges, no indicator lights. No readable text, letters, digits or
symbols anywhere in the frame; no scale marks, no graduation ticks; no
flag, no logo. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no rust.
No lens flare, no anamorphic streak. Metal static and solid — no melting,
no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 15 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip; the cutter stays on the deck beside his boot. One clamp
holds the module for the whole shot. His glove palms, knees and right
forearm sleeve are dulled with wear.

SCENE (as in the start frame): the bay, the open hatch, the module hanging
steeply from its last clamp, and the thin line running straight and taut
from that clamp down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 13.

TIMELINE: 0.0s — his open right glove is already lowered onto the taut line
and already sliding along it, moving toward the clamp. 2.0s — the glove
reaches the clamp and stops there; the line under it pulls hard against the
pin and a fast shiver runs down the line and out of the bottom of the
frame. 3.0s — his helmet, which had been turning back toward the module,
stops in the middle of the turn and does not finish it. 4.0s — his mouth
stays closed and his lower lip draws in; his eyes come down to the clamp
and stay there for a long beat. 8.0s — his right glove closes on the line
and holds it, his grip tightening and the glove's segments lifting over the
knuckles. 10.0s — hold; he does not move.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
thin line is straight and taut from the pin down out of frame — it does not
sag, it does not curve, it does not sway, it does not swing; the shiver
travels along it once and leaves the frame. Everything below the lip of the
hatch keeps moving downward — always the same direction, never rising,
never stopping, never held in place. Up is the rock ceiling above the base;
down is the black disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the dry rasp of the glove
sliding along the line; one hard tick as the line pulls against the pin;
one breath taken and held, then let out slowly. Nothing else — no sound
carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet and
hip lamp identical throughout; the front pane stays clear and unmirrored;
the back stays one continuous smooth panel with no backpack, tank, hose or
cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The thin
line never sags, never curves, never sways and never swings; it does not
break and it does not come loose. The clamp count stays one. No screens, no
dials, no gauges. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
dust, no suspended grit, no haze. No smoke, no exhaust, no flame, no spark,
no rust. No lens flare, no anamorphic streak. Metal static — no melting, no
warping. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 15 (S15) — PİMİN BAŞI · KURULUM B (makro) ⭐ TEMA MOTİFİ

> ⭐ **TEMA MOTİFİ — AŞINMA [TEMA §5 · ZAMAN satırı]:** pimin başı
> yıllarca elden geçmekten yuvarlanmış; hattın halkası o başın ALTINDA
> kalmış. Tohumun (S3 · 0:31) ödemesi burada yapılır [FINAL §3].
> Bekçinin yüzü bu kadrajda YOKTUR — ⭐VİRAL etiketi taşımaz.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 16 of 25.
Exactly one human figure — this film has exactly one human total, and in
this frame only his two gloved hands are in shot.

SCENE: a close view of the last matte grey clamp, the length of a hand,
bolted through its seat in the frame of an open square hatch in a bare grey
metal floor. The clamp's pin stands proud of the seat and its head is
rounded and polished smooth, its original edges gone. Under that rounded
head, held between the head and the seat, sits the spliced eye of a thin
line; the line drops away from it straight and taut, down through the
opening and out of the bottom of the frame. Two heavy segmented gloves are
in the frame and nothing else of the man: the right glove holds the line
just below the eye, his grip tight and its segments lifted over the knuckles; the
left glove is braced flat on the hatch frame. Both gloves run into the
sleeves as one piece at the wrist; the palms are dulled with wear and the
outer face of the right forearm sleeve is dulled too. Beyond the near edge
of the frame the opening drops away into black, and the dark bulk of the
disused module hangs at an angle in the lower right corner.

CAMERA & LIGHT: 85mm spherical lens, fixed 0.9 m above the pin, outside the
ring. High angle close-up looking down, deep focus. Two hooded work lamps
in the bay ceiling light the clamp and the gloves from above with cool
neutral white; the metal walls of the bay throw no second light, and the
shadows inside the bay are absolutely black with razor edges. Nothing
lights the opening from below. The clamp, the rounded pin head and the
held eye hold the centre of the frame, the two gloves the left and lower
bands, the black of the opening the right band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no other hands, no clone, no reflected figure. 0% bloom, no
glow filter, no soft focus. The gloves are heavy and segmented and run into
the sleeves as one piece at the wrist; no bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts keep a clear
structural boundary — no merging, no phasing, no extra fingers. The line's
eye is held under the rounded head and cannot pass over it. The line is
straight and taut — no sag, no curve, no catenary, no sway. No readable
text, letters, digits or symbols anywhere in the frame — not on the clamp,
the pin, the eye, the line, the glove or the hatch frame; no scale marks,
no graduation ticks, no engraved or painted characters of any kind; no
flag, no logo. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no heat glow. No lens flare, no anamorphic streak. Metal static and solid —
no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 16 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total, and in this shot only his two gloved hands are in frame.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: the two heavy segmented gloves
running into the sleeves as one piece at the wrist, palms and right forearm
sleeve dulled with wear; the last matte grey clamp and its rounded polished
pin head; the spliced eye of the thin line held under that head; the
bare grey hatch frame; the dark angled bulk of the module in the lower
right.

SCENE (as in the start frame): the last clamp bolted through its seat, the
line's eye held under the rounded pin head, the line dropping away
straight and taut through the opening, the right glove holding the line
just below the eye and the left glove braced flat on the frame.

CAMERA: 85mm spherical lens, fixed 0.9 m above the pin, outside the ring.
High angle close-up looking down, deep focus.

TIMELINE: 0.0s — the right glove is already holding the line just below the
eye and is already lifting it, taking the slack that is not there; his grip
tightens against the glove's own stiffness. 3.0s —
the eye rises a hair against the underside of the rounded head and stops
hard; it does not clear the head. 5.0s — the glove eases and the eye
settles back into its seat. 7.0s — the left glove shifts its bracing hold a
finger's width along the frame and settles again. 10.0s — hold; the eye is
where it was and nothing else moves.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
The clamp, the pin and the frame are rigid and do not flex. The thin line
is straight and taut from the pin down out of frame — it does not sag, it
does not curve, it does not sway, it does not swing; it holds one exact
line for the whole shot. All hand-surface contacts keep a clear structural
boundary. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; one hard tick as the eye
meets the underside of the pin head; the dry scrape of the bracing glove
along the frame; slow breathing. Nothing else — no sound carries in this
vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no other
hands, no clone. 0% bloom, no glow filter, no soft focus. The gloves stay
identical, segmented, and joined to the sleeves at the wrist; no bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts
keep a clear structural boundary — no merging, no phasing, no extra
fingers. The eye never clears the pin head and the line never comes free.
The line never sags, never curves, never sways. No spark, no heat glow, no
smoke, no molten metal, no flying chips. No readable text, letters or
digits anywhere in frame, on the clamp, pin, eye, line, glove or frame; no
scale marks, no ticks, no engraved characters; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 16 (S16) — ÇEKER 🕰️ KÜME#2 (1/2) · KURULUM C (dönüş · kaynak S14)
### ⭐ BAŞARISIZ DENEME #1 [D158 B2b]

> Kuralın en sert kanıtı burada verilir: ağzın altına inen hiçbir şey
> yukarı GELMEZ. Bekçi hattı iki eldivenle çeker.
> ⛔ **DÖNÜŞ + KÜME:** kamera metni birebir; S17 aynı kurulumda devam eder.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 17 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man braced at the far edge of an open square hatch in the floor of
a small grey vacuum work bay, seen from the side. He is a man of
fifty-four, heavy-shouldered, deep brown skin, in a matte dark olive
surface suit with faded sand-white bands at the shoulders and shins; the
helmet is a hard sand-white shell with a single flat front pane set inside
a visible dark rim — not a bubble, not a dome — the pane optically clear
with zero tint and zero mirror coating, his face fully readable in profile
through it. The back of the suit is one continuous smooth panel from collar
to hip, carrying nothing. A thin pale scratch runs along the left forearm
sleeve of the suit. Both gloves are closed around a thin line that runs
from the last clamp on the frame down through the opening; his arms are
straight, his shoulders are set back and his boots are planted wide on the
deck. The short two-jawed cutter lies on the deck beside his boot. A hooded
hand-lamp the size of his fist rides dark in a clip at his right hip. One
clamp holds the disused module, which hangs steeply from that single corner
below the opening. His glove palms, his knees and the outer face of his
right forearm sleeve are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the last clamp and
its taut line the right foreground.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The thin line is straight and taut — no sag, no curve,
no catenary, no sway. Exactly one clamp holds the module. No screens, no
dials, no gauges, no indicator lights. No readable text, letters, digits or
symbols anywhere in the frame; no scale marks, no graduation ticks; no
flag, no logo. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no rust.
No lens flare, no anamorphic streak. Metal static and solid — no melting,
no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 17 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip; the cutter stays on the deck beside his boot. One clamp
holds the module for the whole shot.

SCENE (as in the start frame): the bay, the open hatch, the module hanging
steeply from its last clamp, and the thin line running straight and taut
from that clamp down through the opening, held in both his gloves.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 15.

TIMELINE: 0.0s — both gloves are already closed on the line and already
pulling; his arms are straight and his shoulders are already set back.
3.0s — the second pull is slower than the first; his grip tightens, the
glove segments lift over the knuckles and his boots press harder into the
deck. 6.0s — his back leans
further and his hips drop; the line does not rise a finger's width. 9.0s —
he holds the pull, still leaning. 10.0s — hold; the line is exactly where
it was.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
The thin line is straight and taut from the pin down out of frame — it does
not sag, it does not curve, it does not sway, it does not swing; it holds
one exact line for the whole shot. Nothing that is below the lip of the
hatch comes back up: the line does not rise, not a finger's width, however
hard it is pulled. Everything below the lip keeps moving downward — always
the same direction, never rising, never stopping, never held in place. Up
is the rock ceiling above the base; down is the black disc below it. This
is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the long dry creak of the
line taking load, transmitted through the frame; the press and shift of
boots on the deck; breathing that gets shorter and harder. Nothing else —
no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet and
hip lamp identical throughout; the front pane stays clear and unmirrored;
the back stays one continuous smooth panel with no backpack, tank, hose or
cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The line
never rises, never stretches, never thins, never breaks and never comes
loose; it never sags, never curves, never sways. The module does not move.
The clamp count stays one. No screens, no dials, no gauges. No readable
text, letters or digits anywhere in frame; no scale marks, no ticks; no
flag, no logo. No subtitles, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no
anamorphic streak. Metal static — no melting, no warping. No voice, no music. No CGI aesthetic. Photorealistic, 35mm
film grain.
```

---

## 🎬 SAHNE 17 (S17) — GELMEZ 🕰️ KÜME#2 (2/2) · KURULUM C

> ⛔ **KÜME KLİBİ [ACI_YAYI §3 🕰️]:** kesme değil, bölünmüş TEK çekim.
> Kamera metni S16'nın metnidir; üstüne devam işareti eklendi.
> Kuvvet GÖVDEYE değil ZEMİNE yazılır — botlar kayar [POLİTİKA §4.1].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 18 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the same man braced at the far edge of the same open square hatch in
the same grey vacuum work bay, seen from the side, one moment later. He is
a man of fifty-four, heavy-shouldered, deep brown skin, in a matte dark
olive surface suit with faded sand-white bands at the shoulders and shins;
the helmet is a hard sand-white shell with a single flat front pane set
inside a visible dark rim — not a bubble, not a dome — the pane optically
clear with zero tint and zero mirror coating, his face fully readable in
profile through it. The back of the suit is one continuous smooth panel
from collar to hip, carrying nothing. A thin pale scratch runs along the
left forearm sleeve of the suit. Both gloves are still closed around the
thin line and his arms are still straight, but his boots have travelled: a
pair of bright scuff tracks runs across the dull deck behind them, and the
line is exactly where it was. The short two-jawed cutter lies on the deck.
A hooded hand-lamp the size of his fist rides dark in a clip at his right
hip. One clamp holds the disused module, which hangs steeply from that single
corner below the opening. His glove palms, his knees and the outer face of
his right forearm sleeve are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the last clamp and
its taut line the right foreground.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The thin line is straight and taut — no sag, no curve,
no catenary, no sway. Exactly one clamp holds the module. No screens, no
dials, no gauges, no indicator lights. No readable text, letters, digits or
symbols anywhere in the frame; no scale marks, no graduation ticks; no
flag, no logo. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no rust.
No lens flare, no anamorphic streak. Metal static and solid — no melting,
no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 18 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. One clamp holds the module for the whole shot. Two bright
scuff tracks stay on the deck behind his boots.

SCENE (as in the start frame): the bay, the open hatch, the module hanging
steeply from its last clamp, the thin line held in both his gloves, and the
scuff tracks his boots have already made on the deck.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus. Continues the previous clip
from its exact last frame — the same position, height and lens as Scene 15.

TIMELINE: 0.0s — he is already pulling and his boots are already sliding
toward the lip, a slow steady scrape across the deck. 3.0s — the slide
stops as his heels find a seam in the plating; his shoulders drop, his rear
boot loads, and the line has not risen at all. 5.0s — he lets the pull off in one long release and his shoulders come
forward. 7.0s — his gloves open and let the line go; it stays exactly where
it was, straight and taut. 9.0s — he lowers his helmet toward the opening.
10.0s — hold; he stays down and nothing moves.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
The thin line is straight and taut from the pin down out of frame — it does
not sag, it does not curve, it does not sway, it does not swing. Nothing
that is below the lip of the hatch comes back up: the line does not rise, a
whole body's weight on it moves only the body. Everything below the lip
keeps moving downward — always the same direction, never rising, never
stopping, never held in place. Up is the rock ceiling above the base; down
is the black disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the long dry scrape of boots
sliding across the deck; one hard knock as the heels catch the seam; a slow
release of held breath. Nothing else — no sound carries in this vacuum. No
voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet and
hip lamp identical throughout; the front pane stays clear and unmirrored;
the back stays one continuous smooth panel with no backpack, tank, hose or
cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The line
never rises, never stretches, never thins, never breaks; it never sags,
never curves, never sways. The module does not move. The clamp count stays
one. No screens, no dials, no gauges. No readable text, letters or digits
anywhere in frame; no scale marks, no ticks; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no anamorphic streak.
Metal static — no melting, no warping. No
voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 18 (S18) — HALKA VE BAŞ · KURULUM B (dönüş · kaynak S15)
### ⭐ BAŞARISIZ DENEME #2 · DÜZ CEVAP (24 sınırın 1'i)

> Halkayı pimin yuvarlanmış başından geçirmeye çalışır — geçmez. Sonra
> kesicinin çenesini pimin üstüne koyar ve durur. Bir sonraki sahne
> soruyu TAM ve rahatlatıcı biçimde kapatmaz; bu sınır filmin TEK düz
> cevabıdır ve kurulum bloğuna yığılmamıştır [SAHNE_ZINCIRI §4].
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 19 of 25.
Exactly one human figure — this film has exactly one human total, and in
this frame only his two gloved hands are in shot.

SCENE: a close view of the last matte grey clamp, the length of a hand,
bolted through its seat in the frame of an open square hatch in a bare grey
metal floor. The clamp's pin stands proud of the seat and its head is
rounded and polished smooth. Under that rounded head sits the spliced eye
of a thin line, and the line drops away from it straight and taut, down
through the opening and out of the bottom of the frame. Two heavy segmented
gloves are in the frame and nothing else of the man: the right glove has
the eye pinched between finger and thumb and has drawn it hard up against
the underside of the head; the left glove is braced flat on the hatch frame
beside the seat. Both gloves run into the sleeves as one piece at the
wrist; the palms are dulled with wear and the outer face of the right
forearm sleeve is dulled too. Beyond the near edge of the frame the opening
drops away into black, and the dark bulk of the disused module hangs at an
angle in the lower right corner.

CAMERA & LIGHT: 85mm spherical lens, fixed 0.9 m above the pin, outside the
ring. High angle close-up looking down, deep focus. Two hooded work lamps
in the bay ceiling light the clamp and the gloves from above with cool
neutral white; the metal walls of the bay throw no second light, and the
shadows inside the bay are absolutely black with razor edges. Nothing
lights the opening from below. The clamp, the rounded pin head and the
pinched eye hold the centre of the frame, the two gloves the left and lower
bands, the black of the opening the right band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no other hands, no clone, no reflected figure. 0% bloom, no
glow filter, no soft focus. The gloves are heavy and segmented and run into
the sleeves as one piece at the wrist; no bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts keep a clear
structural boundary — no merging, no phasing, no extra fingers. The eye is
still held under the rounded head and has not passed it. The line is
straight and taut — no sag, no curve, no catenary, no sway. No readable
text, letters, digits or symbols anywhere in the frame; no scale marks, no
graduation ticks, no engraved or painted characters of any kind; no flag,
no logo. No subtitles, no title card, no watermark. No dust, no suspended
grit, no haze. No smoke, no flame, no heat glow. No lens flare, no anamorphic streak. Metal static and solid — no
melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 19 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total, and in this shot only his two gloved hands are in frame.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: the two heavy segmented gloves
running into the sleeves as one piece at the wrist, palms and right forearm
sleeve dulled with wear; the last matte grey clamp and its rounded polished
pin head; the spliced eye pinched under that head; the bare grey hatch
frame; the dark angled bulk of the module in the lower right.

SCENE (as in the start frame): the last clamp, the rounded pin head, the
line's eye drawn hard up under it, the line dropping away straight and taut
through the opening.

CAMERA: 85mm spherical lens, fixed 0.9 m above the pin, outside the ring.
High angle close-up looking down, deep focus — the same position, height
and lens as Scene 16.

TIMELINE: 0.0s — the right glove is already working the eye against the
underside of the head, turning it a little one way and then the other.
3.0s — the eye rides up the shank and jams on the widest part of the
rounded head; it stops there and will not pass. 5.0s — the glove tries once
more, harder, his grip tightening and the segments lifting over the knuckles; the
eye does not pass. 6.0s — the glove lets go and the eye drops back into its
seat under the head. 8.0s — the right glove leaves the frame and comes back
with the short two-jawed cutter; it sets the open jaws around the pin,
below the eye, and stops there. 10.0s — hold; the jaws are on the pin and
nothing has been cut.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
The clamp, the pin and the frame are rigid and do not flex; the eye is
rigid and does not stretch or deform. The thin line is straight and taut
from the pin down out of frame — it does not sag, it does not curve, it
does not sway, it does not swing. All hand-surface contacts keep a clear
structural boundary. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the small hard grind of the
eye riding the pin head; two dry ticks as it jams and drops back; the flat
click of the cutter's jaws settling on the pin; slow breathing. Nothing
else — no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no other
hands, no clone. 0% bloom, no glow filter, no soft focus. The gloves stay
identical, segmented, and joined to the sleeves at the wrist; no bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts
keep a clear structural boundary — no merging, no phasing, no extra
fingers. The eye never passes the pin head; the line never comes free and
never breaks; it never sags, never curves, never sways. The pin does not
part in this shot. No spark, no heat glow, no smoke, no molten metal, no
flying chips. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks, no engraved characters; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 19 (S19) — KESER · KURULUM C (dönüş · kaynak S17)
### ⭐⭐ MERKEZÎ SEÇİM · 3:09 · ⭐VİRAL · ⭐ TEMA MOTİFİ (kinesik)

> ⭐ **VİRAL KAPISI [§2.4]:**
> **YÜZ:** gözler bir vuruş kapanır; açıldığında bakış aşağıda değil
> ileridedir (0,8 s).
> **HAREKET:** kesicinin çenesi kapanır, pim ayrılır, modül tek karede
> kadrajın altından çıkar; alttan gelen ışık vizörün üstünden hızla geçip
> gider.
> ⛔ **EN RED-RİSKLİ KARE [B6]** — 3:12. Nötr tarifi promptta birebir:
> kıvılcım 0 · ısı parlaması 0 · duman 0 · erimiş metal 0 · talaş 0.
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.
> ⭐ Işıktaki değişim bir DURUM DEĞİŞİMİ DEĞİLDİR: kaynak (aşağıdaki eski
> lamba) modülle birlikte HAREKET EDER ve hareketi kadrajda görünür.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 20 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the far edge of an open square hatch in the floor
of a small grey vacuum work bay, seen from the side. He is a man of
fifty-four, heavy-shouldered, deep brown skin, in a matte dark olive
surface suit with faded sand-white bands at the shoulders and shins; the
helmet is a hard sand-white shell with a single flat front pane set inside
a visible dark rim — not a bubble, not a dome — the pane optically clear
with zero tint and zero mirror coating, his face fully readable in profile
through it, his eyes open and level. The back of the suit is one continuous
smooth panel from collar to hip, carrying nothing. A thin pale scratch runs
along the left forearm sleeve of the suit. His right glove holds the short
two-jawed cutter with its jaws closed around the pin of the last matte grey
clamp; his left glove is flat on the hatch frame. Under the pin's rounded
head sits the spliced eye of a thin line, and the line drops away straight
and taut through the opening. A hooded hand-lamp the size of his fist rides
dark in a clip at his right hip. One clamp holds the disused module, which
hangs steeply from that single corner below the opening. His glove palms,
his knees and the outer face of his right forearm sleeve are dulled with
wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. A weak second light reaches him
from far below through the opening and lays one soft band along the
underside of his helmet rim. A low rim light separates his shoulders and
helmet from whatever is behind him; his silhouette never merges with the
background. He holds the left half of the frame, the open hatch the lower
band, the last clamp and its taut line the right foreground.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The pin is still whole and the module is still held.
The thin line is straight and taut — no sag, no curve, no sway. No spark,
no heat glow, no smoke, no molten metal, no flying chips. No screens, no
dials, no gauges. No readable text, letters, digits or symbols anywhere in
the frame; no scale marks, no graduation ticks; no flag, no logo. No
subtitles, no title card, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak.
Metal static and solid — no melting, no warping. No tilt-shift or miniature
look. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film
grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 20 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip for the whole shot. His glove palms, knees and right forearm
sleeve are dulled with wear.

SCENE (as in the start frame): the bay, the open hatch, the module hanging
steeply from its last clamp, the line's eye under the pin's rounded head,
and the line dropping away straight and taut through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 18.

TIMELINE: 0.0s — the cutter's jaws are already closed on the pin and his
right glove is already squeezing; his grip tightens and the glove's segments lift
over the knuckles. 2.0s — his eyes close for one beat. 3.0s — the tool's
two jaws close on the metal pin and the pin parts cleanly. The parted faces
are matt, flat and cold. 3.4s — the module simply begins to move downward and leaves
the frame under the lip in a single pass; the taut line goes down with it
and the eye slides off the parted pin. 4.0s — the weak second light that
had been coming up through the opening travels down the underside of his
helmet rim and away, and the opening below him is only black. 6.0s — his
eyes open; he is looking level and forward, not down. 10.0s — hold; he
stays crouched, the cutter still in his glove.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary. Below the lip the module is heavy
and carries further before it slows: it leaves the frame in one pass and
keeps going. The change in the light is not a fade — the source itself is
moving away downward, and it moves in one continuous direction, never
flickering, never pulsing. Up is the rock ceiling above the base; down is
the black disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard short bite of the
cutter through the frame; one deep receding groan through the deck as the
mass leaves the frame and the load goes; then only the fan and one long
breath. Nothing else — no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cut makes no spark, no heat glow, no smoke, no molten metal
and no flying chips; the parted faces are matt and flat. The module leaves
downward and never rises, never tumbles back, never breaks apart. The light
from below moves away downward — it never flickers, never pulses, never
strobes. No screens, no dials, no gauges. No readable text, letters or
digits anywhere in frame; no scale marks, no ticks; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 20 (S20) — İNİŞ 🕰️ KÜME#3 (1/2) · KURULUM E ⚡ ŞOK#2 (2 kademe)

> ⭐ **DORUK.** Ağzın altından aşağı: modül asılı alanın içinden iniyor,
> eski lamba onun üstünde, ve geçtiği her nesne bir an aydınlanıp geride
> kalıyor. Bu bir DURUM DEĞİŞİMİ değil, kaynağın YOLCULUĞUDUR.
> ⛔ Bu klip bir KÜMENİN birinci yarısıdır; S21 aynı kurulumda devam eder.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 21 of 25.
Exactly one human figure — this film has exactly one human total, and in
this frame only his boots and knees are in shot at the top edge.

SCENE: looking straight down through the open square hatch in the floor of
a small vacuum work bay. The four edges of the hatch frame the picture; at
the top edge, standing on the deck beside the lip, are the boots and knees
of a man in a matte dark olive surface suit with faded sand-white shin
bands. Below the lip the shaft is open black. Hanging in it, one under the
other and getting further apart with depth, are separate solid objects:
nearest the lip five matte grey clamps the length of a hand at five
different depths, then larger and vaguer shapes further down, then points.
Well below them, a disused cylinder is on its way down through them, tilted
and moving; a small hooded lamp rides on its flank with its cone pointing
down, and a thin line trails up from the cylinder into the dark above it.
The deeper a thing hangs below the lip, the less of the old lamp's light
reaches it: the near ones read as pale steel, the deep ones as faint amber,
the deepest as points only.

CAMERA & LIGHT: 24mm spherical lens, fixed 0.4 m above the lip of the
hatch, aimed straight down. Overhead top-down extreme wide shot, deep
focus. No bay light reaches below the lip; the only light in the shaft is
the small hooded lamp riding on the descending cylinder, and it falls off
quickly in every direction. The lip itself catches a hard cool edge from
the bay lamps above. The shadows are absolutely black with razor edges and
the metal of the frame throws no second light. The hatch frame holds the
outer band of the picture, the descending cylinder the centre, the five
clamps the upper centre column.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no one in the shaft, no reflected figure. 0%
bloom, no glow filter, no soft focus, no glow halo around the small lamp.
The hanging objects are separate solid things with hard edges, each one
countable — not sparks, not embers, not particles, not a dust column.
Exactly five clamps hang above the descending cylinder. No readable text,
letters, digits or symbols anywhere in the frame — not on the frame, the
clamps, the cylinder, the lamp or the line; no scale marks, no graduation
ticks, no survey markers; no flag, no logo. No subtitles, no title card, no
watermark. No dust, no haze. No smoke, no exhaust, no
flame, no spark, no heat glow. No lens flare, no anamorphic streak. Metal
static and solid — no melting, no warping.
No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 21 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total, and in this shot only his boots and knees are in frame at the
top edge.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, and only
his boots and knees are in shot — matte dark olive suit, faded sand-white
shin bands. The hatch frame, the five hanging clamps, the descending
cylinder, the small hooded lamp riding on its flank and the trailing line
stay exactly what they are.

SCENE (as in the start frame): the open shaft below the hatch; five clamps
hanging at five depths; a disused cylinder on its way down through them with a
small hooded lamp riding on its flank, cone pointing down, and a thin line
trailing up behind it. The deeper a thing hangs below the lip, the less of
the old lamp's light reaches it: the near ones read as pale steel, the deep
ones as faint amber, the deepest as points only.

CAMERA: 24mm spherical lens, fixed 0.4 m above the lip of the hatch, aimed
straight down. Overhead top-down extreme wide shot, deep focus.

TIMELINE: 0.0s — the cylinder is already well below the lip and already
moving down, the small lamp riding with it. 2.0s — it passes one of the
deep vague shapes; that shape is lit hard for a moment as the lamp goes by,
and then it is behind the light and dark again. 5.0s — it passes another,
much further down; the same brief lighting and the same going dark. 8.0s —
the cylinder is small now and still going down, more slowly than before,
and the light it carries reaches less and less of what it passes. 10.0s —
hold; it is still moving down and the five clamps above it have barely
moved at all.

PHYSICS: 0.40 g. Everything below the lip of the hatch keeps moving
downward for the whole shot — always the same direction, never rising,
never stopping, never held in place — but each thing moves less the deeper
it already is. The cylinder is heavy and carries further before it slows:
it covers about twenty body-lengths across these ten seconds and is still
going. The light is not fading; the source is travelling away downward, in
one continuous direction, never flickering, never pulsing. Up is the rock
ceiling above the base; down is the black disc below it. This is a vacuum:
no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; one very slow breath; and
nothing from the shaft at all — no sound carries in this vacuum. No voice,
no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
one in the shaft. 0% bloom, no glow filter, no soft focus, no glow halo
around the small lamp. The hanging objects are separate solid things with
hard edges, each countable — not sparks, not embers, not particles, not a
dust column; they never rise, never stop, never hang motionless, never
swirl. Exactly five clamps stay above the descending cylinder. The
cylinder never rises, never tumbles back, never breaks apart, never
explodes. The light moves away downward — it never flickers, never pulses,
never strobes. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
dust, no suspended grit, no haze. No smoke, no flame, no heat glow. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 21 (S21) — KARANLIK 🕰️ KÜME#3 (2/2) · KURULUM E
### ⭐⭐ BEDEL GÖRÜLÜR · ⭐ TEMA MOTİFİ (ışık) · ⛔ MUTLAK SESSİZLİK

> ⛔ **KÜME KLİBİ:** kesme değil, bölünmüş TEK çekim. Kamera metni S20'nin
> metnidir; devam işareti eklendi.
> ⛔ **SESSİZLİK BIÇAĞI KURGUDADIR [D180]:** aşağıdaki AUDIO satırı
> YEDEKTİR. MUZIK dosyasında `KURGUDA HARD MUTE: sn 209,0 – 219,0`
> yazılıdır ve teslimde üç eşikte ölçülür.
> ⭐ **B2 KAYIP SAHNESİ.** Bedel burada EKRANDADIR ve sayılabilir: ağzın
> altında beş kelepçe hâlâ asılı, ve hiçbiri aydınlanmıyor.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 22 of 25.
Exactly one human figure — this film has exactly one human total, and in
this frame only his boots and knees are in shot at the top edge.

SCENE: looking straight down through the open square hatch in the floor of
a small vacuum work bay. The four edges of the hatch frame the picture; at
the top edge, standing on the deck beside the lip, are the boots and knees
of a man in a matte dark olive surface suit with faded sand-white shin
bands, and the lip itself catches a hard cool edge from the bay lamps
above. Everything below the lip is black. Very far down, near the bottom of
the frame, there is a single small point of light: the hooded lamp, riding
on the disused cylinder, far beneath everything else, with its cone pointing
down and away. Its light reaches nothing on the way up. Between that point
and the lip the shaft is unbroken black, and the five clamps that hang
there cannot be seen at all.

CAMERA & LIGHT: 24mm spherical lens, fixed 0.4 m above the lip of the
hatch, aimed straight down. Overhead top-down extreme wide shot, deep
focus. There is no light in the shaft; the single distant point is the only
thing in it, and it lights nothing between itself and the camera. The lip
catches a hard cool edge from the bay lamps above. The shadows are
absolutely black with razor edges and the metal of the frame throws no
second light. The hatch frame holds the outer band of the picture, the
single point the lower centre, and black holds everything else.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no one in the shaft, no reflected figure. 0%
bloom, no glow filter, no soft focus, no glow halo, no lens bloom around
the distant point. The distant point is a small hard light source with a
hooded cone pointing away from the camera — not a star, not a flare, not a
spark, not an ember. Nothing between it and the lip is visible. No readable
text, letters, digits or symbols anywhere in the frame; no scale marks, no
graduation ticks; no flag, no logo. No subtitles, no title card, no
watermark. No dust, no suspended grit, no haze, no volumetric shaft of
light. No smoke, no exhaust, no flame, no heat glow. No lens flare, no
anamorphic streak. Metal static and solid — no melting, no warping. No
tilt-shift or miniature look. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 22 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total, and in this shot only his boots and knees are in frame at the
top edge.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, and only
his boots and knees are in shot — matte dark olive suit, faded sand-white
shin bands. The hatch frame, the unbroken black of the shaft and the single
distant point of light near the bottom of the frame stay exactly what they
are.

SCENE (as in the start frame): the open shaft below the hatch, black from
the lip all the way down, with a single small point of light very far below
— the hooded lamp riding on the disused cylinder, its cone pointing down and
away, lighting nothing on the way up.

CAMERA: 24mm spherical lens, fixed 0.4 m above the lip of the hatch, aimed
straight down. Overhead top-down extreme wide shot, deep focus. Continues
the previous clip from its exact last frame — the same position, height and
lens as Scene 21.

TIMELINE: 0.0s — the distant point is already moving down and away, very
slowly now. 4.0s — one boot at the top edge comes up, sets down again a
hand's width nearer the lip, and stays. 7.0s — the distant point has moved
a little further down and is a little smaller; nothing else in the frame
has changed. 10.0s — hold; the point is still going down and the shaft is
still black.

PHYSICS: 0.40 g. Everything below the lip of the hatch keeps moving
downward — always the same direction, never rising, never stopping, never
held in place — but each thing moves less the deeper it already is; the
cylinder is now deep and moves very little. The distant lamp's cone points
down and away from the camera, so it lights nothing between itself and the
lip. Up is the rock ceiling above the base; down is the black disc below
it. This is a vacuum: no air, no dust, no wind.

AUDIO: absolute silence from 0.0s to 10.0s — no fan, no breath, no contact,
no room tone, no music, no voice. (Backup only: the hard mute is applied in
the edit at 209.0–219.0 s and verified by measurement.)

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
one in the shaft. 0% bloom, no glow filter, no soft focus, no glow halo, no
lens bloom around the distant point. The distant point is a small hard
light source with a hooded cone pointing away — not a star, not a flare,
not a spark, not an ember; it never flickers, never pulses, never strobes,
never rises. Nothing between it and the lip becomes visible. No readable
text, letters or digits anywhere in frame; no scale marks, no ticks; no
flag, no logo. No subtitles, no watermark. No dust, no haze, no volumetric shaft of light. No smoke, no flame, no heat glow. No lens flare, no anamorphic streak. Metal static — no melting, no
warping. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 22 (S22) — SAP · KURULUM D (dönüş · kaynak S13)
### ⭐ SEÇİMDEN SONRAKİ SEÇİM #1 [D158]

> İş bitti: altı yuvanın altısı boş — ama biri boş değil. Kesilmiş altıncı
> kelepçenin gövdesi, SAP, hâlâ çerçeveye cıvatalı duruyor. Bekçi ona
> uzanır ve DOKUNMAZ. Bu bir karardır ve sonucu kalıcıdır: bu üssün
> altında artık asla bırakılmayacak tek parça odur.
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 23 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of a small square vacuum work bay, seen from the far
wall. The bay is bare grey metal; its floor carries one open square hatch
about one body-length on a side, set slightly right of centre, and below
the opening there is nothing at all — the shaft is black and empty. Around
the hatch frame sit six clamp seats. Five are bare. In the sixth, on the
far arc, the cut body of the last clamp is still bolted through its seat: a
short matte grey stub with a flat parted face where the pin was. Standing
on the near arc, a pace back from the lip, is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable through it, turned down to
the stub. The back of the suit is one continuous smooth panel from collar
to hip, carrying nothing. The short two-jawed cutter hangs in his right
glove; a hooded hand-lamp the size of his fist rides dark in a clip at his
right hip. A thin pale scratch runs along the left forearm sleeve of the
suit. His glove palms, his knees and the outer face of his right forearm
sleeve are dulled with wear.

CAMERA & LIGHT: 24mm spherical lens, fixed 5.0 m from him at the far wall
of the bay, eye-level and square on. Wide shot, deep focus. Two hooded work
lamps in the bay ceiling light the room from above with cool neutral white;
the metal walls of the bay throw no second light, and the shadows inside
the bay are absolutely black with razor edges. Nothing lights the opening
from below. A low rim light separates his shoulders and helmet from
whatever is behind him; his silhouette never merges with the background.
The hatch holds the lower centre-right, the figure the left third, the bare
ceiling the upper band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no crew, no reflected or doubled figure. 0%
bloom, no glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. Five clamp seats are bare and one carries a cut stub;
there is no module and no line. No screens, no dials, no gauges, no
keypads, no indicator lights. No readable text, letters, digits or symbols
anywhere in the frame; no scale marks, no graduation ticks; no flag, no
logo, no patch. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no rust.
No lens flare, no anamorphic streak. Metal static and solid — no melting,
no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 23 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. The cutter stays in his right glove; a hooded
hand-lamp stays dark in the clip at his right hip. Five clamp seats stay
bare and the sixth keeps its cut stub for the whole shot.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch with nothing below it, the ring of six clamp seats with one cut stub
still bolted through the sixth, and the man standing a pace back from the
lip.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus — the same position,
height and lens as Scene 14.

TIMELINE: 0.0s — he is already walking the near arc toward the stub in the right
background of the frame, one unhurried step. 3.0s — he reaches the far arc, stops beside the stub and
lowers into a crouch, the cutter still in his right glove. 5.0s — his left
glove comes out and stops a hand's width short of the stub, open, and stays
there. 7.0s — the glove closes on nothing and comes back to his knee. 9.0s
— he straightens up, leaving the stub where it is. 10.0s — hold; the stub
is still bolted through its seat.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
stub is rigid and bolted and does not move. Up is the rock ceiling above
the base; down is the black disc below it; the open hatch faces the black
disc. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; five dry boot contacts
transmitted through the deck; the soft creak of the knee joint as he
crouches and rises; slow breathing. Nothing else — no sound carries in this
vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; the front pane stays
clear and unmirrored; the back stays one continuous smooth panel with no
backpack, tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The stub stays bolted and is never removed, never cut, never
dropped. There is no module and no line anywhere in frame. No screens, no
dials, no gauges, no indicator lights. No readable text, letters or digits
anywhere in frame; no scale marks, no ticks; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no anamorphic streak.
Metal static — no melting, no warping. No
voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 23 (S23) — ÇÖZER · KURULUM C (dönüş · kaynak S19) ⭐VİRAL

> ⭐ **VİRAL KAPISI [§2.4]:**
> **YÜZ:** bir kez uzun ve yavaş nefes verir; kaşlar düşer, bakış
> sabitlenir (1,5 s).
> **HAREKET:** lamba klipsinden kurtulup avucun içinde bir tur döner.
> ⭐ Çehov kapanıyor: bu lamba S0'dan beri her karede kalçasındaydı.
> ⛔ Lamba bu sahnede SÖNÜKTÜR. Yanması S23→S24 SINIRINDA olur [D179].
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 24 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the far edge of an open square hatch in the floor
of a small grey vacuum work bay, seen from the side; below the opening
there is nothing at all. He is a man of fifty-four, heavy-shouldered, deep
brown skin, in a matte dark olive surface suit with faded sand-white bands
at the shoulders and shins; the helmet is a hard sand-white shell with a
single flat front pane set inside a visible dark rim — not a bubble, not a
dome — the pane optically clear with zero tint and zero mirror coating, his
face fully readable in profile through it. The back of the suit is one
continuous smooth panel from collar to hip, carrying nothing. A thin pale
scratch runs along the left forearm sleeve of the suit. His right glove is
at his right hip, closed around a hooded hand-lamp the size of his fist —
the lamp is dark and is still seated in its clip. His left glove rests flat
on his knee. The short two-jawed cutter lies on the deck beside his boot.
On the far arc of the ring a short matte grey stub is bolted through its
seat with a flat parted face where the pin was. His glove palms, his knees
and the outer face of his right forearm sleeve are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the stub the right
background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The hand-lamp is dark and unlit and is still in its
clip. There is no module and no line anywhere in frame. No screens, no
dials, no gauges. No readable text, letters, digits or symbols anywhere in
the frame; no scale marks, no graduation ticks; no flag, no logo. No
subtitles, no title card, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no
anamorphic streak. Metal static and solid — no melting, no warping. No
tilt-shift or miniature look. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 24 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. The cutter stays on the deck beside his
boot; the cut stub stays bolted on the far arc. His glove palms, knees and
right forearm sleeve are dulled with wear.

SCENE (as in the start frame): the bay, the open hatch with nothing below
it, the cut stub on the far arc, and his right glove closed around the dark
hooded hand-lamp still seated in the clip at his hip.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 20.

TIMELINE: 0.0s — his right glove is already closed around the dark lamp and
already pulling against the clip; his grip tightens against the glove's own
stiffness. 2.0s — the lamp comes free of the clip
and turns one full turn in his palm before his fingers close on it; it
stays dark. 4.0s — he lets out one long slow breath; his brows come down
and his gaze settles and stops moving. 7.0s — he brings the lamp across in
front of him and holds it in the closed right glove above his knee. 10.0s —
hold; the lamp is in his glove, still dark, and he does not move.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
lamp is a rigid object turning in his palm; it does not deform. Up is the
rock ceiling above the base; down is the black disc below it. This is a
vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard snap of the clip
letting go; the dull roll of the lamp turning against the glove; one long
slow breath out. Nothing else — no sound carries in this vacuum. No voice,
no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet and
cutter identical throughout; the front pane stays clear and unmirrored; the
back stays one continuous smooth panel with no backpack, tank, hose or
cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The
hand-lamp stays dark and unlit for the whole shot — it never switches on,
never flickers, never glows. The lamp is never dropped and never leaves his
glove. There is no module and no line anywhere in frame. No screens, no
dials, no gauges. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
dust, no suspended grit, no haze. No smoke, no exhaust, no flame, no spark,
no rust. No lens flare, no anamorphic streak. Metal static — no melting, no
warping. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 24 (S24) — BIRAKIR · KURULUM A
### ⭐⭐ KAPANIŞ İMAJI · 4:07 FİNAL VURUŞ KANITI · ⭐ TEMA MOTİFİ (nesne+ışık)

> ⭐ **AÇILIŞ-KAPANIŞ ÇİFTİ [ACILIS_KAPANIS §5]:** kompozisyon S0'ın
> AYNISIDIR — konum kilidi: açık eldiven aynı koordinatta. DEĞİŞEN TEK
> DEĞİŞKEN: avuçtan çıkan şey (eskimiş bir kelepçe → bekçinin kendi yanan
> lambası). Değişim FOVEAL MERKEZDEDİR.
> ⭐ **SON PLAN TİPİ:** İLK KADRAJA DÖNÜŞ [FINAL §2.2].
> ⭐ **FİNAL VURUŞ KANITI [D141] · 4:07:** ağzın altında SAYILABİLİR ALTI
> parlak nesne — beş kelepçe ve lamba. Sap kadrajın üst kenarında,
> çerçeveye cıvatalı, ve sayıya girmez.
> ⛔ Lamba bu karede ZATEN YANIYOR [D179: imaj promptu 0,0 saniyeyi yazar].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 25 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: an open square hatch in the floor of a small vacuum work bay,
photographed from directly above it. Filling the upper-left third of the
frame is a heavy segmented glove, palm down and already open, its fingers
spread; the glove runs into the sleeve as one piece at the wrist. Sitting
below the open glove, on the lower-right third line, is a hooded hand-lamp
the size of a fist, lit, its cone pointing straight down, hanging in the
mouth of the hatch about a hand's width under the fingers. Below the lamp,
lit by it and going away into the dark, hang five matte grey clamps the
length of a hand, one under the other at five different depths, each one
separate and countable; below the fifth there is only black. Along the
right edge of the frame is the top of his hip, and the lamp clip there is
empty. Along the upper edge of the frame the cut stub of the last clamp is
bolted through its seat with a flat parted face where the pin was. He is a
man of fifty-four, heavy-shouldered, deep brown skin, in a matte dark olive
surface suit with faded sand-white bands at the shoulders; the helmet is a
hard sand-white shell with a single flat front pane set inside a visible
dark rim — not a bubble, not a dome — the pane optically clear with zero
tint and zero mirror coating, his face fully readable through it as he
looks down past his own glove. A thin pale scratch runs along the left
forearm sleeve of the suit. The back of the suit is one continuous smooth
panel from collar to hip, carrying nothing. His glove palms, his knees and
the outer face of his right forearm sleeve are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 0.6 m above the lip of the
hatch, aimed straight down. Overhead top-down close-up, deep focus. Two
hooded work lamps in the bay ceiling light the glove and the lip from above
with cool neutral white; the metal walls of the bay throw no second light,
and the shadows inside the bay are absolutely black with razor edges. Below
the lip the only light is the lit hand-lamp itself, cool and near, and what
it reaches are the five clamps below it. A low rim light separates his
shoulders and helmet from whatever is behind him; his silhouette never
merges with the background. The glove holds the upper-left third, the lamp
the lower-right third line, the lit clamps the lower band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus, no glow halo around the lamp. Photorealistic
skin with pores — no airbrushing, no waxy texture. The front pane is clear
glass with zero tint, zero mirror coating and zero reflection. No
back-mounted unit, no backpack, no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. Exactly five
clamps hang below the lamp, each one separate and countable. The clip at
his hip is empty. No readable text, letters, digits or symbols anywhere in
the frame; no scale marks, no graduation ticks; no flag, no logo, no patch.
No subtitles, no title card, no watermark. No dust, no haze, no volumetric shaft of light. No smoke, no flame, no rust. No lens flare, no anamorphic streak. Metal static and solid
— no melting, no warping. No Unreal Engine
look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 25 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder bands, hard sand-white helmet with one
flat front pane in a visible dark rim, the pane optically clear and
reflection-free, his face readable, his back one continuous smooth panel
carrying nothing. The clip at his right hip stays empty. The cut stub stays
bolted along the upper edge of frame. His glove palms, knees and right
forearm sleeve are dulled with wear.

SCENE (as in the start frame): the open hatch seen from directly above; his
open glove in the upper-left third; a lit hooded hand-lamp a hand's width
under the fingers with its cone pointing straight down; below it five matte
grey clamps hanging one under the other at five different depths, lit by
that lamp, each one separate and countable.

CAMERA: 50mm spherical lens, fixed 0.6 m above the lip of the hatch, aimed
straight down. Overhead top-down close-up, deep focus — the same position,
height and lens as Scene 1.

TIMELINE: 0.0s — his glove is already open and the lit lamp is already free
of it, a hand's width below the spread fingers and moving down, its cone
pointing straight down. 1.0s — the lamp has gone about one body-length down
and is visibly slower; the five clamps below it are lit harder as it comes
nearer to them. 4.0s — across these three seconds it moves only a hand's
width further, still downward, still the same direction. 7.0s — his fingers
curl back in and the glove withdraws to the edge of frame; the lamp keeps
going down, slower again, and the five clamps stay lit below it. 10.0s —
hold; the lamp is still moving down, the five clamps are still there, and
nothing else in the frame moves.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second.
Everything below the lip of the hatch keeps moving downward for the whole
shot — always the same direction, never rising, never stopping, never held
in place — but each thing moves less the deeper it already is: the lamp
sinks about one body-length in the first second, then only a hand's width
across the next three seconds, then less. Up is the rock ceiling above the
base; down is the black disc below it. Everything released moves toward the
black disc, which fills the lower half of the frame on the same side as the
open hatch, and never toward the rock. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; one dry click as the glove's
seal ring releases; two slow breaths inside the helmet. Nothing else — no
sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus, no glow halo
around the lamp. Suit, helmet and cutter identical throughout; the front
pane stays clear and unmirrored; the back stays one continuous smooth panel
with no backpack, tank, hose or cable. The clip at his hip stays empty. No
bare skin anywhere: none above the collar seal, none at the wrist between
glove and sleeve, none at the ankle above the boot cuff. The lamp stays lit
for the whole shot — it never flickers, never pulses, never goes out; it
never rises, never stops, never hangs motionless, never drifts sideways,
never spins away. Exactly five clamps hang below it and the count never
changes. No readable text, letters or digits anywhere in frame; no scale
marks, no ticks; no flag, no logo. No subtitles, no watermark, no end card,
no credits. No dust, no suspended grit, no haze, no volumetric shaft of
light. No smoke, no flame, no rust. No lens flare, no
anamorphic streak. Metal static — no melting, no warping. No voice, no music. No CGI aesthetic. Photorealistic, 35mm
film grain.
```

---

> **FİLMİN SONU — S24 · 4:09.**
> ⛔ Son karede jenerik, başlık kartı, kapanış kartı ve filigran YOKTUR:
> SCREEN TEXT 0,0 saniye [D34 · D70 · D72].
> ⭐ Teslimde bakılacak tek kare: **4:07** — kadrajın altında ALTI parlak
> nesne sayılabilir olmalı [D141].
