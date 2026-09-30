# 📋 THE_BRITTLE_EDGE — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

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
FILM:              THE_BRITTLE_EDGE
FORMAT:            yatay 2-4 (12)
RUNTIME:           120 seconds (title card: 0s — screen text lock: 0s)
SCENE COUNT:       12
PART GRID:         —
THEME:             UYUM VE ÖĞRENME (Kuvvet yerine metot değişimi)
THEME SCENES:      S03 · S05 · S08 · S11
INTENDED EMOTION:  Gerilim, odaklanmış mekanik problem çözme, dingin kurtuluş
ENDING TYPE:       KAFİYE (S00 kopan çekme halkası ↔ S11 kurtarılan sağlam şasi)
PROTAGONIST:       Yalnız astronot (Ekin — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S05 — Doğrudan çekmeyi terk edip kompozit sapanı ana şasi altına geçirme
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S00-S11 (tamamen diyalogsuz film)
VIRAL INTERSTITIALS: S00, S01, S05, S08, S09, S11  ⛔ THESE MAY NOT BE CUT
TITLE:             The Tow Hook Snapped on the Moon | THE BRITTLE EDGE
LIBRARY CONTEXT:   THE_LISTENING_WORLD (yatay 2 dk), THE_LAST_SHIFT (Ay/vakum), THE_BORROWED_WEIGHT (kurtarma)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12
SHOT COUNT:      12 · sahne içi kesme 0
TARGET ASL BAND: 10.0 s   ASL CURVE: SABİT (Her klip tam 10.0 saniye üretilir)
                 GEREKÇE: Kart §2.2 yatay 2-4 dakika standart modüler 12 klip kurgusu [D74]
GRID:            sahne başlangıcı(n) = 0 hook + (n−1) × 10.0 klip
RUNTIME:         120.0 s
RAW FOOTAGE:     120.0 s · TRIM BUDGET: 0.0 s
SCREEN TEXT:     0 saniye
CAMERA:          11 / 12 sabit lockoff (S11 tek yavaş geri çekilme)
SETUP SEQUENCE:  A B C D B D C C E E B A
KURULUM İSKELETİ: A B C D B D C C E E B A
KÜME:            2 adet (S06-S07: C-C; S08-S09: E-E)
DÖNÜŞ:           6 / 12 = %50 (S04→B, S05→D, S06→C, S07→C, S09→E, S10→B, S11→A)
ANGLE ARC:       3 açı tipi (göz hizası, alçak açı, yüksek açı)
DORUK:           S08-S09 → Aracın boşlukta tamamen askıda kalması (80.0 s - 100.0 s)

REPLİK ZAMANLARI: Yok (0 replik)

FİNAL VURUŞ KANITI [D141]:
   Kırık çelik çekme halkası parçası · 115.0 saniye · 1 adet · BULUNAN nesne
   ffmpeg -ss 115 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ / KAFİYE KANITI: S00 kopan tek çekme halkası ↔ S11 kurtarılan sağlam sarı şasi
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  - 1 - 1 1 1 1 1 1 1 1 1     (1 = insan var · - = insansız nesne planı)
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (Tek astronot, film boyu aynı karakter)
KASK          Altıgen çerçeveli kask, opak yansıtıcı siyah vizör, kask içi ışık yok [D16, D146, D74 sapma kaydı]
NOVUM         Kriyojenik sıcaklıkta çeliğin sünek-gevrek geçiş sıcaklığı (DBTT) altında bükülmeden gevrek kırılması
YERÇEKİMİ     0.16 g (Ay yerçekimi, balistik toz ve parça düşüşü)
ATMOSFER      0 Pa (sert vakum, hava sürtünmesi ve dağılması yok)
EKRAN YÖNÜ    Uçurum ve krater boşluğu hep kadrajın sağ/alt diliminde, güvenli teras sol/üst diliminde (12/12 sabit eksen)
SAYAÇ         Metinsiz tekerlek temas mesafesi (S01 0cm → S08 10cm → S09 askıda 0 temas → S10 zemin 4 tekerlek)
EŞ KADRAJ     S08 ↔ S09 (aynı kurulum E, devam karesi)
DÜNYA ÇAPASI  3/3 — zifiri karanlık uzay göğü · keskin krater sırtı ufku · 25° eğimli bazalt regolit terası [D209]
YIPRANMA      Sarı gövde üzerinde 3 sabit çapa: sol çamurluk çizikleri, mat regolit tozu, siyah kablo aşınması [D42]
KİMLİK DİZİSİ Kask K (kapalı) tüm sahnelerde; turuncu önkol şeritleri; kirli kırık beyaz giysi; sol dizde koyu regolit lekesi (S03'ten itibaren) [D208]
IŞIK TAKVİMİ  15° alçak açılı güneş, sabit tek yönlü ışık takvimi (monotonik)
SES REGISTER  HUMAN 0 · MACHINE 0
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Süre doğrulaması
KOMUT         ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$M"
DOĞRULANDI    ffprobe 6.0 · 20.09.2026
İKAME         mediainfo --Inform="General;%Duration%" "$M"

KAPI          Çözünürlük ve en-boy oranı doğrulaması
KOMUT         ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$M"
DOĞRULANDI    ffprobe 6.0 · 20.09.2026
İKAME         mediainfo --Inform="Video;%Width%x%Height%" "$M"
```
