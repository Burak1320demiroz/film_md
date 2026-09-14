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

## 🔴 DERS 123: YASAK, YASAKLADIĞI KAVRAMI PROMPTA SOKAR — NEGATİF BLOK POLİTİKA REDDİ ÜRETTİ

**Kaynak:** THE LAST SPAN · 25.08.2026 · ilk üretim turu: 2 prompt denendi,
2 red, 0 başarı. İkisi de aksiyon doruğu (S8 kovalamaca, S9 doruk).

```
S8 → "I can't make videos of real people in situations like that."
S9 → "I can't make videos that could relate to dangerous situations."
```

**Sorun:** Film tasarımı gereği **0 kare** yara, kan, ceset, temas taşıyor —
tür kartının gore bütçesi sıfıra indirilmişti ve dosya bunu satır satır
yazıyordu. Ama prompt dosyası, o sıfırı KORUMAK için, `NEGATIVE:` bloğunda
şu kelimeleri tekrar tekrar yazıyordu:

```
"gore"   29 kez        "wounds"  26 kez
"blood"  26 kez        "corpse"  18 kez
```

Hepsi `no ...` önekiyle. **Politika sınıflandırıcısı öneki değil kelimeyi
okur.** Filmde hiç olmayan bir şiddet, onu yasaklayan cümleler yüzünden
promptun içine girdi. Aynı mekanizmanın üretim tarafı §7'de zaten yazılıydı
(yapısal red: "yokluk listesi istek olarak okunamıyor"); bu, onun **politika
tarafındaki** karşılığıdır ve depoda ilk kez görüldü.

İki yardımcı katman:
- **"crowd of figures" + kaçan insan = kitlesel kaza.** S8'in reddi bunu
  birebir söylüyor ("real people"). Filmin tasarımı figürleri zaten heykel
  gibi kuruyordu (0 yüz, 0 ses, rijit, ayak yerden kalkmaz) — prompt onları
  yanlış adlandırıyordu.
- **Şiddetli fiil.** "hurls the can into the CHEST" — dominoyu deviren itiş
  her yükseklikten olur; göğüs seçimi dramatik değil, sadece riskliydi.

**ÇÖZÜM — prompt'a eklenecek:** yasağı SİL, yerine MALZEMEYİ TARİF ET.

```
✗ YASAK (reddedildi):
no visible faces, no eyes, no open mouths, no teeth, no wounds,
no blood, no gore, no corpse staging, no jump scare

✓ TARİF (aynı işi yapar, daha iyi yapar):
Each one is sealed head to foot under a single unbroken coat of pale
grey dust, so clothing, hair and head read as one continuous matte
surface — the head is a smooth dust shell with no readable features,
like a plaster cast left standing in the open. They are a still field
of upright shapes, not a gathering.
```

```
✗ "a dense standing crowd of dust-caked figures"
✓ "a packed field of upright dust-coated forms"

✗ "the figure topples ... hits the deck ... stays down"
✓ "the form tips the way an upright plank tips, or a domino in a line:
   it rotates about its base, feet staying flat on the ground, knees
   straight, arms down at its sides"

✗ "she hurls the can into the chest of the nearest figure"
✓ "she lets the can go in a low flat swing; it strikes the outermost
   form at hip height"

✗ "no figure falls over the barrier or off the bridge"
✓ "the barrier holds them: the fold stops at the concrete and stays
   on the deck"        ← sınırlamayı YASAKLA değil, KURAL olarak yaz
```

**Teşhis sırası — red gelince prompt kısaltmadan ÖNCE bu üçü elenir:**
```
1. Yasakladığın için YAZDIĞIN bir şiddet/tehlike kelimesi var mı?
   (gore · blood · wound · corpse · injury · jump scare · horror ·
    weapon · victim) → varsa sebep BU. Kısaltma işe yaramaz, SİL.
2. İnsan kütlesini nasıl adlandırıyorsun? "crowd of figures" + kaçan
   insan = kitlesel kaza okuması.
3. Fiil şiddetli mi? Aynı fiziği taşıyan nötr hâl var mı?
```

⛔ **prompt_kontrol.py bunu GÖREMEZ ve göremez de:** betik negatif çekirdeğin
VARLIĞINI arar — kelimelerin politika maliyetini değil. Bu tuzağın kapısı
insan gözüdür ve red gelene kadar görünmezdir.

⚠️ **Sınıflandırıcı promptu BÜTÜN olarak okur.** Tek tek masum üç cümle
(kalabalık + koşan insan + devrilen gövdeler) birlikte bir felaket sahnesi
tarif eder. Reddi tek kelimede arama.

⭐ Bu ders **Ders 59'un** (pozitif hâl yasaktan iyi tutar) politika
eksenindeki tekrarıdır. 59 sadakati ölçüyordu; 123 ÜRETİLEBİLİRLİĞİ.
İkisi aynı cümleyi söylüyor: **modele ne İSTEMEDİĞİNİ değil, ne
İSTEDİĞİNİ yaz.**

**KAPI:** BETİK · `prompt_kontrol.py ⑯ POLİTİKA SÖZLÜĞÜ` (01.09.2026 ·
NEGATIVE bloğu DÂHİL sayar) + LİSTE · `03_PLAN_ONCESI B6`
**TEKRAR:** 0

✅ **DIŞ DOĞRULAMA — 01.09.2026 · TUR 3.** Bu ders depo dışından, bağımsız
olarak doğrulandı **ve mekanizmasının adı bulundu**: sağlayıcı filtreleri
zararın ŞİDDETİNE değil, metnin o kategoriye girme **OLASILIĞINA** göre
puanlıyor. *"Robot beni yumrukladı"* ile *"robot beni parçaladı"* aynı
kefeye girebiliyor. **Olumsuzlama olasılığı düşürmez; kelimenin VARLIĞI
yükseltir.** D123'ün 25.08'de gözlemlediği davranışın nedeni budur.
Ayrıntı: `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` T3.3 ·
kural metni: `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` §1.0①
⚠️ Aynı turda ters yönde bir anekdot da geldi ("isteme `no celebrities`
ön bloğu ekle"); **depo kuralı korundu**, çelişki T3.4 ①'de açık duruyor.

---

## 🔴 DERS 128: MALZEME METAFORU MEKANİĞİ EZER — "PLASTER CAST" DOMİNOYU ÇÜRÜMEYE ÇEVİRDİ

**Kaynak:** THE LAST SPAN QA · 25.08.2026 · filme özel ÖNERME KAPISI:
C1 KURAL OKUNABİLİRLİĞİ **1/10** · A1 + A2 FAIL · karar REGENERATE.

**Sorun:** Filmin novum'u bir MEKANİKTİ — formlar kendi başlarına harekete
geçemez, tek temas devirir, devrilen kalkmaz. Ekranda o mekanikten **0 kare**
çıktı. Bunun yerine formlar kendiliğinden toza dağıldı. İzleyicinin okuduğu
kural ile yazılan kural iki farklı film:

```
OKUNAN:  "Dünya taşlaşmış, kül figürler kendiliğinden toza dönüşüyor."
YAZILAN: "Kendi başlarına harekete geçemezler; tek temas devirir;
          devrilen bir daha kalkmaz."
```

**Mekanizma:** [D123] politika reddini çözmek için yasak sözlüğü silinip
yerine pozitif malzeme tarifi kondu — doğru karardı ve reddi çözdü. Ama
seçilen metafor bir **fiziksel özellik** taşıyordu:

```
"...like a plaster cast left standing in the open"
"the head is a smooth dust shell..."
```

Alçı döküm ve toz kabuğu **KIRILGANDIR**. Devrilmez, DAĞILIR. Model
"dust shell"i gövdenin ÖRTÜSÜ değil **MALZEMESİ** okudu. Domino cümlesi
promptta duruyordu ama malzeme tarifi onu ezdi. Kanıt, fizik merceğinin
PREMISE REGISTER'ında modelin kendi okuması olarak yazılı:

```
"Human bodies have petrified into brittle, dry ash/dust structures that
 hold their shape until collapsing."
```

**ÇÖZÜM — prompt'a eklenecek:** metafor seçilirken **iki soru** sorulur.

```
① Bu metaforun taşıdığı fiziksel özellik nedir?
   plaster cast  → kırılgan, dağılır          ⛔ mekanik: devrilme İSE ters
   mannequin     → rijit, devrilir, kalıcı    ✅
   fence post    → rijit, tabandan döner      ✅
   sandbag       → yarı rijit, yığılır        ⚠️ kısmi
② O özellik filmin MEKANİĞİYLE aynı yönde mi ters mi?
   Ters ise metafor DEĞİŞTİRİLİR — mekanik cümlesi eklenerek kurtarılmaz.
```

**Bu filmin doğru hâli:**

```
✗ "sealed head to foot under a coat of pale grey dust ... like a plaster
   cast left standing in the open"
✓ "sealed head to foot under a coat of pale grey dust. Under the dust each
   one is a solid, heavy, rigid body: it does not crumble, does not shed
   material and does not break apart. It stays whole, standing, and when it
   goes over it goes over in one piece, like a fence post pushed at the top."
```

⭐ **Kural:** *malzemeyi tarif ederken filmin MEKANİĞİNİ de tarif et.*
Dış görünüş cümlesi (ne renk, ne dokulu) mekanik cümlesinden (nasıl
davranır) daha güçlüdür ve onu sessizce ezer. Mekanik cümlesi malzeme
cümlesinin **İÇİNE** yazılır, yanına değil.

⛔ **Genel mercekler bunu göremez ve göstermedi:** altı mercek 5.0-6.8
arası "orta" skorlar verdi çünkü hepsi tutarlı, hoş görünen bir filmi
ölçtü. Yanlış FİLM olduğunu yalnız filme özel kapı gördü. Bir mekaniği
olan her film için o kapı [C1 KURAL OKUNABİLİRLİĞİ] tek erken uyarıdır.

⚠️ **D123 ile ilişkisi:** 123 doğru sorunu çözdü ve yeni bir tane açtı.
İkisi birlikte okunur: *yasağı sil (123), ama yerine koyduğun tarifin
fiziğini ölç (124).*

---

**TEKRAR (02.09.2026 · THE LEANING ROOM):** aynı yuvarlanma, bu kez bir
KUMANDA yüzeyinde. Prompt 12 sahnenin hepsinde *"a brass hand wheel set into
the near edge of the table and one row of unmarked brass levers"* dedi ve
S0/S1/S3/S5'te tam olarak o üretildi: masaya gömülü DÜZ pirinç disk.
S7 ve S10'da aynı tarif **klasik parmaklıklı GEMİ DÜMENİNE** döndü.
Sebep D128'in kendisi: ceviz kaplama + pirinç + yıldız penceresi bir SETTİR,
ve o sette "wheel" kelimesinin en yakın eğitim-verisi nesnesi gemi dümenidir.
⛔ Reçete: jenerik adı GEOMETRİYLE ve ARKETİPİN NEGATİFİYLE yaz —
*"a flat brass disc set flush into the table edge, turned with the
fingertips; not a spoked ship's wheel, no spokes, no rim handles, nothing
standing upright above the table"*. Tema güçlüyse jenerik ad tek başına
tarif değildir, DAVETTİR.

## 🔴 DERS 138: METİN YASAĞI KOSTÜME YAZILDI, ÖLÇÜ ZEMİNE YAZILDI — MODEL ÖLÇÜYÜ ZEMİNE BASTI: HALKANIN İÇİNE "11 metres"

**Kaynak:** THE THIN ROOF QA (28.08.2026) — S2 · 21,0-23,0 s · ① KARE 7,2 · ⑤ ARKA PLAN 7,3
**Sorun:** deponun "sayı yaz, tarif yazma" doktrininin ilk ölçülmüş ters etkisi —
ve prompt kapısının imza denetiminde bir kör nokta

Filmin novum'u tek bir nesnedir: kaldırımdaki doğal soğuma çatlağı, 9 metre
yükseklikten **kapalı bir halka** olarak okunur. Halka kapısı geçti — daire
ekranda, kusursuz. Ama halkanın içine **yazı düştü**:

```
22,41 s karesinde, halkanın iç yayı boyunca:
  beyaz harflerle "11 metres"  +  bir sıra beyaz kertikli gradasyon yayı
  (ölçek çentikleri) + okunamayan ikinci bir etiket
21,0 s'te belirir, 23,0 s'te söner — filmin ASİMETRİ ANI'nın tam üstünde.
```

**Zincir üç halkalıdır ve üçü de belgede yazılıdır:**

```
① YASAK KOSTÜME YAZILDI
   promptun negatif cümlesi:
     "The suit carries no patch, no flag, no lettering, no digits and
      no symbol anywhere."
   → yasağın öznesi SUIT'tir. Zemin, kaya, gökyüzü yasaksızdır.
   KILAVUZ_REHBERI §5'in kapsamlı biçimi ("...on any display, surface,
   patch or sign") bu filmin promptlarına HİÇ yapıştırılmamıştı.

② ÖLÇÜ ZEMİNE YAZILDI — iki kez, görünür nesne cümlesinin içinde
     "a single continuous CURVED fracture, eleven point six metres across"
     "it is a closed ring, eleven point six metres across, and she is inside it"
     "a smooth unbroken arc, six to nine millimetres wide"
   → kadrajdaki bir yüzey işaretine bitişik ölçü. Diyagram, teknik çizim
     ve arazi ölçüm fotoğrafı eğitim verisinde TAM OLARAK böyle görünür.

③ KAPI GEÇİRDİ
   prompt_kontrol.py'nin "metin yasağı" imzası `no digits` kalıbını arıyor.
   Kostüme yazılmış cümlede `no digits` VARDIR. İmza eşleşti, dosya
   0 BLOCK / 0 FIX ile GO aldı. İmza KELİMEYİ arıyordu, KAPSAMI değil.
```

**İki ayrı zarar, aynı cümleden:**

```
① EKRANDA YAZI  — negatif çekirdeğin OTOMATİK BLOCKER kutusu
                  (filmin kendi C bloğu: "ekran metni = 0,0 s")
② NOVUM ÖLDÜ    — çentikli, metrajı yazılmış bir halka DOĞAL ÇATLAK
                  değildir; ölçülmüş bir saha işaretidir. "Kadın bilmiyor,
                  biz biliyoruz" dramatik ironisi çöker: halkayı biri
                  zaten ölçmüş ve işaretlemiştir.
```

⭐ **Kural: SAYI KİLİTTİR, TARİF DEĞİLDİR — ve kilit prompt GÖVDESİNDE
DURMAZ.** Ölçü SPEC'in D bloğunda ve planın fizik defterinde yaşar; image
prompt kadrajdaki nesneyi **nesne göreli ölçekle** anlatır.

```
✗ "a single continuous CURVED fracture, eleven point six metres across"
✓ "a single hairline fracture, no wider than a pencil line, packed with
   rust-coloured dust, curving in one unbroken sweep that closes on itself
   about four body-lengths out from her on every side"
```

⚠️ **Bu, AGENTS §8'in "tarif yerine sayısal kilit" kararını ÇÜRÜTMEZ, SINIRINI
ÇİZER:** sayı SPEC'te ve fizik defterinde kalır — orada ölçülür, orada
denetlenir. Prompt gövdesine indiği anda, kadrajdaki bir nesneye bitişikse,
model onu o nesnenin ÜSTÜNE basabilir.

**ÇÖZÜM — ① metin yasağı KAPSAMLI yazılır (KILAVUZ_REHBERI §5 biçimi):**

```
No readable text, letters, digits, numbers or symbols on any display,
surface, patch or sign — not on the suit, not on the equipment, and not on
the ground, the rock, the ice or any natural surface in the frame. Nothing
in this world has been measured, labelled, marked out or annotated by
anyone: no scale marks, no graduation ticks, no survey markers.
```

**ÇÖZÜM — ② prompt_kontrol.py'ye iki denetim eklendi (28.08.2026):**

```
DOSYA SEVİYESİ · "metin yasağı KAPSAMSIZ" (FIX, dosya başına TEK satır)
  metin yasağı imzası var + kapsam ifadesi yok  →  FIX
  (Depodaki filmlerin TAMAMI bu denetimden düşüyor: hiçbirinin metin
   yasağı kadraja değil, giysiye yazılmış. Bu yüzden bulgu prompt başına
   değil DOSYA BAŞINA yazılır — her prompta bir satır yazan kilit,
   kilit değil duvardır.)

PROMPT SEVİYESİ · "yüzey işaretine bitişik ölçü" (FIX, yalnız image)
  <işaret adı: fracture|crack|ring|arc|groove|seam|line|marking|…>
  aynı cümlede ve ÖNCESİNDE  +  <ölçü>  +  <boyut kelimesi: across|wide|
  in diameter|thick|deep>   →  FIX
  ⚠️ Boy ve mesafe ölçüleri ("1.68 metres tall", "2.83 metres long",
     "one metre from it") bu denetime GİRMEZ — 24 dosyalık taramada
     yalnız 4 dosya tetikledi.
```

⛔ **Ve altı QA merceği bunu görmedi.** ① KARE'nin negatif listesinde bu kutu
vardır ("Text, subtitles, captions, or watermarks visible on screen") ve
işaretlenmedi; ⑤ ARKA PLAN'ın 9. kategorisi bu hatayı adıyla arar
("No readable text, digits or symbols emerge anywhere in the field") ve
8/10 verdi. Sebep okunabilir: iki rubrik de metni **bindirme ya da kenar
artefaktı** olarak arıyor. Bu metin kadrajın ORTASINDA, sahnenin öznesinin
üstünde ve sahnenin kendi malzemesine gömülüydü.

**ÇÖZÜM — ③ ① ve ⑤ rubriklerine, metin kutusunun yanına:**

```
Emergent text is not only an overlay and not only an edge artifact. Look for
characters that belong to the scene's own materials — painted on a wall,
engraved in rock, stencilled on a hull, chalked on the ground, printed on a
label. Check the CENTRE of the frame and the surface the shot is ABOUT, not
only the edges. Text baked into the world reads as intentional set dressing
and survives review, and it is the more damaging case: a number with a unit
next to a natural object turns that object into a measured, man-made one.
```

> 🔗 Ders 34 (jenerik metni) · Ders 40 (diyalog tetikli altyazı) · Ders 50/A1
> (metin yasağı ↔ ekran içeriği çelişkisi) · Ders 70/72 (başlık kartı) ·
> Ders 73 (somut novum taşıyıcısı — burada taşıyıcının KENDİSİ bozuldu) ·
> Ders 124 (görünüş cümlesi mekanik cümlesini sessizce ezer — burada ölçü
> cümlesi yasak cümlesini ezdi) · Ders 139 (aynı desen, sırt yüzeyinde).

---

## 🔴 DERS 155: PROMPTUN KENDİ DEFTER ETİKETİ GİYSİYE BASILDI — "PHASE 1" GÖĞÜSTE, "EVA" SIRTTA; KAPSAMLI METİN YASAĞI VARDI VE YETMEDİ

**Kaynak:** THE PAYLOAD QA (01.09.2026) — ① KARE 4,5 (`0:10 🔴 Text "PHASE 1"
clearly printed on chest plate` · `1:18 🔴 Text "EVA" printed on suit back`) ·
② DEVAMLILIK karakter pasaportu: `Right chest reads "PHASE 1" (S1)` ·
`"EVA" on back (S7)` — **iki mercek birbirinden bağımsız olarak AYNI İKİ
DİZGEYİ yazdı.**
**Sorun:** D138'in reçetesi uygulanmıştı ve arıza tersine döndü — yasak
kapsamlıydı, dizge POZİTİF GÖVDEDEYDİ.

```
PROMPTTA NE VARDI (bu depoda ölçüldü, 01.09.2026):
  PART_A + PART_B'de  "Wear state: PHASE 1|2|3|4 — ..."   33 kez
  PART_A + PART_B'de  "matte slate-grey EVA shell"        25 kez
  Ve AYNI promptların negatif bloğunda, D138'in istediği kapsamla:
     "No readable text, letters or digits on any surface in frame"

EKRANDA NE ÇIKTI:
  göğüs plakasında  "PHASE 1"      (kir merdiveninin faz sayacı)
  sırtta            "EVA"          ("EVA shell" tamlamasının kısaltması)
```

⭐ **MEKANİZMA — YASAK DİZGEYİ SİLMEZ, GÖRÜNÜRLÜĞÜNÜ AZALTMAZ.** Model
promptu okur ve BÜYÜK HARFLİ bir simgeyi bir GİYSİ İSMİNİN yanında görür.
Eğitim verisinde büyük harfli kısa dizge + giysi = **o giysinin üstündeki
baskıdır**: NASA yamaları, itfaiye ceketi, kargo tulumu. "No readable text"
cümlesi bu eşleşmeyi bozmaz; çünkü yasak SAYFANIN BAŞKA BİR YERİNDEDİR ve
dizge hâlâ oradadır. Yasak "yazma" der, gövde "PHASE 1" der — model ikisini
birden yapar: yazıyı küçültür, giysiye basar.

⚠️ **VE TAŞIYICI BİZİM KENDİ DEFTERİMİZDİR.** `Wear state: PHASE n` bir
SAHNE TARİFİ değildir; D147'nin yazım aracıdır — kirin monotonik artışını
yazarın takip etmesi için icat edilmiş bir sayaçtır. Prompt gövdesine
kelimesi kelimesine indiği anda kadrajdaki bir nesnenin ETİKETİNE dönüştü.
Aynı şey `EVA shell` için geçerli: EVA bir kısaltmadır, tarif değil.

```
KAPSAM — bu iki dizge depodaki HEMEN HER FİLMDE var:
  · "EVA shell" ya da "EVA suit" — uzay filmlerinin ortak sözlüğü
  · "Wear state: PHASE n" — D147'den (27.08.2026) sonra yazılan her film
Bu ders tek filmin değil, YAZIM STANDARDININ düzeltmesidir.
```

**ÇÖZÜM — ÜÇ SATIR, ÜÇÜ DE YAZIM TARAFINDA:**

```
① FAZ SATIRI PROMPT GÖVDESİNE GİRMEZ. Kir merdiveni PLANDA ve SPEC'in
   C bloğunda yaşar. Prompta yalnız o fazın TARİFİ iner, etiketi değil:
   ✗ "Wear state: PHASE 3 — an even film of red dust covers the whole
      screen-left side of the suit"
   ✓ "an even film of red dust covers the whole screen-left side of the
      suit and both forearms, the three wear marks reading through it"
② KISALTMA YOK. Giysi, araç ve ekipman adlarında büyük harfli kısaltma
   kullanılmaz — model onu marka/baskı sanır:
   ✗ "matte slate-grey EVA shell"      ✗ "the EVA suit"    ✗ "MAV"
   ✓ "matte slate-grey surface suit"   ✓ "the pressure suit"
③ PROMPT GÖVDESİNDE BÜYÜK HARFLİ DİZGE = BASKI ADAYI. Vurgu için
   kullanılan kapitaller (NEVER, EXACTLY, PHASE) yalnız NEGATİF blokta
   ve TIMELINE fiillerinde kalır; giysi/gövde/nesne tarif eden cümlede
   büyük harfli tek kelime bulunmaz.
```

⛔ **BETİK TARAFINA ÖNERİ (henüz kodda yok):** `prompt_kontrol.py` pozitif
gövdede `\b[A-Z]{2,}\b|\bPHASE \d\b` arar ve giysi/gövde ismine 60 karakter
mesafede duruyorsa FIX verir. D138'in denetimi KELİMEYİ arıyordu; bu denetim
BİÇİMİ arar.

> 🔗 Ders 138 (metin yasağının KAPSAMI — reçetesi buradaydı ve yetmedi:
> kapsam gerekli, yeterli değil) · Ders 147 (faz satırının kendisi — bu ders
> onu prompt gövdesinden ÇIKARIR) · Ders 45/34 (özel ad yazılmaz — aynı
> ailenin ilk üyesi) · Ders 13 (ekrana anlamsız yazı) · Ders 59 (pozitif
> tarif) · Ders 124 (görünüş cümlesi mekanik cümlesini ezer).

---

## 🔴 DERS 167: YEDİ KİMLİK ÖZNİTELİĞİ ÜST ÜSTE = "BİR ÜNLÜYÜ TARİF EDEREK İSTEME" KALIBI — VE AÇIK VİZÖR KİLİDİ O KALIBI BÜYÜTÜYOR

**KAPI:** BETİK · `prompt_kontrol.py` ⑲ KİMLİK YIĞINI (aynı cümle bölgesinde ≥4 kişi özniteliği) — 02.09.2026
**TEKRAR:** 1 · 02.09.2026 THE SINKING STAKE (motor OMNI, red defteri vaka 15)

**Kaynak:** THE SINKING STAKE üretimi (02.09.2026) — sahibin bildirdiği red,
çok sahnede tekrarladı ve üretimi durdurdu:
`"There are a lot of people I can help with, but I can't depict some public
figures. Do you have anyone else in mind?"`
**Sorun:** filmde gerçek hiç kimse yok, hiçbir özel ad geçmiyor, milliyet 0,
`prompt_kontrol ⑯` T1/T2 temiz ve kapı GO vermişti. Yine de reddedildi.

```
PROMPTTA NE VARDI — tek kişide YEDİ kimlik özniteliği, tek cümlede:

  "THE TALLER ONE is about one hundred eighty-eight centimetres,
   broad-shouldered, dark brown skin, close-cropped grey hair,
   deep lines at the outer eyes, mid-fifties."
   ① kesin boy  ② gövde  ③ ten rengi  ④ saç rengi  ⑤ saç biçimi
   ⑥ yüz işareti  ⑦ yaş

VE BU YIĞIN:  İKİ kişide × 25 imaj promptunun 25'inde, kelimesi kelimesine.
```

⭐ **MEKANİZMA — SINIFLANDIRICI NİYETİ DEĞİL BİÇİMİ OKUR.** "Şu ünlüyü çiz"
isteğinin bilinen kaçamağı, adı yazmayıp kişiyi TARİF ETMEKTİR: boy + ten +
saç + yaş + yüz işareti. Bu depo tam olarak o biçimi yazıyor — masum bir
sebeple (D34 özel adı yasaklıyor, o yüzden kimlik tarife taşınıyor) ama
sınıflandırıcı sebebi görmez, kalıbı görür. Öznitelik sayısı arttıkça
"belirli bir gerçek insan" olasılığı yükselir.

⛔ **VE PANZEHİR TETİKLEYİCİYİ BÜYÜTÜYOR — İKİ KİLİT TERS YÖNE ÇEKİYOR:**

```
D79 (06.08.2026)  her prompta yazdırıyor:
   "the face is fully readable through it in every frame, at every head angle"
   Sebep sağlam: aynalı vizör iki filmde üretildi, yokluk kilidi tutmadı.

KART 12 (01.09.2026) diyor ki:
   "KASK/VİZÖR → anonimlik/deepfake imzasına yakın okunuyor.
    ✅ Panzehir ZATEN VAR: D79 açık vizör kilidi."
   ve AYNI kart, üç satır aşağıda:
   "KALABALIK → her yüz ÜNLÜ/yaş/deformasyon için TARANIR."

⭐ AÇIK VİZÖR BİRİNCİ RİSKİ DÜŞÜRÜR, İKİNCİSİNİ YÜKSELTİR.
  Kart birinci yönü biliyor, ikinci yönü bilmiyor, ve panzehir olarak
  yazdığı şey ikinci yönün tetikleyicisi. Bu filmde ikisi çarpıştı:
  iki okunur yüz × 25 prompt × yedi öznitelik.
```

**ÇÖZÜM — YÜZ GÖRÜNÜRLÜĞÜ İLE KİMLİK TARİFİ AYRILIR (dört satır):**

```
① VİZÖR AÇIK KALIR. D79 iptal edilmez — risk vizörde değil TARİFTEDİR.
② KİMLİK YIĞINI PROMPT GÖVDESİNDEN ÇIKAR, PLAN'da ve REFERANS
   PAKETİNDE kalır. Prompta yalnız SİLUET iner.
   ✗ "one hundred eighty-eight centimetres, broad-shouldered, dark brown
      skin, close-cropped grey hair, deep lines at the outer eyes,
      mid-fifties"
   ✓ "the taller of the two, broad through the shoulders"
③ BOY GÖRELİ YAZILIR, SAYIYLA DEĞİL: "a head taller than the other".
   Kesin boy hem kimlik özniteliğidir hem D138'in ölçü-etiket riskidir —
   tek cümlede iki ayrı kapıya takılır.
④ YÜZ TARİFİ YALNIZ YÜZÜN KONU OLDUĞU SAHNEDE. Göz bütçesi kaç sahne
   istiyorsa o kadar (KARAKTER_VE_DUYGU §6: 3-5 dk'da 3-4). Kalan
   sahnelerde vizör "optically clear" der ve DURUR.
```

⭐ **VE ASIL ÖLÇÜM ŞU:** bu filmde ayırt etme yükü zaten GEOMETRİDEYDİ
(göğüs boyunduruğu ↔ düz göğüs · dört cep ↔ sarılı halat). Yüz tarifi
25 sahnenin 21'inde **hiçbir iş yapmadan** sınıflandırıcı yüzeyi üretiyordu.
Kaldırılan şey filmden hiçbir şey götürmez.

> 🔗 Ders 34/45 (özel ad yazılmaz — kimliği tarife İTEN ders; bu ders o
> tarifin sınırını koyar) · Ders 79 (açık vizör — korunur, daraltılmaz) ·
> Ders 138 (ölçü prompt gövdesinde etikete döner) · Ders 123 (yasak
> kelimeyi prompta sokar — aynı aile: niyet değil biçim ölçülür) ·
> KART 12 · POLITIKA_VE_URETILEBILIRLIK §1 · red defteri vaka 15.

---

## 🔴 DERS 179: İMAJ PROMPTU DEĞİŞİMİN *SONRASINI* YAZDI — I2V'DE İMAJ t=0'DIR, VE FİLMİN BEDELİ HİÇ EKRANA GELMEDİ

**KAPI:** BETİK · `prompt_kontrol.py` ⑳b DEĞİŞİM KAPISI
**TEKRAR:** 0

**Kaynak:** THE HEALING GROUND · 04.09.2026 · ⑪ ÖLÇÜM + prompt dosyası
(rapordan DEĞİL). Kareler 111 s ↔ 119 s, aynı kurulum.
④ HİKAYE mod V'de "no thematic cost is paid" · "no peak located" yazdı ve
ikisi de ⑩ ÖNERME KAPISINDAN GEÇTİ.

**Sorun:** Filmin bütün anlamı tek jestteydi — *göğüs kapağını açar,
ısıtıcıyı kapatır, kalçasındaki buhar tüyü söner.* Sahnenin **video**
promptu bunu doğru yazmıştı:

```
0.0s — ... A short white vapour plume stands at his hip.
2.0s — he reaches inside and turns one plain recessed switch. The plume at
       his hip thins, drops and goes out
```

Aynı sahnenin **imaj** promptu ise şunu yazıyordu:

```
... its hinged cover standing open. ... There is no vapour plume at his
hip: the vent is dark and still. ... Around the dark disc under his gloves
there is no vapour
```

İmaj promptu, video promptunun **onuncu saniyesini** tarif ediyor. I2V
hattında imaj **t=0**'dır. Modelden, başlangıç karesinde bulunmayan bir
tüyü söndürmesi istendi; o da tüyü **başka bir yere** (zemindeki diske)
koyup onu söndürdü. Ekranda:

- göğüs kapağı **hiç açılmadı**, el **hiç içeri girmedi**, anahtar **hiç görünmedi**
- tüy kalçada değil **diskte** çıktı
- geriye kalan okuma: *"bir adam bir tabağın üstünde duruyor ve buhar kesiliyor"*

**Bedel yazıldı, sebebi üretilmedi.** Bir izleyicinin göremediği bir seçim,
bedel değildir; film "kamera taşıyıcı" olarak okundu.

⚠️ Planın da payı var: sahnenin kurulumu **24mm EWS · 40 m**. Kırk metreden
bir kalça tüyünün sönmesi üç pikselik bir olaydır. **Film merkezî seçimini
kendi EN GENİŞ kurulumuna yazmıştı.**

**ÇÖZÜM:**

```
① İMAJ PROMPTU HER ZAMAN 0,0 SANİYEYİ YAZAR — SAHNENİN SONUCUNU DEĞİL.
   Değişim taşıyan sahnede imaj promptu, video promptunun `0.0s —`
   satırıyla KELİME KELİME uyumludur.
   ✗ imaj: "there is no vapour plume at his hip"
     video: "0.0s — a short white vapour plume stands at his hip"
   ✓ imaj: "a short white vapour plume stands at his hip, 14 cm tall"
     video: "0.0s — the plume stands at his hip · 2.0s — it thins and goes out"

② ⑳b DEĞİŞİM KAPISI (betik): sahne başlığında `BEDEL SAHNESİ` ya da
   `MERKEZÎ SEÇİM` geçiyorsa — betik video promptunun `0.0s` satırındaki
   durum nesnesini alır ve İMAJ promptunda o nesnenin OLUMSUZUNU
   (`no <nesne>`, `zero <nesne>`, `<nesne> ... dark and still`) arar.
   Bulursa ⛔ BLOCK: iki prompt aynı sahnenin iki farklı anını tarif ediyor.

③ BEDEL SAHNESİ, FİLMİN EN GENİŞ KURULUMUNA YAZILMAZ.
   Sayısal kilit: bedeli taşıyan değişim, kadrajın kısa kenarının
   **en az 1/8'i** kadar yer kaplar. 40 m'den 14 cm'lik bir tüy
   1/300'dür → o sahne CU/MS'e iner ya da bedel başka bir kanala taşınır.
```

> 🔗 Ders 157 (taşıyıcı TEK KARE satırında) · Ders 151 (mercek vuruşu
> göremez) · Ders 172 (novumun yerine tanıdık mekanizma geçer) ·
> Ders 122 (zaman hesaplanmaz, hesaplatılır) · `ONERME_VE_NOVUM §4①` ·
> `03_PLAN_ONCESI` B5 BEDEL maddesi.

---

## 🔴 DERS 203: PLANIN REPLİK ENVANTERİ PROMPTA HİÇ GEÇMEDİ — SPEC YEDİ MAKİNE REPLİĞİ İLAN ETTİ, OTUZ PROMPTUN HİÇBİRİNDE TIRNAK YOKTU, FİLM REPLİKSİZ DOĞDU VE ③ SES BUNA 9/10 VERDİ

**KAPI:** BETİK · `PROMPT_KONTROL/prompt_kontrol.py` ㉓ REPLİK ENVANTERİ (klasör modu: SPEC A
`DIALOGUE LINES: N` ↔ prompt gövdelerinde tırnaklı replik sayısı · 0 → BLOCK · < N → FIX) —
13.09.2026 · ölçen mercek: ⑬ UYUM (🅑 prompt boşluğu) · ③ SES (`SPOKEN LINES: 0` + SPEC N>0)
**TEKRAR:** 1 · 13.09.2026 THE STATIC SHADOW · geriye dönük 09.09.2026 THE MIRROR FAUNA
(SPEC 11 insan repliği · promptta 0 · mod D ③ bir uydurma replik duydu: *"Come front to you take."*)

**Kaynak:** THE STATIC SHADOW QA (13.09.2026) — on iki mercek `LINES HEARD: none`; ③ SES
`STATE B — NO VOICES, SOUND ONLY`, SFX senk 9/10. Plan `📋 REPLİK ENVANTERİ`: 7 HELIOS satırı
(S01 · S02 · S06 · S08 · S09 · S11 · S15). SPEC A: `DIALOGUE LINES: 7 · MACHINE 7`.
`grep -c '"' THE_STATIC_SHADOW_BOLUM_1.md THE_STATIC_SHADOW_BOLUM_2.md` → **0 · 0**.
`00_ANALIZ/03_SAHNE_SIRALAMASI.md`'de "replik yerleşimi" adımı da boş.

**Sorun:** Replik bu depoda ÜÇ yerde yaşar — plan (envanter), SPEC (sayı + register), prompt
(tırnak içi, VEO kılavuzu §3). Üçüncüsü olmadan ilk ikisi HİÇBİR ŞEY üretmez: video modeli
planı görmez. Film repliksiz doğdu ve filmin ÖNERMESİ replikle taşınıyordu — gölge kayması
sayısı, "dört dakika", "Abort", "Shadow lock stabilized". ④ HİKAYE filmi "manuel yanaşma
gerilimi" diye okudu; planın sorusu ("500 m'lik kalkan neden yalpalıyor?") ekranda hiç
sorulmadı. ③'ün 9/10'u yalan değil: mercek belgesizdir, duyduğu sesin planla uyuşmasını
ölçemez — SPEC'i yalnız ㉓ okur.

⭐ **İkinci vaka geriye dönük ve daha kötü:** THE MIRROR FAUNA (09.09.2026, deponun İLK mod D
partisi) SPEC'te 11 insan repliği ilan etti, 30 promptun hiçbirinde replik yoktu; model
1:03'te anlamsız bir cümle uydurdu ve ③ onu tek replik olarak kaydetti. Sekiz mercek mod D
koştu ve hiçbiri "SPEC 11 diyor, 1 duydum" demedi — çünkü rubrik ③'e SPEC vermez (tasarım).

**ÇÖZÜM — kapı yazım tarafında, QA tarafında değil:**

```
㉓ prompt_kontrol.py klasör modu (13.09.2026):
   SPEC A `DIALOGUE LINES: N`  (N = 0 → kapı sessiz)
   prompt gövdelerinde tırnaklı replik sayısı q  (düz " " ve “ ” · satır sonunu aşabilir · ≤240 karakter)
   q = 0        → ⛔ BLOCK  "SPEC N replik ilan ediyor, promptlarda tırnaklı replik 0"
   0 < q < N    → ⚠️ FIX
KALİBRASYON 38 SPEC · 13.09.2026:
   gerçek pozitif 2  — STATIC SHADOW 7→0 · MIRROR FAUNA 11→0
   yanlış pozitif 0  — HEALING GROUND 4=4 · HARD DOCK 8≤18 · WHITE FLOOD 16>15 (yalnız FIX)
   ⚠️ ilk sürüm satır sonunu aşan tırnağı saymıyordu ve LOSS OF LIFT (1) ile BORROWED WEIGHT
     (4) BLOCK aldı; ikisinin repliği de promptta VARDI, 78. sütunda kırılmıştı → düzeltildi
```

⛔ Yazım kuralı (kapının ölçtüğü cümle): **replik prompta tırnak içinde girer; planın envanteri
prompt DEĞİLDİR.** Bilinçli sessiz filmde SPEC `DIALOGUE LINES: 0` yazar — 7 yazıp 0 vermek,
SPEC'in ③'e söylediği ilk yalandır.

🔗 [[D122]] (replik zamanı hesaplatılır — önce replik var olmalı) · [[D82]] · [[D129]]
(SPEC var, mod V) · [[D188]] (aynı filmde teslim eksiği) · `SES_VE_DIYALOG_URETIM_KILAVUZU` §2a


---

## 🔴 DERS 214: KADRAJDA OLMAYAN BEDEN TARİF EDİLDİ — "SELF-CONTAINED" BIBLE'IN TAMAMI DEMEK DEĞİLDİR; MODEL YAZILANI KADRAJA SOKAR

**FREKANS:** 3 film + 1 ölçüm · YERÇEKİMİ FAZ 3 (mod V — ADAY-5: kask ×4 + saç ayrıntısı, kapsayan nesne düştü) · THE UPWARD FALL (⑪ ölçüm kapısı 186 s — ADAY-8: WORLD bloğu tam anatomi, tek-uzuv kadrajda iki bacak) · THE HEALING GROUND (S4 kare 45 s — ADAY-9: kolu yazılmayan eldiven kopuk doğdu, ikinci mürettebat okundu) · THE LOCKED_PULSE (13.09.2026 prompt ölçümü, 0 kare: 10/10 close-up/insert promptu tam yüz tarifi taşıyor; promptun %57'si her sahnede aynen tekrar)
**DEĞİŞEN SATIR:** Her promptun ilk satırı `IN FRAME: face · hands · torso · legs · full body · back | none`; SUBJECT bloğu **yalnız** IN FRAME'dekini tarif eder — yüz kadrajda değilse yüz cümlesi yok, sırt kadrajda değilse sırt cümlesi yok; devamlılık I2V'nin onaylı karesiyle taşınır (`START FRAME:` tek satır)
**KAPI:** BETİK · `prompt_kontrol.py` ㉖ KADRAJ ENVANTERİ (IN FRAME satırı zorunlu; kadrajda olmayan yüz tarifi → BLOCK — 14.09.2026, yeni rejim)
**TEKRAR:** 0

**Kaynak:** THE HEALING GROUND S4 (04.09.2026) prompt dosyası + kare 45 s — ADAY-9. Zincir ADAY-5 · 6b · 8 · 9; LOCKED_PULSE ölçümü `TODO_AKIS_VE_DERS_REFORMU.md` TEŞHİS ②.

**Örüntü:** Kural ③ ("BIBLE'a bak atfı yasak, prompt self-contained") Character Bible'ın tamamını her prompta soktu: 75 mm insert'te yüz, sırttan çekimde göz rengi, tek-uzuv kadrajda tam anatomi. Model yazılan her şeyi kadraja sokmaya çalışır; kadrajda olmayanı yazmak ikinci bacak, ikinci mürettebat, ezilen kask üretir. Deponun ölçümü zaten söylüyordu: tarif kilidi %0 tuttu — tekrar eden 2.300 karakterin etkisi sıfır, maliyeti sıfır değil.

**ÇÖZÜM:** `IN FRAME` satırı + kelime bütçesi (IMAGE ≤ 250 · VIDEO ≤ 300, `prompt_kontrol.py` `KELIME_BANDI`). Self-contained = **kadrajdaki** her şey promptta; kadraj dışı hiçbir şey promptta değil. Negatif çekirdek 8 cümle (`KILAVUZ` §5), gerisi PLAN'da.

🔗 [[D174]] · [[D175]] · [[D176]] · [[D179]] · [[D79]] · AGENTS §2 kural ③ (14.09.2026 notu)

---

## 🔴 DERS 215: EKRAN METNİ, FİLİGRAN VE HAREKETSİZ AĞIZ ARAÇ AYARIDIR — PROMPT CÜMLESİ DEĞİL; ÜRETİM DEFTERİNE ÜÇ KUTU, KURGU KAPISINA ÜÇ SAYI

**FREKANS:** 6 film · THE STANDING WIRE (⑤ çapraz kapı — ADAY-10: sıfır replikli filmde dört cümle duyuldu) · THE AMBER LATTICE (⑤ 7 — sağ altta jeneratör logosu 0:01-1:39) · THE CRACKED HELMET (① V 5,3 — vizör dış yüzeyine yapışık HUD metni) · THE RING WALKER (① 5,3 — 1:50 "THE RING WALKER" burned-in başlık) · LOW_POWER (③ 4,3 — 01:31 MCU'da replik oynarken ağız hareketsiz) · YERÇEKİMİ F5-F7 (ADAY-7, KAPANDI — altyazı sebebi ARAÇ, kapı yazılmaz)
**DEĞİŞEN SATIR:** `<FILM>_URETIM_DEFTERI.md` motor satırı üç kutu — `altyazı/caption: KAPALI` · `filigran: YOK (ücretli katman/ayar)` · `konuşan ağız: kadraj dışı` — ve kurgu kapısı ④'te üç sayı: ekran metni **0 s** · filigran **0** (`rapor_kontrol.py --olcum-filigran`) · kadrajda konuşan ağız **0** klip
**KAPI:** BETİK · `rapor_kontrol.py --olcum-filigran` · LİSTE · `FILM_KLASOR_SABLONU/FILM_URETIM_DEFTERI.md` motor satırı
**TEKRAR:** 0

**Kaynak:** THE RING WALKER QA (10.09.2026) — ① `1:50 — Burned-in title text ("THE RING WALKER") appears on screen, violating series no-text rule`. Zincir ADAY-10 · 20 · 34 · 45 · 64 (+7 kapalı).

**Örüntü:** Altı filmde ekranda metin/logo/altyazı ya da konuşurken kapalı ağız çıktı ve her seferinde NEGATIVE bloğuna bir cümle daha eklendi. ADAY-7'nin kapanışı sebebi ölçtü: **araç ayarı** (caption toggle, ücretsiz katman filigranı, lip-sync modu). Negatif cümle bir araç ayarını değiştiremez; 50 no/never/not içeren çekirdek bunu 6 filmde kanıtladı. Ağız içinse çözüm zaten yazılıydı (`SES_VE_DIYALOG` §2a: konuşan ağız kadraj dışı) — kapısı yoktu.

**ÇÖZÜM:** Üç kutu üretimden önce üretim defterinde işaretlenir; işaretsiz kutuyla üretilen klip kabul edilmez. Kurgu kapısı ④ üç sayıyı masterda ölçer. NEGATIVE bloğuna bu konuda **yeni cümle eklenmez** (`KILAVUZ` §5 8 cümle).

🔗 [[D34]] · [[D40]] · [[D21]] · [[D72]] · [[D101]] · [[D35]] · ADAY-7 kapanışı
