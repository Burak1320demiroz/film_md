# 🔎 06 — KAPI DENETİMİ (akış adım 10 · 13.09.2026)

> Üç kapı, üç çıktı, tek dosya: ① `prompt_kontrol.py` klasör modu · ② `PROMPT_QA_CRITIQUE_PROMPT.md`
> rubriği · ②b `DIALOGUE_CRITIQUE_PROMPT.md` rubriği · ③ `03_PLAN_ONCESI_KONTROL_LISTESI.md` 17 maddesi.
> Sayılar betikten kopyalandı, elle yazılmadı. Özeti `THE_LOCKED_PULSE_PLAN.md` §DENETİM KAYDI taşır.
> ⛔ Bu dosyada sahne başlığı ve prompt başlığı YOKTUR (kapı betiği 00_ANALIZ'i atlar; kural yine de geçerli).

---

## ① prompt_kontrol.py — KLASÖR MODU

```
KOMUT:   python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_4_dk_filmler/THE_LOCKED_PULSE
ÇIKIŞ:   1 (FIX)  ·  📁 FİLM KLASÖRÜ · 2 bölüm dosyası birleşik · 50 prompt  ·  ✅ GO (klasör)  ·  ✅ GO (REFERANS_PAKETI)
TOPLAM:  3 dosya + 1 film klasörü (birleşik) · ⛔ 0 BLOCK · ⚠️ 2 FIX · ✅ 2 GO
FIX'LER (ikisi de bölüm dosyası seviyesi, D74 kaydı PLAN'da):
  · video uzunluğu 3,2-3,8k (bant 2,0-2,6k · tavan 4,3k altı)              → PLAN D74 ①
  · image uzunluğu 3,6-4,4k ("bant depodaki hiçbir filmle uyuşmuyor; karar bekliyor" — betiğin kendi notu; bulgu değil)
  · dosya-modu artefaktları: iskelet 25 harf ↔ dosyada 13/12 video · NOVUM TAŞIYICISI satırı PLAN'da ·
    "kurulum sayısı 8 — 12 sahnede üst bant 6" (BOLUM_2 tek başına)      → klasör modunda birleşik GO; PLAN D74 ⑩
ÖNCEKİ KOŞUDA KAPANANLAR (bu turda 0): dönüş işareti 8 sahne · "through the glove" (S20) · çapasız "toward" (S19) ·
  ⑳ efor/gövde tepkisi (S1 "leaning into" → "leans into … shoulders drop"; sözlük `leans? into` biçimini arıyor)
```

---

## ② PROMPT_QA_CRITIQUE — betiğin göremediği tek şey

```
PROMPT QA — THE_LOCKED_PULSE · 25 sahne / 50 prompt            tarih: 13.09.2026
BETİK KARARI: GO (klasör) · FIX (bölüm dosyaları, D74 kayıtlı)

KARAR: FIX  → iki bilinçli sapma PLAN'a yazıldı (3c · S20 ve S22); BLOCK yok
```

### 1. KİLİT TABLOSU — SAYI mı TARİF mi

| kilit | promptta yazan hâli | SAYI/TARİF | not |
|---|---|---|---|
| yerçekimi | "the pull here is about a quarter / four tenths / half / three quarters of Earth's weight / full Earth weight" + "the wrench reaches the deck from chest height in well under a second" · S15 "in less than half a second" | SAYI | sahne başına tek g (D200) |
| novum sapması | "a palm's width to the LEFT of the point where it left the glove" (S2) · "a little to screen-left" (S15) | SAYI (avuç = birim) | yön TEK, SOL 2/2 |
| kayış hızı | "one full swing in four seconds" (S0) · "one full swing in two seconds — twice as fast as at the start" (S21/S24) | SAYI | ⑥ ± %25 |
| alarm | "once every two seconds / twice every three seconds / once every second" | SAYI | D193 monotonik |
| lamba dizisi | "seven round lamps … six lit white, the last one on the right dark" → S23 "all seven lit" | SAYI (metinsiz sayaç, D50) | KART 5 |
| insan | "Exactly one human figure — this film has exactly one human total" · S13 "Human count: zero" | SAYI | 25/25 |
| jet | "a thin white vapour jet, a hand-span long" → "half a hand-span" → yok | SAYI | 3 sahne |
| kilit tıkı | "closes over the wrist ring with a single hard click; no slow closing, no second click" (S12 4,0 s) | SAYI (1 tık) | — |
| bilek mührü | "the ring parts with a single click" (S22 5,0 s) · "the hand comes out of the glove in one draw" | SAYI | ARA DURUM YASAĞI |
| yıldız (S13) | "the stars cross the frame in about three seconds, one direction" | SAYI | 24 °/s |
| tempo zarfı | "slowly" ×14 (S3 S7 S8 S10 S11 S12 S16 S17 S19 S20 S22 S23) | TARİF DEĞİL — her biri zaman damgalı bir aralığa bağlı ("2.0s → 8.0s a quarter of a turn") | bulgu yok |
| "the bar is heavy" (S6) | "his right shoulder drops a little under it" ile eşli | TARİF + gövde tepkisi | ⑳ sözlüğü tutuyor |

TARİF KİLİDİ: **0** (üç ve üzeri → BLOCK eşiği uzak).

### 2. TETİKLENEN DERSLER

| sahnede var | aranan kilit | durum |
|---|---|---|
| kask / vizör (24 sahne) | kask takvimi KAPALI 25/25 + D79 iki cümlesi (pane clear/zero tint · face readable) | ✅ CHAR bloğunda 24/24 imaj + CHAR_LOCK 24/24 video, bayt-aynı |
| ekran / sayaç (lamba dizisi) | metinsiz kanal | ✅ 7 yuva, 6+1 → 7 (KART 5 · D50) |
| ikinci figür | insan sayısı kilidi | ✅ "exactly one human total"; kriyo kapsülleri kadraj dışı |
| parçacık (buhar jeti) | sayılı ve yerel | ✅ "a hand-span long", düz koni, girdap 0 |
| diyalog (6 MAKİNE) | konuşan ekranda mı · dudak | ✅ 6/6 kadraj dışı hoparlör/telsiz; "his lips stay closed behind the pane" |
| sıfır-g (S13 dış) | mikro hareket | ✅ insansız; yalnız yıldız kayar (24 °/s), yapı sabit |
| su/sıvı · canlı · biniş/iniş · ayna | — | yok (jet buhar, sıvı teması 0; pane "zero reflection") |

🔴 tetikleyici kilitsiz: **0**.

### 3. A1 — yasak ↔ anlatım (anlam düzeyi)

```
DRAMATİK BİLGİ:  halka hızlanıyor, her şey ağırlaşıyor; makine altı kapsülü sayıyor, yedinciyi bekliyor
KANAL:           kayış periyodu (4,0 → 2,0 s) · anahtar/levye SOL sapması · alarm periyodu · lamba dizisi 6+1 → 7 · anons SESİ (sayılar seste)
METİN KANALI:    0 — "no readable text" yasağı hiçbir anlatım cümlesiyle çelişmiyor ("reads" yalnız "reads heavy in the glove")
```

### 3b. politika maliyeti (betik ⑯ temiz; yorum)

```
NEGATIVE bloğunda yasak için yazılmış şiddet/tehlike kelimesi: 0 (gore/blood/wound/injury/corpse/body/victim/weapon 0 geçiş)
insan kütlesi: yok · şiddetli fiil: yok ("closes over", "parts with a click", "draws back") · sınırlama tarif olarak: "the wheel stays where it is"
TOPLAM İZLENİM (bilmeyen biri okusa): "basınç giysili bir adam bir çarkı çeviriyor, kolunu bir yakaya sokuyor, sonra eldivenini orada bırakıp oturuyor"
```

### 3c. KOMPOZİSYON YÜZEYİ — insan gözünün işi ⭐

| soru | sahne | cevap | karar |
|---|---|---|---|
| yüz YOK + uzuv KONU + tepeden/makro üçü birden | **S20** (M · 100mm ECU · 0,6 m · h 0,30) | ① yüz yok ② sol el konu ③ MAKRO — **üçü var**; ama kamera NESNE HİZASINDA ("level with the wheel"), tek el, ikinci ön kol 0, kayış/bant 0, yüz kadraj dışı olduğu için değil kadraj küçük olduğu için | ⚠️ bilinçli sapma → PLAN D74 ⑪ · İKİ YENİLGİ: 2 red → S20 kurulum J'den (S19 kadrajı) üretilir |
| aynı üçlü | S12 · S14 (D · 75mm CU · yandan · h 0,75) | ① yüz yok ② bilek konu ③ TEPEDEN DEĞİL (yandan, yaka hizası), makro değil (CU insert) — 2/3 | ✅ vaka 13 çözümü uygulanmış (PLAN politika) |
| bedenden BİR ŞEY ÇIKARILIYOR mu | **S22** (bilek halkası açılır, çıplak el eldivenden çıkar) | EVET — filmin BEDELİ bu eylemdir, "zaten çıkmış" hâle alınamaz (alınırsa bedel sahne arasına düşer, B1 ihlali). Uygulanan: "çıkarma" fiili 0 ("the hand comes out of the glove in one draw", "the glove stays seated"), kask/yüz kadrajda (C ¾ profil, yüz okunur), eldiven nesne olarak kalır, ARA DURUM YASAĞI | ⚠️ bilinçli sapma → PLAN D74 ⑫ · 2 red → S22 imajı 5,0 s SONRASI kareyle açılır (halka açık, el yarı çıkmış DEĞİL: el çıkmış, göğüste) ve bedel S21 sonu/S22 başı sınırına taşınır — o gün URETIM_DEFTERI + 09_RED_DEFTERI satırı |
| insan kütlesi + kaçan tek kişi | — | yok | — |
| konuşan yüz + kapital kimlik + tehlike çerçevesi | — | konuşan yüz 0; kimlik düz cümle; tehlike çerçevesi 0 | — |

### 4. SELF-CONTAINED

```
kimlik bloğu (CHAR) 24 imaj promptunda + RK1 + KAPAK + PLAN bayt-aynı (S13 insansız); 24 video promptu kısa kilidi (CHAR_LOCK) bayt-aynı taşır · CAM cümleleri kurulum başına bayt-aynı + dönüş işareti ("— the same position, height and lens as Scene N.")
film dışı atıf: "as Scene N" yalnız dönüş işareti biçiminde (ACI_YAYI §7 ⑥ istenen biçim); "as before" 0 · "Bible" 0 · film adı 0 · karakter adı 0
```

### 5. ÇEKİM TARİF EDİLMİŞ Mİ

```
zaman damgası: 50/50 video promptunda 0.0s → 10.0s "hold" ile kapanıyor · ölü saniye: S18 2,8-10,0 "hold" (tasarım: dinleyen beden, anons sürüyor)
tek çekim + lockoff: cümle başı ve sonu 50/50 · doruk S20 4,0-6,0 s klip İÇİNDE · bedel S22 5,0-7,0 s klip İÇİNDE · tohum ödemesi S23 4,0 s klip İÇİNDE
```

### 6. AÇI ↔ VURUŞ

| sahne | vuruş | açı | KAMERA_ACISI §3 karşılığı | uyum |
|---|---|---|---|---|
| S9 | tehditle yüzleşme (leak persists) | H alçak, 15° yukarı, 24mm WS | alt açı, bel-diz | ✅ |
| S11 · S15 · S16 | mutlak yenilgi (yük · levye düşer · gövde çöker) | G üst, 35° aşağı, 50mm MCU | üst açı, tavan yüksekliği | ✅ (35° — ideal 15-30° dışı, ölü bölge 45-60° dışı; betik ⑫ eşiği 45 → geçti; PLAN D74 ⑬) |
| S17 · S19 | sistem çöküşü (frene bakış) | J dutch 15°, 35mm MS | eğik 15-20° | ✅ |
| S20 | doruk (el durur) | M ECU 100mm | — (en yüksek iç sıçrama: 3 kademe + 60° + dutch→düz) | ✅ D74 ③ |
| S22 | epifani/bedel | C ¾ profil 35mm MS (S10 dönüşü) | göz hizası tam profil 50mm | ⚠️ bilinçli: yumruğun girdiği kadrajdan el çıkar (kafiye S10↔S22); PLAN D74 ⑭ |
| S13 | hiçlik | X hub'dan EWS | tepe/XLS | ✅ |
| S0 ↔ S24 | açılış/kapanış | A eye WS | kafiye çifti | ✅ |
ardışık çiftler ≥1 kademe + ≥45°: 21/21 (03 §3 tablosu, nihai azimutlar) · şok 2/2 (S12→S13, S13→S14) · sözlük: "low angle / high angle / Dutch angle (tilted exactly 15 degrees) / over-the-shoulder" biçiminde · sabitlik cümle başı+sonu · hareket süngeri: kayış salınımı (A/C/J), alarm nabzı (her iç sahne), jet (S3-S10)

### BULGULAR (alıntılı) → hepsi PLAN D74'e yazıldı

```
1. S20 CAMERA "100mm macro lens … 0.6 m from the small wheel, camera height 0.30 m, level with the wheel, extreme close-up insert"
   → 3c üçlü (yüz yok · el konu · makro) · YERÇEKİMİ F1 S8 emsali · uygulanan: nesne hizası, tek el, bant/kayış 0 · fallback J
2. S22 TIMELINE "the ring parts with a single click. 5.0s to 7.0s — the bare right hand comes out of the glove in one draw"
   → 3c "bedenden bir şey çıkarılıyor" · COLD BURN S28 emsali · uygulanan: çıkarma fiili 0, eldiven yerinde, yüz kadrajda · fallback 5,0 s sonrası imaj
3. G "high angle pitched down 35 degrees" → KAMERA_ACISI §5 ideal bandın 5° üstü (ölü bölge değil) · gerekçe: 2,20 m tavan altı, yaka+sırt aynı kadrajda 30° ile sığmıyor
4. S22 kurulum C (¾ profil 35mm) ↔ §3 epifani "tam profil 50mm" → kafiye kararı (S10 dönüşü)
AÇIK SORU: 0
```

---

## ②b DIALOGUE_CRITIQUE — 6 MAKİNE repliği

```
INPUT MODE: FULL   (A omurga: PLAN §B5 · B tablo: PLAN §REPLİK TABLOSU, İŞLEV sütunlu · C: BOLUM_1/2 tırnaklı satırlar)
LINES FOUND: 6 in prompts · 6 in table   (her replik promptta iki kez geçer — TIMELINE + AUDIO — aynı satır; uyuşmazlık yok)
```

### DIALOGUE LEDGER

| # | sahne | saniye | konuşan | register | replik | kelime | claimed | observed | etiketler |
|---|---|---|---|---|---|---|---|---|---|
| 1 | S1 | 11,0 | tavan hoparlörü | MACHINE | "Coolant pressure has dropped. Ring spin increasing to two and a half revolutions." | 13 | ENGEL | OBSTACLE + TURN (engelin ilk ısırığı: sebep → makinenin cevabı) | FUNCTIONAL · SUBTEXT · FIT · DISTINCT · SPEAKABLE · FIRST-LINE ✓ |
| 2 | S6 | 61,0 | tavan hoparlörü | MACHINE | "Ring at three revolutions. Six pods stable." | 7 | İSTEK/MUHATAP | WITNESS (bahis adlandırılır: "six pods" — lamba dizisi 6+1 anlam kazanır) | FUNCTIONAL · FIT · SPEAKABLE |
| 3 | S9 | 92,0 | tavan hoparlörü | MACHINE | "Leak persists. Ring spin increasing to three and a half revolutions." | 10 | ENGEL | OBSTACLE + TURN (çark yetmedi → yöntem değişir, S10 yumruk) | FUNCTIONAL · FIT · SPEAKABLE |
| 4 | S12 | 125,0 | tavan hoparlörü | MACHINE | "Port collar latch engaged." | 4 | ENGEL→tema | TURN (orta nokta yenilgisi; makine bileği PARÇA olarak kaydeder) | FUNCTIONAL · SUBTEXT · FIT · SPEAKABLE |
| 5 | S13 | 132,0 | telsiz (dış, insansız) | MACHINE | "Ring at four revolutions. Maximum spin. Six pods stable." | 9 | MUHATAP | WITNESS + OBSTACLE tavanı ("maximum" = tırmanış bitti, bedel sabitlendi) | FUNCTIONAL · FIT · SPEAKABLE · protokol tekrarı ("six pods stable" #2'den) |
| 6 | S18 | 181,0 | tavan hoparlörü | MACHINE | "Loop pressure holding. Spin hold at four revolutions." | 8 | KAYIP | TURN (hız GERİ İNMEYECEK → bilek kilitli kalır → S20 bir tepki değil SEÇİM olur) | FUNCTIONAL · FIT · SPEAKABLE · SON REPLİK |

### FINDINGS BY TEST

```
T1 FUNCTION      silme testi 6/6: #1 silinirse halkanın neden hızlandığı yok (kayış tek başına söylemez) · #2 silinirse "six pods" hiç adlandırılmaz,
                 6+1 lamba S23'e kadar süs kalır · #3 silinirse çarkın neden bırakıldığı yok · #4 silinirse tık bir arıza sanılır, makinenin
                 KAYDI olmaz · #5 silinirse "full weight"in sözlü çapası yok · #6 silinirse S20 seçim değil bekleyiş olur. CUT: 0 · REDUNDANT: 0
                 (#5'teki "Six pods stable" tekrarı protokol nakaratıdır — makinenin defteri değişmezken beden değişiyor; rubrik "protocol
                 repetition" cezalandırmaz)
T2 ON-THE-NOSE   duygu adı 0 · niyet adı 0 · THINKING-OUT-LOUD 0 (insan konuşmuyor) — no findings
T3 EXPOSITION    #1 iki cümle = iki olgu (basınç düştü · hız artıyor): sebep + cevap tek anonsta, cümle sınırı zaten bölüyor; kadrajda rakip
                 izlenebilir eylem var (eller çarkta, omuzlar durur) → meşru teslim, OVERLOADED etiketi KAZANILMIYOR (tereddüt kaydı: rubrik
                 kural 9). AS-YOU-KNOW 0 · LECTURE 0 (kural bir dinleyene karşı değil, bir BEDENE karşı söyleniyor: omuzlar durur)
T4 VOICE         tek konuşan (makine); insanla takas testi: "Coolant pressure has dropped" insan ağzında "Pressure's dropping" olurdu — DISTINCT 6/6
T5 REGISTER      tam biçim 6/6 · kısaltma 0 · sayı/birim/sayım MAKİNEDE 6/6 · edilgen/faili yok ("latch engaged", "spin hold") · UNCLEAR 0
T6 NATURALNESS   makine İngilizcesi doğal; calque 0; "Spin hold at four revolutions" — telsiz/kontrol jargonu, ODD-COLLOCATION değil
T7 ECONOMY       en uzun #1 13 kelime ≈ 4,5 s (TTS düz okuma) — 5 s sınırının altında ama en yakını; hiçbiri klibi doldurmuyor; aynı sahnede ikinci
                 replik 0; üst üste konuşma 0. MONOLOGUE 0
T8 PLACEMENT     FIRST-LINE #1 11,0 s: 11 s sessizlikten sonra engelin ilk ısırığına düşüyor — WASTED değil · IRONY-BREAK: paket DRAMATİK İRONİ
                 penceresi ilan ediyor (boş 7. yuva + hızlanan kayış); 6 replikten hiçbiri gizli olguyu adlandırmıyor, #4 tıkı KAYDEDİYOR (2 s
                 sonra, seyircinin gördüğünü makinenin defterine yazıyor), göz kırpmıyor · EARLY-EMBODIMENT 0 (ağız 0 kare, doruk dâhil)
```

### REWRITE LIST
```
— (boş)
SUGGESTION (yalnız TTS ölçümü 5,0 s'yi aşarsa): #1 "Pressure has dropped. Ring spin increasing to two and a half revolutions." (12 kelime; "Coolant" düşer —
bilgi #3/#6'daki "leak/loop" ile zaten taşınıyor). Yazar karar verir; ölçülmeden değiştirilmez.
```
### CUT LIST — boş · SILENCE CANDIDATES — boş (S19-S24 zaten sessiz; son replik 181,0 s, ardından 68 s replik yok)

### THE THREE THAT MATTER
```
1. #6 "Loop pressure holding. Spin hold at four revolutions." — filmin menteşesi: bu satır olmadan S20 seçim değildir. Zamanı 181,0 s, omuz
   cevabı 1,5 s gecikmeli (DEĞİŞ-TOKUŞ tablosu) — kurguda bu gecikme korunur, anons klip sesinin ÜSTÜNE post'ta biner.
2. #4 "Port collar latch engaged." — dört kelimelik tez. TTS'te vurgu/ton SIFIR; "engaged" yükselen tonla okunursa alarm olur, düz okunursa kayıt.
3. #1 uzunluk — 13 kelime, 5 s sınırının en yakını; TTS ölçümü sınırı aşarsa SUGGESTION uygulanır.
```
### VERDICT
```
GO — CUT 0 · UNCLEAR 0 · MONOLOGUE 0 · doruk sahnesinde replik yok (S20 sessiz, tasarım). Residual: #1 TTS süresi ölçülür; #5 nakarat bilinçli.
```

---

## ③ 03_PLAN_ONCESI_KONTROL_LISTESI — 17 madde (TEK SAYFALIK ÖZET PLAN §DENETİM KAYDI'nda)

```
A1 ☑ "no readable text" 50/50 · ekran/gösterge İÇERİĞİ tarif edilen satır 0 (lamba dizisi yanık/sönük sayımı = D50 çözümü, ihlal değil)
A2 ☑ başlık 25 sahne = "## 🎬 SAHNE" bloğu 25 = "Scene N of 25" 50/50 (betik) · numara atlaması 0
A3 ☑ 9 s + 24 × 10 s = 249 s = 4:09 = PLAN/SPEC/YAYIN_PAKETI iddiası (KLİP SÜRESİ araçtan ölçülecek [D124]; sapınca formül yeniden koşar)
A4 ☑ tarama 25/25: biniş-iniş 0 · loş mekâna giriş 0 (S6 dolap KAPAĞI açılır, mekân değişmez; S6→S7 yürüyüş kesmede) · ayna 0 (pane
     "zero reflection", panel mat) · türetilmiş fenomen novum 0 (taşıyıcı KATI nesne: anahtar/levye) · yokluk novum 0 (sönük 7. lamba TOHUMDUR,
     novum değil) · jenerik/başlık kartı 0 (S0 0,0 s kapak = kare, kart değil). Karar satırı: "S13: dış Overview İNSANSIZ, hub/kapı/biniş 0 — D69 ①"
A5 ☑ 1 numaralı risk ADIYLA: "novum ekrana gelmiyor" (D127/D192) · POZİTİF SAYI: S2 "a palm's width to the LEFT … well under a second";
     S15 "a little to screen-left … in less than half a second"; SPEC L-listesi 0,11 m / 0,08 m · göz kapısı F1 (kare 24,0-25,0) sayıyla
B1 ☑ doruk S20 · 4,0-6,0 s klip İÇİNDE ("the fingers stop a palm's width short of the rim and hold there, open, for two seconds")
B2 ☑ seçim S20 (frenlemez) · kayıp S22 · 224,0 s (sağ eldiven yakada kalır, çıplak el) · kalıcı iz S23-S24
B3 ☑ tema satırı İNSAN-MAKİNE (§3 sekizlisi, sayaçta en az kullanılan) · novum'suz cümle: "bu film, doğru hesap yapan bir makinenin bir
     insanı parça olarak saydığı an hakkında" · motif S2 · S10 · S12 · S18 · S22 · S24 (bedel sahnesi S22 listede ✓)
B4 ☑ iskelet A B C D C E E C D H C G D X D G G J B J M A C C A (25 harf) · kurulum 10 (D74 ②) · açı tipi 6 (eye · OTS · profil · alt · üst ·
     dutch) · ardışık çift 21/21 bant içi · şok 2/2 (S12→S13 · S13→S14) · dereceler: dutch 15 ✓ · alt 15 ✓ · üst 35 (D74 ⑬) ·
     doruk sıçraması S19→S20 (3 kademe + 60° + dutch→düz) · küme 3/2 ✓ · dönüş 11/25 = %44/40 ✓ · dönüş+küme metni birebir + işaret (betik ⑩④ GO)
B5 ☑ İSTEK: sızıntı portunu kapatmak, altı kapsülü soğuk tutmak (vardiya işi; S0'da el çarkta) · ENGEL: otomasyon halkayı hızlandırır +
     yaka kilidi · BEDEL: sağ eldiven yakada kalır · S22 · 224,0 s ⭐ · MUHATAP: ☑ ortamın KALICI değişen parçası (halka 4,0 RPM'de tutulur,
     lamba 6 → 7) + ☑ kendi bedeni (tek eldiven)
B5b ☑ tek insan — AYRILIK uygulanmaz (ikinci insan kadrajda 0, seste 0)
B5c ☑ ÜRETİM SIRASI: REFERANS PAKETİ → S20 → S22 → S24 → S2 → S12 → S0 → S13 → S10 → kalanı · ilk sahne S20 (doruk) · S0'dan başlamıyor
B6 ☑ POLİTİKA SATIRI: S12 · 123,0 s (ikinci S22 · 224,0 s) · nötr tarif yazılı · KART 12 açık (bedenden bir şey çıkarma S22 · kısıtlanmış uzuv
     S12-S21) · ÖNLEM/MALİYET/TELAFİ tablosu (PLAN §POLİTİKA) · TELAFİ boş satır 0 · milliyet/kurum/kişi adı 0
C  ☑ insan 1 × 25 (S13: 0) · kask KAPALI 25/25 · ölçü R 56,0 m · koridor kesiti/raf 4 blok · 1 H = 1,90 m · yerçekimi 0,25 → 1,00 g
     sahne tablosu + düşüş süreleri · sıvı temas 0 (jet BUHAR, 3 sahne arka plan) · canlı 0
D  ☑ risk sayımı 10/14 (payda 02_RISK_KARTLARI RİSK TOPLAMI soru sayısı) → malzeme 8 kalemde azaltıldı (00_ANALIZ/02 §5)
E  ☑ QA SPEC bloğu THE_LOCKED_PULSE_QA_SPEC.md A bloğu (FILM · FORMAT · SCENE COUNT 25 · RUNTIME 249 · DIALOGUE LINES 6 (S1 S6 S9 S12 S13
     S18) · SILENT SCENES 19 · VIRAL INTERSTITIALS S4 S10 S17 S22 · PROTAGONIST · CENTRAL CHOICE S20)

İMZA: 17/17 işaretli · 13.09.2026 · bu liste işaretlenmeden üretim başlamaz — başlamadı (0 kare).
```
