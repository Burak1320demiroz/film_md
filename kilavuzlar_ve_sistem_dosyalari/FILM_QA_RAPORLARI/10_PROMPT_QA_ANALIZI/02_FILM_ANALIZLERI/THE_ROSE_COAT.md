# 🧩 THE_ROSE_COAT — prompt hata analizi

```
FORMAT      yatay 2 dk · 13 sahne · ızgara sahne(n) = n × 10 s
HAM RAPOR   5/5 geçerli · BULGU 15 → tekil 15
HÜKÜM       🅐 3 · 🅑 12 · 🅒 0 · 🅓 0      🅑/(🅐+🅑) = %80
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 13/13: bloom · g-sayı · kamera
  KISMİ: metin 12/13 · efor 1/13 · g-ad 2/13 · filigran 12/13
  ⛔ HİÇ YOK: SES · dış-ses · sayı · temas · giysi · parçacık
  bulgulu sahnelerde eksik: SES 0/11 · dış-ses 0/11 · sayı 0/11 · temas 0/11 · giysi 0/11 · parçacık 0/11 · metin 10/11 · efor 1/11 · g-ad 2/11 · filigran 10/11
```

---

## 🅑 SINIF 1 — PROMPTUN KENDİ KELİMESİ EKRANA YAZILDI · 2 🔴 ⭐⭐ KAPIYA DÖNER

S07 🔴 ×2: *"The word **'rose'** spontaneously generates on the …"* /
*"Text visible on screen: the word 'rose' clearly appears."*

**Promptta ne yazıyordu:** `rose` kelimesi tek dosyada **139 kez** (`rose-pink coat`
· `rose-stained`). Metin yasağı 12/13'te yazılı; motor yine de **en sık tekrarlanan
ayırt edici kelimeyi** kadraja yazı olarak bastı.

⭐ **Üçüncü vaka.** THE_PAYLOAD'da `PHASE 1` göğse, `EVA` sırta basıldı.
Burada `rose` ekrana. Üç film, üç farklı jeton, aynı mekanizma:

```
promptta ÇOK TEKRARLANAN kısa ve ayırt edici bir kelime → motor onu YAZI sanır
```

**Hüküm 🅑 ×2.** Yazım kuralı: ayırt edici kelime **tek başına bırakılmaz**, her
geçtiği yerde bir nesneye bağlanır (`rose-pink` değil `a rose-pink quilted coat`);
metin yasağı ayrıca o kelimeyi **adıyla** dışlar. ⛔ Kapı önerisi: `04_` § JETON SIZINTISI.

## 🅑 SINIF 2 — TEMAS 0/13 · 5 🔴

S04 🔴 (*"the physical brush phases entirely through …"*) · S08 🔴 (*"solid passing
through solid"*) · S12 🔴 ×2 (*"climbing the ladder, hands phase directly through"*) ·
S06 🔴 (*"anatomical breakdown as the character ascends"*).

## 🅑 SINIF 3 — ORTAM ADI 2/13 · 3 🔴 · 2 🟠

Ölçüm: ortam SAYISI **13/13'te yazılı** (`0,4 g`), ortam ADI yalnız 2/13'te.
Sayı var, hangi ortamda geçerli olduğu yok.

S00 🔴 ×2 (*"sand pours continuously from a narrow flat geometric …"*) ·
S01 🔴 (*"the character slides/moonwalks"*) · S03 (*jello/glide*) ·
S07 (*"impact lacks weight"*) · S05 (*"sand falling off the hull behaves as a …"*).

## 🅑 SINIF 4 — IŞIK VE DOKU · 2 🟠

S02 (*gömülü nesnenin gölgesi uyuşmuyor*) · S09 🔴 (*doku yüzmesi*).

---

## 🅐 MODEL SAPMASI · 3

Bloom ve kamera cümlesi 13/13'te yazılı olduğu hâlde S03 jello ve S09 doku yüzmesi;
filigran 12/13.

## 🎯 ÜÇ SATIR

```
1. 🅑 ORANI %80 — çekirdeğin altı cümlesi hiç yok.
2. "ROSE" KELİMESİ EKRANA BASILDI. 139 tekrar; üçüncü jeton sızıntısı vakası.
3. TEMAS 0/13 VE BEŞ 🔴. Tek cümle, beş BLOCKER.
```
