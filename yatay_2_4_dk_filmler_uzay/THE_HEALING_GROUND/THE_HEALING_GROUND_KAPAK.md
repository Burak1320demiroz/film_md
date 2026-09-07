# 🖼️ THE HEALING GROUND — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` §1 — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S0 · 0:04   ·   gerekçe: bu kare filmin novum'unu TEK KARE'de
                taşıyan ilk andır — diz çökmüş koyu figür, eldivenlerinin
                altında koyu disk, diskin kenarından dimdik kalkan beyaz buhar
                yakası ve arkada ufka giden alçak beyaz kubbe dizisi.
                ⛔ "en güzel sahne" gerekçe değildir; bu kare PAKETLEME §1'in
                  iki şartını birden tutuyor: (a) ilk 10 saniyelik bloktan
                  seçildi — izleyici tıkladıktan 4 saniye sonra kapağın
                  aynısını hareketli görüyor, vaat aynı saniyede doğrulanıyor;
                  (b) tek kaynaklı yumuşak ışıkta koyu gövde / soluk zemin
                  kontrastı 120 px'te ayrışıyor.
BAŞLIKLA UYUM:  Kapak "zeminden bir şey kalkıyor ve bir adam ona bakmıyor"
                diyor; başlık (THE HEALING GROUND / "Nothing warm stays on
                this ground") aynı yere bakmayı söylüyor: ZEMİNE.
                ⛔ Kapak başlığın söylediğini TEKRAR ETMİYOR: kapakta
                  "kapanma" henüz tamamlanmamış, buhar yakası daha ayakta.
                  Merak boşluğu kapağın kendisinde duruyor.
PLAN B KAPAK:   S12 · 2:06 — makro: kapanmamış koyu disk, soluk kenar bir el
                genişliği ötede, kalkan ön kenarın altında bir çift koyu göz.
                (Kart Y yayından ÖNCE hazır olmasını ister — §7.2)
                ⚠️ Plan B SPOILER BÜTÇESİNİ zorlar: gözler filmin son
                  vuruşudur. Yalnız A kapağı 48 saatte ölçülüp düşerse ve
                  tek değişken kuralı gereği BAŞLIK sabit tutulacaksa açılır.
ÖLÇÜ:           yatay 1280×720 (yükleme 1920×1080'den küçültülür)
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek harf
> istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir ve
> dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic live-action still, 35mm film grain, horizontal framing.

Exactly one human character — no duplicates, no clones, no second person, no
reflection or shadow of anyone else. A man in his fifties, grey hair, deep
lines at the outer eyes, sealed in a matte dark slate-grey pressure suit,
down on one knee in the right third of the frame, both gloves stacked flat on
a dark blued-steel disc the width of his palm. A bold ochre-yellow band is
wrapped all the way around his RIGHT forearm and all the way around his RIGHT
thigh. The visor is optically clear glass with zero tint, zero mirror coating
and zero reflection of the environment, and his face is fully readable
through it; his eyes are down on his own gloves, not on the lens. The back of
the suit is one continuous smooth panel from collar to hip, carrying nothing.
No bare skin anywhere — none above the collar, none at the wrists between
glove and sleeve, none at the ankles between boot and leg.

A thin white collar of vapour stands straight up around the rim of the disc,
half the height of his glove, bright against the dark suit and made of a few
dozen separate motes. Behind him, running back into the left third of the
frame and shrinking to nothing at a hard flat horizon, a row of low white
domes, evenly spaced, each about the size of a dinner plate. The floor is a
fine pale mat the colour of dry bone. Above the horizon there is only
unbroken amber-brown haze — no sun disc, no beam, no bright spot.

COMPOSITION: the kneeling figure occupies the right third; the row of domes
leads the eye from the lower left corner to the horizon; the vapour collar
sits at the optical centre. The upper fifth and the lower fifth of the frame
carry nothing but haze and empty crust — platform interface bands cover no
story-critical element. Horizon level, in the lower third.

LIGHTING: soft shadowless daylight arriving from the whole sky dome; shadows
shallow, soft-edged, never black. A low rim of sky-light separates his
shoulders and helmet from whatever is behind him; his silhouette never merges
with the background. 0% bloom, no glow filter, no lens flare.

NEGATIVE: exactly one human character, no clones, no second person. 0% bloom,
no glow filter, no soft focus — every surface keeps visible texture. No
readable text, letters, digits, numbers or symbols on any surface, patch or
sign, and none on the ground or any natural surface in frame. No scale marks,
no graduation ticks, no engraved characters of any kind. No HUD overlay, no
lens data, no name label, no subtitle, no lower third, no watermark. No
canyon walls, no hills, no rock formations. No liquid, no wet surface, no
hovering particles. No Unreal Engine look, no CGI aesthetic.

Output: 16:9, 1920x1080, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
  KOYU DİZ ÇÖKMÜŞ GÖVDE + ÖNÜNDE DİMDİK DURAN BEYAZ BİR ŞEY
  (ikincil, hâlâ okunmalı: sol tarafta geriye giden beyaz nokta dizisi)

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — test manuel yapılır.)

⛔ HOOK §8 GEREĞİ MAKİNEYLE DE KOŞULUR (0. kare aynı karedir):
   ffmpeg -i kapak.png -vf scale=120:-1 kapak_120.png
   → kontrast/entropi ölçülür; koşulmadıysa madde işaretlenmez.
```

## 🚫 KAPAK RET ŞARTLARI (PAKETLEME §2)

```
□ Karakter kadrajın ortasında BOŞLUĞA bakıyor mu?      → HAYIR (bakışı kendi
  eldiveninde, ve eldiveninin altında olay var)
□ Ön plan ile arka plan aynı ton bandında mı?          → HAYIR (koyu gövde /
  soluk zemin; ayrıca beyaz buhar üçüncü bir ton)
□ Kapak, başlığın söylediğini görsel olarak TEKRAR mı ediyor?
                                                        → HAYIR (başlık zemini
  işaret ediyor, kapak zeminin YAPTIĞI şeyi yarıda gösteriyor)
⭐ YÜZSÜZ KAPAKTA ÜÇ ODAK'tan ikisi kullanıldı: ② YÜKSEK KONTRASTLI SİLÜET
  (koyu gövde / soluk ova) + ③ ÖLÇEK (kubbe dizisinin ufka gidişi).
  ① VİZÖR YANSIMASI kullanılmadı — bu filmin vizörü tasarım gereği
  yansımasızdır [D79]; yansıma eklemek Character Bible'la çelişirdi.
```
