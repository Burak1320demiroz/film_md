# 📋 THE SKYLIGHT — QA SPEC (rubriklere yapıştırılacak tek dosya)

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

⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ şu üç kilidi: oda ölçüleri /
                   ışık takvimi · ekran yönü · sabit çevre nesneleri
                   (cairn'ler + jalonlar) [Ders 133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri (g · süre · mesafe ·
                   sütun takvimi)
⛔ ⑤ ve ⑥'ya kimlik, kostüm ve olay kilitleri VERİLMEZ — o körlük
   tasarımdır.
⛔ ② ve ③'e belge vermek yasaktır — eksikliği değil, TASARIMI bozar.
   FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⛔ Her mercek AYRI ve TEMİZ sohbette [D110].
⛔ Dördüne de AYNI video dosyası verilir [D75].
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:                 THE SKYLIGHT
FORMAT:               3-5dk
RUNTIME:              329 seconds (title card: none — screen text lock 0.0 s)
                      ⚠️ format deviation on record: 25-scene core (4:09)
                      + 8-scene PART C departure (28.08.2026)
SCENE COUNT:          33  (S0-S32)
REVIEW INPUT:         video only

LOGLINE (intended):   A lone surveyor walks down into a colossal Martian
                      lava-tube chamber through its collapsed skylight,
                      finds that the column of daylight falling from the
                      opening is the chamber's only clock, finishes her
                      last survey station in the dark as the light dies,
                      leaves her own light burning on the first cairn as
                      she climbs out into the night — and at the next dawn
                      walks to her ascent ship and lifts off, seeing the
                      volcano line and the planet's thin blue limb from
                      orbit, the night side below without a single light.
THEME (intended):     Time / transience — the meeting of two clocks: the
                      planet's billion-year room and one human day.
                      Sentence: "Daylight leaves every room; the light
                      that stays is the light someone left."
                      (⛔ NOT the trade pattern [TEMA §3c] — nothing is
                      sacrificed FOR anything; a mark is left.)
THEME SCENES:         S1 (flow layers) · S7/S12/S16/S20 (cairns —
                      accumulation) · S10/S13/S19 (column — cycle) ·
                      S14 (compass — Earth's clock useless here) ·
                      S24 (the light that stays)
INTENDED EMOTION:     awe and settled calm, not fear — the viewer arrives
                      asking "what is at the bottom of that hole?", stays
                      asking "will she finish before the light goes?",
                      leaves answering "why did she leave the light?"
ENDING TYPE:          DOUBLE CLOSE — S24 closes the CHAMBER (S0 mirror:
                      the light's owner changes, sky → human); S32 closes
                      the FILM (S0 scale mirror: the pit seen from one
                      metre ↔ the planet seen from orbit). Her fate is
                      CLEAR (she departs); the open question is how long
                      the left light burns — unseen from orbit by design.

PROTAGONIST:          surveyor, female, 39, unnamed in prompts.
                      Wants: to finish mapping the chamber's station line.
                      Fears: nothing dramatic — her care is that the work
                      be COMPLETE and marked before the day ends.
ANTAGONIST/FORCE:     no villain, no threat — only the sun's schedule
                      made visible by the room's size. Nothing attacks;
                      the light simply leaves.
CENTRAL CHOICE:       S20 — staying to place the final stones as the last
                      daylight dies INSIDE the shot; she finishes in the
                      dark, calmly, then lights her lamp.

DIALOGUE LINES:       0 — the film is fully silent (human 0 · machine 0)
SILENT SCENES:        33
MUSIC (post, 28.08):  2 cues — CUE A 48 BPM S3-S19 (0:29-3:14) · CUE B
                      120 BPM S25-S30 (4:09-5:09) + S32 coda (5:19-5:29).
                      NO MUSIC: 0:00-0:29 · 3:14-4:09 · 5:09-5:19 — beds
                      continuous, no digital zero [D136]. Only resolution
                      S32. Source: THE_SKYLIGHT_MUZIK.md
VIRAL INTERSTITIALS:  S3 · S13 · S19 · S20 · S28 · S30   ⛔ MAY NOT BE CUT
COVER/THUMBNAIL:      S30 (owner decision 28.08) — over-the-shoulder
                      window view: the Tharsis shield line, the thin
                      blue-white limb, only her helmet and shoulder in
                      frame. Promise: "one person, and a whole planet."
                      ⚠️ Cover moment lies OUTSIDE the 0:00-0:10 band
                      (PAKETLEME §1 deviation on record in PLAN + KAPAK).
                      Plan B cover = S0, the pit mouth with sunlight
                      pooled at its floor, tiny human at the rim.
TITLE:                THE SKYLIGHT — the real NASA term for a collapsed
                      lava-tube opening; the film's clock, door and
                      final image are all this one hole.
LIBRARY CONTEXT:      3-5 dk shelf siblings: LOW POWER (Mars, dust storm,
                      resource countdown) · LOSS OF LIFT · THE BORROWED
                      WEIGHT · THE COLD BURN. This film differs: first
                      underground/natural-interior film in the library;
                      no countdown, no resource crisis, no threat — the
                      only pressure is the visible rotation of daylight;
                      scale novum proven by tool failure (lamp that
                      cannot reach a wall), not by any physics violation.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      33          (sahne = çekim = klip; üçü eşit)
SHOT COUNT:      33 · 0 sahne içi kesme
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok; gerekçe: 33×10 s
                 tek-çekim disiplini, tek kurgu müdahalesi S0 kırpması)
                 [D74 gerekçe satırı]
GRID:            sahne başlangıcı(n) = 9 s + (n−1) × 10 s
RUNTIME:         329 s   (Hook 9 s + 32 × 10 s) — 5:29, format sapması kayıtlı
RAW FOOTAGE:     330 s · TRIM BUDGET: 1 s (yalnız S0 10→9)
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı YOK
CAMERA:          33/33 sabit lockoff (S28: kamera yerde sabit, gemi kadrajı terk eder) · klip içi pan/tilt/zoom/dolly 0
SETUP SEQUENCE:  7 kurulum, plandan [ACI_YAYI §4 — promptlarda lens ·
                 yükseklik · mesafe okunur biçimde yazılı]:
                 A 24mm kenar-üstü (S0·S24) · B 40mm göğüs/4m
                 (S1·S12·S14·S22) · C 32mm bel/7m profil (S6·S18·S21) ·
                 D 35mm omuz/1.5m OTS (S2·S9·S17·S23) · E 50mm göz/1.2m
                 (S8) · F 28-32mm diz/3-6m iş (S4·S7·S11·S15·S16;
                 S20 = F-alt açı 24mm zemin+30cm) · G 24mm iç geniş
                 30-60m (S3·S5·S10·S13·S19) · PART C: H yüzey geniş
                 28-32mm bel/40-80m (S25·S28) · I kabin 35mm göğüs/1.5m
                 (S27·S29·S31) · J pencere POV 32mm kask hizası (S30·S32)
ANGLE ARC:       açı TİPİ ≥4: üst bakış (A) · göz/omuz hizası (B-E) ·
                 alçak (F/G) · alçak-yukarı (S3·S20) [KAMERA_ACISI §2 ✅]
EŞ KADRAJ (bilinçli afinite — tek değişken kuralı):
                 S0↔S24 (gündüz↔gece · ışığın sahibi) ·
                 S2↔S23 (iniş↔çıkış OTS) · S6↔S18 (sütun dik↔yatık ·
                 yön sağ↔sol · 9↔5 adım)
REPLİK ZAMANLARI: — (replik 0; hizalama kapısı ⑨ sessiz filmde ızgara
                 dilim birleşimiyle koşulur [D115])
DORUK:           S20 → 3:19-3:29 (sahne başlangıcı 199 s — formülden
                 [D122]; ışığın sönüşü klip içi ~4.5 s → ≈ 3:23-3:24)
AKSİYON ZİRVESİ: S28 kalkış → 4:39-4:49 (başlangıç 279 s); yerden
                 kesilme klip içi T+2 → ≈ 4:41; kadraj-terk ≈ 4:47
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1111111111111111111111111111-1111
       33 karakter — 32 İNSANLI, tek insansız: S28 (dış kalkış; insan
       gemide, kadrajda değil). S13 · S19 · S24 · S25 geniş sahnelerinde
       figür KÜÇÜK ama VARDIR; S30 · S32'de yalnız kask+omuz — yine 1.
       "figür yok" bulgusu bu sahnelerde envanter hatasıdır.
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         tam 1 · 25/25 sahnede görünür · insansız 0 · araç 0 ·
              biniş/iniş 0 kare · eşik geçişi 0 kare (S2 dışarıda
              biter, S3 içeride başlar — kesme tasarımı)
KASK          25/25 KAPALI · kasksız 0 · ara durum 0 · giyme/çıkarma
              0 kare · vizör optik berrak, renksiz, YANSIMASIZ — yüz
              okunur; sırt ünitesi YOK, sırt silueti DÜZ [D79]
YERÇEKİMİ     0.38 g — yürüyüş NORMAL tempoda, süzülme 0, zıplama 0,
              AĞIR ÇEKİM 0 [D44]; düşük g yalnız düşen toz/taş yayında
ATMOSFER      ~6 mbar: ses boğuk ve kısa, yankı yok denecek kadar az ·
              gölgeler zayıf/yumuşak (MEŞRU [D41]) · toz 3-4 saniyede
              TAM çöker · iç mekânda rüzgâr 0 — hiçbir şey kıpırdamaz
ODA           çap 180 m · tavan 60 m · gök deliği 40 m · rampa ~30°
              çökme konisi, yürünerek inilir
IŞIK SÜTUNU   S3-S9 DİK → S10 ilk eğim → S13 30° eğik (elips duvar
              dibinde) → S19 incecik/KOPUK → S20 klip İÇİNDE söner
              (~4.5 s'de iki saniyelik düz sönüş) — MONOTONİK, geri
              dönmez; klip İÇİNDE açı değişimi/ışık süpürmesi YOKTUR
              (değişim yalnız sahneler arası). Sütun bulgusu FİLMİN
              ÖNERMESİDİR, ışık hatası değil [D87/D116 önerme kapısı].
FENER         amber, tek huzme, menzil 25 m — duvar 90 m: ışın duvara
              HİÇBİR sahnede ulaşmaz (S5 bunun kanıt sahnesidir —
              "fener duvarı aydınlatamıyor" bulgusu TASARIMDIR)
KARANLIK      fener/sütun dışı GERÇEK SİYAH — pozlama tasarımı, ekran
              hatası değil; "detay kaybı" bulgusu sütun-dışı siyahta
              düşer
YEDEK HÜCRE   S9'dan itibaren kemerde GÖRÜNÜR (Çehov) · S22'de cairn
              #1 üstüne yerleştirilir ve SABİT yanar — nabız YOK,
              yanıp sönme YOK; S23-S24'te aynı sabit nokta
TAŞ (S15)     1.2 m'den düşüş 0.8 s — tek kesintisiz hızlanan yay;
              havada duraksama = hata; yavaşlık ağır çekim DEĞİL
CAIRN SAYACI  monotonik 1→2→3→4: S7 (7 taş + jalon #1) → S12 (5 taş)
              → S16 (9 taş) → S20 (8 taş + jalon #2) · S21'de #3 ve
              #2 fener konisinde YENİDEN görünür · S22'de #1 üstüne
              hücre konur — taş sayıları sahneler arası DEĞİŞMEZ
PUSULA (S14)  pirinç, gül RAKAMSIZ/HARFSİZ (yalnız çizgi işaretleri);
              iğne 8-10 s'de bir tam salınım, HİÇ DURMAZ — "pusula
              bozuk" bulgusu değil, Mars gerçeği (önermede yazılı)
EKRAN YÖNÜ    derinleşme SOLDAN SAĞA · dönüş sağdan sola · sütun +
              koni + çıkış her iç sahnede SOLDA/sol geride — 25/25
              sabit, tersine dönmez
SUIT YIPRANMA tam 3 sabit bölge: sağ diz ağarmış yama · sol bilek
              koyu kayış izi · göğüs altı soluk sıyrık [D42] — her
              karede aynı yerde
İZLER         milyarlık tozda yalnız KENDİ izleri; izler asla
              silinmez; S21'de eski+yeni izler kesişir (tasarım)
IŞIK TAKVİMİ  S0-S2 yüzey öğle (kızıl) → S3-S9 iç/sütun dik → S10-S12
              ilk eğim → S13-S16 eğik+fener → S17-S19 ölüm → S20
              sönüş → S21-S22 fener gecesi → S23-S24 yüzey gece —
              MONOTONİK; kızıl YALNIZ yüzey sahnelerinde
SES REGISTER  HUMAN 0 · MACHINE 0 — filmde hiçbir konuşma yoktur;
              duyulan her şey nefes/kumaş/zemin iletimi/taş; müzik
              promptlarda 0 (post) · "eksik diyalog" bulgusu yazılamaz
─── PART C KİLİTLERİ (S25-S32) ───
GEMİ          16 m tek gövde · 3 iniş bacağı · 3 motor çanı · mat grafit
              + TEK amber şerit · yazı/bayrak/logo 0 · kokpit: düz
              yatay pencere bandı (kubbe yok) · gemi S25'ten önce 0 kare
BİNİŞ         0 kare — S26 dışarıda biter, S27 içeride kemerli başlar
              [D69/D77]; kapak/merdiven teması 0
KALKIŞ (S28)  ateşleme T+1 · yerden kesilme T+2 · kadrajı üstten terk
              8. saniye [D127] · kamera YERDE sabit · gemi sürekli
              ivmelenir, havada duraksamaz
ALEV          metalox: neredeyse şeffaf MAVİ-MOR · ince atmosferde koni
              GENİŞ açılır · kıvrılma 0 · duman bulutu 0 · ateş topu 0
TOZ BLAST     düz balistik yaylar · ≤2 s'de yerde · mantar bulutu 0 ·
              kabaran duman 0 — "billowing" bulgusu tasarım ihlalidir
VENTING       kriyojenik buhar iki alt vent'ten · ≤1 s'de dağılır
İVME          S29: gövde koltuğa çökük + kemer GERGİN [§3.5 kanıtı];
              titreşim ince, şiddetli sarsıntı 0
0g (S31)      kemer GEVŞEK · kayış ucu yüzer · 2 toz zerresi süzülür ·
              İNSAN KEMERLİ ve koltukta — süzülme 0 [D23 nesneyle]
GÖK GEÇİŞİ    S29 klip içi tek kademe kahve→menekşe · siyah gök S30'dan
MANZARA       Arsia kalkanı + dizide 2 kardeş volkan (gerçek Tharsis
              hattı) · ince mavi-beyaz limb çizgisi · gece tarafında
              yapay ışık 0 — "şehir ışığı yok" tasarımdır
PENCERE       optik berrak · iç yansıma 0 · yüz camda yansımaz
PANELLER      koyu/okunmaz her karede · ekran metni 0.0 s
KASK          33/33 kapalı (kabinde de) · güneş diski 0 kare (tüm film)
İNSANSIZ      yalnız S28 (kısa negatif + boş kadraj varlık tarifi)
```
