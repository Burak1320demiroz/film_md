# 🧑‍🚀 THE COUNTED TURN — FİLM KAYDI

> **Durum:** film üretildi · **kurgu/yeniden üretim gerekiyor** ⚠️
> **Koşu:** 09.09.2026 · **on bir mercek** (① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN · ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK) — **hepsi mod D.**
>
> ⛔ **T TABLOLARI:** `rapor_kontrol.py` koşuldu — T1-T8, T11, T12 ⚠️ ŞARTLI, T10 ✅ GO etiketi aldı [D161/D162].
>
> **⑪ ölçüm kapısı (olcum_kapisi.sh):** 254.0s ölçüldü · 24 kesme (10.0s ızgarada) · 4:10-4:15 başlık kartı.

---

## 📦 MALZEME

```
MASTER:    THE_COUNTED_TURN (yatay_4_dk_filmler/THE_COUNTED_TURN/)
ÖLÇÜLEN:   254.0 s measured · 16:9 YATAY · COMPILATION
GÖVDE:     0:00-4:10 (25 klip × 10 s)
KART:      4:10-4:15 (5 s jenerik/başlık kartı "THE COUNTED TURN")
PLAN:      25 sahne · 249 s (THE_COUNTED_TURN_BOLUM_1.md + BOLUM_2.md)
SPEC:      THE_COUNTED_TURN_QA_SPEC.md ✅ VAR · MOD D koşuldu
```

---

## §⑪ ÖLÇÜM KAPISI VE ①.5 BETİK KOŞUSU

```
Betik: python3 kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/rapor_kontrol.py <7 rapor> --film yatay_4_dk_filmler/THE_COUNTED_TURN --rapor
Rapor: /Users/dai/github/apex_md/film_md/kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/RAPORLAR/THE_COUNTED_TURN_20260909_RAPOR_KONTROL.md

① KARE       : Düzeltilmiş Ortalama = 5.3 ⚠️ ŞARTLI (Ham: 6.5/10)
② DEVAMLILIK : Düzeltilmiş Ortalama = 3.0 ⚠️ ŞARTLI (Ham: 8.2/10)
③ SES        : Düzeltilmiş Ortalama = — (0 sayısal hücre) (Ham: 10.0/10)
④ HİKAYE     : Düzeltilmiş Ortalama = 5.6 ⚠️ ŞARTLI (Ham: 5.8/10)
⑤ ARKA PLAN  : Düzeltilmiş Ortalama = 7.0 ⚠️ ŞARTLI (Ham: 9.4/10) [Derin Tarama]
⑥ FİZİK      : Düzeltilmiş Ortalama = 8.6 ⚠️ ŞARTLI (Ham: 8.6/10) [Derin Tarama]
⑦ AKSİYON    : Düzeltilmiş Ortalama = 7.7 ⚠️ ŞARTLI (Ham: 8.2/10) [Risk Tetikli]

⑤ ÇAPRAZ KAPI SANITY:
- Kesme sayısı yayılımı: 0 (7 mercek de 24 kesme bildirdi)
- Replik ekseni: 7 mercek de 0 replik bildirdi
- Şerit ekseni: 25 hane (`1111110111111111101111110`)
- ①.9 Teslim kapısı: Plan 25 sahne, mercek çoğunluğu 25 sahne izledi — UYUMLU ✅
```

---

## 📊 SKOR ÖZETİ (mod D)

| Mercek | Ham Skor | Düzeltilmiş Skor (betik) | Kategoriler | Verdict |
|---|:--:|:--:|:--:|---|
| ① KARE | **6.5** | **5.3 ⚠️** | 6 | REGENERATE |
| ② DEVAMLILIK | **8.2** | **3.0 ⚠️** | 3 | IDENTITY BREAK |
| ③ SES | **10.0** | **— ⚠️** | 0 | SOUNDTRACK HOLDS (State B/C) |
| ④ HİKAYE | **5.8** | **5.6 ⚠️** | 8 | SHOOT WITH TRIMS |
| 🔬 ⑤ ARKA PLAN | **9.4** | **7.0 ⚠️** | 1 | FIELD HOLDS |
| 🔬 ⑥ FİZİK | **8.6** | **8.6 ⚠️** | 8 | MINOR SLIPS |
| 🎯 ⑦ AKSİYON | **8.2** | **7.7 ⚠️** | 7 | MINOR BLUR |
| 💪 ⑧ EFOR | **0.0** | **0.0 ⚠️** | 8 | NOBODY PAYS |
| 🎭 ⑩ OYUNCULUK | **3.4** | **3.4 ✅** | 9 | THE CHOICE IS INVISIBLE |
| 💡 ⑪ IŞIK | **8.4** | **6.8 ⚠️** | 4 | KEY WALKS |
| 🪝 ⑫ HOOK | **8.5** | **8.0 ⚠️** | 5 | THE STRANGER STAYS |

---

## 🔴 BLOCKER LİSTESİ (kırmızı — kurgu/üretim önce bunlar)

| Timecode | Kaynak | Bulgu | Eylem |
|---|---|---|---|
| 0:27 | ① | Sol el parmakları şiddetle kaynıyor ve kayış geometrisiyle eriyor | REGENERATE |
| 0:35 | ①⑦ | Sağ başparmak turuncu karabinerin masif metalinin içinden geçiyor | REGENERATE |
| 1:26 | ①⑦ | Gri kumaş kayış sağ eldiven ayasının içinden geçiyor | REGENERATE |
| 1:44 | ①⑦ | Kumaş kayış taban pininin içinden geçiyor | REGENERATE |
| 1:50 | ② | S12'de astronot erkek yüzünden pürüzsüz kadın yüzüne dönüşüyor | REGENERATE S12 |
| 2:00 | ② | S13'te astronotun beyaz uzay giysisi arkadan koyu deri cekete dönüşüyor | REGENERATE / EDIT CUT S13 |
| 2:10 | ② | S14'te kadın yüzü devam ediyor, turuncu kemer karabinaları kayıp | REGENERATE S14 |
| 2:44 | ① | Turuncu karabiner basıldığında ray metalinin içinden geçiyor | REGENERATE |
| 3:05 | ① | Gri kayış sağ eldivenin geometrisine gömülüyor | REGENERATE |
| 3:25 | ① | Sağ el parmakları turuncu karabiner metaliyle kaynaşıyor | REGENERATE |
| 4:10 | ① | Ekranda gömülü "THE COUNTED TURN" başlık kartı beliriyor (0.0s metin yasağı ihlali) | EDIT CUT / JENERİK TEMİZLE |

---

## 🟠 MAJOR BULGULAR

| Timecode | Kaynak | Bulgu | Eylem / Reçete |
|---|---|---|---|
| 0:05 | ⑥⑦ | S0'da ilk nesne düşüşü (1.1 s) planlanan 1.69 s kilidinden hızlı | Kurguda düşüş karelerini %30 yavaşlat (Speed ramp) |
| 1:17 | ① | Astronotun spoldan kalkış hareketi aşırı sert, rijit ve mekanik | REGENERATE |
| 1:50 & 2:10 | ② | Parlak turuncu kemer karabinaları MCU çekimlerde yok | REGENERATE S12/S14 |
| 2:50 | ⑥ | Heavy industrial strap lastik bant gibi sıvımsı dalgalanıyor (Material Amnesia) | Kurguda dalgalanma zirvesinden önce kes / REGENERATE |
| 3:30-3:40 | ⑦ | S21'de klipslerin takılması aksiyonu fiziksel olarak işlenmemiş (yalnız duruş var) | Kurgu veya yeniden üretim |

---

## 🟡 MINOR BULGULAR

| Timecode | Kaynak | Bulgu |
|---|---|---|
| 0:10 | ⑥ | Astronot adımları 0.12g itki için biraz ağır basıyor |
| 0:40 & 1:30 | ⑤ | Tünel kemerleri ile derin uzay yıldız alanı aynı hızda kayıyor (Flat-plate Parallax) |
| 2:54 | ① | Boş takip çekiminde metal ray üzerinde hafif doku kayması ve gölge oynaması |

---

## ✂️ ④ HİKAYE (30 SANİYE KESME REÇETESİ)

`SHOOT WITH TRIMS` kararı uyarınca filmi 250s'den 220s'ye indirecek öncelikli 3 kesme:

1. **S7 (1:00-1:10) — 10 saniye tasarruf:** Boş koridor geniş çekimi; tempoyu durduran gereksiz duraksamayı kaldırır. (Reçete: Vizör yansıması yakın planıyla değiştir).
2. **S8 (1:10-1:20) — 10 saniye tasarruf:** Spolda oturma/duraksama beat'i; karakterin ivmesini kırıyor. (Reçete: Aktif çekiş hareketiyle değiştir).
3. **S15 (2:20-2:30) — 10 saniye tasarruf:** Diz çökme beat'i; korunan S16 ile tamamen kopyadır. (Reçete: Kes ve doğrudan korunan S16'ya geç).

---

## 📐 ⑥ FİZİK VE SAYISAL KİLİTLER

```
GRAVİTE HESABI: a = 1.18 → 3.29 m/s² (0.121 g → 0.335 g)
PREMİS: Dönme yerçekiminde ağırlık YÖNE bağlıdır. Bırakılan nesne yana doğru sürüklenir.
```

| Kilit | Belirtilen | Ekranda Ölçülen | Δ | Sonuç |
|---|---|---|---|---|
| Yanal Düşüş Novum | Sabit sapma | 0:05 ve 3:16 düşüşleri yana kayıyor | 0 | PASS |
| S0 Düşüş Süresi | 1.69 s | 1.1 s | -0.59 s | **FAIL (L1)** |
| S23 Düşüş Süresi | 1.03 s | 1.0 s (S19'da) | -0.03 s | PASS |
| Kayış Sarkma Derinliği | S0 4cm → S24 11cm | Sahneler ilerledikçe derinleşiyor | 0 | PASS |
| Yıldız Dönme Hızı | 3.0 → 5.0 RPM | Gözle görülür şekilde hızlanıyor | 0 | PASS |
| Beldeki Klips Sayısı | S15 (6 adet) | 02:30'da 6 klips görünür | 0 | PASS |
| Pindeki Klips Sayısı | S24 (2 adet) | 04:00'da 2 klips pinde | 0 | PASS |

**KİLİT SONUCU: 7 kilit · 6 PASS · 1 FAIL**

---

## 🎬 DEVAMLILIK (② mercek) — DRIFT MAP & CONTRADICTION LOG

```
KARAKTER PASAPORTU:
  Astronot: Beyaz/açık gri uzay giysisi, turuncu kemer/harness, sakallı beyaz erkek.

KİMLİK KAYMALARI (DRIFT MAP):
  - Yüz Kimliği: S12 (1:50) ve S14 (2:10)'te pürüzsüz kadın yüzü, S19 (3:00)'da erkek yüzü geri dönüyor.
  - Kostüm Kimliği: S13 (2:00)'te arkadan koyu deri ceket görünümü, S14 (2:10)'te tekrar uzay giysisi.
  - Ekipman Kimliği: S12 ve S14 MCU çekimlerinde turuncu kemer klipsleri tamamen kayıp.
```

| Timecode A | Timecode B | Özne | Kategori | Çelişki | Şiddet |
|---|---|---|---|---|---|
| 0:10 | 1:50 | Astronot | Identity (Face) | Sakallı erkek yüzü ↔ Pürüzsüz kadın yüzü | 🔴 BLOCKER |
| 0:10 | 2:00 | Astronot | Costume Identity | Beyaz hantal uzay giysisi ↔ Koyu deri ceket | 🔴 BLOCKER |
| 0:10 | 1:50 | Astronot | Equipment | Turuncu kemer klipsleri var ↔ Klipsler yok | 🟠 MAJOR |

---

## 💡 PROMPT İYİLEŞTİRME ÖNERİLERİ

1. Video promptlarına ekle: `"Solid objects maintain strict collision boundaries; hands push against surfaces without penetrating them."` (nesne/el çakışmalarını önlemek için).
2. Video promptlarına ekle: `"Fabric straps rest on top of gloves and metal pins, obeying physical collision."` (kayış/ip geçişlerini önlemek için).
3. Promptlardan temizle: `"title card"`, `"cinematic titles"`, `"ending text"` ifadelerini tüm imaj ve video promptlarından çıkar.
