# ✅ THE_SINKING_HARBOR — ÜRETİM ÖNCESİ KONTROL (18 madde)

**Kaynak:** `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md`
**Koşuldu:** 04.10.2026 · akış adım 10 · üretim 0 kare
**Kural:** her madde ya ✅ (kanıt satırıyla) ya ⚠️ (ölçülmüş sapma + gerekçe)
ya ⬜ (üretimde ölçülür) olur. ⛔ Boş bırakılan madde YAPILMAMIŞ sayılır [D74].

---

## 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### A0 — HİKÂYE ONAYI ✅
```
☑ 00_ANALIZ/00_HIKAYE_ONAYI.md VAR · ONAY: 04.10.2026 · sahip · TUR 1/3 (tarihli)
☑ sahne satırı 24 = PLAN'daki sahne sayısı 24 (S1 … S24, atlama yok)
☑ SAHNELER bölümünde jargon YOK — ölçüldü: ㉙ `\bD\d{1,3}\b|\bnovum\b|kurulum
  \s+[A-Z]\b|\bkilit` deseni temiz. ⚠️ "kilit" kelimesi hikâyenin NESNESİ
  olduğu için sahne satırlarında sahibin kendi ikinci terimi kullanıldı:
  "taşıyıcı bağlantı". Gerekçe SÖZCÜK NOTU'nda, SAHNELER bölümünün DIŞINDA.
☑ SAPMA bölümü dolu — ÜÇ sapma yazılı ve her biri gerekçeli (bkz. 00_HIKAYE_ONAYI)
☑ LOGLINE 23 kelime (≤25) · NEDEN İZLENİR tek soru · BEDEL iki aşamalı ve
  KLİP NUMARALI (K80 pencere · K94 ışıklar)
☑ ADAYLAR bloğu dolu · 0.7a ATLANDI ve gerekçesi yazılı: hikâye SAHİBİN
  (ÖN PLAN rejimi · 00_ON_PLAN/ klasörü var) — 02_KONSEPT §0⑥ ile tutarlı
```

### A1 — Yasak ↔ anlatım çelişkisi ⭐ EN PAHALI HATA ⚠️ ÖLÇÜLDÜ, ÇÖZÜLDÜ
```
☑ "No readable text, letters, digits or symbols on any surface" 184/184
  promptun NEGATIVE'inde var (çekirdek ④).
⚠️ AYNI DOSYALARDA EKRAN/GÖSTERGE İÇERİĞİ TARİF EDİLİYOR — SEKİZ KLİPTE:
  K30 · K39 · K43 · K47 · K54 · K68 · K71 · K85.
  ÇÖZÜM (çelişki değil, KARAR): hiçbirinde VERİ tarif edilmiyor; yalnız
  ÖLÇEKSİZ BİÇİM tarif ediliyor ve her birinde o biçimin ölçeksizliği
  POZİTİF cümleyle yazılı:
     "exactly two plain curves ... There is no scale, no tick, no label and
      no marking of any kind anywhere on the panel."
  ⭐ Yani gösterge bir GRAFİK değil, bir EĞRİ. İki eğrinin BİRBİRİNE GÖRE
  durumu (hizalı → biri geride → kesişiyor → ayrışıyor) olayı taşır; hiçbir
  yerde sayı okunmaz. Bu, D45/D138'in istediği biçimdir: yasak değil MALZEME.
⚠️ İKİNCİ VAKA: K54'te "three plain lit readouts ... each a short bar of pale
  light" — bar sayısı (3) olay, içeriği YOK. Aynı karar.
☑ Üç göğüs şekli de aynı kararla: rozet DEĞİL, malzemenin kendisinde KABARTMA
  (02_KONSEPT §1 · sahibin "rozet" talebinin fizikle uzlaştırılması)
```

### A2 — Sahne sayısı tutuyor mu ✅
```
☑ başlık 24 sahne / 96 klip ↔ dosyalarda 24 `# 📍 SAHNE` bloğu, 92 `## 🎬 KLİP`
  prompt bloğu + 4 kesim kartı = 96
☑ numaralarda atlama yok: S01…S24 · K01…K96
☑ ÖLÇÜLDÜ: `grep -ho "Clip [0-9]* of [0-9]*"` → X değeri 184/184 promptta **96**
  (tek değer, sapma yok)
☑ bölüm başına prompt: B1 16 (8 klip, K01-K04 kart) · B2-B8 24 (12 klip) = 184
```

### A3 — Süre tutuyor mu ✅
```
☑ 96 klip × 10,000 s = 960,000 s = 16:00 — iddia edilen süre 16 dk ✅
☑ bölüm başına 12 klip × 10 s = 120 s = 2:00 · 8 bölüm × 2:00 = 16:00 ✅
☑ sahne başına 4 klip × 10 s = 40 s · 24 sahne × 40 s = 960 s ✅
⬜ GERÇEK SÜRE üretimde ffprobe ile ölçülür; klip süresi ARAÇTAN ölçülür [D124] —
  bugün 10 s bir PLAN birimi olarak yazıldı, araç ayarı olarak DOĞRULANMADI
```

### A4 — Yasaklı sahne tipi var mı ⚠️ ÜÇ VAKA, ÜÇÜ DE KARARA BAĞLANDI
```
· araç/kapak/airlock BİNİŞ-İNİŞ hareketi [D69] → ÜÇ VAKA BULUNDU:
  "K56: iç kapak hareketi kadrajda, FİGÜR GEÇİŞİ kadraj dışı — D69 ① gereği.
   Kadrajda kapak + iki duran figür var; kimse kapıdan GEÇMİYOR (04.10)"
  "K89: dış kapak hareketi kadrajda, FİGÜR GEÇİŞİ kadraj dışı — aynı karar.
   İki figür klibin başında da sonunda da hücrenin İÇİNDE (04.10)"
  "K90: iç kapak AÇILMA hareketi kadrajda; figürler son saniyede açıklığa
   DOĞRU adım atar, geçiş bir sonraki klibin ÖNCESİNDE olur — D69 ① (04.10)"
  ⭐ Üçünde de hareket KAPAĞIN, figürün değil. Sahibin planındaki olay korundu.
· tek ışıklı loş iç mekâna GİRİŞ [D69] → YOK. S04 koridoru iki tavan lambalı
  ve figürler zaten içeride başlıyor.
· aynalı-yansıtıcı yüzey önünde tek karakter [D20 · D69] → YOK. Vizör 92/92
  klipte BERRAK ve "zero reflection" (`vizor` negatifi); ayna hiç yok.
· novum'u TÜRETİLMİŞ optik fenomen taşıyor [D73] → YOK. Taşıyıcı FİZİKSEL bir
  yüzey: koyu kıvrım. Gölge · yansıma · kostik · parlama deseni DEĞİL.
· novum'u bir YOKLUK taşıyor [D76] → ⚠️ SINIRDA, ÖLÇÜLDÜ:
  K84'ün olayı "katman BIRAKIR" — bir kavramanın yokluğu gibi okunabilir.
  "K84: bırakma kadrajda POZİTİF nesneyle yazıldı — gevşemiş katman ve onun
   kadraj dışına çıkan tek bol kıvrımı KADRAJDA; yokluk değil, yeni BİÇİM.
   Karşılaştırma çapası K34/K38'in gerilmiş-gevşemiş çifti — D76 (04.10)"
· jenerik / başlık kartı / kapak çıktısı [D34 · D70 · D72] → YOK. Başlık
  post katmanı (KAPAK dosyası), 92 klibin hiçbirinde harf yok.
```

### A5 — FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI ✅
```
☑ RİSK ADIYLA YAZILI: **D56 MEDIUM LOCK — "batan liman" modele SU üretiyor.**
  (02_KONSEPT §5 A5 · risk kartı 1)
☑ POZİTİF BİÇİM DÖRT SAYI TAŞIYOR:
  ① ortam "a dense hydrogen-helium cloud layer" — 92/92 PHYSICS cümlesinde
  ② "anything let go falls an arm's length in about a third of a second" —
     0,5 m / 0,32 s, s = ½gt² ile DOĞRULANABİLİR aritmetik
  ③ katman yüzeyi "as dry as sheet metal and as matt as soot" (R2 sayfası)
  ④ yasaklı sözcük sayısı **11** — §1c MEDIUM LOCK sözlüğü, her birinin
     yerine geçen kelime yazılı (sinking→losing altitude · dive→descent ·
     deep→far below · wave→load wave · current→drift · floats→is held ·
     surface→face/skin · tissue→layer · tentacle→fold · swirl→travel · wet→dry)
☑ SPEC'in göz kapısı bu sayıları ölçülebilir cümleyle tekrarlıyor (QA_SPEC 🅐)
⚠️ ÖLÇÜM KENDİ İDDİAMI ÇÜRÜTTÜ VE DÜZELTİLDİ (04.10.2026):
  184 promptun pozitif gövdesi 21 sözcüklük MEDIUM LOCK deseniyle tarandı.
  İLK KOŞU: **`sinking` 6 pozitif gövdede bulundu** — K44 (image · video · CA)
  ve K94 (image · video · CA). Oysa `sinking` §1c sözlüğünün BİRİNCİ yasaklı
  kelimesi ve filmin ADINDA geçtiği için en kolay kaçan kelime.
  DÜZELTME: → `going down` (K44) · `settling` (K94). İKİNCİ KOŞU: **0 — TEMİZ**.
  ⭐ DERS: yasaklı sözcük listesi yazmak onu uygulamaz. Liste ancak BETİKLE
     taranırsa kapıdır; elle yazılan 184 promptun altısı listeyi ihlal etti ve
     hiçbir kapı bunu söylemedi (`prompt_kontrol` MEDIUM LOCK sözlüğü tutmuyor).
     → 04_UYARI_NOTLARI §4a aday 24
```

---

## 🔴 B. FİLMİN DORUĞU YAZILMIŞ MI

### B1 — Doruk anı bir sahnenin İÇİNDE mi ✅
```
☑ DORUK: S21 · K84 (830,000-840,000 s = 13:50-14:00)
☑ O klibin VİDEO promptunda an GERÇEKTEN TARİF EDİLİYOR:
  "the dark layer's edge never draws in around it again" + TIMELINE 4,0 s'de
  "the layer's slack fold opens further behind it"
☑ İKİ SAHNENİN ARASINA DÜŞMÜYOR: K84 S21'in 4/4 klibi, kendi sahnesinin içinde
  ve kendi IŞIK/SES kilidini taşıyor
☑ Doruk sahnenin SON klibi olduğu için bölüm sınırına da düşmüyor (B7'nin
  son klibi K84 ↔ B8'in ilk klibi K85 ayrı sahneler, S21|S22)
```

### B1b — Katmanlı dünya ise ışık takvimi var mı ✅
```
☑ FİLM BİR EKSENDE İLERLİYOR: İRTİFA. Liman alçalıyor, her sahne bir önceki
  sahneden daha derinde.
☑ KATMAN IŞIK TAKVİMİ TABLO HALİNDE: 02_KONSEPT §2b LAYER LIGHT SCHEDULE
☑ MONOTONİK Mİ — ÖLÇÜLDÜ: kubbe (yukarıdaki parlak bulut) sayacı
  6/6 → 5/6 (S07) → 4/6 (S15) → 3/6 (S16) → 2/6 (S18) → 1/6 (S24)
  ve kehribar (aşağıdaki kaynak) ters yönde güçleniyor.
  ⭐ TEK İSTİSNA VE GEREKÇESİ: S24'te kubbe yeniden AÇILIYOR — ama liman için
  değil, GEMİ için. Kubbe 1/6 kalır (liman), vault gemi üstünde açılır.
  Yani eksen kırılmıyor: iki nesne iki yönde gidiyor [D74 kaydı].
☑ Kolon sayacı da monotonik: 6 → 5 (S08) → 4 (S15) → 3 (S16) → 2 (S18) →
  1 (S24 · K93) → 0 (K94). Yedi klipte sayılabilir.
```

### B2 — Bedelli seçim var mı ✅
```
☑ KARAKTER SEÇİYOR: pilot, K48'de "Take us down." der. Bu bir TEPKİ değil —
  K45/K46/K47'de kural, sonuç ve yöntem konuşulur, K48'de KARAR verilir.
☑ NEYİ KAYBEDİYOR: limanı. Kilitlerin açılması için limanın daha da
  alçalması gerekiyor ve bu alçalma GERİ ALINAMIYOR.
☑ KAYIP HANGİ KLİPTE GÖRÜLÜYOR — İKİ AŞAMA:
  ① K80 (796 s) pencerenin TAMAMI örtülür → yukarıdaki parlak bant gider
  ② K94 (930 s) son alan ışığı SÖNER → liman terk edilmiş olarak görünür
☑ ⭐ Seçimin kendisi de kadrajda: K48'de pilot konuşur, iki dinleyen CEVAP
  VERMEZ. Sessizlik onayın biçimi.
```

### B3 — Tema hangi sahnede EKRANA çıkıyor ✅
```
☑ TEMA: İLK TEMAS · tanım cümlesi: "Temas bir karşılaşma değil, çektiğin
  şeyin seni de çektiğini fark etmektir." (TAKAS kalıbı DEĞİL)
☑ QA_SPEC'te düz `TEMA:` satırı VAR ve `TEMA SAHNELERİ: S06 S07 S09 S10 S11
  S16 S20 S21 S24` — dokuz sahne (㉑③ ölçtü, GEÇTİ)
☑ EKRANA ÇIKTIĞI KLİP: K34 (ilk kez bir şey KARŞILIK verir) ve K79 (kural
  ölçekte kanıtlanır). İkisi de replik taşımaz — tema SÖYLENMİYOR, OLUYOR.
☑ Tema cümlesi hiçbir replikte geçmiyor — ölçüldü: 38 replikte "contact",
  "touch", "notice", "pull back" yok
```

### B4 — Açı yayı yazıldı mı ✅
```
☑ KURULUM İSKELETİ 92 harf, 26 kurulum — 03_SAHNE_SIRALAMASI §4
☑ ÖLÇEK KADEMESİ 6 (EWS · WS · MWS · MS · CU · ECU)
☑ AÇI TİPİ 4 (eye-level · low · high · over-the-shoulder)
☑ ARDIŞIK AYNI KURULUM: 0 çift (betikle ölçüldü · kamera.py)
☑ ARDIŞIK ÇİFT HATASI: 1 — K23(K) → K24(Z), açı/azimut farkı <45 ve aynı
  mekân. ⭐ BİLİNÇLİ: ikisi de liman dışı EWS/WS ve olay tam o eşlikten
  çıkıyor (aynı yere iki ölçekten bakmak). Gerekçe §3'te yazılı.
☑ 2+ kademe atlayan çift 31 · şok bandı (≥3 kademe) 3: K09→K10 · K41→K42 ·
  K57→K58. Üçü de vuruş noktası ya da belirişe denk geliyor.
☑ BÖLÜM BAŞINA AÇI TİPİ ≥3 — 8/8 bölüm GEÇTİ (ölçüldü)
⚠️ BÖLÜM BAŞINA DÖNÜŞ ORANI: B2 %42 · B3 %42 ✅ ↔ B4 %17 · B5 %25 · B6 %17 ·
  B7 %17 · B8 %17 ⛔ bant %40. **AÇIK KALIR VE GEREKÇESİ ÖLÇÜLDÜ:**
  04_UYARI_NOTLARI §4a aday 20 — B4'ün kısıtlı optimumu 2/12'dir ve 3/12'ye
  çıkmanın tek yolu §3'ü (≥1 ölçek kademesi) ihlal etmek. İki kılavuz aynı
  anda sağlanamıyor. ⚠️ FIX, BLOCK değil.
```

### B5 — İSTEK · ENGEL · BEDEL · MUHATAP ✅
```
☑ İSTEK   sondayı limandan sökmek — film başlamasa da var olan bir İŞ
          (⛔ "anlamak/görmek/fark etmek" DEĞİL)
☑ ENGEL   kilitler yük altında açılmıyor; yükü kaldırmanın tek yolu limanı
          daha da alçaltmak. ⭐ Ortam meşru karşı güç (02.09 kararı).
☑ BEDEL   liman · K80 (pencere örtülür) + K94 (ışıklar söner) — KLİP NUMARALI
☑ MUHATAP ikinci ve üçüncü insan (mühendis + operatör) · ayrıca KENDİ GEÇMİŞ
          KARARI: K22'de pilot "kaldırmayı artır" der, K48'de kendi emrini
          tersine çevirir
```

### B5b — AYRILIK ✅ (üç insanlı plan)
```
☑ AYNI FİKİRDE OLMADIKLARI AN: D07 (K22 · pilot "Increase lift.") ↔
  D12 (K36 · mühendis "Less force. Just for a moment.")
☑ İki kart ≥3 davranış satırında AYRIŞIYOR (02_KONSEPT §7d · üç karakter kartı)
☑ İSTEK ÇAPRAZI: mühendis pilottan KUVVETİ AZALTMASINI istiyor (K36);
  operatör pilottan ONU DIŞARIYA ÇIKARMAMASINI değil, YETKİYİ ALMASINI
  istiyor (K53 "I have the lift controls here."). Üçü de birbirinden bir şey
  istiyor → hiçbiri figüran değil.
```

### B5c — ÜRETİM SIRASI ✅
```
☑ PLAN'da ON HALKALI üretim sırası yazılı [D168]
☑ İLK HALKA: K84 (DORUK) · ikinci: K48 (merkezî seçim) · üçüncü: K96 (kapanış)
☑ ÜRETİM DEFTERİ bu sırayı tekrarlıyor ve "sıra baştan başlarsa ikinci klip
  ÜRETİLMEZ" kuralı yazılı
⛔ KAPI 0 AÇILMADI: referans paketinin 7 sayfası TASLAK → hiçbir klip
  üretilemez (REFERANS_PAKETI §7 · D168)
```

### B6 — POLİTİKA SATIRI ve ANLAM MALİYETİ ✅
```
☑ POLİTİKA SATIRI: 02_KONSEPT §6 — K18 nötr tarif + üç kadraj kararı
☑ ⑲ KİMLİK YIĞINI: kişi başına öznitelik ≤3 (giysi · kask · eldiven);
  ten · saç · yaş hiçbir promptta YOK. ⚠️ TEK İSTİSNA: K31 ve K35'te
  "an older man's face" — YAŞ bir öznitelik. Sayım orada 3'e çıkıyor, tavanı
  AŞMIYOR; ve o iki klipte YÜZ konudur (⑲'un kendi istisnası).
☑ ANLAM MALİYETİ: 92/92 klipte kask KAPALI ve vizör BERRAK. Berrak vizör
  politika reddi riskini DÜŞÜRÜR (D79 · 01.09 TUR 3) ve devamlılığı kilitler.
☑ Kadrajda konuşan ağız YOK: 34 replikli klibin 34'ünde konuşanın ya ağzı
  kadraj dışında ya kaskı çevrili (K45 · K55 · K96 bu yüzden böyle kuruldu)
```

---

## 🟠 C. SAYISAL KİLİTLER YAZILDI MI ✅
```
☑ YERÇEKİMİ tek sayı film boyunca: 1,00 g — 92/92 PHYSICS cümlesi BİREBİR aynı
☑ DÜŞME TABLOSU: 0,5 m ≈ 0,32 s (s = ½gt²) · ⛔ ivme değil ÇIKIŞ SÜRESİ yazılır [D127]
☑ OPTİK: 26 kurulumun 26'sında kadraj eni + ana nesne px'i ölçüldü;
  D179 (ana nesne ≥100 px) 26/26 GEÇTİ. En düşük: K57/K61 figür 108 px.
☑ SAYILABİLİR NESNELER: 6 kolon · 4 kenet · 3 bağlantı · 3 koltuk · 2 eğri ·
  1 pim. Hepsi tek karede sayılabilir ölçekte (en küçüğü 203 px).
☑ KELİME BANDI: image 169-247 (bant 100-250) · video 234-300 (bant 120-300) —
  184/184 prompt BANT İÇİNDE, ölçüldü
☑ NEGATİF TAVANI ㉗: 184/184 prompt ≤11 cümle · insansız 29 klipte bant 900
  karakter (en yüksek 897+39=... ölçüldü, aşım 0)
```

## 🟠 D. RİSK SAYIMI ✅
```
☑ RİSK KARTI SAYISI: 13 (02_KONSEPT §5) → 5+ olduğu için KİLİT TAVANI ≤20
☑ DERS KİLİDİ SAYISI: 20 — tavan TAM DOLU (㉕ GEÇTİ)
☑ UYGULANMAYAN KİLİTLER: 9, hepsi gerekçeli (01_QA_DERS_HASADI §1b)
☑ ÖN-OTOPSİ: beş arıza modu × olasılık/etki → GO (02_KONSEPT §5 sonu)
☑ MALZEME AZALTILMADI — 24 sahne · 92 klip · 26 kurulum · 38 replik korundu
  (14.09 kararı: "malzeme azalt" LOCKED_PULSE'u vana tamirine indirdi)
```

## 🟡 E. QA'YA HAZIRLIK ✅
```
☑ QA_SPEC 🅐 🅑 🅒 🅔 blokları dolu
☑ 🅔 E BLOĞU: altı makine kapısı, her biri `DOĞRULANDI ffmpeg 8.1 · 04.10.2026`
  satırıyla — silencedetect · blackdetect · signalstats · freezedetect ·
  fps/scale · ffprobe. Altısı da KURU KOŞUYLA sınandı [D142].
☑ ÇAPA ÜÇLÜSÜ: K41 (beliriş) · K48 (merkezî seçim) · K84 (doruk)
☑ ANCHOR BEATS + REPLİK SAATLERİ D122 formülüyle (elle yazılmadı)
☑ İNSAN ŞERİDİ: 92 karakter · 29 insansız klip — klip verisinden HESAPLANDI
☑ FİNAL VURUŞ KANITI: dört kenet AÇIK · K92 · 280 px · ffmpeg komutu yazılı
☑ DÖNGÜ KANITI: K05 ↔ K96 (B ↔ B) · iki ffmpeg komutu yazılı
☑ QA BİRİMİ §2.8: 4 PART (2 bölüm = 24 klip) + TAM FİLM koşusu ·
  kör noktalar K24|K25 · K48|K49 · K72|K73 yazılı
⬜ rapor_kontrol.py koşulmadı — master YOK, üretim 0 kare
```

---

## 📋 TEK SAYFALIK ÖZET

```
18 MADDE: ✅ 15 · ⚠️ 3 (A1 çözüldü · A4 karara bağlandı · B4 DÖNÜŞ açık)
⬜ ÜRETİMDE ÖLÇÜLECEK: klip süresi [D124] · gerçek süre (ffprobe) ·
   referans paketinin yedi kabul kapısı maddesi · rapor_kontrol.py
⛔ ÜRETİM BAŞLAYAMAZ: KAPI 0 açılmadı (referans sayfaları TASLAK)
⛔ AÇIK KALAN TEK KAPI BULGUSU: B4'ün DÖNÜŞ oranı — ölçülmüş kılavuz
   çelişkisi, §3 ile §4b aynı anda sağlanamıyor [04_UYARI §4a aday 20]
→ prompt_kontrol.py klasör modu: ⛔ 0 BLOCK ✅
```
