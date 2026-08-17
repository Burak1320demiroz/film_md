# 🎬 Yatay 10-20 Dakika Filmler — Veo Üretim Formatı

> **3 Perde Mimarisi | Değişken Faz Sayısı | 8 Saniyelik Sahne Standardı | Start/End Frame Zinciri**
> Bu format `yatay_7_9_dk_filmler/` formatının **üstüne** kurulmuştur.
> 5 faz mimarisi 8 dakikada doyuma ulaşır; 15 dakikada faz sayısını artırmak yetmez —
> fazların ÜSTÜNE bir katman (PERDE) gerekir.

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 10-20 dakika (600-1200 saniye) |
| **Oryantasyon** | 16:9 yatay (widescreen) |
| **Üst katman** | **3 perde (sabit)** |
| **Orta katman** | **6-12 faz (değişken — süreyi bu belirler)** |
| **Alt katman** | Faz = 3 sekans × 4 sahne = 12 sahne |
| **Klip süresi** | **8 saniye / sahne** (Veo native — extend gerekmez) |
| **Toplam sahne** | 72-144 sahne (hedef: 108) |
| **Tek çekim kuralı** | Her sahne ayrı, kesintisiz tek çekim |
| **Görsel üretim** | Start/End Frame zinciri (7-9 dk formatıyla aynı) |
| **Referans paketi** | **EN BAŞTA — pazarlıksız** |

### ⏱️ Süre Matematiği

```
BİRİM ZİNCİRİ:
  1 sahne  =   8 saniye
  1 sekans =   4 sahne  =  32 saniye
  1 faz    =   3 sekans =  12 sahne =  96 saniye  (1:36)
  1 perde  = 2-4 faz    = 24-48 sahne = 192-384 saniye

SÜRE TABLOSU (faz sayısına göre):

| Faz | Perde dağılımı | Sahne | Saniye | Süre  | Ne zaman              |
|-----|----------------|-------|--------|-------|-----------------------|
|  6  | 2-2-2          |  72   |  576   | 9:36  | ⚠️ alt sınırın altında |
|  7  | 2-3-2          |  84   |  672   | 11:12 | Sıkı, tek mekan       |
|  8  | 3-3-2          |  96   |  768   | 12:48 | Tek karakter, tek arc |
|  9  | 3-3-3          | 108   |  864   | 14:24 | **VARSAYILAN**        |
| 10  | 3-4-3          | 120   |  960   | 16:00 | İki karakter / çift arc|
| 11  | 3-5-3          | 132   | 1056   | 17:36 | Katmanlı dünya        |
| 12  | 4-4-4          | 144   | 1152   | 19:12 | ÜST SINIR             |
```

### ⏱️ 10 SANİYELİK SAHNE VARYANTI (bilinçli sapma — THE SECOND SHIP)

```
Varsayılan 8 saniyedir (Veo native, extend gerekmez). Yavaş tempolu
filmlerde 10 saniye seçilebilir. Seçilirse süre tablosu şu olur:

| Faz | Sahne | Saniye | Süre  | Not                          |
|-----|-------|--------|-------|------------------------------|
|  7  |  84   |  840   | 14:00 |                              |
|  8  |  96   |  960   | 16:00 |                              |
|  9  | 108   | 1080   | 18:00 |                              |
| 10  | 120   | 1200   | 20:00 | ⛔ TAVAN — sahne eklenemez    |
| 11  | 132   | 1320   | 22:00 | ❌ formatı aşar               |

⚠️ 10 saniyelik sahnede FAZ TAVANI 10'dur. 8 saniyedeki 12 fazlık üst
   sınır burada geçerli değildir.

⚠️ ÜRETİM BEDELİ: Veo 3.1 native klip 8 saniye. 10 saniye iki yoldan gelir:
   (A) extend + 10.00s'ye kırpma → maliyet ~%25 artar, hareket doğal
   (B) 0.8× optik akışlı retime → maliyet sıfır, YALNIZ lockoff ve
       hareketsiz sahnelerde. Yürüyen/koşan figürde yasak.
   Yol seçimi sahne bazında faz dosyasında yazılır.

✅ KAZANÇ: 10 saniyelik sahne müzik ızgarasına bedava oturur —
   48/72/96/120/144 BPM tam ölçü verir (müzik kılavuzu §14).
```

> **Alt sınır kuralı:** 6 faz (9:36) bu formatın süre bandına girmez.
> **En az 7 faz** kullanılır; 10 dakikanın altına inen bir hikaye
> `yatay_7_9_dk_filmler/` formatına aittir — zorlamayın.
>
> **Üst sınır kuralı:** 12 faz / 144 sahne kesin tavandır. Post-prodüksiyon
> köprüleri (J-cut, ses köprüsü) ile ~20 dakikaya oturur. 20 dakika aşılmaz.

---

## 🏛️ NEDEN PERDE KATMANI — 5 FAZ NEDEN YETMİYOR

7-9 dk formatının 5 fazı (KURULUŞ → DERİNLEŞME → DÖNÜM → ZİRVE → ÇÖZÜLME)
**tam bir dramatik yaydır**. Faz sayısını 9'a çıkarmak o yayı bozar:

```
YANLIŞ:  9 faz = 9 ayrı dramatik işlev
         → izleyici hangi fazın ne olduğunu takip edemez
         → 4 tane "dönüm noktası" olur, hiçbiri dönüm gibi hissettirmez

DOĞRU:   3 perde = 3 dramatik işlev (klasik üç perde)
         her perde kendi içinde 3 fazlık mini yay barındırır
         → faz = SAHNE GRUBU (üretim birimi)
         → perde = DRAMATİK BİRİM (anlatı birimi)
```

**Kritik ayrım:** Bu formatta faz artık bir dramatik işlev değil,
bir **üretim paketidir** (12 sahne = 15 imaj = 1 çalışma günü).
Dramatik işlev perdeye taşınmıştır.

---

## 📊 3 PERDE HARİTASI (9 fazlık varsayılan)

| Perde | Ad | Faz | Sahne | Süre | Zaman aralığı | İşlev |
|---|---|:---:|:---:|:---:|---|---|
| **I** | KURULUŞ VE İNİŞ | 1-3 | 36 | 288s | 0:00 – 4:48 | Dünya, karakter, soru, eşik |
| **II** | KEŞİF VE ÇÖZÜLME | 4-6 | 36 | 288s | 4:48 – 9:36 | Gerçek, bedel, geri dönüşsüzlük |
| **III** | ZİRVE VE KAPANIŞ | 7-9 | 36 | 288s | 9:36 – 14:24 | Doruk, çözüm, varoluşsal kapanış |

### Perde içi faz işlevleri

```
PERDE I — KURULUŞ VE İNİŞ
  FAZ 1  Ölçek şoku, dünyanın kuralı, karakterin varlığı
  FAZ 2  Rutin, yetkinlik, görev tanımı, ilk diyalog
  FAZ 3  İlk tuhaflık, sorunun netleşmesi → PERDE DÖNÜŞÜ 1 (eşik geçilir)

PERDE II — KEŞİF VE ÇÖZÜLME
  FAZ 4  İçeri: yeni katman, görsel şok, keşif eylemi
  FAZ 5  Kanıt ve gerçek — filmin "aha" karesi bu fazda
  FAZ 6  Sistem/beden/iletişim bozulur → PERDE DÖNÜŞÜ 2 (geri dönüş yok)

PERDE III — ZİRVE VE KAPANIŞ
  FAZ 7  Baskı: tehdit fiziksel, çıkış kapanır
  FAZ 8  DORUK + İMZA ÇEKİM — filmin tek en iyi karesi
  FAZ 9  Çözülme: nefes, muhasebe, ayrılış, final kare
```

> 10-12 fazlık versiyonlarda eklenen fazlar **Perde II'ye** girer
> (keşif katmanı derinleşir). Perde I ve III asla 4 fazı geçmez —
> uzun kuruluş sıkıcı, uzun kapanış duygusal etkiyi seyreltir.

### ⚠️ Faz sayısı esnekliği kuralları

```
□ Perde II hiçbir zaman en kısa perde olamaz
□ Perde I hiçbir zaman en uzun perde olamaz
□ DORUK fazı (Perde III'ün ilk-orta fazı) tek başına en yoğun faz olmalı
□ Her perde en az 2 faz içerir — 1 fazlık perde, perde değildir
```

---

## 🔗 START/END FRAME ZİNCİRİ — 7-9 DK İLE AYNI

Üretim tekniği birebir aynıdır: `../yatay_7_9_dk_filmler/kilavuzlar/KESINTISIZ_VIDEO_URETIM_TEKNIGI.md`

```
Formül:  x. İmaj  →  (x+1). İmaj  =  x. Video

Sekans içi:      zincirleme (4 sahne → 5 imaj)
Sekanslar arası: zincir kırılır, yeni çapa (anchor) imajı
```

**İmaj sayısı hesabı (9 fazlık varsayılan):**
```
1 faz  = 3 sekans × (4 video + 1 kapanış imajı) = 15 imaj / 12 video
9 faz  = 135 imaj / 108 video

12 fazlık üst sınır = 180 imaj / 144 video
```

> ⚠️ **Bu formatın gerçek maliyeti imaj üretimidir.** 135 imaj, 7-9 dk
> formatının (75 imaj) **1.8 katıdır** ve karakter kayması riski doğrusal
> değil, birikimlidir. Aşağıdaki kimlik yenileme protokolü zorunludur.

---

## 🔒 KİMLİK YENİLEME PROTOKOLÜ (bu formata özel, yeni)

7-9 dk formatında tek referans portre 75 imaj boyunca yeterliydi.
135+ imajda yeterli **değildir** — 5. fazdan sonra yüz sürüklenir.

```
ADIM 0 (üretimden önce):  3 açılı referans portre + kilitli seed
                          → REFERANS_PAKETI.md

HER FAZ BAŞINDA:          Faz çapa imajı, referans portreyi YENİDEN
                          referans alarak üretilir — bir önceki fazın
                          son karesini DEĞİL.
                          (aksi halde hata birikir: 9 nesil kopya)

HER FAZ SONUNDA:          Faz çapa imajı ile ADIM 0 portresi yan yana
                          karşılaştırılır → SUREKLILIK_LEDGERI.md'ye işlenir
                          Sapma varsa faz yeniden üretilir, sonraki faza GEÇİLMEZ

PERDE SONUNDA:            Tam denetim — 3 fazın 45 imajı ADIM 0'a karşı
                          kontrol edilir
```

> **Neden faz başında zincir kırılır:** Zincirleme devamlılık sekans içinde
> güçlü, faz boyunca kabul edilebilir, film boyunca **yıkıcıdır**.
> Faz sınırı bilinçli bir "sıfırlama noktasıdır" — dramatik olarak da
> zaten faz geçişinde mekan/zaman sıçraması vardır.

---

## 📁 KLASÖR VE DOSYA DÜZENİ

9-12 faz dosyası tek klasöre sığmaz. Perde bazlı alt klasör kullanılır:

```text
yatay_10_20_dk_filmler/
└── FILM_ADI/
    ├── README.md                      <-- Master İncil + 3 perde / N faz haritası
    ├── REFERANS_PAKETI.md             <-- İLK ÜRETİLEN DOSYA (zorunlu)
    ├── SUREKLILIK_LEDGERI.md          <-- Faz/perde denetim defteri (bu formata özel)
    ├── MUZIK_VE_SES.md                <-- 864 saniyelik müzik yayı + ses tasarımı
    │
    ├── PERDE_1_KURULUS/
    │   ├── 01_FAZ_1_[AD].md
    │   ├── 02_FAZ_2_[AD].md
    │   └── 03_FAZ_3_[AD].md
    ├── PERDE_2_KESIF/
    │   ├── 04_FAZ_4_[AD].md
    │   ├── 05_FAZ_5_[AD].md
    │   └── 06_FAZ_6_[AD].md
    └── PERDE_3_ZIRVE/
        ├── 07_FAZ_7_[AD].md
        ├── 08_FAZ_8_[AD].md
        └── 09_FAZ_9_[AD].md
```

### Dosya içerikleri

| Dosya | İçerik |
|---|---|
| **README.md** | Film kapağı promptu, tüm Bible'lar (World/Character/Ship/Camera/Lighting/Motion/Physics/Negative), 3 perde × N faz × 12 sahne haritası, perde dönüşleri, duygusal yay |
| **REFERANS_PAKETI.md** | Karakter portre promptları (ön/profil/tam boy), mekan çapa imajları, kilitlenen seed numaraları, 135 satırlık üretim takip tablosu |
| **SUREKLILIK_LEDGERI.md** | Faz sonu / perde sonu kimlik denetim kayıtları, sapma notları, yeniden üretilen imajlar |
| **PERDE_N/*_FAZ_*.md** | 12 sahne × (IMAGE PROMPT + VIDEO PROMPT), 3 çapa imajı, faz sonu bağlantı notu |
| **MUZIK_VE_SES.md** | Suno/Udio promptu + Google Flow zaman kodlu prompt (864s yay), perde bazlı enstrümantasyon matrisi |

> **Faz dosyası iskeleti birebir 7-9 dk şablonundan alınır:**
> `../yatay_7_9_dk_filmler/kilavuzlar/FAZ_DOSYASI_SABLONU.md`
> Tek değişiklik: başlıkta perde bilgisi (`PERDE II | FAZ 5`) ve
> faz giriş bağlantısında "referans portreye dönüş" notu.

---

## 🛠 ADIM ADIM ÜRETİM İŞ AKIŞI

### ADIM 1 — Süre kararı ve faz sayısı kilidi
Hikaye analiz edilir, süre tablosundan faz sayısı seçilir.
**Faz sayısı bu adımda kilitlenir** — sonradan faz eklemek perde dengesini bozar.

### ADIM 2 — Master İncil (`README.md`)
World Bible, Character Bible, 3 perde haritası, perde dönüş noktaları (2 adet),
sahne haritası. İmza çekimin hangi fazda olduğu burada belirlenir.

### ADIM 3 — Referans Paketi (`REFERANS_PAKETI.md`)
Karakter portresi (3 açı) → mekan master çekimleri (boş) → ışık varyasyonları
→ seed kilitleme. **135 imajlık zincirde bu adım atlanamaz.**

### ADIM 4 — Perde perde üretim
Perde tamamlanmadan sonraki perdeye geçilmez. Her perde sonunda:
kimlik denetimi + `VIDEO_QA_CRITIQUE_PROMPT.md` çalıştırılır.

### ADIM 5 — Müzik ve Ses
864 saniyelik yay. Ambient bed perdeler arası kesintisiz devam eder,
perde dönüşlerinde enstrümantasyon değişir.

---

## 💰 ÜRETİM MALİYETİ TAHMİNİ (Veo 3.1 Fast, 9 fazlık varsayılan)

```
108 video × 8 saniye × ~$0.15/sn (sesli)  =  ~$130  (tek geçiş, sıfır retry)
Gerçekçi senaryo (sahne başına ~3 deneme) =  ~$390 / film
+ 135 imaj üretimi (Midjourney/Imagen/Dzine)

12 fazlık üst sınır: 144 video → ~$520 gerçekçi
```

> **Bütçe dağılımı:** Perde III'e (özellikle DORUK fazına) bütçenin ~%35'i.
> İMZA ÇEKİM için 6-8 varyasyon baştan planlanır.
> Diyalogsuz sahneler sessiz üretilir (~$0.10/sn) — ses ElevenLabs'ten eklenir.

---

## 📺 YAYIN AVANTAJI (bu formatın asıl gerekçesi)

```
8 dakikanın üstündeki videolarda:
  ✓ Mid-roll reklam yerleştirme açılır (gelir ~2-3 kat)
  ✓ İzlenme süresi (watch time) sinyali algoritmada çok daha güçlü
  ✓ Bölüm işaretleri (chapters) kullanılabilir → perde başları = chapter
  ✓ "Kısa film" kategorisinde festival/playlist uygunluğu
```

**Chapter haritası perde/faz yapısından doğrudan çıkar:**
```
0:00  Perde I — [ad]
4:48  Perde II — [ad]
9:36  Perde III — [ad]
```

---

## 📏 DİĞER FORMATLARLA KARŞILAŞTIRMA

| Özellik | 2-4dk | 3-5dk | 7-9dk | **10-20dk** |
|---|---|---|---|---|
| Sahne sayısı | 13 | 24 | 60 | **72-144 (hedef 108)** |
| Klip süresi | 10s | 10s | 8s | **8s** |
| Yapı | Tek dosya | 2 bölüm | 5 faz | **3 perde × 6-12 faz** |
| Dosya sayısı | 1 | 2 | 8 | **13-16** |
| Üretim tekniği | Text-to-video | Text-to-video | Start/End zinciri | **Start/End zinciri** |
| İmaj sayısı | 13 | 24 | 75 | **135** |
| Referans paketi | Sonda | Sonda | Başta | **Başta + faz başı yenileme** |
| Devamlılık denetimi | — | — | Faz sonu QA | **Faz + perde sonu ledger** |
| Anlatı derinliği | Tek katman | Çift katman | 5 katmanlı yay | **3 perde / 9 alt yay** |
| Mid-roll reklam | ✗ | ✗ | ✓ | **✓✓** |

---

## 📚 İLGİLİ KILAVUZLAR

| Kılavuz | Konum | Ne için |
|---|---|---|
| Kesintisiz Video Üretim Tekniği | `../yatay_7_9_dk_filmler/kilavuzlar/` | Start/End frame zinciri (aynen geçerli) |
| Faz Dosyası Şablonu | `../yatay_7_9_dk_filmler/kilavuzlar/` | Sahne prompt şablonları (aynen geçerli) |
| 5 Faz Mimarisi | `../yatay_7_9_dk_filmler/kilavuzlar/` | Faz işlev mantığı — **perde katmanı için uyarlanır** |
| Veo 3.1 Diyalog Kılavuzu | `../kilavuzlar_ve_sistem_dosyalari/` | Tırnak sentaksı, lip-sync, ses katmanları |
| Sahne Devamlılık Kılavuzu | `../kilavuzlar_ve_sistem_dosyalari/` | Karakter çapalama, seed yönetimi |
| Lessons Learned | `../kilavuzlar_ve_sistem_dosyalari/` | Negatif blok kaynağı |
| Sinematografik Teknik Kılavuz | `../kilavuzlar_ve_sistem_dosyalari/` | Kamera sözlüğü, görünmez geçişler |
| Tek Çekim ve Gizli Geçiş | `../kilavuzlar_ve_sistem_dosyalari/` | Klipler arası geçiş tasarımı |

---

## ✅ FORMAT TESLİM CHECKLIST

```
□ Faz sayısı ADIM 1'de kilitlendi (7-12 arası)
□ Perde dağılımı kurallara uygun (Perde II en kısa değil, I en uzun değil)
□ REFERANS_PAKETI.md fazlardan ÖNCE tamamlandı
□ Her faz çapa imajı referans portreden üretildi (önceki fazdan DEĞİL)
□ SUREKLILIK_LEDGERI.md her faz sonunda güncellendi
□ 2 perde dönüşü net yazıldı (eşik + geri dönüşsüzlük)
□ İMZA ÇEKİM tek bir sahneye atandı, 6-8 varyasyon planlandı
□ Faz sonu bağlantı notları zincir halinde kesintisiz
□ Chapter haritası (perde zaman kodları) README'de
□ Müzik yayı toplam süreyle birebir eşit
```

---

## 🎞️ BU FORMATTAKİ FİLMLER

| Film | Faz | Sahne | Sahne süresi | Toplam | Durum |
|---|:--:|:--:|:--:|:--:|---|
| [THE SECOND SHIP](THE_SECOND_SHIP/) | 10 (3-4-3) | 120 | **10s** ⚠️ sapma | 20:00 | Plan + Bible + senaryo + kapak + müzik + referans paketi ✅ · Faz 1 TAM + Faz 2 S13-S20 promptu ✅ · S21-S120 ve üretim ❌ |

```
THE SECOND SHIP dosya düzeni (bu formatın referans örneği):
  00_PLAN.md        faz kilidi, perde dağılımı, gerekçeler   ADIM 1
  README.md         Bible'lar + 120 sahne haritası           ADIM 2
  01_SENARYO.md     10 kısım × 12 sahne anlatı akışı
  KAPAK.md          kapak A/B + motion poster
  MUZIK_VE_SES.md   330 saniyelik beste, 6 pencere
  REFERANS_PAKETI.md   4 master kimlik çapası + Flow kartları  ADIM 3
  PERDE_1_DUSUS/01_FAZ_1_TRANSIT.md   S1-S12 promptları (TAM)  ADIM 4
  PERDE_1_DUSUS/02_FAZ_2_VURULMA.md   S13-S20 promptları       ADIM 4
```
