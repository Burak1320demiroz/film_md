# 🟫 THE LAST SHIFT — FİLM QA KAYDI

> **Film:** THE LAST SHIFT · 16:9 yatay · 2-4 dk · `yatay_2_4_dk_filmler_uzay/THE_LAST_SHIFT/THE_LAST_SHIFT_COLONY_FILM.md`
> **Plan:** 14 sahne · **24 çekim · 27 klip** · 190 s · ASL 7.9 s · 10 sahne içi kesme ·
> 24/24 sabit kilitli kadraj · 13 replik (13/13 gövdesiz makine) · 7 viral ara
> **Kurgu:** 174 s · **17 × 10 s klip + 4 s başlık kartı** — süreler tekdüze 10 s ızgarasında
> **QA tarihi:** 16.08.2026 — dört mercek aynı gün, **dördü de mod V**
> **Ham raporlar:** `../02_HAM_RAPORLAR/THE_LAST_SHIFT_{TEKNIK,SENARYO,MANTIK,KARAKTER}_HAM.md`

---

## 📊 DÖRT KOŞUNUN DURUMU

| Mercek | Skor | Verdict | Koşu |
|---|:--:|---|---|
| 🔧 VIDEO (teknik) | **5.0/10** Ⓥ | REGENERATE (2 🔴) | ⛔ **ÖN KOŞU** — SPEC §0.15'te hazırdı, mod V koşuldu [D94] |
| 📖 SENARYO | **6.0/10** Ⓥ | REVISE STRUCTURE | ⛔ **ÖN KOŞU** — aynı sebep [D94] |
| 🧩 MANTIK | **5.0/10** | STRUCTURAL PROBLEM | ⚠️ ŞARTLI — kilit çelişkisi defteri açık [D96] |
| 🧍 KARAKTER | **6.0/10** | IDENTITY BREAK | ⚠️ ŞARTLI — aynı sebep [D96] |

```
⭐ Bu filmin QA'sı deponun ilk "SAHNE ≠ ÇEKİM" ölçümüdür. Dört mercek de filmi
   14 sahne / 14 segment olarak saydı ve dördü de doğru saydı — ama planın birimi
   14 sahne DEĞİL, 24 çekim / 27 kliptir. Ölçüm bu yüzden filmin en büyük olayını
   (10 klibin kurguya hiç girmemesi) göremedi; onu ancak plan↔kurgu karşılaştırması
   gösterdi. → DERS 100 · DERS 101
```

---

## ⭐ ANA BULGU 1 — KURGU KAPISI: SAHNE SAYISI TUTTU, KLİP SAYISI TUTMADI

D72'nin kurgu kapısı dört madde sayar. Bu filmde birinci madde **yanlış birimi** saydığı
için ✅ verdi:

| Kapı maddesi | Plan | Kurgu | Sonuç |
|---|---|---|---|
| ① klip sayısı = SCENE COUNT | 14 sahne | 14 segment | ✅ **(yanıltıcı — gerçek birim 27 klip)** |
| ①b klip sayısı = **CLIP COUNT** | **27 klip** | **~18 klip** (17 × 10 s + 4 s kart) | 🔴 **≈10 klip kurguda yok** |
| ② süre = RUNTIME ± 2 s | 190 s | 174 s | 🔴 **−16 s** |
| ③ ekran metni = 0.0 s | 0 kare | **2:50-2:54 yanık başlık kartı** | 🔴 **İHLAL** |
| ④ CENTRAL CHOICE ekranda | S10 (eldiven + çıplak el) | 🔧📖🧩🧍 dördü de 2:00-2:09'da gördü | ✅ **ekranda** |
| ⑤ ASL = süre / çekim | 7.9 s · bant 2.0-20.0 | **tekdüze 10 s** (tek istisna 4 s kart) | 🔴 **ritim mimarisi yok** |

### Plan ↔ kurgu sahne eşlemesi (dört raporun ortak zaman kodlarından)

| Plan | Süre | Kurguda | Durum |
|---|:--:|---|---|
| S0 Ç1 — ECU sürgü kolu | 6 s | 0:00-0:09 | ✅ ama **10 s** (kırpılmadı) |
| S0 Ç2 — parsel kalkıyor | 10 s | 0:09-0:19 | ✅ |
| S1 — iki figür, spor kuralı | 10 s | 0:20-0:29 | ✅ replik duyuldu |
| S2 Ç1-Ç2 — mühürler | 16 s | 0:30-0:49 | ✅ ama **20 s** |
| S3 — ÖNCE KARESİ (B4-A) | 10 s | 0:50-0:59 ⬜ | ⬜ rapor "yürüyüş" diyor, plan geniş yerleşim planı |
| S4 Ç1-Ç2 — havuz, kesik boru | 14 s | 1:00-1:19 | ✅ ama **20 s** |
| **S5 Ç1-Ç2 — ⭐ ALTMIŞ BİR ÇİFT (İFŞA 1 · VİRAL)** | 15 s | **hiçbir raporda yok** | 🔴 ⬜ **ekranda görünmüyor** |
| S6 Ç1-Ç2 — pençe + kurşun (VİRAL) | 15 s | 1:40-1:49 | ⚠️ tek 10 s; dört rapor da "duvardaki tozu okşuyor" okudu |
| S7 — çevirmen, 20 s hold (VİRAL) | 20 s | 1:20-1:39 | ✅ ⭐ **birleşik hold TUTTU** · ⚠️ **S6'dan ÖNCE geldi (sıra ters)** |
| **S8 Ç1-Ç2 — şaftlar** | 12 s | **hiçbir raporda yok** | 🔴 ⬜ **ekranda görünmüyor** |
| S9 Ç1-Ç2 — tek uzuv, 3 s, 300 m | 13 s | 1:50-1:59 | ⚠️ rapor "giant mechanical **legs**" (çoğul, yürüyor) |
| S10 — 🎯 DORUK, çıplak el | 16 s | 2:00-2:09 | ✅ ama **10 s** |
| S11 Ç1-Ç4 — ⭐ HIZ KARTI (MOD C · VİRAL) | 9 s / 4 çekim | 2:10-2:19 tek çekim | 🔴 **filmin tek aksiyon ritmi yok** |
| S12 — SONRA KARESİ (B4-B) | 10 s | 2:20-2:29 | 🔴 ⬜ "orange desert" + kostüm kırılması |
| S13 — final, 30 km EWS (VİRAL) | 18 s | 2:30-2:49 | ✅ ama **20 s** |
| — | — | **2:50-2:54 başlık kartı** | 🔴 **planda yok, §0.18 ⑩ yasaklıyor** |

```
DİYALOG SAYIMI:  plan 13 replik / 9 sahne  →  kurguda 6 replik / 6 sahne duyuldu.
Kayıp repliklerin üçü, ekranda görünmeyen sahnelere ait:
  "Altmış bir kayıtlı. Altmış bir çift."   (S5)
  "Bu izler alet izi değil." / "Delikler içeriden açılmış."  (S6 Ç1-Ç2)
  "Üç yüz metre. Kapalı kalın."             (S9 — sahne VAR, replik yok)
⭐ Ve S5'in repliği filme METİN olarak geri döndü: 2:50'deki kartın alt satırı
   "SIXTY-ONE PAIRS OF BOOTS. ZERO PEOPLE." — bu cümle depoda yalnız TEK yerde
   geçiyor: §5.3 TİPOGRAFİ, kapak alt satırı ("Altmış bir çift bot. Sıfır insan.").
```

---

## ⭐ ANA BULGU 2 — 27 KLİP × 10 s = 270 s HAM MALZEME; HEDEF 190 s. KIRPMAYI KİMSE YAZMADI

Bu film deponun ilk **değişken çekim süreli** planıdır: 2.0 s ile 20.0 s arasında 24 çekim,
ASL 7.9 s. Üretim hattının klibi ise sabittir (~10 s).

```
27 klip × ~10 s  =  ~270 s ham malzeme
hedef            =   190 s
KIRPILACAK       =   ~80 s   ← plan bunu HİÇBİR YERE yazmadı

§0.18 KURGU TALİMATI on bir madde sayar (grade, gren, birleşik hold, ses, J-cut,
başlık kartı yasağı) — "hangi klip kaç saniyeye kırpılır" maddesi YOK.
Süreler yalnız iki yerde duruyor: §0.9 sahne haritası ve VİDEO PROMPTUN İÇİ
("MOTION — 2.5 seconds ..."). İkisi de kurgucuya verilen bir talimat değildir;
modelin dosya uzunluğunu prompt değiştirmez.

SONUÇ (kurgunun ölçülen hâli): kurgu KIRPMADI, KLİP DÜŞÜRDÜ.
17 klip tam 10 s olarak kaldı, ~10 klip düştü, süre 174 s'ye "tuttu".
Kaybedilenler arasında filmin İFŞA 1'i (S5) ve tek aksiyon ritmi (S11) var.
```

⭐ **Süre tuttuğu için kayıp görünmedi** — D62'nin "runtime hides a missing finale"
mekanizmasının klip ölçeğindeki hâli. → **DERS 100**

---

## ⭐ ANA BULGU 3 — BEŞ ÜRETİM KAPISININ BEŞİ DE KAYITSIZ; QA, DÖRT KAPININ ÜSTÜNE DÜŞTÜ

`BÖLÜM 4 · 4.1 KAPI KAYDI` tablosunda altı satırın altısı ⬜ **koşulmadı**, `DURUM` satırı
hâlâ **"ÜRETİM BAŞLAMADI"** yazıyor — oysa 174 s'lik kurgu aynı gün dört mercekle ölçüldü.
Kaydı olmayan kapı koşulmamış kapıdır → **DERS 74'ün 2. vakası.**

Bedeli ölçüldü: raporların bulguları kapıların **tam üstüne** düştü.

| Üretim kapısı | Kabul ölçütü (planda yazılı) | QA'da çıkan |
|---|---|---|
| KAPI 1 — iki figür (S1) | boy farkı · suit renkleri · **bant TARAFI** | 🧍 🔴 2:20 kostüm: bant SOL koldan SAĞ kola geçti, bot modeli değişti |
| KAPI 2 — parsel (S0 Ç2) | toz 20 m'yi aşmasın, 6 s'de otursun, **sıvılaşmasın** | 🔧 🟠 1:52 "dust cloud moves uniformly like a **2D fluid** simulation" (D39) |
| KAPI 3 — uzuv (S9 Ç2) | **TEK** uzuv · 3.0 s · 300 m · gövde 0 kare | 🔧📖🧩 "giant mechanical **legs** march" — çoğul ve yürüyor |
| KAPI 4 — eşleştirme (S3/S12) | aynı lens/mesafe/yükseklik/eksen | 🧩🧍 🔴 2:20 S12 hiç eşleşmiyor: başka arazi, başka suit |
| KAPI 5 — birleşik hold (S7) | ek görünüyor mu | ✅ **TUTTU** — 20 s'lik S7 dört raporda da tek kesintisiz sahne |

```
Beş kapı ~5 klip = üretimin %18'i. Koşulsaydı dördü üretimde yakalanırdı;
koşulmadığı için filmin tamamı üretildi, kurgulandı ve dört mercekle ölçüldü.
Tek koşulan-benzeri kapı (birleşik hold) depoda ilk kez denendi ve TUTTU.
```

---

## ⭐ ANA BULGU 4 — BAŞLIK KARTI = KAPAK ÇIKTISI. ZİNCİRİN 7. VAKASI

`2:50-2:54` — yanık "THE LAST SHIFT" + alt satır. Alt satırın kaynağı belgelidir:
§5.3 TİPOGRAFİ bloğu, kapak için yazılmış **ALT SATIR** cümlesi.

```
D70/72 zinciri:  Unbroken City 2:40 · Starless Circle 2:50 · Stone Sky 2:10 ·
                 Third Dune 4:00 · Ring Light 2:20 · Banded Deep 3:00 ·
                 ⭐ THE LAST SHIFT 2:50  ← 7. VAKA

⛔ Ve bu filmde yasak İKİ yerde birden yazılıydı:
   §0.18 ⑩  "BAŞLIK KARTI YOK. Ne başta ne sonda; kurguya tek harf girmez"
   §5.3 ⛔  "kapak çıktısı kurgu klasörüne KONULMAZ (DERS 70/72)"
   Üstelik 51 promptun 51'inde "no text, no title card" cümlesi var — kart
   ÜRETİMDEN değil KURGUDAN geliyor; 4 saniyede, yeniden üretim olmadan çıkar.
```

⭐ Bu vakada zincir bir adım ileri gitti: kart yalnız başlığı değil, **ekranda hiç
görünmeyen S5'in bilgisini** (61 çift bot / sıfır insan) taşıyor. Kurgu, düşürdüğü
görüntünün yerine yazıyı koydu. → **DERS 100**'ün ikinci yarısı.

---

## ⛔ KİLİT ÇELİŞKİSİ DEFTERİ [DERS 96]

Raporların, planda YAZILI bir kilide aykırı bulguları. Rapordan hangisinin doğru olduğu
çözülemez; **master'ın o saniyesi izlenerek** kapanır. Açık madde varken bu bulgulardan
ders yazılmaz, yeniden üretim siparişi verilmez.

| # | Rapor ne dedi (timecode) | Hangi kilit (§) | Çözüm eylemi | Sonuç |
|:--:|---|---|---|---|
| 1 | 🧍🧩 2:20 kadın suit'i tamamen değişti: bant SAĞ kolda, fitilli diz/bot | §0.12 KADRO KİLİDİ — FİGÜR K: kemik beyazı, **bant SOL üst kolda**, 14/14 sahnede aynı | 2:20-2:29'u izle; bandın tarafına ve bot modeline bak | ⬜ AÇIK — ⚠️ raporun 0:20 taban okuması kilide **birebir uyuyor** (beyaz suit, SOL kol), yani rapor bu kanalı doğru okuyor |
| 2 | 🔧📖🧩 2:20 "orange Mars-like desert", biyom sıçraması | §0.11 ışık takvimi: S11-S12 **HEAVY AMBER** — palet tek kanala iner (amber-gri); ama MEKÂN değişmez, film tek vadide geçer | 2:20'de yerleşim/direk görünüyor mu; sadece renk mi değişti | ⬜ AÇIK — renk PLANLI, arazi değişimi değil |
| 3 | 🔧📖🧩 1:50 "giant mechanical **legs** march through dust" | §0.12 yaratık bütçesi: **1 çekim · 3.0 s · TEK uzuv · 300 m · gövde/baş/bacak takımı 0 kare** | 1:50-1:59'u izle: kaç uzuv, kaç saniye | ⬜ AÇIK — doğrulanırsa 🔴 (KAPI 3 ihlali) |
| 4 | 🧍 1:00 kutu yoktan belirdi (0:50 iki el de boş) | §0.12: çevirmen kutusu **S7'den itibaren** FİGÜR K'nin elinde | 0:50-1:19'u izle: kutu hangi sahnede ilk kez var | ⬜ AÇIK — kurgu sırası (S7 ↔ S6 yer değiştirmesi) bu bulguyu üretmiş olabilir |
| 5 | 🧍🧩 2:00 kanca çubuk yok oldu | §0.12 KADRO KİLİDİ — FİGÜR U'nun elinde **kısa kanca çubuk**; bırakma sahnesi planda yok | 2:00-2:09'u izle: çubuk kadrajda mı, yere mi bırakıldı | ⬜ AÇIK |
| 6 | 📖 kurguda S5 (61 çift bot) ve S8 (şaftlar) yok | §0.9 · §0.15: S5 **VİRAL ARA, KESİLEMEZ** · A3 devralınan dersi (ölümü sayaçla anlat) tamamen S5'e bağlı | master'ı 1:00-1:50 arası izle: ranza/bot sahnesi var mı | ⬜ AÇIK — ⚠️ dört bağımsız sahne haritasının dördünde de yok |
| 7 | 📖 6 replik duyuldu | §0.12: **13 replik** (8 kask AI + 5 çevirmen) | ses master'ını dinle | ⬜ AÇIK |

```
⛔ KURAL (D96): defter kapanmadan bu maddelerden ders yazılmaz. Dört tablo satırı
   da bu yüzden ⚠️ ŞARTLI. Kapanış maliyeti: master'da 7 zaman kodu, ~2 dakika.
```

---

## ✅ D87 KAPISINDA DÜŞEN BULGULAR — "bu değişim filmin önermesi mi?"

| Rapor bulgusu | Belge cevabı | Karar |
|---|---|---|
| 🔧 "2:30 checkerboard terrain — hallucinated?" · 📖 aynı soru | **FİLMİN NOVUM'U.** §0.10 SAYAÇ A + §0.9 S13: 60 × 60 m parseller, 4 m derin, kusursuz düz kenar; final ızgaranın ikinci vadiye girmesidir | **DÜŞTÜ** — bulgu değil, filmin kendisi |
| 🧩 "Time & Light 5/10 — overcast lighting breaks at 2:20" | §0.11: S11-S12 HEAVY AMBER, palet tek kanala iner; ışığın **azalması ve amberleşmesi planlıdır** | **KISMEN DÜŞTÜ** — renk planlı, arazi ⬜ defter madde 2 |
| 📖 "Character 4/10 — camera-carriers, no interiority" | §0.9c ESİRGEME + §0.15 rubrik uyarısı: zirvelerde yakın plan, ters açı, tepki çekimi **bilerek yok**; yüz S7'de hiç görünmez | **DÜŞTÜ** — mod D koşulsaydı bu puan yazılamazdı [D94] |
| 📖 "Hook 4/10 — static handle, a place not a situation" | §0.17 + §0.9b ÖLÇEK YAYI: film 75mm ECU'dan başlar (kaynak filmin açılış grameri), S0 **VİRAL ARA ve KESİLEMEZ** | **DÜŞTÜ** — ama ⚠️ 6 s planlanan çekim 10 s oynadı (D100) |
| 🧩 "Counter Logic N/A — no counter observed" | §0.10: film **ÜÇ metinsiz sayaç** taşır (kalan parsel · kadrajdaki insan sayısı · amber pus yüksekliği) | **BULGU DEĞİL AMA ÖLÇÜM KAYBI** — D78'in 4. vakası: sayaçlar tek karede kanıtlanmadığı için okunmadı |
| 🧩 "Causality 5/10 — scanner yields no shown result" | §0.9: S10'un sonucu S11-S12'dir (kadrajdaki insan sayısı düşer) — ama S11'in dört çekimi kurguda yok | **AYAKTA** — kök neden kurgu kaybı, tasarım değil |

---

## ⭐ FLAGS FOR DOCUMENT CHECK — CEVAPLAR

### 🔧 VIDEO_QA
**S1. "0:09 — planlı sahne sınırları neler?"**
→ Plan 14 sahne / 24 çekim / **10 sahne İÇİ kesme** + 13 sahne sınırı = 23 kesme.
Rapor 14 sınır saydı; sahne sınırları meşrudur [D61b]. ⚠️ Ama sayının 23 değil 14 çıkması
kayıp kliplerin işaretidir (Ana Bulgu 1).

**S2. "2:20'deki turuncu Mars atmosferi senaryolu bir mekân değişimi mi?"**
→ **MEKÂN DEĞİŞİMİ YOK** — film tek vadide, tek öğleden sonrada geçer. **RENK DEĞİŞİMİ VAR
ve planlıdır** (§0.11 HEAVY AMBER). Kilit çelişkisi defteri madde 2.

**S3. "2:30 checkerboard topografya belgeli mi?"**
→ **EVET, filmin novum'u.** Bulgu düşer [D87].

### 📖 SENARYO_QA
**S1. "2:20 (S12) bilinçli zaman atlaması mı, viral ara mı?"**
→ **İKİSİ DE DEĞİL: filmin BEDEL sahnesi.** §0.19 B4: S3 ve S12 aynı kurulumdur (aynı lens,
mesafe, yükseklik, eksen); tek fark yerleşimin yakın yarısının 4 m aşağıda olması ve
kadrajdaki insanın 2 değil 1 olması. Ekrandaki hâli bu tarife uymuyor → defter madde 1-2.
🔴 **Kesme listesi UYGULANMAZ.**

**S2. "S13'teki checkerboard gezegen halüsinasyon mu?"** → Hayır, novum (yukarıda).

**S3. "2:50 yanık başlık kartı planlı mı?"**
→ **HAYIR — YASAK.** §0.18 ⑩ ve §5.3. 🔴 BLOCKER, **kurguda 4 saniyede düzelir.**

**S4. (rubrik sormadı ama kesme listesi için) "S1 (0:00-0:09) kesilebilir mi?"**
→ **HAYIR.** S0 planın 7 KESİLEMEZ viral arasından biridir ve ölçek yayının başlangıcıdır.
Raporun kesme listesinin 1. sırası bir viral aradır — Third Dune ve Ring Light'tan sonra
**3. vaka** (D94 örüntüsü).

### 🧩 MANTIK_QA
**S1. "2:20 mekân sıçraması planlı mı?"** → Ana Bulgu / defter madde 2 (renk planlı, arazi açık).
**S2. "2:30 checkerboard senaryolu mu?"** → Evet, novum.
**Ek:** COUNTER CURVE **NONE** yazıldı; planda üç sayaç var → D78 ×4.

### 🧍 KARAKTER_QA
**S1. "2:20'de kadın suit'i eski/başka bir promptla mı üretildi?"**
→ **Tasarım DEĞİL.** §0.12 KADRO KİLİDİ: FİGÜR K 14/14 sahnede kemik beyazı, **turuncu bant
SOL üst kolda**; FİGÜR U koyu zeytin, bant SAĞ baldırda. Raporun 0:20 taban okuması kilide
birebir uyuyor, 2:20 okuması uymuyor. → defter madde 1 (⬜ AÇIK, güçlü ön kabul: gerçek sapma).

**S2. "Vizörler karanlık ama cam düzlemi yansıması yok — saydam mı, opak mı?"**
→ **Kask 12/12 insanlı sahnede KAPALI, vizör hiç açılmaz** (§0.12 KASK TAKVİMİ). Rapor
kaskı "sealed — evidence: solid visor pane and collar lock" diye kanıtla yazdı: **DERS 95
bu koşuda TUTTU** (Ring Light'ta aynı soru "kask yok" olarak raporlanmıştı).

⭐ **Ayrıca D89 TUTTU:** filmde tek ekipman değişimi vardır (S10'da FİGÜR U'nun **SAĞ**
eldiveni) ve rapor tam olarak bunu gördü — "removes **right** glove", kask/ikinci eldiven
yok. Mühür sayımı kilidi çalışıyor.

⭐ **Ve D97 TUTTU:** rapor yüz sütununu ⚠️ UNVERIFIABLE bıraktı ve kanıt tabanını ölçtü
(kadın 0 s / 14 sahne · erkek ~10 s / 2 sahne). Ring Light'ta bu sütun 9/10 yazılmıştı.

---

## 📋 ONARIM LİSTESİ

### Kurguda düzelir (yeniden üretim YOK)
```
1. 🔴 2:50-2:54 başlık kartını kurgudan ÇIKAR → ekran metni 0 kare olur.
2. 🔴 Düşen ~10 klibi kurguya geri koy (S5 · S8 · S11 Ç1-Ç4 · S6'nın 2. çekimi …)
      ve §0.9'un süre tablosuna göre KIRP: 27 klip → 190 s.
3. 🔴 S11'in dört çekimini 2.5 / 2.0 / 2.0 / 2.5 s'ye kırp — filmin tek aksiyon
      ritmi yalnız kurguda var olabilir.
4. 🟠 S6 ↔ S7 sırasını plana göre düzelt (pençe/kurşun ÖNCE, çevirmen SONRA).
5. 🟠 S0 Ç1'i 6 s'ye, S10'u 16 s'ye getir (ASL 7.9 bandı).
```

### Yeniden üretim gerektirir (defter kapandıktan SONRA)
```
6. ⬜ S12 — kostüm + kadraj eşleşmesi doğrulanırsa yeniden üretim; çapa S3'ün
      üretilmiş son karesi (planın KAPI 4 Plan B'si: I2V).
7. ⬜ S9 Ç2 — "çoğul bacak" doğrulanırsa yeniden üretim ya da §0.8b HAZIR DÜŞÜŞ
      (uzuv yerine gölgesi).
8. ⬜ S0 Ç2 / S9 — toz sıvılaşması doğrulanırsa (D39) ilgili klip yeniden üretilir.
```

### Ölçüm borcu
```
9.  ⭐ Kart çıkarılıp klipler geri konduktan sonra dört mercek **MOD D** ile
       tekrarlanır (§0.15 SPEC yapıştırılarak). Mod D bu depoda hâlâ hiç denenmedi
       — operatör kuralı ②'nin 6. ihlali.
10. ⭐ 🔊 SES_QA hiç koşulmadı; 13 repliğin 13'ü MACHINE register'dadır (kart E3 adım 2).
11. ⭐ BÖLÜM 4 KAPI KAYDI tablosu geriye dönük doldurulamaz — koşulmadı olarak kalır [D74].
```

---

## 📚 BU FİLMDEN ÇIKAN DERSLER

| № | Başlık | Kaynak |
|:--:|---|---|
| **100** | Sabit klip tavanı + kırpma talimatsız plan = kurgu kırpmaz, klip düşürür | plan §0.9/§0.18 + dört sahne haritası |
| **101** | Kurgu kapısı SAHNE sayıyor; SAHNE ≠ ÇEKİM olan ilk filmde kapı körleşti | 🔧📖🧩🧍 ortak sayımı |
| **102** | Aynı olay hem FLAGS sorusu hem puan düşüşü oldu — etiket kategoriye bağlandı, olaya değil | 🔧 Kamera UNV ↔ Çevre 5/10 · 🧩 Coğrafya 4/10 · 🧍 Kostüm 2/10 |
| **103** | Negatif kutu denetimi tek yönlü: işaretlenmeyen kutu sayımı tutturuyor, ihlali yutuyor | 🔧 `BOX 2 · LINKED 2 · UNLINKED 0` ama 5 bulgu |
| 🔁 74 | Kaydı olmayan kapı koşulmamış kapıdır — 2. vaka, bedeli 4/5 kapıda ölçüldü | BÖLÜM 4.1 boş tablo |
| 🔁 70/72 | Jenerik kartı zincirinin 7. vakası — bu kez kartta **düşen sahnenin bilgisi** var | 2:50 |
| 🔁 78 | Üç çevresel sayaç ekranda okunmadı (4. vaka) | 🧩 `COUNTER CURVE: NONE` |
| ✅ 89 · 95 · 97 | Üçü de bu koşuda **TUTTU** — mühür sayımı, mühürlü kask kanıtı, kanıt tabanı eşiği | 🧍 |
