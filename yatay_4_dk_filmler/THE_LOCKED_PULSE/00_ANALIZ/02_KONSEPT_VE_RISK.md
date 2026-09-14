# 🧠 THE_LOCKED_PULSE — KONSEPT VE RİSK

> Girdi: sahibin talebi + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi — "Mevcut konsept korunsun" (12.09.2026 taslağının konsepti:
            dönen halka istasyonunda soğutucu kaçağı · otomasyon altı kriyo kapsülünü
            canlı tutmak için halkayı hızlandırır · mühendisin sağ bileği kilitlenir)
   AI seçmedi → gerekçe satırı yok. Kayıt: sayaç 🎭 TEMA DAĞILIMI'nda İNSAN-MAKİNE 2
   ile §3 sekizlisinin EN AZ kullanılan teması — konsept zaten deponun eksik tarafında.
② FORMAT:   yatay 3-5 dk        → kart §2.3 · bölüm sayısı 2 (BOLUM_1 13 · BOLUM_2 12)
③ SAHNE:    25                  → formatın varsayılanı (9 s hook + 24 × 10 s = 249 s = 4:09)
   Bandın İÇİNDE — D74 gerekçesi gerekmez.
④ REFERANS PAKETİ: YAZILSIN (sahip) → KAPI 0: sayfası ONAYLI ve seed'i yazılı olmayan
   varlığın geçtiği sahne üretilmez [D168]. §5b tablosu bilgi için yine dolduruldu.
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "\"\"THE_LOCKED_PULSE\"\" filmini /yeni-film ile yeniden hazırla"
       + soru ①: "Mevcut konsept korunsun"
REPLİK: var — MAKİNE anonsu (halka otomasyonu), insan repliği 0
        → AYRI kapı zinciri: SES_VE_DIYALOG §1a-§2a + DIALOGUE_CRITIQUE_PROMPT (Kart P 2b)
        + DEĞİŞ-TOKUŞ tablosu (03_SIRALAMA §5) + ㉓ replik envanteri
```

**Talep fizikle çelişiyorsa yeniden tanımlanır ve sapma AÇIKÇA yazılır [D74].**

| sahibin isteği / eski taslağın satırı | fiziksel-üretim sorunu | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| eski PLAN: "hiper-g 1,8 g … bileği ezer, sinir hasarı, ellerinin kontrolünü kaybeder" | 1,8 g'de insan ayakta çalışamaz; 'ezme/sinir hasarı' politika sözlüğü (PK+PB, red defteri 13/15); yaralanma 0 kare kuralı | halka 2,0 → 4,0 RPM (0,25 → 1,00 g); bilek EZİLMEZ, port yakasının basınç KİLİDİ bilek halkasının üstüne KAPANIR (mekanik durum); bedel = eldiveni orada bırakmak | POLITIKA §2 · D123/D128 · KILAVUZ §3.7 (1 g = 4 RPM 56 m) |
| eski PLAN: panelde "6 CREW CRYO ACTIVE" dijital barlar | ekran metni 0,0 s kuralı [D13/D50]; sayaç metinle okunmadı (D78 ×5) | duvarda 7 yuvalı yuvarlak lamba dizisi: 6 yanık + 1 sönük; metin 0 | D13 · D50 · D78 · T14 |
| eski PLAN: "dönen istasyon gövdesi × bilek kilit mekanizması → hiper-g baskısı" taşıyıcı | taşıyıcı SOMUT nesne+jest değil; tek kare testi başka nesneyle (PAYLOAD D157) | taşıyıcı = **düşen anahtar × bırakma jesti → yana iner**; ikincil: salınan kayış (periyot) · pencerede yıldız süpürmesi | ONERME §4 · D157 · D127 |
| önceki okuma turunda yazılan "kayış AÇISI dikleşir" | duran bir kayış dönen halkada her hızda RADYAL sarkar; açı yalnız ivmelenme anında ~1° oynar → görünmez [D90] | kayış açısı DEĞİL, salınım PERİYODU: T = 2π√(L/a) → 4,0 s (0,25 g) · 2,7 s (0,56 g) · 2,0 s (1,00 g) | D90 · D127 · §3.7 (a = ω²R) |
| eski taslak: karakter adı "Lars" promptlarda | özel ad prompta girmez [D34/D45]; TUR 14 kopya sınırı | "the engineer" | D34 · D45 |
| eski taslak: 21 sahne / 3:29 | format kartı 25 sahne / 4:09; bant dışı gerekçesizdi | 25 sahne (soru ③) | §2.3 |
| eski taslak: hub 0 g sahnesi + kriyo odası + dış | risk kartı sayısı eşiğin üstünde (bkz. §5); D200 iki g; kapsüller = 6 insan silüeti (klon/anatomi) | hub 0 g YOK · kriyo kapsülleri KADRAJ DIŞI (yalnız lambaları) · dış sahne TEK (S13, insansız) | 02_RISK_KARTLARI 5+ kuralı |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 3-5 dk                          → §2.3 kartı
ORTAM:         §3.7 VAKUM + DÖNME YERÇEKİMİ (24 iç sahne — halka koridoru, basınçlı)
               + §3.1 VAKUM (yalnız S13 dış Overview, insansız)
               ⛔ §3.10 basınçlı iç hacim kartı KULLANILMAZ — hub 0 g sahnesi yok;
                  yerel dikey FİZİKSEL (dönme g), renkle kurulan 'yukarı' gerekmez
               → tetiklediği zorunlu satırlar: a = ω²R fizik defteri · bırakılan şey YANA
                 iner (süre+mesafe) · halka içinde oklüzyon yok · üst bantta ikinci güverte
                 YOK ("the corridor ceiling is a single arched panel") · 'düşen şey' yönü
                 film boyu TEK ekran yönü (ekran-SOL) · halka içinde PENCERE YOK (lomboz A/C kadrajlarına da düşerdi, T5 düz-plaka riski) — yıldız yalnız S13 dış ·
                 D200 tek karede tek g · S13'te YÖRÜNGE negatif bloğu (kısa)
TÜR:           bilimkurgu · dal: SERT UZAY GERİLİMİ (gerçek mekanik) → §4.1
KLİP SÜRESİ:   10,0 s  ⛔ ARAÇTAN ÖLÇÜLÜR [D124] — PLAN'a "KLİP SÜRESİ = ____ (ffprobe,
               ilk klipten sonra doldur)" satırı; 10,0 varsayımı emsal ölçümlerden
               (COUNTED_TURN 10,0 · IRON SLOPE 10,005)
SAHNE SAYISI:  25    RUNTIME: 249,0 s = 9 + 24 × 10
BÖLÜM SAYISI:  2     (§2.0 — BOLUM_1 S0-S12 · BOLUM_2 S13-S24)
```

### 2b. ⚙️ FİZİK DEFTERİ — metre BURADA ve SPEC'te, promptta GÖVDE BOYU [D138]

```
HALKA:         yarıçap R = 56,0 m (1 g = 4,0 RPM — §3.7 tablosu) · koridor iç kesit
               2,2 × 2,2 m (≈ 1,2 H · 1 H = 1,90 m kasklı ayakta)
DÖNÜŞ PROFİLİ (monotonik ↑, yalnız sahne SINIRINDA değişir — NOVUM DURUMU sütunu):
   S0-S1   2,0 RPM   ω 0,209 rad/s   a 2,46 m/s²   0,25 g
   S2-S5   2,5 RPM   ω 0,262         a 3,84        0,39 g
   S6-S8   3,0 RPM   ω 0,314         a 5,53        0,56 g
   S9-S12  3,5 RPM   ω 0,367         a 7,52        0,77 g
   S13-S24 4,0 RPM   ω 0,419         a 9,83        1,00 g   (SPIN HOLD)
YILDIZ SÜPÜRMESİ yalnız S13 dış (kamera hub'a kilitli, radyal bakış): 4,0 RPM = 24 °/s,
   yıldızlar 74°'lik kadrajı 3,1 s'de geçer, tek yön · halka içinde pencere YOK (T5 düz-plaka
   paralaks riski + KART 6b) → iç sahnelerde hız kanıtı: kayış periyodu · düşüş süresi · adım
DÜŞÜŞ (Coriolis, yana sapma = ⅓·(2h)^1,5/√R — HIZDAN BAĞIMSIZ, süre hıza bağlı):
   S2  anahtar  h 0,90 m · 2,5 RPM → t 0,68 s · yana 0,11 m (bir avuç genişliği) ekran-SOL
   S15 levye    h 0,75 m · 4,0 RPM → t 0,39 s · yana 0,08 m ekran-SOL
   ⛔ SINIR: kural yalnız SERBEST BIRAKILAN nesneye; duran kayış radyal sarkar (eğik değil),
      zemindeki nesne kaymaz, yürüyen adam savrulmaz (2ωv ≤ 0,84 m/s² → yalnız adım genişliği)
KAYIŞ (L 1,0 m, üstten klipsli, salınım): T = 2π√(L/a) → 4,0 s (S0) · 3,2 s (S2-S5) ·
   2,7 s (S6-S8) · 2,3 s (S9-S12) · 2,0 s (S13-S24)
ALARM LAMBASI PERİYODU (IŞIK TAKVİMİ, D193): S0-S5 2,0 s · S6-S12 1,5 s · S13-S24 1,0 s
ADIM KADANSI (10 s yürüyüş): S5 8 adım (0,39 g, uzun hafif adım) · S6/S7 7 adım
SOĞUTUCU JETİ: port yakasından (Ø 0,15 m, zemin +0,75 m) düz beyaz buhar jeti, uzunluk
   0,20 m (bir karış), S3 tam · S8 yarı (0,10 m) · S10 biter (klip içinde, 6,0 s'de)
LAMBA DİZİSİ: 7 yuva × Ø 0,12 m, 0,20 m aralık, vana çarkının üstünde 1,40 m yükseklik;
   S0-S23: 6 yanık + 1 sönük (sağ uç) · S24: 7 yanık
UZAY GİYSİSİ TEK MÜHÜR: sağ bilek halkası Ø 0,11 m brushed steel = port yakası standardı
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM TİPİ:          FİZİKSEL YASA (icat edilmedi — §3.7'nin kendi kuralı; HEAVY SIDE ·
                     COUNTED TURN emsali). Kulvar SERT: bu bir DURUM sınıfıdır ve ONERME
                     kapısından yasa tipi olarak geçer; olay örgüsünü ZORUNLU kılar
                     (basınç ↓ → hız ↑ → ağırlık ↑ → kilit).
NOVUM:               Bu halkada ağırlık dönüş hızıdır: makine basıncı korumak için hızı
                     artırınca her şey ağırlaşır, ve bırakılan hiçbir şey düz düşmez.
NOVUM TAŞIYICISI:    <steel wrench> × <eldivenin bırakması> → <alet düz değil YANA iner,
                     ve hız arttıkça daha kısa sürede iner>
                     ikincil taşıyıcılar: <webbing strap> × <salınım> → <periyot kısalır>;
                     <star field> × <S13 dış bakış> → <yıldızlar kadrajı üç saniyede geçer>
① TEK KARE:          ✅ "A steel wrench released at chest height beside the valve wheel is
                     already on the deck a palm's width to the LEFT of the point it left
                     the glove, while the strap beside it swings as one straight line and
                     six of seven lamps burn above the wheel."  (taşıyıcı adı: wrench [D157])
② KİNETİK BAĞIMSIZLIK: ✅ kural replik/metin olmadan kanıtlanır — S2 anahtar · S15 levye
                     · S0↔S24 kayış periyodu · S13 yıldız süpürmesi · S5→S7 adım kadansı
③ BAŞLIK ŞEMASI:     ✅ "THE LOCKED PULSE" (3 kelime): LOCKED = bilek halkası/port yakası ·
                     PULSE = alarm nabzı + halkanın devri — nereye bakılacağını söyler
MAYA:                ihlal sayısı 1 (dönme g); bilek kilidi ihlal DEĞİL, sonucudur
KURAL TEKRARI:       kurulum S0-S2 (kayış + anahtar) · doğrulama S15 FARKLI nesnede
                     (levye, 1 g) + S13 (yıldız, dış) · sonuç S20-S24 (bedel) — ≥3 sahne ≥2 nesne
HOOK'UN SAKLADIĞI:   novumun kendisi değil SEBEBİ (kriyo döngüsü hidrostatik başla çalışır;
                     basınç düşünce makine başı hızla telafi eder) — S1 anonsu açar
⛔ Üçü de ✅ → KONSEPT KABUL, sıralama yazılır.
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — İNSAN-MAKİNE        (sayaç 🎭: 2 kullanım — sekizlinin en az kullanılanı;
                                    FEDAKÂRLIK 4 kullanım ve TAKAS kalıbı moratoryumu → elendi)
▸ tanım cümlesi — "İnsan-makine sınırı, makinenin doğru hesabının insanı bir parça
                   olarak saydığı yerdir."   (TANIM; novum kelimesi yok; TAKAS kalıbı değil)
▸ depoda kaç kez kullanıldı — 2   (bash sayac.sh · TEMA DAĞILIMI · 13.09.2026)
▸ motif kanalları — NESNE: bilek halkası ↔ port yakası (aynı standart parça) ·
                    KİNESİK: iki parmakla iki vuruş alışkanlığı vanadan KENDİ bileğine geçer ·
                    IŞIK/SES: alarm nabzı (staccato, sentetik) ↔ nefes (organik, sürekli)
▸ sahne indeksi (≥3) — S2 (vuruş alışkanlığı + 7 yuva 6 yanık) · S10 (kol yakaya girer:
                    insan eli fitting olur) · S12 (kilit + "latch engaged" anonsu) ·
                    S18 ("loop pressure holding" — makine onu parça saydı) · S22 (vuruş
                    KENDİ bileğine — kırılma) · S24 (7. lamba yanık: makine defteri +1)
▸ STATED vs ENACTED — makine anonsları 'stable/holding/nominal' der (STATED),
                    beden öder (ENACTED); ikisi çelişir — bilinçli
▸ tema-final — İNSAN-MAKİNE → görsel İFŞA: son karede kazanan makinenin defteridir
                    (7 lamba), insan zeminde tek eldivenli
```

### 4b. 🧩 MOTİF TABLOSU (TEMA_ANALIZ_PROMPT mantığı)

| nesne (literal) | nasıl vurgulanır | READING |
|---|---|---|
| salınan kayış (webbing strap) | S0 ve S24 aynı kadraj, tek değişken periyot | halkanın nabzı görünür hâlde — "pulse" |
| 7 yuvalı lamba dizisi | S0-S23 6 yanık + 1 sönük, hiç bakılmaz; S24 7 yanık | makinenin defteri; boş yuva ONUN için |
| port yakası (Ø bilek halkası) | S3 kenarda jet; S10 kol girer; S12 kilit; S22-S24 eldiven içinde | insan parçası → makine parçası |
| fren çarkı (sarı-siyah bant) | S0 kadraj kenarı (Çehov kurulumu); S16 bakış; S17/S20 el yarım yolda | REDDEDİLEN nesne kadrajda kalır |
| kırmızı alarm lambası | periyodu üç kademede kısalır (2,0 → 1,5 → 1,0 s) | makinenin hızlanan kalbi |

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

> ⛔ **PLAN YAZILMADAN ÖNCE.** 5+ risk çıkıyorsa malzeme AZALTILIR —
> prompt iyileştirmek bu deponun ölçtüğü kadarıyla işe yaramıyor.

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 SU/SIVI | ✗ | sıvı 0 kare; soğutucu BUHAR jeti (gaz), kırağı/damla yok | — | 0 |
| 2 CANLI | ✗ | insan dışı canlı yok | — | 0 |
| 3 KASK/VİZÖR/EKİPMAN | ✓ | kask 25/25, vizör berrak, tek mühür; biçim kilidi metinle tutulmuyor (D146 ×4) | HELMET STATE SCHEDULE 25/25 kapalı · eldiven durumu tek geçiş S21\|S22 · REFERANS PAKETİ RK1 (KAPI 0) | 🟠 |
| 4 İKİNCİ FİGÜR | ✓ | her filmde; loş iç mekân klon sıcak noktası | kriyo kapsülleri KADRAJ DIŞI (6 insan silüeti çıkarıldı) · yansıtıcı yüzey 0 · biniş/kapı 0 · "exactly one human figure" | 🟡 |
| 5 EKRAN/SAYAÇ/METİN | ✓ | sayaç var (lamba dizisi · alarm) | ekran/kadran/yazı 0; sayaç FİZİKSEL lamba (7 yuva); NEGATIVE metin cümlesi tam kapsam ("on any display, surface, patch or sign") | 🟡 |
| 6 PARÇACIK/TOZ | ✓ | soğutucu buhar jeti | yalnız 3 sahne (S3 · S8 · S10), düz koni, uzunluk bir karış, sayıyla; toz/duman/kıvılcım 0 | 🟡 |
| 6b KATMANLI DÜNYA | ✓ | g sahne sahne değişir + 1 dış vakum sahnesi | NOVUM DURUMU sütunu monotonik; hub 0 g ÇIKARILDI; S13 tek ve insansız; D200 | 🟡 |
| 7 DİYALOG | ✓ | 6 MACHINE repliği | kadraj dışı hoparlör · insan repliği 0 · sessiz üretim + post · ㉓ | 🟡 |
| 8 KAMERA | ✓ (iyi haber) | lockoff 25/25 | "zero camera movement" cümle başı+sonu; kurulum 10 | 🟢 |
| 9 IŞIK MIKNATISI | ✓ | kırmızı alarm + tavan paneli, hedef vana istasyonu | kamera HEDEFTE (D · M kurulumları yakada/çarkta); en parlak kaynak mühendisin yöneldiği tarafta; dört kanal 03'te | 🟠 |
| 10 İNSANSIZ + UZUN NEGATİF | ✓ | S13 dış | tek sahne; NEGATIVE kısa (yörünge bloğu 3 cümle); insan yokluğu pozitif kadrajla | 🟡 |
| 11 DEĞİŞKEN SÜRE / SAHNE İÇİ KESME | ✗ | sabit 10 s, 0 kesme | KLİP SÜRESİ ffprobe [D124] | 0 |
| 12 POLİTİKA | ✓ | bilek kilidi (imza ①) · kırmızı ton + CU (⑦) · kask (⑥) | tek bilek YANDAN, kamera yaka hizasında, kask+omuz kadrajda; kırmızı KAYNAĞA bağlı, gri panel referansı; sözlük temiz; iki yenilgi = kamera | 🟠 |
| 13 YAPI ÖLÇEĞİ / TEKRAR EDEN BİRİM | ✓ | halka + spoke + dış S13; raf/ızgara tekrar eden birim | ANATOMİ KARTI: halka 1 · spoke 4 · hub 1 · lamba 7 · pencere 0 · raf bloğu duvar başına 4; metre SPEC'te, gövde boyu promptta; "hundreds of" 0 | 🟡 |

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR 🆕 [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  NOVUM EKRANA GELMİYOR — bırakılan alet düz düşer ya da süzülür
                  (IRON SLOPE D127: 12/12 promptta ivme yazılıyken 0,15 m/s süzüldü)
POZİTİF BİÇİMİ:   S2: "the wrench leaves the glove at chest height and is on the deck
                  before the hand closes — well under one second — a palm's width to the
                  LEFT of the point it was released, and it stays where it lands"
                  S15: "the steel bar slips and is on the deck in less than half a second,
                  a palm's width to the LEFT, and stays"
                  SAYI: süre < 1,0 s (S2) · < 0,5 s (S15) · sapma 1 avuç (≈ 0,11 / 0,08 m) ·
                  yön ekran-SOL film boyu tek · nesne boyu 0,30 m (anahtar) / 0,50 m (levye)
                  ⑥ FİZİK mod D kilidi: t ± %20 · sapma ≥ 0,05 m · yön SOL
                  ⛔ İPTAL KAPISI: S2 üretim testinde anahtar düz düşer/süzülür/sağa iner →
                     film ÜRETİLMEZ (üç deneme, üçüncüde PROB_KOSUSU)
```

```
TETİKLENEN RİSK:  10 / 14
EŞİK:             5
✅ EŞİĞİN ÜSTÜNDE: hangi malzeme çıkarıldı →
   · hub 0 g sahnesi (§3.10 kartı, D200 iki g, metin riski en yüksek)      ÇIKTI
   · kriyo kapsül odası (6 insan silüeti — klon/anatomi/buz erimesi K13)     KADRAJ DIŞI
   · ikinci insan / telsizde cevap veren ses                                 0
   · ekran/gösterge/yazı (eski "6 CREW CRYO ACTIVE")                         0 → lamba
   · dış sahneler (eski taslak 2+)                                            TEK (S13)
   · jet sahneleri                                                            3
   · sıvı · ateş · kıvılcım · toz                                             0 kare
   · kask çıkarma · biniş/iniş · kapı geçişi                                  0 kare
   kalan 10 kartın 5'i tasarımla ≤🟡; 🟠 olan üçü (kask biçimi · ışık mıknatısı · politika)
   ölçülmüş çözümle taşınıyor: REFERANS PAKETİ + kamera hedefte + kamera-yandan kompozisyon.
   Kabul gerekçesi: bu üçü çıkarılamaz — kask ve bilek filmin konusudur.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — sahip "YAZILSIN" dedi; tablo bilgi için

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✓ | RK1 mühendis (kask düz pane + çerçeve · sırt pozitif · sağ bilek halkası) — 24/25 sahne |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✓ | vizör (D146 ×4) · sırt (D139 ×3) → RK1 arka + kask makro |
| T3 | oranı sözle yazılamayan nesne | ✓ | halka koridoru kesiti + spoke (RI1) · dış halka/spoke/hub (RX) |
| T4 | insan dışı canlı | ✗ | — |
| T5 | tekrar eden insan dışı olay | ✓ | soğutucu jeti (RO) S3 · S8 · S10 |
| T6 | bir varlık tekrar tekrar dönüyor | ✓ | vana istasyonu: çark + port yakası + fren çarkı + lamba dizisi (RP) — 20/25 sahne |

```
KARAR: YAZILIR  (sahip kararı + T1/T2/T3/T5/T6 doğru)
⛔ KAPI 0: RK1 · RI1 · RP · RO onaylı ve seed'li olmadan hiçbir sahne üretilmez [D168];
   RX (dış) yalnız S13'ü kilitler.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S12 · 123,0 s (port yakasının kilidi bilek halkasının üstüne kapanır)
                     ve S22 · 224,0 s (mühür açılır, çıplak el eldivenden çıkar)
NÖTR TARİFİ:         "his right forearm rests in the port collar, the wrist ring seated in
                     it; the collar's outer ring turns a quarter turn and closes over the
                     wrist ring with a single click; the glove stays seated; his shoulder
                     settles" — kamera yaka hizasında YANDAN (kurulum D), kask ve omuz
                     kadrajda, tek bilek, tepeden makro YOK, ikinci ön kol YOK
                     S22: "his left glove taps the right wrist ring twice with two fingers,
                     turns it a quarter turn; the ring parts with a click; the bare right
                     hand draws back out of the glove and the glove stays seated in the
                     collar" — çıkarma fiili yok, eldiven yerinde
SÖZLÜK (0 geçiş):    crush · trapped · injury · pain · blood · nerve · stuck · danger ·
                     emergency · failure · warning · hammer · strike · dead · body · frozen
İMZA KAÇINMALARI:    ① tek bilek yandan, gövde kadrajda · ⑥ vizör berrak, yüz okunur ·
                     ⑦ kırmızı kaynağa bağlı ("a red lamp above the bay"), CU'larda gri panel
                     referansı ve tavan paneli nötr ışığı kadrajda kalır
ANLAM MALİYETİ:      ÖNLEM: ezilme/acı yazılmaz → MALİYET: bedelin şiddeti okunmayabilir →
                     TELAFİ: alet tepkisi (levye elden kayar S15) + makine anonsu ("latch
                     engaged" S12, "holding" S18) + kalıntı duruş (S21-S24)
İKİ YENİLGİ KURALI:  aynı kadraja 3. sözcük denemesi yok — 2 red → kamera D'den C'ye taşınır
                     (yaka kadrajın üçte birine iner, mühendis MS), defter satırı + MOTOR
```

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   soğutucu port sızıntısını kapatıp altı kriyo kapsülünü soğuk tutmak — vardiya işi,
         film başlamadan var (S0'da eli çoktan çarkta)
ENGEL:   otomasyon döngü basıncını korumak için halkayı hızlandırır (ağırlık ↑, adım/kol
         ağırlaşır); port yakasının basınç kilidi, kolunu soktuğu anda bilek halkasına kapanır
BEDEL:   sağ eldivenini port yakasında BIRAKIR — S22 (mühürü açar, çıplak eli çıkar; eldiven
         yakayı tıkayan parça olarak kalır; kalıcı iz S23-S24: tek eldiven, çıplak el göğüste)
         ⭐ ASIL KAPI: sahne numaralı — S22 · 224,0 s
MUHATAP: ortamın KALICI değişen parçası — halka hızı (4,0 RPM'de TUTULUR, geri inmez) +
         lamba dizisi (6 → 7 yanık); ikisi de son karede (S24) görünür
AYRILIK: —  (tek insan; ikinci insan kadrajda 0, seste 0 — IKI_KISI kartı gerekmez, PLAN'a
         tek satır gerekçe)
```

Gerekçe: "umursamadım" tepkisinin üç belgelenmiş sebebi — **istek yok · bedel
yok · muhatap yok** [`04_ARASTIRMA_BULGULARI.md` TUR 4].

## 8. 🪪 KARAKTER KARTI — B5'ten hemen sonra (`KARAKTER_KARTI_VE_DAVRANIS` §1 · 11.09.2026)

> Bible GÖRÜNÜŞÜ, kart DAVRANIŞI kilitler — kart PROMPTA GİRMEZ. Başlık rol etiketi, özel ad yok.

| satır | içerik | sahne no |
|---|---|---|
| ROL | halka soğutma hattı bakım mühendisi (tek amber şerit sol pazu+uyluk · elinde çark anahtarı/levye) | S0 · S6 |
| İSTEK | port sızıntısını kapatıp altı kapsülü soğuk tutmak | S0-S12 |
| BASKI TEPKİSİ | **KONTROL EDER** (tek kelime, sabit — panik 0 kare, her deneme ölçülü) | S3 · S14 · S20 |
| ALIŞKANLIK | "before he touches any wheel, his right glove taps the rim twice with two fingers" — BİREBİR cümle ≥3 tekrar: S2 (çark) · S7 (çark, levye takmadan) · S10 (yaka kenarı) · **KIRILMA S22**: iki vuruş KENDİ sağ bilek halkasına | S2 · S7 · S10 · S22 |
| SINIR | halkayı frenlemez (fren çarkı el mesafesinde: S17 · S20 el yarım yolda durur) | S17 · S20 |
| ZAAF | yükü hep SAĞ tarafına alır — sağ omuz önde, sağ el önce: bu yüzden sağ bileği yakaya girer (görünür iz ≥2 sahne) | S2 · S10 · S11 · S16 |
| TEL (kriz işareti) | nefes verişini tutar — omuzlar kalkar ve 2 s asılı kalır, sonra iner (eldiven kontrolü YASAK) | S4 · S17 · S20 |
| İLK ↔ SON | S0: diz çökmüş, iki eldivenli el çarkta, sırt dik ↔ S24: zeminde oturmuş, tek eldiven, çıplak sağ el göğüs plakasında, sırt duvarda — adlandırılabilir fark: eldiven sayısı 2 → 1, duruş dik → oturmuş | S0 · S24 |

### 8b. ⚖️ KARAR MİMARİSİ — dört satır (§3)

```
REDDEDİLEN NESNE:   fren çarkı — S0 kadraj kenarında kurulur, S16'da bakılır, S17 el yarım
                    yolda, S20 el bir avuç mesafede durur ve geri döner; S21-S24'te KADRAJDA
                    KALIR (A ve C kurulumlarında sağ altta)
BAŞARISIZ DENEME:   seçimden ÖNCE 4 deneme, sonucu görünür: S3 çark çeyrek dönüp geri teper ·
                    S4 iki elle çekiş yarım kalır · S14 kolu çeker, halka yerinde · S15 levye
                    kayar ve yana iner — her deneme iz bırakır (sağ omuz düşer, ZAAF)
BEDEL PENCERESİ:    seçimin (S20) bedeli S22'de aynı klipte ilk 3 s'de görünür: eldiven yakada,
                    çıplak el eldivenden çıkar (224,0 s); S12 kilidi ise ENGELİN bedeli
HOBSON SATIRI:      iki seçenek de gerçek: fren = eli serbest + kapsüller ısınır (lambalar
                    sönecek) · frenlememek = kolu yakada kalır → üçüncü yol: mührü açmak =
                    eldiveni kaybetmek. Kolay çıkış yok.
```

### 8c. 🧬 DAVRANIŞ ŞERİDİ ve TEMPO — 03'e taşınır

```
ŞERİT (25):  G R G D T G G G G R G G R - D D S T R S K R B R B
             G 8 · R 6 · D 3 · T 2 · S 2 · K 1 · B 2 · - 1 (S13 insansız)
             K'dan önce D/T ✓ (S15 D · S17 T) · K'dan sonra B/R ✓ (S21 R) · son B ≠ ilk G ✓
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅
☑ risk sayımı yazıldı (10/14) ve eşik kararı verildi (malzeme 8 kalemde azaltıldı)
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S22 · 224,0 s)
☑ KARAKTER KARTI 8 satır + sahne no · KARAR MİMARİSİ 4 satır
→ 03_SAHNE_SIRALAMASI.md yazılabilir
```
