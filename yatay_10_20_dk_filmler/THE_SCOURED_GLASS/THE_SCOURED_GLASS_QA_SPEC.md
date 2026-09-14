# 📋 THE SCOURED GLASS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[D117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle **birlikte** bu dosya verilir; koşu **MOD D** olur.
>
> ⛔ **YAPIŞTIRILMAZSA KOŞU YAPILMAMIŞ SAYILIR [D129].** Ham rapor arşive
> düşer, T tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi
> uygulanmaz. "ŞARTLI diye tabloya alayım" yasaktır.
>
> ⚠️ **BU FİLMİN SPEC'İ NEDEN ERKEN YAZILDI.** YERÇEKİMİ'nin dört fazı da
> mod V koştu ve bedeli ölçüldü: FAZ 9'da ⑥ FİZİK **planın kendi ivme
> rampasını** "TWO GRAVITIES 🔴" ilan edip filmin adını taşıyan olayın
> kırpılmasını istedi; THE SINKING STAKE'te ⑥ ve ② **filmin NOVUM'unu**
> en büyük kusur diye puanladı [D166, iki vaka]. Bu dosya tam olarak o
> arızayı önlemek için vardır.
>
> ⛔ **DOSYA ADI `*_QA_SPEC.md` KALIR** — `sayac.sh`, `rubrik_paketle.sh`
> ve `rapor_kontrol.py` üçü de bu deseni arar.

> 🔧 **11.09.2026 — `yeni-film` AKIŞIYLA GÜNCELLENDİ.** Kaynak `00_ANALIZ/`
> (TUR 16 dört derin araştırma + 109 dosya okuma + hasat/konsept/sıralama/
> uyarı/12 sahne çalışması). Değişenler: KURULUM İSKELETİ satırı gerçek
> (A…L, küme 0 — bilinçli sapma) · replik saatleri formülle (S4 34,0/38,0 ·
> S12 112,0-119,0) · ÇAPA ÜÇLÜSÜ + DAVRANIŞ ŞERİDİ blokları · SAYAÇ satırı
> (iğne S7'de sabit) · KEY DIRECTION STRING (güneş sahne başına, D201) ·
> NOVUM "tasarım, kusur değil" beyanı + KURU/ISLAK ayrımı · CAM MERDİVENİ 12
> kademe · ATMOSFER satırı "toz uzun süre asılı" → "toz oturur" (D39) ·
> yeni sıfır kilitleri · KESİLEMEZ listesi · E kapıları 11.09'da yeniden
> kuru-koşuldu. Film ölçeği alanları hâlâ ⬜ (FAZ 2-15 yazılmadı).

> 🔴 **KAPSAM DÜRÜSTLÜĞÜ (07.09.2026):** filmin **1/15'i yazıldı** (FAZ 1).
> A ve B bloklarının film ölçeğindeki alanları ⬜'dir ve faz faz dolar.
> **C BLOĞU ŞİMDİDEN TAMDIR** — çünkü mod V'nin yaptığı hasar oradan
> gelir. E BLOĞU koşulabilir durumdadır. ⛔ Üretim başlarsa QA bu dosyayla
> koşar; A/B'nin boş alanları o fazın `FAZ_nn_QA_PROMPT.md`'sinden gelir.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                        MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)        MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)        MOD V
④ 📖 HİKAYE      → A BLOĞU + FAZ KAPISI               MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri      MOD D
⑦ ⑧ ⑨ ⑩ ⑪ ⑫    → C BLOĞU + FAZ KAPISI

⛔ FAZ KAPISI [D185]: bu bir FİLM değil, filmin bir FAZIDIR.
   Hook · final · tutundurma · kafiye · döngü · terk eğrisi
   FAZ ÖLÇEĞİNDE ÖLÇÜLEMEZ. O hücreler `—` taşır, sayı taşımaz.
   Tek istisna FAZ 1'dir: hook YALNIZ orada ölçülebilir.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE SCOURED GLASS
FORMAT:            yatay 16:9 · 15 faz × 12 sahne × 10,0 s
RUNTIME:           1.800 s (30:00) · title card YOK · screen text lock 0 s
SCENE COUNT:       180
THEME:             BEDEL (plan etiketi, 07.09) · §3 çapası ENTROPİ ("her düzeltme
                   sistemi geri döndürülemez biçimde eskitir") — sahip kararı ⬜
                   [`02_KONSEPT_VE_RISK` §4]
THEME SCENES:      S8 · S11 · S31 · S94 · S140 · S151 · S180   (yedi — ⛔ en az üç ✅)
INTENDED EMOTION:  yorgun direnç — kahramanlık değil, devam etme
ENDING TYPE:       ⬜ (FAZ 15 yazılmadı) — planlanan: KAPALI · son plan S1 kadrajına
                   dönüş (lomboz, cam 12. kademe) · ikinci bedelli seçim S180: lombozu
                   SİLMEZ [D158]
PROTAGONIST:       isimsiz mühendis, kırklarında bir adam
                   ⛔ özel ad hiçbir promptta geçmez [D34]
CENTRAL CHOICE:    FAZ 13 · S151 — paneli siler, vizörü SİLMEZ (tek EVA, bez elde,
                   camdan bir avuç geri çekilir) [`03_SAHNE_SIRALAMASI` §7]
                   (⛔ seçimden SONRAKİ seçim: FAZ 14'te ~kör tırmanış · S180 lomboz) [D158]
DIALOGUE LINES:    ⬜ film toplamı · FAZ 1'de 2 (S4 telsiz ≤8 kl, POST, cevapsız —
                   dinleyen kadrajı YOK, cevap 2,0 s alıcı hışırtısı · S12 günlük 22 kl, OMNI
                   klip içi, cevapsız TASARIM) — FAZ 1'de her replik CEVAPSIZ; cevap
                   gelmemesi ret değil, DEĞİŞ-TOKUŞ tablosunda kayıtlı [D122]
                   register: HUMAN tümü · MACHINE 0 (bu filmde konuşan makine YOK)
SILENT SCENES:     FAZ 1'de 10/12 · film toplamı ⬜
VIRAL INTERSTITIALS: yok
TITLE:             "aşınmış cam" — başlığın verdiği söz NOVUM'un kendisidir:
                   camın aşınması filmin olayıdır, metaforu değil
LIBRARY CONTEXT:   raftaki kardeşler THE_SECOND_SHIP · THE_SLOW_STONE · YERÇEKİMİ
                   ⭐ ayrıştığı yer: bu deponun ilk 30 dakikalık filmi ve
                     ilk 15 fazlı yapısı
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      180 (FAZ 1: 12)
SHOT COUNT:      180 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s SABİT — ⛔ GEREKÇE SATIRI [D74]:
                 ASL bir tercih değil ÜRETİM KISITIDIR. Hat I2V üretir ve
                 klip süresi motorun tavanıdır; kurgu hızıyla gerilim
                 kurulamaz. Bunun bedeli plana yazıldı: gerilim ritimle
                 değil, sayılabilir kaynak + görünür takvim + dramatik
                 ironi ile kurulur [TUR 14 · rapor 4].
                 ⛔ 10,0 s bu hatta HİÇ ÖLÇÜLMEDİ [D124] — test klibi borç
GRID:            sahne başlangıcı(n) = (n−1) × 10,0 s     · hook ofseti 0
RUNTIME:         1.800 s
RAW FOOTAGE:     ⬜ · TRIM BUDGET: 0 (ızgara sabit, kırpma yok)
SCREEN TEXT:     0 saniye  ⛔ film boyunca okunur metin SIFIR
CAMERA:          180/180 sabit lockoff · 0 kamera hareketi
SETUP SEQUENCE:  ⬜ film · FAZ 1: ECU·CU·EWS·WS·MS·MCU·CU·MCU·MS·MCU·CU·MCU
KURULUM İSKELETİ: ⬜ film · FAZ 1: A B C D E F G H I J K L
                 🔧 11.09: 07.09'un "A B F E D C B C D C B C" satırı ölçeğe göre
                 sayılmıştı; iskelet AYNI KAMERA METNİ demektir [ACI_YAYI §7 ⑥] ve
                 FAZ 1'de 12 azimut/lens/mesafe üçlüsünün hiçbiri tekrar etmez.
KÜME:            FAZ 1'de 0 küme  ⛔ ≥2 şartı TUTMUYOR — BİLİNÇLİ SAPMA
                 [FAZ_01 §BİLİNÇLİ SAPMALAR ②④]: 12 ayrı kurulum = "kimse yok"
                 hissi (kamera sabitlenecek yer bulamıyor). `prompt_kontrol` ⑩④
                 FIX basar; gerekçe yazılı. Karşılığı: F2-F8 her faz ≤6 kurulum,
                 küme ≥2, dönüş ≥%50; günlük kadrajı (L) 24 sahnede BİREBİR.
DÖNÜŞ:           FAZ 1'de 0/12 = %0  ⛔ aynı sapma (yukarıdaki gerekçe)
DAVRANIŞ ŞERİDİ: FAZ 1: S D S T R G G G G R K R
                 (G %33 ≤ %50 ✓ · K(S8) öncesi D(S2)+T(S4) ✓ · K sonrası R ✓ ·
                 S 2 (S1 · S3) · ilk S ≠ son R ✓) [KARAKTER_KARTI §4]
TEMPO:           FAZ 1: Y N Y N Y N Y N N Y H Y  (ardışık üç aynı YOK ✓ ·
                 K=S8 çevresi N-Y-N → K'nın kendisi N ✓) [OYUNCULUK_YAZIM §4]
CAM KADEMESİ:    FAZ 1: 0 0 0 0 0 0 0 0→1 1 1 1 1  (S8 tek klip içi geçiş)
KASK:            FAZ 1: T T T T T T T T T Ç Ç Ç (S10-S12 TEK MÜHÜR açık: kask;
                 eldivenler takılı, yaka halkası kapalı) [D89]
ANGLE ARC:       FAZ 1'de 4 açı TİPİ (üst · göz hizası · tepe · alçak)
                 ✅ §2 en az 3 ister
DORUK:           FAZ 14 · S157-S168 (sahne başlangıcı 1.560 s)
ŞOK BANDI:       film boyu 2 · S2→S3 (FAZ 1) ve ⬜ (FAZ 12)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = (n−1) × 10,0 + promptun TIMELINE ofseti
   S4  = 3 × 10,0 + 4,0  =  34,0 s → 36,0 s (ses; basış 33,0 — tereddüt 1 s);
         ikinci basış 3 × 10,0 + 8,0 = 38,0 s; 36,0-38,0 alıcı hışırtısı = CEVAP YOK
   S12 = 11 × 10,0 + 2,0 = 112,0 s → 119,0 s  (22 kelime / 7 s ≈ 3 kelime/s)
   🔧 11.09: 07.09 "114,0" yazıyordu — promptun TIMELINE'ı 4 s'ye 22 kelime
   sığdırıyordu (5,5 kelime/s, söylenemez); prompt 2,0 s'ye çekildi.
   ⛔ Yazılan her kayıt bu formülle DOĞRULANIR.
   DORUK BAŞLANGICI = 0 + (157 − 1) × 10,0 = 1.560,0 s (FAZ 14 · S157)
   CHOICE S151 = 1.500,0 s · COST S140 = 1.390,0 s · FINAL S180 = 1.790,0 s

FİNAL VURUŞ KANITI [D141 · D76]:
   ⬜ FAZ 15 yazılmadı. Planlanan: BULUNAN nesne değil, BULUNMAYAN —
   son karede vizörün mat şeridi kadrajın yarısını kaplar ve ardındaki
   gökyüzü ilk kez okunmaz. Sayılabilir olması gereken şey ŞERİDİN
   KADEME SAYISIDIR (12). ⛔ SPEC kilitlenmeden bu satır doldurulmalı.
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK

DÖNGÜ KANITI:
   S1 (vizör camının içinden açılan göz, cam TEMİZ) ↔
   S180 (aynı kurulum, aynı ölçek, aynı ışık, cam 12 KADEME MAT)
   ⛔ Eş kadraj çifti: aynı lens (100mm), aynı mesafe (0,4 m), aynı
   üst açı 20°. Değişen TEK değişken CAMDIR — filmin tezi budur.
   ⛔ ÇİFT KAFİYE [ACILIS_KAPANIS §3]: göz kadrajın AYNI koordinatında;
   S180 imajı S1 imajından türetilir (plan ÇİFT KARTI).

⭐ ÇAPA ÜÇLÜSÜ [OYUNCULUK_YAZIM §2 · 11.09.2026] — ⑩ mod D "ANCHOR BEATS"
   ve "THE CHOICE ON THE BODY" testi buradan okunur:
   CHOICE  S151 · 1.500,0 s · BEFORE: bez elde, el vizöre bir avuç kala DURUR
                             AFTER:  el iner, bez asılı; cam silinmemiş; sonraki
                             klipte (S152) cam AYNI kademede [aynı kanal: SAĞ EL]
   COST    S140 · 1.390,0 s · BEFORE: gezici hareketli, adam koltukta, panel yüzü
                             gökte · AFTER: gezici durmuş, adam yerde, panel
                             kaplı, son bez YOK [kanal: ARAÇ + BEDEN KONUMU]
   FINAL   S180 · 1.790,0 s · BEFORE (S179): araç içi, lomboz mat, göz kapalı
                             AFTER: göz açık, lomboza bakar, el lomboza gitmez;
                             mat cam ardından gök okunmaz [kanal: GÖZ + SAĞ EL]
   FAZ 1 ön-çapası: S8 · 76,0 s · BEFORE cam berrak, ped köşede · AFTER
   şerit (3 parmak × 1 el) + memnun baş sallama [kanal: CAM + BAŞ]
   ⬜ S140/S151/S180 saniyeleri FAZ_12-15 promptlarının TIMELINE ofsetiyle
   yeniden hesaplatılır (şimdilik ofset 0,0 varsayıldı) [D122].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [D118]

```
PLAN (FAZ 1):  1 1 1 1 1 1 1 1 1 1 1 1
               ⛔ On iki sahnenin on ikisinde de insan VAR.
PLAN (film):   180 sahnenin 180'inde insan var — bu filmde insansız
               sahne YOKTUR. ⭐ Bu bir kısıt değil TASARIM: tek hatlı
               anlatıda kamera adamı hiç bırakmaz.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> ⛔ **BU BLOK MOD V'NİN PANZEHİRİDİR.** Tarif değil SAYI. Kaynağı burada
> YAZILI olan bulgu ⑩ ÖNERME KAPISI'nda DÜŞER ve puanı geri verilir.

```
İNSAN         1 · kadrajda tek insan, 180/180 sahne. İkinci insan, yansıma,
              manken, heykel YOK. Makine sesi de YOK.

KASK          Beyaz eliptik kubbe, TEK kavisli ön cam, optik berrak,
              tint YOK, ayna kaplama YOK — yüz camdan okunur.
              ⛔ VİZÖRÜN TEK NİTELİĞİ + TEK İSTİSNASI [D197]: "optically clear
              … EXCEPT the single matte abraded band described in the
              scene". Mühürlü durumun üç görünür işareti [D95]: beyaz rim ·
              kapalı yaka halkası · üst kenar spekülar. S10-S12 TEK MÜHÜR
              açık (kask); eldiven çıkmışsa KUSURDUR [D89].
              GİYSİ LİVERY'Sİ v4 (12.09 · sahip onayı; v1-v3 aynı gün iptal):
              YENİ NESİL gezegen giysisi, KATMANLI SERT PANEL — yarı parlak İNCİ
              BEYAZI sert üst gövde kabuğu + sculpted omuz/dirsek/kalça/diz
              kapakları · panellerin ARASINDA GUNMETAL koyu gri esnek eklem, dar
              koyu panel boşluğu · omuz/bilek/kalçada FIRÇALANMIŞ GÜMÜŞ rulman
              halkası (3 çift) · TEK AKSAN ELEKTRİK CYAN: her panel kenarında ince
              çizgi + SOL üst kol ve SOL uyluk çevresel bandı + kask içi şerit ·
              sırt paketi İNCE KONTÜRLÜ (sırtın eğrisini izler), mat gunmetal,
              pahlı kenar, üstünde gümüş panelde 1 cyan üçgen · üç METİNSİZ yama
              (SAĞ göğüs gümüş şevron/lacivert rozet · SOL göğüs siyah altıgen,
              TAM 3 altın nokta + turkuaz yarım daire · SOL omuz KAPAĞI gri/cyan
              köşegen) · eldiven inci beyazı, parmak sırtı gunmetal · kask
              DEĞİŞMEDİ · toz "rust-orange". ⛔ Giysi HACİMLİDİR (sert üst gövde,
              omuz ×1,5, büyük sırt — T14.2): "tulum/süper kahraman silueti"
              KUSURDUR. ⛔ KÖRÜK (corrugated/Michelin eklem) KUSURDUR — v4 bilinçli
              çıkardı, model çizerse ② yazar; "koyu eklem", "metal halka" kusur
              DEĞİLDİR (tasarım).
              ⛔ Yamada harf/rakam/gerçek logo/bayrak = 0 (D45 · ⑯). Cyan bant SAĞA
              geçerse ya da iki tarafta olursa AYNA/devamlılık kusuru [⑥ · ②];
              nokta ≠ 3 ise ① cat.6. Renkler tek yüzeye bağlı [D176] — "livery
              solmuş / renk değişmiş" bulgusu yalnız aynı kadrajda iki farklı
              hue ile yazılır. ⛔ Yamaların VARLIĞI kusur değildir.
              ⛔ Sırt ünitesi VARDIR ve büyüktür (arkadan girişli, sırtın
              eğrisini izleyen kontürlü paket — kutu DEĞİL) — bu D79'un "düz siluet" kuralının BİLİNÇLİ
              istisnasıdır: gezegen giysisi yörünge giysisi değildir,
              gerçek yüzey giysilerinin sırt paketi taşıyıcıdır
              [TUR 14 · rapor 3, KAYNAK]. ⛔ ② ve ⑤ bunu kusur yazamaz.

NOVUM         ⭐ BU GEZEGENDE KURU SİLİNEN HİÇBİR YÜZEY BİR DAHA BERRAK OLMAZ.
              Toz elektrostatik yüklü, keskin kenarlı ve camdan serttir:
              KURU bez onu kaldırmaz, cama sürterek AŞINDIRIR; her kuru
              silme camı ve paneli kalıcı olarak matlaştırır [TUR 16 #8 —
              gerçek triboloji, Suvin novum'u değil]. ISLAK silme çizmez —
              ama su hayattır (F3'ten sonra bez ıslatılmaz: KİLİT 6 su
              tüpü sıfırlanır). Bu ayrım filmin BEDEL çapasıdır.
              ⛔ BEYAN — TASARIM, KUSUR DEĞİL [BLIND RETURN köpük emsali ·
              D166 iki vaka]: mat şerit, çizik, kademe artışı, kaplı
              panel ve tozlu eldiven bu filmin OLAYIDIR; ②/⑤/⑥ bunları
              "vizör hasarı / render kusuru / devamlılık hatası" diye
              puanlayamaz. Puanlayan bulgu ⑩ ÖNERME KAPISI'nda düşer.
              CAM MERDİVENİ — 12 kademe, yalnız ARTAR, FAZ SINIRINDA
              (tek istisna S8: klip içinde 0→1, novum karesi [D157]):
                K0 %0 (F1 S1-S7) · K1 köşe yaması 3 parmak × 1 el (S8→F2) ·
                K2 %10 · K3 %15 · K4 %22 · K5 %30 · K6 %40 · K7 %50 ·
                K8 %60 · K9 %70 · K10 %80 · K11 %88 · K12 %95 (S180)
              Şerit HEP göğüs kadranının yeşil yayıyla aynı taraftaki alt
              köşeden büyür [D104 · D174]; kask bench'teyken de görünür.
              İHLALİ NE OLUR: silinen bir yüzeyin BERRAKLAŞMASI · tozun
              dökülmesi, savrulması ya da silkelenerek düşmesi · mat
              şeridin küçülmesi, kaybolması, yer değiştirmesi ya da buğu/
              yansıma/çatlak/damla olarak okunması · kademenin faz içinde
              (S8 dışında) değişmesi.
              ⛔ MAT ŞERİDİN BÜYÜMESİ KUSUR DEĞİLDİR — FİLMİN OLAYIDIR.
              ⛔ TOZUN YAPIŞIP KALMASI KUSUR DEĞİLDİR — KURALIN KENDİSİDİR.

YERÇEKİMİ     0,38 g (3,721 m/s²) · TEK VE SABİT, 180 sahnenin 180'inde.
              Düşen nesne Dünya'ya göre ~1,5 kat sürede iner ve SERT iner
              (ivme azalır, ATALET AZALMAZ) [D169].
              ⛔ "İki yerçekimi" bulgusu için ölçüm CETVELİ gerekir:
              0,3 s (7 kare @24fps) ve 0,5 m altındaki düşüşten SAYI
              ÇIKMAZ [⑥ RULER FLOOR]. Cetvelsiz FAIL DÜŞER.

ATMOSFER      610 Pa (Dünya'nın 1/600'ü) · %95 CO₂ · yoğunluk 0,020 kg/m³
              ⛔ RÜZGÂR TOZDAN AĞIR HİÇBİR ŞEYİ KIMILDATMAZ.
              30 m/s'de dinamik basınç ~9 Pa'dır. Kadrajda savrulan
              enkaz, devrilen ekipman, dalgalanan bez YOKTUR ve
              OLMAMASI DOĞRUDUR — bunu kusur yazan bulgu düşer.
              TOZ FİZİĞİ [D39 · D59 · LOW POWER Parçacık 2/10]: kalkan
              toz en çok BİR EL yükselir, her tane kendi düz yolunda,
              KLİP İÇİNDE (≤1 s) yere oturur; swirl 0, asılı kalma 0.
              🔧 11.09: 07.09'un "havada uzun süre asılı kalır" satırı
              GERİ ÇEKİLDİ — su altı süzülmesi yazdırıyordu.
              ⑥ SAYISAL KİLİT: kalkış yüksekliği ≤ 1 el · oturma ≤ 1,0 s ·
              dökülen/savrulan tane 0 · BOZULMA KARESİ sütunu zorunlu.
              VİZÖR İÇİ: buğu 0 · yoğuşma 0 · kırağı 0 [T11.5④ sahip
              kararı] — S1'in nefes buğusu 11.09'da çıkarıldı.

EKRAN YÖNÜ    Hedef (yaşam modülü, sonra yükseliş aracı) HEP EKRAN-SAĞ.
              İlerleme HEP soldan sağa. FAZ 1'de S5 ve S9'da modül
              kadrajın EKRAN-SAĞ tarafındadır. 180/180 sahnede sabit.
              KUŞBAKIŞI: modül adamın ~215° yönünde, ~150 m (07.09 "NE 300 m"
              düzeltildi — S3'ün 020° bakışı modülü görürdü). S3 EWS'de
              modül KADRAJDA DEĞİL ve olmaması doğrudur.
              ⛔ AYNA KAPISI: adam asimetrik (şerit köşesi · sağ kalça ·
              çene izi sol) → yön hatası yatay çevirmeyle onarılmaz.

SAYAÇ         GÖĞÜS İĞNESİ — rakamsız mekanik kadran, yeşil yay solda,
              kırmızı yay sağda, tek siyah iğne. MONOTONİK: yalnız
              dolum sahnelerinde geri gider, kendiliğinden ASLA.
              FAZ 1: iğne kırmızı yayın ortasında ve KLİP İÇİNDE SABİT
              (S7 "holds its place"); ilerleme FAZ SINIRINDA.
              🔧 11.09: 07.09 "10 s'de bir iğne kalınlığı kayar" yazıyordu —
              0,7 m/85 mm'de 6 px, ölçülemez; ⑥ cat.5 bu satırı
              NOT EXERCISED yazar, "iğne oynamadı" kusur değildir.
              METİNSİZ SAYAÇ KANALLARI (film): iğne · erzak kulesi 4×10=40
              paket · çentik duvarı (1 çentik = 1 sol) · su tüpü (çizgisiz,
              F3 sonrası boş) · cam kademesi · sakal ≤3 cm · giysi toz
              merdiveni (PHASE 1: sağ avuç pas rengi, S2'den itibaren) ·
              gündüz/gece/fırtına ışık blokları. ⛔ Hiçbirinde rakam yok.
              ⛔ ÜSTÜNDE RAKAM YOKTUR VE OLMAMASI DOĞRUDUR — bunu
              "eksik bilgi" diye kusur yazan bulgu düşer.

EŞ KADRAJ     S1 ↔ S180 (kurulum · ölçek · ışık · jest aynı; CAM farklı)

YIPRANMA      Sabit bölge sayısı: 5 [D42]
              ① vizör camı — mat şerit, yeşil yay tarafı alt köşe, 12 kademe
              ② diz altı — pas rengi toz, 180/180 sahnede kaplı
              ③ sağ kalça yan panel — açıklık (2 parmak) → zımba → kabuk → iz
                 (sözlük: opening/split/dark line — wound/blood/torn/leak
                 hiçbir promptta, ne pozitif ne negatif [red defteri #4])
              ④ sakal — beş kademe, ≤3 cm (SAKAL TOKENİ, faz sınırında değişir;
                 "long" YOK — 30 sol'de 3 cm'yi geçmez [TUR 16 #1])
              ⑤ eldiven/giysi toz merdiveni — PHASE 1 sağ avuç + parmak içi
                 pas rengi (S2→) · PHASE 2 dirsekler · PHASE 3 ön kol · PHASE 4
                 göğüs plakası alt kenarı (KİLİT 7, yalnız artar)
              ÇENE İZİ: S10-S12 sol çene, başparmak boyu, kuru; S13+ kararır/
                 kabuklanır, faz sınırında.
              ⛔ YIPRANMA HİÇ GERİ GİTMEZ. Bir kademe geri giderse kusurdur.
              ⛔ Toz her sahnede vardır ve TEMİZLENMİŞ görünmemelidir.

IŞIK TAKVİMİ  MONOTONİK DEĞİL, İKİ REJİMLİ ve rejim MEKÂNA bağlıdır:
              DIŞ  = tek sert güneş, ufkun 15° üstünde, BATIDA (dünya
                     yönü sabit); EKRAN TARAFI SAHNE BAŞINA kamera
                     azimutundan türer, δ = 90°−θ [D201] — "her kadrajda
                     ekran-sol" 07.09'un hatasıydı, 11.09'da düzeltildi.
                     KEY DIRECTION STRING (FAZ 1 dış):
                     S1 R · S2 ahead · S3 L · S4 behind · S5 R · S6 ahead ·
                     S7 L · S8 behind · S9 R
                     ⛔ ⑪ IŞIK bunu "key walks" diye puanlayamaz — kamera
                     döner, güneş dönmez; kusur yalnız AYNI azimutta iki
                     klip farklı tarafı gösterirse yazılır.
                     Gölgeler güneşten türer, jilet kenarlı, gölge içi
                     soğuk arduvaz mavisi; gökyüzü tereyağ-şeker.
                     Her LIGHTING satırı "LIGHT STATE: exterior day ·
                     scene n of 12" taşır.
              İÇ   = yalnız pratik ışık, ALTTAN (iki sıcak çalışma
                     lambası + zeminde cyan şerit), tavan karanlık.
              GÜN BATIMI (FAZ 9 · 12 · 15) = güneş çevresinde BUZ MAVİSİ
                     hale, çeper pas rengi. ⭐ Bu fizik olarak DOĞRUDUR
                     (Mie ileri saçılma) ve Dünya'nın tersidir
                     [TUR 14 · rapor 3, KAYNAK].
              ⛔ İç ile dış arasındaki ışık farkı KUSUR DEĞİLDİR —
                 filmin kimlik kilididir. ⑪ IŞIK bunu "grade sıçraması"
                 diye puanlayamaz.
              ⛔ MAVİ GÖKYÜZÜ YOKTUR ve olmaması doğrudur.

SES REGISTER  HUMAN: tek ses, tamamen İngilizce.
              MACHINE: 0 — bu filmde konuşan makine YOKTUR.
              ⛔ SESSİZLİK TASARIMDIR. FAZ 1'de 12 sahnenin 10'unda
                 replik yoktur ve olmaması doğrudur; ters U eğrisinin
                 şok evresidir [TUR 13 · rapor 2, ÖLÇÜLMÜŞ].
              ⛔ Dış mekân replikleri POST'TA binmiştir; ağız senkronu
                 aranmaz ve yokluğu kusur değildir.
              ⛔ FAZ 1'de HER REPLİK CEVAPSIZDIR ve cevapsızlık TASARIMDIR
                 (S4 telsiz: 2,0 s hışırtı · S12 günlük: muhatap yok).
                 ③ SES bunu "cevap eksik" diye puanlayamaz; DEĞİŞ-TOKUŞ
                 tablosu FAZ_01 §SES'te.
              ⛔ S8 tek ses olayı: pedin cam üstündeki kuru sürtünmesi
                 (uzun, kesintisiz) — "hoş olmayan" ses TASARIMDIR.
              ORTAM: dışarıda neredeyse mutlak sessizlik + kask içi
              nefes; içeride yaşam destek uğultusu.
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI [D142]

> ⛔ **DOĞRULANDI SATIRI OLMAYAN KAPI YAZILMAMIŞTIR.** Bir SPEC'in kamera
> sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve sessizce hiç
> koşmadı. Aşağıdaki dört kapı **07.09.2026'da bu makinede fiilen sınandı.**

```
KAPI 1        IZGARA — klip süresi gerçekten 10,0 s mi [D124]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
DOĞRULANDI    ffprobe/ffmpeg 8.1 · 07.09.2026 · yeniden 11.09.2026 (/opt/homebrew/bin/ffprobe)
İKAME         —  (ffprobe her zaman var)
⛔ İLK TEST KLİBİ ÜRETİLDİĞİNDE BU KAPI KOŞULUR ve sayı B BLOĞU'na yazılır.

KAPI 2        KAMERA SABİTLİĞİ — 180/180 sahne lockoff iddiası
KOMUT         ffmpeg -i <klip> -vf vidstabdetect -f null -
DOĞRULANDI    🔴 KOŞULAMADI — vidstabdetect bu makinede KURULU DEĞİL
              (ffmpeg -hide_banner -filters | grep " vidstabdetect " → boş;
              11.09.2026'da yeniden sınandı: hâlâ YOK)
İKAME         ✅ freezedetect ile TERS ölçüm: sabit kamerada arka planın
              statik bölgesi donuk kalır.
              ffmpeg -i <klip> -vf "crop=iw/4:ih/4:0:0,freezedetect=n=0.003:d=2" -f null -
              ⛔ Bu bir İKAMEDİR, kamera sabitliğini DOĞRUDAN ölçmez.

KAPI 3        KONTRAST — tekdüze kırmızıda kadrajın düzleşmesi
KOMUT         ffmpeg -i <klip> -vf signalstats -f null - 2>&1 | grep YDIF
              ⛔ EŞİK: her karede YMAX − YMIN ≥ 110
DOĞRULANDI    ffmpeg 8.1 · signalstats mevcut · 07.09.2026 · yeniden 11.09.2026 ✓
İKAME         —
GEREKÇE       Bu filmin kendi riski. `02_RISK_KARTLARI` TEKDÜZE RENK kartı:
              kırmızı-turuncu tek renk havuzu difüzyon modelinde derinliği
              öldürüyor. İnci beyazı paneller + gunmetal eklem + cyan pratik/bant
              + siyah bazalt bu eşiği tutturmak için var (livery v4 12.09: beyaz
              giysi pas zeminin havuzuna girmez, parlaklık aralığını beyaz panel /
              gunmetal eklem çifti kendi içinde taşır; toz "rust-orange").

KAPI 4        SES KANALI — plan sesli, master sessiz çıkarsa [D136]
KOMUT         ffprobe -v error -select_streams a -show_entries stream=codec_type -of csv=p=0 <master>
DOĞRULANDI    ffprobe 8.1 · 07.09.2026 · yeniden 11.09.2026 ✓
İKAME         —
⛔ SES KANALI YOK + plan sesli → 🔴 TESLİM KUSURU: parti durur, master
   yeniden ihraç edilir, dört mercek yeniden koşulur.

KAPI 5        KUYRUK/BAŞ KART — S1↔S180 eş kadraj çiftini öldüren kart
KOMUT         ffmpeg -i <master> -vf "freezedetect=n=0.001:d=1.5" -f null -
              + ffmpeg -sseof -1 -i <master> -frames:v 1 son_kare.jpg → BAK
DOĞRULANDI    ffmpeg 8.1 · freezedetect mevcut · 07.09.2026 · yeniden 11.09.2026 ✓
İKAME         —
⛔ Kart varsa kesilir ve ⑪ yeniden koşulur [D70 · D72, 9 vaka].

KAPI 6        METİN SIFIRI — S12 günlük klibinde altyazı/caption sızıntısı
KOMUT         ffmpeg -ss 112 -i <S12 klibi> -frames:v 3 -vf "select=not(mod(n\,24))" s12_%02d.jpg → BAK
              (alt üçte birde okunur karakter 0 · lens üstü yazı 0)
DOĞRULANDI    ffmpeg 8.1 · select/scale mevcut · 11.09.2026 ✓ (görsel kapı, sayı üretmez)
İKAME         —
⛔ Altyazı varsa klip RET; prompta "No subtitles, no captions" ZATEN yazılı —
   ikinci red → SESSİZ KOŞU teşhisi, motor kararı sahibin [red #15].
```

## ⛔ KESİLEMEZ LİSTESİ — kurgu kapısı bunları kırpamaz [D166 · D141]

```
FAZ 1:  S8 (novum karesi; 6,0-10,0 s şeridin doğuşu) · S10 (ilk yüz, 0,0-3,0 s) ·
        S12 (replik 112,0-119,0 s — dudak senkronu bozulsa da SES kesilmez,
        klip sessiz koşuya alınır) · S1 (0,0-4,0 s kapak anı; göz açılışı)
FİLM:   S140 (COST) · S151 (CHOICE, 1.500,0-1.510,0 s tam klip) · S180 (FINAL, tam
        klip) · her fazın son 2,0 s'si (sınır satırı taşıyıcısı) ⬜ FAZ 2-15
⛔ Kırpma önerisi bu listedeki saniyeye değiyorsa öneri DÜŞER; "ritim için
   kırp" gerekçesi 10,0 s sabit ızgarada zaten geçersizdir (B BLOĞU gerekçesi).
```

---

## 🚫 YANLIŞ POZİTİF DUVARI — bu filmde kusur SAYILMAYAN on dört şey

```
1. Tozun yapışıp kalması, silkelenince dökülmemesi        → NOVUM
2. Silinen camın berraklaşmaması, mat şerit bırakması     → NOVUM
3. Mat şeridin fazdan faza BÜYÜMESİ                       → NOVUM
4. Rüzgârın hiçbir şeyi kımıldatmaması                    → ATMOSFER (9 Pa)
5. Göstergede rakam olmaması                              → METİN YASAĞI
6. İç ile dış arasındaki keskin ışık farkı                → IŞIK TAKVİMİ
7. On iki sahnenin onunda replik olmaması                 → SES REGISTER
8. Büyük sırt paketi (düz siluet değil)                   → KASK, D79 istisnası
9. Güneşin sahneden sahneye ekran tarafı değiştirmesi     → IŞIK TAKVİMİ, D201
10. S3 EWS'de modülün görünmemesi                         → EKRAN YÖNÜ (215°)
11. S7'de iğnenin hiç oynamaması                          → SAYAÇ (faz sınırı)
12. FAZ 1'de 12 farklı kurulum, küme 0                    → B BLOĞU bilinçli sapma
13. Repliklerin cevapsız kalması (S4 · S12)               → SES REGISTER
14. Sağ avucun S2'den sonra pas rengi kalması             → YIPRANMA ⑤

⛔ Bu on dörtten birini kusur olarak yazan bulgu ⑩ ÖNERME KAPISI'nda
   DÜŞER, puanı geri verilir ve merceğin toplamı yeniden hesaplanır.
```
