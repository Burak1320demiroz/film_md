# 🧠 THE_BENT_GRASS — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     SAHİP VERDİ (AI seçmedi — gerekçe aranmaz)
② FORMAT:   Yatay 2-4 dk  → kart §2.2 · bölüm sayısı 2 (ortadan: S0-S6 · S7-S13)
③ SAHNE:    14  → sahip verdi ("Diğer" · 14)
   BANT KONTROLÜ: §2.2 bandı 12-18 → 14 BANT İÇİNDE, sapma yok, D74 kaydı gerekmez
   ⭐ 14 sahne §2.2'nin "14+ sahnede opsiyonel insansız ayrılış kodası"
     satırını AÇAR — bu filmde koda KULLANILIYOR (S12-S13)
④ REFERANS PAKETİ: YAZILMASIN (sahip kararı)
   PLAN'a düşecek TEK SATIR gerekçe [D74]:
   "Referans paketi sahibin kararıyla yazılmadı; T1 (kask/vizör) ve T4
    (insan dışı canlı) tetikleyicileri DOĞRU olduğu için biçim kilidi
    METNE taşındı: dört eklemli bacak sayımı, gövde-boyu oranı, optik
    berrak vizör ve düz sırt cümleleri 14/14 promptta BİREBİR yazılır."
   ⚠️ Kayıt: D146'nın üç ölçülmüş vakası (SKYLIGHT 1 filmde 3 kask ·
     YERÇEKİMİ F2 vizör geometrisi 0/6 · STANDING WIRE 24 klipte kubbe)
     paketsiz filmlerde biçim kilidinin metinle TUTULMADIĞINI gösterdi.
     Bedel bilinerek üstlenildi; telafi §5b'nin altındaki üç satırdır.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "büyük full cimenlik bir gezegene giden 2 astranot olucak ve burda
        4 ayaklı uzaylılar olucak kalanı sen getirrisin"
REPLİK: YOK — talep cümlesinde diyalog geçmiyor → replik zinciri AÇILMAZ.
        Film 0 replik yazılır (SES_VE_DIYALOG: depoda replikli film 0/79,
        PROB B hiç koşulmadı; ekranda konuşan ağız iki riski birden açar).
```

| sahibin isteği | fiziksel sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "full çimenlik gezegen" | `grass` sözcüğü Dünya çayırını ve Dünya bitkilerini çağırıyor [D48] | Gezegenin KENDİ otu: tek tür, tek yükseklik bandı (diz hizası), soluk altın-yeşil; Dünya bitkisi ADIYLA negatifte yasak | D48 · ova 14/14 sahnede aynı biyom |
| "4 ayaklı uzaylılar" (çoğul) | `UZAYLI_VARLIK` §0① **TEK VARLIK** kuralı çoğulu yasaklıyor | **FAUNA olarak yeniden tanımlandı:** tek TÜR, tek şablon, tek ihlal; birey sayısı SAYIYLA kilitli (yakın bantta TAM ÜÇ · uzak bantta ufukta TEK KESİNTİSİZ HAT). Uygarlık, alet, iletişim, ikinci tür YOK | ⛔ SAPMA KAYDI aşağıda §3b |
| "2 astronot" | İkinci figür deponun ölçülmüş 🟠 riski (KART 4 · D86 · D69) | Kabul edildi ve DÖRT KANALLA ayrıştırıldı (şerit · sırt · bilek · eşya) + dizilim kilidi + biniş/iniş 0 kare | D86 · D69 · D77 |
| "büyük gezegen" | Ölçek sözle yazılamaz; model uçurum/kanyon uyduruyor [D145] | HORIZON LOCK: ufka kadar düz; en büyük arka plan nesnesi ADLANDIRILIR (iniş aracı); ölçek şahidi her geniş planda | D145 · D126 |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 2-4 dk                      → §2.2 kartı
ORTAM:         §3.3 DÜNYA ATMOSFERİ              → ⭐ kart ⏸️ "kullanımda değil"
               ama kartın kendi satırı diyor ki: "Dünya benzeri atmosferi
               olan bir GEZEGEN konsepti bu fiziği kullanır… bu ortamda
               film yazılırsa İLK FİLM YENİ REFERANS OLUR."
               → Bu film o ilk filmdir. [D74 kapı kaydı · PLAN'a yazılır]
   TETİKLEDİĞİ ZORUNLU SATIRLAR:
     toz hızlı çöker ve yere oturur · gölge YUMUŞAK ve bu MEŞRU [D41] ·
     dolgu ışığı VAR · dış ses NORMAL yayılır · rüzgâr GERÇEK kuvvet
     (ama abartılmaz — model fırtınayı şişiriyor) · nefes soğukta görünür
   ⛔ VAKUM NEGATİF BLOĞU BU FİLME YAPIŞTIRILMAZ: "mutlak siyah gölge",
     "atmosferik saçılma yok", "süzülen parçacık yok" cümleleri burada
     FİZİK HATASI yazdırır [UZAY_USSU §6 uyarısı].
TÜR:           bilimkurgu · dal: sert uzay gerilimi + ilk temas → §4.1
KLİP SÜRESİ:   10,0 s  ⛔ ARAÇ AYARI, tercih değil [D124]: Veo 8 s + 2 s extend.
               Üretimden sonra `olcum_kapisi.sh` ızgarayı ÖLÇER; plana
               yazılan sayı ölçümle değişebilir ve ölçüm hakemdir.
SAHNE SAYISI:  14   RUNTIME: 10 + (14−1) × 10 = 140 s = 2:20  (hesaplandı, elle yazılmadı)
BÖLÜM SAYISI:  2    (§2.0 — formattan gelir; ortadan: BOLUM_1 S0-S6 · BOLUM_2 S7-S13)
```

### 2b. 🌍 ORTAM SAYILARI — SPEC'e metre/birimle, prompta GÖVDE BOYUYLA

```
YERÇEKİMİ        0,95 g   → normal insan temposu, GERÇEK ZAMAN [D44]
                            1,00 m serbest düşüş ≈ 0,46 s (ölçülebilir kilit)
BASINÇ           0,90 atm · solunabilir bileşim (O₂ ~%19)
   ⛔ KASK YİNE DE 14/14 KAPALI — gerekçe hikâyenin kendisi:
     çift yönlü biyolojik karantina. Bu, D79'un yüz kilidini korur ve
     "kask çıkarma" politika sınıfını (PB ②, iki ölçülmüş red) hiç açmaz.
SICAKLIK         +14 °C  → görünür nefes buharı YOK; nefes kanalı GİYSİDEN
                            okunur (omuz ve göğüs kafesinin periyodik yükselişi)
RÜZGÂR           tek yönlü, sabit; ot dalgası 14/14 sahnede ekran SOLUNDAN SAĞINA
GÜNEŞ            tek kaynak, ekran SOLUNDA, alçak-orta yükseklik; gölgeler
                 ekran SAĞINA düşer ve 14 sahnede MONOTONİK uzar (ışık takvimi)
SES              normal yayılım: ot hışırtısı · rüzgâr · suit fanı · nefes
                 ⛔ "müziksiz" sahne SESSİZ sahne değildir [D83]
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM:  Bu ovada ezilen ot bir daha kalkmaz — ezilen sap soluk gümüze döner
        ve o gümüş hat, sürünün YEMEK YOLUDUR.
        (Rasyonel mekanizma — bilişsellik etkisi: sapın tek kullanımlık bir
         çökme katmanı vardır; çöken sap ışığa dönük yüzünü kaybeder, solar
         ve şeker salar. Dört ayaklılar bu yüzden hiç ezilmemiş ota basmaz;
         yalnız ezilmiş hatlarda yürür ve beslenir. Büyü yok, nedensellik var.)

NOVUM TAŞIYICISI:  <EZİK OT ÇİZGİSİ (gümüş hat)> × <bot basar ve kalkar> →
                   <hat kıpırdamaz: dalga üstünden geçer, hat dalgalanmaz>

① TEK KARE:  "Altın otun dalgası ovayı boydan boya süpürürken, kadrajın
   ortasındaki tek gümüş EZİK OT ÇİZGİSİ hiç kıpırdamıyor."          ✅
   (cümle taşıyıcı nesnenin ADINI içeriyor — D157)
② KİNETİK BAĞIMSIZLIK: kural replik, dış ses ve ekran metni OLMADAN kanıtlanır;
   üç sahnede ve iki ayrı nesnede: bot izi (S0-S1) · iniş aracı pabuç izi (S2)
   · hayvan hattı (S5). Üç sahne / iki nesne = kural kanıtı sağlanır.  ✅
③ BAŞLIK ŞEMASI: "THE BENT GRASS" — 3 kelime (≤5).                    ✅
⛔ Üçü de ✅ → KONSEPT KABUL. Sıralama yazılabilir.

MAYA EŞİĞİ [tek ihlal]: dünyanın TEK yeni kuralı budur. Başka hiçbir fizik
ihlali yok — yerçekimi, ışık, ses, rüzgâr Dünya benzeri ve tutarlı.
```

### 3b. ⛔ SAPMA KAYDI — TEK VARLIK kuralı ↔ sahibin "uzaylılar" çoğulu [D74]

```
KURAL:     UZAYLI_VARLIK_TASARIM_KILAVUZU §0① — kadrajda TEK VARLIK; ikinci
           varlık (ve ikinci TÜR) yasak. Gerekçe: model iki varlığı ayrı
           tutamıyor, biri ötekinin anatomisini yiyor.
TALEP:     "4 ayaklı uzaylılar" — çoğul.
SAPMA:     Çoğul KABUL EDİLDİ, ama TÜR ÇOĞULU DEĞİL BİREY ÇOĞULU olarak:
           tek tür · tek şablon · tek ihlal (ağız yok, temasla beslenir) ·
           uzuv sayısı sabit (tam dört eklemli bacak).
KISITLAR   (sapmanın bedelini ödeyen dört satır):
  ① SAYI KİLİDİ      yakın/orta bantta TAM ÜÇ birey; uzak bantta ufukta
                     TEK KESİNTİSİZ HAT (sayısız çoğul YASAK — "yüzlerce"
                     yazılmaz, model saymaz ve her karede farklı doldurur)
  ② MESAFE + DOF     ikiden fazla birey aynı karede yalnız UZAK bantta ve
                     sığ DOF ile; yakın bantta aynı anda EN ÇOK BİR birey
                     tam gövde [D2 morph panzehiri]
  ③ TAM GÖVDE BÜTÇESİ  tam gövde ≤2 çekim ve toplam ≤6 s; kalan her varlık
                     vuruşu PARÇA üzerinden (bacak · hat · gölge · ses)
                     [NOBODY WAS ALIVE · A2]
  ④ YÖRÜNGE YASAĞI   varlığın çevresinde tam tur yok; görüş yayı ≤90°
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — ZAMAN / geçicilik
▸ tanım cümlesi — "Geçicilik bir doğa yasası değil, bir ayrıcalıktır:
                   bu ovada hiçbir iz kaybolmaz."
                   (TANIM cümlesi — §3c takas kalıbı DEĞİL: "X için Y feda
                    edilir" biçiminden bilinçle kaçınıldı)
▸ depoda kaç kez kullanıldı — 4 (sayac.sh · TEMA DAĞILIMI; İLK-TEMAS 7 ile
  en çok kullanılan etikettir ve bu filmde varlık VAR olduğu hâlde tema
  olarak SEÇİLMEDİ: uzaylı bu filmin konusu değil, kuralın kanıtıdır)
▸ motif kanalları —
   NESNE   : ezik ot çizgisi (gümüş hat) · örnek kasası
   KİNESİK : basmadan önceki duraksama; ayağı geri çekme; hattın üstünden atlama
   KAMERA  : aynı kurulumun ikinci kez kullanımı (kafiye) — S0 ↔ S13
   IŞIK    : gölgelerin monotonik uzaması (ışık takvimi = geri alınamayan zaman)
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa malzeme AZALTILIR —
> prompt iyileştirmek bu deponun ölçtüğü kadarıyla işe yaramıyor.

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 SU / SIVI | ❌ | Filmde su, sıvı, yağmur, çamur 0 kare | malzeme baştan yok | — |
| 2 CANLI / HAYVAN | ✅ 🔴 | Dört ayaklı fauna — deponun en pahalı sınıfı (Tidal Hunt 2/10 · Mirror Fauna canlı kayması) | tam gövde ≤2 çekim/≤6 s · parça anlatımı · sayı kilidi · lokomosyon cümlesi · yörünge yasağı | 🔴 **KALIYOR** |
| 3 KASK / VİZÖR / EKİPMAN | ✅ 🟠 | Her uzay filminde var; iki suit | kask 14/14 kapalı, durum değişimi 0 kare · optik berrak vizör cümlesi · düz sırt pozitifi | 🟠 **KALIYOR** |
| 4 İKİNCİ FİGÜR | ✅ 🟠 | Talebin kendisi: iki astronot (HUMAN COUNT LOCK 2 × 14) | dizilim kilidi (A sol · B sağ) · dört kanallı ayrım · biniş/iniş 0 kare · kadrajda tam 2 gövde | 🟠 **KALIYOR** |
| 5 EKRAN / SAYAÇ / METİN | ✅ 🟠 | Filmin bir sayacı var (gümüş hattın uzaması) | sayaç METİNSİZ ve ÇEVRESEL; ekran/gösterge/rakam 0 kare; sayacın iki ucu aynı karede [D78] | 🟢 sıfırlandı |
| 6 PARÇACIK / TOZ / PATLAMA | ❌ | Tasarımla çıkarıldı: polen/tohum/toz olayı 0 sahne | **MALZEME AZALTMASI ①** | — |
| 6b KATMANLI / BÖLGELİ DÜNYA | ❌ | Tek biyom, tek ışık bölgesi, tek mekân | **MALZEME AZALTMASI ②** | — |
| 7 DİYALOG | ❌ | 0 replik | **MALZEME AZALTMASI ③** | — |
| 8 KAMERA | ✅ 🟢 | Her filmde: lockoff + açı yayı | 14/14 sabit lockoff · klip içi kamera hareketi 0 · açı/ölçek yayı `ACI_YAYI` bandında | 🟢 |
| 9 IŞIK MIKNATISI | ✅ 🔴 | Tek baskın ışık (güneş) + hedefe (iniş aracına) doğru hareket | hedefe yürüyüş sahnesinde **kamera HEDEFİN yanında** (nötr çekim, D104 kaçış basamağı); dört kanallı ışık-yön kilidi; sırtlar güneşe | 🟠 azaltıldı |
| 10 İNSANSIZ SAHNE + UZUN NEGATİF | ✅ 🟡 | Ayrılış kodası S12-S13 insansız | insansız sahnelerin NEGATIVE bloğu KISALTILIR (tek pozitif Style satırı); "Exactly 0 human" biçimi YAZILMAZ | 🟢 sıfırlandı |
| 11 DEĞİŞKEN SÜRE / SAHNE İÇİ KESME | ❌ | 14 × 10,0 s sabit ızgara; sahne içi kesme 0 | **MALZEME AZALTMASI ④** | — |
| 12 POLİTİKA YÜZEYİ | ✅ 🔴 | Yüzü kapatan ekipman (imza ⑥) + canlı sözlüğü + hayvan-insan yakınlığı | D79 yüz okunur · yaratık sözlüğü nötr hâlleriyle · kuvvet vektörü insana YÖNELMEZ · kırmızı ton yok | 🟠 azaltıldı |
| 13 YAPI ÖLÇEĞİ / TEKRAR EDEN BİRİM | ✅ 🟠 | İniş aracı kadrajda (3 sahne) | 1H = 1,90 m sözleşmesi · araç ölçüsü SPEC'te metre, promptta gövde boyu · ölçek şahidi zorunlu · araç yalnız 3 sahnede | 🟠 **KALIYOR** |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  KART 2 — dört ayaklı canlının ANATOMİSİ ve LOKOMOSYONU
                  (Mirror Fauna: 00:20 bacak yüzeyde kaydı · uzuv sayısı
                   4-6 arası oynadı · renk sarı↔cyan · Upward Fall: plan
                   "0 bacak" derken canlı iki sütun uzuvla zemine bastı)
POZİTİF BİÇİMİ:   "exactly four jointed legs, one body, one pair of dark
                  eyes low on the front wedge; each leg lifts clear of the
                  grass and sets down again, one at a time; the shoulder
                  rides just above the standing figure's helmet"
                  → SAYI taşıyor: 4 bacak · 1 gövde · 2 göz · omuz yüksekliği
                    kasklı gövdeye GÖRE (gövde boyu birimi, metre değil)
```

```
TETİKLENEN RİSK:  9 / 14        (2 · 3 · 4 · 5 · 8 · 9 · 10 · 12 · 13)
EŞİK:             5
⛔ EŞİĞİN ÜSTÜNDE → MALZEME AZALTILDI (dört kalem, yukarıdaki tabloda):
   ① parçacık/toz olayı 0 sahne   ② tek biyom + tek ışık bölgesi
   ③ 0 replik                      ④ sabit ızgara, sahne içi kesme 0
   + üç kart tasarımla SIFIRLANDI (5 · 10) ve ikisi AZALTILDI (9 · 12)
KALAN GERÇEK RİSK: 5 → CANLI(2) · KASK(3) · İKİNCİ FİGÜR(4) · IŞIK MIKNATISI(9)
                       · YAPI ÖLÇEĞİ(13)
KABUL GEREKÇESİ:  Beşinin dördü SAHİBİN TALEBİNİN KENDİSİDİR (iki astronot ·
   dört ayaklı canlı · basınç giysisi) ve kaldırılamaz. `01_DERS_ETKINLIK`
   §4'ün cümlesi burada geçerli: "talebi kaldırabildiğin kategori düzelir" —
   kaldıramadığımız iki kategori (CANLI · FİZİK) prompt metniyle değil
   SAHNE SEÇİMİYLE çözülür: canlı uzakta/parçalı, temas yok, tam gövde 6 s.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ

> Soru ④ "YAZILMASIN" cevaplandı; tablo yine de dolduruldu — sessizce
> atlanmadığının kaydı budur.

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✅ | İki astronot · 14/14 sahne |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✅ | Vizör geometrisi (D146'nın üç vakası) · uzaylının kafa/ön kama biçimi |
| T3 | oranı sözle yazılamayan nesne | ✅ | İniş aracı (S2 · S11 · S12) |
| T4 | insan dışı canlı | ✅ | Dört ayaklı fauna · 6 sahne |
| T5 | tekrar eden insan dışı olay | ✅ | Ot dalgası (14/14) · gümüş hattın oluşması |
| T6 | bir varlık tekrar tekrar dönüyor | ✅ | Uzaylı · iniş aracı · ova |

```
KARAR: YAZILMAZ — sahip kararı (soru ④). Altı tetikleyicinin ALTISI da doğru.
⛔ PLAN'a tek satır gerekçe yazılır [D74] — §0'daki cümle.
⭐ TELAFİ — paketin taşıyacağı üç kilidi METİN taşıyacak, ve üçü de
   14/14 promptta BİREBİR aynı cümleyle:
   ① ANATOMİ + BOY ORANI (dört eklemli bacak · omuz kasklı gövdenin üstünde)
   ② VİZÖR + SIRT (optik berrak, yansımasız · düz sırt tek dikişli)
   ③ ROL ŞERİDİ (renk + KOL/BACAK tarafı) — iki figürün ayrım kanalı
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S9 — dört ayaklı canlının bir astronota EN YAKIN olduğu kare
NÖTR TARİFİ:  "The animal stops one body-length short of the standing figure
   and lowers its front wedge to the flattened line between them; it does not
   touch the figure and does not close the distance. The figure stays still,
   arms at their sides, and does not reach out. Nothing is thrown, nothing is
   struck; the only movement in the frame is the animal's front leg setting
   down and the grass wave crossing behind them."
⛔ Yasak cümlesi YAZILMAZ ("no attack", "not aggressive" D123 tuzağıdır);
   yerine yukarıdaki POZİTİF kare tarifi kullanılır.
İKİNCİ RİSKLİ KARE:  S12-S13 (insansız koda) — yapısal red profili
   [KART 10]: insansız sahne + uzun NEGATIVE bloğu. Karşılığı: koda
   sahnelerinde negatif blok tek pozitif Style satırına iner.
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   Kalkış penceresi kapanmadan ovadan alınan BİYOKÜTLE ÖRNEKLERİNİ
         iniş aracına götürmek ve yüklemek.
         (Film başlamasa da var olan bir İŞ: örnek toplama görevi. "Anlamak /
          görmek / fark etmek" DEĞİL — taşınan bir kasa ve kapanan bir pencere.)
ENGEL:   Ova hiçbir izi silmez ve ezilen her hat sürünün yemek yoludur.
         Araca giden en kısa dönüş, sürüyü doğrudan kalkış pistine götüren
         bir hat yazar.
BEDEL:   ÖRNEK KASASI OVADA BIRAKILIR · **S10**
         (görevin ürünü; iki astronot araca BOŞ ELLE döner ve dönüş hattı
          kapalı bir halkaya çevrilerek pistten ayrılır)
MUHATAP: İKİNCİ İNSAN — B (mühendis).
         İkincil kanal: ovanın KALICI değişen parçası (gümüş hat).
AYRILIK: **S8** — B düz hattı seçip araca doğru bir adım atar; A onu izlemez,
         durur ve kavis çizmeye başlar. İki gövde bir süre iki ayrı yöne bakar;
         B önce araca, sonra A'nın yeni hattına bakar ve A'yı izler.
         (0 replik — ayrılık yalnız duruş, yön ve bekleme ile okunur)
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4].

### 7b. Ek omurga satırları — `06_HIKAYE_HATTI_TESHISI` · `UZAY_SENARYO` §9.1

```
ANTAGONİST KANALI:  ④ KARAKTERİN KENDİ SEÇİMİ (+ ② ortam: hiçbir şeyi
                    silmeyen ova). "Oksijen bitiyor" DEĞİL.
ETKİNLİK ÇAPALARI:
  ① TERCİH ÇAPASI  S8 (düz hat ↔ kavis) ve S10 (kasayı bırakmak)
  ② TEPKİ ÇAPASI   her olayın BEDENSEL karşılığı promptta yazılı
                   (hayvan yaklaşınca yarım adım geri · kasayı bırakırken
                    omuz düşmesi · hattın üstünden atlarken duraksama)
  ③ BAŞLANGIÇ AMACI  ilk 3 saniyede NEREYE gidildiği görünür: S0'da botun
                   önünde kasa, arkada ufukta iniş aracının tepesi
BAŞARISIZ DENEME [D158]: S9 — A hattı ELİYLE kaldırmayı dener (ezik sapları
                   doğrultmaya çalışır); saplar geri kalkmaz. Merkezî
                   seçimden ÖNCEKİ başarısız deneme budur.
MERKEZÎ SEÇİMDEN SONRAKİ SEÇİM: S11 — araca binmeden önce A son bir kez
                   geri döner ve halkanın son metresini kendi eliyle kapatır.
BİLGİ ASİMETRİSİ:  İzleyici sürünün hatları izlediğini S5'te öğrenir;
                   astronotlar S7'de fark eder → pencere S5-S7 arası AÇIK
                   (dramatik ironi; karakterler bu pencerede panik yapmaz)
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅   (TEK KARE · KİNETİK BAĞIMSIZLIK · BAŞLIK)
☑ risk sayımı yazıldı: 9/14 tetiklendi · eşik 5 → malzeme dört kalemde azaltıldı
  · iki kart sıfırlandı · kalan beş riskin dördü talebin kendisi (kabul edildi)
☑ B5 dörtlüsü tam · BEDEL sahne numarası taşıyor (S10) · AYRILIK yazıldı (S8)
→ üçü de ✅ → 03_SAHNE_SIRALAMASI.md yazılabilir
```
