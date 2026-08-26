# 🔍 THE CANOPY WORLD — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_CANOPY_WORLD/THE_CANOPY_WORLD_PLANET_FILM.md`
> **Bu filmde ÜÇ ölçüm var:**
> · **TEKNİK QA #1** (aşağıda) — 4/10 · derslerden geri çıkarım, ham rapor kayıp
> · **TEKNİK QA #2** (31.07.2026) — **3/10** · [`../02_HAM_RAPORLAR/THE_CANOPY_WORLD_TEKNIK_HAM.md`](../02_HAM_RAPORLAR/THE_CANOPY_WORLD_TEKNIK_HAM.md)
> · **MANTIK QA** (31.07.2026) — **5/10** · [`../02_HAM_RAPORLAR/THE_CANOPY_WORLD_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_CANOPY_WORLD_MANTIK_HAM.md)
>
> 🎯 **Projede aynı filmin iki kez ölçüldüğü TEK vaka.** Bu, kalite tablosunun
> ne kadar hassas olduğunu söyleyen ilk veri: **±1.3 puan.** Aşağıya bak.

---

# 🔧 TEKNİK QA #1 — geri çıkarım

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Montaj (compilation) — sahne bazlı QA yapılmadı
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    4/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 7/10 | serinin en yüksek karakter skoru |
| Fizik | 5/10 | |
| Kamera | **2/10** | **serinin en düşük kamera skoru** |
| Işık | 6/10 | |
| Çevre | 7/10 | |
| Canlı | 4/10 | |
| Hareket | N/A | ölçülmemiş |
| Parçacık ve Malzeme | ⛔ kayıt yok | rubrikte var, tabloda yok |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ✅ tetiklendi (sayı bilinmiyor) | Ders 9'un kaynağı |

---

## 🧪 ÜRETTİĞİ DERSLER — 8 ders (serinin en verimli QA'sı)

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 1 | Tek çekim kuralı — AI kesiyor | 2/10 kamera |
| 2 | Canlı morph — arka plan canlıları değişiyor | 4/10 canlı |
| 3 | AI bloom — parlayan yüzeyler yıkanıyor | 6/10 ışık |
| 4 | Fizik — kayma ve süzülme | 5/10 fizik |
| 5 | Vizör kaybolması — kask cam tutarsızlığı | 7/10 karakter |
| 6 | Arka plan kararlılığı — çevre morph | 7/10 çevre |
| 7 | Su fiziği — sıvı etkileşimi | 5/10 fizik |
| 8 | Kıyafet değişimi — sahne arası tutarsızlık | 7/10 karakter |
| 9 | Metin — videoda yazı çıkmamalı | negatif ihlal |

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok — timestamp'li bulgu satırları kayıp
□ Hareket (Motion Quality) hiç puanlanmamış
□ 4 rubrik kategorisi (parçacık, diyalog, kare çapası, negatif sayısı) kayıt dışı
□ SPEC bloğunun dolu çalıştırılıp çalıştırılmadığı bilinmiyor
□ QA tarihi yok — hangi model sürümüyle üretildiği bilinmiyor
```

**Tekrar QA gerekli mi?** ✅ **YAPILDI — 31.07.2026.** Aşağıya bak.

---
---

# 🔧 TEKNİK QA #2 — 31 Temmuz 2026

> **Ham çıktı:** [`../02_HAM_RAPORLAR/THE_CANOPY_WORLD_TEKNIK_HAM.md`](../02_HAM_RAPORLAR/THE_CANOPY_WORLD_TEKNIK_HAM.md)
> **Skor:** 3/10 · **Verdikt:** REGENERATE · **Durum:** ⚠️ ŞARTLI (SPEC boş)

## 📏 İKİ ÖLÇÜM YAN YANA — projenin ilk güvenilirlik verisi

| Kategori | #1 | #2 | Fark |
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
ORTALAMA MUTLAK SAPMA: 1.33 puan · EN BÜYÜK: 2 puan
6 kategorinin 5'i AŞAĞI — sistematik sapma, rastgele değil
```

**Sonuç — kalite tablosu için kural:** iki skor arasındaki fark **1.5
puandan küçükse fark yoktur.** Bu, tablodaki "Kaleida 4.5 > Hollow 4.0"
türü karşılaştırmaları geçersiz kılar; "Kamera Low Power'da 8, ortalama
4.2" gibi büyük farkları etkilemez.

> ⚠️ **Bu filmin `Işık 6/10`'u artık şüpheli.** İkinci ölçüm 4 verdi.
> "İlk üç film ışıkta daha iyiydi" örüntüsü bu yüzden zayıfladı —
> ayrıntı: `../../URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md` §6b

## ✅ ASIL KAZANÇ: 8 DERSİN KAYIP HAM VERİSİ GERİ GELDİ

Bu kaydın en büyük eksiği "timestamp'li bulgu satırları kayıp" idi.
Artık 7 dersin kaynak karesi belli:

| Ders | Timestamp |
|:---:|---|
| 1 | `0:20 — sert kesme, wingsuit → yaprak koşusu` |
| 2 | `1:06 — yosun canlısı iki ayaklıdan dört ayaklıya morph` |
| 3 | `1:12 — parlayan yosun temasında şiddetli bloom` |
| 5 | `0:32 — baş dönüşünde vizör camı kayboluyor` |
| 6 | `0:54 — yüzen mantarlar kenarlarından warp` |
| 7 | `1:42 — su sıçraması deforme olmuyor, katı geometri` |
| 9 | `2:10 — jenerik kartı metni` |

> ⚠️ **Bu bir "ders tutmadı" kanıtı DEĞİL.** Görüntü, dersler yazılmadan
> önce üretildi. Aynı karede aynı hatayı bulmak, ilk bulguya nihayet
> timestamp vermektir. Bir ders ancak kendisinden SONRA üretilen filmde
> test edilebilir.

---
---

# 🧩 MANTIK VE DEVAMLILIK QA — 31 Temmuz 2026

> **Ham çıktı + doküman kontrolü:** [`../02_HAM_RAPORLAR/THE_CANOPY_WORLD_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_CANOPY_WORLD_MANTIK_HAM.md)
> **Skor:** 5/10 · **Verdikt:** FIXABLE IN EDIT · **Durum:** ✅ GEÇERLİ

| Kategori | Skor |
|---|:---:|
| Fiziksel Tutarlılık | 6/10 |
| Sayaç Mantığı | N/A |
| Uzamsal Coğrafya | 5/10 |
| Zaman ve Işık | 5/10 |
| **Kostüm ve Prop** | **4/10** |
| Nedensellik | 7/10 |
| Nicelik | 8/10 |
| Kurulum ve Terk | 7/10 |

## 🔎 DOKÜMAN KONTROLÜ — 2 soru cevaplandı, 1 reçete çürüdü

```
❓ "Doğrusal iniş mi, keşif montajı mı?"
✅ DOĞRUSAL İNİŞ. "the first human to descend Verdana's full seven-layer
   canopy in a SINGLE CONTINUOUS EXPEDITION". 7 katman: 3.000m → 0m.
   Ve kurgu sırası PLANLA BİREBİR AYNI — 12 sahnenin 12'si yerinde.

🚨 BU YÜZDEN RAPORUN EN BÜYÜK ÖNERİSİ GEÇERSİZ:
   Rapor "sahneleri ışığa göre grupla, maliyet düşük, kurgu işi" dedi.
   → Kurgu zaten doğru. Sıra = irtifa; ışığa göre gruplamak filmin
     önermesini yok eder.
   → Gerçek sorun: Kök Labirenti sahnesinin LIGHTING BIBLE'ı
     "cold blue-white light refracting through the crystal pools" diyor,
     ekranda "bright sunlit mangrove stream" var.
   → ÜRETİM hatası, kurgu hatası değil. Maliyet: yeniden üretim.

❓ "Katmana göre atmosfer/süzülme fiziği tanımlı mı?"
✅ İKİYE AYRILIYOR:
   · Havada yüzen canlılar TASARIM — "MIST JELLYFISH, 5-meter GAS-BLADDER
     drifting creatures" ve "LIGHT HUNTERS, anglerfish-analog".
   · Karakterin süzülmesi HATA — Physics Bible: "Gravity: 0.85g FIXED
     THROUGHOUT" + "The character MUST NEVER FLOAT."
```

## ⚖️ KOSTÜM BULGULARI — belge karşısında 3'ün 1'i ayakta

```
❌ Kanat membranı (0:30 vs 0:40) — REDDEDİLDİ
   Bible: "foldable wing-membrane ... DEPLOYABLE ONLY FOR CONTROLLED
   GLIDING between layers". Süzülürken açık, halatta kapalı = doğru.

❌ Halatın kaybolması — REDDEDİLDİ
   Bible: "SPRING-LOADED ROPE REEL — deploys and retracts AUTOMATICALLY."

✅ Emniyet kemeri (0:52) — KABUL, 🟡 → 🟠 YÜKSELTİLDİ
   Bible: "a COMPACT HARNESS AT HIP AND CHEST" — kalıcı ekipman,
   toplanmıyor. Üç kostüm bulgusundan tek gerçek olan bu.

✅ Suit ıslaklığı (1:42 → 1:52) — KABUL, belgeyle güçlendi
   Bible ıslaklığı katmana bağlı durum olarak zaten tanımlamış:
   "beading with moisture in the Root Labyrinth".

✅ Karakterin süzülmesi (0:53) — KABUL, 🟡 → 🟠 YÜKSELTİLDİ
   0.85g sabit + "must never float". Ders 4 ve 15 kapsamında.
```

## 🎯 KAPSAM SINIRI İLK KEZ SINANDI — VE TUTTU

Aynı gün, aynı filme, iki rubrik. **Ortak bulgu sayısı: 0.**
Teknik rapor kesme/bloom/morph/metin yazdı; mantık raporu bloom'u
`OUT-OF-SCOPE` satırına attı, jenerik kartını envantere yazıp puanlamadı.
İki rapor çift sayım olmadan toplanabiliyor.

## 📌 SONRAKİ ADIM

```
□ Kök Labirenti sahnesi yeniden üretilsin — katman ışığıyla uyumsuz
□ 1:50 sahnesinin ilk kareleri ıslak görünsün (veya sahne yeniden üretilsin)
□ 0:52 sahnesi yeniden üretilsin — emniyet kemeri kalıcı ekipman
□ 2:10 jenerik kartı kurguda kesilsin — maliyet 0, planda da yok
□ İkinci bir film de iki kez ölçülsün — sapmanın filme mi rubriğe mi
  bağlı olduğu ancak o zaman anlaşılır
```
