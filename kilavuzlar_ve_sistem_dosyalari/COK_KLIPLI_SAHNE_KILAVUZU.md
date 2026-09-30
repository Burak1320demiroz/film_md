# 🎞️ ÇOK KLİPLİ SAHNE KILAVUZU — Bir Sahne, 2-6 Klip, Zincirsiz

> **Neden var (22.09.2026 · sahip kararı):** Depoda bir sahne bir klipti. 8 dakikalık
> film 48 kopuk olay gibi akıyordu. Sahibin 05.09 teşhisi (`ACI_YAYI` §3 🕰️) aynı
> yere işaret ediyordu: *"10 saniyede bir bambaşka açı kafa karıştırıyor."* Tek
> dinlenme aracı KÜME'ydi ve KÜME son kare zincirine bağlıydı ("continues the
> previous clip from its exact last frame").
>
> **Karar:**
> ① Son kare zinciri tamamen kalkar.
> ② Her klip bağımsız ve **tam 10 s** kalır; her klibin kendi IMAGE promptu vardır
>    (START FRAME = o klibin kendi onaylı karesi).
> ③ Bir SAHNE aynı mekânda, aynı eylemin içinde **2-6 klip** sürer.
> ④ Kapsam: yalnız yeni yatay filmler. Eski filmlere ve dikey shorts'a dokunulmaz.
>
> Klip sayısı, süre, bölüm/QA birimi ve betik sayımları değişmez. Değişen şey,
> klibin sahne içindeki yeridir: izleyici 48 kopuk olay yerine 10-18 derin sahne izler.
>
> **Ne zaman okunur:** hikâye sahne sahne yazılırken (yeni-film 0.7), sahne haritası
> ve `SAHNE PLANI` satırı kurulurken ve her bölüm dosyası yazılırken.
> **Kapı:** `prompt_kontrol.py` ㉜ · sayılar betiğin başında (`SAHNE_KLIP_BANDI`).

---

# 0. 📖 BİRİM — SAHNE ≠ KLİP (bu rejimde)

```
SAHNE  dramatik birim · aynı mekân + aynı eylem + aynı ışık/ses yatağı
       2-6 klip (20-60 s) · 1 klip yalnız HOOK ya da geçiş, gerekçeyle
       numarası S01, S02 … (1'den)
KLİP   üretim dosyası · tam 10 s · kendi IMAGE + VIDEO promptu
       numarası K01 … K48 (1'den, filmin sonuna kadar kesintisiz)
ÇEKİM  = KLİP (sahne içi kesme klipler arasındadır, klip içi kesme YOK)
```

`KURGU_VE_TESLIM` §0'daki üç kelimenin bu rejimdeki karşılığı: **SCENE COUNT ≠
CLIP COUNT · SHOT COUNT = CLIP COUNT.** SPEC'e iki satır yazılır. Kurgu kapısı
(klip sayısı, süre) klip üzerinden ölçülür; hiçbir sayım değişmez.

⛔ **Zincir YOK.** Klipler birbirinden bağımsız üretilir. Onları birbirine bağlayan
yalnız üç şeydir: **durum kilidi satırı** (§3), **sahne kilidi cümleleri** (§4) ve
**kare onayı** (§3.3).

---

# 1. 📐 BANT VE PLAN SATIRI

```
SAHNE PLANI: 1 3 4 4 2 4 6        ← PLAN'da, sahne haritasının kod bloğunda
             sahne başına klip sayısı · toplam = CLIP COUNT
             ⭐ BU SATIR ㉜ KAPISINI AÇAR ve ⑩④ KÜME hedefini kapatır
```

| sahne | ne zaman | not |
|---|---|---|
| **1 klip** | yalnız HOOK (K01 soru) ya da geçiş | 📍 başlığının altına `TEK KLİP GEREKÇESİ:` yazılır, yoksa ㉜ FIX |
| **2 klip** | geçiş, kısa eylem, nefes | KURULUM → SONUÇ |
| **3 klip** | filmin ana birimi | KURULUM → EYLEM → TEPKİ |
| **4-5 klip** | doruk, bedel, novum | §2 büyük sahne şablonu |
| **6 klip** | yalnız doruk | tavan: üstü güvenlik kamerası hissi (`ACI_YAYI` §4 alt bandıyla aynı gerekçe) |

**Kaba dağılım** (ölçülmedi ⬜, ilk film sınar): 48 klip ≈ 14-16 sahne; 24 klip ≈ 7-9 sahne.

⛔ **Bölüm sınırı = sahne sınırı.** Bölüm dosyası tam sahnelerle başlar ve biter
(12 klip = 3+4+5 · 2+4+6 · 4+4+4 …). QA part masterı sahne ortasından kesilmez.
`film_klasoru_ac.sh --sahne-plani` açılışta, ㉜③ yazımda denetler.

⛔ **Sahne sayısı hikâyeden gelir, klip sayısı formattan.** Format kartı klip
sayısını verir (48 klip = 8 dk). Hikâye ise sahneleri verir. Plan satırı ikisini
eşler.

---

# 2. 🎬 KAPSAMA ŞABLONLARI — her klibin sahnedeki ROLÜ

Rastgele üç açı yazmak, üç kopuk klip üretmektir. Klibin rolü önce seçilir, açı
sonra gelir. Rol sahne tablosunun `ROL n/N` sütununa ve klip başlığına yazılır.

```
2 KLİP (20 s) — geçiş / kısa eylem
  1/2 KURULUM   geniş · karakter mekânda, hedefe yöneliyor
  2/2 SONUÇ     yakın/karşı açı · eylemin sonucu + beden tepkisi

3 KLİP (30 s) — ana birim
  1/3 KURULUM   geniş/orta · konum + hedef (izleyici coğrafyayı öğrenir)
  2/3 EYLEM     yakın/detay · ana eylem SÜREÇ olarak (kol çekiliyor, alet kesiyor)
  3/3 TEPKİ     karşı açı/vizör · sonuç + yüz/beden tepkisi

4-5 KLİP (40-50 s) — doruk / bedel / novum
  1 BELİRİŞ     geniş/orta · tehdit ya da hedef görünür
  2 MÜCADELE    yakın · efor başlar (gövde tepkisi, ⑳)
  3 TERSLİK     makro/detay · kilitlenme, arıza, beklenmeyen direnç
  4 KARAR       vizör içi yüz · nihai efor (4 kliplikte KARAR + BEDEL birleşir)
  5 BEDEL       geniş'e dönüş · sonuç ve ödenen bedel

6 KLİP (60 s) — yalnız doruk
  5'li şablon + araya bir DÖNÜŞ klibi: KURULUM kamerasına geri dönüş
  (A-B-C-A-D-A) · izleyiciye haritayı yeniden verir
```

**Kurulum kuralları sahne içinde de geçerlidir** (zincir yok, yani kalkan gerekli):

- Ardışık iki klip **aynı kurulumu kullanamaz**. `ACI_YAYI` §3 güvenli bandı (≥1 ölçek kademesi VE ≥45°) aynen geçerli; ⑩① bunu BLOCK'lar.
- Sahne içinde **A-B-A dönüşü teşvik edilir.** Bir sahnenin master'ına dönmek en doğal dönüştür ve `ACI_YAYI` §4b DÖNÜŞ %40 hedefini kendiliğinden doldurur. Dönüş işareti: `— the same position, height and lens as Clip N.`
- Bir sahne en az **iki kurulum** kullanır (㉜⑦). Tek kurulumlu sahne güvenlik kamerası kaydıdır.
- ⛔ **KÜME bu rejimde yoktur.** "Bekleme" artık aynı kurulumda kalmak değil, aynı mekânda ve aynı eylemde kalmaktır. ⑩④'ün "KÜME ≥2" hedefi SAHNE PLANI beyan eden filmde koşmaz.
- Ekran yönü sahne içinde çevrilmez: hedef-dilim, omuz hattı ve yön kilitleri aynen korunur (`UZAMSAL_HARITA`).

---

# 3. 🔒 DURUM KİLİDİ — `CONTINUOUS ACTION:` satırı

Zincir olmadığı için model her klibe sıfırdan başlar. Uyarı yapılmazsa karakteri
nötr bedenle, başka bir yerde başlatır. Depoda bunun dört filmlik kaydı var
[D207]: THE AMBER LATTICE S12 patlama → S13 *"sudden reset … calm standing posture"*.

## 3.1 Kural

Sahnenin **2. ve sonraki** her klibinde, **hem IMAGE hem VIDEO** promptunda,
`IN FRAME:` ve `Clip n of N.` satırlarından hemen sonra:

```
CONTINUOUS ACTION: <önceki klibin SON saniyesindeki durum — ŞİMDİKİ zamanla, kadrajda görünen olarak>
```

```
✅ CONTINUOUS ACTION: she is already at the hatch, right glove on the lever, left knee braced
   against the rim, frost cracked along the seam, breath fog on the inside of the pane.
```

- **Kaynak:** sahne tablosunda önceki klibin `OLAY BAŞ → SON` hücresinin SON yarısı. Satır bu yarıdan kelimesi kelimesine iner [D207 DEĞİŞEN SATIR].
- **IMAGE promptunda da ZORUNLU.** I2V'de imaj t=0'dır [D179 · ⑳b]; durum imaja yazılmazsa video onu geri getiremez.
- **Sıfırlanamayanlar:** mekân · ışık · kıyafet kiri ve hasarı · temel poz (hangi el nerede, hangi diz nerede) · eldeki nesne · açık/kapalı durumu (kapak, vizör, kask) · yorgunluk işareti [D207 BEDEL EĞRİSİ].
- ⛔ **Sahnenin 1. klibine yazılmaz** (㉜④ FIX). Sahne başı yeni bir durumdur; önceki sahneye bağ SINIR SATIRI olarak planda kalır (`SAHNE_ZINCIRI` §5).

## 3.2 Yazım yasakları [D59 · ZİNCİR DİLİ]

```
⛔ geçmiş anlatma     "after she pulled the lever in the previous clip …"
                      → modele geçmiş vermez, ismini çizdirir [D59]; ŞİMDİKİ durumu yaz
⛔ zincir dili        "continues the previous clip" · "exact last frame" · "picks up where
                      the previous …" · önceki klibe bağlanan START FRAME
                      → ㉜⑤ BLOCK. Zincir kalktı; bu kalıplar ayrıca ⑩①'in DEVAM_KLIBI
                        muafiyetini tetikler ve aynı kurulumun art arda gelmesine kapı açar
⛔ yokluk listesi     "no longer standing, not calm" → yasak isim kazanır [D59]
✅ START FRAME        "the approved still from this clip's IMAGE prompt — animate it; …"
```

## 3.3 Kare onayı — satır tek başına yetmez

MARS_SON_CIKIS'te (15.09.2026) S15'in IMAGE promptu yaralı yürüyüşü yazıyordu ve
film yine sıfırladı [D207 TEKRAR]. **Satır gerekli ama tek başına yetmez.** İkinci
kapı insan gözüdür:

```
□ Sahnenin 2.+ klibinin IMAGE karesi, ÖNCEKİ klibin son saniyesinden alınmış bir
  kareyle YAN YANA konur. Poz, eldeki nesne, kir/hasar, ışık yönü ve kapak/vizör
  durumu tutmuyorsa kare REDDEDİLİR ve yeniden üretilir; video o kareden üretilmez.
  (Bu bir ZİNCİR değildir: önceki kare üretime girmez, yalnız karşılaştırma içindir.)
□ Bir sahnenin klipleri aynı oturumda, art arda üretilir [D84 ②].
□ ⬜ İSTEĞE BAĞLI: sahnenin ilk onaylı karesi, aynı sahnedeki sonraki kliplerin
  imaj üretiminde mekân/ışık REFERANSI olarak yüklenebilir. Zorunlu değildir;
  denenirse sonucu üretim defterine yazılır. İlk film ölçer.
```

⚠️ **D84'ün uyarısı sürer:** sahneler arası nicelikler (toz seviyesi, yıpranma
takvimi) metinle kilitlenmekte zorlanır. Bu rejim riski azaltır, çünkü sahne içinde
nicelik değişmez; sıfırlamaz. Nicelik değişimi (kir artışı, hasar) sahne sınırına
konur ve yeni sahnenin 1. klibinde yeni değer olarak yazılır (`SAHNE_ZINCIRI` §0:
DURUM DEĞİŞİMİ klibe değil SINIRA yazılır).

## 3.4 Kesme noktası — klip süren bir hareketin İÇİNDE biter (🆕 TUR 24 · ÖNERİ)

Klasik kurguda "eylem üzerinden kesme" iki çekimin aynı hareketi örtüşerek çekmesi ve
kesmenin hareketin ortasına konmasıdır. Bizde klip **tam 10 s** ve kırpılmaz (sahip kararı
22.09.2026 · kurgu kapısı ±0). Yani kesme noktası kurgu masasında seçilmez; **yazımda**
kurulur:

```
KLİP N    son TIMELINE satırı SÜREN bir süreçle biter — "she keeps her weight on the
          lever, shoulders still dropping" ✅   ·   "the lever stops, she stands up" ⛔
KLİP N+1  aynı süreç, başka kurulumdan, ZATEN SÜRERKEN başlar —
          "CONTINUOUS ACTION: her weight is already on the lever, shoulders low …"
```

Bu, `SAHNE_DOLULUGU`'nun "son satır SÜRDÜRME" kuralının sahne içindeki işlevidir: klibin
bitişi bir durak olursa kesme bir durakta olur ve iki klip arasındaki en küçük kayma
(ışık, kıvrım, arka plan) görünür. Hareketin içinde kesilirse göz hareketi izler.
⚠️ Mekanizma rapor iddiasıdır (TUR 24 1A); ÖLÇÜLMEDİ. İlk filmde ② INTRA-SCENE CUTS ölçer.

**Durum cümlesi EYLEM FİİLİ değildir.** `She grips the lever` modele "0. saniyede tutmuyor,
tutmaya başlıyor" der ve klip bir uzanmayla açılır. `She is already gripping the lever`
0. saniyeyi kurulu verir. Depo ölçümü aynı yönü gösteriyor: temas bulgusu klibin ilk 2
saniyesinde en düşük (%5,9), 2-4 s bandında en yüksek (%19,4) (`PROMPT_HATA_ONLEME` §3b ①).

**Yasak bağlaçlar** (rapor · ÖNERİ): `Next scene` · `Following shot` · `After that` —
model zaman/mekân sıçraması okur ve dekoru yeniden kurar. `Suddenly` — sarsıntı, parlama,
patlama ekler. Sahne içi klibin promptunda **zaman bağlacı yoktur**; süreklilik yalnız
şimdiki zamanlı durum cümlesiyle taşınır.

## 3.5 Ekran yönü ve prop çapası — açı değişince dünya dönmez

Sahne içinde kurulum değişir, dünya değişmez. İki kilit gerekir:

```
EKRAN YÖNÜ  anatomik uzuv + kadrajdaki yeri birlikte yazılır — açı değişince "sol el"
            kelimesi tek başına ters dönebilir (rapor 1B · UZAMSAL_HARITA ile aynı ilke):
            ✅ "her left glove, on the right side of the frame in this frontal view, stays on the lever"
            Bakış/gidiş yönü sahne boyunca aynı ekran yönüne yazılır ("facing screen-left").
            180° çizgisi sahne İÇİNDE aşılmaz (UZAMSAL_HARITA · ACI_YAYI §3 sonu).

PROP ÇAPASI sahnenin sabit nesneleri (kapak, kasa, boru, konsol) BİÇİM + MALZEME + KONUM
            cümlesiyle yazılır ve sahnenin bütün kliplerinde BİREBİR kopyalanır:
            ✅ "a round hatch of dark riveted metal, one arm-span wide, set low in the pale ice bank"
            Kadrajda görünmeyen klipte yazılmaz (IN FRAME dışı [D214]); göründüğü her klipte
            aynı kelimelerle yazılır (PROMPT_HATA §3 sınıf 11: aynı kurulum = aynı arka plan cümlesi).
```

⭐ Sınama vakası: THE_SLOW_RAIN S17'de yerde çekilen kanat-kızak S20'de sırtta, S22'de
yine yerde (② 🔴). O dizide kızağın **yeri** cümlede yoktu, yalnız varlığı vardı. Bu rejimde
aynı eylem bir sahneye toplanır ve kızağın konumu prop çapasına yazılır
(`"the folded wing sled lies flat on the ice behind her, its tow strap taut to her harness"`).

## 3.6 Temas sahne içinde bölünebilir — tek klipte imkânsız olan çözüm

`PROMPT_HATA_ONLEME` §3b ③'ün en güçlü çaresi "temas anını atla, öncesini ve sonrasını
göster" idi — ama tek klipte kesme yoktur, uygulanamıyordu. Çok klipli sahnede uygulanır:

```
KLİP N    HAZIRLIK — eldiven kola doğru, ağırlık geride, temas YOK ya da ilk 2 s'de kurulu
KLİP N+1  SONUÇ    — "CONTINUOUS ACTION: her glove is already closed on the lever …";
                     temas 0. saniyede kurulu gelir, klip temasın SONUCUNU gösterir
                     (kapak aralanır, buhar çıkar)
```

Temas hiçbir klipte "oluşmaz"; biri öncesini, öteki sonrasını taşır. Mikro el işleri için
tam tablo: `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md`.

---

# 4. 🔊 SAHNE KİLİDİ VE SES KÖPRÜSÜ

## 4.1 Birebir cümleler

Aynı sahnenin **bütün kliplerinde** aşağıdaki satırlar harfi harfine aynıdır (㉜⑥ FIX):

```
IMAGE  LIGHT:     ışık kaynağı · yön · gölge · palet
VIDEO  PHYSICS:   yerçekimi · atmosfer · parçacık davranışı
VIDEO  AUDIO:     İLK CÜMLE = sahnenin ses yatağı (oda tonu / rüzgâr / uğultu)
```

Klipten klibe değişenler: **kurulum · eylem evresi · AUDIO'nun ikinci cümlesi
(vurgu sesi) · replik.** Sahne kilidinin Türkçe özeti bölüm dosyasında 📍 başlığının
altına yazılır (`> SAHNE KİLİDİ: mekân · ışık · ses yatağı · kir/hasar durumu`)
ama prompta girmez.

⭐ `KURGU_RITMI` §2 örüntü kırıcı (ardışık iki birim aynı ölçek + palet + ses
dokusunda olamaz) bu rejimde **sahneler arasında** uygulanır. Sahne içinde palet ve
ses yatağı zorunlu olarak aynıdır; farkı yalnız kurulum üretir.

## 4.2 Klip başına ses dramaturjisi (3 kliplik sahnenin varsayılanı)

```
1/3  sessiz gerilim — ses yatağı + nefes / bot / eldiven sesi · No dialogue.
2/3  eylem anı      — ses yatağı + eylemin fiziksel sesi · replik varsa BURADA,
                      tek kısa cümle, yakın planda (ağız okunur) [DIYALOG_SAHNESI §2-§3]
3/3  dinleme        — ses yatağı + telsiz cızırtısı / yapının tepkisi · karakter konuşmaz
```

- Sahne başına **en çok bir replikli klip** (varsayılan). İkincisi `DIYALOG_SAHNESI` muhatap kuralıyla gerekçelenir.
- OMNI katmanı aynen geçerli: ses her klipte doludur, replik yoksa `No dialogue.` yazılır, tırnak kullanılmaz (`OMNI_1_1_FLASH` kılavuzu).
- Ses köprüsünü kurguda ses yatağının kesintisizliği taşır: klipler arası kesmede oda tonu değişmez (`KURGU_RITMI` ses köprüsü). Müzik sahne içinde kesilmez.

---

# 5. ⏱️ DOLULUK — klip içi üç evre, sahne boyu süreç

`SAHNE_DOLULUGU` her klip için aynen geçerlidir: üç evre, ≤3 TIMELINE satırı, son
satır SÜRDÜRME. Bu rejimin eklediği tek şey, eylemin **sahne boyunca** bir SÜREÇ
fiili olmasıdır:

```
3 kliplik "kapağı açmak":
  K1  0-10 s  yaklaşır · kolu bulur · eldiven kola kapanır       (SON: el kolda)
  K2  0-10 s  ağırlığını verir · durur, gerilimi tutar · yeniden yüklenir · buz çatlar (SON: ağırlık kolda)
  K3  0-10 s  kol dayanır · gaz sızar vizöre · içeri bakar        (SON: yüz aralıkta)
```

⛔ "Kapağı açar" tek klipte biten bir iş fiilidir; sahneyi 3 s'de bitirir, 27 s'yi
boş bırakır. Sahne fiili süreçtir, her klip onun bir evresini taşır. Klibin SON'u
bir sonraki klibin `CONTINUOUS ACTION:` satırıdır (§3).

---

# 6. 🪝 HOOK · NOVUM · DORUK · BEDEL · FINAL

- **K01 hook sorusudur** [D211: ilk 10 s soru · ilk 30 s ≤2 kurulum]. Önerilen: S01 tek klip (gerekçe: hook), S02 3 klip ile ilk 30 s. Ya da S01 3 klip, 1/3 soru.
- **Kilit roller klibe bağlanır:** `--kilit-sahne <FMT> <FILM> K<nn> <ROL>` → `K<nn>_<ROL>.md`. Rol dosyasına sahne numarası da yazılır. DORUK ve BEDEL genellikle 4-6 kliplik bir sahnenin KARAR/BEDEL klibidir.
- **BEDEL satırı** (B5) sahne numarasıyla yazılır (`S11`); kaybın görüldüğü klip de verilebilir (`S11 · K38`).
- **FINAL** son sahnenin son klibidir; `ACILIS_KAPANIS_CIFTI` ilk kare ↔ son kare kuralı K01 ↔ son klip arasında ölçülür.

---

# 7. 📝 TAM ÖRNEK — 3 kliplik bir sahne (V3 + OMNI katmanı)

Bölüm dosyasında:

```
# 📍 SAHNE 02 — DONMUŞ KAPAK  (3 klip · 0:10–0:40)

> SAHNE KİLİDİ: buzlu kapak, kehribar pus, düşük uğultu, eldivenlerde kuru buz tozu

## 🎬 KLİP 02 — S02 · 1/3 · KURULUM — KAPAĞA VARIŞ
## 🎬 KLİP 03 — S02 · 2/3 · EYLEM — KİLİT KOLU
## 🎬 KLİP 04 — S02 · 3/3 · TEPKİ — BUHAR
```

**KLİP 03 · IMAGE** (2/3 — durum kilidi var, LIGHT sahnenin öteki klipleriyle birebir):

```
IN FRAME: hands · torso
Clip 3 of 24.
CONTINUOUS ACTION: she is already at the hatch, right glove closed on the short lever, left knee braced against the frosted rim, pale dust on both gloves.
The lever is a forearm long and still frozen in place; a thin line of frost runs along the hatch seam.

Her gloved right hand grips the lever at chest height, the ribbed sleeve and the scuffed composite chest plate filling the lower right of the frame, the teal chest band just visible. The dark metal rim of a round hatch set into a pale ice bank fills the left half of the frame, frost crusted in its grooves.
LIGHT: even amber haze fill from the whole sky, shadows soft and shallow, no sun, no lens flare.
CAMERA: 75mm lens on a locked-off camera 1.2 m to her left, camera height 1.10 m, eye-level close-up, three-quarter left.

NEGATIVE: <KILAVUZ_REHBERI §5.1 çekirdek — 7 cümle> <+ ≤3 sahneye özel>

Output: 16:9, 4K, no text, no watermark.
```

**KLİP 03 · VIDEO:**

```
IN FRAME: hands · torso
Clip 3 of 24. Duration 10 seconds.
CONTINUOUS ACTION: she is already at the hatch, right glove closed on the short lever, left knee braced against the frosted rim, pale dust on both gloves.
START FRAME: the approved still from this clip's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
She leans back into the lever with her whole weight, halts holding the strain, then pulls again.

TIMELINE: 0.0s — her glove is closed on the lever, knee braced, the frost line unbroken. 3.0s — she drives her weight down through both arms and halts, holding the strain, her sleeves pulling tight at the elbows; the frost cracks along the seam. 7.0s — her shoulders drop into a second pull and she keeps her weight on the lever through the last second, chest rising and falling.

CAMERA: 75mm lens on a locked-off camera 1.2 m to her left, camera height 1.10 m, eye-level close-up, three-quarter left, deep focus, fixed lockoff — absolutely zero camera movement. In a single continuous shot.
PHYSICS: Gravity is 0.38 g under a dense cryogenic atmosphere at 0.9 bar; dust settles at once, no wind.
AUDIO: the low hum of the dense cold air carries under everything. A dull metal groan as the lever gives and a dry crackle of frost along the seam. No dialogue. No music.

NEGATIVE: <KILAVUZ_REHBERI §5.1 çekirdek — 8 cümle> <+ ≤3 sahneye özel>

Output: 16:9, no text, no watermark.
```

KLİP 02 (1/3) aynı LIGHT/PHYSICS/AUDIO-ilk-cümleyi taşır, `CONTINUOUS ACTION:`
taşımaz ve geniş kurulumdadır (örn. 24mm · 6 m · WS · frontal). KLİP 04 (3/3)
karşı açıdadır (örn. vizöre 35mm · MCU), `CONTINUOUS ACTION:` satırı K03'ün SON
durumunu (ağırlık kolda, omuzlar düşük, buz çatlak) taşır ve AUDIO'nun ikinci cümlesi gazın tıslamasıdır.

---

# 8. ✅ KAPI VE KONTROL LİSTESİ

**Betik — `prompt_kontrol.py` ㉜** (yalnız `SAHNE PLANI:` taşıyan filmde koşar):

| # | denetim | seviye |
|---|---|---|
| ① | SAHNE PLANI toplamı = KLİP başlığı sayısı · her `📍` başlığının `(n klip)` beyanı = altındaki KLİP sayısı · sahne/klip numaraları 1'den kesintisiz | BLOCK (numara FIX) |
| ② | sahne > 6 klip · tek klip ve `TEK KLİP GEREKÇESİ:` yok | FIX |
| ③ | sahne bölüm dosyası sınırını aşıyor | FIX |
| ④ | 2.+ klipte `CONTINUOUS ACTION:` yok (IMAGE ya da VIDEO) · 1. klipte var | BLOCK · FIX |
| ⑤ | zincir dili ya da önceki klibe bağlanan START FRAME | BLOCK |
| ⑥ | LIGHT / PHYSICS / AUDIO-ilk-cümle sahne içinde birebir değil | FIX |
| ⑦ | sahnenin bütün klipleri tek kurulumda | FIX |

Ayrıca bu rejimde: ⑩① ardışık aynı kurulum BLOCK (muafiyet yok) · ⑩④ KÜME ≥2
koşmaz, DÖNÜŞ %40 koşar · ㉙ satır = SAHNE ve `(n klip)` toplamı = klip sayısı ·
㉚ satır = KLİP (`| K07 | S03 | 2/3 · EYLEM |`) ve SAHNE sütunu plana uyar.

**Yazım kontrolü (insan):**

```
□ SAHNE PLANI PLAN'da · hikâye onayı sahne başına bir satır, (n klip · aralık) ile
□ her sahne bir kapsama şablonuna oturuyor (§2) · rol tabloda ve başlıkta
□ sahne fiili SÜREÇ · her klibin SON'u bir sonraki klibin CONTINUOUS ACTION'ı (§3, §5)
□ sahne kilidi cümleleri kopyala-yapıştır (§4) · replik ≤ 1 klip
□ ardışık klipler ≥1 kademe + ≥45° · sahne içi A-B-A dönüşü işaretli
□ üretimde kare onayı: önceki klibin son karesiyle yan yana (§3.3)
```

---

# 9. ⬜ ÖLÇÜLMEMİŞ — ilk film sınar

- `CONTINUOUS ACTION:` satırının pozu gerçekten taşıyıp taşımadığı. Ölçüm, ilk filmin ② DEVAMLILIK raporunda sahne içi kesmelerden gelir (SPEC'teki "sahne içi kesmeler" listesi merceğe hangi kesmelerin eşleşmesi gerektiğini söyler).
- Kaba dağılım (48 klip ≈ 14-16 sahne) ve 6 klip tavanı. İzleyici tutması `YAYIN_PERFORMANS` tablosundan okunur.
- Sahne ilk karesinin referans olarak yüklenmesinin (§3.3) etkisi.
- Bu kılavuz ilk filmle sınanmadan DERS yazılmaz. Sapma önce bu dosyada düzeltilir (Kart G).

**Kaynaklar:** sahip kararı 22.09.2026 · TUR 24 rapor 1A · 1B (§3.4-§3.6 · `URETIM_ONCESI_ANALIZ/04` §TUR 24) · [D207] · [D84] · [D59] · [D179] · [D211] ·
`ACI_YAYI_VE_SEKANS` §3-§4b · `SAHNE_ZINCIRI_VE_SINIR` §0 · §5 · `SAHNE_DOLULUGU` ·
`KURGU_VE_TESLIM` §0 · `KURGU_RITMI` §2 · `DIYALOG_SAHNESI` · `OMNI_1_1_FLASH`.
