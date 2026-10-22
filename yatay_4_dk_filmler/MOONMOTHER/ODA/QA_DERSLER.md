# 📝 MOONMOTHER — QA Dersleri (`moonmother.mp4`)

> **Tarih:** 19.10.2026 · **Yazan:** Fable (alt ajan yok)
> **Kaynak:** `ODA/HAM_QA_RAPORU.md` (dört rapor)
> **Kural ④:** Bunlar bu filmin dersleridir, hat kuralı değildir. İki filmde tekrar edenler en altta, sahibe soru olarak durur.
> **Çekim numarası:** QA'daki "Cxx" kesme sırasıdır. Süreklilik #22'ye göre atlayış çekimi (plan C13) kurguda yok. Bu yüzden QA C13–C23 = plan C14–C24.

## Tutanlar

| # | Ne | Kanıt |
|:--:|---|---|
| T1 | Hikâyenin omurgası okundu: koruyucu, yavru, dev anne, kavuşma, birlikte uçuş | Anlatım 1-6 · B1 1-4 |
| T2 | **Akrabalık okundu** (F3'ten beri açık ÖLÜMCÜL): dev yaratık yavrunun annesi | Anlatım 2: "göz altındaki üç ışık noktasının ve kanat yapısının birebir aynı olmasından" · B1 2 |
| T3 | Son duygusu geçti | Anlatım 8 · İzleme 8 · B1 8: "huzurlu" |
| T4 | Açılış tuttu: göz açılıyor, yavrunun üç ışığı görünüyor, dev göz aynı üç ışıkla cevap veriyor | Anlatım 00:00 · 00:10 · 00:40 |

⚠️ T2 kesin değil:
- videonun sonunda "MOONMOTHER" başlık kartı var ve dosya adı film adını taşıyor;
- çağrı-cevap ses kanalı (FILM §6) henüz filmde yok.

Temiz ölçüm için gereken iki şey:
- başlık kartı çıkarılmış, nötr adlı bir anlatım koşusu;
- gerçek izleyici.

## Dersler

| # | Ne oldu | Kanıt (ham rapor) | Neden | Ders |
|:--:|---|---|---|---|
| D1 | **Ses her kesmede kopuyor**. Ayrıca görüntüyle uyuşmayan sesler var: yavrunun planında yetişkin insan nefesi, yaratık çağrısına karışan inilti, mekanik tıkırtılar, açık havada kapalı oda nefesi. | Süreklilik S7 × 14 · Tarama #15 #19 #20 #22 #26 · Anlatım A4 #4 ve 7 · İzleme 5-6 · B1 5 | Her klip kendi model sesiyle kurgulandı. FILM §6: "Model sesi kullanılmaz (klip sesi atılır; ses kurguda)". | Model sesi kapalı filmde montajdan önce klip sesi kapatılır. Altına baştan sona tek ortam yatağı (Y1 kıyı · Y2 yüzgeç-hava), efekt ve müzik döşenir. Yeniden üretim gerekmez; düzeltme kurguda yapılır. |
| D2 | **Filmin seçimi görünmüyor**: Khev "nasıl indiği gösterilmeden" yavrunun yanında beliriyor. Atlayışın bedeli (sol kaval çatlağı) da hiçbir raporda geçmiyor. | Süreklilik #22 · Anlatım 5 (seçim listesinde atlayış yok) · Anlatım 1 (01:50, 02:00) | Kararın taşındığı çekim (plan C13, atlayış) kurguda yok. | Kararın ve bedelin taşındığı çekim kurgudan çıkarılmaz. Deneme bozuksa yeniden üretilir; boşluk kesmeyle kapatılmaz. |
| D3 | **Hedef görünmeden yürüyüş**: 01:10-01:30 sıkıcı bulundu. Amaç ancak 01:40'ta anlaşılıyor. Dev yaratık 01:10'da "tamamen yok olmuş", 02:20'de ise kıyının dibinde sudan çıkıyor. | İzleme 7 · B1 7 (01:15) · Anlatım 3 (01:40) · Süreklilik #15 · Anlatım 1 (02:20) · A1 #6 · B1 6 | Yürüyüşün hedefi olan anne bu çekimlerde ufukta görünmüyor. C16'da "ufukta uzak baş" yerine model anneyi yakına getirdi. | Bir karakter bir hedefe yürüyorsa hedef kadrajda görünür. C09 · C11 · C16'nın iki geçişli karesi (geçiş 2: ufukta uzak baş) üretimde atlanmamalı. Yürüyüşü anlamlı yapan o kare. |
| D4 | **Dev yaratığın ölçeği**: başta ay büyüklüğünde, 00:50'de "normal bir dev deniz canlısı" boyunda. | Süreklilik #10 · Anlatım A1 #1 · İzleme 2-3 · B1 6 | Her çekim onu farklı yere ve boya koyuyor (gökte bulut arkası ↔ denizin hemen üstü). Promptlarda sabit bir ölçek bağı yok. | Dev bir canlıya bütün çekimlerde aynı ölçek çapası verilir: neyin yanında ne kadar büyük olduğu tek cümleyle yazılır. |
| D5 | **Yavrunun görünümü**: 00:50'de mavi yarasa/ejderha kanadı, kanat zırhın içinden geçiyor. 02:06'da başında iki ışıklı anten çıkıyor, sonraki çekimde kayboluyor. 01:20'de tek ışık. | Süreklilik #11 #23 #17 · Tarama #6 #16 · Anlatım A1 #5 · İzleme 2-3 · B1 6 | Kimlik cümlesinde biçim tam kilitli değil. "winglike fins" gibi kelimeler kanat çağırıyor. | Küçük canlının kimliği kelimesi kelimesine sabit ve somut olur: yüzgeç, manta yüzgeci olarak tarif edilir, kanat kelimesi kullanılmaz. Ek çıkıntı (anten) çıkan çekim yeniden üretilir. |
| D6 | **Kıyı coğrafyası değişiyor**: 01:00'da alçak çakıllı kumsal ve tek kemer kalıntısı. 01:10'da yine yüksek uçurum. 02:20'de çöken iskele ucu yine sağlam. | Süreklilik #13 #15 #26 | Kamera kıyı seviyesine inince model başka bir kıyı kuruyor. Kırık uç bir sonraki çekime taşınmıyor. | Mekânın kalıcı hâli (yüksek teras, kopuk geçit ucu) her çekimde aynı cümleyle yazılır. Alçak kamerada da teras yüksekliği belirtilir. |
| D7 | **Sebep görünmüyor**: taş blok "kendi kendine" kırılıyor. Hiçbir kuvvet yokken yukarı kalkıyor, sonra düşüyor. | Anlatım A1 #3 · Tarama #12 · İzleme 1-3 · B1 6 | Dalga ile taşın düşüşü aynı hareket olarak okunmuyor; taş ters yöne (yukarı) hareket ediyor. | Sebep ve sonuç aynı çekimde, aynı nesne üzerinde ve doğru yönde görünür: dalga çarpar, taş aşağı eğilir, düşer. |
| D8 | **Kesmeye bırakılan temas izleyiciyi koparıyor**: kanada biniş görünmüyor, Khev "aniden kanadın üzerinde". Kucağa alma da çömelmiş → kucakta sıçraması olarak okunuyor. | Anlatım A1 #7 · Süreklilik #33 #24 · İzleme 3 ve karar "kurguyu değiştir" | Temas anları bilinçli olarak kesmeye alındı (sahip onaylı sapma 11). | Kesmeye bırakılan temas tek başına okunmayabiliyor. Ya ses köprüsüyle bağlanır (§6 S21 "taş→membran sürtmesi") ya da geçiş anı görüntüde kalır. |
| D9 | **Işığın anlamı okunmuyor**: yavrunun ışıkları parlıyor ama "neyi tetiklediği anlaşılmıyor". | Anlatım A1 #2 · Tarama #9 · İzleme 1 | Işığın seslendiği kişi (anne) o kadrajda yok (bkz. D3). | Bir sinyal ancak muhatabı kadrajda ya da hemen sonraki çekimde görünürse anlam taşır. |
| D10 | **Beden ve el hataları**: yürürken ayak kayıyor (00:02, 01:16, 01:21). El yavruya, kanada gömülüyor. Bıraktıktan sonra kollar robotik iniyor. | Tarama #1 #10 #11 · #3 #5 #14 #17 #23 #25 · İzleme 4 | Model hatası. Çoğu OLASI, saniyede 1 kare okumayla. | Şüpheli 2-3 saniye KARE MODU ile doğrulanmadan yeniden üretim kararı verilmez. |

**Kesmede değil, klip içinde tutan yerler** (Süreklilik "sorun bulunmayan"):
- Kesme 11: süzülüş → yerde yatan yavru.
- Kesme 17: göz planı → yüzgeç köprü.

Bakış ve yön zinciri bu iki kesmede kurulmuş. Diğer kesmeler için örnek bunlar.

## QA koşusunun kendisi

| # | Ne | Etkisi |
|:--:|---|---|
| Q1 | Dört rapor da 3:55'lik filmin tamamını tek parça okudu. Kural: Tarama ve Süreklilik için en çok 90 s. | 60-90 s'den sonra ayrıntı düşüyor. El ve kayma bulgularının çoğu OLASI. |
| Q2 | "Olması gerekenler" bloğunu ve kesme listesini model kendisi çıkardı. | Süzülen dev canlı ve yüzgecin suya değmemesi tasarımdı, ama hata sayıldı (Tarama #7 #8 #21). "Ne olmalı" bloğuna şunun gibi bir satır gerekir: "the two manta creatures naturally float and glide in the air". |
| Q3 | Çıktılar Türkçe. Dosya adı film adını taşıyor (`moonmother.mp4`). | Biçim ve Anlatım kuralı dışı; ağırlığı düşük. |
| Q4 | İzleme A "Gözlemsel Ön Doldurum", B1 "Simülasyon": ikisini de model yazdı. | Sahibin izlemesi ve dış izleyici yerine geçmez. İki kaynağın 01:15'te aynı yerde sıkılması bağımsız iki kişi değildir. |

## İki filmde tekrar edenler (kural ④, sahibe soru — kural yazılmadı)

1. **Hat dışı montajda klip sesi olduğu gibi kaldı.**
   - THE_FURNACE_GATE P4: klip sesi replik penceresine kısılmamış.
   - MOONMOTHER: model sesi kapalıyken bütün filmde model sesi var (D1).
   - BILINEN_TUZAKLAR'a ya da kurgu kontrolüne girsin mi?
2. **Gemini QA koşuları kural dışı.**
   - İkisinde de: tek parça >90 s, "ne olmalı" modelin, Türkçe çıktı, izleme simülasyon (FURNACE P4 ve bu film).
   - Her filme yapıştırmaya hazır tek bir "QA koşu kartı" yazılsın mı?
