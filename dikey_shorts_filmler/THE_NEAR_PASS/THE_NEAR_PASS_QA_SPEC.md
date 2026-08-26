# 📋 THE NEAR PASS — QA SPEC (MOD D girdisi)

> **Ne işe yarar:** QA koşusunda operatörün elinde İKİ dosya olur — rubrik +
> bu dosya. Bu dosya verilmezse koşu MOD V'dir ve **ön koşu** sayılır [D94/D117]:
> skor satırı Ⓥ ⚠️ ŞARTLI girer, 00_INDEX tamlık matrisinde hücre ❌ kalır,
> kesme listeleri ve REMOVE reçeteleri uygulanmaz.
>
> ⚠️ **Film HENÜZ ÜRETİLMEDİ (25.08.2026).** Bu SPEC ilk üretim koşusu için
> yazıldı ve THE IRON SLOPE'un hatasını tekrarlamamak için filmle AYNI GÜN
> depoya indi [D117 · SPEC'in bulunamaması altı mercek mod V koşturmuştu].
>
> Film dosyası: `THE_NEAR_PASS_DIKEY_SHORTS.md` (aynı klasör)

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## A BLOĞU — SAHNE SPESİFİKASYONU (① KARE · ⑥ FİZİK rubriklerine)

```
FILM: THE NEAR PASS
FORMAT: dikey shorts (9:16)
SCENE: <sahne numarası> ya da "Compilation" (tam kurgu)
CLIP LENGTH: 10,005 s (plan ızgarası ÖLÇÜLMÜŞ klip süresinden kuruldu [D124];
             koşuda ffprobe ile ölçülen gerçek süre yazılır)
PIPELINE: text-to-video (her sahnenin ayrıca I2V DEVAM sürümü var)

CHARACTER: 34 yaşında kadın, gezegen fotometristi · 1,70 m ·
           sıcak zeytin ten, gözenek dokusu görünür, burun ve elmacıkta
           hafif çil, koyu kahve gözler, kalın koyu kaşlar, SAĞ kaşta
           küçük soluk yara izi, çatlak alt dudak, arkaya toplanmış koyu
           saç, sağ şakakta iki kaçak tel
SUIT: mat kurşun grisi yumuşak kabuk yüzey suit'i · dış kollarda ve kalça
      hattında **tozlu turkuaz** aksan dikişler (kadrandaki TEK soğuk
      doygun renk, TAM 1 kişide) · **sırt TAMAMEN DÜZ** (sırt ünitesi/
      tank/hortum/kablo YOK) [D79] · kask **tek parça berrak baloncuk**,
      tint YOK, ayna kaplama YOK, çevre yansıması YOK · kask halkasının
      SOL yanında küçük lamba yuvası · diz, SOL ön kol ve İKİ bot burnu
      okra tozuyla aşınmış (her sahnede AYNI yerde) · **hiçbir arma,
      bayrak, yazı, rakam, sembol yok** · eldivenler gri ve **6/6 BOŞ**
CHARACTER HEIGHT: 1,70 m

GRAVITY: 0,62 g (6,08 m/s²) — sabit, filmin tamamında
ATMOSPHERE: ince CO₂-N₂, yüzeyde 9 kPa, 210 K · ses hızı 226 m/s ·
            SAÇILMA YOK: pus yok, hüzme yok, gölge içi dolgu yok
            → dışarıda pratikte ses yoktur; duyulan her şey kask içidir
            (nefes, fan) ya da müziktir
LOCOMOTION MODE: DÜZ YÜRÜYÜŞ, yalnız S2'de, 1,1 m/s, TOPLAM 8 metre.
            Botlar kalkar-basar-yük alır; kayma/süzülme 0 kare.
            Koşu 0 kare. Kalkan toz 0 kare (0,62 g'de ve durgun
            havada ince toz ayak altında kalkmaz — TASARIM)
            ⛔ Diğer beş sahnede kadın DURUYOR; "hareketsizlik" bulgu
            değildir

LENS: 24 mm KÜRESEL → S1 · S2 · S3 · S4 · S5  |  75 mm KÜRESEL → S0
      (anamorfik YASAK — ince atmosferde saçılma yok, parlama artefakttır)
      ⛔ 32 mm kullanılmadı ve bu bilinçli sapmadır: gerekçe film
      dosyasının §GÜVENLİ ALAN HARİTASI'nda hesabıyla yazılı
CAMERA DISTANCE: S0 45 m · S1 20 m · S2 30→22 m · S3 24 m · S4 22 m ·
      S5 24 m (hepsi promptta metre olarak)
CAMERA HEIGHT: A kurulumu 0,90 m · B kurulumu 0,25 m · C kurulumu 0,90 m
CAMERA MOVE: **6/6 TAM LOCKOFF** — üç kurulum da yere oturur.
      Pan/tilt/dolly/zoom/sarsıntı/hız rampası 0 kare
      ⛔ Bu satır KLİP İÇİ karardır ve sahneler ARASI kurulumu anlatmaz;
      onu SETUP SEQUENCE satırı anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE: A · B · C · D · C · D          (26.08.2026'da eklendi)
      A = 75 mm · 0,90 m · 45 m   → S0
      B = 24 mm · 0,90 m · 20 m   → S1
      C = 24 mm · 0,25 m · 22 m   → S2 · S4
      D = 24 mm · 0,90 m · 24 m   → S3 · S5
      kurulum sayısı 4 · 6 sahne → ACI_YAYI §4 bandı (≥3) ✅
      ardışık ikili hiçbir yerde aynı değil → §3 ✅
      ⚠️ Yukarıdaki "A/B/C kurulumu" adlandırması YÜKSEKLİĞE göredir
      (0,90 · 0,25 · 0,90); bu satır lens+yükseklik+mesafe üçlüsüne göre
      sayar ve dördü ayırır. İki sayım çelişmiyor, farklı şey ölçüyor.
ANGLE ARC: **1 açı tipi — 6/6 sahnede ALT AÇI** [KAMERA_ACISI §2]
      🚨 AÇIK MADDE (26.08.2026): §2 en az 3 açı tipi ister; bu film 1
      taşıyor. Kurulum bandı tutuyor ama üç kurulum da yerden bakıyor —
      değişen tek şey mesafe. Film HENÜZ ÜRETİLMEDİ, yani bu düzeltilebilir:
      ya S2/S4'ün biri tepe/kuşbakışına çevrilir (dikeyde EWS'in karşılığı
      §6), ya doruk sahnesi göz hizasına alınır. Karar verilene kadar
      `prompt_kontrol.py` bu dosyaya FIX verir.
LIGHT SOURCES: (a) TEK yıldız — 0,55° çapında, batıda 29,7° yükseklikte,
      60 saniyede kımıldamaz · (b) tutulmada: gezegen ışığı (uydunun
      alt yüzünde, kenarda parlak ortada koyu, gündüzün ~%4'ü) ·
      (c) tutulmada: ufuk çevresindeki ince bronz kuşak ·
      (d) 38,6-43,0 s arasında kask lambası. Başka kaynak YOK
FILL LIGHT ALLOWED: hayır — gölgeler MUTLAK siyah, dolgu 0
VEHICLE/STRUCTURE: **YOK.** Kadrajda insan yapımı tek nesne yoktur
      (kadının suit'i hariç). Araç, bina, alet, anten, iz 0 kare
DIALOGUE EXPECTED: **YOK — film tamamen repliksizdir** (tasarım, eksik değil)
AUDIO LAYERS (≤3): ① nefes + kask fanı (60 saniyenin 60'ında, hiç kesilmez)
      ② müzik yatağı (96 BPM, 36,1-56,4 arasında tek sub-bass notasına iner)
      ③ dış ses: YOK — ve bu tasarımdır
```

---

## B BLOĞU — KURGU VE ŞERİT (④ HİKAYE · kurgu kapısı ④)

```
THEME (intended): TANIKLIK  ⏸️ (TEMA_MUHENDISLIGI §3b · depoda doğmuş aday
      etiket, §3 tablosunda yok — pazar/kuşak verisi ÖLÇÜLMEDİ)
      Tek cümle: "Bu film, bir şeyi görebilmek için başka bir şeyi
      görmekten vazgeçmek hakkında." — cümlede novum kelimesi yok ✅
      ⚠️ Bu cümle TAKAS kalıbıdır (§3c): "X için Y'den vazgeç".
      Kalıp arka arkaya en çok 2 filmde kullanılır.
THEME SCENES (§5 matrisi): S0 · S1 · S2 · S4 · S5
      başın arkaya yatışı (S0 · S1 · S5) · eldivenin alna kalkışı
      (S0 · S5) · bot burnunun kabuğu tıklatması (S2) ·
      payoff: çatlak ağı S4'te açılır, S5'te geri alınır
SCENE / SHOT / CLIP COUNT: 6 / 6 / 6
RAW FOOTAGE: 6 klip × 10,005 s = 60,03 s
RUNTIME: 60,03 s ± 0,5 s
TRIM BUDGET: 0,0 s — kırpma yoktur; ızgara zaten aracın klip süresine
      yazıldı [D124]. Araç başka bir süre veriyorsa kırpma PLANDA sahne
      sahne yazılır, yoksa kurgu kırpmaz [D100]
TARGET ASL BAND: 10,0 s — sabit ızgara, eğri yok (bilinçli sapma [D74])
İNSAN ŞERİDİ [D118]: 111111
EKRAN METNİ: 0,0 saniye — başlık kartı DAHİL [D61a/D70]
KESİLEMEZ SAHNELER: S0 (kanca + tohum) · S3 (anahtar/kapanma) ·
      S4 (merkezi seçim + bakır ödül) · S5 (geri açılma + döngü)
DOĞAL DORUK: S5 · 56,4-57,3 — gündüzün 0,94 saniyede geri gelmesi
TOHUM → KARŞILIK: S0 06,2-07,0 (PALL'ın ön kenarındaki SOLUK çatlak ağı,
      0,8 s, tepkisiz) → S4 46,0-49,0 (aynı ağ, bakır yalayan ışıkta
      derin gölgeli yarıklara AÇILIR) → S5 57,6 (gündüz döner, ağ soluk
      lekeye geri iner)
DÖNGÜ NOKTASI: 60,0 → 0,0 — jest eşleşmesi (S5 sonu: sağ eldiven alna
      ÇIKAR · S0 başı: sağ eldiven alından İNER)
```

---

## C BLOĞU — KİLİTLER VE SIK YAPILAN YANLIŞ OKUMALAR (⑩ önerme kapısı)

```
✅ TASARIM — bulgu DEĞİLDİR:
   · Uydunun KÜRE OLMAMASI, yamuk ve uzun olması → 52 km'lik bir cisim
     kendi çekimiyle yuvarlaklaşamaz; Roche sınırının içinde ve kaya
     dayanımıyla ayakta. Oluklar ve çatlak ağı bunun imzasıdır
   · Uydunun ÇOK BÜYÜK görünmesi (6,1°→12,5°) → 150 km irtifada 52 km'lik
     bir cisim bu kadar görünür. Ölçek hatası değil, filmin novum'u
   · Uydunun her sahnede TIRMANMASI ve BÜYÜMESİ → yörünge hareketi;
     hareketsiz çıkması İHLALDİR, hareket etmesi tasarımdır
   · Gündüzün 1,2 saniyede kapanması ve 0,94 saniyede açılması →
     hesaplanmış tutulma süreleri. Asimetri gerçektir (uydu uzaklaşıyor)
   · Kapanmada HİÇBİR ŞEYİN SÜPÜRMEMESİ → gölge saniyede 5,4 km gidiyor;
     ekranda hareketli bir kenar OLAMAZ. "Gölge geçişi görünmüyor"
     bulgusu YANLIŞTIR
   · Kapanmada SESİN HİÇ DEĞİŞMEMESİ → gölge Mach 23,7 ile geliyor;
     önünde hiçbir şey gelemez. "Ses tasarımı eksik" bulgusu YANLIŞTIR
   · Tutulmada TAÇ / ELMAS YÜZÜK OLMAMASI → uydu yıldızdan 18 kat geniş;
     taç tamamen örtülür. Halka çıkarsa İHLALDİR
   · Tutulmada YILDIZ ALANI OLMAMASI → 19 saniyede göz karanlığa uyum
     sağlamaz ve ufuk bronz parlıyor. "Gökyüzü boş" bulgusu YANLIŞTIR
   · Uydunun alt yüzünün KENARDA PARLAK, ORTADA KOYU olması → ışık
     yalnız gölge bandının dışındaki gündüzden, yalayarak geliyor.
     Ters aydınlatma hatası DEĞİL
   · Lamba hüzmesinin HAVADA GÖRÜNMEMESİ → 9 kPa'da saçılacak hava yok.
     Hüzme çıkarsa İHLALDİR
   · Kadının BEŞ SAHNEDE HAREKETSİZ olması → tasarım; film bir tanıklık
     filmidir, aksiyon değil
   · Repliksizlik → ilan edilmiş kısıt [D113], düşük puan sebebi değil
   · Nefes ve fan sesi → kask içi; ince atmosfer ihlali değil

🔴 GERÇEK İHLAL — bulgu SAYILIR:
   · Uydunun bir çekim boyunca YERİNDE DURMASI ya da 10 saniyede alt
     kenarının 100 pikselden az yükselmesi  ← FİLMİN 1 NUMARALI KAPISI
   · Uydunun takla atması, dönmesi, yana kayması, salınması
   · Uydunun kusursuz küre, pürüzsüz, parlayan ya da saydam çıkması
   · Tutulmanın BULUT GÖLGESİ gibi üretilmesi: yumuşak kenar, kadrajı
     süpüren bir karartma, vinyet, renk kayması, gölgelerin kısalması
   · Tutulmada taç, halka, elmas yüzük, parlama
   · Lambanın havada hüzme yapması, sönerken solması/titremesi
   · Toz bulutu, duman, kıvılcım, enkaz, düşen cisim, meteor, kuyruk
   · Halka sistemi, ikinci uydu, yıldız alanı, aurora, bulut, pus
   · Ekranda herhangi bir yazı/rakam/logo/arma (başlık kartı dahil)
   · Kamera hareketi (6/6 lockoff kilidi)
   · İkinci insan, yansımada insan, klon, ikinci turkuaz aksan
   · Sırt ünitesi/tank/hortum, vizör tinti, ayna kaplama
   · S5'te kadının botlarının çizgiden AYRILMIŞ olması (bedel silinir)
```

---

## D BLOĞU — SAYISAL KİLİT LİSTESİ (⑥ FİZİK merceğinin NUMERIC LOCK LIST'i)

> Bu blok doğrudan `6_FIZIK_QA_CRITIQUE_PROMPT.md`'nin lock list alanına
> kopyalanır. Her satır bir tablo satırı olur: PASS / FAIL / UNMEASURABLE /
> NOT EXERCISED.

```
GRAVITY: 0.62 g (6.08 m/s²), constant, whole film
ATMOSPHERE: 9 kPa, 210 K, speed of sound 226 m/s, zero scattering
LOCKS:
LOCK: satellite is a rigid single-piece lopsided rock, 60 × 50 × 44 km,
      150 km overhead; it is NOT a sphere and NOT smooth
LOCK: satellite apparent width grows 6.12° → 12.48° across the film
      (S0 6.12→6.73 · S1 6.73→7.45 · S2 7.45→8.34 · S3 8.34→9.43 ·
       S4 9.43→10.79 · S5 10.79→12.48)
LOCK: satellite elevation climbs 14.84° → 37.87° across the film
      (S0 14.84→17.00 · S1 17.00→19.57 · S2 19.57→22.68 ·
       S3 22.68→26.54 · S4 26.54→31.45 · S5 31.45→37.87)
LOCK: in EVERY shot the satellite travels between 34% and 55% of its own
      apparent width, and the fraction increases monotonically
LOCK: S0 (75mm) — upper edge leaves the top of frame by second 5;
      lower edge rises ≥100 px (design 132 px) between second 0 and second 10
LOCK: satellite path is a dead straight climb — tumble/rotation/lateral
      drift/oscillation = 0 frames
LOCK: star angular width 0.55°, fixed at 29.7° elevation, moves ≤5 px in 60 s
LOCK: gap between satellite leading edge and star (24mm frames):
      S1 236→159 px · S2 159→67 px · S3 67→0 px · contact at 36.09 s
LOCK: daylight ends at 36.09 s and is fully out by 37.30 s → 1.21 s
LOCK: totality 37.30 → 56.37 s = 19.07 s
LOCK: daylight returns 56.37 → 57.31 s → 0.94 s (slower than the close —
      this asymmetry is required, not a defect)
LOCK: both transitions are LEVEL changes — moving shadow edge, sweep,
      vignette, colour shift, shadow shortening = 0 frames
LOCK: no corona, no ring of light, no diamond ring at any point
LOCK: shadow length of the standing woman = 2.98 m, identical in S0 and S5
LOCK: helmet lamp ON 38.60 s, OFF 43.00 s (single frame, no dim, no flicker);
      lit disc on the crust ≈ 2 m across; visible beam in the air = 0 frames
LOCK: satellite in totality is rim-bright and centre-dark, copper-bronze,
      ≈4% of daylight; the plain does NOT brighten
LOCK: walking occurs ONLY in S2, 1.1 m/s, 8 m total; raised dust = 0 frames
LOCK: fracture 4 m wide, 30 m deep; boot toes on its lip from 26.6 s to
      the end of the film
LOCK: exactly 1 human, 6/6 scenes; teal accent seams on exactly 1 body
LOCK: helmet closed 6/6; flat back 6/6; zero visor reflection 6/6
LOCK: camera movement = 0 in all six scenes
LOCK: on-screen text = 0.0 s
```

---

## E BLOĞU — MAKİNEYLE KOŞULACAK ÜÇ KAPI [D125]

> Bu üç ölçüm modele SORULMAZ. Sayı makineden alınır.

```
① TIRMANIŞ KAPISI (S0) — filmin varlık şartı
   ffmpeg -i S0.mp4 -vf "select='eq(n\,0)+eq(n\,239)'" -vsync 0 k_%02d.png
   İki karede uydunun ALT KENARININ piksel farkı ölçülür.
   ⛔ < 100 px  →  ÜRETİM DURUR, film üretilmez [D127 kabul kriteri]
   Ayrıca: 6. saniyeye kadar üst kenar kadrajı terk etmiş olmalı.

② ANAHTAR KAPISI (S3) — 6,1-7,3 s
   ffmpeg -i S3.mp4 -vf "crop=1080:200:0:1250,signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null -
   Düzlük şeridinin ortalama parlaklığı 2,0 saniye içinde ≥ %85 düşmeli.
   ⛔ Düşüş 3 saniyeden uzunsa, ya da kadrajda süpüren bir kenar/vinyet
      varsa sahne REDDEDİLİR.

③ KURGU KAPISI (tam teslim) [D124]
   ffprobe -v error -show_entries format=duration -of csv=p=0 teslim.mp4
   süre = klip_sayısı × ölçülen_klip_süresi ± 0,5 s
   Kesme ızgarası: (n − 1) × klip_süresi  [D115]
   Ekran metni: 0,0 s — başlık kartı dahil
```
