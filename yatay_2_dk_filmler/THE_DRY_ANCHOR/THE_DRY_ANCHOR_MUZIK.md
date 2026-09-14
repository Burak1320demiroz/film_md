# 🎶 THE_DRY_ANCHOR — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u ZEMİNİN BİR TABANI OLMAMASI olarak okumalı —
    bir tehlike ya da bir kaza değil, İŞLEYEN VE UMURSAMAYAN BİR KURAL."

TEMPO:        72 BPM — 10 s sahne → 3 ölçü/sahne (§14 tablosu; 240×3÷10=72).
              Her sahne sınırı (10 · 20 · 30 … 130 s) bir ölçü çizgisine düşer.
SÜRE:         140 s = filmin RUNTIME'ı (hook 10 s + 13 × 10 s klip)
MÜZİKSİZ SAHNE: S0 (hook · 0-10 s) · S10 (100-110 s) · S11 (110-120 s)
              — ⛔ her filmde EN AZ BİR tane (§10); burada ÜÇ, ve ikisi
              ARDIŞIK: kayıp anı (S10) ve doruk (S11) müziksizdir.
              S11'in son iki saniyesi (118,0-120,0) MUTLAK SESSİZLİKTİR:
              müzik yok, ses efekti yok, oda tonu yok.
SUB-BASS:     55 Hz (A1) + 110 Hz oktav eşlikçisi (§15.1 zorunlu · 90-160 Hz
              bandında) + 165 Hz üçüncü harmonik — kayıp temel (§15.1a):
              telefon hoparlörü 55 Hz'i çalmaz, 110+165 Hz onu İŞİTTİRİR.
VURUŞ NOKTASI: 3 tane, ÜÇÜ DE ölçü çizgisinde ve HİÇBİRİ bir eylemin üstünde
              değil (§13 mickey-mousing yasağı · §9 anempatik karar):
                 90,0 s  (S9 başı)  drone bir kademe DÜŞER
                 98,0 s  (S10'dan 2 s önce)  müzik BİTER
                120,0 s  (S12 başı)  tek nota geri döner
```

---

## 📋 §17 FİLM MÜZİĞİ KÜNYESİ

```
FİLM:                 THE_DRY_ANCHOR · 140 s · 14 sahne × 10 s
NOVUM OKUMASI:        "İzleyici bu görüntüyü, tabanı olmayan bir zeminde
                      çalışan bir insan olarak okumalı."   ← ÖNCE BU
MÜZİK-GÖRÜNTÜ İLİŞKİSİ: ANEMPATİK (§9 — bu serinin hiç kullanmadığı araç)
                      Gerekçe filmin kendisi: karşı güç bir ORTAMDIR ve
                      ortam umursamaz. Müzik de umursamaz — kasa toza
                      indiğinde (S9) yükselmez, bir kademe DÜŞER; doruğun
                      üstünde (S11) hiç yoktur.
TEMPO:                72 BPM → sahne başına 3 ölçü (§14 tablosu)
TONALİTE:             A eksenli modal drone (A1 55 Hz), üçlü YOK — majör de
                      minör de söylenmez. ⛔ ÇÖZÜLMEZ: film boyunca sıfır kez.
SESSİZLİK SAHNESİ:    S10 (müzik bu sahneden 2,0 saniye önce, 98,0 s'de biter)
                      + S11 · ayrıca hook S0 baştan müziksizdir
ÇÖZÜLMEYEN CÜMLE:     S8-S9'da yarım kalır (90,0 s'de bir kademe düşer,
                      cümle tamamlanmaz) → S12'de (120,0 s) TEK NOTA olarak
                      geri döner, tamamlanmaz → S13'te asılı kalır ve kesilir
KAPANIŞ:              fade out YOK · 140,0 s'de KESME (çözülmemiş asılı nota)
FREKANS TABANI:       sub 55 Hz + oktav eşlikçisi 110 Hz (+165 Hz)   ← §15.1
KATMANLAR:            3 katman:
                      ① 55/110/165 Hz drone — S1→S9 (10-98 s) aktif
                      ② çok kısık yaylı metal harmoniği (2-4 kHz, hava gibi)
                        — S2→S6 (20-70 s) aktif, S7'de çekilir
                      ③ tek tel/piyano notası (110 Hz) — yalnız S12-S13
                        (120-140 s), her ölçüde BİR kez, sönerek
LUFS HEDEFİ:          -14 nihai / -16…-18 müzik yatağı
REVERB KARARI:        neredeyse KURU — 610 Pa hava taşımaz: 0,25 s'den uzun
                      kuyruk yok, parlak erken yansıma yok. Vakum değil,
                      "ince atmosfer": kuyruğun kendisi karanlık ve kısa.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (tek parça · 140 s · sahne sahne ÜRETİLMEZ)
GENRE: minimal ambient score, anempathetic, no melody, no theme statement
TEMPO: 72 BPM (4/4 — one bar = 3,333 s, one scene = exactly 3 bars)

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. A sustained low drone on A: 55 Hz fundamental doubled by a quiet
     companion tone at 110 Hz and a third at 165 Hz, so the weight survives
     on a phone speaker. No third in the chord — neither major nor minor.
  2. A very quiet bowed-metal harmonic around 2-4 kHz, dry and thin, like
     air moving over a hard edge. It never rises above the drone.
  3. One struck string note at 110 Hz, once per bar, decaying — enters only
     in the last twenty seconds.

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
    0-10 s  (S0): SILENCE — no music at all under the hook
   10-20 s  (S1): layer 1 enters at the bar line, quiet, and holds
   20-70 s  (S2-S6): layer 2 joins; nothing swells, nothing builds
   70-90 s  (S7-S8): layer 2 withdraws; layer 1 alone, unchanged
   90-98 s  (S9): at the bar line the drone steps DOWN one whole tone and
                  stays there — it does not swell when the case is given up
   98-120 s (S10-S11): SILENCE — no music, no pad, no tail; the last two
                  seconds (118-120 s) are absolute silence
  120-140 s (S12-S13): layer 3 only, one note per bar, decaying, over the
                  drone returned at half its earlier level; the phrase is
                  never completed and never resolves; the final note is CUT
                  at 140,0 s, not faded

SYNC RULE: every change happens ON a bar line and NEVER on a physical event.
No hit follows the tool, the pin, the case or the ship. The score does not
react to the character at any point.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP. Reverb almost dry, tail under 0,25 s.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO swell into the climax, NO resolution.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     — (bu filmde diegetik yapay ses YOK: suit AI yok, telsiz yok,
              kayıt yok. Sebep ölçülmüş: 14 sahnede tek insan var ve MUHATAP
              ortamdır; bir ses kaydı ikinci bir zihin yaratırdı.)
REPLİK SAYISI: 0
REPLİK ZAMANLARI: koşmaz — 0 replik.
   ⛔ Bu satır boş bırakılamaz, çünkü boşluk uydurmayı davet ediyor:
     bir merceğin DÖRT İngilizce cümle "transkript" ettiği ölçülmüş vaka
     tam da replik alanı belirsiz olan filmde çıktı. QA_SPEC'in
     `DIALOGUE LINES: 0` satırı bu dosyayla ÇAPRAZ OKUNUR.
   Formül (D122) yine de yazılı durur, ileride replik eklenirse koşar:
     replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti

SES YATAĞI (müzik DEĞİL — her sahnede var, S11'in son 2 s'si hariç):
   ince rüzgâr (yüksek frekansı olmayan) · giysi fanı ve nefes (mikrofona
   yakın) · toz tanelerinin giysiye çarpması · metalin metale kısa, düz
   vuruşu (ince havada kuyruksuz)
   ⛔ 90 Hz altındaki iniş basıncı (S0) MÜZİK DEĞİLDİR, ses efektidir ve
     müzik yatağı hesabına girmez.
```
