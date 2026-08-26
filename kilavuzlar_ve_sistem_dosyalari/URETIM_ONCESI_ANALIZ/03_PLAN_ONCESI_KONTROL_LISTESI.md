# ✅ PLAN ÖNCESİ KONTROL LİSTESİ

> **Ne zaman:** Plan ve Bible yazıldı, **tek kare üretilmedi.**
> **Süre:** ~20 dakika. Maliyeti sıfır.
> **Neden:** Aşağıdaki 14 maddenin **11'i gerçek filmlerde gerçekten oldu** ve
> hepsi üretimden SONRA, para harcandıktan sonra bulundu.
> **26.08.2026:** B3 (tema indeksi) ve B4 (açı yayı) eklendi — ikisi de
> yazılı kuralı olan ama hiçbir kapıda ölçülmeyen alanlardı; liste 12'den
> 14 maddeye çıktı.
> **Ek katman (06.08.2026):** `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §7'nin
> 6 senaryo/kamera maddesi bu listeyle BİRLİKTE koşulur — bu listenin
> yerine geçmez, üstüne eklenir.

---

# 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### A1 — Yasak ↔ anlatım çelişkisi ⭐ EN PAHALI HATA

```
□ Plan dosyasında "no text / NEVER text" yazan bir satır var mı?
□ Aynı dosyada bir ekranın/göstergenin İÇERİĞİ tarif ediliyor mu?
   ("the countdown reads 6:00:00", "the display shows 47%")

İKİSİ BİRDEN VARSA → PLAN BOZUK. Model her zaman YASAĞI seçer,
anlatım sessizce ölür ve QA'da görünmez (ekranda yanlış bir şey yoktur,
sadece bir şey yoktur).
```

> 🚨 **Gerçek olay:** The Tidal Hunt. Satır 285 `NEVER text`, satır 338
> `the countdown reads 6:00:00`. Sayaç ekrana hiç çıkmadı; "6 saatte geç"
> filminden geriye "bir kadın koşuyor" kaldı. → Ders 50

**Düzeltme:** Bilgiyi metinsiz kanala taşı — kapanan halka, su çizgisi,
gölge boyu. `02_RISK_KARTLARI.md` KART 5.

### A2 — Sahne sayısı tutuyor mu

```
□ Başlıkta yazan sahne sayısı ile dosyadaki sahne bloğu sayısı aynı mı?
□ Numaralarda atlama var mı? (S2 → S3.5 gibi)
□ Prompt gövdelerindeki "Scene N of X" ifadesi doğru X'i mi söylüyor?
```

> 🚨 **Gerçek olay:** The Kaleida Crash "13 SAHNE" diyor, dosyada 12 blok var,
> SAHNE 3 hiç yok, 12 promptun 12'si "Scene N of 13" diyor.

### A3 — Süre tutuyor mu

```
□ sahne sayısı × klip süresi = iddia edilen toplam süre?
   (12 × 10s = 120s.  "4:14" yazıyorsa bir yerde hata var)
```

### A4 — Yasaklı sahne tipi var mı ⭐ [DERS 77 · 06.08.2026]

> 🚨 **Gerçek olay:** DERS 69 (05.08) *"biniş/iniş hareketi hiçbir segmentte
> kadraja alınmaz — 0 kez"* diyordu. **Ertesi gün** THE STARLESS CIRCLE'ın
> planına S14 BİNİŞ sahnesi eklendi ("yedi basamak + eşikte son bakış") ve
> klon tam o sahnede çıktı (Nicelik 1/10 · Sayı-Ayrışma 1/10). Ders
> LESSONS_LEARNED'da duruyordu, iki rubriğe işlenmişti, plana hiç ulaşmadı.
> Dersler üretim ve QA kanallarına akıyor; **karar kanalına akmıyor.**

```
□ Plandaki HER sahne için sor — aşağıdaki tiplerden biri mi?
     · araç / kapak / airlock BİNİŞ-İNİŞ hareketi        [D69]  3 vaka
     · tek ışıklı loş iç mekâna GİRİŞ                    [D69]  1 vaka
     · aynalı-yansıtıcı yüzey önünde tek karakter        [D20 · D69]
     · novum'u TÜRETİLMİŞ optik fenomen taşıyor
       (gölge · yansıma · kostik · parlama deseni)       [D73]
     · novum'u bir YOKLUK taşıyor (boşluk, delik,
       "olmayan" bir şey)                                [D76]
     · jenerik / başlık kartı ya da kapak çıktısı        [D34 · D70 · D72]
□ VARSA: sahne ya çıkarılır ya dersin öngördüğü biçime dönüştürülür —
  ve karar plan dosyasına TEK SATIR olarak yazılır:
     "S14: biniş hareketi kadraj dışı — D69 ① gereği (06.08)"
□ Satır yoksa denetim YAPILMAMIŞ sayılır (D74 mantığı: kaydı olmayan kapı).
```

---

# 🔴 B. FİLMİN DORUĞU YAZILMIŞ MI

### B1 — Doruk anı bir sahnenin İÇİNDE mi

```
□ Filmin en yüksek gerilim anını hangi sahne TAŞIYOR? S___
□ O sahnenin video promptunda o an gerçekten TARİF EDİLİYOR mu?
□ Yoksa iki sahnenin ARASINA mı düşüyor?
```

> 🚨 **Gerçek olay:** The Tidal Hunt. S8 `"begins to climb as the wave closes"`
> → S9 `"the wave has passed"`. **Dalganın çarptığı an hiçbir sahnede
> yazılmamış.** Doruk iki sahne arasında. Kurguyla kapatılamaz.

**Test:** Sahne listesini oku, her geçişte sor — *"burada ekranda görülmeyen
ama olması gereken bir şey var mı?"*

### B1b — Katmanlı dünya ise ışık takvimi var mı

```
□ Film irtifa/bölge/derinlik gibi bir eksende ilerliyor mu?
□ Öyleyse her sahnenin katmanı ve o katmanın ışığı TABLO halinde yazılı mı?
□ Sahneleri eksene göre sıralayıp ışığı okuduğunda monotonik mi?
   (parlak → karanlık → parlak = plan ya da üretim yanlış)
```

> 🚨 **Gerçek olay:** The Canopy World, 7 katman, 3.000m'den 0m'ye kesintisiz
> iniş. Kurgu sırası plana birebir uygun — ama Kök Labirenti sahnesi
> `"cold blue-white light"` yerine parlak güneşli üretilmiş. Mantık QA'sı
> ışık salınımını gördü ama sebebi kurguda sandı; belge kontrolünde
> üretim hatası olduğu çıktı.

### B2 — Bedelli seçim var mı

```
□ Karakter bir ŞEY seçiyor mu, yoksa olaylara tepki mi veriyor?
□ Seçtiğinde neyi KAYBEDİYOR?
□ Kaybı hangi sahnede GÖRÜLÜYOR? S___
```

> 🚨 **Gerçek olay:** İki bağımsız senaryo QA'sı, iki farklı filme aynı
> gerekçeyle Karakter 4/10 verdi: Ring Walker ve Kaleida Crash.
> Kaleida: çakılıyor → yürüyor → sinyal gönderiyor → bekliyor. Bedel yok.
> Karşı örnek: Low Power S20 — anahtarı çeviriyor, kendi hayatını veriyor.

### B3 — Tema hangi sahnede EKRANA çıkıyor ⭐ 🆕 26.08.2026

```
□ Planda TEMA satırı var mı — tek kelime
   (TEMA_MUHENDISLIGI_KILAVUZU.md §3'ün sekiz temasından biri)
□ Tema, novum kelimesi geçmeden tek cümleyle söylenebiliyor mu?
   "bu film ___ hakkında"                              [TEMA §9 son madde]
□ ⭐ ASIL MADDE — tema hangi sahnelerde MOTİFE dönüşüyor:
   S___ , S___ , S___     (en az 3 sahne numarası · TEMA §5 matrisi)
   Her sahnede en az BİR 3. derece indeks: kamera · ışık · nesne · kinesik
□ B2 ile çapraz oku: bedelli seçimin yaşandığı sahne bu listede mi?
   Değilse tema olay örgüsüne bağlı DEĞİL, süslemedir.
```

> 🚨 **Gerçek olay:** THE KALEIDA CRASH · film kaydının tema satırı:
> **"bedel yok → tema dekoratif kalıyor" (Tema 5/10)** — aynı kayıtta
> Karakter 4/10 "tepki veriyor, seçim yapmıyor". Yani tema düşüşü B2'nin
> (bedelli seçim) doğrudan sonucu; iki madde aynı boşluğu iki yerden ölçüyor.
>
> ⚠️ **ÖLÇEK DÜRÜSTÇE:** "tema yaygın olarak zayıf" iddiasının tek veri
> tabanı ⛔ KAPALI `03_HIKAYE_KALITE_TABLOSU.md`'dir: geçerli 13 satırın
> **7'sinde Tema ≤5** (tam 4 olan 2 film: Stone Sky · Blind Return).
> O tablo 22.08'de kapatıldı ve AGENTS §1'e göre yeni tablolarla
> KARŞILAŞTIRILAMAZ — eğilim göstergesidir, kanıt değil. Canlı T4'te
> bugün yalnız 2 film var. Bu madde bir eğilime karşı yazıldı; eğilimin
> doğrulanması E fazının (pilot + mod D ölçümü) işidir.
>
> ⚠️ Cold Burn FRAGMAN kaydında aynı cümle geçer ama orada **bulgu
> DÜŞÜRÜLDÜ** (fragman merceği + önerme kapısı). Kanıt sayılmaz.

**Düzeltme:** `TEMA_MUHENDISLIGI_KILAVUZU.md` §5 matrisinden temanın
satırını al, motifi sahne sahne dağıt. Betik tarafı:
`prompt_kontrol.py` TEMA satırını ve sahne indekslerini arar.

### B4 — Açı yayı yazıldı mı ⭐ 🆕 26.08.2026

```
□ SAHNE-KURULUM DİZİSİ yazılı mı?   (örn. A · C · A · C · B · A)
   kurulum = açı + ölçek + kamera konumu       [ACI_YAYI §4]
□ Ardışık HER çift güvenli bandı tutuyor mu?   [ACI_YAYI §3]
   ≥1 tam ölçek kademesi  VE  ≥45° açı farkı
   (bilinçli ŞOK ise işaretli — filmde en fazla 2)
□ Kurulum SAYISI bandın içinde mi?             [ACI_YAYI §4]
   6 sahne → en az 3 · 12 sahne → en fazla 5-6 · uzun formatta
   kurulum sayısı sahne sayısının yarısını geçmez
□ ⭐ AÇI TİPİ sayısı ≥3 mü?                     [KAMERA_ACISI §2]
   (alt · üst · tepe · eğik · göz hizası · OTS · profil · POV)
   Üç kurulumun üçü de alttan bakıyorsa kurulum çeşitliliği YOK,
   yalnız mesafe çeşitliliği vardır.
□ Derece yazan her satır abartı bandında mı?   [KAMERA_ACISI §5]
   dutch 5-15° ideal · 15-30° meşru · 35°+ ⛔ kiç
   alt açı 15-30° meşru · 45°+ ⛔ · üst açı 15-30° · 45-60° ⛔ ölü bölge
□ Doruk sahnesi en yüksek kontrast sıçramasını taşıyor mu? [ACI_YAYI §9]
```

> 🚨 **Gerçek olay:** THE BRIGHT TETHER (26.08.2026, deponun en yeni filmi).
> 6 sahne, 3 kurulum — `ACI_YAYI §4` bandının **içinde** ve dosya bunu
> kendi kontrol bloğunda doğru şekilde ilan ediyor. Ama 6 video promptunun
> kamera satırından yalnız **3'ü benzersiz**: S0·S2·S5 birebir aynı cümle,
> S1·S3 birebir aynı cümle. Üç kurulumun üçü de yerden bakıyor (0.90 m ·
> 0.35 m · 0.20 m), lens 6/6 sahnede 24mm. Yani bant ASGARİYİ ölçüyor,
> hiçbir kapı asgarinin üstüne itmiyordu — ve açı TİPİ hiç sayılmıyordu.

**Düzeltme:** Bu maddenin dört sayısı da betikte ölçülüyor
(`prompt_kontrol.py` · kurulum çeşitliliği · açı sözlüğü · abartı eşiği).
Liste maddesi betiğin göremediği tek şeyi sorar: dizinin VURUŞLA eşleşmesi
(`KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` §3 vuruş→açı tablosu).

> ⛔ **KLİP İÇİ lockoff bu maddeyle ÇELİŞMEZ.** Kamera klip içinde hiç
> hareket etmez (KART 8); değişen tek şey sahneler ARASINDA kurulumdur.
> Sahneler zaten ayrı kliplerde üretiliyor — farklı açıdan çekmenin
> gizli kesme riski sıfır (`02_RISK_KARTLARI.md` KART 8 kapsam bloğu).

---

# 🟠 C. SAYISAL KİLİTLER YAZILDI MI

> Ölçülmüş tek gerçek: **tarif kilidi %0 tuttu, sayısal kilit %100 tuttu.**
> Aşağıdakilerin hepsi SAYI içermeli. İçermiyorsa tutmayacak.

```
□ İNSAN SAYISI      "tam 1 insan, 13 sahnenin 13'ünde"
                    ❌ "she is alone"          ✅ HUMAN COUNT LOCK: 1 × 13

□ KASK TAKVİMİ      "kapalı S0-S12, açık 0 sahne"
                    ❌ "visor ALWAYS VISIBLE"  ✅ HELMET STATE SCHEDULE

□ ÖLÇÜ              "gemi 140 m, bacak 20 m, viewport 1 m"
                    ❌ "massive ship"          ✅ sayı + referans nesne

□ YERÇEKİMİ         "0.38g — düşen nesne 1 saniyede 1.9 m"
                    ❌ "low gravity"           ✅ sayı + sonuç

□ SIVI TEMASI       "sıvıya dokunulan sahne: 2 (S6, S9). Diğer 11'de arka plan"
                    ❌ "she touches the water" ✅ sahne sayımı

□ CANLI ANATOMİSİ   "4 bacak, 1 baş, 1 kuyruk — 13 sahnenin hepsinde"
                    ❌ "creature anatomy fixed" ✅ parça sayımı
```

---

# 🟠 D. RİSK SAYIMI

```
□ 02_RISK_KARTLARI.md açıldı ve malzeme listesi işaretlendi
□ RİSK SAYISI: ___ / ___    ← payda 02_RISK_KARTLARI RİSK TOPLAMI'ndaki
                               soru sayısıdır (26.08.2026'da 12). Buraya
                               sabit sayı yazma, oradan oku.

  0-2 risk  → sistem bu filmi taşır
  3-4 risk  → dikkat, en riskli malzemeyi bir sahneye hapset
  5+ risk   → 🚨 bu film şu anki sistemle 5/10'un üstüne çıkamaz.
              Malzeme azalt. (Kanıt: Kamera 2→8, talebi kaldırınca oldu.
              ⛔ Kaldırılan talep KLİP İÇİ kamera hareketiydi. Sahneler
              ARASI açı değişimi bu karara dahil değildir ve B4 maddesiyle
              ayrıca zorunludur — ACI_YAYI_VE_SEKANS_KILAVUZU.md §3.)
```

---

# 🟡 E. QA'YA HAZIRLIK — üretimden önce yazılır

Bu blok plan dosyasının sonuna eklenir. Üretim bitince QA promptlarının
SPEC bloğuna **doğrudan kopyalanır.** Yazılmazsa QA künyesi elle
hatırlanır ve bozulur — projede 4 rapor bu yüzden şartlı/geçersiz oldu.

```
□ QA SPEC BLOĞU plan dosyasına yazıldı:

  FILM:                 ___
  FORMAT:               ___
  SCENE COUNT:          ___     ← dosyadaki blok sayısıyla doğrulandı
  RUNTIME:              ___ s   ← sahne × klip süresi ile doğrulandı
  DIALOGUE LINES:       ___     ← konuşmalı sahne numaraları: ___
  SILENT SCENES:        ___
  VIRAL INTERSTITIALS:  ___     ← S___, S___  (bunlar KESİLEMEZ)
  PROTAGONIST:          ___     ← ad + meslek
  CENTRAL CHOICE:       S___    ← bedelin görüldüğü sahne
```

> 🚨 **VIRAL INTERSTITIALS satırı neden kritik:** Kaleida Crash'in senaryo
> QA'sı bu alan boş olduğu için iki viral ara sahneyi "gereksiz geçiş"
> sanıp kesme listesine yazdı. Filmin paylaşılabilir iki anıydı.

---

# 📋 TEK SAYFALIK ÖZET — kopyala, plan dosyasının sonuna yapıştır

```
ÜRETİM ÖNCESİ KONTROL — <FİLM ADI>            tarih: __________

A1 □ "no text" ile ekran içeriği aynı dosyada YOK
A2 □ sahne sayısı: başlık ___ = blok ___ = "Scene N of X" ___
A3 □ süre: ___ sahne × ___ s = ___ s = iddia edilen süre
A4 □ yasaklı sahne tipi taraması yapıldı (biniş-iniş · loş mekâna giriş ·
     ayna · türetilmiş fenomen novum · yokluk novum · jenerik kartı)
     bulunan sahne + karar satırı: ______________________ [D77]
B1 □ doruk anı S___ içinde tarif edildi, sahne arasına düşmüyor
B2 □ bedelli seçim S___, kayıp S___ sahnesinde görülüyor
B3 □ TEMA: ___________ · motife döndüğü sahneler: S___, S___, S___
     (≥3 sahne · B2'nin bedel sahnesi bu listede mi?)          [TEMA §5/§9]
B4 □ kurulum dizisi: _______________ · kurulum sayısı ___ · açı tipi ___
     ardışık çiftler güvenli bantta (≥1 kademe + ≥45°) · şok sayısı ___/2
     derece satırları abartı bandında               [ACI_YAYI §3-4 · KAMERA §5]
C  □ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı · canlı)
D  □ risk sayımı yapıldı: ___/___  (payda: 02_RISK_KARTLARI soru sayısı)
E  □ QA SPEC bloğu plan dosyasına yazıldı

İMZA: bu 14 madde işaretlenmeden üretim başlamaz.
```

---

# 🔗 KAYNAK

Bu listedeki her madde bir gerçek olaydan çıktı:

| Madde | Kaynak film | Nerede belgelendi |
|---|---|---|
| A1 | The Tidal Hunt | Ders 50 · `../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TIDAL_HUNT_MANTIK_HAM.md` |
| A2 | The Kaleida Crash | `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md` |
| B1 | The Tidal Hunt | aynı ham rapor · "dalga atlaması planda da var" |
| B2 | Kaleida · Ring Walker | `../FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` |
| B3 | The Kaleida Crash | `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md` · Tema 5/10 "bedel yok → tema dekoratif kalıyor" · eğilim: ⛔ KAPALI `03_HIKAYE_KALITE_TABLOSU.md` 7/13 ≤5 · kural: `../TEMA_MUHENDISLIGI_KILAVUZU.md` §5/§9 |
| B4 | The Bright Tether (26.08.2026) | 6 kamera satırının 3'ü benzersiz · `../ACI_YAYI_VE_SEKANS_KILAVUZU.md` §3-4 · `../KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` §2/§5 |
| C | Slow Stone vs Inversion/Kaleida | `01_DERS_ETKINLIK_RAPORU.md` §4 |
| E | Low Power · Ring Walker · Kaleida | 4 şartlı/geçersiz QA raporu |
