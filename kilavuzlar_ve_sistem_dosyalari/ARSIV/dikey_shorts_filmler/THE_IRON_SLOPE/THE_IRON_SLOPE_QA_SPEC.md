# 📋 THE IRON SLOPE — QA SPEC (MOD D girdisi)

> **Ne işe yarar:** QA koşusunda operatörün elinde İKİ dosya olur — rubrik +
> bu dosya. Bu dosya verilmezse koşu MOD V'dir ve **ön koşu** sayılır [D94/D117]:
> skor satırı Ⓥ ⚠️ ŞARTLI girer, 00_INDEX tamlık matrisinde hücre ❌ kalır,
> kesme listeleri ve REMOVE reçeteleri uygulanmaz.
>
> ⚠️ **25.08.2026 · YENİDEN YAZILDI.** İlk sürüm 24.08'de yazılmıştı ve depoda
> bulunamadı; filmin altı mercekli QA'sı bu yüzden altı kez mod V koştu. Bu
> sürüme, ilk sürümde olmayan **D BLOĞU — SAYISAL KİLİT LİSTESİ** eklendi
> (⑥ FİZİK merceğinin mod D girdisi).
>
> ⛔ **FİLM ÜRETİLDİ VE ÖLÇÜLDÜ (25.08.2026).** Teslim kurgusu bu SPEC'e
> UYMUYOR: 65,0 s / 6 × 10,0 s klip / 4,97 s başlık kartı, ve serbest parça
> hızlanmıyor. Bu SPEC **yeniden üretim** ve sonraki mod D koşusu içindir.
> Ölçüm: `../kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_IRON_SLOPE.md`

> ⛔ **BU DOSYA RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa
> koşu ön koşu değil, **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T
> tablosuna satır yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> SPEC'i olan bir filmde `INPUT MODE: D` yazmayan rapor TEKRARLANIR.

---

## A BLOĞU — SAHNE SPESİFİKASYONU (① KARE · ⑥ FİZİK rubriklerine)

```
FILM: THE IRON SLOPE
FORMAT: dikey shorts (9:16)
SCENE: <sahne numarası> ya da "Compilation" (tam kurgu)
CLIP LENGTH: 8 s hedef — ⚠️ üretim aracı 10,005 s veriyor [D124]; koşuda
             ölçülen süre yazılır
PIPELINE: text-to-video (her sahnenin ayrıca I2V DEVAM sürümü var)

CHARACTER: 34 yaşında erkek, dış gövde teknisyeni · 1,78 m, ince yapılı ·
           açık kahve ten, gözenek dokusu görünür, koyu gözler, kalın koyu
           kaşlar, iki günlük sakal, SOL çenede küçük eski yanık izi
SUIT: kar beyazı sert kabuk EVA · **sırt TAMAMEN DÜZ** (sırt ünitesi/tank/
      hortum/kablo YOK) [D79] · vizör **optik olarak berrak**, tint YOK,
      ayna kaplama YOK, çevre yansıması YOK · diz/ön kol/bot burnu koyu gri
      aşınmış (her sahnede AYNI) · **hiçbir arma, bayrak, yazı, rakam,
      sembol yok** · eldivenler beyaz, avuç gri · göğüs konsolu: düşük
      sıcak anahtar ışığı (ekran/gösterge DEĞİL)
CHARACTER HEIGHT: 1,78 m

GRAVITY: 0,220 g SÜREKLİ İTKİ (a = 2,16 m/s²) — sıfır-g DEĞİL.
         "Yukarısı" pruva, "aşağısı" motor [ortam kartı §3.5]
ATMOSPHERE: sert vakum — ses YAYILMAZ. Duyulan her şey ya gövdeden/eldivenden
            İLETİLİR ya kask içindedir (nefes, fan) ya da müziktir
LOCOMOTION MODE: BASAMAK TIRMANIŞI, 0,5 m/s (S2'de 0,7 m/s) — botlar basar,
            her eldiven bırakır-kalkar-kavrar-yük alır. Süzülme/kayma/
            sıçrama 0 kare. ⛔ "zero-g locomotion" bulgusu YANLIŞTIR

LENS: 32 mm KÜRESEL → S0 · S1 · S3 · S5   |   75 mm KÜRESEL → S2 · S4
      (anamorfik YASAK — vakum kartı §3.1)
CAMERA DISTANCE: S0 14 m · S1 8,5 m · diğerleri promptta metre olarak
CAMERA MOVE: **6/6 TAM LOCKOFF** — üç kurulum da gövdeye/vinç koluna
      kelepçeli. Pan/tilt/dolly/zoom/sarsıntı/hız rampası 0 kare
      ⛔ Bu satır KLİP İÇİ karardır ve sahneler ARASI kurulumu anlatmaz;
      onu SETUP SEQUENCE satırı anlatır [02_RISK_KARTLARI KART 8 kapsamı]
SETUP SEQUENCE: A · B · C · D · C · E          (26.08.2026'da eklendi)
      A = 32 mm · 0,5 m gövdeden · 14 m · TEPE      → S0
      B = 32 mm · 0,4 m gövdeden                    → S1
      C = 75 mm · 7 m gövdeden · PROFİL             → S2 · S4
      D = 32 mm · 0,4 m gövdeden · 0,2 m mesafe     → S3
      E = 32 mm · 0,5 m gövdeden · TEPE             → S5
      kurulum sayısı 5 · 6 sahne → ACI_YAYI §4 bandı (≥3) ✅
      ardışık ikili hiçbir yerde aynı değil → §3 ✅
      A ↔ E döngüsel kapanış çifti (§9 son madde) — bilinçli
ANGLE ARC: **2 açı tipi — TEPE (S0 · S5) · PROFİL (S2 · S4)** [KAMERA_ACISI §2]
      🚨 AÇIK MADDE (26.08.2026): §2 en az 3 açı tipi ister; bu film 2
      taşıyor. S1 ve S3 kurulumlarının açısı promptta kılavuz sözlüğüyle
      YAZILMAMIŞ (§6: "low angle" / "high angle" gibi tutan sözcükler) —
      yani model o iki sahnede açıyı kendi seçiyor. Üçüncü tip buradan
      kazanılır: S3 (en yakın mesafe, 0,2 m) doğal ALT AÇI adayıdır.
LIGHT SOURCES: (a) kadraj DIŞI motor jantı — derin turuncu, alttan ·
      (b) hava kilidi lombozunun sıcak iç ışığı · (c) göğüs konsolunun
      düşük sıcak anahtarı · (d) yıldızlar. Başka kaynak YOK
FILL LIGHT ALLOWED: hayır — gölgeler mutlak siyah; tek istisna motor
      jantının ALT kenar yumuşaması
VEHICLE/STRUCTURE: 320 m kargo gemisinin çıplak dış gövdesi · çift raylı
      servis merdiveni, basamak aralığı 0,4 m · hasarlı montaj bandı ·
      hava kilidi halkası ve yuvarlak lomboz
DIALOGUE EXPECTED: **YOK — film tamamen repliksizdir** (tasarım, eksik değil)
AUDIO LAYERS (≤3): ① nefes + kask fanı ② gövdeden iletilen tok darbeler
      ③ müzik yatağı (120 BPM)
```

---

## B BLOĞU — KURGU VE ŞERİT (④ HİKAYE · kurgu kapısı ④)

```
THEME (intended): UMUT  ✅ (TEMA_MUHENDISLIGI §3 · sekizliden)
      Tek cümle: "Bu film, her şey düşerken tırmanmaya devam etmek
      hakkında." — cümlede novum kelimesi yok ✅
THEME SCENES (§5 matrisi): S1 · S5 + her sahne
      başın hedefe/ışığa dönüşü (S1 · S5) · avucun bir sonraki basamağa
      açılışı (her sahne) · soğuk kadranda iki sıcak nokta: hava kilidi
      penceresi (hedef) ve vizör içi konsol (yüz)
      ⚠️ Sapma kaydı [D74]: §5'in umut satırı sıcak sızıntıyı YANDAN
      önerir; burada sıcak değer ÜSTTE (hedef) ve İÇERİDE (konsol).
      Payoff (§6): S5 sonunda hava kilidi halkası nettir ✅
SCENE / SHOT / CLIP COUNT: 6 / 6 / 6
RUNTIME: 48,0 s hedef (6 × 8,0 s) — ⚠️ araç 10 s veriyorsa ızgara yeniden
         kurulur [D124]; ölçülen süre kapıya O SAYIYLA girer
TRIM BUDGET: 0,0 s  (8 s ızgarada) · 10 s araçta sahne başına 2,0 s kırpma
         PLANDA sahne sahne yazılmalıdır, yoksa kurgu kırpmaz [D100]
TARGET ASL BAND: 8,0 s — sabit ızgara, eğri yok (bilinçli sapma [D74])
İNSAN ŞERİDİ [D118]: 111111
EKRAN METNİ: 0,0 saniye — başlık kartı DAHİL [D61a/D70]
KESİLEMEZ SAHNELER: S0 (kanca + tohum) · S3 (latis) · S4 (merkezi seçim) ·
         S5 (doruk + twist + döngü)
DOĞAL DORUK: S5 — motorun 2,2 saniye susması (44,4-46,6, 48 s ızgarada)
TOHUM → KARŞILIK: S0 0:05,8 (jant 0,4 s kararır) → S5 44,4 (jant söner)
```

---

## C BLOĞU — KİLİTLER VE SIK YAPILAN YANLIŞ OKUMALAR (⑩ önerme kapısı)

```
✅ TASARIM — bulgu DEĞİLDİR:
   · Adamın AĞIR olması, botların basamağa basması → 0,220 g itki, 0 g değil
   · Serbest parçaların KIÇA doğru düşmesi → filmin novum'u
   · Yanma arasında (2,2 s) ağırlığın gitmesi → PLANLI TWIST, hata değil
   · S3'te 6 m'lik anten latisinin devrilip iki bağda asılı kalması → planlı
   · S5'te tether'ın kısa süre YOK olması değil — S4'te karabinerin AÇILMASI
     bir SEÇİM ve bedeli; devamlılık hatası değildir
   · Repliksizlik → ilan edilmiş kısıt [D113], düşük puan sebebi değil
   · Nefes ve fan sesi → kask içi, vakum ihlali değil
   · Vizörde turuncu jant ışığının GÖRÜNMESİ → berrak cam; yasak olan
     AYNA kaplama ve çevre yansımasıdır

🔴 GERÇEK İHLAL — bulgu SAYILIR:
   · Ekranda herhangi bir yazı/rakam/logo/arma (başlık kartı dahil)
   · Gezegen, ay, güneş diski, ikinci gemi, egzoz konisi, alev, toz, duman
   · Kamera hareketi (6/6 lockoff kilidi)
   · Serbest cismin süzülmesi, asılı kalması, kavis çizmesi, takla atması
   · Düşen bir parçanın adama DEĞMESİ (temas 0 kare)
   · İkinci insan, yansımada insan, klon
   · Sırt ünitesi/tank/hortum, vizör tinti, ayna kaplama
```

---

## D BLOĞU — SAYISAL KİLİT LİSTESİ (⑥ FİZİK merceğinin NUMERIC LOCK LIST'i)

> Bu blok doğrudan `6_FIZIK_QA_CRITIQUE_PROMPT.md`'nin lock list alanına
> kopyalanır. Her satır bir tablo satırı olur: PASS / FAIL / UNMEASURABLE /
> NOT EXERCISED.

```
GRAVITY: 0.22 g (a = 2.16 m/s²), continuous thrust, direction = toward the stern
LOCKS:
LOCK: free object fall — 1 s → 1.08 m · 2 s → 4.3 m · 3 s → 9.7 m · 5 s → 27 m
LOCK: free object leaves frame within 1 s of separation (frame ≈ 4 m tall)
LOCK: fall line is dead straight, parallel to the hull; curve/tumble/drift = 0 frames
LOCK: climb speed = 0.5 m/s (S2: 0.7 m/s)
LOCK: ladder rung spacing = 0.4 m
LOCK: man height = 1.78 m · ship length = 320 m · airlock distance 14 m → 2 m
LOCK: passing distances — S0 panel 1.4 m · S2 panel 1.2 m · S4 panel 1.1 m ·
      S5 lattice 1.0 m (contact = 0 frames)
LOCK: S3 lattice pivots 90° in ~2.3 s, then hangs, caught on two ties
LOCK: S5 burn gap = 2.2 s (44.4-46.6 in the 48 s grid): rim light out, boots
      lift one hand-width, tether plumb line curls, falling lattice stops gaining speed
LOCK: tether hangs as a straight plumb line whenever the engine is lit
LOCK: camera movement = 0 in all six scenes
LOCK: on-screen text = 0.0 s
```
