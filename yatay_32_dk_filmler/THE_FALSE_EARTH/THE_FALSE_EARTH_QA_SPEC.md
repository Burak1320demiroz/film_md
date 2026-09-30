# 📋 THE_FALSE_EARTH — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_FALSE_EARTH_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ⚠️ **DİKEY FİLMDE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI — artık MAKİNE KAPISI
> DEĞİL.** Bu başlığı yalnız `rubrik_paketle.sh` okuyordu (aile: yatay/dikey) ve
> o betik 11.09.2026'da silindi. Başlık yazım geleneği olarak KALABİLİR; hiçbir
> betik ona bakmaz, yokluğu artık sessiz bir arıza üretmez.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri (hedef dilimi · hareket yönü · eksen) + A  MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⭐ 14.09.2026: ⑭/⑮ için C bloğuna yazılacak satırlar — `HAREKET KİLİDİ:` (eller/ayaklar/baş ne
   yapar, "tek jest" kuralı) ve `EKRAN YÖNÜ:` (hedef hangi dilimde · figür hangi yöne · eksen
   çizgisi — screen-left/right, pusula yok). Yoksa iki mercek çıkarımla koşar ve bunu yazar.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_FALSE_EARTH
FORMAT:            yatay 16:9 · 32 dk · KILAVUZ_REHBERI §2.9 · ÇOK KLİPLİ SAHNE rejimi
RUNTIME:           1920 seconds (title card: YOK — screen text lock 0 s)
SCENE COUNT:       50
PART GRID:         8 PART × 24 klip × 240 s + FULL (her PART = 2 bölüm dosyası)
                   P1 = S01-S07 · K001-K024 ·    0- 240 s      P5 = S26-S31 · K097-K120 · 960-1200 s
                   P2 = S08-S13 · K025-K048 ·  240- 480 s      P6 = S32-S37 · K121-K144 · 1200-1440 s
                   P3 = S14-S19 · K049-K072 ·  480- 720 s      P7 = S38-S43 · K145-K168 · 1440-1680 s
                   P4 = S20-S25 · K073-K096 ·  720- 960 s      P8 = S44-S50 · K169-K192 · 1680-1920 s
                   ⛔ Her PART tam sahnelerle başlar ve biter; hiçbir sahne PART sınırını aşmaz.
                   Rubriğe "THIS FILE IS PART n OF 8 — 24 clips — <a>-<b> s" beyanı yapıştırılır.
                   BOUNDARY PAIR'lar (K024|K025 · K048|K049 · … · K168|K169) elle kareyle kapanır.
                   — (şablonun özgün notu: yalnız 6/8/16 dk hattı [§2.6/§2.7/§2.8]: n PART satırı — B1 = S00-S17 · 18 clips ·
                   0-180 s · B2 = S18-S35 · 18 clips · 180-360 s (6 dk) … 16 dk: B1-B4 × 24 clips ×
                   240 s + FULL = S00-S95 · 96 clips · 0-960 s. QA her parçaya AYRI koşar; rubriğe
                   SPEC'le birlikte "THIS FILE IS PART n OF m — …" beyanı yapıştırılır;
                   BOUNDARY PAIR(lar) elle kareyle kapanır. Diğer formatlarda "—" kalır)
THEME:             FEDAKÂRLIK — "Başta her şeyi kaydettiren kişi, sonunda kendi
                   kaydını kimsenin duymayabileceği bir yere bırakır."
THEME SCENES:      S42 · S44 · S49     (karar · birinci ödeme · ikinci ödeme)
INTENDED EMOTION:  çift-duygu — kavuşma sevinci ile tanımanın dehşeti AYNI karede (K048)
ENDING TYPE:       KAFİYE — cevap değil, açılışın (K001) çoğalmış hâli (S50 · D210)
PROTAGONIST:       kadın mürettebat, tek kişi (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    "Ama kapıyı açmayacağım." — S42 · K164 · 27:14,0
DIALOGUE LINES:    47 · register: HUMAN 23 / MACHINE 20 / karışık 4
                   ⛔ AĞZI OKUNAN yalnız 4 klip: K057 · K059 · K163 · K164 — geri kalan
                   43 replik kadraj dışı ya da kapalı ağızla [KART 7 · D215]
SILENT SCENES:     1 — S37 · K143 (tam sessizlik; HARD MUTE 1.420-1.430 s, MUZIK dosyası)
VIRAL INTERSTITIALS: K023 · K024 · K045 · K047 · K113 · K174  ⛔ THESE MAY NOT BE CUT
TITLE:             "THE FALSE EARTH" — 3 kelime; izleyiciye nereye bakacağını söyler:
                   kadrajdaki Dünya'ya benzeyen şeyin Dünya OLMADIĞINA
LIBRARY CONTEXT:   yatay uzun hat · aynı rafta THE_STOLEN_SKY (16 dk) · BENI_HATIRLAMA ·
                   SUSMAYAN_NOBETCI · THE_SLOW_RAIN (8 dk)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      192  (192 × tam 10 s = 1920 s)
SHOT COUNT:      192 · sahne içi kesme 142  (192 klip − 50 sahne)
SCENE PLAN:      SAHNE PLANI: 2 2 4 4 3 4 5 3 4 5 4 4 4 4 4 4 4 4 4 3 4 5 4 4 4 4 4 4 5 4 3 4 5 3 3 4 5 4 4 4 4 4 4 6 3 3 3 4 2 3
                 (toplam 192 · SCENE COUNT 50 ≠ CLIP COUNT 192)
                 — (şablonun özgün notu: yalnız ÇOK KLİPLİ SAHNE filminde [COK_KLIPLI_SAHNE §1 · 22.09.2026]: PLAN'daki
                 SAHNE PLANI satırı + "S01 = K01 · S02 = K02-K04 · …"; SCENE COUNT ≠ CLIP COUNT)
INTRA-SCENE CUTS: — (aynı rejimde: K02|K03 · K03|K04 · … — these cuts are INSIDE one scene:
                 location, light, sound bed, costume dirt, held object and body pose MUST match
                 across them; a reset here is a ② CONTINUITY defect, not a scene change)
TARGET ASL BAND: 10,0 s sabit   ASL CURVE: düz
                 ⛔ GEREKÇE [D74]: araç klip süresini 10 s'de kilitliyor [D124]; ritim
                 KLİP süresiyle değil, SAHNE uzunluğuyla (2-6 klip) ve kurulum
                 kademesiyle kuruluyor. Ölçülmüş: sahne uzunluğu 2'den 6'ya değişiyor.
GRID:            klip başlangıcı(n) = (n − 1) × 10 s · n = 1…192 · istisna YOK
                 sahne başlangıcı = SAHNE PLANI'nın kümülatif toplamı × 10 s
RUNTIME:         1920 s
RAW FOOTAGE:     192 × 10 s = 1920 s · TRIM BUDGET: 0 s (ızgara sabit, kesme sahne içi)
SCREEN TEXT:     0 saniye
CAMERA:          192 / 192 sabit lockoff  (her promptta "absolutely zero camera movement")
SETUP SEQUENCE:  bölüm dosyası başına KURULUM İSKELETİ bloğu — 16 dosyanın her birinde
                 harf dizisi + harf başına lens · azimut · MESAFE · yükseklik yazılı
KURULUM İSKELETİ: bölüm başına ayrı dizi (PLAN §KURULUM ile birebir). Son dört dosya:
                 b13 A B A B C D C E C D C D · b14 A B A B A C A C A C A C
                 b15 A B C B A B D E D F G F · b16 A B A C D C D C D E F G
KÜME:            — (ÇOK KLİPLİ SAHNE rejiminde KÜME YOKTUR; yerini sahne içi kapsama
                 alır [COK_KLIPLI_SAHNE §0 · prompt_kontrol ⑩④ dalı koşmaz])
DÖNÜŞ:           bölüm başına ≥%40 · son dört dosya: b13 %58 · b14 %75 · b15 %42 · b16 %42
ANGLE ARC:       5 açı TİPİ film genelinde (§2 en az 3 ister) — cepheden göz hizası ·
                 üç-çeyrek yandan göz hizası · karşı açı alt açı 20° · insert üst açı
                 30° · üstten geniş açı. ⛔ HER BÖLÜM DOSYASINDA en az 3'ü var [⑪].
DORUK:           S44 → K169-K174 (6 klip · sahne başlangıcı 1680 s · bitiş 1740 s)
ANCHOR BEATS:    CHOICE at 1637,5 s (K164) · COST at 1688,0 s (K169) ·
                 FINAL at 1885,0 s (K189)   ← ⑩ mod D bu satırı okur
                 ölçülen gövde farkı: 288 px · 384 px · ⚠️ 32 px
                 ⛔ FINAL eşiğin (kadraj kısa kenarının 1/8'i) ALTINDA ve gerekçesi
                 PLAN §ÇAPA ÜÇLÜSÜ'nde üç seçenekle yazılı — SAHİP KARARI bekliyor.
                 Filmin gerçek son klibi (K192) aritmetik olarak çapa taşıyamaz:
                 Mira 14,0 m'de, eşik 1,97 m, boyu 1,75 m.

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Yazılan her kayıt formülle DOĞRULANIR; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   nesne: karanlıktaki küçük sıcak ışık noktaları (her biri bir pencere)
   saniye: 1918,0 s (K192 · 8,0 s) · kaç tane: kadrajda sayılamayacak kadar çok,
   ama O SANİYEDE YANAN TAM BİR TANE — düz kenarı olmayan bir şeklin içinde
   durum: BULUNAN (yeni bir ışık YANIYOR, sönmüyor)
   ⭐ Sayılabilir olan "kaç ışık var" değil, "kaç ışık DEĞİŞTİ": 1.
   ⛔ Bu, açılışın (K001: TEK sıcak pencere, uzakta) kafiyesidir [D210].
   ⛔ tek karede sayılabilir ve adı konabilir olmalı; "final duygusu" değil
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: ilk kare ↔ son kare — K001 ve K192 AYNI KURULUM AİLESİNDE:
   ikisi de 18mm · EWS · yukarıdan-arkadan · IN FRAME: full body, back ·
   ikisinde de gök "uniform black, no stars, no sun and no moon" ·
   ikisinde de tek ışık kaynağı 3000 K konum lambası · ikisinde de kadın
   KAMERAYA SIRTI DÖNÜK ve bakışı kadrajın dışındaki büyük şeyde.
   TEK FARK — ve filmin bütün cevabı orada: K001'de baktığı şeyde HİÇ IŞIK YOK,
   K192'de baktığı karanlık SAYILAMAYACAK KADAR IŞIKLA DOLU.
   ⛔ Mesafe aynı değil (K001 14,0 m · K192 6,0 m) ve bu kasıtlıdır: son karede
   ona daha yakınız. Jest aynı, uzaklık değil.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1-1-111-1111111--11--111 111-11111111-11111111111 111111-11111--1111111-11 -11111-111111--11---111- ----11111-1111111-1111-- ---------11-1111-1111111 1---1-1-111-111111111111 1----1--1---1-11--111--1
       (1 = insan var · - = insansız · KLİP başına bir karakter · 192 karakter,
        24'lük sekiz PART bloğu hâlinde yazıldı — boşluklar PART sınırlarıdır)
K001-K024  1-1-111-1111111--11--111
K025-K048  111-11111111-11111111111
K049-K072  111111-11111--1111111-11
K073-K096  -11111-111111--11---111-
K097-K120  ----11111-1111111-1111--
K121-K144  ---------11-1111-1111111
K145-K168  1---1-1-111-111111111111
K169-K192  1----1--1---1-11--111--1
       insanlı 132 · insansız 60 · kaynak: 00_SAHNE_TABLOSU IN FRAME sütunu (betikle sayıldı)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         kadrajda en çok 1 · 132 klipte 1 · 60 klipte 0 · iki insan 0 klip
              (Lena yalnız KAYIT içinde görünür: K006 · K114 · K185 · K186)
KASK          KAPALI 192/192 klip · açık 0 · ara durum 0 [D208] · vizör TEK DÜZ PANEL +
              görünür koyu çerçeve · optik berrak [D146] · sırt ünitesi YOK — düz siluet
              [D79] · ⛔ seamless · dome · bubble · mirrored hiçbir promptta yazılmaz
NOVUM         KURAL: yapı gördüğü her şeyi yeniden kurabiliyor, görmediği hiçbir şeyi
              kuramıyor; geçidi açan eşleme görünmez bir iç durumdur (İLİŞKİ tipi).
              İHLALİ: kopyada, kaynakta GÖRÜLMEMİŞ bir ayrıntının bulunması — lambanın
              camındaki beyaz oval leke, fotoğraftaki FLAŞ PARLAMASININ kopyasıdır.
              TAŞIYICI: aile fotoğrafındaki lamba × odadaki lambanın camı.
YERÇEKİMİ     üç rejim, asla aynı kadrajda [D200]: 0 g (vakum) · 0,98 g (gezegen
              yüzeyi) · 1 g (basınçlı iç hacim, dönüşten)
ATMOSFER      0 kPa (vakum) · solunamaz (gezegen yüzeyi) · 101 kPa (iç hacim)
              ODA İSTİSNASI: Lena'nın odasının havası solunabilir — bu bir OLAYDIR
EKRAN YÖNÜ    hedef hep SCREEN-RIGHT · ilerleme SCREEN-LEFT'ten SCREEN-RIGHT'a
              — yaklaşma yönü 50 sahnenin 47'sinde sabit. ÜÇ İSTİSNA ve gerekçesi:
              S37 (kabloyu koparıp geri çekilir) · S44 (çekirdek dışarı, yani
              kameradan UZAĞA) · S46 (kollar gemiyi bırakıp screen-right'a gider —
              ilk kez hedef İNSAN DEĞİL). ⛔ Nesne-göreli taraf ("on her right")
              hiçbir promptta yok; hepsi ekran-göreli [uzamsal §6.1].
SAYAÇ         MONOTONİK — iki sayaç var, ikisi de tek yönlü:
              ① kirlenme: 0 bölge (K001-K023) → 1 bölge (K024'ten sonuna) · geri dönmez
              ② amber ışık: dönüyor (S04-S39) → içinde siyah damar (S40) → üç
                 parçada bölünmüş (K173 başı) → SÖNDÜ (K173 sonu) → hiç yok (S47-S50)
              ⛔ Sönmüş amber hiçbir klipte geri gelmez; QA bunu tek karede ölçer.
EŞ KADRAJ     S01 ↔ S50 (K001 ↔ K192 · yukarıda DÖNGÜ KANITI'nda tam yazılı)
              ikinci çift: S03 ↔ S48 — ikisinde de Mira bir KAYIT izliyor; ilkinde
              kayıt sağlam ve yalan, ikincisinde kayıt bozuk ve doğru.
DÜNYA ÇAPASI  3/3 [D209] — GÖK "A sky of uniform black, no stars, no sun and no moon."
              UFUK "The horizon is black water lying mirror-flat, or wet black basalt."
              YER İMİ "One warm window burning in the distance, the only point source
              on the ground." · ⭐ S50'de bu yer imi ÇOĞALIR (K191 dört küre, her
              birinde tek pencere · K192 sayılamayacak kadar çok) — D210 kafiyesi
              (şablon notu: gök · ufuk · yer imi (World Bible'daki üç cümle BİREBİR; dış-mekân promptlarında sıfır sapma) [D209]
YIPRANMA      1 sabit bölge [D42] — sağ önkol + sağ diz, TEK bölge sayılır çünkü
              tek olaydan (K024) doğar. Birikir, hiç temizlenmez, hiç sıfırlanmaz.
              ⛔ İkinci bir yıpranma bölgesi açılmaz; hasar da açılmaz.
KİMLİK DİZİSİ kask: 192 klibin 192'sinde K (KAPALI) — açık 0, ara durum 0 [D208]
              dizi: KKKK…K (192 harf, istisnasız · diziyi yazmaya gerek yok çünkü
              tek değerli; bir tek A çıkarsa dizi YAZILIR ve gerekçe istenir)
              amblem: SOL omuz (açık gri bant) · film boyu sabit · SAĞ omuzda hiçbir şey yok
              giysi rengi: mat kömür grisi, kuru ve yansımasız · 192 klipte aynı
              kir bölgesi: sağ önkol + sağ diz · başlangıç K024 · geri dönmez
              hasar: YOK — bu filmde giysi hiç yırtılmaz, delinmez, onarılmaz
IŞIK TAKVİMİ  MONOTONİK DEĞİL, ve bu KASITLI — bu filmin ışığı takvim değil MEKÂN
              izler. Üç sabit palet, her biri kendi mekânına bağlı ve mekân
              değişmeden değişmez: 3000 K konum lambası (gemi dışı / bölme) ·
              4500 K tavan paneli (gemi içi) · 2700 K lamba (oda ve kayıtlar).
              Buna binen İKİ tek yönlü değişken monotoniktir:
              ① amber halka 2200 K: var (S04-S44) → yok (S44 sonundan itibaren)
              ② yer imi (uzaktaki tek sıcak pencere): 1 (S01-S30) → şehrin hepsi
                 (S31 · K119) → yok (S32-S49) → sayılamayacak kadar çok (S50)
              ⛔ Aynı sahnenin içinde LIGHT satırı BİREBİR aynıdır [㉜⑥]; takvim
                 sahneler ARASINDA yürür.
SES REGISTER  HUMAN 23 replik · MACHINE 20 replik · karışık 4 = 47
              HUMAN kanalları: Mira'nın kendi sesi (yakın, filtresiz) · telsiz
              (dar bant-pass) · oynatılan kayıt (ince, kusurlu)
              MACHINE tek kanal: ECHO, kask içi, düz ve yakın — ⛔ ECHO hiçbir
              yerde ANLATICI değildir; yalnız ölçtüğü şeyi söyler.
              ⭐ Ağzı okunan YALNIZ 4 klip: K057 · K059 · K163 · K164 [KART 7 · D215].
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI 1        DONUK KARE — K143 (tam sessizlik) ve K192 (final) "hiçbir şey hareket
              etmiyor" talimatıyla yazıldı; model bunu FREEZE olarak üretirse klip reddedilir
KOMUT 1       ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=0.001:d=1.5" -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 24.09.2026 · freezedetect · blackdetect · signalstats mevcut
              ffmpeg -hide_banner -filters | grep -q " freezedetect " || kapıyı yeniden yaz
İKAME 1       filtre yoksa: 0,5 s aralıkla kare çıkarılır ve ardışık kareler
              `ffmpeg -i a.jpg -i b.jpg -lavfi psnr -f null -` ile karşılaştırılır

KAPI 2        SİYAHA KESME YOK — hiçbir klipte fade to black yazılı değil; kurguda
              kazara siyah kare kalırsa PART master'ı reddedilir
KOMUT 2       ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.1:pic_th=0.98" -f null - 2>&1 | grep black_start
DOĞRULANDI    ffmpeg 8.1 · 24.09.2026 · blackdetect mevcut
              ffmpeg -hide_banner -filters | grep -q " blackdetect " || kapıyı yeniden yaz
İKAME 2       filtre yoksa: blackframe=amount=98:threshold=32

KAPI 3        BLOOM / PARLAMA — "0% bloom" bütün promptlarda yazılı; master'ın
              tepe parlaklığı ve YHIGH dağılımı ölçülür
KOMUT 3       ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YMAX" -f null -
DOĞRULANDI    ffmpeg 8.1 · 24.09.2026 · signalstats mevcut
              ffmpeg -hide_banner -filters | grep -q " signalstats " || kapıyı yeniden yaz
İKAME 3       filtre yoksa: her PART'tan 24 kare çıkarılıp histogram elle okunur

⚠️ vidstabdetect bu kurulumda YOK (ffmpeg 8.1, 24.09.2026 ölçüldü). Kamera
   sabitliği kapısı bu yüzden KOMUTLA değil, KARE KARŞILAŞTIRMASIYLA koşar:
   her klibin 0,0 s ve 9,5 s kareleri çıkarılır, kadraj köşeleri üst üste konur.
```
