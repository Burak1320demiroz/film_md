# 🧠 BLIND_ORBIT — KONSEPT VE RİSK

> Girdi: sahibin talebi (`00_ON_PLAN/BLIND_ORBIT_SAHIP_PLANI.md`) + `01_QA_DERS_HASADI.md`.
> ⛔ Konsept kapısının üçü de ✅ olmadan `03_SAHNE_SIRALAMASI.md` yazılmaz.

---

## 0. 🗳️ AÇILIŞ SORULARININ CEVAPLARI — akışın girdisi

```
① KONU:     sahip verdi — tam tretman + 24 kliplik çekim planı (05.10.2026)
② FORMAT:   yatay 4 dk          → kart §2.3 · bölüm sayısı 2 (12 + 12)
③ SAHNE:    24 KLİP × 10 s      → formatın varsayılanı (çok klipli rejim: kartın "24 sahne"si = 24 klip)
            SAHNE sayısı hikâyeden: 6 · SAHNE PLANI 2 6 4 6 4 2 (sahibin bölümlemesi, birebir)
   ⛔ Bandın içinde; izin gerekmiyor.
④ REFERANS PAKETİ: YAZILSIN (sahip, 05.10.2026) → KAPI 0; §5b tablosu bilgi için dolduruldu
⑤ HİKÂYE ONAYI: `00_HIKAYE_ONAYI.md` ONAY 05.10.2026 · TUR 1/3
⑥ FİKİR TURU KAYDI — 0.7a KOŞMADI (hikâye sahibin; gerekçe onay dosyasında NOT)
   GERİLİM CÜMLESİ:  Pilot gemiyi ayrılmak üzere olan dönen istasyona kenetlemek istiyor,
                     ama son metreleri göremiyor, çünkü yanaşma kamerası tam hizada kararıyor.
   ENGEL TİPİ:       ortam (motor/itici/istasyonun ayrılışı) + ilişki (son metre ancak
                     ötekinin gözüyle geçilir)
   DUYGU ADI:        "teslim olan kontrol" · kademe çift-duygu (korku + güven aynı anda;
                     K18'de el gevşerken nefes tutulu)
   ÜÇ YÖNTEM:        yapısal — sahibin planı (fikir turu yok) · çağrışım — — · tersine — —
   DOYUM (§8):       en yakın iki film: THE_HARD_DOCK (4 dk · tek kişi · hasarlı istasyona
                     kenetlenme · dört dikme) · THE_COLD_BURN (iki kişi · iki araç · dönüş
                     eşleme planlanmış ama hiç ekrana gelmemiş).
                     FARK: kör yaklaşma (görüntü kanalı kapanıyor) + iki insan arasında tek
                     görev ikiye bölünmüş (el ↔ göz) + kara delik ölçeği + dönüş eşlemesi
                     filmin İMZA planı olarak üretimde İLK halka.
   ÖLDÜRÜLEN GÖZDE:  A'ya karşı üç satır onay dosyasında (benzer film · güvenin bedeli
                     görünmüyor · replik yoğun) · sonuç: A kaldı (K18 güven anı eklendi)
```

## 1. 🎯 SAHİBİN TALEBİ — birebir

```
TALEP: "bu filmi yapalım /yeni-film" — ekte BLIND ORBIT tretmanı ve 24 kliplik plan
       (tam metin: 00_ON_PLAN/BLIND_ORBIT_SAHIP_PLANI.md — kelimesi kelimesine)
REPLİK: VAR — 13 insan repliği + 2 dış ses satırı (plan §3, §5)
        → AYRI kapı zinciri açık: SES_VE_DIYALOG §1a-§2a + DIYALOG_SAHNESI +
          DIALOGUE_CRITIQUE_PROMPT (Kart P 2b)
```

**Talep fizikle/depo kurallarıyla çelişen yerlerde yeniden tanım — sapma AÇIKÇA:**

| sahibin isteği | sorun | yeniden tanım | gerekçe kaydı |
|---|---|---|---|
| "35 mm sinema hissi, **anamorfik** kompozisyon" | vakumda anamorfik yatay parlama fiziksel olarak yanlış (`KILAVUZ_REHBERI` §3.1 Lens satırı); "anamorphic" kelimesi parlama çağırır | geniş 16:9 kompozisyon + KÜRESEL lens; "anamorphic" promptta 0 | §3.1 · YANAŞMA §1.2 (küresel) |
| Hook K01–K02 "K05/K20 · K16/K18/K14 kaynaklarından **montaj**" | tek klip = tek çekim [D1]; klip içi montaj kesmedir; çok klipli rejimde her klibin kendi IMAGE'ı var | K01 ve K02 KENDİ görüntüleriyle üretilen ileri-sıçrama klipleri (K01 dış · K02 iç); sonuç saklanır | onay dosyası NOT ④ (sahip onayladı) |
| "**Yüz görünüyorsa dudak hareketi sesle eşlenir**" | ekranda konuşan ağız = lip-sync + AI damgası (KART 7 · SES §1a ②); kapalı vizörde replikli üretim cama ağız çizer (DIYALOG §7) | konuşan ağız kadrajda 0: replik telsizden; yüzü görünen DİNLEYENDİR ("lips closed") | onay dosyası NOT ② |
| "**özgün rozetler**" | yüzeyde okunur işaret/arma metne kayar [D138 · DONANIM §0②] | yazısız kabartma ŞEKİL rozet (Lena: altın kanat · Noah: kobalt altıgen) — harf/rakam 0 | onay dosyası NOT ③ |
| D01 "Main drive is dead. **Vesper** burns in **three minutes**." | özel ad promptta tabela olur [D34]; sayı insan ağzında [D82]; "dead" politika sözlüğü (POLİTİKA §2.2) | Noah: "Main drive's gone." + MAKİNE sesi: "Station burn in three minutes." | ☑ SAPMA 1 — sahip onayladı 05.10.2026 (onay dosyası) |
| D07 "**Docking camera is gone.**" | ekran zaten kararmış görünüyor — replik görüneni söylüyor [D217] | Lena: "I can't see the collar." (görünmeyeni söyler; K17'de Noah'nın "I can see the collar." cevabı) | ☑ SAPMA 1 — sahip onayladı 05.10.2026 |
| D12 "**Hard capture confirmed.**" | dört kilit kadrajda kapanıyor — durum okuması [D217] | replik SİLİNİR; yerine K22'de MAKİNE: "Station burn in ten seconds." (görünmeyen süre baskısı) | ☑ SAPMA 1 — sahip onayladı 05.10.2026 |
| Hook dış sesi geçmiş zaman ("Our main engine **was** gone…") | geçmiş zaman anlatıcının hayatta kaldığını söyler → NEDEN İZLENİR sorusunu ilk 10 s'de cevaplar (HOOK §6 vaat-teslim) | şimdiki zaman, uçuş kaydı/telsiz sesi: "Main engine's gone. The station's leaving." · "We have to match its spin— and dock without a camera." | ☑ SAPMA 1 — sahip onayladı 05.10.2026 |
| "Yanaşma kamerası **kararır**" (K16 içinde) | klip içinde durum değişimi ölçülmüş en zayıf eksen (REHBER §7 · 0,0687) | K11'de ekran titrer (oran); kararma K15/K16 SINIRINDA; K16 ekran zaten siyah açılır | `SAHNE_ZINCIRI` §1 · D179 |
| "İstasyonun motorları **yanar**" (K23 içinde) | aynı — ateşleme bir durum değişimi | K22 sonunda gövdeden gelen titreşim BAŞLAR (oran); K23 motorlar ZATEN yanarken açılır | aynı |
| Vakumda "dört kilidin **sesi ayrı duyulur**" | vakumda dış ses 0 (YANAŞMA §2.1) | sesler KOKPİT İÇİNDE, gövdeden taşınan dört ayrı vuruş — dış klipte yalnız telsiz yatağı | sahip planı da "kokpitin içinde duyulur" diyor — uyumlu |

## 2. 🗺️ KARTLAR — `KILAVUZ_REHBERI` §2/§3/§4

```
FORMAT:        yatay 4 dk (§2.3) · çok klipli sahne rejimi (§2.0b)
ORTAM:         §3.1 VAKUM (dış) + §3.10 BASINÇLI İÇ HACİM · §3.10b TAM MİKROGRAVİTE
               → tek PHYSICS satırı iç + dış (PROMPT_HATA §3.10b · THE_LAST_GATE emsali)
               → tetiklediği zorunlu satırlar: dış ses 0 · gölge mutlak siyah · egzoz düz
                 koni · anamorfik parlama yok · iç: hava taşır (nefes, fan) · ekran soyut
                 (METİN RİSKİ §3.10) · 0 g'de yürüme yok, tutamaktan çekilme
TÜR:           bilimkurgu · dal: kurtarma/yanaşma gerilimi · kozmik ölçek  → §4.1
KLİP SÜRESİ:   10,0 s plan · ⬜ ARAÇTAN ÖLÇÜLECEK [D124] (K1 açık işi — ilk üretilen klipte ffprobe)
SAHNE SAYISI:  6 sahne / 24 klip · RUNTIME 24 × 10 = 240 s = 4:00 (hook 24'ün İÇİNDE)
BÖLÜM SAYISI:  2 (BOLUM_1 = S1+S2+S3 = 2+6+4 = 12 klip · BOLUM_2 = S4+S5+S6 = 6+4+2 = 12 klip)
```

### 2.1 Sayısal dünya — METRE BURADA, PROMPTTA DEĞİL [D138 · UZAY_USSU §1]

```
LARK (küçük gemi)   26 m uzun · ~6 m çap · iki kişilik · kenet halkası burnun ALTINDA,
                    uzun eksene paralel, ileri bakar · kokpit penceresi burunda
                    · iskele (sol) itici kümesi hasarlı — K03'ten film sonuna kadar sabit
                    · içeride: kokpit → ~6 m servis geçidi → kesme vanası → ~2 m ileride
                      optik gözlem noktası (küçük yuvarlak pencere + retikül + destek koltuğu)
VESPER (istasyon)   ~900 m uzun · merkezi gövde ~40 m çap · ÜÇ koyu radyatör kanadı
                    (120° aralı, her biri ~80 m, toplam radyal açıklık ~200 m)
                    · tek eksenel kenet halkası gövdenin ön ucunda, dönüş ekseninde
                    · ana motor kümesi arka uçta
DÖNÜŞ               1,5 RPM → bir tur 40 s → 9°/s → 10 s'lik klipte ÇEYREK TUR (90°)
                    · kenet halkası eksende: halka yerinde döner, çember çizmez
                    · K14-K15'te LARK aynı hızla döner → gövde kamerasında istasyon durur,
                      kara delik ve halkası çeyrek tur/10 s döner
KARA DELİK          kurmaca süper kütleli · siyah gölge + ince kehribar toplanma diski +
                    üstte/altta merceklenmiş yay · kadrajın üst yarısında, istasyonun
                    ARKASINDA, yönü sabit (dış kliplerde "upper left behind the station")
GERİ SAYIM          yanışa kalan: 00:20 → 3:20 · 00:40 → 3:00 · 01:50 → 1:50 · 02:40 → 1:00 ·
                    03:10 → 0:30 · 03:30 → 0:10 · 03:40 → 0:00 (ekranda RAKAM YOK — makine sesi
                    + konsoldaki tek kehribar çizginin kısalması)
YAKLAŞMA MESAFESİ   K03-K07 ~120 m (bekleme) · K13-K15 120 m (eksende, dönüş eşlenirken
                    mesafe korunur) · K16 ~100 m · K17 ~60 m · K18 ~20 m · K19 ~2 m → 0,3 m ·
                    K20 temas (bağıl hız ~0,05 m/s) — kurmaca hızlandırılmış son yaklaşma
                    (gerçek yanaşma ~0,1 m/s; 120 m / ~50 s ortalama ~2,4 m/s, frenle) —
                    SPEC'te "kurmaca tasarım kabulü" olarak ilan edilir
```

## 3. 🧩 ÖNERME VE NOVUM — konsept kapısı (`ONERME_VE_NOVUM_KILAVUZU` §4)

```
NOVUM TİPİ:          İLİŞKİ (üçüncü tercih — §1; deponun ikinci ilişki filmi, ilki
                     THE_FALLING_WORLD · aynı tema GÜVEN). Gerekçe: filmin fiziği GERÇEKÇİ
                     (dönüş eşleme, yumuşak/sert yakalama); tek "yeni kural" bir insanın
                     ötekinin gözüyle gemi sürmesidir. Fizik novumu EKLENMEZ (06 §5 "ASLA").
NOVUM:               Son metrelerde gemiyi süren el, onu göremeyen el; gören göz, gemiyi
                     süremeyen göz — kenetlenme ancak ikisi tek hareket olunca olur.
NOVUM TAŞIYICISI:    kenet halkası (Noah'nın optik penceresindeki retikülün ortasında)
                     × Noah'nın vizörünü pencereye yaklaştırıp sol eldiveninin iki parmağını
                     iskele yönüne kaldırması ↔ Lena'nın kararmış yanaşma ekranından başını
                     çevirip sağ eldivenini kumanda kabzasında gevşetmesi
                     → halka ile kenet arasındaki boşluk kapanır (K18-K20)
① TEK KARE:          ✅ K16 — kokpitte KARARMIŞ YANAŞMA EKRANI (yanık konsolun ortasında tek
                     siyah dikdörtgen) + pencerede istasyonun gövdesi pencereyi dolduracak
                     kadar yakın: "kör ama çok yakın" 1 saniyede okunur. İkinci kare K18 —
                     retikülün ortasında KENET HALKASI, vizör pencereye eğik.
                     (taşıyıcı nesne adları cümlede: yanaşma ekranı · kenet halkası [D157])
② KİNETİK BAĞIMSIZLIK: ✅ (şartlı) — replik olmadan: K16 siyah ekran + Lena'nın eli kumandadan
                     çekilir · K17 Noah kendini pencereye bağlar · K18 Noah'nın iki parmağı
                     iskeleyi gösterir, kesmede Lena'nın eli o yöne küçük düzeltme yapar ·
                     K19 boşluk kapanır. Kural (o görür, bu sürer) EYLEMLE okunur; replik onu
                     hızlandırır, taşımaz. Şart: K18'de iki parmak kadrajda ≥ ⅛ kısa kenar.
③ BAŞLIK ŞEMASI:     ✅ "Docking Blind" (2 kelime) — izleyiciye karanlık ekrana ve kapanan
                     boşluğa bakmasını söyler. (Film adı BLIND ORBIT aynı şemayı taşır.)
⛔ Üçü de ✅ → konsept GEÇTİ.
KURAL TEKRARI (§5):  kurulum K08 (Lena kendi elini Noah'nın önerisine bırakır — vana) ·
                     doğrulama K12 (Noah rezervi okur, Lena dönüşü seçer — onun okuduğuna
                     göre) · sonuç K18-K19 (kör yaklaşma) · ≥3 sahne · ≥2 nesne
                     (vana çarkı · kenet halkası/retikül)
```

### 3.1 Novum kilidi — taşıyıcı hangi SAYIYLA ve hangi promptlarda [PROMPT_HATA §5]

```
K15  "the collar and the three dark fins hold still at frame centre while the black hole
      and its amber ring turn a quarter of the way around the frame in ten seconds"
K18  "the collar sits inside the cross-hairs of the small round window, a hand-width off
      centre toward the left thruster side" (retikül = iki ince çizgi, oyulmuş, sayısız)
K19  "the gap between the two collars closes from about one body-length to about a
      hand-width over the ten seconds, at one steady rate"
K20  "the two collars touch at 3.0 s, the soft ring gives a finger's width and holds"
K21  "exactly four hard latch hooks swing over and seat, one after another"
```

## 4. 🎭 TEMA — `TEMA_MUHENDISLIGI` §3 sekizlisi

```
▸ tema adayı — GÜVEN (aday etiket · §3b · sahibin kendi seçimi; depoda 1 kez —
                THE_FALLING_WORLD; sayac.sh 🎭 TEMA DAĞILIMI "GÜVEN 1")
▸ tanım cümlesi — Göremediğin son metrede başkasının gözü senin gözün olur.
                  (TANIM; takas kalıbı DEĞİL — "X için Y'den vazgeçilir" yok)
▸ §4 süre-tatmin — yatay 4 dk = SÜREÇ teması ✅ (güven kurulup K18'de bedel ödenerek
                  verilir; anlık durum değil)
▸ motif kanalları — EL (kumanda kabzası: sıkı → gevşek) / KAMERA (Lena'nın yüzü ekrandan
                  pencereye/sese döner) / NESNE (kararmış ekran ↔ optik pencere) / SES
                  (makine sayar, insan yönetir)
▸ motif sahneleri — K04 (sıkı kabza) · K08 (erteleyip bırakan el) · K12 (onun okuduğuna
                  göre seçim) · K18 (el gevşer — CHOICE) · K19 (yalnız ses) · K24 (açık el)
⚠️ ÖRÜNTÜ UYARISI (TEMA §3b): aday etiket üretimi kolaylaşıyor; bu film YENİ etiket
   üretmiyor, var olan GÜVEN'i ikinci kez kullanıyor — kart Y ölçümüne ikinci film.
```

## 5. ⚠️ RİSK KARTLARI — `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md`

| kart | tetiklendi mi | neden | tasarımla düşürüldü mü | kalan risk |
|---|:--:|---|---|:--:|
| 1 su/sıvı | ✗ | sıvı yok | — | — |
| 2 canlı | ✗ | canlı yok | — | — |
| 3 kask/vizör | ✓ | iki basınç giysisi, vizör 24/24 kapalı | HELMET STATE: kapalı K01-K24 · açık 0 · R1/R2 paneli | 🟠 |
| 4 ikinci figür | ✓ | iki insan + klon riski (D20) | 22 klipte kadrajda en çok BİR insan; iki insan yalnız K04 (konum kilidi + "Exactly 2") | 🟡 |
| 5 ekran/sayaç | ✓ | yanaşma ekranı · geri sayım · rezerv | ekranlar soyut (siyah dikdörtgen · tek kehribar çizgi); sayılar makine SESİNDE; A1 çelişkisi yok | 🟠 |
| 6 parçacık | ✓ | hasarlı itici jeti vakumda | "a short straight cone that thins and is gone" — kıvrılma 0; jet K10'dan sonra 0 | 🟡 |
| 6b katmanlı dünya | ✗ | tek bölge (yörünge) | — | — |
| 7 diyalog | ✓ | 15 replik (sapma sonrası) | basamak 1 kadraj dışı ses; konuşan ağız 0; sayı makinede | 🟠 |
| 8 kamera | ✓ | K14/K15 gövdeye bağlı (dönen) kamera | gövdeye kilitli LOCKOFF — gövdeye göre sıfır hareket; dönen şey arka plan | 🟠 |
| 9 tek baskın ışık + hedefe hareket | ✓ | kara deliğin kehribar halkası tek ışık; LARK hedefe ilerliyor | ışık mıknatısı hedefle AYNI yöne konur (kara delik istasyonun arkasında) + dört kanal yazılı | 🟡 |
| 10 insansız sahne + uzun negatif | ✓ | 9 insansız dış klip (ölçüm 05.10: K01 K03 K05 K07 K13 K15 K20 K21 K24) | NEGATIVE dört cümle, "0 human" kalıbı yok (SIGNAL_KEEPERS emsali) | 🟡 |
| 11 değişken çekim süresi | ✗ | sabit 10 s ızgara, kırpma yok | TARGET ASL 10,0 s sabit | — |
| 12 politika yüzeyi | ✓ | ikinci insan · tehlike çerçevesi (hasar, kaçak, sapma) | sözlük: damaged/emergency/danger/collision/dead/explosion 0 · nötr tarif | 🟡 |
| 13 büyük yapı | ✓ | 900 m istasyon + 26 m gemi | ANATOMİ KARTI · ölçek merdiveni tek nesne (kenet halkası) · iki gövde aynı karede yalnız K05 + K13 | 🟠 |

```
TETİKLENEN RİSK:  10 / 14
EŞİK:             5  → KİLİT TAVANI ≤ 20 (14.09.2026 kuralı) — malzeme AZALTILMADI
                  20 kilit 01 §1'de · 17 ders §1b UYGULANMAYAN KİLİTLER (gerekçeli)
```

### ⭐ A5 — 1 NUMARALI RİSK SAYIYLA YAZILIR [D192 · `03_PLAN_ONCESI` A5]

```
1 NUMARALI RİSK:  K15 DÖNÜŞ EŞLEMESİ (imza planı) — model ya istasyonu döndürür ya kara
                  deliği dondurur ya da ikisini birden yavaş döndürür; COLD BURN'de bu
                  vuruş hiç ekrana gelmedi, HARD DOCK'ta dönme açısı kesmede 45° sıçradı
POZİTİF BİÇİMİ:   "the collar and the three dark fins hold still at frame centre for the
                  whole take while the black hole and its thin amber ring turn a quarter of
                  the way around the frame in ten seconds, in one steady direction (the
                  direction the fins were turning in the clip before), never reversing"
                  → SAYI: çeyrek tur · 10 s · 3 kanat · tek yön
                  SPEC göz kapısı: K15 0,0 s ve 9,9 s kareleri — kanat açısı farkı ≤ 10°,
                  kara delik halkası eğim farkı 70-110°
İPTAL KAPISI:     K15 iki üretimde bu ölçüyü tutmazsa üçüncü yeniden yazım YOK —
                  kamera dış kuruluma taşınır (V3 · iki gövde, yandan): K13 kurulumunda
                  "LARK'ın gövdesi ve istasyonun kanatları AYNI hızda dönüyor" ikinci
                  kanıt olur; imza "duran halka" değil "birlikte dönen ikili" olur.
```

### 🪦 ÖN-OTOPSİ — "film çekildi ve izlenmedi, neden?" [`HIKAYE_FIKIR_TURU` §8]

| arıza modu | olasılık | etki | önlem / öldür |
|---|:--:|:--:|---|
| kanal tezi (`apexaic/README.md`) | düşük | orta | uzay · kozmik ölçek · gerilim — kanalın merkezinde; tehlike: "yine bir kenetlenme filmi" (HARD DOCK) → kapak/başlık kör yaklaşmayı satar ("DOCKING BLIND"), istasyonu değil |
| politika / red (`09_URETIM_RED_DEFTERI`) | orta | orta | ikinci insan + hasar + kara delik; sözlük temiz, kask açılmaz, kalabalık yok · insansız klipte kısa negatif |
| üretim tek-hata noktası (biçim kilidi · kask · metin) | **yüksek** | **yüksek** | **K15 dönüş eşleme** + K20-K21 temas/kilit → RİSK KARTI olarak yukarıda (A5) · referans paketi RB/RO KAPI 0 · üretim sırasının ilk dört halkası · İPTAL KAPISI yazılı |
| tutundurma (ilk on saniyede soru · son on saniyede çıkış) | orta | yüksek | K01 0. kare: kara delik önünde dönen dev yapı + minik gemi → "yetişecek mi?" · K02 kararmış ekran → ikinci bilgi · son kare iki ışık dizisi birlikte (adlandırılmış) |
| doyum (§8 matris — yakın film) | orta | orta | THE_HARD_DOCK + THE_COLD_BURN → fark onay dosyasında ve §0⑥'da yazılı; iki insan + güven ekseni + kör yaklaşma |

```
KARAR: GO — tek yüksek × yüksek hücre (K15/K20-21) risk kartı + iptal kapısı + üretim sırası
       ile önlendi; onaylı metne dokunan revize YOK.
```

## 5b. 📦 REFERANS PAKETİ TETİKLEYİCİLERİ — sahip "YAZILSIN" dedi; tablo kayıt için

| # | tetikleyici | doğru mu | hangi varlık / sahne |
|:--:|---|:--:|---|
| T1 | kask · vizör · basınç giysisi | ✓ | Lena (RK1) · Noah (RK2) — 14 klipte kask kadrajda |
| T2 | biçim kilidi METİNLE tutulmayan varlık | ✓ | vizör geometrisi (D146) · VESPER'in üç kanatlı silueti |
| T3 | oranı sözle yazılamayan nesne | ✓ | LARK (RA) · VESPER (RB) · kokpit (RI1) · servis/optik bölme (RI2) |
| T4 | insan dışı canlı | ✗ | — |
| T5 | tekrar eden insan dışı olay | ✓ | kenetin iki aşaması (RO: yumuşak halka + dört kanca) · itici jeti (K03-K10) |
| T6 | bir varlık tekrar tekrar dönüyor | ✓ | VESPER dönüşü 11 dış klipte (HARD DOCK'ta açı sıçradı) · kara delik (RD) |

```
KARAR: YAZILIR (sahip kararıyla aynı) — sayfalar: RK1 · RK2 · RA (+ hasarlı hâl) · RB ·
       RI1 · RI2 · RO · RD = 8 sayfa (sahibin "sekiz temel referans" önerisiyle birebir)
⛔ KAPI 0: sayfası ONAYLI olmayan ve seed'i yazılmayan varlığın geçtiği hiçbir klip üretilmez.
```

## 6. 🛡️ POLİTİKA SATIRI — `03_PLAN_ONCESI` B6 · KART 12

```
EN RED-RİSKLİ KARE:  S2 · K03 — hasarlı gemi + kaçan gaz jeti + karanlık ana motor,
                     kara deliğin önünde (tehlike çerçevesi yoğun)
NÖTR TARİFİ:         "a small off-white ship drifts sideways in the dark; near its left
                     thruster cluster the hull is opened along one seam, the edges cold
                     and torn, and a short straight jet of gas leaves it and thins out
                     within a hull-length; the main engine bell at the stern is unlit"
⛔ yazılmaz: damaged · wounded · emergency · danger · collision · crash · impact · dead ·
   explosion · fire · glow · burning
İKİNCİ:              S2 · K07 sapma ("drifts sideways toward the station's flank and
                     stops a hull-length short" — "collide/crash" yok)
```

| ÖNLEM | MALİYET | TELAFİ |
|---|---|---|
| "çarpışma" kelimesi ve temas tehdidi görüntüsü kaldırıldı (K07) | yakın-çarpışmanın doğrudan şiddeti | KÜTLE-HIZ kanalı: gövdenin istasyon kanadına bir gövde boyu kalana kadar kayması + iticilerin karşı ateşi; ALET kanalı: rezerv çizgisinin kısalması; GÖVDE kanalı: Lena'nın kilitlenen önkolu |
| konuşan ağız kaldırıldı (13 replik telsizden) | yüz-söz senkronunun yakınlığı | DİNLEYEN kadrajı — yüz cevabı bedende verir (Kuleshov); ses bedensiz otorite taşır (Chion) |
| kask/eldiven hiçbir klipte açılmaz | finalde "ilk yüzler" kasksız rahatlama vuruşu | final rahatlaması vizör ardında yüz + açılan el + fısıltıyla; kasksızlık yok (sahibin planı da kaskı açmıyor) |

## 7. 🧭 B5 — HİKÂYE OMURGASI (sahne haritasından ÖNCE)

```
İSTEK:   LARK'ı ayrılmadan önce VESPER'e kenetlemek — film başlamasa da var olan iş
         (eve dönüş: istasyon ayrılırsa onu izleyecek motorları yok)
ENGEL:   ana motor yok · iskele itici hattı açık kalmış gemiyi eksenden kaçırıyor ·
         istasyon döndüğü için dönüş eşlenmeden yanaşılamaz · yanış 3:40'ta ·
         son metrede yanaşma kamerası kararıyor (görüntü kanalı kapanır)
BEDEL:   ① S2 · K07 — Lena kendi gözüyle yaptığı düzeltmede çarpışmayı önlemek için geri
           çekilme payını harcar: ikinci yaklaşma yok (rezerv çizgisi kısalır, eller
           kumandada kilitli kalır)
         ② S3 · K10 — Noah iskele itici grubunu vanadan kalıcı kapatır: gemi bir manevra
           grubunu sonsuza dek kaybeder
         ③ S4 · K18 — Lena kendi gözüyle sürme alışkanlığını bırakır (el gevşer — CHOICE)
MUHATAP: ikinci insan — Noah, çoğunlukla kadraj dışında, telsiz sesi olarak
AYRILIK: S2 · K08 — Noah hattı kapatmayı önerir; Lena 1,2 s cevap vermez, eli kumandada
         kalır (ERTELEME hücresi) sonra "Do it."
         S4 · K18 — Lena'nın sağ eldiveni kendi gördüğüne göre düzeltmeye uzanır; Noah
         aynı komutu daha alçak sesle tekrarlar (≥0,7 s gecikmeyle); el gevşer (RET →
         UYMA — tersinmiş ikinci ayrılık: K08'de bekleten Lena, K18'de bırakan Lena)
```

### 7.1 İSTEK ÇAPRAZI [`IKI_KISI` §3]

```
Lena, Noah'dan ŞUNU ister:  hattı kapatıp ona kalan iticilerle tek temiz yaklaşma vermesi (K08)
Noah, Lena'dan ŞUNU ister:  son metrede kendi gözüne değil onun sesine göre sürmesi (K18)
NESNE:                      Lena'nın T-kabzalı kumanda kolu — K08'de Noah'ya bırakmadığı,
                            K18'de onun sesine bıraktığı şey
```

### 7.2 KARAR MİMARİSİ [`KARAKTER_KARTI` §3]

```
İKİ SEÇENEK KADRAJDA (K18):  ① kendi gözü — pencerede istasyon gövdesi + konsolda KARARMIŞ
                             yanaşma ekranı · ② ses — telsiz (kadraj dışı) + Noah'nın
                             iskele işareti (kesmede). REDDEDİLEN NESNE: kararmış ekran —
                             K18'de kadrajda, K19-K22'de de orada, siyah kalır.
BAŞARISIZ DENEME:            K06 (kendi düzeltmesi, gemi yine sola çekilir) · K07 (çarpışma
                             önlenir ama pay tükenir) — her deneme yöntemi değiştirir
                             (K06 büyük düzeltme · K07 kesip geri çekilme)
BEDEL PENCERESİ:             K07 anlık (aynı klipte rezerv çizgisi kısalır) · K10 stratejik
                             (bir grup sonsuza kaybolur; dramatik ironi penceresi K11'de açılır:
                             izleyici ekran titremesini Lena'dan önce görür)
HOBSON SATIRI:               K10 Noah için tek seçenek (vana) — seçilen şey TEMPO (iki deneme)
```

## 8. 👤 KARAKTER KARTLARI — B5'ten SONRA [`KARAKTER_KARTI` §1 · `IKI_KISI` §2]

> Kart PROMPTA GİRMEZ; TIMELINE'daki gövde fiillerinin tempo ve sırasını besler.
> Başlıklar rol etiketi — özel ad promptta yok [D34].

```
👤 KART A — "pilot" (Lena)                                     katman     sahne
ROL           pilot koltuğu, sağ eldiven T-kabzalı kumanda kolunda,     TANIMA     K04
              altın bant SAĞ önkol + uyluk
İSTEK         gemiyi istasyona bağlamak (B5)                            HİZALANMA  K03-K04
BASKI TEPKİSİ ACELE EDER — el, bakıştan ÖNCE gider; düzeltme büyük      HİZALANMA  K06
ALIŞKANLIK    her düzeltmeden önce sağ başparmak kabzanın başlığına     TANIMA     K04 · K06 · K11
              iki kez basar (aynı cümle, birebir)                                  → kırılma K18
SINIR         göremediği bir şeye gemi sürmez                           BAĞLANMA   K16 (eli kumandadan
                                                                                   çekilir) → K18 aşar
ZAAF          kendi gözüne güvenip payı tüketir — K07 önkolu kilitli,  BAĞLANMA   K07 · K11
              omuzları düşük; yorgunluk K07=4
TEL           nefesini tutar: omuz hattı kalkar ve bir süre inmez      HİZALANMA  K07 · K16 · K20
İLK ↔ SON     K04 kabzayı sıkı kavrayan sağ eldiven ↔ K24 dizinde AÇIK  BAĞLANMA   K04 ↔ K24
              duran sağ eldiven

👤 KART B — "mühendis" (Noah)                                  katman     sahne
ROL           sağ koltuk, sol bilekte analog gösterge halkası,         TANIMA     K04
              kobalt bant SOL pazı + uyluk
İSTEK         hattı kapatıp yanaşmayı mümkün kılmak; sonra Lena'yı     HİZALANMA  K08 · K17-K18
              halkaya kendi gözüyle taşımak
BASKI TEPKİSİ KONTROL EDER — bakış ÖNCE, el ~1 s sonra                 HİZALANMA  K09 · K10
ALIŞKANLIK    bir yere bağlanınca bağ kayışını iki kez çeker           TANIMA     K04 · K09 → kırılma K17
              (koltuk · vana bağı) — K17'de ilk çekişten sonra
              ikinciyi yapmadan pencereye eğilir
SINIR         görmediği şeyi söylemez (K12 rezervi okumadan konuşmaz · BAĞLANMA   K12 · K18
              K18 halkayı görmeden komut vermez)
ZAAF          vana çarkı direnir — iki deneme, omuz/sırt öder          BAĞLANMA   K10
TEL           vizörünü bakılan yüzeye yaklaştırır, baş öne             HİZALANMA  K10 · K18
İLK ↔ SON     K04 göstergeye bakar (makineye güven) ↔ K24 pencereden   BAĞLANMA   K04 ↔ K24
              halkaya bakar, fısıldar
⭐ AYRIŞMA (≥3 davranış satırı): İSTEK farklı · BASKI TEPKİSİ (acele ↔ kontrol) farklı ·
   ALIŞKANLIK (başparmak/kabza ↔ kayış/bağ) farklı · TEMPO (Lena önce gider, Noah ~1 s
   sonra) farklı ✅
FİZİKSEL FARK (bible): şerit rengi+tarafı · rozet biçimi+tarafı · göğüs plakası (Lena
   inci beyazı kompozit ↔ Noah beyaz teknik kumaş + kobalt eklem panelleri) · KONUM
   (Lena hep kokpitte · Noah K09'dan sonra servis/optik bölmede) — yüze bağlı OLMAYAN üç kanal
```

---

## ✅ KAPI

```
☑ konsept kapısı ①②③ üçü de ✅ (② şartlı: K18 iki parmak kadrajda ≥ ⅛)
☑ risk sayımı yazıldı (10/14) ve eşik kararı verildi (kilit tavanı 20)
☑ B5 dörtlüsü tam, BEDEL sahne numarası taşıyor (S2·K07 · S3·K10 · S4·K18)
☑ iki karakter kartı ≥3 satırda ayrışıyor · İSTEK ÇAPRAZI dolu
☑ ön-otopsi KARAR: GO
→ 03_SAHNE_SIRALAMASI.md yazılabilir
☑ replik SAPMA 1 (D01 · D07 · D12 · hook dış sesi) sahip onayladı 05.10.2026 —
   promptlar yeni repliklerle yazılır.
```
