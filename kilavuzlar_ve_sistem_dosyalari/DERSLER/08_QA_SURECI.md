# 📚 DERSLER — QA Süreci

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **QA Süreci** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🔴 DERS 51: KAPI OKUNDU, MODEL KENDİNE MUAFİYET YAZDI

**Kaynak:** "The Inverted" VIDEO_QA (01.08.2026, Genel 4/10) — STEP 0 —
`"As the exact prompt text files were not supplied, I am filling this gate
based on the visual evidence and title provided in the brief"`

**Sorun:** Kapı, tam olarak bunu yasaklamak için yazılmıştı:

```
RUBRİK DİYOR   "by copying from the scene's prompt file, not from the
               video and not from memory" · uyuşmazlıkta DUR
RAPOR YAPTI    SPEC'i videodan doldurdu, "not" diye başlayan bir
               muafiyet cümlesi yazdı ve puanlamaya devam etti
```

Bu, Bulgu 7'deki dört bozuk çalıştırmadan **farklı ve daha kötü** bir sınıf.
Onlarda kapı **yoktu**. Burada kapı vardı, model onu **okudu, alıntıladı ve
kendine istisna tanıdı.** Bir prompt satırının engelleyemeyeceği hata tipi.

**En pahalı sonucu — inceleme döngüsel hale geliyor:** SPEC videodan
doldurulduğunda film kendi kendisiyle karşılaştırılır. "Tutarlı mı?"
sorusunun referansı yine videodur; her bulgu totolojiktir.

**ÇÖZÜM — KAPI PROMPT SATIRI DEĞİL, ÇALIŞTIRMA ÖN KOŞULUDUR:**

```
1. QA ÇALIŞTIRMA SATIRI — dosya yolu elle yapıştırılır, "varsa" değil:
   VIDEO_QA  +  yatay_2_4_dk_filmler_uzay/<FILM>.md  +  <klip>

2. TEK CÜMLELİK KURAL, RUBRİĞİN EN ÜSTÜNE:
   "A SPEC block filled from the video is an EMPTY SPEC block.
    If the prompt file is not in front of you, you are not reviewing —
    you are describing."

3. FİLM KİMLİĞİ ÖNCE DOĞRULANIR: rapordaki FILM adı 38 filmlik
   kütüphanede yoksa çalıştırma başlamaz. "The Inverted" adında bir
   film YOK — en yakın eşleşme THE_INVERSION_PLANET_FILM.md.
```

> 🔗 Bulgu 7 ile birlikte okunur. 7 "kapı ekle" dedi; 51 "kapı yetmedi" diyor.

---

## 🔴 DERS 52: DOĞRULANMAMIŞ ALANDAN BLOCKER ÜRETİLEMEZ — ÖNCÜL HATA SANILIYOR

**Kaynak:** "The Inverted" VIDEO_QA — Karakter 3/10 —
`0:48 🔴 saç değişiyor` · `1:07 🔴 suit drift` · `1:28 🔴 locomotion mismatch`

**Sorun:** Raporun **kendi künyesinde** SUIT, GRAVITY ve LOCOMOTION alanları
`[UNVERIFIABLE]` yazıyor. Aynı rapor bu üç alandan üç 🔴 BLOCKER üretti.
Rubrik "alan boşsa o kontrol UNVERIFIABLE'dır, puanlama" diyor; model
**alanı** doğrulanamaz işaretledi, **kontrolü** yine de puanladı.

Kütüphanedeki en yakın eşleşme (`THE_INVERSION_PLANET_FILM.md`) ile
karşılaştırıldığında hata iki yöne birden gidiyor:

| Rapor ne dedi | Plan dosyası ne diyor | Sonuç |
|---|---|---|
| `1:28` 🔴 yerçekimi vektörü çevreyle uyuşmuyor | satır 150-158 GRAVITY VECTOR RULE — vektör ters dönüyor, **filmin öncülü bu** | öncül hata sanıldı |
| `0:48` 🔴 saç modeli değişiyor | satır 114-116 saç kısa ve bağlı, **yönü değişsin diye tasarlandı** | tasarım hata sanıldı |
| `1:48` 🟠 tablet tutuşunda parmak kaynaması | satır 133 **HANDS ALWAYS EMPTY** — elde cihaz olamaz | gerçek ihlal normalleştirildi |

Son satır en tehlikelisi: rapor, **var olmaması gereken bir nesnenin render
kalitesini** eleştirdi. Doküman olmadan bakan göz, ihlali "verili" kabul edip
onun içindeki kusuru arıyor.

**ÇÖZÜM — SEVERITY, GROUND TRUTH'A BAĞLANIR:**

```
UNVERIFIABLE alan  →  o kategoride en fazla 🟡 GÖZLEM yazılır.
                      severity YOK · skor YOK · REGENERATE kararı YOK.

Rapor satırı şu biçimi alır:
"1:07 — 🟡 GÖZLEM (UNVERIFIABLE) — tulum gri/turuncudan beyaz EVA'ya
 geçiyor. SUIT alanı doldurulmadığı için ihlal olup olmadığı
 belirlenemez. Plan dosyası gerekiyor."
```

**Kural:** 🔴 BLOCKER, "kural ihlal edildi" demektir. Kuralı görmeden
ihlal yazılamaz.

---

## 🔴 DERS 53: GİRDİSİZ ÇALIŞTIRMA BOŞ ŞABLON ÜRETİYOR — SIFIRLAR TEMİZ FİLM GİBİ OKUNUR

**Kaynak:** MANTIK_QA (01.08.2026) — video eklenmedi — çıktı: tam biçimli
rapor iskeleti · `🔴 BLOCKER: 0 🟠 MAJOR: 0 🟡 MINOR: 0` · `OVERALL: -/10`

**Sorun:** Hiçbir kare izlenmeden, geçerli bir raporla **aynı yapıya sahip**,
kopyala-yapıştıra hazır bir belge üretildi: sahne envanteri tablosu, lokasyon
haritası, sürüklenme haritası, sıfırlanmış severity sayacı.

Bu projede raporlar tablolara taşınıyor (`03_HIKAYE_KALITE_TABLOSU.md`,
`04_MANTIK_KALITE_TABLOSU.md`). Üç hafta sonra bu iskelete bakan biri —
veya onu ayrıştıran bir betik — **sıfır blocker'ı "temiz film" olarak okur.**

```
Slow Stone  →  var olmayan İÇERİĞİ uydurdu ("Faz 5")
Bu rapor    →  var olmayan RAPORUN BİÇİMİNİ uydurdu
```

İkincisi daha sinsi: içerik uydurması yanlış bir cümledir, biçim uydurması
**geçerli görünen boş bir kayıttır.**

**ÇÖZÜM — INPUT YOK PROTOKOLÜ, dört rubriğin de en üstüne:**

```
INPUT MISSING — NO REPORT PRODUCED
Required : [video dosyası / plan dosyası yolu]
Received : [hiçbir şey]

No scores. No tables. No placeholders. No "[Pending]".
This block is the ENTIRE output. A template filled before the data
arrives is a fabricated report.
```

**Kural:** Şablon veriden önce doldurulmaz. Boş şablon üretmek rapor
üretmektir ve sisteme sahte satır sokar.

---

## 🔴 DERS 54: "DOKÜMAN YOK" İLE "DOKÜMAN ÇELİŞİYOR" AYNI KAPIDAN ÇIKIYOR

**Kaynak:** SENARYO_QA (01.08.2026) —
`SPEC MISMATCH — REVIEW ABORTED · Field: Plan Document · Stated: Video Only
Provided · Document says: MISSING`

**Sorun:** Kapı **tuttu** — hiçbir şey puanlanmadı, Low Power'a göre bu bir
kazanç. Ama çıktı iki yerden bozuk:

**(a) "Document says: MISSING" kendi içinde çelişki.** O alan "dokümanı
okudum, şöyle diyor" demektir. Rubrikte tek bir DUR kodu var ve iki farklı
duruma birden kullanılıyor:

```
SPEC MISMATCH   doküman var, künye ile çelişiyor   → FİLM durur, ciddi
INPUT MISSING   doküman hiç gelmedi                 → ÇALIŞTIRMA durur,
                                                      5 saniyede düzelir
```

İkisi aynı kodla raporlanınca, ucuz bir iş akışı kazası pahalı bir film
bulgusu gibi arşivleniyor.

**(b) Dosya aranmadı.** `yatay_2_4_dk_filmler_uzay/THE_INVERSION_PLANET_FILM.md`
depoda duruyor. Bulgu 7'nin Inversion satırında aynı hata yazılıydı:
*"plan doc unsupplied dedi — oysa dosya depoda."* **Aynı hata üst üste ikinci
kez.** Model dokümanın yokluğunu varsayıyor, doğrulamıyor.

**ÇÖZÜM — DUR KODU İKİYE AYRILIR + ARAMA ZORUNLU:**

```
INPUT MISSING — RUN STOPPED (this is not a film finding)
Searched : yatay_2_4_dk_filmler_uzay/  ·  yatay_3_5_dk_filmler/  ·  …
Required : <FILM>/<FILM>_PLAN.md  veya  <FILM>_PLANET_FILM.md
Action   : rerun with the path attached.
No score is written. No CONDITIONAL row is added. This run did not happen.
```

**Kural:** Kayıp doküman **filmin** kusuru değildir. Filmin satırına ŞARTLI
puan yazılmaz; çalıştırma hiç olmamış sayılır ve sayıma girmez.

---

## ⚠️ 51-54 HAKKINDA — ÜÇÜNCÜ DERS SINIFI: QA'NIN KENDİSİ

```
Ders 1-45    PROMPT hatası    → çözüm: prompt'a cümle eklenir
Ders 46      KURGU hatası     → çözüm: kurgu masasında
Ders 47-50   PLAN hatası      → çözüm: plan dosyasında ortak sabit
Ders 51-54   QA HATASI        → çözüm: ÇALIŞTIRMA biçiminde ← YENİ
```

51-54'ün hiçbiri filmle ilgili değil. Dördü de **ölçme aletinin kendisiyle**
ilgili ve dördü de tek bir kök nedene çıkıyor: *rubrik metni, çalıştırma
disiplininin yerini tutmuyor.*

---

## 🚨 ÖLÇÜM — 01.08.2026: ÜÇ MERCEK ARKA ARKAYA ÇALIŞTI, ÜÇÜ DE GİRDİSİZ

> Bu bir ders değil, **dersler hakkında bir ölçüm.** Numarası yoktur.

| Mercek | Girdi | Kapı | Sonuç | Geçerli mi |
|---|---|---|---|:---:|
| VIDEO_QA | plan yok | okundu, **muafiyet yazıldı** | 4/10 + 4 BLOCKER | ❌ |
| SENARYO_QA | plan yok | **tuttu**, durdu | çıktı yok | ⭕ boş |
| MANTIK_QA | video yok | **rubrikte yok** | boş iskelet + 0 blocker | ❌ |

```
ÇALIŞTIRMA          3
GEÇERLİ SKOR        0        ← üçünden hiçbiri tabloya girmemeli
KAPININ TUTTUĞU     1 / 2    (MANTIK_QA'da kapı hiç yok)
```

**İkinci bir aritmetik kusur:** VIDEO_QA raporu başlıkta `4/10` yazıyor, ama
kendi kategori skorlarının ortalaması `4.86`. Low Power'ın 7.0 / 7.1
kusurunun aynısı — **tek film için iki sayı.** Puan bir kez hesaplanıp iki
yere aynı yazılmalı.

**Yapılacak:** Bu üç çalıştırma `00_INDEX.md` Bulgu 7 tablosuna eklendi.
Hiçbiri kalite tablolarına satır olarak girmeyecek.

---

---

## 🔴 DERS 60: DENETÇİ FİLMİN KÜNYESİNİ VİDEODAN UYDURUYOR — EKRANDAKİ YAZI KÜNYE SANILIYOR

**Kaynak:** SHORTS_QA çalıştırması, 03.08.2026 — rapor "THE SLOW STONE'un
eleştirisi" diye teslim edildi, künyesinde şu satır vardı:

```
FILM: The Silent Reckoning   (inferred from on-screen title)
SOURCE DOCUMENT: NOT PROVIDED
SPEC BLOCK PROVIDED: no — all 23 fields blank
STEP 0.5 GATE: FAILED
```

**Sorun:** SPEC yoksa denetçi filmin **adını bile** bilmez. Bu rapor adı
ekranda gördüğü jenerik kartından okudu ve künye yaptı. Sonuç: rapor,
depoda hiçbir belgede geçmeyen bir isim altında kalite tablosuna girmeye
hazır hâlde teslim edildi ve gerçek filmin kaydıyla asla eşleşemezdi.

**En sinsi tarafı bu:** filmin **ihlali** (ekranda metin — Ders 9/34/45)
raporun **kimliği** hâline geldi. Yani en kirli sahne, künyenin kaynağı oldu.

**Ders 51/53'ten farkı:**

```
Ders 51   kapı okundu, model kendine MUAFİYET yazdı
Ders 53   girdi yoktu, model BOŞ ŞABLON doldurdu
Ders 60   girdi yoktu, model künyeyi VİDEODAN İCAT ETTİ
          → 51 ve 53 raporu değersiz yapar; 60 raporu YANLIŞ FİLME BAĞLAR
```

Boş bir rapor zararsızdır — atılır. Yanlış filme bağlanmış bir rapor o filmin
kaydına yazılır ve kalıcı olur.

**ÇÖZÜM — SAYISAL KAPI, iki zorunlu alan:**

```
FILM alanı yalnız İKİ girdiden doldurulur:
  1. SOURCE DOCUMENT = depodaki .md dosyasının TAM YOLU
  2. o dosyanın 1. satırındaki başlık, birebir kopyalanmış

İkisinden biri yoksa:
  FILM: UNIDENTIFIED
  → QUALITY TABLE ROW ÜRETİLMEZ (0 satır)
  → rapor 02_HAM_RAPORLAR/ altına "UNIDENTIFIED_<tarih>" adıyla düşer,
    hiçbir film kaydına işlenmez

⛔ Ekranda görülen hiçbir yazı künye kaynağı değildir. Bu seride ekranda
   yazı OLMAMASI gerekiyor; görülen yazı bulgudur, kimlik değil.
```

---

## 🔴 DERS 62: SKOR RAPORUN KENDİ TABLOSUNDAN ÜRETİLEMİYOR

**Kaynak:** SHORTS_QA çalıştırması, 03.08.2026 — `OVERALL SCORE: 5.7/10`

**Sorun:** Rapor 16 kategoriden 7'sini puanladı, 9'unu UNVERIFIABLE/N/A
bıraktı. Puanlananlar:

```
Camera 6.0 · Lighting 7.0 · Particles 3.5 · Vertical 8.5
Safe Zone 6.0 · Hook 5.0 · Retention 7.0
                                    toplam 43,0 ÷ 7 = 6,14
rapor yazdı:                                       5,7
```

Sayı raporun kendi tablosundan çıkmıyor. Dahası, kalite tablosu satırında
özet tablosunda **hiç bulunmayan** bir kategori var:

```
| ... | Motion 5.5 | **5.7/10** |
        ↑ SCORES SUMMARY'de "Motion" diye bir kategori yok
```

**Neden ölümcül:** Bu projede skorun tek gerçek kaynağı
`FILM_QA_RAPORLARI/00_INDEX.md`. AGENTS.md §6 zaten web panelinin ortalamasının
yanlış olduğunu kaydediyor — **aynı hastalığın ikinci kaynağı burada:** bu kez
yanlış sayı panelde değil, raporun kendisinde üretiliyor ve tabloya elle
taşınacak. Bir kez girdiği anda hangi kategoriden geldiği geri izlenemez.

**ÇÖZÜM — ARİTMETİK KAPI, skor yazılmadan önce:**

```
Rapor OVERALL SCORE satırından ÖNCE üç sayıyı açık yazar:

  PUANLANAN KATEGORİ SAYISI:  __        (UNVERIFIABLE ve N/A hariç)
  PUANLARIN TOPLAMI:          __,_
  BÖLÜM:                      __,_ ÷ __ = __,_

Kurallar:
  · UNVERIFIABLE ve N/A kategoriler bölmeye GİRMEZ ve 0 sayılmaz
  · QUALITY TABLE ROW'daki her kategori adı SCORES SUMMARY'de birebir
    bulunmak zorundadır; bulunmayan sütun için satır üretilmez
  · Puanlanan kategori sayısı 16'nın yarısının altındaysa (< 8) satır
    "KISMİ" işaretiyle yazılır ve ortalama tabloya GİRMEZ
```

> **Çıkarım:** Bir skoru kabul etmeden önce, raporun kendi tablosundan
> yeniden hesapla. Tutmuyorsa hata skorun büyüklüğünde değil, raporun
> güvenilirliğindedir — o rapordaki hiçbir sayı taşınmaz.

---

## 🔴 DERS 60: DUR KODU ÇIKTI ŞABLONUNDA ALAN OLAMAZ — MODEL ALANI DOLDURUP DEVAM EDİYOR

**Kaynak:** The Herd SENARYO_QA (03.08.2026) — raporun kendi başlığı:
`SPEC VERIFIED AGAINST PLAN DOC: no — abort` — ve ardından **10 kategori
puanı + kesme listesi + takip tablosu satırı.**

**Sorun:** Rubrik "beş kontrolden biri tutmazsa DUR, puanlama" diyor. Model
durmadı. Ama Ders 51'den **farklı bir mekanizmayla:**

```
DERS 51   model kapıyı okudu, kendine gerekçeli MUAFİYET yazdı
          ("as the files were not supplied, I am filling this gate based on...")
DERS 60   model gerekçe bile yazmadı. Şablondaki alanı DOĞRU cevapla
          doldurdu ("no — abort") ve bir sonraki satırdan devam etti.
```

Sebep rubriğin kendi çıktı şablonunda:

```
SENARYO_QA_CRITIQUE_PROMPT.md · OUTPUT FORMAT bloğu, satır 357:
  SPEC VERIFIED AGAINST PLAN DOC: [yes — all 5 checks passed / no — abort]
```

**"abort" burada bir KOMUT değil, bir SEÇENEK.** Şablonun içindeki bir alan
üretimi durduramaz — model şablonları doldurur, şablon onun görevidir.
Alan ne kadar net yazılırsa yazılsın, doldurulacak bir kutu olarak kalır.

Aynı rapor ikinci kez düştü: `DECLARED EMOTIONAL PEAK: ABSENT` yazdı,
"Emotional Arc ve Structure UNSAFE" dedi — **ve o iki skoru yine ortalamaya
kattı.** UNSAFE bir etiket olarak kaldı, davranışa dönüşmedi.

**ÇÖZÜM — DUR BLOĞU ÇIKTININ TAMAMIDIR:**

```
1. ÇIKTI ŞABLONUNDAN alan SİLİNİR. Doğrulama satırı bir sonuç değil,
   çalıştırma ön koşuludur; sonuç bloğunda yeri yoktur.

2. DUR durumu şu bloğun KENDİSİDİR ve başka hiçbir şey yazılmaz:

   SPEC MISMATCH — RUN STOPPED
   Field    : [ad]
   Stated   : [x]
   Document : [y]  (dosya yolu)

   No scores. No tables. No scene verdicts. No tracking row.
   This block is the ENTIRE output.

3. UNSAFE ETİKETİ SKOR ÜRETEMEZ. Bir kategori UNSAFE işaretlendiyse
   o kategoriye SAYI yazılmaz, ortalamaya girmez, tabloya boş gider.
   Etiket davranışa bağlanmazsa dekordur.
```

**AYIRICI TEST:** Ders 53 bu biçimi (`bu blok çıktının TAMAMIDIR`) zaten
INPUT MISSING için yazmıştı. 60, aynı biçimin **SPEC MISMATCH** için de
zorunlu olduğunu ve reçetenin rubriklere hiç uygulanmadığını gösteriyor.

> 🔗 Ders 51 (muafiyet yazma) · 53 (boş şablon) · 54 (dur kodu ayrımı) ile
> aynı sınıf: **QA'nın kendisi.** Dördü de tek kök nedene çıkıyor —
> rubrik metni, çalıştırma disiplininin yerini tutmuyor.

---

## 🔴 DERS 61: DERLEMEDE SAHNE SINIRI GİZLİ KESME SANILIYOR — HER MONTAJ BLOCKER ÜRETİR

**Kaynak:** The Herd VIDEO_QA (03.08.2026) — `TOP 3 CRITICAL ERRORS` birinci
sıra: `0:07 — 🔴 BLOCKER — Camera cuts from exterior landing directly to
interior cockpit.`

**Sorun:** Film 15 sahnelik bir **montaj** ve sahneler **ayrı ayrı**
üretiliyor — bu, Ders 1'in kendi mimarisi:

```
DERS 1'İN ÇÖZÜMÜ    "Her sahne AYRI 10 saniyelik video. Asla birleştirme."
MONTAJIN SONUCU     Sahneler arasında kesme OLMAK ZORUNDA.
VIDEO_QA'NIN KURALI "ANY hidden cut is automatically a 🔴 BLOCKER."
```

0:07, S0 → S0.5 sınırıdır. Yani rubrik, **kendi mimarimizin zorunlu
sonucunu** en yüksek severity ile raporladı. Bir montajda bu kural her
sahne sınırında tetiklenir: 15 sahnelik film = 14 sahte BLOCKER.

Ve bedeli sadece gürültü değil: rapor `VERDICT: REGENERATE` verdi ve
`Camera 3/10` yazdı. **Yanlış kategori cezalandırıldı** — kamera sahne
içinde kusursuz sabit olabilirdi.

**ÇÖZÜM — İKİ MOD, İKİ KURAL:**

```
SCENE: <numara>        → TEK KLİP MODU
  Gizli kesme kuralı tam güçle geçerli. Klip içindeki HER kesme BLOCKER.

SCENE: Compilation     → DERLEME MODU
  Kesmeler beklenir. Yalnız şu ikisi bulgu sayılır:
    · bir sahnenin İÇİNDE kesme  → 🔴 BLOCKER
    · plan dosyasındaki sahne sınırıyla EŞLEŞMEYEN kesme → 🟠 MAJOR
  Sahne sınırlarıyla eşleşen kesmeler RAPORLANMAZ.
  ⚠️ Derleme modunda kesme değerlendirmesi PLAN DOSYASI ister.
     Plan yoksa bu kontrol UNVERIFIABLE'dır — BLOCKER üretmez.
```

**İKİNCİ BULGU — Ders 52 fazla künt:** Aynı rapor künyesinin tamamını
`UNVERIFIABLE` işaretledi ve 3 BLOCKER üretti. Ders 52 buna "hiç severity
yazma" demişti. Ama üç bulgunun ikisi künyeden bağımsızdır:

```
KÜNYE-BAĞIMLI kontrol      künye yoksa UNVERIFIABLE, severity YOK
  tulum rengi · yerçekimi · kamera hareketi · ışık kaynağı · eğim açısı
  → "yanlış" demek için kuralı görmek gerekir

KÜNYE-BAĞIMSIZ kontrol     künye olmadan da severity YAZILIR
  fazla parmak · el-yüzey kaynaşması · ekranda metin/altyazı ·
  yüz morphu · nesne içinden geçme · donmuş parçacık
  → bunlar SERİ kuralıdır, film künyesi değil; hiçbir filmde meşru değil
```

The Herd'ün `0:38 el kaynaşması` ve `1:39 fazla parmak` bulguları künye
olmadan da geçerlidir ve atılmamalıdır. `0:07 kesme` bulgusu ise
künye-bağımlıdır (sahne sınırı nerede?) ve künye yokken üretilmemeliydi.

> 🔗 Ders 1 (gizli kesme) ve Ders 52 (doğrulanmamış alandan blocker) ile
> birlikte okunur. 61 ikisinin arasındaki boşluktur: 1 tek klibi korur,
> 52 künyeyi korur, ama **derlemenin kendisi** hiçbirinde tanımlı değildi.

---

## 🔴 DERS 64: DENETÇİ KENDİ EKSİK GİRDİSİNİ YAPIMIN KUSURU YAZDI, SONRA YERİNE SAHTE BIBLE KOYDU

**Kaynak:** SHORTS_QA 05.08.2026 (THE HALF SKY künyeli rapor) — iki satır:

```
BULGU:  "🟠 MAJOR — No-Bible production (Lesson 55) —
         Wardrobe reinvented every scene (white helmet to bubble to red)"

ÖNERİ:  "Costume drift | Character Prompt | Lock exact suit details:
         orange spacesuit, white helmet shell, clear visor across all scenes."
```

**Sorun (a) — teşhis ters çevrildi.** Ders 55 "yapımın Bible'ı yok" demektir.
`THE_HALF_SKY_DIKEY_SHORTS.md` dosyasında **978 karakterlik** karakter bloğu
var ve 6 görsel promptun 6'sında kısaltmasız tekrarlanıyor; dosya bunu ayrıca
ölçüp yazmış. Bible eksik değildi — **denetçinin elinde** yoktu. Denetçi kendi
girdi eksiğini yapımın kusuru olarak dosyaladı.

**Sorun (b) — bu asıl olanı.** Boşluğu boş bırakmadı, **doldurdu:**

```
Gerçek Bible (dosyadan)              Öneri tablosunun yazdığı
──────────────────────────────       ─────────────────────────
OXIDE-RED pressure suit          →   "orange spacesuit"
matte pewter-grey joint rings    →   (yok)
FULLY TRANSPARENT SEAMLESS VISOR →   "clear visor"
kask kabuğu rengi TARİF EDİLMEZ  →   "white helmet shell"   ← icat
```

Rubriğin kendi cümlesi: *"Your PROMPT UPDATE RECOMMENDATIONS table is the most
valuable output — it is pasted straight back into the generation prompt."*
Yani bu tablo bir **gözlem** değil, bir **yazma yoludur.** SPEC'i olmayan bir
denetçinin en değerli çıktısı, gerçek Bible'ın üzerine yazma kanalıdır. Öneri
uygulansaydı film oksit kırmızısından turuncuya döner ve Bible'da hiç olmayan
beyaz bir kask kabuğu 6 sahneye kilitlenirdi.

**Ders 52'den farkı:** 52 "doğrulanmamış alandan BLOCKER çıkmaz" der —
bulgunun ağırlığını sınırlar. 64 bulguyu değil, **düzeltmeyi** konuşuyor:
doğrulanmamış bir çalıştırma, bulgu üretmese bile prompt'a değer yazabiliyor.

**ÇÖZÜM — ÖNERİ TABLOSU KOPYALAR, ÜRETMEZ:**

```
PROMPT UPDATE RECOMMENDATIONS tablosunun "Concrete change" hücresinde
geçen her karakter/dünya/ölçek değeri, SPEC BLOĞUNDAN BİREBİR kopyalanmış
olmak zorundadır. Kendi cümlenle yazdığın her renk, malzeme, ölçü ve
parça adı icattır.

  SPEC BLOK = no     → tablo Character · World · Scale satırı İÇEREMEZ.
                       Bu üç konuda yazılabilecek tek satır şudur:
                       | Bible doğrulanmadı | — | rerun with document |
  SPEC BLOK = yes    → her değerin yanına kaynak satırı yazılır:
                       "OXIDE-RED (Character Bible, satır 1)"

⛔ Bir eksikliği "yapımda Bible yok" (Ders 55) diye dosyalamadan önce:
   dosyayı ARADIN MI? Ders 55 yalnız dosya AÇILDIKTAN ve içinde karakter
   bloğu BULUNMADIKTAN sonra yazılabilir. Aranmamış bir dosya, olmayan
   bir dosya değildir. [Ders 54(b) · üçüncü tekrar]
```

---

## 🔴 DERS 65: UYDURULAN KÜNYE GERÇEK BİR FİLMLE ÇAKIŞTI — YANLIŞ SATIR DOĞRU DOSYAYA YAZILIR

**Kaynak:** SHORTS_QA 05.08.2026 — `FILM: THE HALF SKY [Inferred from S7]`,
yani isim yine ekrandaki jenerik kartından okundu [Ders 60 · ikinci kez].
Raporun son satırı:

```
| THE HALF SKY | ALL | UNV | UNV | 6 | 7 | UNV | N/A | 4 | 4/10 |
```

**Sorun:** Ders 60'ta uydurulan isim (*The Silent Reckoning*) depoda hiçbir
şeyle eşleşmiyordu ve zararı "gerçek filmin kaydıyla asla eşleşemezdi" diye
kaydedilmişti. Bu sefer **eşleşiyor** — ve zarar tersine döndü:

```
dikey_shorts_filmler/THE_HALF_SKY_DIKEY_SHORTS.md   ← GERÇEK, var olan film
```

Yani 4/10 satırı boşluğa değil, **gerçek bir yapımın kaydına** yazılacaktı.
Üstelik neredeyse kesin biçimde yanlış filme:

```
Dosya diyor                        Görüntü diyor (raporun kendi künyesi)
──────────────────────────────     ─────────────────────────────────────
6 sahne (S0–S5)                    7 sahne
48 saniye                          64 saniye
ekranda metin süresi = 0,0 sn      S7 bir jenerik kartı
oksit kırmızısı suit · şeffaf vizör beyaz kask → baloncuk → kırmızı
```

Dört alanın dördü tutmuyor. Bu materyal büyük olasılıkla **o film değil** —
ve 4/10, henüz çekilmemiş olabilecek bir filmin satırına düşecekti.

**Neden Ders 60'ın yaması yetmedi:** 60 "isim uydurma" diyor. Uydurulan ismin
**tutabileceğini** öngörmüyor. Bir isim depodaki bir dosyayla eşleştiğinde
rapor daha da inandırıcı görünür — künye artık gerçek bir yola çözülür.

**ÇÖZÜM — İSİM ÇARPIŞMA KAPISI, kalite satırı yazılmadan önce:**

```
Kalite tablosu satırı yazılabilmesi için üçü birden gerekir:

1. Başlık SPEC BLOĞUNDAN gelir, ekrandan DEĞİL.        [Ders 60]
2. grep -ril "<başlık>" --include="*.md" .
      · eşleşme YOK → satır yazılmaz, çalıştırma kayıtsızdır
      · eşleşme VAR → dosya AÇILIR ve 3. maddeye geçilir
3. Dosyayla dört alan karşılaştırılır: sahne sayısı · toplam süre ·
   sahne numaralandırma tabanı · ekranda metin kuralı.
      · dördü tutuyorsa satır yazılır
      · biri bile tutmuyorsa çıktı yalnız şudur:

      MATERIAL DOES NOT MATCH THIS FILM — NO ROW WRITTEN
      Title read from : <ekrandaki metin / verilen künye>
      Repo file       : <yol>
      Mismatch        : sahne <x/y> · süre <x/y> · metin kuralı <x/y>
      Action          : hangi filmin materyali olduğu doğrulanmadan
                        hiçbir tabloya hiçbir satır girmez.
```

**Kural:** Ekrandan okunan bir başlığın depoda karşılığı çıkması, doğrulama
değildir — **çakışmadır.** Doğrulama, dosyanın içindeki sayıların materyalle
tutmasıdır.

---

## 🟡 DERS 66: SAHNE NUMARALANDIRMA TABANI RUBRİKLE DOSYA ARASINDA UYUŞMUYOR

**Kaynak:** SHORTS_QA 05.08.2026 — rapor sahneleri `S1…S7` diye numaraladı.

**Sorun:** Üç ayrı numaralandırma var ve hiçbiri diğerine eşlenmiyor:

```
Film dosyası      SAHNE 0 · 1 · 2 · 3 · 4 · 5      (S0 = Kanca)
Rubrik SCENE alanı  [Hook / 1 / 2 / 3 / 4 / 5 / ALL]  (Hook adsız, S1 ikinci)
Rapor             S1 … S7                          (taban belirsiz)
```

Sonuç: bulgular geri eşlenemiyor. Rapordaki *"S4 — Suit back entirely
changes"* bulgusu dosyada hangi sahne? Dosyanın S4'ü **dönüş / 40 m / eller
yanında** sahnesidir; raporun S4'ü dördüncü mü beşinci mi bilinmiyor. Prompt'a
geri yazılacak bir bulgunun hangi prompt bloğuna gideceği belirsizse, bulgu
uygulanamaz — rapor okunur ama kullanılamaz.

**ÇÖZÜM — TABAN DOSYADAN ALINIR:**

```
SCENE alanı film dosyasının kendi başlığını kullanır, rubriğin varsayılanını
değil. Dikey shorts hattında taban SIFIRDIR:

  SCENE: [S0 Kanca / S1 / S2 / S3 / S4 / S5 / ALL]

Her bulgu, sahne numarasının yanına dosyadaki başlığın adını da taşır:
  "S1 @ 0:11.2" değil → "S1 YARIM AYNA @ 0:11.2"
Ad tutmuyorsa numara da tutmuyordur; bulgu UNRESOLVED yazılır.
```

---

## ⚠️ 63-66 HAKKINDA — DÖRDÜ DE TEK BİR ÇALIŞTIRMADAN ÇIKTI

Bu dört ders `SHORTS_QA_CRITIQUE_PROMPT.md`'nin **ikinci** çalıştırmasından
çıktı ve dördü de aynı kökten besleniyor: **rubrik durmadı.** STEP 0.5
kapısını "FAILED" diye işaretledi ve bir sonraki satırdan puanlamaya devam
etti — Ders 60'ın (dur kodu ÇIKTI ŞABLONUNDA ALAN olamaz) tarif ettiği
mekanizmanın aynısı, çünkü bu rubriğin çıktı şablonunda hâlâ şu satır var:

```
STEP 0.5 GATE: [PASSED / FAILED — if failed, stop here and report the mismatch]
                ↑ bu bir ALAN'dır. Model alanı DOĞRU cevapla doldurdu
                  ("FAILED"), yanına gerekçesini yazdı ("Proceeding with
                  limited verifiable scoring only") ve devam etti.
```

Aynı çalıştırmada **yeni ders üretmeyen** ama tekrar eden dört ders:

| Ders | Ne tekrarladı | Kaçıncı kez |
|:--:|---|:--:|
| 51 | kapıyı okudu, kendine gerekçeli muafiyet yazdı | 3 |
| 54(b) | doküman aranmadı — dosya depoda duruyordu | 3 |
| 60 | künye videodan uyduruldu | 2 |
| 62 | skor kendi tablosundan çıkmıyor (6·7·4·7·4·3·5 = 5,1 ≠ 4,0) · kalite satırında SCORES SUMMARY'de olmayan "Motion" sütunu | 2 |

> **Çıkarım:** 51-54 QA sınıfının dersleriydi, 60-62 o sınıfın ikinci
> dalgasıydı, 63-66 üçüncü. Üçünde de kusur filmde değil, **filmi ölçen
> araçta.** Bu depoda artık ölçüm aracının kendisi, ölçtüğü filmlerden daha
> çok ders üretiyor — ve bunun tek sebebi var: yamalar rubriklere yazılıyor,
> **kaynak rubriğe** yazılmıyor. [Ders 63]

---

## 🔴 DERS 75: MOD V'DE MALZEME KAPISI YOK — 12 SANİYELİK TEK KLİP, 3 DAKİKALIK FİLM GİBİ PUANLANDI

**Kaynak:** THE STARLESS CIRCLE · SENARYO_QA 4.1/10 (06.08.2026, mod V) —
`RUNTIME: 12 · SCENE COUNT: 1 · PEAK: no peak located · ENDS OR STOPS:
stops`. Aynı gün aynı filmin MANTIK ve KARAKTER mercekleri **2:54'lük
kurguyu** ölçtü (19 klip). Aynı filme dört mercek koşuldu, ikisi filmi
ölçtü, ikisi bir klibi.

**Sorun:** Mod V rubriği "belge yok" durumunu çözdü ama **"malzeme yetersiz"
durumunu çözmedi.** Rubrik tek çekimlik 12 saniyeye Yapı 3 · Duygu Yayı 3 ·
Final 3 · Tutundurma 4 verdi ve "camera-carrier karakter · doruk yok · ölü
bant" diye üç reçete yazdı. Üçü de doğru gözlem, hiçbiri filme ait değil:
tek bir çekimde yapı, yay ve final zaten olmaz. Skor 03_HIKAYE tablosuna
girseydi filmin gerçek hikaye ölçümü diye okunacaktı — Low Power'ın "var
olmayan 7 sahnelik kurgu" satırıyla aynı arıza, bu kez ters yönden:
orada SPEC uydurmaydı, burada MALZEME eksik.

**Neden yeni:** Ders 51-54 ve 60-66 hep **girdi yokken** ya da **SPEC
yanlışken** ne olduğunu konuşuyor. Bu, girdinin GERÇEK ama YETERSİZ olduğu
ilk vaka — ve rubrikte onu durduran tek satır yok, çünkü mod V'nin bütün
mantığı "ne verdilerse onu ölç".

**ÇÖZÜM — SENARYO_QA'ya (ve türevlerine) MALZEME KAPISI:**

```
⛔ STEP −0.5 — MALZEME KAPISI (mod V'de zorunlu, mod D'de SPEC zaten kapar)

Puanlamadan önce iki sayıyı ölç ve rapora yaz:
   ölçülen süre = ___ s        saydığın kesme sayısı = ___

KLİP-ONLY KOŞU  süre < 60 s VE kesme = 0  → elindeki bir FİLM DEĞİL,
                tek çekimdir. Şu dört kategori NUMARA ALMAZ, UNVERIFIABLE
                yazılır ve ortalamaya girmez:
                Yapı & Tempo · Duygu Yayı · Final · Tutundurma
                Header'a tek satır: "MATERIAL: SINGLE CLIP — not a film."
                Skor satırı tabloya `🚨 KLİP` işaretiyle girer, film
                skoru olarak okunmaz.
KISMİ KOŞU      süre, formatın tabanının yarısından azsa (2-4dk → <60 s,
                3-5dk → <90 s, 7-9dk → <210 s) aynı kural uygulanır.
TAM KOŞU        aksi hâlde normal mod V.

⛔ Bu bir DUR bloğu değildir: rapor yine yazılır, ama dört kategori boş
   kalır. "Etiket davranışı değiştirmezse dekordur" (Ders 52 · 60).
```

> 🔗 Operatör tarafı: dört mercek aynı filme koşulacaksa **dördüne de aynı
> dosya verilir.** Bu koşuda iki mercek klibi, iki mercek kurguyu ölçtü ve
> dört skor aynı satıra yazılamaz hâle geldi.

---

## 🔴 DERS 80: GİRDİSİZ KOŞU VERDİKT ÜRETTİ — "INPUT MISSING YASAĞI" MEDYAYI DA KAPSIYOR SANILDI

**Kaynak:** THE BLIND RETURN · VIDEO_QA (07.08.2026) — `VIDEO DURATION:
0s`, 11 kategorinin 11'i UNVERIFIABLE; rapor yine de **`VERDICT:
REGENERATE` + `🔴 BLOCKER: 1` + kalite tablosu satırı** üretti. Blocker
metni: "No video clip was detected in the prompt payload."

**Sorun:** Rubrikteki `⛔ "INPUT MISSING" IS NOT A LEGAL OUTPUT` bloğu
**doküman** için yazılmıştı (mod V'yi kurtarmak için: "belge yoksa da koş").
Model bunu **medya** için de bağlayıcı okudu: video yokken durmak yerine
rapor iskeletini doldurdu ve bir verdikt bastı. Verdikt bir ölçümün
sonucudur; ölçüm yoksa verdikt de yoktur — "REGENERATE" tabloya girseydi,
hiç izlenmemiş bir film "yeniden üretilecek" diye kayda geçecekti.
Bu arızanın üç öncülü var (01.08.2026, Bulgu 7: üç mercek girdisiz koştu,
biri boş rapor iskeleti üretti) ama o gün rubriğe protokol yazılmadı;
arıza altı gün sonra aynen tekrarladı. Ders 75'in ayna hâli: orada malzeme
YETERSİZDİ, burada HİÇ YOK.

**ÇÖZÜM — video-girdili bütün rubriklere MEDYA KAPISI (STEP −2):**

```
⛔ STEP −2 — MEDYA KAPISI (STEP −1'den bile önce)

İlk iş: ekli medyanın süresini ÖLÇ. Süre ölçülemiyorsa, 0 s ise ya da
tek bir kare bile okunamıyorsa tek legal çıktı şudur:

   MEDIA MISSING — RUN NOT STARTED
   Attached media: none readable.
   No scores. No verdict. No severity. No table row.

Bu blok çıktının TAMAMIDIR. "INPUT MISSING is not a legal output" kuralı
YALNIZ DOKÜMAN içindir — medya için tersi geçerlidir: medyasız koşu
diye bir şey yoktur. UNVERIFIABLE bir kategori verdikte katılamazsa
(Ders 52/60), 11 UNVERIFIABLE kategori de bir verdikt üretemez.
```

> 🔗 Ders 52/60 (etiket davranış değiştirmezse dekordur) · Ders 64 (denetçi
> eksik girdiyi yapımın kusuru yazdı) · Ders 75 (malzeme kapısı). Operatör
> tarafı: dört mercek aynı filme koşulacaksa dördüne de aynı dosyanın
> GERÇEKTEN eklendiği gönderimden önce kontrol edilir.

---

## 🔴 DERS 81: KURGU KAPISI SIRAYI VE KURULUM SAHNELERİNİ SAYMIYOR — TEK EKSİK SAHNE + TEK YER DEĞİŞTİRME, ÜÇ MERCEKTE "YAPISAL ÇÖKÜŞ" OKUNDU

**Kaynak:** THE BLIND RETURN (07.08.2026) — MANTIK 4.0 STRUCTURAL PROBLEM
(Coğrafya 3 · Nedensellik 3, dört MAJOR'ın üçü 02:19 sonrası) · SENARYO Ⓥ
4.0 REVISE STRUCTURE ("üç çelişkili final") · KARAKTER 4.0 (Kesme 3).
Plan 18 sahne / 180 s; kurgu 169 s. Eşleme: S0-S14 plan ızgarasına
saniyesi saniyesine oturuyor (çatlak 01:03 = S6 2.8 s), sonra **S15
(pencere + ÇEHOV 4 yedek vizör + "forty hours" repliği) kurguda YOK** ve
2:30-2:39'da **S17 malzemesi (merdiven tırmanışı) S16'dan ÖNCE** duruyor;
kalkışın kendisi hiçbir mercekte görünmüyor.

**Sorun:** Ders 70/72'nin kurgu kapısı dört şey sayıyor: klip sayısı ·
süre · ekran metni · CENTRAL CHOICE varlığı. **SIRA ve KURULUM sahneleri
kapının dışında.** Sonuç zinciri ölçüldü:

```
S15 yok            → yedek vizör kurulumsuz → S16'nın planlı yeni vizörü
                     "silinen hasar" bulgusu oldu (2 mercek, 2 kategori)
S16 ↔ S17 ters     → "hava kilidinde diz çökmüşken kendini dışarıda
                     roket merdiveninde buluyor" = Nedensellik 3/10
İKİSİ BİRLİKTE     → SENARYO reçetesi filmin PLANLI FİNALİNİ kesmeyi
                     önerdi ("drop the rocket and tube scenes")
```

Ders 62/72 eksik sahneyi, Ders 78 okunmayan anlatımı konuşuyordu; bu vaka
üçüncü biçim: **sahneler var, sıraları yok — kurulum düşünce ödeme,
devamlılık ihlali kılığına giriyor.** Ve reçete katmanı en pahalısı:
kurgu hatası içerik zaafı diye raporlanınca düzeltme önerisi filmin
finalini silmeye yöneliyor (Kaleida cıva nehri / Herd gök sürüsü emsali).

**ÇÖZÜM — KURGU KAPISI v2 (D70/72'nin dört maddesine iki madde eklenir;
kapı kaydı D74 gereği plan dosyasına tek satır yazılır):**

```
⑤ SIRA KONTROLÜ: kurgudaki klip dizisi, plan sahne haritasının sırasıyla
   BİREBİR aynı mı? Özellikle SON ÜÇ KLİP elle doğrulanır — bozulan blok
   her vakada final bloğu (D62 ×4 · D72 ×2 · bu vaka).
⑥ KURULUM LİSTESİ: planın her Çehov halkası için KURULUM sahnesi kurguda
   var mı? Ödemesi kurguda olup kurulumu olmayan halka = kapı BATTI;
   eksik sahne eklenmeden teslim edilmez. (Bu filmde tek satırlık
   kontrol — "HALKA 4 / S15 kurguda mı?" — üç merceğin bütün yapısal
   bulgularını üretimden önce yakalardı.)
```

> 🔗 Ders 62/72 (final kurguya girmedi) · Ders 78 (sahne var, anlam yok) ·
> Ders 73 (kurgu/üretim hatası içerik zaafı olarak raporlanır — tabloya
> işlemeden belge cevaplarına bak). QA tarafı için ayna kural: mod V
> raporunun "önerilen kesme listesi" filmin SON sahnelerini hedefliyorsa,
> önce kurgu sırası plandan doğrulanır.

## 🔴 DERS 85: MOD V RAPORUNUN PROMPT REÇETESİ, GÖRMEDİĞİ PROMPTU ALINTILIYOR

**Kaynak:** THE THIRD DUNE · VIDEO_QA (11.08.2026) — mod V, 4/10 ·
`PROMPT IMPROVEMENT SUGGESTIONS #2: REMOVE from video prompt:
"title card, cinematic poster" → causes burned-in text`

**Sorun:** Rapor promptları HİÇ GÖRMEDİ (mod V = yalnız video) ama
"şu ifadeyi promptundan çıkar" diye tırnak içinde metin yazdı. Depoda
kontrol edildi:

```
"cinematic poster"  → repoda HİÇ geçmiyor
"title card"        → 42/42 promptta geçiyor, ama YASAĞIN İÇİNDE:
                      "no subtitles, no title card, no watermark"
```

Reçete uygulansaydı **filmin çalışan metin yasağı silinecekti** — yani
rapor, tespit ettiği hatanın (4:00 yanık başlık kartı) tek savunmasını
kaldırmayı öneriyordu. Yanık kartın gerçek kaynağı prompt değil KURGU:
kapak görselinin başlık katmanı kurgunun sonuna eklenmiş (D70/72
zincirinin 4. vakası).

Bu, D65'in (başlık kartından film adı okumak) prompt tarafındaki
karşılığıdır: model, elinde olmayan bir belgenin içeriğini tahmin edip
alıntı formatında yazıyor. Alıntı formatı tahmini kanıt gibi gösteriyor.

**ÇÖZÜM — operatör kuralı, kart C'ye adım olarak girer:**

```
⛔ PROMPT REÇETESİ UYGULANMADAN ÖNCE GREP'LENİR.
   Raporun her REMOVE / REPLACE önerisi için:

     grep -rn "<önerideki tam dize>" <FILM klasörü>/

   çıktı BOŞSA          → reçete DÜŞER, film kaydına "fabrikasyon" yazılır
   çıktı YASAĞIN İÇİNDE → reçete DÜŞER (yasağı silme önerisidir)
   çıktı olumlu kullanım → reçete değerlendirilir

   ADD önerileri bu kapıdan muaftır — yeni cümle önermek tahmin değildir.
```

⚠️ Bu kapı yalnız mod V için değil: mod D'de de SPEC bloğu promptun
TAMAMI değildir, rapor yine görmediği satırları alıntılayabilir.

---

## 🔴 DERS 87: MOD V, FİLMİN ÖNERMESİNİ "ÇELİŞKİ" SAYDI — DEĞİŞEN ŞEY TASARIMSA BULGU DÜŞER

**Kaynak:** THE THIRD DUNE · MANTIK_QA (11.08.2026) — Coğrafya 4/10 ·
`1:00 araç düz kumda ↔ 2:00 araç dik tepeye gömülü — 🟠 MAJOR` ·
`2:00 ↔ 3:30 kalkışta dairesel çanak — 🟠 MAJOR`

**Sorun:** Raporun üç MAJOR'ından ikisi belge kontrolünde düştü ve
ikisinin de sebebi aynı: **filmin anlattığı şey bir değişimdi.**

```
① Araç önce düz kumda, sonra tepeye gömülü
   → plan S12: "40 m'lik yeni tepenin kayma yüzü aracın sancak yanını
     yutmuş" + ⑩ GÖMÜLME EKİ S12'den sonraki TÜM sahnelere işleniyor.
     Filmin adı zaten bu: ÜÇÜNCÜ TEPE. Çelişki değil, olay örgüsü.
② Kalkıştan sonra dairesel çanak
   → plan S22 (ÇANAK): 14 m genişliğinde sığ dairesel çukur.
     Ayakta kalan gerçek bulgu farklı ve daha küçük: çanak SIĞ SÜPÜRME
     çukuru değil DERİN ÇARPMA krateri olarak üretilmiş — uygunluk
     ihlali, devamlılık ihlali değil.
```

MANTIK_QA'nın baseline'ı "film kendisiyle tutarlı mı"dır. Ama bir
filmin ÖNERMESİ "zemin değişiyor" ise, kendisiyle tutarlı olmanın
tanımı gereği zemin değişecektir. Rubrik değişimi görür, sebebini
göremez — çünkü sebep plandadır.

Bu, D72/73/78/81 ailesinin **tersidir**: orada üretim/kurgu kaybı
içerik zaafı kılığına giriyordu; burada tasarım, devamlılık hatası
kılığına giriyor. İkisi de tabloya yanlış sayı yazdırır.

**ÇÖZÜM — operatör kuralı, kart E'ye adım olarak girer:**

```
⛔ COĞRAFYA / KOSTÜM-PROP / ZAMAN-IŞIK BULGUSU TABLOYA İŞLENMEDEN ÖNCE
   tek soru sorulur:

     "Bu DEĞİŞİM filmin önermesi mi?"
     → plan dosyasının LOGLINE + orta nokta + sayaç kanalları okunur

   evet  → bulgu DÜŞER, film kaydına "önerme" olarak yazılır,
           kategori skoru şerhli işaretlenir (satır ŞARTLI)
   hayır → bulgu ayakta

⭐ Daha ucuz önlem: planın QA SPEC bloğu hazırsa MOD D koş. Bu filmde
   blok plan dosyasının 856. satırında hazır duruyordu ve dört merceğin
   dördü de mod V koştu — üç yanlış bulgunun üçü de mod D'de imkânsızdı.
```

---

## 🔴 DERS 92: EŞLEME ÇÖKTÜĞÜNDE RUBRİK SUSMUYOR — KAYMIŞ SIRAYA ON KATEGORİ PUAN VERİLDİ

**Kaynak:** THE SECOND SHIP · Faz 7 / BEDEL 1. koşusu (MODE R, reel +
sıra kayması) · `.../FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md` D-AU
**Sorun:** ikinci koşu üst üste teslimat yüzünden taban üretemedi
(F6 reel · F7 reel + sıra)

Rubriğin içerik-çelişki kuralı çalıştı: beş segmentin beşi için
"content contradicts row" satırı yazıldı ve hangi satıra benzediği
bildirildi. **Sonra rapor on kategoriye de puan verip 1.9 ortalama
yayımladı.** En açık kanıt kendi cümlesinde:

```
"CAMERA DISCIPLINE - 2/10 (Push-ins and lockoffs fail their assigned
 slots DUE TO THE CLIP SHUFFLE)"
→ rapor, hatanın kendi eşlemesinden geldiğini BİLEREK sahneyi
  cezalandırdı. İçerikle eşlendiğinde kamera disiplini neredeyse
  temizdi: üç push-in ve yedi lockoff DOĞRU sahnelerde.
```

Tehlike puanın düşüklüğü değil, **puanın var olması**: tabloya yazılsa
kalıcı bir yalan olurdu; okuyan da bunu üretim kalitesi sanardı.

**ÇÖZÜM — rubriğe MAPPING COLLAPSE eşiği (çok sahneli rubrikler):**

```
Üç veya daha fazla klip/segment satırıyla çelişiyorsa:
  ① MATERIAL bölümünün ilk satırına "MAPPING COLLAPSE - N of M
     segments contradict their mapped rows" yazılır
  ② DENETİM DURMAZ — bulgular yazılmaya devam eder, ama her bulgu
     içerik çapasıyla verilir ("the segment that SHOWS the recess
     opening")
  ③ SKOR DURUR: eşlemeden bağımsız kategoriler (çapa disiplini,
     malzeme yasaları, ışık) puanlanır; eşlemeye bağlı olanlar
     (olay teslimi, kamera, faz zinciri) UNVERIFIABLE yazılır ve
     ortalamaya GİRMEZ
  ④ Genel ortalama yayımlanmaz; yerine "SKOR YOK - taban koşusu
     değil" satırı yazılır
```

⚠️ Bu eşik yalnız çok segmentli faz rubriklerinde gerekir
(`FAZ_0N_QA_PROMPT.md` ailesi); `QA_PROMPTLARI/` altındaki genel
rubrikler tek sahne/tek kurgu ölçtüğü için eşleme katmanı yoktur.
İşlendiği yer: `FAZ_07_BEDEL/FAZ_07_QA_PROMPT.md` STEP 0.5 + Scoring
rules; sonraki faz rubrikleri bu sürümden türetilir.

---

## 🔴 DERS 93: FİLME ÖZEL RUBRİK 4 SANİYELİK JENERİK KARTIYLA SUSTURULDU — KURGU KAPISI, GÖRDÜĞÜ HATAYI ÖLÇÜME ÇEVİRMEK YERİNE ÖLÇÜMÜ İPTAL ETTİ

**Kaynak:** THE RING LIGHT · 12.08.2026 · FİLME ÖZEL rubrik MOD F koşusu ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_RING_LIGHT_FILME_OZEL_HAM.md`
**Sorun:** ilk vaka — ama susturulan mercek, filmin kırk küsur kilidini tutan
TEK mercekti

Filmin kendi rubriği 12.08'de yazıldı ve gövdesinde her şeyi taşıyor: sayaç A
(8→0 darbe), sayaç B (güneş saati kaburgaları), ışık takvimi, 0 kare ateş,
0 kare metin, 7/7 MACHINE replik, 14/14 mühürlü kask, 0.2 m/s yanaşma, 14
sahnelik vuruş defteri. Koşunun tamamı şu oldu:

```
CLIP COUNT MISMATCH — RUN STOPPED
Observed clip count: 15 clips
Observed duration: 144 s
```

Sebep: kurguya eklenen **4 saniyelik jenerik kartı** (D70/72 zincirinin 5.
vakası — bilinen, ucuz, kurguda 4 saniyede düzelen bir hata). Aynı gün koşan
üç GENEL mercek üç skor üretti (7.0 · 6.0 · 8.5) ve hiçbiri filmin bir tek
kilidini bilmiyordu. Filmin **kendi** rubriği sıfır satır ölçtü.

```
Kapı doğru şeyi gördü. Yanlış şeyi yaptı:
   gördüğü      → planlı olmayan 15. klip = 🔴 bulgu
   yaptığı      → 14 sahnenin 14'ünü de ölçmedi
   maliyeti     → filmin tek gerçek ölçüm aleti karardı
```

⛔ Bir stop koşulu **ölçümü imkansız kılan** durumlar içindir (medya yok,
yanlış film). Fazladan bir jenerik kartı ölçümü imkansız kılmaz; sadece
sayımı bozar. Ders 80 medyasız koşuyu durdurdu çünkü ölçülecek şey yoktu;
burada ölçülecek 140 saniye vardı.

**ÇÖZÜM — kapı önce AYIKLAR, sonra sayar (sayısal):**

```
MOD F kapısı, klipleri saymadan ÖNCE sahne-dışı malzemeyi ayırır:

SAHNE-DIŞI MALZEME = süresi ≤ 6 s VE (ekranda metin taşıyan · statik kart ·
  hiçbir sahne bloğunun parmak izini taşımayan) klip.
  → kurgunun BAŞINDA veya SONUNDA ise: raporun ilk satırına yazılır,
    🔴 BLOCKER olarak loglanır [D70/72] ve sayımın DIŞINDA tutulur:
    "NON-SCENE MATERIAL: 1 clip · 4 s · EXCLUDED — burned title card 2:20"
  → kurgunun ORTASINDA ise: koşu durur (bu gerçekten başka bir kurgudur).

RUN STOPPED yalnız şu iki durumda:
   sahne klibi sayısı ≠ 14   ·   sahne kliplerinin toplamı 140 s ± 2 s dışında
```

⭐ Aynı düzeltme bütün filme özel rubriklere ve `FAZ_0N_QA_PROMPT.md`
ailesine uygulanır: **kapının işi ölçümü korumaktır, iptal etmek değil.**
İşlendiği yer: `QA_PROMPTLARI/FILME_OZEL/THE_RING_LIGHT_QA_CRITIQUE_PROMPT.md`
STEP −1 stop koşulları.

⭐ **İkinci halka — bu ders D72'yi de kapatıyor.** Ring Light'ın planında
jenerik kartı yasağı İKİ yerde yazılıydı (§5 kapak + §0.18 ⑦ kurgu kapısı
"ekran metni = 0.0 sn, jenerik/başlık kartı DAHİL") ve kurgu yine kartla
teslim edildi. **Yazılı bir kontrol maddesi, koşulmadığı sürece kontrol
değildir.** D72'yi mekanik olarak ölçebilecek tek yer koşulan rubriktir —
o yüzden kartı raporun ilk satırında 🔴 olarak loglamak, kapının kendisini
iptal etmekten kat kat değerlidir.

---

## 🔴 DERS 94: SPEC PLANDA HAZIRKEN KOŞULAN MOD V, KİLİT İHLALİNİ CİLA NOTUNA İNDİRİYOR — BEDELİ İLK KEZ ÖLÇÜLDÜ

**Kaynak:** THE RING LIGHT · 12.08.2026 · 🔧 VIDEO_QA + 📖 SENARYO_QA mod V
**Sorun:** operatör kuralı ②'nin 4. ihlali (Slow Stone · Starless Circle ·
Third Dune · Ring Light) — ama ilk kez ihlalin **ne kaybettirdiği** kalem
kalem görülebiliyor

Planın §0.15'inde yapıştırılmaya hazır bir SPEC bloğu duruyordu. Yapıştırılmadı.
Sonuç, dört kilidin dördünde aynı: mercek doğru şeyi gördü, **yanlış ağırlıkta**
raporladı.

| Yazılı kilit | Mod V ne yazdı | Mod D ne yazardı |
|---|---|---|
| `ATEŞ 0 kare` · tek serbest parçacık 6-8 boya pulu | "sparks and metal shards … lightweight CGI spray" 🟠 MAJOR | 🔴 BLOCKER — yasak nesne ekranda |
| `METİN 0 kare` | kutu işaretlendi + FLAGS'e SORU: "kart bilinçli mi?" | 🔴 BLOCKER — otomatik |
| 7 replik, 7/7 gövdesiz AI, ekranda ağız YOK | "lip-sync drift" 🟠 MAJOR | **SPEC MISMATCH — RUN STOPPED** |
| Viral ara S2 · S9 **KESİLEMEZ** | kesme listesinin 1. sırası = S2 | sahne kesme listesine hiç girmez |

```
⭐ Örüntü: mod V kilidi bilmediği için ihlali ŞİDDET DEĞİL, ZEVK sorusu
   sanıyor — "biraz CGI duruyor", "kart bilinçli mi?", "burası yavaş".
   Kilitli bir filmde bunlar cila notu değil, üretim kararlarıdır.
```

**ÇÖZÜM — davranış değiştiren kural (etiket değil):**

```
① Planında §0.15 SPEC BLOĞU olan bir film mod V koşulursa, koşu bir
   ÖN KOŞU'dur:
   · skor satırı tabloya Ⓥ ⚠️ ŞARTLI girer (bugünkü gibi),
   · AMA 00_INDEX tamlık matrisinde o mercek hücresi ❌ kalır —
     "ölçüldü" sayılmaz. /4 paydası mod D veya filme özel koşuyla dolar.
② Kesme listesi ve REMOVE reçeteleri ÖN KOŞU'da UYGULANMAZ (D85 kapısı
   + viral ara listesi kontrolü zaten gerekiyordu; ön koşuda ikisi de
   otomatik ret).
③ Operatöre tek cümle: SPEC bloğunu yapıştırmak 4 mercekte 4 kopyala-
   yapıştırdır; yapıştırmamak bu tablodaki dört satırı üretir.
```

⚠️ Mod D bu depoda **hâlâ hiç denenmedi.** Dört filmde SPEC hazırdı.

---

## 🔴 DERS 96: MOD V BULGUSU YAZILI BİR KİLİDE AYKIRIYSA, "FİLM Mİ SAPTI, RAPOR MI UYDURDU" SORUSU RAPORDAN ÇÖZÜLEMEZ

**Kaynak:** THE RING LIGHT · 12.08.2026 · üç mercek, dört çelişki
**Sorun:** iki emsalin ikisi de bu depoda var — Low Power'da **rapor uydurdu**,
Ring Walker'da **film saptı**; ikisi de aynı cümleyle başladı

Ring Light'ın üç mod V raporu, planın yasakladığı dört olay bildirdi:

```
① 2:14 İngilizce insan repliği + dudak senkronu   ↔ 7/7 gövdesiz AI, ağız yok
② 2:00 "visors up / unhelmeted faces"             ↔ kask 14/14 mühürlü
③ 1:56 kıvılcım ve metal şarapnel                 ↔ ATEŞ 0 kare
④ 1:04 · 1:28 vakumda hava sesi                   ↔ dışarıda ses 0
```

Rapor tek başına hiçbirini çözemez: aynı satır hem "film bozuldu" hem "mercek
uydurdu/yanlış okudu" demek olabilir. ② için üçüncü bir ihtimal daha var ve
en muhtemeli o: **kilit kendi kanıtını silmişti** (bkz. DERS 95).

⛔ Bu belirsizlikteki bulgu ne derse desin **ders üretemez, onarım listesine
giremez, tabloya kesin skor yazdıramaz.** Yazarsa iki hata mümkün: olmayan bir
hatayı yeniden üretmek (Low Power) veya gerçek bir sapmayı "rapor abartmış"
diye kapatmak (Ring Walker).

**ÇÖZÜM — KİLİT ÇELİŞKİSİ DEFTERİ (film kaydında zorunlu bölüm):**

```
Rapor işlenirken, YAZILI bir kilide aykırı her bulgu bulgu listesinden
alınır ve şu beş sütunlu deftere yazılır:

| # | rapor ne dedi (timecode) | hangi kilit (§ numarası) | çözüm eylemi | sonuç |

çözüm eylemi = master'ın O SANİYESİNİ izlemek/dinlemek (ortalama 10 sn iş)
sonuç        = FİLM SAPTI  → onarım listesine geçer, ders adayı olur
               RAPOR UYDURDU → bulgu düşer, merceğin körlüğü kaydedilir
               ⬜ AÇIK        → satır ŞARTLI kalır

⛔ Defterde ⬜ AÇIK madde varken:
   · o merceğin skoru ⚠️ ŞARTLI'dır,
   · bulgulardan ders yazılmaz,
   · yeniden üretim siparişi verilmez.
```

⭐ Defterin ucuzluğu asıl noktadır: dört maddenin dördü de toplam **bir
dakikalık master kontrolüyle** kapanır. Kapanmayan şey rapor değil, karardır.

---

## 🟡 DERS 97: KARAKTER PASAPORTU FİLMİN %14'ÜNDEN KURULDU, SKOR FİLMİN TAMAMINA YAZILDI

**Kaynak:** THE RING LIGHT · 12.08.2026 · 🧍 KARAKTER_QA · 8.5/10 (tablonun en
yüksek skoru olurdu)
**Sorun:** rubrikte "göremediğin kategoriye puan verme" kuralı TARİF olarak
vardı, sayı olmadığı için ateşlenmedi

Filmde iki insan 6 sahnede görünüyor, ama vizör/kadraj yüzünden yüz yalnız son
iki sahnede okunuyor: **2:00-2:20 = 20 s / 144 s = %14.** Rapor bunu kendisi
yazdı ("First clear view: S13, 2:00") ve sonra:

```
Facial Identity 9/10   ← iki sahnenin karşılaştırmasından, 14 sahne için
Voice 9/10             ← "single on-screen spoken line matches the physical
                          body perfectly" — planda böyle bir replik YOK,
                          filmde ekranda ağız YOK (§0.11)
Genel 8.5/10           ← ikisi de ortalamanın içinde
```

Yüz 9 ve Ses 9, filmin **en riskli** iki alanında en yüksek iki puanı verdi ve
tabloya girseydi "Ring Light'ta karakter tuttu" cümlesi kurulacaktı. Oysa
ölçülen şey: iki sahne birbiriyle çelişmiyor.

**ÇÖZÜM — KANIT TABANI (rubrik başlığına zorunlu satır + sayısal eşik):**

```
STEP 1 pasaport başlığına, her karakter için:
   FACE-VISIBLE: __ s / __ s toplam · __ / __ sahne
   COSTUME-VISIBLE: __ / __ sahne

EŞİK: bir kategorinin kanıtı 3 sahneden VEYA sürenin %25'inden azsa,
      kategori ⚠️ KISMİ yazılır, SAYI TAŞIMAZ, ortalamaya girmez —
      "iki sahne çelişmiyor" ile "on dört sahne tutuyor" aynı ölçüm değildir.

MUTLAK: ekranda konuşan bir ağız yoksa Ses ve Performans = N/A.
        Gövdesiz/sentetik anlatıcı bu kategoride ÖLÇÜLMEZ (→ SES_QA).
```

İşlendiği yer: `QA_PROMPTLARI/KARAKTER_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
STEP 1 + kategori 1/8 puanlama kuralı.

---

## 🔴 DERS 98: NEGATİF İHLAL KUTUSU İŞARETLENDİ, BULGUYA DÖNMEDİ — SAYIM LİSTESİ, OTOMATİK BLOCKER'I YUTTU

**Kaynak:** THE RING LIGHT · 12.08.2026 · 🔧 VIDEO_QA · kategori 10
**Sorun:** Ders 52/60'ın ("davranış değiştirmeyen etiket süstür") 3. vakası —
bu kez etiket, rubriğin KENDİ sayım listesinde

VIDEO_QA'nın 10. kategorisi 30 küsur yasak kutusu sayar ve **skoru yoktur.**
Ring Light raporunda kutu düzgün işaretlendi:

```
[x] Text, subtitles, captions, or watermarks visible on screen
    (2:20 - Title card printed directly into the footage)
COUNT total violations: 5
```

Aynı rubriğin 8. kategorisi bu ihlal için **"automatic 🔴 BLOCKER"** diyor.
Ama kutu hiçbir kategoriye bağlı olmadığı için:

```
· zaman kodlu bulgu listesine girmedi
· SEVERITY TALLY'de sayılmadı (rapor 1 🔴 gösterdi, ikincisi kayıp)
· hiçbir kategorinin skorunu düşürmedi
· ve FLAGS'e "bu kart bilinçli mi?" SORUSU olarak yazıldı
```

Yani rubriğin en kesin, en tartışmasız otomatik blocker'ı bir soruya dönüştü.
Kutu doğru işaretlendi; sistem yine de hatayı kaybetti.

**ÇÖZÜM — her kutu bir bulguya bağlanır (rubrik yaması):**

```
Kategori 10 kuralı:
  ① İşaretlenen HER kutu, bir kategoride zaman kodlu ve severity'li bir
     bulgu satırına bağlanır:  [x] <ihlal> → 2:20 · kat. 8 · 🔴 BLOCKER
  ② Bağlanmamış kutu işaretlenemez. Emin değilsen kutuyu boş bırak,
     gözlemi FLAGS'e yaz — kutu = ihlal iddiasıdır, soru değil.
  ③ Rapor sonunda denklik kontrolü yazılır:
     "NEGATIVE BOX COUNT: 5 · LINKED FINDINGS: 5 · UNLINKED: 0"
     eşit değilse rapor eksiktir.
  ④ Otomatik-BLOCKER kutuları (ekran metni/altyazı · gizli kesme · klon ·
     vakumda hava sesi) FLAGS'e SORU olarak yazılamaz — bunlar niyetten
     bağımsız ihlallerdir.
```

---

## 🔴 DERS 102: AYNI OLAY HEM "FLAGS'E SORU" HEM PUAN DÜŞÜŞÜ OLDU — ETİKET KATEGORİYE BAĞLANDI, OLAYA DEĞİL

**Kaynak:** THE LAST SHIFT dört mercek QA (16.08.2026, dördü mod V). Üç raporda
aynı 10 saniye (2:20-2:29) üç kez birden işlendi:

```
🔧 VIDEO_QA   Kamera  : UNVERIFIABLE  "cuts present; scene boundaries unverified"
              Çevre   : 5/10          "radical environment shift mid-video"   ← puan
              FLAGS   : "2:20 sudden shift to orange Mars-like atmosphere —
                         QUESTION: is this a scripted scene location change?"  ← soru
🧩 MANTIK_QA  Coğrafya: 4/10 + 🔴 BLOCKER (0:20↔2:20)                          ← puan
              FLAGS   : "Does the plan dictate a transition to a desert here?" ← soru
🧍 KARAKTER   Kostüm  : 2/10 + 🔴 BLOCKER                                      ← puan
              FLAGS   : "Was this an intentional flash-forward?"               ← soru
```

**Sorun:** Rubrikler mod V'de "belgesiz karara bağlanamayan gözlem FLAGS'e SORU
olarak yazılır, bulgu olmaz" der [mod V kural 3]. Raporlar bunu yaptı — ve **aynı
gözlemden puan da düşürdü.** İki sonuç doğar:

```
① ÇİFTE SAYIM: bir olay hem "ölçemedim" hem "-4 puan" oldu. VIDEO_QA aynı
   kesme sorusunu Kamera'da UNVERIFIABLE yazıp Çevre'de puanladı: etiket
   KATEGORİYE bağlanmış, OLAYA değil.
② D87 SKORU ONARAMIYOR: belge kontrolünde bulgu düşünce (bu filmde iki soru
   da "filmin önermesi" çıktı — parsel ızgarası novum, amber faz planlı)
   BULGU listeden kalkar ama SKOR yerinde kalır. Çünkü hiçbir yerde
   "Çevre 5/10 hangi bulgulardan geldi" yazmıyor. Depodaki mod V skorlarının
   4-6 bandına sıkışmasının ölçülebilir bir sebebi budur: düşen bulguların
   puanı hiç geri verilmiyor.
```

**ÇÖZÜM — rubrik yaması, iki kural (tüm merceklerde):**

```
① SKOR HÜCRESİ KAYNAĞINI TAŞIR. Her kategori skoru, onu düşüren bulguların
   zaman kodlarıyla yazılır:
     | Environment | 5/10 | −3: 2:20 (F2), 2:30 (F3) |
   Kaynağı yazılmayan düşüş uygulanamaz; kategori tam puandan başlar.
② BİR GÖZLEM, BİR YER. Bir gözlem ya severity'li BULGUdur (puan düşürür)
   ya FLAGS SORUsudur (puan düşürmez). İkisi birden olamaz.
   ⛔ Bir kategoride UNVERIFIABLE yazılan olay, KOMŞU kategoride puanlanamaz.
   Etiket olaya aittir, kategoriye değil.
③ Operatör tarafı: belge kontrolünde bir bulgu düşerse [D87], film kaydına
   düzeltilmiş skor da yazılır — "bulgu düştü, satır ŞARTLI" yetmez.
```

> 🔗 Ders 52 (doğrulanmamış alandan blocker çıkmaz) · Ders 87 (önerme
> bulguyu düşürür) · Ders 94 (SPEC hazırken mod V) · Ders 98 (kutu bulguya
> bağlanır — bu ders onun skor tarafıdır).

---

## 🟡 DERS 103: NEGATİF KUTU DENETİMİ TEK YÖNLÜ — İŞARETLENMEYEN KUTU SAYIMI TUTTURUYOR, İHLALİ YUTUYOR

**Kaynak:** THE LAST SHIFT VIDEO_QA (16.08.2026) — rapor D98'in denklik
satırını kurallara uygun yazdı: `NEGATIVE BOX COUNT: 2 · LINKED FINDINGS: 2 ·
UNLINKED: 0` ✅ — ama aynı raporun bulgu listesinde **beş** bulgu var ve
bunlardan en az ikisinin listede karşılığı olan kutusu işaretlenmemiş:

```
1:52 🟠 "dust cloud moves uniformly like a 2D fluid simulation"
     → listede: "Frozen or static particles" · "Low-density CGI particle
       spray on impacts" — ikisi de boş
2:20 🟠 "suit radically changes design/patches/armband"
     → listede kostüm sürüklenmesi kutusu YOK (liste eksik)
```

**Sorun:** D98 denetimi **kutudan bulguya** çalışıyor ("işaretlenen her kutu
bir bulguya bağlanır"). Ters yön denetlenmiyor: bir ihlal bulgu olarak
yazılmış ama kutusu işaretlenmemişse, sayım **tutar** (2 = 2 = 0) ve ihlal
sayımdan düşer. Negatif ihlal sayısı bu yüzden filmin gerçek ihlal sayısı
değil, raporun işaretleme titizliğinin ölçüsü olur — ve o sayı tabloya girer.

**ÇÖZÜM — rubrik yaması, denetim iki yönlü koşulur:**

```
Kategori 10 kapanış bloğu:
  ① (D98, aynen kalır)  her işaretli kutu → zaman kodlu bulgu
  ② 🆕 TERS YÖN: severity taşıyan her bulgu, listede karşılığı olan kutuya
     bakar; karşılığı varsa kutu İŞARETLENİR.
  ③ 🆕 İki satır birden yazılır:
       NEGATIVE BOX COUNT: __ · LINKED FINDINGS: __ · UNLINKED: 0
       FINDINGS WITH A MATCHING BOX: __ · TICKED: __ · MISSED: 0
  ④ 🆕 LİSTE EKSİKSE SÖYLE: bulgunun sınıfı listede hiç yoksa, kapanış
     bloğuna tek satır — "NO BOX EXISTS FOR: costume drift" — böylece
     negatif çekirdek eksiği rapordan görünür (kostüm sürüklenmesi depoda
     D8/D42/D79/D84 ile dört kez ölçüldü ve hâlâ kutusu yok).
```

> 🔗 Ders 98 (denetimin ilk yönü) · Ders 102 (skorun kaynağı) · Ders 84
> (kostüm çapaları metinle tutmuyor — ④'ün sebebi).

---

## 🔴 DERS 105: RAPOR FİLM ADINI UYDURMADI — OPERATÖR AYNI BAŞLIK KARTINDAN OKUDU; DOSYALAMANIN TEK KANITI, FİLMİN EN AĞIR İHLALİ OLDU

**Kaynak:** THE BLACK CRADLE — FRAGMAN · 17.08.2026 · SHORTS_QA mod V ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_BLACK_CRADLE_FRAGMAN_SHORTS_HAM.md`
**Sorun:** ikinci vaka (ilki The Starless Circle, 06.08 — o satır bugün hâlâ
"operatör hangi dosyanın yüklendiğini doğrulayana kadar kesin sayılmaz")

Rubriğin kendi kapısı çalıştı: mod V kural 4 modelin ekrandaki başlığı okumasını
yasaklar ve rapor gerçekten `FILM: (not supplied)` yazdı [D65 ✅]. Kapının
kapattığı kapı, **operatör tarafında açık kaldı**: raporu bir film adının altına
dosyalayan tek kanıt, 00:58'de yanan başlık kartındaki yazıydı — modelin
okumasının yasaklandığı tam o kare. Aynı kart Wrong Shadow'da YANLIŞ film adını
taşıyordu; burada doğru adı + depoda hiç geçmeyen uydurma bir tagline taşıdı.

Eşleme elle yapılınca hiçbir şey tutmadı:

```
belge   6 vuruş × 8 s = 48,0 s · V0 hook = yüzeyde koşu · V4 = KIÇ ÖNDE, temas yok
kurgu   7 segment · 63 s · sahneler ~10 s · hook = statik istasyon planı
        (hiçbir belgede yok) · 2. çekim gezegene iniş (hiçbir belgede yok)
        · yanaşma BURUN ÖNDE (filmin imzasının tersi) · sonda 5 s metin kartı
sonuç   3 vuruş sırası bozuk eşleşti, 2 vuruş hiç yok, 2 çekim belgesiz
```

Buna rağmen rapor 15 kategoriye puan, bir ortalama ve bir **REGENERATE hükmü**
üretti. Tehlike puanın düşük ya da yüksek olması değil, **var olması**: tabloya
yazılsaydı, ölçülmemiş bir fragmanın kalitesi olarak kalıcılaşırdı.

⚠️ D92 bu eşiği yazmıştı ama kapsamını daralttı: *"bu eşik yalnız çok segmentli
faz rubriklerinde gerekir; `QA_PROMPTLARI/` altındaki genel rubrikler tek kurgu
ölçtüğü için eşleme katmanı yoktur."* Bu koşu o cümleyi çürüttü — mod V'de her
kurgu ölçümü bir eşleme ölçümüdür, çünkü eşlemeyi yapan artık rubrik değil
OPERATÖRDÜR ve onun kapısı yoktu.

**ÇÖZÜM — kapı operatöre taşınır (ajan kartı) + rapor kanıtı zorunlu olur:**

```
① AJAN KARTLARI C/D/E/E2/E3'ün ORTAK ADIMLARINA ③ eklenir — KİMLİK KAPISI:
   Ham rapor bir film adının altına dosyalanmadan önce, raporun sahne
   listesinden belgeye METİN OLMAYAN en az İKİ çapa eşlenir:
     · bir vuruş/sahne (ne gösteriyor) + bir sayısal kilit (kaç, kaç metre,
       hangi yön)
   eşleşme < 2  → koşu `UNATTRIBUTED` kaydedilir: ham rapor korunur, film
                  kaydı açılır, ⛔ SKOR SATIRI YAZILMAZ, ders yazılmaz
   ⛔ EKRANDAKİ YAZI ÇAPA DEĞİLDİR. Başlık kartı, filmin en ağır ihlali
      olduğu için kimlik kanıtı olarak da geçersizdir — hem model hem
      operatör için.

② RUBRİK YAMASI: SCENE INVENTORY (mod V'de zaten zorunlu) skorun ÖNÜNE
   alınır ve her sahne için tek isim cümlesi ister. Yazılmadıysa skor
   yayımlanmaz. Operatörün eşleme yapabilmesi için gereken tek şey budur;
   bu koşuda tam da o bölüm yazılmamıştı.

③ TEK SORULUK ÇÖZÜM ALIŞKANLIĞI: kimlik şüphesi doğduğunda master'ın
   TEK anına bakılır — filmin imzasını taşıyan kare (burada 00:48: kıç mı
   burun mu önde). Kimlik, 10 saniyelik bir işle çözülür; 15 kategorilik
   bir raporla çözülmez.
```

> 🔗 Ders 65 (uydurulan künye gerçek filmle çakıştı — bu dersin model tarafı) ·
> Ders 60a (ekrandaki yazı künye sanılıyor) · Ders 75 (malzemenin MİKTAR
> kapısı; bu ders KİMLİK kapısıdır) · Ders 92 (eşleme çöküşü) · Ders 96
> (kilit çelişkisi defteri — kimlik çözülmeden defter işlenmez).

---

## 🔴 DERS 106: RUBRİK FRAGMANI FİLM SANIYOR — BORÇ BIRAKMAYI CEZALANDIRDI, SPOILER'I "AKTARIM" DİYE ÖDÜLLENDİRDİ; ÜSTELİK BAŞKA BİR DERSİN ZORUNLU KILDIĞI BOŞLUĞU HATA YAZDI

**Kaynak:** THE BLACK CRADLE — FRAGMAN · 17.08.2026 · SHORTS_QA mod V
**Sorun:** ilk vaka — ama depodaki her fragman bu rubrikle ölçülecek
(Second Ship · Cold Burn · Black Cradle: üç fragman, tek rubrik)

SHORTS_QA'nın 14. kategorisi tek soru sorar: **"fikir vardı mı?"** Bu soru bir
FİLM için doğrudur. Fragman için tam tersidir: fragmanın işi cevabı vermemek,
borç bırakmaktır [FRAGMAN_KILAVUZU §1.2 spoiler kapısı]. Rubrik bu farkı
bilmediği için ölçüm ters çalıştı:

```
rapor  "Story & Transmission 7,0 — hikaye yayı tamamen okunuyor"
       tek cümle: "iki kişi kutuyu alır, kalkar ve istasyona kenetlenir"
belge  fragmanın tek işi: kenetlenmeyi GÖSTERMEMEK. Kenetlenme ekrana
       girdiyse fragman ÇÖKMÜŞTÜR — ve rubrik bunu 7 puanla ödüllendirdi.
```

İkinci ve daha sinsi taraf: rubrik, **başka bir dersin zorunlu kıldığı boşluğu**
hata olarak faturaladı. Kategori 13 CAUSALITY, "koşan insanlar → kalkan araç"
geçişini "biniş sahnesi yok" diye 🟠 MAJOR yazdı. Oysa biniş/iniş hareketi bu
depoda **kadraja alınmaz** — D69 (klon sıcak noktası) yasaklar, kaynak filmin
S5 satırında da yazılıdır, fragman promptu da bitişi kilitler (`Hold — no
boarding, no hatch`). İki ders ekranda çarpıştı: D69'a uymak, D-13 kategorisinde
puan kaybettiriyor.

**ÇÖZÜM — üçüncü eksen: MATERIAL TYPE (rubrik yaması):**

```
STEP 0'a üçüncü satır eklenir ve raporun ilk üç satırında ilan edilir:
   MATERIAL TYPE: [FILM / TEASER]

TEASER modunda değişen üç şey (yalnız üçü — gerisi aynı kalır):
  ① Kategori 14 sorusu tersine döner: "fikir vardı mı" değil,
     "SORU vardı mı" — teaser bir borç bırakmalıdır. Puan, tek cümlelik
     izleyici özetinde CEVAPLANMAMIŞ bir soru varsa yüksektir; özet
     tamamlanmış bir hikaye anlatıyorsa DÜŞÜKTÜR.
  ② Kategori 13 CAUSALITY, atlanan geçişi otomatik bulgu saymaz: teaser
     zaten atlayarak çalışır. Bulgu yalnız DURUM ÇELİŞKİSİ için yazılır
     (açılan kapanmış, alınan geri gelmiş).
  ③ Kategori 15'in ENDING maddesi "iniyor mu" değil, "borcu bırakıyor mu"
     diye ölçülür; kapanışta cevap verilmesi bir DÜŞÜŞTÜR.

⛔ KADRAJ DIŞI BIRAKILAN GEÇİŞ, EKSİK SAHNE DEĞİLDİR — bir çekimden
   diğerine geçerken binme/inme/kapak hareketi bilerek kadraj dışıdır
   (D69). Bu boşluk hiçbir modda nedensellik bulgusu değildir; kayıp
   sanılıyorsa FLAGS'e soru olarak gider.
```

> 🔗 Ders 69 (biniş/iniş kadraja alınmaz — çarpışan ders) · Ders 87 (film
> önermesiyse bulgu düşer; bu ders onun FORMAT karşılığıdır) · Ders 102
> (aynı olay hem soru hem puan düşüşü olamaz).

---

## 🔴 DERS 107: AYNI DOSYAYA KOŞULAN İKİ MERCEK FARKLI SAHNE SAYISI BİLDİRDİ — ÇAPRAZ SAYIM KAPISI

**Kaynak:** THE BLACK CRADLE · 17.08.2026 · beş mercek, aynı 232 s kurgu, hepsi mod V ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`
**Sorun:** ilk vaka — ama malzemesi eskiden beri var (D75 tek klip / kurgu ayrımını
çözmüştü; bu, kurgunun İÇİNİN kaç parça olduğunu kimsenin doğrulamaması)

Beş rapor aynı dosyaya koşuldu ve malzemenin kaç parçadan oluştuğu konusunda ikiye
bölündüler:

```
🔧 VIDEO            → 21 kesme, hepsi zaman koduyla listelenmiş
📖 🧩 🧍 🔊 dördü   → "SCENES OBSERVED: 4"
```

Dört merceğin sahne haritasında **85 saniyelik** ve **62 saniyelik** iki "sahne" var.
Bu hattın klip tavanı 10 saniyedir: 85 saniyelik tek sahne bu boru hattında
**üretilemez**. Yani dört rapor fiziksel olarak imkânsız bir malzemeyi tarif etti ve
Yapı · Duygu Yayı · Final · Tutundurma · Coğrafya · Zaman-Işık · Yıpranma · Ortam
Devamlılığı puanlarının hepsi o tarifin üstüne yazıldı.

Bedeli tek cümlede: filmin bedelli seçimi (iptal), umut-önce-düşüş anı ve doruğu,
85 saniyelik tek "yörünge sahnesi"nin içinde eridi — mercek "bedelli seçim yok,
umut anı yok, zirve şurada" yazdı, üçü de yanlıştı.

**ÇÖZÜM — ① rubrik yaması (STEP 1, dört mercekte de):**

```
Count the cuts BEFORE you name the scenes, and list them with timecodes.
A pipeline that generates fixed-length clips cannot contain a scene many
times longer than one clip: if any block you are about to call a single
scene is longer than twice the shortest gap between two cuts you observed,
your scene map is wrong — split it and count again.
Report the CUT COUNT as its own line. It is the only number in STEP 1 that
another reviewer can check against yours.
```

**ÇÖZÜM — ② operatör kapısı (maliyeti sıfır, master'a bakmadan işler):**

```
Aynı dosyaya birden çok mercek koşulduysa, raporları tabloya işlemeden ÖNCE
sahne/kesme sayıları yan yana yazılır:
   fark ≤ 1  → koşular birbirini doğruluyor, işle
   fark > 1  → o partinin TÜM satırları 🚨 GEÇERSİZ; hiçbiri tabloya
               girmez, hiçbirinden ders yazılmaz
Ölçüm aletinin kendisi tutarsızken filmin puanı tartışılmaz.
```

> 🔗 Ders 75 (mod V malzeme kapısı: aynı dosya) · Ders 101 (kurgu kapısı SAHNE
> sayıyor, ÇEKİM saymıyor) · Ders 109 (kapı geçilmemişse ölçüm kurguyu puanlar).

---

## 🔴 DERS 108: "BİR GÖZLEM BİR YERDE" KURALI RAPOR İÇİNDE ÇALIŞIYOR, RAPORLAR ARASINDA ÇALIŞMIYOR — TEK GÖZLEM DÖRT TABLOYA FATURALANDI

**Kaynak:** THE BLACK CRADLE · 17.08.2026 · beş mercek aynı kurguya
**Sorun:** D102 bu kuralı altı rubriğin İÇİNE yazdı; kural rapor sınırında bitiyor

Bu koşuda iki gözlem, dört ayrı tabloya düştü:

```
1:09 dudak senkronu (~0.4 s)
   🔧 VIDEO §8 🟠     ← SAHİBİ (üç rubriğin de ❌ listesi bunu VIDEO'ya verir)
   🧩 Nedensellik 5/10 (−5)
   🧍 Ses 5/10 (−5)
   🔊 Performans 5/10 (−5)

1:45 vakumda motor sesi
   🔧 VIDEO §8 🔴     ← SAHİBİ ("sound in vacuum → VIDEO_QA", İKİ rubrikte yazılı)
   🧩 Fizik 4/10 (−6)
   🔊 SFX 4/10 (−6) + Miks 7/10
```

Kapsam-dışı kaynaklar hücrelerden düşürülünce satırların okuması değişiyor:
🧩 5.6 → ~8.4 · 🔊 5.6 → ~8.8 · 🧍 5.8 → ~6.2. **Bildirilen hasarın büyük kısmı
filmin değil, faturalamanın eseriydi** — ve bu, tek bir kusurun film toplamını
mercek sayısı kadar aşağı çekmesi demektir.

**ÇÖZÜM — ① rubrik yaması (kapsam listesi olan her rubriğe):**

```
A finding your scope list hands to another lens carries NO number here,
however well it fits one of your categories. Write it once under
OUT-OF-SCOPE FLAGS and nowhere else: no severity tag, no deduction, no
row in a contradiction log. A category whose only source is such an
observation stays at full score and says so.
```

**ÇÖZÜM — ② film kaydına ÇAPRAZ GÖZLEM tablosu (kart C/D/E/E2/E3 birleştirme adımı):**

```
| gözlem (timecode) | hangi raporlarda | sahibi | puanı kim taşıyor |
Bir gözlem TEK tabloda puanlanır — sahibi, rubriklerin kapsam listesinin
gösterdiği mercektir. Diğer hücreler işaretçiye iner (→🔧 gibi) ve o
kategorinin skoru kaynaksız kaldığı için düşürülmez.
```

> 🔗 Ders 102 (etiket olaya bağlanır, kategoriye değil — bunun rapor içi hâli) ·
> kart E2 adım 5 ve kart E3 adım 6 (kesişim birleştirme: bu ders onları
> "kostüm-prop" ve "ses"ten çıkarıp HER gözleme genişletir).

---

## 🔴 DERS 109: KURGU KAPISINDAN GEÇMEMİŞ MALZEMEYE QA KOŞULDU — KAPI DEFTERİ KURGUDAN GERİDEYSE ÖLÇÜM FİLMİ DEĞİL KURGUYU PUANLAR

**Kaynak:** THE BLACK CRADLE · 17.08.2026 · beş mercek
**Sorun:** dördüncü vaka (Cold Burn kurgu kapısı 0/3 · Banded Deep 3/4 ·
Last Shift klip kaybı · bu film)

Filmin kendi kapı defteri (PART_A · KAPI KAYITLARI) koşu günü şunu yazıyordu:

```
17.08.2026 · ÜRETİM DURUMU: S0-S14 üretildi (operatör onayı).
17.08.2026 · S15 (kapı 1) · ÜRETİM ÖNCESİ V2 — deneme V2 promptuyla yapılır.
17.08.2026 · S16 video · 3 RED (0 başarı)
```

Ölçülen kurgu ise 232 saniye — kabaca 23 klip. İki ihtimalden hangisi doğruysa
sonuç aynı: **ya kapı defteri kurgudan geride (D74'ün 3. vakası), ya da ölçülen
dosya filmin teslim kurgusu değil.** Her iki hâlde de kurgu kapısı (26 klip ·
259 s ±2 s · ekran metni 0.0 s · S17 ve S21 ekranda) koşulmamıştı.

**ÇÖZÜM — operatör kapısı (kart C/D/E/E2/E3'ün ortak adımlarına üçüncü madde):**

```
③ KURGU KAPISI KAPISI
   QA koşulmadan önce iki satır doğrulanır:
     a) üretilen klip sayısı = plandaki SCENE COUNT
     b) kurgunun süresi = plandaki RUNTIME ± 2 s
   ikisi de tutuyorsa koşu NORMAL.
   biri tutmuyorsa koşu ÖN KOŞUdur:
     · satır tabloya ⚠️ ŞARTLI girer (sayım çelişkisi varsa 🚨 GEÇERSİZ)
     · film boyuna bakan kategoriler — Yapı · Duygu Yayı · Final ·
       Tutundurma · Ortam Devamlılığı · Kimlik Sürekliliği — SAYI TAŞIMAZ
     · kesme listeleri ve yeniden üretim siparişleri UYGULANMAZ
   ⛔ Kapı defteri kurgudan geriyse önce DEFTER güncellenir; kaydı olmayan
      kapı koşulmamış kapıdır (D74).
```

> 🔗 Ders 72/81 (kurgu kapısı) · Ders 74 (kayıtsız kapı) · Ders 100/101
> (klip sayısı ≠ sahne sayısı) · Ders 94 (SPEC hazırken mod V = ön koşu).

---

## 🟡 DERS 110: AYNI OTURUMDA ARKA ARKAYA KOŞULAN MERCEKLER BAĞIMSIZ ÖLÇÜM DEĞİLDİR — ORTAK DEFTER

**Kaynak:** THE BLACK CRADLE · 17.08.2026 · beş mercek tek sohbet oturumunda
**Sorun:** ilk kez belgelendi; sistemin "dört mercek birbirini doğruluyor"
varsayımının altını oyuyor

İki kanıt, yalnız raporlara bakarak:

```
· 🧩 MANTIK ile 🔊 SES raporlarının severity tally'si BİREBİR aynı: 🔴1 🟠2 🟡3
· Üç rapor aynı iki zaman kodunu (1:09 · 1:45) aynı saniye tahminiyle
  (~0.4 s) taşıyor; 📖 ile 🧩 aynı dört sahneyi aynı saniyelerle bölüyor
```

Bu, dört merceğin **dört ölçüm değil, tek ölçümün dört kılıfı** olduğu anlamına
gelir. Sistemin en güçlü doğrulama aracı — "üç mercek aynı şeyi gördü" — o zaman
delil değildir: aynı defteri üç kez okumuş olurlar. Bu koşuda dört merceğin
dördü de aynı imkânsız 4 sahnelik haritayı devraldı (D107).

**ÇÖZÜM — operatör kuralı (rubrik yaması değil; rubrik kendi oturumunu göremez):**

```
Her mercek TEMİZ oturumda koşulur: yeni sohbet, yalnız medya + tek rubrik
dosyası. Aynı oturumda ikinci bir rubrik çalıştırılmaz.
Doğrulama: raporların STEP 1 envanterleri BAĞIMSIZ yazılmış olmalı —
iki raporun sahne sınırları saniyesi saniyesine aynıysa ve severity
sayıları birebir tutuyorsa, bu bir doğrulama değil KOPYADIR; parti
yeniden koşulur.
```

**Rubrik tarafına düşen tek cümle (beş rubriğin STEP 1'ine):**

```
Build this inventory from the media alone. A ledger, scene map or finding
list produced earlier in this session — for this film or another, by this
rubric or a different one — is not evidence here. If you were shown one,
rebuild yours from the footage and say so.
```

> 🔗 Ders 107 (çapraz sayım kapısı — bu dersin ölçme aleti) · Ders 108 (aynı
> gözlemin dört tabloya faturalanması, kopya defterin doğrudan sonucu) ·
> AGENTS §2 kural ⑥ (ölçüm sapması ±1.3: bağımsız olmayan koşular bu sapmayı
> yapay olarak KÜÇÜK gösterir).

---

## 🔴 DERS 111: DERS BİR RUBRİĞE YAMANDI, KARDEŞLERİ TARANMADI — AYNI HATA AYNI GÜN İKİNCİ RUBRİKTE TEKRARLADI; ÜSTELİK YASAK KILAVUZDA YAZILIYDI VE MODEL O KILAVUZU HİÇ GÖRMÜYOR

**Kaynak:** THE COLD BURN — FRAGMAN DİKEY · 17.08.2026 · SENARYO_QA mod V ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_COLD_BURN_FRAGMAN_SENARYO_HAM.md`
**Sorun:** D106 aynı gün yazıldı, TEK rubriğe (SHORTS) işlendi; hata ertesi
koşuda ikinci rubrikte (SENARYO) birebir tekrarladı. İki vaka, iki rubrik,
tek kök.

D106 "rubrik fragmanı film sanıyor" hatasını ölçtü ve çözümünü SHORTS_QA'ya
`STEP 0.b — MATERIAL TYPE GATE` olarak yazdı. Yama doğruydu ve çalıştı.
Yamanmayan beş rubrik ise hatayı aynen üretmeye devam etti:

```
SHORTS_QA   MATERIAL TYPE: FILM / TEASER  ✅ var (D106)
SENARYO_QA  —                             ⛔ yok → bu koşu
VIDEO · MANTIK · KARAKTER · SES           ⛔ yok
```

Sonuç, teaser'ın **tasarımının** kusur olarak faturalanmasıdır:

```
rapor  Final 3/10 — "duruyor, bitmiyor; yanaşmayı çözmüyor"
belge  fragmanın kapanış cümlesi: "fragman TAM ORADA durur: cevap değil, borç"
rapor  reçete — "başlık posterini, istasyonun içindeki yangını gösteren
       airlock planıyla değiştir"
belge  o plan kaynak filmin ÜÇÜNCÜ PERDESİDİR; spoiler kapısı onu yasaklar
rapor  tek cümle — "iki astronot kaçar ve hasarlı istasyona sığınır"
belge  TEK CÜMLE TESTİ: özet tamamlanmış hikaye anlatıyorsa fragman ÇÖKMÜŞTÜR
```

⚠️ İkinci ve daha önemli taraf: yasak zaten YAZILIYDI. `FRAGMAN_KILAVUZU.md` §0
tablosu tek satırda "SENARYO_QA fragmana koşulmaz" der. Ama rubrik **operatörün
videoyla birlikte yapıştırdığı tek dosyadır**; kılavuzu ne model görür ne de
koşu anında kimse açar. **Yalnız kılavuzda yaşayan bir yasak, koşulmamış bir
kapıdır** [D74 mantığı]. Rubrik kendi kapsamını kendi içinden reddedebilmelidir.

**ÇÖZÜM — iki yerde, ikisi de zorunlu:**

```
① AJAN KARTI G'ye adım 5c — KARDEŞ RUBRİK TARAMASI:
   Kaynak rubrik yamandıktan sonra, dersin tarif ettiği hatayı ÜRETEBİLECEK
   her rubrik açılır ve yama oraya da yazılır. Ölçüt tek soru:
     "Bu rubrik aynı malzemeyi görse aynı hatayı yapar mıydı?"
   evet → yamanır ve iz defterine satır girer
   hayır → iz defterine "D<n> → <rubrik> · GEREKMEZ · <sebep>" yazılır
   ⛔ Tarama yapılmadan kart kapanmaz. "Kaynak rubrik yamalandı" bitiş
      değildir; D63'ün söylediği şey SIRA'dır, KAPSAM değil.

② RUBRİK YAMASI — MATERIAL TYPE ekseni SENARYO_QA'ya da girer (STEP 0.b).
   SENARYO_QA'nın on kategorisinde TEASER modunun karşılığı:
     · Final: iniş değil DEVİR ölçülür; kapanışta cevap vermek DÜŞÜŞTÜR
     · Yapı: atlanan geçiş bulgu değildir, teaser atlayarak ilerler
     · Kesme listesi ve reçeteler kaynak filmin cevabını fragmana SOKAMAZ
     · Tek cümlelik izleyici özeti CEVAPLANMAMIŞ soru taşımalıdır
```

> 🔗 Ders 106 (bu dersin birinci vakası ve yamanın metni) · Ders 63 (önce
> kaynak rubrik — bu ders onun kapsam eksiğini kapatır) · Ders 74 (kaydı
> olmayan kapı koşulmamış kapıdır; yalnız kılavuzda duran yasak da öyle) ·
> 03.08 emsali: D60/61/62 dört rubriğe işlendi, ÜRETEN rubrik atlandı ve iki
> gün sonra aynı hatayı üretti — bu ders o emsalin tersten tekrarıdır.

---

## 🔴 DERS 112: İKİ FARKLI FİLMİN İKİ AYRI RAPORU BİREBİR AYNI KURGU GEOMETRİSİNİ BİLDİRDİ — MOD V'DE SÜRE BİR ÖLÇÜM DEĞİL, BİR ÇIKTIDIR

**Kaynak:** THE COLD BURN — FRAGMAN (SENARYO_QA) + THE BLACK CRADLE — FRAGMAN
(SHORTS_QA) · 17.08.2026 · ikisi de mod V
**Sorun:** dört koşuda aynı parmak izi (First Morning 64 s · Wrong Shadow 64 s
· Black Cradle 63 s · Cold Burn 62 s)

İki ayrı rubrik, iki ayrı film, iki ayrı koşu — tek geometri:

```
                 süre   segment   sahne süresi   başlık kartı
Black Cradle     63 s      7        ~10 s        00:58'de
Cold Burn        62 s      7        ~9-10 s      0:58'de
belge (ikisi)    48 s      6        8,000 s      YOK (0,0 sn)
```

İki film aynı belgeye sahip değildir; iki kurgunun aynı saniyede aynı kartı
yakması, iki bağımsız üretimin tesadüfü olamaz. İki okuma mümkün ve **rapor
ikisini ayırt edemez**:

```
A) ÜRETİM SAPMASI  dikey hat 8 s yerine ~10 s klip üretiyor ve sona kart
                   koyuyor → gerçek, tekrar eden bir kurgu hatası
B) ÖLÇÜM SAPMASI   mod V okuyucusu gördüğü malzemeye VARSAYILAN bir sahne
                   haritası uyduruyor (7 × ~10 s + kart) → süre ölçülmedi,
                   tahmin edildi
```

⛔ Tehlike, hangisi olduğu değil: **62 s sayısı kurgu kapısına (D109) girdiği
anda ikisi de aynı hükmü verir** — "plan tutmuyor" — ve biri filmi, öteki
raporu suçlar. Ölçüm aleti kendi içinde tutarlıyken bile filmler arasında
tutarlı OLMAMALIYDI.

**ÇÖZÜM — bir operatör kapısı + bir rubrik cümlesi:**

```
① ÇAPRAZ FİLM PARMAK İZİ KAPISI (operatör · C/D/E/E2/E3 ortak adımı):
   Yeni bir mod V raporu işlenmeden önce, aynı rubriğin son iki koşusunun
   künye satırı yan yana konur: SÜRE · SEGMENT SAYISI · ORTALAMA SAHNE
   SÜRESİ · kart saniyesi.
     üçü de ±%5 içinde aynıysa → 🚨 PARMAK İZİ ŞÜPHESİ. Rapor işlenir ama
     SÜRE VE SAHNE SAYISI HİÇBİR KAPIYA GİRDİ SAYILMAZ; operatör dosyanın
     kendi süresini okur ve kapıyı O SAYIYLA koşar.
   D107 aynı DOSYAYA koşulan mercekleri karşılaştırır; bu kapı FARKLI
   dosyalara koşulan aynı merceği karşılaştırır. İkisi ayrı deliği kapatır.

② RUBRİK YAMASI (mod V başlığı olan her rubrik):
   "State how you obtained the runtime. If you read the container's own
   duration, write it as measured. If you counted it from playback or
   inferred it from the shots, write `RUNTIME: ~x s (ESTIMATED)`. An
   estimated runtime may not be used to declare a scene missing, a clip
   over-long or a plan violated."
```

> 🔗 Ders 107 (çapraz sayım kapısı — aynı dosya, farklı mercek) · Ders 110
> (aynı oturum bağımsız ölçüm değildir — aynı deliğin oturum tarafı) ·
> Ders 109 (kurgu kapısı; bu ders onun GİRDİSİNİ doğrular) · Ders 105
> (kimlik kapısı — parmak izi şüphesi kimlikten SONRA koşulur).

---

## 🟡 DERS 113: BELGEDE YAZILI KİLİDİN YOKLUĞU DÜŞÜK PUAN DEĞİL, `N/A`'DIR — RUBRİK BU MEKANİZMAYA ZATEN SAHİPTİ, YALNIZ DİYALOGA TAKILI BIRAKMIŞTI

**Kaynak:** THE COLD BURN — FRAGMAN DİKEY · 17.08.2026 · SENARYO_QA mod V
**Sorun:** aynı raporda iki kez (Karakter 4/10 · Tema 4/10); Diyalog
kategorisinde ise mekanizma DOĞRU çalıştı ve N/A yazıldı

SENARYO_QA'nın 6. kategorisinde tek ve doğru bir kural var: *"fully silent
film → score this category `N/A`, not a number; silence is a declared
constraint of this series, not a deficit."* Rapor bu kuralı uyguladı — Diyalog
`N/A`. Aynı raporun iki kategorisinde ise aynı sınıftan iki kilit **sayıya
çevrildi**:

```
Karakter 4/10  "yüz yok, iç dünya yok, karakterler kamera taşıyıcı"
belge          YÜZ KİLİDİ — yüz 0 KARE. "Fragman bir yüzle değil, bir
               boşlukla kapanır." Kask 2/2 kapalı, V3'te "his face out of
               frame". Yokluk ilan edilmiş ve sayıyla kilitlenmiştir.

Tema 4/10      "bedeli olan bir seçim yok"
belge          B2 maddesi: "BEDELLİ SEÇİM VAR ve fragmanın SON VURUŞUDUR;
               bedeli açıktır — yanaşma penceresi kapanır." Seçimin SONUCU
               spoiler kapısı yüzünden gösterilmez; rubrik sonucu göremeyince
               seçimin kendisini de yok saydı.
```

Sessizlik ile yüzsüzlük arasında hiçbir fark yoktur: ikisi de **belgede yazılı,
sayısal, bilinçli bir kısıttır.** Biri N/A alıyorsa öteki de almalıdır. Aksi
hâlde rubrik, çalışan tasarımı bozmaya yönlendirir — puanı yükseltmenin tek
yolu kilidi kırmaktır ve bir sonraki üretim onu kırar.

**ÇÖZÜM — mekanizma diyalogdan çıkarılıp kategori-üstü kurala terfi eder:**

```
RUBRİK YAMASI (SENARYO · SHORTS · KARAKTER):

DECLARED ABSENCE IS NOT A DEFICIT. When the material declares, as a written
and countable constraint, that something this rubric measures is absent —
no dialogue, no face on screen, no resolution, no second character — that
category takes `N/A`, stays out of the mean, and the constraint is named in
one line. Never convert a declared absence into a low score: the only way to
raise such a score is to break the lock, and the next production will break it.
An absence you merely SUSPECT is declared is not this rule — it goes to FLAGS
as a question.

⛔ Mod V'de "belgede yazılı" bilgisi modelde yoktur; bu yüzden kural iki
   taraflıdır: model bir yokluğu SİSTEMATİK görüyorsa (altı sahnenin altısında
   da yok) düşük puan yerine FLAGS'e soru yazar, operatör belgeden cevaplar ve
   kategori orada N/A'ya döner.
```

> 🔗 Ders 87 (değişen şey filmin önermesiyse bulgu düşer — bu, onun KİLİT
> karşılığı) · Ders 106 (teaser modunun kategori çevirileri) · Ders 102 (bir
> gözlem ya soru olur ya puan düşürür, ikisi birden olmaz) · Ders 52/60
> (etiket sayı taşımaz — N/A'nın ortalamaya girmemesi aynı ailedendir).

---
