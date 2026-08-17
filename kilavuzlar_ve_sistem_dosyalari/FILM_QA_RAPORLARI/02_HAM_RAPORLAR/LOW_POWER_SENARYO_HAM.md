# 📄 LOW POWER — SENARYO QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 31 Temmuz 2026
> **Kapsam:** Hikaye / dramaturji (teknik QA değil)
> **Durum:** 🚨 **GEÇERSİZ SPEC** — skor sisteme işlenmedi. Gerekçe aşağıda.

---

## 🚨 GEÇERLİLİK UYARISI — ÖNCE BUNU OKU

Bu, projede saklanan **ilk senaryo QA çıktısıdır.** Ama SPEC bloğu
`yatay_3_5_dk_filmler/LOW_POWER/LOW_POWER_PLAN.md`'deki filmle uyuşmuyor.

| Alan | Raporun SPEC'i | LOW_POWER_PLAN.md |
|---|---|---|
| SCENE COUNT | 7 | **25** (S0–S24 · Part A 13 + Part B 12) |
| RUNTIME | 254s (4:14) | **249s** (4:09) |
| DIALOGUE LINES | 1 monolog | **5 konuşmalı sahne** (S2, S10, S11, S20, S22) |
| SILENT SCENES | 4 | **20** |
| VIRAL INTERSTITIALS | 2 (2:20) | **4** (S5, S14, S19, S23) |
| CENTRAL CHOICE | 1:40 | **S20** (~3:15, Part B) |
| PROTAGONIST | "botanist" | **tarımsal sistemler mühendisi** — Dr. Selin Aras, 44, sera sorumlusu |
| THEME | "Sacrifice for the future" | "Bir şeyin yaşaması için senin yaşaman gerekmiyor" — **devretme**, feda değil |
| COVER | "8 Percent" HUD'lu astronot | Kapak S14 (mavi gün batımı) temelli; S2'deki gösterge **analog ibre**, HUD değil |

**Sonuç:** Rapor 7 sahnelik, 254 saniyelik, tek monologlu bir film eleştiriyor.
O film bu depoda yok. Sahne numaraları (S0–S6), timestamp'ler ve alıntılanan
replik **doğrulanamıyor.**

### Bu, doğrudan yanlış olan bulgular

```
❌ "Absence of the Up-Before-Down Beat" (en sert 3 bulgudan biri)
   → S17 TOZ ŞEYTANI tam olarak bu beattir. Plan onu kendi sözleriyle
     "filmin tek yukarı hareketi" diye işaretler ve S18'de düşürür.

❌ Rewrite Prescription 1 — "paneli silsin, toz hemen geri gelsin"
   → S6 (SÜPÜRME) + S7 (GERİ DOLUYOR) zaten tam olarak bu.
     Rapor, filmde var olan bir çözümü öneri diye yazıyor.

❌ Rewrite Prescription 3 — "seçimi gün batımına kes"
   → S14 (mavi gün batımı) ile S20 (seçim) arasında 6 sahne var.
     Raporun kurduğu 1:40/2:20 zaman çizgisi uydurma.

⚠️ Alıntılanan replik: "19 minutes each way. So this is not a conversation.
   It is just a record." — planda böyle bir replik yok. Planın taslak anahtar
   repliği S22'de ve farklı. Prompt "replikleri BİREBİR alıntıla" diyor;
   bu alıntı doğrulanamıyor.

⚠️ İç tutarsızlık: başlıkta OVERALL 7.0, STORY TRACKING ROW'da 7.1.
   (Satırdaki 10 skorun ortalaması 7.1 — başlık yanlış.)
```

### Yine de değerli olan 3 gözlem (SPEC'ten bağımsız)

```
✅ Özgünlük 6/10 — The Martian / Silent Running yakınlığı gerçek bir risk.
   Planın kendi "THE MARTIAN'DAN AYRIŞMA" bölümü bu riski zaten biliyor;
   dış gözün de aynı yeri işaret etmesi ayrışmanın HENÜZ okunmadığını gösterir.

✅ "Görüneni anlatan replik" uyarısı — 19 dakikalık gecikmeyi sözle açıklamak.
   Planın replikleri hâlâ TASLAK ("⚠️ Replikler henüz taslak"). Bu uyarı
   S11 ve S20 replikleri kesinleşirken uygulanabilir.

✅ Kapak/başlık hizası sorusu — vaat edilen görüntü filmin neresinde?
   Kapak S14 temelli ve S14 ~2:19'da. 4:09'luk bir filmde bu kabul edilebilir,
   ama ölçülmemişti; artık ölçüldü.
```

### Yapılacak

```
□ Dolu ve DOĞRU SPEC ile senaryo QA'sı tekrar çalıştırılacak
  (SCENE COUNT 25, RUNTIME 249s, 5 konuşmalı sahne, 4 viral ara sahne)
□ Tekrar çalıştırma yapılana kadar 03_HIKAYE_KALITE_TABLOSU.md'de
  Low Power satırı "geçersiz" olarak durur — ortalamaya girmez
```

---

# 📥 HAM ÇIKTI (değiştirilmeden)

## 📋 FILM SPECIFICATION

```
FILM:                 Low Power
FORMAT:               3-5dk
RUNTIME:              254 seconds (4:14)
SCENE COUNT:          7
REVIEW INPUT:         both

LOGLINE (intended):   When Martian dust buries her solar panels, a stranded astronaut must choose between powering her own life support or the habitat's greenhouse.
THEME (intended):     Sacrifice for the future.
INTENDED EMOTION:     Bittersweet acceptance, awe, existential peace.
ENDING TYPE:          Tragic / Hopeful

PROTAGONIST:          Lone female astronaut/botanist; wants her life's biological work to survive; fears dying without leaving a lasting legacy.
ANTAGONIST/FORCE:     Atmospheric Martian dust accumulation starving solar arrays.
CENTRAL CHOICE:       Divert final battery reserves to life support (self-preservation) or to the greenhouse (legacy). Scene 1:40.

DIALOGUE LINES:       1 central monologue / audio log split across scenes.
SILENT SCENES:        4 (0:00, 0:40, 1:20, 2:20)
VIRAL INTERSTITIALS:  2:20 (The Blue Sunset)

COVER/THUMBNAIL:      Astronaut looking up in a dust storm with title "LOW POWER". Promises a survival crisis on Mars.
TITLE:                "Low Power" — Implies physical power failure, dwindling options, and diminishing life support.

LIBRARY CONTEXT:      Solo hard sci-fi shorts focusing on human survival vs. unyielding cosmic/planetary mechanics.
```

---

OVERALL STORY SCORE: 7.0/10

VERDICT: SHOOT WITH TRIMS

## THE FILM IN ONE SENTENCE (as a first-time viewer would say it)

"An astronaut stranded on Mars runs out of solar power and decides to turn off her own life support so her greenhouse can survive."

---

## SCORES SUMMARY

| Category | Score | Core Issue |
| --- | --- | --- |
| Hook | 8/10 | Establishes immediate situation (8% power), but lacks initial stakes clarity until 0:40. |
| Premise & Clarity | 9/10 | Exceptionally clear premise; physical rules of Mars are established cleanly. |
| Structure & Pacing | 6/10 | Mid-section sags between 1:40 and 2:20; central choice happens early without immediate escalation. |
| Character | 7/10 | Motivations are strong, though interiority relies heavily on familiar botanist tropes. |
| Theme | 8/10 | "Sacrifice for the future" is fully dramatized through a physical action with absolute cost. |
| Dialogue | 7/10 | Concise monologue, though slightly states the obvious about light-delay physics at 2:00. |
| Emotional Arc | 7/10 | Strong transition from dread to contemplative peace, but lacks a temporary beat of hope. |
| Ending | 8/10 | Visual payoff lands the theme squarely on the final frame. |
| Originality | 6/10 | Heavy thematic overlaps with *Silent Running* and *The Martian*. |
| Retention Risk | 5/10 | 40-second dead zone around 2:00 where momentum stalls before the sunset reveal. |

---

## THE THREE THINGS THAT MOST HURT THIS FILM

1. **2:00 - Redundant Dialogue Exposition:** The monologue line *"19 minutes each way. So this is not a conversation. It is just a record"* states physics the audience already instinctively understands about deep space isolation. It stalls dramatic momentum right after the choice is declared at 1:40.
2. **0:40 to 1:20 - Redundant Visual Setup:** Scene 0:40 (inspecting solar array) and Scene 1:20 (inspecting plants) deliver identical narrative beats: "things are dying." One of these beats needs to show an active attempt at a solution rather than two consecutive observations of failure.
3. **Absence of the "Up-Before-Down" Beat:** The astronaut accepts her fate too quickly after declaring the choice at 1:40. Without a brief moment where she tries to clear a panel or reroute auxiliary circuits to save *both*, her sacrifice feels pre-determined rather than forced.

---

## THE THREE THINGS WORTH PROTECTING

1. **2:20 — The Blue Sunset Interstitial:** Pairing the scientific reality of Mars' blue sunset with the quiet acceptance of her choice creates a breathtaking emotional breather.
2. **3:20 — The Physical Act of Rerouting:** The drama is dramatized, not announced. The action of physically flipping the grid bus bars from *Life Support* to *Greenhouse* gives the thematic sacrifice concrete weight.
3. **0:00 — Opening Grid Warning:** Starting directly on the HUD showing "8 Percent" drops the viewer into a active situational crisis immediately without setup fluff.

---

## THE ONE THING NOTHING ELSE DOES

It grounds a high-concept sci-fi sacrifice purely in verified, real-world Martian atmospheric physics (dust accumulation + optical light scattering + light-speed delay) without inventing alien anomalies or magical technology.

---

## SCENE-BY-SCENE VERDICT

| # | Scene | Timestamp | Function in story | Verdict | Note |
| --- | --- | --- | --- | --- | --- |
| S0 | 8 Percent | 0:00 | Establishes critical power emergency | KEEP | Immediate hook; clear stakes. |
| S1 | The Solar Array | 0:40 | Shows cause of power failure | TIGHTEN | Trim by 10s. Combine inspection with a failed clearing attempt. |
| S2 | The Greenhouse | 1:20 | Establishes what is at stake | MERGE | Merge with S1 to show status of habitat alongside power loss. |
| S3 | The Choice | 1:40 | Central dilemma introduced | KEEP | Essential turning point. |
| S4 | 19 Minutes Away | 2:00 | Isolation / Audio Log monologue | REWRITE | Cut radio-delay exposition; focus monologue on her legacy/plants. |
| S5 | The Blue Sunset | 2:20 | Emotional breather / Awe beat | KEEP | Strongest visual and emotional anchor in the film. |
| S6 | The Final Record | 3:20 | Climax & resolution | TIGHTEN | Trim final fade-out to prevent lingering on static frame. |

---

## RANKED CUT LIST (to lose 30 seconds)

1. **Scene 2:00 (19 Minutes Away):** Cut 15 seconds of dialogue explaining the radio delay. *(Loss: Scientific context already implied by setting; Gain: Keeps momentum moving into the blue sunset).*
2. **Scene 0:40 (The Solar Array):** Trim 10 seconds of astronaut walking across dust. *(Loss: Atmosphere; Gain: Eliminates visual drag before reaching the central dilemma).*
3. **Scene 3:20 (The Final Record):** Trim 5 seconds of slow black fade at the ending. *(Loss: Extra lingering time; Gain: Sharpens impact of final image).*

---

## RETENTION DROP-OFF FORECAST

* **0:45 (Drop-off Risk: Medium):** Viewer sees astronaut walking in dust after already understanding the 8% power problem.
*Fix:* Have her actively brush a panel and watch dust instantly refill it within 5 seconds.
* **2:05 (Drop-off Risk: High):** Monologue hits a dry patch explaining 19-minute comms delay.
*Fix:* Cut dialogue; let audio focus on heavy suit breathing over visual of the habitat power fading.
* **2:50 (Drop-off Risk: Medium):** Blue sunset shot holds static for too long without action.
*Fix:* Begin the manual power transfer flip *during* the sunset shot.

---

## SHAREABLE MOMENT

**2:20 - 2:32:** The astronaut standing against the sweeping Martian horizon as the pale blue sun dips below dust clouds, while the habitat lights behind her shift from bright white to emergency green.

---

## REWRITE PRESCRIPTIONS

1. **SCENE 0:40:** Replace passive inspection with an active failure. Show her attempting to wipe a solar panel, only for the static dust storm to cling immediately back to the glass, proving cleaning is mathematically futile.
2. **SCENE 2:00:** Cut the line *"19 minutes each way. So this is not a conversation. It is just a record."* Replace with: *"They'll sprout in three weeks. I won't see it. But you will."* (Focuses on theme of legacy rather than mechanics of distance).
3. **SCENE 1:40 & 2:20:** Intercut the central choice directly into the sunset scene. Have her hand throw the power transfer breaker at 2:35 *while* looking at the sunset, rather than separating the choice into two distant narrative blocks.

---

## STORY TRACKING ROW

| Low Power | 3-5dk | 8/10 | 9/10 | 6/10 | 7/10 | 8/10 | 7/10 | 7/10 | 8/10 | 6/10 | 5/10 | **7.1/10** |
