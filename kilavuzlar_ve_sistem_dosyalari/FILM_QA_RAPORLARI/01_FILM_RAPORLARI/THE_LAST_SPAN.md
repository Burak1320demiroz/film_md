# 🧱 THE LAST SPAN — FİLM QA KAYDI  ⏸️ FİLMİ KALDIRILDI

> ## ⏸️ DURUM: FİLM DEPODAN KALDIRILDI (26.08.2026 · kart H2)
>
> Depo yalnız UZAY filmlerine indirildi; zombi türü kaldırıldı ve bu filmin
> dosyaları depodan çıktı. **Bu kayıt ve ham raporları KASITLI OLARAK
> DURUYOR** — AGENTS kural ④: "Bu depoda 11 filmin ham raporu bir kez
> kayboldu. Tekrarlatma."
>
> **Neden korunuyor:** Bu, depoda 6 merceğin birden koşulduğu ender
> partilerden biri. Deponun bir numaralı açığı ÖLÇÜM DURMUŞ (AGENTS §6);
> bu partinin ölçüm verisi ve KAPI DAVRANIŞI (ön koşu etiketleri, çapraz
> sayım, ölçüm kapısı) türden bağımsızdır ve uzay filmleri için geçerlidir.
>
> **Nasıl kullanılır:** Bu satırdan sonrası bir METODOLOJİ kaydıdır, bir
> film kaydı değil. Skorlar zaten TABLOYA YAZILMADI (hepsi ön koşu) ve
> yazılmayacak. ⛔ Bu kayıttan yeni bir T satırı ÜRETİLMEZ, tamlık
> matrisine girmez, kıyas tabanı sayılmaz.
>
> **Film dosyasının arşivi:** depo dışında
> `film_md_ZOMBI_ARSIV_2026-08-26.tar.gz` (git geçmişinde YOK — dosyalar
> hiç commit'lenmemişti).

> **Film:** ⏸️ kaldırıldı — eski yol
> `yatay_2_4_dk_filmler_zombi/THE_LAST_SPAN/THE_LAST_SPAN_VIADUCT_FILM.md`
> **SPEC:** ⏸️ kaldırıldı (aynı klasörde `THE_LAST_SPAN_QA_SPEC.md` idi) [D117]
> **Parti:** 25.08.2026 · 6 genel mercek + 1 filme özel kapı, aynı 114 s kurgu
> **Ham raporlar:** `../02_HAM_RAPORLAR/THE_LAST_SPAN_*.md` (7 dosya) — DURUYOR
> **Filme özel rubrik:** ⏸️ kaldırıldı; türden bağımsız yarısı
> `../../QA_PROMPTLARI/FILME_OZEL/00_YANLIS_POZITIF_DUVARI_SABLONU.md`
> dosyasına damıtıldı ve uzay hattına uyarlandı

---

# 🚨 ÜST BLOK — BU PARTİNİN DURUMU

```
① 🔧 KARE        ⛔ ÖN KOŞU · Ⓥ 5.0   → TABLOYA YAZILMADI
② 🔗 DEVAMLILIK  ⛔ ÖN KOŞU · Ⓥ 6.8   → TABLOYA YAZILMADI
③ 🔊 SES         ⛔ ÖN KOŞU · Ⓥ 6.5   → TABLOYA YAZILMADI
④ 📖 HİKAYE      ⛔ ÖN KOŞU · Ⓥ 6.1   → TABLOYA YAZILMADI
⑤ 🖼️ ARKA PLAN   ⛔ ÖN KOŞU · Ⓥ 5.2   → TABLOYA YAZILMADI
⑥ ⚖️ FİZİK       ⛔ ÖN KOŞU · Ⓥ 5.7   → TABLOYA YAZILMADI
🧱 ÖNERME KAPISI ✅ GEÇERLİ · KARAR: REGENERATE
📏 ⑪ ÖLÇÜM KAPISI ✅ KOŞULDU — üç fabrikasyon yakaladı (§ÖLÇÜM KAPISI)

00_INDEX tamlık matrisi: 0/4 — DEĞİŞMEDİ.
```

⛔ **ALTI MERCEĞİN ALTISI DA ÖN KOŞUDUR.** Sebep tek bir kapı değil, üç
bağımsız kapı: kurgu kapısı 3/3 ihlal (④), SPEC hazırken mod V (①), ve
oturum bulaşması (⑤). Ayrıntı aşağıda.

⭐ **Buna rağmen partinin bir GEÇERLİ çıktısı var** ve o da kararı veriyor:
filme özel ÖNERME KAPISI. O bir mercek değil KAPIDIR — çıktısı skor değil
karardır, A bloğu ikili (PASS/FAIL) ve her satırı alıntılı kanıt taşır.
Bulanmış bir oturum bile bir formun emeklediğini görebilir.

---

# 📏 ⑪ ÖLÇÜM KAPISI [DERS 125] — ⛔ EN BAŞTA KOŞAR

> Master: `~/Downloads/the last stand.mp4` · ölçüm 25.08.2026 · ffprobe/ffmpeg
> ⛔ ④ ⑤ ⑦ ⑨ kapıları BU sayılarla koşar, raporun sayılarıyla değil.

```
SÜRE            115.055 s   (raporların hepsi "114 s measured" dedi)
ÇÖZÜNÜRLÜK      1280 × 720  ⛔ İHRAÇ STANDARDININ ALTINDA
                            (KURGU_RITMI §6: 1440p+)
KARE HIZI       30 fps      ⛔ ALTI RAPORUN ALTISI DA 24 fps VARSAYDI

KESME IZGARASI (scene>0.3):
  10.03 · 20.03 · 50.03 · 60.03 · 70.07 · 80.07 · 90.07 · 100.07 · 110.07
  + ızgara dışı: 70.60 · 93.40 · 105.80

  ⭐ 30 ve 40'ta algılama YOK — ardışık iki tavan-geçişi sahnesi birbirine
     çok benziyor, eşiği tetiklemiyor. Izgara yine de 10,0 s'lik.

SESSİZLİK (-50 dB, ≥0,3 s):
  ⛔ HİÇ YOK — dosyanın hiçbir yerinde 0,3 saniyelik sessizlik dahi yok.
```

## 🚨 ÖLÇÜM ÜÇ FABRİKASYON YAKALADI

```
① ③ SES'İN İKİ 🔴 BLOCKER'I UYDURMA
   Rapor: "0:19 ve 0:50'de MUTLAK DİJİTAL SESSİZLİK · BLOCKER ×2"
   Ölçüm: dosyada hiç sessizlik yok.
   → İki blocker DÜŞER. Ambiyans Devamlılığı 5/10 skorunu SÜREN buydu;
     skor geçersiz. ⛔ Rubriğin KENDİ kuralı bunu zaten yasaklıyordu
     ("never a 🔴 BLOCKER ... an operator can check in ten seconds with
     a meter"). D125'in birebir tekrarı.

② RAPORLARIN KESME LİSTESİ YANLIŞ — ve altısı da AYNI yanlışı verdi
   Rapor:  10 · 19 · 29 · 39 · 50 · 59 · 70 · 78 · 93 · 100
   Ölçüm:  10 · 20 · 30 · 40 · 50 · 60 · 70 · 80 · 90 · 100 · 110
   → ⑤ ÇAPRAZ SAYIM KAPISI "altısı da 10 dedi, uyuşuyor ✅" verdi.
     Uyuşan şey ÖLÇÜM değil, ortak hataydı. D125 tam bu.

③ ⑥ FİZİK'İN BÜTÜN SÜRELERİ YANLIŞ ORANDA
   Rapor "FRAME RATE ASSUMED: 24 fps" yazdı; dosya 30 fps.
   Ledger'daki her süre ve ondan türetilen her g değeri bu oranı taşıyor.
   → GRAVITY TABLE kullanılamaz. TWO GRAVITIES verdikti YÖN olarak
     ayakta kalabilir (iki farklı düşüş süresi ölçülmüş) ama SAYILARI
     yeniden ölçülmeden hiçbir karara girmez.
```

## ✅ ÖLÇÜM BİR BULGUMU DA DÜŞÜRDÜ — dürüst kayıt

```
Raporların zaman kodlarından "değişken klip uzunluğu (7-15 s) → D100
kırpma bütçesi ihlali" diye bir bulgu çıkarmıştım. ÖLÇÜM BUNU ÇÜRÜTÜYOR:
kurgu temiz 10,0 s ızgarasında. Değişkenlik raporların göz kararı zaman
kodlarındaydı, kurguda değil.
⛔ Bulgu GERİ ÇEKİLDİ. Aynı hatayı ben de yaptım: modelin sayısını kapıya
   girdi olarak kullandım. Kapı ⑪ tam olarak bunun için var.
```

## ⭐ ÖLÇÜMÜN AÇTIĞI YENİ BULGU — sahne içi süreksizlik

```
Izgaraya oturmayan üç algılama, üç ayrı sahnenin İÇİNDE:
  70,60 s  → sahne 7'nin içinde, +0,6 s
  93,40 s  → sahne 9'un içinde, +3,4 s
  105,80 s → sahne 10'un içinde, +5,8 s

Plan: "12 sahnenin 12'si single unbroken take · 0 kesme".
→ ÜÇ SAHNEDE GİZLİ KESME / SERT İÇERİK SIÇRAMASI. 🔴
⭐ ① KARE 1:28'de bir gizli kesme bildirmişti (≈88 s); ölçüm 93,40 diyor.
   Bulgusu DOĞRU, yeri yanlıştı — ölçümle yeri düzeltildi ve iki tane
   daha ortaya çıktı.
```

---

# ⛔ ORTAK ADIMLAR — kapı kapı [AGENTS §3 C/D/E/E3/F/F2 ortak bloğu]

## ③ KİMLİK KAPISI [D105] — ①'den ÖNCE

```
GEREKEN: metin olmayan EN AZ İKİ çapa (bir vuruş/sahne + bir sayısal kilit)

ÇAPA 1 — VURUŞ    ✅ TUTTU
  Tıkalı viyadük · araç tavanlarında ilerleyen tek kadın · elinde bidon ·
  araçların arasında ayakta duran tozlu figürler. Depoda başka hiçbir
  filmde bu konfigürasyon yok.

ÇAPA 2 — SAYISAL  ❌ TUTMADI — VE BULGU BUDUR
  Denenen kilitlerin hiçbiri ekranda doğrulanmadı:
  devrilme 1,1 s → hiç yasal devrilme yok (B1 NOT EXERCISED)
  zincir 4,0/5,0 m/s → hiç zincir yok (B2 NOT EXERCISED)
  toz 0,7×0,5 m / 3 s → 3,0 m yayılıyor, 5 s asılı (B4 FAIL)
  12 klip / 120 s → 11 klip / 114 s (B10 FAIL)
  tulum tuğla kırmızısı → TURUNCU
  ekran metni 0,0 s → 1:50-1:54 başlık kartı (B12 FAIL)

KARAR: koşu UNATTRIBUTED SAYILMAZ — vuruş çapası tek başına çok güçlü ve
       kapının ikinci yarısındaki başarısızlık ATFIN değil FİLMİN
       başarısızlığıdır. Ama kayda geçer:
       ⛔ BU MALZEME FİLMİN KONSEPTİNİ TAŞIYOR, SAYILARINI TAŞIMIYOR.

⛔ EKRANDAKİ YAZI ÇAPA DEĞİLDİR — ve bu partide İKİ rapor onu çapa yaptı:
   ④ HİKAYE `FILM: THE LAST STAND` yazdı, ⑤ ARKA PLAN aynısını.
   Kaynak 1:50'deki yanan başlık kartıdır ve iki rubriğin de kendi
   gövdesinde bu YASAKTIR. → **D105/D65 TEKRARI** (24.08 Borrowed Weight
   partisinde ④ aynı hatayı yapmıştı; bir gün sonra iki rubrikte tekrar).
   ✅ ① KARE ve ② DEVAMLILIK doğru davrandı: `FILM: (not supplied)`.
   ⚠️ ③ ve ⑥ dosya adını yazdı (`the last stand.mp4`) — bu bir kart değil
      dosya adıdır, yasak değil ama film adı da değildir.
```

## ④ KURGU KAPISI KAPISI [D109 · D101 · D118] — ⛔ 3/3 İHLAL

```
⛔ BU KAPI ⑪'İN ÖLÇÜLEN SAYILARIYLA KOŞULDU, RAPORLARINKİYLE DEĞİL.

ÖNCE AYIKLA, SONRA SAY [D93]:
  başlık kartı 110,07 → 115,055 s = 4,99 s → 🔴 loglandı, sayım DIŞINDA
  sahne malzemesi = 110,07 s

a) KLİP SAYISI   plan 12  ·  ölçülen 110,07 ÷ 10,0 = 11,01 → 11   ❌  (−1)
b) SÜRE          plan 120 s ±2  ·  ölçülen 110,07 s            ❌  (−9,93 s)
c) İNSAN ŞERİDİ  [D118]                        ❌
     PLAN:   -11111111111   (12 hane · S0 İNSANSIZ hook)
     KURGU:  11111111111    (11 hane · insansız sahne YOK)
     → hem BİR SAHNE EKSİK hem de S0'ın insansızlığı ihlal edilmiş.

⛔ ÜÇÜ DE TUTMADI → koşu ÖN KOŞU. Sonucu:
   · skor satırları ⚠️ ŞARTLI bile olsa T1-T6'ya GİRMEZ
   · film boyuna bakan kategoriler SAYI TAŞIMAZ
     (Yapı · Duygu Yayı · Final · Tutundurma · Ortam Devamlılığı ·
      Kimlik Sürekliliği · Kalabalık Sayımı · Ufuk)
   · ⛔ KESME LİSTELERİ VE YENİDEN ÜRETİM REÇETELERİ UYGULANMAZ
```

### 🧮 IZGARA GERİ ALMA [D115] — ÖLÇÜLEN ızgara

```
Plan ızgarası:    n × 10 s · 12 dilim × 10,0 s = 120 s
Ölçülen ızgara:   n × 10 s · 11 dilim × 10,0 s = 110,07 s  + 4,99 s kart

⭐ IZGARA TEMİZ. Kurgu 10,0 saniyelik dilimlerde ve kırpma yapılmamış —
   plan bu yönden TUTUYOR. Eksik olan tek şey BİR DİLİM.

⛔ Raporların sahne haritası kullanılmaz: zaman kodları göz kararıydı
   ve altısı da aynı ~1 s'lik kaymayı taşıyor (§ÖLÇÜM KAPISI ②).
```

### 🔍 SAHNE EŞLEMESİ — hangi sahne yok

```
PLANDA VAR, KURGUDA YOK:
  ⛔ S0   HOOK · İNSANSIZ — ayna düşer, 4 form devrilir, zincir 1,2 m
          boşlukta durur. FİLMİN KURALINI ÖĞRETEN TEK SAHNE.
  ⛔ S4   30 formluk kendiliğinden zincir (4,0 m/s, 7 s) — mekanik ölçekte
  ⛔ S8   Kovalamaca: omuz teması → arkada zincir
  ⛔ S9   🎯 DORUK — bidonun fırlatılması, 400 formun bariyere katlanması
          (CENTRAL CHOICE · plan §0.5 Çehov 1'in ödemesi)

KURGUDA VAR, PLANDA YOK:
  0:59-1:10  "Mercedes bagajına tırmanma"
  1:10-1:18  "bagajdan inme"

⛔ DORUK KURGUYA GİRMEDİ — D101/D72 zincirinin ÜÇÜNCÜ VAKASI
   (Unbroken City: doruk kurguya girmedi · Last Shift: 10 klip girmedi ·
    Last Span: doruk + hook + mekanik sahnesi girmedi).
   ⭐ ④ HİKAYE bunu bilmeden birebir bildirdi: "1:40 — No character choice —
      the climax happens around her, not because of her". Rapor OLMAYAN bir
      doruğu eleştirdi; bulgu bu yüzden hikâye yargısı olarak DÜŞER ve
      eksik sahnenin KANITI olarak ayakta kalır.
```

## ⑤ ÇAPRAZ SAYIM KAPISI [D107] — sayılar tuttu, KOŞULAR TUTMADI

```
Kesme sayısı:  ① 10 · ② 10 · ③ 10 · ④ 10 · ⑤ 10 · ⑥ 10 · kapı 10
Sahne sayısı:  altısı da 11
fark = 0  →  ⑤ kapısı biçimsel olarak GEÇTİ

⛔ AMA D110 BUNU DOĞRULAMA OLMAKTAN ÇIKARIYOR — üç bulaşma izi:
  ① ⑥ FİZİK raporu `BASELINE: THE FILM AS SCREENED / This review answers
     "does this film work for a viewer who knows nothing about it?"`
     yazdı. Bu ④ HİKAYE'nin mod-V damgasıdır. ⑥'nin kendi damgası bir
     GRAVITY ESTIMATE satırıdır ve o da var — yani İKİ rubriğin başlığını
     birden taşıyor.
  ② ⑤ ARKA PLAN raporu `STORY TRACKING ROW` bastı — ④'ün 10 sütunlu
     satır formatı, `⚠️ ŞARTLI` işaretiyle. ⑤'in rubriğinde böyle bir
     satır YOKTUR ve ⑤'in 9 kategorisiyle sütunları tutmuyor.
  ③ ⑤ ayrıca `INPUT MODE: V`, `MATERIAL TYPE`, `LENGTH CLASS` yazdı —
     üçü de ⑤'in rubriğinde bulunmayan alanlar.
  + Altı raporun onar zaman kodu BİREBİR aynı dize.

KARAR: en az ⑤ ve ⑥ ④'ün çıktısını gören bir oturumda koştu.
       "Altı mercek aynı şeyi gördü" bir DOĞRULAMA DEĞİL, tek raporun
       altı kopyasıdır [D110]. ⑤ kapısının geçmesi bu partide bir şey
       kanıtlamaz.

⛔ VE ÖLÇÜM BUNU KANITLADI: altı raporun ortak kesme listesi ÖLÇÜLEN
   ızgarayla tutmuyor (10·19·29·39·50·59·70·78·93·100 ↔ gerçek
   10·20·30·40·50·60·70·80·90·100·110). Altısı da AYNI yanlışı taşıyor.
   ⑤ kapısı "uyuşma" görüp ✅ verdi; uyuşan şey ölçüm değil ORTAK HATAYDI.
   → D125'in ikinci vakası, aynı hafta.
```

## ⑩ ÖNERME KAPISI [D87 · D116] — her bulgu plana karşı okundu

| Bulgu | Kaynağı planda YAZILI mı? | Karar |
|---|---|---|
| İki yerçekimi (2,3 ↔ 4,6 m/s²) | ❌ plan 1,0 g · gerçek zaman · ağır çekim 0 kare | **AYAKTA** — kilit FAIL |
| Ağır çekim sıçrama (0:30) | ❌ "no slow motion, no speed ramp" | **AYAKTA** — kilit FAIL |
| Kalabalık 0:59'da yok oluyor | ⚠️ plan son 30 m'yi ARAÇSIZ yazar — ama 120 m'lik kalabalığı değil | **AYAKTA** (kısmi) |
| Ufuk çöl → yeşil ağaç + kasaba | ❌ plan: kuru gri çakıl vadi · "ANIMALS · PLANTS 0 frames" | **AYAKTA** — kilit FAIL |
| Tulum tozu 1:18'de sıfırlanıyor | ❌ plan: yıpranma MONOTONİK, S7'den sonra ARTAR ve azalmaz | **AYAKTA** — kilit FAIL |
| Eldivenler S6'da yok, S7'de dönüyor | ❌ plan: siyah deri eldiven 12/12 sahne | **AYAKTA** |
| Bidon 1:18'de kayboluyor | ⚠️ plan bidonun eli terk etmesini İSTER — ama S9'da FIRLATILARAK | **YENİDEN SINIFLANDI:** devamlılık kusuru değil, **eksik doruğun izi** |
| Kamera kaydırma/push (0:29, 1:18) | ❌ plan: 12/12 sabit lockoff | **AYAKTA** — kilit FAIL |
| Formlar emekliyor / belden bükülüyor / kalkıyor | ❌ KAPALI HAREKET LİSTESİ: durma · rijit devrilme · ≤4 cm salınım | **AYAKTA — FİLMİN ÖLÜMÜ** |
| Formlar toza dönüşerek dağılıyor | ❌ plan: devrilir ve YERDE KALIR; dağılma yok | **AYAKTA — PREMİS DEĞİŞMİŞ** |
| "Tehdit yok / pasif antagonist" | ✅ **PLANIN ÖNERMESİ** — yanlış-pozitif duvarı §1 | ⛔ **DÜŞER** |
| "Sessiz kalabalık / ambiyans boş" | ✅ plan: figür sesi 0 kare | ⛔ **DÜŞER** |
| "Yüzler görünmüyor" | ✅ plan: figür yüzü 0 kare | ⛔ **DÜŞER** |
| "Kansız korku / darbelerin sonucu yok" | ✅ plan: gore bütçesi 0 | ⛔ **DÜŞER** |
| "Repliksiz, karakteri tanımıyoruz" | ✅ plan: 0 replik, 12/12 sessiz | ⛔ **DÜŞER** |
| ④'ün "0:19-0:50 gereksiz geçiş sahneleri" | ⚠️ plan: S1·S2·S3·S5 dördü de FARKLI bilgi taşır | **SEBEP EKSİK S4** — bulgu gerçek, teşhisi yanlış |

```
⛔ ④ HİKAYE'nin KESME LİSTESİ AYRICA ENGELLİ:
   Listenin 1. sırası "S4 (0:29-0:39) — jumping beat" = planın S3'ü =
   ⭐ VİRAL ARA · "BUNLAR KESİLEMEZ" [SPEC A bloğu].
   Ön koşu zaten kesme listesini uygulatmıyor; bu ikinci kilit.
```

---

# 🔑 BİRLEŞTİRİLMİŞ BULGU — hiçbir merceğin tek başına söylemediği şey

```
⛔ ÜRETİLEN FİLM, YAZILAN FİLM DEĞİL. Konumunu paylaşıyor, mekaniğini değil.
```

Kanıt tek bir satırda duruyor — ÖNERME KAPISI'nın C1'i, izleyicinin
kuralı kendi cümlesiyle ifade etmesini isteyip sonra karşılaştırıyor:

```
İZLEYİCİNİN OKUDUĞU KURAL:
  "Dünya taşlaşmış, kül figürler kendiliğinden toza dönüşüyor ve bir kadın
   aralarında yürüyor."

YAZILAN KURAL:
  "Kendi başlarına harekete geçemezler; tek temas devirir; devrilen bir
   daha kalkmaz."
```

Bunlar iki farklı film. Birincisi **ÇÜRÜME** filmi, ikincisi **DOMİNO**
filmi. Çürüme filminde kadının ağırlığı hiçbir şey ifade etmez; domino
filminde tek şey odur.

```
FİLMİN NOVUM'U EKRANDA 0 KARE:
  · hiçbir form bir temas yüzünden devrilmiyor
  · hiçbir zincir yok — B1, B2, B3 üçü de NOT EXERCISED
  · doruk (bidonun fırlatılması) kurguda YOK
  · hook (kuralı öğreten S0) kurguda YOK
  → C1 = 1/10 · C3 = 2/10 · C4 = 1/10
```

⭐ **Ve bu, altı genel merceğin neden 5.0-6.8 arası "orta" skorlar
verdiğini açıklıyor:** hepsi tutarlı, hoş görünen bir filmi ölçtüler.
Ölçmedikleri şey, o filmin YANLIŞ FİLM olduğuydu. Genel mercek bunu
göremez ve görmesi de beklenmez — bu tam olarak filme özel kapının
`QA_PROMPTLARI/00_README.md` derin tarama bölümünde yazılı varlık
sebebidir.

## 🧪 MEKANİZMA HİPOTEZİ — neden domino değil çürüme çıktı

```
⚠️ HİPOTEZ, KANIT DEĞİL — operatörün doğrulaması gerekiyor (aşağıda soru).

25.08 sabahı D123 düzeltmesi (yasak sözlüğü → pozitif malzeme tarifi)
formları şöyle tanımladı:
  "sealed head to foot under a single unbroken coat of pale grey dust ...
   the head is a smooth dust shell with no readable features, like a
   plaster cast left standing in the open"

⛔ Bu metafor bir FİZİKSEL ÖZELLİK taşıyor: alçı döküm KIRILGANDIR.
   Devrilmez, DAĞILIR. Ve ⑥ FİZİK'in PREMISE REGISTER'ı modelin okumasını
   birebir yazıyor:
     "Human bodies have petrified into brittle, dry ash/dust structures
      that hold their shape until collapsing."
   Model "dust shell"i gövdenin ÖRTÜSÜ değil MALZEMESİ okudu.

Domino cümlesi promptta duruyordu ama malzeme tarifi onu ezdi.
→ D123 doğru sorunu çözdü (politika reddi) ve yeni bir sorun açtı:
  politika güvenliği için seçilen metafor mekaniği yeniden yazdı.
→ DERS ADAYI D128 (aşağıda).
```

---

# 📋 KİLİT ÇELİŞKİSİ DEFTERİ [D96]

| # | Rapor ne dedi (tc) | Hangi kilit | Çözüm eylemi | Sonuç |
|---|---|---|---|---|
| 1 | formlar emekliyor, belden bükülüyor, kalkıyor (0:03-0:07) | KAPALI HAREKET LİSTESİ §0.12 | master 0:00-0:10 izlenir | ⬜ AÇIK |
| 2 | form başını çeviriyor, kadını izliyor (1:34) | "no head turns · none turns to her" | master 1:33-1:40 izlenir | ⬜ AÇIK |
| 3 | formlar toza dağılıyor (1:41) | "settles there and remains part of the low line" | master 1:40-1:50 izlenir | ⬜ AÇIK |
| 4 | iki yerçekimi 2,3 ↔ 4,6 m/s² (0:50 vs 1:40) | YERÇEKİMİ 1,0 g · ağır çekim 0 kare | iki saniye kare kare ölçülür | ⬜ AÇIK |
| 5 | kamera kaydırıyor/push yapıyor (0:29, 1:18) | 12/12 sabit lockoff | master o iki saniye izlenir | ⬜ AÇIK |
| 6 | ufuk çöl → yeşil ağaç + kasaba (0:59) | kuru gri çakıl vadi · bitki 0 kare | master 0:55-1:05 izlenir | ⬜ AÇIK |
| 7 | ~~mutlak sessizlik 0:19 ve 0:50'de~~ | ③'ün KENDİ kuralı: emin değilsen 🔴 yazma | ✅ **ÖLÇÜLDÜ** — silencedetect −50 dB/0,3 s: dosyada hiç sessizlik yok | ✅ **RAPOR UYDURDU** |
| 8 | üç sahne içi süreksizlik (70,60 · 93,40 · 105,80) | "12/12 single unbroken take · 0 kesme" | ölçümle bulundu; master o üç saniye izlenir | ⬜ AÇIK |
| 9 | 1280×720 teslim | ihraç 1440p+ [KURGU_RITMI §6] | ölçüldü, tartışma yok | ✅ **FİLM SAPTI** |

⛔ **7 madde ⬜ AÇIK** (1-6 ve 8).
✅ **İki madde ÖLÇÜMLE KAPANDI:** 7 numara RAPOR UYDURDU, 9 numara FİLM SAPTI.
   Bu, ⑪ ölçüm kapısının ilk hasadıdır — modele sorulan iki soru bir
   komut satırında on saniyede cevaplandı. Açık madde varken: o merceğin skoru ŞARTLI,
bulgudan ders yazılmaz, yeniden üretim siparişi verilmez [D96].
⚠️ Madde 7 özel: ③ SES rubriğinin kendi gövdesi *"a stretch you are not
sure about is written 'level drops, floor uncertain' and goes to FLAGS —
never a 🔴 BLOCKER"* diyor. Rapor iki 🔴 BLOCKER yazdı. Metreyle
doğrulanmadan bu iki blocker'a göre iş yapılmaz.

---

# ✅ BU PARTİNİN İYİ HABERİ — 24.08 yamaları TUTTU

```
D119 SEVERITY ARİTMETİĞİ — 24.08'de ① KARE tally'sini kendi kütüğüyle
     uyumsuz yazmıştı ve verdict'i o yanlış sayı sürüyordu. Yeni
     SCORES SUMMARY ⑤ maddesi ("count the tally from the findings, not
     from memory") beş rubriğe kondu. Bu partide:
       ① 🔴5 🟠4  ↔ kütükte 5 🔴 + 4 🟠   ✅
       ② 🔴1 🟠3 🟡2 ↔ çelişki kütüğü aynı ✅
       ③ 🔴2 🟠2     ↔ iki log toplamı aynı ✅
       ⑤ 🔴3 🟠3 🟡3 ↔ çelişki kütüğü aynı ✅
       ⑥ 🔴1 🟠2 🟡1 ↔ çelişki kütüğü aynı ✅
     BEŞTE BEŞ. Yama ilk temasta tuttu.

D119 SKOR ARİTMETİĞİ — beş rubriğin aritmetik kapısı da tuttu:
       ① 35/7 = 5.0 ✅ · ② 75/11 = 6.8 ✅ · ③ 26/4 = 6.5 ✅
       ④ 55/9 = 6.1 ✅ · ⑤ 47/9 = 5.2 ✅
       ⚠️ ⑥ 46/8 = 5.75, rapor 5.7 yazdı — kesme, yuvarlama değil.
          0,05'lik sapma, maddi değil ama kayda geçer.

D113 YOKLUK ≠ EKSİKLİK — ①'in 24.08'deki hatası (sessiz filmde başlık
     kartıyla kategori düşürmek) bu partide tekrarlamadı: ① Diyalog-Ses'e
     N/A verdi, ③ beş diyalog kategorisine N/A verdi, ⑥ Balistik'e N/A.
     Hiçbiri 0 yazmadı. ✅

D93 SAHNE-DIŞI MALZEME — yedi raporun YEDİSİ de başlık kartını
     1:50-1:54 olarak ayrı satıra yazdı ve sayımdan düştü. ✅
```

---

# 🎯 KARAR VE SIRADAKİ ADIM

```
KARAR:  ⛔ REGENERATE — kaynağı ÖNERME KAPISI, A1 + A2 FAIL.
        Skor ortalamalarının bununla ilgisi yok ve olmamalı: premis
        ekranda yok, film yok.

⛔ NE YAPILMAZ:
   · ④'ün kesme listesi (ön koşu + viral ara kilidi)
   · ⑥'nın "S11'i %140 speed-ramp'le" önerisi — iki yerçekimini
     gizler, sebebini çözmez; ayrıca ağır çekim planda ZATEN yasak
   · ⑤'in "S7-S11'i yeniden üret" siparişi — doğru yönde ama eksik:
     sorun S7-S11 değil, S0/S4/S8/S9'un HİÇ olmaması
   · ①'in "REMOVE 'cinematic lighting'" reçetesi
     → ⛔ D85 GREP KAPISI: dize depoda YOK (aşağıda doğrulandı) → DÜŞER

✅ NE YAPILIR — sırayla:
   1. ⛔ ÜRETİM KAPILARINA GERİ DÖN. §4.1 beş kapıyı sırayla ister ve
      KAPI 1 (S0 · rijit devrilme) bu kurguda FAIL. Kapı kaydı boş →
      kapılar ya koşulmadı ya kaydedilmedi [D74].
      Tek klip üret → ÖNERME KAPISI'nı MOD K ile koş → geçmeden devam etme.
   2. ⛔ PROMPT DÜZELTMESİ ÖNCE — D128 adayı (aşağıda). Malzeme metaforu
      mekaniği eziyor; kapı 1'i düzeltilmemiş promptla koşmak parayı
      ikinci kez yakar.
   3. Kilit çelişkisi defterinin 7 ⬜ maddesi master'da çözülür.
   4. QA yeniden koşulur — ⛔ HER MERCEK AYRI VE TEMİZ OTURUMDA [D110].
```

## 🔎 D85 GREP KAPISI — ①'in reçetesi doğrulandı

```
$ grep -rn "cinematic lighting" yatay_2_4_dk_filmler_zombi/
THE_LAST_SPAN_VIADUCT_FILM.md:1003:  "cinematic lighting" ifadesi yok [D33]

TEK İSABET VE O DA YASAĞIN İÇİNDE — LIGHTING BIBLE'ın yasak listesinde.
D85'in iki düşme sebebinden İKİNCİSİ: "çıktı yasağın içindeyse reçete
DÜŞER (çalışan yasağı silme önerisi)".

⛔ REÇETE DÜŞER — ve uygulansaydı filmin D33 yasağını SİLECEKTİ.
   Third Dune emsalinin birebir tekrarı ("REMOVE 'title card, cinematic
   poster'" önerisi filmin metin yasağını silecekti; dize depoda yalnız
   yasağın içinde vardı).
   ⭐ ① KARE promptu hiç görmedi: mod V'de göremez de. Bloom bulgusu
      (0:10) ayakta kalabilir; ÇÖZÜM ÖNERİSİ geçersizdir.
```

---

# ❓ OPERATÖRE SORULAR — cevaplanmadan ikinci tur başlamaz

```
1. ⛔ Bu kurgu V1 promptlarıyla mı V2 ile mi üretildi?
   D128 adayının tamamı buna bağlı: V2'nin "plaster cast / dust shell"
   metaforu mu çürümeyi getirdi, yoksa hata V1'de de var mıydı?

2. §4.1 üretim kapıları koşuldu mu? Kapı kaydı BOŞ. Koşulduysa KAPI 1
   (S0 rijit devrilme) nasıl geçti — yoksa geçen klip kurguya mı girmedi?

3. S0 · S4 · S8 · S9 üretildi mi? Üretilip kurguya girmediler mi, yoksa
   hiç üretilmediler mi? İkisi tamamen farklı iki problem.

4. Başlık kartı (1:50-1:54) kim ekledi? Plan 0,0 s ekran metni kilitliyor
   ve bu D70/D72 zincirinin 8. vakası.

5. Tulum neden TURUNCU? Plan tuğla kırmızısı ve "tek kırmızı" bir
   izleme cihazı. Turuncu tasarım kararı mı, model sapması mı?

6. 0:19 ve 0:50'deki sessizlik gerçekten MUTLAK mı? Metreyle 10 saniyede
   bakılır ve iki 🔴 BLOCKER buna bağlı.
```
