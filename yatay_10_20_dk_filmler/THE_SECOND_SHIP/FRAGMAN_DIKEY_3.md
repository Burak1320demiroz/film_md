# 🛰️ THE SECOND SHIP — ÜÇÜNCÜ DİKEY FRAGMAN

## 9:16 DİKEY · 6 vuruş × 10,000 s = 60,000 saniye · tek tırmanış
### **Mekanik: KUSUR YOK** — "burada bir şey var ve hiçbir şeyi yanlış yapmıyor"
### _"Kimse bir gemiyi bu kadar temiz vurmaz."_

> **Kaynak film:** `yatay_10_20_dk_filmler/THE_SECOND_SHIP/`
> 11 faz · 114 sahne · her sahne 10.000 s · 16:9
> Bible'lar: `README.md` · Çapa plakaları: `REFERANS_PAKETI.md` ·
> Sahne metinleri: `FAZ_*/FAZ_*.md` · Beste: `FRAGMAN.md` BÖLÜM 3
>
> **Kılavuz:** `kilavuzlar_ve_sistem_dosyalari/FRAGMAN_KILAVUZU.md` §2
> (shorts kartı · 6 vuruş şablonu) + §1.3b (aynı filme ikinci fragman)
> + §1.3c (kadraj kesişimi). Bu dosya o kartları uygular ve dokuz yerde
> bilinçle sapar; sapmaların hepsi §BİLİNÇLİ SAPMALAR'da yazılıdır.
>
> ⛔ Altı sahnenin on iki promptu da **self-contained**'dır
> (AGENTS.md kural ③). Hiçbiri "BIBLE'a bak" demez.
>
> ✅ **PROMPT KONTROL KAPISI (görev kartı P): GO** — 12 promptun 12'si
> betikten geçti (çıkış kodu 0 · 0 BLOCK · 0 FIX). Video promptları
> 2.318–2.570 karakter, yani bandın (2.000–2.600) içinde; image
> promptları 3.095–3.950 ve betik image uzunluğunu "karar bekliyor"
> olarak işaretler, bulgu saymaz (sapma ⑤). **Üretime girmeden önce
> betiği tekrar koş — sayıları o hesaplar, bu dosyaya elle yazılmaz:**
> `python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_DIKEY_3.md`

---

## ⚠️ BU DOSYA İKİ KARDEŞİNİN YERİNE GEÇMEZ — ÜÇÜNCÜ TESLİMDİR

Aynı filmin dört fragman teslimi var. Dördü dört ayrı iş yapar:

| | `FRAGMAN.md` BÖLÜM 1 | `FRAGMAN_DIKEY_2.md` | `FRAGMAN_PRO_YATAY.md` | **bu dosya** |
|---|---|---|---|---|
| Format | 9:16 · 60 s | 9:16 · 60 s | 16:9 · 120 s | **9:16 · 60 s** |
| Tür | teaser | teaser | trailer | **teaser** |
| Mekanik | **SAYIM** — kaç tane var | **CEVAP** — kim karşılık veriyor | 3+1 perde | **KUSUR YOK** — kim hata yapmıyor |
| Vuruş | 6 | 6 | 27 kesme | **6** |
| Yeni üretim | 6 klip | 6 klip | 0 klip | **6 klip** |
| Kadrajda Bekçi | 1 vuruşta (dönüş) | 2 vuruşta (parçalı) | 6 kesmede | **0 vuruşta — hiç** |
| Bıraktığı soru | *topraktan neden ikinci bir gemi büyüyor?* | *cevap veren kim — içi neden boş?* | ikisi birden | ***hiçbir şeyi yanlış yapmayan bir şey bir kargo gemisini neden vurdu — ve neden aynısını geri yapıyor?*** |

```
⛔ ÇAKIŞMA DENETİMİ ① — SAHNE (FRAGMAN_KILAVUZU §1.3b ②), sayısal:
   FRAGMAN.md dikey kesim  : S1 · S11+S12 · S21 · S28 · S35 · S40
   FRAGMAN_DIKEY_2.md      : S10 · S25 · S29 · S47 · S50 · S39
   FRAGMAN_OZEL_SAHNELER   : S29 · S34 · S11 · S35 · S38 (16:9 kadrajlar)
   BU DOSYA                : S13 · S14 · S32 · S37 · S49 · S51

   Kesişim (dikey 1): 0    Kesişim (dikey 2): 0    Kesişim (F1-F5): 0
   Ortak klip: 0. Üç dikey teaser aynı filme ÜÇ AYRI KAPI açar.
```

```
⛔ ÇAKIŞMA DENETİMİ ② — KADRAJ (FRAGMAN_KILAVUZU §1.3c):
   §1.3b ② sahne NUMARASINI sayar; izleyici ve model kadrajı görür.
   Bu yüzden lens + mesafe + özne sütunları yan yana okundu:

   vuruş  özne                        lens   mesafe  kardeş teslimdeki en yakın kadraj
   ─────  ──────────────────────────  ─────  ──────  ────────────────────────────────────
   K0     CANTOR gövde plakası+delik  50mm   5 m     yok (yatay C10 aynı sahne, 16:9)
   K1     Mühendis + delik, iç        50mm   3 m     yok — iki kardeşte de gemi içi 0 kare
   K2     taş iniş bacağı (2 m)       50mm   3 m     dikey1 S4: 31 m gemi, 32mm, geniş
   K3     taş gövde + eldivenli el    100mm  1,5 m   dikey2 D3: 100mm ama özne ZEMİN
   K4     400 m kule + sınır + figür  32mm   25 m    dikey1 S0: aynı kule, gece, km'lerce
   K5     kule duvarı + yarık         50mm   6 m     dikey2 D4: aynı duvar, 85mm, 0,6 m

   İKİ YAKIN OKUMA VE KARARLARI:
   · K2 ↔ dikey1 S4 — ikisi de "topraktan çıkan taş". Ölçek ayırıyor:
     31 m gövde (geniş, 32mm) ile 2 m'lik TEK BACAK (50mm, 3 m) aynı
     kadraj değil. Ayrıca dikey1'in afiş karesi bu fragmanın spoiler
     listesindedir — 0 kare.
   · K4 ↔ dikey1 S0 — ikisinde de kule var ve ikisi de 32mm. Ayıran
     MESAFE ve IŞIK REJİMİ: dikey1 geceleyin kilometrelerce uzaktan
     ölçeksiz bir ÇİZGİ gösterir (hook'un değeri ölçeğin okunmamasıdır);
     K4 gündüz, 25 m'den, ölçeği OKUNAN tek karedir. Ters iş.
```

---

## 🎯 BU FRAGMANIN TEK İŞİ

Bu dosya **yeni bir film değil, bir FRAGMANDIR.** İşi tek: filmin
vaadini kurmak ve **cevabı vermeden bırakmak.**

Fragman kaynak filmi yeniden anlatmaz. Filmin **ilk %45'inden** altı
vuruş seçer ve altısında da yalnız **YAPILMIŞ ŞEYLERİ** gösterir.

```
⭐ BU FRAGMANIN TEK CÜMLELİK TASARIM KARARI:
   ALTI VURUŞTA BİR TANE BİLE FAİL YOK. Bekçi hiçbir karede yok —
   ne tam boy, ne diz altı, ne el, ne gölge. Seyirci altı vuruş
   boyunca yalnız İŞİ görür; işi yapanı hiç görmez.
   Kardeş iki teslim tam tersini yapar (dikey 1 dönüşü satar,
   dikey 2 üç parmaklı eli satar). Üç teaser aynı riski üç kez
   satın almaz [FRAGMAN_KILAVUZU §1.3b, risk profili notu].
```

```
KAYNAK FİLM (16:9, 11 faz)             BU FRAGMAN (0:60 dikey)
──────────────────────────────         ─────────────────────────────────
114 sahne, üç perde                →   6 vuruş, tek tırmanış, cevap yok
Bekçi 24 sahnede kadrajda          →   0 kare (hiçbir parçası dahil)
  ↑ sayım kaynağı: faz dosyalarındaki sahne kartlarının kadro satırları
    (kadro B · 1+B · 2+B · B+A · 1+K+B · K+B) — 114 sahnenin 24'ü
Bekçi'nin yüzü (S85)               →   0 kare
Kaptan'ın kopyası (imza çekim)     →   0 kare
Kule İÇİ 400 m boşluk              →   0 kare — kule yalnız DIŞ DUVAR,
                                       kapının ötesi okunmaz beyaz
5 replik / 12 kelime               →   0 REPLİK, 0 KELİME, 0 insan sesi
müzik anempatik                    →   ⚠️ mevcut fragman bestesi kullanılır
                                       (sapma kaydı `FRAGMAN.md` §sapma ②)
```

### ⛔ 1 NUMARALI KURAL: KIRPMA YOK, YENİDEN ÇEKİM VAR

```
Altı vuruşun altısı da 9:16 olarak SIFIRDAN üretilir. Hiçbiri 16:9
masterdan kırpılmaz [FRAGMAN_KILAVUZU §1.1].

Bu altı vuruşta dikeyin kazancı sayısal olarak şudur:
  • K0 — gövde plakası kadrajı baştan sona doldurur, geminin HİÇBİR
    ucu kadraja girmez ve delik ölçeksiz kalır. Kaynak kadraj (32mm,
    12 m) burnu da kadraja sokar; 31 m ölçek ele verilir ve hook ölür.
  • K1 — delik gövdenin ÜST yüzeyindedir (filmin hasar çapası). Dikeyde
    boşluk %20–34'te, kask %46–58'de, ikisi AYNI dikey eksende durur:
    "tam üstünden geçmiş" tek karede okunur. 16:9'da film onu yan yana
    koyar (figür sol üçte bir, boşluk sağda) ve kare iki ayrı nesne
    gibi okunur.
  • K2 — bacağın iki ucu da okunmak zorundadır: tepede doğru menteşe
    geometrisi, dipte dikişsiz kök. Dikeyde nesne kadraj yüksekliğinin
    %46'sını alır; yatayda aynı nesne için kadrajın iki yanı boş ovaya
    gider.
  • K3 — iki "turuncu" konumu aynı sütunda üst üste gelir: kaynak
    dirsekteki GERÇEK turuncu %58–66'da, taştaki turuncunun OLMASI
    GEREKEN yer %44–48'de. Yatayda ikisi yan yana durur ve kadraja
    gövde silueti girip bilmeceyi çözer.
  • K4 — 400 m'ye karşı 1,68 m. Yalnız dikeyde kulenin tabanı %52'de
    durup tepesi kadrajı terk ederken figür ve sınır çizgisi aynı
    karede kalır. Yatayda ya yükseklik gider ya figür kaybolur.
  • K5 — duvarın ne üstü, ne altı, ne kenarı kadrajda: dikeyde duvar
    bir NESNE değil bir DÜZLEM olur. Yarık kadraj yüksekliğinin
    %46'sını kaplar; yatayda kavis ve zemin çizgisi girer, duvar bir
    binaya dönüşür.

⚠️ Kırpılmış karenin bedeli bu depoda ölçüldü: güvenli alan denetimini
   geçemez (SHORTS_QA §B).
```

### ⚓ ÇAPA BLOKLARI ZATEN ÖDENMİŞ

`REFERANS_PAKETI.md` varlıkların kanonik tanımını kilitledi; bu dosya
o blokları **tek kelime değiştirmeden** kullanır
[`SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1]. Üçüncü fragmanda avantaj üç kat
çalışır: bedel bir kez ödendi, dört teslim onu paylaşıyor.

### ⚠️ DOKUZ BİLİNÇLİ SAPMA — dürüst kayıt

```
① SAHNE SÜRESİ 10 SANİYE — dikey shorts klasör standardı 8 saniyedir.
   Gerekçe `FRAGMAN.md` sapma ①'de yazılıdır ve burada aynen geçerli:
   kaynak film 10 s'lik sahne imzası taşır, müzik 96 BPM'de 1 vuruş =
   TAM 4 ÖLÇÜ eder, 60 s = 24 ölçü. Bu dosya o kararı miras alır.
   ⚠️ ÜRETİM BEDELİ: Veo native klip 8 saniyedir.
      A YOLU = 8 s üret → extend → 10,000 s'ye kırp
      B YOLU = 8 s üret → 0,8× retime → 10,000 s
      B yolu YALNIZ K0 ve K2'de serbesttir (ikisinde de kadrajda
      hareket eden canlı figür yok). K1, K3, K4'te YASAKTIR: 0.9g
      yalanı görünür hale gelir. K5'te de YASAKTIR — gerekçe ⑧.

② KAYNAK SAHNELERİN KAMERA HAREKETLERİ DÜŞÜRÜLDÜ — 6/6 tam lockoff.
   Kaynakta hareket taşıyan iki sahne var: S13 (yavaş yanal kaydırma,
   burundan deliğe) ve S49 (sınıra doğru yavaş push-in). Fragmanda
   ikisi de SABİT kamerayla yeniden kurulur; kalan dördü kaynağında
   zaten lockoff'tur (S14 · S32 · S37 · S51).
   Gerekçe risk kararıdır, stil değil: hareketi KURGU taşır. Kardeş
   iki teslim de aynı kararı verdi ve 6/6 lockoff çalıştı.
   ⚠️ S13'te hareket düşünce sahnenin ANLAMI korunmak zorunda:
      kaynakta kaydırma "sağlam gövde → delik" cümlesini KURAR.
      K0 aynı cümleyi tek karede kurar: sağlam panel kadrajın
      tamamıdır, delik onun ortasındaki tek olaydır.

③ LENS VE MESAFE DEĞİŞİMİ — §1.3c gereği kaydı burada:
   K0: kaynak 32mm / 12 m → 50mm / 5 m. Gerekçe dikeyin kazancı
       maddesinde sayıyla yazılı (geminin ucu kadraja girerse ölçek
       ele verilir).
   K4: kaynak 32mm / 6 m → 32mm / 25 m. Lens aynı, mesafe dört kat.
       Gerekçe: 6 m'de iki figür kadrajı doldurur ve 400 m bir DUVAR
       olur; afiş karesinin tek işi ölçeği okutmaktır.
   Kalan dört vuruşta lens kaynağıyla aynıdır (50 · 100 · 50).
   ⛔ Kayıtsız lens değişimi sonraki denetimde devamlılık hatası gibi
      okunur — bu yüzden dört satır da burada duruyor.

④ KADRO SAYISI DÜŞÜRÜLDÜ — iki vuruşta:
   K4: kaynak S49 kadro 2 (Kaptan + Mühendis) → fragmanda 1 (Kaptan).
       Gerekçe iki katlı: (a) iki insanlı kare KART 4 riskini satın
       alır (turuncu/teal takası, 13 cm boy farkı) ve bu fragman o
       riski hiç doğurmaz; (b) afiş karesinde TEK siluet 400 m'yi
       daha sert ölçer.
   K5: kaynak S51 kadro 2+Bekçi → fragmanda 0.
       Gerekçe: bu fragmanın tasarım kararı (kadrajda fail yok) ve
       spoiler kapısı (Bekçi 0 kare). Kapı kaynak sahnede zaten
       AÇILMIŞ hâldedir; fragman yalnız duvarı ve yarığı kadrajlar.
   ⛔ Yeni içerik YAZILMADI: her iki kadrajın da her ögesi kaynak
      sahnenin prompt gövdesinde vardır.

⑤ İMAJ PROMPT BANDI AŞILIYOR — ölçülmüş kayıt.
   Betiğin ölçtüğü değerler: imaj 3.095–3.950 · video 2.318–2.570.
   VİDEO tarafı bandın (2.000–2.600) İÇİNDE; sapma yalnız imaj
   tarafındadır ve betik onu "karar bekliyor" olarak işaretler, bulgu
   saymaz (prompt_kontrol.py · IMAGE_BANDI_KARARA_BAGLI). Sebep
   `FRAGMAN.md` sapma ④'te sayıyla yazılı ve burada aynı iki yapısal
   kalem geçerli:
     • COMPOSITION / güvenli alan paragrafı — filmin 16:9
       promptlarında yok; dikeyde yüzde bandı yazılmazsa anlam alt
       çeyreğe düşer ve kare SHORTS_QA §B'den geçmez.
     • STANDALONE RİSK KİLİTLERİ — filmde bir sahnenin negatifini
       komşu sahneler destekler; burada altı klip tek başına durur.
   ⛔ TAVAN: hiçbir prompt 4.000 karakteri geçmez (KILAVUZ_REHBERI §7
      ~4.300'ü "Veo hata veriyor" olarak kaydediyor).

⑥ AYNI FİLME ÜÇÜNCÜ DİKEY FRAGMAN — kılavuzda karşılığı yok.
   §1.3b iki fragman için yazıldı ("bir filme ikinci fragman ancak
   üçü birden sağlanırsa yazılır"). Üçüncüsü için satır yok. Sapmanın
   savunması §ÇAKIŞMA DENETİMİ ① ve ②'dir: üç koşul BİR DEĞİL İKİ
   kardeş teslime karşı ayrı ayrı sağlandı ve kadraj denetimi de
   koşuldu. Bu bir varyant değil, üçüncü bir kapıdır.
   → Koşu tuttuysa §1.3b'ye "üçüncü teslim" satırı eklenmeli.

⑦ DOSYA KONUMU — `dikey_shorts_filmler/` altında DEĞİL, filmin kendi
   klasöründe: `FRAGMAN_DIKEY_3.md`. Sebep kardeş dosyalarla aynı:
   çapa blokları filmin `REFERANS_PAKETI.md`'sinden gelir ve dosya bir
   film değil, bir filmin teslim kalemidir. **Film sayımına GİRMEZ**
   (17.08.2026 emsali · `FRAGMAN_KILAVUZU.md` §0 tablosu).

⑧ K5'TE B YOLU (RETIME) YASAK — kadrajda canlı figür olmamasına rağmen.
   Sapma sapmanın tersidir: ① B yolunu figürsüz karelerde serbest
   bırakır, K5 figürsüzdür ve yine de A yolu zorunludur. Sebep
   ölçülebilir: K5'in tek olayı duvarın ayrılmasıdır ve 0,8× retime o
   ayrılmayı ağır çekim gibi okutur. Ağır çekim negatif çekirdekte
   yasaktır; yasağı üretim yolundan geri sokmak D74'lük bir kapıdır.

⑨ ÜRETİM SIRASI §2.2'DEN SAPIYOR — afiş ikinci kapı.
   §2.2 "AFİŞ vuruşu İLK üretilir" der. Burada sıra K5 ile başlar.
   Gerekçe bu depoda ÖLÇÜLDÜ: F5 koşusunda model kule tabanına
   KEMERLİ bir kapı çizdi (`FAZ_06_KULE.md` KARAR 5 ③). §2.2'nin
   sebebi "en pahalı kare kapıdır"; bu fragmanda en pahalı kare
   ölçülmüş red sebebi olan K5'tir. Kuralın harfi değil, gerekçesi
   uygulanıyor.
```

### 🚫 SPOILER KAPISI — bu fragmanda ASLA olmayacak dokuz kare

```
⛔ Bekçi — HİÇBİR parçası: tam boy yok, diz altı yok, kol yok, el yok,
   gölge yok, ufukta siluet yok. 0 kare.
⛔ Bekçi'nin yüzü ve BEŞ REPLİĞİNDEN hiçbiri; anonsun sekiz kelimesi
⛔ Kaptan'ın kopyası — imza çekim, iki aynı yüz
⛔ Duvardaki bölme ve içindeki ölü asıl — filmin omurga sırrı
⛔ Kule İÇİ: 400 m boşluk, kayıt duvarı, doğrulama plakası
     ⚠️ K5 BUNUNLA KARIŞTIRILMAZ: K5 duvarı DIŞARIDAN gösterir ve
        yarığın ötesinde okunabilir hiçbir şey yoktur — mesafesiz,
        dikişsiz, boş beyaz. İçeride zemin çizgisi, duvar, derinlik,
        nesne ya da figür 0 karedir.
⛔ ÇIPLAK ELİN PLAKAYA DEĞMESİ
⛔ Kalkış, veda, final kare
⛔ 🔥 İKİNCİ GEMİNİN TAM GÖVDESİ (S35) — dikey 1'in afiş karesi.
     Bu fragmanda 0 kare: üç teaser aynı görüntüyü satmaz.
⛔ ZEMİNİN KABARMASI / CEVAP VERMESİ (S28 · S45 · S47) — dikey 2'nin
     mekaniği. Bu fragmanda zemin hiçbir karede tepki vermez.

Bu dokuz kalem fragmanın bütçesinin dışındadır. Son iki kalem
kardeş teslimlerin bütçesidir ve bilerek dokunulmaz.
```

---

## 🧬 FRAGMANIN MEKANİĞİ — "KUSUR YOK"

Her fragmanın TEK bir mekaniği olur [FRAGMAN_KILAVUZU §1.3]. Bunun
mekaniği bir **işçilik** sorusudur: her vuruşta kadraja bir şey daha
girer ve o şeyde yapılmış tek bir hata yoktur. Seyirci dört vuruşta
bunu öğrenir; beşincide işin ölçeğini görür, altıncıda kusursuz olan
şey bir kapıya dönüşür ve kimse çıkmaz.

```
VURUŞ   KADRAJDAKİ İŞ                     HATA ARANIYOR       SEYİRCİ NE ÖĞRENİR
─────   ────────────────────────────      ───────────────     ────────────────────────
K0      gövdede 1,2 m kusursuz daire      is yok, çapak yok   Bu hasar değil, KESİM
K1      delik çekirdeğin tam ortasından   sapma yok           Nişan alınmış
        geçmiş
K2      taştan bir iniş bacağı,           orantı hatası yok   Aynısını YAPABİLİYOR
        topraktan çıkmış
K3 ⭐   taş gövdede her dikiş, her perçin RENK yok            ⚠️ Tek eksik renk —
        yerinde                                               kopyalamıyor, DÖKÜYOR
K4 🔥   400 m tek parça duvar; tozun      dikiş yok,          Ve bu ölçekte çalışıyor
        geçmediği bıçak gibi sınır        pencere yok
K5 ❓   duvar ayrılıyor                   menteşe yok,        Kusursuz olan şey bir
                                          ses yok             KAPI — ve kimse çıkmıyor
```

**Mekaniğin insani karşılığı:** Fragman "bu gezegen tehlikeli" demiyor.
"Bu gezegen USTA" diyor. İnsanların dünyası yamalı, vidalı, çizik
dolu; karşılarındaki şey iki yüz yıldır tek bir hata yapmamış. Son
karede o kusursuzluk bir eşiğe dönüşüyor ve eşikte kimse yok.

```
⭐ MEKANİK KIRILMASI K3'TEDİR, K5'TE DEĞİL.
   Dört vuruş boyunca kurulan kural ("hiçbir şeyi yanlış yapmıyor")
   tam da her şeyi doğru yaptığı yerde bir eksik verir: RENK. Ve bu
   bir HATA değildir, bir SEÇİMDİR — biçim kopyalanır, renk
   bırakılır. Kaynak film bu kuralı aynı sahnede kurar ve 40 sahne
   sonra bir insan yüzüne uygular (`FAZ_04_TARLA.md` S37 sahne kartı).
   Fragman o ikinci yarıyı vermez.

⛔ K5 bir kırılma değil, kırılmanın FATURASIDIR: kusursuz duvar
   açılabiliyorsa, o duvarın arkasında bir şey var demektir.
```

---

## 🎞️ KURGU — altı vuruş ve kaynak eşlemesi

| # | Vuruş | Şablon rolü | Süre | Kadro | Kaynak sahne | Filmdeki yeri | Lens | Hareket | Yol |
|:-:|---|---|:--:|:--:|---|:--:|:--:|---|:--:|
| **K0** | **DELİK** | HOOK | 10 s | 0 | `FAZ_02` S13 | %11 | 50mm | tam sabit | B |
| **K1** | **TAM ORTASINDAN** | KURULUM | 10 s | 1 | `FAZ_02` S14 | %12 | 50mm | tam sabit | A |
| **K2** | **AYNISI** | TIRMANIŞ | 10 s | 0 | `FAZ_04` S32 | %27 | 50mm | tam sabit | B |
| **K3** | ⭐ **RENK YOK** | KIRILMA | 10 s | 1 | `FAZ_04` S37 | %32 | 100mm | tam sabit | A |
| **K4** | 🔥 **DÖRT YÜZ METRE** | AFİŞ | 10 s | 1 | `FAZ_05` S49 | %43 | 32mm | tam sabit | A |
| **K5** | ❓ **DUVAR AÇILIYOR** | SORU | 10 s | 0 | `FAZ_06` S51 | %45 | 50mm | tam sabit | A |

```
⭐ ALTI VURUŞ FİLM SIRASINDA İLERLİYOR: %11 → %12 → %27 → %32 → %43
   → %45. Kardeş iki teslim sırayı bozar; bu fragman bozmaz, çünkü
   mekanik bir MERDİVEN değil bir DELİL DİZİSİDİR: her vuruş bir
   öncekinin üstüne kanıt koyar.

⭐ 6/6 TAM LOCKOFF. Fragmanda tek bir kamera hareketi yok (sapma ②).

⛔ SIFIR KESME — her video 10 saniyelik kesintisiz tek çekimdir ve her
   vuruş AYRI üretilir. Kesmeler klip aralarında yaşar, promptun içinde
   değil [Ders 68]. Hiçbir promptta "cut to", "then we see", "montage"
   geçmez.

⏱️ KESME NOKTALARI (kurgu, saniye):
   00,000 → K0   10,000 → K1   20,000 → K2   30,000 → K3
   40,000 → K4   50,000 → K5   60,000 → SERT KESME, siyah yok, fade yok
```

### 🔁 LOOP DİKİŞİ — ölçülü, tesadüf değil

```
K5 son karesi:  kusursuz beyaz duvarda AÇIK BİR YARIK — düz kenarlı,
                paralel, kadrajın orta dikey ekseninde, %26–%72 bandı,
                PARLAK (içeriden düz beyaz).
K0 ilk karesi:  yamalı gri-kahve gövde plakasında AÇIK BİR DELİK —
                kusursuz daire, kadrajın orta dikey ekseninde,
                %38–%50 bandı, KOYU (içerisi siyah uzay).

DİKİŞ ÜÇ ŞEYİ BİRDEN TUTAR:
  ① aynı ekran bölgesi — ikisi de orta dikey eksende; K0'ın dairesi
     K5'in yarık bandının TAM İÇİNE düşer (%38–50 ⊂ %26–72).
     Kurguda üst üste bindirilerek kontrol edilir.
  ② değer tersine döner — parlak açıklık koyu açıklığa keser.
  ③ mekanik bir tur daha döner: son kare "kusursuz yüzeyde bir
     açıklık", ilk kare de öyle. Seyirci ikinci izlemede K0'a
     "bu da bir kapı mıydı?" diye bakar.

Kesme SERT. Fade yok, siyah kare yok, morph yok.
```

---

## 📱 GÜVENLİ ALAN HARİTASI (9:16 · 1080×1920)

```
┌─────────────────────────┐  0%
│  ÜST %13 — ARAYÜZ       │      kanal adı, başlık üst bandı
├─────────────────────────┤  13%
│   G Ü V E N L İ         │      ⭐ tüm anlam burada
│   A L A N               │      13% – 75%
├─────────────────────────┤  75%
│  ALT %25 — ARAYÜZ       │      açıklama, ses, butonlar
└─────────────────────────┘  100%
     ⬅ sağ %12,5 ➡ beğen/yorum/paylaş sütunu
```

| # | Kritik nesne | Yükseklik bandı | Sağ %12,5 temiz mi |
|:-:|---|:--:|:--:|
| K0 | 1,2 m kusursuz daire delik | %38 – %50 | ✅ |
| K1 | boşluk + açık el + kask | %20 – %58 | ✅ |
| K2 | taş bacak + kaynaşmış kök | %20 – %70 | ✅ |
| K3 | temas noktası + boş şerit yatağı | %44 – %48 | ✅ |
| K4 | kule tabanı + sınır + figür | %52 – %70 | ✅ |
| K5 | duvardaki yarık | %26 – %72 | ✅ |

```
KURAL: Altı promptun altısında da COMPOSITION paragrafı bu bandı YAZAR.
Alt çeyrek her karede yalnız zemin, toz, gölge, defokus kütle ya da
ışıksız yüzey taşır — okunması gereken hiçbir şey oraya düşmez.

⚠️ İKİ ZOR VURUŞ:
  · K2'nin kökü ve çatlakları anlamın bir parçasıdır ve %70'i geçemez.
    Bu yüzden bacak %20'den başlar: nesne yukarı itilir, kök %64'e
    oturur, çatlaklar %64–70'te biter.
  · K4'te figür küçüktür (kadraj yüksekliğinin ~%11'i). %59–%70
    bandında durur; bir adım daha aşağı inerse arayüz butonlarının
    altında kalır ve 400 m'nin ölçüsü kaybolur.
```

## 🌗 IŞIK TAKVİMİ — üç ortam, hepsi sayılı

| Vuruş | Ortam | Kaynak | Renk sıcaklığı | Yön | Gölge |
|:-:|---|---|:--:|---|---|
| K0 | yörünge / vakum | tek soluk ay | 7000K | ekran-sol, sıyırma | sert, hızlı düşüş |
| K1 | gemi içi, basınçsız | yalnız 2 kask lambası | 5600K | alttan, dar konik | mutlak siyaha düşer |
| K2 | yüzey gündüz | turuncu yıldız | 4400K | ekran-sol, yayvan | uzun, yumuşak kenarlı |
| K3 | yüzey gündüz | turuncu yıldız | 4400K | ekran-sol, sıyırma | dikişlerde keskin kabartma |
| K4 | yüzey gündüz | turuncu yıldız | 4400K | ekran-sol | uzun, sınırı serbestçe geçer |
| K5 | yüzey gündüz + iç | yıldız 4400K + iç 5600K | ikisi eşikte karışmadan buluşur | ekran-sol / cepheden | eşikte iki ışık, harmanlanmaz |

```
⛔ Bloom yok, glow filtresi yok, lens flare yok, volumetrik ışın yok.
   Kopya materyali, kule ve deliğin kenarı PARLAMAZ — yalnız temiz,
   ölçülü specular verir.
```

---

## 📖 SABİT REFERANSLAR (Bibles)

### ⚓ SIKIŞTIRILMIŞ ÇAPALAR — `REFERANS_PAKETI.md`'den BİREBİR

> ⛔ Sıkıştırma bir özgürlük değildir. Zorunlu sekiz alan: yaş + rol ·
> boy · gövde tipi · ten · saç · **yara izi ve tarafı** · takviye
> rengi · kask/vizör durumu. Biri düşerse kimlik kayması başlar
> [Ders 55]. Aşağıdaki biçimler on iki promptun tamamında kelimesi
> kelimesine aynıdır.

```
KAPTAN:   a 41-year-old woman pilot, 1.68 m, slim — high cheekbones,
          light olive skin, sharp jawline, dark grey-green eyes, a fine
          faded white scar splitting her LEFT eyebrow, dark brown hair
          in a low bun, dark grey-blue suit with ORANGE worn
          reinforcement, a detachable ring at the right wrist, helmet
          on, visor transparent

MÜHENDİS: a 33-year-old man flight engineer, 1.81 m, broad-shouldered —
          light brown skin, short three-day stubble, a 2 cm burn scar on
          his RIGHT cheekbone, very short black hair, the same dark
          grey-blue suit with TEAL GREEN reinforcement and an oversized
          back tool module, helmet on, visor transparent

CANTOR:   a 31-meter two-crew cargo courier — boxy dark grey-brown
          panelling with mismatched patch panels in three grey tones,
          protruding pipe runs, a narrow forward cockpit, two large aft
          cargo bays, one fusion nozzle and four small thrusters,
          three-legged gear with a 9-meter footprint, thin faded orange
          stripes, dust and heat staining everywhere

HASAR:    a 1.2-meter perfectly circular hole with clean, glassy,
          faintly pearlescent edges in the upper surface of the RIGHT
          rear cargo bay; the RIGHT main leg collapsed and the hull
          tilted exactly 4 degrees to the right

KULE:     a 400-meter seamless one-piece tower, very slightly conical,
          flawlessly matte white — no panel lines, no seams, no windows,
          no lights, no antennas, no markings; the ground within its
          dead ring is bare polished basalt, dustless, honed smooth
```

> ⚠️ **BEKÇİ çapası bu dosyaya TAŞINMAZ.** Altı vuruşun hiçbirinde
> yok; taşınırsa modele davet olur. Aynı sebeple **KARIŞMA KİLİDİ**
> (turuncu/teal + 13 cm) de yok: hiçbir karede iki insan aynı anda
> bulunmuyor, Kaptan ve Mühendis ayrı vuruşlarda ve tek başına
> duruyor. İki insanlı karenin riski bu fragmanda hiç doğmuyor.

### 🌍 World Bible — ANNUR

```
Kayalık dünya, 0.9g yüzey yerçekimi. Atmosfer 0.6 atm, nefes
alınamaz — ama BASINÇ VAR: ses yayılır (boğuk, alçak), rüzgar zayıf,
gölgeler yumuşak kenarlı, toz ÇÖKER ve yüzeye oturur. VAKUM DEĞİL.
Gökyüzü soluk gri-yeşil, tek büyük soluk ay, küçük turuncu yıldız.
Zemin koyu bazalt.
⚠️ İKİ İSTİSNA — K0 ve K1 yüzeyde değildir:
   K0 açık uzayda (vakum) geçer; K1 basınçsız bir gemi bölmesinde.
   İkisinde de toz asılı kalmaz, hiçbir şey süzülmez, ses yoktur.
KOPYA MATERYALİ: mat, kemik grisi, taş dokulu. Orijinalin RENGİ YOK,
sadece BİÇİMİ var. Bu kural K2, K3 ve K4'te geçerlidir.
BÜYÜME GERÇEK ZAMANDA GÖRÜNMEZ — sahneler arası değişir, sahne içinde
asla. Bu cümle her negatif bloğa girer. Bu fragmanda İSTİSNA YOK:
altı vuruşun altısında da zemin ve taş kıpırdamaz.
```

### 🎥 Camera Bible

```
LENS: yörünge/ölçek/ufuk → 32mm anamorphic · orta/gövde → 50mm ·
      yüz/temas → 85mm · makro (doku) → 100mm
HAREKET: 6/6 tam lockoff. Pan yok, tilt yok, zoom yok, track yok,
         el kamerası yok, hız rampası yok, ağır çekim yok.
ÖLÇEK KİLİDİ: CANTOR tam 31 m · delik tam 1,2 m · Kaptan 1,68 m ·
         Mühendis 1,81 m · taş bacak insan boyunda · kule 400 m ·
         yarık 4 m yüksekliğinde
YÖNELİM KİLİDİ: CANTOR'un burnu K0'da kadraj dışında EKRAN-SOLDA,
         kıçı ekran-sağda kalır. Gövde hiçbir karede yuvarlanmaz.
```

### 💡 Lighting Bible

```
(1) VAKUM GECE (K0) — tek soluk ay 7000K, ekran-soldan sıyırarak;
    panel dikişleri ve yama kenarları sert kabartma. Deliğin kenarı
    tek ince sedefli parıltı verir: yansıma, kaynak değil.
(2) BASINÇSIZ BÖLME (K1) — yalnız iki kask lambası 5600K, dar ve
    sert; kalan her şey siyaha düşer. Delikten sert yıldızlar.
(3) YÜZEY GÜNDÜZ (K2, K3, K4, K5) — turuncu yıldız 4400K, Dünya
    ışığının %70'i, kadrajın SOLUNDAN yayvan; gölge kenarları yumuşak.
    K5'te ikinci bir ışık var: yarığın içinden gelen düz, soğuk,
    kaynaksız beyaz (5600K). İki ışık eşikte harmanlanmadan buluşur.
```

### 🚫 Negative Bible — altı promptun altısına gömülür

```
Single unbroken take, no cuts, no transitions, no camera shake.
CHARACTER COUNT LOCK: exactly [N] figures in frame — no duplicates, no
extra people, no crowd. Copy material is matte bone-grey stone — it
never emits light, never sparkles, and never carries the colour of the
original. Growth is never visible in real time; the ground is static
within the shot. Damage is a clean geometric cut and never an
explosion: no burn, no soot, no char, no jagged tear, no blast
deformation. No bloom, no glow filter, no lens flare, no waxy skin, no
airbrushing, no face morphing. Human visors stay visible as distinct
glass surfaces with zero tint and never carry a mirror coating. No
readable text, letters, digits or symbols on any panel, display, wall
or surface. No subtitles, no captions, no title card, no end card, no
watermark. All dust and fragments obey 0.9g on the surface — they fall
and come to rest, never hover, never drift like liquid. Photorealistic,
35mm anamorphic film grain.
```

---

## 🔒 DERS KİLİTLERİ — bu fragmanın risk profili

```
DERS 2    ANATOMİ MORPHU — bu fragmanda Bekçi 0 karededir; uzun kol,
          üç parmak, 2,10 m gövde hiç üretilmez. Kardeş iki teslimin
          1 ve 2 numaralı riskleri burada HİÇ DOĞMUYOR.
DERS 3/29 PARLAYAN MALZEME — taş kopya, kule ve deliğin sedefli kenarı
          ışık YAYMAZ. Üçü de yalnız yansıtır.
DERS 5/79 VİZÖR — K1 ve K4'te insan kaskı takılı, vizör her karede
          ayrı bir cam yüzey, sıfır tint, sıfır ayna kaplaması.
          Sırt ünitesi yalnız Mühendis'te ve yalnız K1'de.
DERS 11/43 TEMAS — K1'de el deliğin KENARINA DEĞMEZ, boşluğun içinden
          geçer. K3'te parmak ucu yüzeyde GEZİNİR: batmaz, iz
          bırakmaz, taşı ısıtmaz.
DERS 13   OKUNABİLİR METİN — hiçbir karede rakam, harf, gemi işareti,
          gösterge değeri yok. ⭐ Bu fragmanda göğüs göstergeleri de
          KADRAJA GİRMİYOR (K1'de lambalar dışında her şey siyah) —
          KART 5 riski sıfırlandı.
DERS 32   ÖLÇEK KAYMASI — delik 1,2 m, Mühendis 1,81 m, taş bacak
          insan boyunda, kule 400 m, yarık 4 m. Beşi de prompt
          gövdesinde yazılı.
DERS 34   AD PROMPTA YAZILMAZ — "a 33-year-old man flight engineer".
          Milliyet, kurum, isim yok.
DERS 38   HASAR ABARTMA — "damaged" kelimesi hiçbir promptta yok.
          K0 ve K1'de gövdenin tamamı SAĞLAM yazılır; tek olay delik.
DERS 39   TOZ ÇÖKER — K2, K3, K4'te toz oturur, girdap yapmaz.
          K0 ve K1'de zaten hiç toz asılı değildir (vakum).
DERS 41   YUMUŞAK GÖLGE — yüzey sahnelerinde atmosfer var, gölge kenarı
          yumuşak. Vakum sertliği yalnız K0 ve K1'de doğrudur.
DERS 68   KESME PROMPTUN İÇİNDE DEĞİL — altı prompt da tek çekim.
DERS 82   GÖVDESİZ SES — 0 replik, 0 kelime; hatanın yüzeyi yok.
```

**RİSK SAYIMI: 2 / 9.** kask/vizör (Kart 3 — K1 ve K4) · toz/parçacık
(Kart 6 — K2 ve K4). Su yok · canlı yok · **ekran/sayaç yok (Kart 5
sıfır)** · **iki insanlı kare yok (Kart 4 hiç doğmuyor)** · diyalog yok ·
patlama yok · kalabalık yok · kamera 6/6 sabit (Kart 8 sıfır).

```
⭐ DEPODAKİ ÜÇ DİKEY TESLİMİN RİSK KARŞILAŞTIRMASI — dürüst kayıt:
   FRAGMAN.md (dikey 1)   : Bekçi TAM BOY DÖNÜŞÜ + iki insanlı kare
   FRAGMAN_DIKEY_2.md     : 3 parmak + başparmak (D4) + kör oyuk (D5)
   BU DOSYA               : 2/9 — serinin en düşük risk profili
   Sebep tesadüf değil: kadrajda fail yok. Anatomi riski taşıyan tek
   varlık hiç üretilmiyor.
```

> 🚨 **DÜRÜST KAYIT — bu fragmanın gerçek 1 numaralı riski K5'tir.**
> Model kusursuz bir duvara KAPI çizmeye eğilimlidir ve bu eğilim bu
> depoda ÖLÇÜLDÜ: F5 koşusunda kule tabanına **kemerli** bir kapı
> çizildi (`FAZ_06_KULE.md` KARAR 5 ③). K5'in tek olayı düz kenarlı,
> paralel kenarlı, kalınlıksız bir YARIK'tır — menteşe, ray, kayan
> plaka, çerçeve, kalınlık ya da kemer belirirse vuruş çöp olur.
> **Üretim K5'ten başlar** (sapma ⑨).
> İkinci risk K0/K1'dir: modeller temiz bir deliği patlamaya çevirir —
> is, çapak, çatlak, eğrilmiş dudak ekler.

---

# 📱 BÖLÜM 1 — ALTI VURUŞ

---

## 🎬 SAHNE K0 — HOOK: DELİK

_"Kimse bu kadar temiz vurmaz."_

**Kaynak:** `FAZ_02_VURULMA` S13 · **Kadro:** 0 · **Işık:** vakum gece ·
**Üretim yolu:** B (retime 0,8× serbest — kadrajda canlı figür yok)

### 📸 GÖRSEL PROMPT

```
SCENE:
A perfectly circular hole has been cut clean through the upper hull plate of a small cargo ship in space. Everything around it is intact.

ENVIRONMENT:
Open space above the night side of a rocky planet. The hull plate fills the frame like a wall: dark grey-brown panelling with mismatched repair patch panels in three grey tones, protruding external pipe runs, thin faded orange accent stripes, dust and heat staining and years of fine scratches — sound, whole and unbroken everywhere except at one point. Past the outboard edge of the plate at the top of frame: black space, sparse hard stars, and the dark curve of the planet far below them.

SUBJECT:
Exactly 0 figures. Dead centre: a 1.2-meter perfectly circular hole through the plate, its edge clean, smooth and faintly pearlescent, as if the metal had been removed rather than broken — no burn, no soot, no scorching, no blast deformation, no bent lip, no torn fibres, no debris. Inside the bore, the dark edge of an interior equipment rack; past that, a small disc of black space with two hard stars in it, where the same bore leaves the far side of the ship. The hole is the only event on the entire hull.

CAMERA:
Shot on a 50mm lens from a fixed locked-off position five meters off the plate, square to its surface, f/5.6. The ship's bow lies out of frame at screen-left and its stern out of frame at screen-right, so no end of the vessel is visible and its size cannot be read. True 31-meter ship scale.

COMPOSITION:
Vertical 9:16. The hull plate fills the frame from top to bottom. The circular hole sits on the centre vertical axis and spans roughly thirty-eight to fifty percent of frame height, clear of the outer right eighth. The outboard edge of the plate crosses at roughly twelve percent with black space and stars above it. The bottom quarter carries only unlit panelling and one pipe run in shadow.

LIGHTING:
Night. Hard grey-blue moonlight at 7000K grazing from screen-left rakes the panel seams and patch edges into sharp relief; the shadowed side falls off fast. The rim of the bore catches one thin pearlescent sheen — a reflection, never a source. Every scratch keeps its texture.

PHYSICS:
Vacuum. The ship coasts level and steady. Nothing vents, nothing drifts, nothing burns.

NEGATIVE:
Human count: exactly 0 humans in frame. Exactly 0 figures and 0 other ships. The hole stays a perfect circle exactly 1.2 meters across with a smooth rim — no burn, no soot, no char, no melted slag, no jagged tear, no radiating cracks, no blast dish, no second hole, no impact scar anywhere else on the hull. Nothing comes out of it: no gas, no vapour, no smoke, no fire, no sparks, no floating debris. The rim never emits light of its own. Fixed locked-off camera — no pan, tilt, zoom, track, handheld, shake, speed ramp or slow motion. No bloom, no glow filter, no lens flare, no volumetric beam. No readable text, letters, digits, serial numbers or hull markings anywhere. No miniature look, no toy look, no CGI look. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 50mm, locked off five meters off the hull plate, square to its surface, f/5.6. The camera does not move at all. Real-time motion at normal speed.

At 0s — Open space above the night side of a dark rocky planet. The upper hull plate of a small cargo ship fills the frame like a wall: dark grey-brown panelling, mismatched repair patches in three grey tones, protruding pipe runs, thin faded orange stripes, dust and heat staining, years of fine scratches. The ship's bow lies out of frame at screen-left and its stern out of frame at screen-right; no end of the vessel is visible. Past the plate's outboard edge at the top of frame: black space, sparse hard stars, the dark curve of the planet far below. On the centre vertical axis, spanning roughly thirty-eight to fifty percent of frame height, a 1.2-meter perfectly circular hole passes through the plate — edge clean, smooth, faintly pearlescent, no burn and no soot.
At 2s — Nothing moves. Hard grey-blue moonlight holds on the panel seams; the rim of the hole keeps one thin sheen.
At 4s — Inside the bore the dark edge of an interior rack is just readable, and past it a small disc of black space with two hard stars in it.
At 6s — The ship coasts. Not one particle leaves the hole; nothing vents, nothing drifts, nothing burns anywhere in frame.
At 8s — The two stars past the far side of the bore shift by a hair as the ship coasts, and nothing else in the frame changes at all.
By 10s — The frame is exactly as it began: a working, intact hull with one perfect circle cut through it.

Human count: exactly 0 humans in this shot, and exactly 0 other ships. The hole stays a perfect circle 1.2 meters across with a smooth rim — it never chars, never cracks, never widens, never grows a second hole. Nothing comes out of it at any second: no gas, no vapour, no smoke, no fire, no sparks, no floating debris. The rim never emits light of its own. The hull never deforms and never rolls. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE K1 — KURULUM: TAM ORTASINDAN

_"Nişan almış."_

**Kaynak:** `FAZ_02_VURULMA` S14 · **Kadro:** 1 (Mühendis) ·
**Işık:** basınçsız bölme, yalnız kask lambaları ·
**Üretim yolu:** A ZORUNLU (kadrajda canlı figür var)

> ⚠️ **DİKEY KADRAJ KAYNAĞA DAHA YAKIN:** delik filmin hasar çapasında
> gövdenin ÜST yüzeyindedir. 16:9'da film onu yana koyar (figür sol
> üçte bir, boşluk sağda); dikeyde olması gereken yere — adamın tam
> üstüne — oturur ve "tam ortasından geçmiş" tek karede okunur.

### 📸 GÖRSEL PROMPT

```
SCENE:
Inside a dark airless cargo bay, a man in a sealed suit stands under a clean circular void where the navigation core used to be, his open hand raised into it.

ENVIRONMENT:
The interior of a cargo bay, unlit except for his suit lamps: equipment racks, conduit bundles, bolted frames, grey repair patches, cargo straps hanging dead still. Directly above him, a 1.2-meter perfectly circular hole passes through the bay's upper surface and through the centre of the rack in one geometric bore — rim smooth, faintly pearlescent, no burn marks, no soot. Through it, black space and hard stars. The bay is airless and silent; the dust is settled and static.

SUBJECT:
Exactly one figure: a 33-year-old man flight engineer, 1.81 m, broad-shouldered — light brown skin, short three-day stubble, a 2 cm burn scar on his RIGHT cheekbone, very short black hair, the same dark grey-blue suit with TEAL GREEN reinforcement and an oversized back tool module, helmet on, visor transparent. Seen three-quarter from behind his right shoulder, chest-up, an arm's length under the void. His right arm is raised into the bore, hand open, fingers spread, touching nothing — the hand hangs inside the circle with clean vacuum on both sides of it. His mouth is closed and still. His face reads clearly in profile through the glass.

CAMERA:
Shot on a 50mm lens from a fixed locked-off position three meters away, f/4, at chest height, dead level. True 1.81-meter human scale.

COMPOSITION:
Vertical 9:16. The circular void sits on the centre vertical axis and spans roughly twenty to thirty-four percent of frame height. His raised open hand is at roughly thirty-eight percent, just under the rim. His helmet sits at roughly forty-six to fifty-eight percent, left of centre and clear of the outer right eighth. The bottom quarter carries only dark bay floor, one bolted frame and a hanging cargo strap.

LIGHTING:
Only his two helmet lamps: two hard, narrow white pools at 5600K that catch the bore's pearlescent rim as a sheen, never a glow, and rake his visor glass from below. Everything else in the bay falls to black. Through the bore, hard stars on black.

PHYSICS:
Normal ship gravity; the bay is airless. Nothing floats, nothing drifts, no dust hangs in the air.

NEGATIVE:
Human count: exactly 1 human in frame — no second person, no duplicate, no reflected face. His reinforcement stays TEAL GREEN and the burn scar stays on his RIGHT cheekbone. The visor is one seamless piece of fully transparent glass with zero tint, zero mirror coating and zero reflection that hides his face. No back-mounted equipment other than his own bulky tool module — no tanks, no hoses, no straps, no antenna. His hand never touches the rim and never leaves the circle. The hole stays a perfect circle 1.2 meters across with a smooth rim — no burn, no soot, no char, no jagged tear, no cracks, nothing venting through it. No handheld tool; the sheath stays closed. No fire, no sparks, no floating debris. Fixed locked-off camera — no pan, tilt, zoom, track, handheld, shake, speed ramp or slow motion. No bloom, no glow filter, no lens flare, no volumetric beam from the lamps. No waxy skin, no airbrushing, no face morphing. No bare head. No readable text, letters, digits or panel markings anywhere. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 50mm, locked off three meters away, at chest height, dead level, f/4. The camera does not move at all. Real-time motion at normal speed.

At 0s — A dark airless cargo bay lit only by two helmet lamps: equipment racks, conduit bundles, bolted frames, grey repair patches, cargo straps hanging dead still. On the centre vertical axis above him, spanning roughly twenty to thirty-four percent of frame height, a 1.2-meter perfectly circular hole passes through the bay's upper surface and the rack in one clean bore, its rim smooth and faintly pearlescent, black space and hard stars past it. Under it stands a 33-year-old man flight engineer, 1.81 m, broad-shouldered, three-quarter from behind his right shoulder: light brown skin, short three-day stubble, a 2 cm burn scar on his RIGHT cheekbone, very short black hair, dark grey-blue suit with TEAL GREEN reinforcement, oversized back tool module, helmet on, visor transparent, his face reading in profile through the glass.
At 2s — He raises his right arm slowly and puts his open hand up into the bore. The hand hangs inside the circle, fingers spread, touching nothing.
At 4s — He holds it there. His two lamps hold their pools on the rim. His mouth stays closed and his lips do not move.
At 6s — He turns the hand over once, palm up, still inside the circle, still touching nothing. The stars past the bore do not change.
At 8s — He lowers the arm to his side and stands still, his head tipped back under the hole.
By 10s — He is motionless under the circle: arm down, head raised, the bore untouched.

Human count: exactly 1 human in this shot. He never speaks, his mouth never opens and no lips move at any second. Reinforcement stays TEAL GREEN, the burn scar stays on his RIGHT cheekbone, and his face keeps identical bone structure from first frame to last. The visor stays fully transparent with zero tint and zero mirror coating. His hand never touches the rim of the hole. The hole never chars, never widens, never vents. Nothing floats or drifts anywhere in the airless bay. No fire, no sparks, no debris. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE K2 — TIRMANIŞ: AYNISI

_"Bu bir enkaz parçası değil."_

**Kaynak:** `FAZ_04_TARLA` S32 · **Kadro:** 0 · **Işık:** yüzey gündüz ·
**Üretim yolu:** B (retime 0,8× serbest — kadrajda canlı figür yok)

### 📸 GÖRSEL PROMPT

```
SCENE:
A spacecraft landing leg stands half-emerged from a basalt plain in morning light — perfect in form, wrong in every other way.

ENVIRONMENT:
Open basalt plain under soft orange daylight from a small orange star, 4400K, soft-edged shadows, pale grey-green sky, one large pale moon as a faint daytime disk. Fine settled dust and hairline fractures across the ground. The plain runs empty to a hazy horizon; a few small pale shapes sit far off, well out of focus and deliberately hard to count.

SUBJECT:
Exactly 0 figures. On the centre vertical axis: a spacecraft landing leg the height of a man, rising from the ground at a slight angle — strut, hinge and wide foot pad all present, every proportion and every mechanical detail correct. But the whole object is matte bone-grey stone, single-toned, carrying no colour of an original, no markings and no light of its own; its surfaces are smooth and dry like honed rock, dusted in the hollows. It has no base line: where it meets the ground its material widens and flows into the basalt in one continuous surface — grown out of the plain, not planted in it. Around its root, hairline cracks radiate outward through the dust.

CAMERA:
Shot on a 50mm lens from a fixed locked-off position three meters away, f/5.6, at chest height, dead level, the whole leg and its rooted base in frame. Physically accurate perspective and true human-height scale.

COMPOSITION:
Vertical 9:16. The stone leg runs from roughly twenty to sixty-six percent of frame height on the centre vertical axis, clear of the outer right eighth. Its root and the radiating hairline cracks sit at roughly sixty-four to seventy percent. The hazy horizon crosses at roughly seventy-four percent. The upper thirteen percent is empty pale sky; the bottom quarter carries only out-of-focus dust and bare basalt.

LIGHTING:
Soft orange daylight, 4400K, from screen-left; long soft-edged shadows from the thin atmosphere. The grey stone takes the warm light dully — matte, unreflective, never emitting. Every surface keeps texture: stone grain, settled dust, the crisp shadow inside the hinge.

PHYSICS:
0.9g, thin 0.6 atm atmosphere — not vacuum. Dust settled and static. The object is stone and completely still.

NEGATIVE:
Human count: exactly 0 humans in frame. Exactly 0 figures, 0 ships and 0 vehicles. The object never moves, never grows, never sparkles, never pulses and never emits light; no veins of light, no crystal facets, no metal sheen. It is bone-grey stone only — never the metal or the colour of a real landing leg, no orange stripe, no coloured panel, no markings. It stays rooted: no gap, no joint, no shadow line and no seam where its material meets the basalt. The ground never cracks open, never bulges and never moves. No fire, no smoke, no dust plume. No bloom, no glow filter, no lens flare, no volumetric beam. No readable text, letters, digits, serial numbers or markings anywhere. No miniature look, no toy look, no CGI look. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 50mm, locked off three meters away, at chest height, dead level, f/5.6. The camera does not move at all. Real-time motion at normal speed.

At 0s — An open basalt plain in soft orange daylight, pale grey-green sky, one faint daytime moon, fine settled dust and hairline fractures on the ground. On the centre vertical axis, running from roughly twenty to sixty-six percent of frame height, a spacecraft landing leg the height of a man rises from the plain at a slight angle: strut, hinge and wide foot pad all present, every proportion correct — and the whole thing matte bone-grey stone, single-toned, dry and honed, dusted in the hollows. Where it meets the ground it has no base line at all: the material widens and flows into the basalt in one continuous surface. Hairline cracks radiate outward from its root through the dust.
At 2s — Nothing moves. The stone holds the warm light dully; the shadow inside the hinge stays crisp.
At 4s — A weak ground wind lifts a thin veil of dust across the plain from screen-left; it drifts low, falls and comes to rest against the root.
At 6s — The dust has settled. The object has not changed in any way: same angle, same colour, same rooted base.
At 8s — Far behind it the pale shapes on the horizon stay out of focus and unchanged. Nothing approaches, nothing rises.
By 10s — The leg stands exactly as it did in the first frame — a perfect mechanical form in a material that was never machined.

Human count: exactly 0 humans in this shot, and exactly 0 ships. The stone object never moves, never grows, never rises, never sinks, never sparkles and never emits light at any second. It never takes on colour: no orange stripe, no metal sheen, no painted panel. Its root never separates from the ground and no seam, gap or shadow line appears between them. The ground never cracks open and never bulges. All dust obeys 0.9g — it falls and comes to rest, never hovers, never drifts like liquid. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE K3 — ⭐ KIRILMA: RENK YOK

_"Biçim var. Renk yok."_

**Kaynak:** `FAZ_04_TARLA` S37 · **Kadro:** 1 (Kaptan — kol, omuz, yumuşak profil) ·
**Işık:** yüzey gündüz · **Üretim yolu:** A ZORUNLU (kadrajda canlı figür var)

> ⭐ **MEKANİĞİN KIRILMA VURUŞU.** Dört vuruşluk "hiçbir şeyi yanlış
> yapmıyor" kuralı burada tek bir eksik verir ve o eksik bir hata
> değil, bir seçimdir. Kadrajda iki turuncu konumu üst üste durur:
> Kaptan'ın dirseğindeki GERÇEK turuncu ve taşta turuncunun OLMASI
> GEREKEN yer. İkisi arasındaki mesafe kadraj yüksekliğinin %20'sidir.

### 📸 GÖRSEL PROMPT

```
SCENE:
A gloved fingertip rests on the flank of a stone ship copy, exactly where the original's orange stripe should run — and there is only flat grey.

ENVIRONMENT:
Close against the flank of a complete bone-grey stone copy of a ship hull in soft orange daylight, 4400K, from screen-left. The stone flank fills nearly the whole frame: panel seams, a shallow conduit groove, rivet bosses and one shallow repair-patch outline — every feature of a real working hull rendered in matte, single-toned grey stone, dusted in the recesses. Along one panel run there is a raised lip exactly where an accent stripe would be edged, and inside that lip the stone is the same grey as everything else.

SUBJECT:
Exactly one figure, entering from screen-left: the right arm and shoulder of a 41-year-old woman pilot, 1.68 m, slim — high cheekbones, light olive skin, sharp jawline, dark grey-green eyes, a fine faded white scar splitting her LEFT eyebrow, dark brown hair in a low bun, dark grey-blue suit with ORANGE worn reinforcement, a detachable ring at the right wrist, helmet on, visor transparent. Her ORANGE elbow reinforcement is sharp and unmistakable at the frame's left edge; her helmeted profile is soft and out of focus behind it, eyes on the point of contact. Her index fingertip rests lightly on the stone inside the empty stripe lip, at the centre of frame. The geometry of the stripe is there; its colour is not.

CAMERA:
Shot on a 100mm lens from a fixed locked-off position one point five meters away, f/4 — the stone texture and the glove sharp, her profile soft. True scale: the panel seams read hand-sized.

COMPOSITION:
Vertical 9:16. The empty stripe lip runs across the frame at roughly forty-six percent and her fingertip rests on it at roughly forty-four to forty-eight percent, on the centre vertical axis, clear of the outer right eighth. Her ORANGE elbow reinforcement sits at roughly fifty-eight to sixty-six percent at the frame's left edge, and her soft profile at roughly twenty-six to forty percent, also at the left edge. The bottom quarter carries only out-of-focus stone flank and dust in the recesses.

LIGHTING:
Soft orange daylight, 4400K, raking from screen-left — the seams and the empty stripe lip in crisp relief; the stone matte, dry and without sheen. Her suit fabric keeps its scuffs and her skin keeps pore texture.

PHYSICS:
0.9g, thin 0.6 atm atmosphere — not vacuum. Dust settled and static. The stone is cold, dry and rigid.

NEGATIVE:
Human count: exactly 1 human in frame — arm, shoulder and a soft profile only; no second person, no duplicate, no reflected face. The fingertip rests ON the surface — never sinking, never merging; the stone never dents, never warms, never sparkles and never emits light, and no colour appears anywhere under her touch. The stone flank carries no orange stripe, no coloured panel and no metal sheen — the stripe lip stays the same grey as the rest. Reinforcement stays ORANGE and the scar stays on her LEFT eyebrow. The visor is one seamless piece of fully transparent glass with zero tint, zero mirror coating and zero reflection that hides her face. No back-mounted equipment on her suit — no tanks, no hoses, no antenna. Fixed locked-off camera — no pan, tilt, zoom, track, handheld, shake, speed ramp or slow motion. No bloom, no glow filter, no lens flare, no volumetric beam. No waxy skin, no airbrushing, no face morphing. No bare head, no bare skin. No readable text, letters, digits, serial numbers or hull markings anywhere. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 100mm, locked off one point five meters away, f/4. The camera does not move at all. Real-time motion at normal speed.

At 0s — Close against the flank of a bone-grey stone copy of a ship hull in soft orange daylight from screen-left. The stone fills nearly the whole frame: panel seams, a shallow conduit groove, rivet bosses, one shallow repair-patch outline — every feature of a working hull, all of it matte single-toned grey stone, dusted in the recesses. A raised lip runs across the frame at roughly forty-six percent exactly where an accent stripe would be edged, and inside that lip the stone is the same grey as everything else. Entering from screen-left: the right arm and shoulder of a 41-year-old woman pilot, dark grey-blue suit with ORANGE worn reinforcement bright at her elbow, a detachable ring at the right wrist, helmet on, visor transparent, her profile soft and out of focus behind the arm, a fine faded white scar splitting her LEFT eyebrow. Her index fingertip rests on the stone inside the empty lip.
At 2s — Nothing happens. The fingertip stays on the surface. Her mouth stays closed and her lips do not move.
At 4s — The fingertip slides slowly along the empty lip, following the line the stripe should occupy. It leaves no mark and picks up nothing.
At 6s — It stops. The stone under it is unchanged: same grey, same dry matte surface, no warmth, no colour.
At 8s — Her hand lifts a few centimetres off the stone and stays there, open.
By 10s — The hand is still raised and the empty lip runs on across the frame, grey from edge to edge.

Human count: exactly 1 human in this shot. She never speaks, her mouth never opens and no lips move at any second. Reinforcement stays ORANGE and the scar stays on her LEFT eyebrow. The visor stays fully transparent with zero tint and zero mirror coating. The fingertip never sinks into the stone and never leaves a mark; the stone never dents, never warms, never sparkles, never emits light and never takes on colour at any second. No orange stripe or coloured panel ever appears on the stone. The hull copy does not move, grow or shift. All dust obeys 0.9g — it falls and comes to rest, never hovers. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE K4 — 🔥 AFİŞ: DÖRT YÜZ METRE

_"Bir adımda değişiyor."_

**Kaynak:** `FAZ_05_TEMAS` S49 (kule ölçek kilidi S48'den) ·
**Kadro:** 1 (Kaptan, sırttan, küçük) · **Işık:** yüzey gündüz ·
**Üretim yolu:** A ZORUNLU (kadrajda canlı figür var)

> ⭐ **AFİŞ VURUŞU — fragmanın tek ölçek karesi.** Bu fragmanda 400 m
> yalnız burada okunur; kalan beş vuruşta ölçek bilerek gizlenir.
> Kaynak sahnede iki insan var; burada bir (sapma ④).

### 📸 GÖRSEL PROMPT

```
SCENE:
One small figure stands at a line drawn across the world: on her side dusty broken basalt, past it polished bare stone — and above it all, a white tower that leaves the top of the frame.

ENVIRONMENT:
An open basalt plain under soft orange daylight, 4400K, from screen-left, pale grey-green sky. Crossing the frame, a perfectly sharp boundary arcs through the plain: on the near side, textured basalt under fine grey dust with hairline fractures and a thin low dust bank drifted against the edge; past it, smooth honed stone — dustless, seamless, faintly reflective — running unbroken to the base of the tower. Rising out of that polished ground and filling the upper frame: a 400-meter seamless one-piece tower, very slightly conical, flawlessly matte white — no panel lines, no seams, no windows, no lights, no antennas, no markings — leaving the top of frame long before it ends.

SUBJECT:
Exactly one figure, small in frame, seen from behind and stopped a stride short of the line: a 41-year-old woman pilot, 1.68 m, slim — dark brown hair in a low bun behind a transparent visor, dark grey-blue suit with ORANGE worn reinforcement, a detachable ring at the right wrist, helmet on. Her head is tipped back so that she is looking up the face of the tower. Her long soft shadow reaches the boundary and continues past it — the only thing in frame that crosses freely. Not one grain of dust lies on the polished side.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed locked-off position twenty-five meters behind her, at chest height, tilted slightly up so the tower crushes the sky. Deep focus. Physically accurate perspective: 400 meters against a 1.68-meter figure.

COMPOSITION:
Vertical 9:16. The tower's base sits at roughly fifty-two percent of frame height, on the centre vertical axis, and its faces fill everything above that, running out of frame at the top. The knife-sharp boundary arcs across the frame at roughly sixty-eight percent. The figure stands on the centre axis at roughly fifty-nine to seventy percent, clear of the outer right eighth, no taller than one ninth of frame height. The bottom quarter carries only dusty basalt and the low dust bank.

LIGHTING:
Soft orange daylight, 4400K, from screen-left: matte and grainy on the dusty side, a clean low sheen on the polished side; the tower holds a soft warm gradient on one face and falls to cool shadow on the other — reflected light only, never emitted. Long, soft-edged shadows from the thin atmosphere.

PHYSICS:
0.9g, thin 0.6 atm atmosphere — not vacuum. Dust settled and static; the low bank rests against the boundary and stops there.

NEGATIVE:
Human count: exactly 1 human in frame — no second person, no duplicate, nobody else on the plain, no tall figure anywhere. Reinforcement stays ORANGE; the visor is fully transparent glass with zero tint and zero mirror coating; the helmet stays on and sealed. No back-mounted equipment on her suit — no tanks, no hoses, no antenna. The boundary stays one continuous knife-sharp edge — no gradient, no blend, no transition band, no glowing rim; nothing stands on or above it: no wall, no pane, no glass, no barrier, no dome. The polished side is bare stone — no pattern, no veins, no light from below, and not one grain of dust on it. The tower is a seamless matte white column: no windows at all, lit or unlit, no glass, no ports, no openings, no doors, no hatches, no vents, no balconies, no markings, no lights, and it never emits light. It is not a rocket: no cylinder joints, no nosecone, no fins, no gantry, no exhaust. Fixed locked-off camera — no pan, tilt, zoom, track, handheld, shake, speed ramp or slow motion. No bloom, no glow filter, no lens flare, no volumetric beam. No readable text, letters, digits or markings anywhere. No miniature look, no toy look, no CGI look. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 32mm anamorphic, locked off twenty-five meters behind the figure, at chest height, tilted slightly up. The camera does not move at all. Real-time motion at normal speed.

At 0s — An open basalt plain in soft orange daylight from screen-left, pale grey-green sky. A perfectly sharp boundary arcs across the frame at roughly sixty-eight percent of frame height: near side textured basalt under fine grey dust with a thin low dust bank drifted against the edge; past it smooth honed stone, dustless and faintly reflective, running unbroken to the base of a tower. The tower rises from roughly fifty-two percent and fills everything above it — 400 meters, seamless, one piece, very slightly conical, flawlessly matte white, no seams, no windows, no lights, no markings — and it leaves the top of frame. On the centre axis, small, seen from behind and stopped a stride short of the line, stands a 41-year-old woman pilot, 1.68 m, dark grey-blue suit with ORANGE worn reinforcement, helmet on, visor transparent, dark brown hair in a low bun.
At 2s — Nothing moves but a weak ground wind, which pushes a thin veil of dust across the near side from screen-left.
At 4s — The dust reaches the boundary and stops dead at it, banking a few centimetres higher against the edge. Not one grain crosses onto the polished stone.
At 6s — She tips her head back slowly and looks up the face of the tower. Her shadow lies still across the line.
At 8s — She holds there, head back, both boots planted on the dusty side.
By 10s — She is motionless, tiny under a wall of white that has no top in this frame.

Human count: exactly 1 human in this shot — nobody else appears on the plain at any second, and no tall figure enters frame. She never speaks and her helmet never comes off. Reinforcement stays ORANGE; the visor stays fully transparent with zero tint and zero mirror coating. The boundary stays one continuous knife-sharp edge and never blurs, blends or lights up; not one grain of dust ever crosses it. The tower never grows a window, a door, an opening, a light, a marking or a seam, and it never emits light. All dust obeys 0.9g — it falls and comes to rest, never hovers, never drifts like liquid. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

## 🎬 SAHNE K5 — ❓ SORU: DUVAR AÇILIYOR

_"Menteşe yok. Ses yok."_

**Kaynak:** `FAZ_06_KULE` S51 · **Kadro:** 0 · **Işık:** yüzey gündüz +
yarıktan gelen düz soğuk beyaz · **Üretim yolu:** A ZORUNLU (sapma ⑧)

> ⛔ **BU FRAGMANIN 1 NUMARALI RİSKİ.** Açıklık DÜZ KENARLI, PARALEL
> KENARLI, KALINLIKSIZ BİR YARIKTIR. Kemer değil, kapı değil, panel
> değil, kayan plaka değil. Bu red bu depoda ölçüldü
> (`FAZ_06_KULE.md` KARAR 5 ③). Üretim buradan başlar.
> ⛔ Yarığın ötesinde okunabilir hiçbir şey yok: zemin çizgisi yok,
> duvar yok, derinlik yok, nesne yok, figür yok. Kule içi 0 karedir.

### 📸 GÖRSEL PROMPT

```
SCENE:
A tall narrow opening stands parted in the flawless white wall of a colossal tower — no hinge, no panel, no seam, and nobody in it.

ENVIRONMENT:
The base of a 400-meter matte white tower on polished dead ground, soft orange daylight, 4400K, from screen-left. The wall fills the whole frame: smooth, unmarked, very slightly curved, running out of frame at the top and at both sides, with no top edge and no corner visible anywhere. Along the bottom of frame, honed bare floor meets it — dustless, seamless, faintly reflective. No other opening, marking, lamp, rivet or panel line exists on the wall.

SUBJECT:
Exactly 0 figures. On the centre vertical axis, one tall narrow opening stands parted in the wall: a straight-edged, parallel-sided vertical slot with a flat top, roughly four meters tall and one meter wide, never an arch. Its edges are perfectly clean, with no visible thickness, no track, no frame, no hinge and no sliding plate — the material of the wall simply is not there any more. Past the opening there is only flat, sourceless white: no floor line, no far wall, no depth, no object, no figure, nothing readable at all. Nothing comes out and nothing goes in.

CAMERA:
Shot on a 50mm lens from a fixed locked-off position six meters from the wall, at chest height, square to the surface, f/5.6. True scale: the opening reads as four meters tall against a wall with no visible end.

COMPOSITION:
Vertical 9:16. The slot sits on the centre vertical axis and spans roughly twenty-six to seventy-two percent of frame height, clear of the outer right eighth. The white wall fills everything else, including the upper thirteen percent. The bottom quarter carries only honed floor and the wall's base, with no clutter and no detail.

LIGHTING:
Two lights that meet without blending. Outside: soft orange daylight, 4400K, from screen-left, giving the wall a barely-there warm gradient and the floor a low sheen. Inside the opening: a flat, cool, sourceless white at 5600K with no visible lamp, no falloff and no shape. The two meet exactly at the threshold, unblended, and neither one spills onto the other.

PHYSICS:
0.9g, thin 0.6 atm atmosphere — not vacuum. The floor is dustless. The wall is one solid piece and does not vibrate.

NEGATIVE:
Human count: exactly 0 humans in frame. Exactly 0 figures of any kind — nobody in the opening, nobody at its edges, no silhouette past it, no shadow of a person, no tall figure anywhere. The opening is a straight-edged parallel-sided vertical slot with a flat top — never an arch, never rounded, never a doorway, never a hatch. It has no door, no hinge, no track, no rail, no sliding plate, no frame, no threshold strip and no visible material thickness. Past it there is only flat white: no floor line, no wall, no ceiling, no depth, no stairs, no machinery, no light source, no object, no movement. The wall carries no seam, panel line, rivet, window, lamp, vent or marking, and no second opening anywhere. Nothing emits light, nothing flickers, nothing pulses. No fire, no smoke, no dust plume. Fixed locked-off camera — no pan, tilt, zoom, track, handheld, shake, speed ramp or slow motion. No bloom, no glow filter, no lens flare, no volumetric beam, no god rays. No readable text, letters, digits or symbols anywhere. No miniature look, no toy look, no CGI look. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

### 🎥 VİDEO PROMPT

```
Vertical 9:16. One continuous take, no cuts, 10 seconds. Lens: 50mm, locked off six meters from the wall, at chest height, square to the surface, f/5.6. The camera does not move at all. Real-time motion at normal speed.

At 0s — A flawless matte white wall fills the whole frame: smooth, unmarked, very slightly curved, no top edge and no corner anywhere, honed dustless floor along the bottom of frame, soft orange daylight from screen-left. There is no opening, no seam, no marking and no light on it.
At 1s — On the centre vertical axis a hairline appears in the wall, straight and vertical, from roughly twenty-six to seventy-two percent of frame height. No panel moves and no plate slides; the material simply parts.
At 2s — The line opens evenly into a narrow slot with straight parallel edges and a flat top. A flat, cool, sourceless white light shows past it, meeting the warm daylight at the threshold without blending.
At 4s — The slot reaches its full width, roughly one meter across and four meters tall. Its edges are clean, with no thickness, no track and no frame. Past it there is only flat white — no floor line, no far wall, no depth, no object.
At 6s — Nothing happens. Nothing comes out. No figure, no shadow, no movement anywhere in the opening.
At 8s — Still nothing. The wall is silent, the light past the slot does not change, not one grain of dust moves on the floor.
By 10s — The opening stands exactly as it parted: a clean bright vertical slot in a flawless wall, with nobody in it.

Human count: exactly 0 humans in this shot. Exactly 0 figures of any kind appear at any second — nobody enters, nobody exits, no silhouette, no shadow of a person, no tall figure. The opening never becomes an arch, never rounds off, never grows a door, a hinge, a track, a sliding plate or a frame, and never shows material thickness. Past it there is only flat white at every second: no floor line, no wall, no ceiling, no depth, no stairs, no machinery, no object, no movement. The wall never grows a second opening, a window, a seam or a marking, and it never emits light, never flickers, never pulses. Everything moves at normal speed, no slow motion.

No dialogue, no speaking, no lip sync. No subtitles, no captions, no text, no logos, no watermark. No camera shake, no focus breathing. No bloom, no glow filter, no lens flare, no volumetric beam, no god rays. Photorealistic live-action cinematography, 35mm anamorphic film grain.
```

---

# 🎶 BÖLÜM 2 — MÜZİK VE SES: YENİ BESTE YOK

```
⭐ BU FRAGMANIN EN UCUZ KARARI:
   Beste yeniden yazılmaz. `FRAGMAN.md` BÖLÜM 3'teki 90 saniyelik tek
   master ve onun 60 saniyelik DİKEY KESİMİ (0:00–0:20 + 0:50–1:30)
   bu fragmanda OLDUĞU GİBİ kullanılır.

   Izgara aynı: 6 × 10,000 s · 96 BPM · 1 vuruş = 4 ölçü · darbe
   50,000'de. Ama §1.3b uyarıyor: "IZGARA YETMEZ, SPOTTING DE TUTMALI".
   Aşağıdaki tablo spotting denetiminin kendisidir.
```

## 🪟 PENCERE HARİTASI — mevcut kesim yeni vuruşlara nasıl oturuyor

| Master ölçü | Master zaman | Dikey zaman | Vuruş | Müzikte ne oluyor |
|:--:|---|---|---|---|
| 1–4 | 0:00–0:10 | 0:00–0:10 | **K0** DELİK | sub drone tek başına + oda tonu |
| 5–8 | 0:10–0:20 | 0:10–0:20 | **K1** TAM ORTASINDAN | granüler taş dokusu girer, çok kısık |
| ✂️ | 0:20 ↔ 0:50 | | | birleşme noktası — ölçü başı, aynı akor |
| 21–24 | 0:50–1:00 | 0:20–0:30 | **K2** AYNISI | nabız + yaylı küme birlikte girer (drop) |
| 25–28 | 1:00–1:10 | 0:30–0:40 | **K3** RENK YOK | ⭐ solo viyola · nabız sekizlik · en yoğun |
| 29–32 | 1:10–1:20 | 0:40–0:50 | **K4** 🔥 DÖRT YÜZ METRE | ⭐ **BOŞLUK** — nabız ve yaylılar KESİLİR |
| 33–36 | 1:20–1:30 | 0:50–1:00 | **K5** ❓ DUVAR AÇILIYOR | 💥 **DARBE** (50,000) → bantlı ton tek başına → 60,000 sert kesme |

```
⭐ ÜÇ BEDAVA HİZALAMA — ölçülmüş, tasarlanmamış:
   • DROP (ölçü 21) tam K2'nin üstüne düşüyor: nabız ve yaylı küme,
     kadraja ilk taş kopyanın girdiği karede birden giriyor.
   • SOLO VİYOLA (ölçü 25–28) bestede KAPTAN katmanıdır ve bu kesimde
     K3'ün üstüne düşüyor — yani Kaptan'ın kendi vuruşuna. Kardeş
     teslim (`FRAGMAN_DIKEY_2.md`) bu satırı "bedava olmayan tek
     hizalama" diye kaydetmişti; aynı master, farklı vuruş sırası,
     burada bedavaya geliyor.
   • BOŞLUK (ölçü 29–32) tam K4'ün, DARBE (50,000) tam K5'in ilk
     karesinin üstünde. Afiş karesi sessizlikte duruyor; duvarın
     ayrıldığı ilk saniyede tek sub darbe düşüyor. Kalan on saniyede
     BANTLI İNSAN TONU tek başına çalıyor — içinde kimse olmayan bir
     açıklığın altında.

⚠️ DÜRÜST KAYIT — bedava olmayan tek hizalama:
   Ölçü 5–8'deki GRANÜLER TAŞ DOKUSU bestede "kopya tarlası"
   katmanıdır ve bu kesimde K1'in (gemi içi, basınçsız bölme) üstüne
   düşüyor. Kadrajda taş yok. Yeniden bestelemek bu tek satır için
   müzik bütçesini sıfırdan açar.
   KARAR: bırakılıyor. Fragman katman adlarını göstermiyor; izleyici
   için orada çalan şey "boşluğun dokusu"dur.

⛔ TAM BEŞLİ SOL–RE HİÇ DUYULMAZ (bestenin kendi kilidi). Kesim
   kontrolünde duyuluyorsa kesim reddedilir.
```

## 🔊 SES TASARIMI — bu fragmana özel üç kalem

```
① İKİ SESSİZLİK REJİMİ, TEK GEÇİŞ: K0 ve K1 VAKUMDUR — bu iki vuruşta
   diegetik ses YOKTUR, yalnız müzik ve çok alçak bir kabin oda tonu
   duyulur. K2'de yüzeye çıkılır ve ince atmosfer açılır: boğuk, alçak
   rüzgar, toz. Geçiş 20,000'de, drop'un içine düşer ve kesme gibi
   değil, kapı açılması gibi duyulur.
② TEK DİEGETİK OLAY K4'TEDİR: tozun sınıra çarpıp durduğu 4,0 s'de
   çok kısık, kuru bir "bank" sesi. Müzikteki BOŞLUK'un içine düşen
   tek ses budur. Başka hiçbir vuruşta nokta efekt yok.
③ K5 SESSİZ AÇILIR: duvarın ayrılmasının SESİ YOKTUR (sahnenin kendi
   kuralı: "Menteşe yok. Ses yok."). Duyulan tek şey 50,000'deki sub
   darbe ve ardından bantlı insan tonudur. Sürtünme, tıkırtı,
   mekanizma, hava kaçağı sesi EKLENMEZ.

LUFS HEDEFİ: -12 LUFS entegre · true peak -1,0 dBTP
             (film -14'te kalır; iki hedef karıştırılmaz)
⛔ 0 kelime, 0 hece, 0 anlaşılır insan sesi — anons dahil.
```

---

# 🖼️ BÖLÜM 3 — KAPAK PROMPTU (dikey · 1080×1920)

> `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` · **metinsiz üretilir.**
> Kapak K4'ün kadrajından türer ama geri çekilir ve figürü büyütür:
> 120 px'te 400 m'lik duvar bir beyaz sütun olarak, figür bir nokta
> olarak okunur; sınır çizgisi ikisini birbirine bağlar.
> ⚠️ Kardeş kapaklarla çakışmaz: dikey 1'in kapağı topraktan çıkan
> gemi, dikey 2'ninki taştan bir suit. Bu kapak İNSAN + DUVAR.

```
Cinematic photorealistic vertical poster frame, 9:16. A basalt plain under a pale grey-green sky in soft orange daylight.
Lens: 32mm anamorphic, f/8, ISO 200. Fixed, locked off, camera height 1.5 metres, dead level, approximately eighteen metres behind the figure.

DOMINANT SUBJECT, filling the vertical axis: a 400-metre seamless one-piece tower in flawless matte white, very slightly conical, rising out of polished dead ground and leaving the top of frame long before it ends — no panel lines, no seams, no windows, no lights, no antennas, no markings, and no light of its own.

MIDGROUND: one knife-sharp boundary arcs across the plain — dusty textured basalt on the near side with a thin low dust bank drifted against the edge, smooth honed dustless stone past it, with no gradient and no blend between them. Standing on the dusty side, stopped a stride short of the line and seen from behind: a 41-year-old woman pilot, 1.68 m, slim, dark grey-blue pressure suit with ORANGE worn reinforcement, integrated helmet with a fully transparent visor, dark brown hair in a low bun, her head tipped back to look up the wall. Her long soft shadow crosses the line.

COMPOSITION: Vertical 9:16. The tower's base sits at roughly forty-eight percent of frame height and its faces fill everything above. The boundary crosses at roughly sixty-six percent. The figure runs from roughly fifty-four to sixty-eight percent on the centre vertical axis, about one seventh of frame height. The upper thirteen percent is unbroken white wall and the lower twenty-five percent is empty dusty basalt — both kept clean and low-detail for interface overlay.

LIGHTING: Small orange star low at frame left, 4400K, seventy percent of Earth daylight. Long, soft-edged shadows from the thin atmosphere. The tower holds a soft warm gradient on one face and falls to cool shadow on the other — reflected light only, never emitted.

NEGATIVE: Exactly 1 human figure — no second person, no tall figure, nobody else on the plain. The tower carries no windows at all, lit or unlit, no glass, no ports, no openings, no doors, no hatches, no vents, no balconies, no markings and no lights; it never emits light. It is not a rocket: no cylinder joints, no nosecone, no fins, no gantry, no exhaust. The boundary stays one continuous knife-sharp edge with no gradient, no blend and no glowing rim; not one grain of dust lies past it. Reinforcement stays ORANGE; the visor is fully transparent glass with zero tint and no mirror coating; the helmet stays on. No fire, no smoke, no dust plume. No bloom, no glow filter, no lens flare, no volumetric light beam, no god rays. No readable text, letters, digits, serial numbers, markings, logo or title card anywhere. No miniature look, no toy look, no CGI look. No subtitles, no captions, no watermark. Photorealistic, 35mm anamorphic film grain.
Output: 9:16, 4K, no text, no watermark.
```

```
⚠️ 120 px ELLE TEST: kapak küçültülüp 120 piksele indirilir. Görünmesi
   gereken üç şey: DİK BEYAZ SÜTUN · zeminde TEK KESKİN ÇİZGİ · çizginin
   önünde KÜÇÜK BİR İNSAN. Figür kaybolursa kamera bir adım
   yaklaştırılır (18 m → 14 m); sütun kaybolursa kadraj yukarı kaydırılır.
```

---

# 📣 BÖLÜM 4 — BAŞLIK VE AÇIKLAMA PAKETİ

> `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` · **TEASER modu.** Ekran metni
> 0,0 saniyedir [D70/D72]: film adı platform başlığında yaşar, karede
> değil. Paketleme testi §1.2'nin dördüncü maddesidir — başlık ve
> açıklama da spoiler kapısından geçer.

## Başlık adayları (A/B testi için üç varyant)

```
A · "Kimse bir gemiyi bu kadar temiz vurmaz"        ← önerilen
B · "Deliğin kenarı cam gibi — ve is yok"
C · "Menteşe yok. Ses yok."                          ← filmin kendi cümlesi

⚠️ ÜÇÜ DE KARDEŞ TESLİMLERİN BAŞLIKLARINDAN FARKLI:
   dikey 1 → "Bu gezegen düşen her gemiyi kopyalıyor" / "Enkazlar neden
             ikişer ikişer duruyor?"
   dikey 2 → "Bu gezegen dokunduğunuz her şeye cevap veriyor" /
             "Tarladaki suitlerin hiçbirinin içinde kimse yok"
   Üç teaser üç ayrı kapı açıyorsa üç ayrı başlıkla yayınlanır;
   aynı başlıkla yayınlanan iki kesim birbirinin izleyicisini yer.
   ⛔ "Cevap veren herkes ölür" bu kesimde KULLANILMAZ — iki kardeş
      teslim onu zaten paylaşıyor.
```

## Açıklama (dikey · Shorts / Reels / TikTok)

```
Bir kargo gemisinin gövdesinde bir metre yirmilik bir delik var.
Kenarı cam gibi. İs yok, çapak yok, çatlak yok.

Aşağıdaki gezegen de aynı işi yapıyor: biçimi kusursuz kopyalıyor.
Perçin yerinde, dikiş yerinde, menteşe yerinde.
Kopyalamadığı tek şey renk.

Tozun geçmediği bir sınırın ötesinde dört yüz metrelik tek parça
bir duvar duruyor. Duvarda tek bir çizgi bile yok.

THE SECOND SHIP — tam film yakında.
```

```
⚠️ AÇIKLAMA KURALI: hiçbir cümle olay dizisi vermez, Bekçi'nin
   varlığını, kopyanın insanlara da olduğunu, kulenin içini ya da
   finali ima etmez ve fragmanı "short film" diye satmaz [DERS 114].
   Yukarıdaki metin bu kapıdan geçmiştir: dört paragrafın dördü de
   bir GÖZLEM, hiçbiri bir OLAY değil.
```

---

# 📋 BÖLÜM 5 — QA SPEC BLOĞU

> Üretim bitince bu blok QA promptlarına kopyalanır (MOD D).
> Rubrikler: `1_KARE_QA_CRITIQUE_PROMPT.md (FORMAT: DİKEY)` (kurgu) ·
> `1_KARE_QA_CRITIQUE_PROMPT.md` (teknik) ·
> `2_DEVAMLILIK_QA_CRITIQUE_PROMPT.md` (yalnız video)
> ⛔ SENARYO_QA bu dosyaya KOŞULMAZ [FRAGMAN_KILAVUZU §0 · §5.1].

```
SPEC — THE SECOND SHIP · ÜÇÜNCÜ DİKEY FRAGMAN

FORMAT:        dikey 9:16 · 6 vuruş × 10,000 s = 60,000 s
MEKANİK:       KUSUR YOK — her vuruşta kadraja hatasız yapılmış bir iş
               girer; kırılma K3'te (renk kopyalanmıyor)
KESME:         her vuruş tek çekim, 0 kesme; kesmeler klip aralarında
KAMERA:        6/6 tam lockoff — hiçbir vuruşta hareket yok
DİYALOG:       0 replik, 0 kelime, 0 insan sesi
KADRO SAYILARI: K0=0 · K1=1 insan (Mühendis) · K2=0 · K3=1 insan
               (Kaptan; kol, omuz, yumuşak profil) · K4=1 insan
               (Kaptan, sırttan, küçük) · K5=0
               ⭐ BEKÇİ 0 KARE — hiçbir parçası, gölgesi ya da silueti yok
               ⭐ hiçbir karede iki insan yok
KİMLİK KİLİDİ: Kaptan 1,68 m, TURUNCU takviye, topuz, SOL kaşta yara izi,
               vizör şeffaf
               Mühendis 1,81 m, TEAL YEŞİL takviye, SAĞ elmacıkta 2 cm
               yanık izi, sırt alet modülü, vizör şeffaf
ÖLÇEK KİLİDİ:  delik 1,2 m · Mühendis 1,81 m · taş bacak insan boyunda ·
               kule 400 m · yarık 4 m × 1 m · Kaptan 1,68 m
HASAR KİLİDİ:  delik KUSURSUZ DAİRE, kenar düz ve sedefli — is, çapak,
               çatlak, eğrilmiş dudak, ikinci delik YOK; gövdenin
               kalanı SAĞLAM
MALZEME KİLİDİ: kopya materyali mat kemik grisi taş — parlamaz,
               ışık yaymaz, orijinalin rengini TAŞIMAZ
KULE KİLİDİ:   400 m, tek parça, dikişsiz, mat beyaz; pencere, kapı,
               menteşe, ray, kemer, işaret, lamba YOK; roket DEĞİL.
               K5'te açıklık düz kenarlı DİKEY YARIK, ötesi okunmaz beyaz
BÜYÜME KİLİDİ:  büyüme gerçek zamanda GÖRÜNMEZ. Bu fragmanda İSTİSNA YOK:
               zemin altı vuruşun altısında da hareketsiz
FİZİK:         K0 vakum · K1 basınçsız bölme · K2/K3/K4/K5 0.9g,
               0.6 atm ince atmosfer · toz çöker ve oturur ·
               yüzeyde gölge kenarları yumuşak
IŞIK:          K0 7000K ay sıyırma · K1 yalnız 2 kask lambası 5600K ·
               K2/K3/K4 4400K soldan yayvan · K5 4400K dışarı +
               5600K düz beyaz içeri, eşikte harmanlanmadan
METİN:         hiçbir karede okunabilir harf, rakam, gemi işareti,
               gösterge değeri, altyazı, başlık kartı ya da filigran yok
MÜZİK:         `FRAGMAN.md` BÖLÜM 3 masterının dikey kesimi ·
               96 BPM · Sol minör · tam beşli HİÇ duyulmaz ·
               boşluk 40,000–50,000 · tek sub darbe 50,000'de ·
               fade yok, sert kesme · -12 LUFS
LOOP:          60,000 → 00,000. K5 yarığı (%26–%72, orta eksen, parlak)
               → K0 deliği (%38–%50, orta eksen, koyu)
SPOILER KAPISI: Bekçi (her parçası), Bekçi'nin yüzü ve replikleri,
               Kaptan'ın kopyası, ölü asıl, kule içi, doğrulama plakası,
               kalkış, final, ikinci geminin tam gövdesi, zeminin
               kabarması — hepsi 0 kare
```

---

# ✅ BÖLÜM 6 — ÜRETİM SIRASI VE KONTROL LİSTESİ

## 🚦 ÜRETİM SIRASI — kapılar

```
KAPI 1 · K5 — "DUVAR AÇILIYOR" (button + loop + 1 numaralı risk)
   6 varyasyon. Kabul: on saniyenin her karesinde açıklık DÜZ KENARLI
   ve PARALEL KENARLI; kemer, yuvarlatma, menteşe, ray, kayan plaka,
   çerçeve ya da görünür kalınlık YOK; yarığın ötesinde zemin çizgisi,
   duvar, derinlik, nesne ya da figür YOK; duvarda ikinci bir açıklık,
   pencere, dikiş ya da işaret belirmiyor.
   ⛔ TUTMAZSA HİÇBİR ŞEY ÜRETİLMEZ (sapma ⑨).

KAPI 2 · K4 — "DÖRT YÜZ METRE" (afiş + kapak kaynağı)
   6 varyasyon. Kabul: sınır tek, sürekli ve bıçak keskinliğinde —
   degrade, harman, geçiş bandı yok; cilalı tarafta tek tane toz yok;
   kule hiçbir karede pencere, kapı, işaret ya da ışık üretmiyor ve
   roket siluetine kaymıyor; figür kadraj yüksekliğinin ~%11'i.

KAPI 3 · K0 — "DELİK" (hook + loop dikişinin öteki ucu)
   4 varyasyon. Kabul: daire kusursuz ve tam 1,2 m; kenar düz, temiz,
   sedefli; is, çapak, çatlak, eğrilmiş dudak, ikinci delik YOK;
   delikten hiçbir şey çıkmıyor; gövdenin kalanı sağlam.

Üç kapı geçilmeden K1, K2 ve K3 üretilmez.
Sonra sırayla: K2 (B yolu, en ucuz) → K3 → K1.
```

## 💰 BÜTÇE TAHMİNİ

```
6 klip × 10 s, sessiz üretim
  tek geçiş                                     ~$6
  gerçekçi (~3 deneme/klip)                    ~$18
  üç kapının ek varyasyonları (6+6+4)          ~$11
  8 s → 10 s extend (A yolu · K1, K3, K4, K5)   ~$6
                                               ─────
                                               ~$35 + 6 imaj + 1 kapak
                                               müzik: $0 (mevcut master)

⚠️ B yolu (retime 0,8×) yalnız K0 ve K2'de serbesttir; ikisinde de
   extend kalemi düşer.
⚠️ Bu fragman iki kardeş teslimden de UCUZDUR: Bekçi hiç üretilmiyor
   (anatomi varyasyonları sıfır), iki insanlı kare yok, yeni müzik yok.
```

## ✅ TESLİM ÖNCESİ KONTROL LİSTESİ

```
KADRAJ
 □ Altı vuruşun altısı da 9:16 SIFIRDAN üretildi mi (kırpılmış kare var mı)
 □ Her karede anlam %13–%75 bandında mı, alt çeyrek boş mu
 □ Sağ %12,5 sütunu her karede temiz mi
 □ K2'de çatlaklar %70'in üstüne taştı mı — taşmamalı
 □ K4'te figür arayüz butonlarının altında kaldı mı — kalmamalı

HASAR VE MALZEME
 □ K0/K1'de delik tam daire mi, kenar temiz mi, is/çatlak var mı [D38]
 □ K1'de el deliğin kenarına değdi mi — değmemeli [D11/43]
 □ K2'de bacağın kökünde dikiş, boşluk ya da gölge çizgisi var mı
 □ K3'te parmak taşa battı mı, iz bıraktı mı, taş ısındı mı
 □ Taş herhangi bir karede parladı mı, renk aldı mı [D3/29]

KULE
 □ K4/K5'te pencere, kapı, kemer, işaret, lamba belirdi mi
 □ K5'te menteşe, ray, kayan plaka, çerçeve, kalınlık var mı
 □ K5'te yarığın ötesinde okunabilir bir şey göründü mü — görünmemeli
 □ K4'te sınır tek ve keskin mi, cilalı tarafa toz geçti mi

SÜREKLİLİK VE KİMLİK
 □ K1'de takviye TEAL, yanık izi SAĞ elmacıkta mı
 □ K3/K4'te takviye TURUNCU, yara izi SOL kaşta mı
 □ Vizörler her karede şeffaf mı, tint/ayna kaplaması var mı [D5/79]
 □ Sırt ünitesi yalnız K1'de ve yalnız Mühendis'te mi
 □ ⭐ Herhangi bir karede Bekçi ya da ikinci bir insan belirdi mi

METİN VE ARAYÜZ
 □ Okunabilir harf/rakam/gemi işareti/gösterge değeri var mı [D13]
 □ Altyazı, başlık kartı, jenerik kartı, filigran var mı

SES VE MÜZİK
 □ Hiç kelime duyuluyor mu — duyulmamalı
 □ K0/K1'de diegetik ses var mı — olmamalı (vakum)
 □ K5'te duvarın açılma sesi eklendi mi — eklenmemeli
 □ Boşluk 40,000'de mi, darbe 50,000'de mi · tam beşli Sol–Re duyuluyor mu
   ⛔ duyuluyorsa kesim reddedilir
 □ -12 LUFS mi (film hâlâ -14 mü)
 □ 60,000'de sert kesme mi, fade var mı

SPOILER VE PAKETLEME
 □ Dokuz yasak kalemden herhangi biri kadraja girdi mi
 □ TEK CÜMLE TESTİ: kurguyu ilk kez izleyen biri tamamlanmış bir hikaye
   anlatıyor mu — anlatıyorsa fragman çökmüştür, teslim edilmez
 □ Başlık kardeş teslimlerin başlığıyla aynı mı — olmamalı
 □ Açıklama olay dizisi veriyor mu, "short film" diyor mu [D114]

LOOP
 □ 60,000 → 00,000 dikişsiz mi: K5'in yarığı ile K0'ın deliği üst üste
   bindirildiğinde delik yarık bandının içine düşüyor mu (%38–50 ⊂ %26–72)
```

---

# 📌 SONRAKİ ADIMLAR

```
✅ FRAGMAN_DIKEY_3.md                ← bu dosya
□ Görev kartı P (PROMPT KONTROL) — üretimden ÖNCE, sıfır kare tüketir:
    python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
      yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_DIKEY_3.md
□ Rubrik: PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md (betiğin
  göremediği tek şey: kilit SAYI mı TARİF mi)
□ Kaynak filmin REFERANS_PAKETI seed'leri hazır mı — R1 (Kaptan),
  R2 (Mühendis), R4 (CANTOR hasarlı). Bekçi plakası bu fragmanda
  KULLANILMAZ.
□ Üç kapı sırayla üretilir (yukarıdaki ÜRETİM SIRASI · K5 → K4 → K0)
□ Müzik: yeni üretim YOK — mevcut 90 s masterın dikey kesimi
□ Kapak: dikey, metinsiz, 120 px elle test
□ Üretim bitince → QA SPEC bloğu SHORTS_QA ve VIDEO_QA'ya verilir
□ Ham raporlar önce 02_HAM_RAPORLAR/ altına kaydedilir [kural ④]
□ Koşu tuttuysa → FRAGMAN_KILAVUZU §1.3b'ye "üçüncü teslim" satırı
  (sapma ⑥) ve emsal listesine bu dosya eklenir
```
