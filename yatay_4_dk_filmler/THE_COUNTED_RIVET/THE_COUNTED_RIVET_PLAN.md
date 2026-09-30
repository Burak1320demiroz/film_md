# 🎬 THE_COUNTED_RIVET — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.

```
FORMAT:        yatay 4 dk — §2.3 kartı · 24 KLİP × 10,0 s · 2 bölüm dosyası
               (BOLUM_1 = K01-K12 / S1-S4 · BOLUM_2 = K13-K24 / S5-S7)
ORTAM:         §3.6 SÜREKLİ BULUT / NÖTR YÜZERLİK — 55 km bandı · 0,904 g ·
               yarım Dünya atmosferi yoğun CO₂ · ufuk YOK · zemin YOK ·
               güneş diski YOK · gölge YOK (her yönden dolgu) · toz YOK
TÜR:           bilimkurgu   (tek açık dal — §4.1) · dal: ölçüm işi / sert gerilim
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124] — plan 10,0 s ızgarasıyla yazıldı:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
               ⛔ Ölçüm üretim defterinin motor satırına yazılır; tercih DEĞİLDİR.
SAHNE SAYISI:  7 sahne · 24 klip      RUNTIME: 240,0 s = 24 × 10,0 s
LOGLINE:       Bulut platformunu bağlayan teknisyen, mandalın ölçüsüne
               güvenmeyip platformun örtüsünden bir çelik şerit çıkarır;
               şerit bağlandığı yüzeyin hiç kavis yapmadığını gösterir.
REFERANS PAK.: ⬜ YAZILMADI — sahip kararı (25.09.2026) [D74 kalıbı]. Altı
               tetikleyiciden BEŞİ doğru (T1 · T2 · T3 · T5 · T6); biçim kilidi
               24 klip boyunca yalnız metinle tutulacak ve risk
               `00_ANALIZ/04_UYARI_NOTLARI.md` ⛔5 satırında AÇIK duruyor.
```

---

## 🎭 TEMA

```
TEMA: İNSAN-MAKİNE
      — Makine yalnız kataloğunda adı olan büyüklükleri görebilir; insan
        kataloğu olmayan bir büyüklüğü ölçmeyi seçer ve bedelini öder.

MOTİF SAHNELERİ: S3 · S5 · S6 · S7
      S3 — makinenin ölçüsü (mandal çenesi) ile insanın gözü aynı karede;
           otomasyon mandalı yeniden gerer, ölçü değişmez
      S5 — makinenin ölçüsü ile insanın ölçüsü (çelik şerit) aynı karede;
           insan kendi cetvelini alır ve bedeli öder
      S6 — makine hiçbir şey öğrenmemiştir: çeneyi aynı periyotta gerer,
           kadrajın kenarında örtünün açık kenarı durur
      S7 — insan makinenin kaydına karşı çalışır; platform yükselirken
           kehribar lamba AYNI periyotta atmaya devam eder (tema-final)
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM:               Bağlandığı yüzey bir gövde değil, gövdenin bir DETAYIDIR —
                     ve bunu ancak düz bir kenarın altından ışık sızıp
                     sızmadığı söyler.
NOVUM TİPİ:          ÖLÇEK   (kılavuzun ikinci tercihi)
NOVUM TAŞIYICISI:    çelik şerit (kol boyu · düz kenarlı) × şeridi yüzeye
                     yatırma jesti → şeridin altından hiçbir yerde ışık
                     sızmıyor
İKİNCİ TAŞIYICI:     perçin başı × eldivenin yanına konması → baş omuzdan geniş
İHLAL SAYISI:        1 — perçin ve sürüklenme aynı ihlalin 2. ve 3. KANITI
TEK KARE (§4①):      Eldiven, omuzdan geniş bir PERÇİN BAŞININ yanında,
                     plakaya yatırılmış düz bir ÇELİK ŞERİDİ tutuyor; şeridin
                     altından hiçbir yerde ışık sızmıyor.
                     → cümle iki taşıyıcı nesnenin de ADINI taşıyor [D157]
KİNETİK BAĞIMSIZLIK: ✅ kural replik, dış ses ve ekran metni olmadan
                     kanıtlanıyor — ölçüm bir IŞIK BOŞLUĞUDUR, bir okuma değil
BAŞLIK ŞEMASI:       ✅ THE COUNTED RIVET (3 kelime) — izleyiciye nereye
                     bakacağını söylüyor: perçine
```

### 📐 ÖLÇÜMÜN ARİTMETİĞİ — filmin tek iddiası ve neden ekranda okunur

```
sagitta    s ≈ c² / 8R          kadraj    W = 2·d·tan(FOV/2) · H = W·9/16
piksel     px = boy / H · 2160  FOV       2·arctan(18 / f)

kenar 0,30 m (mandal çenesi · B kurulumu · H 0,486 m)
   2 m çaplı bir direkte sapma 11,3 mm →  50 px  · okunur ama TARTIŞILIR
kenar 0,60 m (çelik şerit · H kurulumu · H 0,304 m)
   2 m çaplı bir direkte sapma 45,0 mm → 267 px  · TARTIŞILMAZ
kenar 0,60 m, GERÇEK yüzey (R ≈ 15 km)
   sapma 0,003 mm →                        0 px  · hiçbir yerde ışık yok
KABUL EŞİĞİ: boşluk hiçbir yerde eldiven kalınlığından (2 cm = 142 px)
             geniş değil
⭐ Dramanın fizik gerekçesi: mandalın çenesi KISA olduğu için ölçüsü
   belirsizdir. Daha uzun bir düz kenara ihtiyaç duymak inat değil,
   zorunluluktur — ve o kenarı almanın bedeli filmin bedelidir.
⭐ Kanıt YALNIZ bu ortamda mümkün: ışık her yönden gelir, gölge yoktur.
   Tek yönlü bir güneş olsaydı şeridin altı gölgede kalır, boşluk okunmazdı.
```

## 🧭 B5 — HİKÂYE OMURGASI (her formatta · `03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Platformu asit cephesi gelmeden sabit bir kütleye bağlamak.
              Film başlamasa da var olan bir İŞ — bağlama teknisyeni bunu
              her vardiyada yapar. ⛔ "anlamak / görmek / fark etmek" değil.
   □ ENGEL:   Bağlandığı şey bir kütle değil, bir kütlenin DETAYI; ölçüyü
              söyleyen otomasyonun kataloğunda bu kadar büyük bir kategori
              yok. (engel tipi: ORTAM)
   □ BEDEL:   Platformun asit örtüsünün kenar bağı — bir daha geçirilemez,
              asit zarfı yemeye başlar, kaldırma azalır · **S5**
              İkinci bedel: kendi çaktığı dokuz bağlama noktası · **S7**
   □ MUHATAP: ORTAMIN KALICI DEĞİŞEN PARÇASI — açılan örtü kenarı ve üstünde
              yayılan mat kabarma; film boyunca geri dönmez, her klipte aynı
              cümleyle görünür. İkinci yankı: bağlama otomasyonu (sabit
              periyotlu kehribar lamba + her seferinde aynı sürede kapanan
              mandal) insanın kararından sonra da aynı ritimde devam eder.
B5b □ AYRILIK: — (tek insanlı film)

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  K14 (politika kapısı) → K15 (novum · İPTAL KAPISI) → K21 (doruk) →
  K24 (kapanış imajı) → K01 (hook) → kalanı
  ⛔ K15 üç denemede okunmazsa taşıyıcı değişir; Plan B = perçin sayımı
     birincil kanıt olur ve şerit ikinci kanıta düşer.
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR (KILAVUZ_REHBERI §2.1)

```
— UYGULANMAZ: bu film YATAY 16:9'dur (§2.3). Üç satır dikey hattın kapısıdır.
  B5 omurgası (yukarıda) her formatta zorunludur ve yazılıdır.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | klip · saniye | boşsa gerekçe |
|---|---|---|---|---|
| 1 | açılış imajı / soru | %0-4 | K01 · 0:00-0:10 | — |
| 2 | katalizör | %12,5 | K03 · 0:20-0:30 | bant 24-36 s'nin içinde |
| 3 | ilk ölçüm krizi | %25 | K06 · 0:50-1:00 | — |
| 4 | orta nokta — sürükletme kararı | %50 | K12 · 1:50-2:00 | — |
| 5 | MERKEZÎ SEÇİM + BEDEL | %54-58 | K14 · 2:10-2:20 | bedel aynı karede |
| 6 | NOVUM KANITI | %58-62 | K15 · 2:20-2:30 | filmin tek ölçümü |
| 7 | her şeyin kaybı | %75-79 | K19 · 3:00-3:10 | sayı bulundu, karar verildi |
| 8 | DORUK | %83-87 | K21 · 3:20-3:30 | — |
| 9 | FİNAL VURUŞ | %91-95 | K23 · 3:40-3:50 | dokuz kesik uç sayılabilir |
| 10 | kapanış imajı | %95-100 | K24 · 3:50-4:00 | K01'in kamera cümlesi birebir |

```
⛔ ARDIŞIK AYNI VURUŞ: 0 [D212]
⭐VİRAL KLİP: 0 — kartın dört adedinden SAPMA [D74]. Kapı İKİ kanalı birden
   istiyor (okunan yüz + hızlanan hacim); bu estetikte (kilitli kamera ·
   sakin yüz · iş kadrajı) ikisi tek klipte birleşmiyor. Üç aday ölçüldü:
   K14 hareket ✅ / yüz ⛔ (F kurulumu h 0,90 m — baş kadraj dışı) ·
   K16 hareket ✅ / yüz ⛔ (128 px) · K19 yüz ✅ / hareket ⛔ (hızlanan
   hacim yok). Gerekçesi `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §2.4'te.
```

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU — kadrajda tek bir şey yanlıştır ve
                 izleyici onu adlandırmadan görür
K01 SORUSU:      Mandalın çenesi kapanıyor; içine aldığı yüzey hiçbir yerde
                 kavis yapmıyor. Çene bir DİREĞİ kavramak için yapılmış;
                 kavradığı şey düz. → "Bu ne kadar büyük?"
K02 İKİNCİ BİLGİ: İş sıradan ve süreli — kehribar lamba ikinci kez atıyor,
                 eldivenler bağlama kolunu açıyor. Soru büyür, cevap gelmez.
İLK 2 SN SESİ:   yoğun havanın alçak uğultusu + çenenin metal üzerinde
                 kapanan tek tok sesi; kaskın içinde nefes
İLK 30 SANİYE:   kurulum klibi EN ÇOK İKİ (K01 B · K02 F · K03 A) [D211]
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı ·
> el · yürüyüş) ve `KURGU_RITMI §2` örüntü kırıcı — **ardışık iki sahne aynı
> ölçek + palet + ses dokusunda olamaz.**
> Kamera sütunu üç kılavuzdan gelir: vuruş→açı `KAMERA_ACISI` · diziliş bandı
> `ACI_YAYI` §3 (ardışık çift ≥1 ölçek kademesi VE ≥45°) · kalıp `MESHUR_SAHNE`.

| S | klip | başlık | olay | kurulum (lens · ölçek · açı tipi) | ses | bütçe |
|---|---|---|---|---|---|---|
| S1 | K01 | KAPANAN ÇENE | Mandal çenesi kapanıyor; içindeki yüzey hiç kavis yapmıyor | B 50mm · CU · göz hizası | uğultu + tek tok kapanma | el: iki eldiven çenede · göz: çene boşluğunda |
| S2 | K02-K04 | İKİNCİ NOKTA | Asit cephesi kırk dakika uzakta; ikinci kazığı çakıyor ve çene ölçüsü tutmuyor | F 35mm · MS · bel yüksekliği → A 24mm · WS · göz hizası → F | uğultu + çekiç + lamba | tepki planı K04 · yürüyüş K03 · ALIŞKANLIK (çeneyi iki parmakla iki kez yoklar) |
| S3 | K05-K08 | SIFIR KAVİS | Tekrar ölçüyor, ölçü değişmiyor; otomasyon mandalı yeniden geriyor | E 24mm · WS · alt açı → F → A → G 35mm · MS · OTS | uğultu + germe + lamba | göz: yukarı · el: sol eldiven makara kulpunda (TEL) · sırt K08 |
| S4 | K09-K12 | KIRK SANİYE | Platformu yüzey boyunca sürükletiyor; yüzey bitmiyor | E → F → E → G | uğultu + kayma + perçin geçişi | el: başparmak her sıra geçişinde bir kez basıp bırakıyor (sayaç) |
| S5 | K13-K15 | KENDİ CETVELİ | Örtünün bağını çekip çelik şeridi yüzeye yatırıyor | H 50mm · CU · profil → F → H | uğultu + halat sürtünmesi + tok yatma | **BEDEL** · ALIŞKANLIK KIRILIR · omuzlar iner ve kalkmaz |
| S6 | K16-K19 | SAAT | Perçin aralığını ölçüyor; çıkan sayı ineceği saati veriyor | E → F → B → D 85mm · ECU · göz hizası | uğultu bir kademe kalın | tepki planı K19 (tek yüz klibi) · göz: perçin sıralarında |
| S7 | K20-K24 | DOKUZ | Dokuz noktayı kesiyor; platform yükseliyor, yüzeyin sınırı görünmüyor | B → C 35mm · MS · üst açı 15° → B → C → B | uğultu iki kademe kalın | el: makas · İLK↔SON tersinmesi · final vuruş K23 |

```
AÇI TİPİ SAYISI: 5  ≥3 ✅   (göz hizası · alt açı · üst açı · OTS · profil)
KURULUM SAYISI:  8         (tavan 12 = 24 klibin yarısı) ✅
KURULUM İSKELETİ: B F A F  E F A G  E F E G  H F H  E F B D  B C B C B
                 ⭐ BU SATIR KAPIYI AÇAR — prompt_kontrol ⑩④. Bu rejimde
                   KÜME ARANMAZ (son kare zinciri kaldırıldı); ardışık aynı
                   kurulum ⑩① ile BLOCK'tur ve iskelette 0 kez var.
                 DÖNÜŞ 14/24 = %58,3 (hedef ≥%40) ✅
                 ⛔ Aynı harf AYNI kurulumdur ve kamera metni BİREBİR
                   kopyalanır + işaret satırını taşır (ACI_YAYI §7 ⑥):
                     dönüş → "— the same position, height and lens as Clip N."
                 ⛔ Zincir dili YAZILMAZ (㉜⑤); sahne içi süreklilik
                   `CONTINUOUS ACTION:` satırıyla taşınır.
SAHNE PLANI: 1 3 4 4 3 4 5
                 ⭐ ÇOK KLİPLİ SAHNE (22.09.2026) — sahne başına klip sayısı;
                   toplam = CLIP COUNT (24). BU SATIR ㉜ KAPISINI AÇAR ve
                   ⑩④ KÜME hedefini kapatır. Kılavuz: COK_KLIPLI_SAHNE_KILAVUZU.md
                 TEK KLİP GEREKÇESİ (S1): HOOK — soru tek kadrajda sorulur ve
                   cevap verilmeden kesilir; ikinci bir klip soruyu yumuşatır.
BÖLÜM KESİĞİ:    S4 (K12 · G · MS · OTS) ile S5 (K13 · H · CU · profil) arasında
                 → 1 ölçek kademesi (MS→CU) + 90° azimut ✅
                 ⛔ Sahneler bölüm sınırını AŞMAZ: 4+4+3+1=12 / 3+4+5=12
```

### 📐 ARDIŞIK ÇİFT — bant özeti (tam tablo `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §3)

```
bant içi 23/23 · bant dışı 0 · bilinçli ŞOK 1 (K15→K16 · H→E · 2 kademe · 160°)
ŞOK GEREKÇESİ: ölçüm bitti, dünya geri geliyor — kanıttan sonraki ilk kare
               izleyiciyi ölçünün İÇİNDEN çekip platformun tamamına atar.
```

### 🔁 SAHNE KİLİTLERİ — sahne içinde BİREBİR kopyalanacak üç satır (㉜⑥)

| sahne | IMAGE `LIGHT:` | VIDEO `PHYSICS:` | VIDEO `AUDIO:` ilk cümlesi |
|:--:|---|---|---|
| S1-S5 | kubbe okra kademe **0** | 0,904 g · nötr yüzerlik · sabit oranda iniş | yoğun havanın alçak uğultusu |
| S6 | kubbe okra kademe **1** | aynı + iniş oranı iki kat | uğultu bir kademe kalın |
| S7 | kubbe okra kademe **2** | aynı | uğultu iki kademe kalın |

⚠️ Işık kademesi bir **DURUM DEĞİŞİMİ**dir ve klip içinde olmaz: değişim sahne
SINIRINA konur (S5→S6 ve S6→S7). Dizi MONOTONİK, geri açılmaz [D193 uyarlaması —
yön ve Kelvin yok, çünkü güneş diski ve gölge yok; tek parlaklık dizisi].

### 🔢 METİNSİZ SAYAÇLAR — üçü de rakamsız, üçü de aynı kanalda ilerler

```
① KANIT MERDİVENİ   K01 çene boşluğu YOK (belirsiz) → K06 aynı çene, aynı
                    sonuç (ikinci kez) → K15 şeridin altında boşluk YOK
                    (tartışmasız). Aynı jest, uzayan kenar.
② İNİŞ HIZI         perçin sırasının güverte kenarından geçme süresi:
                    K09 ~40 s → K11 ~25 s → K16 ~18 s. Monotonik.
③ IŞIK TAKVİMİ      kubbenin okra kademesi 0 → 1 → 2; yalnız sahne
                    sınırlarında değişir, geri açılmaz.
⛔ Üçünde de RAKAM YOK, ekran yok, sayaç yok. Ölçü gövde-görelidir.
```

---

## 🎙️ REPLİK TABLOSU (yalnız replikli filmde · `SES_VE_DIYALOG_URETIM` §1-§2a)

```
⛔ BU BÖLÜM BOŞ — film bilinçli SESSİZ.
   SPEC `DIALOGUE LINES: 0` · promptlarda tırnak 0 karakter ·
   `No dialogue. No music.` her video promptunun AUDIO satırında.
   Muhatap KONUŞMAZ: bağlama otomasyonu sabit periyotlu kehribar lamba ve
   mandalı yeniden germe ile cevap verir — bu bir SES değil, bir OLAYDIR.
   Kapı ㉓ SPEC ilanıyla gövdeyi karşılaştırır; ikisi de 0 der [D203 · D217].
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna
> yalnız o karenin `IN FRAME:` satırındaki kısmı gider — hands ise eldiven/bilek/
> kol, face ise yüz + kask, full body ise silüet + renk bandı (14.09.2026 · D214 ·
> `prompt_kontrol.py` ㉖). "BIBLE'a bak" atfı YASAK (kural ③), ama self-contained
> ≠ Bible'ın tamamı: kadrajda olmayan YAZILMAZ. Videoya Bible girmez — `START FRAME:`
> tek satır. Bu blok promptların kaynağıdır, kopyası değil.

### 👤 Character Bible

> kimlik: `ASTRONOT_DONANIM` §9 · görünüş: `UZAY_GIYSISI_SINEMATIK_TASARIM` §11
> arketip **T (teknisyen)** · kask + görünür kalın çerçeve · sırt heykelsi pozitif ·
> kir global · "glow / seamless / no …" yok
> ⛔ KİMLİK YIĞINI ≤3 [D167 · ⑲]: yazılan üç öznitelik **cinsiyet · göreli boy ·
> yapı**. Ten rengi, yaş, saç biçimi, yüz hattı 24/24 promptta 0 kez.

```
One suited human figure, female, her standing height a little under four
rivet-head widths, narrow through the shoulders. Muted slate-grey quilted
pressure suit, matte, with a single ochre band wrapped right around the LEFT
upper arm and another right around the LEFT thigh. Rounded hard-shell helmet
seated in a wide dark collar ring; the visor is a single flat pane of
optically clear glass in a thick dark frame, closed and sealed. Dark grey
ribbed gloves with segmented knuckles and a raised cuff ring at each wrist.
Matte grey boots with a raised sole edge. No patches, no emblems, no numbers,
no insignia anywhere on the suit.
```

```
KADRAJA GÖRE HANGİ PARÇA YAZILIR [㉖]:
  hands       → eldiven (kaburgalı bölmeler · manşet halkası) + bilek + kol;
                yüz ve kask YAZILMAZ
  hands·torso → yukarıdakiler + gövde ön yüzü + SOL pazu okra bandı
  back        → sırt yüzeyi POZİTİF cümlesiyle (aşağıda) + SOL uyluk bandı
  full body   → silüet + iki okra bant + kask kubbesi; YÜZ AYRINTISI YOK
  face        → YALNIZ K19: yüz + kask + vizör cümlesi (§5.2 D79)
SIRT POZİTİF [D139 · ⑮] — kamera arkada/OTS olan her klipte birebir:
  "The back of the suit is one continuous sculpted surface from collar to hip,
   low-profile, with two shallow recessed panels, closed and smooth."
VİZÖR [§5.2 D79] — yalnız K19:
  "The visor is a single flat pane of optically clear glass with zero tint,
   her face fully readable through it."
KİR MERDİVENİ [D147 · D42] — GLOBAL bitiş, konumlu leke değil:
  S1-S4  fabrika matı, eklemlerde ince okra tozu
  S5+    ek olarak: sağ eldivenin manşet halkasında bağ çekmekten kalan mat
         bir aşınma — konumu ve boyu üç sahnede BİREBİR aynı cümleyle
  S6-S7  aynı, hiçbir şey temizlenmez ve hiçbir şey eklenmez
```

### 🌍 World Bible

```
A drifting work platform in a continuous cloud layer, about half an Earth
atmosphere of dense carbon dioxide. Overhead a sourceless bright ochre dome
with no sun disc and no beam anywhere in it; below and all around, ochre depth
that fades without a horizon line and without any ground. Filling the upper
part of the frame, a riveted expanse of dark grey-green metal — the plate —
its rivet heads each as wide as her shoulders, standing in rows a stride
apart, running out of frame on every side. The platform deck is ribbed dark
grey steel with a low rail along one edge; along the near edge a heavy grey
fabric cover lies over the envelope trunking, its hem closed with a thick
laced cord. Nine clamp seats stand in a line along the deck edge, each a
two-jawed steel clamp on a short neck.
```

```
ÜÇ DÜNYA ÇAPASI — 24/24 promptta BİREBİR [D209 · ⚠️ UYARLANDI]:
  ① üstte kaynaksız parlak okra kubbe · güneş diski 0 kare
  ② aşağıda okra derinlik · ufuk ÇİZGİSİ yok · zemin yok
  ③ yer imi PLAKANIN KENDİSİ ve bir perçin başı
⛔ Kartın ufku ve zemini YOK; D209'un "gök/ufuk/yer imi" üçlüsü bu yüzden
   uyarlandı. Gerekçe `00_ANALIZ/02_KONSEPT_VE_RISK.md` §2'de.
ANATOMİ KARTI — film boyu SABİT [risk kartı 13]:
  perçin başı Ø 0,50 m · perçin aralığı 1,00 m · sıra aralığı 1,00 m ·
  mandal çenesi 0,30 m · çelik şerit 0,60 m · eldiven kalınlığı 2 cm
  ⛔ Metreler SPEC'te durur; PROMPTTA ölçü gövde-görelidir [D138]:
     "as wide as her shoulders" · "a stride apart" · "the length of her forearm"
ASİT CEPHESİ — POZİTİF ve SAYILI [risk kartı 6]:
  kubbenin okra tonunun BİR KADEME koyulaşması. ⛔ perde · duvar · şelale ·
  kıvrılma · duman · sis kelimeleri 0 kez.
```

### 🎥 Camera Bible

> Sekiz kurulum. Aynı harf = aynı cümle, BİREBİR kopyalanır ve dönüş klibinde
> işaret satırını taşır. Klip içi hareket SIFIR (risk kartı 8).

| harf | lens | mesafe | yükseklik | ölçek · açı tipi | azimut | W × H (m) |
|:--:|---|---|---|---|:--:|---|
| A | 24mm | 4,0 m | 1,50 m | WS · eye level | 0° | 6,00 × 3,375 |
| B | 50mm | 1,2 m | 1,15 m | CU · eye level | 60° | 0,864 × 0,486 |
| C | 35mm | 2,0 m | 1,60 m | MS · high angle 15° | 135° | 2,06 × 1,157 |
| D | 85mm | 1,0 m | 1,45 m | ECU · eye level, frontal | 340° | 0,424 × 0,238 |
| E | 24mm | 5,0 m | 0,50 m | WS · low angle | 250° | 7,50 × 4,219 |
| F | 35mm | 1,4 m | 0,90 m | MS · waist-height | 300° | 1,44 × 0,810 |
| G | 35mm | 2,4 m | 1,70 m | MS · over-the-shoulder | 180° | 2,47 × 1,389 |
| H | 50mm | 0,75 m | 1,10 m | CU · profile insert | 90° | 0,540 × 0,304 |

```
HER KLİPTE: "fixed lockoff — absolutely zero camera movement" ·
            TIMELINE'ın son satırı "hold — the frame does not move" [D210]
⛔ ABARTI BANDI [⑫]: üst açı 15° (bant 15-30°) · alt açı YÜKSEKLİKLE
   (0,50 m), tilt derecesi yazılmaz · dutch 0° · tepe çekim 0
K01 ↔ K24 KAFİYESİ: aynı harf (B) ve BİREBİR aynı kamera cümlesi [D210]
```

### 💡 Lighting Bible

```
Shadowless fill from every direction inside the cloud layer — the whole ochre
dome is the source, so nothing in frame throws a directional shadow and no
surface has a hot edge. Light stays even across the plate, the deck and the
suit; contact shadows under a hand or a batten are the only dark the frame
carries, and they are narrow and soft.
```

```
ÜÇ KADEME — yalnız sahne sınırında değişir, MONOTONİK [D193 uyarlaması]:
  kademe 0 (S1-S5) : bright ochre dome
  kademe 1 (S6)    : one step deeper ochre, the same even fill
  kademe 2 (S7)    : two steps deeper ochre, the same even fill
⛔ Güneş diski 0 · ışın demeti 0 · lens parlaması 0 · bloom %0 ·
   titrek ışık 0 (ortamda parazit yok — makine ritmi SABİT PERİYOTLU
   kehribar lambadır, bir titreme değil)
⛔ IŞIK bloğu düzleme RENK ATAMAZ [D176 · ㉒] — plakanın, güvertenin ve
   örtünün rengi WORLD bloğunun işidir ve orada bir kez yazılır.
```

### ⚙️ Physics Bible

> ⚠️ Bu iki satırın §3.6 ortam kartı için hazır İngilizce karşılığı depoda
> YOKTU (`PROMPT_HATA_ONLEME_KILAVUZU.md` §2 beş kartı veriyor, §3.6 listede
> değil). Bu filmde yazıldı; kılavuza eklenmesi adım 11'de önerilecek.

```
PHYSICS: Gravity is 0.904 g inside a dense carbon-dioxide cloud layer at about
half an Earth atmosphere; the platform floats in neutral buoyancy and is
settling at a constant rate — it never hovers, never hangs motionless, never
rises. There is no ground and no horizon; relative wind is nil, so no fabric
lifts and nothing is blown about, and anything let go falls the height of a
glove in about a third of a second.
AUDIO:   The dense air carries sound well and takes the high frequencies out of
it — everything is low, close and slightly dulled; her breathing inside the
helmet sits under it all. No dialogue. No music.
```

```
⛔ TEK YERÇEKİMİ DEĞERİ: 0,904 g — 24/24 promptta AYNI sayı [D200 · ⑥]
⛔ Nötr yüzerlik POZİTİF kuralla yazılır; negatif çekirdeğin
   "never hovering" yasağıyla çakışmaz çünkü çakışan şey PARÇACIKLARDIR ve
   kadrajda serbest parçacık yoktur.
⭐ 0,904 g Dünya gibidir → "normal human pace, real time"; süzülme,
   ağır çekim, yavaş iniş YOK [D44 · D169]
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin ortam/tür/risk yasakları

> Havuz burada durur, prompta girmez: prompt §5.1 çekirdek (image 7 / video 8
> cümle) + bu listeden sahne başına **≤3** cümle taşır (㉗ · 14.09.2026).

```
§5.1 ÇEKİRDEK — BİREBİR, kısaltılmadan (video 8 · image 7: ① düşer):
① Single unbroken take, no cuts, no dissolves, no camera resets, no angle change.
② Exactly one human character, no duplicates, no second person.
③ 0% bloom, no glow, no soft focus, every surface keeps visible texture.
④ No readable text, letters, digits or symbols on any display, surface, patch
  or sign — none on the suit, the equipment, the ground or any natural surface
  in the frame — no subtitles, no captions, no watermark.
⑤ Photorealistic with 35mm film grain, no CGI or video-game look, real skin
  pores and sweat, no airbrushing, no waxy texture, no face morphing.
⑥ Equipment and clothing identical throughout, no drift, no gear appearing or
  disappearing.
⑦ Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no
  extra fingers.
⑧ Particles obey the stated gravity with continuous momentum, never hovering,
  never swirling like liquid, terrain static, no melting or warping.
```

```
SAHNEYE ÖZEL HAVUZ — ≤3 cümle seçilir (§5.2):
M1 mühür [D175 · ㉑ · 24/24 klipte ZORUNLU, üç sınır birden]:
   "No bare skin anywhere in frame — none above the collar, none at the wrist,
    none at the ankle."
M2 dünya [D209 · 24/24 klipte ZORUNLU]:
   "No sun disc, no beam of light, no horizon line and no ground anywhere in
    the frame."
M3 ölçü yüzeyi [D138 · ölçü aletinin geçtiği klipler]:
   "No notches, no graduations, no scale marks and no tick lines on the batten,
    the clamp or the plate."
M4 kubbe vizör [D146 · kask kadrajdaysa]:
   "No seamless visor, no bubble helmet, no dome faceplate, no spherical glass."
M5 asit [risk kartı 6 · S5-S7]:
   "No curtain, no wall, no waterfall, no smoke and no mist in the cloud."
M6 sürüklenme [risk kartı 6b · S4]:
   "No dust, no grit and no debris in the air; nothing is blown about."
M7 sıvı [risk kartı 1 · S5-S7]:
   "No droplets, no running liquid, no spray and no foam anywhere."
M8 politika [risk kartı 12 · S5 · S7]:
   "No blade, no cutting tool and no torn fabric in the frame; the suit is
    closed and intact."   ← S5'te; S7'de makas VARDIR, bu cümle S7'ye GİRMEZ
M9 ikinci figür [risk kartı 4 · reflektif yüzey klipleri]:
   "No reflection of a person in the visor, the plate or the steel."
⛔ M1 ve M2 her klipte; kalanı klibin malzemesine göre. TAVAN 11 cümle (㉗):
   video 8 çekirdek + 3 · image 7 çekirdek + 3.
⛔ ŞİDDET/TEHLİKE SÖZLÜĞÜ 0 KEZ [D123]: wound · danger · panic · trapped ·
   explosion · smoke · body · dead · injure · kill. Malzeme TARİF edilir:
   bağ ÇEKİLİR (kesilmez), asit "an even matte bloom spreading along the
   opened hem" olur.
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. `02_RISK_KARTLARI.md`'nin bu filmde tetiklenen her kartı
> buraya bir SAYI bırakır. 5+ risk çıkıyorsa kilit tavanı (aşağıda), malzeme değil.

| kilit | sayı | hangi risk kartı | hangi klip |
|---|---|---|---|
| insan sayısı | 1 — her promptta rakamla | 4 İKİNCİ FİGÜR | 24/24 |
| insansız klip | 0 — 24/24 klipte en az eldivenler kadrajda | 10 İNSANSIZ SAHNE | 24/24 |
| vizör kapalı | 24/24 klip · ara durum 0 | 3 KASK / VİZÖR | 24/24 |
| vizör pane sayısı | 1 düz pane + 1 kalın çerçeve | 3 KASK / VİZÖR | 24/24 |
| amblem · yama · rakam | 0 | 3 · 5 EKRAN | 24/24 |
| yansıyan insan | 0 kare | 4 İKİNCİ FİGÜR | 24/24 |
| ekran · rakam · sayaç | 0 — otomasyon 1 kehribar lamba + fiziksel germe | 5 EKRAN / SAYAÇ | 24/24 |
| lamba periyodu | 4,0 s · film boyu DEĞİŞMEZ | 5 EKRAN / SAYAÇ | K02 K07 K12 K18 K24 |
| yerçekimi | 0,904 g — tek değer | — (D200) | 24/24 |
| bırakılan nesnenin düşüşü | eldiven boyu ≈ 0,33 s | 6b KATMANLI DÜNYA | K04 K14 |
| perçin başı | Ø 0,50 m · aralık 1,00 m · sıra 1,00 m | 13 YAPI ÖLÇEĞİ | plaka geçen 8 klip |
| ölçek şahidi | her plaka klibinde 1 (eldiven ya da mandal) | 13 YAPI ÖLÇEĞİ | plaka geçen 8 klip |
| boşluk kabul eşiği | ≤ 2 cm = 142 px (H kurulumu) | 13 · A5 | K15 |
| çene boşluğu (karşıt kare) | 11 mm = 50 px (B kurulumu) | 13 · A5 | K01 K06 |
| ışık kademesi | 0 → 1 → 2 · monotonik · 3 değer | 6b KATMANLI DÜNYA | S1-S5 / S6 / S7 |
| iniş hızı (sıra geçişi) | 40 s → 25 s → 18 s | 6b KATMANLI DÜNYA | K09 K11 K16 |
| kesilen mandal | 9 adet · sayılabilir | — (D141) | K20-K24 |
| replik | 0 · tırnak 0 karakter | 7 DİYALOG | 24/24 |
| kamera hareketi | 0 — 24/24 fixed lockoff | 8 KAMERA | 24/24 |
| klip süresi | 24 × 10,0 s · kırpma bütçesi 0 | 11 DEĞİŞKEN SÜRE | 24/24 |
| kesici alet (S5) | 0 | 12 POLİTİKA | K13-K15 |
| ⭐VİRAL klip | 0 — iki kanal tek klipte birleşmiyor [D74] | — | — |

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕ KİLİT TAVANI)

> 14.09.2026: yaşayan listeden (`00_YASAYAN_DERSLER.md`) bu filme düşenler. Tavan 20;
> aşan kilit aşağıdaki bloğa iner. Sayı elle değişmez (sabit betikte).
> Risk sayımı 7/14 (eşik 5) → tavan devrede. **Malzeme azaltılmadı.**

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| D157 | Taşıyıcı ÇELİK ŞERİTTİR ve kadrajın en az onda birini kaplar; kanıtlandığı klipte kadrajda başka hiçbir şey hareket etmez. TEK KARE cümlesi şeridin ve perçin başının ADINI taşır | K15 (kanıt) · K13 · K18 · TEK KARE satırı |
| D179 | Her IMAGE promptu 0,0 saniyeyi yazar; K14'ün imajı bağ HENÜZ YERİNDE hâlini taşır, video 2,0 s'de çeker. Bedeli taşıyan değişim kadrajın kısa kenarının en az 1/8'ini kaplar | K14 · K15 · K20 · her sahnenin 1. klibi |
| D202 | ÇAPA ÜÇLÜSÜ: iki eldiven kanalı üçünde de aynı. ÖNCE mandal kolunda ↔ SONRA şeritte · ÖNCE dokuz mandalda ↔ SONRA boşta. Dolgu jesti yazılmaz | K01 ↔ K15 ↔ K24 |
| D206 | Her efor klibinde en az bir SANİYELİ ödeme satırı (`4.0s — each grip locks and the lacing stops for half a second`). Ödeme sonraki klibin durum satırına taşınır | K03 · K06 · K14 · K20 · K22 |
| D207 | Yorgunluk sahne başına tek sayı, ardışık düşüş en çok bir kademe. K14'ten sonra hiçbir klip dik ve dinlenmiş omuzla açılmaz; durum satırı önceki klibin SONUNU kelimesi kelimesine taşır | K14 → K15 → K16 → … → K24 |
| D138 | Metin yasağı KAPSAMLI: giysi + plaka + perçin + mandal + şerit. ⛔ Şeride çentik, gradasyon, ölçek işareti YAZILMAZ — ölçü aleti en riskli yüzeydir. Ölçüler SPEC'te; promptta gövde-göreli | 24/24 klip · M3 negatif cümlesi |
| D175 | Çıplak-deri negatifi ÜÇ BÖLGE birden (yaka · bilek · ayak bileği), tek cümlede, 24/24 promptta. Saydamlık tarifi yok; zorlanma giysinin YÜZEYİNDE | 24/24 klip · M1 negatif cümlesi |
| D146 | Vizör tek düz pane + görünür KALIN koyu çerçeve + derin yaka halkası. `seamless · bubble · dome · sphere` 0 kez. ⚠️ Referans paneli yazılmıyor → bu kilidin tek ölçülmüş aracı kapalı | 24/24 klip · M4 negatif cümlesi |
| D139 | Kamera sırtı gören klipte yokluk cümlesi POZİTİF yüzeye çevrilir: `one continuous sculpted surface from collar to hip, low-profile, with two shallow recessed panels, closed and smooth` | K08 · K12 (G kurulumu) |
| D209 | Üç çapa: ① kaynaksız parlak okra kubbe, güneş diski 0 ② aşağıda okra derinlik, ufuk çizgisi yok ③ yer imi plakanın kendisi ve bir perçin başı. Üçü 24/24 promptta BİREBİR | 24/24 klip · M2 negatif cümlesi |
| D210 | K01 ile K24 aynı kurulum harfi ve BİREBİR aynı kamera cümlesi. Her TIMELINE'ın son satırı `hold — the frame does not move`; CAMERA satırı `absolutely zero camera movement` | K01 ↔ K24 · 24/24 klip |
| D211 | K01 soruyu sorar: çene kapanıyor, içindeki yüzey hiç kavis yapmıyor. İlk 30 saniyede kurulum klibi en çok iki. Son kare adlandırılmış nesne: kesilmiş son mandal ucu; statik siyah 0 saniye | K01 · K02-K03 · K24 |
| D213 | Her temaslı klipte üç satır AYNI klipte: TEMAS · DEĞİŞİM · SONUÇ (sonuç ≥1 s kadrajda). Temas noktası kadrajın dış üçte birinde olamaz | mandal · bağ · şerit · makas geçen 14 klip |
| D214 | Her promptun ilk satırı `IN FRAME:`; SUBJECT yalnız kadrajdakini tarif eder. Yüz YALNIZ K19'da yazılır, kalan 23 klipte vizör cümlesi bile girmez | 24/24 klip |
| D200 | SPEC'te tek değer 0,904 g. Nötr yüzerlik POZİTİF kuralla (`floats in neutral buoyancy and is settling at a constant rate; it never hovers, never hangs motionless, never rises`). Bırakılan her nesne saniyeli düşüş satırı taşır | 24/24 klip · K04 · K14 |
| D141 | SPEC B FİNAL VURUŞ KANITI: kesilmiş DOKUZ mandal ucu, K23'te, sayılabilir 9 adet. Yoksa final teslim edilmemiştir | K23 · SPEC B |
| D192 | Bir numaralı risk pozitif biçimde ve sayıyla: `the batten lies hard against the plate and nowhere along its length is there a gap of light wider than the glove is thick` | K15 · SPEC göz kapısı |
| D123 | NEGATIVE'de şiddet/tehlike sözlüğü 0. Malzeme TARİF edilir: bağ ÇEKİLİR (kesilmez); asit `an even matte bloom spreading along the opened hem` olarak yazılır | K14 · K20-K24 · 24/24 negatif |
| D169 | Efor kanalı GİYSİNİN YÜZEYİNDE: `the glove's ribbed segments tighten over the tendons` · `the sleeves pull tight at the elbows`. 0,904 g Dünya gibi → `normal human pace, real time` | K03 · K06 · K14 · K20 · K22 |
| D216 | MUZIK katman tablosu: sahne başına aktif katman ≤4 · her kesmede yoğun CO₂ oda tonu köprüsü ≥0,2 s · kesmede dijital sıfır 0 kare | film boyu · MUZIK dosyası |

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle (boşsa "—")

> İki grup karışmaz. **A** etiketi filmin malzemesine uymuyor. **B** uygulanıyor
> ama tavan (20) dolduğu için ayrı satır almıyor — çoğu §5.1 çekirdeğinin sekiz
> cümlesinin İÇİNDE taşınıyor, yani filme özel bir karar gerektirmiyor.

**A — etiketi uymuyor, uygulanmıyor:**

| ders | neden bu filmde uygulanmadı |
|---|---|
| [D198] sıfır-g eksensel momentum | yerçekimi 0,904 g · kadrajda yüzen nesne yok |
| [D201] vakumda güneş açısı | vakum yok; kaynaksız kubbe ışığı, güneş diski 0 kare |
| [D203] replik envanteri | film bilinçli sessiz — SPEC `DIALOGUE LINES: 0`, tırnak 0 |
| [D217] replik görüneni söylüyor | replik yok |

**B — uygulanıyor, ayrı satır almıyor (çekirdekte ya da başka kilidin içinde):**

| ders | nerede taşınıyor |
|---|---|
| [D1] tek çekim | çekirdek cümle ① + CAMERA satırı |
| [D34] [D45] [D215] ekran metni · prompt künyesi · araç ayarı | çekirdek cümle ④ + üretim defterinin üç kutusu |
| [D167] kimlik yığını ≤3 | Character Bible üç öznitelikle yazıldı; boy GÖRELİ |
| [D42] [D147] yıpranma | kir GLOBAL bitiş olarak yazıldı; Character Bible kir merdiveni |
| [D176] kontrast garantisi | plakanın rengi TEK cümlede, World Bible'da |
| [D174] yön nesneye bağlı | yön cümleleri perçin ve mandal adıyla yazılıyor |
| [D172] taşıyıcının askısı | sarkan hiçbir şey yok — bağ çıktıktan sonra iki elde, serbest uç bırakılmıyor |
| [D208] kimlik dizisi | SPEC C tek satır (kask 24/24 kapalı · amblem 0 · bant SOL · kir K14'ten) |
| [D212] ardışık aynı vuruş | vuruş tablosunda ardışık tekrar 0 |
| [D180] planlı sessizlik | planlı mutlak sessizlik YOK; AUDIO satırı hiçbir klipte boş değil |
| [D78] sayaç tek karede | ölçek sayacının iki ucu K05'te aynı karede (eldiven ↔ perçin başı) |
| [D62] [D70] montajda düşen final | KESİLEMEZ LİSTESİ (aşağıda) + kurgu kapısı üç sayı |
| [D193] ışık takvimi | ⚠️ yön+Kelvin yerine TEK parlaklık dizisi — gerekçe Lighting Bible'da |
| [D16] yüz morph | yüz yalnız K19'da kadrajda; o tek klipte tek blok cümle |
| [D44] ağır çekim tuzağı | D169 satırının içinde (`normal human pace, real time`) |

---

## ⚓ ÇAPA ÜÇLÜSÜ — seçim BEDENDE okunur [D202]

> Aynı kanal, üç kez, aynı iki eldiven. ⛔ Dolgu jesti yazılmaz.

```
① K01  iki eldiven mandal kolunda — bir çeneyi KAPATIR (işini kurar)
② K15  aynı iki eldiven çelik şeridin iki ucunda — kendi ölçüsünü ALIR
③ K24  aynı iki eldiven aynı kurulumda (B) — son çeneyi KESMİŞ, açık bırakır
İLK ↔ SON: bir mandalı kapatır ↔ dokuz mandalı keser. Aynı eldiven, aynı
           kurulum, aynı kamera cümlesi, TERS jest.
```

## ✂️ KESİLEMEZ LİSTESİ — kurgu masasında düşerse film teslim edilmemiştir [D62 · D70]

```
K01  hook — soru burada sorulur; kırpılırsa film sebepsiz başlar
K03  katalizör (%12,5 bandı) — süre baskısı buradan geliyor
K06  karşıt kare — 50 px'lik TARTIŞILIR boşluk; K15 bunun cevabıdır
K14  MERKEZÎ SEÇİM + BEDEL — aynı karede
K15  NOVUM KANITI — filmin tek ölçümü; düşerse film konusuz kalır
K19  her şeyin kaybı — kararın alındığı tek yüz klibi
K21  DORUK
K23  FİNAL VURUŞ KANITI — dokuz kesik uç, sayılabilir 9 adet [D141]
K24  kapanış imajı — K01'in kamera cümlesini birebir taşır [D210]
⛔ Başlık kartı 0 saniye · statik siyah 0 saniye · ekran metni 0 s
   [LOSS_OF_LIFT 8. vakası: prompt yasağı 25/25 tuttu, kurgu masasında delindi]
```

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

> Maliyeti sıfır, iki satır. Bunu yazan tek film redleri önceden gören
> tek film oldu (YERÇEKİMİ). Kural: `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`

```
EN RED-RİSKLİ KARE:  K14 — iki eldiven yakın planda, bir bağ çekilirken,
                     örtünün kenarı açılırken (S5 · 2/3 EYLEM)
NÖTR TARİFİ:         "Two gloved hands draw a thick laced cord out of the
                     hemmed edge of a heavy fabric cover on the deck; a bright
                     steel ring sits between the gloves and the cord, and a
                     flat steel batten slides free of the hem."
                     · kesici alet YOK · gövde yüzeyine dokunulmuyor ·
                       giysi açılmıyor · `cut · remove · strip · tear` K14'ün
                       gövdesinde 0 kez · `open` YALNIZ mandal çenesi için
                       (giysi ya da gövde ile aynı cümlede 0 kez)
                     · kamera NESNE HİZASINDA (h 0,90 m · azimut 300°); iki
                       eldiven ARD ARDA ve farklı derinlikte, aralarında
                       parlak çelik halka (imza ① önlemi — YERÇEKİMİ F1 S8:
                       yüzsüz izolasyon + yan yana iki ön kol sahneyi İPTAL
                       ettirdi)
İKİNCİ RİSKLİ KARE:  K20-K24 — iki kollu makas dokuz mandalın boynunda.
                     Nesne METAL, hedef MAKİNE, gövde kadrajda ve bütün;
                     M8 negatif cümlesi bu kliplere GİRMEZ (makas vardır).
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

**Alınan her politika önlemi için:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Teknisyenin kendi giysisini açma jesti kaldırıldı; yerine platformun örtüsündeki bağın çekilmesi kondu. Kesici alet S5'ten çıktı. | Bedelin BEDENSEL olması gitti — "kendi korumasını kesiyor"un doğrudan acısı azaldı. | ② MALZEME SONUCU: açılan kenar boyunca yayılan mat bir kabarma, üç sahnede aynı cümleyle, geri dönmez · ③ ALET TEPKİSİ: bağ delikleri bozuldu, otomasyon aynı periyotta germeye devam eder ama örtü artık kapanmıyor · ④ TEMASSIZ GÖVDE TEPKİSİ: bağ çıkarken omuzlar düşer ve bir daha tam kalkmaz, bu sonraki üç klibin durum satırına iner |
| Parmak ucuyla dikiş sökme jesti kaldırıldı (modelin üretemediği iş sınıfı — eldiven tutulan şeyle eriyor). | Mikro jestin yakınlığı gitti. | ① KÜTLE-HIZ: aynı iş bütün gövdenin yaptığı bir harekete büyütüldü — iki elle kalın bağ çekilir, ağırlık geride, botlar çıkıntıya dayalı; ödeme saniyeli satırla ölçülür |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
   Dört kanal: kütle-hız · malzeme sonucu · alet tepkisi · temassız gövde tepkisi
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
⭐ VE BEDEL SAYILABİLİR HÂLE GELDİ: iniş hızı perçin sıralarının güverte
   kenarından geçme süresiyle okunuyor (40 s → 25 s → 18 s). Bedenden çıkan
   şey DÜNYADA sayıya dönüştü — ödeme kanalı bedende (omuz) ayrıca duruyor.
```
