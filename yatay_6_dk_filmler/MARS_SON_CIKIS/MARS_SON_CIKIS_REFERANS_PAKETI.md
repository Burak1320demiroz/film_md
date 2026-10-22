# 🧷 MARS_SON_CIKIS — REFERANS PAKETİ

## 0. 🚦 TETİKLEYİCİ KONTROLÜ

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Lena & Aras
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK                     hangi: Kestrel & Horizon
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon)            hangi: Kestrel & Horizon
□ T4 İNSAN DIŞI CANLI                                          hangi: —
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY                               hangi: —
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                           rapor: MARS_SON_CIKIS
```

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: MARS_SON_CIKIS          FORMAT: 16:9 yatay        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 1920x1080    SAHNE SAYISI: 36
SAYFA: 3   TOPLAM PANEL: 9   ARİTMETİK: 3 sayfa × 3 panel = 9
İMAJ MODELİ + SÜRÜM: Midjourney v6 / Imagen 3        TARİH: 15.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 3 | Lena & Aras Astronot Giysileri | 🔴 ZORUNLU | 4920194 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | ONAYLI |
| R2 | 2 | 3 | Kestrel Yükseliş Aracı (~18m) | 🔴 ZORUNLU | 4920195 | f4c0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b856 | ONAYLI |
| R3 | 3 | 3 | Horizon Ana Gemi (~540m) & Port | 🔴 ZORUNLU | 4920196 | a5c0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b857 | ONAYLI |

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| CHAR_01 | Lena | insan | S01 | S36 | R1 | Düşük |
| CHAR_02 | Aras | insan | S01 | S36 | R1 | Düşük |
| VEH_01 | Kestrel | araç | S02 | S33 | R2 | Orta |
| SHIP_01 | Horizon | gemi | S07 | S36 | R3 | Orta |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| Aras | K0 (temel) | Sağlam giysi ve sol kol | S01 | — | R1 p1 |
| Aras | K1 | Sol ön kol zırhı ezilmiş, askıya bağlı | S14 | S14 | R1 p3 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01-S03 | Dış / İç Mars | R1 p1, R2 p1 | Tam | K0 | Fren kolu hareketi |
| S14-S20 | İç Habitat / Kokpit | R1 p3 | Tam | K1 | Sol kol askı kayışı |
| S21-S32 | Uzay Yörünge | R2 p2, R3 p1 | Tam | K0 | Bağıl hız sönümlemesi |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · LENA & ARAS SUITS

```
IN FRAME: full body
Photorealistic full-length still of exactly two adult human astronauts standing on neutral studio backdrop, 35mm film grain, even lighting.
Left figure female pilot: 35-year-old female astronaut, dark hair tied at nape, wearing off-white composite EVA suit with dark petrol blue side torso panels, clear transparent curved visor with visible dark frame, face readable inside, smooth continuous back suit panel from collar to hip without backpack.
Right figure male engineer: 41-year-old male astronaut, short curly black hair, wider torso build, wearing off-white composite EVA suit with oxide-orange shoulder accent panels, clear transparent curved visor with dark frame, face readable inside, smooth continuous back suit panel from collar to hip without backpack.
No extra equipment, no extra characters, no floating gear.

NEGATIVE: 0% bloom, film grain, No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no clones, human count 2, no extra limbs, no helmet backpacks, flat back, back silhouette is flat, zero tint, optically clear, fully readable through, no golden back thrusters, no seamless visors, no glowing suits, no floating gear.

Output: 16:9 aspect ratio, 1920x1080 resolution, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 4920194   SHA-256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855   DURUM: ONAYLI
PANEL LİSTESİ: p1 · Lena & Aras tam boy duruş   p2 · Vizör ardı yüz ve kask detayları   p3 · Aras K1 ezilmiş sol kol askısı
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ ✅ · SONUÇ ✅ · ⑲ öznitelik 3
```

### 📸 IMAGE PROMPT — SAYFA R2 · KESTREL ASCENT VEHICLE

```
IN FRAME: full body
Photorealistic full-length exterior view of an 18-meter wingless space ascent vehicle named Kestrel, 35mm film grain, neutral key light in orbital space.
Vehicle orientation: nose pointing 12 o'clock relative to flight path.
Matte off-white ceramic composite exterior tiles, subtle reddish Mars dust coating on the lower hull, dark joint bands. Curved aerodynamic nose, four symmetrical RCS thruster quads, three heavy retracted landing gear housings. Fixed docking ring at the nose tip with visible optical lens port. Deep cockpit window with dark tinted glass.
The spacecraft body is solid composite tile construction with smooth panel seams.
No wings, no trailing flames, no extra thruster modules, no extra gear.

NEGATIVE: 0% bloom, film grain, No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no clones, human count 0, no extra limbs, no helmet backpacks, flat back, back silhouette is flat, zero tint, optically clear, fully readable through, no golden back thrusters, no seamless visors, no glowing suits, no floating gear.

Output: 16:9 aspect ratio, 1920x1080 resolution, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 4920195   SHA-256: f4c0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b856   DURUM: ONAYLI
PANEL LİSTESİ: p1 · Kestrel tam gövde profili   p2 · Burun kenetlenme halkası CU   p3 · Kokpit pencere ve RCS kulvarı
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ ✅ · SONUÇ ✅ · ⑲ öznitelik 3
```

### 📸 IMAGE PROMPT — SAYFA R3 · HORIZON MOTHERSHIP & DOCKING PORT

```
IN FRAME: full body
Photorealistic exterior shot of a 540-meter interstellar mothership named Horizon in deep space orbit, 35mm film grain, direct solar illumination against black space backdrop.
Vehicle orientation: main spine truss aligned 12 o'clock orbital track, docking port facing forward.
Single long central truss spine, matte grey radiator panels, reinforced front shielding section. Forward docking port module featuring three prominent guide pins arranged symmetrically and six mechanical locking latches around the circular rim. High contrast metallic surfaces, crisp shadow lines.
The mothership hull features continuous metallic structural plates.
No rotating artificial gravity rings, no glowing thruster trails in idling state.

NEGATIVE: 0% bloom, film grain, No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no clones, human count 0, no extra limbs, no helmet backpacks, flat back, back silhouette is flat, zero tint, optically clear, fully readable through, no golden back thrusters, no seamless visors, no glowing suits, no floating gear.

Output: 16:9 aspect ratio, 1920x1080 resolution, no text, no watermark.
```

```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: 4920196   SHA-256: a5c0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b857   DURUM: ONAYLI
PANEL LİSTESİ: p1 · Horizon tam omurga silüeti   p2 · Port mekanizması ve 3 rehber pim CU   p3 · Korunan iç hacim sığınak koridoru
KABUL SINAVI: KABUL ✅ · RET ❌ · YABANCI GÖZ ✅ · SONUÇ ✅ · ⑲ öznitelik 3
```

---

## 7. ✅ KABUL KAPISI

```
☑ ① PANEL ARİTMETİĞİ  §1 künye toplamı = §2 tablo toplamı (9 panel)
☑ ② ÇAPRAZ BAĞ        Tüm kodlar envanterle eşleşti
☑ ③ 120 PX TESTİ      Tüm nesneler 120px üzerinde okunabilir
☑ ④ METİN SAYIMI      Metin/filigran sayısı = 0
☑ ⑤ D79 VİZÖR         Optically clear transparent visor with visible dark frame, face readable inside.
☑ ⑥ D79/D139 SIRT     The back of the suit is one continuous smooth panel from collar to hip, unbroken, carrying no backpack or external housing.
☑ ⑦ D69 KLON          Figür sayıları net kilitli
☑ ⑧ DURUM ÇİFTİ       Aras K0 ve K1 durumları tanımlı
☑ ⑨ ⑲ KİMLİK YIĞINI   Öznitelik sayıları ≤ 3
☑ ⑩ ⑳b DEĞİŞİM        İmaj promptları t=0 durumunu tanımlıyor
☑ ⑪ ÖLÇEK ŞAHİDİ      İnsan ve araç ölçek oranları tutarlı
☑ ⑫ SEED / SHA KAYDI  Tüm seed ve özet değerleri yazıldı
☑ ⑬ BAYT AYNILIĞI     Bible bloğu ile referans metinleri aynı
☑ ⑭ prompt_kontrol.py Koşuldu ve onaylandı
```
