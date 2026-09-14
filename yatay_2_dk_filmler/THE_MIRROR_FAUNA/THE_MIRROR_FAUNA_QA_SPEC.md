# 📋 THE_MIRROR_FAUNA — QA SPEC

> **[DERS 117]:** SPEC bir DOSYADIR. QA anında operatörün eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_MIRROR_FAUNA
FORMAT:            yatay_2_dk_filmler (16:9 Yatay Bilimkurgu)
RUNTIME:           149 seconds
SCENE COUNT:       15
THEME:             İLK-TEMAS / KİMLİK
THEME SCENES:      S04 · S09 · S14
INTENDED EMOTION:  Gerilim, Keşif, Huşu, Tematik Kabulleniş
ENDING TYPE:       Görsel Kafiye / Açık İkilem
PROTAGONIST:       Kaptan Vance & Uzman Ray (Astronot Çifti)
CENTRAL CHOICE:    S09 (Astronot Vance'in elini uzatarak teması kabul etmesi)
DIALOGUE LINES:    11 · register: HUMAN 11 / MACHINE 0
SILENT SCENES:     4 (S00, S02, S08, S10)
VIRAL INTERSTITIALS: S00, S04, S09, S11, S14
TITLE:             THE_MIRROR_FAUNA (İnsan eylemini kopyalayan uzaylı canlı türü)
LIBRARY CONTEXT:   THE_STARLESS_CIRCLE, THE_COLD_WELD, THE_HERD
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ

```
CLIP COUNT:      15
SHOT COUNT:      15 · sahne içi kesme 0
TARGET ASL BAND: 10.0s (Hook 9s + 14 x 10s)
GRID:            sahne başlangıcı(n) = 9s + (n-1) x 10s
RUNTIME:         149s (2:29 min)
RAW FOOTAGE:     15 clips
SCREEN TEXT:     0 saniye
CAMERA:          35mm / 50mm / 85mm Anamorphic Prime (Dinamik Açı Yayları)
SETUP SEQUENCE:  A B C A D E F B C E A F D B C
KURULUM İSKELETİ: A B C A D E F B C E A F D B C
KÜME:            4 küme (A: S00/S03/S10, B: S01/S07/S13, C: S02/S08/S14, E: S05/S09)
DÖNÜŞ:           %60.0 (9/15)
ANGLE ARC:       5 Açı Tipi (Düşük Açı, Göz Hizası, Yan Açı, Yüksek Açı, Dutch Angle)
DORUK:           S11 -> Bedel Patlaması (sahne başlangıcı 109s)

REPLİK ZAMANLARI:
   replik(S01) = 9 + 0x10 + 2s = 11s
   replik(S03) = 9 + 2x10 + 2s = 31s
   replik(S04) = 9 + 3x10 + 2s = 41s
   replik(S05) = 9 + 4x10 + 2s = 51s
   replik(S06) = 9 + 5x10 + 2s = 61s
   replik(S07) = 9 + 6x10 + 2s = 71s
   replik(S09) = 9 + 8x10 + 2s = 91s
   replik(S11) = 9 + 10x10 + 2s = 111s
   replik(S12) = 9 + 11x10 + 2s = 121s
   replik(S13) = 9 + 12x10 + 2s = 131s
   replik(S14) = 9 + 13x10 + 2s = 141s

FİNAL VURUŞ KANITI:
   Ufka doğru yürüyen 2 astronot ve takip eden 1 uzaylı silueti · 145. saniye · 3 siluet · BULUNAN
DÖNGÜ KANITI: S00 (Göz Hizası Düşük Açı, gölge yürüyüşü) ↔ S14 (Düşük Açı, siluet yürüyüşü)
```

### 🧬 İNSAN ŞERİDİ

```
PLAN:  1 1 - 1 1 1 1 1 - 1 1 1 1 1 1  (1 = insan var · - = insansız S02/S08/S10)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         2 Astronot (Kaptan Vance - Mavi Şerit / Uzman Ray - Turuncu Şerit)
KASK          Altın yansımalı vizör berrak · sırt basınç tüpleri kask ile bütünleşik
NOVUM         TRAPPIST-1e Biyo-ışıldayan Taklitçi Fauna (İnsan kinetik ve ışık kopyalaması)
YERÇEKİMİ     0.7g
ATMOSFER      Purple dusk, violet crystalline regolith with bioluminescent cyan moss
EKRAN YÖNÜ    Astronot A solda, Astronot B sağda, Varlık merkezde/karşıda sabit
SAYAÇ         —
EŞ KADRAJ     S00 ↔ S10 (35mm Geniş Çekim), S01 ↔ S13 (50mm Orta Çekim), S05 ↔ S09 (85mm Detay Çekim)
YIPRANMA      0
IŞIK TAKVİMİ  Biyo-ışık modülasyonu ile dinamik dalgalanma (monoton kararma YOK)
SES REGISTER  HUMAN 11 · MACHINE 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI

```
KAPI          Dondurulmuş Kare Doğrulaması (Kapak Anı S09)
KOMUT         ffmpeg -ss 91 -i yatay_2_dk_filmler/THE_MIRROR_FAUNA/THE_MIRROR_FAUNA_BOLUM_2.mp4 -vframes 1 kanit_s09.jpg
DOĞRULANDI    ffmpeg 6.1.1 · 08.09.2026
İKAME         Manuel kare incelemesi
```
