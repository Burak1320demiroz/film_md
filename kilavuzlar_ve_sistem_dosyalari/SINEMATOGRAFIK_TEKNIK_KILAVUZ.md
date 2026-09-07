# 🎬 SİNEMATOGRAFİK TEKNİK KILAVUZ — AI Film Promptları İçin

> Bu kılavuz, profesyonel sinema tekniklerinin AI video üretim promptlarına
> nasıl entegre edileceğini sistematize eder. Her yeni film senaryosunda
> bu teknikleri prompt'lara uygulamak, görsel kaliteyi TV estetiğinden
> sinema estetiğine taşır.
>
> **İKİ BÖLÜMLÜ:**
> **§1-§8** — uygulama katmanı: ışık, hareket, doku, kompozisyon, geçişler.
> **§9-§17** — sinema tekniğinden prompt diline çeviri: hangi teknik prompta
> yazılır ✅, hangisi post-prodüksiyonda yapılır 🎨, hangisi bu hatta hiç
> girmez 📚. Şüphede kalınca **§17 karar tablosuna** bak.

---

## 1. 💡 IŞIKLANDIRMA PSİKOLOJİSİ

### 1.1 Motivasyonlu Işıklandırma (Motivated Lighting)

Işığın sahnede **mantıklı bir kaynağı** olmalıdır. AI jeneratörleri
kaynak belirtilmediğinde düz (flat) televizyon estetiğine kayar.

| Durum | Prompt Tetikleyici | Psikolojik Etki |
|---|---|---|
| Gerilim / Şüphe | `harsh shadows, high contrast, single directional light source` | Bilgi eksikliği hissi, klostrofobi |
| Nostalji / Melankoli | `warm golden hour lighting, soft motivated practical lights` | Geçicilik, duygusal bağ |
| Huşu / Keşif | `volumetric light shafts, cathedral-like beams, dust motes in light` | Kutsallık, büyüklük |
| Distopya / Yabancılaşma | `high contrast neon lighting, cold blue-white against deep shadows` | Yapaylık, tehdit |
| Masumiyet / Umut | `diffused daylight, bright cloudless sky bathing the scene` | Saflık, başlangıç |

### 1.2 Prompt'a Eklenecek Işık Bloğu

Her sahne promptunda ışık kaynağı açıkça belirtilmelidir:

```
MOTIVATED LIGHTING RULE: Every light source in this scene must have a
VISIBLE, LOGICAL ORIGIN within the frame or just outside it (a window,
a lamp, a star, a helmet light, a glowing surface). Light must NOT
appear from nowhere. Deep clean shadows, restrained highlights,
cinematic color grade. Light quality must match the emotional tone:
[WARM/COLD/MIXED] with [SOFT/HARSH] shadows.
```

### 1.3 Renk Sıcaklığı Haritası

Sahne boyunca renk sıcaklığı tutarlı olmalı, ancak **duygusal
geçişlerde** bilinçli kayma yapılabilir:

```
SOĞUK (3000K-4500K): Tehlike, yalnızlık, uzay, teknoloji
NÖTR (5000K-5500K): Gerçekçilik, gündüz, keşif
SICAK (5500K-7000K): Nostalji, güvenlik, insanlık, umut

GEÇİŞ: Bir sahne içinde renk sıcaklığı kademeli olarak değiştirilirse
(sıcaktan soğuğa veya tersine), karakterin iç dünyasındaki değişim
görselleştirilmiş olur — diyalog olmadan duygu aktarımı.
```

---

## 2. 📷 KAMERA HAREKETLERİ VE ANLATIMSAL İŞLEVLERİ

### 2.1 Hareket Sözlüğü

| Hareket | Prompt Terimi | Ne Zaman Kullanılır | Anlatısal İşlev |
|---|---|---|---|
| Push-in | `slow push-in toward subject` | Duygusal kırılma, keşif anı | Dış dünyadan karakterin zihnine geçiş |
| Pull-back | `slow pull-back reveal` | Ölçek şoku, final | Karakterin küçüklüğünü ortaya çıkarma |
| Pan | `horizontal pan left/right` | Mekan tanıtımı, takip | Çevrenin genişliğini gösterme |
| Tracking | `lateral tracking shot following subject` | Aksiyon, yürüyüş | Karakterle birlikte hareket, empati |
| Tilt | `vertical tilt up/down` | Mimari büyüklük, otorite | Devasalık veya güç ilişkisi |
| Orbit | `slow orbital camera around subject` | Karar anı, dönüm noktası | Zamanın durması, odaklanma |
| Aerial | `drone-style aerial sweep, wide-angle` | Establishing shot, dünya tanıtımı | İzleyiciye filmin dünyasını açma |
| Static | `locked-off camera, static frame` | Gerilim, gözlem | Voyeuristik mesafe, rahatsızlık |
| Rack Focus | `rack focus from foreground to background` | Bilgi açığa çıkarma | Dikkat yönlendirme, hiyerarşi |

### 2.2 Hız Kuralı

```
KAMERA HIZI = DUYGU HIZI

YAVAŞ hareket (push-in, tilt, orbit) → Duygu, meditasyon, huşu
ORTA hareket (tracking, pan) → Keşif, takip, süreklilik
HIZLI hareket (whip pan, quick track) → Kaos, panik, aksiyon

BİZİM SERİMİZ: Çoğunlukla YAVAŞ. Huşu ve melankoli tonu
yavaş, kasıtlı kamera hareketleri gerektirir.
```

---

## 3. 🔬 OPTİK VE DOKU GERÇEKÇİLİĞİ

### 3.1 Alan Derinliği (Depth of Field)

```
SHALLOW DOF (f/1.4 - f/2.8): Karakter yakın çekim, duygusal an,
  izolasyon. Arka plan yumuşak, karakter keskin.
MEDIUM DOF (f/4 - f/5.6): Karakter + yakın çevre. Standart keşif.
DEEP DOF (f/8 - f/11): Geniş manzara, ölçek şoku. Her şey keskin.

KURAL: Alan derinliği DOĞAL LENS DÜŞÜŞÜ (natural lens falloff)
ile simüle edilmeli — yapay, uniform bulanıklık (artificial blur)
ASLA kullanılmamalı.
```

### 3.2 Doku Gerçekçiliği (Texture Pass)

AI'nin "pürüzsüzleştirme" eğilimine karşı her promptta:

```
TEXTURE FIDELITY RULE: Maintain photographic micro-detail throughout:
- Skin: visible pores, natural subsurface scattering, micro-wrinkles
- Fabric: visible weave pattern, thread texture, wear marks
- Metal: realistic reflections, oxidation, micro-scratches
- Stone/Rock: grain structure, mineral variation, weathering
- Dust: individual particles visible in light beams
NO artificial beautification, NO smoothing, NO plastic appearance.
The image must look captured by a real camera, NOT rendered.
```

### 3.3 Anamorfik Lens Etkisi (Opsiyonel)

Bazı sahnelerde derinlik ve "sinema filmi" hissi için:

```
ANAMORPHIC LENS: Subtle anamorphic lens characteristics —
horizontal lens flare streaks, slight edge softness and barrel
distortion at frame edges, oval bokeh shapes in out-of-focus areas.
Creates organic, imperfect, film-like quality.
Referans: Cooke Xtal Express 32mm (Ex Machina tarzı).
```

---

## 4. 🎭 TEMATİK ÇERÇEVELER

### 4.1 "1 Klip = 1 Fikir" Kuralı

Her sahne TEK BİR duygusal/tematik fikri işlemeli. Çok fazla
görsel unsur veya çatışan tema = izleyici odağı dağılır.

### 4.2 Türe Özgü Prompt Şablonları

**EPİK KEŞİF (Bizim serimizin ana tonu):**
```
Contemplative, awe-inspiring atmosphere. Slow deliberate camera
movement. The human figure is small against the vast environment.
Scale contrast between character and world. Silence or minimal
ambient sound. The tone is archaeological wonder, not action.
```

**SİBERPUNK / FÜTÜRİSTİK:**
```
Neon-lit cyberpunk aesthetic, dynamic tracking shot, quick pans,
high contrast lighting, rain-slicked surfaces reflecting neon,
lived-in urban decay juxtaposed with gleaming technology.
```

**PSİKOLOJİK GERİLİM:**
```
Locked-off camera, shallow depth of field, warm practical tungsten
lights, glass reflections masking the subject, claustrophobic
framing, suspenseful atmosphere. Motivated lighting only.
```

**MELANKOLİ / KAYIP:**
```
Golden hour warm lighting fading to cool blue, slow push-in on
subject's face, shallow DOF isolating the character from the
background, contemplative stillness, visible breath or tears.
```

---

## 5. 🔗 GÖRÜNMEZ GEÇİŞLER (Sahneler Arası Köprüler)

> 📎 **Bu bölümün genişletilmiş hâli ayrı bir kılavuzdadır:**
> `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` — gizli geçiş kütüphanesi
> (6 teknik + prompt kalıpları), geçişin üç şartı, omurga lens,
> mesafe/süre denklemi ve 360° aydınlatma.

### 5.1 Eşleştirme Kesmesi (Match Cut)

Bir sahnenin son karesiyle sonraki sahnenin ilk karesinin
**görsel olarak eşleştirilmesi**. Örnek: Sahne A'nın sonunda
yuvarlak bir göz bebeği → Sahne B'nin başında yuvarlak bir gezegen.

```
Bizim serimiz için uygulanabilir eşleştirmeler:
- Fener ışık huzmesi → güneş ışın demeti
- Vizör yansıması → göl/su yansıması
- Yuvarlak kask vizörü → yuvarlak gezegen
- Karanlık koridor → karanlık mağara ağzı
- Mavi Photonic Memory glow → mavi bioluminesan mantarlar
```

### 5.2 Eylem Sürekliliği (Action Continuity)

Sahne sonu ve sahne başı arasında hareketi sürdürmek:

```
Sahne A sonu: Karakter sağa doğru yürüyor, headlamp sağa bakıyor.
Sahne B başı: Karakter sağdan giriyor, headlamp sağa bakıyor.
→ Hareket yönü, vücut açısı ve ışık yönü eşleşmeli.
```

### 5.3 Ses Köprüsü (J-Cut)

Bir sonraki sahnenin sesi, mevcut sahnenin görüntüsü hâlâ
ekrandayken başlar. Bu, mekan değişimlerini yumuşatır:

```
MÜZİK PROMPTU: Sahne geçişlerinde müzik kesintisiz devam etmeli.
Yeni sahnenin ortam sesi (rüzgar, su, metal tıkırtısı) bir önceki
sahnenin son 2 saniyesinde kısık olarak başlamalı.
```

### 5.4 Işık Geçişi

Sahne içinde ışık kaynağının değişmesi, kesme olmadan
atmosfer değişimini sağlar:

```
PRATIK IŞIK GEÇİŞİ: Sahne içinde ışık titremesi (flickering)
veya renk sıcaklığı kayması (warm→cold shift) kullanılarak,
tek bir uzun planda bile atmosferin "kırılması" mümkündür.
Bu teknik, kesmeleri maskelemek için de kullanılabilir.
```

---

## 6. 🎬 PROFESYONEL REFERANS FİLMLER

### Prompt'larda Kullanılabilecek Sinematografik Referanslar

| Referans | Stil Kodu (Prompt Tag) | Hangi Filmimiz İçin |
|---|---|---|
| **Ex Machina** (Rob Hardy) | `Shallow DOF, locked-off camera, warm tungsten practicals, glass reflections, claustrophobic brutalist architecture` | Hollow Station (kapalı mekan, cam yansımaları) |
| **Ghost in the Shell** (Oshii) | `Contemplative slow pan, daylight bathing, lived-in futuristic city, melancholic stillness, contemplative montage` | Forgotten Architects (dev yapılar, sessiz montaj) |
| **Blade Runner 2049** (Deakins) | `Volumetric lighting, heavy fog/haze, color-blocked environments, monolithic scale` | Eternal Engine, Last Archive (sis, ölçek) |
| **Annihilation** (Garland/Hardy) | `Psychedelic mutation, organic+synthetic fusion, directional shadows on creatures, alien biology` | Glass Abyss, Canopy World (organik uzaylı çevre) |
| **Arrival** (Villeneuve/Young) | `Overcast diffused light, curved alien surfaces, extreme scale contrast, quiet tension` | Hollow Station (uzaylı mimari, ölçek) |
| **Gravity** (Lubezki) | `Single long take, zero-g floating, Earth reflected in visor, debris fields, silence` | Hollow Station (sıfır-g, vizör yansımaları) |
| **2001: A Space Odyssey** (Kubrick) | `Symmetrical composition, sterile white interiors, slow deliberate movement, cosmic scale` | Hollow Station (istasyon iç mekanları) |
| **Stalker** (Tarkovsky) | `Slow tracking through ruins, overgrown nature reclaiming technology, contemplative stillness` | Forgotten Architects (doğa + kalıntılar) |
| **It Follows** (Gioulakis) | `Revolving camera, suburban mundanity as threat, giallo color palette` | — (gerilim filmleri için) |

---

## 7. 📐 KOMPOZİSYON KURALLARI (Güncelleme)

### 7.1 Çerçeve İçi Hiyerarşi

```
HER KAREDE 3 KATMAN:
1. ÖN PLAN: Derinlik veren çevre detayı (duvar kenarı, dal, toz)
2. ORTA PLAN: Karakter + ana etkileşim
3. ARKA PLAN: Ölçek referansı (devasa yapı, gezegen, gökyüzü)

LIDER ÇİZGİLER: Çevre elementleri (koridor duvarları, ağaç dalları,
enerji damarları) karaktere veya sahnenin odak noktasına doğru
YÖNLENMELI — izleyicinin gözünü çerçeve içinde kasıtlı olarak
hareket ettir.
```

### 7.2 Negatif Alan (Negative Space)

```
İzleyiciye "nefes alma" alanı bırak. Karakter çerçevenin
kenarlarından birine (genellikle alt 1/3) konumlandırılmalı,
kalan alan çevrenin büyüklüğünü göstermeli.

KURAL: Karakter ASLA çerçevenin tam ortasında, tüm alanı
dolduracak şekilde konumlandırılmamalı (istisnası: yüz yüze
karşılaşma anları).
```

---

## 8. 🧪 BİZİM SERİMİZE ÖZEL UYGULAMALAR

### 8.1 Serinin Sinematografik DNA'sı

Araştırmadan çıkarılan ve serimize entegre edilecek prensipler:

```
1. MOTİVASYONLU IŞIK: Her filmde ışık kaynağı belirtilmiş
   (fener, güneş, biolüminesans, gezegen yansıması). ✅ Zaten yapılıyor.

2. DOKU GERÇEKÇİLİĞİ: Cilt gözenekleri, kumaş dokusu, toz parçacıkları.
   ⚠️ AI hâlâ plastik cilt üretiyor (DERS 3, 11). Prompt'lara
   "TEXTURE FIDELITY RULE" eklenecek.

3. ALAN DERİNLİĞİ: Her sahnede f-stop belirtilmiş. ✅ Zaten yapılıyor.

4. YAVAŞ KAMERA = DUYGU: Serimiz meditatif/huşu tonu kullanıyor,
   kamera hızı buna uygun. ✅ Zaten yapılıyor.

5. 1 KLİP = 1 FİKİR: Her sahne tek bir duygusal fikri işliyor.
   ✅ Zaten yapılıyor.

6. RENGİ SICAKLIĞI GEÇİŞİ: Sahne içi renk sıcaklığı kayması
   ile duygusal geçiş. 🆕 YENİ — uygulanacak.

7. PROFESYONEL REFERANSLAR: Prompt'lara sinematograf isimleri
   (Roger Deakins, Rob Hardy) ve film referansları eklenmesi.
   🆕 YENİ — uygulanacak.

8. ANAMORFİK LENS: Kenar yumuşaklığı ve oval bokeh ile
   "sinema filmi" hissi. 🆕 YENİ — test edilecek.
```

### 8.2 Gelecek Film Promptlarına Eklenecek Yeni Blok

Tüm derslerden ve bu araştırmadan çıkarılan, her video promptunun
sonuna eklenecek sinematografik yönerge:

```
=== CINEMATIC QUALITY DIRECTIVES ===

MOTIVATED LIGHTING: Every light source has a visible, logical origin.
Deep shadows, restrained highlights. No flat TV-style lighting.

TEXTURE FIDELITY: Visible skin pores, fabric weave, dust particles,
metal micro-scratches. No artificial smoothing or beautification.

NATURAL LENS: Simulate natural lens falloff and subtle optical
imperfections. No uniform artificial blur. Slight film grain.

COLOR TEMPERATURE: Consistent color temperature throughout the scene
unless an intentional emotional shift is described.

COMPOSITION: Three depth layers (foreground detail, midground character,
background scale). Leading lines directing eye to focal point.
Character positioned in lower or side third, never dead center.

CAMERA WEIGHT: Camera movement has physical inertia — smooth
acceleration and deceleration, not instant starts/stops. The camera
behaves as if operated by a human on a dolly or Steadicam.

REFERENCE: Cinematography quality of Roger Deakins, Emmanuel Lubezki,
or Rob Hardy. This must feel like a real film, not AI-generated content.
===
```

---

# 🎞️ İKİNCİ BÖLÜM — SİNEMA TEKNİĞİNDEN PROMPT DİLİNE

> **Bu bölümün tek kuralı:** Sinema tekniği bilgisi ile PROMPT bilgisi aynı şey
> değildir. Elimizde fiziksel kamera yok; elimizde metinden video üreten bir
> model var. Aşağıdaki her madde üç kutudan birine girer:
>
> ```
> ✅ PROMPTA YAZILIR      modelin eğitim verisinde görsel karşılığı var
> 🎨 POST'TA YAPILIR       promptta istemek zarar verir, kurguda uygulanır
> 📚 SADECE BİLGİ          fiziksel donanım/iş akışı — bu hatta karşılığı yok
> ```
>
> Bir tekniği yanlış kutuya koymak, bu projede en pahalı hata türüdür:
> promptu şişirir, karakter bloğundan yer çalar ve hiçbir şey kazandırmaz.

---

## 9. 🎞️ SENSÖR FORMATI — LARGE FORMAT vs SUPER 35 ✅

Sensör boyutu, aynı odak uzaklığında görüş alanını (FOV) ve alan derinliğini
değiştirir. Modelin eğitim verisinde bu iki estetik ayrışır, dolayısıyla
**format ifadesi prompta yazıldığında görsel karşılığı vardır.**

| | LARGE FORMAT (Full Frame) | SUPER 35 |
|---|---|---|
| Aynı lenste FOV | Daha geniş | Daha dar |
| Alan derinliği | Çok sığ — özne arka plandan sert kopar | Dengeli — çevre okunur kalır |
| Duygusal etki | İzolasyon, sürükleyicilik, "içindeymiş" hissi | Samimiyet, bağlam, klasik sinema |
| Prompt ifadesi | `large-format full-frame field of view` | `Super 35 field of view` |
| Referans | Dune, Oppenheimer | TIFF 2024 yapımlarının çoğu |

```
BU SERİ İÇİN KARAR — SUPER 35 VARSAYILAN:

Sebep 1: Filmlerimizin tamamı ÖLÇEK üzerine kurulu. Karakterin karenin
  1/12'si olduğu, arkasındaki 90 m kraterin okunması gereken bir kadrajda
  aşırı sığ alan derinliği anlatıyı YOK EDER — çevre bilgisi kaybolur.
Sebep 2: "Large Format Yorgunluğu" gerçek bir eleştiri: her şeyin sürekli
  bulanık olduğu kadraj, filmi anlatıdan reklam estetiğine düşürür.
Sebep 3: YOUTUBE SIKIŞTIRMASI. Yayın platformlarının kodlayıcıları geniş
  pürüzsüz bokeh alanlarını verimsiz kodlar; sonuç çamurlu (muddy) arka
  plandır. Bizim dağıtım kanalımız YouTube — bu risk teorik değil.

Large format DİLİ sadece şu iki durumda kullanılır:
  • tek kişilik kapalı mekan / kokpit yakın çekimi (duygusal izolasyon)
  • yüz yüze karşılaşma anı (S32 tipi duygusal zirve)
```

---

## 10. 🔻 ROLLING SHUTTER VE JÖLE ETKİSİ — YENİ NEGATİF ✅

Gerçek CMOS sensörler görüntüyü satır satır okur; kamera hızlı çevrildiğinde
dikey çizgiler eğilir, yapılar esner. Sinemada buna **jello effect** denir.

**Bizim için önemi:** AI video modelleri bu kusuru GERÇEK ÇEKİMLERDEN
öğrenmiştir ve hızlı kamera hareketi tarif edildiğinde taklit eder. Bizim
serimizde kamera zaten yavaş olduğu için risk düşük — ama whip pan, hızlı
lateral track, düşüş/iniş ve titreşim sahnelerinde ortaya çıkar.

```
NEGATİFE EKLENECEK SATIR (sadece hızlı hareket/titreşim içeren sahnelerde):

No rolling shutter skew, no jello effect, no wobbling or leaning
vertical lines during camera movement, no rubbery warping of rigid
structures — the frame is captured as a single stable exposure.
```

> ⚠️ Bunu HER prompta ekleme. Sabit lockoff sahnelerinde yalnızca yer kaplar.
> Kural: kamera hareketi "slow" değilse ekle.

---

## 11. 🔭 LENS KARAKTERİ: KÜRESEL vs ANAMORFİK — ÇATIŞMA UYARISI ✅

| | KÜRESEL (Spherical) | ANAMORFİK |
|---|---|---|
| Bokeh | Dairesel | **Dikey oval** |
| Parlama | Nötr, dairesel | **Yatay mavi/amber çizgi** |
| Kenar | Temiz, düz | **Fıçı bozulması + kenar yumuşaması** |
| Karakter | Temiz, dolaysız, klinik | Resimsel, nostaljik, destansı |
| Referans | Blade Runner 2049 (Master Primes) | Dune (Ultra Panatar) |

### ⚠️ BU SERİDE GERÇEK BİR ÇATIŞMA VAR

```
Anamorfik lensin imzası YATAY PARLAMADIR.
Negatif çekirdeğimiz ise "no lens flare" diyor ve Ders 29 parlama
sözcüklerini (glowing/radiant/shimmering) bloom tetikleyicisi sayıyor.

İkisi aynı promptta bulunamaz. Karar kuralı:

VAKUM FİLMLERİ (Dead Approach, Remembering Dust, Waking Ground)
  → KÜRESEL. Parlama YASAK. Vakumda atmosferik saçılma yoktur;
    yatay parlama fiziksel olarak da yanlış olur.
    Prompt: "spherical lens rendering, circular bokeh, no lens flare"

ATMOSFERLİ / İÇ MEKAN / NEON FİLMLERİ (Low Power, Slow Stone, istasyon)
  → ANAMORFİK SERBEST, ama KONTROLLÜ:
    Prompt: "subtle anamorphic character — vertically oval bokeh, mild
    barrel distortion and edge softness at frame corners. A single thin
    horizontal streak only where a hard light source is directly in
    frame — no halo, no bloom, no glow spill beyond the streak itself."

  ⚠️ "anamorphic lens flare" tek başına yazılırsa model ekranı mavi
     ışık lekeleriyle doldurur ve Ders 29'a düşer. Yukarıdaki gibi
     SINIRLI ve KOŞULLU yaz.
```

Sıkıştırma oranları (1.33x / 1.5x / 2x) **📚 sadece bilgi**: fiziksel çekimde
kareyi sığdırmak için gerekir, bizde çıktı zaten hedef en-boy oranındadır.
Prompta "2x squeeze" yazmak anlamsızdır — "de-squeeze" edecek bir hat yok.

---

## 12. 🎯 ODAK MEKANİĞİ: SOLUMA, RACK FOCUS, DOLLY ZOOM ✅

### 12.1 Odak Soluması (Focus Breathing) — zaten yasak, sebebi buydu

Netlik değiştirilirken lensin görüş alanının hafifçe daralıp genişlemesidir.
Sinema lensleri bunu optik olarak sıfırlar; ucuz lensler yapamaz. Model bunu
öğrenmiştir ve netlik geçişi tarif edildiğinde kadrajı "nefes aldırır".

```
Negatifte zaten var: "no focus breathing". SEBEBİ artık yazılı.
Rack focus içeren her promptta MUTLAKA bulunmalı.
```

### 12.2 Rack Focus / Focus Pull

```
✅ Doğru: "focus pulls from the foreground rim to the distant figure over
2 seconds, the frame size staying exactly constant — no focus breathing,
no zoom, no reframing."
✗ Yanlış: "rack focus" (tek başına — model bunu kesme ile çözebilir)
```

### 12.3 Crash Zoom ve Dolly Zoom (Vertigo / Zolly)

Parfokal lens meselesi bizde **📚 sadece bilgi** (fiziksel zoom yok), ama
etkinin kendisi ✅ prompta yazılır. Dolly zoom modelin en sık YANLIŞ
yorumladığı harekettir: genelde ortada bir kesme uydurur.

```
DOLLY ZOOM — ÇALIŞAN PROMPT KALIBI:

Single continuous optical move, no cuts: the camera physically pulls
back from 3 to 6 meters while the lens simultaneously zooms in at the
same rate. THE SUBJECT'S SIZE AND POSITION IN FRAME STAY EXACTLY
CONSTANT throughout, while the background compresses and rushes toward
her, the walls appearing to close in behind her. No cut, no jump, no
reframing, no change in subject scale at any point.

KULLANIM: Filmde EN FAZLA BİR KEZ. İkinci kullanımda etkisi ölür.
Doğru an: karakterin bilişsel kırılması (Slow Stone S32 tipi bir an,
Remembering Dust'ta S7 "diz ve iki el" anı).
⚠️ Bizim serimizin tonu meditatif; bu hareket agresiftir. Kullanılacaksa
sahnenin geri kalanı tamamen hareketsiz olmalı.
```

---

## 13. 🧠 PSİKOLOJİK AÇILAR VE ÜÇ TUZAK ✅

### 13.1 POV (Bakış Açısı) — ⚠️ VİZÖR KURALIYLA ÇATIŞIR

```
Klasik POV, dünyayı karakterin gözünden gösterir — yani karakter kadrajda
YOKTUR. Ama Ders 5 (VİZÖR KALICILIĞI) her karede yüzün görünmesini şart
koşuyor ve tür kartımızın kilidi bu.

ÇÖZÜM — "VİZÖR İÇİ POV":
Kamera kaskın İÇİNDE konumlanır; kadrajın kenarlarında vizör çerçevesi,
burun köprüsü hizasında hafif bir bulanıklık ve nefes buğusu görünür.
Yüz görünmez ama vizör görünür — kural teknik olarak korunur.

Prompt: "point-of-view shot from inside the helmet: the curved visor
frame edges the top and sides of the image, a faint breath fog pulses at
the lower edge with each exhale, gloved hands entering frame from below."

KURAL: Film başına EN FAZLA BİR POV sahnesi ve asla doruk sahnesinde
değil. ⭐ GEREKÇE DEĞİŞTİ — SAHİBİN KARARI, 04.09.2026:
eski gerekçe "doruk anında yüz gerekir"di ve arkasında hiçbir ders, QA
raporu ya da film skoru yoktu; Aviezer, Trope & Todorov 2012 (Science)
tersini ölçtü — doruk yoğunluğunda pozitif ile negatif durum izole
YÜZDEN ayırt edilemiyor, ayrımı GÖVDE yapıyor. Yasak yerinde duruyor,
gerekçesi şu: POV kameranın karakterin gözüne geçmesidir ve bu serinin
gözlemci lockoff dilini bozar; dahası POV yüzü değil GÖVDEYİ siler —
doruk yuvasında duygu yükü omuz, gövde ve ele yazılır
[KARAKTER_VE_DUYGU §4.3 · kayıt: URETIM_ONCESI_ANALIZ/
04_ARASTIRMA_BULGULARI.md §TUR 11 · T11.5②].
⚠️ Yukarıdaki "vizör içi POV" prompt kalıbındaki NEFES BUĞUSU öğesi
04.09.2026 kararıyla onaylı kanal olmaktan çıktı (T11.5④); kalıp
kullanılacaksa buğu satırı silinir.
```

### 13.2 Kubrick Bakışı — ⚠️ YÜZ KİLİDİYLE ÇATIŞIR

```
Teknik: geniş açı lens + öne eğik baş + kaşların altından doğrudan lense
bakış. Etkisi delilik ve tehdittir.

BU SERİDE RİSKLİ: Geniş açının yüz hatlarında yarattığı optik bozulma,
Ders 16'nın (FACE LOCK: aynı kemik yapısı) tam olarak yasakladığı şeye
benziyor. Model "wide-angle facial distortion" gördüğünde yüzü
deforme etmeyi serbest sayar ve sonraki sahnelerde karakter kayar.

KULLANMA. Yerine: 85mm'de doğrudan lense bakış + sert yan ışık.
Aynı rahatsızlığı yüz kilidini bozmadan verir:
"85mm, she looks directly into the lens, chin slightly lowered, eyes
raised under the brow. No wide-angle distortion, identical bone
structure, no face morphing."
```

### 13.3 Kamera Dönüşü (Roll) — ✅ SERBEST, ama tanımı önemli

```
Roll bir KESME DEĞİLDİR — tek çekim kuralını ihlal etmez. Ama model
"roll" kelimesini açı değişimi sanıp kesme atabilir. Tanımlayarak yaz:

"the camera rotates slowly around its own optical axis, a continuous
2-degree-per-second roll, the horizon tilting steadily — one unbroken
move, no cut, no angle change, no reframing."

KULLANIM: dengesizlik, baş dönmesi, travmatik şok. Bizim serimizde
neredeyse hiç yeri yok — huşu tonu dengesizlik istemez.
İstisna: acil iniş / çarpma sahneleri (Dead Approach S5-S6 tipi).
```

---

## 14. 🖼️ EN-BOY ORANI VE FORMAT SIÇRAMASI 🎨

```
GERÇEK SİNEMADA: sakin sahneler 2.39:1, destansı anlar IMAX 1.43:1 —
siyah bantlar kalkar, kare büyür. Güçlü bir psikolojik araçtır.

BİZDE NASIL YAPILIR:
✗ PROMPTTA İSTEME. "2.39:1 letterbox with black bars" yazarsan model
  bantları görüntünün İÇİNE yakar, kalınlıkları sahneden sahneye değişir
  ve kurguda düzeltilemez.
✅ POST'TA YAP. Üretim 16:9 (shorts 9:16) tam kare. Kurguda:
   • tüm film 2.39:1 isteniyorsa → tek seferde crop
   • "IMAX sıçraması" isteniyorsa → sahne SINIRINDA oranı değiştir
     (klip içinde yapılamaz, kesme yasağı var — ama sahneler arası serbest)

BİZİM FORMATLARIMIZ İÇİN ÖNERİ:
   2-4 dk / 3-5 dk  → düz 16:9. Ölçek zaten kadrajın içinde.
   7-9 dk           → 2.39:1 crop + Overview sahnesinde 16:9'a açılma
                      (48 sahnelik filmde tek bir "nefes" anı)
   dikey shorts     → 9:16 tam kare, crop YOK
```

---

## 15. 🌈 RENK: LOG, ACES VE BU HATTIN GERÇEK SINIRI 📚 + 🎨

```
📚 GERÇEK SİNEMADA: sensör doğrusal (linear) okur, veri logaritmik (LogC4,
REDCODE) kodlanır, ACES gibi cihazdan bağımsız bir renk uzayında birleşir,
16-bit OpenEXR olarak arşivlenir, sonunda ODT ile BT.709 (SDR) veya
ST-2084/PQ (HDR) hedefine çevrilir.

⛔ BİZDE BUNLARIN HİÇBİRİ YOK VE OLAMAZ.
Veo çıktısı: pişmiş (baked) Rec.709, 8-bit, sıkıştırılmış mp4.
Log yok, RAW yok, 17 stop yok, ACES hattı yok.

→ Prompta "LogC4", "ACES", "ARRIRAW", "REVEAL color science", "17 stops
  of dynamic range" yazmak HİÇBİR ŞEY yapmaz. Sadece karakter yer.
  Bu ifadeler bu kılavuzda BİLGİ olarak duruyor, prompt malzemesi değil.

✅ PROMPTA GİREN TEK RENK BİLGİSİ — HIGHLIGHT ROLL-OFF:
Filmin parlak uçtaki davranışı (organik sönümlenme) ile dijitalin
davranışı (sert kırpılma) farklıdır. Bu FARK prompta yazılabilir ve
bizim bloom savaşımızın doğru dili budur:

"Highlights roll off smoothly and retain texture instead of clipping to
flat white — the brightest surfaces keep visible detail. No blown
whites, no bloom, no glow bleeding past object edges."

🎨 POST'TA YAPILANLAR (promptta değil):
  • sahneler arası renk birliği (48 klipte tek grade — ZORUNLU,
    yoksa her sahne başka filmden gibi durur)
  • film greni ekleme (üretimde "35mm film grain" zaten isteniyor,
    post'ta hafif bir kat daha tutarlılık sağlar)
  • halation (parlak kenarlarda ince kırmızımsı taşma) — filmin imzası,
    model bunu güvenilir üretmiyor, post'ta eklenir
  • YouTube teslimi: SDR / BT.709. HDR denemesi yapma — kaynak 8-bit.
```

> **Hibrit "film-out" süreci** (dijital çekim → 35mm ara filme lazer basım →
> yeniden tarama; Dune, The Batman) bu hattın erişemeyeceği bir işlemdir.
> Ama amacı bizim de amacımızdır: dijitalin fazla temiz, klinik yüzeyini
> kırmak. Bizim karşılığımız = gren + doku direktifleri + kusur bırakmak.

---

## 16. 📚 KURAMSAL ZEMİN: PLAN-SEKANS VE ÜÇ PERDE

### 16.1 Plan-sekans — bizim "kesme yok" kuralımızın kuramsal adı

```
Bela Tarr, Tarkovski, Iñárritu ve Türk sinemasından Derviş Zaim (Nokta —
hat sanatındaki kesintisiz çizgi "ihcam" ilkesi) ile Onur Ünlü (Sen
Aydınlatırsın Geceyi — 2-13 dakikalık planlar) aynı şeyi yapar: kesmeyi
reddederek zamanın bütünlüğünü korur. İzleyici bilinçaltında bir kesme
bekler, gelmez ve sahnenin gerilimine hapsolur.

BİZİM İÇİN ANLAMI: "Ders 1 — kesme yok" kuralımız bir teknik zorunluluk
olarak doğdu (model kesme attığında klip çöpe gidiyor). Ama estetik
olarak da savunulabilir bir gelenek içindeyiz: her sahnemiz bir
plan-sekanstır ve ritim sadece kamera hareketiyle kurulur.
→ Bunu kanal açıklamalarında ve paketlemede KULLAN: "her sahne tek
  kesintisiz çekim" bir kısıt değil, bir imza olarak sunulmalı.
```

### 16.2 Üç perde ve çekim ölçeği eşlemesi — ⚠️ kısmi kullanım

```
Kuram: Kurulum → genel çekim + derin odak (mekanı öğret)
       Çatışma → omuz üstü, alt/üst açı, daralan ölçek
       Çözülüm → çok yakın çekim, sığ odak, yoğunluk

⚠️ UZAY_SENARYO_KILAVUZU §7 üç perdeyi bu format için FAZLA KABA buluyor
ve sekans zinciri (Gravity modeli) öneriyor. İkisi çelişmez:
  • HİKAYE yapısı için → sekans zinciri (her sahne kendi mini kriziyle)
  • ÇEKİM ÖLÇEĞİ ilerlemesi için → üç perde eşlemesi geçerli

ÖLÇEK YAYI KURALI (her formatta uygulanır):
  Filmin başı  → geniş, derin odak, karakter küçük
  Ortası       → orta ölçek, karakter-çevre dengesi
  Doruk        → yakın/çok yakın, sığ odak
  Overview     → ÇOK GENİŞ (yayı bilinçli kırar — bu yüzden etkilidir)
  Final        → geniş, held frame

Not: Overview sahnesinin gücünün bir kısmı, doruğun yakın çekiminden
sonra aniden geniş açıya dönmesinden gelir. Ölçek yayı olmadan
Overview sadece bir manzara olur.
```

---

## 17. ✅ ÖZET KARAR TABLOSU — HANGİSİ NEREYE

| Teknik / kavram | Kutu | Not |
|---|---|---|
| Super 35 / large format FOV dili | ✅ prompt | Varsayılan Super 35 (§9) |
| Lens odak uzaklığı + f-stop + mesafe | ✅ prompt | Zaten yapılıyor |
| Küresel lens / dairesel bokeh | ✅ prompt | Vakum filmlerinde zorunlu |
| Anamorfik oval bokeh + fıçı bozulması | ✅ prompt | Sadece atmosferli filmlerde, kontrollü |
| Yatay anamorfik parlama | ⚠️ koşullu | Vakumda YASAK, atmosferde sınırlı (§11) |
| Rolling shutter / jello negatifi | ✅ prompt | Sadece hızlı hareket sahnelerinde |
| Focus breathing negatifi | ✅ prompt | Netlik geçişi olan her sahnede |
| Dolly zoom (Vertigo) | ✅ prompt | Film başına en fazla 1, kalıbıyla (§12.3) |
| Kamera roll | ✅ prompt | Tanımlayarak; kesme sanılmasın |
| Vizör içi POV | ✅ prompt | Film başına en fazla 1, doruk dışında |
| Kubrick bakışı (geniş açı) | ⛔ kullanma | Ders 16 yüz kilidini bozar (§13.2) |
| Highlight roll-off dili | ✅ prompt | Bloom savaşının doğru dili (§15) |
| Film greni | ✅ prompt + 🎨 post | İkisi birlikte |
| En-boy oranı / letterbox | 🎨 post | Promptta istenirse yakılır (§14) |
| Halation | 🎨 post | Model güvenilir üretmiyor |
| Sahneler arası renk birliği | 🎨 post | 48 klipte ZORUNLU |
| Kamera gövdesi markası (ARRI/RED) | 📚 bilgi | Prompta yazmanın ölçülmüş faydası yok |
| Log/RAW/ACES/IMF/Dolby Vision | 📚 bilgi | Bu hatta karşılığı yok (§15) |
| Cooke /i, LDS, XD meta verisi | 📚 bilgi | Fiziksel çekim + VFX hattı içindir |
| Steadicam / TRINITY / gimbal | 📚 bilgi | "camera weight" dili yeterli (§8.2) |
| Global shutter donanımı | 📚 bilgi | Etkisi negatifle istenir, donanımla değil |
| Parfokal/varifokal ayrımı | 📚 bilgi | Zoom etkisi tarif edilir, mekanizma değil |

---

## 📊 MEVCUT KILAVUZLARLA İLİŞKİ

| Bu Kılavuz | İlişkili Dosya | Nasıl Kullanılır |
|---|---|---|
| Işıklandırma Psikolojisi | Her filmin Lighting Bible'ı | Işık türü seçerken referans |
| Kamera Hareketleri | Her filmin Camera Bible'ı | Hareket seçerken anlatısal işlev |
| Doku Gerçekçiliği | LESSONS_LEARNED Ders 3, 11 | Plastik cilt sorununa karşı |
| Tematik Çerçeveler | Her filmin World Bible'ı | Sahne atmosferi kurarken |
| Profesyonel Referanslar | Sahne promptları | Stil kodu olarak prompt'a ekleme |
| Sinematografik Direktifler | Universal Quality Directives | Her video promptunun sonuna |
| §9 Sensör formatı | Her filmin Camera Bible'ı | Super 35 varsayılan; sapma gerekçelendirilir |
| §10 Rolling shutter negatifi | LESSONS_LEARNED (aday Ders 43) | Hızlı hareket içeren sahnelerin negatifine |
| §11 Anamorfik çatışması | KILAVUZ_REHBERI §3 ortam kartları | Ortam vakum mu atmosfer mi — parlama kararı buna bağlı |
| §12 Odak mekaniği | Her filmin Camera Bible'ı | Rack focus / dolly zoom kalıpları |
| §13 Psikolojik açılar | KILAVUZ_REHBERI §4.1 (vizör kilidi) | POV ve Kubrick bakışı kilitlerle çatışır |
| §14 En-boy oranı | Post-prodüksiyon | Promptta İSTENMEZ |
| §15 Renk hattının sınırı | GOOGLE_FLOW / post akışı | Log/ACES yazma; highlight roll-off yaz |
| §16 Plan-sekans kuramı | UZAY_SENARYO_KILAVUZU §7 | Sekans zinciri ile birlikte okunur |
| §17 Karar tablosu | Prompt yazımı | Şüphede kalınca buraya bak |

---

## 🆕 SÜRÜM NOTU

```
v2 — İkinci bölüm (§9-§17) eklendi: sensör formatı, rolling shutter,
lens karakteri, odak mekaniği, psikolojik açılar, en-boy oranı, renk
hattının sınırı, plan-sekans kuramı ve karar tablosu.

Bu bölümün ayırt edici katkısı, tekniklerin ✅ prompt / 🎨 post / 📚 bilgi
olarak üçe ayrılmasıdır. Kaynak metindeki donanım ve renk iş akışı
bilgisinin (ARRI/RED gövdeleri, ACES, IMF, Cooke /i, Steadicam) bu
üretim hattında karşılığı YOKTUR ve prompta yazılmaz — bilgi olarak
korunmuştur, çünkü aynı soru tekrar sorulacaktır.

ÜÇ YENİ ÇATIŞMA TESPİT EDİLDİ VE KARARA BAĞLANDI:
  1. Anamorfik yatay parlama  ×  Ders 29 anti-bloom  → ortama göre (§11)
  2. Klasik POV               ×  Ders 5 vizör kalıcılığı → vizör içi POV (§13.1)
  3. Kubrick bakışı geniş açı ×  Ders 16 yüz kilidi → kullanma (§13.2)
```
