# 📋 THE COLD WELD — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün
> eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU yapıştırılır            MOD D
④ 📖 HİKAYE      → A BLOĞU yapıştırılır                MOD D
② 🔗 DEVAMLILIK  → ⛔ HİÇBİR ŞEY (baseline: videodan sahne envanteri
                                  + karakter pasaportu + kurulum envanteri)
③ 🔊 SES         → ⛔ HİÇBİR ŞEY (baseline: kurgudan ses defteri)

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: ışık çizgisi mesafe
                   sayacı · ekran yönü · sabit çevre nesneleri [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · hız · süre · mesafe)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük tasarımdır.
   Ama bu film bir GEÇİŞ filmidir: ışık çizgisi mesafe sayacı verilmezse ⑤
   tasarlanmış ilerlemeyi "geometri sürüklenmesi" yazar ve tablosunun
   tamamı ⑩'dan düşer [D133].

⛔ ② ve ③'e belge vermek yasaktır — eksikliği değil, TASARIMI bozar.
   FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.

⛔ Her mercek AYRI ve TEMİZ sohbette [D110].
⛔ Dördüne de AYNI video dosyası verilir [D75].
⛔ ① KARE raporunun ilk satırında `FORMAT: YATAY` olmalı; kategori
   12-14 (9:16 · güvenli alan · kanca) N/A dönmeli.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE COLD WELD
FORMAT:               16:9 yatay · 2-4 dk · bilimkurgu (keşif / aksiyon) ·
                      HARD VACUUM üzerinde bir ay yüzeyi (0,30 g · atmosfer
                      yok · gölge içi mutlak siyah) · gündüz, alçak ve
                      sabit yükseklikte tek yıldız
SCENE COUNT:          15   (S0-S14)
RUNTIME:              150 seconds (title card: none — screen text lock 0.0 s)
REVIEW INPUT:         video only

LOGLINE (intended):   On an airless moon where bare metal that touches bare
                      metal fuses permanently on contact — so that a wrecked
                      ship has become one continuous metal reef — a lone
                      technician must cross seventy-eight metres of that reef
                      while the advancing edge of sunlight breaks it back
                      into separate plates, using the only two bare-metal
                      surfaces she has: the grip disc in each palm, each of
                      which can be used exactly once.
THEME (intended):     YALNIZLIK — "Nothing is ever lost here and nobody ever
                      comes back. Everyone who came is still here, and none
                      of them is still themselves."
THEME SCENES:         ✅ YAZILDI — S3 (boşluk: tepe kadrajı, %82 negatif
                      alan, figür 38 piksel) · S8 (yankı: otuz bir parlak
                      disk, insan yok) · S12 (içe kapanma: diz çöküş,
                      omuzlar kısılır, avuç yere kapanır) · S14 (tekil
                      soğuk kaynak: son 3,5 saniyede ekranda insan yok)
                      → TEMA_MUHENDISLIGI §5 matrisi · §3 tablosundan
                      HİÇ KULLANILMAMIŞ tema; §3c takas kalıbı KULLANILMADI
INTENDED EMOTION:     cold procedural focus turning into a two-count dread —
                      the viewer arrives asking "why didn't the wrench
                      fall?", stays asking "how many palms are left?",
                      leaves asking "how does she climb that ladder now?"
ENDING TYPE:          AMBIGUOUS (open) + visual dilemma. Both palms are
                      matte dark, one mirror disc is left in the plate, the
                      lander stands unclimbed in the RIGHT third, and the
                      last 3.5 seconds have no human in frame. Nobody
                      boards: no ladder climb, no lift-off, no answer.

PROTAGONIST:          a woman in her late thirties, 1.71 m, unnamed in
                      prompts, identified by three physical channels only:
                      height, matte pale bone-white suit, and a 14 cm old
                      scuff on the LEFT shoulder.
                      Wants: to cross the reef to the regolith and her
                      lander. Fears: not the light — running out of palms.
SECOND FIGURE:        NONE. Exactly one living human, in 14 of 15 scenes.
                      S0 has zero humans.
ANTAGONIST/FORCE:     no villain, no creature, no pursuit. The force is a
                      SPEED: the edge of sunlight advancing at 0.40 m/s,
                      which never accelerates, never stops and never targets
                      anyone — plus the contact law itself.
CENTRAL CHOICE:       S12 (120-130 s) — she presses her last bright palm
                      onto the plate ON PURPOSE, spending it to be carried
                      by the thing that is about to be released. Cost lands
                      IN THE SAME SHOT: her already-dark right palm is in
                      frame throughout.

DIALOGUE LINES:       0 — completely silent film. No human speech, no
                      machine voice, no radio, no voice-over. There is no
                      "utterance" of any kind anywhere in the film.
SILENT SCENES:        15 (all of them)
MUSIC-FREE SCENES:    2 — S0 (hook) and S12 (the choice)
VIRAL INTERSTITIALS:  S3 · S9 · S13   ⛔ THESE MAY NOT BE CUT
UNCUTTABLE LIST:      S0 · S3 · S6 · S8 · S9 · S12 · S13 · S14
                      (cover moment · scale · cost 1 · Chekhov payoff ·
                       viral 2 · climax · viral 3 · final)
SEED (planted clue):  S2 at 22.0-24.0 s — ONE mirror-bright disc on a
                      vertical plate 3 m behind her, unremarked, ≤2 s.
                      Payoff at S8 (thirty-one of them). [FINAL §3, window
                      for 2-4 min is 15-22 s]
COVER/THUMBNAIL:      A: S0 at 6.0 s — the airborne plate with the wrench
                      standing perpendicular on it, RIGHT third, straight
                      light edge across the LEFT two thirds.
                      B: S12 at 1.5 s — the raised bright palm above the
                      metal with the dark palm in the same frame.
TITLE:                THE COLD WELD — welding without fire; the thing this
                      world does to anything that touches it.
LIBRARY CONTEXT:      First film in the library on cold welding, and the
                      first with a two-item cost counter (2 palms → 0).
                      Nearest neighbour is THE REMEMBERING DUST (a ground
                      that RECORDS and rewrites); this ground KEEPS the
                      object itself and never erases. Structure inherited
                      from THE ROSE COAT (0 cuts, fixed 10 s grid,
                      environmental counters, separate SPEC file); the
                      resource there was 80 brush strokes, here it is 2.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      15          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      15 · 0 sahne içi kesme
PLANNED CUTS:    0           listede olmayan HER kesme ihlaldir
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, bilinçli sapma)
                 ⭐ GEREKÇE SATIRI [D74 · KURGU_RITMI §1]: bu filmin
                 antagonisti SABİT BİR HIZDIR (0,40 m/s) ve o hız hiçbir
                 sahnede değişmez; kurgunun hızlanması, değişmeyen tek
                 şeyin değiştiğini söylerdi. Hızlanma hissi sahne İÇİ
                 olay yoğunluğundan gelir (S9'da dört ardışık kopuş,
                 S12'de tek tereddüt, S13'te 3,0 s'lik kayış).
ASL CURVE:       ①10,0 ②10,0 ③10,0 ④10,0 ⑤10,0  (sabit)
GRID:            sahne başlangıcı(n) = n × 10 s   ·   S0 = 0 s
RUNTIME:         150 s   (15 × 10 s)
RAW FOOTAGE:     150 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı YOK
CAMERA:          15/15 sabit lockoff · 0 pan · 0 tilt · 0 zoom · 0 track
                 ⛔ KLİP İÇİ karar; sahneler ARASI kurulumu SETUP
                 SEQUENCE anlatır [02_RISK_KARTLARI KART 8 kapsamı]

SETUP SEQUENCE:  A · B · C · D · E · F · G · B · C · B · F · G · H · E · A
                 S0  S1  S2  S3  S4  S5  S6  S7  S8  S9 S10 S11 S12 S13 S14
                 8 kurulum · 15 sahne · ardışık ikili aynı kurulum YOK
                 A göz hizası 50mm 4,0 m 1,55 m az.145° MS
                 B alt açı    24mm 6,0 m 0,35 m +18° az.80°  WS
                 C üst açı    35mm 3,5 m 2,60 m −25° az.155° MS
                 D tepe       24mm 40 m yükseklik −90°       EWS
                 E profil     50mm 14,0 m 1,45 m az.90°      WS
                 F OTS        50mm 2,8 m 1,70 m +3° az.38°   MS
                 G makro      100mm 1,2 m 0,30 m −18° az.150° CU
                 H eğik       35mm 2,2 m 1,20 m Dutch 12° az.20° MS
                 ⚠️ ACI_YAYI §4 üst bandı 15 sahne için ≤7,5 kurulum der;
                 bu film 8 taşır. BİLİNÇLİ SAPMA, gerekçesi film
                 dosyasının §0.9b'sinde tek satır [D74]. Mekânsal algı
                 korunuyor: 15 sahnenin 7'si tanıtılmış kurulumun tekrarı.

ANGLE ARC:       ⭐ **7 AÇI TİPİ** — göz hizası (A · G) · alt açı (B) ·
                 üst açı (C) · tepe (D) · profil (E) · OTS (F) · eğik (H).
                 POV kullanılmadı (lockoff gözlemci dilini bozar).
                 ⭐ DEPO KAYDI: 26.08.2026 taramasında 107 dosyanın 43'ü
                 3 tipin ALTINDA ve ölçülen en yüksek çeşitlilik 4'tü.
                 Bu film o açığı kapatmak için yazıldı; ⑪ kapısı GEÇER.
                 ABARTI BANDI [KAMERA_ACISI §5]: Dutch 12° (ideal 5-15) ·
                 alt açı +18° (meşru 15-30) · üst açı −25° (meşru 15-30) ·
                 tepe −90° (ayrı tip, 45-60° ölü bölgesinin dışında).
                 DORUK KONTRASTI [ACI_YAYI §9]: filmin en büyük sıçraması
                 (131°) S11→S12'dedir, yani doruğa girişte ✅

LENS/ÖLÇEK YAYI: 50 · 24 · 35 · 24 · 50 · 50 · 100 · 24 · 35 · 24 · 50 ·
                 100 · 35 · 50 · 50
                 MS·WS·MS·EWS·WS·MS·CU·WS·MS·WS·MS·CU·MS·WS·MS
                 ardışık iki sahne aynı ölçekte DEĞİL; 14 çiftin 12'si
                 tam 1 kademe, 2'si bilinçli ŞOK (S2→S3 · S6→S7)
                 [KURGU_RITMI §2 örüntü kırıcı kapısı · ACI_YAYI §3]

DORUK:           S12 → 120-130 s (sahne başlangıcı 120 s)
                 · avuç havada 121,5 s
                 · AVUÇ BASAR 122,0 s
                 · çekme denemesi ve gelmeme 123,0 s
                 · ışık kaskın içine girer 126,0 s
                 · gövde levhaya yerleşir 129,0 s
KAPAK ANI:       S0 → 6,0 s (A sürümü) · S12 → 121,5 s (B sürümü)
TOHUM:           S2 → 22,0-24,0 s
⛔ ZAMAN HESAPLANMAZ, HESAPLATILIR [D122]: bu filmde replik 0'dır, o
   yüzden replik formülü N/A'dır. Kalan bütün zaman kayıtları TEK
   formülden türetilir ve yukarıdaki her satır onunla doğrulandı:
       t(S_n, ofset) = n × 10 s + promptun TIMELINE ofseti
   Örnek: S12'nin 2,0 s ofseti → 12 × 10 + 2,0 = 122,0 s ✅
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
GÖVDE ŞERİDİ (plan)  : -11111111111111   ← kaç GÖVDE · ÜRETİM kilidi
VARLIK ŞERİDİ (kapı) : -11111111111111   ← rubriğin ÜRETEBİLECEĞİ dize
                                            kurgu kapısı ④c BUNUNLA koşar
        │└─────────── S1-S14 tek insanlı (14 sahne)
        └──────────── S0 insansız (hook)
insansız 1 sahne: S0   ·   tek insanlı 14 sahne   ·   iki insanlı 0 sahne

⭐ Bu filmde iki şerit BİREBİR AYNIDIR; D135'in iki-figür istisnası
   gerekmez ve kapı doğrudan koşulur.
⚠️ S14'ün son 3,5 saniyesinde kadrajda insan YOKTUR ama sahne "1"
   sayılır: şerit SAHNE başına yazılır, kare başına değil.
⭐ Dört merceğin PRESENCE STRING satırları yan yana konur [D135]:
   biri ötekilerden farklıysa önce O RAPORUN kendi sahne envanteriyle
   karşılaştırılır.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
CANLI İNSAN   tam 1 · 14 sahnede görünür · 1 sahne insansız (S0).
              İkinci figür 0 · kopya 0 · klon 0 · yansımada figür 0 ·
              uzakta figür 0 · inicin yanında figür 0 · merdivende
              figür 0.
KİMLİK        Üç kanal, hiçbiri yüze bağlı değil: 1,71 m boy · mat soluk
              kemik beyazı giysi · SOL omuzda 14 cm'lik eski çentik.
              ⛔ Prompt gövdesinde özel ad ve milliyet YOK [D34/D45].
BAŞ/YÜZ       Tek yüz, 15/15 sahnede kask içinde. Vizör tek parça,
              optik olarak ŞEFFAF; sıfır renk, sıfır ayna kaplaması,
              sıfır çevre yansıması; yüz her baş açısında okunur
              [D5 · D79]. Vizör 0 kare açılır, 0 kare buğulanır.
SIRT          Boyundan kalçaya TEK PARÇA düz panel: çanta 0 · tank 0 ·
              hortum 0 · kablo 0 · çıkıntı 0 [D79]. ⭐ S12'de kamera
              gövdenin ARDINDADIR (azimut 20°) ve o promptta yokluk
              listesi POZİTİF YÜZEY TARİFİNE çevrilmiştir [D139].
              "Sırtta bir şey var" bulgusu yalnız SİLÜET BOZULMUŞSA
              geçerlidir.
⭐ SOĞUK KAYNAK  ⭐ FİLMİN NOVUM'U — üç maddelik kapalı liste:
              ① Çıplak metal ↔ çıplak metal teması KALICIDIR.
              ② Seramik kaplı yüzey (bot tabanı 26×11 cm · diz koruması ·
                önkol manşeti 12 cm · kalça paneli) KAYNAMAZ.
              ③ Kumaş, cam ve boya KAYNAMAZ.
              ⛔ "Neden avucunu kaldıramıyor" / "neden yapıştı" soruları
                 BULGU DEĞİLDİR; filmin ÖNERMESİDİR [D87/D116 önerme
                 kapısı]. ⛔ "Botları neden yapışmıyor" da bulgu değildir:
                 asimetri TASARIMDIR ve 15/15 promptta yazılıdır.
              ⛔ Bağ ATOMİKTİR, GEOMETRİK DEĞİL: iki yüzey ayrı ayrı
                 görünür kalır ve aralarında net bir sınır vardır.
                 "El metale eriyor / batıyor" bir ÜRETİM HATASIDIR ve
                 bulgu olarak yazılır [D24 temas bütünlüğü].
AVUÇ SAYACI   ⭐ FİLMİN ANA SAYACI, iki durum:
              PARLAK   9 cm ayna gibi cilalı nikel disk, avuca gömülü
              KARANLIK 9 cm mat koyu gri kumaş daire, ışık yakalamaz
              Takvim: S1-S5 iki avuç da PARLAK (2) · S6 sağ avuç
              KARANLIK (1) · S7-S11 sol PARLAK / sağ KARANLIK (1) ·
              S12-S13 sol PARLAK ama KAYNAMIŞ · S14 ikisi de KARANLIK (0)
              ⛔ Sayaç asla geri gitmez. Bir sahnede karanlık bir avuç
                 yeniden parlaksa bu bir ÜRETİM HATASIDIR.
              ⛔ Diskler hiçbir karede İNSAN yansıtmaz: yüz 0, gövde 0,
                 figür 0. Yalnız çıplak ışığı yansıtırlar — bu TASARIMDIR.
YAMALAR       S2'de 1 · S8'de 31 disk + 6 bot-tabanı boyutunda dikdörtgen
              + 1 dar bilezik · S9'da aynı 31 disk yer değiştirir ama
              HİÇBİRİ KAYBOLMAZ · S14'te 1 disk daha (kadının bıraktığı).
              ⛔ HEPSİ DÜZ SACTIR ve levhanın DÜZLEMİNDE durur. Duvarda
                 gövde, uzuv, yüz ya da üç boyutlu hiçbir şey YOKTUR;
                 hiçbir şey duvardan dışarı taşmaz. "Duvarda insan var"
                 bulgusu bir ÜRETİM HATASIDIR ve öyle yazılır.
IŞIK ÇİZGİSİ  ⭐ FİLMİN SAATİ: krater gölgesinin kenarı. JİLET GİBİ DÜZ,
              0,40 m/s, EKRAN-SOLDAN EKRAN-SAĞA, 15/15 sahnede aynı
              yönde. Hiç durmaz, hızlanmaz, yön değiştirmez, dalgalanmaz.
              Mesafe takvimi (kadının botlarından): S1 34 m · S2 31 m ·
              S3 28 m · S4 24 m · S5 19 m · S6 15 m · S7 12 m · S8 9 m ·
              S9 6 m · S10 4,5 m · S11 3,0 m · S12 1,5 m · S13 0 m ·
              S14 geçmiş.
              ⛔ MONOTONİKTİR — geri gitme = ihlal.
              ⛔ Çizgi bir IŞIN, HÜZME, PROJEKTÖR ya da TARAYICI DEĞİLDİR:
                 bir GÖLGE KENARIDIR. Hüzme görünüyorsa üretim hatasıdır
                 (vakumda saçılma yok).
DİKİŞ KOPUŞU  Gölge 98 K · ışık 371 K · 4,0 m levha ışıkta 5,2 mm uzar ·
              dikiş ışığın geçmesinden 0,4-1,2 s sonra kopar. Kopuş
              SOĞUKTUR: kıvılcım 0 · ısı parlaması 0 · duman 0 · ark 0 ·
              erimiş metal 0 · patlama 0.
SERBEST CİSİM Kopan levha 0,35 m yükselir, 0,9 m yana gider, 0,49 s'de
              tepe yapar, 0,70 s'de OTURUR ve bir daha kımıldamaz [D127].
              ⛔ 1 saniyeden uzun havada kalan levha ihlaldir. Asılı
                 kalma 0 · süzülme 0 · yavaşlama 0 · dönerek uçma 0.
YERÇEKİMİ     0,30 g (2,94 m/s²) — gövde 1,00 m'yi 0,82 s'de düşer.
              Ağır çekim 0 kare · hız rampası 0 kare.
              ⛔ SIÇRAYIŞ 0 KARE: iki bot hiçbir karede aynı anda yerden
                 kesilmez; havada geçen toplam süre 0,0 saniyedir. Bu
                 TASARIMDIR [D23 yapısal olarak tetiklenemez], eksiklik
                 değil.
KAYIŞ         S13: 22° eğimli levha 5,0 m'yi 3,0 saniyede alır, sonda
              3,3 m/s. Sekme 0 · takla 0 · ikinci kayış 0.
TOZ           ⭐ RESİFTE 0 KARE TOZ — zemin çıplak metaldir ve toz
              tutmaz. Bu TASARIMDIR, eksiklik değil. Toz yalnız S13'te
              ve yalnız regolitte: ≤0,4 m yükselir, tamamı 0,6 s'de
              oturur, düz aşağı iner. Girdap 0 · sıvı gibi akma 0 ·
              asılı perde 0 [D39].
IŞIK          ⭐ TEK KAYNAK: yıldız, EKRAN-SOLDA, 4,2°. Yapay ışık 0 kare
              (far · seyir lambası · kapak ışığı · fener · ekran · uyarı
              lambası · kask içi lamba). İniç 15/15 sahnede SÖNÜK ve
              soğuktur; motor alevi 0 kare, egzoz 0 kare.
              ⭐ VAKUMDA DOLGU IŞIĞI YOKTUR: gölge içi MUTLAK SİYAH ve
              gölge kenarı JİLETTİR. "Gölgeler çok sert / detay yok"
              bulgusu DÜŞER — ortamın kuralıdır [§3.1].
              ⛔ Lens parlaması ve anamorfik yatay parlama fiziksel
                 olarak YANLIŞTIR (saçılma yok) ve görülürse bulgudur.
GÖKYÜZÜ       MUTLAK SİYAH ve BOŞ. Yıldız alanı 0 · gezegen 0 · bulutsu
              0 · gradyan 0. "Gökyüzü boş" bulgusu TASARIMDIR.
EKRAN YÖNÜ    15/15 sahnede: yıldız SOL · gölgeler SAĞ · ışık çizgisi
              soldan sağa · hedef (resifin öbür kenarı + iniç) SAĞ ÜÇTE
              BİRDE · kadın ekran-sağa hareket eder. Yön dönüşü 0 kare.
              ⭐ TASARLANMIŞ İSTİSNA: S1 · S7 · S12'de omuz üstünden
              çizgiye TEK saniyelik BAŞ dönüşü var; ayaklar yön
              değiştirmez. Bu Kart 9'un kinesik ayağıdır, ihlal değildir.
              ⭐ S10'da kadın 4 m GERİ (ekran-sola) yürür ama omuz hattı
              ekran-sağda kalır — bu ZORLANMA ÇAPASIDIR ve tasarımdır.
RENK          Filmde tam üç değer var: aydınlık metalin soğuk gümüşü,
              gölgenin mutlak siyahı, giysinin soluk kemik beyazı.
              Doygun renk 0 kare. ⭐ Tek spekülar vurgu avuç diskleri ve
              yamalardır — parlaklık bir SAYAÇTIR ve post'ta oynanmadı.
              ⛔ "Her şey aynı renk" bulgusu TASARIMDIR.
ANAHTAR       56 cm düz çelik, işaretsiz. S0'da bir levhaya DİK kaynamış;
              S10'da önkol manşeti ve dizle kurtarılır; S11'de son dikişe
              çakılır ve kaynar. ⛔ Avuçla 0 kare tutulur — "neden eliyle
              tutmuyor" bulgu değildir, filmin kuralıdır.
TEMAS         Kadın-nesne teması sayılıdır: avuç-metal 2 kez (S5 kaza ·
              S12 seçim) · manşet-anahtar 2 kez (S10 · S11) · bot-basamak
              1 kez (S11). Bunun dışında avuç hiçbir yüzeye değmez.
BİNİŞ         0 kare [D69]. Merdiven tırmanma, kapaktan girme, kalkış
              yok; film levhanın dibinde biter. "Final kesik" bulgusu
              DÜŞER — muğlak/genişleme finalidir.
KOŞU/ZIPLAMA  0 kare. Yürüyüş ölçülüdür. Koşu ve sıçrama TASARIM GEREĞİ
              yoktur (D23 + klon riski).
KONUŞMA       0 replik · ağız hiçbir karede konuşma için oynamaz. Radyo
              0 · AI sesi 0 · dış ses 0. "Diyalog yok" bulgusu TASARIMDIR
              [③ SES merceği için].
METİN         0 kare — gövde yazısı, logo, marka, numara, sembol, bayrak,
              arma, ölçü çentiği, gradasyon işareti, seri numarası, uyarı
              damgası hiçbir yüzeyde yok. ⭐ Bu filmin en yüksek metin
              riski METAL YÜZEYDİR [D138] ve karşı önlem POZİTİFTİR:
              bilgi taşıyan tek şey dikiş, perçin ve göktaşı çukurudur.
SU/ATEŞ       0 kare — su, buz, kırağı, buğu, sis, bulut, alev, duman,
              patlama, kıvılcım, motor jeti yok. İniç hiçbir karede
              çalışmaz.
CANLI         0 kare — hayvan, kuş, böcek, bitki, mikrobiyal örtü,
              organik hareket yok.
HASAR         0 kare — giysi yırtığı, çatlak vizör, sızıntı, buhar,
              kaçak gaz yok. Tek sonuç DİSKİN KALMASIDIR.
EŞ KADRAJ     S0 ↔ S14 (aynı kurulum A, aynı görsel iddia: bir metal
              yüzey ve üstünde ona kaynamış tek bir yabancı nesne —
              biri anahtar, öteki bir avuç diski)
```

---

## ⛔ RUBRİĞE UYARI — bilinçli tasarım kararları, ihlal olarak raporlanmaz

```
· Avucun metalden kalkmaması filmin ÖNERMESİDİR, mantık hatası değil.
· Botların ve manşetlerin yapışmaması TASARIMDIR (seramik kaplama) ve
  15/15 promptta yazılıdır; tutarsızlık değildir.
· Resifte hiç toz olmaması TASARIMDIR — zemin çıplak metaldir.
· Gökyüzünün tamamen boş ve siyah olması TASARIMDIR.
· Gölgelerin mutlak siyah ve dolgusuz olması vakumda MEŞRUDUR [§3.1] ve
  bu filmde ışık çizgisini okunur kılan şeydir.
· Kimsenin konuşmaması TASARIMDIR — ses tasarımı eksik değildir.
· Sıçrama ve koşu olmaması TASARIMDIR (D23 yapısal olarak kapatıldı).
· 15/15 sabit kamera ve 0 kesme TASARIMDIR; sahneler ARASI kurulum
  değişimi ise BİLİNÇLİDİR ve ölçülür (SETUP SEQUENCE · ANGLE ARC).
· 8 kurulumun 7,5'lik bandın üstünde olması BİLİNÇLİ SAPMADIR; gerekçesi
  film dosyası §0.9b'de tek satır olarak yazılıdır [D74].
· Duvardaki yamaların insan olmaması TASARIMDIR — hepsi düz sactır.
· S13'ün kayışında kadının levhaya kaynamış olması TASARIMDIR; "neden
  tutunuyor" sorusu S12'de cevaplanmıştır.
· Kimsenin inice binmemesi ve kalkışın gösterilmemesi TASARIMDIR
  [D69 · muğlak final] — "kesik final" değildir.
· S0'da insan olmaması TASARIMDIR (Kart 4 karşı önlemi).
· S14'ün son 3,5 saniyesinde ekranda insan olmaması TASARIMDIR
  (TEMA_MUHENDISLIGI §5 · yalnızlık motifi).
```
