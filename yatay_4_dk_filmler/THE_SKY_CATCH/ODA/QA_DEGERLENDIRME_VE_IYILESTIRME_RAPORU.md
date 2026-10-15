# 🔬 THE_SKY_CATCH — QA Değerlendirme, Hata Analizi ve İyileştirme Raporu

**Tarih:** 15 Ekim 2026  
**İncelenen Materyal:** `the sky catch.mp4` (Sahip montajı / kurgulanmış taslak video, ~02:41)  
**Kapsam:** Anlatım Testi · İzleme Formu (Sahip A + Dış İzleyici B) · Süreklilik Denetimi · Teknik Tarama  
**İlgili Standartlar:** `uretim_hatti/QA_OKUMA_KILAVUZU.md` · `AGENTS.md` §1, §3, §5  

---

## 1. YÖNETİCİ ÖZETİ

Sahibin `the sky catch.mp4` üzerinde yaptığı 02:41'lik kurgulanmış montaja uygulanan 4 katmanlı QA denetimi; hikâye omurgası, karakter sürekliliği, görsel fizik ve ses miksi açısından filmin güçlü yönleri ile revizyon gerektiren noktalarını açıkça ortaya koymuştur.

* **Ana Başarı:** İki uzay aracının düşüş sırasında yanaşması, Sana'nın uzay yürüyüşü, servis kapağının açılması, çekme kolunun çıkması ve KITE'ın kıskacıyla kilitlenmesi şeklindeki mekanik eylem zinciri izleyici tarafından adım adım ve net biçimde anlaşılmıştır (Anlatım Testi §1 ve B1 teyidi).
* **Temel Sorun (Anlatım):** Filmde içeride **48 yolcu bulunduğu** ve **modülün Dünya'ya kontrolsüz düştüğü** bilgisi 02:36'daki bitiş yazısına kadar ekranda verilmemiştir. Ayrıca filmde **hiçbir diyalog/telsiz sesi yer almadığı** için dramatik gerilim oluşmamış, izleyiciler filmi gerilim dolu bir kurtarma operasyonu yerine *"sakin bir teknik işlem"* olarak deneyimlemiştir.
* **Temel Sorun (Görsel Süreklilik):** Kadın astronotun yüzü 3 ayrı kadına dönüşmüş, tulumundaki turkuaz şeritler maviye kaymış, göğsüne yazılı armalar ve omuzlarına ABD bayrakları eklenmiştir. Erkek pilotun da yüzü ve kolundaki şeritler sahneler arasında değişmiştir.
* **Temel Sorun (Ses ve Fizik):** Sert uzay vakumunda geçerken dış çekimlerde aşırı yüksek ve yankılı metal sürtünme/çarpma sesleri mikslenmiş, roket motoru ateşlendiğinde ise itki sesi susmuştur. Roket alevi vakum fiziği yerine atmosferik meşale/duman bulutları üretmiştir.

---

## 2. HATANIN DOĞDUĞU YER ANALİZİ (`AGENTS.md` §3)

`QA_OKUMA_KILAVUZU.md` ve `AGENTS.md` §3 uyarınca tüm bulgular doğduğu kaynak katmanına göre sınıflandırılmıştır:

```
┌──────────────────────┬─────────────┬────────────────────────────────────────────────────────┐
│ Hatanın Doğduğu Yer  │ Bulgu Sayısı│ Temel Teşhis                                           │
├──────────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ 1. Başlangıç Karesi  │ 22 bulgu    │ Karakter yüzleri, tulum renkleri, bayrak/metinler,     │
│    (kare)            │             │ modül üstündeki hasar dokusu ve kapak menteşe yönü     │
│                      │             │ başlangıç karelerinde referanslarla sabitlenmemiş.    │
├──────────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ 2. Hareket (Video)   │ 16 bulgu    │ 0 g yerine 1 g gibi yürüme/basma, vakumda dumanlı alev,│
│    (hareket)         │             │ tel gibi katı kablo, el-nesne tutunamaması ve kolun   │
│                      │             │ 9 saniye hareketsiz kalması.                           │
├──────────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ 3. Seçim & Kurgu     │ 14 bulgu    │ 180° aks atlamaları (C05→C06, C11→C12), ters el        │
│    (seçim / kurgu)   │             │ yakın planı (C18), temas anlarının kesmeyle            │
│                      │             │ atlatılmaması, havada süzülürken ani basışa geçiş.    │
├──────────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ 4. Ses Miksi         │ 8 bulgu     │ 24 repliğin tamamen eksik olması, vakumda yankılı dış │
│    (kurgu / ses)     │             │ metal gürültüleri, roket ateşleme sesinin olmaması,    │
│                      │             │ C10'daki istenmeyen vokal nefes/gülme sesi.            │
├──────────────────────┼─────────────┼────────────────────────────────────────────────────────┤
│ 5. Anlatım           │ 5 bulgu     │ 48 kişi ve Dünya'ya düşüş tehlikesinin ilk 20 saniyede │
│    (anlatım)         │             │ verilmemesi, sonucun yalnızca bitiş kartına kalması.   │
└──────────────────────┴─────────────┴────────────────────────────────────────────────────────┘
```

---

## 3. ÖNCELİKLİ BULGULAR VE MÜDAHALE PLANI

### A. ÖLÜMCÜL / KRİTİK REVİZYONLAR (Hemen Yapılacaklar)

1. **Açılış Hook'u ve 48 Yolcu Tehlikesinin Girişte Verilmesi (Anlatım & Kurgu):**
   - **Sorun:** Seyirci `02:36`'ya kadar modülün içinde insan olduğunu ve Dünya'ya düştüğünü bilmiyor.
   - **Müdahale:**
     - **C01 (00:01):** Dane'in dış sesi kurguda girecek: *"The last elevator car was falling to Earth. We had one ship to catch it."*
     - **C02 (00:10):** Sana'nın repliği girecek: *"Forty-eight people inside. Cabin pressure is holding."*
     - **C02 Görüntü:** Kurguda ekrana grafik bindirme eklenecek: `48 ON BOARD / CABIN PRESSURE STABLE`.
     - Bu müdahale YouTube ilk 30 saniye kuralını doğrudan karşılar ve izleyiciyi ilk saniyeden itibaren ekrana kilitler.

2. **24 Replik Seslendirilmeli ve Timeline'a İşlenmeli (Ses / Kurgu):**
   - **Sorun:** Montajda hiçbir konuşma yoktur; telsiz ve kask içi iletişim tamamen boştur.
   - **Müdahale:** `FILM.md` §5'teki R01–R24 metinleri kaydedilecek (Dane için olgun/sakin erkek ses, Sana için net/kararlı kadın ses) ve `timeline.json` zaman kodlarına göre yerleştirilecektir.

3. **Karakter ve Kostüm Tutarlılığı (Başlangıç Karesi):**
   - **Sorun:** Sana'nın tulumu turkuazdan maviye dönmüş, göğsüne yazılı armalar ve omuzlarına ABD bayrakları çıkmış, yüzü 3 farklı kadına dönüşmüştür. Erkek pilotun da yüzü ve kol şeritleri değişmiştir.
   - **Müdahale:**
     - Başlangıç kareleri üretilirken `1.DANE_v1.png` ve `2.SANA_v1.png` referansları görsel girdisi olarak verilecek.
     - Promptlardaki `no lettering, numbers, subtitles, logos or watermarks` kuralı korunacak; modelin bayrak veya metin uydurduğu kareler elenecektir.
     - Sana: pearl-white tulum + turkuaz üst kol bantları + üçgen yazısız rozet.
     - Dane: ivory tulum + yanık turuncu üst kol bantları + yuvarlak mavi-altın rozet.

4. **C18 Ters El Hatasının Düzeltilmesi (Kare / Kurgu):**
   - **Sorun:** C17'de sağ elle itilen kontrol kolu, C18 yakın planda sol elle tutuluyor.
   - **Müdahale:** C18 başlangıç karesi `5.KOKPIT` referansıyla yenilenecek ve eldivenin **sağ el** olduğu (`Dane's right gloved hand`) açıkça sabitlenecektir.

5. **Vakumda Ses Tasarımının Düzeltilmesi (Kurgu / Ses):**
   - **Sorun:** Dış uzayda kapak açılırken, kol çekilirken yüksek yankılı metal gürültüleri çalıyor; roket ateşlendiğinde ise ses kesiliyor; C10'da belirsiz vokal nefes/gülme sesi duyuluyor.
   - **Müdahale:**
     - Dış çekimlerde yankılı metal sesleri silinecek. Mekanik sesler yalnızca takım içi radyo ve gemi gövde iletimi hissiyle (boğuk ve alçak) verilecek.
     - C10'daki yabancı vokal ses temizlenecek.
     - C20 ve C21'de roket motoru ateşlendiğinde güçlü derin itki sesi devreye girecek.

---

### B. CİDDİ REVİZYONLAR (Görsel ve Fizik Devamlılığı)

1. **Modül ve Kapak Geometrisi:**
   - C02'de kabinin üst ana halkası sağlam görünmemeli, C04'teki gibi baştan hasarlı görünmelidir.
   - C12'de üstten menteşeyle açılan kapak, C13'te sağdan menteşeli dolap kapağına dönüşmemelidir. `7.SERVIS`, `8.MANDAL` ve `9.CEKMEKOLU` referans sırası korunacaktır.
   - C24'te modülün sağında aniden beliren devasa açık kapak kaldırılacaktır.

2. **Sıfır Yerçekimi (0 g) Eforu ve Duruşu:**
   - C07, C08 ve C16'da astronot 1 g'de ağır adımlarla yürüyor gibi görünmemeli; hava kilidi tutamaklarına tutunarak süzülmelidir.
   - C11'de kapağı iki elle kaldırırken yerde diz çöküyor gibi durmamalı; bir eli platform korkuluğunda sabit, diğer eli kapağı açar durumda olmalıdır (etki-tepki kuralı).
   - C12'de mandalı tutan el 9 saniye donuk kalmamalı; çeyrek tur çevirme hareketi ilk 3-5 saniyede tamamlanmalıdır.

3. **Vakum Roket İtkisi (C20 / C24):**
   - KITE'ın altındaki iki ventral iticinin alevi dumanlı atmosferik meşale gibi değil; vakumda yanan temiz, parlak ve odaklanmış itki çizgisi (mavi-beyaz çekirdek) olarak üretilmelidir. Duman bulutları elenecektir.

4. **180 Derece Aks Atlamaları:**
   - C05→C06 ve C11→C12 geçişlerinde kamera aks çizgisini atlayarak yönleri tersine çevirmiştir. Kurguda KITE daima solda, kabin daima sağda kalacak kamera açıları korunmalıdır.

---

## 4. ÇEKİM BAZINDA DÜZELTME REÇETESİ (C01–C24)

| Çekim | Montaj Zamanı | Tespit Edilen Kusur | Müdahale Yolu | Hatanın Doğduğu Yer |
|:--:|:--:|---|---|:--:|
| **C01** | 00:00–00:07 | Ekranlarda anlamsız yazılar (T3); diyalog yok | Kurguda Dane'in açılış VO repliği (R01) eklenecek; ekranlar boş/karanlık tutulacak | kurgu / ses |
| **C02** | 00:07–00:11 | 48 yolcu bilgisi verilmiyor; arka plandaki modül formu C03'e uymuyor | Sana repliği (R02) + "48 ON BOARD" grafik bindirmesi eklenecek; arka plan kabini 4.KABIN'e eşitlenecek | anlatım / kare |
| **C03** | 00:11–00:21 | Kokpitten bakışta modül yatay halkalı istasyona dönüşüyor; erkek astronotta yeni arma çıkıyor | 1.DANE ve 4.KABIN referanslarıyla başlangıç karesi yenilenecek; dikey kabin formu korunacak | kare |
| **C04** | 00:21–00:31 | Cam koyu maviye dönüyor; tempo düşüyor | Cam şeffaf tutulacak; klip süresi dinamik kesilecek | kare / kurgu |
| **C05** | 00:31–00:35 | Halka metal yerine kırık beton gibi görünüyor; 180° aks atlaması | 6.HALKA metalik dokusuyla kare üretilecek; KITE solda, kabin sağda kalacak | kare / kurgu |
| **C06** | 00:35–00:45 | Kadın astronotun tulumunda yabancı yeşil arma/valf; diyalog yok | 2.SANA referansıyla temiz tulum; R06 repliği kurguda eklenecek | kare / ses |
| **C07** | 00:45–00:47 | Koyu mavi şerit ve göğüste yabancı kutu; 1 g dik duruş | 2.SANA turkuaz şeritleri korunacak; eşikte tutunarak süzülme pozu verilecek | kare / hareket |
| **C08** | 00:47–00:50 | Yüz başka kadına dönüyor; kolda ABD bayrağı; 1 g yürüme | 2.SANA portresiyle kare yenilenecek; bayrak/yazı silinecek; 0 g süzülüş | kare / hareket |
| **C09** | 00:50–01:00 | Gemi beyaza dönüyor; emniyet bağı sert tel gibi; tutamakta kayma | 3.KITE grafit gövdesi; kablo gevşek salınacak; tutunma teması kesmeyle C10'a bağlanacak | kare / hareket / seçim |
| **C10** | 01:00–01:10 | Botlar 1 g gibi basıyor; arkada vokal nefes sesi duyuluyor | Manyetik kilit mandalları karede gösterilecek; vokal ses miksten temizlenecek; R10 eklenecek | kare / ses |
| **C11** | 01:10–01:20 | Basamak yerine platform; vakumda yüksek metal sesi; diz çökme tepkisizliği | Bir el korkulukta tutunacak; vakum sesleri kısılacak; R11 eklenecek | kare / hareket / ses |
| **C12** | 01:20–01:30 | Kol 9 sn oynamıyor; ses bandında hayali kilit çalıyor; aks atlaması | Çeyrek tur çevirme hareketi üretilecek; ses senkronu oturtulacak; R12 eklenecek | hareket / kurgu / ses |
| **C13** | 01:30–01:40 | Kapak dolap kapağına dönüyor; astronot yüzü/kolu maviye dönüyor; vakum sesi | 8.MANDAL ve 2.SANA referansı zorunlu; vakum gürültüsü temizlenecek; R13 eklenecek | kare / ses |
| **C14** | 01:40–01:50 | Astronot çıkıntı yerine modülün iç odasında duruyor | 2.SANA dış çıkıntı korkuluğunda duracak; 9.CEKMEKOLU 90° açılacak; R14 eklenecek | kare / hareket |
| **C15** | 01:50–01:57 | Kıskaç kolun içinden geçiyor (clipping); vakum kilit sesi | Temas ve oturma C15'te bitecek; çene C16/C17'de kapanacak; R15 eklenecek | hareket / seçim / ses |
| **C16** | 01:57–02:02 | Hava kilidi kasa kapısına dönüyor; astronot yüzü değişiyor; 1 g yürüme | 3.KITE hava kilidi ve 2.SANA referansı; 0 g içeri giriş; R16 eklenecek | kare / hareket |
| **C17** | 02:02–02:05 | Kokpitte astronotların şeritleri maviye dönüyor; yüzler değişiyor | 1.DANE ve 2.SANA referanslarıyla kokpit ikili planı yenilenecek; R17 eklenecek | kare |
| **C18** | 02:05–02:07 | Kontrol kolu sağ elden sol ele dönüşüyor (ters el) | 5.KOKPIT referansıyla yakın plan SAĞ EL olarak yeniden üretilecek | kare / kurgu |
| **C19** | 02:07–02:09 | Ateşleme anında kokpitte sarsıntı/ivme tepkisi yok | Astronotların bedenlerinde hafif geriye gömülme ve koltuk sarsıntısı üretilecek; R19 eklenecek | hareket / ses |
| **C20** | 02:09–02:19 | Roket alevi dumanlı kamp ateşi gibi; modülde tork tepkisi yok; roket sesi yok | Temiz mavi-beyaz vakum itki alevi; güçlü derin roket sesi eklenecek; R20 eklenecek | hareket / ses |
| **C21** | 02:19–02:23 | Erkek astronotta ikinci turuncu şerit beliriyor; ekran yazıları | 1.DANE tek turuncu bant; ekranlar boş/loş tutulacak; R21 eklenecek | kare |
| **C22** | 02:23–02:25 | Ekran yazıları; Dünya uzaklaşması | Dünya'nın uzaklaşması stabil ve temiz gösterilecek; R22 eklenecek | hareket |
| **C23** | 02:25–02:26 | Rahatlama anında diyalog eksikliği | Sana'nın 48 stabil teyidi (R23) ses bandına eklenecek; profesyonel rahatlama | ses |
| **C24** | 02:26–02:36 | Modülde dev kapak beliriyor; itici alevinde duman bulutları | 10.DUZEN ve 4.KABIN referansıyla temiz final karesi; duman yok; Dane kapanış VO (R24) | kare / hareket / ses |

---

## 5. SONUÇ VE SONRAKİ ADIMLAR

Montajlanan taslak video hikâyenin omurgasını kanıtlamıştır. Ancak izleyicinin filmi gerçek bir uzay draması olarak algılaması için:

1. **Önce Seslendirme:** `FILM.md` §5'teki 24 replik seslendirilip montaj kanalına oturtulmalıdır (özellikle C01 Dane açılış kancası ve C02 Sana teyidi).
2. **Karakter Yenilemesi:** Yüzleri, logoları ve şerit renkleri bozuk olan çekimler (`C03, C06, C07, C08, C13, C16, C17, C18`) onaylı referans sayfalarından (`1.DANE_v1.png` ve `2.SANA_v1.png`) türetilecek doğru başlangıç kareleriyle yeniden üretilmelidir.
3. **Fizik ve Ses Temizliği:** Uzay boşluğundaki gereksiz metal gürültüleri kaldırılmalı, roket motoru sesi eklenmeli ve alevler duman bulutlarından arındırılmalıdır.

Bu düzeltmeler yapıldığında film hem YouTube izleyici tutma metriklerini tam karşılayacak hem de görsel sürekliliği kusursuz bir seviyeye gelecektir.
