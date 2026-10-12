# 📦 THE_MAYDAY_SEA — Kapak ve yayın paketi

> Kapak bölümü Türkçe notlar + İngilizce prompttan oluşur. Yayın paketi (başlık · açıklama ·
> etiketler · sabit yorum · vaat denetimi) ayrı dosyadadır ve **tamamen İngilizcedir**:
> `YAYIN_PAKETI.md` (06.10.2026).

---

## 1. KAPAK

<!-- kaynak: ODA/SAHIP_PLANI.md §9 "YouTube yayın paketi" (sahip, 12.10.2026). Plan ÜÇ başlık/kapak adayı verir (A · B · C) ve A'yı başlangıç tercihi yapar;
     YouTube Studio A/B/C testi için üçü de hazır tutulur. Hat A/B tek değişken ister → A planın tercihi; B ve C planın diğer adayları, tek değişken değil üç vaat.
     Promptlar plandan birebir; yalnız referans anahtarı `Reference <No> (<rol>)` öne alındı ve olumsuz kuyruk ("no text, logos or watermark") çıkarıldı (hat kuralı).
     F6 bu filmde açılmadı (sahip planı); F9'da kapak-tasarimcisi gerçek kareden final kapağı türetir, 160×90 kontrolü izleyici yapar. -->

```
SAHİP PLANI    Üç aday, ölçülmüş kazanan yok. A — imkânsız mekân + yardım çağrısı (dev yassı okyanus, küçük beyaz kapsül) · B — bir insanın geri dönüşü zor kararı
               (Mara'nın yüzü, kokpit camının ardında okyanus) · C — çağrının kaynağındaki çelişki (yarı batmış istasyon, kırık anten). Kapaklarda metin yoksa görüntü
               tek başına okunur; film adı küçük kimlik olarak eklenebilir. Ortadaki ses taklidi kapakta açıklanmaz. Sağ alt köşe sessiz (süre rozeti).
BAŞLIKLAR      A: An Ocean in Space Was Calling for Help | Sci-Fi Short Film · B: I Answered a Distress Call From an Ocean in Space · C: The Station Was Silent. The Ocean Was Calling.
AN             A: C01/C22 kompozisyonu (okyanus + kapsül) · B: C02/C18 (Mara kokpitte, kanopiden okyanus) · C: C03 (istasyon yanaşma tarafı, kapsül yok)
TEK İLİŞKİ     A: küçük kapsül ↔ dev yassı okyanus (ölçek) · B: Mara'nın yüzü ↔ camın ardındaki okyanus · C: sessiz istasyon ↔ onu tutan okyanus
BOŞ ALAN       sağ alt köşe sessiz (süre rozeti); A'da üst siyah uzay başlık katmanı için
REFERANS       A: Reference 2 (rescue pod) · Reference 4 (floating ocean) · B: Reference 1 (woman) · 3 (cockpit) · 4 · C: Reference 4 · 5 (station)
FİNAL          faz 9: gerçek kare → ~/film_medya/THE_MAYDAY_SEA/cikti/kapak_A.png (B · C testte ise kapak_B.png · kapak_C.png)
```

### Kapak A — imkânsız mekân ve yardım çağrısı (sahip tercihi)
```text
Reference 2 (rescue pod): take the ivory rescue pod with its orange nose band from it. Reference 4 (floating ocean): take the flattened oval ocean, its three black containment frames and the cyan boundary from it. A cinematic YouTube thumbnail, horizontal. The impossible floating ocean is a broad flattened oval water volume in open black space, not a globe or planet; its rippled top and translucent hanging underside are both clearly readable. It occupies most of the upper and central frame. Three thin rigid black containment frames and a faint cyan boundary remain visible. A recognizable ivory rescue pod with an orange nose band is in the lower-left foreground, large enough to read at phone size, facing the enormous ocean; maintain the scale contrast through perspective. Cold luminous teal water against clean dark space, bright ivory vessel, two primary focal objects, sparse stars, sharp coherent shapes, a single unified image. Keep the bottom-right visually quiet for the player duration badge.
```

### Kapak B — bir insanın geri dönüşü zor kararı
```text
Reference 1 (woman): take her face, the clear closed helmet and the ivory suit with navy shoulders from it, using the head-and-shoulders panel. Reference 3 (cockpit): take the canopy and console from it. Reference 4 (floating ocean): take the flattened teal ocean, its three black containment frames and the small half-submerged station from it. A cinematic YouTube thumbnail, horizontal. Tight three-quarter portrait of the woman at frame-left inside the rescue cockpit, clear closed helmet, the exact ivory suit and navy shoulders, focused worried eyes with a calm closed mouth. At frame-right through the canopy, a broad flattened teal ocean hangs in black space within the existing three black containment frames; a small half-submerged station is visible at its rim. Keep the ocean clearly an exposed water volume rather than a rocky planet. Strong readable ivory face lighting and teal water edge, restrained orange accents, clean separation between the two focal subjects, photorealistic, a single unified image. Leave the lower-right area free of critical details.
```

### Kapak C — çağrının kaynağındaki çelişki
```text
Reference 4 (floating ocean): take the suspended teal ocean, its rippled top, thick translucent underside and three black containment frames from it. Reference 5 (station): take the graphite three-module research station, its crooked dish antenna and dry docking port from it. A cinematic YouTube thumbnail, horizontal. Close exterior view of the recognizable graphite three-module research station lying half submerged at the edge of an enormous suspended teal ocean, with open starfield clearly beyond it. The crooked dish antenna at frame-left has a visibly broken support and disconnected feed cable. A dry circular docking port extends at frame-right above the waterline, empty. One faint amber emergency light provides a warm focal accent; most station windows are dark. Behind it, the ocean's rippled top and thick translucent underside make the impossible location understandable; preserve the three black containment frames. Station and water are the two main shapes, strong readable contrast, realistic metal. Keep the bottom-right quiet.
```

Plan notu (kod bloğu dışında): "Gerçek NASA görüntüsü", görülmeyen bir canavar ya da filmde olmayan insan kalabalığı gibi vaatler eklenmez. Film adından çok izleyicinin
anlayacağı olay başlığın başında yer alır. A/B/C testi masaüstü YouTube Studio'da eşzamanlı, izlenme süresiyle değerlendirilir; test sürerken başlık değiştirilmez.

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum, Shorts metni ve vaat denetimi orada,
yapıştırmaya hazır İngilizce bloklar hâlinde. Denetim: `film_dogrula.py <FILM> --bolum yayin`.
F9 kaynağı: `ODA/SAHIP_PLANI.md` §9 — İngilizce açıklama, 3 hashtag (#SciFi #ShortFilm #SpaceHorror), sabit yorum ("Would you have answered the first call?"),
kısa etiket listesi. Yayin ajanı bunları kanal şablonuna (sabit blok · karakter sayımı) oturtur; vaatler tamamlanan üretimin gerçekten kullandığı yöntemlerle eşleşmeli (plan).
