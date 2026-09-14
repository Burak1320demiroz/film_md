# 📋 THE_STATIC_SHADOW — QA SPEC (rubriklere yapıştırılacak tek dosya)

> **[DERS 117]:** SPEC bir DOSYADIR, bölüm değil. QA anında operatörün eline
> rubrikle birlikte BU dosya verilir; koşu mod D olur.

---

## 🚦 HANGİ RUBRİĞE NE VERİLİR

```
① 🔧 KARE        → A + B BLOĞU                     MOD D
② 🔗 DEVAMLILIK  → hiçbir şey (tasarım gereği)     MOD V
③ 🔊 SES         → hiçbir şey (tasarım gereği)     MOD V
④ 📖 HİKAYE      → A BLOĞU                          MOD D
⑤ 🖼️ ARKA PLAN  → C BLOĞU'nun YALNIZ üç kilidi [D133]
⑥ ⚖️ FİZİK      → C BLOĞU'nun sayısal kilitleri    MOD D
```

---

## 🅰️ A BLOĞU — ④ HİKAYE SPEC

```
FILM:              THE_STATIC_SHADOW
FORMAT:            Yatay 16:9 2-4 dk
RUNTIME:           150 seconds (02:30)
SCENE COUNT:       15
THEME:             İNSAN-MAKİNE VE FEDAKÂRLIK
THEME SCENES:      S04 · S12 · S14
INTENDED EMOTION:  Gerilim, soğukkanlı fedakârlık, kararlılık
ENDING TYPE:       MUĞLAK / COST (Gölge kilitli, teleskop güvende, dönüş yakıtı sıfır)
PROTAGONIST:       Servis teknisyeni (isimsiz, 0 replik)
CENTRAL CHOICE:    S12 — Pilot AI'ın abort emrine uymayıp podu kalkan rayına kenetleme kararı alır.
DIALOGUE LINES:    7 replik (HELIOS AI) · register: HUMAN 0 / MACHINE 7
SILENT SCENES:     S03, S04, S05, S07, S10, S12, S13, S14 (8 sessiz sahne)
VIRAL INTERSTITIALS: S01 (Anomali reveal), S14 (Moment-arm yapışma)
TITLE:             THE STATIC SHADOW — Statik gölge kilitlenmesi
LIBRARY CONTEXT:   Yatay uzay serisi (THE_DEAD_APPROACH, THE_HARD_DOCK)
```

---

## 🅱️ B BLOĞU — ① KARE SPEC

```
VISUAL IDENTITY:   Dark realistic hard sci-fi space aesthetics. High contrast between blinding blue-white stellar light, deep black shadows, and white ceramic pod hull.
PROTAGONIST VISUAL LOCK:
  - EV-Suit: Anthracite gray EV-suit with matte carbon fiber chest plate, yellow and black warning stripes on shoulders.
  - Visor: OPAQUE BLACK MIRRORED VISOR (D197 — no internal face/facial features visible under any lighting).
SPACE POD VISUAL LOCK:
  - Hull: Compact utility pod, matte white ceramic thermal coating, sharp titanium cone nose, yellow RCS thrusters. 1/30 scale of shield.
SUNSHIELD VISUAL LOCK:
  - Shield: 500-meter flat octagonal carbon-ceramic panel, dark gray-black metallic rim with titanium-tantalum capture rail.
TELECOPE VISUAL LOCK:
  - Observatory: 80-meter cylindrical silver-gold foil wrapped cryogenic telescope.
```

---

## 🅲 C BLOĞU — ⑤ ARKA PLAN VE ⑥ FİZİK KİLİTLERİ

```
NUMERIC FIZIK KİLİTLERİ:
  - Sunshield rotation speed: ~0.008 rad/s (0.046 rpm, slow wobble, edge speed ~4 m/s). NOT fast spinning.
  - Impact dynamics: Galling, plastic deformation, and vacuum cold adhesion. Pod becomes a rigid 15-meter moment arm.
  - Thermal physics: Radiative flux beyond manipulator qualification. Vacuum thermal radiation. NO melting metal cliché.
  - Vacuum sound physics: Exterior cameras = ABSOLUTE SILENCE (zero sound, cold gas RCS plumes visible without sound). Interior cameras = structural contact vibrations and valve clicks only.
  - Visor rule: 100% opaque black mirrored visor throughout the entire film (D197).
```

---

## 🎬 SAHNE SPESİFİKASYONU

| S | Sahne | Kurulum | Kilit / Karakter | Ses / Replik |
|---|---|---|---|---|
| S01 | Kalkan Yalpalama | 24mm EWS alt | Dev kalkan yalpalar (~0.008 rad/s) | HELIOS telemetri |
| S02 | Teleskop Tehdidi | 35mm OTS göz | Kriyojenik teleskop parıltı altında | HELIOS sıcaklık uyarısı |
| S03 | İrade Kilitlenmesi | 85mm CU ön | Opak aynalı vizörde retikül | Kask nefesi |
| S04 | Alışkanlık Jesti | 50mm ECU üst | Öteleme koluna 2 tıklatma | Mekanik klik (iç) |
| S05 | Hizalanma | 35mm MS yan | Pod kalkan kenarına yanaşır | Dış sessizlik |
| S06 | Oran Karesi | 18mm EWS üst | Pod shield'in 1/30'u boyutta | HELIOS yaklaşma telemetrisi |
| S07 | İlk Başarısızlık | 50mm MCU yan | Pod nose rail'den geri teper | Dış sessizlik / iç sarsıntı |
| S08 | Kaçan Pencere | 35mm OTS göz | Gölge kayar, kabinde amber alarm | HELIOS süre uyarısı |
| S09 | Sensör Kaybı | 24mm FS alt | Particle event pod telemetrisini bozar | HELIOS telemetri cızırtısı |
| S10 | Tereddüt | 85mm CU ön | Opak vizörde İPTAL kolu yansıması | Hızlı nefes |
| S11 | Abort Emri | 35mm OTS göz | AI abort emri verir, pilot tensed | HELIOS "Abort" |
| S12 | Karar / Kırılma | 50mm ECU üst | Tıklatmasız acil kapağı açma | Sert mekanik kapak sesi |
| S13 | Karlı Hücum | 24mm WIDE arka | Ana iticiler kalkan rail'ine | İtki bas sarsıntısı (iç) |
| S14 | Moment Kolu | 35mm MS yan | Galling + yapışma, pod tork uygular | Dış sessizlik + iç nefes |
| S15 | Durgun Gölge | 35mm OTS göz | Gölge sabit, SHADOW ERROR: 0.000 | HELIOS "Shadow lock stabilized" |
