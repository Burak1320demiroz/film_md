# 📄 THE TIDAL HUNT — MANTIK VE DEVAMLILIK QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 31 Temmuz 2026
> **Kapsam:** Sahneler arası kendi içinde tutarlılık (teknik ve hikaye değil)
> **Durum:** ✅ **GEÇERLİ** — kural ihlali yok, rubrik kendi sınırında kaldı.

---

## ✅ NEDEN GEÇERLİ — İLK KURALINA UYAN RAPOR

Bu, projedeki **ilk kapı ihlali olmayan QA raporu.**

```
✅ Girdi doğru:        rubrik "yalnız video" istiyor, rapor yalnız videoyla çalıştı
✅ Baseline bildirildi: "SELF-CONSISTENCY — does the film agree with itself"
✅ "Eksik" raporlamadı:  çözemediği 2 soruyu FLAGS FOR DOCUMENT CHECK'e yazdı
✅ Kapsam sınırı çalıştı: 3 teknik bulgu OUT-OF-SCOPE FLAGS altında kaldı
✅ Sayaç yoksa N/A dedi:  uydurma puan üretmedi
```

Low Power (uydurdu), Ring Walker (dokümansız), Kaleida (tasarımı göremedi),
Inversion (kapı atlandı) — dördü de künye yüzünden şartlı veya geçersizdi.
Bu rapor doküman **istemediği** için o hataya yapısal olarak düşemiyor.
Rubriğin tasarımı işe yarıyor.

---

# 🔎 DOKÜMAN KONTROLÜ — raporun sorduğu 2 sorunun cevabı

Rubrik bu işi rapordan sonra yapılacak iş olarak tanımlıyor. Kaynak:
`yatay_2_dk_filmler/THE_TIDAL_HUNT/THE_TIDAL_HUNT_PLANET_FILM.md`

### ❓ Soru 1 — "Başta ve sonda iki kâşif var, ortada bir. Yalnız mı olmalıydı?"

**CEVAP: YALNIZ OLMALIYDI. İkinci figür bir üretim hatası.**

Character Bible birinci satır:

> *"the **first researcher to attempt a full solo crossing** of Flucta's exposed
> seabed within a single 6-hour tidal cycle"*

S10'un prompt'u da tek kişi tarif ediyor: *"a boarding ramp extending toward
Dalga's **small, still figure**"*. Filmde ikinci bir insan **hiç yok** —
ne mürettebat, ne pilot.

```
→ Bu DERS 20 (karakter klonlama / çift kişi hatası) ihlalidir.
→ İhlal ettiği yerler: 0:00-0:09 (S1 iniş) ve 1:49-2:00 (S10 dönüş)
→ Ders 20 bu filmden değil, Kaleida Crash'ten çıkmıştı; burada TEKRARLADI.
→ Filmin tek insanlı olması dramatik omurga: "solo geçiş" filmin önermesi.
   İki figür, filmin ne olduğu iddiasını ilk 9 saniyede çürütüyor.
```

### ❓ Soru 2 — "Dalgıç ekipmanı sadece su/bataklık yakınında beliriyor. Dinamik mi, hata mı?"

**CEVAP: HATA. Üstelik Bible'ın ÖNCEDEN YASAKLADIĞI bir hata.**

Character Bible, SUIT bölümü:

> *"a low-profile **chest-mounted rebreather unit, integrated into the suit,
> never a separate handheld device**"*

Yani solunum ünitesi **göğüste ve suit'e gömülü.** Sırta takılan büyük bir
dalgıç tüpü ne Bible'da ne de 13 sahne prompt'unun hiçbirinde geçiyor.
Suit'in amfibi uyarlaması **parmak arası perde** olarak yazılmış, tüp olarak
değil.

```
→ Model, "su + dalgıç" bağlamından tüpü KENDİ EKLEDİ.
→ Ders 8 (kıyafet değişimi) ve Ders 37 (ekipman durum geçişi) kapsamında.
→ Raporun "toggles on/off" gözlemi doğru teşhis: 0:37 ve 1:35'te var,
   0:25 ve 1:40'ta yok.
```

---

# 🚨 RAPORUN FARKINDA OLMADAN BULDUĞU ASIL ŞEY

Rapor şunu yazdı ve puanlanacak bir şey bulamadığı için `N/A` geçti:

```
Counter Logic:  N/A — No active counter observed.
Open Threads:   Wrist Device · introduced 0:11 · "Screen never shown;
                purpose unclear."
Setup & Abandonment: 4/10 — "Wrist device frequently used, never explained."
```

**Bu, filmin omurgasının ekrana hiç çıkmadığı anlamına geliyor.**

Plan dosyasına göre bilek ekranı dekor değil, **filmin yapısı:**

| Plan satırı | Ne diyor |
|---|---|
| Character Bible | *"a constant **countdown to the cycle's final hour**"* |
| S0 video prompt | *"the countdown reads **6:00:00** and begins ticking"* |
| S4 video prompt | *"the countdown reading **past the halfway**"* |
| S9 video prompt | *"the countdown resting at **0:00:00**"* |

Film "6 saatte gel-git düzlüğünü geç" filmi. Sayaç, gerilimin tek kaynağı.
İzleyici sayacı hiç görmediği için **filmin saati yok** — geriye "bir kadın
koşuyor" kalıyor. Raporun Yapı ve Kurulum skorlarının düşük olmasının
sebebi bu; rapor sebebi bilmeden sonucu doğru ölçmüş.

### Kök sebep: plan dosyası KENDİ İÇİNDE ÇELİŞİYOR

Aynı dosyanın iki satırı:

```
satır 285:  NO AI TEXT [LESSON 13]: Wrist display = abstract patterns only.
                                    NEVER text.
satır 338:  2s — She raises her wrist display; the countdown reads 6:00:00
```

Ders 13 (hologramda anlamsız AI metni) doğru bir dersti ve bu filmde sert
biçimde uygulandı. Ama sayaç **sayıyla** tarif edildiği için model iki emir
arasında kaldı ve **yasağa uydu:** ekranı hiç göstermedi.

→ **Negatif kilit, filmin anlatı aracını sessizce sildi.**
→ Bu bulgu **DERS 46** olarak yazıldı (`../../LESSONS_LEARNED.md`).

---

# 🌊 İKİNCİ DOĞRULAMA: DALGA ATLAMASI PLANDA DA VAR

Rapor 1:38 → 1:40 arasını "climax is skipped" diye işaretledi ve düzeltmeyi
"yüksek maliyet — köprü çekim üret" diye fiyatladı. **Doğru fiyatlamış:**

```
S8 video prompt, 10s:  "Dalga reaches the base of the outcrop and BEGINS TO
                        CLIMB as the wave closes the final distance."
S9 image prompt, 0s:   "The wave HAS PASSED. Dalga stands alone on the wet
                        rock outcrop."

Arada dalganın çarptığı / geçtiği an YOK. Planda da yok.
```

Yani bu bir kurgu hatası değil, **senaryo boşluğu.** Filmin doruğu iki
sahnenin arasına düşmüş. Kurguyla kapatılamaz; sahne yazılması gerekir.

→ Senaryo QA'sı bu filme henüz yapılmadı; yapıldığında bu boşluğu
  bağımsız olarak bulması beklenir. Bulamazsa senaryo rubriği zayıf demektir.

---

# 📤 KAPSAM DIŞI BULGULARIN ADRESİ

Rapor 3 teknik bulguyu doğru şekilde kendi dışında bıraktı. İkisi bu filmin
**mevcut derslerine ilk kez zaman damgası veriyor:**

| Bulgu | Zaman | Nereye ait |
|---|---|---|
| Yüzde "jello" morphu | 1:03 | Karakter 3/10 — timestamp'i yoktu |
| Kırmızı kuşlar bulanık kütleye dönüşüyor | 1:13 | **Ders 18** (canlı) — ilk timestamp |
| Leviathan dalgayla akışkan etkileşmiyor | 1:30 | **Ders 24 / 31** — sıvı etkileşimi |
| Yengeç kayaya çarpıyor ↔ yaratık bacaklardan geçiyor | 0:14 / 0:54 | **Ders 17** (çarpışma) — ilk timestamp, bu filmden çıkmıştı |

Teknik kayda işlendi: `../01_FILM_RAPORLARI/THE_TIDAL_HUNT.md`

---

# 📥 HAM ÇIKTI (değiştirilmeden)

FILM: The Tidal Hunt
RUNTIME: 02:05 · SCENES OBSERVED: 12
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees
with itself, not whether it matches its design.

OVERALL SCORE: 4/10
VERDICT: FIXABLE IN EDIT

## SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
| --- | --- | --- | --- | --- | --- |
| 1 | 0:00-0:09 | Cliffside | 2 Explorers | Ship lands; explorers exit. | No |
| 2 | 0:09-0:19 | Rocky Shore | Explorer, Crabs | Walks among crabs; checks wrist. | No |
| 3 | 0:19-0:29 | Swamp | Explorer, Crabs | Runs through mud. | No |
| 4 | 0:29-0:39 | Swamp Center | Explorer | Observes tentacle mass; checks wrist. | No |
| 5 | 0:39-0:49 | Salt Flat | Explorer | Walks; checks wrist; looks up. | No |
| 6 | 0:49-0:59 | Salt Flat | Explorer, Beasts | Crawls while beasts stampede. | No |
| 7 | 0:59-1:09 | Salt Flat | Explorer | Runs across flat. | No |
| 8 | 1:09-1:19 | Salt Flat | Explorer, Birds | Stops among red flock. | No |
| 9 | 1:19-1:29 | Salt Flat | Explorer, Beasts | Runs from mega-tsunami. | No |
| 10 | 1:29-1:39 | Coastline | Explorer, Beasts | Runs in shallows from wave; climbs rock. | No |
| 11 | 1:39-1:49 | Isolated Rock | Explorer | Stands by calm sea; checks wrist. | No |
| 12 | 1:49-2:00 | Cliffside | 2 Explorers | Ship hovers, lands; boarding. | No |

## SCORES SUMMARY

| Category | Score | Critical Issue |
| --- | --- | --- |
| Physical Consistency | 3/10 | Severe collision/clipping differences. |
| Counter Logic | N/A | No active counter observed. |
| Spatial Geography | 4/10 | Geographic transitions are abrupt jumps. |
| Time & Light Logic | 3/10 | Instantaneous weather/time shifts. |
| State, Costume & Props | 3/10 | Equipment appears/disappears between shots. |
| Causality & Knowledge | 4/10 | Imminent threat (wave) resolves off-screen. |
| Quantity Consistency | 6/10 | Single character focus mostly stable. |
| Setup & Abandonment | 4/10 | Wrist device frequently used, never explained. |

## SEVERITY TALLY

🔴 BLOCKER: 0   🟠 MAJOR: 4   🟡 MINOR: 3

## COUNTER CURVE

NONE

## LOCATION MAP

| Location (your name for it) | Scenes | Consistent? | Mismatch |
| --- | --- | --- | --- |
| Cliffside | 1, 12 | Yes | None. |
| Swamp | 3, 4 | Yes | None. |
| Salt Flat | 5, 6, 7, 8, 9 | No | Shifts from dry/clear (S5) to flooded/stormy (S9). |
| Isolated Rock | 11 | Yes | None. |

## DRIFT MAP — where the film starts losing itself

| Element | First slip (timecode) | Undeniable by | Recovered? |
| --- | --- | --- | --- |
| Scuba Gear | 0:37 | 0:40 | No (toggles on/off). |
| Time/Weather | 1:10 | 1:20 | No. |
| Physics (Clipping) | 0:54 | 0:54 | Recovers in S7. |

## CONTRADICTION LOG

| Timecode A | Timecode B | Category | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| 0:25 | 0:37 | Costume & Props | Character has no backpack at A; wears large scuba tank at B. | 🟠 MAJOR |
| 0:14 | 0:54 | Physical | Crabs collide with rock at A; beast phases entirely through character at B. | 🟠 MAJOR |
| 1:12 | 1:21 | Time & Light | Sky is orange/clear at A; sky is dark/stormy at B. | 🟠 MAJOR |
| 1:38 | 1:40 | Causality | Wave is crashing onto character at A; sea is instantly flat/calm at B. | 🟠 MAJOR |
| 1:35 | 1:40 | Costume & Props | Wears scuba tank at A; wears no tank at B. | 🟡 MINOR |

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
| --- | --- | --- | --- |
| Wrist Device | 0:11 | Yes (multiple times) | Screen never shown; purpose unclear. |

## THE THREE THAT MATTER

1. **The Disappearing Scuba Tank:** Present in S4 and S10, absent everywhere else. Viewers will feel the gear shifting instantly. *Fix: Cut 0:30-0:39 entirely or regenerate.*
2. **The Wave Resolution Jump:** At 1:38 she is inches from a colossal wave; at 1:40 she stands perfectly dry by a calm sea. The climax is skipped. *Fix: Add a shot showing the wave receding/passing, or cut 1:40 entirely.*
3. **The Phasing Beast:** At 0:54, the large feline clips completely through her legs. Breaks physical reality. *Fix: Cut the crawling shot (S6).*

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Tank toggling (0:25 vs 0:37) | Cut shot 4 | Low (trim edit) |
| Phasing beast (0:54) | Cut shot 6 | Low (trim edit) |
| Abrupt wave cut (1:38 vs 1:40) | Regenerate bridging shot | High (AI gen) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| Two explorers at start/end, one in middle. | Was she supposed to be alone, or is the partner missing from S2-S11? |
| Scuba gear appears only near water/swamp. | Does the suit dynamically generate gear, or is this a continuity error? |

## OUT-OF-SCOPE FLAGS

* Heavy "jello" morphing on character's face at 1:03.
* Red birds morph into blurry blobs at 1:13.
* The Leviathan at 1:30 is a cool reveal but lacks fluid interaction with the wave.
