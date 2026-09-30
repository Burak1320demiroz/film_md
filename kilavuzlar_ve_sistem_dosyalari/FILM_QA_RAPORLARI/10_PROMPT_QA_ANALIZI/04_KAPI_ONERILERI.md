# 🚪 KAPI ÖNERİLERİ — metin hazır, uygulama sahibin

> ⛔ **Bu dosya `prompt_kontrol.py`'yi DEĞİŞTİRMEZ.** Kapı metnini, regex'i ve
> **ölçülmüş** yanlış-pozitif sayısını hazırlar. Betiğe girmesi ayrı bir iştir.
>
> Ölçüm: `python3 ../../RAPOR_KONTROL/prompt_hata_analizi.py --regex-dene "<desen>"`
> → **1733 sahne · 87 film** (bütün depo prompt korpusu, 31 film değil).

---

## ⚠️ ÖLÇÜM KAPSAMI — okumadan önce

```
Bu dosyadaki sayılar SAHNE BLOĞU üzerinde ölçüldü: '## 🎬 SAHNE n' başlığından
sonraki her şey — Türkçe künye satırları (KURULUM · SÜRE · VURUŞ · IN FRAME)
DAHİL. prompt_kontrol.py ise PROMPT GÖVDESİNİ ölçer (kod çitinin içi).

⛔ Sonuç: buradaki oranlar SIRALAMA için geçerlidir, EŞİK için değil.
   Bir kapı betiğe girmeden önce aynı regex prompt_kontrol.py'nin kendi
   gövde ayıklamasıyla YENİDEN ölçülmelidir.
```

Bu uyarı gereksiz değil: `\b[A-Z]{3,}\b` (büyük harfli jeton) denemesi **%100
isabet** verdi — çünkü künye satırları ve `NEGATIVE:` / `AUDIO:` çapaları zaten
büyük harf. Kapsam ayıklanmadan bu sınıf ölçülemez.

---

## 🚪 K1 · JETON SIZINTISI — ⚠️ FIX, BLOCK DEĞİL

**Hangi sınıf:** `03_` §🅑6 — promptun kendi kelimesi kadraja yazı olarak basılıyor
(THE_PAYLOAD `PHASE 1` 🔴 · `EVA` 🔴 · THE_ROSE_COAT `rose` 🔴 ×2).

```
desen:  \b(PHASE|SEQ|REF|LOC|PART|SET)\s*[0-9]*\b        (harf DUYARLI)
ölçüm:  140 isabet / 1733 sahne (%8,1) · 15 film
```

**⛔ DÜRÜST KAYIT — bu kapı ayırt etmiyor.** İsabet alan 15 filmin başında
THE_SKYLIGHT (27) ve THE_FROST_LINE (25) var; **ikisi de jeton sızıntısı bulgusu
ALMADI.** FROST_LINE `Wear state: PHASE 2` cümlesini 25 promptta taşıyor ve
kadraja hiçbir şey basılmadı. THE_PAYLOAD'da ise aynı jeton göğse basıldı.

```
Ayıran şeyin ne olduğu BİLİNMİYOR. Hipotez (sınanmamış): FROST_LINE jetonu
bir CÜMLENİN İÇİNE gömüyor ("Wear state: PHASE 2 — red dust on both knees"),
THE_PAYLOAD ise SATIR BAŞINDA tek başına bırakıyor ("PHASE 1  only the boots…").
```

**Öneri:** kapı **FIX** seviyesinde açılır ve mesajı bir SORU sorar:
> `⚠️ K1 · '<jeton>' satır başında tek başına duruyor — motor bunu giysiye/ekrana`
> `basabilir [THE_PAYLOAD S01 · S07]. Jetonu bir cümlenin içine göm ya da kaldır.`

⛔ BLOCK olamaz: iki filmde dört 🔴, on beş filmde sıfır. Kanıt BLOCK'a yetmiyor.

**Sınanacak:** yukarıdaki hipotezi ölçmek için satır-başı varyantı:
`^[ \t]*[A-Z]{3,}\s*[0-9]*\b` — prompt gövdesi ayıklandıktan sonra ölçülmeli.

---

## 🚪 K2 · EL KADRAJDA, TEMAS SINIRI CÜMLESİ YOK — ⭐ en güçlü aday

**Hangi sınıf:** `03_` §🅑2 — 17 film kısmi · 9 film hiç · 20'den fazla 🔴.

```
desen:  (?s)\A(?=.*(?i:\b(glove|gloved|finger|fingers)\b))
            (?!.*(?i:no merging|no phasing|clear boundary|no extra fingers))
ölçüm:  493 isabet / 1733 sahne (%28,4) · 62 film
```

**Okuma:** deponun **her üç sahnesinden biri** eldiven/parmak taşıyor ve temas
cümlesi taşımıyor. Bu oran yüksek görünüyor ama sınıfın bulgu ağırlığı da öyle:
temas, 🔴 üreten en kalabalık iki sınıftan biri.

**Öneri:** **FIX** seviyesinde aç, mesaj tek satır:
> `⚠️ K2 · kadrajda el/eldiven var, temas sınırı cümlesi yok. Negatif çekirdeğe`
> `ekle: "Hand-to-surface contact keeps a clear boundary, no merging, no phasing,`
> `no extra fingers." [FROST_LINE 5 🔴 · ROSE_COAT 4 🔴 · BORROWED_WEIGHT 3 🔴]`

⚠️ **Ama kapının kendi sınırını da yazar:** `03_` §🅐2 ölçtü — cümle VARKEN de
füzyon oluyor (COUNTED_TURN 7 🔴 · DRY_ANCHOR 6 🔴, cümle 22/25 ve 14/14).
Kapı cümleyi garanti eder, **sonucu garanti etmez**; mesajın son satırı bunu söyler.

---

## 🚪 K3 · VİDEO PROMPTUNDA `AUDIO:` SATIRI YOK

**Hangi sınıf:** `03_` §🅑1 — 12 film hiç · ses yasası 24 filmde yok.

```
desen:  (?s)\A(?=.*(?i:VİDEO PROMPT|MOTION:|TIMELINE:))(?!.*^AUDIO:)
ölçüm:  955 isabet / 1733 sahne (%55,1) · 63 film
```

**Öneri:** **FIX**. Eşik yüksek çünkü deponun yarısından çoğu eski rejim;
yeni rejim klasörlerinde (`00_HIKAYE_ONAYI.md` var) **BLOCK** yapılabilir —
o alt küme ayrıca ölçülmeli.

⚠️ **Sınırı yazılı:** `03_` §🅐1 — SUSMAYAN'ın `AUDIO:` satırı 96/96'da ve
`no exterior sound at all` diyor; yine de 4 🔴 vakumda ses. Kapı satırı
garanti eder, **sesi garanti etmez**. Vakumda ses KURGU kapısıdır.

---

## 🚪 K4 · ORTAM NE ADIYLA NE SAYISIYLA YAZILMAMIŞ

**Hangi sınıf:** `03_` §🅑4 · §🅑4a · §🅑4b — 14 film sayısız · 6 film adsız ·
6 filmde iki rejim aynı kadrajda.

```
desen:  (?s)\A(?!.*(?i:zero gravity|micro-?gravity|zero-?g\b|vacuum|
                       thin atmosphere|low gravity|gravity is|gravity of))
ölçüm:  1140 isabet / 1733 sahne (%65,8) · 78 film
```

**⛔ Bu haliyle kapı olamaz** — %66 çok yüksek ve iç mekân sahnelerinde ortam
adı yazmak gereksiz. **İki parçaya bölünmeli:**

```
K4a  DIŞ sahnede (prompt 'exterior|outside|surface|sky' taşıyorsa)
     ortam adı YOKSA → FIX
K4b  Ortam adı VARSA ama SAYI (0,30 g · m/s²) yoksa → FIX
     ⭐ gerekçe ölçülü: tarifle 2 🔴 (BENI_HATIRLAMA), sayıyla 1 🔴 (FALLING_WORLD)
```

İkisinin de eşiği **dış sahne ayıklandıktan sonra** yeniden ölçülmeli.

---

## 🚪 K5 · EFOR CÜMLESİNDE SAYI YOK — ⛔ BU KAPSAMDA ÖLÇÜLEMEDİ

**Hangi sınıf:** `03_` §🅑5 — ⑧ EFOR 99 bulgu yazdı; `prompt_kontrol.py`
⑳ kapısı cümlenin VARLIĞINI sayıyor, ŞİDDETİNİ ölçmüyor (SUSMAYAN 0 BLOCK aldı,
⑧ dokuz bulgu yazdı).

```
desen denendi: (?s)\A(?=.*(?i:hauls|pulls|drags|lifts|heaves|cranks))(?!.*\d)
ölçüm:         0 isabet  ⛔ ANLAMSIZ
sebep:         sahne bloğu Türkçe künyede zaten rakam taşıyor (SÜRE: 10 s)
```

**Yapılacak:** ölçüm `prompt_kontrol.py`'nin gövde ayıklamasıyla tekrarlanmalı;
aranan şey "efor cümlesinin AYNI cümlesinde bir sayı" olmalı, promptta herhangi
bir sayı değil. Önerilen kilit biçimi:
`the lever moves 4 cm in the first second and 1 cm in the last`.

---

## 📋 ÖZET — dört kapı, hiçbiri BLOCK

| kapı | sınıf | ölçüm | öneri | kendi sınırı yazılı mı |
|---|---|:--:|:--:|:--:|
| K1 jeton sızıntısı | 🅑6 | %8,1 · 15 film | ⚠️ FIX | ✅ ayırt etmiyor, hipotez sınanmamış |
| K2 temas cümlesi | 🅑2 | %28,4 · 62 film | ⚠️ FIX | ✅ cümle varken de oluyor |
| K3 `AUDIO:` satırı | 🅑1 | %55,1 · 63 film | ⚠️ FIX (yeni rejimde BLOCK?) | ✅ satır varken de oluyor |
| K4 ortam adı/sayısı | 🅑4 | %65,8 · 78 film | ⛔ bölünmeli, yeniden ölç | ✅ |
| K5 efor sayısı | 🅑5 | ⛔ ölçülemedi | — | ✅ |

⭐ **Hiçbiri BLOCK önerilmiyor** ve bu bilinçli: bu deponun kayıtlı üç vakası
(`from behind` · `lever` · `through the suit`) kural doğru yazıldığı hâlde
üretimi durdurdu. Yeni kapı **önce FIX olarak yaşar**, bir sonraki filmde
ölçülür, sonra sertleşir.

⛔ **Commit ve uygulama sahibindir.**
