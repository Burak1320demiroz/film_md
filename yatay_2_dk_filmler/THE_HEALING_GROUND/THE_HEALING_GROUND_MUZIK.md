# 🎶 THE HEALING GROUND — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR SALDIRI DEĞİL, BİR ONARIM olarak okumalı."

   Bu tek cümle bütün müzik kararlarını belirliyor: zemin kapanırken müzik
   gerilmez, YUMUŞAR. Tehdit kalıbı (alçalan yarım ton, artan yoğunluk,
   braam) filmin hiçbir yerinde yok. Örtünün her kapanışında müzik bir
   nota EKSİLİR — kapanma bir çözülmedir, bir tırmanma değil.

TEMPO:        48 BPM — sahne uzunluğuna HİZALI (§14): 4/4'te bir ölçü 5,0 s,
              iki ölçü 10,0 s. Her sahne sınırı bir ölçü çizgisine düşer;
              9 saniyelik hook tek başına 1,8 ölçüdür ve S1'in girişi
              bilinçli olarak ölçünün ORTASINDA başlar (tek sapma, aşağıda).
SÜRE:         139 s = filmin RUNTIME'ı (9 s hook + 13 × 10 s)
MÜZİKSİZ SAHNE: S0 · S2 · S9 · S12 — ⛔ her filmde EN AZ BİR tane (§10)
              S12 mutlak zorunlu: UZAYLI_VARLIK §8 "SESSİZLİK BIÇAĞI" —
              K4 tam formdan hemen önce 2 saniye mutlak sessizlik.
SUB-BASS:     42 Hz + 96 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü
              sub-bass'ı hiç çalmaz; eşlikçi olmadan o katman YOK demektir.
              ⛔ 18-19 Hz infrasound KULLANILMAZ [T7.4 ②]: telefonda ölü.)
VURUŞ NOKTASI: 2 tane —
              ① 109,0 s (S11 · 0,0 s): ısıtıcı kapanır → BÜTÜN alt uç
                 aynı karede düşer. Filmin tek sert müzik olayı.
              ② 137,0 s (S13 · 8,0 s): tek uzun alçak nota girer ve
                 filmin sonuna kadar tutar.
              (az olan güçlüdür — üçüncü bir vuruş noktası YOK)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow Music (alternatif: Suno v4, instrumental mode)
GENRE: minimal ambient score for science-fiction film; sustained strings and
       low bowed metal; no percussion of any kind
TEMPO: 48 BPM, 4/4, one bar = 5.0 seconds

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. bowed double bass, one sustained note, 42 Hz fundamental with its own
     96 Hz octave partner always present in the same phrase
  2. a single sustained cello line, no vibrato, entering and leaving on bar
     lines only
  3. a very quiet high string bed, one octave above the cello, used ONLY
     between 59 s and 99 s
  4. one bowed metal bowl, struck once and allowed to decay, used TWICE in
     the whole piece and never together with layer 3

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-9 s     (S0): silence. No music at all.
  9-19 s    (S1): layer 1 enters at 15 s under the wide shot, barely audible
  19-29 s   (S2): silence. Layer 1 drops out for the whole scene.
  29-39 s   (S3): layer 1 returns, one sustained note, no movement
  39-49 s   (S4): layer 1 only, very quiet; nothing new enters
  49-59 s   (S5): layer 1 + layer 2, cello enters on the bar line at 49 s
  59-69 s   (S6): layer 3 enters at 59 s — the only bright colour in the piece
  69-79 s   (S7): layers 1+2+3, the widest the score ever gets
  79-89 s   (S8): layers 1+2, layer 3 removed at 84 s and does not return
  89-99 s   (S9): silence from 89 s. Nothing under the cold rod scene.
  99-109 s  (S10): layer 1 alone returns at 99 s and holds one note
  109-119 s (S11): ⭐ HIT 1 — at 109.0 s everything below 200 Hz stops in one
                   frame with the vent plume. From 109 s to 119 s the piece
                   is a single unaccompanied cello note fading out.
  119-129 s (S12): silence, complete, for the whole scene
  129-139 s (S13): ⭐ HIT 2 — at 137.0 s layer 1 returns alone, one long low
                   note, and holds through the final frame without resolving

SYNC RULE: every entry and every exit lands exactly on a bar line (multiples
of 5.0 s from 9.0 s). The only deliberate exception is the very first entry
at 15.0 s, which lands mid-bar because the 9-second hook is not a whole
number of bars — this is written here so the edit does not "correct" it.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO tension cluster, NO descending semitone motif.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      HUMAN × 4 · MACHINE × 0.
               ⚠️ Bu seri normalde diegetik YAPAY ses kullanır (suit AI ·
               telsiz). Bu film onu kullanMIYOR ve gerekçesi yazılı: kayıt
               bir MAKİNENİN sesi değil, adamın kendi sesidir ve muhatabı
               gelecekteki bir insandır. Sayı söyleyen replik olmadığı için
               D82'nin "sayı MACHINE'dedir" kuralı tetiklenmiyor.
REPLİK SAYISI: 4
REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = hook + (n−1) × klip + promptun TIMELINE ofseti
   hook = 9,0 s · klip = 10,0 s

   R1  S4  → 9 + 3×10 + 2,0  = 41,0 s   "The last one's gone under. Same as
                                          the others."
   R2  S7  → 9 + 6×10 + 3,0  = 72,0 s   "Whoever walks this line next —
                                          start from this end."
   R3  S11 → 9 + 10×10 + 4,5 = 113,5 s  "It'll hold once it's cold."
   R4  S13 → 9 + 12×10 + 6,0 = 135,0 s  "Mark's set. Line's closed."

   ✅ Dört kayıt da formülle doğrulandı; sapma yok.
```

### 🌬️ ORTAM YATAĞI — dört doku, sahne sahne

```
① AĞIR RÜZGÂR YATAĞI (geniş kadrajlarda: S1 · S5 · S7 · S11 · S13)
   0,90 bar yoğun soğuk hava: ses 199 m/s'de yürür. Alçak frekanslar GÜÇLÜ
   ve YAKIN taşınır, tizler anında ölür → yatak 60-300 Hz bandında yaşar,
   üstünde hiçbir şey yok. Hiçbir sahnede uğultu YÜKSELMEZ.
② YAKIN KABUK DOKUSU (makro kadrajlarda: S2 · S4 · S9 · S12)
   kuru kâğıt hışırtısı + ince buz kırılması; rüzgâr uzaklaşır.
③ GİYSİ VE NEFES (profil kadrajlarda: S3 · S10)
   kask içi nefes, kuru ve yakın; kumaş sürtünmesi. ⛔ Nefes hiçbir sahnede
   HIZLANMAZ — panik yasağı; yalnız S8'de iki nefeslik bir hızlanma var ve
   sonra yavaşlar (§2a.2: duygu adlandırılmaz, ritme yazılır).
④ VARLIK SESİ (UZAYLI_VARLIK §8 · yalnız S6 · S12)
   ⛔ SENTETİK KAYNAK YASAK: osilatör/theremin beyin tarafından "makine"
   okunur. Kaynak GERÇEK organik ses + manipülasyon:
     · S6  → perde kaydırılmış büyük bir memelinin nefesi, kumaş üstünde
             uzun kuru bir kayma sesiyle katmanlanmış
     · S12 → aynı nefesin tek bir ekshalasyonu, bir oktav aşağı, 2 saniyelik
             mutlak sessizliğin hemen ardından
   KOGNİTİF UYUMSUZLUK: nefes ritmi tanıdık insan izini taşır ama doku
   yabancıdır (Annihilation mekanizması). ⛔ Çığlık/acı yönünde
   KULLANILMAZ.

SESSİZLİK KARARI [§10]: filmde dört müziksiz sahne var ve biri (S12)
MUTLAK sessizlik taşıyor — rüzgâr dâhil her şey 5,5-7,5 s arasında kesilir.
Bu, filmin en pahalı iki saniyesidir ve kurgu kapısının KESİLEMEZ
listesindedir.
```

### 📉 SES KÖPRÜLERİ [§3 · KURGU_RITMI]

```
S6 → S7   varlığın kuru kayma sesi kesme boyunca 0,4 s taşar (görüntü tepeye
          çıkar, ses yerde kalır — izleyici onu hâlâ orada bilir)
S10 → S11 nefes köprüsü: S10'un son kısa nefesi S11'in ilk karesine sarkar
S11 → S12 ⛔ KÖPRÜ YOK, bilinçli: ısıtıcının sönmesiyle açılan boşluk
          kesmede de korunur. Boşluk bir hatadır gibi durmalı.
```
