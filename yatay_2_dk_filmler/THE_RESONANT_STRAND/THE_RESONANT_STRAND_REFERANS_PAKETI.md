# 🧷 THE_RESONANT_STRAND — REFERANS PAKETİ

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Dr. Sarah Chen
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Devasa Çan Varlık
□ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: —
☑ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4 — zaten ZORUNLU)       hangi: Devasa Çan Varlık (1000m)
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY (toz · kırağı · gaz sütunu)    hangi: —
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                           kim: Sarah Chen & Devasa Varlık
```

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: THE_RESONANT_STRAND          FORMAT: yatay_2_dk_filmler        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 3840x2160 (4K Widescreen)    SAHNE SAYISI: 14
SAYFA: 2   TOPLAM PANEL: 4   ARİTMETİK: 2 sayfa × 2 panel = 4
İMAJ MODELİ + SÜRÜM: Veo 3.1 / Image Gen V2         TARİH: 11.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R01 | Page 1 | Panel 1 | Dr. Sarah Chen EVA Giysisi | 🔴 ZORUNLU | 88472910 | a7f8d... | ✅ ONAYLI |
| R01 | Page 1 | Panel 2 | Yüzey Araştırma Podu & Sensör Mastı | 🔴 ZORUNLU | 88472911 | b3c9e... | ✅ ONAYLI |
| R02 | Page 2 | Panel 1 | Devasa Çan Uzaylı Varlık (1000m) | 🔴 ZORUNLU | 99201482 | c4d1a... | ✅ ONAYLI |
| R02 | Page 2 | Panel 2 | 3 Adet 300m Şerit Yüzgeç Detayı | 🔴 ZORUNLU | 99201483 | e5f2b... | ✅ ONAYLI |

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| VAR-01 | Dr. Sarah Chen | insan | S01 | S12 | R01 | A (Düşük Risk) |
| VAR-02 | Devasa Çan Varlık | canlı | S06 | S11 | R02 | B (Orta Risk) |
| VAR-03 | Araştırma Podu | mekan/araç | S01 | S12 | R01 | A (Düşük Risk) |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| VAR-01 | K0 (temel) | EVA Giysisi, Tether Takılı | S01 | — | R01 p1 |
| VAR-01 | K1 | Tether Sökülü, Rezonans Serbest Süzülüş | S12 | S12 | R01 p1 |
| VAR-02 | K0 (temel) | Bulut Katmanında Gölge | S06 | — | R02 p1 |
| VAR-02 | K1 | Tam Açık Görünüm (1000m Çan + 3 Yüzgeç) | S09 | S09 | R02 p1 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | Dış / Ochre Işık | R01 p2 | Metal Folyo | K0 | Dikey lamine havalanma hareketi |
| S01-S05 | Dış / Ochre Işık | R01 p1 + R01 p2 | Dr. Sarah Chen & Pod | K0 | Telemetri göstergesi bipleri |
| S06-S11 | Dış / Biyolüminesans | R02 p1 + R02 p2 | Devasa Çan Varlık | K0/K1 | Yarı saydam zar dalgası hareketi |
| S12 | Dış / Ochre Zirve | R01 p1 | Sarah Chen Tether Söküm | K1 | Hands unlatching carabiner action |
| S13 | Dış / Ochre Işık | R01 p2 | Titreyen Levha (Match Cut) | K0 | Döngüsel pulse kesmesi |

---

## 📸 REFERANS İMAJ PROMPTLARI

### 📸 IMAGE PROMPT 1 — Dr. Sarah Chen EVA Suit Reference (R01 p1)
```
Full length cinematic character reference sheet of female astronaut Dr. Sarah Chen standing on dry ochre mineral ground of an alien exoplanet canyon. She wears a dark grey heavy EVA pressure suit constructed from composite panels with clean white thermal trim lines along seams. Twin metal harness telemetry clips are on her chest harness, and a fabric left shoulder role stripe displays her rank. Her suit features a wrist telemetry band illuminated with green data graphics. She wears a heavy EVA helmet with a sealed gold-reflective visor, optically clear zero tint, zero face skin visible. Internal green suit LED lighting softly illuminates the interior frame of her helmet. The back silhouette is flat, carrying no back-mounted units, no backpacks, no oxygen tanks mounted on back. Ground is dry ochre soil with hygroscopic dust and mineral pebbles. Volumetric ochre daylight streams from top-left at 30-degree elevation angle. Facing screen-right toward canyon mouth.

COMPOSITION: Centered full-body standing character reference shot with 35mm focal length lens at eye level 0 degrees.

NEGATIVE: No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign. No human faces visible through visor, no exposed skin, no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle, no bare hair, no humanoid alien anatomy, no alien eyes, no alien mouth, no tentacles, 0% bloom, no bloom, zero bloom, no glow, no lens flare, no readable text, no letters, no digits, no numbers, no symbols, photorealistic, film grain, no studio lighting, no CGI artifacts, no miniature models, no tilt-shift lens, no blur, no low resolution, no watermark, single person, exactly one human, human count = 1, one person only, no extra people, no backpacks, no back-mounted units, flat back, back silhouette is flat, no oxygen tanks mounted on back.

Output: 16:9 aspect ratio, 3840x2160 resolution, no text, no watermark.
```

### 📸 IMAGE PROMPT 2 — Colossal Bell Organism Reference (R02 p1)
```
Cinematic wide angle reference sheet of a colossal 1000-meter wide alien organism hovering peacefully in an ochre alien exoplanet sky. The organism possesses a smooth featureless translucent silicate bell mantle with a glass-like crystalline surface texture that refracts ambient ochre daylight. Internal cyan and golden light pulses ripple through its crystalline mantle in a slow rhythmic breath cycle. The organism is completely alien in structure, featuring zero eyes, zero face, zero mouth, zero tentacles, and zero humanoid limbs or organs. Three long 300-meter ribbon-like membrane fins trail beneath the bell mantle, swaying gracefully in the thick exoplanet atmosphere. The scene is illuminated by soft volumetric ochre daylight from top-left at 30 degrees elevation, casting gentle atmospheric shadows across distant ochre canyon walls below. The scale is vast, with the bottom of the canyon floor showing small rock formations for scale reference. Facing screen-right toward the canyon mouth.

COMPOSITION: Low-angle 20-degree wide composition capturing the full width of the 1000-meter silicate bell mantle against the ochre sky.

NEGATIVE: No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign. No human faces visible through visor, no exposed skin, no bare skin above the collar, no bare skin at the wrist, no bare skin at the ankle, no bare hair, no humanoid alien anatomy, no alien eyes, no alien mouth, no tentacles, 0% bloom, no bloom, zero bloom, no glow, no lens flare, no readable text, no letters, no digits, no numbers, no symbols, photorealistic, film grain, no studio lighting, no CGI artifacts, no miniature models, no tilt-shift lens, no blur, no low resolution, no watermark, single person, exactly one human, human count = 1, one person only, no extra people, no backpacks, no back-mounted units, flat back, back silhouette is flat, no oxygen tanks mounted on back.

Output: 16:9 aspect ratio, 3840x2160 resolution, no text, no watermark.
```

---

## 🔒 ONAY KAPI KAPAMASI

✅ **Referans Paketi onaylanmış ve kilitlenmiştir.**
