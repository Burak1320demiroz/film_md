# 🧾 SUSMAYAN_NOBETCI — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu (109 satır · 103 kilit · 6 "—").
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Risk sayımı 11/14 (`02_KONSEPT_VE_RISK` §3) →
> **KİLİT TAVANI ≤ 20**. Satır başına TEK ders numarası (㉕ farklı D-numarası sayar); akraba
> derslerin içeriği satıra katlanır, numarası §1b'de.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| # | ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|:--:|---|---|---|---|
| 1 | D192 | filmin 1 numaralı riski yalnız yasakla korundu, doruğun boşalması şimşek geldi | **Uydu vuruşu SAYIYLA pozitif:** ışın ve mermi kadrajda YOK; vuruş anında vurulan dikişte tek beyaz nokta çakması ≤ 6 kare (bir yumruk büyüklüğünde), ardından parça dikişinden AYRILIR ve kazandığı dönüşle uzaklaşır; ayrılan yerden düz çizgilerle yayılan kısa bir buz kristali konisi 2 s içinde seyrelir. Sayı: ateşleme başlangıcından vuruşa **3,0 s**. "explosion · fire · blast · beam · laser · weapon" 0. | S0 · S4 · S15 · S30 · S45 |
| 2 | D213 | temas/değişim/sonuç kadraj dışında ya da kesmede kaldı; HARD DOCK kenetlenme darbesi kesmeyle gizlendi, KRONOS ayrılma anı tek karelik kesmeyle kaçtı | Her vuruşta ATEŞLEME (t) · VURUŞ (t+3 s) · SONUÇ (≥1 s ayrılan parça kadrajda) AYNI klipte, merkez üçte birde; temas S36 `contact at 4.0s` · kelepçe S37 · bastırma S42 aynı kalıp. | S0 · S4 · S15 · S30 · S36 · S37 · S42 · S45 |
| 3 | D200 | tek kadrajda iki yerçekimi; MARS_SON_CIKIS RCS soğuk gazı vakumda buhar gibi kıvrıldı; KRONOS 0 g'de yürüme | Film boyu **tek g = 0**: soğuk gaz püfü "a brief straight transparent cone that is gone within a quarter second"; buz kristalleri düz çizgide yayılır; kabinde bırakılan hiçbir şey düşmez, kemerli pilotun kolları hafif süzülür; ayak yere basmaz, gövde tutamakla ilerler. | tüm film · S3 · S6 · S12 · S20-S21 · S33 · S40-S42 |
| 4 | D198 | 0 g'de yüzen nesne donuk heykel gibi kaldı | Kopan/salınan her parça dönme ekseni + oranla: "turning end over end about once every three seconds, never slowing"; enkaz S13 "a slow steady tumble about its long axis"; tahliye gemisi S16+ "one full turn about every twenty seconds". | S0 · S4 · S11 · S13 · S16-S37 · S30 · S45 |
| 5 | D209 | dünya çapası yoktu; KRONOS/HARD DOCK arka planda gezegen topoğrafyası ve yön kaydı | **DÜNYA ÇAPASI** üç cümle her dış promptta birebir: "a flat black sky" · "the curved bright edge of a large rust-and-grey planet crossing the lower part of the frame" · "one small steady white light above the planet's edge on the right" (uydu). Yıldız YOK (güneşli vakum). | tüm dış kadrajlar |
| 6 | D193 | ışık takvimi ölçülmedi; KRONOS dış güneşi 10→2 saat döndü; HARD DOCK S8→S9 yüzde sıcak→soğuk | Güneş DÜNYA yönünde sabit (kadrajın sol üstü dışında, gezegenin aydınlık kenarı güneşe bakar) ve kurulum başına ekran yanı PLAN'da; kokpit paneli + kask içi fill **4500K sabit**; PRATİK sayaçlar yalnız sınırda değişir: tahliye penceresi fener **3 → 2 (S23) → 1 (S26) → 0 (S38 sınırı)** · çekici kaş lambası 2 sabit. [D201 katlandı] | tüm film |
| 7 | D78 | sayaç ve bedel iki sahne arasında karşılaştırma istedi, ekranda okunmadı | Üç sayaç TEK KAREDE sayılır: uydunun iki soğutma kanadı AÇIK/KAPALI (S3-S5 · S17 · S31-S32 · S44) · soğuk gaz ibresi RAKAMSIZ kadranın yarısı → dibi (S12 · S21 · S24 · S33) · tahliye penceresinde yanan fener sayısı (#6). | S3-S5 · S12 · S17 · S21 · S23-S27 · S31-S33 · S38 · S44 |
| 8 | D157 | novumun taşıyıcısı tek kare testini geçmiyordu, iki taşıyıcı sahne tekrar sayılıp kesildi | **TEK KARE S0:** "motor konisi hâlâ yanan mekik gövdesinin ikiye ayrıldığı an, ön planda pilotun eldiveni motor kolunun üstünde duruyor" — taşıyıcı nesneler adıyla: MOTOR KOLU × EGZOZ KONİSİ. Kural tekrarı 6 FARKLI nesnede farklı sonuçla (mekik gövdesi · arka yarı motoru · yönelim iticisi · kapsül · çekici motor bölümü · kurtarma gemisi vurulmaz). | S0 · S3-S4 · S15 · S30 · S45 · S47 |
| 9 | D179 | imaj promptu değişimin SONRASINI yazdı, bedel ekrana gelmedi | İmaj t=0 = ÖNCE: S0 mekik motoru yanıyor, gövde bütün · S15 tahliye motoru yanıyor, itici kümesi yerinde · S30 kapsül yuvada, eldiven ayırma kolunda · S36 kenet halkaları arasında el genişliği · S44 motor kolu geride · S45 motor bölümü bağlı ve yanıyor. | S0 · S15 · S30 · S36 · S44 · S45 |
| 10 | D202 | merkezî seçim ve bedel bedende okunmadı (COUNTED TURN THE CHOICE IS INVISIBLE) | ÇAPA ÜÇLÜSÜ aynı kanalda önce/sonra: **SEÇİM S30** sol eldiven ayırma kapağında iki vuruş için kalkık → eldiven kolu sonuna kadar çeker, omuzlar iner · **BEDEL S45** gövde koltuğa bastırılmış → kemerler gevşer, gövde öne süzülür · **FİNAL S46** sağ eldiven dizde kapalı → omzundaki eli tutar. Reddedilen seçenek (kapsül) S30'dan sonra da kadrajda: BOŞ YUVA. | S29-S30 · S44-S46 · S32 · S47 |
| 11 | D210 | kafiye ve lockoff niyette kaldı (HARD DOCK kafiye 2 · KRONOS RHYME BROKEN) | Her CAMERA "fixed locked-off … absolutely zero camera movement. In a single continuous shot."; TIMELINE son satırı sürdürme. ⚠️ **Sahip sapması:** açılış S0 kokpit, kapanış S47 dış geniş (sahip tarifi) → aynı kamera DEĞİL; kafiye iki katmanda: olay kafiyesi (yanan motor vurulur ↔ vurulmaz) + kurulum dönüşü S8 ↔ S47 birebir CAMERA cümlesi (D74 · 04_UYARI Y1). | tüm film · S0 · S8 · S47 |
| 12 | D146 | vizör geometrisi metinle tutulmadı (3 vaka + OPEN CIRCUIT paketliyken bile) | Kask cümlesi film boyu birebir: "a rounded hard off-white shell with a single flat front pane set inside a thick dark-grey rim, seated deep in a raised collar ring, two small square lamps in the brow"; referans paketi YOK (sahip) → yüz planı yalnız 6 sahnede, S29-S30 ve S45'in yüzü PROFİL/üç çeyrek (pane çerçevesi kadrajda okunur). | S14 · S22 · S29 · S30 · S45 · (S46 kask açık) |
| 13 | D69 | araca biniş/inişte klon (Stone Sky · Starless Circle) | **Geçiş hareketi kadraj DIŞI:** S25 pilot kapsülün İÇİNDE başlar · S40 pilot gövdenin DIŞINDA tutamakta başlar · S42 kapağın içinde başlar · S46 pilot bölmenin içinde başlar, geçit arkasında. Hiçbir klip bir eşiği geçmeyi göstermez. | S25 · S40 · S42 · S46 |
| 14 | D174 | "screen-right" koordinat, yön nesneyle bağlanmadı; KRONOS WRONG WAY, HARD DOCK dış yönelim ile pencere perspektifi 45° çelişti | Yön nesneyle ve harita tek: çekici HEP ekranın SOLUNDA, tahliye gemisi SAĞINDA; hareket "toward the evacuation ship on the right"; fren alevi GİDİLEN yöne; dönen gemi "yaws from … to … and keeps turning the same way"; kokpit penceresinden görülen yön = dış kurulumun yönü. [D104 katlandı] | tüm dış kadrajlar · YÖN DEFTERİ |
| 15 | D203 | replik envanteri prompta geçmedi / envanter dışı replik üretildi (MARS_SON_CIKIS) | 8 replik (7 telsiz sesi + pilotun "Don't.") klipte ÜRETİLMEZ, post-dub; promptta tırnak 0, AUDIO "one short burst of radio static, no words"; SPEC `DIALOGUE LINES: 0` + `POST-DUB LINES: 8`. | S1 · S2 · S7 · S9 · S14 · S27 · S46 |
| 16 | D217 | replik ekranda olanı söyledi (MARS_SON_CIKIS · AMBER LATTICE) | Replik tablosunda her satırın İŞLEVİ görünmeyeni taşır: karar (S14 · S27) · kadraj dışı bilgi (S9 hava · S1 kaç kişi) · istek (S7). ⚠️ S2 "You're going past us." görüneni söyleme riski → İŞLEV alt metin (terk edilme korkusu), 04_UYARI Y3. | replikli 7 sahne |
| 17 | D168 | baştan üretilen film sonunda durdu, elde kurulum kaldı | ÜRETİM SIRASI: Scene Foundation (boş kokpit + dış çapa karesi) → S36-S37 temas → S44-S45 → S30 → S47 → S0 → S15-S16 → B4 → B3 → B2 → B1; üretim defterinin ilk KABUL'ü S36 değilse ikinci klip üretilmez. | tüm film · URETIM_DEFTERI |
| 18 | D123 | yasak olarak yazılmış şiddet sözcüğü redde yol açtı (LAST SPAN) | Silah/patlama/yara sözlüğü NEGATIVE dahil 0: uydu "a long straight rail housing on a boxy body with two flat radiator wings"; vuruş #1'in malzeme dili; tahliyedekiler için "injured/dying/dead" 0 — hava kaybı yalnız fener sayısı ve seyrelen nefesle. | tüm film |
| 19 | D139 | düz sırt kilidi kamera arkaya geçince düştü (COLD BURN iki giyside sırt ünitesi) | Sırt görünen dış çıkışta POZİTİF: "the back of the suit is one continuous ribbed surface from collar to hip, closed and smooth, the two shoulder caps wrapping over its upper edge". | S40 · S41 · S42 · OTS kurulumları |
| 20 | D206 | bedel bedende ödenmedi — efor fiili var, kanal yok (7 film · HARD DOCK no tremor) | BEDEL EĞRİSİ hücresi `<kanal @ saniye>` TIMELINE'a iner: S20 halat çekişi ön kol + omuz @2 s · S38 kelepçe yükü omuz titremesi @4 s · S40 tek el tutunma ön kol @1 s · S41 manivela gövde ağırlığı @3 s · S44 G ile gövde koltuğa @2 s. [D169 katlandı] | S20-S21 · S38 · S40-S42 · S44 |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

> ⚠️ "Uygulanmayan" = PLAN'ın 20 satırlık PROMPT KİLİDİ bloğunda ayrı satır almadı. Çoğunun
> içeriği yine de yazılır — kilit olarak değil, **sahne tablosu sütunu / SPEC satırı / üretim
> defteri kutusu / Bible cümlesi** olarak. Hangisinin nereye gittiği sağdaki sütunda.

| ders | neden bu filmde prompt kilidi olarak uygulanmadı · içeriği nerede |
|---|---|
| D1 · D210 | tek çekim — çekirdek ① cümlesi + OMNI "In a single continuous shot." zaten her promptta (#11) |
| D16 · D167 | yüz morph · kimlik yığını — Character Bible yüz cümlesi ≤3 öznitelik, yalnız IN FRAME face promptunda (#12'nin yanında) |
| D34 · D70 · D211 | jenerik/başlık kartı · ilk/son 10 s — kurgu kapısı üç sayı (48 klip · 480 s · ekran metni 0 s) + S47 "the take ends on the held frame" |
| D42 | yıpranma — SPEC C KİMLİK DİZİSİ: giysi global mat sürtünme sabit, S42'den sonra SAĞ eldiven avucunda parlak metal izi |
| D45 · D138 | prompt iskeleti ekrana sızar · ölçü zemine basılır — özel ad/künye prompta 0; metre yalnız SPEC/PLAN, promptta gövde boyu |
| D62 · D141 | final düşer · vuruş yok — KESİLEMEZ listesi (S0 · S15 · S30 · S36 · S44-S47) + SPEC B FİNAL VURUŞ KANITI |
| D104 | ışık mıknatısı — #14'e katlandı (güneş kadraj dışı, tek baskın kaynak kadrajda yok; yön kanalları dört) |
| D172 | askı düzeneği mekanizma sanılır — halat S20-S21 ve hortum S43 eylem nesnesi, kadrajda başka kablo yok; sahne çalışması |
| D175 · D214 | through the glove · kadrajda olmayan beden — çıplak deri negatifi üç bölge (S46 hariç: kask açık, yüz meşru) + IN FRAME ilk satır |
| D176 | kontrast garantisi zemini ikinci kez tarif etti — gezegen rengi TEK cümle (DÜNYA ÇAPASI), LIGHT bloğu renk vermez |
| D180 · D216 | planlı sessizlik · ses miksi — S45 kopmadan sonraki 2 s sessizlik KURGUDA; MUZIK katman ≤4, telsiz band-pass EVET, köprü ≥0,2 s |
| D207 | yorgunluk kesmede sıfırlanır — sahne tablosu yorgunluk 0-6 sütunu (S0=1 → S42=6 → S46=5) |
| D208 | kimlik dizisi — SPEC C: kask K×47 + S46 A · turuncu bant SOL pazu/uyluk · eldiven izi S42+ |
| D212 | aynı vuruş ardışık — vuruş sütununda ardışık tekrar 0; yanaşma sahneleri "hangi koşul değişti" sütunuyla |
| D215 | ekran metni/filigran/ağız araç ayarı — üretim defteri üç kutu |
| D59 | still/frozen tek başına + yokluk listesi — insansız sahnede NEGATIVE kısa, boş kadraj VARLIK olarak (red defteri #2) |
| D32 · D58 | yapı oranı · tekrar eden varlık — ANATOMİ KARTI (çekici · tahliye gemisi · uydu · kapsül) sayıları Bible'da, promptta gövde boyu |
| D82 | sayı söyleyen replik insana geçti — replik tablosunda sayı 0 (ibre ve kanat taşır) |
| D89 | çıkarma eylemi yanlış şeyi çıkardı — S46 kask sahneye AÇIK girer, kimse bir şey çıkarmaz (red defteri #3) |
| D127 | ivme yerine süre — kopan parçanın kadrajı terk etme süresi saniyeyle (sahne çalışması S4 · S45) |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| KRONOS_SON_SINYAL (B2) | ① KARE | 2:20 gövde yırtılmasında ve 2:53 modül ayrılırken VAKUMDA ses (🔴 ×2) | dış kadrajın AUDIO satırı dış ses taşımaz: "no exterior sound — hard vacuum; only the cockpit hum and her breathing inside the helmet" (insansız dış kadrajda telsiz hışırtısı) |
| KRONOS_SON_SINYAL (B2) | ⑥ FİZİK · ⑭ HAREKET | 2:20 enkaz yavaş süzülme · 0:44 0 g'de bisiklet pedalı | kopan parça oran + dönme ekseniyle (#4); pilot hep kemerli ya da iki elle tutunur, bacak serbest işi yok |
| KRONOS_SON_SINYAL (B1) | ⑪ IŞIK | dış güneş S1 10 saat → S9 2 saat (KEY WALKS) | güneş dünya yönünde sabit, kurulum başına ekran yanı PLAN'da (#6) |
| KRONOS_SON_SINYAL (B1/B2) | ⑨ KADRAJ · ⑫ HOOK | S1↔S24 kafiye yok · peş peşe konsol sahneleri 00:40-01:35 plato | S8↔S47 kurulum dönüşü (#11); kokpit sahneleri ardışık ≤2, her kesmede yeni koşul |
| THE_HARD_DOCK | ⑦ AKSİYON | 3:30-3:37 kenetlenme darbesi kokpit tepkisine kesildi | S36 temas klibin İÇİNDE, kamera hedefte (#2) |
| THE_HARD_DOCK | ① KARE | 1:10 dış istasyon yönelimi pencere perspektifine göre ~45° sıçradı | dış kurulumların yönü kokpit penceresinin gördüğü yönle aynı (SPATIAL MAP · #14) |
| THE_HARD_DOCK | ⑥ FİZİK | 2:00 güneş paneli koptuğunda istasyona recoil yok | her vuruşta ana gövde tepki dönüşü: "the hull kicks the other way and starts to turn" (S15-S16 · S45) |
| THE_HARD_DOCK | ② · ⑤ | pencere cıvatası 8→10 · gezegen topoğrafyası değişti | ANATOMİ KARTI sayıları (pencere paneli 3 · kelepçe 4 · kanat 2) + gezegen yalnız kenar ve renk, topoğrafya ayrıntısı YAZILMAZ |
| THE_HARD_DOCK | ⑩ OYUNCULUK | S13-S16 insansız dış dizisi duygusal tırmanışı kesti | ardışık insansız sahne ≤2 (S3-S4 tek istisna, arası kokpit sesiyle bağlı) |
| THE_PAYLOAD | ④ · ② | novum taşıyıcısı (bant) okunmadı, iki taşıyıcı sahne "tekrar" sayılıp kesildi | kural tekrarı her seferinde FARKLI nesne + farklı sonuç (#8) |
| THE_PAYLOAD | ① | göğüste "PHASE 1" basılı yazı | giysi/panel/gövde üzerinde yazı 0; faz adı prompta yazılmaz |
| THE_COUNTED_TURN | ⑧ · ⑩ · ② | NOBODY PAYS 0,0 · THE CHOICE IS INVISIBLE · yüz/giysi kimlik kırılması | #10 çapa · #20 efor kanalı · SPEC C KİMLİK DİZİSİ |
| THE_COLD_BURN | ③ SES | D82 sayı replikleri ağızlara geçti · D83 ortam yatağı klip sınırında öldü | replikte sayı 0 · MUZIK tek parça kokpit yatağı, köprü ≥0,2 s |
| THE_COLD_BURN | ② KARAKTER | D79 sırt ünitesi 32 negatife rağmen iki giyside doğdu | sırt POZİTİF (#19) |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| YR | insansız sahne + uzun `NEGATIVE:` + "Exactly 0 human figures" (COLD BURN S8, yanaşma filmi) | NEGATIVE tek pozitif `Style:` satırına indi, boş kadraj VARLIK olarak tarif edildi | insansız dış sahneler (S3 · S4 · S8 · S13 · S15 · S16 · S47 …) → kısa NEGATIVE (<900 karakter), "human" kelimesi yalnız ⑤ imza cümlesinde |
| PB | kask ÇIKARMA — bedenden bir şey çıkarma eylemi (COLD BURN S28) | kasklar sahneye zaten çıkmış girdi, vuruş başka nesneye taşındı | S46 — kask zaten açık, kucakta; kimse bir şey çıkarmıyor |
| PK+PB | "wounded ship" + "dull orange glow" + replikte tehlike çerçevesi (COLD BURN S26) | tehlike sözlüğü ayıklandı, replik değişti | S15-S16 insanlı tahliye gemisi vuruluyor → malzeme dili (#1 · #18), fener ve nefes |
| PK | milliyet ifadesi (LOW POWER) · kimlik yığını (SINKING STAKE, OMNI) | fiziksel tanım, ≤3 öznitelik | pilotun yüz planları (S14 · S22 · S29 · S30 · S45 · S46) |
| PK | yasak olarak yazılmış şiddet sözlüğü (LAST SPAN) | yasak SİLİNDİ, malzeme tarifi | uydu ve vuruş sahnelerinin tamamı (#18) |
| TK | aynı oturumda 0 başarı (THIRD DUNE · RING LIGHT) | prob BAŞA alınır, kısaltma değil | üretim günü 1 — ilk üç redde PROB_KOSUSU |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet (§1) · 20 ders §1b'de içerik olarak başka yerde
QA ARIZASI:         14 adet (5 kayıttan)
RED SINIFI:          6 adet
⛔ EN PAHALI ÜÇÜ:   #1 uydu vuruşunun görünüşü (D192) · #13 geçiş sahnelerinde klon (D69) ·
                    #12 referans paketsiz kask biçimi (D146)   (04_UYARI_NOTLARI'nda 🔴 satırı olur)
```
