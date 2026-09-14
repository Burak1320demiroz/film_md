# 🧠 THE_DRY_ANCHOR — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     SAHİP VERDİ — "dev bir uzay gemisi ile cöz gezegenine iniş
   yapan ve keşif yapan bir astranot"
   (AI seçmediği için "depoda eksik olandan seç" kuralı koşmaz; yine de
    sayaç okundu: 95 film · tema beyanı olan 40 klasör.)
② FORMAT:   yatay 2-4 dk (uzay)   → kart §2.2 · bölüm sayısı 2
③ SAHNE:    14                    → sahip verdi
   Bant §2.2'de 12-18'dir → 14 BANDIN İÇİNDE, sahip izni GEREKMEZ, D74 satırı
   AÇILMAZ.
④ REFERANS PAKETİ: YAZILMASIN (sahip kararı)
   §5b tablosu yine de ölçüldü (aşağıda) — karar sahibin, kayıt deponun.
   PLAN'a düşecek TEK SATIR gerekçe:
   "REFERANS PAKETİ YAZILMADI — sahip kararı, 10.09.2026. T1·T2·T3·T5
    tetikleyicileri DOĞRUYKEN atlandı; biçim kilidi (kask geometrisi ·
    gemi anatomisi · toz kademesi) tamamen METİNLE taşınıyor ve D146'nın
    üç ölçülmüş vakasının riski bu satırla açıkça kabul edilmiştir [D74]."
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "dev bir uzay gemisi ile cöz gezegenine iniş yapan ve keşif yapan
        bir astranot"                     (kelimesi kelimesine, yorumsuz)
REPLİK: YOK — talep cümlesinde diyalog geçmiyor; film 0 replik yazılacak.
        Diyalog kapı zinciri (SES_VE_DIYALOG §1a-§2a + DIALOGUE_CRITIQUE)
        AÇILMAZ. ⛔ Ama SES yok demek değildir: her sahne AUDIO cümlesi
        taşır ve ortam yatağı 14/14 kesintisizdir [D83].
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**
Emsal: THE OPEN CIRCUIT'te *"fırtınalı"* ve *"patlamalı"* istekleri 610 Pa
Mars basıncında imkânsızdı; ikisi de yeniden tanımlandı, gerekçe yazıldı ve
biri filmin novum'u oldu.

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "cöz gezegeni" | Yazım belirsizliği — depoda "cöz" diye bir ortam kartı yok. En yakın okuma **ÇÖL GEZEGENİ**. | ÇÖL GEZEGENİ olarak okundu → `KILAVUZ_REHBERI` §3.2 İNCE ATMOSFER kartı (Mars sınıfı). | ⛔ Sahibe BEŞİNCİ SORU SORULMADI (skill dört soruyla sınırlı). Varsayım burada AÇIKÇA ilan edildi [D74]. Yanlışsa tek satırlık düzeltme yeter: ortam kartı değişir, novum ve B5 aynen durur. |
| "iniş yapan … astranot" | ⛔ D69: gemiden İNME/BİNME hareketi deponun ölçülmüş iki IDENTITY BREAK'inin ikisinin de çıktığı sahne tipidir (STONE SKY 1:40 · STARLESS CIRCLE 2:10). Astronotun rampadan inişi kadraja alınamaz. | **İNEN ŞEY GEMİDİR, ASTRONOT DEĞİL.** Astronot filmin başında ZATEN YERDEDİR (sahadaki mühendis); gemi onun üstüne iner. Sahibin istediği "iniş" görüntüsü S0'da TAM OLARAK VAR ve ölçek olarak daha güçlü — ama insan uzuvlu geçiş hareketi 0 kare. | Sapma kaydı [D74]: kadrajdaki olay korundu, riskli HAREKET çıkarıldı. Karşı kanıt da kayıtlı: RING LIGHT'ta biniş hareketi planda hiç açılmadı ve klon çıkmadı (Sayı 10/10). |
| "keşif yapan" | Keşif = "yürüyüp bakmak" olarak yazılırsa KAMERA-TAŞIYICI testinden kalır (RING WALKER Karakter 4/10: karakteri drone ile değiştirsen ne kaybederdin?). | Keşif bir İŞE bağlandı: astronot zemini ARAR — hangi noktanın altında taş var. Bakış değil ÖLÇÜM; her bakışın bir aleti ve bir sonucu var. | UZAY_SENARYO §9.1 üç etkinlik çapası: TERCİH (S9) · TEPKİ (S3 ve S11'de bedensel cevap yazılı) · BAŞLANGIÇ AMACI (ilk 3 saniyede nereye gittiği görünür). |
| "dev uzay gemisi" | Ölçek deponun ölçülmüş kayma noktası: AMBER LATTICE'te monolit 25 m → 80 m fırladı; COLD BURN'de 65 m gemi lander boyunda okundu [D32]. | Gemi ölçüsü PLAN fizik defterine ve QA_SPEC D bloğuna METRE ile yazılır; prompt gövdesine yalnız GÖVDE BOYU (1H = 1,90 m) iner. Kesir merdiveni `UZAY_USSU` §5.2 formülüyle hesaplanır, elle seçilmez. | ⛔ Prompt gövdesinde tek metre/derece/f-sayısı yok [D45 · D138]; kamera MESAFESİ muaf. |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 2-4 dk (uzay) → §2.2 kartı · 12-18 sahne × 10 s · 2 bölüm
               · im-to-video · Veo 8 s + 2 s uzatma
ORTAM:         §3.2 İNCE ATMOSFER (Mars sınıfı)
   → tetiklediği ZORUNLU satırlar:
     · toz YAVAŞ ama KESİN çöker ve YERE OTURUR — havada asılı kalmaz [D39]
     · gölge YUMUŞAK kenarlı ve dolgu ışığı VAR — bu MEŞRUDUR, hata değil [D41]
     · dış ses BOĞUK ve ZAYIF taşınır (vakumun "duyulan her şey temastır"
       kuralı BURADA GEÇERSİZ)
     · rüzgâr kuvveti YOK DENECEK KADAR: 30 m/s = 9 Pa, hiçbir şeyi devirmez
       ⛔ FIRTINA GÖSTERİLMEZ — göstermek fizik yalanı olur [TUR 14]
     · egzoz/püskürtü YAYILIR ve ÇÖKER (vakum düz konisi GEÇERSİZ [D36])
     · ⛔ AY negatif bloğu KULLANILMAZ; [YÜZEY ÜSSÜ · MARS] bloğu kullanılır
       ("no atmospheric haze" + "shadows absolutely black" burada FİZİK
        HATASI yazdırır) [UZAY_USSU §6]
   SAYILAR (04_ARASTIRMA §TUR 14): 610 Pa · %95 CO2 · g = 3,721 m/s² ·
   gün ışığı Dünya'nın %43'ü · toz ~1,5 mikron, triboelektrik ·
   gün batımı çevresinde BUZ MAVİSİ hale
TÜR:           bilimkurgu · dal: SERT (hard) — §4.1 · ana kulvar
KLİP SÜRESİ:   10,0 s   ⛔ D124 KAPISI AÇIK: bu sayı hattın ölçülmüş
               standardıdır (yatay 2-4 dk · 14 × 10 s emsali THE BENT GRASS)
               ama BU ARAÇTA henüz ölçülmedi. PLAN §0'a doldurulacak satır:
               `KLİP SÜRESİ = ____ s  (ffprobe -v error -show_entries
                format=duration -of csv=p=0 <ilk klip>)`
               ⛔ Ölçüm yapılmadan üretim başlamaz.
SAHNE SAYISI:  14   RUNTIME: 140,0 s = 2:20   (14 × 10,0 · ayrı hook klibi YOK)
               ⛔ Format tabanı 120 s — 140 s bandın İÇİNDE.
BÖLÜM SAYISI:  2    BOLUM_1 = S0-S6 (7) · BOLUM_2 = S7-S13 (7)
               ⛔ Bölüm SINIRI da ardışık bir çifttir: S6→S7 ACI_YAYI §3
                 güvenli bandından geçer.
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:  "Bu ovadaki tozu hiç yağmur sıkıştırmadı: taban basıncı yüksek olan
         her şey iner ve DURMAZ."
        ⭐ Bir DURUM değil bir KURAL, ve olay örgüsünü ZORUNLU kılıyor:
          çapa tutmazsa gemi eğilmeye devam eder. Ölçülmüş ölçüt buydu —
          novumun VAR OLMASI yetmiyor, karakteri bir şey yapmaya MECBUR
          etmesi gerekiyor (INVERSION 6/10 ↔ RING WALKER 4/10).
        ⭐ Ve DOĞRULANMIŞ BİLİM: yağmur görmemiş ince regolit sıkışmaz;
          taşıma kapasitesi düşüktür. Serinin gerçek kancası budur —
          "bu bilimkurgu değil, gerçekten böyle görünürdü".

NOVUM TAŞIYICISI:  <ÇELİK KAZIK (geniş bilezikli, kısa saplı)>
                 × <iki elle sürme ve DURMA anı>
                 → <ihlal: kazık durmaz, bilezik toza gömülür, vuracak
                    baş kalmaz>
   ⛔ Taşıyıcı SOMUT ve ADI OLAN bir nesnedir — türetilmiş bir optik ya da
     atmosferik fenomen DEĞİL. Bu, THE WRONG SHADOW'un ölçülmüş çöküşünün
     (3,0/10) doğrudan panzehiridir: orada novum gölgeye yüklendi, dönme
     hareketi jalonlara SIÇRADI ve novum ekranda 0 kare çıktı [D73].

① TEK KARE:  ✅ "Kum, sürülen ÇELİK KAZIĞIN başını yutmuştur; sürücü hâlâ
   iki elde, ama vurulacak bir baş kalmamıştır."
   → Cümle TAŞIYICI NESNENİN ADINI içeriyor [D157]. Kare S3'tür ve
     üretimden önce TEK BAŞINA koşulacak (KAPI 1 — aşağıda §6).

② KİNETİK BAĞIMSIZLIK:  ✅ Kural iki jestle kanıtlanır (S3 kazık durmaz ·
   S11 kazık durur ve sürücü geri seker). Replik 0 · ekran metni 0 ·
   dış ses 0 · gösterge 0. Kadrajda okunacak tek şey harekettir.

③ BAŞLIK ŞEMASI:  ✅ "This Dust Has No Bottom" (5 kelime)
   → VIRAL_BASLIK'ın DÜZ GERÇEK kalıbı; doğrulanmış bir olguyu sıradan
     bir cümle gibi söylüyor. Alternatif: "Nothing Here Stops Going Down".

⭐ ÜÇÜ DE ✅ → KONSEPT GEÇTİ, sıralama yazılabilir.
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — İNSAN-MAKİNE SINIRI
   (⛔ satır başında "TEMA:" YAZILMAZ — sayac.sh temayı film klasöründen
    özyinelemeli sayar; gerçek beyan PLAN dosyasında bir kez yapılır.)

▸ tanım cümlesi —
   "Uzayı geçen makine kendi başına YERİNDE DURAMAZ; onu tutan tek şey,
    bir insanın eliyle sürdüğü tek bir çelik çubuktur."
   ⛔ TAKAS DEĞİL TANIM [§3c moratoryumu]: cümle "X olabilmesi için Y feda
     edilir" kalıbında değil. Bedel filmde VAR (S9) ama TEMA CÜMLESİ
     bedelin üstüne kurulmadı — beş filmde üst üste tekrarlanan kalıp bu
     filmde altıncı kez yazılmıyor.

▸ depoda kaç kez kullanıldı — 2 (sayac.sh 🎭 TEMA DAĞILIMI, 10.09.2026)
   ⭐ Yatay/süreç temalarının (Kimlik 3 · Zaman 5 · Fedakârlık 4 ·
     İnsan-Makine 2) EN AZ kullanılanı. §4 süre-tatmin kuralı: bu bir
     SÜREÇ temasıdır ve yatay 1-5 dk bandına aittir ✅ (dikeyde olsaydı
     tamamlanma cezası yerdi).

▸ motif kanalları —
   NESNE   : tek çelik kazık ↔ dev gövde — ikisi AYNI karede (S4 · S13)
   KİNESİK : iki elle sürme jesti; aynı jest S3'te sonuçsuz, S11'de sonuçlu
             ⛔ JEST TEKRARI KURALI: aynı fiziksel jest EN FAZLA İKİ kez ve
               ikincisi ANLAMI DEĞİŞTİRDİĞİ için var (keşif → doğrulama)
   KAMERA  : A kurulumunda gemi kadrajın büyük kısmı / insan ~1/20;
             D kurulumunda eldiven kadrajın çoğu / gemi kadrajda YOK
   IŞIK    : tek alçak güneş; gövde soğuk ve yansıtıcı, eldiven ve kazık
             sıcak alır — insan tarafı ısınır, makine tarafı ısınmaz

▸ TEMA SAHNE İNDEKSİ (≥3 zorunlu) — S3 · S4 · S9 · S11 · S13
  (S9 10.09.2026 KAPI turunda eklendi: `03_PLAN_ONCESI` B3 BEDEL sahnesinin
   motif listesinde olmasını ister — bedeli taşımayan tema dekorlaşır)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa malzeme AZALTILIR —
> prompt iyileştirmek bu deponun ölçtüğü kadarıyla işe yaramıyor.

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| **KART 1** SU / SIVI | ❌ | Çöl gezegeni; sıvı 0 kare. | Tasarımla kapalı. ⛔ Ek kilit [D56]: ÇÖL sözlüğü su ÇAĞIRIR — `dalga · deniz · kumul denizi · dalış · akıntı` prompt gövdesine GİRMEZ; kum hareketi balistik tarif edilir. ⚠️ Ve filmin taşıyıcısı bir ÇAPADIR: İngilizce promptta `anchor · moor · sea` **hiç yazılmaz**, nesne yalnız GEOMETRİSİYLE anılır. | 0 |
| **KART 2** CANLI / HAYVAN | ❌ | Canlı 0 kare, uzaylı 0 kare. | Tasarımla kapalı — `UZAYLI_VARLIK_TASARIM_KILAVUZU` kapıları AÇILMAZ. | 0 |
| **KART 3** KASK / VİZÖR / EKİPMAN | ✅ | Her uzay filminde doğru; bu filmde 14/14 sahnede kask var. | ⛔ DÜŞÜRÜLEMEZ (yapısal). Kilitlendi: vizör GEOMETRİYLE (kabuk + DÜZ ön cam + GÖRÜNÜR METAL ÇERÇEVE + yaka mührü + tek spekülar çizgi); `seamless/domed/bubble` yasak [D146]; yüz her kafa açısında okunur [D79]; sırt POZİTİF tarifle [D139]. ⚠️ Referans paketi YOK → kilit tamamen metinde. | **YÜKSEK** |
| **KART 4** İKİNCİ FİGÜR | ✅ | Kartın kendi kuralı: her filmde geçerli, atlanamaz. | TEK astronot; `exactly one human` 14/14 promptta. ⭐ Kartın kendi cümlesi bu filme birebir uyuyor: "iniş ve kalkış sahnelerinde gemi UZAKTAN çekilir, rampada kimse görünmez" — S0/S1 tam böyle kuruldu. D69 gereği iniş/biniş hareketi 0 kare; D140 gereği her klibin ilk 0,6 s'i klon taranır. | ORTA |
| **KART 5** EKRAN / SAYAÇ / METİN | ❌ | Gösterge · kadran · ekran · HUD 0 kare. | Tasarımla KAPATILDI. Sayaçlar ÇEVRESEL ve METİNSİZ: ① ayaktaki toz halkasının yüksekliği (monotonik, S1→S12) ② kalçadaki iki kazık yuvası (dolu → 1 boş → 2 boş). ⛔ Sayaç PLANDA yazılı olacak — ROSE COAT'ta rapor "no counter present" yazdı ve filmde ÜÇ sayaç vardı [D134]. | 0 |
| **KART 6** PARÇACIK / TOZ | ✅ | Filmin ANA MALZEMESİ: iniş püskürtüsü, toz halkası, gömülen kazık. | ⛔ DÜŞÜRÜLEMEZ (novum burada yaşıyor). Kilitlendi: her toz cümlesi ZERRE YOĞUNLUĞU + DÜŞÜŞ HIZI taşır ve perde/şelale/duvar benzetmesi kullanılmaz [D143]; toz YAVAŞ ama KESİN çöker [D39]; `swirl/hang/float/suspended` kökleri yalnız negatif blokta [D59]; kademe MONOTONİK [D147] ve faz ETİKETİ gövdeye girmez [D155]. **Malzeme AZALTILDI: FIRTINA ve KALKIŞ çıkarıldı** (aşağıda). | **YÜKSEK** |
| **KART 6b** KATMANLI / BÖLGELİ DÜNYA | ❌ | Tek ortam · tek bölge · tek ışık rejimi (gündüz, alçak güneş). | Tasarımla kapalı. Işık takvimi yine yazılır ve MONOTONİKTİR (güneş yalnız alçalır) — geri sarma [D193] ölçülebilsin diye. | 0 |
| **KART 7** DİYALOG | ❌ | 0 replik. | Tasarımla kapalı. ⛔ Ama SESSİZ ≠ SESSİZ DOSYA: yatak envanteri yazılır [D83] ve QA_SPEC'e `DIALOGUE LINES: 0` açıkça konur ki mercek bunu KISIT olarak okusun [D113]. | 0 |
| **KART 8** KAMERA | ✅ | Kartın kendi kuralı: her filmde geçerli. | 14/14 TAM LOCKOFF; klip içi kamera hareketi 0. Ölçek değişimi kameradan değil KURULUM DEĞİŞİMİNDEN gelir. ⭐ Kartın "tek iyi haber" olmasının sebebi ölçüldü: Kamera 2→8 sıçraması klip içi hareket TALEBİ silinerek geldi. | DÜŞÜK |
| **KART 9** TEK BASKIN IŞIK + HEDEFE HAREKET | ✅ | Alçak güneş kadrajın en parlak öğesi; astronot iki kez bir hedefe (koyu taş yaması · gemi ayağı) doğru yürüyor. | Kısmen düşürüldü: hedef hiçbir sahnede SİLİK değil — koyu yama, soluk toza karşı SERT KENARLI ve her karede aynı ekran diliminde, adıyla yazılı. Ayrıca DÖRT KANALLI kilit zorunlu (hedef-dilim + yön aynı cümlede · omuz hattı derecesi · IŞIĞA GÖRE POZ · yön negatifi). ⛔ "silik hedef + baskın ışık + yanal yürüyüş" üçlüsü hiçbir sahnede bir arada YAZILMAYACAK [UZAMSAL §6.8]. | ORTA |
| **KART 10** İNSANSIZ SAHNE + UZUN NEGATİF | ❌ | 14/14 sahnede insan var. | Tasarımla kapalı → yapısal red profili (COLD BURN S8 V2) hiç açılmıyor. | 0 |
| **KART 11** DEĞİŞKEN SÜRE / SAHNE İÇİ KESME | ❌ | Sabit ızgara: 14 × 10,0 s. Sahne içi kesme 0. | Tasarımla kapalı → kırpma bütçesi tablosu gerekmez. ⛔ Ama BOZULMA KARESİ sütunu SABİT IZGARALI FİLMDE DE doldurulur [KURGU_VE_TESLIM §2]. | 0 |
| **KART 12** POLİTİKA YÜZEYİ | ✅ | Üç imza birden: ⑥ yüzü kapatan ekipman (kask) · ⑦ tekdüze KIZIL palet + yakın plan · ve ölçülmüş bir red kalıbı: `hammer` + `blows` (RISING SNOW S2 reddi). | ⛔ Kartın kendi kuralı: "malzeme azalt" POLİTİKAYA UYGULANMAZ — cevap POZİTİF TARİF ve ANLAM MALİYETİ satırıdır. Kilitler: sürücü `hammer` diye ADLANDIRILMAZ, formu tarif edilir ("the flat of the tool comes down on the collar, once, then again") [D67 · D123]; yasak cümlesi de YAZILMAZ; kırmızı KAYNAĞA bağlanır ve her CU'ya ÇEVRESEL ÇAPA konur; beyaz giysi + cyan pratik ışık karşıt renk. Milliyet 0 · kurum 0 · marka 0. | ORTA |
| **KART 13** YAPI ÖLÇEĞİ VE TEKRAR EDEN BİRİM | ✅ | DEV GEMİ filmin baş varlığı — sahibin talebinin merkezi. | ⛔ DÜŞÜRÜLEMEZ (talebin kendisi). Kilitlendi: ANATOMİ KARTI (ayak n · lüle n · kapak n · pencere n — TEK sayı, `hundreds of` YASAK); ölçü SPEC'te metre / promptta gövde boyu; kesir merdiveni §5.2 FORMÜLÜYLE; her yapı kadrajında EN AZ BİR ÖLÇEK ŞAHİDİ (ön planda figür / tekrar eden birim / kadrajı taşan kenar); maket negatifi ("no tilt-shift look, no miniature or toy-model read, no vertical band of blur"). | **YÜKSEK** |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  KART 6 · İNİŞ PÜSKÜRTÜSÜNÜN TOZU
   (deponun ölçülmüş iki arızası burada birleşiyor: D143 toz ŞELALESİ ve
    D39 toz SÜZÜLMESİ — ikisi de "sürekli düşüş" gibi SIFATLA yazılmış
    cümlelerden doğdu.)

POZİTİF BİÇİMİ — SAYIYLA:
   · toz halkası gövde genişliğinin İKİ katı çapında yayılır
   · halka SEKİZ saniyede kapanır ve yere OTURUR
   · oturduktan sonra havada asılı kalan zerre: SIFIR
   · zerreler DÜŞER, dönmez: yörünge düz ve aşağı, yatay sapma yok
   · düşme hızı yürüyüş temposundadır — kar gibi savrulmaz, kum gibi akmaz
   · zemine oturan katman kalınlığı BİR PARMAK, ve o katman bir daha
     kalkmaz (yağmur yok, rüzgâr 9 Pa)
⛔ Negatif cümle YASAĞI söyler, BİÇİMİ söylemez — THE OPEN CIRCUIT'in
   25 sahnesinde "no lightning bolt" yazılıydı ve doruk boşalması ŞİMŞEK
   geldi. Bu filmde biçim POZİTİF ve SAYILIDIR [D192].
```

⛔ **Sıfat yetmez.** THE OPEN CIRCUIT 1 numaralı riskini (KIVILCIM) adıyla ilan
etti ve yalnız sıfatla korudu — *"TEK, İNCE, DÜZ ve SÖNÜMLÜ"*. Aynı planda
sayıyla yazılan her şey tuttu. Ekrana **en az 0,5 s süren, dallanan bir şimşek**
geldi; her sahnenin NEGATIVE bloğunda *"no lightning bolt"* yazılıyken.
**Negatif cümle yasağı söyler, BİÇİMİ söylemez; model boşluğu doldurur.**

```
TETİKLENEN RİSK:  7 / 14      (KART 3 · 4 · 6 · 8 · 9 · 12 · 13)
EŞİK:             5
⛔ EŞİĞİN ÜSTÜNDE → MALZEME AZALTILDI. Çıkarılanlar:

   ① FIRTINA — çıkarıldı. Gerekçe hem risk hem FİZİK: 30 m/s rüzgâr bu
      basınçta 9 Pa uygular ve hiçbir şeyi deviremez; fırtına göstermek
      serinin tek sermayesini (doğruluk) harcardı [TUR 14].
   ② KALKIŞ — çıkarıldı. Film gemi kalkmadan biter; D148'in kalkış yarısı
      (bacak katlanması · alev-bacak çakışması) hiç koşmuyor ve kadrajdaki
      alev sahnesi sayısı 1'e (yalnız S0 inişi) iniyor.
   ③ İÇ MEKÂN — 0 sahne. §3.10 basınçlı hacim kartı hiç açılmıyor;
      kasksız kare 0, dolayısıyla D37/D57 ekipman durum geçişi riski 0.
   ④ İKİNCİ ARAÇ / GEZİCİ — yok. Tek yapı = gemi; KART 13 tek varlıkla
      sınırlı kalıyor.
   ⑤ CANLI · SIVI · EKRAN · REPLİK · SAHNE İÇİ KESME — beşi de 0.

⭐ KALAN 7'NİN DÖRDÜ YAPISALDIR ve hiçbir filmde sıfırlanamaz:
   KART 3 (kask) · KART 4 (ikinci figür) · KART 8 (kamera) · KART 12
   (politika — kartın kendi kuralı gereği malzeme azaltılarak düşürülmez).
   Gerçekten filme özel ve indirilebilir olan üç kart kaldı:
   KART 6 (toz) · KART 9 (ışık mıknatısı) · KART 13 (dev gemi).
   ⛔ Üçü de filmin KONUSUDUR: toz novum'un kendisi, dev gemi sahibin
     talebi, alçak güneş ortam kartının zorunlu ışığı. Bu üçü çıkarılırsa
     film çıkarılmış olur.

KABUL GEREKÇESİ [D74]: eşik 7'de kabul ediliyor; karşılığında üç kart
   SAYISAL kilide bağlandı (KART 6 → A5 bloğu · KART 13 → anatomi kartı +
   kesir formülü · KART 9 → dört kanallı kilit) ve üçünün de ÖLÇEN MERCEĞİ
   yazıldı [D187]: KART 6 → ⑥ FİZİK · KART 13 → ⑤ ARKA PLAN + ⑥ FİZİK ·
   KART 9 → ⑪ IŞIK.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — yalnız soru ④ "analiz karar versin" ise

> `REFERANS_PAKETI_KILAVUZU.md` §1 tablosu. **Altısı da tek tek ölçülür.**

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ DOĞRU | Astronot · 14/14 sahne — ayırt etme kanalı kapalı |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ DOĞRU | Kask kabuğu + vizör geometrisi — D146'nın üç ölçülmüş vakasının sınıfı |
| T3 | oranı sözle yazılamayan nesne | ✅ DOĞRU | DEV GEMİ · S0 · S1 · S4 · S12 · S13 |
| T4 | insan dışı canlı | ❌ YANLIŞ | Canlı 0 kare |
| T5 | tekrar eden insan dışı olay | ✅ DOĞRU | Toz kademesi (halka yüksekliği) — S1'den S12'ye monotonik |
| T6 | bir varlık tekrar tekrar dönüyor | ⬜ ÖLÇÜLEMEZ | Üretim yok; iki klipte fark çıkıp çıkmadığı bilinemez |

```
KARAR: YAZILMAZ — ⛔ SAHİP KARARI (soru ④). Analiz karar vermedi; tablo
       yalnız KAYIT için dolduruldu ve DÖRT tetikleyici DOĞRU çıktı.
       Dosya SİLİNMEZ, `⬜ BEKLİYOR` durur; PLAN'a §0'daki tek satır
       gerekçe yazılır.
       ⚠️ Kabul edilen bedel adıyla: SKYLIGHT (1 filmde 3 kask) ·
       YERÇEKİMİ F2 (vizör geometrisi 9 promptta ölçüyle yazılıydı,
       kubbe çıkan 6 klibin 5'inde tam tarif vardı) · STANDING WIRE
       (24 klibin çoğunda kubbe vizör). Bu filmde aynı risk METİNLE
       taşınıyor ve ölçen mercek ② DEVAMLILIK'tır.
⚠️ T1 bu deponun neredeyse her filminde doğrudur.
⛔ YAZILMAZ ise PLAN'a tek satır gerekçe [D74 kalıbı] — sessizce atlanmaz.
⛔ YAZILIR ise KAPI 0'dır: sayfası ONAYLI olmayan ve seed'i yazılmayan
   varlığın geçtiği hiçbir sahne üretilmez [D168].
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S3 · 33,0-37,0 s
   CU · iki eldivenli el · kısa saplı sürücü · kazık bileziğine inen darbe.
   ÜÇ imza aynı karede birleşiyor: ⑥ yüzü kapatan ekipman (kask kadrajda) ·
   ⑦ kadrajın çoğu KIZIL toz + yakın plan · ve ölçülmüş red kalıbı
   `hammer` + `blows` (RISING SNOW S2, çözümü GEÇTİ).

NÖTR TARİFİ (prompt gövdesine bu cümle girer):
   "Both gloved hands hold a short weighted driver above a steel pin with a
    broad collar. The flat of the driver comes down on the collar, once,
    then again. Behind the hands the pale ground runs back to a low dark
    ridge, and the far ridge stays in frame."
   ⛔ `hammer` · `blows` · `strike` · `smash` YAZILMAZ.
   ⛔ Yasak cümlesi de YAZILMAZ ("no violence" D123 tuzağıdır).
   ⭐ Son cümle KART 12 §3.2'nin ÇEVRESEL ÇAPASIDIR: yakın plan daraldıkça
     sınıflandırıcı bağlamı kaybeder ve yalnız dokuya bakar; uzak bir
     yüzey sahnenin NE olduğunu söyler.

ANLAM MALİYETİ SATIRI [POLİTİKA §4.3] — plana yazılacak:
   ÖNLEM:   fırtına ve kalkış sahneleri çıkarıldı; aletin adı yazılmıyor
   MALİYET: filmin tek "büyük hareket" vuruşu (kalkış) ve rüzgârın
            yarattığı dış baskı gitti
   TELAFİ:  baskı KANAL ③'e (alet tepkisi) ve KANAL ②'ye (malzeme sonucu)
            taşındı: kazığın durmaması · bacaktaki toz halkasının
            yükselmesi · sürücünün geri sekmesi
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Gemiyi kalkışa hazır bırakmak — dört ayağı hizada ve kilitli.
         ⭐ Film başlamasa da var olan bir İŞ: sahadaki mühendisin görev
           listesinin son maddesi. ⛔ "anlamak/görmek/keşfetmek" DEĞİL;
           ölçülebilir, biten, birinin devraldığı bir iş.

ENGEL:   Zemin. Yağmur görmemiş toz sıkışmamıştır; taban basıncı yüksek
         olan her şey iner ve durmaz. İlk kazık yutulur. Tutan tek yer —
         tozun sığ olduğu koyu, rüzgârla süpürülmüş yama — hattın
         yetişmediği kadar uzaktadır.

BEDEL:   ÖRNEK KASASI · **S9**
         Hattı uzatmanın tek yolu, kasa rafının kayışını söküp hatta
         eklemektir. Kasa toza iner ve orada kalır: filmin geliş sebebi,
         dönüşün bedeli olur.
         ⭐ ASIL KAPI BUDUR ve sahne numarası taşıyor. Bedel AYNI karede
           görünür (kasa yerde + kalçadaki ikinci yuva boş) — 79 filmde
           İSTEK 8, ENGEL 2 kez yazılmıştı; bu film o listeye girmiyor.

MUHATAP: ORTAMIN KALICI DEĞİŞEN PARÇASI (B5 seçenek 4)
         ① ayaktaki toz halkasının DURDUĞU çizgi — yükselmesi biten sayaç
         ② gergin hat ve taşa oturmuş kazık
         ⛔ FINAL §4.1 kapısı: muhatap SON KAREDE görünmelidir → S13'te
           üçü de kadrajda (halka çizgisi · hat · kasa).

AYRILIK: — (tek insanlı film; B5b koşmaz)
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4].

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅   (TEK KARE · KİNETİK BAĞIMSIZLIK · BAŞLIK)
☑ risk sayımı yazıldı ve eşik kararı verildi   (7/14 · eşik 5 · malzeme
   beş kalemde azaltıldı · kabul gerekçesi yazılı [D74])
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor   (S9)
→ üçü de ✅ → 03_SAHNE_SIRALAMASI.md yazılabilir

⛔ ÜRETİM KAPISI 1 — SIRALAMADAN DEĞİL, ÜRETİMDEN ÖNCE KOŞAR [D73 · D74]:
   S3'ün IMAGE promptu TEK BAŞINA üretilir. Çıkan karede
     · kazığın bileziği toz seviyesinin ALTINDA mı
     · sürücü hâlâ iki elde ve vurulacak baş YOK mu
   ikisi birden okunmuyorsa VİDEO ÜRETİMİNE HİÇ GEÇİLMEZ.
   KABUL / RET / YABANCI GÖZ / SONUÇ satırları PLAN'a yazılır ve
   SONUÇ tarih + GEÇTİ/BATTI olarak doldurulmadan S4 üretilmez.
```
