# 🎶 THE_COUNTED_RIVET — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR SAAT olarak okumalı — ölçtükçe büyüyen bir şeyin
    altında kalan zamanın sesi; huşu değil, HESAP."

TEMPO:        48 BPM — sahne uzunluğuna HİZALI (§14): 1 vuruş = 1,25 s ·
              1 klip = 10,0 s = 8 vuruş = 4/4'te TAM 2 ÖLÇÜ · her klip sınırı
              ve her sahne sınırı bir ölçü çizgisine düşer
              ⭐ TEMPO SEÇİMİNİN GEREKÇESİ: makinenin kehribar lambası 4,0 s
                 periyotludur ve 48 BPM'de vuruşlara 0 · 3,2 · 6,4 · 9,6 …
                 düşer — HİÇBİR ZAMAN vuruşun üstüne gelmez. Makine ile insan
                 aynı ölçüye girmez; tema bu yüzden mikste de duruyor. Lamba
                 DİEGETİKTİR, müzik katmanı değildir ve ona hizalanmaz.
SÜRE:         240,0 s = filmin RUNTIME'ı (24 × 10,0 s)
MÜZİKSİZ SAHNE: S1 (0,0-10,0 s) ve S5 (120,0-150,0 s)
              ⛔ her filmde EN AZ BİR tane (§10) — burada İKİ tane ve ikisi de
                 yapısal: S1 hook'tur, soru diegetik sesle sorulur; S5 filmin
                 TEK ÖLÇÜMÜDÜR ve 30 saniye boyunca müzik YOKTUR. Kanıt
                 müzikle desteklenirse izleyici müziğe inanır, ölçüye değil.
SUB-BASS:     45 Hz + 90 Hz oktav eşlikçisi + 135 Hz üçüncü harmonik
              (§15.1 — telefon hoparlörü 45 Hz'i hiç çalmaz; eşlikçi olmadan
              o katman telefonda YOK demektir)
VURUŞ NOKTASI: 3 tane — az olan güçlüdür
              150,0 s  S6 başlangıcı · ölçü 61 · alt uç bir kademe kalınlaşır
                       (iniş hızlandı; ses fizikle birlikte kalınlaşır)
              190,0 s  S7 başlangıcı · ölçü 77 · CUE B girer
              234,0 s  dokuzuncu boyun kopar · ölçü 112'nin 1. vuruşu ·
                       TEK sönümlü darbe, sonra alt uç çekilir
```

---

## 🎼 MÜZİK PROMPTU — tek global tema, iki cue

```
TOOL: Google Flow (Music)
GENRE: minimal industrial ambient — a slow mechanical clock, no melody
TEMPO: 48 BPM, 4/4

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. LOW DRONE — a sustained 45 Hz sine with an octave companion at 90 Hz and a
     third harmonic at 135 Hz, absolutely steady, no filter sweep, no swell.
     It is the dense air, not a mood.
  2. TICK — a single dry damped metal tick on beat 1 of every bar (every 2.5 s),
     the same velocity every time, never accented, never syncopated. This is the
     film's meter and it never changes speed.
  3. PLATE — a very quiet bowed-metal tone a fifth above the drone, entering and
     leaving on bar lines only, holding for whole bars. It thickens by one step
     at 150.0 s and by one more at 190.0 s, and it never thins again.
  4. COUNT (CUE B only) — a second dry tick on beat 3 of every bar, so the pulse
     reads twice as fast although the tempo has not moved.

CUE A "ÖLÇÜ"  — 10,0-120,0 s · layers 1+2, layer 3 from 40,0 s
CUE B "DOKUZ" — 190,0-236,0 s · layers 1+2+3+4
⛔ 120,0-150,0 s SESSİZ (S5) · 0,0-10,0 s SESSİZ (S1)
⛔ 150,0-190,0 s (S6): layers 1+2+3 only — CUE A'nın kuyruğu, one step thicker

DYNAMIC SPREAD — klip ızgarasıyla birebir:
    0,0- 10,0 s (K01 · S1): NO MUSIC. Diegetic only.
   10,0- 40,0 s (K02-K04 · S2): layers 1+2 enter on the bar line at 10,0 s,
                 −26 LUFS short-term, flat. Nothing builds.
   40,0-120,0 s (K05-K12 · S3-S4): layer 3 enters at 40,0 s on the bar line and
                 holds whole bars. Still flat — no crescendo anywhere in 80 s.
  120,0-150,0 s (K13-K15 · S5): ALL LAYERS OUT at the bar line at 120,0 s.
                 Silence through the cost and through the proof.
  150,0-190,0 s (K16-K19 · S6): layers 1+2+3 return at 150,0 s, the drone and
                 the plate ONE STEP thicker than they were. Tick unchanged.
  190,0-236,0 s (K20-K24 · S7): layer 4 enters at 190,0 s. At 234,0 s one damped
                 hit on beat 1, then the sub-bass and layer 4 are gone by 236,0 s.
  236,0-240,0 s: layers 2+3 only, thinning to layer 2, and the last tick lands on
                 239,0 s. The cue does NOT resolve — no final chord, no release.

SYNC RULE: every layer enters and leaves ON A BAR LINE, and every bar line falls
on a clip boundary or on the 5,0 s midpoint of a clip. The tick never moves. The
tempo never moves. Nothing accelerates: the sense of acceleration comes from the
picture (rows of rivet heads crossing the deck edge 40 s → 25 s → 18 s apart),
never from the music. ⛔ No ramp, no build, no drop.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     YOK — film bilinçli SESSİZ. HUMAN 0 · MACHINE 0.
              Bu seri diegetik yapay ses kullanır (suit AI · telsiz · kayıt);
              bu filmde üçü de KULLANILMIYOR. Muhatap bir SES değil bir OLAYDIR:
              sabit periyotlu kehribar lamba + mandalı yeniden germe.
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s ·
              dijital sıfır 0 kare · diyalog altında müzik/alarm −6 dB (uygulanmaz,
              replik yok) · kadraj dışı replik = telsiz band-pass (uygulanmaz) [D216]
KATMAN TABLOSU: — ③ SES LAYER COUNT bunu ölçer
```

| sahne | klip | katmanlar (ad) | sayı | köprü |
|:--:|---|---|:--:|---|
| S1 | K01 | oda tonu (yoğun CO₂ uğultusu) · çenenin tok kapanması · kask içi nefes | 3 | — (film başı) |
| S2 | K02-K04 | oda tonu · kehribar lamba 4,0 s · çekiç darbeleri · nefes | 4 | oda tonu kesintisiz, ≥0,2 s örtüşme |
| S3 | K05-K08 | oda tonu · lamba · otomasyon motor çekişi · nefes | 4 | oda tonu kesintisiz |
| S4 | K09-K12 | oda tonu · perçin sırası sürtünmesi · lamba · nefes | 4 | oda tonu kesintisiz |
| S5 | K13-K15 | oda tonu · halat sürtünmesi · şeridin tok yatması · nefes | 4 | oda tonu kesintisiz · **müzik YOK** |
| S6 | K16-K19 | oda tonu (bir kademe kalın) · perçin sürtünmesi (daha sık) · lamba · nefes | 4 | oda tonu kesintisiz |
| S7 | K20-K24 | oda tonu (iki kademe kalın) · makas kopma notaları · lamba · nefes | 4 | oda tonu kesintisiz |

```
⛔ ODA TONU 240,0 s BOYUNCA KESİNTİSİZDİR. Kesmede dijital sıfır 0 kare;
   17 sahne-içi kesmenin 17'sinde oda tonu köprü görevi yapar (J/L-cut).
⛔ ODA TONUNUN KADEMELERİ SAHNE SINIRINDA DEĞİŞİR, klip içinde asla:
   kademe 0 (S1-S5) → kademe 1 (S6) → kademe 2 (S7). Işık takvimiyle AYNI
   üç sahne sınırında ve AYNI yönde — ses ve ışık tek sayaç gibi çalışır.
REPLİK SAYISI: 0
REPLİK ZAMANLARI: — (0 replik; formül koşmaz)
⚠️ LAMBA SESİ BİR KATMAN DEĞİL BİR OLAYDIR: 4,0 s periyotludur, film boyu
   değişmez ve K24'te de aynı periyotta atar. ③ SES merceği bunu "monoton"
   yazarsa yanlış-pozitiftir — QA_SPEC'in duvarında yazılı.
```
