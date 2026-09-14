# 📋 THE LEANING ROOM — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**.
> Paketi betik üretir:
> `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh yatay_2_dk_filmler/THE_LEANING_ROOM`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                    EKRAN YÖNÜ · IŞIK TAKVİMİ · İNSAN
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE LEANING ROOM
FORMAT:            yatay 2-4 dk · 16:9
RUNTIME:           120 seconds (title card: YOK — screen text lock 0,0 s)
SCENE COUNT:       12
THEME:             ENTROPİ — bir oda bir kez düzeltilir, ikinci kez tam düzelmez
THEME SCENES:      S2 · S8 · S10 · S11
INTENDED EMOTION:  huşu (kaygı DEĞİL) + geri alınamazlığın sessiz kabulü
ENDING TYPE:       MUĞLAK — oda düzeldi, gösterge düzelmedi
PROTAGONIST:       otuzlarının sonunda bir kadın, geminin sahibi ve sürücüsü
                   (isimsiz — özel ad hiçbir promptta geçmez [D34])
CENTRAL CHOICE:    S7 · 1:12 — dümeni sonuna kadar açar, dar çizgiyi seçer
COST:              S8 (altı eşya sancak korkuluğunda, anahtar camda) ve
                   S9 (sarkaç lamba ezilir, seyirde 3° eğik kalır)
CHOICES AFTER THE CENTRAL CHOICE: 2 [D158 · B2a]
                   S10 üçüncü kütlede geniş hattı sürer · S10 sarkacı
                   düzeltmemeyi seçer (elini altından geçirir, dokunmaz)
FAILED ATTEMPTS:   2 [D158 · B2b]
                   S6 lambayı eliyle düşeye iter, bırakınca geri döner ·
                   S8 eşyaları toplamaya uzanır, parmak ucu yetişmez
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     müziksiz: S6 (1,5 s'den sonra) · S9 (tamamı)
                   repliksiz: 12 / 12
VIRAL INTERSTITIALS: S4 (1:00'a kadar · lamba 0°→4°, anahtar 8 cm) ·
                   S9 (lamba 68°→3°, iki ezik)   ⛔ THESE MAY NOT BE CUT
TITLE:             "THE LEANING ROOM" — vaat: bir oda yan yatıyor ve bunu
                   yapan şey odanın içindeki insanın kendi kararı
LIBRARY CONTEXT:   aynı raf: THE_COLD_WELD (vakum, soğuk kaynak) ·
                   THE_SILENT_EVENT_HORIZON · THE_SPAGHETTI_TIDAL
                   ⭐ AYRIM: bu depodaki ilk KASKSIZ uzay filmi ve ilk
                   tamamen ARAÇ İÇİ film; dış mekân 0 kare
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12
SHOT COUNT:      12 · sahne içi kesme 0
SCENE COUNT:     12          (üçü de EŞİT — sahne = çekim = klip)
TARGET ASL BAND: 10,0 s sabit   ASL CURVE: DÜZ (sapma 0)
                 ⛔ GEREKÇE [D74]: bu hat sabit ızgaralıdır (format kartı
                   §2.2: 12-18 sahne × 10 s). Ritim ASL ile değil ÖLÇEK ve
                   PALET sıçramasıyla kurulur; 11 ardışık çiftin 11'inde
                   ölçek de palet de ses dokusu da değişir.
GRID:            sahne başlangıcı(n) = 10,0 s hook + (n−1) × 10,0 s klip
                 S0 0,0 · S1 10,0 · S2 20,0 · S3 30,0 · S4 40,0 · S5 50,0
                 S6 60,0 · S7 70,0 · S8 80,0 · S9 90,0 · S10 100,0 · S11 110,0
RUNTIME:         120,0 s
RAW FOOTAGE:     12 klip × 10,0 s = 120,0 s · TRIM BUDGET: 0,0 s
                 (değişken çekim süresi YOK → KART 11 kırpma tablosu gerekmez)
SCREEN TEXT:     0,0 saniye
CAMERA:          12 / 12 sabit lockoff · kamera hareketi 0 kare
SETUP SEQUENCE:  A-D-B-F-E-F-B-A-C-B-F-E
                 A 24mm EWS göz hizası h1,20 6,4m   (S0 · S7)
                 B 50mm MS profil     h1,10 3,0m   (S2 · S6 · S9)
                 C 35mm WS alt açı    h0,42 4,6m   (S8)
                 D 28mm WS üst açı    h2,25 5,2m   (S1)
                 E 85mm ECU göz hizası h1,05 2,1m  (S4 · S11)
                 F 50mm CU omuz üstü  h1,15 1,1m   (S3 · S5 · S10)
ANGLE ARC:       5 açı TİPİ (§2 en az 3 ister) — göz hizası · üst açı ·
                 profil · omuz üstü · alt açı
                 ŞOK BANDI: 1 (S6→S7, MS→EWS, iki kademe) · bant ≤2
DORUK:           S7 → lamba 68°'ye varır (sahne başlangıcı 70,0 s +
                 TIMELINE 7,0 s = 77,0 s = 1:17)
KAPAK KARESİ:    78,0 s = 1:18

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   ⭐ BU FİLMDE REPLİK YOKTUR (0 satır). Formül aynı biçimde OLAY
     zamanlarına uygulandı ve her kayıt doğrulandı:
     katalizör    S1 · 10,0 + 3,0  = 13,0 s = 0:13   ✅ ≤0:15 kapısı
     tohum        S2 · 20,0 + 2,0  = 22,0 s = 0:22   ✅ 15-22 s penceresi
     başarısız ①  S6 · 60,0 + 1,5  = 61,5 s = 1:01
     merkezi seçim S7 · 70,0 + 2,0 = 72,0 s = 1:12   ✅ %60 bandı
     doruk        S7 · 70,0 + 7,0  = 77,0 s = 1:17
     bedel        S8 · 80,0 + 2,3  = 82,3 s = 1:22
     başarısız ②  S8 · 80,0 + 6,5  = 86,5 s = 1:26
     her şeyin kaybı S9 · 90,0 + 6,0 = 96,0 s = 1:36 ✅ %75-80 bandı
     ikinci seçim S10 · 100,0 + 9,0 = 109,0 s = 1:49
     final vuruşu S11 · 110,0 + 3,0 = 113,0 s = 1:53

FİNAL VURUŞ KANITI [D141]:
   nesne: pirinç sarkaç lambanın gövdesindeki EZİKLER
   saniye: 113,0   ·   kaç tane: 2 (biri eski ve mat, biri yeni ve parlak)
   BULUNAN mı BULUNMAYAN mı: BULUNAN — kadraj dolu, ikisi de sayılabilir
   ⛔ tek karede sayılabilir ve adı konabilir: "iki ezik"
   ffmpeg -ss 113 -i "$M" -frames:v 1 kanit.jpg   → BAK

DÖNGÜ KANITI: ilk kare ↔ son kare KASITLI OLARAK AYNI DEĞİL.
   S0 ilk kare: A kurulumu · EWS · oda · lamba 4°→0° (gösterge DOĞRU)
   S11 son kare: E kurulumu · ECU · lamba · 3° eğik, iki ezik (gösterge YALAN)
   Bu bir DÖNGÜ değil, bilinçli KAPANIŞ KONTRASTIDIR [ACI_YAYI §9].
   Kabul ölçütü: iki kare yan yana konduğunda "aynı lamba, artık düşeyde
   değil" tek bakışta okunuyor mu.
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 - 1 1 1 1 - 1 1
       S0 S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 S11
       (1 = insan var · - = insansız)
       insanlı 10 · insansız 2 → S4 ve S9, ikisi de novumun kanıt sahnesi
       ⛔ S11'de kadın KADRAJDADIR ama odak dışıdır ve hiç hareket etmez;
         şeritte 1 sayılır.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 12 sahnenin 10'unda · 2'sinde 0 (S4 · S9)
              mürettebat 0 · pilot 0 · yansıma 0 · ayna 0 kare
KASK          ⛔ YOK — 0 kare. Basınçlı kabin, kısa kollu.
              D5 · D79 · KART 3 bu filmde YAPISAL OLARAK TETİKLENEMEZ.
              ⚠️ prompt_kontrol'ün D79 kapısı bu SPEC ve PLAN metnindeki
              "kask/vizör" kelimelerini görüp yanlış pozitif verir; bölüm
              dosyalarında dizge 0 kez geçer.
NOVUM         Bu gemide "aşağı" zemin değildir, sürücünün ittiği yöndür.
              İHLALİ: tavandan sarkan pirinç lamba düşeyde durmaz — sancak
              penceresine doğru sabit açıda, kordonu gergin, SALLANMADAN
              asılı kalır. İhlal sayısı: 1 (maya eşiği).
              TAŞIYICI: pirinç sarkaç lamba × kadının onu eliyle düşeye
              itip bırakması. 6 sahnede: S0 · S4 · S5 · S7 · S9 · S11.
YERÇEKİMİ     ağırlık YALNIZ itkiden gelir. Sıfır-g 0 kare (D23 elenir).
              seyir 2,45 m/s² (0,250 g) · dar kesme 2,64 (0,269 g) ·
              içeriden kesme 6,55 (0,667 g — seyrin 2,67 katı)
YATMA AÇILARI S0 4°→0° · S1 0° · S2 0° · S3 0° · S4 0°→4° · S5 4°→22° ·
              S6 22°(el 0°'a iter, geri döner) · S7 22°→68° · S8 68° ·
              S9 68°→3° · S10 4° · S11 3°
              θ = arctan(yanal itki / eksenel itki) — her değer doğrulandı
DÜŞME SAYILARI 1,20 m'den: seyirde 1,0 s · 68°'de 0,61 s
              S4 · 4°  : anahtar 8 cm screen-right kayar (~1,5 s), durur
              S8 · 68° : anahtar göğüs hizasından, camdan 2,0 m uzakta;
                         cama 0,8 s'de ulaşır, yolda 0,8 m alçalır
              ⛔ Serbest cisim ASILI KALMAZ, süzülmez, yön değiştirmez [D127]
ATMOSFER      içeride basınçlı ve solunabilir · dışarıda vakum (§3.1)
              toz 0 kare · duman 0 kare · alev 0 kare · rüzgâr 0 kare ·
              sıvı 0 kare · canlı 0 kare · egzoz kadrajda 0 kare
EKRAN YÖNÜ    kamera 12 sahnenin 12'sinde salonun İÇİNDE ve KIÇTAN PRUVAYA
              bakar. Kıça bakan kurulum: 0.
              SANCAK penceresi 12/12 SCREEN-RIGHT · İSKELE duvarı 12/12
              SCREEN-LEFT · yatma 12/12 SCREEN-RIGHT'a · ters dönüş 0
SAYAÇ         ⭐ MONOTONİK: sarkacın DİNLENME açısı 0° → 0° → 0° → 3°.
              Geri dönmez. (S0-S3 dinlenme 0° · S9'dan sonra 3°)
              İKİNCİ KANAL (monotonik değil, kalıcı kayıplı):
              masadaki gevşek eşya 6 → 6 → 5 → 3 → 0 → 4; iki eşya
              kanepenin altında KALICI olarak kayıp
              ÜÇÜNCÜ KANAL: pruva camındaki halkalı varış — S3 nokta,
              S6 biraz büyük, S11 okunur disk. Metin 0, rakam 0.
EŞ KADRAJ     S2 ↔ S6 ↔ S9  (B kurulumu · 50mm · MS · profil · h1,10 · 3,0m)
              ⛔ D153: S6 ve S9'un imajları S2'nin ONAYLI karesinden
              image-edit ile türetilir, ≤3 maddelik fark listesiyle.
              Fark listeleri bölüm dosyalarının sahne kartlarında yazılı.
YIPRANMA      sabit bölge sayısı 2 [D42]: lambanın gövdesindeki iki ezik.
              ESKİ ezik S2'den itibaren 12 sahnenin hepsinde aynı yerde
              (tepeye yakın, mat, kenarı aşınmış). YENİ ezik S9'dan
              itibaren, eskisinin DÖRT PARMAK altında, parlak katlı.
              Giyside yıpranma 0 — kadın 120 saniye boyunca aynı.
IŞIK TAKVİMİ  MONOTONİK DEĞİL, ROTAYA BAĞLI ve sahne sahne yazılı:
              S0 2900K amber · S1 2900→5600K · S2 6200K mavi-beyaz ·
              S3 6200+2700K · S4 2700K tek kaynak · S5 3400K turuncu ·
              S6 3400→4300K · S7 7000K ince halka + 2700K (EN KARANLIK) ·
              S8 7000K zayıflayan · S9 2700K tek kaynak · S10 5200K gümüş ·
              S11 5200+2700K dengede
              ⛔ 11 ardışık çiftin 11'inde palet DEĞİŞİR. S4 ile S9 aynı
              ışıktadır ve ardışık DEĞİLLERDİR (ikisi de insansız novum
              kanıt sahnesi — bilinçli eş).
SES REGISTER  HUMAN 0 replik · MACHINE 0 replik
              Gövdeden iletilen uğultu ağırlıkla değişir: ince (0,25 g) →
              kalın (0,27 g) → çok kalın ve alçak (0,67 g) → ince (seyir).
              Kordonun pirinç gövdeye tek kuru "tık"ı: S0 · 7,0 s ve
              S11 · 5,0 s — filmin iki ucundaki AYNI ses.
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**

```
KAPI          ⑪ FİLİGRAN / KÖŞE TESTİ — üretici ikonu her karede duruyor mu
KOMUT         bash kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/olcum_kapisi.sh "$M"
DOĞRULANDI    ⬜ master üretilince koşulacak · ffmpeg sürümü kaydedilecek
              ffmpeg -hide_banner -filters | grep -q " crop " || kapıyı yeniden yaz
İKAME         filtre yoksa: her 10 s'de bir kare çıkar, dört köşeyi gözle
              (ffmpeg -ss <t> -i "$M" -frames:v 1 kose_<t>.jpg)

KAPI          KURGU KAPISI — klip/çekim/sahne sayısı ve süre [D70/72/101]
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
DOĞRULANDI    ⬜ master üretilince · beklenen 120,0 s ±2 s
İKAME         yok — ffprobe her kurulumda var

KAPI          KLİP SÜRESİ ÖLÇÜMÜ [D124] — ızgara ARAÇTAN yazılır
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 <ilk test klibi>
DOĞRULANDI    ⬜ İLK TEST KLİBİ ÜRETİLİNCE, PLAN YAZIMINDAN SONRA
              ⛔ Ölçüm 10,0 s'den saparsa bu SPEC'in GRID satırı ve
                yukarıdaki BÜTÜN zaman kodları yeniden türetilir.
İKAME         yok

KAPI          SARKAÇ AÇISI — üretilen karede lamba planın açısında mı
KOMUT         ffmpeg -ss <sahne başlangıcı + 9> -i "$M" -frames:v 1 aci_<S>.jpg
              → karede lambanın kordonu ile düşey arasındaki açı ölçülür
DOĞRULANDI    ⬜ master üretilince · 12 karenin 12'si tek tek
İKAME         gözle: kordonun ekrandaki eğimi masanın kenarıyla
              karşılaştırılır (masa 12/12 sahnede zemine paralel)
              ⛔ KABUL/RET her sahnenin kapı kaydına AYRI yazılır [D154 ②]:
                S3'ün onayı S0/S5/S6'yı KORUMAZ.
```
