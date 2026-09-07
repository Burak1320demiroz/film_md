# 📚 YERÇEKİMİ — FAZ 10 / ZEMİN · QA DERSLERİ VE AKSİYON

```
Koşu    07.09.2026 · Gemini · tek oturum · ON İKİ mercek
Ham     ../../../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/
        02_HAM_RAPORLAR/YERCEKIMI_FAZ10_12MERCEK_HAM.md
Betik   ../../../kilavuzlar_ve_sistem_dosyalari/RAPOR_KONTROL/RAPORLAR/
        FAZ_10_ZEMIN_20260907_RAPOR_KONTROL.md
Mod     ⚠️ V — on ikisinin on ikisi · SPEC yok · FAZ_10_QA_PROMPT.md YOK
Karar   🚨 PARTİ GEÇERSİZ — hiçbir satır T tablolarına girmez [D188]

⛔ ⑪ ÖLÇÜM KAPISI KOŞULMADI — sahip kararı (06.09.2026). Aşağıdaki
   bütün sayılar RAPOR beyanıdır; ölçüm hakemliği yoktur. Nerede
   ölçüm gerektiği tek tek yazılıdır.
```

---

# 🔴🔴 BİRİNCİ BULGU — MAKARA 11 KLİP, PLAN 12: **FİLMİN SON KARESİ TESLİM EDİLMEMİŞ**

Bu, koşunun tek gerçek bulgusudur ve **on iki merceğin on ikisi de kaçırdı.**

```
PLAN     FAZ_10_ZEMIN.md · S109 → S120 · 12 sahne
IZGARA   sahne n başlangıcı = (n−1) × 10 s   (03.09.2026 sahip kararı)
BEKLENEN 12 × 10,0 s = 120 s · 18:00 → 20:00

MAKARA   on iki raporun ON İKİSİ de 109–111 s ölçtü
         on rapor 10 kesme saydı, ikisi (⑦ ⑧) 11 — ZAMAN KODU BASMADAN
         ① ve ② kesme zaman kodlarını AYRI AYRI listeledi ve
         ikisi de tam 10 s katlarına oturuyor

⇒ 110 s ÷ 10 s = 11 KLİP.  PLAN 12.  FARK: bir klip.
```

**Hangi sahne yok?** Şeridin başı cevabın yarısını veriyor: dokuz mercek
`--111111111` yazdı — **iki insansız sahne BAŞTA duruyor**, yani S109 İNİŞ ve
S110 SESSİZLİK teslim edilmiş. Eksik olan S111–S120 arasından biridir.

Kalan yarıyı raporların *yazmadığı* şey veriyor:

```
S120 HELD FRAME ⭐ FİLMİN SON KARESİ — planın kendi tarifi:
  24mm · üst açı 20° · WS · fixed lockoff
  ⛔ O YÜRÜMÜYOR: DURUYOR. Yürüyüş S119'da bitti.
  ⛔ Film bir HAREKETLE değil, bir SÜREYLE biter: on saniye kadraj değişmez
  ⭐ AÇIK KALAN TEK SORU: gökte ince, soluk, PARALEL ÇİZGİLER hâlâ akıyor

ON İKİ RAPORUN SON SAHNESİ, KELİMESİ KELİMESİNE:
  ①  "1:40 — spatial jump … capsule hatch and parachute"
  ②  "S10 1:40-1:49 · Walks toward the capsule"
  ④  "S11 · Walks away toward horizon"
  ⑤  "SCENE 11 · Astronaut walking away"
  ⑨  "S11 · WS / eye / normal / BEHIND · tracking forward"
  ⑫  "EXIT · Figure walking away into the distance"

⇒ Altı mercek bağımsız olarak bir YÜRÜYEN figür gördü. Yürüyen figür
  S119 İLK ADIMLAR'dır (35mm · sırttan · göz hizası · MS).
⇒ DURAN bir figürü, 20° üst açıyı ve gökteki paralel çizgileri
  HİÇBİR RAPOR yazmadı. ⑤ ARKA PLAN'ın son sahne göğü: "blue sky
  with cirrus clouds" — çizgi yok.
```

⭐ **KONTROL — AYNI HATTIN BİR ÖNCEKİ FAZI TEMİZ:** F9 de 12 sahneliktir,
aynı 10 s ızgarasını kullanır, ve 12 sahne · 11 kesme · 120 s teslim etti.
Aynı üretim hattı geçen faz 12 klip verdi, bu faz 11.

```
⚠️ ÜÇ OKUMA VAR; RAPOR TARAFINDAN AYRILAMAZLAR. Betiğin kapısı da bunu
   söylüyor ve hüküm vermiyor:

  (a) S120 üretilmedi / kurguya girmedi / ihraçta düştü
  (b) S119 ve S120 tek klipte birleşti — o zaman da sayım 11'dir ve
      filmin son karesi plandaki kare DEĞİLDİR
  (c) mercekler yanlış saydı, makarada 12 klip var

⛔ (c) İÇİN ARİTMETİK ZAYIF, AMA ELENMİŞ DEĞİL: 12 klip × 10,0 s = 120 s.
  On iki raporun on ikisi de 109–111 s ölçtü. (c)'nin doğru olması için
  on iki merceğin SÜREYİ de aynı yönde ~10 s yanlış okuması gerekir —
  oysa süre konteynerden okunur ve sayımdan çok daha kolaydır.
  ⭐ KARŞI VAKA: THE KEPT LIGHT'ta aynı kapı ateşledi (plan 25, raporlar 20)
  ve orada doğru şık (c)'ydi — ölçüm 25 klip buldu, teslim TAMDI.
  Yani bu kapı tek başına hüküm vermez; hakem ölçümdür.

⇒ HANGİSİ OLURSA OLSUN EYLEM AYNI ve tek komutluk.

⛔ NE OLMADIĞI: bu bir QA bulgusu değildir. Merceklerin hiçbiri hatalı
   davranmadı — mod V'de "eksik" denemez, ve hepsi ellerindeki makarayı
   doğru saydı. Bu bir ÜRETİM/İHRAÇ sorusudur ve cevabı depoda değil,
   master'da ve üretim kaydındadır.
```

**AKSİYON — sahip için tek satır:** master'ın KLİP SAYISI (ve son klibinin
içeriği). `olcum_kapisi.sh` → `--olcum-sahne <n>`; ölçüm hakemdir ve üç
şıkkı tek koşuda ayırır. 11 çıkarsa (a)/(b), 12 çıkarsa (c).
⛔ Bu üçünün cevabı gelmeden **kesme listesi, REMOVE reçetesi ve yeniden
üretim UYGULANMAZ** — dört mercek zaten sahne kesmeyi öneriyor ve fazın
zaten bir sahnesi eksik.

> 🔗 **DERS 188 buradan yazıldı** — ve kapısı `rapor_kontrol.py`'ye takıldı:
> plan sahne sayısı ↔ rapor sahne sayısı. Kapı bu partide ilk koşuşunda
> ateşledi ve partiyi düşürdü.

---

# 🔴🔴 İKİNCİ BULGU — ⑥ FİZİK **10,0/10** VERDİ; YEDİ HÜCRENİN YEDİSİ KAYNAKSIZ

⑥ bu makarada tek bir kusur bulmadı ve dokuz kategorinin yedisine 10/10
yazdı. Yedi hücrenin *issue* metni, birebir aynı iki kelime:

```
Gravity & Free Fall     10/10   "no deductions"
Material Behaviour      10/10   "no deductions"
Particles & Atmosphere  10/10   "no deductions"
Scale & Measurement     10/10   "no deductions"
Rates & Timing          10/10   "no deductions"
Light & Shadow Physics  10/10   "no deductions"
Human Biomechanics      10/10   "no deductions"
```

Rubriğin kendi ④ kuralı: *"Absence of evidence is not evidence of
perfection, and a full score is a claim you did not measure."* Betiğin D186
kapısı `none` ve `flawless` kalıplarını görüyordu, `no deductions`'ı
görmüyordu. **Genişletildi; ⑥'nın 10,0'ı `—`'ye düştü — sayı taşıyan
hücre kalmadı.**

**Ve altındaki asıl arıza cetvelde:** ⑥'nın yerçekimi tahmini iki olaya
dayanıyor ve ikisi de ölçülemez:

```
L4  "sand falls from hand · ~0,05 m · ~0,1 s"  →  24 fps'de 2,4 KARE
L6  "dirt falls from knees · ~0,5 m · ~0,3 s"  →  7 kare
```

0,1 saniyelik ve 5 santimlik bir düşüşten yerçekimi ivmesi çıkmaz: zamanlama
hatası da mesafe hatası da hesaplanan büyüklükten büyüktür. ⑥ kendi
rubriğindeki *"a conviction is never finer than its ruler"* satırını taşıyor
ve onu iki kez ihlal etti — **bir kez F9'da 0,1 → 3,2 m/s² diye TWO GRAVITIES
ilan ederken, bir kez burada 10,0/10 verirken.** Aynı kök, zıt sonuç.

```
✅ YAMA — ⑥ rubriği · kategori 1'e CETVEL TABANI eklendi:
   0,3 s'den (24 fps'de ~7 kare) ya da 0,5 m'den küçük düşüş SAYI ÜRETMEZ;
   defterde UNMEASURABLE olarak durur, GRAVITY TABLE'a giremez.
   Filmin BÜTÜN düşüşleri tabanın altındaysa kategori 1 `—` alır.
```

⛔ **VE FAZIN TEK SAYISAL KİLİDİ ÖLÇÜLMEDİ.** KİLİT 48, kelimesi kelimesine:

> *"yaklaşık iki kapsül boyu yüksekliğinde bir toz perdesi kalkar ve **dört
> saniyede** tamamen çöker"*

⑥ o toz perdesini defterinin **birinci satırına** yazdı (`L1 · 0:00-0:10 ·
capsule dragging · dust cloud`) ve çökme süresini hiç ölçmedi. Sonra
Particles & Atmosphere'e 10/10 verdi. Mod V'de kilidi bilemezdi — ama
ölçebilirdi: sayı ekranda, saniye ölçülebilir.

---

# 🔴 ÜÇÜNCÜ BULGU — BİR KAPSÜL, **DÖRT FATURA**

Kapsül ile paraşütün sahneler arası yer değiştirmesi TEK olaydır. Dört
mercek dördü de puan düşürdü:

```
① KARE        Environment          7/10   −3 · "1:40 … shift from the 0:50 master shot"
② DEVAMLILIK  World State & Props  5/10   −5 · iki 🟠 satır
⑤ ARKA PLAN   Background Set&Props 6/10   −4 · "0:10 vs 0:50"
⑨ KADRAJ      Screen Geometry      4/10   −6 · "anchor object jumps left→right"

DOĞRU DAVRANAN ÜÇ MERCEK — puan düşürmeden bayrak yazdılar:
⑥ ⑦ ⑪  → "CONTINUITY LENS" · sayı yok ✅
```

Kök sebep benim yazdığım iki cümlenin çelişmesi:

```
② kategori 10:  "a thing never touched stays put"            → dokunulmamış nesne ②'nin
⑤ kategori 6:   "untouched set dressing … untouched ones are yours"  → dokunulmamış nesne ⑤'in
```

İki rubrik aynı nesne sınıfını ters yönde sahipleniyor. ⑨ ise onu kendi
**çapası** yaptı — oysa on bir sahnenin on birinde kamera farklı: dönüş
olmayan bir filmde çapa hiçbir şey ölçmez. ① ise kendi kapsam testini
çiğnedi: bulgusunda **iki zaman kodu var** ("1:40 … from the 0:50 master
shot") ve rubriği tam bunu yasaklıyor.

```
✅ YAMA — dört rubrik birden:
   ⑤ → "Bir sahnede ÖZNE olan nesne başka sahnede ARKA PLAN değildir.
        Kendi SUBJECTS EXCLUDED listene bak" (kapsül orada, S1 ve S2)
   ② → "Adı olan nesne SENİNDİR; adsız alan ⑤'in. Bir kez yaz, üç
        raporda bayrak olarak göreceksin — o TEKRAR sistemin çalışmasıdır,
        üç DOĞRULAMA değil"
   ⑨ → "Çapa bir DÖNÜŞÜN cetvelidir. Dönüş yoksa kategori 4 ve 7 `N/A`"
   ① → testin mekanik hâli: "KENDİ SATIRINDAKİ ZAMAN KODLARINI SAY.
        İkinci zaman kodunu yazdığın an devamlılık bulgusu yazmışsındır"
```

> 🔗 **DERS 189 buradan yazıldı.**

---

# 🔴 DÖRDÜNCÜ BULGU — VAR OLMAYAN BİR KESME, DÖRT RAPOR

⑦ AKSİYON'un tek 🔴'sı ve **verdict'inin tamamı** (`ACTION NEVER RENDERED`)
tek bir cümleye dayanıyor:

> *"01:36 — She gets into a crouch, and then a **cut** jumps to her already
> standing upright."*

```
1:36'da kesme YOK. Kesmeler 10 s ızgarasında: … 1:30 · 1:40.
① ve ② zaman kodlarını ayrı ayrı listeledi; ikisinde de 1:36 yok.
⛔ VE GİZLİ KESME ① KARE'NİN İŞİDİR — rubriğinin bir numaralı arıza
   kalıbı, %100 tekrar. ① o klipte Camera 10/10 verdi: kesme BULMADI.
```

Yani kesmeyi *ölçen* mercek kesme bulmadı; kesmeyi ölçmeyen mercek bir
kesme iddia etti ve hükmünü ona bağladı. Sonra **⑧ aynı saniyeyi devraldı**
(`01:36 · UNEARNED reset`), **⑨ ve ⑩ onu kendi kapsam-dışı bayraklarına
kopyaladı** — ⑨'unki kelimesi kelimesine *"The cut at 01:36"*.

Dört rubriğin dördünde de şu cümle yazılı:

> *"A flag you did not observe is not a cross-check; it is the same claim
> counted twice, and it travels faster than a real one because it costs
> nothing to copy."*

Yazılı uyarı bağlamadı. **⑦ ve ⑧'in künyeleri zaten birebir aynıydı** —
109 s · 11 kesme · 12 sahne · `--1111111111` — ve ikisi de rubriğin ⛔
zorunlu kıldığı kesme ZAMAN KODLARINI basmadı. Sayım yapılmamış,
devralınmıştır.

```
✅ YAMA — D110'un ilk BETİK kapısı takıldı (`rapor_kontrol.py` ⑦ ORTAK
   DEFTER): künyesi (kesme · sahne · şerit) birebir aynı olan ve
   çoğunluktan sapan mercek grubu → "azınlık İKİ oy değil, BİR oydur".
   Bu partide tam bir kez ateşledi: ⑦ + ⑧.
```

⚠️ **Bu, S118'de gerçek bir kusur OLMADIĞI anlamına gelmez** — ⑧'in ayrı
gözlemi (`E5 · walking away · STRAIN SHOWN: none`) ve ⑩'un bayrağı
(`stand up sequence lacks visible strain`) durmaktadır. Düşen şey
"kesme var" iddiasıdır, "kalkış bedelsiz" gözlemi değil.

---

# 🔴 BEŞİNCİ BULGU — FAZ YİNE FİLM SANILDI, VE KAPI **YAZILIYDI AMA BAĞLAMIYORDU**

F9'da yazılan D185 kapısı bu partide ateşledi ve doğru hücreleri adlandırdı:

```
④ HİKAYE   Hook · Structure & Pacing · Ending · Retention Risk   (4 hücre)
⑫ HOOK     Hook Question · Stakes · Plateau · Peak · Exit        (5 hücre)
⑨ KADRAJ   Rhyme Pair                                            (1 hücre)
```

**Ama hücreleri ortalamadan DÜŞÜRMÜYORDU.** Kapı metni *"Bu hücreler `—`
olur, ortalama yeniden hesaplanır"* diyordu; kod yalnız uyarı basıyordu.
Yazılı ama bağlamayan kapı — deponun kendi klasik arızası [D74].

```
✅ DÜZELTİLDİ. Etkisi:
   ④  6,0 → 6,0 (n 9 → 5)     ⑫  7,5 → 🚨 GEÇERSİZ
   ⑨  4,5 → 5,3  ⭐ SKOR YÜKSELDİ — faz, sahip olmadığı bir kafiye
      çifti yüzünden cezalandırılıyordu. RHYME BROKEN verdict'i düştü.
```

Ve fazın kendi rubriği **hâlâ yok**: `FAZ_01`…`FAZ_08` sekizinde var,
F9'da yok, F10'da yok. Bu, iki fazda üst üste alınan aynı karardır.

---

# 🟠 ALTINCI BULGU — KİLİT 49'UN BEŞ AĞIRLIK KANITI: EN FAZLA **1/5**

F9'da üç kanıt vardı ve 0/3 ölçüldü [D187]. Bu fazda beş oldu:

```
① SAÇ aşağıda, yüze düşüyor          → hiçbir mercek bakmadı
② SAAT KAYIŞI sarkık                  → ② kayışı gördü ("weathered leather
                                         strap") ama SARKIK olup olmadığını
                                         yazmadı — kimlik olarak baktı
③ KOLLAR yükselmiyor                  → hiçbir mercek bakmadı
④ NEFES artık göğsü KALDIRIYOR        → ⑧ "Breath & Recovery 8/10" verdi ama
   (0g'de görünmüyordu)                 göğüs hareketini ölçmedi
⑤ KAS TİTREMESİ (S114 · S118)         → ⑧ E4'te YOKLUĞUNU buldu (S117'de,
   filmde ilk kez                       ⑬ kalıbı 🟠) · ⑩ S118 için bayrak yazdı
```

⇒ **Beşten dördü hiçbir merceğin kapsamına girmiyor.** Kanıt ⑤ kısmen
tutuldu; o da kilidin yazdığı sahnede değil komşusunda.

D187'nin BETİK yarısı hâlâ ⬜ AÇIK ve bu ikinci vakadır. Kapı PLAN
tarafındadır: **her taşıyıcı kilidin yanına onu ÖLÇECEK merceğin adı
yazılır.** KİLİT 49 beş kanıt sayıyor ve beşinin de yanında mercek adı yok.

---

# 🟠 YEDİNCİ BULGU — SES: **İKİ TANIK, ON ÇEKİMSER**

```
③ SES   "none — room tone present" · tam ambiyans haritası:
        çöl rüzgârı · ayak sesi · kumaş hışırtısı · 1:22 saat kurma tıkırtısı
① KARE  "none — room tone present" · 1:22 Foley senkron kayması 🟡
─────────────────────────────────────────────────────────────────
④⑥⑦⑧⑨⑩⑪⑫  "none — nothing audible to me"   (sekiz mercek)
```

① ve ③ **bağımsız olarak aynı saniyede aynı kusuru** yazdı (1:22 · saat
kurma tıkırtısının senkronu). İkisi de "room tone present" dedi. Sekiz
mercek hiçbir şey duymadı.

⛔ **Bu bir çelişki değil, iki TANIK ve on ÇEKİMSERdir.** Çapraz kapı
`LINES HEARD` satırlarını yan yana koyar; "nothing audible to me" bir oy
gibi görünür ama bir gözlem değildir — sesi hiç açmamış bir merceğin
sessizliğidir. Sekizin sekizi aynı şeyi yazınca dosya sessiz sanılır.

Ve plan ③'ü destekliyor: F10'un REPLİK'i 0/12, S120 *"yalnız rüzgâr"*,
müzik S119 sonunda bitiyor. ③'ün duyduğu şey planın yazdığı şeydir.

```
⬜ AÇIK — tek komutla kapanır, ama depo DIŞINA çıkar (sahip kararı):
   ffprobe -v error -select_streams a -show_entries stream=codec_name,channels …
   ⛔ DOĞRULANMADAN SES DERSİ YAZILMAZ [D110 kuralı].
```

---

# ✅ SEKİZİNCİ — SAĞLAM BULGULAR (üretime giden)

Parti geçersiz olsa da bu gözlemler kapı düşürmedi ve tek mercek tarafından,
kendi kapsamında, kaynağıyla yazıldı:

```
🔴 1:20 · S117 SAAT KURULUR — başparmak saatin kurma kolunun İÇİNE geçiyor
        [① · contact morphing]
        ⛔ EN PAHALI KUSUR: S117 ÇEHOV 2'nin ödemesidir. Film boyunca
           hareket etmemiş tek mekanizmanın harekete geçtiği an, elin
           mekanizmayla kaynaştığı andır. KİLİT 51 bu karede duruyor.
🟠 0:30 ↔ 1:00 · alındaki kırmızı çizik kayboluyor        [② · tek yönlü kural]
🟡 1:00 ↔ 1:30 · fermuar kendiliğinden yukarı kapanıyor   [②]
🟠 1:12 · düşen toprak topak hâlinde, zerre ayrışması yok [① · KİLİT 48'in
        "kenarındaki tek tek zerreler görülür" cümlesinin karşılığı yok]
🟠 1:20 · kaba efordan hemen sonra kusursuz ince motor kontrolü, titreme yok
        [⑧ · ⑬ kalıbı] ⭐ KİLİT 49 ⑤'in tam karşılığı
🟠 1:40 · yürüyüşte bedel yok: simetrik, dinlenmiş, sendelemesiz
        [⑧ · E5] ⚠️ plan S119'da "adımlar düzensiz · bir kez sendeler ve
        düzeltir" diyor — bu, kilidin karşılanmadığının kaydıdır
🟡 0:20 · kapsül içi ambiyans dış ses karakterini koruyor [③]
🟡 1:22 · saat kurma Foley'i görüntüyle senkron değil     [③ + ①]
```

⭐ **VE ÜÇ ŞEY DOĞRU ÇIKMIŞ:** ⑪ IŞIK iki bölge boyunca anahtar yönü,
gölge sertliği ve renk sıcaklığını sabit buldu (`LIGHT JUMPS: 0`) — bu hatta
nadir. ⑤ zemin dokusunun kaynamadığını ve ufkun sabit kaldığını yazdı.
⑨ S10'u `ground level` okudu: **KİLİT 52'nin alt açısı kadrajda.**

---

# 🔧 AKSİYON

## KADEME 1 — sahip · başka hiçbir şeyden önce

```
⬜ 1. MASTER'IN KLİP SAYISI. Plan 12 sahne yazıyor, on iki rapor 11 klip
      gördü. S120 HELD FRAME üretildi mi · kurguya girdi mi · ihraçta mı
      düştü? ⛔ Cevap gelmeden hiçbir kesme/yeniden üretim kararı verilmez.
⬜ 2. SES AKIŞI (tek ffprobe). ③ ve ① ses duydu, sekiz mercek duymadı.
```

## KADEME 2 — depo · yazılmayı bekleyen

```
⬜ 3. FAZ_10_QA_PROMPT.md — ve FAZ_09_QA_PROMPT.md. İki fazda üst üste
      genel rubrik koşuldu; rubriksiz faz yeniden denetlenmez [D185].
⬜ 4. KİLİT 49'un beş kanıtının yanına ÖLÇEN MERCEĞİN ADI [D187 · BETİK yarısı].
⬜ 5. YERCEKIMI_QA_SPEC.md — D117 borcu; onsuz film "yazımı tamam" değil.
```

## KADEME 3 — ✅ BU TURDA YAPILDI

```
✅ D188 kapısı: plan sahne sayısı ↔ rapor sahne sayısı (rapor_kontrol.py ①.9)
✅ D186 kapısı genişletildi: "no deductions" da kaynaksızdır → ⑥ 10,0 → —
✅ D185 kapısı BAĞLADI: hücreler artık ortalamadan düşüyor
✅ D110'a ilk BETİK kapısı: ⑦ ORTAK DEFTER (künye birebir + çoğunluktan sapan)
✅ Dört rubrik yaması [D189]: ⑤ özne/arka plan sınırı · ② adı olan nesne ·
   ⑨ çapa dönüş ister · ① iki zaman kodu testi
✅ ⑥ rubriğine CETVEL TABANI: 0,3 s / 0,5 m altı olay sayı üretmez
```

## ⛔ UYGULANMAYACAK — ve niçin

```
❌ ④'ün kesme listesi (S2 ve S5'i kes, −30 s → 91 s)
   → faz zaten bir klip EKSİK. Ve S2 = S110 SESSİZLİK, planın iki insansız
     sahnesinden biri; S5 = S113 DÜZLÜK ⭐ ÖLÇEK 1:10, fazın üç adet
     1:10 karesinden biri. İkisi de yapısal.
❌ ⑫'nin "Cut S5 or S6" plato reçetesi → aynı sebep · ayrıca ⑫ GEÇERSİZ.
❌ ⑨'un RHYME BROKEN hükmü → faz filmin bookend'ini taşımaz [D185].
❌ ④'ün "S5'i ufuktaki bir anomali POV'una çevir" reçetesi
   → SU 0 KARE · CANLI 0 KARE · fazın konusu ağırlıktır, hedef değil.
❌ ⑦'nin "1:36'daki kesme" hükmü → o kesme yok (dördüncü bulgu).
❌ ⑥'nın 10,0/10'u → yedi kaynaksız hücre; betik `—` yaptı.
```

---

```
BAĞLANTILI DERSLER
yeni  D188 (plan↔rapor sahne sayısı · teslim kapısı) · D189 (adı olan nesne)
tekrar D185 (2) · D186 (2) · D110 (+1, ilk betik kapısı) · D187 (2) · D137 (6)
kök    D46 (süre muhasebesi) · D74 (kaydı olmayan kapı) · D117 · D131 · D161
```
