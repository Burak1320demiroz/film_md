# 🔦 THE KEPT LIGHT — Tutulan Işık | BÖLÜM 1

## AI Production Bible — Self-Contained Prompts
### BÖLÜM 1: Sahne 0-12 (13 sahne) | 16:9 Yatay | Görsel + Video
### _"Burada hiçbir şey geçmişe geçmez; bıraktığın her şey bugünde kalır ve birikir."_

> **BÖLÜM 1 süresi:** Hook (9 s) + 12 sahne × 10 s = 129 saniye (0:00 – 2:09)
> **Toplam film:** 25 sahne = 249 saniye = 4:09
> **BÖLÜM 2:** `THE_KEPT_LIGHT_BOLUM_2.md` (S13-S24)
> **Plan:** `THE_KEPT_LIGHT_PLAN.md` — sayısal kilitler, ışık takvimi,
> risk kartları, açı yayı, B5 ve politika satırı orada.
> **Replik:** 0 — film konuşma bakımından tamamen sessiz (insan 0 · makine 0 · telsiz 0).

KURULUM İSKELETİ: A E D C C D C B C D F D C D C B C C B C E E D C A

> ⚠️ **Yukarıdaki satır FİLMİN TAMAMINI kapsar (25 harf) ve bilerek bu
> dosyadadır.** `prompt_kontrol.py` klasör modunda iki bölüm dosyasını
> birleştirir ve iskeleti BİRLEŞİK metinde arar; satır yalnız PLAN'da
> kalırsa klasör modu onu bulamaz ve küme/dönüş kapıları HİÇ KOŞMAZ.
> ⛔ **BİLİNEN YANLIŞ POZİTİF:** dosya modunda aynı kapı 25 harfi bu
> dosyanın 13 promptuyla karşılaştırır ve FIX verir. Bölünmüş filmde bu
> kaçınılmazdır ve GEÇERLİ KOŞU KLASÖR MODUDUR — çıktıda
> `📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik` satırı aranır.

---

## ⚠️ BÖLÜM 1 ÜRETİM NOTLARI (promptlardan önce oku)

```
① AĞZIN ALTINDA DÜŞME BİTMEZ — FİLMİN NOVUMU VE ÜRETİM KAPISI [plan 🧬]
   Modelin refleksi ya düşen bir cismi kadrajdan çıkarmak ya da onu
   HAVADA DONDURMAKTIR. İkisi de yanlış. Çözüm POZİTİF cümle, her
   ilgili promptta birebir:
   "Everything below the lip of the hatch keeps moving downward for the
    whole shot — always the same direction, never rising, never stopping,
    never held in place — but each thing moves less the deeper it already
    is: the clamp sinks about one body-length in the first second, then
    only a hand's width across the next three seconds, then less."
   ⭐ S0 BU CÜMLENİN ÜRETİM KAPISIDIR. S0 temiz çıkmadan S1, S20 ve
     BÖLÜM 2 üretilmez [D73: novum render edilmezse film yoktur].
   ⛔ "hovering" · "frozen" · "suspended" · "floating" kelimeleri bu
     dosyanın POZİTİF gövdesinde 0 kez geçer; yalnız NEGATIVE bloğunda.

② İHLAL YANINDAKİ NORMALLE KANITLANIR [ONERME §3]
   Aynı karede AĞZIN ÜSTÜNDE olan her şey normal davranır ve bu her
   yatak promptunda yazılır:
   "Above the deck the gravity is ordinary: anything let go from his
    glove drops about one body-length in the first second and strikes
    the deck."

③ VAKUM — ÜSSÜN İÇİ DE VAKUMDUR [kart §3.1 · D30 · D39]
   Toz 0 kare. Asılı toz, toz perdesi, toz şelalesi, ışık sütunu tozu:
   0 kare. Gölgeler MUTLAK SİYAH ve jilet kenarlı. Dolgu ışığı YOK.
   ⚠️ Metal bir hacimde model ikincil yansıma üretmeye çok yatkındır —
   pozitif cümle her yatak promptunda:
   "The metal walls of the bay throw no second light; the shadows inside
    the bay are absolutely black with razor edges."

④ YÜZEY RENGİ TEK CÜMLEDE, TEK BLOKTA [⛔ D176]
   "The deeper a thing hangs below the lip, the less of the old lamp's
    light reaches it: the near ones read as pale steel, the deep ones as
    faint amber, the deepest as points only."
   — yalnız SCENE bloğunda. LIGHT bloğu hiçbir yüzeye renk atamaz;
   kontrast garantisi ÖZNEYİ tarif eder:
   "A low rim light separates his shoulders and helmet from whatever is
    behind him; his silhouette never merges with the background."

⑤ YÖN BİR NESNEYE BAĞLIDIR [⛔ D174]
   "Yukarı" ve "aşağı" bu filmde koordinat DEĞİL, adlandırılmış
   nesnelerdir ve her prompt onları adıyla yazar:
   "Up is the rock ceiling above the base; down is the black disc below
    it. Everything that is released moves toward the black disc — toward
    the same side of the frame the open hatch is on — and never toward
    the rock."

⑥ ÖLÇÜ PROMPT GÖVDESİNE GİRMEZ [D138 · D45]
   Metre, santimetre, derece, f-sayısı, çentik, skala: 0.
   Oranlar GÖVDE BOYUYLA yazılır ("a clamp the length of his hand").
   ✅ Kamera MESAFESİ muaftır ("fixed 2.0 m from him").

⑦ ZORLANMA ELDİVENİN ÜSTÜNDE OKUNUR [⛔ D175]
   ✗ "the forearm tendons stand out through the glove"
   ✅ "his grip tightens and the glove's segments lift over the knuckles"
   Yıpranma kilidi GİYSİ YÜZEYİNE yazılır:
   ✅ "a thin pale scratch along the left forearm sleeve of the suit"
   ⛔ ÇIPLAK DERİ NEGATİFİ ÜÇ BÖLGELİDİR ve tek bölgeli yazılamaz:
   "No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff."

⑧ KİR MERDİVENİ — TARİF İNER, ETİKET İNMEZ [D147 · ⛔ D155]
   S0-S12: yalnız eldivenlerin avuç içleri ve dizler mat.
   Klip İÇİNDE sabit, sahneler ARASI monotonik, hiç azalmaz.
   ⛔ "Wear state: PHASE n" hiçbir prompta yazılmaz.

⑨ İMAJ PROMPTU 0,0 SANİYEYİ YAZAR [⛔ D179]
   I2V'de imaj t = 0'dır. Değişim taşıyan her sahnede (S3 · S4 · S6 ·
   S8 · S12) imaj promptu video promptunun `0.0s —` satırıyla KELİME
   KELİME uyumludur ve sahnenin SONUCUNU asla yazmaz.

⑩ TEK KLİBE DURUM DEĞİŞİMİ YAZILMAZ [KILAVUZ_REHBERI §7 · SAHNE_ZINCIRI §1]
   Bu bölümde tek klipte değişen tek şey KONUMDUR (bir cismin yeri).
   Işık kademesi, kir, kelepçe sayısı sahne SINIRINDA değişir.

⑪ KELEPÇE SAYACI — HER "D" KURULUMUNDA SAYILABİLİR [D78 · KART 5]
   S2: 5 · S5: 4 · S9: 2 · S11: 2 · (BÖLÜM 2: S13: 1 · S22: 0)
   ⛔ Sayı hiçbir prompta RAKAMLA yazılmaz; kadrajda SAYILABİLİR olur.
   Yazım biçimi: "five clamps still hold the module" — İngilizce sayı
   sözcüğü kadraj içeriğidir, ekran metni değildir.

⑫ KURULUM SAYISI — BÖLÜM 1'de 6 (A · B · C · D · E · F) ✅ bant içi.
   ⭐ DÖNÜŞ ve KÜME satırları: dönen her sahne kamera metnini BİREBİR
   kopyalar ve sonuna işaret satırını ekler [ACI_YAYI §7 ⑥].

⑬ NOVUM TAŞIYICISI: KELEPÇE × eldivenli avucun kapak ağzında açılması
   → kelepçe iner ama inişi bitmez. TEK KARE testinin nesnesi de
   KELEPÇEDİR — aynı nesne [D157]. S0 ve S1'de kadrajda BAŞKA hiçbir
   şey hareket etmez [D157③].

⑭ UZUNLUK — BİLİNÇLİ SAPMA, KAYITLI [D74 · TUR 11 §5 ① aritmetiği]
   Video promptları 2.000-2.600 hedef bandının üstünde, ~4.300 TAVANIN
   altındadır. Aritmetik depoda ölçüldü:
     §5 negatif çekirdek        1.650 kr
     D79 kask/vizör bloğu        +320
     ────────────────────────────────
     kasklı sahne KALIBI         1.970 kr
   Üstüne bu filmde ZORUNLU olarak binenler:
     · novum cümlesi (iniş bitmez)             ~330 kr
     · normal fizik karşı-cümlesi              ~150 kr
     · yön çapası (kaya ↔ kara disk)           ~230 kr
     · ikincil yansıma pozitifi                ~140 kr
     · üç bölgeli çıplak-deri negatifi         ~150 kr
     · D138 KAPSAMLI metin yasağı              ~260 kr
   ⛔ TAVAN AŞILMADI — ÖLÇÜLDÜ (prompt_kontrol, 06.09.2026):
     image 2.453-3.553 kr · video 2.878-4.211 kr · tavan 4.300.
     En uzun video promptu S24 (4.211) ve S12 (4.087); ikisi de tavanın
     altında ve marj bilerek bırakıldı.
   ⛔ Kısaltmanın tek yolu bir KİLİDİ atmaktır ve her kilit bir dersin
   faturasıdır. Bu dosyada zaten şu üç kısaltma YAPILDI ve kilit
   kaybettirmedi: normal-fizik karşı cümlesi tek cümleye indi ·
   "no tilt-shift / miniature" kilidi yalnız S10'da (tek büyük yapı
   kadrajı) bırakıldı · kesim POZİTİF tarif edildi, yasak listesi
   yalnız NEGATIVE bloğunda kaldı [D59 · D123].
   ⚠️ Üretimde arka arkaya iki red gelirse önce PROB koşulur, prompt
     KISALTILMAZ — Third Dune'da beş red vardı ve en kısası da battı.
```

---

# 📖 BİBLE'LAR

---

## 🌍 WORLD BIBLE — ASILI ÜS

```
YER: bir kara deliğin üstünde sabit tutulan bir kayanın ALT yüzü.
Kayanın uzak yüzündeki motorlar onu orada tutar; o motorlar hiçbir karede
kadrajda DEĞİLDİR — alev, egzoz, kıvılcım, duman 0 kare.
Statik gövde tam yerel ağırlığı hisseder: 0,40 g.

YUKARISI = KAYA: çukurlarla dolu, mat, koyu bir taş tavan.
AŞAĞISI = KARA DİSK: mutlak siyah, kenarsız bir düzlem; tek işareti
kenarındaki saç inceliğinde tek beyaz çizgi — halka değil, hâle değil,
parlama değil.

ÜS: kayanın altına cıvatalanmış kutu biçimli tek gövde, üç buçuk gövde boyu
genişliğinde. İçinde tek bir çalışma hacmi (YATAK) var ve o hacim de
vakumdur. Yatağın zemininde kare bir AĞIZ açıktır — bir gövde boyu
kenarında, film boyunca AÇIK. Ağzın çerçevesinde ALTI kelepçe yuvası var.
Kutunun dışında, ağzın çevresinde tek bir korkuluk dönüyor.

MODÜL: ağzın altında, kelepçelerle çerçeveye asılı ölü bir silindir.
Bekçiden biraz uzun, kalçasının iki katı kalınlığında. Mat, koyu, çıplak.

ASILI ALAN: ağzın altında, birbirinin altında duran nesneler. Yakındakiler
küçük ve yeni, derindekiler daha büyük ve daha sönük, en derindekiler
yalnız birer nokta. Hepsi aynı yönde ve çok yavaş inmeye devam eder.

ESKİ LAMBA: alanın içinde, ağızdan yaklaşık on gövde boyu aşağıda duran,
başlıklı, yumruk büyüklüğünde eski bir el lambası; konisi AŞAĞI bakar.
Alanın görülebilmesinin TEK sebebi odur. Hattı yukarı, ağzın
çerçevesindeki ALTINCI kelepçenin pimine bağlıdır.

⛔ 0 ekran · 0 kadran · 0 gösterge · 0 tuş takımı. Bilgi taşıyan tek şeyler:
  kalan kelepçe SAYISI · modülün YATMA açısı · ağzın altındaki parlak
  nesnelerin SAYISI.
```

## 👤 CHARACTER BIBLE — bekçi (promptlarda İSİMSİZ [D34])

```
Erkek, elli dört. Geniş omuzlu, koyu kahverengi ten.
(⛔ Tek pencerede en çok ÜÇ kişi özniteliği — yaş · yapı · ten [D167].)

GİYSİ: mat KOYU ZEYTİN yüzey giysisi; omuzlarda ve inciklerde solmuş kum
beyazı bantlar. Sol ön kol MANŞETİNDE ince soluk bir çizik (yıpranma
kilidi GİYSİ yüzeyinde, gövdede DEĞİL [D175]).

KASK: sert kum beyazı kabuk, ÖNDE TEK DÜZ PANEL, görünür koyu bir
çerçevenin içinde. ⛔ Kubbe değil, kavis değil, dikişsiz değil [D146].
Panel optik olarak berrak: sıfır ton, sıfır ayna kaplaması, sıfır çevre
yansıması. Yüzü her karede ve her baş açısında tam okunur [D79].
25/25 sahnede KAPALI.

SIRT: DÜZ. Sırta monte ünite yok, sırt çantası yok, tank yok, hortum yok,
kablo yok. Pozitif hâli her prompta iner: yakadan kalçaya kesintisiz tek
düz panel, üstünde hiçbir şey taşımıyor [D139].

ELDİVENLER: ağır, dilimli, koyu; bilekte giysiyle TEK PARÇA. Zorlanma
ELDİVENİN üstünde okunur: dilimler boğumların üstünde gerilir ve kalkar.

TAŞIDIĞI İKİ ŞEY:
  ① kesici — kısa, iki çeneli, tek elle çalışan bir el aleti; SAĞ elinde
    ya da kalçasının solundaki yuvada.
  ② KENDİ EL LAMBASI — yumruğu kadar, başlıklı, SÖNÜK, kalçasının
    SAĞINDAKİ klipste. Bu bölümde hiç kullanılmaz ve hiç yanmaz.

KİR: bu bölümde yalnız eldivenlerin avuç içleri ve dizler mat. Klip içinde
sabit, sahneler arası monotonik, hiç azalmaz.

DUYGU REGİSTERİ: yetkin, yorgun, telaşsız. Panik kare sayısı = 0.
"o çalışıyor, dayanmıyor."
```

## 🚫 NEGATİF ÇEKİRDEK — her prompta iner (vakum · asılı üs)

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly one human character — no duplicates, no clones, no second
person, no crew, no figure in the bay behind him, no reflected or doubled
figure. 0% bloom, no glow filter, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin with pores, sweat and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure throughout. Equipment and
clothing identical to the description — no drift, no gear appearing or
disappearing mid-shot; the helmet stays sealed and the front pane stays
clear. The pane is optically clear glass with zero tint, zero mirror
coating and zero reflection of the environment. No back-mounted unit, no
backpack, no tank, no hose, no cable, no rear housing of any kind. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. Dirt and
wear staining stays fixed and never shifts. No readable text, letters,
digits, numbers or symbols anywhere in the frame — not on the suit, not on
the tool, not on the clamps, not on the hatch frame, not on the module, not
on the rock and not on the black disc. Nothing in this world has been
measured, labelled, marked out or annotated by anyone: no scale marks, no
graduation ticks, no survey markers, no engraved or painted characters of
any kind. No national flag, no agency logo, no mission patch, no
manufacturer marking. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. All
hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers, rigid-body collision throughout. There is no
dust and no loose grit in this vacuum: no suspended dust, no dust curtain,
no haze bank, no drifting motes; any loose particle would obey 0.40 g with
continuous physical momentum — never hovering, never frozen, never swirling
or flowing like liquid. No air, no wind, no smoke, no exhaust, no flame, no
spark, no rust. Structures static and stable — no melting metal, no warping
topology, no swimming texture. No lens flare, no anamorphic streak. No
tilt-shift look, no miniature or toy-model read. No Unreal Engine look, no
CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film
grain. No voice, no music.
```

---

# 🎬 SAHNELER

---

## 🎬 SAHNE 0 (S0) — AVUÇ VE AĞIZ ⭐ HOOK · ⭐ KAPAK ANI (0:04) · KURULUM A

> Kapı sahnesi [HOOK §7]: üç hook varyantı üretilir, en iyisi seçilir.
> Üretim 10 s, kurguda baştan 1,0 s kırpılarak 9,0 s'ye iner.
> ⭐ **NOVUM ÜRETİM KAPISI**: bu sahne temiz çıkmadan başka sahne üretilmez.
> ⛔ Kadrajda kelepçeden başka hiçbir şey hareket etmez [D157③].
> **S0 ÇIKIŞ SORUSU (plana yazılır, ekrana değil):** *"Bu parça neden
> gitmiyor — ve altındaki o kadar şey oraya nasıl birikti?"*

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 1 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: an open square hatch in the floor of a small vacuum work bay,
photographed from directly above it. Filling the upper-left third of the
frame is a heavy segmented glove, palm down and already open, its fingers
spread; the glove runs into the sleeve as one piece at the wrist. Sitting
below the open glove, on the lower-right third line, is a matte grey clamp
the length of a hand, freshly cut, hanging in the black of the hatch mouth
about a hand's width under the fingers. Below the clamp, going away into
the dark, is a line of smaller and dimmer shapes, one under the other,
getting fainter with depth. The deeper a thing hangs below the lip, the
less of the old lamp's light reaches it: the near ones read as pale steel,
the deep ones as faint amber, the deepest as points only. Along the right
edge of the frame is the top of his hip: a hooded hand-lamp the size of his
fist rides dark and unlit in a clip there. He is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders; the helmet is a hard sand-white
shell with a single flat front pane set inside a visible dark rim — not a
bubble, not a dome — the pane optically clear with zero tint and zero
mirror coating, his face fully readable through it as he looks down past
his own glove. A thin pale scratch runs along the left forearm sleeve of
the suit. The back of the suit is one continuous smooth panel from collar
to hip, carrying nothing. Only the palms of his gloves and his knees are
dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 0.6 m above the lip of the
hatch, aimed straight down. Overhead top-down close-up, deep focus. Two
hooded work lamps in the bay ceiling light the glove and the lip from above
with cool neutral white; the metal walls of the bay throw no second light,
and the shadows inside the bay are absolutely black with razor edges. Below
the lip there is no bay light at all — only the weak fall of the old lamp
far down. A low rim light separates his shoulders and helmet from whatever
is behind him; his silhouette never merges with the background. The glove
holds the upper-left third, the clamp the lower-right third line, the black
of the hatch the lower half.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no airbrushing,
no waxy texture. The front pane is clear glass with zero tint, zero mirror
coating and zero reflection. No back-mounted unit, no backpack, no tank, no
hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp is a solid object with a hard edge, not a light, not a
reflection, not a spark. No readable text, letters, digits or symbols
anywhere in the frame — not on the suit, the tool, the clamp, the hatch
frame or the module; no scale marks, no graduation ticks; no flag, no logo,
no patch. No subtitles, no title card, no watermark. No dust, no suspended
grit, no haze. No smoke, no exhaust, no flame, no spark. No lens flare, no
anamorphic streak. Metal static and solid — no melting, no warping. No
tilt-shift or miniature look. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 1 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder bands, hard sand-white helmet with one
flat front pane in a visible dark rim, the pane optically clear and
reflection-free, his face readable, his back one continuous smooth panel
carrying nothing. A hooded hand-lamp the size of his fist stays dark in the
clip at his right hip for the whole shot. Only his glove palms and knees
are dulled with wear.

SCENE (as in the start frame): the open square hatch in the bay floor seen
from directly above; his open glove in the upper-left third; a matte grey
clamp the length of a hand hanging a hand's width under the fingers; below
it a line of smaller, dimmer shapes going away into the dark. The deeper a
thing hangs below the lip, the less of the old lamp's light reaches it: the
near ones read as pale steel, the deep ones as faint amber, the deepest as
points only.

CAMERA: 50mm spherical lens, fixed 0.6 m above the lip of the hatch, aimed
straight down. Overhead top-down close-up, deep focus.

TIMELINE: 0.0s — his glove is already open and the clamp is already free of
it, a hand's width below the spread fingers and moving down. 1.0s — the
clamp has gone about one body-length down into the dark and is visibly
slower. 4.0s — across these three seconds it moves only a hand's width
further, still downward, still the same direction. 7.0s — his fingers curl
back in and the glove withdraws to the edge of frame; the clamp keeps going
down, slower again. 10.0s — hold; the clamp is still moving down and
nothing else in the frame moves.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second.
Everything below the lip of the hatch keeps moving downward for the whole
shot — always the same direction, never rising, never stopping, never held
in place — but each thing moves less the deeper it already is: the clamp
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
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
tool and hip lamp identical throughout; nothing appears or disappears
mid-shot; the front pane stays clear and unmirrored; the back stays one
continuous smooth panel with no backpack, tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp never rises, never
stops, never hangs motionless, never drifts sideways, never spins away; it
is a solid object, not a light or a reflection. No dust, no suspended grit,
no haze, no drifting motes. No readable text, letters or digits anywhere in
frame, on the suit, tool, clamp, hatch frame, module, rock or black disc;
no scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
smoke, no exhaust, no flame, no spark, no rust. No lens flare, no anamorphic
streak. Metal static — no melting, no warping. No tilt-shift or miniature
look. No voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 1 (S1) — ALTIDA NE VAR ⚡ ŞOK#1 (3 kademe) · KURULUM E

> S1'in işi cevap vermek değil, açık döngüyü BÜYÜTMEKTİR [HOOK §3].
> İkinci bilgi = ÖLÇEK: kapağın altı bir kuyu değil bir ARŞİVDİR ve
> dibinde tek bir sıcak ışık vardır.
> ⛔ Kadrajda insan VARDIR (ağzın kenarında iki bot) — insansız sahne
> yazılmaz [KART 10].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 2 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: looking straight down through the open square hatch in the floor of
a small vacuum work bay. The four edges of the hatch frame the picture; at
the top edge of frame, standing on the deck beside the lip, are the boots
and knees of a man of fifty-four in a matte dark olive surface suit with
faded sand-white shin bands — only his legs are in this frame. Below the
lip the shaft is open black. Hanging in it, one under the other and getting
further apart with depth, are separate solid objects: nearest the lip a
matte grey clamp the length of a hand, then another, then a shorter bar,
then larger and vaguer shapes further down, then points. Far down, roughly
ten body-lengths below the lip, a small hooded lamp hangs with its cone
pointing down; it is the only reason any of this is visible. The deeper a
thing hangs below the lip, the less of the old lamp's light reaches it: the
near ones read as pale steel, the deep ones as faint amber, the deepest as
points only. A thin line runs down from the hatch frame to that lamp,
straight and slack-free.

CAMERA & LIGHT: 24mm spherical lens, fixed 0.4 m above the lip of the
hatch, aimed straight down. Overhead top-down extreme wide shot, deep
focus. No bay light reaches below the lip; the only light in the shaft is
the old lamp far down, and it falls off quickly upward. The lip itself
catches a hard cool edge from the bay lamps above. The shadows are
absolutely black with razor edges and the metal of the frame throws no
second light. The hatch frame holds the outer band of the picture, the
hanging objects the centre column, the small lamp the lower centre.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected figure, no one standing in the
shaft. 0% bloom, no glow filter, no soft focus, no glow halo around the
small lamp. The hanging objects are separate solid things with hard edges,
each one countable — not sparks, not embers, not particles, not a dust
column. No dust, no haze. No readable
text, letters, digits or symbols anywhere in the frame — not on the frame,
the clamps, the bar or the lamp; no scale marks, no graduation ticks; no
flag, no logo. No subtitles, no title card, no watermark. No smoke, no
exhaust, no flame, no spark. No lens flare, no anamorphic streak. Metal
static and solid — no melting, no warping.
No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 2 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, and in this
frame only his boots and knees are in shot at the top edge — matte dark
olive suit, faded sand-white shin bands. The hatch frame, the hanging
objects and the small hooded lamp far below stay exactly where they are.

SCENE (as in the start frame): the open shaft below the hatch; separate
solid objects hanging one under the other, getting further apart with
depth; a small hooded lamp far down with its cone pointing down; a thin
straight line running from the hatch frame down to it. The deeper a thing
hangs below the lip, the less of the old lamp's light reaches it: the near
ones read as pale steel, the deep ones as faint amber, the deepest as
points only.

CAMERA: 24mm spherical lens, fixed 0.4 m above the lip of the hatch, aimed
straight down. Overhead top-down extreme wide shot, deep focus.

TIMELINE: 0.0s — every hanging object is already moving down, each one
creeping, the nearest ones fastest. 3.0s — the nearest clamp has moved
about a finger's width further from the lip; the deeper shapes have barely
changed at all. 6.0s — one boot at the top edge shifts its weight on the
deck, a small dry movement, and settles. 10.0s — hold; everything below the
lip is still going down, in the same direction, at the same unhurried rates.

PHYSICS: 0.40 g. Everything below the lip of the hatch keeps moving
downward for the whole shot — always the same direction, never rising,
never stopping, never held in place — but each thing moves less the deeper
it already is: a clamp near the lip creeps a finger's width in ten seconds,
the deep shapes almost nothing. Up is the rock ceiling above the base; down
is the black disc below it. Everything released moves toward the black disc, which
fills the lower half of the frame, and never toward the rock. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; one dry scuff as the boot
shifts on the deck; three slow breaths inside the helmet. Nothing else — no
sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
one in the shaft. 0% bloom, no glow filter, no soft focus, no glow halo
around the small lamp. The hanging objects are separate solid things with
hard edges, each countable — not sparks, not embers, not particles, not a
dust column. They never rise, never stop, never hang motionless, never
swirl, never drift sideways. No dust, no suspended grit, no haze, no
drifting motes. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
smoke, no exhaust, no flame, no spark. No lens flare, no anamorphic streak.
Metal static — no melting, no warping. No
voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 2 (S2) — HALKA · KURULUM D

> Kurulum vuruşu: dünya + bekçinin yetkinliği. Kelepçe sayacı burada
> okunur: BEŞ kelepçe modülü tutuyor [D78 · KART 5].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 3 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of a small square vacuum work bay, seen from the far
wall. The bay is bare grey metal, a little over two body-lengths across;
its floor carries one open square hatch about one body-length on a side,
set slightly right of centre. Around the hatch frame sit six clamp seats,
and five matte grey clamps the length of a hand are still bolted through
them, holding a disused cylinder that hangs just below the opening — the
module is a little longer than he is tall and twice as thick as his hip,
matte, dark and unmarked. One seat is empty — not the one on the far arc. Standing on the near arc of
the ring, half turned toward the hatch, is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable through it. The back of
the suit is one continuous smooth panel from collar to hip, carrying
nothing. A short two-jawed cutter is in his right glove; a hooded hand-lamp
the size of his fist rides dark in a clip at his right hip. A thin pale
scratch runs along the left forearm sleeve of the suit. Only his glove
palms and knees are dulled with wear. Running down from one clamp on the
far arc of the ring, a thin line disappears through the opening.

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
boot cuff. Exactly five clamps hold the module and one seat is
empty — the count does not change. No screens, no dials, no gauges, no
keypads, no indicator lights anywhere in the bay. No readable text,
letters, digits or symbols anywhere in the frame — not on the suit, the
cutter, the clamps, the hatch frame or the module; no scale marks, no
graduation ticks; no flag, no logo, no patch. No subtitles, no title card,
no watermark. No dust, no haze. No smoke, no exhaust, no
flame, no spark, no rust. No lens flare, no anamorphic streak. Metal static
and solid — no melting, no warping. No
Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 3 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. A short two-jawed cutter stays in his right glove;
a hooded hand-lamp stays dark in the clip at his right hip. Five clamps
hold the module and one seat is empty for the whole shot; the empty one is
not the seat on the far arc. Only his
glove palms and knees are dulled with wear.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch in its floor, the ring of six clamp seats, the disused module hanging
just below the opening, and a thin line running down through the opening
from one clamp on the far arc.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus.

TIMELINE: 0.0s — he is already walking the near arc of the ring, one
unhurried step, the cutter low in his right glove. 3.0s — he reaches the
second clamp seat, plants his boots and lowers into a crouch beside it, his
helmet turning down toward the clamp. 6.0s — his left glove settles flat on
the hatch frame beside the clamp and takes his weight. 10.0s — hold; he
stays down, still, looking at the clamp.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. Up is
the rock ceiling above the base; down is the black disc below it; the open
hatch faces the black disc. This is a vacuum: no air, no dust, no wind, and
his suit never stirs.

AUDIO: the narrow steady bed of the suit fan; two dry boot contacts
transmitted through the deck, short and toneless; the flat knock of the
glove landing on the frame; slow breathing inside the helmet. Nothing else
— no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; nothing appears or
disappears mid-shot; the front pane stays clear and unmirrored; the back
stays one continuous smooth panel with no backpack, tank, hose or cable. No
bare skin anywhere: none above the collar seal, none at the wrist between
glove and sleeve, none at the ankle above the boot cuff. The clamp count
stays five and the empty seat stays empty. No screens, no dials, no gauges,
no keypads, no indicator lights. No readable text, letters or digits
anywhere in frame; no scale marks, no ticks; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no anamorphic streak.
Metal static — no melting, no warping. No
voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 3 (S3) — İKİNCİ KELEPÇE 🕰️ KÜME#1 (1/2) · KURULUM C
### ⭐ TOHUM 0:31 · ⭐ KATALİZÖR 0:34

> **TOHUM [FINAL §3]:** 0:31'de, kadrajın arka bandında, halkanın uzak
> yayındaki kelepçeden aşağı inen ince hat 2 saniye görünür. ⛔ Bekçi ona
> BAKMAZ; vurgu = cevap.
> **KATALİZÖR:** 0:34'te ikinci kelepçe ayrılır ve modül ilk kez bir karış
> iner — geri alınamaz.
> ⛔ Bu klip bir KÜMENİN birinci yarısıdır; S4 aynı kurulumda devam eder.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 4 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the edge of an open square hatch in the floor of a
small grey vacuum work bay, seen from the side. He is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable in profile through it. The
back of the suit is one continuous smooth panel from collar to hip,
carrying nothing. A thin pale scratch runs along the left forearm sleeve of
the suit; his grip is tight and the glove's segments are lifted over the knuckles. His
right glove holds a short two-jawed cutter, its jaws already closed around
the pin of a matte grey clamp the length of a hand; his left glove is flat
on the hatch frame. A hooded hand-lamp the size of his fist rides dark in a
clip at his right hip. Five clamps still hold the disused module that hangs
below the opening — the module is a little longer than he is tall, matte,
dark and unmarked. Behind him, across the opening on the far arc of the ring, a
thin line runs from one of those clamps down through the hatch and out of
frame. Only his glove palms and knees are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the far arc and its
thin line the right background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no airbrushing,
no waxy texture. The front pane is clear glass with zero tint, zero mirror
coating and zero reflection. No back-mounted unit, no backpack, no tank, no
hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cutter's jaws are closed on the pin and the pin is still
whole. Exactly five clamps hold the module. No screens, no dials, no
gauges, no indicator lights. No readable text, letters, digits or symbols
anywhere in the frame; no scale marks, no graduation ticks; no flag, no
logo, no patch. No subtitles, no title card, no watermark. No dust, no
suspended grit, no haze. No smoke, no flame, no rust.
No lens flare, no anamorphic streak. Metal static and solid — no melting,
no warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 4 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. Five clamps hold the module at the start of the shot. Only
his glove palms and knees are dulled with wear.

SCENE (as in the start frame): the bay, the open hatch, the ring of clamp
seats, the disused module hanging below, and on the far arc behind him a thin
line running from one clamp down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus.

TIMELINE: 0.0s — the cutter's jaws are already closed on the pin and his
right glove is already squeezing; his grip tightens and the glove's segments lift
over the knuckles. 2.0s — behind him, across the opening, the thin line on
the far arc is plainly there in the frame; he does not look at it and his
helmet does not turn. 5.0s — the pin parts cleanly. The parted faces are
matt, flat and cold. 6.0s — freed on that side, the module drops a hand's width and stops
against its remaining clamps; the whole ring takes the load with one short
dull knock. 8.0s — the loose clamp comes away in his left glove. 10.0s —
hold; he stays crouched with the clamp in his fist.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module is still held by its remaining clamps and does not go further. Up is
the rock ceiling above the base; down is the black disc below it; the open
hatch faces the black disc. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard short bite of the
cutter transmitted through the frame; one dull knock as the module takes
its new angle; the flat click of the freed clamp against his glove; slow
breathing. Nothing else — no sound carries in this vacuum. No voice, no
music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cut makes no spark, no heat glow, no smoke, no molten metal
and no flying chips. The module moves only a hand's width and then holds on
its remaining clamps. No screens, no dials, no gauges, no indicator lights.
No readable text, letters or digits anywhere in frame; no scale marks, no
ticks; no flag, no logo. No subtitles, no watermark. No dust, no suspended
grit, no haze. No flame, no rust. No lens flare, no anamorphic
streak. Metal static — no melting, no warping. No tilt-shift or miniature
look. No voice, no music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 4 (S4) — BIRAKMA 🕰️ KÜME#1 (2/2) · KURULUM C

> ⛔ **KÜME KLİBİ [ACI_YAYI §3 🕰️]:** bu bir kesme değil, bölünmüş TEK
> çekimdir. Kamera metni S3'ün metnidir, kelimesi kelimesine, üstüne devam
> işareti eklenir. Kelepçe sayacı bu klibin sonunda 5 → 4 olur.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 5 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the same crouched man at the edge of the same open square hatch in
the same grey vacuum work bay, seen from the side, one moment later. He is
a man of fifty-four, heavy-shouldered, deep brown skin, in a matte dark
olive surface suit with faded sand-white bands at the shoulders and shins;
the helmet is a hard sand-white shell with a single flat front pane set
inside a visible dark rim — not a bubble, not a dome — the pane optically
clear with zero tint and zero mirror coating, his face fully readable in
profile through it. The back of the suit is one continuous smooth panel
from collar to hip, carrying nothing. A thin pale scratch runs along the
left forearm sleeve of the suit. The short two-jawed cutter now hangs in
his right glove at his side. His left glove is held out over the opening,
palm down, closed around a freshly cut matte grey clamp the length of a
hand. Four clamps still hold the disused module that hangs below the opening.
Behind him, across the opening on the far arc of the ring, a thin line runs
from one of those clamps down through the hatch and out of frame. A hooded
hand-lamp the size of his fist rides dark in a clip at his right hip. Only
his glove palms and knees are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the far arc and its
thin line the right background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp is still closed inside his left glove and
has not been released. Exactly four clamps hold the module. No screens, no
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
10-second single unbroken shot, 16:9, photorealistic. Scene 5 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. Four clamps hold the module for the whole shot. Only his
glove palms and knees are dulled with wear.

SCENE (as in the start frame): the bay, the open hatch, the disused module
hanging below on four clamps, and on the far arc behind him a thin line
running from one clamp down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus. Continues the previous clip
from its exact last frame — the same position, height and lens as Scene 4.

TIMELINE: 0.0s — his left glove is already held out over the opening, palm
down, closed around the freshly cut clamp. 2.0s — the fingers open and the
clamp is free of them, a hand's width below the palm and moving down. 3.0s
— it has gone about one body-length down into the dark and is visibly
slower. 6.0s — across these three seconds it moves only a hand's width
further, still downward, still the same direction. 8.0s — his glove
withdraws and his helmet stays turned down after the clamp. 10.0s — hold;
the clamp is still moving down.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second.
Everything below the lip of the hatch keeps moving downward for the whole
shot — always the same direction, never rising, never stopping, never held
in place — but each thing moves less the deeper it already is: the clamp
sinks about one body-length in the first second, then only a hand's width
across the next three seconds, then less. Up is the rock ceiling above the
base; down is the black disc below it. Everything released moves toward the
black disc, which fills the lower half of the frame, and never toward the rock. This is a vacuum: no air, no dust, no
wind.

AUDIO: the narrow steady bed of the suit fan; one dry click as the glove
opens; slow breathing inside the helmet. Nothing else — no sound carries in
this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The released clamp never rises, never stops, never hangs
motionless, never drifts sideways, never spins away; it is a solid object,
not a light or a spark. The clamp count stays four. No screens, no dials,
no gauges. No readable text, letters or digits anywhere in frame; no scale
marks, no ticks; no flag, no logo. No subtitles, no watermark. No dust, no
suspended grit, no haze, no drifting motes. No smoke, no exhaust, no flame,
no spark, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 5 (S5) — DÖRT · KURULUM D (dönüş · kaynak S2)

> ⛔ **DÖNÜŞ [ACI_YAYI §7 ⑥]:** kamera metni S2'nin metnidir, kelimesi
> kelimesine; sonuna işaret satırı eklenir. Kelepçe sayacı: DÖRT.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 6 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of the same small square vacuum work bay, seen from the
far wall. The bay is bare grey metal; its floor carries one open square
hatch about one body-length on a side, set slightly right of centre. Around
the hatch frame sit six clamp seats; four matte grey clamps the length of a
hand are still bolted through them, holding a disused cylinder that hangs just
below the opening — the module is a little longer than he is tall and twice
as thick as his hip, matte, dark and unmarked, and it now hangs a hand's width
lower on the near side than on the far side. Two seats are empty. Walking
the near arc of the ring is a man of fifty-four, heavy-shouldered, deep
brown skin, in a matte dark olive surface suit with faded sand-white bands
at the shoulders and shins; the helmet is a hard sand-white shell with a
single flat front pane set inside a visible dark rim — not a bubble, not a
dome — the pane optically clear with zero tint and zero mirror coating, his
face fully readable through it. The back of the suit is one continuous
smooth panel from collar to hip, carrying nothing. A short two-jawed cutter
is in his right glove; a hooded hand-lamp the size of his fist rides dark
in a clip at his right hip. A thin pale scratch runs along the left forearm
sleeve of the suit. Only his glove palms and knees are dulled with wear.
Running down from one clamp on the far arc of the ring, a thin line
disappears through the opening.

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
boot cuff. Exactly four clamps hold the module and two seats are
empty — the count does not change. No screens, no dials, no gauges, no
keypads, no indicator lights anywhere in the bay. No readable text,
letters, digits or symbols anywhere in the frame; no scale marks, no
graduation ticks; no flag, no logo, no patch. No subtitles, no title card,
no watermark. No dust, no haze. No smoke, no exhaust, no
flame, no spark, no rust. No lens flare, no anamorphic streak. Metal static
and solid — no melting, no warping. No
Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 6 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. A short two-jawed cutter stays in his right glove;
a hooded hand-lamp stays dark in the clip at his right hip. Four clamps
hold the module and two seats are empty for the whole shot.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch in its floor, the ring of six clamp seats, the disused module hanging
just below the opening at a slight angle, and a thin line running down
through the opening from one clamp on the far arc.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus — the same position,
height and lens as Scene 3.

TIMELINE: 0.0s — he is already mid-stride along the near arc, unhurried,
the cutter low in his right glove. 3.0s — he stops at the third clamp seat
and looks down at it, his helmet tipping forward. 5.0s — he lowers into a
crouch and his left glove goes flat on the hatch frame. 8.0s — his right
glove brings the cutter up and its jaws open. 10.0s — hold; the open jaws
are beside the clamp and nothing has been cut.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module holds on its four clamps and does not move. Up is the rock ceiling
above the base; down is the black disc below it; the open hatch faces the
black disc. This is a vacuum: no air, no dust, no wind, and his suit never
stirs.

AUDIO: the narrow steady bed of the suit fan; three dry boot contacts
transmitted through the deck; the flat knock of the glove landing on the
frame; the small hard click of the cutter's jaws opening; slow breathing.
Nothing else — no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; the front pane stays
clear and unmirrored; the back stays one continuous smooth panel with no
backpack, tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp count stays four and the two empty seats stay
empty. No screens, no dials, no gauges, no keypads, no indicator lights. No
readable text, letters or digits anywhere in frame; no scale marks, no
ticks; no flag, no logo. No subtitles, no watermark. No dust, no suspended
grit, no haze. No smoke, no flame, no rust. No lens
flare, no anamorphic streak. Metal static — no melting, no warping. No
tilt-shift or miniature look. No voice, no music. No CGI aesthetic.
Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 6 (S6) — ÜÇÜNCÜ · KURULUM C (dönüş · kaynak S4)

> ⛔ **DÖNÜŞ:** kamera metni S3/S4'ün metnidir; işaret satırı eklendi.
> Kelepçe sayacı bu klibin sonunda 4 → 3 olur.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 7 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the edge of an open square hatch in the floor of a
small grey vacuum work bay, seen from the side. He is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable in profile through it. The
back of the suit is one continuous smooth panel from collar to hip,
carrying nothing. A thin pale scratch runs along the left forearm sleeve of
the suit; his grip is tight and the glove's segments are lifted over the knuckles. His
right glove holds a short two-jawed cutter with its jaws closed around the
pin of a matte grey clamp the length of a hand; his left glove is flat on
the hatch frame. A hooded hand-lamp the size of his fist rides dark in a
clip at his right hip. Four clamps still hold the disused module hanging below
the opening, and the module leans a hand's width lower on the near side.
Behind him, across the opening on the far arc of the ring, a thin line runs
from one of those clamps down through the hatch and out of frame. Only his
glove palms and knees are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the far arc and its
thin line the right background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cutter's jaws are closed on the pin and the pin is
still whole. Exactly four clamps hold the module. No screens, no dials, no
gauges, no indicator lights. No readable text, letters, digits or symbols
anywhere in the frame; no scale marks, no graduation ticks; no flag, no
logo. No subtitles, no title card, no watermark. No dust, no suspended
grit, no haze. No smoke, no flame, no rust. No lens
flare, no anamorphic streak. Metal static and solid — no melting, no
warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 7 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. Four clamps hold the module at the start of the shot.

SCENE (as in the start frame): the bay, the open hatch, the ring of clamp
seats, the leaning disused module hanging below, and on the far arc behind him
a thin line running from one clamp down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 5.

TIMELINE: 0.0s — the cutter's jaws are already closed on the pin and his
right glove is already squeezing; his grip tightens and the glove's segments lift
over the knuckles. 3.0s — the pin parts cleanly. The parted faces are matt, flat and cold. 4.0s — the module drops another hand's width on that side and stops
against its remaining clamps, one short dull knock through the frame. 6.0s
— he lifts the freed clamp out with his left glove, holds it over the
opening and lets the fingers open; the clamp is free of them and moving
down. 8.0s — it has gone about one body-length down into the dark and is
visibly slower. 10.0s — hold; the clamp is still moving down and his helmet
stays turned after it.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second.
Everything below the lip of the hatch keeps moving downward for the whole
shot — always the same direction, never rising, never stopping, never held
in place — but each thing moves less the deeper it already is. Up is the
rock ceiling above the base; down is the black disc below it. This is a
vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard short bite of the
cutter through the frame; one dull knock as the module takes its new angle;
the flat click of the glove opening; slow breathing. Nothing else — no
sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cut makes no spark, no heat glow, no smoke, no molten metal
and no flying chips. The released clamp never rises, never stops, never
hangs motionless, never drifts sideways. No screens, no dials, no gauges.
No readable text, letters or digits anywhere in frame; no scale marks, no
ticks; no flag, no logo. No subtitles, no watermark. No dust, no suspended
grit, no haze, no drifting motes. No flame, no rust. No lens
flare, no anamorphic streak. Metal static — no melting, no warping. No
tilt-shift or miniature look. No voice, no music. No CGI aesthetic.
Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 7 (S7) — PİM · KURULUM B (makro)

> Bu kurulumun tek işi ÖLÇEK DEĞİŞTİRMEKTİR: kelepçe, pim ve kesicinin
> çenesi kadrajı doldurur. Bekçinin yüzü bu kadrajda YOKTUR — ⭐VİRAL
> etiketi taşımaz [§2.4 ön koşulu].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 8 of 25.
Exactly one human figure — this film has exactly one human total, and in
this frame only his two gloved hands are in shot.

SCENE: a close view of one matte grey clamp the length of a hand, bolted
through a seat in the frame of an open square hatch in a bare grey metal
floor. The clamp's pin stands proud of the seat, its head rounded and
polished smooth from years of handling. Two heavy segmented gloves are in
the frame and nothing else of the man: the right glove holds a short
two-jawed cutter with its jaws open on either side of the pin, not yet
closed; the left glove is braced flat on the hatch frame beside it, its
segments tight and lifted over the knuckles. Both gloves run into the
sleeves as one piece at the wrist, and the palms are dulled with wear.
Beyond the near edge of the frame the opening drops away into black, and
the dark bulk of the disused module fills the lower right corner.

CAMERA & LIGHT: 85mm spherical lens, fixed 0.9 m above the pin, outside the
ring. High angle close-up looking down, deep focus. Two hooded work lamps
in the bay ceiling light the clamp and the gloves from above with cool
neutral white; the metal walls of the bay throw no second light, and the
shadows inside the bay are absolutely black with razor edges. Nothing
lights the opening from below. The clamp and the pin hold the centre of the
frame, the two gloves the left and lower bands, the black of the opening
the right band.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human — no
second person, no other hands, no clone, no reflected figure. 0% bloom, no
glow filter, no soft focus. The gloves are heavy and segmented and run into
the sleeves as one piece at the wrist; no bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts keep a clear
structural boundary — no merging, no phasing, no extra fingers. The cutter's
jaws are open and the pin is whole. No readable text, letters, digits or
symbols anywhere in the frame — not on the clamp, the pin, the cutter, the
glove or the hatch frame; no scale marks, no graduation ticks, no engraved
or painted characters of any kind; no flag, no logo. No subtitles, no title
card, no watermark. No dust, no haze. No smoke, no
exhaust, no flame, no spark, no rust, no heat glow. No lens flare, no
anamorphic streak. Metal static and solid — no melting, no warping. No
tilt-shift or miniature look. No Unreal Engine look, no CGI aesthetic.
Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 8 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total, and in this shot only his two gloved hands are in frame.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: the two heavy segmented gloves
running into the sleeves as one piece at the wrist, palms dulled with wear;
the short two-jawed cutter; the matte grey clamp and its rounded polished
pin; the bare grey hatch frame; the dark bulk of the module in the lower
right.

SCENE (as in the start frame): the clamp bolted through its seat in the
hatch frame, the cutter's jaws open on either side of the pin, the left
glove braced flat on the frame, the opening dropping away into black.

CAMERA: 85mm spherical lens, fixed 0.9 m above the pin, outside the ring.
High angle close-up looking down, deep focus.

TIMELINE: 0.0s — the jaws are already open and already closing, moving in
on the pin from both sides. 2.5s — the jaws meet the pin and stop; his grip
tightens and the right glove's segments lift over the knuckles as it takes
the load. 5.0s — the left glove shifts its bracing hold a finger's width along
the frame and settles again. 8.0s — the right glove squeezes once more and
holds; the pin is still whole. 10.0s — hold; the jaws stay closed on the
pin and nothing else moves.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
The clamp and the frame are rigid and do not flex. All hand-surface
contacts keep a clear structural boundary. This is a vacuum: no air, no
dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the small hard click of the
jaws meeting the pin; the dry scrape of the bracing glove along the frame;
slow breathing. Nothing else — no sound carries in this vacuum. No voice,
no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no other
hands, no clone. 0% bloom, no glow filter, no soft focus. The gloves stay
identical, segmented, and joined to the sleeves at the wrist; no bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. All hand-surface contacts
keep a clear structural boundary — no merging, no phasing, no extra
fingers. The pin does not part in this shot. No spark, no heat glow, no
smoke, no molten metal, no flying chips. No readable text, letters or
digits anywhere in frame, on the clamp, pin, cutter, glove or frame; no
scale marks, no ticks, no engraved characters; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 8 (S8) — İKİ · KURULUM C (dönüş · kaynak S6)

> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.
> Kelepçe sayacı bu klibin sonunda 3 → 2 olur; modülün yatması GÖRÜNÜR.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 9 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a man crouched at the edge of an open square hatch in the floor of a
small grey vacuum work bay, seen from the side. He is a man of fifty-four,
heavy-shouldered, deep brown skin, in a matte dark olive surface suit with
faded sand-white bands at the shoulders and shins; the helmet is a hard
sand-white shell with a single flat front pane set inside a visible dark
rim — not a bubble, not a dome — the pane optically clear with zero tint
and zero mirror coating, his face fully readable in profile through it. The
back of the suit is one continuous smooth panel from collar to hip,
carrying nothing. A thin pale scratch runs along the left forearm sleeve of
the suit; his grip is tight and the glove's segments are lifted over the knuckles. His
right glove holds a short two-jawed cutter with its jaws closed around the
pin of a matte grey clamp; his left glove is flat on the hatch frame. A
hooded hand-lamp the size of his fist rides dark in a clip at his right
hip. Three clamps still hold the disused module hanging below the opening, and
the module now leans plainly, a forearm's length lower on the near side
than on the far side. Behind him, across the opening on the far arc of the
ring, a thin line runs from one of those clamps down through the hatch and
out of frame. Only his glove palms and knees are dulled with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the far arc and its
thin line the right background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. Exactly three clamps hold the module. No screens, no
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
10-second single unbroken shot, 16:9, photorealistic. Scene 9 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. Three clamps hold the module at the start of the shot.

SCENE (as in the start frame): the bay, the open hatch, the leaning disused
module hanging below, and on the far arc behind him a thin line running
from one clamp down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 7.

TIMELINE: 0.0s — his right glove is already squeezing the cutter, his grip
tightens on it and the glove's segments are already lifted over the knuckles. 2.0s — the pin parts
cleanly. The parted faces are matt, flat and cold. 3.0s — the module swings down a
forearm's length on the near side and stops hard against its remaining
clamps; the deck takes the knock and his braced left glove absorbs it. 5.0s
— his shoulders drop and his rear boot loads as he lifts the freed clamp
out, holds it over the opening and opens his fingers; it is free of them and
moving down. 8.0s — it has gone about one
body-length down into the dark and is visibly slower. 10.0s — hold; the
clamp is still moving down, and he is looking not at it but along the
module.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second.
Everything below the lip of the hatch keeps moving downward for the whole
shot — always the same direction, never rising, never stopping, never held
in place — but each thing moves less the deeper it already is. The module
stays held by its remaining clamps. Up is the rock ceiling above the base;
down is the black disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard short bite of the
cutter through the frame; one deep knock as the module swings and stops;
the flat click of the glove opening; slow breathing. Nothing else — no
sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cut makes no spark, no heat glow, no smoke, no molten metal
and no flying chips. The module swings once and then holds on its remaining
clamps; it does not fall free in this shot. The released clamp never rises,
never stops, never hangs motionless, never drifts sideways. No screens, no
dials, no gauges. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
dust, no suspended grit, no haze. No flame, no rust. No lens
flare, no anamorphic streak. Metal static — no melting, no warping. No
tilt-shift or miniature look. No voice, no music. No CGI aesthetic.
Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 9 (S9) — UZAK YAY · KURULUM D (dönüş · kaynak S5)

> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.
> Kelepçe sayacı: İKİ. Bekçi ilk kez halkanın UZAK yayına doğru gider —
> hattın bulunduğu yana.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 10 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of the same small square vacuum work bay, seen from the
far wall. The bay is bare grey metal; its floor carries one open square
hatch about one body-length on a side, set slightly right of centre. Around
the hatch frame sit six clamp seats; two matte grey clamps the length of a
hand are still bolted through them, holding a disused cylinder that hangs
below the opening — the module is a little longer than he is tall, matte,
dark and unmarked, and it now hangs plainly askew, one end a forearm's length
lower than the other. Four seats are empty. Crossing the deck toward the
far arc of the ring is a man of fifty-four, heavy-shouldered, deep brown
skin, in a matte dark olive surface suit with faded sand-white bands at the
shoulders and shins; the helmet is a hard sand-white shell with a single
flat front pane set inside a visible dark rim — not a bubble, not a dome —
the pane optically clear with zero tint and zero mirror coating, his face
fully readable through it. The back of the suit is one continuous smooth
panel from collar to hip, carrying nothing. A short two-jawed cutter is in
his right glove; a hooded hand-lamp the size of his fist rides dark in a
clip at his right hip. A thin pale scratch runs along the left forearm
sleeve of the suit. Only his glove palms and knees are dulled with wear.
Running down from one of the two remaining clamps on the far arc, a thin
line disappears through the opening.

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
boot cuff. Exactly two clamps hold the module and four seats are
empty — the count does not change. No screens, no dials, no gauges, no
keypads, no indicator lights anywhere in the bay. No readable text,
letters, digits or symbols anywhere in the frame; no scale marks, no
graduation ticks; no flag, no logo, no patch. No subtitles, no title card,
no watermark. No dust, no haze. No smoke, no exhaust, no
flame, no spark, no rust. No lens flare, no anamorphic streak. Metal static
and solid — no melting, no warping. No
Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 10 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. A short two-jawed cutter stays in his right glove;
a hooded hand-lamp stays dark in the clip at his right hip. Two clamps hold
the module and four seats are empty for the whole shot.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch in its floor, the ring of six clamp seats, the askew disused module
hanging below, and a thin line running down through the opening from one of
the two remaining clamps on the far arc.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus — the same position,
height and lens as Scene 6.

TIMELINE: 0.0s — he is already crossing the deck, mid-stride, moving around
the ring toward the far arc in the right third of the frame. 4.0s — he passes behind the opening and his
helmet turns down once toward the leaning module without breaking stride.
7.0s — he reaches the far arc, plants his boots and stops with his back
half turned to the camera; the back of his suit is one continuous smooth
panel from collar to hip, carrying nothing. 10.0s — hold; he stands still,
looking down at the two remaining clamps.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module holds on its two clamps and does not move. Up is the rock ceiling
above the base; down is the black disc below it; the open hatch faces the
black disc. This is a vacuum: no air, no dust, no wind, and his suit never
stirs.

AUDIO: the narrow steady bed of the suit fan; six dry boot contacts
transmitted through the deck, evenly spaced and toneless; slow breathing.
Nothing else — no sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; the front pane stays
clear and unmirrored; the back is one continuous smooth panel from collar
to hip, carrying nothing — no backpack, no tank, no hose, no cable, no rear
housing. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The
clamp count stays two. No screens, no dials, no gauges, no keypads, no
indicator lights. No readable text, letters or digits anywhere in frame; no
scale marks, no ticks; no flag, no logo. No subtitles, no watermark. No
dust, no suspended grit, no haze. No smoke, no exhaust, no flame, no spark,
no rust. No lens flare, no anamorphic streak. Metal static — no melting, no
warping. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 10 (S10) — KAYA VE AĞIZ · KURULUM F ⭐ ÖLÇEK KONTRASTI 1:10

> Filmin TEK dış kadrajı. ⭐ TEMA MOTİFİ (kamera + ışık): kayanın altında
> tek aydınlık ağız, altında hiç bitmemiş bir sütun.
> ⛔ İNSANSIZ DEĞİL — figür ağzın içinde, küçük ama okunur [KART 10].
> ⛔ Yapı ölçeği: figür ölçek şahididir [KART 13].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 11 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: a small box-shaped base hanging from the underside of a rock, seen
from below and out to one side. The upper third of the frame is the rock:
a dark, matte, pitted stone ceiling that runs out of frame in every
direction. Bolted to it, hanging under it, is a single grey metal box about
three and a half body-lengths across; a handrail runs round its outside. In
the floor of the box one square hatch stands open and it is the only bright
thing in the picture: a hard white rectangle of spilled work light, and
inside it, small against the opening, the figure of a man in a matte dark
olive surface suit with faded sand-white bands, his hard sand-white helmet
tipped down. Hanging just under the hatch is the dark bulk of a disused
cylinder held by two clamps and plainly askew. Below that, running down the
lower half of the frame, is a long column of separate solid objects, one
under the other, getting further apart and fainter with depth, ending in
points. The deeper a thing hangs below the lip, the less of the old lamp's
light reaches it: the near ones read as pale steel, the deep ones as faint
amber, the deepest as points only. The whole lower band of the frame,
beyond everything, is a perfectly black disc with no edge and no texture,
carrying one hairline of white along its rim.

CAMERA & LIGHT: 28mm spherical lens, fixed 9.0 m from the base and below
it. Low angle extreme wide shot pointing up, deep focus. The only light is
the work light spilling out of the open hatch; it catches the underside of
the box and the nearest stone of the rock and reaches nothing else. The
metal of the box throws no second light and the shadows are absolutely
black with razor edges. The rock holds the upper third, the box the middle
band, the hanging column and the black disc the lower half.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no crew, no figure on the handrail, no
reflected or doubled figure. 0% bloom, no glow filter, no soft focus, no
glow halo around the hatch. The black disc is perfectly black and flat with
no texture, no swirl, no accretion ring, no spiral, no jets, no fire, no
plasma; its only marking is one hairline of white along its rim. The
hanging objects are separate solid things, each countable — not sparks, not
embers, not particles, not a dust column. No stars, no nebula, no galaxy
band. No readable text, letters, digits or symbols anywhere in the frame —
not on the box, the handrail, the module, the rock or the black disc; no
scale marks, no graduation ticks, no survey markers; no flag, no logo, no
patch. No subtitles, no title card, no watermark. No dust, no suspended
grit, no haze. No smoke, no flame, no engine glow, no thruster. No lens flare, no anamorphic streak. Structures static and solid
— no melting, no warping. No tilt-shift look, no miniature or toy-model
read. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film
grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 11 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, small in
the lit hatch, in a matte dark olive surface suit with faded sand-white
bands and a hard sand-white helmet with one flat front pane in a visible
dark rim. The rock ceiling, the grey box, the handrail, the open hatch, the
askew module on its two clamps, the hanging column and the black disc stay
exactly where they are.

SCENE (as in the start frame): the base hanging under the rock, its one lit
hatch, the module below it, the long column of separate hanging objects,
and the black disc filling the lower band with one hairline of white along
its rim. The deeper a thing hangs below the lip, the less of the old lamp's
light reaches it: the near ones read as pale steel, the deep ones as faint
amber, the deepest as points only.

CAMERA: 28mm spherical lens, fixed 9.0 m from the base and below it. Low
angle extreme wide shot pointing up, deep focus.

TIMELINE: 0.0s — every object in the hanging column is already moving down,
each one creeping, the nearest fastest. 3.0s — inside the lit hatch the
small figure shifts his weight from one boot to the other and settles.
6.0s — the nearest object in the column has moved about a finger's width
further from the base; the deep points have barely changed. 10.0s — hold;
the column is still going down, the figure is still, and the black disc has
not changed at all.

PHYSICS: 0.40 g. Everything below the lip of the hatch keeps moving
downward for the whole shot — always the same direction, never rising,
never stopping, never held in place — but each thing moves less the deeper
it already is. Up is the rock ceiling above the base; down is the black
disc below it. Everything released moves toward the black disc, which fills
the lower half of the frame, and never toward the rock. The base and the rock do not move at all. This is a
vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; one long low structural groan
transmitted through the box's mounts; slow breathing. Nothing else — no
sound carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change, no drift, no parallax. Exactly one human — no second
person, no clone, no crew, no figure on the handrail. 0% bloom, no glow
filter, no soft focus, no glow halo around the hatch. The black disc is
perfectly black and flat with no texture, no swirl, no accretion ring, no
spiral, no jets, no fire, no plasma; its only marking is one hairline of
white along its rim, and it does not move or pulse. No stars, no nebula.
The hanging objects are separate solid things, each countable — not sparks,
not embers, not particles, not a dust column; they never rise, never stop,
never hang motionless, never swirl. No readable text, letters or digits
anywhere in frame; no scale marks, no ticks, no survey markers; no flag, no
logo. No subtitles, no watermark. No dust, no haze. No
smoke, no exhaust, no flame, no spark, no engine glow, no thruster. No lens
flare, no anamorphic streak. Structures static — no melting, no warping. No
tilt-shift look, no miniature or toy-model read. No voice, no music. No CGI
aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 11 (S11) — GERİ · KURULUM D (dönüş · kaynak S9)

> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.
> Kelepçe sayacı: İKİ (değişmez). Bekçi artık uzak yayda çalışıyor ve
> ⭐ dramatik ironi burada en gergin: hat kadrajda, o hâlâ görmüyor.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 12 of 25.
Exactly one human figure — this film has exactly one human total.

SCENE: the inside of the same small square vacuum work bay, seen from the
far wall. The bay is bare grey metal; its floor carries one open square
hatch about one body-length on a side, set slightly right of centre. Around
the hatch frame sit six clamp seats; two matte grey clamps the length of a
hand are still bolted through them, holding a disused cylinder that hangs
below the opening — the module is a little longer than he is tall, matte,
dark and unmarked, and hangs plainly askew, one end a forearm's length lower
than the other. Four seats are empty. Crouched on the far arc of the ring,
side on to the opening, is a man of fifty-four, heavy-shouldered, deep
brown skin, in a matte dark olive surface suit with faded sand-white bands
at the shoulders and shins; the helmet is a hard sand-white shell with a
single flat front pane set inside a visible dark rim — not a bubble, not a
dome — the pane optically clear with zero tint and zero mirror coating, his
face fully readable through it, turned down to the nearer of the two
clamps. The back of the suit is one continuous smooth panel from collar to
hip, carrying nothing. A short two-jawed cutter is in his right glove; a
hooded hand-lamp the size of his fist rides dark in a clip at his right
hip. A thin pale scratch runs along the left forearm sleeve of the suit.
Only his glove palms and knees are dulled with wear. From the further of
the two clamps, an arm's length beyond his shoulder, a thin line runs down
through the opening and out of frame.

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
boot cuff. Exactly two clamps hold the module and four seats are
empty. No screens, no dials, no gauges, no keypads, no indicator lights. No
readable text, letters, digits or symbols anywhere in the frame; no scale
marks, no graduation ticks; no flag, no logo, no patch. No subtitles, no
title card, no watermark. No dust, no haze. No smoke, no flame, no rust. No lens flare, no anamorphic streak.
Metal static and solid — no melting, no warping. No tilt-shift or miniature
look. No Unreal Engine look, no CGI aesthetic. Photorealistic, 35mm film
grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 12 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable, his back one continuous smooth
panel carrying nothing. A hooded hand-lamp stays dark in the clip at his
right hip. Two clamps hold the module and four seats stay empty for the
whole shot.

SCENE (as in the start frame): the bare grey vacuum bay, the open square
hatch, the askew disused module on its two clamps, the crouched man on the far
arc, and the thin line running down through the opening from the further of
the two clamps, an arm's length beyond his shoulder.

CAMERA: 24mm spherical lens, fixed 5.0 m from him at the far wall of the
bay, eye-level and square on. Wide shot, deep focus — the same position,
height and lens as Scene 10.

TIMELINE: 0.0s — he is already reaching, his left glove sliding out along
the hatch frame toward the nearer clamp. 3.0s — the glove settles and takes
his weight; his grip tightens and the segments lift over the knuckles. 6.0s — his
right glove brings the cutter across and its jaws open beside the nearer
clamp's pin. 8.0s — beyond his shoulder the thin line hangs plainly in the
frame; his helmet does not turn toward it. 10.0s — hold; the open jaws are
beside the pin and nothing has been cut.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module holds on its two clamps and does not move. The thin line is straight
and taut and does not swing. Up is the rock ceiling above the base; down is
the black disc below it. This is a vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the dry scrape of the glove
along the frame; the small hard click of the cutter's jaws opening; slow
breathing. Nothing else — no sound carries in this vacuum. No voice, no
music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
crew, no reflected figure. 0% bloom, no glow filter, no soft focus. Suit,
helmet, cutter and hip lamp identical throughout; the front pane stays
clear and unmirrored; the back stays one continuous smooth panel with no
backpack, tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The clamp count stays two. The thin line never sags, never
curves, never sways and never swings. No screens, no dials, no gauges, no
keypads, no indicator lights. No readable text, letters or digits anywhere
in frame; no scale marks, no ticks; no flag, no logo. No subtitles, no
watermark. No dust, no haze. No smoke, no exhaust, no
flame, no spark, no rust. No lens flare, no anamorphic streak. Metal static
— no melting, no warping. No voice, no
music. No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

## 🎬 SAHNE 12 (S12) — SALINIM · KURULUM C (dönüş · kaynak S8) ⭐VİRAL

> ⭐ **VİRAL KAPISI [§2.4]** — iki ölçüt de bu sahnede:
> **YÜZ:** çene gevşer, göz kapakları bir kez hızlı kapanıp açılır (0,4 s).
> **HAREKET:** modül tek yandan boşalır, bir karış düşüp bir gövde boyu
> SALINIR; altındaki bütün noktalar kadrajda kayar.
> ⛔ **DÖNÜŞ:** kamera metni birebir; işaret satırı eklendi.
> Kelepçe sayacı bu klibin sonunda 2 → 1 olur.
> ⛔ **BÖLÜM 1 BURADA BİTER.** Sonraki sahne `THE_KEPT_LIGHT_BOLUM_2.md`.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Scene 13 of 25.
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
sleeve of the suit; his grip is tight and the glove's segments are lifted over the
knuckles. His right glove holds a short two-jawed cutter with its jaws
closed around the pin of a matte grey clamp; his left glove is flat on the
hatch frame. A hooded hand-lamp the size of his fist rides dark in a clip
at his right hip. Two clamps still hold the disused module hanging below the
opening, and the module hangs plainly askew. From the second of those two
clamps, an arm's length beyond his shoulder, a thin line runs down through
the opening and out of frame. Only his glove palms and knees are dulled
with wear.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.0 m from him, side-on at eye
height. Medium shot in profile, eye-level, deep focus. Two hooded work
lamps in the bay ceiling light him from above with cool neutral white; the
metal walls of the bay throw no second light, and the shadows inside the
bay are absolutely black with razor edges. Nothing lights the opening from
below. A low rim light separates his shoulders and helmet from whatever is
behind him; his silhouette never merges with the background. He holds the
left half of the frame, the open hatch the lower band, the second clamp and
its thin line the right background.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
no second person, no clone, no reflected or doubled figure. 0% bloom, no
glow filter, no soft focus. Photorealistic skin with pores — no
airbrushing, no waxy texture. The front pane is clear glass with zero tint,
zero mirror coating and zero reflection. No back-mounted unit, no backpack,
no tank, no hose, no cable. No bare skin anywhere in frame: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cutter's jaws are closed on the pin and the pin is
still whole. Exactly two clamps hold the module. No screens, no dials, no
gauges, no indicator lights. No readable text, letters, digits or symbols
anywhere in the frame; no scale marks, no graduation ticks; no flag, no
logo. No subtitles, no title card, no watermark. No dust, no suspended
grit, no haze. No smoke, no flame, no rust. No lens
flare, no anamorphic streak. Metal static and solid — no melting, no
warping. No Unreal Engine look, no CGI
aesthetic. Photorealistic, 35mm film grain.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Scene 13 of 25. Fixed
locked-off camera. Exactly one human figure — this film has exactly one
human total.

START FRAME: the approved still from this scene's IMAGE prompt — animate
it. CONTINUITY LOCKS carried from the frame: exactly one human, a man of
fifty-four, heavy-shouldered, deep brown skin, matte dark olive surface
suit with faded sand-white shoulder and shin bands, hard sand-white helmet
with one flat front pane in a visible dark rim, the pane optically clear
and reflection-free, his face readable in profile, his back one continuous
smooth panel carrying nothing. A hooded hand-lamp stays dark in the clip at
his right hip. Two clamps hold the module at the start of the shot.

SCENE (as in the start frame): the bay, the open hatch, the askew disused
module hanging below on two clamps, and beyond his shoulder the second
clamp with a thin line running down through the opening.

CAMERA: 50mm spherical lens, fixed 2.0 m from him, side-on at eye height.
Medium shot in profile, eye-level, deep focus — the same position, height
and lens as Scene 9.

TIMELINE: 0.0s — his right glove is already squeezing the cutter, his grip
tightens on it and the glove's segments are already lifted over the knuckles. 2.0s — the pin parts
cleanly. The parted faces are matt, flat and cold. 2.4s — freed on that side, the
module drops a hand's width and then swings a full body-length across
beneath the opening, hanging now from its single remaining clamp; every
object in the dark below it shifts across the frame as the swing passes.
3.0s — his jaw slackens and his eyelids close and open once, fast, in the
same half second; his helmet stays where it is. 5.0s — the module's swing
comes back and settles, still hanging from one clamp. 8.0s — he lifts the
freed clamp out and lets his fingers open over the opening; it is free of
them and moving down. 10.0s — hold; the module hangs from one clamp and the
clamp is still moving down.

PHYSICS: 0.40 g, ordinary deliberate movement in real time, no slow motion.
Above the deck the gravity is ordinary: a tool let go from his glove
strikes the deck in about one second. The
module is a rigid body swinging on one clamp: it does not stretch, bend or
deform. Everything below the lip of the hatch keeps moving downward for the
whole shot — always the same direction, never rising, never stopping, never
held in place — but each thing moves less the deeper it already is. Up is
the rock ceiling above the base; down is the black disc below it. This is a
vacuum: no air, no dust, no wind.

AUDIO: the narrow steady bed of the suit fan; the hard short bite of the
cutter through the frame; a long low groan through the deck as the module
swings and the last clamp takes its weight; the flat click of the glove
opening; one held breath, then breathing again. Nothing else — no sound
carries in this vacuum. No voice, no music.

NEGATIVE: Single unbroken take, locked-off camera — no cuts, no pans, no
zoom, no angle change. Exactly one human — no second person, no clone, no
reflected figure. 0% bloom, no glow filter, no soft focus. Suit, helmet,
cutter and hip lamp identical throughout; the front pane stays clear and
unmirrored; the back stays one continuous smooth panel with no backpack,
tank, hose or cable. No bare skin anywhere: none above the collar seal,
none at the wrist between glove and sleeve, none at the ankle above the
boot cuff. The cut makes no spark, no heat glow, no smoke, no molten metal
and no flying chips. The module stays a rigid body — no stretching, no
bending, no deformation — and it does not come free of its last clamp in
this shot. The released clamp never rises, never stops, never hangs
motionless. No screens, no dials, no gauges. No readable text, letters or
digits anywhere in frame; no scale marks, no ticks; no flag, no logo. No
subtitles, no watermark. No dust, no haze. No flame, no rust. No lens flare, no anamorphic streak. Metal static — no
melting, no warping. No voice, no music.
No CGI aesthetic. Photorealistic, 35mm film grain.
```

---

> **BÖLÜM 1 SONU — S12 · 2:09.**
> Devam: `THE_KEPT_LIGHT_BOLUM_2.md` (S13-S24 · 2:09 – 4:09)
> ⛔ Bölüm sınırı da ardışık bir çifttir: S12 kurulum **C** (MS · profil) →
> S13 kurulum **D** (WS · göz hizası) = 1 ölçek kademesi + 90° azimut ✅
