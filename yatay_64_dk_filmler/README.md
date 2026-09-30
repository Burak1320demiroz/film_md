# 🎬 Yatay 64 Dakika Filmler — 384 Sahne · 32 Bölüm · QA 16 PART + Tam Film

> **Açılış:** 22.09.2026 · sahip kararı. 12-sahne modül merdiveninin YEDİNCİ
> basamağı: `yatay_2_dk_filmler/` 12 · `yatay_4_dk_filmler/` 24 · `yatay_8_dk_filmler/` 48 ·
> `yatay_16_dk_filmler/` 96 · `yatay_32_dk_filmler/` 192 → **bu klasör 384 sahne · 64 dk**.
>
> Yazım, prompt, iskelet, kapılar: 24-sahnelik hatla **BİREBİR AYNI**
> (`KILAVUZ_REHBERI.md` §2.0 iskeleti · §2.10 kartı). **Fark QA'dadır:** on iki mercek
> filme değil, ON ALTI PART MASTERINA koşulur (her part = 2 bölüm dosyası = 24 klip = 4:00,
> tam olarak 24-sahnelik hattın bir filmi ölçeği) **ve buna bir TAM-FİLM koşusu eklenir**
> (16 dk ve 32 dk hatlarının oturmuş tam-film modeli burada da geçerlidir).
>
> Bölüm dosyası sayısı (32) ile QA parçası (16) baştan ayrı tanımlıdır; `rapor_kontrol.py`
> eşlemeyi generic formülle kendisi yapar (`bolum_dosyalari`: 32 dosya / 16 parça → part başına 2 dosya).

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 64:00 = 384 × **tam 10,000 s** = 3840,000 s — SABİT |
| **Oryantasyon** | 16:9 yatay |
| **Toplam sahne** | 384 — hook 384'ün İÇİNDEDİR, ayrı sahne değil |
| **Yazım birimi** | 32 bölüm dosyası × 12 sahne (BOLUM_1 = S000–S011 … BOLUM_32 = S372–S383) |
| **QA birimi** | 16 PART × 24 sahne (PART n = BOLUM_2n−1 + BOLUM_2n) **+ TAM FİLM** |
| **Klip süresi** | ham klip ARAÇTAN ölçülür [D124]; kurguya alınan birim seçilen kare hızında **tam 10 s'e sabitlenir** (24 fps → 240 kare); zaman kodları yeniden HESAPLANMAZ, sapma SPEC A'daki KIRPMA/SABİTLEME satırıyla kapanır |
| **Tek çekim kuralı** | her sahne ayrı tek çekim; sekans içi devam klipleri önceki klibin GERÇEK SON KARESİNDEN başlayabilir (I2V zinciri — imaj promptu yazılmaz) |
| **Bölüm sınırı** | 31 dosya sınırı (S011↔S012 … S371↔S372) ardışık çiftin İÇİNDEDİR: 383 çift = 352 bölüm içi + 31 sınır |
| **PART sınırı** | 15 sınır çifti (S023↔S024, S047↔S048 … S359↔S360) — ② DEVAMLILIK hiçbir part masterda yan yana göremez → ELLE KARE |
| **Kurulum iskeleti** | 12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 [ACI_YAYI §3 🕰️ · §4b]; sekans içi devam klipleri ölçek/açı bandından MUAF (aynı harf) |
| **Viral ara sahne** | süreyle ölçeklenir: 24 sahnede 4 → 384 sahnede 64 |
| **Sahne doluluğu** | `SAHNE_DOLULUGU_KILAVUZU.md`; son 3 s beş sınıftan biri (SONUÇ · TEPKİ · KARAR · BEKLEYİŞ · SÜRDÜRME) |
| **Oran seti** | §2.5 bantlarıyla sınanır; plana yüzde satırı yazılır |

```
SÜRE HESABI
   384 sahne × 10,000 s = 3840,000 s = 64:00
   BOLUM_n  = S(12n−12) … S(12n−1) = 120 s         (32 dosya)
   PART n   = BOLUM_(2n−1) + BOLUM_(2n) = 24 klip = 240 s = 4:00   (16 QA parçası)
     PART 1  = S000–S023 · 0–240 s        PART 2  = S024–S047 · 240–480 s
     PART 3  = S048–S071 · 480–720 s      PART 4  = S072–S095 · 720–960 s
     PART 5  = S096–S119 · 960–1200 s     PART 6  = S120–S143 · 1200–1440 s
     PART 7  = S144–S167 · 1440–1680 s    PART 8  = S168–S191 · 1680–1920 s
     PART 9  = S192–S215 · 1920–2160 s    PART 10 = S216–S239 · 2160–2400 s
     PART 11 = S240–S263 · 2400–2640 s    PART 12 = S264–S287 · 2640–2880 s
     PART 13 = S288–S311 · 2880–3120 s    PART 14 = S312–S335 · 3120–3360 s
     PART 15 = S336–S359 · 3360–3600 s    PART 16 = S360–S383 · 3600–3840 s
   ızgara: sahne başlangıcı(n) = n × 10,000 s   (hook ayrı sahne DEĞİL)
   ⛔ Kurgu kapısı TAM master'a: 384 klip · 3840 s ±0
```

---

## 📁 KLASÖR — 24-sahnelik hatla aynı iskelet

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 32):

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh yatay_64_dk_filmler <FILM_ADI> 384
```

```
yatay_64_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                  altı adım + 00_HIKAYE_ONAYI — bitmeden film yazılmaz (Kart A)
│   └── 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md   384 satır + 5 kilit sahne dosyası
├── <FILM>_PLAN.md
├── <FILM>_BOLUM_1.md … _BOLUM_32.md   ## 🎬 SAHNE 0 … 383 (12'şer)
├── <FILM>_KAPAK.md · _MUZIK.md · _YAYIN_PAKETI.md
├── <FILM>_QA_SPEC.md           ⭐ tek dosya — A bloğuna PART GRID (16 satır + FULL) + KIRPMA satırı
├── <FILM>_URETIM_DEFTERI.md    üretim doldurur · §0b DENEME (P-probu) sonuçları burada
└── <FILM>_REFERANS_PAKETI.md   isteğe bağlı (çok varlıklı filmde fiilen zorunlu — §1 tetikleyiciler)
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; sayaç kökteki
her girdiyi BİR FİLM sayar.

---

## ⭐ FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM

```
KOŞU
   PART 1-16 masterları (24 klip · 4:00, NİHAİ SESLİ masterdan kesilir)
      → ①-⑫ on iki mercek, her biri TEMİZ oturumda [D110] → 192 rapor
      rubriğin BAŞINA: <FILM>_QA_SPEC.md + TEK SATIR BEYAN [D129]:
        "THIS FILE IS PART n OF 16 — scenes Sxx-Syy — the film's opening/ending is NOT in this file."
      ⛔ Beyansız koşuda rubrik yarım makarayı EKSİK TESLİM sanır.
   TAM FİLM masterı (384 klip · 64:00 · sesli)
      → ④ HİKAYE + ⑫ HOOK maskesiz ("THIS FILE IS THE FULL FILM — 384 scenes")
      → ③ SES — nihai sesin KABULÜ yalnız burada; + POST-DUB replik tablosu (anlaşılırlık · zamanlama)
   ⑬ UYUM tek koşu (üretim defteri üzerinden) — parttan etkilenmez

MAKİNE KAPILARI — part başına
   olcum_kapisi.sh <part master>                       ⑪ · on altı kez (+ tam master bir kez)
   sahne_kapisi.sh <part master> 10 24                 ⑬ · on altı kez
   rapor_kontrol.py <ham…> --film <klasör> --bolum n/16  ⛔ ZORUNLU — betik 32 dosya / 16 parça
      eşlemesini yapar (PART n = BOLUM_2n−1 + BOLUM_2n); bayraksız koşu ①.9'u yanlış ateşler
   rapor_kontrol.py <ham…> --film <klasör>             TAM-FİLM koşusu — bayraksız, maskesiz

SAYI TAŞIMAYAN KATEGORİLER — ①.11 maskesi
   PART 1 (BAŞ):      ④ Ending · ⑫ Peak Placement · ⑫ Exit & Return
   PART 2-15 (ORTA):  ④ Hook VE Ending · ⑫ Hook Question · Stakes · Peak · Exit (FAZ maskesi)
   PART 16 (SON):     ④ Hook · ⑫ Hook Question · ⑫ Stakes
   Bütün-film dörtlüsü (④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair): part koşularında `—`,
   TAM-FİLM koşusunda SAYI TAŞIR.

PART SINIRI KÖR NOKTASI
   ② DEVAMLILIK 15 sınır çiftini hiçbir part masterda yan yana GÖREMEZ:
   (S023↔S024 · S047↔S048 · S071↔S072 · S095↔S096 · S119↔S120 · S143↔S144 · S167↔S168 ·
    S191↔S192 · S215↔S216 · S239↔S240 · S263↔S264 · S287↔S288 · S311↔S312 · S335↔S336 · S359↔S360)
   → on beş çift SPEC B'ye EŞ KADRAJ / sınır satırı olarak yazılır ve ELLE KAREYLE kapanır
     (①.10 göz kapısı kalıbı): iki masterın son/ilk karesi yan yana (`ffmpeg -frames:v 1`).

KAYIT — on yedi satır
   ham:     02_HAM_RAPORLAR/<FILM>/<FILM>_B1_<MERCEK>_HAM.md … _B16_ · <FILM>_FULL_<MERCEK>_HAM.md
   kayıt:   01_FILM_RAPORLARI/<FILM>.md — TEK dosya, "## PART 1" … "## PART 16" · "## TAM FİLM" başlıkları
   tablo:   T1-T12 satırı  **<Film>** B1 … B16  ·  **<Film>** FULL
   matris:  00_INDEX  **<FILM>** (B1) … (B16) · (FULL)   (sayaç parantezi atar)
   betik:   RAPOR_KONTROL/RAPORLAR/<FILM>_B<n>_<tarih>_RAPOR_KONTROL.md · <FILM>_<tarih>_… (FULL)

⛔ Kesme listesi / yeniden sıralama PART raporundan UYGULANMAZ; TAM-FİLM raporundan sahip kararıyla.
⛔ Kurgu kapısı (KURGU_VE_TESLIM §kapı) TAM master'a: 384 klip · 3840 s ±0.
```

---

## 📏 KOMŞU FORMATLARLA KARŞILAŞTIRMA

| Özellik | 48 · 8 dk | 96 · 16 dk | 192 · 32 dk | **384 · 64 dk** |
|---|---|---|---|---|
| Bölüm dosyası | 4 × 12 | 8 × 12 | 16 × 12 | **32 × 12** |
| QA birimi | BÖLÜM (2 yarım) | PART (4 × 24) + TAM FİLM | PART (8 × 24) + TAM FİLM | **PART (16 × 24) + TAM FİLM** |
| Rapor sayısı ①-⑫ | 24 | 48 + 3 (FULL) | 96 + 3 (FULL) | **192 + 3 (FULL)** |
| Kurgu toleransı | ±2 s | ±0 (tam 10 s) | ±0 (tam 10 s) | **±0 (tam 10 s)** |
| Kart | §2.7 | §2.8 | §2.9 | **§2.10** |

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `FILM_QA_RAPORLARI/00_INDEX.md` tek sayaçtır
(`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`). Yeni film `yeni-film` skill'i (Kart A) ile yazılır.
