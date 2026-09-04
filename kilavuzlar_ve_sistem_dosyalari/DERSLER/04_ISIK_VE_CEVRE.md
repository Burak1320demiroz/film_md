# 📚 DERSLER — Işık ve Çevre

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Işık ve Çevre** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🟡 DERS 3: AI BLOOM — PARLAYAN YÜZEYLER YIKANIYOR

**Kaynak:** The Canopy World QA — Işık: 6/10 | The Deep Root QA — Işık: 6/10
**Sorun:** Bioluminesan sahnelerde AI aşırı bir "bloom" efekti ekliyor — sinematik kontrastı yok ediyor. Deep Root'ta enerji kökleri ve vizör yansımaları aynı sorunu gösterdi. Vizör yansımaları ortam ışığıyla eşleşmiyor.

**ÇÖZÜM — Bioluminesan/parlayan sahnelerin LIGHTING bölümüne eklenecek:**
```
ANTI-BLOOM DIRECTIVE: Bioluminescent light sources must emit SHARP, DIRECTIONAL
light with clear falloff — not a soft, diffused, dreamy glow. Maintain HIGH
CONTRAST between lit and unlit areas. The light must create defined shadows,
not wash out the entire frame. Think practical film set lighting with actual
physical light sources, NOT a post-production bloom filter.

Skin under bioluminescent light must retain visible pore texture, natural
subsurface scattering, and realistic shadow — never airbrushed, never plastic,
never smooth under colored light.
```

**NEGATIVE'e eklenecek:**
```
No bloom, no glow filter, no soft focus glow, no dreamy haze, no airbrushed
skin, no plastic skin texture, no Unreal Engine lighting, no video game
aesthetic, no lens flare on bioluminescent sources.
```

---

## 🟡 DERS 6: ARKA PLAN KARARLILIĞI — ÇEVRE MORPH

**Kaynak:** The Canopy World QA — Çevre: 7/10
**Sorun:** Arka plan elementleri (kökler, mantarlar, ağaçlar) sahne boyunca hafifçe "nefes alıyor", şekil değiştiriyor, kenarları eriyor.

**ÇÖZÜM — Her prompt'un ENVIRONMENT bölümüne eklenecek:**
```
ENVIRONMENT STABILITY LOCK: All background environmental elements (trees, roots,
rocks, mushrooms, moss, water surfaces) must remain COMPLETELY STATIC and
unchanging throughout the 10-second clip unless explicitly described as moving
in the MOTION section. No background breathing, no edge warping, no texture
swimming, no slow morphing of stationary objects. The environment is a FIXED,
SOLID, PHYSICAL world — not a dream, not a hallucination.
```

---

## 🟡 DERS 19: YANSIMA TUTARLILIĞI — SU YANSIMALARI EŞLeŞMiYOR

**Kaynak:** The Tidal Hunt QA — Işık: 4/10
**Sorun:** Geminin su yansıması gerçek gemiyle eşleşmiyor — farklı şekil, farklı açı.

**ÇÖZÜM — Yansıma içeren her sahneye eklenecek:**
```
REFLECTION ACCURACY RULE: Any reflection visible in water, glass, visor, or
polished surface must ACCURATELY MATCH the object being reflected in shape,
scale, color, and angle. Reflections must update consistently with camera
movement. No warped, mismatched, or invented reflections.
```

---

## 🟡 DERS 25: VİZÖR YANSIMA OTONOMİSİ — YANSIMA BAĞIMSIZ HAREKET EDİYOR

**Kaynak:** The Hollow Station QA — Işık: 5/10
**Sorun:** 1:16'da cam/vizör yansıması karakterin gerçek yüzünden bağımsız olarak morph ediyor — yansımadaki yüz gerçek yüzle eşleşmiyor. AI yansımaları ayrı bir obje olarak üretiyor.

**ÇÖZÜM — Cam/vizör/pencere yansıması içeren her sahneye eklenecek:**
```
REFLECTION SYNC RULE: Any reflection of the character visible in a
visor, window, glass panel, or polished surface must be a PHYSICALLY
ACCURATE mirror of the character's actual current pose, expression,
and movement. The reflection must:
- Update in REAL TIME with the character's motion
- Show the SAME facial expression as the real face
- Move at the SAME speed and direction as the source
- Maintain the SAME bone structure and proportions
The reflection must NEVER morph independently, show a different
expression, or become an autonomous figure. It is a mirror image,
not a separate entity.
```

---

## 🟡 DERS 27: MAĞARA DOKU YÜZME — JEOLOJI STABIL OLMALI

**Kaynak:** The Orphan Bloom QA — Çevre: 4/10 — `0:45 — Rock textures in the cavern visibly swim and shift.`
**Sorun:** Mağara duvarı kaya dokuları sahne boyunca görünür biçimde "yüzüyor" — yüzey desenleri yavaşça kayıyor, titreşiyor, değişiyor. Bu, AI'nın dinamik dokularda ortaya çıkardığı özel bir hata: sabit olması gereken mineral/kaya yüzeyleri sanki animasyonlu gibi davranıyor.

**ÇÖZÜM — Mağara/yeraltı/kaya içeren her sahnenin ENVIRONMENT bölümüne eklenecek:**
```
GEOLOGICAL STABILITY LOCK: All rock, mineral, and stone surfaces must
behave as COMPLETELY STATIC, INERT, PHYSICAL MATTER:

- Rock textures (grain, mineral veins, crystal inclusions, basalt pores)
  must NOT animate, swim, shift, drift, or change in any way during the clip.
- Cave walls, floor, ceiling are SOLID GEOLOGY — they do not breathe,
  pulse, undulate, or have any living motion whatsoever.
- Mineral vein patterns (amber veins, crystal seams) are FIXED decorative
  geology — they do not glow more or less over time unless explicitly
  described as pulsing bioluminescence. Even then, the GEOMETRY of the
  vein does not change — only its light output may pulse.
- Water-carved rock surfaces, stalactites, and geological formations are
  physically carved over millennia — they are harder than any force in
  the scene and do not deform.

DISTINCTION: Only EXPLICITLY BIOLOGICAL elements (organisms, living films,
creatures) may show motion. Geology is DEAD. Stone does not move.

NEGATIVE ADDITION: No swimming rock textures. No morphing mineral veins.
No undulating cave walls. No animated geology.
```

---

## 🟡 DERS 41: YUMUŞAK IŞIK ≠ BLOOM — ATMOSFERLİ GEZEGENLERDE YANLIŞ TEŞHİS

**Kaynak:** Low Power QA (Genel 4/10) — Işık: 4/10 — `0:01 — AI Bloom on the blue sunset` + `0:09 — Unmotivated fill`
**Sorun:** Bu ders bir üretim hatasından değil, bir **QA teşhis hatasından** çıktı — ve düzeltilmezse doğru filmleri bozar.

QA raporu Mars gün batımındaki yumuşak ışığı "AI bloom" olarak işaretledi ve çözüm olarak `"Harsh directional sunlight, sharp shadow falloff, no ambient fill"` önerdi. **Bu öneri Mars için fiziksel olarak YANLIŞTIR.** Toz fırtınasındaki bir gezegende ışık her yönden saçılır; gölgeler gerçekten zayıf ve yumuşak kenarlıdır, dolgu ışığı gerçekten vardır ve motivasyonludur. Aynı rapor kendi künye bloğunda `FILL LIGHT ALLOWED: Yes` yazmışken dolgu ışığını ihlal olarak raporladı.

**AYRIM:**
```
MEŞRU ATMOSFERİK YUMUŞAKLIK          AI BLOOM (gerçek hata)
─────────────────────────────────    ─────────────────────────────────
Gölge kenarı yumuşak ama VAR         Gölge tamamen kayboluyor
Yüzey dokusu korunuyor               Doku yıkanıp siliniyor
Parlak alan sınırlı ve kaynaklı      Parlaklık nesnenin dışına taşıyor
Kontrast düşük ama ölçülebilir       Her şey tek bir sisli tona düşüyor
Cilt gözeneği görünür                Cilt mumsu ve pürüzsüz
```

**KURAL:** Bloom teşhisi **gölgenin varlığına değil, DOKUNUN KAYBINA** bakılarak konur. Doku duruyorsa yumuşak ışık meşrudur.

**ÇÖZÜM — PROMPT GÜNCELLEMESİ (atmosferli gezegenler için):**
```
Light is heavily diffused by suspended dust and shadows are weak with soft
edges — this softness is correct and must be preserved. But every surface
retains full visible texture: regolith grain, suit fabric weave, skin
pores. Diffusion without texture loss. 0% bloom, no glow filter, no
luminous halo extending beyond any object, no waxy skin.
```
> ⚠️ Vakum filmlerinde bu ders GEÇERSİZDİR — orada gölgeler mutlak siyah,
> dolgu ışığı yok, ışık serttir. Ders 3 orada tam olarak geçerlidir.

---

## 🔴 DERS 145: ALÇAK AÇI UFKU KADRAJDAN ATAR — KAPANAN UFKU MODEL DUVARLA DOLDURDU (DÜZ OVADAKİ GEMİ KANYONA GİRDİ)

**Kaynak:** THE SKYLIGHT S26 (kurgu 4:00-4:10) — ⑤ 🟠 "canyon pop-in: rocket enclosed
by steep rocky canyon walls"; master karesi 4:05 (iki yanda dik kaya duvarı); S25 (3:55)
ve S28 (4:24) aynı gemi düz ovada · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_SKYLIGHT.md`
**Sorun:** 1 film, 3 sahnenin ALÇAK AÇILI olanı.

S26 promptu kurulumu ("low-angle wide framing"), yeri ("rust-red plain", "the volcano's
soft shoulder on the horizon") ve gemiyi eksiksiz yazdı — ama alçak açılı bir kadrajın
üst üçte ikisini NEYİN doldurduğunu yazmadı. Alçak açıda ufuk kadrajın dibine iner,
üst alan boşalır; model boş alanı Mars'ın en olası dokusuyla doldurdu: uçurum. Göz
hizası geniş kadrajlar (S25 · S28) ovayı korudu, çünkü kadrajları ufku İÇERİYORDU.
Arka plan merceğinin kendi kuralı ("en büyük arka plan nesnesini adlandır") inceleme
anında uygulandı; prompt anında uygulanmalıydı.

**ÇÖZÜM — her dış mekân promptu en büyük arka plan nesnesini ADLANDIRIR ve ufuk kilidi
taşır; alçak açılı prompt GÖĞÜ yazar:**

```
HORIZON LOCK: flat open plain to the horizon in every direction — no cliffs,
no canyon walls, no rock walls, no ridge nearer than the horizon line; nothing
stands higher than knee height within five hundred metres of the ship except
the ship itself.
LOW-ANGLE FIELD: because the camera is low, the horizon sits in the bottom
sixth of the frame and everything above it is EMPTY SKY — butterscotch,
cloudless, featureless; the ship is silhouetted against sky, not against rock.
LARGEST BACKGROUND OBJECT: <adı ve kadraj payı — "the sky, upper five sixths" ·
"the volcano's soft shoulder, bottom sixth">
```

> 🔗 Ders 6 (çevre morph) · Ders 58 (tekrarlayan varlık kimliği — mekân da varlıktır) ·
> Ders 126 (⑤ en büyük nesneyi yazmadı; bu ders aynı kuralı PROMPT tarafına taşır) ·
> Ders 104 (ışık mıknatısı — alçak açının kardeşi: boşluk da mıknatıstır).

---

---

## 🔴 DERS 176: KONTRAST GARANTİSİ ZEMİNİ İKİNCİ KEZ TARİF ETTİ — AYNI PROMPTTA İKİ CÜMLE ZEMİNE İKİ RENK VERDİ VE FİLM ORTASINDA BİYOM DEĞİŞTİRDİ

**KAPI:** BETİK · `prompt_kontrol.py` YÜZEY RENK KAPISI — bir promptun
bütün blokları taranır; aynı yüzey adı (`floor` · `ground` · `wall` · `sky`
· `hull`) **birden çok renk sıfatı** taşıyorsa BLOCK. Kontrast garantisi
yüzeyin RENGİNİ değil, ÖZNENİN OKUNURLUĞUNU söyler.
**TEKRAR:** 0 · 04.09.2026 THE UPWARD FALL

**Kaynak:** THE UPWARD FALL · ⑪ ölçüm kapısı, 22 sahnenin ızgara şeridi
(`grid10s.jpg`) — 0-160 s zemin KAHVERENGİ lif, 160-220 s SOLUK GRİ/KÜL.
**Sorun:** Üç mercek (④ ⑤ ⑥) bunu "ani biyom sıçraması / ash-snow biome /
geography break" diye 🟠 MAJOR yazdı ve üçü de **S20/S21'i kesmeyi** önerdi.
Kusur sahnede değildi: **promptun kendi içindeydi ve 25 promptun 25'inde
vardı.**

```
AYNI PROMPT, İKİ CÜMLE, İKİ ZEMİN:

WORLD bloğu :  "The floor is a deep dry mat of fallen fibre."      → renk YOK
LIGHT bloğu :  "The black suit reads as a clean dark silhouette
                against the PALE GREY FLOOR; the light rims his
                shoulders so the figure never merges with the
                background."                                        → renk VAR

→ Model ilk yarıda WORLD'e, ikinci yarıda LIGHT'a sadık kaldı.
  İki cümle iki sadakat; kurgu ortasında dünya değişti.
```

⭐ **MEKANİZMA — KAPININ KENDİSİ KUSURU ÜRETTİ.** O LIGHT cümlesi bir QA
önlemidir: SPEC'in `KAPI ⑦ KONTRAST` maddesi, mat siyah giysinin karanlıkta
kaybolmasını engellemek için yazıldı (Blind Berth "iki siyah gövde" emsali).
Önlem doğruydu; **yazıldığı yer yanlıştı.** Kontrastı garantilemek için
zemine bir renk verildi, ve o renk WORLD bloğunun tarifiyle çarpıştı.
Bir kalite kapısı, koruduğu filmde bir devamlılık kusuru üretti.

⛔ Bu [[D174]]'ün kardeşidir: orada aynı promptta iki cümle **yöne** iki
farklı sadakat üretti, burada **renge**. Ortak kural: *bir promptta bir
şeyin iki tarifi varsa, model ikisini de üretir — sırayla.*

**ÇÖZÜM — KONTRAST GARANTİSİ ÖZNEYİ TARİF EDER, ZEMİNİ DEĞİL:**

```
✗  "The black suit reads as a clean dark silhouette against the pale
    grey floor; the light rims his shoulders..."

✅ "A low rim light separates his shoulders and helmet from whatever is
    behind him; his silhouette never merges with the background."
       → aydınlatma iddiası. Hiçbir yüzeye renk atamıyor.

✅ Zeminin rengi TEK yerde, WORLD bloğunda, TEK cümlede durur ve
   SPEC C bloğuna da o cümleyle yazılır:
       "The floor is a deep dry mat of fallen fibre, pale grey-brown."
```

⭐ **VE QA TARAFI:** kontrast KAPISI promptla değil ÖLÇÜMLE koşulur —
`olcum_kapisi.sh` KAPI ⑦ (YMAX − YMIN ≥ 110). Promptta yazılan kontrast
garantisi bir ölçüm değil, bir renk ataması olur.
