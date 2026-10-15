# 📊 THE_PLANET_THIEF — QA Değerlendirme ve İyileştirme Raporu

> **Dosya:** `THE_PLANET_THIEF.mp4` (Taslak Montaj · ~04:05 · 25 Çekim)  
> **Tarih:** 15.10.2026  
> **Kaynak Veri:** `ODA/HAM_QA_RAPORU.md` (Anlatım Testi, İzleme Formu, Süreklilik Denetimi, Teknik Tarama)  
> **Dayanak:** `AGENTS.md` §3 (Hata Nerede Doğdu), `uretim_hatti/QA_OKUMA_KILAVUZU.md`

---

## 1. YÖNETİCİ ÖZETİ VE GENEL DEĞERLENDİRME

`THE_PLANET_THIEF.mp4` montajı; ölçek hissi, devasa uzay mimarisi ve merkezinde yapay güneş bulunan gezegen kasası ("Planetary Ark") konseptiyle izleyicide **"görkemli ve ürpertici"** bir atmosfer yaratmayı başarmıştır. Kararan Güneş ve Dünya'nın devasa silindirik yapı tarafından çekilip yeni bir güneş sistemine yerleştirilmesi fikri izleyiciye geçmiştir.

Ancak dört QA merceğinin ortak analizinde iki temel problem öne çıkmaktadır:
1. **Diyalog/Replik Eksikliği (Anlatım Kopukluğu):** Montajda karakterin replikleri yer almadığı ve yalnızca nefes sesleri duyulduğu için, astronotun istasyona sabotaj amacıyla mı (hattı kesmek) yoksa tamir amacıyla mı girdiği, bileğindeki yaşam belirtilerini gördükten sonra neden duraksadığı ve sonunda neyi tetiklediği görsel olarak havada kalmıştır.
2. **Karakter ve Mekân Sürekliliği (Görsel Kırılmalar):** 34 Süreklilik sapması ve 24 Teknik kusur kaydedilmiştir. Özellikle `C19`'da astronotun sinekkaydı tıraşlı bambaşka bir yüze dönüşmesi, `C20`'de göğsünde hilal-yıldız armaları ve arka planda açık hava dağ manzarası belirmesi, `C22`'de uzay vakumunda yoğun baca dumanı çıkması acil düzeltme gerektirmektedir.

---

## 2. ANLATIM VE İZLEYİCİ ALGILAMASI (DRAMATİK ANALİZ)

* **Ana Çatışmanın Algılanması:** İzleyici Güneş'in sönmesini ve Dünya'nın çekilmesini net anlamış; ancak Elias'ın misyonunu (Dünya'yı çeken çekim alanını kesme girişimi ve sonrasındaki vazgeçiş) tam kavrayamamıştır.
* **01:40 (C11) İkilemi:** Astronot elindeki aleti enerji sütununa yaklaştırdığında bir şeyi tamir mi ettiği yoksa sabote mi ettiği anlaşılamamaktadır.
* **03:00–03:15 (C19–C20) Karar Anı:** Karakterin tereddüdü hissedilmekte ancak aleti indirip Dünya komutasına *"Do not attack. This is an evacuation"* uyarısını geçtiği diyalog olmadan eylemin anlamı tamamlanamamaktadır.
* **Çözüm:** `FILM.md` §5'te yer alan 11 replik (Elias telsiz + AI kadın ses) kurguya eklendiğinde anlatım testi %100 berraklığa ulaşacaktır.

---

## 3. HATA NEREDE DOĞDU? (KÖK NEDEN ANALİZİ · AGENTS.md §3)

```
                    ┌──────────────────────────────────────────────┐
                    │     THE_PLANET_THIEF QA KÖK NEDEN DAĞILIMI   │
                    ├──────────────────────────────────────────────┤
                    │ 1. BAŞLANGIÇ KARESİ : %45 (Yüz/Alet/Mekân)   │
                    │ 2. SES MİKSİ & KURGU: %30 (Vakum sesi/Replik)│
                    │ 3. HAREKET & MODEL  : %15 (Boşta dönen alet) │
                    │ 4. FİZİK ÇELİŞKİSİ  : %10 (Vakumda duman)    │
                    └──────────────────────────────────────────────┘
```

### 3.1. Başlangıç Karesinden Doğanlar (Start Frame Mismatch)
* **Elias'ın Yüz ve Kıyafet Değişimi (`S1 LOOK JUMP`):**
  * `C02`: Kır saçlı, sakallı, şeffaf vizörlü kask.
  * `C11`: Yüz hatları değişmiş, sağ kolda turuncu şerit ve siyah omuz pedi.
  * `C19`: **Sinekkaydı tıraşlı, sakalsız, alnında yara olan yabancı bir yüz.**
  * `C20`: Tekrar sakallı yüze dönüş; fakat göğüste daha önce olmayan hilal-yıldız armaları.
  * **Kök Neden:** `ref/1.ELIAS_v1.png` sayfası yerine bağımsız promptlar kullanılması.
  * **Müdahale:** `1.ELIAS_v1.png` dört panelli referans sayfası kilitlenecektir.
* **Alet Karmaşası (Kesici vs Matkap vs Silah):**
  * `C09`: Elde çift namlulu kutu cihaz.
  * `C11`: İnce uçlu elektrikli matkap.
  * `C19`: İki elle tutulan büyük endüstriyel tüfek/silah.
  * **Kök Neden:** Plandaki `8.AKSESUARLAR_v1.png` (mat siyah kapalı plazma kesici) görselinin kare üretiminde kullanılmaması.
  * **Müdahale:** Tek tip mat siyah plazma kesici tüm iç çekimlerde sabitlenecektir.
* **Mekân Sıçraması (C20 · 03:10):**
  * Astronot karanlık enerji bölmesindeyken birden arkasında bulutlar, sarp dağlar ve güneş ışığı olan açık hava terasında beliriyor.
  * **Kök Neden:** Modelin "observation deck" istemini açık hava terası olarak yorumlaması.
  * **Müdahale:** `6.GOZLEM_BOLMESI_v1.png` iç holü ve panoramik cam yarığı referans verilecektir.
* **Kurtarma Gemisi ve Hangar Geometrisi (`C05–C08`):**
  * Mekik kanatlı kama formundan mermi silindirine dönüşmekte; tavan soketi ve kıskaç geometrisi erimektedir.
  * **Müdahale:** `2.KURTARMA_GEMISI_v1.png` ve `5.YANASMA_KORIDOR_v1.png` panelleri zorunlu tutulacaktır.

### 3.2. Hareket ve Fizikten Doğanlar (Motion & Physics)
* **Boşlukta Dönen Alet Ucu (T13 · C11):**
  * Matkap ucu metal yuvaya hiç değmeden birkaç santim havada boşa dönmektedir.
  * **Müdahale:** Kesici hatta temas etmeyecek, plazma kesici brakete doğrultulmuş ve kapalı tutulacaktır (`FILM.md` C11 kuralı).
* **Vakumda Baca Dumanı (T7 · C22):**
  * Uzay boşluğunda istasyonun ağzından baca dumanı gibi siyah dumanlar püskürmektedir.
  * **Müdahale:** Uzay vakumunda duman üretilmeyecek; yalnızca geminin amber ışıkları ve sönen Güneş kalacaktır.
* **Bıyıkta Kalan Mavi Işık Lekesi (T6 · C20):**
  * Bileklik kaldırıldığında dudak üstüne mavi ışık artefaktı yapışıp kalmaktadır.
  * **Müdahale:** Başlangıç karesinde bileklik göğüs hizasında başlatılacak, yüze temas ettirilmeyecektir.
* **İticisiz Yükselme (T9 · C06/C07):**
  * Mekik iticileri ateşlenmeden havada asansör gibi yükselmektedir.
  * **Müdahale:** Dikey iticiler aktif gösterilecek ya da sahneleme açısı değiştirilecektir.

### 3.3. Kurgu ve Ses Miksinden Doğanlar (Audio & Edit)
* **10 Saniyelik Sert Ses Kesilmeleri (S7 SOUND JUMP):**
  * Her 10 saniyede bir (00:10, 00:20, 00:30, 00:40...) ambiyans ve müzik hard cut ile sıfırlanıp yeniden başlamaktadır.
  * **Müdahale:** Mekân içi yataklar klipler boyunca kesintisiz akıtılacak (`timeline.json yataklar`), mekân değişimlerinde 1-1.5 saniye crossfade uygulanacaktır.
* **Vakum Dışı Ses Sızıntıları (T8 WRONG SOUND):**
  * `C01`, `C05`, `C18`, `C21`, `C22`, `C23` dış uzay çekimlerinde jet motoru, fırtına rüzgârı, gök gürültüsü ve kıyıya vuran dalga sesleri vardır.
  * **Müdahale:** Klip sesleri dış çekimlerde kapatılacak, yalnız `Y1` (düşük frekanslı basınç tonu + radyo paraziti) bırakılacaktır.
* **Ses Senkron Kayması (T8 · C08):**
  * 01:15'te kilitlenen kıskaç sesi 01:17'de patlamaktadır. Senkron kurguda 2 saniye öne çekilecektir.

---

## 4. ÇEKİM BAZLI REVİZYON VE EYLEM TABLOSU (C01–C25)

| Çekim | Zaman | QA Bulgusu | Kök Neden | Uygulanacak Aksiyon |
|:--:|:--:|---|:--:|---|
| **C01** | 00:00 | Vakumda rüzgâr ve elektrik sesi (T8) | Ses / Kurgu | Klip sesi kapatılacak, Y1 dış uzay yatağı ve Elias'ın açılış monoloğu (R01) eklenecek. |
| **C02** | 00:10 | Kask arkasında metal kabuk sıçraması (S1) | Başlangıç Karesi | `1.ELIAS_v1.png` şeffaf vizörlü kaskına sadık kalınacak. |
| **C03** | 00:20 | Kokpit içi konsol ışık sıçraması (S2 / S4) | Başlangıç Karesi | `3.KOKPIT_v1.png` camgöbeği konsol ışıkları ve dikmeler hizalanacak. |
| **C04** | 00:30 | Masada büyük monitör belirmesi (S4) | Başlangıç Karesi | Konsolun sağındaki küçük dikdörtgen ekran korunacak, 9.GUNES görüntüsü oturtulacak. |
| **C05** | 00:40 | Vakumda jet motoru sesi (T8), mekiğin gövdede belirmesi | Ses / Anlatım | Dış vakum sesi kapatılacak; kokpitten dış genel plana geçiş ölçeği korunacak. |
| **C06** | 00:50 | Mekikte motor podları türemesi (S1), iticisiz süzülme (T9) | Kare / Model | `2.KURTARMA_GEMISI_v1.png` formuna dönülecek; dikey itici ışığı eklenecek. |
| **C07** | 01:00 | Mekiğin mermiye dönüşmesi (S1), arkada açık uzay (S4) | Başlangıç Karesi | Kapalı hangar içi ve tek tip mekik formu `5.YANASMA_KORIDOR` ile eşlenecek. |
| **C08** | 01:10 | Kıskaç erimesi (T6), kilit sesinin 2 sn gecikmesi (T8) | Model / Kurgu | Kıskaç erimesi kesmede çözülecek; ses efekti 01:15'e çekilecek. |
| **C09** | 01:20 | Elde kutu alet olması (S1) | Başlangıç Karesi | `8.AKSESUARLAR_v1.png` kapalı plazma kesicisi yerleştirilecek. |
| **C10** | 01:30 | Koridor sonunda odanın şekil değiştirmesi (S4) | Başlangıç Karesi | `6.GOZLEM_BOLMESI_v1.png` dikey hatlı derinlik paneli kullanılacak. |
| **C11** | 01:40 | Matkabın havada dönmesi (T13), sabotajın anlaşılmaması (A1) | Model / Anlatım | Plazma kesici hatta doğrultulacak (temas yok); R05 repliği ("One cut. We get our world back.") eklenecek. |
| **C12** | 01:50 | Sol bilekte cihazın yoktan belirmesi (S1) | Başlangıç Karesi | `8.AKSESUARLAR` bilek tarayıcısı C09 ve C11'de de sol kolda gösterilecek. |
| **C13** | 02:00 | Yabancı gezegenin mor adaları | Başarılı | Gezegen tasarımı ve tutma yayı net, C14 ile sürekliliği tam. |
| **C14** | 02:10 | Astronotun adım atmadan kayması (T13) | Model | Elias korkulukta sabit duracak (`FILM.md` kuralı), yürüme üretilmeyecek. |
| **C15** | 02:20 | Işık yönünün ters dönmesi (S2) | Başlangıç Karesi | Gezegeni aydınlatan yapay güneş ışığı sağdan verilecek (7.KASA'ya uygun). |
| **C16** | 02:30 | Gezegenlerin simetrisinin bozulması (S4) | Başlangıç Karesi | `7.KASA_v1.png` gezegen yerleşimi ve üç halkalı güneş korunacak. |
| **C17** | 02:40 | Güneş'in önünde volkanik kül gibi duman (T7) | Model / Kare | Kararan cephe duman gibi değil, ışıksız geometrik karanlık sınır olarak gösterilecek. |
| **C18** | 02:50 | Vakumda derin uğultu (T8) | Kurgu / Ses | Dış ses temizlenecek, Y1 yatağına dönülecek. |
| **C19** | 03:00 | Sinekkaydı tıraşlı yüz (S1), tüfek benzeri silah (S1) | Başlangıç Karesi | `1.ELIAS_v1.png` sakallı profil paneli ve plazma kesicisi bel hizasında indirilecek. R09 repliği eklenecek. |
| **C20** | 03:10 | Arkada dağ manzarası (S4), göğüste armalar (T3), bıyıkta mavi leke (T6) | Başlangıç Karesi | Açık hava manzarası silinecek, iç gözlem holüne dönülecek; armalar silinecek, leke temizlenecek. R10 repliği eklenecek. |
| **C21** | 03:20 | Dünya'nın silindire girişi | Başarılı | Çekim ve geçiş başarılı; arka plandaki vakum rüzgâr sesi temizlenecek. |
| **C22** | 03:30 | İstasyon ağzından çıkan siyah baca dumanı (T7 / S6) | Model / Kare | Uzay boşluğundaki duman tamamen silinecek, temiz silindir uçuşu kalacak. |
| **C23** | 03:40 | Okyanus dalga sesi (T8), Dünya arkasında hayalet kopya (T2) | Ses / Model | Dalga sesi miksten atılacak; Dünya halka içinde tek rijit küre olarak tutulacak. |
| **C24** | 03:50 | Kıtaların aniden Amerika'ya dönmesi (S4) | Başlangıç Karesi | Dünya'nın Afrika kıtası yönü C23 ile aynı açıda kilitlenecek. R11 final dış sesi eklenecek. |
| **C25** | 04:00 | Kapanış başlık kartı | Tasarım | Sabit afiş düzeni kurgusal tercihe göre korunacak. |

---

## 5. SAHİP İÇİN EYLEM PLANI (SIRADAKİ ADIMLAR)

1. **Ses ve Replik Miksi (Kurguda Hemen Yapılacaklar):**
   * `FILM.md` §5'te yazılı olan 11 replik (Elias telsiz + AI kadın ses) seslendirilmeli ve kurguya eklenmelidir. (Bu adım 01:40 ve 03:00'daki anlam belirsizliğini tamamen çözecektir).
   * Her 10 saniyede bir yaşanan ses kesilmeleri 1 saniyelik crossfade ile bağlanmalıdır.
   * Dış uzay çekimlerindeki fırtına, jet motoru, gök gürültüsü ve dalga sesleri temizlenmelidir.
   * C08 kenetlenme sesi 01:15'e çekilmelidir.
2. **Kritik Çekimlerin Yeniden Üretimi (Görsel Düzeltmeler):**
   * **C19 & C20 (En Kritik):** Elias'ın sakalsız yüzü ve arkadaki açık hava dağ manzarası iptal edilmeli; `1.ELIAS_v1.png` ve `6.GOZLEM_BOLMESI_v1.png` referanslarıyla istasyon içinde yeniden üretilmelidir.
   * **C11:** Boşlukta dönen matkap ucu yerine elde duran kapalı plazma kesici başlangıç karesi verilmelidir.
   * **C22:** Uzayda çıkan siyah baca dumanı temizlenmelidir.
   * **C05–C08:** Kurtarma gemisinin gövdesi ve kenetlenme kıskaçları `2.KURTARMA_GEMISI_v1.png` referansına kilitlenmelidir.
