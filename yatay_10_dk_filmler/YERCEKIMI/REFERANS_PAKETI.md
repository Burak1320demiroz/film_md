# 🧷 YERÇEKİMİ — Referans Paketi

## ADIM 3 — Kimlik Çapası Referans Sayfaları
### 6 sayfa × 4 panel (Perde I + Faz 4) + 3 sayfa Perde II/III | 16:9

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR.** Sıra: bu dosya → onay
> → seed kilidi → `FAZ_01_GOREV/FAZ_01_GOREV.md` sahneleri.
> Format kuralı (`../README.md` ADIM 3): 120 imajlık hatta çapa
> kilitlenmeden faz üretilmez; **her faz başında** çapa imajı bir önceki
> fazın çıktısından DEĞİL, bu dosyadaki master'dan üretilir.
>
> ⭐ **Biçim kararı:** varlık başına TEK SAYFA, sayfa başına TAM 4 PANEL
> (THE UPHILL DARK emsali, 17.08.2026). Gerekçe: bu filmin devamlılık
> riski iki DURUM arasındadır — platform/mekik dalga ÖNCESİ ↔ SONRASI,
> istasyon sağlam ↔ hasarlı, oksijen halkası 6/6 → 1/6. Panel sayfası bu
> çiftleri AYNI ÇAĞRIDA çizer; tek görsel çizmez. Bedeli (çözünürlük ¼,
> oluklara metin sızma riski) ve üç önlemi §0'da.
>
> Tüm promptlar **Ders 34** uyumlu (özel ad yok), **Ders 79** uyumlu (A'nın
> sırtı düz, vizör berrak ama görünür), **yazısız** (sayfa, oluk, panel:
> 0 harf). Karakter blokları `../README.md` Character Bible ile ve
> `FAZ_01_GOREV/FAZ_01_GOREV.md` promptlarıyla KELİMESİ KELİMESİNE aynıdır.

---

# 0. ⚠️ NEDEN BU DOSYA VAR — VE ÜÇ ÖNLEM

```
ÖLÇÜLMÜŞ SEBEP (Cold Burn, 07.08.2026): dört varlığın tanımı 60 promptta
kelimesi kelimesine aynı yazıldı — ve yetmedi. Metin çapası modelin aynı
CÜMLEYİ okumasını sağlar, aynı NESNEYİ çizmesini sağlamaz.
BU FİLMDE İKİ EK RİSK:
  ① 120 imaj — format README'si 5. fazdan sonra yüzün süründüğünü yazar;
    faz başı kimlik yenileme protokolü bu sayfalara döner.
  ② A karakteri iki DURUMDA yaşar: kasklı (S1-47) ve kasksız (S48-120).
    İki durum iki ayrı sayfadır (RA · RF); ikisinde de yüz bloğu aynı.

PANEL SAYFASININ BEDELİ VE ÜÇ ÖNLEM (her promptta uygulanmıştır):
  ① Oluk dili: "thin neutral mid-grey gutters" — oluk AYIRICIDIR,
     yerleşim alanı değil.
  ② Negatifte oluk ADIYLA geçer: "no text, labels, captions, arrows,
     callouts, dimension lines, panel titles or watermarks anywhere on
     the sheet or in the gutters."
  ③ "maximum resolution" + 16:9 + panel başına tek konu. §4 kapısı:
     panel içi detay (yara izi, halka segmentleri, cıvata başı) 120 px
     kırpımda okunmuyorsa sayfa atılır, o varlık TEK GÖRSEL üretilir.
```

---

# 1. 📋 ÜRETİM SIRASI VE SEED TAKİP TABLOSU

| # | Sayfa | Panel | Ne | Öncelik | Seed | Durum |
|---|---|:---:|---|:---:|---|:---:|
| **RA** | MÜHENDİS (A) — KASKLI | 4 | 3/4 tam boy · profil · SIRT (düz) · yüz CU | 🔴 ZORUNLU | | ☐ |
| **RB** | EKİPMAN (A + B) | 4 | bilekler · halka merdiveni 6→1 · kanca+kalça halkası · MMU kolu 2/4 | 🔴 ZORUNLU | | ☐ |
| **RC** | KOMUTAN (B) — MANEVRA PAKETİ | 4 | 3/4 tam boy · ⭐ p2 APARAT (sırt) · ⭐ p3 A+B yan yana · yüz CU | 🔴 ZORUNLU | | ☐ |
| **RD** | PLATFORM + MEKİK | 4 | sağlam ↔ HASARLI (aynı kadraj) · panel CU · mekik 3/4 | 🔴 ZORUNLU | | ☐ |
| **RE** | İSTASYON DIŞ | 4 | sağlam ↔ HASARLI (aynı kadraj) · airlock+halat demeti · kapsül konisi | 🔴 F3'ten önce | | ☐ |
| **RF** | MÜHENDİS (A) — KASKSIZ | 4 | 3/4 tam boy · profil · yüz CU · cenin pozu | 🟠 F4'ten önce | | ☐ |
| **RG** | İSTASYON İÇ | 4 | koridor · delik panel · hoparlör/telsiz · **p4 airlock içi (S48)** | 🟠 **F4'ten önce** (29.08 düzeltmesi — S48 zaten iç mekândır; "F5'ten önce" yanlıştı) | | ☐ |
| RH | KAPSÜL İÇ | 4 | kabin 3 koltuk · lomboz · vana+halka · kırmızı kapaklı kol | ⏳ F5'ten önce | | ☐ |
| **RI** | ZEMİN | 4 | kuru göl yatağı · kapsül yatık+paraşüt · çatlak kil CU · sabah ışığı | 🟠 **F9'dan önce** (30.08 düzeltmesi — S107'de paraşütün altında zemin görünüyor) | | ☐ |

```
ÜRETİM SIRASI — kapı kapı:
RA   A ÖNCE: filmin 120 sahnesinin 107'sinde tek insan odur.
     ⛔ p4 (yüz) 120 px'te okunmuyorsa sayfa atılır.
RC   B + ⭐ KLON KAPISI: p3 iki figürü yan yana koyar. Boy farkı (15 cm),
     şerit rengi (turuncu/lacivert) ve sırt (temiz omuz hattı ↔ omuzdan
     taşan paket) üçü de okunmuyorsa sayfa reddedilir. Depodaki üç klon
     vakası (Stone Sky · Unbroken City · Starless Circle) bu panelle
     yakalanırdı.
     ⭐ p2 artık APARAT PANELİDİR (31.08 revizyonu): manevra paketi
     büyütüldü ve modernleştirildi — sayfanın işi yalnız B'yi değil,
     O PAKETİ kilitlemek. Paket omuz hattından taştığı için ayrışma
     artık RENGE değil SİLUETE de dayanıyor: uzak kadrajda (S11 · S45)
     iki figür yüz görünmeden ayrılabiliyor.
RB   Ekipman: halka merdiveni (p2) filmin SAYACIDIR — altı durum tek
     çağrıda; sahne promptları "N of six segments lit" der, bu sayfa
     neyin nasıl göründüğünü kilitler.
RD   Platform+mekik: p1 ↔ p2 farkı YALNIZ hasar olmalı (kol kopuk,
     panel bükük, mekik delik, kargo kapağı kopmuş). Başka fark = ret.
RE   İstasyon: p1 ↔ p2 farkı YALNIZ sol kanat + delinmiş modül.
RF   A kasksız: yüz bloğu RA p4 ile aynı; fark yalnız yaka halkası açık,
     saç serbest. RA p4 ↔ RF p3 yan yana konur, aynı yüz değilse ret.

FAZ_1 DOSYASININ "REFERANS" SATIRLARI → SAYFA:
  A master (kasklı) = RA · B master (MMU'lu) = RC · platform master =
  RD p1/p3 · mekik master = RD p4 · eldiven/manşet/bilek detayı = RB ·
  MMU kumanda kolu = RB p4 · sırt açısı (B) = RC p2
```

---

# 2. 🗺️ SAHNE → REFERANS EŞLEME (Perde I + Faz 4 · S1-S48)

> Sahne üretirken ilgili sayfanın TAMAMI yüklenir (model bütün panelleri
> görür). Parantez = o sahnenin kadrajına en yakın panel.

| Sahne | Yüklenecek | Kadraj paneli |
|---|---|---|
| S1 · S2 · S10 · S11 · S12 | RA + RD (+RC S10/S11) | RA p1 · RD p1 (sağlam) |
| S3 · S7 | RC + RD | RC p2 (sırt/çerçeve) · RD p3 |
| S4 | RA | RA p4 (yüz) |
| S5 · S8 | RB | RB p3 (eldiven/kanca) · RB p1 (bilekler) |
| S6 | RB + RC | RB p4 (MMU kolu 2/4) |
| S9 | RA + RD | RA p2 (profil/sırt) · RD p3 |
| S13-S15 · S17 · S22 | RD | RD p1 → p2 (dalga anında sağlam→hasarlı) |
| S16 · S18-S21 · S23-S24 | RA + RD p2 + (RC S23-24) | RD p2 (HASARLI) |
| S25 · S28 · S29 | RA (+RE) | RA p2 profil · RA p1 tam boy · RA p3 sırt/OTS |
| S26 · S34 | RC (+RB) | RC p2 sırt/çerçeve · RC p4 yüz CU + RB p4 şerit |
| S27 · S31 · S33 · S35 · S36 | RA + RC + RE | RC p3 (iki figür) + **RE p2** (HASARLI) |
| S30 | RB | RB p1 bilekler + RB p2 (4/6 → 3/6 basamakları) |
| S32 | RE | **RE p2** tam boy + RE p4 kapsül konisi (insansız) |
| S37 · S46 | RA + RE | **RE p3** (airlock yüzeyi + halat demeti — geometri buradan donar) |
| S38 · S42 | RA | RA p4 (yüz CU) |
| S39 · S41 | RA + RE | **RE p3** halat dokusu + RA p1 (bot/diz şeridi) · ⛔ İKİZ: aynı seed |
| S40 | RC | RC p4 (yüz CU) |
| S43 | RA + RC + RB | RC p2 (sırt/çerçeve profili) + **RB p3** (karabina) + RA p1 |
| S44 · S45 | RA + RC + RE | **RE p2** (hasarlı gövde / tam boy istasyon) |
| S47 | RA + RE | RA p3 (sırt, düz silüet) + **RE p3** (kapak + uzun dış kol) |
| S48 | **RF** + **RG** | **RF p4** (cenin pozu) + **RG p4** (airlock iç yüzü + hortumlar) |

> ⛔ **F3'ten itibaren istasyon HER SAHNEDE HASARLIDIR (RE p2).** RE p1
> yalnız karşılaştırma için yüklenir, kadraj çapası değildir. MMU şeridi:
> S33'te 1/4 kadrajda, S34'te sahne İÇİNDE 0/4'e söner (RB p4 iki durumu
> da taşır).
> ⛔ **S37-S47 TEK YÜZEYDE geçer: RE p3.** Airlock kapağı, uzun dış kol,
> girintili turuncu tutamak ve handrail direğine dolanmış üç katlı halat
> demeti — bu dördü RE p3'te donar ve on bir sahne boyunca değişmez.
> ⛔ **S48 iki ONAYSIZ sayfaya bağlıdır (RF + RG p4).** İkisi de yoksa
> S48 ÜRETİLMEZ; RF p3 ile RA p4 yan yana konur, aynı yüz değilse faz durur.

---

# 3. 📸 SAYFALAR

## 📸 IMAGE PROMPT — SAYFA RA · MÜHENDİS (A), KASKLI

> Seed: `________` · tarih: `__.__.____` · durum: ☐

```
A single photorealistic 16:9 character reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. The same one woman appears in every panel, identical in
every detail; the backdrop in every panel is a plain flat dark-grey
studio wall with no horizon and no props; the lighting in every panel
is one hard white key from the upper screen-right and a soft cool
blue-white fill from below screen-left, shadows crisp. Exactly one
human figure per panel, human count 1 in each.

THE SUBJECT (identical in all four panels): A 38-year-old woman flight
engineer, 1.70 metres tall, slim and upright: oval face, soft defined
jawline, light wheat-toned skin with visible pores, thin straight
nose, dark hazel eyes, a short vertical pale scar on her LEFT temple
near the hairline, dark chestnut jaw-length hair tucked behind both
ears. Warm off-white pressure suit with ORANGE reinforcement stripes
on shoulders, knees and glove cuffs, a soft chest panel with three
small coloured lights and no numerals, a six-segment amber oxygen
ring on her LEFT wrist, a steel mechanical watch on a black strap
over her RIGHT glove cuff, its hands stopped. Her back silhouette is
flat: smooth off-white shell fabric with one vertical seam down the
spine and a low webbing waist belt, and no pack, tank, hose or cable. Her helmet is a rigid white shell with a flat rectangular front glass
measuring 24 by 16 centimetres, held in a visible bright metal frame the
width of a finger; the glass is optically clear, zero tint, no mirror
coating, and her face is
fully readable through it. A slim orange-and-white tether line hangs
from a small steel ring at her hip, its karabiner clipped to nothing.

PANEL 1 (top-left): full body, three-quarter front, weightless
neutral pose — feet together, arms held slightly away from the body,
gloves open and empty, expression calm and neutral; helmet to boots
in frame, true 1.70-metre proportions.
PANEL 2 (top-right): full body, exact left-side profile facing
screen-left, same pose; the flat back reads clearly against the wall
— nothing projects behind the shoulders or the collar ring.
PANEL 3 (bottom-left): full body seen directly from behind: flat
back, the collar ring, ORANGE shoulder stripes, the tether ring at
the hip; no pack, no tank, no hose, no cable anywhere.
PANEL 4 (bottom-right): close-up of the helmet and face,
three-quarter front, eyes open and level, mouth closed: the visor is
a distinct clear glass surface with one thin highlight line; the scar
on the LEFT temple, the hair tucked behind the ears and the pore
texture of the skin all readable.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign. Exactly one human figure per panel —
no duplicates within a panel. Identical face, bone structure and eye
spacing in all four panels; the scar stays on the LEFT temple; stripes
stay ORANGE. The visor never becomes tinted, mirrored or opaque and
never disappears. No back-mounted unit of any kind. 0% bloom, no glow
filter, no lens flare, no waxy or smoothed skin, no airbrushing. No
CGI or video-game look. Photorealistic, 35mm film grain.
```

---

## 📸 IMAGE PROMPT — SAYFA RB · EKİPMAN (A + B)

> Seed: `________` · tarih: `__.__.____` · durum: ☐
> ⭐ p2 = OKSİJEN HALKASI MERDİVENİ (6/6 → 4/6 → 3/6 → 2/6 → 1/6 → 1/6
> yanıp sönen): filmin sayacı. Sahne promptları "N of six segments lit"
> yazar; nasıl göründüğü burada kilitlenir.

```
A single photorealistic 16:9 equipment reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. Every panel is a macro close-up on a plain flat dark-grey
studio surface, lit by one hard white key from the upper screen-right
and a soft cool blue-white fill from below screen-left, crisp shadows.
No face in any panel; the only human presence is gloved hands and
forearms. Human count: hands only, no face on the sheet.

PANEL 1 (top-left): two off-white gloved wrists resting side by side
on an ORANGE handrail sleeve, seen from above. On the RIGHT cuff,
screen-right: a steel mechanical wristwatch on a black leather strap
buckled over the glove cuff, a scratched crystal, a plain dial with
no numerals, hour and minute hands stopped. On the LEFT wrist,
screen-left: a slim ring of six square amber light segments set into
the cuff, all six lit steadily, no numerals. ORANGE cuff stripes on
both gloves.
PANEL 2 (top-right): a ladder of six identical LEFT-wrist oxygen
rings laid out in two rows of three on the grey surface, the same
ring photographed six times in six states, all else identical: six
of six segments lit; four of six lit; three of six lit; two of six
lit; one of six lit; one of six lit but dimmer, mid-blink. Dark
segments are matte black recesses; lit segments are small, steady,
sharp-edged amber lights with no halo.
PANEL 3 (bottom-left): the tether hardware on a warm off-white suit
hip: a small steel ring sewn into the suit, an orange-and-white
braided line, and its steel karabiner with a spring gate, open; next
to it the RIGHT glove, off-white with an ORANGE cuff stripe, fingers
closed around a dull steel latch lever on a grey painted panel cover,
a captive bolt head with a raised rim beside the lever.
PANEL 4 (bottom-right): a big off-white gloved hand with a NAVY cuff
stripe resting on the forward control arm of a white aluminium
thruster frame: a white tube with a moulded grip and a small round
knob at its top; along the top of the arm a recessed strip of four
square amber light segments, the two nearest the grip lit steadily,
the two beyond them dark; one corner of the white frame and one small
nozzle visible behind, soft.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — the watch dial and the rings carry
no numerals. No faces anywhere on the sheet. Gloves keep a clear
boundary with every object — no merging, no extra fingers. 0% bloom,
no glow filter, no halo around the amber segments, no lens flare.
Photorealistic, 35mm film grain.
```

---

## 📸 IMAGE PROMPT — SAYFA RC · KOMUTAN (B), MANEVRA PAKETİ + ⭐ KLON KAPISI

> Seed: `________` · tarih: `__.__.____` · durum: ☐
> ⛔ p3 KLON KAPISI: iki figür yan yana; boy farkı 15 cm + turuncu/lacivert
> + temiz omuz hattı ↔ omuzdan taşan paket üçü de okunmuyorsa sayfa REDDEDİLİR.

```
⭐ 31.08.2026 REVİZYONU — SIRTTAKİ APARAT BÜYÜTÜLDÜ VE MODERNLEŞTİRİLDİ
   (proje sahibi talebi: "daha büyük ve modern durmalı")

ÖNCE (1984 NASA MMU siluetine yakın)
  "rigid white aluminium thruster frame … as deep as a forearm, two
   control arms reaching forward like armrests, eight small nozzles
   at its corners"
   → ölçü YOK (yalnız "bir önkol kadar"), açık boru kafes, 8 meme

ARA TUR (31.08, REDDEDİLDİ) — kavisli kabuk + çıkıntılı pod'lar
  Omuzların üstünden dönen kavisli kompozit kabuk, 20 cm eğik kollar
  üzerinde yumruk büyüklüğünde dört itici pod'u.
  ⛔ PROJE SAHİBİ REDDETTİ: "günümüzde olanlar gibi dikdörtgen bişi
     olmalı." Haklı — kavis + çıkıntı bilimkurgu aksesuarı okutuyordu,
     gerçek donanım okutmuyordu. Kayda geçiyor ki aynı yol iki kez
     denenmesin [D74].

SONRA — DÜZ DİKDÖRTGEN LEVHA, sayı ile yazıldı
  · tek parça mat beyaz levha        60 × 78 × 24 cm
  · ⭐ ENİNDEN YÜKSEK → arkadan TEK TEMİZ DİKDÖRTGEN okunur
  · dört köşe kare, yalnız hafif yuvarlatılmış — modern sert
    ekipman çantası gibi; kavis YOK
  · ön yüz 2 düz gömme füme dikişle 3 yatay panele bölünür
  · üst kenarda gömme bir taşıma rayı
  · dört köşede YÜZEYLE AYNI HİZADA sığ kare yuva; her yuvada kare
    dizilmiş 4 meme = TOPLAM 16 · ⛔ hiçbir şey dışarı çıkmaz
  · iki DÜZ dikdörtgen kesitli kumanda kolu alt köşelerden öne
    katlanır, kalça hizasında düz füme tutamakla biter
  · omuz hattından iki yandan 5'er cm taşar   ← "büyük" burada ölçülür
  · iki renk ve iki renk yalnız: mat beyaz gövde + koyu füme
    dikiş/yuva/tutamak
  ⛔ Kavisli değil · borulu değil · organik değil · kanatsız · tanksız
     · hortumsuz · kolda/ayakta duran hiçbir parça yok

⭐ NEDEN "MODERN" BİR SIFAT DEĞİL, GEOMETRİ OLARAK YAZILDI [D146 dersi]
   D146: "seamless visor" modele KUBBE yaptırıyordu — sıfat, model
   elinde kontrolsüz bir biçime dönüşür. Aynı tuzak burada da var:
   "modern jetpack" yazsaydık model çizgi film sırt roketi üretirdi.
   O yüzden modernlik SAYILABİLİR ÖZELLİKLERE çevrildi:
     açık boru kafes → KAPALI DÜZ LEVHA · ölçüsüz → 60 × 78 × 24 cm ·
     8 çıkıntılı meme → 16 GÖMME meme (4 köşe yuvası × 4) · tek renk →
     iki renk · tarifsiz yüzey → 3 panel + 2 dikiş + 1 taşıma rayı.
     Kapı ⑤ bunların SAYILABİLİR olmasını şart koşuyor.
     ⭐ "Günümüzde olan" da bir sıfattı ve o da geometriye çevrildi:
        modern donanımın okunan işareti KARE KENAR + DÜZ YÜZEY +
        GÖMME DONANIM'dır. Prompt bu üçünü ayrı ayrı söylüyor.

⭐ YAN KAZANÇ — KLON KAPISI GÜÇLENDİ
   Paket omuz hattından taştığı için A ile B artık SİLUETTE ayrışıyor.
   Kapı ③'ün yabancı göz testi bu yüzden değişti: panel siyah siluete
   çevrilip soruluyor. Eski (önkol derinliğinde) pakette bu test
   anlamsızdı. Uzak kadrajlarda (S11 · S45) iki figür yüz ve renk
   görünmeden ayrılabilir hâle geldi.

⛔ AÇIK ÇELİŞKİ — BU REVİZYON SAHNE PROMPTLARINA İNMEDİ
   Proje sahibi "sadece referans RC güncelle" dedi; bu dosya öyle
   güncellendi. Ama "thruster frame" tarifi sahne promptlarında da
   kelimesi kelimesine duruyor (kural ③ gereği self-contained):
       FAZ_01_GOREV  19 · FAZ_02_DALGA   2
       FAZ_03_HALAT  25 · FAZ_04_FEDA   10   → 56 geçiş
       README                              2   → toplam 58
   ⚠️ ŞU AN REFERANS SAYFASI İLE PROMPTLAR AYNI ŞEYİ SÖYLEMİYOR.
      B, S45'ten sonra ekranda yok — yani aparat yalnız F1-F4'te
      görünüyor; propagasyonun kapsamı da o dört faz.
      KARAR PROJE SAHİBİNİN: ya 58 geçiş yeni tarifle değiştirilir,
      ya bu sayfa ÜRETİM ÇAPASI sayılır ve promptların eski cümlesi
      bilinçli olarak yok sayılır. İkincisi seçilirse burada gerekçe
      olarak yazılmalıdır [D74] — çünkü Flow'a hem sayfa hem prompt
      girer ve ikisi çelişirse model hangisini dinleyeceğini seçer.
```

```
A single photorealistic 16:9 character reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. The backdrop in every panel is a plain flat dark-grey studio
wall with no horizon and no props; the lighting in every panel is one
hard white key from the upper screen-right and a soft cool blue-white
fill from below screen-left, shadows crisp. Panels 1, 2 and 4 hold
exactly one human figure (human count 1); panel 3 holds exactly two
(human count 2).

THE MAN (panels 1-4): A 52-year-old man mission commander, 1.85
metres tall, broad and heavy: wide bony face, thick dark brows, deep
lines at the eye corners, olive-brown skin with visible pores, short
greying stubble, short dense salt-and-pepper hair, dark brown eyes, a
small old notch in his RIGHT earlobe. Warm off-white pressure suit
with NAVY reinforcement stripes on shoulders, knees and glove cuffs,
a soft chest panel with three small coloured lights and no numerals,
and a LARGE RECTANGULAR BACK UNIT: one flat matte-white slab, 60
centimetres wide, 78 centimetres tall and 24 centimetres deep, with
square vertical sides, a flat back face and hard straight edges whose
corners are only slightly radiused, like a modern hard equipment case.
From behind it reads as ONE CLEAN RECTANGLE, taller than it is wide.
Its flat face is divided into three stacked rectangular panels by two
thin straight recessed dark-charcoal seams that run right across it,
and a shallow recessed grab rail is let into the top edge. At each of
the four corners, FLUSH with the surface and set into a shallow square
recess, sits a cluster of four small nozzles — sixteen nozzles in
total, none of them protruding. Two straight rectangular-section
control arms fold forward from the lower corners and end level with his
hips in flat dark-charcoal grips. The slab stands five centimetres
proud of each shoulder. Nothing on this unit is curved, tubular or
organic: no exposed frame, no visible tanks, no hoses, no struts, no
pods on arms, no wings, no fins. Matte white surface, dark-charcoal
seams, recesses and grips — two colours only. His helmet is a
rigid white shell with a flat rectangular front glass measuring 24 by 16
centimetres, held in a visible bright metal frame the width of a finger;
the glass is optically clear, zero tint, no mirror coating, and his face
is fully readable through it.
THE WOMAN (panel 3 only): A 38-year-old woman flight engineer, 1.70
metres tall, slim and upright: oval face, soft defined jawline, light
wheat-toned skin with visible pores, thin straight nose, dark hazel
eyes, a short vertical pale scar on her LEFT temple near the
hairline, dark chestnut jaw-length hair tucked behind both ears. Warm
off-white pressure suit with ORANGE reinforcement stripes on
shoulders, knees and glove cuffs, a soft chest panel with three small
coloured lights and no numerals, a six-segment amber oxygen ring on
her LEFT wrist, a steel mechanical watch on a black strap over her
RIGHT glove cuff, its hands stopped. Her back silhouette is flat — no
pack, tank, hose or cable, and her shoulder line is clean. Her helmet
is a rigid white shell with a flat rectangular front glass measuring 24
by 16 centimetres, held in a visible bright metal frame the width of a
finger; the glass is optically clear, zero tint, no mirror coating, and
her face is fully readable through it.

PANEL 1 (top-left): the man, full body, three-quarter front,
weightless neutral pose, both gloves closed on the two straight
control-arm grips, expression calm; helmet to boots in frame, true
1.85-metre proportions. Seen from this angle the rectangular slab
shows one flat side face and one hard square vertical edge, and it
stands clearly proud of his shoulder line on both sides.
PANEL 2 (top-right): ⭐ THE APPARATUS PANEL — the man, full body seen
directly from behind, the rectangular back unit filling his back and
reading as the subject of the panel. It must read as ONE CLEAN
RECTANGLE with four square corners, taller than it is wide, like a
modern hard case. Countable: THREE stacked rectangular panels
separated by TWO straight recessed dark-charcoal seams running fully
across; ONE shallow recessed grab rail along the top edge; FOUR
shallow square nozzle recesses, one at each corner, FLUSH with the
surface and not protruding; FOUR small nozzles inside each recess,
sixteen in total. The slab is 60 cm wide and visibly wider than his
shoulders. The two straight rectangular control arms fold forward past
his hips and end in flat dark grips. NAVY shoulder stripes. No other
equipment on him: no hoses, no cables, no antenna, no tanks, no struts.
PANEL 3 (bottom-left): ⭐ the man and the woman standing side by side,
full body, both three-quarter front, same neutral pose, the woman on
the screen-left, the man on the screen-right: the height difference
of 15 cm reads at the helmet tops; her stripes ORANGE, his NAVY; her
back and shoulder line are completely clean and rounded, while his
rectangular slab stands proud of his shoulders on both sides and shows
two hard square vertical edges past his silhouette — one soft outline
against one boxy outline, tellable apart at a glance with no face and
no colour. The two suits never swap colours; only the man carries a
back unit.
PANEL 4 (bottom-right): close-up of the man's helmet and face,
three-quarter front, eyes open, mouth closed: clear visor with one
thin highlight line; the notch in the RIGHT earlobe, the greying
stubble and the deep lines at the eye corners all readable.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — no markings, no logo, no serial and
no warning label anywhere on the back unit. Identical faces across
panels; stripes never swap; the unit never appears on the woman and her
shoulder line stays clean. The unit carries NO lights, NO screens, NO
indicator lamps and NO exhaust of any kind — it is inert hardware in
these panels. Its outline is strictly rectangular: NOT an open tubular
cage, NOT a rounded shell, NOT a jetpack with visible flame, NOT a
winged or finned rig, NOT a soft fabric backpack, NOT twin cylinders,
and nothing protrudes from it on an arm or a strut. Visors never
tinted, mirrored or opaque. 0% bloom, no glow filter, no lens flare,
no waxy skin. Photorealistic, 35mm film grain.
```

---

## 📸 IMAGE PROMPT — SAYFA RD · PLATFORM + MEKİK (sağlam ↔ HASARLI)

> Seed: `________` · tarih: `__.__.____` · durum: ☐
> ⛔ p1 ↔ p2 tek fark HASAR olmalı (kol kopuk · panel bükük · mekik delik ·
> kargo kapağı kopuk). Kadraj, ışık, Dünya, mekik yönü AYNI.
> Mekik burnu her panelde EKRAN-SOLA.

```
A single photorealistic 16:9 environment reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. Every panel is in hard vacuum in low Earth orbit: hard white
sun from the upper screen-right, soft blue-white bounce from Earth
below, shadows absolute black with razor edges, no haze. No human
figures anywhere on the sheet — human count 0; the structures and
the planet are the only subjects.

PANEL 1 (top-left) — INTACT: a wide lateral view at eye level with a
thirteen-metre white lattice truss with ORANGE handrails crossing the
panel from left to right; at its screen-left end a four-metre grey
cylindrical instrument body with a hinged access cover standing open
on its side facing the camera, two latch levers on the cover, one
captive bolt head; a slender white support arm joins the cylinder to
the truss. Forty metres beyond the truss to the screen-right, a white
winged shuttle hangs in the black, its nose pointing screen-left, its
cargo bay doors open with their white inner faces catching sun.
Earth's cloud-streaked blue-white curve fills the lower third; black
space with hard pinpoint stars above.
PANEL 2 (top-right) — DAMAGED, the exact same framing, light, Earth
and shuttle position: the white support arm is torn through and the
grey cylinder hangs askew from the truss by one bent strut; one
section of the truss is crumpled; the access cover is bent open at
its hinge. The shuttle, still nose pointing screen-left, carries
three small dark punctures along its flank and one cargo bay door has
sheared off and drifts a few metres from the hull; a handful of small
metal fragments hang nearby, each a straight-line drifter. No fire,
no smoke: cold torn metal.
PANEL 3 (bottom-left): close-up of the intact instrument cylinder's
access panel: grey matte painted cover, micro-scratched, two dull
steel latch levers, one captive bolt head with a raised rim, the seam
where the cover meets the housing, and one ORANGE handrail sleeve
crossing the lower frame.
PANEL 4 (bottom-right): the intact shuttle alone, three-quarter front
from its screen-left side, nose pointing screen-left, cargo bay doors
open, a clean white thermal hull with grey underside tiles, no
markings; Earth's limb low in frame for scale.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — no markings on the shuttle or the
cover. No human figures, no crew. Panels 1 and 2 differ only in the
damage. The shuttle keeps its nose pointing screen-left in every
panel. 0% bloom, no glow filter, no lens flare. Photorealistic, 35mm
film grain.
```

---

## 📸 IMAGE PROMPT — SAYFA RE · İSTASYON DIŞ (sağlam ↔ HASARLI)

> Seed: `________` · tarih: `__.__.____` · durum: ☐ · F3'ten önce
> ⛔ p1 ↔ p2 tek fark: sol panel kanadı parçalanmış + bir modül delinmiş.
> p3 = airlock kapağı + PARAŞÜT HALAT DEMETİ (S37-44 geometrisi burada donar).

```
A single photorealistic 16:9 environment reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. Every panel is in hard vacuum in low Earth orbit, sun low
and golden from the upper screen-right, soft blue-white bounce from
Earth below, shadows absolute black with razor edges. No human
figures anywhere on the sheet — human count 0.

PANEL 1 (top-left) — INTACT: an orbital station sixty metres from end
to end, three-quarter view from slightly above: four white-grey
cylindrical modules in a row, each 12 metres long and 4.2 metres across,
joined by a central white lattice cage 1.8 metres square in section;
their surfaces quilted thermal blanket in panels the size of a door,
with ORANGE handrail runs set 60 centimetres apart; two dark-blue solar
panel wings 18 metres long and 4 metres wide on a spine above the cage;
at the far screen-right end a white conical capsule 2.4 metres across
the base and 3 metres tall sits docked, its tip outward. Earth's curve with a thin orange terminator edge fills
the lower third; black space above.
PANEL 2 (top-right) — DAMAGED, the exact same framing, light and
Earth: the screen-left solar wing is shredded to a bent spine with a
few torn dark-blue cells; the second module from the left carries a
ragged dark puncture in its side the width of a hand, with a strip of
blanket a forearm long peeled back around it;
a few small fragments hang near the wing, straight-line drifters. All
else identical to panel 1. No fire, no smoke.
PANEL 3 (bottom-left): close-up on the underside of the second module:
a circular airlock hatch of white metal 90 centimetres across with a
long external lever handle the length of a forearm and a recessed ORANGE
grab bar beside it, and, snagged across the hull, a tangled bundle of
white-grey parachute cord as thick as a finger — three cords wound
together and looped around a handrail post, their free ends trailing
into the black. The hatch, the lever, the grab bar and the cord bundle
keep these exact proportions in every scene from S37 to S47.
PANEL 4 (bottom-right): the docked capsule alone, close: a white cone
with a grey underside, four small nozzle openings at its base, a
small round porthole on its screen-left flank, a round hatch with an
external handle on its side, and a folded parachute cover at its
tip; the station's end module and one ORANGE rail behind it.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign — no flags, no markings on the hull.
No human figures. Panels 1 and 2 differ only in the damage. 0% bloom,
no glow filter, no lens flare. Photorealistic, 35mm film grain.
```

---

## 📸 IMAGE PROMPT — SAYFA RF · MÜHENDİS (A), KASKSIZ

> Seed: `________` · tarih: `__.__.____` · durum: ☐ · F4'ten önce (S48+)
> ⛔ RA p4 ↔ RF p3 yan yana: aynı yüz değilse ret. Tek fark yaka halkası
> açık, kask yok, saç serbest, eldivenler kemerde.

```
A single photorealistic 16:9 character reference sheet, maximum
resolution, divided into four equal panels by thin neutral mid-grey
gutters. The same one woman appears in every panel, identical in
every detail; the backdrop in every panel is a plain flat dark-grey
studio wall with no horizon and no props; the lighting in every panel
is soft cool white from above screen-right with a faint amber fill
from screen-left, like a pressurised cabin. Exactly one human figure
per panel, human count 1 in each.

THE SUBJECT (identical in all four panels): A 38-year-old woman
flight engineer, 1.70 metres tall, slim and upright: oval face, soft
defined jawline, light wheat-toned skin with visible pores, thin
straight nose, dark hazel eyes, a short vertical pale scar on her
LEFT temple near the hairline, dark chestnut jaw-length hair, now
loose, its tips lifting weightlessly. She wears the same warm
off-white pressure suit with ORANGE reinforcement stripes on
shoulders, knees and glove cuffs, a soft chest panel with three
small coloured lights and no numerals, a six-segment amber oxygen
ring on her LEFT wrist and a steel mechanical watch on a black strap
over her RIGHT cuff, its hands stopped — but no helmet: the steel
collar ring stands open at her neck, and both gloves hang clipped to
her belt. Her back silhouette is flat — no pack, tank, hose or cable.

PANEL 1 (top-left): full body, three-quarter front, weightless
neutral pose, feet together, bare hands open at her sides, expression
calm and tired; hair lifting slightly.
PANEL 2 (top-right): full body, exact left-side profile facing
screen-left, same pose; the open collar ring and the flat back read
clearly.
PANEL 3 (bottom-left): close-up of the face, three-quarter front,
eyes open, mouth closed: the scar on the LEFT temple, the loose hair
lifting away from the cheek, pore texture and faint fatigue under the
eyes all readable.
PANEL 4 (bottom-right): full body curled in a weightless fetal
position, knees drawn up, arms around the shins, head bowed, hair
lifting, seen from the screen-left side; the suit's collar ring open;
nothing else in the panel.

NEGATIVE: No text, labels, captions, arrows, callouts, dimension
lines, panel titles or watermarks anywhere on the sheet or in the
gutters. No readable text, letters, digits, numbers or symbols on any
display, surface, patch or sign. Exactly one human figure per panel.
Identical face, bone structure and eye spacing in all four panels;
the scar stays on the LEFT temple; stripes stay ORANGE; no helmet
appears in any panel. No back-mounted unit. 0% bloom, no glow filter,
no lens flare, no waxy or smoothed skin. Photorealistic, 35mm film
grain.
```

---

## ⏳ SAYFALAR RG · RH · RI — RG **F4'TEN**, RH F5'TEN, RI F10'DAN ÖNCE

```
RG İSTASYON İÇ    koridor 2 m çap, tutamaklar, soğuk beyaz panel +
                  amber acil ışık · delinmiş panel ve süzülen eşyalar
                  (S53) · hoparlör ızgarası + telsiz düğmesi (S51-55) ·
                  airlock iç yüzü, hortumlar (S48)
RH KAPSÜL İÇ      koni kabin, üç koltuk (iki boş), tavan paneli · 30 cm
                  lomboz (sol) · oksijen vanası + halka · kırmızı
                  menteşeli kapak altında tek kol (Çehov 6) · yakıt
                  halkası BOŞ
RI ZEMİN  ⚠️ F9'DAN ÖNCE (S107)  kuru göl yatağı, çatlak kil, ufka kadar düz · kapsül
                  yan yatmış, paraşüt 20 m ötede · çatlak kil CU (avuç) ·
                  alçak sabah güneşi, uzun yumuşak gölgeler
⚠️ 29.08.2026 TAKVİM DÜZELTMESİ: RG "F5'ten önce" yazıyordu ama S48
(CENİN) Faz 4'ün son sahnesidir ve İÇERİDE geçer. RG'nin en azından
p4'ü (airlock iç yüzü + hortumlar) **F4 ÜRETİMİNDEN ÖNCE** hazır olmalı;
RF (kasksız A) zaten öyleydi. Bu iki sayfa onaysızken S48 üretilmez.
Bu üç sayfa ilgili fazlar yazılırken, o fazların ÜRETİMİNDEN ÖNCE eklenir.
Bu dosya o zamana kadar "Perde I + F4 promptları tam" sayılır.
```

---

# 4. 🎭 GOOGLE FLOW KARAKTER KARTLARI

> Flow'un "Karakter oluştur" ekranı üç alan ister: **ad**, **Karakter
> Bilgileri**, **gövde imajı** (dikey). Ad alanına gerçek ad YAZILMAZ
> [D34/45] — rol etiketi: `MUHENDIS` / `KOMUTAN`. Ses alanı önemsiz
> (sahneler sessiz üretilir, ses post'ta). Karakter Bilgileri İngilizce.

### 🎭 FLOW KARTI 1 — MÜHENDİS (A)

**Ad alanı:** `MUHENDIS`

**Karakter Bilgileri:**

```
A 38-year-old woman flight engineer on her first orbital mission.
Procedural and quiet; she never panics. When she is afraid she does
not speed up — she counts: her fingers tap a slow rhythm on her thigh
or the armrest while her lips stay closed. Her movements are measured;
in hesitation her hands SLOW DOWN. Her habitual gesture before a
decision: her right hand goes to the amber ring on her left wrist.
She speaks briefly and only over the helmet radio; with the helmet
off she does not speak at all. VISUAL CONTINUITY (never changes):
oval face, soft defined jawline, light wheat-toned skin with visible
pores, thin straight nose, dark hazel eyes, a short vertical pale
scar on her LEFT temple near the hairline, dark chestnut jaw-length
hair tucked behind both ears (loose and weightless when the helmet is
off), 1.70 m tall, slim and upright. She always wears a warm
off-white pressure suit with ORANGE reinforcement stripes on
shoulders, knees and glove cuffs, a soft chest panel with three small
coloured lights and no numerals, a six-segment amber oxygen ring on
her LEFT wrist, and a steel mechanical watch with stopped hands on a
black strap over her RIGHT cuff. Her back is flat — no pack, tank,
hose or cable. Her helmet visor is optically clear glass with zero
tint; her face is always readable through it.
```

**Gövde imaj promptu (dikey):**

```
Vertical full-body photorealistic reference of a 38-year-old woman
flight engineer floating upright in a weightless neutral pose, feet
together, arms held slightly away from her body, gloves open and
empty, expression calm and neutral. Oval face, soft defined jawline,
light wheat-toned skin with visible pores, thin straight nose, dark
hazel eyes, a short vertical pale scar on her LEFT temple near the
hairline, dark chestnut jaw-length hair tucked behind both ears. She
is 1.70 m tall, slim and upright. Warm off-white pressure suit with
ORANGE reinforcement stripes on shoulders, knees and glove cuffs, a
soft chest panel with three small coloured lights and no numerals, a
six-segment amber oxygen ring on her LEFT wrist, a steel mechanical
watch on a black strap over her RIGHT glove cuff, its hands stopped.
Her back silhouette is flat — no pack, tank, hose or cable. Her
spherical helmet visor is optically clear glass, zero tint, no mirror
coating; her face is fully readable through it. Background: a plain
flat dark-grey studio wall, nothing else in frame. One hard white key
from the upper screen-right, soft cool blue-white fill from below
screen-left, crisp shadows; every surface keeps its texture. Full
body from helmet to boots in frame. Exactly one human figure. No
readable text, letters or digits anywhere. 0% bloom, no glow filter,
no waxy skin, no airbrushing, no face morphing. Photorealistic, 35mm
film grain.
```

### 🎭 FLOW KARTI 2 — KOMUTAN (B)

**Ad alanı:** `KOMUTAN`

**Karakter Bilgileri:**

```
A 52-year-old man mission commander on his last flight. He carries
routine with dry humour and carries the worst moment with the same
calm. He moves economically and never gestures while speaking. When
he is afraid he SLOWS DOWN and his voice drops — the opposite of the
engineer. He flies a back-mounted thruster frame with short, precise
puffs and never wastes propellant. VISUAL CONTINUITY (never changes):
wide bony face, thick dark brows, deep lines at the eye corners,
olive-brown skin with visible pores, short greying stubble, short
dense salt-and-pepper hair, dark brown eyes, a small old notch in his
RIGHT earlobe, 1.85 m tall, broad and heavy. He always wears a warm
off-white pressure suit with NAVY reinforcement stripes on shoulders,
knees and glove cuffs, a soft chest panel with three small coloured
lights and no numerals, and a LARGE RECTANGULAR BACK UNIT: one flat
matte-white slab 60 cm wide, 78 cm tall and 24 cm deep with square
sides and hard straight edges, reading as one clean rectangle taller
than it is wide, its face split into three stacked panels by two
straight recessed dark-charcoal seams, a recessed grab rail along the
top edge, four flush square nozzle recesses at the corners with four
small nozzles in each — sixteen in total, nothing protruding — and two
straight rectangular control arms folding forward to his hips. His
helmet is a rigid white shell with a flat rectangular front glass 24
by 16 centimetres in a visible bright metal frame; the glass is
optically clear with zero tint and his face is always readable through
it. He is 15 cm taller than the engineer; his stripes are navy, hers
orange; only he carries a back unit, and it stands five centimetres
proud of each shoulder so the two of them differ in SILHOUETTE — her
outline soft and rounded, his boxy and square — not only in colour.
```

**Gövde imaj promptu (dikey):**

```
Vertical full-body photorealistic reference of a 52-year-old man
mission commander floating upright in a weightless neutral pose, both
gloves closed on the two forward control-arm grips of his manoeuvring
pack, expression calm. Wide bony face, thick dark brows, deep lines at the
eye corners, olive-brown skin with visible pores, short greying
stubble, short dense salt-and-pepper hair, dark brown eyes, a small
old notch in his RIGHT earlobe. He is 1.85 m tall, broad and heavy.
Warm off-white pressure suit with NAVY reinforcement stripes on
shoulders, knees and glove cuffs, a soft chest panel with three small
coloured lights and no numerals, and a LARGE RECTANGULAR BACK UNIT: one
flat matte-white slab 60 centimetres wide, 78 centimetres tall and 24
centimetres deep, with square vertical sides, a flat back face and hard
straight edges whose corners are only slightly radiused, like a modern
hard equipment case. It reads as ONE CLEAN RECTANGLE, taller than it is
wide, standing five centimetres proud of each shoulder. Its face is
divided into three stacked rectangular panels by two thin straight
recessed dark-charcoal seams running fully across, with a shallow
recessed grab rail let into the top edge. At each of the four corners,
FLUSH with the surface in a shallow square recess, sits a cluster of
four small nozzles — sixteen in total, none of them protruding. Two
straight rectangular-section control arms fold forward from the lower
corners and end level with his hips in flat dark-charcoal grips. From
this three-quarter angle one flat side face and one hard square
vertical edge of the slab are visible past his silhouette. Nothing on
the unit is curved, tubular or organic: no exposed frame, no visible
tanks, no hoses, no struts, no pods on arms, no wings, no fins. Matte
white surface, dark-charcoal seams, recesses and grips — two colours
only. His helmet is a rigid white shell
with a flat rectangular front glass measuring 24 by 16 centimetres,
held in a visible bright metal frame the width of a finger; the glass
is optically clear, zero tint, no mirror coating; his face is fully
readable through it. Background: a plain flat dark-grey
studio wall, nothing else in frame. One hard white key from the upper
screen-right, soft cool blue-white fill from below screen-left, crisp
shadows; every surface keeps its texture. Full body from helmet to
boots in frame. Exactly one human figure. No readable text, letters
or digits anywhere — no markings, no logo, no serial and no warning
label on the back unit. It carries no lights, no screens and no
exhaust. Its outline is strictly rectangular: NOT an open tubular cage,
NOT a rounded shell, NOT a jetpack with visible flame, NOT a winged or
finned rig, NOT a soft fabric backpack, NOT twin cylinders, and nothing
protrudes from it on an arm or a strut. No dome visor, no seamless
bubble. 0% bloom, no glow filter, no waxy skin, no airbrushing, no face
morphing. Photorealistic, 35mm film grain.
```

### 🛰️ Platform · mekik · istasyon — Flow'da karakter DEĞİL

```
Yapılar Flow'un karakter sistemine EKLENMEZ (siluet kayması daveti).
RD / RE sayfaları normal imaj olarak üretilir; sahne üretirken
"malzeme/ingredient" olarak yüklenir. Hasarlı durumlar için AYRI üretim
YOK — aynı sayfanın p2 paneli o durumdur.
```

---

# 5. ✅ KABUL / RET KAPILARI — sayısal, yabancı gözle uygulanabilir

> ⚠️ **30.08.2026 [D144]:** eski sürüm "okunuyor mu / temiz mi" diyordu —
> bunlar ölçülemez. D144: *"her kapı KABUL · RET · YABANCI GÖZ · SONUÇ
> satırı taşır."* Aşağıdaki her kapı bir SAYI ya da bir İKİLİ TEST
> içerir ve dosyayı hiç okumamış biri tarafından uygulanabilir.

```
① 120 PX TESTİ  (bütün sayfalar)
   KABUL: panel 120 piksel yüksekliğe indirildiğinde şu beş öğe hâlâ
          ayırt ediliyor — yara izi (RA p4 · RF p3) · halka segment
          SAYISI (RB p2) · cıvata başı (RD p3) · airlock kolu (RE p3) ·
          vizör camının dikdörtgen çerçevesi (RA p4 · RC p4).
   RET:   beşten biri bile 120 px'te lekeye dönüşüyor.
   YABANCI GÖZ: küçültülmüş paneli birine göster, "burada kaç ışık
          var?" diye sor. Yanlış sayarsa RET.
   SONUÇ: sayfa atılır; o varlık TEK GÖRSEL olarak yeniden üretilir.

② OLUK VE METİN  (bütün sayfalar)
   KABUL: oluklarda, panel köşelerinde ve her yüzeyde harf/rakam/ok/
          ölçü çizgisi SAYISI = 0.
   RET:   ≥1.  SONUÇ: sayfa ATILIR, düzeltilmez.

③ KLON KAPISI  (RC p3 — iki figür yan yana)
   KABUL: boy farkı 15 cm ± 3 cm okunuyor · şerit renkleri turuncu ve
          lacivert, karışma yok · sırt/omuz siluetleri farklı: kadının
          omuz hattı temiz, adamınki paketle iki yandan 6'şar cm taşıyor.
   RET:   üç ölçütten biri bile sağlanmıyor.
   YABANCI GÖZ: paneli SİYAH SİLUETE çevir (rengi tamamen at) ve birine
          göster: "hangisi daha uzun, hangisinin sırtında bir şey var?"
          İkisini de doğru bilmeli. ⭐ 31.08 revizyonuyla bu test artık
          anlamlı — paket büyütülmeden önce siluette ayrım zayıftı.
   SONUÇ: RC yeniden üretilir; F1 ÜRETİLMEZ.

④ DURUM ÇİFTİ  (RD p1↔p2 · RE p1↔p2)
   KABUL: iki panelde modülün/platformun genişliği aynı piksel sayısı
          (±%3) · güneş aynı yönden · Dünya aynı yerde.
   RET:   kadraj, ışık ya da mesafe kaymış.
   SONUÇ: çift yeniden üretilir; dalga sahneleri (S16-S22) ÜRETİLMEZ.

⑤ D79 SIRT VE VİZÖR
   KABUL: RA p3'te sırt hattı boyunca çıkıntı sayısı = 0, ama yüzey
          BOŞ DEĞİL: dikey sırt dikişi ve bel kayışı görünüyor ·
          ⭐ RC p2'de SIRT ÜNİTESİ VAR, DİKDÖRTGEN ve SAYILABİLİR:
          arkadan tek temiz dikdörtgen (eninden yüksek, dört kare köşe) ·
          3 yatay panel · 2 düz gömme dikiş · 1 üst taşıma rayı ·
          4 köşede yüzeyle aynı hizada kare yuva · yuva başına 4 meme
          (toplam 16, hiçbiri çıkıntılı değil) ·
          levha omuz hattından iki yandan taşıyor · her vizörde
          dikdörtgen ön cam ve çevresindeki metal çerçeve ayırt
          ediliyor (24×16 oranı).
   RET:   sırtta herhangi bir kabartı (kadında) · ya da sırt düz ama
          TAMAMEN özelliksiz (D139: yokluk kilidi görünen yüzeyde
          çalışmaz) · ya da vizör kenarsız bir kubbe ·
          ⭐ ya da ünite AÇIK BORU KAFES çıktıysa (ilk tasarım) · ya da
          KAVİSLİ/YUVARLAK bir kabuk çıktıysa (reddedilen ara tur) ·
          ya da kollarda/ayaklarda duran çıkıntılı pod'lar varsa ·
          ya da üstünde ışık/ekran/alev varsa · ya da üç panel ile
          on altı meme sayılamıyorsa.
   ⭐ TEK CÜMLELİK SINAV: paneli birine göster, "bu ne?" diye sor.
      "Sırtında bir kutu" ya da "bir ekipman çantası" demeli.
      "Roket sırt çantası" ya da "jetpack" derse RET — biçim bu filmin
      diline değil, çizgi filme kaymış demektir.
   SONUÇ: sayfa yeniden üretilir.

⑥ YÜZ EŞİTLİĞİ  (RA p4 ↔ RF p3 ↔ Flow kartı 1)
   KABUL: üçü yan yana konduğunda göz aralığı, burun hattı ve çene
          açısı aynı; tek fark kask.
   RET:   üçünden biri farklı kişi okunuyor.
   YABANCI GÖZ: üç görseli karıştırıp birine göster, "kaç kişi var?"
          diye sor. Cevap 1 değilse RET.
   SONUÇ: en iyi olan MASTER ilan edilir, diğer ikisi ondan yeniden
          üretilir. ⛔ Bu kapı düşerken F4-F10 ÜRETİLMEZ.

⑦ RH PANEL BİRLİKTELİĞİ  (F7 KİLİT 34'ün şartı)
   KABUL: vana çarkı ile kırmızı menteşeli kapak AYNI panel görüntüsünde,
          aralarındaki mesafe bir önkol (≈40 cm) olarak okunuyor.
   RET:   ikisi ayrı panellerde ya da mesafe okunamıyor.
   SONUÇ: RH yeniden üretilir; S84 (perde dönüşü 2) ÜRETİLMEZ.

□ Yedi kapı da geçtikten SONRA seed yazılır → faz dosyalarının
  📎 REFERANS satırları o seed'lere bağlanır → üretim S5 ile başlar
  (el inserti, düşük risk).
```
