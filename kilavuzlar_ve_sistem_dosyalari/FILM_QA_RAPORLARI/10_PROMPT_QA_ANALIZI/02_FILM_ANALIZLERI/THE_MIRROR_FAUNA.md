# 🧩 THE_MIRROR_FAUNA — prompt hata analizi

```
FORMAT      yatay 2 dk · 15 sahne · BULGU 6 → tekil 6
HÜKÜM       🅐 1 · 🅑 5 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %83
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 15/15: bloom · metin · g-sayı
  KISMİ: sayı 13/15 · efor 4/15 · g-ad 3/15 · kamera 7/15
  ⛔ HİÇ YOK: SES · dış-ses · temas · giysi · parçacık · filigran
  bulgulu sahnelerde eksik: SES 0/5 · dış-ses 0/5 · temas 0/5 · giysi 0/5 · parçacık 0/5 · efor 2/5 · g-ad 1/5 · filigran 0/5 · kamera 4/5
```

## 🅑 SINIF 1 — KASK İÇİ IŞIK YAZILMAMIŞ · 1 🔴 · 2 🟠 ⭐ bu filme özgü
| S | bulgu |
|:--:|---|
| S11 🔴 | *Unmotivated red strobe inside the helmet* (⑪) |
| S10 | *Right-key → full silhouette backlight* (anahtar ışık kayboluyor) |
| S13 | *Red tint remains on the face* |

Kask içindeki ışığın **kaynağı ve rengi** hiçbir promptta yazılı değil; motor
kırmızı bir uyarı ışığı uydurdu ve sonraki sahnede yüzde bıraktı [D193].

## 🅑 SINIF 2 — VİZÖR HUD'U · 1 🔴
S11 🔴 (*"Red text and data characters are baked into the glowing visor HUD"*) —
metin yasağı 15/15'te var **ama vizörün ne göstereceği yazılmamış**; parlayan bir
HUD tarif edilmiş ve içi boş bırakılmış.

## 🅑 SINIF 3 — TEMAS 0/15 · 1 🟠
S07 (*"the left hand fuses and melts into the handle of the flare device"*).

## 🅐 MODEL SAPMASI · 1
S12 🔴 (*"The edit inserts an exact duplicate of the previous …"*) — kamera/tek
çekim cümlesi 7/15'te; bu sahnede yazılıydı.

## 🎯 ÜÇ SATIR
```
1. KASK İÇİ IŞIK UYDURULDU. Üç bulgunun üçü de kask içindeki kaynaksız kırmızıdan.
2. PARLAYAN HUD TARİF EDİLMİŞ, İÇİ BOŞ BIRAKILMIŞ — metin yasağı onu kurtarmıyor.
3. ÇEKİRDEĞİN ALTI CÜMLESİ YOK; filigran cümlesi bile 0/15.
```
