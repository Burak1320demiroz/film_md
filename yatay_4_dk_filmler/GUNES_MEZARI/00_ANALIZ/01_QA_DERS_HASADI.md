# 🧾 GUNES_MEZARI — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D146 | 4 vaka · vizör geometrisi METİNLE tutulmuyor; referans paketi olan filmde bile 23 klibin hepsinde kubbe çıktı | kask: mat grafit sert kabuk, ÖN yüzde TEK DÜZ pane, çepeçevre KALIN koyu çerçeve, yaka çemberine derin oturmuş; `seamless` · `bubble` · `dome` · `sphere` kelimeleri 48/48 promptta 0 kez | insanlı 20 klibin hepsi (kask cümlesi birebir) |
| D89 | çıkarma sahnesinde model yasaklanan parçayı bırakıp mühür ailesinin bir sonraki üyesini çıkarıyor (eldiven → KASK) | ⭐ bu filmin 4 çıkarma klibinde TEK MÜHÜR SAYIMI: "exactly one thing is taken out in this shot and it is the core / the key bar; every seal on her suit stays closed — helmet on and locked at the collar, collar ring closed, both gloves on" | K17 · K18 · K19 · K20 |
| D59 | 28/28 promptta yazılan yasak, aynı promptun POZİTİF isminde yenildi (`hang` → anti-gravite) | ⭐ `hang · hangs · hanging · suspend · suspended · float · floating · hover · hovering · still · frozen · stopped` yedi kökü YALNIZ negatif blokta; küre pozitif gövdede **TUTULUR**: "three machined rings close around it and it turns with the ship as one body" | 24/24 klip · üretimden önce grep |
| D192 | filmin 1 numaralı riski yalnız SIFATLA korundu, doruğun boşalması ŞİMŞEK geldi | küre pozitif biçimi SAYIYLA: kenarı keskin, çapı halkaların iç açıklığının beşte dördü, yüzeyinde daha parlak hücreler bir genişliği 4 s'de geçer, çevresinde 0 kare korona/ışın/lens parlaması, aradaki hava karanlık | K01 · K02 · K03 · K21 · K22 (küre kadrajda) |
| D127 | 12/12 promptta yazılan ivme ekrana gelmedi; kilitlenebilen şey ivme değil KADRAJI TERK SÜRESİ | kürenin yükselişi süreyle yazılır: "by the sixth second its lower edge has crossed the top frame line, by the eighth it is gone from the shot and does not return; it covers its own width in about two seconds" | K21 |
| D209 | 3 film · gök/ufuk/yer imi her sahnede yeniden tarif edildi, her sahnede başka dünya çıktı | DÜNYA ÇAPASI üç cümle, dış-mekân 13 klibinde BİREBİR: ① gök: yıldız alanı + parçalanmış ay, bir kol boyu tutulan bir tabak genişliğinde ② ufuk: bazalt kule hattı, düz, pussuz ③ yer imi: kaidenin üç taş kemeri, şehrin kenarında | K04-K09 · K13 · K14 · K18-K24 |
| D193 | ışık takvimi "monotonik" yazıldı, hiçbir yerde ölçülmedi; sönen şerit AYNI KLİPTE geri yandı | IŞIK TAKVİMİ 7 satır: S1-S6 tek değer (fener + parçalanmış ay, gök cismi yok) · S6'nın son klibinde kaide yuvası + S7 yeni güneş — **ARTIŞ bir OLAYDIR ve sahne haritasında yazılıdır**; klip içinde geri yanma 0 | bütün sahneler · SPEC C |
| D210 | 4 film · kapanış açılışın kamera cümlesini taşımadı; KEPT_LIGHT'ta S0 tepeden CU ↔ S24 alttan alt açı | iskelet ilk ve son harf AYNI (A … A); K24'ün CAMERA satırı K01'in CAMERA satırının BİREBİR kopyası + `— the same position, height and lens as Clip 1.`; TIMELINE son satırı sürdürme | K01 ↔ K24 |
| D206 | 7 film · efor fiili promptta var, ödeme kanalı ve saniyesi yok (COUNTED_TURN ⑧ **0,0**) | 6 efor klibinin her birinde ≥1 saniyeli ödeme satırı: `4.0s — her grip locks and the bar stops for half a second` biçiminde; kanal omuz · kol yeni · nefes · kadans | K13 · K16 · K17 · K18 · K19 · K20 |
| D207 | 4 film · patlama/yorgunluk bir kesme sonra yok; sonraki imaj bible'ın NÖTR bedeninden doğuyor | YORGUNLUK dizisi 0-6, ardışık düşüş ≤1; sahnenin 2.+ klibinde `CONTINUOUS ACTION:` bedeni kelimesi kelimesine taşır (omuz düşük · nefes · eldeki nesne) | 17 klip (sahne içi 2.+ olanlar) |
| D202 | 5 film · merkezî seçim ve bedel bedende okunmuyor (`THE CHOICE IS INVISIBLE`) | ÇAPA ÜÇLÜSÜ (üçü de AYNI kanalda önce/sonra): CHOICE K16 el+omuz · COST K17 omuz+nefes · FINAL K23 el+omuz — BEFORE K03 (iki eldiven konsol rayında kapalı, omuzlar yüksek) ↔ AFTER K23 (iki eldiven açık ve boş, omuzlar düşük) | K16 · K17 · K23 |
| D179 | imaj promptu değişimin SONRASINI yazdı; bedel EN GENİŞ kuruluma yazıldığı için 3 pikselik olay oldu | her IMAGE promptu 0,0 saniyeyi yazar; K17 ve K20'nin imajı değişimin ÖNCESİ; bedel/seçim klipleri MS ve daha yakın — fark kadrajın kısa kenarının ≥1/8'i | K16 · K17 · K19 · K20 |
| D213 | 4 film · temas kesmeden önce, sonuç kadraj dışında | temaslı 7 klipte üç satır AYNI klipte (TEMAS · DEĞİŞİM · SONUÇ ≥1 s), nesne merkez üçte birde, temas ilk 2 saniyede kurulu (%5,9 bandı) | K06 · K09 · K12 · K14 · K19 · K20 · K21 |
| D141 | kurgu kapısının üç satırı geçti, filmin twist'i ekranda yoktu | FİNAL VURUŞ KANITI: K24 · 236,0 s · oyukta TEK filiz — sayılabilir, 1 adet, adı konabilir; yoksa final teslim edilmemiştir | K24 |
| D157 | novumun taşıyıcısı TEK KARE testini kendi taşıyıcısıyla geçmiyordu; iki mercek onu "tekrar" sayıp kesme listesine yazdı | TEK KARE cümlesi taşıyıcıyı ADIYLA taşır (üç halkanın arasındaki kafesli güneş); K21'de kadrajda başka hiçbir şey hareket etmez — rakip olay 0 | K02 · K21 |
| D78 | dört çevresel sayaç ve filmin bedeli tek karede kanıtlanmadığı için görünmedi (`COUNTER: NONE`) | ⭐ ölçek iddiası K02'de TEK KAREDE iki ucuyla: küre + gövdenin sırtındaki KAPI BOYUNDA tek aydınlık pencere aynı kadrajda — "taşınabilir bir güneş" hafıza istemeden okunur | K02 |
| D139 | düz sırt kilidi 6 sahnenin 5'inde tuttu; düştüğü tek sahne kameranın ARKAYA geçtiği sahne | ⭐ kamera arkayı gören TEK klipte (K06 · kurulum G · OTS) pozitif sırt cümlesi: "her back is turned to the camera and fully visible: one continuous ribbed surface from collar to hip, closed and smooth, the two shoulder caps wrapping over its upper edge, a long worn cloak hanging from them to her calves" | K06 (film boyunca sırtı gören tek kurulum) |
| D95 | "optik berrak, renksiz, yansımasız" vizör ekranda "kask yok" okundu — görünmez kılınan kilit doğrulanamaz | mühürlü durumun ÜÇ GÖRÜNÜR İŞARETİ her insanlı promptta: ① kalın koyu çerçeve ② yaka halkası kadrajda ③ pane'in üst kenarında TEK ince spekülar çizgi — panenin taşıdığı tek yansıma | insanlı 20 klip |
| D147 | üç sabit aşınma izi tozlu odada tutmadı; model kirletti, sonra bible'a dönüp temizledi | KIRAĞI MERDİVENİ monotonik ve GLOBAL: K01-K03 pas yok · K04'ten itibaren pelerin kenarı ve omuz kapaklarında soluk kırağı pası · K15'ten itibaren aynı pas daha yoğun; gemi içinde de ÇÖZÜLMEZ (gövde içi de soğuk ve mühürlü) | bütün klipler · SPEC C |
| D123 | film 0 kare şiddet taşıyordu; o sıfırı KORUMAK için yazılan yasak kelimeleri iki doruğu reddettirdi | yasak SİLİNİR, malzeme TARİF edilir: `wounded` · `dying` · `dead` · yıkım fiilleri ve `dull orange glow` YAZILMAZ; gemi "goes dark in the stated order", küre "a deep red-gold light on the underside ribs" | K17 · K18 · K21 (en red-riskli üçlü) |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

> ⛔ Bu satırlar "atlandı" demek DEĞİLDİR: her biri BAŞKA BİR ADRESTE koşuyor.
> Tavan 20 olduğu için numaralı kilit satırı almadılar (㉕).

| ders | neden bu filmde numaralı kilit satırı almadı |
|---|---|
| D1 · D34 · D45 · D138 · D214 · D215 | V3-S iskeleti + §5.1 çekirdek + üretim defterinin üç kutusu bunları YAPISAL olarak taşıyor; film başına karar gerekmiyor |
| D169 | D206 ile aynı cümlede uygulanıyor (sözlük D169'un, saniye D206'nın) — iki numara tek satır harcamasın diye D206 seçildi |
| D175 | çıplak-deri negatifi ÜÇ BÖLGELİ olarak §5.2 sahneye özel cümlesine yazıldı; zorlanma cümleleri giysi yüzeyinde |
| D58 | tekrar eden varlık kartları `GUNES_MEZARI_REFERANS_PAKETI.md`'de (6 kayıt) — orada sayfa, burada satır olmasın |
| D176 · D174 | World Bible tek zemin cümlesi + yön cümlesinin nesneye bağlanması yazım standardı; 03_SAHNE_SIRALAMASI'nda kurulum satırlarına iniyor |
| D180 · D216 | ikisi de `GUNES_MEZARI_MUZIK.md` dosyasının işi (kurguda hard mute + katman tavanı); prompt kilidi değil |
| D200 | ortam kartının PHYSICS satırı tek g'yi zaten taşıyor; ayrı kilit satırı çift kayıt olurdu |
| D211 | 03_SAHNE_SIRALAMASI'nın HOOK MİMARİSİ bloğunda üç sayıyla duruyor |
| D217 | replik 1 satır; İŞLEV hücresi PLAN replik tablosunda — ayrı kilit satırına değmez |
| D90 · D152 | ölçen kenar ve elde alet kuralları sahne çalışma dosyalarında (K19 · K20) uygulanıyor |
| D198 · D201 | ETİKET filme uymuyor: 0 g yok, vakum yok (çizelgede "—") |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_KEPT_LIGHT | ④ kurgu kapısı d | DÖNGÜ/KAFİYE BAŞARISIZ: S0 (0,5 s) tepeden CU ↔ S24 (248 s) ağzın ALTINDAN alt açı — aynı kurulum değil, kameranın YERİ değişmiş | K24'ün CAMERA satırı K01'den kopyala-yapıştır; iskelet `A … A`; ⑨ KADRAJ merceği bunu ilk okuyacak |
| THE_KEPT_LIGHT | ⑩ önerme kapısı | NOVUMUN SINIRI SIZDI: kural ağzın ALTINDA kalmalıydı, bırakılan kesici güvertenin ÜSTÜNDE 3 s havada durdu; 8 merceğin hiçbiri yazmadı | ⭐ kurgu sözleşmesinin SINIRI her PHYSICS satırında: "anything she lets go falls and reaches the ice in about a second" — küre DIŞINDA hiçbir şey havada durmaz; SPEC göz kapısı bunu klip başına sorar |
| THE_KEPT_LIGHT | ⑪ ölçüm | kuyruk kartı 5,0 s (SPEC: 0) · filigran 6/6 örnekte · planlı sessizlik hiç gelmedi · −16,4 LUFS / +0,9 dBTP | SPEC E'ye dört makine kapısı + ihraç satırı; üretim defterinin filigran kutusu KAPI 0'da işaretlenir |
| THE_HEALING_GROUND | ⑪ ölçüm | başlık kartı 4,99 s ve kartın GÖRSELİ filmin dünyası değil (turuncu gök + dev gezegen ↔ filmin soluk kum paleti) | KAPAK ayrı dosyadır ve kurgu klasörüne GİRMEZ; kapak promptunda başlıklı satır kullanılmaz [D72 3b] |
| THE_HEALING_GROUND | akış | SPEC ve mod-D paketi VARDI, operatör çıplak rubrik yapıştırdı → 13. mod V filmi | SPEC'in başına tek satır: "bu dosya rubriğin BAŞINA yapıştırılır, yoksa koşu mod V'dir" |
| THE_COUNTED_TURN | ⑧ EFOR | **0,0 NOBODY PAYS** — 6 iş olayının 6'sında beden ödemiyor (0:10 · 1:10 · 1:20 · 1:30 · 3:00 · 3:40) | D206 kilidi: 6 efor klibinde saniyeli ödeme; ⑳ kapısı sözlüğü tanıyor |
| THE_COUNTED_TURN | ⑦ AKSİYON | temas cümlesi 22/25 promptta YAZILIYDI ve 4 temas penetrasyonu geldi | cümleye güvenilmiyor: temas ilk 2 s'de kurulu (§3b ①) + görünür ARA KATMAN (çelik halka / çubuğun kılıfı) + iki yönlü temas cümlesi |
| THE_CRACKED_HELMET | ② DEVAMLILIK | kostüm siyah↔beyaz 12 sahnede 5 kez · amblem omuz↔sırt ışınlandı · S7'de vizör KAYBOLDU · göğüs kutusuna `ORION` yazıldı | tek giysi DEĞERİ (`matte graphite`, "black" yazılmaz) · amblem HİÇ YOK · vizör 24/24 · promptta hiçbir büyük harfli jeton yok |
| THE_CRACKED_HELMET | ⑨ · ⑩ | 2,1 `RHYME BROKEN` · 2,0 `THE CHOICE IS INVISIBLE` | D210 + D202 kilitleri; ÇAPA ÜÇLÜSÜ SPEC'e blok olarak yazıldı |
| THE_SOLAR_MIRROR | ① KARE | ⭐ `S04` SAHNE ETİKETİ hava kilidi gövdesine BASILDI — metin yasağı 12/12 promptta yazılıyken | promptta `S04` · `K14` · `PHASE 2` gibi hiçbir kısa büyük harfli dizge yok; klip numarası yalnız `Clip 14 of 24.` cümlesinde |
| LOW_POWER | teknik | **Parçacık 2/10 — projenin en düşük tek skoru**; kir/toz deseni her karede yeniden üretiliyor; mavi gün batımında bloom + motivasyonsuz dolgu | kırağı GLOBAL bitiş (konumlu leke değil) · S7'nin gün doğumunda `0% bloom` + "the air between carries no haze or halo" + dolgu KAYNAKLI (yalnız güneş ve kar yüzeyi) |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **YR** yapısal red | insansız sahne + uzun `NEGATIVE:` bloğu + `Exactly 0 human figures` | ✅ GEÇTİ: NEGATIVE bloğu TEK pozitif satıra indi, boş kadraj VARLIK olarak tarif edildi | ⭐ **K01 · K02 · K04 · K11 · K21 · K24** — altısı insansız; negatif bloğu kısaltılır, insan sayısı cümlesi YAZILMAZ, boşluk pozitif tarif edilir |
| **PB** kompozisyon | **bedenden bir şeyin çıkarılması** (kask çıkarma) | ✅ GEÇTİ: sahne baştan yazıldı — kimse bir şey çıkarmıyor, vuruş başka nesneye taşındı | anahtar GEMİNİN konsolunda, kadının GÖĞSÜNDE değil; giysiden hiçbir şey çıkarılmıyor (D89 ile aynı kapı) |
| **PK+PB** | tehlike çerçevesi: `wounded ship` + `dull orange glow` | ✅ GEÇTİ: replik değişti + tehlike sözlüğü ayıklandı | K17-K18: gemi "goes dark in the stated order" · küre "a deep red-gold light on the underside ribs" — `wounded` · `dying` · `glow` yok |
| **PK** kelime | yasak kelimeleri NEGATİF blokta yazmak (`gore` · `blood` · `corpse`) | ✅ GEÇTİ: yasak silindi, malzeme tarif edildi | K21 (küre salıverme): `no explosion` · `no fireball` · `no flash` YAZILMAZ; yerine pozitif: "the rings swing outward to their stops and the sphere lifts clear of them at one steady rate" |
| **PK** kelime | **milliyet ifadesi** (`Israeli-American` · `Turkish woman`) | ✅ GEÇTİ: milliyet satırı silindi, yalnız fiziksel tanım | 48/48 promptta milliyet · gerçek kurum · gerçek kişi adı 0 |
| **PK** kişi tanımlama | tek kişide YEDİ kimlik özniteliği üst üste (kesin boy + ten + saç + yaş + yüz işareti) × her promptta | ⬜ önerilen: yığın sökülür, boy GÖRELİ, yüz yalnız konu olduğu sahnede | kimlik yığını ≤3; kesin boy yok; yüz yalnız 4 klipte (K03 · K12 · K16 · K23) |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet  (tavanda · ㉕)
QA ARIZASI:         11 adet  (5 film kaydı)
RED SINIFI:         6 adet   (4 sınıf: YR · PB · PK · PK+PB)
⛔ EN PAHALI ÜÇÜ:
   ① D59 + D192 KÜRE — filmin tek iddiası ve tek büyük fizik ihlali aynı
     nesnede: yasak kökler pozitif gövdede yenilir ve model ateş topu çizer
   ② YAPISAL RED (K01·K02·K11·K24) — dört insansız klip, deponun tek
     ölçülmüş YR vakasının profilini birebir taşıyor
   ③ D89 ÇIKARMA — film 4 klipte bir şey söküyor; ölçülmüş vaka modelin
     KASKI çıkardığını gösteriyor ve o kare politika reddi de aldı
```
