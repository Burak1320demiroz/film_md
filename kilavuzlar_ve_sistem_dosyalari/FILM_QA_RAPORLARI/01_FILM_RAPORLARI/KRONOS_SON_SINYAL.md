# 🎬 KRONOS_SON_SINYAL — FİLM QA RAPORU

> **Durum:** Bölüm 1 (S01–S24 / 240 s / 04:00) 15 Mercek QA & Bölüm 2 (S25–S48 / 239 s / 04:00) 15 Mercek QA değerlendirmesi tamamlandı (TOPLAM 30 MERCEK RAPORU TAM).  
> **Bölüm 1 Özeti:** Görsel `REGENERATE` & `IDENTITY BREAK`, Ses `SOUNDTRACK HOLDS`.  
> **Bölüm 2 Özeti:** Görsel `REGENERATE` & `SUBJECT DUPLICATE IN FIELD`, Ses `WRONG VOICE`, Beden `MINOR TWITCHES`, Yön `WRONG WAY`.

---

## 📦 MALZEME VE DEPO YOLLARI

```
HAM RAPORLAR    kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/02_HAM_RAPORLAR/KRONOS_SON_SINYAL/
                ├── BÖLÜM 1: KRONOS_SON_SINYAL_PART1_1_KARE_HAM.md (15 mercek dosyası)
                └── BÖLÜM 2: KRONOS_SON_SINYAL_PART2_1_KARE_HAM.md ... PART2_15_YON_HAM.md (15 mercek dosyası)

PROMPT DOSYALARI yatay_8_dk_filmler/KRONOS_SON_SINYAL/
                ├── KRONOS_SON_SINYAL_BOLUM_1.md (S01–S12 · 00:00–02:00)
                ├── KRONOS_SON_SINYAL_BOLUM_2.md (S13–S24 · 02:00–04:00)
                └── KRONOS_SON_SINYAL_BOLUM_3.md (S25–S36 · 04:00–06:00)
```

---

## 📊 BÖLÜM 2 (PART 2 / S25–S48) 15 MERCEK ÖZET TABLOSU

| Mercek | Mod | Karar | Öne Çıkan Blocker ve Kritik Bulgular |
| :--- | :--- | :--- | :--- |
| **① KARE (Fizik & Görsel)** | Mode V | 🔴 **REGENERATE** | **0:38:** Çift karakter spawner hatası (A kapağı kapatılırken sağda 2. Aras spawn oluyor).<br>**2:20:** Dış uzay vakumunda gövde yırtılması/patlama sesi duyulması (🔴 Blocker).<br>**2:53:** Modül B ayrılırken mekanik kilit açılma sesinin vakumda yayılması (🔴 Blocker). |
| **② DEVAMLILIK (Karakter)** | Mode V | 🔴 **IDENTITY BREAK** | **00:38 & 02:44:** Çift Aras figürü (B modülünde kilitliyken A modülü arka planında da beliriyor).<br>**01:28:** Dijital saat T-01:25'ten T-01:27'ye geriye sıçrıyor.<br>**02:10:** Aras'ın kıyafeti tek çekimde koyu gri/turuncu cekete dönüşüyor. |
| **③ SES (Diyalog & Audio)** | Mode V | 🔴 **WRONG VOICE** | **00:50 (Replik 7):** Kestrel kulaklığı tutarken Aras'ın *"Kestrel, do you read me?"* repliğini Kestrel kendi sesiyle söylüyor! (Ses atama hatası - 🔴 Blocker). |
| **④ HİKAYE (Dramaturji)** | Mode V | 🟡 **SHOOT WITH TRIMS** | **0:45–1:15:** Uzayan şalter kurma prosedürü ritmi düşürüyor (30 sn trim tavsiyesi).<br>**1:40:** Gövde yırtılma krizinin görsel/işitsel hazırlığı yetersiz.<br>**2:30–2:38:** Aras'ın fedakarlık repliği aşırı açıklayıcı. **2:40** fırlatma ve **3:30** Mayday repliği çok güçlü. |
| **⑤ ARKA PLAN (Derin Tarama)** | Mode V | 🔴 **SUBJECT DUPLICATE IN FIELD** | **00:00–04:00:** Tüm sahnelerde sağ alt köşede 4 kollu yıldız AI filigranı (🔴 Blocker).<br>**02:44:** Module A kapı eşiğinde hayalet astronot figürü beliriyor (🔴 Blocker).<br>**00:25 vs 02:58:** Kırmızı kapı S3'te koridora, S18'de doğrudan uzay boşluğuna açılıyor. |
| **⑥ FİZİK (Ölçüm & Hız)** | Mode V | ⚠️ **FIXABLE IN EDIT** | **01:20 & 03:20:** Dijital saatlerin frekans bozulması (2 kat hızlı sayma, SOS saatinde `12:07:64` hatası).<br>**02:20:** 70 kPa patlamada enkaz parçalarının yavaş süzülmesi.<br>**01:30:** Sıfır g ortamında deck üzerinde yürüme footfall hareketi. |
| **⑦ AKSİYON (Okunurluk)** | Mode V | 🟢 **ACTION READS** | **11/11 vuruş okunabilir:** Karabina takma, kapak kapatma, şalter çekme ve EJECT buton basımları net.<br>**02:50:** Modül ayrılma anı tek karelik hızlı kesmeyle geçiyor.<br>**01:21 vs 02:40:** Ekran sayacı zaman uyumsuzluğu. |
| **⑧ EFOR (Fiziksel Bedel)** | Mode V | 🔴 **WEIGHTLESS WORK** | **02:20–02:39:** Vakum patlamasında tek elle tutunma sonrası Aras'ın elinde terleme, titreme veya solunum değişimi yok.<br>**00:21–00:34:** Ağır kırmızı kapı tek elle savrulup kilitlenirken sıfır-g gövde tepki kuvveti/bracing yok.<br>**00:10–02:08:** Basınçlı eldivenler ameliyat eldiveni inceliğinde hareket ediyor. |
| **⑨ KADRAJ (Kamera Sadakati)** | Mode V | 🔴 **RHYME BROKEN** | **00:00 & 03:50 (S1 vs S24):** İlk kare (MCU iç mekan) ile son kare (EWS dış uzay) kadraj kafiyesi oluşturmuyor (🔴 Blocker).<br>**00:00–04:00:** Tüm kliplerde kilitli kamerada mikro-sürüklenme ve creep.<br>**S3 vs S10:** Koridora geri dönüşte kamera hizada sapma yapıyor. |
| **⑩ OYUNCULUK (İfade)** | Mode V | 🟢 **MOSTLY LEGIBLE** | **02:40 (S17) & 03:30 (S22):** Karar ve fedakarlık bedeli beden dilinde net (el titremesi, omuz çökmesi, ağlama sonrası vakur duruş).<br>**00:10–01:30 (S2–S10):** Kriz öncesi mekanik görev hareketlerinde duygu mikro-ayarları eksik. |
| **⑪ IŞIK (Renk Sıcaklığı)** | Mode V | ⚠️ **GRADEABLE DRIFT** | **01:30 (S9→S10):** Aynı koridorda renk sıcaklığı 5600K soğuktan 3200K sıcak tungstene sıçrıyor.<br>**01:10 (S8):** Dünya penceresi yakınında patlayan aşırı pozlama.<br>**02:20 (S15):** Gövde yırtılması sonrası ani siyah seviyesi kayması. |
| **⑫ HOOK (Kanca & İkna)** | Mode V | ⚠️ **LEAVES AT 00:48 s** | **00:40–01:35:** Peş peşe şalter/panel sahneleri orta bölümde izleyici düşüşü yaratıyor.<br>**02:20–02:30 & 02:50–03:00:** Patlama ve modül ayrılma anları tek başına güçlü viral paylaşılamilirlik taşıyor.<br>**03:50–03:59:** Final kare döngüye bağlanamıyor. |
| **⑬ UYUM (SPEC Uyum)** | Mode V | ✂️ **INPUT MISSING** | SPEC bloğu ve sahne promptları veriye girilmediği için Mode V'de girdi eksik uyarısıyla kilitlendi. |
| **⑭ HAREKET (Beden Mantığı)** | Mode V | 🟢 **MINOR TWITCHES** | **00:44 (M6):** Sıfır-g ortamında ayakların havada bisiklet pedallama hareketi yapması (🔴 Blocker).<br>**02:28 (M15):** Patlama anında astronot bedeninin tepkisiz kalarak nötr duruşunu koruması.<br>**01:14 (M8):** Şalter çekilirken kolun 2 cm yukarı sıçrayıp stutters yapması. |
| **⑮ YÖN (Hedef Vektörü)** | Mode V | 🔴 **WRONG WAY** | **00:37 (V6):** Kapı kapandıktan sonra Aras'ın A Modülü içinde Kestrel'in yanında belirmesi (FLIP 🔴).<br>**02:44 (V19):** B Modülünde kilitli astronotun Kestrel'in arkasında hayalet figür olarak belirmesi (MISS 🔴). |

---

## 📊 BÖLÜM 1 (PART 1 / S01–S24) 15 MERCEK ÖZET TABLOSU

| Mercek | Mod | Karar | Öne Çıkan Bulgular |
| :--- | :--- | :--- | :--- |
| **① KARE (Fizik & Görsel)** | Mode V | 🔴 **REGENERATE** | Vakum ortamında ses (0:01 & 1:21 Blocker), vakum gaz püskürmesi fiziği (0:02 & 1:22), bozuk dijital metin (0:30). |
| **② DEVAMLILIK (Karakter)** | Mode V | 🔴 **IDENTITY BREAK** | Kestrel yüz/aktör kayması (S2 vs S4/S14), yok olan yanak yarası (00:12 vs 00:32), geriye/düzensiz sayan dijital saat (S4), Aras ceket değişimi (S7). |
| **③ SES (Diyalog & Audio)** | Mode V | 🟢 **SOUNDTRACK HOLDS** | 21 replik %100 senkronize, 3 farklı ses kaynağı net ayrışmış, dip gürültüsü düşüşü yok. |
| **④ HİKAYE (Dramaturji)** | Mode V | ⚠️ **REVISE STRUCTURE** | 10'ar saniyelik rijit kesme ritmi, B modülüne kimin gireceğine dair diyalog-aksiyon uyumsuzluğu, finalin ayrılma görünmeden 04:00'te kesilmesi. |
| **⑤ ARKA PLAN (Derin Tarama)** | Mode V | ⚠️ **FIELD DRIFTS** | Tüm sahnelerde sağ alt köşede AI filigran ikonu, S14 background astronot ayağının erimesi, S10 "POWER SYSTON" kelime hatası. |
| **⑥ FİZİK (Ölçüm & Hız)** | Mode V | ⚠️ **FIXABLE IN EDIT** | S4 saatin 0.9 saniyede 4 saniye düşüp 00:30'a sıçraması, S20 kapı kapanmasında yerçekimsiz ortam tepki kuvveti olmaması. |
| **⑦ AKSİYON (Okunurluk)** | Mode V | 🟢 **ACTION READS** | 18 aksiyon vuruşunun 15'i tamamen net ve anlaşılır. |
| **⑧ EFOR (Fiziksel Bedel)** | Mode V | 🔴 **NOBODY PAYS** | Basınçlı kıyafet içinde sıfır kas kasılması, sıfır efor, vizörde sıfır terleme/buğulanma, zaman baskısında sıfır solunum artışı. |
| **⑨ KADRAJ (Kamera Sadakati)** | Mode V | 🔴 **RHYME BROKEN** | 13 klipte kilitli kamerada drift/kayma, S01 (dış geniş) ile S24 (iç orta) arasında açılış/kapanış kafiyesi kurulmamış. |
| **⑩ OYUNCULUK (İfade)** | Mode V | 🔴 **TASK WITHOUT FEELING** | Karakterler buton/şalter işlerini düzgün yapıyor ancak hayati tehlike ve zaman baskısı karşısında beden dili nötr kalıyor. |
| **⑪ IŞIK (Renk Sıcaklığı)** | Mode V | 🔴 **KEY WALKS** | Dış uzayda güneş ışığı açısı S1 (10 o'clock) ile S9 (2 o'clock) arasında 180° dönüyor, vakum dumanında ışık hüzmesi hüzmelenmesi var. |
| **⑫ HOOK (Kanca & İkna)** | Mode V | ⚠️ **LEAVES AT 02:15** | İlk 10 saniye uzay kancası güçlü fakat 01:00-01:20 ve 02:00-02:20 arasındaki peş peşe konsol tıklama sahneleri izleyiciyi sıkıp düşürüyor. |
| **⑬ UYUM (SPEC Uyum)** | Mode V | ✂️ **INPUT MISSING** | SPEC bloğu ve sahne promptları girilmediği için bu mercek Mode V'de kilitlendi. |
| **⑭ HAREKET (Beden Mantığı)** | Mode V | 🟢 **MINOR TWITCHES** | 24 hareketin 19'u tam amaçlı. M15 (2:17) ve M22 (3:54) zemin kayması (sliding), M4 el kararsızlığı. |
| **⑮ YÖN (Hedef Vektörü)** | Mode V | 🟢 **MINOR MISAIMS** | 21 hedefin 19'u tam isabet. V21 (3:51) B modülüne gidiş yönü 3:30'daki kapı yönüyle çelişiyor. |
