# 🎶 THE_SIGNAL_KEEPERS — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR ŞEYİN 41 YIL BOYUNCA ÖZENLE SAKLANMIŞ OLMASI
    olarak okumalı." — müzik bunu bir hayret olarak değil, bir BAKIM işi
    olarak taşır: sabırlı, sabit, süslemesiz.

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s klip · 72 BPM'de
              4/4'te bir ölçü 3,333 s → 10,0 s TAM ÜÇ ÖLÇÜ; her klip sınırı
              bir ölçü çizgisine düşer, 24 klip = 72 ölçü)
SÜRE:         240,0 s = filmin RUNTIME'ı (24 × 10,0 s · hook ofseti YOK)
MÜZİKSİZ SAHNE: S01 (0-30 s) ve S03 (70-120 s) — ⛔ her filmde EN AZ BİR tane (§10)
              ⭐ S03 müziksiz OLMAK ZORUNDA: novumun doğduğu sahne (K10-K11) ve
              filmin iki tiz olayı (donuk ton · berrak ton) orada duyuluyor.
              Müzik o iki tonun üstüne binerse tanıma anı ölçülemez hâle gelir.
SUB-BASS:     45 Hz + 90-135 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              sub-bass'ı hiç çalmaz, eşlikçi olmadan o katman yok demektir)
              ⚠️ Bu filmin ortamı kalın ve soğuk hava: tizi ÖLÇÜLÜ olarak ölü.
              Müziğin sözlüğü bu yüzden alt-orta banttan kurulur, 6 kHz üstünde
              hiçbir katman yok — ses tasarımının iki tiz olayı yalnız kalsın.
VURUŞ NOKTASI: 4 — 30,0 s (S02 girişi, ilk müzik) · 120,0 s (S04 girişi, ölçek) ·
              192,6 s (K20, HARD MUTE — müzik de kesilir) · 200,0 s (K21, tam giriş)
              ⭐ Az olan güçlüdür: dördünden biri bir SUSMA.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: ⬜ ÜRETİMDE YAZILIR (araç + sürüm birlikte)
GENRE: slow ambient drone, acoustic-leaning, no melody in the first half
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. one sustained low cello note, bowed very slowly, 45 Hz fundamental with its
     octave doubled at 90-135 Hz (enters 30.0 s)
  2. a single struck glass-like tone, one note, no reverb tail beyond 1.2 s
     (enters 120.0 s — it is the same interval as the film's two tapped tones)
  3. a slow four-note figure on a soft low piano, one note per bar, played only
     once through (enters 200.0 s)
  4. a second cello a fifth above the first, held (enters 210.0 s, last 30 s only)

DYNAMIC SPREAD — klip ızgarasıyla birebir:
  0.0-30.0 s (S01):    SILENCE — no music at all
  30.0-70.0 s (S02):   layer 1 only, entering over four bars, −22 LUFS short-term
  70.0-120.0 s (S03):  SILENCE — full stop at 70.0 s, one bar of decay allowed
  120.0-150.0 s (S04): layer 1 returns at the same level, layer 2 once at 120.0 s
  150.0-192.6 s (S05): layer 1 only, thinning out; nothing enters
  192.6-194.0 s (K20): HARD MUTE — digital zero on the music bus, 1.4 s
  194.0-200.0 s:       SILENCE continues (music does not creep back in)
  200.0-240.0 s (S06): layers 1 + 3 from 200.0 s, layer 4 from 210.0 s,
                       rising to −16 LUFS short-term and holding to the last frame

SYNC RULE: every layer entry and exit lands on a bar line (multiples of 3.333 s
from 0.0 s). The hard mute at 192.6 s is the ONE exception and it is deliberate:
it lands mid-bar, on the word the recording is cut in the middle of.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh. NO content above 6 kHz in any layer.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     RECORDED HUMAN × 2 (aynı cümle, biri bozuk biri net) · HUMAN 0 ·
              MACHINE 0 · kadrajda konuşan ağız 0 kare
              ⭐ Varlığın "sesi" replik DEĞİL: parmak ucuyla vurulan TEK TON.
              Organik kaynak (nefes + sürtünen mineral doku); sentetik/theremin YASAK.
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s ·
              dijital sıfır 0 kare (TEK istisna: 192,6-194,0 s planlı hard mute) ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass
              [D216 · 14.09.2026]
KATMAN TABLOSU: ③ SES LAYER COUNT bunu ölçer

| sahne | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S01 | oda tonu (alçak yakın uğultu) · nefes · panelin kuru vuruşu · kayıt (K02) | 4 | oda tonu kesilmez |
| S02 | oda tonu · nefes · bot/yaprak · tek kuru tıklama | 4 | oda tonu kesilmez |
| S03 | oda tonu · nefes · mineral sürtünme · tek ton (donuk/berrak) | 4 | oda tonu kesilmez |
| S04 | oda tonu (geniş hacim) · nefes · adım · uzak alçak akış | 4 | oda tonu kesilmez |
| S05 | oda tonu (çok alçak çok geniş) · nefes · metal gerilmesi · kayıt | 4 | K20'de kayıt gider |
| S06 | oda tonu · nefes · kilitlenme/halka · yükselen alçak taşıyıcı | 4 | 192,6-194,0 hard mute |

REPLİK SAYISI: 2 duyum · 1 cümle · SPEC `DIALOGUE LINES: 2` [D203]
REPLİK METNİ: "If anyone hears this, we are here."
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(K_n) = (n−1) × 10,0 + promptun TIMELINE ofseti
   K02 = (2−1) × 10,0 + 2,0 = 12,0 s   (bant-limitli, bozuk, anlaşılmaz — kaskın içi)
   K18 = (18−1) × 10,0 + 3,0 = 173,0 s (net, tam — sondanın ızgarası)
   KESİLME = (20−1) × 10,0 + 2,6 = 192,6 s → HARD MUTE 192,6-194,0 s [D180]
   ⛔ Üçüncü duyum YOK: K20 promptunda tırnaklı metin yazılmaz, yalnız kesilme taşınır.
⛔ İKİ TİZ OLAY — filmin tamamında: kaydın ünsüzleri ve camdan çıkan ton. Başka hiçbir
  katman 6 kHz üstünde içerik taşımaz; sebebi ortam kartı (kalın soğuk hava tizi yutar)
  ve sebebi aynı zamanda dramaturji (tanıma bir TİZ olayıdır).
```
