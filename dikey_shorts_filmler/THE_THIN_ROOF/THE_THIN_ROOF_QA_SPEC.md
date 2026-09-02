# 📋 THE THIN ROOF — QA SPEC (MOD D girdisi)

> **Ne işe yarar:** QA koşusunda operatörün elinde İKİ dosya olur — rubrik +
> bu dosya. Bu dosya verilmezse koşu MOD V'dir ve **ön koşu** sayılır [D94/D117]:
> skor satırı Ⓥ ⚠️ ŞARTLI girer, 00_INDEX tamlık matrisinde hücre ❌ kalır,
> kesme listeleri ve REMOVE reçeteleri uygulanmaz.
>
> ⚠️ **Film HENÜZ ÜRETİLMEDİ (27.08.2026).** Bu SPEC ilk üretim koşusu için
> yazıldı ve filmle **aynı gün** depoya indi [D117].
>
> Film dosyası: `THE_THIN_ROOF_DIKEY_SHORTS.md` (aynı klasör)

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## A BLOĞU — SAHNE SPESİFİKASYONU (① KARE · ⑥ FİZİK rubriklerine)

```
FILM: THE THIN ROOF
FORMAT: dikey shorts (9:16)
SCENE: <sahne numarası> ya da "Compilation" (tam kurgu)
CLIP LENGTH: 10,005 s (plan ızgarası ÖLÇÜLMÜŞ klip süresinden kuruldu [D124];
             koşuda ffprobe ile ölçülen gerçek süre yazılır)
PIPELINE: text-to-video (her sahnenin ayrıca I2V DEVAM sürümü var)

CHARACTER: 33 yaşında kadın, volkanik arazi jeoloğu · 1,68 m ·
           koyu sıcak kahve ten, gözenek dokusu görünür, SOL şakakta
           ince ter parlaklığı, koyu kahve gözler, kalın koyu kaşlar,
           BURUN KEMERİNDE küçük soluk yara izi, çatlak alt dudak,
           alçak topuz saç, SOL şakakta iki kaçak tel
SUIT: mat TEBEŞİR GRİSİ yumuşak kabuk yüzey suit'i · omuzlarda ve dış
      baldırda tek bant **soluk çivit** (kadrandaki TEK doygun soğuk
      renk, TAM 1 kişide) · **sırt TAMAMEN DÜZ** (sırt ünitesi/tank/
      hortum/kablo YOK) [D79] · kask **sert kabuk + geniş düz vizör**,
      optik olarak berrak, tint YOK, ayna kaplama YOK, çevre yansıması
      YOK · her iki diz, her iki ön kol ve iki bot burnu PAS RENGİ
      tozla aşınmış (her sahnede AYNI yerde) [D42] · **hiçbir arma,
      bayrak, yazı, rakam, sembol yok** · eldivenler tebeşir grisi,
      avuç içleri koyu gri, **6/6 BOŞ**
CHARACTER HEIGHT: 1,68 m

GRAVITY: 0,379 g (3,71 m/s²) — sabit, filmin tamamında
ATMOSPHERE: ince CO₂, yüzeyde 610 Pa, 243 K · ses hızı 240 m/s (240 Hz
            altı) / 250 m/s (240 Hz üstü) · yüksek frekans ~8 metrede
            biter → dışarıda duyulan tek şey TEMASTIR
            ⭐ SAÇILMA VAR: askıdaki toz gerçek bir dolgu ışığı üretir.
            Gölgeler YUMUŞAK KENARLI ve İÇİ DOLUDUR. Bu, deponun beş
            vakum filminin TERSİDİR ve bu filmin 1 numaralı kapısıdır.
            ⛔ Havada asılı toz, pus, sis, hüzme YOKTUR — saçılma
            GÖKYÜZÜ ışığıdır, kadrajda görünen bir perde değil.
LOCOMOTION MODE: DÜZ YÜRÜYÜŞ · yalnız S0 (yaklaşık 5 m) ve S5 (yaklaşık
            1,3 m) · 0,62 m/s · botlar kalkar-basar-yük alır ·
            kayma/süzülme/sıçrama/koşu 0 kare · KALKAN TOZ 0 KARE
            (zemin rüzgârın temizlediği bazalt kaldırımı; toz yalnız
            eklemlerin içinde ve hareketsiz — TASARIM)
            ⛔ S1-S4'te kadın diz üstünde, çömelmiş ya da yüzükoyun;
            "hareketsizlik" bulgu DEĞİLDİR

LENS: 32 mm KÜRESEL → S0 · S2 · S4 · S5  |  75 mm KÜRESEL → S1 · S3
      (anamorfik YASAK — ince atmosferde yatay parlama artefakttır)
CAMERA DISTANCE: S0 9,0 m · S1 4,0 m · S2 15,0 m · S3 4,0 m ·
      S4 15,0 m · S5 9,0 m (hepsi promptta metre olarak)
CAMERA HEIGHT: A kurulumu 0,35 m · B kurulumu 1,55 m · C kurulumu 9,00 m
CAMERA PITCH: A 0° · B 0° · C −31,0° (aşağı) · eğik/Dutch açı 0,0° · 6/6
CAMERA MOVE: **6/6 TAM LOCKOFF** — A ve B yere oturan tripod, C bir lav
      sırtının üstünde oturan tripod.
      Pan/tilt/dolly/zoom/sarsıntı/hız rampası 0 kare
      ⛔ Bu satır KLİP İÇİ karardır ve sahneler ARASI kurulumu anlatmaz;
      onu SETUP SEQUENCE satırı anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE: A · B · C · B · C · A
      A = 32 mm · 0,35 m · 9,0 m · ALT AÇI        → S0 · S5
      B = 75 mm · 1,55 m · 4,0 m · GÖZ HİZASI     → S1 · S3
      C = 32 mm · 9,00 m · 15,0 m · ÜST AÇI       → S2 · S4
      kurulum sayısı 3 · 6 sahne → ACI_YAYI §4 bandı (≥3) ✅
      ardışık ikili hiçbir yerde aynı değil → §3 ✅
ANGLE ARC: **3 açı TİPİ — alt açı (S0·S5) · göz hizası (S1·S3) ·
      üst açı (S2·S4)** [KAMERA_ACISI §2 eşiği ≥3 ✅]
      ⭐ Açı tipi bu filmde süsleme değil, NOVUMUN TAŞIYICISIDIR:
      kadının göremediğini kamera yalnız 9,00 metreden görüyor.
SCALE LADDER: WS · MS · WS · MCU · WS · MS→WS
      ardışık kademe farkı 1 · 1 · 2 · 2 · 1 (iki ŞOK BANDI, §3 tavanı)
LIGHT SOURCES: (a) TEK güneş — 0,35° çapında, kadrajın SAĞ ÜST DIŞINDA,
      30,7° yükseklikte, kadının ARKASINDA; 60 saniyede 0,24° iner
      (pratik olarak sabit) · (b) GÖKYÜZÜ DOLGUSU — atmosferik saçılma,
      gölgelerin içini dolduran gerçek ışık · (c) SEKTİREN OKRA DUVAR —
      74 m ötedeki güneş alan karşı duvar, S3'ün çıkıntısını gösteren
      ışık · (d) VİZÖR İÇİ KONSOL — çene altı 15 cm, yüzü camın içinde
      okutur; 49,32'de kayaya kapanır. Başka kaynak YOK
FILL LIGHT ALLOWED: **EVET — ve ZORUNLU.** Gölge içleri DOLU, kenarlar
      YUMUŞAK. Mutlak siyah gölge içi = İHLAL
VEHICLE/STRUCTURE: **YOK.** Kadrajda insan yapımı tek nesne kadının
      suit'idir. Araç, bina, alet, anten, ekran, iz 0 kare
DIALOGUE EXPECTED: **YOK — film tamamen repliksizdir** (tasarım, eksik değil)
      ⛔ D122 replik formülü bu filmde KOŞULMAZ: replik sayısı 0.
      Formülün kaydı: replik(S_n) = hook + (n−1) × klip + TIMELINE ofseti
AUDIO LAYERS (≤4): ① kask içi nefes + alçak fan (60,03 saniyenin
      60,03'ünde, hiç kesilmez [D83]) ② gövdeden İLETİLEN temas sesleri
      (bot, diz, eldiven, göğüs, çakıl) ③ müzik yatağı (58 BPM, 2,60'ta
      girer, 58,43'te çekilir) ④ dış hava sesi: YOK — ve bu tasarımdır
      (610 Pa'da ses taşınmaz)
```

---

## B BLOĞU — KURGU VE ŞERİT (④ HİKAYE · kurgu kapısı ④)

```
THEME (intended): YALNIZLIK  (TEMA_MUHENDISLIGI §3 tablosu · §4'e göre
      dikey-uyumlu "anlık durum" teması · §3c'nin HİÇ KULLANILMAMIŞ
      listesinden seçildi)
      Tek cümle: "Bu film, yalnızlığın ne kadar büyük olabileceğini
      görmek hakkında." — cümlede novum kelimesi yok ✅
      ⭐ Cümle TAKAS kalıbı DEĞİLDİR ("X için Y'den vazgeç" yapısı yok) —
      §3c moratoryumu bu dosyada TUTULDU (depo beş filmde üst üste
      takas kalıbı yazmıştı)
THEME SCENES (§5 matrisi): S0 · S1 · S2 · S3 · S4 · S5 (dokuz indeks)
      negatif alan ≥%65 (S0 · S2 · S4 · S5) · içe kapanan kinesik
      (S1 · S3 · S4) · nesne indeksi: kendi gölgesi (S0 · S5) ve
      çakıl (S3 · S4) · payoff: tek AÇILMA jesti S5'te (ayağa kalkış)
SCENE / SHOT / CLIP COUNT: 6 / 6 / 6
RAW FOOTAGE: 6 klip × 10,005 s = 60,03 s
RUNTIME: 60,03 s ± 0,5 s
TRIM BUDGET: 0,0 s — kırpma yoktur; ızgara zaten aracın klip süresine
      yazıldı [D124]. Araç başka bir süre veriyorsa kırpma PLANDA sahne
      sahne yazılır, yoksa kurgu kırpmaz [D100]
TARGET ASL BAND: 10,0 s — sabit ızgara, eğri yok (bilinçli sapma [D74];
      gerekçe film dosyasının "Plan satırları" bölümünde)
KESME IZGARASI [D115]: S0 0,000 · S1 10,005 · S2 20,010 · S3 30,015 ·
      S4 40,020 · S5 50,025 · bitiş 60,030
İNSAN ŞERİDİ [D118]: 111111
FİNAL VURUŞ KANITI [D141]: S5 · 57,0 s · ovada ÜÇ dairesel çöküntü,
      ufka giden dümdüz bir hatta, sayılabilir. Tek kareyle koşulur:
        ffmpeg -ss 57.0 -i teslim.mp4 -frames:v 1 kanit.jpg
      ⛔ 3 tane görünmüyorsa FİNAL TESLİM EDİLMEMİŞTİR — klip sayısı,
        süre ve şerit tutsa bile kurgu kapısı DÜŞER.
DÖNGÜ KANITI [D141]: ilk kare (0,10 s) ile son kare (59,90 s) yan yana —
      aynı kurulum (A) · aynı ölçek · aynı ışık · aynı jest. Arkasına
      eklenen HER KARE döngüyü öldürür, başlık kartı dâhil.
EKRAN METNİ: 0,0 saniye — başlık kartı DAHİL [D61a/D70]
KESİLEMEZ SAHNELER: S0 (kanca + tohum + kapak anı) · S2 (asimetri anı /
      halkanın kapanışı) · S4 (merkezi seçim + çakıl) · S5 (twist +
      döngü)
DOĞAL DORUK: S5 · 56,53-58,03 — ayağa kalkış ve zincirin okunması
TOHUM → KARŞILIK: S0 06,20-06,90 (kaldırımdaki hafifçe bükülmüş TEK
      çatlak, 0,70 s, tepkisiz, vurgusuz) → S2 22,41 (aynı çizgi,
      9,00 metreden KAPALI HALKA) → S5 56,53-58,03 (halka + ovada üç
      tane daha)
DÖNGÜ NOKTASI: 60,03 → 0,00 — jest eşleşmesi (S5 sonu: sağ bot önde,
      baş kendi gölgesini takip ederek dönüyor · S0 başı: BİREBİR aynı
      jest, aynı kurulum, aynı ışık, aynı ölçek)

MUTLAK ZAMAN ÇİZELGESİ (kurgu kapısının okuyacağı liste)
  04,20        gölgenin ucu kesilir  ← KANCANIN KENDİSİ
  06,20-06,90  TOHUM: hafifçe bükülmüş çatlak (0,70 s)
  07,40        diz çöküş · KAPAK ANI
  14,81-16,61  birinci avuç basınç testi (1,80 s)
  22,41        ⭐ ASİMETRİ ANI — halka kapanır, izleyici öne geçer
  32,02        çıkıntı görünür (plakanın altında gün ışığı)
  34,02-35,82  EL YUVASI — avuç düz, kadraj payı ≥%28 (1,80 s)
  38,42        çakıl bir kez 25° sallanır ve geri düşer
  43,22-46,82  çakıl 0,40 m yuvarlanır (3,60 s) ve çatlağa girer
  48,10-49,32  MERKEZİ SEÇİM — yüzükoyun uzanma
  49,32        vizör içi ışık tek çene kenarına iner (BEDEL)
  50,03-54,03  halkanın geçilmesi (yüzükoyun, 4,00 s)
  55,63        ayağa kalkış — filmin tek AÇILMA jesti
  56,53-58,03  TWIST: ovada üç çöküntü daha, ufka kadar
  58,53        adım atar — döngü kurulur
  60,03        son kare = 0,00 karesi
```

---

## C BLOĞU — KİLİTLER VE SIK YAPILAN YANLIŞ OKUMALAR (⑩ önerme kapısı)

```
✅ TASARIM — bulgu DEĞİLDİR:
   · GÖLGELERİN İÇİNİN DOLU ve KENARLARININ YUMUŞAK olması → ince
     atmosfer saçılma yapar; gölge içi dolgu MEŞRUDUR [ortam kartı
     §3.2]. "Gölgeler yeterince sert değil" bulgusu YANLIŞTIR ve bu
     rubriğin bu filmdeki en olası hatasıdır (depoda beş vakum filmi
     var, hepsi mutlak siyah gölge yazıyordu)
   · PİTİN İÇİNİN S0 ve S5'te GÖRÜNMEMESİ → 0,35 metre kamera
     yüksekliğinde yakın kenar ötesini fiziksel olarak kapatır.
     Hesap: 74 × 0,35 / 10,1 = 2,57 m. Bu bir "eksik reveal" değil,
     filmin merkezî cümlesidir
   · TABANIN HİÇBİR SAHNEDE GÖRÜNMEMESİ → en yüksek kurulumdan bile
     ışın 41,4 metreye iner, taban 46,0 metrededir. "Dip gösterilmemiş"
     bulgusu YANLIŞTIR
   · ÇATLAĞIN S0/S1/S3'te DÜZ, S2/S4'te EĞRİ görünmesi → aynı çatlak.
     5,8 m yarıçapta 2,0 m'lik yay 8,7 cm sapar. Süreklilik hatası
     DEĞİL, filmin novum'u
   · ÇAKILIN YAVAŞ YUVARLANMASI → 1,3° eğimde 0,379 g'de ivme
     0,060 m/s²; 0,40 metre 3,6 saniye sürer. Ağır çekim DEĞİL
   · GÖKYÜZÜNÜN TEREYAĞI-KARAMEL olması → askıdaki ince toz. Renk
     düzeltme hatası değil, gezegenin gerçek gündüz rengi
   · GÖKYÜZÜNDE YILDIZ, BULUT, AY OLMAMASI → gündüz ve tozlu atmosfer
   · KADININ 4 SAHNEDE YERDE olması → tasarım; film bir bakış açısı
     filmidir, aksiyon değil
   · REPLİKSİZLİK → ilan edilmiş kısıt [D113], düşük puan sebebi değil
   · DIŞARIDA SES OLMAMASI → 610 Pa'da ses taşınmaz; duyulan her şey
     temas ya da kask içi. "Ses tasarımı eksik" bulgusu YANLIŞTIR
   · S4'te YÜZÜN KARARMASI → göğüs konsolu kayaya kapanıyor. Bu bir
     IŞIK olayıdır; vizör durumu DEĞİŞMEZ (kapalı, berrak, tintsiz)
   · KALKAN TOZ OLMAMASI → zemin rüzgârın temizlediği bazalt kaldırımı;
     toz yalnız eklemlerin içinde. Tasarım kararı, eksik değil

🔴 GERÇEK İHLAL — bulgu SAYILIR:
   · S2 ya da S4'te halkanın KAPALI BİR EĞRİ olarak okunmaması —
     düz çıkması, kesik çıkması, diğer eklemlerden ayırt edilememesi
     ← FİLMİN 1 NUMARALI KAPISI
   · S0, S1 ya da S3'te aynı çatlağın EĞRİ olarak çizilmesi
   · Herhangi bir gölgenin içinin MUTLAK SİYAH ya da kenarının JİLET
     KESKİN olması
   · Havada asılı toz, toz bulutu, savrulan toz, botun kaldırdığı toz,
     duman, alev, kıvılcım, pus, sis, ışık hüzmesi
   · Rüzgâr belirtisi: çırpınan kumaş, savrulan herhangi bir şey
   · Halka çatlağın GENİŞLEMESİ, açılması, çatırdaması; herhangi bir
     sarsıntı, çökme ya da kaya düşmesi
   · Pitin TABANININ görünmesi
   · Çakılın havada uçması, zıplaması, takla atması, yön değiştirmesi,
     ya da S3'te yuvarlanması (S3'te yalnız SALLANIR)
   · Ağır çekim, hız rampası, hareket bulanıklığı izi
   · Kamera hareketi (6/6 lockoff kilidi)
   · İkinci insan, yansımada insan, klon, ikinci çivit bant
   · Sırt ünitesi/tank/hortum/kablo, vizör tinti, ayna kaplama
   · Ekranda herhangi bir yazı/rakam/logo/arma (başlık kartı dahil)
   · Güneş diskinin kadraja girmesi, parlama, hale, bloom
   · S5'te kadının ayağa KALKMAMASI (twist'in mekanizması silinir)
   · S5'te son karenin S0'ın ilk karesiyle eşleşmemesi (döngü ölür)
```

---

## D BLOĞU — SAYISAL KİLİT LİSTESİ (⑥ FİZİK merceğinin NUMERIC LOCK LIST'i)

> Bu blok doğrudan `6_FIZIK_QA_CRITIQUE_PROMPT.md`'nin lock list alanına
> kopyalanır. Her satır bir tablo satırı olur: PASS / FAIL / UNMEASURABLE /
> NOT EXERCISED.

```
GRAVITY: 0.379 g (3.71 m/s²), constant, whole film
ATMOSPHERE: 610 Pa, 243 K, speed of sound 240 m/s below 240 Hz and
      250 m/s above it, real atmospheric scattering present
LOCKS:
LOCK: every shadow in every scene is soft-edged and its interior is
      filled with scattered light — zero black shadow interiors,
      zero razor-sharp shadow edges, 6/6 scenes
LOCK: the standing woman's shadow is 2.83 m long, identical in S0 and S5
LOCK: sun elevation 30.7°, angular diameter 0.35°, outside frame beyond
      the upper right corner in all six scenes; it drops only 0.24°
      across the whole film, so light level and shadow length are
      constant to within measurement error
LOCK: the pit is an irregular oval 74 m × 61 m; its floor is 46.0 m
      below the surface and is NEVER visible from any camera
LOCK: intact roof thickness 9.0 m; the slab she lies on in S3 is
      0.55 m thick and undercut by 1.9 m
LOCK: far wall is in direct sun from its rim down 44.0 m (74 × tan 30.7°)
LOCK: the ring fracture is 11.6 m across (radius 5.8 m), 6-9 mm wide,
      packed with rust-coloured dust, and its width is IDENTICAL in
      all six scenes — it never opens
LOCK: over any 2.0 m chord the ring deviates by 8.7 cm — it must read
      as STRAIGHT in S0/S1/S3 (0.35 m and 1.55 m cameras) and as a
      CLOSED CURVE in S2/S4 (9.00 m camera)
LOCK: pebble is 62 mm across, 2.2 m back from the edge
LOCK: pebble rocks once through 25° at 38.42 s and settles back — it
      does not roll in S3
LOCK: pebble rolls from 43.22 s to 46.82 s: 0.40 m in 3.60 s at
      0.060 m/s², dead straight, no bounce, no tumble, no direction
      change, then enters the fracture and does not return
LOCK: walking occurs ONLY in S0 (≈5 m) and S5 (≈1.3 m), at 0.62 m/s;
      raised dust = 0 frames
LOCK: her distance to the edge: S0 3.4→1.1 m · S1 1.1 m · S2 1.1→0.9 m ·
      S3 0.7 m · S4 0.7→1.9 m · S5 1.9→7.4 m
LOCK: three further circular hollows at 210 m, 480 m and 790 m, in a
      dead straight line, visible ONLY in S5 and ONLY from standing
      eye height; horizon distance 3.31 km
LOCK: airborne particles of any kind = 0 frames, all six scenes
LOCK: falling objects = 0 frames (the only free motion is the pebble
      ROLLING along the rock)
LOCK: exactly 1 human, 6/6 scenes; indigo accent band on exactly 1 body
LOCK: helmet closed 6/6; flat back 6/6; zero visor reflection 6/6
LOCK: visor state IDENTICAL in all six scenes — changed frames = 0
LOCK: camera movement = 0 in all six scenes; camera pitch A 0°,
      B 0°, C −31.0°; Dutch angle 0.0° in all six
LOCK: on-screen text = 0.0 s
LOCK: clip duration 10.005 s each; total 60.03 s ± 0.5 s
```

---

## E BLOĞU — MAKİNEYLE KOŞULACAK ÜÇ KAPI [D125]

> Bu üç ölçüm modele SORULMAZ. Sayı makineden alınır.

```
① GÖLGE DOLGUSU KAPISI (her sahne) — bu filmin varlık şartı
   Bir gölge içi bölgesi kırpılır ve ortalama parlaklığı ölçülür:
   ffmpeg -i S<n>.mp4 -vf "crop=200:200:<x>:<y>,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
   Kırpma penceresi: kadının gölgesinin gövde kısmı.
   ⛔ YAVG < 18/255  →  gölge içi SİYAH demektir → SAHNE REDDEDİLİR.
      Beklenen bant: 28-55/255 (dolu ama karanlık).
   Bu kapı, bu filmin vakum filmlerinden ayrıldığı tek fiziksel
   noktayı ölçer ve elle "bence dolu" demek geçerli değildir.

② KAMERA SABİTLİK KAPISI (her sahne) — 6/6 lockoff kilidi
   ⛔ DOĞRULANDI: HAYIR — 28.08.2026'da koşulmak istendi, ffmpeg 8.1
      yapısında `vidstabdetect` YOK (libvidstab derlenmemiş). Kapı sessizce
      hiçbir .trf üretmedi ve hata bile vermedi. [Ders 142]
   İKAME (koşulan ve işe yarayan): sahnenin +0,5 s ve +9,3 s karelerinin
      satır/sütun luma profilleri ±25 px çapraz korelasyonla eşlenir;
      kayma ≤ 2 px → kamera kilitli. Özne üst bandı dolduran sahnelerde
      ölçüm yapılamaz ve "⬜ ÖLÇÜLEMEDİ" yazılır (boş bırakılmaz).
   ffmpeg -i S<n>.mp4 -vf vidstabdetect=shakiness=1:accuracy=15:result=stab_S<n>.trf -f null -
   stab_S<n>.trf içindeki kare başına ortalama yer değiştirme okunur.
   ⛔ Ortalama > 1,0 piksel  →  kamera hareket ediyor → SAHNE REDDEDİLİR.
   (Kadrajda hareket eden özne varken bile küresel dönüşüm sıfıra
   yakın kalmalıdır; ölçüm özneyi değil KADRAJI okur.)

③ KURGU KAPISI (tam teslim) [D124 · D125]
   ffprobe -v error -show_entries format=duration -of csv=p=0 teslim.mp4
   süre = klip_sayısı × ölçülen_klip_süresi ± 0,5 s
   Kesme ızgarası: (n − 1) × klip_süresi  [D115]
   Ekran metni: 0,0 s — başlık kartı dahil
   ⭐ Ayrıca ÜÇ BİRİM ayrı sayılır [D101]: SCENE 6 · SHOT 6 · CLIP 6
```

```
⛔ DÖRDÜNCÜ KAPI MAKİNEYLE KOŞULAMAZ — ve bu dürüst kayıttır:
   HALKA KAPISI (S2 · 22,41 s). Kaldırımdaki tek eğri çatlağın kapalı
   bir halka olarak okunup okunmadığı bir KAVİS yargısıdır; ne
   prompt_kontrol.py ne ffmpeg bunu ölçer. İnsan gözüyle koşulur ve
   ÜRETİM SIRASININ BAŞINDADIR: S2 ilk üretilir, halka kapanmıyorsa
   diğer beş sahne üretilmez.
```
