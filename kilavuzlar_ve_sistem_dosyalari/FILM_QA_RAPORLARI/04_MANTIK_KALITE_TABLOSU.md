# 🧩 MANTIK VE DEVAMLILIK KALİTE TABLOSU

> **Kaynak prompt:** `../QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Oluşturma:** 31 Temmuz 2026
>
> Projenin **üçüncü** skor tablosu. Ne ölçtüğü diğer ikisinden farklı:
>
> ```
> LESSONS_LEARNED · KALİTE TAKİP    kare içi teknik    "bu klip doğru mu"
> 03_HIKAYE_KALITE_TABLOSU          dramatik           "kimse umursar mı"
> 04_MANTIK_KALITE_TABLOSU  ← bu    sahneler arası     "film kendiyle çelişiyor mu"
> ```
>
> ⚠️ Bu rubrik **doküman istemez** (baseline = self-consistency). Bu yüzden
> senaryo tablosunu bozan "kapı ihlali / şartlı satır" sorunu burada yok —
> satırlar doğrudan geçerli. Karşılığında rubrik "planlanan şey kurguda yok"
> diyemez; çözemediğini `FLAGS FOR DOCUMENT CHECK` altına **soru** yazar ve o
> sorular rapor geldikten sonra plan dosyasıyla cevaplanır.

---

## 📊 TABLO

| Film | Fizik | Sayaç | Coğrafya | Zaman-Işık | Kostüm-Prop | Nedensellik | Nicelik | Kurulum | Genel |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| The Kaleida Crash | 6 | **8** | 4 | 3 | **2** | **2** | **8** | 6 | **4.0/10** |
| The Inversion | 3 | **2** | 4 | **2** | **2** | 4 | 5 | 5 | **3.0/10** |
| The Tidal Hunt | 3 | **N/A** | 4 | 3 | 3 | 4 | 6 | 4 | **4.0/10** |
| The Last Archive | **9** | N/A | 4 | 5 | **3** | **9** | **10** | 8 | **5.0/10** |
| The Canopy World | 6 | N/A | 5 | 5 | 4 | 7 | **8** | 7 | **5.0/10** |
| **The Deep Pressure** | 4 | N/A | 4 | 3 | **1** | N/A | N/A | 7 | **3.0/10** |
| **The Cold Burn** | 7 | N/A ⚠️D78 | 6 | 7 | 7 | 8 | **10** | 5 | **7.0/10** |
| **The Holding Field** | **3** | N/A | **3** | **7** | **3** | 4 | 4 | 4 | **4.0/10** |
| **The Herd** | 5 | N/A | 4 | 5 | **3** | 4 | 5 | 6 | **4.0/10** |
| **The Dawn Front** | 7 | N/A | 7 | **9** | **1** | 4 | **2** | 7 | **3.0/10** |
| **The Stone Sky** | 5 | N/A | 4 | **3** | **2** | **7** | **1** | 6 | **4.0/10** |
| **The Unbroken City** | **9** | N/A | 8 | 7 | **9** | 8 | **10** | 8 | **8.0/10** |
| **The Starless Circle** | 8 | **N/A** | 6 | **3** | 7 | 4 | **1** | **3** | **5.5/10** |
| **The Blind Return** | 6 | **N/A** | **3** | 4 | **3** | **3** | 6 | 5 | **4.0/10** |
| **The Third Dune** | 6 | **10** | 4⚠️ | **9** | →🧍 | 8 | **10** | 6 | **7.0/10** |
| **The Last Shift** | 6 | **N/A** ⚠️ | 4⚠️ | 5⚠️ | 4 →🧍 | 5 | 6 | 5 | ⚠️ **5.0/10** |
| ~~**The Black Cradle**~~ | ~~4~~ | ~~N/A~~ | ~~7~~ | ~~7~~ | ~~8~~ | ~~5~~ | ~~9~~ | ~~8~~ | 🚨 **GEÇERSİZ** |
| ~~**Loss of Lift**~~ | ~~10/7~~ | ~~10/7~~ | ~~9/6~~ | ~~10/7~~ | ~~7/5~~ | ~~10/7~~ | ~~10/7~~ | ~~10/7~~ | 🚨 **GEÇERSİZ** |

> 🎈 **Loss of Lift (21.08.2026) — 🚨 GEÇERSİZ. Rubrik kendi içinde tutarsız çıktı.**
> Aynı rubrik aynı dosyaya AYNI oturumda iki kez koşuldu. İki koşunun **sahne
> haritası, çelişki defteri ve severity tally'si birebir aynı** (🔴0 🟠1 🟡2) —
> yani tek yeni gözlem üretilmedi. Buna rağmen:
>
> ```
>          hücrelerin ortalaması     raporun yazdığı OVERALL
> KOŞU 1            9.5                      8/10
> KOŞU 2            6.6                      6/10
> ```
>
> İki toplam da kendi tablosuyla tutmuyor, aradaki fark **2.0 puan**. Sebep
> filmde değil rubrikte: "kaynağı olmayan kategori tam puanla başlar" kuralı
> KELİMEYLE yazılmıştı, koşu 2 beş hücreye "[no in-scope source]" yazıp 7/10
> verdi; ve "OVERALL = hücrelerin ortalaması" cümlesi bu rubrikte hiç yoktu
> (SENARYO_QA'da var — bu partide toplamı tutan tek rapor oydu).
> → **DERS 119**, beş rubriğe ④ maddesi olarak yamandı. Parti temiz oturumlarda
> ve mod D ile yeniden koşulacak [DERS 110].
> Kaydı: `01_FILM_RAPORLARI/LOSS_OF_LIFT.md`


> 🌑 **Black Cradle (17.08.2026) — 🚨 GEÇERSİZ, iki ayrı sebeple.**
> ① **Sahne envanteri imkânsız [DERS 107]:** rapor 232 s'lik kurguyu 4 sahne saydı,
> aynı dosyaya koşulan VIDEO_QA 21 kesme saydı. Coğrafya · Zaman-Işık · Kostüm-Prop ·
> Kurulum hücrelerinin dördü de bu 4 sahnelik envanterden türetildi.
> ② **İki hücrenin kaynağı bu merceğin kapsamında değil [DERS 108]:** Fizik 4/10'un
> tek kaynağı 1:45 **vakumda ses** (rubriğin kendi ❌ listesi: → VIDEO_QA), Nedensellik
> 5/10'un tek kaynağı 1:09 **dudak senkronu** (aynı liste: → VIDEO_QA). İkisi de
> düşürülünce satırın okuması ~8.4'e çıkıyor — yani bildirilen hasarın büyük kısmı
> filmin değil, FATURALAMANIN eseri.
> ✅ D87 kapısında düşenler: "1:05'te geçiş çekimi yok" = **S5 BİNİŞ kadraj dışı,
> planlı** [D69 ①] · "ışık sıçraması" = **S8 IŞIK SINIRI, filmin tek planlı geçişi**.
> ⚠️ Sayaç yine N/A — planda **DÖRT** metinsiz sayaç var (şafak seti 2°→10° ·
> 8 segment rezerv · üç amber ışık üçgeni · dört kelepçe) → **DERS 78'in 5. vakası.**
> Kilit çelişkisi defteri **11 ⬜ AÇIK** [D96]:
> [`01_FILM_RAPORLARI/THE_BLACK_CRADLE.md`](01_FILM_RAPORLARI/THE_BLACK_CRADLE.md)

> 🟫 **Last Shift (16.08.2026) — satır ŞARTLI, kilit çelişkisi defteri 7 ⬜ AÇIK [D96].**
> ⚠️ **Sayaç N/A yazıldı; planda ÜÇ metinsiz sayaç var** (kalan parsel · kadrajdaki
> insan sayısı 2→1→0 · amber pus yüksekliği) → **DERS 78'in 4. vakası.**
> ⚠️ Coğrafya 4 ve Zaman-Işık 5'in kaynağı 2:20-2:49: **checkerboard arazi filmin
> NOVUM'udur** (60 × 60 m hasat parselleri) ve amberleşme §0.11'de planlı ışık
> fazıdır → bulguların bu yarısı **D87 kapısında düştü**, ama puan yerinde kaldı →
> **DERS 102.** Ayakta kalan yarı (arazi tipi + kostüm) defterde ⬜ AÇIK.
> Kostüm-Prop bulguları 🧍 KARAKTER_QA ile kesişiyor; skor orada okunur.
> Belge cevapları: [`01_FILM_RAPORLARI/THE_LAST_SHIFT.md`](01_FILM_RAPORLARI/THE_LAST_SHIFT.md)

> ⚠️ **Third Dune · Coğrafya 4 satırı ŞARTLI (11.08.2026):** bu skoru kuran üç
> MAJOR'ın **ikisi belge kontrolünde düştü.** (a) "araç önce düz kumda, sonra
> dik tepeye gömülü" = filmin ÖNERMESİ — plan S12 aracın sancak yanını tepenin
> yutmasıyla açılır ve ⑩ GÖMÜLME EKİ S12'den sonraki tüm sahnelere işlenir.
> (b) "kalkışta dairesel çanak" = planlı S22 (ÇANAK). Ayakta kalan gerçek
> bulgu: çanak **sığ süpürme çukuru değil derin çarpma krateri** olarak
> üretilmiş — bu bir UYGUNLUK ihlali, bir çelişki değil; mod D koşulsaydı
> doğru kategoriye yazılırdı. → **DERS 87**
> Kostüm-Prop hücresi `→🧍`: toz sıfırlanması karakterin ÜZERİNDE olduğu için
> 06 tablosunda raporlandı, çift sayım yok (kart E2 adım 5).
> Belge cevapları: `01_FILM_RAPORLARI/THE_THIRD_DUNE.md`

```
ÖLÇÜLEN FİLM: 15   ·    ORTALAMA: 4.7/10   (11.08.2026 · Third Dune ile)
BLOCKER: Dawn Front 5 · Deep Pressure 4 · Holding Field 2 · Stone Sky 2 ·
         Inversion 1 · Starless Circle 1 (klon 2:10) · Blind Return 0 ·
         Third Dune 0
SAYAÇ İLK KEZ 10:  Third Dune — fırtına cephesinin yaklaşması monotonik
         okundu (S1 çok uzak → S13 yutuyor). D78'in üç başarısız vakasından
         sonra ÇALIŞAN ilk çevresel sayaç: sayaç ufku kaplayan bir DUVAR,
         yani ölçeğin iki ucu her karede birlikte görünüyor.
SAYAÇ:   13 filmin 11'inde N/A — DÖRT filmde sayaç PLANLIYDI ve ekranda okunmadı:
         Dawn Front · Stone Sky (üç çevresel sayaç) · Starless Circle (DÖRT
         çevresel sayaç: çanak eğimi · kuşak yaşı · daire yüksekliği · ışık
         takası — rapor yine "NONE" yazdı). Ders 50'nin "sayacı çevreye bağla"
         çözümü üç kez uygulandı, üçünde de okunmadı → DERS 78
         ⚠️ Blind Return YARIM vaka: dört planlı sayacın ikisi fark edilmeden
         OKUNDU (oksijen rakamları → Nicelik 6 · çatlak → yıpranma çizelgesi),
         ikisi (görüş mesafesi · işaretçi zinciri) hiç okunmadı; "NONE"
         satırının FLAGS'e taşınması kuralı (D78 dipnotu) uygulanmadı
KOSTÜM:  12 filmin 10'unda ≤4; kategori ilk kez Unbroken City (9) ve
         Starless Circle (7) ile kırıldı — ikisi de aynı hafta, ikisi de
         Recurring Entity kartı + sayısal ölçü tablosu taşıyan planlar
EN DÜŞÜK KATEGORİ SKORU: Deep Pressure ve Dawn Front Kostüm-Prop 1/10 ·
                         Stone Sky Nicelik 1/10 (klon)
EN YÜKSEK ZAMAN-IŞIK:    Dawn Front 9/10 — güneş takvimi (14 sahne monotonik) TUTTU
EN YÜKSEK NEDENSELLİK:   Last Archive 9 · Stone Sky 7 — okuma-karar zinciri ekranda izlenebildi
```

> 🚨 **The Blind Return — dört MAJOR'ın dördü de belge kontrolünde kimlik
> değiştirdi; hiçbiri devamlılık ihlali olarak ayakta kalmadı (07.08.2026).**
> ① 🟠 "kask opak kabuğa dönüşüyor" (01:55↔01:56) DÜŞTÜ: FOAM SCHEDULE'ın
> doruğu — köpük vizörün TAMAMINI örter, yüz S11-S14 tasarım gereği görünmez
> (§0.15 rubrik uyarısı bulguyu kelimesi kelimesine öngörmüştü).
> ② 🟠🟠 "uzamsal çöküş" (02:18-02:40, iki MAJOR) KURGU HATASI: mekânlar
> (hava kilidi · 8 m hab · 400 m'deki çıkış aracı) üçü de planlı ve ayrı;
> bozuk olan sıra — **S15 kurguda yok, S16↔S17 ters** → **DERS 81.**
> ③ 🟡 "çatlak vizör 02:40'ta bütün" S16'nın planlı YENİ vizörü; ama
> kurulum sahnesi (S15, Çehov 4) düştüğü için ekranda sihir gibi okundu —
> kurgu hatası olarak ayakta. ④ `COUNTER: NONE` → D78'in YARIM vakası
> (yukarıdaki blok). ⑤ Out-of-scope satırı gerçek aday bulgu: geniş
> planlarda toz RÜZGÂRA KARŞI akıyor — plan 18 sahnede SAĞ→SOL tek yön
> şart koşar; gerçek VIDEO_QA koşusu doğrulayacak (girdisiz koşu → D80).
> → kayıt: [`01_FILM_RAPORLARI/THE_BLIND_RETURN.md`](01_FILM_RAPORLARI/THE_BLIND_RETURN.md)
> · ham: [`02_HAM_RAPORLAR/THE_BLIND_RETURN_MANTIK_HAM.md`](02_HAM_RAPORLAR/THE_BLIND_RETURN_MANTIK_HAM.md)

> 🚨 **The Starless Circle — belge kontrolü bir bulguyu düşürdü, üçünü
> ayakta tuttu, birini yeniden adlandırdı (06.08.2026).**
> ① 🟡 "kara kürenin yükselmesi" DÜŞTÜ: dairenin yüksekliği planlı SAYAÇ C'dir
> (58° → 82° → zenit) — mesafenin göstergesi. ⚠️ Ama raporun kelimesi asıl
> bulgu: **"black sphere"** — plan "a black disc of ABSENCE, not a planet"
> diyor; yokluk nesneleşmiş → **DERS 76.**
> ② 🟠 gece→gündüz sıçraması AYAKTA: plan iki kademeli geçiş yazmıştı
> (S12 PRE-DAWN → S13 DAWN) ve **PRE-DAWN kademesi ekranda yok** — aynı sahne
> filmin bedelinin (boş kalça yuvası) görüldüğü sahnedir; tek eksik sahne iki
> kayıp demek.
> ③ 🔴 klon (2:10) GERÇEK İHLAL ve planın **S14 BİNİŞ** sahnesinde çıktı —
> DERS 69'un üçüncü vakası, üstelik ders yazıldıktan bir gün sonra eklenen
> sahnede → **DERS 77.**
> ④ "terk edilmiş prop" diye raporlanan dört şeyin dördü de planlı Çehov
> halkası (oluk bandı · bakım körfezi · güç hücresi · membran taneleri);
> bulgu yine ayakta çünkü zincirin iki ucu hiçbir karede yan yana gelmiyor
> → **DERS 78.**
> → kayıt: [`01_FILM_RAPORLARI/THE_STARLESS_CIRCLE.md`](01_FILM_RAPORLARI/THE_STARLESS_CIRCLE.md)

> 🚨 **The Stone Sky — belge kontrolü raporun bir BLOCKER'ını düzeltti, birini
> büyüttü (05.08.2026).** Raporun "fizik çelişkisi" saydığı yukarı-taşlar ↔
> aşağı-taşlar (0:10 ↔ 1:18) filmin NOVUM'u çıktı: balistik halka, +51 s'de
> geri düşer — çelişki değil tasarım. Buna karşılık "Nicelik 1/10" klonu
> (1:40) planın ÖNCEDEN işaretlediği S10-B iniş sıcak noktasında çıktı →
> **DERS 69.** Kanyon (S8-S9) planda YOK — düz ova + 1.2 m çatlak vardı;
> Ders 48'in yeni vakası. Rover kayması (0:50 ↔ 1:45) Recurring Entity kartı
> (Ders 58) yazılıyken oldu — Dawn Front'la aynı "dosya dolu, model uymuyor"
> örüntüsü. Üç FLAGS sorusunun üçü de plan dosyasından cevaplandı.
> → kayıt: [`01_FILM_RAPORLARI/THE_STONE_SKY.md`](01_FILM_RAPORLARI/THE_STONE_SKY.md)
> · ham: [`02_HAM_RAPORLAR/THE_STONE_SKY_MANTIK_HAM.md`](02_HAM_RAPORLAR/THE_STONE_SKY_MANTIK_HAM.md)

> 🚨 **Dawn Front, Kostüm-Prop 1/10'un ikinci vakası — ama Deep Pressure'ın
> tersi:** orada Bible hiç yoktu (Ders 55), burada Bible dolu, sayısal ve
> her segmentte birebir tekrarlıydı (Ders 55/57 kilitleri uygulanmış). Yüz
> ×3, suit ×4, yük ×4 yine değişti. Yani kategorinin iki ayrı hatası sanılan
> şeyin ("Bible yok" / "Bible var ama tutmuyor") ikincisi, dosya kalitesiyle
> çözülmüyor — üretim mimarisiyle ilgili (Ders 68: segment başına ayrı üretim).
> Buna karşılık **Zaman-Işık 9/10 = serinin rekoru:** güneş sayacının takvimi
> (S0 −4.0° → S13 +0.4°) sahne başına yazılmıştı ve TUTTU — sayısal takvim
> kilidi ışıkta çalışıyor, kostümde çalışmıyor.
> → kayıt: [`01_FILM_RAPORLARI/THE_DAWN_FRONT.md`](01_FILM_RAPORLARI/THE_DAWN_FRONT.md)
> · ham: [`02_HAM_RAPORLAR/THE_DAWN_FRONT_MANTIK_HAM.md`](02_HAM_RAPORLAR/THE_DAWN_FRONT_MANTIK_HAM.md)

> 🚨 **Deep Pressure, rubriğin bugüne kadar gördüğü en ağır tablo:** 6 bulgunun
> 5'i kostüm, 4'ü BLOCKER, ve dördü de tek bir sebepten — **plan dosyasında
> Character Bible yok.** 13 sahnelik filmin dosyasında 2 "viral ara sahne"
> duruyor, kıyafet ise tarif edilmeden referans veriliyor
> (*"Elif's suit provides a neutral reference point"*).
> Rubrik bunu bilmeden doğru ölçtü: dokümansız çalıştı, "eksik" demedi,
> `FLAGS FOR DOCUMENT CHECK` altına **"kanonik kıyafet hangisi?"** diye sordu.
> Cevap doküman kontrolünde çıktı: **kanonik kıyafet 14 sahnenin hiçbirinde yok.**
> → DERS 55-58 · ham rapor: [`02_HAM_RAPORLAR/THE_DEEP_PRESSURE_MANTIK_HAM.md`](02_HAM_RAPORLAR/THE_DEEP_PRESSURE_MANTIK_HAM.md)

> 🚨 **The Herd, rubriğin ilk "iki bulgusu da yanlış çıkan" vakası.**
> İki `FLAGS FOR DOCUMENT CHECK` sorusunun biri üretim hatasını doğruladı
> (kask takvimi: 15 sahne kapalı, 0 açık), **diğeri filmin öncülünü kurtardı:**
> rapor gökteki sürüyü "nedensellik hatası" sanıp silinmesini önerdi — oysa
> sürü S0'dan itibaren dünyada var ve filmin ters simetrisinin yarısı.
> Öneri uygulansa film yapısal iddiasını kaybederdi. Kaleida emsalinin aynısı.
> Belge kontrolü bu filmde raporu **düzeltti**, tamamlamadı.
> → kayıt: [`01_FILM_RAPORLARI/THE_HERD.md`](01_FILM_RAPORLARI/THE_HERD.md)
> · ham: [`02_HAM_RAPORLAR/THE_HERD_UC_MERCEK_HAM.md`](02_HAM_RAPORLAR/THE_HERD_UC_MERCEK_HAM.md)

> 🚨 **Holding Field, rubriğin ilk "öncül ters render edildi" vakası.**
> Filmin tek kuralı *hiçbir şey yükselmez*; `never rising` yasağı 28 promptun
> 28'inde yazılıydı ve **tutmadı** — ekranda taşlar gökyüzüne süzülüyor.
> Rapor bunu "yerçekimi rastgele dönüyor" diye gördü ve Fizik'e 3/10 verdi;
> doküman olmadan bunun *alternatif durum* değil **yasak durum** olduğunu
> bilemezdi. Teşhis `FLAGS FOR DOCUMENT CHECK` cevaplarından çıktı.
> Kök neden yasağın eksikliği değil, pozitif betimlemedeki **isim seçimi**
> (`hang / suspended / floating` × 24) — Ders 56'nın mekanizması, yeni alan.
> → DERS 59 · kayıt: [`01_FILM_RAPORLARI/THE_HOLDING_FIELD.md`](01_FILM_RAPORLARI/THE_HOLDING_FIELD.md)
> · ham rapor: [`02_HAM_RAPORLAR/THE_HOLDING_FIELD_MANTIK_HAM.md`](02_HAM_RAPORLAR/THE_HOLDING_FIELD_MANTIK_HAM.md)

> 🎯 **Canopy World, kapsam sınırının ilk gerçek testi.** Aynı gün aynı filme
> hem teknik hem mantık QA'sı yapıldı. **Ortak bulgu: 0.** Teknik rapor
> kesme/bloom/morph/metin yazdı; mantık raporu ıslaklık/kemer/ışık salınımı
> yazdı; bloom'u out-of-scope satırına attı, jenerik kartını envantere yazıp
> puanlamadı. İki rapor çift sayım olmadan toplanabiliyor — rubriklerin tek
> tasarım iddiası buydu ve tuttu.

---

## 🚨 DÖRT RAPORUN ORTAK BULGUSU — KOSTÜM VE PROP

```
Kostüm-Prop:   Kaleida 2  ·  Inversion 2  ·  Tidal Hunt 3  ·  Deep Pressure 1
```

**Dört filmin dördünde de en düşük veya en düşüğe yakın kategori bu.** Her
seferinde aynı biçimde: bir ekipman parçası sahneler arasında **açılıp
kapanıyor** — kask (Kaleida, Inversion), vizör (Inversion), dalgıç tüpü
(Tidal Hunt), vinç (Inversion).

Bu, teknik tabloda **görünmeyen** bir darboğaz: VIDEO_QA tek klibe bakıyor
ve tek klipte kask ya vardır ya yoktur — çelişki iki klip arasında doğuyor.
Üçüncü mercek açılana kadar bu hata sınıfı hiç ölçülmemişti.

→ Ders 5 ve 37'nin "tarif kilidi"nden **takvim kilidine** çevrilmesi
  gerektiğini söyleyen kanıt budur (`../LESSONS_LEARNED.md`).

⚠️ **Deep Pressure bu örüntünün tabanını gösterdi (1/10).** Diğer üç filmde
Bible vardı ve tutmadı; bu filmde **Bible hiç yoktu.** Yani kategori iki ayrı
hatayı birden ölçüyor:

```
Bible VAR, model uymuyor      → Kaleida 2 · Inversion 2 · Tidal Hunt 3   → Ders 5/37
Bible YOK, uyulacak şey yok   → Deep Pressure 1                          → Ders 55
```

İkisi aynı sütunda görünüyor ama çözümleri farklı: birinci grup kilit
biçimiyle (tarif → takvim), ikinci grup **dosyayı yazarak** çözülür.

---

## 📌 SAYAÇ SÜTUNU — üç film, üç farklı sonuç

```
Kaleida     8/10   ✅ mor adım izleri film boyunca tutarlı ilerledi
Inversion   2/10   🔴 9 saatlik döngü 2.5 dakikada 3 kez döndü
Tidal Hunt  N/A    🚨 sayaç EKRANA HİÇ ÇIKMADI — filmin omurgası kayıp
```

Üçü de aynı şeyi ölçüyor ve üç farklı başarısızlık biçimi gösteriyor:
**tutarlı · çelişkili · görünmez.** En tehlikelisi sonuncusu, çünkü ekranda
yanlış bir şey yok — sadece bir şey yok. Rubrik bunu `N/A` ile yakaladı ve
`OPEN THREADS` altına yazdı; plan dosyasıyla karşılaştırınca filmin tek
gerilim kaynağının kaybolduğu ortaya çıktı → **DERS 50**.

---

## 📥 SATIR EKLEME KURALI

```
1. MANTIK QA çalıştırılır — YALNIZ VİDEO verilir, doküman VERİLMEZ
2. Rapor header'ında "BASELINE: SELF-CONSISTENCY" yazıyor mu, kontrol et.
   Yoksa rapor yanlış rubrikle çalışmış demektir.
3. Ham çıktı 02_HAM_RAPORLAR/<FILM>_MANTIK_HAM.md olarak kaydedilir
4. Satır bu tabloya yapıştırılır
5. ⭐ FLAGS FOR DOCUMENT CHECK sorularının HER BİRİ plan dosyasından
   cevaplanır ve cevap ham rapora yazılır. Bu adım atlanırsa rubriğin
   yarısı boşa gider — sorular raporun en değerli çıktısı.
6. OUT-OF-SCOPE FLAGS satırları filmin teknik kaydına taşınır
   (01_FILM_RAPORLARI/<FILM>.md) — çoğu, mevcut derslere ilk kez
   TIMESTAMP kazandırıyor.
```

---

## 🔗 İLGİLİ

| Dosya | İçerik |
|---|---|
| `00_INDEX.md` | film başına QA kapsamı — üç mercek |
| `03_HIKAYE_KALITE_TABLOSU.md` | dramatik skorlar |
| `../LESSONS_LEARNED.md` | teknik skorlar + dersler (46-50 ve 55-58 bu rubrikten çıktı) |
