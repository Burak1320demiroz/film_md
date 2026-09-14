# 🧠 LOOK_UP — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     LOOK UP — Part 1: THE BREACH [sahip verdi]
② FORMAT:   yatay 2-4 (120 sn) → kart §2.1 · bölüm sayısı 2
③ SAHNE:    12 sahneli (12 × 10 s) → formatın varsayılanı
④ REFERANS PAKETI: YAZILSIN (KAPI 0 aktif — LOOK_UP_REFERANS_PAKETI.md)
⑤ HİKÂYE ONAYI (14.09.2026): `00_HIKAYE_ONAYI.md` ONAY 14.09.2026 · TUR 1/3
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "Beş astronot kapıları savunurken düşmanın tavandan gelmesi, ilk saniyelerde anlaşılabilen güçlü bir ters köşe. Çatışma baştan mikro yerçekiminde geçecek. Astronotlar manyetik botlarla zemine, yaratıklar pençeleriyle yüzeylere tutunacak. Film: LOOK UP — Part 1: THE BREACH. Süre: 12 sahne × 10 saniye = 120 saniye. Tür: Uzayda kuşatma / yaratık gerilimi. Tema: Hayatta kalmak, her yönü kontrol etmekten değil, birbirini bırakmamaktan geçer."
REPLİK: var (12 replik — kask içi telsiz ve fısıltı)
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| Tavandan 10 yaratık | Mikro yerçekiminde düşme yönü yoktur | Yaratıklar tavan ızgarasından ve havalandırmadan yüzeyden itişle fırlar | 0g fiziğine tam uyum [D168] |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 2-4 (12 sahne) → §2.1 kartı
ORTAM:         4 (Uzay / Yörünge İstasyonu) → tetiklediği zorunlu satırlar: 0g bot kilidi, kask şeffaflığı, acil kırmızısı
TÜR:           bilimkurgu · dal: uzayda kuşatma / yaratık gerilimi
KLİP SÜRESİ:   10 s (araçtan ölçüldü)
SAHNE SAYISI:  12    RUNTIME: 120 s = hook + (12−1) × 10 s
BÖLÜM SAYISI:  2 (LOOK_UP_BOLUM_1.md: S01-S06, LOOK_UP_BOLUM_2.md: S07-S12)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Basınçlı istasyonda mikro yerçekiminde yüzeyden itişle saldıran tavan yaratıkları karşısında tutunma ve emniyet hatlarıyla tahliye asansörünü savunmak.
NOVUM TAŞIYICISI:    Noah's composite shield & short safety tether × team rescue anchoring → ceiling breach survival
① TEK KARE:          Tavan ızgarasından sarkan yaratık pençesi ve açıkta sallanan emniyet hattı.
② KİNETİK BAĞIMSIZLIK: Karakterlerin tutunma, kilit bırakma ve savrulma hareketleri ile yaratıkların yüzeyden itiş ve tutunma eylemleri diyalogsuz tamamen okunuyor.
③ BAŞLIK ŞEMASI:     LOOK UP (≤5 kelime)
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — Birbirini bırakmamak, hayatta kalma ihtimalini ortak bir sorumluluğa dönüştürür.
▸ tanım cümlesi — Yörünge istasyonunda bireysel kaçış imkânsızlaştığında, güvenliği birbirine bağlamak hayatta kalmanın tek garantisidir.
▸ depoda kaç kez kullanıldı — 4 (TEMA DAĞILIMI: Dayanışma ve ortak sorumluluk)
▸ motif kanalları — Emniyet kordonu kilitleri · Mara'nın dikey kask şeridi · Asansör kabin eşiğinde el tutuşu
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| R1 | Evet | 5 astronot kask giysisi devamlılığı | Referans paketi R1 ( Mara, Noah, Cole, Jun, Eren) ile | Düşük |
| R2 | Evet | 10 kömür siyahı 4 uzuvlu yaratık | Referans paketi R3 & C10 gri çiziği kilidi ile | Düşük |
| R3 | Evet | Emniyet hattı sıkışması ve kalkan devri | Referans paketi R5 (Kalkan & Makara) ile | Düşük |
| R4 | Evet | 0g mikro yerçekimi hareket fiziği | Bot mekanizması ve tavan braketi takılması ile | Düşük |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  Yaratık anatomisi ve kadro devamlılığı
POZİTİF BİÇİMİ:   Tam olarak 5 insan karakter (Mara, Cole, Jun, Eren, Noah) ve tam olarak 10 kömür siyahı 4 uzuvlu yaratık (C01-C10). C10'un sol omzunda tek gri çizik (longitudinal gray scratch).
```

```
TETİKLENEN RİSK:  4 / 4
EŞİK:             5
✅ EŞİĞİN ALTINDA: Tasarımla tüm riskler kontrol altına alındı.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — soru ④ "analiz karar versin" / "YAZILSIN"

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | Evet | 5 astronot giysisi |
| T2 | biçim kilidi METİNLE tutulmayan varlık | Evet | Kömür siyahı 4 uzuvlu yaratık |
| T3 | oranı sözle yazılamayan nesne | Evet | Kompozit kalkan (65×42 cm) |
| T4 | insan dışı canlı | Evet | Yaratıklar (C01-C10) |
| T5 | tekrar eden insan dışı olay | Evet | Tavandan yüzeyden itişli fırlayış |
| T6 | bir varlık tekrar tekrar dönüyor | Evet | C10 (S03 ve S12'de sol omuz çiziğiyle) |

```
KARAR: YAZILIR (LOOK_UP_REFERANS_PAKETI.md aktif ve ✅ GO durumunda).
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S09 (Kordon kesme ve kalkan devri)
NÖTR TARİFİ:         A guarded synthetic line cutter slices the braided belt tether with one clean stroke, while the off-white chamfered composite shield is transferred from forearm latch to hand grip.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Beş kişi olarak tahliye asansörüne ulaşmak ve istasyondan kaçmak.
ENGEL:   Tavandan giren ten kömür siyahı yaratıklar ve mikro yerçekimindeki savrulma.
BEDEL:   Cole'un bot kilidi kopar (S02), Noah açıkta savrulur (S06), Mara'nın sol omzu zorlanır (S08), kalkan ezilir (S10).
MUHATAP: Noah (genç üye) ve Mara (komutan).
AYRILIK: S07 (Mara açık kaçış yolunu bırakıp açıkta sallanan Noah'a dönmeyi seçer).
```

---

## ✅ KAPI

```
[x] konsept kapısı ①②③ üçü de ✅
[x] risk sayımı yazıldı ve eşik kararı verildi
[x] B5 dörtlüsü tam, BEDEL sahne numarası taşıyor
→ üçü de ✅: 03_SAHNE_SIRALAMASI.md yazılabilir.
```
