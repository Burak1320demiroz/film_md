# 🧷 THE_STILL_POINT — REFERANS PAKETİ

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
[x] T1 AYIRT ETME KANALI KAPALI (kask · vizör · basınç giysisi)   kim: Nora (opak siyah vizör, koyu arduvaz EVA giysi)
[x] T2 BİÇİM KİLİDİ METİNLE TUTULMAYAN VARLIK [D146]              hangi: ORISON Orbital İstasyonu (100 m dönen halka)
[x] T3 ORANI SÖZLE YAZILAMAYAN NESNE (araç · istasyon · mimari)   hangi: Bakım Arabası (ray hattı elektrikli araba)
[x] T6 BİR VARLIK TEKRAR TEKRAR DÖNÜYOR / QA'da biçim sapması     rapor: Turuncu Ağır Çelik Anahtar (S00, S18, S23)
```

---

## 1. 🎫 PAKET KÜNYESİ

```
FİLM: THE_STILL_POINT          FORMAT: YATAY     ORAN: 16:9
SAYFA ORANI = FİLM ORANI (16:9)  ÇÖZÜNÜRLÜK: 4K UHD (3840×2160)   SAHNE SAYISI: 24
SAYFA: 4   TOPLAM PANEL: 14   ARİTMETİK: R1(4) + R2(4) + R3(4) + R4(2) = 14
İMAJ MODELİ: Imagen 3 / Midjourney v6.1     TARİH: 21.09.2026
VİDEO: Veo 3.1 Fast (Google Flow)
KAPAK: ⛔ bu pakette DEĞİL → THE_STILL_POINT_KAPAK.md
```

---

## 2. 🔢 ÜRETİM SIRASI · SEED VE ÖZET TABLOSU

| # | sayfa | panel | ne | öncelik | seed | SHA-256 | durum |
|---|---|:--:|---|---|---|---|---|
| R1 | Nora (Astronot) | 4 | EVA basınç giysisi, kask, sırt, eldiven | 🔴 ZORUNLU | KİLİTLİ | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 | ONAYLI |
| R2 | ORISON İstasyonu | 4 | Dönen halka, kopuk geçit, merkez kapsül | 🔴 ZORUNLU | KİLİTLİ | d4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35 | ONAYLI |
| R3 | Bakım Arabası | 4 | Sarı çelik şasi, ray tekerleri, konsol | 🟠 S06'dan önce | KİLİTLİ | 4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a | ONAYLI |
| R4 | Turuncu Anahtar | 2 | Açık ağızlı ağır çelik montaj anahtarı | 🟠 S00'dan önce | KİLİTLİ | ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d | ONAYLI |

---

## 3. 📦 VARLIK ENVANTERİ

| kod | varlık | tip | ilk sahne | son sahne | sayfa | AI risk sınıfı |
|---|---|---|---|---|---|---|
| AST-NORA | Nora | insan (tek astronot) | S00 | S23 | R1 | Sınıf 1 (Kritik Giysi Kimliği) |
| STA-ORISON | ORISON İstasyonu | dev mimari / mekân | S00 | S23 | R2 | Sınıf 2 (Geometrik Ölçek) |
| VEH-CART | Bakım Arabası | araç | S06 | S12 | R3 | Sınıf 2 (Mekanik Yönelim) |
| PRP-WRENCH | Turuncu Anahtar | prop / eşya | S00 | S23 | R4 | Sınıf 3 (Renk ve Form) |

---

## 4. 🪜 DURUM MERDİVENİ / ÇİFTİ

| varlık | durum kodu | ne değişti | başlangıç sahnesi | dönüşüm sahnesi | panel |
|---|---|---|---|---|---|
| AST-NORA | K0 (temel) | Sağlam EVA giysisi, temiz beyaz zırh plakası | S00 | — | R1 p1-p4 |
| AST-NORA | K1 (aşınmış) | Çizilmiş göğüs zırhı, aşınmış turuncu bileklik | S08 | S12 | R1 p1 |
| PRP-WRENCH | K0 (temel) | Canlı güvenlik turuncusu çelik anahtar | S00 | — | R4 p1-p2 |

---

## 5. 🗺️ SAHNE → REFERANS EŞLEME

| sahne | iç/dış + ışık fazı | yüklenecek KIRPIM (+panel) | görünüm | durum | metne devredilen |
|---|---|---|---|---|---|
| S00 | Dış / Sert güneş | R1 p4 (eldiven), R4 p1 (anahtar) | MCU | K0 | Teğetsel fırlama vektörü |
| S01 | Dış / Sert güneş | R2 p1 (istasyon), R2 p3 (geçit) | ELS | K0 | 0.08 rad/s açısal dönüş hızı |
| S02 | İç / Soğuk koridor | R1 p1 (tam boy), R1 p3 (sırt) | MS | K0 | 0.065g yapay yerçekimi yürüyüşü |
| S03 | Dış / Çift ışık | R1 p1 (tam boy), R2 p3 (uçurum) | EWS | K0 | Uçurum kenarı duruşu |
| S04 | Dış / Çift ışık | R1 p4 (eller), R2 p3 (uçurum) | EWS | K0 | Telsiz bırakış mekaniği |
| S05 | Dış / Boşluk | R2 p1 (merkez kapsül) | MS | K0 | Teğet sapma yörüngesi |
| S06 | İç / Ray hattı | R1 p1 (tam boy), R3 p1 (araba) | MS | K0 | Koridorda arabaya yönelme |
| S07 | İç / Gösterge | R1 p4 (eller), R3 p3 (konsol) | CU | K0 | Hız ibresi kontrolü |
| S08 | İç / Ray hattı | R1 p1 (tam boy), R3 p2 (şasi) | MS | K1 | Ayak kilit mandalı eylemi |
| S09 | İç / Hızlanma | R1 p1 (tam boy), R3 p2 (şasi) | CU | K1 | Ters sürüş ivmelenmesi |
| S10 | İç / Hızlanma | R3 p3 (konsol), R1 p4 (eller) | CU | K1 | 8 m/s hız kilitlenmesi |
| S11 | İç / Durgunluk | R1 p3 (sırt), R2 p4 (merkez) | MS | K1 | Dış merkezin donması algısı |
| S12 | Dış / Ayrılma | R1 p3 (sırt), R3 p1 (araba) | WS | K1 | Arabayı raydan çıkarma itişi |
| S13 | Dış / Boşluk | R1 p1 (tam boy), R2 p1 (istasyon) | EWS | K1 | Sıfır hızda havada asılı kalma |
| S14 | Dış / Boşluk | R1 p2 (profil), R2 p4 (kapsül) | MS | K1 | Kapsüle hedeflenmiş çömelme |
| S15 | Dış / Boşluk | R1 p1 (tam boy), R2 p3 (geçit) | EWS | K1 | 2 m/s patlayıcı bacak itişi |
| S16 | Dış / Boşluk | R1 p1 (tam boy), R2 p1 (istasyon) | EWS | K1 | Halka girdabı içinde süzülüş |
| S17 | Dış / Doruk | R1 p1 (tam boy), R2 p1 (istasyon) | MS | K1 | Durgun Nokta anı ve denge |
| S18 | Dış / Dinginlik | R1 p4 (eller), R4 p1 (anahtar) | MS | K1 | Anahtarla paralel süzülüş |
| S19 | Dış / Yaklaşma | R1 p4 (kollar), R2 p4 (kapsül) | WS | K1 | Kapsül demirlerine uzanma |
| S20 | Dış / Temas | R1 p4 (eller), R2 p4 (korkuluk) | MS | K1 | Metal korkuluğu kavrama darbesi |
| S21 | Dış / Sabitleme | R1 p1 (tam boy), R2 p4 (kilit) | WS | K1 | Bacakları gövdeye dolama |
| S22 | İç / Hava kilidi | R1 p1 (tam boy), R2 p4 (kapak) | WS | K1 | Dış kapağı kapatıp mühürleme |
| S23 | İç / Kabin | R1 p4 (eller), R4 p1 (anahtar) | MS | K1 | Kabin içinde dingin süzülüş |

---

## 6. 📸 REFERANS SAYFALARI

### 📸 IMAGE PROMPT — SAYFA R1 · NORA (ASTRONAUT CHARACTER REFERENCE)

```
IN FRAME: full body, back, hands
A character sheet displaying four clean orthographic views of a solo astronaut named Nora in an advanced pressurized extravehicular activity suit.

Panel 1 shows a three-quarter full-body standing pose facing forward in a dark slate-grey ballistic fabric EVA pressure suit. Rigid matte-white ceramic armor plates cover the shoulders and upper chest. A bold hazard-orange band encircles the right forearm completely. Heavy articulated knee and elbow joints feature reinforced black composite accordion bellows. Panel 2 shows a clean side profile illustrating the narrow helmet collar and torso proportions. Panel 3 shows the rear view: the back of the suit is one continuous smooth panel from collar to hip, carrying a compact integrated life-support pack, and the back silhouette is flat. Panel 4 shows a close-up of the helmet: the helmet visor has zero tint transparency, completely opaque gloss black with no interior light and no visible human face.

CAMERA: 50mm prime studio lens, neutral eye-level perspective, seamless medium neutral grey background with balanced soft studio fill lighting.

NEGATIVE: Exactly 1 human character, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI look, no airbrushing. Equipment and clothing identical throughout, no drift. Hand-to-surface contact keeps a clear boundary, no extra fingers. The helmet visor has zero tint transparency, completely opaque gloss black with no interior light and no visible human face. The suit has a flat back silhouette with no giant back-mounted life-support pack.

Output: 16:9, 4K, no text, no watermark.
```

### 📸 IMAGE PROMPT — SAYFA R2 · ORISON STATION (SPACE STATION REFERENCE)

```
IN FRAME: none
An architectural reference sheet displaying four technical views of the monumental ORISON orbital space station rotating near Saturn.

Panel 1 presents a full exterior wide establishing view of the complete station: a massive circular outer habitat ring of one hundred metres radius linked by four primary structural spokes to a stationary cylindrical central escape hub. Deep golden Saturn and sharp planar ice rings fill the black cosmic space behind the structure. Panel 2 presents an interior view of the curving habitat ring tunnel with steel deck grates and maintenance conduit tracks. Panel 3 details the sheared transit catwalk, showing twisted structural I-beams protruding into ninety metres of empty space between ring and hub. Panel 4 displays the stationary white central escape capsule module with reinforced yellow docking collar rings.

CAMERA: 24mm architectural cinema prime lens, neutral multi-angle framing, deep focus across all panels under harsh direct directional solar illumination.

NEGATIVE: Exactly 0 humans, no people in frame. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI look, no airbrushing. Station geometry identical throughout, no drift. No melting structures, no flickering geometry. Deep space vacuum, no atmospheric haze, no clouds, no lens flare.

Output: 16:9, 4K, no text, no watermark.
```

### 📸 IMAGE PROMPT — SAYFA R3 · MAINTENANCE CART (VEHICLE REFERENCE)

```
IN FRAME: none
A technical vehicle reference sheet showcasing four distinct orthographic angles of the open-frame electric rail inspection cart.

Panel 1 exhibits a three-quarter perspective of the compact industrial maintenance vehicle mounted upon dual steel track rails. The vehicle is oriented facing screen-left, its bow heading along the counter-rotation track. The chassis features welded tubular steel railings finished in faded industrial safety yellow with weathered edges. Panel 2 presents a true lateral side profile detailing four solid flange-fitted steel wheels and heavy underside guide brackets. Panel 3 shows a close-up of the control console equipped with mechanical reverse drive levers, brass locking pins, and a round analog speedometer gauge dial. Panel 4 provides a mechanical detail of the quick-release guide shoe levers and emergency decoupling clamps.

CAMERA: 35mm technical macro lens, crisp studio product lighting against a matte neutral charcoal backdrop, high depth of field across mechanical components.

NEGATIVE: Exactly 0 humans, no people in frame. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI look, no airbrushing. Vehicle geometry identical throughout, no drift. No melting structures, no flickering geometry.

Output: 16:9, 4K, no text, no watermark.
```

### 📸 IMAGE PROMPT — SAYFA R4 · ORANGE HEAVY WRENCH (PROP REFERENCE)

```
IN FRAME: none
A photographic reference sheet displaying two detailed views of a heavy industrial open-end structural assembly wrench.

Panel 1 presents an isometric studio view of the single-piece forged steel hand tool. The entire tool body is coated in durable, matte hazard-orange industrial epoxy paint, displaying minor realistic cosmetic abrasions on the clamping jaws. The tool measures forty-five centimetres in length with a thick rectangular grip shaft and an angled fifteen-degree open jaw head. Panel 2 presents an extreme close-up view of the tool head, highlighting solid forged steel construction, chamfered jaw edges, and a lanyard attachment hole through the base of the handle. Floating in zero-gravity orientation with clean mechanical shadows.

CAMERA: 50mm macro cinema lens, balanced multi-point soft studio lighting against an uncluttered neutral medium grey backdrop, edge sharpness preserved.

NEGATIVE: Exactly 0 humans, no people in frame. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits, numbers or symbols on any display, surface, patch or sign, no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI look, no airbrushing. Tool geometry identical throughout, no drift.

Output: 16:9, 4K, no text, no watermark.
```
