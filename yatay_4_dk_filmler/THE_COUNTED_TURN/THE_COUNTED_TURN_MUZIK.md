# 🎶 THE_COUNTED_TURN — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

## 📋 §17 KÜNYESİ — müzik promptundan ÖNCE

```
FİLM:                 THE_COUNTED_TURN · 249,0 s · 25 sahne (9 s + 24 × 10 s)
NOVUM OKUMASI:        "İzleyici bu kuralı KAYITSIZ BİR ÖLÇÜ olarak okumalı —
                      tehdit değil, ceza değil, yalnızca sayan bir şey."
                      ⛔ Bu cümle yazılmadan müzik promptu yazılmaz [§12]:
                        aynı kare, alçak gergin drone ile TEHDİT; yalnız çello
                        ile HÜZÜN; hareketsiz sakin nabızla HUŞU okunur.
MÜZİK-GÖRÜNTÜ İLİŞKİSİ: **ANEMPATİK** [§9] — bu seride hiç kullanılmadı ve bu
                      filme tam oturuyor: halka insanı umursamıyor. Anempatik
                      hâlimiz NEŞELİ müzik değil, DEĞİŞMEYEN müziktir: olay
                      büyürken müziğin tepki VERMEMESİ.
                      ⭐ §7.1 karşıt ruh hali: Overview'da (S13) müzik YÜKSELMEZ.
TEMPO:                72 BPM → 10 s sahne başına TAM 3 ÖLÇÜ [§14 tablosu]
                      ⛔ Hizasız BPM tekrarlanmıyor (DEAD APPROACH 130 BPM →
                        5,42 ölçü; REMEMBERING DUST 58 BPM → 2,42 ölçü).
                      ⚠️ HOOK 9 SANİYEDİR ve ızgara dışıdır: hizalama S1'den
                        (9,0 s) başlar. Hook, ölçü çizgisine oturmayan tek
                        bloktur ve bu bilinçlidir — sayım orada henüz başlamamıştır.
TONALİTE:             tek merkez, minör renkli, ÇÖZÜLME 1 kez — S13 Overview'ın
                      sonunda ve orada da tam değil (askıda kalır)
SESSİZLİK SAHNESİ:    **S22** (219,0-229,0 s) — filmin doruğu
                      müzik S21 içinde **217,0 s**'de biter (sahneden 2 s önce)
                      ⛔ HARD MUTE 226,0-228,0 s: ortam yatağı DÂHİL her şey
                        kesilir. Bu, yatağın kurgu boyunca TEK kesildiği yerdir
                        ve bilinçli bir istisnadır [D83 · D180].
ÇÖZÜLMEYEN CÜMLE:     S23'te (229,0 s) TEK sürdürülen nota girer ve S24 boyunca
                      taşınır; ÇÖZÜLMEZ
KAPANIŞ:              fade out YOK · **KESME** · çözülmemiş nota
                      [UZAY_SENARYO §15: kapanış yok, held frame]
FREKANS TABANI:       sub 48 Hz + oktav eşlikçisi 96 Hz + armonik yığın
                      144 Hz ve 192 Hz [§15.1 + §15.1a Missing Fundamental]
                      ⛔ 150 Hz altındaki her şeyin TAMAMEN kaybolduğu
                        varsayımıyla yazılır; ağırlık 150 Hz üstünde durmalı.
                      ⛔ İnfrasound (17-19 Hz) KULLANILMAZ — teslim edilemez.
KATMANLAR:            4 katman (aşağıda, giriş sırasıyla)
LUFS HEDEFİ:          −14 nihai · −16…−18 müzik yatağı · true peak −1,0 dBTP
REVERB KARARI:        **KURU** — vakumda yankı yoktur. Tek yankı kaynağı YAPININ
                      KENDİSİDİR (halka bir çandır) ve o yankı müziğe değil
                      DİEGETİK temas seslerine aittir.
```

## 🎵 VURUŞ NOKTALARI — az olan güçlüdür

| # | saniye | sahne | olay | müzikte ne olur |
|:--:|:--:|:--:|---|---|
| 1 | 11,0 | S1 | yapının ilk vuruşu · sayım başlar | nabız katmanı GİRER ve bir daha çıkmaz |
| 2 | 129,0 | S13 | Overview | hiçbir şey olmaz — ⭐ karşıt ruh hali: müzik YÜKSELMEZ, yalnız üst katman incelir |
| 3 | 199,0 | S20 | merkezî seçim | nabız katmanının PERİYODU kısalır (aynı ses, daha sık) |
| 4 | 217,0 | S21 | bedel ödendi | müzik BİTER |
| 5 | 229,0 | S23 | sayaç kapanır | TEK sürdürülen nota girer |

```
⛔ VURUŞ NOKTASI 5'i geçmiyor. Deponun kaydı: az olan güçlüdür.
⛔ HIT POINT AYARI KURGUDA yapılır [§14 ③]: müzik değil GÖRÜNTÜ kaydırılır
   (klip başında 2-6 karelik pay bırakılır). Müzik yeniden bestelenmez.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno / Lyria — one single continuous instrumental piece, 249 seconds.
GENRE: cold minimal cinematic drone with a slow mechanical pulse. No melody.
TEMPO: 72 BPM, strict, no rubato, no accelerando, no ritardando.

INSTRUMENTATION — layers in order of entry:
  1. a low sustained drone around 48 Hz, doubled by a quiet companion tone at
     96 Hz and reinforced with a dense harmonic stack at roughly 144 Hz and
     192 Hz, so the missing fundamental is implied rather than played; the
     perceived weight must survive full loss of everything below 150 Hz
  2. a dry mechanical pulse — one short damped metallic tick per bar, close,
     unreverberated, always the same tick, never varied
  3. a single sustained bowed cello note, high in its range, entering late and
     never resolving
  4. a thin granular metal texture, barely present, no rhythm of its own

DYNAMIC SPREAD — locked to the scene grid:
  0-9 s      (S0)        drone only, very low, no pulse
  9-19 s     (S1)        the pulse enters on the bar line at 11 s and stays
  19-119 s   (S2-S11)    drone and pulse only, absolutely unchanged, no build
  119-139 s  (S12-S13)   the upper texture thins out; the music does NOT rise
  139-199 s  (S14-S19)   unchanged again; the pulse never varies
  199-217 s  (S20-S21)   the pulse period shortens — same sound, more often
  217 s                  everything stops
  217-229 s  (S22)       silence
  229-249 s  (S23-S24)   one sustained cello note enters and carries to the end

SYNC RULE: every scene boundary falls exactly on a bar line, three bars per
scene, from 9 s onward. The 9-second opening block is deliberately outside the
grid. The piece is CUT at 249 s — no fade out, no final chord, no resolution.

MIX: mono compatible — all low end centred, no wide stereo that collapses on a
phone speaker. Completely dry: no reverb, no hall, no space. Target −14 LUFS
integrated, true peak −1.0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal,
NO whoosh, NO swell into the ending.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.
> ⭐ **Kanala özgü SES İMZASI** [SERI_VE_KANAL §3.0]: bu drone+tick çifti
> kanalın açılış ritüeli olarak ilk 1-2 saniyede tekrar kullanılır. YouTube
> 03/2026 ölçümü: <50k abonelik kanallarda orijinal ses bonusu var; trend ses
> kullanılmaz.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     — · bu filmde HİÇBİR register yok
REPLİK SAYISI: **0** (insan 0 · makine 0 · telsiz 0)
              ⛔ Bu bir SIFIR KİLİDİDİR [D156] ve QA_SPEC'te ayrı ölçüm satırı
                olur; sessizce varsayılmaz. Planın "sıfır" dediği her şey
                THE PAYLOAD'da ekrana gelmedi — sıfırı kimse ölçmüyordu.
REPLİK ZAMANLARI: yok. Formül yine de koşuyor ve SPEC'in bütün zaman kodlarını
              üretiyor: t(S_n) = 9 + (n−1) × 10 [D122].

ORTAM YATAĞI (diegetik · müzikten AYRI):
  · suit içi nefes + fan — kurgu boyunca TEK PARÇA serilir
    ⛔ Klip sınırında KESİLMEZ [D83 · THE COLD BURN'de 20 saniyelik dijital
      sıfır çıktı]. "Müziksiz sahne" SESSİZ sahne değildir.
  · yapının çanı — her temas milisaniyelerde halkayı dolaşıp çok yansımalı
    uzun bir kuyrukla döner (alüminyumda 5.100 m/s). Duyulan her şey TEMASTIR.
  · dış mekânda hava sesi 0 kare — vakum.

TEK İSTİSNA: 226,0-228,0 s HARD MUTE — yatak DÂHİL her şey kesilir.
  ⛔ Bu KURGUDA uygulanır, video modelinden İSTENMEZ [D180 · ⛔ ÇALIŞMIYOR,
    üç vaka]. QA_SPEC E bloğunda `silencedetect` ile ölçülür.

MİKS SIRASI: ortam yatağı −18 LUFS · müzik yatağı −16…−18 LUFS ·
             nihai miks −14 LUFS · true peak −1,0 dBTP
             ⛔ Sesi DÜŞÜK teslim etmek en pahalı hata: platform yüksek sesi
               kısar, düşük sesi YÜKSELTMEZ. (İki filmde ölçüldü: −16,6 ve
               −32,0 LUFS teslim edildi.)
```
