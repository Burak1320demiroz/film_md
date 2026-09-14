# 🎶 THE LEANING ROOM — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR SÜRÜŞ HİSSİ olarak okumalı — odanın yatması bir
    arıza değil, bir DÖNÜŞTÜR; müzik korku değil AĞIRLIK taşır."

TEMPO:        72 BPM — 10 s'lik sahneye hizalı (§14: 72 BPM'de bir ölçü
              3,333 s; üç ölçü tam 10,0 s eder ve HER sahne sınırı bir ölçü
              çizgisine düşer). 12 sahne = 36 ölçü.
SÜRE:         120,0 s = 10,0 s hook + 11 × 10,0 s
MÜZİKSİZ SAHNE: S9 (90,0-100,0 s) TAMAMEN sessiz — ⛔ §10'un zorunlu tekidir.
              Ayrıca S6'da 61,5 s'de müzik KESİLİR ve 70,0 s'e kadar yoktur
              (başarısız denemenin altında yalnız nefes ve kordon).
SUB-BASS:     34 Hz temel + 102 Hz oktav eşlikçisi (§15.1 — telefon
              hoparlörü 34 Hz'i hiç çalmaz; eşlikçi olmadan gemi ağırlığı
              küçük hoparlörde YOK demektir)
VURUŞ NOKTASI: 3 tane, hepsi az ve geç:
              ① 72,0 s (S7 · merkezi seçim) — alt uç bir oktav DÜŞER
              ② 96,0 s (S9 · her şeyin kaybı) — her şey susar, tek nota kalır
              ③ 113,0 s (S11 · final vuruşu) — tek nota ÇÖZÜLMEZ, asılı kalır
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow / Lyria
GENRE: minimal orchestral drone, chamber scale, no percussion
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. bowed double bass, sustained, one note, very low in the mix (0 s)
  2. a single sustained cello line, slow, no vibrato (20 s)
  3. brushed metal resonance — the sound of a struck brass body ringing
     out, sparse, one strike every eight bars (40 s)
  4. a high sustained string harmonic, thin, almost inaudible (100 s)

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-20 s    (S0-S1): bass alone, steady, very quiet — room tone, not theme
  20-40 s   (S2-S3): cello enters, one long phrase, unresolved
  40-50 s   (S4):    everything thins to the bass; the brass resonance
                     answers the lamp once
  50-60 s   (S5):    cello rises a whole tone and stays there, pressure
                     without acceleration
  60-70 s   (S6):    ⛔ music CUTS OUT at 61.5 s and does not return in
                     this scene
  70-80 s   (S7):    at 72.0 s the low end drops an octave and holds; no
                     swell, no rise, no hit — weight, not alarm
  80-90 s   (S8):    the low octave alone, slowly thinning
  90-100 s  (S9):    ⛔ COMPLETE SILENCE — no music of any kind
  100-110 s (S10):   the cello returns underneath, quiet, in the same key
                     as at 20 s but a semitone lower
  110-120 s (S11):   a single high string harmonic holds over the cello and
                     does not resolve; it is still sounding at 120.0 s

SYNC RULE: every scene boundary falls on a bar line (72 BPM · 3 bars per
scene). No transition sits inside a scene. The two silences are absolute:
no tail, no reverb bleed across the cut into S9.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO ticking clock, NO heartbeat.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     ⛔ DIEGETİK YAPAY SES YOK. Bu filmde gemi konuşmaz, telsiz yok,
              kayıt yok, yapay zekâ sesi yok. Duyulan her şey TEMASTIR.
REPLİK SAYISI: 0
REPLİK ZAMANLARI: yok — ama formül OLAY zamanlarına uygulandı ve her kayıt
              doğrulandı; tam liste `THE_LEANING_ROOM_QA_SPEC.md` B bloğunda.
              replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti

DİEGETİK YATAK (tek parça, klip sınırında ölmez [D83]):
  · GÖVDE UĞULTUSU — ağırlığın kendisi. Kalınlığı itkiyle değişir ve
    değişim SAHNE İÇİNDE duyulur:
      ince      S0-S4 · S10-S11   (0,250 g)
      kalın     S5-S6             (0,269 g)
      çok kalın ve alçak  S7-S8   (0,667 g — perde bir oktav düşer)
  · KORDONUN PİRİNCE TEK KURU TIKI — filmin iki ucundaki AYNI ses:
      S0 · 7,0 s (17,0 s mutlak) ve S11 · 5,0 s (115,0 s mutlak)
      ⛔ Bu iki tık aynı örnekten alınır; açılış ve kapanış çiftini SESLE
        de kurar. Aradaki 98 saniyede bu ses BİR KEZ BİLE duyulmaz.
  · TEMAS SESLERİ: deri gıcırtısı · yün üstünde yün · tahtada pirinç ·
    cam üstünde pirinç (yalnız 82,3 s'de, bir kez)
  · NEFES: S6 ve S9'da öne çıkar; müzik orada zaten yoktur.

⛔ DIŞARIDA SES YOK (§3.1 vakum). Kütlelerin geçişi SESSİZDİR — geçen
  gezegen uğuldamaz, karadelik ses çıkarmaz. Duyulan her şey gövdeden gelir.
```
