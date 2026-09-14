# 🎶 THE_LOCKED_PULSE — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u KAYITSIZ BİR MAKİNENİN HESABI olarak okumalı: halka hızlandıkça her şey ağırlaşır ve müzik BUNU
    UMURSAMAZ — nabız sabit kalır, olay büyür, tempo değişmez (ANEMPATİK). Makine haklıdır; müzik makinenin tarafındadır."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s sahne = tam 12 vuruş; her sahne sınırı bir ölçü çizgisine düşer;
              9 s hook müziksiz olduğu için ilk ölçü 19,0 s'de S2 ile başlar)
SÜRE:         249,0 s = filmin RUNTIME'ı (9 + 24 × 10) — müzik 19,0-197,5 (CUE A) + 241,0-249,0 (CUE Z)
MÜZİKSİZ SAHNE: S0-S1 (0,0-19,0 · hook: tek diegetik ses) · S20-S23 (197,5-241,0 · doruk sessizliği + bedel: yalnız fan, nefes, tık,
              röle) — ⛔ her filmde EN AZ BİR tane (§10): bu filmde iki pencere, 3 müziksiz blok sayılır (hook · doruk-bedel · —)
SUB-BASS:     45 Hz taşıyıcı + 90-160 Hz OKTAV EŞLİKÇİSİ (§15.1 — telefon hoparlörü sub'ı çalmaz) + 100/150/200 Hz armonik yığın
              (missing fundamental: taşıyıcı seviyede, yedek değil — YERÇEKİMİ TUR 2 ② kararı)
VURUŞ NOKTASI: 3 — ① 19,0 s müzik girer (anahtar yere indikten 0,1 s sonra değil: 19,0'da, sahne sınırında; darbe değil GİRİŞ)
              ② 123,0 s (S12 kilit tıkı) — müzik burada VURMAZ, aksine bir ölçü boyunca tek nota tutar (anempatik: makine tıkı alkışlamaz)
              ③ 197,5 s müzik KESİLİR (doruktan 1,5 s önce; fade yok) · ④ 241,0 s çözülmemiş tek akor girer, 249,0'da kesilir
              (az olan güçlüdür — 3 gerçek vuruş: giriş · kesiliş · son akor)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow (music) — tek parça, iki cue tek promptta üretilip kurguda kesilir
GENRE: minimal industrial ambient — a single mechanical pulse, no melody, no drums
TEMPO: 72 BPM, strict, never drifts, never accelerates (the ring accelerates; the music does not)

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. sub-bass pulse: one soft low tone struck once per beat at 72 BPM, fundamental around 45 Hz, with its octave partner around 90-160 Hz
     carried at the same level (the octave is not a support, it is the carrier on small speakers)
  2. a sustained metallic drone one octave above the pulse, faint, like a large fan heard through a wall, unbroken
  3. from the second minute a second pulse an octave up, offset half a beat — the two pulses never lock into a rhythm, they only coexist
  4. a single held chord, unresolved (a suspended fourth over the bass), used only for the last eight seconds

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0,0-19,0 s (S0-S1):    SILENCE — no music at all (diegetic hum and alarm only)
  19,0-59,0 s (S2-S5):   layer 1 only, very low; enters exactly on the bar line at 19,0 s, no swell
  59,0-129,0 s (S6-S12): layer 1 + layer 2; the level does NOT rise as the scenes get heavier; at 123,0 s (the latch click) the pulse
                         keeps its beat and the drone holds one bar without change — nothing in the music marks the click
  129,0-139,0 s (S13):   layer 1 + 2 continue unchanged over the exterior (non-diegetic; there is no exterior sound)
  139,0-197,5 s (S14-S19): layer 3 joins at 139,0 s; still no rise in level; at 197,5 s the whole music STOPS on the beat — hard cut, no fade,
                         no ring-out; 1,5 s before the peak scene begins
  197,5-241,0 s (S20-S23): SILENCE — no music (fan, breath, one click, one relay click only; 203,0-205,0 s is a hard mute in the edit)
  241,0-249,0 s (S24):   layer 4 alone: one unresolved chord enters at 241,0 s, holds, and is cut at 249,0 s — no resolution, no fade

SYNC RULE: every scene boundary (9 + 10k seconds) falls on a bar line at 72 BPM; the pulse never changes tempo or level to follow the
action — it is the machine's pulse, not his. The only three musical events are: the entry at 19,0 s, the stop at 197,5 s, the chord at 241,0 s.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş stereo yok. Hedef −14 LUFS · −1,0 dBTP (film masterı);
müzik yatağı −16…−18 LUFS, diyalog/anons ve nefes üstte.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh, NO tempo change, NO crescendo at the peak.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     MACHINE ×6 — halka otomasyonu, tavan hoparlörü (5) + telsiz (1, S13 dış); düz sentetik, dolgu yok, edilgen cümle
              ("Coolant pressure has dropped."); HUMAN 0 · UNCLEAR 0. Bu seri diegetik yapay ses kullanır; düz okuma TASARIMDIR.
REPLİK SAYISI: 6 (S1 · S6 · S9 · S12 · S13 · S18) — son replik S18 181,0 s; S19-S24 replik 0 (doruk + final SESSİZ)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   #1 11,0 · #2 61,0 · #3 92,0 · #4 125,0 · #5 132,0 · #6 181,0  (klip 10,0 s varsayımı; ffprobe ölçümü sapıyorsa yeniden hesaplanır)
ÜRETİM:       replikli klipler SESSİZ üretilir (kapalı vizör = oklüzyon, lip-sync yapısal sıfır); anons post'ta biner;
              'a flat synthetic voice from the ceiling speaker' — TTS düz, oda yankısı KISA (metal koridor), telsiz (#5) bant sınırlı + taşıyıcı hışırtı
YATAK:        fan + pompa uğultusu — TEK PARÇA, 24 iç sahne boyunca kesintisiz, klip sınırında dijital sıfır 0 s [D83]; S13 (129-139) yatak YOK
              (vakum) → yalnız telsiz taşıyıcısı; sessizlik = OLAY yalnız 203,0-205,0 (HARD MUTE, kurguda) [D180]
ALARM:        warble, periyot 2,0 s (S0-S5) → 1,5 s (S6-S12) → 1,0 s (S14-S24); ışıkla senkron (ışık takvimi D193); S20'de zayıf/uzak
SFX (post):   23,9 s anahtar zemine (tek clack) · 33-38 s jet tıslaması + çark gıcırtısı + geri tepme knock · 62 s dolap kapağı · 72-77 s metal inilti ·
              80-84 gıcırtı, sonra tıslama incelir · 105 s tıslama kesilir · 123,0 s tek tık · 154,9 s levye clang · 224,0 s mühür tık ·
              233,0 s röle tıkı · nefes: kask içi, yakın, S4/S14/S16/S17 tutulur, S21 ilk uzun nefes
MİKS SIRASI:  anons > nefes > SFX > alarm > yatak > müzik (anempatik: müzik hep altta) · doruk (S20) müzik 0, alarm −12 dB, nefes +3 dB
İHRAÇ:        48 kHz · −14 LUFS · −1,0 dBTP · ses kanalı ffprobe ile doğrulanır (SPEC E ⑤ ⑥)
```
