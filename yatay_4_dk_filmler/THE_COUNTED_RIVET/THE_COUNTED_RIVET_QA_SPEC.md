# 📋 THE_COUNTED_RIVET — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

> ⛔ **RUBRİKLE BİRLİKTE YAPIŞTIRILIR [Ders 129].** Yapıştırılmadıysa koşu ön
> koşu değil **YAPILMAMIŞ koşudur**: ham rapor arşive düşer, T tablosuna satır
> yazılmaz, kesme listesi ve REMOVE reçetesi uygulanmaz.
> ⛔ 11.09.2026: filme özel PAKET KALDIRILDI (`QA_PROMPTLARI/FILME_OZEL/` ve
> `rubrik_paketle.sh` silindi). Operatör `QA_PROMPTLARI/_KAYNAK/` rubriğini açar
> ve BU dosyayı rubriğin BAŞINA yapıştırır. Mod D'yi taşıyan tek şey budur.

> 🧩 **⑬ UYUM MERCEĞİ İÇİN:** bu SPEC tek başına yetmez — o mercek ayrıca
> `THE_COUNTED_RIVET_URETIM_DEFTERI.md`'yi ve `sahne_kapisi.sh` çıktısını ister. SPEC onun
> YANLIŞ-POZİTİF DUVARI'dır: burada İLAN EDİLEN tasarım kararı (0 replik · sabit
> lockoff · tasarımlı sessizlik · metinsiz sayaç) ihlal olarak yazılamaz.

> ⛔ **Dosya adı `*_QA_SPEC.md` KALIR.** `sayac.sh` ve `rapor_kontrol.py` bu
> deseni arar; ad değişirse ikisi birden körleşir.

> ⚠️ **DİKEY FİLM BAŞLIĞI UYGULANMAZ** — bu film yatay 16:9.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → C BLOĞU + B'nin INTRA-SCENE CUTS satırı   MOD D
③ 🔊 SES         → A'nın DIALOGUE LINES + C'nin SES REGISTER  MOD D
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]: DÜNYA ÇAPASI · IŞIK TAKVİMİ · ATMOSFER
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
⑦ 🎯 AKSİYON · ⑧ 💪 EFOR → A + C BLOĞU (çıkarım)   MOD D
⑨-⑫ plan sadakati → A + C + E BLOĞU                MOD D (mod V GEÇERSİZ)
⑬ 🧩 UYUM        → SPEC + klip promptları + üretim defteri + sahne_kapisi (mod V YOK)
⑭ 🧍 HAREKET     → A (sahne haritası) + C HAREKET KİLİDİ     MOD D
⑮ 🧭 YÖN         → C EKRAN YÖNÜ + A                          MOD D
② ③ ⑤'in FLAGS soruları koşudan SONRA C BLOĞU'ndan cevaplanır.
⛔ ② ve ③ bu filmde MOD D koşar — tasarım gereği "hiçbir şey verilmez" DEĞİL:
   çok klipli sahne rejiminde sahne İÇİ kesmeler var ve devamlılık kilidi
   ölçülebilir (aşağıdaki INTRA-SCENE CUTS satırı).
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_COUNTED_RIVET
FORMAT:            horizontal 16:9 · 4 minutes (§2.3 card)
RUNTIME:           240 seconds (title card: NONE — screen text lock 0 s)
SCENE COUNT:       7          ⛔ SCENE COUNT ≠ CLIP COUNT (multi-clip scene regime)
PART GRID:         — (2 bölüm dosyası YAZIM birimidir, QA birimi DEĞİL: 4 dk hattında
                   QA tek master üzerinde koşar [§2.3]. B1 = K01-K12 / S1-S4 · 0-120 s ·
                   B2 = K13-K24 / S5-S7 · 120-240 s. BOUNDARY PAIR: K12|K13 — G(MS·OTS)
                   → H(CU·profil), 1 ölçek kademesi + 90°, elle kareyle kapanır)
THEME:             HUMAN AND MACHINE — a machine can only see magnitudes its
                   catalogue has a name for; a human chooses to measure one it
                   has no name for, and pays for it
THEME SCENES:      S3 · S5 · S6 · S7        ⛔ en az üç ✅
INTENDED EMOTION:  being proved right and paying for it in the same breath
                   (double emotion: vindication + the cost of vindication)
ENDING TYPE:       OPEN / COST PAID — she is right, the surface has no edge,
                   and the platform is going down with her on it
PROTAGONIST:       a mooring technician (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    K14 · S5 — she hauls the lacing cord out of the platform's own
                   acid cover to free a longer straight edge (2:10-2:20)
DIALOGUE LINES:    0 · register: HUMAN 0 / MACHINE 0
                   ⛔ 24/24 promptta tırnak 0 karakter · `No dialogue.` her AUDIO satırında
SILENT SCENES:     0 — planlı MUTLAK sessizlik YOK; AUDIO satırı hiçbir klipte boş değil [D180]
VIRAL INTERSTITIALS: 0  ⛔ kartın dört adedinden SAPMA [D74] — kapı iki kanalı
                   birden istiyor (okunan yüz + hızlanan hacim) ve bu estetikte
                   ikisi tek klipte birleşmiyor; üç aday ölçüldü, gerekçe
                   `00_ANALIZ/03_SAHNE_SIRALAMASI.md` §2.4
TITLE:             THE COUNTED RIVET — başlık izleyiciye nereye bakacağını
                   söylüyor: perçine. Sayılan şey ölçünün kendisidir.
LIBRARY CONTEXT:   aynı ortam kartı §3.6 → LOSS_OF_LIFT (kaldırma KAYBEDİLİR;
                   burada kaldırma bir ÖLÇÜ BİRİMİDİR) · ölçek/keşif →
                   THE_TALL_SHORE (ölçeği manzarayla gösterir; burada büyük
                   şeyin SINIRI hiçbir karede görünmez, yalnız ölçüsü görünür)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ  (① KARE'ye A ile birlikte)

```
CLIP COUNT:      24
SHOT COUNT:      24 · sahne içi kesme 17
SCENE PLAN:      SAHNE PLANI: 1 3 4 4 3 4 5   (toplam 24 = CLIP COUNT)
                 S01 = K01 · S02 = K02-K04 · S03 = K05-K08 · S04 = K09-K12 ·
                 S05 = K13-K15 · S06 = K16-K19 · S07 = K20-K24
INTRA-SCENE CUTS: K02|K03 · K03|K04 · K05|K06 · K06|K07 · K07|K08 · K09|K10 ·
                 K10|K11 · K11|K12 · K13|K14 · K14|K15 · K16|K17 · K17|K18 ·
                 K18|K19 · K20|K21 · K21|K22 · K22|K23 · K23|K24
                 — these cuts are INSIDE one scene: location, light, sound bed,
                 costume dirt, held object and body pose MUST match across them;
                 a reset here is a ② CONTINUITY defect, not a scene change.
                 Each second-and-later clip carries a `CONTINUOUS ACTION:` line
                 stating the previous clip's end state — that line is the contract.
TARGET ASL BAND: 10,0 s   ASL CURVE: NONE — flat grid
                 ⛔ GEREKÇE [D74]: film bir ÖLÇÜM işidir ve ritmi makinenin
                 sabit periyoduna karşı kurulur; kesme hızını değiştirmek
                 makinenin sabitliğini görünmez kılardı. Hızlanma duygusu
                 kesmeden değil SAYAÇTAN gelir (perçin sırası 40 → 25 → 18 s).
GRID:            klip(n) başlangıcı = (n−1) × 10,0 s   ·   hook = K01 = 0,0 s
                 ⛔ hook 24'ün İÇİNDE, ek klip değil
RUNTIME:         240,0 s
RAW FOOTAGE:     240,0 s · TRIM BUDGET: 0 s (sabit ızgara, kırpma yok)
SCREEN TEXT:     0 saniye
                 ⛔ LOSS_OF_LIFT 8. vakası: prompt yasağı 25/25 tuttu, kurgu
                 masasında 5 s başlık kartıyla delindi. Kapak çıktısı AYRI
                 dizinde durur ve kurgu klasörüne girmez.
CAMERA:          24 / 24 sabit lockoff — klip içi hareket 0
SETUP SEQUENCE:  K01 B · K02 F · K03 A · K04 F · K05 E · K06 F · K07 A · K08 G ·
                 K09 E · K10 F · K11 E · K12 G · K13 H · K14 F · K15 H · K16 E ·
                 K17 F · K18 B · K19 D · K20 B · K21 C · K22 B · K23 C · K24 B
KURULUM İSKELETİ: B F A F E F A G E F E G H F H E F B D B C B C B
                 ⛔ PLAN'daki ile BİREBİR aynı · ardışık aynı kurulum 0
KÜME:            ARANMAZ — çok klipli sahne rejiminde küme yoktur (son kare
                 zinciri 22.09.2026'da kaldırıldı); ⑩④ KÜME hedefi bu filmde düşer
DÖNÜŞ:           14 / 24 = %58,3 (hedef ≥%40 ✅)
                 K04 K06 K07 K09 K10 K11 K12 K14 K15 K17 K20 K22 K23 K24
ANGLE ARC:       5 açı TİPİ (göz hizası · alt açı · üst açı · OTS · profil) — §2 ≥3 ✅
                 ardışık çift 23/23 bant içi (≥1 ölçek kademesi VE ≥45°) · bant dışı 0
                 bilinçli ŞOK 1: K15→K16 (H→E · 2 kademe · 160°) — ölçümden dünyaya dönüş
DORUK:           K21 · S7 → 200,0-210,0 s (dokuz mandalın beşi kesilmiş)

REPLİK ZAMANLARI: — (0 replik; formül koşmaz)

FİNAL VURUŞ KANITI [D141]:
   nesne: KESİLMİŞ MANDAL BOYUNLARININ UÇLARI · saniye: 234,0 (K23'ün 4,0 s'i) ·
   kaç tane: 9 · BULUNAN
   ⛔ Tek karede SAYILABİLİR olmak zorunda: dokuz uç güverte kenarı boyunca
      eşit aralıklı bir sıra; C kurulumu (35mm · 2,0 m · üst açı 15°) kadraj
      eni 2,06 m — dokuz uç 1,00 m aralıkla sığmaz, bu yüzden uçlar güverte
      kenarında 0,20 m aralıklı bir sırada durur ve dokuzu birden kadrajda.
   ffmpeg -ss 234 -i "$M" -frames:v 1 kanit_final.jpg   → BAK: dokuz uç sayılıyor mu
DÖNGÜ KANITI: K01 (0,0-10,0 s) ↔ K24 (230,0-240,0 s)
   aynı kurulum harfi (B) · aynı ölçek (CU) · aynı ışık (kademe farkı BİLİNÇLİ:
   0 → 2) · aynı iki eldiven · aynı mandal çenesi · TERS jest (kapatır ↔ kesilmiş)
   ⛔ Kamera cümlesi BİREBİR aynı; K24'ün dönüş işareti K22'yi DEĞİL K01'i
      gösterir — kafiye budur [D210].
   ffmpeg -ss 5 -i "$M" -frames:v 1 kanit_k01.jpg ; ffmpeg -ss 235 -i "$M" -frames:v 1 kanit_k24.jpg
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN:  1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
       (24 hane · 1 = insan var · - = insansız · klip başına bir hane)
⛔ İNSANSIZ KLİP 0 — 24/24 klipte en az eldivenler kadrajda. Risk kartı 10
   (yapısal red profili) bu filmde YAPISAL OLARAK KAPALI.
⚠️ LOSS_OF_LIFT'in ölçülmüş açığı: şerit sayıyı ve süreyi geçirir ama SIRAYI
   geçirmez. Bu filmde şerit 24 hanenin 24'ü `1` olduğu için sırayı ölçemez;
   sırayı ölçen şey aşağıdaki DAVRANIŞ ŞERİDİ ve ANCHOR BEATS saniyeleridir.
```

### 🎭 DAVRANIŞ ŞERİDİ — sıra kilidi, insan şeridinin yerine

```
K   01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
    İ  İ  Ç  R  R  Ç  R  K  R  S  R  K  K  B  N  S  S  R  R  K  Ç  Ç  K  R
İ = iş (istek icra) · Ç = çaba (yük altında) · R = tepki (gövde ödemesi) ·
S = sayım (sayaç ilerler) · K = karar (jest değişir) · B = bedel · N = novum kanıtı
⛔ Ardışık dört hanenin dördü aynı harf OLAMAZ; bu filmde en uzun dizi 2.
```

### ⏱️ ANCHOR BEATS — saniye cinsinden, kareyle doğrulanabilir

```
  0,0- 10,0  K01  hook: çene kapanıyor, içindeki yüzey kavis yapmıyor
 24,0- 30,0  K03  katalizör (%12,5 bandı 24-36 s ✅) — ikinci kazık ve süre baskısı
 50,0- 60,0  K06  ikinci ölçüm, aynı sonuç — 50 px'lik TARTIŞILIR boşluk yok
110,0-120,0  K12  orta nokta (%50) — makinenin kaydına karşı kendi ölçüsüne gitmek
130,0-140,0  K14  MERKEZÎ SEÇİM + BEDEL aynı karede (2:10-2:20)
144,0-150,0  K15  NOVUM KANITI — şeridin altında hiçbir yerde ışık yok
180,0-190,0  K19  her şeyin kaybı (%75-79) — sayı bulundu, karar alındı
200,0-210,0  K21  DORUK
230,0-240,0  K23-K24  FİNAL VURUŞ (234,0) + kapanış imajı
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını ve ⑩ ÖNERME
> KAPISI'nı besler: kaynağı burada YAZILI olan bulgu DÜŞER.

```
İNSAN         1 — her promptta rakamla ("Exactly one human character") ·
              duplikasyon 0 · yansıyan insan 0 kare · ikinci figür 0 kare
KASK          vizör optik BERRAK, tek DÜZ pane + görünür KALIN koyu çerçeve +
              derin yaka halkası · 24/24 klipte KAPALI, ara durum 0 ·
              sırt ünitesi YOK — düz siluet [D79] · `seamless · bubble · dome ·
              sphere` 0 kez · amblem 0 · yama 0 · rakam 0
              ⚠️ REFERANS PANELİ ÜRETİLMEDİ (sahip kararı) — bu kilidin tek
              ölçülmüş aracı kapalı; biçim sapması görülürse ② bulgusu MEŞRU
NOVUM         Bağlandığı yüzey bir gövde değil, gövdenin bir DETAYIDIR — ve
              bunu yalnız düz bir kenarın altından ışık sızıp sızmadığı söyler.
              İHLAL: mandalın çenesi bir DİREK kavramak için yapılmıştır ve
              kavradığı şey hiçbir yerde kavis yapmaz.
              TAŞIYICI: çelik şerit (kol boyu, düz kenarlı) × şeridi yüzeye
              yatırma jesti → şeridin altından hiçbir yerde ışık sızmıyor
              İKİNCİ TAŞIYICI: perçin başı × eldivenin yanına konması
              İHLAL SAYISI: 1 (perçin ve sürüklenme aynı ihlalin 2. ve 3. KANITI)
              ARİTMETİK: sagitta s ≈ c²/8R · kenar 0,60 m · 2 m çaplı direkte
              45,0 mm = 267 px (H kurulumu, H 0,304 m) · gerçek yüzeyde
              R ≈ 15 km → 0,003 mm = 0 px. KABUL EŞİĞİ: boşluk hiçbir yerde
              2 cm = 142 px'ten geniş değil. KARŞIT KARE: K15'in 0,0 s'inde
              aynı şerit bir PERÇİN BAŞININ kubbesine yatırılır ve altında
              iki eldiven kalınlığında ışık VARDIR — alet çalışıyor, yüzey düz.
YERÇEKİMİ     0,904 g — 24/24 promptta AYNI sayı, tek değer [D200]
              bırakılan nesne: eldiven boyu ≈ 0,33 s (K04 çekiç · K14 bağ)
ATMOSFER      yoğun karbondioksit, ≈ yarım Dünya atmosferi, 55 km bandı ·
              nötr yüzerlik GERÇEK (Arşimet) → gövde havada DURUR, POZİTİF
              kuralla yazılı · bağıl rüzgâr 0 → kumaş kıpırdamaz, hiçbir şey
              savrulmaz · ufuk YOK · zemin YOK · güneş diski 0 kare · toz 0
EKRAN YÖNÜ    hedef hep PLAKA (kadrajın üstü) · ilerleme güverte kenarı boyunca
              FRAME RIGHT (K08 · K12 · K21 cümlelerinde yazılı) · eksen çizgisi
              güverte kenarı · 24/24 klipte sabit · pusula yok, yalnız
              screen-left / screen-right
HAREKET KİLİDİ eller: iki eldiven her klipte kadrajda, tek jest kuralı (bir klipte
              bir iş) · ayaklar: yük altında arka bot yüklenir (K03 · K13 · K20 ·
              K22) · baş: kask yalnız hedefe döner, dolgu hareketi 0 ·
              ALIŞKANLIK: mandalı kapatmadan önce çeneyi iki parmakla iki kez
              yoklamak (S2 · S3 · S6) — S5'te KIRILIR
SAYAÇ         ÜÇ metinsiz sayaç, üçü de MONOTONİK, hiçbirinde rakam yok:
              ① KANIT MERDİVENİ  K01 (0,30 m çene, boşluk yok, belirsiz) →
                 K06 (aynı çene, aynı sonuç, ikinci kez) → K15 (0,60 m şerit,
                 boşluk yok, tartışmasız)
              ② İNİŞ HIZI  perçin sırasının güverte kenarından geçme süresi:
                 K09 ≈ 40 s → K11 ≈ 25 s → K16 ≈ 18 s
              ③ IŞIK TAKVİMİ  kubbe okra kademesi 0 (S1-S5) → 1 (S6) → 2 (S7)
EŞ KADRAJ     K01 ↔ K24 (B kurulumu · aynı çene · ters jest)
              ikincil: K13 ↔ K15 (H kurulumu) · K09 ↔ K11 ↔ K16 (E kurulumu)
DÜNYA ÇAPASI  3/3 — ① üstte kaynaksız parlak okra kubbe, güneş diski 0 ②
              aşağıda okra derinlik, ufuk çizgisi YOK, zemin YOK ③ yer imi
              PLAKANIN KENDİSİ ve bir perçin başı (omuz genişliğinde)
              ⛔ Üçü 24/24 promptta BİREBİR aynı cümlelerle; sıfır sapma.
              ⚠️ UYARLANDI [D209]: kartın ufku ve zemini yok, bu yüzden
              "gök · ufuk · yer imi" üçlüsü yukarıdaki üçlüye çevrildi;
              gerekçe `00_ANALIZ/02_KONSEPT_VE_RISK.md` §2
YIPRANMA      2 sabit bölge [D42]: ① global fabrika matı + eklemlerde ince okra
              toz (K01'den, film boyu) ② sağ eldivenin manşet halkasında iki
              parmak genişliğinde mat aşınma (K15'ten, GERİ DÖNMEZ)
              ⛔ Hiçbir klipte temizlenmez, hiçbir klipte yeni leke eklenmez.
KİMLİK DİZİSİ kask: KKKKKKKKKKKKKKKKKKKKKKKK (24 hane, hepsi KAPALI) ·
              amblem: YOK (0 yama, hiçbir omuzda) · giysi rengi: mat kurşun grisi ·
              renk bandı: okra, SOL pazu ve SOL uylukta 360° sarılı ·
              kir bölgesi + başlangıç: manşet aşınması, K15 · hasar başlangıç:
              örtünün açık kenarı ve üstündeki mat kabarma, K14 (geri dönmez) [D208]
              ⛔ KİMLİK YIĞINI 3 öznitelik: cinsiyet · göreli boy · yapı.
                 Ten rengi · yaş · saç biçimi · kesin boy 24/24 promptta 0 [D167]
              ⛔ Yüz YALNIZ K19'da kadrajda (D kurulumu · 85mm · ECU); kalan
                 23 klipte yüz cümlesi YOK [D214 · D16]
IŞIK TAKVİMİ  MONOTONİK — 0 → 1 → 2, yalnız sahne SINIRINDA değişir (S5→S6 ve
              S6→S7), klip içinde asla, geri açılmaz
              ⚠️ UYARLANDI [D193]: yön ve Kelvin YOK (güneş diski ve gölge yok);
              takvim TEK PARLAKLIK DİZİSİ olarak yazıldı
SES REGISTER  HUMAN 0 · MACHINE 0 — film bilinçli SESSİZ
              Muhatap KONUŞMAZ: bağlama otomasyonu ① sabit periyotlu (4,0 s)
              tek kehribar lamba ② mandalı yeniden germe ile cevap verir.
              Lamba periyodu film boyu DEĞİŞMEZ ve K24'te de aynıdır — tema-final.
              ⛔ Oda tonu her kesmede ≥0,2 s köprülenir · dijital sıfır 0 kare
```

## 🅴 E BLOĞU — MAKİNE KAPILARI  [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR** —
> bir SPEC'in kamera sabitlik kapısı kurulu olmayan bir filtreye yazılmıştı ve
> sessizce hiç koşmadı. Aşağıdaki beş kapı bu makinede DENENDİ (kuru koşu).

```
E1 KAPI       SÜRE — master planlanan 240,0 s mi (kırpma bütçesi 0)
   KOMUT      ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
   DOĞRULANDI ffmpeg 8.1 · 25.09.2026 · ffprobe mevcut
   İKAME      yok gerekmiyor
   EŞİK       240,0 ± 0,5 s · sapma varsa eksik klip aranır [FROST_LINE: 2 klip eksik]

E2 KAPI       KLİP SÜRESİ — ızgara gerçekten 10,0 s mi [D124]
   KOMUT      ffprobe -v error -show_entries format=duration -of csv=p=0 <tek klip>
   DOĞRULANDI ffmpeg 8.1 · 25.09.2026
   İKAME      yok
   EŞİK       ⬜ ARAÇTAN ÖLÇÜLECEK — plan 10,0 s ile yazıldı; ölçüm üretim
              defterinin motor satırına yazılır. ⛔ Ölçüm 8 s çıkarsa RUNTIME
              192 s olur ve A bloğunun RUNTIME satırı düzeltilir, plan değil.

E3 KAPI       KAMERA SABİTLİĞİ — 24/24 klip gerçekten lockoff mu
   KOMUT      ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=-60dB:d=2" -f null - 2>&1 | grep freeze
   DOĞRULANDI ffmpeg 8.1 · 25.09.2026 · `freezedetect` filtresi VAR
   İKAME      signalstats YDIF ortalaması klip başına ölçülür
   EŞİK       Kadraj donmasını DEĞİL, kamera kaymasını arıyoruz: freezedetect
              hiç tetiklenmemeli (kadrajda her zaman hareket var) ama
              KENAR akışı olmamalı. ⛔ Kesin ölçüm gözle: her klibin 0,0 s ve
              9,5 s karesi üst üste konur, kadraj kenarı birebir aynı olmalı.
              ffmpeg -ss <t> -i "$M" -frames:v 1 a.jpg ; ffmpeg -ss <t+9.5> -i "$M" -frames:v 1 b.jpg

E4 KAPI       EKRAN METNİ / BAŞLIK KARTI — 0 saniye mi
   KOMUT      ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.2:pic_th=0.98" -f null - 2>&1 | grep black
   DOĞRULANDI ffmpeg 8.1 · 25.09.2026 · `blackdetect` filtresi VAR
   İKAME      ilk ve son 10 s'den saniye başına kare çıkarılıp gözle bakılır
   EŞİK       0 siyah aralık · 0 s başlık kartı · filigran 0 kare [D150]
              ⛔ LOSS_OF_LIFT 8. vakası tam burada delindi.

E5 KAPI       IŞIK TAKVİMİ MONOTONİKLİĞİ — kubbe kademesi geri açılıyor mu
   KOMUT      ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
   DOĞRULANDI ffmpeg 8.1 · 25.09.2026 · `signalstats` ve `metadata` filtreleri VAR
   İKAME      her sahnenin orta karesinden YAVG tek tek ölçülür
   EŞİK       Sahne ortalaması YAVG: S1-S5 > S6 > S7, MONOTONİK AZALAN.
              ⛔ S6 ya da S7 bir önceki kademeye dönerse ⑤ ARKA PLAN bulgusu MEŞRU.
              ⚠️ Bu ölçüm SAHNE ortalamasıdır, klip ortalaması değil: klip
                 içinde parlaklık değişmemeli.
```

---

## 👁️ GÖZ KAPILARI — makinenin ölçemediği beş şey, saniyesiyle

> Bu beş satır olmadan mod D koşmuş sayılmaz. Her satır TEK kare ister ve
> cevabı EVET/HAYIR'dır; "izlenimim" cevap değildir.

```
G1  144,0-150,0 s (K15)  ŞERİDİN ALTINDA IŞIK VAR MI?
    ffmpeg -ss 147 -i "$M" -frames:v 1 g1.jpg
    EVET(ışık var) → filmin tek ölçümü EKRANDA DEĞİL → 1 numaralı risk gerçekleşti
    HAYIR(ışık yok) → novum kanıtlandı. ⛔ Ayrıca 144,0 s'de (K15 · 0,0 s)
    perçin başının üstündeki AYNI şeridin altında ışık OLMALI — karşıt kare.
    ffmpeg -ss 141 -i "$M" -frames:v 1 g1_karsit.jpg

G2  234,0 s (K23)  DOKUZ KESİK UÇ SAYILABİLİYOR MU?
    ffmpeg -ss 234 -i "$M" -frames:v 1 g2.jpg
    Tek karede DOKUZ ayrı uç sayılmıyorsa FİNAL VURUŞ teslim edilmemiştir [D141].

G3  130,0-140,0 s (K14)  BEDEL AYNI KAREDE Mİ?
    ffmpeg -ss 138 -i "$M" -frames:v 1 g3.jpg
    Karede birlikte olmalı: ① bağ iki eldivende ② örtünün AÇIK kenarı
    ③ kenar boyunca mat kabarma ④ inmiş omuzlar. Dördü yoksa seçim bedelsizdir.

G4  0,0-10,0 s ↔ 230,0-240,0 s (K01 ↔ K24)  KAFİYE TUTUYOR MU?
    ffmpeg -ss 5 -i "$M" -frames:v 1 g4a.jpg ; ffmpeg -ss 235 -i "$M" -frames:v 1 g4b.jpg
    Kadraj kenarı, ölçek ve iki eldivenin konumu birebir mi; jest ters mi
    (kapatır ↔ kesilmiş ve açık)? Işık kademesi farkı BİLİNÇLİDİR, bulgu değil.

G5  24/24 klip  VİZÖR BİÇİMİ SAPTI MI?
    Her klibin orta karesi: tek DÜZ pane + görünür KALIN koyu çerçeve + derin
    yaka halkası. Kubbe/balon/küresel vizör tek klipte bile görülürse
    ⛔ ÜRETİM DURUR ve referans paneli kararı sahibe geri gider.
    ⚠️ Bu kapının önlemi yalnız METİNDİR (referans paketi yazılmadı) — D146'nın
       dört ölçülmüş vakası bu kilidin metinle TUTMADIĞINI söylüyor.
```

---

## 🧱 YANLIŞ-POZİTİF DUVARI — burada yazılı olan ihlal DEĞİLDİR

```
① 0 replik · 0 tırnak            → ③ SES "kimse konuşmuyor" yazamaz
② 24/24 sabit lockoff            → ⑨ "kamera hiç hareket etmiyor" yazamaz
③ sabit 10,0 s ızgara, ASL eğrisi yok → ① "ritim monoton" yazamaz (gerekçe B'de)
④ gölgesizlik                    → ⑤ "gölge yok, ışık yanlış" yazamaz (kart §3.6)
⑤ ufuk ve zemin yokluğu          → ⑤ "dünya kurulmamış" yazamaz (üç çapa C'de)
⑥ güneş diski 0 kare             → ⑥ "ışık kaynağı belirsiz" yazamaz
⑦ 0 ⭐viral klip                 → ④ "viral yuva yok" yazamaz (A'da gerekçeli)
⑧ metinsiz sayaç (rakam 0)       → ④ "sayı okunmuyor" yazamaz; sayaç ÜÇÜ de C'de
⑨ ışık kademesi S5→S6→S7 değişimi → ② "ışık tutarsız" yazamaz (takvim C'de)
⑩ sahne İÇİ kesmeler (17 adet)   → ① "kesme var" yazamaz; ② bunları AYRI ölçer
⛔ Duvarın dışında kalan her şey bulgudur. Duvar tasarım kararını korur,
   üretim hatasını KORUMAZ.
```
