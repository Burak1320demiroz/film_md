INPUT MODE: D
FILM: THE_STATIC_VEIL
RUNTIME: 02:05
FRAME RATE ASSUMED: 24 fps
SCENES OBSERVED: 12
CUTS COUNTED: 11 · 00:10, 00:20, 00:30, 00:40, 00:50, 01:00, 01:10, 01:20, 01:30, 01:40, 01:50
NON-SCENE MATERIAL: 02:00-02:05 (başlık kartı "THE STATIC VEIL")
PRESENCE STRING: -11111111111
LINES HEARD: none — room tone present
ACTS LOGGED: 11
ACTS MISSED: 10 HIT · 0 MISS · 0 UNKNOWN · 0 NO TARGET · 1 FLIP
PREMISE REGISTER:
· gravity / medium          [0.16 g Ay yerçekimi, vakum ortamında elektrostatik levitasyon tozu]
· world geometry declared   [Pilon ve fener hedefi ekran sağında; astronot soldan sağa ilerler]
· mirror / reversal rules   [Yok]
· declared screen axis      [12/12 sabit lockoff tripod, ekran sağ dilim hedef kilidi]

---

## TARGET LEDGER

* V1 | 00:10 | GO | screen-left to screen-right | Pilon/fener platformu (00:00, screen-right) | HIT | Astronot soldan sağa pilondan tarafa yürür.
*Vector sentence:* Astronot 00:00'da kadrajın sağ diliminde gösterilen pilona doğru, ekran solundan ekran sağına yürür.
* V2 | 00:20 | REACH | upward to helmet visor | Kask vizörü camı (00:20, screen-center) | HIT | Sağ el vizördeki tozu kazıyarak siler.
*Vector sentence:* Astronot elini 00:20'de kadrajlanan kask vizörüne kaldırıp tozlu camı siler.
* V3 | 00:30 | LOOK / REACH | downward to rail | Zemin çelik rayı (00:30, screen-bottom) | HIT | Eller raya dayanır, baş aşağı bakar.
*Vector sentence:* Astronot 00:30'da kadrajın alt kısmındaki çelik raya doğru eğilip ellerini dayar.
* V4 | 00:40 | REACH / AIM | downward to platform socket | Fener haznesi (00:40, screen-center) | HIT | Amber silindir yuvaya indirilir.
*Vector sentence:* Astronot elindeki silindiri 00:40'ta gösterilen fener haznesine doğru indirip yerleştirir.
* V5 | 00:50 | REACH | inward to cylinder top | Silindir kapağı/bileziği (00:50, screen-center) | HIT | Eldivenler silindir kapağına temas eder.
*Vector sentence:* Eldivenli eller 00:50'de kadraj merkezindeki silindir bileziğine uzanıp kavramaktadır.
* V6 | 01:00 | AIM / CLAMP | screen-right to pilon leg | Pilon gövdesi (01:00, screen-right) | HIT | Kıskaç pilon profiline sabitlenir.
*Vector sentence:* Astronot elindeki kıskacı 01:00'da ekran sağındaki pilon dikmesine yöneltip sıkar.
* V7 | 01:10 | REACH / CLAMP | center to electrical contact | Bağlantı bloku (01:10, screen-center) | HIT | Ark elektrik kıskacın temas noktasından saçar.
*Vector sentence:* Kıskaç 01:10'da kadraj ortasındaki metal temas noktasına bastırılır ve ark oradan patlar.
* V8 | 01:20 | GO / REACH | screen-right to pilon base | Pilon montaj noktası (01:20, screen-right) | HIT | Batarya kutusu pilona yaklaştırılır.
*Vector sentence:* Astronot batarya kutusunu 01:20'de ekran sağındaki pilon montaj alanına taşır.
* V9 | 01:30 | AIM / RELEASE | screen-right to pilon terminal | Pilon terminali (01:30, screen-right) | HIT | Elektrik arkı terminal birleşiminden vizöre sıçrar.
*Vector sentence:* Batarya 01:30'da ekran sağındaki klemense dokundurulur ve elektrik arkı temas yerinden çıkar.
* V10 | 01:40 | REACH / TURN | center to locking ring | Fener kilit bileziği (01:40, screen-center) | HIT | Bilezik çevrilerek kilitlenir.
*Vector sentence:* Eldivenler 01:40'ta kadraj ortasındaki fener bileziğini kavrayıp çevirir.
* V11 | 01:50 | GO / LOOK | screen-right, looking screen-left | Yanan fener (00:00'da screen-right; 01:50'de screen-left) | FLIP | Fener ekran soluna geçmiş, astronot ekran sağından sola bakar.
*Vector sentence:* Astronot ekran sağında durup 00:00'da ekran sağında kurulan fakat 01:50'de ekran soluna kayan fener ışığına bakar.

---

## PRESENCE STRING

-11111111111

---

## VECTOR STRING

-HHHHHHHHHHx

---

## VECTOR LOCK VERIFICATION — MODE D ONLY

| Lock the plan declares (target · slice · direction) | Scene | Found at | Vector from screen | Verdict |
| --- | --- | --- | --- | --- |
| Pilon/fener hedefi · screen-right slice · soldan sağa ilerleme | S01 | 00:10 | Soldan sağa pilona yürüyüş | PASS |
| Pilon/fener hedefi · screen-right slice | S06 | 01:00 | Ekran sağındaki pilona kıskaç takma | PASS |
| Pilon/fener hedefi · screen-right slice | S08 | 01:20 | Ekran sağındaki pilona batarya getirme | PASS |
| Pilon/fener hedefi · screen-right slice | S09 | 01:30 | Ekran sağındaki terminale temas | PASS |
| Pilon/fener hedefi · screen-right slice · 12/12 sabit eksen | S11 | 01:50 | Fener platformu ekran solunda (screen-left) | FAIL |

---

## SCORES SUMMARY

| # | Category | Score | Issue (with ledger rows and timecodes) |
| --- | --- | --- | --- |
| 1 | Target Establishment | 8/10 | -2 · V11 (01:50) - Hedef fener S00'da ekran sağındayken S11'de kurgusal değişimle ekran soluna kaymış (Pattern ⑩). |
| 2 | Look Direction | 10/10 | — |
| 3 | Turn & Travel Direction | 9/10 | -1 · V11 (01:50) - S11'de astronotun durduğu ve yöneldiği aks S00'daki geniş açının simetriği/ters aksı olmuş (Pattern ①). |
| 4 | Reach & Aim | 10/10 | — |
| 5 | Fire · Trigger · Throw · Release | 10/10 | — |
| 6 | Screen Direction Across Cuts | 7/10 | -3 · V11 (01:50) - C bloğundaki 12/12 sabit ekran aksı ve sağ dilim fener kilidi S11'de aks atlaması/aynalama ile ihlal edilmiş (Pattern ①, ⑩). |
| 7 | Camera-Relative Sense | 9/10 | -1 · V11 (01:50) - Kamera pilonun diğer tarafına geçip aksı kırmış. |
| 8 | Consequence on Target | 10/10 | — |

VERDICT: WRONG WAY

---

## MISSED VECTORS TABLE

| Timecode | Act | Vector on screen | Target and where it was (tc) | Match | Pattern (①–⑭) | Severity |
| --- | --- | --- | --- | --- | --- | --- |
| 01:50 | GO / LOOK | Ekran sağında durup ekran soluna bakar | Fener platformu (00:00'da screen-right gösterildi) | FLIP | ① (THE 180° FLIP) / ⑩ (THE GOAL THAT DRIFTS) | 🔴 HIGH |

---

## PROMPT ORDERS FOR THE NEXT FILM

| # | Pattern | Act that missed (tc) | The prompt line that would have prevented it | Confidence |
| --- | --- | --- | --- | --- |
| 1 | ① / ⑩ | V11 (01:50) | the beacon platform stays locked in the right third of the frame in S11; the astronaut stands on the left third looking screen-right toward the lit beacon | HIGH |

---

## CONTRADICTION LOG

00:00 vs 01:50 — 00:00 geniş açıda fener platformu kadrajın sağ diliminde (screen-right) sabitlenmişken, S11 final sahnesinde (01:50) fener platformu kadrajın sol dilimine (screen-left) geçmiş ve astronot ekran sağında konumlandırılmıştır. Puanlama S11'deki aks atlaması (FLIP) üzerinden düşürülmüştür.

---

## THE THREE THAT MATTER

01:50 — Fener platformunun S00'a kıyasla sağ dilimden sol dilime geçerek 180° aks kırması (FLIP): "the beacon platform stays locked in the right third of the frame across all wide shots, with the light cone projecting screen-left to screen-right".

---

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

* **Fixable in the Edit:** S11 klibi kurguda yatay eksende aynalanarak (horizontal flip) fener ekran sağına, astronot ekran soluna çekilebilir; böylece S00 ile kusursuz aks uyumu sağlanır.
* **Requires Regeneration:** Yok (S11'deki aks hatası kurguda tek bir yatay mirror/flip hamlesiyle tamamen çözülebilir durumdadır).

---

## FLAGS FOR DOCUMENT CHECK

01:50 — S11 klibinde fener platformu ekran solundadır — QUESTION: C bloğundaki "12/12 sabit eksen ve fener kadrajın sağ diliminde" kilit kuralı S11 promptunda atlanmış mıdır?

---

## OUT-OF-SCOPE FLAGS

* **00:20 (Kare Merceği ① / Devamlılık Merceği ②):** Kask vizöründeki çizik ve regolit toz kalıbı yakın çekimde değişmektedir.
* **01:13 (Fizik Merceği ⑥):** Elektrik arkı kıvılcımları vakum ortamında yerçekimsiz gibi düz hatta yayılmaktadır.
