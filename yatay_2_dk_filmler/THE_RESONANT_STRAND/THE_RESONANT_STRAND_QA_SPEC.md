# 📋 THE_RESONANT_STRAND — QA SPEC (rubriklere yapıştırılacak tek dosya)

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
FILM:              THE_RESONANT_STRAND
FORMAT:            yatay_2_dk_filmler
RUNTIME:           125 seconds (title card: 120s - 125s — screen text lock 5 s)
SCENE COUNT:       14
THEME:             Algının Ötesindeki Düzen (Organik Keşif)
THEME SCENES:      S03 · S10 · S12
INTENDED EMOTION:  Kozmik Huşu ve Bilimsel Merak
ENDING TYPE:       Döngüsel Match Cut (S13 → S00)
PROTAGONIST:       Dr. Sarah Chen (Astronot)
CENTRAL CHOICE:    Güvenlik Tether Mandalı Sökümü (S12)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S00 - S13 (Tamamı Repliksiz)
VIRAL INTERSTITIALS: S00 · S06 · S09 · S12
TITLE:             THE RESONANT STRAND (Rezonans Teli / İpliği)
LIBRARY CONTEXT:   THE_GRAVITY_ANCHOR · THE_TETHERED_MASS · THE_CANOPY_WORLD
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      14
SHOT COUNT:      14 · sahne içi kesme 0
TARGET ASL BAND: 8.9 s   ASL CURVE: 4-7-4-7 s ritim dalgalanması
GRID:            sahne başlangıcı(n) = 0s + n × 8.9s (yaklaşık 9s)
RUNTIME:         125 s (02:05)
RAW FOOTAGE:     14 klipler · TRIM BUDGET: 0.1s / klip
SCREEN TEXT:     5 saniye (Title Card)
CAMERA:          24mm / 35mm Sinematik Sabit & Takip Kamera
SETUP SEQUENCE:  S00-A, S01-B, S02-B, S03-A, S04-C, S05-B, S06-C, S07-C, S08-B, S09-D, S10-D, S11-D, S12-B, S13-A
KURULUM İSKELETİ: A B B A C B C C B D D D B A
KÜME:            3 küme (S01-S02, S06-S07, S09-S10-S11)
DÖNÜŞ:           %64 (9 dönüş: S02, S03, S05, S06, S07, S08, S10, S11, S12)
ANGLE ARC:       4 Açı Tipi (Low Angle 15° · Eye-Level 0° · Low Angle 20° · Low Angle 40°)
DORUK:           S12 → Safety Tether Sökümü (sahne başlangıcı 119 s)

FİNAL VURUŞ KANITI [D141]:
   Titreyen titanyum metal levha · 124 saniye · 1 adet levha · BULUNAN
DÖNGÜ KANITI: ilk kare S00 titreyen metal levha ↔ son kare S13 titreyen metal levha (birebir aynı kurulum, açı ve ışık).
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  - 1 1 1 1 1 1 1 1 1 1 1 1 -
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
1. Varlık Boyutu: 1000m genişliğinde çan mantle, 300m boyunda 3 şerit yüzgeç.
2. Vizör Opaklığı: 100% yansıtıcı altın zar (DERS 197), 0 external face visible.
3. Kütle Yükseliş Fiziği: Laminar dikey akustik rezonans hattı (DERS 198), 0.3g yerçekimi.
4. Işık Açısı: Sol üstten 30° ochre volumetrik güneş ışığı (DERS 201).
```
