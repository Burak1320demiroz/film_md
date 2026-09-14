# 🎶 THE_BENT_GRASS — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ ÖNCE YAZILDI — bu cümle olmadan müzik promptu yazılmaz:

   "İzleyici bu novum'u BİR TEHDİT DEĞİL, GERİ ALINAMAZ BİR KAYIT olarak
    okumalı: ova kimseye saldırmıyor, yalnız hiçbir şeyi unutmuyor."

   ⭐ Bu cümle yazılmadan aynı kare üç ayrı türe çevrilebilirdi
   (gergin drone → korku · yalnız çello → yas · hareketsiz nabız → huşu).
   Seçilen okuma üçüncüsüdür ve müzik-görüntü ilişkisi ANEMPATİKTİR:
   sürü yaklaşırken müzik TEPKİ VERMEZ.

TEMPO:        72 BPM — 10 s sahneye HİZALI (§14: 72 BPM → sahne başına
              TAM 3 ölçü 4/4). 14 sahne × 3 ölçü = 42 ölçü. Her sahne
              sınırı bir ölçü çizgisine düşer.
SÜRE:         140,0 s = 10,0 + (14−1) × 10,0   (RUNTIME formülünden)
MÜZİKSİZ SAHNE: S11 (110,0-120,0 s) — filmin doruğu.
              ⛔ Müzik S10'un SONUNDA biter (108,0 s), doruğun başında değil:
                sessizliğin fark edilmesi 1-2 saniye ister (§10).
              ⭐ S12-S13 de müziksizdir (koda + final) — müzik 108,0 s'de
                kesilir ve BİR DAHA GİRMEZ. Filmin son 32 saniyesi yalnız
                ortam yatağıdır.
SUB-BASS:     48 Hz + 96/144/192 Hz oktav eşlikçisi (§15.1 + §15.1a).
              ⛔ Eşlikçi bir YEDEK değildir, temeli beyinde İNŞA EDEN
                unsurdur (missing fundamental) — taşıyıcı seviyede mikslenir.
                Miks 150 Hz altındaki her şeyin tamamen kaybolduğu
                varsayımıyla yapılır.
VURUŞ NOKTASI: 3 tane, azlığı bilinçli:
              ① 50,0 s (S5 · ufuktaki hat) — tek alçak nota girer
              ② 90,0 s (S9 · ayrılık) — iki katman AYRIŞIR, çözülmez
              ③ 108,0 s (S10 sonu) — müzik KESİLİR (fade yok)
KAPANIŞ:      fade out YOK · çözülmemiş akor YOK · KESME — ve kesmeden
              sonra 32 saniye yalnız rüzgâr ve ot.
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Suno / Lyria — one continuous instrumental piece, 140 seconds.
GENRE: sparse ambient orchestral drone, patient and unhurried, no cinematic
       trailer language.
TEMPO: 72 BPM, 4/4, steady, no rubato, no accelerando anywhere in the piece.

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. a low sustained drone at roughly 48 Hz, doubled by a quiet companion
     tone at roughly 96 Hz and reinforced by a dense harmonic stack around
     144 Hz and 192 Hz, so the weight survives full loss of everything
     below 150 Hz
  2. a dry, close-mic'd solo viola holding long single notes, entering at
     0:50, never playing a melody, never resolving a phrase
  3. a soft granular texture of dry rustling grain, low in the mix,
     entering at 1:30 and staying at the same level to the end
  4. a single struck low piano note used exactly three times

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
    0-10 s   (S0): silence for the first two seconds, then the drone alone,
                   very quiet, entering under the grass sound
   10-50 s   (S1-S4): drone only, unchanging level, no build
   50-60 s   (S5): one low viola note enters and holds; the drone does not
                   change and does not swell
   60-90 s   (S6-S8): the same two layers hold, flat, indifferent; nothing
                   in the music reacts to what is happening on screen
   90-100 s  (S9): the viola and the drone separate into two pitches a
                   whole tone apart and stay there, unresolved
  100-108 s  (S10): the granular grain texture thins out; the last struck
                   piano note lands at 106 s
  108 s: THE TRACK IS CUT. No fade, no final chord, no reverb tail.
  108-140 s (S11-S13): no music at all.

SYNC RULE: no hit points, no stingers, no swells on any event. The music
must not react to the animals, to the emptied case, or to the approach —
its indifference is the point. The only three musical events are the three
listed above, and none of them coincides with a dramatic beat.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş
stereo yok. Reverb is short and dry (an open field, not a hall).
Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO percussion, NO braam, NO riser,
NO reversed cymbal, NO whoosh, NO orchestral swell, NO choir.
```

> Referans hissi verilebilir, **alıntı verilemez**: bir bestecinin dokusuna
> atıf serbest; melodi, motif veya söz kopyalamak yasak.

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     — (replik yok; register haritası boş)
REPLİK SAYISI: 0
GEREKÇE:      sahibin talep cümlesinde diyalog yok · depoda replikli film
              0/79 · PROB B (tek replik) hiç koşulmadı · ekranda konuşan
              ağız iki riski birden açar (lip-sync çöküşü + AI damgası,
              fonem↔vizem tespit kanalı).
              ⛔ Sessizlik bir KISITTIR, eksik değil: T4'te Diyalog N/A
                yazılır, düşük puan değil [D113].

⛔ ORTAM YATAĞI ENVANTERİ [D83] — "müziksiz" sahne SESSİZ sahne değildir.
   Cold Burn'ün ölçülmüş hatası 20 saniyelik dijital sıfırdı.

   ZEMİN (14/14 sahnede kesintisiz, kurguda TEK PARÇA serilir):
     · kuru ot hışırtısı — sürekli, dalga geçerken yükselip alçalan
     · alçak açık alan rüzgârı — tek yönlü, gürültüsüz
   YAKIN KATMAN (kadraja göre):
     · giysi kumaşının gerilmesi (S3 · S6 · S8 · S10)
     · suit fanının çok alçak sürekli uğultusu (kasklı yakın planlar: S4 · S6)
     · nefes — GÖRÜNÜR değil DUYULUR: kask içi, yavaş, ölçülü
   OLAY SESLERİ (tek tek, sayılı):
     · bot basışı (S0 · S1 · S9)
     · kasa kilidi (S6) · kasa boşalması (S10)
     · uzak metal tıkırtısı — iniş aracı gövdesi (S2)
     · ağır dört ayaklı basışı (S7 uzak · S11 tek ve yakın · S13 tek)
     · alçak toprak uğultusu — sürünün uzaktaki yürüyüşü (S5 · S12)

⛔ TESLİMDEN ÖNCE: 108-140 s aralığı kulakla dinlenir. Müzik orada
  bilerek yoktur; MUTLAK DİJİTAL SIFIR varsa yatak yeniden serilir.
  Ölçüm: ffmpeg -i <master> -af "silencedetect=noise=-50dB:d=0.3" -f null -
  → bu aralıkta sessizlik aralığı ÇIKMAMALIDIR.

REPLİK ZAMANLARI: ⛔ HESAPLANMAZ, HESAPLATILIR [D122] — bu filmde replik
  olmadığı için tablo boştur; sahne başlangıçları aynı formülle:
  sahne(n) = 10,0 + (n−1) × 10,0
```
