# 🖼️ THE_BENT_GRASS — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S11 · 115,0 s   ·   gerekçe: 120 px'e indiğinde kadrajda İKİ
                ayrı siluet kalır — solda dik beyaz bir gövde, sağda alçak ve
                uzun koyu bir gövde — ve aralarında tek bir açık gümüş şerit.
                Üç şekil, üç değer (beyaz · gümüş · koyu mor-gri): posta pulu
                boyunda tek bakışta okunur.
                ⛔ VAAT-TEYİT PENCERESİ SAPMASI [D74 · PAKETLEME §1]:
                  kural kapak anının 0:00-0:10 bloğundan seçilmesini ister.
                  Bu filmde o blok BİLİNÇLİ OLARAK insansızdır (S0 = tek bot
                  ve ezik ot) ve vaadi taşımaz. Kapak S11'den alınır; teyit
                  penceresi HOOK'un kendi vaadiyle kapatılır: kapağın sattığı
                  "iki gövde ve aralarındaki çizgi" ilişkisinin ÇİZGİ yarısı
                  0:00-0:10 arasında zaten ekrandadır.
BAŞLIKLA UYUM:  Kapak "iki gövde arasında bir çizgi" vaat ediyor; başlık
                "The Grass Here Remembers Every Step" aynı çizgiyi söylüyor.
                Kapakta hayvanın ağzı, dişi, saldırı jesti yok — başlık da
                tehdit vaat etmiyor. (→ YAYIN_PAKETI · CROSS-PLATFORM NOTES)
PLAN B KAPAK:   S12 · 128,0 s — kapanmış gümüş halka, üstünde üç koyu gövde,
                kenarında ayakta duran açık boş kasa. İnsansız; 120 px'te
                okunan şey HALKA'nın kendisidir (tek kapalı biçim).
                ⛔ Kart Y: yayın ANINDA hazır olur, 48 saat sonra üretilmez.
ÖLÇÜ:           yatay 1280×720 (16:9)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic still image, 16:9 widescreen, 4K.

A tall figure in a sealed white pressure suit with a smooth matte finish, a
bold red fabric stripe wrapped all the way around the RIGHT forearm and the
RIGHT thigh, the back of the suit one continuous smooth panel from collar to
hip carrying nothing, and a spherical helmet whose visor is optically clear
glass with zero tint, zero mirror coating and zero reflection of the
environment, the face fully readable through it. The figure stands still in
the left third of the frame, arms at the sides, on an unbroken plain of
knee-high pale gold-green grass that runs flat to the horizon in every
direction. One body-length to the right stands a four-legged grazing animal,
dark charcoal-violet, its shoulder just above the figure's helmet, with
exactly four jointed legs, one body and one pair of large dark eyes low on a
broad flat front wedge held parallel to the ground; the wedge is lowered
toward the ground and stops a hand's width above it. Between them, running
across the bottom third of the frame, lies one bright silver band of grass
crushed flat, and the wind wave bends every uncrushed stalk around it while
the silver band stays motionless.

COMPOSITION: the white figure occupies the left third and the dark animal the
right half; the silver band runs between them across the lower third; the
horizon sits high in the upper quarter; the centre of the frame is open sky
and grass, so nothing story-critical falls into the outer edges or the lower
strip where platform interface elements sit. Three values only: white suit,
silver band, dark hide.
LIGHTING:    one sun low on the screen-left side, soft-edged shadows falling
             to screen-right and not touching each other, real fill light
             from a pale high-cloud sky, highlights rolling off smoothly with
             visible texture, no bloom on the white helmet or the dark hide.
NEGATIVE:    Single frame. Exactly one human character — no second person,
             no duplicates, no clones.
             0% bloom, no glow filter, no soft focus, no dreamy haze. No
             readable text, letters, digits, numbers or symbols on any surface
             — not on the suit, not on the ground, not on the grass. No
             subtitles, no captions, no title card, no watermark, no HUD
             overlay, no lens data, no name label. The suit has no
             back-mounted unit: no backpack, no tank, no hose, no cable — the
             back is one continuous smooth panel carrying nothing; the visor
             is optically clear with zero tint and zero mirror coating. No
             contact between the animal and the figure, no open mouth, no
             teeth, no rearing, no charging. No wheat, no reed, no tree, no
             bush, no farmland, no cliff, no canyon, no rock outcrop, no
             water. No tilt-shift look, no miniature or toy-model read. No
             Unreal Engine look, no CGI aesthetic. Photorealistic with 35mm
             film grain.

Output: 1280×720, 16:9, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
  İKİ GÖVDE ARASINDAKİ AÇIK GÜMÜŞ ŞERİT — yani "aralarında bir şey var"
  bilgisi. Yüz 120 px'te gri bir lekedir ve okunması BEKLENMEZ; okunması
  gereken şey üç değerli siluet düzenidir (beyaz · gümüş · koyu).

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)

⭐ TEST İKİ YERE KOŞULUR [27.08.2026]: kapağa VE S0'ın ilk karesine.
   S0'ın 120 px sınavı: altın alanın ortasındaki tek gümüş çizgi.
```
