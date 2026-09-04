# 🌍 YERÇEKİMİ — FİLM KAYDI

`yatay_10_20_dk_filmler/YERCEKIMI` · 120 sahne × 8 s = 16:00 · yatay 10-20 dk
Yazım 120/120 GO · üretim 01.09.2026'da FAZ 1 ile başladı.

---

# 📋 KOŞU 1 — FAZ 1 MAKARASI · 01.09.2026

```
Ham rapor  02_HAM_RAPORLAR/YERCEKIMI_FAZ01_HAM.md
Rubrik     FAZ_01_GOREV/FAZ_01_QA_PROMPT.md (⭐ sıradan bağımsız sürüm)
Mod        ⚠️ V — ÖN KOŞU. Film klasöründe *_QA_SPEC.md YOK [D129].
           ⛔ Skor satırı T tablolarına GİRMEZ. Faz koşusu zaten girmezdi.
```

## § ÖLÇÜM KAPISI ⑪ — ⛔ KOŞULAMADI

```
Master elde yok. Skript koşulmadı. Raporun sayıları DOĞRULANMADI.

RAPORUN BEYANI (doğrulanmamış):
  toplam süre    80 s
  parça sayısı   10
  klip süresi    8,0 s · parçalar arası sapma ≤ 0,3 s

⛔ BU SAYILAR HİÇBİR KAPIYA GİRDİ SAYILMADI [skill §1].
⚠️ D124 KAPISI HÂLÂ AÇIK. Rapor "8,0 s" diyor ama bir modelin beyanı
   ölçüm değildir [D125: komut satırında cevabı duran soru modele
   sorulmaz]. 00_PLAN'daki `KLİP SÜRESİ = ____` DOLDURULMADI.
   Kapatan tek şey şu satırdır:
     ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>.mp4
```

## § KİMLİK KAPISI ③ — 🚨 DÜŞTÜ · UNATTRIBUTED [01.09, aynı gün düzeltildi]

```
⛔ İLK DEĞERLENDİRME YANLIŞTI VE GERİ ALINDI.

İlk okumada dört çapa sayıldı: sırt ünitesi · şerit ayrımı · platform ·
gökteki çizgi. "Denetçi malzemeye bakmış" denildi.

🚨 SONRA ŞU GÖRÜLDÜ: DÖRDÜ DE RUBRİĞİN İÇİNDE DENETÇİYE VERİLMİŞTİ.
   Kapı ③'ün şartı "belgeye eşlenen metin-DIŞI çapa"dır; denetçiye
   promptla SÖYLENMİŞ bir tarifin raporda geri gelmesi çapa DEĞİLDİR.
   Bu bir eşleşme değil, bir yankıdır.

   En kritik örnek — SIRT ÜNİTESİ:
   Rubriğin OPEN ITEM bloğu iki tasarımı da kelimesi kelimesine
   yazıyordu ("...the other is a flat rectangular slab, taller than
   wide, with recessed seams and flush corner nozzle recesses").
   Denetçi ikisinden birini seçip aynı kelimelerle geri verdi.
   İki seçenekli bir yazı-tura, gözlem sayılmaz.

🚨 VE BU, DAHA SERT BİR OLGUYLA BİRLEŞİYOR:
   REFERANS_PAKETI'nde ÜRETİLMİŞ TEK PANEL YOK — 0/15, seed kutuları
   boş, ☑ sayısı 0. Yani ortada yüklenecek bir RC sayfası yoktu.
   O hâlde dikdörtgen levha ya modelin kendi varsayılanıdır
   (düz sırt çantası zaten yaygın varsayılan), ya da denetçinin
   rubrikten okuduğu tariftir. Referans sayfasından GELEMEZ.

SONUÇ: rapor UNATTRIBUTED. Ham rapor korunur, SKOR YAZILMAZ,
       DERS YAZILMAZ [skill §3]. Bulgular "iddia" statüsündedir;
       hiçbiri kareyle doğrulanmadan gerçek sayılmaz.

⛔ GERİ ALINAN SONUÇ: "referans sayfası promptu yener, 58 prompt
   geçişi üretimi engellemiyor, RC fiilî masterdır."
   BU SONUÇ DESTEKSİZDİR. Hiçbir referans sayfası üretilmediği için
   sayfa ↔ prompt yarışı HİÇ KOŞULMADI. Soru hâlâ açık.

✅ KAPATAN TEK ŞEY: KARE. İki komut yeter —
   ffmpeg -ss 26 -i <makara>.mp4 -frames:v 1 vizor.jpg   # kubbe mi, düz cam mı
   ffmpeg -ss 18 -i <makara>.mp4 -frames:v 1 sirt.jpg    # levha mı, kafes mi
```

## § KURGU KAPISI ④ — ⚠️ ŞARTLI (ölçüm yok) · sıra ölçütü UYGULANMADI

```
klip sayısı  10   ↔ katalog 11 bekliyor → 1 EKSİK (G)
süre         80 s ↔ 10 × 8,0 (rapor beyanı, doğrulanmadı)
sıra         ⛔ ÖLÇÜT UYGULANMADI — klipler kasten karışık üretildi;
             rubrik sıradan bağımsız yazıldı, İNSAN ŞERİDİ koşulmaz.
⚠️ S8 iptal edildiği için katalog 11'dir (12 değil) — beklenen sayı 11.
```

## § ÖNERME KAPISI ⑩ — bulgular plana karşı okundu

```
✅ PLANA UYAN (rubriğin kendi "MOST LIKELY FAILURE" satırları gerçek oldu)
   · H'de sırtta ünite    → rubrik bunu ismen öngörmüştü
   · D'de kubbe vizör     → D146'nın ismen öngördüğü hata
   · J'de figür çizgiye bakıyor → rubriğin "tek işini yok eder" dediği şey
   · K'de bakış yukarı-sol → rubriğin "bloker" dediği yön

⚠️ AMA BU BİR ZAAF DA OLABİLİR: rubrik denetçiye "en olası hata şudur"
   diye söyledi. Söylenen hatanın raporda çıkması, hatanın GERÇEK
   olduğunu kanıtlamaz — PRIMING riski. Dördü de kareyle doğrulanmalı.
   ⛔ Bu rubriğin yapısal açığıdır, kayda geçti.

🔴 RAPORUN KENDİYLE ÇELİŞTİĞİ YERLER
   · Çapraz kontrol 4 mekiği "B ve I"de sayıyor — ama K'de de mekik
     kadrajda (S12 promptu: "a white thirty-seven-metre shuttle hangs
     in the black"). K denetlenmemiş.
   · Panel durumu listesi yalnız A, B, J diyor; E ve H de paneli
     gösteriyor. Liste eksik.
   · "shuttle drifts" hem VACUUM PHYSICS hem WORLD CONSISTENCY
     altında sayılmış → aynı kusur ortalamayı İKİ KEZ düşürüyor.
   · C'de "mouths moving": C'de adamın ağzı kafasının arkasında,
     kadının ağzı çok uzakta. O kadrajda ağız fiziksel olarak
     okunamaz. Kareyle doğrulanmadan kabul edilmez.
```

## § SKOR — ⛔ KAYDA GEÇMİYOR, GEREKÇESİ AŞAĞIDA

```
Raporun ortalaması 4,9 (aritmetik DOĞRU: 54/11 = 4,909).
⛔ AMA SAYI KULLANILAMAZ. İki yapısal kusur:

① GEREKÇESİZ KIRINTI — beş kategori "kusur bulunamadı" diyor ama
   yine de 6-7 puan almış:
     IDENTITY 6      "Facial features remain stable"
     FIGURE COUNT 7  "Counts strictly accurate"
     CAMERA 7        "Locked off with zero movement"
     DELIVERY 7      "No watermarks, correct segment timing"
     COVERAGE 6      11'in 10'u yüksek güvenle teşhis edildi
   Beşi de temiz beyan edilip 3-4 puan kırılmış. Kırıntının
   gerekçesi YOK.
   → Beşi 9 olsaydı ortalama 6,0 olurdu. Fark 1,1.
   [kural ⑥: 1,5 altı fark gürültüdür — yani bu ortalama zaten
    karar verecek çözünürlükte değil.]

② ÇİFT SAYIM — "shuttle drifts" iki kategoride birden.

SONUÇ: BULGU LİSTESİ KULLANILIR, SAYI KULLANILMAZ.
       00_INDEX'e skor yazılmıyor.
```

## § 🔴 KÖK SEBEP — REFERANS PAKETİ HİÇ ÜRETİLMEDİ

```
REFERANS_PAKETI.md · 9 sayfa · 15 panel · ÜRETİLEN: 0 · seed: 0
Paketin kendi kuralı: "üretim RA · RC · RB · RD sayfaları onaylanıp
seed'leri yazılmadan BAŞLAMAZ."  → Bu kapı atlandı.

⭐ RAPORDAKİ ÜÇ AĞIR İDDİA TAM DA BUNUN BEKLENEN SONUCU:
   kubbe vizör · kadının sırtında ünite · giyside metin
   Üçü de modelin VARSAYILANIDIR. Çapa olmadığında model varsayılana
   döner — RA sayfasının tek işi buydu.
   ⛔ Yani bunlar prompt kusuru bile olmayabilir; ANCHOR YOKLUĞUDUR.

→ FAZ 2 aynı koşullarda üretilirse aynı üç kusur tekrar gelir.
  Maliyet: F1'de 10 klip, F1+F2'de 22 klip.
```

## § ~~EN DEĞERLİ ÇIKTI~~ — 🚨 GERİ ALINDI, yukarıdaki ③ kapısına bak

```
Denetçiye "sırt ünitesini TARİF ET, PUANLAMA" denmişti. Cevap:
  "flat rectangular slab … recessed seams … flush corner nozzle
   recesses … does not possess an open tubular frame or protruding
   arms … consistent across his appearances"

⭐ BU, 31.08'DE AÇIK BIRAKILAN SORUYU CEVAPLIYOR:
   REFERANS_PAKETI RC 31.08'de güncellendi (düz dikdörtgen levha),
   ama 58 sahne promptu eski tarifi (açık boru kafes) taşıyordu ve
   propagasyon yapılmamıştı. Hangisinin kazanacağı bilinmiyordu.

   ✅ CEVAP: REFERANS SAYFASI KAZANIYOR. Flow, yüklenen sayfanın
      geometrisini uyguladı; promptun eski cümlesini uygulamadı.

   → 58 prompt geçişi ÜRETİMİ ENGELLEMİYOR. RC fiilî masterdır.
   → Yine de temizlenmeli (kural ①: aynı nesne iki tarifle duramaz),
     ama ACİL değil ve üretimi durdurmaz.
```

---

# 🔧 AKSİYON LİSTESİ — üç kuşak

## 🔴 KUŞAK 1 — FAZ 2'DEN ÖNCE (küresel; düzeltilmezse her faza bulaşır)

```
① KUBBE VİZÖR [D146]              her kaskta, her fazda tekrarlanır
   A'nın kaskı S1-S47, B'nin 44 sahne. Faz 2-3-4 aynı hatayı miras alır.
② KADININ SIRTINDA ÜNİTE [D139]   modelin varsayılanı geri geliyor
   Ayrışma kilidinin (klon kapısı) üç işaretinden biri.
③ GİYSİDE OKUNAN METİN [D138]     mutlak metin yasağı, film geneli
⛔ ÜÇÜ DE SAHNE KUSURU DEĞİL, REFERANS/PROMPT KUSURUDUR.
   On promptu tek tek düzeltmekle geçmez — RA/RC sayfaları ve
   negatif çekirdek düzeyinde çözülür.
```

## 🟠 KUŞAK 2 — FAZ 1'İ KAPATMAK İÇİN

```
④ G (S7) EKSİK — komutan döner ve durur. Üretilmedi. Çekilmeli.
⑤ MEKİK BURNU EKRAN-SAĞ (B, I) — yönelim kilidi düştü.
   ⚠️ K de kontrol edilmeli, rapor K'yi hiç bakmamış.
⑥ HALAT KAVİS ÇİZİYOR + MEKİK SÜZÜLÜYOR — vakum fiziği.
⑦ ŞERİT 5 SEGMENT (F) — 4 segmentli şerit 5 gösteremez.
⑧ J ve K'de FİGÜR ÇİZGİYE BAKIYOR — dramatik ironiyi yok eder,
   iki sahnenin de TEK işi buydu.
```

## 🟡 KUŞAK 3 — İNANMADAN ÖNCE KAREYLE DOĞRULA

```
⑨ C'de "ağızlar oynuyor" — o kadrajda ağız okunamaz. Şüpheli.
⑩ E'de "saat sol bilekte" — belge net: halka SOL, saat SAĞ manşet;
   S5 promptu "her RIGHT glove … the black watch strap crossing the
   cuff" diyor. Render hatasıysa gerçek; ama tepeden tek-el makrosunda
   sağ/sol ayrımı zordur.
⑪ Kuşak 1'in dördü — priming riski (yukarıda ⑩ kapısı).
```

---

# 📮 DENETÇİNİN İKİ SORUSU — CEVAPLANDI

```
S: "Segment 5'te saatin sol bilekte olması ayna hatası mı, yoksa
    pasaportun el yönü mü ters?"
C: PASAPORT TERS DEĞİL. Belge üç yerde net: oksijen halkası SOL
   manşette, çelik saat SAĞ manşette. S5'in kendi promptu kadraja
   giren şeyi "her RIGHT glove … the black watch strap crossing the
   cuff" diye yazıyor. Ters çıktıysa RENDER hatasıdır.

S: "Düz dikdörtgen sırt ünitesi tercih edilen üretim tasarımına
    uyuyor mu?"
C: EVET, BİREBİR. 31.08 RC revizyonu tam olarak budur. Bu cevap
   yukarıdaki §EN DEĞERLİ ÇIKTI maddesini doğruluyor.
   ⚠️ 01.09 EKİ: bu cevap F1'de YANKI olduğu için geçersiz sayılmıştı.
   FAZ 2'nin KÖR geçişi aynı sonucu HİÇBİR TARİF VERİLMEDEN üretti
   → artık desteklidir. Aşağıya bak: KOŞU 2 · §③.
```

---
---

# 📋 KOŞU 2 — FAZ 2 MAKARASI · 01.09.2026 · ⭐ İKİ MÜHÜRLÜ GEÇİŞ

```
Malzeme   FAZ 2 makarası · 12 parça · 96 s (iki rapor da aynı sayıyı verdi)
Rubrik    FAZ_02_DALGA/FAZ_02_QA_PROMPT.md — A (kör) + B (katalog)
Motor     Gemini · iki AYRI sohbet, mühür korundu
Ham       02_HAM_RAPORLAR/YERCEKIMI_FAZ02_KOR_HAM.md
          02_HAM_RAPORLAR/YERCEKIMI_FAZ02_KATALOG_HAM.md
Mod       ⚠️ V — *_QA_SPEC.md YOK [D129] · master ELDE YOK [⑪]
⛔ Faz koşusudur: T1-T4 skor tablolarına GİRMEZ.
```

## § ÖLÇÜM KAPISI ⑪ — ⛔ KOŞULAMADI, ama sayı İKİ KEZ BEYAN EDİLDİ

```
İki bağımsız denetçi, ayrı sohbetlerde, aynı üç sayıyı verdi:
   96 s toplam · 12 parça · 8,0 s/parça · sapma < 0,3 s
Bu bir ÖLÇÜM DEĞİLDİR (master elde yok) ama iki bağımsız beyanın
çakışması tek beyandan güçlüdür. D124 kapısının F2 cevabı: KLİP = 8,0 s.
⛔ 00_PLAN'daki `KLİP SÜRESİ = ____` satırı yine de master ölçümüyle
   kapanır; buraya "iki kez beyan" diye yazıldı, "ölçüldü" diye değil.
```

## § KİMLİK KAPISI ③ — ✅ GEÇTİ · SEKİZ YANKISIZ ÇAPA

⭐ **F1'de kapanamayan kapı burada kapandı.** KÖR geçişte denetçiye hiçbir
tarif verilmedi; aşağıdakilerin hepsi kendi gözlemidir ve belgeye oturur.

```
① SIRT DÜZ — "There is absolutely nothing on it; no backpack or
   external equipment is visible." → RA düz-sırt kilidi. ⭐ En değerli
   çapa: F1 raporu tam tersini iddia etmişti.
② HALKA 4 SEGMENT — "a glowing orange panel with four rectangular
   segments on the left wrist" → KİLİT 7 · S19 sonrası 4/6.
   ⭐ SAYISAL ÇAPA: söylenmemiş bir sayıyı doğru saymak en güçlü kanıttır.
③ SAAT SAĞ BİLEKTE — "a black digital watch on the right wrist" → RA
   el yönü (saat SAĞ, halka SOL). Yön doğru, cins yanlış (aşağıda).
④ TURUNCU ŞERİT / BEYAZ GİYSİ, omuz-kol-bacak → RA.
⑤ TURUNCU RAY / BEYAZ KAFES TRUSS / UÇTA GRİ SİLİNDİR → RD p1.
⑥ IŞIK ÜST SAĞDAN — "Light comes from the top right" → L1 kilidi.
⑦ ENKAZ SAĞDAN SOLA, DÜZ ÇİZGİ, SABİT HIZ → KİLİT 5.
⑧ EKRANDA SIFIR YAZI — "no readable letters, digits, numbers or text"
   → mutlak metin kilidi. ⚠️ Ama aynı rapor adamda "US flag patch"
   diyor; kendi içinde çelişiyor (aşağıda 🔴 KARE BEKLEYEN).
```

## § SIRA SKORU — ⭐ YENİ ÖLÇÜ · HİKÂYENİN OKUNABİLİRLİĞİ

```
KÖR denetçinin kurduğu sıra (harfe çevrilmiş):
   A · B · B · F · E · D · J · H · I · G · K · L
GERÇEK sıra (C üretilmediği için 11 girdi + B tekrarı):
   A · B · B · D · E · F · G · H · I · J · K · L

   SIRA SKORU = 8/12 doğru konum
   (D↔E berabere sayılırsa 9/12 — ikisi eşzamanlı, kanıt yok)
```

**Dört sapmanın hepsi İKİ sebebe indi:**

```
🔴 SEBEP 1 — F (S18 KOPUŞ) ANLAŞILMADI
   Kör denetçi F'yi SAĞLAM kliplerin arasına koydu. Sebebi tarifinde:
   "One person's face inside a helmet. An orange rail is in the
    foreground. The person looks around slightly."
   ⛔ HALATIN KOPTUĞUNU HİÇ GÖRMEDİ. S18'in TEK olayı budur.
   Halat kadrajın alt-sağ KENARINDA, ince, 2. saniyede kopuyor;
   ikinci sinyal (vizördeki dönme yansıması) da zayıf.
   → Filmin dönüm anı, ilk izlemede görünmüyor.

🔴 SEBEP 2 — SAVRULMA BLOĞUNUN SAATİ YOK
   Denetçi kendi yazdı: "Least sure: the exact order of Segments 4, 7
   and 10, because they all depict the identical physical state."
   Bunlar I · H · G. Aralarındaki TEK ayrım oksijen halkası 6/6 → 4/6.
   ⛔ Halka yalnız G'de okunabiliyor. Karşılaştırılacak ikinci okuma
      YOK. Tek noktada okunan sayaç SAAT DEĞİLDİR.
```

## § ⑩ ÖNERME KAPISI — filme ait sonuç

```
⭐ BU FİLMİN SAYACINI İZLEYİCİ HİÇ OKUYAMIYOR — film boyu sorun.
   Halka: 6/6 → 4/6 (S19) → 3/6 (F4) → 2/6 (S46) → devamı.
   Ama faz dosyalarındaki durum notları neredeyse her seferinde
   "(kadrajda değil)" · "(kadraj kenarında)" · "vurgusuz" diyor.
   F2'nin kör testi bunu DENEYSEL olarak kanıtladı: sayaç görünmediği
   için üç sahne birbirinden ayrılamadı.
   → F3-F10 için karar gerekiyor: her düşüşün ÖNCESİNDE ve SONRASINDA
     halkayı okunur kılan birer kadraj, ya da savrulma bloklarına
     ikinci bir tek yönlü işaret.

✅ GÖK SAATİ ÇALIŞTI — tek başarılı saat.
   B geçişi gökyüzünü girdi girdi okudu ve HEPSİ doğru çıktı:
   A temiz · B/B ince uzak çizgi · D yoğun akış→seyrelme ·
   E seyrelen parça · J seyrelme→temiz · kalanlar temiz.
   ⭐ Bu, filmin en iyi işleyen görsel zinciridir. Model olarak alınmalı.

✅ HASAR TEK YÖNLÜ ÇALIŞTI — hiçbir girdide onarım/geri dönüş yok.
```

## § 🔴 ASIL SONUÇ — METİN VİZÖRÜ TUTAMIYOR, KANIT BURADA

```
Denetçi B sordu: "Promptta gerçekten 'flat pane' ve 'rectangular
frame' yazıyor muydu, yoksa model varsayılana mı döndü?"
CEVAP KOMUT SATIRINDA [D125] — sayıldı:

  "24 by 16 centimetres" ....................... F2'de 9 promptta
  "visible bright metal frame" ................. yazılı
  "flat rectangular front glass" ............... yazılı
  Kubbe çıkan altı klip: Seg 1·4·6·7·8·11 = S13·S21·S18·S20·S16·S23
  Bunların BEŞİNDE tam vizör tarifi ÖLÇÜLERİYLE promptta VARDI.
  Altısında da kubbe çıktı.

⛔ SONUÇ: Vizör kilidi METİNLE TUTULAMIYOR. Ölçü yazmak yetmedi.
   Bunu tutabilecek tek şey RA p4 REFERANS PANELİDİR — ve
   REFERANS_PAKETI'nde üretilmiş panel sayısı 0/15.
   ⭐ Bu, KOŞU 1'de "kök sebep" diye YAZDIĞIM şeyin artık ÖLÇÜLMÜŞ hâli.
      F1'de çıkarımdı; F2'de kanıt.

⚠️ AYRICA: S18 (F) promptunda TAM vizör cümlesi HİÇ YOK — yalnız
   "in her clear visor" geçiyor. Tek boşluk orada; kapatılmalı.
```

## § SAĞLAM / ŞÜPHELİ AYRIMI — iki geçişin çakışması

```
✅ SAĞLAM (kör + katalog, bağımsız iki kez):
   · vizör KUBBE, altı klipte de                        🔴 RED
   · mekik burnu EKRAN-SAĞ (Seg 1·2·3·9·12)             🔴 RED
     ⭐ tek doğru: Seg 5 (E) — burun kadraj DIŞINDA, yön
       kompozisyonu TAŞIYOR. Kilit ancak yük taşıyınca tutuyor.
   · Seg 3 = Seg 2'nin BİREBİR kopyası                  🔴 RED
   · Seg 9'da kaskısız erkek yüzü, alt sağ köşe          🔴 RED
   · enkaz kendi kendiyle çelişiyor: D bükük-bütün ↔ J ikiye AYRILMIŞ
   · Seg 4'te sırt düz-ışıkta, sert gölge yok            🟡 YELLOW
   · sırt ünitesi: KATI DİKDÖRTGEN PANEL, dört köşe nozulu ✅ tasarım
   · sırt DÜZ, hiçbir ünite yok                          ✅ kilit tuttu
   · sıfır okunur yazı                                   ✅ kilit tuttu

⚠️ ŞÜPHELİ (yalnız katalog geçişi gördü — kare ister):
   · K'de momentum yok: A dururken B'de karşı sarsıntı YOK
     (kör izleyici bunu görmez; bu bir uzman ölçütü — ama tek geçiş)

🔵 YALNIZ KÖR GEÇİŞ (gerçek ama ölçüsüz):
   · saat "siyah dijital" — RA "çelik mekanik, siyah kayış" diyor
   · Seg 1'deki saat ile Seg 10'daki halka AYNI ŞEY sanıldı
     → iki bilek nesnesi ilk izlemede birbirinden ayrılmıyor
   · "sırtında yaşam desteği yok, nasıl hayatta?" — kilit DOĞRU
     çalışıyor ama seyirciye FİZİK HATASI gibi okunuyor (tasarım sorusu)
   · "iki kişinin birbirini tanıdığı ANLAŞILMIYOR"
   · S21'deki enkaz "küçük bir uydu" sanıldı → o mesafede okunmuyor
```

## § 🔴 KARE BEKLEYEN TEK ÇELİŞKİ

```
KÖR geçiş adamda "US flag patch on the left shoulder" gördü.
KATALOG geçişi metin/simge kategorisine 10/10 verdi ("sıfır karakter").
Bayrak açıkça yasak (no flag, no insignia, no mission patch) VE
§7 gerçek kurum kuralına girer.
⛔ İki geçiş ÇELİŞİYOR → kareyle biter:
   ffmpeg -ss 84 -i <makara>.mp4 -frames:v 1 omuz.jpg
```

## § SKOR — ⛔ KAYDA GEÇMİYOR

```
B geçişinin ortalaması 6,69 (13 kategori; aritmetiği DOĞRU, kontrol
edildi: toplam 87 / 13 = 6,692).
⛔ Yine de T tablolarına GİRMEZ: mod V (SPEC yok) + master yok +
   faz koşusu. Sayı burada arşiv amaçlı durur.
```

## 🔧 FAZ 2 AKSİYON LİSTESİ

```
🔴 YENİDEN ÜRETMEDEN ÖNCE — yoksa aynı kusur aynen gelir
 ① RA p4 (yüz CU, düz çerçeveli vizör) ÜRETİLİR, vizör doğru çıkana
    kadar tekrarlanır, seed yazılır. TEK GÖRSEL — kilidin tamamı bu.
 ② RD p2 (HASARLI platform) için D veya J karesinden BİRİ seçilir ve
    master ilan edilir. İkisi çelişiyor; biri kazanmalı.
 ③ RD p4 (mekik) — burun yönü ancak referansla tutar.

🔴 YENİDEN ÜRETİM (RED)
 · vizör: Seg 1·4·6·7·8·11 (S13·S21·S18·S20·S16·S23)
 · mekik burnu: Seg 1·2·3·9·12 (S13·S14·S22·S24)
 · Seg 9 (S22): hayalet yüz + enkaz modelini D ile hizala
 · Seg 11 (S23): momentum sarsıntısı
 · C (S15) HİÇ ÜRETİLMEDİ — 🔥 viral #1 + tek kare testi karesi
   ⚠️ B iki kez üretilmiş, C atlanmış: operatör kayması, model hatası değil.

🟠 PROMPT DÜZELTMESİ (üretimden bağımsız)
 · S18'e tam vizör cümlesi eklenir (tek eksik prompt)
 · S18'de halatın kopuşu kadrajda BÜYÜTÜLÜR / ikinci sinyal verilir

🟡 FİLM BOYU KARAR (F3-F10)
 · halka okunurluğu: her düşüşün öncesi+sonrası birer okunur kadraj
 · savrulma bloklarına ikinci tek yönlü işaret
 · saat ile halkanın ilk izlemede ayrışması
```

---
---

# 📋 KOŞU 3 — FAZ 3 MAKARASI · 01.09.2026 · İKİ MÜHÜRLÜ GEÇİŞ

```
Malzeme   FAZ 3 makarası · 12 parça · 96 s (iki rapor da aynı sayıyı verdi)
Rubrik    FAZ_03_HALAT/FAZ_03_QA_PROMPT.md — A (kör) + B (katalog)
Motor     Gemini · iki AYRI sohbet, mühür korundu
Ham       02_HAM_RAPORLAR/YERCEKIMI_FAZ03_{KOR,KATALOG}_HAM.md
Mod       ⚠️ V — *_QA_SPEC.md YOK [D129] · master YOK [⑪]
⛔ Faz koşusudur: T1-T4'e GİRMEZ.
```

## § ⭐ KAPSAM — FİLMİN İLK TEMİZ FAZI

```
MATCHED    12/12   ·   MISSING 0   ·   UNMATCHED 0   ·   KOPYA 0
F1: S8 iptal (11/12) · F2: C üretilmedi + B iki kez (11/12) · F3: TAM.
Figür sayımı 10/10 — H'de sıfır insan dahil.
```

## § ÖLÇÜM KAPISI ⑪ — ⛔ KOŞULAMADI, sayı İKİ KEZ BEYAN EDİLDİ

```
İki bağımsız denetçi, ayrı sohbetlerde: 96 s · 12 parça · 8,0 s · sapma <0,3 s.
Üçüncü fazda üçüncü kez aynı sayı. Ama hâlâ ÖLÇÜM DEĞİL, beyandır.
```

## § KİMLİK KAPISI ③ — ✅ GEÇTİ · DOKUZ YANKISIZ ÇAPA

Kör geçişe hiçbir tarif verilmedi ("istasyon" ve "halat" kelimeleri bile
prompta girmedi). Aşağıdakilerin hepsi denetçinin kendi gözlemidir:

```
① turuncu şerit (kadın, manşetlerde)      ② lacivert şerit (adam, omuz/kol)
③ bir bilekte saat + öbüründe altı hazneli amber halka, DÖRDÜ yanık
④ istasyon: uç uca silindirik modüller + güneş panelleri + SOL uçta kapsül
⑤ kapsül burnu dışa/sola bakıyor          ⑥ sıfır okunur karakter
⑦ turuncu-beyaz çizgili halat             ⑧ Dünya altta, siyah üstte
⑨ ⭐ SIRT ÜNİTESİ: "kocaman kutu biçimli metal yapı, yatay paneller,
   yan raylar, DÖRT dikdörtgen nozul" — F2'nin kör geçişiyle AYNI aile
   (katı dikdörtgen levha + dört köşe nozulu). FAZLAR ARASI ÇAPA.
```

## § SIRA SKORU — 5/12 (F2: 8/12) · VE DÜŞÜŞÜN SEBEBİ TEK

```
KÖR sıralama :  A · B · C · E · K · I · G · L · D · J   (+F ve H yerleştirilemedi)
GERÇEK       :  A · B · C · D · E · F · G · H · I · J · K · L
Doğru konum  :  A · B · C · G · J  =  5/12
```

⛔ **DÜŞÜŞ GÖRSEL ZİNCİRİN ZAYIFLIĞINDAN DEĞİL — SAHTE BİR SAATTEN.**
Kör denetçi kendi "saat" listesine şunu yazdı:

> *"Survivability: Helmets sealed (1,2,3,5,6,9,11,12) → Helmets removed
> or open in space (4, 10). **Confidence: High.**"*

D ve J'yi bu yüzden **sona** koydu: *"a state representing the terminal end."*
İki render kusuru (D'de kask YOK, J'de vizör AÇIK) tek yönlü bir anlatı
saati uydurdu ve fazın finalini değiştirdi.

⭐ **Kurduğum saat ÇALIŞTI:** *"Proximity to station: dot → medium → fills
frame. Confidence: High."* İlk üç konum doğru, hedef C'de doğru okundu.
Sahte saat onu ezdi.

**İkinci sapma sebebi:** G (gevşek halat toplanıyor) K ve L'ye yapıştı —
üçünde de halat gevşek ve G'de istasyon belirgin değil. Halat durumu üç
sahneyi ayıramıyor.

**F ve H yerleştirilemedi** — ikisi de "bağlamsız" kadraj (F'de arka plan
yok, H'de insan yok). Halka düşüşü yine sıraya hiçbir şey katmadı →
`GOZLEM ADAY-3`'ün ÜÇÜNCÜ vakası.

## § 🔴 ASIL BULGU — HİKÂYENİN SONU DEĞİŞTİ

Kör denetçinin yazdığı final cümlesi:

> *"Ultimately, both astronauts are exposed to the vacuum of space, with
> one opening his helmet visor and the other floating entirely without
> her helmet."*

```
Filmin S25-S36'sı istasyona VARIŞLA biter. İzleyicinin gördüğü:
   istasyona varırlar → el ele tutuşurlar → vakumda ÖLÜRLER.
16:00'lık bir filmin 4:48'inde iki ana karakter ölmüş görünüyor.
⛔ Bu bir süreklilik ayrıntısı değil — OLAY ÖRGÜSÜNÜN TERSİNE ÇEVRİLMESİ.
```

## § 🔬 D'NİN SEBEBİ BULUNDU — KOMUT SATIRINDA [D125]

Denetçi sordu: *"Promptta 'kask takılı' yazıyor muydu?"*

```
S28 IMAGE : helmet ×3 · tam vizör cümlesi ölçüleriyle VAR
S28 VIDEO : helmet ×4
⭐ VE S28 VIDEO'DA ŞU CÜMLE VAR:
     "Her body is never rigid: shoulders lead, legs follow,
      HAIR LIFTS INSIDE THE HELMET."
Render: SAÇ KALKTI, KASK GİTTİ. Küçük canlı ayrıntı, kapsayan nesneyi ezdi.
```

Aynı kalıp A'da (S25) da var ve orada da yarı yarıya düştü: kask kaldı,
ama kör denetçi *"hair lifts violently inside helmet as if in wind"* dedi.

```
"hair … in/inside the helmet" KALIBI FİLMDE 8 YERDE:
   FAZ_01 3 · FAZ_03 3 · FAZ_04 2   (F4 henüz üretilmedi → ucuz düzeltme)
⚠️ F5-F9'daki 47 "hair lift" geçişi KASKSIZ sahnelerde; onlar doğru.
```

## § 🔬 J'NİN SEBEBİ — KUBBEYİ KABUL ETMENİN BEDELİ

```
J'nin promptunda vizör VAR (visor ×4, tam geometri cümlesi ×1).
Render "vizör açık" okundu — İKİ geçiş de öyle dedi.

MEKANİZMA [D95 → D146]:
   D95: "optik berrak vizör 'kask yok' diye okunur."
   D146'nın cevabı GÖRÜNÜR ÇERÇEVEYDİ.
   01.09'da kubbe kabul edildi → çerçeve de gitti.
   Geniş/orta planda sorun yok. YAKIN PLANDA çerçevesiz + berrak cam
   = KASK YOK demektir.

⛔ 01.09'da yazdığım "optik kazandı, geometri kaybetti, optiği koru"
   sonucu YAKIN PLANLAR İÇİN EKSİKTİ: çerçeve dekorasyon değildi,
   kaskı yakın planda KASK yapan şeydi.
```

## § SAĞLAM / ŞÜPHELİ / ÖLÇÜSÜZ

```
✅ SAĞLAM (kör + katalog, bağımsız):
   · D'de kask YOK, saç uçuşuyor                          🔴 RED
   · J'de vizör AÇIK okunuyor                             🔴 RED
   · ⭐ SIRT ÜNİTESİ KAYBOLUYOR: B·C·L'de kocaman levha,
     G·I·K'de sıradan küçük sırt çantası                  🔴 RED
     (kör geçiş bunu SORULMADAN buldu — F3'ün ölçmek için
      tasarlandığı şey buydu; F2'de tek klip vardı, ölçülemiyordu)
   · İSTASYON HASARI HER KLİPTE BAŞKA: H tek dev yırtık ·
     I tek orta delik · K çok sayıda küçük delik · L dev sürekli yarık 🔴
   · L'de EL ELE TUTUŞUYORLAR (spec: kollar açık, eller boşa kapanır) 🔴
     ⭐ kör geçiş bunu fazın DUYGUSAL DORUĞU sandı
   · Pufların sürekli/izli olması, kısa koni değil                🔴
   · C'de gergin halat SARKIYOR                                   🔴
   · Işık tarafı 4 klipte ters (B·H·K·L)                          🟡

⚠️ ŞÜPHELİ (yalnız katalog geçişi):
   · omuz vuruşu (G) "doğrulandı" — ama denetçiye SÖYLENMİŞTİ, yankı olabilir
   · gölgelerde dolgu ışığı var
   · "kilitli kameralarda hafif drift" — ⛔ ⑩'DAN DÜŞER: segment yok,
     zaman kodu yok, harf yok. Rubriğin kendi kuralına göre bulgu değil.
     (kör geçiş 1·2·3 için "tracking/trailing" dedi → kareyle bakılmalı)

🔵 YALNIZ KÖR GEÇİŞ (gerçek ama ölçüsüz):
   · ⭐ OMUZ VURUŞU GÖRÜLMEDİ. "İki insan hiç temas ediyor mu?" sorusuna
     cevabı: "Evet — Segment 12'de el ele tutuşuyorlar." Fazın PLANLI tek
     teması (G'deki iki vuruş) ilk izlemede OKUNMUYOR.
     → `GOZLEM ADAY-4`'ün İKİNCİ vakası (F2'de S18'in halat kopuşu).
   · F'de kol beyaz — ne turuncu ne lacivert şerit var
   · G'de saat SOL bilekte (spec: halka sol, saat sağ) — el yönü takas
```

## § 🔴 KARE BEKLEYEN İKİ ÇELİŞKİ

```
① KADININ SIRTI — kör geçiş A ve C'de "standart, alçak profilli yuvarlak
   BEYAZ SIRT ÇANTASI" gördü; katalog geçişi "sırtı düz" dedi. Düz-sırt
   filmin en sert kilidi. İki geçiş ÇELİŞİYOR.
   ffmpeg -ss 4 -i <makara>.mp4 -frames:v 1 sirt_A.jpg

② J'DEKİ ŞERİT SAYISI — kör geçiş "DÖRT parlayan dikdörtgen" gördü;
   katalog geçişi 1 yanık varsayıp "düşmedi" dedi. Dördü yanıksa sayaç
   YUKARI gitmiş demektir (maksimum ciddiyet) ve Çehov 3 hiç ödenmemiştir.
   ffmpeg -ss 74 -i <makara>.mp4 -frames:v 1 serit_J.jpg
```

## § ⑩ ÖNERME KAPISI — filme ait iki sonuç

```
① ÇEHOV 7 ÜRETİLMEDİ. I'de gök kaymıyor — iki geçiş de kaydetmedi.
   KİLİT 10: "bu kurulum S43'ün feda fiziğinin ÖN ŞARTIDIR; merkezkaç
   oradan gelir." ⛔ F4'ün fedasının fiziksel zemini şu an YOK.

② H'Yİ "SAPMA" DİYE OKUMA. Katalog geçişi H'nin deliğini "spec'teki
   ragged puncture değil, dev yırtık" diye kusur yazdı. Asıl bulgu
   BOYUT değil TUTARSIZLIK; ve H istasyonun TEK tam boy görüntüsüdür →
   RE p2 yerine geçecek olan odur. H sapma değil, MASTER adayıdır.
```

## § SKOR — ⛔ KAYDA GEÇMİYOR

```
B geçişinin ortalaması 4,0 (13 kategori; aritmetik DOĞRU: 52/13 = 4,0).
⛔ T tablolarına GİRMEZ: mod V + master yok + faz koşusu.
Karşılaştırma için: F2 = 6,69. Ama iki koşunun rubriği FARKLI
(vizör biçimi F3'te puanlanmıyor) → sayılar doğrudan kıyaslanamaz.
```

## 🔧 FAZ 3 AKSİYON LİSTESİ

```
🔴 BU İKİSİ İÇİN GERİ DÖNÜLMELİ — sebep süreklilik değil, OLAY ÖRGÜSÜ
 ① D (S28) — kask yok. ÖNCE promptu düzelt: "hair lifts inside the
    helmet" cümlesi çıkar ya da saçı kasktan AYRI cümleye taşı.
 ② J (S34) — vizör açık okunuyor. Yakın plan yüz kadrajlarında
    GÖRÜNÜR ÇERÇEVE geri gelmeli (yalnız CU'larda; geniş planlar kubbe
    kalabilir).
 İkisi de TEK FİGÜRLÜ sahne — fazın en ucuz iki yeniden üretimi.

🟠 ÜÇÜNCÜ ADAY (yapısal)
 · I (S33) — Çehov 7 hiç kurulmadı. F4'ün fedası bu kuruluma dayanıyor.
   Zor sahne (iki figür + kayan arka plan) ama F4 ondan besleniyor.

🟡 ÜRETİMDEN BAĞIMSIZ PROMPT DÜZELTMESİ (ucuz, F4 henüz üretilmedi)
 · "hair … inside the helmet" 8 geçiş: F1 3 · F3 3 · F4 2
 · F4'ün iki geçişi ŞİMDİ düzeltilirse aynı kusur F4'te doğmaz

🔵 KABUL EDİLEBİLİR (geri dönüş yok kararı kapsamında)
 · sırt ünitesinin kaybolması · istasyon hasarının değişmesi ·
   ışık tarafı sapmaları · sayaçların düşmemesi · el ele tutuşma
 ⚠️ Ama sırt ünitesi ve istasyon F4-F10 boyunca DEVAM EDİYOR;
   RC ve RE panelleri üretilmedikçe her fazda tekrarlar.
```

---
---

# 📋 KOŞU 4 — FAZ 4 MAKARASI · 02.09.2026 · İKİ MÜHÜRLÜ GEÇİŞ

```
Ham    02_HAM_RAPORLAR/YERCEKIMI_FAZ04_{KOR,KATALOG}_HAM.md
Rubrik FAZ_04_FEDA/FAZ_04_QA_PROMPT.md — A (kör) + B (katalog), ayrı sohbetler
Mod    ⚠️ V — SPEC yok [D129] · master yok [⑪] · T tablolarına GİRMEZ
```

## § ⑪ ÖLÇÜM — 🔴🔴 IZGARA DEĞİŞTİ. BU KOŞUNUN EN BÜYÜK BULGUSU BU.

```
FAZ 1 · 96 s / 12 →  8,0 s    (iki bağımsız geçiş)
FAZ 2 · 96 s / 12 →  8,0 s    (iki bağımsız geçiş)
FAZ 3 · 96 s / 12 →  8,0 s    (iki bağımsız geçiş)
FAZ 4 · 120 s / 12 → 10,0 s   ⛔ (iki bağımsız geçiş, ayrı sohbetler)

Film 120 × 8 s = 16:00 yazıldı. F4 bu ızgarada DEĞİL.
⛔ FİLM ŞU AN İKİ IZGARALI.
```

**Bedeli:** F4'ün sekiz repliğinin zamanları [D122 formülü] geçersiz ·
müzik ölçü hesabı (240 × ölçü ÷ sahne saniyesi) F4 bandında tutmuyor ·
toplam süre artık 16:00 değil · S43'ün %35,0 konumu kayıyor.

⛔ **BU, 30.08'DE AÇILAN VE HİÇ DOLDURULMAYAN KAPININ FATURASIDIR:**
`00_PLAN.md` · `KLİP SÜRESİ = ____`. Dört koşuda dört kez uyardım;
satır boş kaldı, üretim onsuz başladı. → **D124'ün 4. vakası**, ve
öncekilerden farkı: bu ilk kez **film ortasında** oldu.

⚠️ İki beyan ölçüm değildir. Kapatan tek şey:
```
ffprobe -v error -show_entries format=duration -of csv=p=0 <F4 klibi>.mp4
ffprobe -v error -show_entries format=duration -of csv=p=0 <F3 klibi>.mp4
```

## § KİMLİK KAPISI ③ — ✅ GEÇTİ · ON YANKISIZ ÇAPA

```
① turuncu şerit kadında, omuz/kol/bacak   ② adamda turuncu YOK
③ beyaz kapitone silindirik gövde + turuncu tutamaklar
④ iki uçta koyu güneş paneli               ⑤ Dünya kavisi altta
⑥ sert ışık üst SAĞDAN, derin siyah gölge  ⑦ berrak vizör, yüz okunur
⑧ iç mekân: kapitone beyaz silindirik oda, kask serbest süzülüyor,
   dizler göğüste                          ⑨ dışarıda HER karede kask
⑩ ⭐ SIRT ÜNİTESİ: "katı, kapalı, dikdörtgen, düz beyaz paneller,
   yuvarlak köşeler, alt köşelerden iki konik nozul"
   → F2 ve F3'ün kör geçişleriyle AYNI AİLE. ÜÇ FAZ, ÜÇ KÖR GEÇİŞ.
```

## § SIRA SKORU — 4/10 · AMA BU SEFER SAYIYI OKUMA

```
Eşleşen 10 klibin kör sıralaması : I · A · C · D · H · F · E · K · B · L
Gerçek sıra                       : A · B · C · D · E · F · H · I · K · L
Doğru konum                       : C · D · F · L = 4/10
```

⛔ **BU SAYI GÖRSEL ZİNCİRİ ÖLÇMÜYOR — çünkü makarada KATALOGDA OLMAYAN
İKİ KLİP var ve kataloğun İKİ KLİBİ yok.** Kör denetçi hikâyeyi
üretilmemiş bir nedene ve olmayan bir "kurtarma halatına" göre kurdu.
Bozuk malzemeyle ölçülen okunabilirlik, okunabilirlik değildir.

## § 🔴🔴 ASIL BULGU — FEDA ÇEKİLMEDİ, YERİNE BAŞKA ŞEY ÇEKİLDİ

```
MISSING   : G (S43 · FEDA ⭐ TEMA · %35,0)  ·  J (S46 · TUTAMAKLAR)
UNMATCHED : Segment 7  — adam elinde SERT TURUNCU BİR SIRIKLA kadına
                          uzanıyor. Böyle bir sahne katalogda YOK.
            Segment 10 — kadın SAĞLAM gövde boyunca EMEKLEYEREK kalın
                          beyaz bir halat çekiyor. Katalogda YOK.
```

⭐ **G filmin tematik merkeziydi.** Rubriğe tam bu yüzden şunu yazmıştım:
*"'Halat koptu' cevabı gelirse feda ekrana hiç gelmemiştir."*
Kör denetçinin cevabı geldi ve tereddütsüzdü:

> *"This looks ACCIDENTAL. The deciding factor is the massive, jagged
> hole torn into the station hull directly behind them, indicating a
> violent, unplanned structural failure."*

⛔ **O patlama filmde YOK** — kadrajdaki delik F2'den kalma eski hasar.
Kör denetçi, olmayan nedenin yerine **yanındaki en büyük nesneyi neden
yaptı.** → bu **DERS 170** olarak yazıldı (08_QA).

## § SAĞLAM / ŞÜPHELİ / ÖLÇÜSÜZ

```
✅ SAĞLAM (iki geçiş de bağımsız):
   · G ve J ÜRETİLMEDİ; iki senaryo-dışı klip üretildi        🔴
   · OKSİJEN HALKASI HİÇBİR KLİPTE YOK — kör: "giysilerde 0 ışık"
     katalog: "ring entirely absent in all segments"           🔴
     ⛔ Filmin ana sayacı bu fazda hiç var olmadı.
   · İlmek sayısı 3 değil DÖRT, ve C'de de E'de de DÜŞMÜYOR    🔴
   · C ve E FARKLI MALZEME sarıyor (ince gri kordon ↔ kalın
     beyaz halat) — "aynı çekim, tek fark sayaç" kilidi çöktü  🔴
   · İSTASYON HASARI ÇELİŞİYOR: Seg 8'de dev delik, Seg 1·9·10·11'de
     KUSURSUZ gövde                                            🔴
   · Kadının sırtında SIRT ÇANTASI (Seg 8)                     🔴
   · GÖK HİÇBİR GİRDİDE KAYMIYOR → Çehov 7 F3'te de F4'te de
     kurulmadı; üstelik fedanın SEBEBİ oydu                     🔴
   · Adamın şeridi LACİVERT değil gri/siyah                    🟡
   · Eldiven manşetleri klipler arası değişiyor                🟡
   · ⭐ BAYRAK YAMASI (kör geçiş, Seg 4) — F2'de de kör geçiş
     bayrak görmüştü. İKİ FAZ, İKİ KÖR GEÇİŞ, aynı yasak nesne 🔴

⚠️ ŞÜPHELİ (yalnız katalog geçişi):
   · F'te ağız oynuyor (kör geçiş dudaktan söz etmedi)
   · A'da çarpma/sekme yok · B'de kask darbesi yok
   · K'de kol dönmüyor · L'de saat yok, amber leke yok

🔵 YALNIZ KÖR GEÇİŞ (gerçek ama ölçüsüz):
   · yüzde ÇİLLER var ve SOL şakak yarası ANILMIYOR
     → yüz masteri kayması adayı; F5/F6 raporlarıyla çaprazlanacak
   · Seg 12'de göğüste yuvarlak ve dikdörtgen YAMALAR
```

## § ✅ TUTAN — VE BİRİ FİLMİ KURTARDI

```
⭐ DIŞARIDA HER KAREDE KASK VAR. Çapraz kontrol 3'ü F3'ün S28
   felaketinden sonra "denetimin en önemli maddesi" diye işaretlemiştim.
   İki geçiş de tek tek saydı ve TEMİZ çıktı. F3'ün kusuru TEKRARLAMADI.
✅ VİZÖR ŞEFFAFLIĞI 10/10 — optik yarı üçüncü fazda da tuttu.
✅ İTKİ YOK: hiçbir klipte puf yok (şerit 0/4 kilidi tuttu).
✅ Gövde her dış girdide EKRAN-SOLDA ya da altta.
✅ Işık: alçak güneş üst sağdan, jilet kenarlı siyah gölge.
✅ L'de kıvrılma dönüş hızını değiştirmiyor — 0g fiziği doğru.
```

## § ⑩ ÖNERME — düşen iki bulgu

```
① "Segments 7 ve 10 REGENERATION gerektirir, G ve J olmak üzere."
   ⛔ DÜŞER. O iki segment G ve J'ye dönüştürülemez; onlar BAŞKA
   sahnelerdir. G ve J hiç üretilmedi — yapılacak iş dönüştürme değil,
   ÜRETİM. Denetçi eksikliği bir düzeltme işi sandı.
② "TEXT AND DELIVERY HYGIENE: 3" — kör geçiş yalnız bayrak ve yama
   gördü, HARF/RAKAM görmedi ("no letters, digits, text, labels").
   Yasak gerçek ama sınıf farklı: bu bir SİMGE ihlali, metin değil.
   Kategori adı ikisini birleştirdiği için puan yanıltıcı.
```

## § SKOR — ⛔ KAYDA GEÇMİYOR

```
B geçişinin ortalaması 4,7. ⛔ T tablolarına girmez (mod V + master yok).
⚠️ Ayrıca bu skor BOZUK MALZEME üzerinden alındı: iki klip yanlış,
   iki klip eksik. Fazlar arası kıyaslanamaz.
```

## 🔧 FAZ 4 AKSİYON

```
🔴 ÖNCE ÖLÇ — üretmeden, yeniden üretmeden, hiçbir şey yapmadan:
   iki ffprobe satırı. Film 8 s'de mi 10 s'de mi devam edecek?
   Bu karar verilmeden F4 hakkında hiçbir üretim kararı verilemez.

🔴 SONRA ÜRET (yeniden değil, İLK KEZ):
   · G (S43 FEDA) — filmin tematik merkezi, %35,0
   · J (S46) — iki sayacın birlikte düştüğü tek sahne

🟠 KARAR BEKLEYEN
   · Segment 7 (turuncu sırık) ve Segment 10 (emekleme) ne olacak?
     Katalogda yoklar. Kurguda kullanılacaksa plana yazılmalı;
     kullanılmayacaksa iki yuva daha boşalır.
   · Oksijen halkası F4'te hiç yok → F5/F6'da da yoksa sayaç
     zinciri filmin ortasında kopmuş demektir.

🔵 KABUL EDİLEBİLİR ("geri dönüş yok" kapsamında, F2-F3 gibi)
   · istasyon hasarı çelişkisi · sırt çantası · şerit rengi ·
     eldiven manşeti · ilmek sayısı
   ⚠️ Ama bayrak yaması İKİNCİ kez çıktı ve mutlak metin/simge
     kilidini deliyor — bu ayrı bir karar.
```

---
---

# 📋 KOŞU 5 — FAZ 5 MAKARASI · 02.09.2026 · İKİ MÜHÜRLÜ GEÇİŞ

```
Ham    02_HAM_RAPORLAR/YERCEKIMI_FAZ05_{KOR,KATALOG}_HAM.md
Mod    ⚠️ V — SPEC yok · master yok · T tablolarına GİRMEZ
```

## § ⑪ ÖLÇÜM — IZGARA SAPMASI TEK SEFERLİK DEĞİL, REJİM

```
F1 · F2 · F3 →  8,0 s      F4 · F5 → 10,0 s
```
İki fazda üst üste, dört bağımsız geçişte. **D124'ün 5. vakası.**
⭐ Bu artık "bir faz kaydı" değil: **araç F3 ile F4 arasında değişti.**
   Ve aynı sınırda ikinci bir şey daha başladı → aşağıya bak.

## § KİMLİK KAPISI ③ — ✅ GEÇTİ

```
Kör geçişin yankısız çapaları: turuncu şerit (omuz/kol) · beyaz kapitone
koridor + turuncu tutamaklar · yuvarlak lomboz + gece Dünya'sı ·
mühürlü kapak + gözlem camı + ölü modül · kırmızı kapak · yeşil gösterge ·
kask serbest süzülüyor · dizler göğüste · yalnız · 12/12 kask YOK.
⚠️ ÇAPA DEĞİL, KUSUR: yara SOL şakakta değil **SAĞ kaşın üstünde** —
   iki geçiş de aynı yeri söyledi. Yüz masteri kaymış.
```

## § ⭐⭐ BU KOŞUNUN EN DEĞERLİ BULGUSU — İKİ GEÇİŞ ÇELİŞTİ

```
KATALOG GEÇİŞİ : "TEXT DISCIPLINE: 10 · Zero characters found."
                 "no rogue characters generated on the panels."
KÖR GEÇİŞ      : Seg 9  (1:24) caption "Cabin pressure falling, seal the hatch."
                 Seg 12 (1:54) caption "Capsule power nominal."
```

⛔ **Makarada iki GÖMÜLÜ ALTYAZI var** ve filmin mutlak metin kilidi
"no subtitle, no caption" diyor — maksimum ciddiyet.
Katalog geçişi göremedi çünkü rubrik ona **nereye bakacağını saydı**
("her paneli, gösterge bankasını, düğmeyi, kapağı kontrol et"). İhlal
panelde değildi; **karenin üstündeydi.** → **DERS 171 yazıldı.**

⭐ Tek geçişli bir denetimde bu ihlal rapora HİÇ girmezdi — üstelik
"10/10, kusursuz tutuldu" diye kayda geçecekti.

## § 🔍 VE ALTYAZININ SEBEBİ ÖLÇÜLDÜ

```
F5'in 12 sahnesinden YALNIZ İKİSİNİN video promptu tırnak içinde replik
taşıyor: S57 (STATION AI) · S60 (CAPSULE AI).
Altyazı çıkan iki segment: tam olarak o ikisi. → 2/2.
Yasak promptta VARDI: "no subtitles/caption" F5'te 24 kez.

FİLMİN TOPLAM MARUZİYETİ: video promptunda tırnaklı replik = 33/120
   F1 5 · F2 4 · F3 6 · F4 7 · F5 2 · F6 2 · F7 4 · F8 3
   ÜRETİLMEMİŞ: F7 4 + F8 3 = 7 sahne ← ücretsiz düzeltme penceresi
```
→ `GOZLEM ADAY-7`. ⭐ Çözüm filmin içinde zaten var: F6 KİLİT 27
(*"promptta cümle yazılmaz, sesin tonu tarif edilir"*).

## § SIRA SKORU — 3/12 · VE SEBEBİ TONUN TERS DÖNMESİ

```
Kör : A · B · E · I · C · D · F · J · H · K · G · L
Doğru: A · B · C · D · E · F · G · H · I · J · K · L
Doğru konum: A · B · L = 3/12   (F2 8/12 · F3 5/12 · F4 4/10)
```

⛔ **Ama asıl bulgu sayı değil, kör denetçinin ANLATTIĞI HİKÂYE:**

> *"...flooding the corridor with flashing orange lights and a warning
> that cabin pressure is falling. **Hit by a violent decompression wind**,
> she fights to lock down the vessel... she flees down the corridor...
> **closing her eyes in relief**."*

```
TASARLANAN : filmin EN SESSİZ fazı. Görünmez kaçak. Kimse cevap vermiyor.
             Sonu SAHTE zafer — "gülümsemez" yazılı.
ÇIKAN      : alarm + rüzgâr + panjur + tuş takımı + kaçış + rahatlama.
```

⭐ **Fazın tek fikri — GÖRÜNMEZ KAÇAK — hiç görünmedi**; kör denetçi
kaçağı üç YANLIŞ kanaldan öğrendi: altyazıdan, saçı savuran rüzgârdan,
yanıp sönen turuncudan. Kilit *"tek kanıt kayış ucudur"* diyordu —
kör geçişin "kendiliğinden hareket eden şeyler" listesinde **kayış yok.**

## § SAĞLAM / ŞÜPHELİ

```
✅ SAĞLAM (iki geçiş de bağımsız):
   · S51'de SAÇ RÜZGÂRDA savruluyor (0g + durgun hava kilidi)     🔴
   · S51'de bilekte SİYAH SAAT (bu fazda görünmemeli)              🔴
   · S51'de YÜZ BAŞKA: daha genç, pürüzsüz, yara YOK               🔴
   · S54'te halka DEĞİL: kalın bant, 5 yanık kare (2/6 olmalı)     🔴
     ⛔ Filmin sayacı bu fazda YANLIŞ PROP.
   · S54 paneli ÖLÜ değil, ÇALIŞAN tuş takımı                      🔴
   · S58'de KIRMIZI KAPAĞA DOKUNULUYOR ve çekiliyor                🔴
     ⛔ ÇEHOV 6, 47 sahne erken harcandı.
   · S59'da kadın KORİDORDA, kapsülün İÇİNDE değil                 🔴
   · S60'ta yeşil ARKADAN geliyor, alttan değil                    🔴
   · S60'ta GÜLÜMSÜYOR — "gülümsemez" kilidi                       🔴
     ⛔ SAHTE zafer GERÇEK zafer okundu; orta nokta ters döndü.
   · yara SOL şakak değil SAĞ kaş üstü                             🟡
   · S49'da yüz/S60'ta yüz tutarlı ama S51 kopuk                   🔴

🔵 YALNIZ KÖR GEÇİŞ (gerçek ama ölçüsüz):
   · ⭐ S52'de camı kapatan SİYAH PANJUR — spec'te böyle bir şey yok;
     katalog geçişi bu segmenti "YELLOW, Earth lights visible" diye
     geçti ve panjuru hiç anmadı (D171'in ikinci kanıtı)
   · S60'ta SAÇ DÜMDÜZ, yerçekimi varmış gibi
   · S60'ta koltuğa KEMERLE bağlı
   · S57'de ışık STEP DEĞİL, YANIP SÖNÜYOR (katalog "doğru" dedi)
```

## § ✅ TUTAN

```
⭐ KAPSAM 12/12 — eksik yok, kopya yok, katalog dışı yok. F3'ten beri ilk.
⭐ İKİ CAM AYRIMI TUTTU — lombozda gezegen, kapak camında ölü modül.
   Rubriğin bu faza özel kurduğu testi geçti.
✅ 12/12 KASK YOK · 12/12 YALNIZ · boş koltuklar boş
✅ 12/12 KAMERA KİLİTLİ, sıfır hareket
✅ EKRAN YÖNÜ tutarlı (hep ekran-sola) · koridor B·H·I'de aynı koridor
✅ GÖRÜNÜR GAZ YOK · süzülen nesneler düz çizgide, hiçbiri oturmuyor
✅ E (ölü modül) iki geçişte de övüldü
```

## § SKOR — ⛔ KAYDA GEÇMİYOR

```
Katalog geçişi 5,38 verdi. ⛔ T'ye girmez (mod V + master yok).
⚠️ Üstelik METİN 10/10 puanı GEÇERSİZ (D171) → gerçek ortalama daha düşük.
```

## 🔧 FAZ 5 AKSİYON

```
🔴 ÖNCE: ALTYAZI. Master'da gömülüyse kurguda silinemez — o iki klip
   yeniden üretilir ya da altyazı bandı kırpılır.
   ffmpeg -ss 84 -i <makara>.mp4 -frames:v 1 altyazi_57.jpg
   ffmpeg -ss 114 -i <makara>.mp4 -frames:v 1 altyazi_60.jpg

🔴 IZGARA KARARI hâlâ verilmedi (KOŞU 4'ten devrediyor). İki fazın
   ölçüsü artık aynı: 10 s. Film 8'de mi 10'da mı devam edecek?

🟠 F7 ÜRETİLMEDEN BEDAVA: 7 sahnenin tırnaklı repliği kaldırılır
   (F7 4 · F8 3). Teknik F6 KİLİT 27'de zaten yazılı.

🔵 KABUL EDİLEBİLİR (önceki fazlardaki karar kapsamında)
   · yara yeri · S51'in yüzü/rüzgârı/saati · S54'ün propu · S59'un odası
   · S60'ın yeşili
   ⚠️ AMA İKİSİ AYRI KARAR İSTER:
     ① S60'ta GÜLÜMSEME — orta noktanın anlamını tersine çeviriyor
     ② S58'de KIRMIZI KAPAĞA DOKUNMA — Çehov 6'yı erken harcıyor
```

---
---

# 📋 KOŞU 6 — FAZ 6 MAKARASI · 02.09.2026 · İKİ MÜHÜRLÜ GEÇİŞ

```
Ham  02_HAM_RAPORLAR/YERCEKIMI_FAZ06_{KOR,KATALOG}_HAM.md
     100 s / 10 parça / 10,0 s · Mod ⚠️ V · T tablolarına GİRMEZ
```

## § ⭐⭐ EKSİK-İKİ TESTİ GEÇTİ — RUBRİK TASARIMININ KANITI

```
Denetçiye HANGİ İKİ girdinin iptal edildiği SÖYLENMEDİ.
Yalnız "tam iki harf yaz, fazla ya da eksik çıkarsa YÜKSEK SESLE söyle" dendi.
    MISSING: I, J        UNMATCHED: yok
→ DOĞRU İKİ KLİP DÜŞMÜŞ. Operatör yanlış sahne atlamamış.
⭐ F2'de tam bunun tersi olmuştu (C atlanıp B iki kez üretilmişti) ve o
  zaman ancak katalog 12 beklediği için yakalanmıştı. Kapı iki yönde de
  çalışıyor.
```

## § ⭐ İKİ KARIŞTIRILABİLİR ÇİFT DE AYRILDI

```
F ↔ L : "F'de yeşil sabit, gözler açık · L'de ışık üç aşamada ölür,
        gözler kapanır" → doğru ayrıldı
A ↔ K : "A'da halka PANELDE ve sönük · K'da BİLEKTE" → doğru ayrıldı
```
Depoda ilk kez rubrik denetçinin teşhis güvenini ölçtü ve ölçüm tuttu.

## § 🔴🔴 ALTYAZI — VE HİPOTEZ ÇÜRÜDÜ

```
İKİ GEÇİŞ DE GÖRDÜ (F5'te yalnız kör geçiş görmüştü — D171 işledi):
   Seg 1 (A/S61)  "Main propellant, empty. Orbital burn unavailable."
   Seg 6 (F/S66)  "Contact confirmed. Please maintain trajectory."
   Seg 9 (K/S71)  "Oxygen 11%. Warning."
   Seg 5 (E/S65)  kadranda okunur çentik/rakamlar
```

⛔ **S66'DA PROMPTTA TIRNAKLI CÜMLE YOKTU.** O sahne tam olarak KİLİT 27'ye
göre yazılmıştı — ses anlaşılmaz, ona hitap etmez. **Model bir cümle
UYDURDU ve bastı.** Ve uydurduğu cümle sahnenin anlamını tersine
çeviriyor: "sana hitap ediyorum, rotanı koru."

```
F6: tırnaklı sahne 2  ·  çıkan altyazı 3
ZAMAN ÇİZGİSİ  F1-F3 (8 s) altyazı 0 · F4 (10 s) 0 · F5 2 · F6 3
→ oran ARTIYOR ve tırnak sayısını AŞTI. → GOZLEM ADAY-7 revize edildi.
```

## § SIRA SKORU 2/10 — VE SEBEBİ ÜÇÜNCÜ KEZ AYNI

```
Kör : F · C · G · D · H · A · K · B · E · L
Doğru: A · B · C · D · E · F · G · H · K · L      → 2/10 (D · L)
```

⛔ **Kör denetçi sıralamasını İKİ RENDER KUSURU üzerine kurdu:**
> *"Hand injury: Clean → Cut. **High confidence**"*
> *"Face injury: Clean → Scratched. **High confidence**"*

Filmde ne el yarası ne yüz çiziği var; ikisi de süreklilik kusuru.
⭐ **D170'in 3. vakası** — ve yeni bilgi: kusur yalnız kafa karıştırmıyor,
izleyicinin zaman algısını **örgütlüyor.** (F3: kask → "ölüm saati" ·
F4: delik → "kaza" · F6: yaralar → "yaralanma saati".)

## § SAĞLAM (iki geçiş de bağımsız gördü)

```
· H (OVERVIEW) BOZUK — kadın koltukta değil, ORTADA BAĞDAŞ KURMUŞ
  havada; pencere ORTADA (ekran-sol olmalı); iki koltuk pencereye
  SIRTI dönük; push-in YOK.                                     🔴🔴
  ⛔ Filmin TEK Overview sahnesi ve kilidi "kıpırdamaz"dı.
· B'de kollar AŞAĞI HİÇ BASTIRILMIYOR — yalnız havada titriyor.  🔴
  ⛔ Fazın fiziksel fikri ("çökmek ister, bedeni izin vermez") YOK.
· K'da halka SAĞ bilekte ve 4 yanık (SOL, 2→1 olmalı)            🔴
· L'de SAĞ alında kırmızı çizik (F ve G'de yok)                  🔴
· SOL şakak yarası HİÇBİR karede yok                             🔴
· E'de sağ elde açıklanamayan kesik + kadranda okunur rakamlar   🔴
· L tam karanlıkla bitiyor — tek amber lamba kalmıyor            🔴
· E ve K'da SERT KENARLI gölge (yumuşak kaynak kilidi)           🟡
· C'de camın ardında uydu/panel var, dönen mavi parça değil      🟡
· A'da parmak yay çizmiyor, ortaya basıp kenara vuruyor          🟡
```

## § ✅ TUTAN

```
⭐ 10/10 kapsam · MISSING tam olarak I ve J · UNMATCHED sıfır
⭐ İki karıştırılabilir çift de doğru ayrıldı
✅ 10/10 yalnız · boş koltuklar boş · kask yok · eller çıplak
✅ 10/10 dudak kapalı · hiçbir lamba yanıp sönmüyor
✅ D (boş koltuk) KUSURSUZ — iki geçiş de övdü: kayışlar süzülüyor,
   hiçbiri mindere oturmuyor
✅ Saç kalkıp duruyor (C·F·G·L) · yerçekimi beden dili YOK
✅ L'nin üç aşamalı ışık ölümü tuttu ve tek yönlü kaldı
```

## § SKOR — ⛔ KAYDA GEÇMİYOR

```
Katalog geçişi 3,7 verdi (film içindeki en düşük). Mod V + master yok.
```

## 🔧 AKSİYON

```
🔴 H (S68 OVERVIEW) — filmin tek Overview'u ve tamamen bozuk. Yeniden
   üretilirse ilk sırada bu.
🔴 ALTYAZI — A · F · K karesi. Gömülüyse kurguda silinemez.
🟠 B (S62) — fazın fiziksel fikri hiç görünmedi.
🔵 KABUL EDİLEBİLİR: yara/çizik · halka yeri · sert gölge · C'nin uydusu
```

---

# 🔎 FAZ 7 ÜRETİM ÖNCESİ KONTROL · 02.09.2026

```
✅ 12 sahne · 24 prompt · 12/12 KİLİTLİ KAMERA (hiç hareket yok)
✅ politika sözlüğü uyarısı YOK · uzunluklar bant/tavan içinde
⚠️ D139: 2 promptta sırt için pozitif tarif yok (satır 527, 1334)
⚠️ kurulum sayısı 12 (bant 6) — belgeli sapma ailesi
⛔ B5 BLOCK — depo geneli, F1-F7'nin yedisinde de aynı; plan seviyesi

🔴🔴 AMA BİR ŞEY VAR VE FİLMİN GERİ KALANINDAKİ EN BÜYÜK RİSK BU:

F7 HALÜSİNASYON FAZIDIR. KİLİT 30, ölmüş adamın sesinin meşruiyetini
ÜÇ KANALDAN işaretliyor:
   ① MİKS  — ses hoparlörden gelmez, filtresizdir, her yöndendir
   ② GÖRÜNTÜ — S77 hoparlör ızgarasının makrosudur ve KAYNAK BOŞTUR
   ③ GÖVDE — B ekranda 0 kare

⛔ GÖMÜLÜ ALTYAZI BU ÜÇÜNÜ BİRDEN YOK EDER.
   Altyazı, bir filmin ekrana koyabileceği EN BELGESEL nesnedir:
   "bu söylendi, resmen, ve işte dökümü" der.
   → halüsinasyon GERÇEK bir telsiz çağrısı olarak okunur
   → S77'nin boş ızgarası (fazın kanıtı) anlamsızlaşır
   → S84'ün CENTRAL CHOICE'u "karar verdi" değil "talimatı uyguladı" olur

F7'de tırnaklı replik taşıyan DÖRT sahne var ve ÜÇÜ halüsinasyon:
   S76  "Told you. Half of it's storytelling."
   S78  "Landing rockets are rockets, engineer. Point them the wrong way."
   S81  "Go home. Take the watch with you."
   S84  "OXYGEN SIX PERCENT. RECOVERING."   (makine)

⭐ VE DÜZELTME KÜÇÜK: video promptlarında sesi anlatan TOPLAM DÖRT
   BEAT SATIRI var, o dördü de yukarıdaki sahnelerde.
   Öneri: beat satırı YALNIZ KAMERANIN GÖRDÜĞÜNÜ anlatsın.
   "2s — ses şunu der: ..."  →  "2s — gözleri bir kez oynar ve durur."
   Ses zaten post'ta; filmin kendi kuralı bunu söylüyor.
   ⚠️ F6 kanıtladı ki tırnağı silmek TEK BAŞINA yetmiyor (S66) —
     ses SATIRINI silmek gerekiyor.
```
