# 🎬 SUSMAYAN_NOBETCI — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 8 dk · 48 sahne · 4 bölüm dosyası (sahip kararı; kart §2.7 2 × 24 der → D74 ①)
               ⚠️ QA birimi BÖLÜM — SPEC A `PART GRID` satırı dolu; birim kararı ⬜ K1
ORTAM:         §3.1 VAKUM (alçak yörünge · 0 g) + §3.10 BASINÇLI İÇ HACİM (çekici kokpiti · kaçış kapsülü · tahliye bölmesi)
TÜR:           bilimkurgu   (tek açık dal — §4.1) · dal: sert uzay gerilimi / yanaşma (aksiyon kulvarı)
KLİP SÜRESİ:   ⬜ 10 s VARSAYIM — ARAÇTAN ÖLÇÜLECEK [D124 · K3]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
SAHNE SAYISI:  48        RUNTIME: 480 s = 8:00 (hook S0'ın İÇİNDE; 48 × 10 s)
MOTOR:         OMNI 1.1 Flash (I2V) · ZİNCİR MODU ① tek başlangıç karesi (⬜ K2: S36-S37 için ② başlangıç+bitiş)
LOGLINE:       Savaştan kalma, motor ateşleyen her şeyi vuran bir uydunun menzilinde, bir çekici pilotu havası
               tükenen tahliye gemisine motor ateşlemeden yanaşmak zorundadır.
```

### 🧭 D74 KAYITLARI — bilinçli sapmalar ve sahip kararları (kaydı olmayan sapma yapılmamış sapmadır)

| # | kural / kart | sapma | gerekçe |
|:--:|---|---|---|
| ① | §2.7 "2 bölüm × 24" | 4 bölüm dosyası × 12 sahne | sahip 17.09.2026: "Dört bölümün her biri 12 sahne." · QA birimi K1 |
| ② | YANASMA §1.2 "V3 oran karesi en çok 2" | dört kontrollü iki-gövde kadrajı (I · J · K · Z) | sahip: "Birkaç kontrollü genel plan bu coğrafyayı kurabilir" — her birinde oran + hangi uç önde + ekran tarafı cümlesi |
| ③ | D210 "kapanış CAMERA = açılış CAMERA" | S0 kokpit (A) · S47 dış geniş (Z) | sahip tarifi; kafiye OLAY kafiyesi + Z dönüşü S43↔S45↔S47 |
| ④ | FINAL §2.1 kapanış bütçesi %5-7 | S46-S47 = %4,2 | sahip tablosu (07:40-08:00) |
| ⑤ | DIYALOG §8 "final sessiz" (öneri) | S46'da tek kısa telsizsiz söz | sahip notu; söz S1 çağrısının cevabı |
| ⑥ | REFERANS PAKETİ (5/6 tetikleyici doğru) | YAZILMADI | sahip kararı 17.09.2026 — telafi: ANATOMİ KARTI sayıları + Scene Foundation ana kareleri; kask biçim riski 04_UYARI R2 |
| ⑦ | KARAKTER_VE_DUYGU §6 yürüyüş bütçesi ≥%10 | 2 sahne (S40 · S42) | 0 g + pilot 44 sahne kemerli; bütçe EL kanalına devredildi |

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE
      Savaş, onu başlatanlar gittikten sonra da makinelerin içinde sürer.

MOTİF SAHNELERİ: S3 · S17 · S31 · S44 · S47
      (makinenin tek "nefesi" = iki soğutma kanadı; insanın karşılığı = motor kolundaki el)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Savaştan kalma bir uydu, motoru yanan her şeyi üç saniye içinde vurur; iki soğutma
                     kanadı açıkken ateş edemez.
NOVUM TİPİ:          fiziksel yasa (ortamın içinde TEK kural ihlali — maya eşiği: ihlal sayısı 1)
NOVUM TAŞIYICISI:    MOTOR KOLU × pilotun eldiveni → EGZOZ KONİSİ yanan gövde üç saniye sonra dikişinden ayrılır
TEK KARE (§4①):      S0 ≈ 0:04 — "motor konisi hâlâ yanan mekik gövdesi ikiye ayrılırken, ön planda pilotun
                     eldiveni MOTOR KOLUNUN üstünde duruyor"
KİNETİK BAĞIMSIZLIK: ✅ kural replik/dış ses/ekran metni olmadan kanıtlanır — S0 (yanar → vurulur) ·
                     S3 (yanıyor, kanatlar açık → vurulmaz) · S4 (kanatlar kapanır → vurulur) ·
                     S47 (kenarın ardında yanar → vurulmaz)
BAŞLIK ŞEMASI:       "Don't Light the Engine" (4 kelime)
KURAL TEKRARI:       6 nesne · 6 farklı sonuç: mekik (S0) · arka yarı (S3-S4) · tahliye gemisinin itici kümesi (S15) ·
                     kapsül (S30) · çekicinin motor bölümü (S45) · kurtarma gemisi VURULMAZ (S47)
```

## 🧭 B5 — HİKÂYE OMURGASI (her formatta · `03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   tahliye gemisine yanaşıp havayı paylaşmak ve gemiyi gezegen kenarının ardına, kurtarma
              gemisinin erişebileceği yere taşımak (görev film başlamadan verilmiş)
   □ ENGEL:   motor ateşlemek vurulmak demek · soğuk gaz sınırlı · gemi S16'dan sonra kontrolsüz dönüyor ·
              tahliye bölmesinde hava bitiyor
   □ BEDEL:   kaçış kapsülü yem olarak salınır ve vurulur · S30   ·   çekicinin motor bölümü kopar · S45
   □ MUHATAP: ikinci insan KADRAJ DIŞI (telsizdeki yetişkin ses) + kendi geçmiş kararı (kaçış kapağını açık
              tutma alışkanlığı) + ortamın KALICI değişen parçası (boş kapsül yuvası)
    □ AYRILIK: S7 — pilot çekiciyi uzaklaştırır ↔ ses "Come back." (ret · gecikme 1,2 s)
    □ TERSİNMİŞ AYRILIK: S27-S28 — ses "Take your capsule and go." ↔ pilot kapağı kapatır, üç kez ışık
    □ ÇÖZÜM TİPİ: BOYUN EĞME — pilot kaçış yolunu bırakır; bedel onun (S30)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  Scene Foundation ana kareleri → DORUK S36-S37 → S44-S45 → merkezî seçim S29 + bedel S30 →
  kapanış imajı S47 + S46 → S0 + S3-S4 → S15-S16 → B4 → B3 → B2 → B1
  ⛔ üretim defterinin ilk KABUL satırı S36 değilse ikinci klip üretilmez
```

## 👤 KARAKTER KARTI — davranış (kart PROMPTA GİRMEZ · `KARAKTER_KARTI_VE_DAVRANIS` §1)

```
👤 ÇEKİCİ PİLOTU
ROL           ağır iş çekicisinin tek pilotu — kalın eldiven, turuncu bant, kokpit kolları        S0-S1
İSTEK         tahliye gemisine yanaşıp hava vermek, kenarın ardına taşımak                        S10
BASKI TEPKİSİ KONTROL EDER — hesaplar, bekler; fırsatı hesap yaparken kaçırır                    S5 · S17
ALIŞKANLIK    riskten önce sol başparmakla kapsül ayırma kapağına İKİ KEZ vurur                  S6 · S10 · S23
              KIRILMA: başparmak kalkar, vurmaz; eldiven doğrudan kolu kavrar                     S29
SINIR         ana motoru ateşlemez                                            S5 → pencere içinde S31 → BİLEREK S44
ZAAF          soğuk gaz ibresi ¾ → dip · yorgunluk 1 → 6 · sağ eldiven avucunda parlak sürtünme  S12-S33 · S42+
TEL           nefesini tutar — kask içi nefes kesilir, omuzlar yükselir ve kalır                  S13 · S34 · S38
İLK ↔ SON     S0 eldiven motor kolunun üstünde DONAR ↔ S44 eldiven kolu tek hamlede SONUNA İTER

👤 TAHLİYE BÖLMESİNDEKİ YETİŞKİN (yalnız ses · S46'da yalnız eldiven ve ön kol)
ROL           bölmedeki yetişkin — telsizi tutan, feneri sallayan                                  S1
İSTEK         önce pilotun gelmesi · sonra pilotun kurtulması                                      S7 → S27
BASKI TEPKİSİ ACELE EDER — beklemez, motoru kendisi ateşler                                        S15
ALIŞKANLIK    feneri iki kez yakıp söndürerek cevap verir                                          S1 · S7 · S27
ZAAF          ses nefes nefese → hırıltı → seyrek nefes                                            S9 · S29 · S35
İLK ↔ SON     S1 telsizle çağırır ↔ S46 telsizsiz, aynı sesle cevap verir

İKİ KART AYRIŞMASI (≥3 satır): BASKI TEPKİSİ · ALIŞKANLIK · İSTEK
İSTEK ÇAPRAZI: pilot ondan motoru ATEŞLEMEMESİNİ ister (S14) · o pilottan önce GELMESİNİ (S7),
               sonra GİTMESİNİ (S27) ister · NESNE: kapsül / motor kolu
KARAR MİMARİSİ: seçilen (kapsülü yem yapmak) ve REDDEDİLEN (kapsülle gitmek) aynı kadrajda — E
               kurulumunun SOL yan penceresinde kapsül S22 · S29'da görünür, S30'dan sonra BOŞ YUVA orada kalır
```

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| vuruş | % | sahne |
|---|:--:|---|
| Açılış imajı | %0-2 | S0 |
| Kurulum | %0-10 | S0-S4 |
| Katalizör | %10-15 | S5 · S6 |
| Tartışma | %15-25 | S7-S11 |
| Orta nokta | ~%50 | S24 |
| Merkezî seçim | %60 | S29 |
| Umut-önce-düşüş | %77 | S37 |
| Her şeyin kaybı | %79-81 | S38-S39 |
| Final aksiyonu | %83-94 | S40-S45 |
| Duygusal karşılık | %96 | S46 |
| Kapanış imajı | %98-100 | S47 |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:        IN MEDIAS RES (zemin: hareketin ortası — mekiğin motoru zaten yanıyor)
S0 SORUSU:        "Mekik neden vuruldu — ve pilot o kola basacak mı?"
S1 İKİNCİ BİLGİ:  vurulan mekiğin yakınında insanlar var ve pilotun onlara ulaşması gerek
İLK 2 SN SESİ:    tek diegetik katman — kabin uğultusu + kask içi nefes; müzik 0:00'da YOK
0:03 KONTROLÜ:    3,0 s'de ayrılma (ilk kareden farklı bilgi) ✅
BİLGİ ASİMETRİSİ: DRAMATİK İRONİ — izleyici kanat kuralını S3-S4'te öğrenir; tahliye gemisindekiler S15'te bilmeden yakar
AÇILIŞ↔KAPANIŞ:   KAFİYE · değişen TEK değişken: yanan motor VURULUR (S0) ↔ VURULMAZ (S47)
TOHUM:            S6 (%12,5) kapsül ayırma kapağı + çift vuruş → ödeme S29 (kırılma) · S31/S44/S47 boş yuva
KAPAK ANI:        S0 · 0:04 · ayrılan mekik camın sol üçte ikisinde, eldiven + motor kolu sağ alt üçte birde
FİNAL TİPİ:       MUĞLAK · SON PLAN TİPİ: nesne eki (boş kapsül yuvası + tarayan ışık)
```

## 🗺️ SAHNE HARİTASI

```
KURULUM İSKELETİ: A B I C C A C I Y F C I C F C J J C I G I C E C I Q Q F H E T E T A B I K K A L M N M Z E Z R Z

KÜME 4 (S3-S4 · S15-S16 · S25-S26 · S36-S37) ≥2 ✅   ·   DÖNÜŞ 20/48 = %42 ≥%40 ✅   ·   18 kurulum (üst bant 24) ✅
AÇI TİPİ 7 ≥3 ✅   ·   ARDIŞIK ÇİFT 47/47 bant içi (≥1 ölçek kademesi VE ≥45°) ✅   ·   ŞOK 0
BÖLÜM PARÇALARI:  B1 A B I C C A C I Y F C I  ·  B2 C F C J J C I G I C E C  ·  B3 I Q Q F H E T E T A B I  ·  B4 K K A L M N M Z E Z R Z
⚠️ Dosya modunda "48 harf ↔ 12 prompt" FIX'i bilinen yanlış pozitiftir; geçerli koşu KLASÖR modudur.
DAVRANIŞ ŞERİDİ (G/T/D/K/B/R/S · `-` insansız): RGTRRTKR--GD G-R--DR-DRTT GTK-RKBR-GRS RRD-DDG-KBS-
TEMPO (Y/N/H):                                  HYNNHYNHYYNN YNYHHNYNHHYN NYNYNYHNYNYY HNHNHNHYHHYY
```

| S | başlık | kurulum | vuruş | B5 | dav. | tempo | IN FRAME | replik |
|---|---|:--:|---|---|:--:|:--:|---|---|
| S0 | Motor yanar, gövde ayrılır | A | Açılış · HOOK · kural | ENGEL | R | H | hands, back | — |
| S1 | Pencerede fener | B | Kurulum · muhatap | MUHATAP | G | Y | face, hands | 12,0 s |
| S2 | Hat kayıyor | I | Kurulum · engel | ENGEL | T | N | torso | 25,0 s |
| S3 | Kanatlar açık | C | Kuralın kanıtı ① | ENGEL | R | N | hands | — |
| S4 | Kanatlar kapanır | C · küme S3 | Kuralın kanıtı ② | ENGEL | R | H | hands | — |
| S5 | Pencere kaçar | A · (S0 kurulumu) | Katalizör (%10) | İSTEK × ENGEL | T | Y | hands, back | — |
| S6 | Kaçış kapağı | C · dönüş S4 | Tartışma · TOHUM | geçmiş karar | K | N | hands | — |
| S7 | Geri çekilme | I · (S2 kurulumu) | AYRILIK | MUHATAP | R | H | torso | 73,0 s |
| S8 | Kenarın ardı | Y | Kurulum · harita | İSTEK | - | Y | none | — |
| S9 | Buğu | F | Saat başlar | BEDEL tohumu | - | Y | none | 94,0 s |
| S10 | Hortum hazır | C · dönüş S6 | Plan | İSTEK | G | N | hands | — |
| S11 | Dönüş yolu | I · dönüş S7 | Tartışma sonu | ENGEL | D | N | torso | — |
| S12 | İbre yarıda | C · dönüş S10 | B2 açılış · ilerleme | ZAAF | G | Y | hands | — |
| S13 | Enkaz geliyor | F · dönüş S9 | Tehdit | ENGEL | - | N | none | — |
| S14 | Yapma | C · dönüş S12 | İkinci ayrılık tohumu | MUHATAP | R | Y | hands | 141,5 s yetişkin (KARAR) |
| S15 | Zorunlu ateşleme | J | Vuruş · çıkmaz | ENGEL | - | H | none | — |
| S16 | Dönme başlar | J · küme S15 | Sonuç | ENGEL | - | H | none | — |
| S17 | Hazırlıksız pencere | C · dönüş S14 | Deneme 1 | ZAAF | D | N | hands | — |
| S18 | Her turda bir | I · (S11 kurulumu) | Engel büyür | ENGEL | R | Y | torso | — |
| S19 | Üç fener | G | Bahis | MUHATAP | - | N | none | — |
| S20 | Halat | I · dönüş S18 | Deneme 2 | İSTEK | D | H | torso | — |
| S21 | Halatı kes | C · dönüş S17 | Yenilgi | ZAAF | R | H | hands | — |
| S22 | Kapsüle bakış | E | Fikir | BEDEL | T | Y | face, hands | — |
| S23 | El çekilir | C · dönüş S21 | Tereddüt | geçmiş karar | T | N | hands | — |
| S24 | Önceden hizala | I · dönüş S20 | B3 açılış · orta nokta | İSTEK | G | N | torso | — |
| S25 | Tek koltuk | Q | Hazırlık | BEDEL | T | Y | hands | — |
| S26 | Zamanlayıcı kısalır | Q · küme S25 | Küçük karar | BEDEL | K | N | hands | — |
| S27 | Son fener | F · (S13 kurulumu) | Tersinmiş ayrılık | MUHATAP | - | Y | none | 272,0 s |
| S28 | Üç ışık | H | Cevap | MUHATAP | R | N | hands, back | — |
| S29 | Seçim | E · (S22 kurulumu) | MERKEZÎ SEÇİM | BEDEL | K | Y | face, hands | — |
| S30 | Kapsül vurulur | T | BEDEL | BEDEL | B | H | none | — |
| S31 | Kısa ateşleme | E · dönüş S29 | Pencere kullanılır | İSTEK | R | N | face, hands | — |
| S32 | Motorsuz | T · dönüş S30 | Bekleyiş | BEDEL | - | Y | none | — |
| S33 | İbre dipte | A · (S5 kurulumu) | Eşleşme | ZAAF | G | N | hands, back | — |
| S34 | Eğik halka | B · (S1 kurulumu) | Keşif | ENGEL | R | Y | face | — |
| S35 | Yön yok | I · (S24 kurulumu) | B3 kapanış | ENGEL | S | Y | torso | — |
| S36 | İlk temas | K | DORUK başlar · temas | İSTEK × ENGEL | R | H | torso | — |
| S37 | Üç kelepçe | K · küme S36 | Umut-önce-düşüş | İSTEK | R | N | torso | — |
| S38 | Sıkışan kelepçe | A · (S33 kurulumu) | Kayıp başlar | ENGEL | D | H | hands, back | — |
| S39 | Sızıntı | L | Her şeyin kaybı | ENGEL | - | N | none | — |
| S40 | Dışarıda | M | Final aksiyonu | kendi bedeni | D | H | full body, back | — |
| S41 | Manivela | N | Deneme 3 | kendi bedeni | D | N | hands | — |
| S42 | Kilit tamam | M · dönüş S40 | Kısmi zafer | İSTEK | G | H | full body, back | — |
| S43 | Hava yetmez | Z | B4 · saat doluyor | BEDEL | - | Y | none | — |
| S44 | Bilerek | E · (S31 kurulumu) | ÇAPA İLK↔SON · doruk | BEDEL | K | H | face, hands | — |
| S45 | Motor kopar | Z · dönüş S43 | BEDEL 2 · doruk sonu | BEDEL | B | H | none | — |
| S46 | Buradasın | R | Duygusal karşılık | MUHATAP | S | Y | face, hands, torso | 465,0 s |
| S47 | Kenarın ardında | Z · dönüş S45 | Kapanış imajı | ortamın kalıcı parçası | - | Y | none | — |

### ⚓ ÇAPA ÜÇLÜSÜ (`OYUNCULUK_YAZIM` §2 · aynı kanal · fark ≥⅛ kısa kenar)

```
CHOICE  S29 · 6,0-9,0 s   BEFORE: sol başparmak ayırma kapağının üstünde kalkık, omuzlar kalkık
                          AFTER:  başparmak vurmadan geçer, eldiven kolu kavrar ve sonuna çeker; omuzlar iner ve kalır
COST    S45 · 3,0-8,0 s   BEFORE: gövde ateşleme ivmesiyle koltuğa bastırılmış, iki eldiven kolda
                          AFTER:  kemerler gevşer, gövde öne süzülür, eldivenler koldan kayar ve havada kalır
FINAL   S46 · 5,0-9,0 s   BEFORE: sağ eldiven dizinde kapalı, omuzlar yukarıda
                          AFTER:  sağ eldiven omzundaki ele kapanır, omuzlar iner
⛔ Üçü de aynı kanalda önce/sonra: omuz hattı + el. Fark kadrajın kısa kenarının ≥⅛'i (E ve R kurulumlarında ~%15).
```

### 🧍🧍 AYRILIK KARTI · MESAFE EĞRİSİ

```
AYRILIK          S6-S7 · 60-80 s · NESNE: çekicinin rotası + açık bırakılan ayırma kapağı
A'NIN HAMLESİ    The tug backs away from the ship on short cold-gas bursts.
B'NİN CEVABI     söz (telsiz) · KARŞI TEKLİF — "Come back." · gecikme 1,2 s
MESAFE / YÖN     8 m · burun karşı karşıya → 60 m · burun ayrılmış (90°)
KİM SOLDA        çekici SOL · tahliye gemisi SAĞ (film boyu; S36-S37 kamera eksende, nötr)
BEDEL            pilot öder · S30 · S45
İKİNCİ AYRILIK   S27-S28 TERSİNMİŞ · gecikme 2,0 s · ÇÖZÜM TİPİ: BOYUN EĞME

MESAFE EĞRİSİ (gemiler arası m): S0 150 · S2 20 · S5 8 · S7 60 · S11 45 · S12 30 · S16 25 · S20 15 · S21 30 ·
S24 30 · S31 30→10 · S33 8 · S35 3 · S36 0→1,5 · S37 0 · S47 0 (kenetli)
İNSAN-İNSAN: film boyu kadraj dışı (telsiz) · S46 0,3 m — mahrem banda YALNIZ kurtarma sahnesinde girilir
```

## 🎙️ REPLİK TABLOSU (yalnız replikli filmde · `SES_VE_DIYALOG_URETIM` §1-§2a)

| # | S | saniye | konuşan | REGISTER | kanal | İngilizce (post-dub) · Türkçe | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|---|
| R1 | S1 | 12,0 | yetişkin | HUMAN | telsiz band-pass | "We're here. Can you see us?" · "Buradayız. Bizi görebiliyor musun?" | MUHATAP — kadraj dışı bilgi: birden fazla insan |
| R2 | S2 | 25,0 | yetişkin | HUMAN | telsiz | "You're going past us." · "Yanımızdan geçiyorsun." | ENGEL + alt metin: terk edilme korkusu |
| R3 | S7 | 73,0 | yetişkin | HUMAN | telsiz | "Come back." · "Geri dön." | AYRILIK — karşı teklif |
| R4 | S9 | 94,0 | yetişkin | HUMAN | telsiz | "The air won't last." · "Havamız yetmez." | BEDEL/zaman — kadraj dışı bilgi |
| R5 | S14 | 141,5 | yetişkin | HUMAN | telsiz | "I have to light the engine." · "Motoru çalıştırmak zorundayım." | KARAR — S15'in sebebi |
| R6 | S14 | 144,0 | pilot | HUMAN | kask içi | "Don't." · "Yapma." | İSTEK ÇAPRAZI — pilotun tek sözü |
| R7 | S27 | 272,0 | yetişkin | HUMAN | telsiz | "Take your capsule and go." · "Kapsülünle git." | TERSİNMİŞ AYRILIK |
| R8 | S46 | 465,0 | yetişkin | HUMAN | telsizsiz, oda | "You're here." · "Buradasın." | ÇİFT — R1'in cevabı |

```
İLK REPLİK:     S1 · 12,0 s · öncesindeki kesintisiz sessizlik 12 s · vuruş: MUHATAP'ın girişi
BEDENLEŞTİRME:  □ yarım — S46 (telsiz filtresi kalkar, ağız yine kadraj dışı) [§1a.1]
DIALOGUE LINES: 0 (klipte üretilen tırnaklı replik) · POST-DUB LINES: 8
⛔ Promptta tırnak YOK; AUDIO "one short burst of radio static from the helmet speaker, no words."
⛔ Sayı söyleyen replik 0 [D82] · duygu adı 0 · konuşan ağız 0 klip · replik <5 s
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md (Kart P 2b)
```

**DEĞİŞ-TOKUŞ TABLOSU** (`DIYALOG_SAHNESI` §2 — DEĞİŞİM boş replik silinir)

| # | HAMLE | CEVAP kanal · içerik | GECİKME | DİNLEYENİN BEDENİ | DEĞİŞİM |
|---|---|---|:--:|---|---|
| R1 | ses · görülmek | eylem · uyma (kokpit lambası bir kez) | 1,0 s | profil pencereye kilitli, eldiven anahtara | BİLGİ + |
| R2 | ses · durması | sessizlik · erteleme (motor kolu kapalı) | >2,5 s (S5) | kanopide gövde kıpırtısız, sağ omuz öne | GÜÇ → ses |
| R3 | ses · geri dönmesi | eylem · ret, S11'de uyma | 1,2 s · ödeme S11 | çekici geri çekilmeyi sürdürür | MESAFE +52 m |
| R4 | ses · acele | eylem · kısmi uyma (S10 hortum) | S10 ilk saniye | eldiven hortumu askıya takar | BİLGİ + (saat) |
| R5 | ses · bildirim | söz · ret ("Don't.") | 1,0 s | eldiven itici kolunda donar | NİYET — ilk açık çatışma |
| R6 | pilot · yakmaması | eylem · görmezden (S15 motor yanar) | S15 0,0 s | (insan kadrajda yok) | GÜÇ → ses; bedel gemiye |
| R7 | ses · pilotun kurtulması | eylem · ret (kapak + üç ışık) | 2,0 s | sol eldiven kapak kolunda, sonra anahtarda | NİYET tersine döner |
| R8 | ses · cevap | eylem · uyma (eli tutar) | 1,0 s | omuzlar iner, el yukarı gider | MESAFE 0,3 m · R1 kapanır |

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız o karenin `IN FRAME:`
> satırındaki kısmı gider. "BIBLE'a bak" atfı YASAK, ama self-contained ≠ Bible'ın tamamı: kadrajda olmayan
> YAZILMAZ. Videoya Bible girmez — `START FRAME:` tek satır.

### 👤 Character Bible

```
SUIT (IN FRAME: torso / full body / back):
She wears a heavy industrial pressure suit of worn off-white canvas with vertical quilted padding down the
torso and thighs, broad padded shoulder caps rising to the collar, one safety-orange band wrapped around the
LEFT upper arm and one around the LEFT thigh, dark bronze joint rings at the elbows and knees, heavy
segmented dark-grey gloves and boots.

HELMET (IN FRAME: face · back):
The helmet is a rounded hard off-white shell seated deep in a raised bronze collar ring, two small square
lamps set into the brow, a single flat front pane inside a thick dark-grey rim, a soft neutral 4500K fill
from inside the rim on her face, her face fully readable through the clear pane.

BACK (IN FRAME: back · over-the-shoulder):
The back of the suit is one continuous ribbed surface from collar to hip, closed and smooth, the two shoulder
caps wrapping over its upper edge.

FACE (yalnız IN FRAME: face · ≤3 öznitelik [D167]):
a woman in her mid-forties with a broad square jaw and set lines at rest

WEAR (S42'den sonra): the right glove's palm carries a bright rubbed patch where it pressed the clamp.

SECOND PERSON (yalnız S46): one dark-grey glove and forearm of a second suit reaching in from the right edge
of the frame — no face, no body.
```

### 🌍 World Bible

```
BIOME        hard vacuum in low orbit over a large rust-and-grey planet
SKY          a flat black sky with no stars
BODY         one large rust-and-grey planet, its curved bright edge crossing the lower part of the frame
HORIZON      that curved edge is the only horizon; the biggest thing in every exterior frame
ANCHOR ×3    (DÜNYA ÇAPASI — her dış promptta BİREBİR, kısaltılmadan)
             ① "A flat black sky with no stars."
             ② "The curved bright edge of a large rust-and-grey planet crosses the lower part of the frame."
             ③ "One small steady white light hangs above that edge on the right and blinks once every two seconds."
PERSPECTIVE  no haze and no falloff: the far hull is as sharp and as contrasty as the near one
SUN SIDE     hard sunlight from the upper left, the sun itself out of frame, in every exterior setup
CHANGE       yok — tek ortam; iç bölgeler (kokpit · kapsül · tahliye bölmesi) ayrı ışık bölgesidir (§ Lighting)
INTERIOR     cockpit: a short boxy cabin, a three-panel canopy across the front, a left console at hip height,
             a capsule cradle outside the left flank visible through the side window
```

### 🎥 Camera Bible

> 18 kurulum. Cümle KARAKTER KARAKTER kopyalanır (sayı biçimi dahil). Her CAMERA cümlesi OMNI katmanıyla biter:
> "In a single continuous shot." Kamera kelimesi aksiyon satırına SIZMAZ. Mesafe cümlesinde "behind" yok ("back from").

```
A  CAMERA: 35mm lens on a fixed locked-off mount at shoulder height, 1 m back from her right shoulder, over-the-shoulder medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
B  CAMERA: 50mm lens on a fixed locked-off mount at eye height, 1 m from the right side of her helmet, side-on profile close-up, absolutely zero camera movement. In a single continuous shot.
C  CAMERA: 50mm lens on a fixed locked-off mount at chest height, 0.8 m from the left console, high angle close-up, absolutely zero camera movement. In a single continuous shot.
E  CAMERA: 28mm lens on a fixed locked-off mount at eye height, 1.5 m from her visor on the windscreen side, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
H  CAMERA: 50mm lens on a fixed locked-off mount at shoulder height, 0.6 m back from her left shoulder, over-the-shoulder close-up, absolutely zero camera movement. In a single continuous shot.
Q  CAMERA: 35mm lens on a fixed locked-off mount at chest height, 0.8 m from the timer dial, high angle close-up, absolutely zero camera movement. In a single continuous shot.
R  CAMERA: 35mm lens on a fixed locked-off mount at eye height, 1.5 m from her, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
Y  CAMERA: 24mm lens on a fixed locked-off mount level with the tug, 400 m from the long ship, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
Z  CAMERA: 24mm lens on a fixed locked-off mount level with the docked ships, 30 m from the docked ships, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
F  CAMERA: 50mm lens on a fixed locked-off mount level with the windows, 12 m from the long ship's windows, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
G  CAMERA: 85mm lens on a fixed locked-off mount a little below the windows, 8 m from the windows, low angle close-up, absolutely zero camera movement. In a single continuous shot.
I  CAMERA: 35mm lens on a fixed locked-off mount level with the tug, 30 m from the tug, eye-level medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
J  CAMERA: 35mm lens on a fixed locked-off mount level with the long ship, 35 m from its flank, side-on profile medium shot, deep focus, absolutely zero camera movement. In a single continuous shot.
K  CAMERA: 35mm lens on a fixed locked-off mount on the long ship's docking ring, 15 m from the tug's nose ring, eye-level wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
T  CAMERA: 35mm lens on a fixed locked-off mount above the tug, 40 m from the tug, high angle wide shot, deep focus, absolutely zero camera movement. In a single continuous shot.
L  CAMERA: 85mm lens on a fixed locked-off mount above the collar, 3 m from the docking collar, high angle close-up, absolutely zero camera movement. In a single continuous shot.
M  CAMERA: 24mm lens on a fixed locked-off mount below her boots, 8 m from her, low angle medium long shot, deep focus, absolutely zero camera movement. In a single continuous shot.
N  CAMERA: 50mm lens on a fixed locked-off mount above her hands, 1.2 m from her gloves, high angle close-up, absolutely zero camera movement. In a single continuous shot.
```

```
DÖNÜŞ İŞARETİ (araya kurulum girmiş):  "— the same position, height and lens as Scene N."
KÜME İŞARETİ (ardışık):                "continues the previous clip from its exact last frame — the same
                                        position, height and lens as Scene N."
```

### 💡 Lighting Bible

```
KAYNAK      dışarıda TEK sert güneş (kadraj dışı, sol üst) + gezegen kenarından soğuk ikincil yansıma;
            içeride tavan paneli 4500K + kask içi 4500K rim fill
YÖN         güneş dünya koordinatında sabit: "hard sunlight from the upper left, the sun itself out of frame";
            kurulum başına ekran yanı değişmez
TAKVİM      yok — film gerçek zamanlı ~8 dakika; tek sabit satır
RENK BANDI  4500K iç · nötr beyaz güneş · gezegen yansıması soğuk (plana; gövdede "cool" kelimesiyle)
PRATİKLER   tahliye penceresinde fener 3 → 2 (S23) → 1 (S26) → 0 (S38) · çekicinin kaş lambaları 2 (sabit) ·
            uydunun tek beyaz sensör ışığı (2 s'de bir yanıp söner) · kokpit lambası (S1 · S28 sinyal)
KONTRAST    "the shadow side of every surface stays pure black"; iç hacimde "faint bounce from the pale panels"
⛔ glow · glowing · volumetric · god rays · lens flare · rim light · cinematic lighting YAZILMAZ
```

### ⚙️ Physics Bible

```
YERÇEKİMİ   tek g = 0 — her yerde. Bırakılan hiçbir şey düşmez; kemerli pilotun kolları bir avuç süzülür.
DIŞ SES     yok. Dış kadrajda yalnız telsiz taşıyıcı hışırtısı; iç kadrajda kabin uğultusu + kask içi nefes;
            gövdeye değen her şey (kelepçe, darbe, kopma) İÇERİDEN duyulur.
SOĞUK GAZ   "a brief straight transparent cone that is gone within a quarter second" — bulut yok, kıvrım yok.
EGZOZ       ana motor: düz beyaz koni, kenarı keskin, hızla seyrelir; kıvrılmaz, kabarmaz.
VURUŞ       ateşleme → 3,0 s → vurulma. Tek beyaz nokta çakması ≤6 kare, yumruk büyüklüğünde, sonra 0 kare artık
            ışık; vurulan parça dikişinden ayrılır, kazandığı dönüşü sürdürür ("about one turn every three
            seconds, never slowing"); ayrılma yerinden düz çizgili buz kristali konisi 2,0 s içinde seyrelir;
            ana gövde ters yöne küçük bir tepki dönüşüne girer.
DÖNEN GEMİ  tahliye gemisi S16'dan sonra "one full turn about every twenty seconds, always the same way";
            kanıt arka planda gezegen kenarının tek yönde süzülmesi.
HALAT       yük altında ANINDA düz ve gergin; kesilince ucu düz uçar, dalgalanmaz.
İTKİ        ateşleme süresince kabinde her şey KIÇA doğru tek yönde; motor susunca süzülme geri gelir
            (ikisi aynı klipte değil).
TEMAS       katı gövdeler birbirine geçmez: "the two rings meet, the tug bounces back an arm's length".
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin ortam/tür/risk yasakları

> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (image 7 · video 8 cümle) + bu listeden sahne başına
> ≤3 cümle taşır (㉗). İnsansız sahnelerde NEGATIVE ≤900 karakter (red defteri #2 · 04_UYARI R6).

```
N1  no explosion, no blast, no fireball, no flame, no smoke, no burning debris
N2  no beam, no laser, no tracer, no visible projectile, no muzzle flash, no weapon on screen
N3  no exterior sound of any kind in vacuum
N4  no curling or swirling gas, no vapour cloud, no mist, no haze in vacuum
N5  no stars in frame while the sun is up
N6  no miniature or toy-model read, no vertical band of blur across the frame, no shallow depth of field on the structures
N7  no bodies passing through one another, no merging hulls, no phasing rings
N8  no second tug, no duplicate ship, no extra figure in the cockpit
N9  no readable text, digits, scale marks, graduation ticks, HUD lines or icons on any screen, gauge, hull or panel
N10 no bare skin above the collar, none at the wrist, none at the ankle (S46 hariç: kask açık, yüz ve boyun meşru)
N11 no backpack, no tank, no hose or cable on the back of the suit (sırt POZİTİF cümlesiyle yazılır)
N12 no camera shake, no handheld, no push-in, no zoom, no rack focus
N13 no title card, no end card, no credits, no caption, no subtitle, no watermark
N14 no gore, no blood, no wound, no body — tahliye gemisinin içi hiçbir karede gösterilmez
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| ateşleme → vuruş gecikmesi | 3,0 s | 6 · 12 | S0 · S15 · S30 · S45 |
| vuruş çakması | ≤6 kare (0,25 s) · yumruk büyüklüğü · sonra 0 kare artık ışık | 6 | vuruş sahneleri |
| buz kristali konisi | ≤2,0 s'de seyrelir, düz çizgili | 6 | vuruş sahneleri |
| kopan parça dönüşü | ~3 s'de bir tur, yavaşlamaz | 6 · 13 | S0 · S4 · S15 · S30 · S45 |
| uydu kanat aralığı | 2 kanat · ≈15 s açık | 5 | S3-S5 · S17 · S31-S32 · S44 |
| tahliye gemisi dönüşü | 1 tur / 20 s, tek yön | 13 | S16-S37 |
| soğuk gaz püfü | ≤0,25 s, düz koni | 6 | S6 · S11 · S12 · S17 · S24 · S33 |
| soğuk gaz ibresi | ¾ → ½ → dibe bir parmak → dip (4 kademe, geri çıkmaz) | 5 | S6 · S12 · S21 · S33 |
| tahliye penceresinde fener | 3 → 2 → 1 → 0 (yalnız sınırda) | 5 | S1 · S23 · S26 · S38 |
| uydu ışığı ↔ gezegen kenarı | 1/4 → 1/12 → 1/20 → 0 kare yüksekliği | 5 | S8 · S43 · S45 · S47 |
| kenet kelepçesi | tam 4 (S37'de 3 kapanır, S42'de 4.) | 13 | S37 · S38 · S41 · S42 |
| kanopi pencere paneli | tam 3 | 13 | çekicili kadrajlar |
| tahliye penceresi | tam 3 | 13 | F · G |
| uydu anatomisi | 1 ray gövdesi · 2 kanat · 1 sensör ışığı | 13 | C ekranı |
| çekici anatomisi | 1 burun halkası · 4 kelepçe yuvası · 1 ana motor · 4 itici kümesi · 1 kapsül yuvası | 13 | I · T · K · Z |
| insan sayısı | 1 (S46: 1 + bir eldiven/ön kol) | 4 | tüm film |
| kask durumu | kapalı S0-S45 · AÇIK S46 (sahneye açık girer) | 3 · 12 | S46 |
| klip · süre | 48 klip × 10 s = 480 s (±2 s) | 11 | kurgu kapısı |
| ekran metni | 0,0 s | 5 | kurgu kapısı |
| replik | klipte 0 · post-dub 8 | 7 | replik tablosu |
| ölçek kanıtı | ana nesne ≥100 px (en düşük: boş yuva 102 px · itici 107 px) | 13 | 03 §4 kartları |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D192 | vuruş: ışın/mermi 0 · çakma ≤6 kare · ayrılma + dönüş + ≤2 s düz kristal konisi · gövde tepki dönüşü | S0 · S4 · S15 · S30 · S45 |
| D213 | temas · değişim · sonuç (≥1 s, merkez üçte bir) aynı klipte; ateşleme → 3,0 s → vuruş | S0 S4 S15 S30 S36 S37 S42 S45 |
| D200 | tek g = 0; soğuk gaz düz koni ≤0,25 s; kabinde hiçbir şey düşmez; ateşleme sırasında tek yön | tüm film |
| D198 | kopan/salınan her parça dönme oranıyla yazılır, yavaşlamaz | S0 S4 S11 S13 S15 S30 S45 |
| D209 | DÜNYA ÇAPASI üç cümle her dış promptta BİREBİR | tüm dış kadrajlar |
| D193 | güneş sabit (kadraj dışı sol üst) · iç 4500K · pratik sayaçlar yalnız sınırda değişir | tüm film |
| D78 | üç sayaç tek karede sayılır: kanatlar · ibre · fener (+ uydu ışığı yüksekliği) | S3-S5 S12 S17 S21 S23-S27 S31-S33 S38 S43-S47 |
| D157 | TEK KARE S0: yanan koni + ayrılan gövde + motor kolundaki eldiven aynı karede | S0 · kural tekrarı 6 nesne |
| D179 | IMAGE t=0 = ÖNCE hâli (koni yanıyor, gövde bütün; kapsül yuvada; halka düz) | S0 S15 S29 S30 S36 S44 S45 |
| D202 | ÇAPA ÜÇLÜSÜ: S29 omuz+el · S45 gövde+kemer · S46 el; reddedilen kapsül kadrajda kalır | S29 · S45 · S46 |
| D210 | her CAMERA "fixed locked-off … absolutely zero camera movement. In a single continuous shot." + TIMELINE son satırı sürdürme | 48 prompt |
| D146 | kask cümlesi film boyu birebir; "seamless/bubble/dome" 0; yüz yalnız 7 sahnede | B · E · R kurulumları |
| D69 | eşik geçişi kadraj DIŞI: S25 içeride, S40 dışarıda, S42 kapağa doğru, S46 bölmede başlar | S25 · S40 · S42 · S46 |
| D174 | yön nesneyle: çekici SOL, tahliye SAĞ; "toward the long ship on the right"; fren alevi gidilen yöne | tüm dış kadrajlar |
| D203 | replik klipte üretilmez (post-dub 8); promptta tırnak 0; SPEC DIALOGUE LINES 0 | S1 S2 S7 S9 S14 S27 S46 |
| D217 | her repliğin İŞLEVİ görünmeyeni taşır (karar · kadraj dışı bilgi · istek) | replik tablosu |
| D168 | üretim sırası: doruk → bedel → final → hook → kalanı; ilk KABUL S36 | üretim defteri |
| D123 | silah/patlama/yara sözlüğü NEGATIVE dahil 0; uydu formuyla, vuruş malzemeyle | tüm film |
| D139 | sırt görünen her kadrajda POZİTİF sırt cümlesi | A · H · M kurulumları |
| D206 | BEDEL EĞRİSİ `<kanal @ saniye>`: S20 ön kol @2 s · S38 omuz @4 s · S40 ön kol @1 s · S41 gövde @3 s · S44 gövde @2 s | efor sahneleri |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle (boşsa "—")

| ders | neden bu filmde uygulanmadı · içeriği nerede |
|---|---|
| D1 | tek çekim — çekirdek ① + OMNI cümlesi zaten her promptta (D210 satırına katlandı) |
| D16 · D167 | yüz morph · kimlik yığını — Character Bible FACE satırı ≤3 öznitelik, yalnız IN FRAME face |
| D34 · D70 · D211 | jenerik/başlık kartı · ilk-son 10 s — kurgu kapısı üç sayı + S47 "the take ends on the held frame" |
| D42 | yıpranma — SPEC C KİMLİK DİZİSİ (eldiven avucu S42'den sonra) |
| D45 · D138 | künye/ölçü sızması — metre yalnız PLAN/SPEC, promptta gövde boyu |
| D62 · D141 | final düşer · vuruş yok — KESİLEMEZ listesi + SPEC B FİNAL VURUŞ KANITI |
| D104 | ışık mıknatısı — güneş kadraj dışı; D174 satırına katlandı |
| D172 | askı düzeneği — halat ve hortum eylem nesnesi, kadrajda başka sarkan kablo yok |
| D175 · D214 | mühür · kadrajda olmayan beden — üç bölge negatifi + IN FRAME ilk satır |
| D176 | kontrast garantisi — gezegen rengi TEK cümlede (DÜNYA ÇAPASI) |
| D180 · D216 | planlı sessizlik · ses miksi — S45 sonrası 2 s sessizlik KURGUDA; MUZIK katman ≤4 |
| D207 | yorgunluk — sahne tablosu yorgunluk 0-6 sütunu |
| D208 | kimlik dizisi — SPEC C |
| D212 | ardışık aynı vuruş — sahne haritası vuruş sütununda tekrar 0 |
| D215 | ekran metni/filigran/ağız — üretim defteri üç kutu |
| D59 | insansız + yokluk listesi — NEGATIVE ≤900 karakter (04_UYARI R6) |
| D32 · D58 | yapı oranı · tekrar eden varlık — ANATOMİ sayıları (sayısal kilit listesi) |
| D82 | sayı söyleyen replik — replikte sayı 0 |
| D89 | bedenden çıkarma — S46 kask sahneye açık girer |
| D127 | ivme yerine süre — kopan parçanın kadrajı terk etme süresi saniyeyle |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S15 (insanlı tahliye gemisi vuruluyor)
NÖTR TARİFİ:         "a thruster pod on the long ship's right flank separates along its seam and turns away end
                     over end; a short cone of ice crystals spreads in straight lines and thins; the hull begins
                     a slow turn the other way"
İKİNCİ:              S46 (kasksız yüz + ikinci insanın eli) — kask sahneye AÇIK girer, el t=0'da omzun bir avuç yakınında
ÜÇÜNCÜ:              S30 (kapsül vuruluyor) — yakın plan yüz aynı sahnede DEĞİL (yüz S29, vuruş S30)
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| silah adlandırılmaz, ateşin kendisi görünmez | "neyle vuruldu" görüntüsü | ② malzeme sonucu (dikişten ayrılma + kristal konisi) + ③ alet tepkisi (kanatlar açılır) |
| patlama · alev · duman 0 kare | aksiyonun görsel "patlaması" | ① kütle-hız: parçanın dönüşü + ana gövdenin tepki dönüşü |
| insanlı gemide insan 0 kare | tehlikenin yüzü | ④ temassız gövde tepkisi (pilotun nefesi durur) + penceredeki fener sayısı |
| kask çıkarma eylemi 0 | S46'nın "kaskını açar" jesti | kask sahneye açık girer; vuruş omuzdaki ele taşındı |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
⛔ REFERANS PAKETİ YAZILMADI — sahip kararı 17.09.2026; 5/6 tetikleyici doğru (02 §5b), telafi ANATOMİ KARTI
   sayıları + Scene Foundation ana kareleri, kalan risk 04_UYARI R2 [D74 ⑥].
```

## 🧭 SPATIAL MAP — plana, prompta girmez (`UZAMSAL_HARITA_VE_EKRAN_YONU` §3 · §8)

```
            uydu ışığı ◑ (gezegen kenarının üstünde, SAĞ üst)
   ┌──────────────────────────────────────────────┐
   │   ▣ ÇEKİCİ (burun sağa)   →→→   ▬▬▬ TAHLİYE  │
   │                                  GEMİSİ      │
   │  ○ kurtarma gemisi (SOL, kenarın ardında)    │
   │ ════════ gezegenin kıvrık aydınlık kenarı ═══│
   └──────────────────────────────────────────────┘
        ▲ KAMERA — eksenin GÜNEY yarısı, film boyu (K yalnız eksende, nötr)
AKSİYON EKSENİ : ÇEKİCİ → TAHLİYE GEMİSİ
EKRAN SONUCU   : çekici HEP ekran SOLUNDA · tahliye gemisi SAĞINDA · uydu ışığı SAĞ ÜSTTE ·
                 gezegen kenarı ALT · kurtarma gemisi SOL KENAR
YÖN TAŞIYICILARI: güneş sol üstten (kadraj dışı) · gezegen kenarının süzülme yönü tek (dönen gemide)
HANGİ UÇ ÖNDE  : çekici burnu (halka) önde — "its nose, with the ring, leads; the engine end trails"
FREN YÖNÜ      : yavaşlayan çekicide püf GİDİLEN yöne (sağa) çıkar
```

---

## ✅ KAPI KAYDI

```
☑ 00_ANALIZ altı adım kapalı (çizelge 109/109 · hasat 20 kilit · konsept ✅✅✅ · sıralama 47/47 · uyarı R1-R9 ✅ · tablo 48 ✅ + 5 kilit dosya)
☑ KURULUM İSKELETİ satırı PLAN'da (⑩④ kapısı koşar)
☑ TEMA satırı tek kelime · MOTİF 5 sahne
☑ B5 dörtlüsü + AYRILIK + ÇAPA ÜÇLÜSÜ + KARAKTER KARTLARI yazıldı
☑ Bible'lar (Character · World · Camera 18 · Lighting · Physics · Negative N1-N14)
☑ politika satırı + telafi tablosu + D74 kayıtları (7 satır)
⬜ BOLUM_1-4 promptları · QA_SPEC · MUZIK · KAPAK · YAYIN_PAKETI · URETIM_DEFTERI
⬜ prompt_kontrol klasör modu · DIALOGUE_CRITIQUE (Kart P 2b)
⬜ SAHİP: K1 QA birimi · K2 S36-S37 zincir modu · K3 klip süresi (ffprobe)
```
