# 📋 THE_SHADOW_LINE — QA SPEC (rubriklere yapıştırılacak tek dosya)

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_SHADOW_LINE
FORMAT:            yatay_2_dk_filmler
RUNTIME:           130 seconds
SCENE COUNT:       13
PART GRID:         —
THEME:             FEDAKÂRLIK
THEME SCENES:      S00 · S09 · S10 · S12
INTENDED EMOTION:  Gerilim, çaresizlik, bilinçli fedakarlık, başarma ve bedel
ENDING TYPE:       Kalıcı Fiziksel Bedel (Yanık eldiven ve yumruk kilitlenmesi)
PROTAGONIST:       Mühendis Astronot (isimsiz)
CENTRAL CHOICE:    Mühendisin elini ölümcül Güneş plazma ışığına fırlatarak soğutma emniyet mandalını kaldırması (S10)
DIALOGUE LINES:    0
SILENT SCENES:     S00 - S12
VIRAL INTERSTITIALS: S00, S06, S10, S12
TITLE:             THE SHADOW LINE (Gölge Hattı)
LIBRARY CONTEXT:   THE_SOLAR_MIRROR, THE_CRACKED_HELMET, THE_LAST_SHIFT, THE_HARD_DOCK
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      13
SHOT COUNT:      13
TARGET ASL BAND: 10.0 s saniye sabit ritim
GRID:            sahne başlangıcı(n) = (n−1) × 10.0s (S00 = 0.0s, S01 = 10.0s, ..., S12 = 120.0s)
RUNTIME:         130s
RAW FOOTAGE:     130s
SCREEN TEXT:     0 saniye
CAMERA:          El kamerası takipleri ve kilit yakın çekimler
SETUP SEQUENCE:  A A B B A B A B C C B C B
KURULUM İSKELETİ: A A B B A B A B C C B C B
KÜME:            3 adet (S00-S01, S02-S03, S08-S09)
DÖNÜŞ:           7 adet (%53.8) (S04, S05, S06, S07, S10, S11, S12)
ANGLE ARC:       3 açı tipi (Bel Hızası, Düşük Açı, Üst Açı)
DORUK:           S10 → Plazmada Bedel (sahne başlangıcı 100.0 s)

FİNAL VURUŞ KANITI: Scorched space glove fingers locked in a rigid fist · 128.0s · 1 right hand · BULUNAN
DÖNGÜ KANITI: S00 eldiven makrosu plazma ışığında ↔ S12 eldiven makrosu gölgede (Açılış-kapanış kafiyesi)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1 1 1 1
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (Mühendis Astronot)
KASK          Altın yansıtmalı kapalı vizör · sırt ünitesi yok — düz beyaz kabuk · zero tint, optically clear, fully readable through
NOVUM         Güneş plazma ışığının esnek uzay giysisi eklemlerini yok etmesi ve kayan gölge hattı
YERÇEKİMİ     0 g (Uzay vakumu)
ATMOSFER      0 Pa (Vakum)
EKRAN YÖNÜ    Hedef hep Ekran Sağı (Soğutma Valfi) · ilerleme Soldan Sağa (13/13 sahne sabit)
SAYAÇ         Güneş gölge hattı açısı ve konumu (monotonik sağa kayma)
DÜNYA ÇAPASI  3/3 — Güneş plazma parıltısı · zifiri siyah uzay · istasyon kaportası ve vanası
YIPRANMA      Eldiven parmakları ve bilek esnek eklem yerlerinde termal kavrulma (S10 sonrası kalıcı)
KİMLİK DİZİSİ kask K/K/K/K/K/K/K/K/K/K/K/K/K · amblem SOL omuz · giysi beyaz kabuk · kararma S10 başlar
IŞIK TAKVİMİ  Sert turuncu plazma ışığı ve zifiri gölge kontrastı
SES REGISTER  HUMAN 0 · MACHINE 5 katmanlı uzay vakum mix
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Kamera Titreşimi ve Denge Kontrolü
KOMUT         ffmpeg -i S10.mp4 -vf vidstabdetect -f null -
DOĞRULANDI    ffmpeg 6.1 · 14.09.2026
İKAME         Manuel kurgu kontrolü
```
