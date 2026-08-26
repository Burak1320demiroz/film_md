# 🔍 THE LAST ARCHIVE — QA KAYDI

> **Kaynak dosya:** `yatay_2_4_dk_filmler_uzay/THE_LAST_ARCHIVE/THE_LAST_ARCHIVE_PLANET_FILM.md`
> **Teknik QA (VIDEO_QA):** ⚠️ **4/10 ŞARTLI** · ham: [`../02_HAM_RAPORLAR/THE_LAST_ARCHIVE_TEKNIK_HAM.md`](../02_HAM_RAPORLAR/THE_LAST_ARCHIVE_TEKNIK_HAM.md)
> **Mantık QA (MANTIK_QA):** ✅ **5.0/10** · ham: [`../02_HAM_RAPORLAR/THE_LAST_ARCHIVE_MANTIK_HAM.md`](../02_HAM_RAPORLAR/THE_LAST_ARCHIVE_MANTIK_HAM.md)
> **Senaryo QA:** ❌ yapılmadı
>
> ⭐ **Projede ikinci kez iki mercek aynı filme uygulandı** — ve ikisi
> birbirini görmedi. Aynı kare (1:00 parmak morphu) teknikte 🔴 BLOCKER,
> mantıkta kapsam dışı satırı olarak duruyor. Sınır çalışıyor.

---

# 🔧 TEKNİK QA (VIDEO_QA)

```
KAPSAM:        Compilation · 148 s
SPEC BLOĞU:    🚨 BOŞ — 12 alanın 12'si doldurulmadı
GEÇERLİLİK:    ⚠️ ŞARTLI — skor tabloya girer ama işaretli
GENEL SKOR:    4/10  ·  KARAR: REGENERATE
```

| Kategori | Skor | Sorun |
|---|:---:|---|
| Karakter | 5/10 | mumsu cilt, temasta el morphu |
| Fizik | 4/10 | kayan adımlar, hafif çarpmalar |
| Kamera | **6/10** | kararlı, motivasyonlu hareketler |
| Işık | 5/10 | parlayan yüzeylerde AI bloom |
| Çevre | 4/10 | kaya oymalarında ağır doku yüzmesi |
| Canlı | N/A | yok |
| Parçacık | 4/10 | iniş tozunda fiziksel kütle yok |
| Diyalog ve Ses | 5/10 | diyalog yok, SFX senkronu geçer |
| Kare Çapası | N/A | compilation |
| Negatif İhlal | **6** | morph · bloom · kayma · doku · kütle · mumsu cilt |
| Hareket | 4/10 | jello + moonwalk |

**🔴 BLOCKER 2 · 🟠 MAJOR 4 · 🟡 MINOR 3**

### ⚠️ SPEC KAPISI YİNE ATLANDI — ama bu kez dürüstçe bildirildi

```
SPEC BLOCK PROVIDED: no
→ 12 alan boş: CHARACTER · SUIT · HEIGHT · GRAVITY · ATMOSPHERE ·
  LOCOMOTION · LENS · CAMERA DISTANCE · CAMERA MOVE · LIGHT SOURCES ·
  FILL LIGHT · VEHICLE/STRUCTURE
```

**Plan dosyası depoda duruyor ve bu alanların hepsini içeriyor:**
gemi 340 m · iniş ayakları 15 m · İndeks Kulesi 800 m · 32mm Cooke
anamorfik · f/5.6 · ISO 400 · 3 metre kamera mesafesi · tek altın-beyaz güneş.

Rapor bunları **UNVERIFIABLE** işaretleyerek doğru davrandı — Slow Stone'un
uydurduğu yerde bu rapor "bilmiyorum" dedi. Sistem bu açıdan ilerledi.
Ama kapının kendisi hâlâ atlanıyor: **dördüncü çalıştırma, dördüncü boş SPEC.**

> **Sonuç:** Ölçek, yerçekimi, lens ve ışık kategorileri filmin tasarımına
> karşı ölçülmedi. 4/10 skoru "kötü görünüyor" der, "yanlış" demez.

---

# 🔗 MANTIK VE DEVAMLILIK QA

```
KAPSAM:        tam kurgu · 148 s · 14 blok
BASELINE:      SELF-CONSISTENCY
GEÇERLİLİK:    ✅ GEÇERLİ
GENEL SKOR:    5.0/10  ·  KARAR: FIXABLE IN EDIT
```

| Kategori | Skor | Sorun |
|---|:---:|---|
| Fiziksel Tutarlılık | **9/10** | ⭐ projenin en yüksek fizik tutarlılığı |
| Sayaç Mantığı | N/A | filmde sayaç yok |
| Mekan Coğrafyası | 4/10 | iniş ve kalkış zemini uyuşmuyor |
| Zaman ve Işık | 5/10 | gökyüzüne aniden dev gök cisimleri geliyor |
| **Durum, Kostüm, Prop** | **3/10** | 🚨 sol bilek: kumaş yama → dijital ekran |
| Nedensellik ve Bilgi | **9/10** | ⭐ keşif ilerleyişi doğrusal ve tutarlı |
| Sayı Tutarlılığı | **10/10** | ⭐ projenin ilk 10'u |
| Kurulum ve Terk | 8/10 | hologram projektörü bir kez kullanılıp bırakılıyor |

**🔴 BLOCKER 0 · 🟠 MAJOR 3 · 🟡 MINOR 1**

> **Projenin ilk BLOCKER'sız mantık raporu.** Dört mantık QA'sı içinde
> tek. Fizik 9, nedensellik 9, sayı 10 — bu film kendi kendisiyle
> çelişmiyor, sadece kostüm ve coğrafyada kayıyor.

---

## 📖 BELGE SORULARI — CEVAPLANDI

Rapor iki soru bıraktı. İkisi de plan dosyasından cevaplandı, **ikisi de hata:**

### 1. Gemi yer mi değiştirdi?

| Plan dosyası | Ne diyor |
|---|---|
| `SAHNE 1A — İNİŞ` | *"The landing zone at the base of Kütüphane, dense inscribed bedrock"* |
| `SAHNE 10A — YÜKSELİŞ` | *"[WORLD BIBLE] **The landing zone**, the Index Spire and inscribed plain extending in every direction"* |

**Aynı mekan.** Plan yer değiştirme tarif etmiyor — 10A açıkça "the landing
zone" diyor. → ❌ **HATA**, tasarım değil.

### 2. Bilek: yama mı, ekran mı?

Plan dosyası sol kolda **İKİ AYRI ŞEY** tanımlıyor (`satır 105-118`):

```
· "a soft, worn patch reading (in her own hand, faded) her expedition's
   informal NICKNAME for the mission"        ← kumaş yama · GÖREV LAKABI
· "a single deeply-worn WRIST DISPLAY on her left forearm, its screen
   displaying warm amber-gold translated glyphs"   ← EKRAN · ÇEVİRİLER
```

Ve `SAHNE 0` promptu (`satır 283`):
> *"its first two words already legible on her **display**: 'REMEMBER US.'"*

**"REMEMBER US" EKRANDA olacaktı, yamada değil.** Film 0:01'de metni kumaş
yamaya bastı. → ❌ **HATA.** Rapor bunu "yama ekrana dönüşüyor" diye okudu;
gerçek şu: **birinci sahnede ekran, yama olarak üretildi.**

> Bu, raporun bulamayacağı bir ayrım — plan olmadan iki nesnenin varlığı
> bilinemez. Rubriğin `FLAGS FOR DOCUMENT CHECK` mekanizması tam olarak
> bu yüzden var ve çalıştı.

### 3. Gökyüzündeki aylar (rapor sormadı, plan cevaplıyor)

```
Plan · satır 61-65:
  "A single, steady, warm golden-white sun"
  "a thin ring of ancient orbital data-satellites (long dead, drifting)
   is visible as a pale line across the sky"
```

**Tasarımda tek güneş ve ince bir uydu halkası var. Dev aylar YOK.**
→ ❌ **HATA.** Raporun "kes gitsin" önerisi doğru.

---

## 🚨 PLANIN GÖREMEDİĞİ: 3-4 SAHNE KURGUDA YOK

Mantık QA'sı bunu **yapısal olarak** bildiremez (planı yok). Elle karşılaştırıldı:

```
PLAN     17 blok   S0 · 1A · 1B · 2 · 2.5 · 3 · 4 · 4.5 · 5 · 6 · 6.5 ·
                   7 · 8 · 8.5 · 9 · 10A · 10B
KURGU    14 blok
FARK     -3 blok   ≈ 22 saniye eksik
```

Ring Walker (eksik) ve The Inversion (fazla) ile aynı aile — **üçüncü kanıt.**
Bu filmde eksik yönde.

⚠️ Hangi sahnelerin düştüğü elle eşleme gerektirir; viral ara sahneler
(2.5 · 4.5 · 6.5 · 8.5) ilk şüpheli — dördü de hikayeye değil dağıtıma
hizmet ediyor ve kurguda ilk kesilenler onlar oluyor.

---

## 🔁 DERS 45 İKİNCİ KEZ DOĞRULANDI — FARKLI BİR İSİM TÜRÜYLE

```
0:14  gemi motor podu boş
0:18  aynı pod üzerinde "KÜTÜPHANE" yazıyor
```

Ders 45 (prompt iskeletinin ekrana sızması) The Inversion'da **karakter adıyla**
doğmuştu ("Dr. Kaya Uçan"). Burada aynı hata **geminin adıyla** tekrarlıyor.

Plan dosyası gemiyi promptun içinde adıyla anıyor:
```
"The 340-meter Kütüphane descends, its two 8-meter engine clusters firing"
```

Model, cümledeki özel adı geminin gövdesine **tabela olarak** çizdi.

**Ders 45'in kapsamı genişledi:** yalnız karakter adı değil, **prompt'ta geçen
her özel ad** o nesnenin üstüne yazılabiliyor. Bu, D45'in çözüm bloğuna
eklendi.

⚠️ Ayrıca bu bir **negatif çekirdek ihlali:** plan `satır 250` "No text
(English/Latin) overlay in the image itself. No watermark." diyor.

---

## 📌 BU KAYITTAN ÇIKANLAR

```
□ DERS 45 genişletildi — özel ad → nesnenin üstüne tabela
□ Yeni ders YOK — teknik raporun kendi hükmü: "all errors map to
  existing lessons [4, 6, 10, 11, 27, 28, 33]" ✅ doğrulandı
□ Plan↔kurgu farkı ÜÇÜNCÜ kez: Ring Walker eksik · Inversion fazla ·
  Last Archive eksik. Kalıp değil, kural haline geldi.
□ SPEC kapısı 4. kez atlandı — ama ilk kez dürüstçe bildirildi
□ Senaryo QA yapılmadı — bu filmde ağlama sahnesi var (2:00), dramatik
  ölçüm olmadan filmin işe yarayıp yaramadığı bilinmiyor
□ Rapor içi tutarsızlık: başlık "13 blok" diyor, envanter 14 satır
  → küçük ama not edildi
```
