# 🧠 SUSMAYAN_NOBETCI — KONSEPT VE RİSK

> Girdi: sahibin talebi + `00_HIKAYE_ONAYI.md` (TUR 1/3 · 17.09.2026) + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi — üç aksiyon önerisinden "SUSMAYAN NÖBETÇİ" seçildi, 8 maddelik
            eleştiri + S0-S2 açılışı + S36-S47 doruk tablosu + S46-S47 final notuyla
② FORMAT:   yatay 8 dk          → kart §2.7 · bölüm sayısı 4 (sahip: "her biri 12 sahne")
③ SAHNE:    48                  → formatın varsayılanı (48 × 10 s = 8:00)
   ⚠️ Bölümleme kart dışı: kart 2 × 24 der, sahip 4 × 12 dedi [D74 · 0b ①]
④ REFERANS PAKETİ: YAZILMASIN (sahip, 17.09.2026)
   PLAN'a düşecek TEK SATIR: "Referans paketi yazılmadı — sahip kararı 17.09.2026; T1·T2·T3·T5·T6
   doğru (§5b), telafi ANATOMİ KARTI sayıları + Scene Foundation ana kareleri; kask biçim riski
   04_UYARI R3."
⑤ HİKÂYE ONAYI: `00_HIKAYE_ONAYI.md` ONAY 17.09.2026 · TUR 1/3 · SAPMA yok
```

## 0b. 🧭 BİLİNÇLİ SAPMALAR VE SAHİP KARARLARI — kaydı olmayan sapma yapılmamış sapmadır [D74]

| # | kural / kart | sapma | kimin kararı · gerekçe |
|:--:|---|---|---|
| ① | §2.7 "2 bölüm × 24" | 4 bölüm dosyası × 12 sahne | sahip · "Dört bölümün her biri 12 sahne." QA birimi BENI_HATIRLAMA K1 ile aynı açık karar (öneri 4 çeyrek `--bolum n/4`) |
| ② | YANASMA §1.2 "V3 oran karesi 1, en çok 2" | 4 kontrollü geniş plan (iki gövde aynı karede) | sahip · "Birkaç kontrollü genel plan bu coğrafyayı kurabilir." Her birinde oran cümlesi + hangi uç önde + kesir ZORUNLU; temas V5 (kamera hedefte) korunur |
| ③ | D210 "kapanış CAMERA = açılış CAMERA" | S0 kokpit OTS · S47 dış geniş | sahip tarifi (S0 kokpit, S47 iki gemi birlikte). Kafiye: olay kafiyesi + S8 ↔ S47 birebir kurulum dönüşü |
| ④ | FINAL §2.1 kapanış bütçesi 7-9 dk %5-7 | doruk S45'te biter, kapanış S46-S47 = %4,2 | sahip tablosu (S46-S47 = 07:40-08:00) |
| ⑤ | DIYALOG §8 "doruk ve final sessiz" (öneri) | S46'da tek kısa telsizsiz söz | sahip notu ("baştaki telsiz sesini ilk kez parazitsiz duyarız"); söz S1 çağrısının cevabı (hook ↔ final çifti) |
| ⑥ | SES §2 "kasksız sahnede tek kelime konuşulmaz" | S46 pilot kasksız, söz ÖTEKİNİN (kadraj dışı ağız) | konuşan pilot değil; kadrajda ağız 0 → kuralın gerekçesi (lip-sync) tetiklenmez |
| ⑦ | HOOK §2.2 "hareketin ortasında açılış" + OMNI §3 ④ "kadraj dışı nesne girmez" ↔ YANASMA V5 "araç kadraja girer" | temas sahnelerinde çekici t=0'da KADRAJDA | motor OMNI; V5'in kamera-hedefte kısmı korunur, "kadraja giriş" düşer |

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "daha aksiyonlu uzay gemilerin vurulduğu yanaşma sahnelerin olduğu 3 öneri hazırla"
       → seçim: "ben de üç fikir arasından SUSMAYAN NÖBETÇİ'yi seçerdim … Süre kesinlikle
         korunacak: 48 sahne × 10 saniye = 8 dakika. Dört bölümün her biri 12 sahne."
REPLİK: VAR — sahibin açılış notu iki replik yazdı ("Buradayız. Bizi görebiliyor musun?" ·
        "Yanımızdan geçiyorsun.") ve onaylı hikâye 8 replik taşıyor → SES_VE_DIYALOG §1a-§2a +
        DIYALOG_SAHNESI + DIALOGUE_CRITIQUE zinciri açıktır
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "uzay gemilerinin vurulduğu" | vakumda patlama topu, alev, ses YOK (§3.1); ışın/mermi görünmez | vuruş = ayrılan gövde parçası + düz yayılan buz kristali konisi + ≤6 karelik tek beyaz çakma; ses yalnız gövdeden/kabinden | KILAVUZ §3.1 · D192 · POLİTİKA §4.1 ①② |
| "motoru çalıştırırsan vurulursun" | uydu neyi görüyor? | sıcak egzozu görür (ana motor, kapsül motoru); soğuk gaz iticisi eşiğin altında; ateşleme → vuruş 3,0 s | sahip eleştirisi ① |
| "her atıştan sonra yeniden hazırlanma aralığı" | aralık ekranda nasıl okunur (metin yok) | iki soğutma kanadı açılır = ateş edemez; kanatlar kapanınca hazır; aralık ≈ 15 s | D78 · KART 5 · sahip ① |
| "gezegen uydu ile gemilerin arasına girerek atış hattını keser" | kenarı ne zaman geçtikleri nasıl okunur | dış geniş kadrajda uydu ışığının gezegen kenarına mesafesi (kare yüksekliği kesri) monoton azalır; S47'de kenar araya girmiştir | sahip ⑥ · D78 |
| "S15 çıkmaz: çarpışmayı önler ama saldırıyla yönelim kontrolünü kaybeder" | 0 g'de vurulan yönelim iticisi dönme üretir | itici kümesi dikişinden ayrılır, gövde tepki dönüşüne girer (≈ tur/20 s), sonra kontrolsüz döner | sahip ④ · HARD DOCK recoil bulgusu |
| "S46 kamera yüzünde kalırken kadraja giren bir el omzuna dokunur" | kadraj dışından giren el = OMNI §3 ④ uydurma riski; 2. insan | el t=0'da kadrajın kenarında, omza DOĞRU uzanmış başlar; ikinci insanın yalnız eldiveni ve ön kolu, yüzü 0 | OMNI §3 ④ · D214 |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 8 dk → §2.7 (modül hattı · hook 48'in içinde)
ORTAM:         §3.1 VAKUM (yörünge, 0 g) + §3.10 BASINÇLI İÇ HACİM (çekici kokpiti · tahliye bölmesi)
               → vakum: gölge mutlak siyah · dolgu yok · dış ses 0 · egzoz düz koni kıvrılmaz ·
                 anamorfik parlama yok · süzülen her şey dönme momentumuyla
               → iç hacim: panel ışığı, bounce var, kabin sesi var; 0 g (kemer, süzülen kol)
TÜR:           bilimkurgu · dal: sert uzay gerilimi / yanaşma (aksiyon kulvarı) → §4.1
KLİP SÜRESİ:   10 s VARSAYIM ⛔ ÖLÇÜLMEDİ [D124] — üretim günü 1'de ilk kabul klibinden ffprobe;
               farklıysa 03 SIRALAMA saniyeleri yeniden hesaplatılır
SAHNE SAYISI:  48    RUNTIME: 0 + 48 × 10 = 480 s = 8:00 (hook S0 sahnenin içinde)
BÖLÜM SAYISI:  4 dosya (sahip) · S0-S11 · S12-S23 · S24-S35 · S36-S47
MOTOR:         OMNI 1.1 Flash (I2V) · zincir modu ① tek başlangıç karesi · replikler post-dub
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:               Savaştan kalma bir uydu, motoru yanan her şeyi üç saniye içinde vurur;
                     iki soğutma kanadı açıkken ateş edemez.
NOVUM TİPİ:          fiziksel yasa (makine kuralı olarak, ortamın içinde tek ihlal)
                     ⚠️ ONERME §3 maya eşiği: ihlal sayısı 1 — kanat aralığı kuralın SONUCU
NOVUM TAŞIYICISI:    MOTOR KOLU × pilotun eldiveni → EGZOZ KONİSİ yanan gövde 3 s sonra ayrılır
① TEK KARE:          ✅ S0 ≈ 0:04 — "motor konisi hâlâ yanan mekik gövdesi ikiye ayrılırken ön
                     planda pilotun eldiveni MOTOR KOLUNUN üstünde duruyor" (taşıyıcılar adıyla)
② KİNETİK BAĞIMSIZLIK: ✅ kural replik olmadan kanıtlanır: S0 (yanan → vurulur) · S3 (yanıyor,
                     kanatlar açık → vurulmaz) · S4 (kanatlar kapanır → vurulur) · S47 (kenarın
                     ardında yanar → vurulmaz); telsiz hiçbir kuralı AÇIKLAMAZ
③ BAŞLIK ŞEMASI:     ✅ "Don't Light the Engine" (4 kelime) — izleyici motor ışığına bakar
KURAL TEKRARI:       6 nesne · 6 farklı sonuç (≥3 sahne · ≥2 nesne ✅)
BİLİŞSEL ÇİZELGE:    ihlal 0-3 s S0 · kinetik tepki S0 sonu (el donar) · doğrulama S3-S4 ·
                     bedele dönüşme S30 · doruk S44-S45
→ KONSEPT KAPISI ✅
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — İNSAN-MAKİNE sınırı (yatay süreç teması ✅ §4)
▸ tanım cümlesi — "Savaş, onu başlatanlar gittikten sonra da makinelerin içinde sürer."
                  (takas kalıbı değil: kimse bir şey için bir şeyden vazgeçmiyor cümlede)
▸ depoda kaç kez kullanıldı — İNSAN-MAKİNE 4 (sayac.sh 17.09.2026 14:00)
▸ motif kanalları — IŞIK: uydu sensörünün sabit, değişmeyen tarama ritmi ↔ kabinde düzensiz
                    nefes · NESNE: iki soğutma kanadı (makinenin tek "nefesi") · KİNESİK: pilotun
                    staccato kilitlenmesi (el kolda donar S0/S5) → S44'te kolu tek hamlede sonuna iter ·
                    KAMERA: alt açı YALNIZ uyduya (ekran görüntüsünde), pilota asla
▸ tema-final uyumu (§6 İnsan-makine): görsel İFŞA — S47'de makine hâlâ aynı ritimle tarıyor,
  insan seçiminin izi (boş kapsül yuvası) kadrajda
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 SU/SIVI | ❌ | sıvı yok (buz kristali parçacıktır → kart 6) | — | — |
| 2 CANLI | ❌ | canlı yok | — | — |
| 3 KASK/VİZÖR | ✅ | pilot 47 sahne kasklı | kask durum dizisi: kapalı S0-S45 · S46 AÇIK (sahneye açık girer) | 🟠 |
| 4 İKİNCİ FİGÜR | ✅ | tek görünür insan + S46'da ikinci insanın eli; mekik/kurtarma gemisinde insan görünmez | S46 dışında her insanlı prompt "exactly one human"; S46 iki satır pozitif ayrım | 🟠 |
| 5 EKRAN/SAYAÇ | ✅ | kanat · ibre · fener · uydu ekranı | sayaçlar DURUM (kanat açık/kapalı, ibre yarı/dip, fener sayısı); ekranda görüntü var, rakam/işaret 0 | 🟡 |
| 6 PARÇACIK/PATLAMA | ✅ | 6 vuruş · buz kristali · soğuk gaz · enkaz | patlama 0; ayrılma + düz koni + dönme oranı sayıyla | 🔴 (1 no.) |
| 6b BÖLGELİ DÜNYA | ✅ | kokpit içi ↔ dış uzay ↔ tahliye bölmesi (üç ışık bölgesi) | BÖLGE IŞIK TABLOSU PLAN'da; bölge değişimi yalnız kesmede | 🟡 |
| 7 DİYALOG | ✅ | 8 replik | merdiven basamak 1 (kadraj dışı telsiz) + post-dub; konuşan ağız 0 | 🟢 |
| 8 KAMERA | ✅ | lockoff | klip içi hareket 0; sahneler arası açı yayı ACI_YAYI §3 | 🟢 |
| 9 IŞIK MIKNATISI | ✅ | çekici hedefe gidiyor, tek güneş + uydu ışığı | güneş kadraj DIŞI; hareket nesneye bağlı; temas sahnesinde kamera hedefte | 🟡 |
| 10 İNSANSIZ SAHNE | ✅ | 13 dış sahnede insan yok | NEGATIVE kısa (<900 karakter), boş kadraj VARLIK olarak (COLD BURN S8 V3) | 🟠 |
| 11 DEĞİŞKEN SÜRE | ❌ | sabit 10 s ızgara, küme klipleri de 10 s | — | — |
| 12 POLİTİKA | ✅ | insanlı geminin vurulması · silahlı makine · S46 ikinci insan · kask | malzeme dili, silah adsız, kask çıkarma eylemi 0 (§6) | 🟠 |
| 13 YAPI ÖLÇEĞİ | ✅ | çekici · tahliye gemisi · uydu · kapsül | ANATOMİ KARTI + ölçek merdiveni + ölçek şahidi | 🟠 |

```
TETİKLENEN RİSK:  11 / 14
EŞİK:             5
✅ EŞİĞİN ÜSTÜNDE → KİLİT TAVANI ≤ 20 (01 §1: 20 kilit · 20 ders §1b'de başka yerde);
                     MALZEME AZALTILMADI (14.09.2026 sahip kararı) — kart 12 politika satırı tavan dışı
```

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  UYDU VURUŞUNUN GÖRÜNÜŞÜ — model "gemi vuruldu" kümesinden ateş topu, ışın,
                  alev ve duman çağırır (kart 6 · KRONOS 2:20 · COLD BURN alevli patlama 🔴)
POZİTİF BİÇİMİ:   ① ışın/mermi yolu 0 kare — kuvvet kaynağı kadrajda görünmez
                  ② vuruş anı: vurulan dikişte TEK beyaz nokta çakması, bir yumruk büyüklüğünde,
                     ≤ 6 kare (0,25 s), sonra 0 kare artık ışık
                  ③ ateşleme başlangıcından vuruşa 3,0 s
                  ④ ayrılan parça dikişinden ayrılır, kazandığı dönüşle uzaklaşır: "about one turn
                     every three seconds"; kadrajı en geç 6 s'de terk eder ya da sonuna kadar görünür
                  ⑤ ayrılma yerinden DÜZ çizgilerle yayılan buz kristali konisi, genişliği ayrılan
                     parçanın yarısı, 2,0 s içinde seyrelir, hiçbiri kıvrılmaz
                  ⑥ ana gövde ters yöne tepki dönüşüne girer (HARD DOCK recoil bulgusu)
SPEC GÖZ KAPISI:  "6 vuruş sahnesinin hepsinde çakma ≤6 kare, alev/duman/ışın 0 kare, koni ≤2,0 s"
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — soru ④ "yazılmasın"; tablo D74 gerekçesi için ölçüldü

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | pilot · 47 sahne |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | kask (D146) · uydu gövdesi · çekici kokpiti |
| T3 | oranı sözle yazılamayan nesne | ✅ | çekici (6H) ↔ tahliye gemisi (16H) ↔ kapsül (1,3H) |
| T4 | insan dışı canlı | ❌ | — |
| T5 | tekrar eden insan dışı olay | ✅ | vuruş/ayrılma 6 kez · kanat açılıp kapanma 4 kez |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | uydu (ekran + uzak ışık, 12+ sahne) · tahliye gemisi 36 sahne |

```
KARAR: YAZILMAZ — sahip kararı (17.09.2026). 5/6 tetikleyici doğru.
⛔ PLAN'a tek satır (0 ④) + telafi: ANATOMİ KARTI (her varlığın adet sayıları film boyu tek)
   + Scene Foundation (boş kokpit master · dış çapa master · tahliye gemisi tek-gövde master)
   üretimden önce onaylanır ve her I2V karesi bunlardan türetilir + 04_UYARI R3.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S15 (insanlı tahliye gemisi vuruluyor; telsizde ses; aynı blokta "vurulma")
NÖTR TARİFİ:         "a thruster pod on the long ship's right flank separates along its seam and
                     turns away end over end; a short cone of ice crystals spreads in straight lines
                     and thins; the hull begins a slow turn the other way" — insan 0 kare, silah
                     adı 0, hasar sıfatı 0; kaynak kadraj dışında
İKİNCİ:              S46 (kasksız yüz + ikinci insanın eli) → kask sahneye açık girer, el omza
                     t=0'da yaklaşmış, temas yumuşak kavrama, yüz ≤3 öznitelik
ÜÇÜNCÜ:              S30 (kapsül vurulur + yakın plan vizör yüzü aynı sahnede DEĞİL: yüz S29,
                     vuruş S30 dış geniş)
```

| ÖNLEM | MALİYET | TELAFİ (§4.1 kanalı) |
|---|---|---|
| silah adlandırılmaz, ateş görünmez | "neyle vuruldu" görüntüsü | ② malzeme sonucu (ayrılma + koni) + ③ alet tepkisi (kanatlar açılır) |
| patlama/alev 0 | aksiyonun görsel "patlaması" | ① kütle-hız: ayrılan parçanın dönüşü + ana gövdenin tepki dönüşü |
| insanlı gemide insan görünmez | tehlikenin yüzü | ④ temassız gövde tepkisi: pilotun nefesi durur (TEL) + penceredeki fener sayısı |
| kask çıkarma eylemi 0 | S46 "kaskını açar" jesti | kask sahneye açık girer; vuruş eldiven eli ile omuzdaki ele taşındı |

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Çekici pilotu, uydunun menzilinde sürüklenen tahliye gemisine yanaşıp havasını
         paylaşmak ve gemiyi gezegen kenarının ardına, kurtarma gemisinin erişeceği yere
         taşımak — film başlamadan verilmiş görev (S1 çağrı, S8 kurtarma gemisi, S10 hortum)
ENGEL:   motor ateşlemek vurulmak demek; soğuk gaz sınırlı (ibre); tahliye gemisi S16'dan sonra
         kontrolsüz dönüyor; hava bitiyor (S9 · fener sayısı)
BEDEL:   S30 · kaçış kapsülü yem olarak salınır ve vurulur — kurtarma başarısız olursa pilotun
         tek başına kurtulma şansı kalmaz · S45 · çekicinin motor bölümü kopar
MUHATAP: ikinci insan KADRAJ DIŞI (telsizdeki yetişkin ses) + kendi geçmiş kararı (kaçış kapısını
         açık tutma alışkanlığı) + ortamın kalıcı değişen parçası (boş kapsül yuvası)
AYRILIK: S7 — pilot çekiciyi uzaklaştırır ↔ ses "Come back." (ret, gecikme ≥ 0,7 s)
TERSİNMİŞ AYRILIK: S27-S28 — ses "Take your capsule and go." ↔ pilot kapsülün kapağını kapatır,
         kokpit lambasıyla üç kez cevap verir (bırakmak isteyen tutan oldu)
```

## 8. 👤 KARAKTER KARTLARI — `KARAKTER_KARTI_VE_DAVRANIS` §1 (kart PROMPTA GİRMEZ)

```
👤 KARAKTER KARTI — ÇEKİCİ PİLOTU
ROL           ağır işçi çekicisinin tek pilotu — kalın eldiven, turuncu bant, kokpit kolları  S0-S1
İSTEK         tahliye gemisine yanaşıp hava vermek, kenarın ardına taşımak                    S10
BASKI TEPKİSİ KONTROL EDER — hesaplar, bekler, fırsatı hesap yaparken kaçırır               S5 · S17
ALIŞKANLIK    riskten önce sol başparmakla kapsül ayırma kapağına İKİ KEZ vurur               S6 · S10 · S23
              KIRILMA: S29 başparmak kalkar, vurmaz, eldiven doğrudan kolu kavrar               S29
SINIR         ana motoru ateşlemez                                                              S5 → kırılır S31 (pencerede) · S44 (bilerek, pencere yokken)
ZAAF          soğuk gaz ibresi yarı (S12) → dip (S33) · yorgunluk 1 → 6 · SAĞ eldiven avucunda
              parlak metal sürtünmesi                                                           S12-S33 · S42+
TEL           nefesini tutar — kask içi nefes sesi kesilir, omuzlar yükselir ve kalır            S13 · S38
İLK ↔ SON     S0 eldiven motor kolunun üstünde DONAR ↔ S44 eldiven motor kolunu tek hamlede sonuna İTER
```
```
👤 KARAKTER KARTI — TAHLİYE BÖLMESİNDEKİ YETİŞKİN (yalnız ses · S46 yalnız eldiven ve ön kol)
ROL           tahliye gemisinin bölmesindeki yetişkin — telsizi tutan, feneri sallayan          S1
İSTEK         önce: pilotun gelmesi · sonra: pilotun kurtulması                                  S7 → S27
BASKI TEPKİSİ ACELE EDER — beklemez, motoru kendisi ateşler                                     S15
ALIŞKANLIK    feneri iki kez yakıp söndürerek cevap verir                                        S1 · S7 · S27
SINIR         diğerlerini bırakmaz (bölmeden çıkmaz)                                            —
ZAAF          ses nefes nefese → hırıltı → seyrek nefes                                         S9 · S29 · S35
TEL           telsiz tuşunu bırakır, yalnız taşıyıcı hışırtısı kalır                             S13
İLK ↔ SON     S1 telsizle çağırır ↔ S46 telsizsiz, aynı sesle cevap verir
```
```
İKİ KART AYRIŞMASI (IKI_KISI §2 · ≥3 satır): BASKI TEPKİSİ (kontrol eder ↔ acele eder) ·
ALIŞKANLIK (kapak vuruşu ↔ fener) · İSTEK (yanaşmak ↔ önce gel / sonra git)
İSTEK ÇAPRAZI: pilot ondan motoru ATEŞLEMEMESİNİ ister (S14 "Don't.") · o pilottan önce
GELMESİNİ (S7) sonra KAPSÜLLE GİTMESİNİ ister (S27) · NESNE: kapsül / motor kolu
```

## 9. 🎙️ SES VE MOTOR KARARLARI

```
MOTOR         OMNI 1.1 Flash · I2V · 720p seçim · zincir ① tek başlangıç karesi (K2 ⬜ S36-S37 için ②)
REPLİK        8 replik POST-DUB (OMNI §5 ②: PROB ① koşulmadan klipte replik üretilmez) —
              promptta tırnak 0, AUDIO "one short burst of radio static, no words"
DİL           İngilizce dublaj (kanal İngilizce); Türkçe karşılık plan tablosunda
SES KİMLİĞİ   tek yetişkin ses (post) + pilotun tek kelimesi (post) — OMNI §5 ④ sorunu yok
REGISTER      ikisi de HUMAN · tahliye sesi telsiz band-pass · S46 band-pass YOK (bedenleştirme
              yarısı: ses bedene yaklaşır, ağız yine kadraj dışı)
DIŞ SES       vakum dış kadraj: dış ses 0 — yalnız telsiz hışırtısı (insansız dış) ya da kabin/kask içi
MÜZİK         MUZIK dosyasında; doruk öncesi susar (S43 sonu), çözülme S46'da
```

## 10. ⬜ SAHİP KARARI BEKLEYENLER — üretimden ÖNCE

```
K1  QA birimi — 4 çeyrek (`--bolum n/4`) mi, 2 yarım mı (BENI_HATIRLAMA K1 ile aynı karar)
K2  S36-S37 temas: OMNI başlangıç + bitiş karesi (②) mi, tek kare (①) mi
K3  klip süresi ffprobe (üretim günü 1) — 10 s değilse 03 saniyeleri yeniden hesaplanır
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı (11/14) ve eşik kararı verildi (kilit tavanı ≤20, malzeme azaltılmadı)
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S30 · S45)
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
