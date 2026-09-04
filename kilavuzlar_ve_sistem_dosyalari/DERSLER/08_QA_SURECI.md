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

**(b) Dosya aranmadı.** `yatay_2_4_dk_filmler_uzay/THE_INVERSION/THE_INVERSION_PLANET_FILM.md`
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
dikey_shorts_filmler/THE_HALF_SKY/THE_HALF_SKY_DIKEY_SHORTS.md   ← GERÇEK, var olan film
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

**KAPI:** KARAR · `rubrik_paketle.sh` — rubrik + SPEC mercek başına TEK dosya, mod D VARSAYILAN — 01.09.2026
**TEKRAR:** 6 · ⛔ ÇALIŞMIYOR → araca çevrildi (01.09.2026): "SPEC'i ver" cümlesi tutmadı, varsayılan değişti

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

## 🔴 DERS 115: ÇAPRAZ SAYIM KAPISI RAPORLARI BİRBİRİNE BAKAR, IZGARAYA BAKMAZ — İKİ RAPOR AYNI SAYIYI VERİP İKİSİ DE ON SAHNE YANLIŞ OLABİLİR; IZGARA REPLİK ZAMAN KODUYLA GERİ ALINIR

**Kaynak:** THE BLUE DRIFT · 20.08.2026 · beş mercek, aynı ~254 s kurgu, hepsi mod V ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BLUE_DRIFT.md` KOŞU 2
**Sorun:** D107 bu hatayı GÖRDÜ ve rubrik yaması ("count the cuts before you name
the scenes") beş rubriğin beşinde de yazılıydı. Yine olmadı — ikinci vaka.

Raporların bildirdiği sahne sayısı:

```
📖 SENARYO   → 10 sahne (ve ~23 kesme — kesmeyi neredeyse doğru saydı)
🧩 MANTIK    → 15 sahne          🧍 KARAKTER → 15 sahne
🔧 VIDEO     → saymadı           🔊 SES      → saymadı
FİLMİN GERÇEĞİ → 25 segment (9 s hook + 24 × 10 s = 249 s)
```

İki şey aynı anda doğrudur ve ikisi de kapıyı deler:

```
① D107'nin rubrik yaması raporu KENDİ haritasını denetlemeye çağırır.
   Rapor bunu yapmaz: 🧩 kendi envanterinde 5 ve 9 saniyelik bloklar
   listeledi, sonra 30 saniyelik "tek sahne"ler yazdı — kendi kuralına göre
   bölmesi gerekiyordu. Raporun kendi kendini denetlemesine güvenilmez.

② D107'nin operatör kapısı raporları BİRBİRİYLE karşılaştırır: fark ≤ 1 ise
   "koşular birbirini doğruluyor, işle". Bu partide 🧩 ve 🧍 birebir aynı 15
   bloğu bildirdi — fark 0. Yani gate, on sahne yanlış olan iki raporu
   DOĞRULANMIŞ ilan ederdi. Ölçüyü ölçüye vurmak, ikisi de aynı yönde
   yanlışsa hiçbir şey ölçmez.
```

Bedeli, blokların içinde eriyen şeylerdir: 🧩 filmin üçüncü viral karesini
(airlock nefesi) "kokpit" etiketli 30 saniyelik bloğun içine gömdü; 📖 filmin
dönüm noktasını ve umut anını 40 saniyelik tek "tekrarlı kokpit" bloğu sanıp
kesme listesine yazdı.

**ÇÖZÜM — ölçüyü ölçüye değil, IZGARAYA vur (sayısal, master'a bakmadan):**

```
HİZALAMA KAPISI — plan dosyası elde olan her koşuda, rapor işlenmeden önce:

① IZGARA plandan alınır, rapordan DEĞİL:
      sahne başlangıcı(n) = hook süresi + (n-1) × klip süresi
② Her REPLİKLİ sahne için beklenen mutlak saniye hesaplanır:
      beklenen = sahne başlangıcı + o repliğin prompt TIMELINE'ındaki ofseti
③ Ses raporunun dialogue ledger'ındaki zaman koduyla karşılaştırılır:
      |Δ| ≤ 2 s   → sahne yerinde
      |Δ| ≈ klip süresinin katı → sahne kaymış: hangi dilim olduğu Δ'nın
                    işaretinden ve büyüklüğünden okunur
④ Raporun sahne haritası ızgara dilimlerinin birleşimi olarak yeniden yazılır;
   rapordaki sahne SAYISI hiçbir kapıya girdi sayılmaz.

Blue Drift'te: 16 repliğin 14'ü ±2 s içinde çıktı, biri (S6, iki replik) tam
−9.5 s → tek sıra şüphesi 20 saniyelik pencereye indi. Sıra denetiminin
tamamı, master açılmadan, iki belgeyle yapıldı.
```

⭐ **Bu kapı aynı zamanda kimlik kapısının SAYISAL biçimidir [D105].** Uydurulmuş
ya da başka filme ait zaman kodları bir ızgaraya oturmaz; 14 repliğin ızgaraya
düşmesi, raporun gerçekten O FİLMİ izlediğinin kanıtıdır — üstelik bunun için
başlık kartına bakmak gerekmez (kartın kanıt sayılması D105'in yasağıdır).

⛔ **Kapının koşulamadığı yer:** sessiz filmler. Orada aynı iş sahne sınırı
zaman kodlarıyla yapılır (blokların ızgara dilimlerinin birleşimi olup olmadığı
kontrol edilir) — Blue Drift'te 15 bloğun 15'i öyleydi ve blok 1 tam 9 s'lik
hook'tu.

> 🔗 Ders 107 (çapraz sayım kapısı — bu onun ikinci vakası ve düzeltmesi) ·
> Ders 110 (aynı oturum = ortak defter; iki raporun aynı sayıyı vermesi bu
> yüzden doğrulama değildir) · Ders 101 (kapı sahne sayar, çekim saymaz) ·
> Ders 105 (kimlik çapası) · Ders 92 (eşleme çöktüğünde rubrik susmuyor).

---

## 🔴 DERS 116: "BU DEĞİŞİM FİLMİN ÖNERMESİ Mİ?" KAPISI YALNIZ TEK KARTTA KOŞUYOR — AYNI YANLIŞ OKUMA DÖRT MERCEKTEN GELDİ, ÜÇÜNÜ HİÇBİR KAPI GÖRMEDİ

**Kaynak:** THE BLUE DRIFT · 20.08.2026 · beş mercek ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BLUE_DRIFT.md` KOŞU 2 · defter C bölümü
**Sorun:** D87 çözümü 12.08'de yazıldı ve **yalnız MANTIK kartına** (adım 2b)
işlendi. Bu partide filmin tasarımını "hata" diye faturalayan dört bulgunun
üçü başka merceklerden geldi.

```
🧩 MANTIK   turuncu kubbe (🟡)                → kapı VAR, bulgu düşer
🔧 VIDEO    perde kenarı = "vakumda aurora" (🔴)   → kapı YOK
🔧 VIDEO    telsiz repliğinde ağzın kımıldamaması (🔴) → kapı YOK
🧩 MANTIK   açık yakalama yuvası (🟠) + reçete: "4:00 çekimini kes" → kapı VAR
```

Dördünün de kaynağı planda yazılı:
perde kenarını sıyırarak geçiş = S8 · verici kubbesinin amber nabzı = S10'un
umut vuruşu · omurgadaki açık yakalama yuvası = S24 finali · kapalı kask +
arkadan kadraj = filmin ses mimarisi [D82 sigortası].

Bedeli iki cümlede:

```
· 🧩'in bir numaralı reçetesi uygulansaydı filmin PLANLI FİNALİ kesilecekti.
· 🔧'ün iki 🔴'sinden biri, filmin ses mimarisinin ta kendisiydi — yani
  "düzeltme" filmin çalışan tasarımını bozmak olurdu.
```

**ÇÖZÜM — kapı karttan çıkar, ORTAK ADIMLAR bloğuna girer:**

```
ÖNERME KAPISI, rapor hangi mercekten gelirse gelsin koşulur:

Coğrafya · Kostüm-Prop · Zaman-Işık · Çevre · Fizik · Ses mimarisi ·
Ekipman durumu başlıklarındaki HER bulgu, tabloya işlenmeden önce planın
logline + sahne haritası + sayısal kilit listesine karşı okunur:
   kaynağı planda YAZILI  → bulgu DÜŞER, film kaydına "önerme" yazılır
   kaynağı yok            → bulgu ayakta

⛔ Bulguyu getiren merceğin adı bu kararı değiştirmez. Tasarım, teknik
   rubrikten geldiğinde de tasarımdır.
```

⭐ **D111'in kart karşılığı.** D111 bir dersin kardeş RUBRİKLERE taranmasını
zorunlu kılar; bu ders aynı şeyi KARTLAR için söyler: bir kapı tek görev
kartına yazıldıysa, o kapının göreceği hata diğer kartlardan serbestçe geçer.
Yeni bir kapı yazan herkes şu soruyu cevaplar: **bu kapının yakaladığı hata
başka hangi karttan girebilir?**

> 🔗 Ders 87 (kapının kendisi) · Ders 111 (kardeş tarama — rubrik tarafı) ·
> Ders 94 (SPEC hazırken mod V koşmak: kapı olsaydı bile mercek tasarımı
> göremezdi) · Ders 82 (burada "hata" sanılan ses mimarisinin kaynağı).

---

## 🔴 DERS 117: SPEC PLANIN İÇİNDE GÖMÜLÜ KALDIĞI SÜRECE MOD D HİÇ KOŞULMUYOR — KAPI İHLALİ ETİKETLİYOR AMA AZALTMIYOR

**Kaynak:** LOSS OF LIFT · 21.08.2026 · üç koşu (📖 ×1 · 🧩 ×2), **üçü de mod V** ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/LOSS_OF_LIFT.md` § SPEC kapısı
**Sorun:** 6. vaka. D94 kapısı 12.08'de yazıldı; o günden beri **mod D sayısı 0.**

```
SPEC hazır, mod V koşuldu:  Slow Stone · Starless Circle · Third Dune ·
                            Ring Light · Banded Deep · LOSS OF LIFT
mod D koşusu:               0
```

Bu filmde SPEC eksik değildi — **üretimden önce**, yazım paketinin parçası
olarak, 12 maddelik kontrol listesinin E maddesi olarak yazılmıştı. Yine
kullanılmadı. Sebep bilgi değil ERİŞİM:

```
SPEC bloğu = 906 satırlık PLAN dosyasının 738. satırı
QA anında operatörün elinde  = video + rubrik dosyası
Aradaki mesafe               = bir dosyayı açıp doğru bölümü bulup kopyalamak
```

Kapı bunu yakaladı ve koşuyu ÖN KOŞU olarak etiketledi — ama etiket altı
filmde altı kez basıldı ve davranışı bir kez değiştirmedi. **Yalnız etiketleyen
kapı, kapı değildir.** Bedeli bu partide ölçüldü: üç koşu harcandı, üçünün de
kesme listesi uygulanamaz, üçü de tabloya ŞARTLI girdi.

**ÇÖZÜM — SPEC bir BÖLÜM değil, bir DOSYADIR:**

```
Film klasöründe:  <FILM>_QA_SPEC.md          ← yazım paketinin 6. parçası
İçinde üç blok:   A = SENARYO_QA SPEC alanları (rubriğin alan sırasıyla)
                  B = kurgu geometrisi (klip · süre · ızgara · insan şeridi)
                  C = belgesiz merceklerin FLAGS sorularını cevaplayan kilitler
Başında tek tablo: hangi rubriğe NE verilir — 🧩 🧍 🔊 için "HİÇBİR ŞEY"

QA anında iş = iki dosya yapıştırmak (rubrik + SPEC). Bölüm aramak yok.
```

**⭐ 26.08.2026 EKİ — ZORUNLU İKİ ALAN.** Şablon alan listesi vermediği için
depoda İKİ AYRI YARIM biçim oluştu ve hiçbir SPEC tam değildi:

```
BORROWED_WEIGHT · ROSE_COAT · LOSS_OF_LIFT
   THEME var  →  sahne-bazlı kamera alanları YOK ("CAMERA: 25/25 sabit lockoff")
IRON_SLOPE · NEAR_PASS · OPEN_SEAM
   sahne-bazlı LENS/HEIGHT/DISTANCE/MOVE var  →  THEME satırı YOK
(26.08.2026 sayımı; LAST_SPAN ve HELD_HEAT SPEC'leri o gün zombi türüyle
 birlikte depodan çıktı — kart H2)
```

Her iki alan da bir merceğin GİRDİSİ; eksikse mercek ölçemez:

⛔ Alanın yeri BLOK HARFİYLE değil MERCEKLE tarif edilir — harfler dosyadan
dosyaya kayıyor (bazı SPEC'te A = ① KARE, B = ④ HİKAYE; bazılarında tersi).
Ölçüt tek soru: **bu alanı hangi mercek okuyacak?**

```
④ HİKAYE'yi besleyen bloğa (kategori 5 "THEME & MEANING" temayı SPEC'ten okur):
   THEME (intended):   tek cümle · novum kelimesi geçmeden
                       (TEMA_MUHENDISLIGI §3'ün sekiz temasından biri;
                        §3b'deki aday etiketse ⏸️ işareti ile)
   THEME SCENES:       S__, S__, S__   ← temanın MOTİFE döndüğü sahneler
                       (§5 matrisi · en az 3 · prompt_kontrol.py bunu sayar)

KAMERA ALANLARININ YANINA (② DEVAMLILIK kurulum envanterini buradan doğrular):
   SETUP SEQUENCE:     A · C · A · C · B · A      ← sahne → kurulum harfi
                       + her harfin tanımı (lens · yükseklik · mesafe · açı)
   Sahne bazlı:        LENS / CAMERA HEIGHT / CAMERA DISTANCE / CAMERA MOVE
                       (IRON_SLOPE ve NEAR_PASS'ın biçimi standarttır)
   ANGLE ARC:          hangi vuruşta hangi açı (KAMERA_ACISI §3 tablosu)
                       + kullanılan açı TİPİ sayısı (≥3 · §2)
```

⚠️ **Kurulum SAYISI ile açı TİPİ sayısı ayrı iki sayıdır.** Bir film
ACI_YAYI §4'ün kurulum bandını tutup yine de tek açıdan bakıyor olabilir:
üç kurulumun üçü de yerdeyse çeşitlilik değil MESAFE değişimi vardır.
SPEC ikisini de yazar, betik ikisini de sayar.

⛔ **Kamera satırı TEK TOPLAM olarak yazılamaz.** "25/25 sabit lockoff" bir
kurulum kaydı değil, bir hareket kaydıdır: lockoff KLİP İÇİ karardır ve
sahneler ARASI kurulumu hiç anlatmaz. İkisi ayrı satırdır.

⛔ **Yazım paketi artık PLAN + PART_A + PART_B + KAPAK + MUZIK + QA_SPEC'tir.**
SPEC dosyası yoksa film "yazımı tamam" sayılmaz; plan içindeki blok kaynaktır,
teslim biçimi değildir.

> 🔗 Ders 94 (SPEC kapısının kendisi — bu ders onun uygulanma biçimi) · Ders 74
> (kaydı olmayan kapı koşulmamış kapıdır; buradaki eşdeğeri: **eline verilmeyen
> SPEC yazılmamış SPEC'tir**) · Ders 116 (mod V'de önerme kapısı: SPEC verilse
> kesme listesi virali zaten kesemezdi).

---

## 🔴 DERS 118: KURGU KAPISI SAYIYI VE SÜREYİ DOĞRULUYOR, SIRAYI DOĞRULAMIYOR — İKİ MADDE DE GEÇERKEN FİLMİN DORUĞU YANLIŞ YUVADA OLABİLİR

**Kaynak:** LOSS OF LIFT · 21.08.2026 ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/LOSS_OF_LIFT.md` § kurgu kapısı
**Sorun:** ilk kez ölçüldü. D109'un kapısı iki maddeydi ve ikisi de GEÇTİ:

```
a) KLİP SAYISI   26 − 1 kart = 25  = plan 25            ✅
b) SÜRE          255 − 5 = 250 s ≈ plan 249 s (Δ 1 s)   ✅
   → kapı "koşu NORMAL" dedi
```

Üç QA raporu da filmin **doruk sahnesini insansız bir gece dışı çekimi**,
ondan önceki insansız virali ise **doruğun kendisi** olarak bildirdi. Sayı
tuttuğu ve süre tuttuğu için hiçbir kapı bu soruyu sormadı; üç mercek de
o sıraya göre puanladı — senaryo merceği doruğu 30 saniye erken yerde arayıp
"dönüş çok geç geliyor" yazdı.

**Sıra, sayı ve süreden bağımsız bir boyuttur ve ölçmesi bedavadır.**

**ÇÖZÜM — kurgu kapısına ÜÇÜNCÜ madde: İNSAN ŞERİDİ**

```
Plandan yazılır (sahne haritasının "İnsan" sütunu), 1 karakter = 1 sahne:
    1 = sahnede insan var        - = insansız sahne
Örnek (25 sahne):  -111111111111-11111-1111-

Rapordan yazılır (her rubriğin sahne tablosunda "who is present" sütunu var;
rubriklere PRESENCE STRING çıktısı da eklendi — rapor bu diziyi kendisi verir).

c) SIRA   iki dize birebir aynı mı?
          aynı  → kurgu sırası doğrulandı
          değil → ⛔ ÖNCE ÇÖZ, SONRA PUANLA: farkın olduğu yuvaların
                  saniyeleri master'da izlenir (yuva başına ~10 s iş)
```

Kilit neden İNSAN: raporun sahne tablosundaki en az yorumlu sütun budur.
Mekân adı, aksiyon tarifi ve duygu okuması modele göre değişir; "kadrajda
insan var mı" değişmez. Bu yüzden metinsiz, sayılabilir ve mod V'de de çalışır.

⭐ Şerit bir yan ürün değil, **planın yazdığı bir kilittir**: insansız sahneler
zaten viral aralar ve açılış-kapanış çiftidir — yani filmin sırasının en çok
anlam taşıyan yerleri. Şerit tutuyorsa o dört yuva doğru; tutmuyorsa ilk
bakılacak yer tam olarak orasıdır.

> 🔗 Ders 109 (kurgu kapısının iki maddesi — bu ders üçüncüsü) · Ders 115
> (ızgara geri alma: bu dersin ZAMAN eksenindeki kardeşi; D115 sahnenin
> NEREDE olduğunu, D118 HANGİ SIRADA olduğunu ölçer) · Ders 101 (kapı sahne
> sayar, çekim saymaz) · Ders 70/72 (kart ayıklaması şeritten önce yapılır).

---

## 🔴 DERS 119: SKOR ARİTMETİĞİ RUBRİKTE YAZILI DEĞİLSE MODEL TOPLAMI UYDURUR — AYNI DEFTER, TEK YENİ GÖZLEM YOK, 2.0 PUAN FARK

**Kaynak:** LOSS OF LIFT · 21.08.2026 · 🧩 MANTIK_QA aynı dosyaya iki koşu ·
`02_HAM_RAPORLAR/LOSS_OF_LIFT_MANTIK_HAM.md`
**Sorun:** iki koşunun çelişki defteri, severity tally'si ve sahne haritası
**birebir aynı** — yalnız skorlar farklı:

```
                     hücrelerin ortalaması      raporun yazdığı OVERALL
KOŞU 1  10·10·9·10·7·10·10·10 =  9.5                    8/10
KOŞU 2   7· 7·6· 7·5· 7· 7· 7 =  6.6                    6/10
                                 └ ikisi de kendi tablosuyla tutmuyor
FARK: 2.0 puan · YENİ GÖZLEM: 0
```

İki ayrı ihlal üst üste bindi:

```
① VARSAYILAN DEĞER KELİMEYLE YAZILMIŞTI. Rubrik "kaynağı olmayan kategori TAM
   puanla başlar" diyor. Koşu 2 beş hücreye "[no in-scope source]" yazdı ve
   aynı satıra 7/10 koydu — yani kuralı okudu, uyguladı sandı, uygulamadı.
② TOPLAMIN NEREDEN GELECEĞİ HİÇ YAZILMAMIŞTI. MANTIK_QA'da "OVERALL =
   hücrelerin ortalaması" cümlesi YOK. Aynı cümle SENARYO_QA'da VAR — ve bu
   partide toplamı kendi tablosuyla tutan tek rapor o oldu (7.0 = 70/10).
```

⚠️ Bunun AGENTS §2 ⑥'ya (ölçüm sapması) etkisi doğrudan: **2.0 puanlık sapma
algıdan değil, boş bırakılmış bir varsayılan değerden geliyordu.** Aritmetik
yazılı olsaydı iki kopya koşu birbirinin aynısını verirdi.

**ÇÖZÜM — beş rubriğin skor bloğuna dördüncü madde (kaynak rubrik MANTIK önce):**

```
④ THE OVERALL SCORE IS ARITHMETIC, NOT AN IMPRESSION. Every category begins
   at 10/10 and loses only the deductions its own Issue cell lists with
   timecodes. A category whose issue cell reads "no in-scope source" scores
   10/10 — writing that phrase and a number below ten in the same row is a
   contradiction, and the phrase wins. Then compute the OVERALL SCORE as the
   mean of the category scores you actually printed... if they disagree, the
   table is right and the overall is wrong.
```

⭐ **Genel kural:** bir rubrikte sayı üreten her adımın aritmetiği GÖVDEDE
yazılı olmalı. "Tam puanla başlar" bir tariftir; "10/10 yaz" bir sayıdır.
Tarif kilitleri bu depoda %0 tuttu.

> 🔗 Ders 110 (kopya defter — bu iki koşunun neden tek ölçüm olduğu; yeni
> gözlem: kopya, sapmayı her zaman KÜÇÜK göstermez) · Ders 113 (yokluk `N/A`,
> düşük puan değil — aynı ailenin bir önceki üyesi) · Ders 63 + 111 (kaynak
> rubrik önce, sonra kardeş tarama: yama beş rubriğe işlendi).

---
## 🔴 DERS 120: SAHNE-DIŞI MALZEME KAPISI SÜREYE BAĞLI — VE KARTIN SÜRESİNİ HİÇBİR RUBRİK ÖLÇMÜYOR; ÜÇ MERCEK AYNI BAŞLIK KARTINI ÜÇ FARKLI YUTTU, PARTİ ÇAPRAZ SAYIMDAN DÜŞTÜ

**Kaynak:** THE BORROWED WEIGHT · 24.08.2026 ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md` § kurgu aritmetiği
**Sorun:** kurgunun sonunda planın `SCREEN TEXT: 0.0 saniye` kilidini ihlal
eden bir başlık kartı var. Kart TEK. Dört mercek onu dört farklı şeye çevirdi:

```
🔧 KARE        kesme listesini 4:20'ye kadar sürdürdü        → 26 kesme
🔗 DEVAMLILIK  haritasını 3:59'da bitirdi, künyesi 4:24      → 24 kesme, 25 s haritasız
🔊 SES         künyede 4:24 dedi, kartı hiç ayırmadı         → 24 kesme
📖 HİKAYE      kartı bir SAHNENİN İÇİNE aldı ("rests against
               pod, title") ve üstündeki yazıyı filmin ADI
               diye künyeye yazdı                            → 25 kesme, D105 tekrarı
```

Sonuç: kesme sayıları 26/24/24/25 → **fark 2 → ortak adım ⑤ partinin tamamını
🚨 GEÇERSİZ ilan etti.** Dört rapor, dört tablo, on iki saat iş — hepsini tek
bir kart düşürdü.

**İki ayrı boşluk üst üste bindi:**

```
① KAPI SÜREYE BAKIYOR, İÇERİĞE DEĞİL. AGENTS ortak adım ④ [D93]:
   "süresi ≤ 6 s VE ekranda metin taşıyan / statik kart". Eşik tek bir
   örnekten (4-5 s'lik jenerik) türetilmişti. 6 saniyeyi aşan bir kart
   kapının hiçbir dalına düşmüyor — üstelik UZUN kart, kısa karttan DAHA
   BELİRGİN biçimde sahne değildir. Kural yanlış yöne eğimli.
② KARTIN SÜRESİ HİÇBİR RUBRİKTE ALAN DEĞİL. Kapı "kayda TEK SATIR yazılır
   (kart 5 s)" diyor ama o sayının geleceği yer yok: rubriklerin künyesinde
   CUTS COUNTED var, NON-SCENE MATERIAL yok. Ölçülmeyen sayı, dört modelin
   dört ayrı yorumuna kalıyor — ve kart, sahne haritasının içine sızıyor.
```

**ÇÖZÜM — iki taraflı, ikisi de sayı:**

**a) Rubrik tarafı — dört rubriğin künyesine zorunlu satır:**

```
NON-SCENE MATERIAL: [in-out + what it is, or "none"]

⛔ Material that carries burned-in text, or is static, or bears no scene
   fingerprint, is NOT a scene — at ANY duration. Report it on this line
   with its in and out timecode, then EXCLUDE it from CUTS COUNTED, from
   the scene map, from the presence string and from every duration you
   report. A title card is never a scene and its text is never the film's
   name.
```

**b) Operatör tarafı — AGENTS ortak adım ④'ün kart kuralı süreden içeriğe:**

```
SAHNE-DIŞI MALZEME = ekranda metin taşıyan / statik / hiçbir sahnenin
parmak izini taşımayan klip. ⛔ SÜRE ÖLÇÜT DEĞİLDİR (eski ≤ 6 s eşiği
kaldırıldı — 14 s'lik bir kart 4 s'likten daha az sahne değildir).
  başta/sonda → kayda TEK SATIR ("kart 4 s"), 🔴 loglanır [D70/72],
                sayımın ve SÜRENİN dışında tutulur
  ortada      → bu başka bir kurgudur, koşu durur
Kartın in-out'u raporun NON-SCENE MATERIAL satırından okunur; raporlar
çelişirse kapı koşulmaz, süre master'dan okunur.
```

⭐ **Genel kural:** bir kapı, ölçtüğü şeyi rapordan OKUYAMIYORSA koşmuyordur.
D93 kartı gördü ve ölçümü iptal etti; D120 kartı ölçülebilir hâle getiriyor.

> 🔗 Ders 93 (kartın ölçümü iptal etmesi — bu dersin doğrudan ebeveyni) ·
> Ders 70/72 (kurgudaki başlık kartı 🔴) · Ders 105 (kart kimlik kanıtı
> değildir; bu partide yine öyle kullanıldı) · Ders 107 (çaprazsayım kapısı —
> bu partide onu düşüren şey kartın kendisiydi) · Ders 121 (kart ayıklandıktan
> SONRA şerit aritmetiği çalışır).

---


## 🔴 DERS 125: MAKİNEYLE ÖLÇÜLEBİLEN SAYIYI MODELE SORMA — ALTI MERCEK AYNI YANLIŞ KESME LİSTESİNİ VERDİ, BİRİ HİÇ VAR OLMAYAN SESSİZLİKTEN 🔴 BLOCKER ÜRETTİ

**KAPI:** BETİK · `qa-isle/scripts/olcum_kapisi.sh` — koşu sırasının EN BAŞI; ④ ⑤ ⑦ ⑨ bu betiğin sayılarıyla koşar
**TEKRAR:** 3 parti · son vaka 02.09.2026 (THE STILL SWARM) · ⛔ ÇALIŞMIYOR — ama engel araç değil, **DOSYA**: ffmpeg kurulu, master verilmiyor. Dönüştürme borcu: koşu, master YOLU olmadan başlatılmaz (operatör yolunu ham raporun künyesine yazar [D160])

**Kaynak:** THE IRON SLOPE · 25.08.2026 · altı mercekli parti (🔧🔗🔊📖🖼️⚖️),
altısı da mod V. İki bağımsız kanıt aynı koşudan çıktı:

```
KANIT 1 — KESME IZGARASI
  altı raporun ALTISI da:  0:09 · 0:18 · 0:29 · 0:39 · 0:49 · 1:00
  master (ffmpeg scene):   10,03 · 20,03 · 30,03 · 40,03 · 50,03 · 60,03
  Gerçek ızgara düzgün 10 saniyelik; raporların listesi hem yanlış hem
  DÜZENSİZ (9-9-11-10-10-11). Altı bağımsız ölçüm aynı düzensiz yanlışı
  vermez — ya ölçüm yok, ya defter ortak [D110].

KANIT 2 — SESSİZLİK
  🔊 SES:  "S4 complete digital silence 0:30-0:39" → 🔴 BLOCKER,
           AMBIENCE HOLE LOG'da üç satır, Ambiyans 2/10, toplam 4,3/10
  master:  silencedetect -50 dB / 0,3 s → SIFIR sonuç
           saniyelik RMS: 0-60 s'de en düşük −26,8 dB · S4 −19,7…−22,8 dB
  Merceğin en ağır bulgusu ve skorunun taşıyıcısı UYDURMADIR.
```

**Sorun:** ⑤ ÇAPRAZ SAYIM kapısı [D107] "raporlar birbirini doğruluyor mu"
diye sorar; bu partide altısı da **aynı yanlışta** anlaştı ve kapı ✅ verdi.
**Uyuşma doğruluk değildir.** D112 aynı yerden bir kez daha geçmişti (iki
filmin aynı künyeyi bildirmesi) ve çözümü yine rapora bakmaktı. Oysa bu
sayıların hepsi — süre, kesme, sessizlik, en-boy — **dosyadan 30 saniyede
ölçülür.** Bir modele, yanıtı bir komut satırında duran bir soruyu sormak,
o soruyu cevapsız bırakmaktan kötüdür: cevap gelir ve tabloya girer.

**ÇÖZÜM — ORTAK ADIM ⑪ ÖLÇÜM KAPISI (AGENTS §3'e eklendi):**

```bash
M="<master dosya>"
ffprobe -v error -show_entries format=duration:stream=width,height,r_frame_rate "$M"
ffmpeg -i "$M" -filter:v "select='gt(scene,0.3)',showinfo" -f null - 2>&1 \
  | grep -oE "pts_time:[0-9.]+"
ffmpeg -i "$M" -af "silencedetect=noise=-50dB:d=0.3" -f null - 2>&1 | grep silence_
ffmpeg -i "$M" -af "aresample=8000,asetnsamples=8000,astats=metadata=1:reset=1,\
ametadata=print:key=lavfi.astats.Overall.RMS_level:file=-" -f null -
```

```
· SÜRE · KESME IZGARASI · SESSİZLİK · EN-BOY: master'dan okunur, rapordan
  DEĞİL. Kapı ④ (kurgu) ve ⑨ (hizalama) bu sayılarla koşar.
· Rapor ile ölçüm çelişirse ÖLÇÜM kazanır; o merceğin satırı ŞARTLI olur.
· AMBİYANS DELİĞİ / DİJİTAL SESSİZLİK bulgusu ölçülmeden tabloya GİRMEZ.
· ⑤ çapraz sayım kapısı ÖLÇÜMDEN SONRA koşar: raporların birbirine
  uyması bir doğrulama değil, olsa olsa bir tutarlılıktır.
· Kapı master açılmadan koşar ve ~30 saniye sürer.
```

⭐ **Genel kural:** bir mercek yalnız YARGI ürettiği yerde değerlidir. Sayı
istediğimiz her yerde onu bir alet ölçmelidir — modelin sayıları, gördüğü
şeyin değil, beklediği şeyin sayılarıdır.

> 🔗 Ders 107 (çapraz sayım — bu ders onun kör noktasını kapatıyor) ·
> Ders 110 (aynı oturum = kopya defter) · Ders 112 (mod V'de süre bir
> çıktıdır; artık bir ölçümdür) · Ders 115 (ızgara geri alma — ölçümle
> tek adıma iniyor) · Ders 120 (kart süresi hiçbir rubrik tarafından
> ölçülmüyordu) · Ders 124 (klip süresi de aynı aletle ölçülür).

---

## 🔴 DERS 126: ARKA PLAN MERCEĞİ "ALANI ENVANTERLEDİM" DEDİ, KADRAJIN ALT ÜÇTE BİRİNDEKİ GEZEGENİ GÖRMEDİ — AYNI SATIR ALTI SAHNEDE TEKRARLIYORSA O SATIR ÖLÇÜM DEĞİL ŞABLONDUR

**Kaynak:** THE IRON SLOPE · ⑤ ARKA PLAN (derin tarama, ilk koşusu) — 3,8/10,
`FIELD COLLAPSES`. Envanterin altı sahnesinde de aynı iki satır:
`FAR FIELD: Black space, star field` · `SKY/CEILING: Deep space void`.
Master: **S2'de (20-30 s) bir GEZEGEN kadrajın alt üçte birini kaplıyor**
(bulut bantları ve atmosfer kenarı seçiliyor). Planın negatif bloğu, 12
promptun 12'sinde: `no planet, no moon`.

**Sorun:** Bu mercek bir koşuyu **tamamen özne-dışı alana bakmaya** harcamak
için açıldı; ilk koşusunda alanın en büyük nesnesini kaçırdı — üstelik o
nesne aynı zamanda planın YAZILI bir yasağını deliyordu. Çekirdek mercekler
de görmedi (① KARE `Environment 6/10` yazdı, gezegenden söz etmedi), ama
onların mazereti var: özneyi izliyorlar. ⑤'in yok.

Mekanizma: envanter **genel geçer bir cümleyle** doldurulabiliyor. "Black
space, star field" her uzay sahnesi için doğrudur, hiçbiri için ölçüm
değildir. Bir alan envanteri, sahneden sahneye DEĞİŞMEYEN bir satır
üretiyorsa envanter yapılmamıştır.

**ÇÖZÜM — ⑤ ARKA PLAN rubriğine (STEP 1 envanterine) eklendi:**

```
FAR FIELD, PER SCENE: name the LARGEST non-black object in the far field
and the fraction of frame height it occupies — "planet limb, lower third",
"station spine, upper quarter", or "none — empty black". A planet, moon,
sun, ring or large vessel is never summarised as "space": name it, place
it, size it.
If your FAR FIELD line comes out identical in every scene of the film,
treat that as a flag on your own inventory and look again — a repeated
line is a template, not an observation.
```

Aynı cümlenin ① KARE karşılığı (kategori 5 ÇEVRE) da yamandı: en büyük
arka plan nesnesi adlandırılır, yoksa "none" yazılır.

> 🔗 Ders 108 (bulgu sahipliği — gezegeni ⑤ görmeliydi, ① değil) ·
> Ders 103 (tek yönlü kutu denetimi: işaretlenmeyen kutu ihlali yutar) ·
> Ders 59 (yasak yazmak yetmiyor — `no planet` 12 kez yazılıydı) ·
> Ders 125 (aynı koşunun ikinci kör noktası: ölçülebilir olanı ölçmemek).

---

## 🔴 DERS 129: SPEC DOSYASI FİLMİN KENDİ KLASÖRÜNDE DURURKEN BEŞ MERCEK DE MOD V KOŞULDU — KESME LİSTESİ DORUĞU, KAPAK KARESİNİ VE İKİ VİRALİ KESTİ

**KAPI:** KARAR · `rubrik_paketle.sh` (QA_PROMPTLARI/FILME_OZEL/<FILM>/) + `rapor_kontrol.py` ① SPEC kapısı (mod V → TEKRAR) — 01.09.2026
**TEKRAR:** **11 film** · son vaka 02.09.2026 (THE SINKING STAKE, **sekiz mercek** — sebep: FILME_OZEL paketi yoktu [D165]) · ⛔ ÇALIŞMIYOR → araca çevrildi ama araç KOŞULMADI: paket ancak QA anında, `qa-isle` açılırsa üretiliyordu; film 01.09'da yazıldı, paketi hiç doğmadı, ertesi gün operatörün elinde yapıştıracak paket yoktu → **[[D165]]** aracı filmin YAZIMINA bağlar

**Kaynak:** THE ROSE COAT · 26.08.2026 · beş mercek ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md`
**Sorun:** D94 kapısının 7. vakası — **ama yeni bir vaka türü.** D117'nin
çözümü bu filmde UYGULANMIŞTI: SPEC bir bölüm değil, planın yanında duran
`THE_ROSE_COAT_QA_SPEC.md` dosyasıydı. Yine verilmedi.

```
D117'nin teşhisi   : "sebep bilgi değil ERİŞİM — 906 satırlık planın
                      738. satırını bulup kopyalamak"
Bu filmde erişim   : dosya HAZIR, klasörde, adı `_QA_SPEC.md`
Sonuç              : beş merceğin beşi de mod V
mod D sayısı       : hâlâ 0
```

Erişimi çözmek davranışı değiştirmedi, çünkü **hiçbir adım SPEC'in
yapıştırıldığını doğrulamıyor.** Kapı koşudan SONRA etiket basıyor; o anda
rapor zaten yazılmış oluyor.

Bedeli bu partide ilk kez sahne sahne ölçüldü. ④ HİKAYE'nin sıralı kesme
listesi (rapor numaralandırması plandan bir kayık: rapor S1 = plan S0):

```
1. rapor S4  = plan S3   ⭐ VİRAL 1   ⛔ SPEC: "KESİLEMEZ"
2. rapor S6  = plan S5   ÇEHOV 4 KURULUMU (ödemesi raporun övdüğü düşüş)
3. rapor S10 = plan S9   ⭐ ARİTMETİK — SEÇİMİN KURULUMU · ÇEHOV 5 ödemesi
4. rapor S12 = plan S11  🎯 DORUK + ⭐ VİRAL 3 ⛔ "KESİLEMEZ" + KAPAK KARESİ
5. rapor S3  = plan S2   ÖNCE KARESİ · ÇEHOV 5 kurulumu

Raporun doruk hakkındaki cümlesi:
   "One last redundant brush before climbing. Unnecessary."
Raporun doruk hakkındaki künye satırı:
   PEAK LOCATED AT: no peak located
Planın doruk hakkındaki satırı:
   DORUK: S11 → 110-120 s · yirmi darbe 112.0-118.0 s · boş vuruş 118.5 s
```

⭐ **Beş kesme adayının beşi de yük taşıyan sahne.** Bu bir zayıf rapor
değil: SPEC'siz koşan bir merceğin ÜRETEBİLECEĞİ EN İYİ rapor. Model
tekrarlayan bir fırçalama gördü ve doğru okudu — göremediği şey her
fırçanın ÖTEKİNİN sırtında olduğuydu, yani filmin novum'u.

**ÇÖZÜM — kapı koşudan ÖNCEYE alınır (AGENTS ortak adım ① yerine geçer):**

```
⛔ SPEC KAPISI KOŞUDAN ÖNCE KOŞAR — etiket değil, ÖNKOŞUL.

   f=$(ls <FILM klasörü>/*_QA_SPEC.md 2>/dev/null)
   [ -n "$f" ] && echo "SPEC VAR → mod D ZORUNLU: $f"

   SPEC dosyası VARSA ve rapor `INPUT MODE: D` yazmıyorsa:
     · rapor 02_HAM_RAPORLAR'a düşer, T tablosuna SATIR YAZILMAZ
     · kesme listesi, REMOVE reçetesi, yeniden üretim siparişi UYGULANMAZ
     · koşu TEKRARLANIR — etiketlenmez
   Bir koşuyu ŞARTLI diye tabloya almak, onu yapılmış saymaktır.
```

**ÇÖZÜM — SPEC dosyasının başına (operatörün gördüğü ilk satır):**

```
⛔ Bu dosya rubrikle BİRLİKTE yapıştırılır. Yapıştırılmadıysa koşu
   yapılmamıştır — ön koşu değil, YAPILMAMIŞ koşudur.
```

> 🔗 Ders 94 (SPEC kapısının kendisi) · Ders 117 (SPEC bir dosyadır — bu
> ders o çözümün UYGULANDIĞINI ve YETMEDİĞİNİ ölçüyor: erişim engeli
> kalktı, davranış değişmedi) · Ders 116 (SPEC verilse kesme listesi virali
> zaten kesemezdi) · Ders 74 (kaydı olmayan kapı koşulmamış kapıdır).

---

## 🔴 DERS 130: ⑩ ÖNERME KAPISI BULGUYU DÜŞÜRÜYOR, PUANI GERİ VERMİYOR — HÜCRE PARANTEZE ALINIYOR, TOPLAM AYNI KALIYOR

**Kaynak:** THE ROSE COAT · 26.08.2026 · ② ve ⑤ ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md` §ÖNERME KAPISI
**Sorun:** Kapının metni şunu diyor: *"kaynağı planda YAZILI → bulgu DÜŞER,
film kaydına 'önerme' yazılır."* Bulgu düşünce hücrenin kaybettiği puan ne
oluyor sorusunun cevabı **hiçbir yerde yazılı değil** — ve pratikte cevap
"hiçbir şey" çıkıyor. Bir önceki koşu bunu yazıyla itiraf etmiş:

```
T1_KARE_KALITE.md · The Iron Slope satır notu:
   "Parantezli hücreler ortak adım ⑩'dan geçemedi ...
    Toplam, rubriğin kendi aritmetiğidir."
```

Yani ⑩ tabloyu hiç değiştirmiyor: hücreyi parantez içine alıp toplamı
olduğu gibi bırakıyor. Bu filmde bedeli:

```
② DEVAMLILIK · rapor 7,2
   ⑩'dan düşen: Coğrafya −3 (0:50 ↔ 1:30 — plan: pada mesafe 120 m ↔ 0 m)
                Çapraz Kesme −3 (düşene yardım yok — SPEC: temas bütçesi)
   kalan ⬜ AÇIK: Kostüm · Yıpranma · Ekipman (üçü de "sırt çantası"
                  okumasına asılı; SPEC: çanta 0, sırt DÜZ GÖMME PANEL)
   → ayakta, kapalı, sayı taşıyan hücre: 0

⑤ ARKA PLAN · rapor 6,0
   ⑩'dan düşen: Ufuk −5 · Derinlik −3 · Arka Set −6'nın yarısı
                (üçü de aynı sebep: 500 m ↔ 30 m ↔ 0 m yaklaşma)
                Gökyüzü −4 (aynı gözlem ①'in, D108)
   → ayakta, kapalı, sayı taşıyan hücre: 0

İki tablo satırı da bir sayı taşıyor ve arkasında hiçbir şey yok.
```

⭐ **Genel kural:** bir kapı yalnız "bulgu düşer" diyorsa, o kapı bir NOT
üretir. Puan üreten bir sistemde kapının çıktısı da PUAN olmalıdır — yoksa
kapı çalışır, tablo değişmez, ve tabloyu okuyan kişi kapının hiç
koşulmadığı bir dünyada yaşar.

**ÇÖZÜM — AGENTS ortak adım ⑩'a üçüncü ve dördüncü satır:**

```
⑩ ... kaynağı planda YAZILI → bulgu DÜŞER
       kaynağı yok           → bulgu ayakta

   ⭐ ÜÇÜNCÜ SATIR — PUAN GERİ VERİLİR:
      Düşen her bulgunun timecode'u, hücrenin Issue gözünden SİLİNİR ve
      o hücre kaybettiği puanı GERİ ALIR. Issue gözü boşaldıysa hücre
      TAM PUANDIR — parantez değil.
   ⭐ DÖRDÜNCÜ SATIR — TOPLAM YENİDEN HESAPLANIR:
      Raporun OVERALL'ı ARTIK GEÇERSİZDİR. Film kaydına iki sayı yazılır:
        | mercek | raporun toplamı | ⑩ sonrası toplam | ayakta hücre |
      T tablosuna ⑩ SONRASI sayı girer; raporun sayısı ham raporda kalır.
   ⛔ Ayakta, kapalı, sayı taşıyan hücre sayısı 0 ise satır tabloya
      SAYI ile girmez: `—` girer ve "ölçüm yok" demektir. Sıfır hücreli
      bir ortalama bir ölçüm değildir.
```

> 🔗 Ders 87 + 116 (kapının kendisi ve kapsamı) · Ders 119 (rapor İÇİ
> aritmetik yazılı olmalı — bu ders aynı kuralı rapor SONRASI işleme
> genişletiyor) · Ders 108 (çapraz gözlem: aynı deliğin mercekler arası
> hâli) · Ders 131 (kaynaksız hücrenin tam puan alması — ⑩ bir hücreyi
> boşaltınca tam da o tuzağa düşürüyor).

---

## 🔴 DERS 131: "no in-scope source" = 10/10 — KAPSAM SINIRINA UYAN MERCEK KAYNAKSIZLIKLA ÖDÜLLENDİRİLİYOR; ÇÖKEN FİLM 4,3'TEN 7,2'YE ÇIKTI

**Kaynak:** THE ROSE COAT · 26.08.2026 · ② DEVAMLILIK ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_ROSE_COAT_DEVAMLILIK_HAM.md`
**Sorun:** D108 "kapsam dışı bulgu hücreyi düşürmez" dedi; D119 bunu sayıya
çevirdi: *"A category whose issue cell reads 'no in-scope source' scores
10/10."* İki doğru düzeltme birleşince şu çıktı:

```
② DEVAMLILIK · 13 kategori · 12'si sayı taşıyor

  kaynaklı hücreler : Kostüm 1 · Yıpranma 3 · Ekipman 2 ·
                      Çapraz Kesme 7 · Coğrafya 7 · Dünya Propu 6
                      → 26 / 6 = 4,3
  "no in-scope source · 10/10" hücreleri: Kimlik · Fizik · Zaman-Işık ·
                      Nedensellik · Nicelik+Sayı · Kurulum  (6 × 10 = 60)
  raporun yazdığı   : 86 / 12 = 7,2

  Δ = 2,9 PUAN — tek bir yeni gözlem olmadan.
```

Aynı raporun kendi hükmü `VERDICT: STRUCTURAL PROBLEM`. **Sözü ve sayısı
zıt yöne bakan bir satır tabloya girdi** ve tabloya giren sayıdır.

Aynı partide kuralın TERS yönde ihlali de var — ⑤ ARKA PLAN, `Frame Edges`
hücresine `no in-scope source` yazıp yanına **7/10** koydu; D119'un tahkim
cümlesi ("phrase wins") uygulansaydı 10/10 olacak ve toplam 6,0 değil 6,5
çıkacaktı. Yani aynı kural bir mercekte şişiriyor, ötekinde düşürüyor:
**hiçbir yönde ölçüm üretmiyor.**

⭐ Kökteki hata mantıksal: **kanıtın yokluğu, kusursuzluğun kanıtı değildir.**
`10/10` bir ölçümdür ve "burada bakılacak bir şey yoktu" ile "baktım, temiz"
aynı hücreye yazılamaz. `N/A` mekanizması bu depoda zaten var (D113) —
kaynaksız hücre onun kardeşidir.

**ÇÖZÜM — beş rubriğin skor bloğundaki ④. maddenin ikinci cümlesi
değiştirilir (kaynak rubrik ② DEVAMLILIK önce):**

```
④ THE OVERALL SCORE IS ARITHMETIC, NOT AN IMPRESSION. Every category
   begins at 10/10 and loses only the deductions its own Issue cell lists
   with timecodes.
   A category whose issue cell reads "no in-scope source", "no source" or
   the equivalent CARRIES NO NUMBER: write `—` in the Score cell and keep
   it OUT of the mean, exactly like N/A. Absence of evidence is not
   evidence of perfection, and a full score is a claim you did not measure.
   Then compute the OVERALL SCORE as the mean of the categories that
   actually carry a number, and print how many were excluded.
   ⛔ If fewer than half your categories carry a number, the OVERALL is
      not a score: write `— · n of m categories measured` instead.
```

> 🔗 Ders 119 (bu cümlenin önceki hâli — düzeltilen ders) · Ders 108
> (kaynaksızlığın sebebi: kapsam sınırı doğru çalışıyor) · Ders 113
> (yokluk `N/A`'dır, düşük puan değil — bu ders aynı kuralın YUKARI
> yönlü kardeşi) · Ders 130 (⑩ bir hücreyi boşaltınca tam bu tuzağa
> düşürüyor) · Ders 53 (sıfırlar temiz film gibi okunur — tam puanlar da).

---

## 🔴 DERS 132: SEVERITY TALLY YALNIZ BİR RUBRİKTE SAYILMAK ZORUNDA — AYNI PARTİDE A/B KANITI: SAYAN RUBRİK TUTTURDU, SAYMAYAN 8 BLOCKER'I 7 YAZDI

**Kaynak:** THE ROSE COAT · 26.08.2026 · ① KARE ↔ ⑤ ARKA PLAN
**Sorun:** ⑤ ARKA PLAN rubriğinin skor bloğunda beşinci bir madde var:

```
⑤ COUNT THE SEVERITY TALLY FROM THE FINDINGS, NOT FROM MEMORY.
```

Bu madde ① ② ③ ④'te **yok.** Aynı gün, aynı dosyaya koşulan iki rapor:

```
⑤ ARKA PLAN (kural VAR)  tally 🔴 0 · 🟠 3 · 🟡 2
                         çelişki defteri: 🟠 3 · 🟡 2        ✅ TUTTU
① KARE      (kural YOK)  tally 🔴 7 · 🟠 4 · 🟡 0
                         DETAILED ERROR LOG: 🔴 8 · 🟠 4     ❌ BİR EKSİK
                         (0:03 · 0:12 · 0:45 · 1:05 · 1:18 ·
                          1:25 · 1:33 · 2:02 = sekiz 🔴)
```

Tek partide temiz bir A/B. Ve tally dekoratif bir satır değil: **verdict onu
okuyor** — "Any 🔴 BLOCKER = REGENERATE" cümlesi tally üzerinden işliyor, ve
operatörün "kaç sahne yeniden üretilecek" tahmini de.

D111'in kardeş rubrik taraması bu kural için hiç koşulmamış: kural ⑤'e
yazıldığında ölçüt tek soruydu — *"bu rubrik aynı malzemeyi görse aynı
hatayı yapar mıydı?"* Cevap dördü için de evet.

**ÇÖZÜM — ① ② ③ rubriklerinin skor bloğuna beşinci madde (⑤'teki metnin
aynısı; ⑤ ve ⑥ zaten taşıyor, ④ HİÇ severity etiketi kullanmadığı için
GEREKMEZ — sayılacak şeyi olmayan rubriğe sayım kuralı yazılmaz):**

```
⑤ COUNT THE SEVERITY TALLY FROM THE FINDINGS, NOT FROM MEMORY. Before
   printing it, count the 🔴, 🟠 and 🟡 tags actually written in this
   report; the tally must equal those counts. A verdict driven by a tally
   that does not match the findings is a fabricated verdict.
```

> 🔗 Ders 111 (kardeş rubrik taraması — bu ders onun atlandığı bir kural)
> · Ders 98 (işaretlenen kutu bulguya dönmedi: aynı ailenin negatif kutu
> hâli) · Ders 103 (tek yönlü denetim) · Ders 119 (sayı üreten her adımın
> aritmetiği gövdede yazılı olmalı — tally de bir sayıdır).

---

## 🔴 DERS 133: MONOTONİK MESAFE SAYACI OLAN FİLMDE BELGESİZ MERCEK, TASARLANMIŞ YAKLAŞMAYI "GEOMETRİ SÜRÜKLENMESİ" YAZAR — ⑤'İN ALTI HÜCRESİNİN DÖRDÜ AYNI SAYAÇTAN GELDİ

**Kaynak:** THE ROSE COAT · 26.08.2026 · ⑤ ARKA PLAN 6,0 · ② Coğrafya 7 ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md` §ÖNERME KAPISI
**Sorun:** Bu film bir YAKLAŞMA filmidir: planın üç metinsiz sayacından
biri **pada mesafe 600 → 0 m, monotonik.** Her sahne aynı gemiyi bir önceki
sahneden daha yakından gösterir; ölçek, panel yüksekliği ve zemin dokusu
bu yüzden HER KESMEDE değişir ve değişmesi gerekir.

Belgesiz mercek bunu göremez ve gördüğünü şöyle yazar:

```
⑤ Ufuk    5/10  "0:30 düz sert zemin ↔ 1:00 yuvarlanan kumullar"
                 gerçek: plan S3 = ova kenarı 500 m · plan S6 = pad 30 m
⑤ Derinlik 7/10 "roket bacak ölçeği kesmeler arası şişiyor"
                 gerçek: 120 m ↔ 30 m
⑤ Arka Set 4/10 "panel 0:50'de alçak, 1:30'da devasa"
                 gerçek: 120 m ↔ 0 m
② Coğrafya 7/10 AYNI GÖZLEM, ikinci tabloya faturalanmış [D108]
```

Dört hücrenin dördü de tek bir tasarım kararından: **filme yürünüyor.**
⑩ önerme kapısı dördünü de düşürüyor — ama kapı ancak koşudan sonra,
operatörün elinde planla koşuyor, ve o ana kadar rapor "FIELD DRIFTS"
hükmü + iki "Regenerate S7/S8/S10/S12" siparişi üretmiş oluyor.

⭐ İkinci yarısı daha sessiz ve daha pahalı: SPEC'in `HANGİ RUBRİĞE NE
VERİLİR` tablosunda **yalnız ① ② ③ ④ var.** ⑤ ARKA PLAN ve ⑥ FİZİK
24.08'de açıldı; SPEC şablonu onları hiç tanımıyor. Yani "belgesiz koşan
mercek" listesi kural değil, KAZA.

**ÇÖZÜM — ① SPEC şablonuna iki satır (dağıtım tablosuna):**

```
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: mesafe/ölçek sayacı ·
                   ekran yönü · sabit çevre nesneleri.  ⛔ Kimlik, kostüm
                   ve olay kilitleri VERİLMEZ (o merceğin körlüğü tasarım).
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · oran · hız · süre).
```

**ÇÖZÜM — ② ⑤ ARKA PLAN rubriğine (kategori 5 Depth/Parallax & Scale):**

```
BEFORE CALLING A SCALE OR TOPOLOGY CHANGE A DRIFT, ASK WHETHER THE CAMERA
IS SIMPLY CLOSER. A film that travels toward a fixed object shows that
object larger in every successive scene, and the ground under it changes
with the ground the camera is standing on. A finding here needs TWO scenes
shot from the SAME distance to the SAME object — state the distance cue
you used (a figure's height against the object, a horizon position, a
known feature). "It looks bigger later" is an approach, not a defect.
```

> 🔗 Ders 87 + 116 (önerme kapısı — bu ders onun ⑤'teki en pahalı vakası) ·
> Ders 126 (aynı merceğin öteki kör noktası: en büyük nesneyi
> adlandırmamak) · Ders 130 (düşen bulguların puanı geri gelmiyor) ·
> Ders 117 (SPEC dosyası — bu ders şablonun iki merceği hiç tanımadığını
> ekliyor).

---

## 🔴 DERS 134: BELGESİZ MERCEĞİN "THE THREE THAT MATTER" SIRALAMASI SONUÇ SIRALAMASI DEĞİLDİR — BOT RENGİ FİLMİN ÜÇ KİMLİK KANALINDAN BİRİYDİ, RAPOR ONU "KOSTÜM SÜRÜKLENMESİ" YAZDI

**Kaynak:** THE ROSE COAT · 26.08.2026 · ② DEVAMLILIK ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_ROSE_COAT_DEVAMLILIK_HAM.md`
**Sorun:** ② merceğe BELGE VERİLMEZ ve bu bilinçlidir — baseline'ı videodan
kurulan karakter pasaportudur. Doğru tasarım. Ama sonucu şu: mercek **neyin
ne kadar önemli olduğunu bilemez**, ve raporun en çok okunan bölümü tam
olarak bir ÖNEM SIRALAMASIDIR.

Bu filmde iki uç aynı raporda yan yana duruyor:

```
RAPOR NE DEDİ                          SPEC NE DİYOR
──────────────────────────────────────────────────────────────────────
"Boot and glove color flipping"        KADRO KİLİDİ — iki figürü ayıran
🔴, "THE THREE THAT MATTER" #1,        ÜÇ kanaldan biri:
"Fix: regenerate · Cost: High"           UZUN = koyu antrasit bot+eldiven
   → kostüm sürüklenmesi diye            KISA = beyaz bot+eldiven
     tarif edildi                      Kanal çökerse film iki figürü
                                       ayırt edilemez hâle gelir [Kart 4]

"Counter Logic: N/A —                  SIRT SAYACI — FİLMİN ANA SAYACI,
 no counter present"                   beş görsel durum, monotonik,
   → kategori boş bırakıldı            yalnız fırçayla geri gider
                                       (+ mesafe 600→0 m + fırça kılları:
                                        filmde ÜÇ sayaç var)
```

Yani aynı rapor, filmin en kritik kilidini doğru yakalayıp yanlış
etiketledi ve filmin ana mekanizmasını hiç görmedi. İkisi de merceğin
kusuru değil: **körlüğün doğal sonucu.** Kusur, o sıralamanın operatöre
düzeltilmeden ulaşmasında.

⭐ Fark pratikte şudur: "kostüm sürüklenmesi" bir cila notudur ve sıraya
girer; "filmin iki karakteri ayırt edilemiyor" üretimi durdurur.

**ÇÖZÜM — kart ②/③/⑤ işleme adımlarına yeni adım (⑩'dan hemen SONRA):**

```
⭐ SPEC'E GÖRE YENİDEN SIRALA — belgesiz merceklerin raporlarında zorunlu.

   ⑩'dan sağ çıkan her bulgu, SPEC'in C BLOĞU'ndaki kilit listesiyle
   eşlenir ve film kaydına şu tabloyla yazılır:

   | bulgu (timecode) | raporun sırası | hangi kilide dokunuyor | GERÇEK sıra |

   · Bir KİLİDE dokunan bulgu, dokunmayan her bulgunun ÜSTÜNE çıkar.
   · Raporun "THE THREE THAT MATTER" / "TOP 3" listesi film kaydına
     OLDUĞU GİBİ değil, bu tabloyla YENİDEN SIRALANMIŞ hâlde geçer.
   · SPEC'te sayaç yazılıysa ve rapor `Counter: N/A` demişse, bu bir
     bulgu YOKLUĞU değil bir ÖLÇÜM BOŞLUĞUDUR: kilit defterine ⬜ AÇIK
     satırı olarak girer.
```

> 🔗 Ders 108 (bulgu sahipliği) · Ders 130 (⑩'ın puan tarafı — bu ders
> ⑩'ın SIRA tarafı) · Ders 96 (rapor tek başına "film mi saptı" diyemez) ·
> Ders 97 (pasaport filmin %14'ünden kuruldu — körlüğün ölçü tarafı).

---

## 🔴 DERS 136: PLAN 11 SAHNEDE MÜZİK YAZIYOR, TESLİM EDİLEN DOSYADA SES KANALI YOK — VE BUNU GÖREN TEK MERCEK HİÇBİR TABLOYA SATIR BIRAKMIYOR

**KAPI:** BETİK · `olcum_kapisi.sh` SES KANALI (ffprobe -select_streams a) — 22.08.2026'dan beri; satır 01.09.2026

**Kaynak:** THE ROSE COAT · 26.08.2026 · ③ SES ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_ROSE_COAT_SES_HAM.md`
**Sorun:** ③ SES `AUDIO ABSENT — RUN NOT STARTED` döndürdü — doğru davranış,
STATE C bloğu tam da bunun için yazıldı. Kart E3 ② kapısı da doğru koştu:
skor yazılmadı. Ama iki delik açık kaldı.

**① Aynı dosyaya koşan diğer dört mercek şüpheyi hiç görmedi:**

```
③ SES         "one of them is a delivery defect ... re-export, re-run"
① KARE        "Dialogue & Audio | UNVERIFIABLE | (no sound)"   → geçti
② ④ ⑤        "LINES HEARD: none"                              → geçti
```

`LINES HEARD: none` iki ayrı gerçeği aynı kelimeyle yazıyor: *tasarım gereği
sessiz film* ve *ses kanalı ihraçta düşmüş dosya.* Bu seride birincisi
normaldir, bu yüzden dördü de duraksamadan geçti.

**② ③'ün çıktısı hiçbir tabloya satır bırakmıyor.** Stop bloğu skor
üretmiyor, T3'e satır girmiyor, 00_INDEX'te ③ hücresi ❌ kalıyor — yani
"koşuldu ve dosya bozuk çıktı" ile "hiç koşulmadı" kayıtta AYNI görünüyor.
Partinin tek gerçek teslim şüphesi, kaydedilmeden buharlaşıyor.

Ve bu filmde şüphe planla doğrulanabiliyor:

```
plan §0.15  MUSIC-FREE SCENES: 2 — S0 (hook) ve S8 (fırça yetmez)
            → 13 sahnenin 11'inde MÜZİK VAR
plan C BLOĞU  S11 · 7,0 s: iki eldiven tıklaması (ses tasarımı)
dosya         ses bilgisi YOK
```

⭐ Ders şu: **sessiz film ile sessiz DOSYA aynı şey değildir, ve bu ayrımı
tek bir `ffprobe` satırı yapar.** Ortak adım ⑪ zaten ölçüyor — ama ses
kanalının VARLIĞINI ölçmüyordu, yalnız sessizlik aralıklarını.

**ÇÖZÜM — ① ortak adım ⑪'e beşinci komut:**

```
ffprobe -v error -select_streams a -show_entries stream=codec_type \
  -of csv=p=0 "$M"
→ çıktı BOŞ ise dosyada SES KANALI YOKTUR.
  · plan müzik/ses tasarımı yazıyorsa: 🔴 TESLİM KUSURU, parti DURUR,
    master yeniden ihraç edilir ve DÖRT mercek yeniden koşulur
    (görüntü merceklerinin ölçtüğü dosya da master değildir)
  · plan tamamen sessizse: ses kanalı yokluğu yine kayda geçer,
    ③ satırı `— · ses kanalı yok (doğrulandı)` olur
```

**ÇÖZÜM — ② beş rubriğin künye satırına (① ② ③ ④ ⑥ — ⑤'in künyesinde
`LINES HEARD` satırı yoktur):**

```
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or
"none"]. When you write "none", add which one you heard: "none — room
tone / ambience present" or "none — no audio information at all". A film
with no dialogue and a film with no audio track are different objects and
only one of them is a delivery defect.
```

> 🔗 Ders 125 (ölçüm kapısı — bu ders ona beşinci komutu ekliyor) ·
> Ders 107 (çapraz sayım: bu şüphe hiçbir çapraz eksende görünmüyordu) ·
> Ders 80 (girdisiz koşu verdikt üretti — bunun tersi: doğru duran koşu
> hiçbir iz bırakmıyor) · Ders 74 (kaydı olmayan kapı koşulmamış kapıdır).

---

## 🔴 DERS 137: SES KANALI VAR, ALTI MERCEĞİN ALTISI "HİÇ SES BİLGİSİ YOK" DEDİ — D136'NIN YAMASI TAKILIYDI VE ARIZA TERSİNE DÖNDÜ

**KAPI:** BETİK · `olcum_kapisi.sh` SES KANALI + `rapor_kontrol.py` (AUDIO STATE bir beyandır, ölçüm sayılmaz) — 01.09.2026
**TEKRAR:** 4 · araç zaten vardı; rapor beyanı ölçümün yerine geçmesin diye künye kuralı eklendi (rubrik_paketle künyesi)

**Kaynak:** THE THIN ROOF QA (28.08.2026) — altı mercek, altısı da mod V
**Sorun:** D136'nın tam TERSİ, aynı yamayla, bir sonraki filmde

D136, planı müzikli olan bir filmde ses kanalının ihraçta düşmesiydi. Çözümü
iki parçalıydı: ⑪'e beşinci komut (`ffprobe -select_streams a`), ve beş
rubriğin künyesine yeni `LINES HEARD` cümlesi — *"none — room tone present"*
ile *"none — no audio information at all"* ayrımı.

**Yama takıldı. Arıza tersine döndü.**

```
MASTER (ffprobe · ffmpeg):
  codec_name=aac · channels=2 · sample_rate=48000 · bit_rate=253434
  ebur128:  I = −17,3 LUFS · LRA 14,1 LU · tepe −0,9 dB
  silencedetect −50 dB / 0,3 s:  TEK ARALIK YOK  (65 saniye boyunca ses var)

ALTI RAPOR:
  ① ② ④ ⑤ ⑥   "LINES HEARD: none — no audio information at all"
  ③            "AUDIO ABSENT — RUN NOT STARTED ... The file contains no
                audio information across its full runtime."
```

Altı modelden altısı, 253 kbit/s'lik kesintisiz bir sesi "hiç ses bilgisi
yok" diye yazdı. ③ bunun üzerine STOP bloğu bastı ve **koşuyu hiç yapmadı** —
yani filmin ses tarafı ölçülmedi, ve ölçülmediği hiçbir tabloda görünmedi.

⭐ **Asıl ders yamada değil, yamanın CİNSİNDE.** D136 bir AYRIM öğretti
("iki ayrı gerçeği aynı kelimeyle yazma") ve modelin o ayrımı doğru yapacağını
varsaydı. Model ayrımı öğrendi ve **yanlış tarafını seçti** — çünkü ayrımın
girdisi bir DOSYA ÖZELLİĞİDİR, modelin duyusuyla değil `ffprobe` ile okunur.
Bir modele, kendi algısıyla ölçemeyeceği bir şeyi daha dikkatli ölçmesini
söylemek yamalanmış bir hata değildir; aynı hatanın kibar hâlidir.

**ÇÖZÜM — ① rubrikler DOSYA HAKKINDA HÜKÜM VEREMEZ (beş rubriğin künyesine):**

```
LINES HEARD: [n · every spoken line VERBATIM with its timecode, or "none"]

⛔ This line reports what you HEARD. It is not a statement about the file.
   You may never write that the file has no audio track, no audio
   information, no audio stream, or that the audio was stripped in export:
   that is a property of the container, it is read with one ffprobe command,
   and a model cannot observe it. Write "none — nothing audible to me" and
   put the question in FLAGS. A run that stops on this claim is a run that
   was never made.
```

**ÇÖZÜM — ② ③ SES rubriğinin STATE C bloğu bir ÖNKOŞULA bağlanır:**

```
STATE C — TOTAL DIGITAL SILENCE
⛔ You may declare STATE C only if the operator has pasted the audio-stream
   line of the file's own probe above, and it is empty. Without that line,
   what you have is STATE B with nothing audible to you: run categories 6-9
   and say so. The stop block is reserved for a MEASURED absence.
```

**ÇÖZÜM — ③ ölçüm çıktısı koşunun ÖNKOŞULU olur, tavsiyesi değil.**
Operatör rubriği yapıştırmadan önce `olcum_kapisi.sh` koşar ve çıktının
`SES KANALI: VAR/YOK` satırını rubriğin künye alanına yapıştırır. Yapıştırılan
satır yoksa ses ekseni o koşuda ÖLÇÜLMEMİŞ sayılır ve ③ satırı `— · ses
ekseni ölçülmedi` olur.

> 🔗 Ders 136 (bu dersin tersi — aynı yama, ters arıza) · Ders 125 (ölçüm
> kapısı: cevabı komut satırında duran soru modele sorulmaz) · Ders 129
> (SPEC yazıldı, mod D koşulmadı — aynı desen: belge eklemek davranışı
> değiştirmiyor) · Ders 80 (girdisiz koşu verdikt üretti).

---

## 🔴 DERS 150: ÜRETİCİ FİLİGRANI 315 SANİYENİN 315'İNDE DURUYORDU — ⑤ 31 SAHNEDE "EDGES: CLEAN" YAZDI, ① KUTUYU İŞARETLEMEDİ; KÖŞE TESTİ MAKİNE KAPISINA

**KAPI:** BETİK · `olcum_kapisi.sh` KÖŞE TESTİ (kose_SA.png) + `rapor_kontrol.py` ⑤ SUSKUNLUK — 01.09.2026
**TEKRAR:** 2 · 01.09.2026 THE COLD WELD ÖLÇÜLDÜ ve filigran DOĞRULANDI (sağ alt çeyrek, 6/6 örnek, cyan üçgen; merkez 4K'da ≈3450,1800 — köşeden %10/%17 içeride). ⚠️ Kapının ilk sürümü SABİT 360×240 kırpıyordu ve KAÇIRDI; 01.09.2026'da DÖRT ÇEYREĞE çevrildi (`olcum_kapisi.sh`). ⛔ %3 crop yetmez: temizlik kadraj genişliğinin %12'sini götürür.

**Kaynak:** THE SKYLIGHT (29.08.2026) — master köşe şeridi (`crop=360:240:iw-360:ih-240,
fps=1/30,tile=6x2`): 11 örneğin 11'inde sağ altta aynı "▷" ikonu; altı raporun
altısında filigran bulgusu 0 · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md`
**Sorun:** 2 film. 2. vaka THE FROST LINE (31.08.2026): aynı "▷" ikonu 235/235
saniye — ama bu kez ① TOP-3'üne, ⑤ her EDGES satırına yazdı: aşağıdaki ÇÖZÜM
②'nin yamaları İŞLEDİ; köşe testi teslim kusurunu yine bağımsız doğruladı
(Skylight'ta 1 film, 6 mercek, 315 saniye, 0 bulguydu).

Sabit bir kaplama, filmdeki en kolay ölçülen kusurdur — DEĞİŞMEYEN tek şey odur — ve
inceleyen model için en görünmez olanıdır: değişmediği için dikkat onu atar. ⑤'in
EDGES satırı 31 kez aynı kelimeyle doldu ("Clean") — D126'nın şablon belirtisi, bu
kez kenar satırında. ①'in negatif listesinde kutu var ("watermarks"), severity
yazılmadı. Kaplama aynı zamanda bir TESLİM kusurudur: üreticinin filigranını taşıyan
master master değildir — ve rubrikler DEĞİŞİM aradığı için her rubrikten sağ çıkar.

**ÇÖZÜM ① — ⑪ ölçüm kapısına KÖŞE TESTİ (`olcum_kapisi.sh`'e eklendi):**

```
ffmpeg -i "$M" -vf "crop=360:240:iw-360:ih-240,fps=1/30,tile=6x2" -frames:v 1 kose_SA.png
→ BAKILIR: aynı köşede aynı şekil her örnekte duruyorsa FİLİGRAN VAR →
  🔴 teslim kusuru; master filigransız yeniden ihraç edilir, koşu o master'a
  yapılır. Dört köşe için crop x/y değiştirilir (sol alt: crop=360:240:0:ih-240).
```

**ÇÖZÜM ② — kaynak rubrik ⑤ (EDGES satırı) ve ① (negatif kutu), İngilizce kural:**
```
A mark that sits in the same place in every scene is a watermark or a UI
remnant — name it and log it. "Clean" may not be written for an edge while a
static mark stands on it; a line that reads the same in every scene is a
template, not an observation.
```

**ÇÖZÜM ③ — ihraç listesi (KURGU_RITMI §6): "filigran 0 kare — köşe testi".**

> 🔗 Ders 125 (makineyle ölçülebilen sayı modele sorulmaz) · Ders 126 (şablon satır
> gözlem değildir) · Ders 34/70 (metin ve kart) · Ders 137 (dosya özelliği gözlemle
> ölçülmez — filigran da bir dosya özelliği gibi davranır: her karede aynı).

---

## 🔴 DERS 151: ÜÇ NOVUM VURUŞU EKRANDAYDI, ALTI MERCEK ÜÇÜNÜ DE GÖRMEDİ YA DA TERSİNE OKUDU — KAPI SAHNESİNİN a/b KARE ÇİFTİ OLMADAN "OLAY YOK / OLAY TERS" HÜKMÜ İŞLENMEZ

**TEKRAR:** 2 · 01.09.2026 THE COLD WELD: novumun üç kanıtı da EKRANDAYDI (avuç makrosu 65 s · diskli duvar 100-120 s · doruk 122 s) ve altı merceğin altısı üçünü de adlandırmadı; ② otuz bir diski "wall BUTTONS" sandı, ⑤ hiç saymadı. ⛔ ÇALIŞMIYOR → SPEC E bloğu a/b kare çifti zorunlu, mod D şart [D129 ile ortak].

**Kaynak:** THE FROST LINE (31.08.2026) — master kareleri: t56 (S5 dış yaması
HAVADA, T+6 — novumun gerçekçilik kanıtı) · t141→t147 (S15 yaprağı klip içinde
yeşil→gri) · t181→t187 (S19 yaprağı yeşil→beyaz). Raporlar: ⑤ "yama başarılıydı,
sonraki plume HATA" · ④ S19 = "Payoff: healthy leaf — rig worked" (KEEP) ·
①② S15 = "donuk yaprağa dokunuyor" · `01_FILM_RAPORLARI/THE_FROST_LINE.md`
**Sorun:** 1 filmde 3 vuruş, 6 mercek, 0 doğru okuma. THE SKYLIGHT'ta aynı desen
(④ "no peak located", sönüş 3:03→3:07 ekrandaydı) — bu 4. vuruş vakası.

Mekanizma: 10 saniyelik klibin T+5 civarındaki 1-2 saniyelik dönüşü (uçan yama,
beyazlanan yaprak, çarpılan kelepçe, sönen ışık) mod-V merceğin örneklemesinden
kaçıyor; mercek klibin BAŞINI okuyor ve durumu oradan yazıyor. Ters okuma,
görmemekten kötüdür: ④ filmin HER ŞEYİN KAYBI vuruşunu zafer diye puanladı,
⑤ tasarımın kanıtını "hata, boyayla sil" diye reçeteledi.

**ÇÖZÜM — operatör tarafı (rubrik yaması değil; ① KARE'nin SUB-MILLIMETRE
EVENT kuralı zaten var ve yetmiyor):**

```
① SPEC E bloğu, her viral/doruk/novum sahnesine E7/E8 biçiminde a/b kare
   çifti komutu yazar (a = dönüş öncesi saniye, b = sonrası):
     ffmpeg -ss <a> -i "$M" -frames:v 1 a.jpg · ffmpeg -ss <b> -i "$M" -frames:v 1 b.jpg
② ⑪ ölçüm kapısı bu çiftleri HER koşuda çıkarır ve GÖZLE karşılaştırır.
③ Bir raporun "olay yok / olay ters / bu sahne kesilsin" hükmü, o sahnenin
   a/b çifti bakılmadan film kaydına İŞLENMEZ. Kare raporla çelişirse KARE
   kazanır [D125]; kayda "rapor tersine okudu" yazılır ve o merceğin ilgili
   hücresi kaynağını kaybeder.
```

> 🔗 Ders 141 (FİNAL VURUŞ KANITI — bu ders onu bütün kapı sahnelerine ve rapor
> HÜKÜMLERİNE genişletir) · Ders 125 (ölçüm kazanır) · Ders 129 (asıl ilaç mod D:
> SPEC vuruş saniyesini merceğe baştan söyler) · Ders 130 (düşen bulgu puanı geri verir).

---

## 🔴 DERS 156: PLANIN "VAR" DEDİĞİ HER ŞEY GELDİ, "SIFIR" DEDİĞİ HER ŞEY DÜŞTÜ — SIFIRI KİMSE ÖLÇMÜYOR VE MOD V EN AĞIR İHLALE PARTİNİN EN YÜKSEK PUANINI VERDİ

**Kaynak:** THE PAYLOAD QA (01.09.2026) — altı mercek, altısı da mod V ·
`01_FILM_RAPORLARI/THE_PAYLOAD.md`
**Sorun:** teslim edilen film, planın POZİTİF yapısını kusursuz taşıyor ve
SIFIR kilitlerinin hepsini kırıyor. Ve bu, bir arıza değil bir DESENDİR.

```
PLANIN POZİTİF YAPISI — beş mercek de doğruladı, hiçbiri sapmadı:
  sahne sayısı        24        ✅  (plan 24)
  sahne sırası        S0→S23    ✅  (rapor haritası plan haritasıyla eşleşiyor)
  İNSAN ŞERİDİ        111111111111-111-1-1--1-
                                ✅  planın şeridiyle KARAKTER KARAKTER AYNI
                                    (plan: 111111111111011101010010)
  mekânlar            ova · pist · yük yatağı · yörünge   ✅

PLANIN SIFIR KİLİTLERİ — beşi de düştü:
  replik 0            → 4 replik  (1:11 · 1:15 · 1:18 · 2:51)
  ekran metni 0,0 s   → başlık kartı 4:00-4:06 + "PHASE 1" + "EVA" [D155]
  insan 1 / klon 0    → 1:40'ta klon (② 🔴 · ⑤ 🔴)
  kasa 9              → ~15 → 8 (② ve ⑤ aynı çelişkiyi ayrı ayrı yazdı)
  müzik sessizliği 3  → duvardan duvara müzik, tek sessizlik yok
```

⭐ **MEKANİZMA — SIFIR GÖRÜNMEZ.** Var olması gereken bir şey teslimde
ARANIR: sahne sayılır, şerit okunur, süre ölçülür. Olmaması gereken bir şey
ARANMAZ, çünkü onu aramak için önce onun yasak olduğunu bilmek gerekir —
ve o bilgi yalnızca SPEC'tedir. Mod V merceğin elinde SPEC yoktur; dolayısıyla
mod V, bir sıfır kilidini **ihlal olarak değil MALZEME olarak** okur.

⛔ **VE ÖDÜLLENDİRİR.** Bu partinin en yüksek puanı ③ SES'e aittir:
**8,4/10 · "SOUNDTRACK HOLDS"** — planı `HUMAN 0 · MACHINE 0 · TELSİZ 0`
olan bir filme. Rapor dört repliği duydu, konuşmacı atamasını 10/10 verdi,
ses kimliğini 10/10 verdi. Hepsi kendi ölçütüne göre DOĞRU: replikler
temiz, tek sesli ve tutarlı. Ölçüt yanlış değil; ÖLÇÜLEN ŞEY yanlış.
Aynı desen ④'te tersinden çıktı: HİKAYE merceği "narrating the visible"
diye repliği YAZIM kusuru sandı ve rewrite reçetesi yazdı — oysa o replik
filmde HİÇ OLMAMALIYDI; bu bir yazım kusuru değil TESLİM SAPMASIDIR.

**ÇÖZÜM — SPEC'E "SIFIR KİLİTLERİ" BLOĞU, ⑪'E KİLİT BAŞINA BİR KOMUT:**

```
① SPEC'in C bloğu zaten sıfırları yazıyor ama DAĞINIK. Hepsi tek listede
   toplanır ve her satır ÖLÇÜLEBİLİR biçimde yazılır:

   SIFIR KİLİTLERİ (teslimde ARANACAK yokluklar)
   Z1 replik                0      → kulakla + ⑪: konuşma bandı taraması
   Z2 ekran metni           0,0 s  → ⑪ köşe testi + 6 rastgele karede OCR gözü
   Z3 kart/jenerik          0 kare → E1 süre = gövde süresi (kart varsa Δ>0)
   Z4 klon / ikinci figür   0      → İNSAN ŞERİDİ + sıcak nokta karesi
   Z5 sayılabilir nesne     n = 9  → kapı sahnesinin tek karesinde SAY
   Z6 müziksiz pencere      3      → silencedetect + müzik stem'i

② ⑪ ÖLÇÜM KAPISI bu listeyi HER koşuda satır satır basar. Sıfır kilidi
   ölçülmeden "film teslim edildi" yazılmaz.
③ MOD D ZORUNLU HÂLE GELİR: sıfır kilidi listesi merceğe VERİLMEDEN
   koşulan mercek, o filmin en ağır ihlallerini yapısal olarak göremez.
   (Bu filmde SPEC vardı ve altı koşunun altısı mod V idi — SPEC yazılmış
   olduğu hâlde mod V koşulan film sayısı artık 8.)
```

⚠️ **DÜRÜST KAYIT:** Bu ders master ölçülmeden yazıldı — ⑪ kapısı
koşulamadı (dosya operatörde). Yukarıdaki sıfır ihlallerinin hepsi RAPOR
KAYNAKLIDIR ve ikisi (metin, klon) iki ayrı mercek tarafından bağımsız
yazılmıştır. Kare doğrulaması ⬜ AÇIK: master gelince 0:10 · 1:18 · 1:40 ·
1:30/1:40 · 4:00 kareleri çıkarılır [D125 — çelişkide KARE kazanır].

> 🔗 Ders 129 (SPEC varken mod V — bu ders onun BEDELİNİ ölçer) · Ders 136/137
> (ses ekseninin plan↔teslim kopukluğu) · Ders 141 (final vuruş kanıtı — orada
> "olması gereken", burada "olmaması gereken") · Ders 118 (insan şeridi — bu
> filmde ŞERİT TUTTU ve sıfırlar düştü: şerit sıfır kilidi ölçmez) · Ders 150
> (filigran: sıfır kilidinin ilk vakası, köşe testi oradan geldi).

---

## 🔴 DERS 159: DÖRT MERCEK AYNI BULGUYU BİREBİR AYNI CÜMLEYLE YAZDI — VE BULGU YANLIŞTI; ⑤ KAPISI SAYILARI KARŞILAŞTIRIYOR, CÜMLELERİ DEĞİL

**Kaynak:** THE FROST LINE · 2. QA partisi (01.09.2026) — ① KARE 6,3 ·
`3:23 — 🔴 BLOCKER — Contact morphing. Fingers phase through the solid
helmet visor.`

**Sorun:** Altı merceğin dördü aynı saniyeyi aynı kelimelerle rapor etti:

```
① KARE   TOP-3 / DETAILED ERROR LOG · 🔴 BLOCKER
④ HİKAYE OUT-OF-SCOPE FLAGS: "3:23 — Fingers phase through the glass
         visor of the helmet → FRAME lens."
⑤ ARKA   OUT-OF-SCOPE FLAGS: "3:23 (S21) — Subject's fingers phase
PLAN     directly through the solid glass visor of his helmet → FRAME lens."
⑥ FİZİK  OUT-OF-SCOPE FLAGS: "3:23 — Fingers phase directly through the
         glass visor of the helmet → FRAME lens."
```

Üçünün de kapsam listesi bu bulguyu AÇIKÇA dışlar (④ teknik kusur yazmaz,
⑤ özneyi puanlamaz, ⑥ sayısız bulgu taşımaz). Üç bağımsız model aynı
saniyede aynı olayı bulabilir; aynı cümleyi kuramaz. Bu bir doğrulama
değil, tek bir oturumun kendi çıktısını dört kez raporlamasıdır.

**Ve bulgu yanlıştı.** 4K master'dan çıkarılan üç kare (t202 · t203 · t204,
kafa bölgesi tam çözünürlükte kırpıldı): eldiven vizörün **ÖNÜNDE**, cam
çerçevesi ve pane kenarı okunuyor, hiçbir parmak cama girmiyor. Mercek,
**örtmeyi (occlusion) füzyon sandı** — ve o yanlış 🔴, ①'in REGENERATE
hükmünü taşıyan dört 🔴'dan biriydi.

D110 bu arızayı zaten adlandırıyor ama YANLIŞ YERDE arıyor: "severity
sayıları ve sahne sınırları birebir tutuyorsa bu KOPYADIR". Bu partide
sayılar TUTMADI (① 21 kesme, diğerleri 22) ve kapı ✅ verdi. Kopyanın izi
sayıda değil, **cümlede** duruyordu.

**ÇÖZÜM — ⑤ ÇAPRAZ SAYIM KAPISINA DÖRDÜNCÜ SATIR: METİN ÇAKIŞMASI**

```
④ METİN SATIRI. Raporların OUT-OF-SCOPE FLAGS ve THE THREE THAT MATTER
   satırları yan yana konur ve şu iki testten geçirilir:

   a) AYNI SANİYE + AYNI NESNE + AYNI FİİL iki farklı mercekte mi?
      → o gözlem, kapsamı GEREĞİ SAHİBİ OLAN merceğin dışındaki her
        rapordan SİLİNİR ve yerine "→ <mercek>" işaretçisi yazılır.
   b) İşaretçi bırakan mercek sayısı ≥ 2 ise oturum 🚨 KOPYA'dır:
      bulgu KAREYLE doğrulanmadan hiçbir tabloya, hiçbir tally'ye ve
      hiçbir verdict'e girmez.

⛔ SIRA ÖNEMLİ: kopyalanan bulgu, doğru bulgudan daha hızlı yayılır —
   çünkü doğru bulgu ölçüm ister, kopya yalnız yapıştırma ister. Bir
   partide N mercekte görünen bir bulgu N kat daha GÜVENİLİR değildir;
   bağımsızlık kanıtlanmadıkça N kat daha ŞÜPHELİDİR.
```

**Ve operatör tarafında tek satır:** her mercek TEMİZ oturumda koşulur
(D110). Bu partide altısı da tek oturumdan geldi ve dördü tek bir yanlışı
taşıdı.

> 🔗 Ders 110 (bağımsızlık şüphesi — bu ders onun ölçülebilir izini verir) ·
> Ders 107 (⑤ çapraz sayım) · Ders 108 (çapraz gözlem birleştirme — sahiplik
> zaten oradaydı, eksik olan SİLME adımıydı) · Ders 125 (çelişkide ölçüm
> kazanır — burada kareyi çıkaran taraf dördünü birden çürüttü) · Ders 151
> (karesiz hüküm işlenmez — bu, o kuralın TERSİ yönü: karesiz 🔴 da işlenmez).

---

## 🔴 DERS 160: MASTER'IN DOSYA ADI KİMLİK DEĞİLDİR — AYNI ADI TAŞIYAN BEŞ DOSYANIN İKİSİ BAŞKA BİR FİLMDİ VE ÜSTÜNDE BU FİLMİN KAPAK KARTI VARDI

**Kaynak:** THE FROST LINE · 2. QA partisi (01.09.2026) — ⑪ ölçüm kapısı.
Sahip master yolu vermeden altı rapor gönderdi.

**Sorun:** `~/Downloads` içinde **"the frost lıne" adıyla beş dosya** vardı:

```
the frost lıne.mp4        235,201 s · 1280×720 · t105 = sera tüneli   ✅ bu film
the frost lıne (1).mp4    235,201 s · 1280×720 · aynı kurgu           ✅ bu film
the frost lıne (2).mp4    235,201 s · 3840×2160 · aynı kurgu          ✅ bu film (4K)
the frost lıne .mp4       245,120 s · 1280×720 · t105 = TOZ FIRTINASI 🔴 BAŞKA FİLM
the frost lıne  (1).mp4   245,120 s · 3840×2160 · aynı yabancı gövde  🔴 BAŞKA FİLM
```

Ad farkı yalnız **bir boşluk**. 245 s'lik çiftin gövdesi bambaşka bir film
(kasalarını toza dik dizen adam · toz duvarı · dikey iniş aracı · ranza ·
yörünge · kenetlenme) — **ama kuyruğunda BU FİLMİN kapak kartı duruyor.**
Yani kimliği doğrulamak için bakılabilecek en görünür işaret, tam olarak
yanlış filmi işaret ediyordu.

Bu, D105'in (kimlik kapısı) tersten hâlidir. D105 RAPORUN filme ait olup
olmadığını sorar ve "ekrandaki yazı çapa değildir" der. Ama aynı yasak
DOSYA için hiçbir yerde yazılı değildi: ⑪ ölçüm kapısı süreyi, fps'i,
sesi, filigranı ölçüyor — **hangi filmi ölçtüğünü hiç sormuyor.** Bir
sonraki koşuda 245 s'lik dosya seçilseydi, iki filmin kaydı birden
zehirlenirdi: bu filme ait olmayan bir kurgu bu filmin adına ölçülür,
öteki film de ölçülmemiş sayılmaya devam ederdi.

**ÇÖZÜM — ⑪ ÖLÇÜM KAPISININ İLK ADIMI: KİMLİK KARESİ**

```
⑪.0  MASTER KİMLİĞİ — ölçümden ÖNCE, tek komut, ~5 saniye:

     ffmpeg -ss <süre/2> -i "$M" -frames:v 1 kimlik.jpg

     Kurgunun ORTASINDAN bir kare çıkarılır ve BAKILIR. Kart, jenerik ve
     kapak bu karede olamaz; gövdenin kendisidir.
     · Karedeki mekân/kostüm/nesne SPEC'in C bloğuna oturuyor mu?
     · Oturmuyorsa: ⛔ KOŞU DURUR. Bu dosya o film değildir.

⑪.0b AYNI ADDAN BİRDEN ÇOK DOSYA VARSA HEPSİ ÖLÇÜLÜR:
     for f in <klasör>/*<ad>*; do
       printf '%s ' "$f"; ffprobe -v error -show_entries format=duration \
         -show_entries stream=width,height -of csv=p=0 "$f" | tr '\n' ' '; echo
     done
     Farklı SÜRE = farklı kurgu. Farklı kurgu, aynı ad taşısa bile aynı
     film değildir; hangisinin ölçüldüğü film kaydına YAZILIR.

⑪.0c RAPORUN KÜNYESİNE MASTER YOLU YAZILIR — ham raporun başındaki
     operatör künyesinde `girdi: <tam dosya yolu> · <süre> s · <çözünürlük>`
     satırı bulunmayan koşu, hangi dosyaya koşulduğu BİLİNMEYEN koşudur.

⛔ VE KAPAK KARTI ASLA KİMLİK KANITI DEĞİLDİR — ne rapor için (D105),
   ne dosya için. Bu vakada kart, yanlış filmin kuyruğundaydı.
```

**İkinci bulgu, bedavaya:** kapak kartı kurguya eklenmesin diye yazılan
D70/D72, burada ikinci bir maliyet ürettiğini gösterdi — kart yalnız
döngüyü öldürmüyor, **yanlış filmi doğru film gibi imzalıyor.**

> 🔗 Ders 105 (kimlik kapısı — raporu filme bağlar; bu ders DOSYAYI filme
> bağlar) · Ders 125 (ölçüm kapısı — kimlik adımı onun başına girer) ·
> Ders 70/72 (kapak kartı kurguya eklenmez) · Ders 112 (çapraz film parmak
> izi — o kapı iki RAPORU karşılaştırır, bu kapı iki DOSYAYI).

---

## 🔴 DERS 161: ALTI RAPORUN BEŞİ KENDİ ARİTMETİK KAPISINDAN GEÇEMEDİ — VE BİRİ, HİÇBİR HÜCRE KÜMESİNİN ÜRETEMEYECEĞİ BİR TOPLAM BASTI

**KAPI:** BETİK · `RAPOR_KONTROL/rapor_kontrol.py` (①.5 aritmetik · tally · şerit · ⑨ ızgara · ④ harita) — 01.09.2026
**TEKRAR:** 2 parti · son vaka 02.09.2026 (THE STILL SWARM — **8 raporun 7'sinde** tally ≠ yazılı etiketler; ⑦'de 2, ⑧'de 1 kaynaksız hücreye 10/10) · ⭐ ÇALIŞIYOR: betik hepsini otomatik yakaladı ve verdict'leri düşürdü — ders artık ARAÇTIR, kural değil

**Kaynak:** THE COLD WELD QA (01.09.2026) — altı mercek, altısı mod V. Her
rubrik "ARITHMETIC GATE — write these three numbers BEFORE the score" diye
kendi kapısını taşıyor. O kapı **hiçbir dış kapı tarafından denetlenmiyordu**
ve altı raporun beşi ondan geçemedi. Toplamı yeniden hesaplamanın maliyeti
bir toplama işlemidir; bulunanlar şunlar:

```
mercek        iddia n / Σ / ort   hücrelerden n / Σ / ort   sonuç
① KARE            8 / 41,0 / 5,1        8 / 41,0 / 5,1      aritmetik ✅
② DEVAMLILIK     13 / 115,0 / 8,8      12 / 108,0 / 9,0     ⛔ FABRİKE
③ SES             4 / 24,0 / 6,0        4 / 24,0 / 6,0      aritmetik ✅
④ HİKAYE          9 / 51,0 / 5,6        9 / 51,0 / 5,7      ⛔ yuvarlama
⑤ ARKA PLAN       6 / 30,0 / 5,0        6 / 30,0 / 5,0      ✅ (partideki tek temiz rapor)
⑥ FİZİK           5 / 31,0 / 6,2        5 / 31,0 / 6,2      aritmetik ✅
```

⭐ **AMA TOPLAMA İŞLEMİ KAPININ YALNIZ YARISI.** Rubriklerin kendi ④ ve
"DECLARED ABSENCE" kuralları toplama ile görünmeyen üç ihlal daha üretti ve
üçü de ① ③ ⑥'da, yani "aritmetik ✅" satırlarında duruyor:

```
① KARE      Diyalog & Ses 3/10 — film 0 replikli ama SES TASARIMLI (drone +
            temas dokusu). Rubriğin N/A kuralı "silent by design" içindir ve
            kategori 8 vakumda SES FİZİĞİNİ de ölçer; −4'ün kaynağı F1
            ("havadan ses") tam o kapsamdadır. Yani hücre KURAL İHLALİ DEĞİL —
            ama F1 kilit defterinde ⬜ AÇIK (temaslı ses ↔ havadan ses kulakla
            ayrılır): hücre doğrulanmamış. Betik bu hücreyi ÇEVİRMEZ, insan
            kararına bırakır. ①'in asıl arızası başka yerde: tally 🟡1 yazdı,
            kendi logu 2 🟡 taşıyor (0:50 ışık · 0:30 hareket).
③ SES       Dört hücrenin ÜÇÜNDE Issue gözü "No in-scope source" yazıyor ve
            üçü de sayı taşıyor. Rubriğin kendi ④ kuralı tek cümle: "the
            phrase wins" — o üç hücre `—` olmalıydı. Ayakta kalan tek hücre
            (SFX 5/10) bir ortalama değildir; ③ aslında TEK ŞEY ölçtü.
⑥ FİZİK     Severity tally 🔴0 🟠1 🟡3 = 4 etiket; raporda yazılı etiket 2.
            Rubriğin kendi ⑤ kuralı: "count the tally from the findings, not
            from memory". Verdict o tally'den türetildi.
```

⛔ **NEDEN BU BİR SÜREÇ DERSİDİR, PROMPT DERSİ DEĞİL:** rubrik kuralı ZATEN
yazıyordu. Altı rubriğin altısında, büyük harfle, ⛔ işaretiyle. Yazılı kural
tutmadı çünkü **onu ölçen bir kapı yoktu** — deponun 26.08 bulgusunun aynısı
("sistem neyi ölçüyorsa onu optimize etti"). Model kendi bastığı tabloyu
toplamıyor; kimse de toplamıyordu.

**ÇÖZÜM — ORTAK ADIM ①.5 · RAPOR ARİTMETİĞİ KAPISI (⑤'ten ÖNCE koşar):**

```
Her rapor için, RAPORUN KENDİ TABLOSUNDAN, dört satır:

  a) n     = sayı taşıyan hücre sayısı            (N/A · — · UNVERIFIABLE hariç)
  b) Σ     = o hücrelerin toplamı
  c) Σ/n   = raporun OVERALL'ıyla aynı mı (±0,05)
  d) tally = raporda FİİLEN yazılı 🔴🟠🟡 etiketleri sayılır

  a-c tutmuyorsa           → o merceğin satırı 🚨 GEÇERSİZ, tabloya girmez
  d tutmuyorsa             → verdict geçersiz; REGENERATE hükmü UYGULANMAZ
  "no in-scope source" + sayı aynı hücrede → hücre `—` sayılır, a ve b
                             yeniden hesaplanır [D131]
  0 replikli filmde diyalog hücresi sayı taşıyorsa → hücre N/A'ya çevrilir,
                             a ve b yeniden hesaplanır

Maliyet: rapor başına ~20 saniye. Bu vakada 6 raporun 5'ini yakalardı.
```

⛔ **VE BU KAPI, ⑤'İN GÖREMEDİĞİ BİR ŞEYİ GÖRÜR.** ⑤ raporları BİRBİRİYLE
karşılaştırır; bu kapı her raporu KENDİSİYLE karşılaştırır. ② DEVAMLILIK bu
partide ⑤'ten geçseydi bile — kesme sayısı ötekilerle aynıydı (14) — toplamı
yine fabrikeydi ve 8,8 tabloya girecekti.

> 🔗 Ders 107 (⑤ çapraz sayım — raporlar arası) · Ders 130/131 (⑩ sonrası
> puan geri verilir · kaynaksız hücre `—`) · Ders 129 (mod V ön koşu) ·
> Ders 125 (ölçüm kapısı: komut satırında cevabı duran soru modele sorulmaz —
> bu ders onun rapor tarafıdır: kâğıtta cevabı duran toplama modele sorulmaz).

---

## 🔴 DERS 162: FİLİGRANI ⑤ GÖRDÜ, SAHİBİ ① GÖRMEDİ — VE HİÇBİR KAPI İKİ HÜCREYİ YAN YANA KOYMUYOR; ⑤ MUTABAKATI ÖLÇÜYOR, SUSKUNLUĞU ÖLÇMÜYOR

**KAPI:** BETİK · `RAPOR_KONTROL/rapor_kontrol.py` ⑤ SUSKUNLUK (çoklu rapor modu: film boyu iddia ↔ sahibin sessizliği) — 01.09.2026

**Kaynak:** THE COLD WELD QA (01.09.2026). ⑤ ARKA PLAN raporu, 15 sahnenin
15'inde `EDGES: static cyan triangle mark, bottom right` yazdı, aralığı
verdi (`0:00-2:29`), kendi 9. kategorisinden −2 puan düşürdü ve
"THE THREE THAT MATTER" listesine koydu.

**① KARE — o işaretin SAHİBİ — hiç görmedi.** ①'in negatif çekirdek listesinde
kutu kelimesi kelimesine duruyor: *"Text, subtitles, captions, or watermarks
visible on screen — a static corner mark present in every scene counts; it is
never intentional set dressing and is ticked and logged with a severity tag."*
① üç kutu işaretledi ve bu onlardan biri değildi. ① ayrıca kendi rubriğinin
zorunlu iki denklik satırını (`NEGATIVE BOX COUNT / LINKED / UNLINKED` ve
`FINDINGS WITH A MATCHING BOX / TICKED / MISSED`) hiç basmadı.

```
⛔ VE ⑤ ÇAPRAZ KAPISI BUNU YAPISAL OLARAK GÖREMEZ.

⑤'in dört satırı da MUTABAKAT arar:
  sayım   — aynı sayıyı mı verdiler
  replik  — aynı repliği mi duydular
  şerit   — aynı diziyi mi yazdılar
  metin   — aynı cümleyi mi yazdılar (D159: kopya avı)

Dördü de "İKİ RAPOR AYNI ŞEYİ SÖYLEDİ Mİ?" sorusudur.
Hiçbiri "BİR RAPOR SÖYLEDİ, SAHİBİ SUSTU MU?" diye sormaz.

Ve bu vakada tek bir mercek konuştu: D159'un kopya kapısı SIFIR sonuç verir,
D108'in birleştirme tablosu tek satırlı bir gözlem görür ve normal işler.
Film boyu 🔴 bir ihlal, hiçbir kapıyı tetiklemeden partiden çıkar.
```

⭐ **SUSKUNLUK BİR ÖLÇÜMDÜR.** Bir mercek FİLM BOYU süren bir ihlal bildirdiyse
(15/15 sahne · her karede), o ihlalin sahibi olan merceğin AYNI şeyi görmemiş
olması iki şeyden biridir ve ikisi de eylem gerektirir:
① ihlal yoktur → bildiren merceğin o kategorisi 🚨
② ihlal vardır → sahibi mercek O KATEGORİDE KÖRDÜR ve tüm koşusu şüphelidir

**ÇÖZÜM — ⑤'E BEŞİNCİ SATIR: SUSKUNLUK KAPISI**

```
⭐ BEŞİNCİ SATIR: FİLM BOYU İDDİA [Ders 162].
   Bir raporda, HER sahneyi ya da runtime'ın ≥%80'ini kapsayan bir ihlal
   iddiası varsa (filigran · sabit köşe işareti · sürekli metin · her
   sahnede aynı kusur), o iddia SAHİBİ olan merceğin AYNI KUTUSUYLA yan
   yana konur:

     | iddia (mercek · timecode aralığı) | sahibi mercek | sahibi ne dedi |

     sahibi AYNI şeyi yazdıysa   → gözlem doğrulandı, D108 normal işler
     sahibi SUSTUYSA             → 🚨 SUSKUNLUK: iddia KAREYLE çözülür
                                    (⑪ köşe testi ya da tek kare), ve
                                    çözülene kadar HER İKİ merceğin de o
                                    kategorisi sayı taşımaz

⛔ SAHİPLİK TABLOSU (kim neyin sahibi — rubriklerin kapsam listelerinden):
   ekran metni · filigran · altyazı · köşe işareti          → ① KARE
   arka plan figürü · kalabalık · ufuk · kadraj kenarı       → ⑤ ARKA PLAN
   kimlik · kostüm · aşınma · taşınan nesne                  → ② DEVAMLILIK
   ses kanalı · ambiyans · replik atfı                       → ③ SES
   ölçülmüş fizik (g · süre · mesafe · oran)                 → ⑥ FİZİK
```

⛔ **BU DERS D150'NİN YERİNE GEÇMEZ, ONU TAMAMLAR.** D150 filigranın
ÜRÜNDEKİ çözümünü verdi: teslimden önce ⑪ köşe testi. Bu ders filigranın
RAPORDAKİ çözümünü verir: köşe testi koşulamadığında (bu vakada master
depoda yoktu) tek kalan sinyal iki merceğin ayrışmasıdır — ve o sinyal
şimdiye kadar okunmuyordu.

> 🔗 Ders 150 (filigran · ⑪ köşe testi — ürün tarafı) · Ders 159 (⑤ dördüncü
> satır · kopya avı — bu dersin tersi: o AYNILIĞI, bu FARKLILIĞI ölçer) ·
> Ders 108 (çapraz gözlem birleştirme) · Ders 107 (⑤) · Ders 125 (⑪).

---

## 🔴 DERS 163: İNSAN ŞERİDİ TEK FİGÜRLÜ FİLMDE SABİTTİR — DÖRT SAHNELİK BLOK TAKASI ŞERİDİ HİÇ BOZMADAN GEÇTİ VE ④c "SIRA DOĞRULANDI" DEDİ

**KAPI:** BETİK · `qa-isle/scripts/olcum_kapisi.sh` → **SAHNE IZGARASI** (kesme
listesinden türetilir, her sahnenin ORTASINDAN birer kare, SPEC B bloğunun sahne
haritasıyla yan yana okunur) — 01.09.2026
**TEKRAR:** 0

**Kaynak:** THE COLD WELD ⑪ ölçüm kapısı (01.09.2026) —
`01_FILM_RAPORLARI/THE_COLD_WELD.md` §⑪.4. Master ölçüldü, sahne ortası kareleri
planın sahne haritasıyla eşlendi.

**Sorun:** D118 kurgu kapısına ÜÇÜNCÜ maddeyi (İNSAN ŞERİDİ) getirdi ve doğruydu:
sıra, sayı ve süreden bağımsız bir boyuttur. Ama şerit **"kaç GÖVDE"** diye sorar.
Bu filmde S0 dışındaki 14 sahnenin 14'ü tek insanlıdır:

```
plan   : -11111111111111
② ⑤ ⑥ : -11111111111111   ← üç mercek BAĞIMSIZ üretti, üçü de plana birebir
④c     : "SIRA DOĞRULANDI" ✅

EKRANDA İSE (sahne ortası kareleri, ⑪):
  85 s  plan S8  DUVAR (31 disk)        → ekranda ANAHTAR tutma
  95 s  plan S9  duvar dağılır          → ekranda makro el + anahtar
 105 s  plan S10 anahtarı almak         → ekranda DUVAR
 115 s  plan S11 anahtar basamak olur   → ekranda DUVAR geniş plan
  → ANAHTAR bloğu ile DUVAR bloğu YER DEĞİŞTİRMİŞ. Şerit kılı kıpırdamadı.
```

⭐ **MEKANİZMA — ŞERİDİN ÇÖZÜNÜRLÜĞÜ İNSANSIZ SAHNE SAYISI KADARDIR.**

```
Şerit yalnız `1` ve `-` harflerini taşır; ayırt edici gücü, dizideki `-`
sayısına ve dağılımına eşittir.
   -111111111111-11111-1111-   (LOSS OF LIFT · 4 insansız)  → sıra gerçekten ölçülür
   -11111111111111             (THE COLD WELD · 1 insansız) → yalnız İLK sahne sabitlenir
   111111111111111             (0 insansız)                 → şerit HİÇBİR ŞEY ölçmez
Tek kâşifli bu seride şeridin varsayılan hâli üçüncü satırdır; yani D118'in
kapısı tam da bu depoda en zayıf çalıştığı yerde "geçti" der.
```

**Bedeli anlatıda ölçülür, kurguda değil:** TOHUM (S2'nin tek parlak yaması) ile
ödemesi (diskli duvar) arasındaki mesafe değişti ve novumun ikinci nesnedeki
kanıtı doruktan ÖNCE değil doruğa BİTİŞİK geldi — `ONERME §5`'in
"kurulum → doğrulama → sonuç" dizisi bozuldu. Üç mercek de o sırayı doğru sandı
ve ④ HİKAYE yapıyı o sıraya göre puanladı.

**ÇÖZÜM — ④ KURGU KAPISINA BEŞİNCİ SATIR: SAHNE IZGARASI**

```
bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh "<master>"
  → sahne_izgarasi.jpg  (kesme listesinden TÜRETİLİR: her aralığın ortasından
    bir kare, 4 sütunlu tile, soldan sağa/üstten alta)
  → SPEC B bloğunun sahne haritasıyla YAN YANA okunur: "kare n, planın n.
    sahnesi mi?" — sayı değil GÖRÜNTÜ karşılaştırması, ~60 saniye.

⛔ ŞERİDİN KENDİSİ DE BİR SAYI ÜRETİR VE O SAYI KAYDA YAZILIR:
     ŞERİT ÇÖZÜNÜRLÜĞÜ = insansız sahne sayısı / toplam sahne
   ≤ 1/10 ise ④c satırı "GEÇTİ" DEĞİL "ÖLÇMEDİ" yazar ve sıra ekseni
   yalnız ızgaradan okunur. Bir kapının kendi körlüğünü ilan etmesi,
   yanlış "geçti" demesinden ucuzdur.
```

> 🔗 Ders 118 (şerit — bu dersin atası; kural iptal DEĞİL, çözünürlük şartı
> eklendi) · Ders 121 (Δ okuma — insansız yuva yoksa Δ de okunamaz) ·
> Ders 135 (rubrik "2" üretemez; bu ders şeridin öteki sınırı) · Ders 141
> (final vuruş kanıtı — kare ile koşan dördüncü satır) · Ders 151 (mercek
> vuruşu göremez) · ONERME §5 (kurulum → doğrulama → sonuç dizisi).

---

## 🔴 DERS 164: RUBRİĞİN KENDİ ANLATTIĞI TARİF RAPORDA GERİ GELİNCE ÇAPA SANILDI — DÖRT ÇAPANIN DÖRDÜ DE YANKIYDI; KİMLİK KAPISI ANCAK KATALOGSUZ BİR GEÇİŞLE KOŞULABİLİR

**KAPI:** KARAR · faz QA rubriği İKİYE bölünür — A kör geçiş (katalog/pasaport
YOK, ayrı sohbet) + B katalog geçişi; ③ KİMLİK KAPISI **yalnız A'nın
pasaportundan** koşulur, B'nin pasaportu kapıya girmez.
**TEKRAR:** 0

**Kaynak:** YERÇEKİMİ — FAZ 1 faz koşusu (01.09.2026, mod V): ③ önce
"✅ GEÇTİ (4 çapa)" yazıldı, **aynı gün geri alındı → UNATTRIBUTED**.
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/YERCEKIMI.md` §KOŞU 1 ③ · §KOŞU 2 ③.

**Sorun:** Kimlik kapısı "belgeye eşlenen **metin-dışı** çapa ≥ 2" ister. Ama
rubrik, denetçinin işini yapabilmesi için tarifleri ÖNDEN verir: yüz, vizör
geometrisi, şerit rengi, sayaç değeri — hepsi promptun içindedir. Denetçi
onları geri yazınca eşleşme SAYILDI. Sayılan dördün dördü de rubriğin kendi
cümleleriydi. En açık vaka: rubriğin "açık madde" bloğu sırt ünitesinin İKİ
tasarımını da kelimesi kelimesine yazıyordu; denetçi birini seçip aynı
kelimelerle geri verdi — bu bir gözlem değil, **iki seçenekli yazı-turadır**.

⛔ Kapı yapısal olarak kördü: aynı belgeden hem SORUYU hem CEVABI veriyorduk.
Ve kapı "geçti" dediği için, aynı raporun kubbe-vizör / sırt-ünitesi /
giyside-yazı bulguları "doğrulanmış" sanıldı.

**ÇÖZÜM — RUBRİK MİMARİSİ DEĞİŞTİ (yama değil, ikiye bölme):**

```
A · KÖR GEÇİŞ   makara + STEP'ler.  Katalog YOK · pasaport YOK · kilit YOK ·
                renk YOK · sayı YOK · yön YOK. Denetçi tarifi KENDİ yazar.
                ⛔ İkili seçenek sunmak da sızıntıdır: "düz cam mı, kubbe mi"
                   diye sorulmaz — "kaç düz kenarı var, kaç köşesi var" sorulur.
B · KATALOG     tam rubrik, tam kilit, skor. AYRI SOHBET (A'nın çıktısı B'yi
                kirletir; aynı sohbette koşulursa A'nın tüm değeri sıfırlanır).

③ KAPISI:  yalnız A'nın PASSPORTS AS SEEN bölümünden koşulur.
BULGU GÜCÜ: A+B ikisi de → SAĞLAM · yalnız B → ŞÜPHELİ (yankı olabilir) ·
            yalnız A → GERÇEK ama ölçüsüz.
```

**ÖLÇÜLDÜ (aynı film, ertesi faz, aynı motor):** kör geçiş **8 yankısız çapa**
üretti ve biri SAYISALDI — söylenmemiş bir sayacı ("sol bilekte dört segment
yanıyor") doğru saydı. Söylenmemiş bir sayıyı doğru saymak, kapının
kabul edebileceği en güçlü kanıttır. Aynı geçiş, F1'de "sırtında çanta var"
diye rapor edilen kilidi de **kendi gözüyle** "sırtında kesinlikle hiçbir şey
yok" diye çürüttü.

⭐ **YAN ÜRÜN — KARIŞIK SIRA ÖLÇÜ ALETİNE DÖNDÜ.** Kör geçişe "klipler karışık,
SEN sırala ve her yerleştirmenin kanıtını yaz" denir. Çıkan sayı
**SIRA SKORU = doğru yerleşen klip / toplam** filmin görsel okunabilirliğidir;
yanlış yerleşen her klip, görsel zincirin koptuğu ADRESTİR. Fazlar arası
karşılaştırılabilir. ⛔ Sıralatmadan önce hangi durumların "saat" olduğu
SÖYLENMEZ; yalnız "tek yönlü değişen şeyleri bul" denir — saatleri kendi
bulması, saatlerin ekranda okunup okunmadığının testidir.

> 🔗 Ders 129 (SPEC önkoşulu — bu ders onun kardeşidir: orada eksik bilgi
> kapıyı düşürüyordu, burada FAZLA bilgi kapıyı sahte geçiriyor) · Ders 151
> (mercek vuruşu göremez) · Ders 160 (dosya adı kimlik değildir — orada
> kimliği DOSYA, burada RAPOR taklit ediyor) · Ders 125 (komut satırında
> cevabı duran soru modele sorulmaz).

---

## 🔴 DERS 166: NOVUM'U OLAN FİLM MOD V'DE ÖLÇÜLEMEZ — MERCEK FİLMİN TÜRÜNÜ YAZAR, KURALINI KUSUR SAYAR

**KAPI:** BETİK · `rapor_kontrol.py` ①.6 NOVUM kapısı (SPEC'te `NOVUM` varken ⑥⑦⑧'in `PREMISE REGISTER`'ı yalnız ORTAMI yazıyorsa ⚠️ ŞARTLI + ⑩ zorunlu) · `rubrik_paketle.sh` ⑥ enjeksiyonu NOVUM'u AYNEN taşır
**TEKRAR:** 1 · 02.09.2026 THE LEANING ROOM — aynı arıza, YENİ MERCEKTE de:
⑥ FİZİK `PREMISE REGISTER: Earth-normal gravity (1g)` ve ⑧ EFOR
`Earth-normal 1g inside a pressurized wooden room` yazdı. Filmin novum'u tam
olarak budur: ağırlık YALNIZ itkiden gelir, "aşağı" sürücünün ittiği yöndür.
Üç mercek (① ③ ⑥) novum'un kendisini 🔴 BLOCKER saydı: *"an object falls
diagonally UPWARDS, defying the established 1g"*. Kare 2280-2340 çıkarıldı:
cisim yukarı düşmüyor, lambanın yattığı yöne kayıyor — kural çalışıyor.
⛔ `rapor_kontrol.py` ①.6 NOVUM kapısı bu partide ATEŞLEDİ ve DOĞRU ateşledi;
kapı çalışıyor, kart koşulmuyor

**Kaynak:** THE STILL SWARM QA (02.09.2026) — ⑥ FİZİK 6,2 · ⑦ AKSİYON 7,7 ·
④ HİKAYE 2,7. Filmin novum'u bir FİZİK İHLALİDİR: *kabuğun içine giren her
katı cisim hızının tamamını 0,15 saniyeden kısa sürede kaybeder ve asılı
kalır; etki-tepki hâlâ çalışır.*

**Sorun:** Rubrik ⑥'nın STEP 0'ı zaten bir PREMISE GATE taşıyor ve "kuralın
imkânsızlığı asla bulgu değildir" diyor. Kapı koştu — ve **ORTAMI kaydetti,
KURALI değil:**

```
⑥ raporu, PREMISE REGISTER:
  "Zero-gravity / microgravity orbital space environment — objects, debris,
   and human figures float indefinitely unless acted upon by an external force."
  ⟵ bu Newton'un birinci yasasıdır; filmin ihlal ettiği ŞEYİN TA KENDİSİ
     kural olarak kaydedilmiş.

Sonuç — üç kategori, tek olaydan (S5 gaz konisi, planda YAZILI):
  Ballistics 6/10 (−4) · Material 6/10 (−4) · Particles 5/10 (−5)
  ⑩ ÖNERME KAPISI'nda kaynağı planda yazılı olan yarısı DÜŞER.
⑦ BEAT STRING: S6 yuvası `-` = "bu sahnede vuruş yok".
  S6 filmin NOVUM TAŞIYICISI ve TEK KARE sahnesidir (1:04).
④ "THE ONE THING NOTHING ELSE DOES: I could not find one."
```

**Ve mod D'ye geçmek TEK BAŞINA yetmezdi — paketin kendisi novum'u düşürüyordu:**

```
rubrik_paketle.sh ⑥ enjeksiyonu, C bloğunu SATIR bazlı süzüyordu:
    grep -E "[0-9]+ *(m|cm|s|g|kg|%|°)\b"
· NOVUM kaydı 4 satırlık düz yazıdır; etiket satırında birim SEMBOLÜ yok
· "0,15 saniyeden" TÜRKÇE birim SÖZCÜĞÜDÜR → `\bs\b` tutmaz
→ NOVUM paketten TAMAMEN düştü; yerine yıpranma haritasının "6 cm sürtünme
  izi" satırı girdi (⑥'ya "kimlik/kostüm satırları VERİLMEZ" denmesine rağmen).
Yani doğru iş akışı koşulsa bile ⑥ filmin kuralını GÖREMEYECEKTİ.
```

**ÇÖZÜM — üç uçtan birden, üçü de kod:**

```
① rubrik_paketle.sh — süzgeç SATIR değil KAYIT seçer (etiket + girintili
   devam satırları). NOVUM/ÖNERME/İHLAL kaydı AYNEN ve başında şu etiketle:
     "⭐ PREMISE REGISTER GİRDİSİ — bu bir KUSUR DEĞİL, filmin KURALIDIR"
   Kapsam DIŞLAMAYLA kurulur (yıpranma/kask/insan/kostüm/ses dışarıda),
   birim SEMBOLÜ aranmaz — SPEC Türkçe yazılır.
② rapor_kontrol.py ①.6 — SPEC'te NOVUM varken ⑥⑦⑧'in register'ı yalnız
   ortam sözcükleri taşıyorsa (zero-g · vacuum · free fall · 0 g) ve bir
   KURAL fiili taşımıyorsa ⚠️ ŞARTLI + "⑩ ÖNERME KAPISI ZORUNLU".
③ Ölçüldü: kapı THE STILL SWARM'ın ⑥ ⑦ ⑧'inde üçünde de ateşledi,
   NOVUM'u olmayan THE COLD WELD'in altı raporunda HİÇ ateşlemedi.
```

⛔ **GENEL KURAL:** novum'u bir fizik/mantık ihlali olan filmde mod V bir
ölçüm değil, bir YANLIŞ ANLAMA üretir — ve o yanlış anlama filmin en yüksek
puanlı kusuru olarak tabloya girer. Bu tür filmlerde ⑥⑦⑧ mod V koşulursa
skor satırı yazılmaz; koşu tekrarlanır.

> 🔗 Ders 129 (SPEC önkoşulu) · Ders 165 (paketin VARLIĞI — bu ders paketin
> İÇERİĞİ) · Ders 87/116/130 (önerme kapısı — düşen bulgunun puanı geri
> verilir) · Ders 157 (novum taşıyıcısı tek karede ölçülür — ⑦ tam orada
> "vuruş yok" dedi) · Ders 151 (mercek vuruşu göremez)

---

## 🔴 DERS 170: EKSİK OLAN NEDEN, RAPORDA "EKSİK" DİYE GÖRÜNMEZ — KÖR DENETÇİ YANINDAKİ NESNEDEN BİR NEDEN UYDURUR VE ONU YÜKSEK GÜVENLE YAZAR

**KAPI:** KARAR · GEÇİŞ C'ye zorunlu adım: kör raporun her GÜVENLİ NEDEN
cümlesi, katalog geçişinin **MISSING** listesine karşı okunur. Nedeni
taşıyan girdi MISSING ise, kör raporun o açıklaması gözlem değil
ARTEFAKTTIR ve bulgu listesinden çıkarılır.
**TEKRAR:** 0

**Kaynak:** YERÇEKİMİ FAZ 4 (02.09.2026), iki mühürlü geçiş —
`02_HAM_RAPORLAR/YERCEKIMI_FAZ04_{KOR,KATALOG}_HAM.md`

**Sorun:** Fazın adı FEDA'dır ve tek meselesi şudur: adam halatın
kancasını KENDİ ELİYLE açar; bu bir kaza değil bir SEÇİMDİR. Rubriğin
kör geçişine bu yüzden doğrudan soruldu:

> *"Bir şey ayrılıyor, gevşiyor ya da bırakılıyor mu? KAZA gibi mi
> göründü, KASITLI mı? Kararını görüntüde ne verdirdi?"*

Kör denetçi cevap verdi ve **hiç tereddüt etmedi**:

> *"This looks ACCIDENTAL. The deciding factor in the picture is the
> massive, jagged hole torn into the station hull directly behind them,
> indicating a violent, unplanned structural failure."*

⭐ **Ama o patlama filmde YOK.** Kadrajdaki delik önceki fazdan kalma
eski hasardır. Ve asıl önemlisi: **kancayı açan çekim hiç üretilmemişti**
— katalog geçişi onu MISSING listesine yazdı (girdi G).

**Mekanizma:** kör denetçi "burada bir neden eksik" demez. Ayrılmayı
görür, bir neden arar, ve **kadrajda duran en yakın büyük nesneyi neden
yapar.** Sonra bunu yüksek güvenle raporlar. Eksiklik, raporda bir
BOŞLUK olarak değil, **fazladan bir OLAY** olarak görünür.

⚠️ **İkinci vaka aynı gün, aynı filmde (FAZ 3):** kadının kaskının
düştüğü ve adamın vizörünün açık okunduğu iki kusurdan denetçi
*"Survivability: helmets sealed → helmets removed. Confidence: HIGH"*
diye bir SAAT uydurdu ve iki klibi fazın SONUNA koydu — filmin
karakterleri 4:48'de ölmüş göründü. Aynı kalıp: eksik/bozuk bilgi,
raporda uydurulmuş bir nedensellik olarak çıkıyor.

**ÇÖZÜM — GEÇİŞ C'YE ÜÇ SATIR:**

```
① Kör raporun "X yüzünden Y oldu" biçimindeki her cümlesini işaretle.
② X'i taşıyan katalog girdisini bul.
     girdi MATCHED  → açıklama gözlemdir, işlenir
     girdi MISSING  → ⛔ AÇIKLAMA ARTEFAKTTIR; bulgu değil, EKSİĞİN
                       KANITIDIR. Bulgu listesine değil, "üretilmemiş
                       çekim" listesine yazılır.
③ Kör raporun YÜKSEK GÜVENLE yazdığı bir saat/neden, katalog geçişinde
   karşılığı yoksa: güven ne kadar yüksekse şüphe o kadar büyür.
   Kör geçiş emin olduğunda değil, ÇELİŞTİĞİNDE haklıdır.
```

⭐ **Yan sonuç — bu ders kör geçişin değerini ARTIRIYOR, azaltmıyor:**
uydurulmuş nedensellik, "izleyici bu boşluğu nasıl dolduracak"
sorusunun birebir cevabıdır. F4'ün izleyicisi fedayı bir patlama kazası
sanacaktı; bunu başka hiçbir kapı gösteremezdi.

> ⛔ **3. VAKA — 02.09.2026 · YERÇEKİMİ FAZ 6.** Kör denetçi sıralamasını
> **iki RENDER KUSURU üzerine** kurdu ve ikisine de "High confidence" dedi:
> *"Hand injury: Clean (1, 9) → Cut (5)"* ve *"Face injury: Clean (6, 7) →
> Scratched (10)"*. Filmde ne el yarası ne yüz çiziği vardır; ikisi de
> süreklilik kusurudur. ⭐ Yeni bilgi: kusur yalnız KAFA KARIŞTIRMIYOR,
> izleyicinin zaman algısını **ÖRGÜTLÜYOR** — geri döndürülemez görünen
> her fark bir saat olarak kullanılıyor. Sıra skoru 2/10'a bu yüzden
> düştü. → GEÇİŞ C'de kör raporun her SAATİ de MISSING/kusur listesine
> karşı okunur, yalnız nedenleri değil.

> 🔗 Ders 164 (iki mühürlü geçiş — bu ders o mimarinin ilk büyük
> yan ürünü) · Ders 151 (mercek vuruşu göremez) · Ders 125 (komut
> satırında cevabı duran soru modele sorulmaz) · Ders 118 (insan şeridi).

---

## 🔴 DERS 171: "ŞU YERLERE İYİ BAK" DİYEN KİLİT, İHLALİ O YERLERİN DIŞINDA GİZLER — KATALOG GEÇİŞİ METİNE 10/10 VERDİ, KÖR GEÇİŞ AYNI MAKARADA İKİ ALTYAZI SAYDI

**KAPI:** KARAR · GEÇİŞ C'ye zorunlu adım: katalog geçişinin **TAM PUAN**
verdiği her kategori, kör geçişin ilgili pasaport maddesiyle karşılaştırılır.
Kör geçiş orada bir ihlal saymışsa katalog geçişinin puanı DÜŞER ve o
kategori ⛔ ÖLÇÜLMEDİ olarak işaretlenir. Tam puan bir kanıt değildir.
**TEKRAR:** 0

**Kaynak:** YERÇEKİMİ FAZ 5 (02.09.2026), iki mühürlü geçiş —
`02_HAM_RAPORLAR/YERCEKIMI_FAZ05_{KOR,KATALOG}_HAM.md`

**Sorun:** Rubriğin metin kilidi şöyleydi ve bilerek sert yazılmıştı:

> *"TEXT — ZERO CHARACTERS... This is an interior full of wall panels,
> indicator banks, buttons and hatches, and NONE of them carries a letter...
> ⭐ **you must check every panel, indicator bank, button, hatch and cover
> in every entry.** This is the hardest lock in this phase."*

**Katalog geçişi paneleri denetledi ve doğru cevap verdi:**
`TEXT DISCIPLINE: 10 · "Zero characters found."`
`WHAT WORKED: "no rogue characters generated on the heavily detailed panels."`

**Kör geçiş aynı makarada, aynı gün, ayrı sohbette:**
```
ANY READABLE CHARACTER ANYWHERE:
  Seg 9  (1:24): caption "Cabin pressure falling, seal the hatch."
  Seg 12 (1:54): caption "Capsule power nominal."
```

⛔ **İhlal panelde değildi — KAREYE GÖMÜLMÜŞ ALTYAZIYDI.** Rubrik nereye
bakılacağını sayarak söyledi; denetçi oraya baktı ve **yalnız oraya**
baktı. Liste, dışında kalanı görünmez yaptı.

**Mekanizma:** yer sayan bir kontrol listesi, kapsamı daraltır.
"Her paneli kontrol et" cümlesi, denetçinin zihninde "ihlal panellerde
olur" önermesine dönüşüyor. Bu, D164'ün (yankı) ve D170'in (uydurulmuş
neden) üçüncü kardeşi: **bilgilendirilmiş denetçi, bilgilendirildiği
YERDE körleşir.**

⚠️ İkinci kanıt aynı raporda: kör geçiş D girdisinde **camı kapatan siyah
bir panjur** gördü (spec'te böyle bir şey yok); katalog geçişi aynı
segmenti "D | YELLOW | Earth lights are visible" diye geçti ve panjuru
hiç anmadı. Yine: tarif edilen şeye bakıldı, tarif edilmeyen görülmedi.

**ÇÖZÜM — İKİ SATIR:**

```
① RUBRİK TARAFI: yer sayan her kilidin sonuna kapanış cümlesi konur —
   "...and anywhere else in the frame, including burned-in text, captions,
    subtitles, overlays and anything the renderer may have added on top
    of the picture."
   Yer listesi ÖRNEKTİR, kapsam DEĞİLDİR.

② GEÇİŞ C TARAFI (asıl kapı): katalog geçişinin 10/10 verdiği her
   kategori, kör geçişin karşılık gelen maddesine karşı okunur.
   Çelişki varsa KÖR GEÇİŞ KAZANIR — çünkü ona nereye bakacağı
   söylenmedi.
```

⭐ **Bu, iki mühürlü geçişin şimdiye kadarki en net kazancı.** Tek geçişli
bir denetimde bu ihlal RAPORDA HİÇ GÖRÜNMEZDİ — üstelik "10/10" ve
"kusursuz tutuldu" diye kayda geçecekti.

> 🔗 Ders 164 (yankı — söylenen geri gelir) · Ders 170 (eksik neden
> uydurulur) · Ders 151 (mercek vuruşu göremez) · Ders 138 (metin
> yasağının KAPSAMI).

---

## 🔴 DERS 173: ⑤ ÇAPRAZ KAPISI ÇOĞUNLUĞU DOĞRU SAYDI VE TEK DOĞRU MERCEĞİ SAPAN İLAN ETTİ — ODAK DIŞI FİGÜRDE ÇOĞUNLUK ORTAK KÖR NOKTAYI PAYLAŞIR

**KAPI:** BETİK · `rapor_kontrol.py` ⑤ ŞERİT kapısı — çoğunluktan sapan mercek
🚨 alıyor. Bu ders o kapıya bir TİE-BREAK ekletir: sapma OYLA değil KAREYLE
çözülür.
**TEKRAR:** 0 · 02.09.2026 THE LEANING ROOM

**Kaynak:** THE LEANING ROOM QA (02.09.2026) — sekiz mercekli parti,
`rapor_kontrol.py --olcum-kesme 11 --olcum-sahne 12`:

```
⑤ ÇAPRAZ KAPI çıktısı:
   ⚠️ ŞERİT — çoğunluk `1111-1111-1-` (4 mercek); sapan: ① KARE
      "sapan merceğin şeridi 🚨"

ÖLÇÜM (1:55 karesi çıkarıldı ve BAKILDI):
   S11'de kadın KADRAJDA — koltukta, arkada, odak dışı, kımıltısız.
   Plan da öyle diyor: "Far back and well out of focus, a woman ... sits in
   the deep armchair, a soft charcoal shape."

   ① KARE'nin şeridi:  1111-1111-11   ✅ DOĞRU
   Çoğunluğun şeridi:  1111-1111-1-   ✗ YANLIŞ (4 mercek, aynı hata)
```

⭐ **MEKANİZMA — ÇOĞUNLUK BAĞIMSIZ DEĞİLDİR.** Sekiz mercek aynı dosyayı
izliyor, aynı aileden modellerle koşuyor ve aynı algısal kısayolu kullanıyor:
**odak dışı, hareketsiz, arka plandaki bir insan "sahne insansız" diye
kodlanır.** Bu bir oylama hatası değil, ORTAK KÖR NOKTADIR — ve çoğunluk
kuralı ortak kör noktayı DOĞRULAMA olarak okur.

```
Kapının varsayımı:  n bağımsız gözlemci → çoğunluk gerçeğe yakınsar
Gerçek:             n bağımlı gözlemci → çoğunluk ORTAK ÖNYARGIYA yakınsar

Ve sonuç tersine döner: filmi DOĞRU okuyan tek mercek, kapının kendi
çıktısında 🚨 damgası alır. Bir sonraki koşuda o mercek "sapan" diye
zayıflatılırsa depo, tek doğru ölçümünü atmış olur.
```

⛔ **VE BU ŞERİDİN NEDEN ZATEN ZAYIF OLDUĞUYLA BİRLEŞİYOR [D163]:** tek
figürlü filmde şerit neredeyse sabittir (`1111…`) ve dört sahnelik blok takası
onu hiç bozmadan geçer. D163 şeridin SIRA eksenini ölçmediğini söylemişti;
bu ders şeridin VARLIK eksenini de tek başına ölçemediğini ekliyor. Şerit,
kendisi doğrulanmadıkça hiçbir şeyi doğrulamaz.

**ÇÖZÜM — İKİ SATIR, BİRİ BETİKTE:**

```
① ŞERİT SAPMASI OYLA DEĞİL KAREYLE ÇÖZÜLÜR.
   `rapor_kontrol.py` ⑤ ŞERİT kapısı sapan merceği 🚨 damgalamaz; ÇÖZÜLMEMİŞ
   ilan eder ve o sahnenin ortasının karesini isteyen tek satırı basar:
      ⚠️ ŞERİT ÇATIŞMASI · sahne n · çoğunluk `-` · sapan `1`
         ⛔ ÇÖZÜLMEDİ — kareyi çıkar ve BAK:
            ffmpeg -ss <sahne ortası> -i "$M" -frames:v 1 serit_S<n>.jpg
   Çözülene kadar hiçbir merceğin şeridi 🚨 almaz ve parti bu eksenden düşmez.

② ⑪ ÖLÇÜM KAPISI ŞERİDİ DE ÜRETİR.
   `olcum_kapisi.sh` zaten sahne ortası karelerini basıyor (sahne_izgarasi.jpg).
   O ızgaraya bakıp şeridi OPERATÖR yazar ve hakem şerit O olur — tıpkı kesme
   ve sahne sayısında olduğu gibi. Mercek şeritleri ona karşı ölçülür,
   birbirlerine karşı değil.
```

⚠️ **DÜRÜST KAYIT:** bu partide çoğunluk kuralı kesme (11) ve sahne (12)
eksenlerinde DOĞRU çalıştı — ikisi de ⑪ ölçümüyle bağımsız olarak
doğrulandı. Kural her yerde değil, ORTAK KÖR NOKTANIN olduğu yerde çöküyor:
odak dışı figür, düşük kontrastlı arka plan, tek karelik olaylar. Kapıyı
söküp atmak değil, tie-break eklemek gerekiyor.

> 🔗 Ders 163 (şerit sıra eksenini ölçmez) · Ders 135 (sapan mercek önce kendi
> envanteriyle karşılaştırılır) · Ders 162 (⑤ mutabakatı ölçer, suskunluğu
> ölçmez) · Ders 125 (komut satırında cevabı duran soru modele sorulmaz)
