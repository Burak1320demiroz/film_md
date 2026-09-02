# 🔗 SAHNE DEVAMLILIK VE KARAKTER TUTARLILIK KILAVUZU

> AI film promptları hazırlarken sahne devamlılığı, karakter tutarlılığı
> ve profesyonel iş akışı için pratik referans kılavuzu.
> Araştırma kaynağı: "YZ Sinematografisinde Senaryo Akışı ve Sahne Devamlılığı" (2026)

---

## 1. 🎯 AI MODEL SEÇİM KARARI

> ⛔ **TARİHSEL — KARAR GİRDİSİ DEĞİL (21.08.2026):** Hat %100 Veo
> (Flow) üzerinde üretiyor; bu bölümdeki Kling/Runway/Luma/Firefly
> kıyası araştırma arşividir. Tablodaki yüzdeler (%94, %89, %84, %38)
> kaynağı depoda olmayan ölçümlerdir — alıntılanmaz. Veo dışına
> çıkılacaksa önce güncel ölçüm yapılır.

Hangi sahne için hangi model daha uygun?

| Senaryo Tipi | Önerilen Model | Neden |
|---|---|---|
| Fotogerçekçi hareket, yoğun aksiyon | **Kling 3.0** | 3D uzamsal-zamansal dikkat, %94 komut sadakati, referanssız karakter tutarlılığı |
| Uzun plan, sesli sahne akışı | **Google Veo 3.1** | Native ses sentezi, "Ingredients" modüler mimarisi, 1dk+ kesintisiz |
| Profesyonel kurgu, renk düzeltme | **Runway Gen-4.5** | 4K upscale, renk derecelendirme, referans tabanlı %84 tutarlılık |
| Görüntüden-videoya (I2V) | **Luma Ray 2/3.14** | Keyframe tabanlı, kamera momentumu koruma |
| Marka güvenli ticari iş | **Adobe Firefly** | Lisanslı veri seti, telif koruması |

### Karakter Tutarlılığı Mekanizmaları

```
KLİNG 3.0:  Referanssız (native) tutarlılık. %89 yüz devamlılığı
            10 ardışık üretim boyunca. Voice ID ile ses+yüz eşleşmesi.
            → En iyi: Çok sahneli filmler, ardışık klip üretimi.

VEO 3.1:    "Ingredients" ile sahne bileşenlerini ayrı üretip birleştirme.
            Kamera hareketini matematiksel hesaplama.
            → En iyi: Karmaşık blokaj, sahne başlangıç/bitiş kontrolü.

RUNWAY 4.5: "Gen-4 References" ile kullanıcı referans görseli yükleme.
            Gen-3'e göre %38 görsel tutarlılık hatası azalması.
            → En iyi: Önceden üretilmiş karakter görseli olan projeler.

LUMA RAY:   Anahtar kare (keyframe) tabanlı doğrusal bağlantı.
            → En iyi: Midjourney/Recraft ile üretilmiş başlangıç karesinden video.
```

---

## 2. ✏️ PROMPT MÜHENDİSLİĞİ — DİLSEL ÇAPALAMA

### 2.1 Altın Kural: Kelimesi Kelimesine Tutarlılık

> AI modelleri eşanlamlı kelimeleri bile farklı tensör vektörlerine atar.
> "Koyu kahve saç" ve "dark brown hair" farklı sonuçlar üretir.

```
KARAKTER ÇAPALAMA KURALI:
Karakterin fiziksel tanımı projede BİR KEZ yazılır ve tüm sahnelerde
HİÇBİR KELİME DEĞİŞTİRİLMEDEN kopyala-yapıştır olarak kullanılır.

✅ DOĞRU: Her sahnede aynı karakter bloğu:
   "31-year-old woman, warm olive-tan skin, visible pores,
    dark brown chin-length bob, navy-blue EVA suit..."

⛔ MİLLİYET YAZILMAZ — 01.09.2026 DÜZELTMESİ.
   Bu örnek 31.08'e kadar "31-year-old TURKISH woman" yazıyordu ve
   §7'nin DOĞRULANMIŞ red kuralıyla çelişiyordu ("Israeli-American"
   → üretim reddi, LOW POWER). Örnek kopyalandı: üç filmin canlı
   promptlarında milliyet ifadesi bulundu (09_URETIM_RED_DEFTERI §3).
   Çapa milliyetten değil FİZİKSEL TANIMDAN gelir — ve fiziksel tanım
   zaten daha iyi çapadır (model milliyeti çizemez, ten tonunu çizer).
   → prompt_kontrol.py ⑯ bunu artık BLOCK olarak yakalar.

❌ YANLIŞ: Sahneden sahneye kelime değişikliği:
   Sahne 1: "olive-skinned woman with short dark hair"
   Sahne 2: "tan-skinned female explorer with brown bob"
   → Model bunları FARKLI KİŞİLER olarak algılayabilir.
```

### 2.2 Zayıf vs. Güçlü Prompt Karşılaştırması

```
❌ ZAYIF (halüsinasyon riski yüksek):
"Astronot bir koridorda yürüyor."

✅ GÜÇLÜ (çapalanmış):
"A 31-year-old woman in a navy-blue EVA suit walks slowly
through a 5-meter-wide curved alien corridor made of dark metallic-
green alloy. Her helmet headlamp casts a single narrow cone of cool
white light into the darkness ahead. The camera follows her at waist
height from behind in a slow tracking shot."
```

### 2.3 Sahne Promptu İskelet Yapısı

Her sahne promptu şu yapıyı takip etmeli:

```
1. FORMAT + SÜRE: "Photorealistic cinematic video. 16:9. 10 seconds."
2. MEKAN TANIMI: Sahnenin geçtiği yerin detaylı fiziksel tanımı
3. KARAKTER BLOĞU: Kopyala-yapıştır karakter bible'dan (değiştirme!)
4. AKSİYON: Karakter ne yapıyor (spesifik, zamanlı)
5. KAMERA: Hareket tipi, lens, açı (sinematik terminoloji)
6. IŞIK: Kaynak, yön, renk sıcaklığı, kontrast
7. FİZİK: Yerçekimi, toz, su, saç davranışı
8. NEGATİF: Olmaması gerekenler
```

---

## 3. 🏗️ SAHNE TEMELİ İŞ AKIŞI (Scene Foundation Workflow)

> En güçlü devamlılık tekniği: Önce mekan, sonra karakter.

### 4 Aşamalı Protokol

```
AŞAMA 1 — TEMEL GEOMETRİ (Boş Mekan Üretimi)
┌─────────────────────────────────────────────────┐
│ Karakter OLMADAN sahnenin boş mekan master       │
│ çekimini üret. Sadece mimari + ışık + doku.      │
│ → "Empty curved alien corridor, dark metallic-   │
│    green walls, no characters, no creatures..."   │
└─────────────────────────────────────────────────┘
              ↓
AŞAMA 2 — ÇOKLU PERSPEKTİF (Aynı mekan, farklı açılar)
┌─────────────────────────────────────────────────┐
│ Aynı boş mekan üzerinden farklı kamera açıları  │
│ ve lens uzunlukları ile varyasyonlar üret.       │
│ → Geniş açı (24mm), orta (35mm), yakın (50mm)   │
└─────────────────────────────────────────────────┘
              ↓
AŞAMA 3 — ZAMAN/IŞIK SİMÜLASYONU
┌─────────────────────────────────────────────────┐
│ Aynı mimari iskelet, farklı ışık koşulları:     │
│ → Headlamp only / Planet light through window / │
│   Photonic Memory glow active / Total darkness   │
└─────────────────────────────────────────────────┘
              ↓
AŞAMA 4 — KARAKTER ENJEKSİYONU
┌─────────────────────────────────────────────────┐
│ Mekan kilitlendikten sonra, karakter sabit seed  │
│ ve görsel referanslarla mekanın içine yerleştirilir│
│ → Image-to-Video pipeline: mekan görseli + prompt │
└─────────────────────────────────────────────────┘
```

### Bu Tekniğin Çözdüğü Sorun

```
SORUN: Karakter her hareket ettiğinde arka plan değişiyor
       (duvar rengi, mobilya pozisyonu, pencere ışığı kayıyor)
       → LESSONS_LEARNED Ders 6: Çevre Morph

ÇÖZÜM: Mekan geometrisi ve ışık haritası ÖNCEDEN üretilip
       kilitlendiğinde, karakter eklenmesi arka planı etkilemez.
```

---

## 4. 🎬 SİNEMATİK GRAMER — PROMPT TERMİNOLOJİSİ

### 4.1 Çekim Ölçeği Hiyerarşisi

Sahneler arası geçişlerde bu sıra takip edilmeli:

```
ESTABLISHING → WIDE → MEDIUM → CLOSE-UP → EXTREME CLOSE-UP

1. Establishing Shot (Genel Çekim):
   "Wide establishing shot, 24mm lens"
   → İzleyiciyi sahnenin coğrafyasına yerleştirir

2. Medium Shot (Orta Çekim):
   "Medium shot, 35mm lens, waist-up framing"
   → Karakterin eylemini tanıtır

3. Close-Up (Yakın Çekim):
   "Close-up through visor, 85mm lens, shallow DOF"
   → Karakterin içsel duygusunu aktarır

BİZİM SERİMİZ İÇİN: Her film genellikle
Establishing (Sahne 0-1) → Medium (Sahne 2-7) → Close-up (Sahne 8-9)
→ Wide pullback (Sahne 10-final) şeklinde ilerliyor.
```

### 4.2 Diyalog Sahneleri İçin (Gelecek filmler)

```
OMUZ ÜSTÜ: "Over-the-shoulder shot, foreground character
            slightly out of focus, background character sharp"

ÇEKİM-KARŞI ÇEKİM: "Shot-reverse-shot pattern, matching
                      eyeline at 15 degrees off camera axis"

→ Bu terimleri prompt'a yazmak, AI'nin sahneyi rastgele
  açılardan değil, sinematik kurallara göre üretmesini sağlar.
```

---

## 5. 🔧 POST-PRODÜKSİYON İŞ AKIŞI

### 5.1 Hibrit Pipeline (AI + Geleneksel)

```
AI ÜRETİM (Ham malzeme)
    │
    ├─→ Rotoskop / Maskeleme
    │   (Karakter arka plandan ayrılır, gerekirse farklı
    │    render'lardan en iyi parçalar birleştirilir)
    │
    ├─→ Renk Eşleştirme (Color Match)
    │   (DaVinci Resolve — farklı AI render'ların renk/ışık
    │    tonları tek potada eritilir)
    │
    ├─→ Ses Tasarımı
    │   (Ortam sesi + müzik + ayak sesleri katmanlanır)
    │   → J-Cut: Yeni sahnenin sesi, önceki sahnenin
    │     son 2 saniyesinde kısık başlar
    │
    └─→ Final Export
```

### 5.2 Renk Devamlılığı Checklist

```
□ Tüm sahneler aynı renk sıcaklığı bandında mı?
□ Cilt tonu sahneden sahneye kayıyor mu?
□ Gölge yoğunluğu tutarlı mı?
□ Öne çıkan renk (bioluminesan mavi, amber gezegen ışığı)
  aynı HEX/HSL değerlerinde mi?
□ DaVinci Resolve'da "Color Match" uygulandı mı?
```

### 5.3 Ses Devamlılığı — En Güçlü Kurgusal Yapıştırıcı

```
İŞİTSEL YATAK (Ambient Bed) KURALI:
Sahneler arası geçişlerde ortam sesi KESİNTİSİZ devam etmeli.
Aynı hışırtılı rüzgar, aynı metalik oda tonu, aynı uzak
makine hırıltısı — bu ses, parçalanmış dijital görselleri
tek bir fiziksel evrene bağlayan kancadır.

→ Görsel hatalar tolere edilir eğer ses tutarlıysa.
→ Ses kopukluğu, mükemmel görselleri bile yıkar.
```

---

## 6. 🎲 SEED VE REFERANS YÖNETİMİ

### 6.1 Sabit Tohum (Fixed Seed) Stratejisi

```
ADIM 1: İstenen karakter estetiğini bul (birkaç deneme)
ADIM 2: O üretimin seed numarasını kaydet ve kilitle
ADIM 3: Sonraki tüm sahnelerde aynı seed'i kullan

→ Aynı seed = aynı gürültü kalıbı = aynı yüz gradyanı
→ Piksel düzeyinde devamlılık
```

### 6.2 Referans Görsel Klasör Yapısı

```
proje_adi/
├── referanslar/
│   ├── karakter/
│   │   ├── yuz_onden.png
│   │   ├── yuz_profil.png
│   │   └── tam_vucut.png
│   ├── mekan/
│   │   ├── koridor_genis.png
│   │   ├── kontrol_odasi.png
│   │   └── pencere_gorunumu.png
│   └── isik/
│       ├── headlamp_only.png
│       ├── planet_light.png
│       └── photonic_memory.png
├── sahne_01/
│   ├── image_prompt.txt
│   ├── video_prompt.txt
│   ├── render_v1.mp4
│   ├── render_v2.mp4  ← seed: 42891
│   └── SELECTED.mp4   ← en iyi render
└── sahne_02/
    └── ...
```

---

## 7. 🧠 FELSEFİ YAKLAŞIM — KUSURLARI KUCAKLAMAK

### Paul Trillo Manifestosu (Picture This 2025)

```
"Pek çok insan yapay zekayı yanlış kullanıyor.
 Geleneksel sinematik gerçekliği birebir taklit etme saplantısı,
 yaratıcı bir ölü noktaya ve devasa bir yozlaşmaya yol açtı."

PRENSIP: AI'dan Arri kamera optik gerçekliği BEKLEME.
         AI'nın kendine özgü rüya benzeri, parçalanmış,
         sürreal estetiğini bir anlatı aracı olarak KULLAN.
```

### Bizim Serimize Uygulaması

```
AI KUSURLARI KATEGORILERI:

1. KABUL EDİLEMEZ KUSURLAR (her zaman düzelt):
   - Yüz morph / ekstra parmak / karakter klonu
   - Fizik ihlalleri (kayma, süzülme, clipping)
   - Kamera kesmeleri (tek çekim kuralı ihlali)
   - Metin belirmesi

2. TOLERESEDİLEBİLİR KUSURLAR (duruma göre):
   - Arka plan mikro-detay kayması (eğer ana aksiyon güçlüyse)
   - Hafif renk tonu sapması (post-prod'da düzeltilebilir)
   - Doku hafifçe yumuşaması (texture pass ile çözülebilir)

3. SANATSAL FIRSAT KUSURLARI (kucaklanabilir):
   - Beklenmedik ışık kırılmaları
   - Sürreal doku geçişleri (Annihilation Shimmer estetiği)
   - Rüya benzeri hareket bulanıklığı
   → Bunlar kasıtlı "avant-garde" estetiğine dönüştürülebilir
```

---

## 8. 📋 HIZLI REFERANS — HER SAHNE ÜRETİMİNDE CHECKLIST

### Üretim Öncesi (Pre-Production)

```
□ Karakter bloğu kelimesi kelimesine aynı mı? (Sahne 1'den kopyala)
□ Mekan tanımı önceki sahnelerle tutarlı mı?
□ Işık kaynağı açıkça belirtilmiş mi? (motivasyonlu ışık)
□ Kamera hareketi sinematik terminolojiyle yazılmış mı?
□ Fizik kuralları dahil mi? (yerçekimi, toz, saç)
□ Negatif blok eklenmiş mi?
□ LESSONS_LEARNED direktifleri eklenmiş mi?
□ CINEMATIC QUALITY DIRECTIVES eklenmiş mi?
```

### Üretim Sırası (Production)

```
□ Seed numarası kaydedildi mi?
□ Referans görseller yüklendi mi? (Runway/ComfyUI)
□ En az 3 varyasyon üretildi mi?
□ En iyi render SELECTED olarak işaretlendi mi?
```

### Üretim Sonrası (Post-Production)

```
□ Renk eşleştirme yapıldı mı? (önceki sahneyle karşılaştır)
□ Ses katmanı eklendi mi? (ortam sesi + müzik)
□ J-Cut geçişler uygulandı mı?
□ QA Critique çalıştırıldı mı? (1_KARE_QA_CRITIQUE_PROMPT.md)
□ LESSONS_LEARNED'a yeni hata eklenmesi gerekiyor mu?
```

---

## 📊 MEVCUT KILAVUZLARLA İLİŞKİ

| Bu Kılavuz (Devamlılık) | İlişkili Dosya | Bağlantı |
|---|---|---|
| Karakter Çapalama | Her filmin Character Bible'ı | Kelimesi kelimesine kopyala |
| Mekan Kilitleme | Her filmin World Bible'ı | Scene Foundation Workflow |
| AI Model Seçimi | Film türüne göre karar | Bölüm 1 tablosu |
| Prompt Terminolojisi | SINEMATOGRAFIK_TEKNIK_KILAVUZ.md | Kamera hareketleri sözlüğü |
| Coğrafya / Ekran Yönü | UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md | Kuşbakışı harita + SPATIAL LOCK; §3 workflow'un coğrafya boyutu |
| Hata Tespiti | LESSONS_LEARNED.md | QA sonrası ders ekleme |
| Kalite Kontrolü | 1_KARE_QA_CRITIQUE_PROMPT.md | Her render sonrası çalıştır |
| Ses Tasarımı | Post-prodüksiyon | J-Cut, ambient bed |
