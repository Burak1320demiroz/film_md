# 📋 THE_INWARD_FALL — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.
>
> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].**
> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + sahne promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası · çapa jestleri) + C (el/ayak/baş kilitleri)  MOD D
⑮ 🧭 YÖN         → C BLOĞU ekran yönü kilitleri (hedef dilimi · hareket yönü · eksen) + A  MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_INWARD_FALL
FORMAT:            yatay 2-4
RUNTIME:           240.0 seconds (title card: none — screen text lock 0 s)
SCENE COUNT:       6 (24 clips)
PART GRID:         B1 = S01-S03 · 12 clips · 0-120 s · B2 = S04-S06 · 12 clips · 120-240 s
THEME:             ENTROPİ
THEME SCENES:      S01 · S03 · S05
INTENDED EMOTION:  soğuk dehşet ve inatçı direnç (çift-duygu)
ENDING TYPE:       KAFİYE (açılışta janta bağlı tutsak düşen pim ↔ finalde janttan kopup serbest ataletle uzaklaşan kapsül)
PROTAGONIST:       isimsiz teknisyen (nameless human maintenance technician)
CENTRAL CHOICE:    S05 (K19–K20: sıkışan emniyet kordonunu keserek manyetik botları rayda bırakmak ve korumasız olarak sıfır-g merkez aksına atlamak)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S01 · S02 · S03 · S04 · S05 · S06 (tüm film %100 diyalogsuz)
VIRAL INTERSTITIALS: K03 · K21
TITLE:             THE INWARD FALL
LIBRARY CONTEXT:   THE_RING_WALKER, THE_GRAVITY_ANCHOR
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme YOK
SCENE PLAN:      SAHNE PLANI: 3 4 5 3 5 4 · S01 = K01-K03 · S02 = K04-K07 · S03 = K08-K12 · S04 = K13-K15 · S05 = K16-K20 · S06 = K21-K24
INTRA-SCENE CUTS: K01|K02 · K02|K03 · K04|K05 · K05|K06 · K06|K07 · K08|K09 · K09|K10 · K10|K11 · K11|K12 · K13|K14 · K14|K15 · K16|K17 · K17|K18 · K18|K19 · K19|K20 · K21|K22 · K22|K23 · K23|K24 — these cuts are INSIDE one scene: location, light, sound bed, costume dirt, held object and body pose MUST match across them; a reset here is a ② CONTINUITY defect, not a scene change
TARGET ASL BAND: 10.0 s   ASL CURVE: sabit 10.0 s ızgara
GRID:            sahne başlangıcı(n) = 0.0 hook + (n−1) × 10.0 klip
RUNTIME:         240.0 s
RAW FOOTAGE:     24 × 10.0 s = 240.0 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          24 / 24 sabit lockoff (fixed lockoff in vacuum)
SETUP SEQUENCE:  A B C D B D C E F E F C G F C G F E B G H G H J
KURULUM İSKELETİ: A B C D B D C E F E F C G F C G F E B G H G H J
KÜME:            0 (Çok klipli sahne rejiminde KÜME yok; ardışık aynı kurulum yasaktır)
DÖNÜŞ:           15 / 24 = %62.5 ≥ %40
ANGLE ARC:       4 açı tipi (Göz hizası · Solucan/Alt açı · Yüksek/Kuşbakışı · Eğik açı)
DORUK:           S06 (K21) → 200.0 s

REPLİK ZAMANLARI:
   Film tamamen repliksizdir (0 s).

FİNAL VURUŞ KANITI [D141]:
   Beyaz silindirik tahliye kapsülü · 238.0 saniye · 1 adet · BULUNAN (uzaklaşan kapsül)
DÖNGÜ KANITI: K01 jant zemininde düşen çelik pim ↔ K24 merkez akstan uzaklaşan kapsül (tek değişen: sisteme bağlılık)
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 -
(K01–K23: 1 insan; K24: - kapsül içi insan, dış kadraj insansız)
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (isimsiz teknisyen, EVA tulumu)
KASK          Yarı-ayna altın yansıtmalı kavisli vizör, belirgin grafit çerçeve, pürüzsüz kompozit sırt housing [D79/D139/D146]
NOVUM         Dönen silindirde merkeze tırmanırken yerçekimi azalırken, radyal hıza bağlı Coriolis kuvveti bedeni dönme yönünün tersine yana doğru şiddetle savurur.
YERÇEKİMİ     0.40g (K01–K03) → 1.00g (K04–K07) → 0.80g (K08–K12) → 0.50g (K13–K15) → 0.20g (K16–K20) → 0.00g (K21–K24)
ATMOSFER      Vakum (0.00 bar, mutlak havasız uzay)
EKRAN YÖNÜ    Hedef hep merkez kovanı (screen-up), ilerleme radyal tırmanış
SAYAÇ         İstasyon dönme devri (5 RPM → 8 RPM) ve gölge geçiş hızı (1 Hz → 3 Hz), kask içi soluk ritmi
EŞ KADRAJ     K03 ↔ K07 ↔ K12 ↔ K15 (Setup C, MCU yüksek açı kask vizörü)
DÜNYA ÇAPASI  3/3 — dönme eksenine paralel axial güneş ışığı 15°, 60m iç jant silindiri, sabit merkez kovanı [D209]
YIPRANMA      Kask vizörü buğulanması (K03'te başlar), omuz kompozit çizikleri (K10 darbesi), çelik tırabzan aşınması
KİMLİK DİZİSİ Kask A (altın vizör, tüm sahneler), sarı chevron şeritleri sağ kol ve sağ bacakta, grafit gri gövde, botlar K20'de terk edilir [D208]
IŞIK TAKVİMİ  15° axial skimming güneş ışığı (sabit yönlü) + hızlanan gölgeler ve amber alarm flaşları
SES REGISTER  HUMAN 0 · MACHINE 0 (Diyalogsuz, saf diegetik vakum iletimi)
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Kamera Sabitliği (Lockoff Doğrulama)
KOMUT         ffmpeg -v error -i "$VIDEO" -vf select='eq(n\,0)+eq(n\,239)',scale=1920:1080 -f null -
DOĞRULANDI    ffmpeg 7.0 · 28.09.2026
İKAME         Kare farkı kontrolü
```
