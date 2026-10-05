# 🎶 BLIND_ORBIT — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u GÖRMEYEN ELİN GÖREN BİR SESE TESLİM OLMASI olarak okumalı."
   — müzik bunu bir zafer marşı olarak değil, bir NEFES TUTMA olarak taşır: son
   yaklaşmada çekilir, sesi ve nefesleri yalnız bırakır; yalnız kenet tuttuktan
   sonra tek bir geniş açılımla geri gelir.

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s klip · 72 BPM'de 4/4'te bir
              ölçü 3,333 s → 10,0 s TAM ÜÇ ÖLÇÜ; her klip sınırı bir ölçü çizgisine
              düşer, 24 klip = 72 ölçü)
SÜRE:         240,0 s = filmin RUNTIME'ı (24 × 10,0 s · hook ofseti YOK)
MÜZİKSİZ SAHNE: S03 (80-120 s) ve S05 (180-210 s) — ⛔ her filmde EN AZ BİR tane (§10)
              ⭐ S03 müziksiz: onarımın bedeli MEKANİK seslerle ödenir (çark gıcırtısı,
              sönen tıslama, nefes) — müzik bedeli süslerdi.
              ⭐ S05 müziksiz OLMAK ZORUNDA: novumun kapandığı sahne — yalnız telsiz
              sesi, iki nefes ve dört kancanın dört ayrı tok vuruşu. Müzik o dört
              vuruşun üstüne binerse FİNAL VURUŞ KANITI kulakta sayılamaz.
SUB-BASS:     40 Hz + 80-120 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü sub-bass'ı
              hiç çalmaz, eşlikçi olmadan o katman yok demektir)
              ⚠️ Vakum: dışarıda ses yok. Müzik diegetik olmayan TEK katmandır; alt
              ucu gövde titreşimiyle (S06) çakışmasın diye 40 Hz'de tutulur, titreşim
              30 Hz civarında kalır.
VURUŞ NOKTASI: 4 — 3,33 s (ilk giriş, kayıt sesinin altına) · 80,0 s (S03 girişi —
              TAM DURUŞ) · 180,0 s (S05 girişi — TAM ÇEKİLİŞ) · 213,33 s (K22, makinenin
              "ten seconds" sözünden bir ölçü sonra — TEK GENİŞ AÇILIM)
              ⭐ Dördünden ikisi bir SUSMA.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: ⬜ ÜRETİMDE YAZILIR (araç + sürüm birlikte)
GENRE: slow orchestral ambient, sustained strings and soft low piano, no percussion
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. a low sustained string bed, cellos and basses bowed very slowly, 40 Hz fundamental
     with its octave doubled at 80-120 Hz (enters 3.33 s)
  2. one soft low piano note per bar, the same note, played quietly and evenly like a
     slow pulse — never faster (enters 20.0 s, S02 only)
  3. a slow rising two-chord figure in the violas and violins, held long, one chord
     every two bars (enters 213.33 s)
  4. a single high sustained violin line, quiet, the top of the opening, below 6 kHz
     (enters 220.0 s, the last 20 s only)

DYNAMIC SPREAD — klip ızgarasıyla birebir:
  0.0-3.33 s:           SILENCE — the flight recording and one breath alone
  3.33-20.0 s (S01):    layer 1 only, very low, −26 LUFS short-term
  20.0-80.0 s (S02):    layers 1 + 2, −22 LUFS short-term, flat — no swell on the
                        near-miss at K07 (the held breaths carry it)
  80.0-120.0 s (S03):   SILENCE — full stop at 80.0 s, one bar of decay allowed
  120.0-150.0 s (S04a): layer 1 returns alone at 120.0 s, −24 LUFS short-term
  150.0-180.0 s (S04b): layer 1 thins out bar by bar; at 170.0 s (K18 "Stay with my
                        voice.") it is barely audible; it ends on the bar line at 180.0 s
  180.0-213.33 s (S05 + K22 start): SILENCE — voices, breaths, four latch knocks
  213.33-240.0 s (K22 end · S06): layers 1 + 3 from 213.33 s, layer 4 from 220.0 s,
                        rising to −16 LUFS short-term and holding to the last frame,
                        under the whisper at 233.0 s (ducked −6 dB for 1.5 s)

SYNC RULE: every layer entry and exit lands on a bar line (multiples of 3.333 s from
0.0 s). The S06 opening is the ONE crescendo in the film; nothing else swells.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş stereo yok.
Hedef −14 LUFS · −1,0 dBTP. Diyalog altında müzik −6 dB.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh,
NO synth pulse, NO ticking clock sound. NO content above 6 kHz in any layer.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna atıf serbest;
> melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     HUMAN 13 (kask telsizi, band-pass) · MACHINE 2 (düz sentetik gemi sesi,
              kabin hoparlörü) · RECORDED HUMAN 2 (uçuş kaydı, band-pass, K01 K02) ·
              kadrajda konuşan ağız 0 kare
              ⛔ Vakumdan geçen ses 0: her ses bir gövdeden, koltuktan ya da giysiden
              taşınır (itici darbeleri · kanca vuruşları · titreşim içeriden duyulur)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 (müzik hariç) · her kesmede oda tonu
              köprüsü ≥ 0,2 s · dijital sıfır 0 kare · diyalog altında müzik/alarm −6 dB ·
              kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU: ③ SES LAYER COUNT bunu ölçer

| sahne | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S01 | telsiz taşıyıcı hışırtısı · kask içi nefes · uçuş kaydı (R1 R2) · itici darbesi (içeriden) | 4 | hışırtı kesilmez |
| S02 | kabin uğultusu · dalgalı ikaz tonu · itici darbeleri · telsiz/gemi sesi (R3-R7) | 4 | uğultu kesilmez |
| S03 | menfez havası · raylarda tok vuruş · çark gıcırtısı + sönen tıslama · nefes | 4 | menfez kesilmez |
| S04 | kabin uğultusu · telsiz hışırtısı · itici darbesi / kayış tokası · telsiz (R8-R13) | 4 | hışırtı kesilmez |
| S05 | telsiz hışırtısı · iki nefes · telsiz/gemi sesi (R14-R16) · dört kanca vuruşu | 4 | hışırtı kesilmez |
| S06 | iki gövdeden derin titreşim · nefes · fısıltı (R17) | 3 | titreşim kesilmez |

REPLİK SAYISI: 17 · SPEC `DIALOGUE LINES: 17` [D203] · promptlarda tırnaklı 17 (㉓ ✅)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(K_n) = (n−1) × 10,0 + promptun TIMELINE ofseti
   R1 1,0 · R2 12,0 · R3 31,5 · R4 35,0 · R5 56,0 · R6 71,0 · R7 74,5 · R8 112,0 ·
   R9 116,0 · R10 154,0 · R11 167,0 · R12 171,0 · R13 175,0 · R14 181,0 · R15 185,0 ·
   R16 210,5 · R17 233,0   (tam tablo: SPEC B BLOĞU)
⛔ Sayı söyleyen replik yalnız MAKİNE (R4 · R16) [D82] · aynı anda iki konuşmacı 0 [D35].
⛔ R12 → R13 arası 4,0 s: ikinci replik BİRİNCİDEN ALÇAK (fısıltıya yakın) — kurguda
   seviye −3 dB; R17 fısıltı, müzik altında −6 dB.
```
