# 🧩 THE_KEPT_LIGHT — prompt hata analizi

```
FORMAT      yatay 4 dk · 25 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   8/8 geçerli · BULGU 22 → tekil 20
HÜKÜM       🅐 6 · 🅑 13 · 🅒 1 · 🅓 0      🅑/(🅐+🅑) = %68
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 23/25 · sayı 24/25 · temas 4/25 · giysi 19/25 · parçacık 1/25 · bloom 24/25 · metin 23/25 · efor 24/25 · g-ad 15/25 · g-sayı 24/25 · filigran 24/25 · kamera 24/25
  ⛔ HİÇ YOK: dış-ses
  bulgulu sahnelerde eksik: dış-ses 0/10 · temas 2/10 · giysi 7/10 · parçacık 0/10 · g-ad 5/10
```

---

## 🅑 SINIF 1 — İKİ YERÇEKİMİ AYNI KADRAJDA · 1 🔴 · 3 🟠 ⭐ [D200]

| S | bulgu |
|:--:|---|
| S01 🔴 | *Floating objects (0 G) vs normal human walking gait (1 G)* |
| S01 | *Severe mixed gravity vectors: character walks with a heavy 1 g terrestrial gait …* |
| S01 | *Terrestrial footfall impact dynamics: planted heel-strike and knee flexion* |
| S11 | *Released objects float upward vs dropping slowly downward* |

Ortam ADI **15/25'te** var (S01 ve S11 o on beşin **dışında**), ortam SAYISI 24/25'te.
Filmin açılış sahnesi, ortam yasası yazılmadan üretilmiş.

**Hüküm 🅑 ×4.** ⛔ İki rejim aynı kadraja giremez; giriyorsa ayıran şey kadrajda
olmalıdır. Ortam cümlesi **seçmeli değildir**.

## 🅑 SINIF 2 — MEKÂN DEVAMLILIĞI VE KAPAK DURUMU · 5 🟠

S01 ×2 (*"Hatch is wide open, then firmly closed and bolted"* · *"Character operates
on the hatch, then arrives at it"*) · S05 (*"Hatch closed, then instantly open
again"*) · S03 (*tavan lambaları duvar aplikine dönüşüyor*) · S04 (*düz metal duvar
kayalık mağaraya dönüşüyor*). Kapağın açık/kapalı **durumu** hiçbir promptta
merdiven taşımıyor; mekân her sahnede yeniden tarif ediliyor.

## 🅑 SINIF 3 — ODA TONU VE SES GEÇİŞİ · 3 🟠

S01 · S05 ③ (*"Metal Room — No, just floor drop"*) · S05 (*"Rock cavern tone vs
metal room tone levels jump abruptly"*). `AUDIO:` 23/25'te var ama **hacim
değişiminin ses karşılığı** yazılmamış.

## 🅑 SINIF 4 — HALAT/KABLO FİZİĞİ · 1 🟠 · 🅑 SINIF 5 — ELDİVEN İNCELİĞİ · 2 🔴

S17 (*"horizontal tension cable instantly collapses into a free …"*) ·
S07 🔴 · S08 🔴 (*"Using small pliers in thick gloves — reduced dexterity, fumbling"* ·
*"the visual thickness of the gloves contradicts the bare-hand fine-motor dexterity"*).

---

## 🅐 MODEL SAPMASI · 6

Doku yüzmesi S04 (*"rear bulkhead liquefies and morphs into jagged rock"*, bloom/doku
24/25) · ⑧ EFOR S03 · S16 🔴 (efor 24/25) · nesne devamlılığı S08 (*pense → bağlı
kutu*, giysi 19/25).

## 🅒 BULGU DÜŞER · 1

S15 ⑦ (*"Could not state what the pliers were achieving; motion without a readable
goal"*) — ⚠️ bu aslında 🅑 sayılabilir (hedef promptta yazılı değilse) ama sahne
haritası hedefi taşıyor ve ⑦ SPEC'siz koşmuş.

## 🎯 ÜÇ SATIR

```
1. ORTAM CÜMLESİ SEÇMELİ UYGULANMIŞ — 15/25. Dört bulgu, biri 🔴, hepsi
   cümlenin düştüğü iki sahnede.
2. KAPAK AÇIK MI KAPALI MI BELLİ DEĞİL. Beş bulgu tek bir eksik durum merdiveninden.
3. TEMAS 4/25 · PARÇACIK 1/25 — çekirdeğin iki cümlesi neredeyse hiç yok.
```
