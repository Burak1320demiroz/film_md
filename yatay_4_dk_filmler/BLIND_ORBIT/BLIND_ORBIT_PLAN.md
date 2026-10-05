# 🎬 BLIND_ORBIT — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur.
> Analiz: `00_ANALIZ/` (onay · çizelge · hasat · konsept · sıralama · uyarı · sahne tablosu).
> Sahibin planı birebir: `00_ANALIZ/00_ON_PLAN/BLIND_ORBIT_SAHIP_PLANI.md`.
> Bu dosya analizin SONUCUNU taşır; yeniden düşünmez.

```
FORMAT:        yatay 4 dk · 16:9 · ÇOK KLİPLİ SAHNE (§2.3 · §2.0b) · 2 bölüm (12 + 12)
ORTAM:         §3.1 VAKUM (dış) + §3.10 BASINÇLI İÇ HACİM · §3.10b tam mikrogravite —
               tek PHYSICS satırı iç + dış (PROMPT_HATA §3.10b · THE_LAST_GATE emsali)
TÜR:           bilimkurgu (§4.1) · kurtarma/yanaşma gerilimi · kozmik ölçek
KLİP SÜRESİ:   10,0 s plan · ⬜ ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk klip>
SAHNE SAYISI:  6 sahne / 24 klip     RUNTIME: 24 × 10,0 = 240 s = 4:00 (hook 24'ün içinde)
LOGLINE:       Ana motoru ölmüş gemisini ayrılmak üzere olan dönen istasyona yanaştıran pilot,
               kamerası kararınca son metreleri yalnız mühendisin sesine güvenerek kapatmak zorundadır.
HİKÂYE ONAYI:  00_ANALIZ/00_HIKAYE_ONAYI.md · ONAY 05.10.2026 · TUR 1/3 · SAPMA 1 onaylı (4 replik)
REFERANS PAKETİ: YAZILDI (sahip kararı) — BLIND_ORBIT_REFERANS_PAKETI.md · KAPI 0 · 8 sayfa
```

---

## 🎭 TEMA

```
TEMA: GÜVEN
TANIM: Göremediğin son metrede başkasının gözü senin gözün olur.
      (aday etiket · TEMA §3b · sahibin seçimi; depoda ikinci kullanım — THE_FALLING_WORLD)

MOTİF SAHNELERİ: S2 (K04 sıkı kabza · K08 bekleyip bırakan el) · S3 (K12 onun okuduğuna
      göre seçim) · S4 (K18 el gevşer — CHOICE) · S5 (K19 yalnız ses) · S6 (K23 açık el · K24)
      3. derece indeksler: EL (kumanda kabzası sıkı → gevşek → açık) · KAMERA (Lena'nın başı
      ekrandan pencereye/sese) · NESNE (kararmış yanaşma ekranı ↔ küçük yuvarlak pencere) ·
      SES (makine sayar, insan yönetir)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          İLİŞKİ (üçüncü tercih — fizik kuralı eklenmez; filmin fiziği gerçekçi)
NOVUM:               Son metrelerde gemiyi süren el onu göremiyor; gören göz gemiyi süremiyor —
                     kenetlenme ancak ikisi tek hareket olunca olur.
NOVUM TAŞIYICISI:    kenet halkası, küçük yuvarlak pencerenin retikülünde × Noah'nın vizörünü
                     pencereye yaklaştırıp iki parmağıyla iskeleyi göstermesi ↔ Lena'nın kararmış
                     yanaşma ekranından başını çevirip sağ eldivenini kabzada gevşetmesi
                     → halka ile kenet arasındaki boşluk kapanır (K17-K20)
TEK KARE (§4①):      K16 · 0,0 s — kokpitte kararmış yanaşma ekranı (yanık konsolun ortasında
                     tek siyah dikdörtgen) ve pencereyi dolduran istasyon yüzü; ikinci kare K17 ·
                     8,0 s — küçük pencerenin retikülünde kenet halkası, Noah'nın vizörü cama eğik.
KİNETİK BAĞIMSIZLIK: ✅ şartlı — kara ekran + çekilen el (K16) · pencereye bağlanan Noah (K17) ·
                     iskeleyi gösteren iki parmak / gevşeyen el (K18-K19) · kapanan boşluk (K19-K20);
                     replik hızlandırır, taşımaz. Şart: K18 eldiven ≥ ⅛ kısa kenar (170 px ✅)
BAŞLIK ŞEMASI:       "Docking Blind" — izleyiciye karanlık ekrana ve kapanan boşluğa bak der
KURAL TEKRARI:       kurulum K08 (vana önerisine bırakılan kontrol) · doğrulama K12 (onun
                     okuduğuna göre seçim) · sonuç K18-K20 · ≥3 sahne · ≥2 nesne (vana çarkı ·
                     kenet halkası/retikül) · hepsi KESİLEMEZ listesinde ya da S2-S3 omurgası
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   küçük gemiyi ayrılmadan önce dönen istasyona kenetlemek ve onunla eve dönmek
   □ ENGEL:   ana motor yok · sol itici hattı açık kalmış gemiyi eksenden kaçırıyor · istasyon
              dönüyor ve 3:40'ta yanışa geçiyor · son metrede yanaşma kamerası kararıyor
   □ BEDEL:   S2 · K07 geri çekilme payı tükenir (ikinci yaklaşma yok) · S3 · K10 bir itici
              grubu vanayla sonsuza kapatılır · S4 · K18 pilot kendi gözüyle sürmeyi bırakır
   □ MUHATAP: ikinci insan — mühendis, çoğunlukla kadraj dışında, telsiz sesi
B5 □ AYRILIK: S2 · K08 — Noah hattı kapatmayı önerir, Lena 1,2 s cevap vermez, eli kabzada
              kilitli kalır (ERTELEME) · S4 · K18 — Lena'nın başparmağı kendi düzeltmesine
              gider, Noah komutu daha alçak tekrarlar, el gevşer (RET → UYMA, tersinmiş)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  0 referans paketi (RK1 · RK2 · RA · RB · RI1 · RI2 · RO · RD) → 1 K15 (1 numaralı risk ·
  İPTAL KAPISI) → 2 K20 → K21 (DORUK) → 3 K18 (merkezî seçim) → 4 K24 → K23 (kapanış imajı +
  FİNAL çapası) → 5 K01 → K02 (hook) → 6 K19 · K16 · K17 · K22 · K14 · K13 → 7 S2 (K03-K08) →
  8 S3 (K09-K12)
⛔ İPTAL KAPISI: K15 iki üretimde "halka ve üç kanat durur · kara delik çeyrek tur döner"
   ölçüsünü tutmazsa üçüncü yeniden yazım yok — kamera A'ya taşınır (imza "birlikte dönen
   ikili" olur). K20 + K21 iki üretimde temas/dört kilit göstermezse film ÜRETİLMEZ.
```

### İSTEK ÇAPRAZI · KARAR MİMARİSİ (`IKI_KISI` §3 · `KARAKTER_KARTI` §3)

```
Lena, Noah'dan:  hattı kapatıp kalan iticilerle tek temiz yaklaşma vermesini (K08)
Noah, Lena'dan:  son metrede kendi gözüne değil onun sesine göre sürmesini (K18)
NESNE:           Lena'nın T-kabzalı kumanda kolu
İKİ SEÇENEK:     K18 — ① kendi gözü (pencere + kararmış ekran) · ② ses (telsiz)
REDDEDİLEN:      kararmış yanaşma ekranı — K18'de kadrajda, K19-K23'te de siyah
BAŞARISIZ DENEME: K06 (büyük düzeltme, gemi yine sola çekilir) · K07 (çarpışma önlenir, pay biter)
BEDEL PENCERESİ: K07 anlık · K10 stratejik · ironi penceresi K11 (izleyici ekranın bozulduğunu
                 Lena'dan önce görür) → kapanış K16
```

---

## 👤 KARAKTER KARTI (Character Bible'ın ÜSTÜNDE · `KARAKTER_KARTI_VE_DAVRANIS` §1)

> Kart PROMPTA GİRMEZ; TIMELINE'daki gövde fiillerinin sırasını ve temposunu besler.

```
👤 KART A — "pilot"                                                   sahne
ROL           pilot koltuğu (SOL), sağ eldiven T-kabzada · altın bant SAĞ   K04
İSTEK         gemiyi istasyona bağlamak                                     K03-K04
BASKI TEPKİSİ ACELE EDER — el bakıştan ÖNCE gider, düzeltme büyük           K06
ALIŞKANLIK    düzeltmeden önce sağ eldiven kabzayı iki kez kısa sıkar        K04 · K06 · K14 → kırılma K18
SINIR         göremediği şeye gemi sürmez                                   K16 (el çekilir) → K18 aşar
ZAAF          kendi gözüne güvenip payı tüketir — önkol kilitli, omuz düşük K07-K08
TEL           nefesini tutar: omuz hattı kalkar ve bir süre inmez           K07 · K16 · K18
İLK ↔ SON     K04 kabzayı SIKI kavrayan sağ eldiven ↔ K23 dizinde AÇIK eldiven K04 ↔ K23

👤 KART B — "mühendis"                                                sahne
ROL           sağ koltuk, sol bilekte analog gösterge · kobalt bant SOL     K04
İSTEK         hattı kapatmak; sonra pilotu halkaya kendi gözüyle taşımak    K08 · K17-K19
BASKI TEPKİSİ KONTROL EDER — bakış önce, el ~1 s sonra                      K09 · K10
ALIŞKANLIK    bağlanınca bağ kayışını iki kez çeker                         K04 · K09 → kırılma K17 (tek çekiş)
SINIR         görmediği şeyi söylemez                                       K12 · K17
ZAAF          çark direnir — iki yüklenme, omuz ve sırt öder               K10
TEL           vizörünü bakılan yüzeye yaklaştırır, baş öne                 K10 · K17 · K19
İLK ↔ SON     K04 göstergeye bakar ↔ K22 pencerede bağlı halkaya bakar, omuz iner   K04 ↔ K22
AYRIŞMA       İSTEK · BASKI TEPKİSİ · ALIŞKANLIK · TEMPO dördü farklı ✅
```

---

## 🥁 VURUŞ TABLOSU (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | klip | boşsa gerekçe |
|---|---|---|---|---|
| 1 | açılış imajı (ileri sıçrama) | 0-4 | K01 | — |
| 2 | ikinci bilgi | 4-8 | K02 | — |
| 3 | kurulum + katalizör | 8-17 | K03 · K04 | katalizör 0:31-0:35 (%13-15 bandı) |
| 4 | tartışma / başarısız deneme | 17-29 | K05 · K06 · K07 | — |
| 5 | ilk bedel + ayrılık | 29-33 | K07 · K08 | — |
| 6 | onarımın bedeli | 33-50 | K09 · K10 · K11 | — |
| 7 | orta nokta (sahte zafer) | 46-63 | K12-K15 | — |
| 8 | her şeyin kaybı (görüntü kanalı) | 63-67 | K16 | — |
| 9 | merkezî seçim | 71-75 | K18 | — |
| 10 | doruk | 75-88 | K19 · K20 · K21 | — |
| 11 | çözülme | 88-96 | K22 · K23 | — |
| 12 | kapanış imajı | 96-100 | K24 | — |

## 🪝 HOOK MİMARİSİ (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:        IN MEDIAS RES — ileri sıçrama (yatay 3-5 dk bandı)
S0 SORUSU:        "Kara deliğin önünde dönen dev yapıya bu minik gemi kenetlenebilecek mi?"
S1 İKİNCİ BİLGİ:  K02 — bir insan küçük bir pencereden halkaya bakıyor; "…dock without a camera."
İLK 2 SN SESİ:    telsiz taşıyıcı hışırtısı + kaskın içinde tek nefes · müzik 0:03'ten önce yok
BİLGİ ASİMETRİSİ: DRAMATİK İRONİ · taşıyıcı ① ARKA PLAN OKUR · asimetri anı 1:44 (K11 4,0 s) ·
                  kapanış K16
AÇILIŞ↔KAPANIŞ:   KAFİYE K01 ↔ K24 (kurulum A, CAMERA birebir) — değişen tek değişken: iki
                  gövdenin DOKUNMASI ↔ TEK GÖVDE olarak birlikte taşınması
AÇILIŞ BİLGİ SIRASI: nerede (kara delik + dev yapı) → kim/ne yapıyor (minik gemi aynı dönüşte
                  yaklaşıyor) → ne yanlış (kayıt sesi: motor yok, istasyon gidiyor) → tepki
                  (K02 — birinin pencereden bakması)
```

---

## 🗺️ SAHNE HARİTASI

> Hesap: `00_ANALIZ/03_SAHNE_SIRALAMASI.md` · satır ayrıntısı: `00_SAHNE_TABLOSU.md`.
> Palet ve ses dokusu sahne içinde birebir, sahneler arasında farklı (`KURGU_RITMI` §2).

| K · S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | şerit · tempo |
|---|---|---|---|---|---|
| K01 · S1 1/2 | İKİ HALKA | iki gövde aynı dönüşte, burun ön yüze değer | A · 35mm · EWS · göz hizası profil | hışırtı · nefes · R1 | G · Y |
| K02 · S1 2/2 | PENCERE | Noah'nın vizörü pencerede, iki parmak iskeleye | B · 35mm · MS · OTS | R2 · nefes | S · Y |
| K03 · S2 1/6 | AÇIK HAT | gemi yana kayar, sol itici kümesinden düz jet | A dönüş K01 | warble (içeriden) | G · N |
| K04 · S2 2/6 | ÜÇ DAKİKA | iki koltuk arkadan; kabza iki kez sıkılır; gösterge | C · 35mm · WS · üst açı arkadan | uğultu · R3 · R4 | G · N |
| K05 · S2 3/6 | CEVAPSIZ | istasyon tek başına, kanatlar çeyrek tur; cevap yok | D · 35mm · EWS · alt açı 3/4 | istek tonu | D · Y |
| K06 · S2 4/6 | SOLA ÇEKİYOR | büyük düzeltme; pencerede istasyon yine kayar | C dönüş K04 | itici darbeleri · R5 | D · H |
| K07 · S2 5/6 | BİR GÖVDE BOYU | gemi kanadın önüne kayar, bir gövde boyu kala durur | A dönüş K03 | iki tutulmuş nefes | B · H |
| K08 · S2 6/6 | BEKLEYEN EL | omuzlar düşük; öneri; 1,2 s; "Do it." | C dönüş K06 | R6 · R7 | T · Y |
| K09 · S3 1/4 | GEÇİT | Noah raylardan çekilerek ilerler, vanaya bağlanır | E · 24mm · MS · alt açı sırttan | tutamak tıkırtısı | G · N |
| K10 · S3 2/4 | VANA | sert çark takılır, ikinci yüklenmede dayanağa varır | F · 50mm · CU · OTS sol omuz | tıslama → yok | B · H |
| K11 · S3 3/4 | BOŞ KOLTUK | tek başına söndürür; ekran bir kez kararır (ironi) | C dönüş K08 | tek darbeler | R · N |
| K12 · S3 4/4 | TEK YAKLAŞMA | gösterge okunur; plan değişir | F dönüş K10 | R8 · R9 | K · N |
| K13 · S4 1/6 | EKSEN | eksende, burun ön yüze, dönmeye başlar | A yeniden tanıtım | yatak | R · Y |
| K14 · S4 2/6 | YAVAŞLAYAN KANATLAR | kabza iki kez; küçük dönüş darbeleri; kanatlar yavaşlar | C dönüş K11 | itici darbeleri | G · N |
| K15 · S4 3/6 | DURAN HALKA | gövde kamerası: yüz durur, kara delik çeyrek tur döner | G · 35mm · EWS · göz hizası eksen | nefes yavaşlar | S · Y |
| K16 · S4 4/6 | KARA EKRAN | ekran zaten kara; el kabzadan çekilir | C dönüş K14 | R10 | T · H |
| K17 · S4 5/6 | GÖRÜYORUM | Noah destek koltuğuna, tek çekiş, vizör pencereye | B yeniden tanıtım | kayış · R11 | G · H |
| K18 · S4 6/6 | SESİMİ TAKİP ET | başparmak durur, el gevşer, küçük iskele düzeltmesi | H · 35mm · CU (MCU) · göz hizası 3/4 | R12 · R13 | K · Y ⭐ |
| K19 · S5 1/4 | SON BOŞLUK | retikülde halka merkeze, boşluk kapanır | B dönüş K17 | R14 · R15 | R · N |
| K20 · S5 2/4 | YUMUŞAK TEMAS | halkalar 3,0 s'de dokunur, halka esner ve tutar | I · 35mm · WS · göz hizası frontal | nefesler bırakılır | R · Y |
| K21 · S5 3/4 | DÖRT KİLİT | dört kanca sırayla oturur | J · 50mm · CU · üst açı | dört tok vuruş (içeriden) | R · H |
| K22 · S5 4/4 | IŞIK SABİTLENİR | bölme ışığı oturur, omuzlar iner, titreşim başlar | B dönüş K19 | R16 · titreşim | S · N |
| K23 · S6 1/2 | AÇILAN EL | yanış sürüyor, eldiven dizine açık | H yeniden tanıtım | derin titreşim | R · N |
| K24 · S6 2/2 | WE'RE HOLDING | K01 kadrajı: birlikte taşınıyorlar | A kafiye K01 | R17 fısıltı | S · Y |

```
AÇI TİPİ SAYISI: 5 ≥3 — göz hizası (A G H I) · profil (A) · OTS (B F) · üst açı (C J) · alt açı (D E)
KURULUM SAYISI:  10 (A-J) — 24 klipte üst bant 12 ✅
KURULUM İSKELETİ: A B A C D C A C E F C F A C G C B H B I J B H A
                 DÖNÜŞ 10/24 = %41,7 ✅ (K03 K06 K07 K08 K11 K12 K14 K16 K19 K22) · KÜME yok (rejim)
SAHNE PLANI: 2 6 4 6 4 2
BÖLÜM KESİĞİ:    K12 (F · CU · iç) ile K13 (A · EWS · dış) arasında — 3 kademe + mekân ✅
ŞOK:             1/2 — K20 (WS) → K21 (CU), aynı mekân, doruğun ikinci vuruşu
```

### 🧬 DAVRANIŞ ŞERİDİ · TEMPO · BEDEL EĞRİSİ · MESAFE

```
DAVRANIŞ ŞERİDİ: G S G G D D B T G B R K R G S T G K R R R S R S   (G 6/24 · K'dan önce D/T ·
                 K'dan sonra R · S var · ilk ≠ son)
TEMPO (Y/N/H):   Y Y N N Y H H Y N H N N Y N Y H H Y N Y H N N Y   (ardışık üç aynı yok ·
                 CHOICE Y, çevresi H/N)
BEDEL EĞRİSİ:    Lena K04 2 · K06 3 · K08 4 (omuzlar düşük, sağ önkol kabzada kilitli @ 0,0 s) ·
                 K11 3 · K14 3 · K16 4 (el kabzadan çekilir @ 5,0 s) · K18 4 (nefes tutulu @ 3,0 s)
                 · K23 3 (eldiven dizine iner @ 6,0 s)
                 Noah K04 1 · K09 2 (önkol rayda, gövde çekilir @ 3,0 s) · K10 4 (omuz ve sırt
                 çarka yüklenir, çark takılır @ 3,0 s) · K12 4 · K17 3 · K19 3 · K22 3 (omuzlar
                 bir avuç iner @ 6,0 s)
MESAFE EĞRİSİ:   K04 0,8 m · K08 0,8 m · K09 0,8 → 6 m · K10 6 m · K17-K24 8 m (iki bölme,
                 yalnız telsiz) — ilişki yakınlaşırken mesafe açılır
KİM SOLDA:       kokpit arkadan (C): Lena SOL koltuk · Noah SAĞ koltuk — film boyu
```

### ⚓ ÇAPA ÜÇLÜSÜ (`OYUNCULUK_YAZIM` §2 — QA_SPEC'e iner)

```
COST    K08 · 0,0 s   BEFORE (K06 · 8,0 s): shoulders raised, both gloves hard on the grip,
                      leaning into the correction
                      AFTER  (K08 · 0,0 s): shoulders dropped a palm's width, right forearm still
                      locked on the grip, the chest rising and falling fast
CHOICE  K18 · 3-8 s   BEFORE: head turned to the dark display, right glove tight on the grip,
                      shoulders raised
                      AFTER:  head turned to the window, right glove loose on the grip, the thumb
                      away from its cap, shoulders a palm lower
                      REDDEDİLEN NESNE: kara yanaşma ekranı — kadrajda kalır
FINAL   K23 · 6,0 s   BEFORE: right glove loose on the grip
                      AFTER:  right glove lifted off the grip and laid open on her thigh
```

### 💔 AYRILIK KARTI (`IKI_KISI` §8)

```
SAHNE            S2 · K08 · film saniyesi 71,0-75,5
NESNE            T-kabzalı kumanda kolu
A'NIN HAMLESİ    "I can isolate the damaged bank." — Noah başını Lena'ya çevirir (0,0 s), söz 1,0 s
B'NİN CEVABI     kanal: sessizlik → söz · içerik: ERTELEME → UYMA
GECİKME          1,2 s (Lena'nın eli kabzada kilitli kalır)
MESAFE / YÖN     0,8 m · 90° (yan yana) → aynı
KİM SOLDA        Lena SOL / Noah SAĞ
BEDEL            Lena öder (bir manevra grubu) · S3 · K10'da ödenir
İKİNCİ AYRILIK   S4 · K18 · tersinmiş (bekleten Lena → bırakan Lena)
ÇÖZÜM TİPİ       KARŞILIKLI DEĞİŞİM — Lena kontrolü, Noah gövdesini (vanaya, pencereye) verir
```

### 🗺️ SPATIAL MAP — kuşbakışı (SADECE PLANDA DURUR, PROMPTA GİRMEZ)

```
                         ☀ YOK — tek ışık: kara deliğin kehribar halkası, SOL ÜST arka plan
   ┌────────────────────────────────────────────────────────────┐
   │   ⚫ KARA DELİK (arka plan, sol üst, istasyonun ARKASINDA)   │
   │                                                             │
   │  ███ VESPER ═══════[◎ kenet, ekrana SAĞA bakar (3)]          │
   │  (uzun gövde SOLA uzanır, motorlar sol kenar dışında)        │
   │                           ··· eksen ···   ◁═ LARK (burun 9)  │
   │                                      (sağdan sola süzülür,   │
   │                                       fren lüleleri SOLA)    │
   └────────────────────────────────────────────────────────────┘
        ▲ KAMERA A — eksenin YAKIN tarafı, 250 m · film boyu (180° çizgisi aşılmaz)
AKSİYON EKSENİ : LARK → VESPER kenet halkası (ekran sağ → sol)
EKRAN SONUCU   : istasyon HEP SOL · gemi HEP SAĞ · yaklaşma HEP sağdan sola
YÖN TAŞIYICILARI: kara delik sol üst (ışık + mıknatıs hedefle aynı yönde) · sol itici kümesi
                  (hasar) A kadrajında kameraya BAKAN yan değil → yırtık kenar silüette okunur
GÖVDE KAMERASI G: LARK burnundan eksen boyunca istasyonun ön yüzüne (azimut 90°)
HALKA AĞZI I   : istasyon ön yüzünden eksen boyunca gemiye (azimut 270°)
İÇ: kokpit penceresi = geminin burnu = istasyon yönü · servis geçidi kokpitin altından burnun alt
    bölmesine iner · vana yolun ortasında · optik pencere burnun alt bölmesinde, kenetin yanında,
    eksen boyunca istasyona bakar
"İSKELE / port" = geminin SOL yanı = hasarlı itici kümesinin tarafı
```

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a · SAPMA 1 sonrası)

> Saniye formülü: **replik(K_n) = (n−1) × 10 + ofset** [D122]. Ayrıntı ve DEĞİŞ-TOKUŞ tablosu:
> `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §5-§5.1.

| # | K | saniye | konuşan | REGISTER | kanal | metin | İŞLEV (B5 satırı / görünmeyen) |
|---|---|---|---|---|---|---|---|
| R1 | K01 | 1,0 | Lena | HUMAN · kayıt | uçuş kaydı, band-pass | "Main engine's gone. The station's leaving." | ENGEL — iki görünmeyen bilgi |
| R2 | K02 | 12,0 | Lena | HUMAN · kayıt | uçuş kaydı, band-pass | "We have to match its spin— and dock without a camera." | ENGEL — kamerasızlık |
| R3 | K04 | 31,5 | Noah | HUMAN | kask telsizi | "Main drive's gone." | ENGEL — kokpitten görünmeyen |
| R4 | K04 | 35,0 | gemi | MACHINE | kabin hoparlörü | "Station burn in three minutes." | zaman baskısı (sayı makinede) |
| R5 | K06 | 56,0 | Lena | HUMAN | kask telsizi | "It keeps pulling left." | ENGEL — direnç |
| R6 | K08 | 71,0 | Noah | HUMAN | kask telsizi | "I can isolate the damaged bank." | HAMLE — bedelli öneri |
| R7 | K08 | 74,5 | Lena | HUMAN | kask telsizi | "Do it." | KARAR — 1,2 s ertelemeden sonra |
| R8 | K12 | 112,0 | Noah | HUMAN | kask telsizi | "Enough for one approach." | BEDEL — kalan rezerv |
| R9 | K12 | 116,0 | Lena | HUMAN | kask telsizi | "Match the spin." | KARAR |
| R10 | K16 | 154,0 | Lena | HUMAN | kask telsizi | "I can't see the collar." | ENGEL — halkanın kaybı |
| R11 | K17 | 167,0 | Noah | HUMAN | kask telsizi | "I can see the collar." | MUHATAP — R10'un cevabı |
| R12 | K18 | 171,0 | Noah | HUMAN | kask telsizi (alçak) | "Stay with my voice." | HAMLE — güven talebi |
| R13 | K18 | 175,0 | Noah | HUMAN | kask telsizi (daha alçak) | "Slightly port." | HAMLE tekrarı |
| R14 | K19 | 181,0 | Lena | HUMAN | kask telsizi | "With you." | UYMA |
| R15 | K19 | 185,0 | Noah | HUMAN | kask telsizi | "Hold that line. Reduce closure." | yönetim |
| R16 | K22 | 210,5 | gemi | MACHINE | kabin hoparlörü | "Station burn in ten seconds." | zaman baskısı |
| R17 | K24 | 233,0 | Noah | HUMAN · fısıltı | kask telsizi | "We're holding." | FİNAL |

```
İLK REPLİK:     K01 · 1,0 s (kayıt) · ilk canlı ses K04 · 31,5 s · öncesindeki canlı-sessizlik 31,5 s
                · vuruş: katalizör
BEDENLEŞTİRME:  ☑ yok — ses sonuna kadar bedensiz (konuşan ağız 0 klip) [§1a.1]
REPLİK SAYISI:  17 (insan 13 · kayıt 2 · makine 2) — DIYALOG §8 önerisi ≤16'dan 1 fazla:
                R12/R13 bilerek ikiye bölündü (K18 güven anı) [D74]
⛔ sayı söyleyen replik yalnız MAKİNE (R4 · R16) [D82] · tek konuşmacı her an [D35] · duygu adı 0
KAPI: PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md (Kart P 2b) → 00_ANALIZ/07_DIYALOG_KRITIGI.md
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız o karenin
> `IN FRAME:` satırındaki kısmı gider [D214 · ㉖]. Videoya Bible girmez — `START FRAME:` tek satır.

### 👤 Character Bible
> kimlik: `ASTRONOT_DONANIM` §9 · görünüş: `UZAY_GIYSISI_SINEMATIK_TASARIM` §11 — arketip **T
> (teknokratik form-fit)** iki karakterde de; ayrım rol şeridi (taraf + renk) · rozet biçimi ·
> göğüs malzemesi · KONUM. Kimlik öznitelikleri ≤3 [D167]; yüz R1/R2 panelinde.

```
PILOT — full body / torso (birebir):
a woman pilot in a close-fitting pearl-white pressure suit of matte technical textile, a matte
scuffed pearl-white composite chest plate and matching shoulder plates edged in worn dark-grey
rubber where they meet the textile, a thin dark-gold neck ring and matching dark-gold wrist
rings, heavy segmented off-white gloves one piece with the sleeves, one wide band of dark-gold
textile wrapped around her RIGHT forearm and her RIGHT thigh, and on the left of her chest a
small textless raised badge shaped like a pair of swept wings

PILOT — face (yalnız IN FRAME: face):
a woman in her mid-thirties with dark hair pulled back and steady dark eyes; the helmet is a low
hard pearl-white shell with a single flat front pane set inside a thick dark-grey rim, a soft
cool 5600K fill from inside the rim on her face, her face fully readable through the clear pane

ENGINEER — full body / torso (birebir):
a man flight engineer in a close-fitting white pressure suit of ribbed technical textile with
cobalt-blue textile joint panels at the elbows and knees, a brushed-steel neck ring and steel
wrist rings, heavy segmented off-white gloves one piece with the sleeves, one wide band of
cobalt-blue textile wrapped around his LEFT upper arm and his LEFT thigh, a small textless raised
cobalt hexagon badge on the right of his chest, and on his left wrist a round analogue gauge with
a single needle on a plain dial

ENGINEER — helmet (sırttan / OTS; yüz kameradan uzak):
the helmet is a low hard white shell with a single flat front pane set inside a thick dark-grey
rim, the pane facing away from the camera

BACK (IN FRAME: back — ikisinde de birebir, ⑮ SIRT_POZITIF):
the back of the suit is one continuous sculpted surface from collar to hip, low-profile, with
two shallow recessed panels, closed and smooth

PROMPT HÂLİ — yukarıdaki tam blok REFERANS PAKETİ (RK1/RK2) içindir; bölüm promptuna kadraja
göre kısaltılmış şu hâller BİREBİR girer [D214 · ⑲ ≤3 kimlik özniteliği + şerit]:
pilot · arkadan/torso: a woman pilot in a close-fitting pearl-white suit of matte textile, a
  scuffed composite shoulder plate, a dark-gold neck ring, a dark-gold band on her right forearm
  and a low hard pearl-white helmet
pilot · yüz (K18 · K23): a woman in her mid-thirties with dark hair pulled back and steady dark
  eyes, in a close-fitting pearl-white pressure suit of matte technical textile with a scuffed
  pearl-white composite chest plate, a thin dark-gold neck ring and a wide dark-gold band around
  her right forearm; her helmet is a low hard pearl-white shell with one flat clear front pane
  in a thick dark-grey rim, a soft cool 5600K fill from inside the rim on her face, her face
  fully readable through the clear pane
mühendis · torso: a man flight engineer in a close-fitting white suit of ribbed textile, cobalt-
  blue elbow panels, a steel neck ring, a cobalt-blue band on his left upper arm and a low hard
  white helmet
mühendis · tam boy (K09): a man flight engineer in a close-fitting white pressure suit of ribbed
  technical textile with cobalt-blue elbow and knee panels, a wide cobalt-blue band around his
  left upper arm and left thigh, heavy segmented off-white gloves and a low hard white helmet
mühendis · omuz (K10 · K12): a close-fitting white pressure suit of ribbed technical textile, a
  cobalt-blue elbow panel, a wide cobalt-blue band around the upper arm and the edge of a low
  hard white helmet.
mühendis · kask (B kurulumu): His helmet's flat front pane in its thick dark-grey rim faces the
  window, away from the camera.
sırt · image (tek kişi): The back of the suit is one continuous sculpted surface from collar to
  hip, low-profile, with two shallow recessed panels, closed and smooth.
sırt · image (iki kişi): The back of each suit is one continuous sculpted surface from collar to
  hip, closed and smooth.

HELMET STATE:  kapalı K01-K24 · açık 0 · eldiven 24/24 takılı · kimse bedeninden bir şey çıkarmaz
HUMAN COUNT:   kadrajda en çok 2 (K04 · K06 · K08) · 9 insansız klip · kalan 12 klipte 1 — şerit -1-2-2-21111-1-1111--11- (promptlardan ölçüldü)
```

### 🌍 World Bible — DÜNYA ÇAPASI [D209] (dış kliplerde BİREBİR — prompttaki hâli)

```
GÖK:     Behind everything hangs a black hole: a black disc wrapped in a thin sharp band of hot
  amber light, with a fainter bent arc above and below it.
UFUK:    No horizon and no ground — only black space and a few faint stars.
YER İMİ: a huge dark station, a long dark metal cylinder with three dark flat radiator fins at
  equal angles and one round docking collar at the centre of its front face (gövde cümlesinin
  içinde — kuruluma göre konumla)
KONUM (ayrı cümle): A/D "It fills the upper left, behind the station." · G "Its amber band fills the
         frame behind the station's face." · I/J "The amber band of a black hole shows at the upper left edge."
```

### 🚀 Vehicle / Station Bible — ANATOMİ KARTI (`UZAY_USSU` §2.2 · metre YALNIZ burada)

```
LARK (RA)   26 m · Ø ~6 m · 14 gövde boyu (1H = 1,90 m)
  prompt:   a small off-white service ship, short and blunt, a wide window at its nose, a round
            docking collar below the nose facing forward, a cluster of small nozzles on each
            side, one large dark engine bell at the stern
  HASAR (RA-hasarlı hâl, K03 → K24 sabit): on its left side, by the nozzle cluster, the hull is
            opened along one seam, the edges cold and torn
  sayılar:  pencere 1 · kenet halkası 1 · yan lüle kümesi 2 (sol + sağ) · ana motor çanı 1
VESPER (RB) ~900 m · gövde Ø ~40 m · 3 radyatör kanadı (120°, ~80 m) · radyal açıklık ~200 m
  prompt:   a huge dark station: a long dark metal cylinder, three dark flat radiator fins at equal
            angles, one round docking collar at the centre of its front face, a ring of main
            engine bells at its far end
  sayılar:  kanat 3 · kenet 1 (eksende) · motor çanı halkası 1 · pencere 0 · logo/amblem 0
  dönüş:    1,5 RPM = 40 s/tur = 9°/s = çeyrek tur / 10 s (PHYSICS satırında "one full turn every
            forty seconds")
KENET (RO)  yumuşak dış halka Ø ~2,5 m + dört kanca, eşit aralık, istasyonun kanatlarından AYRI
  prompt:   the station's collar: a round soft outer ring in pale grey, and around it four large
            hook-shaped latches, evenly spaced
KOKPİT (RI1) a narrow cockpit with two seats side by side facing a wide forward window; between
            the seats a low console with a dark rectangular display at its centre and a single
            thin amber line on a small panel beside it; a T-shaped hand grip on the inner armrest
            of each seat · yön (§3.10 kural 3): tavan beyaz · duvar açık gri · zemin koyu grafit
SERVİS/OPTİK (RI2) a low narrow passage of pale grey panels with a rail along each wall and a cold
            white strip light along the ceiling; halfway along, a heavy steel hand-wheel the width
            of a helmet set in the wall at chest height with a short webbing loop beside it; at
            the far end a small round window the width of a helmet with two fine cross-hair lines
            etched on it, and a padded support seat facing it with a lap strap
KARA DELİK (RD) kurmaca süper kütleli · siyah disk + ince kehribar disk bandı + üst/alt merceklenmiş
            yay · araçlar disk düzleminin çok dışında
```

### 🎥 Camera Bible — kurulum kartı (BİREBİR kopyalanır · "tripod" yok)

```
A  CAMERA: 35mm spherical lens on a locked-off camera 250 m from the docking axis, level with
  it, eye-level extreme wide shot, side-on profile, deep focus.
B  CAMERA: 35mm lens on a locked-off camera 1.0 m behind his right shoulder, camera height 1.0 m
  above the bay floor, over-the-shoulder medium shot onto the round window.
C  CAMERA: 35mm lens on a locked-off camera 1.8 m behind the two seats, camera height 1.6 m,
  high angle wide shot toward the forward window.
D  CAMERA: 35mm spherical lens on a locked-off camera 600 m from the station's front end, below
  its axis, low angle extreme wide shot, three-quarter view.
E  CAMERA: 24mm lens on a locked-off camera 3.0 m behind him at the end of the passage, camera
  height 0.4 m above the floor, low angle medium shot along the passage.
F  CAMERA: 50mm lens on a locked-off camera 0.9 m behind his left shoulder, camera height 1.2 m
  above the bay floor, over-the-shoulder close-up onto his gloves.
G  CAMERA: 35mm spherical lens on the small ship's forward hull camera 120 m from the station's
  docking collar, eye-level extreme wide shot straight along the axis.
H  CAMERA: 35mm lens on a locked-off camera 1.3 m in front of her and off to screen right,
  camera height 1.3 m above the cockpit floor, eye-level medium close-up, three-quarter front.
I  CAMERA: 35mm spherical lens on a locked-off camera on the station's front face beside the
  docking collar, aimed out along the axis, eye-level wide shot, frontal.
J  CAMERA: 50mm spherical lens on a locked-off camera 8 m from the joined collars and above
  them, high angle close-up on the whole ring and its four latches.
VIDEO EKİ:  "Fixed lockoff, absolutely zero camera movement, in a single continuous shot."
            G için: "Locked to the small ship's hull, zero movement relative to the ship, in a single continuous shot."
DÖNÜŞ EKİ: "— the same position, height and lens as Clip N." (son noktanın yerine)
```

### 💡 Lighting Bible — sahne başına LIGHT satırı (sahne içinde BİREBİR · ㉜⑥ · D193)

```
S1  LIGHT: The only strong light is the thin amber band around the black hole, from the upper
  left; shadows are black and hard-edged, and nothing blooms.
S2  LIGHT: Hard amber light from the black hole's band, upper left, black hard-edged shadows;
  inside, cold blue-grey panel light and one small pulsing amber lamp.
S3  LIGHT: Inside, a cold white strip light along the ceiling panels; amber light from the black
  hole enters only through windows, from the upper left; nothing blooms.
S4  LIGHT: The amber band of the black hole, behind the station, is the only strong light, from
  the upper left; inside, dim cold blue panels and amber window light across the seats.
S5  LIGHT: Amber light from the black hole's band grazes the collars from the upper left,
  shadows black and hard; the small bay inside is dim and cold.
S6  LIGHT: Hard blue-white light from the station's main engines at its far end joins the black
  hole's amber band from the upper left; inside, steady cold white panels.
IŞIK TAKVİMİ (SPEC C): key kadran 10 (sol üst) · dış ~2700 K kehribar · iç 5600 K soğuk ·
    S6'da +7000 K motor ışığı (OLAY: K22/K23 sınırı) · ardışık sahnede yön farkı 0°
```

### ⚙️ Physics Bible — PHYSICS (24/24 video birebir) + AUDIO ilk cümlesi (sahne içinde birebir)

```
PHYSICS: Orbital free fall: microgravity inside the pressurised hulls, hard vacuum outside. The
  large station turns on its long axis once every forty seconds. Thruster gas is a short
  straight cone gone within a hull-length.

S1  AUDIO: No sound through the vacuum; only a faint radio carrier hiss and slow breathing
  inside a closed helmet.
S2  AUDIO: No sound through the vacuum; inside, a low cabin hum and a soft wavering warning tone
  carry through the hull.
S3  AUDIO: No sound through the vacuum; inside, air through a vent and a dull knock through the
  hull at every touch on a rail.
S4  AUDIO: No sound through the vacuum; inside, a low cabin hum and a close radio carrier hiss.
S5  AUDIO: No sound through the vacuum; only the radio channel, a faint carrier hiss and two
  people breathing slowly.
S6  AUDIO: No sound through the vacuum; a deep steady tremor carries through both hulls and into
  the seats.
REPLİK cümlesi: "A man's/woman's voice comes over the helmet radio, band-limited: "…"" · makine:
    "a flat synthetic ship voice from the cabin speaker" · kayıt: "from a flight recording" · AUDIO ikinci
    cümlesi "heard only, never shown as text. No music." · repliksiz: "No dialogue. No music."
SIRT (video, IN FRAME back): "The back of the suit is one continuous smooth surface from collar to hip."
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 + bu filmin yasak havuzu (prompta ≤3 cümle)

```
ÇEKİRDEK (§5.1 · video 8 · image 7 — ① yalnız video):
① Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.
② Exactly one human character, no duplicates, no second person.
   → K04/K08: Exactly 2 human characters, no duplicates, no third person.
③ 0% bloom, no glow, no soft focus, every surface keeps visible texture.
④ No readable text, letters, digits or symbols on any display, surface, patch or sign — none on
   the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no
   captions, no watermark.
⑤ Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no
   airbrushing, no waxy texture, no face morphing.   (yüz yoksa: "no CGI or video-game look, no
   airbrushing, no waxy texture")
⑥ Equipment and clothing identical throughout, no drift, no gear appearing or disappearing.
⑦ Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers.
⑧ Particles obey the stated gravity with continuous momentum, never hovering, never swirling like
   liquid, terrain static, no melting or warping.

İNSANSIZ DIŞ KLİP (KART 10 · red #2 — 4 cümle, "0 human" YOK):
   [① video] + ④ (kısa: "No readable text, letters, digits or symbols on any surface in the frame
   — no subtitles, no captions, no watermark.") + ⑤ kısa + ③ + "No halo, no light shafts, no
   lens flare and no corona around any lit surface."

SAHNEYE ÖZEL HAVUZ (en çok 3):
S-a ÇIPLAK DERİ [D175]: No bare skin anywhere — none above the collar, none at the wrists between
    glove and sleeve, none at the ankles between boot and leg.
S-b VİZÖR [D146]: The visor is one flat clear pane in a thick dark rim — no dome, no bubble, no
    mirror coating, no tint and no environment reflected in it.
S-c SIRT [D139]: No back-mounted unit, no backpack and no tank on the back.
S-d YAPI [UZAY_USSU §6]: No tilt-shift look and no miniature read — the far end of the structure is
    as sharp as the near end; no logo, emblem or painted marking on any hull.
S-e HALE [§3.1]: No halo, no light shafts, no lens flare and no corona around any lit surface.
S-f EKRAN [SIGNAL KEEPERS ①]: No graphics, no symbols and no reflection of any screen on the
    helmet pane.
S-g KONUŞMA (repliksiz klipte, gerekirse): No speech of any kind occurs in this shot.
⛔ YAZILMAZ: gore · blood · wound · dead · corpse · explosion · fire · crash · collision · danger ·
   emergency · seamless · bubble (pozitif gövdede) · glowing · cinematic lighting · anamorphic ·
   tripod · "Exactly 0 human"
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi klip |
|---|---|---|---|
| İNSAN SAYISI | kadrajda en çok 2 (K04 · K06 · K08) · 9 insansız · 12 tek kişi | KART 4 | 24/24 |
| KASK TAKVİMİ | kapalı 24/24 · açık 0 | KART 3 | 24/24 |
| İSTASYON DÖNÜŞÜ | çeyrek tur / 10 s (40 s/tur) | KART 13 · 1 numaralı risk | dış klipler + K15 |
| KANAT | 3 | KART 13 | K01 K03 K05 K07 K13 K15 K24 |
| KENET KANCASI | 4 (kapanış 2,0 · 3,5 · 5,0 · 6,5 s) | KART 13 · FİNAL VURUŞ | K21 |
| YUMUŞAK TEMAS | 3,0 s · halka bir parmak esner | KART 13 | K20 |
| JET | düz kısa koni · bir gövde boyunda söner · K10 sonrası 0 | KART 6 | K03 K07 (K10 sınırı) |
| REZERV ÇİZGİSİ | tek kehribar çizgi · uzun → kısa → çok kısa · rakam 0 | KART 5 | K04 K06 K08 K11 K14 K16 |
| REPLİK | 17 tırnaklı · makine 2 · konuşan ağız 0 | KART 7 | 12 klip (K01 K02 K04 K06 K08 K12 K16 K17 K18 K19 K22 K24) |
| ÇIPLAK DERİ | 0 kare | — | 15 insanlı klip |
| YERÇEKİMİ | 0 g yörünge (iç + dış) | D200 | 48/48 PHYSICS |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 — `prompt_kontrol.py` ㉕)

> Yaşayan listeden bu filme düşen 20 ders; her satır TEK D-numarası taşır (tavan ders sayar).

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D146 | vizör tek düz pane + kalın koyu çerçeve; RK1/RK2 panelleri KAPI 0 | yüz/kask kadrajlı her klip |
| D208 | iki kimlik dört eksende zıt, her klipte aynı sıra; kimlik dizisi SPEC C'de | 15 insanlı klip |
| D167 | kişi başına ≤3 kimlik özniteliği, yüz panelde | 24/24 |
| D175 | "through the glove" 0; çıplak deri negatifi üç bölge | 15 insanlı klip |
| D214 | ilk satır IN FRAME; yalnız kadrajdaki tarif edilir | 48/48 |
| D138 | ekranlar soyut, metre promptta yok, rozet yazısız | K04 K06 K08 K11 K14 K16 K18 |
| D157 | TEK KARE satırı taşıyıcı nesne adlarını taşır (yanaşma ekranı · kenet halkası) | PLAN · K16 · K17 |
| D179 | IMAGE = önce (jet açık · ekran zaten kara · halkalar aralıklı · motor zaten çalışıyor) | K10 K16 K20 K21 K23 |
| D141 | FİNAL VURUŞ KANITI: dört kanca, adet 4, 8,0 s karesi | K21 · SPEC B |
| D202 | ÇAPA ÜÇLÜSÜ aynı kanalda (el + omuz) | K08 K18 K23 |
| D193 | ışık takvimi: key kadran 10 tek kaynak, sahne içi LIGHT birebir | 48/48 |
| D209 | dünya çapası üç cümle birebir | dış klipler |
| D203 | SPEC DIALOGUE LINES = prompt tırnak sayısı (17) | replikli klipler |
| D217 | her replik görünmeyeni taşır (SAPMA 1) | R1-R17 |
| D213 | temas · değişim · sonuç aynı klipte | K10 K20 K21 |
| D78 | metinsiz sayaç (kanat dönüş hızı) tek karede iki uç | K13 K14 K15 |
| D192 | 1 numaralı risk SAYIYLA (çeyrek tur / 10 s) | K15 |
| D34 | özel ad promptta 0; kart 0 s; son kare tutulur | 48/48 · K24 |
| D200 | tek rejim — PHYSICS 48/48 birebir; yürüme yok, raydan çekilme | 48/48 |
| D139 | sırt kadrajdaysa pozitif sırt cümlesi | K02 K04 K06 K08 K09 K10 K11 K12 K14 K16 K17 K19 K22 |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle

| ders | neden bu filmde ayrı kilit olarak uygulanmadı |
|---|---|
| D206 | içeriği D202 satırında (ödeme kanalı + saniye BEDEL EĞRİSİ'nde) — ayrı satır tavanı aşar |
| D201 | içeriği D193 satırında (vakumda tek kaynak, kadrajdaki nesneye bağlı yön) |
| D70 | içeriği D34 satırında (kurgu kapısı: süre 240 s · kart 0 s) |
| D1 · D16 · D42 · D45 · D62 · D169 · D174 · D176 · D180 · D207 · D210 · D211 · D212 · D215 · D216 | `00_ANALIZ/01_QA_DERS_HASADI.md` §1b — her biri ya şablon disiplini (V3 · çekirdek) ya PLAN bloğu (ÜRETİM SIRASI · KESİLEMEZ · spatial map · iskelet) ya MUZIK/DEFTER işi |
| D172 · D198 | etiket uymuyor — çizelgede "—" |

---

## 🛡️ POLİTİKA SATIRI (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S2 · K03 — hasarlı gemi + kaçan gaz jeti + karanlık ana motor
NÖTR TARİFİ:         "a small off-white ship drifts sideways in the dark; on its left side, by the
                     nozzle cluster, the hull is opened along one seam, the edges cold and torn, and
                     a short straight cone of gas leaves it and is gone within a hull-length; the
                     large engine bell at the stern is unlit"
İKİNCİ:              S2 · K07 — "drifts sideways toward one of the station's dark fins and stops a
                     hull-length short"
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez (ajans/bayrak/logo 0).
```

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| "çarpışma" sözlüğü ve temas tehdidi görüntüsü (K07) | yakın-çarpışmanın doğrudan şiddeti | KÜTLE-HIZ: gövdenin kanada bir gövde boyu kalana dek kayması + karşı itki · ALET: rezerv çizgisi kısalır (K08) · GÖVDE: kilitli önkol, düşen omuz (K08) |
| konuşan ağız (13 replik telsizden) | yüz-söz senkronunun yakınlığı | DİNLEYEN kadrajı (K18) · bedensiz ses otoritesi |
| kask/eldiven açılması | finalde kasksız rahatlama | vizör ardında yüz + açılan el (K23) + fısıltı (K24) |

---

## 📦 REFERANS PAKETİ · QA SPEC · ÜRETİM

```
REFERANS PAKETİ:  BLIND_ORBIT_REFERANS_PAKETI.md — RK1 pilot · RK2 mühendis · RA gemi (+ hasarlı
                  hâl) · RB istasyon · RI1 kokpit · RI2 servis/optik bölme · RO iki aşamalı kenet ·
                  RD kara delik · KAPI 0
QA SPEC:          BLIND_ORBIT_QA_SPEC.md — A/B/C/E blokları · ÇAPA ÜÇLÜSÜ · KİMLİK DİZİSİ ·
                  sahne içi kesmeler · makine kapıları kuru koşulu
KESİLEMEZ:        K01 · K15 · K18 · K20 · K21 · K23 · K24 [D62]
ÜRETİM DEFTERİ:   BLIND_ORBIT_URETIM_DEFTERI.md — üç kutu (altyazı KAPALI · filigran YOK · konuşan
                  ağız kadraj dışı) KAPI 0'da [D215]
KURMACA KABULLER: istasyon boyutu/dönüşü · dört kanca (gerçek standardın donanım sayısı DEĞİL) ·
                  hızlandırılmış son yaklaşma (~120 m / ~50 s) · kara deliğe göre güvenli yörünge
```
