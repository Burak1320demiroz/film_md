# 🖼️ THE WHITE FLOOD — KAPAK

**Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · akış adım 10
**Vaat kapısı:** `PAKETLEME_VE_VAAT_KILAVUZU.md` — kapak ANI senaryoda seçilir,
üretimden sonra aranmaz.

```
KAPAK ANI:      S0 · 0:06   ·   gerekçe: kapak anı 0:00-0:10 bandından
                seçilir [§1 sayısal kilit] ve bu kare filmin TEK KARE
                testini taşıyan karedir: tek nesnenin üstünde iki dünya —
                alt yarısı beyaz kırağı, üst yarısı çıplak metal, sınır
                usturayla çizilmiş gibi düz. Vaat-teyit penceresi: kapağın
                vadettiği şey ekranda 0:06'da, yani ≤10 saniye içinde
                teslim edilir ✅
                ⛔ "en güzel sahne" gerekçe değildir; tek sınav 120 px'tir.
BAŞLIKLA UYUM:  Başlık "THE WHITE FLOOD" yükselen beyaz bir şey vaat ediyor;
                kapak o beyazın SINIRINI gösteriyor ve bir soru açıyor:
                neden beyaz olan ALT yarı? Kapak başlığı TEKRAR ETMİYOR,
                onu SORUYA çeviriyor (§2 ret şartı ③ temiz).
PLAN B KAPAK:   S12 · 1:59-2:09 — çizginin üstünden bakış: mor-siyah gök,
                kesintisiz beyaz ova ve ondan ada gibi çıkan sekiz sırt.
                Kart Y yayından ÖNCE hazır olmasını ister (§7.2). Fraktal
                ölçek odağı (§2 ③) burada en güçlü; ama vaat-teyit
                penceresi 1:59'dadır ve ≤10 s kuralını KARŞILAMAZ — bu
                yüzden PLAN B'dir, A değil.
ÖLÇÜ:           yatay 1280×720  (ve 1920×1080 kaynak)
ODAK (§2):      ② YÜKSEK KONTRASTLI SİLUET — koyu iki gövde arasında
                duran, yarısı beyaz yarısı koyu tek dikey nesne.
                ⛔ ① VİZÖR YANSIMASI KULLANILMADI: bu filmin vizörü optik
                  berrak ve çevre yansıması SIFIR yazılıyor [D79]; yansıma
                  odağı bu hattın kendi kilidiyle çelişir.
```

---

## 📸 KAPAK PROMPTU

> ⛔ **Metinsiz üret.** Tipografi post-prodüksiyonda. Prompt içinde tek
> harf istenmez [Ders 9 / 34 / 45].
> ⛔ Bu başlık bilerek `📸 GÖRSEL PROMPT` DEĞİLDİR: kapak bir sahne değildir
> ve dizi kapılarına (kurulum yayı · açı tipi · tema) girmemelidir.

```
Photorealistic cinematic still, 16:9 landscape, poster-grade.

Two figures in matte charcoal-grey surface suits stand side by side at the edge of a low rock step on a cold mountain world, turned three-quarters toward camera, both leaning back against a thin grey line they are drawing up from below the step. Their helmets are hard charcoal shells with one flat pane of optically clear glass each — zero tint, zero mirror coating, zero reflection — and a pale ring of light inside each rim keeps both faces fully readable. The taller one wears a bold red fabric stripe wrapped right around her RIGHT forearm and RIGHT thigh; the shorter, broader one wears a bright electric blue stripe wrapped right around his LEFT bicep and LEFT thigh. The back of each suit is one continuous smooth panel from collar to hip, carrying nothing.

A bare metal hand lamp the length of a forearm hangs on the end of that line at chest height in the right third of the frame. The lower half of the lamp is furred thick with white rime; the upper half is clean bare metal; the boundary between them is perfectly straight and horizontal, as though it had been cut. Behind them the dark mountain face carries the same straight boundary at the same height, running level away to the horizon: white below, bare charcoal rock above.

COMPOSITION: the hanging lamp on the right third line, its half-white body silhouetted against the darker rock behind it so that the boundary separates at small sizes; the two figures in the left two thirds; the level boundary running out of frame on both sides. A low rim light separates their shoulders and helmets from whatever is behind them and neither silhouette merges with the background. Nothing story-critical in the bottom sixth or the top sixth of the frame — those bands are covered by platform interface.

LIGHTING: no sun and no shadow. Even dim blue-grey fill from the whole sky at once, and a pale flat ceiling three metres overhead closing the top of the world. High separation between the white lower half of the lamp and the dark rock behind it. No orange, no warm tone.

NEGATIVE: Exactly 2 human characters — no third person, no duplicates, no clones, no reflected figure, no extra shadow. 0% bloom, no glow, no lens flare, no soft focus, no haze; every surface keeps texture. Photorealistic skin — pores and fatigue retained, no airbrushing, no waxy or plastic texture. No readable text, no letters, no numbers, no symbols anywhere — not on the suits, not on the lamp, not on the rock or the snow; no scale marks, no survey markers. No watermark, no HUD overlay, no lens data, no name label, no lower third, no border, no frame, no logo. No back-mounted unit — the back silhouette is flat and each back is one continuous smooth panel carrying nothing. No bare skin anywhere — none above the collar, none at the wrists, none at the ankles. No falling snow, nothing drifts through the air. No liquid of any kind: nothing is wet, nothing drips, nothing melts, and the white on the lamp is a dry solid crust. No CGI or game look. Photorealistic, 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

---

## ✅ 120 PX TESTİ — elle, her üretimde

```
Küçültüldüğünde okunması gereken TEK şey:
   iki koyu gövdenin arasında asılı duran, ALT YARISI BEYAZ ÜST YARISI
   KOYU tek dikey nesne — yani "bu şeyin yarısı başka bir dünyada"
   okuması. Sınır çizgisinin YATAY ve DÜZ olduğu 120 px'te de görünmeli.

Yardımcı okumalar (ikincil, kaybolabilir):
   · arkadaki dağ duvarındaki aynı çizgi
   · iki figürün şerit renkleri (kırmızı sağ / mavi sol)

okunmuyorsa → yeniden üret. Geri kalan hiçbir şey kapağı kurtarmaz.
(KAPAK_QA rubriği 12.08.2026'da kaldırıldı — test manuel yapılır.)

⛔ HOOK KILAVUZU §0② ile ORTAK: S0'ın 0. karesi zaten feed'de kapaktır ve
   120 px testi orada MAKİNEYLE koşulur (kare 120 px'e indirilip kontrast
   ve entropi ölçülür). Aynı kare, iki kapı — ikisi de üretimden sonra.
```

## 🚫 RET ŞARTLARI (§2)

```
□ Karakter kadrajın ortasında BOŞLUĞA bakıyor      → bu kapakta HAYIR:
  ikisi de çektikleri nesneye bakıyor, niyet okunuyor
□ Ön plan ile arka plan aynı ton bandında          → HAYIR: beyaz kürklü
  alt yarı koyu kayanın önünde, ayrışma en yüksek
□ Kapak, başlığın söylediğini görsel olarak TEKRAR ediyor → HAYIR:
  başlık "beyaz bir sel" diyor, kapak bir SEL GÖSTERMİYOR — bir nesnenin
  üstündeki çizgiyi gösteriyor ve ikinci bir soru açıyor ("neden ALT
  yarı beyaz?"). Selin ne olduğu (hava) filmin içinde açılır.
```
