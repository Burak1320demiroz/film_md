# 📋 THE_BENT_GRASS — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretir: `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü> <master>`

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh`, `rubrik_paketle.sh` ve
> `rapor_kontrol.py` üçü de bu deseni arar; ad değişirse üçü birden körleşir.

> ⛔ **DİKEY FİLMSE `## 🎬 SAHNE SPESİFİKASYONU` BAŞLIĞI ZORUNLUDUR**
> (08.09.2026'da ölçüldü). `rubrik_paketle.sh` filmin ailesini TEK bir satırla
> tespit ediyor:
> `AILE="yatay"; grep -qE "^## .*SAHNE SPESİFİKASYONU" "$SPEC" && AILE="dikey"`
> Başlık yoksa dikey film **YATAY sanılır** ve paket her merceğe YANLIŞ bloğu
> verir (① KARE'ye A+B+UYARI yerine A, ④ HİKAYE'ye B yerine A+UYARI…).
> ⚠️ Arıza SESSİZDİR: betik hata vermez, `aile: yatay` yazıp geçer — koşu
> sonunda kimse yanlış belgeyle bakıldığını fark etmez.
> Kontrol: betiğin son satırında `aile: dikey` yazdığını GÖZLE doğrula.
> (Depodaki beş dikey filmin beşi de başlığı taşıyor; risk YENİ filmdedir.)

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON     → A + C BLOĞU                     MOD D  (KART 2 · KART 4 açık)
⑧ 💪 EFOR        → C BLOĞU                          MOD D  (KART 3 açık)
⑨ 🎯 KADRAJ      → B BLOĞU (KURULUM İSKELETİ satırı) MOD D
⑩ 🎭 OYUNCULUK   → A BLOĞU (CENTRAL CHOICE satırı)   MOD D  (0 replikli film)
⑪ 💡 IŞIK        → C BLOĞU (IŞIK TAKVİMİ satırı)     MOD D
⑫ 🪝 HOOK        → A + B BLOĞU                       MOD D  (yayından ÖNCE)
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.

⛔ TESLİM SINIFI [D181]: KURGU (14 klip tek dosyada birleştirilmiş).
   HAM ZİNCİR DEĞİL — ⑨ ⑩ ⑪ ⑫ ham zincire koşulmaz.
⛔ PROMPT UZUNLUK KAYDI [D74 · KILAVUZ_REHBERI §7]: video promptları
   2.908-3.700 karakter. Hedef bant 2.000-2.600'ün ÜSTÜNDE, ölçülmüş tavan
   ~4.300'ün ALTINDA. Aritmetik gerekçe: iki insanlı negatif çekirdek +
   D79 kask/sırt bloğu tek başına 2.153 karakter; bandın üst ucu sahneye
   447 karakter bırakıyor ve bu bir MOTION bloğuna sığmıyor. §5'in kendi
   aritmetik notu bunu "silme gerekçesi değil, BÜTÇE uyarısı" diye
   kaydediyor. Çekirdek KISALTILMADI. Image promptları 4.368-6.799 —
   image bandı depoda ÖLÇÜLMEDİ (gözlemdir, kural değil).

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_BENT_GRASS
FORMAT:            16:9 horizontal · 2-4 dk kartı (§2.2)
RUNTIME:           140,0 seconds (title card: NONE — screen text lock 0,0 s)
SCENE COUNT:       14
THEME:             TIME
                   being temporary is a privilege, and this plain does not
                   grant it
THEME SCENES:      S2 · S8 · S13     (dört gümüş kare · kalkmayan saplar ·
                   aynı iz başka ayak)
INTENDED EMOTION:  quiet dread turning into acceptance — never threat,
                   never rescue. The plain is indifferent, not hostile.
ENDING TYPE:       MUĞLAK / held frame — no closure, no fade, no card
PROTAGONIST:       unnamed suited surveyors, a pair (özel ad promptta geçmez
                   [D34] — bu satırın ilk kelimesi de promptta ARANMAMALIDIR);
                   ayrım dört kanalda: stripe colour+side · height and build ·
                   wrist · carried load
                   ⛔ SIRT SİLUETİ AYRIM KANALI DEĞİL: iki suit de düz sırtlı
CENTRAL CHOICE:    the lead empties the sample case onto the fresh trail and
                   leaves it standing in the grass · S10 (100,0-110,0 s)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
                   ⛔ SESSİZLİK BİR KISITTIR, EKSİK DEĞİL — Diyalog kategorisi
                     N/A yazılır, düşük puan DEĞİL [D113]
SILENT SCENES:     music-free: S11 · S12 · S13 (108,0 s'den sona kadar).
                   ⛔ Müziksiz ≠ sessiz: ortam yatağı 14/14 sahnede sürer [D83]
VIRAL INTERSTITIALS: S4 · S11  ⛔ THESE MAY NOT BE CUT
                   ⛔ KESİLEMEZ SAHNELER (tam liste): S0 (novum taşıyıcısı) ·
                     S4 · S10 (merkezî seçim + bedel) · S11 (doruk + kapak
                     karesi) · S13 (final vuruşu)
TITLE:             "The Grass Here Remembers Every Step" — hafıza vaat ediyor,
                   TEHDİT vaat etmiyor; film de tehdit içermiyor
LIBRARY CONTEXT:   aynı raf: THE_MIRROR_FAUNA (2-4 dk · iki astronot + fauna) ·
                   THE_ROSE_COAT (2-4 dk · iki figür) · THE_UPWARD_FALL
                   (bitki örtülü gezegen yüzeyi).
                   ⭐ Bu film §3.3 DÜNYA ATMOSFERİ kartının İLK filmidir —
                     kartın doğrulanabilir referans filmi yoktu [D74]
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      14
SHOT COUNT:      14 · sahne içi kesme 0
TARGET ASL BAND: 10,0 s (sabit) · ASL CURVE: DÜZ — eğri YOK
                 ⛔ GEREKÇE [D74]: bu format sabit ızgaralıdır (14 × 10,0 s);
                   ASL eğrisi kurgu kırpmasıyla kurulamaz çünkü kırpma
                   bütçesi 0'dır. Ritim eğrisinin yerini ÖRÜNTÜ KIRICI alır
                   (KURGU_RITMI §2): ardışık iki sahne aynı ölçek + palet +
                   ses dokusunda değildir; denetimi kurulum iskeletidir.
GRID:            sahne başlangıcı(n) = 10,0 hook + (n−1) × 10,0 klip
                 → 0 · 10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100 ·
                   110 · 120 · 130   (kesme(n) = 10,0 × n)
RUNTIME:         140,0 s
RAW FOOTAGE:     140,0 s (14 × 10,0) · TRIM BUDGET: 0,0 s
                 ⛔ Kurgu süresi plan süresini AŞAMAZ ve altına da inemez;
                   eksik klip = eksik sahne, fazla süre = tekrar klip [D100]
SCREEN TEXT:     0,0 saniye · title card: NONE · end card: NONE
CAMERA:          14 / 14 sabit lockoff · pan 0 · tilt 0 · zoom 0 · track 0
SETUP SEQUENCE:  A B A A D E D E F F G G B A
KURULUM İSKELETİ: A B A A D E D E F F G G B A  (PLAN ile BİREBİR aynı)
KÜME:            3 küme (≥2 ✅) — S2-S3 · S8-S9 · S10-S11
DÖNÜŞ:           6 / 14 = %42,9 (≥%40 ✅) — S2(←S0) S3(←S2) S6(←S4) S7(←S5)
                 S9(←S8) S11(←S10). S12(←S1) ve S13(←S0) uzak tekrardır ve
                 DÖNÜŞ değil KAFİYE sayılır — ayrı kapı.
ANGLE ARC:       3 açı TİPİ (≥3 ✅) — ALÇAK (A) · GÖZ HİZASI (B·D·E·G) ·
                 YÜKSEK (F)
DORUK:           S11 → 110,0-120,0 s (sahne başlangıcı 110,0 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Yazılan her kayıt formülle DOĞRULANIR; sapma varsa paket TAM DEĞİLDİR.

FİNAL VURUŞ KANITI [D141]:
   AYAKTA DURAN AÇIK BOŞ KASA · 128,0 s · TAM 1 tane · **BULUNAN**
   (aynı karede ayrıca: KAPALI gümüş halka + TAM 3 gövde)
   ⛔ tek karede sayılabilir ve adı konabilir olmalı; "final duygusu" değil
   ffmpeg -ss <saniye> -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: ilk kare (S0 · 0,0 s) ↔ son kare (S13 · 139,x s) — kurulum A ·
   CU · yerden 0,35 m · aynı gümüş iz · aynı ışık tarafı. Değişen TEK
   değişken: basan ayak (insan botu → dört ayaklının ayağı).
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  11111-11111-11--    (1 = insan var · - = insansız · sahne başına bir hane)
       S0 1 · S1 1 · S2 1 · S3 1 · S4 1 · S5 - · S6 1 · S7 1 · S8 1 ·
       S9 1 · S10 1 · S11 1 · S12 - · S13 -
       ⛔ ŞERİT GÖVDE SAYISINI TAŞIMAZ [D135 · THE ROSE COAT]: rubrik yalnız
         "1" üretebilir, "2" üretemez. İki figürlü sahnelerin gövde sayımı
         AYRI satırdadır (C bloğu İNSAN satırı) ve ②'nin appearance table'ından
         okunur. Şeridi "2" ile yazmak kapıyı KOŞULAMAZ hâle getirir.
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         sahne başına TAM sayı — S0:1 · S1:2 · S2:2 · S3:1 · S4:1 ·
              S5:0 · S6:1 · S7:2 · S8:2 · S9:2 · S10:2 · S11:2 · S12:0 ·
              S13:0. Üçüncü figür 0 kare · yansımada 0 · gölgede 0.
KASK          14/14 kapalı · durum değişimi 0 kare · vizör optik berrak,
              0 tint, 0 ayna kaplaması, 0 çevre yansıması · sırt ünitesi
              YOK — İKİ SUITTE DE düz siluet, boyundan kalçaya tek sürekli
              panel [D79 · D139]. Ayrım kanalı sırt DEĞİL, BOY ve OMUZ.
CANLI         dört ayaklı otçul · TAM 4 eklemli bacak · 1 gövde · 2 göz ·
              omuz yüksekliği: ayakta duran kasklı gövdenin biraz üstü ·
              gövde uzunluğu ≈ 1,5 gövde boyu · AĞIZ YOK (tek ihlal) ·
              birey sayısı: S5 hat (sayılmaz) · S7:3 · S11:1 · S12:3 ·
              S13 tek AYAK (gövde 0 kare) · tam gövde ≤2 çekim, toplam ≤6,0 s ·
              yörünge yayı ≤90° (kamera hiç dönmez) · uzuv/göz SAYISI yalnız
              S7 ve sonrasında; S5'te anatomi YAZILMAZ
NOVUM         "Ezilen ot bir daha kalkmaz; ezilen sap gümüşe döner ve o gümüş
              hat sürünün yemek yoludur." İHLAL: ot dalgası kadrajı süpürürken
              ezik hat KIPIRDAMAZ — hareketsizlik novum'un kanıtıdır.
              ⛔ ÖNERME KAPISI: "ezik ot geri kalkmıyor / dalga ile hareket
                etmiyor" bir DEVAMLILIK HATASI DEĞİLDİR, filmin kuralıdır.
YERÇEKİMİ     0,95 g · 1,00 m serbest düşüş ≈ 0,46 s · yürüyüş ≈ 1,35 m/s
              (10 s'de ≈ 13,5 m)
ATMOSFER      0,90 atm solunabilir · +14 °C · nefes buharı 0 kare ·
              yumuşak gölge ve dolgu ışığı MEŞRU [D41] · atmosferik saçılma
              uzak bantta MEŞRU. ⛔ Vakum kilitleri ("mutlak siyah gölge",
              "saçılma yok", "süzülen parçacık yok") BU FİLMDE GEÇERSİZDİR.
EKRAN YÖNÜ    iniş aracı HEP ekran SOLUNDA (14/14) · araç burnu 10 yönünde
              ve iniş sonrası SABİT · gidiş ekran solundan sağına · dönüş
              sağdan sola · sürü eski hat üzerinde sağdan sola · ot dalgası
              14/14 sahnede soldan sağa · güneş 14/14 ekran solunda ·
              gölgeler 14/14 ekran sağına.
              DİZİLİM: kırmızı şeritli figür HEP ekran solunda, mavi şeritli
              figür HEP ekran sağında — sıra 14/14 sahnede aynı [D86]
SAYAÇ         ⭐ ÜÇ KANAL, üçü de MONOTONİK ve METİNSİZ:
              ① GÜMÜŞ HAT: S1 tek düz hat → S6 hat + dolu kasa → S9 iki hat
                (eski soluk + yeni parlak) → S12 KAPALI HALKA. Hiç kısalmaz.
                ⛔ Sayacın İKİ UCU her sayaç karesinde birlikte görünür:
                  ezik gümüş hat + ufka kadar ezilmemiş altın ova [D78]
              ② SÜRÜ MESAFESİ: S5 ufuk (~400 m) → S7 orta bant (~90 m) →
                S11 bir gövde boyu. Yalnız yaklaşır.
              ③ IŞIK: gölge boyu S0'da gövdenin ~1,5 katı → S13'te ~3 katı.
              ⛔ Rapor "no counter present" yazarsa bu bir ÖLÇÜM BOŞLUĞUDUR,
                bulgu değil [D134].
EŞ KADRAJ     S0 ↔ S13 (kafiye · kurulum A · değişen TEK değişken: basan ayak)
              S1 ↔ S12 (kafiye · kurulum B · değişen tek şey: düz hat → halka)
YIPRANMA      3 kademe · TEK YÖNLÜ · sabit bölge sayısı 2→4 [D42·D147]:
              K0 (S0-S3) temiz · K1 (S4-S9) diz + manşet · K2 (S10-S13)
              diz + manşet + göğüs + önkol. Geri dönüş 0 kare; kademe
              değişimi SAHNE SINIRINDA, klip içinde değil.
IŞIK TAKVİMİ  MONOTONİK ✅ — güneş yüksekliği S0 32,0° → S13 20,3°, sahne
              başına −0,9°. Prompt gövdesinde DERECE yazılmaz [D138];
              gölge uzunluğu gövde boyuna göre yazılır.
SES REGISTER  HUMAN 0 · MACHINE 0 (replik yok)
              ORTAM YATAĞI: kuru ot hışırtısı (sürekli zemin) · rüzgâr ·
              giysi kumaşı · suit fanı · nefes — kurguda TEK PARÇA [D83]
              MÜZİK: 72 BPM · 0-108,0 s · 108,0 s'de KESİLİR (fade yok) ·
              108,0-140,0 s müzik 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı.

```
KAPI ①        SÜRE VE IZGARA — teslim 140,0 s mi, kesmeler 10,0 s katı mı
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
              ffmpeg -i "$M" -vf "select='gt(scene,0.3)',showinfo" -f null - 2>&1 \
                | grep -oE "pts_time:[0-9.]+"
DOĞRULANDI    ffprobe/ffmpeg 8.1 · 09.09.2026 · `select` ve `showinfo` filtreleri
              kuru koşuyla listede görüldü
İKAME         scene tespiti kaçırırsa: ffmpeg -i "$M" -vf "scdet=threshold=10" \
              -f null -  (scdet 8.1'de KURULU — doğrulandı)

KAPI ②        EKRAN METNİ VE KUYRUK KARTI — 0,0 s olmalı
KOMUT         ffmpeg -sseof -3 -i "$M" -frames:v 1 son_kare.jpg   → GÖZLE BAK
              ffmpeg -i "$M" -vf "freezedetect=n=-60dB:d=2" -f null - 2>&1 \
                | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 09.09.2026 · `freezedetect` listede
İKAME         yok — kart varsa donuk kare olarak görünür; ayrıca ilk/son
              kare gözle kontrol edilir (ölçüm değil GÖZ kapısı)

KAPI ③        SES YATAĞI — 108,0-140,0 s müziksizdir ama SESSİZ DEĞİLDİR
KOMUT         ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 \
                | grep silence_
DOĞRULANDI    ffmpeg 8.1 · 09.09.2026 · `silencedetect` listede
İKAME         yok. ⛔ 108-140 s aralığında sessizlik aralığı ÇIKARSA yatak
              serilmemiştir [D83] — teslim kusuru, rapor bulgusu değil

KAPI ④        İHRAÇ SESİ — −14 LUFS · tepe ≤ −1,0 dBTP
KOMUT         ffmpeg -i "$M" -af ebur128=peak=true -f null - 2>&1 | tail -20
DOĞRULANDI    ffmpeg 8.1 · 09.09.2026 · `ebur128` listede
İKAME         yok

KAPI ⑤        FİLİGRAN VE KÖŞE — üretici damgası 0 kare [D150]
KOMUT         for t in 0 30 60 90 120 139; do ffmpeg -ss $t -i "$M" \
                -frames:v 1 kose_$t.png; done   → dört köşeye GÖZLE BAK
DOĞRULANDI    ffmpeg 8.1 · 09.09.2026 · kare çıkarma, filtre gerektirmez
İKAME         yok — bu bir GÖZ kapısıdır; THE UPWARD FALL'da sekiz merceğin
              sekizi de 225/225 saniye süren filigranı kaçırdı

KAPI ⑥        KAMERA SABİTLİĞİ — 14/14 lockoff
KOMUT         ⛔ `vidstabdetect` BU MAKİNEDE KURULU DEĞİL — kuru koşu ile
              doğrulandı (ffmpeg 8.1 · 09.09.2026 · grep sonucu 0).
              Bu kapı vidstab'a YAZILMAZ [D142].
İKAME         cropdetect ile kadraj kaymasını ölç:
              ffmpeg -i "$M" -vf "cropdetect=limit=0:round=2:reset=1" -f null - 2>&1 \
                | grep -oE "crop=[0-9:]+" | sort -u
              → tek bir crop değeri dönmelidir; birden fazla değer kadrajın
                oynadığını gösterir. (cropdetect 8.1'de KURULU — doğrulandı)

KAPI ⑦        DÖNGÜ KANITI — ilk kare ↔ son kare
KOMUT         ffmpeg -i "$M" -frames:v 1 ilk.jpg
              ffmpeg -sseof -1 -i "$M" -frames:v 1 son.jpg   → YAN YANA BAK
DOĞRULANDI    ffmpeg 8.1 · 09.09.2026 · kare çıkarma
İKAME         yok. Aranan: aynı kurulum (A) · aynı ölçek · aynı ışık tarafı ·
              aynı gümüş iz — değişen TEK şey basan ayak.
              ⛔ THE UPWARD FALL'da jest tuttu, DÜNYA tutmadı: iki kare iki
                ayrı ormandaydı. Burada ORTAM da kilitlidir.
```
