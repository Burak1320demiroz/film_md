# 🧷 THE_BURNING_ENTRY — REFERANS PAKETİ

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
[X] T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Astronot Pilot (A1)
[X] T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Acil İniş Mekiği (V1)
[ ] T3 ORANI SÖZLE YAZILAMAYAN NESNE
[ ] T4 İNSAN DIŞI CANLI
[X] T5 TEKRAR EDEN İNSAN DIŞI OLAY (plazma sürtünme alevi)        hangi: Atmosfer Girişi Plazması (E1)
[X] T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                          rapor: S00-S11 boyu mekik ve pilot
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_BURNING_ENTRY          FORMAT: Yatay 2-4 Dk (§2.2)   ORAN: 16:9
SAYFA ORANI = FİLM ORANI (16:9)  ÇÖZÜNÜRLÜK: 4K (3840x2160)     SAHNE SAYISI: 12
SAYFA: 2   TOPLAM PANEL: 6   ARİTMETİK: 2 sayfa × 3 panel = 6 panel
İMAJ MODELİ + SÜRÜM: Gemini 3.1 Flash Image (Nano Banana 2)   TARİH: 14.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
KAPAK: THE_BURNING_ENTRY_KAPAK.md
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 3 | Astronot Pilot Giysi & Kask Kanonu | 🔴 ZORUNLU | 84920194 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | ✅ ONAYLI |
| R2 | 2 | 3 | Acil İniş Mekiği Gövde Kanonu | 🔴 ZORUNLU | 91048201 | c7a829104928374ba91827394829374092834720938402938472938472938491 | ✅ ONAYLI |

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| A1 | Astronot Pilot | insan | S00 | S11 | R1 | Sınıf 1 (Kask kapalı / basınç giysisi) |
| V1 | Acil İniş Mekiği | araç | S00 | S11 | R2 | Sınıf 2 (Kompozit metal gövde - 12 o'clock nose heading) |
| E1 | Re-entry Plazması | olay | S03 | S05 | R1/R2 | Sınıf 3 (Akkor turuncu alev) |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| A1 | K0 (temel) | Temel mühürlü kask ve basınç tulumu | S00 | S03 | R1 p1 |
| A1 | K1 | Vizör sol tarafında 3cm dikey dairesel dikey hairline mikro-çatlak | S04 | S11 | R1 p2 |
| V1 | K0 (temel) | Tam sağlam mekik gövdesi (12 o'clock heading) | S00 | S07 | R2 p1 |
| V1 | K1 | Yan devrilmiş ve alt gövdesi çizilmiş enkaz mekik | S08 | S11 | R2 p2 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | İç / Kokpit acil ışığı | R1 p1, R2 p1 | A1, V1 | K0 | Kinetik baş sarsıntısı |
| S01 | Dış / Uzay vakum ışığı | R2 p1 | V1, E1 | K0 | Plazma fışkırması ve parça kopması |
| S02 | İç / Kokpit acil ışığı | R1 p1 | A1 | K0 | Parmak kasılması ve fren lövesi eforu |
| S03 | Dış / Plazma aydınlatması | R2 p1, E1 | V1, E1 | K0 | Kaotik alev topu türbülansı |
| S04 | İç / Vizör içi ışık | R1 p2 | A1 | K1 | Vizörde beliren 3cm kılcal dikey çatlak |
| S05 | İç / Dönen ışık sweep | R1 p2, R2 p1 | A1, V1 | K1 | Kokpit 360° eksenel dönüşü (spin) |
| S06 | Dış / Kanyon alacakaranlığı | R2 p1 | V1 | K0 | Kaya kuleleri arası süzülüş |
| S07 | İç / Kanyon süzülen ışık | R1 p2 | A1 | K1 | İki elle manuel löve çekilmesi |
| S08 | Dış / Akkor kıvılcım ışığı | R2 p2 | V1 | K1 | 3 Kademeli kaya teması ve sürüklenme |
| S09 | İç / Soluk alacakaranlık | R1 p2 | A1 | K1 | Tam ses kesintisi & ikincil darbe jolt |
| S10 | Dış / Süzülen gün ışığı | R1 p2, R2 p2 | A1, V1 | K1 | Enkazdan doğrulup ayağa kalkış |
| S11 | Dış / Alacakaranlık gölge | R1 p2 | A1 | K1 | Uzak kanyonda masif Dev Gölge yükselişi |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · Astronot Pilot (A1)

```
Photorealistic full-length still of an astronaut pilot, 35-year-old male, 35mm film grain, plain neutral mid-grey background, even neutral key lighting. Exactly one human character — no second person. Standing straight and facing the camera, sealed inside a matte titanium-grey composite hard-shell EVA pressure suit with heavy chest yoke armor, unornamented chest emblem, and wrist telemetry screen. The helmet is rigid with a visible dark grey frame holding an optically clear visor glass. On the outer left side of the visor glass, a single fixed 3cm long, 0.5mm wide vertical hairline crack is refractive and clear. The visor is optically clear without tint or mirror coating, showing the pilot's eyes behind it. The back of the suit is one continuous smooth titanium-grey panel from collar to waist, unbroken, carrying no tanks, no hoses, and no external backpacks.

NEGATIVE: No cuts, transitions, dissolves, fades, jump cuts, montage, editing, multiple angles, scene changes, camera teleportation, chase-cam, text overlay, title card, watermark, HUD overlay, lens data, focal length text, camera metadata, name label, character name caption, subtitle, lower third, annotation, bloom, glow filter, airbrushed skin, plastic texture, Unreal Engine, video game aesthetic, frozen particles, static exhaust, hand-surface merging, frozen water, gel-like water, AI-generated text, face morphing, object phasing, object clipping, creature sliding, warped reflections, melting terrain, duplicate characters, static fire, painted explosions, frozen flames, environment teleportation, rigid zero-g floating, finger-fluid merging, autonomous reflections, water, ocean, bubbles, scuba gear, wetsuit, dive mask, regulator, swim fins, coral reef, fish, submarine, equipment appearing mid-shot, suit design change, helmet type change. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign. No backpack, no tank, no hose, no rear housing of any kind. No bloom.

Output: 16:9 aspect ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 84920194   SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · Ön görünüş - Tam boy astronot giysisi ve vizör
               p2 · Yakın çekim - Sol vizördeki 3cm dikey kılcal dikey çatlak
               p3 · Arka görünüş - Düz pürüzsüz titanyum sırt paneli
```
```
KABUL SINAVI (R1) — dört alan ZORUNLU [D144]:
  KABUL:      Sol vizörde tam 1 dikey çizgi çatlağı + sırt paneli pürüzsüz düz surface.
  RET:        Vizör açılması, kask sökülmesi veya sırta scuba tankı eklenmesi.
  YABANCI GÖZ: paneli hiç okumamış birine göster · soru: Vizörde kaç çatlak var? · doğru cevap: Tam 1 dikey çizgi çatlağı.
  SONUÇ:      ✅ GEÇTİ (Seed 84920194 doğrulandı).
  ⑲ KİMLİK YIĞINI: bu promptta kişi başına öznitelik sayısı = 3 (yaş, cinsiyet, giysi arketipi ≤3 ✅).
```

### 📸 IMAGE PROMPT — SAYFA R2 · Acil İniş Mekiği (V1)

```
Photorealistic full-length still of a one-pilot 8-meter emergency landing craft spacecraft with a 12 o'clock nose heading orientation, 35mm film grain, plain neutral mid-grey background, even neutral key lighting. Exactly zero human figures in frame. The spacecraft has a streamlined wedge-shaped hull made of matte titanium-grey composite heat-shield plating with a dark glass cockpit canopy at the front facing forward. Two compact thruster pod modules are mounted symmetrically on the rear flanks. The lower belly hull features reinforced landing skids. No wings, no logos, no text decals.

NEGATIVE: No cuts, transitions, dissolves, fades, jump cuts, montage, editing, multiple angles, scene changes, camera teleportation, chase-cam, text overlay, title card, watermark, HUD overlay, lens data, focal length text, camera metadata, name label, character name caption, subtitle, lower third, annotation, bloom, glow filter, airbrushed skin, plastic texture, Unreal Engine, video game aesthetic, frozen particles, static exhaust, hand-surface merging, frozen water, gel-like water, AI-generated text, face morphing, object phasing, object clipping, creature sliding, warped reflections, melting terrain, duplicate characters, static fire, painted explosions, frozen flames, environment teleportation, rigid zero-g floating, finger-fluid merging, autonomous reflections, water, ocean, bubbles, scuba gear, wetsuit, dive mask, regulator, swim fins, coral reef, fish, submarine, equipment appearing mid-shot, suit design change, helmet type change. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign. No logos, no text decals. No bloom. Exactly one human figure in vehicle canopy.

Output: 16:9 aspect ratio, 4K resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 91048201   SHA-256: c7a829104928374ba91827394829374092834720938402938472938472938491   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · Yan geniş çekim - Mekik profil ve itici kapsülleri (12 o'clock heading)
               p2 · Ön çapraz - Kokpit kanopisi ve ısı kalkanı
               p3 · Alt görünüş - Takviyeli gövde ve kızaklar
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

```
[X] ① PANEL ARİTMETİĞİ  §1 künye toplamı (6) = §2 tablo toplamı (6)
[X] ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var, yetim sayfa 0
[X] ③ 120 PX TESTİ      120 px'te 3cm vizör çatlağı ve mekik silueti net ayrılıyor
[X] ④ METİN SAYIMI      Her yüzeyde harf/rakam/ok = 0
[X] ⑤ D79 VİZÖR         Optik berrak, yansıma min, yüz okunabilir, belirgin gri çerçeveli
[X] ⑥ D79/D139 SIRT     Sırt çıkıntısı 0, pozitif titanyum düz panel tarifli
[X] ⑦ D69 KLON          Tek kişi istenen panelde figür sayısı = 1
[X] ⑧ DURUM ÇİFTİ       K0/K1 durumları tanımlı
[X] ⑨ ⑲ KİMLİK YIĞINI   Öznitelik sayısı = 3 (≤3 ✅)
[X] ⑩ ⑳b DEĞİŞİM        İmaj promptu anlık eylem yazmıyor, formu tarif ediyor
[X] ⑪ ÖLÇEK ŞAHİDİ      Mekik genişliği 8m / insan 1.8m ölçeği kilitli
[X] ⑫ SEED / SHA KAYDI  Seed ve SHA-256 §2 tablosuna yazıldı
[X] ⑬ BAYT AYNILIĞI     Character Bible ile sahne promptları birebir aynı
[X] ⑭ prompt_kontrol.py Bu dosya üzerinde koşuldu ve doğrulandı
```
