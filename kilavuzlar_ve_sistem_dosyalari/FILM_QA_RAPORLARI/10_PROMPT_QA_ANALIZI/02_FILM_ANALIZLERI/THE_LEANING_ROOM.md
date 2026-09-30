# 🧩 THE_LEANING_ROOM — prompt hata analizi

```
FORMAT      yatay 2 dk · 12 sahne · ızgara sahne(n) = n × 10 s (hook 10 s)
HAM RAPOR   8/8 geçerli · BULGU 19 → tekil 17
HÜKÜM       🅐 5 · 🅑 11 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %69
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  TAM 12/12: SES · temas · bloom · metin · filigran · kamera
  KISMİ: sayı 10/12 · parçacık 10/12 · efor 11/12
  ⛔ HİÇ YOK: dış-ses · giysi · g-ad · g-sayı
  bulgulu sahnelerde eksik: dış-ses 0/8 · sayı 7/8 · giysi 0/8 · parçacık 7/8 · g-ad 0/8 · g-sayı 0/8
```

---

## 🅑 SINIF 1 — GÖKYÜZÜNDEKİ CİSİM ÜÇ KEZ DEĞİŞTİ · 3 🔴 ⭐ [D209]

| S | bulgu |
|:--:|---|
| S05 🔴 | *Saturn-like planet vs giant Jupiter* |
| S06 🔴 | *Giant Jupiter vs eclipse ring* |
| S08 🔴 | *Eclipse ring vs giant Jupiter* |

**Promptta ne yazıyordu:** dünya çapası cümlesi yok. Pencerenin dışındaki gök
cismi her sahnede yeniden tarif edilmiş ve üç farklı şey olmuş — **12 sahnelik
bir filmde üç BLOCKER, tek eksik cümleden.**

**Hüküm 🅑 ×3.** ⭐ THE_AMBER_LATTICE ile aynı sınıf (orada gece/gündüz, burada
gezegen). **İki filmde tekrar → ders eşiği geçildi.**

## 🅑 SINIF 2 — TAKI/BİLEKLİK HANGİ KOLDA · 3 🟠

S02 (*ince sol bileklik ↔ geniş sağ manşet*) · S06 · S07 (*sağdan sola*).
Giysi cümlesi 0/12; asimetrik işaretin **hangi kolda** olduğu yazılmamış.

⭐ MARS_SON_CIKIS'te aynı bulgu (askı ve omuz yaması kol değiştiriyor).
**İki filmde tekrar.**

## 🅑 SINIF 3 — ORTAM NE ADIYLA NE SAYISIYLA YOK (0/12 · 0/12) · 2 🔴 · 1 🟠

S07 🔴 ×2 (*"a stone drops at 1 g; a background object falls diagonally **UPWARDS**"*)
· S09 (*"rope rigid when pulled, flexible as a pendulum later"*).

## 🅑 SINIF 4 — SES-GÖRÜNTÜ SENKRONU · 2 🟠

S07 (*"clatter SFX plays while the object flies upward"*) · S10 (*"stone clink
delayed vs hand contact"*). `AUDIO:` 12/12'de var ama **sesin hangi ana düştüğü**
yazılmamış.

## 🅑 SINIF 5 — NESNE KİMLİĞİ · 1 🟠

S07 (*"flat horizontal dial wheel vs vertical ship's wheel"*).

---

## 🅐 MODEL SAPMASI · 5

S10 🔴 (*"Fingers of the left hand melt and fuse into the small stones"*) ·
S10 (*taşlar birbirine eriyor*) · S05 (*gergin halat pirinç abajurun içinden
geçiyor*) — temas cümlesi 12/12'de. S01 ×2 (*buzlu gezegen boş karanlıktan
beliriyor*) — doku/bloom cümlesi 12/12'de.

## 🎯 ÜÇ SATIR

```
1. PENCEREDEN GÖRÜNEN GEZEGEN ÜÇ KEZ DEĞİŞTİ — üç 🔴, tek eksik cümle.
2. BİLEKLİK KOL DEĞİŞTİRİYOR. Asimetrik işaret hangi kolda, yazılmamış.
3. SES DOĞRU ANDA DEĞİL. AUDIO satırı var, zaman çapası yok.
```
