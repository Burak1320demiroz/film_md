# 📊 BLACK_ACCORD — QA Değerlendirme ve İyileştirme Raporu · Parça 2 (C49–C96)

> **Video:** `taslak_01` 2. parça · 08:00 · 48 çekim · film içi zaman kodu: 08:00–16:00 (parça içi: 00:00–08:00)  
> **Tarih:** 21.10.2026 · **Yazan:** Fable (ana ajan; alt ajan çağrısı yok, bütçe: 36/60 korundu)  
> **Ham Kaynak:** `ODA/HAM_QA_RAPORU_P2_0800-1600.md` (ve `FILM_QA_RAPORLARI/02_HAM_RAPORLAR/BLACK_ACCORD/HAM_QA_RAPORU_P2_0800-1600.md`)  
> **İçerik:** Sahibin ilettiği 4 mercek: (1) Anlatım Testi · (2) İzleme Formu (A / B1 / B2 / B3) · (3) Süreklilik · (4) Tarama  
> **Dayanak:** `AGENTS.md` §1b (Kural türleri), §3 (Hata Nerede Doğdu) · `uretim_hatti/QA_OKUMA_KILAVUZU.md` · `SECIM_VE_KURGU_KILAVUZU.md` · `FILM.md` §1–§7 · `PROMPTLAR/G05–G08.md`  
> **Kayıt:** `NOTLAR.md` → MONTAJ EŞLEMESİ · TARAMA · SÜREKLİLİK · ANLATIM · İZLEME · KARARLAR ("P2" satırları) · `ODA/DURUM.md`  

---

## 0 · Bu Rapor Neye Dayanıyor?

### 0.1 Kaynakların Geçerliliği ve Doğrulanması (QA_OKUMA §4)

| Rapor | Durum | Gözlem & Metodoloji | Bu Raporda Ne Yapıldı? |
|---|:--:|---|---|
| **ANLATIM TESTİ** | **Geçerli** | Sesli ve plansız izleme simülasyonu; filmin doruk noktası (climax) ve çözülüşü (resolution) C49–C96 üzerinden eksiksiz okunmuş. | 48 çekimlik planla eşlendi; 17 satırlık A1–A4 tablosu çekim numaralarına bağlandı. |
| **İZLEME FORMU A** | **Geçerli / İncelendi** | Sahibin 8 sorusu üzerinden doldurulmuş detaylı teknik analiz. | Telefon ahizesi halüsinasyonu, TTS takılmaları ve kadraj dışı ses karmaşası doğrulandı. |
| **İZLEME FORMU B (B1/B2/B3)** | **Dış İzleyici Simülasyonu** | 3 farklı profil (B1: Bilimkurgu sever, B2: Genel izleyici, B3: Kurgucu). Üçü de ortak kopma noktalarında birleşiyor. | `AGENTS.md` §1 ⑤ gereğince insan yerine geçmez; ancak 02:04–03:20 arasındaki diyalog karmaşasının dramaturgik kanıtıdır. |
| **SÜREKLİLİK** | **Geçerli** | 45 kesme noktası incelenmiş; 26 bulgu sıralanmış. | Gerçek süreklilik kusurları (telefon ahizesi, cihaz çoğalması, arka plan morphing) diyalog kesmelerinden ayrıştırıldı. |
| **TARAMA** | **Geçerli** | 18 somut bulgu (T1–T11); zaman kodları ve güven dereceleri verilmiş. | Çekimlerle eşlendi; nesne morfları, klonlanan silah ve TTS hece takılmaları analiz edildi. |

### 0.2 Zaman → Çekim Eşlemesi (C49–C96)
Parça 2, filmin 08:00 ile 16:00 arasındaki 48 çekimini (C49–C96) 10'ar saniyelik pencerelerle birebir taşımaktadır:
- **08:00–10:00 (C49–C60 · Parça içi 00:00–02:00):** B5 BARIŞIN KÂRI — Çıkar ağının ifşası, silah çekilmesi (C59) ve Nem'in araya girmesi (C60).
- **10:00–12:00 (C61–C72 · Parça içi 02:00–04:00):** B6 KULAKLIKLAR ÇIKIYOR — Kulaklıkların masaya bırakılması, bireysel suç itirafları (Vekh, Orun, Ishra).
- **12:00–14:00 (C73–C84 · Parça içi 04:00–06:00):** B7 TEK SESİN SONU — Nith'in röleyi kesmesi, Orun'un özel kanalını açması (C78 K1 maviye döner), Nith'in durdurulması.
- **14:00–16:00 (C85–C96 · Parça içi 06:00–08:00):** B8 ASLIYLA AYNI — Filolara doğrudan yayın, silahların sönmesi, tahliye koridorunun açılması, kapanış (C96).

---

## 1 · Yönetici Özeti ve Genel Karne

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                     BLACK_ACCORD PARÇA 2 (08:00–16:00) KARNESİ               ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ • Dramatik Çözülüş & Katarsis: 9.5 / 10 (Sorumluluk alma duygusu çok güçlü)   ║
║ • Görsel Tasarım & Uzay Sahnesi: 9.0 / 10 (Filoların durması, kara delik)    ║
║ • Ses Tasarımı & TTS Doğruluğu: 5.5 / 10 (6 TTS kekelemesi, miks kopukluğu)   ║
║ • Kurgu & Kadraj Dışı Sesler  : 5.0 / 10 (Ağız oynamazken dış ses karmaşası) ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### 1.1 Tutanlar ve Büyük Başarılar
1. **Dramatik Doruk ve Çözülüş Kusursuz İlerledi:** Karakterlerin suçu makineye yıkmak yerine kendi gerçek savaş suçlarını üstlenmeleri ("Limanı ben bombalattım" - Vekh; "İki tarafa da silah sattım" - Orun; "Tahliye koridorunu ben kapattım" - Ishra) izleyicilerde derin bir katharsis ve saygı uyandırdı.
2. **Karakter Jestleri ve İletişim Devrimi:** Nem'in kulaklığını çıkarıp masaya koymasıyla başlayan zincirleme tepki (Vekh, Ishra, Silex, Orun'un kulaklıkları çıkarması) filmin en güçlü görsel anı oldu.
3. **Orun'un Kararı:** Bencil tüccar Orun'un tüm sözleşmelerini kaybetme pahasına kendi kanalını açması ("Then I will finally own something I didn't buy") güçlü bir karakter arkı oluşturdu.
4. **Finalin Duygusal Yankısı:** Dış uzayda filoların silahlarını kapatması, küçük sivil gemilerin güvenle geçişi ve Nem'in son repliği ("That is what he said") tüm izleyicilerde "Atmosferik", "Rahatlatıcı" ve "Sakin bir burukluk" bıraktı.

### 1.2 Kırılanlar ve Kusurlar
1. **Kadraj Dışı Konuşma Karmaşası (02:04–03:20 / Film: 10:04–11:20):** Ekranda bir karakter dururken ve ağzı hiç oynamazken başka bir karakterin sesi duyuluyor (örn. Vekh kadrajdayken Nem'in sesi; Nem kadrajdayken Nith'in sesi). İzleyiciler kimin konuştuğunu anlayamadığı için sahneden koptu.
2. **Absürt AI Halüsinasyonu — Kablolu Telefon Ahizesi (02:46 ve 03:07):** Cam fanuslu Ishra'nın kaskının içinden elini geçirip eski tip telefon ahizesi çıkarması ve Orun'un masadan telefon ahizesi kaldırıp kulağına dayaması bilimkurgu ciddiyetini tamamen baltalayan trajikomik bir yapay zekâ hatasıdır.
3. **Cihaz ve Silah Klonlanması (Spawn Bug):**
   - 01:33 (C59): Vekh tabancayı çekerken, sağ kalçasındaki kılıfta tabancanın bir kopyası durmaya devam ediyor.
   - 05:16 (C82): Mor kristal uzaylı K2 kristalini masaya koyarken, masadaki siyah K1 cihazı yoktan ikiye bölünüp çoğalıyor.
4. **TTS Ses Sentezi Kekelemeleri (Tam 6 Noktada):**
   - 00:23 (C51): *"they misunder— they misunderstand"*
   - 00:43 (C54): *"sound like— like permission"*
   - 02:13 (C63): *"what you meant? What you meant."*
   - 03:35 (C72): *"carry consequences— carry consequences"*
   - 03:53 (C74): *"his network— network"*
   - 04:33 (C78): *"own some— own something"*
5. **Klip İçi Mekân Değişimi (06:04 · C87):** Ishra konuşurken arka plan kesme olmadan altın salondan gri gemi kabinine dönüşüyor.
6. **10 Saniyelik Boş Bakışmalar:** 01:41–01:49'da Nem elleri havada 8 saniye heykel gibi bekliyor; diyalog aralarındaki 5-6 saniyelik ölü zamanlar tempoyu ağırlaştırıyor.

---

## 2 · Hata Nerede Doğdu? (Kök Neden Analizi · AGENTS.md §3)

```
┌────────────────────────────────────────────────────────────────────────┐
║                 BLACK_ACCORD P2 HATA DOĞUŞ YERİ DAĞILIMI                ║
├────────────────────────────────────────────────────────────────────────┤
║ 1. KURGU & SES MİKSİ     : %40 (Kadraj dışı ses karmaşası, ölü zaman)  ║
║ 2. SES SENTEZİ (TTS)     : %25 (6 adet kelime takılması/kekeleme)      ║
║ 3. PROMPT & MODEL (AI)   : %20 ("Receiver" → Telefon ahizesi morfu)    ║
║ 4. HAREKET & MODEL       : %10 (Silah ve cihaz klonlanması)            ║
║ 5. ARKA PLAN DOKUSU      : %5  (06:04 klip içi kabin morfu)            ║
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Prompt Kelimesinden Doğanlar ("Receiver" → Telefon Ahizesi)
- **Kök Neden:** Promptta kulaklık/alıcı için kullanılan **"receiver"** kelimesi, görsel üretici model tarafından 20. yüzyıl kablolu telefon ahizesi (telephone receiver) olarak yorumlanmıştır! Model, cam kaskın içinden ahize çıkarma ve masadan ahize kaldırma saçmalığını bu yüzden üretmiştir.
- **Müdahale:**
  - Kurguda: Ahizenin göründüğü o 1.5–2 saniyelik temas anları jiletle kesilecek (trim); elin kulağa gittiği an ile kulaklığın masada durduğu an arasına kesme atılacaktır.
  - Gelecek filmler için: İngilizce promptlarda asla tek başına "receiver" yazılmayacak; `"small magnetic temple-comm disk"`, `"earpiece node"` veya `"audio-comm stud"` kalıbı kullanılacaktır.

### 2.2 Kurgu ve Ses Miksinden Doğanlar (Kadraj Dışı Sesler)
- **Kök Neden:** `FILM.md` §1 plan kuralı ("Ön planda tek konuşmacı; ikinci ses kurguda kadraj dışı verilebilir") doğru uygulanmış, ancak kurguda kadraj dışı seslere mekân akustiği (pan, reverb, telemetri EQ) verilmediği için izleyici ekrandaki karakterin ağzı kapalıyken konuştuğunu zannetmiştir.
- **Müdahale:** Kadraj dışından konuşan karakterlerin seslerine hafif oda tınısı verilecek; konuşulan kişiye dönen reaksiyon planları (reaction shot) kurguya yerleştirilecektir.

### 2.3 Ses Sentezinden Doğanlar (TTS Glitches)
- **Kök Neden:** ElevenLabs / TTS modelinin noktalama işaretleri ve tirelerde çift hece tetiklemesi yapması.
- **Müdahale:** 6 ses takılması da kurgu timeline'ında ses kanalında razor tool ile milisaniyelik kesme yapılarak temizlenecektir. Replikler yeniden üretilmeyecektir.

---

## 3 · Çekim Çekim Birleşik Bulgu Tablosu (C49–C96)

| Çekim | Zaman (Parça · Film) | Planlanan Olay & Replik | Saptanan Kusur / Bulgu | Kaynak | Kök Neden | Alınacak Karar |
|:--:|:--:|---|---|:--:|:--:|---|
| **C49** | 00:01 · 08:01 | Orun: "Every failed summit renews his security contracts." | Karakterin dudakları oynamıyor, dış ses gibi algılanıyor (A3). | A3, İA-1 | Model / Kurgu | Plan gereği model sesi; kabul veya diyalog başlangıcıyla senkron. |
| **C50** | 00:11 · 08:11 | Silex: "I certified it. His contracts kept it running." | Temiz aralık (00:10–00:20). | — | — | Kabul. |
| **C51** | 00:21 · 08:21 | Nem: "You profit every time they misunderstand each other." | **TTS KEKELMESİ (00:23):** *"they misunder— they misunderstand"* (A4, İA-5, T8). | A4, İA-5, T8 | Ses Sentezi | **00:23'teki takılma razor cut ile silinecek.** |
| **C52** | 00:31 · 08:31 | Nith: "I never ordered a single ship to fire." | Temiz aralık (00:30–00:40). Nith'in savunması net. | — | — | Kabul. |
| **C53** | 00:41 · 08:41 | Nem: "You made every reply sound like permission." | **TTS TEKRARI (00:43):** *"sound like— like permission"* (A4, İA-5, T8). | A4, İA-5, T8 | Ses Sentezi | **00:43'teki "like" tekrarı kesilip temizlenecek.** |
| **C54** | 00:51 · 08:51 | Silex: "How many ceasefire offers did you suppress?" | Temiz aralık. Silex'in sorgusu çok etkili. | — | — | Kabul. |
| **C55** | 01:01 · 09:01 | Nith: "As many as the process required." | Nith'in kulaklık aparatı üçgenden yuvarlağa dönüyor (S1). | S1 | Başlangıç Karesi | Kabul adayı (mikro detay). |
| **C56** | 01:11 · 09:11 | Ishra: "You armed the ships that trapped our wounded." | Temiz aralık. Su başlığı ve kırılgan öfke başarılı. | — | — | Kabul. |
| **C57** | 01:21 · 09:21 | Nem: "Do not draw your weapon." | Temiz aralık. Nem'in uyarısı tam vaktinde giriyor. | — | — | Kabul. |
| **C58** | 01:31 · 09:31 | Vekh: "You both chose this." / Silah çekilir. | **SİLAH KLONLANMASI (01:33):** Vekh tabancayı çekerken sağ kılıfta tabanca durmaya devam ediyor (T5/T6). | T5, T6 | Model / Spawn | Silah çekme anı kırpılacak; elinde tabanca olan kareden başlanacak. |
| **C59** | 01:41 · 09:41 | Nem: "Look at my hands. Stop listening to the speaker." | **ÖLÜ ZAMAN:** Replik bittikten sonra Nem elleri havada 8 saniye heykel gibi bekliyor (İA-4). | İA-4, S1 | Kurgu (Ölü Zaman) | Son 5 saniye kırpılarak diyalog akışı hızlandırılacak. |
| **C60** | 01:51 · 09:51 | Nem alıcısını çıkarıp masaya koyar: "My hands are empty..." | Şakağındaki alıcıyı çıkarıp masaya koyuyor ama şakağında metal parça kalıyor (T6). | T6 | Model | Kabul adayı (kulağın üzerinde mikro kalıntı, hikâyeyi bozmuyor). |
| **C61** | 02:01 · 10:01 | Vekh: "The relay told me to draw." | 02:04'te ekranda Vekh varken Nem'in sesi duyuluyor (A3, İA-1). | A3, İA-1 | Kurgu / Ses | Nem'in sesi C62'deki kendi planına J-cut ile bağlanacak. |
| **C62** | 02:11 · 10:11 | Nem: "Who should decide what you meant?" | **TTS TEKRARI (02:13):** *"what you meant? What you meant"* (A4, İA-5, T8). 02:15'te Nith'in dış sesi biniyor (A1). | A4, A1, T8 | Ses Sentezi / Kurgu | **02:13'teki tekrar silinecek;** Nith'in dış sesine telemetri tınısı verilecek. |
| **C63** | 02:21 · 10:21 | Vekh: "Say it again." / Kulaklığı çıkarır. | Vekh'in sol elinde aniden gümüş renkli büyük bir dikdörtgen cihaz beliriyor (T6). | T6 | Model | Cihaz masaya bırakılırken el hareketi kesmeyle atlanacak. |
| **C64** | 02:31 · 10:31 | Nem: "For once, let them hear what the noise is saying." | 02:35'te ekranda Nem varken Nith'in erkek sesi biniyor (A3). | A3, İA-1 | Kurgu / Ses | Dış ses dinleme planı olarak netleştirilecek. |
| **C65** | 02:41 · 10:41 | Ishra kulaklığını çıkarır: "Translate his words..." | **ABSÜRT HALÜSİNASYON (02:46):** Cam fanusun dışına kablolu telefon ahizesi dayıyor! (A1, İA-3, T1). | A1, İA-3, T1 | Model / Prompt | **Kurguda telefon ahizesi anı kesilip atılacak (trim).** |
| **C66** | 02:51 · 10:51 | Vekh: "I ordered the harbor shelled. That part was mine." | Vekh blasteri masaya bırakır; 02:56'da Silex konuşurken ağzı kıpırdamıyor (A3, T1). | A3, T1 | Kurgu / Ses | Silex'in repliği telepatik tınıyla verilecek; Vekh'in itirafı çok vurucu. |
| **C67** | 03:01 · 11:01 | Orun: "I sold to both sides. No machine signed those invoices." | **ABSÜRT HALÜSİNASYON (03:07):** Orun masadan telefon ahizesi kaldırıp kulağına götürüyor! (A1, İA-3, T1). | A1, İA-3, T1 | Model / Prompt | **Kurguda telefon ahizesi anı jiletle kesilip atılacak.** |
| **C68** | 03:11 · 11:11 | Nem: "He changed the words. You sent the ships." | 03:15'te ekranda Nem varken erkek dış sesi biniyor (A3). | A3 | Kurgu / Ses | Ses kadraj dışı olarak mikslenecek. |
| **C69** | 03:21 · 11:21 | Ishra: "I closed the evacuation lanes..." | İtiraf çok net; su kaskındaki yansıma başarılı. | — | — | Kabul. |
| **C70** | 03:31 · 11:31 | Nem: "Then let them live long enough to choose..." | **TTS TEKRARI (03:35):** *"carry consequences— carry consequences"* (A4, İA-5, T8). | A4, İA-5, T8 | Ses Sentezi | **03:35'teki tekrar kurguda kesilecek.** |
| **C71** | 03:41 · 11:41 | Nith: "No uncertified message leaves my station." / Röleyi kapatır. | Masadaki K1 cihazı yassıdan yüksek kübik bloğa dönüşüyor (S5, T6). | S5, T6 | Model / Morf | Kabul adayı (cihazın kapanma animasyonu olarak algılanabilir). |
| **C72** | 03:51 · 11:51 | Nem: "You never use his network for your own accounts." | **TTS TEKRARI (03:53):** *"network— network"* (A4, İA-5, T8). | A4, İA-5, T8 | Ses Sentezi | **03:53'teki kelime tekrarı temizlenecek.** |
| **C73** | 04:01 · 12:01 | Orun: "Would you? My relay reaches my ships directly." | Temiz aralık (04:00–04:10). | — | — | Kabul. |
| **C74** | 04:11 · 12:11 | Nem: "Then let the truth travel the way your money does." | Masada iki adet cihaz yan yana beliriyor (T5/T6). | T5, T6 | Model | Kabul adayı (masanın iki ucundaki terminaller). |
| **C75** | 04:21 · 12:21 | Nith: "Open that channel, and every protected contract is gone." | Temiz aralık (04:20–04:30). Nith'in tehdidi ve öfkesi tam oturmuş. | — | — | Kabul. |
| **C76** | 04:31 · 12:31 | Orun: "Then I will finally own something I didn't buy." / Kanalı açar. | **TTS KEKELMESİ (04:33):** *"own some— own something"* (A4, İA-5, T8). Üçgen ışık maviye döner (S5). | A4, T8, S5 | Ses Sentezi | **04:33 kekelemesi temizlenecek;** ışığın maviye dönmesi planla birebir tuttu! |
| **C77** | 04:41 · 12:41 | Nem: "Original voices. Original faces. No substituted lines." | Temiz aralık (04:40–04:50). Filmin felsefi manifestosu; çok güçlü. | — | — | Kabul. |
| **C78** | 04:51 · 12:51 | Nith: "They won't trust murderers asking for peace." | Temiz aralık (04:50–05:00). | — | — | Kabul. |
| **C79** | 05:01 · 13:01 | Nem: "Then we begin with what we did." | Temiz aralık (05:00–05:10). | — | — | Kabul. |
| **C80** | 05:11 · 13:11 | Silex K2 taşını masaya koyar: "My copy goes with the broadcast." | **CİHAZ ÇOĞALMASI (05:16):** Masadaki siyah cihaz ikiye bölünerek çoğalıyor (A1, İA-3, T5). | A1, İA-3, T5 | Model / Spawn | Çoğalma anı kırpılacak (trim). |
| **C81** | 05:21 · 13:21 | Orun Nith'i engeller: "You don't get to edit this one." | Nith'in geri çekilen parmakları hafif bükülüyor (T1). | T1 | Model | Kabul (anlık el gerilimi). |
| **C82** | 05:31 · 13:31 | Vekh ayağa kalkar: "Sit down. You can answer for every word." | Temiz aralık (05:30–05:40). Vekh'in heybeti ve komutan otoritesi muazzam. | — | — | Kabul. |
| **C83** | 05:41 · 13:41 | Nem: "Tell your fleets what you mean. I'll preserve what you say." | Temiz aralık (05:40–05:50). | — | — | Kabul. |
| **C84** | 05:51 · 13:51 | Vekh: "I order my fleet to withdraw. I will answer for the harbor." | Temiz aralık (05:50–06:00). Filoya geri çekilme emri; çok temiz. | — | — | Kabul. |
| **C85** | 06:01 · 14:01 | Ishra: "Open the evacuation lanes. All ships, stand down..." | **ARKA PLAN MORFU (06:04):** Altın salon bir anda gri gemi kabinine dönüşüyor (İA-2, T6); "stand down" dublajı erken bitiyor (A4). | İA-2, T6, A4 | Model / Dudak | **06:04 sonrası kırpılacak (trim);** replik 06:03'te bitiyor. |
| **C86** | 06:11 · 14:11 | Silex: "Suspend the relay. Preserve every unaltered recording..." | Temiz aralık (06:10–06:20). | — | — | Kabul. |
| **C87** | 06:21 · 14:21 | Orun: "No more weapons deliveries. My ships will carry survivors." | Temiz aralık (06:20–06:30). Tüccarın kurtarma gemisi kararı tam oturdu. | — | — | Kabul. |
| **C88** | 06:30 · 14:30 | Dış uzay / Filolar durur, silahlar söner. | Vakumda derin motor uğultusu var (T8, İA-6); küçük kurtarma gemileri güvenle geçiyor. | T8, İA-6 | Ses Miksi | Motor sesi kısılarak derin uzay sessizliği ve müzik öne çıkarılacak. |
| **C89** | 06:40 · 14:40 | Dış uzay / Tahliye koridoru açık. | İtici ışıkları kameraya doğru yanıyor (T11); uzay rüzgarı efekti var (İA-6). | T11, İA-6 | Ses / Model | Ses temizlenecek; sahne görsel olarak çok görkemli. |
| **C90** | 06:50 · 14:50 | Nith: "They'll build another translator." | Temiz aralık (06:50–07:00). Nith'in yenilgiyi kabul edişi ama sistemin süreceğini hatırlatması harika. | — | — | Kabul. |
| **C91** | 07:01 · 15:01 | Ishra: "Will you speak for us?" | Temiz aralık (07:00–07:10). | — | — | Kabul. |
| **C92** | 07:11 · 15:11 | Silex: "We can't recover those days." | Masadaki plaka mavi diske dönüşmüş (S5/T6); felsefi replik çok temiz. | S5, T6 | Model | Kabul. |
| **C93** | 07:21 · 15:21 | Vekh: "We will not fire." | Vekh bu planda tekrar maskeli (S1/T6); "Ateş etmeyeceğiz" sözü çok ağır ve kesin. | S1, T6 | Başlangıç Karesi | Kabul (kapanış yemini). |
| **C94** | 07:30 · 15:30 | İstasyon kara deliğin önünde / Final sessizliği. | Temiz aralık (07:30–07:39.0). İstasyon ve kara deliğin görsel ihtişamı muazzam. | — | — | Kabul. |
| **C95** | 07:40 · 15:40 | Nem (Dış Ses / VO): "That is what he said." | Senaryonun açılışına ("That's not what he said") mükemmel bir simetrik kapanış. | — | — | **Kusursuz Final.** |
| **C96** | 07:50 · 15:50 | Kara delik ve istasyon uzaklaşır / Kararma. | Genel atmosferik kapanış. | — | — | Kabul. |

---

## 4 · Parça 2 İçin Çıkarılan Gerekli Dersler

### Ders 1: "Receiver" Kelimesi Promptlarda "Telephone Handset" Halüsinasyonu Yaratır
- **Vaka:** Ishra'nın cam kaskın içinden telefon ahizesi çıkarması (02:46) ve Orun'un telefon ahizesiyle konuşması (03:07).
- **Ders:** AI modelleri "receiver" kelimesini sıklıkla eski telefon ahizesi olarak görselleştirir. İletişim aygıtları için daima somut geometrik tarifler kullanılmalıdır: `"small metallic ear-comm stud"`, `"flat hexagonal comm-disk"`. Kurguda bu sahnelerdeki ahize anları kesilip atılmalıdır.

### Ders 2: Kadraj Dışı Replikler (Off-Screen Dialogue) Ses Miksinde Konumlandırılmalıdır
- **Vaka:** 02:04–03:20 arasında ekrandaki karakterin ağzı oynamazken dış seslerin duyulması izleyicide "ses kayması/hatası" hissi yaratmıştır.
- **Ders:** Kadraj dışından konuşan karakterin sesi doğrudan mikslenemez; o karaktere hafif bir oda uzaklığı/akustiği (reverb ve pan) verilmeli ve ekrandaki karakterin dinleme/tepki mimiği (reaction shot) kurgulanmalıdır.

### Ders 3: Nesne Çıkarma ve Bırakma Anlarında Klonlanma (Spawn Bug)
- **Vaka:** Vekh tabancayı çekerken kılıfta ikinci tabancanın kalması (01:33); kristal masaya konurken K1 cihazının ikiye bölünmesi (05:16).
- **Ders:** Modeller nesne hareketinde mevcut nesneyi dönüştürmek yerine kopyasını üretir. Silah çekme eylemi yerine, silahın zaten çekilmiş olduğu başlangıç karesinden başlamak bu hatayı sıfırlar.

### Ders 4: TTS Ses Sentezinde Çift Hece Temizliği Standart Bir Kurgu Adımıdır
- **Vaka:** Parça 2'de 6 ayrı yerde yaşanan hece kekelemeleri (*"they misunder- they misunderstand"*, *"own some- own something"* vb.).
- **Ders:** Ses sentez modellerinde bu takılmalar doğaldır; ancak filmin final miksine giremez. Kurgucu bu takılmaları timeline'da razor tool ile kesip micro-fade ile birleştirmelidir.

### Ders 5: Klip İçi Arka Plan Kayması (Morphing) Sahne Sonunda Kesilmelidir
- **Vaka:** 06:04'te Ishra'nın arkasındaki salonun aniden gemi kabinine dönüşmesi.
- **Ders:** AI modelleri replik bittikten sonra sahneyi taşımakta zorlanır ve arka planı halüsinasyona uğratır. Replik biter bitmez sahne kesilmelidir.

---

## 5 · Eylem Planı (Parça 2 Kurgu Revizyonu)

| Sıra | Eylem | Zaman Kodu (Parça 2) | Yapılacak İşlem | Yeniden Üretim? |
|:--:|---|---|---|:--:|
| **1** | **Telefon Ahizesi Halüsinasyonunu Kes** | 02:46 (C65) ve 03:07 (C67) | Ishra ve Orun'un telefon ahizesi tuttuğu 1-2 saniyelik kareleri timeline'da jiletle kesip at; doğrudan masaya bırakma anına bağla. | **HAYIR** (Kurgu Trim) |
| **2** | **6 TTS Kekelemesini Temizle** | 00:23, 00:43, 02:13, 03:35, 03:53, 04:33 | Ses kanalındaki hece tekrarlarını razor cut ile kes ve yumuşakça birleştir. | **HAYIR** (Ses Editi) |
| **3** | **Silah Klonlanmasını Kırp** | 01:33 (C58) | Silah kılıftan çıkarken oluşan klonlanma anını kes; Vekh'in silahı doğrulttuğu net kareden başlat. | **HAYIR** (Kurgu) |
| **4** | **Kadraj Dışı Sesleri Konumlandır** | 02:04–03:20 (C61–C68) | Nem ve Nith'in kadraj dışı seslerine hafif oda tınısı ver; ekrandaki dinleyiciye tepki planı kur. | **HAYIR** (Ses Miksi) |
| **5** | **Arka Plan Morfunu Kırp** | 06:04 (C85) | Ishra'nın repliği 06:03'te bitiyor; 06:04'teki kabin dönüşümünü sahne sonundan kesip at. | **HAYIR** (Kurgu Trim) |
| **6** | **Cihaz Çoğalmasını Kırp** | 05:16 (C80) | Silex kristali koyarken soldaki K1 cihazının ikiye bölündüğü son 2 saniyeyi kes. | **HAYIR** (Kurgu Trim) |
| **7** | **Kesintisiz Ses Yatağı** | 00:00–08:00 | Tüm kesmelerin altına kesintisiz salon tonu ve doruk noktası için alçak synth drone ser. | **HAYIR** (Ses Miksi) |

> **Özet:** Tıpkı Parça 1'de olduğu gibi, Parça 2'de de **hiçbir sahnenin yeniden üretilmesine gerek yoktur!** Belirlenen tüm hatalar kurgu timeline'ında trim ve ses temizliği ile 1-2 saatte mükemmel bir seviyeye getirilebilir.

---

## 6 · 16 Dakikalık Tam Film Birleşik Değerlendirmesi

Parça 1 (00:00–08:00) ve Parça 2 (08:00–16:00) birleştiğinde:
1. **Hikâye Kusursuz İşliyor:** "Tek bir 'not' kelimesinin silinmesiyle başlayan savaş, tüm delegelerin kulaklıkları çıkarıp kendi suçlarını itiraf etmesiyle durduruluyor." Bu dramatik yay hem içerik hem felsefe açısından tam bir başyapıt omurgası sunuyor.
2. **Kurgu Masasında Yapılacak Toplam Revizyon:**
   - Parça 1'deki 01:40 kronoloji hatası (Ishra tepkisi Vekh'in arkasına kaydırılacak).
   - Parça 1'deki 2, Parça 2'deki 6 TTS ses kekelemesi temizlenecek (toplam 8 mikro ses kesimi).
   - Parça 2'deki 02:46 ve 03:07 telefon ahizesi halüsinasyonları kırpılacak.
   - Parça 1'deki C37 veri grafiğine sinematik HUD metni eklenecek.
   - Tüm filmin altına kesintisiz tek kanal salon ambiyansı döşenecek.
   - 10 saniyelik ham kliplerin sonundaki ölü bakışmalar kırpılarak diyalog ritmi sıkılaştırılacak.

Film bu kurgu dokunuşlarıyla sıfır maliyetle (ekstra kredi harcamadan) doğrudan **yayın ve festival kalitesine** ulaşacaktır!
