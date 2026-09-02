# 📋 THE STILL SWARM — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> Paketi betik üretir:
> `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh yatay_2_4_dk_filmler_uzay/THE_STILL_SWARM <master>`

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]:
                   PARÇA SAYISI · IŞIK TAKVİMİ · EKRAN YÖNÜ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE STILL SWARM
FORMAT:            yatay 2-4 dk · 16:9
RUNTIME:           140 seconds (title card: NONE — screen text lock 0.0 s)
SCENE COUNT:       14   (S0–S13)
THEME:             FIRST-CONTACT
THEME SCENES:      S1 · S7 · S11 · S13        (en az üç ✅)
INTENDED EMOTION:  AWE — not anxiety. The film's signature is a single
                   valence; the share slot is S11 and it is an awe slot.
ENDING TYPE:       TWIST + LOOP  (the rule itself breaks; direction is born)
PROTAGONIST:       isimsiz salvage operator, late thirties, woman
                   (özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S11 · 1:50-2:00 — she pushes away the one object she came
                   for, because pushing it is the only way out
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
SILENT SCENES:     14 / 14 (no spoken line anywhere in the film)
VIRAL INTERSTITIALS: S7 · S11 · S13    ⛔ THESE MAY NOT BE CUT
TITLE:             "THE STILL SWARM" — promises a crowd that does not move.
                   The film delivers that in the first frame and breaks it in
                   the last ten seconds.
LIBRARY CONTEXT:   same shelf, vacuum family: THE DEAD APPROACH · THE COLD WELD
                   (§3.1 vacuum card). This is the shelf's first FIRST CONTACT
                   film and its first zero-gravity 2-4 minute film.
```

### ⛔ KESİLEMEZ SAHNELER (kurgu kapısı listesi)

```
S2 · S5 · S6 · S10 · S11   — novum kanıt zinciri (ONERME §5: kurulum ·
                              doğrulama · sonuç). Biri düşerse kural çöker.
S6                          — NOVUM TAŞIYICISI · TEK KARE
S7 · S11 · S13              — viral aralar
S11                         — CENTRAL CHOICE + doruk [D62 · D72]
S0                          — KAPAK ANI'nın kaynağı [PAKETLEME §1]
S13                         — final vuruş + loop karesi
```

---

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      14
SHOT COUNT:      14  ·  sahne içi kesme 0
TARGET ASL BAND: 10.0 s (sabit ızgara — eğri yok, bilinçli sapma)
ASL CURVE:       ①10.0 ②10.0 ③10.0 ④10.0 ⑤10.0
                 ⛔ GEREKÇE SATIRI [D74 · KURGU_RITMI §0②]: bu film sabit
                 ızgaralıdır (sahne = çekim = klip) ve ASL matematiksel olarak
                 sabittir; §1 eğrisi UYGULANAMAZ çünkü kırpma bütçesi yoktur.
                 Ritmi taşıyan şey ASL değil, §2 kadraj içi değişkenlerdir:
                 13 ardışık çiftin 13'ünde ölçek değişir, 2 bilinçli şok
                 (S6→S7, S10→S11), makro kırıcı S3 · S7 · S9 · S12.
GRID:            sahne başlangıcı(n) = 10 s hook + (n−1) × 10 s klip
                 S0 0 · S1 10 · S2 20 · S3 30 · S4 40 · S5 50 · S6 60 ·
                 S7 70 · S8 80 · S9 90 · S10 100 · S11 110 · S12 120 · S13 130
RUNTIME:         140 s = 2:20
RAW FOOTAGE:     14 klip × 10 s = 140 s  ·  TRIM BUDGET: 0 s
                 ⛔ Kırpma tablosu GEREKMEZ: ham = hedef, klip düşürme riski
                 yapısal olarak sıfır [D100 · D101 · KART 11].
SCREEN TEXT:     0.0 saniye
CAMERA:          14 / 14 sabit lockoff  ·  klip içi hareket 0
SETUP SEQUENCE:  A · B · G · D · E · D · G ‖ F · B · G · D · H · B · A
                 A = 32mm EWS eye-level 60 m
                 B = 35mm WS high-angle +25° 18 m
                 G = 50mm MS profile 6 m
                 D = 75mm CU over-the-shoulder 1.6 m
                 E = 100mm macro ECU eye-level 0.8 m
                 F = 24mm EWS overhead +90° 45 m
                 H = 32mm EWS low-angle −25° 25 m
                 ‖ = bölüm kesiği (S6 ↔ S7), Δ2 ölçek + 90° pitch, bilinçli ŞOK
                 kurulum sayısı 7 · ardışık aynı kurulum 0
ANGLE ARC:       6 açı TİPİ (eye-level · high · profile · OTS · macro
                 eye-level · overhead · low) — §2 en az 3 ister ✅
DORUK:           S11 → 1:50-2:00 (sahne başlangıcı 110 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 10 + (n−1) × 10 + promptun TIMELINE ofseti
   BU FİLMDE REPLİK YOKTUR → tablo BOŞTUR ve boş olması bir karardır.
   Formülle doğrulanacak diğer kayıtlar:
     KATALİZÖR   S1 + 2 s ofset  = 10 + 0 + 2   = 12 s  = 0:12   ✅ (≤0:15 kapısı)
     TOHUM       S2 + 6 s ofset  = 10 + 10 + 6  = 26 s  = 0:26   ✅
     TEK KARE    S6 + 4 s ofset  = 10 + 50 + 4  = 64 s  = 1:04   ✅
     ASİMETRİ    S7 + 4 s ofset  = 10 + 60 + 4  = 74 s  = 1:14   ✅
     RED-RİSKLİ  S8 + 6 s ofset  = 10 + 70 + 6  = 86 s  = 1:26   ✅
     DORUK VURUŞ S11 + 4 s ofset = 10 + 100 + 4 = 114 s = 1:54   ✅
     FİNAL VURUŞ S13 + 8 s ofset = 10 + 120 + 8 = 138 s = 2:18   ✅
   Yedi kaydın yedisi de formülle doğrulandı; sapma yok.

FİNAL VURUŞ KANITI [D141]:
   NESNE: geri gelen gri güç hücresi (60 × 40 cm, mat, çizik)
   SANİYE: 138 s (2:18)   ·   KAÇ TANE: 1   ·   BULUNAN mı BULUNMAYAN mı: BULUNAN
   ⛔ tek karede sayılabilir ve adı konabilir: kadrajda tek bir gri kutu,
     alanın önünde, kadının açık avucundan 1 metre ötede.
   ffmpeg -ss 138 -i "$M" -frames:v 1 kanit.jpg   → BAK

DÖNGÜ KANITI: ilk kare (0 s) ↔ son kare (140 s)
   AYNI: kurulum A · 32mm · eye-level · 60 m · yıldız sağ üst dışarıda ·
         mekik sol üçte bir · kabuk sağ üçte iki · ölçek kesri %9 ↔ %8
   FARK: ilk karede kabuğun tamamı hareketsiz ve kadın harekette;
         son karede kabuğun tamamı harekette ve kadın duruyor.
   ⛔ Son karede hareket DURMAZ, poz verilmez, dondurulmaz: kutu hâlâ yolda.
   ⛔ Jenerik/başlık kartı 0 kare [D70 · D72].
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1 1 1 1 1
       (S0 → S13 · 14 sahnenin 14'ünde tam 1 insan · insansız sahne 0)
```

---

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         tam 1 · 14/14 sahne · mürettebat 0 · yansımada ikinci figür 0 ·
              gölgede ikinci figür 0
KASK          kapalı 14/14 · açık 0 sahne · vizör optik berrak, tint 0, ayna
              kaplama 0 · sırt ünitesi YOK — düz siluet, tek sürekli panel [D79]
              vizör içi aydınlatma bloğu yazılı sahneler: S4 · S9 · S13
NOVUM         Kabuğun içine giren her katı cisim hızının tamamını 0,15 saniyeden
              kısa sürede kaybeder ve bulunduğu yerde asılı kalır; çarpma yok,
              sıçrama yok, temas yok. İHLAL EDİLEN KURAL: momentumun korunumu.
              Etki-tepki hâlâ çalışır — iten geri savrulur, itilen durur.
              TAŞIYICI: 30 cm çelik kelepçe × geriye fırlatma jesti (S6 · 1:04)
YERÇEKİMİ     0 g · serbest düşüş · 14/14 sahne · düşen cisim 0 kare
ATMOSFER      vakum · dış ses 0 · duyulan her ses gövdeden iletilir ya da kask
              içindedir · reverb 0 (kuru miks)
KÜTLE ORANI   kelepçe 4 kg · giyimli insan 96 kg · atış 1,2 m/s → geri tepme
              0,05 m/s → klip başına ilerleme ~0,5 m
EKRAN YÖNÜ    mekik HEP screen-left · kabuk HEP screen-right · yıldız HEP
              kadrajın sağ üst köşesi dışında. Kamera 14/14 sahnede eksenin
              aynı tarafında; 180° kuralı hiç geçilmez.
              İlerleme S0-S11 screen-right · dönüş S12-S13 screen-left ·
              yön terslenmesi 0 kare
SAYAÇ         kelepçe: 8 (S1) → 8 (S4) → 7 (S6) → 5 (S7) → 5 (S8) → 2 (S9) →
              0 (S10) → kuşak yok (S12-S13). MONOTONİK, hiç artmaz.
              Metin 0,0 s — sayı yalnız kuşaktaki boş halkalardan okunur.
EŞ KADRAJ     S0 ↔ S13 (kurulum A) · üretim sırası: S0 önce ONAYLANIR, S13 onun
              onaylı karesinden image-edit ile türetilir · fark listesi TAM 3
              madde, bölüm 2 dosyasının S13 başlığında yazılı [D153]
YIPRANMA      3 sabit bölge, göç etmez [D42]:
              ① sol ön kol dış yüzü — 6 cm açık gri sürtünme izi
              ② sağ dizlik — kanca yuvası etrafında koyu gri aşınma halkası
              ③ göğüs plakası sol alt köşe — 3 cm çentik
              Yeni iz eklenmez, mevcut iz büyümez, kir merdiveni YOKTUR.
IŞIK TAKVİMİ  P1 dış (S0·S1·S13) → P2 sınır (S1·S2·S3·S12) → P3 iç
              (S3-S8·S11) → P4 merkez (S9·S10) → P3 (S11) → P2 (S12) → P1 (S13)
              MONOTONİK bir yay: dışarı → içeri → dışarı. Tek baskın kaynak
              14/14 sahnede AYNI yıldız, AYNI yönden (kadrajın sağ üstü
              dışında). İkinci pratik ışık yalnız kask lambası (S4-S11).
              ⛔ Kırmızı acil aydınlatma 0 kare · anamorfik parlama 0 kare
PARÇA SAYISI  kadraj başına yazılı: EWS 240-300 · WS 60-80 · MS 18-24 ·
              CU 6-9 · ECU 2-3. Sahne bazında:
              S0 260 · S1 80 · S2 22 · S3 9 · S4 3 · S5 7 · S6 20 · S7 250 ·
              S8 70 · S9 20 · S10 8 · S11 200 · S12 tüm kabuk · S13 260
ZERRE SAYISI  kask lambası konisinde aynı anda en fazla birkaç düzine, her biri
              ayrı bir nokta, 0,5 m/s, arka yüzey hep görünür kalır [D143].
              Kabuğun içinde serbest zerre 0.
CANLI         0 kare. Filmde uzuv/baş/eklem taşıyan hiçbir varlık yoktur.
              Uzaylı, ekranda YAPTIĞI İŞLE vardır (kural + S13'teki yön),
              anatomi olarak hiç görünmez.
SES REGISTER  HUMAN 0 · MACHINE 0 (replik yok)
              YATAK ENVANTERİ [D83]: kask içi nefes · giysi oda tonu ·
              gövdeden iletilen temas sesleri (halat, metal, toka, kanvas)
              MÜZİKSİZ SAHNE: S10 (müzik 100 s'de tamamen susar, 110 s'de
              döner). Müziksiz ≠ sessiz: yatak ve nefes akmaya devam eder,
              mutlak dijital sıfır 0,0 saniye.
```

---

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> ⬜ DOĞRULANDI satırları üretim makinesinde koşulacak — master gelmeden
> doldurulamaz ve uydurulmaz.

```
KAPI          ⑪ KÖŞE / FİLİGRAN — üretici ikonu hiçbir karede yok [D150]
KOMUT         bash .claude/skills/qa-isle/scripts/olcum_kapisi.sh <master>
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
              ffmpeg -hide_banner -filters | grep -q " cropdetect " || kapıyı yeniden yaz
İKAME         filtre yoksa: dört köşeden 1 s aralıkla kare çıkar, gözle bak

KAPI          KUYRUK KART — son 2 saniyede donmuş kare var mı [D70/72 · D136]
KOMUT         ffmpeg -i <master> -vf freezedetect=n=0.003:d=1.0 -f null -
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
              ffmpeg -hide_banner -filters | grep -q " freezedetect " || kapıyı yeniden yaz
İKAME         son 3 saniyeden 0,5 s aralıkla 6 kare çıkar, farkı gözle ölç
BEKLENEN      0 donmuş kare. Bu filmde son kare HAREKETLİDİR (loop kuralı);
              freezedetect tetiklenirse final yanlış kesilmiştir.

KAPI          IZGARA — süre 140 s ± 2 s, klip sayısı 14
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 <master>
DOĞRULANDI    ⬜ ffprobe <sürüm> · <tarih>
İKAME         yok — ffprobe her kurulumda var

KAPI          SES — mutlak dijital sıfır 0,0 saniye [D83]
KOMUT         ffmpeg -i <master> -af astats=metadata=1:reset=1 -f null -
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
              ffmpeg -hide_banner -filters | grep -q " astats " || kapıyı yeniden yaz
İKAME         silencedetect=n=-90dB:d=0.3 ile tara
BEKLENEN      0 saniye mutlak sessizlik. S10'da müzik susar ama yatak akar.

KAPI          FİNAL VURUŞ KANITI — 2:18'de gri kutu kadrajda ve tek [D141]
KOMUT         ffmpeg -ss 138 -i <master> -frames:v 1 kanit_2-18.jpg
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
İKAME         yok — kare çıkarma her kurulumda var
BEKLENEN      tek bir gri kutu, alanın önünde, açık avuçtan ~1 m ötede

KAPI          DÖNGÜ KANITI — ilk kare ↔ son kare aynı kurulum
KOMUT         ffmpeg -ss 0 -i <master> -frames:v 1 loop_ilk.jpg
              ffmpeg -sseof -0.1 -i <master> -frames:v 1 loop_son.jpg
DOĞRULANDI    ⬜ ffmpeg <sürüm> · <tarih>
İKAME         yok
BEKLENEN      aynı lens sınıfı, aynı ölçek, aynı ışık yönü, aynı ekran yönü;
              tek fark hareketin hangi tarafta olduğudur
```

---

## 🧾 ÜRETİM ÖNCESİ NOT — PROMPT KAPISI

```
⛔ TEK KARE ÜRETİLMEDEN ÖNCE (AGENTS Kart P):
   python3 kilavuzlar_ve_sistem_dosyalari/PROMPT_KONTROL/prompt_kontrol.py \
           yatay_2_4_dk_filmler_uzay/THE_STILL_SWARM
   ⛔ FİLM KLASÖRÜ verilir, tek bölüm dosyası değil. Çıktıda
     `📁 FİLM KLASÖRÜ · n bölüm dosyası birleşik` satırı yoksa kapı koşmamıştır.
   Ardından: PROMPT_KONTROL/PROMPT_QA_CRITIQUE_PROMPT.md (insan yarısı —
   kompozisyon ekseni betiğe inmez).
```
