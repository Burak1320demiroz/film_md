# 🟠 THE UPHILL DARK — Yokuş Yukarı Karanlık | PART A

## AI Production Bible — Self-Contained Prompts
### PART A: Sahne 0-12 (13 sahne) | 16:9 Yatay | 0:00 – 2:09
### _"Gemiyi yavaşlatamazsın. Yalnız kendini hafifletebilirsin."_

---

## ⚠️ PART A ÜRETİM NOTLARI (promptlardan önce oku)

```
① REFERANS PAKETİ ÖNCE ÜRETİLİR.
   THE_UPHILL_DARK_REFERANS_PAKETI.md · 5 sayfa × 4 panel · §4 kapısı geçilmeden
   tek sahne üretilmez. Cold Burn'ün ölçümü: 60 promptta kelimesi
   kelimesine aynı metin, aracın yeniden tasarlanmasını engellemedi.

② ÜRETİM SIRASI KAPI KAPI:
   S19 (yük atma) → S21 (temas) → S4 (alev) → S1 (kabin, iki insan)
   Dördü temiz çıkmadan kalan 21 sahne üretilmez.

③ DURUM BLOKLARI [D84 ②] — aynı oturumda üretilecek gruplar:
   blok 1: S0-S3 (6 kartuş dolu · yük dolu)
   blok 2: S4-S7 (5 kartuş)
   blok 3: S8-S12 (3 → 2 kartuş)
   Sahneler arası durum metinle tutulmuyor; OTURUMLA tutuluyor.

④ HER PROMPT TEK BAŞINA ÇALIŞIR. Bible'lara atıf yapılmaz, kod bloğunun
   dışına çıkma. Sadece istediğin sahnenin 📸 veya 🎥 bloğunu kopyala.

⑤ BU FİLMDE SIFIR YERÇEKİMİ YOKTUR. Her karede 0.220 g itki ivmesi var:
   aşağısı geminin kıçı, yukarısı pruvası. Süzülen tek bir nesne yok.

⑥ REPLİK YOK. 25 sahnenin 25'i sessizdir; hiçbir promptta konuşma,
   telsiz, anlatıcı ya da yazı yoktur.
```

### ⚠️ UZUNLUK BANDI — BİLİNÇLİ SAPMA + İLK RED PROTOKOLÜ

```
prompt_kontrol.py sonucu (17.08.2026, turkuaz kaplama turu sonrası):
⛔ 0 BLOCK · ⚠️ FIX (yalnız uzunluk)
  PART_A: image 2.029-2.577 · video 2.590-3.299
  PART_B: image 1.929-2.526 · video 2.528-3.909 (en uzun: S19)
  tavan 4.300 — 50/50 prompt altında

GEREKÇE: video promptları hedef bandın (2.000-2.600) üstünde. Sebep tek
kalem: her prompt üç zorunlu bloğu birlikte taşıyor — D79/D95 kask imzası
(sırt düz + üç görünür vizör işareti), D91 iz formülü (organ + ölçü +
"gerisi temiz") ve bu filmin fizik kilidi (0.220 g itki çerçevesi, düşen
cismin sayısı). Üçünü kısaltmak, ölçülmüş biçimde tutan kilitleri silmek
demektir. Bir tur kısaltma yapıldı (en uzun 7 prompt, −400/−1.400 karakter);
kalan fazlalık taşıyıcı kilitlerdir.

⛔ İLK RED GELİRSE — bu sırayla, prompt yeniden yazılmadan önce:
 1. Hata mesajını sınıflandır (KILAVUZ_REHBERI §7):
      "I can't generate that video"      → POLİTİKA
      "something went wrong" / "error"   → TEKNİK, önce tekrar dene
      "having a hard time fulfilling"    → YAPISAL, tekrar denemek boşuna
 2. YAPISAL ise: NEGATIVE bloğunu tek satır pozitif `Style:` cümlesine
    indir → SCENE/TIMELINE/AUDIO etiketlerini kaldırıp düz paragraf yap.
 3. ⛔ AYNI FİLMDE ÜÇÜNCÜ RED VE SIFIR BAŞARI varsa: kısaltmayı BIRAK,
    3 satırlık mini prompt probunu çalıştır (THE_THIRD_DUNE_PART_A.md ·
    BÖLÜM 2 teşhis kutusu). Third Dune 5 red / 0 başarı, Ring Light
    3 red / 0 başarı — ikisinde de sorun promptta değildi.
 4. Son çare I2V: image promptunu üret, onayla, video promptunu yalnız
    HAREKET cümlelerine indir.
```

---

# 📖 BÖLÜM 1 — THE BIBLES

## 🌌 WORLD BIBLE — YANMANIN ALTINCI SAATİ

```
NEREDE      Bir yıldız sisteminin dış kenarı, açık uzay. Yıldız 40° yanda,
            küçük ve sert: mavi-beyaz, paralel ışık, mutlak siyah gölge.
NE          210 metrelik yıldızlararası bir gemi ayrılış yanmasını yapıyor:
            0.220 g (2.158 m/s²), sabit, kesilemez. Yanma penceresi yörünge
            mekaniğiyle sabittir; füzyon motoru bir kez sönerse yeniden
            ateşleme için gereken kütle gemide yoktur.
KİM         Geminin 40 metre yanında, gövdesinin 118 metre aşağısında,
            iki kişilik 5.2 metrelik bir feribot kapsülü. Geç kaldılar.

ORTAM       VAKUM + İTKİ YERÇEKİMİ (yeni alt-ortam)
  ses         dışarıda yok; içeride yalnız gövdeden iletilen
  gölge       mutlak siyah, jilet keskinliğinde kenar
  dolgu ışığı YOK — tek istisna alev, çünkü alev gerçek bir yayıcıdır
  toz         dışarıda 0 (kaldıracak hava yok); kabinde grit tabanda durur
  egzoz       düz keskin koni, 400 m, seyrelerek biter; kıvrılmaz
  ⭐ süzülme  YOK. Serbest her cisim kıça doğru 2.16 m/s² ile düşer:
              1 saniyede 1.08 m, 3 saniyede 9.7 m, 10 saniyede 108 m.

SICAKLIK    gölgede -180°C; güneş gören yüzeyler +90°C
ZAMAN       film 249 saniyedir ve gemi bu 249 saniyede hiçbir şeyini
            değiştirmez: alev aynı boyda, ışıklar aynı, hiçbir hareket yok.
```

---

## ⚓ ÇAPA BLOKLARI — KANONİK İNGİLİZCE TANIMLAR

> ⛔ Aşağıdaki bloklar promptlara **birebir** kopyalanır. Bir kelime
> değişirse varlık değişir [SAHNE_DEVAMLILIK §2.1].

```
ÇAPA A — THE CROSSING SHIP (uzak/tam gövde)
the crossing ship — a 210-metre interstellar vessel under constant burn,
its bow at the TOP of frame and its stern at the bottom: a sleek 26-metre ceramic-white ice shield with a turquoise rim stripe at the bow, three habitat drums wrapped in clean white multi-layer insulation quilting, each ringed by a thin turquoise band,
four polished bright-metal 9-metre propellant spheres, a 12-metre lattice berth
boom standing out from its port flank, a long open graphite truss spine,
two dead-black knife-edge radiator wings, a 30-metre satin pearl-grey conical shadow shield and an armoured drive block with three recessed nozzles

ÇAPA B — THE PLUME
three pale blue-white exhaust cones merge into one straight, sharply
defined 400-metre lance that leaves the BOTTOM of frame and thins away —
it never billows, never curls, never mushrooms, never bends

ÇAPA C — THE FERRY CAPSULE
the ferry capsule — a 5.2-metre truncated cone standing nose-UP, 3.6
metres across its flat base, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows; a 60-centimetre docking probe
with three alignment vanes on its nose; one wide curved window 1.6 metres
across in the upper cone; four scorched main nozzles in the base ring; a
six-socket cartridge rack low on its port flank; and the cargo cradle
bolted to the upper cone on its starboard side

ÇAPA D — THE CARGO (dolu · S0-S19)
the cargo cradle — a machined rack of FORTY identical sealed white core
tubes in five rows of eight, held down by ONE wide BURNT-ORANGE strap
drawn tight through a machined buckle

ÇAPA D2 — THE CARGO (boş · S19 sonrası)
the cargo cradle — FORTY empty moulded sockets, its clamp bar swung open
and its single BURNT-ORANGE strap hanging slack down the flank

ÇAPA E1 — THE PILOT
the pilot — a lean 54-year-old man, 1.75 metres, weathered pale olive skin
with visible pore texture, a THICK GREY MOUSTACHE over his upper lip and no
beard, close-cropped grey hair receding at the temples, and a 2-centimetre
shiny burn scar on the BONE OF HIS RIGHT CHEEK below the outer corner of
his right eye; the rest of his face is completely unmarked

ÇAPA E2 — THE ENGINEER
the engineer — a compact 33-year-old woman, 1.58 metres, very dark brown
skin with visible pore texture, her head COMPLETELY SHAVED to 2 millimetres
of stubble, a broad flat nose, and a pale 4-centimetre surgical line along
the BONE OF HER RIGHT JAW from below the ear to the chin; the rest of her
face is completely unmarked

ÇAPA F — THE SUITS (ikisi de)
matte BURNT-ORANGE hard-shell pressure suits — deep saturated
oxidised-iron orange, segmented chest and shoulder plates with crisp
recessed seams, dark graphite flex-weave at every joint, machined aluminium
rings at shoulders, elbows and wrists, finely scuffed and dulled at the
elbows; his shoulder bands CHARCOAL GREY, hers BONE WHITE, and a
12-centimetre machined tool block on HER LEFT FOREARM only. Both backs are
FLAT — no backpack, no tank, no hose, no cable, no rear housing. Both
helmets are sealed: a single curved optically clear pane in a 2-centimetre
brushed-metal frame, the frame's lower seal ring visible at the collar, one
thin unbroken specular line along the pane's upper edge, and both faces
fully readable through the glass

ÇAPA G — THE BERTH
the berth — a 12-metre lattice boom standing out from the ship's port
flank, carrying on its UNDERSIDE a 2.0-metre machined capture ring with a
40-centimetre conical throat and THREE curved capture arms standing open at
120-degree spacing, ringed by a continuous recessed warm-white light
channel

ÇAPA H — THE CABIN
the cabin — a cramped 2.4-metre-wide cone interior with TWO deep-bucketed
seats side by side, the pilot's at LEFT and the engineer's at RIGHT, both
reclined so the crew face UP toward the window; one wide curved window
above the console; a matte dark console with slim turquoise accent trim, abstract amber and grey light segments, no digits and no screens; a machined six-detent selector at
the left cheek; a BURNT-ORANGE two-handed lever at the right cheek; and a
40-centimetre brass lanyard hanging from the window frame, hanging dead
straight DOWNWARD under tension
```

---

## 🚀 SHIP BIBLE — GEÇİT (ana gemi) & İĞNE (kapsül)

```
GEÇİT — 210 m, pruvadan kıça:
   0-24 m    buz kalkanı, 26 m mat seramik beyazı disk, turkuaz çember şerit
  24-60 m    üç yaşam tamburu, 18 m çapında, temiz beyaz kapitone yalıtım + turkuaz bant
  60-92 m    dört yakıt küresi, her biri 9 m, cilalı parlak metal + turkuaz kızak, kırağı izli
     100 m   YANAŞMA KOLU — port bordadan 12 m dışarı; yuva ALT yüzde
 104-150 m   kafes omurga, altıgen, grafit gri
 150-166 m   iki radyatör kanadı, siyah bıçak ağzı, her biri 40 m
 166-182 m   gölge kalkanı, 30 m koni, kıça bakar
 182-210 m   motor bloğu, üç gömülü lüle · alev 400 m
  ⛔ SAYI KİLİDİ: 3 tambur · 4 küre · 2 kanat · 3 lüle · 3 yakalama kolu
  ⛔ Gemi dönmez, halkası yoktur, kanadı (radyatör dışında) yoktur.

İĞNE — 5.2 m kesik koni, taban 3.6 m, burun yukarı · mat seramik beyazı, grafit iskelet, turkuaz chevron şerit:
  burun      60 cm prob + 3 hizalama kanadı
  pencere    1.6 m × 0.6 m kavisli tek cam, işlenmiş çerçeve
  taban      4 ana lüle (0.4 m boğaz) — SABİT İTKİ, kısılamaz
  port borda 6 yuvalı kartuş rafı (boşalan yuva görünür kalır)
  starboard  yük kızağı, üst koni, pencereden alt sağ köşede görünür
  ⛔ SAYI KİLİDİ: 4 lüle · 6 yuva · 40 karot · 1 prob · 1 turuncu kayış
  ⛔ Bacak yok, tekerlek yok, kanat yok, paraşüt yok.

ÖLÇEK KİLİDİ [D32]: kapsül geminin 1/40'ıdır. Kapsül, tek bir yakıt
küresinin çapından kısadır; tek bir radyatör kanadı kapsülün 8 katıdır.
```

---

## 👤 CHARACTER BIBLE — PİLOT & MÜHENDİS

```
⛔ İSİM HİÇBİR PROMPTTA GEÇMEZ [D34]: "the pilot" · "the engineer".

PİLOT     54, erkek, 1.75 m, ince ve sinirli. Solgun zeytin ten, derin
          çizgiler. KALIN GRİ BIYIK, sakal yok. Dipten kesilmiş gri saç,
          şakaklar geri çekilmiş. İZ: sağ ELMACIK KEMİĞİNDE 2 cm parlak
          yanık; yüzün geri kalanı tamamen işaretsiz [D91].
          KOLTUK: SOL, 25/25 sahne. Ön kolları BOŞ.
MÜHENDİS  33, kadın, 1.58 m, kompakt ve kare omuzlu. Çok koyu kahverengi
          ten. Baş TAMAMEN TIRAŞLI (2 mm dip). Geniş yassı burun.
          İZ: sağ ÇENE KEMİĞİ HATTINDA 4 cm soluk cerrahi çizgi; yüzün
          geri kalanı tamamen işaretsiz [D91].
          KOLTUK: SAĞ, 25/25 sahne. SOL ön kolda 12 cm alet bloğu.

AYRIŞMA DÖRT KANALDAN: boy (17 cm) · baş (bıyıklı gri ↔ tıraşlı) ·
ten (solgun zeytin ↔ çok koyu) · koltuk (SOL ↔ SAĞ, hiç takas yok [D86]).

HELMET STATE SCHEDULE: mühürlü S0-S24 (25 sahne). Açık: 0. Değişim: 0.
Gerekçe: kabin basınçsız uçuyor.
MÜHÜRÜN ÜÇ GÖRÜNÜR İŞARETİ [D95]: 2 cm metal çerçeve · yaka mühür
halkası · üst kenarda tek parlama çizgisi. Yüz her açıda tam okunur.

İKİSİ DE 25/25 SAHNEDE KEMERLİ VE OTURUYOR. Yürüme, biniş, iniş,
kapıdan geçme: 0 kare [D69 ①].
```

---

## 🎥 CAMERA BIBLE

```
25 sahnenin 25'i SABİT LOCKOFF. Kamera hiç hareket etmez: zoom yok, pan
yok, tilt yok, track yok, sahne içi kesme yok, sahne başına 1 çekim.

LENSLER
  24mm   dış geniş — gemi tam boy, ölçek (S0 · S4 · S7 · S12 · S18 · S24)
  35mm   iç kadrajlar (S1 · S3 · S8 · S11 · S14 · S16 · S19 · S20 · S22)
  50mm   dış orta · iki-baş · temas (S2 · S6 · S9 · S10 · S13 · S15 · S21 · S23)
  85mm   tek yüz / detay (S5 · S17)
  ⛔ Küresel lens. Anamorfik yatay parlama YASAK (vakumda saçılma yok).

KADRAJ DEĞİŞMEZLERİ
  · Gemi ekseni kadrajda DİKEY: pruva üstte, alev alttan çıkar
  · Kapsül gemi gövdesinin SOLUNDA; gövde her dış kadrajda SAĞDA
  · İç kadrajda pilot SOLDA, mühendis SAĞDA — hiç takas yok
  · Yükselen = kazanıyor, düşen = kaybediyor
```

---

## 💡 LIGHTING BIBLE — MAVİ ALTTAN, BEYAZ ÜSTTEN

```
① YILDIZ        mavi-beyaz, 40° yanda, EKRAN SOLUNDAN gelen sert paralel
                ışık. 6500K. Gölge mutlak siyah, kenarı jilet keskin.
                Dolgu YOK.
② ALEV          400 m'lik soluk mavi-beyaz mızrak, ALTTAN. Gerçek bir
                yayıcıdır: gölgelerin ALT kenarını yumuşatır, üst kenarı
                mutlak siyah bırakır. Yaklaştıkça güçlenir, uzaklaştıkça
                sayısal olarak zayıflar (§Işık ekseni, plan dosyası).
③ YUVA IŞIĞI    3400K sıcak beyaz, ince gömük ışık oluğu, ÜSTTEN.
                S12'de ilk kez görünür, S18'den sonra ana kaynak olur.
④ KABİN         kısık kehribar ışık segmentleri, pratik, düşük seviye.

⛔ 0% bloom. Yumuşaklık = doku kaybı değil. Her yüzey gözenek/doku tutar.
⛔ "cinematic lighting" yazılmaz [D33]. Parlama sözlüğü yasak [D29].
```

---

## ⚙️ PHYSICS BIBLE

```
İVME ÇERÇEVESİ
  Her iki gövde de 0.220 g (2.158 m/s²) itki altında. AŞAĞI = geminin
  kıçı = kadrajın altı. YUKARI = pruva = kadrajın üstü.
  Serbest cisim kapsüle göre 2.16 m/s² ile düşer.
  ⛔ Hiçbir karede süzülme, asılı kalma, sıfır-g yok.

KAPSÜLÜN İTKİ MANTIĞI (filmin bütün gerilimi buradan çıkar)
  · Ana motor SABİT İTKİLİDİR, kısılamaz. Yüklü hâlde tam eşleşme:
    9.500 N / 4.400 kg = 2.159 m/s² = 0.220 g.
  · YÜKSELMEK için ek itki gerekir → İTME kartuşu (taban portu),
    4.0 s, +0.40 m/s², net ivme 0.260 g: herkes AĞIRLAŞIR.
  · DURMAK için ters itki gerekir → TUTMA kartuşu (üst port),
    4.0 s, −0.40 m/s², net ivme 0.179 g: herkes HAFİFLER.
  · Toplam 6 kartuş = 3 çift = 3 tırmanış.
  · Motorda TEK KULLANIMLIK bir boşaltma valfi var (tel kilitli):
    itkiyi BOŞ kütlede tam eşleşmeye kırpar (9.50 → 7.55 kN). Yük
    dururken açılırsa 0.175 g çıkar ve kapsül DÜŞER — sıralama
    kilitlidir: önce yük (S19, mühendis), 2 sn sonra valf (S19,
    pilot). Geri kapanmaz.
  · Manevra iticileri (RCS) soğuk gazdır, toplam ~6 m/s: yanal
    kaçınma + dönüş ~4 m/s yer, kalan ~1 m/s SON EKSENEL FREN olarak
    S20'nin sonuna saklanır (1.11 → 0.20 m/s). ⛔ RCS'in ekseni
    yalnız AŞAĞI iter (fren) — kapsülde yukarı öteleme lülesi YOK;
    yukarı itkiyi yalnız ana motor + İTME kartuşları verir. Tırmanış
    Δv'si (9.6 m/s) zaten RCS'e sığmaz — kartuşların varlık sebebi.
  · Yanal öteleme eksene dik olduğundan ivmeyle savaşmaz: UCUZDUR.

PARÇACIK KİLİDİ
  düşen kovan   6 adet, düz yay, dönerek küçülür, asla asılı kalmaz
  düşen karot   40 adet, S19'da TEK KÜTLE hâlinde ayrılır
  alev          düz koni, kıvrılmaz [D36]
  kabin griti   tabanda durur; itki değişiminde bir kez oynar, oturur
  ⛔ Hiçbir parçacık sıvı gibi akmaz, girdap yapmaz [D39].

TEMAS KİLİDİ
  Prob ↔ halka teması KATI CİSİM temasıdır: net yapısal sınır,
  kaynaşma yok, geçme yok [D11 · D17]. Temas hızı 0.20 m/s.
```

---

## 🚫 NEGATIVE BIBLE (çekirdek — sahneye göre kısaltılır)

```
Single unbroken take, fixed locked-off camera — no cuts, no edits, no
camera resets, no transitions, no dissolves, no fades, no jump cuts, no
camera teleportation, no angle change, no pan, no zoom, no tilt. Exactly 2
human figures exist in this film — no third person, no duplicate, no clone,
no reflected figure, no crew anywhere on the big ship. 0% bloom, no glow
filter, no soft focus, no dreamy haze — every surface keeps visible
texture. Photorealistic skin pores, sweat and fatigue retained — no
airbrushing, no plastic or waxy texture, no face morphing, identical bone
structure throughout. Both suit backs are FLAT — no backpack, no tank, no
hose, no cable, no rear housing; both visors are optically clear with zero
tint, zero mirror coating and zero environment reflection, and both faces
stay fully readable through the glass. Equipment identical to the
description — no drift, no gear appearing or disappearing mid-shot. No
readable text, letters, digits, numbers or symbols on any display, surface
or panel. No subtitles, no captions, no title card, no end card, no
credits, no watermark. No holograms, no floating interfaces, no blue user
interface. All contacts keep a clear structural boundary — no merging, no
phasing, rigid-body collision throughout. Every free object falls toward
the bottom of frame under 0.220 g of thrust acceleration — nothing floats,
nothing hovers, nothing drifts in zero gravity, nothing is frozen, nothing
flows like liquid. The exhaust never billows, curls or mushrooms. No
Unreal Engine look, no CGI aesthetic, no video game aesthetic.
Photorealistic with 35mm film grain.
```

---

# 🎬 BÖLÜM 2 — KOPYALA-YAPIŞTIR PROMPTLAR (PART A: S0-S12)

> ⚡ **Her prompt tamamen bağımsızdır.** Bible'lara bakmanıza gerek yok.
> Sadece istediğiniz sahnenin 📸 veya 🎥 bloğunu kopyalayıp yapıştırın.

---

## 🎬 SAHNE 0 (S0) — HOOK: GEÇİT (9 saniye)

> 🎯 **REFERANS:** **RA** p1 · p2 · p3 — gemi tam boy (p1) · 1/40 ölçek (p2) · alev (p3) · **RC** p1 (uzakta yüklü kapsül silueti)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space,
600 metres off the flank of a burning interstellar ship. Exactly 2 human
figures exist in this film and both are sealed inside the small capsule —
no figure is visible in frame.

SCENE: The crossing ship crosses the frame vertically, bow at the TOP and
stern at the bottom — a 210-metre interstellar vessel under constant burn:
a sleek 26-metre ceramic-white ice shield with a turquoise rim stripe at the bow, three habitat drums wrapped in clean white multi-layer insulation quilting, each ringed by a thin turquoise band, four polished bright-metal 9-metre propellant spheres, a
12-metre lattice berth boom standing out from its port flank, a long open
graphite truss spine, two dead-black knife-edge radiator wings, a 30-metre
satin pearl-grey conical shadow shield and an armoured drive block with three
recessed nozzles at the stern. From those nozzles, three pale blue-white
exhaust cones merge into one straight, sharply defined 400-metre lance that
leaves the BOTTOM of frame and thins away. At screen-left of the ship,
holding 40 metres off its flank and 118 metres below the berth boom, level
with the drive block: the ferry capsule — a 5.2-metre truncated cone
standing nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, with a 60-centimetre docking
probe on its nose and a cargo cradle of forty white core tubes under one
BURNT-ORANGE strap on its upper cone. It is one fortieth of the ship's
length — shorter than one propellant sphere is wide.

ENVIRONMENT: Hard vacuum. Absolute black sky, sharp pinpoint stars, no
haze, no nebula. Both craft are under 0.220 g of thrust acceleration.

CAMERA & LIGHT: 24mm spherical lens, fixed position 600 metres out, the
ship's axis vertical in frame. Hard parallel starlight from screen-left at
6500K; every shadow it casts is absolute black with a razor-sharp edge. The
blue lance lights the underside of the drive block and the capsule's base
ring from below. No fill light of any other kind.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly THREE habitat drums, FOUR propellant spheres, TWO
radiator wings, THREE engine nozzles. The exhaust is a straight sharp lance
— it never billows, curls or mushrooms. 0% bloom, no glow filter, no lens
flare, no soft focus. No readable text, letters, digits, numbers, insignia
or watermark anywhere. No subtitles, no title card. No nebula, no
atmospheric haze, no light scattering in vacuum. No Unreal Engine look, no
CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
9-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 600 metres out in vacuum, no camera movement. Exactly 2
human figures exist in this film and both are sealed inside the small
capsule — no figure is visible in frame.

SCENE: The crossing ship crosses the frame vertically, bow at the TOP and
stern at the bottom — a 210-metre interstellar vessel under constant burn:
a sleek 26-metre ceramic-white ice shield with a turquoise rim stripe at the bow, three habitat drums wrapped in clean white multi-layer insulation quilting, each ringed by a thin turquoise band, four polished bright-metal 9-metre propellant spheres, a
12-metre lattice berth boom standing out from its port flank, a long open
graphite truss spine, two dead-black knife-edge radiator wings, a 30-metre
satin pearl-grey conical shadow shield and an armoured drive block with three
recessed nozzles. From those nozzles, three pale blue-white exhaust cones
merge into one straight, sharply defined 400-metre lance that leaves the
BOTTOM of frame and thins away. At screen-left, holding 40 metres off the
ship's flank and level with the drive block, one fortieth of its length:
the ferry capsule, a 5.2-metre truncated cone standing nose-UP with a
60-centimetre probe on its nose and forty white core tubes under one
BURNT-ORANGE strap on its upper cone.

TIMELINE:
0.0s — Absolute stillness. The two craft hold their positions exactly;
nothing moves anywhere in frame except the fine internal flicker inside the
blue lance.
4.0s — A flake of frost the size of a hand breaks off the lowest propellant
sphere and begins to fall toward the bottom of frame, accelerating
smoothly, passing the shadow shield.
7.0s — The flake passes the capsule and shrinks into the blue lance and out
of frame. Both craft have not moved relative to each other by a single
metre.
9.0s — Hold on the last frame.

AUDIO: One continuous low hull-conducted engine drone, deep and steady,
with no high frequencies. No voice, no music, no exterior sound.

PHYSICS: Both craft are under 0.220 g of thrust acceleration and perfectly
matched, so neither rises nor falls relative to the other. The loose flake
is not accelerating, so it falls away toward the stern at 2.16 metres per
second squared — 1.1 metres in the first second, 9.7 metres in three.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible anywhere. Exactly THREE habitat drums,
FOUR propellant spheres, TWO radiator wings, THREE engine nozzles. The
exhaust is a straight sharp lance — it never billows, curls, mushrooms or
bends. The falling flake accelerates continuously downward and never
floats, hovers, freezes or drifts sideways. 0% bloom, no glow filter, no
lens flare, no soft focus. No readable text, letters, digits, numbers,
insignia or watermark. No subtitles, no title card. No nebula, no
atmospheric haze. No Unreal Engine look, no CGI aesthetic. Photorealistic
with 35mm film grain.
```

---

## 🎬 SAHNE 1 (S1) — PENCEREDEN YUKARI

> 🎯 **REFERANS:** **RD** p1 (ana iç kadraj) · **RE** p1 · p2 (iki insan) · **RA** p3 (pencereyi dolduran yanan motor bloğu)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin, seen from behind and between two seats. Exactly 2
human figures in frame — this film has exactly 2 humans in total.

SCENE: The cabin is a cramped 2.4-metre-wide cone interior with TWO
deep-bucketed seats side by side, reclined so the crew face UP toward the
window: the pilot in the LEFT seat, the engineer in the RIGHT seat, both
strapped into five-point harnesses drawn tight. The pilot is a lean
54-year-old man, 1.75 metres, with a thick grey moustache; the engineer is
a compact 33-year-old woman, 1.58 metres, her head completely shaved. Both
wear matte BURNT-ORANGE hard-shell pressure suits with crisp recessed
seams, graphite flex-weave at every joint and machined aluminium rings at
the shoulders — his shoulder bands charcoal grey, hers bone white, with a
12-centimetre machined tool block on HER LEFT FOREARM only. Both backs are
FLAT against the seats. Both helmets are sealed, each a single curved
optically clear pane in a 2-centimetre brushed-metal frame with its lower
seal ring visible at the collar. Ahead of and above them, one wide curved
window 1.6 metres across is filled almost entirely by the armoured drive
block of a huge ship forty metres away at screen-right, its
three recessed nozzles burning pale blue-white, the rest of the vessel receding upward beyond it into the black. A 40-centimetre brass
lanyard hangs from the window frame, dead straight DOWNWARD under tension.

ENVIRONMENT: The cabin is unpressurised, in hard vacuum, under 0.220 g of
thrust acceleration. Fine grit rests still in the floor seams.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. The
console's dim amber light segments underlight both figures; pale blue light
from the ship's exhaust enters the window from below-right and rims their
helmets. Hard starlight from screen-left through the window's left edge.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. The lanyard hangs straight down — never floating, never drifting.
0% bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers, icons or screen graphics anywhere. No holograms, no floating
interfaces. No subtitles, no title card, no watermark. No Unreal Engine
look, no CGI aesthetic. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: A cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats
side by side, reclined so the crew face UP toward the window: the pilot in
the LEFT seat, a lean 54-year-old man with a thick grey moustache; the
engineer in the RIGHT seat, a compact 33-year-old woman, 1.58 metres, her
head completely shaved. Both are strapped into five-point harnesses drawn
tight and wear matte BURNT-ORANGE hard-shell pressure suits with crisp
recessed seams, graphite flex-weave at every joint and machined aluminium
rings at the shoulders — his shoulder bands charcoal grey, hers bone white,
a 12-centimetre machined tool block on HER LEFT FOREARM only. Both backs
are flat against the seats; both helmets are sealed, each a single curved
optically clear pane in a 2-centimetre brushed-metal frame with its lower
seal ring visible at the collar, both faces fully readable through the
glass. The wide curved window above them is filled by the armoured drive
block of a huge ship forty metres away at screen-right, its
three recessed nozzles burning pale blue-white, the rest of the vessel receding upward beyond it into the black. A 40-centimetre brass
lanyard hangs from the window frame, dead straight downward under tension.

TIMELINE:
0.0s — Both faces are tilted up at the window, lit blue from above-right.
Nothing in the cabin moves. The lanyard hangs perfectly still.
4.0s — The engineer turns her head slowly to the pilot; her jawline scar
catches the amber console light. He does not turn.
7.0s — Her gloved right hand rises off the armrest and settles on the
machined six-detent selector at the console's left cheek. She does not turn
it.
10.0s — Both faces return to the window. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady. A
faint dry click as the glove settles on the metal selector. No voice, no
radio, no music.

PHYSICS: 0.220 g of thrust acceleration, down is toward the base of the
capsule. Arms have weight and move at ordinary human speed. The lanyard
stays vertical and taut; grit in the floor seams does not move.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; both visors optically clear, zero
tint, zero mirror coating. No helmet is opened, lifted or removed. The
lanyard hangs straight down — never floating, never drifting, never
swinging. Nothing in the cabin floats. 0% bloom, no glow filter, no soft
focus. No readable text, letters, digits, numbers, icons or screen graphics
anywhere. No holograms, no floating interfaces. No subtitles, no dialogue
text, no title card, no watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 2 (S2) — KIRK KAROT

> 🎯 **REFERANS:** **RC** p4 (yüklü kızak makro — kayış gergin) · **RC** p1 (gövde) · **RA** p4 (sağ kenarda küre + kapitone yalıtım)
>
> ⚠️ Bu bir DIŞ çekimdir; kabin/karakter sayfası yüklenmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Close exterior
view of a small spacecraft's upper hull in vacuum. Exactly 2 human figures
exist in this film and both are sealed inside this capsule — no figure is
visible in frame.

SCENE: The upper cone of the ferry capsule fills the left two thirds of the
frame — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and
flush rivet rows, the worn metal frame of its wide curved window running
across the top of the shot. Bolted to the upper cone on the starboard side:
the cargo cradle — a machined rack of FORTY identical sealed white core
tubes in five rows of eight, each tube 0.9 metres long and 0.12 metres
across, packed tight and held down by ONE wide BURNT-ORANGE strap drawn
tight through a machined buckle. The strap is the only warm saturated colour
anywhere in the frame. The rack's clamp bar is closed and pinned; frost
rimes the lower edge of every tube. Beyond and behind, 40 metres away at
screen-right and out of focus only slightly, the flank of an enormous ship:
polished bright-metal propellant sphere and clean white quilted insulation with a turquoise accent line, filling
the right edge of the frame from top to bottom.

ENVIRONMENT: Hard vacuum, 0.220 g of thrust acceleration, absolute black
sky with sharp stars in the gap between the two hulls.

CAMERA & LIGHT: 50mm spherical lens, fixed 6 metres off the capsule's
flank. Hard parallel starlight from screen-left picks out every tube's
upper curve and leaves the gaps between them in absolute black. Pale blue
light from far below rims the lower edge of the rack.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly FORTY core tubes in five rows of eight, exactly ONE
orange strap, exactly ONE clamp bar — these counts never change. The strap
is drawn tight and never loose. No damage, no scorch, no debris. 0% bloom,
no glow filter, no soft focus. No readable text, letters, digits, numbers,
labels, barcodes, insignia or watermark on any tube, strap or hull surface.
No subtitles, no title card. No Unreal Engine look, no CGI aesthetic.
Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 6 metres off the flank of a small spacecraft in vacuum,
no camera movement. Exactly 2 human figures exist in this film and both are
sealed inside this capsule — no figure is visible in frame.

SCENE: The upper cone of the ferry capsule fills the left two thirds of the
frame — matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and
flush rivet rows, the worn metal frame of its wide curved window across the
top of the shot. Bolted to the upper cone on the starboard side: the cargo
cradle — a machined rack of FORTY identical sealed white core tubes in five
rows of eight, each 0.9 metres long, packed tight and held down by ONE wide
BURNT-ORANGE strap drawn tight through a machined buckle, its clamp bar
closed and pinned. The strap is the only warm saturated colour in frame; frost
rimes the lower edge of every tube. At screen-right, 40 metres away, the
flank of an enormous ship fills the frame edge from top to bottom: polished bright-metal propellant sphere and clean white quilted insulation with a turquoise accent line.

TIMELINE:
0.0s — Stillness. Forty white tubes, one orange strap, hard shadows between
them. Nothing moves.
3.0s — Behind the rack, far away on the big ship's flank, a thin sheet of
frost lets go of the propellant sphere and falls toward the bottom of
frame, accelerating.
6.0s — The frost sheet leaves frame at the bottom. On the rack, nothing has
shifted: the strap stays taut, the tubes stay seated.
10.0s — Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady. A
faint metallic tick from the rack as it warms. No voice, no music.

PHYSICS: 0.220 g of thrust acceleration; down is toward the bottom of
frame. The released frost sheet is no longer accelerating, so it falls away
at 2.16 metres per second squared — 1.1 metres in the first second, 9.7
metres in three. Everything bolted down stays exactly where it is.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. No figure visible anywhere. Exactly FORTY core tubes in five rows
of eight, exactly ONE orange strap. Not one tube moves, loosens, rolls or
leaves the rack in this shot. The strap never loosens. The falling frost
accelerates continuously downward and never floats, hovers, freezes or
drifts sideways. 0% bloom, no glow filter, no soft focus. No readable text,
letters, digits, numbers, labels, barcodes or watermark anywhere. No
subtitles, no title card. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 3 (S3) — İLK KARTUŞ

> 🎯 **REFERANS:** **RD** p1 · p3 (seçici BİRİNCİ dişte) · **RE** p1 · p2

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats
side by side: the pilot in the LEFT seat, a lean 54-year-old man with a
thick grey moustache; the engineer in the RIGHT seat, a compact 33-year-old
woman with a completely shaved head. Both strapped into tight five-point
harnesses, wearing matte BURNT-ORANGE hard-shell pressure suits with crisp
recessed seams, graphite flex-weave at the joints and machined aluminium
rings at the shoulders — his shoulder bands charcoal grey, hers bone white,
a 12-centimetre machined tool block on HER LEFT FOREARM only. Both backs
flat, both helmets sealed, each visor a single curved optically clear pane
in a 2-centimetre brushed-metal frame with its lower seal ring visible at
the collar. Her gloved right hand grips the machined six-detent selector at
the console's left cheek, its stubby lever arm standing at the FIRST
detent. Above them the wide curved window is filled by the armoured drive
block of a huge ship, its three nozzles burning pale blue-white. A
40-centimetre brass lanyard hangs from the window frame, dead straight down
and taut.

ENVIRONMENT: Unpressurised cabin in hard vacuum, 0.220 g of thrust
acceleration. Fine grit lies still in the floor seams.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Dim amber
console segments underlight both figures; pale blue exhaust light enters
the window from above-right; hard starlight from screen-left.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT. Both backs flat, no back-mounted unit; both visors
optically clear, zero tint, zero mirror coating, faces fully readable.
Exactly SIX detents on the selector. The lanyard hangs straight down. 0%
bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers, icons or screen graphics anywhere. No holograms, no floating
interfaces. No subtitles, no title card, no watermark. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache; the engineer
in the RIGHT seat, a compact 33-year-old woman with a completely shaved
head. Both strapped into tight five-point harnesses in matte BURNT-ORANGE
hard-shell pressure suits — his shoulder bands charcoal grey, hers bone
white, a 12-centimetre tool block on HER LEFT FOREARM only. Both backs
FLAT, both helmets sealed: each visor a single curved optically clear pane
in a 2-centimetre brushed-metal frame, its seal ring visible at the collar,
both faces fully readable. Her gloved right hand is on the machined
six-detent selector at the console's left cheek. Above them the window is
filled by the drive block of a huge ship, three nozzles burning pale
blue-white. A brass lanyard hangs from the window frame, straight down and
taut.

TIMELINE:
0.0s — Stillness. Her hand rests on the selector arm.
4.0s — She rotates the arm one detent with a short firm movement; the metal
seats with a single dry click.
6.0s — She presses the arm down. A hard white jet fires from the base ring
below the frame and holds.
6.2s — Both bodies settle 2 centimetres deeper into their seat padding; the
harness webbing goes visibly taut across both chests; the lanyard's toggle
dips and stiffens. Grit in the floor seams jumps once and resettles.
9.5s — The window's view has begun, very slowly, to slide downward.
10.0s — The jet is still burning as the shot ends. Hold.

AUDIO: One continuous low hull-conducted engine drone. A dry metallic click
as the selector seats, then a hard double knock and a sustained hiss
through the frame that is still running as the shot ends. No voice, no
music.

PHYSICS: The main motor is fixed thrust and cannot be throttled; the
cartridge adds thrust for four seconds, raising acceleration from 0.220 g
to 0.260 g, so everyone briefly weighs more. Real time, ordinary human
speed.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face. Pilot LEFT, engineer RIGHT. Both backs flat, no
back-mounted unit; visors optically clear, zero tint, zero mirror coating;
no helmet opens or is removed. Exactly SIX detents; no case is ejected in
this shot. The
lanyard never floats, drifts or swings sideways. The jet is a straight
sharp cone — no billowing, no smoke, no sparks, no explosion. 0% bloom, no
glow filter, no soft focus. No readable text, letters, digits, numbers,
icons or screen graphics. No subtitles, no title card, no watermark.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 4 (S4) — 🎬 VİRAL #1: ALEV

> 🎯 **REFERANS:** **RA** p3 (alev · motor bloğu) · **RC** p1 (yüklü kapsül)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space, 120
metres off the stern of a burning interstellar ship. Exactly 2 human
figures exist in this film and both are sealed inside the small capsule —
no figure is visible in frame.

SCENE: The armoured drive block of a 210-metre interstellar vessel fills
the upper right of the frame — a dense mass of machined graphite-grey
armour panels with heavy bolted flanges, heat-discoloured to straw and
blue-grey near the throats, carrying THREE deeply recessed engine nozzles
in a triangle. Three pale blue-white exhaust cones merge below them into
one straight, sharply defined 400-metre lance that runs down the right side
of the frame and leaves the BOTTOM of frame, thinning as it goes. At
screen-left, 40 metres out from the ship's flank and level with the nozzle
plane: the ferry capsule — a 5.2-metre truncated cone standing nose-UP,
matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, a 60-centimetre docking probe with
three alignment vanes on its nose pointing at the TOP of frame, one wide
curved window in its upper cone, forty white core tubes under a
BURNT-ORANGE strap on its starboard side, four scorched nozzles in its base
ring. It is dwarfed: the drive block alone is five times its height.

ENVIRONMENT: Hard vacuum. Absolute black sky, sharp stars, no haze, no
scattering around the lance.

CAMERA & LIGHT: 24mm spherical lens, fixed 120 metres out. The blue lance
is a hard directional source from below-right: it rims the capsule's base
ring and the underside of the drive block and leaves every upward-facing
surface in absolute black. Hard starlight from screen-left picks out the
capsule's window frame and the top of the cargo rack.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly THREE nozzles, ONE merged lance, ONE capsule. The exhaust
is straight and sharply defined — it never billows, curls, mushrooms or
bends, and there are no shock diamonds spreading sideways, no smoke, no
sparks, no debris. The capsule is never larger than one fifth of the drive
block's height. 0% bloom, no glow filter, no lens flare, no anamorphic
streak, no soft focus. No readable text, letters, digits, numbers, insignia
or watermark. No subtitles, no title card. No atmospheric haze, no light
scattering in vacuum. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 120 metres out in vacuum, no camera movement. Exactly 2
human figures exist in this film and both are sealed inside the small
capsule — no figure is visible in frame.

SCENE: The armoured drive block of a 210-metre interstellar vessel fills
the upper right of frame — machined graphite-grey armour panels with heavy
bolted flanges, heat-discoloured to straw and blue-grey, carrying THREE
deeply recessed engine nozzles. Three pale blue-white exhaust cones merge
below them into one straight, sharply defined 400-metre lance running down
the right of frame and out of the BOTTOM. At screen-left, 40 metres off the
ship's flank: the ferry capsule — a 5.2-metre truncated cone standing
nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, a 60-centimetre docking probe with
three alignment vanes on its nose pointing at the TOP of frame, one wide
curved window in the upper cone, forty white core tubes under a
BURNT-ORANGE strap on its starboard side, four scorched nozzles in the base
ring. The drive block alone is five times the capsule's height.

TIMELINE:
0.0s — A spent white cartridge case, ejected a moment ago, tumbles down
past the capsule three metres clear of its hull, gathering speed, and
leaves the bottom of frame.
2.0s — The capsule rises steadily up-frame at a slow walking pace, its nose
and probe pointing at the top of frame throughout; it neither pitches nor
rolls. The drive block's nozzle plane slides down past it.
6.0s — The capsule's base ring draws level with the top of the drive block.
Blue light rakes across its underside and slides off as it climbs clear.
10.0s — Still climbing at the same steady rate. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
nothing else — vacuum carries no sound from either craft. No voice, no
music.

PHYSICS: Both craft are under thrust and matched; the capsule carries 1.6
metres per second of climb from a cartridge burn moments ago and rises at
that constant rate. The tumbling case is unpowered and falls away at 2.16
metres per second squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible anywhere. Exactly THREE nozzles, ONE
merged lance, ONE capsule, ONE tumbling case. The capsule only ever rises
up-frame — no descent, no drift toward the exhaust, no direction reversal,
no mirrored composition, and it never pitches, rolls or turns. The exhaust
is straight and sharply defined — never billowing, curling, mushrooming or
bending; no smoke, no sparks, no explosion, no debris field. 0% bloom, no
glow filter, no lens flare, no anamorphic streak, no soft focus. No
readable text, letters, digits, numbers, insignia or watermark. No
subtitles, no title card. No atmospheric haze. Photorealistic with 35mm
film grain.
```

---

## 🎬 SAHNE 5 (S5) — MAVİ ALTTAN

> 🎯 **REFERANS:** **RE** p1 · p4 (pilot tek yüz, kasklı — vizörün üç işareti p4'te)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Tight interior
portrait inside a small spacecraft cabin. Exactly 1 human figure in frame;
this film has exactly 2 humans in total and the second is out of frame at
screen-right.

SCENE: A close view of the pilot in the LEFT seat — a lean 54-year-old man,
1.75 metres, weathered pale olive skin with visible pore texture, a THICK
GREY MOUSTACHE over his upper lip and no beard, close-cropped grey hair
receding at the temples, and a 2-centimetre shiny burn scar on the BONE OF
HIS RIGHT CHEEK below the outer corner of his right eye; the rest of his
face is completely unmarked. He is strapped into a five-point harness in a
matte BURNT-ORANGE hard-shell pressure suit with crisp recessed seams,
graphite flex-weave at the shoulders and a charcoal-grey band inlaid across
each shoulder plate. His back is FLAT against the seat. His helmet is
sealed: a single curved optically clear pane held in a 2-centimetre
brushed-metal frame, its lower seal ring visible where it meets the collar,
one thin unbroken specular line along the pane's upper edge, his whole face
fully readable through the glass. His eyes are angled up and to
screen-right, tracking something moving. A faint film of breath
condensation sits along the bottom edge of the glass only.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust acceleration.

CAMERA & LIGHT: 85mm spherical lens, fixed 1.2 metres from his face,
shallow depth so the console behind falls soft. Pale blue light from the
ship's exhaust enters from BELOW and rakes up across his jaw, moustache and
the underside of his helmet frame; dim amber console light from the right;
absolute black behind him.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 1 human figure in
frame — no second face, no duplicate, no reflected face in the visor. His
back is flat, no back-mounted unit; the visor is optically clear with zero
tint, zero mirror coating and no environment reflection; it is never open,
lifted or removed and no bare skin shows above the collar. The scar stays
on his right cheekbone and appears nowhere else. 0% bloom, no glow filter,
no soft focus — skin keeps pores and stubble texture inside the blue light.
No readable text, letters, digits, numbers or HUD graphics anywhere. No
subtitles, no title card, no watermark. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 1.2 metres from a seated man's face inside a small
spacecraft cabin, no camera movement. Exactly 1 human figure in frame; this
film has exactly 2 humans in total and the second is out of frame at
screen-right.

SCENE: The pilot in the LEFT seat — a lean 54-year-old man, weathered pale
olive skin with visible pore texture, a THICK GREY MOUSTACHE and no beard,
close-cropped grey hair receding at the temples, a 2-centimetre shiny burn
scar on the BONE OF HIS RIGHT CHEEK below the outer corner of his right
eye, the rest of his face completely unmarked. He is strapped into a
five-point harness in a matte BURNT-ORANGE hard-shell pressure suit with
crisp recessed seams, graphite flex-weave at the shoulders and a
charcoal-grey band across each shoulder plate. His back is flat against the
seat. His helmet is sealed: a single curved optically clear pane in a
2-centimetre brushed-metal frame, its lower seal ring visible at the
collar, one thin specular line along the pane's upper edge, his whole face
fully readable through the glass.

TIMELINE:
0.0s — His eyes are angled up and to screen-right. They track slowly and
steadily downward, following something sliding past outside.
3.0s — The blue light on his face shifts by a few degrees as the source
below moves; the rim on his jaw thins.
5.0s — He blinks once, slowly. His eyes return to the top of their travel
and begin tracking down again at the same rate.
8.0s — His breath fogs the very bottom edge of the glass and clears.
10.0s — Hold, eyes still tracking.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
the soft close sound of his breathing inside the helmet. No voice, no
radio, no music.

PHYSICS: 0.220 g of thrust acceleration; his head has weight and rests back
in the seat. Real-time, ordinary human speed — no slow motion.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 1 human figure in frame — no second face, no duplicate, no
reflected face in the visor, no autonomous reflection. His back is flat, no
back-mounted unit; the visor is optically clear with zero tint, zero mirror
coating and zero environment reflection; it never opens, lifts, retracts or
clears away, and no bare skin shows above the collar. The scar stays on his
right cheekbone throughout and appears nowhere else; bone structure,
moustache and hairline stay identical from first frame to last — no
morphing, no feature drift, no ageing. 0% bloom, no glow filter, no soft
focus — skin keeps pore and stubble texture. No readable text, letters,
digits, numbers, HUD graphics or captions. No subtitles, no dialogue text,
no title card, no watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 6 (S6) — TUTMA

> 🎯 **REFERANS:** **RC** p1 · p2 (kartuş rafı: 4 dolu / 2 boş = p2'nin durumu) · **RA** p1 (gölge kalkanı gövde sırasından)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Exterior view of
a small spacecraft in vacuum, 25 metres out. Exactly 2 human figures exist
in this film and both are sealed inside this capsule — no figure is visible
in frame.

SCENE: The ferry capsule stands nose-UP in the left half of the frame — a
5.2-metre truncated cone, 3.6 metres across its flat base, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows, a
60-centimetre docking probe with three alignment vanes on its nose pointing
at the TOP of frame, one wide curved window in the upper cone with two
helmeted heads dimly visible behind the glass, forty white core tubes under
a BURNT-ORANGE strap on its starboard side, four scorched nozzles in the
base ring, and a six-socket cartridge rack low on its port flank with FOUR
sockets loaded and TWO empty and scorched. From two small ports set high on
its shoulder, near the top face, two short hard white jets fire straight UP
out of the top of frame. At screen-right, 40 metres away, the wide satin pearl-grey face of a 30-metre conical shadow shield fills the frame edge, turned
toward the bottom of frame. Far below, the top of a pale blue-white exhaust
lance shows at the bottom corner.

ENVIRONMENT: Hard vacuum, absolute black sky with sharp stars, 0.220 g of
thrust acceleration.

CAMERA & LIGHT: 50mm spherical lens, fixed 25 metres out. Hard parallel
starlight from screen-left; weak pale blue light from far below rims the
base ring only. The retro jets are small hard-edged white cones with sharp
boundaries.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible outside
the hull. Exactly SIX cartridge sockets with exactly TWO empty, exactly
FOUR base nozzles, exactly FORTY core tubes, exactly ONE probe with THREE
vanes. Exactly TWO retro jets, both pointing at the top of frame. The jets
are straight sharp cones — no billowing, no curling, no smoke, no sparks,
no explosion. 0% bloom, no glow filter, no lens flare, no soft focus. No
readable text, letters, digits, numbers, insignia or watermark. No
subtitles, no title card. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 25 metres off a small spacecraft in vacuum, no camera
movement. Exactly 2 human figures exist in this film and both are sealed
inside this capsule — no figure is visible in frame.

SCENE: The ferry capsule stands nose-UP in the left half of frame — a
5.2-metre truncated cone, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams and flush rivet rows, a 60-centimetre docking probe with
three alignment vanes on its nose pointing at the TOP of frame, one wide
curved window in the upper cone with two helmeted heads dimly visible
behind the glass, forty white core tubes under a BURNT-ORANGE strap on its
starboard side, four scorched nozzles in the base ring, and a six-socket
cartridge rack low on its port flank. At screen-right, 40 metres away, the
wide satin pearl-grey face of a 30-metre conical shadow shield fills the frame
edge. Far below at the bottom corner, the head of a pale blue-white exhaust
lance.

TIMELINE:
0.0s — The capsule is rising steadily up-frame at a slow walking pace, nose
and probe pointing at the top of frame; the grey shield slides down past it
at screen-right. Its cartridge rack shows FIVE loaded sockets and ONE empty.
1.0s — Two short hard white jets fire from small ports high on its
shoulder, straight up out of the top of frame, and hold.
1.2s — The capsule's climb visibly slows. Behind the window, both helmeted
heads lift a centimetre against their harnesses as their weight drops.
5.0s — The jets cut out. The capsule has stopped climbing: it now hangs
exactly level with the shadow shield's rim and stays there.
6.5s — A spent white cartridge case is ejected clear of the flank and falls
away toward the bottom of frame, accelerating and tumbling. The rack now
shows FOUR loaded sockets and TWO empty and scorched.
10.0s — Absolute stillness. Hold.

AUDIO: One continuous low hull-conducted engine drone. A hard double knock
and a four-second hiss carried through the hull as the retro cartridge
fires, then back to the drone alone. No voice, no music.

PHYSICS: The main motor is fixed thrust and cannot be throttled. The retro
cartridge pushes against the direction of travel for four seconds, dropping
net acceleration from 0.220 g to 0.179 g, so everything aboard briefly
weighs less and the climb rate falls to zero. The ejected case falls at
2.16 metres per second squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. No figure visible outside the hull. Exactly SIX sockets, ONE case
ejected, TWO retro jets, FOUR base nozzles, FORTY core tubes. The capsule
never descends, never drifts toward the exhaust, never pitches, rolls or
turns; no direction reversal. The jets are straight sharp cones — no
billowing, no curling, no smoke, no sparks, no explosion, no debris field.
The falling case accelerates continuously and never hovers. 0% bloom, no
glow filter, no lens flare, no soft focus. No readable text, letters,
digits, numbers, insignia or watermark. No subtitles, no title card.
Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 7 (S7) — KANAT

> 🎯 **REFERANS:** **RA** p1 · p4 (radyatör kanadı geometrisi + omurga) · **RC** p1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space,
80 metres off the flank of an interstellar ship. Exactly 2 human figures
exist in this film and both are sealed inside the small capsule — no figure
is visible in frame.

SCENE: A dead-black knife-edge radiator wing crosses the upper third of the
frame from screen-right to screen-left — a flat panel 40 metres long and
only 30 centimetres thick, standing straight out from the ship's spine,
matte and light-swallowing, its edge cutting the star field into two halves
like a blade. Behind and to screen-right, the ship's open hexagonal
graphite truss spine recedes upward toward the top of frame with bolted
nodes and clipped cable runs. Below the wing at screen-left, small in the
lower third of the frame and 40 metres out from the hull: the ferry capsule
— a 5.2-metre truncated cone standing nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe,
a 60-centimetre docking probe with three alignment vanes on its nose
pointing at the TOP of frame, one wide curved window in the upper cone,
forty white core tubes under a BURNT-ORANGE strap. The wing is eight times
the capsule's height and hangs directly across its path.

ENVIRONMENT: Hard vacuum. Absolute black sky, sharp stars, no haze.

CAMERA & LIGHT: 24mm spherical lens, fixed 80 metres out. Hard parallel
starlight from screen-left grazes the wing's upper surface and leaves its
underside in absolute black; the capsule is lit from the same side, with
only a weak blue rim on its base ring from the exhaust far below.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly ONE radiator wing in frame, exactly ONE capsule. The wing
is dead matte black — no gloss, no glint, no mirror reflection, never
glowing. 0% bloom, no glow filter, no lens flare, no soft focus. No
readable text, letters, digits, numbers, insignia or watermark. No
subtitles, no title card. No atmospheric haze, no light scattering in
vacuum. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 80 metres off the flank of an interstellar ship in
vacuum, no camera movement. Exactly 2 human figures exist in this film and
both are sealed inside the small capsule — no figure is visible in frame.

SCENE: A dead-black knife-edge radiator wing crosses the upper third of
frame from screen-right to screen-left — a flat panel 40 metres long and 30
centimetres thick standing straight out from the ship's spine, matte and
light-swallowing, its edge cutting the star field like a blade. Behind it
at screen-right the ship's open hexagonal graphite truss spine recedes
toward the top of frame. Below the wing at screen-left, small in the lower
third and 40 metres out from the hull: the ferry capsule, a 5.2-metre
truncated cone standing nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe, a
60-centimetre docking probe with three alignment vanes on its nose pointing
at the TOP of frame, one wide curved window in the upper cone, forty white
core tubes under a BURNT-ORANGE strap. The wing is eight times the
capsule's height and hangs directly across its path.

TIMELINE:
0.0s — Nothing moves. The capsule holds station exactly level, neither
rising nor falling; the ship holds its burn.
4.0s — Behind the capsule's window, one helmeted head tilts back to look up
at the wing. Nothing else changes.
7.0s — A single flake of ice drifts off the wing's edge and falls away
toward the bottom of frame, accelerating, passing two metres clear of the
capsule.
10.0s — Stillness again. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
nothing else. No voice, no music.

PHYSICS: Both craft are matched at 0.220 g of thrust acceleration, so the
capsule holds its position exactly. The released ice flake is unpowered and
falls away at 2.16 metres per second squared — 1.1 metres in the first
second, 9.7 metres in three.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible outside the hull. Exactly ONE radiator
wing in frame, exactly ONE capsule, exactly ONE falling flake. The capsule
does not move relative to the ship in this shot — no climb, no descent, no
drift, no pitch, no roll. The wing is dead matte black — no gloss, no
glint, no mirror reflection, never glowing. The falling flake accelerates
continuously downward and never floats, hovers, freezes or drifts sideways.
0% bloom, no glow filter, no lens flare, no soft focus. No readable text,
letters, digits, numbers, insignia or watermark. No subtitles, no title
card. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 8 (S8) — İKİNCİ TIRMANIŞ

> 🎯 **REFERANS:** **RD** p1 · p3 (seçici ÜÇÜNCÜ dişte) · **RE** p1 · p2 · **RA** p4 (pencerede omurga + kanat altı)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache and a 2-centimetre burn scar on the bone of his right cheek; the
engineer in the RIGHT seat, a compact 33-year-old woman with a completely
shaved head and a pale 4-centimetre line along the bone of her right jaw.
Both strapped into tight five-point harnesses in matte BURNT-ORANGE
hard-shell pressure suits with crisp recessed seams, graphite flex-weave at
the joints and machined aluminium rings at the shoulders — his shoulder
bands charcoal grey, hers bone white, a 12-centimetre machined tool block
on HER LEFT FOREARM only. Both backs flat, both helmets sealed, each visor
a single curved optically clear pane in a 2-centimetre brushed-metal frame
with its seal ring visible at the collar. Her gloved right hand grips the
six-detent selector, its arm standing at the THIRD detent. Through the wide
curved window above them, the ship's open hexagonal truss spine fills the
upper frame and, higher still at the top edge, the black underside of a
radiator wing. A 40-centimetre brass lanyard hangs from the window frame,
straight down and taut.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust acceleration.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Dim amber
console segments underlight both figures; weak blue light from far below;
hard starlight from screen-left through the window's left edge.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. Exactly SIX detents on the selector. Her scar stays on her right
jawline and his on his right cheekbone. The lanyard hangs straight down. 0%
bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers, icons or screen graphics. No holograms. No subtitles, no title
card, no watermark. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both strapped into
tight harnesses in matte BURNT-ORANGE hard-shell pressure suits — his
shoulder bands charcoal grey, hers bone white, a 12-centimetre tool block
on HER LEFT FOREARM only. Both backs FLAT, both helmets sealed: each visor
a single curved optically clear pane in a 2-centimetre brushed-metal frame,
its seal ring visible at the collar, both faces fully readable. Through the
window above them, the ship's open truss spine fills the upper frame and
the black underside of a radiator wing shows at the top edge. A brass
lanyard hangs from the window frame, straight down.

TIMELINE:
0.0s — Both faces are up at the window. Her gloved right hand is already on
the six-detent selector.
2.0s — She rotates the arm one detent; it seats with a single dry click.
The pilot's head turns 20 degrees toward her and back.
6.0s — She presses. A hard white jet fires from the base ring below frame
and holds; both bodies settle 2 centimetres deeper into the padding and the
harness webbing goes taut across both chests. The lanyard stiffens.
9.5s — Through the window, the truss spine has begun sliding downward.
10.0s — The jet is still burning as the shot ends. Hold.

AUDIO: One continuous low hull-conducted engine drone. A dry metallic click
as the selector seats, then a hard double knock and a sustained hiss
through the frame that is still running as the shot ends. No voice, no
music.

PHYSICS: The main motor is fixed thrust and cannot be throttled; the
cartridge adds thrust for four seconds, raising acceleration from 0.220 g
to 0.260 g, so everyone briefly weighs more, and the capsule leaves at 1.6
metres per second relative to the ship.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens or is removed. Exactly SIX detents;
no case is ejected in this shot. Her scar stays on her right jawline and
his on his right
cheekbone; both faces keep identical bone structure — no morphing. The
lanyard never floats or drifts; nothing in the cabin floats. The jet is a
straight sharp cone — no billowing, no smoke, no sparks, no explosion. 0%
bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers, icons or screen graphics. No subtitles, no dialogue text, no title
card, no watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 9 (S9) — YAKLAŞAN AĞIZ

> 🎯 **REFERANS:** **RE** p4 ⭐ (iki yüz yan yana — KLON KAPISI) · **RD** p1 (pencere çerçevesi) · **RA** p4 (kanadın siyah altı)
>
> ⚠️ Bu bir İÇ karakter sahnesidir; ayrışma burada ölçülür.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin, tight two-shot from the front. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: A tight framing of two helmeted heads side by side, seen from ahead
and slightly above, with the wide curved window and its worn machined frame
filling the background behind and above them. At screen-left the pilot, a
lean 54-year-old man with a thick grey moustache, close-cropped grey hair
and a 2-centimetre shiny burn scar on the BONE OF HIS RIGHT CHEEK; at
screen-right the engineer, a compact 33-year-old woman with a completely
shaved head, a broad flat nose and a pale 4-centimetre surgical line along
the BONE OF HER RIGHT JAW. Both wear matte BURNT-ORANGE hard-shell pressure
suits with machined aluminium collar rings — his shoulder band charcoal
grey, hers bone white. Both helmets are sealed: single curved optically
clear panes in 2-centimetre brushed-metal frames, each frame's lower seal
ring visible at the collar, one thin specular line along each pane's upper
edge, both faces fully readable through the glass. Beyond the window,
filling its upper half, the dead-black underside of a radiator wing hangs
close, its knife edge crossing the glass diagonally, blotting out the stars
behind it.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust acceleration.

CAMERA & LIGHT: 50mm spherical lens, fixed 2.2 metres ahead of the two
heads. Dim amber console light from below picks out both faces; hard
starlight from screen-left through the window's remaining clear corner. The
black wing kills all light from above.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no duplicate, no clone, no reflected face in either visor.
Pilot LEFT, engineer RIGHT. The two are unmistakably different people:
different height, skin, head and face. Both backs flat, no back-mounted
unit; both visors optically clear, zero tint, zero mirror coating, no
environment reflection, faces fully readable. Scars stay on his right
cheekbone and her right jawline. The wing is dead matte black — no gloss,
no glint, never glowing. 0% bloom, no glow filter, no soft focus. No
readable text, letters, digits, numbers or HUD graphics. No subtitles, no
title card, no watermark. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 2.2 metres ahead of two seated helmeted heads inside a
small spacecraft cabin, no camera movement. Exactly 2 human figures in
frame — this film has exactly 2 humans in total.

SCENE: Two helmeted heads side by side, seen from ahead and slightly above,
the wide curved window and its worn machined frame filling the background.
At screen-left the pilot, a lean 54-year-old man with a thick grey
moustache, close-cropped grey hair and a 2-centimetre shiny burn scar on
the BONE OF HIS RIGHT CHEEK; at screen-right the engineer, a compact
33-year-old woman with a completely shaved head, a broad flat nose and a
pale 4-centimetre surgical line along the BONE OF HER RIGHT JAW. Both wear
matte BURNT-ORANGE hard-shell pressure suits with machined collar rings —
his shoulder band charcoal grey, hers bone white. Both helmets are sealed:
single curved optically clear panes in 2-centimetre brushed-metal frames,
each seal ring visible at the collar, both faces fully readable through the
glass. Beyond the window, the dead-black underside of a radiator wing hangs
close, its knife edge crossing the glass diagonally.

TIMELINE:
0.0s — Both faces are angled up at the window, still, watching the black
edge above them.
1.0s — A spent white cartridge case drops past the outside of the glass,
close and fast, and is gone below.
2.5s — The black edge grows measurably larger in the glass as the capsule
climbs; the last clear corner of star field narrows.
5.0s — Both heads turn to each other at the same moment, hold for a beat,
and turn back up. Neither speaks; no mouth moves.
8.0s — The black edge fills two thirds of the window. The amber console
light is now the only light on their faces.
10.0s — Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
the close sound of two people breathing inside sealed helmets. No voice, no
radio, no music, no dialogue of any kind.

PHYSICS: The capsule is climbing at 1.6 metres per second relative to the
ship, so the wing above appears to descend toward it at that steady rate.
0.220 g of thrust acceleration; heads have weight and move at ordinary
human speed.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no clone,
no reflected face in either visor. Pilot LEFT, engineer RIGHT — never
swapped. The two remain unmistakably different people; both faces keep
identical bone structure — no morphing, no feature drift. Scars stay on his
right cheekbone and her right jawline. Both backs flat, no back-mounted
unit; visors optically clear, zero tint, zero mirror coating; neither opens
nor is removed. No mouth moves and no one speaks — no lip movement, no
talking face, no invented speaker. The wing is dead matte black — no gloss,
no glint, never glowing. 0% bloom, no glow filter, no soft focus. No
readable text, letters, digits, numbers or HUD graphics. No subtitles, no
dialogue text, no title card, no watermark. Photorealistic with 35mm film
grain.
```

---

## 🎬 SAHNE 10 (S10) — 🎬 VİRAL #2: ERKEN TUTMA

> 🎯 **REFERANS:** **RA** p4 (kanat ucu + omurga) · **RC** p1 · p2 (raf: 3 dolu / 3 boş)

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Exterior view in
vacuum, 30 metres from a small spacecraft, with a huge black panel edge
directly above it. Exactly 2 human figures exist in this film and both are
sealed inside the capsule — no figure is visible in frame.

SCENE: The ferry capsule stands nose-UP in the lower left of frame — a
5.2-metre truncated cone, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams, a 60-centimetre docking probe with three alignment vanes on
its nose pointing at the TOP of frame, one wide curved window in the upper
cone, forty white core tubes under a BURNT-ORANGE strap on its starboard
side, and a six-socket cartridge rack low on its port flank with THREE
sockets loaded and THREE empty and scorched. Two short hard white jets fire
from small ports high on its shoulder, straight up out of the top of frame.
Six metres above the probe tip, crossing the entire frame from screen-left
to screen-right, hangs the dead-black knife edge of a 40-metre radiator
wing — a flat panel only 30 centimetres thick, matte and light-swallowing,
its edge cutting the star field in half. Behind it at screen-right the
ship's graphite truss spine recedes upward.

ENVIRONMENT: Hard vacuum, absolute black sky with sharp stars, 0.220 g of
thrust acceleration.

CAMERA & LIGHT: 50mm spherical lens, fixed 30 metres out. Hard parallel
starlight from screen-left rakes the capsule's flank and the wing's upper
surface; the wing's underside is absolute black, and its shadow lies across
the capsule's nose as a razor-sharp line.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible outside
the hull. Exactly SIX cartridge sockets with exactly THREE empty, exactly
TWO retro jets, exactly ONE probe with THREE vanes, exactly FORTY core
tubes. The gap between probe tip and wing edge is a clear 6 metres — the
two never touch, overlap or intersect. The wing is dead matte black — no
gloss, no glint, never glowing. The jets are straight sharp cones — no
billowing, no smoke, no sparks, no explosion. 0% bloom, no glow filter, no
lens flare, no soft focus. No readable text, letters, digits, numbers,
insignia or watermark. No subtitles, no title card. Photorealistic with
35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 30 metres off a small spacecraft in vacuum, no camera
movement. Exactly 2 human figures exist in this film and both are sealed
inside the capsule — no figure is visible in frame.

SCENE: The ferry capsule stands nose-UP in the lower left of frame — a
5.2-metre truncated cone, matte ceramic-white composite over a dark graphite frame, a sweeping TURQUOISE chevron stripe down its flank, crisp recessed seams, a 60-centimetre docking probe with three alignment vanes on
its nose pointing at the TOP of frame, one wide curved window in the upper
cone, forty white core tubes under a BURNT-ORANGE strap on its starboard
side, a six-socket cartridge rack low on its port flank. Crossing the whole
frame above it from screen-left to screen-right: the dead-black knife edge
of a 40-metre radiator wing, a flat panel 30 centimetres thick, matte and
light-swallowing. Behind it at screen-right the ship's graphite truss spine
recedes upward.

TIMELINE:
0.0s — The capsule climbs steadily up-frame at a slow walking pace, nose
and probe pointing at the top of frame. The black wing edge hangs 16 metres
above the probe tip and is closing.
1.0s — Two short hard white jets fire from ports high on its shoulder,
straight up out of the top of frame, and hold.
2.0s — The climb slows visibly. The wing's razor-sharp shadow slides down
across the capsule's nose and then across the window.
5.0s — The jets cut out. The capsule stops dead, its probe tip a clear 6
metres below the black edge, and holds there.
6.5s — A spent white cartridge case ejects from the flank and falls away
toward the bottom of frame, tumbling and accelerating. The rack now shows
TWO loaded sockets and FOUR empty.
10.0s — Absolute stillness under the black edge. Hold.

AUDIO: One continuous low hull-conducted engine drone. A hard double knock
and a four-second hiss through the hull as the retro cartridge fires, then
the drone alone. No voice, no music.

PHYSICS: The retro cartridge drops net acceleration from 0.220 g to 0.179 g
for four seconds, killing 1.6 metres per second of climb rate; everything
aboard briefly weighs less. The ejected case is unpowered and falls at 2.16
metres per second squared. The capsule and the wing never touch.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. No figure visible outside the hull. Exactly SIX sockets, ONE case
ejected, TWO retro jets, ONE wing in frame. The capsule only rises and then
stops — no descent, no drift toward the exhaust, no direction reversal, no
pitch, no roll. Probe tip and wing edge keep a clear 6-metre gap — no
contact, no overlap, no clipping, no phasing. The wing is dead matte black
— no gloss, no glint, never glowing. The jets are straight sharp cones — no
billowing, no smoke, no sparks, no explosion. The falling case accelerates
continuously and never hovers. 0% bloom, no glow filter, no lens flare, no
soft focus. No readable text, letters, digits, numbers, insignia or
watermark. No subtitles, no title card. Photorealistic with 35mm film
grain.
```

---

## 🎬 SAHNE 11 (S11) — YANA KAYMA

> 🎯 **REFERANS:** **RD** p1 (kordon — yana savrulup dikeye oturur) · **RE** p1 · p2 · **RA** p4 (pencerede küre + omurga)
>
> ⚠️ İÇ sahne: kapsül dışı (RC) kadraja girmez.

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Interior of a
small spacecraft cabin from behind and between two seats. Exactly 2 human
figures in frame — this film has exactly 2 humans in total.

SCENE: The cramped 2.4-metre-wide cone cabin with TWO deep-bucketed seats:
the pilot in the LEFT seat, a lean 54-year-old man with a thick grey
moustache; the engineer in the RIGHT seat, a compact 33-year-old woman with
a completely shaved head. Both strapped into five-point harnesses in matte
BURNT-ORANGE hard-shell pressure suits with crisp recessed seams and
machined aluminium rings at the shoulders — his shoulder bands charcoal
grey, hers bone white, a 12-centimetre machined tool block on HER LEFT
FOREARM only. Both backs flat, both helmets sealed, each visor a single
curved optically clear pane in a 2-centimetre brushed-metal frame with its
lower seal ring visible at the collar. His gloved left hand is closed
around a short machined translation grip on the console's left edge.
Through the wide curved window above them: at screen-right, the enormous
flank of the ship — graphite truss members and one polished bright-metal propellant sphere; at screen-left, open black space and sharp stars. The
40-centimetre brass lanyard hangs from the window frame, dead straight
DOWNWARD and taut — the capsule is not yet moving sideways.

ENVIRONMENT: Unpressurised cabin in vacuum, 0.220 g of thrust
acceleration.

CAMERA & LIGHT: 35mm spherical lens, fixed low behind the seats. Dim amber
console segments underlight both figures; hard starlight from screen-left
through the window's clear half.

NEGATIVE: Fixed locked-off camera, single frame. Exactly 2 human figures —
no third person, no clone, no reflected face in the glass. Pilot LEFT,
engineer RIGHT — never swapped. Both backs flat, no back-mounted unit; both
visors optically clear, zero tint, zero mirror coating, faces fully
readable. The lanyard hangs straight down and taut — never floating, never
loose, never coiled. 0% bloom, no glow filter, no soft focus. No readable
text, letters, digits, numbers, icons or screen graphics. No holograms. No
subtitles, no title card, no watermark. Photorealistic with 35mm film
grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera low behind two seats inside a small spacecraft cabin, no
camera movement. Exactly 2 human figures in frame — this film has exactly 2
humans in total.

SCENE: The cramped cone cabin with TWO seats side by side: the pilot in the
LEFT seat, a lean 54-year-old man with a thick grey moustache and a
2-centimetre burn scar on the bone of his right cheek; the engineer in the
RIGHT seat, a compact 33-year-old woman with a completely shaved head and a
pale 4-centimetre line along the bone of her right jaw. Both strapped into
harnesses in matte BURNT-ORANGE hard-shell pressure suits — his shoulder
bands charcoal grey, hers bone white, a 12-centimetre tool block on HER
LEFT FOREARM only. Both backs FLAT, both helmets sealed: each visor a
single curved optically clear pane in a 2-centimetre brushed-metal frame,
its seal ring visible at the collar. Through the window above them: at
screen-right the enormous flank of the ship, graphite truss members and one
polished propellant sphere; at screen-left open black space and sharp stars. A
brass lanyard hangs from the window frame.

TIMELINE:
0.0s — The lanyard hangs dead vertical. His gloved left hand closes around
a short machined translation grip on the console's left edge.
1.5s — He tips the grip. Small manoeuvring jets rattle outside the frame;
the lanyard swings 20 degrees toward screen-right, then settles back to
vertical as the push ends and the capsule glides.
4.0s — Through the window the ship's flank slides slowly toward
screen-right, opening a widening band of black star field at screen-left.
The vertical position of everything outside stays exactly the same.
7.5s — He tips the grip the other way. A second short rattle; the lanyard
swings 20 degrees toward screen-left and settles. The slide outside stops.
10.0s — The ship's flank now sits a little further right in the window,
and everything is still. Hold.

AUDIO: One continuous low hull-conducted engine drone, plus two short flat
thruster rattles carried through the frame — one near the start, one near
the end. No voice, no music.

PHYSICS: Sideways translation is cheap here because there is no
gravity component across the thrust axis; a short push, a slow glide and a
short brake move the capsule 6 metres further outboard, clearing the
radiator wing tip, without changing its height at all. Vertical
acceleration stays at 0.220 g throughout, so nothing rises or falls.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom. Exactly 2 human figures — no third person, no duplicate, no
reflected face in the glass. Pilot LEFT, engineer RIGHT — never swapped.
Both backs flat, no back-mounted unit; visors optically clear, zero tint,
zero mirror coating; no helmet opens or is removed. The view outside moves
only sideways — nothing outside rises or falls in this shot. The lanyard
swings only sideways and stays taut — it never floats, never goes slack,
never coils, never drifts in zero gravity. Nothing in the cabin floats. 0%
bloom, no glow filter, no soft focus. No readable text, letters, digits,
numbers, icons or screen graphics. No holograms. No subtitles, no dialogue
text, no title card, no watermark. Photorealistic with 35mm film grain.
```

---

## 🎬 SAHNE 12 (S12) — PART A KAPANIŞ: YUVA GÖRÜNÜR

> 🎯 **REFERANS:** **RB** p4 → p1 (yuva ilk kez görünür — duruş + kollar açık) · **RA** p4 (küreler + omurga) · **RC** p1

### 📸 IMAGE PROMPT

```
Photorealistic cinematic still image, 16:9 widescreen, 4K. Deep space, 90
metres off the flank of an interstellar ship. Exactly 2 human figures exist
in this film and both are sealed inside the small capsule — no figure is
visible in frame.

SCENE: The ship's flank runs up the right half of the frame — open
hexagonal graphite truss spine with bolted nodes, and above it four polished bright-metal 9-metre propellant spheres in a row. Standing out from the flank
near the top of frame: a 12-metre lattice berth boom, square in section,
carrying a flat structural pad at its outer end. Set into the UNDERSIDE of
that pad and facing straight down: a 2.0-metre machined capture ring with a
40-centimetre conical throat and THREE curved capture arms standing fully
open at 120-degree spacing, ringed by a continuous recessed warm-white
light channel that lays a clean pool of 3400K light on the open arms — the
first warm light anywhere in this film. In the lower left third of frame,
56 metres below the boom and 46 metres out from the hull: the ferry capsule
— a 5.2-metre truncated cone standing nose-UP, matte ceramic-white composite over a dark graphite frame with a sweeping TURQUOISE chevron stripe,
its 60-centimetre probe pointing at the TOP of frame, forty white core
tubes under a BURNT-ORANGE strap, a six-socket cartridge rack with FOUR
sockets empty and scorched.

ENVIRONMENT: Hard vacuum, absolute black sky, sharp stars, 0.220 g of
thrust acceleration.

CAMERA & LIGHT: 24mm spherical lens, fixed 90 metres out. Hard parallel
starlight from screen-left; the berth's warm-white channel is a small
distant pool at the top of frame; a weak blue rim from the exhaust far
below the bottom edge.

NEGATIVE: Fixed locked-off camera, single frame. No figure visible
anywhere. Exactly THREE capture arms, all open; exactly FOUR propellant
spheres; exactly SIX cartridge sockets with FOUR empty; exactly FORTY core
tubes. The light channel is a thin recessed line, not a lamp and not a
halo. 0% bloom, no glow filter, no lens flare, no soft focus. No readable
text, letters, digits, numbers, insignia or watermark. No subtitles, no
title card. No atmospheric haze. Photorealistic with 35mm film grain.
```

### 🎥 VIDEO PROMPT

```
10-second single unbroken shot, 16:9 widescreen, photorealistic. Fixed
locked-off camera 90 metres off the flank of an interstellar ship in
vacuum, no camera movement. Exactly 2 human figures exist in this film and
both are sealed inside the small capsule — no figure is visible in frame.

SCENE: The ship's flank runs up the right half of frame — open hexagonal
graphite truss spine with bolted nodes, and above it four polished bright-metal 9-metre propellant spheres in a row. Standing out from the flank near the
top of frame: a 12-metre lattice berth boom carrying a flat structural pad
at its outer end, with a 2.0-metre machined capture ring set into the
UNDERSIDE of that pad facing straight down, a 40-centimetre conical throat
at its centre, THREE curved capture arms standing fully open at 120-degree
spacing, and a continuous recessed warm-white light channel around its rim
laying a clean pool of 3400K light on the open arms. In the lower left
third of frame, 56 metres below the boom and 46 metres out from the hull:
the ferry capsule, a 5.2-metre truncated cone standing nose-UP, its
60-centimetre probe pointing at the TOP of frame, forty white core tubes
under a BURNT-ORANGE strap, a cartridge rack with FOUR sockets empty.

TIMELINE:
0.0s — Nothing moves. The capsule holds station exactly; the ship holds its
burn; the warm light pool at the top of frame is perfectly steady.
4.0s — Behind the capsule's window, two helmeted heads are just visible,
both tilted up toward the boom.
7.0s — A fleck of debris falls down the gap between the two hulls,
accelerating, and leaves the bottom of frame. Neither craft moves.
10.0s — Stillness. The distance between the capsule and the warm light does
not change by a single metre. Hold.

AUDIO: One continuous low hull-conducted engine drone, deep and steady, and
nothing else. No voice, no music.

PHYSICS: Both craft are matched at 0.220 g of thrust acceleration, so the
capsule neither rises nor falls; the 56-metre gap is exactly constant. The
falling fleck is unpowered and accelerates away at 2.16 metres per second
squared.

NEGATIVE: Single unbroken take, fixed locked-off camera — no cuts, no pans,
no zoom, no tilt. No figure visible outside the hull. Exactly THREE capture
arms and all THREE stay open in this shot — none closes, none folds.
Exactly FOUR propellant spheres, SIX cartridge sockets with FOUR empty,
FORTY core tubes. The capsule does not rise or fall in this shot and never
pitches, rolls or drifts. The light channel is a thin recessed line — not a
lamp, not a halo, never glowing. The falling fleck accelerates continuously
downward and never hovers or freezes. 0% bloom, no glow filter, no lens
flare, no soft focus. No readable text, letters, digits, numbers, insignia
or watermark. No subtitles, no title card. Photorealistic with 35mm film
grain.
```

---

# 📋 PART A ÖZET TABLOSU

| # | Sahne | Lens | İç/Dış | Konum | Kartuş | Kilit olay |
|---|---|---|---|---|---|---|
| S0 | HOOK: GEÇİT | 24mm | dış | 118 m | 6 | kırağı düşer — aşağısı var |
| S1 | PENCEREDEN YUKARI | 35mm | iç | 118 m | 6 | iki insan, kordon, mavi ışık |
| S2 | KIRK KAROT | 50mm | dış | 118 m | 6 | yük tanıtılır (bedelin nesnesi) |
| S3 | İLK KARTUŞ | 35mm | iç | 118 m | 6→5 | mekanizma ifşası + ilk kovan |
| S4 | 🎬 VİRAL #1: ALEV | 24mm | dış | 114 m | 5 | ölçek şoku, 400 m mızrak |
| S5 | MAVİ ALTTAN | 85mm | iç | 100 m | 5 | pilot yüzü, alttan mavi |
| S6 | TUTMA | 50mm | dış | 84 m | 5→4 | ters kartuş, tırmanış 1 biter |
| S7 | KANAT | 24mm | dış | 78 m | 4 | engel tanıtılır |
| S8 | İKİNCİ TIRMANIŞ | 35mm | iç | 78 m | 4→3 | üçüncü kartuş |
| S9 | YAKLAŞAN AĞIZ | 50mm | iç | 74 m | 3 | iki yüz, tek bakışma; kovan camdan düşer |
| S10 | 🎬 VİRAL #2: ERKEN TUTMA | 50mm | dış | 60 m | 3→2 | kanat ucu 6 m, hesap bozulur |
| S11 | YANA KAYMA | 35mm | iç | 56 m | 2 | yanal öteleme, kordon yana |
| S12 | 🔑 YUVA GÖRÜNÜR | 24mm | dış | 56 m | 2 | hedef ilk kez ekranda |

**PART A: 13 sahne · 0:00–2:09 · 0 replik · 0 kesme · 13/13 sabit lockoff**

---

## 🚪 KAPI KAYITLARI [D74] — her koşu TEK SATIR

> ⛔ Kaydı olmayan kapı, koşulmamış kapıdır. Üretim yapan kişi buraya yazar.

```
| kapı | tarih | deneme | sonuç | karar |
|------|-------|--------|-------|-------|
| KAPI 0 — referans paketi (5 sayfa × 4 panel) |  |  |  |  |
| KAPI 1 — S19 yük atma                |  |  |  |  |
| KAPI 2 — S21 temas                   |  |  |  |  |
| KAPI 3 — S4 alev                     |  |  |  |  |
| KAPI 4 — S1 kabin / iki insan        |  |  |  |  |
| prompt_kontrol.py PART_A             |  |  |  |  |
```

---

## ➡️ DEVAM

**PART B:** `THE_UPHILL_DARK_PART_B.md` — S13-S24 (12 sahne, 2:09–4:09)
**Referans:** `THE_UPHILL_DARK_REFERANS_PAKETI.md`
**Plan:** `THE_UPHILL_DARK_PLAN.md`
