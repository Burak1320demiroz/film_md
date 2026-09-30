INPUT MODE: D
FILM: THE_STATIC_VEIL
RUNTIME: ~02:04 ESTIMATED
FRAME RATE ASSUMED: 24 fps
GRID GIVEN: 0s + (n−1) × 10.0s
SCENES OBSERVED: 12 · CUTS COUNTED: 11 · CUTS OFF GRID: 0
NON-SCENE MATERIAL: 02:00–02:04 başlık kartı ("THE STATIC VEIL")
PRESENCE STRING: -11111111111
LINES HEARD: Replik yok — ortam sesi ve müzik mevcut
ZONES REGISTERED: 1 · MEDIUM: Vakum (0 Pa)
LIGHT JUMPS: 3 · CLEAN CUTS: 8

---

## ZONE REGISTER

```
ZONE REGISTER
· zone            [Bölge 1 · S00–S11 kapsar]
· sources         [1 · Sert Güneş Işığı · Sol-Üst Krater Kenarı / S11'de ilave Amber Pratik Fener]
· key direction   [Saat 10:00 · Düşük Yükselim]
· key quality     [Sert / Direkt]
· shadow          [Mutlak Siyah / Sert Kenarlı]
· temperature     [Soğuk-Nötr Gün Işığı / Pratik Fener: Amber]
· fill            [Yok / Sadece zemin regolit yansıması]
· medium          [Vakum (0 Pa) — Haze yok, volümetrik ışık hüzmesi yok, saçılma yok]
· change allowed  [S09: Elektrik Arkı Parıltısı · S11: Pratik Fener Amber Aktivasyonu]
```

---

## LIGHT LEDGER

S00 | 00:00–00:10 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Orta | Derin Siyah | 0
S01 | 00:10–00:20 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | 0
S02 | 00:20–00:30 | Bölge 1 | Saat 11:00 · Orta | Sert | Yarı Sert | Nötr Güneş | 0/1 lit | Parlak | Derin Siyah | 0
S03 | 00:30–00:40 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | 0
S04 | 00:40–00:50 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | 0
S05 | 00:50–01:00 | Bölge 1 | Saat 01:00 · Düşük | Sert/Yarı Sert | Yarı Kaldırılmış | Nötr/Sıcak | 0/1 lit | Parlak | Yarı Siyah | 0
S06 | 01:00–01:10 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | 0
S07 | 01:10–01:20 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | Anlık Ark Çakması (01:14)
S08 | 01:20–01:30 | Bölge 1 | Saat 10:00 · Düşük | Sert | Mutlak Siyah | Nötr Güneş | 0/1 lit | Normal | Derin Siyah | 0
S09 | 01:30–01:40 | Bölge 1 | Saat 09:00 · Orta | Yüksek Parlama | Mavi Işık Dolgusu | Mavi Ark | 0/1 lit | Yüksek | Mavi-Siyah | Elektrik Arkı (01:32)
S10 | 01:40–01:50 | Bölge 1 | Saat 02:00 · Orta | Yarı Sert | Kaldırılmış Gölge | Amber/Sıcak | 0/1 lit | Parlak | Yarı Siyah | 0
S11 | 01:50–02:00 | Bölge 1 | Saat 10:00 · Düşük | Sert/Saçılımlı | Hüzme Alanında Aydınlık | Amber + Güneş | 1/1 lit | Normal | Derin Siyah | Fener Hüzmesi (01:50)

---

## KEY DIRECTION STRING

```
OBSERVED:  00E001000920
ZONES:     AAAAAAAAAAAA
```

---

## PRESENCE STRING

`-11111111111`

---

## LIGHT JUMP LOG

| Kesme (Çıkış → Giriş) | Bölge | Ne Değişti | İlan Edilmiş Sınır mı? | Şiddet |
|---|---|---|---|---|
| S04 → S05 | A | Ana ışık açısı saat 10'dan saat 01'e kaydı, gölge içi siyahlık hafif yükseldi. | Hayır | 🟠 Orta |
| S08 → S09 | A | Yüksek voltaj elektrik arkı sebebiyle renk sıcaklığı soğuk maviye kaydı ve lokal pozlama sıçradı. | Evet (Doruk Sahnesi) | 🟢 İlan Edilmiş |
| S09 → S10 | A | Mavi elektrik arkı sönerek yakın planda amber renk sıcaklığı ve sağdan gelen ışık hakim oldu. | Evet | 🟡 Hafif |
| S10 → S11 | A | Fener amber ışık yaymaya başladı; vakum ortamına aykırı volümetrik ışık hüzmesi (haze) belirdi. | Evet (İlan Edilmiş Fener Aktivasyonu) | 🔴 Kritik |

---

## SCORES SUMMARY

| # | Kategori | Puan | Kaynak / İhlal (Ledger Satırları ve Zaman Kodları) |
|---|----------|------|--------------------------------------------------|
| 1 | Ana Işık Yönü Devamlılığı | 7/10 | 🔴 -3 · S05 (00:50) ve S10 (01:40) makro çekimlerde ana güneş ışığı açısı saat 10:00 konumundan sapmaktadır. |
| 2 | Gölge Kalitesi ve Dolgu | 6/10 | 🟠 -4 · S05 (00:50) ve S10 (01:40) sahnelerinde sert vakum ortamı yerine gölgeler yumuşatılmış ve kaldırılmıştır. |
| 3 | Renk Sıcaklığı | 8/10 | 🟡 -2 · S05 ve S10 yakın planlarında genel tonlamada hafif amber/sıcak kayma mevcuttur. |
| 4 | Pratik Kaynaklar | 9/10 | 🟡 -1 · S11'e kadar fener tutarlı biçimde sönük kalmış, S11'de amber renkte aktifleşmiştir. |
| 5 | Kesmelerde Pozlama | 8/10 | 🟡 -2 · S04→S05 ve S09→S10 geçişlerinde süje lokal pozlamasında sıçrama gözlenmektedir. |
| 6 | Klip İçi Stabilite | 9/10 | 🟡 -1 · S09'daki ark çakması haricinde klipler içinde ışık stabili korunmuştur. |
| 7 | Bölge Sınırları | 8/10 | 🟡 -2 · S09 ark çakması ve S11 fener aktivasyonu plana uygundur; ancak S11'deki ışık hüzmesi ortam sınırını ihlal eder. |
| 8 | Atmosfer Dürüstlüğü | 2/10 | 🔴 -8 · S11 (01:50–02:00) 0 Pa vakum ortamında olmaması gereken volümetrik amber ışık demeti / haze saçılması mevcuttur (Pattern ⑧). |

VERDICT: ZONE BROKEN

---

## THE THREE THAT MATTER

1. **01:50–02:00 (Vakum Ortamında Hacimsel Işık Hüzmesi / Pattern ⑧):** S11'de fener yandığında, SPEC'te ilan edilen 0 Pa vakum ortamında ışığı saçacak atmosfer olmamasına rağmen havada belirgin amber volümetrik ışık demeti (haze/glow) oluşmaktadır.
   *Çözüm:* S11 sahnesini, atmosferik saçılma/hüzme efektini kaldırıp fenerin sadece zemin ve yüzeylerde sert amber aydınlatma yapacağı şekilde yeniden üretin (regeneration).
2. **00:50–01:00 & 01:40–01:50 (Makro Çekimlerde Ana Işık Yönü Sapması / Pattern ①):** S05 ve S10 yakın planlarında ana güneş ışığı açısı genel sahnelerdeki saat 10:00 konumundan saat 01:00/02:00 konumuna kaymaktadır.
   *Çözüm:* S05 ve S10 sahnelerini ana ışık kaynağının sol-üstten (saat 10:00) geleceği açıya sadık kalarak yeniden üretin.
3. **00:50–01:00 & 01:40–01:50 (Vakum Şartlarında Gölge Siyahlarının Kaldırılması / Pattern ②):** S05 ve S10 makro çekimlerinde gölge içi pozlama seviyesi yükseltilmiş (lifted shadows), vakumun gerektirdiği mutlak siyah kontrast yumuşatılmıştır.
   *Çözüm:* Renk düzeltme (color grading) aşamasında S05 ve S10 sahnelerinin siyah seviyelerini (black level) ezerek vakum kontrastına çekin.

---

## FIXABLE IN THE GRADE vs REQUIRES REGENERATION

### Fixable in the Grade
* **S05 ve S10 Gölgeleri ve Renk Kayması:** S05 (00:50) ve S10 (01:40) sahnelerindeki hafif gölge siyah seviyesi yükselmesi (lifted blacks) ve renk sıcaklığı sapmaları renk düzeltme (grading) ile siyahlar ezilerek düzeltilebilir.

### Requires Regeneration
* **S11 (Atmosferik Hüzme):** S11 (01:50) sahnesindeki vakum içi hacimsel ışık demeti (volumetric beam) piksel düzeyinde atmosfere işlendiği için yeniden üretim (regeneration) gerektirir.
* **S05 & S10 (Ana Işık Açısı):** S05 ve S10 sahnelerindeki ana ışık yönü değişimi (saat 10:00 yerine saat 01:00/02:00) piksele işlenmiş gölge açıları içerdiğinden klibin yeniden üretilmesini gerektirir.

---

## FLAGS FOR DOCUMENT CHECK
* SPEC'te vakum ortamı (0 Pa) ilan edilmişken, S11'deki amber fenerin hacimsel ışık demeti oluşturması stilde hedeflenen bir görsel tercih midir, yoksa AI modelinin atmosfer varsayımından kaynaklanan bir hata mıdır?

---

## OUT-OF-SCOPE FLAGS
* **Fizik Merceği (Lens ⑥):** S00 sahnesinde regolit toz taneleri 0.16g yerçekimi altında çökmek yerine dik statik kolonlar halinde askıda kalmaktadır.
* **Devamlılık Merceği (Lens ②):** S02'deki kask vizör çizik kalıbı S04 ve S06 sahnelerindeki yakın planlarda hafif doku kayması göstermektedir.
* **Efor Merceği (Lens ⑧):** S09'da astronot yüzüne gelen yüksek voltajlı elektrik arkına rağmen hiçbir fiziksel irkilme veya tepki vermemektedir.
