# 🔎 1 · TARAMA — klip içi teknik şüphe listesi (puansız)

> **Ne için:** ham klipte ya da taslak parçasında gözden kaçabilecek teknik hataları **zaman kodu ve
> kanıtla** önüne getirmek. Karar vermez, puan vermez; şüpheyi sen doğrularsın.
> Eski 15 merceğin şu yedisinin işini görür (06.10.2026'da arşivlendiler):
> ① kare · ② klip içi devamlılık · ⑥ fizik · ⑦ aksiyon · ⑧ efor · ⑨ kadraj · ⑭ hareket.
> **Nerede:** Gemini uygulaması, **her koşu yeni bir sohbette**.
> **Ne verilir:** iki moddan biri.
> - **VİDEO MODU** — tek ham klip ya da **en çok 90 saniyelik** taslak parçası. Model 60-90 saniyeden sonra
>   ayrıntıyı kaybeder (Video-MME); uzun filmi böl.
> - **KARE MODU** — kısa kusur şüphesi olan 2-3 saniye. Gemini videoyu **saniyede 1 kareyle** okur
>   (Gemini API belgesi; uygulamada ayar yok). 1 saniyeden kısa parmak erimesi videodan kaçar.
>   `python3 uretim_hatti/araclar/kareler.py cikar <klip> --hedef ~/film_medya/<FILM>/analiz/tarama/Cxx --aralik 0.25 --sayfa`
>   ile çıkan kontak sayfası verilir; kare etiketleri saniyedir.
>
> ⛔ Plan, hikâye, logline, çekim listesi VERİLMEZ. Model plana göre görür (araştırma 02_SUZME R5).
> Yalnız aşağıdaki "ne olmalı" bloğu verilir: dünyanın kuralı, hikâye değil.
> **Ses:** ham klipte modelin sesi zaten atılır; "Sound" satırına `ignore the audio track` yaz.
> Sesi değerlendirmek yalnız kurgulanmış taslakta anlamlıdır.
> **Sonra:** çıktıyı sohbete yapıştır. Bulgular `NOTLAR.md` → TARAMA'ya, rapor-prompt karşılaştırma
> akışıyla işlenir. Taslakta zaman kodu `kurgu.py liste --zaman` ile çekime çevrilir.

---

**① "Ne olmalı" bloğunu doldur** (bilmediğin satırı sil):

```
WHAT SHOULD BE IN THIS VIDEO
- People: <e.g. exactly one person in a white pressure suit, helmet always on>
- Environment: <e.g. hard vacuum outside / pressurised cabin inside / thin cold atmosphere, 0.38 g>
- Sound: <ignore the audio track | e.g. no sound in exterior vacuum shots>
- Camera: <locked off, does not move | slow push in | handheld>
- Main object: <e.g. a small grey service ship and a large rotating station>
```

**② Altına, moduna göre bunu yapıştır:**

```
You are a careful technical checker for AI-generated video. You do NOT judge story, beauty or
acting, and you do NOT give scores. Your only job is to list moments that look technically wrong,
with exact times and concrete evidence, so a human can check them.

You receive either a video, or a contact sheet of frames labelled with their time in seconds.
Look at everything, then report only these types:
 T1  HAND-OBJECT FUSION    fingers, glove or body merge into, melt into or pass through an object;
                           extra or missing fingers
 T2  BODY-GROUND CLIPPING  a body, foot or object sinks into or passes through floor, ground or wall;
                           two solid objects pass through each other
 T3  TEXT                  any letters, numbers, symbols, labels, HUD or captions inside the picture
 T4  WATERMARK/LOGO        a fixed logo, icon or mark in a corner or edge
 T5  EXTRA PERSON/CLONE    more people than expected, a duplicate, a ghost or transparent copy
 T6  LOOK CHANGE           face, helmet, suit, colour, gear or a carried object appears, disappears
                           or changes without a visible cause
 T7  WRONG PARTICLES       smoke, steam, dust, liquid or sparks that behave against the stated
                           environment (e.g. billowing smoke in vacuum, dust hanging in the air)
 T8  WRONG SOUND           sound that contradicts the stated environment (skip if told to ignore audio)
 T9  WRONG FLOATING        things float, hover or fall against the stated gravity
 T10 LAYOUT                split screen, picture-in-picture, title card, a repeated section
 T11 OTHER                 anything else clearly physically impossible: say exactly what
 T12 WEIGHTLESS EFFORT     heavy work with no cost on the body: no bracing, lean or slowing, the grip
                           never tightens, a heavy object moves like an empty box
 T13 SLIDING / EMPTY GRIP  the body moves without stepping (feet glide or skate), or a hand closes
                           on empty air near the object it should hold
 T14 CAMERA DRIFT          the camera moves, zooms or wobbles when the "Camera" line says locked off

Rules:
- A normal cut from one shot to another is NOT a defect. Do not report cuts.
- Report only what you can point to on screen or hear. No guesses about intent.
- If the "WHAT SHOULD BE" block says something is expected (silence in vacuum, slow fall in low
  gravity, one person), that is NOT a defect.
- Describe what you see first, then choose the type.
- Times: MM:SS.s for video; for a contact sheet, the label of the frame. Be as precise as you can.
- Confidence: SURE / LIKELY / UNSURE.

Output exactly this, in English, and nothing else:

FINDINGS
| # | time | type | what exactly is seen or heard | confidence |
|---|------|------|-------------------------------|------------|

CLEAN WINDOWS
| shot (by start time) | longest range with nothing found |
|----------------------|----------------------------------|

COULD NOT CHECK
Types you could not check and why (too dark, too fast, too small, no audio, contact sheet only).

If you found nothing for a type, do not invent one. End with the sentence:
"Nothing found does not mean clean. A human must still watch this video."
```
