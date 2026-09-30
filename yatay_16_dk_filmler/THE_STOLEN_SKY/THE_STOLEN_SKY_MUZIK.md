# 🎶 THE_STOLEN_SKY — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9 · `SES_VE_DIYALOG_URETIM_KILAVUZU.md` §5-§6 ·
`KURGU_RITMI_VE_IHRAC_KILAVUZU.md` §3 · karar kaynakları `00_ANALIZ/02_KONSEPT_VE_RISK.md` §10 · `00_ANALIZ/00_OKUMA_CIZELGESI.md` D180, D216

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u intikam veya zafer olarak değil, altmış saniyelik bir borç ve tahliye koridoru olarak okumalı: kule ele geçirilse bile gök kurtarılmaz, açılan koridor geri kapanır ve güç intikama değil başkalarının kaçışına harcanır."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s sahne = 12 vuruş = 4/4'te tam 3 ölçü; her sahne sınırı bir ölçü çizgisine düşer; 60 s koridor [S87-S92] = tam 18 ölçü tempo kilidi)
SÜRE:         960 s = filmin RUNTIME'ı (96 × 10 s · hook = S00 ızgaranın içinde · 23.040 kare @24 fps · kurgu kapısı 960,000 s ±0)
MÜZİKSİZ SAHNE: S00 · S01 · S02 (0-30 s · motor tırmanışı ve uzak namlu) · S59 · S60 · S61 (590-620 s · BEDEL / feda / C-0 / telsiz sessizliği) · S82 · S83 (820-840 s · karar öncesi sükûnet) · S94 (940-950 s · kabin 0 g sessizliği) · S95 (950-960 s · vakum, dış ses 0)
              ⛔ S61 ve S94 "müziksiz ≠ sessiz" [D83 · D180]: kabin fanı / telsiz statik / kask içi nefes kalır, HARD MUTE kurguda uygulanır, dijital sıfır 0 kare.
SUB-BASS:     41 Hz (E1) + 110 Hz / 164 Hz oktav ve beşli eşlikçisi (§15.1 — telefon hoparlörü sub-bass'ı çalmaz, missing fundamental serisiyle taşınır)
VURUŞ NOKTASI: 4 — ① 110 s (S11 başı): kule kararı / ilk bas vuruşu · ② 480 s (S48 başı): platform pusu ve ikinci yarı girişi · ③ 840 s (S84 başı): merkezî seçim («Koridoru aç») tek derin ton ve ana temanın yükselişi · ④ 870 s (S87 başı): koridorun açılışı / 60 saniyelik gerilim nabzı. S59 ve S94'te vurucu müzik YOKTUR; kayıp ve boş koltuk müzikle değil müziksizlikle taşınır.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (Lyria 3 Pro) — instrumental
GENRE: dark atmospheric industrial orchestral, relentless mechanical tension giving way to heavy moral debt and sparse awe
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. low sustained industrial drone on E, 41 Hz fundamental doubled at 110 Hz and 164 Hz, carrying a gritty mechanical hum (from 30 s)
  2. subdued metallic pulse, bowed iron texture, rhythmic three-note pulse on bar lines (from 110 s, S11 kule kararı)
  3. muffled heavy brass swells, low French horn/trombone chord pads, dark and strained, never heroic or triumphant (from 240 s, Part 2 dar uçuş yolu)
  4. bowed low string ostinato (cellos/contrabasses), accelerating friction without tempo increase, dry and close (from 480 s, Part 3 platform çatışması)
  5. high distorted harmonic string drone (violins sul ponticello), cold and sterile, reflecting the amber lattice (from 620 s, Part 4 kule içi)
  6. the Choice motif: low felt piano and solitary low cello phrase, four notes that descend and hold unresolved on the fourth note (enters at 840 s, S84)
  7. steady ticking pulse, marking the 60-second corridor countdown (from 870 s to 930 s, S87-S92)

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-30 s (S00-S02): SILENT — no music; raw engine climb, lattice deflection impacts, gate tone only
  30-110 s (S03-S10): Layer 1 enters softly at 30 s; steady low industrial drone under hangar and planning, no rise
  110-240 s (S11-S23): Layer 2 enters on bar line at 110 s (HIT ① «Kuleyi alacağız»); drone + restrained metallic pulse
  240-360 s (S24-S35): Layer 3 enters at 240 s (Part 2 flight in the trench); low brass pads add weight to the chase and K-1 damage
  360-480 s (S36-S47): Layers 1+2+3 sustain; tension thickens under the approach to tower T3, no heroic crescendo
  480-580 s (S48-S57): Layer 4 enters at 480 s (HIT ② Part 3 platform assault); bowed low string ostinato drives forward
  580-590 s (S58): Music thins down abruptly — Layer 4 drops out during Bor's «Git» order, leaving only a fading drone
  590-620 s (S59-S61): HARD MUTE — NO MUSIC (Bor falls, C-0 command, S61 radio silence and clenched fist; helmet breathing and room tone only)
  620-720 s (S62-S71): Layer 1 drone creeps back at 620 s, joined by faint high harmonic string (Layer 5) inside the reserve room
  720-820 s (S72-S81): Layers 1+2+5 hold; cold, calculating tension as Serrak adapts and Mara stands over the selector
  820-840 s (S82-S83): SILENT — NO MUSIC; Captain's radio call, silence holds as Mara's glove hovers over the T-handle
  840-870 s (S84-S86): HIT ③ at 840 s — Layer 6 enters: the four-note Choice motif on solo cello and low piano, deep and solemn, resolving revenge into duty
  870-930 s (S87-S92): HIT ④ at 870 s — Layer 7 enters: 60-second corridor countdown pulse (18 bars @ 72 BPM) alongside swelling brass and strings as E-1, E-2, and K-1 punch through the amber band
  930-940 s (S93): Corridor snaps shut; music cuts to a single sustained, unresolved high string harmonic ringing in vacuum
  940-950 s (S94): HARD MUTE — NO MUSIC (cabin interior, microgravity belt click over empty seat, only cabin hum and 3 breathing rhythms)
  950-960 s (S95): A final distant, unresolved low fundamental chord resonates faintly under the three disappearing points of light; cut at 958 s, last two seconds absolute silence before black

SYNC RULE: every change lands on a bar line (scene boundary, every 10 s = 3 bars @ 72 BPM); nothing lands inside a scene except the hits at their scene starts. No anticipatory swells; visual action leads, musical weight follows [CAM-WN kuralı].

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP. Müzik yatağı diyalogsuz sahnelerde −16…−18 LUFS; post-dub repliklerinin altında (S10, S11, S14, S53, S58, S67, S82, S84) ek −6 dB stem otomasyonu.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md` · `KURGU_VE_TESLIM_KILAVUZU.md` · `THE_STOLEN_SKY_QA_SPEC.md`

```
REGISTER:     HUMAN ×8 — hepsi AKUZMATİK (opak mat siyah vizör, ağız 0 kare; dudak senkronu riski fiziken sıfır);
              kadraj dışı ve telsiz replikleri (S10 · S53 · S82) telsiz band-pass filtresi (300–3400 Hz);
              kask içi replikler (S11 · S14 · S58 · S67 · S84) kask rezonansı ve nefes yatağı taşır; MACHINE ×0.
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU:
  | blok / sekans | sahne | ortam ve katmanlar (ad) | sayı | köprü |
  |---|---|---|:--:|---|
  | B1 (SEK01-03) | S00-S11 | motor tırmanışı · namlu çatlamaları · kask içi nefes · rüzgâr / hangar eko · (S10 telsiz · S11 kask içi) | 3-4 | oda tonu 0,3 s |
  | B2 (SEK04-06) | S12-S23 | patlama yankısı · kafes vızıltısı · kabin hum/fan · nefes · (S14 kask içi) | 3-4 | oda tonu 0,3 s |
  | B3 (SEK07-09) | S24-S35 | K-1 motor halkaları · hava sürtünmesi · hendek çatlamaları · sağ bilezik sürtünmesi · kabin hum | 3-4 | oda tonu 0,3 s |
  | B4 (SEK10-12) | S36-S47 | motor yükü · kalkan sapma çıtırtısı · istasyon mekanik yankısı · çift nefes · adım sesleri | 3-4 | oda tonu 0,3 s |
  | B5 (SEK13-15) | S48-S59 | kalkan sapması · darbe ışığı sesi · asansör ray gıcırtısı · zorlanmış nefes · (S53 telsiz · S58 kask içi) | 3-4 | oda tonu 0,3 s |
  | B6 (SEK16-18) | S60-S71 | C-0 alçak kavisli tonlar / rezerv odası tank hum · kask içi nefes · (S61 boş kanal statik · S67 kask içi) | 3 | oda tonu 0,4 s |
  | B7 (SEK19-21) | S72-S83 | çatı rüzgârı · kule jeneratör nabzı · kask içi çift nefes · telsiz hışırtısı · (S82 telsiz) | 3-4 | oda tonu 0,3 s |
  | B8 (SEK22-24) | S84-S95 | T-handle klik · 60 s koridor nabzı · 3 gemi itişi · kabin 0g hum / tek kemer kliği (S94) · vakum dış ses 0 (S93/S95) · (S84 kask içi) | 2-4 | oda tonu 0,2-0,4 s |
REPLİK SAYISI: 8 (post-dub · klipte 0 üretilir · SPEC A ve PLAN ile birebir)
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 0 + n × 10,000 + promptun TIMELINE ofseti
   S10 · 104,0 s · tahliye kaptanı (telsiz, band-pass) · "Kafes içinde sıçrama yok."
   S11 · 117,0 s · Mara (kask içi) · "Kuleyi alacağız."
   S14 · 145,0 s · Ada (kask içi) · "Yıkmak işe yaramaz."
   S53 · 533,0 s · Rey (telsiz, band-pass) · "Botu çatıya alıyorum."
   S58 · 583,5 s · Bor (kask içi, zorlanmış) · "Git."
   S67 · 674,0 s · Ada (kask içi) · "Bir kez. Sonra biter."
   S82 · 821,0 s · tahliye kaptanı (telsiz, band-pass) · "İki gemi hazır, seni bekliyoruz."
   S84 · 841,5 s · Mara (kask içi) · "Koridoru aç."
⛔ dijital sıfır 0 kare — sessizlik sahnelerinde (S00-S02, S59-S61, S82-S83, S94) nefes ve oda tonu yatağı kesilmez.
⛔ Diyalog altında müzik/alarm −6 dB; sekiz repliğin üçü (S10, S58, S82) zaten müziksiz veya incelmiş sahnededir.
⛔ AĞIZ HİÇBİR KAREDE GÖRÜNMÜYOR (opak vizör) → lip-sync riski FİZİKEN sıfır; bedenleştirme imkânsızdır ve doruk bütçesi serbest kalmıştır.
⛔ KLİP SÜRESİ AÇIK [D124 · K3]: 10 s bir varsayımdır. Ölçüm 10 s'den saparsa aşağıdaki sekiz saniye VE DYNAMIC SPREAD'in her satırı yeniden hesaplanır.
SESSİZLİK PENCERELERİ (makine kapısı SPEC E):
   0,0–30,0 s (S00-S02): açılış motor/namlu diegetik yatak · müzik 0
   590,0–620,0 s (S59-S61): Bor feda / C-0 / Mara telsiz sessizliği · müzik 0 (HARD MUTE) · nefes ve statik üstte
   820,0–840,0 s (S82-S83): kaptan çağrısı ve seçim öncesi bekleme · müzik 0
   940,0–950,0 s (S94): kabin içi mikrogravite sessizliği · müzik 0 (HARD MUTE) · kabin hum + tek kemer kliği
   958,0–960,0 s (S95 son 2 s): kararmaya geçiş · çözülmemiş akor sonu
```
