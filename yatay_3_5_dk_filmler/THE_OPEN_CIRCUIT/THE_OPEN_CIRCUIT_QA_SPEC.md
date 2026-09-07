# 🧪 THE OPEN CIRCUIT — QA SPEC

> ⛔ **AYRI DOSYA** [D117]: SPEC planın içinde bir bölüm olarak yazıldığında
> dokuz filmde bir kez bile mod D koşulmadı; ayrı dosyaya çıkarılınca koştu.
> ⛔ Bu SPEC yazılır yazılmaz QA PAKETİ üretilir [D165]:
> `bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh yatay_3_5_dk_filmler/THE_OPEN_CIRCUIT`

---

## 📐 BLOK A — SAYIM VE SÜRE

```
SCENE COUNT:   25          SHOT COUNT: 25          CLIP COUNT: 25
⭐ Bu filmde sahne = çekim = klip. Sahne içi kesme YOK, çekim bölünmesi YOK.
   [KART 11 yapısal olarak kapalı]

RAW FOOTAGE:   1 klip × 9,0 s + 24 klip × 10,0 s = 249,0 s
TARGET:        249,0 s = 4:09
TRIM BUDGET:   0,0 s
⛔ Ham malzeme hedef süreye EŞİTTİR. Kırpılacak saniye yoktur; bu yüzden
  talimatsız kurgunun KLİP DÜŞÜRME riski (D70/D72/D100/D101) burada
  yalnız TESLİM SAYIMIYLA yakalanır — aşağıdaki KAPI ①.

TARGET ASL:    9,96 s   (249,0 / 25)
ASL BANDI:     9,0 – 10,0 s · sapma toleransı ±0,2 s
⛔ Teslim edilen master'ın ASL'si 9,0'ın altındaysa KLİP DÜŞMÜŞTÜR.

§0.18 KIRPMA TABLOSU: ⬜ GEREKMEZ (trim budget 0). Klip uzunluğu araçtan
  ölçülüp 10,0 s'den saparsa bu tablo AÇILIR ve her klip için
  ham → kurguda → nereden kırpılır satırı yazılır [D124].
```

---

## 🗣️ BLOK B — REPLİK KAYITLARI  [D122 — HESAPLANMAZ, HESAPLATILIR]

```
FORMÜL:  replik(S_n) = 9,0 + (n − 1) × 10,0 + promptun TIMELINE ofseti
⛔ Aşağıdaki 22 kaydın 22'si bu formülle ÜRETİLDİ, elle yazılmadı.
  Teslimden sonra her kayıt master üzerinde ±0,3 s içinde doğrulanır.
```

| # | S | sahne başı | ofset | **kayıt** | kim | replik |
|---|---|---|---|---|---|---|
| 1 | S3 | 29,0 | +1,5 | **30,5** | UZUN | "Second lug's under the coil." |
| 2 | S3 | 29,0 | +5,5 | **34,5** | KISA | "Front's early." |
| 3 | S5 | 49,0 | +2,0 | **51,0** | UZUN | "Then we're quick." |
| 4 | S9 | 89,0 | +1,5 | **90,5** | 🤖 | "Mast line is holding potential." |
| 5 | S9 | 89,0 | +6,5 | **95,5** | KISA | "It won't bite through that." |
| 6 | S11 | 109,0 | +1,5 | **110,5** | UZUN | "Cutters." |
| 7 | S11 | 109,0 | +5,5 | **114,5** | KISA | "Not for that line." |
| 8 | S13 | 129,0 | +1,0 | **130,0** | 🤖 | "Bay pressure is nominal." |
| 9 | S13 | 129,0 | +3,0 | **132,0** | KISA | "We seal, we wait it out." |
| 10 | S13 | 129,0 | +6,5 | **135,5** | UZUN | "Wait it out with what standing?" |
| 11 | S14 | 139,0 | +4,0 | **143,0** | UZUN | "Two left." |
| 12 | S15 | 149,0 | +2,0 | **151,0** | 🤖 | "Module two is open to outside." |
| 13 | S16 | 159,0 | +2,0 | **161,0** | UZUN | "Third rib from the seam. Count it." |
| 14 | S17 | 169,0 | +4,5 | **173,5** | KISA | "Counted." |
| 15 | S18 | 179,0 | +3,0 | **182,0** | 🤖 | "Node is open to outside." |
| 16 | S19 | 189,0 | +1,0 | **190,0** | 🤖 | "Main feed is off." |
| 17 | S19 | 189,0 | +6,5 | **195,5** | UZUN | "Fourth one's past the mast foot." |
| 18 | S20 | 199,0 | +3,0 | **202,0** | KISA | "Crust first." |
| 19 | S20 | 199,0 | +6,0 | **205,0** | UZUN | "I know." |
| 20 | S22 | 219,0 | +2,0 | **221,0** | 🤖 | "Ground path is closed." |
| 21 | S23 | 229,0 | +2,5 | **231,5** | KISA | "It's holding." |
| 22 | S23 | 229,0 | +7,5 | **236,5** | UZUN | "It'll be cold by four." |

```
DAĞILIM:  UZUN 8 · KISA 8 · 🤖 MAKİNE 6   → insan tarafı TAM DENGELİ
EN UZUN REPLİK: 6 kelime (#10) — 5 saniyenin çok altında ✅
EŞZAMANLI KONUŞMA: 0. Aynı sahnedeki iki replik arası en az 2,5 s.
EKRANDA OKUNAN KONUŞAN AĞIZ: **0 kare / 25 sahne** — teslimde göz kapısı.
```

---

## ⏱️ BLOK C — YAPISAL SAATLER  [formülle üretildi]

```
KATALİZÖR         S0 · 4,0 s      = %1,6    (hedef ≤0:15 ✅)
KAPAK ANI         S0 · 6,0 s      = %2,4    (PAKETLEME §1 bandı 0-10 s ✅)
TOHUM             S5 · 53,0-55,0  = %21,3   (hedef ilk %10-15'e YAKIN;
                  ⚠️ SAPMA KAYDI: %21 bandın biraz üstünde, gerekçe hook'un
                  ilk 5 sahneyi tek olaya bağlaması — tohum ancak dünya
                  kurulduktan sonra okunabiliyor)
ASİMETRİ ANI      S5 · 55,0 s     = %22,1   (dramatik ironi ① açılır)
AYRILIK  [B5b]    S11 · 110,5 s   = %44,4
ORTA NOKTA        S12 · 124,0 s   = %49,8   ✅ filmin matematiksel ortası
YIRTILMA ①        S15 · 152,8 s   = %61,4
YIRTILMA ②        S18 · 183,5 s   = %73,7
MERKEZÎ SEÇİM     S19 · 193,0 s   = %77,5   (hedef ~%75 ✅)
BEDEL GÖRÜNÜR     S20 · 206,5 s   = %83,0
DORUK             S22 · 222,5 s   = %89,4   (hedef bandı %85-88 —
                  ⚠️ 1,4 puan üstünde; sebep kümenin ikinci klibinin
                  ortasına düşmesi. Bilinçli: doruğun 20 saniyesi kesilmiyor.)
KAPANIŞ           S24 · 239,0-249,0 = %96-100
TOHUM DÖNÜŞÜ      S24 · 247,0 s   = %99,2
```

---

## 🔊 BLOK D — SES KAPILARI

```
ORTAM YATAĞI: hiçbir sahnede mutlak dijital sıfır teslim EDİLMEZ —
  dış sahnelerde giysi fanı + iki nefes + telsiz taşıyıcısı;
  iç sahnelerde (S13-S17) sürekli fan uğultusu ZEMİNDİR [§3.10].
  ⭐ S23'te fan SUSAR ve bu bir OLAYDIR, hata değildir; o sahnede yatak
    yalnız iki nefes + telsiz hışırtısıdır.

PLANLI SESSİZLİK: 193,0 – 195,0 s  (2,0 s · merkezî seçimin içi)
  ⛔ BIÇAK KURGUDADIR [D180]. MUZIK dosyasındaki HARD MUTE satırı ve
    komutu uygulanmadan teslim edilmez.

MÜZİKSİZ ARALIKLAR: 0,0-9,0 (hook) · 179,0-199,0 (S18+S19) · 239,0-241,0
```

---

## ⚙️ BLOK E — MAKİNE KAPILARI

> ⛔ **[D142] YAZILMADAN ÖNCE FİİLEN SINANDI.** Aşağıdaki dört kapının
> dördü de 07.09.2026'da bu makinede **ffmpeg 8.1** ile kuru koşuldu ve
> çalıştığı görüldü (`signalstats` · `silencedetect` · `astats` · `bandpass`).
> ⛔ **`vidstabdetect` BU MAKİNEDE KURULU DEĞİL** — kamera sabitliği için
> bir kapı YAZILMADI; yerine KAPI ④ (freezedetect ikamesi) kondu.
> THE SINKING STAKE aynı arızayı 02.09.2026'da ölçtü; kayıt korunuyor.

```
KAPI ① — TESLİM SAYIMI (HARD)
  Amaç: kurgunun klip düşürüp düşürmediğini yakalamak [D70/D72/D101].
  ffprobe -v error -show_entries format=duration -of csv=p=0 <master>
  GEÇER: süre 249,0 ± 1,0 s.  DÜŞER: 240,0 s altı → en az bir klip düşmüş.

KAPI ② — KARANLIK TABAN (HARD · filmin 20 sahnesi GECE)
  Amaç: §3.2'nin "gölgenin İÇİ DOLUDUR" kuralı üretimde tutmuş mu.
  Vakum değil ince atmosfer; mutlak siyah bu filmde FİZİK HATASIDIR.
  ffmpeg -i <master> -vf "signalstats,metadata=print:key=lavfi.signalstats.YAVG:file=yavg.txt" -f null -
  GEÇER: 49,0 s sonrasındaki hiçbir karede YAVG < 8/255 DEĞİL.
  DÜŞER: ardışık 12 kareden fazlası YAVG < 8 → o sahne yeniden üretilir.
  ⚠️ Eşik 8/255 bu depoda ölçülmedi; THE THIN ROOF'un 18/255 eşiği GÜNDÜZ
    bir sahne içindi. Bu film gecedir ve eşik ondan düşük tutuldu.
    ⛔ Eşiğin kendisi ÖLÇÜM BORCUDUR, ilk üretilen gece sahnesinde kalibre edilir.

KAPI ③ — PLANLI SESSİZLİK (HARD)
  Amaç: 193,0-195,0 aralığı gerçekten sessiz mi [D180].
  ffmpeg -i <master> -af "bandpass=f=1850:width_type=h:w=1550,silencedetect=n=-50dB:d=0.3" -f null -
  GEÇER: çıktıda 193,0'dan önce başlayıp 195,0'dan sonra biten TEK bir
         silence_start/silence_end çifti var.
  DÜŞER: aralık parçalanmışsa ya da hiç yoksa — kurguda HARD MUTE
         uygulanmamıştır, teslim edilmez.
  ⚠️ THE STANDING WIRE tam burada düştü: −50 dB'de aralık DÖRDE bölünmüştü.

KAPI ④ — KAMERA SABİTLİĞİ İKAMESİ (SOFT · vidstabdetect YOK)
  Amaç: 25/25 lockoff tutmuş mu. Gerçek kapı vidstabdetect'ti, kurulu değil.
  İKAME: sahne içi hareket YALNIZ özneden gelmeli; kadrajın kenarları
  sabit kalmalı. Kaba ölçüm:
  ffmpeg -i <master> -vf "freezedetect=n=-60dB:d=0.5,metadata=print:file=freeze.txt" -f null -
  GEÇER: gözlem satırı üretiliyor (bu kapı SAYI vermez, işaret verir).
  ⛔ DÜRÜST KAYIT: bu bir kamera sabitliği ölçümü DEĞİLDİR, ikamedir.
    Gerçek denetim ⑪ ölçüm kapısında İNSAN GÖZÜYLE yapılır.
```

---

## 👁️ BLOK F — GÖZ KAPILARI  (makineye inmeyenler)

```
□ ① AĞIZ: 22 repliğin 22'sinde konuşan ağız okunuyor mu? Bir tanesi bile
     okunuyorsa o sahne yeniden üretilir [KART 7 · ekranda ağız 0 kare].
□ ② KASK: 50 karenin hepsinde kask ÇERÇEVELİ ve ön pencere DÜZ mü?
     Kubbe/dikişsiz cam çıkan her sahne yeniden üretilir [D146].
□ ③ SIRT: kamera arkada olan 6 sahnede (S6·S7·S8·S18·S23·S24) sırtta
     ünite doğdu mu? [D79 · D139]
□ ④ KIVILCIM: 8 boşalma sahnesinin hepsinde çizgi TEK, İNCE, DÜZ ve
     SÖNÜMLÜ mü? Sürekli yanan / dallanan / geride ışık bırakan her
     kare yeniden üretilir [bu filmin 1 numaralı riski].
□ ⑤ YÖN: S22'de kıvılcım AŞAĞI mı iniyor? Yukarı çıkıyorsa filmin
     doruğu YOKTUR — S22 filmin İPTAL KAPISIDIR [PLAN §ÜRETİM SIRASI].
□ ⑥ RÜZGÂR: hiçbir karede kumaş çırpıyor / kimse eğilerek yürüyor /
     kimse itiliyor mu? [§3.2 · filmin fizik imzası]
□ ⑦ KİR: 25 sahnenin kir fazı MONOTONİK mi, hiç geri sıfırlanıyor mu? [D147]
□ ⑧ ŞERİT: yanan pencere şeridi sayısı 4→3→2→0 sırasını izliyor mu ve
     hiç geri yanıyor mu? [KART 6b · ışık takvimi monotonik]
□ ⑨ AYAK: bağlı ayak sayısı 1→2→3→4 sırasını izliyor mu?
□ ⑩ ÜS: dört geniş planda modül/figür oranı aynı mı? [KART 13]
□ ⑪ İKİ FİGÜR: hiçbir karede üçüncü gövde, klon ya da yansıma var mı? [D69]
□ ⑫ METİN: hiçbir yüzeyde okunabilir metin/rakam/işaret var mı? [D138 —
     zemin, kaya ve iç panel yüzeyleri DÂHİL]
```

---

## 📦 QA PAKETİ

```
⬜ bash .claude/skills/qa-isle/scripts/rubrik_paketle.sh \
       yatay_3_5_dk_filmler/THE_OPEN_CIRCUIT
   → kilavuzlar_ve_sistem_dosyalari/QA_PROMPTLARI/FILME_OZEL/THE_OPEN_CIRCUIT/PAKET_1..12
⛔ Bu klasör yoksa operatörün eline ÇIPLAK RUBRİK kalır, çıplak rubrik
  MOD V koşar, ve mod V koşusu T tablolarına GİREMEZ [D129 · D165].
  İki vaka: THE STILL SWARM (01.09) ve THE SINKING STAKE (02.09) —
  ikisinde de sekiz merceğin sekizi mod V koştu.
⛔ SPEC değişirse betik YENİDEN koşulur.
```
