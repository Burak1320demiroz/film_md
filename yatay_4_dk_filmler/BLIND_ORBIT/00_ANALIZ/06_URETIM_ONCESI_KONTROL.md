# ✅ BLIND_ORBIT — ÜRETİM ÖNCESİ KONTROL (18 MADDE)

**Kaynak:** `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`
**Ne zaman:** PLAN + Bible + 48 prompt + referans paketi + SPEC yazıldı, **tek kare üretilmedi.**
**Tarih:** 05.10.2026 · **Koşan:** yazım · **Maliyet:** 0

> ⛔ Bu dosya bir ÖZET değildir: her madde DOSYA ve SATIR/ÖLÇÜM göstererek cevaplanır.

---

## 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### ☑ A0 — HİKÂYE ONAYI
```
□→☑ 00_ANALIZ/00_HIKAYE_ONAYI.md var · ONAY: 05.10.2026 · sahip · TUR 1/3 (tarihli)
□→☑ satır sayısı = sahne sayısı: S1…S6 = 6 satır · PLAN SAHNE PLANI 2 6 4 6 4 2 ✅
□→☑ SAHNELER'de jargon yok — ㉙ ilk koşuda "kilit" yakaladı (S5 satırı "dört sert kilit")
    → "dört kanca sırayla kapanıyor" yapıldı; olay aynı, kelime değişti ✅
□→☑ SAPMA 1 (dört replik) sahip onaylı: "ONAY (SAPMA 1): 05.10.2026 · sahip · dördü de
    onaylandı". PLAN sahne haritası onaylı satırlarla ve saat aralıklarıyla BİREBİR.
□→☑ LOGLINE 21 kelime (≤25) · NEDEN İZLENİR tek soru · BEDEL klip numaralı (K07 · K10 · K18)
□→☑ hikâye SAHİBİN (yapıştırılan plan) → 0.7a fikir turu KOŞMADI, gerekçe onay dosyasında
```

### ☑ A1 — Yasak ↔ anlatım çelişkisi ⭐ EN PAHALI HATA
```
□→☑ "No readable text, letters, digits or symbols" 48/48 promptta VAR (ölçüldü)
□→☑ Hiçbir ekranın İÇERİĞİ okunur değer taşımıyor: yanaşma ekranı "lit a flat pale grey"
    (K11) / "a flat black rectangle" (K16-K18); rezerv "one thin amber line" — uzun/kısa/çok
    kısa (rakam yok); bilek göstergesi "a single needle on a plain dial"; retikül "two fine
    cross-hair lines" (ölçek çizgisi yok). A1 kapısı (ekran + okunan değer) 0 bulgu.
□→☑ Bilgi metinsiz kanallarda: rezerv çizgisi · kanat süpürüşü (spin eşleme) · makine sesi
    (sayılar yalnız orada, R4 · R16) [D82 · D78]
```

### ☑ A2 — Sahne/klip sayısı tutuyor mu
```
⚙️ ÖLÇÜLDÜ (05.10.2026, elle sayılmadı):
   `# 📍 SAHNE`   BÖLÜM_1 = 3 · BÖLÜM_2 = 3   → 6 ✅
   `## 🎬 KLİP`   12 + 12                      → 24 ✅
   `of 24.`       48 prompt                     ✅
   00_SAHNE_TABLOSU.md K satırı 24 ✅ (㉚)
   SAHNE PLANI 2 6 4 6 4 2 = 24 · en uzun sahne 6 (≤6) ✅ · bölüm sınırı S3|S4 (sahne bölünmüyor)
```

### ☑ A3 — Süre tutuyor mu
```
□→☑ 24 × 10,0 s = 240,0 s = RUNTIME ✅ (hook ofseti YOK — K01 0,0 s'de başlar)
□→☑ Bölümler: B1 K01-K12 = 0-120 s · B2 K13-K24 = 120-240 s ✅
⬜ KLİP SÜRESİ ARAÇTAN ÖLÇÜLECEK [D124] — ffprobe komutu PLAN künyesinde. TAHMİN YAZILMADI.
```

### ☑ A4 — Yasaklı sahne tipi var mı ⭐ [DERS 77]
```
□→☑ 24 klip tek tek soruldu:
    · İNİŞ / KALKIŞ: yok · YANAŞMA: VAR ve filmin konusu — K13-K21 dört kademeye bölündü
      (eksen K13 · spin K14-K15 · son boşluk K19 · temas K20 · kilit K21); hiçbir klip
      "yaklaşır ve kenetlenir" diye tek hareket istemiyor
    · LOŞ MEKÂNA GİRİŞ: yok (geçide giriş kadraj dışında; K09 geçidin içinde başlar)
    · UZUN YÜRÜYÜŞ: yok — 0 g; tek yer değiştirme K09 raylarda çekilme (olayın içinde)
    · KONSOL BAŞINDA OTURMA: VAR (K04 K06 K08 K11 K14 K16) — ⚠️ altısının her biri tek bir
      gövde OLAYI taşır: iki sıkış · büyük düzeltme · 1,2 s kilitli önkol · ekranın kararması
      · kanatların yavaşlaması · elin kabzadan çekilmesi; kamera C arkadan, yüz yok
    · KALABALIK: yok (en çok 2 insan, yalnız K04 K06 K08)
```

### ☑ A5 — FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI [D192]
```
□→☑ Risk ADIYLA: DÖNÜŞ EŞLEMESİNİN OKUNMAMASI (02_KONSEPT §5 · 04_UYARI ⛔ · PLAN İPTAL KAPISI)
□→☑ POZİTİF biçim SAYI taşıyor: "a quarter of the way around the frame in ten seconds, in
    one steady direction, never reversing" (K15 kilit satırı) · PHYSICS "once every forty
    seconds" 24/24 video · K05 "a quarter of the way round in ten seconds"
□→☑ SPEC G1 üç kare (140,5 · 145,0 · 149,5 s) aynı sayıyı soruyor
□→☑ İPTAL KAPISI yazılı: iki üretimde tutmazsa kamera A'ya taşınır (PLAN · DEFTER ilk satır K15)
```

---

## 🟠 B. HİKÂYE VE KAMERA KAPILARI

### ☑ B1 — Doruk anı bir klibin İÇİNDE mi
```
□→☑ Temas K20 3,0 s'de klip İÇİNDE (IMAGE = halkalar aralıklı [D179]) · dört kanca K21
    2,0-6,5 s klip İÇİNDE (IMAGE = kancalar açık) · ikisi KESİLEMEZ listesinde [D62]
□→☑ D213: temas · değişim · sonuç aynı klipte (K20 esneme + tutma · K21 dört kanca + kapalı kalma)
```

### ☑ B1b — Katmanlı dünya ise ışık takvimi var mı
```
□→☑ İç + dış iki katman: tek key kadran 10 (sol üst) · iç 5600 K · S06 motor ışığı İLAN
    EDİLMİŞ olay (K22|K23 sınırı) · sahne içi LIGHT birebir (㉜⑥ makine onayı) · SPEC C
```

### ☑ B2 — Bedelli seçim var mı
```
□→☑ K18: kendi gözü (pencere + kara ekran) ↔ ses — REDDEDİLEN nesne (kara ekran) kadrajda ·
    bedel: alışkanlığın kırılması (başparmak durur) + kontrolün bırakılması · ÇAPA CHOICE
    BEFORE/AFTER PLAN'da ve SPEC'te
```

### ☑ B3 — Tema hangi klipte EKRANA çıkıyor
```
□→☑ GÜVEN: K08 (bekleyen el → "Do it.") · K18 (el gevşer) · K19 ("With you.") · K23 (el
    dizine açık) — dördü de bir GÖVDE değişimi, hiçbiri tema kelimesini söylemiyor
```

### ☑ B4 — Açı yayı yazıldı mı
```
□→☑ 10 kurulum · 5 açı tipi · dönüş 10/24 = %41,7 · ardışık aynı imza 0 (prompt_kontrol
    klasör modu: dizi kapıları GO) · ⚡ şok 1/2 gerekçeli (K20→K21)
```

### ☑ B5 — İSTEK · ENGEL · BEDEL · MUHATAP
```
□→☑ PLAN B5 bloğu (⑰ makine kapısı GO): İSTEK bir İŞ (kenetlemek) · BEDEL üç klip numaralı
    (K07 · K10 · K18) · MUHATAP ikinci insan
```

### ☑ B5b — AYRILIK
```
□→☑ K08 ERTELEME (1,2 s kilitli önkol) · K18 tersinmiş RET → UYMA · ⚠️ prompt_kontrol ilk
    koşuda "AYRILIK yazılmamış" dedi: satır "B5b □ AYRILIK:" biçimindeydi, desen "B5b"yi
    tanımıyor → "B5 □ AYRILIK:" yapıldı, kapı GO
```

### ☑ B5c — ÜRETİM SIRASI [D168]
```
□→☑ PLAN · REFERANS §2 · DEFTER §2 üçü AYNI sırada: ref paketi → K15 → K20 → K21 → K18 →
    K24 → K23 → K01 → K02 → … · DEFTER ilk satırı K15
```

### ☑ B6 — POLİTİKA SATIRI ve ANLAM MALİYETİ
```
□→☑ PLAN POLİTİKA SATIRI: en riskli kare K03 (hasarlı gemi + gaz) nötr tarifle · ÖNLEM/
    MALİYET/TELAFİ tablosu üç satır · ⑯ politika sözlüğü 48 promptta 0 vuruş
□→☑ Bu koşuda yakalanan: K10 "the wheel stops dead" → "stops short" (T2 "dead")
```

---

## 🔢 C. SAYISAL KİLİT DENETİMİ

### ☑ C1 — Sayısal kilit listesi TARİF değil SAYI taşıyor mu
```
□→☑ PLAN SAYISAL KİLİT LİSTESİ 11 satır, hepsi sayı: insan şeridi · kask 24/24 · çeyrek tur
    / 10 s · kanat 3 · kanca 4 (2,0 · 3,5 · 5,0 · 6,5 s) · temas 3,0 s · rezerv üç kademe ·
    replik 17 · 0 g
□→☑ ⚠️ BU KOŞUDA DÜZELTİLDİ: "10 insansız / 14 insanlı / yalnız K04 · K08" ANALİZDEN
    taşınmış ELLE SAYIYDI; promptlardan ölçülen şerit -1-2-2-21111-1-1111--11- → 9 insansız
    · 12 tek · 3 iki kişi (K06 da iki kişi). PLAN · 01 · 02 · 04 · REFERANS düzeltildi.
```

---

## 🧪 BU KOŞUDA BULUNAN GERÇEK HATALAR (üretimden ÖNCE, maliyet 0)

```
① İNSAN SAYIMI elle yazılmıştı (10/14) — ölçüm 9/15; K06'nın iki kişi olduğu atlanmıştı
② PLAN Bible metinleri prompttakinden UZUNDU (LIGHT/PHYSICS/AUDIO/CAMERA) — prompta giren
   kısaltılmış hâller PLAN'a BİREBİR geri yazıldı (Bible ↔ prompt ayrışması = ⑬ sahte bulgu)
③ Videolarda sırt cümlesi yoktu (IMAGE'da vardı) — D139 13 video promptunda pozitif
   "one continuous smooth surface" eklendi
④ "to her right" (nesne-göreli taraf) H kurulumunda → "off to screen right"
⑤ K15 kilit cümlesinde "behind them" ⑮ arkadan-kamera yanlış-pozitifi → "beyond them"
   (05_SAHNE_CALISMALARI/K15_NOVUM.md de güncellendi)
⑥ "lifts/pulls" efor fiilleri gövde kanalı olmadan (K09 K12 K16 K17 K23) → önkol kanalı ya
   da nötr fiil
⑦ K10 "stops dead" (politika T2) · K17 "stays still" (durum kalıbı) → düzeltildi
⑧ D79 vizör şeffaflığı BÖLÜM_1'de hiç yoktu (yüz klibi yok) → K02'ye vizör cümlesi
```

## 🔎 EK KOŞU — D59 GREP'İ VE YASAK SÖZLÜK (üretimden önce, zorunlu)

```
⚙️ 05.10.2026 · 48 promptun POZİTİF gövdesi tarandı:
  suspend 0 · hover 0 · frozen 0 · swirl 0 · motionless 0 ✅
  hang 8 — MEŞRU: 7 × dünya çapası "Behind everything hangs a black hole" (vakum, yerçekimi
     iddiası değil) + 1 × K16 "her glove hangs above the grip" (0 g'de el)
  float 3 — MEŞRU: boş koltuğun kemeri "floating loose" (0 g — ortam kartının kanıtı)
  holds still 8 — MEŞRU: hepsi YAPI/HALKA/KANAT (K15 novum: istasyon yüzü duruyor, evren
     dönüyor) — insan durağanlığı için 0 kez
  stop* 16 — MEŞRU: direnç ve eylem sınırı (çark takılır · başparmak avuç kala durur · gemi
     halkaya dayanır)
  dead 0 (düzeltildi) · burn 2 — makine repliği "Station burn" (sahip onaylı, motor yanışı)
  damaged 1 — R6 repliği "damaged bank" (sahip onaylı, ⑯ sözlüğünde yok)
⚙️ TÜM GÖVDE (negatif blok dâhil):
  seamless 0 · badge 0 · insignia 0 · glowing 0 · radiant 0 · ethereal 0 · shimmer 0 ·
  tripod 0 · anamorphic 0 · "exact last frame" 0 · "previous clip" 0 ✅
  özel ad (Lena · Noah · LARK · VESPER) 0 · kurum (NASA · ESA · SpaceX · Soyuz · Mir) 0 ✅
  bubble 6 · dome 6 · emblem 18 — ⚠️ YANLIŞ-POZİTİF: yalnız negatif bloğun içinde [D85]
  \d+ m 76 — ⚠️ hepsi CAMERA satırında; gövdede birim gövde boyu / el genişliği [D138]
```

---

## ✅ KAPI

```
☑ 18 maddenin 18'i cevaplandı, her biri dosya ve ölçüm gösterdi
☑ Sekiz GERÇEK hata bulundu ve üretimden ÖNCE düzeltildi (maliyet 0)
☑ prompt_kontrol.py klasör modu: ⛔ 0 BLOCK · klasör ✅ GO (05.10.2026)
   dosya FIX'leri gerekçeli: insansız 9 klipte "insan sayısı" (red #2 · GUNES_MEZARI emsali) ·
   bölünmüş-film iskelet sayımı (24 harf ↔ dosya başına 12 — klasör modu tam iskeleti ölçer)
☑ Diyalog kritiği GO (07_DIYALOG_KRITIGI.md) — R3 REDUNDANT sahibe not
☑ ölçüm randevuları AÇIK: klip süresi [D124] · ref paketi kabul kapısı · seed alanı [D142]
→ üretim KAPI 0'a (referans paketi) geçebilir
```
