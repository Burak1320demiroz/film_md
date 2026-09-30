# ✅ GUNES_MEZARI — ÜRETİM ÖNCESİ KONTROL (18 MADDE)

**Kaynak:** `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`
**Ne zaman:** PLAN + Bible + 48 prompt yazıldı, **tek kare üretilmedi.**
**Tarih:** 25.09.2026 · **Koşan:** yazım · **Süre:** ~20 dk · **Maliyet:** 0

> ⛔ Bu dosya bir ÖZET değildir: 18 maddenin her biri DOSYA ve SATIR göstererek
> cevaplanır. Cevabı "evet" olan madde de nereye bakıldığını yazar, yoksa
> denetim yapılmamış sayılır [D74 mantığı].

---

## 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### ☑ A0 — HİKÂYE ONAYI
```
□→☑ 00_ANALIZ/00_HIKAYE_ONAYI.md var · ONAY: 25.09.2026 · sahip · TUR 2/3 (tarihli)
□→☑ satır sayısı = sahne sayısı: S1…S7 = 7 satır · PLAN 7 sahne ✅
    ⚠️ ÇOK KLİPLİ REJİM: onay satırı SAHNE başınadır (klip başına değil) ve her
    satır kendi uzunluğunu taşır — "S3 (3 klip · 1:30–2:00)".
□→☑ SAHNELER'de jargon yok: D-numarası 0 · "novum" 0 · kurulum harfi 0 · "kilit" 0
    (㉙ `kilit` kökünü Türkçe çekimde de arıyor: onaylı S6 satırındaki "kilitte"
    bu yüzden "anahtar çubuğu geri alınamaz biçimde harcanır" olarak yeniden
    yazıldı ve NOT satırına KELİME düzeltmesi olarak kaydedildi — hikâye aynı)
□→☑ SAPMA: PLAN'ın sahne haritası onaylı satırlarla BİREBİR (3 6 3 2 3 4 3);
    sapma yok, bu yüzden SAPMA bölümü boş ve yeniden onay gerekmiyor
□→☑ LOGLINE 23 kelime (≤25) · NEDEN İZLENİR tek soru · BEDEL sahne numaralı (S5 · S6)
□→☑ ADAYLAR bloğu dolu (B, C: logline + neden elendi) · 02_KONSEPT §0⑥ fikir turu
    kaydı yazılı (0.7a KOŞMADI — hikâye SAHİBİN; gerekçe NOT satırında) ·
    §5 ÖN-OTOPSİ KARAR satırı: GO
```

### ☑ A1 — Yasak ↔ anlatım çelişkisi ⭐ EN PAHALI HATA
```
□→☑ "no readable text" 48/48 promptta VAR
□→☑ Hiçbir ekranın/göstergenin İÇERİĞİ tarif edilmiyor: sayaç yok, yüzde yok,
    gösterge yok. K11'in arşiv levhası bir GÖRÜNTÜ döngüsü gösterir (eldiven +
    kol), METİN değil; K15'in çekirdeği kaburgalı bir silindirdir, ekranı YOK
    (referans paketi RP negatifi: "no screens, no indicators, no lamps and no
    readouts on either object").
□→☑ Bilgi metinsiz kanala taşındı: kapanan halka (K21) · sönen lamba sayısı
    (K17: üç lamba) · kırağı pası merdiveni (K0→K1→K2) · hilal yanık izi (K08/K11)
⭐ Filmde HİÇBİR yüzeyde harf/rakam/amblem/arma/rütbe yok; imparatorluk yalnız
  BİÇİM olarak var (üç halka ↔ üç taş kemer, aynı kaburga dili).
```

### ☑ A2 — Sahne/klip sayısı tutuyor mu
```
⚙️ ÖLÇÜLDÜ (25.09.2026, elle sayılmadı):
   `# 📍 SAHNE` başlığı        BÖLÜM_1 = 3 · BÖLÜM_2 = 4   → toplam 7 ✅
   `## 🎬 KLİP`  başlığı       12 + 12                     → toplam 24 ✅
   `Clip n of 24.`             24 + 24 = 48 prompt          → X = 24 doğru ✅
   00_SAHNE_TABLOSU.md satırı  24 ✅ (㉚)
   SAHNE PLANI: 3 6 3 2 3 4 3  toplam 24 ✅ · en uzun sahne 6 (≤6) ✅
   Numara atlaması YOK: K01…K24 kesintisiz · S01…S07 kesintisiz
⚠️ ÇOK KLİPLİ REJİM: SAHNE(7) ≠ KLİP(24) ≠ PROMPT(48) olması NORMALDİR; kart
  "24 sahne" derken bu rejimde 24 KLİP okunur (§2.3 · 22.09.2026).
```

### ☑ A3 — Süre tutuyor mu
```
24 klip × 10,0 s = 240,0 s = 4:00 ✅ — QA_SPEC 🅑 bloğundaki ızgara ile aynı
⬜ AMA: 10,0 s bir PLANDIR, ölçüm değil [D124]. Araç gerçekten kaç saniye
   veriyor — ÜRETİM DEFTERİ §0⑶'te randevu olarak açık. Sayı değişirse
   ızgara (replik 24,0/90,0 s · müzik 72 BPM ölçü çizgileri) yeniden hesaplanır,
   prompt dosyaları DEĞİL (üretimden sonra prompt güncellenmez).
```

### ☑ A4 — Yasaklı sahne tipi var mı [D69 · D73 · D76 · D34/D70/D72]
```
24 klip tek tek tarandı; iki tip DOĞDU ve ikisi de dersin öngördüğü biçime döndü:
  K04: iniş HAREKETİ kadraj dışı — gövde "already down", rampada hareket yok,
       motor/egzoz/iniş ışığı yok — D69 ① gereği (25.09)
  K10: loş iç mekâna GİRİŞ hareketi kadraj dışı — "a step inside the doorway",
       ağırlık arka bota oturmuş, yürüyüş yok; klip bir BEKLEYİŞ — D69 ② gereği (25.09)
Kalan tipler YOK:
  · aynalı/yansıtıcı yüzey önünde tek karakter → YOK; vizör yalnız ÜST KENARDA
    tek spekülar çizgi taşır ve "no environment reflected in it" yazılı [D20 · D69]
  · novum TÜRETİLMİŞ optik fenomen mi → HAYIR, fiziksel bir küre [D73]
  · novum bir YOKLUK mu → HAYIR, taşınan bir nesne [D76]
  · jenerik/başlık kartı/kapak çıktısı klip olarak → YOK; kapak ayrı dosya ve
    KURGUYA GİRMEZ [D34 · D70 · D72]
  · K06 bir kapıdır ama İÇERİ GİRİLMEZ: klip sonunda kapı bir el genişliği
    açık, kadın dışarıda — giriş S03'e ertelendi
```

### ☑ A5 — FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI [D192]
```
□→☑ Risk ADIYLA yazılı: KAFESTEKİ KÜRE (02_KONSEPT §5 A5 · göz kapısı G1)
□→☑ POZİTİF biçim DÖRT SAYI taşıyor:
      ① halkaların iç açıklığının 4/5'i (çap oranı)
      ② yüzeydeki parlak hücre 4 saniyede bir kenardan kenara geçer
      ③ korona/hüzme/hale 0 kare
      ④ küre ile halka arasındaki hava PUSSUZ (yoğunluk 0)
□→☑ SPEC göz kapısı G1 aynı dört sayıyı ölçülebilir cümleyle tekrarlıyor
□→☑ Yalnız NEGATIVE'e bırakılmadı: dördü de POZİTİF gövdede, 5 klipte (K01 ·
    K02 · K03 · K21 · K22) ve referans paketi RO sayfasının KABUL SINAVI'nda
⛔ Yasak biçim değildir: "no fireball" tek başına ateş topunu ENGELLEMEZ.
```

---

## 🔴 B. FİLMİN DORUĞU YAZILMIŞ MI

### ☑ B1 — Doruk anı bir klibin İÇİNDE mi
```
DORUK = K21 (S06 · 4/4 · 200-210 s). Olay TEK klibin içinde başlıyor ve bitiyor:
  0,0 s halkalar KAPALI · 4,0 s halkalar açılır ve küre kendi genişliğini ~2 s'de
  aşarak ayrılır · 6. s alt kenar üst kadraj çizgisini geçer · 8. s kadrajda YOK.
⛔ İki klip ARASINA düşmüyor: ayrılma K20'de başlamıyor, K22'de tamamlanmıyor.
D127: hızlanma değil ÇIKIŞ SÜRESİ yazıldı (ölçülebilir).
```

### ☑ B1b — Katmanlı dünya ise ışık takvimi
```
Film İRTİFA ekseninde ilerlemiyor; ZAMAN/IŞIK ekseninde ilerliyor. Takvim
PLAN Lighting Bible'da 7 SATIRLIK TABLO hâlinde yazılı (sahne = satır):
  S1 kafes ışığı → S2 fener + parçalanmış ay → S3 kule lambası → S4 fener →
  S5 gemi lambaları → S6 fener + yuva ışığı → S7 yeni güneş
MONOTONİK Mİ: ✅ tek yönlü. Sönen hiçbir kaynak geri yanmıyor (gemi pencereleri
K18'den sonra karanlık, yuva K19'dan sonra bir daha sönmüyor), ve yeni güneş
açıldıktan sonra hiçbir klip yalnız-fener ışığına DÖNMÜYOR.
⚠️ Yanlış pozitif notu: anahtar ışık 13 klipte ELDE TAŞINAN bir fenerdir;
  "arkasında lambalar" ifadesi ⑮ KAMERA_ARKADA'yı tetiklediği için kaçınıldı.
```

### ☑ B2 — Bedelli seçim var mı
```
□→☑ SEÇİM: K16 — kalkış kolunu BIRAKIR (tepki değil, karar; kol K17-K18'de
    hâlâ kadrajda ve hâlâ çalışır durumda — reddedilen seçenek görünür kalıyor)
□→☑ KAYIP: ① güç çekirdeği (K17 — gemi bir daha kalkmaz) ② anahtar çubuğu
    (K20 — kilit onu YUTAR, tek kullanım, geri alınamaz)
□→☑ KAYIP GÖRÜLÜYOR: K17 (ışıklar sırayla söner) · K18 (gemi tamamen karanlık,
    arkada) · K23 (karanlık geminin yanında duruyor) — üç klipte, üçü de EKRANDA
⛔ "Anlamak/fark etmek" bedel sayılmadı; iki fiziksel nesne kalıcı olarak gitti.
```

### ☑ B3 — Tema hangi klipte EKRANA çıkıyor
```
□→☑ TEMA tek kelime: FEDAKÂRLIK · TANIM cümlesi (TAKAS kalıbı DEĞİL):
    "Bir şeyi geri veren, geri veremediklerinin önünde bekler."
□→☑ Novum kelimesi geçmeden tek cümleyle söylenebiliyor ✅ (yukarıdaki cümle)
□→☑ ÜÇ MOTİF KANALI ve ekrana çıktığı klipler:
      ① ELDEN ÇIKAN NESNE  K17 (çekirdek) · K20 (çubuk) — sahip olduğunu veriyor
      ② SAYILI IŞIK        K17 (üç lamba söner) · K22 (ışık kenarı iner)
      ③ KAPANMAYAN EL      K16 (kolu bırakır) · K23 (eller açık kalır, kapanmaz)
□→☑ B2 ÇAPRAZ: bedelli seçimin yaşandığı klip (K16/K17) bu listede VAR ✅
```

### ☑ B4 — Açı yayı yazıldı mı
```
□→☑ KURULUM İSKELETİ PLAN'da yazılı (24 harf):
    C I C I F G F D C A C D C D F H F H F D I C A C
□→☑ Ardışık HER çift bandı tutuyor: 23/23 · ihlal 0 · ⭐ 1 bilinçli ŞOK
    (K20→K21: H→... değil, D→I — ölçek + açı sıçraması doruğa ayrıldı)
□→☑ Kurulum SAYISI 7 (A C D F G H I) — bandın içinde
□→☑ AÇI TİPİ sayısı 5 ≥3 ✅ (göz hizası · üst açı · alt açı · OTS · profil)
□→☑ Derece yazan satırlar abartı bandında: üst açı 15° · alt açı · 20° ·
    abartılı değer (45°+ eğim, 90° tepe) YOK
□→☑ DORUK en yüksek kontrast sıçramasını taşıyor: K21 = I (24mm · 25,0 m · h12,0)
□→☑ DÖNÜŞ oranı 10/24 = %41,7 ≥ %40 ✅ · her dönüş kamera cümlesini BİREBİR
    kopyalıyor + işaret cümlesi taşıyor ("the same position, height and lens as Clip n")
⚠️ KÜME ARANMAZ: ÇOK KLİPLİ SAHNE rejiminde KÜME yoktur (22.09.2026); yerine
  sahne içi kamera kilidi ve CONTINUOUS ACTION geçti.
```

### ☑ B5 — İSTEK · ENGEL · BEDEL · MUHATAP
```
İSTEK:   çekirdeği kaideye bağlamak ve küreyi salıvermek — bir İŞ, film
         başlamadan önce de vardı ("anlamak/görmek" DEĞİL)
ENGEL:   TEK engel, ENERJİ — kaide sağlam ama ölü; gezegende çalışan tek
         kaynak geminin çekirdeği. Ekranda üç olgu: K13 (kol sonuna kadar
         iniyor, hiçbir şey olmuyor) · K14 (yatak bir silindir için işlenmiş) ·
         K19 (ilk oturma TUTMUYOR). İki başarısız deneme: K13 · K19.
BEDEL:   çekirdek (K17) + anahtar çubuğu (K20) ⭐ SAHNE NUMARALI
MUHATAP: kendi geçmiş kararı — K11'in arşiv levhasındaki hilal yanıklı eldiven
         ve K20'de kilidin yuttuğu anahtar çubuğu. Yankı EKRANDA: K23'te
         aydınlanmış sokak boş, kimse çıkmıyor.
```

### ⊘ B5b — AYRILIK (yalnız iki insanlı planlarda)
```
UYGULANMIYOR: filmde tek insan var (insanlı 18 klipte tam 1, 6 klipte 0).
⛔ Bu satır "atlandı" değil "kapsam dışı"dır; ikinci bir insan eklenirse
  AYRILIK sahnesi ZORUNLU olur ve hikâye onayına dönülür.
```

### ☑ B5c — ÜRETİM SIRASI [D168]
```
□→☑ Sıra PLAN'da ve ÜRETİM DEFTERİ §0⑴'de yazılı ve DRAMATİK SIRA DEĞİL:
    K21 (DORUK) → K17 (BEDEL) → K24 (FİNAL) → K01 (HOOK) → kalan 20
□→☑ Üretilecek İLK klip = K21 = doruk ✅ (K01 DEĞİL — sıra baştan başlamıyor)
□→☑ İPTAL KAPISI yazılı: K21 üç denemede tutmazsa PLAN B — küre kadraja HİÇ
    girmez, K22 birincil kanıt olur
```

### ☑ B6 — POLİTİKA SATIRI ve ANLAM MALİYETİ
```
□→☑ POLİTİKA SATIRI yazıldı (PLAN §POLİTİKA · 02_KONSEPT §6)
□→☑ EN RED-RİSKLİ KARE: K21 — ve gerekçesi yazılı
□→☑ KART 12 açık mı: filmde ÇOCUK yok, gerçek kurum yok, silah yok, gerçek kişi
    yok, milliyet yok. TEK hassas unsur bir KAYDIN İÇERİĞİ ("there are children
    here") — çocuk EKRANDA YOK, ses bir kayıttır, insan 0. Kart 12 bu yüzden
    SES ekseninde açıldı, görüntü ekseninde değil.
□→☑ Alınan HER önlem ÜÇ SATIR taşıyor (ÖNLEM · MALİYET · TELAFİ) — 5 satır,
    02_KONSEPT §6 tablosu
□→☑ Milliyet · gerçek kurum · gerçek kişi adı planın hiçbir yerinde YOK ✅
    (imparatorluk adsız; "the fleet" bile yazılmıyor, yalnız BİÇİM ortak)
```

---

## 🟠 C. SAYISAL KİLİTLER YAZILDI MI

```
⚙️ PLAN'ın SAYISAL KİLİT tablosu 14 satır; bu maddenin istediği altı eksen:
İNSAN SAYISI   insanlı 18 klipte tam 1 · 6 klipte 0 (K01·K02·K04·K11·K21·K24)
               ⚙️ prompt gövdelerinden ÖLÇÜLDÜ 25.09.2026 (şerit: --1-111111-111111111-11-)
KASK TAKVİMİ   kapalı 24/24 klipte · açılan 0 klip · vizör TEK düz pane, kalın
               koyu çerçeve, optik BERRAK (kubbe/balon/aynalı 0)
ÖLÇÜ           gemi ~24 gövde boyu · aydınlık pencere 1 (kapı boyunda) · halka 3 ·
               taş kemer 3 · kilit yuvası 4 · mühür halkası 2 · anahtar çubuğu
               1 ön kol · küre/halka iç açıklığı 4/5 · ay ~1 kol boyu tabak
               ⛔ METRE prompt gövdesine GİRMEZ [D138] — oran gövde boyu cinsinden
YERÇEKİMİ      0,38 g · 0,90 bar · 95 K — bıraktığı şey ~1 saniyede yere varır ·
               kaldırılan kırağı yarım saniyede oturur · rüzgâr kumaşı KIPIRDATMAZ
SIVI TEMASI    YOK — 24/24 klipte sıvı 0; eriyen buz/su NEGATIVE'de yasaklı
               (KART 1 AÇILMAZ · 02_KONSEPT §1)
CANLI ANATOMİSİ tek canlı: filiz — 1 adet · üç yaprak · bir parmak boyu · hareket 0 ·
               yalnız K24'te. İnsan dışı hayvan/varlık YOK (KART 2 kapsam dışı)
```

---

## 🟠 D. RİSK SAYIMI

```
□→☑ 02_RISK_KARTLARI.md açıldı ve malzeme listesi işaretlendi (00_OKUMA_CIZELGESI)
□→☑ RİSK SAYISI: 11 / 13   ← payda 02_RISK_KARTLARI RİSK TOPLAMI (14.09.2026)
□→☑ 5+ risk çıktı → KİLİT TAVANI ≤20 uygulandı: PLAN'ın DERS KİLİTLERİ bloğu
    20 satır, 20 ayrı D numarası (㉕ tavanı) ✅
□→☑ Tavanı aşan kilitler PLAN'ın UYGULANMAYAN KİLİTLER bölümünde GEREKÇEYLE
    (malzeme AZALTILMADI — 14.09 reformu)
```

---

## 🟡 E. QA'YA HAZIRLIK

```
□→☑ QA SPEC yazıldı: GUNES_MEZARI_QA_SPEC.md (~356 satır)
      🅐 künye (SCENE 7 ≠ CLIP 24 · DIALOGUE 2 · VIRAL 2)
      🅑 ızgara + replik saatleri FORMÜLLE (24,0 s · 90,0 s) + FİNAL VURUŞ 236,0 s
        + DÖNGÜ KANITI K01↔K24 + insan şeridi + davranış şeridi
      🅒 sayısal kilitler (hepsi sayılı, novum sınırı dâhil)
      🅔 altı MAKİNE KAPISI — her biri `DOĞRULANDI ffmpeg 8.1 · 25.09.2026`
        (freezedetect · signalstats · blackdetect · silencedetect · ebur128 · select)
      GÖZ KAPILARI 5 (G1 küre · G2 vizör · G3 kadraj terki · G4 hilal iz · G5 son kare)
      YANLIŞ-POZİTİF DUVARI 10 satır
□→☑ Replik var → `DIALOGUE_CRITIQUE_PROMPT.md` koşulacak (bu dosyadan sonra)
□→☑ prompt_kontrol.py klasör modu: ✅ GO · 0 BLOCK
```

---

## 📋 TEK SAYFALIK ÖZET

```
18 MADDE:  ☑ 17 geçti · ⊘ 1 kapsam dışı (B5b — tek insan) · ⛔ 0 açık
BU KOŞUDA BULUNAN GERÇEK HATALAR (üretimden ÖNCE, maliyet 0):
  ① İNSAN ŞERİDİ 23 karakterdi, 24 olmalıydı — ve insansız klip 4 değil 6
     (K04 ve K21 de insansız). QA_SPEC · PLAN · 02 · 04 · 01 düzeltildi.
  ② DAVRANIŞ ŞERİDİ K04'e G, K21'e R veriyordu; ikisinde de kadrajda beden YOK.
     İkisi "—" oldu, oranlar yeniden sayıldı (G 5/18 = %27,8).
  ③ Yüzü olmayan 20 klibin NEGATIVE bloğu "real skin pores and sweat" istiyordu
     ve aynı blokta "no bare skin anywhere" yazıyordu — eldiven klibinde açık
     bilek davetiyesi. Yüzsüz klipte o cümle kaldırıldı (üreteç koşulu).
  ④ Fenerin yeri "to her right" yazılıydı (nesne-göreli KONUM) — üç klipte
     kesmeler arasında taraf değiştirirdi; "at screen left" oldu.
⬜ ÜRETİME KALAN ÖLÇÜMLER (tahmin YAZILMADI): klip süresi [D124] · vizör biçimi
   (2. klipte, kubbe çıkarsa ÜRETİM DURUR) · küre okuması (K21) · ⭐viral 3 aday
```

---

## 🔎 EK KOŞU — D59 GREP'İ (üretimden önce, zorunlu)

```
⚙️ 26.09.2026 · pozitif gövdeler (NEGATIVE öncesi) tarandı, 48 prompt:
  hang / suspend / float / hover / frozen / stopped        →  0  ✅
  still                                                    → 41, hepsi MEŞRU:
      24 × "the approved still from this clip's IMAGE prompt" (şablon İSMİ)
      17 × ZARF "hâlâ": "the three rings are still closed" · "frost is still
           crusted along the lip" · "the loop still running" · "the hull dark"
  ⛔ D59'un yasakladığı anlam ASKIDA/HAREKETSİZ DURMAKTIR ("hangs still",
     "frozen in place"); yukarıdaki 17 kullanım SÜREKLİLİK zarfıdır ve
     hareketsizlik iddia etmiyor. Kök sayımı sıfıra indirilemez çünkü "the
     approved still" şablonun kendi ismidir — silinirse START FRAME satırı bozulur.
  ⚙️ Yasak ifadeler: "exact last frame" 0 · "previous clip" 0 · seamless 0 ·
     bubble 0 · dome 0 · emblem 0 · badge 0 · insignia 0
```
