# 🎶 THE_GREEN_CEILING — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

## 📋 §17 FİLM MÜZİĞİ KÜNYESİ — müzik promptundan ÖNCE

```
FİLM:                 THE_GREEN_CEILING · 249 s · 25 sahne × 10,0 s (hook 9,0 s)

⭐ NOVUM OKUMASI [§12 — bu cümle yazılmadan müzik promptu yazılmaz]:
   "İzleyici bu novum'u **KAYITSIZ BİR YASA** olarak okumalı — tehdit değil,
    ceza değil, mucize değil. Zemin bırakır çünkü bu dünyanın kuralı budur."
   ⚠️ Aynı kare üç ayrı müzikle üç ayrı tür olur: gergin drone → korku ·
     yalnız çello → yas · hareketsiz sakin nabız → kayıtsızlık. Seçilen üçüncüsü.

MÜZİK-GÖRÜNTÜ İLİŞKİSİ:  ⭐ANEMPATİK [§9] — fırtına büyürken müzik TEPKİ VERMEZ.
   Bu deponun hiç kullanmadığı araç ve bu filmin temasının (ENTROPİ) işitsel
   karşılığı. ⚠️ Anempatik ≠ neşeli: bizim hâlimiz DEĞİŞMEYEN müziktir.
   ⛔ TEK BİLİNÇLİ İSTİSNA: S17 UMUT vuruşunda tek nota BİR KEZ yükselir ve
     S18'de geri çekilir. Gerekçe plana yazıldı; anempatik kural o on saniye
     için askıya alınır, sonra geri döner.

TEMPO:                48 BPM → 10 saniyelik sahne başına TAM 2 ÖLÇÜ (4/4)
   ⭐ IZGARA 9,0 s'YE ÇAPALANIR, 0'a değil: hook 9 s olduğu için ölçü çizgisi
     filmin başında değil hook'un SONUNDA başlar. 48 BPM'de bir ölçü 5,0 s;
     9,0 s'den sonraki her sahne sınırı (19 · 29 · 39 … 249) bir ölçü başına
     denk gelir. Film 9,0 s + 48 ölçü = 249,0 s.
   ⛔ Hizasız BPM ölçülmüş bir hatadır [§14.2: DEAD APPROACH 130 BPM → 5,42
     ölçü · REMEMBERING DUST 58 BPM → 2,42 ölçü].

TONALİTE:             D minor, çözülmesiz. Kadans film boyunca TEK KEZ gelir
                      (S21, doruk) ve o an müzik zaten susmuştur — ⭐çözülme
                      SESSİZLİKLE verilir [§11: "the phrase does not resolve"].

SESSİZLİK SAHNESİ:    **S21** (209-219 s) — DORUK. Müzik 207,5 s'de biter,
                      yani sahne başlamadan 1,5 saniye ÖNCE [§10: sessizliğin
                      fark edilmesi için 1-2 saniye gerekir].
   ⛔ Saatler HESAPLANMADI, HESAPLATILDI [D122]: sahne_başı(n) = 9 + (n−1) × 10;
     n=21 → 209 s. Bu bloğun elle yazılan ilk hâli S13'ten sonra bir sahne
     kaymıştı ve formülle koşturulunca yakalandı.
   ⛔ [D180] PLANLI SESSİZLİK VİDEO MODELİNDEN İSTENMEZ — kurguda HARD MUTE
     ile yapılır ve QA_SPEC E bloğuna komut olarak yazılır. İki film üst üste
     doruğunu bu yüzden kaybetti (sessizlik doruktan beş saniye sonra geldi).
   ⚠️ S21 sessiz DEĞİL, MÜZİKSİZDİR: motorun gövdeden iletilen sesi sahnenin
     son 1,5 saniyesinde kesilir; nefes o an bile sürer [D83 — mutlak dijital
     sıfır bir HATADIR].

ÇÖZÜLMEYEN CÜMLE:     S6'da başlayan alçak yürüyüş figürü S12'de yarım kalır
                      ve S15'te tamamlanır. Yapı = tema.

KAPANIŞ:              ⛔ FADE OUT YOK — KESME. Çözülmemiş akor. [§7 5. işlev
                      bu seride TERSİNE çevrilir: film kapanmaz, DURUR.]
                      Son nota S23'ün temas sesinde kesilir ve S24'te müzik YOKTUR.

FREKANS TABANI:       sub 45 Hz + oktav eşlikçisi 90 Hz ve 135 Hz
   ⭐ [§15.1a MISSING FUNDAMENTAL] eşlikçi bir YEDEK değil, temeli beyinde
     İNŞA EDEN unsurdur — kısık değil TAŞIYICI seviyede mikslenir. Üstüne
     ~100 / 150 / 200 Hz'de yoğun armonik yığın: 150 Hz altındaki her şeyin
     tamamen kaybolduğu varsayımıyla ağırlık AYAKTA kalmalı.
   ⛔ İnfrasound (17-19 Hz) KULLANILMAZ — teslim edilemez, kötü takas.

KATMANLAR:            4 katman (aşağıda, giriş sırasıyla)
LUFS HEDEFİ:          −14 nihai · müzik yatağı −16…−18 · S21 GERÇEKTEN müziksiz
REVERB KARARI:        ⭐İKİ REJİM — filmin işitsel imzası bu geçiştir:
                      S0-S21 KALIN ATMOSFER → ıslak, yakın, alçak; düşük
                        frekanslar iyi taşınır, yankı KISA ama YOĞUN
                      S22-S24 VAKUM → tamamen KURU, yankı YOK; müzik gövdeden
                        iletilmiş gibi, dış akustik sıfır
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

> ⛔ [§14.1] MÜZİK TEK PARÇA ÜRETİLİR, sahne sahne DEĞİL. 25 klibi tek film
> yapan yegâne bağ odur (Copland §7.4 DEVAMLILIK).

```
TOOL: Suno / Lyria — one single continuous instrumental piece, 249 seconds.
GENRE: slow cinematic drone score, patient and unreactive, no melody.
TEMPO: 48 BPM, 4/4, strictly steady. No rubato, no accelerando, no ritardando.
KEY: D minor, unresolved throughout; the phrase does not resolve.

INSTRUMENTATION — layers in order of entry:
  1. a sustained low drone at 45 Hz, doubled by a companion tone at 90 Hz and
     again at 135 Hz, with a dense harmonic stack at roughly 100 Hz, 150 Hz and
     200 Hz so the missing fundamental is implied rather than played; the
     perceived weight must survive full loss of everything below 150 Hz
  2. a second drone one octave below the first, entering later and never leaving
  3. a slow low pulse, one soft stroke every two bars, unchanging in level
  4. a single thin high tone, entering once and withdrawing once

DYNAMIC SPREAD — locked to the scene grid, the bar line anchored at 9,0 s:
  0-19 s      (S0-S1)   silence. The piece has not started.
  19-59 s     (S2-S5)   layer 1 alone, entering on a single note, level and flat
  59-89 s     (S6-S8)   layer 2 enters underneath; the phrase begun here is left
                        unfinished
  89-129 s    (S9-S12)  layer 3 enters; from here nothing in the music reacts to
                        anything on screen, however large the event
  129-169 s   (S13-S16) all three layers hold, unchanged in level and pattern
  169-179 s   (S17)     layer 4 enters and rises once — the only rise in the piece
  179-189 s   (S18)     layer 4 withdraws and does not return
  189-207,5 s (S19-S20) layers thin to one; the piece reaches its quietest point
  207,5 s     ⭐ the music stops. Not a fade — it stops.
  209-219 s   (S21)     no music at all
  219-229 s   (S22)     one single note returns, alone, dry
  229-249 s   (S23-S24) that note is cut at the moment of contact and does not
                        return; the piece ends on a cut, not a fade, and not on
                        a resolved chord

SYNC RULE: every scene boundary after 9,0 s falls on a bar line. Do not place
any hit point, swell or accent on any scene boundary; the music must never
appear to know what the picture is doing.

MIX: mono compatible — all low end centred, no wide stereo that collapses on a
phone speaker. Target −14 LUFS integrated, true peak −1,0 dBTP. The music bed
sits at −16 to −18 LUFS under the sound design.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO orchestral swell, NO percussion hit on any cut.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REPLİK SAYISI:  0
REGISTER:       — (replik yok; register haritası GEREKMEZ)
SES DURUMU:     STATE B — sessiz, TASARIMLI. ⛔ Ses kanalı VAR ve DOLUDUR;
                "AUDIO ABSENT" ile karıştırılmaz [D136 · THE ROSE COAT vakası].
                Teslimden önce doğrulanır:
                ffprobe -v error -select_streams a -show_entries stream=codec_type \
                  -of csv=p=0 "$M"     → çıktı boşsa 🔴 TESLİM KUSURU
REPLİK ZAMANLARI: — (yok)
                ⛔ Replik olsaydı HESAPLANMAZ, HESAPLATILIRDI [D122]:
                  replik(S_n) = 9 + (n−1) × 10 + promptun TIMELINE ofseti

⭐ ORTAM YATAĞI — kurguya TEK PARÇA serilir [D83]:
   Z1 orman   S0-S9    alçak · yakın · damla + yaprak; kalın atmosferde
                       düşük frekanslar güçlü taşınır
   Z2 kabin   S10-S13  gövde uğultusu + fan + iki nefes; dış orman sesi
                       kapak kapanınca (S12) tamamen kesilir
   Z3 tırmanış S14-S21 boğuk motor; S18'de PERDE DÜŞER (güç kaybı alet
                       tepkisiyle okunur) · S21'in son 1,5 s'sinde kesilir
   Z4 vakum   S22-S24  ⛔ DIŞ SES YOK; yalnız gövdeden iletilen uğultu,
                       kabin fanı ve iki nefes
   ⛔ Yatak KLİP SINIRINDA ÖLMEZ. Mutlak dijital sıfır bir HATADIR — COLD
     BURN'de 20 saniyelik sıfır çıktı ve D83 oradan yazıldı.
   ⛔ Kesmelerin ≥%60'ı J/L-cut; sert ses kesmesi EN ÇOK 3 ve planda yazılı:
     S12 (dış ses kesilir) · S21 sonu (motor kesilir) · S23 (temas knock'u).

⭐ İLK 2 SANİYE SES KARARI [HOOK §5]: TEK diegetik ses — kanopiden düşen tek
  bir damlanın kaska çarpması. ⛔ Müzik 0:00'da GİRMEZ; akış içi videoların
  ~%85'i sessiz başlıyor ve ses-önce birincil taşıyıcı YAPILMAZ.

⭐ SES BIÇAĞI [SAVAS §7]: filmin en yüksek ses seviyesi DORUK DEĞİL, doruktan
  HEMEN ÖNCEDİR (S20). Doruk (S21) müziksizdir ve sonunda motor da susar.
```
