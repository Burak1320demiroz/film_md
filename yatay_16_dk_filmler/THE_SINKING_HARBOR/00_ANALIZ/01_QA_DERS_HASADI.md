# 🧾 THE_SINKING_HARBOR — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu (102 ✅ satır · 8 "—").
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 217 ders ve
> 77 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 0. 🏷️ ETİKET EŞLEMESİ — hangi ders ailesi bu filme DÜŞÜYOR

```
hepsi       ✅  — 96 klibin hepsi
kask        ✅  — üç karakterin üçü de kapalı kask + BERRAK vizör (sahip künyesi)
replik      ✅  — 34 D repliği + 4 H dış sesi = 38 (deponun en replikli filmi)
iki-insan   ✅  — ÜÇ insan; kılavuz "yalnız ikinci insan varsa" diyor, üçüncüsü
                  kuralı GENİŞLETİR: istek çaprazı 3 yönlü, konum kilidi üç yerli
novum       ✅  — gezegenin derin dokusu, fiziksel yasa tipi
dış-mekân   ✅  — 38 klip dışarıda (bulut katmanı · bakım yolu · sonda başı)
ses         ✅  — ortamın ses yasası + planlı sessizlik + 38 replik
──────────────────────────────────────────────────────────────────────────
dikey       ✗  — film yatay 16:9
faz         ✗  — 16 dk §2.8 modül hattı, 7-20 dk FAZ hattı DEĞİL
vakum       ✗  — ortam yoğun bulut katmanı; §3.1'in üç sert kuralı GEÇMEZ
düşük-g     ✗  — tek g 1,00 g; D198 (0 g eksensel momentum) tetiklenemez
```

⚠️ **"vakum ✗" bu filmin en ters okunan satırıdır.** Sahip §7'de *"vakum benzeri
ince üst katmanlar"* diyor ve bu bir SES bakış açısı cümlesidir (ses gemi/giysi/
temas/telsizden gelir), bir ORTAM KARTI beyanı değil. Gölge, dolgu, toz, egzoz ve
rüzgâr satırlarında §3.1 **geçersizdir**; geçerli kart §3.6'dır (sürekli bulut).

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D56** ⭐ | THE_DEEP_PRESSURE: bir GAZ DEVİ filminde ekranda okyanus çıktı — kabarcık, tüp, mercan, denizaltı. Tetikleyici promptun kendi kelimeleri (`dive` · `deep` · `current` · `floating`) | **MEDIUM LOCK:** ortam maddesi her dış klipte fizikle kilitlenir — *a dense hydrogen-helium cloud layer, not water*; su negatifi (`no water, no ocean, no bubbles, no waves, no buoyancy, no splash`) sahneye özel cümle olarak girer; yasak sözlük §1c tablosunda | 38 dış klibin hepsi (S02-S03 · S06 · S11 · S15-S22 · S24) + pencere klipleri (K15 · K29 · K80) |
| **D200** | 6 film TWO GRAVITIES; iki yerçekimi aynı kadrajda | **TEK g = 1,00 g**, 92/92 promptta BİREBİR aynı PHYSICS cümlesi; bırakılan her nesne saniyeli düşüş satırı taşır (kopan döşeme K65 · pim K82 · kriko K74) | 92/92 |
| **D206** ⭐⭐ | T8 EFOR deponun en düşük ekseni: 0,0 · 1,0 · 1,4 · 2,7 · 2,9 — `NOBODY PAYS` | Her efor klibinde **≥1 ÖDEME satırı, saniyeli**: `4,0 s — his right forearm locks and the crank stops for half a second`; kanal ELDİVENİN ÜSTÜNDE okunur [D175] | 31 efor klibi: K13 · K17-K19 · K23 · K25 · K28 · K49-K52 · K56-K59 · K62 · K65-K67 · K70 · K72 · K74-K77 · K81-K82 · K86-K88 |
| **D214** | 3 film + 1 ölçüm: kadrajda olmayan beden tarif edildi, model onu kadraja soktu | `IN FRAME:` ilk satır 96/96; SUBJECT yalnız kadrajdakini yazar — 23 insert klibinde yüz cümlesi YOK | 96/96 |
| **D157** | novumun taşıyıcısı TEK KARE testini kendisi geçmiyordu; iki mercek onu "tekrar" sayıp kesme listesine yazdı | TEK KARE cümlesi taşıyıcıyı ADLANDIRIR: *the dark fold drawn tight over the probe's pale metal collar*; taşıyıcı kadrajın ≥1/10'u ve değişim TEK KLİP içinde | K34 (kurulum) · K38 (doğrulama) · K79 (sonuç) |
| **D217** | 2 film: replik ekrandakini söylüyor | Replik tablosunun İŞLEV hücresi görünmeyeni taşır; 9 riskli replik ölçüldü ve plan KANON olduğu için silinmedi — ölçüm `04_UYARI` §2 | 38 replik klibi |
| **D209** | 8 film: dünya çapası yok, gök sahne sahne değişti | §3.6 UYARLANMIŞ ÜÇLÜ: ① üstte kaynaksız parlak kubbe ② altta derinlik, **ufuk ÇİZGİSİ YOK** ③ yer imi = liman kaburgasının kendisi — üçü dış kliplerde BİREBİR | 38 dış klip |
| **D210** ⭐ | T9 kafiye sütunu 2 · 2 · 4 · 5 — neredeyse evrensel RHYME BROKEN | İskeletin ilk ve son harfi AYNI: **K05 ↔ K96** kokpit kurulumu, CAMERA satırı birebir; her video TIMELINE'ının son satırı `hold` | K05 · K96 + 92/92 lockoff |
| **D146** | 4 vaka, ⛔ ÇALIŞMIYOR damgalı: "seamless visor" kubbe davetiyesi | Vizör cümlesi BİÇİM + ÇERÇEVE + TEK PARLAMA [D95 üçlüsü]; `seamless/bubble/dome/sphere` 0 kez; referans paketi T1 sayfası KAPI 0 | `IN FRAME: face` taşıyan 29 klip |
| **D213** | 4 film: temas kesmeden önce, sonuç kadraj dışında | Temaslı 26 klipte ÜÇ satır (TEMAS · DEĞİŞİM · SONUÇ ≥1 s), üçü AYNI klipte; temas noktası kadrajın dış üçte-birinde DEĞİL | K09 · K10 · K18 · K19 · K58 · K59 · K66 · K70-K72 · K74-K76 · K81-K83 · K87-K88 · K92 |
| **D207** | 4 film: şok ve yorgunluk kesmede sıfırlandı | Yorgunluk 0-6 dizisi sahne tablosunda; ardışık düşüş ≤1 kademe; bir klibin SON bedeni sonraki klibin `CONTINUOUS ACTION:` satırı | 96/96 (tablo sütunu) |
| **D208** | 4 film: kimlik beş kanalda kaydı | KİMLİK DİZİSİ satırı ÜÇ karakter için AYRI: kask K 96/96 · rozet konumu · diz desteği K19+ · diz çiziği K65+ | SPEC C + 96/96 |
| **D172** ⭐ | taşıyıcıyı asan kordon filmin mekanizması sanıldı; 8 merceğin 8'i filmi başka bir film sandı | **ÜÇ SARKAN NESNE:** emniyet hattı · kriko · bırakma kolu. Üçü de NEREDE BİTTİĞİNİ yazar; erişilemeyen (ana kaburga ankrajı) için "out of reach" cümlesi | K58 · K64 · K67 · K70 · K77 · K86-K88 |
| **D179** | imaj promptu değişimin SONRASINI yazdı; bedel hiç ekrana gelmedi | BEDEL klibi K80'in imaj promptu pencerenin HENÜZ örtülmediği anı yazar; `0.0s` satırıyla kelime kelime uyumlu | K80 + bütün değişim klipleri |
| **D202** | 5 film: merkezî seçim ve bedel bedende okunmuyor | ÇAPA ÜÇLÜSÜ: SEÇİM K48 · BEDEL K80 · FİNAL K96 — BEFORE/AFTER beden çifti + saniye; dolgu jesti (yaka düzeltme) 0 | K48 · K80 · K96 |
| **D193** | 5 film: ışık takvimi ölçülmedi, şeritler klip içinde geri yandı | Güneş diski yok → takvim **TEK PARLAKLIK DİZİSİ**: kolon ışığı 6 → 5 (K26) → 4 (K44) → 2 kararsız (K69) → kısa denge (K85) → 0 (K94); monotonik, geri yanmaz | 38 dış klip + pencere klipleri |
| **D175** | D169'un kendi cümlesi mührü deldi: `through the glove` deriyi çizdirdi | Çıplak-deri negatifi ÜÇ BÖLGELİ 96/96; zorlanma ELDİVENİN ÜSTÜNDE; çizik GİYSİ YÜZEYİNE (`on the right knee plate of the suit`) | 96/96 |
| **D167** | red defteri vaka 15: yedi kimlik özniteliği = "ünlü tarifi" kalıbı, üretim durdu | Prompt gövdesinde öznitelik ≤3; boy GÖRELİ; ten/saç/yaş PLAN'da ve referans paketinde kalır | 29 yüz klibi |
| **D141** | kurgu kapısının üç satırı geçti, filmin vuruşu ekranda yoktu | FİNAL VURUŞ KANITI: K92 · 15:14 · **dört kenet AÇIK, sayılabilir 4 adet**; ikinci kanıt K94'te alan ışığı 0 | K92 · K94 |
| **D180** | 3 vaka, ⛔ ÇALIŞMIYOR: planlı sessizlik video modelinden istendi | Sessizlik BIÇAĞI kurgudadır: MUZIK'e `KURGUDA HARD MUTE` satırı 3 pencere (K40 · K79 · K96 son 2 s); prompt cümlesi YEDEK | K40 · K79 · K96 |

**TOPLAM 20 — tavan tam dolu.** Aşağıdakiler PLAN'a GİRMEZ.

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

| ders | neden bu filmde PLAN kilidi olarak yazılmadı |
|---|---|
| D1 · D34 · D45 · D42 | **Yazım standardının içinde erimiş durumda.** Tek çekim cümlesi, özel ad yasağı, etiketsiz gövde ve yıpranma konumu 92/92 promptta zaten var; ayrıca kilit satırı olmaları tavandan yer yiyor, davranışı değiştirmiyor. Kapıları betikte koşuyor (①·⑤·⑲·㉖). |
| D16 | D146 + D208 ikisi birden yüz kilidini zaten taşıyor; üçüncü satır aynı şeyi üçüncü kez söylerdi. |
| D62 · D70 · D211 · D212 | Kurgu tarafı. PLAN'ın `KESİLEMEZ LİSTESİ` ve `SAHNE HARİTASI` blokları bunları taşıyor; kilit listesi üretim tarafıdır. |
| D78 · D138 · D174 · D176 | Dört taşıyıcısı da tek bir karara indi: **alçalma sayacı pencere çerçevesine göre okunur.** O karar PLAN'ın `SAYAÇ` ve `DÜNYA ÇAPASI` bloklarında duruyor; dört ayrı kilit satırı yazmak aynı cümleyi dörde bölerdi. |
| D139 | D175'in üç bölgeli mühür cümlesiyle aynı yere düşüyor; `IN FRAME: back` klipleri pozitif sırt cümlesini §5.2 satırından alıyor. |
| D169 | D206'nın alt kümesi — D206 kanalı SAYIYLA istiyor, D169 yalnız sözlüğü veriyordu. |
| D192 | D56'ya devredildi: bu filmin 1 numaralı riski SU'dur ve pozitif biçimi D56 satırında SAYIYLA yazılı. |
| D198 · D201 | Ortam tetiklemiyor (0 g yok, güneş diski yok) — çizelgede "—". |
| D203 · D215 · D216 | SPEC ve MUZIK tarafı; `DIALOGUE LINES: 38`, üç kutu ve katman tablosu oralarda yaşıyor. |

---

## 1c. 🌊 MEDIUM LOCK SÖZLÜĞÜ — D56'nın bu filme uygulanmış hâli

> ⛔ **Bu tablo filmin 1 numaralı riskidir ve kaynağı deponun kendi ölçümüdür**
> (THE_DEEP_PRESSURE · 3,0/10 · Kostüm-Prop 1/10 = deponun en düşük kategorisi).
> Filmin ADI *SINKING*, olayı *batmak*, mekânı *bulut derinliği*, varlığı *kasılan
> doku*, hareketi *dalga*. Beş kanal da suya işaret ediyor; biri kalırsa model
> ortamın MADDESİNİ değiştirir.

| ⛔ prompta GİRMEZ | ✅ yerine yazılan |
|---|---|
| `sinks` · `sinking` | `is drawn down` · `is dragged deeper` · `loses altitude` |
| `deep` (tek başına) | `far down inside the cloud layer` · `in the lower cloud decks` |
| `dive` · `diver` · `diving` | `descent` · `descending under field control` |
| `wave` ⚠️ sahibin kendi kelimesi | `a single broad pulse travels along the lit veins` |
| `current` · `flow` | `a cloud deck moving at a different speed` |
| `floats` · `floating` · `buoyancy` | `is held at a fixed altitude by the lift field` |
| `swims` · `glides` | `is carried by the field, thrusters correcting` |
| `surface` (bulut için) | `the cloud boundary` · `the upper deck of cloud` |
| `tissue` ⚠️ politika + su | `the dark living layer` (⛔ `flesh` · `organ` · `wound` HİÇ yazılmaz) |
| `tentacle` ⚠️ MIRROR_FAUNA | `a fold of the dark layer` |

**Her dış klibin sahneye özel negatif cümlesi (§5.2'nin 3 satırından biri):**
```
No water anywhere — no ocean, no sea, no waves breaking, no bubbles, no splash,
no spray, no wet surfaces, no coral, no fish, no submarine, no scuba gear.
```

⚠️ **D123 tuzağı kontrol edildi:** yasak kelime listesi POZİTİF cümleyle birlikte
yazılır (`a dense hydrogen-helium cloud layer, not water`), yalnız negatifle değil —
yoksa yasak ismi kazandırır. Sahibin kendi `dalga` kelimesi planda KALIR (Türkçe,
prompta girmiyor); İngilizce karşılığı `pulse`tur.

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| **THE_DEEP_PRESSURE** | 🧩 MANTIK 3,0 | `Atmosphere read: Dense liquid (bubbles constantly rising)` — gaz devi atmosferi okyanus okundu; mercan, denizanası, denizaltı | §1c MEDIUM LOCK sözlüğü + 38 dış klibin sahneye özel su negatifi |
| **THE_DEEP_PRESSURE** | 🧩 Kostüm-Prop **1/10** | Bible'sız üretim: kıyafet 14 sahnenin hiçbirinde kanonik değil | Referans paketi YAZILIR (T1·T2·T3·T4·T6 doğru) ve KAPI 0 olur: onaysız sayfanın varlığı geçtiği klip üretilmez |
| **THE_DEEP_PRESSURE** | 🧩 Coğrafya 4/10 | Tekrar eden portal iki sahnede iki farklı yer [D58] | RECURRING ENTITY BIBLE 7 kart: KESTREL · liman kaburgası · D1 yuvası · sonda başı + 3 kilit · kontrol odası · bakım yolu · kriko. Geçtiği HER klipte kartın tamamı birebir |
| **LOSS_OF_LIFT** | 🧩 kilit çelişkisi 6 | `4:00'da sonda ayrılıp DÜŞÜYOR` ↔ EKRAN YÖNÜ KİLİDİ *"yükselen üst üçlükten çıkar, batan altta oturur"* | ⭐ ALÇALMA YÖNÜ KİLİDİ: batan her şey kadrajın ALT üçte-birinde oturur ve ALT kenardan çıkar; K84'te sonda **aşağı** gider, K93'te gemi **yukarı** — iki yön tek filmde ve ikisi de nesneye bağlı [D174] |
| **LOSS_OF_LIFT** | ④ kurgu kapısı | 4:10'da 5 saniyelik başlık kartı — prompt yasağı tuttu, KURGU masasında delindi (8. vaka) | `URETIM_DEFTERI` üç kutusu + kurgu kapısı ③: ekran metni 0,0 s · kapak çıktısı kurguya GİRMEZ |
| **LOSS_OF_LIFT** | ⑤ İNSAN ŞERİDİ | Plan `-111111111111-11111-1111-` ↔ rapor; **slot 19 ve 20 yer değiştirmiş** → doruk yanlış yuvada | İNSAN ŞERİDİ 96 karakter olarak SPEC C'ye yazılır (insansız klipler: K06 · K21 · K23 · K24 · K26 · K33 · K34 · K38 · K40 · K41 · K61 · K69 · K79 · K84 · K93 · K94 · K95) |
| **THE_MIRROR_FAUNA** | ① ⑪ BLOCKER | 01:52 vizör HUD içinde kırmızı alfanümerik metin | Metin yasağı KAPSAMLI (§5.1 ④) + vizör cümlesinde `no HUD, no overlay` sahneye özel satır olarak 29 yüz klibinde |
| **THE_MIRROR_FAUNA** | ① ② ⑦ ⑫ BLOCKER | 02:00 S13, S12'nin birebir KOPYASI | Vuruş sütununda ardışık tekrar 0 · aynı klip 0 kez · `sahne_kapisi.sh` klip sayısı = prompt sayısı |
| **THE_MIRROR_FAUNA** | ⑥ ⑧ BLOCKER | 01:50 düşüş 1,2 s'de 1 m → 0,14 g, kilit 0,7 g | 1,00 g'de 1 m düşüş **0,45 s**; PLAN fizik defterine düşüş tablosu, TIMELINE'a saniye |
| **THE_MIRROR_FAUNA** | ① MAJOR | 01:11 ve 02:12 parmak-cihaz kaynaşması, üç kalın dijit | Temas sınırı cümlesi + ⭐ `MIKRO_AKSIYON` çözümü: temas İKİ KLİBE bölünür (K74 hazırlık / K75 sonuç · K81 / K82) |
| **THE_MIRROR_FAUNA** | ① ⑪ MAJOR | 01:20 tentacle sarı bloom, DOKU KAYBI | Canlı katman için POZİTİF kaynak kuralı (§3.4 kalıbı): `the lit veins are themselves the source, the light not spreading past their edges` — `0% bloom` satırı KALKMAZ |
| **THE_MIRROR_FAUNA** | ⑫ | `LEAVES AT 02:00` | Plato kırıcı: S06 (K21-K24) ilk büyük ölçek olayı 3:20'de; ilk 30 s'de yeni kurulum 2 |
| **THE_HARD_DOCK** | ⑦ 8,8 | `03:30-03:37 B4 kenetlenme darbesi KESMEYLE GİZLENDİ` (Action Ellipsis) | ⭐ K09 (temas) ve K10 (dört kenet) kenetlenmeyi klibin İÇİNDE bitirir, saniyeli; K92 açılmayı da |
| **THE_HARD_DOCK** | ⑨ kafiye **2/10** | `03:50 S24 closing setup mismatch (B vs A) breaks bookend rhyme` | K05 ↔ K96 aynı kokpit kurulumu, CAMERA satırı BİREBİR; SPEC B `DÖNGÜ KANITI: A ↔ A` |
| **THE_HARD_DOCK** | ⑪ **5,5** | `01:20 S8→S9 renk sıcaklığı sıçraması (sıcak turuncu → nötr beyaz)` | Sahne içinde LIGHT satırı birebir (㉜⑥); sahneler arası fark ≤500 K ve ≤30° — iç mekân 4500 K sabit, dış mekân kaynaksız kubbe |
| **THE_HARD_DOCK** | ⑧ 6,6 | `01:48 & 03:12 yoğun nefeste vizör buğulanması YOK` | ⭐ Efor klibinde NEFES kanalı: `breath fog spreads on the inside of the pane and shrinks again` — K62 · K65 · K75 · K78 · K87 |
| **THE_HARD_DOCK** | ⑫ 7,2 | `00:10-00:40 ve 01:10-01:50 kokpit-dış mekân tekrar döngüsü PLATO` | S02 (kokpit) → S03 (yuva) → S04 (koridor) tek yönlü ilerler; kokpit K05-K08'den sonra K53-K55'e kadar geri DÖNMEZ |
| **THE_STOLEN_SKY** | ② B1 | SPEC C sol omuz sıyrığı ilan edildi; 00:30 yırtık → 01:40 TEMİZ → 02:50 temiz | YIPRANMA MERDİVENİ monotonik ve POZİSYONLU; `CONTINUOUS ACTION:` satırı kir/hasarı sıfırlanamaz listesinde |
| **THE_STOLEN_SKY** | ⑧ B1 1,7 | `WEIGHTLESS WORK` — 20 efor olayının 17'sinde sıfır zorlanma; kalın eldivenle çıplak el hızında buton | 31 efor klibinde ≥2 kanal + ödeme satırı; eldiven direnci açıkça (`the fingers close slowly against the glove's own stiffness`) |
| **THE_STOLEN_SKY** | ⑥ | `TWO GRAVITIES`: enkaz 1,56 m/s² ↔ 9,60 m/s² | Tek g, 92/92 aynı cümle; kopan döşemenin düşüşü **kadrajı terk süresiyle** yazılır [D127], ivmeyle değil |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **PB** | **bedenden bir şeyin ÇIKARILMASI eylemi** (COLD BURN S28: kask çıkarma) | Sahne BAŞTAN yazıldı: kimse bir şey çıkarmıyor, vuruş başka nesneye taşındı | ⭐ **K16-K19** — bir adamın bacağı devrilmiş panelin altında, panel kaldırılıyor, bacak serbest kalıyor. **Çözüm:** eylem BEDENDEN değil PANELDEN okunur — *the panel's edge lifts clear of his boot and shin, and he draws the leg back himself*. `trapped` · `crushed` · `pinned` · `injury` · `pain` · `blood` HİÇ yazılmaz; serbest kalan şey PANEL'in altıdır |
| **PB** | **yüzsüz izolasyon + tepeden makro + yan yana iki ön kol** (YERCEKIMI F1 S8) — kelimeler TEMİZDİ, kompozisyon reddetti → ⛔ SAHNE İPTAL | ① önce yalnız sözcük değişti → YETMEDİ ② KADRAJ değişti: nesneler ard arda, ray hizası | **K18 · K74 · K75 · K81 · K82** (eldiven + alet makroları). **Çözüm:** her makro klibinde kadraj kenarında bir ÇAPA durur (omuz hattı, kaburga kenarı, kol) — tam yüzsüz izolasyon kadrajı yazılmaz; iki el yan yana değil, biri önde biri arkada |
| **PK** | **tehlike çerçevesi sözlüğü** (COLD BURN S26: `wounded ship` · `dull orange glow`) | Replik değişti + tehlike sözlüğü ayıklandı | **K24 · K26 · K27 · K44 · K65 · K69** (kırılma, çatlak, kopma). **Çözüm:** hasar SAYILI ve SINIRLI yazılır [D38]: *the hull is whole except for exactly two points* — `wounded` · `catastrophic` · `collapsing` · `doomed` yazılmaz |
| **PK** | **kimlik yığını** — tek kişide 7 öznitelik × 25 prompt (SINKING STAKE · OMNI) | ⬜ önerilen: boy GÖRELİ, ten/saç/yaş prompt gövdesinden ÇIKAR, yüz tarifi yalnız yüzün KONU olduğu sahnede | **29 yüz klibi** × 3 karakter. **Çözüm:** öznitelik ≤3; ayırt etme yükü GEOMETRİDE (inci beyazı + şampanya altını ↔ beyaz + kobalt ↔ saten beyaz + bakır) |
| **YR** | insansız sahne + uzun `NEGATIVE:` bloğu + `Exactly 0 human figures` | NEGATIVE tek pozitif `Style:` satırına indi | **17 insansız klip** (K06 · K21 · K23 · K24 · K26 · K33 · K34 · K38 · K40 · K41 · K61 · K69 · K79 · K84 · K93 · K94 · K95). **Çözüm:** insan sayısı cümlesi RAKAMLA ve POZİTİF: `No people and no figures appear in this shot.` — `Exactly 0 human` kalıbı YAZILMAZ |
| **MİLLİYET / KURUM** | ⑯ ölçümünde 32 milliyet ifadesi, 1 gerçek kurum adı | satır silindi, yalnız fiziksel tanım | **0 risk** — planda milliyet yok, kurum yok, marka yok. Kontrol: ⑯ kapısı |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
⛔ VE DEPONUN KENDİ CÜMLESİ: kelime reddi SÖZLÜKLE çözülür ve her seferinde
   çözüldü; KOMPOZİSYON reddi sözlükle çözülmez. K18/K74/K75/K81/K82 bir
   KOMPOZİSYON riskidir — oraya sözlük çözümü yazmak boşa emektir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet (tavan tam dolu) + 9 satır §1b'de gerekçeli
QA ARIZASI:         20 adet (5 kayıt · 11 mercek)
RED SINIFI:         6 adet (PB ×2 · PK ×2 · YR ×1 · milliyet/kurum ×1)
⛔ EN PAHALI ÜÇÜ:
   ① SU  [D56 · THE_DEEP_PRESSURE 3,0 · Kostüm-Prop 1/10]
      — filmin adı, olayı, mekânı, varlığı ve hareketi beş kanaldan suya işaret ediyor
   ② EFOR [D206 · T8: 0,0 · 1,0 · 1,4 · 2,7 · 2,9 — deponun en düşük ekseni]
      — bu bir fiziksel iş filmi: kriko, kol, pim, yol, bağ
   ③ PANEL ALTINDAKİ BACAK [red defteri PB · COLD BURN S28 ailesi]
      — "bedenden bir şey çıkarma" politika yüzeyi ve film onu K16-K19'da dört klip sürdürüyor
```
