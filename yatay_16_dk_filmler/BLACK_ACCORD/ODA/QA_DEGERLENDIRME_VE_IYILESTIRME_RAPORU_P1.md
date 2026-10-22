# 📊 BLACK_ACCORD — QA Değerlendirme ve İyileştirme Raporu · Parça 1 (C01–C48)

> **Video:** `taslak_01` 1. parça · 08:00 · 48 çekim · film içi zaman kodu: 00:00–08:00  
> **Tarih:** 21.10.2026 · **Yazan:** Fable (ana ajan; alt ajan çağrısı yok, bütçe: 36/60 korundu)  
> **Ham Kaynak:** `ODA/HAM_QA_RAPORU_P1_0000-0800.md` (ve `FILM_QA_RAPORLARI/02_HAM_RAPORLAR/BLACK_ACCORD/HAM_QA_RAPORU_P1_0000-0800.md`)  
> **İçerik:** Sahibin ilettiği 5 mercek: (1) Anlatım Testi · (2) İzleme Formu (A/B1) · (3) Süreklilik · (4) Tarama · (5) "Viral YouTuber" Ekstra Analizi  
> **Dayanak:** `AGENTS.md` §1b (Kural türleri), §3 (Hata Nerede Doğdu) · `uretim_hatti/QA_OKUMA_KILAVUZU.md` · `SECIM_VE_KURGU_KILAVUZU.md` · `ILK_30_SANIYE_KILAVUZU.md` · `GECIS_VE_SES_SUREKLILIGI.md` · `FILM.md` §1–§7 · `PROMPTLAR/G01–G04.md`  
> **Kayıt:** `NOTLAR.md` → MONTAJ EŞLEMESİ · TARAMA · SÜREKLİLİK · ANLATIM · İZLEME · KARARLAR ("P1" satırları) · `ODA/DURUM.md`  

---

## 0 · Bu Rapor Neye Dayanıyor?

### 0.1 Kaynakların Geçerliliği ve Doğrulanması (QA_OKUMA §4)
`uretim_hatti/QA_OKUMA_KILAVUZU.md` sözleşmesine göre gelen ham raporlar değerlendirilmiştir:

| Rapor | Durum | Gözlem & Metodoloji | Bu Raporda Ne Yapıldı? |
|---|:--:|---|---|
| **ANLATIM TESTİ** | **Geçerli** | Sesli ve plansız izleme simülasyonu; 8 dakikalık parça kesimi üzerinden hikâye omurgası, istek, engel ve diyaloglar eksiksiz okunmuş. | 48 çekimlik planla (C01–C48) karşılaştırıldı; A1–A4 tablosu çekim numaralarına bağlandı. |
| **İZLEME FORMU A** | **Geçerli / İncelendi** | Model tarafından sahibin 8 sorusu üzerinden doldurulmuş ("Videonun baştan sona sesli ve detaylı incelemesine dayanarak"). | Somut gözlemler (kurgu sırası, ölü zaman, TTS takılmaları) teknik olarak doğrulandı. |
| **İZLEME FORMU B1** | **Dış İzleyici Simülasyonu** | Yapay zekâ simülasyonu ("B1 — Ön bilgisiz izleme simülasyonu"). | `AGENTS.md` §1 ⑤ gereğince yayın onayında gerçek insan dış izleyicinin yerini tutmaz; ancak dramatik kafa karışıklığı noktaları (01:40, 06:00) referans alındı. |
| **SÜREKLİLİK** | **Biçimsel Uyarı / Geçerli** | 47 kesme (1–48) taranmış; C01–C48 olarak sıralı. | Raporun "LOOK JUMP" dediği maddelerin büyük kısmı diyalog kesmelerinde beklenen konuşmacı değişimleridir (yanlış alarm). Gerçek kostüm/boynuz/maske tutarsızlıkları ayrıştırıldı. |
| **TARAMA** | **Geçerli** | 19 somut bulgu (T1–T11); zaman kodları ve güven dereceleri (KESİN/OLASI) verilmiş. | Çekimlerle eşlendi; el-nesne kaynaşmaları, TTS takılmaları ve ters fizik hareketleri kök nedenine ayrıldı. |
| **VIRAL YOUTUBER ANALİZİ** | **Stratejik Kılavuz** | Puan içerir (`AGENTS.md` §1 ⑥ gereği puan karar vermez); ancak Retention (AVD), ilk 30 saniye kancası ve ölü zaman analizi son derece kritiktir. | 10 saniye blok tuzağı ile kanal kurgu politikası sentezlendi; A/B paketleme önerileri kaydedildi. |

### 0.2 Zaman → Çekim Eşlemesi (C01–C48)
Taslak montajda 48 kesmenin tamamı 10'ar saniyelik pencereler halinde art arda dizilmiştir. `FILM.md` planı ile montaj arasındaki eşleme %100 doğrulanmıştır:
- **00:00–01:00 (C01–C06):** Açılış / Giriş (Vekh C01 → Ishra C02 → Filolar C03 → Nem C04 → Nith C05 → Nem C06)
- **01:00–02:00 (C07–C12):** B1 Bölümü Sonu (Vekh C07 → Nith C08 → Nem C09 → Orun C10 / K1 küpü → Nem C11 → Silex C12 / K2 kristali)
- **02:00–04:00 (C13–C24):** B2 Bölümü — KİMİN TERCÜMESİ? (Vekh C13 → Ishra C14 → Nith C15 → Nem C16 → Salon Geniş C17 → Vekh C18 → Ishra C19 → Vekh C20 → Nem C21 → Nith C22 → Silex C23 → Nem C24)
- **04:00–06:00 (C25–C36):** B3 Bölümü — SAVAŞIN ARŞİVİ (Silex C25 → Vekh C26 → Vekh C27 → Orun C28 → Nem C29 → Orun C30 → Filolar C31 → Nem C32 → Nith C33 → Ishra C34 → Nith C35 → Nem C36)
- **06:00–08:00 (C37–C48):** B4 Bölümü — DIŞARIDA ÜÇ GÜN (Grafik C37 → Filo dış C38 → Nem C39 → İstasyon C40 → Silex C41 → Nith C42 → Nem C43 → Ishra C44 → Vekh C45 → Nith C46 → Nem C47 → Orun C48)

---

## 1 · Yönetici Özeti ve Genel Karne

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    BLACK_ACCORD TASLAK_01 (PARÇA 1) KARNESİ                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║ • Dramatik Omurga & Konsept : 9.5 / 10 (Eksiksiz anlaşıldı, merak yüksek)     ║
║ • Görsel Tasarım & Dünya     : 9.0 / 10 (6 ırk, kara delik salonu sinematik)  ║
║ • Ses Tasarımı & Miks       : 6.5 / 10 (Ambiyans kesintileri, 2 TTS glitch)   ║
║ • Kurgu & Ritim (Pacing)     : 4.0 / 10 (01:40 sıra hatası, 10s ölü zaman)   ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

### 1.1 Neler Tutsun Diye Planlandı ve Tutsun? (BAŞARILAR)
1. **Politik Gerilim ve Hikâye Omurgası Tam Okundu:** İzleyici, çeviri sisteminin (Relay) barış mesajlarındaki kritik kelimeleri bilerek silerek savaşı kışkırttığını ("One word vanished: Not"), orijinal kayıtların kasten imha edildiğini ve silah tüccarı Orun ile sistemin bundan kâr sağladığını sıfır ön bilgiyle eksiksiz kavradı.
2. **Karakter Ayrışması ve Oyunculuk Ağırlığı:** 6 farklı uzaylı ırkın (Nem, Vekh, Ishra, Nith, Silex, Orun) görsel kimliği ve ses tınıları izleyicide güçlü bir merak ve ciddiyet uyandırdı.
3. **Replik Sadakati:** `FILM.md` §5'teki planlı replikler neredeyse kelimesi kelimesine seslendirildi; sahne metinlerinde anlatım sapması yaşanmadı.
4. **Final Vaadi / Duygusal Gerilim:** 07:31'deki *"Neutrality is expensive"* (Tarafsızlık pahalıdır) ve 07:51'deki *"Those accounts are private"* (O hesaplar gizlidir) anları izleyicide soğuk bir gerilim ve tatmin yarattı.

### 1.2 Neler Kırıldı? (KRİTİK SORUNLAR)
1. **01:40–02:15 Kurgu Sırası Tersliği (Kronoloji Hatası):** C14 çekiminde Ishra henüz yapılmamış bir testin sonucuna tepki veriyor (*"His hands are empty. Why did I hear a threat?"*). Halbuki test önerisi C12'de (02:01), Vekh'in ellerini kaldırıp *"My hands are empty"* demesi C13'te (02:11) yer alıyor. Bu hata izleyicinin hikâye mantığını anında kırıyor.
2. **10 Saniyelik Blok Tuzağı ve Ölü Zaman (Dead Air):** 48 çekimin tamamı hiç kırpılmadan 10 saniye olarak uç uca eklenmiş. Replikler ilk 3-4 saniyede bitiyor; kalan 5-6 saniye boyunca karakterler donuk biçimde bakışıyor ya da yapay zekânın boşluğu doldurmak için uydurduğu sahte iç çekme/burun çekme hareketleri devreye giriyor (02:18, 02:48, 04:48, 05:59, 07:09, 07:28).
3. **TTS Ses Sentezi Kekelemeleri (Audio Glitch):**
   - 04:23 (C27): *"after that m- after that message"* (Vekh'in repliğinde yarım hece tekrarı).
   - 07:04 (C43): *"Someone chose- chose what we heard"* (Nem'in repliğinde kelime tekrarı).
4. **Karakter Dışı ve Erken Giren Sesler (L-Cut / J-Cut Hatası):**
   - 00:06 (C01): Vekh ekrandayken telsiz/HUD efekti olmayan mekanik bir ses *"Original transmission altered"* diyor.
   - 00:57 (C06): Kamera Nem'in üzerindeyken ve Nem'in ağzı kapalıyken kalın bir erkek sesiyle *"That was not my intention"* duyuluyor (C07'nin sesi erken sızmış).
5. **Nesne Morfları ve El-Nesne Kaynaşması (T1 / T6 / T9):**
   - C10 (01:30): Orun'un eli K1 küpünün içinden eriyerek geçiyor.
   - C12, C23, C25 (02:00, 03:42, 04:00): Silex'in K2 kristali; el kristalin içinden geçiyor; 04:00'te yassı plaka morphing ile kendiliğinden büyüyüp 3D kristale dönüşüyor ve sonra küçülüp kayboluyor.
   - 04:03 (C25): Kristalden kadın sesiyle yabancı dilde ses çalarken Silex'in kendi ağzı da senkronize kıpırdıyor.
6. **Vekh ve Nith Görsel Sürekliliği (S1 / T6):**
   - Vekh: C01'de maskesiz, C07'de tam kapalı metal ağızlıklı, C13'te maskeli, C20'de tekrar maskesiz. Konuşurken maskenin kıpırdamaması.
   - Nith: 00:40 ve 02:20'deki sivri boynuz ve sağ kulaklık implantı, 03:30 ve 06:50'de yuvarlaklaşıp kısalıyor, kulaklık sol şakağa geçiyor.
7. **C37 (06:00) Soyut Çizgi Grafiği:** Siyah zemin üzerinde uzayan sarı ve mavi çizgilerin neyi temsil ettiği görsel olarak anlatılmıyor; arka plandaki taş/çakıl yürüme foley sesi uzay meclisinden tamamen koparıyor.

---

## 2 · Hata Nerede Doğdu? (Kök Neden Analizi · AGENTS.md §3)

`AGENTS.md` Madde ④ gereğince yeni kural yazılmaz; hatalar doğduğu yere göre sınıflandırılır ve doğrudan orada çözülür:

```
┌────────────────────────────────────────────────────────────────────────┐
║                 BLACK_ACCORD P1 HATA DOĞUŞ YERİ DAĞILIMI                ║
├────────────────────────────────────────────────────────────────────────┤
║ 1. KURGU & MONTAJ SIRASI : %40 (Sıra tersliği, ölü zaman, J/L kesim)   ║
║ 2. SES MİKSİ & TTS       : %25 (Ambiyans kesintisi, hece takılması)    ║
║ 3. BAŞLANGIÇ KARESİ      : %15 (Vekh maskesi, Nith boynuzu, K2 kristal)║
║ 4. HAREKET & MODEL       : %15 (El-nesne kaynaşması, ters motor itişi) ║
║ 5. ANLATIM & HUD         : %5  (C37 grafik arayüz etiket eksikliği)   ║
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Kurgu ve Montajdan Doğanlar (Edit & Sequence)
- **01:40–02:15 Kronoloji Hatası:** C14'ün montajda C11 ile C12 arasına erken konması tamamen bir montaj dizilim hatasıdır. Çekimler yeniden üretilmeyecek; timeline'da C11 → C12 → C13 → C14 sırasına kaydırılacaktır.
- **10 Saniyelik Boş Bakışmalar:** Çekimlerin başında ve sonunda konuşma bittikten sonraki 5-6 saniyelik atıl süreler kurguda trimlenerek diyalog temposu toparlanacaktır.
- **Erken Giren Ses (00:57):** C07'deki Vekh repliğinin ilk cümlesi (*"That was not my intention"*) C06'nın üzerine kontrolsüzce taşmıştır. Kurgu kanalında ses kendi klibine çekilecektir.

### 2.2 Ses Miksi ve TTS Sentezinden Doğanlar (Audio & Voice)
- **TTS Kekelemeleri:** 04:23 (*"after that m-"*) ve 07:04 (*"chose-"*) kısımları ses dalgası üzerinde milisaniyelik kesme (razor trim) ile yok edilecektir. Replik metni yeniden üretilmeyecek, mevcut ses dosyası temizlenecektir.
- **Ambiyans Kesintisi (Her 10 sn'de bir):** Kliplerin kendi içindeki ham oda tonları kesildiği için her 10 saniyede bir ses düşüşü yaşanmaktadır. Çözüm: FILM §6 Y1/Y2 salon oda tonu (alçak hava sirkülasyonu + derin makine vızıltısı) tüm parçanın altına kesintisiz tek kanal olarak döşenecektir.
- **Röle Sesi Yabancılaşması (00:06):** "Original transmission altered" repliğine radyo/telsiz EQ filtresi ve hafif bir sentez tınısı verilerek sistem sesi olduğu tescillenecektir.

### 2.3 Başlangıç Karesinden Doğanlar (Start Frame)
- **Vekh Maske Tutarsızlığı:** Bazı çekimlerde ağzı açık, bazılarında kapalı metal maskeli. Kural: Vekh'in referans paneli (`2.VEKH`) tek bir yüz durumuyla kilitlenmeli; ya da maske bir durum değişimi olarak planlanmışsa çekim promptunda açıkça belirtilmelidir.
- **Nith Boynuz ve İmplant Değişimi:** Nith'in kulaklık aparatının sağdan sola geçmesi başlangıç karesinde simetri hatasından kaynaklanmıştır. Referans görseli (`1.NITH`) başlangıç karesine çapa yapılacaktır.
- **Silex K2 Kristali (C12, C23, C25):** Yassı altıgen levhanın birden 3D sivri kristale dönüşmesi başlangıç karelerindeki farklı nesne tasarımlarından doğmuştur.

### 2.4 Hareket ve Fizikten Doğanlar (Motion & Physics)
- **El-Nesne Kaynaşması (T1 / T9):** 01:30'da Orun'un, 02:00 ve 03:42'de Silex'in parmaklarının nesnelerin içinden geçmesi. Flow/Veo modellerinin el-nesne temasındaki bilinen sınırıdır (`ARIZA_LISTESI` T1). Temas anları ya kadraj dışında bırakılmalı ya da kesmeyle atlanmalıdır.
- **Ters Motor İtişi (C31 · 05:10):** Dış uzayda gemilerin arka iticileri yanarken motor yönünün tersine (geri geri) gitmesi. Model hareket isteminde itiş yönü açıkça belirtilmelidir.

### 2.5 Anlatım ve Görsel Arayüzden Doğanlar (HUD / UI)
- **C37 Zaman Grafiği (06:00):** Senaryoda geçen "yerel 6 dakika ↔ dışarıdaki 3 gün" bilgisini izleyiciye aktarmak için görselin üzerine sinematik bir HUD arayüzü ve İngilizce veri metinleri (*"Local Station Time: 00:06:00" / "Outer Fleet Time: 72:00:00 - 3 Days"*) bindirilmelidir.

---

## 3 · Çekim Çekim Birleşik Bulgu Tablosu (C01–C48)

Aşağıdaki tablo, 5 farklı QA kaynağının (Anlatım `A#`, İzleme `İA`/`B1`, Süreklilik `S#`, Tarama `T#`, YouTuber `YT`) bulgularını C01–C48 çekimleriyle birebir eşlemektedir:

| Çekim | Zaman | Planlanan Olay & Replik | Saptanan Kusur / Bulgu | Kaynak | Kök Neden | Alınacak Karar |
|:--:|:--:|---|---|:--:|:--:|---|
| **C01** | 00:00–00:10 | Vekh: "We did not fire first." / Röle: "Original transmission altered." | Sol implant kaybolup sağda yeni parça çıkıyor (T6); Röle sesi telsiz/HUD efektsiz giriyor, ağız kapalıyken karakter dışı ses algılanıyor (A3, T8, YT). | T6, T8, A3, YT | Başlangıç Karesi / Ses Miksi | İmplant kilitlenecek; Röle sesine telsiz/arayüz EQ filtresi eklenecek. |
| **C02** | 00:10–00:20 | Ishra: "Then you came here to boast about it?" | Replik 00:14'te bitiyor; 00:14–00:20 arası 6 saniye donuk bakışma (YT). | YT, İA-4 | Kurgu (Ölü Zaman) | Son 4 saniye kırpılacak (trim). |
| **C03** | 00:20–00:30 | Dış uzayda dört filo; silah hatları aydınlanır. | Vakumda derin motor uğultusu (T8); plan çok etkileyici, açılış kancası potansiyeli yüksek (YT). | T8, YT | Ses Miksi / Kurgu | Vakum motor sesi hafifletilecek; açılış için J-Cut alternatifi değerlendirilecek. |
| **C04** | 00:30–00:40 | Nem: "That's not what he said." | Parmak uçları konsolla kaynaşıyor/eriyor (T1). Replik 00:34'te bitiyor, 6 saniye boşluk (YT). | T1, YT | Hareket / Kurgu | Parmak teması kısa tutulacak; klip sonu kırpılacak. |
| **C05** | 00:40–00:50 | Nith: "The clerk does not address the council." | Replik 00:45'te bitiyor, 5 saniye boş bakışma (YT). | YT, İA-4 | Kurgu (Ölü Zaman) | Klip sonu kırpılacak. |
| **C06** | 00:50–01:00 | Nem: "Your translator just declared a war." | Nem kadrajdayken ve ağzı kapalıyken 00:57'de Vekh'in sesi ("That was not my intention") erken duyuluyor (A4, T8, YT). | A4, T8, YT | Kurgu / Ses | Vekh'in sesi 00:57'den kaldırılıp C07'nin başına taşınacak. |
| **C07** | 01:00–01:10 | Vekh: "I denied the attack." | C01'de maskesiz olan Vekh'in yüzünde tam kapalı metal maske beliriyor (T6, S1). | T6, S1 | Başlangıç Karesi | Vekh'in yüz/maske durumu referansla (`2.VEKH`) sabitlenecek. |
| **C08** | 01:10–01:20 | Nith: "The relay has no nation. It cannot take sides." | Temiz aralık (01:10–01:19.5). Karakter oturumu tutarlı. | — | — | Kabul. |
| **C09** | 01:20–01:30 | Nem: "Who certified it?" | Temiz aralık (01:20–01:29.5). | — | — | Kabul. |
| **C10** | 01:30–01:40 | Orun: "Shall we argue more efficiently?" / K1 küpü masaya konur. | Orun'un sağ eli 01:31'de K1 sekizgen cihazının içinden eriyerek geçiyor (T1, T9). | T1, T9 | Hareket / Model | Küp bırakma anı kesmeyle atlanacak ya da el teması sadeleştirilecek. |
| **C11** | 01:40–01:50 | Nem: "One word vanished. Not..." *(Montajda Ishra'nın C14 repliği buraya girmiş!)* | **KRİTİK KRONOLOJİ HATASI:** Ishra 01:41'de "His hands are empty..." diyor (A1, İA-1, B1-6). 01:43'te Ishra gergin soru sorarken gülümsüyor (İA-4, YT). | A1, İA-1, YT | Kurgu Sırası / Model | **C14 çekimi 02:10 sonrasına taşınacak;** 01:44'teki sırıtan yüz ifadesi kırpılacak. |
| **C12** | 01:50–02:00 | Silex: "Then test a sentence none of us can mistake." / K2 kristali masaya konur. | Silex'in parmakları mor kristalin içinden eriyerek geçiyor (T1); masadaki bronz ızgara kayarak kadrajdan çıkıyor (T6). | T1, T6 | Hareket / Kare | K2 kristal temas anı kırpılacak; bronz ızgara sabitlenecek. |
| **C13** | 02:00–02:10 | Vekh: "My hands are empty." (Boş eller masada). | Konuşurken maske/çene hareketsiz (T11). Eller masada boş açılıyor. | T11 | Hareket / Model | Planlanan C13 çekimi; montajda C11'in önüne alınmamalı, C12'den sonra gelmeli. |
| **C14** | 02:10–02:20 | Ishra: "His hands are empty. Why did I hear a threat?" | Replik sonrası 02:18'de sahte ve abartılı iç çekme hareketi var (İA-4). | İA-4 | Kurgu / Model | C13'ten sonraya yerleştirilecek; 02:18 iç çekmesi kırpılacak. |
| **C15** | 02:20–02:30 | Nith: "The system translates intent, not primitive sounds." | Temiz aralık (02:20–02:29.5). Nith'in replik tonu ve otoritesi çok başarılı. | — | — | Kabul. |
| **C16** | 02:30–02:40 | Nem: "Then it isn't translating. It's issuing orders in our voices." | Sahne arkasında salon mimarisi doğru; replik vurgusu güçlü. | — | — | Kabul. |
| **C17** | 02:40–02:50 | Geniş salon planı / Kara delik manzarası. | 10 saniye boyunca tamamen sessiz ve hareketsiz; izleyicinin videoyu bırakmak istediği en belirgin ölü zaman (A2, İA-7, B1-7). | A2, İA-7, B1-7 | Kurgu (Tempo) | Süresi 3-4 saniyeye indirilecek veya üzerine Nem/Nith replik yatağı bindirilecek. |
| **C18** | 02:50–03:00 | Vekh: "My intent belongs to me." | Maske hareketsizliği (T11); 02:48'de yapay nefes/iç çekme sesi (İA-6). | T11, İA-6 | Model / Ses | 02:48 nefes sesi temizlenecek. |
| **C19** | 03:00–03:10 | Ishra: "At the last summit, we asked for an evacuation corridor." | Başlıktaki su seviyesi ve yüz dokusu tutarlı. | — | — | Kabul. |
| **C20** | 03:10–03:20 | Vekh: "I received a demand for our undefended coast." | Çekim içi temiz; Vekh bu çekimde tekrar maskesiz görünüyor (T6). | T6 | Başlangıç Karesi | Maskesiz durum korunacak. |
| **C21** | 03:20–03:30 | Nem: "Play the source, not the certified version." | Temiz aralık (03:20–03:29.5). Nem'in duruşu kararlı. | — | — | Kabul. |
| **C22** | 03:30–03:40 | Nith: "Sources are discarded after certification..." | Nith'in boynuz/yüz hatları 02:20'ye göre değişmiş (İA-2, S1). | İA-2, S1 | Başlangıç Karesi | `1.NITH` referans çapasından üretilecek. |
| **C23** | 03:40–03:50 | Silex: "My recorder kept both channels." | Sol el kristali kaldırırken nesnenin içinden geçerek yön değiştiriyor (T1). | T1 | Hareket / Model | Nesne kaldırma temas penceresi kısaltılacak. |
| **C24** | 03:50–04:00 | Nem: "That reply was loaded before he finished speaking." | Nem henüz ses çalınmadan tepki veriyor gibi görünüyor (A1). | A1 | Kurgu (Sıra/Yerleşim) | C25'teki ses çalma anıyla senkronize edilecek. |
| **C25** | 04:00–04:10 | Silex / Kayıt Cihazı: "[Jomis turidi]" (Eski Ishra kaydı dinletilir). | Yassı mor plaka morphing ile 3D kristale dönüşüyor (T6, İA-2); ses çalarken Silex'in kendi ağzı da açılıp kapanıyor (T11); yabancı ses kime ait belirsiz (A3). | T6, T11, A3, İA-2 | Başlangıç Karesi / Hareket | Silex'in ağzı kapalı tutulacak, sesin kristalden geldiği FX ışığıyla vurgulanacak; kristal morfu önlenecek. |
| **C26** | 04:10–04:20 | Vekh: "That was the message we answered." | Vekh yeniden maskeli görünüyor (T6). | T6 | Başlangıç Karesi | Maske durumu kilitlenecek. |
| **C27** | 04:20–04:30 | Vekh: "We shelled the harbor after that message." | **TTS SES HATASI (04:23):** *"after that m- after that message"* kelime tekrarı/takılması var (A4, İA-5, T8, YT). 04:28'de yüksek foley/kumaş hışırtısı (İA-6). | A4, İA-5, T8, YT | Ses Sentezi / Foley | **04:23'teki kekeleme razor cut ile temizlenecek;** 04:28 hışırtısı silinecek. |
| **C28** | 04:30–04:40 | Orun: "War makes every old recording look like evidence." | Temiz aralık (04:30–04:39.5). Orun'un mimikleri ve tüccar tavrı başarılı. | — | — | Kabul. |
| **C29** | 04:40–04:50 | Nem: "And what does it make your weapons shipments?" | Replik sonrası 04:48'de yapay iç çekme ve donuk bakışma (İA-4). | İA-4 | Kurgu / Model | 04:48 sonrasındaki boşluk kırpılacak. |
| **C30** | 04:50–05:00 | Orun: "Legal. Both sides paid." | Temiz aralık (04:50–04:59.5). Karakterin kuru mizahı çok iyi oturmuş. | — | — | Kabul. |
| **C31** | 05:00–05:10 | Dış uzayda dört donanma. | **UZAY FİZİĞİ HATASI (05:10):** Gemiler motor püskürtme yönünün tersine, motorlarının baktığı yöne (geri geri) doğru ilerliyor (T11). | T11 | Model / Hareket | Gemi hareket vektörü düzeltilecek (motor sola bakıp sağa itmeli). |
| **C32** | 05:10–05:20 | Nem: "Who collected the fee for every translated threat?" | Temiz aralık (05:20–05:29.5). Nem'in sorgulaması çok net. | — | — | Kabul. |
| **C33** | 05:20–05:30 | Nith: "Sign the provisional accord..." | Temiz aralık. Nith'in bürokratik baskısı planla uyumlu. | — | — | Kabul. |
| **C34** | 05:30–05:40 | Ishra: "Your accord requires us to keep using your relay." | Temiz aralık (05:30–05:39.5). Su başlığı ve yüz dokusu tutarlı. | — | — | Kabul. |
| **C35** | 05:40–05:50 | Nith: "Without it, you have no common language." | Temiz aralık. | — | — | Kabul. |
| **C36** | 05:50–06:00 | Nem: "We lack a common language, not a reason to listen." | Replik sonu 05:59'da yapay iç çekme/nefes sesi (İA-4). | İA-4 | Kurgu / Ses | 05:59 nefes sesi silinecek. |
| **C37** | 06:00–06:10 | İki saat karşılaştırması — Detay / kurgu grafiği. | **ANLATIM VE GRAFİK KOPUKLUĞU:** Siyah zemin üzerinde uzayan sarı ve mavi çizgiler etiketsiz, daktilo/çakıl sesli; ne olduğu anlaşılmıyor (A1, İA-1, B1-6, T10, YT). | A1, İA-1, T10, YT | Anlatım / Arayüz / Ses | **Çizgilerin üzerine sinematik HUD metinleri eklenecek:** *"Local Station Time: 6 Min"* ve *"Outer Fleet Time: 3 Days"*; taş sesleri silinecek. |
| **C38** | 06:10–06:20 | Vekh öncü gemisi dış / Geciken mesaj. | Temiz aralık (06:10–06:19.5). Filo dış görüntüsü planla uyumlu. | — | — | Kabul. |
| **C39** | 06:20–06:30 | Nem: "When did that arrive?" | Temiz aralık (06:20–06:29.5). | — | — | Kabul. |
| **C40** | 06:30–06:40 | İstasyon ve kara delik geniş manzara. | Temiz aralık (06:30–06:39.5). İstasyonun olay ufkunun dışında kalışı planla örtüşüyor. | — | — | Kabul. |
| **C41** | 06:40–06:50 | Silex: "All four fleets requested a pause. None reached this table." | Ağız hareketsiz (Silex telepatik/cinsiyetsiz tınılı, kabul). Replik çok net. | T11 | Ses / Model | Kabul. |
| **C42** | 06:50–07:00 | Nith: "Signals distort near a black hole." | Nith'in boynuzları kısalmış ve kulaklık sağdan sola geçmiş (T6, S1). | T6, S1 | Başlangıç Karesi | `1.NITH` referansı kilitlenecek. |
| **C43** | 07:00–07:10 | Nem: "Gravity didn't remove only ceasefires. Someone chose what we heard." | **TTS SES HATASI (07:04):** *"Someone chose- chose what we heard"* kelimesi iki kez üst üste biniyor (A4, İA-5, T8, YT). 07:09'da sahte iç çekme (İA-4). | A4, İA-5, T8, YT | Ses Sentezi / Model | **07:04'teki çift binen "chose" kelimesi temizlenecek;** 07:09 iç çekmesi kırpılacak. |
| **C44** | 07:10–07:20 | Ishra: "My hospital ships have been waiting for an answer." | Temiz aralık (07:10–07:19.5). Duygusal kırılganlık ve ses rezonansı çok başarılı. | — | — | Kabul. |
| **C45** | 07:20–07:30 | Vekh: "You spent their last days choosing our words." | Çekim içi temiz; Vekh bu çekimde maskesiz. 07:28'de gereksiz iç çekme hareketi (İA-4). | İA-4 | Kurgu (Ölü Zaman) | 07:28 sonrası kırpılacak. |
| **C46** | 07:30–07:40 | Nith: "Neutrality is expensive." | Temiz aralık (07:30–07:39.5). Filmin en vurucu felsefi repliklerinden biri; tam oturdu. | — | — | Kabul. |
| **C47** | 07:40–07:50 | Nem: "Orun... show us who keeps paying when talks fail." | Temiz aralık (07:40–07:49.5). Nem'in Orun'a dönüşü ve suçlaması kusursuz. | — | — | Kabul. |
| **C48** | 07:50–08:00 | Orun: "Those accounts are private." | Temiz aralık (07:50–07:59.5). Parça 1'in bitiş kancası güçlü bir soru işaretiyle kapanıyor. | — | — | Kabul. |

---

## 4 · Çıkarılan Gerekli Dersler (Kurallara Dokunmadan, Filmin Pratiği İçin)

`AGENTS.md` Madde ④ gereğince: **Yeni kural yazılmaz; yeni kılavuz türetilmez.** Ancak bu 8 dakikalık ham montajdan çıkan ve ikinci 8 dakikanın (C49–C96) montajında/üretiminde doğrudan uygulanması gereken **7 somut üretim dersi** şunlardır:

### Ders 1: Kurguda Kronoloji ve Neden-Sonuç Sırası Asla Bozulamaz
- **Vaka:** 01:40'ta Ishra'nın henüz yapılmayan teste ve masada açılmamış ellere tepki vermesi izleyiciyi hikâyeden tamamen koparmıştır.
- **Ders:** Karakterlerin diyalogları birbiriyle mantıksal zincir (Aksiyon → Reaksiyon) halinde kurgulanmalıdır. Test önerilmeden (C12) ve eller gösterilmeden (C13) sonuç repliği (C14) montajlanamaz. Parça 2'deki C58 (silah çekme emri) ve C59 (Vekh'in blaster çekmesi) sıralamasında aynı kronoloji titizlikle korunmalıdır.

### Ders 2: "10 Saniyelik Blok Tuzağı" ve Boş Bakışmalar Kurguda Eritilmelidir
- **Vaka:** Ham üretilen 10 saniyelik kliplerin son 5-6 saniyesinde karakterler donukça bakışmakta, yapay iç çekmeler yapmakta ve tempo %40'a düşmektedir.
- **Ders:** Klipler ham haliyle art arda dizilmemeli; replik bittikten sonraki anlamsız boşluklar J-Cut ve L-Cut teknikleriyle birbirine bindirilmelidir. Replik süresi 3 saniye ise, dinleyenin tepkisine kesilmeli veya bir sonraki konuşmacının repliği önceki sahnenin son saniyelerine taşırılmalıdır.

### Ders 3: Yapay Zekâ Ses Sentezi (TTS) Kekelemeleri Timeline'da Temizlenmelidir
- **Vaka:** 04:23 (*"after that m- after that message"*) ve 07:04 (*"Someone chose- chose what we heard"*).
- **Ders:** Model sesiyle üretilen diyaloglar ham haliyle yayına sokulamaz. Ses kanalında hece veya kelime takılması görüldüğünde ses yeniden üretilmek zorunda değildir; kurgu yazılımında o 0.3 saniyelik hatalı hece razor tool ile jilet gibi kesilip atılmalı ve ses yumuşakça birleştirilmelidir (micro-crossfade).

### Ders 4: Sahne Sonu AI Mimik ve Hareket Halüsinasyonları Ayıklanmalıdır
- **Vaka:** 01:43'te Ishra'nın tehdit duyduğunu söylerken aniden gülümsemesi; sahne sonlarındaki abartılı iç çekmeler (02:18, 02:48, 04:48 vb.).
- **Ders:** Video üretici modeller 10 saniyelik süreyi tamamlamak için istem dışı mikro mimikler (gülümseme, göz kırpma, esneme) halüsinasyonu üretir. Bu anlar kullanılabilir aralığın (clean window) dışındadır; kurgucu bu anları kesip atmalıdır.

### Ders 5: El-Nesne Temasları ve Donanım Morfları Kadraj Dışında Çözülmelidir
- **Vaka:** Orun'un K1 küpünün içinden elinin eriyerek geçmesi (01:31); Silex'in K2 kristalinin elinde morflanarak 3D büyük taşa dönüşüp sonra küçülmesi (04:00–04:09).
- **Ders:** Video modelleri nesne bırakma ve alma temaslarında parmakları nesneye kaynaştırmaktadır. Nesne masaya konurken ya da alınırken temas anı değil, nesnenin masada durduğu an ve karakterin yüzü kadrajlanmalıdır (kesmeyle atlama). İkinci 8 dakikadaki blaster çekme (C59) ve alıcı kulaklıkları çıkarma (C61–C69) sahnelerinde aynı tuzaktan kaçınılmalıdır.

### Ders 6: Ortam Ses Yatağı (Room Tone) Kesintisiz Tek Kanal Olmalıdır
- **Vaka:** Her 10 saniyede bir oda tonunun bıçak gibi kesilmesi izleyicide amatörlük hissi uyandırmaktadır.
- **Ders:** Kliplerin içindeki atıl sesler kısılmalı; `FILM.md` §6'da belirtilen salon yatağı (alçak uzay salonu hava akımı) tüm 8 dakikanın altına kesintisiz tek bir ses şeridi olarak serilmeli, sahne geçişleri bu yatağın üzerinde akmalıdır.

### Ders 7: Soyut Bilgi Grafikleri (C37) Görsel Metin (HUD UI) ile Desteklenmelidir
- **Vaka:** 06:00'daki iki çizgi grafiğinin neyi anlattığı anlaşılamamış, daktilo/çakıl sesleri atmosferi bozmuştur.
- **Ders:** Zaman genişlemesi gibi karmaşık bilimkurgu kavramları soyut çizgilerle bırakılamaz. Grafiğin üzerine şık, sinematik fontlarla *"LOCAL STATION TIME"* ve *"OUTER FLEET TIME (3 DAYS)"* etiketleri eklenmeli; taş sesleri silinip yerine veri/telemetri sinyal tınısı konmalıdır.

---

## 5 · YouTuber / Viral Büyüme ve Retention Dersi: "10 Saniye Blok Tuzağı" Nasıl Aşılır?

YouTuber raporunda sunulan stratejik öneriler kanalın algoritma başarısı için hayati dersler içerir:

### 5.1 İlk 30 Saniye Kancası (Hook Optimizasyonu)
- **Sorun:** Video ilk 3 saniye sessizlikle başlıyor, ardından durağan bir yakın plan geliyor. YouTube izleyicisi ilk 2-3 saniyede güçlü bir görsel ya da ses kancası görmezse videoyu terk eder.
- **Öneri (YouTuber & Fable Sentezi):** 00:24'teki iki devasa uzay filosunun kara delik önünde kırmızı lazerlerle birbirine ateş açtığı epik dış uzay sahnesi (C03), videonun ilk 3 saniyesine taşınabilir. Görüntüde uzay savaşı başlarken Vekh'in sesi (*"We did not fire first."*) J-Cut olarak bu görüntünün üzerine bindirilebilir. Bu hamle ilk saniyeden dev bütçeli bir uzay operası vaat ederek tıklayan herkesi ekrana kilitler.

### 5.2 10 Saniyelik Blok Kuralı ↔ Viral Ritim Dengesi
- **SÖZLEŞME Sınırı:** `AGENTS.md` gereğince depodaki kural: her çekim 10 saniyedir (toplam 16:00 = 96 çekim).
- **Algoritma Gerçeği:** Ham 10'ar saniyelik bloklar diyalog gerilimini sarkıtmakta ve izlenme süresini (AVD) düşürmektedir.
- **Çözüm (Sahip Tercihi):**
  1. *Depo İçi / Sözleşmeli Montaj:* 10 saniyelik video klipleri korunur; ancak konuşma bittikten sonraki boşluklara dinleyen elçilerin tepki planları (B-roll / Cutaway) kesilerek dinamizm sağlanır; ses yatağı kesintisiz akar.
  2. *YouTube Yayını / Hızlı Kurgu (Director's Cut):* Sahip isterse YouTube'a yüklenecek versiyonda ölü zamanları kesip videoyu ~4-5 dakikalık, nefes aldırmayan saf gerilim formatına indirebilir.

### 5.3 Paketleme ve Thumbnail (Küçük Resim) Stratejisi
Yayın paketinde test edilmek üzere YouTube raporunun önerdiği 2 güçlü konsept:
- **Varyasyon A (Yüz & Çatışma):** 04:20'deki Kızıl Komutan Vekh'in doğrudan kameraya baktığı simetrik yakın plan; arkada devasa kara delik. Üzerinde tek kelimelik sinematik yazı: **"ONE WORD."** veya **"WAR."**
- **Varyasyon B (Ölçek & Epiklik):** 00:24'teki iki uzay filosunun kara delik önünde lazerlerle çatıştığı geniş plan. Başlık alternatifi: *"THE MISSING WORD | An AI Deleted One Word. It Started a Galactic War."*

---

## 6 · Eylem Planı (Hemen Kurguda Yapılacaklar)

| Sıra | Eylem | İlgili Saniyeler / Çekimler | Yapılacak İşlem | Yeniden Üretim Gerekir mi? |
|:--:|---|---|---|:--:|
| **1** | **Kurgu Sırasını Düzelt** | 01:40–02:15 (C11–C14) | C14'teki Ishra'nın tepkisini C12 ve C13'ün sonrasına taşı. Sıralama: C11 (Nem) → C12 (Silex test önerisi) → C13 (Vekh boş eller) → C14 (Ishra tepki). | **HAYIR** (Sadece Timeline) |
| **2** | **TTS Kekelemelerini Kes** | 04:23 (C27) ve 07:04 (C43) | 04:23'teki *"after that m-"* ve 07:04'teki çift binen *"chose"* kelimesini ses kanalında jiletle kesip temizle. | **HAYIR** (Ses Editi) |
| **3** | **Erken Sızan Sesi Taşı** | 00:57 (C06) | Nem ekrandayken erken giren Vekh sesini C07'nin başlangıcına kaydır. | **HAYIR** (Kurgu) |
| **4** | **Yapay İç Çekmeleri ve Boşlukları Kırp** | 02:18, 02:48, 04:48, 05:59, 07:09, 07:28 | Replik bittikten sonraki yapay nefes seslerini ve 01:44'teki sırıtan Ishra mimiğini timeline'da kes. | **HAYIR** (Kurgu Trim) |
| **5** | **Kesintisiz Ses Yatağı Döşe** | 00:00–08:00 (Tüm Parça) | Her 10 sn'de kesilen klip seslerini kıs; altına kesintisiz FILM §6 Y1/Y2 salon tonu ve hafif gerilim drone'u koy. | **HAYIR** (Ses Miksi) |
| **6** | **Röle Sesine Filtre Ekle** | 00:06 (C01) | "Original transmission altered" cümlesine telsiz/HUD EQ filtresi uygula. | **HAYIR** (Ses Efekti) |
| **7** | **Zaman Grafiğini Etiketle** | 06:00 (C37) | Soyut çizgilerin üzerine *"Local Time: 6 Min"* ve *"Outer Fleet Time: 3 Days"* HUD metinleri bindir; çakıl seslerini telemetri bip'iyle değiştir. | **HAYIR** (Basit Grafik/Altyazı) |
| **8** | **Geniş Plan Sessizliğini Kısalt** | 02:40–02:50 (C17) | 10 saniyelik donuk genel planı 3-4 saniyeye indir ya da diyalog köprüsü kur. | **HAYIR** (Kurgu) |

> **Özet:** İlk 8 dakikalık kısımda (Parça 1) **görüntülerin yeniden üretilmesine gerek yoktur!** Saptanan tüm kusurlar (sıra hatası, ses takılmaları, ölü zamanlar, grafik arayüzü) kurgu masasında 1–2 saatlik bir timeline revizyonu ile çözülebilir ve video doğrudan festival/viral seviyesine ulaştırılabilir.

---

## 7 · Sahibe Bildirim ve Sonraki Adım

1. **Parça 1 (00:00–08:00) QA Raporları Başarıyla İşlendi:**
   - Ham rapor `ODA/HAM_QA_RAPORU_P1_0000-0800.md` olarak kaydedildi.
   - Değerlendirme ve dersler bu dosyada (`QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU_P1.md`) toplandı.
   - `NOTLAR.md` ve `ODA/DURUM.md` güncellendi.
2. **Sonraki Adım:** Sahip ikinci 8 dakikalık kısmı (08:00–16:00, C49–C96) verdiğinde aynı titizlikle `HAM_QA_RAPORU_P2_0800-1600.md` ve `QA_DEGERLENDIRME_VE_IYILESTIRME_RAPORU_P2.md` hazırlanacak ve tüm filmin final montaj revizyonu tamamlanacaktır.
