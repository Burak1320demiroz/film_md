# 🧷 KRONOS_SON_SINYAL — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Kestrel & Aras
☑ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: Kronos Station A & B
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: Red Hatch H-R
```

## 1. 🎫 PAKET KÜNYESİ
```
FİLM: KRONOS_SON_SINYAL          FORMAT: yatay_8_dk_filmler        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 1280x720    SAHNE SAYISI: 48
SAYFA: 2   TOPLAM PANEL: 8   ARİTMETİK: 2 sayfa × 4 panel = 8
İMAJ MODELİ + SÜRÜM: Imagen 3         TARİH: 15.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | 1 | 4 | Kestrel Suit | 🔴 ZORUNLU | 1001 | SHA-R1 | ✅ ONAYLI |
| R2 | 2 | 4 | Aras Suit | 🔴 ZORUNLU | 1002 | SHA-R2 | ✅ ONAYLI |

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| C01 | Kestrel | insan | S01 | S48 | R1 | DÜŞÜK |
| C02 | Aras | insan | S02 | S42 | R2 | DÜŞÜK |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · Kestrel Pressure Suit
```
IN FRAME: full body, face, back, exactly 1 human character standing straight facing camera.
Photorealistic studio full-length character reference portrait of Kestrel. She is a 32-year-old female space commander with short dark hair, calm focused expression, and a small permanent scar near her left eyebrow. She wears a tailored cream-gray extravehicular pressure suit featuring distinct petrol-blue shoulder accent panels and dark gray utility joints. The helmet has a 180-degree optically clear transparent visor with visible metal frame, completely clear without mirror coating or tint. The back silhouette is flat, carrying no equipment, with a single vertical center seam. She stands anchored straight on a neutral studio floor.

NEGATIVE: no bloom, no watermark, no text, no logo, no labels, no second person, no clones, no extra characters, no multiple people, no film grain, no captions, no subtitles, no backpack, no rear tank, no rear housing, no oxygen tank, no back-mounted gear.

Output: 16:9 ratio, 720p, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: 1001   SHA-256: SHA-R1   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · 3/4 tam boy   p2 · profil   p3 · sırt   p4 · vizör ardı yüz CU
```
```
KABUL SINAVI (R1):
  KABUL: ✅ Omuz petrol mavisi şerit ve şeffaf vizör doğrusal ayırt ediliyor.
  RET: Yok
  YABANCI GÖZ: astronot kıyafeti · doğru
  SONUÇ: ✅ GEÇTİ
  ⑲ KİMLİK YIĞINI: 3 (yaş, cinsiyet, saç)
```

### 📸 IMAGE PROMPT — SAYFA R2 · Aras Pressure Suit
```
IN FRAME: full body, face, back, exactly 1 human character standing straight facing camera.
Photorealistic studio full-length character reference portrait of Aras. He is a 35-year-old male system engineer with short dark hair, short stubble beard, and a calm, resolute expression. He wears a tailored cream-gray extravehicular pressure suit featuring distinct orange shoulder accent panels and dark gray utility joints. The helmet has a 180-degree optically clear transparent visor with visible metal frame, completely clear without mirror coating or tint. The back silhouette is flat, carrying no equipment, with a single vertical center seam. He stands anchored straight on a neutral studio floor.

NEGATIVE: no bloom, no watermark, no text, no logo, no labels, no second person, no clones, no extra characters, no multiple people, no film grain, no captions, no subtitles, no backpack, no rear tank, no rear housing, no oxygen tank, no back-mounted gear.

Output: 16:9 ratio, 720p, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: 1002   SHA-256: SHA-R2   DURUM: ✅ ONAYLI
PANEL LİSTESİ: p1 · 3/4 tam boy   p2 · profil   p3 · sırt   p4 · vizör ardı yüz CU
```
```
KABUL SINAVI (R2):
  KABUL: ✅ Omuz turuncu şerit ve sakallı yüz doğrusal ayırt ediliyor.
  RET: Yok
  YABANCI GÖZ: astronot kıyafeti · doğru
  SONUÇ: ✅ GEÇTİ
  ⑲ KİMLİK YIĞINI: 3 (yaş, cinsiyet, sakal)
```

---

## 7. ✅ KABUL KAPISI

```
☑ ① PANEL ARİTMETİĞİ  2 sayfa × 4 panel = 8
☑ ② ÇAPRAZ BAĞ        Tüm kodlar envanterde var
☑ ③ 120 PX TESTİ      Şerit ve vizör çerçevesi okunuyor
☑ ④ METİN SAYIMI      Yazı/etiket = 0
☑ ⑤ D79 VİZÖR         Vizör optik berrak, yüz okunuyor
☑ ⑥ D79/D139 SIRT     Sırt paneli düz ve seam çizgili
☑ ⑦ D69 KLON          Tek kişi
☑ ⑧ DURUM ÇİFTİ       Eşit ışık ve kadraj
☑ ⑨ ⑲ KİMLİK YIĞINI   Öznitelik = 3
```
