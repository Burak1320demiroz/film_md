# 📄 THE CANOPY WORLD — MANTIK VE DEVAMLILIK QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 31 Temmuz 2026 · **Skor:** 5/10 · **Durum:** ✅ GEÇERLİ
> **Eş rapor:** aynı gün aynı filme teknik QA da yapıldı →
> [`THE_CANOPY_WORLD_TEKNIK_HAM.md`](THE_CANOPY_WORLD_TEKNIK_HAM.md)

---

## ✅ KAPSAM SINIRI İLK KEZ SINANDI — VE TUTTU

Bu, **aynı filme aynı gün iki farklı rubriğin uygulandığı ilk vaka.**
Rubrik tasarımının tek iddiası şuydu: *"kapsam sınırı blokları sayesinde
aynı hata iki kez sayılmaz."* Test sonucu:

| Bulgu | TEKNİK QA | MANTIK QA | Çakışma |
|---|---|---|---|
| 0:20 sert kesme | 🔴 BLOCKER | — (kapsam dışı) | ✅ yok |
| 1:06 canlı morphu | 🔴 BLOCKER | — | ✅ yok |
| 1:12 AI bloom | 🟠 MAJOR | out-of-scope satırı | ✅ yok |
| 2:10 jenerik metni | 🔴 BLOCKER | S13 envanterine yazdı, puanlamadı | ✅ yok |
| Suit ıslaklığı sıfırlanması | — | 🟠 MAJOR | ✅ yok |
| Kanat/emniyet kemeri | — | 🟠/🟡 | ✅ yok |

**Sıfır çift sayım.** İki rapor toplanabilir. Kural işliyor.

---

# 🔎 DOKÜMAN KONTROLÜ — raporun sorduğu 2 sorunun cevabı

Kaynak: `yatay_2_4_dk_filmler_uzay/THE_CANOPY_WORLD_PLANET_FILM.md`

### ❓ Soru 1 — "Sürekli doğrusal iniş mi, yoksa doğrusal olmayan keşif montajı mı?"

**CEVAP: SÜREKLİ DOĞRUSAL İNİŞ. Tartışmasız.**

```
Başlık:      "Katmanlı Orman Gezegeni"
Slogan:      "Her katman farklı bir dünya. Aşağı indikçe kurallar değişiyor."
Karakter:    "the first human to descend Verdana's full seven-layer canopy
              in a SINGLE CONTINUOUS EXPEDITION"
Dünya kuralı: 7 katman, yukarıdan aşağıya — 3.000m → 0m
```

**Ve kurgu sırası PLANLA BİREBİR AYNI.** 12 sahnenin 12'si, plandaki
sırada:

| Kurgu | Plan sahnesi | Katman |
|---|---|---|
| 0:00 | S0 HOOK — yedi katman içinde düşüş | tümü |
| 0:10 | S1 iniş: gemi sarmaşık | Taç |
| 0:20 | S2 taç katmanı: yapraklar üzerinde koşu | 3.000m |
| 0:30 | S2.5 viral: kanopiden atlayış | ↓ |
| 0:40 | S3 rüzgar koridoru: dal koşucuları | 1.500m |
| 0:50 | S4 sis kuşağı: mantar platformları | 1.000m |
| 1:00 | S5 yosun katedrali: iniş | 500m |
| 1:10 | S5.5 viral: ışık dalgası | ↓ |
| 1:20 | S6 karanlık katman: ışık avcıları | 200m |
| 1:30 | S7 kök labirenti: kristal havuzlar | 50m |
| 1:38 | S8 sürüklenme: yeraltı nehri | 50m |
| 1:50 | S9 zemin: nefes alan yer | 0m |

## 🚨 BU CEVAP RAPORUN EN ÖNEMLİ ÖNERİSİNİ ÇÜRÜTÜYOR

Rapor şunu önerdi:

> *"Cheapest fix: Re-edit scene order to group all sunlit daylight scenes
> together first, followed by dark/bioluminescent scenes."*
> Maliyet: **Low (Edit pass only)**

**Bu öneri uygulanamaz ve maliyet tahmini yanlış:**

```
❌ Kurgu sırası zaten doğru — plandaki sırayla birebir aynı.
❌ Sahneleri ışığa göre gruplamak, filmin ÖNERMESİNİ yok eder.
   Film "yukarıdan aşağıya iniş" filmi; sıra = irtifa.
❌ Maliyet "Low / edit pass" değil.

✅ GERÇEK SORUN: bir sahne KENDİ KATMANININ IŞIĞIYLA üretilmemiş.
   Kök Labirenti'nin (1:38) LIGHTING BIBLE'ı birebir şöyle diyor:
       "Cold blue-white light refracting through the crystal pools"
   Rapor orada "bright sunlit mangrove stream" görüyor.
   → Bu bir KURGU hatası değil, ÜRETİM hatası.
   → Maliyet: o sahnenin yeniden üretilmesi.
```

**Ders:** Doğru teşhis + yanlış reçete. Rapor ışık salınımını **doğru
gördü**, ama dokümansız olduğu için sebebini kurguda aradı. Sebep üretimde.

### ❓ Soru 2 — "Dünya bible'ı katmana göre atmosfer yoğunluğu / süzülme fiziği tanımlıyor mu?"

**CEVAP: İKİYE AYIRMAK GEREKİYOR — biri tasarım, biri hata.**

```
✅ HAVADA YÜZEN CANLILAR = TASARIM, hata değil
   Sis Kuşağı (1.000m): "MIST JELLYFISH — 5-meter translucent,
   GAS-BLADDER drifting creatures that feed on airborne moisture"
   Karanlık Katman (200m): "LIGHT HUNTERS — 3-meter anglerfish-analog
   predators that hunt using their own bioluminescent lure"
   → İkisi de biyolojik olarak gerekçelendirilmiş. Doğru üretilmişler.

🚨 KARAKTERİN SÜZÜLMESİ = HATA
   Physics Bible satır 267:  "Gravity: 0.85g FIXED THROUGHOUT."
   Physics Bible satır 284:  "The character MUST NEVER FLOAT."
   → Raporun 0:53'te gördüğü "floaty, near-zero-g motion" doğrudan
     bir Bible ihlali. Katmana göre yerçekimi YOK — 0.85g sabit.
   → Bu Ders 4 (kayma ve süzülme) ve Ders 15 (imkansız fizik) kapsamında.
```

---

# ⚖️ RAPORUN 3 KOSTÜM BULGUSU — belge karşısında biri ayakta kaldı

Character Bible'ın SUIT bölümü üçünü de doğrudan cevaplıyor:

### ❌ 1. Kanat membranı (0:30 vs 0:40) — REDDEDİLDİ

```
Bible: "a thin, foldable wing-membrane integrated into the suit's underarms
        and sides, DEPLOYABLE ONLY FOR CONTROLLED GLIDING between layers,
        never a separate garment"
```

Membranın süzülürken açık, halatta kapalı olması **doğru davranış.**
Rapor bunu 🟠 MAJOR çelişki saydı — değil. En fazla "açılma/kapanma anı
gösterilmiyor" diye OPEN THREAD olurdu.

### ❌ 2. Halatın kaybolması — REDDEDİLDİ

```
Bible: "an integrated, SPRING-LOADED ROPE REEL — the rope DEPLOYS AND
        RETRACTS AUTOMATICALLY; it is never coiled or carried loose by hand"
```

Halatın sahneler arası görünmemesi tasarım. Otomatik toplanıyor.

### ✅ 3. Emniyet kemerinin kaybolması (0:52) — KABUL, hatta YÜKSELTİLDİ

```
Bible: "a COMPACT HARNESS AT HIP AND CHEST with an integrated ... reel"
```

Kemer kalıcı ekipman — halat gibi toplanmıyor. 0:52'de yok olması gerçek
bir devamlılık hatası. **Rapor buna 🟡 MINOR demiş; belgeye göre üç
kostüm bulgusundan tek gerçek olan bu. 🟠 MAJOR'a yükseltildi.**

### ✅ 4. Suit ıslaklığının sıfırlanması (1:42 → 1:52) — KABUL, belgeyle güçlendi

```
Bible: "a fully transparent, seamless visor ... fogging faintly in the Mist
        Belt, BEADING WITH MOISTURE IN THE ROOT LABYRINTH"
```

Bible ıslaklığı **katmana bağlı bir durum olarak zaten tanımlamış.**
Yeraltı nehrinden çıkıp kupkuru görünmek hem kendi içinde çelişki hem de
Bible ihlali. Raporun en sağlam bulgusu.

---

# 📌 SONUÇ — bulguların belge sonrası hali

```
RAPORUN DEDİĞİ                          BELGE SONRASI
────────────────────────────────────────────────────────────────
🟠 Kanat membranı çelişkisi        →    ❌ REDDEDİLDİ (tasarım)
🟠 Işık salınımı, kurguda düzeltilir →   ⚠️ TEŞHİS DOĞRU, REÇETE YANLIŞ
                                          (üretim hatası, kurgu değil)
🟠 Suit ıslaklığı sıfırlanması      →    ✅ KABUL, belgeyle güçlendi
🟡 Emniyet kemeri kayboluyor        →    ✅ KABUL, 🟠'a YÜKSELTİLDİ
🟡 Karakterin süzülmesi             →    ✅ KABUL, 🟠'a YÜKSELTİLDİ
                                          (0.85g sabit, "must never float")
🟡 Geminin transit görülmeden yer
   değiştirmesi                     →    ⚠️ AÇIK — plan iniş aracını
                                          katmanlar arası taşıyıcı sayıyor
```

**Skor 5/10 duruyor** — reddedilen bulgu kadar yükseltilen bulgu var.

---

# 📥 HAM ÇIKTI (değiştirilmeden)

FILM: The Canopy World
RUNTIME: 02:15 · SCENES OBSERVED: 13
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees with itself, not whether it matches its design.

OVERALL SCORE: 5/10
VERDICT: FIXABLE IN EDIT

## STEP 1 — BASELINE INVENTORY

### SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
|---|---|---|---|---|---|
| S1 | 00:00-00:09 | Dark Canopy / Mist | Character | Gliding down through mist and giant mushroom pillars | None |
| S2 | 00:10-00:19 | Upper Canopy (Above clouds) | Sci-fi Ship, Drake | White mechanical ship perches on giant limb above cloud sea | None |
| S3 | 00:20-00:29 | Cloud Level / Giant Leaves | Character, Drakes | Character runs across massive leaves and leaps off cliff edge | None |
| S4 | 00:30-00:39 | Upper Canopy Airspace | Character, Dragon | Character glides alongside a large winged creature | None |
| S5 | 00:40-00:49 | Sunlit Mid-Canopy | Character, Monkeys | Character swings on rope attached to giant tree trunks | None |
| S6 | 00:50-00:59 | Foggy Mushroom Strata | Character, Jellyfish | Character leaps between floating mushroom caps in dense mist | None |
| S7 | 01:00-01:09 | Sunlit Mid-Forest | Character, Moss Beast | Character rappels down rope while a large creature walks in background | None |
| S8 | 01:10-01:19 | Moss Wall Interior | Character | Character touches glowing moss wall, triggering luminescent ring | None |
| S9 | 01:20-01:29 | Dark Understory | Character, Anglerfish | Character hides behind tree trunk near floating glowing fish | None |
| S10 | 01:30-01:37 | Shaded Stream / Roots | Character, Glass Crabs | Character crouches on root observing transparent crabs in water | None |
| S11 | 01:38-01:49 | Sunlit Mangrove Stream | Character | Character swims/crawls through stream enclosed by large roots | None |
| S12 | 01:50-02:09 | Deep Subterranean Core | Character, Lander Ship | Character walks and kneels on glowing root floor under lander | None |
| S13 | 02:10-02:15 | Title Screen | N/A | Title card graphic showing vertical strata of Canopy World | None |

### THE CHARACTER — as first clearly seen

Face: Female, fair skin, light brown/reddish hair braided in a single rear braid; wears clear bubble helmet visor. First fully visible: S1 (00:01).
Suit: Full-body olive/emerald green suit with bright yellow/neon accent stripes along the torso, arms, and legs.
Wear/dirt: Clean green fabric throughout upper scenes. Fully submerged in water in S11 (01:40).
Equipment: Clear full-head helmet visor, dark green gloves, wingsuit underarm flaps (S1, S4), climbing harness and rope (S5, S7).

### THE WORLD — as the film shows it

Gravity read: Earth-like in S3/S5/S7 (running, rope swinging, rappelling); low-g/floaty in S6 (slow-motion leaping beside floating jellyfish).
Atmosphere read: Dense mist/fog in S1 and S6; clear bright air above clouds in S2–S4; airborne aquatic life (floating jellyfish in S6, floating anglerfish in S9) indicates dense atmosphere or unique biomes.
Light source: Bright direct sunlight in S2–S5 and S7/S11; dim bioluminescent/ambient lighting in S1, S6, S8–S10, and S12.
Locations: Upper Cloud Layer, Sunlit Mid-Canopy, Foggy Mushroom Strata, Dark Understory, Sunlit Mangrove Stream, Deep Subterranean Core.

### THE COUNTER
NONE

### NUMBERS SPOKEN OR SHOWN
NONE

### OBJECTS THAT GET ATTENTION
Sci-Fi Walker/Lander Ship: First appears in S2 (00:10) perched on a branch; reappears hovering in S12 (01:50).
Climbing Harness & Rope: First appears in S5 (00:40); reappears in S7 (01:00).
Glowing Moss / Wall: Appears in S8 (01:10).

## SCORES SUMMARY

| Category | Score | Critical Issue |
|---|:---:|---|
| Physical Consistency | 6/10 | Gravity and air resistance shift between heavy falling (S5) and floating jump (S6). |
| Counter Logic | N/A | NONE |
| Spatial Geography | 5/10 | Unpredictable jumping between bright daylight strata and dark bioluminescent strata. |
| Time & Light Logic | 5/10 | Alternating light conditions (bright sun to dark mist and back to sun) across adjacent scenes. |
| State, Costume & Props | 4/10 | Suit wetness resets instantly after full submersion; harness and wingsuit flaps pop on/off. |
| Causality & Knowledge | 7/10 | Transitions between distinct vertical strata occur without continuous transit steps. |
| Quantity Consistency | 8/10 | No spoken/written numbers; fauna counts remain stable per scene. |
| Setup & Abandonment | 7/10 | Climbing gear and wingsuit introduced and used, but stowing/equipping is omitted. |

## SEVERITY TALLY
🔴 BLOCKER: 0   🟠 MAJOR: 3   🟡 MINOR: 3

## COUNTER CURVE
NONE

## LOCATION MAP

| Location (assigned name) | Scenes | Consistent? | Mismatch |
|---|---|---|---|
| Upper Cloud Layer | S2, S3, S4 | CONTRADICTED | S3 shows bright clear sunlight above cloud sea; S4 switches to grey hazy cloud cover at same altitude. |
| Sunlit Mid-Canopy | S5, S7 | CONSISTENT | Sunlight filtering through high giant trunks. |
| Foggy Mushroom Strata | S1, S6 | CONTRADICTED | S1 shows dark blue/green deep fog; S6 shows bright white cloud fog with airborne jellyfish. |
| Dark Understory / Cave | S8, S9, S10 | CONSISTENT | Dark ambient environment with localized bioluminescence. |
| Sunlit Mangrove Stream | S11 | CONTRADICTED | S11 introduces full bright daylight inside tree roots directly between dark understory shots. |
| Subterranean Core | S12 | CONSISTENT | Enclosed dark cavern with glowing cracked floor network. |

## DRIFT MAP

| Element | First slip | Undeniable by | Recovered? |
|---|---|---|---|
| Harness & Rope Attachment | 00:50 | 01:10 | No (present in S5 & S7, missing in S6 & S8) |
| Wingsuit Webbing | 00:40 | 00:50 | No (present in S1 & S4, missing in S3 & S5) |
| Suit Wetness State | 01:50 | 01:55 | No (fully wet in S11, completely dry in S12) |

## CONTRADICTION LOG

| Timecode A | Timecode B | Category | What contradicts what | Severity |
|---|---|---|---|---|
| 00:30-00:39 | 00:40-00:49 | State, Costume & Props | Wingsuit underarm webbing is deployed during flight in S4, but completely absent while swinging on rope in S5 without any stowing action shown. | 🟠 MAJOR |
| 01:38-01:49 | 01:50-02:09 | State, Costume & Props | Character is fully submerged and swimming in S11 (01:42); suit, boots, gloves completely dry with zero wet sheen in S12 (01:52). | 🟠 MAJOR |
| 01:20-01:29 | 01:38-01:49 | Time & Light Logic | Environment transitions from pitch-black understory lit only by bioluminescent anglerfish in S9 directly into bright sunlit mangrove waters in S11. | 🟠 MAJOR |
| 00:40-00:49 | 00:50-00:59 | State, Costume & Props | Heavy climbing harness with central waist ring worn in S5 and S7, but disappears during mushroom leaping in S6. | 🟡 MINOR |
| 00:50-00:59 | 01:00-01:09 | Physical Consistency | Character leaps with floaty, near-zero-g motion alongside jellyfish in S6, but experiences standard gravitational pull on rope in S7. | 🟡 MINOR |
| 00:10-00:19 | 01:50-02:09 | Spatial Geography | White lander ship perched statically on an upper canopy branch in S2, then hovering inside the subterranean core in S12 without transit shown. | 🟡 MINOR |

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
|---|---|---|---|
| White Lander Ship | 00:10 (S2) | Yes (01:50, S12) | Serves as environmental anchor at top and bottom of world. |
| Climbing Harness & Rope | 00:40 (S5) | Yes (01:00, S7) | Used for locomotion in mid-canopy scenes. |
| Bioluminescent Moss Touch | 01:10 (S8) | No | Wall reacts to touch with glowing ring; character moves on without further interaction. |

## THE THREE THAT MATTER

1. **Suit Wetness Reset (01:42 vs 01:52)** — Character swims through a river in S11, but steps onto the subterranean floor in S12 with a bone-dry suit. The physical impact of full submersion is undone instantaneously between consecutive shots. *Cheapest fix: re-sequence S11 earlier, or apply a specular wetness pass to the opening frames of S12.*
2. **Abrupt Light/Elevation Oscillations (01:25 vs 01:42)** — Jumping from pitch-black bioluminescent forest (S9) to bright sunlit stream (S11) to dark underground core (S12). Destroys the spatial logic of descending through distinct vertical ecological layers. *Cheapest fix: re-edit scene order to group all sunlit daylight scenes together first, followed by dark/bioluminescent scenes.*
3. **Wingsuit and Harness Pop (00:30 vs 00:40)** — Underarm wing webbing and waist harness appear and disappear between flight and ground/swinging scenes. Suit silhouette shifts unexpectedly from shot to shot. *Cheapest fix: accept as montage convention, or regenerate S5 with wing flaps tucked visible along suit seams.*

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
|---|---|---|
| Lighting & Layer Oscillation | Re-edit scene timeline to group sunlit scenes before subterranean scenes | Low (Edit pass only) |
| Suit Wetness Reset | Re-sequence S11 before dry ground scenes or regenerate S12 start | Medium (Regenerate 1 scene) |
| Wingsuit & Harness pop | Regenerate S5 to match suit harness details from S7 | Medium (Regenerate 1 scene) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
|---|---|
| Character moves repeatedly between bright daylight and pitch-black bioluminescent environments. | Was the film designed as a continuous linear descent from sky to core, or as a non-linear exploration montage? |
| Atmosphere supports both winged dragon flight and airborne aquatic floating organisms (jellyfish, anglerfish). | Does the world bible specify distinct atmospheric density zones or floating physics per altitude layer? |

## OUT-OF-SCOPE FLAGS

* Technical: Moderate AI bloom and soft lighting haze around glowing moss and bioluminescent fish → VIDEO_QA
* Dramatic: Lack of central narrative conflict or resolution before the title card → SENARYO_QA
