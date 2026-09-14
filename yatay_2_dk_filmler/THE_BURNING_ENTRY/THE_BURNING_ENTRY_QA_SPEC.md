# 📋 THE_BURNING_ENTRY — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 💥 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_BURNING_ENTRY
FORMAT:            Yatay 2-4 Dk (§2.2) — 16:9 Sinematik Format
RUNTIME:           120 seconds (title card: 0s — screen text lock 0 s)
SCENE COUNT:       12 scenes
PART GRID:         — (2-minute single horizontal block)
THEME:             BEDEL
THEME SCENES:      S02 · S04 · S07 · S08 · S09
INTENDED EMOTION:  High-tension claustrophobia and desperate physical survival effort
ENDING TYPE:       Final Twist (Giant canyon shadow rise - K0 reveal)
PROTAGONIST:       Single 35-year-old male astronaut pilot
CENTRAL CHOICE:    Manual single-thruster counter-thrusting vs spinning to disaster (S07)
DIALOGUE LINES:    0 lines · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S09 (Complete external sound cutout)
VIRAL INTERSTITIALS: S00 · S01 · S02 · S03 · S04 · S05 · S06 · S07 · S08 · S09 · S10 · S11
TITLE:             47 Seconds Until Impact | THE BURNING ENTRY
LIBRARY CONTEXT:   THE SILENT DESCENT, LOSS OF LIFT, THE CRACKED HELMET
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12 clips
SHOT COUNT:      12 shots · sahne içi kesme 0
TARGET ASL BAND: 10s   ASL CURVE: Constant 10.0s per clip (Veo 3.1 engine limit)
GRID:            sahne başlangıcı(n) = 0 + (n−1) × 10 s
RUNTIME:         120s
RAW FOOTAGE:     120s · TRIM BUDGET: 0s
SCREEN TEXT:     0 saniye
CAMERA:          35mm / 50mm / 85mm single unbroken camera takes
SETUP SEQUENCE:  Setup A (S00) → Setup B (S01) → Setup C (S02) → Setup D (S03) → Setup A (S04) → Setup E (S05) → Setup F (S06) → Setup C (S07) → Setup G (S08) → Setup A (S09) → Setup H (S10) → Setup I (S11)
KURULUM İSKELETİ: A - B - C - D - A - E - F - C - G - A - H - I
KÜME:            2 küme (S00-S01, S08-S09)
DÖNÜŞ:           5 dönüş (%41.6 >= %40 ✅ — Setup A 3x, Setup C 2x)
ANGLE ARC:       5 açı tipi (Eye-level, High angle, Low angle, Ext Wide, Tracking spin)
DORUK:           S08 → Üç Kademeli Çakılma (sahne başlangıcı 80 s)

REPLİK ZAMANLARI: Replik yok (0 replik)

FİNAL VURUŞ KANITI [D141]:
   Uzak dikey kaya kulesinde yükselen 1 adet devasa masif organik gölge silueti (K0 level) · 118. saniye · BULUNAN · 120. saniyede aniden kararma (hard cut to black).
DÖNGÜ KANITI: Açılış kokpit sarsıntısı ↔ Kapanış kanyonda doğrulup yükselen Dev Gölgeye bakan pilot (Twist tohum bilgisi).
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1 1 1 (12/12 insan var — pilot her sahnenin odağında)
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (Pilot)
KASK          Optik berrak visor · Sol vizörde 3cm dikey dairesel dikey hairline mikro-çatlak (S04-S11) · Sırt paneli pürüzsüz titanyum
NOVUM         Yörünge bozulumundan tek iticiyle kanyona çakılma manevrası
YERÇEKİMİ     Vakum orbital zero-g (S00-S02) → Planet reentry 1.0g gravity (S03-S11)
ATMOSFER      Uzay vakumu (S00-S02) → Pas kırmızısı alien atmosferi ve kanyon alacakaranlığı (S03-S11)
EKRAN YÖNÜ    Mekik alçalma vektörü soldan sağa kilitli (L->R)
SAYAÇ         Vizör çatlak boyutu: S04'te 3cm tek çizgi → S08'de 5cm dikey dallanma → S10'da is kaplı matlaşma
EŞ KADRAJ     S00↔S04 (Setup A MCU), S02↔S07 (Setup C Close-up)
YIPRANMA      Sabit kask vizörü çizik ve titanyum zırh aşınması
IŞIK TAKVİMİ  Kokpit acil kırmızı/turuncu parıltısı → Atmosfer turuncu plazması → Kanyon alacakaranlık gölgesi
SES REGISTER  DIEGETIC MECHANICAL 100% · HUMAN 0%
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Kamera Sabitlik Kapısı (10s klip unbroken take denetimi)
KOMUT         python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py yatay_2_dk_filmler/THE_BURNING_ENTRY
DOĞRULANDI    Python 3.12 · 14.09.2026
İKAME         Manuel kurgu ve prompt kontrol script çıktısı
```
