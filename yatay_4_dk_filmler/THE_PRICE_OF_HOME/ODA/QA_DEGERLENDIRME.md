# 📊 THE_PRICE_OF_HOME — QA Değerlendirme ve İyileştirme Raporu (`taslak_01`)

> **Kayıt Tarihi:** 16.10.2026  
> **Kapsam:** 4 dakikalık film (24 çekim × 10 s), `taslak_01`  
> **İncelenen Raporlar:** `ODA/HAM_QA_RAPORU.md` içindeki 4 rapor:
> 1. Anlatım Testi (izleyici anlatı testi)
> 2. İzleme Formu (Gemini A + B simülasyonu)
> 3. Süreklilik (kesme bazlı 23 kesme taraması)
> 4. Tarama (T1-T14 bulguları)
>
> **Dayanak:** `uretim_hatti/QA_OKUMA_KILAVUZU.md` · `AGENTS.md` §1, §3, §4, §5.  
> **Kural (AGENTS.md §1 ④):** Çıkarılan dersler bu filmin `NOTLAR.md` ve `ODA/` belgelerine not olur, genel kurala dönüştürülmez. İki ayrı filmde tekrarlayan vakalar sahibe sorulur.

---

## 1. RAPOR GEÇERLİLİĞİ VE KAYNAK GÜVENİLİRLİĞİ (QA_OKUMA §4)

| Rapor | Kaynak / Yöntem | Geçerlilik Durumu | Not / Bayrak |
|---|---|:--:|---|
| **Anlatım Testi** | Bağımsız göz simülasyonu (ekranda görülen ve duyulan) | **GEÇERLİ** | Planı bilmeyen sıradan izleyici gözüyle doldurulmuş. 24 çekimlik akışın ne kadarının anlaşıldığını net gösteriyor. |
| **İzleme Formu (A/B)** | Gemini AI simülasyonu | **KISITLI (Yapay İzleyici)** | A ve B formları insan izleyici tarafından değil, Gemini tarafından "simülasyon" olarak üretilmiştir. **AGENTS.md Madde ⑤ uyarınca:** Gerçek izleme formu sahip + en az 2 dış insan izleyici olmadan tamamlanmış sayılmaz. Teknik maddeleri yol göstericidir. |
| **Tarama** | Gemini 1 fps video taraması | **ŞARTLI GEÇERLİ** (`ne olmalı` bayrağı) | Şablondaki `WHAT SHOULD BE IN THIS VIDEO` kısmı placeholder (`<e.g. ...>`) bırakıldığı için model fiziksel tutarlılık ve iç devamlılığı genel taramıştır. Güvenilirlik yüksek ancak senaryo beklentisi süzülmemiştir. |
| **Süreklilik** | Gemini kesme taraması | **ŞARTLI GEÇERLİ** (`kesme` bayrağı) | `CUT LIST` tablosu placeholder bırakıldığı için Gemini 10'ar saniyelik 23 kesmeyi kendisi varsayarak incelemiştir. Zaman kodları tutarlıdır. |
| **Zaman-Çekim Eşleşmesi** | `timeline.json` boş | **İÇERİK ÇAPASI** | Kurgu repoda kayıtlı olmadığından (`timeline.json` parçaları boş), zaman kodları ($C_n \approx \lfloor t/10 \rfloor + 1$) çekim içi görsel içerik kontrol edilerek doğrulanmıştır. |

---

## 2. BİRLEŞTİRİLMİŞ BULGULAR VE PROMPT KARŞILAŞTIRMASI

> **Sınıflandırma:**  
> 🅐 **Hareket / Model Hatası:** Promptta istenen doğruydu, model görselde/videoda yanlış üretti.  
> 🅑 **Prompt / Eksik Tarif:** Promptta gerekli kısıt veya tarif yazılmadığı için model boşluğu doldurdu.  
> 🅑+ **Promptta Davet:** Prompttaki bir niyet/eylem/fiil ifadesi hatayı doğrudan kışkırttı.  
> 🅒 **Tasarım / Kurgu Kararı:** Model ya da prompt hatası değil, hikâye/sahneleme kurgusunun doğal sonucu.  
> 🅓 **Yanlış Alarm / Okuma Hatası:** Raporda hata denilen şey aslında senaryo gereği veya rapordaki bir yanılgı.

---

### F1. Planlanan Repliklerin Yokluğu ve Modelin Kendi Kendine Konuşması
- **İlgili Çekimler:** C01, C08, C10, C13, C14, C22, C24 (tüm film genelinde)
- **Rapor Kaynağı:** Anlatım §7, İzleme A4/A5, Tarama #11, #13
- **Sınıf:** 🅑+ (Promptta model sesi KAPALI denmesine rağmen videoya konuşma daveti yapılması) + 🅒 (Kurgu/Ses hazırlığı yapılmadan taslağın izlenmesi)
- **Hatanın Doğduğu Yer:** **KURGU / SES**
- **Tespit:**
  - Anlatım testinde duyulan 7 replik de senaryodaki R01–R27 replikleri değildir! Modelin kendi ürettiği bozuk fısıltı ve mırıltılardır (*"Mara, we are running out of time"* 01:31, *"I'm trying to find a way"* ×2 01:34, *"There has to be another option"* 01:37, bozuk mırıltı 02:04, *"Let me take your place"* 02:10, *"Who are you?"* 03:36, *"Ahhh"* 03:46).
  - Planlanan açılış kancası (R01 Mara: *"Who are you?"*, R02 Eli iç ses: *"An alien brought us home..."*) ve aradaki diyaloglar hiç duyulmadığı için izleyici ilk 100 saniye konuyu anlayamamış, kancayı kaçırmış ve 01:40'ta filmi bırakmak istemiştir (Anlatım A2).
- **Prompt Karşılaştırması:**
  - `FILM.md` §5'te replikler "kurguda eklenir" denmiş ve `PROMPTLAR/G01.md` başlığında "Model sesi KAPALI kuralı geçerlidir" yazılmıştır.
  - Ancak video promptlarında modelin ses motorunu kapatacak net bir yönerge bulunmadığı gibi, kurgu aşamasında ham video sesleri kısılmamış ve kaydedilmiş replikler filme eklenmemiştir.

---

### F2. Prompttaki Niyet ve Duygu İfadelerinin Konuşmayı Kışkırtması
- **İlgili Çekimler:** C08, C10, C13, C15, C22, C23
- **Rapor Kaynağı:** İzleme A4, Tarama #11, #13
- **Sınıf:** 🅑+ (Promptta Davet)
- **Hatanın Doğduğu Yer:** **PROMPT**
- **Tespit ve Prompt Alıntıları:**
  - **C10 (01:30–01:40):** Promptta *"as he searches for another option"* denmiş → Model Eli'ye *"There has to be another option"* dedirtmiş ve ağzını oynatmadan ses çıkarmıştır (Tarama #11, İzleme A4).
  - **C13 (02:00–02:10):** Promptta *"as he offers himself in her place"* denmiş → Model Eli'ye *"Let me take your place"* dedirtmiştir!
  - **C08 (01:10–01:20):** Promptta *"her lips slightly parted in quiet contemplation"* denmiş → Dudak açık olunca model diyalog üretmiştir.
  - **C22 (03:30–03:40):** Promptta *"looks upon a total stranger"* denmiş → Mara fısıltıyla *"Who are you?"* mırıldanmıştır.
  - **"Ağız kapalı" koruması:** 15 yüz çekiminin sadece birinde (C12 Vey: *"his small mouth closed"*) ağız kapalı kuralı yazılmıştır. Kalan 14 çekimde model konuşma üretmeye açık bırakılmıştır.

---

### F3. Vey'in İnsan Gibi İç Çekmesi
- **İlgili Çekim:** C23 (03:40–03:50)
- **Rapor Kaynağı:** Anlatım #10, İzleme A6 (03:46), Tarama #27
- **Sınıf:** 🅑+ (Promptta Davet)
- **Hatanın Doğduğu Yer:** **PROMPT / KURGU**
- **Tespit ve Prompt Alıntısı:**
  - C23 Video promptu: *"taking a deep, quiet breath as the emotional essence of the collected memories resonates within him"*.
  - Bu tarif üzerine model, uzaylıya sıradan bir erkek insan sesiyle yüksek sesli *"Ahhh"* iç çekişi yaptırmıştır (Anlatım A4 SOUND OFF, İzleme A6).
  - Kurguda klip sesi sessize alınmadığı için bu ses nihai taslağa sızmıştır.

---

### F4. Uzay Boşluğunda Rüzgâr, Motor ve Metalik Kenetlenme Sesleri
- **İlgili Çekimler:** C02 (00:18), C03 (00:20–29), C05 (00:40–49), C18 (02:50–59), C20 (03:10–19), C21 (03:20–29)
- **Rapor Kaynağı:** Tarama #1, #3, #5, #18, #21, #24; İzleme A6
- **Sınıf:** 🅑 (Eksik Kısıt / Model Varsayımı)
- **Hatanın Doğduğu Yer:** **KURGU** (ve kısmen PROMPT)
- **Tespit:**
  - Dış uzay çekimlerinde şiddetli uğultu, rüzgâr (whoosh), mekanik kilitlenme ve roket gürültüleri duyulmaktadır.
  - `BILINEN_TUZAKLAR.md` §B3 kuralına göre uzay vakumunda atmosferik dış ses olmaz.
  - Video promptlarının başına "Mute exterior vacuum" veya "Silent space" yazılmadığı gibi, kurgu timeline'ında bu kliplerin ses izleri kapatılmamıştır.

---

### F5. Uzay Vakumunda Asılı Kalan İtici Dumanı/Buhar
- **İlgili Çekim:** C03 (00:20–00:29)
- **Rapor Kaynağı:** Tarama #2
- **Sınıf:** 🅑 (Model Fizik Zaafı / Prompt İfadesi)
- **Hatanın Doğduğu Yer:** **PROMPT / MODEL**
- **Tespit:** C03 promptundaki *"slows its forward momentum"* eylemi için model geminin altından duman/gaz çıkarmış ve gaz vakumda dağılmak yerine atmosferdeymiş gibi asılı kalmıştır (`BILINEN_TUZAKLAR.md` §B4 tuzağı).

---

### F6. Rozet, Arma ve Kıyafet Kaymaları (Devamlılık Kopmaları)
- **İlgili Çekimler:** C01, C03, C05, C08, C13, C14, C17, C22, C24
- **Rapor Kaynağı:** Tarama #4, #6, #10, #14, #15, #16, #17, #26, #28; Süreklilik Kesme 3, 5, 13, 14, 16, 23; İzleme A2
- **Sınıf:** 🅑 (Promptta Eksik Tanım)
- **Hatanın Doğduğu Yer:** **REFERANS / BAŞLANGIÇ KARESİ / PROMPT**
- **Tespit ve Karşılaştırma:**
  - **Eli'nin yuvarlak gümüş rozeti:** Yalnızca `ref/1.ELI_v1.png` referans promptunda vardır. 24 çekim promptunun hiçbirinde Eli'nin göğüs arması tarif edilmemiştir! Sonuç: Model bazen yuvarlak arma, bazen üçgen arma, bazen boş beyaz tulum üretmiştir.
  - **Mara'nın turkuaz üçgen rozeti:** Yalnızca C08 promptunda yazılmıştır. C01, C14, C19, C22, C24 çekimlerinde göğüs rozeti tarif edilmemiştir. C22'de ikisi de aynı üçgen armayı takmıştır (Tarama #26).
  - **C24'te Amerikan Bayrağı ve Dijital Ekran:** C24 Görsel ve Video promptlarında astronotların kıyafetleri hakkında HİÇBİR detay cümle yazılmamıştır (*"Same fixed seats, closed helmets and harnesses"* denip geçilmiştir). Model boşluk bulunca Mara'nın sol koluna Amerikan bayrağı ve mavi dijital ekran yerleştirmiştir (Tarama #28, Süreklilik Kesme 23, İzleme A2)!
  - **C17 El ve Bileklik:** Promptta *"Mara's pearl-white gloved hand with muted-gold cuff"* yazılmıştır. Model "cuff" (manşet) kelimesini saat/bileklik/kadran olarak yorumlamış (Tarama #17, Süreklilik Kesme 16) ve sağ el yerine sol el çizmiştir.

---

### F7. C08'de Kasksız Erkek Astronot ve Kask Dışından Çıkan Buhar
- **İlgili Çekim:** C08 (01:10–01:20)
- **Rapor Kaynağı:** Anlatım A1#4, İzleme A2/A3, Tarama #8, Süreklilik Kesme 8
- **Sınıf:** 🅑+ (Promptta Davet) + 🅐 (Model Üretim Hatası)
- **Hatanın Doğduğu Yer:** **PROMPT / BAŞLANGIÇ KARESİ**
- **Tespit ve Prompt Alıntıları:**
  - C08 promptunda: `EKLE ref/2.MARA_v1.png ref/5.ODA_v1.png` (Eli referansı yüklenmemiş!).
  - Video promptu: *"4-7 s: She slowly turns her head to the left toward Eli standing off-camera... 7-10 s: ...her breath fogging faintly against the lower edge of the clear visor before clearing cleanly."*
  - **Sonuç 1:** Model "toward Eli standing off-camera" ifadesini görünce kadrajın sol ön planına referanssız, kasksız, sivil yakalı çıplak kafalı bir erkek sokmuştur!
  - **Sonuç 2:** Model kask içindeki buğulanmayı ("breath fogging faintly") kaskın DIŞINDAN çıkan duman olarak üretmiştir (İzleme A3: *"kaskın DIŞINDAN buhar çıkıyor"*).

---

### F8. Kokpit İki-Plan Geometrisi ve Yön Tutarsızlığı
- **İlgili Çekimler:** C01 (00:00), C04 (00:30), C19 (03:00), C22 (03:30), C24 (03:50)
- **Rapor Kaynağı:** Anlatım A1#1, A1#2, A1#8; İzleme A3; Süreklilik Kesme 1, 16, 18
- **Sınıf:** 🅑+ (Geometrik Olarak İmkânsız Kompozisyon Talebi)
- **Hatanın Doğduğu Yer:** **SAHNELEME / PROMPT**
- **Tespit:**
  - Promptlarda aynı anda: (1) Kokpit içinde Eli solda, Mara sağda iki astronotun yüz ifadeleri, (2) Arkadaki kanopi camından ileriye doğru bakış ve dış uzaydaki Dünya/portalın görünmesi istenmiştir.
  - Eğer kamera astronotların yüzüne bakıyorsa, arka planda kokpitin ARKA DUVARI olmalıdır. Ön cam görünüyorsa koltukların sırtı ön cama dönük demektir! İzleme Formu A3'te tam olarak bu saçmalık belirtilmiştir: *"koltukları ön cama sırtı dönük şekilde konumlanmış"*.
  - Bu hata `THE_FURNACE_GATE` K19 bulgusuyla birebir aynı geometri tuzağıdır!

---

### F9. Portal Halka Etrafındaki Dünya ve İkinci Gezegenler
- **İlgili Çekimler:** C18, C19, C20, C21
- **Rapor Kaynağı:** Anlatım A1#8, İzleme A3 (03:00, 03:10), Tarama #19, #22, #25; Süreklilik Kesme 16, 17, 18
- **Sınıf:** 🅑 (Eksik Kısıt / Model Varsayımı)
- **Hatanın Doğduğu Yer:** **PROMPT / BAŞLANGIÇ KARESİ**
- **Tespit:**
  - C18 Görsel promptunda *"no Earth yet visible outside the ring"* yazılmışken, C19, C20 ve C21 promptlarında bu kısıt yinelenmemiştir.
  - Model C19'da kokpitten bakarken hem halkanın içinde Dünya'yı göstermiş, hem de halkanın DIŞINDA dev bir Dünya çizmiştir (aynı karede iki Dünya!).
  - C20 ve C21'de ise uzay boşluğuna birdenbire Satürn benzeri halkalı gezegenler ve uydular yerleştirmiştir (Tarama #25).

---

### F10. Dış Çekimlerde İstasyona Yanaşma ve Uçuş Yönü Taklaları
- **İlgili Çekimler:** C02, C03, C11, C18, C20
- **Rapor Kaynağı:** Anlatım A1#2, İzleme A3 (00:10), Süreklilik Kesme 1, 2, 10, 15, 17; Tarama #12
- **Sınıf:** 🅑 (Yön Tarifi Eksikliği)
- **Hatanın Doğduğu Yer:** **SAHNELEME / REFERANS**
- **Tespit:**
  - `ref/3.GEMI_v1.png` referansında geminin burnu sola dönük çizilmiştir.
  - C02'de gemi sağdaki istasyona doğru geri geri kayarak yaklaşmaktadır. C03'te burun aniden sağa dönmektedir. C11 ve C18'de istasyon halkası bir sağda, bir solda görünmektedir.
  - `SAHNELEME.md` haritasında mekânın doğrusal ekseni çizilmiş ancak sol/sağ ekran yönü kilitlenmemiştir.

---

### F11. Gemi Tasarımının Çekimden Çekime Değişmesi
- **İlgili Çekimler:** C02, C03, C20, C21
- **Rapor Kaynağı:** Süreklilik Kesme 2; Tarama #20, #23; İzleme A3 (03:10)
- **Sınıf:** 🅑 (Referans Kapsamı Yetersizliği)
- **Hatanın Doğduğu Yer:** **REFERANS SAYFASI**
- **Tespit:**
  - `ref/3.GEMI_v1.png` referans sayfasında sadece 2 panel vardır: Sol panel 3/4 ön görünüş, sağ panel kokpit içi. Geminin yandan, arkadan ve üstten görünüşü YOKTUR!
  - C21'de prompt *"wide rear three-quarter view of the compact spacecraft"* istediğinde model arkadan referans bulamadığı için kafasına göre çift motorlu uzun bir kruvazör uydurmuştur (Tarama #23).
  - C20'de istasyondan ayrılırken gemi küt burunlu kanatsız bir kapsüle dönüşmüştür (Tarama #20).

---

### F12. Kaide ve Hafıza Prizmasının (Memory Prism) Durum Değişimleri
- **İlgili Çekimler:** C06, C07, C08, C09, C10, C13, C14, C17, C23
- **Rapor Kaynağı:** Tarama #7; Süreklilik Kesme 6, 7, 9, 12, 13
- **Sınıf:** 🅑 (Prompt Durum Eksikliği) + 🅐 (Model Hatası)
- **Hatanın Doğduğu Yer:** **PROMPT / BAŞLANGIÇ KARESİ**
- **Tespit:**
  - C06'da prizmanın sönük olması gerekirken parlak kehribar yanmıştır (🅐).
  - C07'de kaide üzerinde el izi paneli ve prizma varken, C08 ve C10'da kaidenin üstü düz metal bir kapakla örtülü görünmektedir (Süreklilik Kesme 7, 9).
  - Çekim promptlarında kaidenin üzerindeki prizmanın o an açıkta mı yoksa kapalı mı olduğu her çekimde yazılmamıştır.

---

### F13. C09 Eldiven Yakın Çekiminde Deforme Parmak
- **İlgili Çekim:** C09 (01:20–01:30)
- **Rapor Kaynağı:** Tarama #9 (T1, LIKELY)
- **Sınıf:** 🅐 (Model Anatomi Hatası)
- **Hatanın Doğduğu Yer:** **BAŞLANGIÇ KARESİ / HAREKET**
- **Tespit:** Yüzük ve fotoğrafı tutan eldivenin iç kısmında ikinci bir küçük başparmak/çıkıntı üremiştir. Nesne tutma planlarında başlangıç karesi denetimi yapılmadan üretime geçilmemelidir.

---

### F14. C23'te Vey'in Tasarım ve Ten Rengi Kayması
- **İlgili Çekim:** C23 (03:40–03:50)
- **Rapor Kaynağı:** İzleme A2, Süreklilik Kesme 20, Tarama #27
- **Sınıf:** 🅑 (Promptta Eksik Tanım)
- **Hatanın Doğduğu Yer:** **PROMPT**
- **Tespit:** C23 Görsel promptunda Vey'in koyu mor (dark-violet) ten rengi yazılmamış, sadece *"bony crests, large recessed amber eyes and aged-bronze high collar intact"* denmiştir. Model teni gri-kahverengiye çevirmiş ve kafatasını genişletmiştir.

---

### F15. Hikâye Temposu ve Durağanlık
- **İlgili Çekimler:** C06–C07 (00:50–01:15), C11–C12 (01:40–02:00)
- **Rapor Kaynağı:** Anlatım A2 (01:40), İzleme A7
- **Sınıf:** 🅒 (Repliklerin Kurguda Olmayışının Doğal Sonucu)
- **Hatanın Doğduğu Yer:** **KURGU / SES**
- **Tespit:** İzleyici 00:50–01:15 ve 01:40–02:00 arasında hiçbir şey olmadan bakışıldığını ve krizin ne olduğunun anlaşılmadığını belirterek izlemeyi bırakmak istemiştir. Taslakta planlanan R07–R12 replikleri ses olarak yer almadığı için sahne dramatik gerilim yerine boş bakışma olarak algılanmıştır.

---

### F16. Final Anlatımının Çarpılması (Bedelin Anlaşılmaması)
- **İlgili Çekimler:** C22, C23, C24
- **Rapor Kaynağı:** Anlatım §6, #11; İzleme A1, A8
- **Sınıf:** 🅒 (Ses ve Kurgu Eksikliği)
- **Hatanın Doğduğu Yer:** **ANLATIM / SES**
- **Tespit:**
  - İzleyici C22'de Mara'nın fısıltısını duyamadığı için kadının hafızasını kaybettiğini tam anlayamamıştır.
  - C24'te (03:50) iki astronotun arkalarında Dünya ile birbirine gülümsemesi, izleyicide *"İkisi de hiçbir bedel ödemeden kurtuldu ve mutlu mesut eve döndü"* izlenimi yaratmış, katarsis ve dramatik fedakârlık çökmüştür.
  - C22 ve C24'teki R24–R27 replikleri (Eli'nin iç sesi: *"She didn't know who I was. But she was home."*) filme konmadığı sürece bu final doğru anlaşılamaz.

---

### F17. 02:00–02:30 Arasında Çekim Sırası Uyuşmazlığı
- **İlgili Çekimler:** C13, C14, C15, C16
- **Rapor Kaynağı:** Anlatım §1 (02:04–02:40), İzleme A1, Tarama #14
- **Sınıf:** 🅒 / 🅓 (Kurgu Sırası veya Zaman Kayması)
- **Hatanın Doğduğu Yer:** **KURGU**
- **Tespit:** Anlatım testinde Mara'nın mırıltısı 02:04'te duyulurken, Eli'nin teklifi 02:10'da görünmektedir. Oysa çekim listesinde C13 (02:00–02:10) Eli'nin teklifi, C14 (02:10–02:20) Mara'nın duraksamasıdır. Taslak kurguda kliplerin sırası mı kaydı yoksa model repliği ters klipte mi üretti incelenmelidir.

---

## 3. ÇEKİM BAZINDA ANLATIM VE ANLAŞILIRLIK ÇETELESİ

| Çekim | Zaman | Planlanan Bilgi / Olay | İzleyicinin Anladığı | Durum |
|:--:|:--:|---|---|:--:|
| **C01** | 00:00–00:10 | Kanca: Eve dönmüşler ama kadın adamı tanımıyor | Kokpitte endişeli bakışma; arkada Dünya var | ⚠️ (Kanca repliksiz kaçtı, geçmişe dönüş anlaşılamadı) |
| **C02** | 00:10–00:20 | Geçmiş: Dev gezegen yanındaki istasyona yaklaşma | Jüpiter benzeri gezegen yanındaki istasyona yaklaşma | ✅ |
| **C03** | 00:20–00:30 | Yanaşma manevrası | İstasyon kapısına doğru süzülüş | ✅ |
| **C04** | 00:30–00:40 | Kokpit kenetlenme hazırlığı | Kokpitten istasyon halkasına bakış | ⚠️ (Pencere yönü kafa karıştırdı) |
| **C05** | 00:40–00:50 | Mekanik kenetlenme kilitlenir | Mekanik kilitlerle istasyona bağlanma | ✅ |
| **C06** | 00:50–01:00 | Vey ile karşılaşma, takas odası | Odada konsol başında uzaylıyla karşılaşma | ✅ |
| **C07** | 01:00–01:10 | Kaide aktifleşir, el izi paneli açılır | Konsol ve el izi tarayıcısı aktifleşir | ⚠️ (Ne olduğu açıklanmadığı için belirsiz) |
| **C08** | 01:10–01:20 | Mara bedeli anlar, Eli'ye bakar | Mara üzüntüyle Eli'ye bakar | ✅ (Görsel devamlılıkta kask hatası var) |
| **C09** | 01:20–01:30 | Sahil fotoğrafı: Kaybolacak anı | Sahildeki çift fotoğrafı ve alyans | ❌ (Vey'in "hissi istiyorum" talebi repliksiz anlaşılamadı) |
| **C10** | 01:30–01:40 | Eli başka seçenek arar, zaman daralıyor | Zaman daralıyor, başka seçenek olmalı | ✅ (Modelin uydurduğu replik planı tesadüfen tutturdu) |
| **C11** | 01:40–01:50 | İstasyon ışıkları sönüyor | Dış istasyon durağan planı | ❓ (Bahsedilmedi / durağanlık eleştirisi aldı) |
| **C12** | 01:50–02:00 | Vey şartın değişmeyeceğini onaylar | Uzaylının sessiz bekleyişi | ❓ (Bahsedilmedi) |
| **C13** | 02:00–02:10 | Eli kendi anılarını vermeyi teklif eder | Eli yerini almayı teklif eder | ✅ (Modelin uydurduğu replik sayesinde anlaşıldı) |
| **C14** | 02:10–02:20 | Mara kararını verir | Mara elini konsola uzatır | ✅ |
| **C15** | 02:20–02:30 | Mara ile Vey son kez bakar | — | ❓ (Bahsedilmedi) |
| **C16** | 02:30–02:40 | Eli çaresizce başını eğer | — | ❓ (Bahsedilmedi) |
| **C17** | 02:40–02:50 | Mara elini panele basar, anılar çekilir | Mara elini basarak mekanizmayı çalıştırır | ✅ |
| **C18** | 02:50–03:00 | Geçit açılır, Dünya görünür | Halkanın içinde Dünya geçidi açılır | ✅ |
| **C19** | 03:00–03:10 | Kokpite dönüş, geçide son bakış | Kokpitte arkada portal ve Dünya | ⚠️ (Ayrılış C20'de olmasına rağmen C19'da kokpitte) |
| **C20** | 03:10–03:20 | Geminin ayrılışı ve portala yöneliş | Gemi ayrılır ve portala doğru uçar | ✅ |
| **C21** | 03:20–03:30 | Geçidin içine dalış, beyaz ışık | Gemi geçidin içine dalar | ✅ |
| **C22** | 03:30–03:40 | Dünya yörüngesi: Mara Eli'yi tanımaz | Dünya yörüngesi, Mara'nın sözüyle erkeğin yıkılışı | ✅ (Söz boğuk duyuldu ama yıkılış anlaşıldı) |
| **C23** | 03:40–03:50 | Vey kristaldeki anıları içine çeker | Uzaylı ışık ağıyla dolan kristale bakıp iç çeker | ✅ |
| **C24** | 03:50–04:00 | Yeni başlangıç: Eli sabırla bakar | İkisi kokpitte birbirine gülümser | ⚠️ (Bedelin kalıcılığı konusunda kafa karıştırdı) |

**Özet:** 14 Çekim Tam Anlaşıldı (✅) · 5 Çekim Kısmen / Sorunlu (⚠️) · 1 Çekim Anlaşılamadı (❌) · 4 Çekim Belirsiz/Bahsedilmedi (❓).

---

## 4. ÇIKARILAN DERSLER (FİLM İÇİ DERSLER)

> `AGENTS.md` §1 ④ uyarınca bu maddeler genel repo kuralı değildir; bu filmin yapım günlüğüne yazılan teknik derslerdir.

### D1. Replik ve Ses Tasarımı Yapılmadan Taslak İzlemeye Çıkılamaz (Hata Doğuşu: Kurgu/Ses)
- Taslakta planlanan seslendirmeler (R01–R27), ortam yatakları (Y1–Y3) ve zaman sıçraması kartı (`"11 DAKİKA ÖNCE"`) olmadığı için film sessiz sinema gibi izlenmiş, kurgusal omurga (flashback yapısı ve hafıza bedeli) izleyiciye geçmemiştir.
- `REPLIK_VE_KLIP_SESI_KILAVUZU.md` §2 kapısı geçilmeden hiçbir taslak QA taramasına verilmemelidir.

### D2. "Model Sesi KAPALI" Demek Yetmez; Klip Sesleri Dışa Aktarımda Susturulmalıdır (Hata Doğuşu: Araç/Kurgu)
- Video motoru (Veo / Gemini video), video promptunda ne yazarsa yazsın varsayılan olarak ses üretir. Bu sesler kurgu yazılımında veya dışa aktarım komutunda (`ffmpeg -an` veya ses kanalını silme) manuel susturulmadığı sürece filmin içine uzayda rüzgâr sesi, anlamsız mırıltılar ve insan gibi iç çeken uzaylı sesleri sızar.

### D3. Prompttaki Niyet ve Eylem Fiilleri Konuşma Davetidir (Hata Doğuşu: Prompt)
- *"as he searches for another option"*, *"as he offers himself in her place"*, *"taking a deep, quiet breath"* gibi zihinsel/eylemsel ifadeler, yapay zekâ video modelini karakterin ağzından söz ve ses çıkarmaya teşvik eder.
- Yüzün göründüğü her çekim promptuna tavizsiz olarak **"mouth closed in complete silence, no speech"** ifadesi eklenmelidir.

### D4. İki Kişilik Kokpit İçi Kamera Geometri Tuzağı (Hata Doğuşu: Sahneleme)
- Yüzleri önden/çaprazdan çekerken arka planda kokpitin ön camındaki manzarayı göstermek fiziksel olarak imkânsızdır (koltukların sırtını cama çevirir).
- Çözüm: Kokpit içi çekimlerde açı kilitlenmeli; yüzler çekilirken arka planda kokpitin iç konsolu/duvarı olmalı, dış manzara ise ya omuz üstünden (POV) ya da yan profilden camı kesen açıyla verilmelidir.

### D5. Referans Sayfası Üretilecek Bütün Kamera Açılarını Kapsamalıdır (Hata Doğuşu: Referans)
- `3.GEMI` referansında sadece 3/4 ön görünüş olduğu için arkadan görünüş (C21) ve yandan ayrılış (C20) çekimlerinde gemi tamamen farklı araçlara dönüşmüştür. Araç referans sayfaları mutlaka ön, yan, arka ve 3/4 panellerini içermelidir.

### D6. Rozet ve Kıyafet Detayları Yalnızca Referans Sayfasına Bırakılamaz (Hata Doğuşu: Prompt)
- Model, referans görselindeki küçük armaları (Eli'nin gümüş yuvarlak arması, Mara'nın turkuaz üçgeni) çekim promptunda açıkça yazılmadığı zaman unutur ve kafasına göre rozet/bayrak/saat uydurur. Kostümün ayırt edici unsurları her video promptunda birebir tekrarlanmalıdır.

### D7. F5 Görsel Üretim Eleştiri Turunun Atlanmasının Maliyeti (Hata Doğuşu: Süreç)
- F5 prompt yazımında alt ajanlar (`devamlilik` ve `teknik-danisman`) çağrılmadığı için; kokpit yön tutarsızlığı, rozet eksiklikleri, C08'deki referanssız Eli daveti ve C17'deki el/manşet belirsizliği önceden yakalanamamış, doğrudan video üretimine yansımıştır.

---

## 5. EYLEM PLANI VE ÖNERİLEN DÜZELTMELER

### A. Kurgu ve Ses Müdahalesi (Yeniden Çekim Gerektirmeyen Adımlar)
1. **Ham Klip Seslerini Sustur:** Kurgudaki 24 video parçasının tüm gömülü sesleri tamamen kapatılacak (özellikle uzay vakumundaki sesler, uzaylının iç çekişi ve modelin bozuk mırıltıları yok edilecek).
2. **Replikleri ve İç Sesi Kaydet/Ekle:**
   - C01 (00:00): Mara *"Who are you?"* + Eli iç ses: *"An alien brought us home. His price was every memory she had of me."*
   - C02 başına: `"11 DAKİKA ÖNCE"` (11 MINUTES EARLIER) zaman kartı eklenerek flashback izleyiciye netleştirilecek.
   - C10, C13, C14 diyalogları net ve temiz seslendirme ile eklenecek.
   - C22 (03:36): Mara *"Who are you?"* repliği belirgin ve temiz duyulacak.
   - C24: Eli'nin kapanış iç sesi eklenerek fedakârlığın kalıcı olduğu ve yeni bir başlangıç yapıldığı vurgulanacak.
3. **Mekân Ses Yatakları (Y1–Y3):** Kokpit kabin uğultusu ve istasyon oda tonu kesintisiz döşenecek.

### B. Prompt Düzeltme Önerileri (Sahip Onayından Sonra Uygulanacak)
- **Tüm Yüz Çekimleri (C01, C04, C06, C08, C10, C12, C13, C14, C15, C16, C19, C22, C24):**
  - Promptlara `his/her mouth remains completely closed in silence, no speaking` cümlesi eklenecek.
  - Zihinsel/eylemsel davetler (`searches for option`, `offers in her place`, `breath fogging`) somut fiziksel bakış tariflerine çevrilecek.
- **C08 Promptu:**
  - `toward Eli standing off-camera` çıkarılacak (`turns her head toward frame-left in quiet contemplation`).
  - `breath fogging faintly` çıkarılacak (dış buhar hatasını önlemek için).
- **C17 Promptu:**
  - `muted-gold cuff` ifadesi saat/bileklik algılandığı için `plain pearl-white glove, no wrist display or watch` olarak düzeltilecek; el yönü açıkça `right gloved hand` olarak kilitlenecek.
- **C24 Promptu:**
  - Boş bırakılan kıyafet alanı yerine: `Both wear their original pressure suits, Eli with cobalt-blue arm bands and Mara with muted-gold arm bands, no flags, no wrist displays, no badges changed.`
- **C19, C20, C21 (Portal Çekimleri):**
  - `Blue Earth is visible strictly and only inside the luminous portal plane; outside the ring is dark empty space with stars, no secondary Earth, no extra ringed planets.`

---

## 6. SAHİBE SORULACAK TEKRARLAYAN VAKALAR (`AGENTS.md` §1 ④)

Aşağıdaki üç hata tipi hem `THE_FURNACE_GATE` hem de `THE_PRICE_OF_HOME` filmlerinde aynen tekrarlamıştır. Sahibin kararıyla genel arıza/tuzak listelerine alınıp alınmayacağı sorulacaktır:

1. **İki Kişilik Kokpit İçi Kamera Geometri Tuzağı:** Hem FURNACE K19'da hem PRICE C01/C04'te pilotların yüzü kameraya bakarken arkalarındaki camda önlerindeki uzay/istasyon istenmiş ve koltuklar cama ters dönmüştür. (`BILINEN_TUZAKLAR`'a girsin mi?)
2. **Modelin Başlangıç Karesi Olmadan veya Ses Açıkken Söz Uydurması:** Her iki filmde de model prompttaki niyet ifadelerinden replik uydurmuş ve dudak kıpırdatmadan bozuk fonetik sesler üretmiştir.
3. **Rozet ve Kıyafetlerin Çekim Promptlarında Unutulması:** Yalnızca referans paneline güvenilip video promptunda rozet/kol şeridi yazılmayınca modelin Amerikan bayrağı veya yanlış arma takması vakası.
