# 🔍 THE INVERSION — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_INVERSION_PLANET_FILM.md`
> **Teknik QA (VIDEO_QA):** ❌ hiç yapılmadı
> **Senaryo QA (SENARYO_QA):** ✅ 5.0/10 · 31.07.2026 · ham rapor
> `../02_HAM_RAPORLAR/THE_INVERSION_SENARYO_HAM.md`
> **Mantık QA (MANTIK_QA):** ✅ **3.0/10** · 31.07.2026 · ham rapor
> `../02_HAM_RAPORLAR/THE_INVERSION_MANTIK_HAM.md`
>
> Teknik puanı hâlâ yok. Ama iki bağımsız rubrik aynı filmi ölçtü ve
> **ikisi de aynı 40 saniyelik tekrar döngüsünü buldu** — biri hikaye
> kusuru, diğeri kurgu hatası olarak. Bkz. Bulgu 2 ve Mantık §1.

---

# 📖 SENARYO QA

## 📋 KÜNYE

```
RUBRİK:        SENARYO_QA_CRITIQUE_PROMPT.md — 10 kategori
QA TARİHİ:     31 Temmuz 2026
GİRDİ:         yalnızca video
SPEC BLOĞU:    KISMİ — rapor "plan doc unsupplied" dedi
               🚨 OYSA PLAN DOSYASI DEPODA DURUYOR
SÜRE:          167 s (2:47)
GENEL SKOR:    5.0/10
KARAR:         SHOOT WITH TRIMS
GEÇERLİLİK:    ⚠️ ŞARTLI — kapı atlandı, doğrulama sonradan elle yapıldı
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Kanca | 6/10 | ⭐ Serinin ölçülmüş en iyi kancası — 10 saniyede anomali kuruluyor |
| Önerme ve Anlaşılırlık | 6/10 | Hayatta kalma kuralı net |
| Yapı ve Tempo | 4/10 | ⚠️ 1:16–1:55 tekrar döngüsü |
| Karakter | 4/10 | ⚠️ Salt prosedürel; kişisel kırılganlık/seçim yok |
| Tema | 5/10 | Dayanma teması tether ile dramatize ediliyor |
| Diyalog | 6/10 | Tamamen görsel anlatım |
| Duygusal Yay | 4/10 | ⚠️ İlk hayret orta bölümde plato yapıyor |
| Final | 5/10 | Tether çözme temiz kapanış |
| Özgünlük | 6/10 | ⭐ Ölçülen en yüksek özgünlük — döngüsel inversiyon + gök megafaunası |
| Retention Risk | 4/10 | ⚠️ Orta filmde yüksek terk riski |

**Paylaşılabilir an:** `0:36–0:42` — kuru topraktan kalkan su damlalarının
havada küre oluşturması.

**Başka hiçbir şeyin yapmadığı tek şey:** döngüsel gezegen yerçekimi
inversiyonu + yüzen su megafaunası ekolojisi.

---

## ⛔ ATLANMIŞ KAPI, SONRADAN ÇALIŞTIRILDI

Rapor künyesinde `SPEC VERIFIED AGAINST PLAN DOC: no — plan doc unsupplied`
yazıyor. Plan dosyası **depoda mevcut.** Kapı elle çalıştırıldı:

| Alan | Plan dosyası | Rapor | Sonuç |
|---|---|---|:---:|
| Sahne sayısı | **13** (S0-S10 + S3.5, S6.5) | 18 blok | ❌ |
| Süre | **130 s** (13 × 10 s) | **167 s** | ❌ +37 s |
| Diyalog | 0 | 0 | ✅ |
| Viral ara sahne | **2** (S3.5, S6.5) | "4 — doğrulanmamış" | ❌ |
| Protagonist | **Dr. Kaya Uçan** | "Explorer — doğrulanmamış" | ⚠️ |

> Protagonist alanı özellikle acı: eleştirmen karakterin adını "doğrulanamadı"
> diye işaretledi — **ama adı 2:12'de ekranda yazıyordu.**
> Bkz. Bulgu 1.

---

## 🚨 BULGU 1 — FİLMİN ÖNLEMEK İÇİN TASARLANDIĞI HATA, EKRANDA

Rapor, 2:12–2:21 arasında *"non-diegetic text overlay — technical lens and
character label graphics"* buldu ve reçetesinde metni alıntıladı:
**"Dr. Kaya Uçan..."**

Plan dosyası bunu **projenin en sert negatif kilidiyle** yasaklamıştı:

```
THE_INVERSION_PLANET_FILM.md:403-406
  "No readable or unreadable text, digits, letters, or symbols on the
   wrist display or any surface — abstract pulsing light only. No text,
   no logos, no on-screen text of any kind."

THE_INVERSION_PLANET_FILM.md:414-415
  "NO AI TEXT [LESSON 13]: Wrist display shows abstract pulsing light only,
   NEVER text — this rule is applied strictly from Scene 0 onward."
```

Belgenin kapanış paragrafı (satır 1189-1193) bu filmi zaten şöyle tanıtıyor:

> *"özellikle **Ders 13 (AI Metin)**, önceki filmlerin kendi negatif
> kurallarıyla çelişen tek örneği (Tidal Hunt Sahne 0'daki "6:00:00" yazısı)
> düzeltilerek, bu filmde bilek göstergesi baştan sona sadece soyut bir
> nabız/halo olarak tasarlandı."*

```
Film, Ders 13'ü ÇÖZMEK için tasarlandı.
Film, Ders 13'ü İHLAL ederek çıktı.
```

**Ve sızan metin rastgele değil:** "karakter etiketi" + "teknik lens
grafikleri". Prompt gövdesinde tam olarak bunlar var —
`[CHARACTER BIBLE] Kaya...` ve `CAMERA: 75mm, f/5.6, ISO 400`.
Model, sahneyi tarif eden **prompt iskeletini** kadraja çizmiş.

Bu, Ders 13'ün (hologramda uydurma yazı) ve Ders 34'ün (jenerik kartı) alt
türü değil, **yeni bir hata sınıfı:** → **DERS 45** olarak kaydedildi.

---

## 🚨 BULGU 2 — 37 SANİYELİK FAZLALIK: YENİ İÇERİK DEĞİL, TEKRAR

```
PLANLANAN     130 s  (13 sahne × 10 s)
GERÇEK        167 s
FARK          +37 s
```

Fazlalığın kaynağı raporun kendi kesim listesinde duruyor:

```
S8  1:16–1:25  su damlası tekrarı      (S4'ün kopyası)   10 s
S9  1:26–1:35  yüzen tether tekrarı    (S5'in kopyası)   10 s
S10 1:36–1:45  yaratık geçişi tekrarı  (S6/S7 kopyası)   10 s
S17 2:42–2:46  jenerik kartı           (planda YOK)       5 s
                                                        ─────
                                                         35 s ≈ +37 s
```

**Fazla sürenin tamamı tekrarlanmış görüntü ve planlanmamış bir karttır.**
Filme tek saniye yeni anlatı girmemiş. Rapor bunu "redundant visual loop"
diye hikaye kusuru saydı — aslında bir **kurgu dolgusu.**

### Ring Walker ile birlikte okunduğunda

| | Plan | Kurgu | Arıza |
|---|---|---|---|
| **Ring Walker** | 129 s / 13 sahne | 115 s | **EKSİK** — doruk sahnesi hiç yok |
| **The Inversion** | 130 s / 13 sahne | 167 s | **FAZLA** — 30 s tekrar + kart |

İki film, aynı hafta, aynı formatta, **aynı hata sınıfının iki zıt yüzü.**
Ortak nokta: hiçbir rubrik "kurgu, plana uyuyor mu?" diye sormuyordu.
`MANTIK_QA §1` (Plan ↔ Edit Conformity) tam olarak bu boşluk için yazıldı —
ve bu iki film onun ilk iki kanıtı.

---

## 🗺️ SAHNE EŞLEME — plan ↔ rapor

> Rapor kendi zaman bloklarını numaralandırdı (S0-S17); plan 13 sahne.
> Eşleme sonradan yapıldı, güven işaretleriyle.

| Plan sahnesi | Rapor bloğu | Güven |
|---|---|:---:|
| S1 — İNİŞ: GEMİ DEMİR | S0 · 0:00–0:05 | ⚠️ sıra farklı |
| S0 — HOOK: TAŞLAR TİTRİYOR | S1 · 0:06–0:15 "floating pebble" | ✅ |
| S2 — ÇAPA BÖCEKLERİ | S2 · 0:16–0:25 "anchoring procedure" | ⚠️ böcekler görünmüyor |
| S3 — TEMAS: CEPHE GEÇİYOR | S3 · 0:26–0:35 | ✅ |
| S3.5 — VİRAL: YÜKSELEN ŞELALE | S4 · 0:36–0:45 | ✅ ⭐ paylaşılabilir an |
| S4 — YÜZEN SAAT | S5 · 0:46–0:55 | ✅ |
| S5 — GÖKVATOZLARI | S6 · 0:56–1:05 | ✅ |
| S6 — YAKIN TEHLİKE: KANAT DALGASI | S7 · 1:06–1:15 | ✅ |
| — | **S8, S9, S10, S11 · 1:16–1:55** | 🚨 **planda yok — tekrar** |
| S7 — GERİ SAYIM | S12 · 1:56–2:01 | ⚠️ |
| **S8 — ÇÖKÜŞ (THE SLAM)** | S13 · 2:02–2:11 | ✅ **doruk ekranda VAR** |
| — | **S14 · 2:12–2:21 "bird swarm"** | 🚨 **planda yok + METİN** |
| S6.5 — VİRAL: TOZ TAVŞANLARI | S15 · 2:22–2:31 "dust storm" | ⚠️ konum kaymış |
| S9 — SESSİZLİK (tether çözme) | S16 · 2:32–2:41 | ✅ |
| S10 — DÖNÜŞ: GEMİ DEMİR | ❓ | ⛔ **bulunamadı** |
| — | S17 · 2:42–2:46 jenerik kartı | 🚨 **planda yok** |

```
PLANLANAN 13 SAHNE:  12 izlenebildi · 1 bulunamadı (S10 dönüş)
PLANLANMAMIŞ BLOK:    6  (4 tekrar + kuş sürüsü + jenerik kartı)
DORUK (S8 SLAM):     ✅ ekranda — Ring Walker'ın aksine
```

---

## 🩸 FİLME EN ÇOK ZARAR VEREN 3 ŞEY

```
1:16–1:55  TEKRAR DÖNGÜSÜ — 40 saniye, sıfır yeni bilgi (→ Bulgu 2)
0:16–0:25  DÜŞÜK BEDEL — karakter prosedürü zorlanmadan uyguluyor
2:12–2:21  EKRAN METNİ — sinematik gerçekliği kırıyor (→ Bulgu 1)
```

## 🛡️ KORUNACAK 3 ŞEY

```
0:06–0:15  ANINDA ÖNERME — kalkan çakıl taşı tek karede kuralı anlatıyor
0:36–0:45  MİKRO-YERÇEKİMİ GÖSTERİSİ — havada toplanan su küreleri
2:32–2:41  DÖNGÜSEL ÇÖZÜM — çapanın çözülmesi, yerin oturması
```

## ✍️ YENİDEN YAZIM REÇETELERİ — kabul/ret

| # | Reçete | Karar |
|:--:|---|---|
| 1 | S8-S10 tekrarlarını aktif bir komplikasyonla değiştir (tether vinci sıkışsın) | ✅ **KABUL** — ama bu bir kurgu değil, **plan** işi: planda o 30 saniye zaten yoktu |
| 2 | S14'teki "Dr. Kaya Uçan..." etiketlerini kaldır | ✅ **KABUL** — plan zaten yasaklamıştı (Bulgu 1) |
| 3 | S2'ye fiziksel zorlanma ekle | ✅ **KABUL** — §9.1 tepki çapası kuralına uyuyor |

> Üç reçetenin üçü de kabul edildi — **bu, dört senaryo raporu içinde bir ilk.**
> Sebebi anlamlı: bu raporun bulguları tasarım kararlarına değil, **kurgu ve
> üretim hatalarına** dokunuyor. Dokümansız çalışan bir eleştirmen tasarımı
> yanlış okur (bkz. Kaleida Crash), ama **hatayı doğru okur.**

---

## 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 45 (yeni)  Prompt iskeletinin ekrana sızması → LESSONS_LEARNED
□ Kurgu dolgusu   Tekrar döngüsü kuralı → UZAY_SENARYO_KILAVUZU §13
□ Karakter 4/10   Üçüncü kez aynı skor → §9.1 etkinlik kuralı doğrulandı
□ S10 (dönüş)     Kurguda bulunamadı — doğrulanmalı
□ Jenerik kartı   Planda yok, videoda var → Ders 34 tekrarı olabilir
□ VIDEO_QA        Bu film hiç teknik QA görmedi — metin ihlali ancak
                  senaryo QA'sı sayesinde ortaya çıktı
```

---

# 🔗 MANTIK VE DEVAMLILIK QA

## 📋 KÜNYE

```
RUBRİK:        MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — 8 kategori
QA TARİHİ:     31 Temmuz 2026
GİRDİ:         yalnızca video (rubrik doküman istemiyor — tasarım gereği)
SÜRE:          166 s (2:46) · 18 blok gözlendi
BASELINE:      SELF-CONSISTENCY
GENEL SKOR:    3.0/10
KARAR:         STRUCTURAL PROBLEM
GEÇERLİLİK:    ✅ GEÇERLİ — rubrik SPEC istemiyor, kapı atlanmadı
```

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | 3/10 | Yerçekimi durumu sahneler arası ileri geri gidiyor |
| **Sayaç Mantığı** | **2/10** | 🚨 Döngü 2.5 dakikada 3 kez dönüyor |
| Mekan Coğrafyası | 4/10 | Düz çöl → dev kaya duvarı, geçiş yok |
| **Zaman ve Işık** | **2/10** | 🚨 40 saniyelik blok birebir tekrar ediyor |
| **Durum, Kostüm, Prop** | **2/10** | 🚨 Kask AÇIK/KAPALI/VİZÖRSÜZ arasında ışınlanıyor |
| Nedensellik ve Bilgi | 4/10 | Tether vinci sahne aralarında yok olup geri geliyor |
| Sayı Tutarlılığı | 5/10 | "9 saat" kartı vs 30 saniyelik gözlenen aralık |
| Kurulum ve Terk | 5/10 | Böcek sürüsü ve HUD metni birer kez görünüp kayboluyor |

**🔴 BLOCKER: 3 · 🟠 MAJOR: 4 · 🟡 MINOR: 2**

---

## ⭐ MANTIK §1 — TEKRAR DÖNGÜSÜ, İKİNCİ KEZ VE BAĞIMSIZ OLARAK BULUNDU

Senaryo QA (Bulgu 2) bu 40 saniyeyi *"redundant visual loop"* diye **hikaye
kusuru** saymıştı. Mantık QA aynı bloğu **kurgu hatası** olarak, birebir
tekrar kanıtıyla buldu:

```
0:36–1:15  S5 su damlaları · S6 tether · S7 vatoz · S8 tether çekme
1:16–1:55  S9 ────────────── S10 ─────── S11 ───── S12  ← BİREBİR AYNI
```

**İki bağımsız rubrik, iki farklı mercek, aynı 40 saniye.** Bu, bulgunun
doğruluğunu tek bir raporun verebileceğinden daha güçlü kanıtlıyor.

→ **DERS 46** olarak kaydedildi: *Montaj tekrarı — aynı blok kurguda iki kez.*
O tarihte projedeki derslerin tamamı prompt’a bakıyordu; bu sınıfın sahibi yoktu.

---

## 🚨 MANTIK §2 — SAYAÇ GERİ GİTTİ: ÖNCÜL ÇÖKTÜ

Bible döngüyü sayıyla kilitlemişti (`THE_INVERSION_PLANET_FILM.md:52-70`):

```
9 saatte BİR kez · T+0:00 → T+6:00 tek kesintisiz pencere · sonra SLAM
→ Bible 2 GEÇİŞ tanımlıyor: giriş (T-0:00) ve çöküş (T+6:00)
```

Kurguda gözlenen:

```
S1 1g → S2 0g → S3 1g ⚠️ → S4-S13 0g → S14 1g → S15 0g ⚠️ → S16 1g ⚠️ → S17 1g
                                                    ─────────────────
                                         5 geçiş · Bible 2 tanımlamıştı
```

Kapanış kartı "her 9 saatte bir" derken görüntü 30 saniyede bir tersine
dönüyor. Bu bir devamlılık kayması değil — **filmin öncülü.** İzleyici kuralı
öğrenemiyor, öğrenemediği kural için gerilim hissetmiyor.

→ **DERS 49** olarak kaydedildi: *Novum döngüsünün kurguda ihlali.*
Sahne haritasına zorunlu "NOVUM DURUMU" sütunu geldi.

---

## 📖 BELGE SORULARI — CEVAPLANDI

Rapor iki soru bıraktı. İkisi de plan dosyasından cevaplandı:

| Rapor sorusu | Plan dosyası ne diyor | Sonuç |
|---|---|:---:|
| Atmosfer kasksız solunabilir mi? | `satır 84` — **"thin dry atmosphere"** · `satır 135, 408` — **"VISOR PERSISTENCE RULE [LESSON 5]: Visor ALWAYS VISIBLE in every frame"** | ❌ **HATA** — 0:16, 1:06 ve 2:32'deki çıplak baş tasarım değil, ihlal |
| Tether yerçekimi dönünce otomatik ayrılıyor mu? | `satır 123` — **"a fixed mechanical tether reel unit mounted flush against her lower back"** — kalıcı montaj | ❌ **HATA** — 2:32'de vincin yok olması ihlal |

Ayrıca raporun doğrudan sormadığı ama plan dosyasının cevapladığı bir şey:

```
2:42 jenerik kartı ("EVERY 9 HOURS, GRAVITY TURNS AGAINST US")
  → planda YOK · negatif çekirdek "no title card, no end card" diyor
  → Senaryo QA da aynı 5 saniyeyi planlanmamış blok olarak işaretlemişti
```

---

## ✅ RAPORUN KENDİ DOĞRULUĞU

Rubrik "eksik raporlama" yasağını taşıyor ve rapor buna **uydu:**

```
✅ Hiçbir yerde "şu sahne eksik" demedi — plan elinde yoktu, iddia etmedi
✅ Çözemediği iki şeyi FLAGS altına SORU olarak yazdı, tahmin etmedi
✅ Her bulgu iki timecode taşıyor — tek gözlemli satır yok
✅ 18 blok saydı; plan 13 sahne + 4 tekrar + 1 kart = 18 ✓ tutarlı
✅ Kapsam dışı iki bulguyu (jello, bloom) puanlamadı, sonda tek satır bıraktı
```

> Bu, projede **künyesi bozulmamış ilk QA raporu.** Sebebi yapısal: rubrik
> SPEC istemiyor, dolayısıyla uydurulacak SPEC de yok.

---

## 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 46 (yeni)  Montaj tekrarı → LESSONS_LEARNED ✅ yazıldı
□ DERS 49 (yeni)  Novum döngüsü ihlali → LESSONS_LEARNED ✅ yazıldı
□ DERS 48         Biyom sıçraması — bu filmde de görüldü (çöl → kaya duvarı)
□ DERS 5 İHLALİ   Bible'da yazılıydı, tutmadı — tarif kilidi kanıtı
□ DERS 37 İHLALİ  Kask durumu 3 kez ışınlandı
□ Ders 34 tekrarı Planda olmayan jenerik kartı 2:42'de
□ VIDEO_QA        Bu film hâlâ teknik QA görmedi — üçüncü rubrik de
                  onun yerini tutmuyor (jello ve bloom kapsam dışı bırakıldı)
```
