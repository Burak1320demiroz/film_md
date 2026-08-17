# 🎬 Yatay 7-9 Dakika Filmler — Veo Üretim Formatı

> **5 Faz Mimarisi | 8 Saniyelik Sahne Standardı | Start/End Frame Zincirleme**
> Bu format, Veo 3.1'in native 8 saniyelik üretim penceresi üzerine kurulmuştur.

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 7-9 dakika (420-540 saniye) |
| **Oryantasyon** | 16:9 yatay (widescreen) |
| **Faz sayısı** | **5 faz (sabit)** |
| **Faz başına sahne** | 11-13 sahne (hedef: 12) |
| **Toplam sahne** | 55-65 sahne (hedef: 60) |
| **Klip süresi** | **8 saniye / sahne** (Veo native — extend gerekmez) |
| **Tek çekim kuralı** | Her sahne ayrı, kesintisiz tek çekim |
| **Görsel üretim** | Start/End Frame zinciri (bkz. `kilavuzlar/`) |

### ⏱️ Süre Matematiği

```
ALT SINIR:  5 faz × 11 sahne × 8s = 440s = 7 dk 20 sn  ✓
HEDEF:      5 faz × 12 sahne × 8s = 480s = 8 dk 00 sn  ✓
ÜST SINIR:  5 faz × 13 sahne × 8s = 520s = 8 dk 40 sn  ✓

Post-prodüksiyon geçişleri (J-cut, ses köprüsü) ile ~9 dakikaya kadar çıkar.
9 dakika ÜST SINIR — kesinlikle aşılmaz.
```

---

## 🎯 NEDEN 8 SANİYE — VE NEDEN BU FORMAT DAHA KOLAY

2-4 dk filmlerde sahne standardı 10 saniyeydi; Veo 3.1 tek üretimde 4s/6s/8s veriyor, yani her sahne için `Extend` gerekiyordu. Bu formatta o sorun yok:

```
2-4 dk film:  10s sahne → 8s üret + 2s extend  → 2 işlem / sahne, dikiş riski
7-9 dk film:   8s sahne → 8s üret              → 1 işlem / sahne, dikiş yok
```

**8 saniye ayrıca 7-9 dk kılavuzundaki "yavaş tempo, uzun plan" kuralını doğrudan destekler** — izleyici sahneyi kesintisiz izler, jump cut hissi oluşmaz.

---

## 🔗 START/END FRAME ZİNCİRİ — TEMEL ÜRETİM MANTIĞI

Bu format text-to-video değil, **image-to-video zinciri** kullanır. Detay: `kilavuzlar/KESINTISIZ_VIDEO_URETIM_TEKNIGI.md`

```
Formül:  x. İmaj  →  (x+1). İmaj  =  x. Video

Video 1 (0-8s):    Start = İmaj 1   End = İmaj 2
Video 2 (8-16s):   Start = İmaj 2   End = İmaj 3
Video 3 (16-24s):  Start = İmaj 3   End = İmaj 4
```

### Sekans Kavramı (zincir kırılma noktaları)

Bir faz baştan sona tek zincir DEĞİLDİR. Mekan/zaman sıçraması olan yerde zincir kırılır ve yeni bir çapa (anchor) imajı üretilir.

```
FAZ = 3 SEKANS × 4 SAHNE (hedef 12 sahne)

Sekans içi:      zincirleme (N sahne → N+1 imaj)
Sekanslar arası: zincir kırılır, yeni çapa imajı
```

**İmaj sayısı hesabı (12 sahneli faz):**
```
3 sekans × (4 video + 1 kapanış imajı) = 3 × 5 = 15 imaj / faz
5 faz × 15 imaj = 75 imaj / film
5 faz × 12 sahne = 60 video / film
```

> ⚠️ Bu formatın en büyük maliyeti **imaj üretimi**, video değil. 75 imajın karakter tutarlılığı sabit seed + referans portre ile kilitlenmeli (bkz. `SAHNE_DEVAMLILIK_KILAVUZU.md` §6).

---

## 📁 KLASÖR VE DOSYA DÜZENİ

Her film için filmin adıyla bir klasör açılır:

```text
yatay_7_9_dk_filmler/
└── FILM_ADI/
    ├── README.md                      <-- Master İncil + 5 faz sahne haritası
    ├── 01_FAZ_1_KURULUS.md            <-- Faz 1 senaryo & prompt dokümanı
    ├── 02_FAZ_2_DERINLESME.md         <-- Faz 2
    ├── 03_FAZ_3_DONUM.md              <-- Faz 3
    ├── 04_FAZ_4_ZIRVE.md              <-- Faz 4
    ├── 05_FAZ_5_COZULME.md            <-- Faz 5
    ├── MUZIK_VE_SES.md                <-- 8 dakikalık müzik yayı + ses tasarımı
    └── REFERANS_PAKETI.md             <-- Karakter/mekan çapa imajları, seed kayıtları
```

### Dosya içerikleri

| Dosya | İçerik |
|---|---|
| **README.md** | Film kapağı promptu, tüm Bible'lar (World/Character/Ship/Camera/Lighting/Motion/Physics/Negative), 5 faz × 12 sahne haritası, duygusal yay tablosu |
| **01-05_FAZ_*.md** | 12 sahne × (IMAGE PROMPT + VIDEO PROMPT), sekans kırılma noktaları işaretli, faz sonu bağlantı notu |
| **MUZIK_VE_SES.md** | Suno/Udio promptu + Google Flow zaman kodlu prompt (480 saniyelik yay), faz bazlı enstrümantasyon matrisi |
| **REFERANS_PAKETI.md** | Karakter portre promptları (ön/profil/tam boy), mekan çapa imajları, kilitlenen seed numaraları, üretim takip tablosu |

---

## 🛠 ADIM ADIM ÜRETİM İŞ AKIŞI

### ADIM 1 — Master İncil (`README.md`)
Hikaye analiz edilir; World Bible, Character Bible ve 5 fazlık sahne haritası kesinleştirilir. **Sahne sayısı bu adımda kilitlenir** (55/60/65).

### ADIM 2 — Referans Paketi (`REFERANS_PAKETI.md`)
> ⚠️ 2-4 dk formatından **en kritik farkı budur**: referanslar EN SONDA değil, **EN BAŞTA** hazırlanır.
>
> 75 imajlık bir zincirde karakter/mekan çapası önceden kilitlenmezse 3. fazda yüz kayar ve geri dönüş yoktur.

Sırayla: karakter portresi (3 açı) → mekan master çekimleri (boş, karaktersiz) → ışık varyasyonları → seed kilitleme.

### ADIM 3 — Fazların Sırayla Üretimi
Her faz dosyası hazırlanır. Sahne şablonu:
- **IMAGE PROMPT:** SCENE / ENVIRONMENT / SUBJECT / CAMERA / LIGHTING / PHYSICS / NEGATIVE (tamamı self-contained — Bible'a atıf YOK)
- **VIDEO PROMPT:** Start/End frame notu + 8 saniyelik hareket + diyalog (tırnak sentaksı) + ses katmanları + negatif blok

### ADIM 4 — Müzik ve Ses (`MUZIK_VE_SES.md`)
480 saniyelik tek yay olarak veya 5 faz parçası olarak üretilir. İşitsel yatak (ambient bed) fazlar arası kesintisiz devam eder.

### ADIM 5 — Kalite Kontrol (`kilavuzlar/kalite_kontrol/`)
Kurgulanmış film **3 ayrı geçişle** eleştirilir — tek promptla değil.
480 saniyelik bir filme 11 kategorilik tekil-klip QA promptu uygulandığında model
ilk 90 saniyeden sonra çözünürlük kaybediyor. Geçişler: **1) Teknik Bütünlük ·
2) Devamlılık & Karakter · 3) Anlatı, Ritim & Ses.** Üç rapor birleştirilip
`LESSONS_LEARNED.md`'ye ders olarak işlenir.

---

## 💰 ÜRETİM MALİYETİ TAHMİNİ (Veo 3.1 Fast)

```
60 video × 8 saniye × ~$0.15/sn (sesli)  =  ~$72  (tek geçiş, sıfır retry)
Gerçekçi senaryo (sahne başına ~3 deneme) =  ~$216 / film
+ 75 imaj üretimi (Midjourney/Imagen/Dzine)
```

> Sessiz üretim (~$0.10/sn) + ElevenLabs hibrit akışı maliyeti düşürebilir,
> ancak Veo'nun native ses senkronu (10ms) kaybolur. Diyalogsuz sahnelerde sessiz üret.

---

## 📏 DİĞER FORMATLARLA KARŞILAŞTIRMA

| Özellik | 2-4dk | 3-5dk | **7-9dk** |
|---|---|---|---|
| Sahne sayısı | 13 | 24 | **60** |
| Klip süresi | 10s | 10s | **8s** |
| Yapı | Tek dosya | 2 bölüm | **5 faz** |
| Dosya sayısı | 1 | 2 | **8** |
| Üretim tekniği | Text-to-video | Text-to-video | **Start/End frame zinciri** |
| İmaj sayısı | 13 | 24 | **75** |
| Referans paketi | Sonda | Sonda | **BAŞTA (zorunlu)** |
| Anlatı derinliği | Tek katman | Çift katman | **5 katmanlı dramatik yay** |

---

## 📚 İLGİLİ KILAVUZLAR

| Kılavuz | Konum | Ne için |
|---|---|---|
| Kesintisiz Video Üretim Tekniği | `kilavuzlar/` | Start/End frame zinciri |
| 5 Faz Mimarisi | `kilavuzlar/` | Dramatik yay ve sahne dağılımı |
| Faz Dosyası Şablonu | `kilavuzlar/` | Sahne prompt şablonları |
| **3 Geçişli QA Sistemi** | `kilavuzlar/kalite_kontrol/` | **Bitmiş filmin eleştirisi — 3 ayrı prompt** |
| Veo 3.1 Diyalog Kılavuzu | `../kilavuzlar_ve_sistem_dosyalari/` | Tırnak sentaksı, lip-sync, ses katmanları |
| Sahne Devamlılık Kılavuzu | `../kilavuzlar_ve_sistem_dosyalari/` | Karakter çapalama, seed yönetimi |
| Lessons Learned | `../kilavuzlar_ve_sistem_dosyalari/` | 33 ders — negatif blok kaynağı |
| Sinematografik Teknik Kılavuz | `../kilavuzlar_ve_sistem_dosyalari/` | Kamera sözlüğü, görünmez geçişler |
