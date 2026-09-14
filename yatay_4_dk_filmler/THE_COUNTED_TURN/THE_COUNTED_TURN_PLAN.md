# 🎬 THE_COUNTED_TURN — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 IMAGE PROMPT` / `### 🎥 VIDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.
>
> Analizin tamamı `00_ANALIZ/` altındadır ve bu plan onun ÇIKTISIDIR —
> burada yeniden düşünülmez, TAŞINIR.

```
FORMAT:        yatay 3-5 dk                              → KILAVUZ_REHBERI §2.3
ORTAM:         §3.7 VAKUM + DÖNME YERÇEKİMİ (dönen halkanın iç güvertesi)
               §3.1'in alt kartı — oradaki her kural geçerli
TÜR:           bilimkurgu · sert (hard) dal              → §4.1
MİMARİ KUTUP:  DISCOVERY (UZAY_SENARYO §5) — depoda hiç denenmedi.
               Halka İNŞA HÂLİNDE: çıplak, temiz, hassas, parlak metal.
KLİP SÜRESİ:   ⬜ ____ s  ⛔ ÜRETİMDEN ÖNCE ARAÇTAN ÖLÇÜLECEK [D124]:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
               PLANLAMA IZGARASI 10,0 s. Ölçüm saparsa bu dosyadaki BÜTÜN
               zaman kodları yeniden hesaplanır.
SAHNE SAYISI:  25        RUNTIME: 249,0 s = 9 s + 24 × 10 s = 4:09
BÖLÜM:         2 — BOLUM_1 S0-S12 (13 sahne) · BOLUM_2 S13-S24 (12 sahne)
LOGLINE:       Dönen bir halkanın iç güvertesinde tek başına kablo hattı çeken
               bir rigger, halka kilit devrine çıkarken işini bitirmek için en
               ağır yönde yürümek zorunda kalır — ve bitirdiğinde, en hafifken
               taktığı ilk klipsin artık tutmadığını görür.
```

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE
      Makinenin saydığı şey ile insanın saydığı şey aynı işin iki ayrı
      ölçüsüdür; biri bittiğinde öteki hâlâ sürüyordur.
      ⛔ Etiket TEK KELİMEDİR: `sayac.sh` TEMA DAĞILIMI'nda boşluk içeren
        değeri ELER (`grep -vE ' '`). "İNSAN-MAKİNE SINIRI" yazılsaydı film
        tema sayımında hiç görünmezdi.

MOTİF SAHNELERİ: S3 · S11 · S20 · S24
      S3  NESNE    — sabit pim (makinenin değişmeyen işareti) ile kalça
                     sırası (insanın azalan sayısı) aynı karede
      S11 KAMERA   — üst güverteye bakış: makinenin geometrisi kapalı ve
                     tam; insan onun içinde tek
      S20 KİNESİK  — akıcı organik adımın staccato kilitlenmeye dönüşü
      S24 İFŞA     — tema-final kilidi [TEMA §6]: insan-makine GÖRSEL BİR
                     İFŞA ister; ifşasız düz bitiş izlenme süresini dibe
                     vurur. İfşa: açık kalan tek klips.
⛔ IŞIK KANALI BİLİNÇLİ OLARAK KULLANILMADI [D74]: §5 matrisi "vizör paraziti
   ile eşzamanlı ışık titremesi" diyor; vizör durum değişimi yasak [D37·D57] ve
   §3.7'de ışık dönmeyle DEĞİŞMEZ. Titremeyen ışık burada temanın kendisidir —
   makinenin dünyası kıpırdamaz, değişimi yalnız insan bedeni kaydeder.
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Bu halkada ağırlık YÖNE bağlıdır — dönüşle aynı yöne
                     yürüyen ağırlaşır, ters yöne yürüyen hafifler; ve
                     bırakılan hiçbir şey düz düşmez, hep aynı yana iner.
NOVUM TİPİ:          FİZİKSEL YASA (§1'in birinci tercihi)
                     ⛔ Yasa İCAT EDİLMEDİ [06 §4⑤]: §3.7'nin KENDİ kuralı,
                       olay örgüsünü ZORUNLU KILACAK biçimde kullanıldı.
                       Mecburiyet: son açıklığı oturtmak için dönüşle AYNI
                       yönde — en ağır yönde — yürümek zorunludur; ters yönde
                       hafiflemiş gövde bandı pime oturtacak ağırlığı üretemez.
NOVUM TAŞIYICISI:    asılı bant ucu × bırakılan cıvata → ikisi aynı karede ve
                     birbirine PARALEL DEĞİL
TEK KARE (§4①):      ✅ "Asılı duran bant ucu ile düşmekte olan cıvata aynı
                     karede ve ikisi paralel değil."
                     ⛔ Cümle taşıyıcı nesnelerin ADINI içeriyor [D157].
KİNETİK BAĞIMSIZLIK: ✅ Üç kanaldan, replik/dış ses/ekran metni OLMADAN:
                     (a) bırakılan cıvatanın yana inmesi (S0 · S23)
                     (b) aynı gövdenin iki yönde iki farklı ağırlıkta
                         görünmesi (S1 ↔ S4 · S10 ↔ S20)
                     (c) sarkan bandın SARKMA DERİNLİĞİ (S2·S5·S14·S16·S23)
BAŞLIK ŞEMASI:       ✅ "THE COUNTED TURN" — 3 kelime · depo kalıbı THE + iki
                     kelime · izleyiciye nereye bakacağını söylüyor
NOVUM SINIRI [D183]: Dönme ekseni boyunca hiçbir cisim ağırlık kazanmaz;
                     eksene DİK her cisim kazanır. Bırakılan cisim ASLA düz
                     düşmez ve ASLA yukarı gitmez. Hiçbir karede sıfır-g YOK.
```

## 🧭 B5 — HİKÂYE OMURGASI (kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Halkanın son kablo hattını, halka KİLİT DEVRİNE ulaşmadan önce
              pimlere oturtmak. Film başlamasa da süren, bitirilebilir,
              adımları sayılabilir bir İŞ.
   □ ENGEL:   Halka her turda hızlanıyor; artan ağırlık bandın sarkmasını
              derinleştiriyor ve hafifken oturtulmuş TEK klipsli açıklıklar
              bu ağırlıkta tutmuyor. Üstelik son açıklık ancak en ağır yönde
              yürünerek oturtulabiliyor.
   □ BEDEL:   Kalça sırasındaki DÖRT klipsin dördünü de son açıklığa harcar
              (pim başına iki); sıra boşalır ve ilk pime dönecek klips kalmaz.
              · **S21**   ⭐ sahne numarası taşıyor
   □ MUHATAP: kendi geçmiş kararı — S3'te, halka hâlâ hafifken, her pime TEK
              klips takmış olması. Sonunda ona cevap veren şey odur.
              (Antagonist kanalı 1 ORTAM + kanal 4 KENDİ SEÇİMİ;
               kanal 2 AI sesi SEÇİLMEDİ çünkü replik yok — UZAY_SENARYO §10)
B5b □ AYRILIK: — · tek insan (yalnız iki insanlı planda zorunlu)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  0. REFERANS PAKETİ (RA·RB·RC·RD) — ONAYSIZ sayfanın sahnesi üretilmez [KAPI 0]
  1. DORUK            S22
  2. MERKEZÎ SEÇİM    S20
  3. KAPANIŞ İMAJI    S24
  4. S0               (HOOK · novumun en ucuz kanıtı)
  5. BEDEL            S21
  6. kalanı: S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11 S12 S13 S14 S15 S16 S17 S18 S19 S23

⛔ İPTAL KAPISI 1 — S0: bırakılan cıvata DÜZ düşüyorsa film ÜRETİLMEZ.
⛔ İPTAL KAPISI 2 — S22: son klips pime oturmuyorsa ya da çan vuruşu
   kesilmiyorsa film ÜRETİLMEZ. Doruk yoksa film yoktur.
⛔ TESLİM KAPISI [D188]: plan sahne sayısı (25) = makara klip sayısı.
   Eşit değilse hiçbir mercek koşulmaz, hiçbir T satırı yazılmaz.
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
⛔ TETİKLENMEZ — bu film YATAY 16:9'dur. Satırlar gerekmediği için değil,
   FORMAT DIŞI olduğu için boştur; gerekmediğini yazmak da kapının parçasıdır.
   B5 OMURGASI (yukarıda) her formatta zorunludur ve yazılmıştır.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

> ⚠️ §2'de 3-5 dk için ayrı eşleme tablosu yok. Vuruşlar §2.2'nin YÜZDE
> bantları 249,0 s'ye uygulanarak ve `SAVAS_SENARYO` §14 Hauge tablosunun
> 25 sahne sütunuyla çapraz doğrulanarak yerleştirildi (`00_ANALIZ/03` §1).

| # | vuruş | % | saniye | sahne | boşsa gerekçe |
|---|---|:--:|:--:|:--:|---|
| 1 | Açılış imajı | %0-4 | 0-9 | S0 | — |
| 2 | Kurulum | %0-12 | 0-29 | S0-S2 | — |
| 3 | Katalizör | %4-8 | 9-19 | S1 | ilk 15 s'yi geçmiyor |
| 4 | Tartışma | %12-24 | 29-59 | S3-S5 | atlanmadı |
| 5 | Eşik / plan değişikliği | %25 | 59-69 | S7 | Hauge S6, ±1 kabul |
| 6 | Orta nokta / dönüşü olmayan nokta | %50 | 119-139 | S12-S13 | bölüm sınırı |
| 7 | Umut-önce-düşüş | %68 | 169-179 | S17 | — |
| 8 | Her Şeyin Kaybı | %75 | 179-189 | S18 | Hauge S19, ±1 kabul |
| 9 | Merkezî seçim | %80 | 199-209 | S20 | — |
| 10 | Doruk | %84-92 | 209-229 | S21-S22 | — |
| 11 | Kapanış imajı | %100 | 239-249 | S24 | — |

```
VİRAL ARA SAHNE: 4 (§2.3 kartı) — S6 · S11 · S16 · S20
⭐VİRAL ETİKETİ:  S11 · S20 (YÜZ + HAREKET satırları yazıldı · §2.4 kapısı)
                  S6 ve S16 İNSANSIZDIR → yüz kanalı fiziksel olarak kapalı,
                  etiket DÜŞER ve etiketsiz kalır (ölçütsüz etiket meşru değil)
OVERVIEW:         S13 — filmde TAM BİR ADET [UZAY_SENARYO §8]
                  ⛔ D74: §8'in "karakter karenin 1/20'si" maddesi iç mekânda
                  uygulanamaz; karşıtlık GÖVDE ↔ KAPANAN HALKA olarak kuruldu
                  (YERÇEKİMİ S68 emsali). Diğer dört madde birebir.
KESİLEMEZ SAHNELER: S6 · S11 · S13 · S16 · S20 · S21 · S22 · S24
                  ⛔ Beş ayrı filmde QA kesme listesinin BİRİNCİ SIRASI planın
                  kesilemez viral arasına düştü [D94 örüntüsü] — bu satır
                  QA_SPEC'e de yazılır.
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       KURAL İHLALİ — bir YER değil bir DURUM gösteriliyor.
                 ⭐ Ölçülmüş gerekçe: Ring Walker açılışı devasa halka
                 gökyüzüydü → Kanca 5/10; Inversion açılışı havalanan bir
                 çakıl taşıydı → 6/10, serinin ölçülmüş en iyi kancası.
S0 SORUSU:       "Neden yana düştü?"
S1 İKİNCİ BİLGİ: Düşüş bir kez olmadı — dikişte zaten iki cıvata var. Ve
                 yapının içinden tek bir vuruş geçtikten sonra arka plandaki
                 yıldızlar daha hızlı akıyor.
İLK 2 SN SESİ:   Eldivenin güverte dikişine değmesi — yapı bir ÇANDIR: temas
                 milisaniyelerde halkayı dolaşıp çok yansımalı uzun bir
                 kuyrukla döner. Vakumda duyulan tek şey TEMASTIR.
AÇILIŞ↔KAPANIŞ:  KAFİYE (3-5 dk bandının çifti · loop DEĞİL)
                 Değişen TEK değişken: kadrajın merkezindeki KAPANIŞ PİMİ —
                 S0'da BOŞ, S24'te üstünde İKİ klips ve biri AÇIK.
FİNAL TİPİ:      TWIST + tohum bilgi · tohum %12 (S3) · kapanış bütçesi
                 %8-12 = S22-S24 · sonda cevapsız kalan soru SAYISI 1 ve o
                 soru TEMA düzeyindedir, OLAY düzeyinde değil.
```

---

## 🗺️ SAHNE HARİTASI

| S | başlık | olay | kurulum (lens · mesafe · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|
| S0 | BIRAKILAN ŞEY | Eldiven açılır, cıvata yana kayarak düşer ve dikişteki iki cıvatanın yanına iner | **A** 85 mm · 0,70 m · ECU · tepeden-aşağı 35° | temas + çan kuyruğu | HOOK · açılış imajı |
| S1 | SAYIM BAŞLAR | Yapıdan tek vuruş geçer, yıldız akışı hızlanır, adım erken ve sert iner | **C** 50 mm · 4,00 m · MS · göz hizası | temas + çan | katalizör · başlangıç amacı |
| S2 | SARKMA · ilk ölçü | Sabit pimin altında bant bir parmak genişliği sarkıyor | **G** 50 mm · 2,50 m · MCU · alçak 0,40 m | nefes + fan | SAYAÇ kurulur |
| S3 | TEK KLİPS | Kapanış pimine tek klips takar; kolayca oturur, sıra dolu | **A**↩3 85 mm · 0,70 m · ECU | sürtünme | ⭐TOHUM · Çehov kurulumu |
| S4 | TERS YÖN | Geri yürür: adım süzülür, geç iner, diz katlanmaz | **C**↩3 50 mm · 4,00 m · MS | nefes + fan | kural keşfi ① · yürüyüş bütçesi |
| S5 | SARKMA · ikinci ölçü | Aynı pim, aynı kadraj: sarkma bir tık derin | **G**↩3 50 mm · 2,50 m · MCU | nefes + fan | SAYAÇ · kadraj çifti |
| S6 | KABURGA GÖZÜ | İNSANSIZ · kaburga aralığından yıldız alanı, süpürme kadrajın yarısını geçer | **F** 50 mm · 6,00 m · MWS · göz hizası | nefes yok · yalnız fan | viral ara #1 · ölçek |
| S7 | MAKARA SÖKÜLÜR | Makarayı yuvasından ayırır ve güverteye indirir | **B** 32 mm · 14,00 m · WS · göz hizası | sürtünme | eşik · geri dönüş zorlaşır |
| S8 | İLK YÜK | İki eldiven banda kapanır; bant bir el yükselir ve durur | **E** 85 mm · 1,20 m · CU · tepeden-aşağı 50° | sürtünme | efor ① · el bütçesi |
| S9 | AYNI YÜK, DEVAM | KÜME · bant pime doğru gelir, omuz hattı düşer ve düşük kalır | **E**↩1 (küme S8) | sürtünme | efor ② birikme |
| S10 | OTURMAYAN KLİPS | Ters yönde klipsi oturtmaya çalışır; bant pimin üstünden kalkar | **B**↩3 32 mm · 14,00 m · WS | sürtünme | ⭐BAŞARISIZ DENEME · tepki çapası |
| S11 | ÜSTÜMDEKİ GÜVERTE | Başını kaldırır: aynı güverte tepede kapanıyor, üstünde kimse yok | **D** 50 mm · 3,00 m · EWS · alttan-yukarı 60° | nefes + fan | viral ara #2 · ⭐VİRAL · göz bütçesi |
| S12 | YARIYI GEÇMEK | Omuz üstü: halkanın yarısı geçildi, geri dönmek ileri gitmekten uzun | **H** 35 mm · 1,50 m · MCU · omuz üstü | temas + çan | dönüşü olmayan nokta |
| S13 | OVERVIEW | Durur; halka başının üstünde kapanır, kendi hattı bütün eğri boyunca | **D**↩2 50 mm · 3,00 m · EWS | nefes + fan | BÖLÜM 2 açılışı · tek Overview |
| S14 | SARKMA · üçüncü ölçü | Aynı pim: sarkma pimin gölgesini geçmiş | **G** 50 mm · 2,50 m · MCU | nefes + fan | SAYAÇ |
| S15 | TEK KLİPS YETMİYOR | Klips oturur ama bant altından kıpırdar; bakış kalça sırasına gider | **A** 85 mm · 0,70 m · ECU | sürtünme | MUHATAP belirir · tepki çapası |
| S16 | YALNIZ ÖLÇÜ | İNSANSIZ · sarkma pimin gölgesinin dışına taşmış | **G**↩2 50 mm · 2,50 m · MCU | nefes yok · yalnız fan | viral ara #3 · SAYAÇ |
| S17 | HALKA KAPANIYOR | Kapanış piminde S3'ün tek klipsi; son açıklığın bandı öbür yandan yaklaşıyor | **A**↩2 85 mm · 0,70 m · ECU | sürtünme | umut-önce-düşüş |
| S18 | KAYAN BANT | Bant eldivenden kayar; kalça sırasından iki klips düşüp yana savrulur | **E** 85 mm · 1,20 m · CU | sürtünme | HER ŞEYİN KAYBI |
| S19 | TOPLAMAK | KÜME · iki klipsi toplar; ikisi de aynı yere, yığının yanına inmiş | **E**↩1 (küme S18) | sürtünme | kural kanıtı ③ |
| S20 | AĞIR YÖN | Bakış, tereddüt, dönüş: dönüşle AYNI yöne yürür | **C** 50 mm · 4,00 m · MS | temas + çan | ⭐MERKEZÎ SEÇİM · ⭐VİRAL |
| S21 | SIRA BOŞALIYOR | Son açıklığa dört klipsi de takar; kalça sırası boşalır | **E**↩2 85 mm · 1,20 m · CU | sürtünme | ⭐BEDEL · DORUK a |
| S22 | SON KLİPS | Son klips kapanış pimine oturur; çan bir kez vurur ve kesilir | **A** 85 mm · 0,70 m · ECU | temas → mutlak sessizlik | ⭐DORUK b · müziksiz sahne |
| S23 | İKİNCİ BIRAKMA | KÜME · son cıvata aynı yere ama daha erken iner; yığın büyümüş | **A**↩1 (küme S22) | temas + çan | SAYAÇ kapanır |
| S24 | AÇIK KALAN | İNSANSIZ · pimde iki klips: yenisi kapalı, S3'ünki AÇIK. Held frame | **A**↩1 (küme S23) | nefes yok · yalnız fan | KAPANIŞ İMAJI · TWIST |

```
AÇI TİPİ SAYISI: 4 ≥3
                 tepeden-aşağı (A · E) · göz hizası (C · F · B · H) ·
                 alçak-hafif yukarı (G) · alttan-yukarı (D)
KURULUM SAYISI:  8 (A B C D E F G H)
                 ⚠️ Tek satır gerekçe [D74]: §3.7'de güverte düzeyindeki bir
                 mercek halkanın ancak ÜÇTE BİRİNİ görür; sekiz kurulum
                 halkanın çevresine dağıtılan sekiz azimuttur ve kadraj
                 menzili her biri için ayrıca hesaplandı (00_ANALIZ/05).
KURULUM İSKELETİ: A C G A C G F B E E B D H D G A G A E E C E A A A
                 KÜME  3 (≥2): S8-S9 · S18-S19 · S22-S23-S24
                 DÖNÜŞ 12/25 = %48 (≥%40): S3 S4 S5 S9 S10 S13 S16 S17 S19
                                            S21 S23 S24
                 AZİMUTLAR: A 000° · B 045° · C 090° · E 135° · F 180° ·
                            D 225° · G 270° · H 315°
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR
                   kopyalanır + işaret satırını taşır (ACI_YAYI §7 ⑥):
                     dönüş → "— the same position, height and lens as Scene N."
                     küme  → "continues the previous clip from its exact last
                              frame — the same position, height and lens as Scene N."
BÖLÜM KESİĞİ:    S12 ile S13 arasında — ⛔ bölüm sınırı da ardışık bir ÇİFTTİR:
                 MCU→EWS 4 kademe · 90° azimut ✅ bant içi.
                 KÖPRÜ TİPİ: EYLEM SÜREKLİLİĞİ — S12'de başlayan baş kaldırma
                 S13'te tamamlanır [5_FAZ_MIMARISI köprü tipleri].
İNSAN ŞERİDİ:    1111110111111111011111110   (insansız: S6 · S16 · S24)
```

---

## 🎙️ REPLİK TABLOSU

```
⛔ REPLİK YOKTUR — 0 insan · 0 makine · 0 telsiz.
   Bu bir TASARIM KARARI ve bir SIFIR KİLİDİDİR [D156]: SPEC'te ayrı ölçüm
   satırı olur, sessizce varsayılmaz.
   → ④ HİKAYE rubriğinde Diyalog N/A'dır, düşük puan DEĞİL; payda 9'a iner
     ("Silence is not a gap" — Kaleida emsali).
   → ③ SES için TESLİM DURUMU B (sessiz, tasarımlı).
   → ⑩ OYUNCULUK merceği TETİKLENİR (tetikleyicisi "replik 0 olan her film").
BEDENLEŞTİRME:  yok — kadrajda okunan konuşan ağız 0 kare.
```

---

## 📖 BIBLE'LAR

> Karakter çapa bloğu **kelimesi kelimesine** sabittir ve her IMAGE promptuna
> tam yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).
> ⛔ KİMLİK YIĞINI PROMPT GÖVDESİNE GİRMEZ [red defteri vaka 15]: kesin boy,
> ten rengi, saç, yaş ve milliyet bu planın hiçbir yerinde yazılmaz; yüz
> kimliği YALNIZ referans paketi RA sayfasında ve onun SEED'inde yaşar.

### 👤 Character Bible — prompt çapa bloğu (25/25 görsel promptta BİREBİR)

> ⚠️ **prompt_kontrol bu bloğu bir prompt sanar ve iki uyarı verir** (negatif
> çekirdek imzası eksik). Uyarı DOĞRU değil YAPISALDIR: bu dosyada prompt
> YOKTUR, blok yalnız kopyalanacak çapadır. Aynı aile: bölüm dosyalarındaki
> "NOVUM TAŞIYICISI satırı yok" uyarısı — satır PLAN'da yaşar ve klasör modu
> ikisini de kapatır (`📁 FİLM KLASÖRÜ · ✅ GO`). [THE_BLUE_DRIFT emsali · §2.0]

```
Exactly one human. A single figure in a matte pale-grey pressure suit works alone on
the deck. The suit is one continuous smooth panel from collar to hip, unbroken,
carrying nothing on the back. The helmet has a flat rectangular front pane, a little
wider than a spread hand and about two thirds as tall, set in a visible brushed metal
rim — not a dome, not a bubble, no seamless shell. The glass is optically clear with
zero tint and zero mirror coating, and the face is fully readable through it at every
head angle. Photorealistic skin pores, sweat and fatigue are retained. The gloves are
the same matte pale grey with raised knuckle ridges and a stitched cuff seam. A short
row of anodised orange clips rides flat on the right hip, each about the length of a
thumb, standing up from the rail in a single line. The suit has no back-mounted unit:
the back is one continuous smooth panel from collar to hip, unbroken, carrying
nothing. The visor is optically clear glass with zero tint, zero mirror coating and
zero reflection of the environment; the face is fully readable through it in every
frame, at every head angle.
```

```
ROL:            halka montaj riggeri · tek kişi · film boyunca yalnız
KİMLİK ÇAPASI:  RA referans sayfası + seed (⛔ prompt gövdesinde tarif YOK)
AYIRT ETME:     ikinci gövde olmadığı için ayırt etme sorunu YOK; süreklilik
                RENKLE değil MALZEMEYLE taşınır — mat dokuma giysi ↔ parlak
                işlenmiş alüminyum güverte
KALÇA SIRASI:   sayılabilir · S0 12 → S15 6 → S17 4 → S18 4 (ikisi düşer) →
                S19 4 (toplanır) → S21 0
                ⭐ Son açıklık tam DÖRT klips ister (pim başına iki, iki pim):
                  düşen ikisi toplanmasaydı iş bitmezdi
```

### 🌍 World Bible

```
YER:            inşa hâlindeki bir halka istasyonun iç güvertesi
İÇ YARIÇAP:     R = 12,00 m       ÇEVRE: 75,40 m       GÜVERTE ENİ: 3,20 m
PİM DİZİSİ:     paslanmaz pimler, 8 cm yüksek, güverte dikişine kaynaklı,
                3,00 m aralıkla — çevrede 25 açıklık
KABLO:          mat koyu gri DOKUMA BANT, 12 cm eninde
                ⛔ `fabric` · `cloth` KELİMELERİ HİÇ KULLANILMAZ [D59 · D153] —
                  karşılık: "woven webbing band"
KABURGA GÖZÜ:   iç kaplaması henüz yapılmamış 2,50 m'lik açıklık; ötesinde
                yalnız yıldız alanı
OKLÜZYON:       YOK — güverte içbükeydir, önü ve arkası yukarı kıvrılır ve
                başın üstünde kapanır. "Tavan" alttan görülen AYNI güvertedir.
                ⛔ Kadrajın üst bandında her zaman ikinci bir güverte görünür
                  ve model oraya İKİNCİ İNSAN koymaya yatkındır:
                  "no one is standing on it" 25/25 promptta ZORUNLU.
KAMERA MENZİLİ: güverte düzeyindeki mercek halkanın ancak ÜÇTE BİRİNİ görür
SOSYOLOJİ:      TEK NESNE ile ima edilir [UZAY_SENARYO §4]: kalça sırasındaki
                klipslerin sayısı — kimse ona fazladan klips vermedi
```

### 🎥 Camera Bible

```
SENSÖR DİLİ:    Super 35 field of view (§9 varsayılanı)
                ⛔ Large format YAZILMAZ: karakterin karenin küçük bir parçası
                  olduğu ve arkadaki yapının OKUNMASI gereken kadrajda aşırı
                  sığ alan derinliği anlatıyı yok eder; ayrıca YouTube
                  kodlayıcısı geniş bokeh'i çamurlu kodlar.
LENS KARAKTERİ: spherical lens rendering, circular bokeh, NO lens flare
                ⛔ Anamorfik yatay parlama vakumda hem yasak hem fiziksel
                  olarak yanlış (§11).
KAMERA:         25/25 TAM LOCKOFF — pan 0 · tilt 0 · dolly 0 · zoom 0 ·
                handheld 0 · klip içi kesme 0
KURULUMLAR:     A 85 mm · 0,70 m · yükseklik 1,10 m · tepeden-aşağı 35° · az 000°
                B 32 mm · 14,00 m · yükseklik 1,55 m · göz hizası · az 045°
                C 50 mm · 4,00 m · yükseklik 1,45 m · göz hizası · az 090°
                D 50 mm · 3,00 m · yükseklik 0,35 m · alttan-yukarı 60° · az 225°
                E 85 mm · 1,20 m · yükseklik 0,95 m · tepeden-aşağı 50° · az 135°
                F 50 mm · 6,00 m · yükseklik 1,50 m · göz hizası · az 180°
                G 50 mm · 2,50 m · yükseklik 0,40 m · alçak, hafif yukarı · az 270°
                H 35 mm · 1,50 m · yükseklik 1,60 m · omuz üstü · az 315°
NEGATİF EKİ:    focus breathing negatifi netlik geçişi olan her sahnede
                rolling shutter / jello negatifi YALNIZ hızlı hareket varsa
                (bu filmde HİÇBİR sahnede yok — eklenmez, yer kaplar)
```

### 💡 Lighting Bible

```
KAYNAK:         TEK kaynak — dönme eksenine paralel gelen yıldız ışığı,
                güverteyi YALAYARAK aydınlatır. Renk sıcaklığı 5.800 K, beyaz.
DOLGU:          YOK. Metal yapıda model ikincil yansıma üretmeye çok yatkındır;
                pozitif cümle her prompta yazılır: "no fill light reaches the
                shadow side; the shadowed metal stays completely black."
GÖLGE:          MUTLAK SİYAH, jilet keskin.
⭐ IŞIK TAKVİMİ YAPISAL SABİTTİR: geometri halkanın dönüşüyle DEĞİŞMEZ, yani
  25 klibin ışık sürekliliği FİZİKLE garanti altındadır [§3.7 · kartın bedava
  kazancı]. Anahtar ışık yönü 25/25 sahnede aynı saat konumundadır.
  ⛔ D193: yazılan takvim ÖLÇÜLMEZSE tutmaz — `olcum_kapisi.sh` IŞIK TAKVİMİ
    İZİ ve ⑪ IŞIK merceği bu satırı okuyacak.
PARLAKLIK DİLİ: highlight roll-off (§15) — "highlights roll off smoothly and
                retain texture instead of clipping to flat white"
                ⛔ `glowing · ethereal · radiant · shimmering · cinematic
                  lighting` 0 geçiş [D29 · D33]
```

### ⚙️ Physics Bible

```
DÖNME:          T = 20,0 s → 12,0 s     (3,00 → 5,00 RPM)
                ω = 0,3142 → 0,5236 rad/s   ·   ω(n) = 0,3142 + 0,008725·n
AĞIRLIK:        a = ω²R → 1,18 → 3,29 m/s²  (0,121 g → 0,335 g)
                ⚠️ §3.7 tasarım ölçütü 1-2 RPM'dir; bu film 3-5 RPM bandındadır
                  ve bandın tamamı ölçütün üstündedir. Bu bir kusur değil,
                  filmin KONUSUDUR — ama plana yazılır: BU ORTAMDA KİMSE
                  ADAPTE OLMUŞ SAYILMAZ. (THE HEAVY SIDE emsali: 4,6-7,5 RPM)
YÖN KURALI:     a = (v_çember ± u)²/R — dönüşle aynı yöne yürüyen AĞIRLAŞIR,
                ters yöne yürüyen HAFİFLER. Aynı güverte, aynı adım, iki farklı
                ağırlık: süreklilik hatası DEĞİL, ortamın kuralı.
BIRAKMA:        h = 1,40 m'den bırakılan cisim: r₀ = 10,60 m · d = 5,625 m
                SAPMA = 0,52 m ve DÖNME HIZINDAN BAĞIMSIZ SABİT
                DÜŞÜŞ SÜRESİ = 1,69 s (S0) → 1,03 s (S23)
                ⭐ Aynı yere, daha erken. Sayaç SÜREDİR, mesafe değil.
SARKMA:         sarkma ∝ a → 4,00 cm (n=0) → 11,12 cm (n=24), MONOTONİK
SÜPÜRME:        RPM × 6 °/s → 18 → 30 °/s · 10 s'lik planda 180° → 300°
                ⛔ DERECE PROMPTA YAZILMAZ [D138] — SÜREYLE yazılır
CORIOLIS:       merkeze doğru tırmanan gövdeye 2ωv biner; yalpalama YUKARI
                ÇIKTIKÇA BÜYÜR. (Bu filmde tırmanma sahnesi YOK — kural
                yazılıdır ama tetiklenmez.)
TOZ:            0 kare. Rüzgâr · alev · kıvılcım · egzoz: 0 kare.
SES:            dışarıda ses yok; yapı bir ÇANDIR (alüminyumda 5.100 m/s) —
                her temas milisaniyelerde çevreyi dolaşıp çok yansımalı uzun
                bir kuyrukla döner. Duyulan her şey TEMASTIR.
D23:            ELENİR — hiçbir kare sıfır-g değil.
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5 negatif çekirdek TAM METİN

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly one human character — no duplicates, no clones, no second
person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every
surface keeps visible texture. Photorealistic skin pores, sweat, scars and
fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed
skin, no face morphing, identical bone structure throughout. Equipment and
clothing identical to the description — no drift, no gear appearing or
disappearing mid-shot. Dirt and wear staining stays fixed and never shifts.
No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not
on the deck, the rail, the pins or any surface in the frame.
Nothing in this world has been measured, labelled, marked out or
annotated by anyone: no scale marks, no graduation ticks, no survey
markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. All hand-surface
contacts keep a clear structural boundary — no merging, no phasing, no extra
fingers, rigid-body collision throughout. All particles obey the stated
gravity with continuous physical momentum — never hovering, never frozen,
never swirling or flowing like liquid. Environment static and stable — no
melting terrain, no warping topology, no swimming texture. No Unreal Engine
look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm
film grain.
```

**Kasklı her sahnede ayrıca [DERS 79 · pozitif hâl]:**

```
The suit has NO back-mounted unit: the back of the suit is one continuous
smooth panel from collar to hip, unbroken, carrying nothing. The visor is
optically clear glass with zero tint, zero mirror coating and zero reflection
of the environment; her face is fully readable through it in every frame, at
every head angle.
```

**§3.7'nin bu filme eklediği negatif satırlar:**

```
No dust, no smoke, no exhaust, no sparks, no flame anywhere. The star field
is made of individual separate points — no star trails, no streaks, no
smearing. No fill light reaches the shadow side; the shadowed metal stays
completely black. On the deck curving overhead, no one is standing on it and
nothing is moving on it. No bare skin is visible anywhere: not above the
collar, not at the hands or wrists, not at the cuffs.
```

**İnsansız sahnelerde (S6 · S16 · S24) — `NEGATIVE:` bloğu YAZILMAZ:**

```
⛔ KART 10 · red defteri vaka 2: insansız sahne + uzun yokluk listesi
  YAPISAL RED profilidir ("having a hard time fulfilling your request").
  Çözüm ilk denemede GEÇTİ: NEGATIVE bloğu tamamen kaldırılır ve tek
  pozitif Style: satırına indirilir. Boş kadraj VARLIK olarak tarif edilir.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. Her tetiklenen risk kartı buraya bir SAYI bırakır.

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| insan sayısı | tam 1 (insansız 3 sahne) | KART 4 | 25/25 |
| üst güvertede insan | 0 | KART 4 · §3.7 | 25/25 |
| replik | 0 (insan 0 · makine 0 · telsiz 0) | KART 7 | 25/25 |
| ekran metni | 0,0 saniye (kart DÂHİL) | KART 5 | kurgu |
| klip içi kesme | 0 | KART 11 | 25/25 |
| vizör durum değişimi | 0 kare | KART 3 | 25/25 |
| vizör ön penceresi | 24 × 16 cm, düz, çerçeveli — ⛔ SAYI yalnız burada ve RA sayfasında; prompt GÖVDESİNDE nesne-göreli yazılır [D138] | KART 3 · D146 | 25/25 |
| kask kubbesi | 0 (`dome/bubble/seamless` 0 geçiş) | KART 3 · D146 | 25/25 |
| sırt ünitesi | 0 · pozitif yüzey cümlesi | KART 3 · D79/D139 | 25/25, özellikle S12 |
| toz / kıvılcım / alev | 0 kare | KART 6 | 25/25 |
| yıldız izi (trail) | 0 | KART 6 · SINKING STAKE | S6 · S11 · S13 · S16 |
| halka iç yarıçapı | 12,00 m | KART 13 | tüm geniş kadrajlar |
| pim aralığı | 3,00 m · 25 açıklık | KART 13 | tüm A/G kadrajları |
| dönme periyodu | 20,0 s → 12,0 s | KART 6b · ⑥ FİZİK | 25/25 |
| devir | 3,00 → 5,00 RPM | KART 6b | 25/25 |
| yerel ağırlık | 1,18 → 3,29 m/s² | ⑥ FİZİK | 25/25 |
| bırakma sapması | 0,52 m (SABİT) | ⑥ FİZİK | S0 · S18 · S19 · S23 |
| düşüş süresi | 1,69 s → 1,03 s | ⑥ FİZİK · D127 | S0 · S23 |
| sarkma | 4,00 → 11,12 cm, monotonik | KART 5 · ② SAYAÇ | S2 S5 S14 S16 S23 S24 |
| kalça sırası | 12 → 6 → 4 → 0 | KART 5 · D78 | S0 S15 S17 S21 |
| kapanış pimindeki klips | 0 → 1 → 2 (biri açık) | D141 | S0 S3 S22 S24 |
| çan vuruşu (doruk) | 1 | D183 · D192 | S22 |
| mutlak sessizlik | 2,0 s · 226,0-228,0 s | D180 | S22 |
| lockoff | 25/25 | KART 8 | 25/25 |
| kurulum sayısı | 8 · açı tipi 4 | ACI_YAYI | 25/25 |
| KÜME / DÖNÜŞ | 3 / %48 | ACI_YAYI §4b | iskelet satırı |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D174 | Yön ekran-yönü kelimesine değil İKİ NESNEYE bağlanır | 25/25 · yıldız alanı + güverte dikişi |
| D127 | İvme yazılmaz; hareket SÜRE ile yazılır | S0 · S18 · S19 · S23 |
| D50 · D78 | Sayaç metinsizdir ve ölçeğin İKİ UCU her karede birlikte | S2 S5 S14 S16 S23 S24 |
| D169 · D175 | Her efor sahnesinde ≥2 beden kanalı, ELDİVEN yüzeyinde | S8 S9 S18 S19 S21 |
| D172 | Sarkma her zaman ARKADA; eller ona ulaşmaz | S2 S5 S14 S16 |
| D157 | Novum taşıyıcısı ≥1/10 kadraj, rakip olay yok | S0 · S23 |
| D158 | Başarısız deneme + bedelden sonra seçim | S10 · S20 |
| D141 | Final vuruş kanıtı sayılabilir: AÇIK KLİPS · 1 adet · 244,0 s | S24 |
| D138 | Metin yasağının KAPSAMI; ölçü gövdede değil SPEC'te | 25/25 |
| D59 · D153 | `float/hang/hover` yalnız negatifte · `fabric/cloth` 0 geçiş | 25/25 |
| D69 · D77 | Biniş/iniş/eşikten geçiş hareketi 0 sahne | sahne haritası |
| D145 · D126 | HORIZON LOCK + en büyük arka plan nesnesi adlandırılır | S6 S7 S10 S11 S13 S16 |
| D183 · D192 | 1 numaralı risk SAYIYLA korunur, sıfatla değil | S22 · fizik bible |
| D193 | Işık takvimi yazılır VE ölçülür | 25/25 · SPEC E |
| D156 | Planın SIFIRLARI ayrı ölçüm satırı olur | sayısal kilit listesi |
| D168 · D188 | Üretim sırası + teslim kapısı | B5 bloğu |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S20 — filmin en ağır çekişinin hazırlığı; gövdeye değen
                     kuvvet (KART 12 tetikleyicisi)
NÖTR TARİFİ:         işlev + malzeme + sayı. Örnek biçim:
                     "both gloves close on the woven band; the band comes off
                      the deck by the width of a hand and holds there; the
                      shoulder line drops a little and stays down"
⛔ 0 GEÇİŞ: strain · injury · hurt · wound · danger · trapped · crushed · pain
  — ve YASAK CÜMLESİ DE YAZILMAZ [D123: yasak, yasakladığı kavramı prompta sokar]
⛔ KOMPOZİSYON: S20 kadrajı MS tutuldu (50 mm · 4,00 m · göz hizası), makro
  DEĞİL. Bütün el makrolarında kadrajda daima korkuluk ya da pim görünür —
  "yan yana iki ön kol + tepeden makro + yüzsüz izolasyon" bileşimi kurulmaz
  [red defteri vaka 13: kelimeler temizken KADRAJ reddedildi].
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Kimlik yığını prompt gövdesinden çıkarıldı (boy/ten/saç/yaş) | Yüz üzerinden kurulacak yakınlık zayıfladı | **temassız gövde tepkisi**: omuz hattı, duruş ve eldiven yüzeyi duyguyu taşır; yüz kimliği RA sayfası + seed ile korunur |
| Yaralanma ve tehlike sözlüğü 0 geçişe indirildi | "zorlanma" kelimesiyle anlatılacak yoğunluk gitti | **malzeme sonucu**: eldiven boğum sırtlarının derinleşmesi, manşet dikişinin gerilmesi, bandın güverteden bir el yükselip orada DURMASI |
| Makro izolasyon kadrajları kaldırıldı (her el planında çevre var) | En yakın plandaki mahremiyet ve klostrofobi azaldı | **kütle-hız**: yakınlık lensle değil AĞIRLIKLA kuruldu — aynı jest iki yönde iki farklı hızda iner |
| İkinci figür hiç açılmadı | İkili dinamik ve diyalog imkânı gitti | **alet tepkisi**: muhatap ikinci insan değil kendi geçmiş kararıdır ve o karar S24'te kadrajda CEVAP VERİR |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
⛔ Karakterin ÖZEL ADI hiçbir yerde geçmez [D34] ve prompt gövdesinde hiçbir
  iç etiket (faz adı, kilit adı, sahne adı) bulunmaz [D45 · D155].
```

---

## 📦 REFERANS PAKETİ — KAPI 0

```
KARAR: YAZILIR. `REFERANS_PAKETI_KILAVUZU` §1'in altı tetikleyicisinden BEŞİ
       doğru: T1 (kask/vizör/basınç giysisi) · T2 (biçim kilidi metinle
       tutulmayan varlık: pim+klips) · T3 (oranı sözle yazılamayan nesne:
       içbükey güverte) · T5 (tekrar eden insan dışı olay: yana iniş, sarkma) ·
       T6 (tekrar tekrar dönen varlık: halkanın kendisi). T4 (insan dışı
       canlı) YOK.
SAYFALAR: RA karakter+giysi+vizör · RB pim+klips birimi · RC bant ve makara ·
       RD halka kesiti + kaburga gözü + ölçek şahidi
⛔ Sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği hiçbir sahne
  üretilmez [D168]. Üretim sırasının İLK halkası budur.
```


---

## ✅ PLAN ÖNCESİ KONTROL — `03_PLAN_ONCESI_KONTROL_LISTESI.md` 14 maddesi

> Maliyeti sıfır, ~20 dakika. On dördün on biri gerçek filmlerde GERÇEKTEN
> oldu ve hepsi üretimden SONRA bulundu. Koşu: 09.09.2026.

```
A1 · YASAK ↔ ANLATIM ÇELİŞKİSİ  ⭐ EN PAHALI HATA
   Planda "no readable text" satırı VAR mı → EVET, 25/25 promptta.
   Aynı dosyada bir ekranın/göstergenin İÇERİĞİ tarif ediliyor mu → HAYIR.
   ✅ ÇELİŞKİ YOK — ve bu tesadüf değil TASARIM: filmin sayacı bir EKRAN
   DEĞİL, fiziksel bir sarkmadır. KART 5 (ekran/sayaç/metin) tetiklendi ama
   metin kanalı tasarımla sıfırlandı: kadranda, göstergede, ekranda okunan
   HİÇBİR değer yok. Model "yasağı seçip anlatımı öldürme" ikilemine hiç
   sokulmuyor.

A2 · SAHNE SAYISI TUTUYOR MU
   Başlıkta yazan: 25 · dosyadaki sahne bloğu: 13 + 12 = 25          ✅
   Numara atlaması: S0…S24 kesintisiz, atlama yok                    ✅
   "Scene N of 25": 1'den 25'e eksiksiz ve X doğru                   ✅

A3 · SÜRE TUTUYOR MU
   25 × 10,0 s = 250,0 s · hook kırpması −1,0 s → 249,0 s = 4:09     ✅
   ⛔ HOOK KIRPILMAZSA süre 250,0 s olur ve SPEC KAPI ① düşer. Bu satır
     TRIM BUDGET olarak SPEC B bloğunda yazılı; THE PAYLOAD ve THE FROST
     LINE'da hook kırpılmadı ve ikisinde de aynı 1 saniye kaydı.

A4 · YASAKLI SAHNE TİPİ VAR MI  [D77 — ders plana ulaşmıyor]
   · araç/kapak/airlock BİNİŞ-İNİŞ hareketi      → 0 sahne. KARAR SATIRI:
     "Biniş · iniş · eşikten geçiş hareketi 25 sahnenin hiçbirinde kadraja
      alınmadı — D69 ① gereği. Karakter halkanın içinde başlar ve orada
      biter; hiçbir eşik geçilmez."
   · tek ışıklı loş iç mekâna GİRİŞ              → 0 sahne (giriş yok)
   · aynalı-yansıtıcı yüzey önünde tek karakter  → 0 sahne; vizör optik
     berrak ve YANSIMASIZ, güverte mat işlenmiş alüminyum
   · novum'u TÜRETİLMİŞ optik fenomen taşıyor    → HAYIR [D73]. Taşıyıcı
     KATI CİSİM ve GEOMETRİDİR (düşen cıvata, sarkan bant), gölge/yansıma/
     kostik/parlama deseni DEĞİL.
   · novum'u bir YOKLUK taşıyor                  → HAYIR [D76]. Taşıyıcı
     VARLIKTIR. Yalnız FİNAL vuruşu bir yokluk içerir (açık klips) ve o da
     iki VAR OLAN nesnenin karşılaştırmasıdır (kapalı klips ↔ açık klips),
     "olmayan bir şey" değil.
   · jenerik/başlık kartı ya da kapak çıktısı    → 0 sahne. Kapak AYRI
     üretilir ve kurguya GİRMEZ [D34 · D70 · D72 — on üç vakalık zincir].
   ✅ Yasaklı tip YOK; altı satırın altısı da kayda geçti.

A5 · FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI  [D192]
   Riskin ADI: DÖNME YÖNÜNÜN YUVARLANMASI (KART 5 · göz kapısı ④ · D174)
   POZİTİF BİÇİMİ SAYI TAŞIYOR MU → EVET:
     R 12,00 m · T 20,0 → 12,0 s · 3,00 → 5,00 RPM · süpürme 18 → 30 °/s ·
     sapma 0,52 m (sabit) · düşüş 1,69 → 1,03 s · sarkma 4,00 → 11,12 cm
   SPEC'in göz kapısı o sayıyı ölçülebilir cümleyle tekrarlıyor mu → EVET
     (GÖZ ④ · GÖZ ⑤ · GÖZ ⑥ + E bloğu KAPI ①).
   ✅ Yalnız NEGATIVE cümlesine yaslanmıyor. THE OPEN CIRCUIT riskini adıyla
   ilan etmiş ama SIFATLA korumuştu ("tek, ince, düz, sönümlü") ve doruk
   şimşek geldi; aynı planda SAYIYLA yazılan her şey tuttu.

B1 · DORUK ANI BİR SAHNENİN İÇİNDE Mİ
   Doruk: S22 · 219,0-229,0 s. Video promptunda TARİF EDİLİYOR:
   "the last clip comes over both and closes in one movement" (3s beat).
   İki sahnenin ARASINA düşmüyor.                                    ✅
   ⭐ İkinci doruk beat'i S21 (BEDEL) ve o da kendi sahnesinin içinde.

B1b · KATMANLI DÜNYA İSE IŞIK TAKVİMİ VAR MI
   Film bir eksende ilerliyor mu → EVET, çevresel bir eksende (halkanın
   çevresi) ve KART 6b tetiklendi.
   Işık takvimi TABLO hâlinde yazılı mı → EVET, ve değeri TEK: ışık dönme
   eksenine paralel olduğu için 25/25 sahnede AYNI saat konumunda.
   Monotonik mi → ⭐ MONOTONİK DEĞİL, SABİT. Ve bu §3.7'nin bedava
   kazancıdır: ışık sürekliliği FİZİKLE garanti altındadır.
   ⛔ [D193] Yazılan takvim ÖLÇÜLMEZSE tutmaz → SPEC E bloğu KAPI ⑤.   ✅

B2 · BEDELLİ SEÇİM VAR MI
   Karakter bir ŞEY seçiyor mu → EVET, S20: ters yön (hafif, kolay, ama
   oturtamaz) ↔ aynı yön (ağır, pahalı, oturtur). Bakış → tereddüt → dönüş.
   Seçtiğinde neyi KAYBEDİYOR → kalça sırasındaki son dört klipsi; ilk pime
   dönecek klips kalmıyor.
   Kaybı hangi sahnede GÖRÜLÜYOR → **S21** (sıra boşalır, çıplak ray kalır)
   ve sonucu **S24**'te (ilk pimin klipsi açık).                      ✅
   ⭐ Bu madde deponun ölçülmüş en dirençli darboğazıdır: yedi hikâye
   satırının yedisinde de KARAKTER ≤4 ve sebebi tek — bedelli seçim yok.

B3 · TEMA HANGİ SAHNEDE EKRANA ÇIKIYOR
   TEMA satırı var mı → EVET: İNSAN-MAKİNE SINIRI (tek kelime etiketi)
   Novum kelimesi geçmeden tek cümleyle söylenebiliyor mu → EVET (yukarıda)
   MOTİF SAHNELERİ: **S3 · S11 · S20 · S24** — dörtten fazlası zaten var
   B2 ile çapraz okuma: bedelli seçimin sahnesi (S20) bu listede Mİ → EVET ✅
   ⛔ Kaleida Crash kaydı: "bedel yok → tema dekoratif kalıyor". Burada bedel
     var, sahne numarası var ve motif sahnelerinden biri bedelin sahnesi.

B4 · AÇI YAYI YAZILDI MI
   SAHNE-KURULUM DİZİSİ yazılı mı → EVET:
     A C G A C G F B E E B D H D G A G A E E C E A A A
   Ardışık HER çift güvenli bandı tutuyor mu → 20/24 bant içi; 4 çift
     bilinçli KÜME (devam) ve gerekçeleri `00_ANALIZ/03` §3'te tek tek yazılı
   Kurulum SAYISI bandın içinde mi → 8 kurulum · bant üstündeyse gerekçe
     yazıldı [D74]: §3.7'de güverte düzeyindeki mercek halkanın ancak üçte
     birini görür; sekiz kurulum sekiz azimuttur.
   AÇI TİPİ sayısı ≥3 mü → **4** (high angle · eye level · low angle ·
     over-the-shoulder) — `prompt_kontrol` sözlüğüyle DOĞRULANDI          ✅
   KÜME ≥2 → 3 · DÖNÜŞ ≥%40 → %48                                      ✅

B5 · İSTEK · ENGEL · BEDEL · MUHATAP
   İSTEK:   son kablo hattını kilit devrinden önce pimlere oturtmak
            (film başlamasa da süren bir İŞ; "anlamak/görmek" DEĞİL)     ✅
   ENGEL:   artan ağırlık — hafifken oturtulmuş tek klipsler tutmuyor ve
            son açıklık ancak en ağır yönde yürünerek oturtulabiliyor     ✅
   BEDEL:   dört klipsin dördü de son açıklığa gider · **S21**           ✅
   MUHATAP: kendi geçmiş kararı (S3'te her pime TEK klips)               ✅
   ⛔ ASIL KAPI BEDEL'dir ve sahne numarası taşıyor.

B5b · AYRILIK
   Tek insanlı plan → madde TETİKLENMEZ. Gerekmediğini yazmak da kapının
   parçasıdır: bu filmde ikinci insan YOKTUR ve KART 4 tasarımla en düşük
   seviyede tutulmuştur.                                                 ✅

B5c · ÜRETİM SIRASI  [D168]
   Yazılı mı → EVET (B5 bloğunda):
     referans paketi → DORUK S22 → merkezî seçim S20 → kapanış S24 → S0 →
     BEDEL S21 → kalanı
   ⛔ VE TESLİM KAPISI AYRICA YAZILDI [D188]: liste PLANI bağlar, TESLİMİ
     bağlamaz — THE OPEN CIRCUIT'te sıra plana yazılmıştı ve iki sahne yine
     teslime girmedi, biri doruktu. Kapı: plan 25 = makara klip sayısı.  ✅

B6 · POLİTİKA SATIRI ve ANLAM MALİYETİ
   EN RED-RİSKLİ KARE yazılı mı → EVET, S20 (+ ikinci yüzey: kimlik yığını)
   NÖTR TARİF yazılı mı → EVET
   ANLAM MALİYETİ TABLOSU dolu mu → EVET, dört satır ve dördünün de TELAFİ
   sütunu dolu (temassız gövde tepkisi · malzeme sonucu · kütle-hız ·
   alet tepkisi).                                                        ✅
   ⛔ TELAFİ sütunu boşsa önlem alınmamıştır, film KISALTILMIŞTIR.
```

```
SONUÇ: 14 maddenin 14'ü koşuldu · 0 açık madde.
       Tetiklenmeyen iki madde (B5b) gerekçesiyle yazıldı.
       prompt_kontrol.py KLASÖR MODU: ✅ GO · 0 BLOCK (09.09.2026)
```

---

## 📌 BİLİNÇLİ SAPMALAR — hepsi tek satır gerekçeli [D74]

```
① VİDEO PROMPT UZUNLUĞU bandın üstünde (~2.800-3.400; bant 2.000-2.600).
   Aritmetik: negatif çekirdek tek başına 1.641 karakter. Tavan ~4.300 ve
   hiçbir prompt ona yaklaşmıyor. Kısaltma seçeneği çekirdeği kesmekti.
② IMAGE PROMPT UZUNLUĞU 2.000-5.100. Image bandı ölçülmedi ve betiğin kendi
   başlık yorumu bunu GÖZLEM sayıyor; depoda 4.577-5.644 karakterlik image
   promptları üretildi ve reddedilmedi.
③ ASL EĞRİSİ DÜZ — sabit 10 s ızgara. Gerekçe SPEC B bloğunda.
④ KURULUM SAYISI 8. Gerekçe: §3.7'de mercek halkanın üçte birini görür.
⑤ OVERVIEW'IN "1/20 ÖLÇEK" MADDESİ uygulanmadı; karşıtlık GÖVDE ↔ KAPANAN
   HALKA olarak kuruldu (YERÇEKİMİ S68 emsali).
⑥ DEVİR BANDI 3-5 RPM, §3.7'nin 1-2 RPM tasarım ölçütünün üstünde. Bu bir
   kusur değil filmin KONUSU — ama plana yazılıyor: bu ortamda kimse adapte
   olmuş sayılmaz.
⑦ TEMA §5 matrisinin IŞIK kanalı (vizör paraziti + ışık titremesi)
   kullanılmadı: vizör durum değişimi yasak [D37·D57] ve §3.7'de ışık
   dönmeyle değişmez.
⑧ İNSANSIZ ÜÇ SAHNEDE (S6 · S16 · S24) NEGATİF ÇEKİRDEK YAZILMADI; tek
   pozitif `Style:` satırına indirildi [red defteri vaka 2 · YAPISAL RED].
```
