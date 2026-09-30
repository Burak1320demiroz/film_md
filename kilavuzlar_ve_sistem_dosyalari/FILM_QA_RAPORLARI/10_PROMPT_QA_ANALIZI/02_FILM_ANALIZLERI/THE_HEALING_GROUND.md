# 🧩 THE_HEALING_GROUND — prompt hata analizi

```
FORMAT      yatay 2 dk · 14 sahne · BULGU 11 → tekil 11
HÜKÜM       🅐 3 · 🅑 8 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %73
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 14/14: SES · sayı · bloom · metin · g-sayı · filigran · kamera
  KISMİ: temas 2/14 · parçacık 1/14 · efor 13/14 · g-ad 1/14
  ⛔ HİÇ YOK: dış-ses · giysi
  bulgulu sahnelerde eksik: dış-ses 0/7 · temas 2/7 · giysi 0/7 · parçacık 1/7 · g-ad 0/7
```

## 🅑 SINIF 1 — GİYSİ İŞARETLERİ SAYILMIYOR · 3 🟠 ⭐ [D78/D151]
| S | bulgu |
|:--:|---|
| S06 | *Suit in S1 has **4 yellow bands** and top helmet lights; S7 has **1 yellow band*** |
| S10 | *S1 has yellow bands and a ribbed chest box; S11 has **zero** yellow bands* |
| S13 | *S1 has a chest box and helmet lights; S14 lacks the chest box entirely* |

Giysi cümlesi 0/14. Üç bulgunun üçü de **sayılabilir bir işaretin** sayısını
değiştiriyor: bant sayısı hiçbir promptta rakamla yazılmamış.

**Yazım kuralı:** giysinin üzerindeki her tekrar eden işaret **rakamla** yazılır
(`four yellow bands across the chest`) ve Bible'dan birebir kopyalanır.

## 🅑 SINIF 2 — TEMAS 2/14 · 2 🟠 · SINIF 3 — MEKÂN · 1 🟠
S03 ×2 (*sağ el parmakları göğüs kumaşına karışıyor*) ·
S11 ⑤ (*"S2 establishes a single receding line of domes; S12 shows two symmetrical
flanking rows"*).

## 🅑 SINIF 4 — AĞIZ KADRAJDA VE REPLİK VAR · 2 🟠 ⭐ tek vaka
S11 ×2 (*"Lip sync is minimal and stiff; the mouth lacks proper articulation"*).
Ağzın kadrajda olduğu ve konuştuğu bir sahne yazılmış — deponun bu riski
(`SES_VE_DIYALOG` §1a.1) tam olarak bunun için var: **bedenleştirme doruğa
saklanır**, kurulum sahnesinde harcanmaz.

## 🅐 MODEL SAPMASI · 3
S00 ×2 · S09 ⑧ *EFFORTLESS HEAVY* — efor cümlesi 13/14'te yazılı.

## 🎯 ÜÇ SATIR
```
1. SARI BANT SAYISI ÜÇ KEZ DEĞİŞTİ. Sayılabilir işaret rakamla yazılmamış.
2. AĞIZ KADRAJDA KONUŞUYOR. Lip-sync riski bilerek açılmış, iki bulgu.
3. TEMAS 2/14 · PARÇACIK 1/14 — çekirdeğin iki cümlesi neredeyse yok.
```
