# 🛰️ THE SECOND SHIP — FAZ 5 / TEMAS · KISIM 5

## S41–S50 PROMPTLARI | 6:40 – 8:20 | Perde II | 16:9 Yatay
### _"Cevap veren herkes ölür."_

> Plan: `00_PLAN.md` · Bible + harita: `README.md` · Anlatı: `../01_SENARYO.md`
> Faz kilitleri (kask · diyalog kadrajı · 10s yolu) + 📎 REFERANS
> lejandı: `../FAZ_01_TRANSIT/FAZ_01_TRANSIT.md`
>
> ✅ **KAPSAM: S41–S50 TAM.** 05.08.2026 yapısı: 10 faz × 10 sahne =
> 100 sahne = 16:40. S50, F6'ya SES KÖPRÜSÜ kurar (200 yılın ilk
> sessizliği) — `../FAZ_06_KULE/FAZ_06_KULE.md` o sessizlikten açılır.
> Kısmın sorusu: _Konuşamadığın bir şeye nasıl güvenirsin?_
>
> ⛔ Her prompt **self-contained**'dır (AGENTS.md kural ③). Uzunluk
> bandı (README §6, 06.08.2026 revizyonu): **imaj 1.700–2.300 ·
> video 1.950–2.600** karakter.

---

# 🔒 FAZ 5'E ÖZEL KARARLAR

## KARAR 1 — BEKÇİ'NİN DİYALOĞU GÖRÜNTÜYE YAZILMAZ

```
"DO NOT. DO NOT." (S43) filmin ilk Bekçi repliğidir ve SES post'ta
eklenir (ElevenLabs — bozuk, bantlı, 200 yıllık insan kaydından
kesilmiş kelimeler; MUZIK_VE_SES.md). Vizör OPAK → lip-sync riski
SIFIR. Kadrajda repliği temsil eden tek şey: Bekçi'nin başının bir
kez, çok yavaş öne eğilmesi. Promptlara "speaking/talking" YAZILMAZ.
```

## KARAR 2 — ZEMİN SADECE İKİ SAHNEDE TEPKİ VERİR (S45 · S47)

```
Novum'un gerçek-zamanlı zemin tepkisi TÜM FİLMDE üç yerde var; ikisi
bu fazda: S45 (çizim yeniden oluşur) ve S47 (adım nefesi). Kural:
yüzey KUM TANESİ ölçeğinde hareket eder — kabarır, iner, taneler
akar. Zemin asla YARILMAZ, açılmaz, ışımaz; damarlar mat kalır
[Ders 3/29]. Diğer tüm sahnelerde zemin ölü ve hareketsizdir.
```

## KARAR 3 — ÖLÜ HALKA ZEMİNİ = R3 PLAKASININ ZEMİNİ

```
S49'da zemin bıçak keskinliğinde bir çizgiyle değişir: dokulu,
damarlı bazalt → cilalı, tozsuz, honlanmış taş. Bu cilalı zemin
REFERANS_PAKETI R3 master plakasının zeminiyle AYNIDIR — Bekçi
imajlarıyla halka sahneleri aynı yüzeyde buluşur. Sınır çizgisi hep
KESKİN yazılır: geçiş bandı, degrade, erime yok.
```

## KARAR 4 — F1-F4 QA TAŞINANLARI (09.08.2026)

> Kaynaklar: `../FAZ_01_TRANSIT/FAZ_01_QA_DERSLER.md` ·
> `../FAZ_02_VURULMA/FAZ_02_QA_DERSLER.md` ·
> `../FAZ_03_IMDAT/FAZ_03_QA_DERSLER.md` ·
> `../FAZ_04_TARLA/FAZ_04_QA_DERSLER.md`

```
① ⛔ BEKÇİ ÇAPA KAPISI [F4 D-R · Ders 68 ②]
   F4 S40'ta Bekçi jenerik astronot çıktı: sırt çantası + oluklu
   hortum, kirli/dikişli suit, BEYAZ vizör, normal boy, normal kol.
   Spec'in yedi maddesinden beşi düştü; yalnız dönüş hareketi tuttu.
   Bu fazın YEDİ Bekçi sahnesi o çapaya yaslanıyor.
   → R3 master plakası üretilip İNSAN GÖZÜYLE onaylanmadan F5'in
     hiçbir Bekçi sahnesi üretilmez. Düşen dört madde bu fazın her
     Bekçi promptuna gömüldü: DÜZ SIRT (çanta/hortum/çıkıntı yok) ·
     koyu gri-yeşil, neredeyse siyah vizör (asla beyaz, asla ayna) ·
     KARŞILAŞTIRMALI boy (1.81 m adamdan bir baş uzun) · üç parmak.

② BENZETME MALZEMEYİ ÜRETİR [F2 D-A]
   "cam gibi" gerçek cam üretti, "dalış" sözlüğü su üretti. Bu fazda
   dört benzetme temizlendi: S45'in "yavaş kuru su gibi akan taneler"
   ve "sudan sonraki kum gibi", S49'un "cama dayanmış kum gibi",
   S50'nin "durgun suya konan el gibi" → fiziksel tarife çevrildi.
   S49'a ayrıca "ortada duvar/cam/kubbe/bariyer YOK" negasyonu girdi.
   Yeni prompt yazarken benzetme kullanma.

③ BOŞLUĞU YASAKLAMA, DOLDUR [F4 D-Q]
   F4 S39'da "vizörde göz/yüz/kafatası yok" negasyonu VARDI ve model
   oyuğa yüz oydu. Model oyuk görürse doldurur. Bekçi'nin vizörü
   artık "arkasında bir şey olmayan pencere" değil, kaskla sürekli
   DOLU MAT PLAKA olarak yazılıyor (S41 S43 S46 S50).

④ ROKET NEGASYONU KULEYE [F3 D-K · F4 D-O]
   dik + beyaz + hafif konik = roket refleksi (F3'te "dik duran gemi"
   roket çizildi). S46'nın ufuk çizgisine ve S48/S50'nin 400 m
   kulesine roket negasyonu gömüldü. Ayrıca F4 D-O'nun kardeşi:
   IŞIKSIZ PENCERE DE PENCEREDİR — "no lit windows" yetmiyor,
   "no windows at all, lit or unlit, no openings of any kind" yazılır.

⑤ SAHNENİN BİLGİSİ CÜMLEYLE AÇILIR [F4 D-T · F3 D-I]
   Dekor üretilip OLAY üretilmeyen sahne sınıfı iki fazda tekrarladı
   (F3 S22 eldiven ritüeli hiç çıkmadı · F4 S37 karşılaştırma öğesi
   düştü). S42 S44 S45 S47 S49 promptları artık
   "THE ONLY EVENT OF THIS SHOT IS ___" cümlesiyle açılıyor ve o öğe
   negatif blokta tekrarlanıyor.

⑥ KASK ÇİFT KİLİDİ [F1 ②]
   Tek cümlelik kask kilidi F1 S9'da delindi. İnsan yüzü/kaskı olan
   altı sahneye (S41 S42 S44 S46 S48 S49) ikinci kilit eklendi:
   "every helmet is ON and sealed for every frame".

⑦ ZEMİN AKIŞINA SAYI [F4 D-P · F1 ③]
   F4 S32'de "ince zayıf toz sürüklenmesi" kum ŞELALESİNE döndü;
   sürekli akan malzeme kopyanın büyüdüğü izlenimi verdi. S45/S47'nin
   zemin hareketine sayısal sınır yazıldı: oluk derinliğini aşmaz,
   2 saniye içinde durur, tane havada asılı kalmaz, şelale yok.

⑧ ÜÇ FİGÜR = DÖRDÜNCÜ FİGÜR RİSKİ [F3 D-L]
   F3 S30'da geniş kadrajda BEYAZ figür üredi. Bu fazın iki üç-figür
   sahnesi (S41 S48) ve iki geniş ova sahnesi (S46 S49) "exactly N
   figures — no fourth, no duplicate, nobody in the background"
   negasyonunu taşır.

⑨ MONTAJ PROTOKOLÜ — ARTIK KAPI [F1 ① · F3 ④ · F4 §1]
   Dört fazın üçünde reel sırası karıştı (F1 dörtlü rotasyon · F3 beş
   misfile · F4 ikili takas); MODE T hiç denenmedi. F5 QA'sı
   birleştirilmiş reel ile KOŞULMAZ: 10 ayrı dosya, adında sahne
   numarası (s41.mp4 … s50.mp4). Montajdan önce zorunlu kontrol:
   10 klip × 10.00 s [F3 D-N · F4 D-V].
```

## 10 SANİYE YOLU (FAZ_01 · KİLİT 3 uygulaması)

```
B yolu (1 sahne):  S43  → kadro B, Bekçi neredeyse hareketsiz
A yolu (9 sahne):  S41 S42 S44 S45 S46 S47 S48 S49 S50
```

---

# 🎨 ÜRETİM SIRASI VE İMAJ BÜTÇESİ

```
S41–S50 = 10 video · 13 imaj  (S45 · S47 · S49 END FRAME imajı da
alır — çizim yer değiştirmiş / kaydırma ilerlemiş / push-in sınıra
varmış)

⛔ ÜRETİM KAPISI — bu faz açık kapıyla başlamaz [KARAR 4 ①]
   F2'nin 1. aksiyonu açıkken F3 üretildi (10 sahnenin 6'sı yeniden
   üretim); F4'te S40 tetik kapısı atlandı (Bekçi jenerik astronot
   çıktı) ve S32 çapası onaylanmadan S35 üretildi (afiş karesi yandı).
   Aynı sınıf ihlal ÜÇ kez, her seferinde faz maliyeti iki katı.
   F5 için kapı: R3 BEKÇİ MASTER plakası üretilir ve insan gözüyle
   doğrulanır — düz sırt · koyu vizör · 2.10 m · uzun kol · üç parmak.
   Onaylanmadan S41 S43 S45 S46 S47 S48 S50 üretilmez (7/10 sahne).

ÖNERİLEN SIRA (kolaydan zora):
  1) S43 → tek Bekçi, lockoff (⛔ R3 master ŞART; F4 S40 düzeltilmiş
     çıktısı da onaylanmış olmalı — bu kare R3'ün saha testidir)
  2) S50 → Bekçi + kule yüzeyi (S43 malzemesiyle)
  3) S44 → Kaptan + toz çizimi (el riski, tek kişi)
  4) S45 · S47 → zemin tepkisi sahneleri (KARAR 2 dili; en riskli
     iki sahne — fazla deneme bütçele)
  5) S46 → Bekçi + Kaptan işaret karesi
  6) S42 · S49 → iki insan
  7) S41 · S48 → ÜÇ FİGÜR (filmin en pahalı karelerinden ikisi —
     5 sahnelik üç-figür bütçesinin 1. ve 2.'si burada yanar)

SES: on sahnenin onu da SESSİZ üretilir. Bekçi repliği, anons ve
     girdap post'ta (ElevenLabs + `MUZIK_VE_SES.md`).
```

---

## 🎬 SAHNE 41 — BEKÇİ

`6:40 – 6:50` · 32mm · kadro 2+B · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 + R3 (ÜÇ FİGÜR — üç master birlikte; KARIŞMA KİLİDİ promptta)

_"2.10 metre."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: antagonist sanılan şey sahneye girer. Tehdit göstermez;
  sadece durur — ve durması korkuyu büyütür.
  ⭐ S40'ın dönüşü TAMAMLANMIŞ hâlde açılır (eylem sürekliliği):
     Bekçi artık tam karşılarında.
  ⚠️ ÜÇ FİGÜR SAHNESİ 1/5. İnsanlar kadrajın bir yanında, Bekçi
     öbür yanında — araya 8 m mesafe yazılır, boy farkı okunur.
```

### 📸 IMAGE PROMPT

```
SCENE:
Two human crew stand face to face with a tall sealed white figure
across eight meters of open dust — nobody moves, nobody threatens.

ENVIRONMENT:
A clearing at the wreck field's edge: grey stone twins and
weathered hulls blurred at frame edges. Soft orange 4400K daylight,
soft-edged shadows, pale grey-green sky, faint daytime moon, fine
settled dust.

SUBJECT:
Three figures. LEFT third, side by side: a 41-year-old woman pilot,
1.68 m — light olive skin, a fine faded white scar splitting her
LEFT eyebrow, dark brown low bun, ORANGE worn reinforcement on a
dark grey-blue suit; and a 33-year-old man, 1.81 m,
broad-shouldered — short black stubble, a 2 cm burn scar on his
RIGHT cheekbone, TEAL GREEN reinforcement, oversized back tool
module; his helmet 13 cm higher.
RIGHT third, eight meters away, facing them: a tall sealed figure,
2.10 m — a full head taller than the man opposite.
Seamless, flawlessly pearl-white, dustless, unmarked; LONG arms to
knee level, three-fingered gloves; BACK FLAT and bare. Smooth
featureless helmet carrying one FILLED matte plate of
dark grey-green, nearly black, where a visor would be — solid,
continuous with the shell, nothing behind it.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position twelve meters
away, square to the standoff, at chest height — all three full
figures and the empty dust between them in frame. If the eight
meters of empty dust between them is not readable across the frame,
the shot is wrong.

LIGHTING:
Soft orange 4400K daylight from frame LEFT; subtle specular on the
pearl shell, warm rims on the suits. Nothing glows.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly three figures
— no fourth, nobody in the background. Orange stays on the woman,
teal on the man; scars stay LEFT eyebrow / RIGHT cheekbone; no
morphing. Every helmet is ON and sealed; human visors stay clear
uncoated glass. The white figure's visor is a solid filled dark
grey-green plate — never white, never transparent; no face, eyes or
light in or behind it. Its back stays flat: no backpack, no hoses.
The white suit stays clean and seamless; rigid anatomy. No weapons.
No bloom, no glow filter, no lens flare. No readable text or digits;
no captions, no HUD, no watermark. Photorealistic, 35mm anamorphic
film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff twelve meters
away, no cuts, no camera movement:

SETUP: the camera is locked off at chest height, square to a
standoff across eight meters of open dust. It never moves for the
whole ten seconds.
FRAME: a clearing at the wreck field's edge, soft orange 4400K
daylight from frame LEFT, pale grey-green sky, faint daytime moon.
LEFT third: a 41-year-old woman pilot, 1.68 m, ORANGE worn
reinforcement on a dark grey-blue suit, faded scar through her LEFT
eyebrow, dark brown low bun; beside her a 33-year-old man, 1.81 m,
broad-shouldered, TEAL GREEN reinforcement, short black stubble,
burn scar on his RIGHT cheekbone, oversized back module — both
visors transparent. RIGHT third: a tall sealed figure, exactly
2.10 m, a full head taller than the man — flawlessly pearl-white
seamless suit, dustless, FLAT BACK with no backpack and no hoses,
long arms to knee level, three-fingered gloves, smooth featureless
helmet whose visor is one filled matte plate of dark grey-green,
nearly black, facing them.

0s — Total stillness on both sides. Three long shadows lie parallel
on the dust.
3s — The man's hand drifts a few centimeters toward his hip — and
stops mid-air. The white figure does not react in any way.
5s — The white figure's helmet tips DOWN by a few degrees — one
slow, continuous motion, reading the humans from crown to boots —
then returns just as slowly to level.
8s — The woman's chest rises and falls once. Nobody has moved a
step.
10s — The standoff holds to the final frame: two small suits, one
tall white shape, eight meters of dust. No cuts.

The white figure's only motion is the single slow head tip — one
continuous flow, never jerky, never repeated; it never steps, never
raises a hand, never threatens. Its anatomy stays rigid: 2.10 m, same
silhouette, same finger count, no morphing; its back stays flat — no
backpack or hose grows on it; its suit stays dustless. Its visor is a
solid filled dark grey-green plate for every frame — never white,
never mirrored, never transparent; nothing appears in or behind it.
The humans never draw a tool; the sheath stays closed; helmets stay
ON and sealed, visors clear glass. Orange stays on the woman, teal on
the man; the 13 cm difference holds; scars stay LEFT eyebrow / RIGHT
cheekbone; no face swap. Exactly three figures — no fourth, nobody in
the background. Camera locked: no cuts, no transitions, no shake, no
zoom. No bloom, no glow filter, no lens flare. No readable text or
digits; no captions, no HUD, no watermark. Photorealistic, 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE 42 — MESAFE

`6:50 – 7:00` · 50mm · kadro 2 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan yakın kadraj)

_"Kaptan kolunu indiriyor."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit. Bekçi KADRAJ DIŞINDA.
  İŞLEV: iki karakterin refleks farkı ilk kez çatışır — dokunan adam
  savunmaya, okuyan kadın beklemeye geçer.
  ⭐ Kesici alet KILIFINDAN ÇIKMAZ [Ders 37]: el kılıfa GİDER,
     Kaptan bileği tutar, kol iner. Alet asla görünmez.
  ⚠️ Konuşma yok — sahnenin tamamı el ve bilek dili.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 12.'si.
```

### 📸 IMAGE PROMPT

```
SCENE:
A woman's gloved hand closes around her crewmate's wrist, stopping
his reach toward the sealed tool sheath on his hip.

ENVIRONMENT:
The wreck-field clearing in soft orange daylight, 4400K, from frame
LEFT: blurred grey stone twins and weathered hulls behind, pale
grey-green sky, fine settled dust. The tall white figure is OUT of
frame; both human faces are angled toward where it stands, off
frame RIGHT.

SUBJECT:
Exactly two figures, waist-up, close together. RIGHT: a 33-year-old
man flight engineer, 1.81 m, broad-shouldered — light brown skin,
short black stubble, a 2 cm burn scar on his RIGHT cheekbone, TEAL
GREEN worn reinforcement on a dark grey-blue suit, oversized back
tool module — his right hand reaching down and back toward the
CLOSED cutting-tool sheath on his left hip, body half-turned.
LEFT, a step behind him: a 41-year-old woman pilot, 1.68 m, slim —
light olive skin, faded scar through her LEFT eyebrow, dark brown
low bun, ORANGE reinforcement — her right hand closed firmly around
his reaching wrist, pressing it down. Both visors transparent, both
gazes locked off frame RIGHT.

CAMERA:
Shot on a 50mm lens from a fixed position two point five meters
away, f/4, at chest height, both figures and the held wrist sharp.
True scale; his helmet rides 13 cm higher.

LIGHTING:
Soft orange 4400K daylight from frame LEFT, modelling both faces
through the glass; warm rim on her restraining glove.

NEGATIVE:
THE ONLY EVENT OF THIS SHOT IS THE GRIP: her glove closed around his
reaching wrist, holding it short of the sheath. If the grip is not
visible, the shot has failed.
Single unbroken take, no cuts, no camera shake. Exactly two figures —
the white figure never enters frame, and nobody stands behind them.
The sheath stays CLOSED; no tool, no blade, no weapon ever appears.
Orange stays on the woman, teal on the man; scars stay LEFT eyebrow /
RIGHT cheekbone; no morphing, no face swap. Every helmet is ON and
sealed for every frame — no bare head, no bare skin. Visors stay
clear, uncoated glass — no tint, no mirror coating, no reflection
that hides what is behind them. Hands keep clear boundaries — never
merging. No bloom, no glow filter, no lens flare. No readable text or
digits; no captions, no watermark. Photorealistic, 35mm anamorphic
film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff two point five meters
away, no cuts, no camera movement:

SETUP: the camera is locked off at chest height on two figures
waist-up, f/4, their eyes angled off frame RIGHT at something the
lens never shows. It never moves for the whole ten seconds.
FRAME: soft orange 4400K daylight from frame LEFT, blurred wreck
pairs behind, pale grey-green sky. RIGHT: a 33-year-old man flight
engineer, 1.81 m, broad-shouldered, TEAL GREEN worn reinforcement,
short black stubble, burn scar on his RIGHT cheekbone, oversized
back module, closed cutting-tool sheath on his left hip. LEFT: a
41-year-old woman pilot, 1.68 m, slim, ORANGE reinforcement, faded
scar through her LEFT eyebrow, dark brown low bun. Both visors
transparent.

0s — He takes one slow step back, eyes off frame right, and his
right hand starts down and back toward the sheath on his hip.
2s — Her hand comes across and closes around his wrist before it
reaches the sheath — firm, quiet, no snatch.
4s — A held beat: his forearm tenses against her grip; her hand
presses the arm DOWN a centimeter at a time, steady as a
metronome. Neither face leaves the off-frame figure.
7s — His fingers open. The arm goes loose; she guides it down to
his side and releases the wrist.
10s — They stand side by side again, both facing off frame right,
the sheath still sealed. No cuts.

THE ONLY EVENT OF THIS SHOT IS THE GRIP AND THE ARM COMING DOWN — if
her hand never closes on his wrist, the shot has failed. The sheath
NEVER opens; no tool, blade or weapon appears in any frame. The white
figure never enters the frame and nothing off screen is shown. Her
grip and his wrist keep clear boundaries — gloves never merge.
Neither speaks: mouths closed, no lip movement. Orange stays on the
woman, teal on the man; the 13 cm difference holds; scars stay LEFT
eyebrow / RIGHT cheekbone; both faces keep identical bone structure —
no morphing, no face swap. Every helmet stays ON and sealed; visors
stay clear, uncoated glass — no tint, no mirror coating, no
reflection that hides what is behind them. Exactly two figures — no
third, nobody in the background. Camera locked: no cuts, no
transitions, no shake, no zoom. No bloom, no glow filter, no lens
flare. No readable text or digits; no captions, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 43 — "DO NOT"

`7:00 – 7:10` · 85mm · kadro B · fixed lockoff · **B yolu (retime)**
📎 **REFERANS:** R3 (BEKÇİ master)

_"DO NOT. DO NOT."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  ⭐ ÇEHOV 1 ATEŞLENİYOR: filmin ilk Bekçi repliği. S8'deki anonsun
     kelimeleri — Bekçi konuşmuyor, elindeki tek kayıttan kelime
     kesip yapıştırıyor. Tehdit değil, UYARI DENEMESİ.
  ⭐ KARAR 1: ses post'ta; kadrajda repliği temsil eden tek hareket
     başın bir kez çok yavaş öne eğilmesi. "speak" yazılmaz.
  ⭐ B yolu güvenli: Bekçi neredeyse hareketsiz; 0.8× retime onun
     zaten akışkan hareket dilini derinleştirir.
```

### 📸 IMAGE PROMPT

```
SCENE:
The tall sealed white figure alone, filling the frame chest-up —
patient, weary, unreadable behind its single dark visor.

ENVIRONMENT:
The wreck-field clearing, compressed by the long lens into soft
bands: blurred bone-grey stone twins and a weathered hull behind,
pale grey-green sky above, soft orange 4400K daylight from frame
LEFT. Fine dust out of focus at the frame bottom.

SUBJECT:
A tall sealed figure in an unfamiliar pressure suit, chest-up,
nearly frontal. Its suit is seamless and flawlessly pearl-white —
no wear, no dust, no panel lines, no seams, no markings, and no
strap, harness or hose across chest or shoulders. The shoulders
follow human skeletal proportions; the visible upper arms run long.
The helmet is smooth and featureless, and where a visor would be
there is NO OPENING AND NO CAVITY: the area is FILLED FLUSH with
one solid matte plate of dark grey-green, nearly black, running
unbroken from cheek to cheek and continuous with the shell. It is
not glass and not a window: there is no inside to it, only a faint
warm sheen on its surface. The figure stands utterly still, weight
even, posture calm — it reads as weary, not threatening.

CAMERA:
Shot on an 85mm lens from a fixed position three meters away,
f/2.8, slightly below its eye line so the 2.10-meter height
presses gently on the frame, shallow depth of field — figure
sharp, world soft.

LIGHTING:
Soft orange 4400K daylight from frame LEFT: a clean subtle specular
gradient across the pearl shell, bright but never glowing; the dark
plate swallows the light it receives.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one
figure. The visor area is solid filled stone-flat plate — never
glass, never a window, never transparent, never mirrored, never
white; no recess or hollow of any depth appears there, and no face,
eyes, skull, silhouette, reflection of a person or light ever forms
in it. The suit stays clean, seamless, unmarked — no dust, no wear,
no panel lines, no insignia, no straps or hoses across the chest or
shoulders. Rigid fixed anatomy — no morphing, no shape-shifting. No
mouth, no speech movement anywhere. No bloom, no glow filter, no
lens flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, fixed lockoff three meters away, no
cuts, no camera movement:

SETUP: the camera is locked off slightly below the figure's eye
line, f/2.8, chest-up framing, shallow depth of field. It never
moves for the whole ten seconds. The scene is generated SILENT;
all audio is added later.
FRAME: a tall sealed figure in an unfamiliar pressure suit,
chest-up, nearly frontal — seamless flawless pearl-white shell, no
dust, no markings, no straps or hoses across chest or shoulders;
long-boned shoulders on human proportions; smooth featureless
helmet whose visor area is FILLED FLUSH with one solid matte plate
of dark grey-green, nearly black — no opening, no cavity, nothing
inside it. Behind it, the wreck field compressed to soft grey
bands; soft orange 4400K daylight from frame LEFT; pale grey-green
sky.

0s — Absolute stillness. The pearl shell carries its clean warm
gradient; the dark plate gives nothing back.
3s — The helmet begins to tip forward — one impossibly slow,
continuous bow, a few degrees over several full seconds, the
motion flowing without any start or stop.
6s — The bow reaches its lowest point and holds there: the dark
visor angled at the unseen humans below the frame line — the
posture of a warning given gently.
8s — Just as slowly, the helmet begins to rise again, the same
liquid continuity in reverse.
10s — The figure is level and still once more, exactly as it
began. No cuts.

The head bow is the ONLY motion in the shot — one slow descent,
one hold, one rise, all a single continuous flow; no other limb
moves; the figure never steps, never gestures, never trembles. Its
anatomy stays rigid and fixed — same height, same silhouette, no
morphing. The visor area stays a solid filled dark plate for every
frame — never glass, never white, never mirrored; no recess opens
there and no face, eyes, skull or reflected person ever forms in
it. The suit stays flawlessly clean, seamless, strapless and
hoseless. The background never moves. Exactly one figure.
Camera locked: no cuts, no transitions, no shake, no push-in. No
bloom, no glow filter, no lens flare. No readable text or digits;
no captions, no subtitles, no HUD, no watermark. Photorealistic,
35mm anamorphic film grain.
```

---

## 🎬 SAHNE 44 — ÇİZİM

`7:10 – 7:20` · 50mm · kadro 1 · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 (KAPTAN master)

_"Gemi. Ok. Yukarı."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: insan tarafı dili çözmeye çalışıyor — resim, sesin
  yapamadığını yapıyor.
  ⭐ Çizim envanteri KİLİTLİ: kutu gövdeli gemi hattı + tek çizgi +
     çizginin ucunda YUKARI bakan kama ucu. Harf/rakam YOK — bu bir
     resimdir, yazı değil [Ders 13 uyumu; "arrow symbol" yerine
     "line with a wedge tip" yazıldı].
  ⚠️ Ders 11: parmak toza 5 mm gömülür — iz bırakır, zemine
     KAYNAMAZ. Çizgiler V-profilli oluk olarak tarif edildi.
```

### 📸 IMAGE PROMPT

```
SCENE:
A woman pilot crouches in the dust, drawing with one gloved finger:
the outline of a ship, and a line whose wedge tip points at the
sky.

ENVIRONMENT:
Open dust floor at the wreck-field clearing, soft orange 4400K
daylight from frame LEFT, long soft-edged shadows, pale grey-green
sky low beyond. Blurred grey stone forms close the background; the
white figure is out of frame.

SUBJECT:
A 41-year-old woman pilot crouched on one knee, seen three-quarter
from her right: light olive skin, sharp jawline, dark grey-green
eyes down on her work, a fine faded white scar splitting her LEFT
eyebrow, dark brown hair in a tight low bun behind a fully
transparent visor. Dark grey-blue pressure suit with ORANGE worn
reinforcement, right glove with a visible detachable wrist ring.
Her index finger is buried half a knuckle in the dust, mid-stroke.
Before her, drawn as clean V-profile grooves: the simple boxy
outline of a small cargo ship, and beside it a straight groove
ending in a wedge tip that points UP toward the sky. The grooves
hold crisp edges in the fine dust.

CAMERA:
Shot on a 50mm lens from a fixed position two meters away, f/4,
low — thirty centimeters above the ground — so both the drawing
and her lowered face read together. True human scale.

LIGHTING:
Soft orange daylight, 4400K, raking from frame LEFT: the grooves
throw thin sharp shadow lines that make the drawing legible; warm
key on her visor and glove.

NEGATIVE:
THE ONLY EVENT OF THIS SHOT IS THE DRAWING: a boxy ship outline and a
straight line whose wedge tip points UP. If both are not legible in
the dust, the shot has failed.
Single unbroken take, no cuts, no camera shake. Exactly one figure —
nobody in the background. Her face keeps identical bone structure —
no morphing; the scar stays on her LEFT eyebrow. Reinforcement stays
ORANGE. Her helmet is ON and sealed — no bare head, no bare hand;
the visor stays clear uncoated glass, no tint, no mirror coating.
The drawing contains ONLY the ship outline and the wedge-tipped line
— no letters, no digits, no other marks. Her finger presses INTO dust,
never merging with solid ground; the grooves stay crisp, never
smoothing on their own. No bloom, no glow filter, no lens flare. No
captions, no HUD, no watermark. Photorealistic, 35mm anamorphic film
grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff two meters away, thirty
centimeters above the ground, no cuts, no camera movement:

SETUP: the camera is locked off low over the dust floor, f/4, a
crouched woman on the right of frame, her drawing space on the
left. It never moves for the whole ten seconds.
FRAME: soft orange 4400K daylight raking from frame LEFT, long thin
shadows, blurred grey stone forms behind. A 41-year-old woman pilot
on one knee — light olive skin, faded scar through her LEFT
eyebrow, dark brown low bun behind a transparent visor, ORANGE worn
reinforcement on a dark grey-blue suit, right glove with a
detachable wrist ring. The dust before her is smooth and unmarked.

0s — Her finger sinks half a knuckle into the dust and begins the
first stroke: one long clean groove, drawn slowly, dust crumbling
at its edges and settling at once.
3s — Three more strokes close the shape: the simple boxy outline of
a small cargo ship, crisp V-profile grooves throwing thin shadows.
6s — Beside it she draws one straight groove and finishes it with
two short angled strokes — a wedge tip pointing UP at the sky. She
does not decorate; the drawing is a sentence.
8s — She pulls her hand back, rises off the knee into a crouch and
goes still, eyes lifting from the drawing toward the unseen figure
beyond the frame.
10s — Hold: the woman waiting, the ship and the up-pointing wedge
sharp in the raking light. No cuts.

THE ONLY EVENT OF THIS SHOT IS THE DRAWING APPEARING — if the ship
outline and the UP-pointing wedge are not legible in the final frame,
the shot has failed. The drawing contains only those two marks — no
letters, no digits, no circles, no other symbols ever appear. The
grooves stay exactly as drawn: they never deepen, smooth over, or move
on their own in this scene. Her finger presses into loose dust only —
never merging with solid ground; displaced grains fall and settle at
once, never hover, never pour or stream. Her face keeps identical bone
structure — no morphing; the scar stays LEFT; reinforcement stays
ORANGE. Her helmet stays ON and sealed; the visor stays clear,
uncoated glass — no tint, no mirror coating, no reflection that hides
what is behind it. She never speaks. Exactly one figure — nobody in
the background. Camera locked: no cuts, no transitions, no shake, no
zoom. No bloom, no glow filter, no lens flare. No captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 45 — ZEMİN CEVAP VERİYOR

`7:20 – 7:30` · 100mm · kadro B · fixed lockoff · **A yolu**
📎 **REFERANS:** R3 (BEKÇİ — kadrajda üç parmaklı el) + S44 karesi (çizim devamlılığı)

_"Cevap zeminden geliyor."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: ⭐ Bekçi konuşmuyor — GEZEGEN konuşuyor. Ve cevap "yukarı"
  değil: kama ucu AŞAĞI bakıyor. Burada kalacaksınız.
  ⭐ KARAR 2 sahnesi: zemin tepkisi kum tanesi ölçeğinde — çizim
     taneleri akarak silinir, birkaç santim ötede taneler akarak
     YENİDEN dizilir. Zemin yarılmaz, ışımaz.
  🎞️ END FRAME alır (yeni çizim oluşmuş, kama ucu aşağıda).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
A three-fingered white glove rests flat on the dust beside a
finger-drawn ship — the moment before the ground itself answers.

ENVIRONMENT:
The dust floor of the clearing in soft orange daylight, 4400K,
from frame LEFT, long thin shadows. Sharp in frame: the finger-
drawn V-groove drawing — a boxy ship outline and a straight groove
ending in a wedge tip pointing UP. Fine settled dust all around;
hairline fracture lines under it; blurred grey forms far behind.

SUBJECT:
From frame RIGHT, the lower arm and hand of a tall sealed figure:
a flawlessly pearl-white, seamless suit arm, unusually long, its
glove carrying THREE FINGERS and a thumb, pressed flat and calm on
the dust half a meter from the drawing. The pearl surface is
dustless and unmarked even against the grey floor. Nothing else of
the figure is in frame. The drawing's grooves hold crisp edges;
nothing has moved yet.

CAMERA:
Shot on a 100mm lens from a fixed position one point five meters
away, f/4, thirty centimeters above the ground, square to the
drawing — glove at frame right, ship and wedge line centered. True
scale: the glove reads larger than a human hand.

LIGHTING:
Soft orange daylight, 4400K, raking from frame LEFT: the grooves
throw thin crisp shadows; the pearl glove takes a clean subtle
specular, bright but never glowing.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one partial
figure — the white arm and glove only; no human hand, no second
figure. The glove has exactly three fingers and a thumb, fixed
anatomy. The ground is still: no grains moving, no veins glowing,
no cracks opening. The drawing holds only the ship outline and the
wedge-tipped line — no letters, no digits. No bloom, no glow
filter, no lens flare. No captions, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
The answer, written by the ground: the old drawing gone smooth, and
a few centimeters away the same ship redrawn by the dust itself —
its wedge tip now pointing DOWN.

ENVIRONMENT:
The same dust floor, same soft orange 4400K raking light from
frame LEFT, same thin long shadows. Where the woman's drawing was,
the dust now lies smooth, level and unmarked, carrying only a very
faint fine-grained texture where the grooves used to run — no
liquid, no wetness, no water anywhere in this world. A hand-span
to the LEFT, a new drawing sits in the
dust: the same boxy ship outline, the same straight line — but its
wedge tip points DOWN into the ground.

SUBJECT:
The three-fingered pearl-white glove still rests flat on the dust
at frame RIGHT, unmoved, dustless, seamless. The new grooves match
the old drawing's scale and style exactly, but their edges are
finer — as if settled into place grain by grain rather than
dragged. Between old site and new drawing, the dust shows a faint,
already-still trail of rearranged grains. Nothing else has
changed; the fracture lines beneath run exactly as before.

CAMERA:
Shot on the same 100mm lens from the same fixed position, thirty
centimeters above the ground, framing unchanged — only the dust
has moved.

LIGHTING:
Unchanged: soft orange 4400K raking key; the new grooves throw the
same thin crisp shadows the old ones did.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one partial
figure — the unmoved white arm and glove. The new drawing holds
only the ship outline and the DOWN-pointing wedge line — no
letters, no digits. The ground is whole: no cracks, no openings,
no glow, no visible veins; grains at rest. No bloom, no glow
filter, no lens flare. No captions, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 100mm, fixed lockoff one point five meters
away, thirty centimeters above the ground, no cuts, no camera
movement:

SETUP: the camera is locked off square to a finger-drawn dust
drawing — a boxy ship outline and a wedge-tipped line pointing UP
— with a three-fingered pearl-white glove resting flat on the dust
at frame RIGHT. It never moves for the whole ten seconds.
FRAME: soft orange 4400K daylight raking from frame LEFT, thin
crisp groove shadows, fine settled dust, blurred grey forms far
behind. The white suit arm is seamless, dustless, unmarked.

0s — Stillness. The glove rests; the drawing holds its crisp
edges.
2s — The dust inside the drawing begins to move at grain scale:
the groove edges crumble inward, individual grains sliding a few
millimeters down the groove wall and stopping, and the ship
outline softens.
4s — The old drawing erases itself completely — the surface
settling smooth and level, no grain travelling further than the
groove it filled. The glove has not moved at all.
6s — A hand-span to the LEFT, grains begin to slide apart in clean
lines: the same boxy ship outline redraws itself stroke-width by
stroke-width, fine-edged, exact.
8s — The straight line forms last — and its wedge tip assembles
pointing DOWN into the ground. The grain-flow stops.
10s — Total stillness: old site smooth, new answer sharp, the
white glove flat and patient on the dust. No cuts.

THE ONLY EVENT OF THIS SHOT IS THE ANSWER: the old drawing erasing
itself and the same ship redrawing itself a hand-span away with its
wedge tip pointing DOWN. If the new drawing does not finish, or its
wedge points anywhere but DOWN, the shot has failed.
All ground motion happens at sand-grain scale on the surface ONLY,
and it is dry: single grains slide a few millimeters and stop. No
grain travels further than groove width, nothing rises above groove
depth, nothing pours, streams or cascades, nothing hovers in the
air, and every grain is at rest by the tenth second. There is no water, no wetness, no liquid anywhere. The
ground never cracks, never opens, never bulges, never
glows; no veins appear; no light comes from below. The white glove
NEVER moves — same position, three fingers and a thumb, dustless,
for every frame. The finished drawing contains only the ship
outline and the DOWN-pointing wedge line — no letters, no digits.
Exactly one partial figure. Camera locked: no cuts, no
transitions, no shake, no zoom. No bloom, no glow filter, no lens
flare. No captions, no HUD, no watermark. Photorealistic, 35mm
anamorphic film grain.
```

---

## 🎬 SAHNE 46 — İŞARET

`7:30 – 7:40` · 50mm · kadro 1+B · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R3 (Kaptan + Bekçi aynı karede)

_"Uzun kol kalkıyor."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: davet mi, sevk mi — belli değil. Bekçi ufuktaki tek dik
  çizgiyi gösterir ve arkasına bakmadan yürümeye başlar.
  ⭐ Ufukta KULE: S1'in dik çizgisi — burada hâlâ ölçeksiz ince
     beyaz çizgi olarak yazılır; ölçek S48'de gelir.
  ⭐ Bekçi hareket dili: kol kalkışı ve ilk adımlar TEK akış.
  ⚠️ İnsan kadraj kenarında izleyici konumunda; konuşma yok.
```

### 📸 IMAGE PROMPT

```
SCENE:
The tall white figure lifts its long arm and points at a thin
vertical white line standing on the far horizon.

ENVIRONMENT:
The open plain past the wreck field, soft orange 4400K daylight
from frame LEFT, pale grey-green sky, faint daytime moon. On the
far horizon, dead ahead, a single thin, perfectly vertical white
line rises from the ground — scale unreadable, no landmark near
it. Fine dust, long soft shadows.

SUBJECT:
CENTER: a tall sealed figure, exactly 2.10 m, in a seamless,
flawlessly pearl-white pressure suit, seen three-quarter from
behind — long arms, three-fingered gloves, smooth featureless
helmet. Its RIGHT arm is raised straight and level, aimed exactly
at the distant line; the
gesture is calm and absolute. Its BACK IS FLAT and bare — no
backpack, no hoses, no protrusion. At the extreme LEFT edge of
frame, out of focus and occupying less than a fifth of the frame
width: the shoulder and helmet rim of a 41-year-old woman pilot,
1.68 m — ORANGE worn reinforcement, sealed transparent visor —
watching the pointing arm. Her full body is not in frame.

CAMERA:
Shot on a 50mm lens from a fixed position five meters behind and
beside the pair, at chest height — the white figure center, the
pointing arm, the horizon line and the watching woman all in
frame. Deep focus; true scale.

LIGHTING:
Soft orange 4400K daylight from frame LEFT: clean specular along
the raised pearl arm; the distant line pale and flat, lit by the
same sun, emitting nothing.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly two
figures — one white, one human; no third, nobody else on the plain
or horizon. The white figure's anatomy stays rigid — 2.10 m, three
fingers, long arms, flat back with no backpack or hoses, no
morphing; where the visor shows it is a solid filled dark plate,
never white, nothing behind it. The horizon line
is a plain straight vertical form, matte and still — never
glowing, never moving. It is NOT a rocket: no cylinder, no
nosecone, no fins, no launch pad, no gantry, no exhaust.
Reinforcement stays ORANGE on the woman; her helmet stays ON and
sealed, visor clear uncoated glass. No bloom, no glow filter, no
lens flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 50mm, fixed lockoff five meters behind the
pair, no cuts, no camera movement:

SETUP: the camera is locked off at chest height, the tall white
figure center frame from three-quarter behind, a human woman
partial at the left edge, a thin vertical white line on the far
horizon. It never moves for the whole ten seconds.
FRAME: open plain in soft orange 4400K daylight from frame LEFT,
pale grey-green sky, faint daytime moon, long soft shadows. The
white figure: exactly 2.10 m, seamless pearl-white suit, dustless,
long arms with three-fingered gloves, smooth featureless helmet.
The woman: 1.68 m, ORANGE worn reinforcement, dark grey-blue suit,
transparent visor.

0s — The white figure stands still, arms at its sides, facing the
horizon line.
2s — Its RIGHT arm begins to rise — one slow, continuous flow from
hip to full extension, no stops along the way — until the long arm
aims exactly at the distant vertical line.
5s — The arm holds its point for a long beat. The woman's helmet
turns from the arm to the horizon and back.
7s — Without lowering hurry, the arm descends in the same liquid
motion — and before it settles, the figure is already walking
toward the line: first step flowing out of the gesture, unhurried,
never looking back.
10s — Second and third steps carry it a meter forward; the woman
still stands at frame edge, watching. No cuts.

Every motion of the white figure is one continuous flow — arm rise,
hold, descent and first steps chain without a single stop or jerk; its
pace is slow and even; it NEVER looks back. Its anatomy stays rigid:
2.10 m, same silhouette, three fingers, long arms, flat back with no
backpack and no hoses, no morphing; the suit stays dustless; where the
visor shows it is a solid filled dark grey-green plate — never white,
never mirrored, nothing behind it. The horizon line is a plain
straight vertical form that never moves, never glows, never thickens,
and is NOT a rocket: no cylinder, no nosecone, no fins, no capsule, no
launch pad, no gantry, no exhaust. The woman stays in place this scene
— she does not follow yet, and only her out-of-focus shoulder and
helmet rim are in frame. Exactly two figures — no third, nobody on the
plain or the horizon. Camera locked: no cuts, no transitions, no
shake, no zoom. No bloom, no glow filter, no lens flare. No readable
text or digits; no captions, no HUD, no watermark. Her helmet stays ON
and sealed; her visor stays clear, uncoated glass — no tint, no mirror
coating. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 47 — 🔥 VİRAL #2: ZEMİN NEFESİ

`7:40 – 7:50` · 100mm · kadro B · yavaş lateral track · **A yolu**
📎 **REFERANS:** R3 (BEKÇİ — kadrajda bacaklar ve botlar)

_"Yürüyen bir yara izi."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: yürüyüşe eşlik eden
  yavaş yanal kaydırma. Kadraj: diz altı + zemin.
  İŞLEV: gezegen canlı bir doku gibi davranıyor — ve bu figür ondan
  kopyalanamayacak kadar akıcı hareket ediyor.
  ⭐ KARAR 2 sahnesi: bastığı yer hafifçe KABARIR, ayak kalkınca
     yavaşça GERİ İNER. Ayak izi kalmaz — nefes kalır.
  ⭐ Kabarma bot tabanı çevresinde 2-3 cm'lik yumuşak bir yastık;
     asla yarılma, asla ışıma.
  🎞️ END FRAME alır (kaydırma ilerlemiş, taze nefes izi ortada).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
Knee-down view behind the walking white figure: where its boot
presses, the ground swells softly around the sole — the planet
breathing under each step.

ENVIRONMENT:
The open dust plain in soft orange daylight, 4400K, from frame
LEFT, long thin shadows, hairline fracture lines under fine grey
dust. One faint fracture line crosses the lower corner. The frame
holds only ground and legs — no horizon, no sky.

SUBJECT:
The lower legs and boots of a tall sealed figure walking away from
the lens: seamless, flawlessly pearl-white suit legs, dustless
even at the boot rims, mid-stride — the LEFT boot planted, the
RIGHT boot lifting. Around the planted sole, the dust has risen in
a soft, smooth swell two to three centimeters high, hugging the
boot like a cushion. Behind the walker, at the spot of the last
stride, a fading swell is sinking back level — no print left in
it, only a soft round ghost.

CAMERA:
Shot on a 100mm lens from a fixed distance of two meters behind
and low, forty centimeters above the ground, at the start of a
slow lateral-following track matching the walk. Shallow-deep
split: boots and swells sharp.

LIGHTING:
Soft orange daylight, 4400K, raking from frame LEFT — the swells
read as soft-shadowed mounds; the pearl legs carry a clean subtle
specular, never a glow.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one
partial figure — white legs and boots only. The swells are smooth
dust mounds: no cracks, no openings, no glow, no veins, no
particles floating. Boot prints NEVER remain — the ground returns
level. The suit stays dustless. No bloom, no glow filter, no lens
flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
Three strides later: the walking legs near the frame edge, and
down the walked line, a row of soft round ghosts in the dust —
each one sinking, none of them a footprint.

ENVIRONMENT:
The same dust plain, same soft orange 4400K raking light and long
thin shadows, the framing slid forward with the walk. The walked
line crosses the frame diagonally: four fading swell-ghosts at
different heights of collapse — the oldest almost level, the
newest still a clear soft mound.

SUBJECT:
The pearl-white legs and boots now at the RIGHT edge of frame,
mid-stride, still dustless, still unhurried. Under the currently
planted boot, the fresh swell hugs the sole. The sequence of
ghosts behind tells the whole rule in one look: press, swell,
lift, sink, level — breath instead of footprints. The dust
everywhere else lies untouched, fracture lines running beneath;
no other mark disturbs the floor. The pearl shell of the suit
legs carries the same clean subtle specular as before — bright in
the raking light, never glowing, not one grain of dust on it.

CAMERA:
Shot on the same 100mm lens at the same two-meter distance and
forty-centimeter height — the end of one slow lateral-following
track, framing shifted one stride-length forward.

LIGHTING:
Unchanged soft orange 4400K raking key; each ghost throws a
progressively softer shadow as it sinks.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one
partial figure. The ghosts are smooth sinking mounds — never
prints, never cracks, never glowing rings. The ground stays whole;
nothing opens, nothing shows veins. The suit stays dustless. No
bloom, no glow filter, no lens flare. No readable text or digits;
no captions, no HUD, no watermark. Photorealistic, 35mm anamorphic
film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 100mm, one slow lateral-following track two
meters behind the walking figure, forty centimeters above the
ground, no cuts:

SETUP: the camera follows at exactly the walker's slow pace, low
and level, keeping the legs in the same part of frame — one
constant speed, no bob, no shake, no push-in.
FRAME: fine grey dust over dark basalt in soft orange 4400K
raking light from frame LEFT, long thin shadows, no sky. The lower
legs and boots of a tall sealed figure walking away: seamless
pearl-white, dustless, unhurried, each stride slow and flowing
without a break. The world here is bone dry — no water, no wetness,
no liquid of any kind.

0s — The LEFT boot presses down; around its sole the dust rises
into a soft smooth swell, two to three centimeters, hugging the
boot like a slow cushion.
3s — The boot lifts; the swell begins to sink back — evenly, grain
by grain, reaching level within about two seconds, leaving NO
print, only a soft round ghost losing height.
5s — The RIGHT boot lands a stride ahead and the ground answers
again: the same soft swell, the same patient hug. Behind, the
first ghost is almost level.
8s — Stride follows stride; the walked line now carries a row of
ghosts at different stages of sinking — a breath moving through
the ground, step by step.
10s — The newest swell holds under the planted boot as the frame
ends. No cuts.

THE ONLY EVENT OF THIS SHOT IS THE GROUND ANSWERING EACH STEP: a
soft swell rising around the planted sole and sinking back level
after the boot lifts, leaving no print. If no swell rises, or if a
footprint remains, the shot has failed.
All ground motion is smooth, slow, dry and local: swells rise and
sink around the soles only, never higher than three centimeters —
the ground never cracks, never opens, never glows, never shows
veins; no grain pours, streams or cascades; no dust floats or
swirls; no print, tread mark or hole ever remains. The walk is one
continuous unbroken rhythm — never stopping, never hurrying. The
pearl legs stay dustless and rigid in form — no morphing; no
backpack, hose or strap enters frame. The following track holds one
constant speed — no bob, no handheld feel. The frame never shows
the horizon or the sky; the composition stays knee-down for every
frame — if the horizon appears, the shot is wrong. Exactly one
partial figure — no human boots, no second walker. No cuts, no
transitions, no shake, no zoom. No bloom, no glow filter, no lens
flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 48 — TAKİP

`7:50 – 8:00` · 32mm · kadro 2+B · fixed lockoff · **A yolu**
📎 **REFERANS:** R1 + R2 + R3 (ÜÇ FİGÜR yürüyüşte; kule promptta tarif edilir)

_"Dört yüz metre."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit; üçlü kadrajı geçer.
  İŞLEV: ⭐ S1'İN CEVABI — hook'taki dik çizgi buydu. Kule ilk kez
  ÖLÇEKLE görünür: 400 m, kusursuz beyaz, dikişsiz, hafif konik.
  ⚠️ ÜÇ FİGÜR SAHNESİ 2/5. Bekçi önde, insanlar birkaç adım
     geride — sıra düzeni karışmayı azaltır.
  ⭐ Kule IŞIK YAYMAZ; gündüz ışığında mat beyaz. Tepesi kadraj
     DIŞINDA biter — yükseklik hissi kesme olmadan kurulur.
```

### 📸 IMAGE PROMPT

```
SCENE:
Three figures walk toward a tower that finally has scale: a
seamless white column four hundred meters tall, the only vertical
line in the world.

ENVIRONMENT:
Open basalt plain, soft orange 4400K daylight from frame LEFT,
pale grey-green sky, faint daytime moon. Dominating the upper
frame ahead: a colossal tower — perfectly smooth, matte white,
seamless, very slightly conical, rising from bare ground and
leaving the TOP of frame before it ends. Around its base,
kilometers off, the plain is empty.

SUBJECT:
Three figures small on the plain, walking away from the lens in
loose file, all three seen from BEHIND. LEADING: a tall sealed
figure, exactly 2.10 m — a full head taller than the man behind it
— seamless pearl-white suit, long arms, smooth helmet, its white
subtly warmer than the tower's flat matte; its BACK COMPLETELY
FLAT AND BARE, no backpack, no hoses, no protrusion. A few steps
behind, side by side: a 41-year-old woman pilot, 1.68 m, ORANGE
worn reinforcement; and a 33-year-old man, 1.81 m,
broad-shouldered, TEAL GREEN reinforcement, with an oversized back
tool module — the ONLY back-mounted equipment in frame is his.
Three shadow lines walk with them.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position ten meters
behind the file, at chest height, tilted slightly UP so the tower
crushes the sky. Physically accurate perspective: 400 m against
2 m figures.

LIGHTING:
Soft orange 4400K daylight from frame LEFT: the tower's west face
holds a soft warm gradient, its east face falls to cool shadow —
reflected light only, never emitted.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly three
figures — no fourth, nobody else on the plain. The tower is a
seamless matte white column: NO WINDOWS AT ALL, lit or unlit, no
glass, no ports, no openings of any kind, no doors, no hatches, no
vents, no markings, no lights, no glow. NOT a rocket: no cylinder,
no nosecone, no fins, no gantry, no exhaust. Orange on the woman,
teal on the man; the white figure stays dustless, rigid, FLAT BACK
with no backpack or hoses — only the man carries a back module.
Every human helmet is ON and sealed. No bloom, no glow
filter, no lens flare. No readable text or digits; no captions, no
HUD, no watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, fixed lockoff ten meters
behind the walking file, no cuts, no camera movement:

SETUP: the camera is locked off at chest height, tilted slightly
up, framing three walking figures and the colossal tower they walk
toward. It never moves; the file recedes inside the static frame.
FRAME: open basalt plain, soft orange 4400K daylight from frame
LEFT, pale grey-green sky, faint daytime moon. The tower: a plain
matte white column, seamless, very slightly conical, four hundred
meters, leaving the top of frame — no door, no window of any kind,
no opening, no marking; not a rocket. LEADING the file: a tall
sealed figure, 2.10 m, pearl-white seamless suit, long arms, smooth
featureless helmet, FLAT BARE BACK. BEHIND: the woman, 1.68 m,
ORANGE worn reinforcement; the man, 1.81 m, broad-shouldered, TEAL
GREEN reinforcement, oversized back module — the only back-mounted
equipment in frame.

0s — The three walk in loose file, the white figure's liquid gait
setting the pace, the humans' steps shorter and harder behind it.
3s — The file recedes steadily; the tower's base line stays fixed
in frame, its face gradient shifting almost imperceptibly as the
sun climbs.
6s — The woman's helmet tilts back as she walks — following the
white face up and up until the frame's top edge cuts it — then
levels again. The walk never breaks.
8s — Three shadows stretch long to frame right, keeping pace; the
figures grow smaller against the enormous base.
10s — The file is deep in frame now, three small shapes against
four hundred meters of white. Hold to the end. No cuts.

The tower never changes: no lights, no seams, no door, no window
lit or unlit, no opening, no marking ever appears; it emits nothing
and never moves; it stays a plain column and never becomes a rocket
— no nosecone, no fins, no gantry, no exhaust. The three figures
never stop or turn back; the white leader never looks behind.
Orange stays on the woman, teal on the man; the 13 cm difference
holds; no morphing; the white figure keeps rigid 2.10 m anatomy, a
dustless shell and a FLAT BARE BACK — no backpack, hose or strap
grows on it at any second, while the man keeps his. Every human
helmet stays ON and sealed. Dust rises low at boot falls and
settles at once. Exactly three figures — no fourth, no duplicate,
nobody in the background. Camera locked: no cuts, no transitions,
no shake, no tilt change, no zoom. No bloom, no glow filter, no
lens flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 49 — ÖLÜ HALKA

`8:00 – 8:10` · 32mm · kadro 2 · yavaş push-in · **A yolu**
📎 **REFERANS:** R1 + R2 (iki insan sınırda; cilalı zemin = R3 plaka zemini)

_"Bir adımda değişiyor."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. TEK hareket: sınıra doğru yavaş
  push-in.
  ⭐ ÇEHOV 6 BURADA KURULUYOR: bu çizginin içinde kopyalama YOK.
     Ateşleme S64'te — ölü halka bir sığınak değil, bir mezar.
  ⭐ KARAR 3: sınır bıçak keskinliğinde — dokulu tozlu bazalt bir
     çizgide biter, cilalı honlanmış taş başlar. Toz bile sınırı
     geçmez. Degrade YASAK.
  ⚠️ KADRO BÜTÇESİ: `2` işaretli 23 sahnenin 14.'sü.
  🎞️ END FRAME alır (push-in sınıra varmış, iki doku tek karede).
```

### 📸 IMAGE PROMPT — START FRAME

```
SCENE:
Two crew stand before a line drawn in the world: on their side,
dusty broken basalt — beyond it, polished bare stone where even
the dust refuses to cross.

ENVIRONMENT:
The tower's base region, soft orange 4400K daylight from frame
LEFT. Crossing the middle distance, a perfectly sharp boundary
arcs through the plain: NEAR side, textured basalt under fine grey
dust with hairline fractures; FAR side, smooth honed stone —
dustless, seamless, faintly reflective, running unbroken toward the
colossal matte white tower whose base rises at the top of frame.

SUBJECT:
Exactly two figures seen from behind at the near edge of frame,
stopped a stride short of the line. LEFT: a 41-year-old woman
pilot, 1.68 m, ORANGE worn reinforcement on a dark grey-blue suit,
dark brown low bun behind a transparent visor. RIGHT: a
33-year-old man, 1.81 m, broad-shouldered, TEAL GREEN
reinforcement, oversized back tool module, helmet 13 cm higher.
Their long shadows reach the boundary — and continue across it,
the only things that cross freely.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position six meters
behind them at chest height, at the start of a slow push-in toward
the line. Deep focus; true scale.

LIGHTING:
Soft orange daylight, 4400K, from frame LEFT: matte and grainy on
the dusty side, a clean low sheen on the polished side — reflected
light only, no glow.

NEGATIVE:
THE ONLY EVENT OF THIS SHOT IS THE LINE: one continuous knife-sharp
boundary across the frame — dust on the near side, polished bare
stone on the far side. If it is not a single clean edge, the shot
has failed.
Single unbroken take, no cuts, no camera shake. Exactly two figures —
no third, nobody in the background. The boundary stays knife-sharp —
no gradient, no blend, no transition band, no glowing edge. Nothing
stands on or above the line: no wall, no pane, no glass, no barrier,
no dome — only two kinds of ground meeting. The polished side is bare
stone — no patterns, no veins, no light from below. Orange stays on
the woman, teal on the man; no morphing. Every helmet is ON and
sealed; visors stay clear uncoated glass. No bloom, no glow filter,
no lens flare. No readable text or digits; no captions, no HUD, no
watermark. Photorealistic, 35mm anamorphic film grain.
```

### 📸 IMAGE PROMPT — END FRAME (10. saniye kadrajı)

```
SCENE:
The boundary fills the frame at close range: one image, two
worlds — grain and dust ending in a single clean line against
polished stone.

ENVIRONMENT:
Ground-level detail at the dead ring's edge, soft orange 4400K
raking light from frame LEFT. The lower half of frame: textured
basalt, fine grey dust, hairline fractures, a few small pebbles —
alive with grain. The upper half: honed, polished bare stone,
dustless and seamless, carrying a soft warm sheen and the faint
cool reflection of the sky. Between them, one continuous
knife-sharp line, arcing gently, without a single blur or step.

SUBJECT:
The two crew now stand at the very line, their boots at the
bottom frame edge on the dusty side — the woman's boot with its
dark grey-blue shin and ORANGE knee reinforcement, the man's
larger boot with TEAL GREEN. A little windblown dust lies banked
against the boundary in a thin low drift and simply stops there,
its far edge as straight as the line itself — not one grain rests
on the polished side. Nothing stands between the two surfaces: the
air above the line is completely empty, with no wall, no pane, no
glass, no barrier and no dome of any kind.

CAMERA:
Shot on the same 32mm anamorphic lens, now one meter from the
line at waist height, angled slightly down — the end of one slow
push-in. The boundary crosses the frame as a clean diagonal.

LIGHTING:
Unchanged: soft orange 4400K raking key; dust matte, polish
sheened; the shadow of the two figures lies across both surfaces.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Two partial figures —
boots and shins only at frame bottom. The line stays knife-sharp: no
gradient, no melt, no glow; not one dust grain on the polished side.
The polished stone shows no veins, no patterns, no light. Orange and
teal stay on their owners. No bloom, no glow filter, no lens flare. No
readable text or digits; no captions, no HUD, no watermark. Exactly
two figures in frame — no duplicates, no third person. Photorealistic,
35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 32mm anamorphic, one slow push-in from six
meters to one meter, no cuts:

SETUP: the camera creeps forward at a constant slow rate from
behind two standing figures toward a sharp boundary in the ground,
dropping gently from chest height to waist height as it closes.
No pan, no shake, no speed change.
FRAME: soft orange 4400K daylight from frame LEFT. Near side:
textured basalt under fine grey dust. Far side: polished, honed
bare stone, dustless, running to the base of a colossal matte
white seamless tower at frame top. Two suited figures from
behind: the woman, 1.68 m, ORANGE worn reinforcement; the man,
1.81 m, broad-shouldered, TEAL GREEN reinforcement, oversized back
module.

0s — They stand a stride short of the line. Their shadows cross
it; nothing else does.
2s — The push-in begins. The woman extends one boot and sets it
down ON the line — half on dust, half on polish — testing.
5s — She commits her weight and steps fully onto the polished
side; the boot lands with a harder, cleaner contact. The man
follows one step behind. No dust comes with them — what their
boots carry falls at the line.
7s — The camera closes on the boundary itself: dust banked in a
thin low drift against the edge, its far side ending in the same
straight line, not one grain beyond it — and nothing standing
there to stop it.
10s — The push-in stops one meter from the line, the two boots on
polish at the frame's top edge, the living dust below. No cuts.

THE ONLY EVENT OF THIS SHOT IS THE LINE AND THE CROSSING — if the
boundary is not one continuous knife-sharp edge, the shot has failed.
It stays knife-sharp for every frame: no gradient, no blending, no
transition band, no glow, no reaction to the crossing — the ground on
either side never moves, never swells, never lights. Nothing stands
on or above the line: no wall, no pane, no glass, no barrier, no
fence, no dome, no force field, no visible effect in the air — only
two kinds of ground meeting. Dust displaced by their boots falls and
stops AT the line; not one grain settles on the polished side. Orange
stays on the woman, teal on the man; no morphing; every helmet stays
ON and sealed. One constant-rate push-in only: no cuts, no
transitions, no shake, no zoom snap. Exactly two figures — no third,
nobody in the background. No bloom, no glow filter, no lens flare. No
readable text or digits; no captions, no HUD, no watermark.
Photorealistic, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE 50 — FAZ KAPANIŞI: ANONS SUSUYOR

`8:10 – 8:20` · 85mm · kadro B · fixed lockoff · **A yolu**
📎 **REFERANS:** R3 (BEKÇİ — üç parmaklı el kule yüzeyinde)

_"200 yıl sonra ilk sessizlik."_

```
⚙️ SAHNE KARTI
  Tek çekim, 0 kesme, 10.0 s. Kamera sabit.
  İŞLEV: Bekçi kule yüzeyine dokunur; telsizde 200 yıldır dönen
  anons KESİLİR. Frekansta sadece taşıyıcı kalır.
  ⭐ SES OLAYI POST'TA — kadrajda hiçbir görsel geri bildirim YOK:
     kule yüzeyi değişmez, ışık yanmaz. Sessizliğin ağırlığını
     kurgu ve mix taşır; görüntü sadece dokunuşu verir.
  ⭐ BAĞLANTI → F6: ses köprüsü. S51 aynı sessizlikte, kapının
     açılışıyla devam eder.
```

### 📸 IMAGE PROMPT

```
SCENE:
A three-fingered white glove rests flat against the seamless white
wall of the tower — the touch that will silence two hundred years
of warning.

ENVIRONMENT:
The base of the colossal tower on the polished dead ground, soft
orange 4400K daylight from frame LEFT. The tower wall fills the
background as a smooth, matte white plane — seamless, unmarked,
slightly curved. The polished honed floor carries a faint warm
sheen and the soft reflection of the figure.

SUBJECT:
A tall sealed figure, 2.10 m, in profile from its right side,
chest-up: seamless, flawlessly pearl-white pressure suit,
dustless, unmarked, its BACK FLAT AND BARE in profile — no
backpack, no hoses, no protrusion.
Long right arm extended, its three-fingered glove pressed FLAT
against the tower wall at shoulder height; smooth featureless
helmet whose visor area is FILLED FLUSH with one solid matte plate
of dark grey-green, nearly black — no opening, no cavity, nothing
inside — angled toward the point of contact. Two whites meet in
frame — the suit's warm pearl against the tower's flat matte —
close in tone, clearly distinct in material.

CAMERA:
Shot on an 85mm lens from a fixed position two point five meters
away, f/2.8, at shoulder height, profile framing — arm, glove and
wall contact sharp; the wall's curve falls softly out of focus.

LIGHTING:
Soft orange daylight, 4400K, from frame LEFT: clean specular on
the pearl shell, flat even response on the matte wall; the glove's
contact point carries a soft shadow rim. Nothing emits light.

NEGATIVE:
Single unbroken take, no cuts, no camera shake. Exactly one
figure — nobody else in frame. The wall stays blank: NO WINDOWS AT
ALL, lit or unlit, no glass, no ports, no openings, no doors, no
hatches, no seams, no panels, no markings, no lights, no ripple, no
response at the touch. The glove has three
fingers and a thumb, fixed anatomy; it presses ON the surface,
never merging, never sinking in. The visor area stays a solid
filled dark grey-green plate — never glass, never white, never
mirrored; no face, eyes or reflection of a person forms in it. The
back stays flat and bare — no backpack, no hoses. No bloom, no glow
filter, no lens flare. No readable text or digits; no captions, no
HUD, no watermark. Photorealistic, 35mm anamorphic film grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, 85mm, fixed lockoff two point five meters
away, no cuts, no camera movement:

SETUP: the camera is locked off at shoulder height in profile,
f/2.8 — a tall white figure at the tower wall, its extended arm
and the contact point sharp. It never moves for the whole ten
seconds. The scene is generated SILENT; the sound event lives in
post.
FRAME: the seamless matte white tower wall filling the
background, the polished dead-ring floor below with its faint
sheen, soft orange 4400K daylight from frame LEFT. The figure:
exactly 2.10 m, pearl-white seamless suit, dustless; long right
arm raised, three-fingered glove hovering a hand-width from the
wall; smooth featureless helmet, opaque dark grey-green visor
angled at the wall.

0s — The glove hovers off the wall, perfectly still, the arm's
long line unbroken from shoulder to fingertip.
2s — It closes the last hand-width in one slow, continuous drift
and settles FLAT against the wall — a contact with no impact, no
recoil and no sound, the fingers meeting the surface all at once.
5s — Hold. Nothing in the frame changes: the wall stays blank,
no light answers, no seam opens. The stillness itself is the
event.
7s — The helmet bows a few degrees toward the contact point — the
same liquid, unhurried motion as everything it does — and holds
there.
10s — Glove flat, head bowed, wall silent. The frame holds this
exact composition to the end. No cuts.

The wall gives NO visible response at any second: no glow, no
ripple, no opening, no seam, no window lit or unlit, no vibration —
it stays a blank matte white plane. The glove presses on the
surface and never merges with it; the arm never trembles; the
figure's anatomy stays rigid — 2.10 m, three fingers, long arm,
flat bare back with no backpack or hoses, no morphing; the visor
area stays a solid filled dark plate — never glass, never white,
never mirrored, no face or reflection forming in it; the suit stays
dustless and seamless. Only two motions exist in
the whole shot: the slow final drift of the glove, and the slow
bow of the head. Exactly one figure. Camera locked: no cuts, no
transitions, no shake, no push-in. No bloom, no glow filter, no
lens flare. No readable text or digits; no captions, no
subtitles, no HUD, no watermark. Photorealistic, 35mm anamorphic
film grain.
```

---

# ✅ FAZ 5 DENETİM TABLOSU

| # | Lens | Kadro | Hareket | 10s yolu | Diyalog | İmaj | Risk (⚑ = F1-F4 QA'sında GERÇEKLEŞMİŞ hata) |
|---|---|:---:|---|:---:|:---:|:---:|---|
| S41 | 32mm | **2+B** | lockoff | A | — | 1 | **ÜÇ FİGÜR 1/5** · morph [D2] · ⚑ Bekçi sırt çantası [F4 D-R] · ⚑ 4. figür [F3 D-L] |
| S42 | 50mm | **2** | lockoff | A | — | 1 | alet belirmesi [D37] · yüz karışması · ⚑ kavrama beati düşer [F4 D-T] |
| S43 | 85mm | B | lockoff | B | Bekçi (post) | 1 | ⚑ **VİZÖRDE YÜZ** [F4 D-Q — F4 S39'da gerçekleşti] · vizörün beyaz çıkması |
| S44 | 50mm | 1 | lockoff | A | — | 1 | harf/rakam sızması [D13] · el-zemin [D11] · ⚑ çizim okunmaz kalır [F4 D-T] |
| S45 | 100mm | B | lockoff | A | — | 2 | **zemin tepki dili** [KARAR 2] · ⚑ kum şelalesi [F4 D-P] · ⚑ su benzetmesi [F2 D-A] |
| S46 | 50mm | 1+B | lockoff | A | — | 1 | işaret kolu morph · ⚑ ufuk çizgisi ROKET olur [F3 D-K] · ⚑ ön plan omuz büyür [F4 D-W] |
| S47 | 100mm | B | yanal takip | A | — | 2 | **VİRAL #2** · ayak izi kalması (yasak) · ⚑ akışa sayı yok [F4 D-P] |
| S48 | 32mm | **2+B** | lockoff | A | — | 1 | **ÜÇ FİGÜR 2/5** · kule ölçeği · ⚑ kulede pencere [F4 D-O] · ⚑ roket [F3 D-K] |
| S49 | 32mm | **2** | yavaş push-in | A | — | 2 | sınır keskinliği [KARAR 3] · ⚑ **"cam gibi" → gerçek cam** [F2 D-A] |
| S50 | 85mm | B | lockoff | A | — | 1 | duvarda görsel tepki (yasak) · geçiş çapası · ⚑ "su gibi" [F2 D-A] · ⚑ sırt çantası [F4 D-R] |

```
KADRO DENETİMİ
  İki insan aynı karede (2 veya 2+B): 4 (S41, S42, S48, S49) ✅
  Film geneli `2` sayacı: 14 / 23 kullanıldı
  Üç figürlü sahne: 2 / 5 kullanıldı (S41, S48) ✅
  Bekçi sahneleri: 7 (S41 S43 S45 S46 S47 S48 S50) ✅ plana uygun

SÜRE DENETİMİ
  10 sahne × 10.0 s = 100 s = 1:40 · S41 başlangıcı 6:40 ✅ FAZ TAM

ÇEHOV DENETİMİ
  ÇEHOV 1 (anons kelimeleri)  → S43'te ATEŞLENDİ ✅ ("DO NOT. DO NOT.")
  ÇEHOV 6 (ölü halka)         → S49'da kuruldu ✅ (ateşleme: S64)
  S1 CEVABI (dik çizgi = Kule) → S48'de verildi ✅
  ZEMİN TEPKİSİ (Novum canlı)  → S45 · S47 ✅ [KARAR 2 sınırları içinde]
  ANONS SUSTU (ses köprüsü)    → S50 ✅ → F6 S51 aynı sessizlikte açılır
  Bekçi replik sayacı: 1 / 5 kullanıldı (kalan: S60 · S66 · S86 · S99)
```

---

# ⏭️ SONRAKİ ADIM

```
✅ Faz 5 TAM — 10 sahne · 13 imaj · 10 video promptu
→ ../FAZ_06_KULE/FAZ_06_KULE.md (S51–S60) · S51, S50'nin
  sessizliğinde kapının açılışıyla devam eder (ses köprüsü)

⛔ ÜRETİMDEN ÖNCE (KARAR 4)
□ R3 BEKÇİ MASTER plakası üretildi ve insan gözüyle onaylandı mı?
   düz sırt · koyu gri-yeşil vizör · 2.10 m · uzun kol · üç parmak
   → onaysız 7 sahne (S41 S43 S45 S46 S47 S48 S50) üretilmez [F4 D-R]
□ İlk çıkan insan yüzü karesinde yara izi taraması: kadın SOL kaş,
   adam SAĞ elmacık — tek kareyle, insan gözüyle. Ters ise önce
   FLIP mi diye bak, yeniden üretime sonra karar ver [F3 D-H · F4 D-U]

□ Üretimden sonra: her sahnenin PLAN beati kurguda okunuyor mu
   [Ders 68 ③ — süre değil, BEAT sayılır]
□ Montajdan önce: 10 klip × 10.00 s [F3 D-N · F4 D-V]
□ QA: reel değil, 10 ayrı dosya — s41.mp4 … s50.mp4, MODE T
   [F1 ① · F3 ④ · F4 §1 — dört fazın üçünde sıra karıştı]
□ Tutan prompt sürümleri bu dosyaya işlenir; batanlar
   FAZ_05_QA_DERSLER.md'ye
```

---

# 📝 DEĞİŞİKLİK KAYDI

```
09.08.2026  F1-F4 QA TAŞIMASI — KARAR 4 eklendi, on sahnenin
            promptlarına dört fazın gerçekleşmiş hataları gömüldü:
            · Bekçi spec'i (düz sırt · koyu vizör · karşılaştırmalı
              boy · üç parmak) 7 Bekçi sahnesine [F4 D-R]
            · vizör "opak pencere" → DOLU MAT PLAKA (S41 S43 S46 S50)
              [F4 D-Q — negasyon vardı ve F4 S39'da tutmadı]
            · dört benzetme temizlendi: S45 "kuru su gibi akan
              taneler" + "sudan sonraki kum", S49 "cama dayanmış kum"
              (×2), S50 "durgun suya konan el" [F2 D-A]
            · S49'a "ortada duvar/cam/kubbe/bariyer YOK" negasyonu
            · roket + ışıksız pencere negasyonu S46/S48/S50 kulesine
              [F3 D-K · F4 D-O]
            · "THE ONLY EVENT OF THIS SHOT IS ___" açılışı S42 S44
              S45 S47 S49'a [F4 D-T · F3 D-I]
            · kask çift kilidi 6 insan sahnesine [F1 ②]
            · zemin akışına sayısal sınır: groove derinliği, 2 sn,
              şelale yasağı (S45 S47) [F4 D-P]
            · "no fourth figure / nobody in the background" S41 S46
              S48 S49'a [F3 D-L]
            · S46'da ön plan omuz kadraj genişliğinin 1/5'ini aşmaz
              [F4 D-W]
            · S48'de sırt ayrımı: tek sırt modülü ADAMINDIR
            ⚠️ Bilinçli KORUNAN: Bekçi'nin "liquid motion" hareket
            dili (S43 S46 S48 S50). Benzetme temizliği kuralının
            istisnası — F4 S40 koşusunda bu dil ÖLÇÜLDÜ ve tuttu
            ("obeys the movement lock beautifully"). Yalnız S47'de
            zemin-sıvı bitişikliği riskli olduğu için kaldırıldı.
            ⚠️ Bu dosya HENÜZ ÜRETİLMEDİ; düzeltmeler üretim öncesi
            girdi olarak yazıldı (F2/F3/F4 dosyalarında kural,
            üretilmiş fazın dosyasına dokunmamaktı).
```
