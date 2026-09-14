# 📋 THE_AMBER_LATTICE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.
> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.**

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
FILM:              THE_AMBER_LATTICE
FORMAT:            Yatay 16:9
RUNTIME:           100 seconds
SCENE COUNT:       10
THEME:             Bilinmeyenin Maddeselliği ve Teknolojik Uyanış
THEME SCENES:      S00 · S04 · S08 · S09
INTENDED EMOTION:  Awe, scientific curiosity, procedural tension
ENDING TYPE:       Visual Dilemma (Uyanan Gezegensel Ağ)
PROTAGONIST:       Exploration Astronaut EVA-4 (Isimsiz)
CENTRAL CHOICE:    Physical contact with monolith surface (S02)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S00 · S01 · S02 · S03 · S04 · S05 · S06 · S07 · S08 · S09
VIRAL INTERSTITIALS: S00 · S05 · S08
TITLE:             What Happens When an Alien Biosteel Lattice Awakens?
LIBRARY CONTEXT:   THE_FORGOTTEN_ARCHITECTS · THE_STONE_SKY · THE_MIRROR_FAUNA
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      10
SHOT COUNT:      10 · sahne içi kesme 0
TARGET ASL BAND: 10.0s (Fixed 10-second grid)
                 GEREKÇE: 10 sahnelik prosedürel keşif ritmi ve müzikal 72 BPM hizası [D74].
GRID:            sahne başlangıcı(n) = 0 + (n−1) × 10
RUNTIME:         100s
RAW FOOTAGE:     100s · TRIM BUDGET: 0s
SCREEN TEXT:     0 saniye
CAMERA:          24mm / 35mm / 50mm / 85mm
SETUP SEQUENCE:  A B C A D B E C D A
KURULUM İSKELETİ: A B C A D B E C D A
KÜME:            2 küme (S00-S03 A, S01-S05 B)
DÖNÜŞ:           %60
ANGLE ARC:       5 açı tipi (Extreme Low, Eye Level, Macro, High Angle, Tracking)
DORUK:           S08 → 80s (sahne başlangıcı 80 s)

FİNAL VURUŞ KANITI [D141]:
   Devasa 120m sekizgen obeliskin 3200K amber ağları ile kaplanmış görüntüsü · 95 saniye · 1 adet Obelisk · BULUNAN
   ffmpeg -ss 95 -i "$M" -frames:v 1 kanit.jpg

DÖNGÜ KANITI: S00 ilk kare (sönük obelisk) ↔ S09 son kare (uyanan amber obelisk) — aynı A kurulumu (24mm EWS extreme low angle).
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1
KASK          Dark gold reflective visor · sırt ünitesi YOK — düz beyaz kompozit [D79]
NOVUM         İnsan-ötesi antik obeliskin amber sarısı biyo-ağ ile uyanması
YERÇEKİMİ     0.4 g
ATMOSFER      Soğuk mavi-gri toz süzülmesi
EKRAN YÖNÜ    Hedef hep Kuzey Obelisk kulesi · İlerleme Doğu->Kuzey — 10 sahnenin 10'unda sabit
SAYAÇ         Amber sarısı parlama yoğunluğu (Monotonik: %0 -> %100)
IŞIK TAKVİMİ  Monotonik (S00 zayıf mikro ışık -> S08 doruk 3200K -> S09 kararlı 3200K)
SES REGISTER  HUMAN 0 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Dondurulmuş Kare ve Titreme Kapısı
KOMUT         ffmpeg -i master.mp4 -vf "freezedetect=noise=-60dB:d=2" -f null -
DOĞRULANDI    ffmpeg 6.1 · 10.09.2026
İKAME         Manuel kare kontrolü ve titreme denetimi
```
