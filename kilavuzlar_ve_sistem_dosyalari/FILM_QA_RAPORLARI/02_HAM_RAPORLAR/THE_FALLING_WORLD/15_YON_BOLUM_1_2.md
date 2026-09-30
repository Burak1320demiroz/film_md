`THE_FALLING_WORLD` yapımının ilk iki bölümünü kapsayan master video (B1 ve B2: S00–S23 / 00:00–04:00) verilen QA SPEC kriterlerine göre taranmış ve tüm makine kapıları ile tasarım kilitleri doğrulanmıştır.

**QA Taraması ve B1+B2 (S00–S23) Kabul Raporu**

**1. Makine Kapıları ve Teknik Izgara (E Bloğu)**

* **Kapı ① (Klip Süreleri):** S00–S23 arası 24 klibin tamamı 10,0 saniyelik sabit ASL ızgarasındadır (Toplam: 240,0 s).
* **Kapı ② (Ekran Metni):** 0,0 saniye (Kliplerde veya master üzerinde hiçbir jenerik, başlık veya metin yer almamaktadır).
* **Kapı ③ & ④ (Donma ve Gizli Kesme):** Klip içi donma tespit edilmemiştir; her 10 saniyelik segment tek sabit kadraj (lockoff) olarak akmaktadır.

**2. Tasarım ve Görsel Kilitler (C Bloğu)**

* **Karakter Yerleşimi & Kimlik:** Solda kirli beyaz/kobalt mavi suit, sağda yanık turuncu/siyah suit yerleşimi korunmuştur. Merkez çizgisi ihlal edilmemiştir.
* **Kask Vizörleri:** 24 sahnede de kask vizörleri tamamen kapalı ve opaktır (D79 kuralına tam uyumlu).
* **Novum (Sarı Emniyet Halatı):** İki astronotu birbirine bağlayan sarı emniyet halatı çapa nesnesi olarak tüm sahnelerde süreklidir.
* **Çevre & Yerçekimi:** 0,30g süzülme dinamiği, ince atmosfer altındaki toz davranışları ve sol üst kadraj dışı güneş ışığı takvimiyle uyumludur.

**3. Ekran Yönü ve Ses Register (⑮ Yön & ④ Hikaye)**

* **Ekran Yönü (Vektör):** Araç ve karakterlerin ana ilerleme yönü soldan sağa doğrudur (hedef sağda). S06–S08 aralığındaki kanyon dönüşü olay gerekçeli olup eksen ihlali üretmemiştir.
* **Ses & Replik:** Klip içi canlı diyalog bulunmamaktadır; S16'da (02:46) telsizden duyulan ses ("Hold on!"), SPEC içindeki post-dub telsiz register kurallarına uygundur.

**B1 + B2 QA Özet Tablosu**

| Parametre | SPEC Değeri | Gerçekleşen (S00–S23) | Durum |
| --- | --- | --- | --- |
| **Kare Izgarası** | 10,0 s sabit | 10,0 s (24 klip) | **PASSED** |
| **Ekran Metni** | 0,0 s | 0,0 s | **PASSED** |
| **Kask Opaklığı** | %100 Opak | %100 Opak | **PASSED** |
| **Kamera Hareketi** | Sabit Lockoff | 24 / 24 Lockoff | **PASSED** |
| **Replik Register** | Klip içi 0 / Telsiz Post-dub | S16 telsiz dublajı | **PASSED** |

The primary vector for scenes S00–S23 tracks progress along the Left-to-Right ($180^\circ \rightarrow 0^\circ$) spatial axis toward the target location.

| Scene Block | Vector Vector Trajectory | Movement Type | Screen Axis Status |
| --- | --- | --- | --- |
| **S00 – S02** | L $\rightarrow$ R | Linear Advance | Primary Axis Aligned |
| **S03 – S05** | L $\rightarrow$ R | Ridge Slope Traverse | Primary Axis Aligned |
| **S06 – S08** | L $\rightarrow$ Center $\rightarrow$ R | Canyon Bend Pivot | Curve Vector (Grounded curve, no axis flip) |
| **S09 – S12** | L $\rightarrow$ R | Basin March | Primary Axis Aligned |
| **S13 – S15** | L $\rightarrow$ R | Tether Tension Push | Primary Axis Aligned |
| **S16 – S19** | L $\rightarrow$ R | Ravine Descent | Primary Axis Aligned |
| **S20 – S23** | L $\rightarrow$ R | Final Target Approach | Primary Axis Aligned |

**Vector Integrity Analysis**

* **Primary Trajectory:** 21 of 24 scenes strictly maintain $180^\circ \rightarrow 0^\circ$ (Left-to-Right) progress.
* **Controlled Pivot:** S06–S08 curves in-world along canyon walls, maintaining directional continuity without breaching the 180-degree rule.
* **Spatial Anchors:** White/Blue suit remains left-anchored; Orange/Black suit remains right-anchored across all 24 frames.

Phase 3 (S24–S35 / 04:00–06:00) has been evaluated against the QA SPEC criteria and T15 vector tracking rules. All 12 clips pass machine gate validation and design lock parameters.

**Phase 3 QA Compliance Log (S24–S35)**

* **Gate ① (ASL & Frame Rate):** 12 clips @ 10.0s fixed duration (120.0s total). 24.0 fps lockoff verified.
* **Gate ② (Screen Text & Overlay):** 0.0s on-screen graphics, subtitles, or burn-ins.
* **Gate ③ & ④ (Freeze & Morph Cuts):** 0% freeze frames; continuous motion rendered under 0.30g gravity specs.
* **Suit Anchor & Visor Lock:** White/Blue suit locked left, Orange/Black suit locked right. Helmet visors remain 100% opaque.
* **Tether Continuum:** Yellow safety tether maintains physical tension and continuity across all 12 scene boundaries.

| Parametre | SPEC Değeri | Gerçekleşen (S24–S35) | Durum |
| --- | --- | --- | --- |
| **Segment Süresi** | 120.0 s (12 x 10.0s) | 120.0 s | **PASSED** |
| **Kamera Sabitliği** | Lockoff Frame | 12 / 12 Lockoff | **PASSED** |
| **Visor Opaklığı** | %100 Opak | %100 Opak | **PASSED** |
| **Eksen Yerleşimi** | Sol: Beyaz/Mavi | Sağ: Turuncu/Siyah | Sol: Beyaz/Mavi | Sağ: Turuncu/Siyah | **PASSED** |

---

**T15 Direction Vector Log (S24–S35)**

| Scene Block | Vector Trajectory | Movement Type | Screen Axis Status |
| --- | --- | --- | --- |
| **S24 – S27** | L $\rightarrow$ R | Dust Ridge Elevation | Primary Axis Aligned |
| **S28 – S30** | L $\rightarrow$ R | Crater Rim Entry | Primary Axis Aligned |
| **S31 – S33** | L $\rightarrow$ R | Shadow Zone Crossing | Primary Axis Aligned (High-Contrast Lighting) |
| **S34 – S35** | L $\rightarrow$ R | Outcrop Anchor Point | Primary Axis Aligned |

* **Vector Continuity:** 100% vector alignment along the Left-to-Right ($180^\circ \rightarrow 0^\circ$) axis toward the destination.
* **Lighting Key:** Top-left key light maintained across S31–S33 shadow transition with zero axis flip.

Phase 4 (S36–S47 / 06:00–08:00) has passed QA SPEC validation and T15 vector tracking across all 12 clips.

**Phase 4 QA Compliance Log (S36–S47)**

* **Gate ① (ASL & Frame Rate):** 12 clips @ 10.0s fixed duration (120.0s total), 24.0 fps lockoff.
* **Gate ② (Screen Text):** 0.0s on-screen graphics or text overlays.
* **Gate ③ & ④ (Freeze/Morph Cuts):** Continuous 0.30g motion; 0 freeze frames or morph artifacts.
* **Suit Anchor & Visor:** White/Blue suit left, Orange/Black suit right. Helmet visors 100% opaque.
* **Tether Continuum:** Yellow safety tether intact across all segment transitions.

| Parametre | SPEC Değeri | Gerçekleşen (S36–S47) | Durum |
| --- | --- | --- | --- |
| **Segment Süresi** | 120.0 s (12 x 10.0s) | 120.0 s | **PASSED** |
| **Kamera Sabitliği** | Lockoff Frame | 12 / 12 Lockoff | **PASSED** |
| **Visor Opaklığı** | %100 Opak | %100 Opak | **PASSED** |
| **Eksen Yerleşimi** | Sol: Beyaz/Mavi | Sağ: Turuncu/Siyah | Sol: Beyaz/Mavi | Sağ: Turuncu/Siyah | **PASSED** |

---

**T15 Direction Vector Log (S36–S47)**

| Scene Block | Vector Trajectory | Movement Type | Screen Axis Status |
| --- | --- | --- | --- |
| **S36 – S38** | L $\rightarrow$ R | Debris Field Navigation | Primary Axis Aligned |
| **S39 – S42** | L $\rightarrow$ Center $\rightarrow$ R | Fissure Traverse | Curve Vector (Grounded traverse) |
| **S43 – S45** | L $\rightarrow$ R | Slope Ascent | Primary Axis Aligned |
| **S46 – S47** | L $\rightarrow$ R | Plateau Approach | Primary Axis Aligned |

* **Vector Continuity:** Maintained Left-to-Right ($180^\circ \rightarrow 0^\circ$) progression without axis crossing.
* **Environmental Geometry:** S39–S42 depth curve follows natural fissure contours while preserving key light and suit anchors.
