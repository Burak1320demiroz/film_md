# 📋 THE_SINKING_HARBOR — QA SPEC

> ⛔ **BU DOSYA RUBRİĞİN BAŞINA YAPIŞTIRILIR** [D129]. Yapıştırılmazsa koşu
> **mod V**'dir ve T tablolarına GİREMEZ.
> ⛔ Sayılar burada; PLAN ile çelişirse PLAN düzeltilir, bu dosya değil —
> ikisini birden tutmak, birini yanlış tutmaktır.
> **Kaynak:** `THE_SINKING_HARBOR_PLAN.md` + `00_ANALIZ/` yedi adımı.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① KARE          A + B blokları
② DEVAMLILIK    C bloğu (KİMLİK DİZİSİ · YIPRANMA · EŞ KADRAJ · DÜNYA ÇAPASI)
③ SES           A (DIALOGUE LINES · register) + MUZIK dosyası
④ HİKAYE        A bloğu                        ⭐ TAM FİLM koşusunda maskesiz
⑤ ARKA PLAN     ⛔ SPEC VERİLMEZ (video-only tasarım) — C bloğunun DÜNYA
                ÇAPASI satırı yalnız ÇELİŞKİ DEFTERİ'nde kullanılır
⑥ FİZİK         C bloğu + E bloğu kilit listesi
⑦ AKSİYON       B bloğu (INTRA-SCENE CUTS) + C (EKRAN YÖNÜ)
⑧ EFOR          PLAN'ın BEDEL EĞRİSİ tablosu
⑨ KADRAJ        B bloğu (KURULUM İSKELETİ · DÖNÜŞ · ANGLE ARC · DÖNGÜ KANITI)
⑩ OYUNCULUK     PLAN'ın ÇAPA ÜÇLÜSÜ + DAVRANIŞ ŞERİDİ
⑪ IŞIK          C bloğu IŞIK TAKVİMİ
⑫ HOOK          A + B (SCREEN TEXT · DÖNGÜ KANITI)
⑬ UYUM          `THE_SINKING_HARBOR_URETIM_DEFTERI.md` (üretim sonrası)
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_SINKING_HARBOR
FORMAT:            yatay 16:9 · 16 dk · 96 klip × 10 s · 8 bölüm · ÇOK KLİPLİ SAHNE
RUNTIME:           960 seconds (title card: YOK — screen text lock 0,0 s)
SCENE COUNT:       24      ⛔ CLIP COUNT (96) ile AYNI DEĞİL — §2.0b rejimi
PART GRID:         PART 1 = K01-K24 · 24 clips · 0-240 s   (BOLUM_1 + BOLUM_2)
                   PART 2 = K25-K48 · 24 clips · 240-480 s (BOLUM_3 + BOLUM_4)
                   PART 3 = K49-K72 · 24 clips · 480-720 s (BOLUM_5 + BOLUM_6)
                   PART 4 = K73-K96 · 24 clips · 720-960 s (BOLUM_7 + BOLUM_8)
                   FULL   = K01-K96 · 96 clips · 0-960 s
                   Rubriğe SPEC ile birlikte beyan: "THIS FILE IS PART n OF 4 —
                   clips Kxx-Kyy". Maske: PART 1 BAŞ · PART 2-3 ORTA (hook VE
                   final "—") · PART 4 SON · FULL maskesiz.
                   BOUNDARY PAIRS (hiçbir part masterda yan yana GÖRÜNMEZ):
                   K24|K25 · K48|K49 · K72|K73 → ELLE KARE ile kapanır.
TEMA:              İLK TEMAS
TEMA SAHNELERİ:    S06 S07 S09 S10 S11 S16 S20 S21 S24
                   (motif: sondanın metal bileziği · kuvvet ↔ eli çekme ·
                   aynı eksenden zıt sonuç · alttan gelen amber)
INTENDED EMOTION:  tekinsiz merak → huşu (kademe: çift-duygu; korku ÇÖZÜLMEZ)
ENDING TYPE:       kapalı olay + açık tutum — liman kaybedilir, üçü kurtulur,
                   gezegene sahiplik işareti DİKİLMEZ
PROTAGONIST:       kurtarma pilotu (isimsiz — özel ad promptta geçmez [D34])
CENTRAL CHOICE:    S12 · K48 · 7,5 s — eldiven kumandayı BIRAKIR
DIALOGUE LINES:    38 · register: HUMAN 38 / MACHINE 0
                   ⛔ MACHINE 0 bir KARARDIR: sayı söyleyen replik YOK, bu yüzden
                   gövdesiz AI sesine ihtiyaç doğmuyor [YANASMA §2.2①]
SILENT SCENES:     S01 (yalnız dış ses) · S03'ün K09-K10'u · S21'in K84'ü ·
                   planlı mutlak sessizlik 3 pencere (aşağıda, E bloğu)
VIRAL INTERSTITIALS: ⬜ ÖLÇÜLMEDİ — üç aday (K57 · K41 · K94) üretimden sonra
                   tek tek ölçülür; hedef olarak YAZILMADI
                   ⛔ THESE MAY NOT BE CUT: KESİLEMEZ listesi PLAN'da
TITLE:             "THE SINKING HARBOR" — başlık izleyiciye NEREYE bakacağını
                   söyler: aşağı inen yapıya. Afiş: TO ESCAPE, THEY HAD TO GO DEEPER.
LIBRARY CONTEXT:   aynı raftaki kardeşler — THE_STOLEN_SKY (16 dk · ilk film) ·
                   THE_LAST_GATE (16 dk · sahip planından yazılan ilk film) ·
                   LOSS_OF_LIFT (§3.6 bulut katmanı) ·
                   THE_DEEP_PRESSURE (gaz devi · D56'nın kaynağı)
```

## 🅱️ B BLOĞU — KURGU GEOMETRİSİ (① KARE'ye A ile birlikte)

```
CLIP COUNT:      96
SHOT COUNT:      96 · sahne içi kesme 72   (ÇEKİM = KLİP; klip İÇİ kesme 0)
SCENE PLAN:      SAHNE PLANI: 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
                 S01 = K01-K04 · S02 = K05-K08 · S03 = K09-K12 · S04 = K13-K16 ·
                 S05 = K17-K20 · S06 = K21-K24 · S07 = K25-K28 · S08 = K29-K32 ·
                 S09 = K33-K36 · S10 = K37-K40 · S11 = K41-K44 · S12 = K45-K48 ·
                 S13 = K49-K52 · S14 = K53-K56 · S15 = K57-K60 · S16 = K61-K64 ·
                 S17 = K65-K68 · S18 = K69-K72 · S19 = K73-K76 · S20 = K77-K80 ·
                 S21 = K81-K84 · S22 = K85-K88 · S23 = K89-K92 · S24 = K93-K96
INTRA-SCENE CUTS: K05|K06 K06|K07 K07|K08 · K09|K10 K10|K11 K11|K12 · K13|K14
                 K14|K15 K15|K16 · K17|K18 K18|K19 K19|K20 · K21|K22 K22|K23
                 K23|K24 · K25|K26 K26|K27 K27|K28 · K29|K30 K30|K31 K31|K32 ·
                 K33|K34 K34|K35 K35|K36 · K37|K38 K38|K39 K39|K40 · K41|K42
                 K42|K43 K43|K44 · K45|K46 K46|K47 K47|K48 · K49|K50 K50|K51
                 K51|K52 · K53|K54 K54|K55 K55|K56 · K57|K58 K58|K59 K59|K60 ·
                 K61|K62 K62|K63 K63|K64 · K65|K66 K66|K67 K67|K68 · K69|K70
                 K70|K71 K71|K72 · K73|K74 K74|K75 K75|K76 · K77|K78 K78|K79
                 K79|K80 · K81|K82 K82|K83 K83|K84 · K85|K86 K86|K87 K87|K88 ·
                 K89|K90 K90|K91 K91|K92 · K93|K94 K94|K95 K95|K96
                 ⛔ these cuts are INSIDE one scene: location, light, sound bed,
                 costume dirt, held object and body pose MUST match across them;
                 a reset here is a ② CONTINUITY defect, not a scene change.
TARGET ASL BAND: 10,0 s sabit   ASL CURVE: düz (96 × 10 s)
                 ⛔ GEREKÇE [D74]: bu hat SABİT IZGARALIDIR — 10 s son kurgu
                 birimidir ve kırpılmaz (§2.8: "tam 10 s · ±0"). ASL bir SEÇİM
                 değil formatın kendisidir. Ritim ızgarayla değil ÖLÇEK,
                 TEMPO ve SES DOKUSU sütunlarıyla kurulur (PLAN sahne haritası).
                 ⭐ `SAHNE_DOLULUGU` §8'in notu: 10 s ızgara ÜRETİM planıdır,
                 kurgu ritmi değildir.
GRID:            klip başlangıcı(n) = 0 + (n−1) × 10,000 s   (hook 96'nın İÇİNDE)
RUNTIME:         960,000 s ±0
RAW FOOTAGE:     92 klip × 10 s = 920 s (K01-K04 kurguda doğar: 40 s)
                 TRIM BUDGET: 0 s  ⛔ klip kırpılmaz
SCREEN TEXT:     0,0 saniye
CAMERA:          92 / 92 sabit lockoff — "absolutely zero camera movement"
SETUP SEQUENCE:  klip başına kurulum imzası `00_SAHNE_TABLOSU.md` KURULUM sütunu
KURULUM İSKELETİ: B D M X E F M G · M H J H M I H M E M K Z · H J M H J A T H N U T H ·
                 C U A O L T A Z H C A T · H M G M C X B M Q P C M ·
                 Q Y W P R P C M S W C V · J P V I P T W J V C W S ·
                 M R W P M H M E D Z L B
                 (92 harf · K01-K04 harf TAŞIMAZ · PLAN'daki ile AYNI)
KÜME:            0 — ⛔ ÇOK KLİPLİ SAHNE rejiminde KÜME YOKTUR (zincir kaldırıldı,
                 22.09.2026); bekleme aynı MEKÂN ve EYLEMDE kalınarak kurulur
DÖNÜŞ:           28 / 92 = %30   (hedef ≥%40 — ÖLÇÜLDÜ, ALTINDA)
                 bölüm bazında: B1 %12 · B2 %42 · B3 %42 · B4 %17 · B5 %25 ·
                 B6 %17 · B7 %17 · B8 %17
                 ⛔ GEREKÇE [D74]: film 11 ayrı mekân geziyor; %40 hedefi
                 tek-iki mekânlı filmlerden ölçülmüştür. Yerine EŞ KADRAJ
                 ÇİFTLERİ kullanıldı (10 çift) — `03_SAHNE_SIRALAMASI` §4b
ANGLE ARC:       4 açı TİPİ (eye-level · low-angle · high-angle · over-the-shoulder)
                 bölüm başına ≥3 — 8/8 bölüm GEÇTİ (§2 en az 3 ister)
ÖLÇEK KADEMESİ:  6 (EWS · WS · MWS · MS · CU · ECU)
ARDIŞIK AYNI KURULUM: 0 çift (⑩① temiz)
DORUK:           S21 · K84 → sonda ayrılır (klip başlangıcı 830,000 s = 13:50)

REPLİK ENVANTERİ — 38 replik: 34'ü PROMPT bloklarında, 4'ü KESİM KARTINDA.
   ⭐ H1 (K01) · H2 (K02) · H3 (K03) · H4 (K04) kesim kartlarının repliği olup
   prompt bloğu TAŞIMAZ (kart 10 alanlı, prompt değil — `COK_KLIPLI_SAHNE` §4).
   Bu yüzden `prompt_kontrol` ㉓ "promptlarda tırnaklı 34" der ve bu ⚠️ FIX
   BİLİNÇLİ KISALTMADIR [D74]: eksik replik yok, taşıyıcı dosya farklı.
   ⛔ Kesim kartları prompt'a çevrilirse bu satır DÜŞER ve sayı 38 olur.

REPLİK ZAMANLARI ⛔ HESAPLANMAZ, HESAPLATILIR [D122]:
   replik(Kn) = (n−1) × 10,000 s + promptun TIMELINE ofseti
   örnek doğrulama: D19 (K48 · ofset 8,0 s) = 47 × 10 + 8 = 478,0 s = 07:58
                    D31 (K80 · ofset 6,0 s) = 79 × 10 + 6 = 796,0 s = 13:16
                    D34 (K96 · ofset 9,0 s) = 95 × 10 + 9 = 959,0 s = 15:59
   ⬜ H1-H4'ün OKUMA SÜRELERİ ölçülecek (ffprobe) — tahmin YAZILMADI.
      Sert kısıt: H4 00:00:39:12'den önce bitmeli (K04 kesim kartı §7.2 kalıbı)

FİNAL VURUŞ KANITI [D141]:
   dört kenet AÇIK · 914,0-920,0 s (K92) · 4 adet · BULUNAN
   her kenet 280 px · tek karede sayılabilir
   ⛔ ikinci kanıt: K94'te YANAN alan ışığı 0 adet · BULUNMAYAN
   ffmpeg -ss 917 -i "$M" -frames:v 1 kanit.jpg   → BAK, DÖRT TANE Mİ
DÖNGÜ KANITI: K05 ↔ K96 — aynı kurulum (B) · aynı ölçek (WS) · aynı ışık
   kaynağı (kokpit tavan paneli) · aynı jest ailesi (eldiven kumandada ↔
   eldiven kumandadan ÇEKİLMİŞ). Harf çifti: B ↔ B
   ffmpeg -ss 40.1 -i "$M" -frames:v 1 ilk.jpg
   ffmpeg -ss 959.8 -i "$M" -frames:v 1 son.jpg   → YAN YANA KOY
```

### 🧬 İNSAN ŞERİDİ — sıra kilidi [DERS 118]

```
PLAN: 1011001111011111010010110111001110100110111111111111111111011111011001011100010011111110 0001
  okunur biçim (K05-K96 · 92 karakter · 1 = insan kadrajda · 0 = insansız):
  1011 0011 1101  1111 0100 1011  0111 0011 1010  0110 1111 1111
  1111 1111 1101  1111 0110 0101  1100 0100 1111  1110 0001
İNSANSIZ 29 KLİP: K06 K09 K10 K15 K21 K23 K24 K26 K29 K33 K34 K38 K40 K41 K44
  K63 K69 K72 K73 K75 K79 K80 K81 K83 K84 K92 K93 K94 K95
K01-K04: kesim kartı — kaynak klibin insan durumunu taşır (K01 0 · K02 2 ·
  K03 2 · K04 2)
⛔ Raporun "Present" dizesi bu dizeyle YAN YANA okunur; yuva kayması varsa
  Δ TABLOSU yazılır [D121] — doruk yanlış yuvada olabilir [LOSS OF LIFT]
```

## 🅲 C BLOĞU — BELGESİZ MERCEKLERİN KİLİTLERİ

> Tarif değil **SAYI**. Bu blok ② ③ ⑤'in FLAGS sorularını besler: kaynağı
> burada YAZILI olan bulgu DÜŞER.

```
İNSAN         3 · pilot (35, kadın) · mühendis (32, erkek) · operatör (58, erkek)
              kadrajda en çok 3, en az 0; dışarıda EN ÇOK 2 (operatör hiç çıkmaz)
              ⛔ dördüncü insan 0 klip · klon 0 · biniş/iniş hareketi 0 klip [D69]
KASK          96/96 KAPALI, hiç açılmaz, hiç çıkarılmaz, ara durum 0 ·
              vizör optik berrak, 0 ton, 0 ayna kaplaması, 0 çevre yansıması ·
              vizör ÖN YÜZDE tek kavisli panel, çevresinde görünür koyu çerçeve,
              yan yüzeyler opak beyaz · üst kenarda TEK ince parlama çizgisi ·
              yaka mühür halkası görünür · sırt ünitesi YOK, düz siluet [D79 · D95 · D146]
              ⛔ seamless · bubble · dome · sphere kelimeleri 0 kez
NOVUM         KURAL: gezegenin derin katmanı kendisine uygulanan kuvvete ORANLI
              kasılır; yukarı çekiş aşağı çekiş üretir, bırakmak GECİKMELİ
              gevşeme üretir.
              NEYİN İHLALİ: etki-tepki bir KUVVET değişimiyle değil bir YÜK
              değişimiyle gecikmeli yanıt veriyor; kuvvet uygulamak kuvveti
              ARTIRIYOR.
              TAŞIYICI: sondanın metal bileziği × yük bindirme/boşaltma jesti
              → bileziğin üstündeki koyu kıvrım GERİLİR, sonra GEVŞER
              TEK KARE: K34 · 05:35 · taşıyıcı adı cümlede [D157]
              KANIT KLİPLERİ: K23-K24 · K34 · K38 · K79 · K84 (≥3 sahne, 3 nesne)
YERÇEKİMİ     1,00 g · TEK g, 92/92 promptta AYNI cümle
              düşüş: 0,2 m → 0,20 s · 0,65 m → 0,36 s · 1 m → 0,45 s · 2 m → 0,64 s
              ⛔ ivme PROMPTA YAZILMAZ; kadrajı terk SÜRESİ yazılır [D127]
ATMOSFER      yoğun hidrojen-helyum bulut katmanı · zemin YOK · ufuk çizgisi YOK ·
              toz YOK (yüzey yok) · bağıl rüzgâr 0-2 m/s, kumaş kıpırdamaz ·
              alçak frekanslar yakın ve güçlü taşır, tizler ölür
              ⛔ SU 0 kare — MEDIUM LOCK, filmin 1 NUMARALI riski [D56]
EKRAN YÖNÜ    batan her şey kadrajın ALT üçte-birinde oturur ve ALT kenardan
              çıkar · yükselen ÜST kenardan çıkar · pilot SOL üçte bir,
              mühendis SAĞ üçte bir, 92/92 (takas 0) [D86 · LOSS OF LIFT madde 6]
SAYAÇ         DÖRT sayaç, dördü de METİNSİZ ve MONOTONİK:
              ① ALÇALMA — bulut sınırının pencere çerçevesindeki yeri:
                 K15 alt çeyrek → K29 orta → K61 üst çeyrek → K80 TAMAMI →
                 K94 liman bulutun içinde
              ② YÜK — iki sade eğri, rakamsız: K30 tepeler hizalı → K39
                 gecikmeli → K68 iki zıt eğilim
              ③ KOLON — yanan kolon sayısı: 6 (K23) → 5 (K26) → 4 (K44) →
                 2 kararsız (K69) → kısa denge (K85) → 0 (K94)
              ④ BAĞLANTI — kapalı taşıyıcı bağlantı sayısı: 3 (K45 · K63) →
                 1 (K71) → 0 (K83)
              ⛔ hiçbirinde rakam, eksen adı, birim ya da etiket YOK
EŞ KADRAJ     K05↔K96 (KAFİYE) · K05↔K55 · K23↔K24 · K33↔K40 · K34↔K38 ·
              K41↔K95 · K57↔K61 · K65↔K86 · K72↔K75↔K81 · K10↔K92
DÜNYA ÇAPASI  3/3 — dış kliplerde BİREBİR (World Bible'daki üç cümle):
              GÖK "a bright sourceless dome of cloud fills the upper third of
                   the frame, with no sun disc anywhere in it"
              DERİNLİK "below there is depth and no horizon line at all — the
                   cloud simply goes down out of frame"
              YER İMİ "the harbour's black ribs cross the frame and run out of
                   it on both sides, the only hard edge in the shot"
              ⚠️ §3.6'da ufuk ve zemin İKİSİ DE YOK → D209'un klasik üçlüsü
                 yazılamaz; bu UYARLANMIŞ üçlüdür
YIPRANMA      2 sabit bölge · MONOTONİK, hiçbir klipte sıfırlanmaz [D42]
              ① pilotun SAĞ DİZ PLAKASI — tek parlak sürtünme izi · K65'ten
                 K96'ya kadar
              ② operatörün SOL DİZİ — geçici destek · K19'dan K96'ya kadar
              eldivenlerde güverte tozu: K17'den itibaren, artar, silinmez
KİMLİK DİZİSİ kask (96 klip, hepsi K): KKKK KKKK KKKK … 96/96 · A hiç yok
              kabartma KONUMU: GÖĞÜS, 96/96 — omuz ya da sırt ASLA
              pilot:     üç kanatlı kabartma · inci beyazı + ŞAMPANYA ALTINI
                         · sağ diz çiziği K65+
              mühendis:  dikdörtgen ızgara kabartma · beyaz + KOBALT
                         · hasar YOK
              operatör:  dairesel kabartma · saten beyaz + BAKIR
                         · sol diz desteği K19+
              kriko: mühendis K18-K58 → pilot K59-K96 (alet sayısı değişmez)
              ⛔ İlan edilmeyen özellik ihlal yazılamaz; ilan edilen tek sapmada 🔴 [D208]
IŞIK TAKVİMİ  MONOTONİK ✅ — güneş DİSKİ olmadığı için yön+Kelvin ile DEĞİL,
              TEK PARLAKLIK DİZİSİ ile yazılır [§3.6 tuzak ③ · D193 uyarlaması]
              kubbe: 6/6 (S02-S06) → 5/6 (S07-S12) → 4/6 (S13-S15) →
              3/6 (S16-S17) → 2/6 (S18-S23) → S24'te GEMİ için 5/6, LİMAN 1/6
              ⛔ sönen kolon GERİ YANMAZ · tek istisna S24 ve o karede liman
                 AYNI ANDA aşağı iner (iki yön aynı kadrajda, gerekçeli)
              iç mekân: ~4500 K nötr beyaz, tavana gömülü, parlamasız
SES REGISTER  HUMAN 38 · MACHINE 0
              kadraj dışı replik 38/38 · telsiz band-pass 36/38 (K16 ve K96
              açık kanal) · kadrajda konuşan ağız HEDEF 0 klip
              katman tavanı 4 · kesmede oda tonu köprüsü ≥0,2 s · diyalog
              altında müzik/alarm −6 dB [D216]
```

## 🅴 E BLOĞU — MAKİNE KAPILARI [Ders 142]

> Her kapı ÜÇ satır taşır. **DOĞRULANDI satırı olmayan kapı YAZILMAMIŞTIR.**
> Aşağıdaki altı filtre 04.10.2026'da KURU KOŞUYLA doğrulandı.

```
KAPI ① PLANLI SESSİZLİK — üç pencere gerçekten sessiz mi [D180 · ⛔ ÇALIŞMIYOR damgalı]
KOMUT         ffmpeg -hide_banner -i "$M" -af silencedetect=noise=-50dB:d=0.3 -f null - 2>&1 | grep silence
DOĞRULANDI    ffmpeg 8.1 · 04.10.2026 · silencedetect VAR
İKAME         filtre yoksa astats ile saniyelik RMS: -af astats=metadata=1:reset=1
PENCERELER    K40 son 1,5 s (398,5-400,0) · K79 orta 1,0 s (784,0-785,0) ·
              K96 son 2,0 s (958,0-960,0)
              ⛔ ÜÇ EŞİKTE koşulur: −50 / −40 / −30 dB

KAPI ② EKRAN METNİ — 0,0 saniye [D34 · D215 · LOSS OF LIFT 8. vaka]
KOMUT         ffmpeg -hide_banner -i "$M" -vf "blackdetect=d=0.2:pix_th=0.05" -f null - 2>&1 | grep black
DOĞRULANDI    ffmpeg 8.1 · 04.10.2026 · blackdetect VAR
İKAME         ilk ve son 10 s'den kare çıkar ve BAK (ffmpeg -ss 0 / -sseof -10)
KABUL         başta 0 kare siyah/kart · sonda 0 kare statik siyah · toplam metin 0,0 s

KAPI ③ IŞIK TAKVİMİ İZİ — parlaklık dizisi monotonik mi [D193]
KOMUT         ffmpeg -hide_banner -i "$M" -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG" -f null - 2>&1 | grep YAVG
DOĞRULANDI    ffmpeg 8.1 · 04.10.2026 · signalstats VAR
İKAME         klip başına tek kare + histogram
KABUL         ↑ işareti 0 (takvim geri sarmadı) · ⟳ işareti 0 (klip içinde geri
              yanmadı) · tek istisna S24, gerekçesi C bloğunda

KAPI ④ KLİP BAŞI KLON — her klibin ilk 0,6 saniyesi [D140]
KOMUT         for s in $(seq 0 95); do ffmpeg -v error -ss $((s*10)) -i "$M" -t 0.6 -vf "fps=10,scale=460:259" -q:v 2 giris_${s}_%02d.jpg -y; done
DOĞRULANDI    ffmpeg 8.1 · 04.10.2026 · fps ve scale VAR
İKAME         yok — bu kapı filtresiz koşar
KABUL         96 şeritte ikinci kask · ikinci yüz · ikinci el · omuzdan doğan
              form 0 adet. ⛔ 0,5 s'den kısa yaşayıp kaybolan form da KUSURDUR

KAPI ⑤ DONMA — 2,5 s'den uzun hareketsizlik [SAHNE_DOLULUGU · T15.1 ④]
KOMUT         ffmpeg -hide_banner -i "$M" -vf "freezedetect=n=-60dB:d=2.5" -f null - 2>&1 | grep freeze
DOĞRULANDI    ffmpeg 8.1 · 04.10.2026 · freezedetect VAR
İKAME         saniyelik kare farkı (select='gt(scene,0.002)')
KABUL         donma aralığı 0. ⚠️ S24'ün son 2 s'si SESSİZ ama HAREKETSİZ DEĞİL:
              omuzlar bir kez yükselip iner — freezedetect bunu yakalarsa klip
              yeniden üretilir

KAPI ⑥ SÜRE VE KLİP SAYISI — 96 klip · 960 s ±0
KOMUT         ffprobe -v error -show_entries format=duration -of csv=p=0 "$M"
DOĞRULANDI    ffprobe 8.1 · 04.10.2026
İKAME         yok
KABUL         960,000 ±0,040 s · 96 klip · kart 0 s
              ⬜ KLİP SÜRESİ ÖLÇÜMÜ [D124]: ilk klip üretilince ffprobe ile
              ölçülür; 10,000 s değilse bütün zaman kodları yeniden hesaplatılır
              ve KIRPMA satırı buraya yazılır. TAHMİN YAZILMADI.
```

---

## ⚓ ÇAPA ÜÇLÜSÜ [`OYUNCULUK_YAZIM` §2 · ⑩ mod D'nin ANCHOR BEATS satırı]

```
CHOICE  K48 · 477,5 s · BEFORE eldiven kumandanın üstünde, parmaklar açık,
        omuzlar dik → AFTER eldiven BIRAKIR ve dizine iner, omuzlar bir avuç
        düşer · kanal: el + omuz
COST    K80 · 796,0 s · BEFORE pencerenin alt çeyreği bulutla kaplı, cam KURU
        → AFTER pencerenin TAMAMI örtülü, iç yüzde nefes buğusu ·
        kanal: pencere + nefes
FINAL   K96 · 958,0 s · BEFORE üç kask ileriye dönük, eldivenler kucakta kapalı
        → AFTER pilotun eldiveni AÇILIR, avuç yukarı döner, kask bir derece
        yana · kanal: el + kask
⛔ Üçünde de dolgu jesti (yaka düzeltme, saç, el kaldırma) YAZILMADI [D202]

DAVRANIŞ ŞERİDİ (sahne başına bir harf · ⑩'un TASK ONLY sayımı = G sayısı):
  G G G R T K B S R G R K R G G G B T D B G G G S
  G 10 (%42) · T 2 · D 1 · K 2 · B 3 · R 4 · S 2

BEDEL EĞRİSİ (sahne başına yorgunluk 0-6 · ⑧'in RESET LOG girdisi):
  0 0 0 1 2 2 3 3 3 3 3 3 3 3 3 4 5 5 5 5 6 6 5 4
  ödeme satırları (kanal @ saniye): PLAN'ın BEDEL EĞRİSİ tablosu — 14 klip
```

## 👥 İKİ+ İNSAN — ⑩ ve ② için ek satırlar [`IKI_KISI_VE_AYRILIK`]

```
KİM SOLDA     pilot SOL üçte bir · mühendis SAĞ üçte bir · operatör ÜÇLÜ
              kadrajda ORTA/arka · 92/92, takas 0
GAZE STRING   pilot: hedefe (kumanda · pim · pencere) · mühendis: ölçüme
              (gösterge · kayıt · kol) — ikisi aynı saniyede aynı yere BAKMAZ
AYRILIK       S06 · K22 (güç EKLE) ↔ S09 · K36 (güç ÇIKAR) · gecikme ≥0,7 s ·
              mesafe eğrisi 0,4 → 1,1 → 1,8 → 0,6 m · TEMAS yalnız K88'de
DİNLEYEN KADRAJI  38 replikten 11'i dinleyenin kadrajında duyulur; o kliplerin
              promptunda replik metni VAR, konuşanın ağzı YOK, dinleyenin
              dudakları KAPALI [DIYALOG_SAHNESI §4 · §7]
```
