# 🔍 THE KALEIDA CRASH — QA KAYDI

> **Kaynak dosya:** `yatay_2_dk_filmler/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_PLANET_FILM.md`
> **Bu filmde ÜÇ ayrı QA var — projede üç merceğin de uygulandığı ilk film:**
> · **TEKNİK QA** (aşağıda) — `LESSONS_LEARNED.md` kalite tablosu + Ders 20-22
> · **SENARYO QA** (31.07.2026) — [aşağıdaki bölüm](#-senaryo-qa--31-temmuz-2026) · ham çıktı: [`../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_SENARYO_HAM.md`](../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_SENARYO_HAM.md)
> · **MANTIK QA** (31.07.2026) — **4.0/10** · ham çıktı: [`../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_MANTIK_HAM.md)
>
> ⚠️ **Teknik QA'nın orijinal raporu dosya olarak mevcut değil.**

---

# 🔧 TEKNİK QA

## 📋 KÜNYE

```
FORMAT:        2-4 dk · yatay · bilimkurgu
QA KAPSAMI:    Full (tam film) — tabloda ilk "Full" kapsamlı QA
QA TARİHİ:     kayıt yok
SPEC BLOĞU:    kayıt yok
GENEL SKOR:    4.5/10
```

---

## 📊 SKORLAR

| Kategori | Skor | Durum |
|---|:---:|---|
| Karakter | 5/10 | karakter klonlama / çift kişi hatası |
| Fizik | 4/10 | |
| Kamera | 3/10 | kesme sorunu tekrarladı |
| Işık | 5/10 | |
| Çevre | 4.5/10 | statik ateş / patlama |
| Canlı | 4.5/10 | |
| Hareket | 4.5/10 | |
| Parçacık ve Malzeme | ⛔ kayıt yok | patlama filmi — bu kategori kritikti |
| Diyalog ve Ses | ⛔ kayıt yok | |
| Kare Çapası Sadakati | ⛔ kayıt yok | |
| Negatif İhlal | ⛔ kayıt yok | |

---

## 🧪 ÜRETTİĞİ DERSLER — 3 ders

| Ders | Başlık | Kaynak skor |
|:---:|---|---|
| 20 | Karakter klonlama — çift kişi hatası | 5/10 karakter |
| 21 | Statik ateş — boyama gibi patlama | 4.5/10 çevre |
| 22 | Aksiyon sürekliliği — imkansız geçişler | 3/10 kamera, 4.5/10 hareket |

---

## ⚠️ BU KAYDIN EKSİKLERİ

```
□ Ham QA raporu yok
□ ⛔ PARÇACIK KATEGORİSİ ÖLÇÜLMEMİŞ — bu bir çarpışma/patlama filmi.
  Ders 21 (statik ateş) "Çevre" altına yazılmış, oysa rubrikte
  "Parçacık ve Malzeme Fiziği" kategorisi var. Yanlış kategoriye kaydedilmiş.
□ Diğer 3 rubrik kategorisi kayıt dışı
□ SPEC bloğu durumu bilinmiyor
```

**Tekrar QA gerekli mi?** Evet — Ders 21 doğru kategoriye taşınmalı. Parçacık
skoru bu filmde muhtemelen 2-3/10 idi ve hiç kaydedilmedi.

## 🆕 SENARYO QA'DAN GELEN TEKNİK BULGU (31.07.2026)

Senaryo raporu kapsam dışına taştı ve bir teknik hata bildirdi. Rubrik bunu
yasaklıyor ama bulgu **değerli** — bu filmin ilk timestamp'li kaydı:

```
1:25 — Duplicate protagonist walking (karakter klonlama)
```

Bu, **Ders 20'nin yayınlanan kurguda hâlâ görünür olduğunun ilk kanıtı.**
Ders 20 bu filmden çıkmıştı; hangi karede olduğu kayıtlı değildi. Artık var.
Zaman damgasına göre klon, planın **S7 (enkaz alanı)** sahnesinde.

---
---

# 📖 SENARYO QA — 31 Temmuz 2026

> **Prompt:** `../../QA_PROMPTLARI/SENARYO_QA_CRITIQUE_PROMPT.md`
> **Ham çıktı + sahne eşleme tablosu:** [`../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_SENARYO_HAM.md`](../02_HAM_RAPORLAR/THE_KALEIDA_CRASH/THE_KALEIDA_CRASH_SENARYO_HAM.md)

```
SKOR:             5.1/10  ·  VERDİKT: SHOOT WITH TRIMS
GİRDİ:            yalnız video — ⚠️ PLAN DOSYASI VERİLMEDİ
KAYIT DURUMU:     ŞARTLI — bulgular kullanılabilir, skor ortalamaya girmez
REÇETE DURUMU:    3 bulgu kabul · 2 reçete REDDEDİLDİ
```

## 📊 HİKAYE SKORLARI

| Kategori | Skor | Not |
|---|:---:|---|
| Kanca | 6/10 | patlama güçlü, kişisel yük yok |
| Önerme | 6/10 | anlaşılır ama gezegen mekaniği açıklanmıyor |
| Yapı | 5/10 | orta bölümde 4 geçiş sahnesi üst üste |
| **Karakter** | **4/10** | 🚨 tepki veriyor, seçim yapmıyor |
| Tema | 5/10 | bedel yok → tema dekoratif kalıyor |
| Diyalog | **N/A** | film tamamen sessiz — rubrik gereği puanlanmaz |
| Duygusal Yay | 5/10 | gerçek bir dip nokta yok |
| Final | 6/10 | ışık sütunu + iki güneş batışı işini yapıyor |
| **Özgünlük** | **4/10** | 🚨 serinin en düşük özgünlük skoru — Pitch Black |
| Tutundurma | 5/10 | orta bölüm kaybı riski |

## ✅ KABUL EDİLEN — dokümanda da doğrulanan

```
1. BEDELLİ SEÇİM YOK  ⭐ en değerli bulgu
   Film: çakılıyor → yürüyor → sinyal gönderiyor → bekliyor.
   Ayla hiçbir şey feda etmiyor, hiçbir şey seçmiyor.
   Karakter 4 ve Tema 5, aynı tek eksiğin iki yüzü.
   Karşılaştırma: Low Power'ın planında S20 = bedelli seçim var.

2. ORTA BÖLÜM GEÇİŞ YIĞILMASI
   12 sahnenin 4'ü yer değiştirme: S2 ufuk · S4 orman · S6 nehir ·
   S6.5 sıçrama. Videoya değil, plana bakarak da sayılabiliyor.
   → Kesmek değil: her geçişe farklı işlev (keşif / risk / bedel).

3. ÖZGÜNLÜK 4/10
   Plan "NEDEN VİRAL" bölümünde ayrışmayı yalnız KARDEŞ FİLMLERE karşı
   kuruyor (Glass Abyss, Inversion, Resonance Field). Tanınmış sinemaya
   karşı hiç kurmuyor — dış göz doğrudan Pitch Black dedi.
```

## ❌ REDDEDİLEN 2 REÇETE

```
❌ "Prizma Hayalet'e tehdit/rehber rolü ver"
   Plan bu sahneyi bilerek tehditsiz yazmış — video promptunda birebir:
   "No horror tone — this is curiosity, not threat."
   Ayrıca seri DNA'sı kötü adam yasaklıyor. Rubriğin kendi kuralı bu
   kısıtı hata saymayı yasaklıyor.
   ✅ Sorulması gereken doğru soru: Ayla bu karşılaşmadan DEĞİŞEREK
      çıkıyor mu? Çıkmıyor. Kusur tehditte değil, etkisizlikte.

❌ "1:00'daki sahneyi tamamen kes"
   O sahne planın S6'sı: CIVA NEHRİ — yüzen kristal levhalar üzerinden
   geçilen, filmin TEK gerçek risk anı. Kesilirse çarpışmadan sinyale
   kadar hiçbir tehlike kalmaz.
   ✅ Gerçek sorun: riskin ekranda okunmaması. Bu bir MANTIK/KURGU
      bulgusudur, senaryo bulgusu değil.
```

## ⚠️ RAPORUN GÖREMEDİĞİ — çünkü doküman verilmedi

```
S3.5  PRİZMATİK ŞOK DALGASI   viral ara sahne  → "yürüyüş" sanıldı
S6.5  AĞIRLIKSIZ SIÇRAMA      viral ara sahne  → "chasm jump", kısaltılsın dendi

Bu iki sahne hikaye için değil, DAĞITIM için tasarlanmış saf görsel beatler.
SPEC'in "VIRAL INTERSTITIALS" alanı boş kaldığı için rapor ikisini de
kesme/kısaltma listesine yazdı. Uygulanırsa filmin paylaşılabilir iki anı
gider.
```

## 🚨 DOĞRULAMA SIRASINDA ÇIKAN AYRI HATA — plan dosyasında

```
THE_KALEIDA_CRASH_PLANET_FILM.md "13 SAHNE" diyor.
Dosyada 12 sahne bloğu var. SAHNE 3 HİÇ YOK — S2'den doğrudan S3.5'e atlıyor.
12 promptun 12'si de kendini "Scene N of 13" diye tanıtıyor.

→ Kalite tablosundaki "Full (tam film)" kapsamı aslında 12 sahne.
→ Numaralandırmayı düzeltmek mi, eksik S3'ü yazmak mı: içerik kararı.
  QA kaydı kendi başına değiştirmedi.
```

---

# 🔗 MANTIK VE DEVAMLILIK QA — 31 Temmuz 2026

## 📋 KÜNYE

```
RUBRİK:        MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md — 8 kategori
GİRDİ:         yalnızca video (rubrik doküman istemiyor — tasarım gereği)
SÜRE:          125 s (2:05) · 12 blok gözlendi
BASELINE:      SELF-CONSISTENCY
GENEL SKOR:    4.0/10
KARAR:         FIXABLE IN EDIT
GEÇERLİLİK:    ✅ GEÇERLİ
```

**⭐ Sahne sayısı ilk kez tuttu:** rapor 12 blok saydı, plan dosyasında 12
prompt bloğu var. (Belgenin başlığı "13 SAHNE" diyor — bu belgenin kendi
hatası, filmin değil. Bkz. yukarıdaki teknik QA notu.)

## 📊 SKORLAR

| Kategori | Skor | Çekirdek sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | 6/10 | 1:12'deki sıçrama havada kalma süresi diğer sahnelerin yerçekimiyle çelişiyor |
| **Sayaç Mantığı** | **8/10** | ⭐ Mor ayak izi sistemi 6 sahnede de tutarlı — projenin en yüksek sayaç skoru |
| Mekan Coğrafyası | 4/10 | Kristal ova → Dünya çam ormanı → kanyon, geçiş yok |
| **Zaman ve Işık** | **3/10** | 🚨 Gündüz → zifiri gece → çift güneş batımı, 8 saniye içinde |
| **Durum, Kostüm, Prop** | **2/10** | 🚨 Kask 4 kez açılıp kapanıyor · omuz yırtığı kendini onarıyor |
| **Nedensellik ve Bilgi** | **2/10** | 🚨 1:26'da ikinci bir protagonist kadraja giriyor |
| Sayı Tutarlılığı | 8/10 | Karakter sayısı 1 — 1:26 hariç |
| Kurulum ve Terk | 6/10 | Kristal kedi 0:50'de görünüp bir daha dönmüyor |

**🔴 BLOCKER: 2 · 🟠 MAJOR: 4 · 🟡 MINOR: 3**

---

## 🚨 DERS 20 AYNI FİLMDE İKİNCİ KEZ — VE HİÇ DÜZELTİLMEMİŞ

```
1:24  tek protagonist enkaza bakıyor
1:26  ikinci, birebir aynı protagonist yanında yürüyerek kadraja giriyor
```

**Ders 20 (karakter klonlama) bu filmden çıkmıştı.** Teknik QA'sında
Karakter 5/10 alan bulgu buydu. Şimdi aynı hata aynı karede yine duruyor.

⚠️ **Bu, dersin başarısızlığı değil — filmin hiç yeniden üretilmemesidir.**
Ders yazıldı, sonraki filmlerin promptlarına girdi, ama bu filmin kendi
görüntüsü düzeltilmedi. Ayrımı kaydetmek önemli: bir ders "işe yaramadı"
demek için, dersi taşıyan bir promptla ÜRETİLMİŞ bir klipte tekrar etmesi
gerekir.

**Düzeltme maliyeti:** `1:25–1:28` kesilir. 3 saniye. 0 USD.

---

## 🚨 GÜN IŞIĞI SIÇRAMASI — BIBLE'IN TANIMLAMADIĞI BİR DURUM

Plan dosyası üç ışık fazı tanımlamış (`satır 329-350`):

```
FAZ 1 — ÇAKILIŞ    baskın ışık: ateş topu
FAZ 2 — YOLCULUK   yumuşak, dağınık, gökkuşağı filtreli
FAZ 3 — ENKAZ      enkazın kendi ışığı + fener sütunu
```

**Hiçbiri gece değil.** Kurguda gözlenen:

```
1:15  parlak gündüz (kanyon)
1:22  zifiri gece (enkaz)          ← Bible'da böyle bir durum yok
1:44  zifiri gece (fener)
1:52  parlak çift güneş batımı     ← aynı mekan, 8 saniye sonra
```

Model tanımlanmamış bir durumu kendi doldurdu. Sahne başına ışık künyesi
yazılmadığı için her klip kendi saatini seçti.

→ **DERS 47** olarak kaydedildi: *Sahne arası ışık sıçraması.*
Çözüm: her prompt'un LIGHTING bölümüne saat + yön + renk sıcaklığı +
"güneş bu sekans içinde hareket etmez" cümlesi; ve plan aşamasında bir
**ışık takvimi tablosu.**

---

## 🌲 DÜNYA ÇAM ORMANI — KRİSTAL GEZEGENDE

```
1:15  "Earth pine tree forest appears on chasm edge; absent in previous scenes"
```

Gezegen baştan sona kristal olarak tasarlanmış. Model "forest" kelimesini
gördüğü yerde bildiği ormanı çizmiş.

→ **DERS 48** olarak kaydedildi: *Sahne arası biyom sıçraması.*
Çözüm: her prompt'un ENVIRONMENT bölümünün ilk cümlesi **BIOME CONSTANT**
olur ve negatif blok Dünya bitki örtüsünü **adıyla** yasaklar
(`pine, conifer, bark, green foliage, grass`). "Alien forest" demek yetmiyor.

---

## 📖 BELGE SORULARI — CEVAPLANDI

Rapor üç soru bıraktı. Üçü de plan dosyasından cevaplandı:

| Rapor sorusu | Plan dosyası ne diyor | Sonuç |
|---|---|:---:|
| Atmosfer kasksız solunabilir mi? | `satır 88` — "thick, humid, **breathable-pressure equivalent**" · `satır 180, 459` — **"VISOR PERSISTENCE RULE [LESSON 5]: Visor ALWAYS VISIBLE in every frame"** | ❌ **HATA** — basınç eşdeğeri "solunabilir" demek değil; vizör kuralı mutlak. 0:22 ve 1:02'deki çıplak baş ihlal |
| Senaryoda klon/halüsinasyon beati var mı? | Yok — belgede böyle bir sahne yok | ❌ **ÜRETİM HATASI** — Ders 20 |
| Yürüyüşün amaçlanan zaman ölçeği ne? | Üç ışık fazı tanımlı, **gece yok**; 12 sahne × 10 s = tek kesintisiz yolculuk | ❌ **HATA** — gece sahneleri tasarımda yok |

Rapor ayrıca bir şeyi sormadan doğru buldu:

```
0:28  omuz yırtığı var
1:28  yırtık YOK — takım kendini onarmış
1:52  yırtık geri gelmiş
```

Plan dosyası (`satır 176`): **"PERSISTENT across all scenes — suit damage
only ACCUMULATES, never [repairs]"**. Doğrudan Bible ihlali. Ders 8 ve 42'nin
birleşimi — hasar sıfırlanması.

---

## ✅ RAPORUN KENDİ DOĞRULUĞU

```
✅ 12 blok saydı — plan dosyasında 12 prompt bloğu var ✓
✅ "Eksik sahne" iddiası yok — plan elinde yoktu, uydurmadı
✅ Üç soruyu FLAGS altına SORU olarak yazdı
✅ Her bulgu iki timecode taşıyor
✅ Kristal kediyi "hata" değil OPEN THREAD diye işaretledi — doğru karar,
   rubriğin "kasıtlı seçimi hata sanma" kuralına uydu
✅ Kapsam dışı iki bulguyu puanlamadı
```

---

## 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 47 (yeni)  Sahne arası ışık sıçraması → LESSONS_LEARNED ✅ yazıldı
□ DERS 48 (yeni)  Sahne arası biyom sıçraması → LESSONS_LEARNED ✅ yazıldı
□ DERS 20 tekrarı Klon hâlâ ekranda — film yeniden üretilmedi, ders değil
□ DERS 5 İHLALİ   Bible'da yazılıydı, 4 kez tutmadı — tarif kilidi kanıtı
□ DERS 8+42       Omuz yırtığı kendini onardı — Bible'ın açık ihlali
□ Sayaç 8/10      ⭐ Mor ayak izi — projenin ölçülmüş en iyi novum tutarlılığı
                  Sebebi anlamlı: sayaç GÖRSEL ve her sahnede ekranda.
                  Soyut sayaçlar (Inversion'ın yerçekimi döngüsü) çöktü.
```
