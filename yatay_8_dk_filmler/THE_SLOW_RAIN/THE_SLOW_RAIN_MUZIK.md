# 🎶 THE_SLOW_RAIN — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u YAVAŞLAMIŞ BİR SAAT olarak okumalı — yağmur düşerken sayılıyor, ve her damla
    bir şeyi ağırlaştırıyor; müzik tik-tak vermez, damla verir."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14: 10 s sahne = 12 vuruş = 3 ölçü 4/4;
              her sahne sınırı bir ölçü çizgisine düşer)
SÜRE:         480 s = filmin RUNTIME'ı (48 × 10 s; hook S0 klibin içinde) — klip süresi araçtan ölçülünce yeniden hizalanır
MÜZİKSİZ SAHNE: S0 (ilk 10 s: tek diegetik ses) · S29 (bedel — kesici, kayış, sıvı; müzik 0) · S43 (doruk — oturma tıkırtısı tek başına) — ⛔ her filmde EN AZ BİR tane (§10)
SUB-BASS:     45 Hz sürekli pedal (yoğun soğuk havanın ağırlığı) + 90-135 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              sub-bass'ı hiç çalmaz, eşlikçi olmadan o katman yok demektir)
VURUŞ NOKTASI: 3 — 130,0 s (S13 çakılma, tek alçak vuruş) · 292,0 s (S29 kayış kesilir: müzik KESİLİR, 8 s boşluk, 300,0 s'de alçak katman geri) ·
              440,0 s (S44 gösterge yanar: ilk sıcak akor) — az olan güçlüdür
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow / Lyria (sahip aracı) — tek global tema, 480 s, sahne başına katman tablosu aşağıda
GENRE: slow ambient score, cold, weighty, near-static harmony; no rhythm section
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. sub pedal 45 Hz + 90-135 Hz oktav eşlikçisi (sürekli, S1'den S47'ye; S29-S30 ve S43'te sıfır)
  2. low bowed strings, one sustained minor chord that changes only at section marks (S1 · S14 · S29 · S35 · S44)
  3. sparse felt-piano single notes — one note per drop-landing beat in the picture, never a melody (S17 · S24 · S32 · S47)
  4. high thin glass harmonic, enters only S34-S36 (çekirdek sıcak) and S44-S47 (ısı geri geldi)

DYNAMIC SPREAD — sahne ızgarasıyla birebir (saniyeler klip 10 s VARSAYIMIYLA; araçtan ölçülünce yeniden yazılır):
  0-10 s (S0): NO MUSIC — damlanın eldivene 'tok'u ve tıslaması tek ses
  10-30 s (S1-S2): sub pedal + strings enter under the glide, −18 LUFS band, no swell
  30-50 s (S3-S4): iç mekân — strings only, thinner, pedal −6 dB (kırağı çıtırtısı önde)
  50-140 s (S5-S13): pedal + strings hold one chord; 130,0 s tek alçak vuruş (çakılma), sonra 4 s incelir
  140-230 s (S14-S22): felt-piano single notes on drop landings (S17 iki nota); strings unchanged
  230-290 s (S23-S28): pedal grows +3 dB over 60 s (kızak batışı), no new layer
  290-300 s (S29): MUSIC OUT — hard mute on 292,0 s (kayış kesilir); 8 s only cutter, strap, liquid
  300-340 s (S30-S33): pedal only, −21 LUFS, strings return at 320 s one octave lower
  340-360 s (S34-S35): glass harmonic enters over the puff (S34), holds through S35 (kabuk dökülür)
  360-430 s (S36-S42): strings + pedal, one chord change at 360 s; slope scenes no swell
  430-440 s (S43): NO MUSIC — oturma tıkırtısı tek başına
  440-480 s (S44-S47): first warm chord at 440,0 s (lamp), glass harmonic to the end; NO cadence at 480 s — pedal holds under the last drop

SYNC RULE: her sahne sınırı ölçü çizgisine oturur (72 BPM · 10 s = 3 ölçü); kesmeler vuruşta DEĞİL vuruş aralarında (KURGU_RITMI §4); beat-cutting yalnız S13 ve S44

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
REGISTER:     — replik yok (HUMAN 0 · MACHINE 0); diegetik yapay ses de yok — giysi sessiz, kask içi nefes tek insan sesi
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU (③ SES LAYER COUNT bunu ölçer) — tek AMBİYANS YATAĞI kurgunun tamamına serilir, klip sınırında ölmez:
  | sahne | katmanlar (ad) | sayı | köprü |
  | S0 | ambiyans (ağır alçak hava) · damla toku+tıslama | 2 | — (ilk sahne) |
  | S1-S2 | ambiyans · kanat membranı uğultusu · müzik pedal+strings | 4 | J-cut 1,0 s |
  | S3-S4 | iç yatak (kırağı çıtırtısı, nefes) · strings | 2 | L-cut 0,5 s (dış ambiyans sönerek) |
  | S5-S13 | ambiyans · damla tokları (uzak) · müzik · olay sesi (kayış/kapı/çakılma) | ≤4 | J-cut 1,0-1,5 s |
  | S14-S28 | ambiyans · sürtünme/sıvı · damla tokları · müzik | 4 | J-cut; S26-S28 küme içi köprü 0,2 s |
  | S29 | ambiyans · kesici+kayış · sıvı | 3 (müzik 0) | sert kesme 292,0 s (bilinçli, 1/3) |
  | S30-S42 | ambiyans · olay sesi · müzik (pedal/strings) · S34-S36 buhar tıslaması | ≤4 | J-cut |
  | S43 | iç yatak · oturma tıkırtısı | 2 (müzik 0) | sert kesme 430,0 s (bilinçli, 2/3) |
  | S44-S46 | iç yatak · hızlı şıpırtılar · müzik | 3 | J-cut 1,0 s |
  | S47 | ambiyans · damla toku · müzik (pedal, kadans yok) | 3 | sert kesme 470,0 s (bilinçli, 3/3) — son kare müzik çözülmez |
  sert kesme 3/3 · J/L-cut ≥%60 · dijital sıfır 0 kare · ambiyans kesintisi 0
REPLİK SAYISI: 0
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   Elle yazılan her kayıt er geç ızgara formülüyle çelişir ve ⑨ HİZALAMA
   KAPISI'nın ölçü aletini bozar.
```
