# 🎬 Yatay 32 Dakika Filmler — 192 Sahne · 16 Bölüm · QA 8 PART + Tam Film

> **Açılış:** 22.09.2026 · sahip kararı. 12-sahne modül merdiveninin ALTINCI
> basamağı: `yatay_2_dk_filmler/` 12 · `yatay_4_dk_filmler/` 24 · `yatay_8_dk_filmler/` 48 ·
> `yatay_16_dk_filmler/` 96 → **bu klasör 192 sahne · 32 dk**.
>
> Yazım, prompt, iskelet, kapılar: 24-sahnelik hatla **BİREBİR AYNI**
> (`KILAVUZ_REHBERI.md` §2.0 iskeleti · §2.9 kartı). **Fark QA'dadır:** on iki mercek
> filme değil, SEKİZ PART MASTERINA koşulur (her part = 2 bölüm dosyası = 24 klip = 4:00,
> tam olarak 24-sahnelik hattın bir filmi ölçeği) **ve buna bir TAM-FİLM koşusu eklenir**
> (16 dk hattının oturmuş tam-film modeli burada da geçerlidir).
>
> Bölüm dosyası sayısı (16) ile QA parçası (8) baştan ayrı tanımlıdır; `rapor_kontrol.py`
> eşlemeyi generic formülle kendisi yapar (`bolum_dosyalari`: 16 dosya / 8 parça → part başına 2 dosya).

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 32:00 = 192 × **tam 10,000 s** = 1920,000 s — SABİT |
| **Oryantasyon** | 16:9 yatay |
| **Toplam sahne** | 192 — hook 192'nin İÇİNDEDİR, ayrı sahne değil |
| **Yazım birimi** | 16 bölüm dosyası × 12 sahne (BOLUM_1 = S000–S011 … BOLUM_16 = S180–S191) |
| **QA birimi** | 8 PART × 24 sahne (PART n = BOLUM_2n−1 + BOLUM_2n) **+ TAM FİLM** |
| **Klip süresi** | ham klip ARAÇTAN ölçülür [D124]; kurguya alınan birim seçilen kare hızında **tam 10 s'e sabitlenir** (24 fps → 240 kare); zaman kodları yeniden HESAPLANMAZ, sapma SPEC A'daki KIRPMA/SABİTLEME satırıyla kapanır |
| **Tek çekim kuralı** | her sahne ayrı tek çekim; sekans içi devam klipleri önceki klibin GERÇEK SON KARESİNDEN başlayabilir (I2V zinciri — imaj promptu yazılmaz)<br>🆕 22.09.2026 · `SAHNE PLANI`'lı filmde (ÇOK KLİPLİ SAHNE) zincir YOK: sahne 2-6 klip, her klibin kendi IMAGE promptu, sahnenin 2.+ klibi `CONTINUOUS ACTION:` taşır (`COK_KLIPLI_SAHNE_KILAVUZU`) |
| **Bölüm sınırı** | 15 dosya sınırı (S011↔S012 … S179↔S180) ardışık çiftin İÇİNDEDİR: 191 çift = 176 bölüm içi + 15 sınır |
| **PART sınırı** | 7 sınır çifti (S023↔S024, S047↔S048, S071↔S072, S095↔S096, S119↔S120, S143↔S144, S167↔S168) — ② DEVAMLILIK hiçbir part masterda yan yana göremez → ELLE KARE |
| **Kurulum iskeleti** | 12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 [ACI_YAYI §3 🕰️ · §4b]; sekans içi devam klipleri ölçek/açı bandından MUAF (aynı harf)<br>🆕 22.09.2026 · `SAHNE PLANI`'lı filmde KÜME yok, muafiyet yok (ardışık aynı kurulum ⑩① BLOCK) · DÖNÜŞ %40 sürer · kapı ㉜ |
| **Viral ara sahne** | süreyle ölçeklenir: 24 sahnede 4 → 192 sahnede 32 |
| **Sahne doluluğu** | `SAHNE_DOLULUGU_KILAVUZU.md`; son 3 s beş sınıftan biri (SONUÇ · TEPKİ · KARAR · BEKLEYİŞ · SÜRDÜRME) |
| **Oran seti** | §2.5 bantlarıyla sınanır; plana yüzde satırı yazılır |

```
SÜRE HESABI
   192 sahne × 10,000 s = 1920,000 s = 32:00
   BOLUM_n  = S(12n−12) … S(12n−1) = 120 s         (16 dosya)
   PART n   = BOLUM_(2n−1) + BOLUM_(2n) = 24 klip = 240 s = 4:00   (8 QA parçası)
     PART 1 = S000–S023 · 0–240 s       PART 2 = S024–S047 · 240–480 s
     PART 3 = S048–S071 · 480–720 s     PART 4 = S072–S095 · 720–960 s
     PART 5 = S096–S119 · 960–1200 s    PART 6 = S120–S143 · 1200–1440 s
     PART 7 = S144–S167 · 1440–1680 s   PART 8 = S168–S191 · 1680–1920 s
   ızgara: sahne başlangıcı(n) = n × 10,000 s   (hook ayrı sahne DEĞİL)
   ⛔ Kurgu kapısı TAM master'a: 192 klip · 1920 s ±0
```

---

## 📁 KLASÖR — 24-sahnelik hatla aynı iskelet

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 16):

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh yatay_32_dk_filmler <FILM_ADI> 192
```

```
yatay_32_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                  altı adım + 00_HIKAYE_ONAYI — bitmeden film yazılmaz (Kart A)
│   └── 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md   192 satır (bir satır = bir KLİP) + 5 kilit klip
├── <FILM>_PLAN.md
├── <FILM>_BOLUM_1.md … _BOLUM_16.md   # 📍 SAHNE nn + ## 🎬 KLİP 1 … 192 (12'şer)
├── <FILM>_KAPAK.md · _MUZIK.md · _YAYIN_PAKETI.md
├── <FILM>_QA_SPEC.md           ⭐ tek dosya — A bloğuna PART GRID (8 satır + FULL) + KIRPMA satırı
├── <FILM>_URETIM_DEFTERI.md    üretim doldurur · §0b DENEME (P-probu) sonuçları burada
└── <FILM>_REFERANS_PAKETI.md   isteğe bağlı (çok varlıklı filmde fiilen zorunlu — §1 tetikleyiciler)
```

🆕 24.09.2026 · **ÇOK KLİPLİ SAHNE bu hattın varsayılanıdır.** Kartın "192 sahne"si
bu rejimde 192 KLİPTİR; sahne sayısı ayrıdır ve hikâyeden çıkar (ilk film
THE_FALSE_EARTH: 192 klip / 50 sahne · sahne 2-6 klip). PLAN'daki `SAHNE PLANI:`
satırı ㉜ kapısını açar; bölüm dosyasında sahne tek `#`, klip `##` ile yazılır ve
sahnenin 2.+ klibi `CONTINUOUS ACTION:` taşır. Son kare zinciri YOKTUR.
⛔ Sahne bölüm dosyası sınırını AŞAMAZ — 12 kliplik dosya 3+4+5 diye bölünür,
böylece PART master'ları sahne ortasından kesilmez.

```
```

🆕 22.09.2026 · **ÖN PLAN:** akıştan önce sahibin tretmanı `<FILM>/00_ON_PLAN/` altında
hazırlanabilir (ilk örnek THE_FALSE_EARTH). Klasörde yalnız `00_ON_PLAN/` varsa betik filmi
onun üstüne açar ve ön planı `00_ANALIZ/00_ON_PLAN/`'a taşır.

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; sayaç kökteki
her girdiyi BİR FİLM sayar.

---

## ⭐ FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM

```
KOŞU
   PART 1-8 masterları (24 klip · 4:00, NİHAİ SESLİ masterdan kesilir)
      → ①-⑫ on iki mercek, her biri TEMİZ oturumda [D110] → 96 rapor
      rubriğin BAŞINA: <FILM>_QA_SPEC.md + TEK SATIR BEYAN [D129]:
        "THIS FILE IS PART n OF 8 — scenes Sxx-Syy — the film's opening/ending is NOT in this file."
      ⛔ Beyansız koşuda rubrik yarım makarayı EKSİK TESLİM sanır.
   TAM FİLM masterı (192 klip · 32:00 · sesli)
      → ④ HİKAYE + ⑫ HOOK maskesiz ("THIS FILE IS THE FULL FILM — 192 scenes")
      → ③ SES — nihai sesin KABULÜ yalnız burada; + POST-DUB replik tablosu (anlaşılırlık · zamanlama)
   ⑬ UYUM tek koşu (üretim defteri üzerinden) — parttan etkilenmez

MAKİNE KAPILARI — part başına
   olcum_kapisi.sh <part master>                      ⑪ · sekiz kez (+ tam master bir kez)
   sahne_kapisi.sh <part master> 10 24                ⑬ · sekiz kez
   rapor_kontrol.py <ham…> --film <klasör> --bolum n/8   ⛔ ZORUNLU — betik 16 dosya / 8 parça
      eşlemesini yapar (PART n = BOLUM_2n−1 + BOLUM_2n); bayraksız koşu ①.9'u yanlış ateşler
   rapor_kontrol.py <ham…> --film <klasör>            TAM-FİLM koşusu — bayraksız, maskesiz

SAYI TAŞIMAYAN KATEGORİLER — ①.11 maskesi
   PART 1 (BAŞ):     ④ Ending · ⑫ Peak Placement · ⑫ Exit & Return
   PART 2-7 (ORTA):  ④ Hook VE Ending · ⑫ Hook Question · Stakes · Peak · Exit (FAZ maskesi)
   PART 8 (SON):     ④ Hook · ⑫ Hook Question · ⑫ Stakes
   Bütün-film dörtlüsü (④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair): part koşularında `—`,
   TAM-FİLM koşusunda SAYI TAŞIR.

PART SINIRI KÖR NOKTASI
   ② DEVAMLILIK 7 sınır çiftini hiçbir part masterda yan yana GÖREMEZ:
   (S023↔S024 · S047↔S048 · S071↔S072 · S095↔S096 · S119↔S120 · S143↔S144 · S167↔S168)
   → yedi çift SPEC B'ye EŞ KADRAJ / sınır satırı olarak yazılır ve ELLE KAREYLE kapanır
     (①.10 göz kapısı kalıbı): iki masterın son/ilk karesi yan yana (`ffmpeg -frames:v 1`).

KAYIT — dokuz satır
   ham:     02_HAM_RAPORLAR/<FILM>/<FILM>_B1_<MERCEK>_HAM.md … _B8_ · <FILM>_FULL_<MERCEK>_HAM.md
   kayıt:   01_FILM_RAPORLARI/<FILM>.md — TEK dosya, "## PART 1" … "## PART 8" · "## TAM FİLM" başlıkları
   tablo:   T1-T12 satırı  **<Film>** B1 … B8  ·  **<Film>** FULL
   matris:  00_INDEX  **<FILM>** (B1) … (B8) · (FULL)   (sayaç parantezi atar)
   betik:   RAPOR_KONTROL/RAPORLAR/<FILM>_B<n>_<tarih>_RAPOR_KONTROL.md · <FILM>_<tarih>_… (FULL)

⛔ Kesme listesi / yeniden sıralama PART raporundan UYGULANMAZ; TAM-FİLM raporundan sahip kararıyla.
⛔ Kurgu kapısı (KURGU_VE_TESLIM §kapı) TAM master'a: 192 klip · 1920 s ±0.
```

---

## 📏 KOMŞU FORMATLARLA KARŞILAŞTIRMA

| Özellik | 48 · 8 dk | 96 · 16 dk | **192 · 32 dk** | 384 · 64 dk |
|---|---|---|---|---|
| Bölüm dosyası | 4 × 12 | 8 × 12 | **16 × 12** | 32 × 12 |
| QA birimi | BÖLÜM (2 yarım) | PART (4 × 24) + TAM FİLM | **PART (8 × 24) + TAM FİLM** | PART (16 × 24) + TAM FİLM |
| Rapor sayısı ①-⑫ | 24 | 48 + 3 (FULL) | **96 + 3 (FULL)** | 192 + 3 (FULL) |
| Kurgu toleransı | ±2 s | ±0 (tam 10 s) | **±0 (tam 10 s)** | ±0 (tam 10 s) |
| Kart | §2.7 | §2.8 | **§2.9** | §2.10 |

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `FILM_QA_RAPORLARI/00_INDEX.md` tek sayaçtır
(`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`). Yeni film `yeni-film` skill'i (Kart A) ile yazılır.
