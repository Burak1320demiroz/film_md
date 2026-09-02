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
## 🔴 DERS 122: KAPININ REFERANS SAYISI ELLE HESAPLANIYOR — PLANIN REPLİK ÇİZELGESİNDE DÖRT KAYDIN İKİSİ BİR YUVA GEÇ; D115 DOĞRU BİR KURGUYU "10 SANİYE KAYMIŞ" OKUYACAKTI

**Kaynak:** THE BORROWED WEIGHT · 24.08.2026 ·
`yatay_3_5_dk_filmler/THE_BORROWED_WEIGHT/THE_BORROWED_WEIGHT_PLAN.md` §replik
çizelgesi + `..._QA_SPEC.md` A/B bloğu
**Sorun:** yazım paketi kusursuz görünüyordu — ızgara formülü SPEC'te yazılı,
replik ofsetleri prompt TIMELINE'larında yazılı, çizelge dolu. Ama çizelgenin
sayıları formülden TÜRETİLMEMİŞ, elle yazılmıştı:

```
formül (SPEC'te yazılı):  başlangıç(S_n) = 9 s + (n−1) × 10 s
prompt ofseti (PART_A/B): S2 +3.0s · S10 +4.0s · S21 +2.0s · S22 +6.0s

           formülün verdiği    planda yazan     fark
S2              0:22               0:32        +10 s  ⛔ bir yuva
S10             1:43               1:53        +10 s  ⛔ bir yuva
S21             3:31               3:31          ✓
S22             3:45               3:45          ✓
DORUK S20   199 s (3:19-3:29)   "başlangıç 209 s"  +10 s ⛔ (satır kendi
                                                    içinde de çelişiyor)
```

Üçü de aynı hatanın kopyası: `9 + n×10` hesaplanmış, `9 + (n−1)×10` değil.

**Neden ağır:** bu sayılar süs değil, **bir kapının ölçü aletidir.** Ortak adım
⑨ HİZALAMA [D115] kurguyu tam olarak bu çizelgeyle doğrular — "|Δ| ≤ 2 s →
sahne yerinde, |Δ| ≈ klip süresinin katı → sahne kaymış". Bu partide teslim
kurgusunun S2 repliği 0:23'te duyuldu: formüle göre Δ = +1 s (kırpılmamış
hook — kurgu YERİNDE), çizelgeye göre Δ = −9 s (bir yuva kaymış — kurgu
BOZUK). Kapı, doğru bir hizalamayı hata; bir sonraki filmde bir hatayı doğru
okuyacaktı. Ve kapı bunu kendi başına fark edemez: karşılaştırdığı iki sayıdan
biri zaten yanlıştır.

**ÇÖZÜM — sayı formülden türetilir, elle yazılmaz (kart A, SPEC adımı):**

```
⛔ REPLİK ÇİZELGESİ VE DORUK SAATİ HESAPLANMAZ, HESAPLATILIR.
   Plan/SPEC yazılırken tek satırla üretilir ve çıktısı yapıştırılır
   (hook 9 s · klip 10 s · ofsetler prompt TIMELINE'larından):

   python3 -c "h=9;c=10
   for n,o in [(2,3.0),(10,4.0),(21,2.0),(22,6.0)]:
       t=h+(n-1)*c+o; print(f'S{n}: {int(t//60)}:{int(t%60):02d} ({t:g}s)')"

   Aynı formülle DORUK satırı da yazılır:
       doruk başlangıcı = h + (doruk_sahne − 1) × c

⛔ YAZIM KAPISI: SPEC'in GRID satırı ile çizelgenin HER kaydı birbirini
   doğrulamalıdır. Bir kayıt formülden ± klip süresi kadar sapıyorsa yazım
   paketi TAM DEĞİLDİR — QA koşulmaz.
```

⭐ **Genel kural:** bir belgede aynı gerçeğin iki temsili varsa (formül +
tablo), biri diğerinden ÜRETİLMELİDİR. Elle yazılan ikinci temsil, er geç
birincisiyle çelişir — ve bu depoda o çelişki bir kapının ölçü aletine düştü.
Bu ders yeni bir kural koymuyor: var olan formülü tek gerçek kaynak yapıyor.

> 🔗 Ders 115 (ızgara geri alma — referansı bu ders koruyor) · Ders 74 (kaydı
> olmayan kapı koşulmamış kapıdır; burada kapı KAYITLI ama referansı bozuk) ·
> Ders 118 + 121 (şeridin ve repliğin Δ hesabı bu sayılara dayanır) ·
> AGENTS §2 ① (bir sayıyı iki yerde tutmak, birini yanlış tutmaktır) —
> bu ders o kuralın belge İÇİ karşılığıdır.

---


## 🔴 DERS 124: PLAN 8 SANİYEYE YAZILIYOR, ARAÇ 10 SANİYE ÜRETİYOR — ÜÇ FİLMDE ÜÇ KEZ; IZGARA PLANDAN DEĞİL ARAÇTAN YAZILIR

**Kaynak:** THE IRON SLOPE (25.08.2026) master ölçümü —
`ffprobe` teslim dosyası **65,000 s**, kesme ızgarası **10,03 · 20,03 ·
30,03 · 40,03 · 50,03 · 60,03**, ve kaynak kliplerin altısı da
**10,005 s** (`~/Downloads/Man_climbing_*.mp4`). Plan: 6 × 8 s = 48,0 s.
Öncesi: THE FIRST MORNING **64 s / ~10 s sahneler** · THE WRONG SHADOW
**64 s / ~10 s sahneler** [D70].

**Sorun:** D70 bu sapmayı bir **kurgu** kusuru sanmış ve kurgu kapısı
yazmıştı. Kapı üç kez koştu, üç kez GEÇ kaldı — çünkü sapma kurguda
doğmuyor: **üretim aracının klip süresi 10 saniye.** Kurgu masasında
"fazladan segment" yoktu; 6 sahnenin 6'sı planlıydı ve her biri iki saniye
uzundu. Kurgunun eklediği tek şey 4,97 saniyelik başlık kartıydı.

**Bedeli sürede değil, ZAMAN KODLARINDA:** 8 saniyelik ızgaraya yazılmış
her şey geçersiz olur — müzik düşüşleri (5,0 · 26,0 · 40,8), tohum
(0:05,8) ve karşılığı (44,4), 2,2 saniyelik yanma arası (44,4-46,6),
48. saniyedeki döngü noktası. Film "iki saniye uzun" değildir; **beat
haritası olmayan bir filmdir.**

**ÇÖZÜM — plan yazılmadan önce (sayısal):**

```
① ARACIN KLİP SÜRESİNİ ÖLÇ, VARSAYMA:
   ffprobe -v error -show_entries format=duration -of csv=p=0 <tek test klibi>
   Çıkan sayı planın künyesine yazılır:  KLİP SÜRESİ = <ölçülen>
② IZGARA O SAYIDAN ÜRETİLİR:
   sahne_başlangıcı(n) = (n − 1) × klip_süresi        [D115 formülü]
   toplam_süre         = klip_sayısı × klip_süresi    (kart 0,0 s)
   ⛔ 8 saniyelik ızgara 10 saniyelik araçta YAZILMAZ.
③ 8 SANİYE ISRARLA İSTENİYORSA KIRPMA PLANDA, SAHNE SAHNE VERİLİR:
   "S0: 0,0-8,0 kullanılır; 8,0-10,0 atılır — kesme noktası eldivenin
   basamağı kavradığı kare." Talimatsız kırpma yapılmıyor [D100].
④ KURGU KAPISININ ② MADDESİ BU SAYIYLA KOŞAR: süre = klip_sayısı ×
   klip_süresi ± 0,5 s. Iron Slope: 6 × 10,005 = 60,03 s; ekranda
   65,00 s → fark 4,97 s = başlık kartı [D70/D120].
```

⭐ **Genel kural:** planın ızgarası bir TERCİH değil, bir ÖLÇÜMDÜR. Aracın
ürettiği süre neyse plan odur; aksi hâlde plan, hiç var olmamış bir
zaman çizgisine beat yazar ve bunu ancak QA'da fark ederiz.

> 🔗 Ders 70 (aynı ihlalin kurgu tarafı — bu ders onun SEBEBİNİ buluyor) ·
> Ders 100 (kırpma talimatsız plan) · Ders 101 (kapı sahne sayar, çekim
> saymaz) · Ders 120 (kart süresi) · Ders 122 (bir gerçeğin iki temsili:
> formül tek kaynak olmalı) · Ders 125 (bu sayıların hepsi makineyle
> ölçülür, modele sorulmaz).

---

## 🟡 DERS 135: İNSAN ŞERİDİ KİLİDİ, ÖLÇME ALETİNİN ÜRETEMEYECEĞİ NOTASYONDA YAZILI — `-222222222222` İLE `-111111111111` HİÇBİR ZAMAN EŞİT OLAMAZ

**Kaynak:** THE ROSE COAT · 26.08.2026 · kurgu kapısı ④c ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_ROSE_COAT.md` §KURGU KAPISI
**Sorun:** D118 kurgu kapısına üçüncü maddeyi ekledi: planın insan şeridi
ile raporun `PRESENCE STRING` çıktısı yan yana konur, aynı değilse önce
çözülür. Bu filmin SPEC'i şeridi şöyle yazıyor:

```
PLAN:  -222222222222      ⭐ "2" = kaç GÖVDE — bu filmin sıra kilidi
                             kaç kişi olduğudur, var olup olmadığı değil
```

Rubriklerin çıktı şartnamesi ise dördünde de birebir aynı cümle:

```
"One character per scene, in edit order, no spaces: `1` if a human figure
 is visible anywhere in that scene, `-` if the scene has none."
```

**Rubrik "2" üretemez.** Kapı, ölçme aletinin fiziksel olarak
veremeyeceği bir cevabı bekliyor; yani her iki-figürlü filmde otomatik
olarak düşer ve "⛔ ÖNCE ÇÖZ, SONRA PUANLA" der. Bu filmde tam olarak bu
oldu ve kapı okunamadan geçildi.

⭐ Kilidin ÖZÜ yine de doğrulanabiliyordu, sadece başka bir sütundan:
②'nin `APPEARANCE TABLE`'ı 12 sahnenin 12'sinde tam iki gövde sayıyor.
Ama hiçbir kapı o sütuna bakmıyor.

**İkinci delik, aynı yerde:** dört mercek de bir şerit yazıyor ve hiçbir
kapı ikisini yan yana koymuyor. Bu partide:

```
① KARE        -111111111111
② DEVAMLILIK  -111111111111
④ HİKAYE      -111111111111
⑤ ARKA PLAN   1111111111111   ← ilk yuvada İNSAN gösteriyor
```

⑤'in dizesi hem öteki üçüyle hem KENDİ envanteriyle çelişiyor (S1'in
öznesi "sand pouring from wall slit", figür yok). Çapraz sayım kapısı ⑤
sahne sayısı, kesme sayısı ve repliği karşılaştırıyor — şeridi
karşılaştırmıyor. Şerit, iki modelin uydurmadan üretemeyeceği ikinci
eksendir (birincisi replik, D121) ve boşta duruyor.

**ÇÖZÜM — ① SPEC şablonunda şerit İKİ satır yazılır:**

```
### 🧬 İNSAN ŞERİDİ — sıra kilidi

GÖVDE ŞERİDİ (plan)     : -222222222222   ← kaç gövde · üretim kilidi
VARLIK ŞERİDİ (kapı)    : -111111111111   ← rubriğin ÜRETEBİLECEĞİ dize
                                             kapı ④c BUNUNLA koşar

⛔ Gövde sayısı kapıda değil, ② DEVAMLILIK'ın APPEARANCE TABLE'ından
   doğrulanır: her sahne satırında kaç ayrı karakter etiketi var?
   Beklenen sayı tutmuyorsa kurgu değil ÜRETİM sapmıştır.
```

**ÇÖZÜM — ② AGENTS ortak adım ⑤'e üçüncü satır:**

```
⭐ ÜÇÜNCÜ SATIR: ŞERİT. Raporların PRESENCE STRING satırları da yan yana
  yazılır.
    hepsi aynı        → şerit ekseni doğrulandı
    biri farklı       → o merceğin şeridi 🚨'dir; ⛔ önce o merceğin KENDİ
                        sahne envanteriyle karşılaştırılır — çoğu zaman
                        rapor kendi kendisiyle çelişir ve fark oradadır
  Parti geçersiz olsa bile şerit okunmaya devam eder [D121].
```

⭐ **Genel kural:** bir kilit, onu ölçecek aletin çıktı biçiminde
yazılmalıdır. Aletin veremeyeceği bir cevabı bekleyen kapı, koşulmamış
kapıdır — ve koşulmamış kapı, D74'e göre hiç var olmamış kapıdır.

> 🔗 Ders 118 (şerit kapısının kendisi — bu ders onun notasyon kusuru) ·
> Ders 121 (şerit ve replik Δ eksenleri) · Ders 122 (aynı aile: kapının
> referans sayısı elle hesaplanıyordu) · Ders 107 (çapraz sayım kapısı —
> şerit oraya ekleniyor) · Ders 74 (kaydı/koşulabilirliği olmayan kapı).

---

## 🟡 DERS 142: SPEC'İN MAKİNE KAPISI KURULU OLMAYAN BİR FİLTREYE YAZILDI — YAZILMIŞ AMA KOŞULAMAYAN KAPI, KOŞULMAMIŞ KAPIDIR

**Kaynak:** THE THIN ROOF QA_SPEC E bloğu, kapı ② (28.08.2026)
**Sorun:** üç makine kapısından biri, koşturulmak istendiğinde çalışmadı

SPEC'in E bloğu D125'in istediğini yaptı: üç ölçüm modele sorulmayacak,
makineden alınacaktı. Kapı ② şöyle yazılmıştı:

```
ffmpeg -i S<n>.mp4 -vf vidstabdetect=shakiness=1:accuracy=15:result=stab_S<n>.trf -f null -
```

Yerel ffmpeg 8.1 yapısında **`vidstabdetect` yoktur** — `libvidstab`
derlenmemiş (`ffmpeg -filters | grep vidstab` boş döner). Kapı sessizce
hiçbir `.trf` üretmedi; betik hata bile vermedi, yalnız dosya oluşmadı.

⭐ **D74 "kaydı olmayan kapı koşulmamış kapıdır" der. Bunun kardeşi:
KOŞULAMAYAN kapı da koşulmamış kapıdır** — ve daha tehlikelidir, çünkü
SPEC'te yazılı durur ve koşulmuş görünür.

**ÇÖZÜM — ① SPEC yazılırken her makine kapısı KURU KOŞUYLA doğrulanır:**

```bash
# SPEC kapatılmadan önce, film klasöründe:
for f in vidstabdetect signalstats deshake mestimate; do
  ffmpeg -hide_banner -filters 2>/dev/null | grep -q " $f " \
    && echo "✅ $f" || echo "⛔ $f YOK — kapı yeniden yazılacak"
done
ffprobe -version | head -1   # ve sürüm SPEC'e yazılır
```

**ÇÖZÜM — ② E bloğunun her kapısı üç satır taşır:**

```
KAPI:      <ne ölçer>
KOMUT:     <tam komut>
DOĞRULANDI: <ffmpeg sürümü ve tarih>   ⛔ bu satır yoksa kapı YAZILMAMIŞTIR
İKAME:     <filtre yoksa hangi ölçüm koşulur>
```

THE THIN ROOF'ta ikame şuydu ve işe yaradı: sahnenin ilk ve son karesinin
satır/sütun luma profilleri ±25 px çapraz korelasyonla eşlendi; 6 sahnenin
4'ünde kayma 0-2 px çıktı (kamera kilitli ✅), 2'sinde özne örneklenen bandı
doldurduğu için ölçülemedi. Yeterli değil ama BOŞ değil — ve boş kapının
tersine, kaydı var.

> 🔗 Ders 125 (makine kapıları) · Ders 74 (kaydı olmayan kapı) · Ders 129
> (SPEC yazıldı ama kullanılmadı — aynı ailenin üçüncü üyesi: belge var,
> uygulama yok).

---

## 🔴 DERS 144: ÜRETİM KAPISI "OKUNMALI" DİYORDU, KABUL/RET ÖLÇÜTÜ YOKTU — İKİ KAPI GÖRÜNÜR BİÇİMDE GEÇMEDİ, 31 KLİP ÜRETİLDİ

**Kaynak:** THE SKYLIGHT PLAN "ÜRETİM KAPI SIRASI [D74]: S0 (delik+ışık gölü okunurluğu)
→ S3 (sütun + toz cümlesi ÇEKİRDEK testi — geçmeden S13/S19 üretilmez) → S5 → S20";
master kareleri 0:05/0:25 (göl beyaz, düz — ② ve ⑤ "white puddle/ice patch") · 0:35
(toz şelalesi) · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md`
**Sorun:** D74'ün kardeşi — kapı yazılıydı, kaydı yoktu; ve kaydı OLAMAZDI.

Kapılar amaç olarak yazıldı ("okunmalı", "testi"), ölçüt olarak değil. Sonuç: S0'ın
gün ışığı gölü düz BEYAZ bir disk olarak çıktı; altı merceğin ikisi (ve filmi ilk
kez gören herkes) onu su/buz okudu — filmin novum'u ("kara deliğin dibinde duran
güneş ışığı") ekranda SU'dur. S3'ün toz cümlesi perde üretti (D143) ve S13/S19 yine
üretildi. Hiçbir kayıt "kapı geçti" demiyordu; çünkü "geçti"nin tanımı yoktu. D74
"kaydı olmayan kapı koşulmamış kapıdır" der; bu ders ekler: **kabul satırı olmayan
kapının kaydı TUTULAMAZ** — his kaydedilmez, gözlem kaydedilir.

**ÇÖZÜM — planın her kapı satırı üç alan taşır; cevap bir sonraki klip üretilmeden
film dosyasına yazılır:**

```
KAPI <n> · S<k> · <ne test edilir>
  KABUL:      <sayılabilir gözlem>   ör. "dipteki oval SICAK ve DOKULU — zemin
              taneleri ve taşlar ovalin İÇİNDE görünüyor"
  RET:        <yanlış okuma>         ör. "oval beyaz, düz, yansıtıcı; birikinti/
              buz okunuyor"
  YABANCI GÖZ: <filmi bilmeyen birine tek soru>  ör. "dipteki parlak şey ne?" —
              cevap "güneş ışığı / gün ışığı" değilse RET
  SONUÇ:      ✅ / ⛔ + tarih + karenin adı   ← bu satır boşsa kapı koşulmamıştır [D74]
```

**ÇÖZÜM — S0 ailesinin (delik + göl: S0 · S2 · S23 · S24) prompt cümlesi:**
```
the bright oval on the floor is DRY sunlit rock — warm, matte and grainy, with
visible stones and dust inside it; it is not water, not ice, not a mirror, not a
lake; nothing reflects in it.
```

> 🔗 Ders 74 (kaydı olmayan kapı) · Ders 143 (S3 kapısının düştüğü yer) · Ders 129
> ve 142 (yazılı ama koşulmayan/koşulamayan kapı ailesi — dördüncü üye: ölçütsüz kapı)
> · Ders 87 (önerme kapısı — burada önerme EKRANDA yanlış okundu, raporda değil).

---

## 🔴 DERS 165: ARAÇ YAZILDI, KOŞACAK KART YOKTU — QA PAKETİ FİLMİN YAZIMINDA ÜRETİLİR, QA ANINDA DEĞİL

**KAPI:** BETİK · `yeni-film` Kart A §4 → `qa-isle/scripts/rubrik_paketle.sh <film klasörü>` · paket klasörü yoksa film "yazımı tamam" DEĞİLDİR [D117'nin kardeşi]
**TEKRAR:** 1 · 02.09.2026 THE SINKING STAKE — sekiz mercek yine mod V koştu

> ⛔ **02.09.2026 · İKİNCİ VAKA VE SEBEBİ BULUNDU — KAPI SATIRI ARACIN
> KENDİSİNE İNMEMİŞTİ.** Ders 01.09'da yazıldı; ertesi gün yazılan
> THE SINKING STAKE yine paketsiz kaldı ve sekiz merceğin sekizi mod V koştu.
> Sebep bir ihmal değil, bir ADRES hatası: kapı satırı "yeni-film Kart A §4"
> diyor, `AGENTS.md` Kart A gerçekten de `rubrik_paketle.sh` koşmasını
> zorunlu tutuyor — ama **`.claude/skills/yeni-film/SKILL.md` §4 `QA_SPEC`
> yazımında BİTİYOR ve paket adımını hiç içermiyor.** Ajan skill'i okuyor,
> AGENTS.md'nin o satırını okumuyor.
> ⭐ **BORÇ ÖDENDİ (02.09.2026):** adım SKILL dosyasının §4'üne eklendi.
> Ders → araç kanalının aynı arızası: D157 "ders filme ulaşmadı" demişti,
> bu "ders ARACA ulaşmadı" der ve daha sinsidir — kapı satırı DOLU
> göründüğü için sayaç bu dersi "kapısı var" diye sayar.

**Kaynak:** THE STILL SWARM QA (02.09.2026) — sekiz mercek, sekizi de mod V ·
`rapor_kontrol.py` çıkış 2 · ⛔ 5 TEKRAR ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_STILL_SWARM.md`

**Sorun:** D129'un dönüştürme borcu 01.09.2026'da ödendi: `rubrik_paketle.sh`
yazıldı, THE COLD WELD için sekiz paket üretildi, D129'un TEKRAR satırına
"araca çevrildi" yazıldı. **Ertesi gün aynı hata sekiz mercekle tekrarladı.**

```
01.09  THE COLD WELD  → 6 mercek mod V → araç yazıldı  → paket üretildi (GERİYE DÖNÜK)
01.09  THE STILL SWARM yazıldı (Kart A) → SPEC ✅ · paket ✗ (kart onu koşmuyor)
02.09  THE STILL SWARM → 8 mercek mod V → aynı hata, bir mercek DAHA GENİŞ
```

Araç kusursuz çalışıyor: koşması **1 saniye** sürdü ve sekiz paketi bastı.
Kusur aracın değil, **koşacağı yerin** yokluğuydu. Paket, `qa-isle` skill'inin
§2b adımında tarif edilmişti — yani ancak QA anında, ve ancak operatör o
skill'i açarsa. Operatör QA anında skill açmaz; rubriği açar. Rubrik
`QA_PROMPTLARI/` altında ÇIPLAK durur ve tek yapıştırılabilir dosyadır.

```
⛔ GENEL KURAL — bir aracın "kaderi" yazıldığı yer değil, KOŞULDUĞU yerdir.
   Araç, kullanıcısının zaten yaptığı işin içine konur; kullanıcının
   hatırlaması gereken bir adıma konursa yazılmamış sayılır.
```

**ÇÖZÜM — kart değişikliği (araç değil, SIRA değişti):**

```
Kart A §4  QA_SPEC yazıldıktan HEMEN SONRA, tek satır:
             bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh <film klasörü>
           Çıktı: QA_PROMPTLARI/FILME_OZEL/<FILM>/PAKET_1..8
           ⛔ Bu klasör yoksa film "yazımı tamam" sayılmaz (D117 gibi).
Kart P     prompt_kontrol.py'den önce paket klasörü GÖZLE doğrulanır —
           üretim başlamadan önce QA malzemesi hazırdır.
SPEC değişirse betik yeniden koşulur (paket elle düzenlenmez).
```

> 🔗 Ders 129 (SPEC önkoşulu — bu ders onun ARACININ koşulmadığını ölçer) ·
> Ders 117 (SPEC bir dosyadır — aynı kalıp: erişim çözüldü, davranış değişmedi) ·
> Ders 142 (yazılı ama koşulamayan kapı) · Ders 74 (kaydı olmayan kapı) ·
> Ders 166 (paketin İÇERİĞİ de eksikti — bu ders paketin VARLIĞINI çözer)

---

## 🔴 DERS 168: ÜRETİM SIRASI DRAMATİK SIRAYLA AYNIYSA, YARIDA KALAN FİLM KENDİNİ SAVUNAMAZ — 14 KLİP ÜRETİLDİ VE ÜÇÜNCÜ PERDE HİÇ VAR OLMADI

**KAPI:** LİSTE · `03_PLAN_ONCESI_KONTROL_LISTESI.md` B5 (yeni madde: ÜRETİM SIRASI) — 02.09.2026
**TEKRAR:** 1 · 02.09.2026 THE SINKING STAKE

**Kaynak:** THE SINKING STAKE (02.09.2026) — üretim bir politika reddi
yüzünden yarıda bırakıldı. Dosya sisteminden ölçüldü: 25 sahnenin ~14'ü
üretilmiş, sırası planla birebir, **ve eksik olan 11 sahne ARDIŞIKTIR ve
filmin SONUDUR.**

```
ÜRETİLEN     S0-S15 kuşağı — kurulum + iki BAŞARISIZ deneme + orta nokta
ÜRETİLMEYEN  merkezi seçim S19 (3:09) · doruk S21 (3:29) ·
             ikinci seçim S22 (3:39) · twist/final S24 (3:59)

SAHİBİN DEĞERLENDİRMESİ: "ne bir mantıklı ilerleme var ne de sahneler
arası devamlılık."
→ İLERLEME YOK ÇÜNKÜ İLERLEME VAR OLMAYAN KISIMDA. Elde kalan şey
  ikinci perdenin ortasında kesilmiş bir film: iki başarısız deneme
  ve hiç ödül.
```

⭐ **MEKANİZMA — YARIDA KALMA BİR OLASILIK DEĞİL, BU HATTIN NORMALİDİR.**
Üretim red alır, kota biter, motor değişir, gün biter. Depo bunu 15 red
vakasıyla zaten biliyor. O hâlde soru şu değildir "film biterse nasıl
görünür"; soru şudur: **film HERHANGİ BİR NOKTADA durursa elde ne kalır?**
Sırayı baştan üretirsen elde hep KURULUM kalır — ve kurulum, tanımı gereği,
kendini savunamayan malzemedir.

⛔ **VE İKİNCİ ZARAR DAHA PAHALI: KONSEPT YANLIŞ YARGILANIR.** Sahip elindeki
malzemeye bakıp filmin hikâyesi hakkında karar verir. Kurulum + iki
başarısızlık gösteren bir kesit, planı ne kadar sağlam olursa olsun,
"saçma sapan" okunur. Konsept, hiç ekrana gelmemiş bir doruk yüzünden
reddedilir.

**ÇÖZÜM — ÜRETİM SIRASI PLANDA YAZILIR VE DRAMATİK SIRA DEĞİLDİR:**

```
① İLK ÜRETİLEN SAHNE DORUKTUR. Filmin en pahalı, en riskli, en çok
   şeyi kanıtlayan karesi ilk sırada üretilir.
② İKİNCİ, MERKEZİ SEÇİM. Üçüncü, KAPANIŞ İMAJI.
③ Ancak ondan sonra S0/hook ve kurulum kuşağı.
④ PLANA TEK SATIR: "ÜRETİM SIRASI: S21 → S19 → S24 → S0 → …"
   Bu satır yoksa üretim baştan başlar — varsayılan budur.

⭐ EMSAL DEPODA ZATEN VAR ve bu film onu okumadı:
   THE SLOW LIGHT  "üretim S11→S6→S9→S0 kapılarıyla başlar"
   THE HOLLOW COUNT "dört üretim kapısı + Plan B'leri §BÖLÜM 4'te"
   İkisi de doruktan başlıyor. THE SINKING STAKE'in planında ÜRETİM
   KAPILARI vardı ama sırası REFERANS PAKETİ → S0 → geri kalanı idi:
   çapa doğru, sıra yanlış.
```

⚠️ **BU DERS "REFERANS PAKETİ ÖNCE" KURALIYLA ÇELİŞMEZ.** Referans sayfaları
(karakter · araç · olay) hâlâ ilk iştir — onlar SAHNE DEĞİLDİR. Çelişen şey
"ilk SAHNE S0'dır" varsayımıdır. Sıra: referans paketi → doruk → seçim →
kapanış → kurulum.

⭐ **BEDAVA KAZANÇ:** doruk önce üretilirse novum'un ekrana gelip gelmediği
ilk günde bilinir. D157/D151'in tamamı "kural ekrana hiç gelmedi"nin geç
fark edilmesidir; bu sıra o gecikmeyi yapısal olarak kapatır.

> 🔗 Ders 157 (novum ekrana gelmedi — geç fark edildi) · Ders 151 · Ders 165
> (araç yazıldı, koşacak kart yoktu — aynı aile: sıra bilgisi araca inmedi) ·
> 03_PLAN_ONCESI B5 · red defteri (yarıda kalmanın 15 sebebi orada).
