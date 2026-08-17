# 📚 DERSLER — Metin ve Prompt Dili

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Metin ve Prompt Dili** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## ⬛ DERS 9: METİN — VİDEODA YAZI ÇIKMAMALI

**Kaynak:** The Canopy World QA — Negatif İhlal
**Sorun:** Videonun sonunda "THE CANOPY WORLD" yazısı belirdi.

**ÇÖZÜM — NEGATIVE BIBLE'a güçlendirilmiş ekleme:**
```
No text overlay, no title card, no credits, no subtitles, no watermarks, no
logos, no on-screen text of any kind at any point during the video.
```

---

## 🔴 DERS 13: AI METİN — HOLOGRAMDA ANLAMSIZ YAZI

**Kaynak:** The Slow Tide QA — Negatif İhlal
**Sorun:** Bilek ekranı/hologram sahnesinde AI anlamsız garble metin üretiyor. Okunabilir veya okunamaz — her türlü sinematik illüzyonu kırıyor.

**ÇÖZÜM — Her ekran/display/hologram sahnesine eklenecek:**
```
NO AI TEXT RULE: Any wrist display, hologram, screen, or readout shown in
frame must display ONLY abstract geometric patterns, simple colored bars, or
a blank glowing surface. NEVER generate readable or unreadable text,
letters, numbers, symbols, or AI-garbled characters on any in-world display.
If a countdown or reading is needed, describe it in the prompt narration
but show it as a simple visual indicator (pulsing light, color change) —
not as rendered text.
```

---

## 🟡 DERS 29: ANTİ-PARLAMA KELİME SÖZLÜĞÜ — TETİKLEYEN SÖZCÜKLER

**Kaynak:** The Orphan Bloom QA — Işık: 5/10 — `Pervasive AI bloom and unnatural glow.`
**QA Önerisi:** `"Reduce reliance on terms like 'glowing,' 'ethereal,' or 'luminescent' to diminish the persistent AI bloom effect."`

**Sorun:** Belirli kelimeler AI'da otomatik bloom efekti tetikliyor. "Glowing", "ethereal", "luminescent", "radiant", "shimmering" gibi kelimeler AI'nın yüksek yoğunlukta bloom ve diffuse glow üretmesine yol açıyor. Bu, Anti-Bloom direktifine (Ders 3) rağmen devam ediyor çünkü tetikleyici kelimeler prompt'un içinde hâlâ yer alıyor.

**ÇÖZÜM — Tüm prompt'larda uygulanacak kelime politikası:**
```
ANTI-GLOW VOCABULARY POLICY:

❌ TETİKLEYEN SÖZCÜKLER — Bu kelimeleri ASLA kullanma:
- "glowing" → yerine "emitting sharp directional light"
- "ethereal" → yerine "otherworldly but physically real"
- "luminescent" / "bioluminescent" → yerine
  "organisms with visible photophore organs that emit cool blue-green light"
- "radiant" → yerine "brightly lit from a point source"
- "shimmering" → yerine "reflecting light in brief individual flashes"
- "magical glow" → yerine "physically motivated light emission"
- "soft glow" → yerine "directional light with defined falloff"
- "dreamy" → yerine "cinematic, photorealistic"
- "ethereal light" → yerine "sharp-edged practical light"

✅ KULLANILACAK ALTERNATİFLER:
- Işık kaynağını her zaman fiziksel olarak tanımla:
  "organisms emit sharp, directional blue-green light from photophore organs"
- Işığın düştüğü yüzeyi tanımla, ışığın kendisini değil:
  "the wall surface is lit blue-green by the organisms — cool, defined shadows"
- Falloff'u her zaman belirt:
  "clear falloff — illuminates within 2 meters, falls to darkness beyond"
- Anti-bloom her zaman negatif bölümde:
  "No bloom, no glow filter, no soft focus, no dreamy haze, no luminescent wash"

BIOLUMINESCENT REWRITE FORMULA:
[❌ YANLIŞ]: "The bioluminescent organisms glow ethereally, creating a magical shimmering light"
[✅ DOĞRU]: "Dense mats of small organisms emit sharp, directional cool blue-green light from
photophore organs — defined falloff, clear shadows on unlit rock surfaces, no bloom,
no diffusion. The light is bright near the organisms and falls to darkness at 2 meters."
```

---

## 🔴 DERS 34: JENERİK METNİ HALÜSİNASYONU — MODEL BAŞLIK KARTI EKLİYOR

**Kaynak:** The Dead Approach Compilation QA (Genel 3/10) — Negatif: 4 ihlal — `2:10 — Text overlay ("THE DEAD APPROACH")`
**Sorun (3 filmde tekrarladı):** Dead Approach 2:10 · The Inversion 2:42 (planda olmayan jenerik kartı) · **The Stone Sky 2:10 ("THE STONE SKY" — 05.08.2026, negatif çekirdekte "no title card" 21 segmentte yazılıyken).** Model, klibin **sonuna** eğitim verisinden öğrendiği bir film jeneriği/başlık kartı ekliyor. Bu, Ders 13'ten (hologram üzerinde anlamsız yazı) FARKLI bir hatadır: orada yazı sahnenin İÇİNDEKİ bir yüzeydedir; burada model kadrajın ÜSTÜNE bir kompozit metin katmanı bindiriyor — sanki filmi kendisi kurguluyormuş gibi.

**Neden oluyor:** Eğitim verisindeki fragman ve kısa film klipleri neredeyse her zaman bir başlık kartıyla biter. Model "sinematik klip" istendiğinde bu kalıbı da taklit ediyor. Risk özellikle şu durumlarda artar: (a) promptta filmin adı geçiyorsa, (b) klip bir final/kapanış sahnesiyse, (c) compilation (birleştirilmiş) üretim yapılıyorsa.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **Film adını prompta ASLA yazma.** Karakter adı da yazılmamalı — model bunları başlık kartına dönüştürüyor. Karakteri sadece fiziksel tanımla çapala.
2. Negatif bloğa yalnızca "no text overlay" yetmiyor. Metin katmanının her türü ayrı ayrı sayılmalı:
```
no text overlay, no title card, no end card, no credits, no caption,
no lower third, no logo, no watermark, no subtitles, no burned-in text,
no letters or numbers composited over the frame at any point
```
3. **Son sahnelerde ekstra dikkat.** Kapanış sahnesi promptuna açıkça yazılmalı:
```
The take ends on the held frame. No title card appears, no text fades in,
no credits roll — the shot simply ends.
```

---

## 🔴 DERS 40: DİYALOG TETİKLİ ALTYAZI — SES BAŞLAYINCA YAZI BELİRİYOR

**Kaynak:** Low Power QA (Genel 4/10) — Diyalog & Ses: 3/10 — `0:02 — Burned-in gibberish subtitles fade in when the voiceover begins`
**Sorun:** Ders 34 modelin klip **sonuna** jenerik/başlık kartı eklemesini kapsıyordu. Bu farklı bir tetikleyici: altyazı, **diyalog başladığı anda** kadrajın altına biniyor. Model konuşmayı gördüğü an "bu bir film sahnesi, altyazısı olmalı" kalıbını uyguluyor.

**Kritik gözlem:** Bu hata **sadece sesli sahnelerde** ortaya çıkıyor. Sessiz sahnelerde altyazı riski neredeyse yok. Yani altyazı negatifi, diyaloğun kendisiyle birlikte gelmeli.

**ÇÖZÜM — PROMPT GÜNCELLEMESİ:**
Diyalog içeren HER sahnede, repliğin hemen ardına yazılır:
```
The spoken line is heard only — it is NEVER shown as text. No subtitles,
no captions, no closed captions, no burned-in dialogue text, no lower
third, no karaoke text, no transcript appearing at any point during or
after the line.
```
**Negatif bloğa:** `subtitles, captions, burned-in dialogue text, transcript overlay`

> Ders 34 (jenerik metni) + Ders 40 (altyazı) birlikte uygulanmalı — biri
> klibin sonunu, diğeri diyalog anını koruyor. İkisi birbirinin yerine geçmez.

---

## 🔴 DERS 45: PROMPT İSKELETİNİN EKRANA SIZMASI — MODEL KENDİ KÜNYESİNİ ÇİZİYOR

**Kaynak:** The Inversion **senaryo** QA — `2:12–2:21 — Non-diegetic text
overlay — Technical lens and character label graphics break cinematic
immersion.` Reçetede alıntılanan metin: **"Dr. Kaya Uçan..."**

> ⚠️ **Bu ders bir senaryo QA'sından çıktı — kuralın tek istisnası.**
> Normalde dersler yalnızca teknik QA'dan çıkar. Bu bulgu ekranda görünen
> fiziksel bir ihlal ve plan dosyasıyla karşılaştırılarak doğrulandı, bu
> yüzden ders sayıldı. Filmin teknik QA'sı hiç yapılmamıştı — yapılsaydı
> bu hatayı o yakalardı.

**Sorun:** Model, sahneyi tarif eden **prompt iskeletini** kadraja çiziyor.
Sızan metin uydurma değil — prompt'un kendi yapısal etiketleri:

```
PROMPT GÖVDESİNDE                        EKRANDA ÇIKAN
[CHARACTER BIBLE] Kaya crouches...   →   karakter adı etiketi "Dr. Kaya Uçan..."
CAMERA: 75mm, f/5.6, ISO 400         →   "teknik lens grafikleri" (HUD gibi)
```

**Bunun neden yeni bir ders olduğu:**

| Ders | Ne yapıyor | Kaynağı |
|:---:|---|---|
| 9 | videoda yazı olmamalı — genel kural | — |
| 13 | model **hologram/ekran içeriği** uyduruyor | diegetik yüzey |
| 34 | model **jenerik/başlık kartı** ekliyor | film dili |
| **45** | model **prompt'un kendi künyesini** çiziyor | **prompt biçimi** |

9, 13 ve 34 modelin *sahneye* bir şey eklemesidir. 45 farklıdır: model
**girdinin biçimini çıktıya kopyalıyor.** Negatif kilit bunu durduramaz —
çünkü sorun sahnede istenen bir şey değil, prompt'un görünüşü.

**🚨 BU FİLMİN ÖZEL DURUMU — kilidin sertliği yetmedi:**

`THE_INVERSION_PLANET_FILM.md` metni projedeki **en sert** biçimde yasaklıyor:

```
satır 403-406  "No readable or unreadable text, digits, letters, or symbols
                on the wrist display or any surface — abstract pulsing light
                only. No text, no logos, no on-screen text of any kind."
satır 414-415  "NO AI TEXT [LESSON 13]: ... NEVER text — this rule is applied
                strictly from Scene 0 onward, with no exception."
```

Belge kapanışı bu filmi zaten *"Ders 13'ü düzeltmek için yazılmış film"*
diye tanıtıyor (Tidal Hunt'ın "6:00:00" hatasına atıfla).

```
Film Ders 13'ü ÇÖZMEK için tasarlandı.  →  Film Ders 13'ü İHLAL ederek çıktı.
```

**Çıkan asıl bilgi:** *negatif kilidin sertliğini artırmak işe yaramıyor.*
"No text" 4 kez, büyük harfle, iki ayrı bölümde yazılmış ve tutmamış.

**ÇÖZÜM — negatif eklemek DEĞİL, prompt'un BİÇİMİNİ değiştirmek:**

```
1. ETİKETLERİ GÖVDEDEN ÇIKAR
   ❌ [CHARACTER BIBLE] Kaya crouches slightly, one hand hovering...
   ✅ Kaya crouches slightly, one hand hovering...
   Bible referansları prompt'un GÖVDESİNDE değil, ayrı bir başlıkta dursun.
   Köşeli parantezli etiket = modele "bunu bir etiket olarak çiz" sinyali.

2. KAMERA SATIRINI CÜMLEYE ÇEVİR
   ❌ CAMERA: 75mm, f/5.6, ISO 400, fixed at 10 meters
   ✅ Shot on a 75mm lens from a fixed position ten meters away, shallow
      depth of field.
   Sayı+harf dizilimi ("75mm f/5.6 ISO 400") ekranda lens verisi olarak
   okunabilecek tek biçim — düz cümle bu riski taşımıyor.

3. HİÇBİR ÖZEL ADI PROMPT'A YAZMA — karakter, gemi, yapı, hiçbiri
   ❌ Dr. Kaya Uçan stands alone on the rust-bronze plain
   ✅ A woman in her late thirties stands alone on the rust-bronze plain
   ❌ The 340-meter Kütüphane descends, its engine clusters firing
   ✅ The 340-meter research vessel descends, its engine clusters firing
   Ad, görsel bilgi taşımıyor ama etiket olarak çizilebiliyor. Kimlik
   Bible'da tutulur; prompt'a fiziksel tarif girer.

   🔁 **31.07.2026 — bu madde The Last Archive ile genişletildi.**
   Ders ilk yazıldığında yalnız KARAKTER adını kapsıyordu. Last Archive'da
   aynı hata GEMİ adıyla tekrarladı: prompt "the 340-meter Kütüphane"
   diyordu, model 0:18'de kelimeyi motor podunun üstüne **tabela olarak**
   yazdı (0:14'te aynı pod boştu).

   ```
   The Inversion    karakter adı  → yüzün yanına etiket
   The Last Archive gemi adı      → gövdeye tabela
   ```
   Kural artık şu: **prompt'ta geçen her özel ad, ait olduğu nesnenin
   üstüne yazılabilir.** İstisna yok.

4. NEGATİF BLOĞA (yine de eklensin — ikinci savunma hattı):
   HUD overlay, lens data, focal length text, camera metadata, name label,
   character name caption, subtitle, lower third, watermark, annotation
```

**KONTROL:** Üretilen klipte metin çıktıysa, önce prompt'un **biçimine** bak —
büyük harfli başlık, köşeli parantez, iki nokta üst üste ve sayı-harf dizisi
var mı? Negatif listeye kelime eklemeden önce bunları temizle.

> 🔗 Ders 9 · 13 · 34 ile birlikte okunur. Dördü de "ekranda yazı" ailesindendir
> ama çözümleri farklıdır: 13 diegetik yüzeyi soyutlaştırır, 34 jenerik ister,
> **45 prompt'un kendi biçimini düzeltir.**

---

## 🔴 DERS 50: NEGATİF KİLİT ANLATI ARACINI SİLİYOR — BIBLE KENDİ İÇİNDE ÇELİŞİYOR

**Kaynak:** The Tidal Hunt MANTIK QA (Genel 4/10) — `Counter Logic: N/A —
No active counter observed` + `Wrist Device · introduced 0:11 · Screen never
shown; purpose unclear.`

**Sorun:** Filmin **tek gerilim kaynağı** ekrana hiç çıkmadı. Ve sebebi
modelin hatası değil — **plan dosyasının kendi içindeki çelişki.**

`THE_TIDAL_HUNT_PLANET_FILM.md`, aynı dosya, iki satır:

```
satır 285   NO AI TEXT [LESSON 13]: Wrist display = abstract patterns only.
                                    NEVER text.
satır 338   2s — She raises her wrist display; the countdown reads 6:00:00
                 and begins ticking
```

Model iki emir arasında kaldı ve **yasağa uydu:** bilek ekranını hiç
göstermedi. Sonuç:

| Planda | Ekranda |
|---|---|
| S0 — sayaç **6:00:00**'da başlar | ekran gösterilmez |
| S4 — sayaç **yarıyı geçmiş** | ekran gösterilmez |
| S9 — sayaç **0:00:00**'da durur | ekran gösterilmez |

Film "6 saatte gel-git düzlüğünü geç" filmi. Sayaç görünmeyince geriye
**"bir kadın koşuyor"** kalıyor. MANTIK QA sayacı arayıp bulamadı ve
kategoriye `N/A` yazdı — filmin omurgasının kaybolduğunu, ne olması
gerektiğini bilmeden doğru ölçtü.

**Bunun neden yeni bir ders olduğu:**

```
Ders 13   model UYDURMA metin ekliyor      → yasak koy
Ders 45   model PROMPT BİÇİMİNİ çiziyor    → prompt'un biçimini düzelt
Ders 50   yasak, İSTENEN anlatıyı siliyor  → yasağı değil, ANLATIMI değiştir
```

13 ve 45 fazlalık üretir. **50 eksiklik üretir** — ve eksiklik QA'da
görünmez, çünkü ekranda yanlış bir şey yoktur. Sadece bir şey yoktur.

**ÇÖZÜM — sayacı metinden çıkar, FİZİĞE bağla:**

```
❌ ÇELİŞKİ:  "no text on the wrist display" + "the countdown reads 6:00:00"

✅ SAYAÇ, EKRANDA DEĞİL DÜNYADA OKUNUR — üç kanal, hepsi metinsiz:

1. SU ÇİZGİSİ    Kayadaki ıslak bant her sahnede biraz daha aşağıda/yukarıda.
                 İzleyici saati sudan okur. Sahne haritasına sütun olarak
                 yazılır: S0 %100 · S4 %50 · S8 %90 · S9 %100.
2. IŞIK AÇISI    Gölge boyu her sahnede sayısal olarak sabitlenir
                 (S0 uzun · S5 dik · S9 uzun). Zaman ışıkla anlatılır.
3. BİLEK EKRANI  Metin değil, DOLULUK: kapanan bir halka, azalan bir çubuk,
                 sönen segmentler. "Abstract patterns" yasağıyla uyumlu,
                 ölçülebilir ve her sahnede aynı yönde ilerler.

PROMPT SATIRI:
   The wrist display shows a single closing arc of light, three-quarters
   complete in this scene — no digits, no letters, no symbols.
```

**KONTROL — plan yazarken:** her negatif kilit için sor, *"bu yasak filmin
anlatmak istediği bir şeyi de kesiyor mu?"* Kesiyorsa yasak kalır ama o bilgi
için **metinsiz ikinci bir kanal** açılır. Yasakla anlatım aynı dosyada
çelişiyorsa, model her zaman yasağı seçer ve anlatım sessizce ölür.

> 🔗 Ders 13 ve 45 ile birlikte okunur. Ayrıca Ders 49 (sayaç mantığı) ile:
> 49 sayacın **geri gitmesini** yasaklar, 50 sayacın **hiç görünmemesini**.
> İkisi de MANTIK_QA'nın "Sayaç Mantığı" kategorisinden çıktı.

---

## 🔴 DERS 56: "DALIŞ" SÖZLÜĞÜ SU ÜRETİYOR — ATMOSFER OKYANUSA DÖNÜŞÜYOR

**Kaynak:** The Deep Pressure MANTIK QA — `Atmosphere read: Dense liquid
(bubbles constantly rising)` · gözlenen lokasyonlar: mercan resifi, denizanası
sürüsü, su altı volkanik bacalar, denizaltı.

**Sorun:** Film bir **gaz devinin atmosferinde** geçiyor. Ekranda okyanus var.
Model gazı su yaptı; yanına da suyun bütün eşyasını getirdi: kabarcıklar,
scuba tüpü, regülatör, ıslak dalgıç kıyafeti, palet, mercan, denizaltı.

Tetikleyici, prompt'un kendi kelimeleri:

```
"atmospheric DIVE SUIT"          → dalgıç kıyafeti
"Bir derin DENİZ DALGICI gibi"   → maske + tüp + palet
"DEEP pressure" (filmin adı)     → derinlik = su
"CURRENT" / "slipstream"         → akıntı
"MANTA-ray-like creatures"       → resif ekosistemi
"floating / glides"              → nötr yüzerlik
```

Hepsi tek tek doğru betimlemeler; **üst üste binince ortamın maddesini
değiştiriyorlar.** Bu, Ders 29'un (parlama sözlüğü) aynı mekanizması:
model sözcüğün mecazını değil, **sözlük anlamını** çiziyor.

**ÇÖZÜM — ortam maddesi her sahnede fizikle kilitlenir:**

```
MEDIUM LOCK: The character is suspended in a DENSE GAS atmosphere —
hydrogen-helium, not water. There is NO water anywhere in this film.
- No bubbles rising, no bubble trails, no exhaled air
- No scuba tank, no regulator, no dive mask, no swim fins, no wetsuit
- No coral, no reef, no seaweed, no jellyfish, no fish, no submarine
- Particulate drifts and settles slowly — it does not float in suspension
- Her body is held by pressure and thrusters, not buoyancy

❌ TETİKLEYEN SÖZCÜKLER — kullanma:
  "dive suit"      → "high-pressure atmospheric exploration suit"
  "diver"          → "atmospheric explorer under thruster control"
  "swims"          → "is carried by the gas current, thrusters correcting"
  "underwater"     → "deep within the atmosphere"
  "deep sea"       → "deep atmospheric layer"
  "current"        → "gas band moving at a different velocity"
  "manta-ray-like" → "wide flat-bodied atmospheric drifters"

NEGATIVE ADDITION: no water, no ocean, no sea, no underwater scene,
no bubbles, no scuba gear, no wetsuit, no coral reef, no fish,
no jellyfish, no submarine, no buoyancy.
```

**KONTROL — plan yazarken:** filmin ortamını bir cümlede tarif et, sonra o
cümledeki her ismi tek tek sor: *"bu kelime hangi ortamdan geliyor?"*
"Dalış" sudan gelir. Gaz devinde geçen bir filmde "dalış" kelimesi
kullanılacaksa, yanına **her seferinde** su yasağı yazılır.

> 🔗 Ders 29 (anti-parlama sözlüğü) ve Ders 39 (parçacıkların sıvı gibi
> davranması) ile aynı sınıf: yanlış sözcük → yanlış fizik. 39 parçacığın
> suda süzülmesiydi; 56 **karakterin** suda olması.

---

## 🔴 DERS 59: YASAK DEĞİL, İSİM KAZANIYOR — 28 KEZ YAZILAN KİLİT TUTMADI

**Kaynak:** The Holding Field MANTIK QA (03.08.2026, Genel 4/10) — Fiziksel
Tutarlılık **3/10** — `0:16 vs 0:42 🔴 BLOCKER — Rock falls heavily down vs
rocks float suspended upwards` · `1:30 debris float upwards into the sky`

**Sorun:** Filmin tek dünya kuralı **"hiçbir şey yükselmez"**. Kilit eksik
değildi — projedeki en sıkı kilitti:

```
"never rising"                        → 28 promptun 28'inde
"NO OBJECT IS EVER MOTIONLESS IN
 MID-AIR ... never rising, never
 frozen, never hovering"              → 28/28, BÜYÜK HARFLE
sayısal terminal hız tablosu          → her promptta, m/s cinsinden
```

**Ve tutmadı.** Ekranda taşlar gökyüzüne süzülüyor. Kilidi daha fazla
tekrarlamanın bir anlamı yok; 28 zaten üst sınır.

**Sebep prompt'ta eksik yasak değil, prompt'ta fazla İSİM:**

```
AYNI 28 PROMPTTAKİ POZİTİF BETİMLEME
  "hang / hanging"     13 kez   ← "sheets of dust hanging at chest height"
  "in mid-air"         28 kez   ← yasak cümlesinin İÇİNDE, ama kelime orada
  "caught material"     4 kez
  "suspended"           3 kez
  "floating / float"    4 kez
```

Model olumsuzlamayı değil **ismi** çiziyor. "Havada asılı duran taş"ın eğitim
verisindeki tek karşılığı **anti-gravitedir** — ve o klişe, yanındaki
"never rising" ibaresinden güçlüdür. Yasak, kendi cümlesinin içindeki isim
tarafından yeniliyor.

**AYIRICI TEST — Ders 56 ile aynı mekanizma, yeni alan:**

```
Ders 56   "dive suit"  → model SUYU çizdi        (ORTAMIN MADDESİ)
Ders 59   "hangs"      → model ANTI-GRAVİTEYİ çizdi  (FİZİĞİN YÖNÜ)
```

56 bir sözcüğün yanlış ortam getirmesiydi; 59 bir sözcüğün **filmin öncülünü
tersine çevirmesi.** Ve 59 daha sinsi, çünkü tetikleyici sözcük filmin kendi
konusunu tarif eden en doğal kelimedir — yazar onu seçmemek için özel bir
sebep bilmiyor.

**ÇÖZÜM — POZİTİF BETİMLEMEDEN İSMİ ÇIKAR, YASAĞI DEĞİL:**

```
❌ YAZMA (pozitif betimlemede)      ✅ YAZ
  "dust hanging in the air"          "dust descending through the air"
  "the suspended layer"              "the descending layer"
  "an age of caught material"        "an age of material still coming down"
  "floating fragments"               "fragments in continuous descent"
  "the sky looks stopped"            "the sky is coming down slowly"
  "NO OBJECT IS EVER MOTIONLESS      "EVERY UNSUPPORTED OBJECT IS DESCENDING
   IN MID-AIR"                        IN EVERY FRAME"

KURAL 1: Yasak cümlesi bile POZİTİF başlar. Modele ne YAPMAYACAĞINI değil,
         ne YAPACAĞINI önce söyle; yasak listesi arkadan gelir.
KURAL 2: hang · suspend · float · hover · stopped · frozen · still —
         bu yedi kök YALNIZCA negatif blokta geçebilir. Pozitif
         betimlemede tek bir kez bile geçemez.
KURAL 3: PLAN AŞAMASINDA KONTROL — filmin öncülünü bir cümlede yaz, sonra o
         cümledeki her ismi sor: "bu kelimenin eğitim verisindeki en güçlü
         karşılığı ne?" Cevap filmin kuralının TERSİ ise, kelime değişir.
         Maliyeti sıfır, üretimden önce yapılır.
```

**KONTROL BETİĞİ — üretimden önce çalıştır:**

```bash
# pozitif betimlemede tetikleyici kök arar; çıktı BOŞ olmalı
grep -oE '\b(hang|hangs|hanging|suspend|suspended|float|floating|hover|hovering)\b' \
  <film>.md | sort | uniq -c
# sayılar yalnız negatif bloktaki geçişler kadar olmalı
```

**BEDELİ:** Bu filmde 6 sahne (S1, S2, S2.5, S3, S6.5, S9) yeniden üretilecek.
Kontrol 15 saniye sürüyordu ve üretimden önce yapılabilirdi.

> 🔗 Ders 29 (parlama sözlüğü) · Ders 39 (sıvı gibi parçacık) · Ders 56
> (dalış sözlüğü) ile aynı sınıf: **yanlış sözcük → yanlış fizik.**
> 59 bu sınıfın en pahalı üyesi, çünkü tetiklediği şey bir detay değil
> **filmin öncülü.**

---

## ⚠️ 59 HAKKINDA — KİLİT SAYISI BİR ÜST SINIRA ÇARPTI

```
Bugüne kadarki varsayım:  kilit tutmuyorsa DAHA ÇOK/DAHA SAYISAL yaz
Holding Field ölçümü:     28/28 promptta, büyük harfle, sayısal tabloyla
                          birlikte yazıldı ve TUTMADI
```

Bu, `URETIM_ONCESI_ANALIZ/01_DERS_ETKINLIK_RAPORU.md`'nin "sayısal kilit
%100 tuttu" bulgusuna ilk karşı örnek değil — ama ilk kez **kilidin kendisi
doğru yazılmışken** başarısız oldu. Fark şu: sayısal kilit bir MİKTARI
sabitler (kaç insan, kaç segment, kaç m/s). Bu vakada sabitlenmesi gereken
şey miktar değil **yön**, ve yön bir isimle çelişiyordu.

> **Çıkarım:** Kilit yazmadan önce, kilidin çeliştiği bir isim olup olmadığına
> bak. Çelişen isim varsa kilit değil, isim düzeltilir.

---

## 🔴 DERS 61: SON SAHNE JENERİK KARTINA HARCANIYOR — 48 SANİYENİN 8'İ METİN

**Kaynak:** SHORTS_QA çalıştırması, 03.08.2026 — S5 skoru **2.0/10**,
raporun en düşük sahnesi:

```
S5  0:43–0:48  "Static poster with burned-in title text"
               THE SILENT RECKONING / NOT ALL DISCOVERIES SPEAK
```

**Sorun:** Dikey shorts'ta yapı **6 sahne × 8 s = 48 s** ve altısı da canlı
çekimdir. Bu üretimde son sahne statik bir başlık posteri olarak üretilmiş.
Tek karar üç ayrı şeyi birden kırıyor:

```
1. METİN YASAĞI          Ders 9 / 34 / 45 — kadrajda yazı olmaz.
                         Başlık PLATFORMDA yazılır, karede değil.
2. İÇERİK KAYBI          8 saniye = 48'in %16,7'si. Altı sahnelik bir
                         filmde bir sahnenin tamamı anlatıdan çıkarılmış.
3. LOOP ÖLÜMÜ            0:48 → 0:00 dönüşü statik bir karttan başlıyor.
                         Dikey akışta ikinci izleme ücretsiz tutundurmadır;
                         jenerik kartı onu sıfırlar.
```

Üçüncüsü yatay formatta yok — 7-9 dakikalık bir filmde jenerik kartı
normaldir. **Bu ders yalnızca dikey hatta geçerlidir** ve tam da bu yüzden
yazılmamıştı: yatay alışkanlığı, kural yokken shorts'a sızıyor.

**ÇÖZÜM — SAYISAL KİLİT:**

```
EKRANDA METİN SÜRESİ = 0,0 saniye  (48 saniyenin 48'inde)
CANLI ÇEKİM SAHNE SAYISI = 6 / 6
JENERİK, KAPAK KARTI, AÇILIŞ KARTI, KAPANIŞ KARTI = 0 adet

Son sahne promptuna zorunlu satır:
"This is a live-action photographic shot for its full 8 seconds. No title
card, no end card, no poster frame, no static graphic, no text of any kind
appears at any point, including the final second."

Kapak görseli AYRI üretilir (KAPAK PROMPTU bölümü) ve videoya GİRMEZ.
Başlık paketi platformda kullanılır (BAŞLIK VE AÇIKLAMA PAKETİ bölümü).
```

⚠️ Shorts dosyalarında `🖼️ KAPAK PROMPTU` ve `📣 BAŞLIK VE AÇIKLAMA PAKETİ`
bölümlerinin var olması, o içeriğin **videoya girmesi gerektiği anlamına
gelmez.** İkisi de yayın katmanıdır. Bu ayrımın dosyada yazılı olmaması bu
üretimi doğrudan davet etti.

---

## 🔴 DERS 67: İSİM YAZILMADAN DA KAYBEDİLİYOR — İSTENEN GÖRÜNTÜNÜN KENDİSİ TETİKLEYİCİ

**Kaynak:** THE DAWN FRONT teknik QA (05.08.2026) — Çevre 4/10 · Parçacık 3/10
· `0:20 — 🔴 wall behaves like a waterfall` · `0:06 / 1:06 — 🔴 flames in
vent` · `1:35 — 🔴 wall crest illuminated by fire`

**Sorun:** Bu film Ders 56 ve 59'un çözümünü **eksiksiz uygulamıştı:**
"explosion / blast / smoke / flame" kökleri 28 promptun hiçbirinde pozitif
betimlemede geçmiyordu (plan §0.9), sıvı yasağı serinin en sert negatif
çekirdeğiydi ("no melting, no wetting, no dripping... no wet look
anywhere"), ateş yasağı ayrı bloktu. Model yine de duvarı **şelale** gibi
akıttı ve bacadan **alev** çıkardı.

Mekanizma Ders 59'un bir adım ötesi: 59'da yasak, pozitif betimlemedeki
**isme** yeniliyordu (`hang/suspended` × 24). Burada isim hiç yok — yenilen
şey görüntünün kendisi. "Ufuktan ufka 60 m yüksek, ilerleyen beyaz duvar"ın
eğitim verisindeki en yakın komşusu şelale/çığ/tsunami; "600 °C turuncu
akkor ızgara"nınki alev ve egzoz. **Model kelimeyi değil, kompozisyonu
tamamlıyor** — ve kompozisyonun istatistiksel komşusu yasaklı malzemeyse,
negatif cümle kaybediyor.

```
Ders 56   kelime tetikliyor      → çözüm: kelimeyi değiştir      ✅ tuttu
Ders 59   pozitif isim kazanıyor → çözüm: ismi hiç yazma          ✅ uygulandı
Ders 67   GÖRÜNTÜ tetikliyor     → prompt katmanında çözüm YOK gibi
```

**ÇÖZÜM — İKİ KATMAN:**

Katman 1 — rakip kavramı pozitif tarifle doldur (ilk yeniden üretimde dene):

```
The wall is a DRY SOLID AVALANCHE OF POWDER — crushed chalk, not water.
Every part of it is matte granular solid; nothing pours, nothing splashes,
nothing foams, nothing reflects light like a wet surface. Motion blur on
the wall face is grain-streaked, never smooth like flowing liquid.
The vent grid is dark solid metal with a faint dull-orange heat tint on
the bars only — no flame, no exhaust plume, no sparks, nothing burning,
the air above it stays perfectly clear.
```

Katman 2 — Katman 1 de tutmazsa bu bir prompt sorunu DEĞİLDİR:
`URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` Kart 6 gereği **malzeme
değiştirilir** (duvarın görsel dili başka bir fiziksel kavrama taşınır —
ör. yüzeyden kalkan dikey jet perdesi yerine zeminde ilerleyen karanlık
süblimasyon hattı). Aynı görüntü üçüncü kez istenmez; §8'in ölçülmüş
gerçeği geçerli: kural eklemek kaliteyi artırmıyor, karar değiştirmek
artırıyor.

---

## 🔴 DERS 76: YOKLUKLA KURULAN NOVUM NESNEYE DÖNÜŞÜR — "YILDIZSIZ DAİRE" KARA KÜRE OLARAK ÇIKTI, YILDIZ ALANI DA GİTTİ

**Kaynak:** THE STARLESS CIRCLE (06.08.2026) — MANTIK_QA sahne envanteri
`Black sphere visible low in the sky` (S5) / `looking up at the black
sphere, now higher` (S8); VIDEO_QA baseline `Location: … dark sky devoid
of stars`. Plan: *"a perfect circular patch, two degrees wide, that
contains NO stars — a black disc of absence… never glowing, never
outlined, not an eclipse, not a planet"*, ve her gece karesinde **yoğun,
titreşimsiz yıldız alanı** zorunlu.

**Sorun:** Filmin adı, kancası, teması ve finali tek bir şeye bağlıydı:
**gökte yıldız OLMAYAN bir yama.** Model bunu iki ayrı şekilde bozdu ve
ikisi de aynı kökten geliyor:

```
① YOKLUK NESNELEŞTİ   "yıldızsız daire" → "kara küre/disk cismi"
                      Yokluk çizilemez; model boşluğu bir NESNEYLE
                      doldurur, çünkü prompt ondan bir şey ister.
② TAŞIYICI ALAN GİTTİ Bir klipte gök tamamen yıldızsız çıktı. Yıldız
                      alanı yoksa "yıldızsız yama" da yoktur — yokluk,
                      ancak POZİTİF alan render edilirse okunur.
```

DERS 73 türetilmiş optik fenomenleri (gölge, yansıma, kostik) yasaklamıştı;
bu onun kardeşi ve bir adım daha kötüsü: **negatif uzam** (yokluk, boşluk,
delik, sessizlik) taşıyıcı olarak seçilirse model ya nesne çizer ya alanı
siler. İki filmde iki farklı novum sınıfı, aynı sonuç: novum ekranda yok.

**ÇÖZÜM — plan aşaması kararı + tek-kare kapısı (DERS 73 ② ile aynı kapı):**

```
NEGATİF NOVUM KURALI:
① Novum bir YOKLUK ise, plan onu POZİTİF ALAN + ÖLÇÜLEBİLİR KESİNTİ
   olarak yazar. Kabul ölçütü prompt cümlesi değil, SAYIdır:
     "the sky must show at least 200 individually resolved stars;
      inside a 2-degree circle at <konum> there are ZERO stars;
      the circle has no edge line, no rim, no gradient, no object —
      only the star density drops to zero"
   Yokluğun kenarı tarif edilmez; SAYIM tarif edilir (200 ↔ 0).
② TEK KARE KAPISI (D73 ②): tek imaj promptu koşulur. Kare kabul edilir
   ancak (a) pozitif alan sayılabiliyorsa ve (b) yokluk bölgesinde
   NESNE yoksa. "Küre / disk / gezegen / tutulma / hale" görünen kare
   BATTI'dır ve sonuç KAPI KAYDI'na yazılır (D74).
③ Kapı batarsa novum taşıyıcısı değişir — dosyadaki Plan B'yi çalıştırmak
   OPSİYON DEĞİL, kapının çıktısıdır. Bu filmde Plan B yazılıydı
   ("daire yalnız S0 ve S6'da tutulur") ve hiç uygulanmadı.
```

> 🔗 Ders 50 (sayaç ekrana çıkmadı) · Ders 59 (yasak, andığı şeyi çağırır) ·
> Ders 73 (türetilmiş fenomen) ile aynı aile. Ortak cümle: **modelin
> çizemeyeceği şeyi prompt cümlesi çizdiremez; plan taşıyıcıyı değiştirir.**

---

## 🔴 DERS 88: SINIRLI İZİN TAM İZİNDİR — "HAFİF YANSIMA AMA GİZLEMESİN" TAM AYNA ÇIKIYOR

**Kaynak:** THE SECOND SHIP · Faz 7 / BEDEL 1. koşusu (S67) — skor yok,
bulgu koşusu · `yatay_10_20_dk_filmler/THE_SECOND_SHIP/FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md` D-AQ
**Sorun:** iki fazda iki farklı malzemede aynı mekanizma (F6 S53 toz →
duvarda iz · F7 S67 yansıma → tam ayna)

Prompt aynı nesne hakkında iki şey söylüyordu:

```
SUBJECT  : "a fully transparent visor; the face reads clearly through
            the glass, WHICH CARRIES A FAINT COOL REFLECTION"   ← izin
NEGATIVE : "no mirror coating, no reflection that hides what is
            behind it"                                          ← sınır
EKRANDA  : tam yansıtıcı cam; yüz okunmuyor.
```

Model niceliği (hafif / faint / subtle) değil, **niteliği** alıyor:
sahnede yansıma VAR yazıyorsa, yansımayı fizik önselinin verdiği
kuvvette çiziyor. Negatifin işi o niteliği geri almak değil — geri
alamıyor. Aynı mekanizma F6'da kirli parmak ucuyla yaşandı: "grubby
fingertips" + "leaves no mark" → duvarda iz.

**ÇÖZÜM — kaynağı sahneden çıkar, sonra yasakla:**

```
① İZİN CÜMLESİNİ SİL. "faint / subtle / slight / a touch of X"
   kalıbı, aynı promptta X yasaklanıyorsa promptta DURAMAZ.
② YERİNE SIFIR TARİFİ + BİR REFERANS YAZ (tarif değil, karşılaştırma):
   The visor is optically clear and carries NO reflection at all -
   the eyes, the brows and the scar are the sharpest, brightest
   things in the frame and nothing floats on the glass in front of
   them.
③ PROMPT TARAMASI (üretimden önce, bedava):
   grep -nE "faint|subtle|slight|a hint of|barely" <film>.md
   → her eşleşme için sor: aynı nitelik aşağıda yasaklanıyor mu?
     Yasaklanıyorsa çelişki vardır; izin cümlesi silinir.
```

⚠️ İstisna: yasakla ÇELİŞMEYEN "faint" cümleleri kalır (temas gölgesi,
sedef kabuğun spekülerı) — bunlar üç koşuda üst üste tuttu.

---

## 🔴 DERS 99: PROMPT NESRİ SESE SIZIYOR — "SHADOW ENTRY AND EXIT" TARİF CÜMLESİYDİ, KURGUDA REPLİK OLARAK DUYULDU

**Kaynak:** THE RING LIGHT · 12.08.2026 · 📖 SENARYO_QA'nın duyduğu 9 replik
listesi + planın S4-B video promptu (`grep` ile bulundu, D85 kapısı tersine
çalıştırılarak)
**Sorun:** ilk teşhis; ama seride **sessiz sahne** sayısı yüksek olduğu için
(bu filmde 7/14) kapsamı geniş

Filmin replik mimarisi §0.11'de kilitli: **7 replik, hepsi Türkçe, hepsi
gövdesiz AI.** QA raporu 9 replik duydu. Fazladan gelenler İngilizceydi ve
en az biri promptun **kendi tarif cümlesiyle** birebir örtüşüyor:

```
rapor (0:50-1:00 bandı):  "Shadow entry…"
plan S4-B video promptu:  "Shadow entry and exit are hard-edged at each
                           boundary — no gradient, no glow…"      (PHYSICS)
aynı promptun AUDIO'su:   "Outside the hulls there is absolute silence.
                           On the radio channel: … No voices."
```

Yani modele "burada ses yok" denmiş, ama aynı promptun içindeki **anons
biçimli isim tamlaması** (`Shadow entry`, `Sonic warning`, `Contact`) ses
kanalına düşmüş. Bu, D82'nin (ses mimarisi tersine döndü) akrabası ama farklı
mekanizma: orada VAR OLAN replik yanlış ağza gitti, burada **replik olmayan
bir cümle replik oldu.**

⚠️ Doğrulama durumu: kilit çelişkisi defterinde açık madde (master'ın
0:50-1:00 ve 2:00-2:24 bandı dinlenerek kapanır, D96). **Panzehir her iki
sonuçta da doğrudur ve maliyeti sıfırdır.**

**ÇÖZÜM — iki cümle, iki yer:**

```
① SESSİZ SAHNELERİN AUDIO BLOĞUNA (bu filmde 7 sahne):
   No speech of any kind occurs in this shot: no voice, no narration, no
   announcement, no radio call-out, no whisper, no spoken word in any
   language. The only sounds are the ones listed above.
   ⛔ "No voices" YETMİYOR — ölçülen vaka tam olarak bu cümlenin altında
      çıktı. Yasak, konuşmanın BÜTÜN biçimlerini tek tek saymalıdır.

② TARİF NESRİNDEN ANONS BİÇİMİNİ ÇIKAR:
   "Shadow entry and exit are hard-edged"
      → "the lander's crossing into and out of the shadow is hard-edged"
   "Sonic warning / Contact / Zero" gibi tek başına duran isim tamlamaları
   cümle içine gömülür; prompt nesri ASLA anons gibi okunmamalıdır.
```

⭐ **Genel kural:** promptta tırnak içinde olmayan her cümle de sese
dönüşebilir. Replikler tırnakla ve dilleriyle kilitlenir; **tarif nesri ise
konuşulamaz biçimde yazılır.**

---
