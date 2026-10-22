# ✅ KABUL LİSTELERİ — faz kapıları (denetci ajanı okur, Fable karar verir)

> Her faz kapısında `denetci` iki şeye bakar: **süreç** (Ö maddeleri — her fazda aynı) ve
> **faza özel** maddeler. Her madde için: ✅ / ❌ + kanıt (dosya yolu, satır, alıntı).
> **M** işaretli maddeler mekaniktir: ❌ ise faz KAPANAMAZ ve Fable bunu aşamaz.
> Diğer maddeleri Fable gerekçe yazarak aşabilir; gerekçe `ODA/DURUM.md` → AŞILAN
> KAPILAR bölümüne yazılır ve yayın onayında sahibe gösterilir.

## Ö · Ortak süreç maddeleri (her faz)

- Ö1 **M** — Fazın zorunlu eleştirileri `ODA/`'da var (dosya adları: `F<faz>_<ajan>_<n>.md`).
- Ö2 **M** — Her eleştirinin `GİRDİ` satırı var ve "EKSİK" içermiyor.
- Ö3 — Her ÖLÜMCÜL ve CİDDİ bulguya yazarın cevabı var (KABUL / RED).
- Ö4 — Her KABUL yeni sürümde gerçekten uygulanmış (önceki sürümle fark — `git diff` ya da
  iki ODA sürümünün karşılaştırması). Uygulanmamış KABUL = ❌.
- Ö5 — RED gerekçeleri bulgunun kanıtına cevap veriyor ("katılmıyorum" gerekçe değildir).
- Ö6 — Açık ÖLÜMCÜL bulgu yok ya da tur tavanı doldu ve Fable'ın kararı gerekçesiyle yazılı.
- Ö7 **M** — `ODA/DURUM.md` güncel: faz, tur, ajan çağrı sayacı, sıradaki adım.
- Ö2b — (16.10.2026) Eleştiriler `ELESTIRI_PROTOKOLU` v2 biçiminde: her bulguda YER + DÜZELTME; listeli eleştirmen (devamlilik 8 · kurgucu 7) her soruyu cevaplamış; oran paydasıyla.
- Ö8 — (16.10.2026) Metin fazları (F1-F6, pilot hariç) 30 çağrıyı geçmedi; geçtiyse yalnız ÖLÜMCÜL'e tur açıldı (AGENTS §2 bütçe).
- Ö9 — (16.10.2026) FAZ ≥ 3p ise `medya.py durum` GERÇEK DURUM'u DURUM.md ile çelişmiyor (dosyalar ileride değil); kayıtsız deneme yok.

## F1 · Hikâye odası

- F1.1 — Üç aday var; her birinde AMAÇ (ekranda bir iş) · ENGEL · KARAR · SONUÇ · BEDEL (sahne no) · BİTİŞ.
- F1.2 — dramaturg, yonetmen ve izleyici üç adayı da gördü (izleyici yalnız logline'ları).
- F1.3 — Seçilen adayda dramaturg'un H02 (bitmiyor), H04 (prosedür) ve H06 (amaç yok) bulgusu açık değil.
- F1.4 **M** — Sahibe üç aday + Fable'ın seçimi + gerekçesi gösterildi; sahibin cevabı `DURUM.md`'de.

## F2 · Tretman (+ diyalog)

- F2.1 — Sahne sahne olay dili; her sahne öncekinden doğuyor (seçim ya da başarısız deneme).
- F2.2 — izleyici tretmanı okudu: anladığı amaç ve son, planlananla aynı.
- F2.3 — Replikler (REPLIK varsayılan var):
  - model sesi ≤8 s, ağız kadrajda ≤5 s ve sayısız; yeni filmde Kaynak her satırda model sesi (diyalog kurguda eklenmez, 21.10.2026);
  - HUMAN/MACHINE kaydı;
  - görüneni anlatan replik yok;
  - diyalog alışveriş olarak kurulu (her alışveriş bilgi, ilişki ya da karar değiştiriyor);
  - konuşan başına konuşma ve ses profili var;
  - replik sayısı bantta ya da gerekçeli.
- F2.4 — ses-tasarimcisi her repliğin nereden duyulduğunu işaretledi (kadraj dışı / telsiz / makine / ağız kadrajda).

## F3 · Çekim listesi

- F3.1 **M** — `film_dogrula.py` çekim listesi bölümünde hata vermiyor (zorunlu sütunlar, her çekim 10 s, çekim sayısı = HEDEF_SURE/10, zihinsel fiil).
- F3.2 — Her çekim tek bir bilgi taşıyor; bilgisi olmayan çekim yok (H01).
- F3.3 — izleyici yalnız "ekranda görünen" sütununu okudu; anladığı her kritik bilgi planlananla eşleşiyor. Eşleşmeyenler revize edildi ya da gerekçeyle bırakıldı.
- F3.4 — teknik-danisman'ın ÖLÜMCÜL risk bulgusu açık değil (temas anı, vakum, okunacak ekran, kask).
- F3.5 — Çekim sayısı × 10 s = HEDEF_SURE; son çekim bir sonuç gösteriyor (H02).
- F3.6 **M** — `GEREKEN REFERANSLAR` numaralı (`<No>.<AD>`), §3 tablosunda `No` sütunu ve dosya adı `<No>.<AD>_v1.png`; §4 Referans sütunu aynı numarayı taşıyor; **özne başına tek satır**, açılar/yüz/durumlar o satırın panel listesinde (sahip kararı 10.10.2026).
- F3.7 — (12.10.2026) §4 AÇILIŞ tablosu dolu (C01-C03: sorun · insan · replik/yazı · kapak bağı · sesi kapalı okunur mu); C01 ilk karede hareket hâlinde bir sorun, insan en geç C02; sapma gerekçeli (`ILK_30_SANIYE_KILAVUZU.md` §2).
- F3.8 — (16.10.2026) kurgucu çekim listesini kurgu gözüyle okudu (7 soru: kesmenin iki yanı · mekân · tepki · 10 s hareketi · yedek yol · replik yerleşimi · açılış/bitiş); ÖLÜMCÜL açık değil.
- F3.9 — (16.10.2026) `DURUM.md` `PILOT` satırında 1-3 pilot çekimi ve tek satır gerekçe (en riskli an · açılış · kimlik/konuşma) ya da sahibin "pilot yok" kararı.

## F3b · Sahneleme (faz 3, ADIM sahneleme)

- F3b.0 — (16.10.2026) Adım yalnız zincir açıkken ajanla koştu (ZİNCİR ADAYI + araç başlangıç/bitiş karesi alıyor + SMOKE zincir sonucu var);
  değilse `SAHNELEME.md` §5'te "zincir yok — gerekçe" satırı var, ajan çağrılmadı ve aşağıdaki maddeler atlanır.

- F3b.1 **M** — `film_dogrula.py --bolum cekim sahneleme` hata vermiyor:
  - her zincirli çekimin SAHNELEME karşılığı;
  - ≤4 halka;
  - halka sonu = sonraki başı;
  - anahtar kare tarifleri;
  - süre ≤ KLIP_SURESI;
  - replik dikişi aşmıyor;
  - delta satırları.
- F3b.2 — Her zincirin "neden zincir" gerekçesi kesintisizliğin ne anlattığını söylüyor; her halka yeni bir bilgi taşıyor (H01).
- F3b.3 — teknik-danisman'ın delta/morf ÖLÜMCÜL bulgusu açık değil.
- F3b.4 — mekan-haritacisi her halkanın mesafe/süre ve 180° denetimini yaptı; ÖLÜMCÜL açık değil.
- F3b.5 — izleyici anahtar kare tariflerinden akışı anlattı; zincirin taşıması gereken bilgi tuttu.
- F3b.6 — Zincir yoksa: §5'te bütün çekimler gerekçesiyle "zincir dışı".

## F3p · Pilot (16.10.2026 · faz 3, ADIM pilot)

- F3p.1 **M** — `film_dogrula.py --bolum cekim pilot` 0 hata: PILOT.md 1-3 çekim, hepsi çekim listesinde, çekim promptunun bütün kontrolleri.
- F3p.2 — `## KİMLİK CÜMLELERİ` §3'e birebir kopyalandı; DERS uyarılarının her satırı cevaplı.
- F3p.3 **M** — `medya.py durum`: her pilot çekiminin en az bir denemesi `ham/`'da ve DENEMELER'de kayıtlı (`medya.py al`).
- F3p.4 — Sahibin işareti her pilot denemesinde var (İŞARETLEME); devamlilik (kare) ve teknik-danisman (pilot) çıktıları ODA'da.
- F3p.5 — `ODA/F3p_pilot_karar.md`: her çekim için soru · istenen · gelen (kare kanıtı) · doğduğu yer · F5 notu · karar (GEÇTİ · PROMPT DEĞİŞİR · ÇEKİM DEĞİŞİR · REFERANS DEĞİŞİR).
- F3p.6 — Pilot notu F5 görev metnine girdi; hat kuralına çevrilmedi (AGENTS §1 ④).

## F4 · Ses + müzik planı

- F4.1 — Ses katmanları sahne başına ≤4; vakum dış planları ↔ iç hacim ayrımı yazılı.
- F4.2 — Replik kayıt listesi var: metin · ses profili · ton · hedef süre · filtre.
- F4.5 — Efekt listesi her çekimi kapsıyor (sessiz çekim gerekçeli); her satırda kaynak + nereden (arama terimi ya da İngilizce efekt promptu); sahne başına ortam yatağı.
- F4.3 — Müzik varsa: okuma cümlesi · en az bir müziksiz an · vuruş/susma noktaları · tempo kesme noktalarına bağlı.
- F4.4 — (21.10.2026) Yeni filmde her replik model sesi (künye `DIYALOG model sesi`; replik video promptunda birebir, klip sesi yalnız replik için `klip_sesi`, yatak planda). Eski filmde: model sesinin kullanılmayacağı yazılı; istisnalar §5 Kaynak sütununda: **ağız kadrajda** (≤5 s, sesi klipten) ya da **model sesi** (12.10.2026: replik video promptunda birebir, Omni konuşur; klip sesi yalnız replik için `klip_sesi`, yatak planda; kurgu kaydı yedek).
- F4.6 — §6 ORTAM YATAĞI tablosu: mekân başına TEK kesintisiz yatak (kapsadığı çekimler, İngilizce üretim/arama cümlesi, seviye, dosya); GEÇİŞ tablosu her kesme için tür taslağı + ses köprüsü (`GECIS_VE_SES_SUREKLILIGI.md` §2). Model sesi AÇIK filmde mekân başına ortam ses cümlesi (§3 ORTAM SESİ).
- F4.7 **M** — MUZIK var ise §7 `### MÜZİK PROMPTU` bloğu dolu (İngilizce, ≥200 karakter): `film_dogrula.py --bolum muzik` 0 hata (F4 taslak, F8 kesin).
- F4.8 — (12.10.2026) İlk 2 s insan sesi yok, açılış efekt/nefes/ortamla; müzik C01'de girmiyor ya da çok düşük zemin; C01'de en çok bir kısa replik (`ILK_30_SANIYE_KILAVUZU.md` §4-§5).

## F5 · Promptlar

- F5.1 **M** — `film_dogrula.py` prompt bölümünde hata vermiyor:
  - meta etiket ve sıra numarası yok;
  - başka çekime atıf, film geneli ifade, konuşma tarifi yok;
  - "insan yok" deyip kişiye gönderme yok;
  - her blok ≤4.300 karakter; her çekimin promptu var;
  - **referans anahtarı** (10.10.2026): EKLE/KAYNAK'taki her `ref/<No>.<AD>` görsel promptta `Reference <No>` olarak adlandırılmış, fazlası yok, numara-ad §3 ile aynı;
  - **10 s planı** (10.10.2026): her video promptunda 2-4 vuruş `a-b s`, 0'da başlar, 10'da biter, boşluksuz, vuruş ≥2 s.
- F5.2 — devamlilik'in ÖLÜMCÜL bulgusu açık değil: kimlik cümlesi birebir, dünya/ışık cümlesi, taraf, sayı, görsel ↔ video başlangıç durumu, tutan ve bağlantı.
- F5.3 — teknik-danisman risk sütunu dolu çekimlere baktı.
- F5.4 **M** — Flow iş emri var: her çekim için dosya adı · mod · eklenecek referans/kare (referanslar numaralı dosya adıyla, yükleme sırasında).
- F5.6 — devamlilik baktı: aynı numara her promptta aynı rolü taşıyor; vuruş iskeleti çekimden çekime aynı değil; son vuruş donmuyor.
- F5.7 — Her öznenin **tek referans sayfası** promptu var; çekimlerin istediği her açı ve durum sayfada panel; anahtar cümle gereken paneli adlandırıyor; panel üstünde yazı/etiket istenmiyor (sahip kararı 10.10.2026).
- F5.8 — devamlilik baktı (12.10.2026, `GECIS_VE_SES_SUREKLILIGI.md` §1): §3 ORTAK GÖRÜNÜM cümlesi her görsel ve video promptunda birebir; mekân ışık cümlesi birebir; model sesi AÇIK filmde mekân başına ORTAM SESİ cümlesi birebir; ilk vuruş hareketle başlıyor; ardışık aynı-mekân çekimlerinde ölçek ya da açı farkı var.
- F5.9 **M** — Model sesi repliği olan her çekimin Video promptu repliği birebir taşıyor (`film_dogrula.py` prompt bölümü); alıcıdan gelen ses için kadrajdaki kişinin ağzı kapalı yazılı.
- F5.10 — (12.10.2026) C01-C03 promptlarında görüntüde yazı ve logo yok; kalabalık, hızlı kamera ve karmaşık el-nesne teması yok; şeffaf vizörde yüz yakın planı varsa risk sütununda yazılı (teknik-danisman; `ILK_30_SANIYE_KILAVUZU.md` §6).
- F5.11 — (16.10.2026) G01 kalan gruplardan **önce** yazıldı ve eleştirildi; kalan grupların görev metni G01'i örnek grup olarak verdi.
  `film_dogrula` her `⚠️ DERS Yn` satırı ya düzeltildi ya `ODA/F5_uyari_cevaplari.md`'de (ya da grup dosyasının `## 8 SORU` tablosunda) gerekçeli.
- F5.12 — (16.10.2026) devamlilik 8 soruluk tabloyu her çekim için doldurdu (yokluk da bulgu); G01'deki bir kilit başka grupta düşmüşse bulgu var.
- F5.5 **M** — Zincir varsa:
  - her anahtar karenin görsel promptu ve iş emri satırı var;
  - zincirli çekimin EKLE satırı başlangıç + bitiş karesini taşıyor;
  - promptta zincir dili ("previous clip / last frame …") yok.

## F6 · Kapak konsepti

- F6.1 — (12.10.2026 güncellendi) 2-3 aday, her biri A'dan tek değişkenle ayrışıyor; an plandaki bir çekimden. Eski metin: "A/B tek değişkenle ayrışıyor".
- F6.2 — izleyici adayların görünen tarifini okudu: tek ilişkiyi okudu (F9'da 168×94 ve 120×68 kopyalarla).
- F6.3 — (12.10.2026 güncellendi) Vaadin dünyası (kapaktaki mekân · tehlike · ışık) C01'de; kapak anı ya da bir parçası ilk 30 saniyede, tercihen C03'te; kapak anı sonda kalıyorsa gerekçe yazılı (yayin denetimi; `ILK_30_SANIYE_KILAVUZU.md` §3). Eski metin: "filmin ilk %25-40'ında".
- F6.4 — (12.10.2026) `uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md`: 2-3 aday, her biri A'dan tek değişkenle; ≤ 3 kişi ya da ana nesne; kapak yazısı 0-3 kelime, film adı yok; vaat sınırı satırı (kapaktaki her varlık → çekim); yükleme sırası A ilk.

## F7 · Üretim

- F7.1 **M** — Referans kareleri `FILM.md` §2'de dosya adı + SHA-256 + onay satırıyla.
- F7.2 — devamlilik başlangıç karelerini görsel olarak karşılaştırdı (kask, giysi, yüz, eşya).
- F7.3 — Kareli animatik izleyiciye gösterildi; kopma noktaları not edildi.
- F7.4 — Sahibin deneme işaretlemesi `NOTLAR.md`'de; reddedilen her denemenin "doğduğu yer" yazılı.
- F7.8 **M** — (16.10.2026) `medya.py durum`: `ham/`'daki her deneme NOTLAR DENEMELER'de kayıtlı (prompt `p:sha8` + girdi); adı kurala uymayan dosya yok.
- F7.5 — Aynı sebeple iki kez bozulan çekim üçüncü kez aynı promptla gönderilmedi (bütçe kuralı).
- F7.7 — (12.10.2026) C01-C03 ilk üretilenler arasında; kare kapısında filigran, logo, yazı, el kaynaşması, yüz bozulması ve kimlik kayması arandı; biri olan çekim açılışta kullanılmadı (`ILK_30_SANIYE_KILAVUZU.md` §6).
- F7.6 — Zincir varsa:
  - `SMOKE_TEST.md` zincir bölümü koşulmuş (sonuç tablosu dolu);
  - zincir-bekcisi anahtar kareleri (mod 1) ve dikişleri (mod 2) denetledi;
  - her dikişin kararı `NOTLAR.md`'de.

## F8 · Seçim + kurgu

- F8.1 **M** — `kurgu.py kontrol` 0 hata.
- F8.10 — (16.10.2026) Montaj hat dışında yapıldıysa `medya.py bol` koştu, NOTLAR MONTAJ EŞLEMESİ dolu, QA bulguları plan numarasına çevrilmiş; timeline montajdan geri kuruldu.
- F8.2 — Seçilen her aralık sahibin "kullanılabilir" işaretlediği bir denemeden.
- F8.3 — izleyici kare sayfasından filmi anlattı; dramaturg bitişi doğruladı (H02).
- F8.4 — Müzik varsa: final Flow Music promptu gerçek kesme noktalarıyla yazıldı.
- F8.5 **M** — `kurgu.py yukseklik <final>`: −14 ±1 LUFS · ≤ −1 dBTP · 48 kHz.
- F8.6 — SÜREKLİLİK taraması taslağın bütün kesmelerinde koştu; SURE/LIKELY bulguların her biri `NOTLAR.md`'de kararlı (düzeltildi · kabul · yanlış alarm).
- F8.7 **M** — `timeline.json` (12.10.2026): her kesmenin geçişi `gecis` ile belli (kesme varsayılan; karışım ≤ kesmelerin ¼'ü, karartma ≤ 2; zincir içinde yalnız kesme), mekân yatakları `yataklar`da klipleri aşıyor, model sesi replik taşıyan parçalar `klip_sesi: true`; `kurgu.py kontrol` 0 hata, toplam süre geçiş kısalmalarıyla yazılı.
- F8.8 — Her kesmede `kareler.py dikis` koştu; jump cut ve renk sıçraması bayrakları §6 GEÇİŞ tablosunda kararlı (geçiş türü · renk eşle · yeniden üret); FILM.md §6 GEÇİŞ tablosu timeline ile aynı.
- F8.9 — (12.10.2026) İlk 30 s'de logo, siyah ekran ve karartmadan açılma yok; başlık varsa C03'ün son 2-3 s'sinde yazı katmanı; İngilizce altyazı dosyası replik metninden hazır (≤42 kr/satır, ≤2 satır, hedef ≤17 kr/s); ekran yazısı ≤4 kelime (`ILK_30_SANIYE_KILAVUZU.md` §2, §4).

## F9 · Paket + yayın onayı

- F9.1 **M** — İzleme Formu A (sahip) + en az 2 dış izleyici (B) `NOTLAR.md`'de.
- F9.2 — Gemini anlatım testi koştu; tutmayan bilgiler ve yanlış duyulan replikler not edildi.
- F9.3 — (12.10.2026 güncellendi) Final kapak aynı referanslarla ayrı kompozisyon ya da gerçek kareden düzenleme; kapaktaki her varlığın filmdeki saniyesi yazılı; `kareler.py kapak` her adayda koştu, 1280×720 uyarısı yok, bayraklar kararlı; 168×94 ve 120×68 kopyalar izleyiciye gösterildi (`uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §4, §7). Eski metin: "Final kapak gerçek bir kareden; 160×90 hâli izleyiciye gösterildi."
- F9.4 **M** — `film_dogrula.py --bolum yayin` 0 hata: `YAYIN_PAKETI.md` tamamen İngilizce, başlık sayımı doğru, kanal sabit bloğu birebir, tam 3 hashtag, etiket ≤500.
- F9.6 — Bilim cümleleri doğrulandı ya da "iddia değil" işaretli; vaat denetimi (§8) her vaadin filmdeki saniyesini veriyor.
- F9.7 — (12.10.2026) `IZLEYICI_VERISI.md` deney defterine filmin satırı açıldı: test edilen tek açılış değişkeni + H1/H2/H3 (`ILK_30_SANIYE_KILAVUZU.md` §8); Giriş oranı F10'da doldurulur.
- F9.8 — (12.10.2026) Başlık seçeneklerinde en az bir merak cümlesi (`<merak> | <AD>`) ve bir QUIET; kanca ilk ~45 karakterde; seri numarası yok; Test & Compare'e ilk yüklenecek seçenek işaretli (`uretim_hatti/KAPAK_VE_BASLIK_KILAVUZU.md` §5, §8).
- F9.5 **M** — `DURUM.md` → AŞILAN KAPILAR sahibe gösterildi.
