# 📊 THE_WRONG_BURN — QA Değerlendirme ve İyileştirme Raporu

> **Dosya:** `the wrong burn.mp4` (Taslak Montaj · ~02:03 · 12 Çekim + Kapanış Kartı)  
> **Tarih:** 15.10.2026  
> **Kaynak Veri:** `ODA/HAM_QA_RAPORU.md` (Anlatım Testi, İzleme Formu, Süreklilik Denetimi, Teknik Tarama)  
> **Dayanak:** `AGENTS.md` §3 (Hata Nerede Doğdu), `uretim_hatti/QA_OKUMA_KILAVUZU.md`

---

## 1. YÖNETİCİ ÖZETİ VE GENEL DEĞERLENDİRME

`the wrong burn.mp4` taslak montajı; yörünge mekaniğinin soğuk atmosferi, Dünya yörüngesindeki derinlik hissi, yalnızlık ve uzay boşluğundaki gerilim bakımından güçlü bir görsel temel kurmuştur. İlk 30 saniyelik hook (C01–C03) kopan halatı, sürüklenen astronotu ve Sela'nın kurtarma motivasyonunu başarıyla izleyiciye geçirmiştir.

Buna rağmen, dört QA merceğinin (Tarama, Süreklilik, Anlatım, İzleme) ortak değerlendirmesinde filmin bütünlüğünü sakatlayan **üç ölümcül problem** saptanmıştır:

1. **Final Kurgu Çelişkisi ve Anlatı İntiharı (01:39 – 01:48):**
   * `C11`'de (01:39–01:46) iki astronot uzay boşluğunda çarpışıp uzay istasyonundan tamamen koparak kadrajın solundan uzayın derinliğine doğru savrulmaktadır.
   * Ancak hemen sonra gelen `C12`'de (01:48) Sela, hiçbir ara geçiş veya açıklama olmadan **aniden yeniden istasyon korkuluğuna tutunmuş**, Bram'ı halatla tutar halde durmaktadır.
   * İzleyici simülasyonu bu sahneyi *"Hem uzaya savruldular hem istasyona tutunmuş göründüler, son iki sahne mantık olarak birbirini yalanladı"* şeklinde okumuş ve filmi tek kelimeyle **"Kopuk"** olarak nitelendirmiştir.
2. **Model Sesi ve Vakum Kuralı İhlali (Ses Çöküşü):**
   * `FILM.md` §6 kuralı açıkça: *"Model sesi kullanılmaz (Return silent videos; ses kurguda)"* demesine rağmen, videolarda yapay zekânın ürettiği bozuk, anlamsız heceler ve yapay mırıltılar bırakılmıştır (`00:16`, `00:53`, `01:01`, `01:50`).
   * `FILM.md` §5'teki hayati replikler (Bram R01–R08, R11, R12; Sela R04, R09, R10) kurguya eklenmediği için filmin ana önermesi olan *"İstediğine ulaşmak için ondan uzağa yak / Yükselen geride kalır"* kuralı sözel desteğinden mahrum kalmıştır.
   * Uzay vakumu kuralına aykırı dış sesler (00:08 metalik çarpma, 00:20 ve 00:47 whoosh/hava sesleri, 01:30'da el kaldırırken seri mekanik tıkırtı) atmosferi zedelemiştir.
3. **Karakter ve Mekân Sürekliliği Kırılmaları (24 Süreklilik Hatası):**
   * `C01`'de Sela'nın kolunda renkli şerit yokken `C02`'de turuncu şerit belirmekte; sırtında gereksiz çift halat süzülmektedir.
   * `C04`'te Bram'ın kaskında küçük bir işaret lambası yerine güneş gibi parlayan devasa sarı bir ışık küresi türemektedir.
   * `C05`'te Sela'nın kaskının içinde siyah bere varken `C06`'da bere kaybolmakta, yüz hatları değişmekte ve kaskta çift vizör hatası görülmektedir.
   * `C07b`'de (01:03) uzay boşluğunda dururken aniden sol kenarda dev bir istasyon duvarı belirmekte ve Dünya 6 saniyede gece-gündüz çizgisi dönecek kadar gerçek dışı bir hızla dönmektedir.

---

## 2. ANLATIM VE İZLEYİCİ ALGILAMASI (DRAMATİK ANALİZ)

* **Amaç ve Giriş (C01–C03):** İzleyici ana karakterin halatı kopan ekip arkadaşını kurtarmak istediğini ve bileğindeki göstergenin sönmesiyle zaman/gaz kaybı yaşadığını net anlamıştır.
* **Kuralın Görselleşmesi (C04–C06):** Uzaktaki astronotun aşağıya doğru inmesi ve Sela'nın gözlerini kapatıp dönerek kendini boşluğa bırakması güçlü bir karar anı olarak algılanmıştır.
* **01:03 Mekân Çöküşü (C07):** Sela'nın uzay boşluğunda serbest süzüldüğü anda aniden solda istasyon duvarına tutunması izleyicinin mekân algısını felç etmiştir (`FILM.md` C07'de istasyon kadraj dışıdır).
* **01:25–01:29 Iska ve Bağlantı (C09–C10):** C09'da dev eldiven ile uzaktaki küçük astronotun parmak teması yaşaması bir perspektif karmaşası doğurmuş; C10'da halatın nasıl takıldığı gösterilmeden bir anda bağlı çıkması izleyicide soru işareti yaratmıştır.
* **01:39–01:48 Final Çelişkisi (C11–C12):** İzleyici C11'deki çarpışmayı bir kurtarma değil, bir kaza ve ölümcül bir savrulma olarak görmüş; hemen ardından gelen kapak sahnesiyle çelişki doruğa çıkmıştır.
* **Diyalog Eksikliğinin Bedeli:** Telsizdeki anlamsız heceler diyalog zannedilmiş, ne söylendiği anlaşılmadığı için kafa karışıklığı büyümüştür. `FILM.md` §5'teki diyaloglar kurguya girdiğinde hem kural ("You climb, you fall behind") hem karar ("Away from me— you might reach me") hem de son onay ("Good call.") berraklaşacaktır.

---

## 3. HATA NEREDE DOĞDU? (KÖK NEDEN ANALİZİ · AGENTS.md §3)

```
                    ┌──────────────────────────────────────────────┐
                    │      THE_WRONG_BURN QA KÖK NEDEN DAĞILIMI    │
                    ├──────────────────────────────────────────────┤
                    │ 1. KURGU & SEÇİM    : %40 (C11/C12 çelişkisi)│
                    │ 2. SES MİKSİ & MODEL: %35 (Bozuk telsiz hece)│
                    │ 3. BAŞLANGIÇ KARESİ : %15 (Bere/Vizör/Halat) │
                    │ 4. HAREKET & FİZİK  : %10 (Dünya dönüşü/Darbe)│
                    └──────────────────────────────────────────────┘
```

### 3.1. Kurgu ve Seçimden Doğanlar (Edit & Selection Mismatch)
* **Final Savrulma Çelişkisi (`C11 → C12`):**
  * Montajda kullanılan C11 klibinde soldaki astronot hızla gelip sağdakine çarpmakta ve iki astronot istasyondan uzağa savrulmaktadır. Bu durum senaryodaki *"Sela eve sırtını dönüp son ışığı yakar, ip gerilir ve Bram'ı arkasından kapağa doğru çeker"* aksiyonuna tamamen terstir.
  * `C12` klibinde ise başlangıç karesi doğru olarak kapak kenarındaki tutamağı kavramış Sela'yı göstermektedir.
  * **Müdahale:** `C11` klibi savrulma klibiyle değil, kapağa doğru ortak çekilme klibiyle değiştirilmeli; C11 sonu ile C12 başı arasındaki hareket vektörü tutarlı hale getirilmelidir.
* **Plansız İstasyon Duvarı Kesmesi (`C07b · 01:03`):**
  * 01:03'te giren ve astronotun solundaki istasyon duvarına tutunduğu 3 saniyelik parça, tretmana ve sahneleme haritasına aykırıdır (C07'de istasyon kadraj dışıdır).
  * **Müdahale:** Bu plansız parça kurgudan çıkarılmalı, C07 tek parça olarak uzay ve gece Dünya'sı zemininde tutulmalıdır.
* **Kapanış Jenerik Kartı (`C13 · 01:58`):**
  * Kurgunun sonuna eklenen büyük harfli slogan yazısı ("THE WRONG BURN - ONE LIGHT...") film içi anlatı karesi değil bir jenerik kartıdır; YouTube yayın standartlarına göre ayrılmalıdır.

### 3.2. Ses Miksi ve Model Sesinden Doğanlar (Audio & Model Speech)
* **Model Sesi Replik Faciası (`T8 WRONG SOUND / A3 REPLİK BELİRSİZ`):**
  * `00:16`, `00:53`, `01:01`, `01:50` zaman kodlarındaki telsiz sesleri anlaşılmaz yapay hecelerden oluşmaktadır.
  * **Kök Neden:** Video üretiminden gelen ham ses kanalının kurguda susturulmaması.
  * **Müdahale:** Video ses parçalarının sesi tamamen kısılacak (-inf dB). `FILM.md` §5'teki temiz insan ses kayıtları (Bram bariton telsiz filtresi, Sela alto kask içi filtresi) mikslenecektir.
* **Vakum Dış Sesleri:**
  * `00:08`: Vakumda dış metalik kopma sesi.
  * `00:20 & 00:47`: LED sönerken ve gözler kapanırken rüzgâr/whoosh sesleri.
  * `01:30`: Bram elini kaldırırken ortaya çıkan seri mekanik/elektriksel tıkırtı sesi.
  * `01:39`: Uzay boşluğunda çarpışma ve sürtünme sesleri.
  * **Müdahale:** Bu yapay ses efektleri kurgudan temizlenecektir. `FILM.md` §6 ses planı uygulanarak yalnız fan uğultusu, kask içi nefes, valf tıslaması ve kask içi darbe sesleri bırakılacaktır.

### 3.3. Başlangıç Karesinden Doğanlar (Start Frame Mismatch)
* **Kıyafet ve Halat Sürekliliği (`C01 → C02`):**
  * `C01`'de kol şeridi olmayan Sela'ya `C02`'de turuncu şerit eklenmiş; sırtına ise serbest süzülen çift halat takılmıştır.
  * **Müdahale:** `ref/SELA_v1.png` ve `ref/KANCA_bosta_v1.png` referanslarına tam sadık kalınacaktır.
* **Kaskta Aşırı Parlayan Işık Küresi (`C04 · 00:30`):**
  * Bram'ın kaskındaki işaret lambası minik bir amber nokta olması gerekirken dev bir ampul/küre gibi üretilmiştir.
  * **Müdahale:** Başlangıç karesinde kehribar lamba nokta boyutunda tutulacaktır.
* **Bere ve Çift Vizör Hatası (`C05 & C06`):**
  * `C05`'te kask içinde siyah bere varken, `C06`'da bere kaybolup saçlar görünmekte ve kask camında çift vizör çizgisi çıkmaktadır.
  * **Müdahale:** `ref/SELA_yuz_v1.png` referansı kullanılmalı, bere kaldırılmalı ve küresel vizör tek parça olmalıdır.

### 3.4. Hareket ve Model Fiziğinden Doğanlar (Motion & Physics)
* **Dünya'nın Hiper Hızda Dönüşü (`T11 · C03 & C07b`):**
  * Yörünge hızına aykırı olarak Dünya yüzeyindeki bulutlar ve kıtalar saniyeler içinde yüzlerce kilometre kaymaktadır.
  * **Müdahale:** Video promptlarında arka plan kayması "very slow, imperceptible orbital drift" olarak sabitlenecektir.
* **Perspektif ve Ölçek Hatası (`T11 · C09`):**
  * 01:26'da ön plandaki dev eldiven parmağı ile uzaktaki küçük astronotun eli aynı düzlemde birbirine değmektedir.
  * **Müdahale:** `FILM.md` C09 kuralına uyulmalı; temas yaşanmamalı, aralarında bir insan boyu açık boşluk bırakılmalıdır.
* **Halat Erimesi ve Kaskatı Çarpışma (`T6 & T12 · C11`):**
  * Halat uzayda elastik salınmak yerine figürlerin gövdesi içine erimekte; çarpışmada bedenler manken gibi hareketsiz kalmaktadır.
  * **Müdahale:** C11'de çarpışma sahnesi değil, yumuşak çekme ve gergin halat hareketi kullanılacaktır.

---

## 4. ÇEKİM BAZLI REVİZYON VE EYLEM TABLOSU (C01–C13)

| Çekim | Zaman | QA Bulgusu | Kök Neden | Uygulanacak Aksiyon |
|:--:|:--:|---|:--:|---|
| **C01** | 00:00 | Halatın kaskatı durması (T9), vakumda kopma sesi (T8) | Hareket / Ses | Halat hafif süzülecek; kopma sesi silinecek, Bram R01 ("Lost my jets.") telsizden mikslenecek. |
| **C02** | 00:10 | Sırtta çift halat (S1), noktanın ateşe dönüşmesi (T11), yapay telsiz heceleri (T8) | Kare / Ses | Çift halat silinecek; nokta boyutu küçültülecek; model sesi silinip Bram R02 ("No, no— don't burn at me!") eklenecek. |
| **C03** | 00:20 | LED sönerken whoosh sesi (T8), Dünya'nın aşırı hızlı akışı (T11) | Ses / Fizik | Whoosh efekti atılacak; tıslama 1,6'da kesilecek; Bram R03 ("Cut it. You're climbing...") ve Sela R04 ("Copy. Down to two.") eklenecek. |
| **C04** | 00:30 | Bram kaskında dev ışık küresi (T6 / S5) | Başlangıç Karesi | Lamba kehribar nokta boyutuna çekilecek (`ref/BRAM_v1`); Bram R05, Sela R06, Bram R07 mikslenecek. Kapak anı (0-4 s) korunacak. |
| **C05** | 00:40 | Kask içinde siyah bere (S1), rüzgâr uğultusu (T8) | Kare / Ses | `ref/SELA_yuz_v1` kilitlenecek (bere yok); rüzgâr sesi silinecek; Bram R08 takas repliği ("At me— you're home. Away from me...") yerleştirilecek. |
| **C06** | 00:50 | Çift vizör çizgisi (T6), rüzgâr sesi (T8), anlaşılmaz fısıltı | Kare / Ses | Kask vizörü tek parça üretilecek; model sesi silinip Sela'nın kask içi R09 repliği ("Sunrise. You be there.") eklenecek. |
| **C07** | 01:00 | 01:03'te aniden beliren istasyon duvarı (S4), Dünya'nın aşırı hızlı dönüşü (T11), boş kumanda tutuşu (T13) | Kurgu / Fizik | 01:03'teki istasyon duvarı kesmesi montajdan tamamen çıkarılacak (C07'de istasyon kadraj dışıdır); Sela R10 ("Bram?") ve hat hışırtısı mikslenecek. |
| **C08** | 01:10 | Dünya üstte geçişi başarılı; kask ışığı dozu yüksek | Başarılı / Kare | Dünya'nın üstte olması senaryoya uygundur; kasktaki aşırı parlama giderilecek; müziksiz sessizlik korunacak. |
| **C09** | 01:20 | Dev eldiven ile uzaktaki figürün parmak teması (T11 / A1) | Fizik / Sahneleme | Temas iptal edilecek; aralarında bir insan boyu açık boşluk kalacak (ıska); kanca atış hazırlığı gösterilecek. |
| **C10** | 01:28 | Halatın aniden belirmesi (A1), seri mekanik tıkırtı sesi (T8) | Kurgu / Ses | C09-C10 arasındaki kanca takılması kurgusal köprüyle bağlanacak (`KANCA_cantada`); anlamsız tıkırtı sesi atılacak; Bram R11 ("I heard you. In the dark.") eklenecek. |
| **C11** | 01:38 | Astronotların çarpışıp uzaya savrulması (A1), halatın erimesi (T6), manken çarpışması (T12) | **Kurgu / Seçim (ÖLÜMCÜL)** | Savrulup kadrajdan çıkma sahnesi montajdan atılacak. Sela'nın eve sırtını dönüp son gazı yaktığı ve Bram'ı gergin iple arkasından çektiği doğru klip yerleştirilecek. |
| **C12** | 01:48 | Savrulma sonrası aniden korkulukta olma çelişkisi (S5 / A1), bozuk kadın sesi (T8) | **Kurgu / Ses** | C11'deki doğru hareketle varış darbesi (0,0 s) bağlanacak; bozuk telsiz sesi silinecek; Bram R12 ("Good call.") ve Sela'nın rahatlayan nefesi konulacak. |
| **C13** | 01:58 | Ekranda büyük başlık ve slogan kartı (T3 / T10) | Tasarım / Kurgu | Film içi sahne yerine başlık kartı montajdan ayrılacak; film Sela'nın tutamaktaki eldiveni ve boş göstergesiyle (C12) bitecektir. |

---

## 5. SAHİP İÇİN EYLEM PLANI (SIRADAKİ ADIMLAR)

1. **Kurgusal Devamlılık ve Final Düzeltmesi (En Acil Adım):**
   * **C11 ve C12 Bağlantısı:** 01:39'daki iki astronotun çarpışıp istasyondan uzaklaşarak uzaya savrulduğu klip montajdan derhal çıkarılmalıdır. Yerine senaryoya uygun olarak Sela'nın son gazı yakıp Bram'ı arkasından istasyona doğru çektiği alternatif çekim konulmalıdır. Bu değişiklik filmin sonundaki "kurtuldular mı öldüler mi?" belirsizliğini tamamen çözecektir.
   * **01:03 Duvar Kesmesi:** C07'nin ortasına giren ve astronotun aniden istasyon paneline tutunduğu 3 saniyelik parça montajdan silinmeli; C07 tek parça uzay/gece Dünya'sı olarak akıtılmalıdır.
2. **Ses ve Replik Miksi (Kurguda Hemen Yapılacaklar):**
   * Video kliplerinin tüm ham ses kanalları kapatılmalıdır (-inf dB).
   * `FILM.md` §5'teki diyaloglar kaydedilmeli ve mikslenmelidir:
     * **Bram (telsiz filtresi):** R01 ("Lost my jets."), R02 ("No, no— don't burn at me!"), R03 ("Cut it. You're climbing. You climb, you fall behind."), R05 ("Turn your back on me— and brake."), R07 ("At sunrise, I'm right in front of you."), R08 ("At me— you're home. Away from me— you might reach me..."), R11 ("I heard you. In the dark."), R12 ("Good call.").
     * **Sela (kask içi filtresi):** R04 ("Copy. Down to two."), R06 ("Negative. I can see you."), R09 ("Sunrise. You be there."), R10 ("Bram?").
   * 00:08 çarpma sesi, 00:20 ve 00:47 whoosh sesleri, 01:30'daki seri mekanik tıkırtı sesi silinmelidir.
3. **Kritik Kare ve Görsel Revizyonları (Gerektiğinde Flow'da Yeniden Üretim):**
   * `C05 & C06`: Kask içindeki siyah bere silinmeli, `ref/SELA_yuz_v1.png` ile beresiz şeffaf vizörlü yüz kilitlenmelidir.
   * `C04`: Bram'ın kaskındaki aşırı parlayan ampul küresi küçültülmeli, küçük kehribar işaret lambası yapılmalıdır.
   * `C09`: Ön plandaki dev eldiven ile uzaktaki astronotun el teması kesilmeli, aralarında bir insan boyu açık boşluk bırakılmalıdır.
