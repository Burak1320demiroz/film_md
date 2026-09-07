# 🪢 THE STANDING WIRE — Duran Tel | BÖLÜM 1

## AI Production Bible — Self-Contained Prompts
### BÖLÜM 1: Sahne 0-12 (13 sahne) | 16:9 Yatay | Görsel + Video
### _"Bu film, en dipte duran birinin yukarıyı hâlâ ciddiye almasıyla ilgilidir."_

> **BÖLÜM 1 süresi:** Hook (9 s) + 12 sahne × 10 s = 129 saniye (0:00 – 2:09)
> **Toplam film:** 25 sahne = 249 saniye = 4:09
> **BÖLÜM 2:** `THE_STANDING_WIRE_BOLUM_2.md` (S13-S24)
> **Plan:** `THE_STANDING_WIRE_PLAN.md` — sayısal kilitler, ışık takvimi,
> risk kartları, açı yayı, B5 ve politika satırı orada.
> **Replik:** 0 — film tamamen sessiz (insan 0 · makine 0 · telsiz 0).

---

## ⚠️ BÖLÜM 1 ÜRETİM NOTLARI (promptlardan önce oku)

```
① TEL SARKMAZ — FİLMİN NOVUMU VE ÜRETİM KAPISI [plan 🧬]
   Modelin refleksi sarkan, sallanan, rüzgârda kıpırdayan bir kablodur.
   Çözüm POZİTİF cümle, her promptta birebir:
   "The wire is perfectly straight from the bottom of the frame to the top —
    it does not sag, it does not curve, it does not sway, it does not
    swing; it holds one exact vertical line for the whole shot."
   ⭐ S3 BU CÜMLENİN ÜRETİM KAPISIDIR. S3 temiz çıkmadan S0, S9 ve
     BÖLÜM 2 üretilmez [D73: novum render edilmezse film yoktur].

② İHLAL YANINDAKİ NORMALLE KANITLANIR [ONERME §3]
   Aynı karede tele bağlı olmayan her şey NORMAL düşer. S0 ve S3'te
   düşen çakıl bu yüzden vardır ve sayısı yazılır:
   "no more than six separate grains, each a distinct point, falling
    in a straight arc and settling within three seconds."
   ⛔ "swirl" kelimesi bu dosyanın hiçbir yerinde yok — yasak bloğunda bile.
   ⛔ Asılı toz, toz perdesi, toz şelalesi, ışık sütunu tozu: 0 kare [D143].

③ İNCE ATMOSFER — YUMUŞAK GÖLGE MEŞRUDUR [kart §3.2 · D41]
   Gölgeler zayıf ve yumuşak kenarlıdır ve bu bir render hatası DEĞİLDİR.
   Her prompta pozitif cümle: "shadow edges are soft and weak — this is
   correct for this thin air, not a rendering fault; the frame still
   holds high contrast." ⛔ "shadows absolutely black" BU BÖLÜMDE YAZILMAZ
   (o cümle vakum bloğudur ve BÖLÜM 2'de başlar).

④ YÜZEY RENGİ TEK CÜMLEDE, TEK BLOKTA [⛔ D176]
   "The rock is dark blue-grey basalt; the loose dust caught in its lees
    is pale gold." — yalnız SCENE/WORLD bloğunda.
   ⛔ LIGHT bloğu hiçbir yüzeye renk atamaz. Kontrast garantisi ÖZNEYİ
     tarif eder: "a low rim light separates her shoulders and helmet
     from the background."

⑤ IŞIK MIKNATISI — DÖRT KANAL [KART 9 · D104 · UZAMSAL §6.7]
   Yarıkta tek baskın ışık kaynağı yukarıdaki şerittir ve kadın ona
   doğru gidiyor. Model özneyi ışığa DÖNDÜRME eğilimindedir. Dört kanal
   her tırmanış promptunda gövdededir: hedef-dilim + omuz hattı +
   ışığa göre poz + yön negatifi.
   ⛔ İKİ YENİLGİ KURALI: iki redden sonra üçüncü yeniden yazım yok;
     kamera HEDEFE taşınır [UZAMSAL §6.8].

⑥ ÖLÇÜ PROMPT GÖVDESİNE GİRMEZ [D138 · D45]
   Metre, santimetre, derece, f-sayısı, çentik, skala: 0.
   Oranlar GÖVDE BOYUYLA yazılır ("a coil as wide as her helmet").
   ✅ Kamera MESAFESİ muaftır ("from four metres away").

⑦ ZORLANMA ELDİVENİN ÜSTÜNDE OKUNUR [⛔ D175]
   ✗ "the forearm tendons stand out through the glove"
   ✅ "the glove's ribbed segments tighten and lift over the knuckles"
   Yıpranma kilidi GİYSİ YÜZEYİNE yazılır, gövdeye değil:
   ✅ "a thin pale scratch on the left forearm SLEEVE of the suit"

⑧ KİR MERDİVENİ — TARİF İNER, ETİKET İNMEZ [D147 · ⛔ D155]
   S0-S3: yalnız botlar ve dizler tozlu.
   S4-S12: + her iki kolun ön yüzü ve dirsekler.
   Klip İÇİNDE sabit, sahneler ARASI monotonik, hiç azalmaz.
   ⛔ "Wear state: PHASE n" hiçbir prompta yazılmaz — model onu göğse basar.

⑨ İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [⛔ D179]
   I2V'de imaj t = 0'dır. Değişim taşıyan her sahnede (S3 · S9 · S12)
   imaj promptu video promptunun `0.0s —` satırıyla KELİME KELİME
   uyumludur; sahnenin SONUCUNU asla yazmaz.

⑩ TEK KLİBE DURUM DEĞİŞİMİ YAZILMAZ [KILAVUZ_REHBERI §7 · SAHNE_ZINCIRI §1]
   Bu bölümde tek klipte değişen tek şey KONUMDUR (bir cismin yeri),
   nitelik değil. Işık kademesi sahne SINIRINDA değişir, klip içinde değil.

⑪ UZUNLUK BANDI
   Video hedef 2.000-2.600 karakter; image bandı gözlemdir.
   TAVAN (~4.300) aşılmaz. 13 videonun 13'ü I2V (onaylı IMAGE start frame).

⑫ KURULUM SAYISI — BÖLÜM 1'de 5 (A · C · D · E · F) ✅ bant içi.
⑫b SAYACIN ÜÇ EVRESİ — promptların hızını bu belirler [PLAN ⚖️]
   S3-S6   yarık duvarı, dinlenmiş beden → kadın telden HIZLI, öne geçer
   S7-S12  üst teraslar, yorgunluk → tel onu yakalar; S9'da GEÇER
   S13-S15 masifin omzu, yürünebilir yamaç → kaybettiğini geri alır
   ⭐ Bu yüzden S13-S15 promptları TIRMANIŞ değil YÜRÜYÜŞ yazar.
   ⛔ Hiçbir sayı prompta girmez; evre yalnız ADIM TEMPOSU ve NEFES
     kadansı olarak görünür.

⑬ NOVUM TAŞIYICISI: TEL × kadının ona bir cisim asması → asılan cisim
   düşmez; tel boyunca sabit hızla YUKARI gider [ONERME §2 · plan 🧬].
   TEK KARE testinin nesnesi de TEL'dir — aynı nesne [D157].

⑭ UZUNLUK — BİLİNÇLİ SAPMA, KAYITLI [D74 · TUR 11 §5 ① aritmetiği]
   Bu dosyanın video promptları 2.600 hedef bandının üstünde, ~4.300
   TAVANIN altındadır. Sebep aritmetiktir ve depo onu kendi ölçtü:
     §5 negatif çekirdek        1.650 kr
     D79 kask/vizör bloğu        +320
     ────────────────────────────────
     kasklı sahne KALIBI         1.970 kr
   Sahneye ait tek kelime yazılmadan bandın 1.970'i doludur. Bu filmde
   kalıbın üstüne şunlar ZORUNLU olarak biner ve hiçbiri kısaltılamaz:
     · novum cümlesi (tel sarkmaz)            ~180 kr
     · KART 9 dört kanal (ışık mıknatısı)     ~330 kr
     · ortam kartı cümlesi (yumuşak gölge)    ~150 kr
     · D139 pozitif sırt yüzeyi                ~90 kr
     · D138 KAPSAMLI metin yasağı             ~210 kr
   Toplam ~2.930 — ölçülen bant tam burası. Kısaltmanın tek yolu bir
   KİLİDİ atmaktır ve her kilit bir dersin faturasıdır.
   ⛔ TAVAN AŞILMADI: en uzun video promptu 4.041 kr (< 4.300).
   ⚠️ Üretimde arka arkaya iki red gelirse önce PROB koşulur, prompt
     KISALTILMAZ — Third Dune'da beş red vardı ve en kısası da battı.
```

---

# 📖 BİBLE'LAR

---

## 🌍 WORLD BIBLE — THE SLOT (yarık)

```
GEZEGEN: adsız. Yerçekimi 0,42 g — yürüyüş GERÇEK ZAMANLI, ağır çekim
YOK [D44]; düşük yerçekimi yalnız düşen cismin yavaş ama DÜZ yayında
görünür. Atmosfer ~1,0 kPa, çok soğuk: ses boğuk, tizsiz, zayıf.
Gölgeler zayıf ve yumuşak kenarlı — MEŞRU, hata değil. Dolgu ışığı VAR
ve motivasyonlu (atmosferik saçılma). Rüzgâr hiçbir şeyi deviremez:
kumaş çırpmaz, kimse savrulmaz. Kaldırılan toz üç dört saniyede oturur.

⭐ MARS DEĞİLDİR: bu gezegenin tozu demir bakımından fakir, SOLUK ALTIN
gri silikattır; gök zirvede koyu çivit, ufka doğru soluk altın bir bant.

YARIK: dokuz kilometre derin, tabanda dar (bir kilometrenin altında),
ağızda dört kat geniş. İki duvar da basamaklı teras hâlinde yükselir.
Kaya koyu mavi-gri bazalt; kayanın rüzgâr altı ceplerinde biriken gevşek
toz soluk altın. Duvarlar ISLAK DEĞİL, parlak değil, mat.

MERDİVEN: kuzey duvarında, hattın kurulduğu günden kalma oyulmuş bir
basamak dizisi yukarı gider. UZAK bantta tek soluk çizgi olarak görünür
ve basamakları sayılmaz; YAKIN bantta kadraja giren basamaklar görünür.
⛔ "yüzlerce basamak" gibi sayısız çoğul hiçbir bantta yazılmaz.

TEL: kuzey duvarının yüzünden birkaç gövde boyu açıkta, dimdik iner ve
tabandaki PLAKAya oturur. Serçe parmağından kalın değil. Koyu, mat,
tek parça. DÜMDÜZ: sarkmaz, kıvrılmaz, sallanmaz, salınmaz.

PLAKA: tabanda, kayaya gömülü, mat gri, dairesel bir taban levhası.
Üstünde tek bir bağlantı kaburgası var. Üstünde ya da yanında YAZI,
RAKAM, İŞARET, ÇENTİK YOKTUR.

BARAKA: plakanın ekran-SOLUNDA, kayaya yaslanmış alçak gri bir kutu.
Ön yüzünde tek koyu pencere şeridi ve duvarında BİR BOŞ ASKI — kadının
elindeki halkanın biçiminde, kavisli, boş. HİÇ AÇILMAZ, içine girilmez,
yanında ikinci figür YOKTUR.

IŞIK: tabanda doğrudan güneş YOKTUR. Tek ışık yukarıdaki dar gök
şeridinden gelen dolaylı ışıktır: soğuk, mavi-gri, yönsüz, yumuşak.
Yükseldikçe karşı duvarın TEPESİ önce aydınlanır (ince altın şerit),
sonra ışık aşağı iner. Güneş DİSKİ hiçbir karede kadrajda değildir.
```

## 👤 CHARACTER BIBLE — hat bekçisi (promptlarda İSİMSİZ [D34])

```
Kadın, otuz sekiz. İnce, uzun boyunlu, geniş omuzlu, sıcak kahverengi
ten. Mat KOYU ARDUVAZ-MAVİ yüzey giysisi; omuzlarda ve inciklerde
solmuş kemik-beyazı şeritler. Sol ön kol MANŞETİNDE ince soluk bir
çizik (yıpranma kilidi — GİYSİ yüzeyinde, gövdede değil [D175]).

KASK: sert beyaz kabuk, ÖNDE TEK DÜZ PANEL, görünür koyu bir çerçevenin
içinde. ⛔ Kubbe değil, kavis değil, dikişsiz değil [D146].
Panel optik olarak berrak: sıfır ton, sıfır ayna kaplaması, sıfır çevre
yansıması. Yüzü her karede ve her baş açısında tam okunur [D79].

SIRT: DÜZ. Sırta monte ünite yok, sırt çantası yok, tank yok, hortum
yok, kablo yok, arka muhafaza yok.

ELDİVENLER: ağır, dilimli, koyu; bilekte giysiyle tek parça. Zorlanma
ELDİVENİN üstünde okunur: dilimler boğumların üstünde gerilir ve kalkar.

TAŞIDIĞI TEK ŞEY: SOL elinde, elle sarılmış bir tel halkası. Kaskının
genişliği kadar. Yıllarca tutulmaktan avuç yerleri parlamış. Cebe
girmez, sırta bağlanmaz, koltuk altına sıkışmaz — SOL ELİ SÜREKLİ
MEŞGULDÜR ve bu S0'dan S17'ye kadar her karede böyledir.

KİR: S0-S3 yalnız botlar ve dizler soluk altın tozlu.
     S4-S12 buna her iki kolun ÖN yüzü ve dirsekler eklenir. Hiç azalmaz.
```

## 🚫 NEGATİF ÇEKİRDEK — her prompta iner (yüzey üssü · ince atmosfer)

```
Single unbroken take, no cuts, no edits, no camera resets, no
transitions, no camera teleportation, no angle change. Exactly one human
character — no duplicates, no clones, no second person, no crew, no
figure at the shelter, no reflected or doubled figure. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible
texture. Photorealistic skin pores, sweat and fatigue retained — no
airbrushing, no waxy texture, identical bone structure throughout.
Equipment and clothing identical to the description — no drift, no gear
appearing or disappearing mid-shot; the helmet stays sealed and the
visor pane stays clear. Dust and wear staining stays fixed and never
shifts. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — not on the suit, not on the plate, not
on the shelter, and not on the ground, the rock, the wire or the sky.
Nothing in this world has been measured, labelled, marked out or
annotated by anyone: no scale marks, no graduation ticks, no survey
markers, no engraved or painted characters of any kind. No national
flag, no agency logo, no mission patch, no manufacturer marking. No
subtitles, no captions, no burned-in dialogue text, no title card, no
end card, no credits, no watermark. All hand-surface contacts keep a
clear structural boundary — no merging, no phasing, no extra fingers,
rigid-body collision throughout. All loose particles obey 0.42 g with
continuous physical momentum — never hovering, never frozen, never
flowing like liquid. Insulation and covers are rigid and taut — nothing
billows, nothing flaps. Terrain, sky and structures static and stable —
no melting terrain, no warping topology, no swimming texture. No
tilt-shift look, no miniature or toy-model read, no vertical band of
blur across the frame, no shallow depth of field on the canyon walls.
No Unreal Engine look, no CGI aesthetic, no video game aesthetic.
Photorealistic with 35mm film grain. No voice, no music.
```

---

# 🎬 SAHNELER

---

## 🎬 SAHNE 0 (S0) — HOOK: YARIĞIN DİBİ ⭐ KAPAK ANI (0:06)

> Kapı sahnesi [HOOK §7]: üç hook varyantı üretilir, en iyisi seçilir.
> Üretim 10 s, kurguda 9 s'ye kırpılır. **Katalizör burada DEĞİL** —
> burada yalnız kural görünür. Çakıl 3,0 s'de düşer.
> **S0 ÇIKIŞ SORUSU (plana yazılır, ekrana değil):** *"Bu tel neye bağlı
> ve neden düşen her şeyin tersine hiç kıpırdamıyor?"*

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 1 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: the floor of a canyon nine kilometres deep on a cold thin-aired
planet, seen from the ground looking almost straight up the gap. Two
dark blue-grey basalt walls rise in stepped terraces and fill the left
and right thirds of the frame, running out past the top edge; between
them the sky is a narrow bright slot, deep indigo at its centre, pale
gold along its edges. The rock is dark blue-grey basalt; the loose dust
caught in its lees is pale gold. Down the exact middle of that bright
slot, one dark wire runs from the top of the frame to the bottom, no
thicker than her little finger — perfectly straight, no sag, no curve, no
sway. It ends on a grey circular base plate set into the rock. In the
lower-left third, small and silhouetted, a woman of thirty-eight kneels
at the plate with her right glove on its single connecting rib; her
left glove holds a hand-turned coil of wire as wide as her helmet. She
wears a matte dark slate-blue surface suit with faded bone-white bands
at the shoulders and shins; the helmet is a hard white shell with a
single flat front pane inside a visible dark rim — not a bubble, not a
dome — the pane optically clear with zero tint and zero mirror coating,
her face fully readable through it. The back of the suit is one continuous smooth panel from collar to hip, carrying nothing. Only her boots and knees carry pale gold
dust. To her left a low grey shelter box leans against the rock, one
dark window strip on its face.

CAMERA & LIGHT: an extreme wide shot on a 24mm spherical lens from a
fixed position on the canyon floor four metres from her, set low and
angled steeply up the gap, f/8, deep focus. No direct sun reaches this
floor and no sun disc is in frame; the only light is cool indirect blue-
grey light falling from the bright slot above. Shadow edges are soft and
weak — correct for this thin air, not a rendering fault; the frame still
holds high contrast between the bright slot and the dark walls. A low
rim light separates her shoulders and helmet from the background. The bright slot holds the centre quarter of the frame, the two wall
masses the outer thirds, the figure the lower-left third.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human
figure — no second person, no duplicate, no figure at the shelter, no
reflected or doubled figure. 0% bloom, no glow filter, no soft focus —
every surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no waxy texture. The visor pane is clear glass with zero
tint, zero mirror coating and zero reflection. No back-mounted unit, no
backpack, no tank, no hose, no cable. The wire is perfectly straight — no
sag, no curve, no catenary, no sway, no coil hanging from it. No
readable text, letters, digits, numbers or symbols anywhere in the frame —
not on the suit, the plate, the shelter, the rock or the sky; no scale
marks, no graduation ticks, no survey markers. No flag, no logo, no
patch. No subtitles, no title card, no watermark. No suspended dust, no
dust curtain, no haze bank. Terrain and walls static and solid — no
melting, no warping. No tilt-shift look, no miniature or toy-model read.
No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 1 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, lean, warm brown skin, matte dark slate-blue
surface suit with faded bone-white shoulder and shin bands, hard white
helmet with one flat front pane in a visible dark rim, the pane
optically clear and reflection-free, her face readable, her back
silhouette flat with no back-mounted unit. A hand-turned coil of wire as
wide as her helmet stays in her LEFT glove the whole shot. Only her
boots and knees carry pale gold dust. The two wall masses, the bright
slot, the base plate and the shelter stay exactly where they are.

SCENE (as in the start frame): the canyon floor, the walls filling the
outer thirds, one dark wire running down the middle of the bright slot
to the base plate, the kneeling woman in the lower-left third.

CAMERA: 24mm lens, fixed on the canyon floor four metres from her, low
and angled steeply up the gap. Extreme wide shot.

TIMELINE: 0.0s — She is already working: her right glove turns the
single rib on the plate, one slow quarter turn, the glove's ribbed
segments tightening over the knuckles. Her left glove keeps the coil.
3.0s — A handful of loose grit breaks from a terrace high on the right
wall and falls past the wire: no more than six separate grains, each a
distinct point, each dropping in a straight arc at 0.42 g and settling
on the floor within three seconds. The wire does not move. 7.0s — She
straightens her back, her helmet tilting up along the wire toward the
bright slot, and holds. 10.0s — Hold; nothing else moves.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight from the bottom of the frame
to the top — it does not sag, it does not curve, it does not sway, it
does not swing; it holds one exact vertical line for the whole shot.

AUDIO: a wide, very low air tone; the dry click of the rib turning; the
grains landing faint and toneless; two calm helmet breaths. No voice,
no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no angle change. Exactly one human — no second person, none at
the shelter, no clone, no reflected figure. 0% bloom, no glow filter,
no soft focus. Suit, helmet and coil identical throughout; nothing
appears or disappears mid-shot; the visor stays clear and unmirrored;
the back stays flat with no backpack, tank, hose or cable. The wire
never sags, curves, sways or swings. Grains obey 0.42 g — never
hovering, never frozen, never flowing like liquid; no suspended dust,
no dust curtain. No readable text, letters or digits anywhere in the frame,
on the suit, plate, shelter, rock or sky; no scale marks, no ticks; no
flag, no logo; no subtitles, no watermark. Terrain static — no melting,
no warping. No tilt-shift or miniature look. No voice, no music. No
CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 1 (S1) — PLAKA VE BOTLAR ⭐ EL #1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 2 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: low on the canyon floor beside the grey circular base plate. In
the centre of the frame the plate sits flush in dark blue-grey basalt;
the loose dust caught in the rock's lees is pale gold. Rising out of the
plate and running straight up out of the top of the frame is one dark
wire, no thicker than a little finger — perfectly straight, no sag, no curve.
The woman of thirty-eight stands beside it, framed from mid-thigh up,
turned three-quarters away: matte dark slate-blue surface suit, faded
bone-white bands at the shoulders and shins, hard white helmet with a
single flat front pane inside a visible dark rim — not a bubble — the
pane optically clear with zero tint and zero mirror coating, her face
readable in profile through it. Her back silhouette is flat, with no
back-mounted unit of any kind. Her right glove rests open on the plate's
rib; her LEFT glove holds a hand-turned coil of wire as wide as her
helmet, hanging at her hip. A thin pale scratch runs along the left
forearm sleeve of the suit. Only her boots and knees carry pale gold
dust. Behind and above her the stepped terraces of the north wall climb
out of frame; far up, a narrow bright slot of indigo sky.

CAMERA & LIGHT: a wide shot on a 32mm spherical lens from a fixed
position on a rock two and a half metres from her boots, set just above
ground level and angled slightly up, f/5.6, deep focus. No direct sun
on this floor, no sun disc in frame; cool indirect blue-grey light from
the slot far above. Shadow edges are soft and weak — correct for this
thin air, not a rendering fault; the frame still holds high contrast.
A low rim light separates her shoulders and helmet from the background. The wire holds the centre line, the wall the upper two
thirds, the plate and her boots the lower band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing. The visor pane is clear with zero tint, zero mirror coating
and zero reflection; no back-mounted unit, no backpack, no tank, no
hose, no cable. The wire is perfectly straight — no sag, no curve, no
catenary, no sway. No readable text, letters, digits, numbers or symbols
anywhere in the frame — not on the suit, the plate, the rock or the sky; no
scale marks, no graduation ticks, no survey markers; no flag, no logo,
no patch. No subtitles, no title card, no watermark. No suspended dust,
no dust curtain, no haze. Rock and plate static and solid — no melting,
no warping. No tilt-shift look, no miniature read. No Unreal Engine
look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 2 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with faded bone-white shoulder and shin bands and a thin pale
scratch on the left forearm sleeve, hard white helmet with one flat
front pane in a visible dark rim, the pane optically clear and
reflection-free, her face readable, the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The hand-turned coil as wide as her helmet stays in
her LEFT glove the whole shot. Only boots and knees carry pale gold
dust. The plate, the wire and the terraces stay exactly where they are.

SCENE (as in the start frame): the base plate in the centre, the wire
running straight up out of frame, the woman beside it in three-quarter
profile.

CAMERA: 32mm lens, fixed on a rock two and a half metres from her
boots, just above ground level, angled slightly up. Wide shot.

TIMELINE: 0.0s — Her right glove is already flat on the plate's rib,
pressing down; the glove's ribbed segments tighten and lift over the
knuckles and the sleeve's fabric draws taut along the forearm. Her shoulders drop and come forward over the plate,
the forearm sleeve tightening as she leans into it, and her breath goes
out slowly on the press. Her left glove holds the coil steady at her hip. 3.5s — She
lifts the right glove clear of the rib, turns the palm over once and
lowers it again beside the rib, not on it. 6.5s — Her helmet turns a
few degrees toward the wire and holds there. 10.0s — Hold; her left
glove has not moved and the coil has not moved.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight from the plate to the top of
the frame — it does not sag, it does not curve, it does not sway, it
does not swing; it holds one exact vertical line for the whole shot.

AUDIO: a wide, very low air tone; the muffled press of a glove on
metal; one slow helmet breath. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, no clone, no reflected
figure. 0% bloom, no glow filter. Suit, helmet and coil identical
throughout; nothing appears or disappears mid-shot; the visor stays
clear and unmirrored; the back stays flat with no backpack, tank, hose
or cable. The coil never leaves her left glove. The wire never sags,
curves, sways or swings. No suspended dust, no dust curtain. No readable
text, letters or digits anywhere in the frame, on the suit, plate, rock or
sky; no scale marks, no ticks; no flag, no logo; no subtitles, no
watermark. Terrain static — no melting, no warping. No tilt-shift or
miniature look. No voice, no music. No CGI aesthetic. Photorealistic,
35mm film grain.
```

---

## 🎬 SAHNE 2 (S2) — BARAKA VE BOŞ ASKI 🌱 TOHUM (8,0-10,0 s)

> **TOHUM [FINAL §3]:** barakanın duvarındaki BOŞ ASKI. İki saniye
> görünür, periferikte durur, kadın ona BAKMAZ (bakış = cevap).
> Kadraj yüzdesi: %10,8-11,6 — pencere ✅.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 3 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: the canyon floor beside the low grey shelter box that leans
against the north wall. The woman of thirty-eight stands facing camera,
framed from the knees up, one pace back from the base plate: matte dark
slate-blue surface suit, faded bone-white bands at shoulders and shins,
a thin pale scratch on the left forearm sleeve, hard white helmet with a
single flat front pane inside a visible dark rim — not a bubble — the
pane optically clear with zero tint and zero mirror coating, her whole
face readable through it. The back of the suit is one continuous smooth panel from collar to hip, carrying nothing. Her LEFT glove holds a hand-turned coil of wire as
wide as her helmet; her right glove hangs open at her side. Only boots
and knees carry pale gold dust. Behind her right shoulder, in the
background and slightly out of the centre of attention, the shelter's
flat grey face carries one dark window strip and, beside it, ONE EMPTY
BRACKET — a curved metal cradle the exact shape of the coil in her hand,
holding nothing. To her left the dark wire runs straight up out of the
frame from the plate. The rock is dark blue-grey basalt; the loose dust
caught in its lees is pale gold.

CAMERA & LIGHT: a medium shot on a 35mm spherical lens from a fixed
position four metres in front of her at eye level, head-on, f/4, the
shelter behind her still legible. No direct sun on this floor, no sun
disc in frame; cool indirect blue-grey light from the bright slot far
above. Shadow edges are soft and weak — correct for this thin air, not
a rendering fault; the frame still holds high contrast. A low rim light
separates her shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no figure at or inside the shelter, no clone, no
reflected or doubled figure. 0% bloom, no glow filter, no soft focus.
Photorealistic skin with pores — no airbrushing. The visor pane is clear
with zero tint, zero mirror coating and zero reflection; no back-mounted
unit, no backpack, no tank, no hose, no cable. The bracket on the
shelter wall is EMPTY — it holds nothing at all. The wire is perfectly straight — no sag, no curve, no sway. No readable text, letters, digits,
numbers or symbols anywhere in the frame — not on the suit, the shelter, the
bracket, the plate, the rock or the sky; no scale marks, no graduation
ticks; no flag, no logo, no patch. No subtitles, no title card, no
watermark. No suspended dust, no haze. Shelter and rock static and solid
— no melting, no warping. No tilt-shift look, no miniature read. No
Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 3 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with faded bone-white bands and a thin pale scratch on the left
forearm sleeve, hard white helmet with one flat front pane in a visible
dark rim, the pane optically clear and reflection-free, her face
readable, the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The coil
as wide as her helmet stays in her LEFT glove. Only boots and knees
carry pale gold dust. The shelter, its dark window strip and the single
empty bracket beside it stay exactly where they are.

SCENE (as in the start frame): the woman head-on one pace back from the
plate, the shelter behind her right shoulder, the wire running straight
up out of frame at the left.

CAMERA: 35mm lens, fixed four metres in front of her at eye level,
head-on. Medium shot.

TIMELINE: 0.0s — She is already turning her head slowly from the wire
back toward the plate, her right glove closing and opening once at her
side. 4.0s — She shifts her weight from the left boot to the right, one
small settling step, and her shoulders drop a little. 8.0s — She turns
her helmet fully away to camera left, toward the wire, and holds; her
back is not to camera. Behind her right shoulder the empty bracket on
the shelter wall stays plainly in frame and she never looks at it. 10.0s
— Hold.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight — it does not sag, it does not
curve, it does not sway, it does not swing.

AUDIO: a wide, very low air tone; a faint steady hum from the shelter;
one boot settling on grit; one calm helmet breath. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, none at or inside the
shelter, no clone, no reflected figure. 0% bloom, no glow filter. Suit,
helmet and coil identical throughout; nothing appears or disappears
mid-shot; the visor stays clear and unmirrored; the back stays flat with
no backpack, tank, hose or cable. The bracket stays EMPTY for the whole
shot — nothing is placed in it, nothing hangs from it. The coil never
leaves her left glove. The wire never sags, curves or sways. No
suspended dust. No readable text, letters or digits anywhere in the frame,
on the suit, shelter, bracket, plate, rock or sky; no scale marks, no
ticks; no flag, no logo; no subtitles, no watermark. Shelter and terrain
static — no melting, no warping. No tilt-shift or miniature look. No
voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 3 (S3) — ⭐VİRAL #1 · KATALİZÖR: UÇ AYRILIYOR (3,0 s)

> ⛔ **ÜRETİM KAPISI.** Bu sahne temiz çıkmadan S0, S9 ve BÖLÜM 2
> üretilmez. KABUL: telin ucu plakadan ayrılıp SABİT HIZLA yükseliyor,
> tel sarkmıyor/sallanmıyor, aynı karede çakıl DÜŞÜYOR.
> RET: tel sarkarsa · uç düşerse · uç sallanırsa · çakıl asılı kalırsa.
>
> ⭐ **İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [D179]:** başlangıç karesinde uç
> HÂLÂ PLAKADADIR. Sahnenin sonucu (uç yukarıda) imaj promptunda YOKTUR.
>
> **⭐VİRAL #1 · YÜZ:** göz hattı üç saniyede ellerden tele kilitlenir,
> kaşlar bir kez yukarı gider, ağız kapalı kalır.
> **HAREKET:** uç kopar ve dört saniyede kendi çapının kırk katı
> yükselir; altındaki çakıl aşağı düşer — kadrajda iki zıt yön.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 4 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: a close view over the woman's right shoulder, down onto her two
gloved hands and the grey circular base plate set into dark blue-grey
basalt; the loose dust caught in the rock's lees is pale gold. Her right
glove is closed around the plate's single connecting rib, half a turn
from open, the glove's ribbed segments tightened and lifted over the
knuckles. Her LEFT glove holds a hand-turned coil of wire as wide as her
helmet, resting on her thigh. A thin pale scratch runs along the left
forearm sleeve of the matte dark slate-blue suit; the shoulder and back
that fall inside this frame are one continuous smooth panel, carrying
nothing. Rising out of the
plate at the centre of the frame and running straight up out of the top
edge is one dark wire, no thicker than a little finger, PERFECTLY STRAIGHT
with no sag and no curve — its lower end is STILL SEATED IN THE PLATE,
touching it. At the top-left of the frame, in soft focus, the lower rim
of her helmet: a hard white shell with a single flat front pane inside a
visible dark rim, the pane optically clear with zero tint and zero
mirror coating, part of her face readable through it. Only her knees
carry pale gold dust in this frame.

CAMERA & LIGHT: a close-up on a 50mm spherical lens from a fixed
position one and a quarter metres above and behind her right shoulder,
angled gently down onto the plate, f/2.8, the plate and both gloves
sharp. No direct sun on this floor, no sun disc in frame; cool indirect
blue-grey light from far above. Shadow edges are soft and weak —
correct for this thin air, not a rendering fault. A low rim light
separates her shoulder and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no second pair of hands, no reflected figure.
0% bloom, no glow filter, no soft focus on the plate. Photorealistic
gloves and skin with texture — no airbrushing, no melting fingers, no
extra fingers; the glove and the rib keep a clear structural boundary.
The visor pane is clear with zero tint and zero mirror coating; no
back-mounted unit, no backpack, no tank, no hose, no cable. The wire is
perfectly straight — no sag, no curve, no catenary, no sway — and its lower
end is still seated in the plate, not lifted, not floating. No readable
text, letters, digits, numbers or symbols anywhere in the frame — not on the
suit, the gloves, the plate, the wire or the rock; no scale marks, no
graduation ticks, no engraved characters. No flag, no logo, no patch. No
subtitles, no title card, no watermark. No suspended dust, no floating
grit. Plate and rock static and solid — no melting, no warping. No
tilt-shift look, no miniature read. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 4 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
her two gloves, the matte dark slate-blue sleeve with a thin pale
scratch on the left forearm sleeve, the shoulder and back in frame one
continuous smooth panel carrying nothing, the hand-turned coil as wide as
her helmet in her LEFT glove, the hard white helmet rim top-left with its
single flat clear pane, the grey base plate and its single rib.

SCENE (as in the start frame): both gloves on and beside the plate, the
dark wire rising from the plate straight up out of the top of the frame,
its lower end still seated in the plate.

CAMERA: 50mm lens, fixed one and a quarter metres above and behind her
right shoulder, angled gently down onto the plate. Close-up.

TIMELINE: 0.0s — Her right glove completes the last half turn on the
rib; the glove's ribbed segments tighten and lift over the knuckles, her
shoulder drops into the turn, and her breath is held through it.
3.0s — The rib comes free. The wire's lower end lifts clear of the plate
and begins to rise, straight up, at one slow steady pace, and keeps
rising for the rest of the shot without stopping and without swinging.
At the same instant a few grains of grit break off the plate's edge and
fall in straight arcs at 0.42 g — no more than six separate grains, each
a distinct point, settling on the rock within three seconds. 6.0s — Her
right glove opens and stays open, empty, below the rising end. Her LEFT
glove keeps the coil. 8.0s — The end has climbed past the top of the
frame; the wire still runs perfectly straight through the frame. 10.0s —
Hold; the wire is still rising and still perfectly straight.

PHYSICS: 0.42 g. Everything not attached to the wire falls normally:
the grains drop in straight arcs and settle. The wire itself rises —
it does not fall, it does not sag, it does not curve, it does not sway,
it does not swing; it holds one exact vertical line the whole shot.

AUDIO: a wide, very low air tone; one dry metallic release; the grains
landing faint and toneless; her breath catching once and going on. No
voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, no second pair of hands,
no clone. 0% bloom, no glow filter. Gloves, sleeve and coil identical
throughout; nothing appears or disappears mid-shot; the visor stays
clear and unmirrored. The glove and the rib keep a clear structural
boundary — no merging, no phasing, no extra fingers. The wire never
sags, curves, sways or swings and never falls; its end rises steadily
and never drops back. Grains obey 0.42 g — never hovering, never frozen,
never flowing like liquid; no suspended dust, no dust curtain. No
readable text, letters or digits anywhere in the frame, on the suit, gloves,
plate, wire or rock; no scale marks, no ticks; no flag, no logo; no
subtitles, no watermark. Plate and rock static — no melting, no warping.
No tilt-shift or miniature look. No voice, no music. No CGI aesthetic.
Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 4 (S4) — MERDİVENİN İLK BASAMAĞI ⭐ TEPKİ PLANI

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 5 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: at the foot of a cut stair on the north wall of the canyon. The
woman of thirty-eight stands facing camera, framed from the knees up,
her right boot already on the first cut step: matte dark slate-blue
surface suit, faded bone-white bands at shoulders and shins, a thin pale
scratch on the left forearm sleeve, hard white helmet with a single flat
front pane inside a visible dark rim — not a bubble — the pane optically
clear with zero tint and zero mirror coating, her whole face readable
through it. The back of the suit is one continuous smooth panel from collar to hip, carrying nothing. Her
LEFT glove holds a hand-turned coil of wire as wide as her helmet; her
right glove is closed on a cut handhold in the rock. Her boots, knees,
the fronts of both arms and both elbows carry pale gold dust. Behind
her, the stepped terraces of the wall climb out of the top of the frame;
the cut stair reads as a single pale line running up the dark rock,
its individual steps only visible in the near band. To camera left, at
the edge of the frame, the dark wire runs straight up, no thicker than
a little finger. The rock is dark blue-grey basalt; the loose dust
caught in its lees is pale gold.

CAMERA & LIGHT: a medium shot on a 35mm spherical lens from a fixed
position four metres in front of her at eye level, head-on, f/4, deep
enough that the wall behind stays legible. No direct sun at this depth
and no sun disc in frame; cool indirect blue-grey light from far above,
strongest at the top of the frame. Shadow edges are soft and weak —
correct for this thin air, not a rendering fault; the frame still holds
high contrast. A low rim light separates her shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure on the stair above or below her, no
reflected figure. 0% bloom, no glow filter, no soft focus.
Photorealistic skin with pores — no airbrushing. The visor pane is clear
with zero tint, zero mirror coating and zero reflection; no back-mounted
unit, no backpack, no tank, no hose, no cable. The wire is perfectly straight
— no sag, no curve, no sway. The stair reads as one pale line in the far
band — no countable rows of steps running to the horizon, no repeated
railings, no rope, no ladder. No readable text, letters, digits, numbers
or symbols anywhere in the frame — not on the suit, the rock, the stair or
the sky; no scale marks, no graduation ticks, no survey markers, no
painted route marks of any kind. No flag, no logo, no patch. No
subtitles, no title card, no watermark. No suspended dust, no haze.
Rock static and solid — no melting, no warping. No tilt-shift look, no
miniature read. No Unreal Engine look, no CGI aesthetic. Photorealistic,
35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 5 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with faded bone-white bands and a thin pale scratch on the left
forearm sleeve, hard white helmet with one flat clear front pane in a
visible dark rim, her face readable, the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The coil as wide as her helmet stays in her LEFT
glove. Boots, knees, the fronts of both arms and both elbows carry pale
gold dust. The cut stair, the wall and the wire stay where they are.

SCENE (as in the start frame): the woman head-on at the foot of the cut
stair, right boot on the first step, the wall climbing behind her.

CAMERA: 35mm lens, fixed four metres in front of her at eye level,
head-on. Medium shot.

TIMELINE: 0.0s — She is already mid-movement: her right glove pulls on
the cut handhold and her weight comes forward onto the right boot, the
glove's ribbed segments tightening over the knuckles. 3.0s — Her left
boot leaves the floor and finds the step above; her left glove holds the
coil away from the rock so it never touches. 6.0s — Her helmet lifts
and holds, her face turned up along the wall, and her shoulders stay
square to the rock. 10.0s — Hold; her chest rises and falls twice.

TARGET AND DIRECTION: her target is the notch of bright sky at the top
of this wall, straight up the same vertical line the wire holds. Her
shoulders stay square to the wall. The lit band is above and behind her
— the light rims the top of her helmet and her shoulders from behind.
She never turns toward the light, there is no direction reversal, and
she never faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight — it does not sag, it does not
curve, it does not sway, it does not swing.

AUDIO: a wide, very low air tone; boot grit on cut rock; the muffled
scrape of a glove on stone; two working helmet breaths. No voice, no
music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, none on the stair above
or below, no clone, no reflected figure. 0% bloom, no glow filter. Suit,
helmet and coil identical throughout; nothing appears or disappears
mid-shot; the visor stays clear and unmirrored; the back stays flat with
no backpack, tank, hose or cable. The coil never leaves her left glove
and never touches the rock. The wire never sags, curves or sways. Glove
and rock keep a clear structural boundary — no merging, no phasing. No
suspended dust, no dust curtain. No readable text, letters or digits
anywhere in the frame; no scale marks, no ticks, no painted route marks; no
flag, no logo; no subtitles, no watermark. Rock static — no melting, no
warping. No tilt-shift or miniature look. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 5 (S5) — BASAMAKLAR ⭐ YÜRÜYÜŞ #1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 6 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: low on a cut step of the north wall, a few hundred body-lengths
above the canyon floor. The woman of thirty-eight climbs away from
camera and slightly across it, seen full length from just above ground
level: matte dark slate-blue surface suit, faded bone-white bands at
shoulders and shins, a thin pale scratch on the left forearm sleeve,
hard white helmet with a single flat front pane inside a visible dark
rim — not a bubble — the pane optically clear with zero tint and zero
mirror coating, her face readable in three-quarter view. Her back
silhouette is one continuous smooth panel from collar to hip, unbroken,
carrying nothing. Her LEFT glove holds a hand-turned coil of wire as wide
as her helmet; her right glove is on the rock. Boots, knees, the fronts
of both arms and both elbows carry pale gold dust. The dark blue-grey
basalt wall fills the right two thirds of the frame and runs out past
the top edge; the loose dust caught in its lees is pale gold. At the
left edge, the dark wire runs straight up, no thicker than a little
finger. Far above, the bright slot of indigo sky is wider than it was at
the floor.

CAMERA & LIGHT: a wide shot on a 32mm spherical lens from a fixed
position on the step two and a half metres from her boots, set just
above the rock and angled slightly up, f/5.6, deep focus. No sun disc in
frame; cool indirect blue-grey light from above, and along the very top
of the far wall a first thin band of warmer light. Shadow edges are soft
and weak — correct for this thin air, not a rendering fault; the frame
still holds high contrast. A low rim light separates her shoulders and
helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure on the wall above or below, no
reflected figure. 0% bloom, no glow filter, no soft focus.
Photorealistic skin with pores — no airbrushing. The visor pane is clear
with zero tint, zero mirror coating and zero reflection; no back-mounted
unit, no backpack, no tank, no hose, no cable — the back of the suit is
one continuous smooth panel from collar to hip. The wire is perfectly straight — no sag, no curve, no sway. The stair reads as one pale line
in the far band — no countable rows of steps, no repeated railings, no
rope, no ladder. No readable text, letters, digits, numbers or symbols
anywhere in the frame; no scale marks, no graduation ticks, no survey
markers, no painted route marks. No flag, no logo, no patch. No
subtitles, no title card, no watermark. No suspended dust, no haze bank.
Rock static and solid — no melting, no warping. No tilt-shift look, no
miniature read. No Unreal Engine look, no CGI aesthetic. Photorealistic,
35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 6 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, matte dark slate-blue surface suit with faded
bone-white bands and a thin pale scratch on the left forearm sleeve,
hard white helmet with one flat clear front pane in a visible dark rim,
her face readable, and the back of the suit one continuous smooth panel
from collar to hip, carrying nothing. The coil as wide as her helmet
stays in her LEFT glove. Boots, knees, arm fronts and elbows carry pale
gold dust. The wall, the cut steps and the wire stay where they are.

SCENE (as in the start frame): the woman climbing the cut steps away
from camera, the wall filling the right two thirds, the wire at the left
edge.

CAMERA: 32mm lens, fixed on the step two and a half metres from her
boots, just above the rock, angled slightly up. Wide shot.

TIMELINE: 0.0s — She is already climbing: right boot up, left glove
swinging the coil clear of the rock, right glove finding the next
handhold. 3.0s — Two more steps at the same steady pace; her shoulders
stay level and square to the wall. 6.0s — She pauses with one boot
raised, holds for a beat, then sets it down and takes another step.
10.0s — Hold; she is still climbing, still moving away from camera.

TARGET AND DIRECTION: her target is the bright notch of sky at the top
of this wall, straight up the same vertical line the wire holds. Her
shoulders stay square to the wall. The lit band is above and behind her
— the light rims the top of her helmet and her shoulders from behind.
She never turns toward the light, there is no direction reversal, and
she never faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion, no bounding, no floating leaps. The thin air exerts no force:
her suit never stirs, nothing lifts or blows. The wire is perfectly straight
— it does not sag, it does not curve, it does not sway, it does not
swing.

AUDIO: a thinner, higher air tone than the canyon floor; steady boot
grit; the coil's wire ticking once against her hip; three working
helmet breaths. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no crane. Exactly one human — no second person, none above or
below on the wall, no clone, no reflected figure. 0% bloom, no glow
filter. Suit, helmet and coil identical throughout; nothing appears or
disappears mid-shot; the visor stays clear and unmirrored; the back
stays one smooth panel with no backpack, tank, hose or cable. The coil
never leaves her left glove. The wire never sags, curves or sways.
Glove, boot and rock keep a clear structural boundary — no merging, no
phasing. No suspended dust, no dust curtain. No readable text, letters
or digits anywhere in the frame; no scale marks, no ticks, no route marks;
no flag, no logo; no subtitles, no watermark. Rock static — no melting,
no warping. No tilt-shift or miniature look. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 6 (S6) — KARŞI DUVARDAN ⭐ ÖLÇEK KONTRASTI 1:10

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 7 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: seen from a ledge on the far, south wall of the canyon, looking
across the gap and down. The north wall fills the whole right half and
the bottom of the frame — dark blue-grey basalt in stepped terraces,
its faces going out of frame in both directions; the loose dust caught
in its lees is pale gold. On that wall, tiny, one human figure: the
woman of thirty-eight, less than a hundredth of the frame's height, in
a matte dark slate-blue surface suit with a hard white helmet, climbing
a cut stair that reads as a single pale line running up the dark rock.
A few body-lengths out from the wall face, one dark wire runs from the
bottom of the frame to the top in one exact vertical line — perfectly straight, no sag, no curve — passing her at her own height. In the upper
left, the gap between the walls opens onto the bright slot of indigo
sky; along the top edge of the far wall runs a first thin band of warmer
light. Below her the wall drops away into cool blue-grey shadow that
gives no floor.

CAMERA & LIGHT: an extreme wide shot on a 24mm spherical lens from a
fixed position on the south ledge four hundred metres from her, angled
gently down across the gap, f/8, deep focus, the near and far rock
equally sharp. No sun disc in frame; cool indirect blue-grey light in
the gap and one warm band along the top of the far wall. Shadow edges
are soft and weak — correct for this thin air, not a rendering fault;
the frame still holds high contrast. The wall holds the right half, the
open gap the upper left, the figure sits small at the centre right.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human
figure — no second person, no clone, no other climber, no figure on the
south ledge, no reflected or doubled figure. 0% bloom, no glow filter,
no soft focus. Equipment identical to the description; no back-mounted
unit, no backpack, no tank, no hose, no cable. The wire is perfectly straight
from the bottom of the frame to the top — no sag, no curve, no catenary,
no sway. The stair reads as one pale line — no countable rows of steps,
no repeated railings, no ropes, no ladders, no strings of lights. No
readable text, letters, digits, numbers or symbols anywhere in the frame —
not on the rock, the wire or the sky; no scale marks, no graduation
ticks, no survey markers, no painted route marks. No flag, no logo, no
patch. No subtitles, no title card, no watermark. No suspended dust, no
dust curtain, no haze bank filling the gap. Rock static and solid — no
melting, no warping, no swimming texture. No tilt-shift look, no
miniature or toy-model read, no vertical band of blur across the frame,
no shallow depth of field on the canyon walls — the far rock is as sharp
as the near rock. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 7 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
tiny on the far wall, in a matte dark slate-blue surface suit with a
hard white helmet; the north wall's terraces, the pale line of the cut
stair, the warm band along the top of the far wall, and the dark wire
running in one exact vertical line stay exactly where they are.

SCENE (as in the start frame): the canyon gap seen from the south ledge,
the north wall filling the right half and the bottom, the figure small
on it, the wire passing her at her own height.

CAMERA: 24mm lens, fixed on the south ledge four hundred metres from
her, angled gently down across the gap. Extreme wide shot.

TIMELINE: 0.0s — She is already climbing, one small steady figure
moving up the pale line of the stair, covering a little less than her
own height every two seconds. 4.0s — A single small stone comes loose
below her boots and falls down the wall face in a straight arc at 0.42
g, out of the bottom of the frame; it is one distinct point, not a
cloud, and nothing follows it. 7.0s — She keeps climbing at exactly the
same pace, without pausing, without looking down. 10.0s — Hold; she has
gained a little more than one of her own heights since the first frame.

PHYSICS: 0.42 g — the stone falls in a straight arc, slow but certain,
and never hovers, never drifts sideways, never flows. The thin air
exerts no force: nothing lifts, nothing blows, no cloth stirs. The wire
holds one exact vertical line for the whole shot — it does not sag, it
does not curve, it does not sway, it does not swing, and it does not
move with the falling stone.

AUDIO: a wide, thin, toneless air sound with no high frequencies; the
falling stone barely audible and gone; no breath at this distance. No
voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no drift, no parallax. Exactly one human — no second climber,
no clone, no figure on the south ledge, no reflected figure. 0% bloom,
no glow filter. Nothing appears or disappears mid-shot. The wire never
sags, curves, sways or swings. The stone obeys 0.42 g — never hovering,
never frozen, never flowing like liquid; it does not become a cloud, a
plume or a curtain of dust; no suspended dust anywhere in the frame. The
stair stays one pale line — no countable steps, no railings, no ropes.
No readable text, letters or digits anywhere in the frame; no scale marks,
no ticks, no route marks; no flag, no logo; no subtitles, no watermark.
Rock static — no melting, no warping, no swimming texture. No
tilt-shift, no miniature or toy-model read, no vertical band of blur —
the far rock is as sharp as the near rock. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 7 (S7) — BASAMAKLAR, DAHA YUKARI ⭐ NEFES #1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 8 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: low on a cut step of the north wall, higher than before. The
woman of thirty-eight stands full length, turned three-quarters away and
leaning into the rock with her right shoulder: matte dark slate-blue
surface suit, faded bone-white bands at shoulders and shins, a thin pale
scratch on the left forearm sleeve, hard white helmet with a single flat
front pane inside a visible dark rim — not a bubble — the pane optically
clear with zero tint and zero mirror coating, her face readable in
three-quarter view. Her back silhouette is one continuous smooth panel
from collar to hip, carrying nothing. Her LEFT glove holds a hand-turned coil of wire as wide as her helmet, hanging low; her right glove presses
flat on the rock at shoulder height. Boots, knees, arm fronts and elbows
carry pale gold dust. The dark blue-grey basalt fills the right two
thirds and runs out past the top edge; the loose dust in its lees is
pale gold. At the left edge, the dark wire runs straight up, no thicker
than a little finger. Above and beyond, the far wall's upper third
carries a clear warm band of direct light; her own level is still cool
and shadowed.

CAMERA & LIGHT: a wide shot on a 32mm spherical lens from a fixed
position on the step two and a half metres from her boots, just above
the rock, angled slightly up, f/5.6, deep focus. No sun disc in frame.
Cool indirect blue-grey light on her; a warm band high on the far wall
behind her. Shadow edges are soft and weak — correct for this thin air,
not a rendering fault; the frame still holds high contrast. A low rim
light separates her shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure above or below on the wall, no
reflected figure. 0% bloom, no glow filter, no soft focus.
Photorealistic skin with pores, sweat and fatigue retained — no
airbrushing. The visor pane is clear with zero tint, zero mirror coating
and zero reflection; no back-mounted unit, no backpack, no tank, no
hose, no cable — the back of the suit is one continuous smooth panel.
The wire is perfectly straight — no sag, no curve, no sway. The stair reads
as one pale line in the far band — no countable steps, no railings, no
ropes. No readable text, letters, digits, numbers or symbols anywhere in the frame; no scale marks, no graduation ticks, no route marks. No flag, no
logo, no patch. No subtitles, no title card, no watermark. No suspended
dust, no haze. Rock static and solid — no melting, no warping. No
tilt-shift look, no miniature read. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 8 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, matte dark slate-blue surface suit with faded
bone-white bands and a thin pale scratch on the left forearm sleeve,
hard white helmet with one flat clear front pane in a visible dark rim,
her face readable, the back of the suit one continuous smooth panel
carrying nothing. The coil as wide as her helmet stays in her LEFT
glove. Boots, knees, arm fronts and elbows carry pale gold dust. The
wall, the wire and the warm band high on the far wall stay where they
are.

SCENE (as in the start frame): the woman leaning into the rock on a cut
step, the wall filling the right two thirds, the wire at the left edge.

CAMERA: 32mm lens, fixed on the step two and a half metres from her
boots, just above the rock, angled slightly up. Wide shot.

TIMELINE: 0.0s — She is already stopped and breathing: her shoulders
and chest rise and fall visibly, four full breaths across the shot, each
one lifting the bone-white band on her shoulder a little. 3.0s — Her
right glove slides a hand's width down the rock and grips again; the
glove's ribbed segments tighten and lift over the knuckles. 6.5s — Her
helmet turns up along the wall and holds there; her shoulders stay
square to the rock. 10.0s — Hold; the breathing continues at the same
slow rate.

TARGET AND DIRECTION: her target is the bright notch of sky at the top
of this wall, straight up the same vertical line the wire holds. Her
shoulders stay square to the wall. The lit band is above and behind her
— the light rims the top of her helmet and her shoulders from behind.
She never turns toward the light, there is no direction reversal, and
she never faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight — it does not sag, it does not
curve, it does not sway, it does not swing.

AUDIO: a thin, toneless air sound with no high frequencies; four slow
working helmet breaths, close and dry; one glove sliding on rock. No
voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, none above or below, no
clone, no reflected figure. 0% bloom, no glow filter. Suit, helmet and
coil identical throughout; nothing appears or disappears mid-shot; the
visor stays clear and unmirrored; the back stays one smooth panel with
no backpack, tank, hose or cable. The coil never leaves her left glove.
The wire never sags, curves or sways. Glove and rock keep a clear
structural boundary — no merging, no phasing. No suspended dust, no
dust curtain. No readable text, letters or digits anywhere in the frame; no
scale marks, no ticks, no route marks; no flag, no logo; no subtitles,
no watermark. Rock static — no melting, no warping. No tilt-shift or
miniature look. No voice, no music. No CGI aesthetic. Photorealistic,
35mm film grain.
```

---

## 🎬 SAHNE 8 (S8) — CEPHEDEN TIRMANIŞ

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 9 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: on the cut stair of the north wall, roughly a third of the way
up the canyon. The woman of thirty-eight climbs directly toward camera,
framed from the knees up: matte dark slate-blue surface suit, faded
bone-white bands at shoulders and shins, a thin pale scratch on the left
forearm sleeve, hard white helmet with a single flat front pane inside a
visible dark rim — not a bubble — the pane optically clear with zero
tint and zero mirror coating, her whole face readable through it. Her
back silhouette is flat with no back-mounted unit. Her LEFT glove holds
a hand-turned coil of wire as wide as her helmet, held out slightly from
her hip; her right glove is raised to a cut handhold. Boots, knees, arm
fronts and elbows carry pale gold dust. Behind and below her the dark
blue-grey basalt drops away out of the bottom of the frame; the loose
dust caught in its lees is pale gold. To camera right, close to the
frame edge, the dark wire runs straight up, no thicker than a little
finger. Above her the gap is wide and bright with indigo sky, and the
top band of the frame carries warm direct light on the opposite rock.

CAMERA & LIGHT: a medium shot on a 35mm spherical lens from a fixed
position four metres up the stair from her at eye level, head-on, f/4.
No sun disc in frame. Cool indirect blue-grey light on her face and
suit; warm direct light only in the top band of the frame. Shadow edges
are soft and weak — correct for this thin air, not a rendering fault;
the frame still holds high contrast. A low rim light separates her
shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure on the stair behind her, no reflected
figure. 0% bloom, no glow filter, no soft focus. Photorealistic skin
with pores, sweat and fatigue retained — no airbrushing. The visor pane
is clear with zero tint, zero mirror coating and zero reflection; no
back-mounted unit, no backpack, no tank, no hose, no cable. The wire is
perfectly straight — no sag, no curve, no sway. The stair reads as cut rock —
no railings, no ropes, no ladders, no cables strung along it. No
readable text, letters, digits, numbers or symbols anywhere in the frame; no
scale marks, no graduation ticks, no route marks. No flag, no logo, no
patch. No subtitles, no title card, no watermark. No suspended dust, no
haze. Rock static and solid — no melting, no warping. No tilt-shift
look, no miniature read. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 9 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with faded bone-white bands and a thin pale scratch on the left
forearm sleeve, hard white helmet with one flat clear front pane in a
visible dark rim, her face readable, the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The coil as wide as her helmet stays in her LEFT
glove. Boots, knees, arm fronts and elbows carry pale gold dust. The
wall, the cut stair and the wire stay where they are.

SCENE (as in the start frame): the woman climbing the cut stair straight
toward camera, the wall dropping away behind her, the wire close to the
right frame edge.

CAMERA: 35mm lens, fixed four metres up the stair from her at eye level,
head-on. Medium shot. The camera is at her target, and she climbs
toward it.

TIMELINE: 0.0s — She is already climbing toward camera: right glove
pulls on the handhold, right boot rises, weight transfers, and her whole
body comes a little larger in frame. 3.5s — Two more steps at the same
steady pace; her left glove keeps the coil out from her hip so it never
strikes the rock. 7.0s — She takes one step, stops with both boots
planted, and her chest rises twice. 10.0s — Hold; she is a clear step
closer than in the first frame.

TARGET AND DIRECTION: her target is the camera position at the top of
this stretch of stair, straight up the same vertical line the wire
holds. Her shoulders stay square to the wall. The lit band is above and
behind her — the light rims the top of her helmet and her shoulders from
behind. She never turns toward the light, there is no direction
reversal, and she never faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion, no bounding, no floating leaps. The thin air exerts no force:
her suit never stirs, nothing lifts or blows. The wire is perfectly straight
— it does not sag, it does not curve, it does not sway, it does not
swing.

AUDIO: a thin, toneless air sound; steady boot grit; the glove's grip on
cut stone; three working helmet breaths. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no dolly. Exactly one human — no second person, none on the
stair behind her, no clone, no reflected figure. 0% bloom, no glow
filter. Suit, helmet and coil identical throughout; nothing appears or
disappears mid-shot; the visor stays clear and unmirrored; the back
stays flat with no backpack, tank, hose or cable. The coil never leaves
her left glove. The wire never sags, curves or sways. Glove, boot and
rock keep a clear structural boundary — no merging, no phasing. No
suspended dust, no dust curtain. No readable text, letters or digits
anywhere in the frame; no scale marks, no ticks, no route marks; no flag,
no logo; no subtitles, no watermark. Rock static — no melting, no
warping. No tilt-shift or miniature look. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 9 (S9) — ⭐ NOVUM DOĞRULAMA: UÇ GÖZ HİZASINDAN GEÇİYOR

> ⛔ **ÜRETİM KAPISI.** Kural İKİNCİ NESNEDE kanıtlanır [ONERME §5].
> KABUL: bağlantı parçası kadının göz hizasından SABİT HIZLA YUKARI
> geçiyor, eli boşa gidiyor, tel sarkmıyor.
> RET: parça düşerse · asılı kalırsa · sallanırsa · eline gelirse.
> ⭐ **İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [D179]:** başlangıç karesinde parça
> göz hizasının hemen ALTINDADIR ve eli henüz uzanmamıştır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 10 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: a close view over the woman's left shoulder on a cut step of the
north wall, roughly half way up the canyon. Her hard white helmet fills
the left third of the frame in profile: a single flat front pane inside
a visible dark rim — not a bubble — the pane optically clear with zero
tint and zero mirror coating, her eye and cheek fully readable through
it. She wears a matte dark slate-blue surface suit with a faded
bone-white shoulder band and a thin pale scratch on the left forearm
sleeve; her back is one continuous smooth panel carrying nothing. Her
right glove is beginning to lift, still below her chin, fingers
half-open. In the centre and right of the frame, a few body-lengths out
in the canyon's air, one dark wire runs from the bottom of the frame to
the top in one exact vertical line — perfectly straight, no sag, no curve.
Clamped to that wire is a small dull grey connecting fitting, a
plain rounded block no bigger than her fist; it sits JUST BELOW the
level of her eyes. Beyond the wire the far wall is a soft cool blue-grey
mass with a warm band along its top edge. The rock is dark blue-grey
basalt; the loose dust caught in its lees is pale gold.

CAMERA & LIGHT: a close-up on a 50mm spherical lens from a fixed
position one and a quarter metres above and behind her left shoulder,
angled gently down and out toward the wire, f/2.8, her helmet and the
fitting both sharp, the far wall soft. No sun disc in frame. Cool
indirect blue-grey light on her; a warm band high behind. Shadow edges
are soft and weak — correct for this thin air, not a rendering fault. A
low rim light separates her shoulder and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no second pair of hands, no reflected figure.
0% bloom, no glow filter, no soft focus on the helmet or the fitting.
Photorealistic skin with pores — no airbrushing. The visor pane is clear
with zero tint, zero mirror coating and zero reflection; no back-mounted
unit, no backpack, no tank, no hose, no cable. The wire is perfectly straight
— no sag, no curve, no catenary, no sway — and the fitting is clamped
to it, not floating free beside it, and it sits just BELOW her eye
level. No readable text, letters, digits, numbers or symbols anywhere in the frame — not on the suit, the glove, the fitting, the wire or the rock;
no scale marks, no graduation ticks, no engraved characters. No flag,
no logo, no patch. No subtitles, no title card, no watermark. No
suspended dust, no floating grit. Rock static and solid — no melting, no
warping. No tilt-shift look, no miniature read. No Unreal Engine look,
no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 10 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
her hard white helmet in profile at the left with one flat clear front
pane in a visible dark rim, her eye and cheek readable, the matte dark
slate-blue suit with a faded bone-white shoulder band and a thin pale
scratch on the left forearm sleeve, her back one continuous smooth panel
carrying nothing. The dark wire runs in one exact vertical line; the
small dull grey fitting is clamped to it just below her eye level.

SCENE (as in the start frame): her helmet in profile at the left, the
wire and the fitting at centre right, the far wall soft beyond.

CAMERA: 50mm lens, fixed one and a quarter metres above and behind her
left shoulder, angled gently down and out toward the wire. Close-up.

TIMELINE: 0.0s — The fitting is already rising, straight up the wire at
one slow steady pace, and it does not stop. Her right glove lifts toward it, fingers opening; her weight goes onto the
forward boot and her shoulder rises with the reach. 3.0s — The fitting passes exactly level with her
eyes; her glove is still a hand's width short of it. Her eye follows it
without her head turning. 5.0s — Her glove closes on empty air below the
fitting and stays closed there. The fitting keeps rising at exactly the
same pace. 7.5s — Her helmet tilts up to follow it and holds; the
fitting is now well above her head and still going. 10.0s — Hold; the
fitting is still rising and the wire is still perfectly straight.

PHYSICS: 0.42 g. Anything not attached to the wire would fall — the
fitting is clamped to the wire and rises instead, at one constant slow
pace, without stopping, without slowing and without swinging. The wire
holds one exact vertical line the whole shot: it does not sag, it does
not curve, it does not sway, it does not swing, and it does not move
when her glove passes near it.

AUDIO: a thin, toneless air sound; one dry tick as the fitting clears a
strand; her breath held for a beat and then released. No voice, no
music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, no second pair of hands,
no clone, no reflected figure. 0% bloom, no glow filter. Suit, helmet
and fitting identical throughout; nothing appears or disappears
mid-shot; the visor stays clear and unmirrored; the back stays one
smooth panel with no backpack, tank, hose or cable. The fitting NEVER
falls, never hovers, never reverses, never reaches her glove and never
leaves the wire; it rises steadily for the whole shot. Her glove and the
wire keep a clear structural boundary — no merging, no phasing, no extra
fingers. The wire never sags, curves, sways or swings. No suspended
dust, no floating grit. No readable text, letters or digits anywhere in the frame, on the suit, glove, fitting, wire or rock; no scale marks, no
ticks; no flag, no logo; no subtitles, no watermark. Rock static — no
melting, no warping. No tilt-shift or miniature look. No voice, no
music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 10 (S10) — BAŞINI KALDIRIR ⭐ GÖZ #2 · KULESHOV B

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 11 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: on the cut stair of the north wall, above the half-way terraces.
The woman of thirty-eight stands facing camera, framed from the chest
up, both boots planted, her head tilted back: matte dark slate-blue
surface suit, faded bone-white band at the shoulders, a thin pale
scratch on the left forearm sleeve, hard white helmet with a single flat
front pane inside a visible dark rim — not a bubble — the pane optically
clear with zero tint and zero mirror coating, her whole face fully
readable through it, both eyes open and turned upward. Her back
silhouette is flat with no back-mounted unit. Her LEFT glove holds a
hand-turned coil of wire as wide as her helmet, just inside the bottom
edge of the frame; her right glove hangs open. Her arm fronts and elbows
carry pale gold dust. Behind her the dark blue-grey basalt rises and
leaves the frame at the top; the loose dust in its lees is pale gold.
To camera right, at the frame edge, the dark wire runs straight up, no
thicker than a little finger. The upper quarter of the frame is bright
indigo sky.

CAMERA & LIGHT: a medium shot on a 35mm spherical lens from a fixed
position four metres in front of her at eye level, head-on, f/4. No sun
disc in frame. Cool indirect blue-grey light from above falls into the
visor and lights her face from the front — her eyes are the brightest
readable detail in the frame. Shadow edges are soft and weak — correct
for this thin air, not a rendering fault; the frame still holds high
contrast. A low rim light separates her shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no reflected figure, no face reflected in the
pane. 0% bloom, no glow filter, no soft focus. Photorealistic skin with
pores, sweat and fatigue retained — no airbrushing, identical bone
structure. The visor pane is clear glass with zero tint, zero mirror
coating and zero reflection of the environment; her face is fully
readable through it at this head angle. No back-mounted unit, no
backpack, no tank, no hose, no cable. The wire is perfectly straight — no
sag, no curve, no sway. No readable text, letters, digits, numbers or
symbols anywhere in the frame; no scale marks, no graduation ticks. No flag,
no logo, no patch. No subtitles, no title card, no watermark. No
suspended dust, no haze. Rock static and solid — no melting, no warping.
No tilt-shift look, no miniature read. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 11 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with a faded bone-white shoulder band and a thin pale scratch on
the left forearm sleeve, hard white helmet with one flat clear front
pane in a visible dark rim, her face fully readable and both eyes open,
the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The coil as wide as
her helmet stays in her LEFT glove at the bottom edge. Arm fronts and
elbows carry pale gold dust.

SCENE (as in the start frame): the woman head-on from the chest up, head
tilted back, the wall behind her, the wire at the right frame edge, the
bright sky in the upper quarter.

CAMERA: 35mm lens, fixed four metres in front of her at eye level,
head-on. Medium shot.

TIMELINE: 0.0s — She is already looking up, and holds; her eyes track
slowly upward across the frame, following something above and beyond it,
and her chest rises once. 3.5s — Her jaw sets and her brows draw
together for about a second, then release. 6.0s — Her eyes come down a
little, level, and fix straight ahead past camera; her shoulders square.
8.5s — Her right glove closes into a fist at her side, slowly, the
ribbed segments tightening over the knuckles, and stays closed. 10.0s —
Hold; her face stays readable and lit the whole shot.

TARGET AND DIRECTION: her target is above and beyond the camera,
straight up the same vertical line the wire holds. Her shoulders stay
square to the wall. The lit band is above and behind her — the light
rims the top of her helmet and her shoulders from behind. She never
turns toward the light, there is no direction reversal, and she never
faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight — it does not sag, it does not
curve, it does not sway, it does not swing.

AUDIO: a thin, toneless air sound; two close, slow helmet breaths; the
faint creak of a glove closing. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no push in. Exactly one human — no second person, no clone, no
reflected figure, no face reflected in the pane. 0% bloom, no glow
filter, no soft focus. Suit, helmet and coil identical throughout;
nothing appears or disappears mid-shot; the visor stays clear and
unmirrored and her face stays readable at every head angle; the back
stays flat with no backpack, tank, hose or cable. The coil never leaves
her left glove. The wire never sags, curves or sways. No suspended dust.
No readable text, letters or digits anywhere in the frame; no scale marks,
no ticks; no flag, no logo; no subtitles, no watermark. Rock static —
no melting, no warping. No face morphing, identical bone structure
throughout. No tilt-shift or miniature look. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 11 (S11) — ÜST TERASLAR ⭐ TEMA İNDEKSİ: YANDAN SICAK SIZINTI

> **TEMA (UMUT) · 3. derece indeks [TEMA §5]:** soğuk karanlık kadraja
> YANDAN ince sıcak sızıntı. İlk doğrudan güneş karşı duvarın tepesinde
> tek altın şerittir; kadın hâlâ gölgededir.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 12 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: low on a cut step high on the north wall, near the upper
terraces. The woman of thirty-eight climbs away from camera and slightly
across it, seen full length from just above the rock: matte dark
slate-blue surface suit, faded bone-white bands at shoulders and shins,
a thin pale scratch on the left forearm sleeve, hard white helmet with a
single flat front pane inside a visible dark rim — not a bubble — the
pane optically clear with zero tint and zero mirror coating, her face
readable in three-quarter view. Her back is one continuous smooth panel
from collar to hip, carrying nothing. Her LEFT glove holds a hand-turned coil of wire as wide as her helmet; her right glove is on the rock.
Boots, knees, arm fronts and elbows carry pale gold dust. The dark
blue-grey basalt fills the lower right; the loose dust in its lees is
pale gold. At the left edge the dark wire runs straight up, no thicker
than a little finger. Across the upper left third, beyond the gap, the
top edge of the far wall carries one narrow band of warm direct
sunlight — the first in the film — and it does not reach her; she and
the rock around her are still in cool blue-grey shadow.

CAMERA & LIGHT: a wide shot on a 32mm spherical lens from a fixed
position on the step two and a half metres from her boots, just above
the rock, angled slightly up, f/5.6, deep focus. No sun disc in frame.
Cool indirect blue-grey light on the figure; one warm band on the far
rock in the upper left. Shadow edges are soft and weak — correct for
this thin air, not a rendering fault; the frame still holds high
contrast. A low rim light separates her shoulders and helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure above or below, no reflected figure.
0% bloom, no glow filter, no soft focus, no lens flare, no anamorphic
streak, no light bleeding off the warm band onto neighbouring rock.
Photorealistic skin with pores — no airbrushing. The visor pane is clear
with zero tint, zero mirror coating and zero reflection; no back-mounted
unit, no backpack, no tank, no hose, no cable — the back of the suit is
one continuous smooth panel. The wire is perfectly straight — no sag, no
curve, no sway. The warm light stays on the far wall only and does not
touch the figure. No readable text, letters, digits, numbers or symbols
anywhere in the frame; no scale marks, no graduation ticks, no route marks.
No flag, no logo, no patch. No subtitles, no title card, no watermark.
No suspended dust, no haze, no god rays, no visible light shafts. Rock
static and solid — no melting, no warping. No tilt-shift look, no
miniature read. No Unreal Engine look, no CGI aesthetic. Photorealistic,
35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 12 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, matte dark slate-blue surface suit with faded
bone-white bands and a thin pale scratch on the left forearm sleeve,
hard white helmet with one flat clear front pane in a visible dark rim,
her face readable, her back one continuous smooth panel carrying
nothing. The coil as wide as her helmet stays in her LEFT glove. Boots,
knees, arm fronts and elbows carry pale gold dust. The warm band on the
far wall's top edge stays exactly where it is for the whole shot.

SCENE (as in the start frame): the woman climbing away from camera on
the upper terraces, the wire at the left edge, the single warm band on
the far rock in the upper left.

CAMERA: 32mm lens, fixed on the step two and a half metres from her
boots, just above the rock, angled slightly up. Wide shot.

TIMELINE: 0.0s — She is already climbing at a steady pace, right glove
to handhold, left glove swinging the coil clear of the rock. 4.0s — She
gains two steps; her helmet turns once toward the warm band on the far
wall and comes back. 7.0s — She keeps climbing without pausing; her
shoulders stay square to the rock. 10.0s — Hold; she is still climbing
and still fully inside the cool shadow.

TARGET AND DIRECTION: her target is the bright notch of sky at the top
of this wall, straight up the same vertical line the wire holds. Her
shoulders stay square to the wall. The lit band is above and behind her
— the light rims the top of her helmet and her shoulders from behind.
She never turns toward the light, there is no direction reversal, she never walks toward the warm band on the far wall at screen left, and
she never faces back down the canyon.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion. The thin air exerts no force: her suit never stirs, nothing
lifts or blows. The wire is perfectly straight — it does not sag, it does not
curve, it does not sway, it does not swing.

AUDIO: a thin, toneless air sound, quieter than before; steady boot
grit; three working helmet breaths. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom. Exactly one human — no second person, none above or below, no
clone, no reflected figure. 0% bloom, no glow filter, no lens flare, no
anamorphic streak, no glow spill from the warm band. The warm band stays
on the far wall and never moves, never widens, never reaches the figure
during this shot. Suit, helmet and coil identical throughout; nothing
appears or disappears mid-shot; the visor stays clear and unmirrored;
the back stays one smooth panel with no backpack, tank, hose or cable.
The coil never leaves her left glove. The wire never sags, curves or
sways. No suspended dust, no god rays, no visible light shafts. No
readable text, letters or digits anywhere in the frame; no scale marks, no
ticks; no flag, no logo; no subtitles, no watermark. Rock static — no
melting, no warping. No tilt-shift or miniature look. No voice, no
music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 12 (S12) — ⭐VİRAL #2 · ORTA NOKTA: AĞIZDA TAM GÜNEŞ

> **ORTA NOKTA — SAHTE ZAFER.** Tırmanış bitti; masif henüz görünmedi.
> ⭐ **İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [D179]:** başlangıç karesinde yüz
> HÂLÂ GÖLGEDE; ışığa girme video promptunun içinde olur.
>
> **⭐VİRAL #2 · YÜZ:** panelin ardındaki yüz iki saniyede karanlıktan tam
> okunurluğa geçer; gözler kısılır, sonra açılır.
> **HAREKET:** gövde ağzın kenarından yukarı çıkarken arkasındaki yarık
> kadraja girer; kadrajın alt yarısı iki saniyede doluluktan boşluğa döner.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 13 of
25. Exactly one human figure — this film has exactly one human total.

SCENE: at the very lip of the canyon's north rim. The woman of
thirty-eight rises into frame from below, facing camera, framed from the
chest up, her boots still on the last cut steps out of sight: matte dark
slate-blue surface suit, faded bone-white band at the shoulders, a thin
pale scratch on the left forearm sleeve, hard white helmet with a single
flat front pane inside a visible dark rim — not a bubble — the pane
optically clear with zero tint and zero mirror coating, her whole face
readable through it. Her back silhouette is flat with no back-mounted
unit. Her LEFT glove holds a hand-turned coil of wire as wide as her
helmet, just inside the bottom edge; her right glove grips the rim rock.
Boots, knees, arm fronts, elbows and the lower half of her chest carry
pale gold dust. She is STILL IN SHADOW: the rim's edge cuts a soft line
across the frame just above her helmet, and the sunlight beyond it lies
on the open ground behind her, not on her. Behind and beyond, the far
side of the rim runs flat to a horizon of deep indigo sky with a pale
gold band low above it. To camera right, at the frame edge, the dark
wire runs straight up, no thicker than a little finger. The rock is dark
blue-grey basalt; the loose dust caught in its lees is pale gold.

CAMERA & LIGHT: a medium shot on a 35mm spherical lens from a fixed
position four metres in front of her at eye level, head-on, f/4. No sun
disc in frame. Direct sunlight lies on the open ground behind her; her
face and chest are still in the rim's cool shadow. Shadow edges are soft
and weak — correct for this thin air, not a rendering fault; the frame
still holds high contrast. A low rim light separates her shoulders and
helmet from the background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no clone, no figure on the rim behind her, no reflected
figure, no face reflected in the pane. 0% bloom, no glow filter, no soft
focus, no lens flare, no anamorphic streak. Photorealistic skin with
pores, sweat and fatigue retained — no airbrushing, identical bone
structure. The visor pane is clear with zero tint, zero mirror coating
and zero reflection; no back-mounted unit, no backpack, no tank, no
hose, no cable. Her face and chest are still in shadow in this frame —
the sunlight has not reached her. The wire is perfectly straight — no sag,
no curve, no sway. No readable text, letters, digits, numbers or symbols
anywhere in the frame; no scale marks, no graduation ticks. No flag, no
logo, no patch. No subtitles, no title card, no watermark. No suspended
dust, no haze, no god rays. Rock static and solid — no melting, no
warping. No tilt-shift look, no miniature read. No Unreal Engine look,
no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 13 of 25.
Fixed locked-off camera. Exactly one human figure — this film has
exactly one human total.

START FRAME: the approved still from this scene's IMAGE prompt —
animate it. CONTINUITY LOCKS carried from the frame: exactly one human,
a woman of thirty-eight, warm brown skin, matte dark slate-blue surface
suit with a faded bone-white shoulder band and a thin pale scratch on
the left forearm sleeve, hard white helmet with one flat clear front
pane in a visible dark rim, her face fully readable, the back of the suit one continuous smooth panel from collar to hip, carrying nothing. The coil as wide as her helmet stays in
her LEFT glove. Boots, knees, arm fronts, elbows and the lower chest
carry pale gold dust.

SCENE (as in the start frame): the woman rising into frame at the
canyon's rim, still in the rim's shadow, the sunlit open ground behind
her, the wire at the right frame edge.

CAMERA: 35mm lens, fixed four metres in front of her at eye level,
head-on. Medium shot.

TIMELINE: 0.0s — She is already rising: her right glove pushes down on
the rim rock and her shoulders come up past the shadow line. 2.0s — Her
helmet clears the shadow line and full direct sunlight reaches her face
for the first time; her eyes narrow for about a second, then open. Her
face stays readable through the clear pane the whole time. 5.0s — She
brings her left boot up onto the rim and stands, her whole body now in
sunlight; behind her, over her shoulders, the canyon gap opens and the
lower half of the frame goes from rock to empty air. 8.0s — She stands
still, chest rising twice, her helmet turned slightly up and past
camera. 10.0s — Hold.

PHYSICS: 0.42 g — ordinary deliberate movement in real time, no slow
motion, no bounding, no floating. The thin air exerts no force: her suit
never stirs, nothing lifts or blows. The wire is perfectly straight — it does
not sag, it does not curve, it does not sway, it does not swing.

AUDIO: the thin air sound drops away almost to nothing as she clears the
rim; three close helmet breaths; one boot on flat rock. No voice, no
music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans,
no zoom, no crane, no angle change. Exactly one human — no second
person, none on the rim, no clone, no reflected figure, no face
reflected in the pane. 0% bloom, no glow filter, no lens flare, no
anamorphic streak, no white-out as the light reaches her face — the exposure holds and her face stays fully readable. Suit, helmet and coil identical
throughout; nothing appears or disappears mid-shot; the visor stays
clear and unmirrored; the back stays flat with no backpack, tank, hose
or cable. The coil never leaves her left glove. The wire never sags,
curves or sways. No suspended dust, no dust kicked into a cloud, no god
rays. No readable text, letters or digits anywhere in the frame; no scale
marks, no ticks; no flag, no logo; no subtitles, no watermark. Terrain
static — no melting, no warping. No face morphing, identical bone
structure throughout. No tilt-shift or miniature look. No voice, no
music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

# ✅ BÖLÜM 1 KONTROL

```
□ 13 sahne bloğu · "Scene N of 25" doğru  (S0 = Scene 1 … S12 = Scene 13)
□ 13 IMAGE + 13 VIDEO prompt · hepsi self-contained (kural ③) — hiçbirinde
  "BIBLE'a bak" atfı yok
□ Kurulum: A · C · D · E · F = 5  ✅ ACI_YAYI §4 bandı içinde
□ Ardışık çiftlerin tamamı ≥1 ölçek kademesi + ≥45°; bu dosyada bilinçli
  şok YOK (ŞOK #1 dosya sınırında: S12→S13, BÖLÜM 2'nin başında)
□ İnsan sayısı: 13/13 sahnede tam 1
□ Kask: 13/13 kapalı · panel berrak, aynasız, tonsuz
□ Sırt: her promptta düz; S5 · S7 · S11'de POZİTİF yüzey cümlesi [D139]
□ Metin yasağı KAPSAMLI: giysi + eldiven + plaka + baraka + kaya + tel + gök
□ Ölçü prompt gövdesinde YOK; yalnız kamera mesafesi [D138 muafiyeti]
□ Zorlanma eldivenin üstünde, deride değil [D175]
□ "swirl" kelimesi: 0 · asılı toz: 0 · toz perdesi: 0
□ Yumuşak gölge MEŞRU cümlesi: 13/13
□ Yüzey rengi tek cümlede, yalnız SCENE bloğunda [D176]
□ İmaj promptları 0,0 saniyeyi yazıyor — S3 · S9 · S12'de açıkça [D179]
□ Novum cümlesi ("perfectly straight … does not sag") 13/13 promptta
□ Üretim kapıları: S3 · S9 — geçmeden BÖLÜM 2 üretilmez
```

## 🚪 KAPI KAYITLARI (üretim koştukça doldurulur)

| Tarih | Sahne | Koşu | Sonuç | Not |
|---|:--:|:--:|:--:|---|
| ⬜ | S3 | — | ⬜ | üretim kapısı: tel sarkmıyor mu, uç yükseliyor mu |
| ⬜ | S9 | — | ⬜ | üretim kapısı: parça göz hizasından yükselerek geçiyor mu |
| ⬜ | S0 | — | ⬜ | hook, 3 varyant |
