MEDIA: video played

INPUT MODE: D
FILM: THE_BRITTLE_EDGE
RUNTIME: 02:05 measured
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0s + (n−1) × 10.0s (SPEC §B)
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 02:00–02:05 (Başlık ve final jenerik kartı)
PRESENCE STRING: -11111111111
LINES HEARD: none — room tone present
ZONES REGISTERED: 1 · MEDIUM: vacuum
LIGHT JUMPS: 6 · CLEAN CUTS: 5

---

## ⛔ ZONE REGISTER

```
ZONE REGISTER
· zone            [Ay Yüzeyi / Krater Terası — S00-S11]
· sources         [1 · Güneş · 15° Alçak Açı (SPEC C Bloğu)]
· key direction   [2 o'clock ve 10 o'clock arasında değişken — Sabit Monotonik Işık İhlali]
· key quality     [hard — vakum ortamı sert gölge sınırları]
· shadow          [absolute black / derin vakum gölgesi]
· temperature     [neutral / cool lunar daylight (~5600K)]
· fill            [none — atmosferik saçılma yok]
· medium          [vacuum — no haze, no bloom, no dust scattering]
· change allowed  [none — plan boyunca sabit ışık takvimi declared]
```

---

## LIGHT LEDGER

| Scene | Time | Zone | Key Direction | Quality | Shadow Density | Temp | Practicals | Subject Exp | BG Black | In-Clip Change |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S00 | 00:05 | Ay Yüzeyi | 2 o'clock · alçak | hard | absolute black | neutral | 0/0 | mid | pure black | 0 |
| S01 | 00:15 | Ay Yüzeyi | 10 o'clock · alçak | hard/soft dust | lifted shadow | warm-neutral | 0/0 | bright | lifted grey | dust haze in-clip |
| S02 | 00:25 | Ay Yüzeyi | 2 o'clock · alçak | hard | absolute black | neutral | 0/0 | mid | pure black | 0 |
| S03 | 00:35 | Ay Yüzeyi | 10 o'clock · orta | hard | deep shadow | neutral | 0/0 | bright | dark grey | 0 |
| S04 | 00:45 | Ay Yüzeyi | 10 o'clock · alçak | hard | deep shadow | neutral | 0/0 | mid | dark grey | 0 |
| S05 | 00:55 | Ay Yüzeyi | 2 o'clock · alçak | hard | absolute black | warm grey | 0/0 | bright | pure black | 0 |
| S06 | 01:05 | Ay Yüzeyi | 10 o'clock · alçak | hard | lifted shadow | neutral | 0/0 | mid | dark grey | 0 |
| S07 | 01:15 | Ay Yüzeyi | 1 o'clock · yüksek | hard | deep shadow | neutral | 0/0 | bright | dark grey | 0 |
| S08 | 01:25 | Ay Yüzeyi | 10 o'clock · alçak | hard | deep shadow | neutral | 0/0 | bright | dark grey | 0 |
| S09 | 01:35 | Ay Yüzeyi | 2 o'clock · alçak | hard | absolute black | neutral | 0/0 | mid | pure black | volumetric haze in-clip |
| S10 | 01:45 | Ay Yüzeyi | 2 o'clock · yüksek | hard | deep shadow | warm-neutral | 0/0 | bright | pure black | 0 |
| S11 | 01:55 | Ay Yüzeyi | 2 o'clock · alçak | hard | absolute black | neutral | 0/0 | bright | pure black | 0 |

---

## KEY DIRECTION STRING

```
OBSERVED:  202002010222
ZONES:     AAAAAAAAAAAA
```

⛔ SCENES OBSERVED ile uzunluk eşleşmektedir (12 sahne).

---

## PRESENCE STRING

```
-11111111111
```

---

## LIGHT JUMP LOG

| Cut (out → in) | Zone | What changed | Declared boundary? | Severity |
| --- | --- | --- | --- | --- |
| S00 (00:10) → S01 (00:10) | Ay Yüzeyi | Ana ışık yönü 2 yönünden 10 yönüne sıçradı; arka plan siyah seviyesi griye kalktı. | No | 🔴 High |
| S01 (00:20) → S02 (00:20) | Ay Yüzeyi | Ana ışık yönü 10 yönünden tekrar 2 yönüne döndü; mutlak siyah seviye geri geldi. | No | 🔴 High |
| S02 (00:30) → S03 (00:30) | Ay Yüzeyi | Ana ışık açısı 2 yönünden 10 yönüne kaydı. | No | 🟠 Medium |
| S04 (00:50) → S05 (00:50) | Ay Yüzeyi | Ana ışık yönü 10 yönünden 2 yönüne sıçradı; renk sıcaklığı ısındı. | No | 🔴 High |
| S05 (01:00) → S06 (01:00) | Ay Yüzeyi | Ana ışık yönü 2 yönünden 10 yönüne sıçradı; gölge kenar sertliği yumuşadı. | No | 🔴 High |
| S08 (01:30) → S09 (01:30) | Ay Yüzeyi | Ana ışık yönü 10 yönünden 2 yönüne sıçradı; hacimsel atmosferik sis belirdi. | No | 🔴 High |

---

## SCORES SUMMARY

| # | Category | Score | Issue (ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Key Direction Continuity | 3/10 | S00-S01 (00:10), S01-S02 (00:20), S04-S05 (00:50), S05-S06 (01:00), S08-S09 (01:30) kesmelerinde ışık yönü 2 ve 10 saat yönleri arasında sürekli geziniyor (Pattern ①). |
| 2 | Shadow Quality & Fill | 5/10 | S01 (00:15) ve S06 (01:05) sahnelerinde atmosferik dolgu ışığı ve yumuşatılmış gölgeler mevcut; vakum kuralı ihlali (Pattern ②). |
| 3 | Colour Temperature | 7/10 | S01 (00:15) ve S05 (00:55) sahnelerinde genel regolit renginde nötr gri yerine sıcak/toprak tonu kayması var (Pattern ③). |
| 4 | Practical Sources | 10/10 | Pratik yapay ışık kaynağı yok, güneş tek kaynak olarak tutarlı tanımlanmış. |
| 5 | Exposure at Cuts | 7/10 | S01 (00:10) ve S06 (01:00) kesmelerinde arka plan uzay siyahlığı gri tonlara yükseliyor (Pattern ⑩). |
| 6 | In-Clip Stability | 6/10 | S01 (00:10-00:20) ve S09 (01:30-01:40) sahnelerinde klip içerisinde toz ve sis efektine bağlı olarak ışık yoğunluğunda sürüklenme mevcut (Pattern ⑦). |
| 7 | Zone Boundaries | 4/10 | SPEC C Bloğunda tanımlanan monotonik (sabit tek yönlü) güneş açısı kuralı kurgu sınırlarında korunmamış. |
| 8 | Atmosphere Honesty | 3/10 | 0 Pa vakum ortamında (SPEC C) S01 ve S09 sahnelerinde havada süzülen atmosferik ışık huzmeleri ve toz sisi emisyonu bulunuyor (Pattern ⑧). |

VERDICT: KEY WALKS

---

## THE THREE THAT MATTER

1. **Ana Işık Yönünün Kesmelerde Gezinmesi (Key Walks)**
*Düzeltme:* S01, S03, S04, S06 ve S08 klipslerini ana güneş ışığı kadrajın sağ üstünden (2 o'clock açısı) gelecek şekilde yeniden ürettirin.
2. **Vakum Ortamında Atmosferik Sis ve Huzme Oluşumu**
*Düzeltme:* S01 ve S09 promptlarındaki "haze / dust clouds / volumetric light" parametrelerini kaldırıp balistik toz düşüşü ile yeniden üretin.
3. **Uzay Siyahının Griye Kalkması ve Gölge Yoğunluğu Kaybı**
*Düzeltme:* Color grade / renk düzenlemesinde S01 ve S06 klibindeki arka plan siyah seviyelerini (black level) tam sıfıra (#000000) çekin.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

* **Renk Düzenlemede (Grade) Düzeltilebilir:**
* S01 ve S05'teki hafif sıcak renk sıcaklığı kaymaları.
* S01, S04 ve S06'daki arka plan uzay siyah seviyesinin (0 RGB) çekilmesi.

* **Yeniden Üretim (Regeneration) Gerektirenler:**
* S01, S03, S04, S06, S08 klipslerindeki ters ışık yönü (Key Walks — piksel seviyesinde gölge yönü değişimi).
* S01 ve S09'daki vakum kuralına aykırı atmosferik toz/sis ışık dağılımları.

---

## FLAGS FOR DOCUMENT CHECK

* SPEC C Bloğunda belirtilen "15° alçak açılı monotonik güneş" kuralına rağmen, kamera açısı değiştikçe AI motorunun ışık kaynağını kameralara göre göreceli yerleştirmesi önlenmelidir.

---

## OUT-OF-SCOPE FLAGS

* **⑤ ARKA PLAN:** S01 (00:10-00:20) sahnesindeki krater yapısı ve regolit dokusu S02'deki uçurum kenarı topografyası ile birebir çakışmıyor.
* **⑥ FİZİK:** S01'de tekerleklerden kalkan regolit tozunun havada asılı kalma süresi 0.16 g Ay yerçekimi balistik düşüş hızından daha yavaş süzülmektedir.
