# 🧷 THE OPEN CIRCUIT — REFERANS PAKETİ

> Kaynak kılavuz: `kilavuzlar_ve_sistem_dosyalari/REFERANS_PAKETI_KILAVUZU.md`
> ⛔ **KAPI 0.** Bu paketin sayfaları ONAYLANIP seed'leri yazılmadan o
> varlığın geçtiği HİÇBİR sahne üretilmez [D168].
> ⛔ Modele SAYFA değil, o sahnede gereken KIRPILMIŞ TEK PANEL yüklenir
> (kılavuz §4.3 — ⚠️ bu kural depoda ÖLÇÜLMEDİ, dört eski paket tersini
> yazıyor; sapılırsa buraya yazılır).

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
T1 kask / vizör / basınç giysisi ......... ✅ 25/25 sahne, iki figür
T2 biçim kilidi metinle tutulmayan varlık  ✅ KASK GEOMETRİSİ — D146'nın
                                             üç vakasında da metin çapası
                                             tek başına tutmadı
T3 oranı sözle yazılamayan nesne ......... ✅ üs anatomisi [KART 13]
T4 insan dışı canlı ...................... ❌ yok
T5 tekrar eden insan dışı olay ........... ✅ BOŞALMA — 6 sahnede ve
                                             biçimi her seferinde AYNI
                                             olmak zorunda
T6 tekrar tekrar dönen varlık ............ ✅ kelepçe + ayak plakası
                                             (S0 · S1 · S10 · S18 · S20 ·
                                              S21 · S22)

→ ALTI TETİKLEYİCİDEN DÖRDÜ DOĞRU. Paket ZORUNLU.
```

---

## 1. 🎫 PAKET KÜNYESİ

```
FİLM:            THE OPEN CIRCUIT  ·  yatay 3-5 dk  ·  25 sahne / 4:09
TARİH:           07.09.2026
SAYFA SAYISI:    4   (RA · RB · RC · RD)
PANEL SAYISI:    18  (RA 6 · RB 4 · RC 4 · RD 4)
ÜRETEN SİSTEM:   ⬜ imaj modeli + sürüm (üretimde doldurulur)
DURUM:           ⬜ HİÇBİR SAYFA ÜRETİLMEDİ — dördü de ONAY bekliyor
```

---

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

> ⛔ Seed alanı doldurulmadan o sayfanın varlığı hiçbir sahnede üretilmez.
> ⚠️ Flow arayüzünde seed alanının varlığı bu depoda HENÜZ SINANMADI [D142];
> alan yoksa bu satır "kabul edilen kare dosya adı" olarak doldurulur.

| # | sayfa | varlık | öncelik | seed | SHA-256 | onay |
|---|---|---|---|---|---|---|
| 1 | **RA** | İKİ FİGÜR — giysi, kask geometrisi, ayrım eksenleri | 🔴 | ⬜ | ⬜ | ⬜ |
| 2 | **RB** | ÜS — dört modül, düğüm, mast, ayaklar | 🔴 | ⬜ | ⬜ | ⬜ |
| 3 | **RC** | KELEPÇE VE AYAK PLAKASI — dört durum | 🟠 | ⬜ | ⬜ | ⬜ |
| 4 | **RD** | BOŞALMANIN BİÇİMİ — dört aralık, iki yön | 🔴 | ⬜ | ⬜ | ⬜ |

```
ÜRETİM SIRASI [D168]:  RA → RD → RB → RC → S22 (doruk) → S19 → S24 → S0 → kalanı
⛔ RA onaylanmadan hiçbir insanlı sahne (25/25) üretilmez.
⛔ RD onaylanmadan hiçbir boşalma sahnesi (S0 · S7 · S10 · S15 · S18 · S22 · S23 · S24) üretilmez.
⛔ RB onaylanmadan hiçbir geniş plan (S6 · S7 · S8 · S18 · S23 · S24) üretilmez.
⭐ **RD SIRAYI RB'DEN ÖNCE ALDI (07.09 denetimi):** filmin İPTAL KAPISI
  S22'dir ve S22'nin tek konusu boşalmanın YÖNÜDÜR. RD tutmuyorsa film
  üretilmez — o yüzden en erken sınanacak ikinci sayfa odur, en geç değil.
```

---

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| varlık | sayfa | kaç sahnede | neden kaydı hak ediyor |
|---|---|---|---|
| UZUN OLAN (figür) | RA | 25 | T1 · kimliğin metinle tutulmadığı üç vaka [D146] |
| KISA/GENİŞ OLAN (figür) | RA | 25 | T1 · aynı + D69 klon sıcak noktası |
| KASK (ikisinde de aynı) | RA | 25 | T2 · **düz pencere + görünür çerçeve**, kubbe DEĞİL |
| ÜS (4 modül + düğüm + mast) | RB | 6 | T3 · KART 13 oran ve tekrar eden birim kayması |
| PENCERE ŞERİDİ (4 adet) | RB | 12 | filmin sayacı ③ — sayı film boyu 4, yanan sayısı azalır |
| TOPRAKLAMA KELEPÇESİ | RC | 7 | T6 · novum taşıyıcısı |
| AYAK PLAKASI (4 adet) | RC | 6 | T6 · filmin sayacı ② |
| BOŞALMA (kıvılcım) | RD | 8 | T5 · biçimi her seferinde aynı olmak ZORUNDA |
| KESİCİ (el aleti) | RA p6 | 5 | AYRILIK'ın ve merkezî seçimin nesnesi |

---

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

```
KİR MERDİVENİ (figürler · monotonik · RA p3-p4 aynı sayfada, karşılaştırılabilir)
  FAZ 1  S0-S5    yalnız bot dikişlerinde ince pas-kahve toz
  FAZ 2  S6-S12   toz filmi bot, incik ve iki uyluk
  FAZ 3  S13-S18  toz göğüs kabuğu ve dış önkol; camın DIŞ kenarında
  FAZ 4  S19-S24  bütün giysi donuk pas-kahve + camın İÇİNDE kırağı halkası

CAM DURUMU (RA p5-p6 aynı sayfada — ⭐ tek değişken kırağı)
  DURUM A  temiz cam, silinmiş oval geniş        (S0-S18)
  DURUM B  içeride kırağı halkası, oval bir avuç (S20)
  DURUM C  halka kapanmış, oval dört parmak      (S23-S24)

ŞERİT SAYACI (üs · monotonik AZALAN · RB p2-p3 aynı sayfada)
  4 yanıyor (S1-S14) → 3 (S15) → 2 (S18) → 0 (S19-S24)

KIVILCIM ARALIĞI (RD · monotonik ARTAN · dördü de aynı sayfada)
  bir parmak ucu → iki parmak → bir eldiven eni → bir avuç açıklığı
  ⭐ VE DÖRDÜNCÜSÜNDE YÖN TERSİNİR: yukarıdan aşağı, toprağa.
```

---

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | RA | RB | RC | RD | kırpım (modele hangi panel yüklenir) |
|---|---|---|---|---|---|
| S0 · S1 | – | – | ✅ | ✅ | RC p1 (kelepçe açık) + RD p1 (aralık: parmak ucu) |
| S2 · S4 | kir faz 1 | – | ✅ | – | RC p2 (kelepçe kapalı) |
| S3 · S5 | ✅ p1-p2 | – | – | – | RA p1 (iki figür, ayrım eksenleri) |
| S6 · S8 | kir faz 2 | ✅ p1 | – | – | RB p1 (anatomi, dört şerit yanıyor) |
| S7 | kir faz 2 | ✅ p1 | – | ✅ | RB p1 + RD p2 (uzak, toz halkası) |
| S9 · S11 · S12 | ✅ p3 (faz 2) | – | ✅ | – | RA p3 + RC p3 (kırağı kabuklu flanş) |
| S10 | – | – | ✅ | ✅ | RC p2 + RD p2 (aralık: iki parmak) |
| S13-S17 | ✅ p4 (faz 3) | ✅ p2 | – | – | RA p4 + RB p2 (iç mekân + üç şerit) |
| S15 | – | ✅ p4 | – | ✅ | RB p4 (kapak yerinde ↔ çıkmış) + RD p3 |
| S18 | ✅ p4 | ✅ p3 | ✅ | ✅ | RB p3 (iki şerit) + RD p3 |
| S19 · S20 | ✅ p5 (durum B) | – | ✅ p4 | – | RA p5 + RC p4 (kabuk temizlenmiş) |
| S21 · S22 | – | – | ✅ p4 | ✅ p4 | RC p4 + **RD p4 (YÖN AŞAĞI)** |
| S23 · S24 | ✅ p6 (durum C) | ✅ p3 | – | ✅ p4 | RA p6 + RB p3 (sıfır şerit) |

```
BAŞLANGIÇ KARESİ KONTRATI [kılavuz §5.2 · D179]:
  Bu film 25/25 sahnede I2V koşar. Başlangıç karesi VARSA video promptu
  GÖRÜNÜŞÜ yeniden yazmaz — LOCKS satırı yalnız KONUMU ve DURUMU sabitler.
  ⛔ Ve başlangıç karesi değişimin ÖNCESİDİR: S15'te kapak yerinde,
    S19'da iki şerit yanıyor, S21'de kayış oturmamış [kapı ⑳b].

⛔ YENİDEN ÇAPALAMA ÇİZELGESİ: bu depoda hâlâ YAZILMADI [kılavuz §5.3].
  Kaç sahnede bir sayfaya geri dönüleceği ÖLÇÜLMEDİ. Bu film varsayılan
  olarak HER sahnede ilgili paneli yükler ve ölçüm borcu açık durur.
```


---

## 5b. 🔒 PANEL → KİLİT SÖZLEŞMESİ — her panel hangi cümleyi tutuyor

> ⭐ Bir referans sayfası, bir ruh hâli tahtası değil bir SÖZLEŞMEDİR:
> her panel, film promptunda yazılı BİR CÜMLEYİ ekranda sabitler.
> Panel o cümleyi tutmuyorsa panel değil, CÜMLE yeniden yazılır.

| panel | ekranda ne sabitler | filmdeki karşılığı (birebir kilit) |
|---|---|---|
| **RA p1** | iki figürün ayrım eksenleri | *"THE TALLER ONE stands a head taller… orange woven webbing band… RIGHT forearm and RIGHT thigh"* — 10 iki-figürlü promptta |
| **RA p2** | sırt yüzeyi | *"the back of each suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing"* — 20 promptta [D79·D139·kapı ⑮] |
| **RA p3** | **kask geometrisi** | *"a visible sand-grey metal rim, and set into that rim one flat pane of optically clear glass"* — ⭐ D146'nın üç kez ödediği ders |
| **RA p4** | kir merdiveni FAZ 4 | *"the whole suit is dulled all over with rust-brown dust"* — S19-S24 |
| **RA p5** | cam durumu B | *"a thin ring of white frost has begun to grow in from the rim, leaving a clear oval… about a hand wide"* — S20 |
| **RA p6** | cam durumu C + kesici | *"a ring of white frost… leaving a clear oval around the eyes about four fingers wide"* — S23·S24 · ⭐ ağzın kapanma mekanizması |
| **RB p1** | üs anatomisi + F kurulumu | *"exactly four sand-white modules in a row… The mast stands about two fifths of the frame height"* — S6 |
| **RB p2** | şerit sayacı 3 | S15 sonrası hâli · *"three window strips lit and one dark"* — S18 |
| **RB p3** | şerit sayacı 0 + ayakta | *"the outpost dark and upright, no strip lit"* — S23·S24 · ⭐ KAPI 4'ün tam sınavı |
| **RB p4** | basınç kapağı çifti | *"either seated flush in the drum's side or gone, never half-detached"* — S18'in ARA DURUM kilidi |
| **RC p1** | çene AÇIK | S0 · S10 · S20 · S21'in başlangıç kareleri [I2V t=0 · kapı ⑳b] |
| **RC p2** | çene KAPALI | S1 · S2 · S12 · S22'nin başlangıç kareleri |
| **RC p3** | kırağı kabuğu + kayma | *"the copper jaws slide off the white crust"* — S9 · S20, başarısız denemelerin ikisi |
| **RC p4** | sıyrılmış metal + birleşmiş uçlar | S21 · S22 · S24 |
| **RD p1** | aralık: bir parmak ucu | S0 · ⭐ NOVUM TAŞIYICISI, TEK KARE 0:04 [D157] |
| **RD p2** | aralık: iki parmak | S10 · sayaç ①'in ikinci kademesi |
| **RD p3** | aralık: bir eldiven eni | S15 · S18 |
| **RD p4** | **aralık: bir avuç · YÖN AŞAĞI** | S22 · ⛔ **FİLMİN İPTAL KAPISI** — bu panel tutmuyorsa film üretilmez |

```
⛔ TERSİ DE DOĞRUDUR: yukarıdaki 18 cümlenin biri promptta değişirse
  karşısındaki panel GEÇERSİZDİR ve yeniden üretilir. Paket ile promptlar
  tek yönlü değil ÇİFT YÖNLÜ bağlıdır.
```

---

## 5c. 🚫 RED PROTOKOLÜ — sayfa reddedilirse ya da yanlış gelirse

> Kaynak: `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` §2'nin iki cümlesi.

```
⭐ DEFTERİN ÖLÇÜLMÜŞ TEK AYRIMI:
   "Kelime reddi SÖZLÜKLE çözülür ve her seferinde çözüldü.
    Kompozisyon reddi sözlükle çözülmez — YERCEKIMI S8'de önce
    sözcükler değişti, YETMEDİ, kadraj değişti.
    Sözcük çözümünü kompozisyon reddine uygulamak, bu deponun
    ölçülmüş tek boşa emeğidir."

① MESAJ GELDİ Mİ, YOKSA ÇIKTI MI YANLIŞ?
   · model REDDETTİ  → ② ye git
   · model ÜRETTİ ama kabul sınavı düştü → ④ e git

② RED · MESAJI SINIFLANDIR ve deftere YAZ (MOTOR sütunu ZORUNLU)
   "can't make that type of…" / "real people" → PK ya da PB
   "I encountered an error…"                  → TK
   ⭐ İLERLEDİ Mİ? üretim görünür şekilde ilerleyip sonda mı düştü —
     bu sütun SONRADAN HATIRLANAMAZ, o an yazılır.

③ SINIFA GÖRE ÇÖZ — ve karıştırma
   PK (kelime) → sözlüğü ayıkla, YASAK YAZMA MALZEMEYİ TARİF ET [D123].
                 Bu pakette en olası aday RA'dır: iki yüz × altı panel
                 kişi tanımlama yüzeyidir [red defteri vaka 15].
                 İlk kısaltılacak yer: p5 ve p6'nın yüz cümleleri.
   PB (kompozisyon) → SÖZCÜĞE DOKUNMA, KADRAJI DEĞİŞTİR. En olası aday
                 RA p2 (yan yana iki sırt, yüzsüz) — YERCEKIMI S8'in
                 iptal olan karesiyle aynı aile. Çözüm: iki sırtı yan yana
                 değil ARD ARDA koy, ya da p2'yi tek figüre indir.
   TK (teknik) → aynı promptu tekrar dene. ⛔ AYNI OTURUMDA 3 RED /
                 0 BAŞARI varsa prompt kısaltma DENENMEZ; sorun üretim
                 tarafındadır, `PROB_KOSUSU.md` koşulur.

④ ÇIKTI YANLIŞ · sayfaya göre ilk bakılacak yer
   RA → kask KUBBE mi çıktı? [D146'nın üç vakası] → p3'ün çerçeve
        cümlesini panelin İLK cümlesi yap, sonra yeniden üret
   RB → MAKET gibi mi duruyor? → tilt-shift negatifi zaten var; kadrajı
        yatır (daha az yukarıdan), ön plandaki figürü büyüt
   RC → kabuk ISLAK/PARLAK mı? → "dry matte solid" cümlesini panelin
        başına al
   RD → çizgi DALLANDI mı ya da geride ışık mı kaldı? → panel sayısını
        4'ten 2'ye indir (p1 ve p4 yeter); kalabalık sayfa modeli
        şaşırtıyor olabilir

⛔ ÜÇÜNCÜ REDDEN SONRA SAYFA BÖLÜNÜR: altı panelli RA → 3+3 iki sayfa.
  Kılavuz §4.1'in bant tavanı zaten panel başına düşen dikkati ölçüyor.
```

---

## 5d. ▶️ KOŞU KARTI — operatörün eline geçen dört adım

| # | sayfa | kabul sınavı (tek soru) | düşerse |
|:--:|---|---|---|
| 1 | **RA** | *"Bu kaskın önü düz bir pencere mi, yuvarlak bir kubbe mi?"* + **gri tonlama sınavı**: `ffmpeg -i RA.png -vf hue=s=0 -y RA_gri.png` → renksiz hâlde iki figür hâlâ ayırt ediliyor mu? | ④ RA satırı |
| 2 | **RD** | *"Kıvılcım p4'te nereye gidiyor?"* → "aşağı / toprağa" değilse ⛔ | ④ RD satırı · ⛔ **film iptal riski** |
| 3 | **RB** | *"Bu bir maket mi?"* → "evet" ise ⛔ · ve p1↔p3'te mast aynı yükseklikte mi? | ④ RB satırı |
| 4 | **RC** | *"Kabuk ıslak mı?"* → "evet" ise ⛔ · p1↔p2 aynı kelepçe mi? | ④ RC satırı |

```
⭐ HER SAYFA İÇİN SIRA: üret → kabul sınavı → seed ve SHA-256 yaz →
   §2 tablosunda ONAY kutusunu işaretle. ⛔ ONAY işaretlenmeden o
   sayfanın kapsadığı hiçbir sahne üretilmez [KAPI 0].
⭐ SHA-256 komutu:  shasum -a 256 <dosya>
⭐ Gri tonlama sınavı 07.09.2026'da ffmpeg 8.1 ile FİİLEN kuru koşuldu
   ve çalışıyor [D142] — yazılmadan önce sınanmayan kapı yazılmaz.
```

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA RA · İKİ FİGÜR · ⬜

```
Photorealistic reference sheet, 16:9 landscape, six panels in two rows of three, thin plain mid-grey gutters between them, no border decoration.

SUBJECT — the two people of one film, and no one else appears on this sheet. Both wear the same matte sand-grey surface suit: a hard sand-grey torso shell, dark graphite ribbed arms and legs, graphite knee and elbow plates, black gloves and black boots. The back of each suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing. Each helmet is a hard sand-grey shell with a visible sand-grey metal rim, and set into that rim one flat pane of optically clear glass — zero tint, zero mirror coating, zero reflection of the environment; the pane is a flat front window in a frame and is not a smooth curved dome. No bare skin anywhere — none above the collar, none at the wrists, none at the ankles; cuff and glove meet in a closed ring, boot and leg meet in a closed ring.

PANEL 1 — TOP LEFT, THE PAIR, FULL FIGURE, CLEAN: both standing upright side by side, a body length apart, three-quarters to camera, arms relaxed, both faces readable through the clear panes. THE TALLER ONE stands a head taller than the other and wears a bright orange woven webbing band wound right around the RIGHT forearm and the RIGHT thigh, with a flat coil of braided webbing on her LEFT hip. THE SHORTER, BROADER ONE has a wider chest shell and a squarer shoulder line, and wears a bright electric blue woven webbing band wound right around the LEFT upper arm and the LEFT thigh, with a flat tool roll on his RIGHT hip. DIRT: fine rust-brown dust in the boot stitching only.

PANEL 2 — TOP MIDDLE, THE PAIR FROM BEHIND, CLEAN: the same two in the same order, from directly behind, showing that the back of each suit is one continuous smooth surface from collar to hip with nothing mounted on it, no pack, no tank, no hose, no housing. The orange strap shows on the taller one's right forearm, the bright electric blue on the shorter one's left upper arm.

PANEL 3 — TOP RIGHT, HELMET GEOMETRY, THREE-QUARTER: one helmet alone, empty and on a plain stand, in three-quarter view. The shell is hard sand-grey. A visible sand-grey metal rim runs all the way around a flat front window, and one flat pane of optically clear glass is set into that rim. The rim is a distinct raised frame with a visible edge, and the pane inside it is flat, not curved, not a bubble and not a dome. A short neck ring at the base is a closed collar seal.

PANEL 4 — BOTTOM LEFT, THE TALLER ONE, FULL FIGURE, DIRT PHASE 4: the same taller one in the same pose as panel 1, face readable through the clear pane. DIRT: the whole suit is dulled all over with rust-brown dust, heaviest on boots, shins, thighs, chest shell and outer forearms; rust-brown dust also sits on the OUTSIDE of the pane at its rim, while the centre of the pane stays wiped clear. This panel and panel 1 must be directly comparable — SAME person, SAME suit, ONLY the dust level differs.

PANEL 5 — BOTTOM MIDDLE, PANE STATE B, HEAD AND SHOULDERS: the taller one in close head-and-shoulders, three-quarters to camera. On the INSIDE of the flat pane a thin ring of white frost has grown in from the rim, leaving a clear oval around the eyes about a hand wide; her face stays fully readable through that oval. Rust-brown dust sits on the OUTSIDE at the rim. The frost is dry matte crystal with visible grain — it never runs and is never wet.

PANEL 6 — BOTTOM RIGHT, PANE STATE C AND THE TOOL: the shorter, broader one in close head-and-shoulders, three-quarters to camera, with the same frost ring on the INSIDE of his pane closed further, leaving a clear oval around the eyes about four fingers wide; his face stays readable. In his gloved hand at the bottom of the panel he holds a pair of plain heavy insulated cable cutters at hip height, jaws down.

CAMERA AND LIGHT ACROSS THE SHEET: soft even neutral key at five thousand kelvin with gentle fill, plain mid-grey seamless background in every panel, shadows soft but present. Every skin pore, woven weave, scuff, dust grain and crystal facet stays fully visible.

NEGATIVE: Exactly 2 human figures on this sheet and no others — no third person, no crowd, no duplicate, no reflection of another figure. The face, build and suit of each are IDENTICAL across every panel — no drifting, no morphing, no age or feature change between panels, and the two never swap height, strap colour, strap limb or hip object. The helmet pane is a FLAT window in a visible rim — no seamless dome, no bubble helmet, no single curved wrap-around pane, no frameless glass. No visor tint, no mirrored coating, no gold coating, no reflection of the room or of any figure on the glass, no HUD overlay, no display on the glass. No back-mounted unit on either suit — each back is one unbroken surface. No bare skin — none above the collar, none at the wrists, none at the ankles. No frost in panels 1-4. No dust in panels 1-3. 0% bloom, no glow, no soft focus, no haze. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, and none anywhere on the sheet — not on the suits, the helmet, the tool, the stand, the ground, the rock, the background or in the gutters; no patches, no badges, no flags, no labels, no panel titles, no captions, no watermark. No national flag, no agency logo, no mission patch, no painted emblem on either suit. The webbing bands are flat woven straps wound tight around the limb — they never flap, never ripple, never hang loose, and they never light up or glow. No airbrushing, no waxy or plastic skin, no beauty filter, no makeup, no jewellery. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

```
KÜNYE — SAYFA RA
KAPSAM:      S0-S24 · 25/25 sahne (iki figürün geçtiği her kare)
             ⚠️ 20 sahne GECE — RA'nın asıl sınavı ⑦'dir, renk değil.
KABUL SINAVI: ① kask ÇERÇEVELİ ve ön pencere DÜZ mü (kubbe ise RED) [D146]
              ② sırt paneli p2'de kesintisiz ve boş mu [D79 · D139]
              ③ boy farkı p1'de bir baş mı, bant KOLLARI doğru mu [D69]
              ④ p1 ↔ p4 aynı kişi mi (yalnız kir değişmiş)
              ⑤ p5 ↔ p6 kırağı halkası KAPANIYOR mu (açılmıyor)
              ⑥ camda yansıma / renk / kaplama VAR MI (varsa RED) [D79]
              ⑦ ⭐ **SİLUET SINAVI [ASTRONOT_DONANIM §2 · 07.09 denetimi]:**
                 p1 ve p2 gri tonlamaya çevrilir (`ffmpeg -vf hue=s=0`) ve
                 RENKSİZ hâlde ikisi hâlâ ayırt edilebiliyor mu?
                 Kanallar: BOY · kalçadaki nesnenin BİÇİMİ (yuvarlak kangal
                 ↔ düz alet rulosu) · o nesnenin YANI (sol ↔ sağ).
                 ⛔ Ayırt edilemiyorsa RED — bu filmin 20 sahnesi GECEDİR
                   ve orada renk okunmaz.
SEED:        ⬜        SHA-256: ⬜        ONAY: ⬜
```

---

### 📸 IMAGE PROMPT — SAYFA RB · ÜS · ⬜

```
Photorealistic reference sheet, 16:9 landscape, four panels in two rows of two, thin plain mid-grey gutters between them, no border decoration.

SUBJECT — one small surface outpost on a flat rust-brown plain, and the same outpost in every panel. Its anatomy is fixed and identical in all four: exactly FOUR low sand-white horizontal cylinder modules lying in one straight row, each about two body lengths across and seven body lengths long, each half buried in a banked berm of rust-brown regolith, and each carrying exactly ONE horizontal window strip along its flank — four modules, four strips. Exactly ONE low six-sided drum joins the four in the middle of the row and carries exactly TWO flat radiator panels lying on its roof, and one rectangular pressure panel set into its side. Exactly ONE lattice mast with exactly THREE guy-wires stands at the END of the module row, where the row stops. On the open ground outside the berm there are exactly FOUR flat steel bonding plates, one out from each module's far end. The plain around the outpost is empty open regolith with nothing else standing on it.

PANEL 1 — TOP LEFT, THE WHOLE OUTPOST, ALL FOUR STRIPS LIT: the whole outpost seen from eye level on top of the berm, from far enough back that the entire row of four modules sits inside the frame width, three-quarters along the row. The lattice mast stands about two fifths of the panel height and one module stands about one twelfth of it. One standing suited figure is small in the near foreground for scale, about a third of the panel height. All four window strips are lit warm. Last light, cinnamon-brown sky.

PANEL 2 — TOP RIGHT, SAME POSITION, THREE STRIPS LIT: the identical outpost from the identical camera position, height, lens and angle, at night, with three window strips lit warm and one dark. The mast still stands about two fifths of the panel height. The rectangular pressure panel is still seated in the drum's side. One standing suited figure small in the foreground.

PANEL 3 — BOTTOM LEFT, SAME POSITION, NO STRIP LIT: the identical outpost from the identical camera position, height, lens and angle, at night, with no window strip lit at all and the whole structure intact and upright. The rectangular pressure panel is GONE from the drum's side and there is a plain dark rectangular opening where it was. Two small suited figures stand at the foot of the mast, each with one small cool chest lamp, and those two lamps are the only light. This panel and panel 1 must be directly comparable — SAME outpost, SAME camera, SAME proportions, the mast still about two fifths of the panel height, ONLY the lighting and the pressure panel differ.

PANEL 4 — BOTTOM RIGHT, THE DRUM, CLOSE: the six-sided drum alone, from the side, filling the panel, with the two flat radiator panels visible on its roof. Left half of the panel: the rectangular pressure panel seated in the drum's side, complete, with a plain flush edge. Right half: the same drum with that panel gone, leaving a plain dark rectangular opening with a clean unburnt rim.

CAMERA AND LIGHT ACROSS THE SHEET: physically accurate perspective and scale in every panel. Panels 1, 2 and 3 are all shot on a wide lens from eye level on top of the berm, from one identical camera position far enough back to hold the whole row, so the outpost can be measured between them; they are NOT high-angle views and the camera never looks down on the outpost. The mast stands at the same end of the row in every panel.

NEGATIVE: Exactly 1 human figure in panels 1 and 2 and exactly 2 human figures in panel 3, and no others anywhere on this sheet — no third person, no crowd. Exactly four modules, one drum, two radiator panels, one mast, three guy-wires, four window strips and four bonding plates — in every panel, with no extra module, no extra mast, no antenna forest, no cable bundles, no hundreds of small repeated fittings, no domes, no towers. No vehicle of any kind — no lander, no rover, no ship, no wheels, no landing legs. The proportion of module to figure is identical in panels 1, 2 and 3. 0% bloom, no glow, no lens flare, no haze, no bloom around the window strips. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, and none anywhere on the sheet — not on the hulls, the drum, the mast, the ground, the rock, the berm, the background or in the gutters; no painted numbers, no hull markings, no labels, no panel titles, no captions, no watermark. Insulation and covers are rigid and taut — nothing billows, nothing flaps, nothing hangs loose. NO TILT-SHIFT LOOK, no miniature or toy-model read, no shallow depth of field on the structure — the far end of the row is as sharp as the near end. No national flag, no agency logo, no mission patch, no painted emblem or roundel on any surface. Ground tracks are dulled and partly filled with settled dust, unchanging. One low sun; shadows soft-edged and weak but the frame stays high-contrast — that softness is correct, not a rendering fault. Nothing is burning, nothing glows, no fire and no soot, and the opening in panel 3 and panel 4 has a clean unburnt rim. The horizon stays straight and unbroken — no canyon, no ridge, no mountains. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

```
KÜNYE — SAYFA RB
KAPSAM:      S6 · S7 · S8 · S13 · S15 · S17 · S18 · S23 · S24
KABUL SINAVI: ① p1/p2/p3 AYNI açı ve AYNI oran mı (kesir kayarsa RED) [KART 13]
              ② birim sayıları dört panelde de aynı mı: 4/1/2/1/3/4/4
              ③ mast HER panelde sıranın AYNI ucunda mı [D174 — yön nesneye bağlı]
              ④ p4'te açıklığın kenarı YANIK/İSLİ mi (öyleyse RED — basınç
                 olayı ateş değildir)
              ⑤ kadrajda araç VAR MI (varsa RED)
SEED:        ⬜        SHA-256: ⬜        ONAY: ⬜
```

---

### 📸 IMAGE PROMPT — SAYFA RC · KELEPÇE VE AYAK PLAKASI · ⬜

```
Photorealistic reference sheet, 16:9 landscape, four panels in two rows of two, thin plain mid-grey gutters between them, no border decoration.

SUBJECT — one hand tool and one ground fitting, the same two objects in every panel. The tool is a heavy hand-sized bonding clamp with two bare copper jaws, a plain steel body, a single side lever, and a braided metal strap tail leaving the back of it. The fitting is a flat steel bonding plate set level into rust-brown regolith, with one raised edge along its near side that the copper jaws can close on.

PANEL 1 — TOP LEFT, CLAMP OPEN, THREE-QUARTER: the clamp alone on the plate, jaws open about a finger's width above the raised edge, lever up, braided strap tail lying loose behind it. The plate's raised edge is bare grey metal, clean. No hands.

PANEL 2 — TOP RIGHT, CLAMP CLOSED, SAME ANGLE: the identical clamp from the identical position and angle, jaws closed on the raised edge, lever down, the braided strap tail drawn flat against the plate and running away out of frame. This panel and panel 1 must be directly comparable — SAME clamp, SAME plate, SAME angle, ONLY the jaws and the lever differ.

PANEL 3 — BOTTOM LEFT, CRUSTED EDGE, CLOSE: the plate's raised edge alone, close, with a thin dull white crust lying over its upper surface — a dry matte solid deposit with visible grain and fine cracks, never wet, never running, never glossy. The copper jaws of the clamp rest against the crust without gripping it and one jaw has slid a hand's width, leaving a shallow bright scrape in the crust.

PANEL 4 — BOTTOM RIGHT, SCRAPED CLEAN AND JOINED, CLOSE: the same edge from the same angle with the white crust scraped away in one bare grey patch, a rim of crust still around that patch. The clamp is closed on the bare grey metal, and two thick cut ends of an armoured cable are joined into the braided strap tail beneath the jaws, lying flat on the plate.

CAMERA AND LIGHT ACROSS THE SHEET: soft even neutral key at five thousand kelvin with gentle fill, plain mid-grey seamless background behind the near objects in every panel, shadows soft but present. Panels 1 and 2 share one identical camera position, height and lens; panels 3 and 4 share another. Every metal grain, copper scratch, braid strand and crystal facet stays fully visible.

NEGATIVE: Exactly 0 human figures on this sheet — no person, no face, no figure anywhere. The sheet shows one clamp and one plate design only — no second clamp variant, no alternative tool, no split diagram, no cutaway. The clamp is identical in all four panels: two bare copper jaws, plain steel body, one side lever, one braided strap tail — no extra jaws, no extra levers, no springs added or removed. In every panel the jaws have NO INTERMEDIATE STATE — either fully open or fully closed on the edge, never half-closed, never mid-travel, never bending. No human figure, no face, no hand in panels 1, 2 and 3. 0% bloom, no glow, no soft focus, no haze. No spark, no arc, no light of any kind coming off the metal; no continuous glow, no plasma beam, no lightning, no electrical fire, nothing burns and nothing keeps burning. The white crust is a dry matte solid — it never melts, never runs, never drips and is never wet or glossy. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, and none anywhere on the sheet — not on the clamp, the plate, the cable, the ground, the rock, the background or in the gutters; no measurement marks, no graduation ticks, no part numbers, no labels, no panel titles, no captions, no watermark. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

```
KÜNYE — SAYFA RC
KAPSAM:      S0 · S1 · S2 · S4 · S10 · S18 · S20 · S21 · S22
KABUL SINAVI: ① p1 ↔ p2 aynı kelepçe, aynı açı mı (yalnız çene/kol değişmiş)
              ② p3'te kabuk MAT ve KURU mu (parlak/ıslaksa RED)
              ③ p4'te kazınmış yama ile kalan kabuk sınırı okunuyor mu
              ④ sayfada kıvılcım VAR MI (varsa RED — kıvılcım RD'nin işi)
SEED:        ⬜        SHA-256: ⬜        ONAY: ⬜
```

---

### 📸 IMAGE PROMPT — SAYFA RD · BOŞALMANIN BİÇİMİ · ⬜

```
Photorealistic reference sheet, 16:9 landscape, four panels in two rows of two, thin plain mid-grey gutters between them, no border decoration.

SUBJECT — one single electrical discharge, photographed four times at four different lengths, always the same shape: one thin hair-fine straight blue-violet line crossing an air gap between two pieces of metal, present for an instant only, leaving nothing behind it. In every panel the line is thin, straight and single, it has no branches, no forks, no halo and no afterglow, and no surface it touches is heated, marked, scorched or lit up afterwards.

PANEL 1 — TOP LEFT, GAP OF ONE FINGERTIP: extreme close-up of a black gloved fingertip approaching a bare copper jaw, with a gap between them about as wide as a fingertip. One thin straight blue-violet line stands in that gap, leaving the copper and reaching the glove.

PANEL 2 — TOP RIGHT, GAP OF TWO FINGERS: the same kind of gap, now about two fingers wide, between the same bare copper jaw and the raised edge of a steel plate. One thin straight blue-violet line stands in it, leaving the plate and reaching the copper. Same shape, same thinness, only longer.

PANEL 3 — BOTTOM LEFT, GAP OF ONE GLOVE'S WIDTH: a wider view, the gap now about as wide as a glove, between the bright cut end of a heavy cable lying on rust-brown regolith and the rim of a steel hatch frame. One thin straight blue-violet line stands in it. The regolith immediately under the line is lit only for that instant and is not scorched.

PANEL 4 — BOTTOM RIGHT, GAP OF ONE OPEN HAND, AND THE DIRECTION IS DOWNWARD: a braided metal strap running from the top of the panel down to a flat steel plate set in the ground, with a black gloved hand resting on the strap halfway down. One thin straight blue-violet line runs DOWNWARD along the strap, from the top of the panel past the resting glove without touching it, and enters the steel plate at the ground. This panel and panels 1-3 must be directly comparable — SAME thin straight line, SAME colour, ONLY the length and the direction differ.

CAMERA AND LIGHT ACROSS THE SHEET: soft even neutral key at five thousand kelvin with gentle fill so the metal and the glove read fully, plus the brief cold blue-violet edge the line itself puts on the nearest metal. Plain mid-grey seamless background in panels 1 and 2; plain dark ground in panels 3 and 4. Every metal grain, braid strand and glove seam stays fully visible.

NEGATIVE: Exactly 0 human figures on this sheet — no person and no face anywhere; only one gloved hand appears where a hand is shown. Each panel shows exactly ONE thin straight hair-fine line and no other light at all — no second line, no branching, no forking, no tree shape, no web, no halo, no corona, no bloom around the line. The line has NO INTERMEDIATE STATE — it is either fully present at full brightness or wholly absent, never fading in, never fading out, never leaving a trail, never partly drawn. No continuous glow, no plasma beam, no laser, no lightning bolt, no ball of light, no electrical fire, no sparks flying off as particles, nothing burns and nothing keeps burning. Nothing that the line touches is scorched, blackened, melted, pitted or left lit. The line never touches the glove in panel 4. No human face anywhere, and no figure other than the one gloved hand where a hand is shown. 0% bloom, no glow filter, no soft focus, no haze, no lens flare. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, and none anywhere on the sheet — not on the metal, the glove, the ground, the rock, the background or in the gutters; no measurement marks, no arrows, no callouts, no panel titles, no captions, no watermark. No stylisation, no illustration, no CGI look, no video game render. Photorealistic with 35mm film grain.

Output: 16:9, 1920x1080, no text, no watermark.
```

```
KÜNYE — SAYFA RD
KAPSAM:      S0 · S1 · S6 · S7 · S10 · S15 · S18 · S22 · S23 · S24
KABUL SINAVI: ① dört panelde de çizgi TEK, İNCE ve DÜZ mü (dallanıyorsa RED)
              ② hiçbir yüzey yanmış/kararmış/erimiş mi (öyleyse RED)
              ③ p4'te yön AŞAĞI mı ve eldivene DEĞMİYOR mu — ⭐ filmin
                 doruğu bu tek panele bağlıdır
              ④ çizgi sönünce geriye ışık kalıyor mu (kalıyorsa RED)
⭐ RD ONAYLANMADAN S22 ÜRETİLMEZ — ve S22 filmin İPTAL KAPISIDIR [PLAN §ÜRETİM SIRASI].
SEED:        ⬜        SHA-256: ⬜        ONAY: ⬜
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

```
BUGÜN KOŞABİLENLER (kılavuz §6.1 · python3 · bash · ffmpeg · göz):
□ ① prompt_kontrol.py bu dosyayı DOSYA modunda denetledi ve BLOCK yok
□ ② dört sayfanın dördü de üretildi ve KABUL SINAVI maddeleri tek tek işaretlendi
□ ③ RA p1 ↔ RA p4 · RB p1 ↔ RB p3 · RC p1 ↔ RC p2 · RD p1 ↔ RD p4
     çiftleri yan yana konup GÖZLE karşılaştırıldı (tek değişken kuralı)
□ ④ seed alanları dolduruldu · dosyaların SHA-256 özeti yazıldı
□ ⑤ üretim sırasının ilk halkası (RA) onaylanmadan hiçbir sahne başlamadı

⛔ MAKİNE EŞİKLERİ YAZILMADI [kılavuz §6.2]. Yüz benzerliği, algısal
   uzaklık ve renk farkı için dışarıdan gelen sayılar (ArcFace · LPIPS ·
   ΔE) bu depoda ÖLÇÜLMEDİ ve kaynakları doğrulanamadı; kapı olarak
   yazılmadı. Kabul bugün GÖZLEdir ve bu dürüst kayıttır.
```

---

## 8. ⬜ BEKLİYOR

```
⬜ Dört sayfanın dördü de ÜRETİLMEDİ — paket bugün YAZILI, ONAYLI DEĞİL.
⬜ Seed / SHA-256 / ONAY sütunları boş.

⭐ 07.09.2026 DENETİMİNDE PAKETE İNEN SEKİZ DEĞİŞİKLİK:
   ① RB'nin kamera geometrisi filmin DÜZELTİLMİŞ F kurulumuyla eşitlendi.
      Paket "yukarıdan sığ açı" diyordu, film artık 47 m'den GÖZ HİZASI —
      ikisi ÇELİŞİYORDU ve referans yanlış kadrajı kilitleyecekti.
   ② UZAY_USSU §6 [YÜZEY ÜSSÜ · MARS] negatifi pakette HİÇ YOKTU (0 geçiş).
      En pahalı eksik satır MAKET/TILT-SHIFT okumasıydı — ve maket riski
      bütün pakette en çok RB'dedir.
   ③ ARA DURUM YASAĞI RC ve RD'ye indi: RC çene açık↔kapalı, RD kıvılcım
      var↔yok. Filmin dört ARA DURUM kilidinin KAYNAĞI bu iki sayfadır.
   ④ RA'ya amblem/bayrak yasağı + "bant dokuma, kıpırdamaz, ışımaz".
   ⑤ RD'nin önceliği 🟠 → 🔴 ve üretim sırasında RB'nin ÖNÜNE alındı:
      filmin İPTAL KAPISI (S22) RD'ye bağlıdır, sona bırakılamaz.
   ⑥ §5b PANEL → KİLİT SÖZLEŞMESİ: 18 panelin 18'i, filmde birebir hangi
      cümleyi tuttuğunu gösteriyor — ve bağ ÇİFT YÖNLÜDÜR.
   ⑦ §5c RED PROTOKOLÜ (red defterinin ölçülmüş ayrımı üstünden: kelime
      reddi ≠ kompozisyon reddi) + §5d KOŞU KARTI.
   ⑧ RA'ya ⑦ SİLUET SINAVI: 20 sahne gece, orada renk okunmaz.
⬜ Flow arayüzünde seed alanının varlığı sınanmadı [D142].
⬜ §4.3'ün yükleme kuralı (sayfa mı, kırpılmış panel mi) ÖLÇÜLMEDİ;
   bu film varsayılan olarak KIRPILMIŞ PANEL yükler ve sapma olursa
   buraya yazılır.
⬜ Yeniden çapalama çizelgesi yok [kılavuz §5.3] — kaç sahnede bir
   sayfaya dönüleceği ölçülmedi.
```
