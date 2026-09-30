# 🎬 THE_FALLING_WORLD — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 8 dk · 48 sahne · 4 bölüm dosyası (sahip kararı; kart §2.7 2 × 24 der → D74 ①)
               ⚠️ QA birimi BÖLÜM — SPEC A `PART GRID` satırı dolu; birim kararı ⬜ K1
ORTAM:         §3.2 İNCE ATMOSFER (dış yüzey · taş ocağı · platform) +
               §3.10 BASINÇLI İÇ HACİM (galeri · gemi kabini) — ikisi de 0,30 g'de (D74 ②)
TÜR:           bilimkurgu   (tek açık dal — §4.1) · dal: hayatta kalma / tahliye (halat kulvarı)
KLİP SÜRESİ:   ⬜ 10 s VARSAYIM — ARAÇTAN ÖLÇÜLECEK [D124 · K3]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk kabul klibi>
SAHNE SAYISI:  48        RUNTIME: 480 s = 8:00 (hook S0'ın İÇİNDE; 48 × 10 s)
NUMARA:        sahibin V01-V48'i = S00-S47   (V<n> = S<n-1>)
MOTOR:         OMNI 1.1 Flash (I2V) · ZİNCİR MODU ① tek başlangıç karesi (⬜ K2: 9 küme çifti için ②)
LOGLINE:       Kara deliğin yanındaki bir gezegende zemin parça parça çökerken, birbirine
               halatla bağlı iki astronot kaçış gemisine ulaşmaya çalışır.
NEDEN İZLENİR: Altlarındaki son zemin kaybolmadan ikisi de gemiye binebilecek mi?
```

### 🧭 D74 KAYITLARI — bilinçli sapmalar ve sahip kararları (kaydı olmayan sapma yapılmamış sapmadır)

| # | kural / kart | sapma | gerekçe |
|:--:|---|---|---|
| ① | §2.7 "2 bölüm × 24" | 4 bölüm dosyası × 12 sahne | sahip 18.09.2026; son iki 8 dk filminin emsali · QA birimi K1 |
| ② | §3.2 kartının Mars 0,38 g satırı · §3.10'un 0 g satırları | tek sayı: **0,30 g**, dış ve iç hacimde AYNI | düşüş süreleri, toz oturması ve halat gerilmesi bu sayıya bağlı; sayı yazılmazsa her prompt kendi yerçekimini uydurur |
| ③ | D79 vizör cümlesi (berrak cam · yüz okunur) | vizör TAMAMEN OPAK, cümle HİÇ yazılmaz | sahibin sert kısıtı: "Hiçbir sahnede yüz, göz veya ağız görünmüyor. Kabinde de vizörler açılmıyor." §5.2'nin belgelenmiş dalı |
| ④ | D196 + KART 12 "temas yalnız BEDEL sahnesinde" | 6 temas sahnesi (S00 · S17 · S29 · S41 · S43 · S46) | temas filmin TEMASIDIR (GÜVEN); kural es geçilmiyor, SAYILABİLİR yapılıyor — altısı da eldiven ↔ sert manşet, sıfır ten, her birinde sınır cümlesi |
| ⑤ | ⭐VİRAL'in YÜZ satırı | YAZILAMIYOR — etiket yalnız HAREKET satırıyla taşınıyor | yüz kanalı fiziken kapalı; telafi S41'de BAŞ AÇISI (aktarımdan önce yukarı, sonra aşağı) |
| ⑥ | Politika imzası ⑥'nın ölçülmüş panzehiri (berrak vizör) | KULLANILAMIYOR | telafi: her karede ÇEVRESEL ÇAPA — 24 kurulumun 24'ünde figür tanınabilir bir yapı/araç/gemi parçasıyla aynı karede |
| ⑦ | D79/D139 "düz sırt · sırt ünitesi yok" | İKİ FARKLI SIRT ÜNİTESİ var ve kalıcı | ayırt etme yükü yüz kapalı olduğu için RENK + OMUZ + SIRT GEOMETRİSİ'nde; sırt ünitesi bu filmin kimlik taşıyıcısıdır. D139'un asıl talebi karşılanıyor: sırt POZİTİF yüzey cümlesiyle yazılıyor (bir sürekli kaburgalı yüzey) ve ünite onun ÜSTÜNE monte ediliyor; NEGATIVE'de sırt sırt çantası/hortum/kablo yasağı duruyor |
| ⑧ | Kara deliğin gelgit çöküş HIZI | KURGU — YAYIN_PAKETI'nin VERIFIED SCIENCE satırlarına GİRMEZ | oraya yalnız doğrulanabilirler yazılır: merceklenmiş disk görünümü, olay ufkuna girilmemesi, ince atmosferde ses/toz davranışı, düşük çekimde düşüş süresi |

---

## 🎭 TEMA

```
TEMA: GÜVEN
           (depoda 0 kez işlenmiş; TEMA_MUHENDISLIGI §3b'ye ÜÇÜNCÜ aday etiket
           olarak eklendi — pazar ve kuşak sütunları ÖLÇÜLMEDİ → BOŞ kalır)
TANIM:     Başta arkadaşını taşıyan insan, sonunda kendi hayatını onun eline bırakır.
           ⛔ TAKAS kalıbı değil, TANIM cümlesi [§3c moratoryumu]
MOTİF:     uzatılan el / gerilen hat
KANALLAR:  KAMERA+IŞIK  iki gövde aynı kadrajda ama aralarında boşluk; ikisini BİRDEN
                        aydınlatan TEK güneş (ayrı ışık = ayrı dünya)
           NESNE İNDEKSİ  sarı halat — kimin elinde, kimin kemerinde, kimin aletinde
           KİNESİK        bırakma jesti: parmaklar tek tek açılır, ağırlık ötekinin
                          eline geçer (bağlı akıştan serbest akışa)
MOTİF SAHNELERİ (B3 ≥3): S00 · S02 · S24 · S29 · S41 · S46   → 6 ✅
TEMA-FİNAL UYUMU (§6): S46'da iki eldiven birbirine dokunur, aralarında KESİK halat
           sallanır (3. derece nesne indeksi); S47'de gemi uzaklaşır
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ: İLİŞKİ (kılavuzun ÜÇÜNCÜ tercihi) — bu deponun bu tipteki İLK filmi
NOVUM:      Bu dünyada kimse kendini kurtaramaz; her kurtuluş, birini bağlayan
            hattın BAŞKASI tarafından kesilmesidir.
NOVUM TAŞIYICISI: sarı emniyet halatı × BAŞKASININ ayırması → kimse kendi hattını ayıramaz
            (BEYAZ ayırır S02 ↔ TURUNCU ayırır S42 — aynı nesne, ters yön)
⛔ ÇÖKEN GEZEGEN NOVUM DEĞİLDİR — ORTAMDIR [kılavuz §0③]. Novum ilişkinin kuralıdır.

KAPI ① TEK KARE          ✅ S41 — cümle taşıyıcının ADINI taşır: *sarı emniyet halatı
                            Beyaz'ın kemerinden enkazın altına gidiyor ve onu aşağı çekiyor,
                            gemiye giden kol hâlâ gergin.* [D157]
KAPI ② KİNETİK BAĞIMSIZLIK ✅ halat kendi başına hareket eder: gerilir, sıkışır, yük alır,
                            ayrılır — hiçbirinde insan açıklaması gerekmez
KAPI ③ BAŞLIK ŞEMASI      ✅ "Cut the Right Line"

KURAL TEKRARI (≥3 · farklı nesnelerle):
  S01-S02  KURULUM    gri sandık kayışı kesilir → sandık gider, insan kalır
  S25-S27  DOĞRULAMA  sarı halat yük alır → insan kalır, direk gider
  S42      SONUÇ      sarı halatın bir KOLU kesilir → insan kalır, enkaz gider
  ⇒ 3 kez, 2 farklı nesne, 3 farklı sonuç ✅

⬜ DÜRÜST SINIR: İLİŞKİ tipinin thumb-stop sütunu kılavuzda BOŞtur. Bu film o
   sütunun İLK veri noktası olur; tahminle doldurulmaz.
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
İSTEK:   BEYAZ, EKİBİ VE NUMUNELERİ GEMİYE BİNDİRMEK ister. Film başlamadan
         başlamış İŞ: yüzey numunelerini toplamak — S01'de sandık hâlâ
         TURUNCU'nun kemerindedir, kimse onu toplamaya "karar vermez".
ENGEL:   Zemin parça parça çöküyor ve tek çıkış tek yönde. ÜÇ kademede büyür,
         her kademe bir şey KAPATIR:  ① S13 araç gider → geri dönüş kapanır
         ② S16 sol kol gider → tek elle çalışılır  ③ S36 halat sıkışır →
         gemi ile BEYAZ aynı anda kurtulamaz
BEDEL:   BEYAZ'IN SOL KOLU İŞLEVİNİ KAYBEDER · **S16** — ve geri kazanmaz.
         İKİNCİ BEDEL (doruk): kendini kurtarma ihtimalini bırakır · **S41**
MUHATAP: İKİNCİ İNSAN — TURUNCU
AYRILIK: **S40** — BEYAZ koltuktan kalkmamasını söyler, TURUNCU yine de kalkar
         [00_HIKAYE_ONAYI SAPMA 1 · sahip onayladı 18.09.2026]
```

```
🔀 İSTEK ÇAPRAZI  [`IKI_KISI_VE_AYRILIK` §3]
  BEYAZ → TURUNCU'dan:  YERİNDE KALMASINI (S31'de hattın ucunu ONA uzatır ve
                        gemi halkasına BAĞLATIR; kendi ucunu kemerinde tutar)
  TURUNCU → BEYAZ'dan:  HATTIN UCUNU BIRAKMAMASINI (S24 bağlar · S27 toplar ·
                        S36'da ilk baktığı yer hattır, insan değil)
  NESNE:   İNCE SARI ORTAK EMNİYET HALATI — tek nesne, iki istek
  ÇAKIŞMA: S40 — biri BAĞLI KALMAK ister, öteki AYRILMAK; geri adımı BEYAZ atar (S41)
```

## 👤 KARAKTER KARTI — davranış (kart PROMPTA GİRMEZ · `KARAKTER_KARTI_VE_DAVRANIS` §1)

```
👤 BEYAZ (kirli beyaz giysi · kobalt mavi omuzlar · sol önkolda düz alet)
ROL            saha lideri — aleti O taşır, kararı O verir                S00-S02
İSTEK          ekibi ve numuneleri gemiye bindirmek                        S01
BASKI TEPKİSİ  KONTROL EDER — önce ölçer, sonra tek hamle                  S01 · S06 · S34
ALIŞKANLIK     her tehlikeli geçişten önce kendi kemerindeki bağı sağ
               eliyle bir kez yoklar                                       S04 · S20 · S31
               KIRILIR: S37 — yoklayacak eli eşiği tutuyordur
SINIR          yardım İSTEMEZ; kendi yükünü başkasına vermez               S25-S28
               FİLM ONU ÇİZGİYE GETİRİR: S39'da söyler, S41'de bırakır
ZAAF           sol kol S16'dan sonra yük taşımaz; efor sağ omuzda birikir  S17-S47
TEL            sağ elin başparmağı avuca kapanır, tutuş ikiye katlanır     S25 · S37 · S39
İLK ↔ SON      S00 başkasının bileğini yakalar ↔ S41 kendi bileğini verir
               → adlandırılabilir TEK fark: EL YÖNÜ DEĞİŞİR

👤 TURUNCU (yanık turuncu giysi · siyah üst kollar · bel onarım kiti)
ROL            teknisyen — bağlar, sarar, onarır; aleti taşımaz            S04 · S17 · S24
İSTEK          BEYAZ'ı yanında tutmak — hattı hep BAĞLI tutmak             S04'ten
BASKI TEPKİSİ  ACELE EDER — önce hamle eder, sonra bakar                   S14 · S23 · S40
ALIŞKANLIK     her yeni sahanlıkta önce SABİT NOKTA arar ve hattı bağlar   S24 · S27 · S31
               KIRILIR: S41 — sabit nokta YOKTUR, kendi gövdesi olur
SINIR          yerini terk etmez (kalkarsa gemi sahipsiz)                  S33 · S40
               FİLM ONU ÇİZGİYE GETİRİR: S40'ta kalkar
ZAAF           iki eliyle çalışırken gövdesi öne düşer; dengesi ellerinde  S20 · S22 · S42
TEL            başı hedefe değil HATTA döner — önce ipi, sonra insanı      S27 · S36 · S38
İLK ↔ SON      S00 bileği başkasının elinde ↔ S42 başkasının hattını kesen el
               → EL YÖNÜ DEĞİŞİR (tersine)

AYRIŞMA: 5 davranış satırında ✅ (şart ≥3)
  ① KONTROL EDER ↔ ACELE EDER   ② kendine bakar ↔ yapıya bakar
  ③ TUTUŞ ↔ BAKIŞ               ④ yardım istemez ↔ yerini terk etmez
  ⑤ ekipman hasarı ↔ denge
```

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % (480 s) | sahne |
|---|---|---|---|
| 1 | Açılış imajı | %0-2 | S0 (0:00) |
| 2 | Kurulum | %0-10 | S0-S4 |
| 3 | Katalizör | %10-15 | S6-S7 (1:00-1:20) — gemi YERE BAĞLI |
| 4 | Tartışma | %15-25 | S8-S11 |
| 5 | Orta nokta | ~%50 | S24 (4:00) — BEYAZ'ın hayatı BAŞKASININ düğümüne girer |
| 6 | Merkezî seçim | %60 | S28-S29 (4:40-5:00) — ROL TERSİNE DÖNER |
| 7 | Umut-önce-düşüş | %77 | S35 (5:50) |
| 8 | Her şeyin kaybı | %79-81 | S36-S37 (6:00-6:20) |
| 9 | Final aksiyonu | %83-94 | S39-S45 |
| 10 | Duygusal karşılık | %96 | S46 (7:40) |
| 11 | Kapanış imajı | %98-100 | S47 (7:50) |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:        IN MEDIAS RES — düşüş 0:00'da ZATEN olmuş
S0 SORUSU:        "Bu eli tutan adam onu yukarı çekebilecek mi — ve altındaki
                  zemin ne kadar dayanacak?"
S1 İKİNCİ BİLGİ:  düşen adamı aşağı çeken şey kemerindeki sandıktır; ötekinin
                  sol önkolunda düz bir alet vardır (TOHUM)
İLK 2 SN SESİ:    boğuk dış uğultu + kask içi İKİ AYRI nefes ritmi; müzik YOK
AÇILIŞ↔KAPANIŞ:   KAFİYE — bir el bir bileği tutar (S0) ↔ iki parmak bir eldivene
                  dokunur (S46). Değişen TEK değişken: TUTUŞUN YÖNÜ
TOHUM:            S01-S02 alet · ödemesi S42 · ara görünüm S39
BİLGİ ASİMETRİSİ: DRAMATİK İRONİ — izleyici S31'de hattın ucunu gemi halkasında
                  GÖRÜR; S36'da tehlikeyi BEYAZ'dan önce anlar
FİNAL TİPİ:       KAPALI + tek açık uç
KAPAK ANI:        S41 · 7:00+4 s   (KAPAK B adayı: S00 · 0:04)
```

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` ve `KURGU_RITMI §2`
> örüntü kırıcı — ardışık iki sahne aynı ölçek + palet + ses dokusunda olamaz
> (`00_ANALIZ/03_SAHNE_SIRALAMASI.md` §3'te mekanik denetlendi: 47/47 bant içi).
> Ses kodları: Y1 dış yüzey · Y2 araç kabini · Y3 ocak · Y4 galeri içi ·
> Y5 platform · Y6 kabin. Bütçe sütunu: davranış harfi · tempo · efor kanalı.
> ◆ = bölüm sınırı.

| S | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S0 | Bilek | Turuncu yarığa beline kadar düşer; Beyaz kayarak gelip bileğini yakalar. | A · 24mm · MLS · low angle | Y1 | R · H · el: kavrama · yük SOL+SAĞ |
| S1 | Sandık kayıyor | Turuncu'nun kemerindeki numune sandığı yarığa kayar; Beyaz kesicisini çıkarır. | B · 50mm · CU · high angle | Y1 | T · H · el: alet · yürüyüş yok |
| S2 | Kayış ayrılır | Beyaz sandığın kayışını keser; sandık düşer, Turuncu kenarın üstüne çekilir. | B · küme S1 · 50mm · CU · high angle | Y1 | K · N · el: alet · yük SAĞ |
| S3 | Sırttaki gemi | İkisi araca koşarken ileride kaya sırtındaki küçük kaçış gemisi görünür. | A · dönüş S0 · 24mm · MLS · low angle | Y1 | B · H · yürüyüş: koşu kadansı |
| S4 | Makara | Beyaz sürücü yerine, Turuncu yanına biner; ortak halat makaraya alınır. | C · 35mm · MS · eye level | Y2 | G · N · eşya: makara · sırt |
| S5 | Arkadaki zemin | Araç hızlanır; arkalarındaki zemin parça parça aşağı çöker. | E · 24mm · WS · high angle | Y1 | G · H · — |
| S6 | Devrilen kule | Servis kulesi yola devrilir; Beyaz direksiyonu kırıp taş ocağına iner. | E · küme S5 · 24mm · WS · high angle | Y1 | R · H · el: direksiyon |
| S7 | Kırmızı kalan işaret | Turuncu uzaktan kalkışı dener; gemi yere bağlıdır, işaret kırmızı kalır. | C · dönüş S4 · 35mm · MS · eye level | Y2 | D · N · el: bilek kumandası |
| S8 | Dar yol | Araç ocağın dar yoluna girer; bir yanda kaya duvarı, bir yanda boşluk. | F · 35mm · MLS · eye level | Y3 | G · H · el: direksiyon |
| S9 | Bükülen tekerlek | Kopan kaya sol arka tekerleği büker; araç savrulur, Beyaz düzeltir. | G · 50mm · CU · low angle | Y3 | R · H · el: direksiyon · yük SAĞ |
| S10 | Kapanan dönüş | Kaya kolonu arkalarında yola devrilir ve dönüş yolunu kapatır. | F · dönüş S8 · 35mm · MLS · eye level | Y3 | R · N · — |
| S11 | Açılan yol | Yol ileride açılmaya başlar; Beyaz aracı galeri sahanlığına yöneltir. | F · küme S10 · 35mm · MLS · eye level | Y3 | G · H · el: direksiyon |
| S12 | ◆ Eğik sahanlık | Araç eğik sahanlıkta durur; ikisi kafesten çıkıp sağlam basamağa geçer. | I · 24mm · WS · high angle | Y3 | G · N · yürüyüş: iniş |
| S13 | Aracın düşüşü | Sahanlığın araç altındaki bölümü kopar; keşif aracı uçuruma düşer. | I · küme S12 · 24mm · WS · high angle | Y3 | R · H · — |
| S14 | Servis kapısı | Turuncu servis kapısını omzuyla iter; ikisi galeriye girer. | K · 24mm · MLS · low angle | Y4 | G · N · omuz: kapı itişi |
| S15 | Yana yatan koridor | Galeri taşıyıcıları kayar, koridor yana yatar; ikisi korkuluğa tutunur. | K · küme S14 · 24mm · MLS · low angle | Y4 | R · H · el: korkuluk · iki kol |
| S16 | Kiriş | Gevşeyen kiriş Beyaz'ın sol önkolunu sıkıştırır; kol artık yük taşımaz. | L · 35mm · MS · profile | Y4 | B · H · yük SAĞ kola geçer (kalıcı) |
| S17 | Gümüş bant | Turuncu gümüş bandı sol manşete sarar; sızdırmazlık döner, kol dönmez. | L · küme S16 · 35mm · MS · profile | Y4 | G · Y · el: bant sarma (TURUNCU) |
| S18 | Karşı kapı | İkisi karşı kapıdan çıkar; arkalarındaki galeri bölümü kopup aşağı kayar. | K · dönüş S15 · 24mm · MLS · low angle | Y4 | R · H · yürüyüş: çıkış |
| S19 | Kesilen yol | Gemi yakındır ama yol yarıkla kesilmiştir; devrilmiş direk geçit olur. | M · 24mm · WS · eye level | Y1 | T · N · — |
| S20 | Kafese çıkış | Turuncu direğe çıkar; kafes esner, o ağırlığını alçaltarak ilerler. | N · 35mm · MLS · low angle | Y1 | D · Y · yük: bot + iki el (TURUNCU) |
| S21 | Önde ve geride | Turuncu önde, Beyaz geride kafeste ilerler; altlarındaki yarık açılmayı sürdürür. | O · 50mm · MS · eye level | Y1 | G · Y · yürüyüş: kafes adımı |
| S22 | Dönen yüzey | Direğin orta eklemi kayar, yürüyüş yüzeyi döner; ikisi gövdeye kapanır. | N · dönüş S20 · 35mm · MLS · low angle | Y1 | R · H · gövde: kafese kapanma |
| S23 | Karşı sahanlık | Turuncu son bölümden karşı sahanlığa geçer ve hemen Beyaz'a döner. | P · 35mm · MS · eye level | Y1 | G · N · yürüyüş: geçiş |
| S24 | ◆ Düğüm | Turuncu halatı karşı korkuluğa bağlar; Beyaz kalan bölümü geçmeye başlar. | R · 50mm · CU · high angle | Y1 | G · Y · el: düğüm (TURUNCU) |
| S25 | Kopan destek | Direğin desteği kopar; Beyaz düşer, halat onu duvarın yanında durdurur. | M · 24mm · WS · eye level | Y1 | R · H · yük: halat ilk kez |
| S26 | Duvar | Beyaz kaya duvarına çarpar; sağ eliyle halatı tutup ayaklarını dayar. | Q · 35mm · MS · eye level | Y1 | R · H · el: SAĞ tek · bot dayanışı |
| S27 | Toplanan halat | Turuncu sabit noktadan halatı toplar; arkada kopan direk boşluğa düşer. | M · dönüş S25 · 24mm · WS · eye level | Y1 | G · N · yük: çekiş kadansı (TURUNCU) |
| S28 | Çıkıntı | Beyaz botunu çıkıntıya basıp sağ eliyle üst basamağa uzanır. | Q · dönüş S26 · 35mm · MS · eye level | Y1 | D · Y · el: SAĞ uzanma · bot çıkıntı |
| S29 | İkinci bilek | Turuncu Beyaz'ın sağ bileğini yakalayıp onu sahanlığın üstüne alır. | R · 50mm · CU · high angle | Y1 | G · N · el: bilek (TURUNCU çeker) |
| S30 | Rampa | Sahanlığın dış kenarı çatlar; ikisi rampadan gemi platformuna ilerler. | S · 24mm · WS · eye level | Y5 | S · Y · yürüyüş: rampa · nefes |
| S31 | Sarı halka | Turuncu ortak halatın ucunu gemi kapısındaki sarı halkaya aktarır. | T · 50mm · CU · high angle | Y5 | G · N · el: halka aktarımı |
| S32 | Ayırıcı | Turuncu kontrol yerine geçer; Beyaz dışarıda sıkışmış servis ayırıcısına ulaşır. | S · dönüş S30 · 24mm · WS · eye level | Y5 | G · N · yürüyüş: ayrışma |
| S33 | Titreyen gemi | Turuncu motorları hazırlar; gemi titrer, yer bağlantısı hâlâ takılıdır. | U · 35mm · MS · eye level | Y6 | T · H · el: kontrol yeri |
| S34 | Eğilmiş kapak | Beyaz eğilmiş kapağı sağ eliyle açar; manuel kolun yolu serbest kalır. | V · 50mm · CU · high angle | Y5 | D · N · el: SAĞ tek · kapak |
| S35 | Düşen bağlantı | Beyaz kolu sonuna çeker; siyah servis bağlantısı düşer, platform çatlar. | V · küme S34 · 50mm · CU · high angle | Y5 | G · H · el: SAĞ tek · kol çekişi |
| S36 | ◆ Sıkışan hat | Devrilen korkuluk sarı halatı kirişin altında sıkıştırır; Beyaz basamağını kaybeder. | W · 24mm · MLS · high angle | Y5 | R · H · — |
| S37 | Eşik | Beyaz kapı eşiğini sağ eliyle yakalar; gemi kalkar, halat gerilince durur. | W · küme S36 · 24mm · MLS · high angle | Y5 | R · H · el: SAĞ tek · eşik |
| S38 | Üç parça hat | Kapıdan bakış: halat gemi halkasından enkaza, oradan Beyaz'ın kemerine gider. | X · 24mm · WS · low angle | Y5 | S · Y · — |
| S39 | Uzanamıyorum | Beyaz kesiciye uzanamaz; sağ elini bırakırsa düşer ve bunu telsizle söyler. | W · dönüş S37 · 24mm · MLS · high angle | Y5 | T · Y · el: SOL yarım uzanma |
| S40 | Koltuktan kalkış | Beyaz kalkmamasını söyler; Turuncu yine de kemeri açıp kapıya yürür. | U · 35mm · MS · eye level | Y6 | K · N · yürüyüş: koltuktan kapıya |
| S41 | Aktarılan ağırlık | Turuncu basamaklara dayanıp Beyaz'ın sağ bileğini kavrar; Beyaz elini aktarır. | X · dönüş S38 · 24mm · WS · low angle | Y5 | B · Y · el: bilek aktarımı · yük geçer |
| S42 | Doğru hat | Turuncu kesiciyi alır ve Beyaz'ın kemerinden enkaza giden hattı keser. | Y · 50mm · CU · eye level | Y5 | K · N · el: alet (TURUNCU) |
| S43 | Kabin zemini | Turuncu Beyaz'ı eşikten kabin zeminine çeker; Beyaz korkuluğa tutunur. | Z · 35mm · MS · low angle | Y6 | B · H · yük: çekiş (TURUNCU) |
| S44 | Hızlı bağlantı | Beyaz sarı halkanın hızlı bağlantısını açar; kalan hat dışarı kayar. | Z · küme S43 · 35mm · MS · low angle | Y6 | G · N · el: hızlı bağlantı |
| S45 | Kalkış | Turuncu kalkış verir; gemi çöken platformdan yükselip kaya sırtını sıyırır. | S · 24mm · WS · eye level | Y5 | G · H · el: kontrol yeri |
| S46 | İki parmak | Beyaz iki parmağıyla Turuncu'nun eldivenine dokunur; Turuncu karşılık verir. | Z · dönüş S44 · 35mm · MS · low angle | Y6 | R · Y · el: iki parmak |
| S47 | Uzaklaşan gemi | Küçük gemi yarılmış yüzeyden uzaklaşır; kara delik gökyüzünü doldurur. | H · 24mm · WS · eye level | Y1 | S · Y · — |

```
AÇI TİPİ SAYISI: 4 ≥3 ✅   (low angle · high angle · eye level · profile)
KURULUM SAYISI:  24        (48 sahne bandının TAVANI 24 — tavanda, üstünde değil)
KURULUM İSKELETİ: A B B A C E E C F G F F I I K K L L K M N O N P R M Q M Q R S T S U V V W W X W U X Y Z Z S Z H
                 KÜME 9 ≥2 ✅   DÖNÜŞ 20/48 = %41,7 ≥%40 ✅
                 KÜME çiftleri: S1-S2 · S5-S6 · S10-S11 · S12-S13 · S14-S15 ·
                                S16-S17 · S34-S35 · S36-S37 · S43-S44
                 DÖNÜŞ: S2 S3 S6 S7 S10 S11 S13 S15 S17 S18 S22 S27 S28 S32
                        S35 S37 S39 S41 S44 S46
                 ⛔ Aynı harf AYNI kurulumdur; kamera metni Camera Bible'dan
                   BİREBİR kopyalanır + işaret satırını taşır:
                     dönüş → "— the same position, height and lens as Scene N."
                     küme  → "continues the previous clip from its exact last
                              frame — the same position, height and lens as Scene N."
BÖLÜM KESİĞİ:    S11↔S12 · S23↔S24 · S35↔S36 — üçü de ardışık ÇİFT olarak
                 denetlendi ve bant içinde; üçü QA_SPEC 🅑 B bloğuna EŞ KADRAJ
                 satırı olarak iner
```

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a)

| # | S | saniye | konuşan | REGISTER | kanal | İngilizce (post-dub) | İŞLEV (B5 satırı / vuruş) |
|---|---|---|---|---|---|---|---|
| R1 | S7 | 74 s | TURUNCU | düz bildirim | telsiz | Ship's still tied down. | ENGEL③'ü adlandırır · katalizör |
| R2 | S16 | 166 s | BEYAZ | kısık, tek nefeste | telsiz | Left cuff is locked. | BEDEL③'ü MALZEME diliyle ilan eder |
| R3 | S19 | 193 s | TURUNCU | plan bildirir | telsiz | The mast takes us across. | ENGEL②'nin çözümü · TURUNCU öne geçer |
| R4 | S26 | 264 s | BEYAZ | kesik, yüklü | telsiz | Hold it. | İLK KEZ bir şey ister — SINIR çatlar |
| R5 | S33 | 335 s | TURUNCU | düz bildirim | telsiz | Engines are up. | umut vuruşu |
| R6 | S39 | 394 s | BEYAZ | düşük, yavaş | telsiz | I can't reach it. | SINIR kırılır (sahibin birebir repliği) |
| R7 | S40 | 402 s | BEYAZ | emir, sert | telsiz | Stay in the seat. | AYRILIK hamlesi — cevabı EYLEMLE gelir |
| R8 | S46 | 466 s | TURUNCU | çok kısık | kabin içi | Still here. | TEMA'nın sözle karşılığı — tek ve son |

```
İLK REPLİK:     S7 · 74 s · öncesindeki kesintisiz sessizlik 74 s · vuruş: katalizör
BEDENLEŞTİRME:  ⛔ YOK — FİZİKEN imkânsız. Ağız 48/48 sahnede kapalı (opak vizör).
                Bu, doruk bütçesini SERBEST bırakır ve lip-sync riskini SIFIRLAR.
REPLİKSİZ:      40/48 sahne (%83) · 480 saniyede toplam ≈11 saniye söz
⛔ Promptta TIRNAK İŞARETİ YOK (OMNI kuralı) — VIDEO promptunun AUDIO satırında
   replik TARİF edilir: one short radio line from the other suit.
⛔ İŞLEV sütunu boş replik yazılmadan silinir · replik <5 s · tek konuşmacı [D35]
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md (Kart P 2b)
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız o karenin
> `IN FRAME:` satırındaki kısmı gider. "BIBLE'a bak" atfı YASAK, ama self-contained ≠ Bible'ın
> tamamı: kadrajda olmayan YAZILMAZ. Videoya Bible girmez — `START FRAME:` tek satır.

### 👤 Character Bible

```
WHITE — SUIT (IN FRAME: torso / full body / back):
He wears a dirty off-white hard-shell pressure suit with cobalt-blue shoulder caps rising over the
collar, dark grey joint rings at the elbows and knees, heavy segmented dark-grey gloves and boots,
a short flat tool clipped along the outside of his left forearm, and a crate hook on the right of
his belt.

WHITE — HELMET (IN FRAME: full body / torso / back — never face):
His helmet is a hard off-white shell seated in a dark grey collar ring, one flat front pane inside
a thick dark-grey rim, the pane fully opaque matte black with no face, no eyes and no skin visible
from any angle.

WHITE — BACK (IN FRAME: back):
The back of his suit is one continuous ribbed surface from collar to hip, and one angular dark box is
mounted flat on it, its upper edge under the cobalt-blue shoulder caps.

WHITE — WEAR: dust sits in three fixed places from Scene 0 onward — the left cuff, the right knee
and the lower back. From Scene 16 the left cuff shell is dented inward and wrapped in silver tape,
and its joint ring no longer turns.

ORANGE — SUIT (IN FRAME: torso / full body / back):
He wears a burnt-orange hard-shell pressure suit with black upper arms from shoulder to elbow, dark
grey joint rings at the elbows and knees, heavy segmented dark-grey gloves and boots, a small flat
control block on the left wrist and a flat repair kit on the right of his belt.

ORANGE — HELMET (IN FRAME: full body / torso / back — never face):
His helmet is a hard burnt-orange shell seated in a dark grey collar ring, one flat front pane
inside a thick dark-grey rim, the pane fully opaque matte black with no face, no eyes and no skin
visible from any angle.

ORANGE — BACK (IN FRAME: back):
The back of his suit is one continuous ribbed surface from collar to hip, and one narrow dark rectangle
stands on it, tall and thin, clear of the black upper arms.

ORANGE — WEAR: dust sits in two fixed places from Scene 0 onward — both knees.

⛔ FACE bloğu YOKTUR ve yazılmaz [D74 ③]. `IN FRAME:` satırına `face` girmez.
⛔ Yaş · boy · ten PLAN'da bile yazılmaz — kimlik yığını bu filmde hiç doğmuyor [D167].
⛔ Ayrım üç kanalda: RENK + OMUZ GEOMETRİSİ + KONUM (BEYAZ sol üçte bir · TURUNCU sağ üçte bir).
```

### 🌍 World Bible — ÜÇ cümle, BİREBİR kopyalanır [D209]

```
W1  The ground is a rust-brown rock plain of flat plates split by dark open cracks, thin grey dust
    drifted along every edge.
W2  The horizon is close and slightly curved under a deep brown-violet sky with no clouds.
W3  One lensed bright ring hangs high in that sky at a fixed place, never moving, never pulsing,
    never growing.
```

```
⛔ ㉖ İLE UYUM (D214) — üçü de HER prompta girmez, kadrajda olan girer:
   GENİŞ DIŞ kurulumlar (A · E · F · H · I · M · S · X)  → W1 + W2 + W3 birebir
   DAR DIŞ kurulumlar (B · G · N · O · P · Q · R · T · V · W · Y) → yalnız W1
   İÇ HACİM (C araç kabini · K ve L galeri · U ve Z kabin)  → hiçbiri
   Gerekçe: D209 dünya ÇAPASI ister, ㉖ kadrajda olmayanı YASAKLAR. Çapa geniş
   kurulumlarda kurulur ve dar kurulumlar ona ZEMİN cümlesiyle bağlanır.
   SPEC C DÜNYA ÇAPASI sayımı: W1+W2+W3 taşıyan sahne sayısı ≥ 12 (gerçekleşen: 18 —
   A S0 S3 · E S5 S6 · F S8 S10 S11 · I S12 S13 · M S19 S25 S27 · S S30 S32 S45 ·
   X S38 S41 · H S47).
```

### 🎥 Camera Bible — 24 kurulum, her harf BİREBİR kopyalanır

| harf | mekân | sahneler | kamera cümlesi (İngilizce · karakter karakter kopyalanır) |
|:--:|---|---|---|
| A | yüzey | S0 S3 | `24mm lens on a fixed locked-off mount at ground level, 6 m from the crevasse edge, low angle medium long shot, deep focus, absolutely zero camera movement.` |
| B | yüzey | S1 S2 | `50mm lens on a fixed locked-off mount at chest height, 1.2 m from the crate on his belt, high angle close-up, deep focus, absolutely zero camera movement.` |
| C | araç kabini | S4 S7 | `35mm lens on a fixed mount inside the rover cage at seat height, 1.5 m from the right seat, eye level medium shot, deep focus, absolutely zero camera movement.` |
| E | yüzey/yol | S5 S6 | `24mm lens on a fixed locked-off mount above the road, 25 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement.` |
| F | ocak yolu | S8 S10 S11 | `35mm lens on a fixed locked-off mount at ground level, 12 m ahead on the road, eye level medium long shot, deep focus, absolutely zero camera movement.` |
| G | ocak yolu | S9 | `50mm lens on a fixed mount on the rover frame at wheel height, 2.5 m from the left rear wheel, low angle close-up, deep focus, absolutely zero camera movement.` |
| H | gök | S47 | `24mm lens on a fixed locked-off mount level with the ship's path, 60 m from the ship, eye level wide shot, deep focus, absolutely zero camera movement.` |
| I | sahanlık | S12 S13 | `24mm lens on a fixed locked-off mount above the landing, 15 m from the rover, high angle wide shot, deep focus, absolutely zero camera movement.` |
| K | galeri | S14 S15 S18 | `24mm lens on a fixed locked-off mount at waist height, 8 m along the corridor, low angle medium long shot, deep focus, absolutely zero camera movement.` |
| L | galeri | S16 S17 | `35mm lens on a fixed locked-off mount at chest height, 2.5 m from the fallen beam, profile medium shot, deep focus, absolutely zero camera movement.` |
| M | yarık | S19 S25 S27 | `24mm lens on a fixed locked-off mount at ground level, 20 m from the crevasse, eye level wide shot, deep focus, absolutely zero camera movement.` |
| N | direk | S20 S22 | `35mm lens on a fixed locked-off mount at waist height, 4 m from the mast's flank, low angle medium long shot, deep focus, absolutely zero camera movement.` |
| O | direk | S21 | `50mm lens on a fixed locked-off mount at walking-surface height, 4 m along the mast, eye level medium shot, deep focus, absolutely zero camera movement.` |
| P | karşı sahanlık | S23 | `35mm lens on a fixed locked-off mount at chest height, 3 m from the far railing, eye level medium shot, deep focus, absolutely zero camera movement.` |
| Q | duvar | S26 S28 | `35mm lens on a fixed locked-off mount at chest height, 3 m from him at the wall, eye level medium shot, deep focus, absolutely zero camera movement.` |
| R | karşı sahanlık | S24 S29 | `50mm lens on a fixed locked-off mount above the railing, 1.2 m from the two gloves, high angle close-up, deep focus, absolutely zero camera movement.` |
| S | platform | S30 S32 S45 | `24mm lens on a fixed locked-off mount at ramp height, 18 m from the ship, eye level wide shot, deep focus, absolutely zero camera movement.` |
| T | gemi kapısı | S31 | `50mm lens on a fixed locked-off mount at sill height, 1 m from the yellow ring, high angle close-up, deep focus, absolutely zero camera movement.` |
| U | kabin | S33 S40 | `35mm lens on a fixed mount inside the cabin at seat height, 1.5 m from the control station, eye level medium shot, deep focus, absolutely zero camera movement.` |
| V | platform | S34 S35 | `50mm lens on a fixed locked-off mount at deck height, 1.2 m from the service connection base, high angle close-up, deep focus, absolutely zero camera movement.` |
| W | platform | S36 S37 S39 | `24mm lens on a fixed locked-off mount at deck height, 3 m from the railing, high angle medium long shot, deep focus, absolutely zero camera movement.` |
| X | kapı dışı | S38 S41 | `24mm lens on a fixed locked-off mount 5 m out from the door sill and 4 m below it, low angle wide shot, deep focus, absolutely zero camera movement.` |
| Y | kapı eşiği | S42 | `50mm lens on a fixed locked-off mount at sill height, 1.5 m from his belt ring, eye level close-up, deep focus, absolutely zero camera movement.` |
| Z | kabin | S43 S44 S46 | `35mm lens on a fixed mount inside the cabin at floor height, 2 m from the two of them, low angle medium shot, deep focus, absolutely zero camera movement.` |

```
⛔ Her CAMERA satırı `In a single continuous shot.` ile BİTER (OMNI · D1).
⛔ Mesafe cümlesinde "behind" YOK — "back from" kullanılır.
⛔ Dönüş/küme sahnelerinde işaret cümlesi kamera satırının ARDINA eklenir.
```

### 💡 Lighting Bible

```
One hard sun sits out of frame to the upper left for the whole film; its direction never changes
and the difference between two consecutive scenes is never more than 30° and never more than 500 K.
Shadow edges are soft, not razor-sharp — the atmosphere is thin, not absent.
GALLERY (S14-S18): one yellow service lamp high on the right inside the frame, plus one cold slice
of daylight entering from a crack on the left.
CABIN (S33 · S40 · S43 · S44 · S46): one neutral 4500K panel above the control station, one narrow
orange strip along the floor line.
⛔ Kask içi ışık rigi KAPALI — opak pane arkasında ışık kaynağı yok (D74 ③'ün üçüncü bedeli).
```

### ⚙️ Physics Bible

```
Gravity is 0.30 g everywhere in this film, outside and inside. A 2 m fall takes about 1.17 s.
A dropped object travels about one glove-width in its first second and about one arm-length in its
second second.
Dust rises in columns, not clouds; it falls slowly but certainly and always settles — it never hovers
and never swirls like liquid.
A broken piece keeps its rotation axis and does not slow down.
A hanging body swings with a period about 1.8 times longer than on Earth — slow and wide.
The thin atmosphere carries sound: everything is heard muffled and without high frequencies; there
is no silence outside, and no full-spectrum clarity either.
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin yasakları

> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (VIDEO 8 · IMAGE 7 cümle)
> + bu listeden sahne başına ≤3 cümle taşır (㉗).

```
N1  no cuts, no dissolves, no camera resets, no angle change (VIDEO çekirdek ①)
N2  Exactly two human characters, no duplicates, no third person (çekirdek ② — İKİ kişilik biçim)
N3  0% bloom, no glow, no soft focus, every surface keeps visible texture
N4  no readable text, letters, digits or symbols on any display, surface, patch or sign — none on
    the suits, the equipment, the rover, the ship or any rock face in the frame — no subtitles,
    no captions, no watermark
N5  photorealistic with 35mm film grain, no CGI or video-game look, no airbrushing, no waxy texture
N6  equipment and clothing identical throughout, no drift, no gear appearing or disappearing
N7  hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers
N8  particles obey 0.30 g with continuous momentum, never hovering, never swirling like liquid,
    terrain static, no melting or warping
N9  no bare skin anywhere — none at the wrist, none at the collar, none at the ankle; the pressure
    suits are never opened and the visors are never raised
N10 no face, no eyes, no mouth behind either pane; the panes stay fully opaque
N11 no fabric, no cloth, no flapping or billowing material — the suits are hard shells
N12 no miniature read, no tilt-shift, no shallow depth of field on any structure
N13 no lens flare on the lensed ring, no pulsing, no growing, no moving of the ring
N14 no wind, no rain, no liquid, no flame, no explosion
N15 no third line, no extra cable, no rope appearing that was not named
N16 no camera shake, no handheld, no push-in, no zoom, no rack focus
N17 no title card, no end card, no credits, no caption
N18 no gore, no blood, no wound — damage reads on metal only
N19 no other vehicle, no other ship, no structure that was not named
N20 no animal, no plant, no organic growth
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| yerçekimi | 0,30 g — dış ve iç AYNI | 6 · 13 | 48/48 |
| 2 m düşüş süresi | ≈1,17 s | 6 | S00 · S13 · S25 · S35 |
| düşen nesne yolu | 1. saniye bir avuç · 2. saniye bir kol boyu | 6 | S02 · S13 · S18 · S27 · S36 |
| asılı gövde salınımı | Dünya'nın ≈1,8 katı periyot | 6 | S25 · S37 · S41 |
| toz | SÜTUN, adet yazılır (2-3); perde YOK | 6 | S05 · S06 · S10 · S13 · S18 · S30 · S35 · S45 |
| kafes gözü | 0,6 m | 13 | S19-S27 |
| devrilmiş direk | 14 m · 8 bölüm | 13 | S19-S27 |
| galeri taşıyıcı aralığı | 2 m | 13 | S14-S18 |
| gemi boyu | 8 m | 13 | S03 · S19 · S30-S47 |
| keşif aracı boyu | 4 m | 13 | S03-S13 |
| sarı ortak halat | 0,02 m kalınlık · 9 m tam boy | 3 · 12 | S04-S47 |
| gri sandık kayışı | 0,015 m kalınlık · 0,6 m | 3 · 12 | S01-S02 |
| siyah servis bağlantısı | 0,08 m kalınlık | 3 · 12 | S07 · S32-S35 · S38 |
| sarı halka (gemi kapısı) | 0,12 m | 3 | S31 · S44 |
| kemer halkası (S42 kadrajı) | 0,08 m → 142 px ✅ (A5 eşiği 120 px) | 12 | S42 |
| S42 üst kol açısı | yatayla +20° · 10 s boyunca GERGİN | 12 | S42 |
| S42 alt kol açısı | yatayla −55° · iki kol farkı ≥35° | 12 | S42 |
| S42 alet mesafesi | alt kola 15 cm · üst kola hiçbir karede <40 cm | 12 | S42 |
| S42 ayrılan uç | 0,5 s'de kadraj dışı · üst kol 3 s daha gergin | 12 | S42 |
| insan sayısı | 2 — 48/48 sahne (S47'de 0, kabin ışığıyla sayılır) | 4 | tüm film |
| kabin ışığı (final sayımı) | tam 2 | 5 | S47 |
| gemi kadraj payı (final) | ≤ kadraj eninin 1/3 (gerçekleşen %8,9) | 5 · 13 | S47 |
| kask durumu | KAPALI ve OPAK — 48/48, istisna YOK | 3 · 12 | tüm film |
| temas | 6 sahne · hepsi eldiven ↔ sert manşet · 0 ten | 12 | S00 · S17 · S29 · S41 · S43 · S46 |
| ekran metni | 0,0 s | 5 | kurgu kapısı |
| replik | klipte 0 · post-dub 8 | 7 | replik tablosu |
| kurulum | 24 (tavan 24) · açı tipi 4 | 8 | Camera Bible |
| ölçek kanıtı | ana nesne ≥100 px — en düşük 112 px (L manşet) | 13 | 03 §4 kartları |
| klip · süre | 48 × 10 s = 480 s (±2 s) | 11 | kurgu kapısı |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D1 | Her video CAMERA satırı `In a single continuous shot.` ile biter; sahne = klip, klip içinde kesme yok. | 48/48 |
| D42 | BEYAZ üç sabit kir bölgesi (sol manşet · sağ diz · sırt altı), TURUNCU iki (iki diz); kir merdiveni tek yönlü. | S00-S47 · kademe S13 · S25 |
| D62 | KESİLEMEZ LİSTESİ: S41 · S42 · S45 · S47 + sekiz nefes sahnesi. | S41 · S42 · S45 · S47 |
| D138 | Prompt gövdesinde metre yok: yarık eni bir gövde boyu, direk kafesi iki gövde boyu, eldiven eni bir avuç. | 48/48 |
| D139 | `IN FRAME: back` olan promptta POZİTİF sırt cümlesi; iki sırt ünitesi birbirinin zıddı (köşeli geniş ↔ dar dikdörtgen). | S04 · S12 · S21 · S43 |
| D141 | SPEC B FİNAL VURUŞ KANITI: S47'de iki kabin ışığı SAYILIR (2) ve gemi kadraj eninin üçte birini geçmez. | S47 |
| D146 | Kask tek düz ön pane + kalın koyu gri çerçeve; `seamless` · `dome` · `bubble` hiçbir promptta yok. Pane tamamen opak. | 48/48 |
| D157 | TEK KARE cümlesi taşıyıcının ADINI taşır: sarı emniyet halatı Beyaz'ın kemerinden enkazın altına gidiyor. | S38 · S41 · S42 |
| D167 | Prompt gövdesinde figür başına en çok üç öznitelik: giysi rengi · omuz parçası · sırt ünitesi. | 48/48 |
| D169 | Efor sahnelerinde gövde tepkisi + kadans: dördüncü çekiş ilkinden yavaş, ağırlık arka bota biner. | S20-S24 · S27-S28 · S34-S35 · S43 |
| D175 | Mühür korunur: anatomi hiçbir cümlede eldiven/manşet sınırında tarif edilmez; hasar YÜZEYDE. | S16 · S17 · S28 · S40 |
| D179 | İmaj = ÇAPA'nın BEFORE'u. Düşüş anı karede YOKTUR — kare tutuşun yük aldığı andır. | S00 · S25 · S26 · S37 · S41 |
| D193 | Tek güneş film boyu aynı saat yönünde; ardışık sahne arası fark ≤30° ve ≤500 K. Galeri içi tek pratik ışık. | 48/48 · SPEC C |
| D198 | 0,30 g sayısal kilit: düşen nesne 1. saniyede bir avuç, 2. saniyede bir kol boyu; kopan parça dönme eksenini sürdürür. | S02 · S13 · S18 · S27 · S36 |
| D202 | ÇAPA ÜÇLÜSÜ: CHOICE S41 · COST S16 · FINAL S47 — her biri adlandırılabilir BEFORE/AFTER gövde çifti taşır. | S16 · S41 · S47 |
| D206 | BEDEL EĞRİSİ: sol kol S16'dan sonra hiçbir karede yük taşımaz; her bedel hücresi `<kanal> @ <saniye>`. | S16-S47 |
| D207 | Yorgunluk 0-6 ve ardışık düşüş ≤1; S25 düşüşünün kalıntısı S26'nın 0,0 s satırında devralınır. | S25-S30 · S37-S43 |
| D209 | World Bible ÜÇ cümle birebir kopyalanır: zemin · ufuk · gökteki merceklenmiş halkanın yeri. | 48/48 · SPEC C |
| D213 | TEMAS · DEĞİŞİM · SONUÇ aynı klipte: kayış ayrılır → sandık düşer → Turuncu yukarı gelir. | S02 · S10 · S13 · S18 · S36 · S42 |
| D217 | Sekiz repliğin İŞLEV hücresi GÖRÜNMEYENİ taşır; "durum bilgisi" yazılan replik silinir. | S07 · S16 · S19 · S26 · S33 · S39 · S40 · S46 |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle

| ders | neden bu filmde uygulanmadı |
|---|---|
| D16 | vizör tasarım gereği tamamen opak; yüz morph yüzeyi FİZİKEN kapalı. |
| D34 | ㉖ + şablonun `SCREEN TEXT: 0` satırı ve negatif çekirdeğin metin cümlesi bunu zaten koşuyor. |
| D45 | prompt iskeletinin sızmaması V3 şablonunun kendi kuralı; kapı ① ve ㉖ ölçüyor. |
| D70 | kurgu kapısının maddesi; üretim defterinde ve QA_SPEC'te duruyor, PLAN kilidi değil. |
| D78 | bu filmde sayaç yok; çöküşün ilerlemesi yarık genişliğiyle okunuyor (D209'a bağlı). |
| D172 | sarı halat zaten emniyet hattı olarak kuruluyor; askı düzeneği hiç kadraja girmiyor. |
| D174 | yön cümlesi nesne-göreli yazımı Camera Bible'ın kendi kuralı olarak girdi. |
| D176 | zemin tek cümle tek renk — World Bible'ın üç cümlesinde taşınıyor. |
| D180 | ses kararı MUZIK dosyasının işi; AUDIO satırı her klipte dolu. |
| D192 | A5 maddesi olarak 02_KONSEPT §5'te ve SAYISAL KİLİT LİSTESİ'nde ayrı blok hâlinde yazıldı. |
| D200 | tek g kararı Physics Bible'ın ilk satırı; D198'in sayısı onu zaten kilitliyor. |
| D201 | ortam vakum değil, ince atmosfer; güneş yönü kilidi D193 + D209'da. |
| D203 | ㉓ replik envanteri kapısı koşuyor; SPEC satırı zorunlu. |
| D208 | kimlik dizisi SPEC C'nin kendi satırı; dört referans sayfası aynı işi görselde yapıyor. |
| D210 | kafiye çifti iskelet satırında ve ⑩④ kapısında ölçülüyor. |
| D211 | hook ve final kapıları 03_SAHNE_SIRALAMASI §1'e yazıldı. |
| D212 | ardışık tekrar denetimi sahne haritasının VURUŞ sütununda yapılıyor. |
| D214 | ㉖ IN FRAME kapısı her promptta koşuyor. |
| D215 | üç araç-ayarı kutusu üretim defterinde; prompt tarafında karşılığı yok. |
| D216 | ses miksi MUZIK dosyasının tablosu; PLAN kilidi değil. |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S16 — gevşeyen kiriş BEYAZ'ın sol önkolunu sıkıştırır.
NEDEN O:  üç imza aynı karede — ⑥ yüzü kapalı figür (panzehiri YOK) + kısıtlanmış
          uzuv + tek kişilik izolasyon okuması. Deponun TEK ÇÖZÜLEMEYEN reddi tam
          bu birleşimdir: YERÇEKİMİ F1 S8 (üç yazım, üçü de düştü).
NÖTR TARİFİ:
  ① TURUNCU aynı karede ve hareket halinde → izolasyon KOMPOZİSYONLA kapatılır
  ② sonuç METALDE: manşetin dış kabuğu içeri ezilir, eklem halkası dönmeyi bırakır
  ③ ölçek daima medium shot ya da daha geniş; yakın plan YOK
  ④ yara · kan · acı · ezilen uzuv · tehlike sözcükleri NE pozitifte NE NEGATIVE'de [D123]
  ⑤ hasarın TEK kanıtı S17'nin gümüş bandıdır — hasar gösterilmez, sonucu yaşanır
  ⑥ iki yenilgide ÜÇÜNCÜ YAZIM denenmez, kamera taşınır
⛔ "riskli sahne yok" geçerli DEĞİLDİR.
PROB KLİPLERİ (ilk gün): P1 = S02 · P2 = S16 · P3 = S42 · P4 = iki figür kopyalanma probu
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Alet ADLANDIRILMIYOR, yalnız FORMU yazılıyor | aletin ne olduğu sözle söylenemiyor | ALET TEPKİSİ — alet kapandığında gri kayış AYRILIR ve düşer; işlev sonuçtan okunur |
| S16'da yakın plan kaldırıldı (ölçek MS ve geniş) | sıkışmanın şiddeti yakından görülmüyor | MALZEME SONUCU — ezik manşet + dönmeyen eklem + S17'nin gümüş bandı |
| Yara/acı sözlüğü tamamen kaldırıldı | acının sözü yok | TEMASSIZ GÖVDE TEPKİSİ — sol kol S17'den sonra 31 sahnede pasif; efor sağ omuzda birikir |
| Berrak vizör (imza ⑥'nın panzehiri) kullanılamıyor | yüz kanalı ve ⭐VİRAL'in YÜZ satırı kapandı | ÇEVRESEL ÇAPA — 24 kurulumun 24'ünde figür tanınabilir bir yapıyla aynı karede; ayrıca S41'de BAŞ AÇISI telafisi |
| S47'nin NEGATIVE bloğu kısaltıldı | tam negatif koruma yok | KÜTLE-HIZ — kadrajda insan yok; yapısal red profilinden kaçınmak koruma kaybından ucuz [KART 10] |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR. — 5/5 dolu ✅
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez. ✅
```

---

## 🧭 SPATIAL MAP — plana, prompta girmez

```
EKRAN YÖNÜ KİLİDİ: hareket film boyu SOLDAN SAĞA (gemiye doğru). Tek istisna
  S06'da araç sağa kırıp ocağa iner — kırılma OLAY gerekçelidir ve S08'de yön geri döner.
KONUM KİLİDİ:      BEYAZ SOL üçte bir · TURUNCU SAĞ üçte bir · 48/48 · merkez geçilmez
MEKÂN ZİNCİRİ:     açık yüzey (S00-S07) → taş ocağı (S08-S13) → kapalı galeri (S14-S18)
                   → yarık ve direk (S19-S29) → gemi platformu (S30-S37)
                   → kapı ve dış (S38-S42) → kabin (S43-S46) → gök (S47)
GÜNEŞ:             sol üst, kadraj dışı, 48/48 sabit
DİSK:              ufkun üstünde sabit yerde; hiçbir sarsıntıda nabız atmaz, büyümez
```

---

## ✅ KAPI KAYDI

```
✅ konsept kapısı ①②③        ✅ B5 dörtlüsü + AYRILIK S40 + İSTEK ÇAPRAZI
✅ iki karakter kartı (5 satırda ayrışıyor)   ✅ vuruş tablosu 11 satır
✅ sahne haritası 48/48        ✅ kurulum iskeleti 48 harf · KÜME 9 · DÖNÜŞ %41,7 · 24 kurulum
✅ replik tablosu 8 satır      ✅ altı Bible yazıldı (Character · World · Camera · Lighting · Physics · Negative)
✅ sayısal kilit listesi 30 satır   ✅ ders kilidi 20/20 (tavan) + 20 uygulanmayan gerekçeli
✅ politika satırı + 5 önlem, 5 telafi   ✅ D74 kayıtları 7 satır
⬜ klip süresi ÖLÇÜLMEDİ [D124 · K3]     ⬜ zincir modu ② kararı [K2]     ⬜ QA birimi [K1]
→ BOLUM_1..4 (96 prompt) YAZILABİLİR
```
