# 🎶 THE_FALLING_WORLD — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR BORÇ olarak okumalı: her kurtuluş birinin
   başkasının hattını ayırmasıdır ve müzik o ayırmayı ZAFER gibi çalmaz."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s sahne = 12 vuruş =
              tam 3 ölçü 4/4; her sahne sınırı bir ölçü çizgisine düşer)
SÜRE:         480 s = filmin RUNTIME'ı (48 × 10 s)
MÜZİKSİZ SAHNE: S00 · S01 · S02 (0-30 s) · S16 · S17 (160-180 s) · S38 · S39 (380-400 s)
              — 7 sahne. ⛔ Açılış müziksiz: ilk 30 saniyede tek diegetik katman
              (§10). BEDEL sahnesi (S16) ve SÜKÛNET/uzanamama (S38-S39) de müziksiz.
SUB-BASS:     38 Hz + 96 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü sub-bass'ı
              hiç çalmaz; eşlikçi olmadan o katman yok demektir)
VURUŞ NOKTASI: 4 — 300 s (S30 sükûnet) · 410 s (S41 doruk) · 420 s (S42 ayrılma) ·
              470 s (S47 kapanış). Az olan güçlüdür; S13 ve S25 kayıpları
              MÜZİKLE vurgulanmaz, sesle taşınır.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow music
GENRE: slow orchestral drone with one plucked string voice, no percussion
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. low bowed string bed, 38 Hz fundamental with a 96 Hz octave companion (from 30 s)
  2. single plucked low string, one note per bar, never a melody (from 120 s)
  3. high sustained string, one long note holding across scene boundaries (from 240 s)
  4. second plucked string a fifth below the first, answering the first (from 410 s only)

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-30 s (S00-S02):    SILENT — diegetik ses tek başına
  30-160 s (S03-S15):  layer 1 alone, quiet, no swell
  160-180 s (S16-S17): SILENT — bedel sahnesi ve malzemedeki kanıtı
  180-240 s (S18-S23): layer 1 returns, layer 2 enters at 240 s
  240-300 s (S24-S29): layers 1+2, slow rise into the reversal
  300-310 s (S30):     ACCENT 1 — layer 3 enters on the bar line at 300 s
  310-380 s (S31-S37): layers 1+2+3 holding, no swell
  380-400 s (S38-S39): SILENT — üç parça hat ve uzanamama
  400-410 s (S40):     layer 1 alone returns under the separation
  410-420 s (S41):     ACCENT 2 — layer 4 enters on the bar line at 410 s (DORUK)
  420-430 s (S42):     ACCENT 3 — layers 2 and 4 answer each other once, then stop
  430-470 s (S43-S46): layers 1+3 only, falling
  470-480 s (S47):     ACCENT 4 — all layers hold one chord, cut at 478 s;
                       last two seconds carry only the diegetic low bed

SYNC RULE: müzik olayı ÖNCEDEN haber vermez. Her aksan olayın 0,0 saniyesinde
DEĞİL, 0,4 saniye SONRASINDA girer — izleyici önce görür, sonra duyar.
Ölçü çizgileri sahne sınırlarına düşer (10 s = 3 ölçü), aksanlar ölçü başında.

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
REGISTER:     HUMAN ×8 — hepsi TELSİZ (band-pass, kadraj dışı ya da opak vizör ardı);
              MACHINE ×0. Bu filmde suit AI ya da kayıt sesi YOK.
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU: aşağıdaki tablo (③ SES LAYER COUNT bunu ölçer · tavan 4)
REPLİK SAYISI: 8 (post-dub · klipte 0 üretilir)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = n × 10 s + promptun TIMELINE ofseti
⛔ dijital sıfır 0 kare — S47'nin son iki saniyesi SESSİZ DEĞİL, yalnız alt yatak.
⛔ Diyalog altında müzik/alarm −6 dB; sekiz repliğin dördü zaten müziksiz sahnede.
⛔ AĞIZ HİÇBİR KAREDE GÖRÜNMÜYOR (opak vizör) → lip-sync riski FİZİKEN sıfır;
   bedenleştirme (§1a.1) imkânsız ve doruk bütçesi serbest kaldı.
⛔ KLİP SÜRESİ AÇIK [D124 · K3]: 10 s bir varsayımdır. Ölçüm 10 s'den saparsa
   aşağıdaki sekiz saniye VE DYNAMIC SPREAD'in her satırı yeniden hesaplanır.
```

### 🎚️ KATMAN TABLOSU

| sahne bandı | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S00-S07 dış yüzey | boğuk uğultu · kask içi çift nefes · toz akışı · (S07 telsiz) | 3-4 | oda tonu 0,3 s |
| S04·S07 araç kabini | gövdeden motor titreşimi · çift nefes · (S07 telsiz) | 3 | oda tonu 0,3 s |
| S08-S13 ocak | duvardan boğuk yankı · çift nefes · yol gürültüsü | 3 | oda tonu 0,3 s |
| S14-S18 galeri içi | kapalı hacim · gövdeden metal gerilmesi · çift nefes · (S16 telsiz) | 3-4 | oda tonu 0,4 s |
| S19-S29 yarık | boğuk uğultu · çift nefes · halat yükü · (S19·S26 telsiz) | 3-4 | oda tonu 0,3 s |
| S30-S39 platform | gemi hazırlık uğultusu · nefes · metal yük · (S33·S39 telsiz) | 3-4 | oda tonu 0,3 s |
| S33·S40·S43-S46 kabin | basınçlı iç · fan · net telsiz · nefes | 3-4 | oda tonu 0,2 s |
| S45·S47 insansız | uzaklaşan uğultu · derin itki notası | 2 | oda tonu 0,5 s |

### 🎙️ REPLİK ZAMANLARI — formülle

| # | S | hesap | saniye | konuşan | İngilizce (post-dub) |
|---|---|---|---|---|---|
| R1 | S07 | 7×10+4 | 74 s | TURUNCU | Ship's still tied down. |
| R2 | S16 | 16×10+6 | 166 s | BEYAZ | Left cuff is locked. |
| R3 | S19 | 19×10+3 | 193 s | TURUNCU | The mast takes us across. |
| R4 | S26 | 26×10+4 | 264 s | BEYAZ | Hold it. |
| R5 | S33 | 33×10+5 | 335 s | TURUNCU | Engines are up. |
| R6 | S39 | 39×10+4 | 394 s | BEYAZ | I can't reach it. |
| R7 | S40 | 40×10+2 | 402 s | BEYAZ | Stay in the seat. |
| R8 | S46 | 46×10+6 | 466 s | TURUNCU | Still here. |
