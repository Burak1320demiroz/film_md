# 🎬 Yatay 16 Dakika Filmler — 96 Sahne · 8 Bölüm · QA 4 PART + Tam Film

> **Açılış:** 19.09.2026 · sahip kararı. 12-sahne modül merdiveninin BEŞİNCİ
> basamağı: `yatay_2_dk_filmler/` 12 · `yatay_4_dk_filmler/` 24 · `yatay_6_dk_filmler/` 36 ·
> `yatay_8_dk_filmler/` 48 → **bu klasör 96 sahne · 16 dk**.
>
> Yazım, prompt, iskelet, kapılar: 24-sahnelik hatla **BİREBİR AYNI**
> (`KILAVUZ_REHBERI.md` §2.0 iskeleti · §2.8 kartı). **Fark QA'dadır:** on iki mercek
> filme değil, DÖRT PART MASTERINA koşulur (her part = 2 bölüm dosyası = 24 klip = 4:00,
> tam olarak 24-sahnelik hattın bir filmi ölçeği) **ve buna bir TAM-FİLM koşusu eklenir**
> (8 dk hattında ⬜ kalan "bütün-film dörtlüsü" sorusunun bu formattaki cevabı).
>
> ⚠️ 8 dk hattının "4 × 12 yazım ↔ 2 yarım QA" sapması burada YOKTUR: bölüm dosyası
> sayısı (8) ile QA parçası (4) baştan ayrı tanımlıdır; `rapor_kontrol.py` eşlemeyi
> kendisi yapar (19.09.2026 · `bolum_dosyalari`).


> 🆕 **30.09.2026 · KLASÖRÜN İKİNCİ FİLMİ: THE_LAST_GATE.** Kartın ilk filmi
> (THE_STOLEN_SKY) üretildi ve 4 PART × 15 mercekle ölçüldü; ikinci film o ölçümün
> dört 🔴'sını doğrudan prompt negatifine bağladı (kapak gövdeden geçiyor · bedensiz
> süzülen eldiven/kask · kütlesiz çarpışma · vurulan figürün ayakta olması).
> ⭐ **Kartın ⬜ kalan iki satırına bu filmden gelen ilk veri:**
> · **"16 dk'da oran seti ölçümü YOK"** → THE_LAST_GATE yüzdeleri YAZDI ama "bant
>   içinde" İDDİA ETMEDİ: katalizör %5,2 · seçim %24,0 · orta nokta %42,7 ·
>   doruk başlangıcı %71,9 · doruk %95,8. Ölçüm TAM-FİLM ④ koşusuna bırakıldı.
> · **"viral ara sahne süreyle ölçeklenir: 96'da 16"** → bu film hedefi YAZMADI.
>   §2.3'ün ölçümü (THE_LAST_TOW 48 klipte 3) süre-ölçekleme iddiasını çürütmüştü;
>   THE_LAST_GATE 8 adayı tek tek ölçecek ve 16/92 yüz taşıyan klibiyle "bağımlı
>   değişken YÜZ" hipotezinin ilk BERRAK VİZÖRLÜ testi olacak.
> ⚠️ **Bu filmde ortaya çıkan yapısal yenilik: KURGU BLOĞU.** Zaman çizgisi 96 blok,
> üretilen klip 92 — ilk dört blok kaynak kliplerden monte edilen özet açılıştır ve
> kendi promptu yoktur (sahibin kapsamlı planı §9 · §16). Kapı ㉜ prompt taşımayan
> klibi atlar; bu ÖLÇÜLDÜ. Prompt sayısı bu rejimde `üretilen klip × 2`dir.

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 16:00 = 96 × **tam 10,000 s** = 960,000 s — SABİT |
| **Oryantasyon** | 16:9 yatay |
| **Toplam sahne** | 96 — hook 96'nın İÇİNDEDİR, ayrı sahne değil |
| **Yazım birimi** | 8 bölüm dosyası × 12 sahne (BOLUM_1 = S00–S11 … BOLUM_8 = S84–S95) |
| **QA birimi** | 4 PART × 24 sahne (PART n = BOLUM_2n−1 + BOLUM_2n) **+ TAM FİLM** |
| **Klip süresi** | ham klip ARAÇTAN ölçülür [D124]; kurguya alınan birim seçilen kare hızında **tam 10 s'e sabitlenir** (24 fps → 240 kare); zaman kodları yeniden HESAPLANMAZ, sapma SPEC A'daki KIRPMA/SABİTLEME satırıyla kapanır |
| **Tek çekim kuralı** | her sahne ayrı tek çekim; sekans içi devam klipleri önceki klibin GERÇEK SON KARESİNDEN başlayabilir (I2V zinciri — imaj promptu yazılmaz) |
| **Bölüm sınırı** | 7 dosya sınırı (S11↔S12 … S83↔S84) ardışık çiftin İÇİNDEDİR: 95 çift = 88 bölüm içi + 7 sınır |
| **PART sınırı** | S23↔S24 · S47↔S48 · S71↔S72 — ② DEVAMLILIK hiçbir part masterda yan yana göremez → ELLE KARE |
| **Kurulum iskeleti** | 12+ sahne kuralı: KÜME ≥2 · DÖNÜŞ ≥%40 [ACI_YAYI §3 🕰️ · §4b]; sekans içi devam klipleri ölçek/açı bandından MUAF (aynı harf) |
| **Viral ara sahne** | süreyle ölçeklenir: 24 sahnede 4 → 96 sahnede 16 |
| **Sahne doluluğu** | `SAHNE_DOLULUGU_KILAVUZU.md`; son 3 s beş sınıftan biri (SONUÇ · TEPKİ · KARAR · BEKLEYİŞ · SÜRDÜRME) — soru "bu süre izleyiciye ne kazandırıyor?" |
| **Oran seti** | §2.5 bantlarıyla sınanır; 16 dk'da ölçüm YOK — ilk filmin TAM-FİLM koşusu ölçer, plana yüzde satırı yazılır |

```
SÜRE HESABI
   96 sahne × 10,000 s = 960,000 s = 16:00
   BOLUM_n  = S(12n−12) … S(12n−1) = 120 s        (8 dosya)
   PART n   = BOLUM_(2n−1) + BOLUM_(2n) = 24 klip = 240 s = 4:00   (4 QA parçası)
     PART 1 = S00–S23 · 0–240 s      PART 2 = S24–S47 · 240–480 s
     PART 3 = S48–S71 · 480–720 s    PART 4 = S72–S95 · 720–960 s
   ızgara: sahne başlangıcı(n) = n × 10,000 s   (hook ayrı sahne DEĞİL)
   ⛔ Kurgu kapısı TAM master'a: 96 klip · 960 s ±0 (8 dk'nın ±2 s toleransı bu formatta YOK —
      "her video tam 10 s" sahip koşuludur; sapma kırpmayla kapanır, zaman kodu kaymaz)
```

---

## 📁 KLASÖR — 24-sahnelik hatla aynı iskelet

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 8):

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh yatay_16_dk_filmler <FILM_ADI> 96
```

```
yatay_16_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                  altı adım + 00_HIKAYE_ONAYI — bitmeden film yazılmaz (Kart A)
│   └── 05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md   96 satır + 5 kilit sahne dosyası
├── <FILM>_PLAN.md
├── <FILM>_BOLUM_1.md … _BOLUM_8.md   ## 🎬 SAHNE 0 … 95 (12'şer)
├── <FILM>_KAPAK.md · _MUZIK.md · _YAYIN_PAKETI.md
├── <FILM>_QA_SPEC.md           ⭐ tek dosya — A bloğuna PART GRID (4 satır + FULL) + KIRPMA satırı
├── <FILM>_URETIM_DEFTERI.md    üretim doldurur · §0b DENEME (P-probu) sonuçları burada
└── <FILM>_REFERANS_PAKETI.md   isteğe bağlı (çok varlıklı filmde fiilen zorunlu — §1 tetikleyiciler)
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; sayaç kökteki
her girdiyi BİR FİLM sayar.

---

## ⭐ FARK — QA BİRİMİ PART (2 bölüm dosyası) + TAM FİLM

```
KOŞU
  PART 1-4 masterları (24 klip · 4:00, NİHAİ SESLİ masterdan kesilir)
     → ①-⑫ on iki mercek, her biri TEMİZ oturumda [D110] → 48 rapor
     rubriğin BAŞINA: <FILM>_QA_SPEC.md + TEK SATIR BEYAN [D129]:
       "THIS FILE IS PART n OF 4 — scenes Sxx-Syy — the film's opening/ending is NOT in this file."
     ⛔ Beyansız koşuda rubrik yarım makarayı EKSİK TESLİM sanır.
  TAM FİLM masterı (96 klip · 16:00 · sesli)
     → ④ HİKAYE + ⑫ HOOK maskesiz ("THIS FILE IS THE FULL FILM — 96 scenes")
     → ③ SES — nihai sesin KABULÜ yalnız burada; + POST-DUB replik tablosu (anlaşılırlık · zamanlama)
     → sahibin dört sorusu SPEC A'ya satır olarak: hedef anlaşılmış mı · orta bölüm uzuyor mu ·
       kayıp etkili mi · final beklentiyi karşılıyor mu — rapor bunları cevaplamak zorunda
  ⑬ UYUM tek koşu (üretim defteri üzerinden) — parttan etkilenmez

MAKİNE KAPILARI — part başına
  olcum_kapisi.sh <part master>                      ⑪ · dört kez (+ tam master bir kez)
  sahne_kapisi.sh <part master> 10 24                ⑬ · dört kez
  rapor_kontrol.py <ham…> --film <klasör> --bolum n/4   ⛔ ZORUNLU — betik 8 dosya / 4 parça
     eşlemesini yapar (PART n = BOLUM_2n−1 + BOLUM_2n); bayraksız koşu ①.9'u yanlış ateşler
  rapor_kontrol.py <ham…> --film <klasör>            TAM-FİLM koşusu — bayraksız, maskesiz

SAYI TAŞIMAYAN KATEGORİLER — ①.11 maskesi
  PART 1 (BAŞ):   ④ Ending · ⑫ Peak Placement · ⑫ Exit & Return
  PART 2-3 (ORTA): ④ Hook VE Ending · ⑫ Hook Question · Stakes · Peak · Exit (FAZ maskesi)
  PART 4 (SON):   ④ Hook · ⑫ Hook Question · ⑫ Stakes
  Bütün-film dörtlüsü (④ Structure · ④ Retention · ⑫ Plateau · ⑨ Rhyme Pair): part koşularında `—`,
  TAM-FİLM koşusunda SAYI TAŞIR. Part ③ SES hücresi: part masterlar sesli masterdan kesilmediyse
  `uygulanmadı`, ortalamaya girmez.

PART SINIRI KÖR NOKTASI
  ② DEVAMLILIK S23↔S24 · S47↔S48 · S71↔S72 çiftlerini hiçbir part masterda yan yana GÖREMEZ.
  → üç çift SPEC B'ye EŞ KADRAJ / sınır satırı olarak yazılır ve ELLE KAREYLE kapanır
    (①.10 göz kapısı kalıbı): iki masterın son/ilk karesi yan yana (`ffmpeg -frames:v 1`).

KAYIT — beş satır
  ham:     02_HAM_RAPORLAR/<FILM>/<FILM>_B1_<MERCEK>_HAM.md … _B4_ · <FILM>_FULL_<MERCEK>_HAM.md
  kayıt:   01_FILM_RAPORLARI/<FILM>.md — TEK dosya, "## PART 1" … "## PART 4" · "## TAM FİLM" başlıkları
  tablo:   T1-T12 satırı  **<Film>** B1 … B4  ·  **<Film>** FULL
  matris:  00_INDEX  **<FILM>** (B1) … (B4) · (FULL)   (sayaç parantezi atar)
  betik:   RAPOR_KONTROL/RAPORLAR/<FILM>_B<n>_<tarih>_RAPOR_KONTROL.md · <FILM>_<tarih>_… (FULL)

⛔ Kesme listesi / yeniden sıralama PART raporundan UYGULANMAZ; TAM-FİLM raporundan sahip kararıyla.
⛔ Kurgu kapısı (KURGU_VE_TESLIM §kapı) TAM master'a: 96 klip · 960 s ±0.
```

---

## 🧪 ÜRETİM SIRASI — bu formatın kendi kuralı (19.09.2026)

96 klip yazılmadan önce **taslak referanslar → zor çekim denemeleri (P-probu) → 16 dk ön kurgu
(animatik)** gelir; kalan promptlar deneme ve animatik sonuçlarına göre yazılır. Deneme
sonuçları `<FILM>_URETIM_DEFTERI.md` §0b'ye; sadeleştirme, sahnenin KORUNACAK BİLGİSİNE dokunmaz.
Tam akış ilk filmin planında: `THE_STOLEN_SKY/00_ANALIZ/00_TODO_GOREV_PLANI.md`.

---

## 📏 KOMŞU FORMATLARLA KARŞILAŞTIRMA

| Özellik | 24 · 4 dk | 36 · 6 dk | 48 · 8 dk | **96 · 16 dk** | 7-20 dk FAZ |
|---|---|---|---|---|---|
| Bölüm dosyası | 2 × 12 | 2 × 18 | 2 × 24 (fiilen 4 × 12) | **8 × 12** | faz başına |
| QA birimi | film | BÖLÜM (2 yarım) | BÖLÜM (2 yarım) | **PART (4 × 24) + TAM FİLM** | FAZ [D185] |
| Rapor sayısı ①-⑫ | 12 | 24 | 24 | **48 + 3 (④ ⑫ ③ FULL)** | faz başına |
| Kurgu toleransı | ±2 s | ±2 s | ±2 s | **±0 (tam 10 s)** | — |
| Kart | §2.3 | §2.6 | §2.7 | **§2.8** | §2.5 |

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `FILM_QA_RAPORLARI/00_INDEX.md` tek sayaçtır
(`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`). Yeni film `yeni-film` skill'i (Kart A) ile yazılır.

> **İlk film:** THE_STOLEN_SKY (ÇALINAN GÖKYÜZÜ) — hikâyeyi sahip yazdı (96 klip, 24 sekans,
> 8 bölüm); depo hikâyeyi üretmedi, TAŞIDI (THE_FALLING_WORLD kalıbı). 19.09.2026 itibarıyla
> klasör açılmadı; görev planı ve 96 klip hazırlık dosyası `ilk_deneme/` altında bekliyor.
