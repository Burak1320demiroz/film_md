# 🎶 THE KEPT LIGHT — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ — müzik promptundan ÖNCE yazıldı:
   "İzleyici bu novum'u BİR KAYIP DEĞİL, BİR BİRİKİM olarak okumalı.
    Aşağıya inen şey kaybolmuyor; kalıyor. Müzik bu yüzden hiçbir yerde
    ağlamaz ve hiçbir yerde kurtarmaz — sadece SAYAR."

TEMPO:        72 BPM — 10 s = 12 vuruş = 4/4'te TAM 3 ÖLÇÜ.
              Her sahne sınırı bir ölçü çizgisine düşer [§14].
              Hook 9 s = 10,8 vuruş → hook kurguda 1,0 s baştan kırpıldığı
              için ilk ölçü çizgisi 0:09'da, S1'in başında oturur.
SÜRE:         249 s = 9 s hook + 24 × 10 s   (RUNTIME ile birebir)
MÜZİKSİZ SAHNE: S0 · S1 · S21   (kural EN AZ BİR tane ister [§10])
              · S0-S1: akış içi videoların ~%85'i sessiz başlar; görsel
                zemin tek başına ayakta durmak zorunda [HOOK §5].
              · S21: MUTLAK SESSİZLİK — aşağıdaki bıçak bloğu.
SUB-BASS:     38 Hz + 90-160 Hz oktav eşlikçisi [§15.1]
              ⛔ Eşlikçi olmadan telefon hoparlöründe o katman YOK demektir.
VURUŞ NOKTASI: 4 — az olan güçlüdür
              0:34  S3  KATALİZÖR — ilk kelepçe iner (tek düşük vuruş)
              2:09  S13 ORTA NOKTA — hat gerilir (tek yüksek tel girişi)
              3:09  S19 MERKEZÎ SEÇİM — kesici kapanır (tek alt oktav çekilir)
              3:59  S24 KAPANIŞ — lamba avuçtan çıkar (tek yumuşak yükseliş)
```

---

## ⛔ SESSİZLİK BIÇAĞI — KURGU İŞİ, ÜRETİM İŞİ DEĞİL [D180]

```
KURGUDA HARD MUTE: sn 209,0 – 219,0        (S21 · 10,0 s)

Gerekçe: bu on saniye filmin en pahalı on saniyesidir. Bedelin görüldüğü
kare buradadır (B2 kayıp sahnesi) ve orada duyulacak TEK şey, hiçbir şey
duyulmamasıdır.

⛔ VİDEO PROMPTUNUN "absolute silence" CÜMLESİ YEDEKTİR. Veo'nun yerel sesi
mutlak sessizlik teslim etmiyor — depoda iki film üst üste doruğunu bu
yüzden kaybetti (THE UPWARD FALL · THE HEALING GROUND, 04.09.2026).
Bıçak kurgudadır ve komutu şudur:

   ffmpeg -i master.mp4 -af "volume=enable='between(t,209,219)':volume=0" \
          -c:v copy -c:a aac -b:a 320k master_mute.mp4

⛔ ÖLÇÜM ÜÇ EŞİKTE KOŞAR (−50 dB YETMEZ) [D180 ③]:
   bash kilavuzlar_ve_sistem_dosyalari/.../olcum_kapisi.sh <master>
   python3 .../rapor_kontrol.py --olcum-sessizlik 209-219
   Aralık −50 / −40 / −30 dB'nin ÜÇÜNDE de kesintisiz değilse
   🔴 TESLİM KUSURU — master yeniden ihraç edilir.
⛔ Ölçüm ayrıca filmin SESSİZ DİBİNİ de raporlar (saniye + dB): "sessizlik
   yok" ile "sessizlik var ama beş saniye geç" farklı kusurlardır ve
   ikincisi kurguda bedava düzelir [D180 ④].
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow / Lyria
GENRE: minimal ambient score for science fiction; sparse, patient,
       non-orchestral; no theme statement, no melody that resolves
TEMPO: 72 BPM, 4/4, strict grid, no rubato, no accelerando

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. 38 Hz sine sub-pedal with a 90-160 Hz octave companion — one note,
     held, never changing pitch for the whole piece (enters 0:19)
  2. a single bowed double bass harmonic, one long note per bar, always on
     the bar line (enters 0:19, this is the CLOCK)
  3. dry felted piano, one note at a time, never a chord, always on beat 1
     (enters 0:59)
  4. a thin high string, one sustained note, no vibrato (enters 2:09 only)
  5. nothing else. No pad, no choir, no percussion of any kind.

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
    0-19 s   (S0-S1): SILENT — no music at all
   19-59 s   (S2-S5): sub-pedal + bass clock only, very quiet
   59-99 s   (S6-S9): piano enters, one note per bar, no louder
   99-129 s  (S10-S12): the piano stops for S10, returns for S11-S12
  129-159 s  (S13-S15): high string enters and holds; sub-pedal unchanged
  159-189 s  (S16-S18): everything thins — bass clock alone by 179 s
  189-209 s  (S19-S20): sub-pedal drops one octave and holds; nothing else
  209-219 s  (S21): SILENT — hard mute in the edit
  219-239 s  (S22-S23): bass clock returns alone, same tempo, same note
  239-249 s  (S24): piano returns with one rising figure, four notes, and
                    the sub-pedal comes back up its octave on the last note

SYNC RULE: every scene boundary is a bar line at 72 BPM. Nothing changes
inside a scene; every change happens ON a boundary. The four hit points
(34 s, 129 s, 189 s, 239 s) are the only moments where an instrument
enters or leaves in the same bar as a picture event.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO percussion, NO braam, NO riser,
NO reversed cymbal, NO whoosh, NO impact hit, NO heartbeat, NO ticking clock.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      — (bu filmde makine sesi de YOK; diegetik yapay ses 0)
REPLİK SAYISI: 0 · HUMAN 0 · MACHINE 0 · telsiz 0 · kayıt 0
REPLİK ZAMANLARI: madde BOŞ — replik yok, formül koşacak kayıt yok [D122].
                  (Formül yine de SPEC'te durur: replik(S_n) = 9 + (n−1)×10
                   + promptun TIMELINE ofseti.)

⛔ DİYALOG KARARININ GEREKÇESİ PLANDA YAZILI ve bir "en güvenli" iddiası
   DEĞİLDİR [KART 7'nin 02.09.2026 kaydı]. Üç sebep: kinetik bağımsızlık ·
   vakumda kadraj dışı insan sesi için ikinci bir insan gerekir ·
   filmin muhatabı bir insan değil, ortamın kalıcı değişen parçasıdır.
```

### 🎧 DIEGETİK SES YATAĞI — beş doku (kurgu sütunu)

```
① fan + klik      giysi fanının dar sabit yatağı + mühür halkasının kuru
                  klik'i          → S0 · S4 · S23 · S24
② ince fan        yalnız fan, temas yok (kadrajda dokunulan şey yok)
                  → S1 · S13 · S15 · S18 · S20
③ güverte teması  bot temasları, gövdeden iletilen, kuru ve kısa
                  → S2 · S5 · S9 · S11 · S14 · S22
④ kesici ısırığı  kesicinin çerçeveden iletilen sert kısa ısırığı
                  → S3 · S6 · S7 · S8 · S12 · S19
⑤ gövde iniltisi  kutunun bağlantılarından gelen uzun alçak gıcırtı
                  → S10 · S16 · S17
⑥ SESSİZLİK       → S21 (hard mute)

⛔ HAVADAN TAŞINAN SES 0 KARE. Bu üssün içi de vakumdur; duyulan her şey
   ya giysinin İÇİNDEN (fan, nefes) ya da TEMASTAN gelir [kart §3.1].
⛔ ARDIŞIK İKİ SAHNE AYNI DOKUDA OLAMAZ [KURGU_RITMI §2] — tek istisna
   S16↔S17 kümesidir ve orada doku bilerek sürer: küme bir kesme değil,
   bölünmüş TEK çekimdir.
```

### 🎚️ İHRAÇ KİLİTLERİ [KURGU_RITMI §6.2]

```
LOUDNESS:     −14 LUFS integrated · −1,0 dBTP  ⛔ ölçülür, tahmin edilmez
              (THE LEANING ROOM −32,0 LUFS teslim etti; 18 LU sapma)
SES KANALI:   var ve boş değil — teslimden önce ffprobe ile doğrulanır
KUYRUK KARTI: 0,0 s — jenerik, başlık kartı, kapanış kartı, filigran YOK
              [D70 · D72 — depoda 10 vaka]
SESSİZLİK:    209,0-219,0 s · üç eşikte ölçülür (yukarıdaki blok)
```
