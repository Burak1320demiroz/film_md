# 📒 THE_SKY_CATCH — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da / Gemini'de üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|
| 15.10.2026 | `the sky catch.mp4` (taslak montaj) | ❌ | 02:41 süreli ilk montaj; 48 kişi ve düşüş bilgisi girişte yok, diyaloglar eksik, karakter ve modül sürekliliği kopuk, vakumda ses hataları mevcut. |

## DENEMELER

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|
| 15.10.2026 | C01–C24 | taslak_01 | Frames to Video / Montaj | p1 | ❌ Montaj QA taramasından 28 teknik, 24 süreklilik, 5 anlatım kusuru aldı. | |

```
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

## RED (üretim reddi)

| Tarih | Çekim | Mesajın BİREBİR metni | İlerleyip sonda mı düştü | Değişen şey | Sonuç |
|---|:--:|---|:--:|---|:--:|
| 15.10.2026 | C01–C24 | Karakter sürekliliği koptu (yüz, arma, şerit renkleri); vakum sesleri hatalı; 48 yolcu tehlikesi girişte anlatılamadı. | — | Revizyon paketi hazırlandı | ✍️ Yeniden üretim planlandı |

---

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

> Girdi: `the sky catch.mp4` (Video modu, tam montaj ~02:41) · 15.10.2026

| Tarih | Video / kare modu | Zaman | Çekim (`kurgu.py liste`) | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması | Sınıf | Doğduğu yer |
|---|---|---|:--:|---|---|:--:|:--:|:--:|:--:|
| 15.10.2026 | Video | 00:00.0–00:06.5 | C01 | T3 TEXT | C01: Kokpitin sağ alt kısmındaki kontrol ekranlarında okunaksız harfler, rakamlar ve grafik etiketleri yer alıyor. | SURE | ✅ | 🅑 | kare |
| 15.10.2026 | Video | 00:32.0–00:35.5 | C05 | T11 OTHER | C05: Modülün üst kısmındaki kopmuş bağlantı halkası, yırtılmış metal/kompozit yerine kırılmış beton veya taş enkazı dokusunda görünüyor. | LIKELY | ✅ | 🅑 | kare |
| 15.10.2026 | Video | 00:36.0–00:45.0 | C06 | T3 TEXT | C06: Kadın astronotun göğsündeki yuvarlak portun hemen üstünde yer alan dikdörtgen etikette ve sol ekran çerçevesinde küçük yazılar/semboller görülüyor. | SURE | ✅ | 🅐 | kare |
| 15.10.2026 | Video | 00:45.5–00:47.0 | C07 | T9 WRONG FLOATING | C07: Yörüngedeki sıfır yerçekimi ortamında kadın astronot hava kilidi kapısında normal Dünya yerçekimi (1 g) varmış gibi dik duruyor. | SURE | ✅ | 🅑 | hareket |
| 15.10.2026 | Video | 00:47.0–00:50.5 | C08 | T9 WRONG FLOATING | C08: Kadın astronot hava kilidi zemini üzerinde ağırlıksız ortamda süzülmek yerine normal yerçekimindeymiş gibi ağır adımlarla yürüyor. | SURE | ✅ | 🅑+ | hareket |
| 15.10.2026 | Video | 00:49.0–00:50.5 | C08 | T3 TEXT | C08: Astronotun göğsündeki mavi üçgen armanın içinde yazılar ve sol omzunda ABD bayrağı arması görülüyor. | SURE | ✅ | 🅐 | kare |
| 15.10.2026 | Video | 00:53.0–00:59.5 | C09 | T11 OTHER | C09: Astronotun arkasındaki emniyet halatı (tether), sıfır yerçekiminde gevşek salınmak yerine ortasında sabit bir düğüm/halka varmış gibi sert tel gibi şeklini koruyarak ilerliyor. | LIKELY | ✅ | 🅐 | hareket |
| 15.10.2026 | Video | 00:55.5–01:00.0 | C09 | T13 SLIDING / EMPTY GRIP | C09: Astronot karşı modülün tutamağına uzandığında eldivenli parmakları demiri tam kavramadan/kilitlemeden tutamağın üzerinde kayıyor ve vücudu çarpma/tutunma ivmesi göstermiyor. | LIKELY | ✅ | 🅐 | seçim / kurgu |
| 15.10.2026 | Video | 01:01.0–01:10.0 | C10 | T9 WRONG FLOATING | C10: Astronotun botları dış platformun üzerinde herhangi bir manyetik kilit veya kanca olmadan, 1 g yerçekimi altındaymış gibi ağırlığını vererek basıyor. | SURE | ✅ | 🅑 | kare / hareket |
| 15.10.2026 | Video | 01:01.0–01:02.0 | C10 | T8 WRONG SOUND | C10: Dış uzay çekiminde müziğin arkasında görüntüyle ilgisi olmayan kısa bir nefes/gülme benzeri insan sesi duyuluyor. | LIKELY | ✅ | 🅑 | kurgu |
| 15.10.2026 | Video | 01:11.0–01:20.0 | C11 | T12 WEIGHTLESS EFFORT | C11: Sıfır yerçekiminde astronot tek eliyle gövdeye tutunmadan iki eliyle ağır bakım kapağını kaldırıyor; tepki kuvvetiyle geriye savrulması gerekirken yerde diz çökmüş gibi sabit kalıyor. | SURE | ✅ | 🅑+ | hareket / prompt |
| 15.10.2026 | Video | 01:17.0–01:19.5 | C11 | T8 WRONG SOUND | C11: Sert vakum (uzay boşluğu) çekimi olmasına rağmen bakım kapağı açılırken yüksek sesli ve yankılı metal çarpma sesleri duyuluyor. | SURE | ✅ | 🅑 | kurgu |
| 15.10.2026 | Video | 01:21.0–01:30.0 | C12 | T12 WEIGHTLESS EFFORT | C12: Eldivenli sağ el mekanik kolu 9 saniye boyunca tutuyor ancak kol hiç hareket etmiyor, eldivende sıkma/çekme eforu görünmüyor. | SURE | ✅ | 🅐 | hareket |
| 15.10.2026 | Video | 01:27.0–01:29.5 | C12 | T8 WRONG SOUND | C12: Hem vakum ortamında dış mekanik gürültü duyuluyor hem de görüntüde kol hiç kıpırdamadığı halde ses bandında kolun çekilip kilitlendiğine dair gürültülü bir efekt çalıyor. | SURE | ✅ | 🅑 | kurgu |
| 15.10.2026 | Video | 01:31.0–01:40.0 | C13 | T9 WRONG FLOATING | C13: Astronot dış çıkıntının üzerinde 1 g yerçekimindeymiş gibi dik duruyor ve sol elini açık kapağa sadece hafifçe dayıyor. | SURE | ✅ | 🅑 | kare / hareket |
| 15.10.2026 | Video | 01:31.0–01:39.5 | C13 | T8 WRONG SOUND | C13: Kenetlenme kolu dışarı doğru açılırken uzay boşluğunda yüksek sesli mekanik/hidrolik gürültüler ve metal vuruş sesleri duyuluyor. | SURE | ✅ | 🅑 | kurgu |
| 15.10.2026 | Video | 01:51.0–01:57.0 | C15 | T2 BODY-GROUND CLIPPING | C15: Kurtarma gemisinin kıskacı kapanırken (01:52–01:55) kıskacın alt ve üst çeneleri uzanan kolun ucunu fiziksel olarak sıkıştırmak yerine kısmen içinden geçiyor / boşluğu ısırıyor. | LIKELY | ✅ | 🅐 | hareket / seçim |
| 15.10.2026 | Video | 01:52.0–01:56.0 | C15 | T8 WRONG SOUND | C15: Uzay boşluğundaki dış çekimde kıskaç kapanırken yankılı metalik kilitlenme sesleri duyuluyor. | SURE | ✅ | 🅑 | kurgu |
| 15.10.2026 | Video | 01:58.0–02:02.0 | C16 | T3 TEXT | C16: Hava kilidinin yuvarlak kapısı üzerinde sarı uyarı levhası, yazılar ve astronotun göğüs armasında metin/semboller bulunuyor. | SURE | ✅ | 🅐 | kare |
| 15.10.2026 | Video | 01:58.0–02:02.0 | C16 | T9 WRONG FLOATING | C16: Henüz motorlar ateşlenmediği halde astronot hava kilidi içinde 1 g yerçekimi varmış gibi yürüyerek ilerliyor. | SURE | ✅ | 🅑+ | hareket |
| 15.10.2026 | Video | 02:05.5–02:07.0 | C18 | T6 LOOK CHANGE | C18: Bir önceki çekimde (02:05) sağ elle itilen gaz kolunu, bu yakın çekimde başparmağı sağa bakan bir sol el tutuyor. | SURE | ✅ | 🅑+ | kare / kurgu |
| 15.10.2026 | Video | 02:07.0–02:09.5 | C19 | T12 WEIGHTLESS EFFORT | C19: Geminin ana motorları tam güçle ateşlenirken kokpitteki iki astronotun bedeninde hiçbir ivme, sarsıntı veya koltuğa gömülme tepkisi oluşmuyor. | SURE | ✅ | 🅑 | hareket |
| 15.10.2026 | Video | 02:10.0–02:19.0 | C20 | T7 WRONG PARTICLES | C20: Vakum ortamında geminin altından çıkan dört roket alevi, atmosferde yanan dumanlı ve dalgalı kamp ateşi/meşale alevi gibi davranıyor. | SURE | ✅ | 🅐 | hareket |
| 15.10.2026 | Video | 02:10.0–02:19.0 | C20 | T11 OTHER | C20: Yalnızca soldaki geminin altından dikey roketler ateşlenmesine rağmen, yatay bir kolla bağlı olduğu sağdaki devasa modül üzerinde hiçbir dönme (tork), bükülme veya yukarı ivmelenme hareketi gerçekleşmiyor. | SURE | ✅ | 🅑 | anlatım / kurgu |
| 15.10.2026 | Video | 02:20.0–02:26.5 | C21-C23 | T3 TEXT | C21, C22, C23: Kokpitin sağ tarafındaki ve orta konsoldaki ekranlarda okunaksız arayüz yazıları ve grafik etiketleri yer alıyor. | SURE | ✅ | 🅑 | kare |
| 15.10.2026 | Video | 02:27.0–02:36.0 | C24 | T7 WRONG PARTICLES | C24: Geminin altındaki iki roket motorundan çıkan gazlar vakum fiziğine aykırı biçimde yoğun beyaz/gri duman bulutları oluşturarak dağılıyor. | SURE | ✅ | 🅐 | hareket |
| 15.10.2026 | Video | 02:27.0–02:36.0 | C24 | T11 OTHER | C24: Soldaki gemi tam güçle dikey itki uygularken aradaki ince yatay kol ve sağdaki büyük modül hiçbir fiziksel kuvvet/tork etkisine girmeden asılı duruyor. | SURE | ✅ | 🅑 | anlatım |
| 15.10.2026 | Video | 02:36.5–02:41.5 | C25 | T10 LAYOUT | C25: Ekrana büyük harflerle "THE SKY CATCH" ve "48 PEOPLE WERE FALLING TO EARTH. WE HAD ONE SHIP." yazılı sabit bitiş afişi/başlık kartı geliyor. | SURE | ✅ | 🅒 | — (tasarım kararı) |

---

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

> Girdi: `the sky catch.mp4` (24 kesme noktası, C01→C25) · 15.10.2026

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) | Sınıf | Doğduğu yer |
|---|---|---|---|---|---|:--:|---|:--:|:--:|
| 15.10.2026 | taslak_01 | Kesme 2 · 00:11.5 | C02 → C03 | S1 LOOK JUMP | C01'de sağ omuzda arma yokken C03'te mavi-altın yuvarlak arma beliriyor. | SURE | düzeltilecek | 🅑+ | kare |
| 15.10.2026 | taslak_01 | Kesme 2 · 00:11.5 | C02 → C03 | S4 WORLD JUMP | C02'de gemi dikey sarı pencereli modülün dibindeyken C03'te penceresiz yatay halkalı istasyon görülüyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 3 · 00:21.0 | C03 → C04 | S4 WORLD JUMP | C03'te uzaktaki halkalı modülden C04'te dikey sarı pencereli modüle ani geçiş; cam koyu maviye dönüyor. | SURE | düzeltilecek | 🅑 | kare / kurgu |
| 15.10.2026 | taslak_01 | Kesme 4 · 00:31.5 | C04 → C05 | S5 STATE RESET | C02'de tepesi sağlam antenliyken C05'te tepesi parçalanmış beton/metal yığını görünüyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 5 · 00:35.5 | C05 → C06 | S3 DIRECTION FLIP | Kadın astronot sağ pencereden dışarı bakarken C06'da sola dönüyor (180° aks atlaması). | SURE | düzeltilecek | 🅑 | kurgu |
| 15.10.2026 | taslak_01 | Kesme 5 · 00:35.5 | C05 → C06 | S1 LOOK JUMP | C01'de omuzda arma yokken C06'da sol omuzda yeşil üçgen arma ve göğüste valf beliriyor. | SURE | düzeltilecek | 🅑+ | kare |
| 15.10.2026 | taslak_01 | Kesme 6 · 00:45.5 | C06 → C07 | S1 LOOK JUMP | Turkuaz şerit ve valf varken C07'de koyu mavi şerit, mavi arma ve göğüste kutu beliriyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 7 · 00:47.0 | C07 → C08 | S1 LOOK JUMP | C07'deki koyu tenli yüzden C08'de tamamen başka bir kadına geçiş; ABD bayrağı beliriyor. | SURE | düzeltilecek | 🅐 | kare |
| 15.10.2026 | taslak_01 | Kesme 8 · 00:50.5 | C08 → C09 | S4 WORLD JUMP | Koyu gri/siyah gemi ve hava kilidi C09'da beyaza dönüşüyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 8 · 00:50.5 | C08 → C09 | S1 LOOK JUMP | Kolda mavi şerit ve ABD bayrağından C09'da yeşil/turkuaz kare arma ve büyük sırt çantasına geçiş. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 9 · 01:00.5 | C09 → C10 | S5 STATE RESET | Boşlukta yatay süzülen bacaklar kesme anında metal platforma dik ve sabit basmış hale geliyor. | SURE | düzeltilecek | 🅑 | kurgu / seçim |
| 15.10.2026 | taslak_01 | Kesme 9 · 01:00.5 | C09 → C10 | S7 SOUND JUMP | Kesmenin hemen ardından müziğin içinde vokal nefes/gülme sesi duyuluyor. | LIKELY | düzeltilecek | 🅑 | kurgu |
| 15.10.2026 | taslak_01 | Kesme 10 · 01:10.5 | C10 → C11 | S4 WORLD JUMP | Küçük tek kişilik basamaktan korkuluklu uzun platforma geçiş; arka planda halkalı uydu beliriyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 10 · 01:10.5 | C10 → C11 | S7 SOUND JUMP | Dış uzayda kapak açılırken yüksek yankılı metal çarpma sesi başlıyor. | SURE | düzeltilecek | 🅑 | kurgu |
| 15.10.2026 | taslak_01 | Kesme 11 · 01:20.5 | C11 → C12 | S3 DIRECTION FLIP | Kamera 180° aks çizgisi atlayarak modülü sağdan sola, Dünya'yı soldan sağa alıyor. | SURE | düzeltilecek | 🅑 | kurgu / kamera |
| 15.10.2026 | taslak_01 | Kesme 12 · 01:30.5 | C12 → C13 | S5 STATE RESET | Üstten menteşeli kapak C13'te sağdan menteşeli dolap kapağına dönüşüyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 12 · 01:30.5 | C12 → C13 | S1 LOOK JUMP | C11'deki turkuaz şeritli yüzden C13'te farklı kask yapısı ve koyu mavi şerite geçiş. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 13 · 01:40.5 | C13 → C14 | S4 WORLD JUMP | Dış çıkıntıdaki astronot C14'te modülün içindeki açık bir odacıkta duruyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 15 · 01:57.5 | C15 → C16 | S1 LOOK JUMP | Hava kilidine dönen astronotun yüzü değişiyor; kapı devasa kasa kapısına dönüşüyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 16 · 02:02.5 | C16 → C17 | S1 LOOK JUMP | Kokpitte her iki astronotun şeritleri maviye dönüyor; erkek pilotun yüzü değişiyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 17 · 02:05.5 | C17 → C18 | S1 LOOK JUMP | C17'de sağ elle itilen kontrol kolu, C18 yakın çekimde sol ele dönüşüyor. | SURE | düzeltilecek | 🅑+ | kare / kurgu |
| 15.10.2026 | taslak_01 | Kesme 19 · 02:09.5 | C19 → C20 | S4 WORLD JUMP | Gemide mavi logo beliriyor, karşı modül yumurta formuna şişiyor, sert ışık parlaması ekleniyor. | SURE | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 20 · 02:19.5 | C20 → C21 | S1 LOOK JUMP | Erkek astronotun sağ bileğinde ikinci bir turuncu şerit beliriyor. | LIKELY | düzeltilecek | 🅑 | kare |
| 15.10.2026 | taslak_01 | Kesme 23 · 02:26.5 | C23 → C24 | S5 STATE RESET | 4 roket alevi 2'ye düşüyor; modülde devasa yeni bir açık kapak/çıkıntı beliriyor. | SURE | düzeltilecek | 🅑 | kare / hareket |

---

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

> Girdi: `the sky catch.mp4` (Plansız, dış izleyici perspektifi) · 15.10.2026

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|
| 15.10.2026 | taslak_01 | C01–C02 | 48 yolcu Dünya'ya düşüyor, tek kurtarma gemisi yanaşıyor | İki astronot kokpitte oturuyor, bir uzay modülüne yaklaşıyor | ❌ Kısmen (tehlike ve 48 yolcu anlaşılmadı) |
| 15.10.2026 | taslak_01 | C03–C05 | Ana kenetlenme halkası kopmuş, geri çekilme | Yaklaşıp duruyorlar, tepede kırık bir yer var ama ne olduğu belirsiz | ❌ Kısmen (halka olduğu anlaşılmadı) |
| 15.10.2026 | taslak_01 | C06–C14 | Dış servis kapağı elle açılıp yedek çekme kolu çıkarılacak | Kadın astronot dışarı çıkıp bir kol açıyor | ✅ Tuttu (eylem anlaşılır) |
| 15.10.2026 | taslak_01 | C15–C17 | Dünya çok yakın, tek çene kapanıp kol kilitlenir | Kıskaç uzanan kolu yakalıyor | ✅ Tuttu |
| 15.10.2026 | taslak_01 | C18–C20 | Sana içeri girmeden ateşleme yapılmaz, güvene alınır | Kadın içeri dönüyor, koltuklara oturup kolu itiyorlar | ✅ Tuttu |
| 15.10.2026 | taslak_01 | C21–C24 | Kurtarma motorları ateşlenir, düşüş durur, 48 kişi güvende | Motorlar ateşleniyor, modülü itiyorlar, gülümsüyorlar | ❌ Kısmen (48 kişi bilgisi ancak 02:36 bitiş yazısında anlaşıldı) |

Duyulan replikler ↔ `FILM.md` §5:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|
| 15.10.2026 | taslak_01 | 00:00–02:41 | A2 NO SPEECH | Videoda hiçbir diyalog veya telsiz konuşması bulunmamaktadır (yalnızca 00:43'te nefes ve 01:01'de vokal ses). | R01–R24 | ❌ 24 repliğin tamamı eksik; kurguda İngilizce seslendirme eklenmeli. |
| 15.10.2026 | taslak_01 | 00:31 | A1 CONFUSED | Modülün tepesindeki hasarın uzay asansörü kabini olduğu ve Dünya'ya düştüğü anlaşılmıyor. | — | Giriş sesi (R01) ve C02 ekran yazısı şart. |
| 15.10.2026 | taslak_01 | 00:48 | A1 CONFUSED | Kadın astronotun kıyafeti, kol şeritleri ve yüzü değişiyor. | — | Referans sürekliliği sağlanmalı. |
| 15.10.2026 | taslak_01 | 01:01 | A4 SOUND OFF | Bot platforma basarken belirsiz vokal nefes/gülme sesi duyuluyor. | — | Kurguda ses miksi temizlenmeli. |
| 15.10.2026 | taslak_01 | 01:17–01:38 | A4 SOUND OFF | Uzay boşluğunda yüksek ve yankılı metal sürtünme sesleri duyuluyor. | — | Vakum kurallarına uygun ses tasarımı yapılmalı. |
| 15.10.2026 | taslak_01 | 02:10 | A1 CONFUSED | Yatay bağlı araç dikey itkiyle kaldırılırken tork oluşmaması kafa karıştırıyor. | — | İtki açısı ve rijit kilit vurgusu netleştirilmeli. |

---

## İZLEME (insan · `IZLEME_FORMU.md`)

| tarih | kim (A / B1 / B2 / B3) | sürüm (taslak_xx) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| 15.10.2026 | A (Sahip / Teknik Kontrol) | the_sky_catch | Kısmen (00:31, 02:10 - düşüş ve 48 kişi bilgisi 02:36'ya kadar yok) | Hayır (00:46, 01:31, 01:58, 02:03 suit/logo ve yüz değişimleri) | 01:41 (astronot kabin içinde), 02:06 (ters el), 02:27 (modülde yeni kapak) | Sahte: 01:21 (hareketsiz el), 02:03 (tepkisiz yüzler) | Diyalog yok | 01:01 (vokal ses), 01:17-01:53 (vakumda yüksek metal sesi), 02:10 (roket sesi yok) | 00:21-00:31, 01:41-01:50 | Zayıf (tehlike en sonda yazıyla söylendi) |
| 15.10.2026 | B (Dış İzleyici Simülasyonu) | the_sky_catch | İki astronot hasarlı modüle ulaşıp elle kolu açtı ve itti | Kendi gemilerini bağlayıp itmek | Modülün üstünün parçalanmış olması | Kolu yakalayıp motorları ateşlediler | Filmde hiç konuşma yoktu | 00:31'deki kırık yer ve içerdeki insanlar en son anlaşıldı | 00:21-00:30 arası durağan bekleyiş | Tek kelimeyle: Sakin (gerilim eksik) |

---

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 14.10.2026 | Film sahibin hazır üretim paketinden kurulur; plan `ODA/SAHIP_PLANI.md` ve `THE_SKY_CATCH.md`'de birebir saklanır. FILM.md §1-§7 doğrudan plandan oluşturulmuştur. | Sahip talimatı: "sana attığım .md film isminde 4dk film klasörünün içine koy ve o plandan dışarı çıkamadan o filmi yapacak planı hazırla". |
| 14.10.2026 | 10 Tasarım referansı numaralandırıldı: 1.DANE · 2.SANA · 3.KITE · 4.KABIN · 5.KOKPIT · 6.HALKA · 7.SERVIS · 8.MANDAL · 9.CEKMEKOLU · 10.DUZEN. | Sahip kararı (10.10.2026): referanslar numaralı ve adlı dosyalara (`ref/<No>.<AD>_v1.png`) bağlanır. |
| 14.10.2026 | Replikler kurguda eklenen ses olarak tasarlanmıştır. Video modellerine dudak senkronu veya ses üretimi zorlanmaz; video çıktıları temiz hareket taşır. | Sahibin açık plan kararı: "Üretim: GPT Image ile başlangıç kareleri → Gemini video ile klipler → ayrı İngilizce seslendirme ve kurgu. Diyalog post prodüksiyonda eklenir; yüz hareketleri dudak senkronuna bağımlı tutulmaz." |
| 14.10.2026 | 24 Çekimin her biri tam 10 saniye; toplam tam 04:00. | Sahip kuralı (08.10.2026) ve sahibin planı birebir örtüşür. |
| 14.10.2026 | Çekimlerde zincirleme yerine net kesmeler kullanılır. | Sahneleme bağımsız planlar olarak kurulmuştur; her sahne kendi başlangıç karesine dayanır. |
| 15.10.2026 | **QA KARARI 1: Açılış Hook'u ve 48 Kişi Bilgisinin Girişe Taşınması (Anlatım Düzeltmesi)** | İzleme ve Anlatım testinde hem sahip hem dış izleyici, modülün içinde 48 kişi olduğu ve Dünya'ya düştüğü bilgisinin 02:36'ya kadar anlaşılmadığını, bu yüzden filmin gerilimden yoksun "sakin" geçtiğini belirtti. Kurguda C01'in 00:01'inde Dane'in dış sesi ("The last elevator car was falling to Earth. We had one ship to catch it.") ve C02'de ekran yazısı ("48 ON BOARD / CABIN PRESSURE STABLE") mutlaka yerleştirilecek. |
| 15.10.2026 | **QA KARARI 2: 24 Replik Seslendirilmeli (Kurgu / Ses)** | Montajda hiç diyalog olmaması anlatım testinde en büyük kusur olarak raporlandı. FILM.md §5'teki R01–R24 seslendirme dosyaları kaydedilip timeline'a yerleştirilecek. |
| 15.10.2026 | **QA KARARI 3: Karakter ve Kostüm Sürekliliği (Kare / Referans Denetimi)** | Sana'nın turkuaz şeritli tulumu C07, C08, C13, C16, C17'de mavi şerite, mavi üçgen armalara ve ABD bayraklarına dönmüş; erkek pilotun yüzü değişmiş. `1.DANE_v1.png` ve `2.SANA_v1.png` referansları başlangıç karelerinde zorunlu tutulacak, bayrak/metin içeren kareler elenecek. |
| 15.10.2026 | **QA KARARI 4: Vakum Seslerinin Düzeltilmesi (Kurgu / Ses Miksi)** | C11, C12, C13, C15 dış uzay çekimlerinde duyulan yüksek yankılı mekanik sesler kaldırılacak; kask içi nefes ve gövde titreşimi (Y3 yatağı) mikslenecek. C10'daki istenmeyen vokal ses silinecek; C20'de roket motoru ateşleme sesi eklenecek. |
| 15.10.2026 | **QA KARARI 5: Ters El ve İvme Düzeltmesi (C18 / C19 / C20)** | C18'de sol el olarak üretilen itici kolu yakın planı sağ el olarak düzeltilecek; motor ateşlendiğinde kokpitte hafif ivme/gömülme hissi verilecek; C20 ve C24'teki roket alevi vakum fiziğine uygun mavi/parlak itki çizgisine çekilecek (dumanlı atmosfer alevi elenecek). |
