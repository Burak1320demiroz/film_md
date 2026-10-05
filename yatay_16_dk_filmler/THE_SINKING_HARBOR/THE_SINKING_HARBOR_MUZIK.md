# 🎶 THE_SINKING_HARBOR — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR FIRTINA SANDIĞI ŞEYİN KENDİNİ TUTTURMADIĞINI
    FARK ETMEK olarak okumalı."

TEMPO:        48 BPM — klip uzunluğuna HİZALI (§14: 10 s klip → 48 BPM'de
              ölçü 5,000 s; her klip sınırı TAM ikinci ölçü çizgisine düşer,
              her sahne sınırı (4 klip = 40 s) sekizinci ölçü çizgisine)
SÜRE:         960,000 s = filmin RUNTIME'ı (96 klip × 10,000 s)
              ⚠️ K01-K04 kesim kartıdır; müzik 0,000 s'den başlar, kart
              sınırları ölçü çizgilerine denk gelir (10/20/30/40 s)
MÜZİKSİZ SAHNE: HARD MUTE üç PENCERE — ⛔ her filmde EN AZ BİR tane (§10)
              ① K40 son 1,500 s  → 398,500-400,000 s  (novum doğrulaması)
              ② K79 tamamı       → 780,000-790,000 s  (nabız · en büyük cümle)
              ③ K96 tamamı       → 950,000-960,000 s  (final · açık avuç)
              ⭐ Üçü de NOVUM'un üç cümlesine denk gelir; tesadüf değil karar.
SUB-BASS:     34 Hz + 102 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              34 Hz'i hiç çalmaz; eşlikçi olmadan gezegen ritmi YOK demektir)
VURUŞ NOKTASI: 4 tane (az olan güçlüdür)
              V1  60,000 s  K07 → dört kenet hazır, yatak ilk kez gerilir
              V2 400,000 s  K41 → damar örüntüsü BELİRİR (ölçek şoku)
              V3 640,000 s  K65 → döşeme kopar, bağ yük alır
              V4 830,000 s  K84 → katman sondanın ucunu BIRAKIR ⭐ DORUK
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow · Music
GENRE: slow orchestral drone, chamber strings and low brass, no percussion kit
TEMPO: 48 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. sustained double bass + contrabassoon unison, 34 Hz fundamental with its
     102 Hz octave always doubled (the planet's rhythm — never absent after 0 s)
  2. divisi cello and viola, slow bowed swells, no vibrato (the structure)
  3. one solo violin in its lowest register, entering only above 400 s (the entity)
  4. bowed metal / tuned steel plate, single strikes only (the mechanism)
  ⛔ TAVAN 4. Beşinci katman YAZILMAZ — ses yatağı zaten 4'e kadar dolu.

DYNAMIC SPREAD — klip ızgarasıyla birebir:
    0,000-120,000 s (S01-S03): layer 1 alone, pp, one swell per 40 s
  120,000-240,000 s (S04-S06): layer 2 enters at 160 s, p, swells every 20 s
  240,000-400,000 s (S07-S10): layers 1-2, broken into short uneven pulses;
                               at 398,500 s ALL LAYERS CUT (hard mute ①)
  400,000-480,000 s (S11-S12): layer 3 enters at 400 s on V2, mp, sustained
  480,000-600,000 s (S13-S15): layers 1-3, one step up at 560 s
  600,000-720,000 s (S16-S18): layer 4 enters at 640 s on V3, single strikes
                               only, never a pattern; mf
  720,000-780,000 s (S19):     layers 1-2-4, thinning
  780,000-790,000 s (K79):     SILENCE (hard mute ②)
  790,000-830,000 s (S20-S21): layer 1 returns alone at 790 s, builds to all
                               four at 830 s on V4 ⭐ film's only f
  830,000-950,000 s (S22-S24): all four, decaying one layer every 30 s
  950,000-960,000 s (K96):     SILENCE (hard mute ③)

SYNC RULE: every bar line falls on a 5,000 s boundary; every clip boundary
falls on a bar line; the four hit points fall on the FIRST beat of their bar.
⛔ No hit point is created by a new layer and a dynamic rise at the same time —
V2 and V4 are layer entries, V1 and V3 are dynamic only.

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
REGISTER:     diegetik — kask içi nefes · telsiz (band-pass) · yapı titreşimi.
              ⛔ Bu filmde suit AI YOK, anlatıcı YOK, kayıt sesi YOK: üç
              insanın sesi ve yapının sesi dışında konuşan hiçbir şey yok.
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare ·
              diyalog altında müzik/alarm −6 dB · kadraj dışı replik = telsiz band-pass [D216 · 14.09.2026]
KATMAN TABLOSU: ③ SES LAYER COUNT bunu ölçer

| sahne | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S01 | yapı uğultusu · motor · kask nefesi | 3 | oda tonu 0,3 s |
| S02 | kokpit uğultusu · kask nefesi · telsiz taşıyıcısı | 3 | 0,3 s |
| S03 | yuva metali · valf · kask nefesi · telsiz | 4 | 0,3 s |
| S04 | tavan lambası uğultusu · fan · iki kask nefesi | 4 | 0,2 s |
| S05 | tünel fanı · kriko · kask nefesi | 3 | 0,3 s |
| S06 | yuva metali · alan gerilmesi · kask nefesi | 3 | 0,3 s |
| S07 | alarm tonu · oda uğultusu · metal gerilmesi · üç nefes | 4 | 0,2 s |
| S08 | derin vuruş · panel teması · kask nefesi | 3 | 0,4 s |
| S09 | veri bağlantısı tınısı · taşıyıcı · derin vuruş | 3 | 0,4 s |
| S10 | makine uğultusu (kısık) · sürgü · derin vuruş | 3 | 0,4 s |
| S11 | geniş kabarma · oda uğultusu · kask nefesi | 3 | 0,3 s |
| S12 | yavaş ritim · çok kısık uğultu · üç nefes | 3 | 0,3 s |
| S13 | iç fanlar · tutamak temasları · bot · iki nefes | 4 | 0,2 s |
| S14 | valfler · giysi kumaşı · telsiz taşıyıcısı · üç nefes | 4 | 0,2 s |
| S15 | yapı titreşimi · kask nefesi · kilit mekanizması | 3 | 0,3 s |
| S16 | yapı titreşimi (artmış) · kırpılmış telsiz · iki nefes | 3 | 0,2 s |
| S17 | yapısal kırılma · bağın yük sesi · iki hızlı nefes | 3 | 0,2 s |
| S18 | alçak ritim · ağır mekanik vuruş · kask nefesi | 3 | 0,3 s |
| S19 | yavaş krank · metal gerilmesi · kask nefesi | 3 | 0,3 s |
| S20 | gezegen ritmi · çok kısık makine · tek nefes | 3 | 0,4 s |
| S21 | ince metal boşalma · son ağır kilit · kask nefesi | 3 | 0,3 s |
| S22 | telsiz nefesi · kayar bağlantı · ray · iki nefes | 4 | 0,2 s |
| S23 | kapak · valf · dört açılma · iki nefes | 4 | 0,2 s |
| S24 | motor titreşimi · sakin uzak ritim · üç nefes | 3 | 0,4 s |
```
```
⛔ 24/24 sahne katman tavanının ALTINDA (en yüksek 4, altı sahnede).
⛔ Köprü 24/24 sahnede ≥ 0,2 s. ⚠️ Bölüm sınırlarında (K24|K25 · K48|K49 ·
   K72|K73) köprü 0,4 s'ye çıkar: §2.8 bu üç noktayı QA kör noktası sayıyor.

REPLİK SAYISI: 38 — 34'ü prompt bloklarında, 4'ü (H1-H4) kesim kartlarında
REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(Kn) = (n−1) × 10,000 s + promptun TIMELINE ofseti
   doğrulama: D19 (K48 · 8,0 s) = 478,000 s · D31 (K80 · 6,0 s) = 796,000 s
              D34 (K96 · 9,0 s) = 959,000 s
   ⚠️ D34 HARD MUTE ③'ün İÇİNDE (950-960 s): müzik yok, replik VAR. Bu
   bilinçli — filmin son cümlesi müziksiz duyulur.
   Elle yazılan her kayıt er geç ızgara formülüyle çelişir ve ⑨ HİZALAMA
   KAPISI'nın ölçü aletini bozar.
⬜ H1-H4'ün okuma süreleri ÜRETİMDE ffprobe ile ölçülür — tahmin YAZILMADI.
```
