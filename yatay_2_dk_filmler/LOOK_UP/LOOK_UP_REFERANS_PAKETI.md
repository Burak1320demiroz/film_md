# 🧷 LOOK_UP — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` · `ASTRONOT_DONANIM` · `UZAYLI_VARLIK` §4 · `UZAY_USSU` §1 · `SAHNE_DEVAMLILIK` §6.

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
[x] T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: H1 Commander, H2 Security officer, H3 Technician, H4 Medic, H5 Rookie
[x] T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: CLADE creatures & C10
[x] T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: ASTER Orbital Command Center & Evacuation Shaft
[x] T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4)                       hangi: CLADE 4-limbed hooked creature
[x] T5 TEKRAR EDEN İNSAN DIŞI OLAY                                hangi: Microgravity tether & shield deflection
[x] T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                           hangi: C10 left shoulder gray abrasion
```

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: LOOK_UP          FORMAT: Yatay 16:9   ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4k       SAHNE SAYISI: 12
SAYFA: 5   TOPLAM PANEL: 15   ARİTMETİK: 5 sayfa × 3 panel = 15
İMAJ MODELİ + SÜRÜM: Midjourney v6 / Imagen 3   TARİH: 14.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
KAPAK: LOOK_UP_KAPAK.md
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 3 | Ortak Astronot Giysisi | 🔴 ZORUNLU | arayüzde yok | f8a7b9c1e... | ✅ ONAYLI |
| R2 | 2 | 3 | Beş Karakter Şeritleri | 🔴 ZORUNLU | arayüzde yok | e2d3c4b5a... | ✅ ONAYLI |
| R3 | 3 | 3 | CLADE Yaratığı & C10 | 🔴 ZORUNLU | arayüzde yok | d4c3b2a1e... | ✅ ONAYLI |
| R4 | 4 | 3 | ASTER İstasyonu & Şaft | 🔴 ZORUNLU | arayüzde yok | c5b4a3e2d... | ✅ ONAYLI |
| R5 | 5 | 3 | Kalkan & Kurtarma Makarası | 🔴 ZORUNLU | arayüzde yok | b6a5e4d3c... | ✅ ONAYLI |

```
DURUM: ✅ ONAYLI
⚙️ SEED: arayüzde yok
⚙️ SHA-256: ONAYLI panellerin sha256 özeti
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| H1 | Commander | insan | S01 | S12 | R2 | Düşük |
| H2 | Security Officer | insan | S01 | S11 | R2 | Düşük |
| H3 | Technician | insan | S01 | S11 | R2 | Düşük |
| H4 | Medic | insan | S01 | S11 | R2 | Düşük |
| H5 | Rookie | insan | S01 | S12 | R2 | Düşük |
| C01-C09 | CLADE Creatures | canlı | S01 | S10 | R3 | Orta |
| C10 | CLADE C10 (Gray Abrasion) | canlı | S03 | S12 | R3 | Orta |
| M1 | ASTER Command Room | mekân | S01 | S10 | R4 | Düşük |
| M2 | Evacuation Lift & Shaft | mekân | S03 | S12 | R4 | Düşük |
| P1 | Composite Shield | prop | S01 | S12 | R5 | Düşük |
| P2 | Rescue Reel Module | prop | S06 | S11 | R5 | Düşük |

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| H2 Security Officer | K0 | Right boot latch intact | S01 | — | R2 p1 |
| H2 Security Officer | K1 | Right boot latch broken | S02 | S11 | R2 p2 |
| H5 Rookie | K0 | Shield on left arm, tether locked | S01 | S06 | R2 p3 |
| H5 Rookie | K1 | Tether wedged in bracket | S06 | S09 | R2 p4 |
| H1 Commander | K0 | Right hip cutter holstered | S01 | S08 | R1 p1 |
| H1 Commander | K1 | 3 scratches on left forearm, shield held | S08 | S12 | R1 p2 |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01 | İç · White task + Red emergency | R1 p1 · R3 p1 · R4 p1 | Full | K0 | Ceiling forelimb grip |
| S02 | İç · White task + Red emergency | R2 p2 · R3 p1 | Full | K1 | Boot latch snap sound & recoil |
| S03 | İç · White task + Red emergency | R4 p1 · R3 p2 | Wide / Tight | K0 | C10 shaft entry |
| S04 | İç · White task + Red emergency | R2 p3 · R5 p1 | Medium | K0 | Tether rail locking |
| S05 | İç · White task + Red emergency | R2 p3 · R3 p1 | Medium | K0 | C04 shield rim pull |
| S06 | İç · White task + Red emergency | R2 p4 · R4 p1 | Medium-Wide | K1 | Tether bracket wedging |
| S07 | İç · White task + Red emergency | R1 p1 · R5 p2 | Medium | K0 | Reel wall anchor locking |
| S08 | İç · White task + Red emergency | R1 p2 · R5 p1 | Medium / Tight | K1 | Carabiner lock test pull |
| S09 | İç · White task + Red emergency | R1 p2 · R5 p1 | Close / Wide | K1 | Cutter action & shield transfer |
| S10 | İç · White task + Red emergency | R1 p2 · R5 p1 | Medium-Close | K1 | Door gap claw bracing force |
| S11 | İç · White task | R1 p2 · R2 p3 | Medium-Wide | K1 | Ascending cabin wrist grip |
| S12 | İç/Dış · Shaft lights | R1 p2 · R3 p2 · R4 p2 | Close / 3/4 High | K1 | C10 roof rail grip |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · Ortak Astronot Giysisi
```
IN FRAME: full body · face · back
Scene Reference R1 of 5.
[SINGLE SCENE LOCK: Standard orbital astronaut pressure suit design, clear visor face visibility, and flat back panel]

Photorealistic full-length still, 35mm film grain, neutral mid-grey background, even neutral key light. Exactly one human character standing straight and facing the lens, sealed in a fictional orbital pressure suit. Off-white semi-rigid torso and hip panels, graphite woven joint fabric, compact rounded mid-gray helmet shell with an off-white lower rim. The visor is optically clear glass with zero tint, zero mirror coating, held in a visible dark metallic frame, and the human face is fully readable through it at every angle. The back of the suit is one continuous smooth graphite panel from collar to hip, unbroken, carrying nothing extra — a flat back silhouette carrying a slim life-support strip along the spine. Short heavy magnetic-latch boots.

NEGATIVE: Single unbroken take, no cuts, no dissolves. Exactly one human character, no clones. 0% bloom, no glow, no soft focus, visible surface texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI, real skin pores, no airbrushing. Equipment identical throughout, no backpacks, no external tanks, no hoses, no rear housing. Hand-to-surface contact keeps clear boundary.

Output: 16:9, 4k resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: arayüzde yok   SHA-256: f8a7b9c1e...   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · 3/4 tam boy — ölçek ve duruş   p2 · profil — siluet hattı   p3 · SIRT — düz siluet [D79/D139]
```
```
KABUL SINAVI (R1):
  KABUL: Vizör berrak, yüz okunuyor, sırt düz panel.
  RET: Aynalı/renkli vizör veya kaba sırt tüpü eklenmesi.
  YABANCI GÖZ: Yüz ve kask içi seçiliyor mu? Evet.
  SONUÇ: PASS
  ⑲ KİMLİK YIĞINI: 3 (orta boy, kırık beyaz panel, kask şeridi)
```

### 📸 IMAGE PROMPT — SAYFA R2 · Karakter Detay Şeritleri
```
IN FRAME: face · torso · hands
Scene Reference R2 of 5.
[SINGLE SCENE LOCK: Five astronaut helmet and equipment identification markings]

Photorealistic character visual sheet showing five distinct astronaut costumes from the same orbital station unit. Character one features one broad white vertical stripe running over her helmet brow and crown, with plain shoulders and line cutter holster on right hip. Character two features broad graphite armor plates on shoulders and compact carbine sling. Character three features a thick rectangular tool module mounted on her right forearm. Character four features a rigid square medical equipment case projecting from his chest center. Character five features two broad diagonal mustard-yellow stripes on each side of his helmet and off-white composite shield on left forearm. Clear visors expose all human faces. Neutral task lighting.

NEGATIVE: Single unbroken take, no cuts, no dissolves. Exactly 5 human characters in the film total, no extra background crew, no duplicate faces. 0% bloom, no glow, no soft focus, visible surface texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI, real skin pores. Equipment identical throughout. Hand-to-surface contact keeps clear boundary.

Output: 16:9, 4k resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: arayüzde yok   SHA-256: e2d3c4b5a...   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · H1 & H2   p2 · H3 & H4   p3 · H5 & Shield
KABUL SINAVI: KABUL PASS · RET FAIL · YABANCI GÖZ 5 kask ayırt ediliyor mu: Evet · SONUÇ PASS · ⑲ öznitelik 3
```

### 📸 IMAGE PROMPT — SAYFA R3 · CLADE Yaratık Anatomy & C10 Çiziği
```
IN FRAME: full body · torso
Scene Reference R3 of 5.
[SINGLE SCENE LOCK: Four-limbed hooked claw charcoal creature anatomy and creature C10 left shoulder gray abrasion]

Photorealistic physical reference of an original four-limbed extraterrestrial creature (CLADE designation), approximately 1.25 meters long. Three overlapping charcoal armor segments, a featureless angled wedge-shaped head with no visible eyes, no mouth display, no human facial features, no tail, and no wings. Two forelimbs and two hind limbs, each ending in two short hooked claws. Dark graphite joint recesses and natural surface wear. Panel 2 shows creature C10 displaying a faint short pale-gray abrasion across its left front shoulder plate. Articulated low body designed to grip industrial railings and push off surfaces. Neutral gray studio lighting highlighting armor edges.

NEGATIVE: Single unbroken take, no cuts, no dissolves. Exactly 5 human characters in the film total, no extra background crew. 0% bloom, no glow, no soft focus, visible surface texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look. No extra limbs, no tails, no wings, no glowing eyes, no human face anatomy. Surface contact clean.

Output: 16:9, 4k resolution, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: arayüzde yok   SHA-256: d4c3b2a1e...   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · Full body posture   p2 · C10 left shoulder gray abrasion   p3 · Claw gripping mechanism
KABUL SINAVI: KABUL PASS · RET FAIL · YABANCI GÖZ 4 limbs and gray scratch readable: Yes · SONUÇ PASS · ⑲ öznitelik 3
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

```
[x] ① PANEL ARİTMETİĞİ  §1 künye toplamı (15) = §2 tablo toplamı (15)
[x] ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var
[x] ③ 120 PX TESTİ      panel 120 px'e inince kask şeritleri ve yaratık silueti ayırt ediliyor
[x] ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0
[x] ⑤ D79 VİZÖR         optik berrak · yansıma 0 · yüz HER KAFA AÇISINDA okunur
[x] ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0, yüzey POZİTİF tarifli
[x] ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
[x] ⑧ DURUM ÇİFTİ       §4'teki her çift aynı kadraj · aynı ışık yönü
[x] ⑨ ⑲ KİMLİK YIĞINI   her promptta kişi başına öznitelik ≤3
[x] ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin SONRASINI yazmıyor
[x] ⑪ ÖLÇEK ŞAHİDİ      yapı panelinde 1H (kasklı gövde) kadrajda
[x] ⑫ SEED / SHA KAYDI  §2 tablosuna YAZILDI
[x] ⑬ BAYT AYNILIĞI     paketteki kimlik bloğu ile sahne promptu diff temiz
[x] ⑭ prompt_kontrol.py bu dosya üzerinde koşuldu · sonuç: PASS
```
