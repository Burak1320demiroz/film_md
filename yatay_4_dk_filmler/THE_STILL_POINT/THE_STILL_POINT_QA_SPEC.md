# 📋 THE_STILL_POINT — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.
> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].**
> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar.

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
FILM:              THE_STILL_POINT
FORMAT:            YATAY 16:9
RUNTIME:           240.0 seconds (title card: 0.0 — screen text lock 0 s)
SCENE COUNT:       24
PART GRID:         —
THEME:             cesaret (Korkunun içinde rasyonel ve doğru hareketi bulmak)
THEME SCENES:      S07 · S12 · S17
INTENDED EMOTION:  dread shifting to calculated calm, awe at orbital mechanics
ENDING TYPE:       RHYME (kafiye). Seed at S00, paid at S23. Wrench flings at S00, floats calmly at S23.
PROTAGONIST:       an unnamed astronaut (sole survivor, EVA rigger, no proper name in prompts [D34])
CENTRAL CHOICE:    S09 — she launches the cart in reverse against the rotation (starts 90.0 s)
COST:              S12 — she uncouples the maintenance cart and pushes it into the void, eliminating return (starts 120.0 s)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0 / RADIO 0
                   ⛔ THE FILM IS SILENT BY DESIGN. In the story rubric DIALOGUE IS N/A.
                   ⛔ CHARACTER: the face is behind an opaque gloss-black visor in all scenes.
SILENT SCENES:     all 24 scenes (no spoken dialogue, sound is internal breath + structure conduction)
VIRAL INTERSTITIALS: S17 (The Still Point)  ⛔ THIS MAY NOT BE CUT
UNCUTTABLE:        S00 · S01 · S05 · S09 · S11 · S12 · S15 · S17 · S20 · S23
TITLE:             "THE STILL POINT" promises a point of relative rest amidst extreme rotation.
LIBRARY CONTEXT:   Horizontal 4-minute hard sci-fi, second film exploring §3.7 rotating station mechanics, unique in demonstrating zero-g counter-rotation transition.
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE · ⑦ AKSİYON · ⑨ KADRAJ · ⑫ HOOK)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri YOK)
ASL CURVE:       FLAT, by design (24 scenes × 10.0 s = 240.0 s).
GRID:            sahne başlangıcı(n) = (n) × 10.0 s (S00=0.0s, S01=10.0s, ..., S23=230.0s)
RUNTIME:         240.0 s
RAW FOOTAGE:     24 × 10.0 s = 240.0 s · TRIM BUDGET: 0.0 s
SCREEN TEXT:     0.0 saniye — başlık kartı, jenerik, altyazı, filigran DÂHİL
CAMERA:          24/24 mechanically stable or locked-off
SETUP SEQUENCE:  A B C B B C D E D E E D F G H G G H D F D F F D
KURULUM İSKELETİ: A B C B B C D E D E E D F G H G G H D F D F F D
KÜME:            4 adet (S03-S04, S09-S10, S15-S16, S21-S22) ≥ 2
DÖNÜŞ:           14 / 24 = %58 ≥ %40
ANGLE ARC:       4 açı tipi — dutch angle · high angle · eye level · low angle
DORUK:           S17 → Nora boşluğun ortasında, arkasında dönen devasa istasyon (170.0 s)
BÖLÜM SINIRI:    S11 ↔ S12 · MS→WS · Bölüm 1 sonu / Bölüm 2 başı

REPLİK ZAMANLARI: yok (replik 0).

FİNAL VURUŞ KANITI [D141]:
   TURUNCU ANAHTAR · 236.0 s · 1 adet · BULUNAN
   Kapsül içinde Nora'nın parmakları yanında sakince havada süzülen turuncu İngiliz anahtarı.
   ffmpeg -ss 236 -i "$M" -frames:v 1 kanit.jpg → BAK
DÖNGÜ KANITI: ilk kare (S00 · 0.0 s) ↔ son kare (S23 · 239.0 s)
   AYNI nesne (turuncu anahtar) · AYNI mikro-yerçekimi ortamı.
   TEK değişken: hareket niteliği — S00'da ölümcül teğetsel fırlama, S23'te sükunet içinde süzülüş (KAFİYE).
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  101110111111111111111111
       (1 = insan var · 0 = insansız · sahne başına bir karakter)
       insansız yuvalar: S01 (kopan geçit ve istasyon mimarisi) · S05 (savrulan cihaz kanıtı)
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (Nora, EVA basınç giysili, isimsiz)
KASK          opak parlak siyah dışbükey vizör · sırt silueti düz (flat back) · sırt ünitesi kompakt [D79·D139]
NOVUM         Dönen halkanın teğet hızının (8 m/s) ters yönde sürüşle sıfırlanması
YERÇEKİMİ     S00-S11: 0.065g (dönen güverte); S12: 0.065g→0g; S13-S23: 0g (serbest süzülme / sabit merkez)
ATMOSFER      Sert uzay vakumu (0 kPa), atmosfer yok
EKRAN YÖNÜ    Hedef merkez kaçış kapsülü kadraj merkezinde sabit · ray hareketi dönme teğetine zıt
SAYAÇ         Hız göstergesi 0 m/s'den 8 m/s'ye monotonik yükselir (S09-S11)
EŞ KADRAJ     S00 (fırlayan anahtar) ↔ S23 (süzülen anahtar)
DÜNYA ÇAPASI  3/3 — Satürn dev diski · altın renkli halkalar · ORISON çift halkalı kafesi [D209]
YIPRANMA      3 sabit bölge — mat beyaz göğüs zırhı · turuncu sağ önkol şeridi · turuncu alet yüzeyi [D42]
KİMLİK DİZİSİ kask hep kapalı (K) · turuncu şerit SAĞ önkol · koyu kayrak grisi giysi · aşınma S00'dan başlar [D208]
IŞIK TAKVİMİ  Sabit tek yönlü Güneş ışığı ve Satürn gezegen yansıması, monotonik
SES REGISTER  HUMAN 0 · MACHINE 0 (kask içi nefes ve mekanik temas rezonansı)
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142]

```
KAPI          Kamera ve kadraj stabilitesi (lockoff denetimi)
KOMUT         ffmpeg -i "$M" -vf "vidstabdetect=stepsize=32:shakiness=10:accuracy=15:result=transforms.trf" -f null -
DOĞRULANDI    ffmpeg 6.1 · 20.09.2026
İKAME         Sahneler arası manuel optik sınır ve kadraj sapması denetimi
```
