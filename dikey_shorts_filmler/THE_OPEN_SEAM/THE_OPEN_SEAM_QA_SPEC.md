# 📋 THE OPEN SEAM — QA SPEC (MOD D girdisi)

> **Ne işe yarar:** QA koşusunda operatörün elinde İKİ dosya olur — rubrik +
> bu dosya. Bu dosya verilmezse koşu MOD V'dir ve **ön koşu** sayılır [D94/D117]:
> skor satırı Ⓥ ⚠️ ŞARTLI girer, 00_INDEX tamlık matrisinde hücre ❌ kalır,
> kesme listeleri ve REMOVE reçeteleri uygulanmaz.
>
> ⚠️ **Film HENÜZ ÜRETİLMEDİ (26.08.2026).** Bu SPEC ilk üretim koşusu için
> yazıldı ve filmle AYNI GÜN depoya indi [D117 · IRON SLOPE'un SPEC'i
> bulunamadığı için altı mercek mod V koşmuştu].
>
> Film dosyası: `THE_OPEN_SEAM_DIKEY_SHORTS.md` (aynı klasör)

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## A BLOĞU — SAHNE SPESİFİKASYONU (① KARE · ⑥ FİZİK rubriklerine)

```
FILM: THE OPEN SEAM
FORMAT: dikey shorts (9:16)
SCENE: <sahne numarası> ya da "Compilation" (tam kurgu)
CLIP LENGTH: 10,005 s (ızgara ÖLÇÜLMÜŞ klip süresinden kuruldu [D124];
             koşuda ffprobe ile ölçülen gerçek süre yazılır)
PIPELINE: text-to-video (her sahnenin ayrıca I2V DEVAM sürümü var)

⚠️ FİLM GERÇEK ZAMANLI DEĞİL — altı sahne, bir hizalanma yaklaşmasının
   117 dakikasından alınmış altı ANdır. Hikâye saatleri:
   S0 T−96 dk · S1 T−71 dk · S2 T−44 dk · S3 T−19 dk · S4 T+0 · S5 T+21 dk
   ⛔ "Sahneler arası süreklilik kopuk" bulgusu YANLIŞTIR: ilan edilmiş
   yapıdır ve gerekçesi fizikseldir (yelpaze 96 dakikada kapanıyor).

CHARACTER: 35 yaşında kadın, buz kabuğu jeofizikçisi · 1,70 m ·
           açık zeytin ten, gözenek dokusu görünür, koyu gözler,
           kalın koyu kaşlar, SOL ağız kenarında küçük soluk yara izi,
           çatlak dudak, arkaya toplanmış koyu saç, SAĞ şakakta iki
           kaçak tel
SUIT: mat KAR BEYAZI sert kabuk yüzey suit'i · **renkli aksan YOK,
      şerit YOK, parlak kenar YOK** — beyaz burada bir renk tercihi
      değil ÖLÇÜM YÜZEYİDİR: üç ayın rengi ancak beyaz bir gövdenin
      üstünde ayrı ayrı okunur (sol yan turuncu, sağ yan mavi-beyaz,
      ön menekşe) · **sırt TAMAMEN DÜZ** (sırt ünitesi/tank/hortum/
      kablo YOK) [D79] · kask **tek parça berrak baloncuk**, tint YOK,
      ayna kaplama YOK, çevre yansıması YOK · göğüs konsolu: düşük
      sıcak AMBER anahtar ışığı (ekran/gösterge DEĞİL) · diz, SOL ön
      kol ve İKİ bot burnu gri aşınmış (her sahnede AYNI yerde) ·
      **hiçbir arma, bayrak, yazı, rakam, sembol yok** · eldivenler
      beyaz ve **6/6 BOŞ** · **KASK LAMBASI YOK ve hiç açılmıyor**
CHARACTER HEIGHT: 1,70 m

GRAVITY: 1,08 g (10,59 m/s²) — sabit, filmin tamamında
ATMOSPHERE: ince N₂+CO₂, yüzeyde 8 kPa, 232 K · ses hızı 310 m/s ·
            saçılma zayıf · RÜZGÂR YOK
            → havada görünür ışık hüzmesi 0 kare
            → 2,8 metrelik yarıkta su ÖLÜ DURGUN
            → dışarısı neredeyse sessiz; duyulan her şey BUZDAN
              BOTLARA İLETİLİR
LOCOMOTION MODE: DÜZ YÜRÜYÜŞ, yalnız S0 ve S2'de, 0,9 m/s, TOPLAM
            11 metre. Botlar kalkar-basar-yük alır; kayma/süzülme
            0 kare. Koşu 0 kare. Zeminden kalkan kırıntı 0 kare
            (zemin kar değil CAM). Diğer dört sahnede kadın duruyor,
            diz çöküyor ya da kalkıyor.

LENS: **24 mm KÜRESEL, 6/6 SAHNEDE — TEK LENS.**
      (anamorfik YASAK — 8 kPa'da saçılma yok, her parlama artefakttır
      ve bu filmde artefaktla gerçek ışık kordonunu ayırt etmek
      imkânsızlaşır)
CAMERA HEIGHT: S0 0,90 m · S1 0,22 m · S2 0,90 m · S3 0,45 m ·
      S4 0,22 m · S5 0,90 m   (kamera film boyunca yere iner ve döner)
CAMERA DISTANCE: S0 20 m · S1 5,0 m · S2 20 m · S3 9,0 m · S4 5,0 m ·
      S5 20 m (hepsi promptta metre olarak)
CAMERA MOVE: **6/6 TAM LOCKOFF** — üç kurulum da buza oturur.
      Atım sarsıntısında bile kamera sabittir (kamera dikişin
      ÖTE yakasında değil, aynı blokta). Pan/tilt/dolly/zoom/
      sarsıntı/hız rampası 0 kare
      ⛔ Bu satır KLİP İÇİ karardır ve sahneler ARASI kurulumu anlatmaz;
      onu SETUP SEQUENCE satırı anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE: A · B · A · C · D · A          (26.08.2026'da eklendi)
      A = 24 mm · 0,90 m · 20 m · ALT AÇI   → S0 · S2 · S5
      B = 24 mm · 0,22 m · 5,0 m · ÜST AÇI  → S1
      C = 24 mm · 0,45 m · 9,0 m · ALT AÇI  → S3
      D = 24 mm · 0,22 m · 5,0 m            → S4
      kurulum sayısı 4 · 6 sahne → ACI_YAYI §4 bandı (≥3) ✅
      ardışık ikili hiçbir yerde aynı değil → §3 ✅
      A ↔ A döngüsel kapanış (S0/S5) — §9 son madde, bilinçli
      ⚠️ B ile D aynı yükseklik ve mesafede; ayıran tek şey D'de açının
      kılavuz sözlüğüyle yazılmamış olması. Aynı kurulumsa dizi
      A·B·A·C·B·A olur ve kurulum sayısı 3'e iner — bant yine tutar.
ANGLE ARC: **2 açı tipi — ALT AÇI (S0·S2·S3·S5) · ÜST AÇI (S1)**
      🚨 AÇIK MADDE (26.08.2026): §2 en az 3 açı tipi ister; bu film 2
      taşıyor. S4 (dikişin açıldığı sahne — filmin doruğu) açısı
      promptta kılavuz sözlüğüyle yazılmamış. Doruk sahnesi ACI_YAYI
      §9'a göre EN YÜKSEK kontrast sıçramasını taşımalı: üçüncü tip
      buradan kazanılır (dikeyde tepe/kuşbakışı — §6, zemin teması
      için de doğru açı).
LIGHT SOURCES: **TAM ÜÇ, hepsi gökyüzünde, hepsi farklı yükseklikte
      ve farklı renkte** — (a) ARDE: 7,04° çapında, KENDİ LAVIYLA
      yanan turuncu · (b) NIVE: 2,33°, keskin kenarlı mavi-beyaz buz
      ayı · (c) VELUM: 1,86°, kenarsız menekşe-gül puslu ay.
      Güç oranı yaklaşık 5 : 3 : 1.
      ⛔ BAŞKA IŞIK YOK: yıldız ufkun ALTINDA · kask lambası YOK ·
      yapay ışık 0 kare · havada hüzme 0 kare
FILL LIGHT ALLOWED: hayır — ama hiçbir gölge de nötr gri DEĞİLDİR:
      her gölgenin içi, onu YAPMAYAN iki ayın renginin karışımıdır
VEHICLE/STRUCTURE: **YOK.** Kadrajda insan yapımı tek nesne yoktur
      (suit hariç). Araç, bina, alet, direk, iz 0 kare
DIALOGUE EXPECTED: **YOK — film tamamen repliksizdir** (tasarım, eksik değil)
AUDIO LAYERS (≤3): ① nefes + kask fanı (60 saniyenin 60'ında, hiç
      kesilmez) ② buzdan iletilen ses: bot sürtünmesi + ÜÇ derin
      darbe (32,6 · 41,8 · 51,4 s) + S5'in uzun sürtünmesi
      ③ müzik yatağı (96 BPM) · ⛔ SU HİÇ SES ÇIKARMAZ
```

---

## B BLOĞU — KURGU VE ŞERİT (④ HİKAYE · kurgu kapısı ④)

```
THEME (intended): ZEMİN  ⏸️ (TEMA_MUHENDISLIGI §3b · depoda doğmuş aday
      etiket, §3 tablosunda yok — pazar/kuşak verisi ÖLÇÜLMEDİ)
      Tek cümle: "Bu film, üstünde durduğun şeyin ne olduğunu öğrenmek
      hakkında." — cümlede novum kelimesi yok ✅
THEME SCENES (§5 matrisi): S0 · S1 · S2 · S3 · S4 · S5
      eldivenin cama düz basması (S1 · S5) · bot burnunun buza
      sürtünmesi (S0 · S2) · başın arkaya yatışı (S0 · S4) ·
      sarsıldığında ağırlığını alçaltması (S3 · S4)
      Payoff (§6): S1'de "cam" olan zemin S4'te gerçekten açılır,
      S5'te başka bir camla kapanır ✅
SCENE / SHOT / CLIP COUNT: 6 / 6 / 6
RAW FOOTAGE: 6 klip × 10,005 s = 60,03 s
RUNTIME: 60,03 s ± 0,5 s
TRIM BUDGET: 0,0 s — ızgara zaten aracın klip süresine yazıldı [D124]
TARGET ASL BAND: 10,0 s — sabit ızgara, eğri yok (bilinçli sapma [D74])
İNSAN ŞERİDİ [D118]: 111111
EKRAN METNİ: 0,0 saniye — başlık kartı DAHİL [D61a/D70]
KESİLEMEZ SAHNELER: S0 (kanca + tohum) · S2 (KEŞİF: üç yayın
      kesişmesi) · S3 (atım + merkezi seçim) · S4 (açık su + üç disk)
      · S5 (kapanma + döngü)
DOĞAL DORUK: S4 · 41,8-43,0 s — 2,2 metrelik atım ve dikişin 2,8 m'ye
      açılması; ardından suda üç renkli disk
TOHUM → KARŞILIK: S0 07,2-08,1 (uzakta, camın içinde açık renkli dar
      bir şerit — tepkisiz) → S2 26,0-30,0 (aynı şerit yakından: üç
      yayın kesişmesi + 15 cm'lik dikiş) → S5 55,4 (aynı yerde SÜT
      BEYAZI kalıcı şerit)
ÜÇ ATIM (ses ve görüntü birlikte):
      S3 · 32,6 s → 1,2 m / 0,5 s
      S4 · 41,8 s → 2,2 m / 1,1 s
      S5 · 51,4 s → kapanma başlangıcı, 4 saniyede tamamlanır
DÖNGÜ NOKTASI: 60,0 → 0,0 — jest eşleşmesi (S1: eldiven CAMA düz ·
      S5 sonu: aynı eldiven aynı jestle SÜT BEYAZI ŞERİDE düz;
      değişen tek şey elinin altındaki şeyin artık saydam olmaması)
⚠️ SERT KESME SAYISI 5 — KURGU_RITMI §3'ün ≤3 bandının ÜSTÜNDE ve
      bilinçli [D74]: film gerçek zamanlı değil, altı ayrı an; iki an
      arasında 25 dakika varken görsel perde YALAN olur.
      Telafi: BEŞ kesmenin BEŞİ de ses köprülü (%100 — depodaki en
      yüksek oran), üçü J ikisi L, köprü malzemesi tek ve diegetik.
```

---

## C BLOĞU — KİLİTLER VE SIK YAPILAN YANLIŞ OKUMALAR (⑩ önerme kapısı)

```
✅ TASARIM — bulgu DEĞİLDİR:
   · Zeminin SAYDAM olması → filmin varlık şartı. "Buz opak olmalı"
     bulgusu YANLIŞTIR: bu dünyada toz ve kara yok, kabuk aşağıdan
     yavaş dondu ve tek kristal olarak büyüdü
   · ÜÇ gölge ve üçünün AYRI BOYDA olması → üç ay, üç yükseklik.
     "Çoklu gölge devamlılık hatası" bulgusu YANLIŞTIR
   · Hiçbir gölgenin nötr gri OLMAMASI → her gölge, onu yapmayan iki
     ayın renginin karışımıyla dolar. Renk sızması değil, fizik
   · Üç kordonun ÜÇ AYRI DERİNLİKTE bitmesi → buz kırmızıyı önce yer
     (buzul buzunun mavi görünme sebebi). Tutarsızlık değil, cetvel
   · Çatlakların DÜZ OLMAMASI → sikloid; kabuk dönerken gel-git
     geriliminin yönü değişiyor. Europa'da doğrudan gözlenmiştir.
     "Çatlaklar doğal görünmüyor" bulgusu YANLIŞTIR
   · Suyun HİÇ KIPIRDAMAMASI → rüzgâr yok, yarık iki buz duvarıyla
     korunuyor, kabuk yüzüyor. "Su ölü/cansız görünüyor" bulgusu
     YANLIŞTIR — tasarım budur ve Kart 1'in panzehiridir
   · Suda kadının YANSIMAMASI → tasarım kilidi [D20/Kart 4].
     "Yansıma eksik" bulgusu YANLIŞTIR
   · Buzun UFALANMAMASI → dikiş açılırken bloklar birbirinin yanından
     KAYAR (yanal atım), kırılmaz. Europa'da ölçülü
   · S5'teki şeridin OPAK olması → hızlı donan buz hava hapseder ve
     süt beyazı çıkar; çevresindeki 60 metre yavaş donduğu için cam
   · Kadının çok az hareket etmesi (11 m yürüyüş) → tasarım; film
     bir ölçüm filmidir, kovalamaca değil
   · Repliksizlik → ilan edilmiş kısıt [D113], düşük puan sebebi değil

🔴 GERÇEK İHLAL — bulgu SAYILIR:
   · Zeminin OPAK çıkması: kar, kırağı, buzul dokusu, beyaz kırık
     pusu, kabarcık  ← FİLMİN 1 NUMARALI KAPISI
   · Gölge sayısının üç OLMAMASI ya da üçünün aynı boyda olması
   · Çatlakların DÜZ çizgi olması
   · **Suyun kıpırdaması:** dalga, kırışık, sprey, damla, köpük,
     akıntı, girdap — herhangi biri
   · **Suda insan yansıması** ya da ikinci figür
   · Suya TEMAS (eldiven, bot, herhangi bir şey)
   · Buzun ufalanması, parçalanması, yarığa parça düşmesi
   · S5'te kristal/buz dikeni büyümesi (şerit bir YÜZEY değişimidir)
   · Havada görünür ışık hüzmesi, god ray, ışık konisi
   · Dördüncü ay, halka sistemi, yıldız alanı, aurora
   · Kask lambası ya da herhangi bir yapay ışık
   · Ekranda herhangi bir yazı/rakam/logo/arma (başlık kartı dahil)
   · Kamera hareketi (6/6 lockoff kilidi)
   · Suit'te renkli aksan, şerit ya da reflektör
   · Sırt ünitesi/tank/hortum, vizör tinti, ayna kaplama
```

---

## D BLOĞU — SAYISAL KİLİT LİSTESİ (⑥ FİZİK merceğinin NUMERIC LOCK LIST'i)

```
GRAVITY: 1.08 g (10.59 m/s²), constant, whole film
ATMOSPHERE: 8 kPa N₂+CO₂, 232 K, speed of sound 310 m/s, no wind
LOCKS:
LOCK: floor = one sheet of optically clear ice 60 m thick, single
      crystal, no bubbles, no frost, no white, no fracture haze
LOCK: below the shell, 60 km of liquid water and NO sea floor
LOCK: exactly 3 moons, 6/6 scenes — angular widths 7.04° / 2.33° /
      1.86°, strength ratio ≈ 5 : 3 : 1
LOCK: exactly 3 shadows from every object, 6/6 scenes, three different
      lengths (figure height 1.70 m):
      S0 5.93 / 2.52 / 1.38 m   S1 4.67 / 2.52 / 1.48 m
      S2 3.65 / 2.52 / 1.70 m   S3 3.07 / 2.52 / 2.03 m
      S4 2.67 / 2.52 / 2.38 m   S5 2.34 / 2.52 / 2.72 m
LOCK: the middle shadow is 2.52 m in ALL SIX scenes (fixed reference)
LOCK: shadow fan angle 35° → 29° → 20° → 11° → 3° → −4° (reversed)
LOCK: no shadow is neutral grey — each is filled by the two moons
      that did not cast it
LOCK: three light cords inside the ice end at three depths —
      orange 10 m · violet-rose 29 m · blue-white through all 60 m
      and on into the water
LOCK: at the thin crossing the shell is 9 m, so even the orange cord
      passes through it — this single image is the film's discovery
LOCK: every crack is a chain of long shallow arcs; straight cracks
      = 0 frames
LOCK: seam width 0.15 m (S2) → 1.4 m (S3) → 2.8 m (S4) → closed (S5)
LOCK: tidal sum 28.1 m (opposed) → 54.7 m (aligned); the three
      component tides are 41.4 m + 5.1 m + 8.2 m
LOCK: three strike-slip jumps, rigid whole-block sideways slides —
      1.2 m / 0.5 s (S3) · 2.2 m / 1.1 s (S4) · closure over 4 s (S5)
LOCK: slab tilt 6°, drop 0.40 m (S3), and the 0.40 m step is
      PERMANENT in S5
LOCK: shattering / crumbling / fragments falling into the seam
      = 0 frames
LOCK: LIQUID CONTACT SCHEDULE — contact 0 frames in 6/6 scenes;
      water visible in 2 of 6 scenes (S4, S5) for 14.0 s total;
      closest approach 1.5 m; waves/ripples/spray/droplets/foam/
      current/whirlpool = 0 frames; human reflection in water
      = 0 frames
LOCK: S5 band = 2.8 m wide, opaque milk white, matt; growing
      crystals / ice spikes = 0 frames
LOCK: walking only in S0 and S2, 0.9 m/s, 11 m total
LOCK: exactly 1 human, 6/6 scenes; helmet closed 6/6; flat back 6/6;
      zero visor reflection 6/6; helmet lamp = 0 frames
LOCK: camera movement = 0 in all six scenes
LOCK: on-screen text = 0.0 s
```

---

## E BLOĞU — MAKİNEYLE KOŞULACAK BEŞ KAPI [D125]

> Bu ölçümler modele SORULMAZ. Sayı makineden alınır.

```
① CAM KAPISI (S0) — filmin varlık şartı
   ffmpeg -i S0.mp4 -vf "select='eq(n\,120)'" -vsync 0 k.png
   Zeminin (alt üçte bir) ortalama parlaklığı / gökyüzünün ortalama
   parlaklığı ölçülür.
   ⛔ > %20 ise, ya da zeminde kar/kırağı/beyaz doku varsa
      → ÜRETİM DURUR, film üretilmez.
   Ayrıca aynı karede en az İKİ ayrı derinlikte ışık yapısı okunmalı.

② ÜÇ GÖLGE KAPISI (S0)
   Aynı karede gölge sayısı sayılır ve en uzun/en kısa oranı ölçülür.
   ⛔ Gölge sayısı 3 değilse ya da oran 2,0'ın altındaysa sahne
      REDDEDİLİR (tasarım oranı 5,93/1,38 = 4,3).

③ ATIM KAPISI (S3) [D127]
   ffmpeg -i S3.mp4 -vf fps=24 -ss 2.2 -t 1.4 k_%02d.png
   Uzak dudağın piksel yer değiştirmesi ve süresi ölçülür.
   ⛔ > 1,5 saniye sürerse ya da buz ufalanırsa sahne REDDEDİLİR.

④ SU KAPISI (S4) [KART 1 — 🔴]
   ffmpeg -i S4.mp4 -vf "crop=1080:200:0:1150,signalstats" -f null -
   Su bandının kare-kare farkı ölçülür (hareket enerjisi).
   ⛔ Ölçülebilir bir hareket varsa, ya da karede insan biçimli bir
      yansıma varsa, ya da herhangi bir şey suya değiyorsa
      → sahne REDDEDİLİR.

⑤ KURGU KAPISI (tam teslim) [D124]
   ffprobe -v error -show_entries format=duration -of csv=p=0 teslim.mp4
   süre = klip_sayısı × ölçülen_klip_süresi ± 0,5 s
   Kesme ızgarası: (n − 1) × klip_süresi  [D115]
   Ekran metni: 0,0 s — başlık kartı dahil
```
