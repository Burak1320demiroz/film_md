# 🎬 Yatay 8 Dakika Filmler — 48 Sahne · 2 Bölüm

> **Açılış:** 13.09.2026 · sahip kararı. 12-sahne modül merdiveninin DÖRDÜNCÜ
> basamağı: `yatay_2_dk_filmler/` 12 sahne · 2 dk → `yatay_4_dk_filmler/`
> 24 sahne · 4 dk → `yatay_6_dk_filmler/` 36 sahne · 6 dk → **bu klasör 48 sahne · 8 dk**.
>
> (13.09.2026 · ilk iki basamak aynı gün yeniden adlandırıldı: eski adları
> `yatay_2_4_dk_filmler_uzay` ve `yatay_3_5_dk_filmler` — belgelerdeki "2-4 dk" /
> "3-5 dk" bu formatların eski adlarıdır.)
>
> Yazım, prompt, iskelet, kapılar: 24-sahnelik hatla **BİREBİR AYNI**
> (`KILAVUZ_REHBERI.md` §2.0 iskeleti · §2.7 kartı). **Tek fark QA'dadır:**
> on iki mercek filme değil, İKİ YARIM MASTERA koşulur — aşağıda.
>
> ⚠️ **8 DAKİKADA İKİ HAT VAR — bu klasör MODÜL hattıdır.** Faz mimarisinin
> kısa ucu (5 faz · start/end zinciri · THE_SLOW_STONE 48 × 10 s = 8:00)
> `yatay_10_20_dk_filmler/`'dedir ve oraya KALIR (eski film taşınmaz). Ayrım:
> burada perde/faz yok, 12-sahne modülü ve 2 bölüm dosyası var. Bandın
> §2.5'ten geri çekilip çekilmeyeceği ⬜ sahip kararı (Kart H2 ④: bandın
> adresi de bir atıftır, varsayılmaz).

---

## 📐 FORMAT KURALLARI

| Özellik | Değer |
|---|---|
| **Süre** | 8:00 (48 × 10 s) |
| **Oryantasyon** | 16:9 yatay |
| **Toplam sahne** | 48 — hook 48'in İÇİNDEDİR, ayrı sahne değil |
| **Yapı** | 2 bölüm × 24 sahne (BOLUM_1 = ilk 24 · BOLUM_2 = son 24) — her bölüm 24-sahnelik hattın bir filmi büyüklüğünde |
| **Klip süresi** | 10 s / sahne — ⛔ plan yazılmadan ARAÇTAN ölçülür [D124] |
| **Tek çekim kuralı** | Her sahne ayrı tek çekim video |
| **Bölüm sınırı** | S23 ↔ S24 (betik damgası S00'dan sayar) — sınır da ARDIŞIK BİR ÇİFTTİR (≥1 ölçek + ≥45°) |
| **Kurulum iskeleti** | 12+ sahne kuralı geçerli: KÜME ≥2 · DÖNÜŞ ≥%40 [ACI_YAYI §3 🕰️ · §4b] |
| **Viral ara sahne** | süreyle ölçeklenir: 24 sahnede 4 → 48 sahnede 8 (SENARYO_VE_VIRAL §2.2 yüzde bantları) |
| **Sahne doluluğu** | 48 birimin her biri 10 s DOLU yazılır: kilit fiili süreç · TIMELINE ≤3 satır, son satır sürdürme · ölü sahne 5 soru — `SAHNE_DOLULUGU_KILAVUZU.md` (15.09.2026 · TUR 19; bu formatın tetiklediği tur) |

```
SÜRE HESABI
   48 sahne × 10 s = 480 s = 8:00
   BÖLÜM 1 = S00-S23 = 240 s = 4:00      BÖLÜM 2 = S24-S47 = 240 s = 4:00
   ızgara: sahne başlangıcı(n) = (n) × 10 s   (hook ayrı sahne DEĞİL — HARD_DOCK kalıbı)
   ⛔ 9 s hook kırpması isteniyorsa plana KIRPMA TABLOSU yazılır [D100];
      yazılmazsa kurgu kırpmaz ve bütün zaman kodları kayar.
   ⚠️ 8 dakikada tema-tatmin kuralı ağırlaşır (TEMA_MUHENDISLIGI süre-tatmin
      kuralı) ve ORAN SETİ §2.5'in ölçülmüş bantlarıyla sınanır (katalizör ·
      feda · doruk başlangıcı) — plana yüzde satırı yazılır.
```

---

## 📁 KLASÖR — 24-sahnelik hatla aynı iskelet

Klasör ELLE açılmaz, betikle açılır (bölüm sayısı formattan gelir = 2):

```bash
bash kilavuzlar_ve_sistem_dosyalari/film_klasoru_ac.sh yatay_8_dk_filmler <FILM_ADI> 48
```

```
yatay_8_dk_filmler/<FILM_ADI>/
├── 00_ANALIZ/                  altı adım — bitmeden film yazılmaz (Kart A)
├── <FILM>_PLAN.md
├── <FILM>_BOLUM_1.md           ## 🎬 SAHNE 0 … 23
├── <FILM>_BOLUM_2.md           ## 🎬 SAHNE 24 … 47
├── <FILM>_KAPAK.md · _MUZIK.md · _YAYIN_PAKETI.md
├── <FILM>_QA_SPEC.md           ⭐ tek dosya KALIR — A bloğuna BÖLÜM IZGARASI eklenir (aşağıda)
├── <FILM>_URETIM_DEFTERI.md
└── <FILM>_REFERANS_PAKETI.md   isteğe bağlı (08.09.2026)
```

⛔ Bu klasörün köküne `.md` bırakma — yalnız bu README durur; sayaç kökteki
her girdiyi BİR FİLM sayar.

---

## ⭐ TEK FARK — QA BİRİMİ BÖLÜMDÜR

> 24-sahnelik hatta on iki mercek TEK master'a koşulur. Burada film yine TEK
> master olarak kurgulanır ve yayınlanır; ama QA için **iki yarım master**
> ihraç edilir ve **on iki mercek her yarıya AYRI koşulur** → 24 rapor.
> Yarım master TAM OLARAK 24-sahnelik hattın bir filmi ölçeğindedir (4:00 ·
> 24 klip — THE_HARD_DOCK'un on iki mercekle ölçüldüğü ölçek). ⑬ UYUM sahne
> sahne koşar, bölümden etkilenmez (üretim defteri tektir).

```
KOŞU
  BÖLÜM 1 masterı (S00-S23 · 4:00)  →  ①-⑫ on iki mercek, her biri TEMİZ oturumda [D110]
  BÖLÜM 2 masterı (S24-S47 · 4:00)  →  ①-⑫ on iki mercek, her biri TEMİZ oturumda
  Her koşuda rubriğin BAŞINA: <FILM>_QA_SPEC.md + TEK SATIR BEYAN [D129]:
     "THIS FILE IS PART 1 OF 2 — scenes S00-S23 — the film's ending is NOT in this file."
     "THIS FILE IS PART 2 OF 2 — scenes S24-S47 — the film's opening is NOT in this file."
  ⛔ Beyansız koşuda rubrik yarım makarayı EKSİK TESLİM sanır (D188'in yarım-film hâli).

MAKİNE KAPILARI — bölüm başına
  olcum_kapisi.sh <yarım master>                    ⑪ · iki kez
  sahne_kapisi.sh <yarım master> 10 24              ⑬ · iki kez (prompt sayısı = bölümün klip sayısı)
  rapor_kontrol.py <ham…> --film <klasör> --bolum 1/2   ⛔ ZORUNLU — bayraksız koşu
     ①.9 teslim kapısını YANLIŞ ateşler (plan 48 sayar, makara 24).
     --bolum: teslim kapısı yalnız <FILM>_BOLUM_n.md'yi sayar · ①.11 BÖLÜM
     KAPISI aşağıdaki hücreleri `—` yapar, ortalamayı yeniden hesaplar.

SAYI TAŞIMAYAN KATEGORİLER — D185'in yarım-film uzantısı
  BÖLÜM 1'de (filmin SONU dosyada yok):  ④ Ending · ⑫ Peak Placement · ⑫ Exit & Return
  BÖLÜM 2'de (filmin BAŞI dosyada yok):  ④ Hook · ⑫ Hook Question · ⑫ Stakes by the First Share Moment
  HİÇBİRİNDE (bütün filmi ister):        ④ Structure & Pacing · ④ Retention Risk · ⑫ Plateau · ⑨ Rhyme Pair
  ⬜ AÇIK (sahip kararı bekliyor): bütün-film dörtlüsü bu hatta hiçbir koşuda sayı
     taşımaz. Seçenekler: (a) yalnız ④ ve ⑫ için tam master'a ÜÇÜNCÜ koşu ·
     (b) elle kare denetimi (göz kapısı kalıbı) · (c) hücre `—` kalır.
     Karar gelene kadar (c) geçerlidir; dört hücre ortalamaya GİRMEZ.

BÖLÜM SINIRI KÖR NOKTASI
  ② DEVAMLILIK S23↔S24 çiftini hiçbir yarım masterda yan yana GÖREMEZ.
  → Sınır çifti SPEC B'ye EŞ KADRAJ / sınır satırı olarak yazılır ve ELLE
    KAREYLE kapanır (①.10 göz kapısı kalıbı): iki masterın son/ilk karesi
    yan yana (`ffmpeg -frames:v 1`) — gövde · dünya · ışık takvimi · sayaç.

KAYIT — üç yerde de bölüm etiketi taşınır
  ham:     02_HAM_RAPORLAR/<FILM>/<FILM>_B1_<MERCEK>_HAM.md  ·  <FILM>_B2_<MERCEK>_HAM.md
  kayıt:   01_FILM_RAPORLARI/<FILM>.md — TEK dosya, "## BÖLÜM 1" / "## BÖLÜM 2" başlıkları
  tablo:   T1-T12 satırı  **<Film>** B1  ·  **<Film>** B2   (iki satır; --t-tablo bunu yazar)
  matris:  00_INDEX  **<FILM>** (B1)  ·  **<FILM>** (B2)     (iki satır; sayaç parantezi atar,
           klasör adıyla eşleşir · tamlık paydası bölüm başına /4)
  betik:   RAPOR_KONTROL/RAPORLAR/<FILM>_B1_<tarih>_RAPOR_KONTROL.md · _B2_

⛔ Kesme listesi / yeniden sıralama / REMOVE reçetesi bölüm raporundan UYGULANMAZ —
   kesme filmin kurgusudur, bölüm raporunun yetkisi değildir (D185 ile aynı kural).
⛔ Kurgu kapısı (KURGU_VE_TESLIM §kapı) TAM master'a koşulur: klip sayısı = 48,
   süre = 480 s ±2 s. Yarım masterlar QA aracıdır, teslim değil.
```

---

## 📏 KOMŞU FORMATLARLA KARŞILAŞTIRMA

| Özellik | 24 sahne · 4 dk | 36 sahne · 6 dk | **48 sahne · 8 dk** | 7-20 dk FAZ hattı |
|---|---|---|---|---|
| Klasör | `yatay_4_dk_filmler/` (eski adı 3-5 dk) | `yatay_6_dk_filmler/` | **bu klasör** | `yatay_10_20_dk_filmler/` |
| Bölüm dosyası | 2 × 12 | 2 × 18 | **2 × 24** | faz başına alt klasör |
| Klip | 10 s | 10 s | **10 s** | 8 s (öneri) / 10 s (SLOW_STONE) |
| QA birimi | film (tek master) | BÖLÜM | **BÖLÜM (2 yarım master × 12 mercek)** | FAZ — kendi rubriği [D185] |
| Rapor sayısı (①-⑫) | 12 | 24 | **24** | faz başına |
| Kart | §2.3 | §2.6 | **§2.7** | §2.5 |

---

## 🎞️ FİLMLER

Film listesi burada tutulmaz — `FILM_QA_RAPORLARI/00_INDEX.md` tek sayaçtır
(`bash kilavuzlar_ve_sistem_dosyalari/sayac.sh`). Bu klasörde henüz film yok;
ilk film `yeni-film` skill'i (Kart A) ile yazılır.
