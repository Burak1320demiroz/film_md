# 🧠 THE_FALSE_EARTH — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     SAHİP VERDİ — tretman ve öneri metni 00_ON_PLAN/01_SAHIP_TRETMANI.md'de
   birebir duruyor. AI seçimi koşmadı; gerekçe satırı bu yüzden boş DEĞİL, yok.
② FORMAT:   yatay 32 dk → kart §2.9 · bölüm sayısı 16 · QA birimi 8 PART + TAM FİLM
③ SAHNE:    192 KLİP (çok klipli sahne rejiminde kartın "N sahne"si N KLİPTİR)
            · 50 SAHNE · bant içi (sahne 2-6 klip, tek 6'lık S44 doruk)
            ⛔ Bandın dışına çıkılmadı; sapma gerekçesi gerekmiyor.
④ REFERANS PAKETİ: YAZILSIN (sahip kararı 23.09.2026) → KAPI 0
   §5b tablosu yine de dolduruldu: altı tetikleyicinin ALTISI da doğru.
⑤ HİKÂYE ONAYI: 00_HIKAYE_ONAYI.md ONAY 23.09.2026 · TUR 1/3 · SAPMA sekiz madde, onaylı
⑥ FİKİR TURU KAYDI — 0.7a KOŞMADI (K6 · sahip kararı 23.09.2026)
   GEREKÇE: hikâye sahibin kendi tretmanıdır ve iki tur dış değerlendirmeden geçmiştir.
   Fikir havuzu, hikâyesi olmayan filmler içindir; hazır ve sahibine ait bir hikâyeye
   üç aday üretmek onu başkasının hikâyesiyle yarıştırmak olurdu.
   GERİLİM CÜMLESİ:  Mira dokuz yıl önce kaybettiği kardeşini eve götürmek istiyor, ama
                     onu çağıran şey kardeşi değil Dünya'ya açılan kapıyı isteyen bir
                     tuzak, çünkü kardeşinin gemisi o kapıyı dokuz yıl önce yok etti.
   ENGEL TİPİ:       ilişki (yapının Mira'dan istediği şey) + ortam (kırk dakikalık yükselme)
   DUYGU ADI:        çift-duygu — kavuşma sevinci ile tanımanın dehşeti AYNI karede (K048)
   ÜÇ YÖNTEM:        koşmadı (0.7a atlandı)
   DOYUM:            en yakın iki film THE_MIRROR_FAUNA (taklit eden canlı) ve
                     BENI_HATIRLAMA (kimlik · hatırlama). FARK: burada taklidin
                     KAYNAĞI gösteriliyor (arşiv, S23) ve taklidin SINIRI olay örgüsünü
                     çeviriyor — kopya çalışmadığı için yapı gerçeğini istiyor.
   ÖLDÜRÜLEN GÖZDE:  A'ya karşı üç argüman sohbette yazıldı (ortanın beklemesi ·
                     sahteliğin 8:00'de anlaşılması · finalin teknikleşmesi).
                     SONUÇ: A kaldı; üçü de P0/P2 ölçütlerine bağlandı, kapatılmış sayılmadı.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "32dk ilk filim icin planalrım şu şekilde başlamadan yeni-film akışına
        öncen bir planlama yapalım istiyorum klasörü hazırla"
        + iki uzun metin (öneri özeti ve tretman), 01_SAHIP_TRETMANI.md'de birebir
REPLİK: VAR → ayrı kapı zinciri açıldı: SES_VE_DIYALOG §1a-§2a + DIYALOG_SAHNESI +
        DIALOGUE_CRITIQUE_PROMPT (Kart P 2b) + ㉓ REPLİK ENVANTERİ
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**
Emsal: THE OPEN CIRCUIT'te *"fırtınalı"* ve *"patlamalı"* istekleri 610 Pa
Mars basıncında imkânsızdı; ikisi de yeniden tanımlandı, gerekçe yazıldı ve
biri filmin novum'u oldu.

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "ortalama 8 saniyelik planlarla yaklaşık 240 plan" | Hattın klibi sabit ve tam 10 s [D124]; 240 × 8 s değişken çekim süresi demektir ve kurgu KIRPMAZ, KLİP DÜŞÜRÜR [D100 · KART 11] | 192 klip × tam 10 s = 1920 s. Ritim klip sayısıyla değil, sahne içi kurulum değişimiyle kuruluyor | K1 · kurgu kapısı ±0 · `00_ON_PLAN/02_ON_PLAN.md` §1 |
| "Lena'nın durumu ağır, basınç ve yükseklik değişimine dayanamaz" | Kontrollü kabini olan bir podda basınç gerekçesi tek başına yetmiyordu (eleştiri 1 · madde 3) | Pod tek koltuklu; koltuğun arkasındaki kurtarma yatağı BASINÇSIZ. Lena yalnız kurtarma torbasında taşınabilir, torbada 20 dakika hava var | ON_PLAN §2.3 · K013 · K024 · K049-K053 |
| "Yapı yalnızca edindiği bilgiyi bilir" | Kural finalde kendi geçmişiyle çelişiyordu: dokuz yıllık bir yapı hiç mi kopya denemedi? (eleştiri 2 · madde 1) | Yapı düşünür ve plan kurar; sınırı ÜRETMEKTE. Çekirdeğin biçimini kopyalayabiliyor ama geçidi açan EŞLEME görünmez — kopyaları çalışmıyor, bu yüzden gerçeğini istiyor | ON_PLAN §2.2 · K094 · K127 → K180 |
| "Gezegen Dünya'ya benziyor" (atmosfer, yağmur, okyanus) | `KILAVUZ_REHBERI` §3.3 DÜNYA ATMOSFERİ kartı RAFTA ve **referans filmi YOK** — kartın fizik satırları duruyor ama doğrulanabilir örneği yok | Kart kullanılıyor; kartın kendi cümlesi bunu öngörüyor: *"Dünya benzeri atmosferi olan bir GEZEGEN konsepti bu fiziği kullanır… bu ortamda film yazılırsa ilk film yeni referans olur."* THE_FALSE_EARTH §3.3'ün ilk referansı olacak | §2 kart satırı · KILAVUZ §3.3 |
| "Ton: korku mekânın davranışından doğar" | `KILAVUZ_REHBERI` §4.1 bilimkurgu kartı TON'u **"Huşu ve varoluşsal huzur (Overview Effect). Korku değil."** diye kilitliyor | Sapma kabul edildi: bu film psikolojik gerilim. Huşu kanalı KORUNUYOR (S33 kabuk · S50 küreler) ve korku yalnız mekânın davranışından geliyor — jump scare, canavar saldırısı, yara/kan yok | D74 · PLAN'a tek satır |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 32 dk → §2.9 kartı (192 klip · 16 bölüm · 8 PART + TAM FİLM · ±0)
               + §2.0b ÇOK KLİPLİ SAHNE (rejimin ilk filmi)
ORTAM:         İKİ KART BİRDEN, ve asla aynı kadrajda değil:
               §3.3 DÜNYA ATMOSFERİ (gezegen yüzeyi · S06-S10 · S26-S34)
                    → toz hızlı çöker ve oturur · dolgu ışığı VAR · ses normal yayılır ·
                      nefes soğukta görünür buhar · ⚠️ referans filmi YOK, bu ilk
               §3.1 VAKUM (uzay · S05 · S44-S46 · S50)
                    → gölge mutlak siyah · dolgu YOK · dışarıda ses YOK · küresel lens
               §3.10 BASINÇLI İÇ HACİM (gemi içi · S04 · S35-S43 · S47-S49)
                    → hava taşır, fan zemini · gölge yumuşak · metin riski EN YÜKSEK
               ⛔ Üç kartın `PHYSICS:` ve `AUDIO:` cümleleri ADI ve SAYISIYLA yazılır
                  ve sahne içinde BİREBİR kopyalanır [D200 · ㉜⑥]
TÜR:           bilimkurgu · dal: kozmik gizem + psikolojik gerilim → §4.1
               ⚠️ §4.1 TON satırından SAPMA (yukarıda, D74)
               ⚠️ §4.1 "ikinci figür BÜTÇELİ" — bütçe §7'de (iki kart + istek çaprazı)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124] — üretim defterinin ilk satırı.
               Yazım tam 10,000 s varsayar; ölçüm sapar ve kurgu birimi değişirse
               PLAN'ın süre satırı yeniden hesaplanır, klip sayısı DEĞİŞMEZ.
SAHNE SAYISI:  50 sahne · 192 klip     RUNTIME: 1920 s = 32:00 (hook 192'nin içinde)
BÖLÜM SAYISI:  16 (formattan gelir — §2.0)
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM TİPİ:          İLİŞKİ (✅ üçüncü tercih · §1 tablosu)
                     ⛔ GEREKÇE ZORUNLU çünkü birinci/ikinci tercih değil:
                     bu filmin kuralı bir fizik yasası değil, bir varlığın bir
                     insandan istediği şeydir. Depoda İLİŞKİ tipiyle yazılmış film
                     YOK (`06_HIKAYE_HATTI` §1.2: 13 filmin 12'si "fiziksel yasa");
                     tip 02.09.2026'da sahip kararıyla açıldı ve hiç kullanılmadı.
NOVUM:               Yapı gördüğü her şeyi yeniden kurabiliyor, görmediği hiçbir şeyi
                     kuramıyor — ve geçidi açan eşleme görünmez bir iç durumdur.
NOVUM TAŞIYICISI:    aile fotoğrafındaki lamba × Mira'nın fotoğrafı odadaki lambanın
                     yanına tutması → fotoğraftaki FLAŞ PARLAMASI, odadaki lambanın
                     camında MADDİ BİR LEKE olarak kopyalanmıştır
                     (İLİŞKİ tipinin ikinci jesti: Lena aynı lambayı yakar ve
                      lekeyi görmez — göremez, çünkü onu kendisi üretmiştir)
① TEK KARE:          ✅ "odadaki lambanın camının üstünde, cama işlenmiş beyaz bir
                     parlama lekesi" — K071. Taşıyıcı nesnenin ADI cümlede [D157]
② KİNETİK BAĞIMSIZLIK: ✅ Mira fotoğrafı kaldırır, lambanın yanına tutar, elini geri
                     çeker. Replik, dış ses ve ekran metni olmadan okunur.
                     ⚠️ Kuralın ÖNCEKİ iki kanıtı da sözsüz: K017 (yansıma geç döner)
                     ve K029 (cephe bıçak gibi biter). ECHO yalnız ikisini adlandırır.
③ BAŞLIK ŞEMASI:     ✅ "THE FALSE EARTH" — 3 kelime; izleyiciye nereye bakacağını
                     söylüyor: gezegene. Kapak metni "THAT ISN'T EARTH"
KURAL TEKRARI (§5):  KURULUM K017 (su) → DOĞRULAMA K029 (dükkân) → K071 (lamba) →
                     SONUÇ K094 (kopyalar çalışmıyor) → K180 (kabuktaki halkalar)
                     ≥3 sahne ✅ · ≥2 farklı nesne ✅ (su · cephe · lamba · halka)
İHLAL SAYISI (§3):   1 — ve ikincisi yok. Maya kabuğu tanıdık: uzay giysisi, pod,
                     gemi, bir çocukluk odası. Yenilik yalnız yapının kuralında.
⛔ Üçü de ✅ → KONSEPT GEÇTİ.
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — FEDAKÂRLIK   (§3 sekizlisinden · §4'e göre YATAY/süreç teması ✅)
▸ tanım cümlesi — "Başta her şeyi kaydettiren kişi, sonunda kendi kaydını
                   kimsenin duymayabileceği bir yere bırakır."
                   ⛔ TAKAS kalıbı DEĞİL: cümle bir ilk hâl ile bir son hâli
                   karşılaştırıyor, "X için Y feda edilir" demiyor [§3c]
▸ depoda kaç kez kullanıldı — 5 (sayac.sh · TEMA DAĞILIMI). §4'e uygun dört yatay
  temadan (Kimlik · Zaman · Fedakârlık · İnsan-Makine) son uzun-form koşusunda
  KULLANILMAYAN tek tema: Kimlik 22.09 THE_SLOW_RAIN ve BENI_HATIRLAMA ·
  Zaman 15.09 KRONOS · İnsan-Makine 18.09 SUSMAYAN_NOBETCI · Fedakârlık —
▸ motif kanalları — NESNE: kayıt ("Kaydet" K012 → K019 → K031 → kırılma K047 →
                           modül K084 → onarım K184 → işaretçi K188)
                    KİNESİK: eldivenin cama konması (K009 çekirdek camı →
                           K083 kabin kapağı → K160 halka camı → K187 ekran)
                    IŞIK: tek yanan pencere (K004 → K036 → K119 → K191)
                    SES: annenin lambası, kaydın içinden (K011 → K159 → K189)
▸ motife döndüğü sahneler — S04 · S22 · S41 · S42 · S47 · S48
  ⭐ B3 ÇAPRAZ OKUMASI: bedelli seçimin yaşandığı sahne bu listede mi? EVET —
  S42 motifin KIRILDIĞI sahnedir (el camdan kalkar ve mandala gider, K164) ve
  S47 bedelin görüldüğü sahnedir (dokunulan cam artık karanlık, K181)
```

### ⚠️ K7 — TEMA TEKRARI, YAPISAL ÖLÇÜM (sahip kararı: bilinçli istisna)

```
ÖLÇÜM (PLAN dosyalarından, 23.09.2026 · bedel satırları okundu):
  THE_SLOW_RAIN    BEDEL: kanatlar kesilir, kızağa çevrilir          → vazgeçerek koruma
  THE_STOLEN_SKY   BEDEL: Mara saldırı fırsatından VAZGEÇER          → vazgeçerek koruma
  THE_STILL_POINT  BEDEL: tek kaçış aracını bırakır                   → vazgeçerek koruma
  THE_FALSE_EARTH  BEDEL: dönüş çekirdeğini kendi eliyle yok eder    → DÖRDÜNCÜ

⭐ DÜZELTME — ön plandaki tespit bir noktada YANLIŞTI: THE_FALLING_WORLD'ün bedeli
  bu kalıba girmiyor ("Beyaz'ın sol kolu işlevini kaybeder" — fiziksel kayıp,
  vazgeçme değil). Zincir yine de üç filmdir ve bu film dördüncü olur.

TEMA ETİKETİ TEKRAR DEĞİL: §3c moratoryumu TANIM CÜMLESİNİN kalıbını ölçer, bedel
  yapısını değil. Yukarıdaki tanım cümlesi takas kalıbında değil ve FEDAKÂRLIK
  etiketi son uzun-form koşusunda kullanılmadı.

SAHİP KARARI (23.09.2026): (a) BİLİNÇLİ İSTİSNA [D74].
GEREKÇE — PLAN'a tek satır olarak iner:
  Önceki üçünde vazgeçilen şey bir ARAÇTI (kanat · fırsat · araç) ve bedel tek
  sahnede ödendi. Burada vazgeçilen şey evin KENDİSİDİR ve bedel iki kez ödenir:
  S44'te dönüş yolu yok edilir, S49'da kurtarılma ihtimali REDDEDİLİR. İkinci ödeme
  bu kalıbın önceki üç filminde yok.
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa KİLİT TAVANI (≤ 20 ders kilidi) —
> malzeme azaltılmaz; dışarıda kalan kilitler PLAN `UYGULANMAYAN KİLİTLER`e gerekçeyle
> (14.09.2026, 02_RISK_KARTLARI §RİSK TOPLAMI).

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 SU / SIVI | ✅ | siyah okyanus S06 · ıslak sokak S07-S10 · camda yağmur S09 | Çıplak el ↔ sıvı teması SIFIR: Mira mühürlü, eldivenli. Suya dokunulan klip YOK; su yalnız yüzey ve yansıma | 🟡 |
| 2 CANLI | ✅ | yapı = insan dışı organizma/makine; siyah madde hareket ediyor | ANATOMY LOCK sayıyla: madde dallanır, uzuvlanmaz; yüz/göz/ağız YOK; yakın planda yalnız yüzey ve uç. `UZAYLI_VARLIK_TASARIM` havuzdan açılacak (adım 5) | 🔴 |
| 3 KASK / VİZÖR | ✅ | Mira film boyu kasklı | HELMET STATE SCHEDULE: kapalı K001-K192, açık 0 klip. Vizör biçim+sayı [D146] + referans paketi kask sayfası | 🟠 |
| 4 İKİNCİ FİGÜR | ✅ | HER filmde geçerli — ve bu filmde ikinci insan GERÇEKTEN var | HUMAN COUNT LOCK klip başına yazılır: 1 ya da 2, hangisi olduğu her promptta. İniş/kalkış klipleri (K013-K014 · K118-K120 · K133-K135) UZAKTAN, rampada kimse yok [D69] | 🔴 |
| 5 EKRAN / SAYAÇ / METİN | ✅ | ECHO ekranları · kol ekranı · arşiv · tarama · işaretçi | Sayaç metinle DEĞİL fizikle: geminin ışığının pencere kenarına göre yüksekliği (K061 · K096) ve duvardaki çizginin kalınlaşması. Ekranlar salt geometrik desen [D138] | 🔴 |
| 6 PARÇACIK / PATLAMA | ✅ | servis yükü patlar K172 · dağılan madde K175-K177 · sis S07 | Patlama SESSİZ ve vakumda: genişleyen tek bir kabuk, 0 alev, 0 duman, 0 kıvrım. Dağılma "kül gibi" değil SAYIYLA: parça sayısı ve düşüş yok (0 g) | 🟠 |
| 6b KATMANLI DÜNYA | ✅ | gemi → pod → okyanus → şehir → oda → duvar arkası → enkaz → kabuk → uzay | LAYER LIGHT SCHEDULE zorunlu: her sahnenin katmanı + o katmanın ışığı tek tabloda, irtifaya göre monotonik okunacak (adım 5) | 🔴 |
| 7 DİYALOG | ✅ | filmin taşıyıcılarından biri replik | DİYALOG MERDİVENİ: basamak 1-2 baskın (ECHO kadraj dışı · Lena'nın sesi duvardan/telsizden · VELA kaydı). Basamak 3 (ekranda tek replik) yalnız S11-S20 ve S27'de, PROB B koşulmadan üretilmez | 🔴 |
| 8 KAMERA | ✅ | her filmde | Klip içi fixed lockoff, 0 hareket. Sahneler ARASI ve sahne İÇİ kurulum değişimi zorunlu (ACI_YAYI §3 bandı) | 🟢 |
| 9 IŞIK MIKNATISI | ✅ | ⭐ **kadrajdaki tek baskın ışık yanan penceredir ve Mira ona doğru yürüyor** — kartın tarif ettiği durumun tam kendisi | DÖRT KANAL birden yazılacak (hedef-dilim+yön · omuz hattı · ışığa göre poz · yön negatifi). İKİ YENİLGİ KURALI: iki redden sonra kamera HEDEFE taşınır | 🔴 |
| 10 İNSANSIZ SAHNE | ✅ | ~30 klipte kadrajda insan yok | O kliplerin NEGATIVE bloğu tek pozitif `Style:` satırına iner; boş kadraj VARLIK olarak tarif edilir [D59] | 🟠 |
| 11 SAHNE İÇİ KESME | ✅ | rejimin kendisi: 50 sahnede 142 sahne içi kesme | SPEC'e üç sayım (SCENE 50 · SHOT 192 · CLIP 192) + "sahne içi kesmeler" listesi ② DEVAMLILIK'e. Kırpma bütçesi 0 (±0 kuralı) | 🟠 |
| 12 POLİTİKA YÜZEYİ | ✅ | ölüm · mühürlü kabin · gövde kesilmesi · kadın sesiyle ayartma · iki yüz | §6 politika satırı + hasat §3 tablosu; her önleme ÖNLEM/MALİYET/TELAFİ | 🔴 |
| 13 YAPI ÖLÇEĞİ | ✅ | ana gemi · kıta boyunda halkalar · kabuk levhaları · pod · VELA enkazı | ANATOMİ KARTI (modül/halka/levha sayısı film boyu sabit) + ÖLÇEK MERDİVENİ (S32→S33→S34 monotonik kesir) + ÖLÇEK ŞAHİDİ her yapı planında | 🔴 |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  SİYAH MADDENİN DAVRANIŞI — filmin tek insan dışı canlısı, 30'dan
                  fazla klipte kadrajda, ve "canlı" kategorisi bu depoda hiç 5'i geçmedi
POZİTİF BİÇİMİ:   Tek bir gövdeden çıkan, en çok ÜÇ dala ayrılan, kolun kalınlığında,
                  mat siyah, ıslak görünümlü, KATI bir yüzey. Uçları yuvarlak, kör.
                  İlerleme hızı: on saniyede bir el genişliği (yaklaşık 10 cm),
                  sabit hız, geri çekilme yok. Yüzeyde 0 akış, 0 dalgalanma,
                  0 damla, 0 parlama, 0 duman. Kadrajda aynı anda en çok 3 uç.
                  Kesildiğinde: hareket 1 saniyede durur, 2 saniyede matlaşır,
                  3. saniyede kenardan başlayarak ayrılır — sıvı gibi akmaz.
GÖZ KAPISI (SPEC): "dal sayısı ≤3 · uç sayısı ≤3 · ilerleme ≤1 el genişliği / 10 s ·
                   0 damla · 0 duman · 0 parlama · yüzey KATI, akmıyor"
```

⛔ **Sıfat yetmez.** THE OPEN CIRCUIT 1 numaralı riskini (KIVILCIM) adıyla ilan
etti ve yalnız sıfatla korudu — *"TEK, İNCE, DÜZ ve SÖNÜMLÜ"*. Aynı planda
sayıyla yazılan her şey tuttu. Ekrana **en az 0,5 s süren, dallanan bir şimşek**
geldi; her sahnenin NEGATIVE bloğunda *"no lightning bolt"* yazılıyken.
**Negatif cümle yasağı söyler, BİÇİMİ söylemez; model boşluğu doldurur.**

```
TETİKLENEN RİSK:  14 / 14
EŞİK:             5
⭐ EŞİĞİN ÜSTÜNDE: 14.09.2026 kuralı — MALZEME AZALTILMAZ, KİLİT TAVANI ≤20 uygulanır.
                  Uygulanan 20 kilit + gerekçeli 20 uygulanmayan kilit:
                  `01_QA_DERS_HASADI.md` §1 ve §1b; PLAN'a aynen taşınacak (㉕).
                  ⛔ KART 12 tavanın DIŞINDA — politika satırı her filmde zorunlu.
```

### 🪦 ÖN-OTOPSİ — "film çekildi ve izlenmedi, neden?" 🆕 21.09.2026 [`HIKAYE_FIKIR_TURU` §8]

> Konsept kapılarından ÖNCE, okuma bittikten SONRA. Beş arıza modu; yüksek × yüksek
> hücre ya önlem alır ya konsepti öldürür ve yukarıdaki risk kartı tablosuna kart olarak iner.

| arıza modu | olasılık | etki | önlem / öldür |
|---|:--:|:--:|---|
| kanal tezi | orta | yüksek | 32 dakika deponun en uzun filmi ve kanalda emsali yok. Önlem: PART masterları kendi başına izlenebilir birimler (her PART bir soruyla açılıp bir soruyla kapanıyor — S07\|S08 … S43\|S44 sınırları sahne sınırında) |
| politika / red | **yüksek** | **yüksek** | ⛔ YÜKSEK × YÜKSEK — kart olarak indi (KART 12). İki yüz × ~90 prompt, SINKING STAKE'in üretimi durduran profilinin aynısı. Önlem: kimlik özniteliği ≤3, yüz yalnız konu olduğu klipte, referans paketi KAPI 0. **P1 denemesi bu riski ilk 4 klipte ölçecek** |
| üretim tek-hata noktası | **yüksek** | **yüksek** | ⛔ YÜKSEK × YÜKSEK — kart olarak indi (KART 2 + KART 13). Siyah maddenin biçim kilidi ve halka/kabuk oranı metinle tutmuyor [D146 · D84]. Önlem: referans paketi (K4 ✅) + A5'in sayısal biçimi + **P3 denemesi** |
| tutundurma | orta | yüksek | İlk 10 s soru taşıyor (K001-K002), son 10 s adlandırılmış kare + döngü. ⚠️ Asıl risk 12:00-22:00 platosu (eleştiri itirazı 1). Önlem: **P0 ilk 10 dakikayı**, ⑫ HOOK tam-film koşusu ortayı ölçer |
| doyum | düşük | orta | En yakın iki film THE_MIRROR_FAUNA ve BENI_HATIRLAMA; ikisi de kısa ve ikisinde de taklidin KAYNAĞI gösterilmiyor. Fark yeterli |

```
KARAR: GO
   İki YÜKSEK × YÜKSEK hücre de ÖNLEM aldı ve ikisi de bir DENEMEYE bağlandı
   (P1 · P3). Denemeler 192 prompt yazılmadan koşacak (sahip kararı 23.09.2026),
   yani bu iki hücre yazımdan önce ölçülecek. Konsept öldürülmedi, revize de gerekmedi.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

> `REFERANS_PAKETI_KILAVUZU.md` §1 tablosu. **Altısı da tek tek ölçüldü.**
> (Soru ④ "YAZILSIN" ile cevaplandı; tablo yine de dolduruldu — hangi varlığın
> sayfayı hak ettiğini bu tablo söylüyor.)

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | Mira'nın giysisi ve kaskı — 192 klibin ~160'ında |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | siyah madde (S26 · S36 · S39-S40 · S45) · amber halka (S04 · S39-S44 · S47) |
| T3 | oranı sözle yazılamayan nesne | ✅ | ana gemi · pod · kıta boyunda halkalar (S33) · kabuk levhaları (S32) · VELA enkazı (S21-S22) |
| T4 | insan dışı canlı | ✅ | yapı — kaburgalar (S07 · S26 · S34) ve siyah madde |
| T5 | tekrar eden insan dışı olay | ✅ | maddenin bir gövdeyi sarması: S26 (gemi) · S39 (yuva) · S44 (kesilme) |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | Lena — İKİ sürüm: taklit (S11-S20 · S27) ve arşiv kaydı (S24 · S48) |

```
KARAR: YAZILIR (sahip kararı · K4 · 23.09.2026)
⛔ KAPI 0'dır: sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği
   hiçbir klip üretilmez [D168]. Üretim sırasının İLK halkası referans paketidir.
SAYFALAR (ilk liste · kesinleşmesi adım 9a): RK1 Mira kask+vizör · RK2 Mira giysi ·
   RK3 Lena (kasksız, iki sürüm) · RA ana gemi · RB pod · RC amber halka + mandal +
   ayırma kolu · RD siyah madde (uç · dal · kesik) · RE kaburga · RF halka/kabuk ölçek ·
   RG Lena'nın odası · RH VELA enkazı
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S22 · K083 — mühürlü kabin kapağı, camında dokuz yıllık kırağı;
                     Mira eldivenini kapağa koyuyor ve ölüm kesinleşiyor
NÖTR TARİFİ:         "A sealed inner hatch with a small round pane, the pane fully
                     opaque with nine years of frost crystals. A gloved hand rests
                     flat on the metal beside the pane. Nothing is visible through
                     the pane." — kadrajda beden YOK, yara YOK, yüz YOK.
                     Ölümün kanıtı kapak, kırağı ve basınç okumasıdır.
⛔ Sözlükten çıkan kelimeler: dead · body · corpse · remains · decay · frozen body ·
   skeletal — negatif blokta bile yazılmaz [SLOW STONE vakası]
```

**Üç satırlık anlam maliyeti — alınan her önlem için [POLİTİKA §4.3]:**

| önlem | maliyet | telafi |
|---|---|---|
| Lena'nın bedeni hiç gösterilmiyor (K082-K083) | Ölümün dolaysız görsel kanıtı gitti; izleyici "belki hâlâ oradadır" diyebilir | Kanıt üç kanala bölündü: mühürlü kapak (alet tepkisi) · dokuz yıllık kırağı (malzeme sonucu) · ECHO'nun basınç okuması (0 kPa, dokuz yıl). Üçü bir arada tek bedenden daha kesin |
| K102'de kask kilidi AÇILMIYOR, yalnız el dokunup çekiliyor | Ayartmanın en fiziksel hâli (kaskı çıkarmaya kalkışmak) gitti | Temassız gövde tepkisine taşındı: el kilide gider, iki saniye durur, geri döner ve fotoğrafı alır. Tereddüt kanalı [OYUNCULUK §3 ③] bunu daha okunur taşıyor |
| K171'de kesilen şey bir bedene değil bir GÖVDEYE ait | "Parçalanma" dehşeti azalır | Kütle-hız kanalına taşındı: kapak iner, gövde bir el kalınlığında kesilir, kesik uç 3 saniyede matlaşır. Ses kanalı da taşıyor (metal + kuru çatırtı) |
| Kalabalık yok — K119'da pencereler yanıyor, figür yok | "Binlerce izleyen göz" imgesi gitti | Işığa taşındı: pencereler aynı anda ve aynı sıcaklıkta yanıyor; tekilliğin yokluğu tehdidi büyütüyor. Kadrajda insan sayısı 1 kalıyor [KART 4] |

```
⛔ Milliyet · gerçek kurum · gerçek kişi adı: planın hiçbir yerinde YOK.
   VELA ve ECHO uydurma adlardır ve PROMPT GÖVDESİNE GİRMEZ [D34].
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Mira kayıp bir mürettebatı bulup gemisine geri götürecek — kurtarma pilotu
         olarak yaptığı iş bu; film başlamasa da VELA'nın son atış bölgesini
         tarıyor olacaktı (K005). ⛔ "anlamak/görmek/fark etmek" DEĞİL
ENGEL:   Kurtarmaya geldiği kişi dokuz yıl önce ölmüş; onu çağıran şey, kurtarma
         aracının kendisini (dönüş çekirdeğini) istiyor
BEDEL:   Dönüş çekirdeği · S44 (yok edilir) → kaybın GÖRÜLDÜĞÜ sahne S47
         (çekirdek bölmesi karanlık, ECHO: "Dünya'yla bağımız yok")
         ⭐ İKİNCİ ÖDEME: kurtarılma ihtimali · S49 (işaretçiye "Beni aramayın")
MUHATAP: ☑ ikinci insan — Lena (kadrajda S11-S20 · S27, kadraj dışı S30-S49)
         ☑ karakterin film başlamadan verdiği kendi kararı — dokuz yıl önce
           kardeşinin çağrısına yetişememesi (K114'te GERÇEK kayıtla geri geliyor)
         ⛔ İkisi birden işaretli ve ikisi de sahne taşıyor
AYRILIK: S13 · K047 — Mira, ECHO'nun "ses eşleşmesi tam" bulgusunu duyar ve
         ECHO'yu SUSTURUR. Kardeşiyle aynı fikirde olmadığı ilk an: Lena
         cümlenin doğru olduğunu söylüyor, Mira kanıtı kapatıyor.
         Farkı taşıyan kanal: TEMAS REDDİ değil, ÜÇÜNCÜ SESİ KESME
İSTEK ÇAPRAZI (`IKI_KISI` §3):
         Mira, Lena'dan şunu ister:  torbaya girmesini — odadan çıkmasını
         Lena, Mira'dan şunu ister:  kalmasını (K074 "Gitme" · K101 "Kalırsan
                                     yaşarım" · K158 "Kapıyı aç. Eve dön.")
         NESNE: önce KURTARMA TORBASI (S14-S16), sonra GEÇİT (S27-S42)
         ⛔ İkisi de aynı şeyi istemiyor ✅ · B figüran değil ✅
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4].

### 👤 KARAKTER KARTLARI — B5'ten hemen SONRA [`KARAKTER_KARTI` §1]

> Kart PROMPTA GİRMEZ; TIMELINE'daki her gövde fiilinin hangi tempoda
> yazılacağını söyler. İki kart **üç davranış satırında** ayrışır (§2 LİSTE 2).

**KART 1 — KURTARMA PİLOTU**

| satır | içerik | sahne |
|---|---|---|
| ROL | kurtarma pilotu — kol ekranı, mühürlü giysi, sırtında katlı kurtarma torbası | S01 · S05 |
| İSTEK | kayıp mürettebatı bulup gemisine geri götürmek | S03 · S07 |
| BASKI TEPKİSİ | **KONTROL EDER** — engelde önce ölçer ve kaydettirir, sonra hareket eder | S06 · S09 · S14 |
| ALIŞKANLIK | her şeyi kaydettirmek: bir şeyi gördüğünde "Kaydet." der ve devam eder (K012 · K019 · K031) · **KIRILMA** K047: bu kez kaydı kapatır | S04 · S06 · S09 → S13 |
| SINIR | geçidi açmaz — Dünya'ya bir cümle bile göndermez (K095) | S25 · S42 |
| ZAAF | aynı kaybı ikinci kez kabullenmek istememesi; görünür izi: gördüğünü kaydettirip ERTELEMESİ | S06 · S07 · S09 |
| TEL | baskı altında eldivenli eli bir cama yaslanır ve orada kalır (K009 · K083 · K160) | S04 · S22 · S41 |
| İLK ↔ SON | ilk klipte bir kaydı DİNLİYOR (çağrı), son sahnede bir kayıt BIRAKIYOR (işaretçi) | K001 ↔ K188 |

**KART 2 — ODADAKİ**

| satır | içerik | sahne |
|---|---|---|
| ROL | kardeş görünümü — ev kıyafeti, kasksız, giysisiz; odanın havasına bağlı | S11 · S12 |
| İSTEK | Mira'nın kalması (ve gemisinin alçalması) | S15 · S20 · S27 · S41 |
| BASKI TEPKİSİ | **GERİ ÇEKİLİR** — sıkıştığında konuyu değiştirir, soruyu geri çevirir (K067 "Sen söyle.") | S12 · S18 |
| ALIŞKANLIK | lambayı yakmak ve cümleyi söylemek — her seferinde AYNI vurguyla (K045 · K059) | S13 · S16 |
| SINIR | kapının eşiğini geçemez (K044) | S12 |
| ZAAF | kayıtta olmayanı bilemez; görünür izi: cevaptan önceki gecikme ve kelimeler arası kesik ekler | S16 · S18 |
| TEL | baskı altında Mira'ya bir adım yaklaşır (K067) — mesafeyi kapatarak cevaplar | S18 · S20 |
| İLK ↔ SON | ilk göründüğünde yatağın kenarında OTURUYOR, son göründüğünde kapıda AYAKTA duruyor ve yol kesiyor | K038 ↔ K101 |

```
AYRIŞMA DENETİMİ (≥3 davranış satırı):
  İSTEK          götürmek        ↔  kalmak                         ✅
  BASKI TEPKİSİ  kontrol eder    ↔  geri çekilir                   ✅
  ALIŞKANLIK     kaydettirmek    ↔  lambayı yakıp cümleyi söylemek ✅
  TEL            el cama yaslanır ↔ bir adım yaklaşır              ✅ (dördüncü)
⛔ FAZ FARKI: hiçbir TIMELINE satırında ikisi aynı fiili aynı saniyede yapmaz.
   TEK BİLİNÇLİ İSTİSNA K048 (ikisi aynı anda gülümser) — ve tekinsizliği
   tam olarak bu kuralın bilerek çiğnenmesinden geliyor. Sahne çalışmasına yazılır.
MESAFE EĞRİSİ (§5 · metre): S11 1,8 → S13 1,2 → S16 1,0 → S18 0,7 (Lena yaklaşır) →
   S20 0,5 (yol keser) → S27 1,5 (eşik) → S30+ kadraj dışı → S41 ∞ (yalnız ses)
   ⛔ Ardışık sahnede en çok bir bant; final mesafesi ilk mesafeden farklı ✅
KİM SOLDA: Mira kadrajın SOLUNDA, Lena SAĞINDA; taraf değişimi yalnız S20'de
   (Lena önüne geçer) ve o klipte geçiş görünür.
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅ (§3)
☑ risk sayımı yazıldı (14/14) ve eşik kararı verildi (kilit tavanı ≤20)
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S44 → S47 · ikinci ödeme S49)
☑ ÖN-OTOPSİ KARAR: GO · iki yüksek×yüksek hücre önlem aldı ve denemeye bağlandı
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
