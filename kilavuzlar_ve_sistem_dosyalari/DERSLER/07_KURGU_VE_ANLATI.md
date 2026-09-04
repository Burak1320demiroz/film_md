# 📚 DERSLER — Kurgu ve Anlatı Yapısı

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Kurgu ve Anlatı Yapısı** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🔴 DERS 46: MONTAJ TEKRARI — AYNI BLOK KURGUDA İKİ KEZ

**Kaynak:** The Inversion MANTIK QA (Genel 3/10) — Zaman Çizgisi 🔴 BLOCKER —
`0:36–1:15 vs 1:16–1:55 — Shots S5–S8 are replayed verbatim in S9–S12`

**Sorun:** Kurguya aynı 40 saniyelik blok **iki kez** yerleştirilmiş: su
damlacıkları, tether'da asılı figür, vatoz geçişi — dördü de birebir tekrar.

```
PLANLANAN   130 s  (13 sahne × 10 s)
GERÇEK      167 s
FARK        +37 s  →  tamamı tekrar + planda olmayan jenerik kartı
```

Filme tek saniye yeni anlatı girmemiş. İzleyici bunu "kayıt döngüde kalmış"
diye okur ve bırakır.

**⚠️ BU BİR PROMPT HATASI DEĞİL.** Model bu hatayı yapmadı — klipler doğru
üretildi, **kurgu masasında** iki kez kullanıldı. Bu ders yazılana kadar
projedeki derslerin tamamı
prompt'a bakıyordu; bu sınıfın sahibi yoktu.

**ÇÖZÜM — KURGUDA (prompt'a hiçbir şey eklenmez):**

```
1. SÜRE MUHASEBESİ — kurgu bitince ZORUNLU
   planlanan sahne sayısı × klip süresi = beklenen süre
   gerçek süre bundan SAPIYORSA sapmanın kaynağı satır satır yazılır
   → The Inversion'da +37 s vardı ve kimse sormadı

2. SAHNE SAYIM LİSTESİ
   Kurgu zaman çizgisindeki her blok, plandaki bir sahne numarasına
   eşlenir. Eşlenemeyen blok = ya tekrar ya planlanmamış içerik.

3. TEKRAR YASAĞI
   Aynı klip kurguda birden fazla kez kullanılamaz. Süre kısaysa film
   kısa biter — dolgu yapılmaz. Kısa film, tekrarlı filmden iyidir.
```

**KONTROL:** `MANTIK_QA` §Zaman Çizgisi bu hatayı ilk denemede yakaladı.
Kurgu tesliminden önce çalıştırılırsa maliyeti sıfırdır — bu düzeltme
"1 dakikalık ripple delete" olarak raporlandı.

> 🔗 Ders 33 (compilation kesmeleri) ile aynı aileden ama tersi: 33 kurgunun
> **eklediği** kesmelerdi, 46 kurgunun **tekrarladığı** bloklar.

---

## 🟡 DERS 47: SAHNE ARASI IŞIK SIÇRAMASI — GÜNDÜZ → GECE → GÜN BATIMI

**Kaynak:** The Kaleida Crash MANTIK QA (Genel 4/10) — Zaman ve Işık 3/10 —
`1:15 bright daylight → 1:22 pitch-black night` ·
`1:44 pitch-black night → 1:52 bright twin-sun sunset, same location`

**Sorun:** Bitişik sahneler arasında günün saati sıçrıyor ve geri dönüyor.
Aynı mekanda (gemi gövdesi) 8 saniye içinde gece → gün batımı oluyor.

**Sebep:** Her sahne AYRI üretiliyor ve prompt ışığı sahne bazında tarif
etmiyorsa model her seferinde **kendi ışığını seçiyor.** Kaleida'nın Bible'ı
üç ışık fazı tanımlamış (yangın / yumuşak gökkuşağı / enkaz) — **hiçbiri
gece değil.** Yani model tanımlanmamış bir durumu doldurdu.

**ÇÖZÜM — her sahne promptunun LIGHTING bölümüne, sahne numarasıyla:**

```
LIGHT STATE (scene N of M): [saat] · [yön] · [renk sıcaklığı] · [sertlik]
Örnek:
  "Late afternoon, sun low from frame left, 4800K warm, long soft-edged
   shadows falling to frame right. This is the same light as the previous
   and following scenes — the sun does not move within this sequence."
```

```
⚠️ ZORUNLU EK — filmin ışık takvimi PLAN aşamasında yazılır:
| Sahne | Saat | Güneş yönü | K | Gölge |
Tabloda ardışık iki satır arasında açıklanamayan sıçrama varsa, hata
üretimden önce görülür.
```

**KURGUDA İKİNCİ SAVUNMA:** Sıçrama yine de olursa renk düzeltmesiyle
harmanlanır — Kaleida'da bu "0 USD, post-processing" olarak raporlandı.

> 🔗 Ders 41 ile karıştırma: 41 ışığın **fiziksel doğruluğu** hakkında
> (yumuşak ışık bloom değildir). 47 ışığın sahneler arası **eşleşmesi**
> hakkında. Bir sahnenin ışığı fiziksel olarak doğru olabilir ve yine de
> komşusuyla çelişebilir.

---

## 🟡 DERS 48: SAHNE ARASI BİYOM SIÇRAMASI — ARAZİ TİPİ DEĞİŞİYOR

**Kaynak:** The Kaleida Crash MANTIK QA — Mekan Coğrafyası 4/10 —
`Earth pine tree forest appears on chasm edge; absent in previous scenes` ·
The Inversion MANTIK QA — Mekan Coğrafyası 4/10 —
`S3 shows flat desert with beetles; S4 instantly shows giant cliff rock`

**Sorun:** Bitişik sahnelerde arazi tipi tamamen değişiyor — kristal ova →
Dünya çamı ormanı → kanyon → karanlık enkaz düzlüğü. Aralarında yolculuk
gösterilmiyor, yani izleyici karakterin başka bir gezegende olduğunu
düşünüyor.

**Sebep:** Prompt sahnenin **kendi** ortamını tarif ediyor ama gezegenin
ortak biyomunu tarif etmiyor. Model her sahnede sıfırdan bir manzara kuruyor
ve "orman" kelimesini gördüğünde en bildik ormanı — Dünya çam ormanını —
çiziyor.

**ÇÖZÜM — her prompt'un ENVIRONMENT bölümünün İLK cümlesi:**

```
BIOME CONSTANT (identical in every scene of this film):
[gezegenin değişmeyen üç görsel imzası — zemin malzemesi, bitki örtüsü
 tipi, gökyüzü rengi]

Örnek:
  "Ground is fractured violet-grey crystal sand throughout. The only
   vegetation on this planet is translucent crystalline growth — there
   are NO Earth trees, no wood, no green leaves, no pine, no bark
   anywhere on this world. Sky is warm gold-amber."
```

⚠️ Negatif blokta Dünya bitki örtüsünü **adıyla** yasakla. "Alien forest"
demek yetmiyor; model "forest" kelimesini bildiği ormana çeviriyor.

```
NEGATIVE: pine trees, conifers, oak, birch, green foliage, bark, grass,
Earth vegetation, terrestrial forest, national park scenery
```

> 🔗 Ders 6 (çevre morph) ile aynı değil: 6, **tek klip içinde** arka planın
> kaymasıdır. 48, **sahneler arasında** gezegenin değişmesidir. İkisi ayrı
> yerde çözülür — 6 klip promptunda, 48 film genelinde ortak bir sabitle.

---

## 🔴 DERS 49: NOVUM DÖNGÜSÜNÜN KURGUDA İHLALİ — ÖNCÜL ÇÖKÜYOR

**Kaynak:** The Inversion MANTIK QA (Genel 3/10) — Sayaç Mantığı **2/10** —
`Inversion cycle flips 3 times in 2.5 minutes` ·
`2:02 gravity restores → 2:12 zero-G returns → 2:22 gravity restores again`

**Sorun:** Filmin Bible'ı döngüyü **sayıyla** kilitlemişti:

```
THE_INVERSION_PLANET_FILM.md:52-70
  T-0:00 CONTACT        yerçekimi ters döner
  T+0:00 → T+6:00       THE FLOATING WINDOW — tek, kesintisiz
  T+6:00 THE SLAM       alan çöker, her şey düşer
  T+6:05 SETTLE         taban yerçekimi geri gelir
  → 9 saatte BİR kez, 6 dakika sürer
```

Kurgu bunu 160 saniyede **üç kez** yaptı. Kapanış kartı "her 9 saatte bir"
derken görüntü 30 saniyede bir tersine dönüyor.

**Bu bir devamlılık kayması değil.** Suit'in kirlenmesi düzeltilebilir bir
detaydır; sayacın yönünü kaybetmesi **filmin öncülünü** yok eder. İzleyici
kuralı öğrenemez, öğrenemediği kural için gerilim hissetmez.

**Sebep:** Sahne haritasında her sahnenin **novum durumu** yazılı değildi.
Sahneler tek tek doğru üretildi; yanlış sırada dizildiler.

**ÇÖZÜM — PLAN aşamasında, sahne haritasına zorunlu sütun:**

```
| Sahne | Süre | İçerik | NOVUM DURUMU |
|-------|------|--------|--------------|
| S3    | 10s  | temas  | 1g → 0g GEÇİŞ |
| S4    | 10s  | asılı  | 0g            |
| S5    | 10s  | vatoz  | 0g            |
| S8    | 10s  | çöküş  | 0g → 1g GEÇİŞ |
| S9    | 10s  | sessizlik | 1g         |

KURAL: Durum sütunu monoton olmalı. Bible kaç geçiş tanımladıysa
haritada o kadar GEÇİŞ satırı olur — bir fazla, bir eksik olmaz.
The Inversion'da Bible 2 geçiş tanımlamıştı (giriş + SLAM);
kurguda 5 geçiş göründü.
```

**KURGUDA KONTROL:** `MANTIK_QA` §Sayaç Mantığı sayacın gözlenen eğrisini
çıkarır. Eğri geri dönüyorsa rapor **BLOCKER** verir — diğer skorlar temiz
olsa bile. Bu kural rubriğe bilerek konuldu.

> 🔗 Ders 32 ve 37 ile aynı ailedendir: üçü de **sayısal kilit** ister.
> 32 ölçüyü, 37 ekipman takvimini, 49 novum durumunu sayıya bağlar.

---

## ⚠️ 46-50 HAKKINDA — YENİ BİR DERS SINIFI

```
Ders 1-45   PROMPT hataları   → çözüm: prompt'a cümle eklenir
Ders 46     KURGU hatası      → çözüm: kurgu masasında, prompt değişmez
Ders 47-48  PLAN hataları     → çözüm: film genelinde ortak sabit
Ders 49     PLAN hatası       → çözüm: sahne haritasına durum sütunu
Ders 50     PLAN hatası       → çözüm: yasak ↔ anlatım çelişkisi çözülür
```

İki MANTIK_QA raporunun bulgularının çoğu **üretim dışında** doğuyor ve
**bedelsiz** düzeltiliyor. Kaleida'nın 9 bulgusundan 3'ü, Inversion'ın
9 bulgusundan 3'ü "0 USD, kurguda" olarak raporlandı.

## 🔴 DERS 62: MONTAJDA EN ÇOK DÜŞEN SAHNE FİNALDİR — ÜÇ FİLMDE ÜÇ KEZ

**Kaynak:** üç ayrı film, üç ayrı QA, aynı boşluk:

```
THE RING WALKER   plan S7-S8'i "filmin duygusal zirvesi" ilan ediyor
                  115 s'lik montajda YOK        (31.07.2026)
THE HOLDING FIELD S10 — yükselen gemi, ters simetri, held frame
                  134 s'lik montajda YOK        (03.08.2026)
THE HERD          S11 — boş fener yuvası, Çehov ödemesi, temanın taşıyıcısı
                  152 s'lik montajda YOK        (03.08.2026)
```

> 🔁 **4. vaka — THE STONE SKY (05.08.2026):** plan S12 (OVERVIEW — göz +
> temiz merkez, temanın görüntüsü ve kapak adayı) 135 s'lik kurguda
> bulunamadı; yerini planda olmayan bir başlık kartı aldı (Ders 34).
> Overview olmadan final oturuşu "güvende" değil "yenilgi" okundu —
> senaryo raporunun filmi ters anlamasının kökü bu. Örüntü aynen sürüyor.

**Sorun:** Üçü de filmin **son planlanan sahnesi** ve üçü de **ödeme**
sahnesi — kurulup beklenen şeyin karşılığı. Yani düşen sahne rastgele
değil; sistematik olarak **filmin anlamını taşıyan sahne** düşüyor.

Sebep tahmin değil, aritmetik: kurgu masasına gelen klipler sırayla
işlenir, süre hedefi dolunca durulur. Son sahne, süre hedefine en yakın
duran sahnedir — ve en kolay "zaten bitmiş gibi duruyor" denilendir.

**Neden hiçbir rubrik yakalayamıyor:**

```
VIDEO_QA     kare içine bakar — olmayan sahneyi göremez
MANTIK_QA    "eksik" raporlaması YASAK (haklı olarak, plan dosyası yok)
SENARYO_QA   hisseder ama adını koyamaz — The Herd'de tam olarak bu oldu:
             "Final cockpit check lacks a concluding thematic punch"
             Doğru teşhis, yanlış sebep: sahne zayıf değil, YOK.
```

**ÇÖZÜM — MONTAJ KONTROLÜ SONDAN BAŞLAR:**

```
MONTAJ TESLİM KAPISI — sırayla, ilk madde geçmeden diğerlerine bakılmaz

1. ⭐ SON PLANLANAN SAHNE MONTAJDA MI?
      Plan dosyasının son ## 🎬 SAHNE bloğunu aç. Kompozisyonunu oku.
      Montajın son 10 saniyesiyle KARŞILAŞTIR.
      Eşleşmiyorsa montaj EKSİKTİR — süre tutsa bile.

2. Planın "doruk" / "ödeme" / "ters simetri" dediği sahneler montajda mı?
      Bu kelimeler plan dosyasında aranır, bulunan her sahne işaretlenir.

3. Sahne sayısı: plan N, montaj N. Eksikse hangisi?

4. Toplam süre plandaki süreyle uyuşuyor mu?
```

⚠️ **4. madde en sona bırakıldı bilerek.** Üç filmin üçünde de süre
neredeyse tutuyordu (150 vs 152, 140 vs 134, 129 vs 115) — süre kontrolü
eksik finali **gizliyor**, çünkü kalan sahneler biraz uzun kurgulanınca
toplam yerine oturuyor. Süreye bakan kişi filmi tam sanıyor.

**BU BİR PROMPT DERSİ DEĞİL.** Prompt'a eklenecek cümlesi yok. Kurgu
masasında, teslimden önce, dört maddelik bir bakışla çözülür — ve
şimdiye kadar hiç kimse bakmadı.

> 🔗 Ders 46 (montaj tekrarı) ile aynı aile: ikisi de kurgu hatası, ikisi
> de prompt'la çözülmüyor. 46 fazlalığı, 62 eksikliği ölçer.
> Sınıf tablosu: 1-45 prompt · 46+62 kurgu · 47-50+55+58 plan ·
> 51-54+60-61+63-66 QA'nın kendisi · 56-57+59 sözcük/zaman kilidi.

---

## 🔴 DERS 70: ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — 48 SANİYELİK FİLM KURGUDA 64 SANİYE OLDU, JENERİK KARTI GERİ GELDİ

**KAPI:** BETİK · `olcum_kapisi.sh` KUYRUK/BAŞ KART ŞÜPHESİ (freezedetect −60dB + `son_kare.jpg`) — 01.09.2026
**TEKRAR:** 10 · son vaka 04.09.2026 (THE UPWARD FALL 220,13-225,11 · kart üstelik KAPAK görselidir: kahverengi ceket + baloncuk kask, filmin mat siyah kostümüyle çelişir) · önceki 01.09.2026 (THE PAYLOAD 4:00-4:06 · THE COLD WELD 2:30-2:35) · ⛔ ÇALIŞMIYOR → araca çevrildi: "kart ekleme" cümlesi dokuz teslimde tutmadı, kapı artık betikte

**Kaynak:** THE FIRST MORNING SHORTS_QA koşusu (06.08.2026, MOD V) — 6/10,
REGENERATE · `Negative Violations: 🔴 BLOCKER — title card presented at 1:00`
· `Clips given: 1 joined cut (7 segments) · duration 64s` (plan: 6 × 8 s = 48 s)

**Sorun:** Metin yasağı (Ders 9/34/61) ve 6×8=48 yapısı film dosyasında
KİLİTLİYDİ ve üretim aşamasında TUTTU — rapor sahne içi kesme ve sahne içi
metin bulamadı. İhlal KURGUDA doğdu: plana ekli olmayan fazladan segment(ler)
+ sona eklenen başlık kartı. Ders 61 üretim promptlarında yamalanmıştı;
montaj masasında ikinci kez geri geldi. Prompt-tarafı kilitlerin yalnız
üretimi bağladığı, kurgunun ayrı bir kapı gerektirdiği üçüncü kanıt
(Ders 46 · 62 aynı sınıf).

**ÇÖZÜM — PROMPT DEĞİL, KURGU KAPISI (sayısal):**

```
KURGU KAPISI — dikey shorts, yayın öncesi üç sayı doğrulanır:
  ① klip sayısı  = plan sahne sayısı (6) — plana ekli olmayan segment
                   kurguya GİREMEZ
  ② toplam süre  = 48.0 s (± 0.5 s)
  ③ ekran metni  = 0,0 saniye — JENERİK/BAŞLIK KARTI DAHİL. Başlık
                   platformun açıklama alanına yazılır, kareye değil
                   [Ders 61]. Karta harcanan her saniye en pahalı
                   saniyedir: 0:48'deki loop noktasını da öldürür.
```

> 🔗 Ders 61 üretimdeki jenerik kartını yasaklamıştı; bu ders aynı ihlalin
> kurgu kapısından girdiğini kapatıyor. Ders 62 teslim kapısıyla birlikte
> çalışır: süre/beat kontrolüne klip sayısı ve metin süresi eklendi.
>
> ⚠️ **TEKRAR — 06.08.2026, THE WRONG SHADOW:** aynı gün, aynı çift ihlal —
> 64 s / 7 segment (~10 s'lik sahneler) + sona jenerik kartı; üstelik
> karttaki başlık ("THE DEVIL'S DOUBLE") filmin adı bile değil, model
> uydurdu. Ders yazıldığı gün ikinci kez delindi: kapı metni tek başına
> yürümüyor → **DERS 74** (kapı kaydı zorunluluğu).

---

## 🔴 DERS 71: MERAK PERDESİ ANALOG MEKANİZMAYA EMANET EDİLMEZ — SİS TUTMADI, REVEAL 0. SANİYEYE KAYDI

**Kaynak:** THE FIRST MORNING SHORTS_QA koşusu (06.08.2026, MOD V) — Hook
Timing 6/10: `S0 @ 0:00 anomaly is revealed immediately; no curiosity gap.`

**Sorun:** Hook planı viral zamanlama yasasını (0-2 sn merak → 6. sn reveal)
yazmıştı ama S0 görsel promptu boynu İLK KAREDEN kadraja koyuyordu
(`the silhouette's neck occupies the upper frame`, y≈350-700) — gizleme işi
SİS YOĞUNLUĞUNA bırakılmıştı. Model sis yoğunluğunu derece derece tutmaz:
silüet 0. saniyede net okundu, merak boşluğu doğmadan kapandı. Plan kendi
içinde de çelişikti: metin 6. saniyede "sisin üstüne boyun çıkar" derken
kompozisyon satırı boynu baştan sahneye koyuyordu. Sis/mesafe/flu/ışık gibi
SÜREKLİ (analog) değişkenler perde olarak güvenilmez — kilit ya İKİLİDİR
(kadrajda VAR/YOK) ya da yoktur. Ders 68'in kanıtıyla birleşik: saniye
damgalı beat de promptun içinde tutmuyor.

**ÇÖZÜM — PROMPT DEĞİL, SAHNELEME:**

```
HOOK REVEAL KİLİDİ (dikey shorts):
① Reveal nesnesi 0-5 sn bandında KADRAJDA DEĞİLDİR — gizleme
   "thick mist hides it" gibi yoğunluk sıfatıyla YAPILMAZ; sis
   atmosferdir, perde değil.
② Hook sahnesi I2V'ye alınır: start frame reveal'siz üretilir ve
   kilitlenir (T2V'de saniye damgası tutmuyor — Ders 68). Video
   promptu girişi tek cümleyle yazar: "the neck rises into frame
   from the top edge in the second half of the shot."
③ Plan çelişki denetimi: viral zamanlama satırındaki reveal saniyesi
   ile COMPOSITION satırı AYNI sahneyi anlatmak zorunda — biri
   "6. saniyede girer" derken diğeri nesneyi kareye koyamaz.
```

> 🔗 Ders 3/29 (ışık yayan leke) nasıl "parlamayı" yasaklayıp çözmediyse,
> "sis gizler" de gizlemiyor. Güvenilen tek mekanizma ikili durum:
> kadraj dışı → kadraj içi. Kaynak rubrik §C'ye işlendi.

---

## 🔴 DERS 72: KURGU KAPISI YATAYA GENELLENİR — PLANIN DORUĞU KURGUYA GİRMEDEN FİLM TESLİM EDİLDİ

**KAPI:** BETİK · `olcum_kapisi.sh` KUYRUK/BAŞ KART ŞÜPHESİ — D70 ile aynı araç — 01.09.2026
**TEKRAR:** 10 · D70 ile ortak sayaç · 04.09.2026 THE UPWARD FALL: planlı DORUK S24 kurguya hiç girmedi (⑪ + kare ile doğrulandı) · ⛔ ÇALIŞMIYOR → araca çevrildi (01.09.2026)

**Kaynak:** THE UNBROKEN CITY dört mercek QA (06.08.2026, dördü mod V) —
senaryo Karakter 4/10 ("the astronaut makes zero choices") · mantık
Kurulum 8/10 (`01:30 hook inspected, never used` — OPEN THREAD) · teknik
`2:40 — 🔴 burned-in title` · kurgu 165 s ≠ plan 160 s

**Sorun:** Plan 16 sahne / 160 s; doruk S9'da kayıt cihazı kapı
mekanizmasına verilir ve bedel S12'de görülür. Kurguda kanca sahnesinin
MEKÂNI var, SEÇİMİ yok — filmin tek dramatik motoru ekrana hiç girmemiş.
Üç bağımsız mercek aynı boşluğu üç ayrı dille raporladı (senaryo: seçim
yok; mantık: açık uç; tutundurma: 4/10). Ders 62 sınıfının BEŞİNCİ
tekrarı (Ring Walker · Holding Field · Herd · Stone Sky · Unbroken City).
Ayrıca 2:40'taki yanık metin ("THE WINDOW THAT SHOWS NO SKY") üretim
belgesindeki KAPAK PROMPTUNUN kendi başlık satırıdır — belge metni
kurguya sızdı. Ders 70 kurgu kapısını kurmuştu ama yalnız dikey shorts
kartında duruyordu; yatay teslim akışında kapı yoktu.

**ÇÖZÜM — prompt'a değil TESLİM AKIŞINA eklenecek (TÜM formatlar):**
```
KURGU KAPISI — teslimden önce dört sayı, plan SPEC bloğuna karşı:
1. klip sayısı   = SCENE COUNT           (eksik/fazla sahne → geri)
2. toplam süre   = RUNTIME ± 2 s         (Unbroken City: 165 ≠ 160)
3. ekran metni   = 0.0 sn                (başlık/jenerik/KAPAK ÇIKTISI
                                          dahil — kapak ayrı dosyadır,
                                          kurguya asla eklenmez)
4. CENTRAL CHOICE sahnesi kurguda VAR ve seçim EKRANDA TAMAMLANIYOR
   (mekânın görünmesi yetmez: Unbroken City'de kanca girdi, seçim
    girmedi; Ders 62'nin beş tekrarını tek başına bu madde yakalar)
```

> 🔁 **TEKRAR — 06.08.2026 · THE STARLESS CIRCLE, aynı gün ikinci vaka ve
> 3. madde birebir aynı mekanizmayla delindi.** Kurgunun son 4 saniyesi
> yanık bir başlık kartı: **"THE CIRCLE WITH NO STARS"** — filmin adı bile
> değil (film: THE STARLESS CIRCLE). Bu metin, üretim belgesinin KAPAK
> PROMPTU A sürümünün kendi bölüm başlığıdır (`SUBJECT — THE CIRCLE WITH NO
> STARS:`), üstelik iki satır yukarısında "NO TEXT ANYWHERE IN THE IMAGE"
> yazarken. İki filmde üst üste aynı zincir: **kapak promptunun başlık
> satırı görsele basılıyor → kapak çıktısı kurguya kapanış kartı olarak
> ekleniyor.** Kurgu kapısına ek madde:
> ```
> 3b. KAPAK ÇIKTISI KURGU KLASÖRÜNE GİRMEZ — ayrı dizinde durur.
>     Kapak promptunda "SUBJECT — <başlık>:" gibi BAŞLIKLI satır
>     kullanılmaz; bölüm etiketi yerine düz cümle yazılır, çünkü model
>     etiketi görsele basıyor (Ders 45'in kapak hâli).
> ```

> ⚠️ **BİRİNCİ MADDE 16.08.2026'da DEĞİŞTİ.** `klip sayısı = SCENE COUNT`
> satırı yalnız sahne = çekim = klip olan filmlerde doğrudur. THE LAST SHIFT
> (14 sahne / 24 çekim / 27 klip) bu satıra 14 = 14 diye ✅ verdirdi, oysa
> ekranda 27 klibin ~17'si vardı. Güncel altı maddelik kapı: **DERS 101.**
> Yanık kart zincirinin 7. vakası da bu filmdir (2:50).

---

## 🔴 DERS 73: NOVUM, TÜRETİLMİŞ OPTİK FENOMENE YÜKLENMEZ — ÇİFT GÖLGE 64 SANİYEDE SIFIR KARE ÇIKTI, DÖNME HAREKETİ JALONLARA SIÇRADI

**Kaynak:** THE WRONG SHADOW · SHORTS_QA 5.6/10 + SENARYO_QA 3.0/10
(06.08.2026, ikisi MOD V) — REGENERATE. İki bağımsız merceğin İKİSİNDE de
"çift gölge / second shadow" ifadesi SIFIR kez geçiyor; senaryo merceği
filmi "adam direklere bakıyor, sonda direkler havada dönüyor" diye okudu.

**Sorun:** Filmin tek var olma sebebi — kaynaksız, 1,5°/sn dönen ikinci
gölge seti — ekrana hiç girmedi. Dosya riski öngörmüştü ("kaynaksız
ikinci set ya kaybolur ya çoğalır ya gökyüzüne kaynak uydurulur") ve
sayısal kilitleri eksiksizdi (açı takvimi derece derece, %60 yoğunluk,
kesişim-en-koyu fiziği, 6/6 tekrar). Hiçbiri işe yaramadı, çünkü sorun
kilit eksikliği değil: **model gölgeyi ışık kaynağından TÜRETİR; bağımsız
davranış verilecek bir gölge onun için ayrı bir nesne değildir.** Kaynağı
görünmeyen gölgeye verilen davranış ya silinir ya da dördüncü (yeni) modda
BİRİNCİL NESNEYE TRANSFER olur — "dönen gölge" → "dönen jalon". Gölge,
yansıma, kostik, ışık sütunu gibi türetilmiş fenomenler bu sınıftadır.

**ÇÖZÜM — prompt değil, KARAR + KAPI:**

```
NOVUM TAŞIYICI KURALI (plan yazılmadan):
① Novum'un taşıyıcısı BİRİNCİL, çizilebilir bir nesne/durum olmalı
   (cisim, arazi, gökyüzü, ışık KAYNAĞI). Türetilmiş optik fenomen
   (gölge · yansıma · kostik · parlama deseni) üzerine kurulan novum
   YÜKSEK RİSK sayılır ve ② şartsız yazılamaz.
② TEK KARE FİZİBİLİTE KAPISI: 6 sahne / tam plan üretilmeden önce
   novum'u en çıplak gösteren TEK görsel prompt (S0 veya doruk karesi)
   koşulur. Karede novum sayısal speciyle okunmuyorsa (örn. nesne
   başına TAM 2 gölge) video üretimine geçilmez — konsept ya I2V
   start-frame kilidine alınır ya taşıyıcı değiştirilir.
③ Kapının maliyeti 1 görsel üretim; atlandığında maliyeti bu koşuda
   6 video + kurgu + 2 QA merceği oldu.
```

> 🔗 Ders 50 (sayaç ekrana hiç çıkmadı) ve Ders 59 (yasak, adını andığı
> şeyi çağırır) ile aynı aile: modelin ÇİZEMEYECEĞİ şeyi prompt cümlesi
> çizdiremez. Üç kalite sıçramasının üçü de karar değişikliğiydi — bu da
> öyle: taşıyıcı seçimi plan aşamasının kararıdır.

---

## 🔴 DERS 78: SAHNELER ARASI ANLATIM OKUNMUYOR — DÖRT ÇEVRESEL SAYAÇ VE FİLMİN BEDELİ, TEK KAREDE KANITLANMADIĞI İÇİN GÖRÜNMEDİ

**KAPI:** BETİK · `prompt_kontrol.py` A1 ÇELİŞKİSİ (yasak ↔ ekran içeriği aynı dosyada) — kapı 12.08.2026'dan beri vardı, satır 01.09.2026'da yazıldı
**TEKRAR:** 5 (×5 — 01.09.2026 sayımı)

**Kaynak:** THE STARLESS CIRCLE (06.08.2026) — MANTIK_QA
`THE COUNTER: NONE` + `Setup & Abandonment 3/10` ("cylinder, tool wall,
case, particles — introduced and abandoned"); KARAKTER_QA pasaportunda
güç hücresi de, boş kalça yuvası da **hiç geçmiyor**. Oysa plan DÖRT
çevresel sayaç (çanak eğimi 55°→90° · kuşak yaşı 300 m→4 m · dairenin
yüksekliği 58°→zenit · ışık takası soğuk→sıcak) ve bir bedel nesnesi
(12 cm güç hücresi: S0-S8 kalçada, S10-S14 yuva BOŞ) tanımlıyordu.

**Sorun — ve bu Ders 50'nin çözümünün çürümesidir.** Ders 50 "sayacı
metinden çıkar, fiziğe/çevreye bağla" demişti. Bu film onu ders kitabı gibi
uyguladı: dört sayaç, sıfır metin, hepsi monotonik, hepsi tabloyla yazılı.
**Sonuç yine `COUNTER: NONE`.** Sebep artık net:

```
Sayaç da bedel de, izleyicinin İKİ AYRI SAHNEYİ hafızada karşılaştırmasını
istiyor:  S1'deki 55° ↔ S8'deki 90°  ·  S2'deki oluk deseni ↔ S10'daki
ritim  ·  kalçadaki hücre ↔ 40 saniye sonraki boş yuva.
Kesmeyle ayrılmış iki durum, izleyicide TEK bir değişen büyüklük kurmuyor.
Denetçi de kuramıyor — ve denetçi burada izleyicinin vekilidir.
```

İkinci mekanizma bedel nesnesine özel: anti-metin/anti-gösterge kilidi
(Risk Kartı 5) propu **"ekransız, ışıksız, işaretsiz düz koyu blok"a**
indirdi. Silueti olmayan nesnenin yokluğu da görülmez. Unbroken City'de
birebir aynısı olmuştu (24 cm kayıt cihazı → jenerik "chest box"); iki
filmde iki doruk, aynı sebeple okunmadı.

**ÇÖZÜM — plan aşaması, iki sayısal kural:**

```
① TEK KARE KANITI: Bir sayaç, en az BİR karede iki ucunu AYNI ANDA
   göstermek zorundadır. (Bu filmde bir tek kare yeterdi: ön planda
   90°'lik 4 m'lik İlk Dinleyici, arkada 55°'lik 300 m'lik kolos —
   sayaç o karede kurulur, kalan 17 sahne onu ilerletir.)
   Karşılaştırma karesi yazılmamışsa o sayaç PLANDA YOKTUR, sil.

② BEDEL NESNESİ SİLUET TESTİ: 120 pikselde siluetinden tanınmayan
   nesne bedel taşıyamaz. Kilit üçlüsü:
     · nesnenin RENGİ gövdeden ayrışır (kemik beyazı suit ↔ kızıl hücre)
     · nesne en az 2 sahnede YAKIN planda VARDIR
     · yokluğu en az 1 sahnede YAKIN planda kadrajlanır (boş yuva +
       açık kelepçe kadrajın merkezinde, tam ekran değil el planı)
   "no screen, no lights, no markings" kilidi nesneyi görünmez yapıyorsa
   kilit korunur ama nesneye BİÇİM verilir — yasak, anlatıyı silemez
   (Ders 50'nin ilk cümlesi hâlâ geçerli).
```

> 🔗 Ders 50 (sayaç ekrana çıkmadı · Tidal Hunt) · Ders 62/72 (doruk
> kurguya girmedi). Bu ders üçüncü hâli: **doruk kurguda VAR, bedel
> nesnesi yok, sayaç yok — yani sahne var, anlam yok.**

---
## 🔴 DERS 83: ORTAM YATAĞI KLİP SINIRINDA ÖLÜYOR — KURGUYA SÜREKLİ SES YATAĞI SERİLMEDEN FİLM TESLİM EDİLMEZ

**Kaynak:** THE COLD BURN SES_QA ilk koşusu (09.08.2026) — Ortam Devamlılığı
**3/10** — `1:20-1:40 — total digital silence for 20 seconds` · `0:50 —
1-second dead hole at the cockpit cut` · `music cues hard-cut at scene
transitions`
**Sorun:** Şot şot üretimde her klip KENDİ odasını üretir ve hiçbir ses
kesmeyi geçmez: kabin uğultusu 1:19'da var, 1:20'de mutlak sıfır; müzik
cümle ortasında kesiliyor; seviye her kesmede sıçrıyor. İzleyici bunu
adlandıramaz ama "bozuk kurgu" olarak HİSSEDER — mutlak dijital sessizlik,
ekrandaki hatalardan farklı olarak filmin TAMAMINI amatörleştirir. Planda
"üç sahne müziksiz" yazması bunu aklamaz: MÜZİKSİZ ≠ SESSİZ, tasarlanmış
sessizliğin bile bir zemin tonu (oda, uğultu, rüzgar) vardır.

**ÇÖZÜM — prompt değil KURGU/MİKS; teslim öncesi SES KAPISI (kurgu
kapısının [D72] beşinci maddesi olarak koşulur):**
```
① YATAK: lokasyon başına BİR sürekli ortam yatağı kurgu boyunca serilir;
   klip kendi ortam sesini taşısa bile yatak altta kesintisiz akar.
② SIFIR YASAĞI: mutlak dijital sessizlik yalnız bilinçli tasarımsa kalır
   ve çevresi sesli olmalıdır (sessizliği okunur kılan kontrast).
③ KESME TESTİ: hiçbir kesmede seviye sıçraması duyulmaz; müzik cümle
   ortasında kesilmez, kuyruklar yumuşatılır.
④ HİYERARŞİ: replik altındaki efekt yatağı duck edilir — katman sayısı
   anlık 3-4'ü geçiyorsa önce yatak kısılır [VEO kılavuzu §7].
```
Bu maddelerin DÖRDÜ de miks seansı işidir — yeniden üretim gerektirmez.
SES_QA'nın "FIXABLE IN THE MIX vs REQUIRES REGENERATION" ayrımı tam bu
yüzden var: Cold Burn'de 5 bulgunun 4'ü miksle kapanıyordu.

> 🔗 Ders 70/72 (kurgu kapısı — bu ders ona ses maddesi ekler) · Ders 35
> (ses katman limiti üretim tarafında). Rubrik bu hata sınıfını "signature
> failure of shot-by-shot AI generation" olarak ÖNGÖRMÜŞTÜ; ilk koşu
> doğruladı.

---

## 🔴 DERS 100: SABİT KLİP TAVANI + KIRPMA TALİMATSIZ PLAN = KURGU KIRPMAZ, KLİP DÜŞÜRÜR — 27 KLİPLİK FİLM 17 KLİPLE "SÜREYİ TUTTURDU"

**Kaynak:** THE LAST SHIFT dört mercek QA (16.08.2026, dördü mod V) —
plan 14 sahne / **24 çekim / 27 klip / 190 s / ASL 7.9 s**; kurgu **174 s ve
tekdüze 10 s ızgarası** (17 × 10 s + 4 s başlık kartı). Dört bağımsız sahne
haritasının dördü de aynı zaman kodlarını verdi: 0:09 · 0:19 · 0:29 · 0:49 ·
0:59 · 1:19 · 1:39 · 1:49 · 1:59 · 2:09 · 2:19 · 2:29 · 2:49.

**Sorun:** Depodaki filmler bugüne kadar **sabit 10 s ızgarasıyla** yazıldı
(16 × 10 s = 160 s). Bu, hattın klip uzunluğuyla planın birimi aynı olduğu
için kurguda kırpma gerektirmiyordu. Bu film ilk kez DEĞİŞKEN çekim süresi
planladı (2.0-20.0 s, ASL 7.9) ve aritmetik şudur:

```
27 klip × ~10 s (hattın verdiği sabit uzunluk)  =  ~270 s ham malzeme
plan hedefi                                     =   190 s
KIRPILACAK                                      =   ~80 s
```

O 80 saniyeyi kimin, nerede, hangi klipten alacağı **hiçbir belgede yazmıyordu**.
Süreler iki yerde duruyordu ve ikisi de kurgucuya verilen bir talimat değil:
§0.9 sahne haritası (plan tablosu) ve VİDEO PROMPTUN İÇİ (`MOTION — 2.5
seconds ...`). **Prompt, dosyanın uzunluğunu değiştirmez** — 2.5 saniyelik
eylem 10 saniyelik klibin içine yazılır, kalan 7.5 saniye kurgucunun işidir.

Kurgu bunun yerine **klip düşürdü**: 17 klip tam 10 s olarak kaldı, ~10 klip
kurguya hiç girmedi ve süre 174 s'ye "tuttu". Düşenler arasında filmin İFŞA 1'i
(S5 — altmış bir çift bot, VİRAL ARA, filmin ölüm anlatma yönteminin tamamı) ve
tek aksiyon ritmi (S11 — 4 çekim / 9 s / ASL 2.25) var. **Süre yaklaşık tuttuğu
için kayıp görünmedi** — D62'nin "runtime hides a missing finale" mekanizmasının
klip ölçeğindeki hâli.

⭐ Ve zincirin sonu: kurgu, düşürdüğü sahnenin bilgisini **yazıyla** geri koydu.
2:50'deki yanık kartın alt satırı ("altmış bir çift bot, sıfır insan") depoda
yalnız TEK yerde geçiyor — §5.3 kapak tipografisi. Görüntü düştü, cümle kaldı.

**ÇÖZÜM — prompt değil PLAN + KURGU TALİMATI (her formatta):**
```
① KIRPMA TABLOSU ZORUNLU. Çekim süresi hattın klip uzunluğundan FARKLI olan
   her film, §0.18'e klip başına tek satır yazar:
     | klip | ham | kurguda | nereden kırpılır |
     | S11-Ç1 | 10.0 s | 2.5 s | baştan 1.0 · sondan 6.5 (botlar kadraj dışına çıkınca) |
   Tablosu olmayan değişken süreli plan, sabit ızgaralı plan sayılır.

② HAM MALZEME SATIRI SPEC'E YAZILIR:
     RAW FOOTAGE: 27 klip × 10 s = 270 s   TRIM BUDGET: 80 s
   Kurgu kapısı bu iki sayıyı da okur.

③ KLİP TAVANININ ALTINDAKİ ÇEKİM YALNIZ KURGUDA VAR OLUR. 5 s'nin altında
   çekim planlayan sahne, plan dosyasında "üretimde değil KURGUDA doğar"
   etiketiyle işaretlenir; üretim kapısı o sahneyi ham hâliyle onaylar.

④ DÜŞEN KLİBİN BİLGİSİ METNE DÖNÜŞTÜRÜLEMEZ. Kurguya giren tek harf yoktur
   [D70/72]; bir sahne düştüyse çözüm sahneyi geri koymaktır, alt yazı değil.
```

> 🔗 Ders 62 (süre tutarken sahne kaybolur) · Ders 70/72 (kurgu kapısı) ·
> Ders 81 (kapı sırayı ve kurulum sahnelerini saymıyor) · Ders 101 (kapı
> yanlış birimi sayıyor — bu dersin ölçüm tarafı).

---

## 🔴 DERS 101: KURGU KAPISI SAHNE SAYIYOR, ÇEKİM SAYMIYOR — "SAHNE ≠ ÇEKİM" OLAN İLK FİLMDE KAPININ BİRİNCİ MADDESİ ✅ VERDİ

**Kaynak:** THE LAST SHIFT (16.08.2026) — plan `SCENE COUNT: 14 · SHOT COUNT:
24 · CLIP COUNT: 27`; kurguda 14 segment. Dört mercek de 14 saydı ve dördü de
DOĞRU saydı.

**Sorun:** D72'nin kurgu kapısı birinci maddesi şöyle yazılmıştı:
`klip sayısı = SCENE COUNT`. Bu, sahne = çekim = klip olan filmlerde çalışır ve
depodaki 20 küsur film bugüne kadar öyleydi. Bu filmde üç sayı üç ayrı şeydir ve
kapı **14 = 14** görüp ✅ verdi; oysa ekranda 27 klibin ~17'si vardı. Kapının
yakaladığı tek şey süre maddesiydi (174 ≠ 190) — ve tek başına o, "sahneler
kısa kesilmiş" diye okunup geçilebilirdi. Kayıp klipler ancak plan↔kurgu
eşlemesi elle yapılınca göründü.

Aynı körlük ritim tarafında da var: kapının **ASL maddesi yok.** Filmin bütün
ritim iddiası (üç mod, tek aksiyon kartı, esirgeme) tek bir sayıya bağlıydı ve
o sayı kurguda ölçülmedi.

**ÇÖZÜM — kurgu kapısı [D72] maddeleri güncellenir:**
```
① klip sayısı  = CLIP COUNT      (SCENE COUNT DEĞİL)
①b çekim sayısı = SHOT COUNT     (sahne ≠ çekim olan filmlerde ayrı satır)
①c sahne sayısı = SCENE COUNT
   ⛔ Üçü eşitse film sabit ızgaralıdır ve tek satır yeter; eşit değilse
      ÜÇÜ DE ölçülür. Eşit sanmak, en kalabalık birimi görmemektir.
② toplam süre  = RUNTIME ± 2 s
③ ekran metni  = 0.0 s (jenerik/başlık kartı ve KAPAK ÇIKTISI dahil)
④ CENTRAL CHOICE sahnesi ekranda ve seçim TAMAMLANIYOR
⑤ 🆕 ASL = süre / çekim sayısı, SPEC'teki hedef bandın içinde mi
⑥ 🆕 EN KISA ÇEKİM TESTİ: planın en kısa çekimi kurguda o uzunlukta mı?
      (Last Shift: planın en kısası 2.0 s; kurgudaki en kısa 10.0 s —
       tek satırlık bu test, kayıp ritim modunu tek başına yakalar)
```

> 🔗 Ders 100 (kırpma bütçesi — bu dersin plan tarafı) · Ders 72 (kapının
> kendisi) · Ders 81 (kapı sırayı saymıyor). Üçü birlikte okunur: kapı SAYI,
> SIRA ve BİRİM olmak üzere üç ayrı yerden delindi.

---

## 🟡 DERS 114: SPOILER KAPISI KURGUDA KOŞULDU, PAKETLEMEDE KOŞULMADI — AÇIKLAMA METNİ FRAGMANIN SAKLADIĞI HER ŞEYİ TEK CÜMLEDE VERDİ

**Kaynak:** THE COLD BURN — FRAGMAN DİKEY · 17.08.2026 · aynı oturumda üretilen
başlık/açıklama/etiket paketi ·
`FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_COLD_BURN_FRAGMAN_SENARYO_HAM.md` §paketleme
**Sorun:** ilk vaka — ama depodaki her fragman aynı paketleme promptundan geçecek

`FRAGMAN_KILAVUZU.md` §1.2 spoiler kapısını 17.08'de plandan KURGUYA taşıdı
(3 madde: liste 0 kare · TEK CÜMLE TESTİ · İMZA TESTİ). Kapı bir adım eksik
kaldı: **teslimin üçüncü yüzeyi paketlemedir** ve orada hiç koşulmadı.

```
fragmanın işi   çıkışı göstermeden bırakmak; 48. saniyede tek soru kalmalı:
                "yanaşamazlarsa nereye gidecekler?"
açıklama metni  "From a ground-shattering geyser eruption to a tense orbital
                docking procedure" → fragmanın altı vuruşunun yayını, sonucu
                dahil, tek cümlede veriyor
başlık          "THE COLD BURN | Epic Sci-Fi Short Film" → 48 saniyelik bir
                teaser'ı KISA FİLM diye satıyor; izleyici filmi izlediğini
                sanıp kaynak filme hiç gitmiyor
etiketler       "short film", "sci fi movie", "space movie" — aynı yanlış vaat
```

Kurgu testini geçen bir fragman, açıklama kutusunda çökebilir: izleyici oynat
tuşuna basmadan önce metni okur. Sıra şudur — **başlık, açıklama, kurgu.**

**ÇÖZÜM — paketleme promptuna TEASER modu (`VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md`):**

```
① AÇIKLAMA FRAGMANIN SORUSUNDAN YAZILIR, OLAY ÖRGÜSÜNDEN DEĞİL.
   Fragman dosyasının "BIRAKTIĞI SORU" satırı açıklamanın ilk cümlesidir.
   ⛔ Açıklamada olay dizisi yasak: "X olur, sonra Y olur, sonra Z" kalıbı
      fragmanın tek ürününü (borç) siler.
② TEK CÜMLE TESTİ AÇIKLAMAYA DA KOŞULUR: metni ilk kez okuyan biri filmi
   tek cümleyle anlatabiliyorsa paketleme ÇÖKMÜŞTÜR.
③ TÜR ADI DOĞRU YAZILIR: teaser "short film" değildir. Başlıkta ve
   etiketlerde tür = teaser / önizleme; "short film" ve "movie" etiketleri
   YALNIZ kaynak filmin kendi paketinde kullanılır.
④ ÇAĞRI KAYNAK FİLMEDİR: fragmanın CTA'sı beğeni değil, filme gidiştir.
⑤ İSİM VE TAGLINE UYDURULMAZ: pakette geçen her cümle depoda bir dosyada
   geçmelidir (kardeş vakada model kendi tagline'ını uydurup karta yaktı).
```

> 🔗 Ders 106 (rubrik borç bırakmayı cezalandırdı — bu, onun PAKETLEME
> tarafı) · Ders 111 (kilavuzda yaşayan yasak koşulmuş sayılmaz) · Ders 70/72
> (başlık karede değil platform başlığında yaşar; bu ders o başlığın NE
> DİYECEĞİNİ kurallar) · `FRAGMAN_KILAVUZU.md` §1.2.

---
## 🔴 DERS 121: ŞERİT VE REPLİK "TUTUYOR MU"YU DEĞİL "KAÇ YUVA KAYMIŞ"I SÖYLER — Δ EĞRİSİ FAZLA VE EKSİK KLİPLERİ MASTER AÇILMADAN YERİYLE BULUR; ÜÇ MERCEK AYNI DUPLİKE KLİBİ ÜÇ FARKLI HASTALIK SANDI

**Kaynak:** THE BORROWED WEIGHT · 24.08.2026 ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_BORROWED_WEIGHT.md` § kurgu aritmetiği
**Sorun:** parti ⑤'ten geçmedi, dört skor da geçersizdi — ama **iki raporun
insan şeridi ve bir raporun replik alıntıları teslim kurgusunu saniyesine
kadar yeniden kurdu.** D118 şeridi "aynı mı değil mi" diye soruyor ve
"değil" deyip duruyor. Farkın KENDİSİ bir ölçümdür:

```
PLAN          1111111111111-11111-11111    25 yuva   (- = S13 · S19)
① KARE        1111111111111111-11111-111   26 yuva
② DEVAMLILIK  1111111111111111111111-1     24 yuva

⭐ İki mercek insansız yuvanın MUTLAK YERİNDE anlaştı: 3:40-3:50.
   S13 planda 2:09-2:19 → teslimde 2:40-2:50   Δ = +31 s ≈ +3 klip
   S19 planda 3:09-3:19 → teslimde 3:40-3:50   Δ = +31 s ≈ +3 klip
                                               └ iki eksen, aynı sayı

ŞERİDİN BÖLÜNMESİ — fazlalık önde, eksiklik arkada
   yuva  1-16  → planın S0-S12'si (13 sahne)   → +3 FAZLA KLİP
   yuva  17    → S13 ✓        yuva 18-22 → S14-S18 ✓ birebir
   yuva  23    → S19 ✓        yuva 24-26 → S20-S24 (5 sahne) → −2 EKSİK
   26 × 10 s = 260 s + 4 s kart = 264 s  ✓ raporların ölçtüğü süre
```

**Replik ekseni aynı sonucu bağımsız verdi.** Aynı replik 0:23 ve 0:33'te —
tam BİR YUVA arayla — duyuldu; senaryoda o replik tektir. Fazladan üç
klipten biri, S2 klibinin ikinci kez kullanılmasıdır.

**Ve asıl bedel:** tek bir kurgu kusuru üç mercekte üç farklı hastalık gibi
göründü, üçü de YANLIŞ reçete yazdı:

```
🔊 SES     "aynı replik iki kez, matematiksel olarak birebir"
           → reçete: "repliği sustur veya değiştir"  (miks işi)
📖 HİKAYE  "S5-S6 gereksiz emek, ikinci dakikada yeni bilgi yok"
           → reçete: "sahneleri KES"                 (senaryo işi)
📖 HİKAYE  "düz duygu yayı, kriz yok, bedeli düşük final"
           → reçete: "doruğa fiziksel çöküş EKLE"    (yeniden üretim)
GERÇEK     kurguda plan dışı 3 klip var ve kuyrukta 2 sahne YOK —
           bunlardan biri filmin bütün önermesini taşıyan TWIST finali.
           Doğru eylem: kurguyu düzelt. Ne miks, ne senaryo, ne üretim.
```

**ÇÖZÜM — ortak adım ④ madde (c) "aynı mı"da durmaz, FARKI OKUR:**

```
c) SIRA — iki dize yan yana. Aynıysa doğrulandı. DEĞİLSE Δ TABLOSU YAZILIR:

   ① insansız yuvaların MUTLAK saniyeleri eşlenir (plan ↔ rapor)
        Δ = rapor saniyesi − plan saniyesi
   ② fazla/eksik klip sayısı = Δ ÷ klip süresi
   ③ Δ ilk insansız yuvada zaten büyükse fazlalık ÖNDE;
      Δ iki insansız yuva arasında SABİTSE o aralık birebir;
      son insansız yuvadan sonraki yuva sayısı planınkinden AZSA
      kuyrukta sahne EKSİK  ⛔ önce oraya bakılır: kuyruk, filmin
      finalidir [D62/D72].
   ④ replikli filmde aynı hesap replik ekseninde tekrarlanır:
        Δ(replik) = raporun duyduğu saniye − planın DIALOGUE SCHEDULE'ı
        Δ sabit            → kurgu hizalı (sabit değer = uygulanmayan kırpma)
        Δ iki replik arası SIÇRIYOR → kurgu tam orada malzeme kazanmış
        aynı replik bir yuva arayla İKİ KEZ → duplike KLİP (ses bulgusu değil)
   ⑤ iki eksen aynı sayıyı veriyorsa sonuç ÖLÇÜMDÜR, tahmin değil:
      master'da yalnız işaret edilen yuvalar izlenir (yuva başına ~10 s).
```

⭐ **Bu, geçersiz bir partiden bile çıkan tek sağlam çıktıdır.** Skorlar
kapılardan geçmediği için çöpe gitti; şerit ve replik alıntısı ise modelin
yorumu değil, SAYIM'ıdır — ve iki bağımsız mercekte aynı çıktı.

> 🔗 Ders 118 (insan şeridi — bu ders onun okunma biçimi) · Ders 115 (ızgara
> geri alma; Δ eğrisi onun zaman eksenindeki genişletilmişi) · Ders 100/101
> (kurgu kapısının klip/çekim/sahne birimleri) · Ders 72/62 (planın doruğu ve
> son sahnesi kurguya girmeden teslim) · Ders 120 (kart ayıklanmadan şerit
> aritmetiği koşulamaz) · Ders 122 (bu hesabın referans sayıları planda elle
> yazılıyor — 4 kaydın 2'si bir yuva geçti).

---


---

## 🔴 DERS 141: KLİP VAR, VURUŞ YOK — KURGU KAPISININ ÜÇ SATIRI DA GEÇTİ, FİLMİN TWIST'İ VE DÖNGÜSÜ EKRANDA YOKTU

**Kaynak:** THE THIN ROOF QA (28.08.2026) — S5 · 50,03-60,03 s ·
④ HİKAYE "Ending 3/10 · ENDS OR STOPS: **Stops**"
**Sorun:** kurgu kapısı klip SAYAR, vuruş sayamaz

Kurgu kapısının (ortak adım ④) üç satırı da temiz geçti:

```
a) klip sayısı   6 = 6              ✅
b) süre          60,033 = 60,03     ✅   (Δ = +0,003 s)
c) İNSAN ŞERİDİ  111111 = 111111    ✅
```

Ve filmin finali teslim edilmedi. S5 klibi VAR, 10 saniye, kadın ayağa
KALKIYOR (twist'in mekanizması) — ama twist'in KENDİSİ, planın
`TOHUM → KARŞILIK` zincirinin üçüncü halkası, ekranda yok:

```
PLAN  56,53-58,03  TWIST: ovada üç çöküntü daha, ufka kadar, dümdüz bir hatta
                   (210 m · 480 m · 790 m — yalnız ayakta göz hizasından görünür)
EKRAN 56,50 / 58,00 / 59,50 kareleri:  düz ova + kesintisiz kaya duvarı.
                   Çöküntü YOK. Sıfır tane.
PLAN  60,03 → 0,00 DÖNGÜ — jest eşleşmesi, aynı kurulum, aynı ışık
EKRAN 59,90 karesi ile 00,10 karesi: farklı kamera yüksekliği, farklı arka
                   plan, farklı ölçek. Eşleşme yok. Döngü öldü.
```

⭐ **D62/D72 "sahne eksik" der; bu onun daha sinsi hâlidir: SAHNE VAR,
VURUŞ YOK.** Eksik sahne aritmetikte görünür (süre tutmaz, sayı tutmaz).
Eksik VURUŞ hiçbir aritmetikte görünmez — klip tam boyunda, doğru yuvada,
insan içinde. Kapı ✅ verir ve filmin bütün yükünü taşıyan iki saniye
sessizce kaybolur.

⛔ Ve bunu gören tek mercek, plana hiç bakmayan ④ oldu: *"the character
pushes up, completely ignoring the climax."* Belgesiz mercek yarayı HİSSETTİ,
sebebini bilemedi ve reçetesinde filmin KESİLEMEZ sahnelerini kesmeyi önerdi.

**ÇÖZÜM — SPEC'in B BLOĞUNA yeni zorunlu satır: FİNAL VURUŞ KANITI**

```
FİNAL VURUŞ KANITI: <tek karede ekranda BULUNAN ya da BULUNMAYAN, ADI
KONABİLİR bir nesne> · <hangi saniyede> · <kaç tane>

örnek (THE THIN ROOF):
  FİNAL VURUŞ KANITI: ufka giden hatta ÜÇ dairesel çöküntü · 57,0 s ·
  sayılabilir, 3 adet · yoklarsa final teslim edilmemiştir
```

```
⛔ KURGU KAPISINA DÖRDÜNCÜ SATIR (a/b/c'den sonra):
   d) FİNAL VURUŞ KANITI ekranda mı?
      ffmpeg -ss <saniye> -i "$MASTER" -frames:v 1 kanit.jpg
      → tek kare, tek bakış, ~10 saniye iş.
      YOKSA: koşu ÖN KOŞU'dur, Final ve Duygu Yayı kategorileri SAYI
      TAŞIMAZ, ve o klip yeniden üretilir.
   Bu satır a/b/c gibi SAYIYLA değil, KAREYLE koşulur — çünkü ölçtüğü şey
   sayı değil, VARLIKTIR.
```

⭐ **Kanıt seçme kuralı:** kanıt SAYILABİLİR ve ADI KONABİLİR olmalı.
"final duygusu", "yalnızlık hissi", "ufka bakış" kanıt değildir. "Üç
çöküntü", "ikinci kule", "sönmüş lamba", "boş kanca" kanıttır. Tek karede
görülemeyen bir vuruş, tek karede doğrulanamaz — o zaman kanıt, vuruşun
BAŞLANGIÇ ve BİTİŞ karesindeki fark olarak yazılır.

⛔ **Ve döngü ayrı bir kanıttır.** Dikey formatta döngü zorunludur
[FINAL §2]; kanıtı iki karedir:

```
   ffmpeg -ss 0.10 -i "$M" -frames:v 1 ilk.jpg
   ffmpeg -ss <süre-0.15> -i "$M" -frames:v 1 son.jpg
   → yan yana. Aynı kurulum · aynı ölçek · aynı ışık · aynı jest mi?
   Değilse döngü yoktur; ve arkasına eklenen HER KARE (başlık kartı dâhil)
   döngüyü zaten öldürmüştür [D70/D72].
```

> 🔗 Ders 62/72 (kuyrukta sahne eksik — bunun aritmetikte GÖRÜNEN hâli) ·
> Ders 121 (Δ okuma prosedürü — burada Δ = 0 ve film yine eksik) ·
> Ders 115 (kesme ızgarası) · Ders 117/129 (SPEC dosyası) · Ders 134
> (belgesiz merceğin sıralaması sonuç sıralaması değildir).

---

## 🔴 DERS 157: NOVUMUN TAŞIYICISI TEK KARE TESTİNİ KENDİSİ GEÇMİYORDU — KURAL EKRANA HİÇ GELMEDİ VE İKİ MERCEK ONU "TEKRAR" SAYIP KESME LİSTESİNE YAZDI

**KAPI:** BETİK · `prompt_kontrol.py` ⑭ NOVUM TAŞIYICI (taşıyıcı nesne TEK KARE satırında geçmeli) — 01.09.2026
**TEKRAR:** 1 · 01.09.2026 THE COLD WELD: ders sabah yazıldı, aynı gün yazılan film onu okumadı, akşam 6/6 mercek novum'u adlandırmadı (⬜ AÇIK — GOZLEM_DEFTERI ADAY-1)

**Kaynak:** THE PAYLOAD QA (01.09.2026) — planın novum taşıyıcısı: ön iniş
bacağının cilalı milindeki parlak bant (iki parmak S4 → bir el S8 → iki parmak
S12). Altı mercek, **bandı bir kez bile anmadı.** ② DEVAMLILIK: `0:40 / 1:20 —
Hand hits strut and dust pours out exactly the same twice 🟡` · ④ HİKAYE:
`S5 CUT (redundant pair with S9)` + `S9 CUT (shows what S5 already showed)` —
**sıralı kesme listesinin 2. ve 3. maddesi novumun iki taşıyıcı sahnesidir.**
**Sorun:** kural görünmedi; görünmeyince tekrar sayıldı; tekrar sayılınca
kesilmesi önerildi.

```
PLANIN KENDİ İÇİNDEKİ ÇATLAK — yazarken görülebilirdi:
  NOVUM TAŞIYICISI : amortisör bandı × kasa kaldırma jesti  (S4 · S8 · S12)
  ÜÇ KAPI ① TEK KARE: "S11 · 1:52 — yük yatağında yatan adam, dört boş
                       kelepçe yuvası"                       (BAŞKA BİR NESNE)
  → Kuralın kanıtı ile kuralın tek-kare testi AYNI NESNE DEĞİL.
    ONERME §4① geçmiş görünüyor, ama geçen şey novum değil DEKORDU.
```

⭐ **MEKANİZMA ÜÇ KATLI:**

```
① TAŞIYICI ÇOK KÜÇÜK. "İki parmak → bir el" bir el genişliğidir; 24mm'lik
   geniş kadrajda görünmez, 50mm insertte bile referanssız okunmaz.
② TAŞIYICI HAFIZA İSTİYOR. Değişim tek karede DEĞİL, 40 saniye arayla iki
   ayrı sahne arasında. İzleyici (ve mercek) ikisini yan yana koyamaz —
   koyabilmesi için filmin ona bunu yapmasını söylemesi gerekir; film
   söylemiyor.
③ AYNI PROMPTTA RAKİP OLAY VAR. S4/S8 promptları hem bandı hem "eldivenden
   düşen toz"u tarif ediyor. Model ikisinden TANIDIK olanı üretti: toz.
   İki mercek de tam olarak tozu yazdı, bandı değil. Bir promptta iki olay
   varsa model soyut olanı bırakır, somut olanı çizer.
```

**ÇÖZÜM — PLAN AŞAMASINDA, ÜÇ KURAL:**

```
① TEK KARE TESTİ NOVUMUN KENDİ TAŞIYICISIYLA KOŞULUR. ONERME §4①'e
   yazılan kare, §2'nin taşıyıcı nesnesini İÇERMEK ZORUNDADIR. Başka bir
   nesneyle geçilen kapı, geçilmemiş kapıdır.
② TAŞIYICI KADRAJIN EN AZ ONDA BİRİNİ KAPLAR ve değişimi TEK KLİP İÇİNDE
   olur. Sahneler arası değişim novum DEĞİL, sayaçtır — sayaç ikinci
   kanaldır, birinci kanal olamaz.
③ NOVUM SAHNESİNDE İKİNCİ OLAY YOKTUR. Kuralın kanıtlandığı klipte kadrajda
   başka hiçbir şey hareket etmez (D143'ün "zerreleri say" kuralının anlatı
   tarafı). Rakip olay varsa kural değil rakip üretilir.
```

⛔ **VE BİR KESME LİSTESİ TESTİ:** raporların kesme listesinde novumun
taşıyıcı sahnesi varsa, novum EKRANA GELMEMİŞTİR — listeyi tartışma, kareye
bak [D151]. Bu, D151'in tersinden okunuşudur ve daha erken uyarır: D151
"mercek vuruşu görmedi" der ve QA anında yakalar; bu ders "taşıyıcı
görünecek gibi tasarlanmamıştı" der ve PLAN anında yakalar.

> 🔗 Ders 151 (mercek vuruşu göremez/tersine okur — QA tarafı) · Ders 73
> (novum türetilmiş fenomene yüklendi, 0 kare çıktı — bu dersin atası) ·
> Ders 76 (yokluk novumu) · Ders 143 (rakip olay: sayısız toz cümlesi perdeye
> döner) · Ders 141 (vuruş ekranda mı) · ONERME_VE_NOVUM §2/§4/§5.

---

## 🔴 DERS 158: BEDEL ÖDENDİKTEN SONRA KAHRAMAN 12 SAHNE BOYUNCA HİÇBİR ŞEY SEÇMEDİ — VE PLAN BUNU TEMAYLA GEREKÇELENDİRMİŞTİ; TEMA, EDİLGENLİĞİN EN İYİ SAKLANDIĞI YERDİR

**Kaynak:** THE PAYLOAD QA (01.09.2026) — ④ HİKAYE 3,4/10: Karakter **2/10**,
Duygusal Yay **2/10**, `PEAK LOCATED AT: no peak located`, `THE ONE THING
NOTHING ELSE DOES: I could not find one`. Sahip değerlendirmesi (aynı gün):
*"filmin hikayesi berbattı bence."*
**Sorun:** planın kendi cümlesi savunmayı yazmıştı — *"Yanaşmayı makine yapar
ve bu TEMANIN kendisidir"* — ve o cümle, filmin ikinci yarısında insan
eyleminin sıfırlanmasını meşru gösterdi.

```
SAYIM (plandan, üretimden önce görülebilirdi):
  merkezi seçim              S7-S10   (dokuz kasayı çıkarmak)
  seçimden SONRAKİ sahne     13 adet  (S11-S23)
  bu 13 sahnede kahramanın BEDELLİ seçimi:      0
  bu 13 sahnede kahramanın herhangi bir eylemi: 3
     (S11 kayışı kilitler · S15 tüpe bakar · S22 avuçlarını açar)
  kahramanın hiç kadrajda olmadığı sahne:       6
→ filmin ikinci yarısı bir KODADIR ve koda 13 sahnedir; kodanın tamamı,
  gövdenin tamamı kadar uzun.
```

⭐ **MEKANİZMA — TEMA BİR ZIRHTIR VE EN ÇOK YAZARI KORUR.** "Kahraman
edilgen çünkü tema edilgenlik hakkında" cümlesi her zaman kurulabilir ve
her zaman doğru görünür. Ama izleyici temayı okumaz, EYLEMİ okur: bir insan
uzanıp beklerken makine çalışıyorsa, ekranda görünen şey "insan-makine
sınırı" değil, **bahis yokluğudur**. ④ merceğin "lack of stakes and
friction" cümlesi tam olarak bunu ölçtü — ve mod V olduğu için bunu
tasarımın bir sonucu olarak değil, bir kusur olarak yazdı. Haklıydı.

⛔ **VE İKİNCİ EKSİK, BİRİNCİYİ BÜYÜTÜYOR: BAŞARISIZ DENEME YOK.** Aynı
raftaki THE FROST LINE'ın omurgası bir başarısızlıktır (dış yama bir
saniyede uçar, S5) — plan onu "ultra gerçekçilik kanıtı" diye yazar ve
film oradan enerji alır. THE PAYLOAD'ın 24 sahnesinde kahramanın denediği
ve TUTMAYAN tek bir şey yoktur: karar verir, uygular, kalkar, kenetlenir.
Sürtünmesiz bir plan, kusursuz üretilse bile sürtünmesiz bir film verir.

**ÇÖZÜM — PLAN KONTROL LİSTESİNE İKİ SAYIM (03_PLAN_ONCESI B2'nin altına):**

```
B2a  MERKEZİ SEÇİMDEN SONRAKİ SEÇİM SAYISI: ___
     0 ise ikinci yarı kodadır. Koda 3-5 sahneyi geçiyorsa ya bir seçim
     eklenir ya sahne sayısı düşer. Tema gerekçesi bu maddeyi KAPATMAZ —
     gerekçe yazılır, sayım yine yazılır.
B2b  BAŞARISIZ DENEME SAYISI: ___  (kahramanın yaptığı ve TUTMAYAN şey)
     0 ise filmde sürtünme yoktur. En ucuz çözüm, mevcut bir sahneyi
     ikiye bölmek değil, mevcut bir eylemi BİR KEZ BAŞARISIZ KILMAKTIR.
```

⚠️ **BU DERS "TEMAYI ZAYIFLAT" DEMİYOR.** Edilgenlik temanın kendisi
olabilir — ama o zaman edilgenlik BİR SEÇİMLE kurulur: kahraman
müdahale edebileceği bir anda müdahale ETMEMEYİ seçer ve bunu ekranda
görürüz. Seçilmemiş edilgenlik tema değil, boşluktur.

> 🔗 Ders 141 (vuruş ekranda mı — bu ders "vuruş PLANDA mı?" diye sorar) ·
> B2 bedelli seçim maddesi (03_PLAN_ONCESI) · Ders 134 (belgesiz merceğin
> sıralaması) · KARAKTER_VE_DUYGU §6 (tepki planı bütçesi — bu filmde bütçe
> DOLUYDU ve yetmedi: tepki seçim değildir).

---

## 🔴 DERS 172: TAŞIYICIYI ASAN KORDON, FİLMİN MEKANİZMASI SANILDI — RAKİP OLAY DEĞİL, TAŞIYICININ KENDİ ASKI DÜZENEĞİ NOVUM'UN YERİNE GEÇTİ

**KAPI:** ⬜ AÇIK — plan tarafı. `03_PLAN_ONCESI` ⑩'a "TAŞIYICININ ASKISI
ERİŞİLEBİLİR Mİ?" maddesi gerekiyor.
**TEKRAR:** 0 · 02.09.2026 THE LEANING ROOM

**Kaynak:** THE LEANING ROOM QA (02.09.2026) — sekiz merceğin **SEKİZİ** filmi
aynı cümleyle özetledi ve cümle filmin cümlesi değildi:

```
④ HİKAYE, "THE FILM IN ONE SENTENCE (as a first-time viewer would say it)":
   "A woman ... PULLS ROPES and turns dials to shift the cosmos outside
    her window."

⑦ AKSİYON, altı vuruşun dördü:  B1 "pulls a hanging rope" · B2 "pulls the
   rope again" · B5 "pushes the hanging lamp" · B6 "presses the stones"
⑧ EFOR, dört efor olayının ikisi:  "pulling thick hanging rope downward"
⑥ FİZİK, L1: "rope pull · low tension"   ② ⑤ ①: "rope clips through the
   brass lamp housing"

PLANDA HALAT YOKTUR. Filmde çekilen bir halat yoktur.
Olan şey: SARKAÇ LAMBAYI TAVANA ASAN ÖRGÜ KORDON.
```

⭐ **MEKANİZMA — ASKI DÜZENEĞİ BOŞ BİR EYLEM YUVASIDIR VE MODEL ONU DOLDURUR.**
Prompt kordonu üç kez tarif etti ve üçünde de yalnız NE OLDUĞUNU söyledi
("braided cord", "taut and perfectly straight"), hiçbirinde NE OLMADIĞINI ve
KİMİN ERİŞEMEYECEĞİNİ söylemedi. Kadrajda aynı anda bir KONSOL ve bir EL vardı.
Model üçünü birleştirdi:

```
S3 · 0:35  kordon lambada BİTMİYOR — konsola kadar iniyor, ucu kadının elinde
S5 · 0:55  aynı, çapraz ve gevşek — "çekme halatı" okuması pekişiyor
S8 · 1:25  kordona PİRİNÇ KARŞI AĞIRLIKLAR takılmış — model mekanizmayı
           tamamlamış: artık bu bir kaldıraç düzeneği
```

Ve zincir kapanıyor: kordon bir kumanda olunca, **novum bir kurala değil bir
KUMANDAYA dönüşüyor.** ⑦ AKSİYON'un sorusu tam olarak bunu söylüyor: *"why
does a stone drop cause an eclipse, but a rope pull summons Saturn?"* — mercek
filmin fiziğini değil, filmin hiç var olmayan arayüzünü sorguluyor.

⛔ **BU D157 DEĞİL, D157'NİN AKRABASI.** D157'de kadrajda RAKİP BİR OLAY vardı
(banda karşı eldivenden düşen toz) ve model tanıdık olanı üretti. Burada rakip
olay yok: **rakip, taşıyıcının kendi askısı.** Novum'un var olabilmesi için
gereken parça, novum'un yerine geçti. Bu yüzden "novum sahnesinde ikinci olay
yoktur" kuralı bu arızayı yakalamaz — ikinci olay yok, ikinci NESNE de yok;
olan tek şey birinci nesnenin üst yarısı.

**ÇÖZÜM — ÜÇ SATIR:**

```
① ASKI NEREDE BİTTİĞİNİ SÖYLER, HER PROMPTTA.
   ✗ "a heavy brass pendant lamp hangs from a ceiling rail on a braided cord"
   ✓ "a heavy brass pendant lamp hangs on a braided cord that runs from the
      lamp straight up to the ceiling rail and ends there; nothing else hangs
      from it, nothing is attached to it, and it carries no weights, no
      handle and no loop"

② ERİŞİLEMEZLİK YAZILIR — ve ELİN NEREDE OLDUĞU SÖYLENİR.
   "the cord stays out of her reach at all times; her hands are on the table
    and never come near it"
   Kadrajda aynı anda bir kumanda varsa bu cümle ZORUNLUDUR.

③ PLAN KONTROLÜNE MADDE: TAŞIYICININ ASKISI.
   "Taşıyıcı neyle duruyor? O askı kadrajda görünüyor mu? Karakterin eli ona
    değebilir mi? Değebiliyorsa model onu bir kumandaya çevirir."
   ⛔ Sarkan her şey — kordon, kayış, halat, zincir, kablo, kolon — bu
     maddeye girer. Sarkmak, çekilmeyi davet eder.
```

⚠️ **VE MALİYETİ ÖLÇÜLDÜ:** bu filmde novum EKRANA GELDİ (lamba yattı, oda
yattı, bedel ödendi, iki ezik finalde sayılabilir hâlde duruyor) ve buna
rağmen sekiz merceğin sekizi filmi başka bir film sandı. **Görünen novum,
yanında daha tanıdık bir mekanizma varsa okunmaz.**

> 🔗 Ders 157 (rakip OLAY) · Ders 151 (mercek vuruşu göremez) · Ders 73
> (taşıyıcı türetilmiş fenomen) · Ders 174 (aynı filmde yönün yuvarlanması) ·
> ONERME_VE_NOVUM §2 (A nesnesi × B jesti)
