# 📋 THE_STATIC_VEIL — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_STATIC_VEIL_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

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
FILM:              THE_STATIC_VEIL
FORMAT:            yatay_2_dk_filmler
RUNTIME:           120.0 seconds (title card: 0 — screen text lock 0 s)
SCENE COUNT:       12
PART GRID:         —
THEME:             FEDAKÂRLIK
THEME SCENES:      S00 · S02 · S09 · S11
INTENDED EMOTION:  Tense sacrifice, optical vulnerability, determined resolution
ENDING TYPE:       Kafiye / Bedelle Yaşama
PROTAGONIST:       isimsiz EVA astronotu (özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S08 Battery unlatch decision
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     S00-S11 (all 12 scenes)
VIRAL INTERSTITIALS: S00 (dust lift), S02 (visor scouring), S08 (battery hesitation), S09 (battery arc), S11 (final lit beacon)
TITLE:             THE STATIC VEIL — the invisible electrostatic dust layer that blinds the astronaut
LIBRARY CONTEXT:   THE_BRITTLE_EDGE, THE_SHADOW_LINE
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      12
SHOT COUNT:      12 · sahne içi kesme 0
SCENE PLAN:      —
INTRA-SCENE CUTS: —
TARGET ASL BAND: 10.0 s   ASL CURVE: SABİT (Her klip tam 10.0 saniye)
                 GEREKÇE: Kart §2.2 yatay 2-4 dakika standart modüler 12 klip kurgusu [D74]
GRID:            sahne başlangıcı(n) = 0 hook + (n−1) × 10.0 klip
RUNTIME:         120.0 s
RAW FOOTAGE:     120.0 s · TRIM BUDGET: 0.0 s
SCREEN TEXT:     0 saniye
CAMERA:          12 / 12 sabit lockoff tripod
SETUP SEQUENCE:  A B C C D E D C C D E A
KURULUM İSKELETİ: A B C C D E D C C D E A
KÜME:            2 adet (S02-S03: C-C; S07-S08: C-C)
DÖNÜŞ:           5 / 12 = %42 (S03→C, S06→D, S07→C, S08→C, S09→D)
ANGLE ARC:       3 açı tipi (Düşük Açı, Göz Hizası, Üst Açı)
DORUK:           S09 → Batarya çarpması ve kask ekranlarının sönüşü (90.0 s)

REPLİK ZAMANLARI: Yok (0 replik)

FİNAL VURUŞ KANITI [D141]:
   Yanan optik fener amber ışık konisi · 115.0 saniye · 1 adet · BULUNAN nesne
   ffmpeg -ss 115 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ / KAFİYE KANITI: S00 karanlık pilon ↔ S11 yanan fener ve uzaklaşan kararmış astronot
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  - 1 1 1 1 1 1 1 1 1 1 1     (1 = insan var · - = insansız nesne planı)
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 (Tek astronot Can, film boyu aynı karakter)
KASK          Beyaz sert kompozit çerçeve, altın aynalı küresel yansıtıcı vizör, kask içi ışık yok, sırtsız düz gövde [D16, D146]
NOVUM         Regolit toz taneleri × kask vizörü cam yüzeyi → elektrostatik levitasyon ve optik körlük
YERÇEKİMİ     0.16 g (Ay yerçekimi, yavaş adımlar, tozlar dik asılı kalır)
ATMOSFER      0 Pa (sert vakum, hava sürtünmesi ve saçılma yok)
EKRAN YÖNÜ    Pilon ve fener hedefi hep kadrajın sağ diliminde, astronot soldan sağa ilerler (12/12 sabit eksen)
SAYAÇ         Metinsiz vizör matlaşma oranı (S00 %0 → S01 %15 → S02 %50 → S08 %80 → S09 2cm temiz delik)
HAREKET KİLİDİ Her sahnede tek odaklanmış kinesik eylem; yürüme, silme, arama, sökme, çarpma
EŞ KADRAJ     S00 ↔ S11 (aynı kurulum A, tam kafiye)
DÜNYA ÇAPASI  3/3 — zifiri karanlık uzay göğü · keskin krater sırtı güneş hattı · zemin çelik rayı ve pilon [D209]
YIPRANMA      Giysi üzerinde regolit tozu birikimi S01'den S11'e monoton artar [D42]
KİMLİK DİZİSİ Beyaz sert gövde, koyu gri körük eklemler, altın yansıtıcı vizör, sol kolda basınç saati [D208]
IŞIK TAKVİMİ  Krater kenarından düşük açılı sert güneş, tek yönlü monoton ışık açısı
SES REGISTER  HUMAN 0 · MACHINE 0
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          Süre doğrulaması
KOMUT         ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$M"
DOĞRULANDI    ffprobe 6.0 · 26.09.2026
İKAME         mediainfo --Inform="General;%Duration%" "$M"

KAPI          Çözünürlük ve en-boy oranı doğrulaması
KOMUT         ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 "$M"
DOĞRULANDI    ffprobe 6.0 · 26.09.2026
İKAME         mediainfo --Inform="Video;%Width%x%Height%" "$M"
```
