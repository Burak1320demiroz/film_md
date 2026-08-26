# 📄 THE DEEP PRESSURE — MANTIK VE DEVAMLILIK QA · HAM RAPOR

> **Prompt:** `QA_PROMPTLARI/MANTIK_VE_DEVAMLILIK_QA_CRITIQUE_PROMPT.md`
> **Tarih:** 1 Ağustos 2026
> **Kapsam:** Montaj — 2:15, 14 sahne · yalnız video verildi, doküman verilmedi
> **Durum:** ✅ **GEÇERLİ** — header'da `BASELINE: SELF-CONSISTENCY` yazıyor,
> "eksik" raporlanmamış, teknik bulgular OUT-OF-SCOPE altında kalmış,
> izlenebilir nicelik olmadığı için Sayaç/Nicelik/Nedensellik `N/A`.

```
GENEL: 3/10 — STRUCTURAL PROBLEM
🔴 BLOCKER: 4   🟠 MAJOR: 2   🟡 MINOR: 0
Kostüm-Prop 1/10 → üç tablonun tamamındaki EN DÜŞÜK kategori skoru.
```

---

# 🔎 DOKÜMAN KONTROLÜ — raporun sorduğu 2 sorunun cevabı

Rubrik bunu rapordan sonra yapılacak iş olarak tanımlar
(`04_MANTIK_KALITE_TABLOSU.md` §SATIR EKLEME KURALI, adım 5).

Kaynak dosya: `yatay_2_4_dk_filmler_uzay/THE_DEEP_PRESSURE/THE_DEEP_PRESSURE_GAS_GIANT_FILM.md`

### 🚨 ÖNCE: KAYNAK DOSYA 13 SAHNELİK BİR FİLMİN 2 SAHNESİ

Dosya 56 satır ve içinde **yalnızca iki "Viral Ara Sahne"** var:

```
SAHNE 2.5 — GÖRÜNMEZ NEHİR   "Scene 2.5 of 13"
SAHNE 6.5 — IŞIK DONDURMA    "Scene 6.5 of 13"
```

İkisi de kurguda birebir bulunabiliyor — film gerçekten bu dosyanın filmi:

| Rapor sahnesi | Plan sahnesi | Eşleşme |
|---|---|---|
| S4 · 00:30 · Amber/Purple Portal + manta | SAHNE 2.5 · altın/mor yoğunluk sınırı + manta | ✅ birebir |
| S7 · 01:00 · mor fraktal kristal parçalanıyor | SAHNE 6.5 · donan yıldırımın kristalleşip dağılması | ✅ birebir |

**Diğer 11 sahnenin plan metni depoda yok.** Character Bible yok, dünya
tanımı yok, sahne haritası yok, negatif blok yok.

Karakter ve gezegen serinin ikinci Aethon filminden okunabiliyor
(`THE_BREATHING_STORM_GAS_GIANT_FILM.md` — aynı karakter Dr. Elif Vural,
aynı gezegen). Deep Pressure'ın kendi dosyası ise kıyafeti **tarif etmeden
referans veriyor**:

```
satır 14   "Elif's suit provides a neutral reference point."
satır 42   "casting sharp, dramatic light across Elif's suit"
satır  8   "the golden gas clinging to her glove"
```

Model'e "suit" deniyor, ama hangi suit olduğu **hiçbir yerde yazmıyor.**

---

### ❓ Soru 1 — "Bu karakterin kanonik kıyafeti hangisi? Turuncu uzay giysisi mi (00:30, 01:00), siyah dalgıç kıyafeti mi (00:00, 01:10)?"

**CEVAP: İKİSİ DE DEĞİL. Kanonik kıyafet ekranda HİÇ görünmüyor.**

Seri Bible'ı (Breathing Storm, satır 26):

> *"Derin mor ve bakır-kızıl termal aksanlara sahip, yüksek basınçlı şeffaf
> küresel vizörlü bir 'atmosferik dalış kıyafeti'."*

Raporun 14 sahnelik envanterinde **"mor" veya "bakır" bir kıyafet tek bir
kez bile geçmiyor.** Gözlenenler: siyah+camgöbeği çizgili ince kıyafet,
siyah ıslak dalgıç kıyafeti + tüp + regülatör, gri hantal uzay giysisi,
turuncu/siyah astronot giysisi + altın vizör.

Tek tutan öğe şeffaf küresel kask — o da 14 sahnenin sadece bir kısmında.

**Sebep, modelin hatası değil:** kıyafet üretilen dosyada hiç yazmıyordu.
→ **DERS 55**

---

### ❓ Soru 2 — "Bu sürreal bir montaj/rüya mı, yoksa gerçek bir yolculuk mu? Yolculuksa geçiş sahnesi yok."

**CEVAP: YOLCULUK OLMALIYDI. Montaj bir üretim/plan sonucu, tasarım değil.**

Elimizdeki iki sahne de bunu açıkça söylüyor:

```
"Scene 2.5 of 13"  → ara sahne numarası; 2 ile 3 arasına giren bir EK
"Starts on the exact Scene 2.5 image"  → önceki karenin devamı, yeni kurulum değil
"By 9s: she glides ... the golden-violet boundary now behind her. No cuts."
```

Seri kuralı da aynı yerde (Breathing Storm, KURAL 2 — GÖRSEL SADAKAT):
*"Video, görselin devamıdır — yeni bir kurulum değil."*

Yani plan bitişik bir iniş yolculuğu; kurguda görünen 14 kopuk lokasyon
(resif → denizaltı → denizanası → portal → kristal → volkanik baca → uzay →
dijital boşluk → dev göz) o yolculuğun **omurgası yazılmadan** üretilmiş
"viral an" sahnelerinin yan yana dizilmesi.

⚠️ Dikkat: raporun S12'si (ayna zemin) seri Bible'ında tanımlı bir sahnedir
(Breathing Storm SAHNE 9 — Metalik Okyanus, sıvı metalik hidrojen aynası).
İki Aethon filmi arasında sahne tasarımı taşınmış olabilir; bu, plan metni
olmadan doğrulanamaz.

---

# 📌 BU RAPORDAN ÇIKAN DERSLER

| Ders | Başlık | Kaynak bulgu |
|:---:|---|---|
| **55** | Character Bible'sız üretim — kıyafet her sahnede yeniden icat ediliyor | Kostüm-Prop 1/10 · 4 BLOCKER |
| **56** | "Dalış/deep" sözlüğü su üretiyor — atmosfer okyanusa dönüşüyor | Atmosfer okuması: "yoğun sıvı, sürekli yükselen kabarcıklar" |
| **57** | Tek çekim içinde ekipman morphu — 7. saniyede tüp beliriyor | 00:00 vs 00:07 BLOCKER |
| **58** | Tekrar eden varlık kimlik kilidi — aynı portal/göz iki farklı nesne | Coğrafya 4/10 · LOCATION MAP 2/3 satır "No" |

Tekrar tetiklenen (yeni ders değil): **5** (vizör kalıcılığı — 00:40 vs 00:48),
**8/37** (kıyafet ve ekipman durumu), **47** (sahne arası ışık sıçraması —
Zaman-Işık 3/10), **48** (biyom sıçraması — 12 farklı lokasyon, geçiş yok).

---

# 📤 OUT-OF-SCOPE FLAGS → teknik kayda taşındı

Rapor bunları kendi kapsamı dışında bıraktı, `01_FILM_RAPORLARI/THE_DEEP_PRESSURE.md`
altına yazıldı:

```
(VIDEO_QA)   00:48 ve 02:04 — vizör camının arkasında yüz morphu
             → DERS 16'ya iki yeni timestamp
(SENARYO_QA) Film anlatı değil, yüksek bütçeli mood board / fragman gibi
             okunuyor; lokasyonlar arasında nedensellik zinciri yok
```

---

# 📄 RAPORUN TAM METNİ

```
FILM: deep pressure
RUNTIME: 02:15 · SCENES OBSERVED: 14
BASELINE: SELF-CONSISTENCY — this review measures whether the film agrees
with itself, not whether it matches its design.

OVERALL SCORE: 3/10
VERDICT: STRUCTURAL PROBLEM
The protagonist's costume, equipment, and life support system change in almost
every single shot, and frequently within the same continuous action. The film
cannot decide if she is an astronaut, a scuba diver, or a futuristic aquanaut.
```

## SCENE INVENTORY

| # | In-out | Location | Present | What happens | Dialogue |
| --- | --- | --- | --- | --- | --- |
| 1 | 00:00-00:09 | Blue Ocean Reef | Woman, Manta rays | Woman swims horizontally. Suit morphs mid-swim. | No |
| 2 | 00:10-00:19 | Submersible Interior | Woman | Woman pilots a spherical sub in deep water. | No |
| 3 | 00:20-00:29 | Pink Jellyfish Field | Woman | Woman swims among massive glowing jellyfish. | No |
| 4 | 00:30-00:39 | Amber/Purple Portal | Woman, Manta rays | Woman touches a vertical fluid boundary. | No |
| 5 | 00:40-00:49 | Dark Crystal Field | Woman | Woman uses a blue laser tool on a crystal. | No |
| 6 | 00:50-00:59 | Underwater Volcanic Vents | Woman | Woman floats above massive fiery smoke plumes. | No |
| 7 | 01:00-01:09 | Space/Storm Void | Woman | Massive purple fractal crystal shatters above her. | No |
| 8 | 01:10-01:19 | Blue/Cyan Portal | Woman, Manta rays | Woman touches reflection in a blue vertical boundary. | No |
| 9 | 01:20-01:29 | Digital Void | Woman | Woman floats before a blue glowing circuit pattern. | No |
| 10 | 01:30-01:39 | Bioluminescent Leviathan | Woman | Woman swims next to a colossal glowing creature. | No |
| 11 | 01:40-01:49 | Giant Eye Wall | Woman | Woman shines a flashlight at a massive green eye. | No |
| 12 | 01:50-01:59 | Dark Mirror Floor | Woman | Woman floats/stands vertically over a rippled mirror surface. | No |
| 13 | 02:00-02:09 | Submersible Interior | Woman | Woman waves from inside the sub, moving towards surface light. | No |
| 14 | 02:10-02:15 | Title Card | Woman, Giant Eye | Character looks back at a massive blue eye. | No |

### THE CHARACTER — as first clearly seen

```
Face:       Clean, dark hair pulled back/contained.
Suit:       Sleek black form-fitting suit with glowing cyan geometric lines.
Wear/dirt:  Clean.
Equipment:  Full transparent bubble helmet, no back-mounted tanks, fins on feet.
First scene fully visible: 1 (00:00)
```

### THE WORLD — as the film shows it

```
Gravity:     Zero-G / underwater neutral buoyancy. Things float, swim, or hang.
Atmosphere:  Dense liquid (bubbles constantly rising).
Light:       Varies wildly — overhead surface light, bioluminescence, glowing voids.
Locations:   Ocean Reef, Submersible, Pink Jellies, Amber Portal, Crystal Field,
             Vents, Space Storm, Blue Portal, Digital Void, Leviathan, Giant Eye,
             Mirror Floor.
```

### THE COUNTER

`NONE`

## SCORES SUMMARY

| Category | Score | Critical Issue |
| --- | --- | --- |
| Physical Consistency | 4/10 | Gravity and buoyancy read as underwater until S12, where she stands vertically on a mirror. |
| Counter Logic | N/A | No counter observed. |
| Spatial Geography | 4/10 | The vertical portal boundary drastically changes environments and physics between appearances. |
| Time & Light Logic | 3/10 | The film functions as a disconnected montage; ambient light jumps wildly shot-to-shot. |
| State, Costume & Props | 1/10 | The suit and life support equipment constantly mutate, sometimes within the same shot. |
| Causality & Knowledge | N/A | It is a montage; cause and effect are not observable between scenes. |
| Quantity Consistency | N/A | No quantities tracked. |
| Setup & Abandonment | 7/10 | Tools appear once and vanish, though the submersible nicely bookends the edit. |

## SEVERITY TALLY

```
🔴 BLOCKER: 4   🟠 MAJOR: 2   🟡 MINOR: 0
```

## COUNTER CURVE

`NONE`

## LOCATION MAP

| Location | Scenes | Consistent? | Mismatch |
| --- | --- | --- | --- |
| Submersible Interior | 2, 13 | Yes | None |
| Vertical Portal Boundary | 4, 8 | No | S4 is Amber/Purple with a spacesuit; S8 is Blue/Cyan with a wetsuit. |
| Giant Eye Wall | 11, 14 | No | The eye is green with grey wrinkled skin in S11, but glowing blue with starry textures in S14. |

## DRIFT MAP

| Element | First slip | Undeniable by | Recovered? |
| --- | --- | --- | --- |
| Suit/Equipment Design | 00:07 | 00:20 | Never. It changes in almost every cut. |
| Helmet Type | 00:07 | 00:40 | Never. Shifts from bubble to mask to opaque visor. |

## CONTRADICTION LOG

| A | B | Category | What contradicts what | Severity |
| --- | --- | --- | --- | --- |
| 00:00 | 00:07 | State, Costume | Character starts with a full clear bubble helmet and no tank. Seven seconds later in the *same continuous action*, she has a scuba face mask, a regulator in her mouth, and a ribbed tank on her back. | 🔴 BLOCKER |
| 00:10 | 00:20 | State, Costume | Inside the sub, she wears a bulky grey spacesuit. Outside with the jellies, she is back in a sleek black scuba wetsuit. | 🔴 BLOCKER |
| 00:30 | 00:37 | State, Costume | At the amber portal, she wears a bulky orange/black astronaut suit with a gold visor. At 00:37, interacting with the *same* portal, she is suddenly in a sleek black suit with a clear bubble helmet. | 🔴 BLOCKER |
| 00:40 | 00:48 | State, Costume | In the crystal field, she wears an angular helmet with a dark, opaque visor. At 00:48, the visor is suddenly fully transparent, revealing her face. | 🔴 BLOCKER |
| 00:40 | 01:40 | Setup & Abandonment | She is holding a specialized glowing blue laser tool. In S11, this tool is gone, replaced by a standard yellow-beamed flashlight. | 🟠 MAJOR |
| 01:40 | 02:10 | State, Costume | The giant eye is a natural green color surrounded by grey, organic wrinkled skin. In the title card shot, the eye is neon blue surrounded by starry, glowing space textures. | 🟠 MAJOR |

## OPEN THREADS

| Object / setup | Introduced | Returned to? | Note |
| --- | --- | --- | --- |
| Blue Laser Tool | 00:40 | No | Used once to cut a crystal, never seen again. |
| Flashlight | 01:40 | No | Appears only to illuminate the green eye. |
| Submersible | 00:10 | Yes (02:00) | Successfully establishes a beginning/end visual motif. |

## THE THREE THAT MATTER

**1. The In-Shot Gear Morph (00:00 vs 00:07)**
*Why:* It happens in the very first scene. An audience will immediately notice
the character's life support (bubble vs scuba mask/tank) radically changing
while swimming.
*Cheapest fix:* Cut the second half of S1 (00:07-00:09) where the tank appears.

**2. The Portal Suit Jump (00:30 vs 00:37)**
*Why:* She approaches the barrier in a heavy orange spacesuit, then swims along
it in a sleek black wetsuit. It breaks the continuity of a single location.
*Cheapest fix:* Cut the shot at 00:37.

**3. The Visor Transparency Toggle (00:40 vs 00:48)**
*Why:* The face is hidden, then suddenly revealed in the same location without
the character touching the helmet.
*Cheapest fix:* Accept it as a "smart glass" feature, or cut the shot at 00:48.

## FIXABLE IN THE EDIT vs REQUIRES REGENERATION

| Finding | Fix | Cost |
| --- | --- | --- |
| Mid-shot gear morph (S1) | Trim the tail of the clip before the tank appears. | Low |
| Visor transparency change (S5) | Trim the tail of the clip. | Low |
| Suit changing every single scene | None. The footage fundamentally lacks a consistent character model. | High (regenerate all scenes to match ONE suit design) |

## FLAGS FOR DOCUMENT CHECK

| Observation | Question the document must answer |
| --- | --- |
| The film jumps between deep sea, fiery vents, space, and digital voids. | Is this intended to be a surreal montage/dream sequence, or a literal contiguous journey? If it's a journey, there are no transition scenes. |
| The character wears an orange spacesuit (00:30, 01:00) and a black wetsuit (00:00, 01:10). | Which suit is the canonical design for this character? |

→ İkisi de yukarıda **DOKÜMAN KONTROLÜ** bölümünde cevaplandı.

## OUT-OF-SCOPE FLAGS

* (VIDEO_QA) Slight facial morphing and loss of structure occurs behind the
  visor glass in multiple shots (e.g., 00:48, 02:04).
* (SENARYO_QA) The video reads as a high-budget mood board or trailer rather
  than a narrative short; there is no clear causal chain between the locations.
