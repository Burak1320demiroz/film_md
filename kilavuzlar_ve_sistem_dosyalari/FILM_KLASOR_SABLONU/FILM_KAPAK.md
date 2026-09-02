# 🖼️ <FILM_ADI> — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S⬜   ·   gerekçe: ⬜
                ⛔ "en güzel sahne" gerekçe değildir. Tek sınav 120 px'tir:
                  yüz 120 px'e inince gri lekedir, iki siluet okunur.
BAŞLIKLA UYUM:  ⬜ kapak neyi vaat ediyor, başlık aynı şeyi mi söylüyor
                  (`<FILM_ADI>_YAYIN_PAKETI.md` → CROSS-PLATFORM NOTES)
PLAN B KAPAK:   ⬜ S⬜ — Kart Y yayından ÖNCE hazır olmasını ister (§7.2)
ÖLÇÜ:           ⬜ dikey 1080×1920 · yatay 1280×720
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
⬜

COMPOSITION: [güvenli alan — platform UI'ın kapattığı bantlara hikâye
              kritik hiçbir şey düşmez]
LIGHTING:    ⬜
NEGATIVE:    [KILAVUZ_REHBERI §5 negatif çekirdek] no text, no letters,
             no numbers, no watermark, no HUD overlay.

Output: ⬜, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey: ⬜

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — hiç çalıştırılmamıştı;
 test manuel yapılır.)
```
