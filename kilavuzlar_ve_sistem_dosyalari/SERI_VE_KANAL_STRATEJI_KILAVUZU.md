# 🛰️ SERİ VE KANAL STRATEJİ KILAVUZU — Filmden Evrene

> **Neden var (22.08.2026):** Depodaki her film kendi evrenini kurup
> atıyor. Hiçbir belge iki film arasındaki izleyici taşımasını
> konuşmuyordu: devam filmi karar kuralı yok, filmler ARASI bible
> taşıma kuralı yok, kapak aile kimliği yok, yayın kadansı yok.
> `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` "CHANNEL CONTEXT" soruyor ama
> kanalın kendisi için sistem dosyası yoktu.
>
> **Mekanizma:** Öneri motorları "birlikte ziyaret" (co-visitation)
> bağlarına dayanır. Birbirinden bağımsız N film, ağda birbirine zayıf
> bağlarla bağlı N izole düğüm demektir — birini izleyene diğerini
> önermek için sebep yoktur. Aynı evrenin filmleri ardışık izlenince
> bu bağlar kalınlaşır ve kanalın kendi içeriği kendi önerisi olur.
>
> **Ne zaman okunur:** ① yeni film konsepti seçilirken (bağımsız mı,
> evrene mi bağlı) ② yayın planı yapılırken ③ geçmiş filmler taranıp
> devam adayı seçilirken.
> Kaynak: `araştırmalar/4.md` (22.08.2026 derin araştırması).

---

# 0. ⚠️ DÜRÜST KAYIT — bu kılavuzun sınırları

```
① BU KANALIN HİÇ YAYIN VERİSİ YOK. §4'teki devam hakkı eşikleri dış
   kaynaktır ve İLK KOŞULARDA UYGULANAMAZ — "ilk 1 saatte 100+ yorum"
   gibi bir eşik sıfır aboneli kanalda hiçbir filmin geçemeyeceği
   bir kapıdır. Başlangıç için §4.2'deki İKİ KRİTERLİ indirgenmiş
   kapı kullanılır; dört kriterli tam kapı, kanal düzenli gösterim
   almaya başladığında açılır.

② DEPO ZATEN BİR EVREN ÜRETİYOR — farkında olmadan.
   Ortak fizik kuralları, ortak negatif çekirdek, ortak görüntü kimliği
   (sinema grade + lockoff + tek çekim), ortak adlandırma kalıbı
   (THE + iki kelime) ve ortak karakter tipi (kasklı, yalnız, sayaçla
   yarışan insan). Bu bir marka imzasıdır; eksik olan şey ÇATI ve
   filmler arası GÖRÜNÜR bağdır. Kılavuz sıfırdan evren kurmuyor,
   var olanı görünür kılıyor.

③ SERİ ÜRETİMİ FİLM SAYISINI DEĞİL, FİLM BAŞINA MALİYETİ DEĞİŞTİRİR.
   Aynı evrende ikinci film, bible'ın yeniden kullanılması sayesinde
   daha ucuzdur — ama §2'deki taşıma kuralları uygulanmazsa yüz ve
   ölçek kayar ve tasarruf zarara döner.

④ BU KILAVUZ HİÇBİR FİLMİ GERİYE DÖNÜK DEĞİŞTİRMEZ. Yayınlanmış
   filmlere devam yazmak ayrı bir karardır; §4 kapısından geçmeyen
   hiçbir filme devam yazılmaz.
```

---

# 1. 🧬 MODEL SEÇİMİ — bağımsızlık zorunludur

İki seri modeli vardır ve bu depo için yalnız biri işler.

```
❌ ZİNCİR MODELİ ("önceki bölümü izlemeden anlaşılmaz")
   4. bölüm milyonlarca yeni kişiye önerildiğinde bağlamı bilmeyen
   kitle ilk saniyelerde çıkar; izlenme süresi çöker ve algoritmik
   yayılım durur. Yeni izleyici için "geç kaldım" bariyeri CTR'ı düşürür.

✅ EVREN MODELİ ("aynı dünya, bağımsız hikayeler")
   Her film aynı fizik kurallarını, aynı görsel dili ve aynı temayı
   paylaşır; ama kendi girişi, gelişmesi ve TATMİN EDİCİ SONU vardır.
   İzleyici bunun bir evrenin parçası olduğunu filmin ortasında veya
   sonunda fark eder — hikayeye çekildikten SONRA.
```

```
SAYISAL KİLİT — BAĞIMSIZ İZLENEBİLİRLİK
  □ Filmi hiç bilmeyen bir izleyici için ÖN BİLGİ gereksinimi: 0 sahne
  □ Önceki filme yapılan açık gönderme: ≤ 1 ve filmin ANLAŞILMASI
    için gerekli DEĞİL (fark edilirse ödül, edilmezse kayıp yok)
  □ Filmin kendi çatışması kendi içinde ÇÖZÜLÜR — açık uç yalnız
    tema düzeyinde bırakılır, olay düzeyinde değil
```

⚠️ Bu kilit, `FRAGMAN_KILAVUZU.md` §1.2 spoiler kapısının kardeşi ve
tersidir: fragman bilgiyi SAKLAR, seri filmi bilgiyi TAMAMLAR. Bir
filmin sonunu sonraki filme borçlu bırakmak bu seride yasaktır.

---

# 2. 🔗 EVREN ÇATISI — filmler arası ne taşınır

Aynı evrenin ikinci filmi yazılırken taşınan şeyler ve taşınma biçimi.
Tek film içi çapalama `SAHNE_DEVAMLILIK_KILAVUZU.md`'de; bu bölüm
filmler ARASI çapalamadır.

```
KELİMESİ KELİMESİNE TAŞINIR (kopyala-yapıştır, değiştirme)
  □ Ortam kartı sayıları: basınç, yerçekimi, ışık sıcaklığı, gökyüzü
  □ Suit / ekipman tanımı: renk, malzeme, vizör tipi, sayısal ölçüler
  □ Tekrar eden varlığın kimlik kartı [D58]: araç, yapı, canlı —
    renk + boyut + doku + hasarın YERİ
  □ Negatif çekirdek (zaten her prompta giriyor)

YENİDEN YAZILIR (aynı evren, farklı hikaye)
  □ Karakter — aynı ROL tipi, farklı kişi. Aynı yüzü ikinci filmde
    taşımak isteniyorsa REFERANS PAKETİ zorunludur (yalnız 3-5 dk ve
    7-9 dk formatlarında emsali var)
  □ Mekan, olay, sayaç, çatışma

⛔ TAŞINMAZ
  □ Çözülmüş çatışma ve final imajı
  □ Önceki filmin doruğunu açıklayan bilgi (yeni izleyiciye spoiler)
```

```
EVREN DOSYASI — ikinci filmle birlikte açılır
  <EVREN_ADI>_EVREN_BIBLE.md   ortam + varlık + görsel dil kartları
  ⭐ Evrenin ÇEKİRDEĞİ novumdur: aynı evrenin filmleri aynı yeni kuralı
    paylaşır, farklı sonuçlarını gösterir → ONERME_VE_NOVUM_KILAVUZU.md
    Novumu paylaşmayan iki film aynı evrende değildir, yalnız aynı
    ortam kartını kullanıyordur.
  → Her filmin PLAN'ı bu dosyaya ATIFTA BULUNMAZ, İÇİNDEN KOPYALAR.
    Prompt self-contained kuralı [AGENTS §2③] evren dosyası için de
    geçerlidir: "[EVREN BIBLE'a bak" yasak.
```

---

# 3. 🎨 KANAL KİMLİĞİ — kapak, ad, açıklama

## 3.0 ⭐ HANGİ KİMLİK KALDIRACI ÖLÇÜLDÜ, HANGİSİ VARSAYIM

> **Eklendi 27.08.2026 (araştırma 4).** Bu bölümün altındaki kurallar
> doğru ama hepsi aynı ağırlıkta değildi. Antoloji yapısı — her filmde
> farklı karakter, farklı dünya — tanınabilirliği kimliğe yıkar; bu
> tablo hangi kaldıracın gerçekten ölçüldüğünü ayırır.

| Kaldıraç | Durum | Ölçüm |
|---|:--:|---|
| **Kapak ailesi** (tutarlı iskelet + yüksek kontrast) | ✅ ÖLÇÜLDÜ | ortalama CTR'a **+%35'e kadar** katkı |
| **Renk imzası** (evren başına sabit palet) | ✅ ÖLÇÜLDÜ | tutundurma metriklerinde iyileşme; görsel marka belleği |
| **Ses imzası** (orijinal, kanala özgü) | ✅ ÖLÇÜLDÜ | YouTube 03/2026: **<50k abonelik kanallarda "orijinal ses bonusu"** — trend ses yerine kendi imzasını kullanan kanal ölçülebilir erişim artışı alıyor |
| **Başlık grameri** ("THE + iki kelime") | ⚠️ VARSAYIM | SEO faydası kabul görüyor; sadakat kurduğuna dair izole test **YOK** |
| **Açılış kadrajı** (aynı kamera grameri) | ⚠️ VARSAYIM | ilk 3 saniyenin kritikliği gerçek; belirli bir açının afinite ürettiği **ölçülmedi** |

```
KANAL AFİNİTESİ EŞİĞİ — algoritmanın "sadık izleyici" saydığı nokta
  ~15 oturum   VEYA   7 günde dönen izleyici oranı > %15

→ Bu eşik, §4'ün DEVAM HAKKI kapısından ÖNCE gelir: eşik geçilmeden
  hiçbir filmin "seriye dönüşme" verisi okunamaz.
```

> ⛔ **VE BİR ÇELİŞKİ KAYDA GEÇİYOR — karar proje sahibinindir.**
> `SHORTS_SISTEM_PROMPTU` viral DNA madde 4: *"Aynı paleti başka bir
> konsept için tekrar kullanma."* Bu bölüm §3.1: *"RENK KODU: evren
> başına 2 ana renk, tüm kapaklarda aynı."* İkisi aynı anda uygulanamaz.
> Ölçüm renk imzasından yana ama madde 4'ün gerekçesi de gerçek
> (16 film, 16 farklı dünya — palet tekrarı tembellik okunabilir).
> **Önerilen çözüm — iki katmana ayır:**
> ```
> KANAL KATMANI   sabit: 2 imza rengi + sabit kompozisyon iskeleti
>                 → kapakta ve filmin ilk/son karesinde görünür
> FİLM KATMANI    özgün: kalan 2-3 renk konsepte özel, tekrar etmez
>                 → filmin gövdesinde çalışır (madde 4 burada geçerli)
> ```
> Bu çözüm uygulanana kadar iki kural çelişmeye devam eder; bir sonraki
> ajan birini sessizce silmesin.

## 3.1 KAPAK AİLE KİMLİĞİ

Yüz olup olmaması küçük kanallarda CTR'ı belirlemiyor; belirleyen şey
**tanınabilirlik**. Sabit kompozisyon iskeleti + sabit renk kodu,
rastgele tasarlanmış kapaklara göre belirgin CTR farkı üretir ve
video soğuk kitleye açıldığında yaşanan CTR düşüşünü frenler.

```
SAYISAL KİLİT — her kapakta AYNI kalan üç şey
  □ KOMPOZİSYON İSKELETİ: figürün kadraj içindeki yeri sabit
    (öneri: sol veya sağ üçte bir · figür kadraj yüksekliğinin ≤%25'i)
  □ RENK KODU: evren başına 2 ana renk, tüm kapaklarda aynı
  □ İMZA UNSURU: her kapakta evrene ait aynı sembol/siluet/nesne tipi
  □ Değişen tek şey: olay, mekan, ışık şiddeti

⛔ Kapak METİNSİZ üretilir; tipografi post'ta eklenir — mevcut kural
   değişmedi (KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU). Aile kimliği
   tipografiyle DEĞİL, kompozisyon ve renkle kurulur.
   120 px posta pulu testi her kapakta ayrıca koşulur.
```

## 3.2 ADLANDIRMA MİMARİSİ

```
⭐ DEPO ZATEN BİR AİLE ADINA SAHİP: "THE + iki kelime" kalıbı tüm
   filmlerde tutuyor. Bu kalıp KORUNUR — kanal imzasının yarısı bu.

PLATFORM BAŞLIĞI — üç kural
  □ İlk 50-60 karakter (ekranda kesilmeden görünen kısım) VAADİ taşır
  □ Seri adı ve bölüm numarası SONA veya açıklamanın ilk satırına gider
  □ ⛔ "Bölüm 3:" ile BAŞLAYAN başlık yazılmaz — yeni izleyiciye
     "geç kaldım" bariyeri kurar

  ✅ <VAAT / MERAK CÜMLESİ> | <EVREN ADI> (Bölüm 3)
  ❌ Bölüm 3: <vaat>

  İSTİSNA: tamamlanma motivasyonu istenen kapalı diziler için
  "1/4 · 2/4" biçimi dönüşümü artırır — yalnız baştan sonu belli,
  kısa ve kapalı bir dizide kullanılır.
```

## 3.3 FORMAT RİTÜELİ

Her bölümün aynı görsel ve işitsel imzayla açılıp kapanması, izleyicide
tanıma refleksi kurar ve bu serinin yapaylık riskini stilistik tercihe
çevirir.

```
□ AÇILIŞ RİTÜELİ: aynı ses imzası (tek ton / basınç tıslaması / sayaç
  sesi) filmin ilk 1-2 saniyesinde — HOOK §5 ile aynı yuva
□ KAPANIŞ RİTÜELİ: aynı final imaj TİPİ (ölçek kontrastı 1:10 —
  KARAKTER_VE_DUYGU §5.1) her filmde tekrarlanır
□ ⛔ Ritüel EKRAN METNİ İÇEREMEZ: jenerik, logo, başlık kartı ve
  kanal adı 0,0 saniyedir [D61/70 · kurgu kapısı madde ③].
  Ritüel görsel-işitseldir, yazılı değildir.
```

---

# 4. 🚦 DEVAM HAKKI — hangi film seriye dönüşür

> Geçmiş filmler harcanmış emek değil, **pilot bölüm havuzudur.**
> Devam kararı beğeniyle değil veriyle verilir.

## 4.1 TAM KAPI — kanal gösterim almaya başladığında

| Kriter | Eşik | Ne kanıtlar |
|---|:--:|---|
| İlk 10 sn tutunma | **> %70** | Kanca çalışıyor — evrenden bağımsız |
| Ortalama görüntülenme (AVD/APV) | **> %50** | İzleyici o evrene yatırım yaptı |
| Erken etkileşim | ilk saatte yoğun ve **derin** yorum | Evren tartışılıyor, teori üretiliyor |
| Bitiş ekranı tıklama | **> %5** | İzleyici taşınabiliyor — co-visitation'a hazır |

```
⭐ NİTELİK > NİCELİK: izleyicilerin evren hakkında teori ürettiği,
   soru sorduğu, geçmişi tartıştığı bir film; çok sayıda tek kelimelik
   yorum alan filmden daha güçlü bir devam adayıdır. Yorum tarama
   ölçütü: "kaç kişi bu dünyayı MERAK ETTİ".
```

## 4.2 İNDİRGENMİŞ KAPI — ilk yayınlar için (şu an geçerli olan)

```
Kanal düzenli gösterim almaya başlayana kadar YALNIZ iki kriter:
  □ İlk 10 sn tutunma > %70
  □ AVD/APV > %50
Bu ikisi 3 farklı filmde ölçüldükten SONRA dört kriterli kapıya geçilir
— tek filmden devam kararı verilmez (ölçüm sapması kuralı, AGENTS §2⑥).

KAPIYI GEÇEN FİLM  → 3-5 bölümlük mini evren sırasına alınır
KAPIYI GEÇMEYEN    → devam YAZILMAZ. Kanca zayıfsa evren genişletilmez;
                     önce S0-S1 mimarisi revize edilir (HOOK §8).
```

## 4.3 GEÇMİŞ KÜTÜPHANE TARAMASI

```
□ Yayınlanmış filmler §4.2 ile puanlanır ve sıralanır
□ Zaten aynı ORTAM kartını paylaşan filmler gruplanır — evren adayı
  çatılar buradan çıkar (ortak ortam = ortak fizik = ucuz genişleme)
□ En yüksek AVD'li film çatının BİRİNCİ bölümü olarak konumlanır
  (kronoloji zorunlu değilse); en eski/en zayıf film asla giriş
  noktası yapılmaz
□ Sonuç: 08_YAYIN_PERFORMANS_TABLOSU.md'ye "evren adayı" sütunu
```

---

# 5. 📺 DAĞITIM — playlist, köprü, kadans

## 5.1 PLAYLIST VE RESMİ SERİ

```
□ Her evren için TEK playlist açılır
□ Platformun "resmi seri" ayarı işaretlenir — öneri motoruna
  "bunlar ardışık tüketilmek için tasarlandı" sinyali gider ve
  sıradaki video aynı evrenden gelme ihtimali yükselir
□ ⛔ BİR VİDEO YALNIZ TEK resmi seride yer alabilir → her filmin
  ait olduğu ana evren TEK SEFERDE seçilir ve tabloya yazılır
□ Playlist'in İLK sırası = en yüksek AVD'li film (§4.3)
```

## 5.2 BÖLÜM SONU KÖPRÜSÜ

```
❌ Veda kapanışı ("abone olmayı unutmayın") — izleyiciye ayrılma izni verir
✅ Değer teslim edildiği anda kesme + sonraki bölüme görsel geçiş

BU SERİDEKİ BİÇİMİ — ekran metni yasağı içinde:
  □ Film kendi final imajında biter (ritüel · §3.3)
  □ Köprü FİLMİN İÇİNDE DEĞİL, platform katmanındadır:
    bitiş ekranı kartı + playlist otomatik geçişi + açıklama ilk satırı
  □ Filmin son karesi, bitiş ekranı kartının üstüne binebileceği
    SAKİN ve okunaklı bir kadraj olur (ölçek kontrastı planı bunun
    için idealdir — figür küçük, kadrajın kalanı boş)
  □ ⛔ Filmin içine "sonraki bölüm" yazısı, logo veya kart KONMAZ
```

## 5.3 YAYIN KADANSI

```
SIKLIK DEĞİL, İSTİKRAR ÖDÜLLENDİRİLİR.
  □ Sabit bir kadans seçilir: HAFTALIK veya İKİ HAFTADA BİR
  □ Kadans tabloya yazılır ve değişirse kaydedilir
  □ Seyrek ama yüksek kaliteli üretim cezalandırılmaz — düşük
    tutunmalı sık üretim, yüksek tutunmalı seyrek üretimi yenemez
  □ ⭐ Bu depo için doğal sonuç: film sayısını artırmak değil,
    yayın ritmini sabitlemek. Yazılmış ama yayınlanmamış film stoğu
    kadansın yakıtıdır — hepsini aynı anda yayınlamak stoğu yakar
```

---

# 6. ⛔ ARAŞTIRMADAN DEPOYA GEÇMEYENLER — dürüst kayıt

| Araştırmadaki öneri | Neden geçmedi |
|---|---|
| Bölüm başında "geçen bölümde…" özet kurgusu | Ekran metni ve anlatıcı dış ses bu seride yok; ayrıca §1 bağımsız izlenebilirlik kilidi özeti gereksiz kılar. Bağlam açıklamanın ilk satırında verilir. |
| Ekranda tipografi animasyonlu açılış ritüeli | Ekran metni 0,0 sn [D61/70]. Ritüel görsel-işitseldir (§3.3). |
| Her videoda tekrarlayan anlatıcı / sinik dış ses | Register haritası ve replik bütçesi ayrı kısıt; dış ses bu serinin dili değil. Tekrar eden unsur KARAKTER TİPİ ve EVREN KURALLARIDIR. |
| Kapakta abartılı yüz ifadesi | Küçük kanalda yüzün CTR etkisi marjinal; belirleyici olan aile kimliği (§3.1). Ayrıca bu seride yüz kask altındadır. |
| Filmin içine bitiş kartı / sonraki bölüm kartı | Kurgu kapısı madde ③: ekran metni 0,0 sn — altı vakada bu yasak çiğnendi. Köprü platform katmanında kurulur (§5.2). |

---

# 7. ✅ KONTROL LİSTESİ

```
YENİ FİLM KONSEPTİ SEÇİLİRKEN
 □ Bu film bağımsız mı, var olan bir evrene mi bağlanıyor
 □ Evrene bağlanıyorsa: EVREN_BIBLE'dan taşınacaklar kopyalandı mı (§2)
 □ §1 bağımsız izlenebilirlik kilidi sağlanıyor mu (ön bilgi = 0 sahne)
 □ Kapak aile kimliğinin üç sabiti planlandı mı (§3.1)

YAYINDAN ÖNCE
 □ Başlık mimarisi §3.2'ye uygun (bölüm numarası başta değil)
 □ Evren playlist'i var mı, film doğru playlist'e eklendi mi
 □ Resmi seri işaretlemesi yapıldı mı (film TEK seride)
 □ Bitiş ekranı kartı hangi filme gidiyor — kararlaştırıldı mı
 □ Son kare bitiş ekranı kartını taşıyacak kadar sakin mi

DEVAM KARARI VERİLİRKEN
 □ §4.2 indirgenmiş kapı 3 filmde ölçüldü mü
 □ Kapıyı geçen film mini evren sırasına alındı mı
 □ Karar 08_YAYIN_PERFORMANS_TABLOSU.md'ye yazıldı mı
```

---

# 8. 📚 KAYNAKLAR

```
araştırmalar/4.md                      bu kılavuzun kaynak araştırması (22.08.2026)
YAYIN_VE_PERFORMANS_KILAVUZU.md        §4 eşiklerin ölçüldüğü yer · koşu kaydı
FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md  evren adayı sütunu
KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md   kapak psikolojisi · 120 px testi · Plan B
VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md     platform başlığı ve açıklama üretimi
FRAGMAN_KILAVUZU.md                    §1.2 spoiler kapısı — §1'in kardeş kuralı
SAHNE_DEVAMLILIK_KILAVUZU.md           tek film içi çapalama (bu dosya filmler ARASI)
KILAVUZ_REHBERI.md §3                  ortam kartları — evren gruplamasının temeli
KARAKTER_VE_DUYGU_KILAVUZU.md          §5.1 ölçek kontrastı — kapanış ritüelinin kaynağı
```
