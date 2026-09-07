# 🩺 06 — HİKÂYE HATTI TEŞHİSİ: kapalı döngü

> **Tetikleyici:** proje sahibinin 02.09.2026 tarihli cümlesi —
> *"yeni filmlerin hikayeleri berbat saçma sapan şeyler."*
> **Oluşturma:** 02.09.2026
> **Girdi:** 79 film klasörünün makineyle taranması (§9.1) + `sayac.sh`
> 02.09 çıktısı + `4_HIKAYE_QA_CRITIQUE_PROMPT.md` gövdesi +
> `ONERME_VE_NOVUM_KILAVUZU.md` §1 + beş yeni planın satır sayımı.
> **Yeni üretim YOK.** Bu dosya tek bir kare üretmeden yazıldı.

> ⚠️ **DÜRÜSTLÜK KURALI [05'ten devralındı]:** her satır bir kanıta dayanır
> (dosya + satır, ya da betik çıktısı). **ÖLÇÜM** ile **OKUMA** ayrı ayrı
> etiketlidir. Kanıtı olmayan cümle ölçüm gibi yazılmaz.

> ⚠️ **05 İLE İLİŞKİSİ:** `05_DIKEY_HAT_TESHISI.md` (30.08.2026) aynı
> şikâyetin **dikey hat** kesitidir ve bulgusu ayaktadır. Bu dosya onu
> tekrar etmez; **bütün depoya** bakar ve 05'in göremediği **üçüncü halkayı**
> ekler: türü ölçen aletin de aynı türle yazılmış olması.

---

# 0. TEK CÜMLE

**Depo hikâye yazmıyor, novum gösterisi yazıyor — ve bu bir tercih değil,
kapalı bir döngü: yasaklar türü kurdu, kapılar yalnız üretimi ölçtü, ve
sonunda tür kendisini ölçen rubriğe "bu kusur değildir" diye yazıldı.
Sistem artık kendi arızasını göremiyor.**

⭐ **Ve döngünün imzası tek bir işarettir: `N/A`.** Sessizlik, hasımsızlık
ve tek insan ölçümün DIŞINA çıkarıldı; sonra dışarıda oldukları için
"güvenli" sayıldılar. Bu dosyanın bulduğu her arıza o işaretin altında
duruyor (§2 HALKA 3 · §4b).

---

# 1. ÖLÇÜLEN DURUM

## 1.1 Dört sıfır ve bir tavan — bütün depo (79 film)

```
FİLM KLASÖRÜ                                              79   (sayac.sh 02.09)
promptunda GERÇEK REPLİK olan film                         0
  └─ tek iz: THE_DEAD_APPROACH — ki o da D35'in KAYNAĞIDIR
kadrajda POZİTİF tarif edilmiş ikinci insanı olan film     15
"tek insan / ikinci insan YOK" yasağını taşıyan film       48
İSTEK satırı olan film                                      8
ENGEL satırı olan film                                      2
BEDEL satırı olan film                                     28
```

⭐ **En keskin satır ikinci ile üçüncüdür:** ikinci insanı YASAKLAYAN film
sayısı, ikinci insanı OLAN film sayısının üç katıdır. THE PAYLOAD'da bu
oran tek dosyada görünür: **1 pozitif ikinci-insan geçişine karşı 162 yasak
geçişi.**

## 1.2 Motor tek tip — ölçüm

`NOVUM TİPİ:` satırı yazılmış 13 filmin dağılımı:

```
fiziksel yasa            6
fiziksel yasa — algısal  5
fiziksel yasa            1   (küçük harfli varyant)
ölçek                    1
──────────────────────────
İNSAN / İLİŞKİ           0
(novum tipi hiç yazılmamış: 66 / 79)
```

**12/13 filmin motoru bir fizik kuralıdır.** Ve bu bir sapma değil,
kılavuzun kendi kararıdır — `ONERME_VE_NOVUM_KILAVUZU.md` §1 tablosu:

| Novum tipi | Karar (kılavuzun kendi sütunu) |
|---|---|
| Fiziksel yasa | ✅ **BİRİNCİ TERCİH** |
| Ölçek | ✅ **İKİNCİ TERCİH** |
| Zaman | ⚠️ ŞARTLI |
| Algı | ⛔ KAÇIN |
| Toplum | ⛔ **YASAK** — *"tek karakterde toplum gösterilemez"* |

⭐ **ÖLÇÜM:** tabloda **beş tip vardır ve beşi de insan-dışıdır.** İnsanın
insana yaptığı bir şeyin novum olabileceği seçenek olarak **listede yok.**
Ve son satırın gerekçesi bir başka yasağa dayanıyor: *"tek karakterde"* —
yani bir yasak (tek insan) ikinci bir yasağı (toplum novumu) doğuruyor.

## 1.3 Plan dosyaları — hikâye kaç satır

| PLAN | toplam satır | hikâye | üretim | hikâye % |
|---|---:|---:|---:|---:|
| THE_SINKING_STAKE (02.09) | 794 | 171 | 592 | **22%** |
| THE_LEANING_ROOM (02.09) | 654 | 184 | 445 | **28%** |
| THE_STILL_SWARM (01.09) | 968 | 264 | 684 | **27%** |
| THE_PAYLOAD (01.09) | 1209 | 438 | 769 | 36% |
| THE_FROST_LINE (29.08) | 1037 | 384 | 651 | 37% |

> Sayım §9.2 betiğiyle yapıldı: TEMA · ÖNERME/NOVUM · VURUŞ · HOOK ·
> SAHNE HARİTASI · MAYA · KARAKTER · DUYGU · FİNAL başlıklı bölümler
> **hikâye**, kalan her başlık **üretim** sayıldı.

**THE SINKING STAKE tek dosyada:**

```
SAHNE HARİTASI    58 satır  ← 25 sahnenin TAMAMI = 2,3 satır/sahne
NEGATIVE BIBLE    45 satır  ← tek sahne yok, yalnız yasak listesi
WORLD BIBLE       76 satır
CAMERA BIBLE      32 satır
PHYSICS BIBLE     41 satır
POLİTİKA SATIRI   44 satır
```

⭐ **ÖLÇÜM:** 4 dakikalık bir filmin bütün olay örgüsü, tek bir yasak
listesinden **13 satır** uzundur.

## 1.4 "Character Bible" karakter taşımıyor — ölçüm

THE SINKING STAKE'in CHARACTER BIBLE'ı **43 satırdır** ve iki insanı tarif
eder. İçerdiği bilgi: boy (188 / 165 cm), omuz genişliği, ten rengi, saç,
yaş bandı, göğüs boyunduruğu, kalça halatı, cep sayısı, vizör kaplaması,
sırt paneli.

```
İki figürün BİRBİRİNE ne olduğu           0 satır
Hangisinin ne İSTEDİĞİ                    0 satır
Nerede ANLAŞMADIKLARI                     0 satır
```

**OKUMA:** bu dosyanın adı yanlıştır. Yaptığı iş **süreklilik
şartnamesidir** — modelin figürü sahneden sahneye kaydırmamasını sağlar.
Karakter işi yapmaz ve yapması da beklenmez. Ama adı "CHARACTER" olduğu
için **karakter yazılmış sayılır** ve boş kutu görünmez.

## 1.5 İki kişi var, ikisi de aynı fikirde — okuma

THE SINKING STAKE depodaki **iki insanlı en yeni filmdir** ve merkezî
seçimi şudur (plan · S19):

> *"kısa boylu avucunu çekirdeğe yatırır (**onay**), uzun boylu onu
> beşikten kaldırır (**karar**)"*

**OKUMA:** film 25 sahne boyunca iki insanı yan yana tutar ve **tek bir
sahnede bile aralarına bir fark koymaz.** Onay + karar = tek kişi, iki
gövde. 05 §2.1'in duvarı yıkılmadı; **iki kişilik hâline getirildi.**

## 1.6 Ölçüm hattının kendi durumu

```
CANLI SİSTEMDE ÖLÇÜLEN FİLM        2 / 79       (sayac.sh 02.09)
ÖLÇÜLDÜ AMA TABLOYA İŞLENMEDİ      8 film
T4 HİKAYE tablosundaki satır       2  — ikisi de Ⓥ ⛔ ⚠️ ŞARTLI
SPEC'i olan film                  15 / 79
```

⛔ **T4'ün iki satırının ikisi de bağlayıcı değildir** (mod V · ön koşu).
Yani **hikâye kalitesi bu depoda bugüne kadar bir kez bile bağlayıcı
olarak ölçülmedi.** Şikâyet bir ölçümü tartışmıyor; bir boşluğu bildiriyor.

---

# 2. MEKANİZMA — üç halka, ve üçüncüsü döngüyü kapatıyor

## HALKA 1 — yasaklar bir tür kurdu  `[05 §3 · ayakta ve büyüdü]`

05 bunu ölçtü: D20 (klon) → ilişki gitti · D35 (lip-sync) → ses gitti ·
D34/D45 (ekran metni) → isim gitti · D1 (gizli kesme) → kurgu gitti.
Dördü de ayrı ayrı doğru; üst üste gelince geriye **isimsiz + sessiz +
yalnız + hareketsiz** bir tür kaldı.

⛔ **02.09 kesitinde bu halka kapanmadı, GENİŞLEDİ:** 05 *"ASLA yeni bir
novum kataloğu maddesi ekleme, 16 tane var"* yazdı (§8). O tarihten sonra
yazılan beş filmin beşi de yeni bir fizik kuralı ekledi (Cold Weld ·
Still Swarm · Payload · Leaning Room · Sinking Stake).

## HALKA 2 — kapıların tamamı üretim ölçüyor

`03_PLAN_ONCESI_KONTROL_LISTESI` imza bloğunun **15 maddesi:**

```
A1 metin çelişkisi · A2 sahne sayısı · A3 süre · A4 yasaklı sahne tipi
B1 doruk sahne içinde mi · B1b ışık takvimi · B2 bedelli seçim VAR MI
B3 tema hangi sahnede · B4 açı yayı · B6 politika satırı
C  6 sayısal kilit · D risk sayımı · E QA SPEC bloğu
```

**ÖLÇÜM:** on beş maddenin **on ikisi** üretim/uygunluk denetimidir.
Hikâyeye değen üçü (B1 · B2 · B3) **VARLIK** denetimidir — "bedelli seçim
var mı", "tema hangi sahnede" — **NİTELİK** denetimi değildir. Hiçbir kapı
*"bu kimin umurunda"* sorusunu sormaz.

`TODO_TEMA_VE_ACI_KAPILARI.md` bunu kendi cümlesiyle zaten yazmış:

> *"Sistem neyi ölçüyorsa onu optimize etti: kesmeyi ve fiziği ölçüyordu,
> temayı ve açıyı değil."*

⭐ Cümle doğru ve **hâlâ geçerli** — yalnız değişkeni değişti. Bugün sistem
tema ve açıyı da ölçüyor. **Hikâyeyi ölçmüyor.**

## HALKA 3 — ⭐ YENİ BULGU: tür, kendisini ölçen aleti de yazdı

`QA_PROMPTLARI/_KAYNAK/4_HIKAYE_QA_CRITIQUE_PROMPT.md` — deponun hikâye kalitesini
ölçen **tek** aleti. §"THE SERIES' STORY DNA" bloğu, rubriğe **neyi kusur
saymayacağını** söyler:

```
✅ INTENDED, NOT A FLAW:
- Exactly one human character. No ensemble, no dialogue partners on screen.
- Slow, contemplative pacing. Wonder over action.
- Endings that hold rather than resolve. Silence over speeches.
- No villain. The opposing force is environmental, physical, or temporal.
```

Ve kategori kuralları:

```
⛔ DECLARED ABSENCE IS NOT A DEFICIT — IT IS `N/A`.
   ... no dialogue, no face on screen, no resolution, no second character ...
   takes N/A, stays out of the mean.
⛔ FULLY SILENT FILM → SCORE THIS CATEGORY N/A, NOT A NUMBER.
```

**ÖLÇÜM — bunu yan yana koy:**

| Sahibin "saçma" dediği şey | Rubriğin hükmü |
|---|---|
| kimse yok | *"Exactly one human character"* → ✅ kusur değil |
| kimse konuşmuyor | Diyalog → **N/A**, ortalamanın DIŞINDA |
| kimse kimseye karşı değil | *"No villain"* → ✅ kusur değil |
| hiçbir şey bitmiyor | *"Endings that hold rather than resolve"* → ✅ kusur değil |

⛔ **DÖNGÜ BURADA KAPANIYOR.** Şikâyetin dört maddesi, ölçen aletin
"düşmeyeceksin" dediği dört maddedir. Aynı rubrik her filmi ölçse bile
**bu arızayı asla raporlayamaz** — raporlaması yasaklanmıştır.

⭐ **VE İKİNCİ SONUÇ DAHA AĞIR:** THE IRON SLOPE **2,6/10** ve THE THIN ROOF
**3,5/10** aldı. Bu skorlar, en düşük düşecek kategoriler **ortalamadan
çıkarıldıktan sonraki** skorlardır. Yani ölçülen gerçek, ölçülen sayıdan
**daha kötüdür.**

> ⚠️ **RUBRİK KURALI KENDİ BAŞINA YANLIŞ DEĞİLDİR.** "Sessiz filme sessiz
> olduğu için 5 verme" doğru bir tasarım korumasıdır ve tasarımı cezadan
> korur. Arıza kuralda değil, **kapsamındadır**: koruma "bu bir kısıttır"
> demekle kalmıyor, "bu kısıt hikâyeye zarar veriyor mu" sorusunu da
> **sordurmuyor.** 05 §3.1'in mekanizmasının aynısı: daraltılan RİSK,
> genişletilen YASAK.

---

# 3. NEDEN 05'İN ① REÇETESİ İŞE YARAMADI — iki ayrı sebep

## 3.1 Kapıya inmedi — ölçüm

05 §5①, 30.08'de sıfır maliyetli birinci madde olarak İSTEK/ENGEL/BEDEL
satırını yazdı. `03_PLAN_ONCESI_KONTROL_LISTESI.md` satır 343'te bugün
şu duruyor:

```
⛔ B5 BOŞ DEĞİL, AYRILMIŞ: İSTEK/ENGEL/BEDEL satırı
   (05_DIKEY_HAT_TESHISI §5① · henüz bu listeye inmedi).
```

**Üç gün "ayrılmış" kaldı ve o üç günde beş film yazıldı.** Sonuç
ölçüldü: ENGEL satırı **2/79**.

## 3.2 ✏️ İnse bile yetmezdi — okuma  ⛔ BU BÖLÜMÜN HÜKMÜ GERİ ÇEKİLDİ

> **02.09.2026, aynı gün.** Aşağıdaki muhakeme OKUMA olarak yazılmıştı ve
> dış araştırma turu onu **desteklemedi.** İki bağımsız rapor çapraz
> okundu: insan-hasım ile doğa-hasım arasında izleyici tutundurması veya
> hatırlanma açısından **belgelenmiş nicel bir fark yok**; fark çatışmanın
> TÜRÜNDEN değil **BEDELİN büyüklüğünden** geliyor. Kayıt ve gerekçe:
> `04_ARASTIRMA_BULGULARI.md` T4.0.
>
> **Metin silinmedi, kayıt olarak duruyor** — bir okumanın nasıl
> düşürüldüğü, okumanın kendisi kadar öğreticidir.
>
> ⭐ **AMA B5 ÇÖKMEDİ, KAYNAK BULDU.** Rapor ②, *"hiçbir şey olmuyor /
> umursamadım"* tepkisinin üç belgelenmiş sebebini ayırıyor: **istek yok ·
> bedel yok · muhatap yok.** Üçü B5'in üç satırıdır. Değişen: dördüncü
> satır HASIM'dan **MUHATAP**'a döndü ve asıl kapı **BEDEL**'e taşındı.

THE LEANING ROOM (02.09) üç satırın **üçünü de** yazdı. Ve film hâlâ
"bir kadın + bir fizik kuralı"dır. Sebep yapısal:

```
İSTEK  bir kişinin ne istediğidir.
ENGEL  bu depoda HER ZAMAN bir fizik kuralıdır.
       Fizik kuralı hiçbir şey İSTEMEZ.
       İstemeyen bir engel bir ENGELDİR — bir HASIM değildir.
```

**Engel parkuru gerilim üretir; hasım hikâye üretir.** 05'in ① maddesi
isteği geri getirdi ama isteğin **muhatabını** geri getirmedi — ve
rubriğin *"No villain"* satırı (§2 HALKA 3) muhatabı getirmeyi zaten
kusur olmaktan çıkarmıştı.

---

# 4. ÇÖZÜM — maliyete göre sıralı

> Sıra önemlidir. ⓪ bu dosyayla birlikte **UYGULANDI**. ①-② bugün
> uygulanabilir ve hiçbir üretim yasağını değiştirmez. ③-④ **sahibin
> editoryal kararıdır** — ajan tek başına almaz (§6).

## ⓪ UYGULANDI — B5 kapıya indi VE betiğe indi

```
① 03_PLAN_ONCESI_KONTROL_LISTESI.md  → B5 maddesi + imza bloğu 15 → 16
② prompt_kontrol.py                  → ⑰ B5 HİKÂYE OMURGASI kapısı
③ .claude/skills/yeni-film/SKILL.md  → §3 yazım sırasına B5 dörtlüsü
```

**⑰ ne denetliyor:**

```
İSTEK · ENGEL · BEDEL · HASIM satırları var mı            → BLOCK
İSTEK bir SEYİR mi ("anlamak/görmek/fark etmek")          → FIX
HASIM satırı ORTAMI mı gösteriyor                          → FIX
iki insanlı filmde AYRILIK sahnesi yazılmış mı            → FIX
```

**⑰ KALİBRASYONU · 02.09.2026 · 80 film klasörü:**

```
kapı KOŞTU     69   (sahne başlığı ≥6 — ⑭ ile AYNI sınır)
kapı ATLANDI   11   (eski sahne başlığı biçimi)
B5 EKSİK       69 / 69
```

⭐ **En yakın film THE LEANING ROOM: yalnız HASIM eksik.** O oturum B5'i
kapı inmeden kendi yazmıştı — yani eksik olan bilgi değil, KAPIYDI.

⛔ **Neden betiğe indi:** 05 §5① üç gün "listeye inecek" diye bekledi ve
inmedi. Deponun kendi dersi: **yazılan ama koşulmayan kapı, koşulmamış
kapıdır** (05 §5⑥). Bu madde listeye yazıldığı gün betiğe de yazıldı.

## ① ✏️ SIFIR MALİYET — MUHATAP satırı (B5'in ikinci yarısı)

> **02.09.2026 · TUR 4 ile düzeltildi.** Bu madde önce "HASIM" adıyla ve
> *"ORTAM hasım değildir"* kapısıyla yazıldı; kapı **geri çekildi** (§3.2).
> Ortam meşru bir karşı güçtür. Satır kalıyor çünkü işlevi kanıtlandı —
> ama işlevi "hasım bul" değil, **"eylemin yankısını göster"**dir.

Her plana tek satır, üç seçenekten **biri**:

```
MUHATAP: eylemin yankısı NEREDE görünüyor
         □ ikinci insan  (kadrajda VEYA kadraj dışında)
         □ karakterin kendi geçmiş kararı (film başlamadan verilmiş)
         □ karakterin kendi bedeni / dayanma sınırı
         □ ortamın KALICI olarak değişen bir parçası

⛔ ASIL KAPI BURADA DEĞİL, BEDEL'DE: bedel bir SAHNE numarası taşımıyorsa
   madde boştur. Ölçülmüş olan budur — "güzel ama boş" şikâyeti, insanî
   bedelin görsele yenildiği filmlerde çıkıyor.       [TUR 4 · T4.1/13]
```

**Neden işe yarar (gerekçe ÖLÇÜMDÜR, sonuç OKUMADIR):** üç seçeneğin
üçü de **mevcut yasakların hiçbirini ihlal etmez.** İkincisi ve üçüncüsü
tek insanla, sessizce, tek çekimde yazılabilir. Bugün 79 filmin
79'unda bu satır YOK.

## ② ÇOK UCUZ — iki insanlı filmlerde AYRILIK KAPISI

15 filmde ikinci insan zaten var ve hiçbirinde bir fark yok (§1.5).
İki insan yazan her plana tek kapı:

```
AYRILIK: iki figürün AYNI FİKİRDE OLMADIĞI sahne = S___
         · farkı taşıyan kanal: jest / duraklama / yön / temas reddi
         · ⛔ ikisi de aynı anda aynı şeyi yapıyorsa satır BOŞTUR
```

**Sıfır replikle mümkündür ve depo bunu bir kez neredeyse yaptı:**
THE SINKING STAKE S1 — *"0:14'te kısa boylu bırakır"*. Bu bir ayrılıktı;
plan onu **yorgunluk** olarak yazdı, **itiraz** olarak değil.

## ③ ✅ UYGULANDI — rubriğin DNA bloğu SINIRLANDI

**Sahip kararı (02.09.2026 · §6-A): KALINTI.** Dört madde kaldırılmadı,
kapsamı daraltıldı. Rubriğe (İngilizce gövde kuralı olarak, depo kuralı
gereği Türkçe not/tarih/ders numarası girmeden) eklenen:

```
"Exactly one human character"
  → kusur değil. AMA: filmde kimsenin kimseden bir şey istemediği
    de kusur değil MİDİR? Bu ayrı bir sorudur ve sorulur.

"No villain. The opposing force is environmental."
  → kusur değil. AMA: karşı gücün karakterden bir şey İSTEYİP
    istemediği sorulur. Hiçbir şey istemiyorsa bu bir BULGUDUR.

"Endings that hold rather than resolve"
  → kusur değil. AMA rubriğin kendi ayrımı geçerlidir:
    "ends" ile "stops" aynı şey değildir (mevcut MODE V sorusu).
```

Ve **N/A kuralına tek istisna**: bir kategori N/A ise ortalamadan çıkar
**ama rapora bir satır bırakır** —

```
N/A DEFTERİ: bu filmde N/A alan kategori sayısı ___ / 10
⛔ 3'ten fazlaysa rapor başlığına yazılır: "bu skor 10 kategorinin
   ___'i üzerinden hesaplandı."
```

**Neden:** bugün bir film dört kategoriden muaf tutulup 6/10 alabiliyor
ve rapor bunu hiçbir yerde söylemiyor. Bu bir sayı hilesi değil, ama
**okuyan sayının neyi kapsadığını bilmiyor.**

## ④ ✅ UYGULANDI — novum tablosuna altıncı satır

**Sahip kararı (02.09.2026 · §6-B): EKLENSİN.**
`ONERME_VE_NOVUM_KILAVUZU.md` §1 tablosuna:

| Novum tipi | İlk 3 sn | Thumb-stop | Risk | Karar |
|---|:--:|:--:|---|:--:|
| **İlişki** (birinin ötekinden istediği şey) 🆕 | yüksek | ⬜ ölçülmedi | yasaklar hiç sınanmadı | ✅ **ÜÇÜNCÜ TERCİH** |

Ayrıca §2'ye ilişki tipinin TAŞIYICI kalıbı yazıldı — aynı somutluk kuralı,
iki jest: `<nesne> × <A'nın jesti> ↔ <B'nin FARKLI jesti> → <görünen ayrılık>`.
"Aralarında gerilim var" taşıyıcı DEĞİLDİR.

⬜ **Dürüst sınır kılavuza da yazıldı:** thumb-stop sütunu BOŞ ve öyle
kalacak — depoda ölçülmüş tek bir ikinci-insanlı film yok. Elde bulgu
değil, KARAR var; ilk ölçüm `PROB_KOSUSU.md`'nin iki probudur.

---

## ④b DİYALOG — neden 0/79 ve nasıl açılır  🆕 02.09.2026

> Sahibin ikinci sorusu: *"daha çok diyalog için neler yapabiliriz."*
> Bu bölüm ayrı durur çünkü bulgusu §2'den bağımsızdır ve daha sert.

### ÖLÇÜM — yasağın bütün kanıtı TEK FİLM

```
replik olan film                                     0 / 79
yasağın dayandığı vaka sayısı                        1
  └─ THE DEAD APPROACH · Diyalog & Ses 3/10 ·
     "0:11 — Lip-sync fails entirely on dialogue"
D35'in bu vakadan çıkardığı REÇETE sayısı            5
reçetelerden biriyle üretilmiş film sayısı           0
```

⛔ **VE VAKANIN KENDİSİ KARIŞIK BİR ÖLÇÜMDÜR.** `LESSONS_LEARNED`'ın kendi
cümlesi: *"ilk diyaloglu **compilation** üretimi. Diyalog + birleştirilmiş
kurgu, kesme ve senkron hatalarını **aynı anda** tetikledi."* İki değişken
birlikte değişti. Bu kayıt, düşüşü **yalnız diyaloğa** yüklemeyi
desteklemez.

### RİSK KARTI 7'NİN DÖNGÜSÜ — HALKA 3'ün ikinci kopyası

`02_RISK_KARTLARI.md` KART 7, yazara şunu söylüyor:

> *"💡 EN GÜVENLİ: Sessiz film. Kaleida tamamen sessiz ve Diyalog
> kategorisinden hiç puan kaybetmedi (**N/A**)."*

⭐ **ÖLÇÜM:** kartın kanıtı bir N/A'dır. Yani *"sessiz film daha iyi puan
alıyor"* cümlesinin sebebi, **sessizliğin puanlanmamasıdır.** Bu bir kanıt
değil, §2 HALKA 3'ün risk kartındaki aynısıdır — ve bu kez doğrudan
YAZIM kararını yönlendiriyor.

### 05 §3.1'İN MEKANİZMASI BURADA DA ÇALIŞTI

```
D35 NE DEDİ                      NASIL UYGULANDI          FARK
"çöken lip-sync ekrana çıkmasın" → "film sessiz"          ⛔ kapsam
```

**Ekranda ağız yoksa lip-sync riski YAPISAL OLARAK sıfırdır.** Kadraj dışı
ses · telsiz · kayıt · kask içi AI — dördü de D35'in **dışındadır** ve
D35'in kendi 3. maddesi bunu zaten tarif eder. Yani depo **bugün, hiçbir
yasağı ihlal etmeden** replikli film yazabilir. Engel D35 değil, **D35'in
geniş yorumudur.**

### DEPODA HAZIR DURAN VE HİÇ KULLANILMAMIŞ YIĞIN

```
../SES_VE_DIYALOG_URETIM_KILAVUZU.md   register haritası (HUMAN/MACHINE) ·
                                       replik bütçesi · plana giren tablo ·
                                       prompta giren ses bloğu
../VEO_3_1_FAST_...KILAVUZU.md §3      tırnak sentaksı — tırnaksız replik
                                       modelde anlamsız dudak hareketi üretir
                            §4         lip-sync artıran parametreler +
                                       "no subtitles" + "clean dialogue only"
                            §8         iki kişi AYNI ANDA konuşursa başarı
                                       %40 altına düşer → tek konuşmacı,
                                       sahne sahne üret, kurguda birleştir
                            §9         ElevenLabs Sync 3 hibrit: sessiz üret,
                                       sonra kare hassasiyetinde senkronla
DERSLER/02 · D35                       beş reçete (ölçek · <5 sn · kaynak ·
                                       fonem cümlesi · sıra alma yok)
PROB_KOSUSU.md · PROB B                yapıştırmaya hazır 10 sn'lik sınama
```

⛔ **Yedi kaynağın yedisi de yazılmış ve sıfırı kullanılmış.**

### VE MOTOR DEĞİŞTİ — depo bunu kendi kılavuzuna yazdı

`VEO_3_1_FAST` §1 başlığı: *"ÇİFT AKIŞLI DİFÜZYON VE EŞZAMANLI SES DÖNEMİ"* —
*"varsayılan sessiz video dönemini kapatıp"* · çift akışlı difüzyon ·
10 ms senkron gecikmesi.

```
yasağın ölçüldüğü tarih        ~03-04.08.2026  (Dead Approach · D34-D38)
motorun değiştiğinin yazıldığı  27-28.08.2026  (VEO 3.1 kılavuzu §1)
yasağın yeniden sınandığı tarih  ⬜ hiç
```

**OKUMA:** yasak bir motor kuşağı ÖNCESİNE aittir ve o motorun değiştiği
aynı depoda belgelenmiştir.

### ÇÖZÜM — DİYALOG MERDİVENİ, riski en düşükten yükseğe

> Sıra maliyet değil **RİSK** sırasıdır. Her basamak bir öncekini geçmeden
> çıkılmaz ve her basamağın sonucu `04_ARASTIRMA_BULGULARI.md`'ye yazılır.

```
BASAMAK 1 · KADRAJ DIŞI SES        lip-sync riski YAPISAL OLARAK SIFIR
   ekranda ağız yok. Telsiz · kayıt · kask AI · başka odadan gelen ses.
   D35'in 3. maddesinin kendi cümlesi prompta girer.
   ⭐ BUGÜN, SINAMA GEREKTİRMEDEN YAZILABİLİR.

BASAMAK 2 · TEK YÖNLÜ KAYIT (LOG)  cevap beklenmiyor → sıra alma yok
   KART 7'nin kendi ✅ satırı. LOW POWER'ın planı bunu doğru çözmüş:
   "19 dakikalık gecikme nedeniyle kimse cevap veremez."

BASAMAK 3 · EKRANDA TEK REPLİK     D35'in beş reçetesi AYNI ANDA
   orta yakın çekim · replik < 5 sn (tercihen < 3) · tırnak sentaksı ·
   fonem sadakati cümlesi · "no subtitles" · tek konuşmacı.
   ⛔ Bu basamak PROB B'dir ve prob KOŞULMADAN filme girmez.

BASAMAK 4 · İKİ KİŞİ, SIRAYLA      asla eşzamanlı — §8'in %40 sayısı
   iki ayrı klip, iki tek-konuşmacı planı, kurguda birleştirme.
   ⛔ Bu, D1'in (modelin uydurduğu kesme) İHLALİ DEĞİLDİR: senin yaptığın
     kesme başka şeydir [05 §3.1 ikinci satır].

BASAMAK 5 · HİBRİT SENKRON         VEO §9 · sessiz üret + Sync 3
   yalnız 1-4 yetmezse. Ekstra araç, ekstra maliyet.
```

⛔ **KART 7 YENİDEN YAZILIR:** "💡 EN GÜVENLİ: sessiz film" satırı, kanıtı
bir N/A olduğu için kaldırılır ve yerine bu merdiven konur. Sessizlik bir
seçenek olarak KALIR — ama "en güvenli" damgası ölçüme dayanmıyor.

## ⑤ ASLA

```
· Yeni bir fizik kuralı eklemek. 21 tane var. [05 §8'in tekrarı]
· "Hikâye kötü" tanısını yeni bir YASAK ile çözmeye çalışmak —
  arızayı üreten mekanizma tam olarak budur (§2 HALKA 1).
· ⭐ BİR N/A'YI KANIT OLARAK KULLANMAK. Bu dosyanın en çok tekrar eden
  hatası budur ve iki ayrı yerde bulundu: rubrikte (§2 HALKA 3) ve risk
  kartında (§4b). Ölçülmeyen bir şey "iyi" değildir — ÖLÇÜLMEMİŞTİR.
```

---

# 5. NE ÖLÇÜLMEDİ — dürüst kayıt

```
⬜ 77 filmin ekranda nasıl hissettirdiği     → canlı sistemde ölçülmedi
⬜ İkinci insanlı klibin modelde tutup tutmadığı → 05 §9.2 PROB A hâlâ koşulmadı
⬜ Replikli klibin lip-sync davranışı        → 05 §9.2 PROB B hâlâ koşulmadı
⬜ HASIM satırı yazılmış bir filmin skoru    → böyle bir film yok
⬜ Rubriğin DNA bloğu daraltılırsa skorların ne olacağı → denenmedi
⬜ Kadraj dışı sesli bir filmin lip-sync davranışı → hiç denenmedi
   (ve BASAMAK 1'de ekranda ağız yoktur — risk yapısal olarak sıfırdır)
⬜ Veo 3.1 kuşağında replikli klibin davranışı → yasak eski motorda ölçüldü
⬜ Hiçbir film YAYINLANMADI                  → tutundurma verisi 0
```

⛔ **05'in son sınırı burada da geçerli ve bir gün daha yaşlandı:**
"izleyici sıkılıyor" cümlesinin arkasında **tek bir gerçek izlenme
eğrisi yok.** Elimizde rubrik okumaları ve sahibin izlenimi var. İkisi de
meşru girdidir; ikisi de tutundurma verisi DEĞİLDİR.

---

# 6. ✅ SAHİBİN KARARLARI — 02.09.2026'da verildi

```
A) RUBRİK DNA BLOĞU        → KALINTI. Kapsam daraltıldı (§4③).
   Dört madde kaldırılmadı; her birinin altına "STILL ASK" sorusu ve
   N/A DEFTERİ eklendi. Rubrik artık şunu sorabiliyor: bu filmde
   kimse kimseden bir şey istiyor mu.

B) NOVUM TABLOSU 6. SATIR   → EKLENSİN. İlişki tipi ✅ ÜÇÜNCÜ TERCİH (§4④).
   Gerekçe kılavuza yazıldı; thumb-stop sütunu ⬜ BOŞ bırakıldı —
   ölçüm yok, karar var.

C) DİYALOG (sahibin 2. sorusu) → MERDİVEN kuruldu (§4b).
   KART 7'nin "en güvenli: sessiz film" satırı KALDIRILDI; kanıtı bir
   N/A'ydı. Sessizlik seçenek olarak kalır, "en güvenli" damgası düştü.
```

⭐ **A ve B'nin ortak sonucu tek cümle:** seri artık *"tek insan, sessiz,
hasımsız"* olmayı bir KİMLİK olarak savunmuyor. Bu dördü hâlâ yazılabilir
— ama artık **seçilerek** yazılır, birikerek değil.

# 7. BU DOSYANIN KENDİ SINIRI

```
· §1 sayıları makineyle üretildi ve tekrarlanabilir (§9.1 · §9.2)
· §1.5 · §1.4 OKUMADIR — altındaki satır sayıları ÖLÇÜMDÜR
· §2 HALKA 3 ÖLÇÜMDÜR: alıntılar rubriğin gövdesinden, kesilmeden
· §3.2 OKUMADIR; §3.1 ÖLÇÜMDÜR (dosya + satır numarası)
· §4'ün hiçbir maddesi denenmedi → "işe yarar" denmiyor,
  "denenmedi ve denenebilir" deniyor
· T4'ün iki satırı mod V'dir → sayı olarak bağlayıcı değildir,
  bu dosya onları KANIT değil İŞARET olarak kullanır
```

---

# 8. ÖNERİLEN SIRA — tek sayfa

```
✅ BUGÜN YAPILDI (02.09.2026)
   ⓪ B5 → 03_PLAN_ONCESI + prompt_kontrol ⑰ + yeni-film skill
   ③ rubrik DNA bloğu daraltıldı + N/A DEFTERİ (sahip kararı A)
   ④ novum tablosuna İLİŞKİ satırı + ilişki taşıyıcı kalıbı (karar B)
   ④b DİYALOG MERDİVENİ + KART 7 yeniden yazıldı (karar C)

BİR SONRAKİ FİLM (hiçbir sınama gerektirmez)
   ① HASIM satırı yazılır — ORTAM değil
   ② iki insan varsa AYRILIK sahnesi
   ④b BASAMAK 1: kadraj dışı ses — lip-sync riski YAPISAL SIFIR
   ⭐ Bu üçü bugünün kurallarıyla, tek bir yasağı ihlal etmeden yazılır.

BU HAFTA — iki prob (PROB_KOSUSU.md · toplam 2 klip)
   PROB A ikinci insan   → İLİŞKİ satırının thumb-stop sütununu doldurur
   PROB B tek replik     → BASAMAK 3'ün kapısıdır, geçmeden filme girmez
   Sonuç: 04_ARASTIRMA_BULGULARI.md

SONRA
   İlk İLİŞKİ novumlu film + ilk replikli film mod D ile ÖLÇÜLÜR.
   ⛔ Ölçülmezse bu dosyanın tamamı bir varsayım olarak kalır.

ASLA
   yeni fizik kuralı · yeni yasak · N/A'yı kanıt olarak kullanmak
```

# 9. EKLER

## 9.1 Depo taraması — §1.1 ve §1.2'nin sayıları

```bash
python3 - <<'PY'
import os,glob,re
roots=['dikey_shorts_filmler','yatay_2_4_dk_filmler_uzay','yatay_3_5_dk_filmler',
       'yatay_10_20_dk_filmler']   # 7-9 klasörü 04.09.2026'da kapandı;
                                   # THE_SLOW_STONE 10-20'ye taşındı, film kümesi AYNI
tot=pos=neg=dia=0; novum={}
for r in roots:
    for d in sorted(os.listdir(r)):
        p=os.path.join(r,d)
        if not os.path.isdir(p): continue
        fs=glob.glob(p+'/**/*.md',recursive=True)
        txt=''.join(open(f,encoding='utf-8').read()+'\n' for f in fs if os.path.isfile(f))
        if not txt.strip(): continue
        tot+=1
        if re.search(r'(?<![Nn]o )\b(two figures|two people|two astronauts|'
                     r'both figures|the other astronaut)\b',txt,re.I): pos+=1
        if re.search(r'(no second (person|human|figure)|exactly one human)',txt,re.I): neg+=1
        if re.search(r'(says?, in |DIALOGUE:\s*"[^"]{2,})',txt): dia+=1
        m=re.search(r'NOVUM TİPİ:\s*(.+)',txt)
        if m: novum[m.group(1).strip().lower()]=novum.get(m.group(1).strip().lower(),0)+1
print(f"film {tot} · pozitif ikinci insan {pos} · yasak {neg} · replik {dia}")
for k,v in sorted(novum.items(),key=lambda x:-x[1]): print(f"  {v:3}  {k}")
PY
```

## 9.2 Plan hikâye oranı — §1.3'ün sayıları

```bash
python3 - <<'PY'
import re,sys,os
STORY=re.compile(r'TEMA|ÖNERME|NOVUM|VURUŞ|HOOK|SAHNE HARİTASI|LOGLINE|'
                 r'KARAKTER|DUYGU|FİNAL|MAYA',re.I)
for p in sys.argv[1:]:
    L=open(p,encoding='utf-8').read().split('\n')
    hd=[(i,l) for i,l in enumerate(L) if re.match(r'^#{2,3} ',l)]
    s=t=0
    for j,(i,l) in enumerate(hd):
        n=(hd[j+1][0] if j+1<len(hd) else len(L))-i
        (s:=s+n) if STORY.search(l) else (t:=t+n)
    print(f"{os.path.basename(p):34} {len(L):>5} satır · hikâye {s:>4} "
          f"({100*s//max(len(L),1)}%) · üretim {t}")
PY
# kullanım: yukarıdaki betik <PLAN dosyaları...>
```

## 9.3 Kaynaklar

```
05_DIKEY_HAT_TESHISI.md                   §2.1 dört sıfır · §3 dört önlem · §5① · §9.2 problar
03_PLAN_ONCESI_KONTROL_LISTESI.md         imza bloğu · B5 "ayrılmış" satırı (30.08→02.09)
QA_PROMPTLARI/_KAYNAK/4_HIKAYE_QA_CRITIQUE_PROMPT.md  §STORY DNA · §DECLARED ABSENCE · §6 N/A
ONERME_VE_NOVUM_KILAVUZU.md §1            beş novum tipi · "BİRİNCİ TERCİH"
02_RISK_KARTLARI.md KART 7                "EN GÜVENLİ: sessiz film" · kanıtı N/A
DERSLER/02_KARAKTER_VE_CANLI.md D35       tek vaka · beş reçete · sıfır uygulama
LESSONS_LEARNED.md                        "diyalog + compilation AYNI ANDA"
SES_VE_DIYALOG_URETIM_KILAVUZU.md         register · replik bütçesi · ses bloğu
VEO_3_1_FAST_...KILAVUZU.md §1·§3·§4·§8·§9  motor kuşağı · sentaks · hibrit
PROB_KOSUSU.md                            PROB A · PROB B — ikisi de koşulmadı
FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md     iki satır · ikisi de Ⓥ ⛔ ⚠️
TODO_TEMA_VE_ACI_KAPILARI.md              "sistem neyi ölçüyorsa onu optimize etti"
sayac.sh (02.09.2026)                     79 film · canlı ölçüm 2 · SPEC 15
yatay_3_5_dk_filmler/THE_SINKING_STAKE/   §1.3 · §1.4 · §1.5 ham kanıt
```
