# 📋 THE ROSE COAT — QA SPEC (rubriklere yapıştırılacak tek dosya)

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
                                  + karakter pasaportu)
③ 🔊 SES         → ⛔ HİÇBİR ŞEY (baseline: kurgudan ses defteri)

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: mesafe/ölçek sayacı ·
                   ekran yönü · sabit çevre nesneleri [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · oran · hız · süre)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük tasarımdır.
   Ama YAKLAŞMA filminde mesafe sayacı verilmezse ⑤ tasarlanmış yaklaşmayı
   "geometri sürüklenmesi" yazar ve tablosunun tamamı ⑩'dan düşer [D133].

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
FILM:                 THE ROSE COAT
FORMAT:               16:9 yatay · 2-4 dk · bilimkurgu (keşif / bakım) ·
                      ince atmosfer (%1,2 basınç · 0,40 g) · gündüz,
                      alçak ve yavaş yükselen yıldız
SCENE COUNT:          13   (S0-S12)
RUNTIME:              130 seconds (title card: none — screen text lock 0.0 s)
REVIEW INPUT:         video only

LOGLINE (intended):   On a plain whose rose dust bonds electrostatically
                      to every surface and never comes off by itself,
                      two technicians walking 600 meters to their lander
                      keep each other alive by brushing the one surface
                      neither of them can reach — the flat radiator
                      panel on their own back — until a collapsed drift,
                      a coated ship and a brush with a finite charge
                      leave exactly enough strokes for two of the three
                      surfaces that need them.
THEME (intended):     Nobody can reach their own back. Everything still
                      working here is working because something else
                      brushed it.
THEME SCENES:         🚨 YAZILMAMIŞ (26.08.2026 ölçümü)
                      TEMA_MUHENDISLIGI §5 temayı MOTİFE, motifi SAHNEYE
                      bağlar; bu filmde tema tek cümle olarak yazılmış,
                      hangi sahnede hangi motife döndüğü hiç yazılmamış.
                      ⛔ Sonradan TÜRETME — Kaleida Crash kaydındaki
                      teşhis tam bu boşluk ("bedel yok → tema dekoratif
                      kalıyor"). Sonraki filmde plana yazılır
                      [03_PLAN_ONCESI B3].
INTENDED EMOTION:     quiet procedural warmth turning into arithmetic
                      dread — the viewer arrives asking "what is this
                      dust doing?", stays asking "how many strokes are
                      left?", leaves rereading the last frame as a debt
                      rather than a rescue.
ENDING TYPE:          EXPANSION (not resolution) + visual dilemma. One
                      back panel is clean deep rose, the other is the
                      colour of the plain, the brush is spent, and
                      nobody boards: no ladder climb, no lift-off, no
                      answer.

PROTAGONIST:          the taller figure (1.86 m, dark charcoal gloves and
                      boots, band on the RIGHT thigh), unnamed in
                      prompts. Wants: to get both of them and the ship's
                      radiator panel clean enough to leave.
                      Fears: not the dust — running out of strokes.
SECOND FIGURE:        the shorter figure (1.62 m, white gloves and boots,
                      band on the LEFT upper arm), unnamed in prompts.
                      ⭐ NOT a passenger: the film's novum requires two
                      people, because the mechanic is "cannot reach".
ANTAGONIST/FORCE:     no villain, no creature, no pursuit. The force is
                      a RATE: 0.25 mm of bonded dust per minute on every
                      upward and rearward facing surface. It never
                      accelerates, never stops and never targets anyone.
CENTRAL CHOICE:       S11 — the last twenty strokes go on the other
                      figure's back panel, not the protagonist's own.
                      Cost lands IN THE SAME SHOT: its own back panel is
                      in frame throughout and stays pale chalk; the
                      brush is struck at 8.5 s and nothing falls out.

DIALOGUE LINES:       0 — completely silent film. No human speech, no
                      machine voice, no radio, no voice-over. The only
                      "utterance" is two glove taps on a helmet (S11,
                      7.0 s) and it is sound design, not a line.
SILENT SCENES:        13 (all of them)
MUSIC-FREE SCENES:    2 — S0 (hook) and S8 (the brush fails)
VIRAL INTERSTITIALS:  S3 · S7 · S11   ⛔ THESE MAY NOT BE CUT
COVER/THUMBNAIL:      S11 at 6.0 s — the brush on the shorter figure's
                      half-cleaned panel while the taller figure's own
                      panel, in the same frame, is the colour of the
                      ground.
TITLE:                THE ROSE COAT — the coat of dust, and the thing
                      the world puts on you if nobody brushes it off.
LIBRARY CONTEXT:      Second two-figure space film in the library after
                      THE LAST SHIFT, and structurally its opposite:
                      there two figures solve a mystery and speak 12
                      lines; here two figures maintain each other and
                      speak none. Nearest thematic neighbour is THE
                      REMEMBERING DUST (a ground that RECORDS); this
                      ground COATS.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      13          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      13 · 0 sahne içi kesme
PLANNED CUTS:    0           listede olmayan HER kesme ihlaldir
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok)
                 ⭐ GEREKÇE SATIRI [D74]: sabit ızgara bilinçlidir. Bu
                 bir bakım işi filmidir ve ritmi işin ritmidir: darbe,
                 bekleme, darbe. Hızlanma hissi kurgudan değil sahne
                 İÇİ olay yoğunluğundan gelir (S7'de 0,71 s'lik düşüş,
                 S10'da 30 darbe, S11'de tek bir tereddüt).
GRID:            sahne başlangıcı(n) = (n) × 10 s   ·   S0 = 0 s
RUNTIME:         130 s   (13 × 10 s)
RAW FOOTAGE:     130 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı YOK
CAMERA:          13/13 sabit lockoff · 0 pan · 0 tilt · 0 zoom · 0 track
                 ⛔ KLİP İÇİ karar; sahneler ARASI kurulumu SETUP
                 SEQUENCE anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE:  13 sahne · 13 AYRI kurulum (26.08.2026'da ölçüldü)
                 her sahne kendi lens+yükseklik+mesafe üçlüsünü taşıyor;
                 tekrar eden kurulum YOK
                 ⚠️ ACI_YAYI §4 üst bandı: kurulum sayısı sahne sayısının
                 YARISINI geçmez (13 sahne → ~7). Bu film 13 taşıyor.
                 §4'ün gerekçesi mekânsal algı: her sahne yeni bir
                 kurulumsa izleyici mekânı kuramaz. Bilinçli sapmaysa
                 tek satır gerekçe ister [D74]; değilse tekrar eden
                 kurulumlar tanıtılır (A-B-A yapısı §3'te serbesttir).
ANGLE ARC:       **2 açı tipi — GÖZ HİZASI (9 sahne) · PROFİL (S4 · S8)**
                 🚨 AÇIK MADDE: KAMERA_ACISI §2 en az 3 tip ister.
                 Bu film 13 KURULUM ama 2 AÇI TİPİ taşıyor — yukarıdaki
                 LENS/ÖLÇEK YAYI satırı ölçek çeşitliliğini doğru
                 kuruyor, çeşitlenmeyen şey AÇI. Doruk (S11) §9'a göre
                 en yüksek kontrast sıçramasını taşımalı; üçüncü tip
                 oradan kazanılır.
DORUK:           S11 → 110-120 s (sahne başlangıcı 110 s)
                 · ulaşamama hareketi 110.5-111.5 s
                 · yirmi darbe 112.0-118.0 s
                 · boş vuruş 118.5 s
LENS/ÖLÇEK YAYI: 50 · 35 · 28 · 24 · 50 · 35 · 28 · 35 · 50 · 35 · 28 ·
                 50 · 24  — ardışık iki sahne aynı ölçekte DEĞİL
                 [KURGU_RITMI §2 örüntü kırıcı kapısı]
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
GÖVDE ŞERİDİ (plan)  : -222222222222   ← kaç GÖVDE · ÜRETİM kilidi
VARLIK ŞERİDİ (kapı) : -111111111111   ← rubriğin ÜRETEBİLECEĞİ dize
                                          kurgu kapısı ④c BUNUNLA koşar
        │└─────────── S1-S12 İKİ insanlı (12 sahne)
        └──────────── S0 insansız (hook)
insansız 1 sahne: S0   ·   iki insanlı 12 sahne   ·   tek insanlı 0 sahne

⛔ [Ders 135] KAPI GÖVDE ŞERİDİYLE KOŞULAMAZ. Rubriklerin çıktı şartnamesi
   "`1` if a human figure is visible, `-` if none" — model "2" ÜRETEMEZ.
   İki dize hiçbir zaman eşit olmaz ve kapı her iki-figürlü filmde düşer.
   ④c kapısı VARLIK şeridiyle koşulur; GÖVDE sayısı ② DEVAMLILIK'ın
   APPEARANCE TABLE'ından doğrulanır — her sahne satırında kaç ayrı
   karakter etiketi var? Beklenen 2 tutmuyorsa kurgu değil ÜRETİM sapmıştır
   [D118 + Risk Kartı 4].
⭐ Dört merceğin PRESENCE STRING satırları da yan yana konur [D135]:
   biri ötekilerden farklıysa önce O RAPORUN kendi sahne envanteriyle
   karşılaştırılır.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
CANLI İNSAN   tam 2 · 12 sahnede görünür · 1 sahne insansız (S0).
              Üçüncü figür 0 · kopya 0 · klon 0 · yansımada figür 0 ·
              uzakta figür 0.
KADRO KİLİDİ  Ayrım üç kanaldır ve hiçbiri yüze bağlı değildir:
              UZUN 1,86 m · KOYU ANTRASİT eldiven + bot · SAĞ uylukta
                   bant (fırça klipsi)
              KISA 1,62 m · BEYAZ eldiven + bot · SOL pazuda bant
              ⛔ "İki figür birbirine benziyor" bulgusu ancak bu ÜÇ
                 kanaldan biri bozulmuşsa geçerlidir; giysi renginin
                 aynı olması TASARIMDIR.
BAŞ/YÜZ       Filmde tam 2 yüz var ve ikisi de 13/13 sahnede kask
              içindedir. Vizör tek parça, optik olarak ŞEFFAF; sıfır
              renk, sıfır ayna kaplaması, sıfır çevre yansıması; yüzler
              her baş açısında okunur [D5 · D79].
              ⭐ İKİ YÜZÜN AYNI KAREDE OKUNDUĞU SAHNE TAM 2'DİR
              (S4 · S9). Diğer sahnelerde en fazla bir yüz okunur ve
              bu bir eksiklik değil, Kart 4 karşı önlemidir.
SIRT PANELİ   ⭐ D79 UYARLAMASI — bulgu yazılmadan ÖNCE okunur:
              giysinin sırtı DÜZ, GÖMME, dikdörtgen bir radyatör
              panelidir. Sırt silüeti 13/13 sahnede DÜMDÜZDÜR: çanta 0,
              tank 0, hortum 0, kablo 0, çıkıntı 0. Panel bir ÜNİTE
              DEĞİLDİR ve dışarı taşmaz. "Sırtta bir şey var" bulgusu
              yalnız silüet BOZULMUŞSA geçerlidir.
ULAŞAMAMA     ⭐ FİLMİN NOVUM'U: omuz eklemi sırt paneline 40 derece
              yetişmez; hiçbir figür kendi sırtına dokunmaz,
              uzanmaz, fırça tutmaz — 0 kare. S11'in 0.5-1.5
              saniyesinde kol kendi omzuna gider ve YETİŞMEZ.
              ⛔ "Neden kendi sırtını temizlemiyor" sorusu bir bulgu
                 değildir; filmin ÖNERMESİDİR [D87/D116 önerme kapısı].
TEMAS         İki figür arasındaki TEK temas fırça ucunun sırt
              panelidir. El-el 0 kare · sarılma 0 kare · omuz tutma
              0 kare · taşıma 0 kare · itme 0 kare.
              ⛔ S7'de düşen figüre YARDIM EDİLMEMESİ TASARIMDIR
                 (temas bütçesi), duygusuzluk bulgusu değildir.
BİNİŞ         0 kare [D69]. Merdiven tırmanma, kapaktan girme, kalkış
              yok; film merdivenin dibinde biter. "Final kesik"
              bulgusu DÜŞER — genişleme finalidir.
KOŞU/ZIPLAMA  0 kare. İki figürün de yürüyüşü ölçülüdür; 0,40 g'de
              adım uzun ve iniş yavaştır. Koşu ve zıplama TASARIM
              GEREĞİ yoktur (klon riski).
KONUŞMA       0 replik · ağızlar hiçbir karede konuşma için oynamaz.
              Tek "söz" S11'in 7.0 s'sindeki iki eldiven tıklamasıdır.
              "Diyalog yok" bulgusu TASARIMDIR [③ SES merceği için].
TOZ ORANI     0,25 mm/dakika, her yukarı ve geri bakan yüzeyde.
              Fırça darbesi 0,25 mm kaldırır (8 darbe = DURUM 0).
              Birikinti kabuğuna düşmek TEK SEFERDE +9,5 mm.
              Kaldırılan toz DÜZ AŞAĞI, 0,25 m/s, asılı kalmaz,
              girdap yapmaz, sıvı gibi akmaz, yukarı savrulmaz [D39].
              Rüzgâr (0,5 m/s) hiçbir tozu kaldırmaz — filmdeki her
              toz hareketinin mekanik bir sebebi vardır.
SIRT SAYACI   ⭐ FİLMİN ANA SAYACI, beş görsel durum:
              DURUM 0 (0,0 mm) doygun gül, hafif parlak
              DURUM 1 (1,0)    ince tebeşir sisi, mat
              DURUM 2 (2,5)    gül yalnız kıvrım ve dikişlerde
              DURUM 3 (5,0)    tebeşir soluk, 20 m'den ova rengi
              DURUM 4 (9,0+)   omuz dikişinde kenarı olan sert kabuk
              Takvim: S1 0/0 · S4 2,0→0 (ikisi de) · S7 UZUN 2,5 /
              KISA 12,0 · S8 KISA 6,0 · S11 KISA 7,5→0 · S12 UZUN 5,5
              (DURUM 3) / KISA 0,5.
              ⛔ Sayaç yalnız FIRÇAYLA geri gider; kendiliğinden
                 azaldığı tek bir kare yoktur. Geri gitme = ihlal.
FIRÇA SAYACI  80 darbelik yük. S4 (16) · S6 (4) · S8 (10) · S10 (30) ·
              S11 (20) = 80. Kıllar S1'de bembeyaz, S9'da yarı gül,
              S12'de tamamen ova rengi; her darbede dökülen perde
              incelir. Bir darbe = 0,30 s, tek yönlü çekiş; ileri
              geri sürtme 0 kare.
FIRÇA VERİMİ  Darbe başına kalkan kalınlık yüzeyin durumuna bağlıdır:
              gevşek üst yük 0,60 mm/darbe · bağlı ya da düşerken
              gövde ağırlığıyla BASTIRILMIŞ film 0,40 mm/darbe.
              S8'de 10 darbe yalnız gevşek 6 mm'yi alır; kalan 6 mm
              bastırılmıştır ve 15 darbe ister — uzun figür bu yüzden
              durur. S11'de 20 darbe × 0,40 = 8,0 mm ≥ 7,5 mm ve panel
              DURUM 0'a iner. ⛔ "Fırça neden bir seferde temizlemiyor"
              bulgusu DÜŞER: verim sayısal olarak kilitlidir.
YERÇEKİMİ     0,40 g — gövde 1,0 m'yi 0,71 s'de düşer. Ağır çekim
              0 kare, hız rampası 0 kare.
IŞIK          ⭐ FİLMDE YAPAY IŞIK YOK — far, seyir lambası, kapak
              ışığı, fener, ekran, uyarı lambası 0 kare. Sönük panel
              ve ışıksız gövde TASARIMDIR, eksik değildir.
              Yıldız 13/13 sahnede EKRAN-SOLDA, 6,0° → 10,2°
              MONOTONİK yükselir (40 saatlik gün: 32 dakikada 4,2°);
              gölgeler 13/13 sahnede EKRAN-SAĞA.
              ⭐ Gölge kenarının YUMUŞAK ve gölge içinin SİYAH
              OLMAMASI ince atmosferde MEŞRUDUR [D41] ve bu filmde
              ZORUNLUDUR: gölgedeki sırtın rengi okunmalıdır. "Gölge
              zayıf / dolgu fazla" bulgusu DÜŞER.
RENK KİLİDİ   İki giysi filmdeki TEK DOYGUN RENKTİR. Ova, gök, üs,
              gemiler, toz: hepsi soluk, tebeşirli, düşük doygunluk.
              Ayrım TONDA değil DOYGUNLUKTA ve PARLAKLIKTADIR.
              ⛔ "Her şey aynı renk" bulgusu TASARIMDIR — filmin
                 tamamı tek bir hue üzerine kurulmuştur ve sayaç
                 doygunlukla okunur.
              ⛔ Post'ta doygunluk oynanmadı; oynanırsa sayaç bozulur.
EKRAN YÖNÜ    Kamera 13/13 sahnede AYNI yöne bakar (ova ekseni
              derinliğe). Yıldız SOL · gölgeler SAĞ · üs ve gömülü
              mekik pad sahnelerinde kameranın ARDINDA kalır. Bu
              yüzden mekik S9'da kadrajda değildir ve S9'un dördüncü
              bakışı KADRAJ DIŞINADIR — bilinçlidir.
SAYAÇLAR      üçü de metinsiz: ① pada mesafe 600→0 m (monotonik)
              ② sırt durumu (palet) ③ fırçanın kılları.
              Ekran, rakam, gösterge, uyarı lambası 0 kare.
METİN         0 kare — gövde yazısı, logo, marka, numara, sembol,
              bayrak, arma hiçbir yüzeyde yok.
SU/ATEŞ       0 kare — buz, kırağı, buğu, sis, bulut, birikinti,
              alev, duman, patlama, kıvılcım, motor jeti yok.
              Gemi hiçbir karede çalışmaz.
CANLI         0 kare — hayvan, kuş, böcek, bitki, mikrobiyal örtü,
              organik hareket yok. Toz MİNERALDİR.
YARA          0 kare — düşüşte kan, yırtık giysi, çatlak vizör,
              sızıntı, buhar yok. Tek sonuç KAPLAMADIR.
EŞ KADRAJ     S0 ↔ S12 (aynı görsel iddia: iki yarı, biri temiz biri
              ova rengi — biri panelde, öteki iki sırtta)
```

---

## ⛔ RUBRİĞE UYARI — bilinçli tasarım kararları, ihlal olarak raporlanmaz

```
· İki figürün AYNI RENK giysi giymesi TASARIMDIR; ayrım boy, eldiven-
  bot rengi ve bant tarafıyla yapılır.
· İkisinin de konuşmaması TASARIMDIR — ses tasarımı eksik değildir.
· Kendi sırtına ulaşamamak filmin ÖNERMESİDİR, mantık hatası değil.
· S7'de düşen figüre dokunulmaması TASARIMDIR (temas bütçesi).
· Sırttaki düz gömme panel D79'un GEREKÇELİ uyarlamasıdır; silüet düz
  olduğu sürece ihlal yoktur.
· 13/13 sabit kamera ve 0 kesme TASARIMDIR.
· Filmde yapay ışık olmaması TASARIMDIR.
· Gölgelerin yumuşak ve dolgulu olması ince atmosferde MEŞRUDUR [D41].
· Paletin tek renk üzerine kurulu olması TASARIMDIR; doygunluk farkı
  filmin sayacıdır.
· Kimsenin gemiye binmemesi ve kalkışın gösterilmemesi TASARIMDIR
  [D69 · genişleme finali] — "kesik final" değildir.
· S0'da insan olmaması TASARIMDIR.
· Gömülü mekiğin hasarsız olması TASARIMDIR: bu bir kaza değil, bir
  bakım eksikliğidir.
```
