# 📊 THE_MAYDAY_SEA — QA Değerlendirme ve İyileştirme Raporu

> **Dosya:** `the mayday sea.mp4` (Taslak Montaj · ~03:54)  
> **Tarih:** 15.10.2026  
> **Kaynak Veri:** `ODA/HAM_QA_RAPORU.md` (Anlatım Testi, İzleme Formu, Süreklilik Denetimi, Teknik Tarama)  
> **Dayanak:** `AGENTS.md` §3 (Hata Nerede Doğdu), `uretim_hatti/QA_OKUMA_KILAVUZU.md`

---

## 1. YÖNETİCİ ÖZETİ VE GENEL DEĞERLENDİRME

`the mayday sea.mp4` kurgusu, projenin en temel dramatik ve tematik vaadini (**"Yıldızlar arasındaki okyanus yardım çağırmıyordu, yanıtlanmayı bekliyordu"**) izleyiciye başarıyla aktarmıştır. Dış izleyici simülasyonu ve anlatım testi, izleyicinin hikâyeyi baştan sona eksiksiz anladığını, canavar yerine bütün okyanusun canlı bir organizma olduğunu kavradığını ve finalde Mara'nın kendi sesinin yeni bir tuzağa dönüşmesiyle derin bir tekinsizlik hissi yaşadığını doğrulamaktadır.

Bununla birlikte, ham QA raporlarında listelenen **19 Tarama bulgusu**, **13 Süreklilik sapması** ve **6 Anlatım sorunu**; özellikle **karakter/mekân başlangıç kareleri**, **uzay vakumu ses miksi** ve **fizik/hareket kararları** üzerinde net revizyonlar gerektirmektedir.

---

## 2. DÖRT MERCEĞİN SENTEZİ VE DRAMATİK BULGULAR

### 2.1. Anlatım ve İzleme (Ne Oldu, Kim, Amaç, Bedel, His)
* **Temel Başarı:** Hikâye omurgası tam oturmuştur. İzleyici, Mara'nın yardım çağrısına gidişini (00:15), vericinin kapalı olduğunu keşfini (00:50), kendi sesini duyduğu andaki şoku (01:55) ve acil ayrılma kolunu çekerek kaçışını (02:43–03:08) net bir neden-sonuç zinciriyle takip edebilmiştir.
* **A1 Kafa Karışıklığı (00:24):** 00:24'te konuşan erkek sesin tonu, 00:11'deki kazazede çağrısıyla aynı tonda olduğu için gemi bilgisayarı/yardımcı pilot mu yoksa istasyondaki kazazede mi olduğu ilk anda ayırt edilememiştir.
* **A1 Kafa Karışıklığı (01:59):** Uzaydaki okyanusun dibinde 18. yüzyıl tarzı ahşap yelkenli kalyonların kamaralarında fenerler yanarak yüzmesi, bilimkurgu evreninin gerçekçiliğini kırmıştır.
* **A3 Replik Bozulması (01:04):** Mara'nın *"Then who is call— is calling?"* repliğinde ses modelinden kaynaklanan bir kekeleme/takılma izleyici tarafından anında fark edilmiştir.
* **A4 Dudak Senkronu Şüphesi (03:32):** Finalde kokpitte telsizden kendi sesinin kopyası gelirken Mara'nın dudaklarının aralık olması, cümleyi kendisinin mi söylediği yoksa telsizden mi geldiği konusunda anlık tereddüt yaratmıştır.

---

## 3. HATA NEREDE DOĞDU? (KÖK NEDEN ANALİZİ · AGENTS.md §3)

`AGENTS.md` Madde ④ gereğince yeni kural yazılmaz; hatalar sınıflandırılarak doğduğu yerde çözülür:

```
                    ┌──────────────────────────────────────────────┐
                    │      THE_MAYDAY_SEA QA KÖK NEDEN DAĞILIMI    │
                    ├──────────────────────────────────────────────┤
                    │ 1. BAŞLANGIÇ KARESİ : %40 (Kıyafet/Yelkenli) │
                    │ 2. SES MİKSİ & KURGU: %30 (Vakum sesi/Müzik) │
                    │ 3. HAREKET & MODEL  : %20 (Ters itki/Kol)    │
                    │ 4. ANLATIM          : %10 (AI ses kimliği)   │
                    └──────────────────────────────────────────────┘
```

### 3.1. Başlangıç Karesinden Doğanlar (Start Frame / Reference Mismatch)
* **Mara'nın Tulum ve Kask Sürekliliği (S1 LOOK JUMP):**
  * `C02`: Lacivert omuzluk, siyah göğüs askısı, kaskta kilit parçası.
  * `C05`: Omuzluklar beyaza dönmüş, kolda turuncu şeritler, kask yan bağlantısı yuvarlak yuvaya dönüşmüş.
  * `C07`: Yeniden lacivert omuzluk, sağ yanakta yeni yaralar.
  * `C12`: Kask aşırı derecede çizik, iki yanakta yara izi.
  * `C17`: Sol göğüste daha önce hiç olmayan yuvarlak lacivert-sarı arma.
  * `C22`: Sol kolda iki adet turuncu şerit.
  * **Kök Neden:** Kare üretiminde `ref/1.MARA_v1.png` referans sayfası yerine bağımsız istemler kullanılması.
  * **Müdahale:** `1.MARA_v1.png` referans görseli kilitlenecek; fildişi basınç giysisi, lacivert omuzluk, dar yanık turuncu ön kol bantları ve sağ elmacık kemiğindeki tek yara tüm yakın çekimlerde sabitlenecektir.
* **Uzayda Ahşap Kalyon (T11 OTHER / S4 WORLD JUMP · C13):**
  * Okyanusun dibinde direkli ahşap korsan/kalyon gemisi çıkmıştır.
  * **Kök Neden:** `4.OKYANUS_v1.png` `wreck fleet panel` (kısa süpürme kanatlı mekik ve silindirik modüller) yerine modelin genel "sunken ship" çağrışımına izin verilmesi.
  * **Müdahale:** C13 başlangıç karesi bilimkurgu keşif gemisi ve grafit uzay modülü enkazı olarak yeniden tasarlanacaktır.
* **İstasyon ve Koridor Geometrisi (S4 / S5):**
  * `C03 → C04`: İstasyon kenetlenme kapısındaki kolların şekil değiştirmesi.
  * `C06 → C07`: Duvardaki verici kutusunun içindeki siyah modülün beyaz sigorta kutusuna dönüşmesi.
  * **Müdahale:** `5.ISTASYON_v1.png` ve `8.AKSESUARLAR_v1.png` panelleri başlangıç karesine referans verilecek.

### 3.2. Hareket ve Fizikten Doğanlar (Motion & Physics)
* **Ters Motor İtişi (T11 OTHER · C20):**
  * Gemi istasyondan ayrılırken motorlar sağa doğru ateşlenmekte, ancak gemi itiş yönünün tersine (kendi motor ateşinin içine, sağa doğru) kaymaktadır.
  * **Müdahale:** Motor alevleri istasyona (sola) doğru bakmalı ve gemiyi sağa itmeli ya da gemi sola hareket ediyorsa motorlar sağa bakmalıdır.
* **Uzay Vakumunda Damlayan Sıvı (T7 WRONG PARTICLES · C18):**
  * Kenetlenme halkasını saran sıvıdan aşağı doğru 1g yerçekimi varmış gibi damlalar kopup düşmektedir.
  * **Müdahale:** Sıvı, metal halkayı sıkıca saran gergin ve pürüzsüz bir kordon olarak hareket etmeli, serbest damlama üretilmemelidir.
* **Kokpit İçi Su Damlaması (T7 WRONG PARTICLES · C19):**
  * Kapalı kokpit kabininde tavandan kontrol konsoluna yağmur gibi su damlamaktadır.
  * **Müdahale:** Kokpit kuru basınç kabinidir (`FILM.md` §3 MEKÂN IŞIĞI/ORTAM). Başlangıç karesi ve prompttaki su sızıntısı kaldırılacaktır.
* **Ayrılma Kolu Eforu (T12 WEIGHTLESS EFFORT · C19):**
  * Mara acil ayrılma kolunu çekerken el sadece titremekte, ağır mekanik kilit direnci hissedilmemektedir.
  * **Müdahale:** Mara'nın kolu omzuyla çekişi, menteşenin mekanik durdurucuya sert çarpışı kadrajlanacaktır.

### 3.3. Kurgu ve Ses Miksinden Doğanlar (Sound & Edit)
* **Uzay Vakumunda Dış Mekanik / Su Sesleri (T8 WRONG SOUND):**
  * `C01`, `C03`, `C04`, `C18`, `C21` çekimlerinde vakum ortamında dış su dalgalanması, metal tıkırtısı ve motor uğultusu duyulmaktadır.
  * **Müdahale:** Modelin video klibine gömdüğü sesler dış çekimlerde kapatılacak (`klip_sesi: false`); dış uzay yatağı (`Y1`: alçak basınç tonu + radyo paraziti) ve müzik öne alınacaktır.
* **Müzikte Sert Kesilme (S7 SOUND JUMP · 01:39):**
  * C10'daki yüksek tempolu synth müzik, C11'de telsiz kutusu yakın çekimine geçildiğinde bıçak gibi kesilmektedir.
  * **Müdahale:** 1-1.5 saniyelik çapraz sönümlenme (crossfade) ile tekinsiz alçak frekanslı drone yatağına geçilecektir.
* **Replik Hataları ve Miks Dengesizliği:**
  * `01:04` R08: *"Then who is call— is calling?"* takılması düzeltilecek.
  * `03:23` R16: *"We're clear of the field"* repliği yükselen müzik seviyesinin altından kurtarılıp mikste +2.5 dB parlatılacaktır.
  * `00:24` R04: AI sesine hafif telsiz komuta rezonansı eklenerek 00:11'deki yorgun kazazede sesinden ayrıştırılacaktır.

---

## 4. ÇEKİM BAZLI İYİLEŞTİRME VE REVİZYON TABLOSU

| Çekim | Zaman | QA Bulgusu | Kök Neden | Uygulanacak Aksiyon |
|:--:|:--:|---|:--:|---|
| **C01** | 00:04 | Vakumda su çalkalanma sesi (T8) | Kurgu / Ses | Klip sesi kapatılacak, Y1 dış uzay yatağı ve Mara'nın açılış dış sesi (R01) mikslenecek. |
| **C03** | 00:24 | AI repliği kazazede çağrısıyla aynı tonda (A1), dış su sesi (T8) | Ses / Anlatım | Dış su sesi temizlenecek; AI telsiz repliğine (R04) ayırt edici synthesizer/sistem tonu verilecek. |
| **C04** | 00:29 | İstasyon kenetlenme kollarında biçim sıçraması (S4) | Başlangıç Karesi | `5.ISTASYON_v1.png` soket paneli kullanılarak başlangıç karesi üretilecek. |
| **C05** | 00:39 | Mara'nın tulumunda beyaz omuzluk ve turuncu şerit sıçraması (S1) | Başlangıç Karesi | `1.MARA_v1.png` tulum detayları (lacivert omuzluk, dar şerit) korunacak. |
| **C06** | 00:50 | Duvardaki elektrik kablosundan su damlaması (T7) | Hareket / Kare | Açık fiş ve soket kuru metal olarak üretilecek, su damlası silinecek. |
| **C07** | 00:59 | Verici kutusunun sigorta kutusuna dönüşmesi (S5), yanakta yeni yara (S1) | Başlangıç Karesi | `8.AKSESUARLAR_v1.png` siyah verici modülü ve tek sağ elmacık yarası kilitlenecek. |
| **C07/08**| 01:04 | *"Then who is call— is calling?"* takılması (T8 / A3) | Ses Üretimi | Mara'nın R08 repliği pürüzsüz tek cümle olarak yeniden seslendirilecek. |
| **C08** | 01:09 | Suda boş kasktan sürekli hava kabarcığı çıkması (T7) | Hareket / Model | Kask suyla dolu ve boş olduğu için hava kabarcığı akışı seyreltilecek / kesilecek. |
| **C10** | 01:28 | Hızlı tempolu synth müzik (A6) | Ses / Kurgu | Gerilim atmosferine uygun tekinsiz, yavaş drone yatağına çekilecek. |
| **C11** | 01:39 | Müzikte ani bıçak kesilmesi (S7 / T8), kablonun yoktan belirmesi (T6) | Kurgu / Kare | Müzik kesilmesi crossfade ile yumuşatılacak; telsiz kablosu ilk kareden itibaren zeminde olacak. |
| **C12** | 01:48 | Kaskta aşırı kir/çizik ve iki yanakta yara (S1), pencerede mercan (S4) | Başlangıç Karesi | `1.MARA_v1.png` portresi uygulanacak; pencere arkasına mercan/deniz tabanı yerine derin uzay suyu konacak. |
| **C13** | 01:59 | Okyanus dibinde ahşap yelkenli kalyonlar (T11 / S4 / A1) | Başlangıç Karesi | Ahşap kalyon yerine `4.OKYANUS_v1.png` paneline uygun bilimkurgu uzay gemisi ve mekik enkazları yerleştirilecek. |
| **C17** | 02:38 | Sol göğüste yeni beliren yuvarlak logo (S1) | Başlangıç Karesi | `1.MARA_v1.png` soyut üçgen altın-mavi rozeti haricinde göğse ekstra logo konulmayacak. |
| **C18** | 02:49 | Vakumda damlayan mavi sıvı ve sıvı sesi (T7 / T8) | Hareket / Ses | Dış sıvı sesleri atılacak; mavi sıvı halkaya dolanan gergin ve rijit bir kordon olarak tutulacak. |
| **C19** | 02:59 | Kokpitte su damlaması (T7), kol çekme eforu zayıf (T12 / A4) | Hareket / Kare | Kokpit tavanından su damlaması kaldırılacak; kol çekme eforu mekanik direnç hissiyle yeniden üretilecek. |
| **C20** | 03:09 | Ters motor itişi (T11), metal çubukların yüzeyden çıkması (T2) | Hareket / Model | İtki yönü fiziksel olarak doğru yöne çevrilecek; ayrılma arayüzü boşluğu korunacak. |
| **C21** | 03:18 | Vakumda güçlü motor sesi (T8), okyanusta dairesel halka çerçeve (S4) | Kurgu / Kare | Dış motor sesi kısılacak; okyanus containment çerçevesi köşeli dikdörtgen kirişlere sadık kalacak. |
| **C22** | 03:23 | *"We're clear of the field"* repliğinin boğuk kalması (A3 / A6) | Kurgu / Miks | Replik seviyesi yükseltilip müzik ve motor uğultusunun üstüne çıkarılacak. |
| **C23** | 03:32 | Mara'nın dudaklarının aralık olması (A4) | Seçim / Kare | Alıcıdan kendi sesi gelirken Mara'nın dudaklarının tamamen kapalı olduğu kare/aralık seçilecek. |
| **C24** | 03:48 | Sabit bitiş başlık kartı (T10 / T3) | Tasarım / Kurgu | Başlık kartı istenen bir afişleme ise korunacak, hareketli devam etmesi istenirse son 6 s video üretilecek. |

---

## 5. SAHİP İÇİN EYLEM PLANI (SIRADAKİ ADIMLAR)

1. **Ses Düzeltmeleri (Hızlı Revizyon - Kurguda Çözülecekler):**
   * `R08` (*"Then who is calling?"*) repliği tek parça üretilip yerleştirilecek.
   * `01:39` kesmesindeki müzik sıçraması crossfade ile bağlanacak.
   * `03:23`'teki `R16` repliği mikste parlatılacak.
   * Dış uzay sahnelerindeki su şıpırtısı ve vakum dışı motor sesleri temizlenecek.
2. **Kritik Çekimlerin Yeniden Üretimi (Görsel Düzeltmeler):**
   * **C13 (Öncelikli):** Ahşap yelkenli gemi yerine uzay enkazı başlangıç karesi oluşturulacak.
   * **C18 & C19:** Kokpitteki su damlaması kaldırılacak, acil ayrılma kolunun ağırlığı artırılacak.
   * **C20:** Motor itiş yönü fizik kurallarına uygun hale getirilecek.
   * **C05, C07, C12, C17:** Mara'nın tulum/kask ve yara sürekliliği `ref/1.MARA_v1.png` referansı kullanılarak kilitlenecek.
