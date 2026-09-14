# 🧾 THE_BENT_GRASS — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D1 · D22 · D68 | Model klip içinde kesme uyduruyor (8/8 filmde) | Her sahne TEK kesintisiz 10 s çekim; kesme yalnız kurguda. Sahne içi kesme İSTENMİYOR → "no cuts" cümlesi her VIDEO promptunda kalır | 14/14 |
| ⭐ D86 · D104 | İki figürün sol-sağ dizilimi kesmeler arası yer değiştiriyor (Third Dune 0:10↔0:20) | **A hep ekran SOLUNDA, B hep ekran SAĞINDA; sıra hiçbir karede değişmez.** Cümle iki figürün göründüğü HER prompta birebir | iki figürlü tüm sahneler |
| ⭐ D2 · D18 | Arka plan canlısı morph ediyor; hayvan kayarak yürüyor | Uzaylı UZAKTA = siluet + sığ DOF, YAKINDA = her bacak ayrı kalkar-basar, gövde adımla senkron yükselir; "kayma / süzülme" 0 kare | uzaylının göründüğü tüm sahneler |
| ⭐ D192 · D123 | Negatif anatomi listesi modele anatomiyi ÜRETTİRİYOR | Anatomi POZİTİF ve SAYILI: `exactly four jointed legs, one body, no additional limbs anywhere in frame` — "no extra legs" biçimi YASAK | uzaylının göründüğü tüm sahneler |
| ⭐ ADAY-8 (GÖZLEM) | WORLD bloğu canlının tam anatomisini yazınca kısmi reveal çöküyor | K0-K3 kademelerinde uzuv/göz SAYISI hiçbir blokta geçmez; sayı yalnız TAM REVEAL sahnesinde | reveal merdiveni |
| D20 · D69 · D140 | Klon/ikinci figür sıcak noktası: araca biniş-iniş | **Biniş ve iniş hareketi kadraja ALINMAZ** — araç sahnelerinde figürler ya zaten dışarıda ya zaten içeride | iniş aracı sahneleri |
| D8 · D55 | Bible'sız üretimde kıyafet her sahnede yeniden icat ediliyor (Kostüm-Prop 1/10) | İki suit tarifi de HER promptta TAM ve birebir; kısaltma yok, "[BIBLE]" atfı yok | 14/14 |
| D37 · D57 · D147 | Ekipman durumu sahneler arası açılıp kapanıyor; yıpranma sıfırlanıyor | Kask **14/14 kapalı, 0 değişim**; çimen sürtünmesi/toz yeşil lekesi MONOTONİK üç kademe (K0→K1→K2), geri dönüş 0 kare | 14/14 |
| ⭐ D79 · D95 · D146 | Vizör kubbeleşiyor / opaklaşıyor; yüz okunmuyor (Ekipman 4/10) | `optically clear, zero tint, zero mirror coating; the face stays fully readable at every head angle` + düz sırt cümlesi sırtı gören her karede | 14/14 |
| ⭐ D48 | "grass" kelimesi Dünya çayırı ve Dünya bitkilerini çağırıyor | Negatifte Dünya bitkisi ADIYLA yasak (buğday · yulaf · bambu · saz · karahindiba · ağaç · çalı); pozitifte gezegenin kendi otu tarif edilir: tek tip, tek yükseklik bandı, tek renk ailesi | 14/14 |
| ⭐ D145 | Uçsuz ovada model kanyon/uçurum/sırt uyduruyor | HORIZON LOCK: `flat to the horizon in every direction — no cliff, no canyon, no ridge`; en büyük arka plan nesnesi ADLANDIRILIR (iniş aracı) | 14/14 |
| D4 · D44 · D90 | Temas iz bırakmıyor; düşük-g olmayan yerçekimi ağır çekim okunuyor | Her adımda çimen EZİLİR ve ezik KALIR; `normal human walking pace, real time` + adım hızı m/s SPEC'te | yürüyüş sahneleri |
| D6 · D41 | Arka plan morph; yumuşak ışık bloom sanılıyor | Ova dokusu SABİT: aynı yükseklik bandı, aynı dalga yönü; atmosferli gezegende yumuşak gölge ve dolgu ışığı MEŞRUDUR, hata değil | 14/14 |
| ⭐ D154 · D4 | Tekrar eden doğa olayı VARLIK gibi davranıyor | Çimen dalgası tek yönlü ve TEK kaynaklı (rüzgâr); yön 14/14 sahnede aynı ekran yönünde | 14/14 |
| D56 · D59 · D67 | Sözcük fiziği çağırıyor; yasak yerine POZİTİF tarif gerekiyor | "sürü/akın/saldırı" değil; hareket ve mesafe tarif edilir. Yasak cümle yerine pozitif kilit | uzaylı sahneleri |
| D45 · D138 · D155 | Prompt iskeleti ve ölçü ekrana yazı olarak sızıyor | Prompt gövdesinde etiket, köşeli parantez, karakter adı, metre/derece/f-sayısı YOK; ölçü SPEC'te metre, promptta gövde boyu | 14/14 |
| D34 · D13 · D70 · D72 | Jenerik/başlık kartı ve HUD metni kurguya sızıyor (5+ film) | Ekran metni 0,0 sn — kart, HUD, isimlik, rakam 0 kare; kurgu kapısında tek tek işaretlenir | 14/14 + kurgu |
| D179 | IMAGE promptu sahnenin ortasını tarif edince video oradan başlıyor | IMAGE promptu **t=0** karesidir; değişim içeren sahnede başlangıç karesi değişimin ÖNCESİDİR | 14/14 |
| ⭐ D157 · D172 · D73 | Novum taşıyıcısı türetilmiş fenomene yüklenince ekrana hiç gelmiyor | Novum TEK KARE cümlesi taşıyıcı NESNENİN adını içerir ve o nesne ilk 20 saniyede kadrajda | S0-S1 |
| D158 | Merkezî seçimden sonra karakterin kararı yok, başarısız deneme yok | Merkezî seçimden SONRA en az bir seçim daha + bir BAŞARISIZ deneme | doruk sonrası |
| ⭐ D168 | Baştan üretilen filmde elde hep KURULUM kalıyor (Sinking Stake: eksik 11 sahne ardışık ve filmin SONU) | ÜRETİM SIRASI: doruk → merkezî seçim → kapanış imajı → S0 → kalanı | üretim planı |
| D141 | Final vuruşu kanıtlanamıyor | FİNAL VURUŞ KANITI: tek karede sayılabilir, adı konabilir nesne + saniyesi + adedi | S13 |
| D181 | Teslim sınıfı belirsiz (ham zincir ↔ kurgu) | QA_SPEC'e teslim sınıfı yazılır | SPEC |
| D122 | Replik/doruk saatleri elle yazılınca tutmuyor | Saniyeler HESAPLATILIR: sahne(n) = hook + (n−1)×klip | SPEC |
| D124 | Klip süresi tercih sanılıyor | Klip süresi ARAÇTAN ölçülür (10 s = 8 s + 2 s extend); ızgara ölçümle doğrulanır | SPEC |
| D83 | "Müziksiz" sahne dijital sessizlik olarak teslim ediliyor | Ortam yatağı envanteri: çimen hışırtısı · rüzgâr · suit fanı · nefes; yatak kurguda TEK PARÇA | 14/14 + kurgu |
| D78 | Planlı sayaç ekranda okunmuyor (13 filmin 11'inde N/A) | Sayaç ölçeğin İKİ UCUNU aynı karede gösterir: ezilmiş çimen hattı + ufka kadar ezilmemiş ova | sayaç sahneleri |
| D84 · D42 | Metin kilidi sahneler arasını tutmuyor (toz 42 promptta yazılıydı, kırıldı) | Yıpranma kademesi SAHNE ADIYLA yazılır ve kademe değişimi SINIRDA olur | 14/14 |
| D117 · D129 · D165 | SPEC ayrı dosyada yoksa / paket yoksa mercek mod V koşuyor | QA_SPEC ayrı dosya + `rubrik_paketle.sh` paketi SPEC ile AYNI GÜN | paket |
| D74 | Kapı kaydı yazılmayınca kapı koşulmamış sayılıyor | Bant/kart sapmaları ve referans paketi kararı PLAN'a TEK SATIR gerekçeyle yazılır | PLAN |
| D167 · ⑲ | Kişi başına 7 öznitelik politika reddi getirdi | Tek pencerede EN ÇOK 3 kişi özniteliği; ayrım biyometriden GEOMETRİYE | 14/14 |
| D139 | Sırt negatifle tarif edilince model sırt ünitesi çiziyor | Sırt POZİTİF yazılır: `flat back with a single vertical spine seam` (A) / `a single rectangular pack` (B) | sırtı gören kareler |
| D169 · D175 | Zorlanma kanalı yok; çıplak deri sızıyor | Zorlanma eldiven/kol kumaşında görünür; üç bölgeli çıplak-deri negatifi | efor sahneleri |
| D193 · D47 | Işık takvimi yazılmayınca güneş sahneden sahneye zıplıyor | Işık takvimi tablosu: güneş azimut/yükseklik 14 sahnede monotonik; gölge yönü ondan TÜRETİLİR | 14/14 |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_MIRROR_FAUNA | ① KARE | 00:20 · uzaylının ön sağ bacağı yüzeyde KAYIYOR | Her uzaylı promptunda dört bacağın SIRAYLA kalkıp bastığı yazılır; temas noktasında çimen ezilir (temas kanıtı) |
| THE_MIRROR_FAUNA | ② DEVAMLILIK | 01:20-01:30 · varlığın uzuv rengi sarı→cyan; uzuv sayısı 4-6 arası oynuyor | ANATOMİ + PALET tek cümle, 14 promptta birebir kopya; uzuv sayısı yalnız tam reveal sahnesinde ve tek sayı |
| THE_MIRROR_FAUNA | ② DEVAMLILIK | 00:50-01:10 · figürün elindeki alet üç kesmede üç farklı nesne | Elde alet SAYISI ve BİÇİMİ bible'da; alet taşınan sahneler sahne çalışmasında tek tek işaretlenir |
| THE_MIRROR_FAUNA | ①⑪ | 01:52 · vizör içinde kırmızı alfanümerik HUD metni → REGENERATE | Vizör içi ışık YAZI DEĞİL: `a faint even glow inside the helmet, no symbols, no digits` |
| THE_MIRROR_FAUNA | ⑥ FİZİK | 01:50 · 1 m düşüş 1,2 s → 0,14 g; kilit 0,7 g idi (FAIL) | Yerçekimi kilidi düşüş SÜRESİYLE yazılır ve SPEC'te ölçülebilir: "1,0 m serbest düşüş ≈ 0,45 s" (1 g bandı) |
| THE_MIRROR_FAUNA | ⑧ EFOR (2.0) | Ağır giysiyle yürüme, eldivenle kadran çevirme — hiçbirinde zorlanma yok | Her iş olayının BEDENSEL faturası promptta: omuz düşmesi · kavrayışın sıkılaşması · nefes ritmi · bir saniyelik durgunluk |
| THE_MIRROR_FAUNA | ②⑦⑫ | 02:00 · S13 = S12'nin BİREBİR kopyası (aynı klip iki kez) | Kurgu kapısı: klip sayısı = sahne sayısı; aynı klibin ikinci kullanımı DOLGUDUR |
| THE_MIRROR_FAUNA | ⑫ HOOK | 02:39 · başlık kartına kesiliyor, döngü ölüyor | Kart 0 kare; son kare ilk kareye KAFİYE ile bağlanır |
| THE_UPWARD_FALL | ⑪ ölçüm + kare | 186 s · plan `0 bacak · 0 adım · hiçbir şey zemine değmez` derken canlı İKİ SÜTUN UZUVLA zemine bastı | Bu filmde canlının bacakları ZATEN dört; kilit "kaç bacak" değil "**bacak sayısı DEĞİŞMEZ ve gövde zemine değmez**" biçiminde yazılır |
| THE_UPWARD_FALL | ⑪ ölçüm | 216 s · plan 40 m'lik yarık, ekranda 2 m'lik hendek (ölçek çöküşü) | Her büyük oluşumun yanında ÖLÇEK ŞAHİDİ: ön planda figür / tekrar eden birim / kadrajı taşan kenar |
| THE_UPWARD_FALL | ⑪ ölçüm | 195-199 s · ÇIPLAK ÖNKOL — solunamaz atmosferde giysi kilidi delinmiş | Giysi bütünlüğü cümlesi (bilek-eldiven-manşet kapalı) sırtı/kolu gören her karede |
| THE_UPWARD_FALL | ⑪ ölçüm | Döngü KIRIK: jest tuttu, DÜNYA tutmadı (ilk kare başka orman, son kare başka) | Kafiye çiftinde yalnız jest değil ORTAM da kilitlenir: aynı konum, aynı kurulum harfi, aynı ufuk |
| THE_UPWARD_FALL | teslim | filigran 225/225 saniye · kuyrukta 5 s kart · −16,1 LUFS / 0,0 dBFS | Teslim kapısı: filigran 0 · kart 0 · −14 LUFS / −1,0 dBTP; sekiz mercek bunları KAÇIRDI, ölçüm kapısı yakaladı |
| THE_STILL_SWARM | ⑦ AKSİYON | S6 novum taşıyıcı sahnesinde vuruş yuvası BOŞ — sekiz merceğin sekizi de novum'u görmedi | Novum taşıyıcısı ilk 20 saniyede ve TEK KAREDE; taşıyıcı nesnenin adı TEK KARE cümlesinde |
| THE_STILL_SWARM | ② DEVAMLILIK | `Counter Logic: N/A` — planda 8→8→7→5→5→2→0 sayacı vardı | Sayaç kadrajda ölçeğin iki ucunu birden gösterir; sayaç sahneleri sahne çalışmasında adlandırılır |
| THE_STILL_SWARM | ④ + ızgara | 14 klipten 13'ü teslim; eksik olan S13 = FİNAL VURUŞU + TWIST + LOOP | Üretim sırası doruk/final ÖNCE [D168]; final vuruş kanıtı SPEC'te |
| THE_ROSE_COAT | ② DEVAMLILIK | 0:10 bot siyah ↔ 0:40 bot beyaz — iki figürü ayıran TEK kanal (renk) kırıldı | Ayrım DÖRT kanala yayılır: rol şeridi rengi+kolu · sırt silueti · bilek düzeni · kişisel eşya |
| THE_ROSE_COAT | ① + ② | 2:00-2:09 merdiven tırmanışı — plan `BİNİŞ 0 kare` diyordu | Biniş/iniş/tırmanış hareketi kadraja alınmaz; araç sahnesi ya "zaten dışarıda" ya "zaten içeride" |
| THE_ROSE_COAT | kapı ④ | İNSAN ŞERİDİ notasyonu rubriğin üretemeyeceği biçimde yazılmış (`2222…` ↔ `1111…`) | Şerit rubriğin üretebildiği biçimde yazılır; gövde SAYISI ayrı satırda ("her sahnede tam 2 gövde") |
| THE_ROSE_COAT | ④ HİKAYE | Kesme listesi filmin DORUĞUNU, KAPAK KARESİNİ ve iki virali kesiyordu | PLAN ve SPEC'te `⛔ KESİLEMEZ` etiketi: viral aralar · doruk · kapak karesi |
| THE_DEEP_PRESSURE | ② DEVAMLILIK | Kostüm-Prop **1/10** — 13 sahnelik filmin dosyasında 2 sahne, Character Bible YOK | BIBLE GATE: iki karakter + uzaylı + ova bible'ı yazılmadan hiçbir sahne promptu yazılmaz |
| THE_DEEP_PRESSURE | ② DEVAMLILIK | Tekrar eden portal iki sahnede iki farklı yer (S4↔S8) | RECURRING ENTITY kartı: iniş aracı · ova kenarı · ezilmiş çimen hattı · uzaylı — dördü de kimlik kartıyla |
| THE_HERD (ek kayıt) | 🧩 MANTIK | Kask baloncuğu kayboluyor ve geri geliyor — takvim 15/15 kapalı yazılıydı | Kask durumu her promptta AYNI cümleyle; ara durum/geçiş 0 kare |
| THE_HERD (ek kayıt) | belge kontrolü | Rapor "gökteki sürüyü sil" dedi — sürü filmin ÖNERMESİYDİ | Önerme kapısı: sürü bu filmin de önermesidir; rapor onu kesmeyi önerirse UYGULANMAZ [D87] |
| THE_HERD (ek kayıt) | belge kontrolü | Çehov nesnesi (fener) kadrajın KENARINDA kurulunca kurulmamış sayıldı | Kurulan her nesne kadrajın merkezine yakın ve ÖDEME SAHNE NUMARASI yazılı |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK | Milliyet ifadesi (`Israeli-American` · `Turkish woman`) — DOĞRULANMIŞ red | Milliyet satırı silindi, yalnız fiziksel tanım kaldı | İki astronotun kimlik bloğu — milliyet 0 kelime |
| PK | `dead` · `body` · `does not breathe` · `decay` · `skeletal` | Pozitif tarife çevrildi: "completely inert · absolutely motionless" | Uzaylının hareketsiz durduğu kare(ler) — "cansız/ölü" sözcüğü yazılmaz |
| PK | Yaratık sözlüğü: `tentacle` · `mutant` · `deformed` (⚠️ hipotez, depoda ölçülmedi) | Bedava nötr hâl: `elongated organic appendages` · pozitif sayım `exactly four jointed limbs` | Uzaylı tarifi — 14 promptun tamamı |
| PB | Bedenden bir şeyin ÇIKARILMASI (kask/eldiven) — iki red | Nesne sahneye ZATEN çıkmış olarak girer; kimse bir şey çıkarmaz | Kask 14/14 kapalı — çıkarma sahnesi YOK |
| PB | Tek insan + gövdeye yönelen kuvvet vektörü | Kuvvet NESNEYE taşındı; insan kuvvetin YANINDA durur | Uzaylı ile temas/yaklaşma anı — vektör astronota değil ekipmana/zemine |
| PB ⑥ | Yüzü kapatan ekipman = anonimlik imzası (bu deponun standart malzemesi) | Yüz GÖRÜNÜR kılınır (D79 optik berrak vizör) | 14/14 — vizör cümlesi kısaltılmaz |
| PB ⑦ | Kırmızı ton yoğunluğu + yakın plan | Kırmızı kaynağa bağlanır ve çevrelenir | Bu filmde kırmızı ışık kullanılmayacak; yeşil-altın palet |
| YR | İnsansız sahne + uzun `NEGATIVE:` bloğu → "I'm having a hard time…" | NEGATIVE kaldırıldı, tek pozitif `Style:` satırı | İnsansız ayrılış kodası (S12-S13 adayı) — negatif blok KISALTILIR |
| TK | Aynı oturumda 0 başarı (5/0 · 3/0) | Üçüncü yeniden yazım YOK → PROB koşusu | Üretim kaydı: red gelirse defter satırı AYNI GÜN, MOTOR + İLERLEDİ yazılır |
| MÇ | Üretim ilerleyip SONDA düştü (maskeli çıktı reddi) | Kelime değil KARE reddedildi → kompozisyon eksenine geç | Kalabalık/sürü kadrajı — kütle "heykel gibi" değil, FAUNA olarak adlandırılır |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        34 adet
QA ARIZASI:         25 adet
RED SINIFI:         10 adet
⛔ EN PAHALI ÜÇÜ:
   ① CANLI — dört ayaklı uzaylının lokomosyonu, uzuv sayısı ve rengi
     (MIRROR FAUNA'da üçü de kırıldı; UPWARD FALL'da anatomi kilidi delindi)
   ② İKİ FİGÜR — dizilim + kadro ayrımı + biniş/iniş klon sıcak noktası
     (ROSE COAT'ta ayrım tek kanaldaydı ve kırıldı; şerit kapısı hiç koşamadı)
   ③ EKSİK FİNAL — planın doruğu/finali kurguya girmiyor
     (STILL SWARM S13 · UPWARD FALL S24 · üç ayrı filmde aynı arıza)
```
