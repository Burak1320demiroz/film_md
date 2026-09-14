# 🖼️ THE LEANING ROOM — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçildi,
üretimden sonra aranmayacak.

```
KAPAK ANI:      S7 · 78,0 s (1:18)
                gerekçe: 120 px'te okunması gereken TEK şey "her şeyi tek
                yöne yatmış bir oda + siyah bir daire"dir ve bu, iki büyük
                geometrik lekeyle taşınır — yatay duran bir sarkaç çizgisi
                ve mükemmel bir siyah disk. Yüz gerekmez; yüz zaten 120 px'te
                gri lekedir. Kadraj kadının EN KÜÇÜK olduğu karedir (EWS) ve
                ölçek kontrastı 1:10 tam burada kurulur.
                ⛔ "en güzel sahne" gerekçe değildir — bu kare filmin tek
                  kare testinin ta kendisidir (ONERME §4①).
BAŞLIKLA UYUM:  Başlık "THE LEANING ROOM" — kapak tam olarak yatmış bir oda
                gösterir. Vaat ve teyit AYNI nesnede: oda.
                Vaat-teyit penceresi: izleyici ilk 10 saniyede yatmayı görür
                (S0'ın 0. karesinde lamba zaten 4° eğik) → vaat büyütülmedi.
PLAN B KAPAK:   S9 · 96,0 s (1:36) — pirinç lambanın ECU'ya yakın hâli,
                iki ezik ve 3°'lik eğim. Daha soyut ama tek nesne, tek
                anlam; 120 px'te "yamuk asılı bir lamba" okunur.
                (Kart Y: Plan B yayından ÖNCE hazır olur.)
ÖLÇÜ:           yatay 1280×720  (kanal ana kapağı) + 1920×1080 arşiv
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek harf
> istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic, 16:9, the main saloon of a private long-range ship seen whole
on the diagonal from the aft corner on the port side: matte walnut panelling,
a dark woven floor, a low table, a deep armchair, a settee.

Everything loose in the room has gone one way. A single heavy brass pendant
lamp hangs from a ceiling rail on a braided cord over the middle of the room
and it is not vertical: the cord is taut and perfectly straight and the lamp
lies far over toward the starboard window on screen-right, sixty-eight degrees
off vertical, almost horizontal, completely still. The table top is empty.
Small objects have gathered along a low brass rail at the foot of the
starboard window on screen-right. The walls, floor and table stay rigid and
square to each other; only the hanging lamp and the loose objects have
answered a new direction of down.

A woman in her late thirties, brown skin, black hair drawn back into a low
flat knot, in a long charcoal wool coat-dress buttoned to the collarbone,
sits small in the deep armchair with a lap belt lying flat and tight across
her skirt, both hands on a brass hand wheel set into the table edge. Her face
is fully lit and completely readable, her expression level. She takes up less
than a tenth of the frame.

Through the long starboard window on screen-right, filling the right third of
the frame, hangs a perfect black circle with a thin bright ring of light
around its edge; the star field near it is drawn out into fine arcs.

COMPOSITION: the black circle in the right third, the leaning lamp crossing
the upper middle, the woman low and small in the left half. Nothing story
critical in the bottom eighth or the right sixth of the frame — the platform
interface covers those bands. Safe area respected.

LIGHTING: the thin ring around the black circle lays one hard cold line of
light in through the starboard window on screen-right, grazing the floor;
everything outside that line falls to absolute black with a razor edge. The
lamp's own warm pool, thrown sideways, is the only other source. No halo
around either source. Spherical lens rendering, no horizontal streak.

NEGATIVE: Exactly 1 human character in frame — no duplicates, no clones, no
second person, no reflected figure. 0% bloom, no glow filter, no soft focus,
no dreamy haze — every surface keeps visible texture. Photorealistic skin
pores retained, no waxy or smoothed skin. No readable text, letters, digits,
numbers or symbols on any surface in frame — not on the clothing, the brass,
the panelling, the glass or any object. No subtitles, no captions, no title
card, no watermark, no HUD overlay, no lens data, no name label. No mirrors.
The walls, floor and table stay rigid and square and never tilt, bend or warp.
Loose objects keep real weight, never hovering, never frozen. No lens flare,
no anamorphic streak, no starburst, no light rays. No Unreal Engine look, no
CGI aesthetic. Photorealistic with 35mm film grain.

Output: 1280×720, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
   "bir odadaki her şey tek yöne yatmış — ve dışarıda siyah bir daire var"

İki leke yeter: yatay duran açık renkli sarkaç ÇİZGİSİ + mükemmel siyah DİSK.
Kadının okunması GEREKMEZ; okunuyorsa bonus, okunmuyorsa kapak yine geçer.

⛔ okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
   Tipik arıza: oda düz çıkar (model ihlali "düzeltir"). O zaman lamba
   cümlesini kadrajın ilk cümlesine taşı ve odayı ikinci cümleye at.

⬜ MAKİNEYLE KOŞULACAK: kare 120 px'e indirilir, kontrast/entropi ölçülür.
   Koşulmadıysa bu madde işaretlenmez [HOOK §8].
```

---

## 🤐 SPOILER BÜTÇESİ — dört yüzey, tek bütçe [D114]

```
KAPAK      yatmış oda + siyah daire → İHLALİ gösterir, SEBEBİNİ göstermez ✅
BAŞLIK     "THE LEANING ROOM" → aynı ihlal, başka kelimeyle ✅
AÇIKLAMA   ilk satır ihlali tekrarlar, kararı ve bedeli ANMAZ ✅
İLK 10 SN  S0'ın 0. karesinde lamba zaten 4° eğik → vaat teyit edilir ✅

⛔ DÖRT YÜZEYİN HİÇBİRİNDE GEÇMEZ: kadının dar çizgiyi SEÇMESİ (S7),
   lambanın EZİLMESİ (S9) ve finaldeki 3°. Bunlar filmin tek ödemesidir.
```
