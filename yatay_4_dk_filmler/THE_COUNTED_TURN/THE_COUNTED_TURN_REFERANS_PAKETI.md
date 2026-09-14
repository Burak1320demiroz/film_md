# 🧷 THE_COUNTED_TURN — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` · giysi kimliği `ASTRONOT_DONANIM` ·
ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK S22 → merkezî seçim S20 → kapanış S24 →
> S0 → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Karşı kayıt:
> THE SINKING STAKE'in referans paketi HİÇ ÜRETİLMEDİ → çapa yok → göğüs paketi
> tasarımı S13'te değişti.
> ⛔ **İngilizce prompt, başlıktan sonraki İLK çitli bloktur.** Künye ve kabul
> sınavı promptun ALTINA yazılır.

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı
```
[x] T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)  kim: tek rigger, 25/25 sahne
[x] T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]             hangi: pim + klips birimi
    emsal: THE LEANING ROOM'da "düz pirinç el çarkı" arketipine çöktü [D128]
[x] T3 ORANI SÖZLE YAZILAMAYAN NESNE                             hangi: halkanın içbükey güvertesi
    önü ve arkası yukarı kıvrılıp başın üstünde kapanıyor; bu oran cümleyle tutulmaz
[ ] T4 İNSAN DIŞI CANLI                                          yok
[x] T5 TEKRAR EDEN İNSAN DIŞI OLAY                               hangi: bırakılan cismin yana inişi · bandın sarkması
[x] T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                          hangi: halkanın kendisi
→ ALTI tetikleyicinin BEŞİ doğru. Paket YAZILIR ve KAPI 0'dır.
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_COUNTED_TURN          FORMAT: yatay 3-5 dk       ORAN: 16:9
ÇÖZÜNÜRLÜK: 4K                  SAHNE SAYISI: 25
SAYFA: 4   TOPLAM PANEL: 14   ARİTMETİK: RA 4 + RB 4 + RC 3 + RD 3 = 14
İMAJ MODELİ + SÜRÜM: ⬜ (üretim günü yazılır)   TARİH: ⬜.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → THE_COUNTED_TURN_KAPAK.md (RA onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| RA | karakter · giysi · vizör | 4 | tek rigger, kapalı vizör, düz sırt, kalça sırası | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| RB | pim + klips birimi | 4 | pim geometrisi · klips açık/kapalı · banda kilitli hâli | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
| RC | dokuma bant + makara | 3 | gergin/gevşek/kesit · makara ve yuva | 🟠 S7'den önce | ⬜ | ⬜ | ⬜ TASLAK |
| RD | halka kesiti · kaburga gözü | 3 | içbükey güverte · üst güverte · ölçek şahidi | 🔴 ZORUNLU | ⬜ | ⬜ | ⬜ TASLAK |
```
🔴 üretim başlamadan · 🟠 belirli sahneden önce · ⏳ ertelenebilir
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı) → GEÇERSİZ
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
⚙️ SEED: Flow arayüzünde alanın VAR OLDUĞU önce sınanır [D142]; yoksa bu
   sütun "arayüzde yok" yazar ve kapı SHA-256 sütununa devreder.
⚙️ SHA-256: shasum -a 256 <panel.png>
```

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| V1 | rigger (tek insan) | insan | S0 | S23 | RA | 🔴 yüksek — kimlik + vizör + sırt |
| V2 | pim | prop (tekrar eden birim) | S0 | S24 | RB | 🟠 orta — arketipe yuvarlanma [D128] |
| V3 | klips | prop (sayılabilir) | S3 | S24 | RB | 🟠 orta — biçim + sayı |
| V4 | dokuma bant | prop | S1 | S24 | RC | 🟠 orta — fabric/cloth tuzağı [D153] |
| V5 | makara + yuva | prop | S7 | S13 | RC | 🟡 düşük |
| V6 | halka iç güvertesi | mekân | S0 | S24 | RD | 🔴 yüksek — oran + üst güverte |
| V7 | kaburga gözü + yıldız alanı | mekân | S1 | S20 | RD | 🟠 orta — yıldız izi riski |
| V8 | cıvata yığını | prop (sayaç) | S0 | S24 | RB p4 | 🟡 düşük |
```
⛔ KOD kullanılır, AD kullanılmaz [D34].
⛔ Envanterde olup sayfası olmayan varlık yok; yetim sayfa yok.
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| V3 klips | K0 açık | — | S3 | — | RB p2 |
| V3 klips | K1 kapalı | jaw kapandı, bandı pime kilitledi | S3 | S3 | RB p3 |
| V3 klips | K2 açık kalmış | aynı klips, jaw AÇIK, bant pimden kalkmış | — | S24 | RB p2 kırpım |
| V1 kalça sırası | K0 dolu (12) | — | S0 | — | RA p1 |
| V1 kalça sırası | K1 yarı (6) | klips sayısı azaldı | S15 | S15 | RA p1 kırpım |
| V1 kalça sırası | K2 boş (0) | çıplak ray kaldı | S21 | S21 | RA p2 kırpım |
| V4 bant | K0 sığ sarkma | — | S2 | — | RC p2 |
| V4 bant | K1 derin sarkma | aynı açıklık, sarkma pimin gölgesini geçti | S14 | S16 | RC p2 kırpım |
```
⛔ MERDİVEN TEK YÖNLÜDÜR. Klipsin K1→K2 dönüşü (kapalı → açık) TEK istisnadır
   ve gerekçesi filmin twist'idir: klips açılmadı, AÇILMIŞ BULUNDU — açılma anı
   HİÇBİR karede gösterilmez [ara durum yasağı · T2V-CompBench 0,0687].
⛔ DURUM ÇİFTİ aynı kadraj · aynı ışık yönü · aynı mesafe, TEK FARK.
   Bu dosyanın seçimi: aynı panelde iki durum GÖSTERİLMEZ; her durum ayrı
   kırpımdır. Gerekçe: kılavuz §3 ② aynı sayfada iki durumu ölçülmemiş
   çelişki sayıyor.
```

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | ışık fazı | yüklenecek KIRPIM | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S0 | eksenel, sabit | RB p1 + RB p4 | pim boş, cıvatalar dikişte | V3 yok | cıvatanın yana inişi ve süresi |
| S1 S4 S10 S20 | eksenel, sabit | RA p1 + RD p1 | tam boy, güverte | V1 K0 | adımın ağırlığı ve iniş anı |
| S2 S5 S14 S16 | eksenel, sabit | RC p2 + RB p1 | gergin açıklık ve sarkma | V4 K0/K1 | sarkma derinliği (SPEC'ten) |
| S3 S15 S17 S22 | eksenel, sabit | RB p2 + RB p3 | klips açık ve kapalı | V3 K0/K1 | kapanma hareketi, tek beat |
| S6 | eksenel, sabit | RD p2 | kaburga gözü, yıldız alanı | — | süpürme süresi |
| S7 | eksenel, sabit | RC p3 + RD p1 | makara ve yuva | V5 K0 | yuvadan ayrılma ve durdurma |
| S8 S9 S18 S19 S21 | eksenel, sabit | RA p4 + RC p1 | eldiven makrosu, bant | V1 K0/K1/K2 | eldiven yüzeyindeki zorlanma |
| S11 S13 | eksenel, sabit | RD p3 | üst güverte, kapanan halka | V6 | kaş kaldırma, hareketsizlik |
| S12 | eksenel, sabit | RA p3 | sırt, düz siluet | V1 | ağırlık kaydırma |
| S23 S24 | eksenel, sabit | RB p1 + RB p2 + RB p4 | pim, iki klips, yığın | V3 K1+K2 | düşüş süresi farkı |
```
⛔ Bir sahnede EN ÇOK 3 kayıt yüklenir (VEO §6 md.2) — hiçbir satır 3'ü geçmiyor.
⛔ YÜKLENEN ŞEY SAYFA DEĞİL, KIRPILMIŞ PANELDİR [kılavuz §4.3].
   Bu dosyanın seçimi: KIRPIM. Gerekçe: tam sayfa yüklemek panel aralarındaki
   nötr zemini de referansa sokuyor ve arka planı düzleştiriyor.
· Flow çağırma: @RA biçiminde — etiket KOD olur, asla özel ad [D34]. ⚙️ SINANMAMIŞ.
```

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA RA · KARAKTER · GİYSİ · VİZÖR

```
Photorealistic full-length still, 16:9, 4K, 35mm film grain, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, no bloom.

Exactly one human character — no clones, no second person. A single figure stands straight and faces the lens, sealed in a matte pale-grey pressure suit. The suit is one continuous smooth panel from collar to hip, unbroken, carrying nothing on the back — one smooth surface with a single flat vertical seam down its centre. The helmet has a flat rectangular front pane, a little wider than a spread hand and about two thirds as tall, set in a visible brushed metal rim; the glass is optically clear with zero tint, zero mirror coating and zero reflection of the environment, and the face is fully readable through it at every head angle. The gloves are the same matte pale grey with raised knuckle ridges and a stitched cuff seam at the wrist. A short row of anodised orange clips rides flat on the right hip, each about the length of a thumb, standing up from a bare rail in a single line. Fixed wear that never moves: a scuffed patch on the left knee and a shallow dent on the right hip rail.

NEGATIVE: Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. The suit has no back-mounted unit of any kind: no backpack, no tank, no hose, no rear housing. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek, duruş, DOLU kalça sırası
               p2 · profil — siluet hattı ve kalça sırasının siluetteki yeri
               p3 · SIRT — düz, kesintisiz panel [D79/D139]
               p4 · eldivenler ve manşet dikişi, makro [D175]
⛔ "seamless visor" YAZILMAZ: çerçevesizlik kubbe davetiyesidir [D146].
⛔ ARKA PANELDE yokluk listesi TUTMAZ — panelin işi sırta ne KOYACAĞINI
   söylemektir: tek düz dikey dikişli sürekli yüzey [D123 · D139].
⛔ VİZÖR ÖLÇÜSÜ (24 x 16 cm) YALNIZ burada ve SPEC kilit listesinde yaşar;
   prompt gövdesinde nesne-göreli yazılır [D138].
```
```
KABUL SINAVI (RA) — dört alan ZORUNLU [D144]:
  KABUL:      kalça sırasındaki klipsler p1 ve p2'de TEK TEK sayılabiliyor (12)
              ve sırt panelinde çıkıntı sayısı 0
  RET:        vizörde renk, ayna ya da çevre yansıması · kubbe/çerçevesiz kask ·
              sırtta herhangi bir kutu, tüp, hortum
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: "sırtında ne var?" ·
              doğru cevap: "hiçbir şey"
  SONUÇ:      ⬜ (geçmezse sayfa yeniden üretilir · hiçbir sahne üretilmez)
  ⑲ KİMLİK YIĞINI: kişi başına öznitelik sayısı = 0
     ⭐ Bilinçli: boy · ten · saç · yaş · yüz işareti HİÇBİRİ yazılmadı.
       Kimlik SEED ile taşınır. Gerekçe: red defteri vaka 15 — yedi öznitelik
       25 promptta tekrarlanınca sınıflandırıcı "gerçek kişi" kalıbı okudu.
```

### 📸 IMAGE PROMPT — SAYFA RB · PİM + KLİPS BİRİMİ

```
Photorealistic product-style still, 16:9, 4K, 35mm film grain, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, no bloom. No human anywhere in frame.

A single stainless steel pin, machined and unpainted, stands upright on a short section of bare machined aluminium deck with a welded seam running through it. The pin is a plain round post with a shallow groove near its top and a flat cap; it is not a hook, not a bollard, not a cleat and not a rigging eye. Beside it lies one anodised orange clip, open: a simple sprung jaw about the length of a thumb, with a flat pressing face and a single hinge. A second identical clip is shown closed over a short length of dark grey woven webbing band, gripping it against the pin. Every surface is clean and new — no rust, no grime, no paint marks.

NEGATIVE: Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. The suit has no back-mounted unit of any kind: no backpack, no tank, no hose, no rear housing. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · pim tek başına, dikişle birlikte (ölçek ve geometri)
               p2 · klips AÇIK — jaw, menteşe, basma yüzü
               p3 · klips KAPALI, bandı pime kilitlemiş
               p4 · dikişte yatan cıvatalar (sayaç nesnesi)
⛔ D128 tuzağı: "pin" ve "clip" arketipe yuvarlanır (kanca · babafingo · karabina).
   Prompt ne OLMADIĞINI da sayar: not a hook, not a bollard, not a cleat,
   not a rigging eye — bu biçimi TARİF eden bir cümledir, yasak listesi değil.
```
```
KABUL SINAVI (RB) — dört alan ZORUNLU [D144]:
  KABUL:      p2 ve p3'teki klips AYNI nesne olarak okunuyor (tek menteşe,
              aynı jaw uzunluğu) ve p3'te bant pimin oluğuna oturmuş
  RET:        karabina · kanca · yaylı toka görünümü · iki menteşeli klips
  YABANCI GÖZ: soru: "bu ikisi aynı parça mı?" · doğru cevap: "evet, biri açık"
  SONUÇ:      ⬜ (geçmezse S3 · S15 · S17 · S21 · S22 · S24 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok — 0
```

### 📸 IMAGE PROMPT — SAYFA RC · DOKUMA BANT + MAKARA

```
Photorealistic product-style still, 16:9, 4K, 35mm film grain, plain neutral mid-grey seamless backdrop, even neutral key light with soft fill, no bloom. No human anywhere in frame.

A heavy dark grey woven webbing band, flat and about as wide as three fingers, is shown three ways in one frame: a length lying slack on bare machined aluminium; the same band pulled taut between two stainless pins so that it is dead straight where it leaves each pin and sags only in the middle; and one cut end showing the tight weave and a sealed edge. Beside them stands a plain cylindrical cable spool of bare machined aluminium seated in a bolted cradle, with the band wound onto it in even flat turns. The band is stiff and heavy and holds its shape; it is not cloth, not rope, not chain and not cable.

NEGATIVE: Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. The suit has no back-mounted unit of any kind: no backpack, no tank, no hose, no rear housing. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🟠 S7'den önce   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · bant gevşek, güvertede
               p2 · bant iki pim arasında GERGİN — sarkma yalnız ortada
               p3 · makara ve cıvatalı yuvası
⛔ fabric ve cloth 0 geçiş [D59 · D153]: model onları kumaş sanıp DALGALANDIRIR
   ve bu filmin fizik imzası "gergin ve düz"dür.
⛔ p2 sarkmanın KANONİK biçimidir: pimden çıkışta DÜZ, yalnız ortada eğri.
```
```
KABUL SINAVI (RC) — dört alan ZORUNLU [D144]:
  KABUL:      p2'de bant her iki pimden çıkarken DÜZ; eğri yalnız ortada
  RET:        dalgalanan/uçuşan bant · halat örgüsü · zincir · kablo kılıfı
  YABANCI GÖZ: soru: "bu neyden yapılmış?" · doğru cevap: "sert dokuma bant"
  SONUÇ:      ⬜ (geçmezse S1 · S7 · S8 · S9 · S18 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: insan yok — 0
```

### 📸 IMAGE PROMPT — SAYFA RD · HALKA KESİTİ · KABURGA GÖZÜ · ÖLÇEK ŞAHİDİ

```
Photorealistic architectural still, 16:9, 4K, 35mm film grain, hard single-source light along the ring's axis grazing the deck, no fill, black shadows, no bloom.

Exactly one human character — no clones, no second person. The inside of a ring station under construction, seen from deck level. The deck is bare machined aluminium, bright and clean, with a welded seam running along it and stainless pins standing up from the seam at even intervals. The deck curves upward on both sides of frame and closes overhead; the surface overhead is the same deck seen from underneath, and nothing is standing on it. One section of the inner skin is unplated and the bare structural ribs are open there, with the star field beyond them — individual separate points, no trails, no streaks. A single suited figure stands on the deck at mid-distance as the scale witness, small against the curve, in a matte pale-grey pressure suit with a flat rectangular helmet pane in a visible brushed metal rim and an unbroken back panel carrying nothing.

NEGATIVE: Single unbroken take, no cuts, no edits, no camera resets, no transitions, no dissolves, no fades, no jump cuts, no camera teleportation, no angle change. Exactly one human character — no duplicates, no clones, no second person. 0% bloom, no glow filter, no soft focus, no dreamy haze — every surface keeps visible texture. Photorealistic skin pores, sweat, scars and fatigue retained — no airbrushing, no plastic or waxy texture, no smoothed skin, no face morphing, identical bone structure throughout. Equipment and clothing identical to the description — no drift, no gear appearing or disappearing mid-shot. Dirt and wear staining stays fixed and never shifts. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — not on the suit, not on the equipment, and not on the deck, the rail, the pins or any surface in the frame. Nothing in this world has been measured, labelled, marked out or annotated by anyone: no scale marks, no graduation ticks, no survey markers, no engraved or painted characters of any kind. No subtitles, no captions, no burned-in dialogue text, no title card, no end card, no credits, no watermark. All hand-surface contacts keep a clear structural boundary — no merging, no phasing, no extra fingers, rigid-body collision throughout. All particles obey the stated gravity with continuous physical momentum — never hovering, never frozen, never swirling or flowing like liquid. Environment static and stable — no melting terrain, no warping topology, no swimming texture. No Unreal Engine look, no CGI aesthetic, no video game aesthetic. Photorealistic with 35mm film grain. No panel gutters, no labels, no captions, no arrows, no callouts, no dimension lines, no panel titles. The suit has no back-mounted unit of any kind: no backpack, no tank, no hose, no rear housing. No bare skin is visible anywhere: none above the collar, none at the wrist, none at the ankle. No miniature look, no tilt-shift, no scale-model appearance, no toy-like proportions.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: ⬜   SHA-256: ⬜   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · güverte düzeyinden geniş — eğri iki yandan yükseliyor
               p2 · kaburga gözü ve yıldız alanı
               p3 · alttan-yukarı — üst güverte kapanıyor, üstünde kimse yok
⛔ ÖLÇEK ŞAHİDİ zorunlu [UZAY_USSU §1]: p1 ve p3'te kasklı gövde kadrajda.
⛔ MAKET OKUMASI negatifi bu sayfada ZORUNLU: no miniature, no tilt-shift,
   no scale-model, no toy-like proportions [UZAY_USSU §6 · OPEN CIRCUIT ④].
⛔ YILDIZ ALANI tek tek noktadır — iz/çizgi 0 (THE SINKING STAKE'te sabit
   kamerada dairesel yıldız izleri üretildi ve fiziksel olarak imkânsızdı).
```
```
KABUL SINAVI (RD) — dört alan ZORUNLU [D144]:
  KABUL:      p3'te üst güverte KAPALI bir eğri olarak okunuyor ve üstünde
              hiçbir figür yok; p1'de gövde ölçek şahidi olarak ayırt ediliyor
  RET:        maket/tilt-shift görünümü · üst güvertede duran ikinci figür ·
              yıldız izi/çizgisi · ufkun bükülmesi
  YABANCI GÖZ: soru: "tavanda ne var?" · doğru cevap: "aynı güverte, boş"
  SONUÇ:      ⬜ (geçmezse S6 · S7 · S10 · S11 · S13 ÜRETİLMEZ)
  ⑲ KİMLİK YIĞINI: kişi başına öznitelik sayısı = 0
```

## 7. ✅ KABUL KAPISI — üretim başlamadan önce
```
[ ] ① PANEL ARİTMETİĞİ  künye toplamı (14) = tablo toplamı (4+4+3+3) ✅
[ ] ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var ✅ · YETİM sayfa 0 ✅
[ ] ③ 120 PX TESTİ      RA → sırtın düzlüğü · RB → klipsin açık/kapalı hâli ·
                        RC → sarkmanın ortada olması · RD → üst güvertenin kapanması
[ ] ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
[ ] ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
                        + GÖRÜNÜR ÇERÇEVE var (kubbe değil) [D95/D146]
[ ] ⑥ D79/D139 SIRT     çıkıntı 0 AMA yüzey POZİTİF tarifli ✅
[ ] ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
[ ] ⑦b GRİ TON ⚙️       ffmpeg -i <panel> -vf hue=s=0 -frames:v 1 <out>.png
                        → ayrım yalnız renge dayanıyorsa panel reddedilir.
                        ⭐ Bu filmde ayrım zaten MALZEMEDİR (mat dokuma ↔ parlak
                        işlenmiş alüminyum), renk değil — sınav yine de koşulur
[ ] ⑧ DURUM ÇİFTİ       §4'teki her çift aynı kadraj · aynı ışık yönü
[ ] ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik = 0 ✅
[ ] ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin SONRASINI yazmıyor [D179]
[ ] ⑪ ÖLÇEK ŞAHİDİ      RD p1 ve p3'te kasklı gövde kadrajda ✅
[ ] ⑫ SEED / SHA KAYDI  §2 tablosuna yazıldı mı
[ ] ⑬ BAYT AYNILIĞI ⚙️  paketteki kimlik bloğu ile sahne promptu diff temiz mi
[ ] ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: ⬜
⛔ Bu on dört madde işaretlenmeden ilk sahne ÜRETİLMEZ.
```

## 8. ⬜ BEKLİYOR
```
✅ Tetikleyici kontrolü işaretlendi (5/6)   ✅ Envanter · merdiven · eşleme yazıldı
✅ Dört sayfa bloğu yazıldı (RA · RB · RC · RD)
⬜ Kabul kapısı koşulmadı, seed ve SHA-256 boş — ÜRETİM GÜNÜ doldurulur
```
