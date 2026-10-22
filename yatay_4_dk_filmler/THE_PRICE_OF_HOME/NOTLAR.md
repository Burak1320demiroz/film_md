# 📒 THE_PRICE_OF_HOME — Notlar

> Bu filmde olan her şeyin günlüğü. Hata burada **ret nedeni** olur, kural olmaz
> (`AGENTS.md` §1 ④). Satır olay olduğu gün yazılır.

---

## İŞARETLEME (sahip · Flow'da üretirken)

> Sahip her denemeyi izler ve işaretler: ✅ kullanılabilir (aralıkla) · ❌ değil (tek cümle neden).
> Bu bir onay değil, iş adımıdır; Fable hareketi göremez, seçim bu işaretten başlar.

| Tarih | Deneme dosyası | İşaret | Aralık / neden |
|---|---|:--:|---|

## DENEMELER

> 16.10.2026: satırı **`medya.py al <FILM> --yaz`** yazar (ham/'daki her yeni `Cxx_dN` için); elle yazılmaz.
> Girdi = EKLE satırındaki kare + referans numaraları.
> Ret nedeninin sonuna hatanın DOĞDUĞU YER yazılır (AGENTS.md §3):
>   → kare · → hareket · → seçim · → kurgu · → anlatım · → ses · → araç

| Tarih | Çekim | Deneme | Flow modu | Prompt sürümü | Sonuç | Kredi |
|---|:--:|:--:|---|:--:|---|:--:|

## MONTAJ EŞLEMESİ (hat dışı montaj · `medya.py bol`)

> Montaj hat dışında yapıldıysa (`cikti/` altında taslak/final dışı bir video) `medya.py bol <montaj> <FILM>` kesmeleri bulur.
> `taslak_01` doğrudan klip sırasıyla izlenmiştir ($C_n \approx \lfloor t/10 \rfloor + 1$).

| Kesme sırası (QA no) | Zaman | Plan çekimi | Deneme | Nasıl doğrulandı (kare · benzerlik) |
|:--:|---|:--:|:--:|---|
| 1–24 | 00:00–04:00 | C01–C24 | taslak_01 | İçerik ve zaman çapasından doğrulandı (10 sn klip periyodu) |
| 1–20 | 00:00–03:19 | C01–C20 | THE_PRICE_OF_HOME (2) | 20 çekimlik revize montaj taslağı (2026-10-22) |

## TARAMA (Gemini · `uretim_hatti/QA_PROMPTLARI/TARAMA.md`)

> Kaynak notu: `WHAT SHOULD BE IN THIS VIDEO` placeholder bırakıldığı için genel fizik ve süreklilik taranmıştır.

| Tarih | Video / kare modu | Zaman | Çekim | Tür (T1-T14) | Ne görüldü | Gemini | İnsan doğrulaması / Karar |
|---|---|---|:--:|---|---|:--:|---|
| 16.10.2026 | video (1 fps) | 00:18–00:19 | C02 | T8 | Uzay vakumunda motor uğultusu ve rüzgâr (whoosh) sesi | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 00:20–00:29 | C03 | T7 | Geminin altından çıkan duman atmosferik gibi asılı kalıyor | SURE | 🅑 Model fizik zaafı (→ prompt/hareket) |
| 16.10.2026 | video (1 fps) | 00:20–00:29 | C03 | T8 | Uzay vakumunda itici ve mekanik sesler | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 00:30–00:39 | C04 | T6 | Eli'nin göğüs arması ve kol şeridi yer/biçim değiştiriyor | SURE | 🅑 Çekim promptuna arma tarifi eklenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 00:40–00:49 | C05 | T8 | Vakumda kenetlenme, tıslama ve mekanik çarpma sesleri | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 00:50–00:59 | C06 | T6 | Eli'nin göğüs arması kayboluyor, beyaz tulum kalıyor | SURE | 🅑 Çekim promptuna arma eklenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 01:00–01:09 | C07 | T6 | Kaidedeki prizma kehribardan neredeyse opak siyaha dönüyor | SURE | 🅑 Prizmanın sönük/aydınlık durumu netleştirilecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 01:16–01:19 | C08 | T6 | Sol ön planda kasksız, sivil yakalı erkek beliriyor | SURE | 🅑+ "toward Eli off-camera" ifadesi kaldırılacak (→ prompt) |
| 16.10.2026 | video (1 fps) | 01:20–01:29 | C09 | T1 | Fotoğrafı tutan sağ eldivende iç kısımda deforme başparmak | LIKELY | 🅐 Başlangıç karesi kontrol edilecek (→ kare/hareket) |
| 16.10.2026 | video (1 fps) | 01:30–01:39 | C10 | T6 | Eli'nin göğsüne Mara'nın turkuaz üçgen arması geliyor | SURE | 🅑 Eli'nin arması prompta yazılacak (→ prompt) |
| 16.10.2026 | video (1 fps) | 01:30–01:39 | C10 | T11 | Eli ekrandayken Mara'nın sesi duyuluyor, ağız oynamıyor | LIKELY | 🅑+ Çift replik atılacak, mouth closed eklenecek (→ ses/prompt) |
| 16.10.2026 | video (1 fps) | 01:40–01:49 | C11 | T6 | Gemi kenetlenmede sola dönük, arka plandaki gezegen yön değiştirmiş | SURE | 🅑 Sahneleme haritasına yön kilitlenecek (→ sahneleme) |
| 16.10.2026 | video (1 fps) | 02:04–02:06 | C13 | T11 | Mara'nın ağzı oynuyor, bozuk mırıltı çıkıyor | SURE | 🅑+ Mouth closed eklenecek, ses kurguda verilecek (→ prompt/ses) |
| 16.10.2026 | video (1 fps) | 02:10–02:19 | C14 | T6 | Eli'nin göğüs arması ve eldiven bilekliği değişiyor | SURE | 🅑 Kostüm detayı yinelenmeli (→ prompt) |
| 16.10.2026 | video (1 fps) | 02:20–02:29 | C15 | T6 | Mara'nın sağ eldiveninde siyah parmak uçları beliriyor | SURE | 🅑 Eldiven tanımı kilitlenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 02:30–02:39 | C16 | T6 | Eli'nin göğüs arması tekrar üçgene dönüyor | SURE | 🅑 Çekim promptuna arma eklenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 02:40–02:49 | C17 | T6 | Kaideye uzanan sol kolda altın bilek göstergesi beliriyor | SURE | 🅑+ "cuff" çıkarılacak, right hand kilitlenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 02:50–02:59 | C18 | T8 | Geçit açılırken uzay vakumunda elektrik cızırtısı ve uğultu | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 03:00–03:09 | C19 | T11 | Halkanın DIŞINDAKİ arka planda da dev bir Dünya duruyor | SURE | 🅑 "Only inside ring, dark space outside" eklenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 03:10–03:19 | C20 | T6 | Gemi küt burunlu silindirik kapsüle dönüşüyor | SURE | 🅑 3.GEMI referansına arka/yan panel eklenecek (→ ref/prompt) |
| 16.10.2026 | video (1 fps) | 03:10–03:19 | C20 | T8 | Vakumda itici rüzgârı (whoosh) sesi | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 03:10–03:19 | C20 | T11 | Dünya halkanın dışındaki uzaya taşıyor | SURE | 🅑 Dünya halkanın içine hapsedilecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 03:20–03:29 | C21 | T6 | Gemi çift motorlu uzun kruvazöre dönüşüyor | SURE | 🅑 Referans sayfası tüm açıları içermeli (→ ref) |
| 16.10.2026 | video (1 fps) | 03:20–03:29 | C21 | T8 | Vakumda jet/roket kükremesi sesi | SURE | 🅑 Kurguda klip sesi susturulacak (→ kurgu) |
| 16.10.2026 | video (1 fps) | 03:20–03:29 | C21 | T11 | Sol altta Satürn benzeri halkalı gezegen beliriyor | SURE | 🅑 "no extra planets" kısıtı konacak (→ prompt) |
| 16.10.2026 | video (1 fps) | 03:30–03:39 | C22 | T6 | İki astronot da aynı mavi üçgen armayı takıyor | SURE | 🅑 Eli ve Mara armaları ayrı ayrı yazılacak (→ prompt) |
| 16.10.2026 | video (1 fps) | 03:40–03:49 | C23 | T6 | Vey'in kafa yapısı, göz rengi ve omuz zırhı değişiyor | SURE | 🅑 Koyu mor ten ve dar yüz prompta eklenecek (→ prompt) |
| 16.10.2026 | video (1 fps) | 03:50–03:59 | C24 | T6 | Mara'nın kolunda ABD bayrağı ve mavi ekran beliriyor | SURE | 🅑 Kostüm tarifi C24'e eksiksiz eklenecek (→ prompt) |
| 2026-10-22 | video (1 fps) | 00:08.5 | C01 | T13 | Beyaz uzay gemisi itici olmadan yana doğru kayıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 00:15.2 | C03 | T13 | İki astronot zemin üzerinde kaskatı durup hafifçe havada süzülüyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 00:25.4 | C04 | T1 | Konsoldaki parlayan kristal temas çizgisi olmadan kaideyle kaynaşıyor | SURE | Doğrulandı |
| 2026-10-22 | video (1 fps) | 00:35.2 | C05 | T6 | Mara'nın eldiven parmakları konsol kenarıyla hafifçe eriyip kaynaşıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 00:41.1 | C05 | T6 | Erkek astronotun kaskı aniden kaybolup saçı/sakalı açığa çıkıyor | SURE | Doğrulandı (yeniden üretim önceliği) |
| 2026-10-22 | video (1 fps) | 00:45.0 | C06 | T11 | Eldivenli ellerde tutulan sahil fotoğrafının arkasında 3. astronot kaskı beliriyor | SURE | Doğrulandı (temizlenecek) |
| 2026-10-22 | video (1 fps) | 00:58.3 | C07 | T1 | Erkek astronotun dudak hareketi ve sesi arasında senkron kayması var | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 01:21.0 | C09 | T7 | Mara'nın kapalı vizörünün içinden yukarı doğru buhar/duman yükseliyor | SURE | Doğrulandı |
| 2026-10-22 | video (1 fps) | 01:31.2 | C10 | T13 | Erkeğin eldivenli parmakları konsol üzerinde yüzey teması olmadan kayıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 01:41.0 | C11 | T1 | Mara'nın eldiven uçları holografik ışık hüzmeleriyle kaynaşıyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 02:03.1 | C13 | T2 | Konsoldaki parlayan ışık halkası metal çemberin içinden hayalet gibi geçiyor | SURE | Doğrulandı |
| 2026-10-22 | video (1 fps) | 02:12.4 | C14 | T9 | Geçit içindeki Dünya istasyon yapısına göre yerçekimsiz/rotasyonsuz duruyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 02:22.0 | C16 | T13 | Gemi itici alevlerine rağmen geçide doğru kayma hareketiyle ilerliyor | LIKELY | Doğrulandı |
| 2026-10-22 | video (1 fps) | 02:40.1 | C18 | T6 | Kokpitte her iki astronotun emniyet kemerleri/kayışları kayboluyor | SURE | Doğrulandı |
| 2026-10-22 | video (1 fps) | 02:56.2 | C19 | T13 | Karakterlerin baş dönüşlerinde AI interpolasyon kayması (glide) var | LIKELY | Doğrulandı |

## SÜREKLİLİK (Gemini · `SUREKLILIK.md`)

> Kaynak notu: `CUT LIST` placeholder bırakıldığı için Gemini 10 sn periyotla 23 kesmeyi varsayarak incelemiştir.

| Tarih | Sürüm | Kesme no · zaman | Çekimler | Tür (S1-S7) | Önce → sonra | Gemini | Karar |
|---|---|---|---|---|---|:--:|---|
| 16.10.2026 | taslak_01 | Cut 1 · 00:10.0 | C01 → C02 | S4 (WORLD) / S3 | Kokpitte arkada mavi Dünya → dışta gaz devi ve istasyon; gemi geri uçuyor | SURE | 🅒 Flashback zaman kartı eksik (`11 DAKİKA ÖNCE`) |
| 16.10.2026 | taslak_01 | Cut 2 · 00:20.0 | C02 → C03 | S3 (DIR) / S1 | Burun sola dönükken sağa dönüyor, burun kenetlenme halkası sivri koniye dönüşüyor | SURE | 🅑 Yön ve burun formu kilitlenecek (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 3 · 00:30.0 | C03 → C04 | S1 (LOOK) | Eli tek mavi şerit → iki mavi şerit ve yuvarlak göğüs arması değişimi | SURE | 🅑 Kol şeridi ve arma prompta yazılacak (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 5 · 00:50.0 | C05 → C06 | S1 (LOOK) | Eli'nin arması üçgene dönüşüyor, kol şeridi tekrar tek kalın mavi oluyor | SURE | 🅑 Eli arması sabitlenecek (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 6 · 01:00.0 | C06 → C07 | S4 / S5 (WORLD) | Vey kaide arkasındayken yok oluyor, kaidede el izi beliriyor | SURE | 🅒 Senaryo gereği kaide yakın çekimidir (kabul) |
| 16.10.2026 | taslak_01 | Cut 7 · 01:10.0 | C07 → C08 | S5 (STATE) | Parlayan kristal var → kaide üstü düz kapakla kapalı | SURE | 🅑 Prizma durumu her çekimde yazılmalı (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 8 · 01:20.0 | C08 → C09 | S1 (LOOK) | Soldaki erkek kasksız sivil → POV çekimde kask vizörü yansıması var | LIKELY | 🅑+ C08'deki referanssız adam temizlenecek (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 9 · 01:30.0 | C09 → C10 | S5 (STATE) | Eller fotoğrafta → eller aşağıda, kristal açıkta duruyor | SURE | 🅒 Çekim açısı değişimi (kabul) |
| 16.10.2026 | taslak_01 | Cut 10 · 01:40.0 | C10 → C11 | S4 (WORLD) | İstasyon halkası sağdayken sola geçiyor | SURE | 🅑 Sahneleme haritasına yön kilitlenecek (→ sahneleme) |
| 16.10.2026 | taslak_01 | Cut 13 · 02:10.0 | C13 → C14 | S1 / S5 | Siyah askılar beyaza dönüyor; kristal kaybolup düz el izi yüzeyi kalıyor | SURE | 🅑 Askı rengi ve kristal durumu kilitlenecek (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 14 · 02:20.0 | C14 → C15 | S1 / S5 | Eli'nin omuz askıları ve kristal geri geliyor; eldivende siyah uçlar | SURE | 🅑 Kıyafet ve kaide sürekliliği (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 16 · 02:40.0 | C16 → C17 | S1 (LOOK) | Sağ el üzerinde saat yokken → sol kolda altın bilek göstergesi beliriyor | SURE | 🅑+ "cuff" çıkarılacak, right hand yazılacak (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 17 · 02:50.0 | C17 → C18 | S4 (WORLD) | Halka ve yanaşmış gemi yatay ters dönüyor; ikinci uydu beliriyor | SURE | 🅑 Dış uzay sahnelemesi kilitlenecek (→ sahneleme) |
| 16.10.2026 | taslak_01 | Cut 18 · 03:00.0 | C18 → C19 | S4 (WORLD) | Gemi istasyona kenetliyken → kokpitten bakışta serbest uzayda ve Dünya sağda | SURE | 🅒 C19/C20 sıralaması ve kokpit açısı kontrol edilecek |
| 16.10.2026 | taslak_01 | Cut 19 · 03:10.0 | C19 → C20 | S4 (WORLD) | Kokpit öne bakarken → dış çekimde gemi soldan ayrılıyor, Dünya halkanın dışına taşıyor | SURE | 🅑 Ayrılış açısı ve portal Dünya kısıtı (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 20 · 03:20.0 | C20 → C21 | S4 (WORLD) | Gemi sağa giderken → kameradan uzaklaşıp portala giriyor; sol altta Satürn | SURE | 🅑 Ekstra gezegen çıkarılacak (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 21 · 03:30.0 | C21 → C22 | S2 (LIGHT) | Bembeyaz portal ışığı parlaması → aniden normal kokpit aydınlığına sert kesme | SURE | 🅒 Kurguda beyaz parlamadan kokpite çözünme/karışım geçişi verilecek |
| 16.10.2026 | taslak_01 | Cut 22 · 03:40.0 | C22 → C23 | S1 (LOOK) | Koyu mor tenli Vey → gri-kahverengi tenli geniş başlı Vey | SURE | 🅑 Koyu mor ten prompta yazılacak (→ prompt) |
| 16.10.2026 | taslak_01 | Cut 23 · 03:50.0 | C23 → C24 | S1 (LOOK) | Mara düz beyaz kol → Amerikan bayrağı ve mavi ekran | SURE | 🅑 C24'e kostüm kısıtları eklenecek (→ prompt) |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 01 · 00:10.0 | C01 → C02 | S3 / S4 | Gemi yönü ters dönüyor, gaz devi soldan sağa sıçrıyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 03 · 00:25.0 | C03 → C04 | S5 STATE RESET | Parlayan kristal sönük/siyah oluyor, karakterler konsol dibinden kayboluyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 04 · 00:35.0 | C04 → C05 | S1 / S5 | Konsol üstü kapalı kapak oluyor; 00:41'de erkeğin kaskı yok oluyor | SURE | Yeniden üretim önceliği |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 05 · 00:45.0 | C05 → C06 | S4 WORLD JUMP | Fotoğraf tutulurken arkada siyah vizörlü 3. astronot kaskı beliriyor | SURE | Düzeltilecek |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 06 · 00:55.0 | C06 → C07 | S1 / S4 | Erkeğin kaskı geri geliyor, uzaylı yok oluyor, arka duvar ekrana dönüyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 09 · 01:25.0 | C09 → C10 | S1 / S5 | Erkeğin omuz kayışları kayboluyor, arması rozete dönüyor, kristal yok oluyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 11 · 01:45.0 | C11 → C12 | S7 SOUND JUMP | 01:47'de orkestral müzik aniden kesilip 01:48'de solo yaylıya atlıyor | SURE | Kurguda crossfade ile bağlanacak |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 14 · 02:15.0 | C14 → C15 | S3 / S4 | İstasyon ve geçit yönü ters dönüyor, gaz devi kayboluyor, Dünya dışarı taşıyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 15 · 02:20.0 | C15 → C16 | S1 LOOK JUMP | Küt burunlu kapsül yan kanatlı uzun mekiğe dönüşüyor | SURE | Kabul |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 17 · 02:40.0 | C17 → C18 | S1 / S4 | Kokpitte kemerler yok oluyor; camda hem geçit hem Dünya aynı anda görünüyor | SURE | Mekânsal çelişki |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 19 · 03:00.0 | C19 → C20 | S1 LOOK JUMP | Mor tenli uzaylı bej renkli geniş kemik başlıklı yaratığa dönüşüyor | SURE | Prompt kısıtı |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | Kesme 20 · 03:10.0 | C20 → C21 | S1 LOOK JUMP | Mara'nın kolunda sarı şerit yerine ABD bayrağı ve mavi ekran beliriyor | SURE | C21 kurgudan atılınca çözülür |

## ANLATIM (Gemini · `ANLATIM_TESTI.md`)

| Tarih | Sürüm | Çekim | Planlanan bilgi | İzleyicinin anladığı | Tuttu mu |
|---|---|:--:|---|---|:--:|
| 16.10.2026 | taslak_01 | C01 | Açılış kancası: Mara Eli'yi tanımıyor | Kokpitte endişeli bakışma; arkada Dünya var | ⚠️ Replik eksik |
| 16.10.2026 | taslak_01 | C02 | Geçmişe dönüş: İstasyona yaklaşım | Jüpiter benzeri gezegen yanındaki istasyona yaklaşma | ✅ |
| 16.10.2026 | taslak_01 | C03 | Yanaşma manevrası | İstasyon kapısına doğru süzülüş | ✅ |
| 16.10.2026 | taslak_01 | C04 | Kokpit kenetlenme hazırlığı | Kokpitten istasyon halkasına bakış | ⚠️ Pencere açısı kafa karıştırdı |
| 16.10.2026 | taslak_01 | C05 | Mekanik kenetlenme kilitlenir | Mekanik kilitlerle istasyona bağlanma | ✅ |
| 16.10.2026 | taslak_01 | C06 | Vey ile karşılaşma, takas odası | Odada konsol başında uzaylıyla karşılaşma | ✅ |
| 16.10.2026 | taslak_01 | C07 | Kaide aktifleşir, el izi paneli açılır | Konsol ve el izi tarayıcısı aktifleşir | ⚠️ Replik olmadan amaç belirsiz |
| 16.10.2026 | taslak_01 | C08 | Mara bedeli anlar, Eli'ye bakar | Mara üzüntüyle Eli'ye bakar | ✅ (Kask hatası hariç tuttu) |
| 16.10.2026 | taslak_01 | C09 | Sahil fotoğrafı: Kaybolacak anı | Sahildeki çift fotoğrafı ve alyans | ❌ "Hissi istiyorum" anlaşılamadı |
| 16.10.2026 | taslak_01 | C10 | Eli başka seçenek arar, zaman daralıyor | Zaman daralıyor, başka seçenek olmalı | ✅ (Model repliği sayesinde tuttu) |
| 16.10.2026 | taslak_01 | C11 | İstasyon ışıkları sönüyor | Dış istasyon durağan planı | ❓ Bahsedilmedi (tempo düştü) |
| 16.10.2026 | taslak_01 | C12 | Vey şartın değişmeyeceğini onaylar | Uzaylının sessiz bekleyişi | ❓ Bahsedilmedi |
| 16.10.2026 | taslak_01 | C13 | Eli kendi anılarını vermeyi teklif eder | Eli yerini almayı teklif eder | ✅ (Model repliği sayesinde tuttu) |
| 16.10.2026 | taslak_01 | C14 | Mara kararını verir | Mara elini konsola uzatır | ✅ |
| 16.10.2026 | taslak_01 | C15 | Mara ile Vey son kez bakar | — | ❓ Bahsedilmedi |
| 16.10.2026 | taslak_01 | C16 | Eli çaresizce başını eğer | — | ❓ Bahsedilmedi |
| 16.10.2026 | taslak_01 | C17 | Mara elini panele basar, anılar çekilir | Mara elini basarak mekanizmayı çalıştırır | ✅ |
| 16.10.2026 | taslak_01 | C18 | Geçit açılır, Dünya görünür | Halkanın içinde Dünya geçidi açılır | ✅ |
| 16.10.2026 | taslak_01 | C19 | Kokpite dönüş, geçide son bakış | Kokpitte arkada portal ve Dünya | ⚠️ C20'den önce kokpitte olma hatası |
| 16.10.2026 | taslak_01 | C20 | Geminin ayrılışı ve portala yöneliş | Gemi ayrılır ve portala doğru uçar | ✅ |
| 16.10.2026 | taslak_01 | C21 | Geçidin içine dalış, beyaz ışık | Gemi geçidin içine dalar | ✅ |
| 16.10.2026 | taslak_01 | C22 | Dünya yörüngesi: Mara Eli'yi tanımaz | Dünya yörüngesi, Mara'nın sözüyle yıkılış | ✅ (Fısıltı boğuk ama tepki tuttu) |
| 16.10.2026 | taslak_01 | C23 | Vey kristaldeki anıları içine çeker | Uzaylı ışık ağıyla dolan kristale bakıp iç çeker | ✅ |
| 16.10.2026 | taslak_01 | C24 | Yeni başlangıç: Eli sabırla bakar | İkisi kokpitte birbirine gülümser | ⚠️ Kalıcı unutuş anlaşılamadı |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C01–C02 | İstasyona yaklaşım ve kenetlenme | Gemi istasyona yanaşıp kenetlenir | Evet |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C03–C06 | Takas konsolu ve sahil fotoğrafı (kaybolacak anı) | Kristalli konsol başında duruş ve fotoğraf tutuş | Kısmen (00:15-00:44 donukluk) |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C07–C10 | Zaman daralıyor, erkeğin fedakarlık teklifi | Erkeğin onun yerini almayı teklif ettiği tam anlaşıldı | Evet |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C11–C13 | Mara'nın teklifi reddedip elini basması | Mara elini panele basıp altın ışık dalgası yayar | Evet |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C14–C16 | Geçidin açılışı ve Dünya'ya uçuş | Halka içinde Dünya görünür, gemi geçide dalar | Evet |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C17–C19 | Dünya'ya varış, Mara'nın hafıza kaybı | Mara "Who are you?" diyerek unuttuğunu gösterir, erkek yıkılır | Evet (Vurucu) |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C20 | Kristale hapsolan anılar ve uzaylının nefesi | Kristal anılarla parlar, uzaylı derin iç çeker | Evet |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | C21 | Final | İkisi birden tekrar birbirine gülümsüyor | Hayır (A1 - Bedeli sıfırlıyor) |

### Duyulan Replikler ve Anlatım Tablosu (A1–A4)

| Tarih | Sürüm | Zaman | Tür (A1-A4) | Ne duyuldu / görüldü | Replik no | Karar |
|---|---|---|---|---|---|---|
| 16.10.2026 | taslak_01 | 00:00 | A1 CONFUSED | İlk saniyede arkada Dünya var, 00:10'da Jüpiter yanında | C01 → C02 | Kurguya `"11 DAKİKA ÖNCE"` kartı eklenecek |
| 16.10.2026 | taslak_01 | 00:30 | A1 CONFUSED | Kokpit pencere yönü ve kenetlenme açısı kafa karıştırıyor | C04 | Kamera yönü sahneleme kuralıyla netleştirilecek |
| 16.10.2026 | taslak_01 | 01:00 | A1 CONFUSED | Kristal ve el izi tarayıcısının işlevi açıklanmadığı için belirsiz | C07 | R07–R09 replikleri kurguda eklenecek |
| 16.10.2026 | taslak_01 | 01:16 | A1 CONFUSED | Erkek astronot kaskı çıkmış, 01:30'da tekrar takılı | C08 | Prompttaki "toward Eli off-camera" kaldırılacak |
| 16.10.2026 | taslak_01 | 01:34 | A1 CONFUSED | Mara'nın sesi duyulurken ekranda Eli var; kimin konuştuğu belirsiz | C10 | Model sesi atılacak, seslendirme temizlenecek |
| 16.10.2026 | taslak_01 | 01:40 | A2 WOULD STOP | İlk 100 sn diyalogsuz ve durağan; izleyici bırakmak istedi | C11 | Replikler ses olarak eklenince tempo düzelecek |
| 16.10.2026 | taslak_01 | 02:04 | A3 LINE UNCLEAR | Mara'nın mırıltısı boğuk ve yapay zeka fonetiğiyle anlaşılmıyor | C13 | Model sesi susturulacak, net seslendirme konacak |
| 16.10.2026 | taslak_01 | 03:00 | A1 CONFUSED | Gemi ayrılmadan önce kokpitte arkada portal ve Dünya var | C19 | Kurguda C19/C20 sırası kontrol edilecek |
| 16.10.2026 | taslak_01 | 03:36 | A3 LINE UNCLEAR | Mara'nın fısıldadığı "Who are you?" anlaşılmıyor | C22 / R24 | R24 repliği net ses kaydıyla eklenecek |
| 16.10.2026 | taslak_01 | 03:46 | A4 SOUND OFF | Uzaylı insan sesiyle yüksek sesli "Ahhh" iç çekişi yapıyor | C23 | Klip sesi kurguda tamamen susturulacak |
| 16.10.2026 | taslak_01 | 03:50 | A1 CONFUSED | Yıkılıştan sonra ikisi birden mutlu gülümseyince bedel boşa düştü | C24 | Eli iç sesi R26–R27 kurguda eklenecek |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | 00:58–01:02 | A4 | "I'm trying to find a way" aynı ses kaydı iki kez üst üste çalıyor | R02 | Kurguda mükerrer ses silinecek |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | 01:19–01:21 | A3 | "...for years" fısıltısı fon müziği altında boğuluyor | R05 | Müzik ducking / ses düzeltilecek |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | 01:47–01:48 | A4 | Orkestral müzik aniden kesilip solo yaylıya atlıyor | — | Kurguda crossfade yapılacak |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | 02:56 | — | Mara: "Who are you?" | R10 | Korunacak (Trajik zirve) |
| 2026-10-22 | THE_PRICE_OF_HOME (2) | 03:06 | A4 | Uzaylı insan nefesiyle derin iç çekiyor | R11 | Klip sesi kurguda kısılacak |

## İZLEME (Gemini Simülasyonu — insan izleyici değil)

> Not: Bu bölüm Gemini modeli tarafından üretilen simülasyondur. Gerçek yayın onayı için sahip + en az 2 dış insan izleyici formu gereklidir (`AGENTS.md` §1 ⑤).

| Tarih | Kim | Sürüm | 1 (Ne oldu) | 2 (Aynı kişi mi) | 3 (Saçma şey) | 4 (Oyunculuk) | 5 (Diyalog) | 6 (Ses) | 7 (Sıkılma) | 8 (His/Son) |
|---|---|---|---|---|---|---|---|---|---|---|
| 16.10.2026 | A (Gemini) | taslak_01 | kısmen (02:10-03:09 feda mantığı boşta) | hayır (01:16 kask yok, 03:40 uzaylı değişiyor, 03:50 ABD bayrağı) | 00:00 arkada Dünya, 00:10 gemi yan uçuyor, 01:18 kask dışından buhar, 03:00 çift Dünya | 01:37 ve 03:36 dudaksız ses; 02:04 bozuk yüz | 01:34 çift tekrar, 02:04 bozuk telaffuz, 03:36 "Her you" | 00:18, 00:21, 00:41 vakumda ses; 03:46 insan iç çekişi | 00:50-01:15 ve 01:40-02:00 | Kısmi rahatlama ama katarsis zayıf |
| 16.10.2026 | B1 (Gemini) | taslak_01 | İstasyona kenetlendiler, kadın butona bastı, Dünya'ya döndüler | Eve dönmek | Bedelin ne olduğu anlaşılmadı (ikisi de döndü) | İkisi de kurtulup Dünya'ya döndü | 02:04 anlaşılmadı, 01:34 iki kez söylendi, 03:36 kopuktu | 00:00 Dünya'nın başta olması, 02:15'te yerini alayım deyip ikisinin dönmesi | 01:40-02:00 arası durağan planlar | Kopuk |
| 2026-10-22 | A (Sahip - Taslak) | THE_PRICE_OF_HOME (2) | Kısmen (00:15-00:44 donukluk, 02:40 mekân, 03:10 tezat) | Hayır (00:41 kask yok, 01:25 arma, 03:10 bayrak) | 00:41 kasksız erkek; 00:45 3. astronot; 02:40 çift Dünya/geçit; 03:10 mutlu bakışma | 00:15 donukluk; 01:39 mekanik el; 03:10 sahte gülümseme | 00:58 çift ses; 01:19 "...for years" boğuk | 00:00 & 02:20 vakumda ses; 00:58 çift ses; 01:19 müzik bastırıyor; 01:47 ani müzik kesilmesi | 00:15-00:44, 01:05-01:18 | 02:56 vurucu ve buruk, 03:10 duyguyu bozuyor → Kurguyu değiştir / sesi düzelt / çekimi yeniden üret |
| 2026-10-22 | B1 (Simülasyon) | THE_PRICE_OF_HOME (2) | İki astronot kristalle geçidi açıp Dünya'ya döndü, kadın hafızasını kaybetti | Geçidi açıp Dünya'ya dönmek | Birinin hafızasını feda etmesi | Eve döndüler ama kadın unuttu; son gülümseme belirsiz | 00:58 tekrarlandı; 01:19 müzikten anlaşılmadı | 00:15-00:44 sessiz bekleyiş; 00:41 kask kaybı; 02:40 geçit konumu; 03:10 mutlu son | 00:35-00:44 | Buruk |

## KARARLAR

| Tarih | Konu | Karar | Gerekçe |
|---|---|---|---|
| 16.10.2026 | Plan yerleşimi | F1-F4 kapıları aşıldı | Sahip planı birebir uygulandı. |
| 16.10.2026 | Referans sayfaları | 7 sayfa | 10.10.2026 kuralı: özne başına tek sayfa. R07 aktif geçit, 4.ISTASYON'un paneli yapıldı. |
| 16.10.2026 | Replik modeli | Model sesi kapalı (sesler kurguda) | Plandaki "bütün konuşmalar kurguda eklenir" yönlendirmesi korundu. |
| 16.10.2026 | QA Değerlendirmesi | Kurgu ve ses revizyonu öncelikli | Ham klip sesleri tamamen kısılacak; planlanan replikler ve iç sesler kaydedilip eklenecek; C02 başına `"11 DAKİKA ÖNCE"` kartı konulacak. |
| 16.10.2026 | Prompt İyileştirmeleri | Sahibin onayına sunuldu | 15 yüz çekimine "mouth closed" eklenecek, zihinsel niyet fiilleri somut bakışa çevrilecek, C08/C17/C24 kıyafet ve yön kısıtları netleştirilecek. |
