# 🎶 THE_BRITTLE_EDGE — MÜZİK

**Kaynak:** `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` §7-19 · akış adım 9

```
⛔ §17 KÜNYESİ:
"İzleyici bu novum'u aşırı soğukta metallerin bükülmeksizin kırılması ve kör kuvvet yerine yükü şasiye yaymanın zorunluluğu olarak okumalı."

TEMPO:        72 BPM (10 s sahne süresine hizalı: 10s = tam 12 vuruş / 3 ölçü)
SÜRE:         120 s (12 sahne × 10.0 s)
MÜZİKSİZ SAHNE: S00 — İlk kopma anında yapay müzik yok; mekanik gerilimin saf çıplaklığı ve derin vakum sessizliği korunur.
SUB-BASS:     45 Hz sub-bass + 110 Hz oktav eşlikçisi (telefon hoparlörlerinde duyulabilir bas tanımı için)
VURUŞ NOKTASI: 3 adet — S00 kopma (02.5s) · S08 temas kaybı (84.0s) · S10 terasa varış (103.5s)
```

---

## 🎼 MÜZİK PROMPTU — tek global tema

```
TOOL: Udio / Suno / MusicFX
GENRE: Minimalist Cinematic Sci-Fi Ambient Drone & Tension Underscore
TEMPO: 72 BPM

INSTRUMENTATION — katmanlar giriş sırasıyla:
  1. Low-frequency analog synth sub-drone (45 Hz fundamental with warm 110 Hz saturation)
  2. Cold bowed metallic cello textures, slow evolving microtonal clusters
  3. Muted analog modular pulse keeping steady 72 BPM heartbeat rhythm
  4. Distant resonant metallic harmonics evoking massive cold hollow structures

DYNAMIC SPREAD — sahne ızgarasıyla birebir:
  00-10 s (S00): Müzik yok. Yalnız mekanik metal gerilimi ve kuru kopma çıtırtısı.
  10-30 s (S01-S02): Çok hafif, soğuk 45 Hz sub-drone ve donuk metalik yaylı dokusu yavaşça yükselir.
  30-60 s (S03-S05): 72 BPM ritmik modüler nabız alttan devreye girer; temkinli, odaklanmış problem çözme atmosferi.
  60-80 s (S06-S07): Yaylı harmonikleri yükselir; gerilen vinç kablosuyla paralel analog rezonans gerilimi.
  80-100 s (S08-S09): Doruk noktası. Ritmik nabız susar, devasa derin bir bas dalgası (110 Hz) aracı havada asılı tutar.
  100-120 s (S10-S11): Bas tonu yumuşar, majör-minör arası dingin bir synth yaylı akoruna dönüşür; ferahlama ve sonsuzluk hissi.

SYNC RULE: Her 10 saniyelik sahne geçişi tam bir müzikal ölçü çizgisine (bar boundary) oturmalıdır.

MIX: mono uyumlu — tüm alt uç merkezde, telefon hoparlöründe çöken geniş stereo yok. Hedef −14 LUFS · −1,0 dBTP.

NO vocals, NO lyrics, NO drums, NO braam, NO riser, NO reversed cymbal, NO whoosh.
```

---

## 🔊 SES YATAĞI VE REPLİK

**Kaynak:** `SES_VE_DIYALOG_URETIM_KILAVUZU.md`

```
REGISTER:     Diegetik mekanik ve biyolojik iç sesler (kask içi solunum, telsiz statik dip tonu)
KATMAN TAVANI: sahne başına aktif katman ≤ 4 · her kesmede oda tonu köprüsü ≥ 0,2 s · dijital sıfır 0 kare
REPLİK SAYISI: 0 (diyalogsuz)
```

| sahne | aktif katmanlar | katman sayısı | ses köprüsü |
|---|---|:--:|:--:|
| S00 | Kask içi soluk · vinç iniltisi · metal kopma çatlağı | 3 | 0,3 s |
| S01 | Kask içi soluk · regolit kayma titreşimi · tekerlek çarpma gümbürtüsü | 3 | 0,3 s |
| S02 | Kask içi soluk · eldiven metal sürtünmesi · mikroyapı çıtırtısı | 3 | 0,3 s |
| S03 | Kask içi soluk · şasiye dokunma sesi · regolit ayak sesi | 3 | 0,3 s |
| S04 | Kask içi soluk · kumaş fermuar açılma · sentetik kayış hışırtısı | 3 | 0,3 s |
| S05 | Kask içi soluk · sapanın metale sürtünme sesi · diz çökme regoliti | 3 | 0,3 s |
| S06 | Kask içi soluk · karabina kilit klik sesi · sapan gerilim çıtırtısı | 3 | 0,3 s |
| S07 | Kask içi soluk · vinç motoru uğultusu · kablo gerilme tınısı | 3 | 0,3 s |
| S08 | Kask içi soluk · son kaya sürtünmesi · derin sessizlik | 3 | 0,3 s |
| S09 | Kask içi soluk · sapan lif gerilme iniltisi · vinç çekiş motoru | 3 | 0,3 s |
| S10 | Kask içi soluk · tekerleklerin terasa oturma gümbürtüsü · vinç durma klik | 3 | 0,3 s |
| S11 | Kask içi soluk · sakinleşen nefes · uzaktan mekanik soğuma çıtırtısı | 3 | 0,3 s |
