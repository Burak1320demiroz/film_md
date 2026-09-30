# 🖼️ <FILM_ADI> — KAPAK · iki aday, tek deney

**Kaynak:** `FILM_KAPAGI_KILAVUZU.md` · akış adım 10 (PLAN'dan sonra, prompt üretiminden önce)
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir, üretimden sonra aranmaz.
**Sayılar:** `apexaic/DIS_SAYILAR.md` §1 (ölçü · format · A/B varyant · CTR yorumu).

## 🔒 SABİTLER — iki adayda da DEĞİŞMEZ (kılavuz §2)

```
FİLMİN RESMÎ ADI:          <FILM_ADI>
KAPAK METNİ (post katmanı): ⬜ film adı · İngilizce · promptta tek harf yok
FİGÜR SAYISI:              ⬜ (anın kadrosu — NEGATIVE count cümlesiyle aynı)
VİZÖR KURALI:              ⬜ opak → yüz/göz/yansıma yok · berrak → D79 cümlesi yalnız `face` kadrajda
KİMLİK REFERANSLARI:       ⬜ Character/Vehicle Bible cümleleri birebir (PLAN → BIBLE'LAR)
MEKÂN / DÜNYA ÇAPASI:      ⬜ World Bible cümlesi (gök kadrajdaysa)
KORUNACAK HİKÂYE BİLGİSİ:  ⬜ finalde cevaplanan şey kapakta yok (PAKETLEME §5 spoiler bütçesi)
TUVAL / TESLİM:            16:9 · 3840×2160 kaynak → DIS_SAYILAR §1 · dikey/Shorts kapağı ayrı kompozisyon (⬜ gerekiyorsa)
HEDEF İZLEYİCİ:            ⬜ (= <FILM_ADI>_YAYIN_PAKETI AUDIENCE)
```

## 🎯 AN ADAYLARI — PLAN'dan (vuruş tablosu · İPTAL KAPISI · HOOK/DORUK/FINAL) — kılavuz §3

| aday | sahne · saniye | anlaşılan olay | açık kalan soru | küçük boyut riski | spoiler |
|---|---|---|---|---|---|
| A | S⬜ · ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| B | S⬜ · ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| C (yedek) | S⬜ · ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

```
TEK DENEY SORUSU:  ⬜ (örn. "izleyici tehlikeye mi, çıkışa mı tıklıyor?")
DEĞİŞKEN:          ⬜ vaat tipi / zaman / odak / ölçek — kılavuz §4 menüsünden BİRİ
SABİTLER:          palet · ışık dili · kimlik · ad · oran · başlık (A ve B aynı başlıkla test edilir)
BAŞLIKLA UYUM:     ⬜ kapak neyi söylüyor · başlık neyi ekliyor · ortak vaat (<FILM_ADI>_YAYIN_PAKETI TITLE)
160×90'DA OKUNAN TEK İLİŞKİ:  A: ⬜   B: ⬜
```

---

## 🅰️ ADAY A — S⬜ · ⬜(değişkenin A değeri)

> ⛔ Metinsiz üret; tipografi post'ta [Ders 9/34/45]. ⛔ `📸 GÖRSEL PROMPT` başlığı KULLANILMAZ — kapak sahne değildir.

```
COVER A — <FILM_ADI> · S⬜ · ⬜
IN FRAME: ⬜
Exactly ⬜ human character(s) in frame.
⬜ <the one relationship that must read at thumbnail size, with a number>

⬜ <body — Bible strings verbatim · object/obstacle/goal · object-relative scale · damage/wear state of this scene · world anchor if sky · one balanced pose, no motion>
COMPOSITION: ⬜ primary element at x%,y% · secondary element · direction and the space left for it · title overlay region empty · bottom-right badge corner and bottom band carry nothing story-critical
CAMERA: ⬜ <the scene's letter sentence when the moment is a scene>
LIGHTING: ⬜ <Lighting Bible for this place; the edge separation that keeps the figure off the background>
NEGATIVE: ⬜ <7 core sentences, film scope> No text, letters, numbers, logos, HUD or watermark anywhere. ⬜ <≤2 cover-specific>

Output: 16:9, 3840×2160, no text, no watermark.
```

## 🅱️ ADAY B — S⬜ · ⬜(değişkenin B değeri)

```
COVER B — <FILM_ADI> · S⬜ · ⬜
IN FRAME: ⬜
Exactly ⬜ human character(s) in frame.
⬜

⬜
COMPOSITION: ⬜
CAMERA: ⬜
LIGHTING: ⬜
NEGATIVE: ⬜ No text, letters, numbers, logos, HUD or watermark anywhere. ⬜

Output: 16:9, 3840×2160, no text, no watermark.
```

---

## ✅ KONTROLLER — üretimden sonra, elle (kılavuz §7)

| kontrol | A | B |
|---|---|---|
| kaynak çözünürlük: el · temas · ekipman · figür sayısı · kimlik | ⬜ | ⬜ |
| 320×180: olay + (post) ad birlikte okunuyor | ⬜ | ⬜ |
| 160×90: TEK ilişki ayırt ediliyor | ⬜ | ⬜ |
| gri ton: hiyerarşi duruyor | ⬜ | ⬜ |
| açık / koyu arayüz · gerçek telefon | ⬜ | ⬜ |
| süre etiketi / rozet alanı boş | ⬜ | ⬜ |

Okunmuyorsa → yeniden üret. Hiçbir şey kapağı kurtarmaz.

## 🧪 YAYIN TESTİ VE ÖĞRENME (kılavuz §10–§11 · Kart Y · 08_YAYIN_PERFORMANS_TABLOSU)

```
DOSYALAR:            <FILM>_YT_EN_A_v1.png · <FILM>_YT_EN_B_v1.png  (teste giren dosya üzerine yazılmaz)
TEST:                Studio A/B · A + B aynı başlıkla · başlangıç ⬜ · bitiş ⬜ · özellik erişimi ⬜
PLATFORM SONUCU:     ⬜ açık kazanan / benzer / belirsiz (belirsiz = kazanan yok)
SEÇİLEN ADAY:        ⬜   GEREKÇE: ⬜
DESTEKLENEN BULGU:   ⬜   BELİRSİZ KALAN: ⬜
SONRAKİ KAPAKTA DENENECEK DEĞİŞKEN: ⬜
```
