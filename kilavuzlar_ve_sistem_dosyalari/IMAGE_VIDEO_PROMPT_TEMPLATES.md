# 🎬 EVRENSEL PROMPT ŞABLONLARI — Image & Video

> Bu şablonlar, mevcut film dosyalarının analiz edilmesiyle çıkarılmıştır.
> İki nesil format tespit edildi: **V1 (düz format)** ve **V2 (Bible yapılı format)**.
> Aşağıdaki şablonlar **V2'nin en güncel ve en başarılı versiyonunu** temel alır.
> ⭐ 14.09.2026: yeni açılan klasörler (00_HIKAYE_ONAYI.md var) **V3** iskeletini
> kullanır — bir sonraki bölüm; V2 eski klasörler için durur.

---

## 📊 ANALİZ BULGULARI

### Tespit Edilen Ortak Yapı (20 Film)

| Özellik                 | V1 (Eski: Burning World, White Silence, Breathing Storm) | V2 (Yeni: Tidal Hunt, Last Archive, Inversion, Resonance Field vb.)                         |
| ----------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Bible sistemi**       | ❌ Tek blok dünya/karakter açıklaması                    | ✅ Ayrı Bible'lar (World, Character, Ship, Camera, Lighting, Motion, Physics, Negative)     |
| **Lesson entegrasyonu** | ❌ Yok                                                   | ✅ LESSON referansları prompt'lara gömülü                                                   |
| **Image prompt yapısı** | Tek paragraf, serbest akış                               | Etiketli bölümler: SCENE / ENVIRONMENT / SUBJECT / CAMERA / LIGHTING / PHYSICS / NEGATIVE   |
| **Video prompt yapısı** | Saniye bazlı, serbest akış                               | `MOTION (Xs, lens, distance):` + saniye bazlı kırılım + `[PHYSICS + NEGATIVE bibles apply]` |
| **Lens kilidi**         | Bazılarında var                                          | ✅ Her sahne için tek lens (32mm / 75mm / 100mm macro)                                      |
| **Mesafe kilidi**       | Nadiren                                                  | ✅ Her prompt'ta metre cinsinden kamera mesafesi                                            |
| **Klip süresi**         | 7-10 saniye değişken                                     | ✅ Sabit 10 saniye (hook'lar hariç 7-9s)                                                    |
| **Negatif Bible**       | Kısa, genel                                              | ✅ Kapsamlı, Lesson bazlı, filme özel eklentiler                                            |
| **Sahne sayısı**        | 10 + Hook + 2 viral ara                                  | 10 + Hook + 2-4 viral ara sahne                                                             |

### Tüm Filmlerde Sabit Kurallar

- **Tek çekim** — sahne içinde kesme yok
- **Tek karakter** — her filmde bir kâşif
- **Fotogerçekçi** — CGI/video oyunu estetiği yasak
- **Ölçek referansı** — her karede insan-çevre oranı
- **Eller boş** — elde taşınan alet yok (bilek ekranı)
- **Vizör şeffaf** — yüz her zaman görünür
- **Metin yok** — ekranda yazı/harf/rakam yok

---

## ⭐ 14.09.2026 · YENİ REJİM İSKELETİ — IN FRAME · bütçe · START FRAME (V3)

> **Sahip kararı (reform FAZ 7 · `TODO_AKIS_VE_DERS_REFORMU.md`).** Yalnız
> `00_ANALIZ/00_HIKAYE_ONAYI.md` taşıyan (14.09.2026'dan sonra açılan) klasörlerde;
> eski klasörler aşağıdaki V2 şablonuyla kalır. Ölçüm: THE_LOCKED_PULSE IMAGE promptu
> ort. 719 kelime, %57'si her promptta aynen tekrar; 10/10 insert promptu kadrajda
> olmayan yüzü tarif ediyordu ve model yazılanı kadraja soktu [D214]. Kapılar
> `prompt_kontrol.py` ① (kelime bandı) · ㉖ (IN FRAME) · ㉗ (NEGATIVE ≤ 11 cümle);
> sayılar betikte (`KELIME_BANDI` · `NEGATIF_CUMLE_TAVANI`), buraya kopyadır.
>
> Üç kural: **① ilk satır `IN FRAME:`** — kadrajda ne var, sözlükten (face · hands ·
> torso · legs · full body · back · none); yalnız yazılan tarif edilir, Bible'ın kalanı
> YAZILMAZ (self-contained ≠ Bible'ın tamamı — AGENTS §2 kural ③). `face` yalnız yüz
> OKUNABİLİR kadrajda (MS ve yakını) yazılır; `full body`/WS'de yüz ayrıntısı girmez.
> **② bütçe** — POZİTİF gövde (NEGATIVE öncesi) IMAGE 100-250 · VIDEO 120-300 kelime,
> üstü BLOCK; NEGATIVE = `KILAVUZ_REHBERI` §5.1 çekirdek (image 7 · video 8 cümle) +
> ≤3 sahneye özel (§5.2). **③ video Bible'ı tekrar etmez** — I2V'de imaj t=0'dır,
> tek satır `START FRAME:` devamlılığı taşır; `CONTINUITY LOCKS` paragrafı yazılmaz.
> Sahnenin tutması gereken TEK kilit ÜÇÜNCÜ satırdadır (TUR 11 ② KONUM — ilk kez şablona indi).

### 📸 IMAGE (V3)

```
IN FRAME: <face · hands · torso · legs · full body · back | none — kadrajda olan, sözlükten>
Scene <n> of <N>.
<SAHNENİN TEK KİLİDİ — bu karede tutması gereken şey, SAYIYLA. Örn.:
 The left glove stays open, all five fingers spread, resting on the valve wheel.>

<ÖZNE — yalnız IN FRAME'dekiler: hands → eldiven · bilek halkası · kol;
 face → yüz + kask + [D79 vizör cümlesi, §5.2]; back → [D139 sırt cümlesi, §5.2];
 full body → kostümün silüeti ve renk bandı, yüz ayrıntısı YOK.
 Character Bible'ın kalanı yazılmaz — model yazılanı kadraja sokar [D214].>
<MEKÂN · IŞIK · ÖLÇEK — bu karede görünen kadarı; ölçü nesne-göreli [D138]>
<CAMERA: lens + mesafe + yükseklik + açı tipi sözlük kelimesiyle
 ("low angle" / "eye level" / "high angle" / "over-the-shoulder")>

NEGATIVE: <§5.1 çekirdek — IMAGE'de 7 cümle (① tek çekim düşer)>
<+ ≤3 sahneye özel cümle — §5.2 (diyalog · risk kartı kilidi); yoksa boş>

Output: <oran>, <çözünürlük>, no text, no watermark.
```

### 🎥 VIDEO (V3)

```
IN FRAME: <face · hands · torso · legs · full body · back | none>
Scene <n> of <N>. Duration <klip> seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
<SAHNENİN TEK KİLİDİ — hareket kilidi, SAYIYLA. Örn.:
 The wheel turns exactly one quarter, then stops, and nothing else in frame moves.
 ⚠️ 15.09.2026: "then stops … nothing else moves" SAHNE_DOLULUGU §4 ⑥ ile çelişir —
 kilit fiili SÜREÇ (§1 · §4 ①); örneğin değişimi ⬜ sahip kararı (22_ aday 3)>

<TIMELINE: 0,0 s … / <t> s … — her satırda ≥1 GÖVDE FİİLİ; iki aşamalı eylem iki
 satıra; replik varsa ofseti buradan okunur ve konuşan/dinleyen bedeni §5.2 diyalog satırı ·
 ⭐ 15.09.2026: ≤3 satır (evre ① yük altında · ② direnç · ③ SÜRDÜRME) —
 SAHNE_DOLULUGU §2 · §4.1 önce/sonra>
<CAMERA: ⛔ I2V'de bu satır ŞART — betik kurulum yayını buradan ölçer; lens · mesafe ·
 hareket tipi (fixed lockoff / push-in …) · IN FRAME: back ya da kamera arkadaysa
 pozitif sırt cümlesi burada [D139]>

NEGATIVE: <§5.1 çekirdek — 8 cümle>
<+ ≤3 sahneye özel cümle — §5.2>

Output: <oran>, no text, no watermark.
```

> Ölçülen kalıp: §5.1 çekirdek 886 karakter / 139 kelime; bütçe POZİTİF gövdeye
> uygulandığı için çekirdek sahne metninden yer yemez. Toplam karakter tavanı
> (4.300, `TAVAN`) aynen durur.

### 📝 V3 doldurulmuş örnek — THE_LOCKED_PULSE S0'ın yeniden yazımı (14.09.2026 doğrulaması)

> Aynı sahne, aynı kurulum (24mm · WS · 6,0 m). Eski IMAGE 4.382 karakter (tavan
> üstü, BLOCK) ve 24mm geniş planda **yüz tarifi** (kaş kemeri · çene · gözenek);
> V3 hâli 2.392 karakter / 247 kelime pozitif gövde, `IN FRAME: full body` — yüz
> yok, silüet + renk bandı var. VIDEO 3.845 → 2.477 karakter; `CONTINUITY LOCKS`
> paragrafı tek satır `START FRAME:` oldu. `prompt_kontrol.py` yeni rejimde bu
> çift için 0 bulgu (①/㉖/㉗/㉑). Üçüncü satır = sahnenin tek kilidi (sayıyla).
> Sahneye özel 2 negatif cümle: mühür üç sınırı [D175] + pencere/yıldız yok.

```
IN FRAME: full body
Scene 1 of 25.
The hand-wheel stays at its starting position for the whole frame, both gloves closed on its rim.

A single suited figure kneels side-on to the camera in the right third of a curved ring-habitat corridor, facing the wall, torso upright. Muted slate-grey quilted pressure suit, one amber band on the LEFT upper arm and one on the LEFT thigh, rounded hard-shell helmet in a wide bronze collar ring, dark-grey gloves. In the right-hand wall at chest height a recessed valve bay: a brushed-steel hand-wheel the width of a helmet, a round port collar at hip height, above them a row of seven fist-sized lamps, six lit white, the last on the right dark, and one red lamp above the bay. A stiff webbing strap hangs from a ceiling rail on the left, nearer the camera, almost to the deck, one straight line caught at the left end of a swing, filling the left third of the frame. Dark grey ribbed deck rising into the distance like the inside of a great wheel, pale grey matte wall panels, one arched ceiling panel overhead.

CAMERA: 24mm spherical lens on a fixed locked-off tripod 6.0 m from the valve bay, camera height 1.20 m, eye-level wide shot, deep focus. LIGHT: even neutral light from the ceiling panel, slightly from screen-left, short soft shadows; the red lamp pulses once every two seconds, reaching only the bay face and his right shoulder, no halo.

NEGATIVE: Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere in frame — none above the collar, none at the wrist, none at the ankle. No window, no sky, no stars inside the corridor.

Output: 16:9, 4K, no text, no watermark.
```

```
IN FRAME: full body
Scene 1 of 25. Duration 9 seconds.
START FRAME: the approved still from this scene's IMAGE prompt — animate it; suit, helmet, light and scene carried from the frame, nothing re-described.
The hand-wheel does not move for the whole clip; the strap on the left completes one full swing every four seconds.

TIMELINE: 0.0s — he kneels at the bay, both gloves closed on the rim of the hand-wheel, the strap at the left end of its swing. 2.0s — the strap has swung across to the right end and is on its way back; his torso leans into the wheel. 4.0s — the strap completes one full swing and keeps swinging at that same rate. 7.0s — his shoulders settle back a finger's width, then lean into the wheel again. 9.0s — hold: both gloves on the rim, the strap mid-swing, the red lamp pulsing; the wheel has not moved.

CAMERA: 24mm spherical lens on a fixed locked-off tripod 6.0 m from the valve bay, camera height 1.20 m, eye-level wide shot, deep focus, fixed lockoff — absolutely zero camera movement.

PHYSICS: spin gravity inside the ring — down is the deck and the corridor curves up into the distance; about a quarter of Earth's weight; real time, normal human pace; anything let go falls to the deck; the strap swings as one straight line and never ripples. AUDIO: a steady low fan-and-pump hum; the alarm warble once every two seconds; his breathing inside the helmet; no music.

NEGATIVE: Single unbroken take, no cuts, no dissolves, no camera resets, no angle change. Exactly one human character, no duplicates, no second person. 0% bloom, no glow, no soft focus, every surface keeps visible texture. No readable text, letters, digits or symbols on any display, surface, patch or sign — none on the suit, the equipment, the ground or any natural surface in the frame — no subtitles, no captions, no watermark. Photorealistic with 35mm film grain, no CGI or video-game look, real skin pores and sweat, no airbrushing, no waxy texture, no face morphing. Equipment and clothing identical throughout, no drift, no gear appearing or disappearing. Hand-to-surface contact keeps a clear boundary, no merging, no phasing, no extra fingers. Particles obey the stated gravity with continuous momentum, never hovering, never swirling like liquid, terrain static, no melting or warping. No bare skin anywhere in frame — none above the collar, none at the wrist, none at the ankle. No window, no sky, no stars inside the corridor.

Output: 16:9, no text, no watermark.
```

---

## 📸 IMAGE PROMPT ŞABLONU (V2 — eski rejim · 14.09.2026'dan önce açılan klasörler)

```
SCENE:
[Sahnenin tek cümlelik özeti — ne oluyor, kim nerede?]

ENVIRONMENT:
[WORLD BIBLE] [Gezegenin bu sahnedeki spesifik durumu — hangi faz/saat/katman?
Atmosfer, zemin, gökyüzü detayları. Sahnede görünür olması gereken çevresel
elementler: canlılar, su, kaya formasyonları, hava olayları vb.]

SUBJECT:
[CHARACTER BIBLE] [Karakterin bu sahnedeki pozu, eylemi, duygusal durumu.
Kıyafet detayları Bible'dan tekrarlanmalı. Vizör, bilek ekranı, tether/halat
gibi ekipman durumu. Canlı varsa: boyut, tür, hareket tipi belirtilmeli.
GIANT-CREATURE SCALE RULE uygulanmalı.]

CAMERA:
[Lens]mm, f/[X], ISO [X], camera fixed at approximately [X] meters,
[açı: low angle / eye level / high angle / three-quarter].
Physically accurate perspective[, correct engineering proportions,
realistic scale relationships — gemi/dev canlı varsa bu eklenir].

SPATIAL LOCK:
[Sahnede sabit hedef (gemi/kapı/yapı) ve ona doğru hareket varsa
ZORUNLU — UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md §4.
Hedefin ekran dilimi + yönelimi, karakterin hareket ve bakış yönü
EKRAN-uzayında (screen-left/right, camera-left/right), ölçek kesri
(frame height oranı), yön taşıyıcıları (rüzgâr/duman yönü), eksen
cümlesi. Dünya-uzayı kelimeleri (north, çapasız "toward") YASAK.]

LIGHTING:
[LIGHTING BIBLE — Faz Adı] [O fazın spesifik ışık kaynakları, gölge yönü,
renk sıcaklığı. Biolüminesan varsa: ANTI-BLOOM DIRECTIVE uygulanır —
sharp, directional, clear falloff.]

PHYSICS:
[PHYSICS BIBLE — İlgili kurallar] [Yerçekimi değeri, ölçek oranları,
fizik kurallarının bu sahnedeki spesifik uygulaması.
Su varsa: DYNAMIC WATER RULE.
Canlı varsa: CREATURE LOCOMOTION.
Temas varsa: CONTACT INTEGRITY.
Çarpışma varsa: COLLISION INTEGRITY.]

NEGATIVE:
[NEGATIVE BIBLE — full list applies; emphasis: bu sahneye özel riskler]
```

> ## 🚨 UYARI — BU ŞABLONUN BİÇİMİ EKRANA SIZABİLİYOR (DERS 45)
>
> **Kanıt:** The Inversion, `2:12–2:21` — kadrajda *"teknik lens grafikleri"*
> ve **"Dr. Kaya Uçan..."** isim etiketi çıktı. Film, metni **dört ayrı yerde**
> ve büyük harfle yasaklamıştı; yasak tutmadı. Sızan şey sahneye ait değil,
> **bu şablonun kendi biçimine** ait:
>
> ```
> ŞABLONDAKİ BİÇİM                     EKRANDA ÇIKAN
> [CHARACTER BIBLE] Kaya crouches…  →  isim etiketi / alt yazı şeridi
> CAMERA: 75mm, f/5.6, ISO 400      →  HUD gibi lens verisi grafiği
> ```
>
> ### Ne yapılacak
>
> ```
> 1. KARAKTERİN ADINI PROMPT GÖVDESİNE YAZMA
>    ❌ Dr. Kaya Uçan stands alone on the plain
>    ✅ A woman in her late thirties stands alone on the plain
>    Ad görsel bilgi taşımıyor; etiket olarak çizilebiliyor.
>    Kimlik Character Bible'da durur, prompt'a fiziksel tarif girer.
>
> 2. KAMERA SATIRINI CÜMLEYE ÇEVİRMEYİ DENE (riskli sahnelerde)
>    ❌ CAMERA: 75mm, f/5.6, ISO 400, camera fixed at approximately 10 meters
>    ✅ Shot on a 75mm lens from a fixed position ten meters away, f/5.6,
>       shallow depth of field, physically accurate perspective.
>    "Sayı+harf+bölü" dizilimi ekranda lens verisi olarak okunabilecek
>    tek biçim.
>    ⚠️ **04.09.2026:** bu örnek KARAKTER çekimi içindir. Kadrajın öznesi
>    BÜYÜK BİR YAPI ise (istasyon · üs · gemi) sığ alan derinliği ölçeği
>    kırar ve yapıyı maket okutur — orada derin netlik zorunludur:
>    `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` §5.4.
>    ⛔ Ve nesne ÖLÇÜSÜ prompt gövdesine yazılmaz [Ders 138]; kamera
>    MESAFESİ yazılır (muaf).
>
> 3. NEGATIVE bloğuna ekle (ikinci savunma hattı):
>    HUD overlay, lens data, focal length text, camera metadata, name label,
>    character name caption, subtitle, lower third, annotation
> ```
>
> ⚖️ **Kapsam dürüstlüğü:** bu bir filmde, bir zaman kodunda gözlendi.
> `[WORLD BIBLE]` / `[CHARACTER BIBLE]` etiket düzeni film dosyalarının çoğunda
> kullanılıyor ve Bible tutarlılığını sağlıyor — **toptan sökülmemeli.**
> Önce 1. ve 3. maddeyi uygula (bedelsiz), 2. maddeyi metin çıkan sahnelerde
> dene. Etiket düzeninin tamamen kaldırılması ayrı bir test gerektirir.
>
> 🔗 `LESSONS_LEARNED.md` → DERS 45 · kaynak:
> `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_INVERSION.md`

### 📸 Kullanım Notları

- **ENVIRONMENT** içinde `[WORLD BIBLE]` etiketi kullanarak Bible referansı verin
- **SUBJECT** içinde `[CHARACTER BIBLE]` etiketi kullanarak kıyafet/ekipman detaylarını tekrarlayın
- ⚠️ **Karakterin ADINI prompt gövdesine yazmayın** — fiziksel tarif kullanın (Ders 45)
- **Gemi sahnelerinde** SHOT-SPLIT RULE'u unutmayın: geminin tamamı + okunabilir yüz = AYRI sahneler
- **Lens seçimi**:
  - `32mm Cooke anamorphic` → geniş, establishing, gemi, ölçek
  - `75mm` → medium, karakter, aksiyon, duygu
  - `100mm macro` → extreme detay, su damlası, doku, yazı
- **Her prompt'ta metre cinsinden kamera mesafesi ZORUNLU**
- **SPATIAL LOCK** yalnız coğrafyalı sahnelerde doldurulur (sabit hedef +
  hareket); statik tek-mekân sahnesinde satır atlanır. Ayrıntı ve dolu
  örnek: `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` §4

---

## 🎥 VIDEO PROMPT ŞABLONU (V2 — eski rejim · 14.09.2026'dan önce açılan klasörler)

```
MOTION ([X] seconds, [lens]mm, [hareket tipi] at [X] meters):
0s — [Başlangıç durumu — image prompt'un devamı, sahne bu görüntüyle AÇILIR]
[X]s — [İlk aksiyon/değişim anı]
[X]s — [İkinci beat — kamera hareketi başlarsa burada belirtilir]
[X]s — [Üçüncü beat — doruk an veya reveal]
[X]s — [Kapanış durumu]. No cuts.
[PHYSICS + NEGATIVE bibles apply throughout]
```

### 🎥 Kullanım Notları

- **Süre**: Standart sahneler = **10 saniye**. Hook = **7-9 saniye**
- **Hareket tipleri** (tek seçim, asla karıştırma):
  - `fixed lockoff` — sabit kamera
  - `push-in` — yaklaşma
  - `pull-back` — uzaklaşma
  - `slow orbit` — karakter etrafında yavaş dönüş
  - `tilt-up` / `tilt-down` — dikey kaydırma
  - `slow lateral track` — yatay takip (koşma/kaçış sahneleri)
  - `slow crane-rise` — yukarı yükselme (reveal sahneleri)
  - `slow vertical track` — dikey takip (yüzme/tırmanma)
- **Saniye kırılımı**: 3-5 beat, eşit aralıklı, her beat'te BİR aksiyon
- **"No cuts."** cümlesi her video prompt'un SON satırında ZORUNLU
- **Coğrafyalı sahnede her beat'e ekran yönü yazılır** ("crosses the
  midground left-to-right") ve blok sonuna tek satır eksen hatırlatması
  eklenir ("Ship remains in the right third throughout; no direction
  reversal.") — `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` §4.4
- **`[PHYSICS + NEGATIVE bibles apply throughout]`** her video prompt'un en son satırında ZORUNLU (eski rejim; V3'te atıf yok — çekirdek promptun kendisinde, §5.1)
- **Video, image'in DEVAMI olmalı** — aynı kompozisyon, aynı ışık, aynı poz

---

## 🛡️ KALİTE DİREKTİFLERİ — TEK KAYNAK ADRESİ

> ⛔ **Burada eskiden duran "v4 UNIVERSAL QUALITY DIRECTIVES" bloğu
> 21.08.2026'da kaldırıldı.** Üç sebep:
> 1. Blok, ders tabanının yalnız ilk 19 dersinden derlenmişti (21.08.2026 tespiti) ve
>    `DERSLER/00_HIZLI_REFERANS.md`'deki güncel havuzla ayrışmıştı —
>    iki blok, iki ayrı doğru.
> 2. Her maddesi `[LESSON n]` etiketi taşıyordu — aşağıdaki Ders 45
>    uyarısının bizzat yasakladığı biçim.
> 3. "Her video promptunun sonuna eklenmeli" talimatı uzunluk bandıyla
>    (`KILAVUZ_REHBERI.md` §7) aritmetik olarak çelişiyordu.
>
> **Güncel kullanım:**
> - Tür-bağımsız çekirdek (her prompta giren kısa blok):
>   `KILAVUZ_REHBERI.md` **§5.1 ÇEKİRDEK — 8 cümle** (14.09.2026; eski
>   klasörde §5.3 tam metin). Film-özel tam liste PLAN Negative Bible'da.
> - Sahneye göre seçilecek kilit havuzu (suit/su/canlı/sıfır-g vb.):
>   `DERSLER/00_HIZLI_REFERANS.md` — havuzdur, tamamı yapıştırılmaz.
>
> 🚨 **Ders 45 uyarısı (geçerli):** `[CHARACTER BIBLE]` gibi köşeli
> parantezli etiketler prompt GÖVDESİNDE durursa model onları ekrana
> çizebiliyor. The Inversion'da tam olarak bu oldu. Etiketleri gövdeden
> çıkar; kilit maddelerini etiketsiz düz cümle olarak yaz.

---

## 📝 ÖRNEK: BOŞ BİR SAHNE NASIL DOLDURULUR

### 📸 IMAGE PROMPT — Doldurulmuş Örnek

> ⛔ **Bu örnek Ders 45'i UYGULAR, anlatmaz.** Karakterin özel adı hiçbir
> blokta geçmiyor — SCENE'de "A lone suited figure", SUBJECT ve MOTION'da
> "The figure". Adı örneğe yazarsan yeni film onu kopyalar ve ad ekrana
> etiket olarak düşer (THE INVERSION 2:12 · dört ayrı yerde).
> Kimlik ADLA değil FİZİKSEL TARİFLE taşınır: kostüm · rozet · yaka rengi.

```
SCENE:
A lone suited figure crouches before a small hexagonal crystal spike
that has just formed from the sand, studying its geometry.

ENVIRONMENT:
[WORLD BIBLE] The central sand plain of Sforza, scattered Ancient
Spires visible in the far background. The sand is fine, pale grey,
completely still. The violet-gold sky casts even, warm light.

SUBJECT:
[CHARACTER BIBLE] The figure crouches an arm's length from a crystal
spike no taller than her forearm, her head tilted, studying its facets.
Her throat-collar resonator plate is inactive (no glow). Her wrist
display shows a slow amber pulse. Hands empty.

CAMERA:
75mm, f/4, ISO 400, camera fixed at approximately 5 meters,
eye-level. Physically accurate perspective.

LIGHTING:
[LIGHTING BIBLE — Baseline] Harsh, even violet-gold sky light
raking across the sand and crystal surfaces, throwing micro-relief
into sharp shadow. No bloom on the crystal.

PHYSICS:
[PHYSICS BIBLE] 0.92g. The crystal spike's facets are geometrically
precise, matching its acoustic trigger (a single short handclap).
Sand grains at its base are visibly compressed where the
piezoelectric fusion occurred.

NEGATIVE:
[NEGATIVE BIBLE — full list applies; emphasis: no bloom on crystal,
no random geometry, crystal must read as acoustically precise]
```

### 🎥 VIDEO PROMPT — Doldurulmuş Örnek

```
MOTION (10 seconds, 75mm, slow push-in from 5 to 3 meters):
0s — The figure crouches motionless, studying the 0.3m spike, her
breath fogging faintly at the visor seal.
3s — She extends one hand toward the spike, fingers hovering above
its surface without touching, tracing its hexagonal edges in the air.
5s — Slow push-in begins, the crystal's facets catching the violet-
gold light with sharper, more defined prismatic refraction.
8s — She tilts her head, lips moving silently as if counting the
spike's facets.
10s — She glances at her wrist display, then back at the spike. No
cuts.
[PHYSICS + NEGATIVE bibles apply throughout]
```

---

## 🔄 SAHNE TİPLERİNE GÖRE HIZLI REFERANS

| Sahne Tipi                 | Lens                        | Mesafe      | Hareket                           | Süre  |
| -------------------------- | --------------------------- | ----------- | --------------------------------- | ----- |
| **Hook (ölçek şoku)**      | 32mm veya 75mm→32mm         | Yakın→uzak  | Slow pull-back + crane-rise       | 7-9s  |
| **Gemi inişi (geniş)**     | 32mm Cooke anamorphic       | 80-260m     | Fixed lockoff veya slow tilt-down | 10s   |
| **Gemi penceresi (yakın)** | 75mm                        | 8-15m       | Slow push-in                      | 8-10s |
| **İlk adım**               | 75mm                        | 5-10m       | Slow orbit veya fixed             | 10s   |
| **Koşma/kaçış**            | 75mm                        | 8-12m       | Slow lateral track                | 10s   |
| **Canlı karşılaşma**       | 32mm (büyük) / 75mm (küçük) | 15-50m      | Fixed veya slow orbit             | 10s   |
| **Macro detay (su, doku)** | 100mm macro                 | 1-3m        | Fixed veya slow tilt              | 10s   |
| **Viral ara sahne**        | Duruma göre                 | Duruma göre | Genellikle tilt veya pull-back    | 9-10s |
| **Panorama/ölçek**         | 32mm Cooke anamorphic       | 50-100m+    | Slow orbit veya pan               | 10s   |
| **Kapanış/veda**           | 32mm → pull-back            | 10m→100m+   | Slow pull-back                    | 10s   |

---

## ⚠️ SIKÇA YAPILAN HATALAR VE ÇÖZÜMLER

| Hata                            | Kalite Tablosundaki Skor    | Çözüm                                           |
| ------------------------------- | --------------------------- | ----------------------------------------------- |
| AI sahne içinde kesme yapıyor   | Canopy 2/10, Deep Root 3/10 | `CONTINUITY LOCK` + her sahne AYRI üretim       |
| Canlılar shape-shift yapıyor    | Canopy 4/10                 | `CREATURE ANATOMY LOCK` + arka plan shallow DOF |
| Bloom/glow her şeyi yıkıyor     | Canopy 6/10, Deep Root 6/10 | `ANTI-BLOOM DIRECTIVE` + "sharp directional"    |
| Karakter yüzeyde kayıyor        | Canopy 5/10                 | `WEIGHT & CONTACT RULE` + ayak tepkisi          |
| Eller yüzeye eriyor             | Deep Root 4/10              | `CONTACT INTEGRITY RULE`                        |
| Su donmuş/jel gibi              | Slow Tide 5/10              | `DYNAMIC WATER RULE`                            |
| Nesneler birbirinden geçiyor    | Tidal Hunt 2/10             | `COLLISION INTEGRITY RULE`                      |
| Canlılar kayarak hareket ediyor | Tidal Hunt 2/10             | `CREATURE LOCOMOTION RULE`                      |
| Vizör kayboluyor                | Canopy 7/10                 | `VISOR PERSISTENCE RULE`                        |
| Bilek ekranında garble metin    | Slow Tide                   | `NO AI TEXT RULE` — abstract pulse only         |
