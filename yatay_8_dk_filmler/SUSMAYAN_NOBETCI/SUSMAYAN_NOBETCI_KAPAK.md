# 🖼️ SUSMAYAN_NOBETCI — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S0 · 0:04   ·   gerekçe: filmin kuralı tek karede duruyor — ön camın sol üçte ikisinde
                ikiye ayrılmış bir gövde ve hâlâ yanan motor konisi, sağ alt üçte birde pilotun eldiveni
                motor kolunun üstünde donmuş. İki büyük leke (parlak koni + koyu eldiven/kol) 120 px'te
                birbirinden ayrılıyor; tıklayan izleyici ilk on saniyede aynı kareyi görüyor.
                ⛔ "en güzel sahne" gerekçe değildir. Tek sınav 120 px'tir.
BAŞLIKLA UYUM:  başlık "Don't Light the Engine" motoru işaret ediyor; kapakta yanan koni ve kola uzanmış
                el var — ikisi aynı şeyi söylüyor (YAYIN_PAKETI → CROSS-PLATFORM NOTES)
PLAN B KAPAK:   S30 · 5:00 — kapsülün ayrıldığı kare (turuncu bant + dönen parçalar); yalnız A/B testinde
                kullanılır, spoiler bütçesi: bedelin SEBEBİ görünmez, yalnız turuncu bir nesne ayrılır
ÖLÇÜ:           yatay 1280×720 (dikey 1080×1920 yeniden çerçevelenir: kol sağ altta kalır, koni üstte)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
A photorealistic still from inside a small spacecraft cockpit, seen from just back of a suited pilot's
right shoulder. Her helmet and shoulder fill the lower right of the frame as a dark mass, a heavy
dark-grey glove open a palm above a stubby engine lever; one safety-orange band shows on her upper arm.
Through a three-panel canopy, far out in black space, a small shuttle has parted into two halves that
drift apart, a straight white engine cone still burning at the tail of the rear half; a thin cone of ice
crystals spreads from the torn seam in straight lines. The curved bright edge of a large rust-and-grey
planet crosses the bottom of the frame.

COMPOSITION: the parted shuttle and its burning cone in the upper left two thirds, the glove and lever
             in the lower right third; centre of frame empty black. Safe areas: nothing story-critical
             in the lower right 15% (duration chip) or the top 10%.
LIGHTING:    one hard sun from the upper left, out of frame; bright top faces, pure black shadow sides,
             the cone and the crystal spray the only bright shapes; the cabin lit dimly by a neutral
             4500K panel so the glove reads as a silhouette with texture, not a black blob.
NEGATIVE:    [KILAVUZ_REHBERI §5 negatif çekirdek] no text, no letters,
             no numbers, no watermark, no HUD overlay. No explosion, no fireball, no flame, no smoke.
             No beam and no visible projectile. 0% bloom, no glow. No second person in the cockpit.

Output: 1280×720, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey: PARLAK BİR ÇİZGİ (yanan koni) ve ONUN ALTINDA DURAN KOYU BİR EL —
yani "bir şey yanıyor, biri dokunmuyor". İki leke ayrı ayrı okunmalı; gövdenin ikiye ayrıldığı 120 px'te
okunmaz ve okunması da BEKLENMEZ (o bilgi ilk on saniyede geliyor).

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)
```
