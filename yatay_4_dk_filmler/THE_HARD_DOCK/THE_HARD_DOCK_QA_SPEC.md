# 📋 THE_HARD_DOCK — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz. Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar ve BU dosyayı
> rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_HARD_DOCK_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister.
> SPEC onun YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı
> (insan repliği 0 · sabit lockoff · vakumda dış ses 0 · metinsiz sayaç · port-kilitli
> kamerada arka planın kayması · sentetik makine sesi) ihlal olarak yazılamaz.

> **Revizyon 11.09.2026:** ilk taslak dosyanın başında sahipsiz bir kask cümlesi
> taşıyordu, KÜME 0 / DÖNÜŞ 1 yazıyordu (iskelet A A B B ile çelişki), insan şeridi
> 22 karakterdi ve vizörü opak ilan ediyordu. Hepsi PLAN'ın revize hâliyle hizalandı.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]: YERÇEKİMİ · ATMOSFER · IŞIK TAKVİMİ
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_HARD_DOCK
FORMAT:            yatay 3-5 dk (§2.3) · 16:9
RUNTIME:           240 seconds (title card: none — screen text lock 0 s)
SCENE COUNT:       24
THEME:             İNSAN-MAKİNE — makine hayatta kalma optimumunu hesaplar ("dön"), insan bedeli göze alır ("kal")
THEME SCENES:      S03 · S06 · S10 · S15 · S17 · S19 · S24
INTENDED EMOTION:  tutulan nefes; prosedürel gerilim, sonunda sessiz ve pahalı bir rahatlama
ENDING TYPE:       KAFİYE — S02 ↔ S24 aynı kurulum (B): pencerede dönen küçük istasyon ↔ pencereyi dolduran sabit port; eller kumandada ↔ eller uylukta
PROTAGONIST:       Astronot (isimsiz — özel ad promptta geçmez [D34]; kadın, ~40, geniş omuzlu, koyu kahverengi ten)
CENTRAL CHOICE:    S19 · 3,0-4,0 s — sağ eldiven iptal barına DEĞİL, çizgili koruma kapağına gider ve kapağı kaldırır; iptal barı kadrajda dokunulmamış kalır
COST:              S22 · 6,0 s — dört kenetlenme dikmesi sonuna kadar çöker (gemi bir daha ayrılamaz); adı S24 · 2,0 s'de makine tarafından konur
DIALOGUE LINES:    8 · register: HUMAN 0 / MACHINE 8 (gemi bilgisayarı MIRA, akuzmatik, bedenleştirme YOK)
SILENT SCENES:     17 (S01 S04 S05 S07 S08 S09 S11 S12 S13 S14 S16 S18 S19 S20 S21 S22 S23)
VIRAL INTERSTITIALS: S01 · S14 · S22 · S23 · S24   ⛔ THESE MAY NOT BE CUT
TITLE:             THE HARD DOCK — "sert kenet": halka nominal hızın beş katıyla porta sürülür ve geri alınamaz biçimde kilitlenir
LIBRARY CONTEXT:   THE_COLD_BURN · THE_BLACK_CRADLE (yanaşma hattı) · THE_COUNTED_TURN · THE_AMBER_LATTICE
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 0
TARGET ASL BAND: 10 s sabit   ASL CURVE: düz — 24 × 10 s
                 GEREKÇE [D74]: format kartı §2.3 sabit 10 s ızgara; küme sahneleri (S14-15 · S22-23)
                 kesme sayısını 23'ten 21'e düşürür, ızgarayı değiştirmez
GRID:            sahne başlangıcı(n) = 0 hook + (n−1) × 10 s   (hook ayrı sahne değil; S01 hook'tur)
RUNTIME:         240 s (04:00)
RAW FOOTAGE:     240 s · TRIM BUDGET: 0 s
SCREEN TEXT:     0 saniye
CAMERA:          7 kurulum, hepsi sabit lockoff · 24 · 32 · 35 · 50 · 85 mm küresel (anamorfik 0)
SETUP SEQUENCE:  A B C B A E A B C D C B A F F G B C D C B G G B   (PLAN'daki KURULUM İSKELETİ ile aynı)
KÜME:            2 · S14-S15 (F tepe) · S22-S23 (G port-kilitli)   [12+ sahnede ≥2 ✓]
DÖNÜŞ:           11/24 = %46   (S04 S05 S07 S08 S11 S12 S15 S20 S21 S23 S24)   [≥%40 ✓]
ANGLE ARC:       6 açı tipi — göz hizası frontal (A·G) · OTS (B) · alt açı (C) · profil (D) · üst açı (E) · tepe (F)
DORUK:           S22 → sert kenet, temas 6,0 s (sahne başlangıcı 210 s · temas 216 s)

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(S_n) = 0 + (n−1) × 10 + TIMELINE ofseti
   #1 S02 · ofset 3,0 → 013 s (00:13)   "Station wobble confirmed. One full cycle every forty-eight seconds."
   #2 S03 · ofset 3,0 → 023 s (00:23)   "Relay carrier lost."
   #3 S06 · ofset 3,0 → 053 s (00:53)   "Coronal flux rising. Sensor confidence fifty percent."
   #4 S10 · ofset 3,0 → 093 s (01:33)   "Capture window six seconds per cycle."
   #5 S15 · ofset 3,0 → 143 s (02:23)   "Sensor confidence zero. Guidance withdrawn."
   #6 S17 · ofset 3,0 → 163 s (02:43)   "Abort approach. Return burn available for ninety seconds."
   #7 S24 · ofset 2,0 → 232 s (03:52)   "Hard capture confirmed. Release struts destroyed."
   #8 S24 · ofset 7,0 → 237 s (03:57)   "Relay carrier restored."
   (formülle doğrulandı 11.09.2026 — sekiz kayıt da tutuyor)

ÇAPA ÜÇLÜSÜ [OYUNCULUK_YAZIM §2 · ⑩ mod D ANCHOR BEATS]:
   CHOICE  S19 · 184 s (klip 4,0 s)  BEFORE: sağ eldiven T-kolda kapalı, kapak KAPALI
                                     AFTER:  sağ eldiven kapak yuvasında, kapak AÇIK, parmak düğmede; iptal barı yerinde
   COST    S22 · 216 s (klip 6,0 s)  BEFORE: dört dikme tam boy, yaka yuvarlak
                                     AFTER:  dört dikme çökük, yaka bükük, gemi hareketsiz
   FINAL   S24 · 237 s (klip 7,0 s)  BEFORE: iki eldiven kumandalarda, omuz yüksek
                                     AFTER:  iki eldiven açık uyluklarda, omuz inik
   DAVRANIŞ ŞERİDİ (insanlı sahneler): S02 G · S03 R · S04 S · S08 G · S09 G · S10 G · S11 T · S12 D ·
                                       S17 R · S18 T · S19 K · S20 B · S21 G · S24 R
   REPLİK: 8/8 cevapsız (makine söyler, insan cevap vermez — tasarım) · dinleyen kadrajı: sırt (B) / yüz ağzı kapalı (C) / el (D)

FİNAL VURUŞ KANITI [D141]:
   DÖRT gösterge lambası YANIK · 237 s (S24 · 7,0 s) · 4 tane · BULUNAN   (S01-S23'te yanan lamba 0)
   ikinci kanıt: iptal barı DİK ve dokunulmamış · aynı kare · 1 tane · BULUNAN
   ffmpeg -ss 237 -i "$M" -frames:v 1 kanit.jpg   → BAK
DÖNGÜ KANITI: S02 (010 s) ↔ S24 (230 s) — aynı kurulum B · aynı ölçek · aynı kabin ışığı · jest: eller kapalı ↔ eller açık
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  -111---11111----11111--1     (24 · 1 = pilot kadrajda · - = dış/insansız)
       S01 - · S02-S04 1 · S05-S07 - · S08-S12 1 · S13-S16 - · S17-S21 1 · S22-S23 - · S24 1
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

```
İNSAN         1 — kadın, ~40, geniş omuzlu, koyu kahverengi ten; kadrajda 0 ya da 1, hiçbir karede 2
KASK          24/24 takılı ve mühürlü · vizör TEK DÜZ PANEL, görünür koyu-gri çerçeve içinde — kubbe DEĞİL ·
              0 ton · 0 ayna · 0 çevre yansıması · üst kenarda TEK parlama çizgisi · yaka halkası görünür ·
              yüz her açıda okunur [D79 · D95 · D146 · D197 tek kilit] · sırt ünitesi YOK — düz panel [D139]
NOVUM         yalpalayan istasyona yumuşak kenet imkânsız; halka nominalin 5 katıyla (0,5 m/s) porta sürülür →
              4 dikme dibe vurur, yaka bükülür, kilit geri alınamaz. İhlali: gemi bir daha ayrılamaz.
YERÇEKİMİ     0 g (kabin içi ve dış)
ATMOSFER      0 Pa dış (vakum: dış ses 0, gölge mutlak siyah, dolgu 0) · kabin basınçlı ama giysi mühürlü
EKRAN YÖNÜ    dış yan görünüşte (E) gemi SOLDA, istasyon SAĞDA, burun sağa · burun kamerasında (A) istasyon merkez,
              burun istasyona · port-kilitli (G) gemi burnu KAMERAYA · 24/24 sabit
SAYAÇ         gösterge lambası: S01-S23 yanan 0 · S24 yanan 4 (dikme başına bir) — tek adım, monotonik
              koruma kapağı: S01-S18 KAPALI · S19 (3,0 s) → S24 AÇIK — tek yönlü
              dikme durumu: S01-S22 (6,0 s) UZUN · S22 (6,0 s) → S23 ÇÖKÜK — tek yönlü
EŞ KADRAJ     S02↔S04↔S08↔S12↔S17↔S21↔S24 (B birebir) · S03↔S09↔S11↔S18↔S20 (C) · S10↔S19 (D) · S01↔S05↔S07↔S13 (A) · S16↔S22↔S23 (G)
YIPRANMA      0 sabit bölge — kabin içi, kir/toz 0; giysi 24/24 temiz [D42: sıfır da bir kilittir]
IŞIK TAKVİMİ  değişim YOK (monotonik değil, SABİT): güneş istasyonun arkasında, eksenin ~30° üstünde, kadraj dışı ·
              gemi tarafından istasyon ARKADAN ışıklı · port tarafından gemi ÖN-ÜSTTEN · gezegen turuncusu alttan ·
              kabinde tek beyaz lamba + alçaktan turuncu [D201 · D193 riski yok]
              ⚠️ G kurulumunda (S16 S22 S23) ARKA PLAN KAYAR — kamera istasyonla döner; bu ihlal değil kanıttır
SES REGISTER  HUMAN 0 · MACHINE 8 (düz sentetik, kabin hoparlörü/telsiz) · temasta dış ses 0 [YANASMA §2.1]
İSTASYON      salınım 48 s/tam koni (10 s'de ~1/5 daire) · hız SABİT · yaka SEKİZGEN · kendi mandalları bükük güdük ·
              screen-left kol kopuk · gemi/istasyon 1/20
GEMİ          halka dikme sayısı TAM 4 · nominal kapanma 0,1 m/s (klipte ~bir halka eni) · sert kenet 0,5 m/s
              (S22: 6 s'de ~dört halka eni) · temas: tek oturma, bir el genişliği, sekme 0
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

```
KAPI          port-kilitli kamerada yaka KIMILDAMAZ (S22 · S23): ön plan bölgesinde kare-arası fark ~0
KOMUT         ffmpeg -ss 210 -t 20 -i "$M" -vf "crop=iw*0.30:ih*0.35:0:ih*0.65,signalstats" -f null - 2>&1 | grep -c "YDIF"
              → sahne_kapisi.sh ile birlikte okunur: ön plan kırpımında YDIF ortalaması eşik altı olmalı (eşik ölçümle konur)
DOĞRULANDI    ffmpeg 8.1 · 11.09.2026 — `ffmpeg -hide_banner -filters | grep -q " signalstats "` ✓ · `" crop "` ✓
İKAME         signalstats yoksa: `freezedetect` ön plan kırpımına (ffmpeg 8.1'de VAR ✓); o da yoksa iki karenin gözle kıyası

KAPI          klip başı/sonu donma ve kuyruk kart (24 klip)
KOMUT         bash .claude/skills/qa-isle/scripts/sahne_kapisi.sh "$M" 10 24
DOĞRULANDI    freezedetect ffmpeg 8.1 · 11.09.2026 ✓
İKAME         `ffmpeg -i "$M" -vf "select='gt(scene,0.3)',showinfo" -f null -` kesme sayısı = 23 (küme kesmeleri dâhil 23 sınır)

KAPI          final kanıt karesi — dört lamba yanık
KOMUT         ffmpeg -ss 237 -i "$M" -frames:v 1 kanit_S24.jpg   → gözle: yanan lamba sayısı 4, iptal barı dik
DOĞRULANDI    ffmpeg 8.1 · 11.09.2026 ✓ (temel çıkarım, filtre yok)
İKAME         —
```
