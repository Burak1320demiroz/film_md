# 🎬 THE LEANING ROOM — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarındadır.

```
FORMAT:        yatay 2-4 dk (16:9)
ORTAM:         KILAVUZ_REHBERI §3.5 — VAKUM + İTKİ YERÇEKİMİ, kabin İÇİ dalı
               (§3.1 vakum kuralları dışarıda aynen geçerli; içeride
                ağırlık YALNIZ itkiden gelir → D23 tetiklenemez)
TÜR:           bilimkurgu  (§4.1 — tek açık dal)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLMEDİ [D124]. Izgara format kartı §2.2'nin
               10,0 s'i varsayılarak yazıldı (10 s → Veo 8 s + 2 s extend).
               ⛔ İlk test klibi üretilince ÖLÇ ve sapma varsa QA_SPEC'in
                 GRID satırı ile bütün zaman kodlarını yeniden türet:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <klip>
SAHNE SAYISI:  12        RUNTIME: 10 + 11 × 10 = 120 s (2:00)
LOGLINE:       Kütlelerin arasından geçen lüks bir geminin salonunda, tavandan
               sarkan pirinç bir lamba "aşağı"nın nerede olduğunu söyler; ve
               gemiyi eliyle süren kadın her yakın geçişte odayı biraz daha
               yatırır.
```

---

## 🎭 TEMA

```
TEMA: ENTROPİ
      — Bir oda bir kez düzeltilir; ikinci kez tam düzelmez.

MOTİF SAHNELERİ: S2 · S8 · S10 · S11
      S2  nesne     : oda kusursuz kare — masanın kenarı zemine paralel,
                      altı gevşek eşya masada, sarkaç düşeyde
      S8  nesne     : altı eşyanın altısı sancak korkuluğunda; masa boş
                      (⛔ B2'nin BEDEL sahnesi — B3 çapraz okuması ✅)
      S10 kinesik   : kadın eşyaları eliyle geri koyar — dördünü koyabilir,
                      ikisi kanepenin altında kalır; sarkacı düzeltmez
      S11 nesne+ışık: seyir ışığı geri gelir, oda düz görünür,
                      sarkaç 3° eğik durur
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          fiziksel yasa  (§1 birinci tercih)

NOVUM:               Bu gemide "aşağı" zemin değildir, sürücünün ittiği yöndür.
                     Dönmek yana itmektir; yana itmek odayı yatırmaktır.

NOVUM TAŞIYICISI:    tavandan sarkan pirinç sarkaç lamba × kadının onu eliyle
                     düşeye itip bırakması → lamba düşeye DÖNMEZ, sancak
                     penceresine doğru sabit açıda ve kordonu GERGİN durur;
                     sallanmaz, salınmaz, geri gelmez

TEK KARE (§4①):      Donmuş TEK KAREde tavandan sarkan pirinç sarkaç lamba
                     düşeyde değildir: kordonu gergin, sancak penceresine
                     doğru 68° eğik ve hareketsizdir — masa ile zemin ise
                     birbirine dik ve kusursuz düzdür.
                     ✅ D157①: kare, §2'nin taşıyıcı NESNESİNİ içeriyor.
                     ✅ D157②: taşıyıcı ECU kurulumunda (E) kadrajın tamamı,
                        EWS kurulumunda (A) merkez üçte biri; değişim TEK
                        KLİP içinde olur (S0 · S4 · S5 · S7 · S9 · S11).
                     ✅ D157③: taşıyıcının kanıt sahnelerinde (S4 · S9)
                        kadrajda başka HİÇBİR ŞEY hareket etmez.

KİNETİK BAĞIMSIZLIK: ✅ Kural replik, dış ses ve ekran metni olmadan üç
                     kanaldan kanıtlanır: lambanın açısı · bırakılan pirinç
                     anahtarın izlediği yol · kadının koltuğa çöküşü ve
                     kemerin gerginliği. Filmde 0 replik, 0 ekran, 0 gösterge.

BAŞLIK ŞEMASI:       THE LEANING ROOM (3 kelime) — izleyiciye nereye bakacağını
                     söyler: ODAYA. ✅ (§1 paketleme kapısında ikinci kez koşar)

MAYA EŞİĞİ (§3):     KABUK tanıdık: salon, koltuk, masa, lamba, dümen.
                     İHLAL SAYISI: 1. "Aşağı"nın yön değiştirmesi dışında
                     her şey normal fizikle davranır — ve ihlalin kanıtı,
                     yanındaki normalin kusursuz çalışmasıdır.

KURAL TEKRARI (§5):  KURULUM   S0 (lamba 4° → 0°) · S4 (0° → 4°, ikinci
                               nesne: masadaki anahtar 8 cm kayar)
                     DOĞRULAMA S5 (22°) · S6 (el iter, geri döner)
                     SONUÇ     S7-S8 (68°; anahtar avuçtan cama gider) ·
                               S9 (taşıyıcının kendisi ezilir)
                     TOPLAM    6 sahne · 3 farklı nesne (lamba · anahtar ·
                               kadının kendi ağırlığı)  ✅ ≥3 sahne, ≥2 nesne
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR

```
⏭️ UYGULANMAZ — bu film YATAY 2-4 dk. (KILAVUZ_REHBERI §2.1 yalnız dikey.)
   Bilgi asimetrisi satırı yatayda opsiyoneldir ve bilinçli kararı: YOK.
   Sebep: hook'un işi bilgi vermek değil, tek bir yanlış açıyı göstermek.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2.2)

| # | vuruş | % | sahne | not |
|---|---|---|---|---|
| 1 | Açılış imajı | 0-8 | S0 | kapanış imajıyla ÇİFT tasarlandı (§2.3③) |
| 2 | Kurulum | 0-17 | S0-S1 | oda + kadının yetkinliği (dümeni bilen el) |
| 3 | Katalizör | ~11 | S1 · 0:13 | ilk kütle sancakta belirir ✅ ≤0:15 |
| 4 | Tartışma | 17-33 | S2-S3 | geniş hat mı dar hat mı — dümeni bir parmak çevirir |
| 5 | Orta nokta (sahte yenilgi) | ~50 | S6 | lambayı eliyle düşeye iter, TUTMAZ |
| 6 | Umut-önce-düşüş | 58 | S7 · 0-3 s | dar çizgi tutuyor gibi görünür |
| 7 | Merkezi seçim | 58-67 | S7 | dümeni sonuna kadar açar |
| 8 | Her Şeyin Kaybı | ~75 | S9 · 1:30 | taşıyıcının kendisi ezilir, 3° geri gelmez |
| 9 | Final | 83-100 | S10-S11 | ikinci seçim: geniş hat |
| 10 | Kapanış imajı | 100 | S11 | iki ezik yan yana |

```
§2.3 ÜÇ SERT KURAL
① KAMERA-TAŞIYICI TESTİ: "kadını dronla değiştirsek ne kaybolur?"
   → S6 kaybolur tamamen (bir şeyi eliyle düz tutmaya çalışmak), S7'de
     seçim kaybolur (dron dar hattı seçmez, hesaplar), S10'da eşyaları
     eliyle geri koyma jesti kaybolur. Üç sahne yalnız İNSANLA var.
② SEÇİMİN BEDELİ NESNEDİR, CÜMLE DEĞİL: kaybedilen şey kadrajda görünür —
   sancak korkuluğundaki iki eşya (geri konamayan) + lambadaki yeni ezik.
③ AÇILIŞ-KAPANIŞ ÇİFTİ: S0 = oda, lamba düşeyde. S11 = lamba, 3° eğik ve
   iki ezikli. Yan yana konduğunda değişim tek bakışta okunur.
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       görsel anomali — düşeyde olmayan bir sarkaç
S0 SORUSU:       "Neden o lamba düşeyde değil ve neden odadaki kadın
                  buna bakmıyor bile?"
S1 İKİNCİ BİLGİ: oda hareket ediyor · bir yol var · ve yolu bu kadın
                 ELİYLE sürüyor (dümen masaya gömülü, pirinç, ekransız)
İLK 2 SN SESİ:   diegetik TEK ses — gövdeden iletilen alçak uğultu +
                 lamba kordonunun pirinç gövdeye tek kuru "tık"ı.
                 ⛔ 0:00-0:02 arasında müzik YOK (erken giriş elendi).
0. KARE:         örüntü kesintisi = ceviz-pirinç bir salon + yanlış açıda
                 asılı bir lamba · süren hareket = sancak penceresinde
                 kayan yıldız alanı
                 ⬜ 120 px testi MAKİNEYLE koşulacak (ilk kare üretilince)
İHLAL GÖRÜNÜRLÜĞÜ: 0. karede zaten kadrajda (ONERME §6: 0-3 sn bandı) ✅
REVEAL İKİLİ KİLİT [D71]: saklanan şey ihlal DEĞİL, ihlalin SEBEBİDİR —
                 lamba 0. karede eğik, sebebi (kadının dönüşü) S3'te görünür
BİLGİ ASİMETRİSİ: YOK (bilinçli karar)
```

## 🏁 FİNAL  (`FINAL_VE_PAYLASIM_KILAVUZU.md` §2-§3)

```
FİNAL TİPİ:  MUĞLAK — görsel ikilem: oda düzeldi, gösterge düzelmedi.
             İzleyici "bir dahaki kütlede yine dar hattı seçer mi" sorusuyla
             kalır ve cevabı film vermez. (2-4 dk kartı: TWIST veya MUĞLAK.)

TOHUM BİLGİ: S2 · 0:22-0:24 (filmin %18'i — pencere 15-22 s, bir tık geç
             ama S2'nin ilk yarısında) — lambanın pirinç gövdesinde, tepeye
             yakın, ESKİ ve solmuş bir ezik. Ekranda ≤2 s, kadının bakışıyla
             VURGULANMAZ, ışık onu yalnızca yalar.
             GERİ DÖNÜŞ: S11 tam o eziğe döner ve yanında YENİSİ vardır.
             ⭐ Tohumun anlamı: bunu daha önce de yaptı. Final "bir kez
               bozdu" değil, "her seferinde bozuyor" der.

PAYLAŞILAN DUYGU: HUŞU (kaygı değil) — §5: ikisinin arası tutmuyor.
             Taşıyıcısı S7'nin ölçek kontrastı ve S11'in sessizliği.
```

## 🖼️ KAPAK ANI  (`PAKETLEME_VE_VAAT_KILAVUZU.md` §1)

```
KAPAK ANI = S7 · 1:18 — oda 68°'de. Tavandan sarkan pirinç lamba neredeyse
yatay, kordonu gergin; masanın üstü boş; sancak camının ötesinde kusursuz
siyah bir daire ve çevresinde ince bir ışık halkası.
   ⛔ Saat HESAPLATILDI [D122]: S7 başlangıcı = 10 + 6 × 10 = 70,0 s ·
     promptun TIMELINE ofseti 8,0 s → 78,0 s = 1:18.
⬜ 120 px testi: eşik boyutunda okunması gereken tek şey "her şey tek yöne
   yatmış bir oda + siyah bir daire". ⛔ MAKİNEYLE koşulacak (kapak dosyası).
Ayrıntı ve Plan B: `THE_LEANING_ROOM_KAPAK.md`
```

---

## 🗺️ SAHNE HARİTASI

> Kamera sütunu: vuruş→açı `KAMERA_ACISI §3` · diziliş `ACI_YAYI §3-4`.
> **Uygulanan sıçrama okuması:** ardışık her çiftte ölçekte ≥1 tam kademe
> DEĞİŞİR **ve** AÇI TİPİ (§2 sekizlisi) değişir. `ACI_YAYI §3`'ün kendi
> örneği ("göz hizası MS → alt açı CU") tam olarak bu okumadır; kamera
> salonun içinde kaldığı için azimut yayı fiziksel olarak dardır ve
> ayrım YÜKSEKLİK + AÇI TİPİ + ÖLÇEK ile kurulur [D74 gerekçe satırı].

| S | zaman | başlık | olay | kurulum (lens · ölçek · açı tipi) | palet | ses dokusu | bütçe |
|---|---|---|---|---|---|---|---|
| S0 | 0:00 | THE ROOM AT CRUISE | Lamba 4°'de açılır; 7 s'de düşeye döner ve DURUR. Kadın odayı geçip koltuğa oturur, eli dümene iner. | **A** 24mm · EWS · göz hizası · h 1,20 m · 6,4 m | 2900 K amber, alçak | uğultu ince (0,25 g) + tek tık | 🚶 yürüyüş · açılış imajı |
| S1 | 0:10 | THE FIRST MASS | 0:13 sancakta buz dünyası belirir. Lamba 0°'de KALIR — hat geniş. | **D** 28mm · WS · üst açı · h 2,25 m · 5,2 m | amber→soğuk kenar | uğultu sabit | 🔁 tepki planı · katalizör |
| S2 | 0:20 | THE ROOM IS SQUARE | Kadın profilden, buz dünyası pencereyi doldurur. **TOHUM:** lambada eski ezik, 2 s. | **B** 50mm · MS · profil · h 1,10 m · 3,0 m | 6200 K mavi-beyaz, yatay sert | uğultu + nefes | 👁️ göz · 🔁 tepki · **TEMA** |
| S3 | 0:30 | THE ROAD | Omuz üstünden pruva camı: ileride, merkezden kaçık, halkalı soluk bir nokta. Dümeni bir parmak çevirir. | **F** 50mm · CU · omuz üstü · h 1,15 m · 1,1 m | soğuk düşer + lamba havuzu | uğultu perdesi bir ton | ✋ el · varış sayacı ① |
| S4 | 0:40 | THE LAMP ANSWERS | **İNSANSIZ · viral ara ①.** Lamba 0°→4°, DURUR. Masadaki anahtar 8 cm screen-right kayar, durur. | **E** 85mm · ECU · göz hizası · h 1,05 m · 2,1 m | tek kaynak: 2700 K lamba havuzu | uğultu + kordon gerilmesi | **NOVUM KURULUM** |
| S5 | 0:50 | THE TIGHT CUT | Turuncu toz dünyası. Dümeni açar; lamba 22°'ye gider. Masadan bir eşya kayar. | **F** 50mm · CU · omuz üstü · h 1,15 m · 1,1 m | 3400 K turuncu, geniş | uğultu kalınlaşır (0,27 g) | ✋ el · bahis |
| S6 | 1:00 | SHE HOLDS IT TRUE | **BAŞARISIZ DENEME ①.** Ayağa kalkar, lambayı eliyle düşeye iter, 3 s tutar. Bırakır: 0,9 s'de 22°'ye döner. Anahtarı avucuna alır. | **B** 50mm · MS · profil · h 1,10 m · 3,0 m | turuncu nötrleşir | ⛔ müzik SUSAR · yalnız nefes | 👁️ göz · 🔁 tepki · 🎒 eşya |
| S7 | 1:10 | THE INSIDE LINE | ⚡**ŞOK #1** · **MERKEZİ SEÇİM:** dümeni sonuna açar. Lamba 22°→68°. Oda yatar. Camın ötesinde siyah daire + ince halka. | **A** 24mm · EWS · göz hizası · h 1,20 m · 6,4 m | 7000 K ince halka + eğik 2700 K havuz — filmin EN KARANLIK sahnesi | uğultu kalın (0,67 g) + deri | 🌌 ölçek 1:10 · **KAPAK ANI** |
| S8 | 1:20 | EVERYTHING GOES TO THE GLASS | Anahtar avuçtan çıkar, 2,0 m'yi 0,8 s'de geçer, cama yaslanır. Altı eşya sancak korkuluğunda. **BAŞARISIZ DENEME ②:** toplamaya uzanır, geri kayarlar. | **C** 35mm · WS · alt açı · h 0,42 m · 4,6 m | 7000 K halka gerilerken | cam üstünde kuru pirinç | **BEDEL GÖRÜNÜR · TEMA** |
| S9 | 1:30 | THE CREASE | **İNSANSIZ · viral ara ②.** S2/S6'nın aynı profil kadrajı, koltuk BOŞ. Lamba seyre döner ama 3°'de durur. Gövdesinde yeni parlak ezik, eskisinin dört parmak altında. | **B** 50mm · MS · profil · h 1,10 m · 3,0 m | yalnız 2700 K lamba havuzu | ⛔ müzik YOK · kadraj dışı tek nefes | **HER ŞEYİN KAYBI** |
| S10 | 1:40 | SHE PUTS THEM BACK | **İKİNCİ SEÇİM:** ileride üçüncü kütle; dümeni açmaz, geniş hattı sürer (lamba 4°). Eşyaları eliyle geri koyar — dördü masaya, ikisi kanepenin altında kalır. Sarkaca dokunmaz. | **F** 50mm · CU · omuz üstü · h 1,15 m · 1,1 m | 5200 K gümüş, geniş, yumuşak | uğultu ince geri gelir | ✋ el · 🔁 tepki · **TEMA** |
| S11 | 1:50 | THE TWO CREASES | **KAPANIŞ.** Seyir. Pruva camında halkalı varış dünyası artık okunur bir disk. Lamba tam kadrajda: 3° eğik, iki ezik yan yana. Kadın arkada, odaklanmamış, kımıltısız. | **E** 85mm · ECU · göz hizası · h 1,05 m · 2,1 m | 5200 K gümüş + 2700 K amber dengede | uğultu + tek tık (S0'ın aynısı) | 🌌 kapanış imajı · **TEMA** |

```
AÇI TİPİ SAYISI: 5 ≥3 ✅  — göz hizası (A·E) · üst açı (D) · profil (B) ·
                 omuz üstü (F) · alt açı (C)
KURULUM SAYISI:  6  (bant: 12 sahnede en fazla 6) ✅
                 A×2 (S0·S7) · B×3 (S2·S6·S9) · C×1 (S8) · D×1 (S1) ·
                 E×2 (S4·S11) · F×3 (S3·S5·S10)
İSKELET TEKRARI: F-E-F (S3-S4-S5) · B-A-C-B (S6-S7-S8-S9) — A-B-A ritmi
ŞOK BANDI:       1 adet (bant ≤2) — S6→S7, MS→EWS (2 kademe), merkezi seçim
BÖLÜM KESİĞİ:    S5 ile S6 arasında — CU(F) → MS(B): 1 kademe + açı tipi
                 değişimi (omuz üstü → profil) ✅ ardışık çift kuralı sağlanır
ÖRÜNTÜ KIRICI [KURGU_RITMI §2]: 11 ardışık çiftin 11'inde ÖLÇEK değişir,
                 11'inde PALET değişir, 11'inde SES DOKUSU değişir. Üçünün
                 üçü birden sabit kalan tek çift yoktur.
MAKRO KIRICI (her 3-4 sahnede tempo/mekân): S4 (insansız insert) ·
                 S7 (şok + karanlık) · S9 (insansız + sessizlik)
```

### 🔁 KULESHOV DÖNGÜLERİ (`KARAKTER_VE_DUYGU §8` madde 5 — 120 s'de ≥4)

```
① S3 (o + yol) → S4 (yalnız lamba) → S5 (o + yol)          A-B-A
② S6 (o)       → S7 (oda + siyah daire) → S8 (o, alçaktan)  A-B-A
③ S8 (o)       → S9 (boş koltuk + lamba) → S10 (o + yol)    A-B-A
④ S1 (o, üstten) → S2 (o, profilde buz dünyasına bakar) → S3 (baktığı şey)
   ⚠️ ④ klasik A-B-A değil, bakış→nesne zinciridir; dönüş planı S5'tedir.
   Her döngünün dönüş planı ≥2 s (klip 10 s, sahne=çekim).
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** sabittir ve her görsel promptuna TAM
> yazılır (kural ③: prompt self-contained · "BIBLE'a bak" atfı YASAK).
>
> ⛔ Bu dosyada prompt YOKTUR. Aşağıdaki bloklar sahne promptlarına
> KOPYALANAN kaynak metinlerdir; başlıkları bilerek prompt başlığı biçiminde
> DEĞİLDİR (kapı betiği başlıktan prompt sayar).

### 👤 Character Bible  (kelimesi kelimesine — 12 sahnenin 12'sinde)

```
A woman in her late thirties, tall and square-shouldered, brown skin, black
hair drawn back into a low flat knot at the nape with no loose strands. High
cheekbones, a straight nose, a wide mouth, a matte dark red on the lips and no
other makeup. She wears a long charcoal wool coat-dress, single-breasted, cut
to the ankle, buttoned to the collarbone, with a narrow standing collar; the
wool has a visible flat weave and no pattern of any kind. The sleeves are
pushed back to the elbow and her forearms are bare. On her left wrist a plain
wide band of brushed brass with no face and no dial. Flat black leather shoes.
The back of the coat-dress is one continuous panel of charcoal wool from
collar to hem, unbroken, carrying nothing. Her hands are bare, the nails short
and unpainted. She is calm and unhurried in every frame; she is working, not
enduring.
```

```
⛔ D155 KİLİDİ: gövdede BÜYÜK HARFLİ dizge ve kısaltma YOK. "coat-dress"
   yazılır, kısaltma yazılmaz — büyük harfli kısa dizge giysinin üstüne
   BASKI olarak çizilir.
⛔ D34/D45: özel ad YOK. Kadının adı hiçbir dosyada geçmez.
⛔ MİLLİYET YOK: "brown skin" fiziksel tariftir, uyruk değildir.
⭐ D139 KARŞILIĞI: sırt cümlesi POZİTİFTİR ve omuz üstü kurulumunda (F —
   S3 · S5 · S10) prompta AYNEN girer. Bu filmde kask/skafandr yoktur,
   ama boş sırt yüzeyi riski aynıdır: model boş sırtı DOLDURUR.
```

### 🌍 World Bible

```
Kabin: özel uzun menzilli bir yatın SALONU. 7,0 m uzun, 4,4 m geniş, 2,5 m
yüksek. Duvarlar mat ceviz kaplama; zemin koyu dokuma. Alçak bir masa, tek
bir derin koltuk, bir kanepe, gömme raflar.

İKİ CAM:
  · PRUVA CAMI — salonun ön duvarı, kavisli, alçak ve enli bir şerit.
    YOL burada görünür: gidilecek yön.
  · SANCAK BANT PENCERESİ — salonun sağ duvarı boyunca uzanan uzun bir
    bant. GEÇEN KÜTLELER burada görünür.

DÜMEN: masanın kenarına gömülü pirinç bir el çarkı ve tek sıra işaretsiz
pirinç kol. ⛔ GEMİDE HİÇBİR EKRAN, GÖSTERGE, KADRAN VEYA SAYAÇ YOKTUR.
Bilgi taşıyan tek şey sarkacın açısıdır.

SARKAÇ LAMBA: tavan rayından sarkan, örgü kordonlu, ağır pirinç gövdeli tek
bir lamba; abajur mat pirinç ve KAPALIDIR — masaya keskin kenarlı bir havuz
düşürür, hale yapmaz. Gövdesinde bir ESKİ ezik vardır (tohum, S2) ve S9'da
bir YENİ ezik alır.

ALTI GEVŞEK EŞYA (masada, S0'da): deri etiketli pirinç bir anahtar · düz bir
nehir taşı · katlanmış koyu bir gözlük · sarılmış kömür grisi yün bir atkı ·
erik büyüklüğünde som pirinç bir küre · boş sığ bir pirinç tabak.
⛔ AYNA YOK (Kart 4: yansıma ikinci figür üretir) · SIVI YOK · CANLI YOK ·
   KİTAP/KAĞIT/ETİKET YOK (D138 metin riski).

DIŞARISI: vakum (§3.1). Toz 0 kare · duman 0 kare · alev 0 kare ·
rüzgâr 0 kare. Gölgeler mutlak siyah ve jilet keskin. Küresel lens —
yatay anamorfik parlama YASAK, vakumda fiziksel olarak yanlış.
```

### 🎥 Camera Bible

```
KLİP İÇİ: 12 sahnenin 12'sinde SABİT LOCKOFF. Kamera hiç hareket etmez —
zoom yok, pan yok, tilt yok, track yok, sarsıntı yok, kesme yok. [KART 8]

⛔ EKRAN YÖNÜ KİLİDİ — 12 sahnenin 12'sinde geçerli, İSTİSNASIZ:
   · Kamera HER ZAMAN salonun İÇİNDEDİR ve KIÇTAN PRUVAYA doğru bakar.
     Hiçbir kurulum kıça bakmaz — ekran yönü hiçbir sahnede çevrilmez.
   · SANCAK bant penceresi HER kadrajda SCREEN-RIGHT'tadır.
   · İSKELE ceviz duvarı HER kadrajda SCREEN-LEFT'tedir.
   · PRUVA camı kadrajın DERİNLİĞİNDEDİR.
   · YATMA HER ZAMAN SCREEN-RIGHT'a doğrudur. Serbest kalan her cisim
     SCREEN-RIGHT'a gider. Ters dönüş YOKTUR.
   · Kadın otururken yüzü SCREEN-RIGHT'a dönüktür (geçen kütleye bakar).

ALTI KURULUM (yükseklik = salon zemininden):
  A  24mm · EWS · göz hizası      · h 1,20 m · 6,4 m · kıç-iskele köşesi
  B  50mm · MS  · profil          · h 1,10 m · 3,0 m · kıç, orta hat
  C  35mm · WS  · alt açı (+10°)  · h 0,42 m · 4,6 m · kıç, 1,2 m iskeleye
  D  28mm · WS  · üst açı (−28°)  · h 2,25 m · 5,2 m · kıç perdesi, 1,4 m sancağa
  E  85mm · ECU · göz hizası      · h 1,05 m · 2,1 m · 1,6 m iskeleye, lambaya
  F  50mm · CU  · omuz üstü       · h 1,15 m · 1,1 m · kadının iskele omzunun arkası

⛔ ABARTI EŞİĞİ [KAMERA_ACISI §5]: alt açı +10° (meşru bant 15-30° altı,
   solucan bakışı 45°+ ELENDİ) · üst açı −28° (zafiyet bandı 15-30° içinde,
   ölü bölge 45-60° ELENDİ) · eğik/Dutch açı bu filmde HİÇ KULLANILMAZ —
   odanın kendisi yattığı için eğik kamera ihlali GİZLER.
```

### 💡 Lighting Bible — KATMAN IŞIK TAKVİMİ  [KART 6b · zorunlu]

> Bu filmde her sahnenin ışığı DIŞARIDAKİ KÜTLEDEN gelir; kütle her sahnede
> değişir. Canopy World'ün arızası tam olarak buydu: bir sahne yanlış
> katmanın ışığıyla üretildi. Takvim sahne numarasıyla yazılır.

| S | dış kaynak | kabin içi baskın ışık | renk | gölge |
|---|---|---|---|---|
| S0 | uzak sarı cüce, sancak kirişinde | alçak açılı, uzun gölgeli | 2900 K amber | uzun, screen-left'e |
| S1 | sarı cüce sönerken + buz dünyasının ilk kenarı | amber zayıflar, soğuk kenar girer | 2900→5600 K | karışık, yumuşayan |
| S2 | buz dünyası, sancakta, pencereyi doldurur | yatay ve sert | 6200 K mavi-beyaz | keskin, screen-left'e |
| S3 | buz dünyası geride; pruva camı koyu | soğuk düşer, lamba havuzu belirir | 6200 + 2700 K | iki yönlü |
| S4 | dışarıda kaynak yok | YALNIZ lambanın havuzu | 2700 K tek kaynak | dar, masada |
| S5 | turuncu toz dünyası, sancakta | geniş ve sıcak | 3400 K turuncu | geniş, yumuşak |
| S6 | toz dünyası sönerken | turuncu nötrleşir ve düşer | 3400→4300 K | zayıflayan |
| S7 | kara daire + ince lensli ışık halkası | ince tek soğuk çizgi + eğik lamba havuzu | 7000 K + 2700 K | mutlak siyah, jilet keskin |
| S8 | halka gerilerken | aynı soğuk çizgi zayıflar | 7000 K düşen | uzayan |
| S9 | dışarıda yalnız yıldız alanı | YALNIZ lambanın havuzu | 2700 K tek kaynak | dar, boş koltukta |
| S10 | halkalı varış dünyası, pruvada | geniş ve yumuşak | 5200 K gümüş | yumuşak, iki yönlü |
| S11 | halkalı dünya, pruvada, büyük | gümüş + amber dengede | 5200 + 2700 K | dengeli |

```
⚠️ KONTROL: ardışık 11 çiftin 11'inde palet değişiyor ✅
⚠️ S4 ile S9 aynı ışıktadır (yalnız lamba) — ardışık DEĞİLLER ✅ ve bu
   bilinçli bir eştir: ikisi de novumun insansız kanıt sahnesidir.
⛔ ANTI-BLOOM [D29 · D41]: hiçbir kaynak hale yapmaz, parlama halkası
   üretmez. Yumuşak ışık ≠ bloom. Abajur KAPALI ve keskin kenarlı havuz
   düşürür. Karadeliğin halkası odaya TEK SERT ÇİZGİ olarak iner —
   yıldız patlaması, ışın demeti ve lens parlaması üretmez.
⛔ KART 9 IŞIK MIKNATISI — DÖRT KANAL, S2 · S5 · S7 · S8'in promptlarında:
   ① hedef-dilim + yön: kütle screen-right'ta, sabit üçte bir
   ② omuz hattı: omuzları kadraja paralel, dönmüyor
   ③ IŞIĞA GÖRE POZ: "the light is on her screen-right side and rims that
      side of her face; she does not turn into it"
   ④ yön negatifi: "nothing in the room turns toward the light; the ship
      does not swing its bow to it; no direction reversal"
   ⚠️ Betik bu kapıyı GÖREMEZ (yönelim aramaz) — denetim insan gözüyle.
```

### ⚙️ Physics Bible

```
KABİN: basınçlı, solunabilir, ısıtılmış. Kask YOK, skafandr YOK, tether YOK.
       ⭐ Bu, depodaki İLK kasksız uzay filmidir → D5 (vizör kalıcılığı),
       D79 (sırt ünitesi) ve KART 3 (kask/vizör — ölçülmüş en net
       başarısızlık) bu filmde YAPISAL OLARAK TETİKLENEMEZ.

AĞIRLIĞIN KAYNAĞI: yalnız itki. Zemin itki eksenine diktir.
       ⭐ D23 (sıfır-g'de rijit beden) TETİKLENEMEZ: hiçbir kare sıfır-g
       değildir. Bu, prompt cümlesiyle değil KARARLA kapatılmış risktir.

DÖNMEK = YANA İTMEK. Hissedilen "aşağı" toplam itkinin tersidir:
       θ = arctan(yanal itki / eksenel itki)

| durum            | sahne        | eksenel   | yanal     | toplam    | θ    |
|------------------|--------------|-----------|-----------|-----------|------|
| seyir            | S0·S1·S2·S3  | 2,45 m/s² | 0,00      | 2,45 m/s² |  0°  |
| geniş çizgi      | S4 · S10·S11 | 2,45      | 0,17      | 2,46      |  4°  |
| dar kesme        | S5 · S6      | 2,45      | 0,99      | 2,64      | 22°  |
| içeriden kesme   | S7 · S8      | 2,45      | 6,07      | 6,55      | 68°  |
| seyir (ezik son) | S9           | 2,45      | 0,00      | 2,45      |  3°* |
*S9'da yanal itki SIFIRDIR ve lamba yine de 3° eğik durur — çünkü artık
 gösterge yalan söylüyor. Filmin tek fizik "hatası" bir HASARDIR, kural değil.

KADININ AĞIRLIĞI: seyirde 0,250 g · dar kesmede 0,269 g · içeriden kesmede
       0,667 g (seyrin 2,67 katı). İtki artınca gövde koltuğa çöker ve kemer
       gerilir; azalınca kemer gevşer. [§3.5 kartının İTKİ DEĞİŞİMİ satırı]

⛔ İVME YAZILMAZ, SÜRE VE MESAFE YAZILIR [D127 · Iron Slope karşı-örneği]:
   · 1,20 m'den bırakılan cisim zemine seyirde 1,0 s'de iner
   · 1,20 m'den bırakılan cisim içeriden kesmede 0,61 s'de iner
   · S4  · 4°  : masadaki anahtar 8 cm screen-right kayar ve DURUR
   · S6  · 22° : bırakılan lamba 0,9 s'de 22°'ye döner ve DURUR
   · S8  · 68° : göğüs hizasından bırakılan anahtar, camdan 2,0 m
                 uzaktayken cama 0,8 saniyede ulaşır ve yolda 0,8 m alçalır
   ⛔ Serbest kalan hiçbir cisim kadrajda ASILI KALMAZ, süzülmez, yavaşlamaz.

SARKACIN DAVRANIŞI — üç cümle, altı promptun altısında aynen:
   · Kordon GERGİNDİR, düz bir çizgidir, kıvrılmaz.
   · Lamba SALLANMAZ, salınmaz, titremez — sabit ivmede sabit açıda DURUR.
   · Açı DEĞİŞİRKEN geçiş 1-2 saniye sürer ve TEK YÖNLÜDÜR: gider ve durur.

TEMAS BÜTÜNLÜĞÜ [D24]: elin lambaya, cismin cama, kalçanın koltuğa teması
   net sınırlıdır. Erime yok, geçme yok, fazlalık parmak yok.
```

### ⚠️ KAPI BETİĞİ — İKİ BİLİNÇLİ SAPMA (dürüst kayıt)

```
① D79 BLOĞU "EKSİK" BULGUSU — YANLIŞ POZİTİFTİR, DÜZELTİLMEYECEK.
   `prompt_kontrol.py` klasör modunda D79 kapısı `helmet|visor|suit|kask|vizör`
   dizgesini ARAR ve bulduğu yerde "sırt ünitesi yasağı + vizör şeffaflığı"
   cümlelerini bekler. Bu filmde 0 kare kask, 0 kare vizör, 0 kare skafandr
   vardır; dizge YALNIZ BU PLANIN Türkçe metninde geçer (fizik kartında,
   sayısal kilit listesinde ve risk sayımında — üçü de "YOK" demek için).
   Bölüm dosyalarında dizge hiç yoktur:
      grep -niE '\bhelmet|\bvisor|\bsuit\b|kask|vizör' *_BOLUM_*.md  → 0 satır
   ⛔ Bu bulguyu kapatmak için prompta vizör cümlesi YAZILMAZ: olmayan bir
     ekipmanı tarif etmek D37/D57'nin tam tersini yapar.
   ⭐ Kapının kendisine "0 kask" kaçışı gerekiyor — GOZLEM_DEFTERI adayı.

② IMAGE PROMPT UZUNLUĞU 2.072-4.879 karakter.
   Betiğin image bandı (1.700-2.100) kendi başlık yorumunda TARTIŞMALI
   yazılıdır ve bulgu NOT seviyesindedir; 4.300 tavanı YALNIZ VİDEO için
   ölçülmüştür (KILAVUZ_REHBERI §7). Depo emsali: Quiet Impact 4.577-5.644
   image ile üretildi, red almadı. Karakter bloğu kelimesi kelimesine
   yazılmak ZORUNDA (kural ③) ve tek başına ~880 karakter.
   ⛔ Video promptlarının 24'ünün 24'ü bantta: 2.206-2.603.
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5 negatif çekirdek TAM METİN

```
Single unbroken take, no cuts, no edits, no camera resets, no transitions,
no dissolves, no fades, no jump cuts, no camera teleportation, no angle
change. Exactly 1 human character in frame — no duplicates, no clones, no
second person, no reflected figure, no shadow of anyone else. 0% bloom, no
glow filter, no soft focus, no dreamy haze — every surface keeps visible
texture. Photorealistic skin pores, fine lines and fatigue retained — no
airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing,
identical bone structure throughout. Clothing and fittings identical to the
description — no drift, no items appearing or disappearing mid-shot. No
readable text, letters, digits, numbers or symbols on any display, surface,
plate or sign — not on the clothing, not on the fittings, not on the brass,
not on the panelling, not on the glass and not on any object in the frame.
Nothing in this room has been measured, labelled, marked out or annotated by
anyone: no scale marks, no graduation ticks, no engraved or painted
characters of any kind. No subtitles, no captions, no burned-in dialogue
text, no title card, no end card, no credits, no watermark. No HUD overlay,
no lens data, no focal length text, no camera metadata, no name label, no
lower third, no annotation. All hand-surface contacts keep a clear structural
boundary — no merging, no phasing, no extra fingers, rigid-body collision
throughout. All loose objects obey the stated weight direction with
continuous physical momentum — never hovering, never frozen, never drifting
sideways on their own, never flowing like liquid. Room static and stable —
no melting surfaces, no warping topology, no swimming texture. No lens flare,
no anamorphic streak, no starburst. No Unreal Engine look, no CGI aesthetic,
no video game aesthetic. Photorealistic with 35mm film grain.
```

```
⛔ D138 KAPSAM: yukarıdaki metin yasağı ÖZNESİ GENİŞTİR — giysi, pirinç,
   kaplama, cam ve kadrajdaki HER nesne sayılır. Kısaltılırsa öznesi daralır.
⛔ D123 YASAK LİSTESİ TUZAĞI: bu blokta şiddet/tehlike sözlüğünden TEK
   kelime yoktur (gore · blood · wound · corpse · injury · horror · weapon ·
   victim · panic · danger). Filmde 0 kare olan şeyi yasaklayarak prompta
   sokmuyoruz. ⑯ kapısı bunu sayar.
⛔ KART 10 · İNSANSIZ SAHNE (S4 · S9): bu iki sahnede NEGATIVE bloğu
   yukarıdaki tam metin DEĞİLDİR — tek kısa pozitif bloğa iner ve boş
   kadraj VARLIK olarak tarif edilir ("the room around it is empty and
   still"). Yokluk listesi istem sınıflandırıcısında "yerine getirilemez"
   okunuyor [Cold Burn S8].
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

| kilit | sayı | hangi risk kartı | hangi sahne |
|---|---|---|---|
| İNSAN SAYISI | tam 1 · 12 sahnenin 10'unda · 2'sinde 0 | KART 4 | S4 · S9 insansız |
| SIVI | 0 kare | KART 1 🔴 | — |
| CANLI | 0 kare | KART 2 🔴 | — |
| KASK / VİZÖR | 0 kare (film boyunca kask yok) | KART 3 🟠 | — |
| TOZ · DUMAN · ALEV | 0 kare | KART 6 | — |
| EKRAN / KADRAN / SAYAÇ | 0 adet — gemide hiç yok | KART 5 | — |
| REPLİK | 0 | KART 7 | — |
| EKRAN METNİ | 0,0 s | KART 5 · D70 | — |
| KLİP SÜRESİ | 12 × 10,0 s sabit | KART 11 | — |
| SAHNE İÇİ KESME | 0 | KART 11 | — |
| KURULUM SAYISI | 6 | KART 8 | — |
| AÇI TİPİ SAYISI | 5 | KART 8 | — |
| ŞOK BANDI | 1 | — | S6→S7 |
| SEYİR İTKİSİ | 2,45 m/s² eksenel | KART 6 | S0-S3 |
| YATMA AÇILARI | 0° · 4° · 22° · 68° · 3° | — | S0·S4·S5·S7·S9 |
| DÜŞME SÜRESİ (1,20 m) | 1,0 s seyirde · 0,61 s 68°'de | KART 6 · D127 | S8 |
| ANAHTARIN CAMA YOLU | 2,0 m'yi 0,8 s'de, 0,8 m alçalarak | D127 | S8 |
| GEVŞEK EŞYA SAYACI | 6 → 6 → 5 → 3 → 0 → 4 | KART 5 | S0·S4·S5·S7·S8·S10 |
| LAMBADAKİ EZİK | 1 (eski) → 2 (yeni) | — | S2 tohum · S9 |
| İNSANSIZ SAHNE | 2 | KART 10 | S4 · S9 |
| VİRAL ARA | 2 (⛔ KESİLEMEZ) | §2.2 | S4 · S9 |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| **D157** | Novumun taşıyıcısı TEK KARE testini KENDİSİ geçer | TEK KARE satırı sarkaç lambayı adıyla içeriyor; taşıyıcı 6 sahnede, kanıt sahnelerinde (S4·S9) kadrajda rakip olay yok |
| **D158** | Merkezi seçimden SONRA da seçim sayılır; başarısız deneme sayılır | B2a = 2 (S10 geniş hat · S10 sarkaca dokunmama) · B2b = 2 (S6 · S8) |
| **D155** | Faz/defter etiketi prompt gövdesine girmez; kısaltma yok | Yatma açısı promptta DERECE olarak yazılır, "PHASE" etiketi yok; giysi adında büyük harfli kısaltma yok |
| **D154** | Tekrarlayan olay bir VARLIKTIR — kapı ölçütü her sahneye kopyalanır | Sarkacın üç cümlelik davranış kilidi 6 promptun 6'sında AYNEN; ilk onaylı kare sonraki imaj üretimlerine referans girer |
| **D153** | Eş kadraj çifti metinle taşınmaz — ayna sahne ONAYLI kareden türetilir | S2 ↔ S6 ↔ S9 aynı B kurulumu: S6 ve S9'un imajı S2'nin ONAYLI karesinden image-edit ile üretilir, ≤3 maddelik fark listesiyle |
| **D127** | İvme yazılmaz; kadrajı terk etme SÜRESİ ve MESAFESİ yazılır | Physics Bible'ın süre/mesafe blokları; S8'in 0,8 s / 2,0 m / 0,8 m üçlüsü |
| **D139** | Kamera arkadaysa yokluk listesi tutmaz — POZİTİF yüzey tarifi | Omuz üstü kurulumu F (S3·S5·S10): "one continuous panel of charcoal wool from collar to hem, carrying nothing" |
| **D138** | Metin yasağının KAPSAMI yasağın kendisi kadar önemli | Negatif çekirdekte özne genişletildi: pirinç, kaplama, cam, her nesne |
| **D147/D42** | Yıpranma MONOTONİK merdivendir | Lambanın dinlenme açısı: 0° → 0° → 0° → 3°, geri DÖNMEZ; eşya sayacı 6→0→4, ikisi kalıcı olarak kayıp |
| **D104** | Işık mıknatısı — dört kanal + iki yenilgi kuralı | Lighting Bible'ın KART 9 bloğu, S2·S5·S7·S8 promptlarında |
| **D71** | Hook'un sakladığı şey ihlal değil, SEBEBİDİR | İhlal 0. karede; sebebi (kadının dönüşü) S3'te |
| **D32** | Gemi ölçek kilidi — geometri sahneler arası sabit | Salon 7,0 × 4,4 × 2,5 m; iki cam, tek masa, tek koltuk, tek kanepe, 12 sahnenin 12'sinde aynı |
| **D24** | Temas bütünlüğü | El-lamba, cisim-cam, gövde-koltuk temaslarında net sınır |
| **D13/D34/D45** | Ekrana anlamsız yazı · özel ad · şablon biçimi sızması | Gemide 0 ekran · 0 ad · CAMERA satırı cümleye çevrildi, "75mm, f/5.6, ISO 400" dizilimi kullanılmadı |
| **D74** | Banttan sapılıyorsa plana tek satır gerekçe | Sahne haritasının üstündeki "Uygulanan sıçrama okuması" bloğu (azimut yayı kabin içinde dar) |
| **D122** | Zaman kodları hesaplanmaz, HESAPLATILIR | QA_SPEC B bloğu: başlangıç(n) = 10 + (n−1) × 10 |

---

## 📋 RİSK TOPLAMI  (`02_RISK_KARTLARI.md`)

```
FİLM: THE LEANING ROOM

□ Su/sıvı teması var mı?            HAYIR — 0 kare. KART 1 🔴 tetiklenmiyor
□ Canlı var mı?                     HAYIR — 0 kare. KART 2 🔴 tetiklenmiyor
□ Kask/vizör var mı?                HAYIR — basınçlı kabin. KART 3 🟠 yok
□ İkinci figür riski                EVET — KART 4 (her filmde)
□ Ekran/sayaç/gösterge var mı?      EVET — KART 5 (gösterge VAR, ekran YOK)
□ Parçacık/toz/patlama var mı?      HAYIR — 0 kare
□ Katmanlı/bölgeli dünya mı?        EVET — KART 6b, ışık takvimi yazıldı
□ Diyalog var mı?                   HAYIR — 0 replik
□ Kamera hareketi var mı?           KART 8 — klip içi lockoff, sahneler arası yay yazıldı
□ Tek baskın ışık + hedefe hareket? EVET — KART 9, dört kanal yazıldı
□ İnsansız sahne var mı?            EVET — KART 10, S4 · S9
□ Değişken çekim süresi?            HAYIR — 12 × 10,0 s sabit
□ Politika yüzeyi?                  EVET — KART 12, aşağıda

RİSK SAYISI: 7 / 13     ⚠️ 5+ bandının üstünde.

⛔ MALZEME AZALTMA KARARI — bu satır zorunlu ve şu şekilde okundu:
   Yediden DÖRDÜ her filmde açık olan sabit kartlardır (4 ikinci figür ·
   8 kamera · 10 insansız · 12 politika) ve dördü de yazılı önlemle kapandı.
   Kalan üçü filmin OMURGASIDIR ve çıkarılırsa film kalmaz:
     KART 5  gösterge = sarkaç = novumun kendisi
     KART 6b katman = yolun üstündeki kütleler = filmin konusu
     KART 9  tek baskın ışık = geçilen kütle = aynı şey
   AZALTMA GERÇEKTEN YAPILDI ve nerede yapıldığı sayılabilir:
     sıvı 0 · canlı 0 · kask 0 · toz 0 · duman 0 · alev 0 · replik 0 ·
     ekran 0 · ayna 0 · kağıt-etiket 0 · sahne içi kesme 0 · kamera hareketi 0
   İki 🔴 kart (su · canlı) ve ölçülmüş en net başarısızlık kartı (KART 3
   kask/vizör) bu filmde SIFIRDIR.

⚠️ AZALTMANIN AÇTIĞI YENİ RİSK — dürüst kayıt:
   Kask kaldırılınca 120 saniye boyunca fotogerçekçi bir İNSAN YÜZÜ ekranda
   kalıyor. DIKEY_MIKRO_DRAMA §6.1'in ölçtüğü ceza kutusu "kırılgan insan
   duygusu + fotogerçekçi insan"dır. Karşı önlem TASARIMDADIR: bu kadın
   kırılgan değil YETKİN — çalışıyor, katlanmıyor (Character Bible son
   cümlesi). Ceza kutusuna girmemek yüz sayısını değil, DUYGU REGISTERINI
   seçmekle olur. ⚠️ Bu depoda ÖLÇÜLMEDİ; ilk ölçüm bu film olacak.
```

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

```
EN RED-RİSKLİ KARE:  S7 · 1:13-1:20
NÖTR TARİFİ:
  Kadraj profili: kemerli bir insan, yatmış bir oda, kayan eşyalar ve
  dışarıda kara bir daire → sınıflandırıcı bunu "tehlike çerçevesi +
  kısıtlanmış uzuv" olarak okuyabilir (defterdeki çözülemeyen tek
  kompozisyon reddi tam bu profildeydi: yüzsüz izolasyon + kısıtlanmış uzuv).
  Nötr hâl üç kararla yazılır:
   ① YÜZ AÇIK VE OKUNUR — kask yok, gölge yok, yüz her karede net.
      Yüzsüz izolasyon profili yapısal olarak kırılır.
   ② TEHLİKE SÖZLÜĞÜ SIFIR: savrulma, çarpma, panik, acil, tehlike,
      kaçış, alarm kelimeleri promptun HİÇBİR yerinde (negatif blok DÂHİL)
      geçmez. Kadın sürüyor, hayatta kalmıyor.
   ③ KUVVET GÖVDEDEN DEĞİL NESNEDEN OKUNUR: "she is settled deep into
      the screen-right arm of the chair; the lap belt lies flat and tight
      across the wool" — duruş ve malzeme, darbe değil.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| S7-S8'de tehlike ve darbe sözlüğü kaldırıldı | tehdit hissi zayıflar; izleyici "bu tehlikeli mi" diye sormaz | **malzeme sonucu:** pirinç lambanın gövdesinde kalıcı ezik + anahtarın cama yaslanıp orada kalması — kuvvet nesnenin üstünde okunur |
| Gemide ekran, kadran ve sayaç yok (D13/D138 metin riski + KART 5) | teknik gerilim ve "kaç saniye kaldı" bahsi gitti | **alet tepkisi:** sarkacın açısı tek göstergedir; ölçüm aleti dramanın kendisi olur (S6'da onu düz tutmaya çalışır) |
| 0 replik (KART 7 + KART 12 ses denetim dalı) | motivasyon sözle kurulamaz | **temassız gövde tepkisi:** nefes ritmi (S6 · S9), koltuğa çöküş, kemer gerginliği, elin dümen üstündeki duraksaması |
| Ayna ve yansıtıcı yüzey yok (KART 4) | lüks kabinin klasik görsel zenginliği azaldı | **kütle-hız:** zenginlik yansımayla değil AĞIRLIKLA anlatılır — som pirinç küre, ağır ceviz, kalın yün |

```
⛔ TELAFİ sütununun dördü de dolu — önlemler ALINDI, film KISALTILMADI.
   Dört kanalın dördü de kullanıldı (kütle-hız · malzeme sonucu ·
   alet tepkisi · temassız gövde tepkisi).
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR yerinde geçmez.
⛔ PROMPTLAR YAZILINCA: prompt_kontrol.py ⑯ koşulur (kelime ekseni).
   Kompozisyon ekseni betiğe İNMEZ → PROMPT_QA_CRITIQUE_PROMPT.md POLİTİKA §3.
```

---

## 📋 03_PLAN_ONCESI — TEK SAYFALIK ÖZET

```
A  □ plan kendi içinde çelişmiyor: "no text" yasağı ile okunacak bir gösterge
     AYNI ANDA yok — bu filmde gösterge FİZİKSELDİR (sarkacın açısı) [KART 5]
B1 □ doruk anı S7'nin İÇİNDE tarif edildi (1:13, lamba 68°'ye varır),
     sahne arasına düşmüyor
B1b□ katmanlı dünya: IŞIK TAKVİMİ yazıldı (Lighting Bible tablosu)
B2 □ bedelli seçim S7 · kayıp S8 ve S9 sahnelerinde GÖRÜLÜYOR
B2a□ merkezi seçimden SONRAKİ seçim sayısı: 2
     (S10 geniş hattı sürer · S10 sarkacı düzeltmemeyi seçer)
     ⛔ Koda uzunluğu: S8-S11 = 4 sahne. 3-5 bandının içinde ✅
B2b□ başarısız deneme sayısı: 2
     (S6 lambayı düz tutmaya çalışır ve tutamaz · S8 eşyaları toplamaya
      uzanır ve geri kayarlar)
B3 □ TEMA: ENTROPİ · motife döndüğü sahneler: S2, S8, S10, S11
     B2'nin bedel sahnesi (S8) bu listede ✅
B4 □ kurulum dizisi: A-D-B-F-E-F-B-A-C-B-F-E · kurulum sayısı 6 ·
     açı tipi 5 · şok bandı 1 (S6→S7)
B5 □ İSTEK: varış — pruva camında büyüyen halkalı disk (S3'te nokta,
     S11'de okunur disk). ENGEL: yolun üstündeki kütleler ve odanın
     kendisi. BEDEL: göstergenin kalıcı olarak yalan söylemesi.
     ⛔ "anlamak · görmek · fark etmek" İSTEK DEĞİLDİR — buradaki istek
       görünür bir hedeftir ve kadrajda büyür.
B6 □ POLİTİKA SATIRI: en red-riskli kare S7 · nötr tarifi yukarıda
C  □ sayısal kilitler yazıldı (21 satır)
D  □ risk sayımı yapıldı: 7/13 + azaltma kararı + yeni riskin dürüst kaydı
E  □ QA'ya hazırlık: THE_LEANING_ROOM_QA_SPEC.md
```
