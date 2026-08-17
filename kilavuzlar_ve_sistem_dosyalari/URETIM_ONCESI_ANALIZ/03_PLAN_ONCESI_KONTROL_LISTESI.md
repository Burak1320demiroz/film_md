# ✅ PLAN ÖNCESİ KONTROL LİSTESİ

> **Ne zaman:** Plan ve Bible yazıldı, **tek kare üretilmedi.**
> **Süre:** ~15 dakika. Maliyeti sıfır.
> **Neden:** Aşağıdaki 12 maddenin **9'u gerçek filmlerde gerçekten oldu** ve
> hepsi üretimden SONRA, para harcandıktan sonra bulundu.
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
□ RİSK SAYISI: ___ / 9

  0-2 risk  → sistem bu filmi taşır
  3-4 risk  → dikkat, en riskli malzemeyi bir sahneye hapset
  5+ risk   → 🚨 bu film şu anki sistemle 5/10'un üstüne çıkamaz.
              Malzeme azalt. (Kanıt: Kamera 2→8, talebi kaldırınca oldu.)
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
C  □ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı · canlı)
D  □ risk sayımı yapıldı: ___/8
E  □ QA SPEC bloğu plan dosyasına yazıldı

İMZA: bu 12 madde işaretlenmeden üretim başlamaz.
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
| C | Slow Stone vs Inversion/Kaleida | `01_DERS_ETKINLIK_RAPORU.md` §4 |
| E | Low Power · Ring Walker · Kaleida | 4 şartlı/geçersiz QA raporu |
