# 🔗 2 · SÜREKLİLİK — kesmenin iki yanı (puansız)

> **Ne için:** her klip ayrı üretilir ve model bir öncekini hatırlamaz. Hata çoğu zaman klibin içinde değil,
> **iki klibin birleştiği kesmede** görünür: ışık sağdan soldan döner, kask değişir, gemi ters yöne gider,
> gökteki gezegen yer değiştirir.
> Eski 15 merceğin şu dördünün işini görür: ② devamlılık (kesmeler arası) · ⑤ arka plan · ⑪ ışık · ⑮ yön.
> **Nerede:** Gemini uygulaması, **yeni bir sohbet**.
> **Ne verilir:** taslak film (sesli olabilir), **en çok 90 saniyelik** parçalar hâlinde + o parçanın
> kesme listesi + "ne olmalı" bloğu.
> **Kesme listesi:** `python3 uretim_hatti/araclar/kurgu.py liste <FILM>/timeline.json --kesmeler`
> - Zincir içindeki kesmeler kendiliğinden SAME çıkar.
> - `?` kalanları FILM.md §2/§4'e bakarak sen doldurursun: aynı yer ve kesintisiz zaman = `SAME`;
>   yer ya da zaman atlıyor = `NEW`.
> - Parçaya bölünmüşse zamanları parçanın başına göre kaydır.
>
> ⛔ Plan, hikâye, logline VERİLMEZ. Kesme listesi yapı bilgisidir, hikâye değil. "Gemi soldan sağa
> gitmeli" gibi beklenen yön verilmez: model değişimi raporlar, doğru olanı sen bilirsin.
> **Sonra:** çıktıyı sohbete yapıştır. Bulgular `NOTLAR.md` → SÜREKLİLİK'e, rapor-prompt karşılaştırma
> akışıyla işlenir (kesmenin iki yanındaki iki çekimin promptları açılır).

---

**① "Ne olmalı" bloğu ve kesme listesi:**

```
WHAT SHOULD BE IN THIS VIDEO
- People: <e.g. exactly one person in a white pressure suit, orange band on the left upper arm>
- Environment: <e.g. hard vacuum, 0.16 g, one hard sun, black sky>
- Sound: <ignore the audio | final mix: no sound in exterior vacuum shots>

CUT LIST   (time · from → to · SAME = same place and continuous time · NEW = place or time jumps)
1  00:08.4  C01 → C02  SAME
2  00:16.0  C02 → C03  NEW
```

**② Altına bunu yapıştır:**

```
You are a continuity supervisor for a film made of separately generated AI clips. You do NOT judge
story, beauty or acting, and you do NOT give scores. Your only job is to compare the last moment
before each cut with the first moment after it, and list what changed that should not have.

For every cut in the CUT LIST, look at the last second before and the first second after.
At a SAME cut (same place, continuous time) check all of these:
 S1  LOOK JUMP        face, helmet, visor, suit colour or parts, a marking or band (which side?),
                      a carried object: different on the two sides of the cut
 S2  LIGHT JUMP       the main light comes from a different side, changes colour, or exposure jumps
 S3  DIRECTION FLIP   a person or vehicle moving or looking left-to-right now moves or looks
                      right-to-left; the camera crosses the line between two people or objects
 S4  WORLD JUMP       sky, planet, sun, horizon, background structure or set layout is different
 S5  STATE RESET      damage, dirt, a door or hatch, a light, a cable, a tool or an object's
                      position goes back or jumps without being shown
 S6  PHYSICS MISMATCH the same place shows a different gravity, atmosphere (dust, haze) or scale
 S7  SOUND JUMP       only with sound: the background sound drops to silence or changes abruptly
                      at the cut, or a sound continues that should have stopped
At a NEW cut (place or time jumps) check only S1: the same person must still look the same.

Rules:
- The cut itself is NOT a defect. A change in camera angle or framing is NOT a defect.
- Report only differences you can point to on both sides. Describe the before and the after.
- If the "WHAT SHOULD BE" block says something is expected, that is NOT a defect.
- Times: the cut time from the CUT LIST.
- Confidence: SURE / LIKELY / UNSURE.

Output exactly this, in English, and nothing else:

FINDINGS
| # | time | type | what exactly is seen or heard (cut number · before → after) | confidence |
|---|------|------|-------------------------------------------------------------|------------|

CUTS WITH NOTHING FOUND
List the cut numbers.

COULD NOT CHECK
Cuts or types you could not check and why (too dark, too short, face not visible, no audio).

End with the sentence: "Nothing found does not mean clean. A human must still watch this video."
```
