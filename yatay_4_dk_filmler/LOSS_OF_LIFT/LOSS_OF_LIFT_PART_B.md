# 🎈 LOSS OF LIFT — Kaldırma Kaybı | PART B

## AI Production Bible — Self-Contained Prompts
### PART B: Sahne 13-24 (12 sahne) | 16:9 Yatay | Seçim · Bedel · Devretme
### _"Bir şeyin yükselmesi için senin inmen gerekir."_

> **PART B süresi:** 12 sahne × 10s = 120 saniye (2:09 – 4:09)
> **Toplam film:** 25 sahne = 249 saniye = 4 dakika 09 saniye
> **PART A:** `LOSS_OF_LIFT_PART_A.md` (S0-S12 + tüm Bible'lar)
> **Plan:** `LOSS_OF_LIFT_PLAN.md` — QA SPEC, risk kartları, ışık takvimi orada
> **FİLMİN TEK REPLİĞİ BU DOSYADADIR:** S22 · "Ağırlık bende kalsın."

---

## ⚠️ PART B ÜRETİM NOTLARI (promptlardan önce oku)

```
① İNSANSIZ SAHNELER (S13 · S19 · S24) — YAPISAL RED PROTOKOLÜ
   Üçünde de NEGATIVE kısa, insan imzası pozitif ("Human count in this
   frame: zero — the one crewman is inside the gondola"; S24'te ek:
   "the probe carries no one"). S19'daki 5.0s kararması İÇERİDEN GEÇEN
   adamın izidir — figür 0 kare; negatif bunu açıkça söyler.
   Red gelirse KILAVUZ_REHBERI §7 merdiveni.

② UZUNLUK BANDI — BİLİNÇLİ SAPMA GEREKÇESİ [PART A §② ile aynı]
   Çapa kuralı kelimesi kelimesine kopya ister → videolar bandın
   üstünde; TAVAN (4.300) aşımı SIFIR. 9/12 video I2V (insansız üçlü
   T2V); karakter videoda kompakt kilit satırı, çevre çapaları birebir.
   → prompt_kontrol 20.08.2026: 24 prompt · 0 BLOCK · FIX yalnız
     uzunluk — image 1.970-3.293 (S13 ve S22 bandın İÇİNDE) · video
     2.539-3.799 (S13-S14 bandın içinde/kenarında) · TAVAN (4.300)
     aşımı SIFIR. Kilit imzaları (tek çekim · bloom · metin · insan
     sayısı · grain · D79 · A1 · yön): 0 bulgu. Parafraz avcısı:
     0 şüphe. TR taraması (replik hariç): 0.

③ S22 REPLİK KURALLARI [KART 7 · D35 · D40]
   Filmin TEK repliği: "Ağırlık bende kalsın." — kask telsizi, tek
   konuşmacı, ~2 s (<5 s), AĞIZ KADRAJ DIŞI (kadraj göğüste biter →
   lip-sync yüzeyi 0). Altyazı yasağı hem gövdede hem negatifte.
   Replik görüneni ANLATMAZ [plan kuralı]: eylem kenetleme, cümle
   ağırlık. Üretimde replik değişecekse önce plan güncellenir.

④ ÜRETİM KAPILARI [D74] — S20 BU DOSYADADIR
   Film sırası: S0 → S5 → S20 → S8. S20 (doruk) PART B'nin İLK
   üretilecek sahnesidir; bedel kanalı (boru terlemesi + ıslık takası)
   orada test edilir. Koşular dosya sonundaki KAPI KAYITLARI'na.

⑤ ZAMAN SIKIŞTIRMA — İKİ BİLİNÇLİ SAPMA (ikisi de planda kilitli)
   S17: +2 çentik yükselim ekranda ~6 s (hikâyede ~6 dk) — planın
   SAYISAL KİLİTLER bloğunda yazılı. S21: balon dolumu; büyüme rivet
   çizgisine karşı "bir parmak" — dolum hikâyede ~1 saat.

⑥ ⛔ ÇAPA PARAFRAZ YASAĞI [PART A §⑥ ile aynı]
   Bu dosyanın promptları da PART A'nın SABİTLERİNDEN üreteçle
   basıldı — MAN/KOLON/PİN/MANİFOLD/PLAKA/CROWN/STATION blokları iki
   dosyada bayt bayt aynıdır. Yeni PART B çapaları aşağıda; doğrulama
   komutu çapa bölümünün sonunda.

⑦ S20 BEDEL KANALI ADAPTASYONU [D90 — kayıtlı karar]
   Plan: "takviye hattı susar, ibre yeniden düşmeye başlar". İbrenin
   düşüşü 10 saniyede FİZİKSEL OLARAK GÖRÜNMEZ (30 m/saat). Bedel aynı
   karede İKİ görünür kanala taşındı: boru terlemesi (kalın hatta
   yayılan film durur/sönerken ince hat boncuklanmaya başlar) + ıslık
   takası (besleme ıslığı ölür, daha ince yenisi doğar). "Takviye
   hattı susar" birebir korunur; ibre kanıtı S21'in son-pin beatine
   devredildi. Bu bir plan İHLALİ değil, D90 uygulamasıdır.

⑧ GECE/ŞAFAK IŞIK REJİMİ + RENK DİSİPLİNİ
   S13 gün batımı (en doygun kare) · S14-S22 gece (iç: tek nötr servis
   lambası + mor; dış: zifiri) · S23-S24 ilk ışık. MOR kaynağı her
   zaman kolon (S14 zemin taşması · S19 lomboz · S23 omuz taşması).
   AMBER: yalnız sonda feneri, KESİN 4 s periyot (S23 · S24) — S11'in
   2 s verici nabzından AYRI cihaz. Gölge yalnız iç mekân lambasından
   (S15 çentik gölgeleri) — dış dünya gölgesiz kalır.

⑨ KASK GEÇİŞİ S20→S21 SAHNE SINIRINDA [D69 ①]
   S20 kasksız, S21-S23 kask KAPALI; giyme hareketi 0 kare. Suit
   gerekçesi S21 gövdesinde: soğutma bandın altında, suit artık serin
   taraf. Vizör buğusu ALT KENARDA kalır — yüz okunur [D95].
   Sonda AYRILIŞI da kadraj dışıdır: S22 mühürle biter, S23 sonda
   çoktan yukarıdadır — mekanizma sahnesi yok [D69 ① sınıfı karar].
```

---

## 🔁 EŞLEŞTİRİLMİŞ KADRAJLAR — PART B'NİN KAFİYE SİSTEMİ

```
S0  ↔ S24   aynı ölçek/mesafe; kamera aşağı ↔ yukarı; 1 gövde ↔ 2 gövde
S2  ↔ S17   pin yayı 85mm/1.2 m; pin takma ↔ yükselip geri düşme
S3  ↔ S18   SETUP birebir [PART A Bible]; buğu VAR ↔ YOK (tek değişken)
S9  ↔ S16   kolon camı 85mm/1.6 m; canlı dokunuş ↔ ölü bant
S10 ↔ S20   manifold 32mm/4 m; bakılan kol ↔ atılan kol
S12 ↔ S21   lomboz kadrajı (ayna); sise gömülüş ↔ yükselenin gölgesi
S11 ↔ S23   85mm/1.4 m; amber nabız 2 s (verici) ↔ 4 s (sonda feneri)
```

---

## ⚓ PART B ÇAPA EKLERİ — KANONİK BLOKLAR

```
⚓ PART A'nın bütün kanonik blokları (MAN çekirdek/iç/suit · VİZÖR ·
KİLİT SATIRLARI · KOLON · PİN YAYI · MANİFOLD · PLAKA · CROWN ·
STATION · CALM · BUOY · I2V başlığı) bu dosyanın promptlarına da
BAYT BAYT AYNI enjekte edildi — burada yeniden basılmaz. Aşağıdakiler
yalnız PART B'de doğan bloklardır. Kural aynı: kelimesi kelimesine
kopyalanır, sahneye özgü durum bloktan SONRA gelir.
```

**GÜN BATIMI DÜNYASI (S13):**
```
the sunset cloud world — the ochre sea gone deep red-amber, the light still
even and shadowless with no sun disk anywhere; the upper veil burns dim
copper, the lower deck is almost black, and no ground, no horizon shadow and
no blue sky exist anywhere
```

**GECE DÜNYASI (S19):**
```
the night cloud world — near-total darkness in every direction: no stars, no
moon, no ground, no horizon; the cloud sea survives only as a faint charcoal
texture below the black
```

**İLK IŞIK (S23 S24):**
```
first light — a deep amber-ochre light returning evenly through the cloud from
every direction, shadowless, with no sun disk; the sea's upper haze pale
below, the veil brightening above
```

**VARMAYAN YAĞMUR / VİRGA (S13):**
```
the acid rain — far across the open air, vast slow curtains of rain hang from
the veil, falling in straight dim sheets that thin and end in mid-air,
dissolving two kilometers down; not one drop reaches any ground, because there
is no ground
```

**ZARF İÇİ — GECE SÜRÜMÜ (S18; PART A ENVIN'in gece varyantı):**
```
the inside of the envelope at night — a vast black vault, its milky skin gone
dark, the patch discs unreadable above; the only light is the small pool of
one neutral-white service lamp at the gondola neck, and the thin ceaseless
leak-whistle still hangs far up in the dark
```

**KALKIŞ KOLTUĞU KABUĞU (S15):**
```
the launch seat shell — a bare grey composite launch-seat shell with its
mounting feet cut short, two cut strap ends at its sides, and four
hand-scratched vertical notches on its backrest, one of them crossed by a
diagonal scratch; the notches are plain scratches — not letters, not numerals
```

**KÜLTÜR KARTUŞU (S22):**
```
the culture cartridge — a sealed forearm-length steel cylinder with one long
glass window showing pale filament strands in clear liquid, a machined locking
collar at each end
```

**SONDA (S23 uzak nokta · S24 gövde):**
```
the probe — a 12-meter pale teardrop balloon above a small boxy carrier frame
slung beneath it, one recessed amber beacon on the carrier pulsing once every
4 seconds
```

**DİYALOG NEGATİF EKİ (S22):**
```
The spoken line is heard only — no subtitles, no captions, no transcript. One
speaker, one line; no mouth and no face is in frame. Beyond the stated line
there is no other voice, no chatter, no music.
```

**DOĞRULAMA (parafraz avcısı — çıktı boşsa temiz):**
```
python3 - <<'X'
import re
KEYS={"culture column":"filled with clear liquid in which pale filament",
 "pin arc":"24 plain notches and carrying no numerals",
 "gas manifold":"eleven of them empty open collars",
 "launch seat shell":"four hand-scratched vertical notches",
 "culture cartridge":"one long glass window showing pale filament",
 "the probe —":"pulsing once every 4 seconds",
 "acid rain":"thin and end in mid-air",
 "night cloud world":"faint charcoal texture below the black",
 "first light":"returning evenly through the cloud"}
MAN_SIG="sunken cheeks, deep nasolabial lines"
t=open("LOSS_OF_LIFT_PART_B.md").read()
n=0
for b in re.findall(r"```\n(.*?)\n```",t,re.S):
    f=re.sub(r"\s+"," ",b)
    if re.search(r"[ğĞşŞıİçÇöÖüÜ]",f): continue
    for name,sig in KEYS.items():
        if name in f and sig not in f:
            print("PARAFRAZ ŞÜPHESİ:",name,"→",f[:70]); n+=1
    if "air engineer —" in f and MAN_SIG not in f and "CONTINUITY LOCKS" not in f:
        print("PARAFRAZ ŞÜPHESİ: air engineer →",f[:70]); n+=1
print("sonuç:",n,"şüphe (0 olmalı)")
X
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART B: S13-S24)

> ⚡ **Her prompt tamamen bağımsızdır.** İnsanlı 9 sahnenin videoları
> I2V içindir: önce IMAGE üretilir, onaylanır, video onaylı kareden
> koşulur. İnsansız üçlü (S13 · S19 · S24) T2V koşulabilir.

---

## 🎬 SAHNE 13 (S13) — VİRAL #2 — VARMAYAN YAĞMUR

> İnsansız — kısa negatif [üretim notu ①]. Virga = PERDE, parçacık bulutu değil
> [plan KART 6 kararı]. Filmin kapak adayı karesi (plan 🎬 #2).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Sunset over an
endless acid-cloud sea, vast rain curtains hanging in mid-air. Human count in
this frame: zero — the one crewman is inside the gondola.

SCENE: The camera holds a fixed position at the crown rail; at frame left the
dim curve of the crown of the station's envelope — a curving field of milky
acid-proof laminate mapped with hand-laid patch discs, the shallow recessed
walkway strip with low cleats and a thin guide rail running along it anchors
the scale. Beyond it: the sunset cloud world — the ochre sea gone deep
red-amber, the light still even and shadowless with no sun disk anywhere; the
upper veil burns dim copper, the lower deck is almost black, and no ground, no
horizon shadow and no blue sky exist anywhere. Across the middle distance: the
acid rain — far across the open air, vast slow curtains of rain hang from the
veil, falling in straight dim sheets that thin and end in mid-air, dissolving
two kilometers down; not one drop reaches any ground, because there is no
ground. The air is glass-calm: the station drifts with the wind it lives in,
so the relative wind is zero — nothing flutters, nothing sways, nothing is
blown.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position at the
crown rail, f/8. The film's most saturated frame: deep copper-amber, even and
shadowless; the rain sheets darker threads against the burning veil.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame:
zero — the one crewman is inside the gondola. 0% bloom, no glow filter, no
soft focus — every surface keeps texture. No readable text anywhere; no
subtitles, no title card, no watermark. The envelope and gondola are rigid and
unchanging — no melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. The rain sheets are straight, slow and
dim — never turbulent, never glossy; they end in mid-air and touch nothing.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera movement. Human count in this frame: zero — the one crewman is
inside the gondola.

SCENE: Fixed at the crown rail; at frame left the dim curve of the crown of
the station's envelope — a curving field of milky acid-proof laminate mapped
with hand-laid patch discs, the shallow recessed walkway strip with low cleats
and a thin guide rail running along it. Beyond: the sunset cloud world — the
ochre sea gone deep red-amber, the light still even and shadowless with no sun
disk anywhere; the upper veil burns dim copper, the lower deck is almost
black, and no ground, no horizon shadow and no blue sky exist anywhere. Across
the middle distance: the acid rain — far across the open air, vast slow
curtains of rain hang from the veil, falling in straight dim sheets that thin
and end in mid-air, dissolving two kilometers down; not one drop reaches any
ground, because there is no ground. The air is glass-calm: the station drifts
with the wind it lives in, so the relative wind is zero — nothing flutters,
nothing sways, nothing is blown.

TIMELINE: 0.0s — Stillness. The curtains hang from the veil, dim straight
sheets in copper light. 3.0s — One curtain's lower fringe thins and retreats
slightly upward — evaporation, slow and even. 6.0s — The copper light deepens
one shade everywhere at once; the unseen sun is sinking. 9.0s — The curtains
still hang, still falling, still arriving nowhere. Hold.

AUDIO: Vast soft quiet; the deep distant murmur of the cloud mass; the
faintest air-hiss. No voice, no music.

PHYSICS: 0.904 g. The rain falls straight and slow and dissolves mid-air;
nothing reaches a surface, because no surface exists. Relative wind zero:
nothing flutters.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Human count in this frame: zero — the one crewman is inside the gondola.
0% bloom, no glow filter, no soft focus — every surface keeps texture. No
readable text anywhere; no subtitles, no title card, no watermark. The cloud
deck moves only as one slow vast mass — never fast, never turbulent; loose
particles obey 0.904 g, never hovering, never swirling. The envelope and
gondola are rigid and unchanging — no melting, no warping. Real time — no slow
motion. No speech, no voice, no music. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain. The rain sheets are straight,
slow and dim — never turbulent, never swirling; they end in mid-air and touch
nothing.
```


---

## 🎬 SAHNE 14 (S14) — GECE

> [D90] ölçen kenar: lomboz ışığının ölümü rivet çerçevesine karşı okunur.
> MOR bu sahneden itibaren baskın — plan ışık takvimi S14-S18 gece rejimi.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Dim gondola
interior at nightfall, one man between a dying window and a violet doorway
spill. Exactly one human figure — this film has exactly one human total.

SCENE: A wide fixed frame across the gondola. At frame left, the round
porthole with its riveted frame: through the glass only a deep red-grey
darkness, the last of the light dying in the mist outside. At frame right, a
soft violet spill lies across the deck floor from the culture-room hatchway —
no one passes through it. Seated on a low bench between the two, hands loose
on his knees: the air engineer — a man in his early fifties, 1.79 m, thin,
shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. One small
recessed neutral-white service lamp holds the room dim.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position three
meters away at chest height, f/4. One neutral lamp, the dying porthole, and
the violet floor-spill — three lights, three directions, no other source.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The violet light enters only as the floor-spill from frame right;
no figure stands in or crosses the hatchway.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): The gondola at nightfall: porthole at frame
left, violet floor-spill from the culture-room hatchway at frame right, the
air engineer seated on the low bench between them. One neutral-white service
lamp. Camera fixed three meters away, 32mm spherical lens.

TIMELINE: 0.0s — He sits still, facing the porthole. The glass holds a last
deep red-grey. 3.0s — Read against the porthole's riveted frame, the light
outside dies by degrees — red-grey to near black. 6.0s — The violet spill is
now the strongest color in the room. He turns his head slowly from the dark
glass to the violet. 8.5s — He holds there, face half-lit in violet. 10.0s —
Hold.

AUDIO: Low fan hum; the thin leak-whistle; creak-ticks slower and sparser than
before. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The dense
air is still.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The violet light enters only as the floor-spill; no figure stands
in or crosses the hatchway; the porthole only darkens — nothing appears in it.
```


---

## 🎬 SAHNE 15 (S15) — DÖRDÜNCÜ KOLTUK

> Geride kalışın TEK anlatım nesnesi [plan: söylenmez]. Çentikler ÇİZİKTİR —
> harf/rakam değil [A1/D50 sigortası plandan]. Mor ışık çentiklere gölge verir
> (iç mekân lamba gölgesi meşru).

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man standing over
a bare launch seat in a violet-lit room. Exactly one human figure — this film
has exactly one human total.

SCENE: The small dark-walled culture room, flooded by the directional
violet-magenta light of the culture column — a sealed vertical glass cylinder,
2.4 meters tall and 60 centimeters wide, standing in a machined frame, filled
with clear liquid in which pale filament strands drift with slow individual
motion; a deep violet-magenta grow lamp inside its crown floods the room — the
only violet light that exists anywhere on the station standing at frame right.
On the floor at frame center: the launch seat shell — a bare grey composite
launch-seat shell with its mounting feet cut short, two cut strap ends at its
sides, and four hand-scratched vertical notches on its backrest, one of them
crossed by a diagonal scratch; the notches are plain scratches — not letters,
not numerals. Standing over it, looking down at the four scratched notches,
hands loose: the air engineer — a man in his early fifties, 1.79 m, thin,
shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. The violet
light rakes the backrest so the scratches carry small hard shadows — the only
shadows this film ever shows are lamp-made, indoors.

CAMERA & LIGHT: Shot on a 35mm spherical lens from a fixed position three
meters away at chest height, f/4. Single source: the grow lamp — directional,
clear falloff, full texture on every surface.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The four notches are plain hand-scratches — no letters, no
numerals, no symbols anywhere; the seat shell is empty equipment, no figure in
it.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): The violet-lit culture room; the culture column
— a sealed vertical glass cylinder, 2.4 meters tall and 60 centimeters wide,
standing in a machined frame, filled with clear liquid in which pale filament
strands drift with slow individual motion; a deep violet-magenta grow lamp
inside its crown floods the room — the only violet light that exists anywhere
on the station at frame right; on the floor the launch seat shell — a bare
grey composite launch-seat shell with its mounting feet cut short, two cut
strap ends at its sides, and four hand-scratched vertical notches on its
backrest, one of them crossed by a diagonal scratch; the notches are plain
scratches — not letters, not numerals; the air engineer standing over it.
Camera fixed three meters away, 35mm spherical lens.

TIMELINE: 0.0s — He looks down at the backrest: four scratched notches, one
crossed. 2.5s — He lowers himself slowly into the shell — weighted, ordinary
Earth pace, a man sitting into something never meant to stay here. 5.5s — His
hands find the two cut strap ends and rest on them. 7.5s — His right thumb
moves to the crossed notch and settles over it. 10.0s — He does not move
again. Hold.

AUDIO: The soft liquid circulation of the column; the low pump tick; his
breathing. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. The seat
shell takes his weight and does not shift; the straps are cut ends, limp and
static.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The four notches are plain hand-scratches — no letters, no
numerals; the shell holds only the one man who sits into it — no second
figure.
```


---

## 🎬 SAHNE 16 (S16) — ÖLEN BANT

> S9'un EŞ KADRAJI (85mm / 1.6 m — canlı dokunuş ↔ ölü bant). [D90] ölçen
> kenar: hareket KONTRASTI — üstte hiç, altta yavaş süzülme. Isı fiziği doğru:
> sıcak sıvı yükselir, önce ÜST bant pişer.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close on the glass
of a violet-lit culture column, a bare hand at a boundary line. Exactly one
human figure — this film has exactly one human total.

SCENE: Close on the glass wall of the culture column — a sealed vertical glass
cylinder, 2.4 meters tall and 60 centimeters wide, standing in a machined
frame, filled with clear liquid in which pale filament strands drift with slow
individual motion; a deep violet-magenta grow lamp inside its crown floods the
room — the only violet light that exists anywhere on the station. In the top
30 centimeters of the liquid, the strands have turned pale bone-white and hang
utterly motionless — a dead band, cooked by the heat that now rises past the
station. Below a visible boundary, the living strands still drift with slow
individual motion. Flat against the outside of the glass at that boundary
line: the bare right hand of the air engineer — a man in his early fifties,
1.79 m, thin, shoulders slightly stooped, light olive skin with visible pores,
sunken cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent
fatigue, short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm
old burn scar at his left temple, yellowed nail beds on his right hand; he
wears a faded sand-grey thermal jumpsuit, worn thin at the elbows and knees,
under an old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. The palm
rests ON the glass with a clean structural boundary, pores and creases sharp
in the violet light.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.6
meters away, f/2.8, focus on the glass plane. Single source: the
violet-magenta grow lamp, directional, clear falloff.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The dead strands never move; the living strands never cross the
boundary upward; the hand stays outside the sealed glass — it never touches
the liquid.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): Close on the glass of the culture column — a
sealed vertical glass cylinder, 2.4 meters tall and 60 centimeters wide,
standing in a machined frame, filled with clear liquid in which pale filament
strands drift with slow individual motion; a deep violet-magenta grow lamp
inside its crown floods the room — the only violet light that exists anywhere
on the station: the top 30 centimeters of strands bone-white and motionless —
the dead band — a visible boundary, and below it the living strands still
drifting. The bare right hand of the air engineer just off the glass. Camera
fixed 1.6 meters away, 85mm spherical lens, focus on the glass plane.

TIMELINE: 0.0s — The open hand waits a few centimeters off the glass, level
with the boundary line. 2.0s — The palm settles flat onto the glass at the
boundary — clean contact, clear structural edge. 4.5s — Below the line, the
living strands drift on, slow and individual. Above it, nothing moves at all.
The difference is the entire event. 7.5s — His fingers curl slightly against
the glass — the first crack in his stillness anywhere in the film. 10.0s —
Hold.

AUDIO: The circulation murmur, thinner than before; the pump tick; his
breathing, uneven once. No voice, no music.

PHYSICS: 0.904 g. Real time, no slow motion. The glass never flexes; the dead
strands hang; the living strands move only below the boundary.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The dead strands never move and never revive; the living strands
never cross the boundary; palm and glass never merge.
```


---

## 🎬 SAHNE 17 (S17) — YÜKSELİM — YANLIŞ UMUT

> S2'nin EŞ KADRAJI (85mm / 1.2 m). ⚠️ BİLİNÇLİ SAPMA [plan kilidi]: +2 çentik
> ekranda ~6 s'ye sıkıştırılır (hikâyede ~6 dk) — sapma planın SAYISAL
> KİLİTLER'inde yazılı. LOW POWER'ın toz şeytanı beatinin karşılığı.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close on a brass
quarter-circle instrument, a man slumped at frame right. Exactly one human
figure — this film has exactly one human total.

SCENE: Filling the left half of the frame: the pin arc — a 60-centimeter
quarter-circle of brushed brass bolted to the wall, cut with 24 plain notches
and carrying no numerals, no letters, no markings of any kind; a
phosphor-tipped needle rides along it, and a trail of small brass pins sits in
holes beside the notches above the needle — the topmost pins almost touching,
the lower ones spaced wider and wider apart. The phosphor-tipped needle now
rides a clear two notches below the lowest pin — the gap has grown since the
pins ran ahead of it. At frame right, seated slumped on the low stool, eyes on
the arc: the air engineer — a man in his early fifties, 1.79 m, thin,
shoulders slightly stooped, light olive skin with visible pores, sunken
cheeks, deep nasolabial lines, grey-brown eyes ringed with permanent fatigue,
short thinning iron-grey hair, patchy three-day grey stubble, a 4-cm old burn
scar at his left temple, yellowed nail beds on his right hand; he wears a
faded sand-grey thermal jumpsuit, worn thin at the elbows and knees, under an
old light-grey knitted cardigan with a stretched-open collar; on the
jumpsuit's chest a blank darker rectangle of cloth marks where a patch was
once sewn — it carries no lettering, no emblem, nothing readable. One small
recessed neutral-white service lamp; the brass holds its clean unbroken
highlight lines.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.2
meters away, f/4. One neutral lamp; the phosphor tip a steady pale point in
the dimness.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The arc carries plain notches only — no numerals, no letters, no
markings anywhere.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): the pin arc — a 60-centimeter quarter-circle of
brushed brass bolted to the wall, cut with 24 plain notches and carrying no
numerals, no letters, no markings of any kind; a phosphor-tipped needle rides
along it, and a trail of small brass pins sits in holes beside the notches
above the needle — the topmost pins almost touching, the lower ones spaced
wider and wider apart. The needle two notches below the lowest pin. The air
engineer slumped on the stool at frame right. Camera fixed 1.2 meters away,
85mm spherical lens. One neutral service lamp.

TIMELINE: 0.0s — Stillness; the thin leak-whistle holds its constant pitch.
1.5s — The whole gondola CREAKS once, long and low. The whistle thins to
almost nothing. 3.0s — The phosphor tip climbs one full notch — visible,
steady, real. 4.5s — It climbs a second notch. He is on his feet in one
movement, ordinary fast human pace, staring at the arc. 6.5s — The whistle
returns to full. The tip slows, stops, and slides back down. 8.5s — The tip
rests exactly where it began, two notches under the lowest pin. He is left
standing over an instrument that has told him nothing new. 10.0s — Hold.

AUDIO: The creak-swell at 1.5s; the leak-whistle thinning, then returning; one
sharp exhale when he stands. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time, no slow motion. A
convective updraft lifts the station and sets it back; on screen the
rise-and-return is compressed into this take — the needle's travel is smooth,
continuous and mechanical, never jumping.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The needle moves smoothly along the arc — up two notches, back to
the same notch — and the pins never move; no numerals, no letters anywhere.
```


---

## 🎬 SAHNE 18 (S18) — ISI — EŞ KADRAJIN İKİNCİ YARISI

> ⭐ S3↔S18 EŞLEŞTİRİLMİŞ KADRAJ [Hollow Count emsali]: SETUP cümlesi PART A
> Bible'ından BİREBİR (7 m · 32mm · alttan). Tek anlatı değişkeni BUĞU+BONCUK
> (var→yok); ışık gece rejimi plan takviminin gereğidir ve kayıtlıdır.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Low-angle night
interior of a vast dark balloon vault, a small man beside a steel plate.
Exactly one human figure — this film has exactly one human total.

SCENE: Low fixed angle from the catwalk floor: the inside of the envelope at
night — a vast black vault, its milky skin gone dark, the patch discs
unreadable above; the only light is the small pool of one neutral-white
service lamp at the gondola neck, and the thin ceaseless leak-whistle still
hangs far up in the dark. At frame bottom, small in the lamp pool, stands the
air engineer — a man in his early fifties, 1.79 m, thin, shoulders slightly
stooped, light olive skin with visible pores, sunken cheeks, deep nasolabial
lines, grey-brown eyes ringed with permanent fatigue, short thinning iron-grey
hair, patchy three-day grey stubble, a 4-cm old burn scar at his left temple,
yellowed nail beds on his right hand; he wears a faded sand-grey thermal
jumpsuit, worn thin at the elbows and knees, under an old light-grey knitted
cardigan with a stretched-open collar; on the jumpsuit's chest a blank darker
rectangle of cloth marks where a patch was once sewn — it carries no
lettering, no emblem, nothing readable. Beside him at shoulder height: the
condenser plate — a one-meter square of brushed steel set into the wall panel
beside the gondola neck, part of the cooling loop, its face BONE-DRY — not one
bead of condensation anywhere on it. Above him the vault climbs into total
darkness.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed low position seven
meters away, f/2.8, tilted up — the same framing as the earlier breath scene,
now in the dark. Single neutral-white service lamp pool.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The plate stays bone-dry — no fog, no bead, no condensation forms
at any point.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): Low fixed angle, tilted up: the inside of the
envelope at night — a vast black vault, its milky skin gone dark, the patch
discs unreadable above; the only light is the small pool of one neutral-white
service lamp at the gondola neck, and the thin ceaseless leak-whistle still
hangs far up in the dark. The air engineer small at frame bottom beside the
bone-dry condenser plate at shoulder height. Camera fixed seven meters away,
32mm spherical lens — the same setup as the earlier breath scene.

TIMELINE: 0.0s — He stands before the plate in the lamp pool, the vault black
above him. 2.0s — He leans in and exhales onto the steel — and nothing
appears. No fog, no bloom, no bead. 4.5s — He exhales again, longer, closer.
The plate stays bone-dry. 6.5s — Somewhere far up in the dark, metal TICKS —
sharp, irregular, the sound of heat working on structure. He lifts his head
into the black. 10.0s — Hold: a man, a dry plate, a vault he can no longer
see.

AUDIO: Low fan hum; the leak-whistle; two close soft exhales; then the hard
irregular ticks of expanding metal above. No voice, no music.

PHYSICS: 0.904 g — ordinary Earth pace, real time. The air is warm now: breath
cannot fog, and the cooling loop has fallen behind — that is the entire event
of this scene.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. No fog, no bead, no condensation forms at any point; the plate
stays bone-dry; the darkness above stays empty — nothing appears in it.
```


---

## 🎬 SAHNE 19 (S19) — VİRAL #3 — TEK MOR

> İnsansız — kısa negatif. Tek karede filmin bütün teması [plan 🎬 #3].
> 5.0s'deki yarım saniyelik kararma: içeriden geçen adamın izi — figür 0 kare.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Night: a
barely-visible dark sphere with one small violet window, nothing else in the
world. Human count in this frame: zero — the one crewman is inside the
gondola.

SCENE: the night cloud world — near-total darkness in every direction: no
stars, no moon, no ground, no horizon; the cloud sea survives only as a faint
charcoal texture below the black. Near frame center: the station — a 60-meter
translucent spherical envelope of milky acid-proof laminate, lit through by
the even daylight, mapped with hundreds of hand-laid patch discs in faintly
differing shades, a shallow recessed walkway strip with low cleats and a thin
guide rail running over its crown; beneath it, on a short lattice neck, hangs
an 11-meter boxy gondola of matte pale panels with one round porthole in its
flank. In this darkness the sphere reads only as a faint charcoal round, its
patch map gone, its walkway invisible; the gondola beneath it is a shadow. One
thing exists: the single round porthole in the gondola's flank, lit deep
violet from within — the only light in any direction, in any distance, in the
entire frame. The station floats in neutral buoyancy, settling at a constant
30 meters per hour — far too slow for the eye; within this shot it is
perfectly still, held by lift, never bobbing, never swinging, never rising.
The air is glass-calm: the station drifts with the wind it lives in, so the
relative wind is zero — nothing flutters, nothing sways, nothing is blown.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position 120 meters
out, f/2.8. No source but the violet window; it lights nothing beyond its own
small ring of gondola panel.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame:
zero — the one crewman is inside the gondola. 0% bloom, no glow filter, no
soft focus — every surface keeps texture. No readable text anywhere; no
subtitles, no title card, no watermark. The envelope and gondola are rigid and
unchanging — no melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. The violet window is the only light — no
stars, no second window, no reflection; the sphere stays a faint charcoal
round, never outlined, never rimmed.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera movement. Human count in this frame: zero — the one crewman is
inside the gondola.

SCENE: the night cloud world — near-total darkness in every direction: no
stars, no moon, no ground, no horizon; the cloud sea survives only as a faint
charcoal texture below the black. Near frame center: the station — a 60-meter
translucent spherical envelope of milky acid-proof laminate, lit through by
the even daylight, mapped with hundreds of hand-laid patch discs in faintly
differing shades, a shallow recessed walkway strip with low cleats and a thin
guide rail running over its crown; beneath it, on a short lattice neck, hangs
an 11-meter boxy gondola of matte pale panels with one round porthole in its
flank. In this darkness the sphere is only a faint charcoal round; the one
round porthole in the gondola's flank is lit deep violet from within — the
only light that exists. The station floats in neutral buoyancy, settling at a
constant 30 meters per hour — far too slow for the eye; within this shot it is
perfectly still, held by lift, never bobbing, never swinging, never rising.
The air is glass-calm: the station drifts with the wind it lives in, so the
relative wind is zero — nothing flutters, nothing sways, nothing is blown.

TIMELINE: 0.0s — Blackness, and one small violet window. 3.0s — Nothing moves.
The charcoal texture of the deck below shifts almost imperceptibly, one slow
vast breath. 5.0s — The violet window dims for half a second — something
passing between the lamp and the glass inside — then steadies. 9.0s —
Blackness, and one small violet window. Hold.

AUDIO: The deep distant cloud murmur, lower than ever; the faintest hiss;
nothing else. No voice, no music.

PHYSICS: 0.904 g. Neutral buoyancy, settling at 30 meters per hour —
invisible. Relative wind zero.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Human count in this frame: zero — the one crewman is inside the gondola.
0% bloom, no glow filter, no soft focus — every surface keeps texture. No
readable text anywhere; no subtitles, no title card, no watermark. The cloud
deck moves only as one slow vast mass — never fast, never turbulent; loose
particles obey 0.904 g, never hovering, never swirling. The envelope and
gondola are rigid and unchanging — no melting, no warping. Real time — no slow
motion. No speech, no voice, no music. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain. The violet window is the only
light — no stars, no second window, no beam; the half-second dimming at 5s is
an interior occlusion, not a figure — no person, face or silhouette is ever
visible.
```


---

## 🎬 SAHNE 20 (S20) — SEÇİM — DORUK · CENTRAL CHOICE

> ⛔ ÜRETİM KAPISI 3 [doruk] — PART B'nin İLK üretilecek sahnesi.
> S10'un EŞ KADRAJI (32mm / 4 m). ⚠️ BEDEL KANALI ADAPTASYONU [D90]: planın
> 'ibre yeniden düşer' kanıtı 10 s'de görünmez — bedel BORU TERLEMESİ (yayılan
> film durur/söner ↔ yeni boru boncuklanır) + ISLIK TAKASI ile aynı karede;
> 'takviye hattı susar' birebir korunur. İbre kanıtı S21'in pin/yay beatine
> devredildi. Kol tek hareket [D43 rijit].

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A man with his hand
on a steel lever between two pipes, night gondola. Exactly one human figure —
this film has exactly one human total.

SCENE: Filling the frame: the gas manifold — a wall rack of twelve cylinder
sockets, eleven of them empty open collars in a long row, one holding a single
full steel cylinder; beside the rack a single steel lever stands between two
pipes — a thick insulated line climbing up into the envelope, and a thinner
line running level into the probe-bay bulkhead. Tonight the rack is alive: the
lever stands thrown to the thick insulated line, and along that line's first
meter lies a thin film of condensation — the single full cylinder is FEEDING
the envelope, buying meters with the last gas. Standing squarely before the
rack, his right hand already resting on the lever: the air engineer — a man in
his early fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin
with visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes
ringed with permanent fatigue, short thinning iron-grey hair, patchy three-day
grey stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on
his right hand; he wears a faded sand-grey thermal jumpsuit, worn thin at the
elbows and knees, under an old light-grey knitted cardigan with a
stretched-open collar; on the jumpsuit's chest a blank darker rectangle of
cloth marks where a patch was once sewn — it carries no lettering, no emblem,
nothing readable. One neutral-white service lamp; the violet floor-spill faint
at the frame's right edge.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position four
meters away at chest height, f/4 — the same framing as the earlier reckoning
scene, now at night.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The rack carries no numerals, no letters, no markings; eleven
collars stay empty, one cylinder only; condensation exists only on the thick
line.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair,
grey stubble, in the faded sand-grey thermal jumpsuit and light-grey knitted
cardigan; the darker chest rectangle stays blank, carrying no lettering.

SCENE (as in the start frame): the gas manifold — a wall rack of twelve
cylinder sockets, eleven of them empty open collars in a long row, one holding
a single full steel cylinder; beside the rack a single steel lever stands
between two pipes — a thick insulated line climbing up into the envelope, and
a thinner line running level into the probe-bay bulkhead. The lever thrown to
the thick insulated line, a thin film of condensation along that line's first
meter, a low steady feed-hiss: the last cylinder is feeding the envelope. The
air engineer stands before the rack, right hand on the lever. Camera fixed
four meters away, 32mm spherical lens — the reckoning scene's framing, at
night.

TIMELINE: 0.0s — His hand rests on the lever. The feed-hiss holds; the thick
line's condensation film catches the lamp. 2.5s — He throws the lever in one
clean quarter-turn to the thin probe line — a hard mechanical stop. Nothing
else in the frame moves. 4.0s — The feed-hiss DIES. On the thick line, the
condensation film stops spreading and begins to dull. 6.0s — A new, fainter
hiss rises; the first fine beads of condensation appear on the thin probe
line. The lift he was buying is now going somewhere else. 8.0s — His hand
leaves the lever and hangs at his side. 10.0s — Hold: one dulling pipe, one
beading pipe, one still man.

AUDIO: The feed-hiss, its death at 4.0s, and the thinner new hiss from 6.0s —
the entire scene lives in that exchange; under it the fan hum and his steady
breathing. No voice, no music.

PHYSICS: 0.904 g. Real time, no slow motion. The lever moves exactly once,
through one quarter-turn, and stops hard; gas flow reads only as sound and as
condensation on the pipes.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The lever moves exactly once and nothing else on the rack moves;
no numerals, no letters, no markings; eleven collars stay empty, one cylinder
only; no vapor, no visible gas jet, no spray anywhere.
```


---

## 🎬 SAHNE 21 (S21) — BEDEL — SON PİN

> S12'nin AYNA KADRAJI (lomboz bu kez sağda). Kask geçişi S20→S21 sahne
> SINIRINDA [D69 ①]; suit gerekçesi gövdede: soğutma bandın altında, suit
> artık serin taraf. Vizör buğusu ALT KENARDA — yüz okunur kalır [D95].
> [D89] tek nesne sayımı: yerleşen TEK şey pin, hiçbir mühür açılmaz.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. A suited man
placing a last brass pin, a pale curve swelling in the porthole behind.
Exactly one human figure — this film has exactly one human total.

SCENE: At frame left: the pin arc — a 60-centimeter quarter-circle of brushed
brass bolted to the wall, cut with 24 plain notches and carrying no numerals,
no letters, no markings of any kind; a phosphor-tipped needle rides along it,
and a trail of small brass pins sits in holes beside the notches above the
needle — the topmost pins almost touching, the lower ones spaced wider and
wider apart. Beside the arc, a small brass pin cup, holding ONE last pin. At
frame right, the round porthole with its riveted frame: outside in the
blackness, barely, a dim pale curve — the flank of the probe balloon, filling
in the dark. Between arc and window stands the air engineer — a man in his
early fifties, 1.79 m, thin, shoulders slightly stooped, light olive skin with
visible pores, sunken cheeks, deep nasolabial lines, grey-brown eyes ringed
with permanent fatigue, short thinning iron-grey hair, patchy three-day grey
stubble, a 4-cm old burn scar at his left temple, yellowed nail beds on his
right hand; he wears a dirty sand-white acid-rated hard-shell pressure suit
with machined joint rings, matte and finely scuffed, carrying exactly three
fixed acid-bleached pale zones — across the right shoulder, along the left
forearm, over the knees — identical in every frame; a low-profile sand-white
helmet, CLOSED, his face fully readable through the visor The visor is one
seamless optically clear pane in a 2-cm brushed-metal frame, its lower seal
ring visible where it meets the collar, one thin unbroken specular line along
its top edge — the glass is always present, never absent. A faint film of
breath-mist sits along the visor's lower edge — the gondola's cooling has
fallen behind the heat, and the suit is now the cooler place; his face stays
fully readable above the mist line.

CAMERA & LIGHT: Shot on a 32mm spherical lens from a fixed position three
meters away at chest height, f/2.8. One neutral-white service lamp; the brass
and the visor frame carry the only highlights.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The arc carries plain
notches only — no numerals, no letters; the pale curve in the porthole is dim
and out of focus — never bright, never sharp.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): the pin arc — a 60-centimeter quarter-circle of
brushed brass bolted to the wall, cut with 24 plain notches and carrying no
numerals, no letters, no markings of any kind; a phosphor-tipped needle rides
along it, and a trail of small brass pins sits in holes beside the notches
above the needle — the topmost pins almost touching, the lower ones spaced
wider and wider apart The brass pin cup beside it holds ONE last pin. At frame
right the porthole: outside, barely, the dim pale curve of the probe balloon
filling in the darkness. The suited air engineer stands between them, a faint
film of breath-mist along the visor's lower edge, his face readable above it.
Camera fixed three meters away, 32mm spherical lens.

TIMELINE: 0.0s — He stands before the arc. Through the structure, a deep soft
rumble: fabric filling, somewhere below. 2.0s — He lifts the last pin from the
cup. The cup is now empty. 4.0s — He presses the pin into the hole at the
needle's own notch — one clean seat. EXACTLY ONE OBJECT IS PLACED IN THIS SHOT
— THE PIN; every seal on the suit stays closed in every frame: helmet locked,
collar ring closed, both gloves on. 6.0s — His glove drops. Read against the
porthole's rivet line, the pale curve outside has swelled a finger-width since
the shot began. 8.5s — He turns his head from the arc to the window. 10.0s —
Hold.

AUDIO: The deep soft fill-rumble through the structure; the faint new
feed-hiss below it; his breathing inside the closed helmet. No voice, no
music.

PHYSICS: 0.904 g — ordinary Earth pace, real time. The balloon fills slowly
and steadily; its curve's growth is read only against the rivet line.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The arc carries plain
notches only — no numerals, no letters; the pin cup ends this shot empty and
stays empty; the pale curve grows only slightly and stays dim.
```


---

## 🎬 SAHNE 22 (S22) — DEVRETME — FİLMİN TEK REPLİĞİ

> Replik: "Ağırlık bende kalsın." — KAYIT değil, kask telsizi; AĞIZ KADRAJ
> DIŞI (kadraj göğüste biter) → D35 yüzeyi 0. Tek konuşmacı, <5 s, altyazı
> yasağı negatifte [D40]. [D89] tek mühür: kapanan TEK şey taşıyıcı bileziği.
> Replik görüneni ANLATMAZ [plan kuralı] — eylem kenetleme, cümle ağırlık.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Two sand-white
gloves holding a sealed glass-windowed cylinder above an open cradle collar.
Exactly one human figure — this film has exactly one human total; only his
gloved hands and forearms are in frame.

SCENE: Close on the probe bay cradle: an open machined collar set in a frame,
sized to a forearm-length cylinder, with a quarter-turn locking ring. Held
above it in two sand-white hard-shell gloves: the culture cartridge — a sealed
forearm-length steel cylinder with one long glass window showing pale filament
strands in clear liquid, a machined locking collar at each end. The gloves and
forearms belong to the suited air engineer; the framing ends at his chest — no
helmet, no face in frame. Behind, dim and out of focus, the pale folded fabric
of the deployment line and one small neutral work lamp.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position one meter
away, f/2.8, focus on the cartridge and collar. One neutral work lamp; the
glass window of the cartridge carries the frame's only bright line.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. No face, no helmet, no mouth is in frame — the framing ends at the
chest; the visor, out of frame, stays optically clear and closed; the suit has
NO back-mounted unit. The cartridge window shows drifting strands only — no
readable text, no markings anywhere.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total; only his gloved hands and forearms are in frame. One human voice speaks
over the suit radio; no mouth is in frame.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): Close on the probe bay cradle — the open
machined collar, the quarter-turn locking ring. Held above it in two
sand-white gloves: the culture cartridge — a sealed forearm-length steel
cylinder with one long glass window showing pale filament strands in clear
liquid, a machined locking collar at each end. The framing ends at the chest:
no helmet, no face. Camera fixed one meter away, 85mm spherical lens, focus on
the cartridge and collar.

TIMELINE: 0.0s — The gloves hold the cartridge level above the open collar,
steady. 2.5s — They lower it in — a visible gap closing to one hard, clean
contact. 4.5s — One quarter-turn of the locking ring to a dead stop. EXACTLY
ONE SEAL CLOSES IN THIS SHOT AND IT IS THE CARRIER COLLAR — every seal on the
suit stays closed: helmet locked, collar ring closed, both gloves on; nothing
on the suit is opened or removed. 6.5s — The gloves go still on the sealed
carrier. Over the suit radio, quiet and level, in Turkish: "Ağırlık bende
kalsın." 9.5s — The gloves lift away slowly, empty. 10.0s — Hold on the sealed
cartridge in its collar.

AUDIO: The hard contact at 2.5s and the ring's stop at 4.5s, both dull and
close; the fill-rumble beneath everything; the single spoken line at 6.5s —
heard only, never shown as text; then only his breathing. No music.

PHYSICS: 0.904 g. Real time, no slow motion. Cartridge, collar and gloves stay
rigid separate bodies — visible gaps close to hard contacts, nothing merges.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The spoken line is heard only — no subtitles, no captions, no
transcript. One speaker, one line; no mouth and no face is in frame. Beyond
the stated line there is no other voice, no chatter, no music. The suit has NO
back-mounted unit; the visor, out of frame, stays optically clear and closed.
The locking ring turns exactly once; the cartridge window shows drifting
strands only — no readable text, no markings.
```


---

## 🎬 SAHNE 23 (S23) — VİRAL #4 — İKİ IŞIK

> S11'in EŞ LENSİ (85mm / 1.4 m — verici nabzı ↔ sonda nabzı). İki ışık CAMDAN
> GEÇEN ışıktır, vizör YANSIMASI değil [D79/D88 çizgisi gövdede açık]. Amber
> burada ve S24'te yalnız sonda feneri (4 s) — S11'in 2 s verici nabzından
> ayrı cihaz, plan 🎨 disiplini.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close on a suited
man at a round porthole, two colors of light on one face. Exactly one human
figure — this film has exactly one human total.

SCENE: Three-quarter close at the porthole: head and shoulders of the air
engineer — a man in his early fifties, 1.79 m, thin, shoulders slightly
stooped, light olive skin with visible pores, sunken cheeks, deep nasolabial
lines, grey-brown eyes ringed with permanent fatigue, short thinning iron-grey
hair, patchy three-day grey stubble, a 4-cm old burn scar at his left temple,
yellowed nail beds on his right hand; he wears a dirty sand-white acid-rated
hard-shell pressure suit with machined joint rings, matte and finely scuffed,
carrying exactly three fixed acid-bleached pale zones — across the right
shoulder, along the left forearm, over the knees — identical in every frame; a
low-profile sand-white helmet, CLOSED, his face fully readable through the
visor The visor is one seamless optically clear pane in a 2-cm brushed-metal
frame, its lower seal ring visible where it meets the collar, one thin
unbroken specular line along its top edge — the glass is always present, never
absent. Through the glass beyond him: first light — a deep amber-ochre light
returning evenly through the cloud from every direction, shadowless, with no
sun disk; the sea's upper haze pale below, the veil brightening above. High in
the porthole's upper corner, a single tiny amber point pulses once every 4
seconds — the probe, already above the haze, already safe. From frame left
behind him, the violet spill of the culture room lies along the left side of
his helmet and shoulder; the right side of his face takes the returning
amber-ochre through the glass. Two lights, one face — both falling THROUGH the
clear pane onto him, neither reflected on it.

CAMERA & LIGHT: Shot on an 85mm spherical lens from a fixed position 1.4
meters away, f/2.8, focus on his face through the visor. Two sources only: the
violet spill from frame left, the first light through the porthole.

NEGATIVE: Fixed locked-off camera, single frame. Exactly one human figure —
this film has exactly one human total: no second person, no duplicate, no
figure in any reflection. 0% bloom, no glow filter, no soft focus — every
surface keeps visible texture. Photorealistic skin with pores — no
airbrushing, no face morphing. Clothing identical to the description. No
readable text, letters, digits or symbols anywhere; no subtitles, no title
card, no watermark. Hand-surface contacts keep a clear structural boundary —
no merging, no extra fingers. Surfaces static and solid — no melting, no
warping. No Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The amber point is the
only amber light and it pulses on a strict 4-second period; the two lights
fall on the face and never appear as reflections on the visor.
```

### 🎥 VIDEO PROMPT (I2V — onaylı IMAGE karesinden)

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera move. Exactly one human figure — this film has exactly one human
total.

START FRAME: the approved still from this scene's IMAGE prompt. Everything in
that frame is already correct — face, clothing, set, light, framing. Do not
redesign any of it; animate it. CONTINUITY LOCKS carried from the frame:
exactly one human — the air engineer, early fifties, thin, iron-grey hair, in
the sand-white acid-rated hard-shell pressure suit with its three fixed
bleached zones (right shoulder, left forearm, knees); helmet CLOSED, the visor
a clear pane in its 2-cm brushed-metal frame with the collar seal ring visible
and one thin specular line at its top edge; back silhouette flat.

SCENE (as in the start frame): Three-quarter close at the porthole: the suited
air engineer, head and shoulders. Through the glass: first light — a deep
amber-ochre light returning evenly through the cloud from every direction,
shadowless, with no sun disk; the sea's upper haze pale below, the veil
brightening above. In the porthole's upper corner a single tiny amber point —
the probe above the haze. Violet spill from frame left on his helmet's left
side; first light on the right of his face. Camera fixed 1.4 meters away, 85mm
spherical lens.

TIMELINE: 0.0s — He is still, eyes on the amber point. 2.0s — The point pulses
once. His eyes hold it. 4.0s — His gaze comes down slowly to the pale haze of
the sea below the light. 6.0s — The point pulses again, at its strict 4-second
period, at the frame's top corner. 7.5s — His breathing slows; his shoulders
settle. Not surrender — arrival. 10.0s — The point pulses a third time. Hold
on the two-lit face.

AUDIO: Near silence: his slow breathing inside the helmet; the faintest
structural creak; nothing else. No voice, no music.

PHYSICS: 0.904 g. Real time. The amber point holds its exact 4-second period;
the two lights hold their directions; nothing in the frame moves but the man's
eyes, head and breath.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Exactly one human figure — this film has exactly one human total; no
second person, no duplicate, no figure in any reflection. 0% bloom, no glow
filter, no soft focus — every surface keeps visible texture; photorealistic
skin with pores, no airbrushing, no face morphing. Clothing identical to the
description — nothing appears or disappears mid-shot. No readable text
anywhere; no subtitles, no title card, no watermark. Hand contacts keep a
clear structural boundary — no merging, no extra fingers. Particles obey 0.904
g — never hovering, never swirling. Surfaces static — no melting, no warping.
The background is identical in every frame — nothing changes, appears or
disappears. Real time — no slow motion. No speech, no voice, no music — this
scene is wordless. No unnamed prop. No CGI aesthetic. Photorealistic with 35mm
film grain. The suit has NO back-mounted unit — no backpack, no tank, no hose,
no cable; his back silhouette is flat. The visor is optically clear, zero
tint, zero mirror coating — his face fully readable through it in every frame.
The three bleached zones stay fixed and never shift. The amber point is the
only amber light, pulsing on a strict 4-second period — never drifting, never
brightening; both lights fall on the face and never read as reflections on the
visor.
```


---

## 🎬 SAHNE 24 (S24) — FİNAL — AYNA

> S0'IN AYNASI [plan 🔁 çifti]: aynı ölçek, kamera bu kez hafif YUKARI; tek
> gövde↔iki gövde, gün sonu↔gün başı. İnsansız — kısa negatif. Sondanın
> yükselişi 10 s'de GÖRÜNÜR (birkaç m/s — balon fiziği), istasyonunki görünmez
> (30 m/saat) — zıtlık finalin kendisidir.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Dawn over an
endless cloud sea: a great dark sphere sinking below, a small pale balloon
rising above. Human count in this frame: zero — the one crewman is inside the
gondola; the probe carries no one.

SCENE: The camera holds a fixed position 250 meters out, looking gently UP —
the mirror of the film's first frame. Filling the world: first light — a deep
amber-ochre light returning evenly through the cloud from every direction,
shadowless, with no sun disk; the sea's upper haze pale below, the veil
brightening above. In the lower third, sunk to its equator in the dark
sea-top: the station — a 60-meter translucent spherical envelope of milky
acid-proof laminate, lit through by the even daylight, mapped with hundreds of
hand-laid patch discs in faintly differing shades, a shallow recessed walkway
strip with low cleats and a thin guide rail running over its crown; beneath
it, on a short lattice neck, hangs an 11-meter boxy gondola of matte pale
panels with one round porthole in its flank — only the upper half of the
sphere still clear of the mist, dim and patched, its gondola gone from sight.
In the upper third, small and climbing into the brightening light: the probe —
a 12-meter pale teardrop balloon above a small boxy carrier frame slung
beneath it, one recessed amber beacon on the carrier pulsing once every 4
seconds. The air is glass-calm: the station drifts with the wind it lives in,
so the relative wind is zero — nothing flutters, nothing sways, nothing is
blown. The station settles as it always has; the probe rises slowly and
steadily, straight up, a few meters per second.

CAMERA & LIGHT: Shot on a 24mm spherical lens from a fixed position 250 meters
away, f/8. First light, even and shadowless; the probe's balloon pale against
the veil, the sphere dark against the sea.

NEGATIVE: Fixed locked-off camera, single frame. Human count in this frame:
zero — the one crewman is inside the gondola. 0% bloom, no glow filter, no
soft focus — every surface keeps texture. No readable text anywhere; no
subtitles, no title card, no watermark. The envelope and gondola are rigid and
unchanging — no melting, no warping. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain. Two bodies only — one sphere below, one
small balloon above; no other object exists in the sky; the amber beacon
pulses on a strict 4-second period.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9, photorealistic. Fixed locked-off camera,
no camera movement. Human count in this frame: zero — the one crewman is
inside the gondola; the probe carries no one.

SCENE: Fixed position 250 meters out, looking gently up — the mirror of the
film's first frame. first light — a deep amber-ochre light returning evenly
through the cloud from every direction, shadowless, with no sun disk; the
sea's upper haze pale below, the veil brightening above. Lower third: the
station — a 60-meter translucent spherical envelope of milky acid-proof
laminate, lit through by the even daylight, mapped with hundreds of hand-laid
patch discs in faintly differing shades, a shallow recessed walkway strip with
low cleats and a thin guide rail running over its crown; beneath it, on a
short lattice neck, hangs an 11-meter boxy gondola of matte pale panels with
one round porthole in its flank — sunk to its equator in the dark sea-top,
only the upper half of the sphere clear, dim and patched. Upper third: the
probe — a 12-meter pale teardrop balloon above a small boxy carrier frame
slung beneath it, one recessed amber beacon on the carrier pulsing once every
4 seconds, climbing into the brightening light. The air is glass-calm: the
station drifts with the wind it lives in, so the relative wind is zero —
nothing flutters, nothing sways, nothing is blown.

TIMELINE: 0.0s — Two bodies, one frame: the dark half-sphere below, the small
pale balloon above. 1.0s — The amber beacon pulses. 3.0s — The probe has risen
visibly against the top of the frame — slow, steady, straight; the station has
not moved at all. 5.0s — The beacon pulses again. The mist takes another edge
of the sphere's dark curve. 9.0s — The beacon pulses a third time, higher now,
smaller now. 10.0s — Hold: one thing going down with the light rising around
it, and one thing going up.

AUDIO: The deep cloud murmur, far below; the faintest air-hiss; nothing human.
No voice, no music.

PHYSICS: 0.904 g. The station settles at its constant 30 meters per hour —
invisible; the probe climbs at a few meters per second — visible, steady,
straight up; both hold their lines. Relative wind zero.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans, no
zoom. Human count in this frame: zero — the one crewman is inside the gondola.
0% bloom, no glow filter, no soft focus — every surface keeps texture. No
readable text anywhere; no subtitles, no title card, no watermark. The cloud
deck moves only as one slow vast mass — never fast, never turbulent; loose
particles obey 0.904 g, never hovering, never swirling. The envelope and
gondola are rigid and unchanging — no melting, no warping. Real time — no slow
motion. No speech, no voice, no music. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain. Two bodies only — nothing else
appears in the sky; the probe rises only, straight and slow, and never drifts
sideways; the beacon holds its strict 4-second period; the sphere never lifts,
never brightens.
```

---

# 📋 PART B ÖZET TABLOSU

| # | Sahne | İnsan | Kask | Işık | Lens / mesafe | Sayaç / kanıt kanalı |
|---|---|:---:|:---:|---|---|---|
| S13 | VİRAL #2 — VARMAYAN YAĞMUR | 0 | — | Gün batımı | 32mm / taç rayı | virga: varmayan yağmur |
| S14 | GECE | 1 | — | Gece + mor | 32mm / 3 m | lomboz ışığının ölümü |
| S15 | DÖRDÜNCÜ KOLTUK | 1 | — | Mor | 35mm / 3 m | 4 çentik, biri çizik |
| S16 | ÖLEN BANT | 1 | — | Mor | 85mm / 1.6 m | ölü bant sınır çizgisi |
| S17 | YÜKSELİM | 1 | — | Gece iç | 85mm / 1.2 m | ⭐ ibre +2 çentik → aynı yer |
| S18 | ISI | 1 | — | Gece zarf içi | 32mm / 7 m | buğu YOK (S3 çifti) |
| S19 | VİRAL #3 — TEK MOR | 0 | — | Zifiri + mor | 32mm / 120 m | tek mor lomboz |
| S20 | SEÇİM — DORUK | 1 | — | Gece iç | 32mm / 4 m | ⭐ boru terlemesi + ıslık takası |
| S21 | BEDEL — SON PİN | 1 | ✔ | Gece iç | 32mm / 3 m | boş pin kabı · vizör buğusu · dolan balon |
| S22 | DEVRETME — TEK REPLİK | 1(el) | ✔ | Gece yatak | 85mm / 1.0 m | kenetlenen kartuş |
| S23 | VİRAL #4 — İKİ IŞIK | 1 | ✔ | Şafak + mor | 85mm / 1.4 m | amber nokta 4 s |
| S24 | FİNAL — AYNA | 0 | — | İlk ışık | 24mm / 250 m | iki gövde, zıt yön |

**Doğrulama:** 12 sahne · 24 prompt · insanlı 9 sahne / 18 prompt ·
insansız 3 (S13 S19 S24, kısa negatif) · suit'li 3 sahne (S21-S23,
D79 6/6 promptta; S22 yüz kadraj dışı varyantı) · replik 1 (S22,
Türkçe, telsiz, ağız kadraj dışı) · altyazı bütçesi 0.0 sn · MOR
kaynağı hep kolon · AMBER yalnız sonda feneri 4 s (S23 S24) · kamera
12/12 sabit lockoff · eş kadraj çiftleri yukarıdaki tabloda · ışık
ekseni monotonik: gün batımı → gece → ilk ışık (plan takvimi birebir).

---

## 🚪 KAPI KAYITLARI [D74] — her koşu TEK SATIR

```
Format: TARİH · KAPI (S0/S5/S20/S8) · SONUÇ (GEÇTİ / V2 / DÜŞÜŞ) · not
20.08.2026 · YAZIM · PART B üreteçle basıldı (24 prompt; PART A
  sabitleri bayt bayt devralındı, parafraz avcısı 0 şüphe) ·
  prompt_kontrol: sonuç üretim notu ②'ye işlendi · TR taraması: 0.
20.08.2026 · DURUM: ÜRETİM BAŞLAMADI — film kapı sırası S0 → S5 →
  S20 (bu dosya) → S8. Dört kapının dördü de artık koşulabilir.
(sonraki koşular buraya eklenecek)
```
