# 🔊 F4 — Ses Tasarımcısı Raporu (Tur 1)

**Film:** `yatay_2_dk_filmler/THE_SNAP_LINE`  
**Girdi:** `FILM.md` §1–§5 · `ODA/F2_ses_notlari.md`

---

## 1. SES KATMANLARI VE STRATEJİSİ
* **Katman 1 (Ortam Yatağı):** Zifiri karanlık okyanus tabanı kütlesel su basıncı (30–60 Hz sub-rumble). C01–C12 boyunca kesintisiz akar.
* **Katman 2 (Mekanik Gerilim):** Kordonun yay gibi gerilmesi ve hidrolik vinç iniltisi (C03–C09). Frekansı yükselerek tansiyonu kurar.
* **Katman 3 (Efektler / SFX):** Manometre ibre tıkırtısı, fışkıran kabarcık jeti, kask içi regülatör soluğu, makas çene sıkışması, kordon kopma patlaması, acil tüp tıslaması, silt çamuru çarpması.
* **Katman 4 (Replikler):** Model sesiyle klipten gelen kask içi mikrofon ve güverte telsiz sesleri.

---

## 2. ORTAM YATAĞI TABLOSU

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | Sualtı Taban | C01–C12 | Continuous deep ocean sub-bass ambient rumble at 310 meters with distant muffled metallic pipe groans | −18 dB | `yatak_sualti_taban.wav` |
| Y2 | Kordon Gerilim | C03–C09 | Strained taut steel wire hum and hydraulic winch motor whine slowly rising in acoustic pitch | −22 dB | `yatak_kordon_gerilim.wav` |

---

## 3. GEÇİŞ TABLOSU (Kesme Sürekliliği)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01 → C02 | kesme | J-cut (0.8 s nefes) | Manometreden kask içine geçerken Miller'ın soluk sesi kesmeden önce girer |
| C02 → C03 | kesme | L-cut (0.5 s telsiz) | Kask telsiz mandal sesi gerilen kordon planına akar |
| C03 → C04 | kesme | — | Dalgıcın savrulması ile flanşı yakalaması sert kesmeyle vurulur |
| C04 → C05 | kesme | J-cut (0.6 s vinç gıcırtısı) | Tamburun arıza iniltisi dalgıç planının sonunda duyulmaya başlar |
| C05 → C06 | kesme | L-cut (0.5 s mekanik inilti) | Vinç tambur sesi derinlik saatine akar |
| C06 → C07 | kesme | L-cut (0.4 s nefes) | Miller'ın acı iniltisi makasa uzanışa sarkar |
| C07 → C08 | kesme | — | Makasın kordona oturması mekanik sert vuruşla kesilir |
| C08 → C09 | kesme | — | Tetiğin sıkılması anında kabarcık patlamasına ani geçiş |
| C09 → C10 | kesme | ani patlama ardından 1.5 s boşluk | Kordon koptuğunda devasa bir hava/su patlaması ve hemen ardından derin düşüş sessizliği |
| C10 → C11 | kesme | J-cut (0.5 s gaz tıslaması) | Acil durum tüpünün devreye girişi düşüş planında başlar |
| C11 → C12 | karisim (0.5 s) | L-cut (0.8 s düzenli soluk) | Acil havanın tıslaması taban çamuruna çarpışa ve finale akar |

---

## 4. EFEKT LİSTESİ (Çekim Başına SFX)

* **C01:** `E01_gauge_tick.wav` (metalik ibre titreşimi), `E02_gasket_hiss.wav` (yüksek basınçlı sualtı gaz kabarcığı fışkırması).
* **C02:** `E03_heavy_breathing.wav` (regülatör diyafram sesi, kask içi buğu tınısı), `E04_chest_tap.wav` (göğüs valfine iki eldiven vuruşu).
* **C03:** `E05_cable_snap_tension.wav` (çelik yay gerilme iniltisi ve sualtı boşalma dalgası).
* **C04:** `E06_flange_grip_clank.wav` (çelik halkayı kavrayan ağır pirinç eldiven sesi), `E07_chest_tap.wav`.
* **C05:** `E08_winch_grind_chatter.wav` (tambur kilitlenme gıcırtısı ve buhar kabarcığı patlamaları).
* **C06:** `E09_depth_gauge_whir.wav` (hızlı dönen mekanik ibre sesi), `E10_shoulder_strain.wav` (askı kumaşının yırtılma sesi).
* **C07:** `E11_shears_draw.wav` (kılıftan sıyrılan ağır hidrolik çelik sürtünmesi).
* **C08:** `E12_jaw_lock.wav` (makas çenelerinin kordon zırhına kilitlenme sesi), `E13_trigger_squeeze.wav` (hidrolik tetik tıklaması).
* **C09:** `E14_cable_crush.wav` (çelik örgünün ezilme sesi), `E15_massive_gas_vent.wav` (şiddetli tazyikli gaz ve sıcak su patlaması).
* **C10:** `E16_snap_shockwave.wav` (kordonun ikiye ayrılma şok dalgası), `E17_silent_fall.wav` (alçak frekanslı dikey su sürtünmesi).
* **C11:** `E18_bailout_valve_twist.wav` (metalik vana sürtünmesi), `E19_cold_gas_rush.wav` (kask içine dolan soğuk kuru gaz tıslaması).
* **C12:** `E20_mud_impact_thud.wav` (silt çamuruna boğuk çarpma sesi), `E21_steady_bailout_breaths.wav` (yavaşlayan düzenli mekanik nefes).
