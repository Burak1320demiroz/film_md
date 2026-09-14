# 🧷 THE_GRAVITY_ANCHOR — REFERANS PAKETİ

## 0. 🚦 TETİKLEYİCİ KONTROLÜ

```
[x] T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Selin
[x] T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Fin
[x] T4 İNSAN DIŞI CANLI (UZAYLI_VARLIK §4)                        hangi: Fin
[x] T5 TEKRAR EDEN İNSAN DIŞI OLAY (gravite bükülmesi · cam hat)   hangi: Camlaşmış silikat hat
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_GRAVITY_ANCHOR          FORMAT: yatay 2-4m        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 3840x2160    SAHNE SAYISI: 10
SAYFA: 4   TOPLAM PANEL: 12   ARİTMETİK: 4 sayfa × 3 panel = 12
İMAJ MODELİ + SÜRÜM: Imagen 3 / Midjourney v6   TARİH: 10.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 3 | Selin Astronot Giysisi & Kask | 🔴 ZORUNLU | 4829103 | 9a8f... | 🟢 ONAYLI |
| R2 | 2 | 3 | Fin (Monolith Gravite Varlığı) | 🔴 ZORUNLU | 7193012 | 3c1e... | 🟢 ONAYLI |
| R3 | 3 | 3 | Obsidian-7 Gezegen Zemin & Çift Gölge | 🟠 S0'dan önce | 1049281 | 7b2d... | 🟢 ONAYLI |
| R4 | 4 | 3 | Camlaşmış Silikat Hat (Metastable Track) | 🟠 S8'den önce | 5509281 | 1e4f... | 🟢 ONAYLI |

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| C01 | Dr. Selin Vural | insan | S0 | S9 | R1 | Düşük (Kask içi ışık kilitli) |
| E01 | Obsidian-7 Volkanik Basalt | mekân | S0 | S9 | R3 | Düşük |
| A01 | Fin (Monolith Varlık) | canlı | S0 | S9 | R2 | Yüksek (D146 biçim kilidi) |
| E02 | Camlaşmış Silikat Hat | olay | S8 | S9 | R4 | Orta |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| A01 | K0 (Yatay Taban) | 200m sırt zemine yatay hizalı | S0 (0.0s) | — | R2 p1 |
| A01 | K1 (Dikey Yapı) | 80m maksimum dikey yüksekliğe ulaşmış dik duruş | S0 (2.2s) | S0 (2.2s) | R2 p2 |
| A01 | K2 (Optik Dalga) | Yüzeyinde ritmik prizmatik ışık dalgası kayan durum | S2 | S2 | R2 p3 |
| C01 | K0 (Polarize Kask) | Kask vizörü koyu polarize filtreli | S0 | — | R1 p1 |
| C01 | K1 (Şeffaf Kask) | Polarize filtre kapatılmış, şeffaf cam vizör arkasında yüz net | S7 | S7 | R1 p3 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S0 | Dış · Bakır/Gül Çift Işık | R1 p1 (Selin), R2 p1 (Fin K0) | Geniş | K0 ➔ K1 | Sırt yükselme hareketi + 2mm taş kalkması |
| S1 | Dış · Bakır/Gül Çift Işık | R1 p1 (Selin) | CU | K0 | Sağ el kılıf kilitleme kinesigi |
| S2 | Dış · Bakır/Gül Çift Işık | R2 p3 (Fin K2) | Wide | K2 | Dikey prizmatik ışık dalgası ritmi |
| S3 | Dış · Bakır/Gül Çift Işık | R1 p1 (Selin) | OTS | K0 | Wrist display dairesel frekans grafiği |
| S4 | Dış · Bakır/Gül Çift Işık | R3 p1 (Zemin) | Macro | K0 | Bot çevresi 10cm süzülen basalt parçacıkları |
| S5 | Dış · Bakır/Gül Çift Işık | R1 p1, R2 p2 | Profile | K1 | Eldivenin 5 cm kala durması |
| S6 | Dış · Bakır/Gül Çift Işık | R1 p1, R2 p2 | Low Angle | K1 | 1.5s gecikmeyle yayılan altın biyo-gravite halkası |
| S7 | Dış · Bakır/Gül Çift Işık | R1 p3 (Selin şeffaf kask) | CU | K1 | Şeffaflaşan vizör + retinal afterimage |
| S8 | Dış · Bakır/Gül Çift Işık | R4 p1 (Cam Hat) | High Angle | K1 | Fin'in sürtünmesiz kayması + cam iz |
| S9 | Dış · Bakır/Gül Çift Işık | R1 p1, R2 p2, R4 p1 | Extreme Wide | K1 | S0 kadrajında cam hat + uzaktaki dikey Fin |

---

## 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · C01 (Dr. Selin Vural)

```
Photorealistic full-length reference still, 35mm film grain, neutral grey studio backdrop. Exactly one human character — no clones, no second person. A 34-year-old female exogeologist sealed in a custom pressure suit. Torso shell: matte titanium-sapphire composite. Limbs: dark graphite ribbed material. Shoulders: copper-gold rank strips. Helmet: clear bubble helmet with a visible titanium frame, containing an internal warm-amber visor ring light that illuminates her face clearly through zero-tint glass. Closed hard tool case fastened flat on right thigh. Wrist display on left forearm. The back of the suit is one continuous smooth graphite panel from collar to hip, unbroken, carrying zero backpack, zero tanks, zero hoses.

NEGATIVE: No bloom, 0% bloom, no space fleets, no blasters, no backpacks, no oxygen tanks, no hoses, no floating baked text, no mouth movement, no airbrushed skin, no CGI textures, no camera shake. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 4829103   SHA-256: 9a8f...   DURUM: 🟢 ONAYLI
PANEL LİSTESİ: p1 · Ön boy — giysi malzemeleri   p2 · Profil — thigh case ve kask çerçevesi   p3 · Vizör ardı yüz CU [D146]
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ Selin Vural · SONUÇ ✅ · ⑲ öznitelik 3 (yaş, cinsiyet, milliyet)
```

---

### 📸 IMAGE PROMPT — SAYFA R2 · A01 (Fin - Monolith Gravite Varlığı)

```
Photorealistic full-length architectural reference still, 35mm film grain. A monolithic non-humanoid gravity entity named Fin on an exosphere planetary floor. Dimensions: 200 meters base length, 80 meters vertical peak height. Skin texture: smooth crystalline carbon-diamond obsidian with high specular reflectivity. Zero eyes, zero limbs, zero tentacles, zero mouth, zero flex joints, zero animalistic features. Clean monolithic geometry refracting ambient red-amber starlight in subtle prismatic rainbow patterns along its sharp vertical edge.

NEGATIVE: No animal legs, no tentacles, no eyes, no mouth, no muscle flex, no mechanical joints, no space fleets, no blasters, no glowing magic portals, no neon lights, no floating baked text, no CGI textures, no camera shake. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 7193012   SHA-256: 3c1e...   DURUM: 🟢 ONAYLI
PANEL LİSTESİ: p1 · K0 Yatay sırt görünümü   p2 · K1 Dikey 80m monolit silüeti   p3 · K2 Prizmatik yüzey dokusu makrosu
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ Monolitik obsidiyen varlık · SONUÇ ✅ · ⑲ öznitelik 2 (malzeme, boyut)
```

---

### 📸 IMAGE PROMPT — SAYFA R3 · E01 (Obsidian-7 Gezegen Zemin & Çift Gölge)

```
Photorealistic landscape still, 35mm film grain, 16:9 widescreen. Exosphere Moon Obsidian-7 environment. Vast vitrified volcanic basalt floor with high specular mirror-like reflectivity. Deep black starfield sky with binary red dwarf stars. Dual soft shadows cast across the vitrified ground at two distinct angles from every rock outcropping. Zero atmosphere haze, zero wind, zero vegetation, zero water.

NEGATIVE: No atmosphere wind, no clouds, no dust storms, no trees, no ocean, no space fleets, no blasters, no glowing magic portals, no neon lights, no floating baked text, no CGI textures. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

```
ÖNCELİK: 🟠 ZORUNLU   PANEL: 3   SEED: 1049281   SHA-256: 7b2d...   DURUM: 🟢 ONAYLI
PANEL LİSTESİ: p1 · Geniş krater düzlüğü   p2 · Çift gölge açısı detayı   p3 · Basalt yüzey yansıma makrosu
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ Volkanik basalt düzlüğü · SONUÇ ✅ · ⑲ öznitelik 2
```

---

### 📸 IMAGE PROMPT — SAYFA R4 · E02 (Camlaşmış Silikat Hat)

```
Photorealistic ground macro still, 35mm film grain. A smooth metastable vitrified glass track running across dark volcanic basalt ground on Obsidian-7. Formed by localized gravity alteration of surface bond energy. Clean sparkling crystalline surface reflecting red dwarf starlight. Zero lava, zero fire, zero melted rock, zero smoke.

NEGATIVE: No lava, no fire, no smoke, no molten rock, no space fleets, no blasters, no glowing magic portals, no neon lights, no floating baked text, no CGI textures. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

```
ÖNCELİK: 🟠 ZORUNLU   PANEL: 3   SEED: 5509281   SHA-256: 1e4f...   DURUM: 🟢 ONAYLI
PANEL LİSTESİ: p1 · Cam hat geniş takip açısı   p2 · Basalt-cam geçiş sınırı makrosu   p3 · Starlight yansıması
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ Camlaşmış silikat yol · SONUÇ ✅ · ⑲ öznitelik 2
```

---

## 7. ✅ KABUL KAPISI
```
[x] ① PANEL ARİTMETİĞİ (4 sayfa × 3 panel = 12 panel)
[x] ② ÇAPRAZ BAĞ (Tüm kodlar envanterde mevcut)
[x] ③ 120 PX TESTİ (Selin'in kask içi amber ışığı 120px'te ayırt ediliyor)
[x] ④ METİN SAYIMI (Her yüzeyde harf/rakam/ok = 0)
[x] ⑤ D79 VİZÖR (Optik berrak, yüz okunur, çerçeveli kask)
[x] ⑥ D79/D139 SIRT (Sırt düz panel, çıkıntı 0)
[x] ⑦ D69 KLON (Karakter sayısı = 1)
[x] ⑧ DURUM ÇİFTİ (A01 ve C01 durum merdiveni doğrulanmış)
[x] ⑨ ⑲ KİMLİK YIĞINI (Öznitelik ≤ 3)
[x] ⑩ ⑳b DEĞİŞİM (Görsel promptlar değişimin durumunu net tanımlar)
[x] ⑪ ÖLÇEK ŞAHİDİ (R2 sayfasında 1.8m Selin ölçek şahidi olarak mevcut)
[x] ⑫ SEED / SHA KAYDI (Tüm seedler tabloya işlendi)
[x] ⑬ BAYT AYNILIĞI (Character Bible promptları ile birebir aynı)
[x] ⑭ prompt_kontrol.py sonuç: 0 BLOCK
```
