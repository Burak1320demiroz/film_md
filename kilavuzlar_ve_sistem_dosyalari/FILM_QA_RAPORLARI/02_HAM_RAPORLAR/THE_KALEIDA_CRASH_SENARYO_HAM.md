# 📄 THE KALEIDA CRASH — SENARYO QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 31 Temmuz 2026
> **Kapsam:** Hikaye / dramaturji
> **Durum:** ⚠️ **ŞARTLI GEÇERLİ** — skor tabloya girdi, 2 reçete reddedildi.

---

## ✅ ÖNCE İYİ HABER: ZAMAN ÇİZGİSİ TUTUYOR

Low Power'ın aksine bu rapor **gerçekten var olan filmi** izlemiş.
Kendi sahne numaralarını kullanmış ama timestamp'ler plandaki 10 saniyelik
sahne ızgarasına neredeyse birebir oturuyor:

| Rapor | Timestamp | Plan dosyası | Eşleşme |
|---|---|---|---|
| S0 | 0:00–0:09 | S0 HOOK — gemi patladı | ✅ |
| S1 | 0:10–0:29 | S1 çakılış + S2 duman sütunu | ✅ birleştirilmiş |
| S2 | 0:30–0:49 | **S3.5 prizmatik şok dalgası** + S4 kristal orman | ⚠️ viral sahne ayırt edilememiş |
| S3 | 0:50–0:59 | S5 Prizma Hayalet | ✅ |
| S4 | 1:00–1:09 | S6 **CIVA NEHRİ** | ⚠️ "water/reflection walk" diye okunmuş |
| S5 | 1:10–1:19 | **S6.5 ağırlıksız sıçrama (viral)** | ⚠️ "chasm jump" diye okunmuş |
| S6 | 1:20–1:39 | S7 enkaz alanı + S8 tırmanma | ✅ birleştirilmiş |
| S7 | 1:40–1:49 | S9 sinyal — ışık sütunu | ✅ |
| S8 | 1:50–2:05 | S10 iki güneş batıyor | ✅ (plan 10s, kurgu 15s) |

**Sonuç:** Rapor uydurmadı. Bulgular gerçek karelere ait. Ama künye
verilmediği için **iki tasarım gerçeğini göremedi** ve reçeteleri o yüzden
yanlış hedefe gitti.

---

## ⚠️ NEDEN "ŞARTLI" — GÖREMEDİĞİ ÜÇ ŞEY

```
1. DOKÜMAN VERİLMEDİ (REVIEW INPUT: video)
   Rubrik "video + PLAN DOSYASI" diyor. Ring Walker'la aynı hata.
   → VIRAL INTERSTITIALS alanı boş kaldı; rapor S3.5 ve S6.5'in
     dağıtım için tasarlanmış saf görsel beatler olduğunu bilmiyordu
     ve ikisini de kesme/kısaltma listesine yazdı.

2. SAHNE SAYISI DOĞRULANMADI
   Rapor: 9 sahne / 125s.  Plan: 12 sahne bloğu / ~120s.
   Numaralandırma kaymış — raporun "S4"ü planın S6'sı.
   Bu haliyle reçeteler DOĞRUDAN UYGULANAMAZ, önce yukarıdaki
   eşleme tablosundan çevrilmeleri gerekir.

3. KAPSAM SIZINTISI — teknik bulgu hikaye raporuna girmiş
   "1:25 — Cloning Visual Error" teknik bir hata (Ders 20).
   Rubrik bunu açıkça yasaklıyor. Yine de DEĞERLİ: bu, Ders 20'nin
   yayınlanan kurguda hâlâ görünür olduğunun İLK TIMESTAMP'Lİ kanıtı.
   → Teknik kayda taşındı: 01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md
```

---

## ❌ REDDEDİLEN 2 REÇETE

```
❌ Reçete 1 — "Prizma Hayalet'e aktif tehdit veya yol gösterici rol ver"
   Plan bu sahneyi bilerek tehditsiz yazmış: video promptunda birebir
   "No horror tone — this is curiosity, not threat" yazıyor.
   Ayrıca serinin DNA'sı: "No villain. The opposing force is
   environmental, physical, or temporal." Rubriğin kendi kuralı bu
   kısıtı hata saymayı yasaklıyor.
   → Sahnenin sorunu tehdit eksikliği değil, KARAKTERİN o karşılaşmadan
     değişmeden çıkması olabilir. Doğru soru bu; rapor yanlışını sormuş.

❌ Reçete 2 — "S4'ü (1:00) tamamen kes"
   Raporun S4'ü planın S6'sı: CIVA NEHRİ — 15m genişliğinde, yüzen
   kristal levhalar üzerinden geçilen tek gerçek tehlike sahnesi.
   "Redundant walking beat" değil, filmin tek risk anı. Kesilirse
   S0'daki çarpışmadan S9'daki sinyale kadar hiçbir tehlike kalmaz.
   → Sorun sahnenin varlığı değil, çekimde riskin okunmaması olabilir.
     Bu bir MANTIK/KURGU bulgusu, senaryo bulgusu değil.
```

---

## ✅ KABUL EDİLEN — DOKÜMANDA DA DOĞRULANAN 3 BULGU

```
✅ KARAKTER 4/10 — "reactive protagonist, lacks interiority"
   Plan doğruluyor: Ayla'nın SEÇİMİ yok. Film çakılıyor → yürüyor →
   sinyal gönderiyor → bekliyor. Rubriğin COST TEST'i: karakter neyi
   feda ediyor? Hiçbir şeyi. Tema 5/10 bunun sonucu, sebebi değil.
   → Serinin en güçlü filmlerinde (Low Power S20) bir bedel var.
     Bu filmde yok. En değerli bulgu bu.

✅ ORTA BÖLÜM TEKRARI — 12 sahnenin 4'ü geçiş/yürüyüş
   S2 (ufuk) · S4 (orman) · S6 (nehir) · S6.5 (sıçrama).
   Plan üzerinde de sayılabilen yapısal bir örüntü; videoya bağlı değil.
   → Çözüm kesmek değil, geçiş sahnelerinin her birine FARKLI bir
     işlev vermek (biri keşif, biri risk, biri bedel).

✅ ÖZGÜNLÜK 4/10 — projenin en düşük özgünlük skoru
   Plan "NEDEN VİRAL" bölümünde ayrışmayı diğer FİLMLERE karşı
   kuruyor (Glass Abyss, Inversion, Resonance Field) — ama tanınmış
   sinemaya karşı hiç kurmuyor. Dış göz Pitch Black'i işaret etti.
```

---

## 🔧 RUBRİK KUSURU — BU RAPORUN ORTAYA ÇIKARDIĞI

```
Diyalog: 5.0/10 — gerekçe: "Completely silent film".

Rubrik kendi notlarında "Silence is not a gap" diyor ve sessizliği
serinin bilinçli kısıtları arasında sayıyor. Buna rağmen kategori
puanlandı ve ortalamayı aşağı çekti.
→ Tamamen sessiz filmde Diyalog kategorisi N/A olmalı, toplam kalan
  9 kategori üzerinden hesaplanmalı. (Teknik tablo bunu zaten yapıyor:
  "Canlı: N/A".) SENARYO_QA promptuna kural eklendi.
  Bu filmde etkisi küçük: 51/10 = 5.1 → 46/9 = 5.1.
```

---

## 📌 PLAN DOSYASINDA BULUNAN AYRI BİR HATA

QA'dan bağımsız, doğrulama sırasında çıktı:

```
🚨 THE_KALEIDA_CRASH_PLANET_FILM.md 13 SAHNE olduğunu söylüyor.
   Dosyada 12 sahne bloğu var. "SAHNE 3" HİÇ YOK — S2'den S3.5'e atlıyor.
   12 prompt'un 12'si de kendini "Scene N of 13" diye tanıtıyor.

Etkisi: kalite tablosundaki "Full (tam film)" kapsamı aslında 12 sahne.
Numaralandırmayı düzeltmek mi, eksik S3'ü yazmak mı — bu bir içerik
kararı, QA kaydı bunu kendi başına değiştirmedi.
```

---

# 📥 HAM ÇIKTI (değiştirilmeden)

FILM: The Kaleida Crash

FORMAT: 2-4dk

RUNTIME: 125s

REVIEW INPUT: video

SPEC BLOCK PROVIDED: partial (derived from video asset)

SPEC VERIFIED AGAINST PLAN DOC: partial (evaluated directly from footage)

OVERALL STORY SCORE: 5.1/10

VERDICT: SHOOT WITH TRIMS

## THE FILM IN ONE SENTENCE (as a first-time viewer would say it)

"An astronaut crash-lands on a dangerous crystal planet and hikes to her destroyed ship to send a distress beacon into space."

## SCORES SUMMARY

| Category | Score | Core Issue |
| --- | --- | --- |
| Hook | 6.0/10 | High-stakes explosion, but situation lacks personal narrative depth. |
| Premise & Clarity | 6.0/10 | Straightforward survival story; world mechanics remain unexplained. |
| Structure & Pacing | 5.0/10 | Linear sequence with repetitive middle traversal beats. |
| Character | 4.0/10 | Reactive protagonist; lacks interiority and distinct personal motivation. |
| Theme | 5.0/10 | Standard sci-fi survival tropes with minimal emotional sacrifice. |
| Dialogue | 5.0/10 | Completely silent film; relies entirely on visual beats. |
| Emotional Arc | 5.0/10 | Moderate escalation leading to beacon activation; missing a true low point. |
| Ending | 6.0/10 | Satisfying visual climax with beacon release and sunset resolve. |
| Originality | 4.0/10 | Visually distinct crystal world, but narrative borrows heavily from *Planet of the Apes* / *Pitch Black*. |
| Retention Risk | 5.0/10 | Slow middle section risks viewer drop-off before the climax. |

## THE THREE THINGS THAT MOST HURT THIS FILM

1. **0:50** — *Creature Encounter* — The crystal beast appears briefly without posing real danger or advancing the plot.
2. **1:00–1:19** — *Redundant Traversal* — Multiple shots of running and hopping across crystals stall the narrative momentum.
3. **1:25** — *Cloning Visual Error* — A duplicate protagonist walking disrupts narrative immersion and continuity.

## THE THREE THINGS WORTH PROTECTING

1. **0:00–0:09** — *Opening Drop* — Immediate high-stakes hook with orbital explosion and pod impact.
2. **1:40–1:49** — *Beacon Launch* — High visual payoff when the beam ignites into the sky.
3. **1:50–2:05** — *Twin Suns Closing* — Reflective, quiet final frame that grounds the atmosphere.

## THE ONE THING NOTHING ELSE DOES

The interactive, energy-glowing footsteps left on iridescent crystal terrain.

## SCENE-BY-SCENE VERDICT

| # | Scene | Function in story | Verdict | Note |
| --- | --- | --- | --- | --- |
| S0 | 0:00–0:09 | Inciting Incident / Crash | KEEP | Establishes immediate stakes. |
| S1 | 0:10–0:29 | Pod Exit & Orientation | TIGHTEN | Trim crawl sequence by 5s. |
| S2 | 0:30–0:49 | Crystal Forest Walking | KEEP | Sets planetary environment rules. |
| S3 | 0:50–0:59 | Crystal Beast Meeting | REWRITE | Give creature an active threat or helper beat. |
| S4 | 1:00–1:09 | Water/Reflection Crossing | CUT | Redundant walking beat. |
| S5 | 1:10–1:19 | Chasm Jump | TIGHTEN | Trim jump prep to speed up pacing. |
| S6 | 1:20–1:39 | Ship Wreckage Discovery | KEEP | Clear structural goal reached. |
| S7 | 1:40–1:49 | Beacon Activation | KEEP | Strong emotional and visual peak. |
| S8 | 1:50–2:05 | Sunset Resolution | KEEP | Lands thematic tone of quiet isolation. |

## RANKED CUT LIST (to lose 30 seconds)

1. **1:00–1:09 (S4)** — Save 9s — Removes redundant reflection walk without losing narrative context.
2. **0:10–0:19 (S1)** — Save 9s — Trims prolonged crawling out of pod.
3. **1:10–1:19 (S5)** — Save 12s — Condenses chasm traversal directly to ship arrival.

## RETENTION DROP-OFF FORECAST

* **0:35** — Environmental walk lacks conflict — Add subtle environmental hazard sound/visual.
* **0:55** — Beast encounter ends passively — Have creature block or redirect her path.
* **1:15** — Repeated running beats — Cut straight to sighting the crashed ship hull.

## SHAREABLE MOMENT

* **1:45** — Skyward energy beam launching through crystal atmosphere.

## REWRITE PRESCRIPTIONS

1. **SCENE S3 (0:50)**: Replace passive creature stare with creature pointing toward or guarding the wreckage location → establishes clear environmental dynamic.
2. **SCENE S4 (1:00)**: Cut scene entirely → transitions faster to the primary goal (ship hull).
3. **SCENE S6 (1:25)**: Remove duplicate character visual element → preserves solo survival focus.

## STORY TRACKING ROW

| The Kaleida Crash | 2-4dk | 6.0 | 6.0 | 5.0 | 4.0 | 5.0 | 5.0 | 5.0 | 6.0 | 4.0 | 5.0 | **5.1/10** |
