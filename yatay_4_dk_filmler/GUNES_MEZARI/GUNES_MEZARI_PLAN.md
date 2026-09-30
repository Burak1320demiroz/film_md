# 🎬 GUNES_MEZARI — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 4 dk — 24 KLİP × 10 s · 2 bölüm dosyası (§2.3 · ÇOK KLİPLİ SAHNE)
ORTAM:         §3.9 KRİYOJENİK ORTA BASINÇ (95 K · 0,90 bar N₂ · 0,38 g)
               + KURU/BERRAK alt bandı — üç sapma D74 ile kayıtlı (00_ANALIZ §2b)
TÜR:           bilimkurgu   (tek açık dal — §4.1) · görsel ton: gotik
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
               PLAN 10,0 s ızgarasıyla yazıldı; ölçüm 10,0 değilse RUNTIME ve
               SPEC A/B düzeltilir, PLAN değil.
SAHNE SAYISI:  7 SAHNE · 24 KLİP      RUNTIME: 240,0 s = 24 × 10,0
LOGLINE:       Yıllar önce bir şehrin güneşini kafese kapatan kaptan onu geri
               getirir; salıvermenin tek yolu kendi gemisini sökmektir.
```

---

## 🎭 TEMA

```
TEMA: FEDAKÂRLIK
      — "Bir şeyi geri veren, geri veremediklerinin önünde bekler."
      ⛔ TAKAS kalıbı değil TANIM cümlesi [§3c moratoryumu]

MOTİF SAHNELERİ: S1 · S2 · S3 · S5 · S6 · S7   (indeksler aşağıda kanal kanal)
      ① NESNE KANALI — ışık taşıyan kafes:  K02 (halkalar tutuyor) ·
        K19 (kaide devralıyor) · K21 (halkalar bırakıyor)
      ② KİNESİK KANAL — avucu bir yüzeye düz basmak: K08 (duvar) ·
        K12 (levha) · K19 (çekirdek) → K20'de KIRILIR (avuç gitmiyor, çubuk gidiyor)
      ③ IŞIK KANALI — taşınan tek fener → kaideden yayılan sabah:
        K03 (aşağıdan gelen kızıl-altın) · K22 (ışığın kenarı iniyor) ·
        K23 (ışık var, kimse yok)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Bir güneş taşınabilir: beslenen bir kafes onu sıkıştırıp
                     tutar, ve kafes değişirse güneş el değiştirir.
NOVUM TİPİ:          ÖLÇEK  ⚠️ üst üste ikinci ÖLÇEK film (00_ANALIZ §3 notu)
NOVUM TAŞIYICISI:    üç halkalı kafes × anahtar çubuğunu iki elle sürüp omuzla
                     çevirmesi → halkalar dışa açılır ve bir güneş aralarından
                     sıyrılıp yükselir
                     ⭐ TAŞIYICI NESNE = ÜÇ HALKALI KAFES (anahtar çubuğu jestin
                     aleti, taşıyıcı değil) — TEK KARE cümlesi bu nesneyi
                     ADIYLA içerir [D157]
TEK KARE (§4①):      "Bir geminin sırtındaki KAPI BOYUNDAKİ tek aydınlık
                     pencerenin altında, ÜÇ HALKALI KAFESİN içine sıkıştırılmış
                     kızıl bir GÜNEŞ." — taşıyıcı nesne (üç halkalı kafes)
                     cümlede ADIYLA geçiyor ve ölçek İKİ UCUYLA aynı karede (K02)
KİNETİK BAĞIMSIZLIK: ✅ kural yalnız görüntüyle kanıtlanır: halkalar kapanıyor
                     (tutuyor) → kaide ışık alıyor (devraldı) → halkalar
                     açılıyor (bıraktı) → küre yükseliyor. Replik, dış ses,
                     ekran metni GEREKMİYOR.
BAŞLIK ŞEMASI:       "A Sun Is Something You Can Carry" (5 kelime)
```

### 🧪 KURGU SÖZLEŞMESİ — üç satır, film boyunca değişmez

```
① Küre kendini tutamaz. Onu daima BESLENEN bir kafes tutar ve SIKIŞTIRIR.
   İmparatorluğun üç halkası taşınabilir kafestir; şehrin kaidesi sabit
   kafestir. Beslenme kesilirse küre SÖNER — patlamaz, söner.
② TAŞIMA HÂLİ    kısık, koyu kızıl-altın; üç halkanın iç açıklığının 4/5'i;
                 bir yüzü aydınlatır, bir şehri aydınlatmaz
   ÇALIŞMA HÂLİ  kaide devraldığında açılır, genişler, kaidenin alanında
                 yükselir; gökte bir kol boyu tutulan tırnak genişliğinde disk
③ DEVRALMA SIRASI TERSİNE ÇEVRİLEMEZ: kaide beslenir → kaide tutar →
   halkalar açılır. Halkalar önce açılırsa küre söner.

⛔ SINIR — kural YALNIZ küre içindir. Küre dışında hiçbir şey havada durmaz;
   her PHYSICS satırı bunu taşır: "anything she lets go falls and reaches the
   ground in about a second." [KEPT_LIGHT ⑩'da sınır sızdı, film saptı]
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Geminin güç çekirdeğini şehrin salıverme kaidesine bağlamak ve
              küreyi salıvermek — film başlamasa da var olan bir İŞ
   □ ENGEL:   ENERJİ (tek engel): kaide sağlam ama ölü; gezegende çalışan tek
              kaynak kendi gemisinin çekirdeği
   □ BEDEL:   Gemisi — S5 · K17 (çekirdek yataktan çıkar, gemi bir daha
              kalkamaz) ve S6 · K20 (kilidin yuttuğu tek anahtar harcanır)
              ⭐ İkinci kayıp S7 · K23: sabah gelir, kimse çıkmaz — sürpriz
              değil, K10-K12'de sezilenin kesinleşmesi
   □ MUHATAP: KENDİ GEÇMİŞ KARARI — kuledeki kayıt (K11) ve geminin anahtarı
B5b □ AYRILIK: — (tek insan)
B2a MERKEZÎ SEÇİMDEN SONRAKİ SEÇİM: 1 (K20 — anahtarı saklayabilirdi)
B2b BAŞARISIZ DENEME: 2 (K13 kaidenin kolu · K19 çekirdek ilk bastırmada tutmaz)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  ① REFERANS PAKETİ (6 kayıt onaylanır — KAPI 0)
  ② K21  DORUK + en red-riskli kare
  ③ K17  merkezî seçimin bedeli
  ④ K24  kapanış imajı (K01'in kamera cümlesini birebir taşır)
  ⑤ K01  hook
  ⑥ kalan 19 klip
⛔ İLK KABUL satırı K21 DEĞİLSE ikinci klip üretilmez.
⛔ İPTAL KAPISI: K21 — halkaların açılması ve kürenin yükselmesi üç denemede
  de ateş topu / korona / lens parlaması olarak çıkarsa TAŞIYICI DEĞİŞİR.
  PLAN B: küre K21'de kadraja HİÇ girmez, halkalar boş göğe açılır ve
  salıverme yalnız IŞIĞIN GELMESİYLE anlatılır (K22 birincil kanıt olur).
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR (KILAVUZ_REHBERI §2.1)

```
— bu film YATAY; üç satır geçerli değil.
① BİLGİ ASİMETRİSİ (yatayda da yazılır): TERS İRONİ · karakter biliyor,
  izleyici K11'e kadar bilmiyor · asimetri anı 1:30 · süre 90 s.
  Saklama YOK: K02'den itibaren üç işaret verilir (taşıyan o · şaşırmıyor ·
  kuleyi arar gibi değil bilir gibi yürüyor).
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | klip | boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | %0 | K01 | — |
| 2 | Kurulum | %0-10 | K02 · K03 | — |
| 3 | Katalizör | ~%11 · 26,0 s | K03 | bant %10-15 = 24-36 s ✅ |
| 4 | Tartışma | %12-40 | K04-K09 | — |
| 5 | Orta nokta | ~%46 | K11 · K12 | sahte yenilgi (kanıt) |
| 6 | Umut-önce-düşüş | %50-58 | K13 · K14 | — |
| 7 | Her Şeyin Kaybı | %70 | K17 | somut ve geri dönüşsüz ✅ |
| 8 | Final | %85-99 | K21 · K22 | doruk kurguya GİRMEK zorunda |
| 9 | Kapanış imajı | %100 | K24 | açılışın aynası |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       ÖLÇEK ŞOKU (tek tip)
S0 SORUSU:       "Bu nedir, ve neden bir kafeste?"
S1 İKİNCİ BİLGİ: K02 — kafes bir geminin altında ve gemi karanlık bir şehrin
                 üstünde: bu ışık BURAYA ait ve BURADAN gitmiş
İLK 2 SN SESİ:   tek diegetik ses — gerilen metalin alçak inlemesi
                 (müzik 0:00'da girmez; ilk müzik 0:20 bandında)
0. KARE:         120 px testinde siyahın içinde tek kızıl kavis — okunur ✅
İLK 30 s:        kurulum klibi 1 (K02) · soru K01'de ✅
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` ve `KURGU_RITMI §2`
> örüntü kırıcı. Sahne içinde palet ve ses yatağı AYNI kalır (sahne kilidi);
> fark yalnız kurulumdan gelir. Palet/ses farkı SAHNELER arasında aranır.

| K | S · rol | olay | kurulum | ölçek · açı | palet | ses | tempo | şerit |
|---|---|---|:--:|---|---|---|:--:|:--:|
| K01 | S1 1/3 KURULUM | kısık küre döner, metal inler | C | MS · üst açı | kızıl-altın/siyah | metal inlemesi | N | — |
| K02 | S1 2/3 EYLEM | küre üç halkada, gemi şehrin üstünde | I | WS · göz hizası | kızıl-altın/siyah | alçak uğultu | N | — |
| K03 | S1 3/3 TEPKİ | kokpit, yüz aşağıdan aydınlanmış, çağrı başlar | C · dönüş K01 | MS · üst açı | kızıl-altın/siyah | cızırtı + replik | Y | R |
| K04 | S2 1/6 BELİRİŞ | gemi inmiş, kaide ufukta, kızak yanda | I · dönüş K02 | WS · göz hizası | kırağı/bazalt | kuru kar | N | G |
| K05 | S2 2/6 MÜCADELE | heykellerin bacakları arasında yürüyor | F | MS · alt açı | kırağı/bazalt | bot + nefes | N | G |
| K06 | S2 3/6 TERSLİK | kapıya omzunu verir, menteşe kırağısı çatlar | G | WS · OTS | kırağı/bazalt | menteşe | Y | G |
| K07 | S2 4/6 DÖNÜŞ | sıcak oyuğun önünde diz çöker, buhar yakası | F · dönüş K05 | MS · alt açı | kırağı/bazalt | buhar | N | T |
| K08 | S2 5/6 KARAR | avucu kazınmış güneşte; hilal yanık izi | D | CU · göz hizası | kırağı/bazalt | eldiven-taş | H | T |
| K09 | S2 6/6 BEDEL | fener yerde, duvar boyu çizimler, diz çökmüş | C | MS · üst açı | kırağı/bazalt | nefes | Y | S |
| K10 | S3 1/3 KURULUM | salon boş, sıralar devrik, tek lamba | A | WS · göz hizası | mürekkep/tek ışık | çağrı en yüksek | Y | G |
| K11 | S3 2/3 EYLEM | levhada döngü: hilal yanıklı eldiven kolu çekiyor | C · dönüş K09 | MS · üst açı | mürekkep/tek ışık | makara + replik | N | — |
| K12 | S3 3/3 TEPKİ | eldiven levhayı avucuyla kapatır, tam sessizlik | D | CU · göz hizası | mürekkep/tek ışık | kesilme | Y | R |
| K13 | S4 1/2 KURULUM | kaidenin kolunu çeker, hiçbir şey olmaz | C · dönüş K11 | MS · üst açı | bazalt/fener | kuru klik | N | D |
| K14 | S4 2/2 SONUÇ | feneri yuvaya indirir, ölçü tutuyor | D · dönüş K12 | CU · göz hizası | bazalt/fener | fener | N | G |
| K15 | S5 1/3 KURULUM | çekirdek çalışıyor, rampa ovaya açık | F | MS · alt açı | amber/iç metal | çekirdek nabzı | N | T |
| K16 | S5 2/3 EYLEM | eli kalkış kolunda, kolu bırakır | H | CU · profil | amber/iç metal | boş dönüş | Y | K |
| K17 | S5 3/3 BEDEL | mühürleri çevirir, çekirdek çıkar, ışıklar söner | F · dönüş K15 | MS · alt açı | amber→kararan | mühür + sönme | H | B |
| K18 | S6 1/4 BELİRİŞ | eldiven çeki kayışında, uzak pencere karanlık | H · dönüş K16 | CU · profil | kararmış/kırağı | kızak | N | G |
| K19 | S6 2/4 MÜCADELE | çekirdek ilk denemede tutmaz, kırağı sıyrılır, kilitlenir | F · dönüş K17 | MS · alt açı | bazalt/uyanan taş | kilit | H | D |
| K20 | S6 3/4 KARAR | anahtar çubuğunu kilide sürer, omuzla çevirir | D | CU · göz hizası | bazalt/uyanan taş | çubuk | N | K |
| K21 | S6 4/4 BEDEL | kaide devralır, halkalar açılır, küre kadrajı terk eder | I | WS · göz hizası | kızıl-altın→beyaz | halkalar | H | R |
| K22 | S7 1/3 KURULUM | ışığın sert kenarı duvardan kaldırıma iner | C | MS · üst açı | sert altın/uzun gölge | ilk sabah | Y | S |
| K23 | S7 2/3 EYLEM | karanlık geminin yanında, boş sokağa bakıyor | A | WS · göz hizası | sert altın/uzun gölge | oda tonu | Y | S |
| K24 | S7 3/3 TEPKİ | oyuk ışıkta, içinde filiz | C · dönüş K22 + KAFİYE K01 | MS · üst açı | sert altın/bordo | tek nefes | Y | — |

```
AÇI TİPİ SAYISI: 5 ≥3 ✅  göz hizası (A·D·I) · üst açı (C) · alt açı (F) ·
                 OTS (G) · profil (H)
KURULUM SAYISI:  7 ≤12 ✅
KURULUM İSKELETİ: C I C I F G F D C A C D C D F H F H F D I C A C
                 DÖNÜŞ 10/24 = %41,7 ≥%40 ✅ · KÜME aranmaz (rejimde yok) ·
                 ardışık aynı kurulum 0 ✅ · ŞOK 1 (K20→K21, doruk) ≤2 ✅ ·
                 KAFİYE ilk harf C ↔ son harf C ✅
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR
                   kopyalanır + işaret satırı: "— the same position, height
                   and lens as Clip N."
SAHNE PLANI: 3 6 3 2 3 4 3
                 ⭐ ÇOK KLİPLİ SAHNE — toplam = CLIP COUNT (24). BU SATIR ㉜
                   KAPISINI AÇAR ve ⑩④ KÜME hedefini kapatır.
BÖLÜM KESİĞİ:    K12 ile K13 arasında — ⛔ bölüm sınırı da ardışık bir ÇİFTTİR
                 (D→C · ölçek Δ1 · azimut 55° · bant içi ✅) ve K12'nin TAM
                 SESSİZLİĞİNE denk gelir
```

### ⚓ ÇAPA ÜÇLÜSÜ  (`OYUNCULUK_YAZIM` §2 · SPEC'e blok olarak iner)

```
CHOICE  K16 · 4,0 s   kanal: EL + OMUZ
  BEFORE: eldiven kalkış kolunda kapalı, ağırlık ön botta, omuzlar yüksek
  AFTER:  parmaklar tek tek açılıyor, kol yerinde kalıyor, omuzlar iniyor
  REDDEDİLEN NESNE: kalkış kolu — K17 ve K18'de HÂLÂ kadrajda ve hiç çekilmiyor
COST    K17 · 7,0 s   kanal: OMUZ + NEFES
  BEFORE: iki avuç mühür halkalarında, omuzlar yüklü ve yukarıda
  AFTER:  çekirdek kollarında, omuzlar aşağıda, göğüs hızlı inip kalkıyor
FINAL   K23 · 6,0 s   kanal: EL + OMUZ  (CHOICE ile AYNI kanal — karşılaştırılabilir)
  BEFORE (K03): iki eldiven konsol rayında kapalı, omuzlar yüksek
  AFTER  (K23): iki eldiven açık ve boş, yanlarda; omuzlar bir kez daha iniyor
⛔ Fark kadrajın kısa kenarının ≥1/8'i: K16'da eldiven 0,25 m / 0,32 m = %78 ✅ ·
  K17'de çekirdek %78 ✅ · K23'te gövde 1,70 m / 5,06 m = %34 ✅
```

### ✂️ KESİLEMEZ LİSTESİ  [D62 · beş tekrar]

```
K01 (hook) · K02 (novum tek kare) · K11 (kanıt) · K12 (tepki + sessizlik) ·
K17 (bedel) · K20 (ikinci seçim) · K21 (doruk) · K23 (bekleyiş) · K24 (final)
⛔ ④ HİKAYE merceğinin kesme listesi bu dokuz klipten birine dokunuyorsa
  liste TARTIŞILMAZ, KAREYE bakılır [D151 · KEPT_LIGHT'ta iki kesme adayının
  ikisi de kilide çarptı, biri filmin doruğunu kesiyordu].
```

### 🧬 DAVRANIŞ ŞERİDİ · TEMPO  (`KARAKTER_KARTI` §4 · `OYUNCULUK_YAZIM` §4)

```
ŞERİT: — — R — G G T T S G — R D G T K B G D K — S S —
  insanlı 18 klipte G=5 (%27,8 ≤%50 ✅) · T 3 · D 2 · K 2 · B 1 · R 2 · S 3
  insansız 6 klip "—": K01 · K02 · K04 · K11 · K21 · K24 (ölçüm 25.09.2026)
  K'dan önce D/T ✅ (K15 T→K16 K · K19 D→K20 K) · K'dan sonra B/R ✅
  (K20 K → K21 insansız sonuç → K22 S; G gelmiyor)
  en az bir S ✅ · ilk harf (R) ≠ son harf (S) ✅
TEMPO: N N Y N N Y N H Y Y N Y N N N Y H N H N H Y Y Y
  ardışık üç aynı harf yok ✅ · değişim 14 ≥3 ✅ · CHOICE (K16 Y) çevresinden
  farklı ✅ · COST sonrası (K18 N) yavaş başlıyor ✅
```

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a)

| # | K | saniye | konuşan | REGISTER | kanal | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|
| 1 | K03 | 26,0 s | kayıt cihazı | RECORDED HUMAN | bant-limitli, uzak, bozuk | MUHATAP — ekranda hiç olmayan ÇOCUKLAR + artık cevaplanamayacak bir RİCA (katalizör) |
| 2 | K10 | 92,0 s | aynı kayıt | RECORDED HUMAN | bant-limitli, en yüksek | aynı işlev, bu kez kaynağının yanında (orta nokta) |

```
REPLİK METNİ: "There are children here. Please give the light back."
İLK REPLİK:   K03 · 26,0 s · öncesindeki kesintisiz sessizlik 26,0 s · vuruş katalizör
BEDENLEŞTİRME: ⛔ YOK — ve bu filmde yapısal olarak İMKÂNSIZ: sesin ağzı bu
              dünyada kalmadı. Chion'un kuralı tersine çalışır, ses büyüsünü
              asla yitirmez [SES §1a.1]
⛔ SANİYE HESAPLATILDI [D122]: (n−1) × 10,0 + TIMELINE ofseti
⛔ İŞLEV testi: repliği sil → şehirde çocuk olduğu ve birinin bunu isteyecek
  kadar beklediği bilgisi gider; ikisi de kadrajda YOK → KALIR
⛔ duygu ADLANDIRILMIYOR · replik <5 s · tek konuşmacı · kadrajda konuşan ağız
  0 klip (ses bir CİHAZDAN gelir, ağız vizörün ardında ve hiç konuşmuyor)
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md
```

---

## 👤 KARAKTER KARTI  (`KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU` §1 · PROMPTA GİRMEZ)

```
ROL           bir filonun eski kaptanı — ekipmanla okunur: servis kızağı, fener,
              geminin anahtar çubuğu                                    K04 · K14
İSTEK         çekirdeği kaideye bağlamak ve küreyi salıvermek (bir İŞ)   K13-K21
BASKI TEPKİSİ KONTROL EDER — engelde ilk yaptığı şey ölçmek/denemek     K13 · K19
              ⛔ film boyunca DEĞİŞMEZ
ALIŞKANLIK    eldivenli SOL avucunu bir yüzeye düz basıp bir an tutmak
              tekrar 1/3 K08 (duvar) · 2/3 K12 (levha) · 3/3 K19 (çekirdek)
              derecelenme: 2. tekrar daha kısa, 3. tekrar daha hızlı
              ⭐ KIRILMA K20: avuç kilide doğru kalkar, bir el genişliği
              önünde DURUR, sonra iki el çubuğa gider — avuç hiç basmaz
SINIR         bu dünyadan bir şey ALMAMAK — K24'te filize dokunmaz, kamera
              dokunur; K20'de anahtarı da bırakır                       K20 · K24
ZAAF          ① sol eldiven sırtındaki hilal yanık izi (kalıcı, insanlı 18 klipte)
              ② kırağı pası (monotonik, K04'ten itibaren)
              ③ K18'de adım kadansı ilk klipten yavaş                  K08 · K18
TEL           baskı altında sol el düz açılıp bir an öyle kalır (yanık iz görünür)
                                                                  K12 · K17 · K21
İLK ↔ SON     K03: iki eldiven konsol rayında KAPALI, bir ışığı taşıyor →
              K23: iki eldiven AÇIK ve BOŞ, taşıyamadığı bir ışığın içinde
```

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna
> yalnız o karenin `IN FRAME:` satırındaki kısmı gider [D214 · ㉖]. Videoya
> Bible girmez — `START FRAME:` tek satır.

### 👤 Character Bible

> arketip **K** (TAKTİK/YÜKSEK-G) · üç zorunlu hafifletme uygulandı:
> `matte` + `scuffed`/`worn` + tekstil eklem. ⛔ M arketipi (dar pencere)
> KULLANILMADI: dar pencere yüzü kapatır.

```
She wears a heavy pressure suit of matte graphite quilted textile with squared
composite shoulder caps rising to a raised collar ring and a matte scuffed
graphite breastplate, the plates edged in worn dark rubber where they meet the
fabric, a visible brushed-steel neck ring and matching steel rings at both
wrists, heavy segmented dark gloves one piece with the sleeves, and a crescent
scorch the width of two fingers across the knuckles on the back of her left
glove; the helmet is a squared hard graphite shell seated deep into the collar
ring, two small square lamps set into the brow, a single flat front pane inside
a thick dark rim, a soft warm 3200K fill from inside the chin of the helmet on
her face, her face fully readable through the clear pane; the back is one
continuous ribbed surface from collar to hip, closed and smooth, the two
shoulder caps wrapping over its upper edge, a long worn dark cloak hanging from
them to her calves; three ribs of tarnished dull-gold thread run across the
upper chest just below the neck ring; the whole suit carries an even matte
dusting of pale frost rime along the cloak hem and the shoulder caps.
```

```
⛔ BLOK KISALTMA SIRASI (banda sığmazsa — katman atılır, cümle kısaltılmaz):
   ① kırağı pası cümlesi → ② altın kaburga ipliği → ③ `quilted` / `scuffed`
   → ④ bilek halkaları (yaka halkası KALIR) → ⑤ SİLÜET ASLA
⛔ `seamless` · `bubble` · `dome` · `sphere` (kask için) · `glow` · `glowing` ·
   `EVA` · `black` (giysi için) 48/48 promptta 0 kez
⭐ AYRIM EKSENİ: mat grafit zırh siyah bazaltta erir; figürü ayıran şey
   KIRAĞI PASIDIR (omuz kapakları + pelerin kenarı). Kontrast cümlesi ÖZNEYE
   yazılır, zemine renk atanmaz.
```

### 🌍 World Bible

> ⭐ DÜNYA ÇAPASI — üç cümle, dış-mekân klibinin HEPSİNDE BİREBİR.

```
SKY:      a black sky thick with stars and one shattered moon low over the
          rooftops, its ring a thin arc, the moon as wide as a plate held at
          arm's length
HORIZON:  a flat line of black basalt towers to a straight horizon, no haze
LANDMARK: the release cradle at the city's edge — three stone arches, its open
          socket facing the sky
```

```
ŞEHİR:   black basalt, thin ribbed towers, giant seated statues along one
         avenue, their knees higher than she is
KAİDE:   three stone arches in the same ribbed language as the towers; a round
         open socket at their centre, machined for a cylinder
GEMİ:    a long ribbed hull, the same three-ring motif as the arches but cut in
         machined metal — a portable copy of a cradle; one lit window the height
         of a door on its spine; three rings under the spine
OYUK:    a rock hollow at the foot of a wall, the stone warm from below, a thin
         upright vapour collar standing off its lip
⛔ ŞEHİR DEĞİŞMEZ: aynı gök, aynı ufuk, aynı yer imi — her dış klipte aynı
  kelimelerle [D209 · 3 filmde her sahnede başka dünya çıktı]
```

### 🎥 Camera Bible

> ⛔ Aynı harfin cümlesi BİREBİR kopyalanır; dönüşte işaret satırı eklenir.
> ⛔ `tripod` kelimesi hiçbir satırda YOK (ADAY-98).

| harf | prompta giren cümle (birebir) | kadraj |
|:--:|---|---|
| A | `24mm spherical lens on a locked-off camera 6.0 m from her, camera height 1.50 m, eye-level wide shot, deep focus` | 9,00 × 5,06 m |
| C | `35mm lens on a locked-off camera 2.2 m away, camera height 1.60 m, high angle fifteen degrees, medium shot, deep focus` | 2,26 × 1,27 m |
| D | `50mm lens on a locked-off camera 1.3 m away, camera height 1.40 m, eye-level frontal close-up, deep focus` | 0,94 × 0,53 m |
| F | `35mm lens on a locked-off camera 1.5 m away, camera height 0.95 m, low angle medium shot, deep focus` | 1,54 × 0,87 m |
| G | `35mm lens on a locked-off camera 4.0 m behind her, camera height 1.30 m, over-the-shoulder wide shot, deep focus` | 4,11 × 2,31 m |
| H | `50mm lens on a locked-off camera 0.8 m away, camera height 1.10 m, profile close-up insert, deep focus` | 0,58 × 0,32 m |
| I | `24mm spherical lens on a locked-off camera 25.0 m away, camera height 12.0 m, eye-level wide shot, deep focus` | 37,50 × 21,09 m |

### 💡 Lighting Bible

> IŞIK TAKVİMİ — sahne başına BİR satır; artış S6'nın son klibinde BAŞLAR ve
> bir OLAYDIR [D193]. Sahne içinde LIGHT satırı BİREBİR aynıdır (㉜⑥).

| sahne | kaynak | kademe | not |
|---|---|:--:|---|
| S1 | kafesteki kürenin altından gelen koyu kızıl-altın; başka kaynak yok | 1 | gölge sert, dolgu yok |
| S2 | göğüs hizasındaki kendi feneri + parçalanmış ay | 1 | pussuz gökte sert kenarlı gölge |
| S3 | salonda yanıp sönen tek ölü lamba + kendi feneri | 1 | lamba iki saniyede bir sönüp yanar |
| S4 | yuvanın içine konmuş feneri, taşta tek koni | 1 | — |
| S5 | geminin kendi iç lambaları + güverte ızgarasından yükselen kızıl-altın | 1 | ışıklar BU sahnede söner (6→3) |
| S6 | buzun üstünde feneri + yuvanın ışığı + kısık kürenin kızıl-altını | 1→2 | ⭐ ARTIŞ K21'de başlar |
| S7 | yeni güneş: tek sert alçak kaynak | 3 | uzun ve sert gölgeler, dolgu YOK |

```
⚠️ YANLIŞ-POZİTİF: ana ışık ELDE TAŞINAN FENERDİR ve kadının hareketiyle
  birlikte döner. Yön SAATLE değil KAYNAKLA kilitlenir ("her own lamp, at her
  own chest height"). ⑪ merceği bunu "KEY WALKS" yazarsa bulgu TASARIMDIR.
⛔ `glow` · `glowing` · `radiant` · `luminescent` · `shimmering` · `ethereal`
  0 kez [D29]; ışık her zaman DÜŞTÜĞÜ YÜZEYLE yazılır.
⛔ 0% bloom · halo yok · lens parlaması yok · aradaki hava pus taşımaz.
```

### ⚙️ Physics Bible

> §5.1b: PHYSICS ve AUDIO gövdede, her promptta AYNI sayılarla.

```
PHYSICS (24/24 promptta, sahne içinde birebir):
  Gravity is 0.38 g in a dense cryogenic atmosphere at 0.90 bar and 95 kelvin.
  Lifted frost settles within half a second, the slow wind never moves cloth,
  and anything she lets go falls and reaches the ground in about a second.
  There is no haze: shadows are hard and fill is weak.

AUDIO (24/24 promptta, ilk cümle sahne içinde birebir):
  The cold dense air carries low frequencies close and strong and kills the
  highs, so everything sounds heavy and near. Her breathing sits under it.
  No dialogue. No music.

KÜRE EKİ — kadrajda küre varsa PHYSICS'e eklenen tek cümle:
  S1-S6:  The sphere is held and compressed at the focus of three machined
          rings and moves with the hull as one body.
  S7:     The sphere is held by the stone cradle high above the city.

DÜŞÜŞ TABLOSU (0,38 g · 3,7 m/s²):
  eldiven yüksekliği (1,0 m) → 0,73 s      gövde boyu (1,7 m) → 0,96 s
  kaide kemeri (6,0 m)       → 1,80 s
⛔ Tek g değeri. `free fall` · `plummets` · `crashes down` 0 kez.
⛔ `swirl` kökü 0 kez; kırağı yoğunluğu SAYILI ("a few dozen dry grains").
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin yasakları

> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (video 8 · image 7
> cümle) + bu listeden klip başına ≤3 cümle taşır (㉗).

```
BU FİLME ÖZEL (sahneye göre ≤3 seçilir):
① No bare skin anywhere — none above the collar, none at the wrists between
   glove and sleeve, none at the ankles between boot and leg.
② The visor is one flat clear pane in a thick dark rim — no dome, no bubble,
   no mirror coating, no tint, no environment reflected in it.
③ No haze, no halo, no light shafts, no lens flare, no corona around the sphere.
④ Nothing changes shape, melts or warps; the only change is the stated one.
⑤ No water, no liquid, no rain, no ice melting, no dripping anywhere.
⑥ No emblem, no badge, no patch, no rank mark, no flag on the suit or the hull.
⑦ No second ship, no other craft, no lights in the sky but the stars and the moon.

⛔ ASLA YAZILMAZ (yasak, yasakladığı kavramı prompta sokar [D123]):
   explosion · fireball · flash · blast · detonate · wounded · dying · dead ·
   corpse · blood · danger · panic · trapped · smoke
⛔ İNSANSIZ KLİPTE (K01 · K02 · K04 · K11 · K21 · K24): `Exactly 0 human` ya da `no people`
   YAZILMAZ; NEGATIVE bloğu kısaltılır ve boşluk POZİTİF tarif edilir
   [red defteri #2'nin GEÇEN çözümü].
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi klip |
|---|---|---|---|
| İNSAN SAYISI | 18 klipte tam 1 · 6 klipte 0 (K01·K02·K04·K11·K21·K24) | 4 · 10 | hepsi |
| KASK TAKVİMİ | 24/24 KAPALI · açık 0 klip · durum değişimi 0 | 3 | hepsi |
| VİZÖR PANESİ | TEK düz ön pane · çerçeve KALIN · spekülar çizgi 1 | 3 | insanlı 20 |
| YERÇEKİMİ | tek değer 0,38 g · düşüş 1,0 m → 0,73 s | 6 · 6b | hepsi |
| KÜRE (taşıma) | çap = halkaların iç açıklığının 4/5 · hücre 4 s'de 1 genişlik · korona 0 kare | 12 | K01·K02·K03·K18·K21 |
| KÜRE (kadrajı terk) | 6. saniyede alt kenar üst çizgiyi geçer · 8. saniyede yok | 12 | K21 |
| GEMİ IŞIK SAYACI | 6 → 3 → 1 → 0 (monotonik) | 5 | K15·K17·K18·K21 |
| KIRAĞI MERDİVENİ | 3 kademe · geri dönmez · global bitiş | 3 · 6 | hepsi |
| EKRAN METNİ | 0,0 saniye (kart/jenerik dâhil) | 5 | hepsi |
| REPLİK | 2 tırnaklı geçiş · 1 cümle · ağız konuşan 0 klip | 7 | K03 · K10 |
| FİLİZ | 1 adet · bir parmak boyu · 3 yaprak · hareket 0 | 2 | K24 |
| AYDINLANMIŞ ALAN | 0 → yuva → duvar+kaldırım → sokak (monotonik artan) | 6b | K19-K24 |
| HEYKEL | dizleri kadından yüksek · sayı yazılmaz, "an avenue of them" | 13 | K05 |
| ANAHTAR ÇUBUĞU | ön kol boyu · 1 adet · K20'den sonra 0 | 5 | K15-K20 |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — ㉕ KİLİT TAVANI)

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D146 | kask mat grafit sert kabuk · ÖN yüzde TEK DÜZ pane · çepeçevre KALIN koyu çerçeve · yaka çemberine derin oturmuş; `seamless/bubble/dome/sphere` 0 kez | insanlı 20 klip + referans paketi RK1 |
| D89 | çıkarma klibinde TEK MÜHÜR SAYIMI: çıkarılan şey adıyla sayılır, geri kalan bütün mühürler tek tek kapalı ilan edilir | K17 · K18 · K19 · K20 |
| D59 | yedi kök (`hang/suspend/float/hover/still/frozen/stopped`) yalnız negatif blokta; küre pozitif gövdede TUTULUR ve SIKIŞTIRILIR | 24/24 klip · üretim öncesi grep |
| D192 | küre pozitif biçimi dört SAYIYLA: çap oranı 4/5 · hücre 4 s · korona 0 kare · aradaki hava pussuz | K01 · K02 · K03 · K21 |
| D127 | kürenin yükselişi İVME ile değil KADRAJI TERK SÜRESİ ile yazılır (6. s alt kenar, 8. s yok, kendi genişliği ~2 s) | K21 |
| D209 | DÜNYA ÇAPASI üç cümle (gök · ufuk · yer imi) dış-mekân klibinin hepsinde birebir | 13 dış klip |
| D193 | IŞIK TAKVİMİ 7 satır; artış S6'nın son klibinde başlar ve bir OLAY olarak ilan edilmiş; klip içinde geri yanma 0 | hepsi · SPEC C |
| D210 | K24'ün CAMERA satırı K01'in CAMERA satırının BİREBİR kopyası + dönüş işareti; iskelet ilk/son harf C | K01 ↔ K24 |
| D206 | altı efor klibinin her birinde saniyeli ödeme satırı + DESTEK/GÖVDE/2 işaret/DURAKSAMA | K13·K16·K17·K18·K19·K20 |
| D207 | YORGUNLUK 0-6, ardışık düşüş ≤1; sahnenin 2.+ klibinde `CONTINUOUS ACTION:` bedeni kelimesi kelimesine taşır | 17 klip |
| D202 | ÇAPA ÜÇLÜSÜ üçü de AYNI kanalda önce/sonra beden çifti; CHOICE karesinde reddedilen nesne kadrajda ve sonra da orada | K16 · K17 · K23 |
| D179 | her IMAGE promptu 0,0 saniyeyi yazar; bedel ve seçim klipleri MS ve daha yakın, fark kısa kenarın ≥1/8'i | K16 · K17 · K19 · K20 |
| D213 | temaslı klipte üç satır AYNI klipte (TEMAS · DEĞİŞİM · SONUÇ ≥1 s), nesne merkez üçte birde, temas ilk 2 saniyede kurulu | K06·K08·K12·K14·K19·K20·K21 |
| D141 | FİNAL VURUŞ KANITI: K24 · 236,0 s · oyukta TEK filiz, 1 adet, sayılabilir ve adı konabilir | K24 |
| D157 | TEK KARE cümlesi taşıyıcıyı ADIYLA taşır; novum klibinde kadrajda ikinci olay YOK | K02 · K21 |
| D78 | ölçek iddiası TEK KAREDE iki ucuyla: küre 922 px ↔ kapı boyundaki pencere 205 px | K02 (ve aynası K18) |
| D139 | kameranın arkayı gördüğü TEK klipte pozitif sırt cümlesi ("one continuous ribbed surface … a long worn cloak hanging from them") | K06 |
| D95 | mühürlü durumun ÜÇ GÖRÜNÜR İŞARETİ: kalın koyu çerçeve · kadrajdaki yaka halkası · panenin üst kenarında tek ince spekülar çizgi | insanlı 20 klip |
| D147 | KIRAĞI MERDİVENİ monotonik ve GLOBAL bitiş; gemi içinde de çözülmez (gövde içi de mühürlü ve soğuk) | hepsi · SPEC C |
| D123 | yasak SİLİNİR, malzeme TARİF edilir; tehlike ve yıkım sözlüğü 0 kez; gemi "goes dark in the stated order" | K17 · K18 · K21 |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle

| ders | neden bu filmde numaralı kilit satırı almadı |
|---|---|
| D1 · D34 · D45 · D138 · D214 · D215 | V3-S iskeleti + §5.1 çekirdek + üretim defterinin üç kutusu bunları YAPISAL olarak taşıyor |
| D169 | D206 ile aynı cümlede uygulanıyor (sözlük D169'un, saniye D206'nın) |
| D175 | çıplak-deri negatifi ÜÇ BÖLGELİ olarak §5.2 cümlesine yazıldı; zorlanma giysi yüzeyinde |
| D58 | tekrar eden varlık kartları `GUNES_MEZARI_REFERANS_PAKETI.md`'de (6 kayıt) |
| D176 · D174 | World Bible tek zemin cümlesi + yön cümlesinin nesneye bağlanması yazım standardı |
| D180 · D216 | ikisi de `GUNES_MEZARI_MUZIK.md`'nin işi (kurguda hard mute + katman tavanı) |
| D200 | ortam kartının PHYSICS satırı tek g'yi zaten taşıyor |
| D211 | HOOK MİMARİSİ bloğunda üç sayıyla duruyor |
| D217 | replik 1 satır; İŞLEV hücresi replik tablosunda |
| D90 · D152 | ölçen kenar ve elde alet kuralları sahne çalışma dosyalarında (K19 · K20 · K22) |
| D91 | hilal izin ÖZELLİK+ÖLÇÜ+KAPATMA üçlüsü Character Bible'a ve K08'in kilidine yazıldı |
| D198 · D201 | ETİKET filme uymuyor: 0 g yok, vakum yok |
| D69 | üç yasaklı geçiş (iniş · loş mekâna giriş) SINIRDA ve kadraj dışında; satır 00_ANALIZ'da |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  K21 (kaide devralır, halkalar açılır, küre yükselir)
NÖTR TARİFİ:         the three rings swing outward to their stops and the
                     sphere lifts clear of them at one steady rate; the ribs
                     of the hull stay whole and still
⛔ `explosion` · `fireball` · `flash` · `blast` · `detonate` NEGATİF BLOKTA
   BİLE yazılmaz [D123 · red defteri PK sınıfı].
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal) |
|---|---|---|
| `wounded/dying/dead` sözlüğü | geminin "ölüyor" olduğu duygu kelimesi | MALZEME SONUCU: ışıklar SAYILI sırayla söner (6→3→1→0), kokpit kararır, buzda tek iz kalır |
| amblem/arma (D138 + red #3) | imparatorluğu ADLANDIRAN işaret | BİÇİM: kaburga + üç halka dilbilgisi; geminin halkaları şehrin üç taş kemerinin kaba kopyasıdır — geri hikâye repliksiz okunur |
| dört insansız klipte kısaltılmış negatif blok | çekirdeğin 7-8 cümlesinin koruması o dörtte azaldı | POZİTİF ENVANTER: boşluk VARLIK olarak tarif edilir ("the flight deck above it is dark and unmanned") |
| "vizör açılır" jesti | yüzün ilk kez görünme ANI | IŞIK: yüz ilk kez K03'te, yalnız aşağıdan gelen kızıl-altınla; çene içi 3200K dolgu |
| göğüsten disk sökme jesti | üniformayı reddetme hareketi | ALET TEPKİSİ: anahtar çubuğu kilide sürülür ve kilit onu YUTAR — imparatorluğun son aleti ve eve dönüş aynı hareketle harcanır |

```
⛔ TELAFİ sütunu boş satır YOK.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
```

---

## 📎 REFERANS PAKETİ

```
KARAR: YAZILIR — `GUNES_MEZARI_REFERANS_PAKETI.md` · KAPI 0
TETİKLEYİCİ: T1 (kask/vizör) · T2 (biçim kilidi) · T3 (oran) · T6 (dönen varlık)
KAYITLAR: RK1 zırh+kask · RA gemi · RB kaide · RO küre (2 durum) + buhar yakası ·
          RP çekirdek + anahtar çubuğu · RD şehir/oyuk
⛔ Sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği klip ÜRETİLMEZ.
```
