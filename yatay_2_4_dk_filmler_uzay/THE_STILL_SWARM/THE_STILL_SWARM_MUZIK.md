# 🎶 THE STILL SWARM — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9
**Durum:** ⬜ TASLAK (yazımla birlikte) → ⬜ FINAL (kurgudan sonra)

```
⛔ §17 KÜNYESİ ÖNCE YAZILDI — bu cümle yazılmadan müzik promptu yazılmaz:

NOVUM OKUMASI: "İzleyici bu duran alanı bir TEHDİT olarak değil, bir
               DİKKAT olarak okumalı — bir yerin sessizce dinliyor olması."

FİLM:         THE STILL SWARM · 140 s · 14 sahne × 10 s
MÜZİK-GÖRÜNTÜ İLİŞKİSİ: ⭐ ANEMPATİK
              Kılavuzun §18 karar tablosunda "bu seriye çok uygun, HİÇ
              KULLANILMADI" diye işaretli olan seçenek. Gerekçe yapısal:
              filmin novum'u tepkisizliktir. Müzik de olaylara tepki vermez —
              kelepçe durduğunda vurmaz, halat koptuğunda yükselmez, doruğa
              kreşendo yapmaz. Tek istisna S13'tür ve orada bile tepki değil
              ÇEKİLME olur (müzik biter, oda tonu kalır).
TEMPO:        72 BPM — 10 s sahne = 12 vuruş = TAM 3 ölçü (4/4). Her sahne
              sınırı bir ölçü çizgisine düşer [§14 tablosu].
SÜRE:         140 s = 10 s hook + 13 × 10 s
MÜZİKSİZ SAHNE: S10 (100-110 s) — "her şey kayboldu" yuvası [§10 + KARAKTER §5.3]
              ⛔ Müziksiz ≠ SESSİZ [D83]: giysi oda tonu ve kask içi nefes
                akmaya devam eder. Mutlak dijital sıfır 0,0 saniye.
              Müzik 99 s'de çekilir (1 saniye önce — sessizliğin fark
              edilmesi 1-2 saniye ister [YANASMA §2.1]) ve 110 s'de döner.
SUB-BASS:     45 Hz temel + 90 / 135 / 180 Hz oktav ve harmonik eşlikçileri
              [§15.1 ZORUNLU — telefon sürücüsü 150 Hz altını fiziksel olarak
              üretmez; eşlikçi olmadan o katman telefonda YOK hükmündedir]
VURUŞ NOKTASI: 2 — az olan güçlüdür
              ① 70 s (S7 başı) — orta nokta: ikinci katman girer
              ② 130 s (S13 başı) — alan hareket eder: alt uç bir tam ton düşer
              ⛔ Doruk (110 s) bir vuruş noktası DEĞİLDİR. Anempatik karar:
                filmin en yüksek anında müzik hiçbir şey yapmaz.
TONALİTE:     D doğal minör — çözülmez. Baskın akor hiçbir yerde toniğe
              gitmez; film boyunca askıda kalır.
ÇÖZÜLMEYEN CÜMLE: 20 s'de (S2) yarım kalan üç notalık figür → 130 s'de (S13)
              aynı figür bir kez daha başlar ve YİNE tamamlanmaz; bunun
              yerine 139 s'de kesilir.
KAPANIŞ:      fade out YOK · kadans YOK · 139 s'de kesme + 1 saniye oda tonu
              (sessizlik de loop'lanır [SENARYO_VE_VIRAL §5③])
FREKANS TABANI: sub 45 Hz + oktav eşlikçisi 90-180 Hz
LUFS HEDEFİ:  −14 nihai / −17 müzik yatağı
REVERB KARARI: ⛔ KURU — vakum. Hiçbir katmanda mekân yankısı yok; yalnız
              çok kısa (<80 ms) gövde rezonansı. Bu fizikle tutarlıdır ve
              seri imzası olabilir [§18].
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno v4 (instrumental)
GENRE: minimal ambient score for a silent science-fiction short; static,
       unresolving, dry
TEMPO: 72 BPM, strict, no rubato, no accelerando anywhere

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. 45 Hz sine sub with a strong 90 Hz and 135 Hz harmonic partner stacked
     directly above it (the sub must remain audible on a phone speaker)
  2. bowed double bass, single sustained D, no vibrato, bow noise kept
  3. detuned metal plate resonance, struck once every 4 bars, decaying dry
  4. high glass harmonic drone, D and A only, entering at 70 s
  5. low prepared piano, damped strings, three notes only, entering at 130 s

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-10 s (S0):    silence for the first 4 seconds, then layer 1 only, very low
  10-20 s (S1):   layer 2 joins, still under the breath
  20-30 s (S2):   three-note figure begins on layer 3 and stops unfinished
  30-60 s (S3-S5): layers 1-3, flat, no swell, no response to any event
  60-70 s (S6):   layer 3 drops out; only sub and bass, held
  70-100 s (S7-S9): layer 4 enters at 70 s and holds; no crescendo
  100-110 s (S10): ⛔ ALL MUSIC OUT. Room tone and breath only.
  110-130 s (S11-S12): layers 1 and 2 return at the same level as before —
                  the climax gets no swell, no hit, no crescendo
  130-139 s (S13): layer 5 enters; the sub drops one whole tone; the three-note
                  figure starts again and is cut off at 139 s
  139-140 s:      one full second of room tone, no music

SYNC RULE: the score never responds to an on-screen event. No hit lands on the
clamp stopping, on the line parting, or on the push. Bar lines fall on scene
boundaries only. Nothing resolves to the tonic at any point in the piece.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Dry throughout, no reverb tail longer than 80 ms.
Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO orchestral swell, NO ticking clock, NO heartbeat.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      — (bu filmde replik YOKTUR; HUMAN 0 · MACHINE 0)
REPLİK SAYISI: 0
REPLİK ZAMANLARI: tablo BOŞ — ve boş olması bir karardır, eksiklik değil.
   Formül yine de SPEC'te yazılıdır [D122]:
   replik(S_n) = 10 + (n−1) × 10 + promptun TIMELINE ofseti

YATAK ENVANTERİ [D83] — filmin sürekli ses zemini:
  ① kask içi nefes                  14/14 sahne, kesintisiz
  ② giysi oda tonu (fan + kumaş)    14/14 sahne, kesintisiz
  ③ gövdeden iletilen temas sesleri  olay bazlı: halat gerilmesi (S0·S8),
     eldiven-metal (S2), toka kliği (S4), valf tıslaması (S5), kanvas rasp
     (S6·S7·S10), gövde çınlaması (S12), yapı uğultusu (S13)
  ⛔ Vakumda DIŞARIDA ses yoktur. Duyulan her şey ya gövdeden iletilir ya
     kask içindedir. Bu ikisi aynı sahnede çelişmez [KARAKTER §4.2].

ORTAM KARTI KARŞILIĞI (§3.1 vakum): dış ses SIFIR · yalnız gövdeden iletilen ·
kuru miks, reverb yok.

KURGU TARAFI [KURGU_RITMI §3]:
  □ Ambiyans yatağı TEK PARÇA — 14 klibin tamamına serilir, klip sınırında
    ölmez, sıfırlanmaz, seviye sıçraması yapmaz. Kesinti 0.
  □ J-cut varsayılan: sonraki sahnenin gövde sesi 1,0-1,5 s önden girer.
    Hedef: kesmelerin ≥%60'ı ses köprülü.
  □ SERT KESME (ses ve görüntü aynı karede) tam 2 tane, ikisi de planlı:
    ① 60 s — S5'in valf tıslaması bitip S6'nın sessizliğine geçiş
    ② 100 s — S10'un başında müziğin tamamen çekilmesi
    ⛔ Tavan 3; bu film 2 kullanır.
  □ Beat-cutting yalnız kancada — doruk öncesi rampa YOKTUR (anempatik karar).
```
