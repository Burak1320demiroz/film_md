# 🎶 SUSMAYAN_NOBETCI — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9 · `SES_VE_DIYALOG_URETIM_KILAVUZU.md` §5-§6 ·
`KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §3 · karar kaynağı `00_ANALIZ/02_KONSEPT_VE_RISK.md` §9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici uyduyu bir düşman değil, kimsenin kapatmadığı bir SAAT olarak duymalı."

TEMPO:        66 BPM — 10 s sahne = 11 vuruş; sahne sınırları ölçü çizgisine YAKIN ama kilitli değil (§14),
              çünkü filmin kendi saati uydunun 2 saniyelik tarama ritmidir; müzik ona karşı çalar
SÜRE:         480 s = RUNTIME (48 × klip · klip 10 s VARSAYIM — ffprobe ölçümünden (K3) sonra ızgara yeniden hizalanır)
MÜZİKSİZ SAHNE: S0 (0-10 s · ilk sesi kabin uğultusu taşır) · S15-S16 (150-170 s · insanlı geminin vuruluşu) ·
              S36-S37 (360-380 s · DORUK: temas) · S45 (450-460 s · motor kopar)
              ⛔ "müziksiz ≠ sessiz" [D83 · D180]: kabin yatağı ve kask içi nefes −35/−40 dB kalır, dijital sıfır 0 kare
              ⛔ S45'in son iki saniyesindeki PLANLI SESSİZLİK kurguda yapılır (hard mute 453,0-455,0 s), promptta istenmez
SUB-BASS:     55 Hz (A1) + 110 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü sub-bass'ı çalmaz; üst armonik şart)
VURUŞ NOKTASI: 2 — ① 290 s (S29 başı): tek alçak ton, merkezî seçim · ② 460 s (S46 başı): filmin TEK çözülmesi
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (Lyria) — instrumental
GENRE: sparse ambient score for hard vacuum, machine pulse against human breath
TEMPO: 66 BPM

INSTRUMENTATION — layers in order of entry:
  1. a low sustained synth drone on A, very soft, with a 55 Hz sub layer doubled at 110 Hz (from 10 s)
  2. a single muted metal pulse every two seconds, dry and unchanging — the machine's clock (from 30 s)
  3. bowed double bass, one long note every four bars, always below the pulse (from 100 s)
  4. felt piano, single low notes off the pulse, never on it (from 200 s)
  5. a four-note cello line that rises and does not finish (from 290 s)
  6. resolution: bass and piano complete that four-note line once, together (460 s)

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-10 s (S0): no music — cabin hum and breath only
  10-30 s (S1-S2): drone enters barely audible under the first radio line
  30-100 s (S3-S9): drone + the two-second metal pulse; the pulse never changes tempo for the whole film
  100-150 s (S10-S14): bass enters under the pulse, one note every four bars
  150-170 s (S15-S16): NO MUSIC — the strike and the start of the spin carry only radio hiss
  170-290 s (S17-S28): pulse and bass return at the same level; piano notes enter at 200 s, always off the pulse
  290-360 s (S29-S35): the cello line rises, one note per scene boundary, and stops unfinished at 355 s
  360-380 s (S36-S37): NO MUSIC — contact and clamps in radio hiss and held breath
  380-450 s (S38-S44): pulse alone for twenty seconds, then bass under it; nothing rises
  450-460 s (S45): NO MUSIC — hard mute 453.0-455.0 s, then hiss only
  460-474 s (S46): the four-note line completes once, low and warm — the only resolution in the film
  474-480 s (S47): drone and pulse alone; the last two seconds are pulse only, unresolved
⛔ No percussion kit, no drums, no rising cinematic swell, no trailer hit, no brass, no choir, no vocals. [No Vocals]
```

---

## 🔊 SES YATAĞI VE REPLİK

```
YATAK ENVANTERİ (katman ≤4 · D216):
  Y1 kokpit: fan/pompa uğultusu + kask içi nefes                     (S0 · S3-S6 · S10 · S12 · S14 · S17 · S21-S23 · S28-S29 · S31 · S33-S34 · S38 · S44)
  Y2 dış vakum: yalnız telsiz taşıyıcı hışırtısı — DIŞ SES 0         (S2 · S7-S9 · S11 · S13 · S15-S16 · S18-S20 · S24 · S27 · S30 · S32 · S35-S37 · S39 · S43 · S45 · S47)
  Y3 kapsül içi: yakın fan + nefes                                    (S25-S26)
  Y4 dış giysi: gövdeden iletilen metal + nefes                       (S40-S42)
  Y5 tahliye bölmesi: oda tonu + geçitten gelen hava                  (S46)
KÖPRÜ:        her kesmede oda tonu köprüsü ≥0,2 s — dijital sıfır 0 kare [D83]
DUCKING:      replik altında yatak ve müzik −6 dB
TELSİZ:       kadraj dışı replik band-pass 300-3400 Hz + hafif hışırtı ✅ (S46 hariç: filtre YOK, oda sesi)
REPLİK:       8 satır POST-DUB (klipte üretilmez) — R1 12,0 · R2 25,0 · R3 73,0 · R4 94,0 · R5 141,5 · R6 144,0 ·
              R7 272,0 · R8 465,0 · hepsi <5 s, tek konuşmacı, ekranda ağız 0
              ⛔ saniyeler formülden gelir [D122]; klip süresi ölçülünce (K3) yeniden hesaplanır
İHRAÇ:        −14 LUFS · −1,0 dBTP · 48 kHz · AAC 384 kbps (E bloğu ebur128 kapısı ölçer)
```
