# 🖼️ BENI_HATIRLAMA — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S0 (≈0:04)   ·   gerekçe: filmin sorusunun kendisi — fırtına önünde kasksız bir kadın. 120 px'te okunan
                  iki şey kalıyor: koyu siluet + tek doygun renk (sarı atkı) ve arkada koyu duvar. Yüz yok, yüz testine
                  girmiyor; kontrastlı siluet (PAKETLEME §1 üç odaktan ②). Kadın sağ üçte birde — başlık yazısına sol alan kalır.
BAŞLIKLA UYUM:  kapak "burada nefes alınamaz ama o kasksız duruyor" der; başlık "Close Your Eyes, Dad" onu tanıyan birini ve
                  bir oyunu vaat eder → ikisi AYNI soruyu farklı yandan sorar (kim bu? neden tanıyor?) · spoiler 0:
                  canlı, ısı görüşü, atkının akıbeti kapakta yok (`BENI_HATIRLAMA_YAYIN_PAKETI.md` → CROSS-PLATFORM NOTES)
PLAN B KAPAK:   S5 — omuz üstünden: giysili adam solda, uzakta sarı atkılı kasksız kadın sağda, aralarında kapanmayan mesafe
                  (iki siluet 120 px'te okunur; adam figürü ölçek ve tehlike taşır). Kart Y yayından ÖNCE hazır olmasını ister (§7.2).
ÖLÇÜ:           yatay 1280×720 (16:9) · dikey kesit 1080×1920 ayrı kompozisyon (dikey recut kapağı, YAYIN_PAKETI VERTICAL RECUT)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
IN FRAME: full body
A dark sand plain under a low, still cloud deck. Exactly one semi-transparent woman figure in her late twenties stands in
the right third with her back to the lens: long dark brown hair tied low at the nape, a dark navy wool sweater, and a yellow
wool scarf whose end lifts in the wind toward screen-right. She is lit by the same flat grey daylight as the sand; her hair
and sweater keep ordinary colour and texture, and the dune crest behind her shows through her shoulders at about half
strength. Far off on screen-left a small squat lander, its hatch angled camera-right, stands in front of a long dark storm
wall that fills the lower sky. The yellow scarf is the only saturated colour in the picture.

COMPOSITION: the woman and scarf in the right third, head below the top tenth; the left half kept calm and dark for the title
              added in post; nothing important in the bottom fifth (platform UI) or the top tenth.
LIGHTING:    diffuse daylight through thick cloud, one brighter patch high on screen-left, soft shallow shadows, the storm wall a
             deep slate band; high contrast between the dark sweater and the pale horizon band.
CAMERA:      35mm lens, 0.5 m above the ground, 4 m from her, low angle medium long shot, deep focus.
NEGATIVE:    Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps
             visible texture. Photorealistic with 35mm film grain, no CGI or video-game look. No light rays, no halo and no haze
             around the woman figure. No tilt-shift look, no miniature read on the lander. No text, no letters, no numbers, no
             watermark, no HUD overlay.

Output: 16:9, 1280×720 and 4K master, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey: koyu bir kadın silueti + sarı atkı, arkasında koyu bir duvar

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)
```
