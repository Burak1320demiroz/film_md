# 🎬 APEXAIC — Stüdyo Logo İntrosu (10 saniye)

> **Amaç:** Her filmin başına konacak 10 saniyelik marka introsu.
> **Üretim akışı:** Önce image (logo dosyası REFERANS GÖRSEL olarak eklenir),
> imaj onaylanınca video. Video, imajın devamıdır — aynı kompozisyon, aynı ışık.
>
> ⚠️ **A1 notu (bilinçli sapma):** Negatif çekirdekteki "no readable text"
> yasağı bu dosyada **"referans logodaki mark hariç"** olarak uyarlanmıştır.
> Logo intro'nun konusu metnin kendisidir; yasak yalnız logo DIŞI her yazıyı
> kapsar. Bu sapma bilinçlidir, film promptlarına taşınmaz.
>
> **prompt_kontrol.py bilinçli sapma gerekçesi (D74):** Bu dosya film değil
> marka introsu — sahnede insan yok ("exactly one human" imzası kasıtlı yok),
> metin yasağı logoya izin verecek şekilde uyarlandı, uzunluk bantları film
> bantlarına göre sapabilir. FIX bulguları bu üç başlıkta kabul edilmiştir.

---

## 🎨 KONSEPT

Kara boşlukta fırçalanmış koyu çelik bir plaka. APEXAIC logosu plakaya
işlenmiş kabartma metal amblem olarak durur. Tek sert ışık huzmesi ambleme
vurur; toz zerreleri huzmede süzülür. Kamera 10 saniyede yavaşça yaklaşır,
ışık amblemin pahlı kenarlarında gezinir, son karede amblem tam aydınlık ve
sabit kalır. Fotogerçekçi, 35mm film greni — kanalın film estetiğiyle aynı dil:
bloom yok, CGI parlaklığı yok, doku her yerde.

---

## 📸 IMAGE PROMPT (16:9) — logo dosyasını referans görsel olarak ekle

```
SCENE:
A cinematic studio-logo emblem shot: the logo from the attached reference
image, machined as a raised dark-metal emblem mounted on a massive brushed
steel plate, lit by a single hard beam in a black void.

ENVIRONMENT:
Pure black background, no visible walls or horizon. A large brushed
gunmetal-steel plate fills the frame behind the emblem, its surface showing
fine horizontal machining lines and subtle wear. Sparse fine dust motes
hang in the air, visible only where they cross the light beam.

SUBJECT:
The logo reproduced EXACTLY as in the attached reference image — identical
letterforms, identical proportions, identical mark, nothing added and
nothing removed — rendered as a machined metal emblem raised about 3
centimeters off the plate. Emblem surfaces are dark gunmetal with brushed
micro-texture; every edge has a small chamfer that catches the light as a
thin hard specular line. The emblem is bolted to the plate with four small
recessed hex bolts at its corners.

CAMERA:
Shot on a 50mm lens from a fixed position two meters away, f/4, dead-center
composition, emblem centered and occupying roughly one third of the frame
width, 16:9. Physically accurate perspective, correct engineering
proportions.

LIGHTING:
A single hard key light from upper screen-left at 45 degrees, sharp
directional falloff across the plate. Speculars stay small and hard on the
chamfered edges. The plate darkens smoothly toward the frame edges. 0%
bloom, no glow filter, no haze — every surface keeps visible texture.

PHYSICS:
Normal gravity. Dust motes drift and settle slowly with continuous physical
momentum. The emblem and plate are rigid, static, perfectly stable.

NEGATIVE:
No text, letters, digits or symbols anywhere in frame EXCEPT the logo from
the attached reference image. No extra letters, no invented glyphs, no
tagline, no subtitle, no lower third, no watermark, no HUD overlay, no lens
data text. Logo geometry identical to the reference — no warped, melted or
restyled letterforms. No lens flare, no bloom, no glow filter, no soft
focus. No Unreal Engine look, no CGI aesthetic, no video game aesthetic.
Photorealistic with 35mm film grain. Environment static and stable — no
melting surfaces, no warping, no swimming texture.
```

---

## 🎥 VIDEO PROMPT (10 saniye, 16:9) — onaylanan imajdan başlar

```
MOTION (10 seconds, 50mm, slow push-in from 2.0 to 1.4 meters):
0s — Opening frame identical to the source image: the machined metal
emblem centered on the brushed steel plate, lit by a single hard beam from
upper screen-left, sparse dust motes drifting through the light.
2s — The beam begins a slow sweep from screen-left toward screen-right;
thin hard specular lines travel across the chamfered edges of the
letterforms one by one, the brushed texture of the plate raking into
relief as the light passes.
5s — Slow push-in continues; the beam reaches center and its sweep slows,
the full emblem now evenly lit, speculars small and hard, dust motes
settling downward under gravity.
8s — The light locks in place, fully front-lit and steady; the emblem
holds dead center, every letterform sharp and readable, the plate
darkening smoothly toward the frame edges.
10s — Hold on the fully lit emblem, completely static and stable. No cuts.
Single unbroken take, no transitions, no dissolves, no fades, no camera
teleportation, no angle change. No text anywhere in frame except the
emblem itself — no tagline, no subtitle, no watermark, no title card, no
end card. Logo geometry stays identical in every frame — no warping, no
morphing, no restyling of the letterforms. 0% bloom, no glow filter, no
lens flare; all speculars stay small and hard. Dust obeys gravity with
continuous momentum — never hovering, never frozen, never swirling.
Environment static and stable. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.
```

---

## 🎥 ALTERNATİF VİDEO — karanlıktan açılış (araç SON KARE destekliyorsa)

> Flow'un "frames to video" gibi son-kare kabul eden bir akış varsa: yukarıdaki
> imaj **son kare** olarak verilir, video karanlıktan açılır. İlk-kare akışında
> bu prompt KULLANILMAZ (imajla çelişir).

```
MOTION (10 seconds, 50mm, slow push-in from 2.0 to 1.4 meters):
0s — Near-total darkness; only the top edge of a raised metal emblem
catches a faint hard rim of light on a brushed steel plate. Sparse dust
motes drift where they cross the faint beam.
3s — A single hard beam sweeps slowly from screen-left across the plate,
raking light revealing the brushed texture and the chamfered letterforms
of the emblem edge by edge.
6s — The beam settles centered; the full emblem becomes readable, lit by
one hard key from upper screen-left, speculars small and hard; slow
push-in continues.
10s — The light locks steady; hold on the fully lit emblem, dead center,
completely static. Final frame identical to the source image. No cuts.
Single unbroken take, no transitions, no fades-from-black as an edit —
the darkness is in-scene lighting, the camera never cuts. No text
anywhere in frame except the emblem itself. Logo geometry identical in
every frame — no warping, no morphing. 0% bloom, no glow filter, no lens
flare. Dust obeys gravity with continuous momentum. Environment static
and stable. No CGI aesthetic. Photorealistic with 35mm film grain.
```

---

## 📱 9:16 DİKEY VARYANT — değişen satırlar

Aynı image + video promptları kullanılır; yalnız şu satırlar değişir:

```
CAMERA (9:16): Shot on a 50mm lens from a fixed position two meters away,
f/4, dead-center composition, emblem centered and occupying roughly two
thirds of the frame WIDTH, upper and lower thirds of the frame falling
into smooth darkness, 9:16 vertical. Physically accurate perspective.
```

Video prompt'ta `16:9` geçen ifade yoksa dokunma; push-in mesafeleri aynı kalır.

---

## 🔊 SES NOTU (üretim sonrası, kurguda)

- 0-2s: derin, düşük seviyeli oda tonu / uzak metalik rezonans
- 2-6s: ışık süpürmesiyle senkron yükselen tek ton (bloom yok, ses de "şişmesin")
- 8s: ışık kilitlenince tek kısa, tok metalik vuruş (logo damgası)
- 10s: sessizliğe düşüş — filmin ilk sahnesine temiz giriş
- Müzik üretimi: `kilavuzlar_ve_sistem_dosyalari/GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md`

---

## ✅ KULLANIM KONTROL LİSTESİ

```
□ Image üretiminde logo dosyası REFERANS GÖRSEL olarak eklendi mi?
□ Üretilen imajda letterform'lar referansla BİREBİR aynı mı?
  (harf sayısı, oranlar, mark — değilse video üretme, imajı yeniden üret)
□ İmaj onaylandı mı? → ancak o zaman video
□ Video son karesi sabit ve tam aydınlık mı? (filme temiz geçiş için)
□ 16:9 ve 9:16 ayrı ayrı üretildi mi? (yatay filmler / dikey shorts)
```
