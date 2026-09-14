# 🎶 THE UPWARD FALL — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILIR — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u BİR TEHDİT DEĞİL, BİR DÜZEN olarak okumalı —
    ormanın ölüsünü yukarı taşıyan sessiz, işleyen, kişisel olmayan bir
    döngü. Müzik ne uyarır ne kutlar; ÇALIŞAN bir şeyin altını çizer."

TEMPO:        72 BPM — sahne uzunluğuna HİZALI (§14): 10 s sahne = 12 vuruş
              = tam 3 ölçü (4/4). Her sahne sınırı bir ölçü çizgisine düşer.
              Hook 9 s = 10,8 vuruş → hook TEK BAŞINA ölçüsüzdür ve S1'in
              ilk ölçü çizgisi 0:09'dadır (müziğin gerçek girişi).
SÜRE:         249 s = hook 9 s + 24 × 10 s
MÜZİKSİZ SAHNE: S21 (3:29-3:39) — ⛔ her filmde EN AZ BİR tane (§10).
              Uzuv indiğinde müzik TAMAMEN kesilir; yalnız iki hızlı nefes
              ve iki alçak sürtünme kalır. Sessizlik bir eksiklik değil,
              filmin en yüksek gerilim aracıdır ve bu karar PLANLIDIR.
              İkincil müziksiz bant: S0'ın ilk 2 saniyesi (hook sesi —
              diegetik tek nefes; erken müzik girişi elendi).
SUB-BASS:     45 Hz temel + 90 / 135 / 180 Hz armonik eşlikçi (§15.1).
              MISSING FUNDAMENTAL: telefon sürücüsü 150 Hz altını fiziksel
              olarak üretmiyor; 45 Hz katmanı tek başına telefonda YOK
              hükmündedir. Üst armonikler yoğun yazılır, beyin temeli
              "duyduğunu" varsayar.
VURUŞ NOKTASI: 4 tane (az olan güçlüdür)
              ① 0:69  S7 — kırk parça kalkar (ilk gerçek dinamik açılım)
              ② 1:59  S12 — 18 m'lik dal geçer (alt katman ilk kez 45 Hz'e iner)
              ③ 3:09  S19 — bağ kopar (bütün katmanlar tek vuruşta düşer)
              ④ 3:39  S22 — beşinci kesik (tek sürekli ton girer ve kalır)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno (v4 · instrumental)
GENRE: minimal orchestral drone / textural ambient, no percussion
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low sustained cello drone, bowed slowly, no vibrato — enters 0:09
  2. A single high sine tone, very quiet, one pitch, never moving —
     enters 0:19 and stays for the whole film
  3. Bowed double bass at 45 Hz with its own upper harmonics at 90, 135
     and 180 Hz played by cellos in unison — enters 1:59
  4. A soft breathy wooden flute layer, single long notes, no melody —
     enters 2:59 and only appears three times
  5. One low sustained tone alone — enters 3:39 and never resolves

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  0-9 s      (S0): silence, then nothing but room tone
  9-29 s     (S1-S2): cello drone alone, very low, rising slowly
  29-69 s    (S3-S5): drone plus the high sine tone; no movement
  69-79 s    (S7): the drone opens into a fifth and holds — the film's
                   first real widening
  79-119 s   (S8-S11): back to the drone; the sine tone thins
  119-129 s  (S12): the 45 Hz bass enters underneath with its harmonics
  129-179 s  (S13-S16): bass and drone hold, everything else drops out
  179-189 s  (S18): flute layer, one long note
  189-199 s  (S19): every layer drops together on one beat, leaving the
                   sine tone alone for four seconds
  199-209 s  (S20): bass returns alone, very quiet
  209-219 s  (S21): TOTAL SILENCE — no music of any kind
  219-229 s  (S22): a single low sustained tone enters at 6.0s into the cue
  229-249 s  (S23-S24): that tone plus the cello drone, unresolved; at the
                   very end it drops to one low layer and simply continues

SYNC RULE: every scene boundary lands on a bar line (72 BPM, 4/4, 10 s =
3 bars). No layer enters or leaves anywhere except on a bar line. The four
hit points are the only moments where two things change at once.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO percussion, NO braam, NO riser, NO
reversed cymbal, NO whoosh, NO final chord, NO resolution.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

> ⛔ **FİNAL ÇÖZÜLMEZ.** Loop satırı (§5③) bunu gerektiriyor: müzik son
> saniyede kadans yapmaz, alçak katmana iner ve 0:00'a akar. Kadanslı bir
> final "bitti" sinyalidir ve döngüyü öldürür.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:      — (bu filmde replik YOKTUR; register haritası boş)
REPLİK SAYISI: 0 · konuşan ağız 0 · dış ses 0 · kask AI 0 · telsiz 0
BEDENLEŞTİRME [§1a.1]: yok — bedensiz ses de yok. Karar bilinçlidir:
   filmin novum'u SESSİZ bir düzendir ve tek insan tek başınadır; bir
   telsiz muhatabı eklemek MUHATAP satırını (ortamın kalıcı değişen
   parçası) zayıflatırdı.
   ⛔ Bu, KART 7'nin kaldırılan "sessizlik en güvenlidir" damgasına
     dayanmıyor — o cümle 02.09.2026'da geri çekildi (kanıtı bir N/A idi).
     Gerekçe tasarımdır: 0 replik = 0 lip-sync riski + 0 AI-damgası
     kanalı [TUR 4 · T4.1/9-10], ve bu filmin bilgisi zaten NESNELERDE.
REPLİK ZAMANLARI: yok — hesaplanacak kayıt yok.
   Formül yine de SPEC'te durur [D122]:
   replik(S_n) = 9 s + (n−1) × 10 s + promptun TIMELINE ofseti
```

### 🎚️ DİEGETİK SES KATMANLARI — sahne dokusu takvimi

```
S0-S3    alçak geniş orman uğultusu (18-40 Hz zemin + 90 Hz üstü taşıyıcı)
         + kask içi tek nefes
S4-S8    yükselen dokuların ince KURU sürtünmesi; kayış gıcırtısı
S9-S13   uzak, alçak, ritmik gövde-içi akış; taş sürtünmesi
S14-S18  lif kopması · adım · boşluk yankısı (yarık açılınca alan genişler)
S19-S21  uğultu çekilir; S21'de MUTLAK SESSİZLİK + iki nefes
S22-S24  beş lif kopması · derin hava kayması · uğultunun geri dönüşü

⛔ KALIN ATMOSFER KURALI [KILAVUZ_REHBERI §3.4]: bu dünyada ses GÜÇLÜ,
   ALÇAK ve YAKINDIR — 3,2 atm düşük frekansları iyi taşır. Vakum
   sessizliği YOKTUR ve hiçbir sahnede "uzay sessizliği" yazılmaz.
⛔ TELEFON HOPARLÖRÜ [HOOK §5④]: hook sesinin taşıyıcısı 90 Hz üstündedir;
   ilk iki saniyenin nefesi ve uğultunun üst armonikleri o bandı doldurur.
```
