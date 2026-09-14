# 🎞️ THE_COUNTED_TURN — SAHNE SIRALAMASI

> **Bu dosya sıranın TÜRETİLDİĞİ ve DENETLENDİĞİ yerdir.** Sonuç `THE_COUNTED_TURN_PLAN.md`
> §SAHNE HARİTASI'na taşınır — orası sonucu taşır, burası hesabı.
> ⛔ Bu dosyada `## ... SAHNE <n>` biçiminde başlık yoktur (kapı betiği o
> deseni sahne sanar); sahneler TABLO satırıdır.
>
> Girdi: `02_KONSEPT_VE_RISK.md` (25 sahne · B5 · tema İNSAN-MAKİNE · risk 9/14).

---

## 0. 🧮 IZGARA VE ZAMAN — her şey bu iki satırdan türer

```
IZGARA:   S0 = 9,0 s hook · S1…S24 = 10,0 s   →   toplam 249,0 s = 4:09
FORMÜL:   başlangıç(S_n) = 9 + (n−1) × 10        [D122 — hesaplanmaz, hesaplatılır]
          S1 = 9 · S6 = 59 · S12 = 119 · S13 = 129 · S18 = 179 · S20 = 199 ·
          S22 = 219 · S24 = 239 (bitiş 249,0)
⛔ KLİP SÜRESİ üretimden önce ffprobe ile ÖLÇÜLECEK [D124]. 10,0 s'den saparsa
  bu bloktaki BÜTÜN zaman kodları yeniden hesaplanır.

DÖNME BANDI (02_KONSEPT §5 A5'ten):  ω(n) = 0,3142 + 0,008725·n  rad/s
  a(n) = 12·ω²  ·  RPM(n) = 9,5493·ω  ·  sarkma(n) = 4,00 × a(n)/1,184  cm
```

## 1. 🥁 VURUŞ TABLOSU — sahne dağıtılmadan ÖNCE (`SENARYO_VE_VIRAL_KAMERA` §2)

> ⚠️ **DÜRÜST KAYIT:** §2'de 3-5 dk için ayrı eşleme tablosu YOK (§2.1 dikey,
> §2.2 yatay 2-4 dk). Vuruşlar §2.2'nin YÜZDE bantları 249,0 s'ye uygulanarak
> ve `SAVAS_SENARYO` §14 Hauge tablosunun **25 sahne sütunu** ile çapraz
> doğrulanarak yerleştirildi. İkisi bağımsız olarak aynı yerlere düştü.

| # | vuruş | % | saniye | hangi sahnede | Hauge 25-sütunu | boşsa gerekçe |
|---|---|:--:|:--:|:--:|:--:|---|
| 1 | Açılış imajı | %0-4 | 0-9 | **S0** | — | — |
| 2 | Kurulum | %0-12 | 0-29 | S0-S2 | — | — |
| 3 | **Katalizör** | %4-8 | 9-19 | **S1** | Fırsat S2-3 | ⛔ ilk 15 saniyeyi geçmiyor (HOOK kapısı) |
| 4 | Tartışma | %12-24 | 29-59 | S3-S5 | — | atlanmadı |
| 5 | Eşik / plan değişikliği | %25 | 59-69 | **S7** | **S6** | ±1 sahne — kabul |
| 6 | Orta nokta | %48-52 | 119-139 | **S12-S13** | **S12-13** | ⭐ bölüm sınırı burada |
| 7 | Umut-önce-düşüş | %68 | 169-179 | **S17** | — | — |
| 8 | Her Şeyin Kaybı | %72-76 | 179-189 | **S18** | **S19** | ±1 sahne — kabul |
| 9 | Tercih / merkezî seçim | %80 | 199-209 | **S20** | — | — |
| 10 | Doruk | %84-92 | 209-229 | **S21-S22** | Son itiş S23-25 | — |
| 11 | Kapanış imajı | %96-100 | 239-249 | **S24** | — | — |

```
HOOK TİPİ:        KURAL İHLALİ (bir kural bozuluyor) — bir YER değil bir DURUM.
                  ⭐ Ölçülmüş gerekçe: Ring Walker'ın açılışı devasa halka
                  gökyüzüydü ve Kanca 5/10 aldı ("bir YER"); Inversion'ın
                  açılışı havalanan bir çakıl taşıydı ve 6/10 aldı ("bir KURAL
                  BOZULUYOR") — serinin ölçülmüş en iyi kancası. Aynı 10 saniye,
                  fark: biri manzara, öteki OLAY. Bu film ikincisini seçiyor.
S0 SORUSU:        "Neden yana düştü?"
S1 İKİNCİ BİLGİ:  Düşüş bir kez olmadı — dikişte zaten iki cıvata var. Ve
                  yapının içinden tek bir vuruş geçtikten sonra arka plandaki
                  yıldızlar daha hızlı akıyor. (Katalizör: sayım BAŞLADI.)
İLK 2 SN SESİ:    Eldivenin güverte dikişine değmesi — yapı bir çandır: temas
                  milisaniyelerde halkayı dolaşıp çok yansımalı uzun bir
                  kuyrukla döner. Vakumda duyulan tek şey TEMASTIR.
AÇILIŞ↔KAPANIŞ:   **KAFİYE** (3-5 dk bandının çifti · loop DEĞİL)
                  Değişen TEK değişken: **kadrajın merkezindeki KAPANIŞ PİMİ** —
                  S0'da BOŞ, S24'te üstünde İKİ klips ve biri AÇIK.
                  ⭐ Halka kapandığı için ilk açıklığın ve son açıklığın ucu
                  AYNI PİMDİR: iki klips 0,7 m'de aynı ECU kadrajına sığar.
                  ⚠️ Alt kenardaki cıvata yığını sayacın kapanışıdır ve S23'te
                  tamamlanır; S24'te DEĞİŞMEZ — böylece çiftte tek değişken kalır.
FİNAL TİPİ:       TWIST + tohum bilgi · tohum %12 (S3) · kapanış bütçesi
                  %8-12 = S22-S24 (3 sahne) · sonda cevapsız kalan soru SAYISI 1
                  ve o soru TEMA düzeyindedir, OLAY düzeyinde değil
                  [SERI_VE_KANAL §1 bağımsız izlenebilirlik kilidi]
```

## 2. 🗺️ SIRALAMA — 25 sahne, sırayla

> Her satır dört bütçeyi birden taşır:
> `KARAKTER_VE_DUYGU §6` (göz · tepki planı · el · yürüyüş · eşya) ·
> `KURGU_RITMI §2` örüntü kırıcı (**ardışık iki sahne aynı ölçek + palet +
> ses dokusunda OLAMAZ**) · `ACI_YAYI §3` güvenli bant · B5 bağı.
>
> **Palet kodları:** `N` çıplak alüminyum beyaz-gri (nötr) · `Y` soğuk yıldız
> beyazı baskın · `T` anodize turuncu aksan baskın (kalça sırası) · `K` mutlak
> siyah gölge baskın.  **Ses dokuları:** `ç` temas vuruşu + uzun çan kuyruğu ·
> `s` gövdeden iletilen sürtünme (bant/eldiven) · `n` yalnız suit içi nefes+fan.

| S | başlık | olay (tek cümle) | vuruş | B5 satırı | kurulum | lens · mesafe · ölçek · açı tipi | palet | ses | ⭐VİRAL |
|---|---|---|---|---|:--:|---|:--:|:--:|:--:|
| S0 | BIRAKILAN ŞEY | Eldiven açılır, cıvata düşerken yana kayar ve dikişte yatan iki cıvatanın yanına iner. | açılış imajı · HOOK | İSTEK (iş sürüyor) | **A** | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | K | ç | — |
| S1 | SAYIM BAŞLAR | Yapının içinden tek bir vuruş geçer; yıldız akışı hızlanır; kadın adımını atar ve adım erken, sert iner. | **KATALİZÖR** (≤15 s) | İSTEK · başlangıç amacı | **C** | 50 mm · 4,0 m · MS · göz hizası | N | ç | — |
| S2 | SARKMA · ilk ölçü | Oturttuğu açıklığa bakar: sabit pimin altında kablo bir parmak genişliği sarkıyor. | kurulum · SAYAÇ kurulur | ENGEL kurulur | **G** | 50 mm · 2,5 m · MCU · alçak 0,4 m, hafif yukarı | N | n | — |
| S3 | TEK KLİPS | Pime **tek** klips takar; kolayca oturur; kalça sırası dolu. | tartışma · ⭐**TOHUM %12** | MUHATAP kurulur (kendi geçmiş kararı) | **A**↩3 | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | T | s | — |
| S4 | TERS YÖN | Makarayı almaya geri yürür: aynı adım süzülür, geç iner, diz katlanmaz. | tartışma | ENGEL (kural keşfi ①) | **C**↩3 | 50 mm · 4,0 m · MS · göz hizası | Y | n | — |
| S5 | SARKMA · ikinci ölçü | Aynı pim, aynı kadraj: sarkma bir tık derin. | tartışma · SAYAÇ | ENGEL | **G**↩3 | 50 mm · 2,5 m · MCU · alçak, hafif yukarı | N | n | — |
| S6 | KABURGA GÖZÜ | **İNSANSIZ** · kaburga aralığından yıldız alanı; süpürme kadrajın yarısını geçer; kaburga kenarı kımıldamaz. | **viral ara #1** | — (ortam) | **F** | 50 mm · 6,0 m · MWS · göz hizası | Y | n | — |
| S7 | MAKARA SÖKÜLÜR | Geniş: makarayı yuvasından ayırır ve güverteye indirir — buradan sonrası ileri. | **eşik / plan değişikliği** | İSTEK · geri dönüş zorlaşır | **B** | 32 mm · 14,0 m · WS · göz hizası | N | s | — |
| S8 | İLK YÜK | Eldiven makro: iki eldiven banda kapanır, bant güverteden bir el yükselir ve orada durur. | tırmanış | ENGEL · efor ① | **E** | 85 mm · 1,2 m · CU · tepeden-aşağı 50° | T | s | — |
| S9 | AYNI YÜK, DEVAM | **KÜME** — aynı kadrajın son karesinden devam: bant pime doğru gelir, omuz hattı düşer ve düşük kalır. | tırmanış | efor ② (birikme) | **E**↩1 | 85 mm · 1,2 m · CU · tepeden-aşağı 50° | T | s | — |
| S10 | OTURMAYAN KLİPS | **BAŞARISIZ DENEME** — ters yönde hafif yürüyerek klipsi oturtmaya çalışır; bant pimin üstünden kalkar, oturmaz; durur. | tırmanış | ENGEL (kural keşfi ②) | **B**↩3 | 32 mm · 14,0 m · WS · göz hizası | N | s | — |
| S11 | ÜSTÜMDEKİ GÜVERTE | Başını kaldırır: aynı güverte tepesinde kapanıyor ve üstünde kimse durmuyor. | **viral ara #2** | MUHATAP (ortam) | **D** | 50 mm · 3,0 m · EWS (yukarı) · alttan-yukarı 60° | Y | n | ⭐ |
| S12 | YARIYI GEÇMEK | Omuz üstü: pim dizisi ileri uzanıyor — halkanın yarısı geçildi, geri dönmek ileri gitmekten uzun. | **orta nokta / dönüşü olmayan nokta** | ENGEL kilitlenir | **H** | 35 mm · 1,5 m · MCU · göz hizası (omuz üstü) | N | ç | — |
| S13 | ⭐OVERVIEW | Durur; halka başının üstünde kapanır; kendi hattı bütün eğri boyunca uzanıyor. Hiçbir şey hareket etmez. | orta nokta · **BÖLÜM 2 açılışı** | MUHATAP | **D**↩2 | 50 mm · 3,0 m · EWS (yukarı) · alttan-yukarı 60° | Y | n | — |
| S14 | SARKMA · üçüncü ölçü | Aynı pim: sarkma artık pimin gölgesini geçmiş. | SAYAÇ | ENGEL büyür | **G** | 50 mm · 2,5 m · MCU · alçak, hafif yukarı | N | n | — |
| S15 | TEK KLİPS YETMİYOR | Pime klips takar; klips oturuyor ama bant altından kıpırdıyor. Kalça sırasına bakar. | tırmanış | MUHATAP (S3'ün cevabı belirir) | **A** | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | T | s | — |
| S16 | YALNIZ ÖLÇÜ | **İNSANSIZ** · yalnız pim ve kablo: sarkma pimin gölgesinin dışına taşmış. | **viral ara #3** · SAYAÇ | ENGEL | **G**↩2 | 50 mm · 2,5 m · MCU · alçak, hafif yukarı | K | n | — |
| S17 | HALKA KAPANIYOR | KAPANIŞ PİMİ kadrajda: üstünde S3'te takılan tek klips duruyor, son açıklığın bandı öbür yandan yaklaşıyor. Sırada sayılı klips kaldı. | **umut-önce-düşüş** | İSTEK bitmek üzere | **A**↩2 | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | T | s | — |
| S18 | KAYAN BANT | Bant eldivenden kayar ve güverteye iner; kalça sırasından iki klips düşüp yana savrulur. | **Her Şeyin Kaybı** | BEDEL'in sebebi | **E** | 85 mm · 1,2 m · CU · tepeden-aşağı 50° | T | s | — |
| S19 | TOPLAMAK | **KÜME** — aynı kadrajdan devam: düşen iki klipsi toplar; ikisi de aynı yere, cıvata yığınının yanına inmiş. | kayıp sürüyor | ENGEL · kural kanıtı ③ | **E**↩1 | 85 mm · 1,2 m · CU · tepeden-aşağı 50° | K | s | — |
| S20 | AĞIR YÖN | ⭐**TERCİH ÇAPASI** — bakış, tereddüt, sonra dönüş: ters yöne değil, dönüşle AYNI yöne yürür. | **merkezî seçim** | ⭐SEÇİM | **C**↩(16) | 50 mm · 4,0 m · MS · göz hizası | Y | ç | ⭐ |
| S21 | SIRA BOŞALIYOR | Son açıklığa ikişer klips takar; kalça sırası boşalır. | **DORUK a** | ⭐**BEDEL** | **E**↩2 | 85 mm · 1,2 m · CU · tepeden-aşağı 50° | T | s | — |
| S22 | SON KLİPS | Son klips **aynı kapanış pimine** oturur — halka kapanır; yapının çanı bir kez vurur ve kuyruğu sönerken kesilir. | **DORUK b** | BEDEL ödendi | **A** | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | N | ç | — |
| S23 | İKİNCİ BIRAKMA | **KÜME** — aynı kadraj: eldiven açılır, son cıvata aynı yere iner ama **daha erken**; yığın büyümüş. | SAYAÇ kapanır | İSTEK tamamlandı | **A**↩1 | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | K | ç | — |
| S24 | AÇIK KALAN | **İNSANSIZ** · aynı kadraj, kimse yok: kapanış piminde İKİ klips — S22'de takılan yenisi kapalı, **S3'te takılan eskisi AÇIK** ve bandı pimden kalkmış. Held frame. | **kapanış imajı · TWIST** | MUHATAP cevap verir | **A**↩1 | 85 mm · 0,7 m · ECU · tepeden-aşağı 35° | K | n | — |

### 2b. ⭐VİRAL KAPISI — `SENARYO_VE_VIRAL_KAMERA` §2.4 (iki satır zorunlu)

```
⭐VİRAL S11 · YÜZ:    vizör ardında kaş kaldırma (AU2) — 1,5 saniyede yerleşir
                      ve sahne sonuna kadar geri inmez
              HAREKET: yıldız alanı üst güvertenin arkasında süpürür + kendi
                      kablosunun çizgisi eğri boyunca kadrajı geçer
⭐VİRAL S20 · YÜZ:    çene kasılması + bakışın yönü değişmesi (AU4) — 2,0 saniye
              HAREKET: adım dönüş yönüne kilitlenirken yıldız alanı kadrajın
                      çoğunu geçer; gövde tek karede iki farklı ağırlıkta okunur
⛔ Diğer sahneler ETİKETSİZDİR ve bu meşrudur — ölçütsüz etiket meşru değildir.
⛔ Viral ara sahne SAYISI 4 (§2.3 kartı): S6 · S11 · S16 · S20.
   İkisi (S6 · S16) insansız SAF ÖLÇÜ sahnesidir ve ⭐VİRAL etiketi TAŞIMAZ
   (yüz kanalı fiziksel olarak kapalı → kapı düşer).
⛔ OVERVIEW (S13) viral ara DEĞİLDİR ve filmde TAM BİR ADETTİR [UZAY_SENARYO §8].
   ⚠️ §8'in "karakter karenin 1/20'si" maddesi iç mekânda uygulanamaz ve bu
   YAZILIYOR [D74 · YERÇEKİMİ S68 emsali]: karşıtlık figür-kare değil
   **GÖVDE ↔ KAPANAN HALKA** olarak kurulur. Diğer dört madde birebir:
   hareketsizlik · sessizlik · geriye bakış · tam bir sahne harcanması.
```

### 2c. 🧍 İNSAN ŞERİDİ — ve neden bu filmde ÖLÇÜYOR

```
ŞERİT (25 hane):  1111110111111111011111110
                  insansız yuvalar: S6 · S16 · S24
⭐ [D163] THE OPEN CIRCUIT'te 25/25 sahne insanlıydı → şerit SABİT çıktı ve
  SIRA eksenini ölçemedi; S2↔S3 yer değiştirmesi görülmedi. Bu filmde üç
  insansız yuva şeride BİLGİ koyuyor ve şerit yeniden bir ölçüm aracı oluyor.
⛔ Yine de sıra ekseninin İKİNCİ çapası kuruluyor (replik yok, o kanal kapalı):
  her sahnenin SAYAÇ DEĞERİ SPEC'e yazılır ve sıra ondan da okunur.
⛔ KART 10: S6 · S16 · S24'ün `NEGATIVE:` bloğu TEK pozitif `Style:` satırına
  iner — insansız sahne + uzun yokluk listesi YAPISAL RED profilidir
  (red defteri vaka 2; çözüm ilk denemede GEÇTİ).
```

## 3. 📐 ARDIŞIK ÇİFT DENETİMİ — mekanik, göz kararı değil

> `ACI_YAYI §3` güvenli bant: ardışık her çift **≥1 ölçek kademesi VE ≥45° azimut**.
> ⛔ Bölüm SINIRI da ardışık bir çifttir (son sahne ↔ ilk sahne).
> Ölçek merdiveni: `ECU < CU < MCU < MS < MWS < WS < EWS`
> Kurulum azimutları (halka çevresine göre): A 000° · B 045° · C 090° · E 135° ·
> F 180° · D 225° · G 270° · H 315°

| çift | ölçek kademesi | azimut farkı | bant içi | şok mu · gerekçe |
|---|:--:|:--:|:--:|---|
| S0→S1 | ECU→MS · 3 | 90° | ✅ | — |
| S1→S2 | MS→MCU · 1 | 180° | ✅ | — |
| S2→S3 | MCU→ECU · 2 | 90° | ✅ | — |
| S3→S4 | ECU→MS · 3 | 90° | ✅ | — |
| S4→S5 | MS→MCU · 1 | 180° | ✅ | — |
| S5→S6 | MCU→MWS · 2 | 90° | ✅ | — |
| S6→S7 | MWS→WS · 1 | 135° | ✅ | — |
| S7→S8 | WS→CU · 4 | 90° | ✅ | — |
| S8→S9 | 0 | 0° | ⛔ **KÜME 1** | bilinçli · tek vuruş sürüyor · birebir kopya + "continues the previous clip from its exact last frame" |
| S9→S10 | CU→WS · 4 | 90° | ✅ | — |
| S10→S11 | WS→EWS · 1 | 180° | ✅ | — |
| S11→S12 | EWS→MCU · 4 | 90° | ✅ | — |
| **S12→S13** | MCU→EWS · 4 | 90° | ✅ | ⭐ **BÖLÜM SINIRI** · köprü tipi **EYLEM SÜREKLİLİĞİ** [5_FAZ]: S12'de başlayan baş kaldırma S13'te tamamlanır |
| S13→S14 | EWS→MCU · 4 | 45° | ✅ | tam sınırda — kabul |
| S14→S15 | MCU→ECU · 2 | 90° | ✅ | — |
| S15→S16 | ECU→MCU · 2 | 90° | ✅ | — |
| S16→S17 | MCU→ECU · 2 | 90° | ✅ | — |
| S17→S18 | ECU→CU · 1 | 135° | ✅ | — |
| S18→S19 | 0 | 0° | ⛔ **KÜME 2** | bilinçli · tek vuruş sürüyor · birebir kopya |
| S19→S20 | CU→MS · 2 | 45° | ✅ | — |
| S20→S21 | MS→CU · 2 | 45° | ✅ | — |
| S21→S22 | CU→ECU · 1 | 135° | ✅ | — |
| S22→S23 | 0 | 0° | ⛔ **KÜME 3** | bilinçli · doruk sonrası tek nefes; S22-S23-S24 üçlü küme, film tek kadraja kapanıyor |
| S23→S24 | 0 | 0° | ⛔ **KÜME 3 devam** | bilinçli · KAFİYE'nin ikinci ucu; insan kadrajdan çıkar, kadraj değişmez |

```
ARDIŞIK ÇİFT:     20 / 24 bant içi · 4 çift KÜME (bilinçli, gerekçeli)
BİLİNÇLİ ŞOK:     0   — ölçek/azimut şoku kullanılmadı; kümelerin hepsi
                  DEVAM'dır, şok değildir
AÇI TİPİ SAYISI:  4 ≥3 ✅  (tepeden-aşağı A·E · göz hizası C·F·B·H ·
                  alçak-hafif yukarı G · alttan-yukarı D)
                  ⛔ KAMERA_ACISI §2: üç kurulumun üçü de aynı yönden bakıyorsa
                  çeşitlilik yoktur, yalnız mesafe değişir — bu film dört ayrı
                  yönden bakıyor
KURULUM SAYISI:   8 (A·B·C·D·E·F·G·H)
                  ⚠️ Tek satır gerekçe [D74]: §3.7'de güverte düzeyindeki bir
                  mercek halkanın ancak ÜÇTE BİRİNİ görür; sekiz kurulum
                  halkanın çevresine dağıtılan sekiz azimut demektir ve
                  kadraj menzili her biri için ayrıca hesaplanmıştır.
```

## 4. ⭐ KURULUM İSKELETİ — PLAN'a taşınacak satır

```
İSKELET: A C G A C G F B E E B D H D G A G A E E C E A A A

KÜME:   3 ≥2   →  S8-S9 (E) · S18-S19 (E) · S22-S23-S24 (A, üçlü)
DÖNÜŞ:  12 / 25 = %48 ≥%40  →  S3 S4 S5 S9 S10 S13 S16 S17 S19 S21 S23 S24
        (dönüş = kaynağından ≤3 sahne sonra gelen tekrar)
KURULUM DAĞILIMI: A×7 · E×5 · G×4 · C×3 · B×2 · D×2 · F×1 · H×1
```

⛔ Aynı harfin kamera metni **BİREBİR kopyalanır** ve işaret satırını taşır —
model iskeleti görmez, metni görür [`ACI_YAYI` §7 ⑥]:
```
dönüş → "— the same position, height and lens as Scene N."
küme  → "continues the previous clip from its exact last frame — the same
         position, height and lens as Scene N."
```
⛔ Bu satır PLAN'a yazılmazsa `prompt_kontrol` ⑩④ kapısı **hiç koşmaz.**
⛔ Ve ⑨ KADRAJ merceği SETUP STRING'i bu satıra karşı okur [D184]; satır yoksa
mercek koşamaz.

## 5. 🎙️ REPLİK YERLEŞİMİ

```
⛔ BU FİLMDE REPLİK YOKTUR — 0 insan · 0 makine · 0 telsiz.
   Bu bir TASARIM KARARI ve bir SIFIR KİLİDİDİR [D156]: SPEC'te ayrı ölçüm
   satırı olur, sessizce varsayılmaz.
   → ④ HİKAYE rubriğinde Diyalog **N/A**'dır, düşük puan DEĞİL; payda 9'a iner
     ("Silence is not a gap" — Kaleida emsali). Bu satır SPEC'e yazılır ki
     mercek sessizliği kusur sanmasın.
   → ③ SES için TESLİM DURUMU **B (sessiz, tasarımlı)**: Atıf · Sentetik ·
     Ses Kimliği · Aktarım · Sıra Alma sütunları `—`; yalnız Ambiyans · SFX ·
     Miks · Müzik puanlanır (THE STILL SWARM emsali).
   → ⑩ OYUNCULUK merceği TETİKLENİR: tetikleyicisi "replik 0 olan her film".
```

## 6. 🔢 METİNSİZ SAYAÇ — ekran/kadran/gösterge kullanmadan

```
KANAL 1 — SARKMA DERİNLİĞİ (sabit pime göre) · birincil sayaç
  S2 4,46 cm → S5 5,19 → S14 7,72 → S16 8,35 → S23 10,75 → S24 11,12
  MONOTONİK: ✅  ·  ölçüm aracı: pimin kendisi (yapısal, işaretsiz)
  ⭐ ÖLÇEĞİN İKİ UCU HER KAREDE BİRLİKTE [Third Dune 10/10 kalıbı]: pim
    (başlangıç) ve kablo (şimdi) aynı kadrajda, yan yana.
  ⛔ D138: ölçü PROMPT GÖVDESİNE YAZILMAZ; SPEC'in kilit listesinde yaşar.
    Gövde nesne-göreli yazar: "the cable hangs a finger's width below the pin"
    → "…a full hand's width below the pin".

KANAL 2 — YILDIZ ALANI SÜPÜRME HIZI · doğrulayıcı kanal [D78 çift kanal]
  S0 3,00 RPM → S12 4,00 → S24 5,00     (18 → 24 → 30 °/s)
  MONOTONİK: ✅
  ⛔ DERECE YAZILMAZ [D138] — SÜREYLE yazılır:
    başta  "the starfield sweeps half way around the frame during the shot"
    ortada "…two thirds of the way around…"
    sonda  "…most of the way around…"

ÜÇÜNCÜ KANIT (sayaç DEĞİL — iki vuruşluk kural kanıtı)
  Bırakılan cismin DÜŞÜŞ SÜRESİ: S0 = 1,69 s → S23 = 1,03 s
  Yana sapma: 0,52 m ve **DÖNME HIZINDAN BAĞIMSIZ SABİT**
    (sapma = R·(d/r₀ − arctan(d/r₀)); ω sadeleşir)
  ⭐ Yani cisim HER SEFERİNDE AYNI YERE, ama DAHA ERKEN iner.
  ⛔ JEST TEKRARI KURALI [UZAY_SENARYO §13]: bu jest filmde TAM İKİ KEZ
    kullanılır — 1. kez KEŞİF (S0), 2. kez DOĞRULAMA ve YENİ BİLGİ taşır
    (S23: aynı yer, daha erken). ÜÇÜNCÜSÜ ÖLÜ SAHNEDİR ve yazılmadı.

⛔ Cihaz ekranı / sayaç / yazı ile sayılan şey bu depoda arıza üretiyor:
  13 filmin 11'inde sayaç `N/A` okundu; DÖRT filmde sayaç PLANLIYDI ve
  ekranda hiç okunmadı [D50 · D78 · D134].
⛔ SAYAÇ TERSİNMESİ diğer bütün skorları EZER — geri giden sayaç bir
  devamlılık kayması değil ÖNERMENİN ÇÖKÜŞÜDÜR [T2 verdict]. Yukarıdaki iki
  kanalın 25 sahnelik değer dizisi SPEC'e sayı sayı yazılır.
```

## 7. ⛔ ÜRETİM SIRASI — dramatik sıra DEĞİLDİR [D168]

```
ÜRETİM SIRASI:
  0. REFERANS PAKETİ (RA · RB · RC · RD) — sayfalar ONAYLANMADAN hiçbir
     sahne üretilmez [KAPI 0]
  1. DORUK            S22   (son klips oturur · çan bir kez vurup kesilir)
  2. MERKEZÎ SEÇİM    S20   (tercih çapası · ⭐VİRAL)
  3. KAPANIŞ İMAJI    S24   (KAFİYE'nin ikinci ucu · FİNAL VURUŞ KANITI)
  4. S0                     (HOOK · novumun en ucuz kanıtı)
  5. BEDEL            S21
  6. kalanı: S1 · S2 · S3 · S4 · S5 · S6 · S7 · S8 · S9 · S10 · S11 · S12 ·
             S13 · S14 · S15 · S16 · S17 · S18 · S19 · S23
```

Üretim her an durabilir (red · kota · motor · gün). Baştan üretirsen elde hep
KURULUM kalır ve kurulum kendini savunamaz. **THE SINKING STAKE tam böyle
durdu: 25 sahnenin 14'ü üretildi, eksik 11'i ARDIŞIK ve filmin SONUYDU** —
merkezî seçim, doruk ve twist hiç üretilmedi. **THE OPEN CIRCUIT'te üretim
sırası PLANA YAZILMIŞTI ve yine iki sahne teslime girmedi; biri doruktu**
[D168 2. vaka: liste PLANI bağlar, TESLİMİ bağlamaz] → bu yüzden aşağıdaki
teslim kapısı ayrıca yazılır.

```
⛔ İPTAL KAPISI 1 — S0: bırakılan cıvata DÜZ düşüyorsa (yana inmiyorsa)
   film ÜRETİLMEZ. Bu, novumun en ucuz ve tek kareyle sınanabilir kanıtıdır;
   tutmuyorsa geri kalan 24 sahnenin hiçbiri kuralı taşıyamaz.
   [Emsal: THE IRON SLOPE'ta serbest parça sabit 0,15 m/s süzüldü, kilit
   3. saniyede 9,7 m istiyordu — novum ekrana HİÇ gelmedi ve T4 2,6 aldı.]

⛔ İPTAL KAPISI 2 — S22: son klips pime OTURMUYORSA ya da çan vuruşu
   kesilmiyorsa film ÜRETİLMEZ. Doruk yoksa film yoktur.

⛔ TESLİM KAPISI [D188]: plan sahne sayısı (25) = makara klip sayısı.
   Eşit değilse hiçbir mercek koşulmaz, hiçbir T satırı yazılmaz.
```

---

## ✅ KAPI

```
☑ 25 sahnenin 25'i tabloda, olay sütunu dolu
☑ ardışık çiftlerin hepsi denetlendi (20/24 bant içi · 4 çift bilinçli KÜME,
  gerekçeli) · bölüm sınırı S12↔S13 ayrıca denetlendi ve köprü tipi yazıldı
☑ kurulum iskeleti yazıldı · KÜME 3 (≥2) · DÖNÜŞ %48 (≥%40) · açı tipi 4 (≥3)
☑ metinsiz sayaç iki kanaldan kuruldu, ikisi de monotonik, değerleri sayıyla
☑ üretim sırası + iki iptal kapısı + teslim kapısı yazıldı
→ beşi de ✅ ise 04_UYARI_NOTLARI.md yazılabilir
```
