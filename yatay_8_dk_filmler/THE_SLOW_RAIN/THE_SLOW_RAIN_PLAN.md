# 🎬 THE_SLOW_RAIN — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.
>
> ⭐ 22.09.2026 · `/yeni-film` ile yazıldı — deponun İLK FİKİR TURU filmi (HIKAYE_FIKIR_TURU 0.7a:
> 12 logline · 5 eleme · 3 aday · sahip ONAY A · TUR 1/3 · iki SAPMA yeniden onaylı).
> Analiz: `00_ANALIZ/` (çizelge 47 zorunlu + 6 havuz dosyası · hasat 20 kilit · konsept · 48 sahne sıralaması · uyarılar · sahne tablosu + 5 kilit sahne).

```
FORMAT:        yatay 8 dk · 48 sahne · KART §2.7 — yazım dosyası 4 × 12 (sahip; kart 2 × 24 der),
               QA birimi BÖLÜM: yarımlar S0-S23 · S24-S47 → SPEC A PART GRID dolu
ORTAM:         §3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar N₂+CH₄ · 0,38 g) — ⭐ SIVI BANDI bu filmle
               açıldı (kart "sıvı yok" diyordu; 02_KONSEPT §1, kart notu sahip kararı ⬜) + §3.10 iç hacim
TÜR:           bilimkurgu · hayatta kalma / taşıma   (tek açık dal — §4.1)
KLİP SÜRESİ:   10 s VARSAYIM ⛔ ARAÇTAN ÖLÇÜLÜR [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
SAHNE SAYISI:  48        RUNTIME: 480 s = 48 × 10 s (hook S0 klibin içinde, ayrı sahne değil)
LOGLINE:       Soğuk bir ayda kanatla uçan bakımcı, üssün ölen ısı çekirdeğinin yedeğini, yavaş
               inen metan yağmuru göl yatağını doldurmadan, kanatlarını feda ederek üsse taşır.
REFERANS PAKETİ: YAZILMADI — sahip kararı (soru ④). T1 (kask) ve T2 (kanat → kızak → yok biçim
               dizisi) tetikleyicileri AÇIK; kanat/kızak/kask cümleleri 48 promptta birebir, S1 ve
               S15 ilk onaylı kareleri sonraki sahnelere imaj referansı [D153/D154]; dosya ⬜ BEKLİYOR.
```

---

## 🎭 TEMA

```
TEMA: KİMLİK (TEMA_MUHENDISLIGI §3 · süreç teması · yatay)
      — "Uçarak var olan biri, yürüyerek eve döndüğünde de aynı kişidir: kanat askısı boş,
        kayış kesik, el belde." (TANIM cümlesi; takas kalıbı değil)

MOTİF SAHNELERİ: S1 · S10 · S15 · S19 · S25 · S29 · S45 · S47
      motif: KANAT ASKISI / KAYIŞ (nesne) · kendi izine/kayışa dolaylı bakış (kinesik) ·
      vizör kabuğu = bölünmüş ayna (S25) · bölünen kanat (S19). Bedel sahnesi S29 listede.
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Yağmur yavaş yağar — iri (bilye boyu), seyrek, sayılabilir damlalar Dünya
                     yağmurunun yaklaşık üçte biri hızla (yavaş koşu temposu) iner; bulut tabanından
                     yere inmeleri dakikalar sürer, cephe gökte görünür; sıcak olana değince buharlaşıp
                     kuru kar olarak geri düşer, soğuk olanı ıslatıp ağırlaştırır.
NOVUM TİPİ:          fiziksel yasa (kalın soğuk hava → sürüklenme sınırı düşük); uçuş aynı fiziğin
                     sonucu, ikinci kural değil (ihlal sayısı 1)
NOVUM TAŞIYICISI:    yağmur damlaları × kaldırılan eldiven (S0) → damla yavaş koşu temposunda iner,
                     eldivene değince beyaz kuru-kar pufu kalkar; aynı kural kanat (S7 · S17) · kask (S24) ·
                     zemin (S32)
TEK KARE (§4①):      ✅ S24 — yağmur damlaları omuz hizasında yavaşça inerken bakımcı aralarında yürüyor,
                     kask çerçevesinde beyaz tortu (taşıyıcı: damlalar, kadrajın ≥1/10'u)
KİNETİK BAĞIMSIZLIK: ✅ damla iner, eldiven kalkar, puf kalkıp kar düşer — replik/metin/dış ses yok
BAŞLIK ŞEMASI:       ✅ "Yavaş Yağmur" (2 kelime) — izleyici damlalara bakar
NOVUM DAVRANIŞI SAYIYLA: "large sparse drops the size of marbles, few enough to count, falling at a
                     slow jogging pace, far slower than rain on Earth, none streaking, none hanging still"
                     — novum sahnelerinde birebir (S0 · S17 · S24 · S32 tam · S7 kısa), öteki dış sahnelerde kısa hâli
```

## 🧭 B5 — HİKÂYE OMURGASI (her formatta · `03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   üssün ısısını ayakta tutmak — yedek ısı çekirdeğini eski istasyondan üsse getirip yuvaya
              oturtmak (bakımcının işi, film başlamadan var: S1'de ısı hattını uçarak dolaşıyor)
   □ ENGEL:   çekirdek kanatların taşıyabileceğinden ağır (S13) + inen yağmur göl yatağını dolduruyor
              (S20 → S33 → S40) + yağmur değdiği her şeyi ağırlaştırıp ısı emiyor
   □ BEDEL:   KANATLAR — S15 kızağa çevrilir · S19 kesilir · S29 kayışı kesilip çukurda bırakılır ·
              S30 batar · S45 boş askı; bir daha uçamaz, göl doldu (S46) · S29 ⭐
   □ MUHATAP: kendi geçmiş kararı (S10 kanat işareti — çekirdeği oraya hafif uçmak için kendisi
              bıraktı) + kendi bedeni (S22 · S25 · S31 · S35) + ortamın KALICI değişen parçası
              (göl dolar S20 · S33 · S40 · S46)
B5b ☐ AYRILIK — tek insan, yok

KARAR MİMARİSİ (KARAKTER_KARTI §3):
   S15  iki nesne kadrajda: kanatlar (uç, çekirdeği bırak) ↔ çekirdek (yürü) — kanatları yere serer;
        reddedilen yolun bedeli S13'te gösterildi
   S29  iki nesne kadrajda: batan kızak/kanat ↔ çekirdek — kayışı keser; kanat kadrajda kalır ve
        S30'da batmayı sürdürür
   BAŞARISIZ DENEME: S13 (uçuş) · S18 (kazıma) · S27 (kızağı çekme) · S38 (yuvarlama) — her deneme yöntem değiştirir
   HOBSON: S39 — tek yol (diz üstü), tarz ve zaman seçilir

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  S1 (kanat biçimi — referans paketi yerine ilk onaylı kare) → S15 (kızak biçimi) → DORUK S43 →
  BEDEL S29 → kapanış imajı S47 → S0 (A kurulumu S47'den kilitlenir) → S24 (tek kare) → S13 →
  S45 → kalanı
  ⛔ İPTAL KAPISI: S1 kanat tek geometriyle çıkmıyorsa · S24 damlalar çizgi/perde çıkıyorsa ·
  S29 kayış kesimi + kanat kadrajda tutmuyorsa — film ÜRETİLMEZ (03_SAHNE_SIRALAMASI §7)
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR (KILAVUZ_REHBERI §2.1)

```
— yatay film; bu blok uygulanmaz. B5 OMURGASI yukarıda.
BİLGİ ASİMETRİSİ (HOOK §3.1, yatayda da yazılır): DRAMATİK İRONİ · taşıyıcı ① ARKA PLAN ·
asimetri anı S9 (~1:30): kapıyı zorlarken damla perdesi kadraj arkasında S7'dekinden alçak;
S11 daha alçak; karakter S14'te görür (kapanış). Panik karesi 0.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | %0-2 | S0 | — |
| 2 | Kurulum | %0-6 | S0-S2 | ilk 30 s'de 3 kurulum (A·C·R): S2 kurulum değil katalizör tohumu — bilinçli [D74] |
| 3 | Katalizör | ~%6 | S3 | banttan erken; yatay "≤0:15" kapısıyla uyumlu |
| 4 | Tartışma | %8-27 | S4-S13 | — |
| 5 | Orta nokta (sahte yenilgi) | %50-56 | S24-S27 | — |
| 6 | Umut-önce-düşüş | %71-73 | S34-S35 | — |
| 7 | Her Şeyin Kaybı | %60 · %79 | S29 (bedel) · S38 (çaresizlik) | bedel banttan erken; seçim sonrası 18 sahne bedelin taşındığı yol (D158) |
| 8 | Final | %85-98 | S41-S46 | doruk S43, çözülme S44-S47 (kapanış bütçesi %8) |
| 9 | Kapanış imajı | %100 | S47 | — |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:     yanlışlık kompozisyonu — normal kadraj (kapı önünde figür) + TEK anormal öğe (damla
               yavaş iniyor, eldivende puf); tek tip
S0 SORUSU:     "Bu damlalar neden inmiyor — ve indiğinde ne olacak?"
S1 İKİNCİ BİLGİ: insan kanatla uçuyor — soru büyür; S3 katalizör yeni soruyu açar (ısı bitmeden
               çekirdek gelecek mi)
İLK 2 SN SESİ: tek diegetik ses — damlanın eldivene 'tok'u + kısa buhar tıslaması; müzik 0:00'da
               girmez (en erken S1, alçak katman)
AÇILIŞ BÜTÇESİ: katalizör S3 (%6) — bant %10-15'in altında (erken, izin gerekmez)
TOHUM (FINAL §3): boş kanat askısı S4 kadraj kenarında (%8, ≤2 s, vurgusuz) → ödeme S45
```

### 🔗 ÇİFT KARTI (`ACILIS_KAPANIS_CIFTI` §5)

```
ÇİFT TİPİ        KAFİYE (8 dk yatay)
TAŞIYAN TEMA     kanatla var olan, kanatsız da aynı kişi — el kalkmaz
İLK KARE         S0 · A · CU frontal · figür kadraj merkezinde, eldiven kalkık (foveal merkez) ·
                 tohum: kapı çerçevesi solda (kenar) · 120 px testi ⬜ koşulmadı (üretimde kare)
SON KARE         S47 · A birebir · aynı koordinat · eldivenler belde · ödeme: kaskta puf, el yok
DEĞİŞEN TEK DEĞİŞKEN  ① GÖVDE — el kalkık ↔ el belde (merkez); ikinci değişken (kanat) A kurulumunda
                 KADRAJ DIŞI — ekranda tek değişken kalır (gerekçe: CU frontal sırtı göstermez)
FİNAL TİPİ       MUĞLAK (yağmurla barışık mı, kanatsız mı — boş askı S45 + el S47)
SON PLAN TİPİ    ilk kadraja dönüş · kapanış sinyali yok (damla inmeye devam eder), kart 0
```

---

## 👤 KARAKTER KARTI — "kanatçı" (`KARAKTER_KARTI_VE_DAVRANIS` §1 · promptta ad YOK)

```
ROL           ısı hattı bakımcısı, kanatla uçarak dolaşır — S0-S1 (kanat takımı sırtta, eldiven damlaya)
İSTEK         yedek çekirdeği üsse getirip yuvaya oturtmak — S4 (parmak haritada karşı kıyıya)
BASKI TEPKİSİ KONTROL EDER — S3 (el mandalda durur-gevşer) · S5 (perdeyi ölçer) · S14 (perdeye bakar)
ALIŞKANLIK    kanat tokasını iki kez çeker (sağ eldiven, göğüs tokası) — S6 · S12 · (S15'te derecelenme:
              tokaya uzanır, bir an durur) → KIRILMA S29 (iki parmak tokaya gider, durur, kesici)
SINIR         çekirdeği bir daha bırakmaz — S13→S15 (uçuş yerine yürüyüş) · S29 (kanat yerine çekirdek)
ZAAF          kanat ucu çatlak S8+ · bacak ıslak/kabuklu S22+ · vizör tortusu S25+ · giysi kabuğu S31 ·
              adım yarım bot kısa S31 (yorgunluk 5)
TEL           vent tüyü uzar (kriz: S11 · S28) — dolgu değil, giysinin kendi göstergesi
İLK ↔ SON     S0 eldiven kalkar ↔ S47 eldiven kalkmaz (aynı kadraj, aynı el)
İNANDIRICILIK 6 soru: tutarlı ✅ · deneyimle değişiyor (S13→S15, S29) ✅ · çevrenin farkında (bakış
              nesneye) ✅ · amacı okunur (çekirdek elde) ✅ · kişilik (toka, kontrol) ✅ · tepki dışa (R 13) ✅
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı ·
> el · yürüyüş) ve `KURGU_RITMI §2` örüntü kırıcı — **ardışık iki sahne aynı
> ölçek + palet + ses dokusunda olamaz** (küme hariç: bir vuruşun iki klibi).
> Tam hesap: `00_ANALIZ/03_SAHNE_SIRALAMASI.md` (vuruş · B5 · palet · soru/cevap tipi · SON 3 s).

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S0 | İLK DAMLA | Eldiven kalkık, ilk yağmur damlası yavaş koşu temposunda (Dünya yağmurunun ~üçte biri) inip eldivene değer, beyaz kuru-kar yakası kalkar | A · ilk · 75mm · CU · eye-level close-up, frontal | tek diegetik: damlanın 'tok'u + kısa tıslama; müzik yok | şerit G · tempo Y · HOOK ⭐VİRAL |
| S1 | SÜZÜLÜŞ | Sırtındaki kanatlarla tepeden atlar, kalın havada göl yatağının üstünde bir tur süzülür | C · ilk · 24mm · WS · low angle wide shot | kanat membranı gerilim uğultusu, alçak; adım yok | şerit G · tempo H ·   |
| S2 | ÇENTİĞİN ÜSTÜ | Üs kapısına konar; kapı camında içerideki kırağı çizgisi işaretli çentiğin üstüne çıkmış | R · ilk · 35mm · MS · eye-level medium shot, three-quarter front | kanat kayışlarının gevşemesi, cam üstünde eldiven | şerit R · tempo N ·  ⭐VİRAL |
| S3 | SÖNÜK GÖSTERGE | İçeride ısı çekirdeğinin yuvası; gösterge sönük; eli kapağa gider, kapak soğuk | J · ilk · 75mm · CU · high angle close-up looking down | iç sessizlik: uğultu yok, kırağı çıtırtısı | şerit T · tempo Y ·   |
| S4 | HARİTA | Duvardaki haritada gölün karşısındaki eski istasyonu parmağıyla bulur; boş kanat askısı kadraj kenarında (TOHUM) | R · 🔁 dönüş · 35mm · MS · eye-level medium shot, three-quarter front | kırağı çıtırtısı, eldiven duvarda | şerit K · tempo N ·   |
| S5 | PERDE YARI YOLDA | Sırtta durur, gökten inen damla perdesine bakar; damlalar tepe hizasına yarı yolda (SAYAÇ 2 a-karesi) | B · ilk · 24mm · WS · high angle wide shot, full profile | ağır alçak ambiyans + uzak damla tıkırtısı | şerit R · tempo Y ·   |
| S6 | ATLAYIŞ | Kanat tokasını iki kez çeker (ALIŞKANLIK 1), tırmanır, sırtın ucundan boşluğa atlar | B · 🕰️ küme S5 · 24mm · WS · high angle wide shot, full profile | (küme S5) + kayış çekilme sesi | şerit G · tempo H ·   |
| S7 | PERDENİN ALTINDAN | Damla perdesinin altından göl yatağını geçer; bir damla kanada değer, beyaz yaka kalkar (novum doğrulama 2. nesne) | G · ilk · 24mm · EWS · low angle extreme wide shot, full profile | membran uğultusu + tek damla 'tok'u | şerit G · tempo N · NOVUM  |
| S8 | SERT İNİŞ | Eski istasyonun çatısına sert konar; kanat ucu kırağıya sürtüp çatlar (ZAAF 1) | G · 🕰️ küme S7 · 24mm · EWS · low angle extreme wide shot, full profile | (küme S7) + kırağı sürtünmesi, çatlak | şerit R · tempo H ·   |
| S9 | DONMUŞ KAPI | İstasyon kapısı donmuş; omuzla iter, kanat çubuğuyla zorlar; kapı bir el genişliği aralanır (DRAMATİK İRONİ başlar: arkasında damla perdesi alçalıyor) | I · ilk · 24mm · WS · eye-level wide shot, three-quarter front | omuz kapıda tok, kırağı kırılma | şerit G · tempo N ·   |
| S10 | KANAT İŞARETİ | Raftaki yedek çekirdeği bulur; üstünde kendi kazıdığı iki çizgili kanat işareti (HAFİF UÇ — metinsiz; SAPMA 2) | K · ilk · 35mm · MS · eye-level medium shot, full profile | iç sessizlik, eldiven rafta | şerit T · tempo Y ·   |
| S11 | AĞIRLIK | Kapı eşiğinde çekirdeği kaldırır; dizleri bükülür, kanatlar sırtında sallanır; kapı arkasından damla perdesi alçalmış | I · 🔁 dönüş · 24mm · WS · eye-level wide shot, three-quarter front | nefes omuzda, kırağı çıtırtısı | şerit G · tempo Y ·   |
| S12 | ÇATIYA | Çekirdeği kanat takımının göğüs kayışına bağlar, çatıya çıkar (ALIŞKANLIK 2: toka iki kez) | G · ilk · 24mm · EWS · low angle extreme wide shot, full profile | kayış, kırağı çıtırtısı | şerit G · tempo N ·   |
| S13 | ÇAKILMA | Çatıdan atlar; kanatlar çekirdeğin ağırlığıyla süzülemez, göl yatağına çakılır (BAŞARISIZ DENEME 1) | G · 🕰️ küme S12 · 24mm · EWS · low angle extreme wide shot, full profile | (küme S12) + çakılma toku, kırağı | şerit D · tempo H ·   |
| S14 | YERDE | Kırağıda yatarken damla perdesi alçalmış (ironi kapanır — o da görür); kalkar, çekirdeği çözer | N · ilk · 24mm · WS · low angle wide shot, full profile | nefes omuzda, kayış tokası | şerit R · tempo Y ·   |
| S15 | KANATLAR YERE | Kanatları sırtından çıkarıp yere serer; çekirdeği kanat yüzeyine kayışlar (MERKEZÎ SEÇİM: uçmak ↔ taşımak — iki nesne kadrajda) | O · ilk · 50mm · MS · high angle medium shot looking down | kayış sürtünmesi, membran çıtırtısı | şerit K · tempo Y · DORUK-1 (seçim)  |
| S16 | ÇEKİŞ | Kanat kayışını omzuna alır, kızağı çekmeye başlar; üs ufukta puslu leke | P · ilk · 24mm · WS · eye-level wide shot, three-quarter front | kızak kırağıda sürtünme, nefes | şerit R · tempo N ·   |
| S17 | KABUK | İlk damlalar kızağa ulaşır; ıslanan kanat yüzeyine kuru kar yapışır, kızak ağırlaşır (novum 3. nesne) | O · 🔁 dönüş · 50mm · MS · high angle medium shot looking down | damla 'tok'ları (birkaç), sürtünme ağırlaşır | şerit R · tempo N ·   |
| S18 | KAZIMA | Durup kabuğu kanat çubuğuyla kazır; kazıdıkça yeni damlalar iner (BAŞARISIZ DENEME 2) | P · 🔁 dönüş · 24mm · WS · eye-level wide shot, three-quarter front | kazıma sürtünmesi, damla | şerit D · tempo H ·   |
| S19 | KESİM | Kazımayı bırakır, kanadın kabuklu ucunu bilek kesiciyle keser; parça düşer ve yerde kalır; kızak küçülür (SEÇİM 2) | O · 🔁 dönüş · 50mm · MS · high angle medium shot looking down | kesici hırıltısı, membran yırtılma, parça düşüş toku | şerit K · tempo H ·   |
| S20 | UZAKTA YERE | Arkasından: göl yatağının uzak ucunda yağmur yere değer, çukurlar koyu sıvıyla dolmaya başlar (ortamın kalıcı değişimi) | Q · ilk · 24mm · WS · eye-level wide shot, back to the lens | uzak ağır damla toku dizisi | şerit R · tempo N ·   |
| S21 | GERİDE KALAN | Kesilen kanat parçası kırağıda kalır; bakımcı arkasına bakmadan çeker (KARAR: reddedilen nesne kadrajda) | O · 🔁 dönüş · 50mm · MS · high angle medium shot looking down | sürtünme, damla | şerit G · tempo N ·   |
| S22 | ÇUKUR | Ayağı çukura girer; giysinin bacağı sıvıya değince ıslanıp koyulaşır, kuru kar yapışır, ağırlaşır (ZAAF 2) | N · ilk · 24mm · WS · low angle wide shot, full profile | sıvı ağır çalkantı, kısa | şerit R · tempo Y ·   |
| S23 | YARI YOL | Bacağını çekip çıkarır, buzu çubukla kırar; ilerler, üs yarı yolda | R · ilk · 35mm · MS · eye-level medium shot, three-quarter front | kabuk kırılma çıtırtısı, nefes | şerit G · tempo N ·   |
| S24 | DAMLALARIN ARASINDA | Damla perdesi omuz hizasında; her adımda kaskına damla değip beyaz tortu bırakıyor (TEK KARE) | R · 🕰️ küme S23 · 35mm · MS · eye-level medium shot, three-quarter front | (küme S23) + kaskta 'tok'lar | şerit G · tempo N · NOVUM (tek kare) ⭐VİRAL |
| S25 | VİZÖR | Vizör çerçevesinde kuru-kar tortusu büyür; eldiven tersiyle siler, görüş daralır (tema: ayna/kabuk) | S · ilk · 75mm · CU · eye-level close-up, frontal | eldiven camda sürtünme, nefes | şerit R · tempo Y ·  ⭐VİRAL |
| S26 | KIZAK KAYAR | Kızak bir çukurun kenarında kayar, çekirdek koyu sıvıya yarı gömülür | T · ilk · 35mm · MS · high angle medium shot, three-quarter rear | kızak kayma, sıvı çalkantı | şerit R · tempo H ·   |
| S27 | ÇAKILI | Kayışı çeker, kızak sıvıda çakılı kalır; kanat gövdesi metana batmış (BAŞARISIZ DENEME 3) | T · 🕰️ küme S26 · 35mm · MS · high angle medium shot, three-quarter rear | (küme S26) + kayış gerilim, sıvı | şerit D · tempo H ·   |
| S28 | BELE KADAR | Çukura girer, sıvı bele çıkar; giysisi ıslanıp kuru kar tutar, hareketi yavaşlar | T · 🕰️ küme S27 · 35mm · MS · high angle medium shot, three-quarter rear | (küme S27) + ağır çalkantı | şerit G · tempo Y ·   |
| S29 | KAYIŞI KESER | Elini tokaya götürür, iki parmak durur (KIRILMA); çekirdeğin kayışını keser, çekirdeği kucağına alır; kanatları çukurda bırakır (BEDEL) | Y · ilk · 75mm · CU · eye-level close-up, full profile | kesici hırıltısı, kayış ayrılır, sıvı | şerit B · tempo Y · BEDEL ⭐VİRAL |
| S30 | BATIŞ | Kanat takımı sıvı metana batar; bakımcı çekirdekle çukurdan sürünerek çıkar | T · 🔁 dönüş · 35mm · MS · high angle medium shot, three-quarter rear | sıvı çalkantı, sürünme | şerit R · tempo N ·   |
| S31 | AYAĞA | Çekirdek kucakta ayağa kalkar; kuru-kar tutmuş giysi çatırdar, adım kısalır (yorgunluk 5) | V · ilk · 24mm · WS · eye-level wide shot, full profile | kabuk çatırtısı, adım | şerit G · tempo Y ·   |
| S32 | HER YERDE | Yağmur artık her yerde; damlalar önünde ve arkasında yere değiyor (novum sonuç) | V · 🕰️ küme S31 · 24mm · WS · eye-level wide shot, full profile | (küme S31) + yakın damla tokları | şerit G · tempo N ·   |
| S33 | ŞERİT DARALIR | Çukurlar birleşip göl olmaya başlar; kuru şerit daralır, bakımcı şeride sapar (SEÇİM 3: yol) | V · 🕰️ küme S32 · 24mm · WS · eye-level wide shot, full profile | (küme S32) + sıvı yayılma | şerit K · tempo N ·   |
| S34 | SICAK | Çekirdeği yere koyup soluklanır; koyduğu yerde kırağı erir, buhar yakası kalkar — çekirdek sıcak | O · ilk · 50mm · MS · high angle medium shot looking down | buhar tıslaması, nefes | şerit R · tempo Y ·   |
| S35 | GÖĞSE | Sıcak çekirdeği göğsüne bastırır; giysinin ön kabuğu pul pul dökülür, kollar açılır (umut-önce-düşüş tepesi) | Y · ilk · 75mm · CU · eye-level close-up, full profile | kabuk dökülme çıtırtısı, uzun nefes | şerit R · tempo Y ·  ⭐VİRAL |
| S36 | ERİYEN İZ | Çekirdeği göğsüne sarılı taşır; arkasındaki eriyen iz yeniden donar | O · 🔁 dönüş · 50mm · MS · high angle medium shot looking down | adım, buhar | şerit G · tempo N ·   |
| S37 | YAMAÇ | Sırt yamacına varır; yamaç kırağı, her adım kayar, geri kayar | Z · ilk · 24mm · WS · high angle wide shot looking down, three-quarter front | kırağı kayması, nefes | şerit G · tempo N ·   |
| S38 | GERİ KAYAR | Çekirdeği yamaca yuvarlar, ardından tırmanır; çekirdek geri kayar, bota dayanıp durur (BAŞARISIZ DENEME 4 · SAPMA 1) | AA · ilk · 35mm · MS · low angle medium shot, full profile | yuvarlanma, kırağı, bota dayanma toku | şerit D · tempo H ·   |
| S39 | DİZ ÜSTÜ | Çekirdeği kucaklayıp diz üstü tırmanır; kabuk kırılır, giysi tepeye kadar dayanır (HOBSON: tek yol) | Z · 🔁 dönüş · 24mm · WS · high angle wide shot looking down, three-quarter front | kabuk kırılma, diz kırağıda | şerit K · tempo H · DORUK-öncesi  |
| S40 | TEPE | Tepeye çıkar; arkasında göl yatağı sıvıyla dolmuş, eski istasyon karşıda ada (ölçek kontrastı) | AB · ilk · 24mm · EWS · high angle extreme wide shot, three-quarter rear | uzak sıvı, rüzgâr yok, nefes | şerit R · tempo Y ·   |
| S41 | KAPI | Üs kapısı donmuş; çekirdeği kapıya dayar, kırağı erimeye başlar; kapı bir el genişliği aralanır | AC · ilk · 24mm · WS · eye-level wide shot, three-quarter front | buhar tıslaması, kapı sürtünme | şerit G · tempo N ·   |
| S42 | TAVANA YAKIN | İçeride kırağı çizgisi tavana yaklaşmış (SAYAÇ 1 b-karesi); çekirdeği yuvaya taşır, kapağı zorlar | AD · ilk · 35mm · MS · high angle medium shot, three-quarter rear | iç sessizlik, kapak sürtünme | şerit G · tempo N ·   |
| S43 | OTURUR | Çekirdek yuvaya oturur (TEMAS · DEĞİŞİM · SONUÇ aynı klipte); klip gösterge sönükken biter — gösterge sınırda yanar | AD · 🕰️ küme S42 · 35mm · MS · high angle medium shot, three-quarter rear | (küme S42) + oturma tıkırtısı | şerit K · tempo Y · DORUK  |
| S44 | ERİME | Gösterge yanık; duvardaki kırağı erimeye başlar, içeride damlalar hızla yere düşer (iki hız: iç su damlası hızlı, dış yağmur yavaş) | AD · 🕰️ küme S43 · 35mm · MS · high angle medium shot, three-quarter rear | (küme S43) + hızlı damla şıpırtıları | şerit R · tempo N ·   |
| S45 | BOŞ ASKI | Boş kanat askısının önünde durur; askıya kesik kayış ucunu asar (FİNAL VURUŞ 2 · tema ödeme) | AE · ilk · 75mm · CU · eye-level close-up, three-quarter front | kayış tokası, sessiz | şerit B · tempo Y · FINAL-1 ⭐VİRAL |
| S46 | PENCERE | Pencereden bakar: yağmur gölü doldurmuş, karşı kıyı görünmüyor | AD · 🔁 dönüş · 35mm · MS · high angle medium shot, three-quarter rear | iç sessizlik + cam ardı uzak damla | şerit S · tempo N ·   |
| S47 | ELİNİ KALDIRMAZ | Dışarıda kapı önünde durur; damlalar kaskına değip beyaz tortu bırakır, elini kaldırmaz (KAFİYE: S0) | A · kafiye S0 · 75mm · CU · eye-level close-up, frontal | damlanın kaskta 'tok'u; müzik çözülmez | şerit S · tempo Y · FINAL ⭐VİRAL |

```
AÇI TİPİ SAYISI: 6 ≥3   (göz hizası · alt açı · üst açı · profil · dörtte üç ön · dörtte üç arka/sırt)
KURULUM SAYISI:  22 / 48 (ACI_YAYI §4: ≤24 ✅) — ⚠️ betik bölüm DOSYASI başına 12 sahnede 6 tavanı
                 uygular; dosya başına 7-8 kurulum çıkar. Film 48 sahnedir, tavan filme uygulanır;
                 dosya kesiği yazım birimidir, kurulum birimi değil [D74 gerekçesi].
KURULUM İSKELETİ: A C R J R B B G G I K I G G N O P O P O Q O N R R S T T T Y T V V V O Y O Z E Z F H L L L M L A
                 KÜME 7 (S5-6 · S7-8 · S12-13 · S23-24 · S26-27-28 · S31-32-33 · S42-43-44) ≥2 ✅
                 DÖNÜŞ 20/48 = %42 ≥%40 ✅ (dönüş = kaynağından ≤3 sahne sonra; küme klipleri dâhil)
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR kopyalanır + işaret satırını taşır:
                   dönüş → "— the same position, height and lens as Scene N."   (Scene n = S + 1)
                   küme  → "Continues the previous clip from its exact last frame — the same
                            position, height and lens as Scene N."
BÖLÜM KESİĞİ:    S11 ↔ S12 (I · WS · 45° ↔ G · EWS · 270°) · S23 ↔ S24 (küme — bilinçli, QA yarımı sınırı)
                 · S35 ↔ S36 (Y · CU · 90° ↔ O · MS · 0°) — üçü de ardışık çift kuralında
DAVRANIŞ ŞERİDİ: GGRTKRGGRGTGGDRKRRDKRGRGGRRDGBRGGKRRGGDKRGGKRBSS
                 G 17/48 · T 2 · D 4 · K 6 · B 2 · R 15 · S 2
TEMPO:           YHNYNYHNHNYYNHYYNNHHNNYNNYHHYYNYNNYYNNHHYNNYNYNY
⭐VİRAL (8):     S0 · S2 · S24 · S25 · S29 · S35 · S45 · S47 — her biri sahne tablosunda YÜZ + HAREKET satırıyla
KESİLEMEZ:       S43 (doruk) · S45 · S47 · 8 ⭐VİRAL · S1 (kanat referansı) · S15 · S29
```

### ⚓ ÇAPA ÜÇLÜSÜ (`OYUNCULUK_YAZIM` §2 → SPEC'e iner)

```
CHOICE  S15 · 3,0 s   BEFORE: iki eldiven kayışta, omuzlar kalkık, el tokadan bir avuç uzakta 2 s durur
                      AFTER:  eldivenler tokayı çeker, omuzlar her çekişte düşer; boş sırt askısı yerde kalır
COST    S29 · 2,0 s   BEFORE: sol eldiven tokada, iki parmak düz, bir parmak eksik, omuzlar yüksek
                      AFTER:  iki kol çekirdeği sarar, kesik kayış tokadan sallanır, omuzlar düşer ve düşük kalır;
                              kanat çubuğu sıvının altında kadrajda
FINAL   S47 · 1,0 s   BEFORE (S0): sağ eldiven göğüs hizasında kalkık, kaşlar kalkar
                      AFTER (S47): iki eldiven belde, kaşlar düz — aynı kanal (el + kaş), aynı kadraj
```

### 📈 BEDEL EĞRİSİ — yorgunluk 0-6 (D206 · D207)

```
S0-S5 0 · S6-S7 1 · S8 2 · S9 2 · S10 2 · S11 3 (@4 s omuz) · S12 3 · S13 4 · S14 4 · S15 3 · S16 3 (@4 s omuz) ·
S17 3 · S18 4 (@6 s kadans) · S19 4 · S20 4 · S21 4 · S22 5 (@3 s bacak) · S23 5 · S24 5 · S25 5 · S26 5 ·
S27 6 (@7 s üçüncü çekiş kısa) · S28 6 (@3 s nefes) · S29 6 · S30 6 · S31 5 (kalıntı) · S32 5 · S33 5 · S34 5 ·
S35 4 (dinlenme: çekirdek ısıtır — yazılı) · S36 3 · S37 4 · S38 5 (@2 s diz) · S39 5 (@3 s diz) · S40 5 · S41 5 ·
S42 5 · S43 5 · S44 4 · S45 4 · S46 3 · S47 3
ardışık düşüş ≤1 ✅ · tek dinlenme S34-S35 (yazılı olay: sıcak çekirdek)
```

---

## 🎙️ REPLİK TABLOSU (yalnız replikli filmde · `SES_VE_DIYALOG_URETIM` §1-§2a)

| # | S | saniye | konuşan | REGISTER | kanal | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | replik yok — film sessiz tasarımlı; ses tasarımı MUZIK dosyasında, AUDIO satırı her promptta |

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız o karenin
> `IN FRAME:` satırındaki kısmı gider. Videoya Bible girmez — `START FRAME:` tek satır.

### 👤 Character Bible
> arketip T (teknokratik form-fit — uçuş için) · kask düz pane + kalın koyu çerçeve · sırt: kanat takımı
> (S0-S14) → düz (S29+) · kir: kuru-kar tortusu global, S17'den · ad yok, rol etiketi "kanatçı"

```
FULL BODY:  A single figure in a close-fitting pale grey ribbed pressure suit, scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the chest, slim dark gloves and boots, and a low hard off-white helmet with a single flat front pane inside a thick dark rim.
TORSO:      her close-fitting pale grey ribbed pressure suit, matte scuffed composite chest and shoulder plates, a brushed-steel neck ring, one teal band across the upper chest, and the low hard off-white helmet with a single flat front pane inside a thick dark rim
FACE:       Her face is fully readable through the clear pane, zero tint, zero mirror, a soft warm fill from inside the rim: a woman in her thirties, dark cropped hair.
HANDS:      her slim dark segmented glove and the ribbed pale grey sleeve, a brushed-steel wrist ring where the glove meets the sleeve
WINGS ON:   On her back a folding wing rig, two dark smoke-grey membranes folded flat along her spine on a pale grey spar frame, held by one steel chest buckle; the rig is the only thing on her back and under it the back of the suit is one continuous smooth panel.
WINGS OPEN: her wing rig open, two taut dark smoke-grey membranes on a rigid pale grey spar frame spanning twice her arm-span, held by a chest harness with one steel buckle, the only thing on her back, the back of the suit under it one continuous smooth panel
BACK FLAT:  the back of the suit is one continuous smooth pale grey panel from collar to hip, a flat back silhouette carrying nothing
SLED:       the sled — the wing rig laid flat on the frost, two dark smoke-grey membranes on a pale grey spar frame, the core strapped on top
CORE:       a matt dark-metal cylinder the size of a small keg with a carry handle on each side
```

### 🌍 World Bible — DÜNYA ÇAPASI 3 cümle [D209], dış promptlara BİREBİR
```
GÖK:     An unbroken amber haze sky, no sun disc, no horizon glow.
UFUK:    A flat dark lakebed of pale-dusted ice to a soft horizon at eye level.
YER İMİ: the base dome on the ridge in the right third, three body-lengths tall, one dark door, one round window.   (dönüş yolu S14-S47)
         the old station in the left third, a low dark module barely taller than she is, one door, a flat roof.   (gidiş S5-S13)
RAIN:    Large sparse drops the size of marbles, few enough to count, fall through the frame at a slow jogging pace, far slower than rain on Earth, none streaking, none hanging still.
PUFF:    where a drop meets a warm surface a white puff rises to knee height and falls back as dry snow within two seconds.
ANATOMİ KARTI (KART 13): üs = 1 kubbe (5,3 H) · 1 kapı · 1 pencere · 1 anten (kadraj dışı) ·
         istasyon = 1 alçak modül (3 H) · 1 kapı · düz çatı — sayı film boyu sabit; metre SPEC D'de
```

### 🎥 Camera Bible
```
22 kurulum, her biri sabit lockoff; CAMERA cümleleri 03_SAHNE_SIRALAMASI §4b'de BİREBİR.
Video CAMERA satırı: "<kurulum cümlesi>, deep focus, fixed lockoff — absolutely zero camera movement.
[dönüş/küme işareti] In a single continuous shot."
Her video TIMELINE'ının son satırı SÜRDÜRME; "holds/settles/still" yazılmaz.
```

### 💡 Lighting Bible — IŞIK TAKVİMİ (D193)
```
DIŞ (S0-S2 · S5-S41 · S47): LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.  — saat yok (pus dolgusu, tepe), ~5000 K amber-gri, film boyu SABİT
İÇ ÜS (S3-S4 · S42-S46):    LIGHT: one warm ceiling panel inside, soft and steady, the frost on the walls lit evenly, no glare.  — 3200 K, tek tavan paneli, sabit yön
İÇ İSTASYON (S10):          LIGHT: dim grey-blue inside the station, the amber haze fill spilling in through the open door.
geçişler OLAY: S2/S3 · S4/S5 · S9/S10 · S10/S11 · S41/S42 · S46/S47 — takvim geri sarmaz; S44'te ışık değil damla değişir
```

### ⚙️ Physics Bible
```
DIŞ:   PHYSICS: Gravity is 0.38 g under a dense cryogenic nitrogen-methane atmosphere at 0.9 bar and 95 kelvin; the dense air slows the rain to a slow jogging pace while any solid thing let go falls fast; dust settles at once, no wind.
İÇ:    PHYSICS: Inside the pressurised base at about one atmosphere, gravity is 0.38 g; the frost on the walls is real ice and any meltwater drips fall fast.
İST.:  PHYSICS: Inside the unheated station at about one atmosphere, gravity is 0.38 g; frost coats every surface and nothing drips.
SES:   AUDIO: sound carries low, heavy and close in the dense cold air — each drop a soft dull tick, each contact a dull thud, no high frequencies. No dialogue. No music.
       AUDIO: near silence inside — a faint crackle of frost, her breathing inside the helmet, no hum. No dialogue. No music.
DÜŞÜŞ TABLOSU (SPEC C): damla — sürüklenme sınırı ~3 m/s SABİT (bilye boyu, kalın hava) · bırakılan katı
       nesne — 0,38 g serbest düşüş: eldiven boyu (~0,3 m) 0,4 s · diz boyu (0,5 m) 0,5 s · çekirdek yamaçtan
       kayış: ivmeli, sürtünmeli; iç mekân su damlası: serbest düşüş (hızlı)
UÇUŞ:  kanat açıklığı iki kol boyu; yoğun havada (~3 kg/m³) 0,38 g'de süzülme mümkün, çırpma yok;
       yükseklik kaybı gövde boyu / 2 s; çekirdekle (+kütle) süzülemez → S13 düşüş
SIVI:  metan sıvısı 95 K'de durgun, koyu, mat; sıvıya değen soğuk yüzey ISLANIR (koyulaşır), donmaz;
       sıcak yüzeyde (eldiven · kask çerçevesi · vent · çekirdek) damla buharlaşır → puf 0,5 m / 2 s → kuru kar
       geri düşer; giysi ve kızaktaki BEYAZ TORTU = bu kuru kar (kabuk)
VENT:  giysinin sırt ventinden kuru kar tüyü — ısı sayacı (S1 kısa · S16 orta · S28 uzun · S35 kısa)
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin ortam/tür/risk yasakları
> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (8 cümle) + sahne başına ≤3 cümle.
```
ÇEKİRDEK (her promptta): §5.1 sekiz cümle (image yedi)
SAHNEYE ÖZEL (≤3):
  MÜHÜR (her insanlı prompt): No bare skin anywhere — none above the collar, none at the wrist between glove and sleeve, none at the ankle between boot and leg, every seal ring visible.
  DIŞ: No sun disc, no lens flare, no wind, no hard black shadow, no falling snow other than the named puffs.
  İÇ:  No screen, no readout, no digits on the socket or the lamp — the lamp is one plain point of light.
  KANAT (S1-S13): No back-mounted tank, hose or cable — the folding wing rig is the only thing on her back.
  SIVI (S20-S33 · S40 · S46): The dark liquid stays flat and matte, no ripples, no waves, no flow.
HAVUZ (PLAN'da kalır, prompta girmez): "seamless / bubble / dome / glow / glowing / swirl / cinematic lighting /
  hundreds of" hiçbir prompta yazılmaz [§7]; kubbe vizör · aynalı vizör · sırt ünitesi · ikinci figür ·
  başlık kartı · HUD/lens verisi · Dünya yağmuru çizgisi · asılı toz perdesi · alev/duman · çıplak deri ·
  akan/dalgalanan sıvı · rüzgârda dalgalanan kumaş · maket/tilt-shift okuması · kırmızı acil ışık.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| İNSAN SAYISI | tam 1 insan × 48 sahne | KART 4 | hepsi |
| KASK TAKVİMİ | kapalı 48, açık 0 | KART 3 | hepsi |
| DAMLA | bilye boyu · seyrek (birkaç düzine) · ~3 m/s sabit · kadrajı ~2 s'de geçer (WS) · puf 0,5 m / 2 s | KART 6 · A5 | S0 · S7 · S17 · S24 · S32 (+ kısa: dış sahneler) |
| YERÇEKİMİ | 0,38 g · katı nesne serbest düşüş eldiven boyu 0,4 s · damla sabit hız | D200 · KART 6 | S13 · S38 · S44 (iç hızlı) |
| SIVI TEMASI | 5 sahne (S22 · S26 · S27 · S28 · S29-S30 kenar), gerisi arka plan | KART 1 | S20-S33 · S40 · S46 |
| KANAT | 2 membran · 1 çubuk iskeleti · 1 toka · açıklık 2 kol boyu · sırtta S0-S14 / kızak S15-S28 / yok S29+ | KART 3 · D208 | S1-S30 |
| YAPI | üs 1 kubbe · 1 kapı · 1 pencere (5,3 H) · istasyon 1 modül · 1 kapı · düz çatı (3 H) | KART 13 | S2-S5 · S8-S13 · S40-S47 |
| SAYAÇ 1 | kırağı çizgisi: S2 çentik üstü → S42 tavana bir el → S44 erir; a/b S3 ↔ S42 | KART 5 · D78 | S2 · S3 · S42 · S44 |
| SAYAÇ 2 | damla perdesi: S5 yarı yol → S14 baş üstü → S24 omuz → S32 yerde; a/b S5 ↔ S24 | KART 5 · D78 | S5 · S9 · S11 · S14 · S24 · S32 |
| GÖSTERGE | tek yuvarlak lamba, sönük S3-S43 / yanık S44+ (sınırda) | KART 5 | S3 · S43 · S44 |
| KESİK KAYIŞ | 1 adet, bir el boyu, çelik toka — S29'dan S45'e | D141 | S29 · S45 |
| ALIŞKANLIK | toka iki kez: S6 · S12 (· S15 derecelenme) · S29 kırılma | KARAKTER_KARTI §2 | S6 · S12 · S15 · S29 |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

> Kaynak ve uygulama: `00_ANALIZ/01_QA_DERS_HASADI.md` §1 (aynı 20 satır).

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D200 | damla sabit hız ↔ katı nesne ivmeli; PHYSICS iki hızı adlandırır; SPEC C düşüş tablosu | her video PHYSICS · SPEC C · S13 · S38 · S44 |
| D157 | taşıyıcı damla × eldiven; TEK KARE S24; damla perdesi ≥1/10; novum sahnesinde rakip olay yok | S0 · S7 · S17 · S24 · S32 üçüncü satır |
| D192 | 1 no. risk damla: sayılı pozitif cümle + göz kapısı | novum cümlesi · SPEC E |
| D179 | S15/S29 imaj = 0,0 s; sonraki imaj AFTER; kurulum MS/CU | S15 O · S29 Y · S16/S30 imaj |
| D202 | ÇAPA ÜÇLÜSÜ omuz+el saniyeli; efor sahnesinde ödeme satırı [+ders 206] | PLAN çapa bloğu · TIMELINE'lar |
| D207 | yorgunluk 0-6, ardışık düşüş ≤1, kalıntıyla açılış | BEDEL EĞRİSİ · S14 · S23 · S30 · S31 · S39 imajları |
| D208 | KİMLİK DİZİSİ (kask · kanat/kızak/yok · tortu bölgeleri) [+ders 42] | SPEC C |
| D209 | DÜNYA ÇAPASI 3 cümle birebir | World Bible · dış image promptları |
| D211 | S0 sorusu · ilk 30 s ≤2 kurulum (+1 gerekçeli) · FİNAL VURUŞ KANITI gösterge + kayış [+ders 141] | HOOK bloğu · SPEC B |
| D213 | TEMAS·DEĞİŞİM·SONUÇ aynı klipte, sonuç ≥1 s, temas ilk 2 s | S9 · S12 · S15 · S19 · S29 · S35 · S43 TIMELINE |
| D174 | yön nesneye [+ders 104] (dome right third / station left third); ikinci cisim teyit | dış promptlar |
| D176 | zemin rengi tek yerde (World), LIGHT renk atamaz | LIGHT satırları |
| D175 | üç bölgeli çıplak-deri negatifi; zorlanma kumaş üstünde | her insanlı NEGATIVE |
| D139 | kanatlı sırt pozitif [+ders 146] · kanatsız 'flat back silhouette carrying nothing' · kask düz pane + çerçeve | Bible · back sahneleri |
| D169 | efor sahnelerinde ≥2 kanal (gövde · kadans · eldiven · nefes) | S11 · S16 · S18 · S19 · S27 · S28 · S31 · S37 · S39 |
| D210 | [+ders 62 · 70] S47 CAMERA = S0 + işaret; son satır sürdürme; KESİLEMEZ; kurgu kapısı 48 · 480 s · kart 0 | S47 · her TIMELINE · SPEC B |
| D212 | ardışık vuruş tekrarı 0; klip tekrarı 0 | sahne haritası vuruş sütunu |
| D214 | [+ders 167] IN FRAME ilk satır; insert'te yüz yok; yüz ≤3 öznitelik, yalnız 10 yüz sahnesinde | her prompt |
| D193 | ışık takvimi: dış sabit · iç 3200 K · geçişler olay | Lighting Bible · SPEC C |
| D78 | iki metinsiz sayaç, a/b kare çiftleri; bedel nesnesi siluet testi (koyu kanat ↔ açık giysi) | SAYAÇ satırları · S15/S29/S45 |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle (boşsa "—")

| ders | neden bu filmde uygulanmadı |
|---|---|
| D198 | 0 g karesi yok (§3.9: hiçbir kare 0 g değil) |
| D201 | vakum yok, güneş diski yok — pus dolgusu |
| D203 · D217 | replik yok |
| D216 · D180 | MUZIK dosyasına yazılır (katman ≤4 · köprü ≥0,2 s · dijital sıfır 0); planlı sessizlik yok — kilit sayımına girmez |
| D172 | kanat kayışları iki uçlu adlandırıldı (göğüs tokası ↔ kanat kökü) — D139 kilidinin içinde taşınır |
| D138 | §5.1 metin yasağı KAPSAMLI cümle + gövde-boyu dili çekirdekle kapanır |
| D34 · D45 | ad/etiket hiçbir promptta yok — çekirdek kural |
| D215 | üretim defteri üç kutu — üretim tarafı |
| D16 | D214/D167 yüz kilidinin içinde; FACE LOCK paragrafı V3'te yazılmaz (bütçe) |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S38 (çekirdek yamaçtan geri kayıp figüre doğru gelir) — ikinci: S28 (bele kadar sıvı)
NÖTR TARİFİ:         S38 — "the core slides back down the frost slope and stops against the sole of her
                     braced boot; she stands beside its path, not below it; her face fully readable"
                     S28 — "she stands waist-deep in the dark still liquid beside the sunk sled, seen from
                     above and behind, the far edge of the lakebed visible past her"
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| S38 darbe fiili (dize çarpma) kaldırıldı → bota dayanma (SAPMA 1, sahip onayı) | "çekirdek beni de yıkabilir" acısı | ④ temassız gövde tepkisi: diz bükülür, omuz düşer · ① kütle-hız: çekirdek yamaçta hızlanır, kırağıda oluk bırakır, tok ses |
| kesme aleti adlandırılmadı (blade/knife yok) | 0 | ③ alet tepkisi: "hooked cutter on her wrist parts the strap" — işlev görünür |
| S10 kazınmış YAZI (HAFİF UÇ) → kanat işareti (SAPMA 2, sahip onayı) | sözcüğün açıklığı | ② malzeme sonucu: iki çizgili kazı = kanat; S45 askıyla kafiye |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
```

---

## ✅ ÜRETİM ÖNCESİ KONTROL — THE_SLOW_RAIN            tarih: 22.09.2026

```
A0 ✅ HİKÂYE ONAYI: ONAY 22.09.2026 · TUR 1/3 · satır 48 = sahne 48 · jargon yok · SAPMA: 2, yeniden onaylı 22.09.2026
A1 ✅ "no text" ile ekran içeriği aynı dosyada YOK (gösterge tek ışık noktası, kırağı çizgisi işaretsiz)
A2 ✅ sahne sayısı: başlık 48 = blok 48 = "Scene N of 48"
A3 ✅ süre: 48 sahne × 10 s = 480 s (klip süresi VARSAYIM — araçtan ölçülür)
A4 ✅ yasaklı sahne tipi taraması: biniş-iniş yok · loş mekâna giriş S9/S10 → pus dolgusu kapıdan içeri (tek ışık değil) ·
     ayna yok · türetilmiş fenomen yok (novum damla, somut) · yokluk novumu yok · jenerik kartı 0 [D77]
A5 ✅ 1 no. risk (damla) sayıyla: bilye · seyrek · yavaş koşu · ~2 s kadraj · puf 0,5 m / 2 s
B1 ✅ doruk S43 içinde (oturma 3,0 s, sonuç ≥1 s), sahne arasına düşmüyor; gösterge sınırda
B2 ✅ bedelli seçim S15 · S29, kayıp S29-S30 görülüyor, S45 kaydı
B3 ✅ TEMA: KİMLİK · motif sahneleri S1 · S10 · S15 · S19 · S25 · S29 · S45 · S47 (S29 listede)
B4 ✅ kurulum dizisi 22 harf · açı tipi 6 · ardışık çift 37/37 + 10 küme · şok 1/2 · KÜME 7 · DÖNÜŞ %42
B5 ✅ İSTEK çekirdeği getirmek · ENGEL yağmur+ağırlık · BEDEL kanatlar S29 · MUHATAP geçmiş karar + beden + ortam
B5b — tek insan
B6 ✅ POLİTİKA SATIRI S38/S28 · üç önlem üçlüyle · milliyet/kurum/ad YOK
C  ✅ sayısal kilit listesi (12 satır)
D  ✅ risk sayımı 7/14 → kilit tavanı ≤20 uygulandı (20 + 9 uygulanmayan)
E  ✅ QA SPEC bloğu — THE_SLOW_RAIN_QA_SPEC.md
```
