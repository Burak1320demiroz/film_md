# 🖼️ THE STILL SWARM — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.
**Durum:** ⬜ TASLAK (yazımla birlikte) → ⬜ FINAL (üretimden sonra)

```
KAPAK ANI:      S0 · 0:06   ·   gerekçe:
                Kapak anı 0:00-0:10 bandından seçilir [PAKETLEME §1] — böylece
                tıklayan izleyicinin gördüğü ilk hareketli görüntü kapakla
                AYNI olur ve beklenti ilk saniyede doğrulanır. 0:06 o bloğun
                içinde kabuğun tamamının kadrajda ve tam hareketsiz olduğu,
                figürün ise açıkça HAREKET HÂLİNDE olduğu tek andır: kapağın
                taşıdığı bilgi bu kontrasttır, güzellik değil.

ÜÇ ODAKTAN HANGİSİ (§2): ③ FRAKTAL ÖLÇEK
                Sabit figürün arkasında kendini tekrarlayan devasa bir yapı —
                260 ayrı parçadan kurulu 40 metrelik kabuk. Figür ile arka
                plan arasındaki ölçek farkı keşif arzusu üretir ve lockoff'un
                durağanlığını kırar.
                ⛔ ① vizör yansıması bilinçli olarak SEÇİLMEDİ: bu filmin
                  vizörü optik berraktır (tint 0, ayna kaplama 0) ve
                  yansıtmaz; o odak burada fiziksel olarak mümkün değil.

BAŞLIKLA UYUM:  Kapak "kalabalık bir şey, ama hiçbiri kımıldamıyor" diyor.
                Seçilen başlık aynı şeyi söylüyor ve fazlasını söylemiyor —
                twist'i, hücreyi, finali vermiyor.
                → THE_STILL_SWARM_YAYIN_PAKETI.md → CROSS-PLATFORM NOTES

PLAN B KAPAK:   S7 · 1:14 — tepeden bakış: kadın kadrajın %10'u, arkasında üç
                kelepçenin kusursuz düz hattı. Kart Y yayından ÖNCE hazır
                olmasını ister (§7.2). ⛔ İlk 48 saatte kapak VEYA başlık
                değişir, ikisi birden değil.

ÖLÇÜ:          yatay 1280×720 (master 2560×1440'tan ölçeklenir)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek harf
> istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic frame, 16:9, hard science-fiction, shot on a 32mm
spherical lens from a locked-off camera 60 metres out at eye level.

In the left third, small and clearly in motion: a woman in her late thirties in
a bone-grey pressure suit, matte and lightly scuffed, gripping a taut line with
both gloves, body angled forward mid-glide, one arm reaching. The visor is
optically clear glass with zero tint and zero mirror coating; her face is
readable through it. The back of the suit is one continuous smooth panel from
collar to hip, carrying nothing. She occupies 9 percent of frame height.

Filling the background right two thirds: a spherical shell of torn hull metal,
40 metres across and 6 metres thick, built of roughly 260 separate fragments —
flat panels, bent struts, loose bolts, cut strap ends — every one of them
absolutely motionless and evenly spaced, holding the curve of the sphere. They
are ordinary dead machined objects: nothing here has limbs, joints, a head,
eyes or a face, and nothing grows, opens, folds or reaches.

COMPOSITION: figure on the left third line, low; the shell mass filling right
and upper right; deep black negative space through the lower right corner. The
figure's silhouette breaks cleanly against empty black, not against the shell.
Safe area: nothing story-critical in the bottom 15 percent or the right 12
percent of frame (platform UI bands).

LIGHTING: one distant star just outside the upper right corner of frame, hard,
parallel and white. Every fragment carries a bright hard rim on its upper edge;
every shadow is absolutely black with a razor edge and no second light fills
them. High contrast, deep blacks, no fill.

NEGATIVE: Exactly one human character — no duplicates, no clones, no second
person, no second silhouette in any shadow. 0% bloom, no glow filter, no soft
focus, no dreamy haze; every surface keeps visible texture. Photorealistic skin
pores and fatigue retained — no airbrushing, no waxy texture, no smoothed skin.
No readable text, letters, digits, numbers or symbols on any surface in frame —
not on the suit, not on the equipment, not on any fragment; nothing here has
been measured, labelled or marked by anyone. No subtitles, no captions, no
title card, no watermark, no HUD overlay, no lens data, no name label. No
anamorphic flare, no horizontal streak flare; spherical lens only. No Unreal
Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with
35mm film grain.

Output: 16:9, 2560×1440, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
   küçük insan silueti  ↔  taneli devasa kabuk
   (bir kişi, ve arkasında kımıldamayan bir kalabalık)

⛔ HOOK §8: bu test artık TEK yük taşıyıcıdır ve GÖZLE değil MAKİNEYLE de
   koşulur. Kare 120 px genişliğe indirilir, kontrast ve entropi ölçülür:

     ffmpeg -i kapak.jpg -vf scale=120:-1 kapak_120.png
     ffmpeg -i kapak_120.png -vf "signalstats,metadata=print:key=lavfi.signalstats.YDIF" -f null -
     ffmpeg -i kapak_120.png -vf entropy -f null -

   Figür 120 px'te tek bir koyu leke olarak ayrışmıyorsa → yeniden üret.
   Kabuk 120 px'te düz gri bir kütleye dönüşüyorsa (tanecik gitmişse) →
   yeniden üret: kapağın vaadi TANECİKLİLİKTİR.

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel + yukarıdaki iki komutla yapılır.)
```

---

## 🚦 KABUL / RET (`PAKETLEME §6`)

```
□ Vizörde net bir yansıma VAR ya da duruş belirgin bir hedefe yönelmiş
  → duruş: gövde ve bakış screen-right'a, kabuğa kilitli ✅
  (yansıma bu filmde yok ve olamaz — vizör optik berrak)
□ Silüet ile arka plan arasında keskin kontrast var
  → figür siyah boşlukta kırılıyor, kabuğun önünde değil ✅
□ Kapaktaki kompozisyon, ölçek, palet ve ışık 0:00-0:10 bloğunda birebir var
  → kapak anı S0'ın kendi karesi ✅
□ Kapak, başlığın soyut sorusunu fiziksel bir ana çeviriyor
  → "still swarm" → 260 parça, hiçbiri kımıldamıyor ✅
□ Kapak, başlığın söylediğini görsel olarak TEKRAR ETMİYOR
  ⚠️ RİSK BURADA: başlık "still" diyor, kapak da hareketsizlik gösteriyor.
     Merak boşluğunu açan şey figürün HAREKETİDİR — kapakta tek hareketli
     şey odur ve "o oraya neden gidiyor?" sorusunu kapak tek başına kurar.
     Bu satır yayından sonra CTR ile sınanır (Kart Y).
```
