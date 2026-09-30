# 🧩 THE_PAYLOAD — prompt hata analizi

```
FORMAT      yatay 4 dk · 24 sahne · ızgara 9 s hook + (n−1) × 10 s
HAM RAPOR   6/6 geçerli · BULGU 23 → tekil 21
HÜKÜM       🅐 5 · 🅑 15 · 🅒 0 · 🅓 1      🅑/(🅐+🅑) = %75
KİLİT ENVANTERİ (betikle ölçüldü · prompt_hata_analizi.py --kilit)
  KISMİ: SES 22/24 · dış-ses 8/24 · sayı 23/24 · temas 3/24 · giysi 12/24 · parçacık 8/24 · bloom 22/24 · metin 21/24 · efor 23/24 · g-ad 2/24 · g-sayı 15/24 · filigran 21/24 · kamera 22/24
  bulgulu sahnelerde eksik: SES 7/8 · dış-ses 0/8 · sayı 7/8 · temas 2/8 · giysi 7/8 · parçacık 5/8 · bloom 7/8 · metin 6/8 · efor 7/8 · g-ad 1/8 · filigran 7/8 · kamera 7/8
```

---

## 🅑 SINIF 1 — PROMPTUN DEFTER ETİKETİ GİYSİYE BASILDI · 2 🔴 ⭐⭐ KAPIYA DÖNER

| S | bulgu |
|:--:|---|
| S01 🔴 | *Clear, legible text **"PHASE 1"** burned into the character's suit* (iki mercek ayrı yazdı) |
| S07 🔴 | *Text **"EVA"** printed on suit back* |

**Promptta ne yazıyordu:** filmin kendi **durum merdiveni etiketi**:

> `PHASE 1  only the boots and knees carry red dust;`

`PHASE 1` promptun **defter dili**dir — okuyucuya hangi aşamada olduğumuzu söyler.
Motor onu bir **giysi yazısı** sandı ve göğse bastı. `EVA` de aynı: 10 promptta
teknik kısaltma olarak geçiyor, motor sırta yazdı.

⭐ Bu ders **filmin kendi dosyasında zaten kayıtlı** (`THE_PAYLOAD_PART_A.md` sat. 202:
*"o etiket ölçüldü: model onu giysinin göğsüne BASTI"*) — ama yazım standardına
dönmemiş ve ikinci kez (EVA) tekrarlamış.

**Hüküm 🅑 ×2.** Yazım kuralı: prompt gövdesinde **BÜYÜK HARFLİ kısa jeton
yazılmaz** — ne `PHASE 1`, ne `EVA`, ne `S07`, ne `R3`. Defter dili prompt gövdesine
girmez; wear state düz cümleyle yazılır (`only the boots and knees carry red dust`).
⛔ Bu kapıya dönebilir: `04_KAPI_ONERILERI` § BÜYÜK HARF JETONU.

## 🅑 SINIF 2 — SAYILABİLİR NESNE KADRAJDA SAYILMIYOR · 2 🟠 [D78/D151]

S10 ×2: *"The long continuous row of cargo cases (approx 15) suddenly drops to
exactly 8."* Sandık sayısı hiçbir promptta **rakamla** yazılı değil.

## 🅑 SINIF 3 — TEMAS SINIRI 3/24 · 1 🟠 · 🅑 SINIF 4 — ORTAM ADI 2/24 · 3 🔴 · 3 🟠

S08 (*"Thumb merges into the metal strut"*). Ortam SAYISI 15/24'te var ama ortamın ADI yalnız 2/24'te — ve dört bulgu
doğrudan oradan: S15 🔴 ×3 (*"Cylinder falls at 1 g then randomly hovers in
0 g"*) · S07 ⑥ (*"dust falls at ~0,5 m/s² while the cargo case falls at ~9,8"*).

## 🅑 SINIF 5 — YÜKÜN BEDENDE VE SESTE KARŞILIĞI · 3 🟠

S07 ⑥ ×2 (*"massive cargo case impacts with zero recoil or dust displacement"* ·
*"zero biomechanical lean"*) · S07 ③ (*"lifts heavy cases visually, but the voice
sounds entirely rested"*) — **ses de yükü taşımıyor**.

## 🅑 SINIF 6 — ORTAM VE KİR DEVAMLILIĞI · 3 🟠

S02 ×2 (*güneş paneli tarlası tamamen kayboluyor*) · S11 (*dışarıda tozlu giysi
yatakta tertemiz*) · S02 (*göğüsteki "PHASE 1" yazısı kayboluyor*).

---

## 🅐 MODEL SAPMASI · 5

S10 🔴 ×2 (*"A duplicate of the protagonist walks through the background"*) —
insan sayısı 23/24'te yazılı. S12 (roket egzozu kütlesiz) — parçacık 8/24'te var.

## 🎯 ÜÇ SATIR

```
1. DEFTER DİLİ PROMPTA SIZDI. "PHASE 1" ve "EVA" giysiye basıldı — iki 🔴.
   Ders filmin kendi dosyasında yazılı ve yazım standardına dönmemiş.
2. ORTAM ADI 2/24, DÖRT BULGU. Bir silindir aynı sahnede hem 1 g hem 0 g.
3. SANDIK SAYISI PROMPTTA YOK. 15 sandık 8'e düştü; rakam hiç yazılmamış.
```
