# 📊 DERS ETKİNLİK RAPORU

> **Soru:** 50 dersin hangisi gerçekten çalışıyor?
> **Yöntem:** Ders X, Y filminden çıktı. Y'den SONRA QA edilen filmlerde
> aynı hata tekrar bildirildi mi? Tekrar bildirildiyse **ders tutmadı.**
> **Kanıt:** film adı + kategori skoru veya timestamp. Kanıtsız satır yok.
> **Tarih:** 31 Temmuz 2026 · yeni üretim yapılmadı

---

# ⚠️ 31.07.2026 — İKİ DÜZELTME (Canopy World'ün iki yeni raporundan)

Bu rapor yazıldıktan sonra aynı gün gelen iki rapor, iki bulgusunu düzeltti.
Düzeltmeler aşağıya işlendi; okumadan önce ikisini bil:

```
DÜZELTME 1 — KRONOLOJİ HATASI
Ders 17, 18 ve 20'yi "tekrar etti" saymıştım. Yanlış: kanıtların hepsi
DERSİN ÇIKTIĞI FİLMİN KENDİ GÖRÜNTÜSÜNDEN. O görüntü, ders yazılmadan
önce üretildi. Aynı karede aynı hatayı yeniden bulmak dersin işe
yaramadığını göstermez.
→ Bir ders ancak KENDİSİNDEN SONRA üretilen bir filmde test edilebilir.
→ 17, 18, 20 → ÇALIŞMIYOR listesinden ÖLÇÜLEMEDİ'ye taşındı. 8 → 6.

DÜZELTME 2 — ÖLÇÜM SAPMASI
Aynı film (Canopy World) ikinci kez ölçüldü: 4/10 → 3/10, kategori
sapması ortalama 1.33 puan, en fazla 2 puan.
→ Kalite tablosunun çözünürlüğü ±1.3. 1.5 puandan küçük farklar
  GÜRÜLTÜ. Aşağıdaki kategori analizinde bu sınır uygulandı.
```

---

# 1️⃣ ÖZET — 50 DERSİN DURUMU

```
✅ ÇALIŞIYOR        2   (%4)    — yazıldıktan sonra hiç tekrar etmedi, kanıtlı
❌ ÇALIŞMIYOR       6   (%12)   — SONRAKİ bir filmde tekrar etti, kanıtlı
🆕 ÇOK YENİ         6   (%12)   — 45-50, henüz test edilecek film üretilmedi
⛔ ÖLÇÜLEMEDİ      36   (%72)   — test edilecek sonraki üretim yok/kayıtsız
```

> ⚠️ **%68 değil %72.** Kronoloji düzeltmesi kör alanı büyüttü.
> Bu kötü haber değil — daha önce "ölçüldü" sandığımız üç satır aslında
> ölçülmemişti. Yanlış güven, bilinen cehaletten kötüdür.

> 🚨 **En önemli sayı %72.** Proje, kurallarının dörtte üçünün işe yarayıp
> yaramadığını **bilmiyor.** Sebep tek: 12 filmin 10'unda timestamp'li ham
> bulgu saklanmamış, elimizde yalnız kategori skoru var. "Fizik 4/10" hangi
> dersin ihlal edildiğini söylemiyor.

---

# 2️⃣ ❌ ÇALIŞMAYAN 6 DERS — kanıtlı

> **Geçerlilik kuralı:** Kanıt, dersin çıktığı filmden **sonra** üretilen bir
> filmden gelmeli. Aynı filmin kendi görüntüsü kanıt sayılmaz.

| Ders | Konu | Çıktığı film | Sonraki filmde tekrar | Kilit tipi |
|:---:|---|---|---|---|
| **1** | Tek çekim / gizli kesme | Canopy World (1.) | **8/8 filmde** — projenin en dirençli hatası | tarif |
| **3** | AI bloom | Canopy World (1.) | Orphan Bloom (7.) · Low Power (11.) | tarif |
| **5** | Vizör kaybolması | Canopy World (1.) | Kaleida (5.) `0:22·1:02` · Inversion `0:16·1:06·2:32` | tarif |
| **9** | Videoda yazı | Canopy World (1.) | Dead Approach (10.) `2:10 text overlay` | tarif |
| **13** | AI metin / ekran içeriği | Slow Tide (3.) | Dead Approach (10.) · Inversion `2:12 Dr. Kaya Uçan` | tarif |
| **37** | Ekipman durum geçişi | Dead Approach (10.) | Inversion (kask ON/OFF/MISSING 2/10) | **karışık** ↓ |

### Kronoloji yüzünden listeden ÇIKARILANLAR

```
17  çarpışma fiziği   kanıt: Tidal Hunt 0:54  → AYNI FİLM, ders oradan çıktı
18  canlı morphu      kanıt: Tidal Hunt 1:13  → AYNI FİLM
20  karakter klonlama kanıt: Kaleida 1:25     → AYNI FİLM
                      kanıt: Tidal Hunt 0:00  → Tidal Hunt Kaleida'dan ÖNCE
                                                üretildi (ders 17-19 vs 20-22)
2, 6, 7  Canopy World'ün 2. teknik QA'sında yeniden görüldü — ama aynı
         görüntüde. Kanıt değil, ilk bulguya gecikmiş timestamp.

Üçü de artık ÖLÇÜLEMEDİ. Test edilmeleri için o derslerden SONRA üretilmiş
bir filmde aranmaları gerekir; öyle bir ölçüm yok.
```

### Ders 37 tek başına her şeyi anlatıyor

Aynı ders iki farklı biçimde yazıldı ve iki farklı sonuç verdi:

```
TARİF BİÇİMİ (Inversion, Kaleida)      "Visor ALWAYS VISIBLE in every frame"
                                        → İKİSİNDE DE TUTMADI

SAYISAL BİÇİM (The Slow Stone)          "kask S21'de bir kez"
                                        → HİÇ TETİKLENMEDİ
```

Aynı kural. Aynı model. Farklı **biçim.** Sonuç ters.

---

# 3️⃣ ✅ ÇALIŞAN 2 DERS — ve ikisi de sayısal

| Ders | Konu | Kilit biçimi | Kanıt |
|:---:|---|---|---|
| **32** | Gemi/yapı ölçek tutarlılığı | `24 m` · `6 derece` | Slow Stone'da **hiç tetiklenmedi** |
| **37**(sayısal hali) | Ekipman durumu | `kask S21'de bir kez` | Slow Stone'da **hiç tetiklenmedi** |

**Örneklem 2 ve ikisi de aynı filmden.** Zayıf kanıt — ama tarif kilitlerinin
6/6 başarısızlığıyla karşılaştırıldığında yön net.

---

# 4️⃣ 🔑 SAYISAL KİLİT vs TARİF KİLİDİ — sayılar

| | Sayısal kilit | Tarif kilidi |
|---|:---:|:---:|
| Kanıtla test edilmiş ders | 2 | 6 |
| Tekrar etti | **0** | **6** |
| Tutma oranı | **%100** | **%0** |

```
TARİF KİLİDİ    "Visor ALWAYS VISIBLE"
                "No text of any kind"
                "Objects must obey collision"
                → modele bir NİTELİK anlatır. Model niteliği yorumlar.

SAYISAL KİLİT   "kask S21'de bir kez, diğer 12 sahnede kapalı"
                "gemi 24 m, eğim 6 derece"
                "bilek ekranı: S0 tam halka → S9 kapalı halka, 13 adım"
                → modele bir SAYIM verir. Sayım yorumlanamaz.
```

⚠️ **Sınır:** 2 vs 6 küçük bir örneklem ve iki başarı da aynı filmden geliyor.
Bu bir hipotez, kanıtlanmış yasa değil. **Ama sistemde ölçülmüş tek şey bu** —
ve bir sonraki filmde test edilecek tek şey de bu olmalı.

---

# 5️⃣ 📉 KATEGORİ DARBOĞAZI — "neden kamera düzelebiliyor da fizik düzelemiyor"

11 filmin kalite tablosundan hesaplandı:

| Kategori | En düşük | En yüksek | Ortalama | Yayılım | Seri |
|---|:--:|:--:|:--:|:--:|---|
| **Kamera** | 2 | **8** | 4.18 | **6** ⭐ | 2·3·3·4·3·3·6·4·3·**8**·**7** |
| Karakter | 3 | 7 | 4.82 | 4 | 7·4·4·3·5·4·5·5·3·6·7 |
| Çevre | 3 | 7 | 4.68 | 4 | **7**·5·5·3·4.5·5·4·5·5·5·3 |
| Fizik | 2 | **5** | 3.64 | 3 | **5**·4·3·2·4·4·4·4·3·3·4 |
| Canlı | 2 | 5 | 3.90 | 3 | 4·2·4.5·4·5 |
| Hareket | 3 | 5 | 4.15 | 2 | 4·4·3·4.5·4·4·4·4·5·5 |
| **Işık** | 4 | 6 | 5.00 | **2** 🚨 | **6·6·6**·4·5·5·5·5·4·4·5 |

### ⚠️ Işık: "ilk üç film daha iyiydi" örüntüsü ZAYIFLADI

İlk okumada şöyle görünüyordu: ilk üç filmde 6·6·6, sonra hiç 6 yok —
yani Ders 3 (AI bloom) yazıldıktan sonra kategori kötüleşti.

**Canopy World'ün ikinci ölçümü bunu sarstı:** aynı filmin ışığı ikinci
kez ölçüldüğünde **6 değil 4** çıktı. O "6"lar ölçüm sapması olabilir.

```
Kalan sağlam kısım:  Işık hiçbir ölçümde 6'nın üstüne çıkmadı ve
                     yayılımı en dar kategori (2 puan).
                     → Işık düzelmiyor. Ama "kötüleşti" diyemeyiz.
Düşen kısım:         "Ders 3 zarar verdi" iddiası. Kanıt yetersiz.
```

Bu, ±1.3 kuralının ilk uygulaması: tek filmin tek kategorisine dayanan
her sonuç, ikinci ölçümle yıkılabilir.

### Fizik hiç 5'i geçmedi

Ve o tek 5, hiçbir dersin yazılmadığı **ilk filmde.** 44 ders sonrasında
fizik ortalaması 3.64.

### Kamera neden farklı — asıl cevap

Kameranın iki sıçraması var ve **ikisi de prompt cümlesi değil:**

```
3 → 8   Low Power    SABİT LOCKOFF        = kamera hareketi TALEBİNİ SİLDİ
3 → 7   Slow Stone   sahneleri ayrı üret  = kesme İHTİYACINI SİLDİ
```

**Genel kural:**

> Bir kategori, o kategorideki **talebi kaldırabiliyorsan** düzelir.
> Talebi kaldıramıyorsan düzelmez.

| Kategori | Talep kaldırılabilir mi | Sonuç |
|---|---|---|
| Kamera | ✅ "kamera hiç hareket etmesin" → geçerli sinematik seçim | 2→8 |
| Işık | ⚠️ kısmen — ama sahne aydınlatılmak zorunda | 6→4, sabit |
| Fizik | ❌ sahnede su varsa su akmak zorunda | 2-5, sabit |
| Canlı | ❌ canlı varsa yürümek zorunda | 2-5, sabit |

**Üretim öncesi karşılığı:** Bir sahnede fizik riski varsa çözüm daha iyi
prompt değil — **o fiziği sahneden çıkarmak.** Su temasını kesme, canlıyı
uzak planda tut, parçacığı hareketsiz bırak. Bkz. `02_RISK_KARTLARI.md`.

---

# 6️⃣ ⛔ ÖLÇÜLEMEYEN 34 DERS — neden ve nasıl ölçülür

**Neden ölçülemiyor:** Ders 26 (halat fiziği) Orphan Bloom'dan çıktı.
Sonraki 4 filmde halat var mıydı? Bilinmiyor — çünkü raporlar sahne
envanteri tutmuyordu. "Fizik 4/10" hangi dersin ihlali olduğunu söylemiyor.

**Nasıl ölçülür — bedelsiz, yeni üretim gerektirmez:**

```
1. MANTIK_QA raporları SAHNE ENVANTERİ üretiyor (Tidal Hunt raporunda var:
   12 satır, her sahnede kim/ne var). Bu envanter, hangi dersin o filmde
   TEST EDİLDİĞİNİ söyler. Halat yoksa Ders 26 test edilmemiştir.
2. Her yeni QA raporunda bulgu satırına DERS NUMARASI yazılır:
      ❌ "0:54 — beast phases through character"
      ✅ "0:54 — beast phases through character  [DERS 17 TEKRAR]"
3. Bu tablo her rapordan sonra güncellenir.
```

→ Bu üç adım uygulanırsa 5-6 film sonra %72'lik kör alan kapanır.

---

# 6️⃣b 📏 ÖLÇÜM GÜVENİLİRLİĞİ — projenin ilk tekrar ölçümü

The Canopy World 31.07.2026'da **ikinci kez** teknik QA'dan geçti.
Aynı film, aynı kurgu, aynı rubrik:

| Kategori | 1. ölçüm | 2. ölçüm | Fark |
|---|:--:|:--:|:--:|
| Karakter | 7 | 5 | **−2** |
| Fizik | 5 | 4 | −1 |
| Kamera | 2 | 3 | +1 |
| Işık | 6 | 4 | **−2** |
| Çevre | 7 | 6 | −1 |
| Canlı | 4 | 3 | −1 |
| **Genel** | **4** | **3** | **−1** |

```
ORTALAMA MUTLAK SAPMA: 1.33 puan
YÖN: 6 kategorinin 5'i aşağı — sistematik, rastgele değil
```

### Bunun kestiği iddialar

```
❌ "Kaleida 4.5 > Hollow 4.0"          → 0.5 fark, gürültü içinde
❌ "Orphan Bloom 5 > Dead Approach 3"  → 2 puan, sınırda; dikkatli kullan
❌ Tek filmin tek kategorisine dayanan her sonuç

✅ "Kamera Low Power'da 8, ortalama 4.2"   → 3.8 fark, gürültünün 3 katı
✅ "Fizik 11 ölçümün 11'inde ≤5"           → örüntü, tek ölçüm değil
✅ "Tarif kilidi 6/6 tekrar etti"          → sayım, skor değil
```

**KURAL:** İki skor arasındaki fark **1.5 puandan küçükse fark yoktur.**
Bu kural bu rapordaki her karşılaştırmaya uygulandı.

**Sonraki adım:** İkinci bir filmi de iki kez ölçmek. Tek noktadan sapma
tahmini zayıf; iki nokta sapmanın filme mi rubriğe mi bağlı olduğunu söyler.

---

# 7️⃣ 📏 PROMPT UZUNLUĞU ↔ SKOR — ÖLÇÜLEMEDİ

Ölçülemedi çünkü hangi filmde promptun kaç dersi taşıdığı kayıtlı değil.
Ama şu **kayıtlı ve önemli:**

```
Prompt'un BİÇİMİ skoru etkiliyor — uzunluğu değil.

DERS 45: model prompt'un kendi künyesini ekrana çizdi.
         "[CHARACTER BIBLE]" etiketi ve "CAMERA: 75mm f/5.6 ISO 400"
         satırı görüntüye HUD olarak sızdı.
         → Prompt uzadıkça yapısal etiket sayısı artıyor.
           Yani uzunluğun zararı doğrudan değil, ETİKET ÜZERİNDEN.
```

**Ölçmek için gereken (tek seferlik, ucuz):** Aynı sahneyi üç promptla üret —
(a) çıplak, (b) +10 ders, (c) +50 ders. Aynı rubrikle puanla. Bu, projedeki
tek gerçek A/B testi olur ve 50 dersin ağırlığını tartar.

---

# 8️⃣ 🎯 BU RAPORDAN ÇIKAN 4 KARAR

```
1. YENİ DERS YAZMAYI DURDUR, MEVCUTLARI SAYISALLAŞTIR.
   50 ders yeterli. Tutma oranı %0 olan 6 tarif kilidini sayısal biçime
   çevirmek, 51. dersi yazmaktan daha değerli.
   → Öncelik: Ders 1 · 3 · 5 · 9 · 13 · 37

2. HER QA BULGUSUNA DERS NUMARASI ZORUNLU.
   Tek satırlık değişiklik, %72'lik kör alanı kapatan tek şey.

3. FİZİK VE CANLI'YI PROMPTLA DEĞİL, SAHNE SEÇİMİYLE ÇÖZ.
   İkisi de 11 filmde hiç 5'i geçmedi. Talep kaldırılamıyor →
   sahneden çıkarılmalı. Kamera 8'e bu şekilde çıktı.

4. IŞIK KURALINI YENİDEN AÇ.
   Ders 3 yazıldıktan sonra ışık skoru düştü. Bu, "kural işe yaramadı"dan
   daha kötü bir sinyal — kural ZARAR VERMİŞ olabilir.
   "No bloom" demek, modeli düz ve motivasyonsuz ışığa itiyor olabilir.
```

---

# 🔗 KAYNAK

| Veri | Dosya |
|---|---|
| 50 dersin metni ve kaynağı | `../LESSONS_LEARNED.md` |
| Kalite tablosu (11 film × 7 kategori) | `../LESSONS_LEARNED.md` §KALİTE TAKİP |
| Timestamp'li ham bulgular | `../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/` |
| Ders 5/37 karşılaştırması | `../LESSONS_LEARNED.md` §"DERS 5 VE 37..." |
