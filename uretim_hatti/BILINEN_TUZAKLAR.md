# ⚠️ BİLİNEN TUZAKLAR — yeni hattın tek zorunlu okuması

> **Ne zaman okunur:** her filmde faz 1 (hikâye) ve faz 5 (üretim) öncesi.
> **Bir maddenin buraya girme ölçütü:** kayıtlı gerçek vaka + bilinen sonuç. Sonucu bilinmeyen
> madde `HİPOTEZ` etiketi taşır. Her satırın kaynağı yazılıdır; ayrıntı oradadır.
> **Bu liste kural kapısı DEĞİLDİR** — regex ile denetlenmez, yazarken akılda tutulur.
> Yeni madde yalnız sahibin kararıyla eklenir (AGENTS.md §1 ④).

Kaynak kısaltmaları:
`RED` = `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` (satır no) ·
`SINIF` = `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/10_PROMPT_QA_ANALIZI/03_PROMPT_HATA_SINIFLARI.md`

---

## A · ÜRETİM REDDİ — model "yapamam" dediğinde

| Tuzak | Vaka | Ne işe yaradı | Durum |
|---|---|---|---|
| Şiddet/ölüm kelimeleri — `dead · body · corpse · zombie · decay · skeletal · gore · blood · wounds` — **olumsuz blokta "no blood" diye yazılsa bile** | SLOW STONE S4 · LAST SPAN S8-S9 | Kelime hiç yazılmaz; malzeme tarif edilir ("mineralin içine mühürlenmiş, tamamen hareketsiz yüz") | ✅ SLOW STONE geçti · LAST SPAN sonucu kayıtsız (RED 8, 9, 11) |
| Milliyet ifadesi — `Israeli-American`, `Turkish woman` | LOW POWER | Yalnız fiziksel tarif | ✅ geçti (RED 12) |
| Bedenden bir şeyin ÇIKARILMASI eylemi (kask çıkarma) | COLD BURN S28 | Eylem değişti: kasklar baştan rafta, kimse bir şey çıkarmıyor | ✅ geçti (RED 3) |
| Kompozisyon reddi — kelimeler temiz, kadraj şüpheli (yan yana iki ön kol + tepeden makro + yüzsüz) | YERCEKIMI S8 | Kelime değiştirmek **yetmedi**; kadraj değişmeliydi | ⛔ sahne iptal (RED 13) |
| Yön başlığı prompt içinde — `LIP-SYNC REQUIRED` · `THE SPEAKER IS ON CAMERA` + kesin yaş + yara izi | RISING SNOW S2 | Başlıklar ve kimlik kilidi kaldırıldı | ✅ geçti (RED 10) |
| Uzun olumsuz blok + `Exactly 0 human figures` (insansız sahne) | COLD BURN S8 | Olumsuz blok tek pozitif `Style:` satırına indi | ✅ geçti, tek vaka (RED 2) |
| İki promptu tek girdiye yapıştırmak | çok film | Her çekim ayrı girdi | ✅ (RED 14) |
| Prompt ~4.300 karakteri aşınca Veo hata veriyor | LOW POWER S5, S11 | Kısalt | ✅ doğrulanmış (`KILAVUZ_REHBERI.md` §7) |
| Tek kişide üst üste kimlik tarifi (kesin boy + ten + saç + yaş + yüz izi) → "ünlü kişi" reddi | SINKING STAKE (OMNI) | Önerilen: kimlik yığınını sök, yaş/ten/saç gövdeden çıkar | `HİPOTEZ` — sınanmadı (RED 15) |

```
⭐ Kelime reddi kelimeyle çözülür (her seferinde çözüldü). Kompozisyon reddi kelimeyle ÇÖZÜLMEZ —
   kadraj ya da eylem değişir. İkisini karıştırmak deponun ölçülmüş boşa emeğidir.
⭐ Aynı oturumda HİÇ geçen deneme yoksa (THIRD DUNE 5/0 · RING LIGHT 3/0) sorun prompt değil üretim
   tarafıdır — üçüncü kez yeniden yazmadan önce tek, temiz, basit bir deneme gönder.
⭐ Red geldiği GÜN not et: mesajın birebir metni · hangi araç/model · üretim ilerleyip sonda mı düştü.
   Bu üçü sonradan hatırlanamaz (dosya oluşmaz, meta veri yoktur).
```

---

## B · EKRANDA ÇIKAN HATALAR — sıklık sırası ve kapanma yeri

**Ölçüm (05.10.2026):** `python3 uretim_hatti/araclar/ham_rapor_say.py` → 70 film klasörü,
540 🔴 satırı. Satır sayar, tekil bulgu değil; raporları bir yapay zekâ yazdı. Sıra yön gösterir.

| Sıra | Hata türü | 🔴 satır | Kapanma yeri | Kanıt |
|:--:|---|:--:|---|---|
| 1 | El-nesne kaynaşması / içinden geçme (parmak tokaya erir, el kola gömülür) | 92 | **KADRAJ + KURGU.** Temas anı gösterilmez; öncesi ve sonrası çekilir, an kesmeyle atlanır. Ya da temas kadraj dışında kalır | Temas cümlesi 22/25 promptta yazılıyken 7 🔴 (COUNTED_TURN) · 14/14'te 6 🔴 (DRY_ANCHOR) — SINIF 🅐2 |
| 2 | İstenmeyen yazı / harf / rakam (konsolda "SUIT RELEASE", vizörde HUD, metalde seri no) | 67 | **TASARIM + PROMPT KELİMESİ.** Okunacak ekran kadraja girmez ya da ekran yazısız tasarlanır (ışık çubuğu, dolu yuva). Aynı promptta hem ekran hem "yazı yok" duramaz | SINIF 🅑7 · 🅑6 (bkz. §C) |
| 3 | Ortama aykırı ses (vakumda motor, patlama) | 51 | **KURGU.** Model sesi atılır, ses kurguda kurulur | Ses satırı tam yazılıyken 4 🔴 (SUSMAYAN) = yazılmamışken 4 🔴 (KRONOS) — SINIF 🅐1 |
| 4 | Duman / toz / buhar / sıvı ortama aykırı | 46 | **TASARIM.** Vakumda toz/buhar çıkaran eylem filmin taşıyıcı anı yapılmaz; gerekiyorsa kısa tutulur ve kesmeyle sınırlanır | SINIF 🅑9 · `HİPOTEZ`: kesmeyle kısaltmanın etkisi ölçülmedi |
| 5 | Kask / kıyafet / ekipman kayması (kask kaybolur, çanta düşüp geri gelir) | 44 | **REFERANS + BAŞLANGIÇ KARESİ.** Görünüş metinle tutmuyor; onaylı referans karesinden üretilen başlangıç karesi | SINIF 🅑3 · 🅐5 (durum merdiveni metinle tutmadı) |
| 6 | Kamera / kesme | 39 | Bir kısmı **eski rubriğin önyargısı**: normal kesme 🔴 sayılmış (bkz. §D). Gerçek olanlar: bölünmüş ekran, gizli atlama, kesmede yarım kalan eylem | ham raporlar |
| 7 | Yerçekimine aykırı süzülme / iki yerçekimi aynı filmde | 38 | **TASARIM.** Aynı kadrajda iki yerçekimi rejimi varsa ayıran işaret (tutamak, kemer) görünür; yerçekimini sayıyla yazmanın faydası gösterilemedi | SINIF 🅑4 · 🅑4b |
| 8 | Filigran / köşe logosu | 17 | **ARAÇ AYARI + yeniden dışa aktarma.** Promptta yapılacak bir şey yok ("no watermark" beş filmde yazılıydı) | SINIF 🅐3 |
| 9 | Klon / fazla kişi | 16 | **KADRAJ.** Bir kadrajda en az kişi; ikinci kişi ancak hikâye istiyorsa | ham raporlar |
| 10 | Beden / nesne zemine geçme | 13 | **HAREKET.** Zemine yaslanma, diz çökme gibi geniş temaslar kısa tutulur ya da bölünür | ham raporlar |
| 11 | Yüz / kimlik / SES kimliği değişimi | 8 | **REFERANS** (yüz) · **KURGU** (ses: replik tek kaynaktan, modelin ürettiği ses kullanılmaz) | ham raporlar |
| 12 | Kurgu: tekrar eden yarı / eksik doruk | 5 | **KURGU VERİSİ.** `kurgu.py kontrol` + `liste`; final baştan sona izlenir | INWARD_FALL (ikinci yarı birinci yarının kopyası) |

---

## C · PROMPTUN KENDİ KELİMESİ KADRAJA YAZI OLARAK BASILIYOR

| Promptta | Ekranda | Film |
|---|---|---|
| `PHASE 1` (durum etiketi) | göğüs plakasına basıldı | THE_PAYLOAD |
| `EVA` (kısaltma, 10 promptta) | sırta basıldı | THE_PAYLOAD |
| `rose` (renk adı, 139 kez) | ekrana yazıldı | THE_ROSE_COAT |
| `S04` (sahne etiketi) | hava kilidi gövdesine stencil | THE_SOLAR_MIRROR |
| `ORION` (büyük harfli ad) | göğüs kutusuna yazıldı | THE_CRACKED_HELMET |

```
⛔ Prompt gövdesine YAZILMAZ: sahne/çekim kodu (S04 · C03 · K18) · "Clip 18 of 24" · referans kodu
   (R3 · RK1) · büyük harfli kısa etiket · başlık satırları (IN FRAME: · LIP-SYNC REQUIRED).
   Bunlar FILM.md'de promptun DIŞINDA durur. Ayırt edici bir kelime tekrar ediyorsa her seferinde
   bir nesneye bağlanır ("the rose-coloured coat"), tek başına durmaz.
```
Kaynak: SINIF 🅑6.

---

## D · YAPAY ZEKÂ QA'NIN BİLİNEN ÖNYARGILARI — tarama sonucunu okurken

| Önyargı | Vaka | Ne yapılır |
|---|---|---|
| Normal kesmeyi hata saymak ("Hard cut to interior" 🔴) | ham raporlar (eski rubrik "0 kesme" varsayıyordu) | TARAMA promptu kesmeyi açıkça hata dışı sayar |
| Doğru fiziği kusur sanmak (gövdeden iletilen ses, ince atmosfer = "vakum", 0,30 g = "floaty") | SUSMAYAN · THE_FALLING_WORLD | Tarama girdisinde 4 satırlık "ne olmalı" bloğu verilir |
| Plan verilmeyince yapıyı uydurmak (var olmayan sahnelere puan) | THE_SLOW_STONE | Tarama tek klip ya da ≤90 sn parçaya koşulur; puan istenmez |
| Aynı filmi iki kez ölçünce ±1,3 puan oynamak | `T1_KARE_KALITE.md` | Puan istenmez, yazılmaz |
| Nesneyi başka adla anmak (rover → "buggy", gümüş bant → "duct tape") | THE_FALLING_WORLD | Bulgu kelimeyle değil, gösterilen NESNEYLE eşlenir |
| "Bulamadım"ın "temiz" sanılması | — | Final her zaman insan gözüyle, sesli ve baştan sona izlenir |

Kaynak: SINIF 🅒 · `kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/ARSIV_20261006/UC_GECISLI_QA/00_QA_SISTEMI_REHBERI.md`.
