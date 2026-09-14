# 🎬 THE_HARD_DOCK — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur.
>
> **Revizyon 11.09.2026 (kart P koşusu):** ilk yazım kapıdan BLOCK aldı — bölüm
> dosyaları şablon kopyasıydı (BÖLÜM 2 = BÖLÜM 1'in ACTION satırları), vizör iki
> hâlde birden yazılmıştı (D197'nin tam kendisi), 1.5 rad/s kilidi kendi A5
> satırıyla çelişiyordu (1.5 rad/s = 6 s'de 516°, 45° değil). Bu plan o koşunun
> düzeltilmiş hâlidir; sapma kayıtları §"BİLİNÇLİ SAPMALAR"da.

```
FORMAT:        yatay 3-5 dk (§2.3 kartı)
ORTAM:         uzay §3.1 kartı (vakum) + §3.10 kokpit iç hacmi (basınçlı kabin, mühürlü giysi)
TÜR:           bilimkurgu · sert bilimkurgu (§4.1)
KLİP SÜRESİ:   10 s (8 s üret + 2 s uzat) — ⬜ ARAÇTAN ÖLÇÜLECEK [D124], ilk test klibinde ffprobe
SAHNE SAYISI:  24        RUNTIME: 04:00 (240 s = 24 × 10 s · hook ayrı sahne değil, S01 hook'tur)
BÖLÜM:         BOLUM_1 S01-S12 · BOLUM_2 S13-S24
LOGLINE:       Yalpalayan, hasarlı bir röle istasyonuna kenetlenmeye çalışan tek kişilik
               servis gemisinin pilotu, sensörleri kör olan gemi bilgisayarının "iptal et,
               dönüş yakıtı 90 saniye" direktifine rağmen istasyon rölesini kurtarmak için
               geminin kenetlenme halkasını nominal hızın beş katıyla porta sürer — halka
               bir daha açılmamak üzere kilitlenir; röle yaşar, gemi bir daha ayrılamaz.
```

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE — hayatta kalma optimumunu hesaplayan makine ile bedeli
      göze alan insan sorumluluğu arasındaki çatışma (makine "dön" der, insan kalır).

MOTİF SAHNELERİ: S03 · S06 · S10 · S15 · S17 · S19 · S24
      (makinenin sesi her seferinde bir SAYI söyler; insanın cevabı her seferinde
       bir JESTTİR — S17'de makine "dön" der, S19'da el korumayı kaldırır)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Yalpalayan istasyona yumuşak kenetlenme imkânsızdır; tek yol geminin
                     yaylı kenetlenme halkasını nominal hızın beş katıyla porta sürmektir —
                     dört dikme dibe vurur, halka bükülür ve kilit GERİ ALINAMAZ (sert kenet).
NOVUM TAŞIYICISI:    Geminin dört dikmeli kenetlenme halkası × halkanın nominal hızın beş
                     katıyla porta sürülmesi → dikmeler dibe vurur, halka yakası bükülür, gemi
                     bir daha ayrılamaz.
TEK KARE (§4①):      S23 · 0,0 s karesi — geminin kenetlenme halkasının DÖRT DİKMESİ tamamen
                     çökmüş, halka yakası portun içine bükülmüş, gemi portta hareketsiz; arkada
                     gezegen kayıyor (istasyonla birlikte dönüyor). Halka ve dikmeler kadrajın
                     konusudur [D157].
KİNETİK BAĞIMSIZLIK: S22'de dört dikme tek hareketle sonuna kadar çöker ve gemi bir daha
                     kımıldamaz; S23'te arka plan kayarken gemi porta göre sabittir —
                     replik olmadan okunur.
BAŞLIK ŞEMASI:       THE HARD DOCK (3 kelime) — "sert kenet" terimin kendisidir.
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5)

```
B5 □ İSTEK:   İstasyona kenetlenip röle taşıyıcısını geri getirmek — film başlamadan var
              olan bir İŞ (S02'de eldivenler zaten kumandalarda, yanaşma başlamış).
   □ ENGEL:   İstasyonun yalpalaması (48 s'de bir tam salınım; port her salınımda yalnız
              6 s hizada) + koronal akı altında gemi sensörlerinin körleşmesi (%50 → %0).
   □ BEDEL:   Sert kenet halkayı geri alınamaz biçimde kilitler; gemi bir daha ayrılamaz,
              dönüş yakıtı işe yaramaz · bedelin GÖRÜLDÜĞÜ sahne S22 (dikmeler çöker) ·
              adının KONDUĞU sahne S24 (makine: "Release struts destroyed.")
   □ MUHATAP: MIRA — gemi bilgisayarı, akuzmatik; film boyunca bedensiz kalır (§1a.1:
              bedenleştirme YOK — hoparlör, ağız yok, ekran yok).
B5b □ AYRILIK: S17 — makine "Abort approach." der; insan başını iptal koluna çevirir ve
              çevirmez (S18 tereddüt · S19 karar). İki insan yok; muhatap makine.

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR]:
  REFERANS PAKETİ (R1 giysi/kask · R2 port+halka) → S22 (DORUK · temas) → S23 (tek kare)
  → S19 (merkezî seçim) → S24 (kapanış imajı) → S01 (hook) → kalanı
```

## 👤 KARAKTER KARTI — pilot (`KARAKTER_KARTI_VE_DAVRANIS` §1 · prompta GİRMEZ, promptu besler)

```
ROL            tek kişilik servis gemisinin pilotu/röle teknisyeni — giysi, iki kumanda
               kolu ve koruma kapaklı tetik onu tanıtır                        S02
İSTEK          kenetlenip röleyi geri getirmek (iş başlamış hâlde açılır)     S02 · S08
BASKI TEPKİSİ  KONTROL EDER — her uzanmadan önce baş kumandaya döner, el bir an
               durur, sonra gider (bakış eli önceler)                          S08 · S10 · S18
ALIŞKANLIK     her kumanda girdisinden önce sağ işaret parmağı T-kolu İKİ kez tıklatır
               S02 · S08 · S10 — S19'da KIRILIR: el tıklatmadan doğrudan korumaya gider
SINIR          röleyi ölü bırakıp dönmez — film onu S17'de bu çizgiye getirir
ZAAF           S12 iptalinden sonra omuz hattı yüksek kalır ve S20'ye kadar inmez
               (nefes omuzda okunur, sık ve sığ); S20'de tek seferde iner        S12 · S18 · S20
TEL            baskı altında BAŞ KİLİTLENİR, yalnız gözler hareket eder            S09 · S11 · S20
İLK ↔ SON      S02: iki eldiven iki kumandada kapalı, omuzlar yüksek
               S24: iki eldiven açık, uyluklarda, omuzlar inik — tek fark: eller bıraktı
```

## ⚓ ÇAPA ÜÇLÜSÜ (`OYUNCULUK_YAZIM` §2 · ⑩ mod D ANCHOR BEATS buradan okunur)

```
CHOICE  S19 · 4,0 s   BEFORE: sağ eldiven T-kolda kapalı, başparmak kolun üstünde;
                      çizgili koruma kapağı KAPALI; sarı-siyah iptal kolu kadrajın solunda dik
                      AFTER:  sağ eldiven koruma yuvasında, kapak AÇIK, işaret parmağı düğmede;
                      iptal kolu aynı yerde, dokunulmamış
COST    S22 · 6,0 s   BEFORE: geminin dört kenetlenme dikmesi tam uzunlukta, halka yakası yuvarlak
                      AFTER:  dört dikme sonuna kadar çökmüş, yaka portun içine bükülmüş,
                      gemi porta göre hareketsiz (bedelin GÖRÜLDÜĞÜ kanal: geminin gövdesi)
FINAL   S24 · 7,0 s   BEFORE: iki eldiven iki kumandada kapalı, omuz hattı yüksek
                      AFTER:  iki eldiven açık, uyluklarda; omuz hattı inik ve inik kalır
DAVRANIŞ ŞERİDİ (yalnız insanlı sahneler; "–" insansız):
  S01 – · S02 G · S03 R · S04 S · S05 – · S06 – · S07 – · S08 G · S09 G · S10 G · S11 T · S12 D
  S13 – · S14 – · S15 – · S16 – · S17 R · S18 T · S19 K · S20 B · S21 G · S22 – · S23 – · S24 R
  G 5/14 (%36 ≤ %50) · T 2 · D 1 · K 1 · B 1 · R 3 · S 1 · K'dan önce T+D var · K'dan sonra B · ilk G ≠ son R
KARAR MİMARİSİ: S19 kadrajında iki nesne — koruma kapaklı tetik (seçilen) ve iptal kolu
  (reddedilen); reddedilen S19'dan sonra da kadrajda (S24'te dik duruyor). Başarısız deneme:
  S12 (ilk yanaşma iptal — pencere kaçtı). Bedel penceresi: S22 temasla aynı klipte.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | S0 anomali — yalpalayan istasyon | 4% | S01 | |
| 2 | ortam / tehdit yükselişi — pencere, röle kaybı, oran | 17% | S02-S06 | |
| 3 | birinci manevra — manuel yanaşma başlar | 33% | S07-S10 | |
| 4 | orta nokta / kriz — pencere kaçar, iptal (wave-off) | 50% | S11-S12 | |
| 5 | ikinci kriz — sensör sıfır, port hasarı görülür | 67% | S13-S16 | |
| 6 | ayrılık / tırmanış — "abort", tereddüt, karar | 79% | S17-S19 | |
| 7 | doruk — ikinci yanaşma ve sert kenet | 92% | S20-S22 | |
| 8 | çözülüş / kafiye — tek kare + eller bırakır | 100% | S23-S24 | |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       ANOMALİ REVEAL — geminin burun kamerasından, önümüzde yalpalayan dev istasyon
S0 SORUSU:       "Bu şeye nasıl kenetlenilir?"
S1 İKİNCİ BİLGİ: (S02) makine sayıyı söyler: 48 saniyede bir tam salınım; pencerede kopan
                 panel geçer — istasyon dağılıyor
İLK 2 SN SESİ:   telsiz taşıyıcı hışırtısı + kabinden iki tonlu alçak uyarı sesi (2 s'de bir)
AÇILIŞ↔KAPANIŞ:  KAFİYE · S02 ↔ S24 aynı kurulum (B): pencerede küçük, dönen istasyon ↔
                 pencereyi dolduran sabit port; eller kumandada ↔ eller uylukta
```

---

## 🗺️ SAHNE HARİTASI

> Kurulum harfleri: A dış-burun · B iç-OTS · C iç-yüz · D iç-el · E dış-oran (V3, 1 kez) ·
> F dış-tepe · G dış-port-kilitli (V5/V6, D104). Ölçek merdiveni EWS-WS-MS-CU-ECU:
> A WS · B MS · C CU · D ECU · E EWS · F EWS · G WS — ardışık her çift TAM 1 kademe.

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe / şerit |
|---|---|---|---|---|---|
| S01 | Yalpalayan istasyon ⭐ | Burun kamerası: istasyon önümüzde, port ucu geniş bir daire çizer; gezegen altta | A · 32mm · WS · göz hizası frontal | taşıyıcı + kabin uyarı tonu | – |
| S02 | Kumandalar | OTS: pencerede istasyon; kopan radyatör paneli pencereyi sağdan sola geçer; MIRA #1 | B · 35mm · MS · OTS | MIRA #1 (3,0 s) | G |
| S03 | Röle kaybı | Yüz: MIRA "relay carrier lost"; gözler konsola iner, çene sıkılır, geri kalkar | C · 50mm · CU · alt açı | MIRA #2 (3,0 s) | R |
| S04 | Nefes | OTS dönüş: istasyon pencerede dönmüş; parmak iki tık; omuz bir kez kalkar, iner | B dönüş S02 | kabin fanı, nefes | S |
| S05 | Pencere mekaniği | Burun kamerası dönüş: port yüzü 4-6 s arasında tam karşıya gelir, sonra kayar | A dönüş S01 | taşıyıcı | – |
| S06 | Oran karesi (V3) | İki gövde: gemi solda, istasyonun yirmide biri, burnu sağa; MIRA #3 | E · 32mm · EWS · üst açı | MIRA #3 (3,0 s) | – |
| S07 | Halka | Burun kamerası dönüş: port üçte bir kadraj; alt kenarda halka yakası + iki dikme | A dönüş S05 | taşıyıcı | – |
| S08 | Manuel yanaşma | OTS dönüş: baş kola döner, iki tık, T-kol bir parmak ileri; port büyür | B dönüş S04 | kabin fanı | G |
| S09 | Baş kilitlenir | Yüz: gözler pencerede, omuzlar yüksek, nefes sığ; 5,0 s baş kilitlenir | C dönüş S03 | nefes | G |
| S10 | Altı saniye | El ECU: T-kol merkezde, koruma kapağı KAPALI sağda, iptal kolu solda; MIRA #4; iki tık, itiş | D · 85mm · ECU · profil | MIRA #4 (3,0 s) | G |
| S11 | Kaçış | Yüz dönüş: gözler pencerede sola kayan bir şeyi izler, baş yavaş takip eder, durur; kısa nefes | C dönüş S09 | nefes tutulur | T |
| S12 | İptal | OTS dönüş: port pencerenin merkezinden sola kayıp yan döner; T-kol geri çekilir; omuz yüksek kalır | B dönüş S08 | kabin fanı | D |
| S13 | Geri çekilme | Burun kamerası: gemi geri açılır; kopan panel sağ üstten yakın geçer, uçtan uca döner | A · 32mm · WS · göz hizası | taşıyıcı | – |
| S14 | Gezegen ⭐ | Tepe: istasyon kadraj ortasında, ergimiş yüzey tüm arka planı doldurur; istasyon salınır | F · 24mm · EWS · tepe | derin bas | – |
| S15 | Sıfır | Tepe KÜME: aynı; MIRA #5 "sensor confidence zero" — kadrajda insan yok | F küme S14 | MIRA #5 (3,0 s) | – |
| S16 | Hasarlı port | Port-kilitli: ön planda bükük mandal güdükleri; gemi uzakta soldan merkeze geçip sağa kayar | G · 35mm · WS · göz hizası frontal | taşıyıcı | – |
| S17 | Abort | OTS dönüş: MIRA #6; baş pencereden sola, iptal koluna döner ve orada kalır | B dönüş S12 | MIRA #6 (3,0 s) | R |
| S18 | Tereddüt | Yüz: gözler korumaya, sağ eldiven kola gider, bir avuç önünde durur, 2 s, geri gelir | C dönüş S11 | iki kısa nefes | T |
| S19 | Karar | El ECU dönüş: eldiven TIKLATMADAN korumaya gider, başparmak kapağı kaldırır; iptal kolu solda dokunulmamış | D dönüş S10 | kabin fanı | K |
| S20 | Basış | Yüz dönüş: baş kilitli, omuzlar iner ve inik kalır; 6,0 s tek kısa basış; nefes tutulur | C dönüş S18 | nefes tutulur | B |
| S21 | Pencere dolar | OTS dönüş: port pencerenin merkezine gelir ve hızla büyür, 10,0 s'de pencereyi doldurur | B dönüş S17 | kabin fanı | G |
| S22 | Sert kenet ⭐ DORUK | Port-kilitli: gemi soldan merkeze, kameraya doğru hızla büyür; 6,0 s temas — dört dikme tek harekette dibe vurur, bir el genişliği oturma, sekme yok | G dönüş S16 | taşıyıcı + iki tutulan nefes | – |
| S23 | Tek kare ⭐ | Port-kilitli KÜME: hiçbir şey kımıldamaz; dikmeler çökük, yaka bükük; arkada gezegen kayar | G küme S22 | taşıyıcı, nefes bırakılır | – |
| S24 | Eller bırakır ⭐ | OTS dönüş (kafiye S02): port pencereyi doldurur, sabit; dört lamba yanık; eldivenler açılır, uyluklara; MIRA #7, #8 | B dönüş S21 | MIRA #7 (2,0 s) · #8 (7,0 s) | R |

```
AÇI TİPİ SAYISI: 6 ≥ 3   (göz hizası frontal · OTS · alt açı · profil · üst açı · tepe)
KURULUM SAYISI:  7 (A B C D E F G) — 24 sahnede üst bant 12 · alt bant 3 ✓
KURULUM İSKELETİ: A B C B A E A B C D C B A F F G B C D C B G G B
                 KÜME 2 (S14-S15 F · S22-S23 G) · DÖNÜŞ 11/24 = %46 ≥ %40 ·
                 ardışık farklı her çift TAM 1 ölçek kademesi (şok bandı 0 kez) ·
                 V3 (E) yalnız S06 [D32/D78]
BÖLÜM KESİĞİ:    S12 (B) ile S13 (A) arasında — bölüm sınırı da ardışık çifttir: MS→WS, iç→dış ✓
İNSAN ŞERİDİ:    -111---11111----11111--1   (24 · 1 = pilot kadrajda · - = dış)
```

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a)

> Tüm replikler MACHINE register, gemi bilgisayarı MIRA, kabin hoparlörü/telsiz kanalı,
> bedensiz. Saniye FORMÜLLE [D122]: film zamanı = (n−1) × 10 + klip içi ofset.
> Promptta konuşanın ADI geçmez [D34]: "the ship computer's flat synthetic voice".

| # | S | film s | klip s | konuşan | REGISTER | kanal | replik | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|---|---|
| 1 | S02 | 00:13 | 3,0 | MIRA | MACHINE | kabin hoparlörü | "Station wobble confirmed. One full cycle every forty-eight seconds." | ENGEL — sayı kurulur |
| 2 | S03 | 00:23 | 3,0 | MIRA | MACHINE | kabin hoparlörü | "Relay carrier lost." | İSTEK — kurtarılacak şey adlandırılır |
| 3 | S06 | 00:53 | 3,0 | MIRA | MACHINE | telsiz (dış çekim) | "Coronal flux rising. Sensor confidence fifty percent." | ENGEL — makinenin körleşmesi başlar |
| 4 | S10 | 01:33 | 3,0 | MIRA | MACHINE | kabin hoparlörü | "Capture window six seconds per cycle." | ENGEL — pencere sayısı |
| 5 | S15 | 02:23 | 3,0 | MIRA | MACHINE | telsiz (dış çekim) | "Sensor confidence zero. Guidance withdrawn." | MUHATAP — makine çekilir, insan kalır |
| 6 | S17 | 02:43 | 3,0 | MIRA | MACHINE | kabin hoparlörü | "Abort approach. Return burn available for ninety seconds." | AYRILIK — makine "dön" der |
| 7 | S24 | 03:52 | 2,0 | MIRA | MACHINE | kabin hoparlörü | "Hard capture confirmed. Release struts destroyed." | BEDEL — bedelin adı konur |
| 8 | S24 | 03:57 | 7,0 | MIRA | MACHINE | kabin hoparlörü | "Relay carrier restored." | İSTEK — ödeme karşılığı |

```
İLK REPLİK:     S02 · 13 s · öncesindeki kesintisiz sessizlik 13 s (yalnız taşıyıcı + uyarı tonu) ·
                vuruş: kurulum / ENGEL sayısı
BEDENLEŞTİRME:  □ yok — MIRA film boyunca bedensiz (hoparlör; ekran yok, ağız yok) [§1a.1]
SİLME TESTİ:    8/8 tutuyor — her satır görüntünün gösteremediği tek bilgiyi taşıyor (sayı ·
                röle · güven yüzdesi · pencere · geri çekilme · dönüş yakıtı · bedelin adı · ödül)
ON-THE-NOSE:    0 — makine duygu adlandırmaz; insan hiç konuşmaz (HUMAN 0)
SAYI KURALI:    tüm sayılar makinede [D82]; ekranda rakam 0,0 s
```

---

## 📖 BIBLE'LAR

> Karakter çıpası her insanlı IMAGE promptuna KELİMESİ KELİMESİNE girer; video promptu
> aynı çıpanın kısa hâlini CONTINUITY LOCKS'ta taşır. "Bible'a bak" atfı yasak.

### 👤 Character Bible — pilot (promptlarda isimsiz [D34])

```
She is a woman of about forty, broad-shouldered, dark brown skin, in a matte white
pressure suit with one safety-orange band around each upper arm; the helmet is a hard
white shell with a single flat front pane set inside a visible dark-grey rim — not a
bubble, not a dome — the pane optically clear with zero tint and zero mirror coating,
one thin unbroken specular line along the pane's upper edge, the collar seal ring
visible where the helmet meets the suit, her face fully readable through the pane. Her
gloves are heavy, segmented, dark grey, one piece with the sleeve at the wrist. The
back of the suit is one continuous smooth white panel from collar to hip, carrying
nothing.
```

```
KİMLİK ÖZNİTELİĞİ: 3 (yaş · yapı · ten) ≤ 3 [D167]
VİZÖR: BERRAK — tek nitelik, 24/24 sahne [D197 tek kilit · D79 · D95 üç işaret · D146
       düz panel + görünür çerçeve · tür kartı §4.1 D5 "tam şeffaf"]
       ⛔ "opaque / mirrored / pitch-black visor" hiçbir prompta girmez.
SIRT: DÜZ — OTS kurulumu B'de pozitif yüzey cümlesi ZORUNLU [D139 · ⑮]
KASK TAKVİMİ: 24/24 takılı, mühürlü. Kasksız sahne 0.
ÇIPLAK DERİ NEGATİFİ: üç bölge birden [D175]
```

### 🌍 World Bible

```
İSTASYON: terk edilmiş endüstriyel röle istasyonu — koyu gri silindirik gövde (hub),
  bize bakan ucunda SEKİZGEN kenetlenme yakası (collar); yakanın kendi yakalama
  mandalları hasarla içe bükülmüş, işe yaramaz güdükler. Gövdeden iki yana uzun
  radyatör kolları; screen-left kol kopuk, panelleri bükük. Gövde uzunluğu geminin
  yaklaşık YİRMİ katı (V3 cümlesi). Hiçbir yazı, işaret, bayrak, logo yok.
YALPALAMA: istasyon ekseni 48 saniyede bir tam koni çizer (nutasyon); port yüzü her
  salınımda ~6 s boyunca yaklaşma eksenine bakar. 10 s'lik klipte port ucu dairenin
  yaklaşık beşte birini süpürür. Hız SABİTTİR — tork yok, hızlanma yok.
GEMİ: küçük, küt burunlu tek kişilik servis gemisi; mat beyaz, turuncu bantlar; burnunda
  DÖRT yaylı dikme üstünde yuvarlak kenetlenme halkası (halka çapı geminin eninin üçte
  biri). Burun her dış karede istasyona/kameraya bakar (yönelim kilidi).
KOKPİT: tek koltuk; kaskının bir buçuk katı genişliğinde YUVARLAK ön pencere, kalın,
  koyu çerçeveli, yansımasız; altında düz koyu konsol: TAM DÖRT yuvarlak beyaz gösterge
  lambası (S01-S23 sönük, S24 dördü yanık — dikme başına bir lamba); sağ elde T-biçimli
  öteleme kolu; onun screen-right'ında menteşeli kırmızı-beyaz çizgili KORUMA KAPAĞI
  altında tek basma düğme (S01-S18 kapak kapalı · S19-S24 açık); sol elde kısa dönüş
  kolu; konsolun en solunda dik duran sarı-siyah çizgili İPTAL KOLU (24/24 dokunulmamış).
  Ekran 0 · gösterge ibresi 0 · yazı 0. Bilgi kanalı: lamba SAYISI · pencere geometrisi · ses.
GEZEGEN: volkanik gezegenin ergimiş yüzeyi her dış karede kadrajın alt kısmını doldurur:
  siyah kabuk, turuncu çatlak ağı. Atmosfer yok, bulut yok, yıldız yok (gezegen parlaması
  yıldızları siler).
```

### 🎥 Camera Bible

```
KÜRESEL lensler (anamorfik YASAK — vakum kartı §3.1): 24 · 32 · 35 · 50 · 85 mm.
Her sahne LOCKOFF, tek çekim; kamera hareketi 0. Kamera geometrisi harf başına birebir
kopyalanır (aşağıdaki yedi satır bölüm dosyalarında kelimesi kelimesine geçer):
A  32mm spherical lens fixed to the craft's nose, 0.5 m above the docking ring's rim,
   aimed straight ahead along the docking axis; eye-level frontal wide shot.
B  35mm spherical lens fixed 1.3 m behind her right shoulder at shoulder height, aimed
   past her helmet at the round forward window; over-the-shoulder medium shot.
C  50mm spherical lens fixed 0.9 m in front of her at chest height, the camera pitched
   up 15 degrees at her face; low-angle close-up.
D  85mm spherical lens fixed 0.5 m from the right glove at hip height, side-on to the
   console; profile extreme close-up.
E  32mm spherical lens fixed 60 m from the craft and 20 m above the docking axis, aimed
   down at the pair; high-angle extreme wide shot.
F  24mm spherical lens fixed 40 m above the station's hub, aimed straight down;
   top-down extreme wide shot.
G  35mm spherical lens fixed to the station's hull 3 m from the port axis at the
   collar's face plane, aimed straight out along the port axis; eye-level frontal wide
   shot, the collar's octagonal rim in the lower-left foreground.
```

### 💡 Lighting Bible — GÜNEŞ AÇISI SABİT [D201]

```
GÜNEŞ: istasyonun ARKASINDA ve yaklaşma ekseninin ~30° üstünde, HİÇBİR karede kadrajda
  değil. Sonuç kurulum başına sabit ve birbirine tutarlı:
  · gemi tarafından (A · E · F): istasyon ARKADAN ışıklı — kenarlarında sert beyaz
    kontur, bize bakan yüzleri yalnız gezegenin alttan gelen derin turuncu ışığıyla;
    E ve F'de ışık screen-right üstten, gölgeler screen-left'e.
  · port tarafından (G): güneş KAMERANIN ARKASINDA — gemi ön-üstten sert ışıklı,
    gölgeleri lensten uzağa düşer; altları gezegen turuncusu.
  · kokpit (B · C · D): gezegenin derin turuncu ışığı yuvarlak pencereden ALÇAKTAN girer,
    konsolun ve kask çerçevesinin altını yalar; pencerenin üstündeki tek küçük beyaz
    kabin lambası yüzü panelin içinde eşit aydınlatır; dört gösterge lambası nokta.
  · her gölge MUTLAK SİYAH, jilet kenarlı; dolgu 0, saçılma 0, parlama 0, bloom 0.
IŞIK TAKVİMİ: monotonik değişim YOK — 24 sahne aynı güneş, aynı gezegen [D193 riski yok].
```

### ⚙️ Physics Bible

```
0 g vakum. Dış ses 0 — yalnız telsiz kanalı ve kabin. İstasyon sabit açısal hızla
salınır (48 s), hiç hızlanmaz/yavaşlamaz. Kopan panel uçtan uca sabit hızda döner,
asla durmaz [D198]. Gemi nominal kapanma hızı 0,1 m/s (klip başına ~bir halka eni);
sert kenet 0,5 m/s (S22: 6 s'de ~dört halka eni). Temas: rijit gövde — dört dikme tek
harekette sonuna kadar çöker, gövde bir el genişliği oturur, sekme 0, geçişme 0 [D17].
Egzoz: düz keskin beyaz koni, anında seyrelir; alev 0, duman 0.
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5 çekirdeği + vakum + kask + diyalog

```
Single unbroken take, locked-off camera — no cuts, no pans, no zoom, no angle change,
no camera teleportation. Exactly one human character — no duplicates, no clones, no
second person, no reflected or doubled figure. 0% bloom, no glow filter, no soft focus,
no dreamy haze — every surface keeps visible texture. Photorealistic skin with pores and
fatigue retained — no airbrushing, no waxy texture, no face morphing, identical bone
structure throughout. Suit, helmet and gloves identical to the description — nothing
appears or disappears mid-shot; the helmet stays sealed; the front pane stays optically
clear with zero tint, zero mirror coating and zero reflection of the environment; the
back stays one continuous smooth panel with no backpack, no tank, no hose, no cable. No
bare skin anywhere in frame: none above the collar seal, none at the wrist between
glove and sleeve, none at the ankle above the boot cuff. No readable text, letters,
digits, numbers or symbols anywhere in the frame — not on the suit, the console, the
hull, the collar or the station; no scale marks, no graduation ticks, no flag, no logo,
no patch. No screens, no displays, no HUD, no subtitles, no captions, no title card, no
watermark. All hand-surface contacts keep a clear structural boundary — no merging, no
phasing, no extra fingers. No atmosphere, no clouds, no sky, no stars, no haze, no dust,
no smoke, no flame, no spark, no lens flare, no anamorphic streak. Structures static and
solid — no melting, no warping, no swimming texture. No Unreal Engine look, no CGI
aesthetic. Photorealistic with 35mm film grain.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| istasyon salınım periyodu | 48 s / tam koni (10 s'de dairenin ~1/5'i) | R1 yalpalama | S01 S05 S07 S13 S14 S15 S16 S22 S23 |
| yakalama penceresi | 6 s / salınım | R1 yalpalama | S05 S10 S11 S12 S16 S22 |
| nominal kapanma hızı | 0,1 m/s (klip başına ~bir halka eni) | R1 | S08 S09 S12 |
| sert kenet hızı | 0,5 m/s (nominalin 5 katı · 6 s'de ~dört halka eni) | R1 / novum | S21 S22 |
| kenetlenme dikmesi · lamba | TAM 4 · TAM 4 (dikme başına lamba) | R4 sayaç | S07 S22 S23 · S02-S24 |
| gemi / istasyon oranı | 1/20 (V3 cümlesi) | D32 / D78 | S06 |
| sensör güveni | %50 → %0 | tema | S06 S15 |
| dönüş yakıtı | 90 s | AYRILIK | S17 |
| insan sayısı | tam 1 (kadrajda 0 ya da 1) | R2 | S01-S24 |
| vizör | berrak · 0 ton · 0 ayna · 24/24 | R2 vizör | S02-S24 |
| güneş | istasyonun arkasında, eksenin ~30° üstünde, kadraj dışı | R3 ışık | S01-S24 |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D5 · D79 · D95 · D146 · D197 | vizör TEK nitelik: berrak, düz panel, görünür çerçeve, üst kenarda tek parlama çizgisi, yaka halkası görünür | S02-S24 (her insanlı prompt) |
| D139 · ⑮ | kamera arkada (B): sırt POZİTİF yüzey cümlesi | S02 S04 S08 S12 S17 S21 S24 |
| D175 | mühürlü filmde uzuv adı ±12 kelimede örtü adıyla; çıplak deri negatifi üç bölge | tüm insanlı promptlar |
| D32 · D78 | V3 iki gövdeli kadraj yalnız 1 kez; oran cümlesi + hangi uç önde + kesir merdiveni | S06 |
| D104 | doruk: kamera PORTA kilitli, gemi kadraja girer ve kameraya doğru oturur (V5) | S16 S22 S23 |
| B1 | temas ANI sahnenin içinde ve saniyesi yazılı (6,0 s) | S22 |
| D198 · D23 | kopan panel sürekli eksensel dönüşle geçer, asla donmaz | S02 S13 |
| D201 | güneş açısı 24 sahnede sabit, kadran/derece ile SPEC'te | S01-S24 |
| D202 · OYUNCULUK §2-§3 | seçim/bedel/final BEDENDE: bakış eli önceler, tereddüt durma-başlama, omuz hattı iner | S08 S18 S19 S20 S24 |
| D179 | imaj t=0'ı yazar; S19 imajı kapak KAPALI, video kapağı açar; S20 imajı omuz inik | S19 S20 S22 S23 |
| D82 · YANASMA §2.2 | sayı söyleyen her replik makinede; insan hiç konuşmaz | S02-S24 |
| D138 | gövdede metre yok; ölçü gövde/halka oranıyla; kamera mesafesi muaf | tüm promptlar |
| D157 | TEK KARE cümlesi taşıyıcı nesneyi (halka + dikmeler) içerir | S23 |
| KART 10 | insansız sahnede NEGATIVE bloğu 900 karakterin altında | S01 S05 S06 S07 S13-S16 S22 S23 |

---

## 🛡️ POLİTİKA SATIRI (`03_PLAN_ONCESI` B6)

```
EN RED-RİSKLİ KARE:  S22 · 6,0 s — temas anı ("çarpışma" okunma riski)
NÖTR TARİFİ:         Geminin yuvarlak halkası sekizgen yakaya oturur; dört yaylı dikme tek
                     harekette sonuna kadar kısalır; gövde bir el genişliği oturur ve durur —
                     sekme yok, parça yok, kıvılcım yok, alev yok.
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| İlk taslaktaki "acil durum çelik hattı / fırlatıcı" (S18) tümüyle kaldırıldı — zıpkın/silah formu | "halat atma" vuruşu | alet tepkisi: koruma kapağı + düğme (S19) · malzeme sonucu: dikmelerin çökmesi (S22-S23) |
| Temas "collision / impact / crash / debris" kelimeleriyle YAZILMAZ | — | kütle-hız: "seats · struts compress to their stops · settles a hand's width · no bounce" |
| Kopan panel "wreckage / destroyed" değil, "a torn radiator panel" | — | malzeme sonucu: bükük kenar, sabit dönüş |

---

## 📝 BİLİNÇLİ SAPMALAR — tek satır gerekçe [D74]

```
① VİZÖR BERRAK (ilk taslak "opak siyah aynalı" yazmıştı): tür kartı §4.1 D5 "tam şeffaf",
   D79 kapısı, D95 görünür-mühür işaretleri, POLİTİKA §3 ⑥ (yüzü kapatan ekipman red imzası)
   ve D202 (seçim bedende/yüzde okunmalı) tek yönü gösteriyor. İlk taslak iki hâli aynı
   promptta yazıyordu — D197'nin tarif ettiği arıza. Opak istenirse: çıpa cümlesi + NEGATIVE
   D197'nin 3. kalıbıyla değiştirilir, D79 bulgusu gerekçeli düşer.
② SAHNE SAYISI 24 (format varsayılanı 25 = hook 9 s + 24): hook ayrı 9 s'lik sahne değil,
   S01'in kendisi; 24 × 10 s = 4:00 band içinde. Sahip 24 dedi (02_KONSEPT §0).
③ VİDEO PROMPT UZUNLUĞU bandın (2.000-2.600) üstünde, tavanın (4.300) altında: kask bloğu +
   üç bölgeli deri negatifi + diyalog bloğu + kapsamlı metin yasağı aritmetiği (REHBER §5 ①)
   bandı tek başına doldurur; insansız sahneler bandın içindedir. Ölçüm: prompt_kontrol çıktısı.
④ 1.5 rad/s KİLİDİ SİLİNDİ: fiziksel olarak saçma (dev istasyonda 1,5 rad/s = 4 s'de bir tur,
   kenetlenme imkânsız) ve kendi A5 satırıyla çelişiyordu. Yerine 48 s periyot + 6 s pencere.
⑤ G KURULUMUNDA IŞIK: kamera istasyonla döndüğü için gölge kenarları 10 s'de ±6° kayar —
   promptta yazılmaz, ihmal edilir; kadran kilidi S16/S22/S23'te "güneş kameranın arkasında".
```

---

## 🔎 KART P KAYDI — 11.09.2026 (prompt denetim kapısı)

```
① BETİK  python3 …/PROMPT_KONTROL/prompt_kontrol.py yatay_4_dk_filmler/THE_HARD_DOCK --rapor
   İLK KOŞU (ilk taslak):  ⛔ 3 BLOCK — 48 promptta Türkçe etiket · video 1.591-1.795 kr (band altı) ·
                           9 ardışık aynı-kurulum çifti işaretsiz · BÖLÜM 2 = BÖLÜM 1 kopyası · vizör iki hâlde
   SON KOŞU (revizyon):    klasör modu ✅ GO (📁 2 bölüm birleşik · 48 prompt · ⑩①-④ ⑪ ⑫ ⑬ ⑭ ⑮ ⑯ ⑰ ㉑ ㉒ temiz)
                           dosya modu ⚠️ 2 FIX — yalnız UZUNLUK (video 2.359-4.137 kr; band 2.000-2.600 üstü,
                           tavan 4.300 altı) → gerekçe §BİLİNÇLİ SAPMALAR ③ [D74]; iskelet 24↔12 dosya-modu
                           yanlış pozitifi (bölünmüş film; geçerli koşu klasör modu) · rapor: PROMPT_KONTROL/RAPORLAR/
② RUBRİK PROMPT_QA_CRITIQUE (insan yarısı):
   §1 kilitler SAYI: salınım 48 s · pencere 6 s · dikme 4 · lamba 4 · oran 1/20 · boşluk 6 gemi boyu ·
      kamera geometrisi metre/derece · kapanma "halka eni / pencere kesri" ile — tarif kilidi 0
   §2 tetiklenen dersler: kask (takvim + D79 iki cümle ✓) · sayaç (metinsiz kanal ✓) · diyalog (konuşan
      ekran dışı ✓) · sıfır-g (panel dönüşü ✓) · yansıtıcı yüzey (pane/pencere reflection-free ✓ D20)
   §3 A1: dramatik bilgi lamba SAYISI + pencere geometrisi + ses kanalında; yasak onu silmiyor ✓
   §3c kompozisyon: S10/S19 yüz yok + el + makro → kamera nesne hizasında, tepeden değil; ikinci riskli kare
      olarak kayıtlı; S22 makine-makine teması, insan yok ✓
   §5 TIMELINE 0-10 s dolu, her damgada görünür değişim, doruk S22'nin İÇİNDE (6,0 s) ✓
   §6 açı↔vuruş: hook frontal geniş · seçim el ECU (iki nesne) · doruk port-kilitli (D104) · final OTS kafiye ✓
③ RUBRİK DIALOGUE_CRITIQUE: 8 satır · T1 silme testi 8/8 tutuyor · T2 on-the-nose 0 · T4 swap: hepsi makine ·
   T5 FIT (sayılar makinede) · T6 tam form, dolgu 0 · T7 en uzun satır ~3,5 s < 5 s · MONOLOGUE 0 · UNCLEAR 0 → GO
④ KARAR: ✅ GO — üretim sırası: R1 → R2 → R3 → R4 (KAPI 0) → S22 → S23 → S19 → S24 → S01 → kalanı.
   ⛔ Referans sayfaları ONAYLANMADAN hiçbir sahne üretilmez [D168]; ilk test klibinde klip süresi ffprobe ile ölçülür [D124].
```
