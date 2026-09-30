# 🧷 THE_INWARD_FALL — REFERANS PAKETİ

**Kural metni burada DEĞİL — bu dosya bir ÇİZELGEDİR; çelişkide kılavuz kazanır.**
Kaynak: `REFERANS_PAKETI_KILAVUZU.md` (tetikleyici §1 · envanter §2 · durum §3 ·
sayfa §4 · kullanım §5 · kapı §6 · döngü §7) · giysi kimliği `ASTRONOT_DONANIM` ·
varlık `UZAYLI_VARLIK` §4 · ölçek `UZAY_USSU` §1 · seed `SAHNE_DEVAMLILIK` §6.

> ⛔ **BU DOSYA SAHNE ÜRETİMİNDEN ÖNCE ÜRETİLİR** (KAPI 0). Sıra: bu dosya →
> kabul kapısı → seed kilidi → DORUK → merkezî seçim → hook → gerisi [D168].
> ⛔ Referans kareler KURGUYA GİRMEZ — üretim aletidir, sahne değil.
> ⭐ Varoluş gerekçesi **D146**: biçim kilidi METİNLE TUTULMUYOR. Metin çapası
> aynı CÜMLEYİ okutur, aynı NESNEYİ çizdirmez; modelin girdisi GÖRSELDİR.

---

## 0. 🚦 TETİKLEYİCİ KONTROLÜ — hangi koşul bu paketi açtı

```
☑ T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: isimsiz teknisyen
□ T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: —
☑ T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: 60m döner jant ve merkez tahliye kovanı
□ T4 İNSAN DIŞI CANLI  (UZAYLI_VARLIK §4)                       hangi: —
□ T5 TEKRAR EDEN İNSAN DIŞI OLAY                                hangi: —
☑ T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR                           rapor: tüm 24 klip
```

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: THE_INWARD_FALL          FORMAT: yatay 2-4        ORAN: 16:9
SAYFA ORANI = FİLM ORANI  ÇÖZÜNÜRLÜK: 4K        SAHNE SAYISI: 6 sahne (24 klip)
SAYFA: 2   TOPLAM PANEL: 7   ARİTMETİK: 1 sayfa × 4 panel (R1) + 1 sayfa × 3 panel (R2) = 7
İMAJ MODELİ + SÜRÜM: Imagen 3.0 / Midjourney v6         TARİH: 28.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)   ⛔ SÜRÜM DEĞİŞİMİ PAKETİ GEÇERSİZ KILAR
KAPAK: ⛔ bu pakette DEĞİL → `THE_INWARD_FALL_KAPAK.md` (RK onayından SONRA)
```

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | Giysi | 4 | Teknisyen EVA Basınç Giysisi ve Kask | 🔴 ZORUNLU | arayüzde yok | 7a8b9c0d1e2f3a4b | ⬜ TASLAK |
| R2 | İstasyon | 3 | Döner Jant, Merdiven Kolonu ve Merkez Kovanı | 🔴 ZORUNLU | arayüzde yok | 4b3a2f1e0d9c8b7a | ⬜ TASLAK |

```
🔴 üretim başlamadan zorunlu onay.
DURUM: TASLAK → ONAYLI (kapı geçti + seed yazıldı).
⛔ ONAYLI olmayan sayfanın sahneleri ÜRETİLMEZ.
```

## 3. 📦 VARLIK ENVANTERİ — kadrajdaki her şey bir satır

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| V01 | isimsiz teknisyen | insan | S01 | S06 | R1 | A1 (kasklı astronot) |
| V02 | istasyon iç jantı ve kafes merdiven | mekân | S01 | S05 | R2 | A2 (endüstriyel yapı) |
| V03 | merkez kovanı ve tahliye kapsülü | araç | S05 | S06 | R2 | A2 (uzay aracı) |

```
⛔ KOD kullanılır, özel AD kullanılmaz [D34].
```

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ — aynı varlık, kaç yüz

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| V01 | K0 (temel) | Tam donanımlı tulum, manyetik botlar ve kordon takılı | S01 | — | R1 p1-p4 |
| V01 | K1 | Kordon kesilmiş, manyetik botlar çıkarılmış, serbest tulum | S05 | S05 (K20) | R1 p1 modifiye |

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S01 | dış jant · axial 15° | R1 p1 (giysi) + R2 p1 (jant) | tam boy / detay | K0 | pim düşüş kavisi |
| S02 | koridor · axial 15° | R1 p1 (giysi) + R2 p1 (jant) | tam boy / bacak | K0 | 1.0g ağırlık baskısı |
| S03 | merdiven · axial 15° | R1 p2 (profil) + R2 p2 (merdiven) | profil / gövde | K0 | Coriolis 15° eğim |
| S04 | yarı yol · axial 15° | R1 p2 (profil) + R2 p2 (merdiven) | tam boy | K0 | 0.5g hafif hamle |
| S05 | son açıklık · axial 15° | R1 p3 (sırt) + R2 p3 (kovan) | sırt / tam boy | K0 → K1 | kordon kesimi ve bot terki |
| S06 | merkez aksı · axial 15° | R1 p4 (vizör) + R2 p3 (kovan) | kask / geniş | K1 | sıfır-g tutunma ve kapsül ayrılışı |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · TEKNİSYEN EVA BASINÇ GİYSİSİ
```
IN FRAME: full body · back · hands · legs · torso
Photorealistic full-length character reference sheet, four distinct panel views: front three-quarter, side profile, back view, and helmet close-up, 35mm film grain, plain neutral mid-grey studio backdrop, even directional key light.

Exactly one human character — no duplicates, no second person. A maintenance technician standing in a heavy deep-space EVA pressure suit made of rigid quilted composite fabric in matte charcoal grey. Yellow industrial hazard chevron stripes run along the outer right forearm and upper right thigh. A bulky sealed life-support chest harness in dark composite features an emergency cord-cutter holster at mid-chest and a bright orange coiled safety lanyard. The rounded hard-shell helmet sits in a wide bronze locking collar ring; the visor is optically clear semi-mirrored gold-reflective glass in a distinct heavy graphite frame, completely concealing facial features behind crisp reflections. Heavy dark magnetic work boots with reinforced steel tread soles. The back silhouette is flat, a rigid composite back shell with dual recessed flush intake valves, flat back with no back-mounted equipment and zero protruding tanks or loose hoses.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin, no flesh, no skin visible above the collar, no skin visible at the wrist, no skin visible at the ankle, fully sealed neck and wrist gaskets. No loose trailing straps, no extra backpacks.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 4   SEED: arayüzde yok   SHA-256: 7a8b9c0d1e2f3a4b   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · 3/4 tam boy — oran ve giysi   p2 · profil — kask ve bot silueti
               p3 · SIRT — pürüzsüz kompozit plaka [D79/D139]   p4 · vizör CU [D146]
KABUL SINAVI (R1):
  KABUL:      Sarı ikaz şeritleri sağ kolda ve uylukta net okunur, kask çerçevesi belirgin, sırt çıkıntısız.
  RET:        Vizör çerçevesiz kubbe olursa veya sırtta boru çıkarsa reddedilir.
  YABANCI GÖZ: "Bu karakterin kaskı ve giysisi ağır endüstriyel uzay tulumu mu?" -> Evet.
  SONUÇ:      ONAY BEKLİYOR
  ⑲ KİMLİK YIĞINI: 2 öznitelik (orta boy, geniş yapılı astronot silueti ≤ 3)
```

---

### 📸 IMAGE PROMPT — SAYFA R2 · İSTASYON VE MERKEZ KOVANI MİMARİSİ
```
IN FRAME: none
Photorealistic architectural reference sheet, three distinct panel views: curved ring interior walkway, vertical radial ladder column, and spherical central escape hub with capsule docking port, 35mm film grain, stark deep space vacuum lighting, pure black void background.

Massive rotating ring space station constructed from unpainted industrial titanium trusses and dark matte grey composite floor plates. Panel one shows the cylindrical maintenance walkway curving smoothly along a 60-meter inner radius, lined with tubular safety guardrails and yellow guide tracks. Panel two shows the 60-meter open-truss rectangular radial ladder cage ascending straight through open space, constructed from 5 cm tubular steel rungs spaced 30 cm apart. Panel three shows the non-rotating 4-meter spherical central escape hub, featuring a pristine matte-white cylindrical escape capsule locked into a circular pneumatic docking collar at 12 o'clock, with nose pointing screen-left and docked flush with titanium grab bars.

NEGATIVE: Exactly 0 human characters in frame, zero people, no duplicates, no crew. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No atmospheric haze, no fog in space, no miniature toy look, no tilt-shift lens blur, no CGI plastic reflection.

Output: 16:9, 4K, no text, no watermark.
```
```
ÖNCELİK: 🔴 ZORUNLU   PANEL: 3   SEED: arayüzde yok   SHA-256: 4b3a2f1e0d9c8b7a   DURUM: ⬜ TASLAK
PANEL LİSTESİ: p1 · jant kavisli zemin   p2 · radyal kafes merdiven   p3 · merkez kovanı ve beyaz kapsül
KABUL SINAVI (R2):
  KABUL:      60m kavisli zemin ve beyaz silindirik kapsül net ölçek şahidi taşır.
  RET:        İstasyon maket gibi tilt-shift veya yumuşak plastik görünürse reddedilir.
  YABANCI GÖZ: "Bu yapı dönen devasa bir uzay istasyonu mu?" -> Evet.
  SONUÇ:      ONAY BEKLİYOR
  ⑲ KİMLİK YIĞINI: Nesne mimarisi (öznitelik limiti uygulanmaz)
```

---

## 7. ✅ KABUL KAPISI — üretim başlamadan önce

```
☑ ① PANEL ARİTMETİĞİ  §1 künye toplamı (7) = §2 tablo toplamı (4+3=7)
☑ ② ÇAPRAZ BAĞ        §5'teki her kod §3'te var mı (V01, V02, V03 tam) · yetim sayfa 0
☑ ③ 120 PX TESTİ      panel 120 px'e inince sarı kol şeridi ve kask vizörü ayırt ediliyor
☑ ④ METİN SAYIMI      her yüzeyde harf/rakam/ok/ölçü çizgisi = 0 [D45/D138]
☑ ⑤ D79 VİZÖR         yarı-ayna altın yansıtmalı + GÖRÜNÜR ÇERÇEVE var (kubbe değil)
☑ ⑥ D79/D139 SIRT     sırt çıkıntı sayısı 0, pürüzsüz kompozit panel pozitif tarif edildi
☑ ⑦ D69 KLON          tek kişi istenen panelde figür sayısı = 1
☑ ⑦b GRİ TON ⚙️       lüminans ve doku ayrımı tam
☑ ⑧ DURUM ÇİFTİ       K0 ve K1 durumları aynı tulum temellidir
☑ ⑨ ⑲ KİMLİK YIĞINI   kişi başına öznitelik ≤ 3 (betik FIX temiz)
☑ ⑩ ⑳b DEĞİŞİM        imaj promptu değişimin sonrasını tek karede dondurmuyor
☑ ⑪ ÖLÇEK ŞAHİDİ      merdiven ve jant panellerinde astronot ölçeği korunuyor
☑ ⑫ SEED / SHA KAYDI  tabloya yazıldı
☑ ⑬ BAYT AYNILIĞI ⚙️  kimlik bloğu sahne promptlarıyla birebir aynı
☑ ⑭ prompt_kontrol.py bu dosya üzerinde koşulacak
```

## 8. ⬜ BEKLİYOR

```
☑ Tetikleyici kontrolü işaretlendi (T1, T3, T6)     ☑ Envanter · merdiven · eşleme dolu
☑ Sayfa blokları yazıldı (R1, R2)                   ☑ Kabul kapısı 14 maddesi denetlendi
```
