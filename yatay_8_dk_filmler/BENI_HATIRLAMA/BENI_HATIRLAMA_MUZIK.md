# 🎶 BENI_HATIRLAMA — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9 · `SES_VE_DIYALOG_URETIM_KILAVUZU.md` §5-§6 ·
`KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §3 · karar kaynağı `00_ANALIZ/02_KONSEPT_VE_RISK.md` §10

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u bir tehdit değil, bir yardım çağrısı olarak okumalı."

TEMPO:        72 BPM — 10 s sahne = 12 vuruş = 4/4'te 3 ölçü; her sahne sınırı bir ölçü çizgisine düşer (§14)
SÜRE:         480 s = RUNTIME (48 × klip · klip 10 s VARSAYIM — ffprobe ölçümünden sonra ızgara yeniden hizalanır)
MÜZİKSİZ SAHNE: S0-S1 (0-20 s · ilk sesi rüzgâr taşır) · S36-S37 (360-380 s · DORUK) · S42-S45 (420-460 s · yalnız fırtına/kokpit)
              ⛔ S37 "müziksiz ≠ sessiz" [D83 · D180]: yatak + kask içi nefes −35/−40 dB kalır, dijital sıfır 0 kare
SUB-BASS:     55 Hz (A1) + 110 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü sub-bass'ı çalmaz)
VURUŞ NOKTASI: 2 — ① 320 s (S32 başı): tek alçak ton girişi, paylaşım/HUŞU anı · ② 460 s (S46 başı): filmin TEK çözülmesi
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (Lyria) — instrumental
GENRE: sparse ambient chamber score, grief turning to awe
TEMPO: 72 BPM

INSTRUMENTATION — layers in order of entry:
  1. low sustained cello drone on A, very soft, with a 55 Hz sub layer doubled at 110 Hz (from 20 s)
  2. felt piano, single low notes, one every two bars, never a melody yet (from 60 s)
  3. bowed glass harmonics, thin and high, only inside the cave (from 200 s)
  4. warm divided string pad, slow swell (from 250 s)
  5. solo cello line, a four-note motif that rises and does not finish (from 300 s)
  6. resolution: low strings and piano together complete the four-note motif once (460 s)

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-20 s (S0-S1): silence under wind — no music
  20-60 s (S2-S5): cello drone enters barely audible under the recorded voice at 22 s
  60-120 s (S6-S11): drone + single piano notes on bar lines; at 110 s (heat view) the piano stops for one bar
  120-200 s (S12-S19): drone steady, piano notes every bar, slightly closer; no rise
  200-250 s (S20-S24): glass harmonics join inside the cave; piano thins out
  250-300 s (S25-S29): string pad swells gently from 250 s (midpoint shelter) and falls back at 270 s (hands fail)
  300-320 s (S30-S31): solo cello motif, three notes, left unfinished
  320-330 s (S32): HIT ① one low sustained tone under the climbing light, pad opens wide
  330-360 s (S33-S35): pad contracts, drone only, getting thinner; everything fades out by 360 s
  360-380 s (S36-S37): NO MUSIC
  380-420 s (S38-S41): after the recorded voice at 382 s, a single held cello note returns very softly, then drone
  420-460 s (S42-S45): NO MUSIC — storm and cockpit sound only
  460-470 s (S46): HIT ② resolution — low strings and piano complete the four-note motif once, the only crescendo in the film
  470-480 s (S47): the last chord decays over the two pulsing lights; ends at 480 s

SYNC RULE: every change lands on a bar line (scene boundary); nothing lands inside a scene except the two hits at their scene starts

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
REGISTER:     MACHINE 6/6 — tek kayıt, yetişkin kadın sesi, küçük hoparlör bandı (band-pass ≈300-3400 Hz);
              görüntünün yönünden gelen ses de AYNI bant (register'ın kendisi ipucu) · uyarı: sözsüz warble (MACHINE)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = band-pass [D216 · 14.09.2026]
KATMAN TABLOSU:
  | blok | sahne | katmanlar (ad) | sayı | köprü |
  |---|---|---|:--:|---|
  | Y1 düzlük | S0-S19 | rüzgâr · kum hışırtısı · kask içi nefes · (S2/S8/S12 kayıt · S6 warble · S2-S19 drone) | ≤4 | rüzgâr tabanı kesintisiz |
  | Y1→Y2 | S19→S20 | rüzgâr söner, kaya uğultusu açılır | 3 | 1,5 s çapraz |
  | Y2 mağara | S20-S41 | kaya uğultusu · baca ıslığı (S23-S24, S25'te kesilir) · nefes · canlı hırıltısı / (S26/S35 warble · S36/S38 kayıt) | ≤4 | uğultu tabanı kesintisiz |
  | Y2→Y3 | S41→S42 | uğultu → fırtına kükremesi | 3 | 1,0 s çapraz |
  | Y3 fırtına | S42-S43 | alçak kükreme · kaska çarpan kum · nefes | 3 | — |
  | Y3→Y4 | S43→S44 | SERT KESME (planlı) · motor titreşimi başlar | 3 | 0,2 s oda tonu |
  | Y4 kokpit | S44-S45 | motor · gövdeye kum · nefes | 3 | — |
  | Y2 dönüş | S46-S47 | kaya uğultusu · canlının alçak sesi · atkı hışırtısı · müzik çözülmesi | 4 | S45→S46 1,0 s çapraz |
REPLİK SAYISI: 6 kullanım · 2 cümle · hepsi POST-DUB (klipte replik yok)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = n × klip + promptun TIMELINE ofseti   (hook S0 ızgaranın içinde)
   S2 22,0 s "Baba, gözlerini kapat." (görüntünün yönü) · S8 81,5 s aynı cümle (cihaz) + 83,3 s "Şimdi açabilirsin."
   (görüntünün yönü, BEKLEMEDEN) · S12 123,0 s ilk cümle kesik kesik (görüntünün yönü) · S36 363,0 s ilk cümle (cihaz) ·
   S38 382,0 s "Şimdi açabilirsin." (cihaz)
   ⚠️ S8'in ≤0,3 s boşluğu bilinçli: oyunun kuralı beklemektir, anında gelen cevap sahteliği ele verir.
   ⚠️ S37→S38 SES SMASH: 380,0 s'de müziksiz yatağın üstüne kayıt sesi — tek sert ses kesmesi.
SESSİZLİK PENCERESİ (makine kapısı SPEC E): 370-380 s müzik 0 · nefes yatağı dijital sessizliğin üstünde
```
