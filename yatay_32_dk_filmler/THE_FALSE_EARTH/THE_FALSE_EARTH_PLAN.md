# 🎬 THE_FALSE_EARTH — PLAN

> **Bu dosyada PROMPT YOKTUR.** `### 📸 GÖRSEL PROMPT` / `### 🎥 VİDEO PROMPT`
> başlıkları YALNIZ bölüm dosyalarında bulunur. Sebep: kapı betiği promptu
> başlıktan sayar; plana konan örnek bir prompt sahne dizisine karışır.
>
> Bu dosya SONUCU taşır. Hesap `00_ANALIZ/`dedir: sıra ve iskelet
> `03_SAHNE_SIRALAMASI.md`, klip başına ayrıntı
> `00_ANALIZ/05_SAHNE_CALISMALARI/00_SAHNE_TABLOSU.md`'nin 192 satırında.
> ⛔ İki yerde tekrar edilen hiçbir sayı yoktur.

```
FORMAT:        yatay 32 dk → §2.9 (192 klip × 10 s · 16 bölüm · QA birimi 8 PART + TAM FİLM · kurgu kapısı ±0 s)
               + §2.0b ÇOK KLİPLİ SAHNE — bu rejimin İLK filmi (sahip kararı 22.09.2026)
               ⚠️ PART GRID SPEC A'da dolu: 8 PART, her biri iki bölüm dosyası
ORTAM:         ÜÇ KART BİRDEN, ve asla aynı kadrajda değil [D200]
               §3.3  DÜNYA ATMOSFERİ   gezegen yüzeyi · S06-S10 · S26-S34
               §3.1  VAKUM              uzay · S01 · S02 · S05 · S26 · S32-S34 · S38 · S44 · S46 · S50
               §3.10 BASINÇLI İÇ HACİM  gemi içi · S03 · S04 · S35-S43 · S47-S49
               ⚠️ §3.3'ün depoda referans filmi YOK — bu ilk
TÜR:           bilimkurgu · dal: kozmik gizem + psikolojik gerilim (§4.1)
KLİP SÜRESİ:   ⬜ ARAÇTAN ÖLÇÜLECEK [D124] — üretim defterinin İLK satırı:
               ffprobe -v error -show_entries format=duration -of csv=p=0 <test klibi>
               ⛔ Yazım tam 10,000 s varsayar. Ölçüm saparsa bu dosyanın RUNTIME
                 satırı yeniden hesaplanır; KLİP SAYISI DEĞİŞMEZ.
SAHNE SAYISI:  50 sahne · 192 klip
RUNTIME:       1920,0 s = 32:00,0   (hook 192'nin içinde · title card 0,0 s)
BÖLÜM SAYISI:  16 (formattan gelir — §2.0)
LOGLINE:       Bir kurtarma pilotu kardeşinin çağrısını dokuz yıl sonra duyar, sesin
               geldiği gezegene iner ve onu geri götürecek tek şeyin istenen şey
               olduğunu anlar.
```

---

## 🎭 TEMA

```
TEMA: FEDAKÂRLIK
      — "Başta her şeyi kaydettiren kişi, sonunda kendi kaydını kimsenin
         duymayabileceği bir yere bırakır."
      ⛔ TAKAS kalıbı DEĞİL: cümle bir ilk hâl ile bir son hâli karşılaştırıyor,
        "X için Y feda edilir" demiyor [TEMA_MUHENDISLIGI §3c moratoryumu].

MOTİF SAHNELERİ: S04 · S22 · S41 · S42 · S47 · S48
      ⛔ Altı sahne indeksi — tavan üç. Yazılmayan tema dekoratiftir.

MOTİF KANALLARI (§5 matrisi → §9):
  NESNE    kayıt        "Kaydet" K012 → K019 → K031 → KIRILMA K047 → modül K084
                        → onarım K184 → işaretçi K188
  KİNESİK  eldiven cama K009 çekirdek camı → K083 kabin kapağı → K160 halka camı
                        → K187 ekran
  IŞIK     tek pencere  K004 → K036 → K119 → K191
  SES      annenin lambası, kaydın içinden   K011 → K159 → K189

B3 ÇAPRAZ OKUMASI: bedelli seçimin yaşandığı sahne motif listesinde mi? EVET —
  S42 motifin KIRILDIĞI sahnedir (el camdan kalkar ve mandala gider · K164),
  S47 bedelin görüldüğü sahnedir (dokunulan cam artık karanlık · K181).
```

## 🧠 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU.md` §4)

```
NOVUM TİPİ:          İLİŞKİ — deponun İLK İLİŞKİ tipi novum'u
                     (13 filmin 12'si "fiziksel yasa"; tip 02.09.2026'da açıldı,
                      bugüne kadar hiç kullanılmadı)
NOVUM:               Yapı gördüğü her şeyi yeniden kurabiliyor, görmediği hiçbir şeyi
                     kuramıyor — ve geçidi açan eşleme görünmez bir iç durumdur.
NOVUM TAŞIYICISI:    aile fotoğrafındaki lamba × Mira'nın fotoğrafı odadaki lambanın
                     yanına tutması → fotoğraftaki flaş parlaması, odadaki lambanın
                     camında MADDİ BİR LEKE olarak kopyalanmıştır
TEK KARE (§4①):      ✅ "Odadaki lambanın camının üstünde, cama işlenmiş beyaz bir
                     parlama lekesi." — K070. Cümle taşıyıcı nesnenin ADINI içeriyor [D157]
                     ⛔ İPTAL KAPISI ÖLÇÜTÜ (`03_SAHNE_SIRALAMASI` §8):
                       lambanın camındaki leke   20 mm → 194 px
                       fotoğraftaki flaş parlaması 16 mm → 155 px
                       İKİSİ DE AYNI KAREDE ve ≥100 px. Üç denemede okunmuyorsa
                       FİLM ÜRETİLMEZ. Bu iki sayı referans paketinin RC sayfasına
                       ve SPEC'in göz kapısına aynen iner.
KİNETİK BAĞIMSIZLIK: ✅ Mira fotoğrafı kaldırır, lambanın yanına tutar, elini çeker.
                     Replik, dış ses ve ekran metni olmadan okunur. Kuralın önceki
                     iki kanıtı da sözsüz: K017 (yansıma geç döner) · K029 (cephe
                     bıçak gibi biter). ECHO yalnız ikisini adlandırır.
BAŞLIK ŞEMASI:       ✅ "THE FALSE EARTH" — 3 kelime. Kapak metni: "THAT ISN'T EARTH"
KURAL TEKRARI (§5):  KURULUM K017 (su) → DOĞRULAMA K029 (dükkân) → K070 (lamba) →
                     SONUÇ K094 (kopyalar çalışmıyor) → K180 (kabuktaki halkalar)
                     ≥3 sahne ✅ · ≥2 farklı nesne ✅ (su · cephe · lamba · halka)
İHLAL SAYISI (§3):   1 — ikincisi yok. Kabuk tanıdık: giysi, pod, gemi, bir çocukluk
                     odası. Yenilik yalnız yapının kuralında.
⛔ Üçü de ✅ → KONSEPT GEÇTİ.
```

## 🧭 B5 — HİKÂYE OMURGASI (`03_PLAN_ONCESI` B5 · kapı: prompt_kontrol ⑰)

```
B5 □ İSTEK:   Mira kayıp bir mürettebatı bulup gemisine geri götürecek — kurtarma
              pilotu olarak yaptığı iş bu; film başlamasa da VELA'nın son atış
              bölgesini tarıyor olacaktı (K005).
              ⛔ "anlamak / görmek / fark etmek" DEĞİL — bu bir İŞ.
   □ ENGEL:   Kurtarmaya geldiği kişi dokuz yıl önce ölmüş; onu çağıran şey,
              kurtarma aracının kendisini — dönüş çekirdeğini — istiyor.
   □ BEDEL:   dönüş çekirdeği · S44 (yok edilir) → kaybın GÖRÜLDÜĞÜ sahne S47
              ⭐ İKİNCİ ÖDEME: kurtarılma ihtimali · S49 ("Beni aramayın")
   □ MUHATAP: ☑ ikinci insan — Lena (kadrajda S11-S20 · S27 · kadraj dışı S30-S49)
              ☑ kendi geçmiş kararı — dokuz yıl önce kardeşinin çağrısına
                yetişememesi; K114'te GERÇEK kayıtla geri geliyor
              ⛔ İkisi de işaretli ve ikisi de sahne taşıyor.
   □ AYRILIK: S13 · K047 (B5b — iki insanlı plan) — Mira, ECHO'nun "ses
              eşleşmesi tam" bulgusunu duyar ve
              ECHO'yu SUSTURUR. Kardeşiyle aynı fikirde olmadığı ilk an.
              Farkı taşıyan kanal: temas reddi değil, ÜÇÜNCÜ SESİ KESME.

İSTEK ÇAPRAZI (`IKI_KISI` §3):
  Mira → Lena:  torbaya girmesini, odadan çıkmasını
  Lena → Mira:  kalmasını (K074 "Gitme." · K101 "Kalırsan yaşarım." · K158 "Kapıyı aç. Eve dön.")
  NESNE: önce KURTARMA TORBASI (S14-S16), sonra GEÇİT (S27-S42)
  ⛔ İkisi de aynı şeyi istemiyor ✅ · B figüran değil ✅

ÜRETİM SIRASI [D168 — dramatik sıra DEĞİLDİR; üretim her an durabilir]:
  0. REFERANS PAKETİ   RK1 kask+vizör · RK3 Lena · RC amber halka + mandal + kol ·
                       RD siyah madde — dördü ONAYLANMADAN tek klip üretilmez
  1. DORUK             S44 · K169-K174
  2. MERKEZÎ SEÇİM     S42 · K161-K164
  3. KAPANIŞ İMAJI     S50 · K190-K192
  4. BEDEL             S47 · K181-K183
  5. AÇILIŞ            S01-S02 · K001-K004
  6. KUSURLAR          S06 · S09 · S19 — kasıtlı anomalilerin sınandığı üç sahne
  7. kalan 40 sahne, bölüm sırasıyla
  ⛔ ÜRETİM DEFTERİ KAPISI [D168 · 3. vaka]: ilk KABUL satırı bu sıranın ilk
    halkası değilse ikinci klip üretilmez.
```

## ⚓ ÇAPA ÜÇLÜSÜ — SEÇİM · BEDEL · FİNAL (`OYUNCULUK_YAZIM_KILAVUZU` §2 · D202)

> Rubriğin tek testi: üç çapa vuruşta öncesi/sonrası karesi DONDURULUR ve bedendeki
> fark bir cümleyle yazılır. "Hiçbir şey" ise vuruş ekrana ulaşmamıştır ve hüküm
> skordan bağımsız `THE CHOICE IS INVISIBLE` olur. Bu blok o çifti ÖNCEDEN yazar.
> ⛔ Kılavuz §2: bu blokun SPEC'te şablon yeri YOK, plana ayrı blok olarak girer.

```
CHOICE  S42 · K164 · 1630-1640 s   (replik 4,0 s · el hareketi 7,5 s)
   KANAL: SOL ELDİVEN ↔ SOL ELDİVEN
   BEFORE: sol eldiven halkanın dar penceresinde DÜZ ve açık, avuç cama bastırılmış,
           parmak yastıkları beyazlamış (K160'tan taşınan durum)
   AFTER:  aynı eldiven camdan KALKMIŞ, halka boyunca bir karış gitmiş ve SARI
           MANDALIN üstünde KAPANMIŞ — kaldırmıyor, yalnız kapanıyor
   ÖLÇÜ:   35mm · Mira 2,6 m'de → W 2,67 m · H 1,50 m · yol 0,20 m (bir karış)
           → 0,20 / 1,50 × 2160 = **288 px**   ·   eşik H/8 = 0,1875 m ✅ GEÇER
   REDDEDİLEN NESNE KADRAJDA: halkanın camı (geçidin kendisi) K164'ten sonra da
           kadrajda kalır — seçim iki şeyden birini seçmektir [KARAKTER_KARTI §3]

COST    S44 · K169 · 1680-1690 s   (1. çekiş 3,5 s · TUTUŞ 5,5 s · 2. çekiş 8,0 s)
   KANAL: İKİ ELDİVEN ↔ İKİ ELDİVEN
   BEFORE: iki eldiven çelik kolun üstünde kapalı, kol üçte bir çekilmiş, ağırlık
           arka botta, omuzlar ellerinin GERİSİNDE
   AFTER:  iki eldiven kolla birlikte sonuna kadar inmiş, kol sert durağına
           çarpmış, omuzlar geri gelip DÜZLEŞMİŞ
   ÖLÇÜ:   24mm · Mira 4,0 m'de → W 6,00 m · H 3,375 m · yol 0,60 m (1 m'lik kolun
           üçte birinden sonuna yayı) → 0,60 / 3,375 × 2160 = **384 px**
           eşik H/8 = 0,42 m ✅ GEÇER
   REDDEDİLEN NESNE KADRAJDA: kolun kendisi ve halkanın gövdesi, klip sonunda da orada
   ⭐ Ödeme satırının DÖRT parçası bu tek karede okunur [⛔2 · D206]:
     bot (kaymaz) · kalça (arka bota yüklenir) · omuz (bir karış yol alır) ·
     DURAKSAMA (5,5 s'de tam bir saniye hiçbir şey hareket etmez)

FINAL   ⚠️ EŞİĞİN ALTINDA — ölçüldü, gizlenmedi
   EN GÜÇLÜ ADAY: S49 · K189 · 1880-1890 s (replik 5,0 s)
   KANAL: KASK ↔ KASK
   BEFORE: kask düz, çene yukarıda, iki eldiven kucağında açık
   AFTER:  kask son kelimede birkaç derece İNMİŞ ve orada KALMIŞ (geri kalkmıyor)
   ÖLÇÜ:   24mm · Mira 4,0 m'de → H 3,375 m · yol ≈ 0,05 m
           → 0,05 / 3,375 × 2160 = **32 px**   ·   eşik H/8 = 0,42 m ⛔ GEÇMEZ

   ⛔ FİLMİN GERÇEK FİNAL KLİBİ (K192) ÇAPA TAŞIYAMAZ ve bu ARİTMETİKTİR:
     18mm · Mira 14,0 m'de → H 15,75 m · eşik H/8 = 1,97 m. Mira'nın TAMAMI
     1,75 m'dir, yani o kadrajda HİÇBİR gövde jesti eşiği geçemez. Kadraj
     bilinçli olarak böyle: final bir eylem değil, bir kabullenmedir ve
     K192'nin tek olayı 8,0 s'de YANAN BİR IŞIKTIR (gövdede değil, dünyada).

   ⬜ SAHİP KARARI — üç seçenek, üçünün de bedeli yazılı:
     ① OLDUĞU GİBİ BIRAK. ⑩ mod D `THE CHOICE IS INVISIBLE` verebilir ve bu
        skoru düşürür. Bedel: bir mercek hükmü. Kazanç: final bozulmaz.
     ② K189'U ÇAPA YAP — kaskın inişi yerine İKİ ELDİVENİN kucakta KAPANMASI
        yazılır: yol ≈ 0,10 m → 64 px. Hâlâ eşiğin altında ama iki kat güçlü.
        Bedel: K189'un videosu yeniden yazılır. Kazanç: ölçü iki katına çıkar.
     ③ K192'YE İKİNCİ BİR KADRAJ EKLE — 50 sahnenin dışına çıkmadan, S50'nin
        üçüncü klibini 2 klibe böl (K192a yakın · K192b geniş). Bedel: SAHNE
        PLANI ve 192 sayısı DEĞİŞİR — ⛔ format kartı 192 klip diyor, bu
        seçenek D74 gerekçesi ve YENİDEN ONAY ister. Kazanç: gerçek final çapası.
   ⭐ ÖNERİ: ②. Filmi bozmuyor, ölçüyü iki katına çıkarıyor ve ⑩'a gösterilecek
     bir gövde farkı bırakıyor. ⛔ Ama karar sahibindir ve ① de meşrudur —
     "gerekmediğini yazmak da kapının bir parçasıdır".

KURAL DENETİMİ [§2]
  ☑ BEFORE ve AFTER aynı KANALDA (eldiven↔eldiven · eldiven↔eldiven · kask↔kask)
  ☑ Fark ADLANDIRILABİLİR: "el camdan kalkar ve mandalda kapanır" · "kol sonuna
    kadar iner" · "kask iner ve kalkmaz" — hiçbiri "duruşu değişir" değil
  ☑ Fark KADRAJDAN okunur: planı bilmeyen biri de söyleyebilir
  ☑ CHOICE karesinde reddedilen nesne kadrajda ve sonra da orada
  ⚠️ KADRAJ ÖLÇEĞİ: CHOICE ✅ 288 px · COST ✅ 384 px · FINAL ⛔ 32 px

NEREYE YAZILDI — üç yer, üç zaman [§2]
  İMAJ PROMPTU (t=0)       BEFORE gövdesi kelimesi kelimesine → K164 · K169 · K189
  VİDEO PROMPTU (klip içi) BEFORE → AFTER geçişi gövde FİİLİYLE → aynı üç klip
  SONRAKİ SAHNENİN İMAJI   AFTER gövdesi 0,0 s satırı olarak → K165 · K170 · K190
  ☑ Üçü de yazılı ve klasör koşusunda GO.
```

## 📱 DİKEY FİLMSE — ÜÇ ZORUNLU SATIR (KILAVUZ_REHBERI §2.1)

```
— UYGULANMAZ. Bu film YATAY 16:9'dur (§2.9). Üç satır dikey shorts'a özgüdür
  ve bu planda boş bırakılmaz, GEÇERSİZ olarak işaretlenir [D74 kalıbı].
  B5 omurgası (yukarıda) her formatta zorunludur ve yazılıdır.
```

---

## 🥁 VURUŞ TABLOSU  (`SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §2)

| # | vuruş | % | sahne | boşsa gerekçe |
|---|---|---|---|---|
| 1 | Açılış imajı | %0-2 | S01 · K001-K002 · 0:00-0:20 | — |
| 2 | Kurulum | %0-6 | S01-S03 · K001-K008 | — |
| 3 | Katalizör | **%6,3** | S04 · K012 — Mira protokolü çiğner ve kaskını alır | bant tavanı %15; erken olması meşru (HOOK §1.1) |
| 4 | Tartışma | %6-25 | S05-S13 · 2:00-8:00 | — |
| 5 | Orta nokta | **%50** | S25-S26 · 15:20-16:40 — yapının amacı + geminin yakalanması | sahte yenilgi; bahis yükselir |
| 6 | Umut-önce-düşüş | %75-78 | S38 · 24:00-24:40 | — |
| 7 | Her Şeyin Kaybı | **%79** | S40 · 25:20-26:00 | %75 bandının 4 puan üstü; S38'in umudu araya girdiği için kaydırıldı |
| 8 | Final | %85-99 | S43-S50 · 27:20-32:00 · DORUK S44 (%87,5) | — |
| 9 | Kapanış imajı | %100 | S50 · K190-K192 | açılışın aynası |

## 🪝 HOOK MİMARİSİ  (`HOOK_VE_ILK_SAHNE_KILAVUZU.md` §8)

```
HOOK TİPİ:       YANLIŞLIK KOMPOZİSYONU (§4) — tamamen tanıdık bir kare (vizörde
                 Dünya) + TEK anormal öğe (tamamen karanlık).
                 ⚠️ Anomali türetilmiş bir fenomen DEĞİL, bir cismin kendisi;
                 D73'ün tek-kare fizibilite kapısı bu yüzden geçilebilir.
S0 SORUSU:       "Bu karanlık gezegende neden tek bir pencere yanıyor?"
                 ⛔ Soru K004'te doğar; K002'de yalnız "bu ne?" vardır.
S1 İKİNCİ BİLGİ: Işık bir odadır, o odada biri var, ve o biri Mira'nın adını
                 söylüyor. Kimin olduğu S03'e ertelenir (bağlam taksiti).
İLK 2 SN SESİ:   gemi gövdesinin alçak uğultusu + kask içi nefes; replik YOK.
İLK 30 s:        K001 (U1) · K002 (U2) · K003 (U1) → ⛔ EN ÇOK İKİ KURULUM ✅ [D211]
İLK İNSAN SESİ:  K004 · 0:37,0 ("Mira.") — öncesinde 37 s kesintisiz insan sesi
                 yokluğu [SES §1a.2: sessizlikten gelen ilk insan sesi bir şalterdir]
AÇILIŞ ↔ KAPANIŞ: KAFİYE [D210] — K001 ve K192 AYNI kurulum (U1 · 18 mm · EWS ·
                 azimut 0° · yükseklik 3,00 m), kamera cümlesi BİREBİR, IN FRAME
                 ikisinde de `full body, back`, kadraj eni ikisinde de 28,00 m.
                 DEĞİŞEN TEK DEĞİŞKEN: K001'de vizörde TEK kara küre vardır;
                 K192'de kadrajda ONLARCA küre vardır ve her birinde bir ışık.
ÇIKIŞ [D211]:    adlandırılmış kare ("BAŞKA PENCERELER") + sesli siyah.
                 ⛔ Kart YOK, yazı YOK. TIMELINE son satırı `hold`.
```

---

## 🗺️ SAHNE HARİTASI

> Her satır iki bütçeyi de taşır: `KARAKTER_VE_DUYGU §6` (göz · tepki planı · el ·
> yürüyüş → **göz** sütunu davranış şeridinin harfi) ve `KURGU_RITMI §2` örüntü
> kırıcı — **ardışık iki SAHNE aynı palet + ses dokusunda olamaz.**
> 🆕 22.09.2026: örüntü kırıcı yalnız SAHNELER arasında aranır; sahne içinde palet
> ve ses AYNI kalır, yalnız kurulum değişir (`COK_KLIPLI_SAHNE_KILAVUZU` §4).
> Kamera sütunu: vuruş→açı `KAMERA_ACISI` · bant `ACI_YAYI` §3 (ardışık çift
> ≥1 ölçek kademesi VE ≥45°) · kalıp `MESHUR_SAHNE`.
> Davranış şeridi harfleri: S sabit · G gözlem · T tereddüt · K karar · R tepki ·
> D direnç · B bedel. Tempo: Y yavaş · N normal · H hızlı.

| S | klip · zaman | başlık | olay | kurulum (lens · ölçek · açı tipi) | palet / ses | bütçe |
|---|---|---|---|---|---|---|
| S01 | K001-K002 · 0:00-0:20 | KARA DÜNYA | Vizörde Dünya'ya benzeyen kara bir küre; ne güneş var ne şehir ışığı | U1 18mm EWS arkadan-yukarıdan · U2 24mm WS cepheden | obsidyen + vizör amberı / gemi uğultusu · nefes | göz S · tempo Y |
| S02 | K003-K004 · 0:20-0:40 | TEK IŞIK | Optik tarama karanlıkta tek sıcak noktaya kilitlenir; hoparlörden Mira'nın adı | U1 18mm EWS arkadan-yukarıdan · U2 24mm WS cepheden | obsidyen + tek amber nokta / tarama tıkırtısı · bozuk çağrı | göz G · tempo Y |
| S03 | K005-K008 · 0:40-1:20 | ÇAĞRI | ECHO çağrıyı çözer: VELA. Aile kaydı ile tarama yan yana; penceredeki ışık zayıflar | G3 35mm MS üç-çeyrek · G2 24mm WS cepheden | soğuk gri konsol + amber kayıt / konsol tonu · kayıttan ev sesi | göz T · tempo N |
| S04 | K009-K012 · 1:20-2:00 | ÇEKİRDEK | Çekirdek ve mandal tanıtılır; Mira protokolü çiğneyip inmeye karar verir | C3 35mm MS üç-çeyrek · C2 24mm WS cepheden | amber halka + grafit / halka rezonansı · eldiven camda | göz K · tempo N |
| S05 | K013-K015 · 2:00-2:30 | AYRILIŞ | Pod ayrılır; camda ana gemi küçülür, uzakta iki sinyalsiz küre geçer | P1 18mm EWS arkadan-yukarıdan · P2 24mm WS cepheden | siyah + pod paneli yeşili / itici darbesi · basınç tıslaması | göz R · tempo Y |
| S06 | K016-K019 · 2:30-3:10 | SİYAH OKYANUS | Podun yansıması yarım an geç dönüyor; Mira görür, kaydettirir, ilerler | O2 24mm WS cepheden · O3 35mm MS üç-çeyrek · O1 18mm EWS arkadan-yukarıdan | ayna siyahı + ince beyaz iz / su yüzeyi yankısı · itici | göz T · tempo Y |
| S07 | K020-K024 · 3:10-4:00 | KIYI ŞEHRİ | Cepheler poda doğru dönüyor; çağrıda nefes daralıyor, Mira iniyor | O2 24mm WS cepheden · O3 35mm MS üç-çeyrek · O4 50mm CU karşı açı | sis grisi + ıslak bazalt / sis içinde boğuk itici · çağrı | göz G · tempo N · ⭐ |
| S08 | K025-K027 · 4:00-4:30 | SOKAK | Mira yön işareti bırakır ve kardeşinin apartmanını fotoğraftan tanır | K3 35mm MS üç-çeyrek · K4 50mm CU karşı açı | ıslak siyah asfalt + soluk cam / bot sesi · damlama | göz G · tempo N |
| S09 | K028-K031 · 4:30-5:10 | ARKASIZ DÜKKÂN | Kusursuz cephenin arkası yok; elinin altında düz siyah yüzey | D2 24mm WS cepheden · D3 35mm MS üç-çeyrek | vitrin sarısı + düz siyah / cam titreşimi · aletin boş sinyali | göz T · tempo N |
| S10 | K032-K036 · 5:10-6:00 | PENCEREYE | Çağrı kesilip geri gelir; Mira koşar, kapı altındaki sıcak ışığa varır | M2 24mm WS cepheden · M3 35mm MS üç-çeyrek · M4 50mm CU karşı açı | soğuk merdiven grisi + kapı altı amber / nefes · basamak · kapı altından oda tonu | göz G · tempo H |
| S11 | K037-K040 · 6:00-6:40 | LENA | Odada Lena oturuyor, hiç yaşlanmamış; Mira'nın uzanan eli havada durur | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı · R2 24mm WS cepheden | sıcak lamba ambarı + ev dokusu / oda tonu · lamba vızıltısı | göz R · tempo Y |
| S12 | K041-K044 · 6:40-7:20 | TARAMA | Tarama Lena'yı sağlıklı gösterir; dışarısı solunamaz, tek temiz hava bu odada | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı | amber + tarayıcı soğuk beyazı / tarayıcı tonu · nefes | göz G · tempo N |
| S13 | K045-K048 · 7:20-8:00 | AYNI VURGU | Lena dokuz yıllık cümleyi aynı vurguyla söyler; Mira ECHO'yu susturur | R3 35mm MS üç-çeyrek · R2 24mm WS cepheden | amber + kaskın iç yansıması / kayıt ile canlı sesin üst üste binmesi | göz T · tempo N · ⭐ |
| S14 | K049-K052 · 8:00-8:40 | HESAP | Torbada yirmi dakika hava, yüksek yörüngede buluşma üç saat | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı · R2 24mm WS cepheden | kol ekranı soluk mavisi + amber / kol ekranı tonu · torba kumaşı | göz G · tempo N |
| S15 | K053-K056 · 8:40-9:20 | EMİR | Mira gemiyi alçak yörüngeye çağırır; geçidi ve çekirdek kapağını kapattırır | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı · R2 24mm WS cepheden | amber + pencereden geçen soğuk gemi ışığı / telsiz · uzak motor ateşlemesi | göz K · tempo N |
| S16 | K057-K060 · 9:20-10:00 | BEKLEYİŞ | Mira ilk kez güler; Lena'nın anlattığı anı kayıtla kelimesi kelimesine aynıdır | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı | en sıcak amber · en yumuşak doku / iki nefes · kelimeler arası kesik ek | göz R · tempo Y |
| S17 | K061-K064 · 10:00-10:40 | İZLEYEN ÇİZGİ | Duvarda ince bir amber çizgi alçalan gemiyi izler; Mira'nın sırtı dönük | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı · R2 24mm WS cepheden | amber + duvarda ikinci, yanlış amber / duvarın içinden gelen ince tık | göz S · tempo Y |
| S18 | K065-K068 · 10:40-11:20 | KAYITTA OLMAYAN ANI | Mira kaydedilmemiş bir anıyı sorar; Lena yanlış cevap verir ve yaklaşır | R3 35mm MS üç-çeyrek · R2 24mm WS cepheden | amber + soğuyan kenarlar / sessizlik · gecikmiş cevap | göz D · tempo N |
| S19 | K069-K072 · 11:20-12:00 | LAMBANIN İZİ | Lambadaki flaş lekesi kanıttır; Mira tahliyeyi iptal eder, yükselme kırk dakika | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı · R2 24mm WS cepheden | lamba camında beyaz leke / lamba vızıltısı · telsiz | göz K · tempo N |
| S20 | K073-K075 · 12:00-12:30 | METAL SESİ | Duvarın arkasından metal inler; Lena önüne geçer, Mira yanından geçer | R3 35mm MS üç-çeyrek · R4 50mm CU karşı açı | amber + kapı çerçevesi gölgesi / duvar içinde metal inlemesi | göz R · tempo N |
| S21 | K076-K079 · 12:30-13:10 | DUVAR | Duvar ince bir kabuk; arkasındaki boşlukta gömülü VELA'nın burnu görünür | W2 24mm WS cepheden · W3 35mm MS üç-çeyrek | boşluk siyahı + el feneri konisi / menteşe kopması · boşluk yankısı | göz G · tempo N |
| S22 | K080-K084 · 13:10-14:00 | VELA | Mira enkaza iner: kabin dokuz yıldır basınçsız. Kayıt modülünü söker | V2 24mm WS cepheden · V3 35mm MS üç-çeyrek · V4 50mm CU karşı açı | kırağı beyazı + enkaz grisi / ip gerilmesi · metal · ECHO | göz B · tempo Y |
| S23 | K085-K088 · 14:00-14:40 | ARŞİV | Arşiv her şeyin kaynağı: cepheler, Lena'nın nabzı, Lena'nın kelimeleri | V3 35mm MS üç-çeyrek · V4 50mm CU karşı açı | arşiv soğuk beyazı / modül tonu · arşivden kesik sesler | göz G · tempo N |
| S24 | K089-K092 · 14:40-15:20 | VELA'NIN SON KAYDI | Gerçek Lena, uzantı gelmeden kendi çekirdeğini parçalar ve ölür | V3 35mm MS üç-çeyrek · V4 50mm CU karşı açı · V2 24mm WS cepheden | kayıt yeşili + bozulma / bozulan kayıt sesi · alarm | göz R · tempo N |
| S25 | K093-K096 · 15:20-16:00 | AMAÇ | Yapı kopyalarını çalıştıramıyor, gerçeğini istiyor; uyarı göndermek geçidi açmak | V3 35mm MS üç-çeyrek · V4 50mm CU karşı açı · V2 24mm WS cepheden | soğuk beyaz + uzak amber / ECHO · uzak motor | göz T · tempo N |
| S26 | K097-K100 · 16:00-16:40 | TUTUŞ | Şehrin kaburgaları yükselen gemiye yetişir ve sarar; komuta hattı kopar | U3 35mm MS üç-çeyrek · U4 50mm CU karşı açı · U2 24mm WS cepheden | gece siyahı + gemi konum ışıkları / yapısal gerilme · kopan hat | göz R · tempo H |
| S27 | K101-K104 · 16:40-17:20 | SEN DEĞİLSİN | "Kalırsan yaşarım." Mira kask kilidine dokunur, fotoğrafı alıp çıkar | R1 18mm EWS arkadan-yukarıdan · R2 24mm WS cepheden | amber kapı ışığı + soğuk koridor / iki nefes · kapı | göz K · tempo N |
| S28 | K105-K108 · 17:20-18:00 | YOL | Sokaklar yer değiştirir; Mira kendi bıraktığı işareti yanlış duvarda bulur | K1 18mm EWS arkadan-yukarıdan · K2 24mm WS cepheden | ıslak siyah + reflektör parıltısı / koşu · yer değiştiren yapı sesi | göz R · tempo H |
| S29 | K109-K113 · 18:00-18:50 | ARKA YÜZ | Arkasız cephenin boşluğundan girip kaburgaya tırmanır; yukarıdan podu görür | K1 18mm EWS arkadan-yukarıdan · K2 24mm WS cepheden · K3 35mm MS üç-çeyrek | boşluk siyahı + kaburga matı / tırmanma · kayma · nefes | göz D · tempo H · ⭐ |
| S30 | K114-K117 · 18:50-19:30 | GERÇEK ÇAĞRI | Pencerelerden dokuz yıl önceki gerçek çağrı gelir: "Mira, beni bırakma." | K2 24mm WS cepheden · K3 35mm MS üç-çeyrek · K1 18mm EWS arkadan-yukarıdan | binlerce pencere ambarı / eksiz, kesintisiz gerçek kayıt | göz S · tempo Y |
| S31 | K118-K120 · 19:30-20:00 | BİNLERCE PENCERE | Şehrin bütün pencereleri birden yanar; pod kalkar | K2 24mm WS cepheden · K3 35mm MS üç-çeyrek | amber tarla + siyah gökyüzü / aynı anda yanan ışığın sessizliği | göz R · tempo N |
| S32 | K121-K124 · 20:00-20:40 | LEVHALAR | Şehir blokları ayrılır, sahil levhalar gibi yarılır, altta karanlık derinlik | U3 35mm MS üç-çeyrek · U4 50mm CU karşı açı · U2 24mm WS cepheden | levha kenarı grisi + derinlik siyahı / yapısal ayrılma · pod itici | göz G · tempo N |
| S33 | K125-K129 · 20:40-21:30 | KABUK | Kabuk kalkar: kıta boyunda halkalar, aralarında çalışmayan küçük karanlık kopyalar | U4 50mm CU karşı açı · U3 35mm MS üç-çeyrek · U2 24mm WS cepheden | kıta ölçeğinde grafit + sıfır amber / alçak frekanslı yapı sesi | göz R · tempo Y |
| S34 | K130-K132 · 21:30-22:00 | KABURGALAR | Pod kaburgaların arasından geçer; uzantı çekirdeğe ilerliyor, son mandal direniyor | U3 35mm MS üç-çeyrek · U4 50mm CU karşı açı | kaburga matı + pod ışığı / yakın geçiş · ECHO uyarısı | göz G · tempo H |
| S35 | K133-K135 · 22:00-22:30 | YANAŞMA | Pod bakım bölmesine kenetlenir; Mira gemiye girer | P4 50mm CU karşı açı · P5 100mm ECU insert | gemi gövdesi grisi + kilit yeşili / hizalama · kenet · basınç | göz G · tempo N |
| S36 | K136-K139 · 22:30-23:10 | KORİDOR | Tek gövde, kapalı dış kapağı zorlayıp girmiş; ucu yuvaya iki bölme uzakta | H3 35mm MS üç-çeyrek · H4 50mm CU karşı açı · H2 24mm WS cepheden | steril beyaz → mat siyah / gemi fanı · madde sürtünmesi | göz R · tempo N |
| S37 | K140-K144 · 23:10-24:00 | SESSİZLİK | Hoparlörden Lena'nın sesi gelir; Mira kabloyu koparır ve tam sessizlikte kalır | H3 35mm MS üç-çeyrek · H4 50mm CU karşı açı · H5 100mm ECU insert | koridor beyazı + tek acil ışığı / ses → tam sessizlik → nefes | göz S · tempo Y |
| S38 | K145-K148 · 24:00-24:40 | İTİCİLER | Yedek iticiler ateşlenir, bir uzantı kopar, gemi birkaç metre kurtulur | U4 50mm CU karşı açı · U5 100mm ECU insert | itici beyazı + siyah madde / itici · kopma · gövde inlemesi | göz D · tempo H |
| S39 | K149-K152 · 24:40-25:20 | YUVA | Çekirdek yuvası çatlar; siyah ucun halkanın gövdesine kaynadığı görülür | C4 50mm CU karşı açı · C5 100mm ECU insert · C3 35mm MS üç-çeyrek | amber halka + siyah uç / çatlama · amber rezonans | göz R · tempo N |
| S40 | K153-K156 · 25:20-26:00 | İKİSİ BİRDEN | Mira çekirdeği sökerek kaçırmayı dener; halka kıpırdamaz, içinde damar ilerler | C4 50mm CU karşı açı · C5 100mm ECU insert | amber + ilerleyen siyah damar / kelepçe · direnç · ECHO | göz D · tempo N |
| S41 | K157-K160 · 26:00-26:40 | TEKLİF | Kask telsizinden teklif gelir: "Kapıyı aç, eve dön" ve annesinin sesi | C4 50mm CU karşı açı · C5 100mm ECU insert | amber cam + kaskın içi / telsizde iki ses · nefes | göz T · tempo Y |
| S42 | K161-K164 · 26:40-27:20 | KARAR | Mira vedalaşır, ses yumuşar; eli camdan sarı mandala gider | C4 50mm CU karşı açı · C3 35mm MS üç-çeyrek | amber + sarı mandal / kırılan ses · "Biliyorum." | göz K · tempo Y |
| S43 | K165-K168 · 27:20-28:00 | HAZIRLIK | Mandal açılır, ayırma kolu oturur, servis yükü halkaya bağlanır | C4 50mm CU karşı açı · C3 35mm MS üç-çeyrek | sarı + amber + grafit / mekanik oturma · tek nefes | göz R · tempo N |
| S44 | K169-K174 · 28:00-29:00 | KOL | Mira kolu çeker: çekirdek fırlar, kapak gövdeyi keser, halka üçe ayrılır | C2 24mm WS cepheden · C3 35mm MS üç-çeyrek · C4 50mm CU karşı açı | amber → sıfır amber / iç gürültü → vakum sessizliği | göz B · tempo H · ⭐ |
| S45 | K175-K177 · 29:00-29:30 | MADDE DURUR | Koridordaki kesik dallar durur, kararır, elinin altında dağılır | H2 24mm WS cepheden · H1 18mm EWS arkadan-yukarıdan | mat siyah + acil ışığı / durma · çatlama · kuru dağılma | göz S · tempo Y |
| S46 | K178-K180 · 29:30-30:00 | PARÇALAR | Kollar gemiyi bırakıp parçalara uzanır; kabukta çalışmayan kopyaların yanına dizer | U1 18mm EWS arkadan-yukarıdan · U2 24mm WS cepheden | uzay siyahı + üç sönük parça / vakum sessizliği · gövde titreşimi | göz R · tempo Y |
| S47 | K181-K183 · 30:00-30:30 | KARANLIK HALKA | Çekirdek bölmesi karanlık; yaşam desteği çalışıyor, Dünya'yla bağ yok | C2 24mm WS cepheden · C1 18mm EWS arkadan-yukarıdan | sıfır amber + tek küçük yeşil / yaşam desteği tonu · ECHO | göz B · tempo Y |
| S48 | K184-K187 · 30:30-31:10 | GERÇEK KAYIT | Onarılan kayıtta gerçek Lena: "Işığı açık bırakmayın artık." | G1 18mm EWS arkadan-yukarıdan · G2 24mm WS cepheden | ekran ambarı + karanlık kokpit / onarılan kayıt · kusurlu gerçek ses | göz S · tempo Y |
| S49 | K188-K189 · 31:10-31:30 | UYARI | Mira sonraki gemiye uyarı bırakır: "Gelmeyin. Beni aramayın." | G1 18mm EWS arkadan-yukarıdan · G2 24mm WS cepheden | kokpit karanlığı + işaretçi kırmızısı / kayıt · işaretçi bip | göz K · tempo N |
| S50 | K190-K192 · 31:30-32:00 | BAŞKA PENCERELER | Karanlıkta başka küreler; her birinde başka bir uygarlığın tek penceresi yanıyor | U3 35mm MS üç-çeyrek · U2 24mm WS cepheden · U1 18mm EWS arkadan-yukarıdan | siyah + yüzlerce küçük amber / nefes · yaşam desteği · siyaha | göz R · tempo Y |

```
AÇI TİPİ SAYISI: 5 ≥3 ✅  (arkadan-yukarıdan · cepheden · üç-çeyrek · karşı açı ·
                 insert — KAMERA_ACISI §2 sekizlisinin beşi)
KURULUM SAYISI:  44 benzersiz kurulum / 192 klip
                 ⛔ TAVAN: klip sayısının yarısı = 96. 44 tavanın çok altında ✅
                 12 mekân × havuz kademesi; mekân değişmeden kademe değişiyor.
ÖLÇEK MERDİVENİ: kurulum havuzu bir MERDİVENDİR, rastgele değil —
                 kademe 0 = 18mm EWS azimut 0°    · kademe 1 = 24mm WS azimut 120°
                 kademe 2 = 35mm MS azimut 240°   · kademe 3 = 50mm CU azimut 60°
                 kademe 4 = 100mm ECU azimut 180°
                 Ardışık 191 çiftin 190'ı TAM BİR kademe atlar; tek ŞOK (≥2 kademe)
                 K125'tedir (kabuğun kalkması) — bant 1-2 şok, film 1 kullandı ✅
ÇİVİLENMİŞ SAHNE: dört sahnenin kademe dizisi şablondan türetilmedi, doğrudan
                 yazıldı — çünkü dördü de bir KİLİDİN ölçütünü taşıyor:
                   S03 · S04  [2,1,2,1]     filmin ilk okunabilir yüzü K005'te (0:40)
                              olsun diye; iskelet kendi hâline bırakıldığında ilk yüz
                              K023'teydi (3:40) ve P1'in ①. ölçütü ölçülemiyordu
                   S44  [1,2,3,2,1,2]       K169 GENİŞ plan — ⛔2 · D206 ödeme satırı
                              dört parçayı (bot · kalça · omuz · duraksama) tek karede ister
                   S50  [2,1,0]             K192 = K001'in kurulumu — D210 kafiyesi
                 ⛔ Çivileme İLERİ KISITLA yapılır: bir sonraki sahne çiviliyse,
                   öncekinin SON kademesi ona tam bir kademe uzak seçilir. Kısıt
                   yazılmadığında S43→S44 sınırında üç kademelik sıçrama doğuyordu.
BÖLÜM KESİĞİ:    her 12 klipte bir, ve HER kesik bir SAHNE sınırındadır:
                 S04|S05 · S07|S08 · S10|S11 · S13|S14 · S16|S17 · S19|S20 ·
                 S22|S23 · S25|S26 · S28|S29 · S31|S32 · S34|S35 · S37|S38 ·
                 S40|S41 · S43|S44 · S46|S47 · (film sonu)
                 ⛔ Bölüm sınırı da ardışık bir ÇİFTTİR ve bandı tutar ✅
                 ⛔ QA PART masterı sahne ortasından kesilmez ✅
```

### ⭐ KURULUM İSKELETİ — bölüm dosyalarına AYRI AYRI yazılır

> ⛔ **KRİTİK BİÇİM:** `prompt_kontrol.py` iskeleti `\b([A-Z])\b` ile okur — harfler
> TEK BÜYÜK HARF olmak zorunda — ve harf sayısını **o dosyadaki video promptu
> sayısıyla** karşılaştırır. Bu yüzden `KURULUM İSKELETİ:` satırı HER BÖLÜM
> DOSYASINA ayrı ayrı, 12 harf olarak yazılır. Harf o dosya içinde tek bir
> kurulumu gösterir; **dosyalar arası harf paylaşılmaz.**

| bölüm | klip | KURULUM İSKELETİ (12 harf) | kurulum | dönüş |
|:--:|:--:|---|:--:|:--:|
| 1 | K001-K012 | `A B A B C D C D E F E F` | 6 | 6/12 · %50 |
| 2 | K013-K024 | `A B A C D C E C D C D F` | 6 | 6/12 · %50 |
| 3 | K025-K036 | `A B A C D C D E F E F G` | 7 | 5/12 · %42 |
| 4 | K037-K048 | `A B A C A B A B A C A C` | 3 | 8/12 · %67 |
| 5 | K049-K060 | `A B A C A B A C A B A B` | 3 | 9/12 · %75 |
| 6 | K061-K072 | `A B A C A C A C A B A C` | 3 | 8/12 · %67 |
| 7 | K073-K084 | `A B A C D C D E F E F G` | 7 | 5/12 · %42 |
| 8 | K085-K096 | `A B A B A B A C A B A C` | 3 | 9/12 · %75 |
| 9 | K097-K108 | `A B A C D E D E F G F G` | 7 | 5/12 · %42 |
| 10 | K109-K120 | `A B A B C B C B A B C B` | 3 | 8/12 · %67 |
| 11 | K121-K132 | `A B A C B A B A C A B A` | 3 | 8/12 · %67 |
| 12 | K133-K144 | `A B A C D C E C D C D F` | 6 | 6/12 · %50 |
| 13 | K145-K156 | `A B A B C D C E C D C D` | 5 | 7/12 · %58 |
| 14 | K157-K168 | `A B A B A C A C A C A C` | 3 | 9/12 · %75 |
| 15 | K169-K180 | `A B C B A B D E D F G F` | 7 | 5/12 · %42 |
| 16 | K181-K192 | `A B A C D C D C D E F G` | 7 | 5/12 · %42 |

```
DÖNÜŞ (bağlayıcı sayı · DOSYA İÇİ): 109/192 = %56,8   ≥ %40 ✅
  ⛔ ⑩④ dönüşü her bölüm dosyasının KENDİ İÇİNDE sayar (pencere: önceki 4 klip).
  ⚠️ Bölüm sınırını aşan film-geneli sayım 122/192 verir ve GEÇERSİZDİR.
KÜME:   YOK — çok klipli sahne rejiminde küme kalktı (zincir kaldırıldı).
        ⑩④'ün 'KÜME ≥2' dalı `SAHNE PLANI:` beyan eden dosyada KOŞMAZ.
        Bekleme aynı kurulumda değil, aynı MEKÂN ve EYLEMDE kalınarak kurulur.
⛔ Aynı harfin kamera metni BİREBİR kopyalanır ve dönüş işaretini taşır:
        "— the same position, height and lens as Clip N."
⛔ ZİNCİR DİLİ YASAK (㉜⑤ BLOCK): "continues the previous clip from its exact
   last frame" · "picks up where the previous" · önceki klibe atıf yapan START FRAME.

SAHNE PLANI: 2 2 4 4 3 4 5 3 4 5 4 4 4 4 4 4 4 4 4 3 4 5 4 4 4 4 4 4 5 4 3 4 5 3 3 4 5 4 4 4 4 4 4 6 3 3 3 4 2 3
        ⭐ Sahne başına KLİP sayısı; toplam = 192 = CLIP COUNT.
        BU SATIR ㉜ KAPISINI AÇAR ve ⑩④'ün KÜME hedefini kapatır.
        Değişirse bölüm dosyalarındaki 📍 başlıkları + sahne tablosu + hikâye
        onayı BİRLİKTE değişir. Kılavuz: COK_KLIPLI_SAHNE_KILAVUZU.md
```

### 🎥 HARF → KAMERA HARİTASI

> Aynı harfin kamera cümlesi o bölüm dosyası içinde BİREBİR kopyalanır.
> Kurulum kimliği (U1 · R3 · C4 …) MEKÂN + KADEME demektir ve film boyu sabittir.

| bölüm | harf | mekân | kurulum | lens · ölçek · açı |
|:--:|:--:|---|:--:|---|
| 1 | A | uzay / gemi dışı | U1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 1 | B | uzay / gemi dışı | U2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 1 | C | gemi kokpiti | G3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 1 | D | gemi kokpiti | G2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 1 | E | çekirdek bölmesi | C3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 1 | F | çekirdek bölmesi | C2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 2 | A | pod içi | P1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 2 | B | pod içi | P2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 2 | C | kıyı hattı | O2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 2 | D | kıyı hattı | O3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 2 | E | kıyı hattı | O1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 2 | F | kıyı hattı | O4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 3 | A | kıyı şehri sokağı | K3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 3 | B | kıyı şehri sokağı | K4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 3 | C | dükkân cephesi | D2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 3 | D | dükkân cephesi | D3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 3 | E | apartman | M2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 3 | F | apartman | M3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 3 | G | apartman | M4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 4 | A | Lena'nın odası | R3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 4 | B | Lena'nın odası | R4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 4 | C | Lena'nın odası | R2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 5 | A | Lena'nın odası | R3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 5 | B | Lena'nın odası | R4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 5 | C | Lena'nın odası | R2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 6 | A | Lena'nın odası | R3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 6 | B | Lena'nın odası | R4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 6 | C | Lena'nın odası | R2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 7 | A | Lena'nın odası | R3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 7 | B | Lena'nın odası | R4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 7 | C | duvar arkası boşluk | W2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 7 | D | duvar arkası boşluk | W3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 7 | E | VELA enkazı | V2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 7 | F | VELA enkazı | V3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 7 | G | VELA enkazı | V4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 8 | A | VELA enkazı | V3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 8 | B | VELA enkazı | V4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 8 | C | VELA enkazı | V2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 9 | A | uzay / gemi dışı | U3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 9 | B | uzay / gemi dışı | U4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 9 | C | uzay / gemi dışı | U2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 9 | D | Lena'nın odası | R1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 9 | E | Lena'nın odası | R2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 9 | F | kıyı şehri sokağı | K1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 9 | G | kıyı şehri sokağı | K2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 10 | A | kıyı şehri sokağı | K1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 10 | B | kıyı şehri sokağı | K2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 10 | C | kıyı şehri sokağı | K3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 11 | A | uzay / gemi dışı | U3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 11 | B | uzay / gemi dışı | U4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 11 | C | uzay / gemi dışı | U2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 12 | A | pod içi | P4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 12 | B | pod içi | P5 | 100mm · ECU · insert · azimut 180° · üst açı 30° · yükseklik 1,90 m |
| 12 | C | gemi koridoru | H3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 12 | D | gemi koridoru | H4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 12 | E | gemi koridoru | H2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 12 | F | gemi koridoru | H5 | 100mm · ECU · insert · azimut 180° · üst açı 30° · yükseklik 1,90 m |
| 13 | A | uzay / gemi dışı | U4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 13 | B | uzay / gemi dışı | U5 | 100mm · ECU · insert · azimut 180° · üst açı 30° · yükseklik 1,90 m |
| 13 | C | çekirdek bölmesi | C4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 13 | D | çekirdek bölmesi | C5 | 100mm · ECU · insert · azimut 180° · üst açı 30° · yükseklik 1,90 m |
| 13 | E | çekirdek bölmesi | C3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 14 | A | çekirdek bölmesi | C4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 14 | B | çekirdek bölmesi | C5 | 100mm · ECU · insert · azimut 180° · üst açı 30° · yükseklik 1,90 m |
| 14 | C | çekirdek bölmesi | C3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 15 | A | çekirdek bölmesi | C2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 15 | B | çekirdek bölmesi | C3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 15 | C | çekirdek bölmesi | C4 | 50mm · CU · karşı açı · azimut 60° · alt açı 20° · yükseklik 1,10 m |
| 15 | D | gemi koridoru | H2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 15 | E | gemi koridoru | H1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 15 | F | uzay / gemi dışı | U1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 15 | G | uzay / gemi dışı | U2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 16 | A | çekirdek bölmesi | C2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 16 | B | çekirdek bölmesi | C1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 16 | C | gemi kokpiti | G1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |
| 16 | D | gemi kokpiti | G2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 16 | E | uzay / gemi dışı | U3 | 35mm · MS · üç-çeyrek (yandan) · azimut 240° · göz hizası 1,55 m |
| 16 | F | uzay / gemi dışı | U2 | 24mm · WS · cepheden · azimut 120° · göz hizası 1,55 m |
| 16 | G | uzay / gemi dışı | U1 | 18mm · EWS · arkadan-yukarıdan · azimut 0° · yükseklik 3,00 m |

---

## 🎙️ REPLİK TABLOSU (`SES_VE_DIYALOG_URETIM` §1-§2a)

> ⛔ **SANİYE HESAPLANMAZ, HESAPLATILIR** [D122]: `replik(K_n) = (n−1) × 10 s + ofset`.
> Bu tablo = SPEC `DIALOGUE LINES` = promptlardaki tırnaklı replik. ㉓ üçünü karşılaştırır [D203].
> Repliğin İNGİLİZCE metni bölüm dosyasındaki promptta durur; burada İŞLEVİ durur.
> ⛔ İŞLEV sütunu ekranda OLMAYAN bir şeyi taşır [D217]. Ses kapatıldığında izleyici
> o bilgiyi kadrajdan alabiliyorsa replik silinir ya da görünmeyene çevrilir.

| # | klip | S | saniye | konuşan | REG | kanal | İŞLEV (B5 satırı / vuruş) |
|---|:--:|:--:|:--:|---|:--:|---|---|
| 1 | K002 | S01 | 0:16,0 | ECHO | M | gemi sesi | ENGEL — mesafeyi kimse kadrajdan alamaz |
| 2 | K004 | S02 | 0:37,0 | çağrı | H | hoparlör | İSTEK — çağıran biri var; adı bilmesi kadrajda yok |
| 3 | K005 | S03 | 0:43,0 | ECHO | M | gemi sesi | İSTEK — Mira'nın neden BURADA olduğu |
| 4 | K006 | S03 | 0:55,0 | Lena (kayıt) | H | aile kaydı | MUHATAP — ailenin ritüeli; tohum |
| 5 | K012 | S04 | 1:55,0 | ECHO / Mira | M/H | gemi sesi / oda | MUHATAP (kendi kararı) — kuralı çiğnediğini duyuyoruz |
| 6 | K015 | S05 | 2:24,0 | ECHO | M | pod sesi | ENGEL — arşivle karşılaştırma kadrajda yok |
| 7 | K018 | S06 | 2:56,0 | ECHO | M | pod sesi | ENGEL — ⚠️ D217 ile YENİDEN YAZILDI: gecikme ekranda, "su değil" değil |
| 8 | K019 | S06 | 3:07,0 | Mira | H | kask içi | İSTEK — erteleme kararı |
| 9 | K023 | S07 | 3:43,0 | Lena (çağrı) | H | telsiz | ENGEL — saat işliyor |
| 10 | K031 | S09 | 5:07,5 | Mira | H | kask içi | İSTEK — ikinci erteleme; alışkanlık |
| 11 | K040 | S11 | 6:34,0 | Lena | H | oda | MUHATAP — karşılama |
| 12 | K043 | S12 | 7:05,0 | ECHO | M | kask içi | ENGEL — tahliye hesabının ilk terimi |
| 13 | K045 | S13 | 7:24,0 | Lena | H | oda | MUHATAP — kusur 4'ün kendisi |
| 14 | K046 | S13 | 7:37,0 | ECHO | M | kask içi | ENGEL — ölçüm, kadrajda yok |
| 15 | K051 | S14 | 8:25,0 | ECHO | M | kask içi | ENGEL — hesabın ikinci terimi |
| 16 | K053 | S15 | 8:43,0 | Mira / ECHO | H/M | telsiz | MUHATAP (kendi kararı) — tuzağı tamamlayan emir |
| 17 | K065 | S18 | 10:43,0 | Mira | H | oda | MUHATAP — sınama |
| 18 | K066 | S18 | 10:55,5 | Lena | H | oda | MUHATAP — yanlış cevap (kayıtlı başka gün) |
| 19 | K067 | S18 | 11:08,0 | Lena | H | oda | MUHATAP — soruyu geri çevirir; mesafe daralır |
| 20 | K071 | S19 | 11:47,0 | Mira | H | oda | BEDEL hazırlığı — kural bir kez söylenir |
| 21 | K072 | S19 | 11:52,0 | Mira / ECHO | H/M | telsiz | BEDEL hazırlığı — sayaç kurulur |
| 22 | K074 | S20 | 12:16,0 | Lena | H | oda | MUHATAP — ilk açık engelleme |
| 23 | K080 | S22 | 13:12,0 | Mira | H | kask içi | İSTEK — aşağı inmesinin gerekçesi |
| 24 | K083 | S22 | 13:46,5 | ECHO | M | kask içi | BEDEL — ölüm kanıtı; kadrajda beden yok |
| 25 | K088 | S23 | 14:36,0 | ECHO | M | kask içi | ENGEL — ikinci kaynak |
| 26 | K094 | S25 | 15:33,0 | ECHO | M | kask içi | ENGEL — yapının amacı |
| 27 | K095 | S25 | 15:42,0 | Mira / ECHO / Mira | H/M/H | kask içi | SINIR — Mira'nın yapmayacağı şey |
| 28 | K099 | S26 | 16:26,0 | ECHO | M | kask içi | ENGEL — görünmeyen kopma |
| 29 | K101 | S27 | 16:43,0 | Lena | H | kapı | MUHATAP — teklif biçiminde tehdit |
| 30 | K103 | S27 | 17:05,0 | Mira | H | oda | AYRILIK — kararın sözü |
| 31 | K108 | S28 | 17:56,0 | ECHO | M | kask içi | ENGEL — ⚠️ D217 ile YENİDEN YAZILDI: "rota geçersiz" ekranda, mesafe değil |
| 32 | K114 | S30 | 18:53,0 | Lena (gerçek kayıt) | H | pencereler | MUHATAP (kendi kararı) — suçluluk; eksiz, gerçek |
| 33 | K131 | S34 | 21:45,0 | ECHO | M | kask içi | ENGEL — görünmeyen saat |
| 34 | K139 | S36 | 23:04,0 | ECHO | M | kask içi | ENGEL — Mira'nın elle açmasının sebebi |
| 35 | K155 | S40 | 25:46,0 | ECHO | M | kask içi | ENGEL — kaçırmanın imkânsızlığı |
| 36 | K158 | S41 | 26:14,0 | Lena | H | kask telsizi | MUHATAP — ayartma, tehdit değil TEKLİF |
| 37 | K159 | S41 | 26:26,5 | anne (gerçek kayıt) | H | kask telsizi | MUHATAP — ödeme (K011) |
| 38 | K162 | S42 | 26:54,0 | ECHO | M | kask içi | MUHATAP — seçim somutlaşır |
| 39 | K163 | S42 | 27:05,0 | Mira / ses | H/H | kask telsizi | BEDEL kararı — veda ile teslimiyet arası |
| 40 | K164 | S42 | 27:14,0 | Mira | H | kask telsizi | BEDEL kararı — MERKEZÎ SEÇİM |
| 41 | K166 | S43 | 27:36,0 | ECHO | M | kask içi | BEDEL — mekanizma önceden bilinir |
| 42 | K177 | S45 | 29:27,0 | ECHO | M | kask içi | ENGEL — ⚠️ D217 ile YENİDEN YAZILDI: kesilme ekranda, yapının yaşaması değil |
| 43 | K178 | S46 | 29:34,0 | ECHO | M | kask içi | ENGEL — kolların neden gemiyi bıraktığı |
| 44 | K183 | S47 | 30:25,0 | ECHO | M | kokpit | BEDEL — ⚠️ D217 ile KISALTILDI: "yaşam desteği çalışıyor" ekranda |
| 45 | K185 | S48 | 30:44,0 | Lena (gerçek) | H | onarılan kayıt | MUHATAP — temanın cümlesi |
| 46 | K188 | S49 | 31:13,0 | Mira | H | işaretçi kaydı | BEDEL — ikinci ödeme |
| 47 | K189 | S49 | 31:25,0 | Mira | H | işaretçi kaydı | BEDEL — kapanış |

```
REPLİKLİ KLİP:  47 / 192        REPLİKLİ SAHNE: 29 / 50
REGISTER:       HUMAN 25 · MACHINE 22
KAYIT (oynatılan arşiv · canlı replik SAYILMAZ): K006 · K114 · K159 · K185 · K188 · K189
İLK REPLİK:     K004 · 0:37,0 — öncesinde 37 s kesintisiz insan sesi yokluğu
BEDENLEŞTİRME:  ☑ S11-S20 · S27 — ve bu filmde TERSİNE işliyor (bilinçli karar):
                Lena'nın sesi BEDENLE başlar (ağız kadrajda, oda içinde) ve
                BEDENSİZLEŞİR (S30 pencereler · S37 hoparlör · S41 kask telsizi).
                Chion'un kuralı sesin bedenleşince otoritesini yitirdiğini söyler;
                burada yapı bedeni KAYBEDİNCE otoritesini kazanıyor.
                ⚠️ BEDELİ: S11-S20'de ekranda konuşan ağız var → lip-sync + AI
                damgası riski ikisi birden açık [KART 7 · D215].
                ⛔ PROB B koşulmadan bu klipler ÜRETİLMEZ.
⛔ Sahne başına ≤1 replikli klip varsayılanını aşan 8 sahne var (S06 · S13 · S18 ·
   S19 · S22 · S25 · S27 · S42) ve her biri TEK BİR DEĞİŞ-TOKUŞU taşır (hamle →
   cevap), iki ayrı repliği değil. Gerekçeler `03_SAHNE_SIRALAMASI` §5'te satır satır.
⛔ UNCLEAR register yazımda yasak · sayı söyleyen replik MACHINE'de [D82]
KAPI: promptlar bitince PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md (Kart P 2b) —
      CUT/UNCLEAR varken üretime geçilmez
```

---

## 📖 BIBLE'LAR

> Karakter bloğu **kelimesi kelimesine** burada sabitlenir; IMAGE promptuna yalnız
> o karenin `IN FRAME:` satırındaki kısmı gider [D214 · ㉖]. "BIBLE'a bak" atfı
> YASAK (kural ③), ama self-contained ≠ Bible'ın tamamı: **kadrajda olmayan YAZILMAZ.**
> Videoya Bible girmez — `START FRAME:` tek satır.
> ⛔ Bu blok promptların KAYNAĞIDIR, kopyası değil.

### 👤 Character Bible

**MIRA — kurtarma pilotu** (ad prompta GİRMEZ [D34]; promptta "the pilot")

```
A sealed one-piece pressure suit in matt charcoal grey, dry and unreflective, with a
single pale grey band across the left shoulder. A rigid helmet with a visible dark
frame and one flat clear visor panel. Beneath the visor the face reads as a face and
nothing more.
```
```
⛔ KİMLİK ÖZNİTELİĞİ TAVANI: promptta kişi başına EN ÇOK ÜÇ [D167 · red vaka 15].
   Mira'nın üçü:  ① kapalı vizör (tek düz panel + koyu çerçeve)
                  ② sol omuzdaki açık gri bant
                  ③ sağ diz ve sağ önkoldaki kir bölgesi (K024'ten itibaren)
   ⛔ Kesin boy · ten rengi · saç rengi · yaş BU PLANDA KALIR, prompta GİRMEZ.
   ⛔ Yüz yüzeyi (brow / jaw / cheekbones / pores) yalnız `IN FRAME: face` olan
      klipte ve orada da TEK cümleyle. Bu filmde ~40 klip, 192 değil.
VİZÖR [D146]:  tek düz panel · görünür koyu çerçeve · optik berrak.
   ⛔ `seamless` · `dome` · `bubble` · `mirrored` hiçbir yerde YAZILMAZ.
   Aracı: referans paketi RK1 sayfası — onaylanmadan Mira'nın klibi üretilmez.
KASK DURUMU [D208]: KAPALI · K001-K192 · açık 0 klip · ARA DURUM YOK.
KİR [D42]: tek bölge, tek başlangıç klibi. Sağ diz + sağ önkol, K024'ten itibaren;
   birikir, hiç sıfırlanmaz, hiç temizlenmez.
ÇIPLAK DERİ NEGATİFİ [D175 · ㉑]: Mira'nın klibinde ÜÇ BÖLGE birden —
   `above the collar` + `at the wrist` + `at the ankle`.
SIRT [D139]: `IN FRAME: back` olan klipte yüz tarifi YAZILMAZ; omuz hattı, bant ve
   kir bölgesi taşır. Sırt ünitesi heykelsi ve POZİTİF tarif edilir, yasakla değil.
```

**LENA — odadaki** (ad prompta GİRMEZ; promptta "the woman in the room")

```
A woman in soft indoor clothes: a pale long-sleeved top and dark trousers, the fabric
stiff and still. No helmet, no suit, no gloves. She is lit only by the table lamp.
```
```
⛔ KİMLİK ÖZNİTELİĞİ TAVANI: üç —
   ① kasksız ve giysisiz (Mira'dan ayıran birinci eksen)
   ② açık renkli uzun kollu üst
   ③ hiç yaşlanmamış olması — ve bu YAZILMAZ, KADRAJ söyler (fotoğrafla yan yana)
⛔ LENA'NIN KLİBİNDE ÇIPLAK DERİ NEGATİFİ YAZILMAZ [D175 · D208 ayrımı].
   O kasksız ve giysisizdir; cümle yazılırsa kapı onu ihlal sanar. SPEC C'de ayrım yazılı.
⛔ KUMAŞ [D59 · D153]: `the fabric stiff and still` — gevşek/dalgalanan kumaş tarifi
   YAZILMAZ. `flowing` · `billowing` · `rippling` hiçbir yerde.
KADRAJ ÖMRÜ: S11-S20 ve S27. S20'den SONRA kadrajda YOK — yalnız ses [② DEVAMLILIK
   kilidi · STOLEN_SKY'ın S13→S24 arızası].
REFERANS: RK3 sayfası — onaylanmadan Lena'nın geçtiği hiçbir klip üretilmez [KAPI 0].
```

```
İKİ KİŞİ · KADRAJ TARAFI: Mira kadrajın SOLUNDA, Lena SAĞINDA.
   Taraf değişimi YALNIZ S20'de (Lena önüne geçer) ve o klipte geçiş GÖRÜNÜR.
MESAFE EĞRİSİ (metre): S11 1,8 → S13 1,2 → S16 1,0 → S18 0,7 → S20 0,5 →
   S27 1,5 (eşik) → S30+ kadraj dışı → S41 ∞ (yalnız ses)
   ⛔ Ardışık sahnede en çok bir bant; final mesafesi ilk mesafeden farklı ✅
HUMAN COUNT LOCK [KART 4 · D69]: her promptta kadrajdaki insan sayısı YAZILIR (0 · 1 · 2).
   İniş/kalkış klipleri (K013-K014 · K118-K120 · K133-K135) UZAKTAN; rampada kimse yok.
FAZ FARKI: hiçbir TIMELINE satırında ikisi aynı fiili aynı saniyede yapmaz.
   TEK BİLİNÇLİ İSTİSNA K048 (ikisi aynı anda gülümser) — tekinsizliği tam olarak
   bu kuralın bilerek çiğnenmesinden geliyor.
```

### 🌍 World Bible

```
DÜNYA ÇAPASI — üç cümle, film boyu DEĞİŞMEDEN [D209]:
  GÖK     A sky of uniform black, no stars, no sun and no moon.
  UFUK    The horizon is black water lying mirror-flat, or wet black basalt.
  YER İMİ One warm window burning in the distance, the only point source on the ground.
NOVUM TAŞIYICISI — LAMBANIN CAMI · KANONİK TARİF, kelime kelime kilitli
  (24.09.2026 · bölüm 4-5-6 taramasından çıktı: aynı nesne üç ayrı biçimde
   yazılmıştı — "teardrop of cloudiness" · "white mark" · "white oval mark" —
   ve novumun TEK KANITI olan nesnede bu ② DEVAMLILIK kırılmasıdır.)

  NESNE   a table lamp with a brass base and a clear glass body
  İZ ①    a hairline crack up one side of the glass, old and clean-edged
          → NESNENİN kendi kusuru. S03'teki kayıtta (K006) DA VARDIR.
  İZ ②    one white oval mark twenty millimetres across, soft-edged on one side
          and sharp on the other, set into the material
          → FOTOĞRAFIN kusuru: kamera flaşının parlaması. Cam kusuru DEĞİL.
  FOTOĞRAF one white oval flare sixteen millimetres across, the same soft edge
          on the same side — ve fotoğraftaki lamba AYNI çatlağı taşır.

  ⭐ ÖNERME TAM BURADA KURULUYOR: yapı, nesnenin kusurunu (çatlak) ve NESNENİN
    RESMİNİN kusurunu (parlama) aynı özenle kopyalamış. İkisini ayırt edemiyor.
    Bu yüzden K070'te DÖRT unsur birden okunur: gerçek camda çatlak + oval leke,
    fotoğraftaki lambada aynı çatlak + oval parlama.

  GÖRÜNÜRLÜK — ne kadar yazılacağı MESAFEYE bağlı [D179 ile ölçüldü]:
  | kadraj            | oval iz | çatlak (boy) | promptta        |
  |-------------------|--------:|-------------:|-----------------|
  | CU  50mm @ 0,55 m |  194 px |       582 px | TAM kanonik     |
  | MS  35mm @ 2,6 m  |   29 px |        86 px | çatlak + "one small white mark" |
  | WS  24mm @ 4,0 m  |   13 px |        38 px | yalnız lamba; iz YAZILMAZ |
  ⛔ MS'te izin ŞEKLİ yazılmaz — 29 px'te okunmaz ve okunmaması TASARIMDIR:
    iz S11'den beri kadrajdadır, fark edilmesi K070'tedir [⚠️7 · D179].

YER İMİ MESAFESİ — kilitli, D179 ile ölçüldü:
  kıyıdan (S07)  cephe hattı 140 m · pencere aynı düzlemde → 24mm'de 29 px · 50mm'de 61 px
                 ⇒ bu iki klipte pencere KAYNAK olarak okunur, NESNE olarak değil
                 [D179 dışı · emsal K182 yeşil ışık]
  sokaktan (S08) pencere 55 m → 35mm'de 109 px ⇒ artık NESNE olarak okunur ✅
  ⭐ Yer iminin "tek ışık"tan "bir binanın penceresi"ne dönüşmesi BU İKİ ÖLÇÜMDÜR;
    kadraj daraltılarak ya da pencere öne alınarak ÇÖZÜLMEZ — mesafe hikâyenin kendisi.

⛔ Bu üçünden biri DEĞİŞİYORSA bu bir OLAYDIR ve haritada yazılıdır:
  S31 · K119 — şehrin BÜTÜN pencereleri aynı anda yanar. YER İMİ tekilliğini
  kaybeder ve tehdit tam olarak budur.

YAPI (siyah madde · kabuk · halkalar) — ANATOMİ KARTI, film boyu SABİT [KART 13 · ⚠️2]:
  kaburga sayısı şehir başına        12   (S07 · S26 · S29 · S34 · her seferinde 12)
  kıta boyunda halka sayısı           2   (S33 · ters yönde dönüyor)
  halkalar arasındaki sönük kopya     9   (S33 · K127 → S46 · K180 aynı 9)
  ana geminin çekirdek halkası        1   (S04 → S44'te ÜÇE ayrılır → S46'da 3 parça)
  kabuk levhası (sahilde)             4   (S32)
ÖLÇEK MERDİVENİ [⚠️2 · P3 ölçer]: S32 → S33 → S34 aynı nesnenin monotonik kesri;
  her yapı planında ÖLÇEK ŞAHİDİ var (pod ya da ana gemi, silüet olarak).

MEKÂNLAR (12) ve kurulum kimliğinin harfi:
  U uzay / gemi dışı · G gemi kokpiti · C çekirdek bölmesi · H gemi koridoru ·
  P pod içi · O kıyı hattı · K kıyı şehri sokağı · D dükkân cephesi ·
  M apartman · R Lena'nın odası · W duvar arkası boşluk · V VELA enkazı
```

### 🎥 Camera Bible

```
Fixed lockoff. Absolutely zero camera movement. In a single continuous shot.
36 mm sensor. Shot on an anamorphic-free spherical lens.
```
```
⛔ KLİP İÇİ KAMERA HAREKETİ SIFIR — 192 klibin 192'sinde [KART 8].
   Hareket ÖZNEDEDİR: kadrajdaki miktar değişiyorsa özne yer değiştiriyordur.
OPTİK ARİTMETİĞİ (§5.2) — her klip için hesaplandı, sahne tablosunun OPTİK sütununda:
   kadraj eni  W = 2 · d · tan(FOV/2)      FOV = 2 · arctan(18 mm / f)
   kadraj boyu H = W · 9/16
   ana nesne   px = boy / H · 2160  (dikey) ya da boy / W · 3840 (yatay)
   ⛔ ≥100 px [D179] — 192 klibin 192'si geçti.
   ⛔ Sığmayan nesne KÜÇÜLTÜLMEZ; taşma ve ölçek şahidi yazılır [⚠️ tek.3].
NOMİNAL ÖZNEL MESAFE (kurulum kademesine göre):
   iç hacimde  9,0 / 4,0 / 2,6 / 1,2 / 1,0 m
   dışarıda    14,0 / 6,0 / 2,6 / 1,2 / 1,0 m
   Özne yer değiştirdiğinde klibe yazılan gerçek mesafe kullanılır (11 klip).
```

### 💡 Lighting Bible

```
⛔ BU FİLMDE GÜNEŞ YOKTUR. Sabitlenecek bir güneş açısı da yok; risk TERSİNE döner —
   key'siz uzay kadrajında model kendi güneşini icat eder [D201 · ⚠️6].
   Bu yüzden HER klibin `LIGHT:` satırı key'i ADI KONMUŞ BİR PRATİK olarak yazar
   ve sahne içinde BİREBİR kopyalanır [㉜⑥].

KATMAN IŞIK TAKVİMİ — dokuz katman [KART 6b · D193]

| katman | sahneler | key (adı konmuş pratik) | K |
|---|---|---|:--:|
| ① gemi içi (yörünge) | S03 · S04 · S48 · S49 | tavan paneli + amber halka | 4500 / 2200 |
| ② pod içi | S05 · S35 | pod paneli (yeşil-beyaz) | 5200 |
| ③ uzay / gemi dışı | S01 · S02 · S26 · S32 · S33 · S34 · S38 · S44 · S46 · S50 | geminin konum ışıkları | 3000 |
| ④ deniz yüzeyi | S06 | podun iniş lambaları, suda yansıyan | 5200 |
| ⑤ kıyı ve sokak | S07 · S08 · S09 · S28 · S29 · S30 · S31 | tek yanan pencere + pod lambası | 2700 / 5200 |
| ⑥ apartman | S10 | kapı altından sızan sıcak ışık | 2700 |
| ⑦ oda (filmin en sıcak noktası) | S11-S20 · S27 | masa lambası | 2700 |
| ⑧ duvar arkası ve enkaz | S21 · S22 · S23 · S24 · S25 | el feneri — tek koni, dolgu YOK | 5600 |
| ⑨ gemi koridoru ve çekirdek | S36 · S37 · S39-S43 · S45 · S47 | tavan paneli → tek acil ışığı | 4500 → 1900 |

EĞRİ: 3000 → 5200 → 2700 → 5600 → 4500 → 1900 → 0 amber
  TEK TEPE: S16 (9:20-10:00) — odanın en sıcak, en yumuşak karesi ve filmin
  duygusal orta noktası. Tepeden SONRA eğri MONOTONİK düşüyor.
  ⛔ Eğri düz DEĞİL, testere DEĞİL. Tepe bilinçli ve tek.
⚠️ Ardışık sahnede yön farkı ≤30° · K farkı ≤500 [D193] — tek istisna KATMAN
  GEÇİŞLERİDİR (S10→S11 · S20→S21 · S25→S26) ve üçü de OLAY olarak yazılıdır:
  kapı açılır · duvar açılır · gemi yakalanır.
KONTRAST [D176]: kontrast cümlesi ÖZNEYİ tarif eder —
  `a low rim light separates her helmet from whatever is behind her`
  ⛔ Zemine ya da duvara İKİNCİ BİR RENK SIFATI verilmez.
  Aynı kurulumun arka plan cümlesi BİREBİR aynıdır (sınıf 11).
```

### ⚙️ Physics Bible

```
⛔ ÜÇ REJİM, ASLA AYNI KADRAJDA [D200 · altı film `TWO GRAVITIES`]:

VAKUM (§3.1)             PHYSICS: hard vacuum, zero g, 0 kPa. Shadows are absolute
                         black with no fill. Nothing falls, nothing settles, nothing
                         drifts sideways. No sound carries outside the hull.
GEZEGEN YÜZEYİ (§3.3)    PHYSICS: planetary surface, 0,98 g, unbreathable atmosphere.
                         Dust falls fast and stays down. Fill light exists. Sound
                         carries normally. Breath fogs on cold surfaces.
BASINÇLI İÇ HACİM (§3.10) PHYSICS: pressurised interior, 1 g under spin, 101 kPa.
                         Air carries; a low fan bed under everything. Shadows soft.

GEÇİŞ KLİPLERİ [K121-K129]: rejim değişimi MEKANİK BİR SEBEBE bağlanır (pod itici
  ateşlemesi · basınç kilidi), asla sessizce değişmez.
ODA İSTİSNASI: Lena'nın odasının havası SOLUNABİLİR, dışarısı değil. Bu bir OLAY
  değil bir BULGU'dur ve ECHO K043'te ölçerek söyler.

⭐ 1 NUMARALI RİSK — SİYAH MADDE, SAYIYLA [A5 · D192]
  Tek bir gövdeden çıkan, en çok ÜÇ dala ayrılan, kolun kalınlığında, mat siyah,
  ıslak görünümlü, KATI bir yüzey. Uçları yuvarlak, kör.
  İlerleme:  on saniyede bir el genişliği (~10 cm) · sabit hız · geri çekilme YOK
  Yüzey:     0 akış · 0 dalgalanma · 0 damla · 0 parlama · 0 duman
  Kadrajda:  aynı anda EN ÇOK 3 uç
  Kesildiğinde: 1 s'de durur · 2 s'de matlaşır · 3. s'de kenardan ayrılır —
                sıvı gibi AKMAZ
  ⛔ Sıfat yetmez. OPEN CIRCUIT 1 numaralı riskini yalnız sıfatla korudu
    ("TEK, İNCE, DÜZ ve SÖNÜMLÜ") ve ekrana dallanan bir şimşek geldi.
    Negatif cümle YASAĞI söyler, BİÇİMİ söylemez; model boşluğu doldurur.
  ⛔ Yüz · göz · ağız · uzuv YOK. Madde dallanır, UZUVLANMAZ [KART 2].
```

### 🚫 Negative Bible — `KILAVUZ_REHBERI` §5.3 TAM LİSTE + bu filmin yasakları

> Havuz burada durur, PROMPTA GİRMEZ: prompt §5.1 çekirdeğini (IMAGE 7 cümle /
> VIDEO 8 cümle) + bu listeden sahne başına ≤3 cümle taşır (㉗ · tavan 11).

```
ÇEKİRDEK (§5.1) — her promptta, kısaltılmadan:
  bloom yasağı · metin/yazı yasağı · insan sayısı · film grain · çıplak deri bölgeleri ·
  ekstra uzuv/parmak · marka ve logo   (+ VIDEO'da: kamera hareketi)

BU FİLMİN HAVUZU — sahneye göre ≤3 seçilir:
  ① ÖLÇEK / MAKET       no tilt-shift look, no shallow depth of field on structures
                        larger than the pod; the frame keeps a named scale witness
                        → S32 · S33 · S34 · S46 (maket okuması en yüksek risk)
  ② MADDE               no liquid flow, no dripping, no smoke, no glow, no limbs,
                        no face and no eyes on the dark material
                        → S36 · S38 · S39 · S40 · S44 · S45
  ③ EKRAN İÇERİĞİ       no readable characters, digits, glyphs or labels on any
                        display; screens carry geometric pattern only
                        → S03 · S12 · S14 · S23 · S36 · S49  [D138]
  ④ GÜNEŞ               no sun, no sunlight, no lens flare from a star
                        → bütün ③ katmanı klipleri  [D201]
  ⑤ ÇOKLUK              no crowd, no figures in the windows, no second silhouette
                        → S31 · K119  [KART 4 · red defteri]
  ⑥ KUMAŞ               no flowing, billowing or rippling fabric
                        → S14-S16 (torba) · S11-S20 (Lena'nın kıyafeti)  [D59 · D153]
  ⑦ ZİNCİR DİLİ         (NEGATIVE'de değil, YAZIM kuralı) — ㉜⑤ BLOCK

⛔ POLİTİKA SÖZLÜĞÜ NEGATİF BLOKTA DA YAZILMAZ [SLOW STONE vakası · red defteri 11]:
   dead · body · corpse · remains · decay · frozen body · skeletal · blood · wound
   Bunların karşılığı bir yasak değil, POZİTİF BİR KİLİTTİR (§POLİTİKA).
⛔ "never drawn/aimed" kalıbı D123 tuzağıdır: yasak cümlesi yazıldı ve model onu
   ÜRETTİ. Bu planda hiçbir yasak cümlesi pozitif gövdeye girmez.
⛔ İNSANSIZ KLİPTE [red defteri · YR · COLD BURN S8]: uzun NEGATIVE bloğu tek
   pozitif `Style:` satırına iner ve boş kadraj VARLIK olarak tarif edilir [D59].
   Bu filmde insansız klip: 60 (00_SAHNE_TABLOSU IN FRAME sütunundan betikle
   sayıldı · 24.09.2026; eski elle sayım 62 diyordu).
```

---

## 🔢 SAYISAL KİLİT LİSTESİ

> Tarif değil SAYI. `02_RISK_KARTLARI.md`'nin tetiklenen her kartı buraya bir SAYI
> bırakır. 14/14 risk tetiklendi; eşik 5 → **KİLİT TAVANI ≤20** uygulandı,
> malzeme AZALTILMADI (14.09.2026 kuralı).

| kilit | sayı | risk kartı | sahne |
|---|---|---|---|
| madde dalı | ≤3 dal · ≤3 uç, aynı anda | 2 CANLI | S36 · S38-S40 · S44 · S45 |
| madde ilerlemesi | 1 el genişliği (~10 cm) / 10 s, sabit | 2 CANLI | aynı |
| madde sönmesi | durur 1 s · matlaşır 2 s · ayrılır 3. s | 2 CANLI | S45 |
| kask durumu | kapalı 192 klip · açık 0 klip · ara durum 0 | 3 KASK | tüm film |
| vizör | 1 düz panel · 1 görünür koyu çerçeve | 3 KASK | tüm film |
| kadrajdaki insan | 0 · 1 · 2 — her promptta yazılır | 4 İKİNCİ FİGÜR | tüm film |
| kimlik özniteliği | kişi başına ≤3 | 12 POLİTİKA | tüm film |
| ekran içeriği | 0 okunabilir karakter | 5 EKRAN | S03 · S12 · S14 · S23 · S36 · S49 |
| sayaç 1 · geminin yükselmesi | 3 kademe: alt → orta → üst kenar | 5 EKRAN | K061 · K096 · K119 |
| sayaç 2 · maddenin ilerlemesi | 4 kademe: saç → parmak → duvar → uç | 5 EKRAN | K062 · K096 · K136 · K151 |
| patlama | 1 kabuk · 0 alev · 0 duman · 0 kıvrım | 6 PARÇACIK | K172 |
| kaburga sayısı | 12 / şehir | 13 YAPI ÖLÇEĞİ | S07 · S26 · S29 · S34 |
| kıta halkası | 2 · sönük kopya 9 | 13 YAPI ÖLÇEĞİ | S33 · S46 |
| kabuk levhası | 4 | 13 YAPI ÖLÇEĞİ | S32 |
| halka parçası | 3 (K172'de ayrılır) | 13 YAPI ÖLÇEĞİ | S44 · S46 |
| novum lekesi | 20 mm → 194 px · fotoğraf parlaması 16 mm → 155 px | — (İPTAL KAPISI) | K070 |
| ana nesne pikseli | ≥100 px · 192/192 geçti | — (D179) | tüm film |
| ışık yön farkı | ≤30° ardışık sahnede | 6b KATMAN | tüm film |
| ışık K farkı | ≤500 ardışık sahnede | 6b KATMAN | tüm film |
| kir bölgesi | 1 bölge · 1 başlangıç klibi (K024) | 3 KASK | K024-K192 |
| mesafe eğrisi | 1,8 → 1,2 → 1,0 → 0,7 → 0,5 → 1,5 m | 4 İKİNCİ FİGÜR | S11-S27 |
| sahne içi kesme | 142 | 11 SAHNE İÇİ KESME | tüm film |
| kırpma bütçesi | 0 s (±0 kuralı) | 11 SAHNE İÇİ KESME | kurgu |

---

## 🔒 DERS KİLİTLERİ — bu filmin risk profili (⛔ en çok 20 satır — `prompt_kontrol.py` ㉕)

> Yaşayan listeden (`00_YASAYAN_DERSLER.md`) bu filme düşenler. Risk sayımı 14/14
> olduğu için tavan ≤20. Aşan kilit aşağıdaki bloğa gerekçesiyle iner.
> ⛔ Ders metni kopyalanmaz — **bu filmde ne yapılacağı** yazılır.
> ⛔ Kilit prompta ETİKETSİZ girer: `[LESSON n]` gövdeye YAZILMAZ (yazım
> disiplini dersi §1b'de, tavanın dışında).
> **Sıra risk sırasıdır.** İlk üçü `04_UYARI_NOTLARI`'nın ⛔ satırı oldu.

| ders | kilit cümlesi | nerede uygulandı |
|---|---|---|
| **D167** | Prompt gövdesinde kişi başına **en çok üç** kimlik özniteliği. Kesin boy · ten rengi · saç rengi · yaş PLAN'da kalır, prompta girmez. Yüz tarifi yalnız `IN FRAME: face` olan klipte; kalanında vizör cümlesi yeter | Mira'nın geçtiği her klip · Lena'nın geçtiği her klip (iki yüz aynı dosyada) |
| **D206** | Efor fiili olan her klipte **saniyeli ödeme satırı**: `<kanal> @ <saniye>`. Dört parça birden — destek · gövde · işaret · duraksama. Sonuç sayısı (`moves two inches`) yazılmaz | S21 kapak · S22 iniş · S29 tırmanma · S40 çekirdek · S43-S44 kol · S36 kapı |
| **D212** | Sahne tablosunun vuruş sütununda **ardışık iki klip aynı vuruş adını taşımaz**. "yürür · bakar · girer" klipleri tek tek sayılır; 192 klipte bu en kolay kırılan sayıdır | tüm film · özellikle S08 · S10 · S28 (yol) ve S12 · S16 (oda) |
| **D217** | Her repliğin İŞLEV hücresi **ekranda OLMAYAN** bir şeyi taşır. Ses kapatıldığında izleyici o bilgiyi kadrajdan alabiliyorsa replik silinir ya da görünmeyene çevrilir. ECHO dâhil | ECHO'nun bütün satırları · Lena'nın bütün satırları · özellikle K018 · K046 · K099 |
| **D214** | Her promptun ilk satırı `IN FRAME:`; SUBJECT yalnız oradakini tarif eder. Insert klibinde yüz cümlesi YOK, geniş planda yüz ayrıntısı YOK | 192 klibin hepsi · özellikle insert klipleri K070 · K152 · K182 |
| **D138** | Gösterge ve ekranın **içeriği** hiçbir yerde yazılmaz — pozitif gövdede de. Tarama, şema ve arşiv **salt geometrik desen**; okunacak şey varsa onu Mira söyler | S03 tarama · S12 tarayıcı · S14 kol ekranı · S23 arşiv · S36 şema · S49 işaretçi |
| **D207** | Sahnenin 2.+ klibinde `CONTINUOUS ACTION:` satırı önceki klibin SON durumunu taşır (㉜④). Yorgunluk 0-6, ardışık klipte en çok 1 kademe düşer | rejim gereği 142 klipte · toparlanma merdiveni S29 (K111-K113) |
| **D200** | Filmde **iki rejim** var ve asla aynı kadrajda değil: gezegen yüzeyi (Dünya benzeri) ve uzay. `PHYSICS:` satırı ortamın ADI ve SAYISI ile, sahne içinde birebir | S05-S10 · S26-S33 geçişleri · S44-S46 uzay |
| **D209** | Üç cümle BİREBİR, değişmeden: **GÖK** yıldızsız siyah, ne güneş ne ay · **UFUK** ayna gibi siyah su / ıslak bazalt · **YER İMİ** tek yanan pencere. Değişecekse bu bir OLAYDIR ve haritada yazılır (S31) | bütün dış kadrajlar: S01 · S05-S10 · S28-S34 · S50 |
| **D193** | Bu filmde güneş yok; key **adı konmuş bir pratik kaynaktır**. SPEC C: sahne başına key yönü (saat) + renk sıcaklığı (K); aynı mekânda ardışık sahnede yön farkı ≤30°, K farkı ≤500 | tüm film · S31 (bütün pencereler yanar) bir OLAY satırı |
| **D176** | Kontrast **özneyi** tarif eder: `a low rim light separates her helmet from whatever is behind her`. Zemine/duvara ikinci bir renk sıfatı verilmez | karanlıkta geçen her klip — yani filmin neredeyse tamamı |
| **D146** | Vizör **biçim + sayı** ile: tek düz panel, görünür koyu çerçeve, optik berrak. `seamless` · `dome` · `bubble` hiçbir yerde. Aracı referans paketinin kask sayfasıdır (K4 onaylandı) | Mira'nın kadrajda olduğu her klip |
| **D208** | SPEC C KİMLİK DİZİSİ tek satır: Mira kask **KAPALI** K001-K192 (ara durum yok) · şerit rengi ve tarafı · kir bölgesi K024'ten itibaren. ⚠️ Lena **kasksız ve giysisiz** — ayrım SPEC'e yazılır, yoksa kapı onu ihlal sanar | iki figürün geçtiği her klip |
| **D203** | PLAN replik tablosu = SPEC `DIALOGUE LINES` = promptlardaki tırnaklı replik sayısı. Üçü ㉓ ile karşılaştırılır; tabloya girmeyen replik prompta da girmez | replikli bütün klipler |
| **D213** | Temaslı klipte üç satır aynı klipte: **TEMAS · DEĞİŞİM · SONUÇ (≥1 s kadrajda kalır)**. Temas klibin **ilk 2 saniyesinde** kurulu gelir | K134 kenet · K165 mandal · K169 kol · K171 kapak · K177 dokunuş |
| **D211** | K001-K002 bir soru taşır ve hareketin ortasında açılır; ilk 30 s'de **en çok iki kurulum**. Son 10 s adlandırılmış bir kare + sesli siyah — kart değil | S01 · S02 · S50 |
| **D210** | K001 ile K192 **aynı kurulum** ve kamera cümlesi **birebir** aynı. TIMELINE son satırı `hold`, CAMERA `absolutely zero camera movement` | K001 ↔ K192 |
| **D141** | SPEC B FİNAL VURUŞ KANITI: **K172'de halka üç parçaya ayrılır** — tek karede sayılabilen, adı konabilen üç parça | S44 (K172) |
| **D180** | K143'ün tam sessizliği **modelden istenmez**: prompt AUDIO satırı doludur (nefes), sessizlik MUZIK dosyasındaki HARD MUTE ve kurgu bıçağıyla yapılır | S37 (K143) |
| **D192** | Bu filmin 1 numaralı riski **siyah maddenin davranışı**. Pozitif biçim sayıyla: kaç dal · ne hızla ilerliyor (bir el genişliği / 2 s) · 0 duman · 0 sıvı akış · 0 parlama | S26 · S36 · S39-S40 · S45-S46 |

```
⛔ EN PAHALI ÜÇÜ:  D167 kimlik yığını (üretimi DURDURUR) ·
                   D206 bedel bedende (doruk bir çekme eylemi) ·
                   D212 aynı vuruş (192 klipte en kolay kırılan sayı)
```

### ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar, gerekçesiyle

> Bunlar **yanlış** değil; bu filmde ayrı bir kilit satırı tutmaya değmeyecek kadar
> başka bir kilidin ya da şablonun içinde. Gerekçesiz atlama yoktur [D74].

| ders | neden bu filmde uygulanmadı |
|---|---|
| D1 | Rejimin CAMERA satırı `fixed lockoff … In a single continuous shot.` ile şablonda sabit (`COK_KLIPLI` §7); ayrı kilit satırı tavandan yer yer |
| D16 | Yüz sürekliliği D146 (vizör biçimi) + D208 (kimlik dizisi) + referans paketinin yüz sayfasıyla kapanıyor |
| D34 | Özel ad yasağı D167'nin kilit cümlesinin içinde; ayrıca negatif çekirdeğin 4. cümlesi |
| D42 | Yıpranma tek bölge + tek başlangıç klibi (K024); SPEC C satırıdır, prompt kilidi değil |
| D45 | Yazım disiplini — hiçbir sahneye düşmez, bölüm dosyasının biçimiyle kapanır |
| D62 | PLAN'ın KESİLEMEZ LİSTESİ'ne yazılıyor; kurgu/teslim kapısının işi, yazım kilidi değil |
| D70 | Kurgu kapısının kendi ölçümü (192 klip · 1920 s · ±0); prompta inen bir satırı yok |
| D78 | Sayaç kanıtı D141'in FİNAL VURUŞ kalıbıyla yazılıyor — iki satır aynı işi yapıyor |
| D139 | Sırt cümlesi D208 kimlik dizisinin içinde; `IN FRAME: back` olan klipte §5.2 eki olarak giriyor |
| D157 | Novum taşıyıcısı PLAN'ın TEK KARE cümlesinde; ⑭ betiği ayrıca ölçüyor |
| D169 | Sözlüğü D206'nın ödeme satırı zaten taşıyor; `through the glove` kalıbı D175 yüzünden kullanılmıyor |
| D172 | Tek sahnelik risk (S22'nin ipi); kilit değil, `04_UYARI_NOTLARI` satırı olarak yazıldı |
| D174 | Yön cümlesi nesne-göreli yazımı zaten her promptun kuralı; UZAMSAL kılavuz havuzdan açılacak |
| D175 | Mühür negatifi çekirdekte + D208'in Mira/Lena ayrımında; ayrı satır tekrar olur |
| D179 | V3 iskeletinin kendi kuralı (IMAGE = 0,0 s) — şablon satırı, film kilidi değil |
| D198 | Yalnız 11 klipte (K170-K180) geçerli; sahne çalışmasına not olarak iner |
| D201 | Bu filmde **güneş yok** — sabitlenecek bir güneş açısı yok (çizelgede "—") |
| D202 | ÇAPA ÜÇLÜSÜ SPEC'e yazılıyor ve D206 ile aynı kanalı ölçüyor |
| D215 | Üretim defterinin üç kutusu; yazım tarafına inen satırı yok (⚠️ ağız kadrajda — kutu ayrıca işaretlenecek) |
| D216 | MUZIK dosyasının katman tablosu; prompt kilidi değil |

---

## 🛡️ POLİTİKA SATIRI  (`03_PLAN_ONCESI` B6 · `02_RISK_KARTLARI` KART 12)

> Maliyeti sıfır, iki satır. Bunu yazan tek film redleri önceden gören tek film
> oldu (YERCEKIMI). Kural: `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md`
> ⛔ KART 12 kilit tavanının DIŞINDADIR — politika satırı her filmde zorunlu.

```
EN RED-RİSKLİ KARE:  S22 · K083 — mühürlü kabin kapağı, camında dokuz yıllık
                     kırağı; Mira eldivenini kapağa koyuyor ve ölüm kesinleşiyor
NÖTR TARİFİ:         "A sealed inner hatch with a small round pane, the pane fully
                     opaque with nine years of frost crystals. A gloved hand rests
                     flat on the metal beside the pane. Nothing is visible through
                     the pane."
                     — kadrajda beden YOK, yara YOK, yüz YOK.
                       Ölümün kanıtı kapak, kırağı ve basınç okumasıdır.
⛔ "riskli sahne yok" geçerli DEĞİLDİR — en riskli kare her filmde vardır.
```

**Alınan her politika önlemi için [POLİTİKA §4.3]:**

| ÖNLEM (ne kaldırıldı) | MALİYET (hikâyeden ne gitti) | TELAFİ (hangi kanal — §4.1) |
|---|---|---|
| Lena'nın bedeni hiç gösterilmiyor (K082-K083) | Ölümün dolaysız görsel kanıtı gitti; izleyici "belki hâlâ oradadır" diyebilir | **malzeme sonucu + alet tepkisi**: mühürlü kapak · dokuz yıllık kırağı · ECHO'nun basınç okuması (0 kPa, dokuz yıl). Üçü bir arada tek bedenden daha kesin |
| K102'de kask kilidi AÇILMIYOR, yalnız el dokunup çekiliyor | Ayartmanın en fiziksel hâli (kaskı çıkarmaya kalkışmak) gitti | **temassız gövde tepkisi**: el kilide gider, iki saniye durur, geri döner ve fotoğrafı alır. Tereddüt kanalı [OYUNCULUK §3 ③] bunu daha okunur taşıyor |
| K171'de kesilen şey bir bedene değil bir GÖVDEYE ait | "Parçalanma" dehşeti azalır | **kütle-hız**: kapak iner, gövde bir el kalınlığında kesilir, kesik uç 3 saniyede matlaşır. Ses kanalı da taşıyor (metal + kuru çatırtı) |
| Kalabalık yok — K119'da pencereler yanıyor, figür yok | "Binlerce izleyen göz" imgesi gitti | **malzeme sonucu**: pencereler aynı anda ve aynı sıcaklıkta yanıyor; tekilliğin yokluğu tehdidi büyütüyor. Kadrajda insan sayısı 1 kalıyor [KART 4] |

```
⛔ TELAFİ sütunu boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.
   Dört kanal: kütle-hız · malzeme sonucu · alet tepkisi · temassız gövde tepkisi
   — dördünün dördü de kullanıldı ✅
⛔ Milliyet · gerçek kurum · gerçek kişi adı bu planın HİÇBİR YERİNDE geçmez.
   VELA ve ECHO uydurma adlardır ve PROMPT GÖVDESİNE GİRMEZ [D34].
```

---

## 🧪 ÜRETİM ÖNCESİ DENEMELER — P0-P3 (sahip kararı 23.09.2026: YAZIMDAN ÖNCE)

> ⛔ **Bu denemeler yazılım tarafından koşulamaz.** Ölçütleri insan izleyici ve
> kare üretimi gerektiriyor. Aşağısı koşulabilir hâle getirilmiş hâlleridir;
> sonuçları `THE_FALSE_EARTH_URETIM_DEFTERI.md`'ye yazılır.
> ⚠️ P0 video ÜRETMEZ (durağan kare + geçici ses). P1-P3 video üretir.

| # | ne | kapsam | ölçüt | durum |
|:--:|---|---|---|:--:|
| **P0** | İlk 10 dakikanın ritmi · K001-K060 | sesli kaba kurgu: klip başına tek durağan kare (eskiz ya da üretilmiş imaj) + geçici seslendirme + ses efekti + müzik yatağı | ① izleyici 10 dakikayı durdurmadan izler; ilk dikkat kaybının dakikası yazılır ② her sahnenin sonunda neyin değiştiğini tek cümleyle söyleyebilir; söyleyemediği sahneler listelenir ③ 10:00'da "neden gemiyi indirdi?" sorusuna HESAPLA cevap verir (torba, süre) ④ "Mira'ya kızdın mı?" — erteleme sabır tüketiyor mu ⑤ yalnız görüntüyle okunması gereken beş klip (K017 · K022 · K029 · K044 · K056) sessiz izlemede de fark ediliyor mu | ⬜ |
| **P1** | Açılış S01-S02 · K001-K004 | tam sahne, video | ① berrak vizörde yansıma ve yüz aynı karede okunuyor ② kara gezegen telefon ekranında bir leke değil, bir küre ③ ilk 10 s'de "bu ne?" sorusu doğuyor ⭐ ayrıca ÖN-OTOPSİ'nin birinci YÜKSEK×YÜKSEK hücresini ölçer: kimlik özniteliği ≤3 ile yüz tutuyor mu | ⬜ |
| **P2** | Oyunculuk S18 · K065-K068 | tam sahne; iki kişi, iki yüz | **ana ölçüt:** izleyici açıklama almadan (ECHO yok, altyazı yok) Mira'nın şüphesinin BÜYÜDÜĞÜNÜ hissediyor. "Mira ne hissediyor?" → "şüpheleniyor" / "inanmak istemiyor". Destek: ① bakış Lena'dan tarayıcıya iniyor (K068) ② cevaptan önce görünür duraklama ③ göğüs ve omuz ritmi K065→K068 arasında değişiyor ④ Lena'nın adımı (K067) kadrajda ölçülebiliyor ⑤ Lena'nın yüzü dört klipte aynı kişi. ⛔ Dört klipte aynı donmuş poz = BAŞARISIZ, durum kilidi tutmuş olsa bile | ⬜ |
| **P3** | Ölçek S33 · K125-K129 | tam sahne | ① pod, halka ve gemi arasındaki oran beş klipte tutarlı ② ışık ve fizik satırları BİREBİR olduğu hâlde kurulum değişiyor (sahne kilidi çalışıyor) ③ halka bir canavar değil, bir YAPI olarak okunuyor ④ K127'deki karanlık küçük halkalar seçilebiliyor (K180 onlara dayanıyor) ⭐ ÖN-OTOPSİ'nin ikinci YÜKSEK×YÜKSEK hücresini ölçer | ⬜ |

```
⛔ SIRA: P0 → (gerekirse sahne haritası düzeltilir) → P1 · P2 · P3 → kalan promptlar.
⛔ P1 ve P3 iki YÜKSEK×YÜKSEK ön-otopsi hücresine bağlıdır; ikisi de BAŞARISIZ
   dönerse konsept REVİZE edilir, 192 prompt yazılmaz.
⛔ PROB B (lip-sync / konuşan ağız · KART 7 · D215) P2'nin içinde koşar:
   S11-S20'nin klipleri PROB B geçmeden ÜRETİLMEZ.
⚠️ Denemeler için gereken promptlar: K001-K060 (bölüm 1-5) · K065-K068 · K125-K129.
   Kalan 123 klibin promptu denemeler sonuçlanmadan yazılmaz.
```

## ⬜ SAHİP KARARI BEKLEYEN ÜÇ MADDE

> Üçü de ön plandan (00_ON_PLAN/02_ON_PLAN.md) devrediyor. Yazım önerilen
> varsayılanlarla ilerliyor; karar farklı gelirse etkilenen yer tek satırda yazılı.

| # | soru | yürüyen varsayılan | karar farklı gelirse ne değişir |
|:--:|---|---|---|
| **K1b** | 10 s'nin altına inen klibe izin var mı (kurguda kırpma)? | HAYIR — 192 × tam 10 s, kurgu kapısı ±0 s | SPEC A RUNTIME satırı + kurgu kapısı yeniden yazılır; klip sayısı değişmez | ⬜ |
| **K9** | Mira ve Lena'nın yaşları | yazılmıyor — yaş PLAN'da da yok, prompta da girmiyor [D167 tavanı] | Character Bible'a bir satır; prompta YİNE girmez | ⬜ |
| **K10** | Anne kadrajda görünecek mi? | HAYIR — yalnız SES, kaydın içinden (K011 · K159 · K189) | üçüncü bir kimlik sayfası (RK4) ve KART 4 insan sayısı kilidi yeniden yazılır | ⬜ |
