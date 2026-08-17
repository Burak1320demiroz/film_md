# 📚 DERSLER — Sistem ve Süreç

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Sistem ve Süreç** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🔴 DERS 55: BIBLE'SIZ ÜRETİM — KIYAFET HER SAHNEDE YENİDEN İCAT EDİLİYOR

**Kaynak:** The Deep Pressure MANTIK QA (Genel 3/10) — Kostüm-Prop **1/10** —
`The suit and life support equipment constantly mutate` · 6 bulgunun 5'i kostüm,
4'ü BLOCKER.

**Sorun:** Karakter 14 sahnede en az dört farklı kişi:

```
S1  siyah ince kıyafet + camgöbeği çizgi + şeffaf küre kask
S1  (7. saniyede) siyah ıslak dalgıç kıyafeti + maske + regülatör + sırt tüpü
S2  hantal GRİ uzay giysisi
S4  turuncu/siyah ASTRONOT giysisi + altın vizör
S5  köşeli kask + OPAK vizör
```

**Sebep, modelin hatası değil — plan dosyasında kıyafet YAZMIYOR.**
`THE_DEEP_PRESSURE_GAS_GIANT_FILM.md` 56 satır ve 13 sahnelik filmin yalnız
2 sahnesini içeriyor. O iki sahnede kıyafet **tarif edilmeden referans veriliyor:**

```
satır 14   "Elif's suit provides a neutral reference point."
satır 42   "casting sharp, dramatic light across Elif's suit"
```

Model'e "onun kıyafeti" deniyor; hangi kıyafet olduğu hiçbir yerde yazmıyor.
Boşluk kalınca model her sahnede türün en yakın klişesine düşüyor — su
altındaysa **scuba**, uzaydaysa **NASA turuncusu**, bilimkurguysa **ince siyah**.
Seri Bible'ındaki gerçek kıyafet (mor + bakır aksan, Breathing Storm satır 26)
**14 sahnenin hiçbirinde görünmüyor.**

**ÇÖZÜM — üretimden ÖNCE, dosya seviyesinde kapı:**

```
BIBLE GATE — bu üçü yoksa hiçbir sahne üretilmez:
  1. CHARACTER BIBLE bloğu (kıyafet, kask, ekipman, kir — sayısal)
  2. SAHNE HARİTASI (kaç sahne, hangi sırayla, hangi lokasyon)
  3. NEGATIVE bloğu

KURAL: "suit", "her gear", "kıyafeti" kelimeleri bir prompt'ta TARİFSİZ
geçemez. Geçtiği her yere Bible bloğunun TAMAMI kopyalanır (Ders 8).
Kısaltma yok, "[CHARACTER BIBLE]" etiketi yok (Ders 45).

SUIT IDENTITY LOCK — her sahne prompt'unda birebir aynı cümle:
  Deep violet high-pressure atmospheric dive-suit with copper-red thermal
  accent lines along the arms and thighs, one transparent spherical helmet,
  no back-mounted tank, no face mask, no regulator, no orange panels.
  This is the ONLY suit in the film — 13 scenes, 13 identical suits.
```

**AYIRICI TEST:** Ders 8 "Bible'ı her sahneye kopyala" der ve Bible'ın VAR
olduğunu varsayar. Ders 55 bir adım öncesidir: **Bible hiç yazılmadıysa
kopyalanacak bir şey de yoktur.** Bu filmde 4 BLOCKER'ın kaynağı tek bir
eksik bloktur — prompt'a eklenecek cümleyle değil, dosyayı yazarak çözülür.

> 🔗 Ders 8 (kıyafet devamlılığı), Ders 37 (ekipman durumu) ve
> [Ders 57](#-ders-57-tek-çekim-İçİnde-ekİpman-morphu--7-sanİyede-tüp-belİrİyor)
> ile aynı ailedendir. Üçü de Bible varsa çalışır.

---

## ⚠️ 55-58 HAKKINDA — SINIFLAR

```
Ders 1-45    PROMPT hatası    → çözüm: prompt'a cümle eklenir
Ders 46      KURGU hatası     → çözüm: kurgu masasında
Ders 47-50   PLAN hatası      → çözüm: plan dosyasında ortak sabit
Ders 51-54   QA hatası        → çözüm: çalıştırma biçiminde
Ders 55      PLAN hatası      → çözüm: dosya yazılmadan üretim başlamaz ← EN AĞIRI
Ders 56      PROMPT hatası    → çözüm: sözcük politikası + ortam kilidi
Ders 57      PROMPT hatası    → çözüm: kilit zaman çizelgesine taşınır
Ders 58      PLAN hatası      → çözüm: Bible'a tekrar eden varlık kartları
```

**55, bu dosyadaki hiçbir dersin çözemediği bir hata sınıfı açıyor:**
1-54 arasındaki her ders, *var olan bir belgeye* eklenecek bir cümle ya da
*yapılmış bir çalıştırmanın* düzeltilmesidir. 55'te düzeltilecek belge yok.
Deep Pressure'ın 4 BLOCKER'ı, hiç yazılmamış bir Character Bible'ın izidir.

---

## 🔴 DERS 63: DERSİ ÜRETEN RUBRİK, DÜZELTMEYİ ALMAYAN TEK RUBRİK OLDU

**Kaynak:** SHORTS_QA çalıştırması, 05.08.2026 — künyesinde
`FILM: THE HALF SKY [Inferred from S7]` · `SOURCE DOCUMENT: NOT PROVIDED` ·
`SPEC BLOCK PROVIDED: no` · `STEP 0.5 GATE: FAILED` yazan rapor, ardından
16 kategori puanı, per-scene tablosu ve kalite tablosu satırı.

**Sorun:** Bu dört satır **yeni değil.** Ders 60'ın kaynağı olan 03.08 tarihli
SHORTS_QA raporunda birebir aynı dört satır vardı. Aradaki tek fark uydurulan
isim. Yani ders yazıldı, rapor yine aynı yerden çıktı.

Sebep tek bir commit'te görünüyor — `eec615c`, mesajı:
**"THE HERD üç mercek + DERS 60/61/62 + dört rubrik düzeltildi."**

```
Düzeltilen dört rubrik           yama
─────────────────────────────    ────────────────────────
VIDEO_QA_CRITIQUE_PROMPT.md      [DERS 60] · [DERS 61] ×3
SENARYO_QA_CRITIQUE_PROMPT.md    [DERS 60] ×2 · [DERS 62]
MANTIK_VE_DEVAMLILIK_QA...md     [DERS 60]
KAPAK_QA_CRITIQUE_PROMPT.md      [DERS 60]

SHORTS_QA_CRITIQUE_PROMPT.md     grep -c "DERS" → 0
                                 ↑ Ders 60'ı ve 62'yi ÜRETEN rubrik
```

**Neden ölümcül:** Yama, dersin **anlatıldığı** dosyalara gitti; dersin
**doğduğu** dosyaya gitmedi. Ders 60/62 yatay hattın dört rubriğine anlatıldı,
oysa ikisi de dikey hattın tek rubriğinden çıkmıştı. İki gün sonra aynı rubrik
aynı hatayı üretti — çünkü kendi dersini hiç okumadı.

İkinci kanıt aynı dosyanın kendi dipnotunda:

```
"⚠️ Bu rubrik hâlâ hiç çalıştırılmadı."
   ↑ 05.08 itibarıyla İKİ kez çalıştırıldı ve iki kez aynı şekilde battı.
     Rubriği açan ajan "denenmemiş" okuyor; doğrusu "iki kez denendi,
     ikisinde de künye uydurdu."
```

**ÇÖZÜM — DERS KAPANIŞ SIRASI (görev kartı G'ye 5. maddenin yerine):**

```
Ders yazıldıktan sonra, sırayla:

1. HANGİ RUBRİK ÜRETTİ?  Dersin **Kaynak** satırındaki çalıştırma hangi
   rubrikten çıktıysa, yama ÖNCE oraya yazılır. Kaynak rubrik yamalanmadan
   diğerlerine geçilmez.
2. grep -L "DERS <n>" kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/*.md
   → çıktı BOŞ olmalı. Dolu ise dersi almayan rubrik listelenir.
3. Kaynak rubriğin dipnotundaki çalıştırma sayısı güncellenir:
   "N kez çalıştırıldı · son çalıştırma <tarih> · sonucu <geçti/battı>"
```

**Kural:** Bir dersi en çok, o dersi üreten dosya taşımak zorundadır. Dört
dosyaya anlatılıp beşinciye — kaynağa — yazılmayan ders, yazılmamıştır.

---

## 🔴 DERS 74: KAYITSIZ KAPI, KOŞULMAMIŞ KAPIDIR — "ÜRETİM S4'TEN BAŞLAR, BOZUKSA FİLM ÜRETİLMEZ" YAZILIYDI; NOVUM'SUZ 64 SANİYELİK TESLİM İKİ QA MERCEĞİNE KADAR GELDİ

**Kaynak:** THE WRONG SHADOW (06.08.2026) — plan dosyası "⭐ ÜRETİM
BURADAN BAŞLAR (S4)… üçüncü gölge ya da gök parlaması çıkarsa film
üretilmez" diyordu; DERS 70 kurgu kapısı ve DERS 72 teslim kapısı 0-2 gün
önce yazılmıştı. Buna rağmen: çift gölgesiz 6 sahne üretildi, 64 s'lik
kurgu yapıldı, jenerik kartı eklendi ve iki mercek bu teslimi puanladı.

**Sorun:** Kapılar metin olarak VAR ama sonuçları hiçbir yere yazılmıyor.
Kaydı olmayan kapının koşulup batması ile hiç koşulmaması ayırt edilemez;
sonraki adım (kalan sahneler, kurgu, QA) her iki durumda da başlıyor.
Ders 62 sınıfının altı tekrarının ortak mekanizması bu: kural eklemek
davranışı değiştirmedi, çünkü kuralın ÇALIŞTIĞINI gösteren zorunlu bir
çıktı yok.

**ÇÖZÜM — prompt değil, İŞ AKIŞI:**

```
KAPI KAYDI BLOĞU — her kapının sonucu film dosyasının sonuna yazılır:

  ## 🚪 KAPI KAYDI
  | Tarih | Kapı | Ölçülen | Sonuç |
  |---|---|---|---|
  | GG.AA | tek-kare fizibilite [D73] | 2 gölge/nesne: VAR/YOK | GEÇTİ/BATTI |
  | GG.AA | S4-önce üretim kapısı    | ... | ... |
  | GG.AA | kurgu kapısı [D70/72]    | 6 klip · 48.2 s · metin 0,0 | ... |

KURAL: Kaydı olmayan kapı KOŞULMAMIŞ sayılır → sonraki adım başlamaz;
QA merceği kapı kaydı olmayan teslime çalıştırılmaz (çalıştırılırsa
skor tablosuna DERS 72 şerhiyle girer). BATTI satırı olan film "üretim
sırasında" değil "üretilmedi" statüsündedir.
```

> 🔗 DERS 70'in tekrar notuyla birlikte okunur: kapı aynı gün ikinci kez
> delindi. Bu ders kapıya yeni madde eklemez — kapının İZİNİ zorunlu kılar.

> 🔁 **TEKRAR — 06.08.2026 · THE STARLESS CIRCLE (yatay hattaki ilk vaka).**
> Film dosyası ÜÇ kapı tanımlıyordu: KAPI 1 gece testi (S1) · KAPI 2 daire
> testi (S0) · KAPI 3 toz testi (S10) — üçünün de kabul ölçütü ve Plan B'si
> yazılıydı. Hiçbirinin sonucu hiçbir yere yazılmadı ve 18 sahnenin 18'i
> üretildi. QA sonucuna bakılırsa **KAPI 2 battı** (daire "black sphere"
> olarak çıktı — bkz. DERS 76) ve dosyadaki Plan B ("daire yalnız S0 ve
> S6'da tutulur") devreye alınmadı. Kapı kaydı bloğu bu filmin dosyasına
> geriye dönük eklendi; **kural şu: KAPI KAYDI bloğu olmayan film QA'ya
> gönderilmez.**

> 🔁 **TEKRAR — 16.08.2026 · THE LAST SHIFT. Bu kez bedel kapı kapı ölçüldü.**
> Film dosyası BEŞ üretim kapısı tanımlıyordu (BÖLÜM 4), her birinin kabul
> ölçütü ve Plan B'si yazılıydı; `4.1 KAPI KAYDI` tablosunun altı satırının
> altısı ⬜ **koşulmadı** ve `DURUM` satırı QA gününde hâlâ "ÜRETİM BAŞLAMADI"
> diyordu — oysa 174 s'lik kurgu aynı gün DÖRT mercekle ölçülmüştü. Dört
> raporun bulguları kapıların tam üstüne düştü:
> ```
> KAPI 1 iki figür (bant TARAFI)   → 🧍 🔴 2:20 bant SOL koldan SAĞ kola geçti
> KAPI 2 parsel (toz sıvılaşmasın) → 🔧 🟠 1:52 toz "2D fluid simulation" (D39)
> KAPI 3 uzuv (TEK uzuv, 3.0 s)    → 🔧📖🧩 "giant mechanical LEGS march"
> KAPI 4 eşleştirme (S3 ↔ S12)     → 🧩🧍 🔴 2:20 eşleşme yok: başka arazi, başka suit
> KAPI 5 birleşik hold (S7)        → ✅ TUTTU — 20 s'lik hold dört raporda tek sahne
> ```
> Beş kapı ≈ 5 klip = üretimin %18'i. Koşulsaydı dördü üretimde yakalanırdı;
> koşulmadığı için film tamamlandı, kurgulandı ve dört mercek harcandı.
> **Kapı kaydı, QA'nın ucuz alternatifidir; koşulmazsa pahalı olanı otomatik
> devreye giriyor.**

---

## 🔴 DERS 77: DERS PLANA GERİ AKMIYOR — 69 YAZILDI, ERTESİ GÜN YASAKLADIĞI SAHNE PLANA EKLENDİ, KLON TAM ORADA ÇIKTI

**Kaynak:** THE STARLESS CIRCLE (06.08.2026) — mantık Nicelik **1/10** ·
karakter Sayı-Ayrışma **1/10** · `2:10 — two identical astronauts at the
ship ladder`. DERS 69 (05.08.2026) madde ①: *"BİNİŞ/İNİŞ HAREKETİ HİÇBİR
SEGMENTTE KADRAJA ALINMAZ — 0 kez."* Bu filmin planı ertesi gün genişletildi
ve eklenen sahne şu: **S14 BİNİŞ — "yedi basamak + eşikte diziye son bakış".**

**Sorun:** Ders sistemi tek yönlü çalışıyor. Bir ders yazıldığında ①
LESSONS_LEARNED'a giriyor, ② QA rubriklerine dipnot olarak işleniyor,
③ negatif çekirdeğe cümle olarak giriyor. **Üçü de ÜRETİM SONRASI ya da
PROMPT içi kanallar.** Planı yazan ajan/insan hiçbir zorunlu adımda ders
listesine bakmıyor: `03_PLAN_ONCESI_KONTROL_LISTESI.md`'nin 12 maddesinin
hiçbiri "bu planda yasaklanmış bir SAHNE TİPİ var mı?" diye sormuyor. Bu
yüzden 24 saatlik bir ders, yeni bir planı hiç etkilemeden delinebildi —
üstelik plan Risk Kartı 4'ü (ikinci figür) açmış, HUMAN COUNT LOCK yazmış
ve klonun çıktığı sahneyi kendi eliyle eklemişti.

**ÇÖZÜM — kontrol listesine yeni bölüm (prompt değil, PLAN kapısı):**

```
A4 — YASAKLI SAHNE TİPİ DENETİMİ   (plan yazılırken, 2 dakika)
□ Plandaki her sahne için sor: aşağıdaki tiplerden biri mi?
     · araç/kapak/airlock BİNİŞ-İNİŞ hareketi          [D69] 3 vaka
     · tek ışıklı loş iç mekâna GİRİŞ                  [D69] 1 vaka
     · aynalı/yansıtıcı yüzey önünde tek karakter      [D20/D69]
     · novum'u türetilmiş optik fenomen taşıyor        [D73]
     · novum'u bir YOKLUK/boşluk taşıyor               [D76]
     · jenerik/başlık kartı ya da kapak çıktısı        [D34/D70/D72]
□ VARSA: sahne ya çıkarılır ya dersin öngördüğü biçime dönüştürülür,
  ve bu karar plan dosyasına TEK SATIR olarak yazılır:
     "S14: biniş hareketi kadraj dışı — D69 ① gereği (06.08)"
□ Satır yoksa denetim yapılmamış sayılır (D74 mantığı).
```

> 🔗 AGENTS §8'in ölçümüyle uyumlu: kural eklemek kaliteyi artırmadı, çünkü
> kurallar üretim ve QA aşamasına akıyor, **karar aşamasına akmıyor.** Bu
> ders yeni bir yasak koymuyor — var olan yasakların plana ulaşma yolunu
> açıyor.

---
