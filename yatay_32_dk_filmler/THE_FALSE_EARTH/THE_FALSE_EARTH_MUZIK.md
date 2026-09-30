# 🎶 THE_FALSE_EARTH — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR MAKİNENİN ÖZENİ olarak okumalı: yapı gördüğünü
    kusursuz kopyalıyor, görmediğini hiç kuramıyor — ve ikisini AYIRT EDEMİYOR.
    Müzik bu yüzden TEHDİT değil, DİKKAT çalar."

TEMPO:        72 BPM — sahne ızgarasına HİZALI [§14]
              72 BPM 4/4 → vuruş 0,8333 s · ölçü 3,3333 s
              10 s klip = tam 12 vuruş = tam 3 ÖLÇÜ ⇒ HER KLİP SINIRI bir ölçü
              çizgisine düşer, 192 klipte kayma 0. ⭐ Bu yüzden 72 seçildi:
              menüdeki 48/96/120/144 de tutuyor ama 72 bu filmin nefes kadansı
              (dört kısa → üç → iki) ile aynı hızda.
SÜRE:         1920 s = 192 klip × 10 s = 576 ölçü. ⛔ Formülle: (klip−1)×10+10.
MÜZİKSİZ SAHNE: S37 (K140-K144 · 1390-1440 s) ve S47 (K181-K183 · 1800-1830 s)
              — ⛔ §10 en az bir tane ister, bu filmde İKİ tane var ve ikisi de
              GEREKÇELİ: S37 filmin tek tam sessizliğini taşır, S47 ise bir
              YOKLUĞU (amber ışığın olmayışı) taşır; müzik ikisini de doldurur.
              ⭐⭐ HARD MUTE: 1420-1430 s (K143). Bu on saniyede MÜZİK DE, ses
              yatağı DA kesiktir; yalnız kask içi nefes kalır. ⛔ Sessizlik
              MODELDEN İSTENMEZ, burada ve kurgu bıçağıyla yapılır [⚠️4 · D180].
SUB-BASS:     40 Hz temel + 110 Hz oktav eşlikçisi [§15.1]
              ⛔ Telefon hoparlörü 40 Hz'i HİÇ çalmaz; eşlikçi olmadan o katman
              izleyicinin yarısında YOK demektir. 110 Hz her klipte 40 Hz ile
              birlikte girer ve birlikte çıkar.
VURUŞ NOKTASI: 4 tane — hepsi klip sınırında, yani ölçü çizgisinde:
               ①  700 s  K070 sonu   novum okunur (camdaki iz + fotoğraftaki flaş)
               ② 1640 s  K164 sonu   merkezî seçim söylendi
               ③ 1730 s  K173 sonu   üçüncü amber ışık söndü
               ④ 1920 s  K192 sonu   karanlıkta bir ışık daha yandı
               ⛔ Beşincisi YAZILMAZ. Az olan güçlüdür [§14]. Doruğun (S44)
               kendi vuruşu YOKTUR: 1680-1740 s'de müzik ÇEKİLİR, ödemeyi
               gövde ve metal taşır.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow · Music
GENRE: minimal ambient score for hard science fiction; sustained strings and
processed metal, no percussion kit
TEMPO: 72 BPM, 4/4, strict — every bar line falls on a 3,3333 s boundary

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. sustained low strings, bowed, no vibrato — one held note, moving by a
     semitone at most once per minute
  2. a 40 Hz sine bed with a 110 Hz octave companion always sounding with it
  3. struck metal, dry and unreverberated, single strikes only — the same
     material the ship is made of, never a cymbal and never a gong
  4. one high sine tone, thin and steady, entering only where a copy is shown

DYNAMIC SPREAD — sahne ızgarasıyla birebir (8 PART × 240 s):
     0- 240 s (P1 · S01-S07): layer 1 alone, very quiet, one held note.
                              Layer 2 enters at 100 s and stays.
   240- 480 s (P2 · S08-S13): layer 4 enters at 300 s — the first copied thing.
                              Layer 1 moves one semitone down at 420 s.
   480- 720 s (P3 · S14-S19): layer 3 enters at 560 s, one strike per 20 s.
                              ⭐ HIT ① at 700 s: layers 1-2-4 stop dead for
                              1,5 s, then layer 4 alone returns, a fifth higher.
   720- 960 s (P4 · S20-S25): all four layers, the quietest they are in the film
                              after the hit; layer 3 goes to one strike per 40 s.
   960-1200 s (P5 · S26-S31): layer 1 rises a semitone at 1000 s and again at
                              1150 s, the only place it moves twice.
  1200-1440 s (P6 · S32-S37): layer 2 doubles in length, layer 3 stops entirely.
                              ⛔ 1390-1440 s (S37): ALL LAYERS OUT.
                              ⛔ 1420-1430 s (K143): HARD MUTE, digital silence
                              on the music stem, breath stem only.
  1440-1680 s (P7 · S38-S43): layers 1-2 return at 1440 s at half the level they
                              had at 1390 s. Layer 3 returns at 1600 s.
                              ⭐ HIT ② at 1640 s: one metal strike, then layer 1
                              alone for 20 s.
  1680-1920 s (P8 · S44-S50): 1680-1740 s (S44): layer 1 ONLY, falling away —
                              ⛔ the climax carries no music above the held note.
                              ⭐ HIT ③ at 1730 s: layer 2 drops out mid-bar and
                              does not return until 1830 s.
                              ⛔ 1800-1830 s (S47): ALL LAYERS OUT.
                              1830-1910 s: layers 1-2-4, layer 4 for the last time.
                              ⭐ HIT ④ at 1920 s: layer 4 alone holds through the
                              final frame and is cut, not faded.

SYNC RULE: every layer change, entry, exit and strike lands on a bar line —
that is, on a multiple of 3,3333 s — and every one listed above is also a clip
boundary (a multiple of 10 s). No layer ever crosses a scene boundary while
changing level.

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
REGISTER:     diegetik yapay ses — ÜÇ KANAL, hiçbiri anlatıcı değil:
              ① ECHO · kask içi makine sesi (düz, yakın, filtresiz) — 20 replik
              ② TELSİZ · kask telsizi (dar bant-pass, uzak) — Lena + anne
              ③ KAYIT · oynatılan arşiv (ince, kusurlu, düşen) — 6 klip
              + Mira'nın KENDİ sesi: yakın ve filtresiz, yalnız ağzı kadrajda
                okunduğunda ya da kadraj dışından (9 replik)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s ·
              dijital sıfır 0 kare (⛔ İSTİSNA: K143 HARD MUTE, kasıtlı) ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass
              [D216 · 14.09.2026]
              ⭐ ÖLÇÜLDÜ: 50 sahnenin en yükseği 4 katman (S48 · S49) — tavan AŞILMIYOR.
              Katman sayımı = ses yatağı + yatağın altındaki ikinci öğe + replik
              kanalı + müzik. Müziksiz iki sahnede müzik katmanı düşüyor.
REPLİK SAYISI: 47  (HUMAN 23 · MACHINE 20 · karışık 4)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(K_n) = (n − 1) × 10 s + promptun TIMELINE ofseti
   ⭐ 24.09.2026 · BETİKLE DOĞRULANDI: 47/47 replik bu formülle tutuyor,
   ızgara dışına düşen 0. Elle yazılan her kayıt er geç ızgara formülüyle
   çelişir ve ⑨ HİZALAMA KAPISI'nın ölçü aletini bozar.
   Kaynak tablo: `00_ANALIZ/03_SAHNE_SIRALAMASI.md` replik yerleşimi.
```

### 🧮 KATMAN TABLOSU — 50 sahne · ③ SES LAYER COUNT bunu ölçer

| sahne | klip | s | ses yatağı (sahne kilidinin AUDIO ilk cümlesi) | replik | müzik | katman |
|---|---|---|---|---|:--:|:--:|
| S01 | K001-K002 | 0-20 | the low hum of the ship's hull, conducted through her boots | K002@16.0s | var | **3** |
| S02 | K003-K004 | 20-40 | the tick of the scanner arm stepping across its track | K004@37.0s | var | **3** |
| S03 | K005-K008 | 40-80 | a steady console tone under everything | K005@43.0s · K006@55.0s | var | **3** |
| S04 | K009-K012 | 80-120 | the ring's low resonance under everything | K012@115.0s | var | **3** |
| S05 | K013-K015 | 120-150 | the thump of the separation thrusters, with a steady pressure hiss under it | K015@144.0s | var | **4** |
| S06 | K016-K019 | 150-190 | the flat slap of the water's own echo under the thrusters | K018@176.0s · K019@187.0s | var | **3** |
| S07 | K020-K024 | 190-240 | the thrusters gone dull inside the fog, a woman's call thin over them | K023@223.0s | var | **3** |
| S08 | K025-K027 | 240-270 | her boots on wet stone, and water dripping somewhere out of frame | — | var | **2** |
| S09 | K028-K031 | 270-310 | a faint ring in the shop glass, and the flat empty tone of the hand tool | K031@307.5s | var | **3** |
| S10 | K032-K036 | 310-360 | her breathing inside the helmet, and her boots on stone | — | var | **2** |
| S11 | K037-K040 | 360-400 | the room's own tone, with a faint buzz in the lamp | K040@394.0s | var | **4** |
| S12 | K041-K044 | 400-440 | the room's own tone, with the scanner's steady note under it | K043@425.0s | var | **4** |
| S13 | K045-K048 | 440-480 | the room's own tone, with a faint buzz in the lamp | K045@444.0s · K046@457.0s | var | **4** |
| S14 | K049-K052 | 480-520 | the room's own tone, with the forearm screen's low note and the bag's fabric under it | K051@505.0s | var | **4** |
| S15 | K053-K056 | 520-560 | the room's own tone, with radio traffic and a distant engine under it | K053@523.0s | var | **4** |
| S16 | K057-K060 | 560-600 | the room's own tone, with two people breathing in it | — | var | **3** |
| S17 | K061-K064 | 600-640 | the room's own tone, with a fine tick coming from inside the wall | — | var | **3** |
| S18 | K065-K068 | 640-680 | the room's own tone, and nothing under it at all | K065@643.0s · K066@655.5s · K067@668.0s | var | **3** |
| S19 | K069-K072 | 680-720 | the room's own tone, with the lamp's buzz and an open radio channel under it | K071@707.0s · K072@712.0s | var | **4** |
| S20 | K073-K075 | 720-750 | the room's own tone, with metal groaning somewhere inside the wall | K074@736.0s | var | **4** |
| S21 | K076-K079 | 750-790 | a hinge snapping somewhere behind the wall, and a room-sized echo after it | — | var | **2** |
| S22 | K080-K084 | 790-840 | a line under tension, with metal turning somewhere below | K080@792.0s · K083@826.5s | var | **4** |
| S23 | K085-K088 | 840-880 | the module's low tone, with cut fragments of old recordings under it | K088@876.0s | var | **4** |
| S24 | K089-K092 | 880-920 | a recording breaking up, with an alarm under it | — | var | **3** |
| S25 | K093-K096 | 920-960 | the module's low tone, with a distant engine under it | K094@933.0s · K095@942.0s | var | **4** |
| S26 | K097-K100 | 960-1000 | structural strain conducted through the plating, with a command channel cutting out under it | K099@986.0s | var | **4** |
| S27 | K101-K104 | 1000-1040 | two people breathing, with an open door standing between them | K101@1003.0s · K103@1025.0s | var | **4** |
| S28 | K105-K108 | 1040-1080 | her boots running on wet stone, with stone moving on stone somewhere out of frame | K108@1076.0s | var | **4** |
| S29 | K109-K113 | 1080-1130 | her gloves and boots working on a dry matt surface, with her breathing loud inside the helmet | — | var | **3** |
| S30 | K114-K117 | 1130-1170 | a recorded voice carried out of the windows, unbroken and without a single join in it | K114@1133.0s | var | **3** |
| S31 | K118-K120 | 1170-1200 | close mechanical systems running, with nothing at all coming from the city | — | var | **3** |
| S32 | K121-K124 | 1200-1240 | structural separation conducted through the frame, with a thruster pulse under it | — | var | **3** |
| S33 | K125-K129 | 1240-1290 | a low-frequency structural note conducted through the frame, with nothing above it | — | var | **3** |
| S34 | K130-K132 | 1290-1320 | close passes conducted through the frame, with an open machine channel under them | K131@1305.0s | var | **4** |
| S35 | K133-K135 | 1320-1350 | an alignment tone, with clamp and pressure noise under it | — | var | **3** |
| S36 | K136-K139 | 1350-1390 | the ship's fan bed under everything, with dry contact from the walls | K139@1384.0s | var | **4** |
| S37 | K140-K144 | 1390-1440 | her breathing inside the helmet, with the ship's fan bed under it | — | ⛔ YOK | **2** |
| S38 | K145-K148 | 1440-1480 | structural strain conducted through the plating, with a thruster's dry pulse under it | — | var | **3** |
| S39 | K149-K152 | 1480-1520 | a hairline crack working in the shell, with an amber resonance under it | — | var | **3** |
| S40 | K153-K156 | 1520-1560 | the clamp's dry ratchet in the housing, with an amber resonance under it | K155@1546.0s | var | **4** |
| S41 | K157-K160 | 1560-1600 | two voices on the helmet radio, with her breathing under them | K158@1574.0s · K159@1586.5s | var | **4** |
| S42 | K161-K164 | 1600-1640 | an open radio channel in the helmet, with an amber resonance under it | K162@1614.0s · K163@1625.0s · K164@1634.0s | var | **4** |
| S43 | K165-K168 | 1640-1680 | dry mechanical seating in the housing, with one long breath under it | K166@1656.0s | var | **4** |
| S44 | K169-K174 | 1680-1740 | the bay's own noise under everything, with the vacuum silent beyond the glass | — | var | **3** |
| S45 | K175-K177 | 1740-1770 | dry cracking along the corridor walls, with nothing running under it | K177@1767.0s | var | **4** |
| S46 | K178-K180 | 1770-1800 | structural vibration conducted through the plating, with nothing carrying beyond it | K178@1774.0s | var | **4** |
| S47 | K181-K183 | 1800-1830 | a steady life-support tone under everything, with nothing else running | K183@1825.0s | ⛔ YOK | **3** |
| S48 | K184-K187 | 1830-1870 | a steady life-support tone under everything, with a repaired recording thin and flawed over it | K185@1844.0s | var | **4** |
| S49 | K188-K189 | 1870-1890 | a steady life-support tone under everything, with a beacon's slow beep over it | K188@1873.0s · K189@1885.0s | var | **4** |
| S50 | K190-K192 | 1890-1920 | her breathing inside the helmet, with a steady life-support tone under it | — | var | **3** |
```
⭐ TABLO ELLE YAZILMADI — bölüm dosyalarının AUDIO satırlarından ve
  `03_SAHNE_SIRALAMASI` replik tablosundan betikle üretildi (24.09.2026).
  Sahne kilidi değişirse tablo YENİDEN üretilir, düzeltilmez [㉜⑥].
⛔ Sahne içindeki kliplerin AUDIO satırı ilk cümlede BİREBİR aynıdır; tablodaki
  "ses yatağı" sütunu o cümledir. Klipten klibe değişen şey yatağın ÜSTÜNE
  binen olaydır (replik · tek darbe · kesilme) ve o promptta yazılı.
⚠️ K143 satırı (S37) tabloda "⛔ YOK" görünüyor ve bu DOĞRUDUR: o sahnede
  müzik katmanı yok, K143'te ses yatağı da yok. Tek kalan nefes stem'idir.
```

## ⬜ ÜRETİM DURUMU

```
⬜ MÜZİK ÜRETİLMEDİ — bu dosya promptu ve ızgarayı taşır, tek saniye ses yok.
⬜ Flow · Music aracının TEMPO alanı fiilen sınanmadı; 72 BPM'in çıktıda
   tutup tutmadığı ilk denemede ölçülür ve üretim defterine yazılır [D142 kalıbı].
⬜ HARD MUTE'un kurguda uygulanması: 1420-1430 s müzik stem'inde dijital sıfır.
   Makine kapısı `THE_FALSE_EARTH_QA_SPEC.md` 🅴 E BLOĞU KAPI 1 (freezedetect)
   görüntüyü ölçer; SESİN sessizliği ③ SES merceğinde elle doğrulanır.
⛔ SAHİP KARARI: 72 BPM mi 96 BPM mi? İkisi de ızgarayı tutuyor (96 BPM → 10 s =
   16 vuruş = 4 ölçü). 72 seçildi çünkü nefes kadansıyla aynı hızda; 96 filmi
   daha tedirgin yapar. Karar müzik üretilmeden önce verilebilir.
```
