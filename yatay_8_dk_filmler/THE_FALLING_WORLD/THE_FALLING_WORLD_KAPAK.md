# 🖼️ THE_FALLING_WORLD — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S41 · 7:00+4 s   (sahibin seçimi — V42)
                gerekçe: 120 px'te İKİ AYRI LEKE okunur — kapı eşiğinde turuncu
                gövde sağ üçte birde, asılı beyaz gövde sol alt üçte birde, ikisi
                arasında tek bir kol. Altta yarılmış siyah zemin, üstte merceklenmiş
                halka. Bu filmde yüz zaten hiç yok, yani 120 px sınavı ilk günden
                beri kadrajın TEK sınavıydı: iki leke ve aralarındaki boşluk.
                Optik: X kurulumu · insan 1,9 m → kare yüksekliğinin %35'i (380 px)
                → 120 px'e indirgendiğinde gövde ~42 px, siluet ayrık kalır.
BAŞLIKLA UYUM:  kapak "biri düşüyor, biri tutuyor" vaat ediyor; başlık
                (THE FALLING WORLD) düşen ŞEYİN gezegen olduğunu ekliyor —
                ikisi aynı olayı iki ölçekte söylüyor, çelişmiyor
                (`THE_FALLING_WORLD_YAYIN_PAKETI.md` → CROSS-PLATFORM NOTES)
PLAN B KAPAK:   S00 · 0:04 — bilek tutuşu. Tıklayan izleyici İLK ON SANİYEDE aynı
                kareyi görür; spoiler bütçesi sıfır. A/B testinin ikinci kolu.
ÖLÇÜ:           yatay 1280×720 (kaynak 3840×2160'tan kırpılır)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic still, 35mm film grain. Wide and low, out beyond the open door of a
small white ship and below its sill. The hull fills the upper right of frame. A man
in a burnt-orange hard-shell pressure suit with black upper arms is braced across the
inner steps at the door mouth, one arm reaching down. In the lower left a man in a
dirty off-white hard-shell pressure suit with cobalt-blue shoulder caps hangs from the
sill, his left cuff dented and wrapped in silver tape and held against his chest. An
orange glove is closed round the hard grey cuff of his right wrist. A thin yellow line
runs from his belt down to a tangle of fallen rail below. Both helmets carry one flat
front pane in a thick dark-grey rim, each pane fully opaque matte black. Beneath them
the rust-brown rock ground is split into separating plates with wide black gaps. High
above, one lensed bright ring hangs at a fixed place in a deep brown-violet sky.

COMPOSITION: two clearly separated silhouettes on opposite thirds with one arm
             bridging them; the split ground fills the bottom third and the bright
             ring sits in the top right. [güvenli alan — platform UI'ın kapattığı
             alt 15% ve sağ alt köşeye hikâye kritik hiçbir şey düşmez; süre damgası
             ve kanal rozeti oraya biner]
LIGHTING:    one hard sun out of frame to the upper left, the white hull bright along
             its top, the hanging body partly in the ship's shadow, shadow edges soft.
NEGATIVE:    [KILAVUZ_REHBERI §5 negatif çekirdek] Exactly 2 human characters, no
             duplicates, no third person. No face, no eyes and no mouth behind either
             pane, and both panes stay fully opaque. No miniature read, no tilt-shift.
             no text, no letters, no numbers, no watermark, no HUD overlay.

Output: 16:9 3840×2160 (1280×720'a küçültülür), no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey: BİR GÖVDE ASILI, BİR GÖVDE ONU TUTUYOR.
(Renk değil, POZİSYON: üstte bir leke, altta bir leke, arada tek bir kol hattı.)
⛔ "Gemi" okunmasına gerek YOK. "Gezegen çöküyor" okunmasına gerek YOK.
   Bu ikisi başlığın işi; kapağın işi TEK İLİŞKİDİR.

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)
```
