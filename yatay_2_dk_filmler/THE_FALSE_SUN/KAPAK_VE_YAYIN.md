# 📦 THE_FALSE_SUN — Kapak ve yayın paketi

> Kapak bölümü Türkçe uygulama notları ve İngilizce prompttan oluşur (`ODA/SAHIP_PLANI.md` §10 kaynaklı).
> Yayın paketi `YAYIN_PAKETI.md` dosyasındadır (İngilizce).

---

## 1. KAPAK

```
DENEY SORUSU   Tehdit yakınlığı ve pilotun yüz ifadesi 160×90'da tıklama oranını nasıl etkiler?
DEĞİŞKEN       Kürenin boyutu ve yansıması (C04 vs C05 karesi)
SABİTLER       Kamera açısı (28mm tek sabit kokpit kamerası) · Nia vizör ardında · konsol ve iki dikme · beyaz gerçek güneş
AN             A: çekim C04 · B: çekim C05 (aynı sabit kamera karesi; yeni açı veya canavar yüzü eklenmez)
TEK İLİŞKİ     160×90'da okunacak tek şey: kokpit içindeki pilotun yüzü ve camın hemen ardındaki yaklaşan dev amber güneş
BOŞ ALAN       Sağ alt köşe (süre rozeti) boş; merkezde film adı için iki satır alan
FİNAL          faz 9: gerçek kare → ~/film_medya/THE_FALSE_SUN/cikti/kapak_A.png
```

Uygulama notu (sahip planı):
- C04 veya C05'in aynı sabit kamera karesinden okunur bir görüntü seç.
- Pilotun vizörlü yüzü, iki ışık ve yaklaşan amber küre görülsün. Yeni açı veya filmde olmayan yaratık yüzü ekleme.
- Üzerine sonradan İngilizce film adını merkezde iki satır ekle: `THE FALSE SUN`
- Soğuk mavi ile amber karşıtlığını koru; yazı okunur kırık beyaz veya altın tonunda olsun. Önemli yazıyı üst/alt kenarlara yaslama.

### Kapak A (C04 karesi)
```text
Photorealistic cinematic live-action film still from inside a spacecraft cockpit, horizontal 16:9, fixed 28mm single camera bolted to the port wall. At left, a 34-year-old female pilot sits in a navy seat wearing an ivory pressure suit and round helmet with a completely clear closed visor; her alert face and dark brown eyes look toward the broad forward canopy with restrained dread. Her right glove holds a silver throttle, left glove holds an upright orange lever. The canopy has two dark graphite mullions. Outside the glass at upper-right, an intense glowing amber-gold spherical false sun looms close, casting warm amber reflections across the glass and her visor, contrasting sharply with the deep cold blue shadows inside. High contrast, sharp skin texture, fine 35mm grain, no text or watermark.
```

### Kapak B (C05 karesi)
```text
Photorealistic cinematic live-action film still from inside a spacecraft cockpit, horizontal 16:9, fixed 28mm single camera bolted to the port wall. At left, the female pilot in her ivory suit and clear visor sits rigid in her seat, gazing between her low console and the canopy. Outside the forward canopy at upper-right, the menacing amber-gold sunlike orb is even closer and larger, burning with intense halo illumination that floods the cockpit in golden-amber highlights over cold cyan battery emergency lights. At upper-left outside the glass, a tiny distant white sun stays cold and still. Stark visual contrast between cold cyan interior and burning amber predator outside. No text, logos, or watermark.
```

---

## 2. YAYIN PAKETİ → `YAYIN_PAKETI.md`

Başlık seçenekleri, açıklama, etiketler, sabit yorum ve vaat denetimi `YAYIN_PAKETI.md` dosyasındadır.
Denetim: `python3 uretim_hatti/araclar/film_dogrula.py yatay_2_dk_filmler/THE_FALSE_SUN --bolum yayin`
