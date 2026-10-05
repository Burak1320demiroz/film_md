INPUT MODE: D
FILM: THE_LAST_TOW
BOLUM: PART 2 (BÖLÜM 2 · K25–K48 · S07–S12)
RUNTIME: 04:00 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 00:00 + n × 10 s
SCENES OBSERVED: 6 · CUTS COUNTED: 23 · CUTS OFF GRID: 0 · 0:10, 0:20, 0:30, 0:40, 0:50, 1:00, 1:10, 1:20, 1:30, 1:40, 1:50, 2:00, 2:10, 2:20, 2:30, 2:40, 2:50, 3:00, 3:10, 3:20, 3:30, 3:40, 3:50
NON-SCENE MATERIAL: none
PRESENCE STRING: --1111111111111111111111
LINES HEARD: none — contact sound bed present
ZONES REGISTERED: 2 · MEDIUM: vacuum
LIGHT JUMPS: 2 · CLEAN CUTS: 21

---

## ZONE REGISTER

```
ZONE REGISTER
· zone 1          [S01–S03 · Deck Hatch]
· sources         [2 overhead LED strips, top-left]
· key direction   [10 o'clock · 45° elevation]
· key quality     [hard]
· shadow          [absolute black · hard edge]
· temperature     [cool 6500K]
· fill            [none]
· medium          [vacuum — no haze, no bloom]
· change allowed  [at S04 boundary to Zone 2]

· zone 2          [S04–S06 · Airlock Corridor]
· sources         [1 overhead spot]
· key direction   [12 o'clock · top]
· key quality     [hard]
· shadow          [absolute black · hard edge]
· temperature     [neutral 5000K]
· fill            [none]
· medium          [vacuum — no haze, no bloom]
· change allowed  [none]
```

---

## LIGHT LEDGER

| Scene | Time | Zone | Key Direction | Quality | Shadow | Temp | Practicals | Exposure | BG Black | In-Clip Change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | 00:00 | Zone 1 | 10 o'clock 45° | hard | absolute black | cool | 2/2 | mid | black | 0 |
| S02 | 00:40 | Zone 1 | 10 o'clock 45° | hard | absolute black | cool | 2/2 | mid | black | 0 |
| S03 | 01:20 | Zone 1 | 10 o'clock 45° | hard | absolute black | cool | 2/2 | mid | black | temp drift (01:50) |
| S04 | 02:00 | Zone 2 | 12 o'clock top | hard | absolute black | neutral | 1/1 | dark | black | 0 |
| S05 | 02:40 | Zone 2 | 12 o'clock top | hard | absolute black | neutral | 1/1 | dark | black | 0 |
| S06 | 03:20 | Zone 2 | 12 o'clock top | hard | absolute black | neutral | 1/1 | dark | black | 0 |

---

## KEY DIRECTION STRING

```
OBSERVED:  000000000000TTTTTTTTTTTT
ZONES:     AAAAAAAAAAAABBBBBBBBBBBB
```

---

## PRESENCE STRING

`--1111111111111111111111`

---

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| K11 → K12 (01:50) | Zone 1 | Slight color temperature warmth shift | No | Minor |
| K17 → K18 (02:50) | Zone 2 | Visor frame exposure lift | No | Minor |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 7/10 | S01–S06 (00:00–04:00): Key directions maintain zone placement. |
| 2 | Shadow Quality & Fill | 7/10 | S01–S06 (00:00–04:00): Vacuum shadow density is consistent across scenes. |
| 3 | Colour Temperature | 6/10 | S03 / K12 (01:50): Shows subtle temperature drift in key light. |
| 4 | Practical Sources | 7/10 | S01–S06 (00:00–04:00): Practical count matches registered sources per zone. |
| 5 | Exposure at Cuts | 6/10 | S05 / K17–K18 (02:50): Exhibits minor exposure jump on helmet. |
| 6 | In-Clip Stability | 6/10 | S03 / K12 (01:50): Shows minor mid-clip warmth drift. |
| 7 | Zone Boundaries | 7/10 | S03→S04 (02:00): Transition matches declared SPEC boundary. |
| 8 | Atmosphere Honesty | 7/10 | S01–S06 (00:00–04:00): No air haze or volumetric bloom observed in vacuum. |

VERDICT: GRADEABLE DRIFT

---

## THE THREE THAT MATTER

1. **S03 renk sıcaklığı kayması (01:50 / K12):** Ana ışıkta beliren hafif ısınma. *Fix:* Grade aşamasında S03 tonomakslarını soğuk tona eşitleyin.
2. **S05 kask parlaması (02:50 / K18):** Kask kenarındaki pozlama zıplaması. *Fix:* K18 girişinde kask vurgusunu %10 düşürün.
3. **S04 alan geçiş gölgesi (02:00 / K13):** Siyah seviyesinde hafif yumuşama. *Fix:* S04 dip siyah seviyelerini vakum ortamına uygun olarak sıkılaştırın.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Fixable in the grade:** K12 renk sıcaklığı düzeltmesi ve K18 pozlama dengelemesi renk servisinde çözülebilir.
* **Requires regeneration:** Yeniden üretim gerektiren kritik ışık yönü veya kaynak hatası bulunmamaktadır.

---

## FLAGS FOR DOCUMENT CHECK

* S04 alanındaki ışık kaynağının yoğunluk değeri SPEC planı ile teyit edilmelidir.

---

## OUT-OF-SCOPE FLAGS

* **ARKA PLAN (Lens ⑤):** K13 kapı arkası metalik doku sürekliliği kontrol edilebilir.
