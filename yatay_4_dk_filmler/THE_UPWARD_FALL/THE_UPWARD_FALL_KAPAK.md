# 🖼️ THE UPWARD FALL — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S0 · 0:06   ·   gerekçe: kapak anı 0:00-0:10 bandından
                seçilir [§1 sayısal kilit] ve bu kare filmin TEK KARE
                testini taşıyan karedir: avuçtan YUKARI ayrılan gri parça
                ile yanından AŞAĞI düşen yeşil yaprak aynı kadrajda.
                Vaat-teyit penceresi: kapağın vadettiği şey ekranda 0:06'da,
                yani ≤10 saniye içinde teslim edilir ✅
                ⛔ "en güzel sahne" gerekçe değildir; tek sınav 120 px'tir.
BAŞLIKLA UYUM:  Başlık "THE UPWARD FALL" düşmenin yönünü söylüyor; kapak da
                tam olarak onu gösteriyor — iki zıt yön tek karede. Kapak
                başlığı TEKRAR ETMİYOR, KANITLIYOR (§2 ret şartı ③ temiz).
PLAN B KAPAK:   S24 · 3:59-4:03 — dört uzuv 60 metrelik gövdeyi kavrarken,
                ön planda oturan figür. Kart Y yayından ÖNCE hazır olmasını
                ister (§7.2). Fraktal ölçek odağı (§2 ③) burada en güçlü.
ÖLÇÜ:           yatay 1280×720  (ve 1920×1080 kaynak)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic still, 16:9 landscape, poster-grade.

A man in a modern matte black surface suit kneels on one knee on the floor of
an enormous forest, turned three-quarters toward camera in the right third
of the frame. His helmet is a hard matte black shell with one flat front pane of optically clear glass, zero tint, zero mirror coating and zero reflection; a pale ring of light inside the helmet rim keeps his face fully readable through it and he is looking up. His open right glove is held out palm-up at chest height, and a hard black case rides flat on his right thigh with its flap fastened shut, a short ribbed grip standing out of it. Thirty centimetres
above the open palm, a pale grey piece of dead tissue the length of a hand
is travelling upward, clear of the hand, its lower face lit. Half a metre
to his left, a dark olive living leaf two point two metres long is falling
to the ground, tip first.

Behind and above him the trunks are forty metres across and four hundred
metres tall, pale grey-green and smooth-barked, running up out of frame and
holding the left two thirds; a narrow pale gap in the closed canopy sits
directly above the rising piece. The floor is a deep dry mat of fallen
fibre.

COMPOSITION: the kneeling figure and the open palm in the right third; the
nearest trunk and the vertical run of the forest in the left two thirds; the
rising grey piece on the third line, silhouetted against the lit trunk so
that it separates at small sizes. The matte black suit reads as a clean dark
silhouette against the pale grey floor and the gold-green shaft rims his
shoulders — the figure never merges with the background. Nothing story-critical in the bottom
sixth or the top sixth of the frame — those bands are covered by platform
interface.

LIGHTING: morning. Narrow gold-green shafts come straight down through the
canopy gaps; one crosses the palm and the rising piece. The dense air
scatters strong fill so shadows are soft-edged and deep but never fully
black. High separation between the pale grey piece and the darker trunk
behind it. No orange, no red.

NEGATIVE: Exactly one human character — no duplicates, no second person, no reflected figure, no extra shadow. 0% bloom, no glow, no soft focus, no haze; every surface keeps texture. Photorealistic skin — pores
and fatigue retained, no airbrushing, no waxy or plastic texture. No
readable text, no letters, no numbers, no symbols anywhere — not on the
suit, not on the bark, not on the floor; no scale marks, no survey markers.
No watermark, no HUD overlay, no lens data, no name label, no lower third,
no border, no frame, no logo. The suit has no back-mounted unit — the back
silhouette is flat. The rising piece is a solid object, not smoke, not
vapour, not embers, not a light effect. No wind, nothing flutters. No
liquid. No insects, no birds, no animal. No CGI or game look. Photorealistic, 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
   avucun üstünde duran açık gri leke ile onun altındaki koyu figür —
   yani "elinden bir şey ÇIKIYOR" okuması.
   🔧 REVİZYON 1 (siyah giysi) BU TESTİ GÜÇLENDİRDİ: mat siyah siluet soluk
   gri zeminin önünde 120 px'te daha temiz kesiliyor — PAKETLEME §2 ②
   "yüksek kontrastlı siluet" odağı artık kapağın birincil çapası.

Yardımcı okumalar (ikincil, kaybolabilir):
   · dev dikey gövdelerin ölçeği
   · düşen yeşil yaprak

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — test manuel yapılır.)

⛔ HOOK KILAVUZU §0② ile ORTAK: S0'ın 0. karesi zaten feed'de kapaktır ve
   120 px testi orada MAKİNEYLE koşulur (kare 120 px'e indirilip kontrast
   ve entropi ölçülür). Aynı kare, iki kapı — ikisi de üretimden sonra.
```

## 🚫 RET ŞARTLARI (§2)

```
□ Karakter kadrajın ortasında BOŞLUĞA bakıyor      → bu kapakta HAYIR:
  bakış yönü yükselen parçayı işaret ediyor, niyet okunuyor
□ Ön plan ile arka plan aynı ton bandında          → HAYIR: açık gri parça
  koyu yeşil-gri gövdenin önünde, ayrışma yüksek
□ Kapak, başlığın söylediğini görsel olarak TEKRAR ediyor → HAYIR:
  başlık yönü söylüyor, kapak o yönün KANITINI gösteriyor ve ikinci bir
  soru açıyor ("yukarıda ne var?")
```
