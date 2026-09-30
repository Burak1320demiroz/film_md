# 🎶 THE_LAST_TOW — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ — bu cümle yazılmadan müzik promptu yazılmaz:
   "İzleyici bu novum'u DEĞEN ŞEYİN BİR DAHA AYRILMAMASI olarak okumalı."

TEMPO:        72 BPM — 10,0 s klibe HİZALI: 4/4'te bir ölçü 3,333 s, üç ölçü tam
              10,0 s → her klip sınırı bir ölçü çizgisine düşer (§14)
SÜRE:         480 s = filmin RUNTIME'ı (48 × 10,0 s)
MÜZİKSİZ SAHNE: S01 (0-40 s) ve S03 (70-120 s) — ⛔ §10'un istediği en az bir tane;
              bu filmde İKİ tane, gerekçesi aşağıda
SUB-BASS:     38 Hz + 90-160 Hz oktav eşlikçisi (§15.1 — telefon hoparlörü 38 Hz'i
              hiç çalmaz; eşlikçi olmadan o katman YOK demektir)
VURUŞ NOKTASI: 4 tane — 240 s · 360 s · 430 s (SUSMA) · 470 s
              ⭐ azlığı tasarımdır: filmin ses kanalı TEMAS, müzik onun altında durur
```

⭐ **NEDEN İKİ MÜZİKSİZ SAHNE:** bu filmin ortam kartı "dışarıda ses yok, duyulan
her şey TEMASTIR" diyor. Müzik ilk 40 saniyede hiç yoksa izleyici kuralı ses
tarafından da öğrenir: bu dünyada bir şey duyuluyorsa ona bir şey DEĞMİŞTİR.
S03 ikinci kez susar çünkü orada iki uzak ışık yaklaşıyor ve tek taşıyıcı nefes olmalı.

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Google Flow (Music)
GENRE: minimal ambient drone, cold metallic, no melody
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. 38 Hz sine sub with a 90-160 Hz octave companion — enters at 40 s, never leaves
  2. bowed metal plate, single sustained note, no vibrato — enters at 120 s
  3. very slow tremolo on a low string, one semitone movement only — enters at 240 s
  4. a single struck metal harmonic, decaying eight seconds — only on the hit points

DYNAMIC SPREAD — klip ızgarasıyla birebir:
  0-40 s      (S01 · K01-K04): SILENT. Only the sound bed and contact.
  40-70 s     (S02 · K05-K07): layer 1 alone at -26 LUFS, no movement
  70-120 s    (S03 · K08-K12): SILENT again — layer 1 fades out over 3 s at 70 s
  120-160 s   (S04 · K13-K16): layers 1 + 2, rising 3 dB across the scene
  160-200 s   (S05 · K17-K20): layers 1 + 2 hold, no rise
  200-240 s   (S06 · K21-K24): layers 1 + 2, one 4 dB swell into the part boundary
  240-280 s   (S07 · K25-K28): HIT 1 at 240 s (layer 4), layer 3 enters under it
  280-330 s   (S08 · K29-K33): layers 1 + 2 + 3, quiet, no swell — the reveal is silent
  330-360 s   (S09 · K34-K36): layer 3 alone thins to a single held note
  360-400 s   (S10 · K37-K40): HIT 2 at 360 s, all layers, the loudest 40 s of the film
  400-430 s   (S11a · K41-K43): layers pull back 6 dB, tension held
  430-431,4 s (S11b · K44): ⭐ HARD MUTE — every layer cuts to digital silence for 1,4 s
  431,4-450 s (S11c · K44-K45): layer 1 returns alone, very low
  450-480 s   (S12 · K46-K48): layers 1 + 2; HIT 4 at 470 s, then both withdraw over 4 s

SYNC RULE: hiçbir katman klip sınırının ORTASINDA girmez ya da çıkmaz — giriş ve
çıkış yalnız 3,333 s'nin katlarında olur. HARD MUTE 430,0 s'de başlar (43. klibin
sonu = 430 s) ve 431,4 s'de biter, yani 44. klibin ilk 1,4 saniyesi tamamen sessizdir.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş stereo yok.
Hedef -14 LUFS · -1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🥁 VURUŞ NOKTALARI — dördü de bir OLAYIN üstüne düşer

| # | saniye | klip | olay | müzik ne yapıyor |
|:--:|--:|:--:|---|---|
| 1 | 240,0 | K25 | ışık kenarı dikişe varıyor, kaynak kopuyor | tek vurulmuş metal armonik + 3. katman girer |
| 2 | 360,0 | K37 | iki bot tabanı kopuyor | armonik ikinci kez, bütün katmanlar açık |
| 3 | **430,0** | **K44** | kesici kafası dikişe değiyor ve KALIYOR | ⭐ **HARD MUTE 1,4 s** — filmin tek dijital sessizliği |
| 4 | 470,0 | K48 | çekici gitti, resifte tek yeni işaret | armonik son kez, sonra iki katman 4 s'de çekilir |

```
⛔ HARD MUTE MODELDEN İSTENMEZ [D180]. Bu bir KURGU işlemidir: video promptunun
  AUDIO satırı K44'te doludur (tek tık + metalin gerilmesi). Sessizlik MÜZİK
  katmanının kesilmesidir, ses yatağının değil.
⭐ NEDEN K44: filmin bedeli K43'te ÖDENİR ama K44'te KANITLANIR. Müziğin kesildiği
  yer kararın alındığı yer değil, geri alınamaz olduğunun görüldüğü yerdir.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     — (bu filmde diegetik yapay ses YOK: suit AI yok, telsiz yok, kayıt yok)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s ·
              dijital sıfır 0 kare (HARD MUTE hariç, o KURGU kararıdır ve 1,4 s'dir) ·
              kadraj dışı replik yok [D216]
REPLİK SAYISI: 0
REPLİK ZAMANLARI: — (replik yok; ㉓ envanteri promptlarda 0 tırnak sayar)
```

### KATMAN TABLOSU — ③ SES merceğinin LAYER COUNT ölçümü

| sahne | katmanlar (ad) | sayı | köprü |
|---|---|:--:|---|
| S01 | temas sesi (kesici uğultusu, bot, anahtar tıkı) · nefes | 2 | oda tonu kesilmez |
| S02 | temas (eldiven rasp) · nefes · fener motoru · müzik k1 | 4 | ✓ |
| S03 | nefes · suit fanı · helmet halkası scrape | 3 | ✓ |
| S04 | kesici notası · nefes · müzik k1 · müzik k2 | 4 | ✓ |
| S05 | ölçü aleti tıkları · nefes · müzik k1 · müzik k2 | 4 | ✓ |
| S06 | çapa/levha çanı · nefes · müzik k1 · müzik k2 | 4 | ✓ |
| S07 | kuru çatlama · metal tık · nefes · müzik (k1-k4) | 4 | ✓ |
| S08 | kapak sürtünmesi · nefes · müzik k1 · müzik k3 | 4 | ✓ |
| S09 | kör bıçak notası · nefes · müzik k3 | 3 | ✓ |
| S10 | iki kopuş · yük basıncı · nefes · müzik (tümü) | 4 | ✓ |
| S11 | çerçeve gerilmesi · tek tık · nefes · müzik k1 | 4 | ⭐ 430,0-431,4 s HARD MUTE |
| S12 | çekici gövde sesi · nefes · müzik k1 · müzik k2 | 4 | ✓ |

⛔ Hiçbir sahnede 4 katman aşılmadı. ⛔ Müzik sahne İÇİNDE kesilmez — S03'ün
çıkışı S02'nin son klibinin sonunda (70,0 s = sahne sınırı) tamamlanır.
