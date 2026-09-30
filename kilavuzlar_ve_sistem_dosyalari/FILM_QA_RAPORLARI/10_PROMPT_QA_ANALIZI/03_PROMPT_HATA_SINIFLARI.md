# ⭐ PROMPT HATA SINIFLARI — bu klasörün asıl çıktısı

> **Girdi:** 34 filmin `02_FILM_ANALIZLERI/` dosyaları · 395 geçerli ham rapor
> (31 film belgeli ızgarayla, 3 film **ölçülmüş** ızgarayla — 19.09.2026 genişletmesi)
> **Eşik:** `00_DERS_YAZIM_KONTRATI` §2b — **tek filmde görülen örüntü ders olmaz**.
> Buradaki her sınıf ≥ 2 filmden kanıt taşır; tek filmlik olanlar §ADAY'da.

```
TOPLAM HÜKÜM     🅐 323 · 🅑 391 · 🅒 33 · 🅓 24   =  771 tekil bulgu
🅑 ORANI         %55  (391 / 714)
⭐ ANLIK GÖRÜNTÜ: 19.09.2026 14:24. Korpus CANLIDIR — THE_FALLING_WORLD'ün ikinci yarım QA'sı
   oturum sırasında koştu (15 mercek). Yukarıdaki hüküm dağılımı 771 bulguluktur;
   defter (01_) makineyle güncel ve daha yüksek sayı gösterebilir. Sınıf örüntüleri
   bundan etkilenmez, yalnız toplamlar kayar.
OKUMA            Bulguların yarısından biraz fazlası PROMPTTA önlenebilirdi.
                 Diğer yarısı kilit yazılı olduğu hâlde tutmadı — onlar
                 yazım işi değil, KADRAJ · ARAÇ · KURGU işidir.
```

---

## 📊 ÖLÇÜM — çekirdek cümlelerin 31 filmdeki kapsaması

`prompt_hata_analizi.py --kilit` her filmin her sahnesinde ölçtü:

| çekirdek cümle | hiç yok | kısmi | tam |
|---|:--:|:--:|:--:|
| `AUDIO:` satırı | **12** | 8 | 11 |
| ortamın ses yasası (dış ses var mı yok mu) | **24** | 7 | **0** |
| insan sayısı (`exactly N human`) | 4 | 20 | 7 |
| temas sınırı (`no merging / no phasing`) | **9** | 17 | 5 |
| giysi/donanım devamlılığı (`identical, no drift`) | **12** | 13 | 6 |
| parçacık momentumu | 5 | 18 | 8 |
| bloom (`0% bloom`) | 3 | 8 | 20 |
| metin yasağı | 1 | 9 | 21 |
| efor/beden cevabı | 0 | **29** | 2 |
| ortamın ADI (vakum / ince atmosfer / 0-g) | 6 | 18 | 7 |
| ortamın SAYISI (`0,30 g` · `m/s²`) | **14** | 10 | 7 |
| filigran yasağı | 2 | 9 | 20 |
| kamera/tek çekim | 3 | 8 | 20 |

⛔ **"Kısmi" en tehlikeli sütundur.** Bulguların büyük kısmı, cümlenin filmde
VAR olduğu ama **o sahnede DÜŞTÜĞÜ** yerlerde. Negatif çekirdek film başına bir
kez yazılıp her prompta birebir kopyalanmıyor; sahne sahne elle yazılıyor ve kayıyor.

---

# 🅑 PROMPT HATASI SINIFLARI — önlenebilir olanlar

## 🅑1 · ORTAMIN SES YASASI HİÇ YAZILMIYOR · **24/31 film** ⭐ en yaygın

**Ölçüm:** 31 filmin **hiçbirinde** ortam ses yasası bütün sahnelere yazılmamış;
24 filmde hiç yok. `AUDIO:` satırı olan filmlerde bile satır **ne duyulduğunu**
yazıyor, ortamın **neyi taşıyıp taşımadığını** yazmıyor.

**Kanıt:** KRONOS 4 🔴 · MARS 2 🔴 · COLD_WELD 1 🔴 · STANDING_WIRE · STILL_SWARM ·
TETHERED_MASS · LOOK_UP · SHATTERED_BREATH.

**Yazım kuralı:** her video promptunun `AUDIO:` satırı ortamı adlandırır ve
**neyin taşıdığını** söyler — `no exterior sound at all; the hull parts in silence`
(vakum) ya da `a low muffled rumble, no high frequencies` (ince atmosfer).

⚠️ **Ama bu kural tek başına yetmiyor — bkz. 🅐1.**

## 🅑2 · TEMAS SINIRI CÜMLESİ SAHNELERİN BİR KISMINDA DÜŞÜYOR · **17 film kısmi · 9 film hiç**

**Kanıt (cümlenin DÜŞTÜĞÜ sahnelerde çıkan BLOCKER'lar):** FROST_LINE 5 🔴 ·
ROSE_COAT 4 🔴 · BORROWED_WEIGHT 3 🔴 · SILENT_PERIHELION 3 🟠 · SKYLIGHT 3 🟠 ·
UPWARD_FALL 4 🟠 · MARS 3 🟠 · GREEN_CEILING 2 🟠 · HEALING_GROUND 2 🟠 ·
COLD_WELD 2 🔴 · AMBER_LATTICE 2 · TETHERED_MASS 2 · MIRROR_FAUNA 1.

**Yazım kuralı:** `Hand-to-surface contact keeps a clear boundary, no merging,
no phasing, no extra fingers.` — **eldivenin bir şeye dokunduğu HER sahnede**.

## 🅑2a · TEMAS CÜMLESİ TEK YÖNLÜ — NESNE-NESNE GEÇİŞİ KAPSAMSIZ · **26 bulgu** ⭐ 19.09 eklendi

Promptlardaki cümle `hand-surface contacts` diyor; el karışmayan geçiş
(kayış ↔ pim · halat ↔ abajur · kemer ↔ gövde · canlı uzvu ↔ giysi) hiçbir
cümlenin kapsamında değil. **81 temas/geçiş bulgusunun 26'sı bu sınıfta.**

Kanıt: DRY_ANCHOR S09 ×2 🔴 · COUNTED_TURN S10 🔴 · S16 🔴 · S18 🔴 ·
LEANING_ROOM S05 · STILL_SWARM S12 🔴 · LOOK_UP S05 🔴 ×2 · BENI_HATIRLAMA S03 · S28.

⚠️ **Bu sınıf 19.09.2026'da SAHNE SAHNE OKUMAYLA bulundu** — regex matrisi
"temas cümlesi var" diyordu, cümlenin ne kapsadığını okumak gerekiyordu.
İlgili filmlerin 🅐 hükümlerinin bir kısmı bu yüzden 🅑'ye çevrilmelidir
(⬜ dosya düzeyinde henüz yapılmadı).

**Yazım kuralı:** `Hand-to-surface **and object-to-object** contacts both keep a
clear structural boundary…`

## 🅑3 · GİYSİ/DONANIM DEVAMLILIK CÜMLESİ YOK · **12 film hiç · 13 kısmi**

**Kanıt:** MARS 4 🔴 + 3 🟠 (askı kol değiştiriyor · miğfer takılı/elde/takılı) ·
UPWARD_FALL 5 · STANDING_WIRE 4 · SKYLIGHT 4 · KRONOS 4 · HEALING_GROUND 3 ·
LEANING_ROOM 3 · RESONANT_STRAND 3 · TETHERED_MASS 2.

**Yazım kuralı:** giysi cümlesi Bible'dan **birebir** kopyalanır; kir/hasar bir
**durum merdivenidir** (PHASE n) ve geri sayılmaz.

### 🅑3a · ASİMETRİK İŞARET HANGİ KOLDA, YAZILMIYOR · **3 film**
MARS (askı ve omuz yaması sağdan sola) · LEANING_ROOM (bileklik 3 kez) ·
BENI_HATIRLAMA (kol bandı aynalanıyor). Yama · askı · bant · kılıf:
hepsi `on his **left** upper arm` biçiminde yazılır.

## 🅑4 · ORTAM SAYIYLA DEĞİL TARİFLE YAZILIYOR · **14 film hiç · 10 kısmi**

⭐ Bu sınıfın kanıtı deponun kendi ölçümünü dördüncü kez doğruluyor:
*tarif kilidi %0 tuttu, sayısal kilit %100 tuttu.*

| film | promptta yazan | ekranda ölçülen |
|---|---|---|
| BENI_HATIRLAMA | `about two thirds of Earth's weight` + `the stated gravity` | 0,39 · 1,11 · 1,13 · 2,48 m/s² — **2,9× tutarsızlık, 2 🔴** |
| LOOK_UP | `gravity` · `gravity drift obeyed` (sıfat) | 1,73 ↔ 6,67 m/s² aynı güvertede — **1 🔴** |
| THE_FALLING_WORLD | **`Gravity is 0.30 g` · 48/48 promptta** | 4,4 ↔ 2,2 m/s² + S34 sıfır-g süzülmesi — **3 🔴** |

```
yerçekimi TARİFLE yazılı  → 2 🔴   (BENI_HATIRLAMA · 48 sahne)
yerçekimi SAYIYLA yazılı  → 3 🔴   (THE_FALLING_WORLD · 48 sahne · ikinci yarım dahil)
```
⚠️ **19.09 düzeltmesi:** ikinci yarım raporları gelince sayısal yerçekiminin
avantajı KAYBOLDU — iki film, aynı sahne sayısı, 2 🔴 ↔ 3 🔴. Sayının faydası
bu ölçümle **gösterilemiyor**; `25_` §3'ün araştırma sorusu tam da budur.

### 🅑4a · SAYI VAR, ORTAMIN ADI YOK · **6 film**
SKYLIGHT (sayı 27/33, ad 3/33) · UPWARD_FALL (25/25 ↔ 2/25) · ROSE_COAT (13/13 ↔ 2/13) ·
COLD_WELD (15/15 ↔ 0/15) · MIRROR_FAUNA (15/15 ↔ 3/15) · PAYLOAD (15/24 ↔ 2/24).
Sayı tek başına yetmiyor: motor **hangi ortamda** uygulayacağını bilmiyor.

### 🅑4b · İKİ YERÇEKİMİ REJİMİ AYNI KADRAJDA · **6 film** [D200]
LOOK_UP 2 🔴 · KEPT_LIGHT 1 🔴 · GREEN_CEILING 2 🔴 · PAYLOAD 3 🔴 ·
SKYLIGHT 3 🟠 · LEANING_ROOM 2 🔴. ⛔ Giriyorsa **ayıran işaret** (manyetik bot ·
tutamak · kemer) kadrajda ve promptta olmak zorundadır.

## 🅑5 · EFOR CÜMLESİ YOK YA DA ŞİDDETİ SAYISIZ · **29 film kısmi** ⭐ en kalabalık bulgu kaynağı

⑧ EFOR merceği tek başına **99 bulgu** yazdı. İki ayrı kusur:

```
🅑 cümle HİÇ YOK        RESONANT_STRAND 8 · KRONOS 11 · SHATTERED 5 · AMBER 4 ·
                        SILENT_PERIHELION 2 · TETHERED 3 · DRY_ANCHOR 4
🅐 cümle VAR, SAYI YOK  SUSMAYAN 9 · COUNTED_TURN 6 · STANDING_WIRE 7 ·
                        LOCKED_PULSE 9 · FALLING_WORLD 5 · STILL_SWARM 3
```

⭐ **`prompt_kontrol.py` ⑳ kapısının ölçülmüş sınırı:** kapı cümlenin VARLIĞINI
sayıyor, ŞİDDETİNİ ölçmüyor. `his forearm tightens` yazmak kapıdan geçiriyor,
ekranda hiçbir şey değiştirmiyor.

**Yazım kuralı:** efor cümlesi **oran düşüşü** taşır —
`the lever moves 4 cm in the first second and 1 cm in the last`.

## 🅑6 · PROMPTUN KENDİ KELİMESİ KADRAJA YAZI OLARAK BASILIYOR · **4 film · 7 bulgu** ⭐⭐ KAPIYA DÖNER

| film | promptta | ekranda |
|---|---|---|
| THE_PAYLOAD | `PHASE 1` (durum merdiveni etiketi, 3 promptta) | **göğüs plakasına basıldı** 🔴 |
| THE_PAYLOAD | `EVA` (teknik kısaltma, 10 promptta) | **sırta basıldı** 🔴 |
| THE_ROSE_COAT | `rose` (renk adı, **139 kez**) | **ekrana yazıldı** 🔴 ×2 |
| **THE_SOLAR_MIRROR** 🆕 | **`S04` — SAHNE ETİKETİ** | **hava kilidi gövdesine stencil olarak basıldı** 🟠 ×2 |
| **THE_CRACKED_HELMET** 🆕 | `ORION` (büyük harfli ad) | **göğüs kutusuna yazıldı** 🟠 |

⭐ **19.09 genişletmesi bu sınıfın öngörüsünü doğruladı:** kılavuz §6 `S07` ve `R3`
gibi sahne/referans etiketlerini **varsayımsal** örnek olarak yasaklamıştı;
THE_SOLAR_MIRROR'da `S04` gerçekten kadraja basıldı. Öngörü ölçüldü.

Mekanizma tek: **promptta çok tekrarlanan, kısa ve ayırt edici bir kelime** →
motor onu bir yazı sanıyor. Metin yasağının 12/13 · 21/24 oranında yazılı olması
kurtarmıyor.

⭐ Ders THE_PAYLOAD'ın **kendi dosyasında zaten kayıtlı** ("o etiket ölçüldü:
model onu giysinin göğsüne BASTI") ve yazım standardına dönmediği için ikinci
(EVA) ve üçüncü (rose) kez tekrarladı.

**Yazım kuralı:** prompt gövdesinde BÜYÜK HARFLİ kısa jeton (`PHASE 1` · `EVA` ·
`S07` · `R3`) yazılmaz; ayırt edici kelime her geçtiği yerde bir nesneye bağlanır.
⛔ **Kapı adayı — bkz. `04_KAPI_ONERILERI.md` §K1.**

## 🅑7 · METİN YASAĞI EKRANLI TASARIMLA ÇELİŞİYOR · **6 film · 8 🔴**

KRONOS (saat okunacak, `no text` yazılı) · MARS (79 ekran/monitör, mutlak yasak,
4 🔴) · AMBER_LATTICE (tarayıcı ekranı, içi boş) · MIRROR_FAUNA (parlayan vizör
HUD'u, içi boş) · TETHERED_MASS · SILENT_PERIHELION.

Prompt aynı anda hem ekran istiyor hem yazı yasaklıyor; motor bulanık harfle
dolduruyor. **Yazım kuralı:** sayaç **metinsiz** çözülür (D50/D78 — ışıklı çubuk,
dolu yuva) ya da yasak o sahnede kalkar ve metin kadrajda meşru sayılır.
İkisi aynı promptta duramaz.

## 🅑8 · DÜNYA ÇAPASI YOK — GÖK VE UFUK SAHNE SAHNE DEĞİŞİYOR · **8 film** [D209]

LEANING_ROOM **3 🔴** (Satürn → Jüpiter → tutulma halkası) ·
AMBER_LATTICE 4 (gece/gündüz üç kez) · SILENT_PERIHELION 2 · MARS 2 ·
SKYLIGHT 2 · UPWARD_FALL 2 · SHATTERED_BREATH 1 · HARD_DOCK 1.

**Yazım kuralı:** dünya cümlesi (gök · ufuk · ışık kaynağı) film başına bir kez
yazılır ve **her dış sahneye birebir** girer.

## 🅑9 · PARÇACIK CÜMLESİ FİLMİN ANA MALZEMESİNDE EKSİK · **5 film hiç · 18 kısmi**

⭐ Örüntü: **filmin novumu neyse, o kilitsiz.**
STILL_SWARM (yüzen panel filmi, parçacık 2/14 → 6 bulgu · 2 🔴) ·
RESONANT_STRAND (yüzen levha filmi, 0/14 → 4 bulgu) ·
STANDING_WIRE (tel filmi, telin kalınlığı sayısız) ·
UPWARD_FALL (ivme filmi, ivme değişimi yazısız) ·
HARD_DOCK (kenetlenme filmi, kenetlenme anı perdeleniyor).

**Yazım kuralı:** filmin **taşıyıcı olgusu** negatif çekirdekle yetinmez;
pozitif gövdede sayıyla da yazılır.

## 🅑10 · SAYILABİLİR NESNE RAKAMLA YAZILMIYOR · **5 film** [D78 · D151 · D138]

PAYLOAD (15 sandık → 8) · HEALING_GROUND (4 sarı bant → 1 → 0) ·
HARD_DOCK (8 cıvata → 10) · LOSS_OF_LIFT (12 nozul → 6 silindir) ·
BENI_HATIRLAMA (eşarp 1,2 m ↔ tüm gövde).

**Yazım kuralı:** kadrajda sayılabilen her tekrar eden öge **rakamla** yazılır.

## 🅑11 · ARKA PLAN ENVANTERİ KURULUMLA BİRLİKTE DÖNMÜYOR · **6 film**

LOCKED_PULSE 3 · KEPT_LIGHT 5 · SKYLIGHT 2 · PAYLOAD 2 · UPWARD_FALL 1 ·
HEALING_GROUND 1. Kamera aynı duvara iki kez bakıyor, iki farklı duvar görüyor.

**Yazım kuralı:** aynı kurulum harfine dönen sahne **aynı arka plan cümlesini
birebir** taşır — model iskeleti görmez, metni görür.

## 🅑12 · AKSİYONUN HEDEFİ VE İZİ KADRAJ DIŞINDA · **6 film** [D213]

RESONANT_STRAND 4 (atış var, hedef yok, iz yok) · AMBER_LATTICE 2 ·
COUNTED_TURN 2 · DRY_ANCHOR 1 (çekiç izsiz) · HARD_DOCK 1 · LOOK_UP 1.

## 🅑13 · IŞIK TAKVİMİ VE ANAHTAR IŞIK YÖNÜ YAZILMIYOR · **4 film** [D193]

BENT_GRASS 3 (anahtar ışık üç geçişte kayboldu, bir kez taraf değiştirdi) ·
MIRROR_FAUNA 3 (kask içinde kaynaksız kırmızı) · BORROWED_WEIGHT 1 (gündüz → gece) ·
FALLING_WORLD 1 (gölge 80°, halka tam karşıda).

**Yazım kuralı:** ışık yönü **saat yönüyle** yazılır (`one hard sun out of frame
at 9 o'clock`) ve takvim monotoniktir.

## 🅑14 · SES İLE GÖRÜNTÜ ARASINDA ZAMAN/SAYI KÖPRÜSÜ YOK · **5 film**

LOCKED_PULSE (replik "dört tur" diyor, kadrajda 0,21 tur) · LEANING_ROOM 2
(ses yanlış anda) · BORROWED_WEIGHT 3 (aynı ses örneği iki kez · oda tonu sıfıra
düşüyor) · KEPT_LIGHT 3 (hacim değişiminin ses karşılığı yok) · STANDING_WIRE 1.

## 🅑15 · CANLI ANATOMİSİ · **4 film**

BENT_GRASS (arka plan canlısı beş bacaklı — cümle YOK) ·
BENI_HATIRLAMA 2 🔴 (altı bacak çıktı — **cümle VAR**: `creature keeps the same
number of legs … no extra limbs`, 34 promptta) · LOOK_UP 3 🔴 (canlı uzuvları
insana geçiyor — temas cümlesi yalnız EL için yazılmış) · UPWARD_FALL 1.

**Yazım kuralı:** canlı içeren filmde temas cümlesi **iki yönlüdür** (elden
yüzeye VE canlıdan gövdeye); anatomi metinle tutmuyor → **referans paneli** [D168].

---

# 🅐 KİLİT YAZILIYDI, TUTMADI — yazım işi OLMAYAN sınıflar

⛔ Bu bölüm **prompt düzeltilerek kapanmaz.** Kapanma yeri her satırda yazılı.

## 🅐1 · VAKUMDA SES · **6 film · 12 🔴** ⭐ ölçülmüş tavan

```
AUDIO satırı HİÇ YOK  (KRONOS)    → 4 🔴
AUDIO satırı TAM      (SUSMAYAN)  → 4 🔴
```
SUSMAYAN'ın satırları: `no exterior sound at all, the hull parts in silence` ·
`the pod separates in silence`. Bundan net yazılamaz.

**Kapanma yeri:** ⛔ KURGU. Master ihraç edildikten sonra dış ses kanalı ölçülür
ve gerekiyorsa susturulur. Prompt tarafında yapılacak iş bitti.

## 🅐2 · TEMAS FÜZYONU — CÜMLE VARKEN DE OLUYOR · **7 film · 20+ 🔴** ⭐⭐

| film | temas cümlesi | sonuç |
|---|:--:|---|
| THE_COUNTED_TURN | 22/25 | **7 🔴** (kayış ve karabina filmi) |
| THE_DRY_ANCHOR | 14/14 | **6 🔴** |
| BENI_HATIRLAMA | 48/48 | 4 (2 🔴) |
| THE_LEANING_ROOM | 12/12 | 3 (1 🔴) |
| THE_LOCKED_PULSE | 24/25 | 3 |
| THE_STILL_SWARM | 14/14 | 2 |
| THE_FALLING_WORLD | 46/48 | 2 |

**Kapanma yeri:** ⛔ KADRAJ KARARI. Temas anı perdelenir · eldivenle nesne arasına
görünür bir ara katman (halka · sap kılıfı) konur · ya da temasın öncesi ve
sonrası gösterilip anı atlanır. **Cümle yazmak ölçüldü ve yetmiyor.**

## 🅐3 · FİLİGRAN VE KÖŞE ARTEFAKTI · **5 film** [D150 · D215]

KRONOS (S25, 24 karenin hepsinde) · FROST_LINE (S00 · S22, mavi üçgen) ·
BENI_HATIRLAMA (S20) · SHATTERED_BREATH (S11) · STANDING_WIRE (S16, dikey çizgi).
`no watermark` beş filmde de **hemen hemen her promptta** yazılı.

**Kapanma yeri:** ⛔ ARAÇ AYARI + YENİDEN İHRAÇ. Promptta yapılacak hiçbir şey yok.

## 🅐4 · BLOOM — TARİF KİLİDİ · **çok film**

`no bloom` (tarif) tutmuyor; `0% bloom, no glow, no soft focus, every surface keeps
visible texture` (sayısal + sonuç) **daha iyi tutuyor ama sıfırlamıyor**:
SUSMAYAN 96/96'da yazılı ve 3 bloom bulgusu çıktı.

## 🅐5 · DURUM MERDİVENİ METİNLE TUTMUYOR · **3 film**

FROST_LINE (PHASE 1-4 kusursuz yazılı → 6 bulgu) · BENI_HATIRLAMA (canlı bacak
sayısı yazılı → 2 🔴) · BORROWED_WEIGHT (taşıyıcı nesne dört kez biçim değiştirdi).

**Kapanma yeri:** ⛔ REFERANS PANELİ [D168]. Varlığın iki durumu PANEL olarak
kilitlenir; metin bu işi yapmıyor.

---

# 🅒 BULGU DÜŞER — mercek tarafındaki kusurlar · 29 bulgu

## 🅒1 · SPEC OKUNMADAN KOŞAN MERCEK · **THE_FALLING_WORLD 5 bulgu** ⭐

Mercek ince atmosferi **vakum** sandı (`atmospheric vacuum` yazdı), 0,30 g'yi
"floaty" kusuru sandı, **opak vizörlü** filmde "flinching" aradı.
⛔ `qa-isle` §2 zaten SPEC'i zorunlu kılıyor; raporun `INPUTS:` satırında yoktu.

## 🅒2 · BAŞLIK/KAPAK KARTINI ① MERCEĞİNE BULGU YAZMAK · **4 film · 7 🔴**

STANDING_WIRE 2 🔴 (`"THE STANDING WIRE" text baked onto screen`) ·
BENT_GRASS 2 🔴 · LOOK_UP 1 🔴 · RESONANT_STRAND 2.
Tipografi **post-prodüksiyondadır**; ① KARE'nin kapsamı değildir.
⚠️ Ama kartın **son sahnenin yerine geçmesi** ④ KURGU'nun işidir ve oraya gider.

## 🅒3 · TASARIM KARARINI KUSUR SAYMAK · **4 film**

BENI_HATIRLAMA (saydam ikinci figür = novum) · SUSMAYAN (gövdeden iletilen ses =
doğru fizik) · FROST_LINE (berrak vizör yansıması) · TETHERED_MASS (belirsizlik
olayın kendisi). ⛔ ⑩ ÖNERME KAPISI her mercekte koşar.

---

# ⬜ ADAY — tek filmde görüldü, ders değil [kontrat §4]

| aday | film | not |
|---|---|---|
| ADAY-A · ağız kadrajda + replik → lip-sync | THE_HEALING_GROUND | bedenleştirme kurulum sahnesinde harcanmış |
| ADAY-B · aynı ses örneği iki kez | THE_BORROWED_WEIGHT | prozodi matematiksel olarak aynı |
| ADAY-C · kask içi ışığın kaynağı yazılmamış | THE_MIRROR_FAUNA | motor kırmızı uyarı ışığı uydurdu |
| ADAY-D · replik bir SAYI söylüyor, prompt söylemiyor | THE_LOCKED_PULSE | "dört tur" ↔ 0,21 tur |

---

# 🎯 ÜÇ CÜMLE

```
1. BULGULARIN %54'Ü PROMPTTA ÖNLENEBİLİRDİ — ve büyük kısmı çekirdeğin
   SEÇMELİ uygulanmasından: cümle filmde var, bulgunun düştüğü sahnede yok.
2. ÜÇ SINIF PROMPTLA KAPANMIYOR VE ARTIK ÖLÇÜLDÜ: vakumda ses (kurgu),
   temas füzyonu (kadraj), filigran (araç). Bunlara prompt cilası çekmek boşa emek.
3. TEK YENİ MEKANİZMA: promptun kendi kelimesi kadraja yazı olarak basılıyor
   (PHASE 1 · EVA · rose). İki filmde dört 🔴 ve makine kapısına dönebilir.
```
