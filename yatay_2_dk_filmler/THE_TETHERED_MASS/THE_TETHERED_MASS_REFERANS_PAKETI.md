# 🧷 THE_TETHERED_MASS — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md`

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Astronot Selin
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: Momentum Halat Tamburu & Çekici
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: THE_TETHERED_MASS          FORMAT: yatay 2-4 dk        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4K    SAHNE SAYISI: 16
SAYFA: 2   TOPLAM PANEL: 4   ARİTMETİK: 2 sayfa × 2 panel = 4
İMAJ MODELİ + SÜRÜM: Imagen 3 / Veo 3.1 Fast         TARİH: 10.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R01 | R1 | 1 | Astronot Basınç Giysisi & Vizör | 🔴 ZORUNLU | 849201 | pend | ONAYLI |
| R02 | R1 | 2 | Momentum Halat Tamburu & Modül | 🔴 ZORUNLU | 849202 | pend | ONAYLI |
| R03 | R2 | 1 | Koloni-Habitat İstasyonu Dış Yapı | 🔴 ZORUNLU | 849203 | pend | ONAYLI |
| R04 | R2 | 2 | Çekici Kokpit & İtki Paneli | 🔴 ZORUNLU | 849204 | pend | ONAYLI |

---

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| H01 | Astronot Basınç Giysisi | insan | S01 | S12 | R1 p1 | Düşük |
| V01 | Momentum Halat Tamburu | prop/araç | S00 | S15 | R1 p2 | Düşük |
| V02 | Koloni-Habitat İstasyonu | mimari | S03 | S15 | R2 p1 | Düşük |
| V03 | Çekici Kokpit & Panel | mekân | S02 | S12 | R2 p2 | Düşük |

---

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| V01 | K0 (temel) | Gergin sağlam halat lifleri | S00 | — | R1 p2 |
| V01 | K1 (kopuş) | Kopmuş serbest dönen lifler | S13 | S15 | R1 p2 |

---

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | Uzay / Vakum Güneş | R1 p2 | V01 | K0 | Lifin mikro kopma hareketi |
| S02 | İç / Amber Panel | R1 p1, R2 p2 | H01, V03 | K0 | Astronotun el hareketi |
| S03 | Uzay / Dünya Halo | R2 p1 | V02 | K0 | Orbital sürüklenme eğrisi |
| S11 | İç / Kırmızı İkaz | R1 p1, R2 p2 | H01, V03 | K0 | Akrilik cam kırma aksiyonu |
| S13 | Uzay / Dik Güneş | R1 p2, R2 p1 | V01, V02 | K1 | Bağlantı ayrılma şoku |
| S15 | Uzay / Atmosfer Ateş | R1 p2, R2 p1 | V01, V02 | K1 | Serbest halat ucunun dönmesi |

---

## 6. 📸 İMAJ PROMPTLARI

### 📸 IMAGE PROMPT — Panel R1.1 (Astronot Basınç Giysisi)

```
PHOTOGRAPH. A cinematic full-body reference page of a female astronaut in a dark grey industrial pressure suit with white role stripe on chest patch and mechanical wrist telemetry. The back of the suit is one continuous smooth panel from collar to hip, carrying no backpack, no thruster pack, no oxygen tanks. Clear 100% transparent glass helmet visor revealing focused eyes, no airbrushed skin, photorealistic 4K.

NEGATIVE: No space fleets, no blasters, no magic portals, no neon lights, no floating baked text, no mouth movement, no airbrushed skin, no CGI textures, no camera shake, no wind, no lava, no fire. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

### 📸 IMAGE PROMPT — Panel R1.2 (Halat Tamburu & Bağlantı Modülü)

```
PHOTOGRAPH. Industrial emergency momentum exchange tether drum module mounted on a spacecraft hull, thick rigid braided steel cable wrapped around a heavy-duty drum latch, zero-g space vacuum background, Vehicle orientation: Tug vessel positioned at 7 o'clock heading 1 o'clock toward station, station positioned at 2 o'clock in Earth orbit, photorealistic 4K.

NEGATIVE: No space fleets, no blasters, no magic portals, no neon lights, no floating baked text, no mouth movement, no airbrushed skin, no CGI textures, no camera shake, no wind, no lava, no fire. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

### 📸 IMAGE PROMPT — Panel R2.1 (Koloni-Habitat İstasyonu)

```
PHOTOGRAPH. Massive modular orbital agricultural colony station with solar array panels and green-lit agricultural domes, dark space background with Earth atmospheric horizon below, Vehicle orientation: Tug vessel positioned at 7 o'clock heading 1 o'clock toward station, station positioned at 2 o'clock in Earth orbit, 24mm prime wide lens, photorealistic 4K.

NEGATIVE: No space fleets, no blasters, no magic portals, no neon lights, no floating baked text, no mouth movement, no airbrushed skin, no CGI textures, no camera shake, no wind, no lava, no fire. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```

### 📸 IMAGE PROMPT — Panel R2.2 (Çekici Kokpit Paneli)

```
PHOTOGRAPH. Compact spaceship tug cockpit interior with red and amber instrument telemetry displays, manual override lever under acrylic glass safety cover, dark metallic console, Vehicle orientation: Tug vessel positioned at 7 o'clock heading 1 o'clock toward station, station positioned at 2 o'clock in Earth orbit, photorealistic 4K.

NEGATIVE: No space fleets, no blasters, no magic portals, no neon lights, no floating baked text, no mouth movement, no airbrushed skin, no CGI textures, no camera shake, no wind, no lava, no fire. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign.

Output: 16:9, 4K, photorealistic, no text, no watermark.
```
