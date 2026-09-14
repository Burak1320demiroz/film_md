# 📋 THE_SHATTERED_BREATH — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_SHATTERED_BREATH
FORMAT:            Yatay 2-4 dk (16:9)
RUNTIME:           120 seconds (12 scenes x 10s)
SCENE COUNT:       12
THEME:             BEDEL (The Price of Survival)
THEME SCENES:      S02 · S07 · S08
INTENDED EMOTION:  High tension survival dilemma, claustrophobic determination
ENDING TYPE:       Paradox / Visual Rhyme
PROTAGONIST:       Lone Survivor Astronaut
CENTRAL CHOICE:    S08 (Dismantling outer suit insulation to direct heat internally)
DIALOGUE LINES:    0 · HUMAN 0 / MACHINE 0
SILENT SCENES:     S00 - S11 (All silent dialogue, 3-layer diegetic audio)
VIRAL INTERSTITIALS: S00, S02, S04, S07, S08, S11
TITLE:             The Heat That Melts The Ground Beneath You
LIBRARY CONTEXT:   THE_COLD_WELD, THE_FROST_LINE, THE_SOLAR_MIRROR
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12
SHOT COUNT:      12 (1 shot per 10s scene, zero intra-clip cuts)
TARGET ASL BAND: 10.0s   ASL CURVE: Fixed 10s grid
                 Gerekçe: 16:9 Yatay 2-4 dk format 10s sahne standardı [D74]
GRID:            sahne başlangıcı(n) = 0 + n × 10 s
RUNTIME:         120s
RAW FOOTAGE:     12 clips x 10s = 120s
SCREEN TEXT:     0 saniye (No text overlay)
CAMERA:          35mm / 50mm / 85mm / 24mm / 100mm prime lenses, fixed lockoff per shot
SETUP SEQUENCE:  A A B B C C B C D C E A
KURULUM İSKELETİ: A A B B C C B C D C E A
KÜME:            3 (S01, S03, S05)
DÖNÜŞ:           5 / 12 (%42 ≥ %40)
ANGLE ARC:       5 (Göz Seviyesi, Alçak Açı, Yüksek Açı, Dik Yüksek Açı, Aşırı Yakın Göz)
DORUK:           S08 → Yalıtım Sökümü (01:20 - 01:30)

REPLİK ZAMANLARI: Replik yok.

FİNAL VURUŞ KANITI:
   Astronot mikro-adacık üzerinde · 118 saniye · 1 adet adacık · BULUNAN adacık ve altındaki parıltı
DÖNGÜ KANITI: S00 (0s) ↔ S11 (110s) — Setup A (35mm Eye-level, 0°), aynı kadraj, tek değişken erimiş zemin durumu.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  111111111111     (Her 12 sahnede 1 astronot mevcut)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 astronot
KASK          Altın kaplama yansıtmalı vizör, 470nm cyan-blue HUD iç aydınlatma, sırt heykelsi pozitif, no backpack, no suit humps, flat back profile
NOVUM         Isı donmayı önler ancak durulan 88 K kompozit buz zemini eriterek altında uçurum açar
YERÇEKİMİ     1.0 g
ATMOSFER      88 K Kriyojenik vakum/mikro-partikül buhar
EKRAN YÖNÜ    Soldan sağa jeotermal hat ilerleyişi
SAYAÇ         Zemin erime çapı: 10cm → 50cm → 1.8m → 0.9m
EŞ KADRAJ     S00 ↔ S01 ↔ S11, S02 ↔ S03 ↔ S06, S04 ↔ S05 ↔ S07 ↔ S09, S08, S10
YIPRANMA      Göğüs pirinç termo-valf ve zırh dış yüzeyi
IŞIK TAKVİMİ  Gece Kriyojenik + 590nm kehribar alt parıltı
SES REGISTER  HUMAN 0 · MACHINE 0 (Diegetik sesler)
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Kamera Sabitlik Kapısı
KOMUT         ffmpeg -i input.mp4 -vf vidstabdetect=result=transform.trf -f null -
DOĞRULANDI    ffmpeg 7.0 · 2026-09-13
İKAME         Siyah ekran süzme testi
```
