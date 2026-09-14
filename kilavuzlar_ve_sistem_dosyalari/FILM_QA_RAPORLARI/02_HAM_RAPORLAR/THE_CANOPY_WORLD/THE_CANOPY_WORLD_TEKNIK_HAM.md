# 📄 THE CANOPY WORLD — TEKNİK (VIDEO) QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/VIDEO_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 31 Temmuz 2026 · **Skor:** 3/10 · **Verdikt:** REGENERATE
> **Durum:** ⚠️ ŞARTLI — SPEC bloğu boş çalıştı (ama dürüstçe bildirdi)
> **Eş rapor:** [`THE_CANOPY_WORLD_MANTIK_HAM.md`](THE_CANOPY_WORLD_MANTIK_HAM.md)

---

# 🎯 BU RAPORUN ASIL DEĞERİ SKORU DEĞİL

Bu, **projede aynı filmin ikinci kez ölçülmesi.** The Canopy World kalite
tablosunda zaten 4/10 ile duruyordu. Aynı film, aynı kurgu, aynı rubrik —
farklı çalıştırma.

## 📏 ÖLÇÜM GÜVENİLİRLİĞİ — projenin ilk gerçek verisi

| Kategori | 1. ölçüm | 2. ölçüm | Fark |
|---|:--:|:--:|:--:|
| Karakter | 7 | 5 | **−2** |
| Fizik | 5 | 4 | −1 |
| Kamera | 2 | 3 | +1 |
| Işık | 6 | 4 | **−2** |
| Çevre | 7 | 6 | −1 |
| Canlı | 4 | 3 | −1 |
| Hareket | N/A | 4 | — |
| **GENEL** | **4/10** | **3/10** | **−1** |

```
ORTALAMA MUTLAK SAPMA:  1.33 puan  (6 karşılaştırılabilir kategori)
EN BÜYÜK SAPMA:         2 puan     (Karakter ve Işık)
YÖN:                    6 kategorinin 5'i AŞAĞI — sistematik sapma,
                        rastgele değil. İkinci rubrik daha sert.
```

## 🚨 BUNUN KALİTE TABLOSUNA ETKİSİ

```
Tablonun çözünürlüğü ±1.3 puan. Yani:

❌ ARTIK SÖYLENEMEZ:  "Kaleida 4.5, Hollow 4.0 — Kaleida daha iyi"
                      1.3 sapma varken 0.5 fark gürültüdür.
                      Tablo filmleri BİRBİRİYLE SIRALAYAMAZ.

✅ HÂLÂ SÖYLENEBİLİR:  "Kamera Low Power'da 8 — ortalama 4.2"
                       3.8 puanlık fark, gürültünün 3 katı. Sinyal gerçek.

✅ HÂLÂ SÖYLENEBİLİR:  "Fizik 11 filmin 11'inde 5 ve altında"
                       Tek filmin ±1.3'ü, 11 filmlik örüntüyü bozmaz.

⚠️ DİKKAT:             "Işık ilk üç filmde 6, sonra hiç 6 olmadı"
                       Bu filmin ışığı ikinci ölçümde 6 → 4 düştü.
                       Yani o "ilk üç film daha iyiydi" örüntüsü,
                       kısmen ölçüm sapması olabilir. Zayıfladı.
```

**Kural (bundan sonra):** Kalite tablosundaki iki skor arasındaki fark
**1.5 puandan küçükse, fark yoktur.** Aynı film iki kez ölçüldüğünde
bu kadar oynuyor.

---

# ⚠️ SPEC BLOĞU BOŞ ÇALIŞTI

```
SPEC BLOCK PROVIDED: NO — all fields unverified
FORMAT: [UNVERIFIABLE]
```

STEP 0 kapısı SPEC'in plan dosyasından kopyalanmasını istiyor. Kopyalanmamış.
**Ama rapor bunu gizlemedi:** Diyalog ve Kare Çapası kategorilerine `N/A —
UNVERIFIABLE` yazdı, uydurma puan üretmedi. The Slow Stone'un boş-SPEC
raporları var olmayan bir "Faz 5" puanlamıştı; bu rapor o hataya düşmedi.

→ **ŞARTLI kabul.** Bulgular geçerli (hepsi ekranda görünür şeyler),
skor tablosuna ikinci ölçüm olarak kaydedildi, ilk satırın yerine geçmedi.

Doldurulabilecekken doldurulmamış alanlar — dosyada hepsi var:
```
FORMAT: 2-4dk          SCENE: Compilation      PIPELINE: text-to-video
GRAVITY: 0.85g fixed   ATMOSPHERE: dense, oxygen-rich (ses taşır)
CHARACTER: Dr. Yaprak Orman — koyu zümrüt tırmanış suiti, biyolüminesan
           sarı-yeşil dikiş şeridi, tam şeffaf vizör
SUIT: katlanabilir kanat membranı (sadece süzülürken açık) + yaylı halat
      makarası (otomatik toplanır) + kalıcı kalça/göğüs kemeri
```

---

# ✅ MANTIK RAPORUYLA ÇAKIŞMA: SIFIR

İki rapor aynı gün, aynı filme, iki ayrı rubrikle çalıştı.
Ortak bulgu sayısı: **0.** Kapsam sınırı blokları çalışıyor —
iki rapor çift sayım olmadan toplanabilir. Ayrıntı: mantık ham dosyası.

---

# 🔁 DERS DOĞRULAMASI — dikkatli okunmalı

Rapor `[1, 2, 3, 24, 33]` derslerine işaret ediyor ve haklı. **Ama bu,
"ders tutmadı" demek değil:**

```
Ders 1, 2, 3, 5, 6, 7, 9 ZATEN BU FİLMDEN çıktı.
Bu görüntü, o dersler yazılmadan ÖNCE üretildi.
Aynı görüntüde aynı hatayı yeniden bulmak, dersin işe yaramadığını
göstermez — sadece ilk bulguya nihayet TIMESTAMP verir.

Bir dersin çalışıp çalışmadığı, ancak o ders yazıldıktan SONRA üretilen
bir filmde ölçülebilir.
```

**Bu raporun gerçek katkısı:** 8 dersin kaynağı olan filmin ham bulguları
kayıptı. Artık zaman damgalı:

| Ders | Nihayet timestamp'i var |
|:---:|---|
| 1 | `0:20 — sert kesme, wingsuit → yaprak koşusu` |
| 2 | `1:06 — yosun canlısı iki ayaklıdan dört ayaklıya morph` |
| 3 | `1:12 — parlayan yosun temasında şiddetli bloom` |
| 5 | `0:32 — baş dönüşünde vizör camı kayboluyor` |
| 6 | `0:54 — yüzen mantarlar kenarlarından nefes alıyor/warp` |
| 7 | `1:42 — su sıçraması deforme olmuyor, katı geometri gibi` |
| 9 | `2:10 — jenerik kartı metni` |

---

# 🚨 2:10 — JENERİK KARTI, PLANDA YOK

Plan dosyası 12 sahne. Kurguda 13. sahne bir başlık kartı.
Mantık raporu da bunu S13 olarak envantere yazdı (puanlamadan).

```
→ Ders 9 (videoda yazı) ihlali · Ders 34 (jenerik kartı) örüntüsü
→ Kaynak: model, kurgunun sonuna kendi başlık kartını ekliyor
→ Kurguda kesilir. Maliyet: 0. Ama plan dosyasında da yok — yani
  kimse istememiş, model kendiliğinden koymuş.
```

---

# 📥 HAM ÇIKTI (değiştirilmeden)

FILM: The Canopy World
FORMAT: [UNVERIFIABLE]
SCENE: Compilation
VIDEO DURATION: 134 seconds
SPEC BLOCK PROVIDED: NO — all fields unverified; relying on visual baseline.

OVERALL SCORE: 3/10
VERDICT: REGENERATE

## SCORES SUMMARY

| Category | Score | Critical Issues |
|----------|:-----:| --------------- |
| Character | 5/10 | Visor clipping; waxy skin. |
| Scale & Physics | 4/10 | Float physics; rigid liquid. |
| Camera | 3/10 | 🔴 BLOCKER: Multiple hard cuts. |
| Lighting | 4/10 | 🟠 MAJOR: AI Bloom on moss. |
| Environment | 6/10 | 🟠 MAJOR: Background texture swim. |
| Creatures | 3/10 | 🔴 BLOCKER: Anatomy morphing. |
| Particles & Materials | 4/10 | 🟠 MAJOR: Solid water splashes. |
| Dialogue & Audio | N/A | [UNVERIFIABLE] |
| Frame Anchor Fidelity | N/A | [UNVERIFIABLE] |
| Negative Violations | 4 | Cuts, bloom, text, morphing. |
| Motion Quality | 4/10 | 🟠 MAJOR: Jello effect. |

## SEVERITY TALLY
🔴 BLOCKER: 3    🟠 MAJOR: 4    🟡 MINOR: 3

## TOP 3 CRITICAL ERRORS (most impactful)
1. 0:20 — 🔴 BLOCKER — Camera: Multiple hard cuts violate single-cut rule.
2. 1:06 — 🔴 BLOCKER — Creatures: Moss beast morphs biped to quadruped.
3. 2:10 — 🔴 BLOCKER — Negative Violation: Burned-in text overlay.

## DETAILED ERROR LOG
0:20 — 🔴 BLOCKER — Camera — Hard cut from wingsuit to leaf running.
0:24 — 🟠 MAJOR — Physics — Character floats; no weight transfer on leaf.
0:32 — 🟡 MINOR — Character — Visor glass vanishes during head turn.
0:45 — 🟠 MAJOR — Motion — Legs warp (jello effect) during vine swing.
0:54 — 🟠 MAJOR — Environment — Floating mushrooms warp/breathe at edges.
1:06 — 🔴 BLOCKER — Creatures — Background monster structure morphs entirely.
1:12 — 🟠 MAJOR — Lighting — Severe AI bloom on glowing moss contact.
1:15 — 🟡 MINOR — Character — Plastic/waxy skin texture under green light.
1:42 — 🟠 MAJOR — Particles — Water splashes do not deform; behave like solid geometry.
2:10 — 🔴 BLOCKER — Negative Violation — Title card text appears.

## WHAT WORKED WELL (keep these in future prompts)
- High-contrast color palette in the bioluminescent cave.
- Static crab-like creatures hold structural integrity nicely.

## PROMPT IMPROVEMENT SUGGESTIONS
1. ADD to video prompt: "Single unbroken take, continuous camera pan, no cuts." → prevents camera resets.
2. REMOVE from image prompt: "Cinematic lighting, glowing, magical." → causes AI bloom and waxy skin.
3. REPLACE "water splashing" with "fluid dynamics, liquid displacement, continuous micro-motion" → prevents solid water geometry.

## NEW LESSON CANDIDATE
No new lesson — all errors map to existing lessons [1, 2, 3, 24, 33].

## QUALITY TABLE ROW
| The Canopy World | Compilation | 5/10 | 4/10 | 3/10 | 4/10 | 6/10 | 3/10 | 4/10 | **3/10** |
