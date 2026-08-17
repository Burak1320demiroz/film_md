# 🪨 THE STONE SKY — Taş Gökyüzü

## AI Production Bible — Full Format V3 (Self-Contained Prompts · Sahne İçi Kesme)

### 14 Sahne × 10 s = 140 s | 21 Segment · 7 Kesme (sahne başına en çok 1) | 16:9 Yatay | İnce Atmosfer | Bilimkurgu

### _"Bu ayda yanardağ taşları gökyüzüne atar. Gökyüzü onları bir çember hâlinde geri verir — ve çember dıştan içe kapanır."_

---

# 🧭 BÖLÜM 0 — PLAN

> Bu bölüm `KILAVUZ_REHBERI.md` §6 adım 1'dir ve üretimden önce yazıldı.
> Sıralama: PLAN → BIBLE → PLAN KONTROL → PROMPT.

## 0.1 DÖRT SORU

```
① YÖN?    yatay 16:9
② SÜRE?   2-4 dk  → 14 sahne × 10 s = 140 s (2:20)
③ TÜR?    bilimkurgu     → KILAVUZ_REHBERI §4.1 + UZAY_SENARYO_KILAVUZU
④ ORTAM?  ince atmosfer  → KILAVUZ_REHBERI §3.2 + Ders 39, 41
           referans film: THE_DAWN_FRONT (aynı ortam kartı + sahne içi
           kesme mimarisinin ilk uygulaması — bu film o mimarinin
           SADELEŞTİRİLMİŞ sürümüdür: sahne başına en çok 1 kesme)
```

**Ortam neden ince atmosfer:** Filmin bütün mekaniği **balistik**tir — taşlar
çıkar, kavis çizer, düşer. Bu ancak sürtünmesiz-gibi seyrek havada temiz
çalışır: jetler iğne keskinliğinde kalır, taş yörüngeleri sapmasız kavistir
ve düşme HARİTASI önceden okunabilir. Kalın atmosferde taşlar savrulur ve
halka bulanır; vakumda kalkan toz hiç oturmaz ve final sahnesinin "toz
çöküyor" görüntüsü imkânsızlaşır. Fizik tam olarak §3.2 kartıdır.

---

## 0.2 ⭐ KESME MİMARİSİ — sahne başına EN ÇOK BİR kesme

> THE_DAWN_FRONT bu depoda sahne içi kesmeyi açtı: 26 segment, 12 kesme,
> sahne başına 2 kesmeye kadar. Bu film aynı mimariyi **bilinçli olarak
> yarıya indiriyor:** her sahne ya TEK ÇEKİMDİR ya da TEK kesme taşır.

### Neden en çok 1 kesme

```
DAWN FRONT'UN RİSKİ   Referanssız segment. İmaj promptu yalnız A
                      segmentini bağlar; B ve C'yi model yorumlar.
                      2 kesmeli sahnede referanssız segment SAYISI 2.

BU FİLM               2 kesmeli sahne YOK. En kötü durumda tek
                      referanssız segment var (B) ve onun kurulumu
                      video promptunda kelimesi kelimesine yazılı.
                      Referanssız segment sayısı sahne başına en çok 1,
                      film genelinde 7.

KURAL                 7 sahne × 1 kesme + 7 sahne × 0 kesme
                      = 21 segment · 7 kesme
```

### ⛔ EN KRİTİK KURAL — "no cuts" nerede durur, nerede durmaz

```
Kontrol listesi A1 (deponun en pahalı hatası): "Aynı dosyada hem YASAK
hem ANLATIM varsa model YASAĞI seçer, anlatım sessizce ölür."

  TEK ÇEKİMLİ 7 SAHNE  (S1 · S3 · S5 · S7 · S9 · S12 · S13)
    → "Single unbroken take: no cuts..." cümlesi AYNEN durur.

  TEK KESMELİ 7 SAHNE  (S0 · S2 · S4 · S6 · S8 · S10 · S11)
    → o cümle promptta YOKTUR. Yerine:
      "CUT SCHEDULE: exactly one hard cut, at X.Xs, and no others.
       Each of the two segments is a single unbroken locked-off take
       with no camera movement inside it. No dissolve, no fade, no
       wipe, no morph, no speed ramp at the cut."
```

### 0.2.1 KESME GRAMERİ — DAWN FRONT'un yedi kuralı, devralınan hâliyle

```
① EKSEN KİLİDİ — 21 segmentin 21'inde koni/tehlike kadrajın SOLUNDADIR.
   Dışa kaçış SAĞA doğru akar (S0-S7); S8'deki ters dönüşten sonra
   hareket SOLA doğrudur — ama koni hiçbir karede sağa geçmez.
   180° kuralı hiç ihlal edilmez; değişen tek şey hareket yönüdür ve
   o değişim filmin dorukdaki anlamıdır (ters simetri).
② 30° / ÖLÇEK KURALI — her kesmede ya ≥30° açı ya ≥1 tam ölçek kademesi
   farkı vardır; sahnenin KESME PLANI bloğunda yazılıdır.
③ HAREKET ÜZERİNDE KES — 7 kesmenin 7'si bir hareketin ortasındadır.
④ HER SEGMENT KENDİ KURULUMUNU TAM YAZAR — B segmentinin referans imajı
   yoktur; lens + mesafe + açı + kadraj içeriği video promptunda yeniden
   ve tam yazılır. Kıyafet bloğu segment başına tekrarlanır.
⑤ KESME SAYISI = GERİLİM — aksiyon 2 segment, nefes 1 segment. Filmin
   en gergin koşusu (S9) TEK ÇEKİMDİR: yedi kesmeli bir filmde kesmesiz
   on saniye, tehlikenin kendisidir.
⑥ SEGMENT SÜRELERİ SAYIYLA — 5+5 · 4+6 · 6+4 · 3+7 · 10. Her sahne tam
   10.0 s. Saniyeler hem MOTION hem CUT SCHEDULE bloğunda geçer.
⑦ KAMERA SEGMENT İÇİNDE SABİT — 21/21 lockoff. Aksiyon kameradan değil
   kesmeden ve kadrajı geçen kütleden gelir (Risk Kartı 8: kamera
   projede çözülmüş TEK kategori).
```

## 0.3 NOVUM — tek cümle, ilk 5 saniyede kurulur

> **Bu ayda soğuk çakıl yanardağları taşları 40 m/s ile göğe atar; taşlar
> bir dakika sonra HALKA hâlinde geri düşer. Halka DIŞTAN İÇE kapanır —
> kaçış yönü önce ölür — ve hiç taş düşmeyen tek yer, deliğin dibindeki
> 500 metrelik disktir.**

Novum bir durum değil, dünyanın **kuralı**dır ve olay örgüsünü zorunlu kılar:

```
Kural gösterilir      → S0-S1: küçük delik aynı şeyi minyatür yapar;
                        halka düşer, merkez temiz kalır (Çehov 1)
Kural haritadadır     → S4: ova eski düşüşlerin krater iziyle kaplı;
                        koninin dibindeki koyu cam örtü HİÇ vurulmamış
                        (Çehov 2 — zemin, nereye taş düştüğünün kaydıdır)
Kural yolu kapar      → S6: ilk taşlar DIŞ halkaya düşer; gemiye giden
                        yol, tam kaçarken kapanır (dünya hayır der)
Tek çıkış             → S8: aracı ters çevirip patlayan koniye sürmek
```

**Bilim çapası:** Balistik menzil eğrisi 45°'de tepe yapar. 45°-85° arası
püsküren bir koni hiçbir taşı ne dibine ne sonsuza atar: düşüş alanı bir
**halkadır** (iç yarıçap 500 m, dış 1450 m). 45°'lik taşların uçuş süresi
EN KISADIR — dış kenar İLK düşer, halka içe doğru kapanır. Karakterin
hayatı tek bir trigonometri gerçeğinin içindedir.

## 0.4 KANCA — YER değil DURUM

```
0-3 s    TİTREME     matkap başında; çakıl zeminde zıplamaya başlıyor
3-5 s    ⭐ NOVUM     30 m solda kılcal çatlak AÇILIYOR ve çakıl fışkırıyor
5-10 s   DÖNÜŞ       başı sola dönüyor; jet hâlâ yükseliyor — matkap
                     elinden bırakılmış, film başlamıştır
```

İlk 10 saniyede bir imkânsızlık (yerden fışkıran taş), bir tehdit ve bir
kesme var. Manzara kancası yasağı (UZAY_SENARYO_KILAVUZU §15) kapalı:
kanca bir olaydır, bir yer değil.

## 0.5 ANTAGONİST KANALI

```
Kanal 1 (çevre)        S0-S7    kapanan halka: konuşmaz, seçmez, sadece düşer
Kanal 4 (kendi seçimi) S8-S13   ⭐ asıl antagonist
```

Değer çatışması: **kurtulmak için, dokuz yıllık işi (karot) ve aracı
taşların altında bırakıp tehlikenin kaynağına koşmak zorunda.** Kimse kötü
değil: koni bir gaz basıncıdır, kimseye kızgın değildir.

## 0.6 ÇEHOV — dört halkalı zincir, dördü de görülüyor

```
HALKA 1  S0-S1  Küçük delik: 12 m'lik yelpaze, 13 saniyede 30-55 m'lik
                bir HALKA hâlinde düşer; deliğin 5 m'lik dibi TEMİZ kalır.
                → İzleyici kuralı minyatüründe GÖRÜR.
HALKA 2  S4     Dışa kaçış yolu ESKİ kraterlerle delik deşik — her düşüşün
                kaydı. S7'de karşı yön: koninin dibindeki koyu, pürüzsüz
                cam örtü — asırlardır TEK taş yememiş zemin.
HALKA 3  S6     Apaçık çözüm denenir: gemiye, DIŞA sür. İlk taşlar tam
                önüne, DIŞ kenara düşer — 45° taşları en kısa sürede iner.
                Dünya hayır der; kaçış yönü önce kapanır.
HALKA 4  S8     Üçü birleşir: halka dıştan kapanıyorsa ve merkez hiç
                vurulmuyorsa, tek güvenli yön İÇERİDİR. Yeni alet yok;
                üç kez gösterilen kuralın doğru okunması var.
```

**Ters simetri:** S4'te araç koniden kaçıyor. S8'de aynı araç koniye
gidiyor. Aynı araç, ters yön, ters anlam.

## 0.7 ETKİNLİK ÇAPALARI

```
1. TERCİH ÇAPASI     S8 segment A: eller direksiyonu sonuna kadar sola
                     kırıyor, güç kolu tam ileri. Doruk bir SEGMENTİN
                     içinde (3 saniye).
2. TEPKİ ÇAPASI      S6 segment B: fren; gövde harnessa yüklenir, sağ el
                     refleksle göğüs kayışını kavrar, sonra direksiyona
                     döner.
3. BAŞLANGIÇ AMACI   S0 segment A: matkap çalışıyor, karot işi yarıda —
                     amaç ilk kareden görünür.
4. ZORLANMA ÇAPASI   S7: durmuş araçta 10 saniye. Hiçbir şey yapmıyor —
                     BAKIYOR. Yetkinliğin tek işe yaradığı an, ölçme anı.
5. BAŞARISIZ DENEME  S6: apaçık çözüm (dışa, gemiye) denendi ve dünya
                     hayır dedi. S8'in seçimi zekice değil, ZORUNLU okunur.
```

**Kamera-taşıyıcı testi:** Karakteri drone ile değiştirirsem S8 kaybolur —
drone karot bırakmayı seçmez, geometriyi okuyup içeri dönmez. ✅

## 0.8 JEST TEKRARI DENETİMİ

```
Başı sola (koniye) çevirme   S0-B · S7 → 2 kez, ikincisi karar anı ✅
Göğüs kayışını kavrama       S6-B · S10-B (inişte) → 2 kez, ters anlam:
                             biri durmak, biri bırakmak için ✅
Güç kolu / direksiyon        S8-A tek doruk jesti — filmde bir kez ✅
Yukarı bakma                 S5'te bir kez (sütun sırtı geçerken) —
                             bilinçli tek kullanım ✅
```

## 0.9 RİSK SAYIMI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

```
□ KART 1  Su / sıvı .................. YOK    0 sahne   ✅ 🔴 kart elendi
□ KART 2  Canlı / hayvan ............. YOK    0 sahne   ✅ 🔴 kart elendi
□ KART 3  Kask / vizör ............... VAR    → HELMET STATE SCHEDULE
□ KART 4  İkinci figür ............... VAR    → HUMAN COUNT LOCK
                                        ⚠️ S2-B (binme) ve S10-B (inme)
                                        klon sıcak noktaları — ayrıca yazıldı
□ KART 5  Ekran / sayaç / gösterge ... VAR    → metinsiz, ÇEVRESEL (§0.11)
□ KART 6  Parçacık / patlama ......... VAR    → 🔴 bu filmin en pahalı kartı
□ KART 6b Katmanlı dünya ............. YOK    → tek katman
□ KART 7  Diyalog .................... VAR    → 5 replik · 3 sahne (S1/S6/S7)
                                        hepsi ≤5 s · konuşanlar: kadın
                                        (yalnız geniş planda) + ekran
                                        dışı AI sesi → Character Bible
                                        SUIT AI bloğu
□ KART 8  Kamera hareketi ............ YOK    21/21 segment sabit lockoff ✅

RİSK SAYISI: 5 / 9      ⚠️ TAM EŞİKTE — diyalog BİLİNÇLİ eklendi
   Gerekçe: analiz diyaloğu novum'u sözle kilitliyor (halka + temiz
   merkez) ve S7 ölü bant riskini kapatıyor. Karşı önlem: replikler
   kısa, kadın yalnız geniş planda konuşur (dudak senkron riski yok),
   AI görsel varlıksız ekran dışı ses. Altıncı risk EKLENMEZ — bu
   filmde başka hiçbir kart açılamaz.
🆕 KARTLARDA OLMAYAN RİSK: sahne içi kesme — DAWN FRONT §0.2.2 ile aynı;
   bu filmde doz yarıya indirildi (sahne başına en çok 1).
```

```
⚠️ KART 6 filmin merkezinde ve kartın kanıtı kötü (Low Power Parçacık
   2/10). Karşı önlem SAYISAL ve §0.13'te: fırlatma 40 m/s, taş 0.1-0.6 m,
   çarpma sütunu 4 m, toz çökmesi 40 s, yerçekimi 1.1 m/s², hiçbir yerde
   sıvı yok, hiçbir şey yanmıyor. "explosion / blast / smoke / flame /
   fireball / shockwave" kökleri 28 promptun hiçbirinde pozitif
   betimlemede geçmiyor (Ders 56 + 59): koni SOĞUKTUR, jetler SOĞUK KURU
   ÇAKILDIR, yazım hep böyledir.
```

## 0.10 SAHNE HARİTASI — 14 sahne × 10 s = 140 s

| # | Sahne | İskelet | Segment | Kesme | Kesme sn | Erüpsiyon saati |
|---|---|---|---|---|---|---|
| S0 | **HOOK** — çatlak fışkırıyor | novum tetiği | **2** | 1 | 5.0 | −20 s |
| S1 | Küçük halka — **ÇEHOV 1** | kuralın minyatürü | 1 | 0 | — | −10 s |
| S2 | **KONİ PATLIYOR** | novum tam boy | **2** | 1 | 4.0 | 0 s |
| S3 | ⭐ **VİRAL** — taş sütunu (insansız) | saf görsel | 1 | 0 | — | +10 s |
| S4 | Dışa kaçış — **ÇEHOV 2** | apaçık çözüm | **2** | 1 | 5.0 | +20 s |
| S5 | Sütun sırtı geçiyor | sayaç A | 1 | 0 | — | +30 s |
| S6 | **DIŞ HALKA KAPANIYOR** | dünya hayır der | **2** | 1 | 6.0 | +45 s |
| S7 | **Hesap** — AI analizi | ⭐ nefes = ölçme | 1 | 0 | — | +55 s |
| S8 | ⭐ **DORUK** — ters dönüş | **SEÇİM** | **2** | 1 | 3.0 | +65 s |
| S9 | ⭐ **İÇE KOŞU** | kovalamaca | 1 | 0 | — | +75 s |
| S10 | Çatlak büyümüş — araç düşüyor | bedelin başı | **2** | 1 | 6.0 | +85 s |
| S11 | **ÇİZGİ + BEDEL** | araç vuruluyor | **2** | 1 | 5.0 | +95 s |
| S12 | **OVERVIEW** — göz | ölçek · tema | 1 | 0 | — | +105 s |
| S13 | **FİNAL** — gözün içinde | held frame | 1 | 0 | — | +115 s |

```
TOPLAM        14 sahne · 21 segment · 7 kesme · 140 saniye
              28 prompt (14 imaj + 14 video)
VİRAL ARA     S3 ve S9 — bunlar KESİLEMEZ
DİYALOG       S1 · S6 · S7 — 5 replik, hepsi ≤5 s (SUIT AI bloğu)
OVERVIEW      S12, tam olarak bir tane
TEK ÇEKİMLİ   S1 · S3 · S5 · S7 · S9 · S12 · S13 → "no cuts" cümlesi AYNEN
TEK KESMELİ   S0 · S2 · S4 · S6 · S8 · S10 · S11 → CUT SCHEDULE (§0.2)
```

## 0.11 ⭐ ÜÇ SAYAÇ — üçü de metinsiz, üçü de ÇEVRESEL

`Risk Kartı 5` iki yönlüdür: model ekrana yazı ekler YA DA "no text" yasağı
anlatımı siler. Bu filmde gösterge diye bir şey yok; üç sayaç da manzarada.

### SAYAÇ A — SÜTUN / SIRT (yükselen tehdit)

| Sahne | Sütun tepesi | Arkadaki 400 m'lik sırta göre |
|---|---|---|
| S2 | ~200 m | sırtın YARISINDA |
| S5 | ~600 m | sırtın ÜSTÜNDE, açık farkla |
| S12 | ~600 m | sabit — artık gökyüzünün parçası |

### SAYAÇ B — EN YAKIN ÇARPMA (kapanan halka)

| Sahne | En yakın çarpma sütunu | Yön |
|---|---|---|
| S6 | 60 m ÖNDE (dış kenarda) | yolu kesiyor |
| S9 | 30 m ARKADA | kovalıyor |
| S11 | 12 m ARKADA | ensesinde |

### SAYAÇ C — ZEMİNİN KENDİSİ (harita)

```
DELİK DEŞİK OVA   eski çarpma kraterleri (0.5-2 m, ışınlı) = halkanın içi
KOYU CAM ÖRTÜ     pürüzsüz, asırlardır taş yememiş = göz (iç 500 m)
ÇİZGİ             ikisinin arasındaki KESKİN sınır — S11'de koşarak geçilir
Rakam yok, doluluk ve mesafe var. Üç sayaç da monotonik ilerler.
```

## 0.12 SAYISAL KİLİTLER

```
□ İNSAN SAYISI    HUMAN COUNT LOCK: tam 1 insan, 21 segmentin 21'inde
                  (S3 İNSANSIZ — "No human in frame" yazılır; S12'de tek
                  nokta-figür). İkinci silüet yok, yansımada figür yok.
                  ⚠️ S2-B (araca binme) ve S10-B (araçtan inme) Risk
                  Kartı 4'ün tam hedefi — o segmentlerde "exactly one
                  human" cümlesi ayrıca vurgulanır ve iniş sonrası
                  "the seat behind her is EMPTY" yazılır.

□ KASK TAKVİMİ    HELMET STATE SCHEDULE: kapalı 21/21. Açık: 0.
                  Ara durum yok. Gerekçe fizikte: %1.4 basınç, solunamaz.

□ ÖLÇÜ            kadın 1.66 m · rover 3.0 × 1.7 m · tekerlek 0.8 m ·
                  matkap sehpası 2.4 m · karot silindiri 0.9 m / 40 kg ·
                  koni 60 m yüksek, ağzı 40 m · sırt 400 m · sütun ~600 m ·
                  küçük delik yelpazesi 12 m · taşlar 0.1-0.6 m ·
                  çarpma sütunu 4 m · çatlak S0'da kılcal, S10'da 1.2 m

□ YERÇEKİMİ       0.11 g (1.1 m/s²). Serbest düşüş: 1 saniyede 0.55 m.
                  Ağır çekim panzehiri §0.14'te.

□ SIVI TEMASI     0 sahne. Bu filmde HİÇ sıvı yok; su, buz, ıslaklık yok.

□ CANLI           0 canlı, 21 segmentin 21'inde.

□ HIZ             fırlatma 40 m/s · çarpma 40 m/s · küçük delik jeti 8 m/s ·
                  rover cam örtüde 10 m/s, delikli ovada 8 m/s · koşu 5 m/s ·
                  halka kapanışı: dış kenar +51 s'de, iç kenar +72 s'de

□ HALKA           düşüş alanı: yarıçap 500-1450 m. GÖZ: iç 500 m disk +
                  koyu cam örtü. Gemi 2100 m'de, dış kenarın ÖTESİNDE.
                  Kadının sondaj noktası 900 m'de — halkanın tam ortası.

□ YOĞUNLUK        sürekli düşüşte her 20 m'lik kareye 5 saniyede bir taş.
                  Koni sustuktan 70 s sonra son taş iner.

□ KESME           CUT SCHEDULE: 7 kesme, 7 saniye değeri yazılı —
                  S0 5.0 · S2 4.0 · S4 5.0 · S6 6.0 · S8 3.0 · S10 6.0 ·
                  S11 5.0. Yazılı kesmeden BAŞKA kesme yok; bindirme,
                  fade, morph, hız rampası hiçbir sahnede yok.

□ DİYALOG         DIALOGUE SCHEDULE: 5 replik / 3 sahne — S1 (kadın +
                  AI) · S6 (yalnız AI) · S7 (kadın + AI). Her replik
                  ≤5 s, saniyesi video promptunda yazılı. Replik asla
                  metin olarak görünmez; AI ekran dışı sestir. Diğer
                  11 sahnede tek kelime yok.
```

## 0.13 ⭐ KONİ — filmin fizik sözleşmesi

```
AY          yarıçap 1100 km · 0.11 g (1.1 m/s²) · ince N2 atmosferi,
            deniz seviyesi basıncının %1.4'ü. Gökyüzü koyu menekşe;
            SOL ufkun üstünde bantlı, soluk, dev bir gaz gezegeni.

KONİ        900 m solda, 60 m yüksek eski bir çakıl konisi, ağzı 40 m.
            İçeride sıkışan soğuk azot gazı basınçla boşalır ve gevşek
            çakılı 40 m/s ile fırlatır. SOĞUKTUR: ateş yok, kor yok,
            duman yok, kül yok. Çıkan şey yalnızca KURU TAŞ ve GAZDIR.

YELPAZE     45° ile 85° arası, her yöne. Asla tam dik, asla 45°'den yatık.
            → menzil eğrisi düşüşü bir HALKAYA hapseder: 500-1450 m.

KURAL 1     DIŞ KENAR İLK DÜŞER. 45° taşı en uzağa gider AMA en kısa
            sürede iner (+51 s). 85° taşı en yakına, en geç iner (+72 s).
            Halka dıştan içe 21 saniyede kapanır. → Kaçış yönü önce ölür.

KURAL 2     MERKEZ HİÇ VURULMAZ. Hiçbir taş 45°'den yatık çıkmadığı için
            koninin 500 m'lik dibi ile koyu cam örtü asla taş yemez.
            Kanıt zeminde: örtü pürüzsüz, ova delik deşik (Sayaç C).

KURAL 3     KONİ SUSUNCA GÖK 70 SANİYE DAHA DÜŞER. Havadaki her taş
            balistik borcunu öder. Film bittiğinde halka hâlâ düşüyordur.

KÜÇÜK DELİK aynı mekaniğin minyatürü: jet 8 m/s, yelpaze 12 m, taşlar
            13 saniyede 30-55 m'lik halkaya iner, deliğin 5 m'lik dibi
            temiz kalır. S0-S1'in tek işi bu kuralı GÖSTERMEKTİR.
```

### Kaçış hesabı — filmin tuzağı

```
KADIN       900 m'de (halkanın ortası). Gemi 2100 m'de, sağda, güvenli.
DIŞA        dış kenara 550 m · delikli ovada 8 m/s → ~69 s.
            İlk taşlar +51 s'de TAM O KENARA düşer. → yol kapanır (S6).
İÇE         cam örtü çizgisine 400 m · geri dönüş + koşu payıyla ~70 s.
            Halka +72 s'de tamamen kapanır; sonrası sürekli yağış altında
            sürüştür. Her saniye gecikme, taş yoğunluğunu artırır.
BEDEL       İçeri dönüş karotu ve aracı halkanın İÇİNDE bırakmaktır:
            araç S10'da çatlağa saplanır, S11'de taş altında ezilir.
            Kadın çizgiyi S11'de koşarak geçer. Gemiye gidiş, koni
            susana kadar BEKLEMEK zorundadır (S13 bu bekleyiştir).
```

```
⚠️ NEGATİF ÇEKİRDEKLE ÇELİŞKİ DENETİMİ — üçü de bilerek çözüldü

① "never hovering" ↔ yükselen taş sütunu.
   ÇÖZÜM: sütun asla ASILI yazılmaz. Her taş her an hareket hâlindedir:
   "rising, arcing over and falling back with continuous momentum".
   Tepe noktası hiçbir promptta betimlenmez; sütunun tepesi uzak ve
   süreklidir, tek taşın apeks anı asla kadraja alınmaz.

② "no cuts" ↔ istenen kesme — §0.2'de çözüldü: tek kesmeli 7 sahnede
   cümle yok, CUT SCHEDULE var. Tek çekimli 7 sahnede aynen duruyor.

③ Patlama sözlüğü ↔ erüpsiyon. ÇÖZÜM [Ders 56+59]: yasaklı kök pozitif
   betimlemede HİÇ geçmez. Yerine ne yazılır:
     "a cone-shaped spray of dry cold gravel at 40 m/s"
     "needle-sharp streams of stones rising in straight ballistic arcs"
     "a 4-meter column of dust where each stone strikes"
```

## 0.14 AĞIR ÇEKİM PANZEHİRİ [Ders 44]

0.11 g bu deponun en floaty ortamı — panzehir prompt cümlesi değil,
**sahne tasarımı**:

```
① HIZ REFERANSI KADRAJIN İÇİNDE — taşlar 40 m/s ile çıkar, rover 10 m/s
   ile kadrajı 3-4 saniyede geçer; her promptta "full real-world speed,
   not slow motion" + sayı birlikte durur.
② İNSAN HAVADA SÜZÜLMEZ — atlama/sıçrama sahnesi BİLEREK YOK. Koşu
   "long LOW flat strides" olarak yazılır: adım 3 m, yükseklik 0.5 m,
   temas sık. 0.11 g'nin uzun balistik uçuşu kadraja hiç alınmaz.
③ DÜŞEN NESNE SAYISI YAZILI — serbest düşüş 1 saniyede 0.55 m; çarpma
   hızı 40 m/s (fırlatma hızına eşit — balistik simetri). Taşlar yere
   HIZLI çarpar; yavaş süzülen tek şey 40 saniyelik toz perdesidir ve
   o da "settles, never hovers" olarak kilitlidir.
```

## 0.15 ÜRETİM ÖNCESİ KONTROL — `03_PLAN_ONCESI_KONTROL_LISTESI.md`

```
ÜRETİM ÖNCESİ KONTROL — THE STONE SKY               tarih: 05.08.2026

A1 ✅ Yasak ↔ anlatım çelişkisi YOK:
      · METİN: gösterge yok; üç sayaç da çevresel ve rakamsız (§0.11).
      · KESME: kesme istenen 7 sahnede "no cuts" yok, CUT SCHEDULE var;
        istenmeyen 7 sahnede cümle aynen duruyor (§0.2).
      · HOVER: sütun "asılı" değil "sürekli momentumlu" yazılı (§0.13 ①).
A2 ✅ sahne sayısı: başlık 14 = harita 14 = "Scene N of 14" 14 promptta;
      segment 21, kesme 7 (§0.10 tablosuyla birebir)
A3 ✅ süre: segment süreleri toplamı her sahnede tam 10.0 s; 14 × 10 = 140 s
B1 ✅ doruk S8 segment A'nın İÇİNDE (3 saniye: direksiyon + güç kolu).
      S8 → S9 geçişinde görünmeyen zorunlu olay yok: S9 ilk karesinde
      araç zaten içe doğru tam hızda.
B1b ✅ ışık takvimi §0.11/Lighting Bible'da; bölge başına monotonik:
      halka kararır (toz perdesi), göz sabit aydınlık kalır. IŞIK = TEMA.
B2 ✅ bedelli seçim S8; bedel S10 (araç saplanır), S11-B (karot taş
      altında parçalanır) ve S13'te (eli boş, gemi halkanın ötesinde)
      GÖRÜLÜYOR.
C  ✅ 10 sayısal kilit yazıldı — §0.12
D  ⚠️ risk sayımı: 5/9 — TAM EŞİKTE. Su ve canlı elendi; diyalog
      bilinçli açıldı (gerekçe ve karşı önlem §0.9'da). Altıncı kart
      açılamaz.
D2 ✅ diyalog ↔ metin çelişkisi YOK: replikler yalnız SES; "no text"
      yasağı korunuyor, AI'ın ekranı/gövdesi/avatarı yok.
E  ✅ QA SPEC bloğu yazıldı — §0.16
```

## 0.16 QA SPEC BLOĞU — üretimden sonra rubriklere BUNU kopyala

```
FILM:                 THE STONE SKY
FORMAT:               16:9 yatay · 2-4 dk · bilimkurgu · ince atmosfer
SCENE COUNT:          14
RUNTIME:              140 s       (14 × 10 s ile doğrulandı)
SEGMENT COUNT:        21          ⭐ sahne içi kesme — aşağıyı oku
PLANNED CUTS:         7           (sahne başına en çok 1)
DIALOGUE LINES:       5           konuşmalı sahne: S1 (2) · S6 (1) ·
                                  S7 (2) — hepsi ≤5 s; kadın yalnız
                                  geniş planda konuşur, AI ekran dışı
                                  sentetik sestir, replik asla metin
                                  olarak görünmez
SILENT SCENES:        11
VIRAL INTERSTITIALS:  2           S3, S9  — BUNLAR KESİLEMEZ
PROTAGONIST:          Dr. Nehir Solak · gezegen sismoloğu / sondaj müh.
CENTRAL CHOICE:       S8          bedelin görüldüğü sahne: S10, S11-B, S13
OVERVIEW SCENE:       S12         (tam olarak bir tane)
CAMERA:               21/21 segment sabit lockoff · segment içinde
                      hiçbir kamera hareketi yok

⛔ RUBRİĞE UYARI — bu film bilinçli olarak sahne içinde kesiyor.
   7 kesmenin 7'si aşağıda saniye olarak yazılıdır; Ders 1 ihlali
   olarak raporlanmamalıdır. Listede OLMAYAN her kesme gerçek ihlaldir;
   bindirme/fade/morph her durumda ihlaldir.

   PLANLI KESME NOKTALARI (sahne başlangıcından itibaren, saniye):
     S0  5.0     S2  4.0     S4  5.0     S6  6.0
     S8  3.0     S10 6.0     S11 5.0
   KESMESİZ SAHNELER (bunlarda TEK kesme bile ihlaldir):
     S1 · S3 · S5 · S7 · S9 · S12 · S13
```

## 0.17 FARKLILAŞMA — depodaki komşu filmlerle çakışma denetimi

```
THE DAWN FRONT       en yakın komşu (aynı ortam + kesme mimarisi). Orada
                     tehlike bir ÇİZGİ ve sabittir: 13.3 m/s, tek yönlü.
                     Burada tehlike bir HALKA ve iki zamanlıdır: önce
                     yükselir (görünür ama zararsız), sonra düşer. Orada
                     çözüm kaçmak, burada çözüm tehlikenin KAYNAĞINA
                     gitmektir. Kesme dozu bilinçli yarı: 12 → 7.
THE KALEIDA CRASH    araçlı felaket · orada kaza filmin başında, burada
                     araç dorukta bilerek terk edilir ve bedel olarak
                     ezilir.
THE REMEMBERING DUST ay ortamı · orada toz hafızadır ve tema durağandır;
                     burada zemin bir DÜŞÜŞ HARİTASIDIR ve okumak hayat
                     kurtarır.
THE RING WALKER      "ring" orada yörünge halkasıdır (gökyüzünde); burada
                     halka ZEMİNDE kapanan bir çemberdir. Ad benzerliği
                     dışında ortaklık yok.
THE BURNING WORLD    püskürme · orada kaynak LAV = sıvı + sıcak + sürekli.
                     Burada her şey KURU ve SOĞUK; sıvı sıfır sahne.
```

## 0.18 📈 TUTUNDURMA HARİTASI

| Saniye | Sahne | İzleyiciye ne veriyor | Kesme | Paylaşılabilir? |
|---|---|---|---|---|
| 0:00-0:10 | S0 | ⭐ **Kanca:** yer titriyor → çatlak fışkırıyor | **1** | ✅ 5 sn klip |
| 0:10-0:20 | S1 | **Kural:** taşlar HALKA hâlinde düşüyor | 0 | ✅ 6 sn klip |
| 0:20-0:30 | S2 | ⭐ Koni patlıyor — sütun sırtın yarısında | **1** | ✅ 6 sn klip |
| 0:30-0:40 | S3 | ⭐ Sütunun içi: taş akıntıları, 40 m/s | 0 | ✅ 5 sn klip |
| 0:40-0:50 | S4 | Kaçış başlıyor; zemin delik deşik | **1** | |
| 0:50-1:00 | S5 | Sütun sırtı geçiyor — gök doluyor | 0 | ✅ 4 sn klip |
| 1:00-1:10 | S6 | ⭐ **Yol kapanıyor:** ilk taşlar tam öne | **1** | ✅ 6 sn klip |
| 1:10-1:20 | S7 | **Hesap:** soru + AI analizi — geometri sözle kilitleniyor | 0 | ✅ 8 sn klip |
| 1:20-1:30 | S8 | 🎯 **Doruk:** ters dönüş, koniye doğru | **1** | ✅ 6 sn klip |
| 1:30-1:40 | S9 | ⭐ **Koşu:** halka ensesinde, tek çekim | 0 | ✅ 10 sn klip |
| 1:40-1:50 | S10 | Çatlak aracı yutuyor → yaya | **1** | ✅ 5 sn klip |
| 1:50-2:00 | S11 | ⭐ Çizgi geçiliyor + karot eziliyor | **1** | ✅ 5 sn klip |
| 2:00-2:10 | S12 | ⭐ **Overview:** kapanan halka + temiz göz | 0 | ✅ kapak adayı |
| 2:10-2:20 | S13 | Gözün içinde, yağan göğün ortasında | 0 | |

```
İLK 10 SANİYEDE  1 kesme · 1 imkânsızlık · terk edilmiş matkap
TEK CÜMLELİK ÖNCÜL — izleyicinin yoruma yazabileceği hâli:
  "Gök taş yağdırıyor ve tek kuru yer, taşları atan deliğin dibi."
✅ ÖLÜ BANT KAPANDI: 1:10-1:20 (S7) filmde görsel olarak en durgun
   banttı; soru + AI analizi diyaloğu bandı taşıyor. Ölçüm yine de
   "durdu" derse çözüm S7'yi 2 segmente bölmektir.
```

## 0.19 🎬 KURGU TALİMATI

```
① TEK GRADE, TEK GREN — 14 klip tek renk düzenlemesi + tek gren katmanı.
   Sahne İÇİ kesmeler tek üretimden geldiği için muaf.
② SES KESİLMEZ — motor vınlaması, tekerlek çıtırtısı, koninin alçak
   basınçlı tıslaması ve nefes, kesmelerin üzerinden akar (J-cut).
   ⭐ S8-A'da ters kullanım: karar anında ses BİR SANİYE tamamen kesilir,
   görüntü akar — sonra motor tam güçle döner. Filmin en güçlü ses anı.
③ SAHNE SINIRLARI — 14 sahne arası düz sert kesme. S11 → S12 (Overview
   öncesi) kesmesinde ses tamamen kesilir (§10 müziksiz sahne).
④ HİÇBİR KLİP HIZLANDIRILMAZ VE YAVAŞLATILMAZ — hız rampası Ders 44'ü
   tetikler; yasaktır.
```

## 0.20 ⏬ PLAN B — kesme prompt içinde tutmazsa

```
7 kesme yazıldığı saniyede ve kadrajla çıkmazsa: her segment AYRI
üretilir → 21 klip → kurguda sert kesme. Her segmentin kurulumu zaten
video promptunda tam yazılı (kural ④); ayrı prompta dönüştürmek için
ek yazı gerekmez.
  MALİYET  14 → 21 klip (+%50 — DAWN FRONT Plan B'sinin +%86'sından ucuz;
           sahne başına en çok 1 kesmenin ikinci kazancı budur)
⚠️ Karar İLK SAHNE üretildikten sonra verilir. Test sahnesi: S0 (bir
   kesme, ölçek atlaması, referanssız B segmenti). S0 temiz çıkarsa
   mimari tutuyor demektir.
```

---
# 📖 BÖLÜM 1 — THE BIBLES

---

## 🌍 WORLD BIBLE — AY: ADRAS

```
CORE CONCEPT: Adras is a small moon (radius 1100 km, 0.11 g) of a huge
banded gas planet, under a thin nitrogen atmosphere at 1.4% of Earth
sea-level pressure. Pockets of cold nitrogen gas trapped under its
gravel plains vent through old cinder cones. When a cone fires, it
throws dry cold gravel upward at 40 meters per second in a fixed fan
between 45 and 85 degrees of elevation, in every direction. Nothing
burns: no fire, no ember, no smoke, no ash. What comes out is stone
and cold gas, and what goes up comes back down on ballistics alone.

CRITICAL WORLD RULE — THE FALL IS A RING: because no stone leaves
flatter than 45 degrees or steeper than 85, every stone lands between
500 and 1450 meters from the cone. The 500-meter disk at the cone's
foot is never hit — its dark glassy ash apron is smooth and unmarked
after centuries of eruptions, while the plain beyond is pocked with
old impact craters. The ground itself is the map of where stones fall.

RULE ONE — THE OUTER EDGE FALLS FIRST: the 45-degree stones fly
farthest but land soonest (51 seconds after launch). The steepest
stones land nearest and last (72 seconds). The ring of falling stones
closes from the outside inward over 21 seconds. The escape direction
dies first.

RULE TWO — THE CENTER IS NEVER HIT: no stone leaves flatter than 45
degrees, so the inner 500-meter disk stays clean through the whole
eruption. The only safe ground is at the foot of the thing throwing
the stones.

RULE THREE — THE SKY OWES 70 MORE SECONDS: when the cone goes quiet,
every stone still in the air keeps falling for up to 70 seconds. The
ring keeps churning long after the source dies.

GROUND: a flat plain of pale grey regolith gravel. Between 500 and
1450 meters from the cone: old impact pockmarks 0.5 to 2 meters wide
with bright ray-spokes. Inside 500 meters: a smooth dark glassy ash
apron with a SHARP visible boundary line where the pocked ground ends.
A dark ridge 400 meters high runs behind the cone. No water, no ice,
no liquid of any kind, no vegetation, no animal life.

SKY & LIGHT: deep violet sky. A huge dim ochre-banded gas planet
hangs low above the LEFT horizon behind the ridge. The sun sits fixed
8 degrees above the RIGHT horizon (a slow moon day — it does not move
during the film), throwing long hard shadows to the left. Shadows are
weak-filled and soft-edged, correct for 1.4% pressure.

SOUND: thin and muffled. The cone is a deep continuous low hiss felt
more than heard. Impacts are dry distant thuds. Nothing rings.
```

---

## 👤 CHARACTER BIBLE — DR. NEHİR SOLAK

> ⚠️ **Ders 45:** Bu ad prompt gövdesine ASLA yazılmaz. Prompt'ta yalnız
> fiziksel tarif geçer; ad yalnız burada durur.

```
IDENTITY: 38-year-old planetary seismologist and drilling engineer,
nine years of solo survey work. She landed to pull one 0.9 meter core
from the flank plain of a dormant vent cone — the seismic charts said
dormant. Her one error is an error of information, not intelligence:
the charts were made from orbit, and orbit cannot hear gas.

COMPETENCE RULE [UZAY_SENARYO_KILAVUZU §9]: she never panics and never
moves before she reads. She watches the small vent's ring fall (S1),
reads the pocked plain and the clean apron (S4, S7), tries the obvious
exit first (S4-S6) — and only when the world refuses does she turn
toward the cone. Every decision on screen is a read decision.

⭐ SUIT IDENTITY LOCK [Ders 55] — yüzün okunduğu her segmentte (50mm,
75mm) BİREBİR yazılır; 32mm geniş planlarda kısa biçim + sayılar:

  A 38-year-old woman, 1.66 meters tall, compact and quick. Medium-brown
  skin with real visible pore texture, dark brown eyes, black hair
  cropped close, a thin pale scar through her left eyebrow, chapped
  lips. She wears a sleek current-generation matte sand-grey hard-composite exploration suit, close-fitting and machine-finished, with burnt-orange
  sealed seams along both forearms and across the chest, a scuffed dark
  grey hard-shell chest pack holding a flat integrated rebreather, and
  heavy ribbed boots. One fully transparent seamless visor, no tint, no
  coating, no mask or regulator beneath it, her whole face clearly
  readable through it. A narrow dark band on her left wrist shows a
  slow abstract amber pulse and nothing else. No back-mounted tank, no
  hose, no cable. Her wear marks are fixed and never move: a dark grey
  dust smear across the right thigh, a scuffed patch on the left
  shoulder where the orange seam line has worn dull, and a film of pale dust
  along the lower edge of the visor.

  This is the only suit in the film: 21 segments, 21 identical suits.

⭐ EQUIPMENT FRAME LOCK [Ders 57]: the suit and life-support
  configuration visible in the first frame is IDENTICAL in the last
  frame — AND IDENTICAL ACROSS EVERY CUT INSIDE THE SAME SCENE.
  Nothing is added, removed or reshaped at a cut. No tank appears, no
  mask appears, no hose appears. The visor never opens, tints or
  clears. If any equipment differs before and after a cut, the
  generation is an ERROR. Kıyafet tarifi her segment bloğunda TEKRARLANIR.

HELMET STATE SCHEDULE [Ders 5, 37 · Risk Kartı 3]:
  Kapalı: 21 segmentin 21'inde. Açık: 0. Ara durum yok, geçiş yok.

HANDS: gloved, empty in every segment. She touches exactly three
things in this film and nothing else: the drill rig, the steering
yoke with its power lever, and her chest harness strap.

MOVEMENT SIGNATURE (her segmentte en az biri):
- başını 15 derece sola, koniye çevirip hemen öne dönmek
- bir hareketten hemen önce kısa, kontrollü bir nefes vermek
- sarsıntıda sağ elin göğüs kayışını kavraması
- 0.11 g'de UZUN, ALÇAK, DÜZ adımlarla koşmak — adım 3 m, yükseklik
  0.5 m, temas sık; asla yüksek sıçrama, asla havada süzülme
- inişte dizlerin yükü emmesi ve gövdenin öne eğilmesi

⭐ SUIT AI — KIYAFET YAPAY ZEKÂSI (görsel varlığı YOKTUR)
  A calm, neutral, slightly dry SYNTHETIC VOICE from the suit's
  helmet speaker. It has NO body, NO face, NO avatar, NO hologram,
  NO screen and NO text output of any kind — it exists only as an
  off-screen voice. Ses tonu: sakin, ölçülü, asla telaşlı; kötü
  haberi de aynı düz tonda verir.

  DİYALOG KURALLARI [VEO_3_1 kılavuzu + Risk Kartı 5 + 7]:
  · Toplam 5 replik, 3 sahnede: S1 (2) · S6 (1) · S7 (2). Başka
    hiçbir sahnede tek kelime yok.
  · Her replik 5 SANİYENİN ALTINDA (kılavuz: 5 s üstü ses kesilir).
  · Aynı anda tek konuşmacı; sıra promptta açıkça yazılır
    ("She speaks first, then the synthetic voice replies").
  · Kadının replikleri YALNIZ geniş planlarda (20-25 m) — yüz o
    ölçekte okunmaz, dudak senkron riski sıfıra iner. AI zaten
    ekran dışı sestir, dudak diye bir şeyi yoktur.
  · Replik ASLA metin olarak gösterilmez — altyazı yok, transkript
    yok (Risk Kartı 5 YÖN 1 kapalı; sesli anlatım YÖN 2'yi kapatır).
  · Ses hiyerarşisi ≤3 katman: diyalog loud · araç/adım sesi mid ·
    koni tıslaması faintly. "Audio: Clean dialogue only" her
    diyaloglu promptta yazılır.
  · Türkçe yayın gerekirse hibrit yol: kılavuz §9 (ElevenLabs+Sync).
```

---

## 🛻 ROVER BIBLE — SAHA ARACI

> Araç adı prompt gövdesine yazılmaz; yalnız "the 3.0 meter sleek
> angular four-wheel rover" geçer.

```
DIMENSIONS: 3.0 m long, 1.7 m wide, 1.5 m tall at the cockpit hoop.

DESIGN LOGIC: a current-generation lunar-class terrain vehicle —
sleek, angular, machine-finished, clearly the product of a modern
space program. A low FACETED MONOCOQUE BODY of matte sand-grey
composite panels with crisp angular edges, like a concept
electric vehicle built for another world; a single open cockpit (no
cabin, no doors, no glass, no hot parts) sunk into the body's
centerline. It carries work dust and honest scuffs, but it is
unmistakably MODERN hardware: never old, never rusted, never
improvised, no exposed wiring, no visible frame tubes, no
mismatched parts.

STRUCTURE (sayılabilir parçalar — asla tek düz kütle değil):
- four airless alloy mesh wheels, each 0.8 m in diameter, on
  articulated suspension arms faired smoothly into the body panels
- a single open cockpit sunk into the centerline: one form-fitting
  seat, a low integrated cockpit hoop, a simple cross-chest harness
  strap, a clean matte-composite steering yoke with one power lever
- a recessed rear cargo bay holding one 0.9 m dark grey core
  cylinder under two burnt-orange quick-release straps
- a flat sealed battery deck under the body — no vents, no exhaust,
  nothing hot
- matte sand-grey machine-finished faceted panels with crisp
  burnt-orange accent markings and a thin film of pale work dust

SPEED: 10 m/s on the smooth ash apron, 8 m/s on the pocked plain.
Wheels always rotate in ground contact, never slide, never float.

SCALE ANCHORS REQUIRED IN EVERY ROVER SEGMENT: at least one of — her
1.66 m figure in the seat, the 0.8 m wheel diameter, or the 0.9 m
core cylinder on the cradle.

MANDATORY QUALIFIER IN EVERY VEHICLE SEGMENT: "physically accurate
perspective, correct engineering proportions, realistic scale
relationships — the rover must never appear miniature or toy-like."

⭐ MODERN LOCK — yıpranma ≠ eskime:
  The rover and the suit are CURRENT-GENERATION equipment: sleek,
  machine-finished, cleanly engineered. Work dust and fixed scuffs
  are allowed and wanted; rust, patches, improvised repairs, exposed
  wiring, dents and mismatched parts are NOT. "Worn by work, never
  old" — bu cümlenin İngilizce karşılığı araç ve kıyafet geçen kritik
  segmentlerde tekrar eder: "worn by work but unmistakably modern,
  never old, never rusted, never improvised."

⭐ ROVER STATE SCHEDULE — hangi segmentte ne hâlde
  Park, matkap yanında:        S0-A..B · S1 · S2-A
  Sürüşte, DIŞA (sağa):        S2-B · S4-A..B · S5 · S6-A
  Fren / durmuş:               S6-B · S7 · S8-A
  Sürüşte, İÇE (sola):         S8-B · S9 · S10-A
  ÇATLAKTA, burnu gömülü:      S10-A sonundan itibaren · S10-B · S11-B
  EZİLMİŞ (taş almış):         S11-B sonundan itibaren · S12 (uzakta)
  Karot silindiri kızakta:     S11-B'deki darbeye kadar her segmentte
```

---

## 🚀 SHIP BIBLE — İNİCİ

```
HULL: 14 meters long, three splayed legs, matte sand-grey plating with
crisp burnt-orange markings, standing on the open plain 2100 meters
from the cone — BEYOND the outer edge of the fall ring. Safe, visible,
unreachable.

IN FRAME: yalnız S4-B (sağ ufukta parıltı), S7 (sağ kenarda küçük),
S12 (uzak nokta) ve S13 (sağ ufukta, halkanın ötesinde, netsiz).
Gemiye HİÇ varılmaz; film gemiye 1600 metre kala biter.

MANDATORY QUALIFIER: "physically accurate perspective, correct
engineering proportions — the ship must never appear miniature or
toy-like."
```

---

## 🗺️ RECURRING ENTITY BIBLE [Ders 58]

| Varlık | Segment | Sabit tanım (sayısal — asla değişmez) |
|---|---|---|
| **Koni** | 12 segment | 60 m yüksek eski çakıl konisi, ağzı 40 m, 900 m solda; sütunu 45°-85° yelpaze, taşlar 40 m/s |
| **Sütun** | 12 segment | ~600 m tepe, iğne keskin taş akıntıları, HER KAREDE SOLDA, sürekli momentum — asla asılı değil |
| **Rover** | 13 segment | 3.0 × 1.7 m, kum grisi açık kafes, 4 × 0.8 m ağ tekerlek, tek koltuk + göğüs kayışı, kızakta 0.9 m karot |
| **Karot silindiri** | 9 segment | 0.9 m, koyu gri, iki turuncu kayışla kızağa bağlı |
| **Küçük delik** | S0, S1 | 2 m'lik çatlak deliği, 30 m solda; jeti 8 m/s, halkası 30-55 m |
| **Cam örtü + ÇİZGİ** | S7, S9, S11, S12, S13 | koyu, pürüzsüz, taş izi yok; delikli ovayla arasında KESKİN sınır çizgisi |
| **Gemi** | S4-B, S7, S12, S13 | 14 m, üç ayak, 2100 m sağda, halkanın ötesinde |

```
KURAL 1: Kartı olan varlığın geçtiği her SEGMENTTE kartın tamamı yazılır —
         kesmeden sonraki segmentte ÖZELLİKLE.
KURAL 2: İki segmentten azında görünen prop üretilmez.
KURAL 3: İkinci gelişte "aynı yer" demek yetmez; sayı tekrarlanır.
```

---

## 🎥 CAMERA BIBLE

```
⭐ MOVEMENT: 21/21 SEGMENT FIXED LOCKOFF. Kamera hiçbir segmentin
   içinde hareket etmez. Zoom yok, pan yok, tilt yok, track yok.
   Kadraj yalnız KESMEYLE değişir.

LENS LOCK — segment başına tek lens:
- ÇOK GENİŞ / KONİ / OVA / OVERVIEW   → 32mm anamorphic
- GENİŞ-ORTA / ARAÇ / KOŞU            → 50mm
- ORTA-YAKIN / EL / YÜZ / KARAR       → 75mm
- MAKRO (taş akıntısı, zemin dokusu)  → 100mm macro

DISTANCE LOCK: her segment kamera mesafesini metre cinsinden yazar.

⭐ AXIS LOCK: 21 segmentin 21'inde koni ve sütun kadrajın SOL
   tarafındadır. Gemi ve güneş SAĞDADIR. Kamera eksenin öbür yanına
   hiçbir segmentte geçmez. S0-S7'de hareket SAĞA, S8-S11'de SOLA
   akar — yön değişimi doruğun kendisidir, eksen değişmez.

⭐ CUT GEOMETRY: her kesmede ≥30° açı veya ≥1 ölçek kademesi farkı
   (§0.2.1 ②) — sahnenin KESME PLANI bloğunda yazılı.

⚠️ Ders 45 — KAMERA SATIRI CÜMLE OLARAK: "Shot on a 75mm lens from a
   fixed position two meters away, f/5.6, physically accurate
   perspective." — künye biçiminde değil.

CLIP LENGTH: her video prompt tam 10 saniyedir ve içinde 0 veya 1 sert
kesme taşır. Kesme saniyesi MOTION ve CUT SCHEDULE bloklarında iki kez
yazılır.

CONTINUITY LOCK [Ders 1] — İKİ BİÇİMDE:
  Tek çekimli 7 sahnede : "single unbroken take, no cuts" (aynen)
  Tek kesmeli 7 sahnede : "CUT SCHEDULE: exactly one hard cut at X.Xs,
                           and no others" (§0.2)

MOTION SPEED [Ders 12, 44]: insan ve araç gerçek zamanlı hızda. Ağır
çekim YOK, hız rampası YOK — panzehir §0.14.
```

---

## 💡 LIGHTING BIBLE

> Faz adı her segmentte açıkça yazılır. **"cinematic lighting" hiçbir
> prompt'ta geçmez** (Ders 33). Bir sahnenin iki segmenti AYNI ışık
> fazındadır; kesme ışığı değiştirmez.

```
CLEAR (S0-S5): hard low key from the RIGHT, sun fixed 8 degrees above
the right horizon, long shadows running left. Fill is weak and shadows
are soft-edged — CORRECT for 1.4% pressure, not an error, not bloom
[Ders 41]. The gas planet is a dim flat presence in the left sky.

FIRST CURTAIN (S6-S8): where stones strike, each impact stands a
4-meter column of dust that settles over 40 seconds; over the outer
ring these columns merge into a thin grey veil. The key light from the
right softens over the ring; contrast stays.

UNDER THE FALL (S9-S11): the ring is under continuous fall; hanging
dust dims the ambient light over the pocked plain, cold and grey. The
cone's sunlit right flank and the column's lit right edge are the
brightest things in frame.

THE EYE (S12-S13): the inner 500-meter disk stands under a clean
column of clear air — no impacts, no dust — a well of full hard
sunlight while the churning grey ring surrounds it. IŞIK = TEMA:
aydınlık tek yer, tehlikenin dibi.

ANTI-BLOOM DIRECTIVE [Ders 3, 29]: 0% bloom on every source. High
contrast between lit and unlit. Yasak kelimeler hiçbir prompt'ta
geçmez: glowing, ethereal, radiant, shimmering, cinematic lighting.
```

---

## ⚙️ PHYSICS BIBLE

```
GRAVITY: 0.11 g (1.1 m/s²). Serbest düşüş — 1 saniyede 0.55 m. Bu bir
ağır çekim değildir; insan ve araç normal hızdadır [Ders 44 · §0.14].

BALLISTIC PHYSICS — filmin çekirdeği:
  Launch speed         40 m/s, every stone, every direction
  Launch fan           45° to 85° elevation — never flatter, never
                       vertical
  Stones               dry cold gravel, 0.1 to 0.6 m
  Fall ring            500 to 1450 m from the cone
  First landings       outer edge, 51 s after launch
  Ring fully falling   72 s after launch — closes outside-in over 21 s
  Impact speed         40 m/s — hard, fast, never floating down
  Impact plume         a 4 m column of dry dust per strike, settling
                       over 40 s, never hovering, never swirling
  Fall density         one stone per 20-meter square every 5 seconds
  After the cone dies  the sky keeps falling for up to 70 s

SMALL VENT (S0-S1): jets at 8 m/s, fan 12 m high, stones land in a
ring 30-55 m out after about 13 s; the 5 m around the vent stays clean.

COLD ERUPTION LOCK: nothing burns anywhere in this film. No fire, no
flame, no ember, no ash, no smoke — the cone vents cold nitrogen gas
and dry gravel. The jets are needle-sharp because the air is thin.

CONTINUOUS MOMENTUM LOCK [Ders 10, 30, 39 + §0.13 ①]: every stone and
grain obeys 1.1 m/s² with continuous physical momentum — rising,
arcing over, falling back. Nothing hovers, nothing freezes mid-air,
nothing flows like liquid. Tek taşın apeks anı asla kadraja alınmaz.

ROVER PHYSICS: 10 m/s on the smooth apron, 8 m/s on the pocked plain;
wheels rotate in ground contact, never slide, never float. In S10 the
front-left wheel drops into a 1.2 m crack and the vehicle pitches
nose-down and stops within 5 meters — it stays there.

CONTACT INTEGRITY [Ders 11, 43]: eldivenli el hiçbir yüzeye erimez.
COLLISION INTEGRITY [Ders 17]: hiçbir nesne diğerinin içinden geçmez;
düşen taş yere değer ve orada kalır.
ENVIRONMENT STABILITY [Ders 6]: zemin, sırt, koni gövdesi ve gemi
statiktir. Hareket eden yalnız taşlar, toz, araç ve insandır.
FACE LOCK [Ders 16] · SUIT CONTINUITY [Ders 8] · VISOR PERSISTENCE
[Ders 5]: Character Bible bloğu her segmentte tekrarlanır.

THIN ATMOSPHERE RULES [KILAVUZ_REHBERI §3.2]: toz yavaş ama kesin
çöker (40 s); gölge zayıf ve yumuşak kenarlı — meşru; dolgu ışığı var
ve motivasyonlu; rüzgâr hiçbir şeyi deviremez; jetler keskin, kabarmaz.
```

---

## 🚫 NEGATIVE BIBLE — ⭐ İKİ ÇEKİRDEK

> Hangisinin nereye gideceği §0.10 tablosunda yazılıdır. Karıştırmak
> A1 hatasıdır.

### ÇEKİRDEK A — TEK ÇEKİMLİ SAHNELER (S1 · S3 · S5 · S7 · S9 · S12 · S13)

```
=== NEGATIVE CORE A ===

Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits, letters or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no lens
flare. Photorealistic skin with pores and fatigue — no airbrushing, no
waxy or plastic texture, no face morphing, identical bone structure
throughout. Suit and equipment identical from first frame to last;
dirt and wear stay fixed. Every stone and grain obeys 0.11 g with
continuous physical momentum — rising, arcing over and falling back —
never hovering, never frozen in mid-air, never flowing like liquid.
There is no liquid anywhere — no water, no ice, no wet look. Nothing
burns: no fire, no flame, no ember, no ash — the cone is cold and the
jets are cold dry gravel. Hands keep a clear boundary at every contact
— no merging, no phasing, no extra fingers, rigid-body collision.
Terrain static except where a stone strikes — no melting terrain, no
warping. No animal, no creature, no vegetation. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain.
===
```

### ÇEKİRDEK B — TEK KESMELİ SAHNELER (S0 · S2 · S4 · S6 · S8 · S10 · S11)

```
=== NEGATIVE CORE B ===
⭐ FARK: "single unbroken take / no cuts" cümlesi YOKTUR. Yerine CUT
SCHEDULE gelir ve her promptta sahnenin kendi kesme saniyesiyle
yazılır. Geri kalan her cümle Çekirdek A ile aynıdır; "from first
frame to last" yerine "before and after the cut" yazılır.

Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits, letters or symbols anywhere
— no subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no lens flare. Photorealistic skin with pores
and fatigue — no airbrushing, no waxy or plastic texture, no face
morphing, identical bone structure throughout. Suit and equipment
identical before and after the cut; dirt and wear stay fixed. Every
stone and grain obeys 0.11 g with continuous physical momentum —
rising, arcing over and falling back — never hovering, never frozen in
mid-air, never flowing like liquid. There is no liquid anywhere — no
water, no ice, no wet look. Nothing burns: no fire, no flame, no
ember, no ash — the cone is cold and the jets are cold dry gravel.
Hands keep a clear boundary at every contact — no merging, no phasing,
no extra fingers, rigid-body collision. Terrain static except where a
stone strikes — no melting terrain, no warping. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
===
```

```
FİLME ÖZEL EK YASAKLAR (uygun segmentlerde vurgulanır)
- No mushroom cloud, no billowing cloud, no rolling bank of dust —
  the jets are needle-sharp streams in 1.4% pressure.
- No slow motion, no speed ramp: stones strike at full speed, the
  rover crosses frame at full real-world speed.
- No high jump, no floating leap: she runs in long LOW flat strides.
- Not miniature, not toy-like (rover, gemi, koni kadrajları).
- No second vehicle, no other tracks except the rover's own wheel
  lines and her boot prints.
```

---
# 🎬 BÖLÜM 2 — SHOT-BY-SHOT PROMPTS (14 SAHNE × 10 s)

> **Kopyalama kuralı:** yalnız kod bloğunun içini kopyala. Türkçe başlık
> ekleme, iki promptu birleştirme (politika reddi alındı, doğrulandı).
>
> **Her sahne tek bir 10 saniyelik üretimdir.** Kesme varsa promptun
> içindedir: MOTION bloğunda segment segment, CUT SCHEDULE bloğunda
> saniyesiyle kilitli. **İmaj promptu yalnız A segmentinin ilk karesidir;**
> B segmentinin referans imajı yoktur — kurulumu video promptunda tam yazılır.
>
> **İnsansız sahne (S3):** negatif çekirdeğin insan cümlesi "No human in
> frame" biçiminde yazılır.

---

## 🎬 SAHNE 0 — HOOK: ÇATLAK FIŞKIRIYOR

_Matkap başında diz çökmüş. Zemin titriyor. 30 metre solda kılcal bir çatlak açılıyor ve kuru çakıl göğe fışkırıyor._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 5+5 = 10.0 s
  A  0.0-5.0 s   50mm · 8 m · yandan, göğüs hizası — matkap + kadın
  ✂  5.0 s       ölçek: geniş-orta → yakın   (+45° açı farkı)
  B  5.0-10.0 s  75mm · 2 m · önden-soldan, yüz + dönüş
  EKSEN   çatlak ve koni SOLDA, rover ve gemi yönü SAĞDA
  KES ANI hareket üzerinde: jet hâlâ yükselirken
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 0 of 14, opening frame. A lone field scientist kneels at a small
drill rig on a pale gravel plain, one second before the ground begins
to shake.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
under a thin nitrogen atmosphere at 1.4% of Earth sea-level pressure.
The sky is deep violet; a huge dim ochre-banded gas planet hangs low
above the LEFT horizon behind a dark ridge 400 meters high, and a
60-meter old gravel cone stands far left, 900 meters away. Hard low
sunlight comes from the RIGHT, 8 degrees above the horizon, throwing
long soft-edged shadows to the left. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
A 38-year-old woman, 1.66 meters tall, compact and quick, kneeling
side-on at a 2.4 meter tripod drill rig, both gloved hands on its
handle. Medium-brown skin with real visible pore texture, dark brown
eyes, black hair cropped close, a thin pale scar through her left
eyebrow, chapped lips. She wears a matte sand-grey exploration suit
with burnt-orange sealed seams along both forearms and across the chest,
a slim dark grey hard-shell chest pack, heavy ribbed boots, and one
fully transparent seamless visor with no tint and no mask beneath it,
her whole face clearly readable. A narrow dark band on her left wrist
shows a slow abstract amber pulse. Fixed wear marks: a dark grey dust
smear across the right thigh, a scuffed patch on the left shoulder, a
film of pale dust along the visor's lower edge. Fifteen meters to the
RIGHT, a 3.0 meter sleek angular four-wheel rover is parked: matte
sand-grey faceted composite body, four 0.8 meter airless alloy mesh wheels, single sunken cockpit seat,
a 0.9 meter dark grey core cylinder under two burnt-orange straps on
its rear cradle — physically accurate perspective, correct engineering
proportions, never miniature or toy-like.

CAMERA:
Shot on a 50mm lens from a fixed position 8 meters away, side-on at
chest height, f/5.6, physically accurate perspective.

LIGHTING:
Clear phase. Hard low key from the right, sun fixed 8 degrees above
the horizon; long shadows run left. Fill is weak and shadow edges are
soft, correct for 1.4% pressure. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Loose gravel rests on the surface. The air is thin;
nothing blows, nothing drifts.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits or symbols anywhere — no
subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no lens flare. Photorealistic skin with pores —
no airbrushing, no waxy texture, no face morphing. Suit and equipment
exactly as described. There is no liquid anywhere — no water, no ice,
no wet look. Nothing burns: no fire, no flame, no ember, no ash. Hands
keep a clear boundary at every contact — no merging, no extra fingers.
Terrain static. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 5.0 s
SETUP: 50mm lens, fixed lockoff 8 meters away, side-on at chest
height. No camera movement inside this segment.
FRAME: a 38-year-old woman in a matte sand-grey exploration suit with
burnt-orange sealed seams, dark grey chest pack and one fully transparent
visor kneels at a 2.4 m tripod drill rig on a pale gravel plain; 15 m
to the RIGHT her 3.0 m angular-bodied rover with four 0.8 m airless alloy mesh wheels
and a 0.9 m core cylinder on its cradle; far LEFT a 60 m gravel cone
900 m away under a dim banded gas planet; hard low sun from the right.
0.5s — Loose gravel grains on the ground begin to jitter in place,
rising and falling millimeters, obeying 0.11 g.
1.5s — The drill string rattles in its clamp; her hands tighten on the
handle.
2.5s — Thirty meters to the LEFT a hairline crack snaps open in the
ground and a fan of dry cold gravel jets upward 12 meters, needle-
sharp streams at 8 meters per second, at full real-world speed.
4.8s — The fan is still climbing; small stones arc over at its top and
start back down.
✂ HARD CUT AT 5.0s

▸ SEGMENT B — 5.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff 2 meters away, from front-left at head
height. No camera movement inside this segment.
FRAME: her head and shoulders. The same woman: medium-brown skin with
visible pores, dark brown eyes, black cropped hair, thin pale scar
through the left eyebrow, fully transparent seamless visor with a film
of pale dust along its lower edge, matte sand-grey suit with
burnt-orange sealed seams, dark grey chest pack. Behind her right
shoulder, out of focus, the parked rover. The rising gravel fan is NOT
in this frame; its faint light plays on the left side of her visor.
5.0s — Her head turns fifteen degrees left toward the fan, eyes
tracking upward.
7.0s — She gives one short controlled exhale; her hands leave the
drill handle.
8.5s — She rises from the kneel in one smooth motion, knees absorbing
the load, gaze still left.
10.0s — Standing, still, watching. Hold.

CUT SCHEDULE:
Exactly one hard cut, at 5.0s, and no others. Each of the two segments
is a single unbroken locked-off take with no camera movement inside
it. No dissolve, no fade, no wipe, no morph, no speed ramp at the cut.
Suit, equipment and lighting identical before and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². The small jet climbs at 8 m/s in needle-sharp
streams; every grain rises, arcs over and falls back with continuous
momentum — never hovering, never frozen in mid-air, never flowing like
liquid. Human movement at full real-world speed, not slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits or symbols anywhere — no
subtitles, no title card, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no lens flare. Photorealistic skin with pores —
no airbrushing, no waxy texture, no face morphing, identical bone
structure. Suit and equipment identical before and after the cut; wear
stays fixed. There is no liquid anywhere. Nothing burns: no fire, no
flame, no ember, no ash — the jet is cold dry gravel. Hands keep a
clear boundary at every contact — no extra fingers. Terrain static
except the crack described. No animal, no creature, no vegetation. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
Emphasis: no dissolve and no morph at the cut — one instant hard cut;
no extra cut anywhere; no slow motion.
```

---

## 🎬 SAHNE 1 — KÜÇÜK HALKA (ÇEHOV 1)

_Fışkıran taşlar geri dönüyor: bir HALKA hâlinde. Deliğin dibi temiz kalıyor. Kural, minyatüründe gösterildi._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s · 💬 2 REPLİK
  32mm · 20 m · yandan-geniş. Kesme YOK — kural tek nefeste izlenmeli.
  Kadın sorar, AI kuralı SÖZLE kilitler: "halka + temiz merkez".
  20 m'de yüz okunmaz → dudak senkron riski sıfır (SUIT AI bloğu).
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 1 of 14. A wide side view: a standing scientist watches the
stones of a small gravel jet begin to land around its vent in a
perfect ring, while the vent's own foot stays untouched.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; a huge dim ochre-banded gas planet low above the LEFT
horizon behind a dark 400 meter ridge; a 60-meter old gravel cone far
left at 900 meters. Hard low sunlight from the RIGHT, 8 degrees up,
long soft-edged shadows running left. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
In mid-frame, small at this distance, a 38-year-old woman, 1.66 meters
tall, standing still in a matte sand-grey exploration suit with
burnt-orange sealed seams, dark grey hard-shell chest pack, heavy ribbed
boots and one fully transparent seamless visor. Her 2.4 m tripod drill
rig stands beside her, her 3.0 m angular-bodied rover parked 15 m to the
right. On the LEFT third of frame, a 2 meter crack vent still spitting
a thin 12 meter fan of dry gravel; around it, at 30 to 55 meters from
the vent, the first returning stones strike the plain and stand small
columns of dry dust — the strikes forming a visible RING, while the
5 meters around the vent itself stay clean and unmarked. Physically
accurate perspective, correct engineering proportions, never miniature
or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 20 meters away,
f/8, side-on at chest height so the vent, the ring of strikes and the
watching figure are all in frame, physically accurate perspective.

LIGHTING:
Clear phase. Hard low key from the right, sun fixed 8 degrees above
the horizon; each small dust column catches the light on its right
side. Weak fill, soft shadow edges, correct for 1.4% pressure. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Stones launched at 8 m/s return after about 13
seconds and strike at the same speed — hard and fast, never floating.
Each strike stands a small column of dry dust that settles over
seconds. Every grain keeps continuous momentum.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no lens
flare. Photorealistic skin — no airbrushing, no waxy texture. Suit and
equipment exactly as described; wear stays fixed. There is no liquid
anywhere — no water, no ice, no wet look. Nothing burns: no fire, no
flame, no ember, no ash — the vent is cold and the stones are cold dry
gravel. Every stone obeys 0.11 g with continuous momentum — never
hovering, never frozen in mid-air, never flowing like liquid. Terrain
static except where a stone strikes. No animal, no creature, no
vegetation. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts:

SETUP: 32mm anamorphic lens, fixed lockoff 20 meters away, side-on at
chest height. No camera movement at any point.
FRAME: the standing woman mid-frame in her matte sand-grey suit with
burnt-orange sealed seams and transparent visor, drill rig beside her,
rover 15 m right; on the left third the small 2 m crack vent with its
thinning 12 m gravel fan; pale gravel plain, violet sky, dim banded
gas planet low left, hard low sun from the right.

AUDIO & DIALOGUE — Audio: Clean dialogue only. Two spoken lines,
one speaker at a time, she speaks first, then the synthetic voice
replies. Ambient: dry distant impact thuds at midground, faint thin
hiss in the background. The lines are HEARD ONLY — never shown as
text, no subtitles, no captions, no transcript. At 20 meters her
face is too small for lips to read; her voice is close and clear
over the suit channel. The replying voice is a calm neutral
SYNTHETIC voice from her helmet speaker — off-screen only, it has
no body, no face, no avatar, and no second figure ever appears.

0.0s — The fan from the vent is thinning; the last stones of its
launch climb away from it while the first launched stones come down
far out: strikes at 55 meters from the vent, then 50, then 45 — each
strike a hard fast impact standing a small column of dry dust.
3.0s — The strikes walk INWARD in a closing ring: 45 meters, 40, 35 —
a circle of small dust columns forming around the vent. She does not
move. As her head tracks one falling stone down, she says in a low
even voice: "Analyze that."
5.5s — The calm synthetic voice replies while the innermost strikes
land at 30 meters and stop there: "Ejecta returned in a ring, thirty
to fifty-five meters out. The center is untouched." The ground
within 30 meters of the vent — and especially the 5 meters around
its foot — takes NOT ONE stone and stays clean, pale and unmarked.
8.5s — The fan dies to nothing. The ring of dust columns begins to
settle, each column sinking straight down over seconds. She stands
silent, reading the clean center.
10.0s — Still frame: a ring of settling dust on the plain, a clean
center, one unmoving watcher. Hold.

PHYSICS:
0.11 g — 1.1 m/s². Stones strike at 8 m/s, hard and fast, never
floating down. Dust columns are dry, needle-thin in 1.4% pressure
air, and settle straight down over seconds — never hovering, never
swirling. Everything at full real-world speed, not slow motion.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no lens
flare. Photorealistic skin — no airbrushing, no waxy texture, no face
morphing. Suit and equipment identical from first frame to last; wear
stays fixed. There is no liquid anywhere — no water, no ice, no wet
look. Nothing burns: no fire, no flame, no ember, no ash — the vent is
cold and the stones are cold dry gravel. Every stone and grain obeys
0.11 g with continuous momentum — never hovering, never frozen in
mid-air, never flowing like liquid. Terrain static except where a
stone strikes — struck ground keeps its small crater. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
```

---

## 🎬 SAHNE 2 — KONİ PATLIYOR

_Ana koni ateşliyor: 40 m/s'lik çakıl yelpazesi. O koşup araca biniyor. Film artık bir kronometre._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 4+6 = 10.0 s
  A  0.0-4.0 s   32mm · 400 m · çok geniş — koni ve doğan sütun
  ✂  4.0 s       ölçek: çok geniş → geniş-orta   (+60° açı farkı)
  B  4.0-10.0 s  50mm · 6 m · rover yanı — biniş ⚠️ KLON SICAK NOKTASI
  EKSEN   koni SOLDA; biniş sonrası hareket SAĞA başlar
  KES ANI hareket üzerinde: sütun yükselirken
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 2 of 14. A very wide frame one breath before the main cone
fires: the old gravel cone stands silent on the left, the pale plain
runs to the right, and the ground at the cone's foot has just begun
to shiver.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; a huge dim ochre-banded gas planet low in the LEFT sky
behind a dark ridge 400 meters high. Hard low sunlight from the RIGHT,
8 degrees above the horizon, long soft-edged shadows running left. No
water, no ice, no liquid, no vegetation, no animal life.

SUBJECT:
On the LEFT third of frame, 400 meters away, a 60-meter old gravel
cone with a 40 meter mouth, its flanks dark loose scree. Around its
foot, a smooth DARK glassy ash apron spreads for hundreds of meters,
unmarked and unpocked, ending at a SHARP visible boundary line where
the pale plain beyond begins — and that outer plain is pocked with old
impact craters 0.5 to 2 meters wide with bright ray-spokes. In the
lower right, small in frame, the tiny figure of the scientist beside
her parked 3.0 meter angular-bodied rover and tripod drill rig, 900 meters
from the cone. Physically accurate perspective, correct engineering
proportions, realistic scale relationships — the cone and rover never
miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 400 meters from
the cone, f/8, low at chest height so the cone, its dark apron, the
boundary line and the pocked plain all read in one frame, physically
accurate perspective.

LIGHTING:
Clear phase. Hard low key from the right; the cone's right flank is
lit, its left flank dark. The dark apron reads matte and smooth
against the pale pocked plain. Weak fill, soft shadow edges, correct
for 1.4% pressure. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Still air, thin at 1.4% pressure. Loose grains at
the cone's foot jitter in place, rising and falling millimeters.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone. No
text, digits or symbols anywhere — no subtitles, no title card, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no lens
flare. There is no liquid anywhere — no water, no ice, no wet look.
Nothing burns: no fire, no flame, no ember, no ash, and there is
nothing rising from the cone yet. Terrain static except the described
jitter. No animal, no creature, no vegetation. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 4.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 400 meters from the cone,
low at chest height. No camera movement inside this segment.
FRAME: the 60 m gravel cone on the left third with its smooth dark
glassy apron and the sharp boundary line to the pale pocked plain;
the tiny figure and rover lower right at 900 m; violet sky, dim
banded gas planet low left, hard low sun from the right.
0.8s — The cone FIRES: a cone-shaped spray of dry cold gravel bursts
from its 40 meter mouth at 40 meters per second, needle-sharp streams
fanning between 45 and 85 degrees in every direction, at full
real-world speed. A deep low thud rolls through the thin air.
2.5s — The spray climbs past 100 meters, each stream sharp and
straight, stones visibly discrete; loose scree rattles down the
cone's flanks.
3.8s — The spray tops 150 meters — level with the half-height of the
400 m ridge behind it — and keeps climbing.
✂ HARD CUT AT 4.0s

▸ SEGMENT B — 4.0 to 10.0 s
SETUP: 50mm lens, fixed lockoff 6 meters away, side-on at chest
height beside the parked rover. No camera movement inside this
segment.
FRAME: the 3.0 m angular-bodied rover: matte sand-grey faceted composite body, four
0.8 m airless alloy mesh wheels, single sunken cockpit seat with cross-chest harness
strap, 0.9 m dark grey core cylinder under two burnt-orange straps on
the rear cradle. The cone and its rising spray stand far LEFT in the
background. EXACTLY ONE HUMAN anywhere in this segment.
4.0s — The woman in the matte sand-grey suit with burnt-orange seam
tape, dark grey chest pack and fully transparent visor runs into
frame from the left in two long LOW flat strides — stride 3 meters,
height half a meter, fast ground contact, not slow motion.
5.5s — She swings into the seat in one motion, knees absorbing the
load; the seat held EXACTLY one person before and holds exactly one
now.
7.0s — Her right hand pulls the cross-chest harness strap tight; her
left hand takes the steering yoke.
8.0s — The rover lurches and accelerates RIGHTWARD, wheels biting,
loose gravel kicked back in low fast arcs that land within a meter.
10.0s — The rover exits frame right at 8 meters per second, two
wheel lines cut into the gravel behind it.

CUT SCHEDULE:
Exactly one hard cut, at 4.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera movement
inside it. No dissolve, no fade, no wipe, no morph, no speed ramp at
the cut. Suit, vehicle and lighting identical before and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². Launch speed 40 m/s, fan 45 to 85 degrees; every
stone rises, arcs over and falls back with continuous momentum —
never hovering, never frozen, never flowing like liquid. Rover at 8
m/s on pocked ground, wheels always rotating in ground contact. Human
and vehicle at full real-world speed, not slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection; the cockpit is strictly single-seat. No text, digits
or symbols anywhere — no subtitles, no watermark, no HUD. 0% bloom, no
glow filter, no soft focus, no lens flare. Photorealistic skin with
pores — no airbrushing, no waxy texture, no face morphing. Suit and
equipment identical before and after the cut; wear stays fixed. There
is no liquid anywhere. Nothing burns: no fire, no flame, no ember, no
ash — the cone is cold and the spray is cold dry gravel; never a
mushroom cloud, never a billowing bank. Every stone obeys 0.11 g with
continuous momentum. Hands keep a clear boundary at every contact — no
merging, no extra fingers. Terrain static except described motion. No
animal, no creature, no vegetation. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: no dissolve and no
morph at the cut — one instant hard cut; no extra cut anywhere.
```

---

## 🎬 SAHNE 3 — ⭐ VİRAL: TAŞ SÜTUNU (İNSANSIZ)

_Sütunun içi. Yüzlerce taş, dümdüz iğne akıntılar hâlinde, saniyede kırk metreyle yükseliyor. Henüz hiçbiri düşmüyor._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s · İNSANSIZ
  100mm · 200 m · sütunun orta gövdesi. Saf görsel; KESİLEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 3 of 14. Inside the rising column: hundreds of discrete stones
climbing in straight needle-sharp streams against a violet sky and
the face of a banded gas planet. No human in frame.

ENVIRONMENT:
Above a small moon at 0.11 g with a thin nitrogen atmosphere at 1.4%
of Earth sea-level pressure. The frame looks across at the middle
body of the eruption column, 100 to 250 meters above the ground; deep
violet sky behind it, and the huge dim ochre-banded disk of the gas
planet filling the upper left of frame. Hard low sunlight from the
RIGHT edge-lights every stone. No ground in frame. No water, no ice,
no liquid, no vegetation, no animal life.

SUBJECT:
The column of dry cold gravel in cross-view: dozens of parallel
needle-sharp streams of discrete stones, each stone 0.1 to 0.6 meters
across, tumbling slowly around its own axis while rising fast along a
straight ballistic line at 40 meters per second. The streams fan
slightly apart with height, between 45 and 85 degrees of elevation.
The stones are matte pale grey, edge-lit hard from the right, sharp
against the dark violet sky and the dim bands of the planet. Every
stone in this frame is RISING; nothing falls yet. Fine dry dust
trails thin and straight behind the larger stones and does not
billow, because the air is only 1.4% pressure.

CAMERA:
Shot on a 100mm lens from a fixed position 200 meters from the
column, f/4, level, physically accurate perspective — the stones read
their true 0.1 to 0.6 meter scale, never miniature.

LIGHTING:
Clear phase. Hard low key from the right; each stone carries a bright
right edge and a dark left face. The gas planet is dim and flat, far
darker than the sunlit stones. 0% bloom, high contrast.

PHYSICS:
0.11 g — 1.1 m/s². Launch speed 40 m/s; each stone follows a clean
ballistic line with continuous momentum, decelerating imperceptibly
at this height, tumbling as it climbs. Nothing hovers, nothing
freezes, nothing floats.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no figure
of any kind. No text, digits or symbols anywhere — no subtitles, no
title card, no watermark. 0% bloom, no glow filter, no soft focus, no
lens flare. There is no liquid anywhere — no water, no ice, no wet
look. Nothing burns: no fire, no flame, no ember, no ash — the stones
are cold dry gravel; never a mushroom cloud, never a billowing bank,
never rolling smoke. Every stone obeys 0.11 g with continuous
momentum — never hovering, never frozen in mid-air, never flowing
like liquid, never swirling. No animal, no creature, no vegetation.
No Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts, no human:

SETUP: 100mm lens, fixed lockoff 200 meters from the column body,
level, framing the column's middle 100 to 250 meters above ground.
No camera movement at any point.
FRAME: dozens of parallel needle-sharp streams of discrete pale grey
stones, 0.1 to 0.6 m each, rising through frame at 40 meters per
second against the deep violet sky and the dim ochre-banded face of
the gas planet upper left; hard low sun from the right edge-lighting
every stone.
0.0s — Stones stream steadily upward through the whole frame at 40
m/s, each one tumbling slowly around its own axis while its path
stays a straight ballistic line, at full real-world speed.
3.0s — Fresh pulses of stones enter from the bottom of frame in
waves, a new wave every second or so; thin straight dust trails
follow the largest stones and stay needle-thin in the 1.4% pressure
air.
6.0s — The streams continue without pause; the spacing between
individual stones reads clearly — they are discrete rocks, never a
solid mass, never a cloud.
9.0s — Still rising, wave after wave. Nothing in this frame falls
yet; the sky is still loading. Hold.

PHYSICS:
0.11 g — 1.1 m/s². Every stone keeps continuous ballistic momentum:
rising fast, decelerating imperceptibly at this height, tumbling as
it goes. Nothing hovers, nothing freezes mid-air, nothing drifts
sideways — the air is far too thin to push a stone.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. No human in frame — no person, no figure
of any kind. No text, digits or symbols anywhere — no subtitles, no
title card, no watermark. 0% bloom, no glow filter, no soft focus, no
lens flare. There is no liquid anywhere — no water, no ice, no wet
look. Nothing burns: no fire, no flame, no ember, no ash — the stones
are cold dry gravel; never a mushroom cloud, never a billowing bank,
never rolling smoke. Every stone obeys 0.11 g with continuous
momentum — never hovering, never frozen in mid-air, never flowing
like liquid, never swirling. No animal, no creature, no vegetation.
No Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
```

---

## 🎬 SAHNE 4 — DIŞA KAÇIŞ (ÇEHOV 2)

_Apaçık çözüm: gemiye sür. Ama kamera zemini gösteriyor — kaçış yolu eski çarpma kraterleriyle delik deşik. Zemin bir haritadır._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 5+5 = 10.0 s
  A  0.0-5.0 s   32mm · 3 m · yerden, ön planda ESKİ kraterler
  ✂  5.0 s       ölçek: çok geniş → geniş-orta   (+35° açı farkı)
  B  5.0-10.0 s  50mm · 12 m · önden-sağdan çeyrek — rota + gemi parıltısı
  EKSEN   koni ve sütun SOLDA, gemi SAĞDA; hareket SAĞA
  KES ANI hareket üzerinde: rover kadrajı geçerken
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 4 of 14. Ground level on the pocked plain: old impact craters
fill the foreground, and the fleeing rover is about to cross the
frame behind them. The ground itself is the map of every old fall.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; a huge dim ochre-banded gas planet low in the LEFT sky;
far left, 900 meters away, the 60-meter cone with its full eruption
column rising at 40 m/s, needle-sharp streams of stones topping 300
meters. Hard low sunlight from the RIGHT, 8 degrees up, long
soft-edged shadows running left. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
The FOREGROUND is the subject: old impact pockmarks 0.5 to 2 meters
wide crowd the pale gravel from the camera to the middle distance,
each with a shallow bowl and bright ray-spokes of ejected grains —
dozens of them, overlapping, old and sharp-rimmed. Behind them, 20
meters away, the 3.0 meter sleek angular four-wheel rover crosses left
to right at 8 meters per second: matte sand-grey faceted composite body, four 0.8
m airless alloy mesh wheels, the woman in the matte sand-grey suit and transparent
visor low in the single cockpit seat, the 0.9 m dark grey core cylinder under
two burnt-orange straps on the rear cradle. Physically accurate
perspective, correct engineering proportions, realistic scale
relationships — never miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position at ground level,
3 meters from the nearest crater, f/8, so the pocked ground fills the
lower half of frame and the rover rides the middle band, physically
accurate perspective.

LIGHTING:
Clear phase. Hard low key from the right; every crater rim carries a
bright right lip and a small pool of soft shadow. Weak fill, correct
for 1.4% pressure. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². The rover holds 8 m/s on the pocked ground, wheels
rotating in contact, kicked gravel landing in low fast arcs within a
meter. The distant column keeps rising at 40 m/s with continuous
momentum.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone. No
text, digits or symbols anywhere — no subtitles, no watermark, no
HUD. 0% bloom, no glow filter, no soft focus, no lens flare. There is
no liquid anywhere — no water, no ice, no wet look. Nothing burns: no
fire, no flame, no ember, no ash — the distant column is cold dry
gravel, never a mushroom cloud. Every stone obeys 0.11 g with
continuous momentum — never hovering, never flowing like liquid.
Terrain static except described motion. No animal, no creature, no
vegetation. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 5.0 s
SETUP: 32mm anamorphic lens, fixed lockoff at ground level, 3 meters
from the foreground craters. No camera movement inside this segment.
FRAME: old impact pockmarks 0.5-2 m wide with bright ray-spokes
crowding the foreground; the pale plain behind; far LEFT the cone and
its rising column of needle-sharp stone streams; violet sky, dim
banded planet.
0.0s — The rover enters frame LEFT at 8 meters per second, 20 meters
behind the craters: sand-grey open faceted composite body, four 0.8 m airless alloy mesh wheels
biting the gravel, the suited woman low in the seat, the 0.9 m core
cylinder jolting once against its two burnt-orange straps.
2.0s — The rover threads BETWEEN two old craters without slowing; its
wheels kick low fast arcs of grains that land within a meter, at full
real-world speed.
4.8s — The rover nears frame right, its two fresh wheel lines cutting
through the field of old pockmarks.
✂ HARD CUT AT 5.0s

▸ SEGMENT B — 5.0 to 10.0 s
SETUP: 50mm lens, fixed lockoff 12 meters ahead of the rover's path,
front-right three-quarter view at chest height. No camera movement
inside this segment.
FRAME: the rover coming toward and past the camera's right side,
heading RIGHT; on the far right horizon, 1200 meters ahead, the small
bright shape of a 14 meter three-legged lander catches the low sun;
the cone and its column stand far LEFT background; the plain between
is pocked with old craters all the way out.
5.0s — The rover comes on at 8 m/s, front wheels rising and dropping
over the uneven pocked ground, suspension arms working; the woman's
head is level, eyes fixed ahead — medium-brown skin, dark brown eyes,
black cropped hair behind the fully transparent visor, sand-grey suit
with burnt-orange sealed seams.
7.5s — Her head turns fifteen degrees LEFT toward the cone — the
column now tops 300 meters — and snaps straight back to the route.
10.0s — The rover passes close along the camera's right edge and out
of frame, wheel noise a dry crunch in thin air.

CUT SCHEDULE:
Exactly one hard cut, at 5.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera movement
inside it. No dissolve, no fade, no wipe, no morph, no speed ramp at
the cut. Suit, vehicle and lighting identical before and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². Rover constant 8 m/s on pocked ground, wheels
always rotating in ground contact, never sliding, never floating.
Kicked grains obey 0.11 g and land within a meter. The distant column
rises at 40 m/s with continuous momentum. Full real-world speed, not
slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin with pores — no airbrushing,
no waxy texture, no face morphing, identical bone structure. Suit and
equipment identical before and after the cut; wear stays fixed. There
is no liquid anywhere. Nothing burns: no fire, no flame, no ember, no
ash — the column is cold dry gravel, never a mushroom cloud. Every
stone obeys 0.11 g with continuous momentum — never hovering, never
flowing like liquid. Hands keep a clear boundary on the yoke — no
merging, no extra fingers. Terrain static except described motion. No
animal, no creature, no vegetation. No second vehicle, no other
tracks except the rover's own. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: no dissolve and no
morph at the cut — one instant hard cut; no extra cut anywhere; no
slow motion.
```

---

## 🎬 SAHNE 5 — SÜTUN SIRTI GEÇİYOR (SAYAÇ A)

_Sütunun tepesi 400 metrelik sırtın üstüne çıkıyor. Gök doluyor. Tek yukarı bakış bu sahnede._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  32mm · 80 m · alçak-geniş; sütun + sırt + geçen rover tek kadrajda.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 5 of 14. A low wide frame: the eruption column's top climbs
past the crest of the dark 400-meter ridge behind it while the tiny
rover crosses the plain below. The sky is loading.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; a huge dim ochre-banded gas planet low in the LEFT sky.
On the left half of frame, 900 meters away, the 60-meter cone fires
its column: needle-sharp streams of discrete stones at 40 meters per
second, the column's top now LEVEL with the crest of the dark ridge
400 meters high behind it. Hard low sunlight from the RIGHT, 8
degrees up. No water, no ice, no liquid, no vegetation, no animal
life.

SUBJECT:
The vertical race on the left: dark ridge crest as a hard horizontal
reference line, and the pale column of rising stones crossing it. On
the lower right, small, the 3.0 meter angular-bodied rover heads right at
8 meters per second across the pocked plain: sand-grey faceted composite body,
four 0.8 m airless alloy mesh wheels, the suited woman in the single cockpit seat, the 0.9
m dark grey core cylinder on the rear cradle. Two wheel lines trail
behind it. Physically accurate perspective, correct engineering
proportions — never miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 80 meters from
the rover's line of travel, f/8, low at knee height so the ridge
crest and the column top sit high in frame, physically accurate
perspective.

LIGHTING:
Clear phase, last minutes of it. Hard low key from the right; the
column's right edge is lit bright, its left side dark against the
ridge. Weak fill, soft shadow edges, correct for 1.4% pressure. 0%
bloom.

PHYSICS:
0.11 g — 1.1 m/s². The column climbs at 40 m/s launch speed, stones
decelerating along clean ballistic lines with continuous momentum;
the rover holds 8 m/s, wheels in ground contact.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. There is no liquid anywhere — no water, no ice,
no wet look. Nothing burns: no fire, no flame, no ember, no ash — the
column is cold dry gravel; never a mushroom cloud, never a billowing
bank. Every stone obeys 0.11 g with continuous momentum — never
hovering, never frozen in mid-air, never flowing like liquid. Terrain
static except described motion. No animal, no creature, no
vegetation. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts:

SETUP: 32mm anamorphic lens, fixed lockoff 80 meters from the rover's
line, low at knee height. No camera movement at any point.
FRAME: left half — the erupting cone at 900 m, its column of
needle-sharp stone streams, and the dark 400 m ridge behind it, crest
reading as a hard horizontal line; lower right — the rover crossing
rightward at 8 m/s on the pocked plain; violet sky, dim banded
planet, hard low sun from the right.
0.0s — The column's top sits exactly LEVEL with the ridge crest.
Fresh waves of stones pulse up through it at 40 m/s; the rover rolls
right, wheels working over old pockmarks.
3.0s — The column's top climbs visibly PAST the crest — clear
daylight opens between the crest line and the column's tip.
5.5s — In the rover the woman's helmeted head tips back for one
second — the single upward look of the film — then levels again to
the route. Her transparent visor catches the low sun.
8.0s — The column top stands well above the ridge now, still fed
from below, wave after wave.
10.0s — The rover reaches frame right; the column owns the left sky.
Hold.

PHYSICS:
0.11 g — 1.1 m/s². Launch 40 m/s; stones climb along straight
ballistic lines with continuous momentum, tumbling slowly; none of
them fall in this frame yet. Rover constant 8 m/s, wheels rotating
in ground contact. Full real-world speed, not slow motion.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin — no waxy texture, no face
morphing. Suit and equipment identical from first frame to last.
There is no liquid anywhere. Nothing burns: no fire, no flame, no
ember, no ash — cold dry gravel only; never a mushroom cloud. Every
stone obeys 0.11 g with continuous momentum — never hovering, never
frozen mid-air, never flowing like liquid. Terrain static except
described motion. No animal, no creature, no vegetation. No second
vehicle. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain.
```

---

## 🎬 SAHNE 6 — DIŞ HALKA KAPANIYOR (DÜNYA HAYIR DER)

_İlk taşlar tam kaçış yoluna, dış kenara düşüyor. 45 derecelik taşlar en uzağa gider ama en önce iner. Fren._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 6+4 = 10.0 s
  A  0.0-6.0 s   50mm · 10 m · yandan — sürüş + önde beliren perde
  ✂  6.0 s       ölçek: geniş-orta → yakın   (+50° açı farkı)
  B  6.0-10.0 s  75mm · 2.5 m · önden — yüz, eller, fren · 💬 1 REPLİK
                 (yalnız AI konuşur; kadının dudakları KIPIRDAMAZ —
                 yakın planda dudak senkron riski böyle sıfırlanır)
  EKSEN   koni SOLDA, perde SAĞ-ÖNDE (dış kenar); hareket SAĞA, duruşla biter
  KES ANI hareket üzerinde: fren kayması sürerken
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 6 of 14. Side view of the rover at full speed heading right —
one second before the first returning stones cut the road ahead.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; dim ochre-banded gas planet low LEFT; far left the
erupting cone, its column of needle-sharp stone streams standing
taller than the dark 400 m ridge behind it. Hard low sunlight from
the RIGHT, 8 degrees up. The plain ahead of the rover, to the right,
runs pocked and open toward a small bright three-legged lander on the
horizon. No water, no ice, no liquid, no vegetation, no animal life.

SUBJECT:
The 3.0 meter sleek angular four-wheel rover crossing frame left to
right at 8 meters per second: matte sand-grey faceted composite body with faded
burnt-orange markings, four 0.8 m airless alloy mesh wheels on faired suspension
arms, single sunken cockpit seat, rear cradle carrying the 0.9 m dark grey
core cylinder under two burnt-orange straps. In the seat, the
38-year-old woman: sand-grey suit with burnt-orange sealed seams, dark
grey chest pack, fully transparent seamless visor, both gloved hands
on the yoke, body leaned into the drive. Physically accurate
perspective, correct engineering proportions, realistic scale
relationships — never miniature or toy-like.

CAMERA:
Shot on a 50mm lens from a fixed position 10 meters away, side-on at
chest height, f/5.6, physically accurate perspective.

LIGHTING:
First Curtain phase begins this scene. Hard low key from the right,
but over the far right distance a thin grey veil is starting to
stand where the first strikes land. Contrast stays high. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Rover at 8 m/s, wheels rotating in ground
contact; kicked grains land within a meter. Returning stones strike
at 40 m/s — hard, fast, never floating.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone. No
text, digits or symbols anywhere — no subtitles, no watermark, no
HUD. 0% bloom, no glow filter, no soft focus, no lens flare.
Photorealistic skin — no waxy texture. Suit and equipment exactly as
described. There is no liquid anywhere. Nothing burns: no fire, no
flame, no ember, no ash. Every stone obeys 0.11 g with continuous
momentum — never hovering, never flowing like liquid. Terrain static
except described motion. No animal, no creature, no vegetation. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 6.0 s
SETUP: 50mm lens, fixed lockoff 10 meters away, side-on at chest
height. No camera movement inside this segment.
FRAME: the rover crossing left to right at 8 m/s on the pocked plain;
far LEFT the cone and its column; far RIGHT the open route and the
distant lander glint; violet sky, hard low sun from the right.
0.0s — The rover holds full speed rightward, suspension arms working
over old pockmarks, the core cylinder riding steady under its two
burnt-orange straps.
2.0s — Far ahead on the RIGHT, along the plain's outer distance, a
LINE of dust columns bursts up one after another — the first
returning stones striking at 40 meters per second, each strike
standing a 4-meter column of dry dust. The line runs squarely across
the rover's route.
4.5s — A single stone strikes sixty meters AHEAD of the rover with a
hard dry thud and stands its own 4-meter column; the bright strikes
march visibly CLOSER, walking inward.
5.7s — She brakes hard: all four wheels bite, the rover's nose dips,
loose gravel sprays forward in low fast arcs and lands within a
meter.
✂ HARD CUT AT 6.0s

▸ SEGMENT B — 6.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff 2.5 meters away, from the front at
chest height. No camera movement inside this segment.
FRAME: her upper body and face over the open cockpit rim of the rover,
which slides to its final stop during the first second. Medium-brown
skin with visible pores, dark brown eyes wide and reading, black
cropped hair, thin pale scar through the left eyebrow, fully
transparent seamless visor with pale dust along its lower edge,
sand-grey suit with burnt-orange sealed seams, dark grey chest pack.
Beyond her right shoulder, out of focus, dust columns keep standing
up across the blocked route.
6.0s — The rover halts; her body loads forward against the
cross-chest harness; her right hand leaves the yoke and grabs the
harness strap by reflex.
7.2s — One short controlled exhale; the visor stays clear. Her eyes
track the marching strikes beyond frame right.
7.8s — A calm neutral SYNTHETIC voice speaks from her helmet
speaker, off-screen — HER LIPS DO NOT MOVE, her mouth stays closed:
"Impact line ahead. Every outward route is closing."
9.3s — The right hand returns to the yoke. Her jaw sets. She is
already reading the other direction.
10.0s — Still. Hold.

AUDIO — Audio: Clean dialogue only. One spoken line, synthetic
voice only; the woman never speaks in this scene. The line is heard
only — no subtitles, no captions, no transcript; the voice has no
body, no avatar, no second figure. Ambient: dry impact thuds
midground, faint hiss background.

CUT SCHEDULE:
Exactly one hard cut, at 6.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera movement
inside it. No dissolve, no fade, no wipe, no morph, no speed ramp at
the cut. Suit, vehicle and lighting identical before and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². Stones strike at 40 m/s, hard and fast, never
floating down; each strike stands a 4 m dust column that settles over
40 seconds, never hovering, never swirling. Rover braking is real
deceleration with weight transfer. Full real-world speed, not slow
motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin with pores — no
airbrushing, no waxy texture, no face morphing, identical bone
structure. Suit and equipment identical before and after the cut;
wear stays fixed. There is no liquid anywhere. Nothing burns: no
fire, no flame, no ember, no ash — cold dry stone only; never a
mushroom cloud. Every stone obeys 0.11 g
with continuous momentum — never hovering, never frozen mid-air,
never flowing like liquid. Hands keep a clear boundary — no merging,
no extra fingers. Terrain static except where a stone strikes. No
animal, no creature, no vegetation. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: no dissolve and no
morph at the cut — one instant hard cut; no extra cut anywhere; no
slow motion.
```

---

## 🎬 SAHNE 7 — HESAP (AI ANALİZİ)

_Durmuş araçta on saniye. Sağda kapanan perde, solda hiç vurulmamış koyu örtü. Bir soru, bir analiz — ve sessiz kalan bir karar._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s · 💬 2 REPLİK
  32mm · 25 m · yandan-geniş. Yedi kesmeli filmde kesmesiz on saniye.
  Kadın sorar (≤2 s), AI analiz döner (≤5 s) — KARAR yine sessizdir:
  AI veri verir, yönü o seçer. KESİLEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 7 of 14. The whole geometry of survival in one static frame:
the stopped rover in the middle, the closing curtain of strikes on
the right, and the dark untouched apron of the cone on the left.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; dim ochre-banded gas planet low LEFT. LEFT third: the
erupting 60 m cone at 900 meters with its full column, and spreading
from its foot the smooth DARK glassy ash apron, unmarked, ending at a
sharp boundary line against the pale pocked plain. RIGHT third: a
field of standing dust columns where stones keep striking — a slow
grey curtain across the outward route; beyond it, tiny on the
horizon, the bright three-legged lander. Hard low sunlight from the
RIGHT filters through the curtain. No water, no ice, no liquid, no
vegetation, no animal life.

SUBJECT:
Center frame, side-on: the stopped 3.0 meter angular-bodied rover, four
0.8 m airless alloy mesh wheels still, the 0.9 m dark grey core cylinder on its
cradle, and the woman upright in the single cockpit seat — sand-grey suit,
burnt-orange sealed seams, transparent visor — her head turned RIGHT
toward the curtain. Two wheel lines run back behind the rover.
Physically accurate perspective, correct engineering proportions —
never miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 25 meters away,
side-on at chest height, f/8, framing cone and apron left, rover
center, strike curtain right, physically accurate perspective.

LIGHTING:
First Curtain phase. The key from the right is softened by the
standing dust over the outer ring; the dark apron on the left lies in
clean unfiltered light. The frame is literally brighter toward the
cone. 0% bloom, contrast preserved.

PHYSICS:
0.11 g — 1.1 m/s². Strikes at 40 m/s continue on the right; each 4 m
dust column settles over 40 seconds while new ones stand up. The
apron and the inner disk take no strikes at all.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin — no waxy texture. Suit and
equipment exactly as described. There is no liquid anywhere. Nothing
burns: no fire, no flame, no ember, no ash. Every stone obeys 0.11 g
with continuous momentum — never hovering, never flowing like liquid.
Terrain static except where a stone strikes. No animal, no creature,
no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts:

SETUP: 32mm anamorphic lens, fixed lockoff 25 meters away, side-on at
chest height. No camera movement at any point.
FRAME: stopped rover center with the woman upright in the seat; the
cone, its column and its dark unmarked apron on the LEFT; the
curtain of strike columns walking inward on the RIGHT; the tiny
lander beyond it; violet sky, banded planet low left.
AUDIO & DIALOGUE — Audio: Clean dialogue only. Two spoken lines,
one speaker at a time, she speaks first, then the synthetic voice
replies. The lines are HEARD ONLY — never shown as text, no
subtitles, no captions, no transcript. At 25 meters her face is too
small for lips to read; her voice is close and clear over the suit
channel. The replying voice is a calm neutral SYNTHETIC voice from
her helmet speaker — off-screen only, no body, no face, no avatar,
no second figure. Ambient: dry impact thuds at midground, faint
thin hiss in the background.

0.0s — Stones keep striking on the right at 40 m/s, each standing
its 4-meter dust column; the nearest strike stands forty meters from
the rover. She sits motionless, head turned right, watching the
curtain walk.
2.0s — She says in a low even voice: "Analyze the dark ground."
3.5s — Her head swings slowly LEFT — past the camera line — to the
cone, the column, and the smooth dark apron at its foot where not
one dust column stands and not one crater marks the ground.
5.0s — The calm synthetic voice replies in the same flat tone: "No
impact recorded inside the apron. Not one, at any time. Beyond the
line I have no data."
8.0s — Her head returns front. Both hands settle onto the yoke, the
right hand closing over the power lever. She does not move it yet.
The decision is hers alone and she makes it in silence.
10.0s — Absolute stillness except the marching strikes behind her.
Hold.

PHYSICS:
0.11 g — 1.1 m/s². Strikes at 40 m/s, hard and fast; dust columns
settle over 40 seconds while new ones rise; the curtain's nearest
edge creeps closer through the scene. No strike lands left of the
rover. Full real-world speed.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits or symbols anywhere — no subtitles, no watermark, no HUD. 0%
bloom, no glow filter, no soft focus, no lens flare. Photorealistic
skin — no airbrushing, no waxy texture, no face morphing. Suit and
equipment identical from first frame to last; wear stays fixed. There
is no liquid anywhere. Nothing burns: no fire, no flame, no ember, no
ash — cold dry stone on cold dry ground. Every stone obeys 0.11 g
with continuous momentum — never hovering, never frozen mid-air,
never flowing like liquid, never swirling. Hands keep a clear
boundary — no merging, no extra fingers. Terrain static except where
a stone strikes. No animal, no creature, no vegetation. No Unreal
Engine or video game aesthetic. Photorealistic, 35mm grain.
```

---

## 🎬 SAHNE 8 — ⭐ DORUK: TERS DÖNÜŞ

_Direksiyon sonuna kadar sola. Güç kolu tam ileri. Araç, kaçtığı şeye doğru dönüyor. Seçim üç saniyenin içinde._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 3+7 = 10.0 s
  A  0.0-3.0 s   75mm · 1.5 m · eller — DORUK SEGMENTİN İÇİNDE
  ✂  3.0 s       ölçek: yakın → çok geniş   (+70° açı farkı)
  B  3.0-10.0 s  32mm · 30 m · dönüş ve içe hızlanma
  EKSEN   koni SOLDA — değişmez; hareket bu sahneden itibaren SOLA
  KES ANI hareket üzerinde: direksiyon dönerken
  🎬 KURGU NOTU: 0.19 ② — karar anında ses BİR saniye tamamen kesilir
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 8 of 14. Close on two gloved hands at the moment of the film's
one decision: the left hand hard on the steering yoke, the right hand
resting on the power lever, one breath before both commit.

ENVIRONMENT:
On a small moon at 0.11 g, thin nitrogen atmosphere at 1.4% of Earth
sea-level pressure, aboard a stopped angular-bodied rover on a pale
pocked gravel plain. Beyond the open faceted composite body, out of focus: LEFT,
the pale mass of the distant eruption column; RIGHT, soft grey dust
columns standing where stones strike. Hard low sunlight from the
RIGHT crosses the frame. No water, no ice, no liquid, no vegetation,
no animal life.

SUBJECT:
Her two gloved hands and the rover's controls fill the frame: a
clean matte-composite steering yoke and, on its right stalk, a
single short power lever, both machine-finished and worn smooth at
the grip points. The
gloves are matte sand-grey with burnt-orange sealed seams at the wrists;
a narrow dark band on the left wrist shows a slow abstract amber
pulse and nothing else. Her right knee and the edge of the cross-
chest harness read soft at frame bottom. Every knuckle of the gloves
is defined; fingers keep a clear structural boundary against yoke and
lever — rigid-body contact, no merging. Physically accurate
perspective.

CAMERA:
Shot on a 75mm lens from a fixed position 1.5 meters away, angled
down at the controls, f/4, shallow depth holding both hands sharp,
physically accurate perspective.

LIGHTING:
First Curtain phase. Hard low key from the right rakes across the
gloves and the matte controls; soft weak fill, correct for 1.4% pressure. 0%
bloom.

PHYSICS:
0.11 g — 1.1 m/s². The rover is stopped; the hands are still. The
only motion in frame is the slow amber pulse on the wrist band.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone; no
face in this frame, only hands. No text, digits, letters or symbols
anywhere — the wrist band shows only an abstract pulse, no numerals,
no display; no subtitles, no watermark, no HUD. 0% bloom, no glow
filter, no soft focus, no lens flare. Gloves and equipment exactly as
described; wear stays fixed. Hands keep a clear boundary at every
contact — no merging, no phasing, no extra fingers, rigid-body
collision. There is no liquid anywhere. Nothing burns. Terrain
static. No animal, no creature, no vegetation. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 3.0 s
SETUP: 75mm lens, fixed lockoff 1.5 meters away, angled down at the
rover's controls. No camera movement inside this segment.
FRAME: two gloved hands, the matte-composite steering yoke, the single
power lever; sand-grey gloves with burnt-orange wrist tape, amber
pulse band on the left wrist; harness edge soft at frame bottom.
0.0s — Stillness. The left hand flexes once on the yoke.
1.0s — The left hand spins the yoke HARD LEFT, all the way to its
stop, and holds it there — the decision, inside this segment.
2.2s — The right hand pushes the power lever fully forward in one
clean stroke. The deck under the frame begins to vibrate.
✂ HARD CUT AT 3.0s

▸ SEGMENT B — 3.0 to 10.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 30 meters away, side-on
at chest height. No camera movement inside this segment.
FRAME: the full rover on the pocked plain; the cone, its column and
its dark apron far LEFT; the curtain of strike columns RIGHT and
behind; violet sky, banded planet low left. EXACTLY ONE HUMAN.
3.0s — The rover slews through a tight turn, all four 0.8 m mesh
wheels biting, kicked gravel arcing low and landing within a meter;
the 0.9 m core cylinder strains against its two burnt-orange straps.
5.0s — Out of the turn, it accelerates LEFTWARD — toward the cone —
reaching 8 meters per second on the pocked ground, the woman leaned
forward in the seat, sand-grey suit, transparent visor, both hands
committed.
7.5s — A stone strikes one hundred meters BEHIND it with a hard dry
thud, standing a 4-meter dust column; two more strike farther back,
the curtain now chasing, walking inward after the rover.
10.0s — The rover drives hard LEFT toward the dark apron line in the
distance, strikes stitching the ground behind it. Exit approach —
no exit yet. Hold the run.

CUT SCHEDULE:
Exactly one hard cut, at 3.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera movement
inside it. No dissolve, no fade, no wipe, no morph, no speed ramp at
the cut. Suit, vehicle and lighting identical before and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². Rover at 8 m/s on pocked ground, wheels always in
ground contact through the turn — real load transfer, no drifting
float. Strikes at 40 m/s, hard and fast; dust columns settle over 40
seconds, never hovering. Full real-world speed, not slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD; the wrist band shows only an
abstract pulse. 0% bloom, no glow filter, no soft focus, no lens
flare. Photorealistic skin and gloves — no waxy texture, no face
morphing. Suit and equipment identical before and after the cut; wear
stays fixed. There is no liquid anywhere. Nothing burns: no fire, no
flame, no ember, no ash — cold dry gravel only. Every stone obeys
0.11 g with continuous momentum — never hovering, never frozen
mid-air, never flowing like liquid. Hands keep a clear boundary at
every contact — no merging, no extra fingers, rigid-body collision.
Terrain static except where a stone strikes. No animal, no creature,
no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain. Emphasis: no dissolve and no morph at
the cut — one instant hard cut; no extra cut anywhere; no slow
motion.
```

---

## 🎬 SAHNE 9 — ⭐ İÇE KOŞU (VİRAL — TEK ÇEKİM)

_Kadrajı sağdan sola tam hızda geçen araç. Arkasında zemine dikiş atan taşlar. En yakını otuz metre. Kesme yok — nefes de yok._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s
  32mm · 40 m · yandan. Filmin en gergin sahnesi TEK ÇEKİMDİR (§0.2.1 ⑤).
  KESİLEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 9 of 14. The chase in one wide frame: the rover flat-out from
right to left, the falling stones stitching the plain behind it, the
dark cone and its column ahead of it on the left.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; dim ochre-banded gas planet low LEFT; the erupting 60 m
cone and its column of needle-sharp stone streams on the left third,
its smooth dark glassy apron spreading from its foot toward the
camera's left; the pale pocked plain filling the rest. Hanging dust
from previous strikes greys the air over the RIGHT distance; the
light there is dimmer and cold, while the left of frame stays in
clean hard low sun from the right edge. No water, no ice, no liquid,
no vegetation, no animal life.

SUBJECT:
The 3.0 meter angular-bodied rover at full speed RIGHT TO LEFT, 8 meters
per second: matte sand-grey faceted composite body, four 0.8 m airless alloy mesh wheels
biting, suspension arms working, the woman low over the yoke in her
sand-grey suit with burnt-orange sealed seams and fully transparent
visor, the 0.9 m dark grey core cylinder under its two straps.
BEHIND the rover, to the right, three standing 4-meter dust columns
mark fresh strikes — the nearest thirty meters back — and one new
stone is caught mid-fall above them. Physically accurate
perspective, correct engineering proportions, realistic scale
relationships — never miniature or toy-like.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 40 meters from
the rover's line, side-on at chest height, f/8, physically accurate
perspective.

LIGHTING:
Under-the-Fall phase. Ambient over the right half is dimmed by
hanging dust, cold and grey; the cone's sunlit right flank and the
column's lit right edge are the brightest things in frame. Contrast
preserved. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Falling stones strike at 40 m/s, hard and fast;
each stands a 4 m dust column that settles over 40 seconds. The
rover holds 8 m/s, wheels always rotating in ground contact.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone. No text, digits or symbols anywhere — no
subtitles, no watermark, no HUD. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin — no waxy texture. Suit and
equipment exactly as described. There is no liquid anywhere. Nothing
burns: no fire, no flame, no ember, no ash — cold dry gravel only;
never a mushroom cloud. Every stone obeys 0.11 g with continuous
momentum — never hovering, never frozen in mid-air, never flowing
like liquid. Terrain static except where a stone strikes. No animal,
no creature, no vegetation. No second vehicle. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts:

SETUP: 32mm anamorphic lens, fixed lockoff 40 meters from the
rover's line, side-on at chest height. No camera movement at any
point.
FRAME: the pocked plain; the cone, column and dark apron left; grey
hanging dust dimming the right distance; the rover entering from the
RIGHT at full speed heading LEFT. EXACTLY ONE HUMAN.
0.0s — The rover tears in from frame right at 8 meters per second,
all four wheels throwing low fast arcs of gravel; behind it a stone
strikes with a hard dry thud and stands a 4-meter dust column,
thirty meters back.
2.0s — Two more strikes behind it, twenty-five and twenty meters
back, walking closer; the woman stays low over the yoke, head
level, eyes on the dark apron line ahead-left.
4.5s — A stone falls PAST the upper frame ahead of the rover and
strikes wide of its line with a thud; the rover does not swerve —
there is nowhere better to steer; speed is the only answer.
6.5s — The core cylinder slams once against its straps as the
wheels cross an old crater rim; her shoulders twitch with the jolt;
her right hand stays on the lever.
8.5s — The nearest strike now fifteen meters behind; the rover
holds its line, closing on the left edge of frame, the dark smooth
apron visibly nearer beyond it.
10.0s — The rover exits frame LEFT at full speed, three fresh dust
columns settling in its wake. Hold on the churned plain.

PHYSICS:
0.11 g — 1.1 m/s². Rover constant 8 m/s on pocked ground, wheels
rotating in ground contact, never sliding, never floating; real
suspension motion over crater rims. Stones strike at 40 m/s — hard,
fast, never floating down; dust columns settle over 40 seconds and
never hover. Full real-world speed, not slow motion.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions, no
jump cuts, no angle change. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits or symbols anywhere — no subtitles, no watermark, no HUD. 0%
bloom, no glow filter, no soft focus, no lens flare. Photorealistic
skin — no airbrushing, no waxy texture, no face morphing. Suit and
equipment identical from first frame to last; wear stays fixed. There
is no liquid anywhere. Nothing burns: no fire, no flame, no ember, no
ash — cold dry stone on cold dry ground; never a mushroom cloud.
Every stone obeys 0.11 g with continuous momentum — never hovering,
never frozen mid-air, never flowing like liquid, never swirling.
Terrain static except where a stone strikes — struck ground keeps its
crater. No animal, no creature, no vegetation. No second vehicle, no
other tracks except the rover's own. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain.
```

---

## 🎬 SAHNE 10 — ÇATLAK BÜYÜMÜŞ: ARAÇ DÜŞÜYOR

_S0'daki kılcal çatlak artık 1.2 metre. Ön sol tekerlek içine düşüyor. Araç biter. Yol yaya devam eder._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 6+4 = 10.0 s
  A  0.0-6.0 s   50mm · 8 m · yandan — çatlak + saplanış
  ✂  6.0 s       açı: +40° (yandan → arka-çeyrek)  ⚠️ İNİŞ = KLON SICAK NOKTASI
  B  6.0-10.0 s  50mm · 6 m · arka-çeyrek — iniş ve koşunun başlangıcı
  EKSEN   koni SOLDA; hareket SOLA
  KES ANI hareket üzerinde: gövde öne yatarken
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 10 of 14. Side view: the rover races left at full speed — and
across its path, cutting the plain from foreground to background,
runs a fresh open crack 1.2 meters wide.

ENVIRONMENT:
A flat plain of pale grey regolith gravel on a small moon at 0.11 g,
thin nitrogen atmosphere at 1.4% of Earth sea-level pressure. Deep
violet sky; dim ochre-banded gas planet low LEFT; the erupting cone
and its column close now on the left third, its smooth dark apron
beginning 200 meters beyond the crack; hanging dust greys the right
distance where stones keep striking. Hard low sun from the RIGHT,
dimmed over the plain, clean toward the cone. No water, no ice, no
liquid, no vegetation, no animal life.

SUBJECT:
The 3.0 meter angular-bodied rover mid-frame heading LEFT at 8 meters
per second — sand-grey faceted composite body, four 0.8 m airless alloy mesh wheels, the woman
low in the seat in her sand-grey suit with burnt-orange sealed seams
and transparent visor, the 0.9 m dark grey core cylinder under two
burnt-orange straps. Eight meters ahead of it, the CRACK: a clean
dark fissure 1.2 meters wide with sharp broken edges, running
across the whole frame at a shallow diagonal, its inside in deep
shadow. Physically accurate perspective, correct engineering
proportions — never miniature or toy-like.

CAMERA:
Shot on a 50mm lens from a fixed position 8 meters away, side-on at
chest height, f/5.6, physically accurate perspective.

LIGHTING:
Under-the-Fall phase. Cold dimmed ambient over the plain; the
crack's near lip catches a hard edge of low sun; the cone's flank
bright left. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Rover at 8 m/s, wheels in ground contact. The
crack is static — it does not widen on camera; it simply waits.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone. No
text, digits or symbols anywhere — no subtitles, no watermark, no
HUD. 0% bloom, no glow filter, no soft focus, no lens flare.
Photorealistic skin — no waxy texture. Suit and equipment exactly as
described. There is no liquid anywhere. Nothing burns: no fire, no
flame, no ember, no ash. Every stone obeys 0.11 g with continuous
momentum. Terrain static except described motion. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 6.0 s
SETUP: 50mm lens, fixed lockoff 8 meters away, side-on at chest
height. No camera movement inside this segment.
FRAME: the rover racing LEFT at 8 m/s; the 1.2 meter crack cutting
diagonally across its path eight meters ahead; the cone and column
left, greyed falling-dust distance right.
0.0s — The rover comes on hard; she sees the crack — her body
stiffens, the yoke twitches half a turn but there is no room to
turn at this speed.
1.5s — The FRONT-LEFT wheel drops into the crack. The suspension arm
slams its stop; the nose pitches down hard; the rear lifts, both
rear wheels clawing air for half a second, kicked gravel arcing low.
3.0s — The rover slams to rest nose-down in the crack, deck tilted
twelve degrees forward, front-left wheel buried to the hub. The
core cylinder strains forward against its two straps and HOLDS. She
is thrown against the cross-chest harness; her right hand grabs the
strap.
5.0s — Dust from the impact settles fast around the hull. She is
already releasing the harness buckle with both hands.
✂ HARD CUT AT 6.0s

▸ SEGMENT B — 6.0 to 10.0 s
SETUP: 50mm lens, fixed lockoff 6 meters away, rear three-quarter
view at chest height, the tilted rover in the right of frame, the
open route to the dark apron running LEFT. No camera movement
inside this segment. EXACTLY ONE HUMAN in this segment — the seat
she leaves stays EMPTY behind her, no second figure appears
anywhere.
6.0s — She swings out of the seat in one motion, boots hitting the
gravel together, knees absorbing the load.
7.0s — She runs LEFT in long LOW flat strides — each stride 3
meters, body never rising more than half a meter, ground contact
fast and frequent, at full real-world speed, not slow motion, no
floating.
8.5s — A stone strikes forty meters behind the wrecked rover with a
hard dry thud, standing its 4-meter dust column; she does not look
back.
10.0s — She exits frame LEFT at 5 meters per second, running low
and hard; the tilted rover holds still, nose in the crack, the
core cylinder still strapped on its cradle. Hold one beat.

CUT SCHEDULE:
Exactly one hard cut, at 6.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera
movement inside it. No dissolve, no fade, no wipe, no morph, no
speed ramp at the cut. Suit, vehicle and lighting identical before
and after the cut.

PHYSICS:
0.11 g — 1.1 m/s². The crash is rigid-body: the wheel drops, the
arm hits its stop, the chassis pitches and stays — nothing bends
like rubber, nothing bounces twice. Her run is 5 m/s in long LOW
flat strides — 0.11 g shortens nothing and floats nothing because
her strides stay low. Stones strike at 40 m/s. Full real-world
speed throughout, not slow motion.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone, no
figure in any reflection; the vacated seat stays EMPTY. No text,
digits or symbols anywhere — no subtitles, no watermark, no HUD. 0%
bloom, no glow filter, no soft focus, no lens flare. Photorealistic
skin — no airbrushing, no waxy texture, no face morphing, identical
bone structure. Suit and equipment identical before and after the
cut; wear stays fixed. There is no liquid anywhere. Nothing burns:
no fire, no flame, no ember, no ash. Every stone obeys 0.11 g with
continuous momentum — never hovering, never frozen mid-air, never
flowing like liquid. Hands keep a clear boundary at every contact —
no merging, no extra fingers, rigid-body collision. Terrain static
except described motion. No animal, no creature, no vegetation. No
high jump, no floating leap. No Unreal Engine or video game
aesthetic. Photorealistic, 35mm grain. Emphasis: no dissolve and no
morph at the cut — one instant hard cut; no extra cut anywhere; no
slow motion.
```

---

## 🎬 SAHNE 11 — ÇİZGİ + BEDEL

_Koşarak ÇİZGİYİ geçiyor: delikli ova biter, hiç vurulmamış koyu örtü başlar. Arkasında bir taş, dokuz yıllık karotu eziyor._

```
⚙️ KESME PLANI — 2 segment · 1 kesme · 5+5 = 10.0 s
  A  0.0-5.0 s   32mm · 15 m · alçak — ÇİZGİ ve geçiş
  ✂  5.0 s       ölçek: çok geniş → orta-yakın (tele)   (+45° açı farkı)
  B  5.0-10.0 s  75mm · 100 m (tele) · enkaz — karotun ezilişi
  EKSEN   koni SOLDA; koşu SOLA; enkaz SAĞ gerido
  KES ANI hareket üzerinde: koşu adımı ortasında
```

### 📸 IMAGE PROMPT — segment A'nın ilk karesi

```
SCENE:
Scene 11 of 14. Ground level on the boundary itself: to the right,
pale gravel pocked with craters; to the left, smooth dark glassy
ground with not one mark on it. A sharp line between them crosses
the frame — and a running figure is three strides from it.

ENVIRONMENT:
A small moon at 0.11 g, thin nitrogen atmosphere at 1.4% of Earth
sea-level pressure. Deep violet sky; dim ochre-banded gas planet low
LEFT; the erupting cone fills the left background 500 meters away,
its column of needle-sharp stone streams rising at 40 m/s; grey
hanging dust dims the right distance where stones keep striking.
The light over the dark apron ahead-left is CLEAN — a well of hard
low sun — while the plain behind-right lies under a cold grey veil.
No water, no ice, no liquid, no vegetation, no animal life.

SUBJECT:
THE LINE: a sharp visible boundary running across the frame at a
shallow diagonal — on its right the pale pocked regolith, on its
left the smooth dark glassy ash apron, unmarked for centuries. The
woman runs toward it from the right in long LOW flat strides:
1.66 meters, sand-grey suit with burnt-orange sealed seams, dark grey
chest pack, fully transparent visor, dark grey dust smear on the
right thigh. Twelve meters behind her a fresh 4-meter dust column
stands where a stone has just struck. Physically accurate
perspective — never miniature.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position 15 meters away,
very low at knee height so the boundary line reads from foreground
to background, f/8, physically accurate perspective.

LIGHTING:
Under-the-Fall phase, at its edge. Cold grey dimmed light on the
right half; clean hard low sun on the dark apron left — the frame
splits its light along the same line that splits the ground. 0%
bloom, high contrast.

PHYSICS:
0.11 g — 1.1 m/s². She runs at 5 m/s, strides 3 meters long and
half a meter high, fast ground contact. Stones strike at 40 m/s
behind her; no strike lands left of the line.

NEGATIVE:
Exactly one human in frame — no second person, no crew, no clone. No
text, digits or symbols anywhere — no subtitles, no watermark, no
HUD. 0% bloom, no glow filter, no soft focus, no lens flare.
Photorealistic skin — no waxy texture. Suit and equipment exactly as
described. There is no liquid anywhere — the dark ground is dry
glassy ash, not wet, no reflections of a wet kind. Nothing burns: no
fire, no flame, no ember, no ash in the air. Every stone obeys 0.11
g with continuous momentum. Terrain static except where a stone
strikes. No animal, no creature, no vegetation. No high jump, no
floating leap. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, 1 kesme içinde

```
MOTION — 10 seconds, two fixed setups joined by one hard cut:

▸ SEGMENT A — 0.0 to 5.0 s
SETUP: 32mm anamorphic lens, fixed lockoff 15 meters away, very low
at knee height, the boundary line running diagonally through frame.
No camera movement inside this segment.
FRAME: pale pocked gravel right, smooth dark glassy apron left, the
sharp line between; the cone and column left background; grey veil
right distance. EXACTLY ONE HUMAN.
0.0s — She runs in from the RIGHT at 5 meters per second in long
LOW flat strides, breath rhythmic, arms driving; a stone strikes
twelve meters behind her with a hard dry thud and stands its
4-meter dust column.
2.0s — Her boots hit the last pale ground — one stride, two — and
CROSS the line onto the dark glass. The sound of her steps changes:
from dry crunch to a harder, cleaner knock.
3.5s — Two strides INSIDE the dark ground she lets her pace fall,
shoulders dropping, and turns her head half back toward the plain —
still moving away from the line, slowing.
4.8s — Behind her, beyond the line, another strike stands its
column; on her side of the line, nothing falls and nothing marks
the ground.
✂ HARD CUT AT 5.0s

▸ SEGMENT B — 5.0 to 10.0 s
SETUP: 75mm lens, fixed lockoff reading 100 meters back across the
line toward the wrecked rover, compressed telephoto view at chest
height. No camera movement inside this segment.
FRAME: the tilted rover nose-down in the crack, sharp; the 0.9 m
dark grey core cylinder on its rear cradle under two burnt-orange
straps; around it the pocked plain under falling stones; hanging
grey dust behind. NO HUMAN in this frame — she is out of this
field of view; the empty seat is visible and stays empty.
5.0s — A stone strikes twenty meters from the rover, then another
at ten, columns of dry dust standing and beginning to settle.
6.5s — A 0.5 meter stone comes down at 40 meters per second
squarely onto the rear cradle: the cradle frame buckles, both
straps snap taut and part, and the core cylinder's casing SPLITS —
dark core fragments scatter in low fast arcs and land within
meters, obeying 0.11 g.
8.0s — The dust of the strike rises 4 meters and starts straight
back down; the rover settles deeper on its broken cradle, holding
still.
10.0s — The wreck stands tilted and still under the thinning dust,
one strap end hanging. Hold.

CUT SCHEDULE:
Exactly one hard cut, at 5.0s, and no others. Each of the two
segments is a single unbroken locked-off take with no camera
movement inside it. No dissolve, no fade, no wipe, no morph, no
speed ramp at the cut. Lighting continuous across the cut.

PHYSICS:
0.11 g — 1.1 m/s². Her run 5 m/s, strides low and flat. Stone
impact at 40 m/s is rigid-body: metal buckles once and stays
buckled; fragments arc low and land; nothing bounces twice, nothing
floats. Dust columns settle over 40 seconds, never hovering. Full
real-world speed, not slow motion.

NEGATIVE:
At most one human across this scene — no second person, no crew, no
clone; in segment B, NO human in frame and the rover's seat is
EMPTY. No text, digits or symbols anywhere — no subtitles, no
watermark, no HUD. 0% bloom, no glow filter, no soft focus, no lens
flare. Photorealistic materials — no waxy texture. Suit, vehicle and
wreck state identical before and after the cut except the described
strike; wear stays fixed. There is no liquid anywhere — the dark
ground is dry glassy ash, never wet. Nothing burns: no fire, no
flame, no ember, no ash in the air — the strike is cold stone on
cold metal. Every stone and fragment obeys 0.11 g with continuous
momentum — never hovering, never frozen mid-air, never flowing like
liquid. Terrain static except where a stone strikes. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain. Emphasis: no dissolve and no morph at
the cut — one instant hard cut; no extra cut anywhere; no slow
motion.
```

---

## 🎬 SAHNE 12 — OVERVIEW: GÖZ

_Bütün geometri tek karede: patlayan koni, temiz koyu disk, kaynayan gri halka — ve diskin içinde tek bir nokta. Kapak adayı._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s · OVERVIEW (filmde tek)
  32mm · sırt omzundan, 2.5 km · yüksek-geniş. KESİLEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 12 of 14. From high on the dark ridge's shoulder: the whole
machine of the fall seen at once — the erupting cone, the clean
dark disk at its foot, and the churning grey ring of strikes
closing it in. One tiny figure stands inside the disk.

ENVIRONMENT:
A small moon at 0.11 g, thin nitrogen atmosphere at 1.4% of Earth
sea-level pressure, seen from 2500 meters, high on the shoulder of
the dark 400 m ridge. Deep violet sky above; the huge dim
ochre-banded gas planet fills the upper LEFT of frame. Hard low
sunlight from the RIGHT rakes the whole plain. No water, no ice, no
liquid, no vegetation, no animal life.

SUBJECT:
The full geometry, center frame: the 60-meter cone with its column
of needle-sharp stone streams rising 600 meters, leaning none; at
its foot the smooth DARK glassy disk reaching 500 meters out,
CLEAN — under a well of clear hard light, not one dust column
inside it; around that disk, from 500 to 1450 meters, the RING — a
churning grey annulus of standing and settling dust columns where
stones strike continuously, dozens of 4-meter columns at every
moment; beyond the ring the pale untouched plain, and far right, a
tiny bright three-legged lander, 2100 meters from the cone, safely
outside. Inside the dark disk, small but distinct, ONE standing
human figure, and near the disk's edge the tiny tilted wreck of the
rover just outside the line. Physically accurate perspective,
correct engineering proportions — never miniature or toy-like, true
map-like scale.

CAMERA:
Shot on a 32mm anamorphic lens from a fixed position on the ridge
shoulder 2500 meters away, high wide angle looking down the plain,
f/11, physically accurate perspective.

LIGHTING:
The Eye phase. The ring lies under its own grey veil, cold and
dim; the inner disk stands in a clean column of clear air, taking
full hard low sun — the brightest ground in frame. IŞIK = TEMA. 0%
bloom, high contrast.

PHYSICS:
0.11 g — 1.1 m/s². The column rises at 40 m/s; stones fall into the
annulus at 40 m/s; every dust column settles over 40 seconds while
new ones stand. Nothing falls inside the 500-meter disk.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions,
no jump cuts, no angle change. Exactly one human in frame — one
tiny figure, no second person anywhere on the plain. No text,
digits or symbols anywhere — no subtitles, no title card, no
watermark. 0% bloom, no glow filter, no soft focus, no lens flare.
There is no liquid anywhere — no water, no ice, no wet look.
Nothing burns: no fire, no flame, no ember, no ash — cold dry
gravel only; never a mushroom cloud, never a billowing bank. Every
stone obeys 0.11 g with continuous momentum — never hovering, never
frozen mid-air, never flowing like liquid. Terrain static except
the described strikes. No animal, no creature, no vegetation. No
Unreal Engine or video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts:

SETUP: 32mm anamorphic lens, fixed lockoff high on the ridge
shoulder, 2500 meters out, wide down-angle on the whole plain. No
camera movement at any point.
FRAME: the erupting cone and its 600 m column center-left; the
clean dark 500 m disk at its foot in a well of clear light; the
churning grey ring of strike columns from 500 to 1450 meters; the
pale plain beyond; the tiny lander far right; the tiny wreck at
the disk's edge; ONE tiny figure inside the disk; violet sky, the
banded planet upper left.
0.0s — The whole system runs at once: waves of stones pulse up the
column at 40 m/s; across the ring, strikes land steadily — a new
4-meter dust column standing somewhere every second while older
ones sink straight down.
3.0s — The ring's inner edge stays EXACTLY at the line of the dark
disk: strike after strike walks close to it and none crosses. The
disk holds clean and bright.
6.0s — The tiny figure inside the disk walks slowly toward the
cone, small deliberate steps, alive and unhurried.
8.5s — The eruption column flickers once at its base — a first
missed pulse — then feeds again; the ring churns on.
10.0s — The machine turns: rise, fall, ring, eye. Hold.

PHYSICS:
0.11 g — 1.1 m/s². Continuous ballistic circulation at true scale:
launch 40 m/s, fall 40 m/s, settle 40 s. The inner disk takes zero
strikes; the ring takes one stone per 20-meter square every 5
seconds. Full real-world speed — at 2500 meters this reads as slow
majesty, but nothing is slowed.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions,
no jump cuts, no angle change. Exactly one human in frame — one
tiny figure, no second person. No text, digits or symbols anywhere.
0% bloom, no glow filter, no soft focus, no lens flare. There is no
liquid anywhere. Nothing burns: no fire, no flame, no ember, no
ash — cold dry gravel only; never a mushroom cloud, never a
billowing bank, never rolling smoke. Every stone obeys 0.11 g with
continuous momentum — never hovering, never frozen mid-air, never
flowing like liquid, never swirling. Terrain static except where
stones strike. No animal, no creature, no vegetation. No second
vehicle. No Unreal Engine or video game aesthetic. Photorealistic,
35mm grain.
```

---

## 🎬 SAHNE 13 — FİNAL: GÖZÜN İÇİNDE

_Temiz koyu zeminde tek başına. Otuz metre ötede çizginin ardında gök hâlâ düşüyor. Oturuyor ve bekliyor. Held frame._

```
⚙️ KESME PLANI — 1 segment · 0 kesme · 10.0 s · HELD FRAME
  50mm · 12 m · yandan. Filmin son karesi bir duruştur. KESİLEMEZ.
```

### 📸 IMAGE PROMPT

```
SCENE:
Scene 13 of 14, the film's closing frame. A lone figure stands on
smooth dark glassy ground in clean hard light, and thirty meters
behind her, beyond a sharp line on the ground, the sky is still
falling.

ENVIRONMENT:
A small moon at 0.11 g, thin nitrogen atmosphere at 1.4% of Earth
sea-level pressure. The smooth dark glassy ash apron fills the
foreground and midground, unmarked, faintly sheened but bone-dry;
the sharp boundary line crosses the frame thirty meters behind her,
and beyond it the pale plain churns under falling stones — standing
grey dust columns, one fresh strike caught mid-burst. The erupting
cone rises at the LEFT edge, its column still fed. Far RIGHT, tiny
on the horizon beyond the ring, the bright three-legged lander.
Deep violet sky; the huge dim banded gas planet low left. Clean
hard low sunlight from the RIGHT floods the apron — the eye of the
fall is the brightest ground in frame. No water, no ice, no liquid,
no vegetation, no animal life.

SUBJECT:
The 38-year-old woman standing side-on, center frame, facing RIGHT
— toward the ring, the wreck and the unreachable lander: 1.66
meters, compact, sand-grey suit with burnt-orange sealed seams along
both forearms and across the chest, slim dark grey chest pack,
heavy ribbed boots, one fully transparent seamless visor, her face
readable through it — medium-brown skin, dark brown eyes steady,
black cropped hair, thin pale scar through the left eyebrow. Fixed
wear marks: dark grey dust smear on the right thigh, scuffed left
shoulder, pale dust along the visor's lower edge. Her hands hang
empty. Her boot prints are the only marks on the dark ground.
Physically accurate perspective.

CAMERA:
Shot on a 50mm lens from a fixed position 12 meters away, side-on
at chest height, f/5.6, physically accurate perspective.

LIGHTING:
The Eye phase. Full clean hard key from the right on her and the
dark ground; the ring beyond the line lies under its cold grey
veil. The frame holds light and fall in one image. 0% bloom.

PHYSICS:
0.11 g — 1.1 m/s². Beyond the line, stones strike at 40 m/s and
dust columns settle over 40 seconds. On her side of the line,
nothing moves but her.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions,
no jump cuts, no angle change. Exactly one human in frame — no
second person, no crew, no clone, no figure in any reflection. No
text, digits or symbols anywhere — no subtitles, no title card, no
end card, no credits, no watermark. 0% bloom, no glow filter, no
soft focus, no lens flare. Photorealistic skin with pores and
fatigue — no airbrushing, no waxy texture. Suit and equipment
exactly as described; wear stays fixed. There is no liquid anywhere
— the dark ground is dry glassy ash, never wet. Nothing burns: no
fire, no flame, no ember, no ash in the air. Every stone obeys
0.11 g with continuous momentum — never hovering, never flowing
like liquid. Terrain static except where stones strike beyond the
line. No animal, no creature, no vegetation. No Unreal Engine or
video game aesthetic. Photorealistic, 35mm grain.
```

### 🎥 VIDEO PROMPT — 10 saniye, tek kesintisiz çekim

```
MOTION — 10 seconds, one fixed setup, no cuts — the film's held
closing frame:

SETUP: 50mm lens, fixed lockoff 12 meters away, side-on at chest
height. No camera movement at any point.
FRAME: the woman standing center on the smooth dark apron in clean
hard light, facing RIGHT; the sharp ground line thirty meters
behind her; beyond it the churning ring — grey dust columns
standing and settling, fresh strikes at 40 m/s; the cone's column
at the left edge; the tiny lander far right beyond the ring.
0.0s — She stands still, breathing visibly, shoulders lifting and
settling. A strike lands beyond the line with a distant dry thud;
she does not flinch.
2.5s — Her head turns slowly from the wreck's direction to the
lander's tiny shape on the horizon, and holds there. Between her
and it, the whole falling ring.
5.0s — She lowers herself to sit on the dark ground, knees up,
forearms on knees — a controlled, unhurried motion in 0.11 g,
settling softly.
7.0s — She watches. The ring keeps falling; the light on her stays
clean and hard; her breath is the loudest thing in the world.
10.0s — Held frame: seated figure, bright ground, falling sky
beyond the line. No fade. The film simply ends here.

PHYSICS:
0.11 g — 1.1 m/s². Her sit-down is real weight settling softly, not
floating. Beyond the line, stones strike at 40 m/s and dust settles
over 40 seconds. Nothing crosses the line. Full real-world speed.

NEGATIVE:
Single unbroken take: no cuts, no camera movement, no transitions,
no jump cuts, no angle change — and no fade-out at the end, the
frame holds to the last. Exactly one human in frame — no second
person, no crew, no clone, no figure in any reflection. No text,
digits or symbols anywhere — no subtitles, no title card, no end
card, no credits, no watermark. 0% bloom, no glow filter, no soft
focus, no lens flare. Photorealistic skin with pores and fatigue —
no airbrushing, no waxy texture, no face morphing, identical bone
structure. Suit and equipment identical from first frame to last;
wear stays fixed. There is no liquid anywhere — the dark ground is
dry glassy ash, never wet. Nothing burns: no fire, no flame, no
ember, no ash in the air. Every stone obeys 0.11 g with continuous
momentum — never hovering, never frozen mid-air, never flowing like
liquid. Hands keep a clear boundary at every contact. Terrain
static except where stones strike beyond the line. No animal, no
creature, no vegetation. No Unreal Engine or video game aesthetic.
Photorealistic, 35mm grain.
```

---

# 🎶 BÖLÜM 3 — MÜZİK PROMPTU

> `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` akışına göre: önce §17 künyesi,
> sonra §14 tempo hizalaması, §15.1 sub-bass oktav eşlikçisi, §10
> müziksiz sahne.

```
§17 KÜNYE — bu cümle yazılmadan müzik promptu yazılmaz:
"İzleyici bu novum'u OKUNABİLİR BİR GEOMETRİ olarak okumalı — tehdit
 kaostan değil balistikten gelir; taşları atan şey bir basınçtır ve
 kimseye kızgın değildir."
→ Müzik bu yüzden canavar değil, SARKAÇ tonunda. Filmin gerçek
  perküsyonu taşların kendisidir: S6'dan itibaren gerçek çarpma
  sesleri partisyonun üstüne DÜZENSİZ vuruşlar olarak biner ve müzik
  onlarla asla senkron olmaz — düzenli nabız (insan) ile düzensiz
  yağış (dünya) iki ayrı katman olarak duyulur.

§10 MÜZİKSİZ SAHNE: S12 (Overview). Tam sessizlik — yalnız koninin
     uzak alçak tıslaması. En yüksek görsel, en düşük ses.

§14 TEMPO — 10 saniyelik sahne ızgarasına hizalı (72/96/144 BPM)
⭐ EK KURAL — bu filme özel: müzik KESMEYE hizalanır.
   Vuruş, planlı kesme saniyelerine (3.0 · 4.0 · 5.0 · 6.0) düşer.
   Kesme ile vuruş çakışırsa kesme "montaj hatası" değil "ritim"
   olarak okunur — sahne içi kesmenin en ucuz sigortası.

💬 DİYALOG KURALI — S1, S6 ve S7'de replik anında partisyon diyaloğun
   altına iner (duck); replik üstünde yalnız nabız kalır ve müzik sesi
   asla örtmez. Ses katmanı üçü geçmez: diyalog önde · mekanik sesler
   ortada · koni tıslaması arkada (VEO kılavuzu §7).
```

```
Genre: Sparse, dry percussive score for a film about ballistics — a
pendulum, not a monster. Lean electronic-orchestral with real found
percussion.

Instrumentation: A single soft mallet pulse on a deep drum — one hit
per beat, never resolving, never changing key — as the human clock of
the film. A dry wooden tick-tock counter-rhythm enters when the small
vent fires (Scene 0, at 2.5 s) and dies when its ring finishes falling
(end of Scene 1). A low sustained brass pedal, no vibrato, builds
under the main eruption (Scene 2) and holds as a floor through Scenes
3-5 while a thin high tone rides above the rising stone column. From
Scene 6 the world joins the orchestra: real dry stone-impact thuds,
IRREGULAR and unquantized, land over the score and never lock to the
grid — the ordered pulse against the disordered fall. Everything but
the pulse drops out for the stopped-rover read (Scene 7) — one drum,
distant thuds and the film's quietest exchange of spoken lines; the
score ducks fully under the voices and never touches them. One hard struck piano
note on the yoke turn (Scene 8, at 1.0 s), then the pulse doubles and
stays doubled through the chase (Scene 9) — the only fast music in
the film. A muted low hit as the wheel drops (Scene 10, at 1.5 s). At
the boundary crossing (Scene 11, at 2.0 s) the impact-thud layer PANS
AWAY and dies behind the listener while the pulse walks on alone — the
music itself crosses the line. TOTAL SILENCE for the Overview (Scene
12), only a faint distant hiss. One unresolved low note, unmetered,
for the held final frame (Scene 13), decaying under her breathing.

Mood: Patient, physical, geometric. Never frightening, never heroic.
The score treats the eruption as weather and the survival as
arithmetic.

Tempo: 72 BPM through Scenes 0-1. 96 BPM through Scenes 2-7. 144 BPM
from the decision (Scene 8, after the piano note) through the chase
and the wreck (Scenes 9-11). Silence at Scene 12. Unmetered at Scene
13. Beats land exactly on the planned cut points: 5.0 s (Scene 0),
4.0 s (Scene 2), 5.0 s (Scene 4), 6.0 s (Scene 6), 3.0 s (Scene 8),
6.0 s (Scene 10), 5.0 s (Scene 11).

Low-end rule: every sub-bass element below 90 Hz is doubled by an
octave companion between 90 and 160 Hz so the low end survives phone
speakers.

Dynamic arc: small tick and a question (0-1) — a floor opens under
everything (2) — awe held flat (3-5) — the world starts drumming out
of time (6) — one drum alone (7) — a struck note and a doubling (8) —
full dry gallop (9) — a muted failure (10) — the fall panning away
behind (11) — silence over the whole machine (12) — one unresolved
note and breath (13).

Reference feel: the dry patience of a metronome-driven heist cue
crossed with field recordings of rockfall — the tuned versus the
untuned. No lyrics, no choir, no melody louder than the pulse. One
continuous evolving piece, roughly 2 minutes 20 seconds, mapped to
the 14-scene arc above.
```

---

# 📋 BÖLÜM 4 — ÜRETİM NOTLARI

```
DURUM              ✍️ YAZILDI (05.08.2026) · ÜRETİLMEDİ
                   Plan: 140 s / 14 sahne / 21 segment / 7 kesme
                   28 prompt (14 imaj + 14 video) + müzik + 2 kapak

⛔ ÜRETİM SIRASI — bu filmde iki kapı var

   KAPI 1 — MİMARİ TESTİ: ÖNCE S0 ÜRETİLİR. Tek başına.
      S0 bir kesme ve bir referanssız B segmenti taşıyor (75mm yüz
      kadrajı). Bu tek klip, tek-kesme mimarisinin tutup tutmadığını
      söyler.
      Kabul ölçütü:
        · Kesme 5.0 saniyede mi?
        · SERT kesme mi — bindirme, fade, morph var mı?
        · Segment B'nin kadrajı yazıldığı gibi mi?
        · Kıyafet ve vizör kesmeden sonra aynı mı?
      Tutmuyorsa → §0.20 Plan B: 21 ayrı klip, kurguda kesme.
      Karar burada verilir, filmin tamamı üretildikten sonra değil.

   KAPI 2 — FİZİK TESTİ: sonra S3 (sütun makrosu) ve S1 (küçük halka).
      Filmin bütün görsel iddiası taşların TAŞ olarak çıkmasına bağlı.
      Kabul ölçütü: taşlar AYRIK ve KESKİN mi — bulut, duman, sis
      olarak mı çizilmiş · hiçbir taş asılı kalıyor mu · S1'de halka
      gerçekten HALKA mı ve merkez temiz mi · hiçbir yerde alev,
      ıslaklık, kabaran kütle var mı.
      Tutmazsa film üretilmez; 12 segmentte sütun kadrajda ve başka
      hiçbir sahne bu hatayı kurtaramaz.

   Sonra kalan 11 sahne. Onaylanmamış imajdan video üretilmez.

PROMPT UZUNLUK KONTROLÜ — üretimden önce ölçülecek
  ⚠️ 4.300 karakter Veo'da hata veriyor (KILAVUZ_REHBERI §7).
     Bu dosyanın en uzun bloğu ~3.950 karakter — eşiğin altında,
     ama kopyalarken Türkçe başlık EKLEME (blok büyür).

🆕 BU FİLMDE İLK KEZ DENENEN BEŞ ŞEY — üretimden sonra ölçülecek
  1. 🆕 SAHNE BAŞINA EN ÇOK 1 KESME. Dawn Front mimarisinin yarı dozu;
     referanssız segment sayısı sahne başına 1'e indi. Ölçülecek soru:
     kesme isabeti Dawn Front'tan iyi mi?
  2. 🆕 KAPANAN HALKA. Tehdit çizgi değil, içe kapanan bir çember —
     ve kaçış yönü ÖNCE kapanıyor. Model "dıştan içe sıralı çarpma"yı
     çizebiliyor mu?
  3. 🆕 DÜZENSİZ PERKÜSYON KATMANI (Bölüm 3). Gerçek çarpma sesleri
     partisyona senkronsuz biner.
  4. 🆕 0.11 g'DE SIÇRAMASIZ AKSİYON. Deponun en düşük yerçekimli
     koşu-kovalamaca filmi; havada süzülme kadraja hiç alınmadı.
  5. 🆕 AI ANALİZ DİYALOĞU. Kâşif sorar, kıyafet AI'ı analiz döner —
     5 replik / 3 sahne. Kadın yalnız geniş planda konuşur (dudak
     senkron riski sıfır), AI ekran dışı sestir. Ölçülecek soru:
     replikler yazıldığı saniyede, metinsiz ve tek seste mi çıkıyor?

⚠️ ÜRETİMDE İZLENECEK BEŞ AÇIK RİSK
  · Sütunun DUMANA dönmesi. Model taş akıntısını bulut olarak çizmeye
    eğilimli. "discrete stones, needle-sharp streams, never a cloud"
    her sütun promptunda yazılı.
  · Apeks asılması. "never hovering" ile yükselen sütunun çelişkisi
    §0.13 ①'de çözüldü; yine de tek taşın havada durduğu kare
    çıkarsa o klip reddedilir.
  · Klon. S2-B (biniş) ve S10-B (iniş) deponun ölçülmüş en riskli
    çekim tipleri. Negatif bloklarda "the seat stays EMPTY" vurgulu.
  · Kesmenin geçişe dönüşmesi. CUT SCHEDULE satırında beş ayrı yasak.
  · Diyalog. Üç bilinen tuzak: (a) replik ekranda METİN olarak
    belirir → "heard only, no subtitles" her diyaloglu promptta;
    (b) AI'a gövde/ikinci figür icat edilir → "no body, no avatar,
    no second figure"; (c) 5 s üstü replikte ses kesilir → tüm
    replikler ≤5 s. Türkçe yayın gerekirse hibrit yol: VEO kılavuzu
    §9 (ElevenLabs + Sync 3).

QA SIRASI          1) VIDEO_QA — SPEC bloğu §0.16'dan kopyalanır
                   2) MANTIK_QA — yalnız video
                   3) SENARYO_QA — video + bu dosyanın BÖLÜM 0'ı
SONRAKİ ADIM       KILAVUZ_REHBERI §6 adım 3.5 — prompt QA (elle)
KAPAK              ✅ BÖLÜM 5'te hazır — A sürümü + Plan B + tipografi
PAKETLEME          VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
                   Tek cümlelik öncül: "Gök taş yağdırıyor ve tek kuru
                   yer, taşları atan deliğin dibi."
```

---

# 🖼️ BÖLÜM 5 — KAPAK FOTOĞRAFI

> **Kaynak:** `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md`
> **Ev kuralı:** kapak **metinsiz** üretilir, tipografi post'ta eklenir.

## 5.1 ✅ PALET — filmden çıkıyor, uydurulmuyor

```
Filmin paleti:  soluk kemik grisi (ova ve taşlar) + koyu cam örtü +
                derin menekşe gökyüzü
Tek doygun kırılma: YANIK TURUNCU — kıyafetin turuncu dikiş hatları, araç
                    işaretleri ve alçak güneşin taş kenarlarındaki
                    sıcak kenar ışığı

→ "Derin menekşe zemin üzerine yanık turuncu" — kılavuzun "lacivert
  zemin üzerine canlı turuncu" kombinasyonunun bu filmdeki fiziksel
  olarak meşru karşılığı. 120 pikselde ayrışır.
```

## 5.2 🎯 MİKRO-HİKAYE — kapak neyi soruyor

```
ÖLÇEK       Kadrajın sol %60'ı: yükselen taş sütunu — tepesi kadraj
            dışında
ÖZNE        Alt sağ üçte birde minicik araç — SÜTUNA DOĞRU gidiyor
NESNE       Aracın ARKASINDA duran toz sütunları — kaçtığı şey
BAKIŞ       Göz önce sütuna, sonra araca, sonra yöne gider
DUYGU       "Neden patlamaya DOĞRU sürüyor?"

İZLEYİCİNİN SORUSU: "Bu taş sütunu ne — ve araç neden ona gidiyor?"
```

Kapak S9'un tek karelik hâli ve film 1:20-1:40 arasında o vaadi
ödüyor → `PROMISE VS PAYLOAD: HONEST`.

## 5.3 📸 KAPAK PROMPTU — A SÜRÜMÜ (ÖNERİLEN, metinsiz)

> Başlık için **üst-sağ** dörtte birlik alan boş bırakıldı (sütun
> solda olduğu için Dawn Front'un tersi). **Sağ alt köşe** tamamen
> boş — YouTube süre rozeti orayı kapatır.

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels,
16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE.
YouTube thumbnail optimized — maximum impact at 120 pixels wide.

SUBJECT — THE SHOCK, FILLS THE LEFT:
A colossal column of dry cold gravel rises from a dark 60-meter cinder
cone on the LEFT 60% of frame, its top going out of the top of frame:
dozens of parallel needle-sharp streams of discrete pale grey stones,
each stone 0.1 to 0.6 meters, climbing along straight ballistic lines
— visibly individual rocks, never a cloud, never smoke, never fog. A
hard warm BURNT-ORANGE rim of low sunlight edges the column's right
side and the cone's right flank. At the cone's foot spreads a smooth
DARK glassy apron with a sharp boundary line against a pale
crater-pocked plain.

THE SCALE ANCHOR — SMALL AND COMMITTED:
In the LOWER RIGHT THIRD, tiny against the column, a 3.0 meter
sleek angular four-wheel rover races LEFT — TOWARD the eruption: matte
sand-grey machine-finished faceted composite body with crisp burnt-orange markings, four
airless alloy mesh wheels each 0.8 meters across biting the gravel, a
low cockpit hoop over a single sunken cockpit seat with one small human figure in a matte
sand-grey suit with burnt-orange sealed seams and a fully transparent
visor. BEHIND the rover, to the right, three standing 4-meter columns
of dry dust mark fresh stone strikes, and one dark stone hangs
mid-fall above them, streaking down. The rover is no more than one
twelfth of the frame width. Physically accurate perspective, correct
engineering proportions — never miniature or toy-like.

LIGHTING — TWO SOURCES ONLY:
1. Hard low sunlight from the RIGHT: a warm burnt-orange edge on the
   column, the cone flank and the rover's right side.
2. Cold pale ambient off the grey plain and violet sky.
Sharp directional light with clear falloff. Deep shadow on the left
face of every stone. 0% bloom, 0% glow filter, no soft focus, no lens
flare, no halo around any light source.

BACKGROUND:
Deep violet sky. The huge dim ochre-banded disk of a gas planet sits
low behind the cone, partly cut by the column. The UPPER RIGHT
QUADRANT is kept clean, dark and uncluttered — open negative space
reserved for the title added later in post.

COLOR — TWO COLORS ONLY:
- COLD PALE GREY and deep violet: the stones, the plain, the sky
- WARM BURNT-ORANGE: the sunlit rims and the suit's sealed seams
No green, no teal, no red. Two-value contrast: cold mass against a
warm edge. Increase final saturation by 20% so the orange survives at
thumbnail scale.

COMPOSITION:
- The column and cone own the left 60%, edge to edge vertically
- The rover in the lower right third, sharply in focus, heading LEFT
- The strike columns behind it, softer
- UPPER RIGHT QUADRANT clean negative space
- LOWER-RIGHT CORNER completely empty — no detail of any kind

TECHNICAL:
- No text, no letters, no numbers, no digits, no logo, no watermark,
  no subtitles, no name label, no HUD
- Exactly one human being — no second person, no crew, no figure on
  the plain, no reflection of another person
- Photorealistic, 35mm film grain
- Sharp focus on the rover and the column's nearest streams — the two
  sharpest things in the image
- The column is discrete flying stones — NOT smoke, NOT fog, NOT a
  dust storm, NOT a cloud bank, NOT a water spout
- Nothing is on fire: no flame, no ember, no ash, no smoke — the
  eruption is cold dry gravel
- No liquid, no wet surface, no melting
- No Unreal Engine look, no CGI aesthetic, no video game aesthetic
```

## 5.4 📸 KAPAK PROMPTU — B SÜRÜMÜ (PLAN B, 48 saat kuralı)

> Kılavuz §7: yayından **48 saat** sonra CTR %4'ün altındaysa devreye
> girer. A sürümü ölçek odaklı; B sürümü **soru odaklı** — S12
> Overview'un kapak hâli: "merkez neden temiz?"

```
Photorealistic cinematic film cover image, EXACTLY 1280x720 pixels,
16:9 landscape. NO TEXT ANYWHERE IN THE IMAGE.
YouTube thumbnail optimized — maximum impact at 120 pixels wide.

SUBJECT — THE QUESTION, SEEN FROM ABOVE:
A high wide view down onto a pale gravel plain: at center-left, a dark
60-meter cinder cone fires a column of needle-sharp streams of
discrete stones straight up and out of the top of frame. Around the
cone's foot lies a smooth DARK glassy disk reaching 500 meters out —
perfectly CLEAN, lit by a shaft of clear hard low sun, not one mark
inside it. Around that disk, a churning grey RING of dozens of
standing 4-meter dust columns where stones strike the plain — a
complete annulus of chaos wrapped around a circle of calm. Beyond the
ring, pale untouched plain to the horizon.

THE SCALE ANCHOR:
Inside the clean dark disk, tiny and alone, ONE standing human figure
in a matte sand-grey suit with burnt-orange sealed seams, no more than
one twentieth of the frame height, its long shadow running left. Near
the disk's sharp boundary line, just outside it, the tiny tilted
wreck of a small angular-bodied rover. Exactly one human being in the
image.

LIGHTING:
Hard low sunlight from the RIGHT. The clean disk is the brightest
ground in frame — a well of clear light — while the ring around it
lies under its own cold grey veil of hanging dust. Warm burnt-orange
edge along the column and cone. 0% bloom, no glow filter, no soft
focus, no lens flare, no halo.

BACKGROUND:
Deep violet sky across the top; the huge dim ochre-banded gas planet
low in the UPPER LEFT. The UPPER RIGHT QUADRANT kept clean and dark —
negative space reserved for the title added later in post.

COLOR — TWO COLORS ONLY:
- COLD PALE GREY and deep violet: plain, dust ring, sky
- WARM BURNT-ORANGE: the column's sunlit rim and the planet's dim bands
Increase final saturation by 20% so the orange survives at thumbnail
scale.

COMPOSITION:
- The ring-and-disk geometry reads as one bold graphic shape at
  thumbnail size: grey ring, dark clean circle, bright center-left cone
- The figure inside the disk, sharply in focus
- UPPER RIGHT QUADRANT clean negative space
- LOWER-RIGHT CORNER completely empty of detail

TECHNICAL:
- No text, no letters, no numbers, no logo, no watermark, no HUD
- Exactly one human being — no second person, no crew
- Photorealistic, 35mm film grain
- The ring is made of discrete standing dust columns from stone
  strikes — NOT smoke rings, NOT fog, NOT a crop circle, NOT water
- The eruption column is discrete flying stones — NOT smoke, NOT a
  cloud bank
- Nothing is on fire: no flame, no ember, no ash, no smoke
- No liquid, no wet surface — the dark disk is dry glassy ash, not
  water, not a lake
- No Unreal Engine look, no CGI aesthetic, no video game aesthetic
```

## 5.5 ✍️ TİPOGRAFİ — post'ta eklenir, prompt'a ASLA girmez

```
KONUM        üst-sağ dörtte birlik alan (her iki sürümde boş bırakıldı)
BAŞLIK       THE STONE SKY      — ağır grotesk, tümü büyük harf
ALT SATIR    "Tek kuru yer, taşları atan deliğin dibi."  — ince, %60 opaklık
RENK         kemik beyazı; turuncu ASLA kullanılmaz (tek doygun renk
             görüntüde zaten var, ikincisi onu öldürür)
ÖLÇÜ TESTİ   120 piksel genişliğe küçült — başlık hâlâ okunuyor mu
YASAK        kapak promptunun içine tek harf bile yazılmaz
```

## 5.6 ✅ ÜRETİM ÖNCESİ KAPAK KONTROLÜ

```
□ Görüntüde tek bir harf, rakam veya sembol var mı?        → varsa yeniden üret
□ Tek insan mı? İkinci figür veya yansıma var mı?          → varsa yeniden üret
□ Sütun DUMAN/BULUT gibi mi görünüyor?                     → öyleyse yeniden üret
□ Halka (B sürümü) su/sis halkası gibi mi okunuyor?        → öyleyse yeniden üret
□ Herhangi bir yerde alev, kıvılcım, ıslaklık var mı?      → varsa yeniden üret
□ Turuncu kenar sert mi, yoksa hale mi yapmış?             → hale varsa yeniden üret
□ Üst-sağ çeyrek başlık için boş mu?                       → değilse yeniden üret
□ Sağ alt köşe boş mu (süre rozeti)?                       → değilse yeniden üret
□ 120 piksele küçülttüğünde araç/figür hâlâ seçiliyor mu?
□ Kapağın vaadi filmde ödeniyor mu? (A → S9 · B → S12)     → PROMISE VS PAYLOAD
```

---

# THE STONE SKY

### _"Gök taş yağdırıyor. Ve o kadın, taşları atan deliğe doğru sürüyor."_
