# 🖼️ THE SINKING STAKE — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir.

```
KAPAK ANI:      S1 (0:09-0:19)  ·  gerekçe: kapak filmin VAADİNİ göstermeli,
                en güzel karesini değil. S1 tek karede üç şeyi birden verir:
                (a) gökte kusursuz SİYAH bir disk, (b) yerde dimdik BEYAZ bir
                kazık, (c) kazığın dibinden çıkan dikey beyaz gaz halkası ve
                onun etrafında içeri çöken kar. Yani başlığın söylediği şeyin
                tam olarak olduğu an.
                ⛔ "en güzel sahne" gerekçe değildir. Tek sınav 120 px'tir.

BAŞLIKLA UYUM:  Başlık "THE SINKING STAKE" — kapakta batan bir kazık var.
                Kapak, filmin sonunu (yükselen sütun) SATMAZ; filmin
                KURALINI satar. Vaat-teyit penceresi: vaat 0:09'da verilir,
                film onu 0:14'te teyit eder (kazık kendi başına iner).
                → `THE_SINKING_STAKE_YAYIN_PAKETI.md` · CROSS-PLATFORM NOTES

PLAN B KAPAK:   S21 (3:29) — dikilen tek şeyin GAZ olduğu kare: ovadaki tek
                dikey nesne, kadrajın üstünden çıkan beyaz sütun, altında iki
                küçük beyaz figür. Kart Y bunun yayından ÖNCE hazır olmasını
                ister (§7.2). ⚠️ Plan B'nin bedeli: finali ele verir.

ÖLÇÜ:           yatay 1280×720
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek harf
> istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels, 16:9
landscape. Optimised for maximum legibility at thumbnail size.

Two astronauts in plain matte white surface suits stand on a flat white
plain of fine dry nitrogen snow, one on each side of a smooth white
column planted upright in the snow. The taller broad-shouldered one, dark
brown skin and close-cropped grey hair, wears a rigid white chest yoke
with two vertical tool loops; the shorter slight one, pale freckled skin,
has a flat chest and a wide white belt with a coiled white line at the
right hip. Both helmets are hard white shells with one flat front pane of
optically clear glass — zero tint, zero mirror coating, zero reflection —
and both faces are fully readable through them. The back of each suit is
one continuous smooth white panel from collar to hip, carrying nothing.
Nothing on either suit carries a patch, a mark, a stripe or a printed
shape; every surface is plain white.

The column is buried to a third of its length and the snow has dished
inward around it. From the snow all round its base one thin dead-straight
translucent white column of vapour rises straight up — no wider than the
column making it, the plain clearly visible through it, gone within about
six metres; it never curls, never widens, never drifts sideways and never
reads as smoke.

The sky is black. In the upper third of the frame hangs a perfectly black
disc about six times the width of a full moon, edged by one thin
brilliant white ring; outside the ring the starfield is stretched into
thin concentric arcs. There is no accretion disk: no plasma, no orange,
no red, no spiral, no flowing matter.

COMPOSITION: the black disc sits in the upper centre-right, well inside
the frame. The white column runs vertically from the bottom third up
toward it, so the disc and the column read as one vertical line. The two
figures are small and low, one in each outer third, clear of the bottom
15% and the right 20% of the frame — the bands platform interface elements
cover. Nothing story-critical falls in those bands.

LIGHTING: one source only — the thin bright ring around the black disc.
Bright moonlit snowfield level; soft-edged filled shadows, none fully
black; neutral white to very faint blue-white. No orange, no red, no gold.

NEGATIVE: Exactly two human characters and no others — no third person,
no duplicates, no clones, no reflected figure, no extra shadow. The suits
have no back-mounted unit — one continuous smooth white back panel,
carrying nothing. Helmet panes optically clear, zero reflection; both
faces fully readable. 0% bloom, no glow filter, no lens flare, no halo
around the disc or the ring, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin pores, lines and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — not on the suits, not on the column, not
on the snow. No scale marks, no graduation ticks, no survey markers, no
engraved or painted characters of any kind. No subtitles, no captions, no
title card, no end card, no credits, no watermark, no HUD overlay, no
logo. Nothing melts and there is no liquid of any kind — no water, no wet
surface, no drips, no slush, no ice sheen. No wind: nothing flutters,
nothing is blown, no snow drifts sideways. The vapour is thin, straight
and vertical — not smoke, not steam clouds, not fog, not fire. The black
disc has no accretion disk, no plasma, no colour. No Unreal Engine look,
no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film
grain.

Output: 1280x720, 16:9, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
  gökteki SİYAH DAİRE ve yerden ona doğru uzanan İNCE BEYAZ DİKEY ÇİZGİ.
  (İki figür 120 px'te iki beyaz leke olur — okunmaları GEREKMİYOR.)

⚠️ BU FİLMİN ÖZEL RİSKİ — BEYAZ ÜSTÜNE BEYAZ:
  Giysi beyaz, kar beyaz, gemi beyaz, gaz beyaz. Kapağı taşıyan tek
  kontrast SİYAH GÖKYÜZÜ ve SİYAH DİSKTİR. Kadrajın en az %55'i siyah
  gökyüzü olmalı; olmazsa 120 px'te kapak tek parça gri lekeye döner.
  Kontrol: kareyi 120 px'e indir, gri tonlamaya çevir, histogramda İKİ
  ayrı tepe (koyu gök / açık ova) görünüyor mu? Görünmüyorsa yeniden üret.

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı; test manuel yapılır.)
```
