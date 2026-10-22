# 🌍 YERÇEKİMİ (YERCEKIMI)

## ADIM 1 PLANI — Süre kararı, faz kilidi, hikaye omurgası
### 3 Perde × 10 Faz × 12 Sahne = 120 sahne × 8s = **16 dakika 00 saniye** | 16:9 Yatay
### _"Aşağısı yok. Ta ki geri gelene kadar."_

> Bu dosya master İncil (`README.md`) DEĞİLDİR. Format kılavuzunun
> **ADIM 1**'idir: faz sayısı burada kilitlenir, hikaye omurgası burada
> onaylanır. Onaydan sonra README.md → REFERANS_PAKETI.md → fazlar yazılır.
>
> **Yapı kaynağı:** Gravity (2013) yapı sökümü — dört derin araştırma
> raporunun süzme kaydı: `kilavuzlar_ve_sistem_dosyalari/URETIM_ONCESI_ANALIZ/
> 04_ARASTIRMA_BULGULARI.md` §TUR 2. Oran seti, bayrak yarışı iskeleti,
> sayaç kadansı ve fizik/ses kilitleri oradan gelir; oranların bu plandaki
> sahne karşılıkları aşağıda faz faz doğrulanmıştır.

---

## 🧭 KULVAR VE ÖNERME — bilinçli karar

```
KULVAR: SERT UZAY GERİLİMİ (novum yok, DURUM var — UZAY_SENARYO §1
karar noktası: "Gravity, The Martian aynı kulvarda... bilinçli bir seçim
olmalı, kaza olmamalı." → BİLİNÇLİ SEÇİLDİ, adı kondu.)
Emsal: THE QUIET IMPACT — "novumu gerçek fizik olan ilk film" ailesi.

ÖNERME (tek cümle): "Alçak yörüngede bir enkaz kaskadı başlarsa,
o enkaz doksan dakikada bir aynı gökten geri gelir."   (Kessler kaskadı)

ÖNERME SATIRI (≤5 kelime): "Enkaz doksan dakikada bir döner."

NOVUM TAŞIYICISI: enkaz sürüsü × tutunma/bırakma jesti →
  sessiz kasırga: ses yok, rüzgâr yok, ama her şey parçalanıyor
  (taşıyıcı SOMUT: metal parçalar + eller. Optik fenomen değil [D73].)

ÜÇ KAPI [ONERME §4]:
 ① TEK KARE  ✅ S15: gökyüzünün yarısı güneşte parlayan paralel metal
    çizgileriyle "akıyor", önde astronot sakin çalışıyor — anomali
    1 saniyede işaretlenir.
 ② KİNETİK BAĞIMSIZLIK  ✅ dalga sahneleri repliksiz de okunur:
    parçalar kadrajı sessizce tarar, teleskop kopar, figür savrulur —
    ses/metin/replik gerekmez.
 ③ BAŞLIK ŞEMASI  ✅ şartlı: film adı YERÇEKİMİ (kullanıcı kararı,
    tek kelime); yön verme işini kapak üstlenir (enkaz yayı + astronot).
    Kapı paketlemede ikinci kez koşulacak [PAKETLEME §1].

KURAL TEKRARI [ONERME §5]: kurulum S16-S18 (dalga 1, mekik) →
doğrulama S53 (istasyonda dalga hasarı okunur) → sonuç S94-S96
(dalga 2, istasyon) — ≥3 sahne, ≥2 farklı nesne ✅. Bu sahneler
kurgu kapısının KESİLEMEZ listesine girer.
```

### 🎯 TEMA

```
TEMA: FEDAKÂRLIK          (TEMA_MUHENDISLIGI §3 tablosu; süreç teması —
                           yatay format uyumu §4 ✅; takas kalıbı DEĞİL)

TEK CÜMLE (novum kelimesi yok):
"Hayatta kalmak, sana verilenleri taşımayı öğrenmektir."

MOTİF [TEMA §5 satırı]: verme / azalma —
  oksijen halkası film boyu AZALIR (sayaç motifin fiziğidir),
  el ele aktarım: kanca · oksijen disiplini · saat · iniş kolu.

TEMA → MOTİFE DÖNDÜĞÜ SAHNELER (betik bu indeksleri arar):
  S30  yara + saat repliği — oksijen krizi ÜSTÜNE bindirilmiş ekim
  S43  feda: kancayı açan el (bedelli seçimin aynadaki yarısı)
  S84  CENTRAL CHOICE: vanayı geri açmak = ölünün sesini bırakmak
  S117 durmuş saati kurmak — verileni taşımayı kabul etmek
B2 çaprazı ✅: bedelli seçim sahnesi (S84) listede.
```

---

## ⚙️ FORMAT KARARLARI VE SAPMALAR

```
1. FAZ SAYISI: 10 (3-4-3) · SAHNE SÜRESİ: 8 s   ← BU ADIMDA KİLİTLENDİ
   120 sahne × 8 s = 960 s = 16:00

   🔴 ⛔ AÇIK KAPI — KLİP SÜRESİ ÖLÇÜLMEDİ [D124 · 30.08.2026 denetimi]
   KLİP SÜRESİ = ____________  ← ffprobe çıktısı buraya yazılacak
     ölçüm komutu:
     ffprobe -v error -show_entries format=duration -of csv=p=0 <test.mp4>

   D124 (🔴, 25.08.2026): "planın ızgarası bir TERCİH değil, bir ÖLÇÜMDÜR."
   Bu ders depoya ÜÇ filme mal oldu (Iron Slope · First Morning · Wrong
   Shadow: plan 8 s, araç 10,005 s). Dersten sonra yazılan iki film
   (THE NEAR PASS · THE HEAVY SIDE) ızgarasını ÖLÇÜMDEN kurdu.
   YERÇEKİMİ 8 saniyeyi format kartından aldı
   (`yatay_10_20_dk_filmler/README.md` satır 19: "Veo native — extend
   gerekmez") ve o satırın hiçbir ölçüm atfı YOK. ⚠️ Format kartı ile
   D124 şu an birbiriyle ÇELİŞİYOR ve kimse uzlaştırmamış.

   ⛔ TEK KARE ÜRETİLMEDEN ÖNCE koşulacak:
     ① Bir test klibi üret, ffprobe ile ölç, sayıyı yukarıya yaz.
     ② Sayı 8,0 ± 0,2 ise: bu plan aynen geçerlidir, hiçbir şey değişmez.
     ③ Sayı farklıysa İKİ YOL var ve biri SEÇİLİR:
        (a) IZGARA ARAÇTAN yeniden yazılır: sahne_başı(n) = (n−1) × ölçüm.
            Yüzdeler KORUNUR (ızgara tekdüze) → feda %35,0 · orta nokta
            %50 · doruk %78 aynı sahnelerde kalır. Değişen YALNIZ mutlak
            saniyelerdir: replik defterleri (sayı README §REPLİK
            LİSTESİ'nde — tek yer, kural ①), chapter haritası,
            MUZIK_VE_SES yayı ve promptlardaki "8 seconds" ibaresi.
        (b) 8 saniyede ISRAR edilirse [D124 ③]: her sahneye KIRPMA
            TALİMATI yazılır — "S_n: 0,0-8,0 kullanılır; kalanı atılır,
            kesme noktası <şu kare>". ⛔ Şu an 120 sahnenin 120'sinde
            kırpma talimatı YOK; talimatsız kırpma yapılmıyor [D100].
   ⛔ Bu satır doldurulmadan üretim başlamaz. Kaydı olmayan kapı
      koşulmamış kapıdır [D74].
   · 8 s = format varsayılanı, Veo native, extend/retime BEDELİ YOK
     (Second Ship'in 10 s sapması bilinçli olarak ALINMADI)
   · 10 faz = format tablosunun "iki karakter / çift arc" satırı;
     dış araştırmanın bağımsız ölçekleme önerisiyle (16:00 · 10 faz ·
     3-4-3 · doruk %78-80) birebir örtüştü [04_ARASTIRMA §TUR 2].
   · Proje sahibi kararları (27.08.2026): 8 s ızgara · 10 faz · 16:00 ·
     iki karakter + feda ~%35 · SU 0 KARE · ATEŞ 0 KARE.

2. PERDE DAĞILIMI: I=3 / II=4 / III=3
   ✓ Perde II en uzun · Perde I en uzun değil · her perde ≥2 faz
   ✓ DORUK fazı (Faz 9) tek başına en yoğun faz

3. ⚠️ İKİ KARAKTER — TÜR KARTI SAPMASI (bilinçli, yazılı)
   §4.1 "tek kâşif" der. Bu filmde iki insan var; ikinci karakter
   S43'te anlatıdan çıkar (feda; oran §KARAKTER B kartının ÇIKIŞ
   satırında — tek yer, kural ①) ve film tek karaktere düşer.
   · Emsal: THE COLD BURN (deponun ilk iki insanlı filmi; bütün
     replikler kask telsizi) + format tablosunun 10 faz satırı.
   · ZORUNLU ÖNLEMLER: iki insan AYNI KAREDE en fazla 14 sahnede
     (%12); geri kalan diyalog telsizle (A konuşur, B'nin karesi
     görünür ya da tersi). Aynı-kare sahnelerinde iki gövdenin
     hareketi AYRI cümleyle yazılır (tek dönüş vektörü riski —
     04_ARASTIRMA §TUR 2 Veo bulgusu).

4. ⚠️ SIRT ÜNİTESİ — D79 BLOĞU SAPMASI (yalnız B karakteri)
   B'nin itici ünitesi (MMU) hikâyenin taşıyıcısıdır ve SIRTTADIR.
   D79 "flat back" bloğu B promptlarında değiştirilir: ünite POZİTİF
   ve sayısal tarif edilir (çerçeve geometrisi README Bible'da kilitlenir).
   A karakteri D79'a birebir uyar: düz sırt silüeti, şeffaf vizör.

5. ⚠️ KASKSIZLIK — TEK SAHNE KURALI SAPMASI [YANASMA §2.2⑤]
   F5-F8 iç fazlarında (istasyon + kapsül) A kasksızdır — tek sahne
   değil, dört faz. TELAFİ: kasksız hiçbir sahnede A KONUŞMAZ
   (yalnız nefes — HUMAN register); konuşan her ses hoparlör/telsiz
   kaynaklıdır ve kadraj dışıdır. Lip-sync gereken kare: 0.

6. FİNAL: KAPALI (kurtuluş) + held frame [UZAY_SENARYO §15] + açık
   kalan tek soru (gökteki enkaz çizgileri sürüyor).
   Kapalı finalin bedeli yazılı [FINAL §2]: bu film paylaşım değil
   GÜVEN satın alır — kanalın ilk 16 dakikalık filmi için doğru takas.

7. PROMPT UZUNLUĞU: video 2.000-2.600 karakter (image: gözlem bandı).
   Promptlarda film/karakter özel adı YOK [D34 + homage sınırı:
   MESHUR_SAHNE_KALIPLARI §4 — "Gravity gibi" kalıbı YAZILMAZ; sahneyi
   ikonik yapan matematik (ışık oranı · ölçek ilişkisi · kompozisyon)
   yazılır].

8. ÜRETİM: Start/End Frame zinciri (format standardı, sapma yok).
   150 imaj / 120 video. Faz başı kimlik yenileme protokolü zorunlu.
   Uzun plan HİSSİ: klipler arası momentum devamlılığı + kesmenin
   oklüzyon/hızlı geçiş anına gizlenmesi; geniş→makro geçiş tek
   klibe SIKIŞTIRILMAZ (hyper-lapse riski) [04_ARASTIRMA §TUR 2].
```

---

## 👥 KADRO

```
┌─ MÜHENDİS (A — filmi taşıyan) ───────────────────────────────┐
│ Bible adı: DENİZ ARAT, 38                                    │
│ Promptta:  "a 38-year-old woman flight engineer" [D34]       │
│ İşlev:     İlk uzay görevindeki yük mühendisi. Prosedüre     │
│            sığınan, geri dönmek için sebebi kalmamış insan.  │
│ YAY:       prosedür kabuğu → çıplak hayatta kalma →          │
│            teslimiyet → yaşamayı SEÇMEK → yerde durmayı      │
│            yeniden öğrenmek                                  │
│ Kusuru:    Yası bir iş programına çevirmiş: "uyanırım,       │
│            çalışırım." Dönmek istemediği için uzayda iyidir. │
│ YARASI:    İkiz kardeşi bu programın pilotuydu; iniş         │
│            kazasında öldü. Bileğinde onun DURMUŞ kurmalı     │
│            saati (kişisel eşya bütçesinin nesnesi, §Bütçe).  │
└──────────────────────────────────────────────────────────────┘

┌─ KOMUTAN (B — S43'te çıkar) ─────────────────────────────────┐
│ Bible adı: SARP EGE, 52                                      │
│ Promptta:  "a 52-year-old man mission commander" [D34]       │
│ İşlev:     Son görevindeki kıdemli. Mentor arketipi —        │
│            anlatıdan fiziksel çıkışı A'nın ayağa kalkma      │
│            şartıdır [04_ARASTIRMA §TUR 2].                   │
│ YAY:       rutini espriyle taşıyan usta → fedayı da aynı     │
│            sakinlikle taşır → SESİ kalır (telsiz, sonra      │
│            halüsinasyon telsizi), bedeni dönmez              │
│ Ekipman:   Sırtında MMU itici çerçevesi (sapma 4). Yakıt     │
│            göstergesi Çehov 3'tür.                           │
│ ÇIKIŞ:     S43 (5:36 = %35,0) — feda vuruşu; gövdesinin      │
│            son karesi S45 (5:52).                            │
│            İkinci görünüş S73-84 YALNIZ SES (halüsinasyon    │
│            telsizi; ekranda gövde YOK — sapma 5 ile uyumlu). │
└──────────────────────────────────────────────────────────────┘

FEDA FİZİĞİ — Gravity'nin ölçülmüş ihlali KOPYALANMAZ
[04_ARASTIRMA §TUR 2 "bilinçli ihlaller" satırı]:
  İstasyon 6°/s (dakikada bir tur) DÖNMEKTEDİR (kanıt: arka planda
  yıldız alanı/Dünya ufku sabit hızla kayar). A paraşüt halatlarına
  dolanmış, B 12 m halatın ucundadır; dönme merkezkaçı B'yi SÜREKLİ
  dışa çeker — ~16 N, küçük ama sıfır olmayan SABİT kuvvet. Aynı
  kuvvet A'ya ~2 N düşer (o gövdeye yakındır) → feda B'nin
  karakterinden değil KONUMUNDAN doğar. Halat ikisini taşımaz değil —
  A'nın dolandığı halat DEMETİ sökülmektedir: yük altında bir kat
  açılır (görünür sayaç: 3 kat → 2). B kancayı bu aritmetik ekranda
  kanıtlandıktan sonra açar; kalan iki katın TUTMASI (S46) onun
  hesabının doğru çıkmasıdır.
  ⚠️ 29.08.2026: dönüş 2°/s → 6°/s ve sayaç 3→2→1 → 3→2→tutar.
     Gerekçe ve hesap: FAZ_04_FEDA/FAZ_04_FEDA.md KİLİT 13-14. Fizik merceği (⑥)
  bu sahneyi bu sayılarla ölçer.
```

---

## 🌍 DÜNYA — ALÇAK YÖRÜNGE

```
YER: Dünya alçak yörüngesi, ~410 km. Film %90 VAKUM (ortam kartı §3.1),
  F10 zemin sahneleri DÜNYA ATMOSFERİ (§3.3 fiziği — bozkır, kuru göl
  yatağı; SU YOK).
IŞIK MANTIĞI [Light Box'ın prompt karşılığı — 04_ARASTIRMA §TUR 2]:
  tek sert kaynak GÜNEŞ + Dünya = devasa mavi-beyaz yumuşak dolgu
  (bounce). Gece tarafında dolgu ölür, şehir ışıkları nokta desendir.
  Olaylar (parçalanma, alarm) yüze/vizöre RENK yansıması olarak düşer.
  Lens KÜRESEL, anamorfik parlama yasak [§3.1].
SES MİMARİSİ (birinci ağız kaynaklı — Freemantle/Price/Lievsay kuralları):
  dış sahnelerde efekt YOK; ses yalnız TEMAS titreşimiyle (matkap,
  tutunma, çarpma gövdeden boğuk gelir, temas kesilince milisaniyede
  söner). Müzik = efekt İKAMESİ (patlamanın kendisi değil kinetik
  nabzı) ve PERKÜSYONSUZ. Kask içi perspektifte dış frekanslar
  filtrelenir; nefes tek duyumdur. Doruk öncesi MUTLAK sessizlik
  bıçağı tek kez kullanılır (S94 dalga anı). Ayrıntı MUZIK_VE_SES.md'de;
  sub-bass↔telefon çelişkisi orada kapanır (missing fundamental,
  GOOGLE_FLOW_MUSIC §15.1a).
ENKAZ SAATİ (filmin saati):
  Diegetik döngü 90 dakika (B hesaplar, S22). EKRAN karşılığı ~10,5
  dakika: dalga 1 = S16 (2:00) → dalga 2 = S94 (12:24). Zaman
  sıkıştırması Gravity'de ölçülmüş ve fark edilmemiştir (90 dk → 54 dk)
  [Bordwell · 04_ARASTIRMA §TUR 2]: saat SÜREYLE değil HATIRLATMA
  RİTMİYLE işler. Hatırlatma kanal sırası: diyalog → gösterge → nefes;
  aralıklar doruğa doğru sıklaşır.
OKSİJEN SAYACI (Kart 5 — çift yönlü çözüm):
  ekranda RAKAM YOK; gösterge = kapanan DOLULUK halkası (segment söner).
  Sayı yalnız SES kanalında ve YALNIZ MACHINE register'da (suit AI):
  "OXYGEN 62 PERCENT" → 41 → 23 → 11 → 6 → 3 (aralıklar eksponansiyel
  sıklaşır — senaryo kadansı, 04_ARASTIRMA §TUR 2). İnsan repliği sayı
  SÖYLEMEZ [D82].
```

---

## 🃏 RİSK SAYIMI [02_RISK_KARTLARI · payda 12]

```
⚠️ KARTLARDA OLMAYAN ANLATI RİSKLERİ [30.08.2026 denetimi — beyan]
  Risk kartlarının 12'si de ÜRETİM tarafıdır; aşağıdaki üç risk
  hiçbir kartta yok ve bu plan onları BİLEREK üstleniyor:
  ① TEK MEKÂN KUŞAĞI: S58-S84 = 27 ardışık sahne (3:36) 2,4 m'lik tek
     kapsül konisinde; S49-S84 = 36 sahne (4:48) iç mekânda.
     KURGU_RITMI §2 makro örüntü kırıcıyı "her 3-4 sahnede bir mekân/
     tempo değişimi" olarak ister. Panzehir: her sahnede ölçek kademesi
     değişimi · F7'de lomboz mavisinin dönüşle gelip gitmesi · S68
     Overview · ses olayları (çoban · halüsinasyon · S84'te cızırtının
     ani kesilmesi). ⛔ Kabul edilen bedel: bu kuşak %30-65 bandına
     düşüyor, yani kılavuzun "orta bölüm çöküşü" yuvası.
  ② SESSİZ PROTAGONİST: A'nın son repliği S45 (5:52). Sonrasında 75
     sahne (10:08) protagonist sesi yok; F9 ve F10 diyalog yükü 0, yani
     son 24 sahne (3:12) tamamen sessiz. Sebep kask takvimi (kasksız
     sahnede replik 0) ve bu bilinçli — ama telafisi F8-F10'un görsel
     olay yoğunluğuna borçludur.
  ③ MÜZİK 0 OLAN FAZ: F7 (S73-S84) baştan sona müziksiz [§5.3 yuvası].
     ①+②+③ aynı kuşakta üst üste biniyor: S73-S84 hem tek mekân, hem
     sessiz karakter, hem müziksiz. Bu üçlü BİLEREK seçildi; kurgu
     masasında ilk kırpılacak yer burasıdır.

TETİKLENEN KARTLAR: 7/12 → tasarım sonrası ÇEKİRDEK 5/12 (tam eşik)
  KART 3  kask/vizör       → HELMET STATE SCHEDULE (aşağıda, C bloğu)
  KART 4  ikinci figür     → HUMAN COUNT LOCK sahne sahne (C bloğu)
  KART 5  ekran/sayaç      → halka + MACHINE ses; rakam 0 (A1 temiz)
  KART 6  parçacık (enkaz) → dalga sahnelerinde yakın alanda ayrık
                             parça sayısı YAZILI (≤12), gerisi uzak
                             paralel çizgi; vakumda duman/alev 0 kare
  KART 7  diyalog          → karşılıklı atışma yok; turn-lock; sayılar
                             MACHINE; en güvenli iki yerleşim ağırlıklı
  KART 9  ışık mıknatısı   → TASARIMLA KAPATILDI: yaklaşma sahnelerinde
                             kamera HEDEFTE, hareket kameraya doğru
                             [UZAMSAL §6.8 baştan uygulanır]; hedef
                             hiçbir kadrajda tek baskın ışığın
                             karşısına konmaz
  KART 10 insansız sahne   → işaretli (~10 sahne); o promptlarda
                             NEGATIVE tek pozitif Style satırına iner

MALZEME AZALTIMI (proje sahibi kararı, 27.08.2026):
  SU 0 kare (göl finali İPTAL → kuru zemin inişi; gözyaşı sahnesi de
  YOK — duygu nefes/el/ses kanallarına devredildi) · ATEŞ 0 kare
  (istasyon yangını → basınç kaybı + sönen sistemler; atmosfere giriş
  DIŞARIDAN gösterilmez, İÇERİDEN yaşanır) · CANLI 0 · PATLAMA 0
  (parçalanma soğuk/kinetik, alevsiz).

KARTLARDA OLMAYAN 1 NUMARALI RİSKLER (bu filme özgü, plana yazıldı):
  ① İKİ GÖVDELİ SIFIR-G: aynı kadrajda iki süzülen figüre model TEK
    dönüş vektörü atar → aynı-kare bütçesi 14 sahne + her promptta
    iki gövdeye AYRI hareket cümlesi.
  ② D23 SIFIR-G RİJİTLİĞİ: süzülen beden rijit çıkar → her dış
    sahnede mikro hareket satırı (eksen dönüşü, uzuv sürüklenmesi).
  ③ DALGA ANI: çok parçacık + yüksek hız + iki gövde AYNI sahnede
    olamaz — dalga sahnelerinde kadrajda en fazla 1 insan.
  ④ POLİTİKA SÖZLÜĞÜ: "debris strikes her" tipi şiddet fiili ve
    tehlike kelimeleri nötrlenir ("fragments cross the frame");
    negatif bloklara yasak-kelime sokulmaz [YASAK LİSTESİ TUZAĞI].
```

---

## 🏛️ 3 PERDE / 10 FAZ HARİTASI

| Perde | Ad | Faz | Sahne | Süre | Zaman |
|---|---|:---:|:---:|:---:|---|
| **I** | YUKARISI | 1-3 | S1-36 | 288s | 0:00 – 4:48 |
| **II** | BOŞLUK | 4-7 | S37-84 | 384s | 4:48 – 11:12 |
| **III** | AĞIRLIK | 8-10 | S85-120 | 288s | 11:12 – 16:00 |

**Oran doğrulaması** (Gravity oran seti → bu ızgara):
katalizör %10-15 → dalga 1 S16-18 (2:00-2:24 = %12,5-15 ✅) ·
feda %30-35 bandı → S43 (5:36 = %35,0 ✅ · bandın tam kenarında) ·
orta nokta %50 sahte zafer → S60 (8:00 ✅) ·
her şey kaybedildi → S72-78 (%60-65; 16 dk ölçeğinde Faz 7 bandı) ·
doruk başlangıcı %78-80 → S94-97 (12:24-12:48 ✅) · çözülme %90+ → F10 ✅.

### PERDE I — YUKARISI

```
FAZ 1  GOREV                                      0:00 – 1:36  S1-S12
  Yörüngede rutin onarım: teleskop servis platformu + mekik.
  S1 = KAPAK ANI karesi (aşağıda §HOOK). İki karakter tanıtımı:
  A panelde çalışır (yetkinlik), B MMU ile çevrede süzülür, telsizde
  hafif gevezelik — KONTROL (yer) üçüncü ses.
  İSİM-İSTEK-BEDEL ≤ S12 [KARAKTER §3]: rol = onarım ekibi (kostüm),
  istek = paneli kapatıp eve dönmek (görünür hedef: mekik kapısı),
  bedel = bilek konsolundaki oksijen halkası + görev süresi.
  S8: EL İNSERTİ — eldivenli bilekte DURMUŞ kurmalı saat (Çehov 2;
  2 sn, bakışla vurgulanmaz) [tohum penceresi %10-15 içinde].
  ⚠️ ÇEHOV 3: B'nin MMU göstergesi yarıda — "yakıtın yarısı hikâye
  anlatmaya gider" esprisi (telsiz).
  S11: DRAMATİK İRONİ AÇILIR — arka planda, A'nın görmediği yerde,
  gökyüzünde ince bir parıltı çizgisi büyür. İzleyici görür.
  FAZ KAPANIŞI: KONTROL'ün sesi kesilir, statik.

FAZ 2  DALGA                                      1:36 – 3:12  S13-S24
  S13-14: KONTROL geri gelir, tek cümle: görev iptal, ayrılın.
  S15: 🔥 VİRAL ARA #1 — gök "akıyor": güneşte parlayan paralel
  çizgi sürüsü (TEK KARE TESTİ karesi). S15'te gökte sabit küçük
  parıltı: İSTASYON (Çehov 4 — tohum, 2 sn, vurgusuz).
  S16-18: DALGA BİR. Sessiz parçalanma: teleskop kolu kopar, mekik
  delinir, A'nın halatı kopar — savrulur (momentum kilidi: sabit
  dönüş hızı, kadrajda tek insan).
  S19-21: A boşlukta döner; nefes hızlanır; suit AI ilk sayı:
  "OXYGEN 62 PERCENT". S22: B'nin telsiz hesabı: "doksan dakika"
  (Çehov 5).
  S23-24: B MMU ile yaklaşır, yakalar, kancalar.
  FAZ KAPANIŞI: mekiğin enkazı arkalarında — dönüş aracı YOK.

FAZ 3  HALAT                                      3:12 – 4:48  S25-S36
  Bağlı süzülüş istasyona doğru (kamera hedefte — Kart 9 çözümü).
  S27: MMU yakıt göstergesi kırmızıda (Çehov 3 ateşleme başlangıcı).
  S30: ⭐ YARA EKİMİ — oksijen düşerken (AI: "41") B dikkat dağıtmak
  için sorar; A tek replikte (≤10 s, eylem üstünde): kardeş + saat +
  "artık sadece çalışıyorum". [McKee "cephane": soru A'yı hayatta
  tutma aracıdır — hiperventilasyonu yavaşlatma talimatıyla birlikte.]
  S33: istasyonun YAVAŞ DÖNDÜĞÜ görülür (yıldız alanı kayar — feda
  fiziğinin kurulumu, Çehov 7).
  ▶ PERDE DÖNÜŞÜ 1 (EŞİK · S36): MMU yakıtı biter; istasyona
  frenlenemeyen bir yaklaşma başlar — geri dönüş yolu kapandı.
```

### PERDE II — BOŞLUK

```
FAZ 4  FEDA                                       4:48 – 6:24  S37-S48
  ✅ YAZILDI 29.08.2026 — FAZ_04_FEDA/FAZ_04_FEDA.md · prompt_kontrol GO
  S37-38: sert temas ve sekme; A'nın botu handrail direğine dolanmış
  paraşüt halat demetine girer, B gövdeden seker ve dışarı çıkar
  (MMU boş — geri gelemez).
  S39-42: merkezkaç B'yi dışa çeker; demet yük altında açılır
  (görünür sayaç: 3 → 2). B hesabı S40'ta yapar, A S42'de reddeder.
  S43: ⭐ FEDA (%35,0). B kancayı kendi eliyle açar — tek cümle
  telsiz repliğiyle; ağırlık sözde değil ELDE.
  S44: 🔥 VİRAL ARA #2 — bir halat, iki uç.
  S45: ⭐ ÖLÇEK 1:10 — 60 m'lik yapı, iki leke. B'nin gövdesinin
  son karesi; sesi hâlâ düz ve sakin.
  S46-47: kalan iki kat TUTAR (B'nin hesabının kanıtı); A kendini
  kurtarır, airlock koluna gider. B'nin sesi S47'de mesafeden değil
  GEOMETRİDEN kesilir: modülün kenarı araya girer.
  S48: A içeride; kask ZATEN çıkmış; CENİN POZU — kordon gibi süzülen
  hortumlar (rahim motifi). Kasksız bölüm başlar (sapma 5: bundan
  sonra A konuşmaz).
  FAZ KAPANIŞI: ilk ODA TONU — filmde ilk kez vakum değil HAVA.

FAZ 5  ISTASYON                                   6:24 – 8:00  S49-S60
  ✅ YAZILDI 29.08.2026 — FAZ_05_ISTASYON/... · prompt_kontrol GO
  İstasyon yaralı: modül 2 delik ve VAKUMDA, kapağı mühürlü; A modül
  3'tedir. S53 kural doğrulaması: mühürlü kapağın gözlem camından ölü
  modül — nesneler düz çizgide, sabit hızda (insansız, Kart 10).
  Işıklar bölge bölge ölü (S54, bilgi elden gelir, rakam 0).
  S51: ⚠️ ÇELİŞKİ KAPANDI — bu satır önce "A çağrı yapar, statik
  döner" diyordu; ama S51 kasksızdır ve kask takvimi "kasksız sahnede
  replik 0" der. Çağrı KALDI, ses GİTTİ: A telsiz düğmesine iki kez
  basar (telsizde "orada mısın?"), hoparlör açık ve sabit cızırtıda,
  kimse cevap vermez. Sözsüz çözüm sahneyi büyüttü ve S76-81'in
  halüsinasyon fazına bir tohum bıraktı.
  S55: KAÇAK — A tehdidi MAKİNEDEN ÖNCE bulur (yetkinlik kuralı):
  mühürlü kapağın contası bozuk, hava ölü modüle sızıyor. Ekranda
  duman/buhar/parçacık 0 kare; tek kanıt contaya çekilen kayış ucudur.
  S57: basınç alarmı — makine ONAYLAR ve emir verir (ateşsiz tehdit;
  amber bir kademe artar, kırmızı ışık ve siren YOK).
  S58: A'nın eli İNİŞ ROKETLERİ kolunun üstünden geçer — kırmızı
  kapaklı kol, dokunmadan, vurgusuz (Çehov 6 ekilir).
  S59: iç kol çevrilir, kapak mühürlenir (hareket kadraj dışı, D69);
  İKİ BOŞ KOLTUK ilk kez kadrajda — üç koltuklu kapsülde tek kişi.
  S60: ▶ ORTA NOKTA (%50, tam 480/960 s) — SAHTE ZAFER: sistemler
  açılır, göstergeler sıra sıra yeşile döner ve yüzünü boyar.
  Nefes yavaşlar. Gülümseme yok.

FAZ 6  KAPSUL                                     8:00 – 9:36  S61-S72
  ✅ YAZILDI 29.08.2026 — FAZ_06_KAPSUL/... · prompt_kontrol GO
  ⭐ FİLMİN EN DAR FAZI: 12 sahnenin 11'i CU ya da daha yakın; tek
  geniş plan S68'dir (Overview). Biçim içeriği yapar.
  S61-62: YAKIT GÖSTERGESİ ÖLÜ — ana itki yok, sahte zaferin faturası.
  S62 ⭐ 0g TESLİMİYETİ REDDEDER: taslak "eller kucağa düşer" diyordu;
  0g'de el düşmez, kollar nötr duruşa YÜKSELİR. A çökmek ister, bedeni
  izin vermez — iki deneme, iki başarısızlık, sonra vazgeçiş. Filmin
  adı YERÇEKİMİ'dir ve burada eksikliği bir duyguyu imkânsız kılar.
  S63-64: pencere ve boş koltuk kurulur (S68'in ön şartları).
  S65-67: telsiz taraması; Dünya'dan tek yakalanan ses: anlaşılmayan
  bir dilde bir çoban, köpek sesi, ninni. TEK TARAFLI — A kasksızdır,
  konuşamaz ve adam onu duymuyor (Aningaaq işlevi).
  S68: 🔥 VİRAL ARA #3 / OVERVIEW SAHNESİ (tam 1 adet [UZAY_SENARYO
  §8]). Dört madde birebir: hareketsizlik · sessizlik (filmin en düşük
  seviyesi, ölçüm noktası) · geriye bakış (yakıt yok — Dünya gidilecek
  yer değil, GELİNEN yer) · süre. ⚠️ Beşinci madde ("karakter karenin
  1/20'si") iç mekânda imkânsızdır: 2,4 m'lik bir koninin içinde hiçbir
  kadraj onu 1/20'ye indirmez. Karşıtlık MEKÂN-PENCERE olarak kuruldu
  [D74]: kadrajın tamamı loş dar bir kutu, içinde otuz santimlik bir
  delik, o delikte bir gezegen. Literal 1:10 kareleri zaten var
  (S1 · S45 · S115 · S120).
  S69-70: pencereden dönüş; kardeşin durmuş saati dördüncü kez —
  S30'un jesti birebir tekrar eder, anlamı değişir.
  S71: teslimiyet — A oksijen vanasını KISAR (çeyrek tur; kapatmaz).
  Neden-sonuç tek karede: vana döner → halka 2/6 → 1/6 → AI uyarır.
  Yüz kadrajda YOK: bir yüz bu kararı açıklamaya çalışır, bir el
  yalnızca yapar. Çehov 1 (S9 oksijen zinciri) burada ödenir.
  S72: FAZ KAPANIŞI — ışıklar üç grup hâlinde söner, tek amber lamba
  kalır; A hiçbirine dokunmaz. S60'ın aynası (orada paneller sırayla
  yeşile dönüp yüzünü boyamıştı).

FAZ 7  SES                                        9:36 – 11:12 S73-S84
  ✅ YAZILDI 30.08.2026 — FAZ_07_SES/... · prompt_kontrol GO
  ⭐ Kurulum deseni bilinçli DÖNGÜ: F-G-F-D-E-D iki kez. Halüsinasyon
  budur — aynı şey ikinci kez, biraz daha yakından.
  HER ŞEY KAYBEDİLDİ yuvası [KARAKTER §5.3]: müzik TAMAMEN susar;
  kalan tek katman yavaşlayan nefes + kapsül gövde tıkırtıları
  (mutlak dijital sıfır YOK [D83]).
  S76-78: bilinç bulanır. TELSİZ ÇATIRDAR — B'NİN SESİ (halüsinasyon;
  ekranda gövde YOK, yalnız hoparlör ızgarası ve A'nın yüzü):
  önce eski bir espri, sonra bilgi: "iniş roketleri de rokettir."
  [Sahte kurtarış İŞARETLİ: izleyicinin bildiği fizik ihlal edilir —
  B'nin MMU'su S36'da boştu ve menzil imkânsızdı; ses karışımında
  telsiz bandı A'nın kask hoparlöründen DEĞİL her yönden gelir.
  04_ARASTIRMA §TUR 2 "halüsinasyon meşruiyet kuralı".]
  S79-83: karar olgunlaşır. ⭐ TİK (S18'de kuruldu) üç kez döner ve
  ölür: zayıf (S79) → sayar gibi (S82) → durur ve parmaklar vana
  çarkını kavrar (S83). Alışkanlık eyleme dönüşür.
  ⭐ S82 bir KURALIN ÜRÜNÜ: kask takvimi kasksız sahnede replik 0 der,
  yani A ölüyle KONUŞAMAZ. Bu kısıt doğru karardır — ölüyle konuşan
  karakter halüsinasyonu gerçek sayar, konuşmayan onu KULLANIR.
  Dudaklar açılmaya yeltenir, açılmaz; cevap bedenden gelir.
  S84: ▶ CENTRAL CHOICE — A vanayı GERİ AÇAR (çeyrek tur), yaşamayı
  seçer; bedel AYNI KAREDE: cızırtı ANİDEN kesilir, fade yok
  (ölünün sesini bırakmak — TEMA'nın dördüncü yüzü).
  ⛔ Halka DOLMAZ: 1/6'da kalır ve yanıp sönmeye başlar; açılan
  AKIŞTIR, seviye değil (MACHINE "%6 RECOVERING" der, ışık "uyarı"
  der — ikisi de doğru). Bible takvimiyle çelişen README satırı
  30.08'de düzeltildi.
  ▶ PERDE DÖNÜŞÜ 2 (GERİ DÖNÜŞ YOK): aynı çekimde el bir önkol yana
  gider ve iniş roketi kapağını AÇAR; altındaki tek kol görünür.
  ⭐ Üç iş tek çekimde — vana, susan hoparlör, açılan kapak — ancak
  vana ile kapak AYNI PANELDE olduğu için mümkün (F7 KİLİT 34).
```

### PERDE III — AĞIRLIK

```
FAZ 8  AYRILIS                                    11:12 – 12:48 S85-S96
  ✅ YAZILDI 30.08.2026 — FAZ_08_AYRILIS/... · prompt_kontrol GO
  ⭐ Yeni prompt standardıyla yazılan İLK faz: 12/12 imaj promptunda
  COMPOSITION bloğu · hareket kadraj oranı + süre olarak [D127] ·
  üretim kapıları sayısal kabul/ret ile [D144].
  ⚡ ŞOK BANDI 1 burada harcandı (S93 ECU → S94 WS, üç kademe).
  Filmde bir tane kaldı: S102.
  S85: sessiz telsiz — kayıp GÖRÜLÜR (bedelin sahnesi).
  S86-90: hazırlık: kemer, kontrol listesi, elle hedef hesabı
  (yetkinlik geri geldi; Gravity'nin Soyuz-Rusça paneli işlevi:
  A yabancı arayüzü sesli DEĞİL, jestle çözer — kasksız konuşma 0).
  S91-93: gök yeniden "akmaya" başlar — DALGA İKİ yaklaşır
  (hatırlatma: gösterge titrer, nefes sıklaşır; sayı yok).
  S94-96: ⭐ DORUK RAMPASI (%78-80): dalga istasyonu SESSİZCE
  parçalar (S94 mutlak sessizlik bıçağı — tek kez); S96 iniş
  roketleri ateşlenir, kapsül son anda ayrılır. (Dalga sahnelerinde
  kadrajda tek insan / insansız kareler — risk ③.)

FAZ 9  DUSUS · DORUK + İMZA ÇEKİM                 12:48 – 14:24 S97-S108
  ✅ YAZILDI 30.08.2026 — FAZ_09_DUSUS/... · prompt_kontrol GO
  ⚡ ŞOK BANDI 2 burada harcandı (S101 ECU → S102 WS, üç kademe).
  Filmin iki şok bandı da bitti; F10'da merdiven istisnasız 1 kademe.
  🎬 En yoğun faz. Bütçenin ~%35'i.
  S97-99: yörüngeden düşüş; kapsül titreşimi gövde sesiyle büyür;
  pencerede ışık ISINIR (renk kayması — alev 0 kare, giriş
  İÇERİDEN yaşanır).
  S101-103: ⭐ İMZA ÇEKİM (S102): YERÇEKİMİ YAĞMURU — kabinde film
  boyu süzülen her şey (toz, kalem, saat kayışı, su damlası DEĞİL;
  kuru nesneler) AYNI ANDA yere yağar; A koltuğa çakılır; kollar
  ağırlaşır. Filmin adını taşıyan kare. 8 varyasyon bütçelenir.
  S104-106: sarsıntı tepe yapar — ekran kararmaz, A bilincin
  kıyısında (nefes tek katman).
  S107-108: ana paraşüt açılır — ani yavaşlama, kemerde asılı gövde.

FAZ 10 ZEMIN                                      14:24 – 16:00 S109-S120
  ✅ YAZILDI 30.08.2026 — FAZ_10_ZEMIN/... · prompt_kontrol GO
  ⭐ 120/120 SAHNE TAMAM. Şok bandı yok (ikisi de harcandı); ölçek
  merdiveni 12/12 tam bir kademe. Alt açı (H) filme yalnız S118'de
  girdi. Ölçek 1:10 karesi zincirleme kısıt yüzünden S115→S113.
  S109-110: kuru göl yatağına sert iniş; toz perdesi (SU YOK);
  kapsül yan yatar; sessizlik.
  S111-114: kapak açılır; A dışarı EMEKLER — yerçekimi bacakları
  tutmuyor; toprağı avuçlar (el bütçesinin son büyük sahnesi).
  S117: ⭐ SAATİ KURAR — durmuş saat tik'ler (Çehov 2 ateşleme;
  temanın son indeksi). 
  S118-119: AYAĞA KALKIŞ — titrek, iki deneme, sonra dik duruş;
  kamera alt açıya iner (filmde ilk kez): ağırlık artık zafer.
  S120: FİNAL / HELD FRAME: geniş sabit kare — ayakta duran küçük
  figür, uçsuz düzlük; gökte sessiz ince çizgiler SÜRÜYOR (açık
  kalan tek soru + tohum dönüşü). Kesme yok, kart yok.
```

---

## 📈 DUYGUSAL YAY

```
Yoğunluk
10 │                                             ╱╲
   │              ╱╲                        ╱╲  ╱  ╲
 8 │             ╱  ╲       ╱╲             ╱  ╲╱    ╲
   │        ╱╲  ╱    ╲  ╱╲ ╱  ╲       ╱╲ ╱           ╲
 6 │       ╱  ╲╱      ╲╱  V    ╲     ╱  V              ╲
   │  ╱╲  ╱                     ╲   ╱                   ╲──╲
 4 │ ╱  ╲╱                       ╲ ╱                        ╲──
 2 │╱                             V                            ╲_/⌃
   └──┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┬────
     F1    F2    F3    F4    F5    F6    F7    F8    F9    F10
    0:00  1:36  3:12  4:48  6:24  8:00  9:36  11:12 12:48 14:24
    └── P I YUKARISI ──┘└──── P II BOŞLUK ────┘└─ P III AĞIRLIK ─┘

Dip noktası F7 (SES) — filmin en sessiz yeri, doruğun tam öncesinde.
F10 sonu F1 başından YÜKSEK biter: aynı insan değil, ayakta bir insan.
```

---

## 🔫 ÇEHOV ZİNCİRİ (kurulum → ateşleme)

| # | Kurulum | Sahne | Ateşleme | Sahne |
|---|---|:---:|---|:---:|
| 1 | Suit AI oksijen anonsları (rutin) | S9 | Vana = intihar aracı ve yaşam kararı | S71 · S84 |
| 2 | Durmuş kurmalı saat (kardeşin) | S8 | Saat kurulur, tik'ler | S117 |
| 3 | MMU yakıt göstergesi yarıda (espri) | S10 | Yakıt biter → feda zorunlulaşır | S36 · S43 |
| 4 | Gökte sabit parıltı = istasyon (tohum) | S15 | Tek sığınak | S37 |
| 5 | "Doksan dakika" hesabı (B, telsiz) | S22 | Dalga 2 istasyonu vurur | S94 |
| 6 | Kırmızı kapaklı iniş roketi kolu | S58 | Halüsinasyon bilgisi + ayrılış itkisi | S78 · S96 |
| 7 | İstasyonun yavaş dönüşü (yıldız kayması) | S33 | Feda fiziği (merkezkaç) | S43 |

---

## 🔢 SAYISAL KİLİTLER [kontrol listesi C bloğu]

```
İNSAN SAYISI   HUMAN COUNT LOCK — S1-S45: en fazla 2 (aynı karede 2
               olan sahne sayısı: 14 · listesi README sahne haritasında)
               S46-S120: tam 1 · insansız sahneler: ~10 (işaretli)
               ⚠️ 29.08: eşik S44 → S45. B'nin gövdesinin son karesi
               S45'tir (ölçek 1:10 sahnesi — orada beyaz bir noktadır).
               Yansıma/gölge/üçüncü figür 0.
KASK TAKVİMİ   HELMET STATE SCHEDULE — A: kapalı S1-S47 · kasksız
               S48-S120 (iç mekân + zemin; kasksız sahnede replik 0).
               B: kapalı, 44 sahnenin 44'ünde (yüzü yalnız vizör
               ARKASINDAN, 2 sahnede net: S30 · S43).
ÖLÇÜLER        istasyon gövdesi 60 m · kapsül dış çap 2,4 m · halat
               demeti 12 m · teleskop platformu 13 m · MMU çerçevesi
               sırttan 40 cm derinlik (hepsi README Bible'da kilitlenir)
YERÇEKİMİ      yörünge sahneleri 0g: serbest nesne yön DEĞİŞTİRMEZ,
               itkisiz dönüş DURMAZ, atılan kütle gövdeyi geri iter;
               A'nın savrulma dönüşü 20°/s SABİT · istasyon dönüşü 6°/s
               F9: ivme rampası (nesneler kabin kıçına doğru "düşer")
               F10: 1g — toz hızlı çöker, gölgeler normal
SIVI TEMASI    0 sahne (su 0 kare — proje sahibi kararı; gözyaşı dahil)
CANLI          0 (hayvan/canlı yok; çoban sesi YALNIZ ses)
PARÇACIK       dalga sahnelerinde yakın alanda ayrık parça ≤12, uzak
               alan paralel çizgi dokusu; duman/alev/ateş topu 0 kare
OKSİJEN        MACHINE ses zinciri: 62 → 41 → 23 → 11 → 6 → 3
               (S19 · S30 · S46 · S71 · S84 · S96) — ekranda rakam 0,
               halka doluluğu 6 kademe iner (aynı sahnelerde)
```

---

## 📊 BÜTÇELER [KARAKTER_VE_DUYGU §6 — 960 s ölçeği]

| Bütçe | Hedef | Bu planda |
|---|:--:|---|
| 👁️ göz görünürlüğü ≥%12 | ≥14 sahne | kasksız iç fazlar (F5-F7) + S30/S43 vizör içi — dağılım README'de |
| 🔁 tepki planı ≥%25 | ≥30 sahne | her olayın bedensel cevabı prompt satırı olarak (etkinlik kuralı §9.1) |
| ✋ el / mikro-jest ≥%15 | ≥18 sahne | S8 saat · S43 kanca · S71/S84 vana · S111-117 toprak+saat + inserts |
| 🚶 tam boy süzülüş/yürüyüş ≥%10 | ≥12 sahne | dış geniş planlar + F10 emekleme/kalkış |
| 🎒 kişisel eşya ≥%5 | ≥6 sahne | DURMUŞ SAAT (tek nesne; S8 · S30 · S48 · S102 · S117 + 1) |
| 🌌 ölçek kontrastı 1:10 | 2 sahne | S1 (kapak) · **S45** (feda sonrası ölçek karesi) — ikisi de TAM klip, kırpılmaz. 29.08: S44 → S45; S44'te ≤%10 pull-back var ve kamera hareketi ölçek kademesi değiştiremez |
| 🔁 Kuleshov döngüsü | ≥32 | A-B-A döngüleri sahne haritasında (README) |

```
ASL / KURGU [KURGU_RITMI §1]
  TARGET ASL BAND: 8.0 s (sabit ızgara — eğri yok, bilinçli sapma)
  GEREKÇE [D74]: format standardı sahne=çekim=klip · Veo native 8 s ·
  kırpma bütçesi yok; ritim KADRAJ İÇİ değişkenlerle taşınır.
  ÖRÜNTÜ KIRICI KAPISI [KURGU_RITMI §2]: ardışık iki sahne aynı
  ölçek + palet + ses dokusunda OLAMAZ — sahne haritası (README)
  üç sütunla yazılır ve çift çift denetlenir.

AÇI YAYI [ACI_YAYI §3-4 · plan düzeyi taahhüt]
  · Ardışık her çift: ≥1 ölçek kademesi VE ≥45° (şok bandı ≤2:
    S94 dalga · S102 yerçekimi yağmuru — işaretli)
  · Kurulum sayısı ≤ sahne sayısının yarısı; faz başına 4-6 kurulum
    ailesi, iskelet tekrarlı (A-B-A) — dizilim README'de
  · AÇI TİPİ ≥3: üst (yörünge geniş) · göz hizası (iç mekân) ·
    alt (S118-120 — filmde İLK alt açı finalde: ağırlık=zafer) ·
    + profil/OTS aileleri
  · Klip içi kamera: %90+ sabit kadraj (Kart 8); işaretli az sayıda
    sahnede tek yavaş drift — liste README'de
```

---

## 🪝 HOOK · KAPAK · FİNAL [HOOK §8 yedi madde + PAKETLEME §1]

```
HOOK TİPİ: ÖLÇEK ŞOKU (tek tip) — tanıdık eylem (panelde çalışan el)
  + imkânsız bağlam (ayakların altında dönen gezegen) aynı karede.
S0 SORU CÜMLESİ: "Altında hiçbir şey yokken bu insan neden bu kadar
  sakin?"
0. KARE: S1 — sağ üçte birde küçük astronot + platform silüeti; sol
  üçte ikide Dünya'nın aydınlık kavisi; süren hareket: Dünya'nın
  dönüşü + A'nın çalışan eli (hareketin ortasında açılış ✅).
İLK 2 SN SES: müzik YOK; tek diegetik katman = kask içi tek sakin
  nefes + telsizde uzak cızırtı. (erken müzik elendi ✅)
REVEAL İKİLİ KİLİT [D71]: enkaz teması S11'e kadar kadraj dışı;
  0:03'te yeni bilgi: serbest bir cıvata düz çizgide süzülüp
  kadrajdan çıkar — sıfır-g kanıtı (29.08: B'nin girişi S3'e alındı,
  kadro-2 bütçesi ve tek-figürlü kapak anı için).
S1'İN İKİNCİ BİLGİSİ (S2 bandı): bu bir ONARIM ve bugün SON gün —
  katalizör S16 ≤ %15 ✅.
BİLGİ ASİMETRİSİ: DRAMATİK İRONİ · taşıyıcı: arka plan hareketi
  (gökte büyüyen parıltı çizgisi, karakterler görmez) · an: S11 (1:20).
TOHUM: S8 durmuş saat + S15 gökte sabit parıltı (2'si de ≤2 sn,
  bakışsız) → final S117 (saat) + S120 (gök) geri döner.
KAPAK ANI [PAKETLEME §1 — 0:00-0:10 bandından]:
  S1 · 0:05 · sağ üçte bir: astronot+platform silüeti, sol üçte iki:
  Dünya terminatör kavisi · tek kaynak sert yan güneş + mavi bounce ·
  odak: vizörde Dünya yansıması · ölçek 1:10+ · kompozisyon üçte bir ✅
AÇILIŞ-KAPANIŞ ÇİFTİ [SENARYO_VE_VIRAL §2.3③]:
  S1 ayakların altında gezegen (asılı insan) ↔ S120 ayakların
  altında toprak (ayakta insan) — değişim tek bakışta okunur ✅.
FİNAL TİPİ: KAPALI + held frame · açık kalan soru sayısı: 1
  (gökteki çizgiler) · bedel notu sapma 6'da yazılı.
```

---

## 🗣️ DİYALOG PLANI [SES_VE_DIYALOG §1-2]

```
DİL: İngilizce (depo standardı). TOPLAM REPLİK: sayı tek yerde —
  README §REPLİK LİSTESİ (kural ①; F8-F10'un 4'ü hepsi MACHINE) — saniyeler
  faz dosyalarında formülle HESAPLATILIR [D122].
KANALLAR ve REGISTER:
  SUIT AI        MACHINE — bütün sayılar (oksijen zinciri, uyarılar)
  KONTROL (yer)  MACHINE-benzeri telsiz bandı — S13-14'te kesilir
  A (DENİZ)      HUMAN — yalnız kask KAPALIYKEN (S1-S47); kasksız 0
  B (SARP)       HUMAN — telsiz; S43 feda repliği; S76-83 halüsinasyon
                 telsizi (ekranda gövde 0)
  ÇOBAN/BALIKÇI  HUMAN — yabancı dil, tek taraflı, S65-67
YERLEŞİM GÜVENLİĞİ: ①  kadrajda insan yokken telsiz ②  sırttan/uzak
  kadrajda kask telsizi — ekranda okunan ağız hedefi: 0 kare.
KURALLAR: her replik <5 s · turn-lock (eşzamanlı konuşma yok) ·
  sayı söyleyen replik yalnız MACHINE [D82] · kasksız sahnede insan
  repliği 0 (sapma 5).
```

---

## 📊 ÜRETİM MATEMATİĞİ

```
120 sahne × 8 s                     = 960 s = 16:00
10 faz × 3 sekans × 5 imaj          = 150 imaj
10 faz × 12 sahne                   = 120 video (extend YOK — native 8 s)

MALİYET (Veo 3.1 Fast):
  960 s × ~$0.15/sn (tek geçiş)     = ~$145
  Gerçekçi (~3 deneme/sahne)        = ~$430
  + 150 imaj üretimi
  + iki-figürlü 14 sahne için sahne başına +2 deneme payı (~$34)

BÜTÇE DAĞILIMI:
  Faz 9 (DORUK + imza çekim)   %35   ← S102 için 8 varyasyon
  Faz 2 + Faz 8 (iki dalga)    %20
  Faz 4 (feda + viral #2)      %12
  Kalan 6 faz                  %33

ÜRETİM SIRASI (risk kapıları önce): S102 (imza) → S94-96 (dalga 2) →
  S45 (ölçek 1:10, faz 4'ün risk kapısı) → S43-44 (feda, iki figür) →
  S15-18 (dalga 1) → S1 (kapak/hook,
  2-3 hook varyantı [HOOK §7]) → kalan akış.
```

## 📺 CHAPTER HARİTASI (YouTube)

```
0:00   Perde I — Yukarısı
4:48   Perde II — Boşluk
11:12  Perde III — Ağırlık
```

---

## 📁 ÜRETİLECEK DOSYALAR (onay sonrası, bu sırayla — TEK TEK)

```text
yatay_10_20_dk_filmler/YERCEKIMI/
├── 00_PLAN.md                    ✅ bu dosya (ADIM 1)
├── README.md                     ✅ ADIM 2: Master İncil + 120 sahne haritası
├── REFERANS_PAKETI.md            ✅ ADIM 3: sayfa tarifleri + 7 sayısal kapı
│                                    ⛔ ama 0/15 PANEL ÜRETİLDİ (seed kutuları boş)
├── SUREKLILIK_LEDGERI.md         ⚠️ AÇIK KARAR — dosya YOK. İşlevi README'nin
│                                    incillerinde duruyor (halat sayacı 3→2 ·
│                                    kask takvimi · oksijen halkası · saat).
│                                    Ya yazılır ya bu satır gerekçeyle silinir
│                                    [D74: yazılmayan dosya planda durursa
│                                    "yapıldı" sanılır].
├── MUZIK_ALTERNATIFLERI.md       ✅ 31.08 · BEŞ ALTERNATİF + ortak kap
│                                    ⭐ sub-bass ↔ telefon çelişkisi KAPANDI
│                                    (150 Hz sıkı taraf + missing fundamental)
│                                    ⚠️ seçim bekliyor — biri seçilmeden ↓ yazılmaz
├── MUZIK_VE_SES.md               ❌ seçilen yay + 960 s spotting cetveli
├── KAPAK.md                      ✅ 31.08 · İKİ ALTERNATİF (A yüz-öncelikli
│                                    lansman · B ölçek-öncelikli Plan B) +
│                                    piksel-ölçülü tipografi katmanı
│                                    ⚠️ kapaktaki İSİM açık karar (§0)
├── YERCEKIMI_QA_SPEC.md          ❌ yazım paketinin SON parçası [D117]
│                                    ⛔ BU DOSYA OLMADAN FİLM "YAZIMI TAMAM"
│                                    SAYILMAZ — ve ondan da önce D124 kapısı.
│
│   ⭐ FAZ BAŞINA KLASÖR (29.08.2026, proje sahibi kararı) — format
│   kartındaki PERDE_N/ düzeninden bilinçli sapma [D74]. Gerekçe:
│   formatın referans filmi THE_SECOND_SHIP da faz klasörü kullanıyor
│   (FAZ_01_TRANSIT/…) ve üretim/QA birimi FAZDIR: her faz kendi
│   promptunu, üretim sonrası kendi QA rubriğini ve ders dosyasını
│   aynı klasörde taşır. Perde bilgisi README'nin perde haritasında
│   durur; iki yerde tutulmaz.
│
├── FAZ_01_GOREV/FAZ_01_GOREV.md        ✅ S1-S12
├── FAZ_02_DALGA/FAZ_02_DALGA.md        ✅ S13-S24
├── FAZ_03_HALAT/FAZ_03_HALAT.md        ✅ S25-S36   ← PERDE DÖNÜŞÜ 1
├── FAZ_04_FEDA/FAZ_04_FEDA.md          ✅ S37-S48
├── FAZ_05_ISTASYON/FAZ_05_ISTASYON.md  ✅ S49-S60
├── FAZ_06_KAPSUL/FAZ_06_KAPSUL.md      ✅ S61-S72
├── FAZ_07_SES/FAZ_07_SES.md            ✅ S73-S84   ← PERDE DÖNÜŞÜ 2
├── FAZ_08_AYRILIS/FAZ_08_AYRILIS.md    ✅ S85-S96
├── FAZ_09_DUSUS/FAZ_09_DUSUS.md        ✅ S97-S108
└── FAZ_10_ZEMIN/FAZ_10_ZEMIN.md        ✅ S109-S120

   ⭐ 31.08.2026 · 120/120 SAHNE YAZILDI · 10/10 faz prompt_kontrol GO
   (0 BLOCK · 0 FIX). Eksik olan üç dosya yukarıda ❌ ile işaretli.

Üretimden SONRA her faz klasörüne eklenir (Second Ship emsali):
  FAZ_NN_QA_PROMPT.md   faza özel rubrik (12 sahne birden ölçer)
  FAZ_NN_QA_DERSLER.md  bulgular + aksiyon
  ⛔ Bu koşular T1-T4 skor tablolarına GİRMEZ [00_INDEX 10-20 dk notu].

  ✅ 31.08 · FAZ_01_QA_PROMPT.md YAZILDI (üretim F1'den başladı).
  ⭐ Emsalden ayrıldığı yer: ızgara SABİT YAZILMADI. Second Ship
     rubriği "10 saniye"yi varsayıyordu; bu rubrik STEP -1'de
     toplam süreyi 12'ye böldürüp KLİP SÜRESİNİ ÖLÇTÜRÜYOR ve
     bütün zaman kodlarını o ölçümden türetiyor [D124].
     → Bu koşu aynı zamanda yukarıdaki `KLİP SÜRESİ = ____`
       satırının cevabını üretir.

  ✅ 01.09 · FAZ_02_QA_PROMPT.md YAZILDI — ⭐ İKİ MÜHÜRLÜ GEÇİŞ
     F1'in ③ kimlik kapısı UNATTRIBUTED düştü: rubrik denetçiye her
     tarifi önden verdiği için rapordaki "çapa"lar YANKI çıktı.
     F2 rubriği ikiye bölündü ve İKİ AYRI SOHBETTE koşulur:
       A · KÖR   — belge yok, katalog yok. Denetçi pasaportu KENDİ
                   gözüyle yazar → yankısız ÇAPA. Ayrıca karışık
                   klipleri kendi kanıtıyla SIRALAR.
       B · KATALOG — 12 girdilik kadraj kataloğu + kilitler + skor.
     ⭐ Karışık sıra artık engel değil, ÖLÇÜ: sıra skoru = doğru
       yerleştirilen klip / 12. Yanlış yerleştirme = görsel zincirin
       koptuğu adres; sonraki fazlara müdahale bu sayıdan çıkar.
     ⛔ A ve B aynı sohbette koşulursa belgenin tüm değeri sıfırlanır.

  ✅ 01.09 · FAZ_03_QA_PROMPT.md YAZILDI — aynı iki geçiş, F3'e göre ayarlı
     ⛔ VİZÖR BİÇİMİ ARTIK PUANLANMIYOR (proje sahibi "geri dönüş yok"
        kararı; film 24 sahnedir ve 24'ünde kubbe var). Yerine OPTİK
        sert puanlanıyor — berrak · tonsuz · aynasız · yüz okunur;
        kilidin tutan yarısı buydu.
     Faza özgü dört yeni ölçüt:
       · İKİ hareketli plan (C pull-back · L push-in) — F2'de bir vardı
       · GÜNEŞ TARAFI BÖLÜNÜYOR: B ve E'de üst SOL, kalan onda üst SAĞ
       · HALAT FİZİĞİ: gergin = ölü düz · gevşek = yavaş geniş salınım ·
         çekiş omuz→kalça→bacak · ⭐ gergin hatta biri hızlanınca İKİSİ de
       · İKİ SAYAÇ SAHNE İÇİNDE DÜŞÜYOR (F: halka 4→3 · J: şerit 1→0) —
         düşüşün EKRANDA olması ayrı kontrol maddesi [GOZLEM ADAY-3'ün
         çözümü zaten F3'ün tasarımında]
     ⭐ I girdisi için özel tuzak uyarısı: gök kayar, gövde SABİT durur —
        bu kamera hareketi DEĞİLDİR (istasyonun 6°/s dönüşü, Çehov 7).
     ⭐ Sırt ünitesi F2'de tek klipteydi, burada YEDİ → "aynı nesne mi"
        ilk kez ölçülebiliyor. İstasyon yedi ölçekte, referans yok.
```

---

## ✅ ADIM 1 CHECKLIST + ÜRETİM ÖNCESİ KONTROL ÖZETİ

```
☑ Faz sayısı kilitlendi: 10 (3-4-3) · 8 s · 16:00
☑ Perde dağılımı kurallara uygun (II en uzun · I en uzun değil)
☑ Kulvar bilinçli: sert uzay gerilimi (novum yerine DURUM — yazılı)
☑ Önerme üç kapıdan geçti (③ şartlı — paketlemede ikinci koşu)
☑ 2 perde dönüşü net (eşik = S36 · geri dönüşsüzlük = S84)
☑ İMZA ÇEKİM tek sahnede (S102) · KAPAK ANI 0-10 s bandında (S1)
☑ Çehov zinciri 7 halka, hepsi ateşleniyor
☑ Kılavuz sapmaları yazılı ve gerekçeli (6 sapma, §FORMAT)
☑ Feda fiziği Gravity'nin ölçülmüş ihlalini KOPYALAMIYOR (merkezkaç)

ÜRETİM ÖNCESİ KONTROL — YERÇEKİMİ            tarih: 28.08.2026
A1 ☑ "no text" ↔ ekran içeriği çelişkisi YOK (halka rakamsız; sayılar
     yalnız MACHINE seste)
A2 ☑ 120 sahne = 10 faz × 12 (blok sayımı README+fazlarda ikinci kez)
A3 ☑ 120 × 8 s = 960 s = 16:00
A4 ☑ yasaklı tip taraması: biniş-iniş kadraj dışı (airlock girişi S48
     İÇERİDEN, kapı hareketi kadraj dışı — D69) · loş mekâna giriş
     S49'da ışık motivasyonu yazılacak (README) · ayna/yansıtıcı yüzey
     önünde tek karakter sahnesi YOK · novum türetilmiş fenomen DEĞİL ·
     jenerik/başlık kartı 0
B1 ☑ doruk anı sahne İÇİNDE: dalga çarpması S94'ün, ateşleme S96'nın,
     yerçekimi dönüşü S102'nin gövdesinde tarif edilecek
B2 ☑ bedelli seçim S84 · kayıp S85'te GÖRÜLÜYOR (sessiz telsiz)
B3 ☑ TEMA: FEDAKÂRLIK · motif sahneleri S30 · S43 · S84 · S117
B4 ☑ kurulum dizisi 120/120 sahnede yazıldı (README faz tabloları) ve
     betik 10/10 faz dosyasında koşuldu: kurulum sayısı bandı ✅ ·
     açı TİPİ ≥3 ✅ · ardışık çift ≥1 kademe + ≥45° ✅  [31.08.2026]
C  ☑ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı=0 ·
     canlı=0) + oksijen kadansı + enkaz saati
D  ☑ risk sayımı: 7/12 tetiklendi → çekirdek 5/12 TAM EŞİK; malzeme
     azaltımı uygulandı (su 0 · ateş 0 · canlı 0 · patlama 0)
E  ◻ QA SPEC BLOĞU ayrı dosyaya yazılacak (YERCEKIMI_QA_SPEC.md —
     yazım paketinin son parçası; replik/doruk saatleri formülle)

☑ KULLANICI ONAYI alındı (28.08.2026) → README → REFERANS_PAKETI →
  FAZ_01 … FAZ_10 tek tek yazıldı, hepsi GO (31.08.2026).

⛔ SIRADAKİ ADIM ARTIK ONAY DEĞİL, ÖLÇÜM:
  ① D124 kapısı  → yukarıdaki `KLİP SÜRESİ = ____` ffprobe ile dolar
  ② MUZIK_VE_SES.md   ③ KAPAK.md   ④ YERCEKIMI_QA_SPEC.md  [D117]
  ⑤ REFERANS_PAKETI'nin 15 paneli üretilir, 7 sayısal kapıdan geçer
  ⛔ ①-④ bitmeden HİÇBİR FİLM KARESİ üretilmez.
```
