# 📊 THE_TETHERED_MASS — FİLM QA KAYDI

> **Format:** `yatay_2_dk_filmler`
> **Kayıt Tarihi:** 11.09.2026
> **SPEC:** `yatay_2_dk_filmler/THE_TETHERED_MASS/THE_TETHERED_MASS_QA_SPEC.md` (VAR)

---

## 🗂️ HAM RAPOR KAYITLARI
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_KARE_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_DEVAMLILIK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_SES_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_HIKAYE_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_ARKA_PLAN_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_FIZIK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_AKSIYON_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_EFOR_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_KADRAJ_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_OYUNCULUK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_ISIK_HAM.md`
- `kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TETHERED_MASS/THE_TETHERED_MASS_HOOK_HAM.md`

---

## ①.5 BETİK KOŞUSU (`rapor_kontrol.py`)

```
SPEC: yatay_2_dk_filmler/THE_TETHERED_MASS/THE_TETHERED_MASS_QA_SPEC.md → ①/④/⑥/⑦/⑧ + ⑨-⑫ için MOD D ZORUNLU
PLAN: 16 sahne (THE_TETHERED_MASS_BOLUM_1.md + THE_TETHERED_MASS_BOLUM_2.md)

① KARE       🚨 GEÇERSİZ  (SPEC var, MOD V koşulmuş [D129] + SCORES SUMMARY okunamadı)
② DEVAMLILIK ✅ GO        (Mod V tasarımdır · Skor: 6.2/10)
③ SES        🚨 GEÇERSİZ  (SCORES SUMMARY okunamadı)
④ HİKÂYE     🚨 GEÇERSİZ  (SPEC var, MOD V koşulmuş [D129] + SCORES SUMMARY okunamadı)
⑤ ARKA PLAN  ⚠️ ŞARTLI    (Mod V tasarımdır · Skor: 6.7/10 · SEVERITY TALLY uyuşmazlığı [D161])
⑥ FİZİK      ⛔ TEKRAR    (SPEC var, MOD V koşulmuş [D129] + SEVERITY TALLY uyuşmazlığı [D161])
⑦ AKSİYON    ⛔ TEKRAR    (SPEC var, MOD V koşulmuş [D129] + SEVERITY TALLY uyuşmazlığı [D161])
⑧ EFOR       ⛔ TEKRAR    (SPEC var, MOD V koşulmuş [D129] + SEVERITY TALLY uyuşmazlığı [D161] + COST CURVE sabit)
⑨ KADRAJ     🚨 GEÇERSİZ  (Plan sadakati merceği SPEC'siz / MOD V koşulmuş [D190/D184])
⑩ OYUNCULUK  🚨 GEÇERSİZ  (Plan sadakati merceği SPEC'siz / MOD V koşulmuş [D190/D184])
⑪ IŞIK      🚨 GEÇERSİZ  (Plan sadakati merceği SPEC'siz / MOD V koşulmuş [D190/D184])
⑫ HOOK      🚨 GEÇERSİZ  (Plan sadakati merceği SPEC'siz / MOD V koşulmuş [D190/D184])

⑤ ÇAPRAZ KAPI (12 RAPOR):
🚨 KESME YAYILIMI 18 > 1 → Parti GEÇERSİZ (KARE 14, HİKÂYE 15, AKSİYON 14, OYUNCULUK 14 kesme vs DEVAMLILIK 32, ARKA PLAN 32, EFOR 31, IŞIK 31 kesme [D107])
🚨 TESLİM ŞÜPHESİ — plan 16 sahne yazıyor, 4 mercek 32 sahne saydı [D188]
▶ Parti GEÇERSİZ: hiçbir satır T tablolarına girmez (D107 / D129 / D188 / D190).
```

---

## 📝 RAPOR BULGULARI VE DERS DEĞERLENDİRMESİ

### ① KARE & FİZİK BULGULARI (HAM - 4.9/10 Ortalama)
- **Fizik & İvme İhlali (0:06, 0:35, 1:15):** Kopan çelik halat kinetik sönümleme olmadan sarmal yay gibi süzülüyor; itici roket egzozu uzay vakumunda konik dağılmak yerine atmosferik bulut gibi birikiyor.
- **Parçacık & Malzeme Erimeleri (1:54 - 🔴 BLOCKER):** Kontrol kolu etrafındaki kırık cam parçacıkları kareler arası eriyerek biçim değiştiriyor.
- **Negatif Kural İhlali (2:40 - 🔴 BLOCKER):** Final karesinde gömülü metin ("THE TETHERED MASS") beliriyor (Seri negatif çekirdek ihlali).

### ② DEVAMLILIK BULGULARI (HAM - 6.3/10)
- **Ekipman & Kask Kaybı (S21 vs S22):** 01:30'da kaskı kapalı astronot 01:34'te kask çıkarma hareketi olmadan bir anda çıplak kafa beliriyor.
- **Kostüm Değişimi & Göğüs Paneli:** S2 (00:04), S6 (00:22), S11 (00:44) ve S18 (01:16) sahnelerinde göğüs ışık paneli 4 farklı geometriye bürünüyor.
- **Kir & Aşınma Sıfırlanması:** Wasteland bölümünde kirli suit bacakları tesise (S13) ve kar alanına (S21) girişte tertemiz parlak beyaza sıfırlanıyor.

### ③ SES BULGULARI (HAM - 6.7/10)
- **Ses Kimliği:** 17 replikli anlatım logunda Voice A (Operator) ve Voice B (Suit AI) ses kimliklerini ve comms eşitliğini %100 koruyor.
- **Mekanik Akustik & Efor Uyumsuzluğu:** Fiziksel efor sahnelerinde anlatıcı sesi durağan stüdyo tonunu koruyor; mekanik foley ayak sesleri metal catwalk adımlarına tam kilitlenmiyor.

### ④ HİKÂYE BULGULARI (HAM - 7.4/10)
- **Kanca & Çıkış:** İlk 10 saniyede doğrudan halat kopması ile yüksek dinamik başlangıç (9/10).
- **Tematik Bedel:** İstasyondan ayrılma kararı ve acil durum camını kırıp kolu çekme seçimi dramatik olarak işlenmiş (8/10).
- **Pacing & İzleyici Kaybı Risk:** S7 (boş koridor) ve S8 (roket nozulu) sahneleri üst üste gelerek ivmeyi düşürüyor (1:05-1:25 retention riski).

### ⑤ ARKA PLAN BULGULARI (HAM - 6.7/10)
- **Tek Düzlem Paralaks Kilidi (S5 · 0:17):** Gemi gövdesi ve uzaktaki dağlar kamera kaymasında tek parça 2D katman gibi hareket ediyor.
- **Topoloji Sıçraması (S21 vs S23):** 1:30'daki karlı dağ sırtı 1:39'da aniden düz çam ormanı havzasına dönüşüyor.
- **Ufuk Çizgisi Kayması (S1 vs S5):** Çorak arazinin arkasındaki dağ silueti geniş açılarda şekil değiştiriyor.

### ⑥ FİZİK BULGULARI (HAM - 6.4/10)
- **Işık & Gölge Tersinmesi (L8 · 0:58):** Karakterin gölgesi doğrudan ana ışık kaynağı olan merkeze doğru düşüyor.
- **Patlama & Kapı Hızı/Ölçeği (L12 vs L3/L4):** Acil durum kapısı kapanışta 1.68 kat büyüyor ve açılış hızına göre 3 kat daha hızlı kapanıyor (2.45 m/s vs 0.84 m/s).
- **Kütlesiz Kıvılcım Düşüşü (L11 · 1:50):** Tavandan düşen kıvılcımlar yerçekimi ivmesi yerine 2.08 m/s sabit hızla süzülüyor.

### ⑦ AKSİYON BULGULARI (HAM - 7.4/10 · VERDICT: ACTION READS)
- **Baskı & Vuruş Netliği:** 12 vuruştan 11'i okunabilir; B7 (1:10-1:29) roket nozulu püskürmesi itki kontrolü ile belirsiz bağ kuruyor.
- **Kopan Halat Kadrajı (B11 · 2:10-2:19):** Kopan halat ucu salınım anında çerçevenin alt kenarından anlık olarak çıkıyor (-3 Puan).
- **Cam Temas Engeli (B9 · 1:50-1:59):** Eldivenli parmakların kırık cam ile teması kol tabanı arkasında gizleniyor (-3 Puan).

### ⑧ EFOR BULGULARI (HAM - 1.0/10 · VERDICT: NOBODY PAYS)
- **Cezalandırılmayan Reaktör Patlaması (S20 · 01:25 - 🟠 MAJOR):** Genişleyen yok edici patlama dalgasına karşı beden hiçbir siper, çömelme veya geri itilme tepkisi göstermiyor.
- **Sıfır Ağırlıklı Kıyafet Yükü (S1–S21 · 00:00–01:34 - 🟠 MAJOR):** Ağır EVA kıyafeti eklem direnci, siper buğulanması veya ağırlık merkezi kayması üretmiyor; kumaş gibi ağırlıksız hareket ediyor.
- **Biyomlar Arası Taze Sıfırlanma (00:00–02:25 - 🟠 MAJOR):** 32 sahne boyunca dağ, kar ve patlama yürüyüşlerinde solunum ve kas yorgunluk eğrisi sabit 0 seviyesinde kalıyor.

### ⑨ KADRAJ BULGULARI (HAM - 8.2/10 · VERDICT: MINOR DRIFT)
- **Kilitli Çekimlerde İleri Sürüklenme (0:02, 0:30, 1:00, 2:26):** Sabit durması gereken kilitli çekimlerin son saniyelerinde dijital kamerada unprompted ileri kayma/push oluşuyor.
- **Ufuk Çapalaması Sapması (Setup D · S21 · 1:24):** Dönüş çekiminde çekirdek halka ızgarası S11/S13'e kıyasla +1.8° açıyla eğriliyor.
- **Kullanıcı Arayüzünde Yeniden Merkezleme (S19 · 1:17):** Terminal arayüzünde model HUD ögesine kilitlenirken kadraj mid-clip yukarı doğru tilting yapıyor.

### ⑩ OYUNCULUK BULGULARI (HAM - 5.5/10 · VERDICT: MOSTLY LEGIBLE)
- **Ayrılma Duruş Sıfırlanması (S12 · 02:08 - 🟠 MAJOR):** Halat kopması sonrasında gövde duruşu araç geri tepmesini göz ardı ederek anında nötr konuma sıfırlanıyor.
- **Tiyatral Yüz Buruşturması (S3 · 00:28 - 🟡 MINOR):** Erken kumanda kolu çekimindeki yüz ifadesi ilk efor ağırlığına göre fazla tiyatral kalıyor.
- **Kesmede Yüz Gerilimi Düşüşü (S10–S11 · 01:50 - 🟡 MINOR):** Telemetri takibinden acil durum kolu makrosuna geçişte yüz gerilimi ve bakış açısı aniden düşüyor.

### ⑪ IŞIK BULGULARI (HAM - 6.6/10 · VERDICT: KEY WALKS)
- **Gezici Ana Işık (S1–S5 · 00:00–00:22 - 🟠 MAJOR):** Çorak arazi sahnelerinde güneş/gökyüzü ana ışık yönü 11 saat yönünden 1 ve 12 saat yönlerine düzensiz kayıyor.
- **Gece/Gündüz Işık Sıçraması (S28 → S29 · 02:01–02:10 - 🟠 MAJOR):** Açık gündüz çayırından zifiri karanlık orman tabanına, ardından gün batımına anlık ışık sıçraması.
- **Renk Sıcaklığı Dalgalanması (S27 → S28 · 01:57–02:06 - 🟡 MINOR):** Sıcak altın saat yan ışığı (3800K), üst açı çayır çekiminde soğuk nötral ışığa (5200K) sıfırlanıyor.

### ⑫ HOOK BULGULARI (HAM - 8.5/10 · VERDICT: THE STRANGER STAYS)
- **Açılış Sis Tutması (0:00–0:04 - 🟡 MINOR):** İlk 4 saniye sisli manzara çekiminde kalıyor; dış ses/eylem 5. saniyede kilitleniyor.
- **Koridor Yürüyüş Platosu (0:24–0:38 - 🟡 MINOR):** Ardışık 3 koridor temposu merkez çekirdeğe ulaşmadan önce görsel ivmeyi yavaşlatıyor.
- **Tekrarlanan Kurulum Beat'i (1:28–1:36 - 🟡 MINOR):** Podyumdaki çift geri çekim hareketi görsel riski tırmandırmadan koridor hareketini tekrarlıyor.

---

## ⛔ SONUÇ VE AKSİYON
- Raporlar `02_HAM_RAPORLAR/` dizininde saklandı (Toplam 12 mercek ham raporu).
- SPEC bulunduğu ve raporlar `MOD V` koşulduğu için [D129] gereğince T1-T4, T7-T8 tablolarına skor **YAZILMADI**.
- ⑨-⑫ (KADRAJ, OYUNCULUK, IŞIK, HOOK) plan sadakati mercekleri SPEC olmadan / MOD V koşulduğu için [D190/D184] uyarınca geçersiz sayılarak karantinaya alındı.
- Plan-makara sahne sayısı uyuşmazlığı (Plan 16 sahne ↔ Rapor 32 sahne [D188]) ve kesme yayılımı farkı [D107] nedeniyle teslim geçersiz sayıldı; yeniden üretim ve MOD D formatında SPEC eşliğinde QA koşusu gerekmektedir.
