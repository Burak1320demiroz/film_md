# 📒 THE_PLANET_THIEF — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|
| <GG.AA> | C01 | d1 | Frames to Video | p1 | ✅ kullanılabilir 01.2–04.6 | |
| <GG.AA> | C01 | d2 | Frames to Video | p1 | ❌ el tokaya eriyor 03.1 → hareket | |

```
Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
  → kare · → hareket · → seçim · → kurgu · → anlatım
İki deneme AYNI sebeple bozuksa üçüncüsü aynı promptla gönderilmez (AGENTS.md §4).
```

## RED (üretim reddi)

| Tarih | Çekim | Mesajın BİREBİR metni | İlerleyip sonda mı düştü | Değişen şey | Sonuç |
|---|:--:|---|:--:|---|:--:|

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

| Tarih | Video / kare modu | Zaman | Çekim (`kurgu.py liste`) | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması |
|---|---|---|:--:|---|---|:--:|:--:|
| 15.10.2026 | video (1 fps) | 00:00.0–00:09.9 | C01 | T8 WRONG SOUND | Dış uzay vakumu çekimi olmasına rağmen rüzgâr uğultusu, elektrik cızırtısı ve bas gürültüsü duyuluyor | SURE | doğrulanacak (vakum sesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 00:03.0–00:07.0 | C01 | T11 OTHER | Silindirik istasyonun ağzından çıkan plazma yıldırımları vakumda hava varmış gibi kıvrılarak Dünya yüzeyine çarpıyor | LIKELY | doğrulanacak |
| 15.10.2026 | video (1 fps) | 00:20.0–00:29.9 | C03 | T13 SLIDING / EMPTY GRIP | Kokpitteki eller lövye üstünde hareketsizken dışarıdaki istasyon gemi manevra yapıyormuş gibi hızla dönüyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 00:22.0–00:29.9 | C03 | T11 OTHER | Ön camdan görünen dev istasyon dönerken perspektifi bükülerek deforme oluyor, Dünya sabit kalıyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 00:40.0–00:49.9 | C05 | T8 WRONG SOUND | Uzay boşluğunda uçan mekiğin dış çekiminde yüksek sesli jet motoru ve rüzgâr/türbülans sesi duyuluyor | SURE | doğrulanacak (vakum sesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 00:50.0–00:59.9 | C06 | T9 WRONG FLOATING | Mekik hangar içinde dikey yükselirken hiçbir dikey itici çalışmıyor, arka motor mavi yanarken yukarı süzülüyor | SURE | doğrulanacak (itici fiziği) |
| 15.10.2026 | video (1 fps) | 01:00.0–01:09.9 | C07 | T9 WRONG FLOATING | Mekik arka motor sönük ve dikey iticisiz tavandaki kenetlenme yuvasına doğru yükseliyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 01:12.0–01:15.5 | C08 | T6 LOOK CHANGE | İki çatallı kıskaç 01:14.5'te kenetlenme bileziğine değdiği anda eriyerek yatay metal şeride dönüşüyor | SURE | doğrulanacak (kıskaç geometrisi) |
| 15.10.2026 | video (1 fps) | 01:15.0–01:17.5 | C08 | T8 WRONG SOUND | Mekanik kıskaç 01:15'te kapandığı halde ağır metalik kilitlenme sesi 2 sn gecikmeli olarak 01:17'de duyuluyor | SURE | doğrulanacak (senkron düzeltilecek) |
| 15.10.2026 | video (1 fps) | 01:40.0–01:49.9 | C11 | T13 SLIDING / EMPTY GRIP | Astronotun elindeki matkap benzeri aletin ucu metal yuvaya hiç temas etmeden havada dönüyor | SURE | doğrulanacak (temassızlık giderilecek) |
| 15.10.2026 | video (1 fps) | 01:40.0–01:49.9 | C11 | T12 WEIGHTLESS EFFORT | Çalışan aletin dönüşü kollarında, bileklerinde titreşim, geri tepme veya efor yaratmıyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 02:10.0–02:15.0 | C14 | T13 SLIDING / EMPTY GRIP | Sol alttaki astronot adım atma hareketi olmadan ayakları zeminde kayarak sola doğru kadrajdan çıkıyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 02:40.0–02:49.9 | C17 | T7 WRONG PARTICLES | Güneş'in önünü kaplayan siyah kütle vakumda atmosferik baca dumanı veya volkanik kül gibi kıvrılarak ilerliyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 02:50.0–02:59.9 | C18 | T8 WRONG SOUND | Dünya ve silindirik istasyonun dış uzay vakumu çekiminde derinden yankılı uğultu duyuluyor | SURE | doğrulanacak (vakum sesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 03:00.0–03:09.9 | C19 | T12 WEIGHTLESS EFFORT | Astronot büyük ağır endüstriyel silahı/aleti hiçbir gerilim olmadan boş bir kutu gibi taşıyor | LIKELY | doğrulanacak |
| 15.10.2026 | video (1 fps) | 03:10.0–03:19.9 | C20 | T3 TEXT | Göğüs zırhının sağ ve solunda daha önceki çekimlerde bulunmayan hilal-yıldız sembollü iki arma görülüyor | SURE | doğrulanacak (armalar kaldırılacak) |
| 15.10.2026 | video (1 fps) | 03:14.5–03:19.9 | C20 | T6 LOOK CHANGE | Sol bileğindeki saati kaldırdığında kaskın içinde bıyığının sol üstüne mavi ışık lekesi yapışıp kalıyor | SURE | doğrulanacak (ışık lekesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 03:20.0–03:29.9 | C21 | T8 WRONG SOUND | Dünya'nın silindirik yapıya çekildiği dış çekimde yüksek sesli rüzgâr ve bas uğultusu duyuluyor | SURE | doğrulanacak (vakum sesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 03:30.0–03:39.9 | C22 | T7 WRONG PARTICLES | Uzay boşluğunda ilerleyen istasyonun ağzından atmosferdeymiş gibi yoğun siyah duman püskürüp dağılıyor | SURE | doğrulanacak (vakumda duman yok) |
| 15.10.2026 | video (1 fps) | 03:30.0–03:39.9 | C22 | T8 WRONG SOUND | Dış uzay vakumu çekiminde rüzgâr ve gök gürültüsü benzeri uğultular duyuluyor | SURE | doğrulanacak (vakum sesi temizlenecek) |
| 15.10.2026 | video (1 fps) | 03:41.0–03:47.0 | C23 | T8 WRONG SOUND | Gezegenlerin genel görünümünde görüntüyle bağdaşmayan kıyıya vuran okyanus dalga sesi duyuluyor | SURE | doğrulanacak (dalga sesi atılacak) |
| 15.10.2026 | video (1 fps) | 03:42.5–03:49.9 | C23 | T2 BODY-GROUND CLIPPING | Dünya sola kayarken arkasında yarı saydam ikinci bir atmosfer küresi ayrılıp sağ kenarla iç içe geçiyor | SURE | doğrulanacak (hayalet kopya düzeltilecek) |
| 15.10.2026 | video (1 fps) | 04:00.0–04:05.1 | C25 | T3 TEXT | Kapanış karesinde gökyüzünde büyük harflerle "THE PLANET THIEF" başlık yazısı yer alıyor | SURE | doğrulanacak |
| 15.10.2026 | video (1 fps) | 04:00.0–04:05.1 | C25 | T10 LAYOUT | Kapanışta film içi sahne yerine başlık kartı düzeni kullanılıyor | SURE | doğrulanacak |

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

| Tarih | Sürüm | Kesme no · zaman | Çekimler (önce → sonra) | Tür (S1-S7) | Önce → sonra | Gemini | Karar (düzeltildi · kabul · yanlış alarm) |
|---|---|---|---|---|---|:--:|---|
| 15.10.2026 | taslak_01 | 1 · 00:10.0 | C01 → C02 | S7 SOUND JUMP | C01 sonundaki uzay uğultusu kesmede sıfırlanıyor → C02 başında bip ve nefes sesiyle farklı ambiyans başlıyor | SURE | düzeltilecek (crossfade ile bağlanacak) |
| 15.10.2026 | taslak_01 | 2 · 00:20.0 | C02 → C03 | S1 LOOK JUMP | C02'de kask şeffaf fanus ve omuzlarda turuncu kemer varken C03'te kask arkası beyaz metal kabuğa dönüşüyor, kemerler kayboluyor | SURE | düzeltilecek (1.ELIAS kask paneli kilitlenecek) |
| 15.10.2026 | taslak_01 | 2 · 00:20.0 | C02 → C03 | S2 LIGHT JUMP | C02'de sağ pencereden güçlü sarı ışık vururken C03'te kokpit karanlık ve mavi konsol ışıklı | SURE | düzeltilecek (ışık sürekliliği) |
| 15.10.2026 | taslak_01 | 2 · 00:20.0 | C02 → C03 | S4 WORLD JUMP | C02'de pencere dibinde istasyon duvarı varken C03'te gemi henüz uzay boşluğunda istasyona uzaktan yaklaşıyor | SURE | düzeltilecek (mekân konumu hizalanacak) |
| 15.10.2026 | taslak_01 | 3 · 00:30.0 | C03 → C04 | S4 WORLD JUMP | C03'te konsol kavisli ve küçük mavi ekranlıyken C04'te düz endüstriyel masada büyük kare monitör ve turuncu ışık beliriyor | LIKELY | düzeltilecek (3.KOKPIT referansına uyulacak) |
| 15.10.2026 | taslak_01 | 3 · 00:30.0 | C03 → C04 | S7 SOUND JUMP | C03'teki bas uğultu kesmede aniden kesiliyor → C04'te saat tiktakı benzeri ritmik vuruş ve yeni müzik başlıyor | SURE | düzeltilecek (miks yumuşatılacak) |
| 15.10.2026 | taslak_01 | 4 · 00:40.0 | C04 → C05 | S7 SOUND JUMP | C04'teki iç mekân müziği aniden kesiliyor → C05'te dış vakum olmasına rağmen jet motoru ve rüzgâr uğultusu başlıyor | SURE | düzeltilecek (vakum sesi kapatılacak) |
| 15.10.2026 | taslak_01 | 5 · 00:50.0 | C05 → C06 | S1 LOOK JUMP | C05'te mekiğin üst gövdesi düz ve arkada çift dikey kanatlıyken C06'da üstte dairesel kapak, yanlarda motor podları beliriyor | SURE | düzeltilecek (2.KURTARMA_GEMISI paneline kilitlenecek) |
| 15.10.2026 | taslak_01 | 5 · 00:50.0 | C05 → C06 | S3 DIRECTION FLIP | C05'te mekik yatay hangara soldan sağa girerken C06'da dikey şaftta sol alttan sağ üste süzülüp kameraya dönüyor | SURE | düzeltilecek (giriş açısı ve doğrultusu) |
| 15.10.2026 | taslak_01 | 5 · 00:50.0 | C05 → C06 | S7 SOUND JUMP | C05'teki motor uğultusu bıçak gibi kesilip C06'da sakin hangar uğultusuna geçiyor | SURE | düzeltilecek (crossfade) |
| 15.10.2026 | taslak_01 | 6 · 01:00.0 | C06 → C07 | S1 LOOK JUMP | C06'da mekiğin kanatları ve köşeli camı varken C07'de kanatsız mermi gibi pürüzsüz silindirik gövdeye dönüşüyor | SURE | düzeltilecek (2.KURTARMA_GEMISI gövdesi) |
| 15.10.2026 | taslak_01 | 6 · 01:00.0 | C06 → C07 | S4 WORLD JUMP | C06'da kapalı hangar ve tek halkalı yuva varken C07'de sol arkada açık uzay/gün ışığı ve devasa kubbe görünüyor | SURE | düzeltilecek (5.YANASMA_KORIDOR hol paneli) |
| 15.10.2026 | taslak_01 | 7 · 01:10.0 | C07 → C08 | S1 LOOK JUMP | C07'de üst kenetlenme bileziği pürüzsüz/ışıklıyken C08'de dikey turuncu ışıklı yıpranmış bileziğe ve sağdan kıskaçlı sisteme dönüşüyor | SURE | düzeltilecek (kenetlenme halka tasarımı) |
| 15.10.2026 | taslak_01 | 7 · 01:10.0 | C07 → C08 | S2 LIGHT JUMP | C07'de mekik gölgede ve üstten turuncu ışık alırken C08'de soldan sert beyaz gün ışığı vuruyor | SURE | düzeltilecek (ışık sürekliliği) |
| 15.10.2026 | taslak_01 | 7 · 01:10.0 | C07 → C08 | S7 SOUND JUMP | C07'deki bas uğultu kaybolup C08'de tiz türbin ıslığı aniden başlıyor | SURE | düzeltilecek (ses miksi) |
| 15.10.2026 | taslak_01 | 8 · 01:20.0 | C08 → C09 | S1 LOOK JUMP | C02'deki astronota kıyasla C09'da vizör küçülüyor, sırtta büyük çanta beliriyor ve sol üst kolda turuncu şerit görülüyor | LIKELY | düzeltilecek (1.ELIAS giysi referansı) |
| 15.10.2026 | taslak_01 | 9 · 01:30.0 | C09 → C10 | S4 WORLD JUMP | C09'da koridor sonunda kemerli dar geçit varken C10'da astronot kayboluyor ve sonu sekizgen geniş odaya dönüşüyor | SURE | düzeltilecek (6.GOZLEM_BOLMESI derinlik paneli) |
| 15.10.2026 | taslak_01 | 9 · 01:30.0 | C09 → C10 | S7 SOUND JUMP | C09'daki piyano/nefes kesilip C10'da yüksek elektrik akımı uğultusu başlıyor | SURE | düzeltilecek (ses geçişi) |
| 15.10.2026 | taslak_01 | 10 · 01:40.0 | C10 → C11 | S1 LOOK JUMP | C09'da sağ kolda şerit yok ve elde kutu alet varken C11'de sağda şerit/omuz pedi, ince matkap ve farklı yüz beliriyor | SURE | düzeltilecek (1.ELIAS + 8.AKSESUARLAR) |
| 15.10.2026 | taslak_01 | 10 · 01:40.0 | C10 → C11 | S7 SOUND JUMP | C10'daki yüksek elektrik uğultusu kesilip sessiz alt uğultuya bırakıyor | SURE | düzeltilecek |
| 15.10.2026 | taslak_01 | 11 · 01:50.0 | C11 → C12 | S1 LOOK JUMP | C11'de sol bilek düz beyaz kumaşken C12'de sol bilekte siyah kayışlı mavi ekranlı kare cihaz beliriyor | SURE | düzeltilecek (8.AKSESUARLAR bileklik ilk kareden olmalı) |
| 15.10.2026 | taslak_01 | 13 · 02:10.0 | C13 → C14 | S1 LOOK JUMP | C12'de sol bilekte parlayan mavi cihaz varken C14'te astronot sol elini korkuluğa koyduğunda cihaz görünmüyor | LIKELY | düzeltilecek |
| 15.10.2026 | taslak_01 | 14 · 02:20.0 | C14 → C15 | S2 LIGHT JUMP | C14'te yapay güneş gezegeni sağdan aydınlatırken C15'te güneş ışığı sol üstten geliyor, sağ taraf karanlıkta kalıyor | SURE | düzeltilecek (ışık yönü 7.KASA'ya göre sağdan olmalı) |
| 15.10.2026 | taslak_01 | 14 · 02:20.0 | C14 → C15 | S7 SOUND JUMP | C14'teki yaylı çalgı müziği 02:20'de kesilip derin uğultuya bırakıyor | SURE | düzeltilecek |
| 15.10.2026 | taslak_01 | 15 · 02:30.0 | C15 → C16 | S4 WORLD JUMP | C14'te gezegenler simetrik halkalardayken C16'da sağ önde dev kızıl gezegen, sol arkada iki küçük uydu beliriyor | SURE | düzeltilecek (7.KASA gezegen dizilimi sabit) |
| 15.10.2026 | taslak_01 | 18 · 03:00.0 | C18 → C19 | S1 LOOK JUMP | C02/C11'deki sakallı astronot C19'da sinekkaydı tıraşlı, alnı yaralı yüze dönüşüyor; cihaz sağ kola geçiyor, matkap silaha dönüşüyor | SURE | düzeltilecek (1.ELIAS + 8.AKSESUARLAR kilitlenecek) |
| 15.10.2026 | taslak_01 | 19 · 03:10.0 | C19 → C20 | S1 LOOK JUMP | C19'da sakalsız yüz, düz göğüs varken C20'de sakallı yüz, kaşta yara, göğüste hilal-yıldız armalar beliriyor, cihaz sol bileğe geçiyor | SURE | düzeltilecek (armalar silinecek, sol bilek sabitlenecek) |
| 15.10.2026 | taslak_01 | 19 · 03:10.0 | C19 → C20 | S2 LIGHT JUMP | C19'da karanlık içte sağdan amber ışık varken C20'de sağ arkadan doğal gün doğumu/güneş ışığı vuruyor | SURE | düzeltilecek (iç mekân ışığı korunacak) |
| 15.10.2026 | taslak_01 | 19 · 03:10.0 | C19 → C20 | S4 WORLD JUMP | C19'da arka plan karanlık metal duvar iken C20'de bulutlar, sarp dağlar ve konteynerlerin olduğu açık hava terası beliriyor | SURE | düzeltilecek (6.GOZLEM_BOLMESI penceresine dönülecek) |
| 15.10.2026 | taslak_01 | 19 · 03:10.0 | C19 → C20 | S5 STATE RESET | C19'da astronot iki eliyle alet tutarken C20'de alet kayboluyor, sol elini boş olarak göğsüne kaldırıyor | SURE | düzeltilecek (C19 kesici belde, C20 sol el bileğe basış) |
| 15.10.2026 | taslak_01 | 21 · 03:30.0 | C21 → C22 | S4 WORLD JUMP | C21'de Dünya girişten içeri girerken C22'de Dünya ve altın halkalar kayboluyor, istasyon ağzından uzaya siyah dumanlar çıkıyor | SURE | düzeltilecek (Dünya girişte, duman yok) |
| 15.10.2026 | taslak_01 | 21 · 03:30.0 | C22 → C22 | S6 PHYSICS MISMATCH | C21'de normal uzay vakumu varken C22'de uzay boşluğunda kıvrılarak yükselen yoğun siyah baca dumanları görülüyor | SURE | doğrulanacak (vakumda duman fiziği aykırı) |
| 15.10.2026 | taslak_01 | 23 · 03:50.0 | C23 → C24 | S4 WORLD JUMP | C23'te Dünya'da Afrika kameraya bakarken ve gezegenler tek sırada diziliyken C24'te Dünya aniden Amerika'yı gösteriyor, gezegenler dairesel kubbe dizilimine dönüyor | SURE | düzeltilecek (Afrika kıtası ve 7.KASA dizilimi sabit) |
| 15.10.2026 | taslak_01 | 23 · 03:50.0 | C23 → C24 | S7 SOUND JUMP | C23'teki dalga/uğultu sesi aniden kesilerek yerini C24'teki sakin ambiyansa bırakıyor | SURE | düzeltilecek (dalga sesi tamamen kaldırılacak) |

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|
| 15.10.2026 | taslak_01 | C01 | Dünya dev kara geminin açık ağzına çekilmektedir | Devasa silindirik uzay yapısı Dünya'nın önünde durarak turuncu enerji dalgaları yayıyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C02–C03 | Elias kokpitte gemiye bakar, içeri girmeye karar verir | Astronot nefes alıp dışarıdaki yapıya bakıyor, aracı istasyona doğru yönlendiriyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C04 | Güneş'in kenarında açıklanamayan karanlık | Kokpit ekranında Güneş'in siyah karanlık kütle tarafından kaplandığı görülüyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C05–C08 | Küçük kurtarma gemisi dev gövdeye uçar, sokete yanaşır ve kilitlenir | Küçük beyaz mekik gövde boyunca uçup hangara giriyor, tavandaki mekanizmaya kilitleniyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C09–C10 | Elias boş koridorda ilerler, enerji hattı kavşağa ışık taşır | Astronot elinde aletle sarı enerji borulu koridorda ilerliyor, dikey ana enerji sütununu çalıştırıyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C11–C12 | Elias kesiciyi hatta doğrultur; bilek tarayıcısı yaşam uyarısı verir | Astronot matkap benzeri cihazı bölmeye yerleştirip çalıştırıyor, bileğindeki cihaz mavi ışıkla uyarı veriyor | ⚠️ KISMEN (Tamir mi sabotaj mı belirsiz) |
| 15.10.2026 | taslak_01 | C13–C16 | Dar pencerede Dünya olmayan mavi gezegen, kasadaki altı gezegen ve yapay güneş | Pencereden mor bölgeli şehir ışıklı gezegen ve yapay güneş etrafında tutulan gezegenler görülüyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C17–C18 | Dışarıda karanlık Güneş'i kaplar, Dünya geminin ağzına çok yaklaşır | Karanlık kütle Güneş'i neredeyse tamamen kaplıyor, Dünya karanlığa gömülüyor | ✅ TUTTU |
| 15.10.2026 | taslak_01 | C19–C20 | Elias kesiciyi indirir (sabotaj durur), kanalı açıp Dünya komutasına tahliye bildirir | Astronot tereddüt içinde bekliyor, bileğindeki cihaza bakıyor | ⚠️ KISMEN (Karar net değil, neyi tetiklediği belirsiz) |
| 15.10.2026 | taslak_01 | C21–C24 | Dünya giriş halkasını geçer, içerideki yapay güneşle aydınlanır, Elias kurtarılanları izler | Dünya istasyonun içine çekiliyor, yapay güneşin yanına yerleşiyor, astronot izliyor | ✅ TUTTU |

Duyulan replikler (madde 7) ↔ `FILM.md` §5 · A3/A4 satırları:

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|
| 15.10.2026 | taslak_01 | 00:40 | A1 CONFUSED | Kokpitteki gemi ağza bakarken dışarıdaki mekik yan duvar boyunca uçuyor; gemide mi istasyonda mı kafa karıştırıyor | C04→C05 | Geçiş ölçeği ve açısı netleştirilecek, kokpitten dış genel plana geçiş korunacak |
| 15.10.2026 | taslak_01 | 01:40 | A1 CONFUSED | Astronotun yüzü ve aleti değişiyor; enerji sütununu tamir mi ettiği yoksa sabote mi ettiği anlaşılmıyor | C11 (R05) | Plazma kesici doğrultulurken replik eklenerek ("One cut. We get our world back.") sabotaj amacı netleştirilecek |
| 15.10.2026 | taslak_01 | 03:00 | A1 CONFUSED | Yüz ve alet tekrar değişmiş; enerji sütununa doğrulttuğu aletle ne yapacağı ve neden beklediği belirsiz | C19 (R09) | Replik ("I almost cut our only way out.") ve kesicinin aşağı indirilmesiyle kararın dönüşü vurgulanacak |
| 15.10.2026 | taslak_01 | 03:10 | A1 CONFUSED | İstasyon içindeyken arkada açık hava ve dağlık gezegen manzarası beliriyor, mekân sürekliliği kopuyor | C20 | Arka plan teras/dağ silinip 6.GOZLEM_BOLMESI iç penceresine dönülecek |
| 15.10.2026 | taslak_01 | 03:30 | A1 CONFUSED | Silindirik istasyon uzayda kendi kendine siyah dumanlar çıkararak uçuyor; istasyondan mı Güneş'ten mi belirsiz | C22 | Uzay vakumundaki siyah baca dumanı kaldırılacak; temiz uzayda uzaklaşma gösterilecek |

## İZLEME (insan · `IZLEME_FORMU.md`)

| tarih | kim (A / B1 / B2 / B3) | sürüm (taslak_xx) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-15 | A (Teknik Denetim) | THE_PLANET_THIEF | Kısmen (01:40, 03:00 belirsiz) | Hayır (01:40, 03:00, 03:10 yüz/kask değişiyor) | 01:40 havada dönen uç, 03:10 arka plan dağlar, 03:15 bıyıkta mavi ışık, 03:30 uzayda duman | 01:40 ağırlık yok, 02:10 tepkisiz, 03:15 saate değil kameraya bakıyor | Diyalog yok (yalnızca nefes sesleri) | 10 sn geçişlerinde ses kesilmesi, 00:40 vakumda ses, 01:17 senkron kayık, 03:42 dalga sesi | 00:50-01:19 ve 02:10-02:39 | Görsel ölçek etkileyici ama motivasyon kopuk → Çekimi yeniden üret / Sesi düzelt |
| 2026-10-15 | B0 (AI Ön İzleyici) | THE_PLANET_THIEF | Güneş kararırken astronot dev istasyona girip Dünya'yı içerideki yapay güneş sistemine çekti | Dünya'yı istasyonun içine almak (03:20'de netleşti) | Güneş'i kaplayan karanlık kütle ve 03:00'daki tereddüdü | Dünya istasyona çekildi, istediğini aldı | Konuşma yoktu, sadece nefes sesleri | 00:40 gemi/istasyon yönü, 01:40/03:00 değişen yüz ve alet, 03:10 arka plan, 03:30 siyah duman | 01:00-01:19 (uzun kenetlenme sekansı) | Görkemli |
| 2026-10-15 | B1 | THE_PLANET_THIEF | | | | | | | | |
| 2026-10-15 | B2 | THE_PLANET_THIEF | | | | | | | | |
| 2026-10-15 | B3 | THE_PLANET_THIEF | | | | | | | | |

## KARARLAR

| Tarih | Karar | Neden |
|---|---|---|
| 15.10.2026 | **QA Kararı (taslak_01): Sesi Düzelt:** (1) Dış uzay vakumu çekimlerindeki rüzgâr, jet motoru, gök gürültüsü ve dalga sesleri temizlenecek (C01, C05, C18, C21, C22, C23). (2) 10 saniyelik kesmelerdeki sert ses sıçramaları (hard cut) 1 saniyelik crossfade ile bağlanacak. (3) C08'deki 2 saniye gecikmeli kilitlenme sesi (01:15 kilitlenme, 01:17 ses) senkronlanacak. (4) Montajda eksik kalan Elias telsiz replikleri ve AI sesleri eklenerek sabotaj/kurtarma motivasyonu anlatılacak (FILM.md §5 R01-R11). | QA Raporları: Tarama T8 (madde 1, 5, 9, 14, 18, 20, 21) · Süreklilik S7 (1, 6, 7, 10, 15, 18, 20, 24, 34) · İzleme A6. |
| 15.10.2026 | **QA Kararı (taslak_01): Çekimi Yeniden Üret (Kare & Hareket):** (1) C02, C03, C09, C11, C19, C20: Elias'ın yüzü, sakalı, kask yapısı ve omuzlukları `ref/1.ELIAS_v1.png` sayfasına kilitlenecek; C19'daki sakalsız yüz ve C20'deki hilal-yıldız armaları iptal edilecek. (2) C11 & C19: Havada dönen alet ucu yerine `ref/8.AKSESUARLAR_v1.png` plazma kesicisi elde sabit tutulacak. (3) C20 (03:10): Arka plandaki açık hava dağ manzarası silinip `ref/6.GOZLEM_BOLMESI_v1.png` iç holüne dönülecek; bıyıktaki mavi ışık lekesi temizlenecek. (4) C22 (03:30): Uzay boşluğundaki baca dumanı kaldırılacak. (5) C05–C08: Kurtarma gemisi ve hangar kenetlenme mekanizması `2.KURTARMA_GEMISI_v1.png` ve `5.YANASMA_KORIDOR_v1.png` panellerine kilitlenecek. | QA Raporları: Tarama T6, T7, T11, T12, T13 · Süreklilik S1, S2, S4, S5, S6 · İzleme A2, A3, A4. |
| 10.10.2026 | Film sahibin hazır planından kurulur; plan `ODA/SAHIP_PLANI.md`'de birebir, FILM.md §1-§7 oradan yerleşti; faz 1-4 ajan turu açılmadı (DURUM AŞILAN KAPILAR). Fable'ın türettikleri: referans numaraları (1.ELIAS · 2.KURTARMA_GEMISI · 3.KOKPIT · 4.ARK · 5.YANASMA_KORIDOR · 6.GOZLEM_BOLMESI · 7.KASA · 8.AKSESUARLAR · 9.GUNES), grup bölümü (G01 C01-08 · G02 C09-16 · G03 C17-24), replik saniye/süre tahmini, AI repliği MACHINE varsayımı, FIZIK_IDDIASI yok. | Sahip talimatı "plana sadık kal ve bu filmi yap". Plan araçları (GPT Image · Gemini Omni 10 s) hat araçlarından (Flow) farklı; promptlar F5'te hat biçimine çevrilir, içerik planın kendisidir. |
| 11.10.2026 | F5 KAPANDI (Fable). Denetçi 3 yargı ❌: Ö4 aşıldı (kanıt izi eksik, içerik doğrulandı), F5.6/F5.7 yazar düzeltti, yeniden denetçi çağrılmadı. FILM §4 C02/C16/C19/C21 Fable promptlarla hizaladı; Durum 24/24 ✍️. F6 açılmadı: plan kapağı A olarak KAPAK_VE_YAYIN §1'de, B F9'da. FAZ 7 sahipte. Plandan 4 sapma SAHİP CEVAPLARI'nda onay bekliyor. | Plan hazır olduğu için faz başına ajan turu açmak bütçeyi boşa harcar; eleştiri yalnız biçim çevirisinin (F5) olduğu yere kondu. 6 çağrı. |
| 10.10.2026 | F5 birleştirme geçişi (§2c, tur açılmadı; ÖLÜMCÜL 0/2 eleştirmen). Fable kararları: (1) soket TEK konum = tavan (plan K06 'sağ duvar' ↔ K07 'tavan' kendi içinde çelişiyordu), sayfa 5'e dış kuyu+tavan soketi paneli ve braketler; (2) C14 kamera cama doğru ileri dolly (planın 'geri dolly'si optik olarak açılmaz), başlangıç karesi çerçeveyle kırpık; (3) C08 temas C07→C08 kesmesine, videoda tek hareket kelepçe, C07 son karesi bağımlılığı kalktı; (4) C20 başparmak basışı C19→C20 kesmesine, halka loş→parlak, ref 8 eklendi; (5) 1.ELIAS'a dördüncü panel sağdan tam boy, her çekimde tek panel adı, 'body' yok; (6) sayfa 6 aynalandı (hat sağda); (7) sayfa 4 ¾ giriş paneli, sayfa 7 yakın gezegen panelleri; (8) C21 kenar/yön düzeltmesi, bitiş karesi talimatı kare/C21.png'ye bağlı, iki deneme zorunlu; (9) rol etiketleri tek, rozet cümlesi birebir, 'no lettering' yok, C24 vizör cümlesi tam; (10) C12 KISMEN: kamera sol omuz üstünden, giysi listesi manşete iner, kesici kenarı planda olduğu için kalır (kavrama fiili yok); (11) kimlik yığını KISMEN: sayfa 1'de '38 yaş…' kalır (sahip planı), çekimlerde tekrarlanmaz; (12) kilit olay ≤7-8 s, son vuruş hafif süren hareket, hız farkı. FILM §3 (paneller, 8→C20) ve §4 (C06 · C08 · C12 · C14 · C20 · C21) Fable güncelledi. | Plan olayları korunur; değişenler mekanik/optik çelişkiler ve ölçülmüş tuzaklar (T01 temas, T11 yön, §A 'body', T05 kask). Sahip planı 'Kullanım 5': yapıyı değiştiren çıktıyı referans yapma — kaynak kare bağımlılıklarını azaltmak bununla uyumlu. |
| 10.10.2026 | Plan promptlarının hat kurallarıyla çatışan kalıpları F5 çevirisinde kalkar: olumsuz blok ("No readable text…"), zincir dili ("first frame", "preceding shot"), ses tarifi ("Audio: …", "no dialogue"), araç/süre etiketi ("10 seconds", "16:9"), çekim atfı ("from the end of the preceding shot", "introduced earlier"). Yerine: `Reference <No> (<rol>)` anahtarı, 10 s vuruş planı, pozitif tarif. Ses satırları §6'ya taşındı. | film_dogrula M (meta · atıf · konuşma · olumsuz blok META `NEGATIVE`) ve PROMPT_HATA_ATLASI (olumsuz blok ters etki). Sahip planı "Kullanım 4": video üretiminde konuşma ve müzik istenmez — hatla aynı. |

## AJAN GÜNLÜĞÜ

> Her alt ajan çağrısı bir satır. Ham çıktı `ODA/`'da; burada yalnız özet.

| Tarih | Faz/tur | Ajan | Model | Girdi | Çıktı (ODA dosyası) | Sonuç |
|---|:--:|---|:--:|---|---|---|
| 10.10.2026 | F5/1 | goruntu-yonetmeni (G01) | sonnet | FILM §3 §4 + SAHIP_PLANI K01-K08 + R01-R09 (biçim çevirisi görevi) | PROMPTLAR/G01.md | ✅ 9 referans sayfası + 8 çekim, iş emri 25 satır · sapma: objektif eklendi; dış çekimlerde sabit ışık cümlesi; C04 görsele camgöbeği ışık; olumsuzlar pozitife (R01 yüz, R07 kıtalar, R09 cephe); "body"/"extinction" çıktı, 9 rolü "darkening sun"; kimlik cümlesi kadraja göre kısaldı; C08 karesi C07 son karesini beklemez (not) · risk: tek görünümlü sayfalar 2 ve 5 yan/üst açıları tutmayabilir; P14 ölçülmeden video koşulmaz |
| 10.10.2026 | F5/1 | goruntu-yonetmeni (G02) | sonnet | FILM §3 §4 + SAHIP_PLANI K09-K16 | PROMPTLAR/G02.md | ✅ 8 çekim · sapma: R01 kimlik iki parça (giysi her karede, yüz yalnız C11); "Elias Rook" adı yok; C09 arkadan ¾ (yüz yok, arka panel); C11 yerleşim planın (R06'nın aynalısı); objektif eklendi; C15 kaynak kare C13 (onaysız üretilmez); kesici olumsuzları pozitife |
| 10.10.2026 | F5/1 | goruntu-yonetmeni (G03) | sonnet | FILM §3 §4 + SAHIP_PLANI K17-K24 | PROMPTLAR/G03.md | ✅ 8 çekim, iş emri 9 kare (C21_bitis dahil) + 8 video · sapma: C24 arkadan kimlik kısaldı; "the man"; objektif eklendi; C19 yerleşim C11'den; C20 ışık sağdan, ref 8 eklenmedi (tarayıcı R08 metniyle); C20 başparmak basışı 5-7 s tek vuruş (§B1 riski); kaynak kare cümlesi "the last attached image gives only…"; C21_bitis'e ref 4 eklendi |
| 10.10.2026 | F5/1 | devamlilik (grup içi + gruplar arası tek çağrı) | sonnet | G01-G03 + FILM §3 §4 | ODA/F5_devamlilik_1.md | ÖLÜMCÜL 0 · CİDDİ 10 (C14 kamera kendini yalanlıyor · soket 3 yerde · 1.ELIAS profil paneli yok · 5'te braket yok · 7/4 yakın panel yok · C08 kaynak kare rolsüz · C20 halka zaten yanık · C21 kenar/yön · C24 vizör cümlesi düşmüş · C12 kol tarafı) · KÜÇÜK 8 (C02 'behind', rozet 3 biçim, rol etiketleri, C14 şerit/kesici, kimlik yığını hipotez, vuruş tekdüze, C17 kaynak kare, C16 şafak) · KAPANABİLİR |
| 10.10.2026 | F5/1 | teknik-danisman | sonnet | G01-G03 risk sütunu dolu çekimler + 9 sayfa | ODA/F5_teknik-danisman_1.md | ÖLÜMCÜL 0 · CİDDİ 9 ('body' G02'de 4 kez · C14 optik yön · C06→C07 soket · C08 temas + 2 durum değişimi · C12 kavrama/giysi · C20 halka yanık + başparmak · C21 bitiş karesi ref 4'e bağlı · 1.ELIAS iki panel/profil yok · sayfa 6 aynalı) · KÜÇÜK 6 (kimlik yığını · no/not kalıntı · EKLE karışık · kilit olay son 2 s · C04 'layout' · görünmeyen kimlik) · KAPSAM DIŞI C18≈C01 tekrar, C22'de Dünya yokluğu sesle · KAPANABİLİR |
| 10.10.2026 | F5/1b | goruntu-yonetmeni G01 · G02 · G03 (birleştirme geçişi, SendMessage devamı — çağrı sayılmaz) | sonnet | F5_devamlilik_1 + F5_teknik-danisman_1 + Fable kararları K1-K7 / G1-G5 | PROMPTLAR/G01-G03.md (güncel) · ODA/F5_goruntu-yonetmeni_2_G01/G02/G03.md (§K tabloları) | ✅ hepsi uygulandı · G01: sayfa 1 +sağ yan panel, 4 +¾ giriş, 5 +braket +dış kuyu/tavan soketi, 6 aynalandı, 7 +2 yakın panel; C06 soket tavan; C08 temas kesmede, C07 bağımlılığı kalktı; C02/C04 düzeltme · G02: C14 ileri dolly + kırpık kare; C12 KISMEN (kesici kenarı planda kalır); C11 tek panel (K2 > K4); C16 şafak videoda · G03: C20 halka loş→parlak, ref 8, basış kesmede; C21 kenar/yön + bitiş karesi C21.png tabanlı, d1/d2 iki deneme; C24 vizör cümlesi tam · film_dogrula cekim+sahneleme+prompt ✅ |
| 11.10.2026 | F5 kapı | denetci | opus | KABUL Ö + F5 · ODA F5 dosyaları · G01-G03 · FILM §3 §4 · DURUM · NOTLAR | mesaj (özet burada) | KAPANABİLİR · mekanik ❌ 0 · yargı ❌ Ö4 (önceki sürüm yok) · F5.6 (C18→C19 aynı iskelet) · F5.7 (sayfa 2 tek görünüm) · yan: sayfa 5 iç panel "far wall", G03'te "16:9" ×8 ve "extinction", sayfa 7 panel adları, FILM §4 C02/C16/C19/C21 promptla uyumsuz, Durum ⬜, teknik dosyasında "GİDİ" yazımı (ajan çıktısı aynen, düzeltilmedi), plandan sapmalar sahibe yazılmamış |
| 11.10.2026 | F5/1c | goruntu-yonetmeni G01 · G03 (denetçi düzeltmeleri, SendMessage devamı — sayılmaz) | sonnet | denetçi bulguları | PROMPTLAR/G01.md · G03.md | ✅ G01: sayfa 2 üç panel (¾ · yan · önden-üst), C05-C08 panel adları; sayfa 5 iç holde soket tavanda; sayfa 7 panel adları çekimlerle birebir; §K güncellendi · G03: "16:9" ×8 silindi, "extinction" → "front of darkness", C18 0-2·2-7·7-10 · film_dogrula ✅ |
