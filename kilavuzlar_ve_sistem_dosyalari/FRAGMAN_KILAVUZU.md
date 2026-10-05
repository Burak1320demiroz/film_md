# 🎞️ FRAGMAN KILAVUZU — İki Formatlı Teaser Üretimi

> **Bu kılavuz ne zaman okunur:** Bitmiş (tercihen QA'dan geçmiş) bir filmin
> fragmanı yazılacağı zaman. Fragman YENİ BİR FİLM DEĞİLDİR; kendi konsepti,
> kendi novum'u, kendi hikayesi olmaz. Tek işi kaynak filmin vaadini kurmak
> ve **cevabı vermeden bırakmaktır.**
>
> **Depodaki emsaller:**
> `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN.md` (çift format · 6 + 9 vuruş)
> `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_PRO_YATAY.md`
> (yatay trailer · 2:00 · 27 kesme · kırpma tabanlı · logo blokları → §1.1b)
> `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_DIKEY_2.md`
> (aynı filmin **İKİNCİ** dikey teaser'ı · 6 vuruş · farklı mekanik →
> §1.3b: bir filme ikinci fragman ne zaman yazılır)
> `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_DIKEY_3.md`
> (aynı filmin **ÜÇÜNCÜ** dikey teaser'ı · 6 vuruş · mekanik KUSUR YOK ·
> ⚠️ üretim BEKLİYOR, prompt kontrol GO → §1.3b'nin üçüncü teslim notu)
> `yatay_4_dk_filmler/THE_COLD_BURN/THE_COLD_BURN_FRAGMAN_DIKEY.md`
> (dikey · 6 vuruş · mekanik KAPANAN KAPILAR · **kadraj kesişimi**
> denetimini ekledi → §1.3c)
> `yatay_4_dk_filmler/THE_BLACK_CRADLE/THE_BLACK_CRADLE_FRAGMAN.md`
> (dikey · 6 vuruş · mekanik TERS KURALLAR)
> `yatay_4_dk_filmler/THE_BORROWED_WEIGHT/THE_BORROWED_WEIGHT_FRAGMAN_DIKEY.md`
> (dikey · 6 vuruş · mekanik TERAZİ · kaynak filmin I2V hattını fragmana
> taşıyan ilk teslim · ⚠️ üretim BEKLİYOR, prompt kontrol GO)
> `yatay_10_20_dk_filmler/YERCEKIMI/YERCEKIMI_FRAGMAN_YATAY.md`
> (yatay trailer · 2:00 · **14 vuruş sıfırdan üretim, 8 s klip** · mekanik
> EKSİLME · logo blokları + replikler POST'ta [F6 gömülü altyazı vakası] ·
> ⚠️ üretim BEKLİYOR, prompt kontrol GO)
> `yatay_16_dk_filmler/THE_LAST_GATE/FRAGMAN/` (yatay · **1:00** · 12 vuruş ·
> aynı oranlı → §1.1b · yeni üretim 0 kare, risk 0/9 · mekanik DARALMA ·
> ⭐ **ilk KLASÖR biçimli teslim** (üç dosya: eşleme · kare hassasiyetli kesim
> listesi · müzik+vurgu) ve ⭐ **ilk 1:00 yatay** — §0 bandının (1:20-2:00)
> ALTINDA, sapma dosyada sayısal karşılığıyla kayıtlı · ⚠️ kaynak film 0 kare
> üretildi, teslim KURGU TALİMATI)
> Altısını da şablon olarak aç; bu kılavuz oradaki kararları genelleştirir.

---

# 0. İKİ FORMAT — tek bakışta

| | 📱 SHORTS FRAGMAN | 🖥️ YATAY FRAGMAN |
|---|---|---|
| Oran | 9:16 DİKEY | 16:9 YATAY |
| Sahne | **3-6 vuruş** | **8-12 vuruş** |
| Klip süresi | 8 s (dikey shorts standardı) | 10 s (yatay standart; Veo'da 8+2 extend) |
| Toplam | 24-48 s | 1:20-2:00 (kurgu kırpmasıyla kısalabilir) |
| Tür | **TEASER** — tek mekanik, tek tırmanış | **TRAILER** — 3+1 perde (cold open dahil) |
| Replik | **0 replik** (varsayılan) | ≤ 2 replik, tercihen gövdesiz AI |
| Loop | ZORUNLU (son kare → ilk kare dikişi) | opsiyonel |
| Dosya | **kaynak film klasörlüyse İÇİNE** (`<FILM>/…_FRAGMAN_DIKEY.md` · ikincisi `…_FRAGMAN_DIKEY_2.md`, üçüncüsü `…_FRAGMAN_DIKEY_3.md`, §1.3b) · kaynak film tek dosyaysa `dikey_shorts_filmler/<FILM>_FRAGMAN_DIKEY_SHORTS.md` | film klasörlüyse `<FILM>/FRAGMAN.md` · tek dosyaysa yanına `<FILM>_FRAGMAN_YATAY.md` |
| Sayımdaki yeri | klasör içi dosya film sayımına GİRMEZ (17.08.2026 · Second Ship · Black Cradle · Cold Burn emsali) · yalnız dikey klasörde duran dosya ayrı film satırı sayılır | klasör içi dosya — film sayımına GİRMEZ |
| QA merceği | SHORTS_QA | VIDEO_QA (kurgu) — SENARYO_QA fragmana koşulmaz |

Dış dünya karşılığı: teaser 15-90 saniye ve ton satar; trailer 1-3 dakika ve
hikaye kurar. İki bandımız da bu aralıkların içinde — bilinçli.

---

# 1. ⛔ HER İKİ FORMATIN DEĞİŞMEZ KURALLARI

## 1.1 KIRPMA YOK, YENİDEN ÇEKİM VAR

```
Fragman, masterdan KIRPILARAK üretilmez. Her vuruş hedef oranda SIFIRDAN
üretilir.

Sebep sayısal (Cold Burn'ün dikey fragman çalışmasında ölçüldü): 16:9 masterda duvar kadrajın
sol yarısındadır; 9:16'ya kırpınca ya duvar ya figürler kadraj dışında kalır.
Kırpılmış kare güvenli alan denetimini (SHORTS_QA §B) geçemez.
Ters yönde de aynıdır: dikey üretilmiş kareyi 16:9'a çevirmek üst/alt keser.

Dikeyin kazancı: kule, duvar, gemi gibi DİKEY nesneler izleyicinin üstüne
gelir. Yatayın kazancı: yan yana duran iki varlık, ölçek karşılaştırması ve
ufuk çizgisi ancak yatayda okunur. Vuruş seçimini bu belirler — aynı vuruş
listesi iki formatta birebir aynı OLMAZ.
```

## 1.1b ⭐ İSTİSNA: AYNI ORANLI FRAGMAN — kırpma değil, KIRPMA

> 13.08.2026'da açıldı. §1.1'in kapatmadığı bir boşluk vardı ve ilk
> gerçek yatay trailer denemesi onu buldu:
> `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FRAGMAN_PRO_YATAY.md`

```
§1.1'in yasağı ORAN DEĞİŞİMİ içindir. Ölçülen bedel kadraj kaybıdır:
16:9 → 9:16 çevirince kadrajın yarısı gider, güvenli alan denetimi
düşer. Bu bedel ORAN AYNIYSA OLUŞMAZ.

16:9 bir filmin 16:9 fragmanı için kural şudur:
  ✅ Kadraj kırpılmaz — bir piksel bile.
  ✅ ZAMAN kırpılır: masterda üretilmiş 10 s'lik klipten kurguya
     1,5-8 s'lik bir dilim alınır. §3.2 bunu zaten serbest bırakıyor.
  ✅ Bir klipten İKİ ayrı dilim iki ayrı yere alınabilir.
  ⛔ Klibin İÇİNE kesme atılmaz · hız rampası yok · ağır çekim yok.

BUNUN ÜÇ SONUCU VAR, üçü de §0 tablosunu bu satırda esnetir:
  ① VURUŞ SAYISI BANDI (8-12) GEÇERSİZDİR. O bant "her klip ~10 s tam
     kullanılır" varsayımına dayanır ve bir ÜRETİM BÜTÇESİ sınırıdır.
     Kırpma tabanlı kesimde klip başına düşen süre 2-4 s'ye iner;
     100 saniyelik bir gövde 25-30 kesme ister. Second Ship: 27.
  ② YENİ ÜRETİM SIFIRA İNER. Aynı oranlı fragmanın maliyeti kurgu
     işidir, üretim işi değil. Risk sayımı da sıfırdır.
  ③ IN/OUT NOKTALARI TAHMİN EDİLMEZ, OKUNUR. Faz dosyalarındaki video
     promptları saniye işaretleri taşır (`0s`, `3s`, `5s` …). Her IN ve
     OUT o işaretlerden seçilir; seçilmezse kesme klibin ölü yerine
     düşer.

⚠️ 9:16 teslim hâlâ §1.1'e tabidir: dikey fragman sıfırdan üretilir.
   Bu istisna YALNIZ oran aynıyken açılır.
```

## 1.2 SPOILER KAPISI — fragman bütçesinin dışı

Fragman dosyasının başına **"fragmanda ASLA olmayacak kareler"** listesi
yazılır (Second Ship'te 7 kalem). Değişmez kalemler:

```
⛔ DORUK sahnesi ve çözümü        ⛔ FİNAL ve kapanış imajı
⛔ CENTRAL CHOICE'un SONUCU       ⛔ filmin omurga sırrı / reveal'i
⛔ karakterin kaderi              ⛔ novum'un AÇIKLAMASI (görüntüsü girebilir,
                                     mekanizması giremez)
```

Kural: **vuruşlar filmin ilk %70'inden seçilir** — dış dünyadaki karşılığı
"perde 1 + perde 2A malzemesi, üçüncü perde asla." Cold Burn fragmanı bunu
birebir uyguladı: doruk S26 ve final S29 dışarıda, yangının adı başlıkta
ama karesi fragmanda yok.

### ⛔ SPOILER KAPISI PLANDA DEĞİL, KURGUDA KOŞULUR [17.08.2026]

Bu liste bugüne kadar yalnız fragman DOSYASININ başında yaşadı; teslim
edilen kurguda kimse tekrar bakmadı. Kurgu kapısına iki satır girer ve
ikisi de tek soruyla ölçülür:

```
□ SPOILER LİSTESİ · her kalem kurguda 0 KARE (madde madde işaretlenir)
□ TEK CÜMLE TESTİ: kurguyu ilk kez izleyen biri filmi tek cümleyle
     anlatsın. Cümle TAMAMLANMIŞ bir hikaye anlatıyorsa fragman
     ÇÖKMÜŞTÜR — teslim edilmez. Cümlede cevaplanmamış bir soru
     kalmalıdır; fragmanın ürünü o sorudur.
□ İMZA TESTİ: fragmanın sattığı TEK görüntü (afiş vuruşu) kurguda var mı
     ve TERSİNE ÇEVRİLMEMİŞ mi? İmza, filmin varsayılanı bozan karedir;
     model varsayılana geri döner (kıç önde yanaşma → burun önde çıktı).
□ 🆕 PAKETLEME TESTİ [DERS 114]: aynı üç test BAŞLIK ve AÇIKLAMAYA da
     koşulur. İzleyici oynat tuşuna basmadan önce metni okur; sıra
     BAŞLIK → AÇIKLAMA → KURGU'dur. Açıklamada olay dizisi ("X olur,
     sonra Y") fragmanın tek ürününü siler; teaser "short film" diye
     satılmaz. Ayrıntı: `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` TEASER modu.
```

⚠️ Kaynağı: Black Cradle fragman koşusu — ölçen mercek kurguyu "iki kişi
kutuyu alır, kalkar, istasyona kenetlenir" diye özetledi ve bunu AKTARIM
BAŞARISI sayıp 7 puan verdi. Teaser'ın işi tam tersiydi.
→ `LESSONS_LEARNED.md` DERS 106.

## 1.3 TEK MEKANİK KURALI

Her fragmanın TEK bir mekaniği olur ve bütün vuruşlar ona hizmet eder:

```
Second Ship  → SAYIM        seyirciye saymayı öğret, son vuruşta sayımı boz
Second Ship 2→ CEVAP        her vuruşta bir şey gönderilir, bir şey karşılık verir
Second Ship 3→ KUSUR YOK    her vuruşta hatasız yapılmış bir iş; kırılma tek EKSİKTE
Cold Burn    → KAPANAN KAPILAR  her vuruş bir kaçış yolunu siler (YOKLUK ailesi)
Black Cradle → TERS KURALLAR    her vuruş bir beklentiyi çevirir
Low Power    → ÖRTÜLME      her vuruşta toz bir şeyin daha üstünü kapatır
Borrowed W.  → TERAZİ       her vuruş kefe değiştirir: dünya hafifler,
                            adam ağırlaşır; iki serinin bağı hiç kurulmaz
YERÇEKİMİ    → EKSİLME      her vuruş bir şeyi eksiltir (cıvata → rutin →
                            platform → halat → cevap → yakıt → ışık →
                            ritim); butonda kalan tek şey camdaki gezegen
LAST GATE    → DARALMA      her vuruşta bir SAYI küçülür ve izleyici onu
                            kendi öğrenir (16.000 → 9.000 → 1.200 → 900 m);
                            ölçüt vuruşu (480 m gemi kesiti) sondan bir önce
                            konur, button iki sayıyı çarpıştırıp CEVAPSIZ keser.
                            ⭐ TAKVİM'in TERSİ: sayaç ilerlemez, GERİ SAYAR.
diğer adaylar→ ÖLÇEK (merdiven yukarı) · TAKVİM (sayaç ilerler)
              · YAKLAŞMA (tehdit her vuruşta yakında)

⚠️ Bu liste bir SİCİLDİR: aynı filme ikinci/üçüncü fragman yazan ajan
   buradan hangi mekaniğin tutulduğunu okur (§1.3b ①).
```

Mekanik "filmi özetlemek" değildir. Fragman filmi YENİDEN ANLATMAZ —
depodaki eski dikey türevlerin (Slow Tide, Slow Stone) ölçülmüş hatası
buydu: 6 sahnede filmin tamamını sıkıştırıyorlardı.

## 1.3b ⭐ AYNI FİLME İKİNCİ FRAGMAN — üç koşul, üçü birden

> 16.08.2026'da açıldı. Second Ship'in ikinci dikey teaser'ı
> (`FRAGMAN_DIKEY_2.md`) bu boşluğu buldu: §0 tablosu film başına TEK
> dikey fragman varsayıyordu ve varsayımın yazılı bir gerekçesi yoktu.

```
Bir filme ikinci fragman ancak ÜÇÜ BİRDEN sağlanırsa yazılır:

  ① MEKANİK FARKLI       §1.3'teki listeden BAŞKA bir mekanik.
                         Aynı mekaniğin ikinci çekimi varyanttır,
                         ikinci fragman değil.
  ② SAHNE KESİŞİMİ SIFIR Vuruş/kaynak eşleme tabloları yan yana
                         konur; ortak kaynak sahne sayısı 0 olmalı.
                         Second Ship: 6 + 6 vuruş, kesişim 0.
  ③ SORU FARKLI          İki fragmanın seyircide bıraktığı soru aynı
                         cümle olamaz. Aynıysa ikincisi para harcar,
                         yeni izleyici getirmez.

İKİNCİ FRAGMANIN BEDAVA GELEN ÜÇ KALEMİ (ölçüldü):
  · çapa blokları — kaynak filmde bir kez ödendi, üç teslim paylaşır
  · müzik — vuruş ızgarası aynıysa (n × 10 s, aynı BPM) mevcut master
    yeniden kullanılır; beste bütçesi ikinci kez açılmaz
    ⚠️ IZGARA YETMEZ, SPOTTING DE TUTMALI (17.08.2026'da ölçüldü):
    ızgara aynı olabilir (6 × 8 s) ama cue'nun tek yapısal olayı —
    örneğin atmosfer kaybı — birinde 16,0'da, ötekinde 8,0'da düşer.
    O zaman cue yeniden bestelenir.
    Kontrol: iki fragmanın rejim/ton değiştirdiği SANİYELER aynı mı?
  · spoiler kapısı ve negatif çekirdek — bir kez yazılır, kopyalanır

⭐ ÜÇÜNCÜ TESLİM DE AYNI KAPIDAN GEÇER — İKİ KEZ (20.08.2026):
   Second Ship'in üçüncü dikey teaser'ı (`FRAGMAN_DIKEY_3.md`) yazıldı
   ve üç koşul TEK kardeşe değil, İKİ kardeşe karşı ayrı ayrı koşuldu:
     · mekanik: SAYIM · CEVAP · KUSUR YOK — üçü de ayrı
     · sahne kesişimi: 6+6+6 vuruş, iki kesişim de 0
       (S1·S11+S12·S21·S28·S35·S40 | S10·S25·S29·S47·S50·S39 |
        S13·S14·S32·S37·S49·S51)
     · soru: üçü de farklı cümle
   ⭐ VE BİR ADIM DAHA: üçüncü teslim, kardeşlerinin AFİŞ ve MEKANİK
     karelerini kendi SPOİLER LİSTESİNE yazdı (ikinci geminin tam
     gövdesi · zeminin kabarması = 0 kare). Kesişimi sıfır tutmak
     yetmiyor; teslimler birbirinin sattığı görüntüyü de satmamalı,
     yoksa üçü aynı izleyiciyi paylaşır.
   ⚠️ n'inci teslim için kural değişmiyor: koşullar her kardeşe karşı
     AYRI koşulur, tek bir "önceki dosya" karşılaştırması yetmez.

⚠️ RİSK PROFİLİ BİLEREK FARKLI SEÇİLİR. Second Ship'in birinci dikey
   fragmanının 1 numaralı riski Bekçi'nin TAM BOY DÖNÜŞÜYDÜ (Ders 2);
   ikincisi o çekimi hiç istemez — riski üç parmaklı ELE indirir.
   İki teslim aynı riski iki kez satın almaz.
```

## 1.3c ⭐ SAHNE KESİŞİMİ SIFIR ≠ KADRAJ KESİŞİMİ SIFIR

> 17.08.2026'da açıldı. Cold Burn'ün dikey fragmanı §1.3b ②'yi geçmişti
> (kesişim 0), ama denetim sırasında iki vuruşun **kompozisyon olarak**
> kardeş teslimle çakıştığı görüldü. §1.3b ② sahne NUMARASINI sayar;
> izleyici ve model kadrajı görür, numarayı değil.

```
İki fragman aynı filmin aynı varlıklarını kullanmak ZORUNDADIR. Bu
yüzden ② geçildikten SONRA ikinci bir denetim yapılır:

  İki vuruş tablosuna LENS + MESAFE + ÖZNE sütunları konur ve yan yana
  okunur. Aynı özneyi benzer lens ve mesafede gösteren iki vuruş varsa
  KADRAJ ÇAKIŞMASI vardır; ikinci teslim o vuruşu yeniden kadrajlar.

Cold Burn'de iki çakışma çıktı, ikisi de yeniden kadrajlanarak çözüldü
(kararlar `THE_COLD_BURN_FRAGMAN_DIKEY.md`'nin başında durur):
  · prob/koni ikilisi → makro TEMAS (75mm / 3 m) yerine geniş IŞKA
                        (32mm / 40 m) — ters ölçek, ters sonuç
  · ana gemi        → burun tarafından KULE yerine gövdeye monteli
                        kameradan ÇAPRAZ, arkasında dönen yıldız alanı

⚠️ Yeniden kadrajlama kaynak sahnenin lensini değiştirmek demektir ve
   bu bir SAPMADIR: fragman dosyasına "kaynak lens → yeni lens +
   gerekçe" satırı yazılır (Camera Bible'ın altına). Kayıtsız lens
   değişimi sonraki denetimde devamlılık hatası gibi okunur.
```

## 1.4 ÇAPA BLOKLARI KAYNAK FİLMDEN BİREBİR

Karakter/gemi/dünya tanımları kaynak filmin kanonik bloklarından **tek kelime
değiştirilmeden** kopyalanır (`SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1). Fragmanın
en büyük maliyet avantajı budur: çapa bedeli kaynak filmde zaten ödendi.
Negatif çekirdek de aynen taşınır — fragman olması hiçbir yasağı gevşetmez.

## 1.5 SIFIR KESME + LOCKOFF VARSAYILANI

```
· Her vuruş AYRI klip olarak üretilir; kesme klip ARALARINDA yaşar,
  promptun içinde değil [Ders 68]. "cut to", "then we see", "montage" yasak.
· Kamera varsayılanı TAM LOCKOFF — fragmanın ritmi kurgudan ve müzikten
  gelir, kamera hareketinden değil [Ders 1 · iki emsal de 6/6 lockoff].
· Yatay fragmanda kurgu KIRPMASI serbesttir: 10 s üretilen klip kurguda
  baştan/sondan kırpılıp 5-8 s kullanılabilir (klipin İÇİNE kesme atmak
  değildir). Ritim hızlanması bununla yapılır — bkz. §3.2.
```

## 1.6 REPLİK BÜTÇESİ

Dikey fragmanda **0 replik** varsayılandır — kaynak filmin ölçülmüş en pahalı
hatası diyalog zincirinden çıktı [DERS 82] ve repliksiz fragmanda o hata
sınıfının yaşayacağı yüzey yoktur. Yatay fragmanda en fazla 2 replik; ikisi de
tercihen gövdesiz AI/telsiz (dudak riski sıfır) ve İKİSİ DE spoiler kapısından
geçer (doruğu anlatan cümle repliğe de giremez).

## 1.7 DÜRÜST KAYIT

Fragman dosyasının başına, emsallerdeki gibi:
```
□ BİLİNÇLİ SAPMALAR listesi (format DNA'sından her sapma + sayısal karşılığı)
□ RİSK SAYIMI (x/9 — URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md)
□ kaynak filmin ölçüm durumu (kaç mercek, hangi skorlar)
```

---

# 2. 📱 SHORTS FRAGMAN KARTI — 9:16 · 3-6 vuruş

```
YAPI:      3-6 vuruş × 8 s = 24-48 s · tek tırmanış, perde YOK
DOSYA:     dikey_shorts_filmler/<FILM>_FRAGMAN_DIKEY_SHORTS.md
GÜVENLİ    hiçbir figür/reveal y=1436 altına ve sağ 242 px şeridine girmez
ALAN:      (SHORTS_SISTEM_PROMPTU.md güvenli alan haritası)
HOOK:      ilk 3 saniye — dış araştırmanın "ilk 5-7 saniyede güçlü an"
           kuralının dikey hattaki sertleşmiş hâli. S0 HOOK_VE_ILK_SAHNE
           kılavuzuna tabidir.
LOOP:      ZORUNLU. Son karenin kompozisyonu ilk kareye diker
           (SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md §5) — fragman loop'tan
           iki kat kazanır: tekrar izleme = tutundurma = kaynak filme trafik.
MÜZİK:     tek cue, tek tırmanış; kesme noktaları vuruşa oturur
           (GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md)
METİN:     ekran metni 0.0 sn — jenerik/başlık kartı DAHİL [D70 zinciri ×5].
           Film adı platform başlığında yaşar, karede değil.
```

## 2.1 Vuruş şablonları

```
3 VURUŞ (minimum — mekanik çok güçlüyse):
  V1 HOOK      dünyanın en garip karesi, bağlamsız
  V2 AFİŞ      filmin "para karesi" — en pahalı, en paylaşılabilir görüntü
  V3 SORU      cevapsız kırılma; loop dikişi buradan S0'a döner

4-5 VURUŞ (varsayılan):
  V1 HOOK → V2 KURULUM (dünya/karakter tek karede) → V3 TIRMANIŞ
  → V4 AFİŞ → V5 SORU

6 VURUŞ (kaynak film çok varlıklıysa — Cold Burn / Second Ship bandı):
  V1 HOOK → V2 KURULUM → V3 TIRMANIŞ → V4 KIRILMA
  → V5 AFİŞ → V6 SORU
```

Seçim kuralı: **vuruş sayısını mekanik belirler, süre hedefi değil.**
Mekaniğin her basamağı bir vuruştur; basamak yoksa vuruş da yok. Dolgu
vuruşu ("bir manzara daha") fragmanı teaser'dan özete çevirir — yasak.

## 2.2 Üretim sırası

```
1. SPOILER KAPISI listesi yazılır (kaynak filmin planından)
2. AFİŞ vuruşu İLK üretilir — en pahalı kare kapıdır: o çıkmıyorsa
   fragman yoktur, kalan vuruşlara para harcanmaz
3. HOOK ikinci; kalan vuruşlar sonra
4. Kurgu → kurgu kapısı: klip sayısı = plan · süre ±2 s · ekran metni
   0.0 sn · loop dikişi üst üste bindirilerek kontrol edilir
5. QA: SHORTS_QA (MOD D — SPEC bloğu dosyanın içine yazılır)
6. Paketleme: VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md · kapak 120 px elle test
```

---

## 2.3 ⭐ HUNİ PARAMETRELERİ — dikey fragman kaç tane, hangi kadansta

> **Eklendi 27.08.2026 (araştırma 4).** Bu parametreler **yalnız FRAGMAN
> hattına aittir.** Bağımsız dikey film hattına uygulanmaz — o hat
> `DIKEY_MIKRO_DRAMA_KILAVUZU.md` §6'ya göre BAĞIMSIZ olmak zorundadır ve
> araştırmanın huni önerisi orada bilinçli olarak reddedilmiştir. İki hat
> karışırsa depo yarım bırakılmış dikey filmler üretmeye başlar.

```
DÖNÜŞÜM BANDI (dikey → yatay uzun form)
  %0,5 - 5      ← 27.08.2026'da %0,1-0,5'ten revize edildi
  ⚠️ Üst uç tek bir üreticinin paylaştığı kanal verisidir (200 izlenmelik
     Shorts'tan uzun forma 10 tıklama). Zayıf kaynak. Alt uç bile bir
     dağıtım stratejisi kurmaya yeter, üst uca güvenilmez.

70/20/10 İÇERİK DAĞILIMI — dikey üretimin bileşimi
  %70   uzun bir filme bağlı FRAGMAN (bu kılavuz)
  %20   bağımsız dikey film (DIKEY_MIKRO_DRAMA — kendi kuralları)
  %10   süreç / kamera arkası / fizik defteri anlatımı
        ⭐ Bu %10 depoda hazır malzemedir ve AI algısına karşı da
           çalışır [DIKEY_MIKRO_DRAMA §6.1 ①]: elle türetilmiş
           sayıların gösterilmesi insan yazarlığının belgesidir.

YAYIN KADANSI
  Uzun form : dikey  =  1 : 2  ya da  1 : 3
  → hibrit kanalların tek hatlı kanallara göre ~%41 daha hızlı büyüdüğü
    ölçüldü; sadece dikey ya da sadece yatay üreten kanal geride kalıyor

SABİTLENMİŞ YORUM
  Fragmanın altına uzun form linki SABİTLENİR → toplam izlenme süresinde
  ~%20 artış. Bu, deponun kullanmadığı en ucuz tek kaldıraçtır.
  ⛔ Link YORUMDA durur, KAREDE değil — metin yasağı [D61/70] kareyi
     kapsar, yorum alanını değil.
```

```
⚠️ YANLIŞ KİTLE TUZAĞI — ölçülmüş ve deponun düşme ihtimali yüksek
  Uzun formda ağır bir konu anlatan kanalın dikey tarafta algoritma
  sevsin diye alakasız içerik üretmesi, geçişi SIFIRLAR: gelen kitle
  uzun forma hiç tıklamaz, tıklarsa ilk saniyelerde çıkar ve kanalın
  ortalama izlenme süresini AŞAĞI çeker.
  → Dikey ve yatay hat AYNI evrenden beslenmek zorundadır
    (SERI_VE_KANAL_STRATEJI §2 evren çatısı).
```

---

# 3. 🖥️ YATAY FRAGMAN KARTI — 16:9 · 8-12 vuruş

```
YAPI:      8-12 vuruş × 10 s üretim · kurguda 1:20-2:00
           3+1 perde: COLD OPEN + kurulum + komplikasyon + tırmanış
DOSYA:     film klasörlüyse <FILM>/FRAGMAN.md
           tek dosyaysa <FILM>_FRAGMAN_YATAY.md (filmin yanına)
MÜZİK:     kesmeler müzik vuruşuna oturur; cue fragmanla aynı 3 perdeyi
           izler (kurulum → build → tam enerji) ve son vuruştan önce
           SUSAR — button karesi sessiz kalır
REPLİK:    ≤ 2 · gövdesiz AI tercih · spoiler kapısından geçer
METİN:     ekran metni 0.0 sn — başlık kartı kurguya GİRMEZ [D70/72].
           İstisna yok; beş filmde üst üste yandı.
```

## 3.1 Perde yapısı — vuruş eşlemesi

```
PERDE 0 — COLD OPEN         V1        bağlamsız en güçlü kare; dış
   (%0-10)                            araştırmadaki "4. perde": fragman
                                      güçlü açılır, sonra sakinleşir
PERDE 1 — DÜNYA + KARAKTER  V2-V4     kim, nerede, ne yapabiliyor;
   (%10-35)                           kaynak filmin %0-25 bandından
PERDE 2 — KOMPLİKASYON      V5-V8     engel üstüne engel; kaynak filmin
   (%35-70)                           %25-60 bandından; her vuruş bahsi
                                      yükseltir
PERDE 3 — TIRMANIŞ          V9-V11    hız artar (kurgu kırpması 10→6-8 s),
   (%70-95)                           kesme ritmi müzikle sıklaşır;
                                      DORUĞA KADAR ÇIKAR, DORUĞA GİRMEZ
BUTTON — SORU KARESİ        V12 (son) müzik susar; tek kare, cevapsız;
   (%95-100)                          fragmanın akılda kalan son görüntüsü
```

```
8 VURUŞ  → V1 + V2-V3 + V4-V6 + V7 + V8(button)     kompakt trailer
10 VURUŞ → V1 + V2-V4 + V5-V7 + V8-V9 + V10          varsayılan
12 VURUŞ → tam şablon (yukarıdaki)                    çok varlıklı filmler
```

Vuruşların kaynak eşlemesi tablo olarak yazılır (Second Ship formatı):
`| # | Vuruş | Süre | Kadro | Kaynak sahne | Lens | Hareket |` — her vuruş
kaynak filmin HANGİ sahnesinden geldiğini gösterir; kaynağı olmayan vuruş
yeni içeriktir ve fragmanda yeni içerik yazılmaz.

## 3.2 Ritim — kesme hızlanması

Dış araştırmanın en net bulgusu: fragman kurgusu VURUŞ GÜDÜMLÜDÜR — her
geçiş bir müzik vuruşuna oturur ve ritim perde ilerledikçe hızlanır.
Bu depoda bunun tek meşru aracı **kurgu kırpmasıdır**:

```
PERDE 0-1   10 s klipler tam kullanılır       sakin, geniş nefes
PERDE 2     8-10 s                            tempo hissedilir
PERDE 3     6-8 s (baştan/sondan kırp)        sıklaşan kesme
BUTTON      tek klip, tam 10 s, müzik yok     sert fren — kontrast
```

Klipin içine kesme atılmaz; kırpma klip sınırlarında yapılır. Sahne İÇİ
hız rampası, whip pan, shake — hepsi yasak kalır (negatif çekirdek).

## 3.3 Üretim sırası

```
1. SPOILER KAPISI + vuruş/kaynak eşleme tablosu
2. BUTTON ve COLD OPEN klipleri önce (fragmanın iki ucu — ikisi de
   çıkmıyorsa yapı kurulamaz), sonra PERDE 3, sonra kalanlar
3. Kurgu: müzik önce yerleşir, kesmeler vuruşa oturtulur
4. Kurgu kapısı: ekran metni 0.0 sn · button sessiz · süre bandda mı
5. QA: VIDEO_QA kurguya MOD D ile (SPEC bloğu fragman dosyasına yazılır)
6. Paketleme: VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md
```

---

# 4. İKİ FORMAT BİRLİKTE ÜRETİLİYORSA (Second Ship modeli)

```
· TEK dosya, iki bölüm: BÖLÜM 1 dikey (ana teslim) · BÖLÜM 2 yatay (varyant)
· Mekanik iki formatta AYNIDIR; yatay varyant mekaniği yalnız YATAYDA
  okunan ara basamaklarla uzatır (Second Ship: 6 vuruş → 9 vuruş,
  eklenen üçü de "yan yana" kompozisyonlar)
· Çapa blokları, spoiler kapısı, negatif çekirdek iki bölümde ortak —
  bir kez yazılır
· Hiçbir klip iki formatta ortak KULLANILMAZ (kural 1.1: kırpma yok)
```

---

# 5. ✂️ FRAGMAN NE DEĞİLDİR — dört ölçülmüş tuzak

```
① ÖZET DEĞİLDİR      filmi 6 sahnede yeniden anlatmak (Slow Tide/Slow
                     Stone dikey türevlerinin hatası)
② EN İYİ ANLAR DEĞİLDİR  bağlamsız güzel kare dizisi mekanik kurmaz;
                     vuruşlar birbirine bir şey ÖĞRETMELİDİR (§1.3)
③ İKİNCİ FİLM DEĞİLDİR   fragmana yeni sahne/varlık/novum yazılmaz;
                     her vuruşun kaynak sahnesi tabloda gösterilir
④ KANITSIZ SÖZ DEĞİLDİR  fragman kaynak filmde OLMAYAN bir vaat kuramaz —
                     izleyicinin fragmandan aldığı soru, filmin gerçekten
                     cevapladığı soru olmalı
⑤ AÇIKLAMA KUTUSUNDA ÖZETLENMEZ  kurgu testini geçen bir fragman
                     paketlemede çöker: açıklama metni olay dizisini
                     verirse borç silinir, başlık "short film" derse
                     izleyici filmi izlediğini sanır ve kaynak filme
                     hiç gitmez [DERS 114 · Cold Burn fragman paketi]
```

## 5.1 ⛔ YASAĞIN NEREDE YAŞADIĞI — §0 tablosu tek başına yetmedi

> 17.08.2026'da ölçüldü. §0 tablosu "SENARYO_QA fragmana koşulmaz" der ve
> bu satır doğrudur; ama **rubrik, operatörün videoyla birlikte yapıştırdığı
> tek dosyadır** — kılavuzu ne model görür ne koşu anında kimse açar. Cold
> Burn'ün dikey fragmanına SENARYO_QA koşuldu, rubrik fragmanı film sandı ve
> tasarımını kusur diye faturaladı.

```
Yalnız kılavuzda yaşayan bir yasak, koşulmamış bir kapıdır [D74 mantığı].
Yasak bugün ÜÇ yerde birden duruyor:
  · bu kılavuzun §0 tablosu               (insan için)
  · rubriklerin STEP 0.b MATERIAL TYPE     (model için)
  · AGENTS.md ortak adım ⑧ FRAGMAN MERCEK KAPISI (operatör için)
Yeni bir mercek eklenirse üçü birden güncellenir → DERS 111.
```

---

# 6. 📚 KAYNAKLAR

**Depo içi:** iki emsal dosya (başta) · `HOOK_VE_ILK_SAHNE_KILAVUZU.md` (S0) ·
`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` (loop §5, vuruş bantları §2) ·
`SHORTS_SISTEM_PROMPTU.md` (güvenli alan) · `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md`
(cue yapısı) · `SAHNE_DEVAMLILIK_KILAVUZU.md` §2.1 (çapa blokları) ·
`VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` (paketleme)

**Dış araştırma (12.08.2026):** fragman 3 perdeli kurulur, cold open fiilen
4. perdedir; malzeme filmin 1. ve 2A perdesinden seçilir, 3. perde asla;
kurgu vuruş güdümlüdür ve ritim hızlanır; teaser 15-90 s / trailer 1-3 dk;
ilk 5-7 saniyede güçlü an zorunlu.
Kaynaklar: [StudioBinder — How to Make a Movie Trailer](https://www.studiobinder.com/blog/how-to-make-a-movie-trailer/) ·
[Derek Lieu — Trailer 3-Act Structure](https://derek-lieu.medium.com/the-matrix-and-movie-trailer-3-act-structure-b06a68e01214) ·
[PremiumBeat — 3 Ingredients Every Great Trailer Needs](https://www.premiumbeat.com/blog/3-ingredients-every-great-trailer-needs/) ·
[Film Editing Pro — Trailers, Teasers & Promos](https://www.filmeditingpro.com/trailers-teasers-promos-lengths-formats-tips/) ·
[Rareform Audio — Trailer Music Structure](https://www.rareformaudio.com/blog/how-production-music-reveals-trailer-structure) ·
[Beverly Boy — Teaser vs Trailer](https://beverlyboy.com/filmmaking/teaser-vs-trailer-whats-the-difference/)

---

> **Bu dosya ne zaman güncellenir**
> □ Yeni fragman üretilip QA'dan geçince → tuzak/ders çıktıysa §5'e ekle
> □ Vuruş bantları değişirse (yeni format) → §0 tablosu
> □ İlk yatay fragman koşusu → §3'ün "ilk gerçek koşu" notu buraya
