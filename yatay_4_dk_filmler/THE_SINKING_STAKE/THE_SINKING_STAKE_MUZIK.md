# 🎶 THE SINKING STAKE — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR:
   "İzleyici bu novum'u BİR TEHDİT olarak DEĞİL, DÜNYANIN SESSİZ VE
    TARAFSIZ BİR KURALI olarak okumalı."
   Sonucu: müzik hiçbir yerde gerilim kurmaz, hiçbir yerde uyarmaz.
   Tehlike müziği yazılırsa film bir hayatta kalma filmine döner ve
   tema (kalıcılık) duyulmaz.

TEMPO:        72 BPM — sahne ızgarasına HİZALI (§14). 4/4'te bir ölçü
              3,333 s; 10 s sahne = TAM 3 ölçü. Her sahne sınırı bir ölçü
              çizgisine düşer. Hook 9,0 s = 2,7 ölçü → müzik 9,0 s'de,
              yani S1'in ilk ölçü çizgisinde başlar (S0 müziksizdir).
SÜRE:         249 s = 4:09 (hook 9 s + 24 × 10 s)
MÜZİKSİZ SAHNE: S0 (0:00-0:09) · S16 (2:39-2:49) · S24 (3:59-4:09)
              ⛔ §10 en az bir tane ister; burada üç tane var ve üçü de
                yapısaldır: S0 hook'un sessiz açılışı, S16 filmin mutlak
                sessizlik anı, S24 kapanış. S16 ve S24'ün video promptları
                zaten "absolute silence" diyor — müzik oraya GİRMEZ.
SUB-BASS:     34 Hz + 90-160 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              34 Hz'i hiç çalmaz; eşlikçi olmadan o katman yok demektir)
VURUŞ NOKTASI: 3 tane, hepsi az ve geç:
              0:14 (S1 · katalizör) · 1:59 (S12 · orta nokta) ·
              3:29 (S21 · doruk). Başka hiçbir yerde vurgu yok.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno
GENRE: minimal ambient score for a silent science-fiction short — sparse,
cold, patient, non-dramatic. Textural, not melodic.
TEMPO: 72 BPM, 4/4, absolutely steady, no rubato, no accelerando.

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Sustained low string bed (double bass and cello, bowed, no vibrato),
     one held note, entering at 0:09.
  2. A single high sine tone at the octave, entering at 0:39, almost
     inaudible, holding.
  3. Sub-bass sine at 34 Hz with a companion at 96 Hz, entering at 1:59.
  4. One prepared-piano note, struck once and left to decay, used only
     three times in the whole piece.
  5. Nothing else. No pads, no strings ensemble, no choir, no synth lead.

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
    0-9 s    (S0):        SILENCE. No music at all.
    9-39 s   (S1-S3):     one held low string note, very quiet;
                          a single prepared-piano note at 0:14
   39-119 s  (S4-S11):    the low bed continues; the high sine enters and
                          holds; no movement, no build, no swell
  119-129 s  (S12):       a single prepared-piano note at 1:59; the
                          sub-bass enters underneath and stays
  129-159 s  (S13-S15):   the bed thins to the sub-bass alone
  159-169 s  (S16):       SILENCE. Everything stops dead at 2:39 and
                          nothing plays for ten seconds.
  169-209 s  (S17-S20):   the low string returns alone, one note, quiet
  209-219 s  (S21):       the third and last prepared-piano note at 3:29;
                          the high sine and sub-bass come in together
                          underneath it and hold — no crescendo, no swell
  219-239 s  (S22-S23):   everything decays slowly and evenly
  239-249 s  (S24):       SILENCE. Nothing plays for the final ten seconds.

SYNC RULE: every entry and every exit lands exactly on a bar line at 72
BPM, which is exactly on a scene boundary. Nothing crosses a scene
boundary except the held low string bed.

MIX: mono compatible — all low end centred, no wide stereo that collapses
on a phone speaker. Target −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO percussion of any kind, NO braam, NO
riser, NO reversed cymbal, NO whoosh, NO impact hit, NO tension build,
NO horror sting, NO crescendo.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      HUMAN 0 · MACHINE 0 · DIEGETIC-INTERNAL yalnız.
               Bu filmde konuşan hiç kimse ve hiçbir şey yoktur. Duyulan
               her ses giysinin İÇİNDEN gelir: nefes, eklem yatağı
               gıcırtısı, gövdeden iletilen bot darbesi, halat gerilmesi.
REPLİK SAYISI: 0
SESSİZ SAHNE:  25 / 25 (replik yok)
REPLİK ZAMANLARI: yok — formül `replik(S_n) = 9 + (n−1) × 10 + TIMELINE
               ofseti` bu filmde BOŞ koşar. ⑨ HİZALAMA KAPISI'nın ölçü
               aleti bozulamaz çünkü ölçecek kayıt yoktur [D122].

⭐ DIŞ MEKÂN SES KURALI — bu filmin imzası:
   Atmosfer ~15 µbar; ses taşımaz. Süblimleşme patlamaları, kazığın
   düşüşü, gaz sütununun kalkışı: HEPSİ TAMAMEN SESSİZ. Kükremesi
   gereken yerdeki sessizlik tesadüf değil, tasarımdır ve rahatsız
   etmesi amaçlanmıştır.
   ⛔ Hiçbir sahnede dışarıdan gelen tıslama, uğultu, rüzgâr, çıtırtı
     ya da patlama sesi KULLANILMAZ. Tek istisna: aracın gövdesinden
     iletilen çok alçak yapısal uğultu (S4 · S11 · S18 · S23).
```
