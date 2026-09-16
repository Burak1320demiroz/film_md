# 📚 DERSLER — Ekipman ve Varlık Sürekliliği

> `LESSONS_LEARNED.md` 07.08.2026'da tematik dosyalara bölündü; bu dosya
> **Ekipman ve Varlık Sürekliliği** derslerini taşır. Numaralar depo genelindeki atıflar yüzünden
> DEĞİŞTİRİLMEZ ve dosyalar arasında kesintisiz DEĞİLDİR — tam dizin:
> [`../LESSONS_LEARNED.md`](../LESSONS_LEARNED.md) · yeni ders ekleme: `AGENTS.md` kart G.

---

## 🟡 DERS 5: VİZÖR KAYBOLMASI — KASK CAM TUTARSIZLIĞI

**Kaynak:** The Canopy World QA — Karakter: 7/10
**Sorun:** Karakter başını çevirdiğinde kask vizörü kayboluyor veya beliriyor. Vizör cam yüzeyi tutarsız.

**ÇÖZÜM — CHARACTER BIBLE'a eklenecek:**
```
VISOR PERSISTENCE RULE: The transparent visor/helmet glass must remain ALWAYS
VISIBLE in every frame, regardless of head angle or lighting conditions. The
visor must show consistent reflections, condensation, or environmental
interaction (water beading, fog, dust) appropriate to the current layer. The
visor must NEVER disappear, become invisible, or merge with the face — it is
always a distinct, visible glass surface between the camera and the face.
```

---

## 🟢 DERS 8: KIYAFETTEĞİŞİMİ — SAHNE ARASI TUTARSIZLIK

**Kaynak:** The Canopy World QA — Karakter: 7/10
**Sorun:** Kesmelerden sonra sırt çantası/yaşam destek sistemi tasarımı değişiyor.

**ÇÖZÜM — Her sahnede CHARACTER BIBLE'ın TAMAMI tekrarlanmalı:**
```
SUIT CONTINUITY RULE: The character's suit, equipment, and all accessories must
match the CHARACTER BIBLE description EXACTLY in every single scene. No design
changes, no color shifts, no added or removed equipment between scenes. The
backpack, harness, rope reel, wrist display, visor, gloves, and boots must be
IDENTICAL across all shots.

IMPLEMENTATION: Copy the full CHARACTER BIBLE suit description into EVERY scene
prompt — do not use shorthand like "[CHARACTER BIBLE]" for suit details in
scenes where continuity has previously failed.
```

---

## 🟡 DERS 32: GEMİ/YAPI ÖLÇEK TUTARLILIĞI — ORANLAR DEĞİŞİYOR

**Kaynak:** The Ring Walker QA — Ölçek: 4/10
- `1:44 — Lander staircase angle and door proportions alter relative to 0:01 setup.`

**Sorun:** Gemi (lander/ship) veya büyük yapıların oranları farklı sahnelerde değişiyor. Merdiven açıları, kapı boyutları, pencere oranları ilk kuruluşa göre farklılaşıyor. Bu, karakterin gemiye göre boyut değişmesi sorunuyla (Ders 4'ün ölçek kısmı) ilişkili ama farklı: burada GEMİNİN KENDİ İÇ ORANLARI değişiyor.

**ÇÖZÜM — Gemi/yapı içeren her sahnenin SHIP BIBLE veya ENVIRONMENT bölümüne eklenecek:**
```
VEHICLE/STRUCTURE SCALE LOCK: The ship, lander, or any significant
structure must maintain IDENTICAL INTERNAL PROPORTIONS across all scenes:

- Door height must remain the SAME ratio to the character's height in
  every frame the door appears (e.g., door = 1.3x character height).
- Staircase/ramp angle must remain CONSTANT between wide and close shots.
- Window proportions (width:height ratio) must not change.
- Landing leg geometry (angle, pad size, strut thickness) must remain
  identical in every visible frame.
- Hull panel proportions and accent stripe widths must not shift.
- The ship's LONGEST DIMENSION relative to the character must remain
  CONSTANT in all establishing shots where both are visible. SPEC side:
  "hull 12,0 m · figure 1,67 m · 1:7,2". Prompt side: "the hull's long
  axis reads about seven body-lengths of the figure standing beside it".

IMPLEMENTATION: proportions live in the SPEC lock list and the plan's
geometry ledger, NEVER in the prompt body. The image prompt carries the
SAME ratios as OBJECT-RELATIVE units: "the hatch opening is a little
wider than her shoulders", "the ramp rises at a shallow angle, about two
body-lengths of run for every half body-length of rise". The ratio is
what must be COPIED IDENTICALLY into every scene prompt that shows the
ship — not the metre value.

NEGATIVE ADDITION: No door/window proportion shifts. No staircase angle
changes. No hull scaling between scenes. No landing leg geometry changes.
```

> 🔄 **REVİZYON — 04.09.2026 (TUR 9 denetimi).** Bu dersin
> IMPLEMENTATION satırı **Ders 138 ile doğrudan çarpışıyordu:** metreli
> ölçüyü image prompt gövdesine yazdırıyordu, D138 ise ölçünün gövdeye
> inince modelin onu nesnenin ÜSTÜNE bastığını ölçtü (THE THIN ROOF S2 ·
> 22,41 s · halkanın iç yayında `11 metres` + gradasyon çentikleri).
> Daha kötüsü, `prompt_kontrol.py`'nin yüzey-işareti sözlüğünde
> door/hatch/ramp/hull/panel/truss yoktu ve "height/…m" muafiyete
> giriyordu — bu dersin ihlali kapıdan **0 BLOCK ile geçiyordu.**
> ⭐ Ders geçersiz değil, DİLİ değişti: **oran korunur, birimi değişir.**
> Metre SPEC'te ve fizik defterinde kalır; prompt aynı oranı gövde boyu
> cinsinden taşır. Ayrıntılı biçim ve dönüşüm tablosu:
> `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` §1.

---

## 🔴 DERS 37: EKİPMAN DURUM GEÇİŞİ — KASK ANİDEN BELİRİYOR

**Kaynak:** The Dead Approach Compilation QA (Genel 3/10) — Karakter: 3/10 — `0:19 — Suit design drifts, helmet appears instantly`
**Sorun:** Ders 8 (kıyafet devamlılığı) kıyafetin DETAYLARININ sahneler arası korunmasını kapsıyordu. Bu ise farklı bir hata: ekipmanın **AÇIK/KAPALI DURUMU** bir kesme olmadan değişiyor — kask sahne ortasında birdenbire kafada beliriyor, harness kendiliğinden geri geliyor, eldiven ortaya çıkıyor. Model, ekipmanı bir "durum" değil bir "dekor" olarak işliyor.

**Neden oluyor:** Prompt ekipmanı tarif ediyor ama DURUMUNU sahneye kilitlemiyor. "Kask entegre" yazıyor ama "bu sahnede kask TAKILI ve tüm çekim boyunca TAKILI KALIYOR" yazmıyor. Model boşluğu kendi doldurmaya çalışıyor.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **Her sahne promptunda ekipman durumu açıkça beyan edilir** — sadece varlığı değil, durumu:
```
HELMET STATE: worn and sealed for the entire take — it is already on at
0s and never removed, and no helmet appears, materializes or is put on
during the shot.
HARNESS STATE: removed before this scene — it stays off her body for the
entire take and does not reappear.
```
2. **Bible'a "EKİPMAN DURUM TABLOSU" eklenir** — hangi sahnede hangi parça takılı:
```
| Sahne | Kask | Harness | Eldiven | Toz kirlenmesi |
|-------|------|---------|---------|----------------|
| S1-S6 | Takılı | Takılı | Takılı | Temiz |
| S7    | Takılı | Çıkarılıyor | Takılı | Temiz |
| S8+   | Takılı | YOK | Takılı | Kirli |
```
3. Negatif bloğa: `no equipment appearing or disappearing, no helmet materializing, no gear state change mid-shot`

---

## 🟡 DERS 38: HASAR ABARTMA — MODEL "HASARLI"YI "PARÇALANMIŞ" OKUYOR

**Kaynak:** The Dead Approach Compilation QA (Genel 3/10) — Parçacık: 4/10 — `0:00 — Debris excessive, structural disintegration instead of localized damage`
**Sorun:** Prompt spesifik ve sınırlı bir hasar tarif ediyordu (kanat ucu kopuk, sensör direği bükülmüş). Model bunu genel bir "hasarlı gemi" sinyali olarak alıp gövdeyi parçalara ayırdı, etrafa sürekli enkaz saçtı ve yapısal bütünlüğü bozdu. Sonuç: gemi ölçek kilidi de çöktü (Ders 32 ile zincirleme hata).

**Neden oluyor:** "Damaged", "wrecked", "torn", "shattered" gibi kelimeler eğitim verisinde felaket görüntüleriyle güçlü ilişkilidir. Tek bir güçlü hasar kelimesi, spesifik tarifi ezip geçiyor.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. **Hasarı SAY ve SINIRLA.** Genel sıfat yerine sayılabilir liste:
```
❌ "a heavily damaged ship with torn hull"
✅ "the hull is intact and structurally whole except for exactly three
   points of damage: the left wing tip is missing at 70% of its length,
   the forward sensor mast is bent 45 degrees, and the bow beacon array
   is a clean torn stump. All other surfaces are undamaged."
```
2. **Sağlam olanı da açıkça söyle.** Model neyin BOZULMAYACAĞINI bilmiyorsa hepsini bozabilir.
3. **Enkaz miktarını sınırla:**
```
no continuous debris shedding, no structural disintegration, no
fragmenting hull, no expanding debris field — the ship is damaged but
whole and holds its exact 34-meter silhouette
```
4. Negatif bloğa: `excessive debris, structural disintegration, fragmenting hull, wreckage cloud`

---

## 🟡 DERS 42: KİR VE TOZ DESENİ SÜRÜKLENMESİ — YIPRANMA HER KAREDE YENİDEN ÜRETİLİYOR

**KAPI:** LİSTE · SPEC C `YIPRANMA` (sabit bölge + başlangıç sahnesi) · ölçen mercek: ② DEVAMLILIK `WEAR TIMELINE` — satır 15.09.2026'da eklendi (kontrat §5)
**TEKRAR:** 1 · 15.09.2026 MARS_SON_CIKIS (mod V · ② B1 — SPEC C `S14 yangın isi (S15-S36 boyu)` İLAN ETTİ; 2:05 isli giysi → 2:22 Mars yüzeyinde temiz 🟠 · 2:52 göğüste önceki sahnede olmayan kan lekesi 🟡)

**Kaynak:** Low Power QA (Genel 4/10) — Karakter: 6/10 — `0:08 — Dust accumulation patterns on shoulders and chest shift completely between frames`
**Sorun:** Ders 8 kıyafetin *tasarımını* (renk, şerit, amblem) kilitliyordu. Ama kıyafetin üzerindeki **kir, toz, leke ve yıpranma deseni** ayrı bir kategori: model bunları tasarım değil doku gürültüsü sayıyor ve her karede yeniden üretiyor. Sonuç: omuzdaki toz birikimi kare kare yer değiştiriyor, suit "titriyor".

**Neden önemli:** Kirlenme bu seride bir **anlatı aracıdır** — Low Power'da tozun artması zamanın geçtiğini, The Waking Ground'da kirlenme fazın ilerlediğini gösterir. Deseni oynayan bir suit, bu anlatımı yok eder.

**ÇÖZÜM — PROMPT GÜNCELLEMELERİ:**
1. Kirlenmeyi **konumlandır** — "tozlu" demek yetmiyor, nerede olduğunu söyle:
```
❌ "dirty suit with heavy dust accumulation"
✅ "rust-red dust staining concentrated on the knees, the glove palms and
   the lower right chest panel; the shoulders and back stay comparatively
   clean. This exact staining pattern is fixed and identical in every
   frame — it does not shift, redistribute, regenerate or animate."
```
2. Negatif bloğa: `shifting dirt patterns, regenerating dust texture, animated grime, wear pattern drift`
3. Bible'a **KİRLENME HARİTASI** eklenir — hangi fazda hangi bölge ne kadar kirli.

---

## 🚨 UYARI — 5 VE 37 NUMARALI DERSLER İKİ FİLMDE DE YAZILIYDI, İKİSİNDE DE TUTMADI

> Bu bir ders değil, **dersler hakkında bir ölçüm.** Numarası yoktur ve
> ders sayısına dahil edilmez.


Her iki filmin Bible'ında, ders numarasına atıfla, şu satır var:

```
VISOR PERSISTENCE RULE [LESSON 5]: Visor ALWAYS VISIBLE in every frame
```

Sonuç:

| Film | Kural yazılı mı | Ekranda |
|---|:---:|---|
| The Inversion | ✅ satır 135, 408 | 0:16 çıplak baş · 1:06 vizör yok · 2:32 kask çıkıyor |
| The Kaleida Crash | ✅ satır 180, 459 | 0:22 çıplak baş · 1:02 çıplak baş — 4 kez salınıyor |

**Ders yazıldı, prompta girdi, uygulandı — ve iki filmde de tutmadı.**

Bu, projedeki en önemli ölçümü doğruluyor: *"Sayısal kilit çalışıyor, tarif
kilidi çalışmıyor."* "ALWAYS VISIBLE" bir tarif kilididir. The Slow Stone'da
tutan kilit ise sayıydı: *"kask S21'de bir kez"*.

**Yapılacak:** Ders 5 ve 37 tarif biçiminden **takvim biçimine** çevrilmeli:

```
❌ Visor ALWAYS VISIBLE in every frame
✅ HELMET STATE SCHEDULE — 13 scenes, sealed in all 13.
   The helmet is never removed, never opened, and appears in exactly
   0 scenes as open. Any frame without the visor is a generation error.
```

---

## 🔴 DERS 57: TEK ÇEKİM İÇİNDE EKİPMAN MORPHU — 7. SANİYEDE TÜP BELİRİYOR

**Kaynak:** The Deep Pressure MANTIK QA — 🔴 BLOCKER `00:00 vs 00:07` —
`Character starts with a full clear bubble helmet and no tank. Seven seconds
later in the SAME CONTINUOUS ACTION, she has a scuba face mask, a regulator
in her mouth, and a ribbed tank on her back.`

**Sorun:** Bugüne kadar ölçülen bütün kostüm hataları **iki klip arasında**
doğuyordu (Ders 8, 37; Kaleida/Inversion kask salınımı). Bu ilk kez **tek
kesintisiz çekimin içinde** oluyor — kamera kesmiyor, karakter yüzmeye devam
ediyor ve yaşam destek sistemi kare kare değişiyor.

Sebep: prompt kıyafeti yalnız **0. saniyede** tarif ediyor. 0s'de kurulan
görsel, 10s boyunca modelin serbest yorumuna bırakılıyor; model boşluğu
kendi klişesiyle dolduruyor. Zaman çizelgesi (`At 2s / At 5s / At 7s`) hep
KAMERA ve AKSİYON yazıyor, **hiç KIYAFET yazmıyor.**

**ÇÖZÜM — kıyafet, sahne tarifine değil zaman çizelgesine yazılır:**

```
EQUIPMENT FRAME LOCK: The suit and life-support configuration visible in
frame 1 is IDENTICAL in frame 300. Nothing is added, nothing is removed,
nothing changes shape at any point in this 10-second take.
Specifically at 0s, 3s, 6s and 10s she wears exactly:
[SUIT IDENTITY LOCK bloğu — birebir aynı cümle]
No tank appears. No mask appears. No regulator appears. No visor opens,
closes, tints or clears. If any piece of equipment differs between the
first and last frame, the generation is an ERROR.
```

Video prompt'unun zaman satırlarına da kısa hatırlatma girer:

```
At 5s: the camera pans right — her suit, helmet and equipment unchanged.
At 9s: she glides alongside the drifters — same suit, same helmet, no tank.
```

**KURGUDA UCUZ ÇÖZÜM:** morph başladığı yerden klibi kes. Bu filmde S1'in
son 2 saniyesini atmak 4 BLOCKER'dan birini bedelsiz siliyor —
rapor "Low cost" olarak işaretledi.

> 🔗 Ders 37 sahneler ARASI ekipman durumunu kilitler; 57 tek çekimin
> İÇİNİ kilitler. İkisi birlikte yazılmazsa aradaki boşluktan bu hata geçer.

---

## 🟡 DERS 58: TEKRAR EDEN VARLIK KİMLİK KİLİDİ — AYNI YER İKİ FARKLI YER

**Kaynak:** The Deep Pressure MANTIK QA — Coğrafya **4/10** — LOCATION MAP'in
3 satırının 2'si `Consistent? No`:

```
Portal   S4 amber/mor + astronot giysisi   ·  S8 mavi/camgöbeği + dalgıç kıyafeti
Dev göz  S11 yeşil göz, gri buruşuk deri   ·  S14 neon mavi göz, yıldızlı doku
Denizaltı S2 ↔ S13                          ·  ✅ TEK TUTAN — çünkü tek tasarımı vardı
```

**Sorun:** Filmin iki kez dönülen üç varlığından ikisi ikinci gelişte başka
bir şeye dönüşmüş. Kıyafet için Bible tutuluyor (en azından tutulması
gerektiği biliniyor); **lokasyon ve dev nesneler için hiç Bible tutulmuyor.**
Tekrar eden portal, tekrar eden yaratık, tekrar eden yapı — hepsi ikinci
sahnede sıfırdan tarif ediliyor ve tarif değişiyor.

Aynı bölümdeki iki prop da tek kullanımlık kaldı: mavi lazer alet (00:40)
bir kez kesip kayboldu, yerine 01:40'ta sarı ışıklı el feneri geldi.

**ÇÖZÜM — Bible'a ikinci bir bölüm: TEKRAR EDEN VARLIKLAR**

```
RECURRING ENTITY BIBLE — karakterden sonra, sahne haritasından önce.
Filmde birden fazla sahnede görünen HER lokasyon, yapı, yaratık ve alet
için bir kart:

| Varlık   | Sahneler | Sabit tanım (sayısal) |
|----------|----------|------------------------|
| Sınır    | S4, S8   | dikey, altın-sol / mor-sağ, 2m kırılma bandı — RENK ASLA DEĞİŞMEZ |
| Dev göz  | S11, S14 | 40m çapında, sarı-yeşil iris, gri buruşuk deri, tek göz |
| Denizaltı| S2, S13  | küresel, 3m, bakır çerçeve, tek ön pencere |
| Tarayıcı | S5, S11  | ince bakır gövde, dar altın ışık konisi — TEK ALET |

KURAL 1: Kart varsa, o varlığın geçtiği her sahne prompt'una kartın
         TAMAMI kopyalanır — kıyafet gibi (Ders 8/55).
KURAL 2: Bir alet iki sahneden azında görünüyorsa ya silinir ya ikinci
         sahnesi yazılır. Tek kullanımlık prop üretilmez.
KURAL 3: İkinci gelişte "aynı yer" demek yetmez; ilk sahnenin renk,
         ölçü ve doku değerleri sayıyla tekrarlanır.
```

**NEDEN 🟡:** İzleyici kıyafet değişimini saniyede fark eder, portalın rengini
90 saniye arayla fark etmez. Ama bu iki bulgu filmin **iki dönüş noktasında**
duruyor — tekrar, kurgunun tek yapısal iddiası. Denizaltı tuttuğu için
Kurulum skoru 7/10 çıktı; kart sistemi olsaydı üçü de tutardı.

> 🔗 Ders 32 (gemi ölçek tutarlılığı) bunun tek varlıklı halidir; 58 onu
> filmdeki BÜTÜN tekrar eden varlıklara genişletir ve sayısal kilit ister —
> projedeki tek kanıtlanmış çalışan kilit türü.

---

## 🟡 DERS 79: BIBLE'DAKİ OLUMSUZ KOSTÜM KİLİDİ NEGATİF ÇEKİRDEĞE GİRMEDİKÇE TUTMUYOR — SIRT ÜNİTESİ VE AYNALI VİZÖR İKİ FİLMDE ÜST ÜSTE GERİ GELDİ

**Kaynak:** THE STARLESS CIRCLE · KARAKTER_QA 6.0/10 — pasaport:
`life-support backpack` + `visor state fluctuates between clear and
opaque/reflective` (Ekipman 4/10, yüz 14 sahnenin yalnız 3'ünde okunuyor).
**Tekrar:** THE UNBROKEN CITY · KARAKTER_QA 8.0/10 — `rear backpack life
support`. İki filmin Character Bible'ı da aynı cümleyi taşıyordu:
*"No back-mounted tank, no hose, no cable."* Starless Circle ayrıca
*"one fully transparent seamless visor, no tint, no coating… her whole
face clearly readable through it"* diyordu.

**Sorun:** Bu iki yasak **yalnız Character Bible'da** duruyor; 36 promptta
tekrarlanan NEGATİF ÇEKİRDEK'te yok. Çekirdeğe giren yasaklar (klon, metin,
bloom, sıvı, ateş) tuttu; bible'da kalanlar tutmadı. Mekanizma basit ve
ölçülmüş: **model prompt gövdesindeki tarifi çiziyor, referans belgeyi
okumuyor** — ve "astronot" ön-yargısı sırt ünitesi + aynalı vizör getiriyor.
Vizörün bedeli ayrıca dramatik: bu filmin bütün okuma-karar zinciri (Ders
45 · yetkinlik kuralı) yüzden okunacaktı.

**ÇÖZÜM — negatif çekirdeğe iki cümle, POZİTİF tarifle:**

```
Add to NEGATIVE CORE (verbatim, in every prompt of any film whose suit
bible forbids them):

"The suit has NO back-mounted unit: no backpack, no tank, no hose, no
cable, no rear housing of any kind — her back silhouette is flat.
The visor is optically clear glass with zero tint, zero mirror coating
and zero reflection of the environment; her face is fully readable
through it in every frame, at every head angle."

⚠️ Neden pozitif cümle: "no tinted visor" cümlesi aynalı vizörü çağırıyor
   (Ders 59). Çekirdeğe hem yasak hem POZİTİF durum yazılır: "flat back
   silhouette" ve "face fully readable" ölçülebilir; "no coating" değil.
```

> 🔗 Ders 5 (vizör kalıcılığı) · Ders 8 (suit devamlılığı) · Ders 55
> (bible yoksa üretim bozulur) ile aynı hat. Yeni olan şu: **bible VAR,
> dolu ve doğru — ama prompt gövdesine girmeyen satırı model görmüyor.**
> Kontrol: yeni film yazarken bible'daki her "No …" cümlesi için sor —
> bu cümle 36 promptun 36'sında var mı? Yoksa ya çekirdeğe girer ya
> bible'dan silinir; ikisinin arası, iki filmde iki kez, üretim hatası
> oldu.
>
> 🔁 **3. vaka (07.08.2026 · THE BLIND RETURN):** karakter pasaportu yine
> `Backpack` + `dual headlamps` yazdı; bible yine "No back-mounted tank,
> no hose, no cable" + "a single integrated helmet lamp" diyordu ve sabit
> yıpranma izleri (çene yanık izi dahil) yine üretilmedi. Film bu dersle
> AYNI GÜN yazılmıştı ve D79 cümlesi negatif çekirdeğine girmemişti —
> D77'nin mekanizması bir kez daha: ders plana geri akmıyor.

---

## 🔴 DERS 84: SAHNELER ARASI DURUM METİNLE KİLİTLENMİYOR — ÜÇ ÇAPA DA YAZILIYDI, ÜÇÜ DE KIRILDI

**Kaynak:** THE THIRD DUNE QA (11.08.2026) — 🧍 KARAKTER Yıpranma 3/10 ·
Kostüm 5/10 · 🧩 MANTIK Kostüm-Prop · `2:29 kumlu → 2:40 tertemiz` ·
`1:30 mor bant → 2:10 bant yok` · iki suitte de sırt çantası

**Sorun:** Bu depoda ilk kez, bulguların kökü **eksik cümle değil.**
Önceki vakalarda yanıt hep "cümle promptta yoktu" çıkıyordu (Starless
Circle vizör · Blind Return sırt ünitesi · Dawn Front kostüm). Third
Dune'da üç çapa da yazılıydı ve üçü de kurguda kırıldı:

```
KİLİT                          NEREDE YAZILI            EKRANDA
sırt ünitesi yasağı            42/42 promptun negatifi   iki suitte de çanta
bant rengi (mor / buz mavisi)  çift blok, 42 prompt      2:10'da mor yok
toz seviyesi (2→3→4 takvim)    her sahneye tek tek       2:40'ta sıfırlandı
  + 3 cm temiz referans şeridi  42/42 promptta
```

Mekanizma: **her klip önceki klibi görmeden üretiliyor.** "Seviye 4"
yazan bir cümle modele bir önceki karede ne yaptığını söylemez; sahne
İÇİNDEKİ durumu kilitler, sahneler ARASINDAKİ durumu kilitlemez. Toz,
yıpranma, bant, sırt silueti — hepsi sahneler arası niceliklerdir.
Bu yüzden sayısal kilit (Ders 44'ün kanıtlanmış aracı) burada çalışmaz:
sayı doğru, taşıyıcı yok.

**ÇÖZÜM — prompt cümlesi DEĞİL, üretim zinciri kararı:**

```
① DURUM DEĞİŞEN SAHNELERİ I2V ÜRET
   Toz/yıpranma seviyesinin değiştiği ilk sahne text-to-video üretilir;
   o klibin SON KARESİ bir sonraki sahnenin start frame'i olur. Metin
   yalnız hareketi tarif eder. (7-9 dk formatının zaten yaptığı şey —
   3-5 dk formatı bunu yalnız durum kırılma noktalarında kullanır,
   25 sahnenin hepsinde değil: ~4 zincir noktası yeter.)

② AYNI SEVİYEYİ BLOK HÂLİNDE ÜRET
   Seviye 2'nin beş sahnesi arka arkaya, seviye 3'ün dokuzu arka arkaya,
   seviye 4'ün yedisi arka arkaya üretilir. Aynı oturumda üretilen
   klipler arasında sapma ölçülebilir biçimde daha az.

③ KABUL ET VE ONARIMI BÜTÇELE
   Kırılan klip sayısı azdır (bu filmde 3). Yeniden üretim maliyeti,
   25 promptu yeniden yazma maliyetinden düşük. Onarım listesi film
   kaydına yazılır, prompt dosyası DEĞİŞTİRİLMEZ — cümle zaten doğru.
```

⛔ **Bu derse "prompta şunu ekle" çözümü yazma.** Üç kilidin üçü de
zaten prompttaydı; dördüncü bir cümle eklemek ölçülmüş bir başarısızlığı
dördüncü kez denemektir [AGENTS §8].

---

## 🔴 DERS 89: SAHNENİN EYLEMİ BİR ÇIKARMA İSE, MODEL EN YAKIN ÇIKARILABİLİRİ ÇIKARIR

**Kaynak:** THE SECOND SHIP · Faz 7 / BEDEL 1. koşusu (S69, 1:23) —
fazın BLOCKER'ı · `.../FAZ_07_BEDEL/FAZ_07_QA_DERSLER.md` D-AK
**Sorun:** ilk vaka, ama sınıfı F6 D-AD'nin (kemeri yasakla, kapı kasası
gelir) insan-ekipman kardeşi — negasyon klişeyi komşuya kaydırıyor

Sahnenin olayı bir çıkarma feinti: adam eldiven halkasını çeviriyor,
kadın bileğini tutup durduruyor, **eldiven çıkmıyor.** Prompt bunu
açıkça yazıyordu: "The glove NEVER comes off: no bare hand, no bare
skin, no exposed wrist." Ekranda eldiven gerçekten çıkmadı — **kadın
kaskını çıkardı.** Solunamaz atmosfer kilidi, faz blocker'ı ve bir
sonraki fazın ateşlemesi tek karede harcandı.

Kök neden grep'le görülüyor:

```
grep -n "helmet stays ON and sealed" FAZ_07_BEDEL.md
→ yalnız S61 ve S64 (kaskın çıkması akla bile gelmeyen iki sahne)
→ S69'da YOK — çıkarma eyleminin geçtiği TEK sahnede yok.
```

Mekanizma: jest iptal edilmiyor, **hedef değiştiriyor.** Modele
"burada bir şey çıkıyor" bilgisi verildiğinde, yasaklanan parçayı
bırakıp mühür ailesinin bir sonraki üyesine geçiyor
(eldiven → kask → yaka halkası).

**ÇÖZÜM — TEK MÜHÜR SAYIMI (sayısal, tarif değil):**

```
Çıkarma / açma / sökme geçen HER sahnede, dokunulan mühür SAYILIR ve
geri kalan bütün mühürler tek tek kapalı ilan edilir:

EXACTLY ONE SEAL IS TOUCHED IN THIS SHOT AND IT IS THE RING AT HIS
RIGHT WRIST. Every other seal stays closed in every frame - both
helmets ON and locked at the collar, both collar rings closed, both
gloves on both hands. No bare head, face, neck, hand, wrist or skin
appears at any second; no helmet is lifted, opened or removed.

⭐ Kural lisanslı çıkarma sahnelerinde de aynıdır — orada sayı yine
   BİRDİR, sadece açılan mühür değişir:
   "EXACTLY ONE SEAL OPENS IN THIS SHOT AND IT IS THE RIGHT WRIST
   RING: no helmet, collar ring or second glove is touched."
```

⛔ **Kilidi "riskli görünen" sahneye değil, EYLEMİN GEÇTİĞİ sahneye
yaz.** Bu depoda kilit tam tersi dağılmıştı ve bedeli bir blocker oldu.

---

## 🔴 DERS 95: "OPTİK BERRAK, RENKSİZ, YANSIMASIZ VİZÖR" EKRANDA "KASK YOK" OKUNUYOR — MÜHÜRLÜ DURUM KENDİ KANITINI SİLDİ

**Kaynak:** THE RING LIGHT · 12.08.2026 · 🧍 KARAKTER_QA pasaportu + 🔧 VIDEO_QA
baseline'ı — iki bağımsız mercek aynı yanlışı okudu
**Sorun:** D79'un POZİTİF hâlinin ters etkisi; D88 ("sınırlı izin tam izindir")
ile aynı aileden. **2 vaka:** 2.si THE FROST LINE (31.08.2026) — C kilidi yine
"optik berrak, renksiz, YANSIMASIZ" yazdı; ② vizör hâlini "unreadable/erratic"
okudu, master karelerinde cam yalnız S21'de (t204, çerçeve + spekülar) okunuyor

Ders 79 aynalı vizörü yasaklattı, çünkü yüz okunmuyordu. Ring Light bunu en uç
biçimde uyguladı (§0.12):

```
Vizör: tek parça, optik berrak, RENKSİZ, kaplamasız, yansımasız —
yüz her kafa açısında tam okunur.
KASK TAKVİMİ: S0-S13 kask TAKILI, vizör KAPALI ve MÜHÜRLÜ, durum değişimi 0.
```

Ekranda ortaya çıkan şey: **vizörün var olduğunu gösteren tek bir işaret yok.**
Renk yok, yansıma yok, çerçeve tarif edilmemiş, kenar parlaması yasaklanmış.
İki mercek de aynı sonuca vardı:

```
🧍 "Equipment: Helmet (visor retracted/open)" · "unhelmeted faces at 2:00"
🧍 FLAGS: "Does the script specify the crew retracting their visors?"
🔧 "Equipment: Helmets with opaque/reflective visors (0:10),
    visors up/removed (2:00)"
```

Mekanizma önemli: bu bir üretim hatası olmayabilir. **Görünmez kılınan bir
kilit, doğru üretilse bile doğrulanamaz.** QA vizörü göremiyorsa izleyici de
göremez; "14/14 mühürlü" bilgisi ekranda hiçbir yerde yoktur ve filmin vakum
gerilimi (dışarısı öldürür) o mühürden beslenir.

⚠️ İkinci etki: rapor "kask çıktı" okuduğu için Ekipman kategorisine 8/10
verdi ve gerçek soru (mühür sabit mi) hiç ölçülmedi.

**ÇÖZÜM — mühürlü durumun ÜÇ GÖRÜNÜR İŞARETİ, her insanlı prompta sayısal:**

```
The visor is a single curved pane held in a 2 cm brushed-metal frame; the
frame's lower seal ring is visible where it meets the collar in every frame.
One thin unbroken specular line runs along the visor's upper edge in every
frame — the only reflection the visor carries. The face is fully readable
THROUGH the pane at every head angle.

NEGATIVE: no bare skin above the collar, no open helmet, no lifted or
retracted visor, no removed pane, no mirror coating, no colored tint, no
environment reflected in the visor.
```

```
ÜÇ İŞARET, TEK CÜMLEYLE ÖZETİ:
  ① ÇERÇEVE  2 cm metal — vizörün SINIRI görünür
  ② MÜHÜR    yaka halkası — vizörün KAPALI olduğu görünür
  ③ TEK ÇİZGİ üst kenarda ince parlama — camın VAR olduğu görünür
Üçü de "yansımasız berrak vizör" kuralını bozmaz: yüz hâlâ tam okunur.
```

⛔ **Genel kural:** bir durum kilidi ("mühürlü", "kapalı", "dolu", "bağlı")
ekranda **ayırt edici bir işaret** taşımıyorsa, o kilit ölçülemez. Kilidi
yazarken sor: *bu durumun tersi ekranda nasıl görünürdü?* İki durum aynı
görünüyorsa kilit değil, temennidir.

---

## 🔴 DERS 139: DÜZ SIRT KİLİDİ YALNIZ SIRT GÖRÜNMEZKEN TUTUYOR — KAMERA ARKAYA GEÇEN TEK SAHNEDE SIRT ÇANTASI DOĞDU (6/6 → 5/6)

**KAPI:** BETİK · `prompt_kontrol.py` ⑮ SIRT POZİTİF YÜZEY (kamera arkada/OTS ise pozitif sırt cümlesi aranır) — 01.09.2026

**Kaynak:** THE THIN ROOF QA (28.08.2026) — S2 · 20,03-30,03 s, on saniyenin
altı karesinde de · ② DEVAMLILIK "Equipment 6/10"
**Sorun:** D79'un pozitif adlandırma çözümü uygulandığı hâlde bir sahnede düştü.
**2. vaka THE FROST LINE (31.08.2026):** "flat back / no back-mounted unit"
beyanı 50/50 prompttaydı ama bu dersin YAZIM KAPISI koşulmamıştı — kamera
arkayı gören iç sahnelerden birinde (yuva 13, kare t134) beyaz sırt ünitesi +
omuz kayışları doğdu; öteki arkadan sahnede (t155) sırt düz kaldı (1/2)

Kilit altı promptun altısında, D79'un istediği gibi prompt GÖVDESİNDE yazılıydı:

```
"... and a completely FLAT back — no backpack, no tank, no hose, no cable,
 no rear housing of any kind."
```

**Sonuç: 6 sahnenin 5'inde tuttu. Düştüğü tek sahne, kameranın kadının
ARKASINA geçtiği tek sahnedir.** S2'de (üst açı, azimut 200°) sırtında altın
renkli altıgen bir ünite ve iki omuz kayışı belirdi; on saniye boyunca kaldı.
② DEVAMLILIK bunu gördü ama teşhisi TERS kurdu ("çanta S5'te kayboluyor") —
çünkü belgesiz mercek için ilk görülen hâl doğru hâldir.

⭐ **Mekanizma:** yokluk kilidi, o yüzey KADRAJIN KONUSU olmadığı sürece
çalışır. Yüzey kadrajın konusu olunca model orayı **doldurmak** zorundadır
ve "no backpack" cümlesi ona ne KOYACAĞINI söylemez. Boş bir sırt, eğitim
verisinde astronot sırtı değildir.

**ÇÖZÜM — kamera özneyi ARKADAN ya da TEPEDEN gören her sahnede, yokluk
listesi o sahnenin promptunda POZİTİF yüzey tarifine çevrilir:**

```
Her back is turned to the camera in this shot and it is fully visible: the
back of the suit is one continuous smooth chalk-grey soft-shell panel from
collar to hip, unbroken, with a single matt indigo band running straight
across the shoulder blades. The panel carries nothing: no pack, no tank, no
housing, no strap, no buckle, no hose, no cable, no hard-point, no seam
other than the two shoulder seams. It is a plain surface, and the plain
surface is what this shot shows.
```

```
⛔ YAZIM KAPISI — sahne-kurulum dizisi yazılırken koşulur:
   Her kurulumun azimutu için sor: "kamera hangi yüzeyi görüyor?"
   O yüzeyde bir YOKLUK kilidi varsa (düz sırt · boş el · takısız yaka ·
   yamasız omuz), o sahnenin promptunda kilit POZİTİF TARİFE çevrilir.
   Yokluk cümlesi kalır; yerine geçmez, yanına eklenir.
```

⭐ Genel biçim: **yokluk kilidi görünmeyen yüzeyde beyandır, görünen yüzeyde
tariftir.** Aynı cümleyi iki yerde de kullanmak, kadrajın hangi yüzeyi
gösterdiğini prompta hiç söylememektir.

> 🔗 Ders 79 (düz sırt + berrak vizör prompt GÖVDESİNE) · Ders 59 (pozitif
> adlandırma) · Ders 42/58 (varlık sürekliliği) · Ders 134 (belgesiz mercek
> ilk gördüğü hâli doğru sanar — burada teşhisi tam ters kurdu).

---

## 🔴 DERS 152: ELDEKİ KÜÇÜK ALET KLİPTE BUHARLAŞIYOR, YÜKLÜ JEST NÖTR DURUŞA İNİYOR — "STAYS IN HIS HAND" KİLİDİ İKİ SAHNENİN İKİSİNDE DE TUTMADI

**Kaynak:** THE FROST LINE (31.08.2026) — S24: video promptu "the folding brush
stays in his hand" + imaj "mid-stroke, brushing" yazıyordu; karelerde (t222/t227)
fırça YOK, elde koyu bir panel var → FİNAL VURUŞ KANITI (fırçalı figür) FAIL ·
S20: "kelepçe çubuğunu ÇARPAR" yazıyordu; t193/t198'de çubuk 8 saniye boyunca
iki elde HAVADA tutuluyor, çarpma/mühürleme yok → DORUK VURUŞU FAIL · S11:
"yatak çerçevesinde, eli yamada, tepki planı" → boş elle koridor yürüyüşü
(t115/t118) · `FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_FROST_LINE.md`
**Sorun:** 1 filmde 3 sahne (+S0'ın süpürme jesti örnek karelerde yok).

Mekanizma: I2V modeli 10 saniyelik klipte SÜREKLİ ve NÖTR hareketi (yürümek,
durmak, tutmak) TEK SEFERLİK ve YÜKLÜ jestten (çarpmak, fırçalamak, çömelip
basmak) daha ucuza üretir; start frame jestin ortasını göstermiyorsa jest hiç
gelmez, elde kalması istenen küçük alet de kadrajdan silinir. "X stays in his
hand" bir YOKLUK KİLİDİ gibi davranır [D139 mekanizması]: modele neyi
GÖSTERECEĞİNİ söylemez.

**ÇÖZÜM — üç kilit birden:**

```
① START FRAME JESTİN ORTASINDA DONAR: imaj promptu aleti TEMAS hâlinde yazar —
   "the short folding brush mid-stroke ON the crown, bristles bent against the
   film, his wrist turned" (elde-duran değil, İŞ GÖREN alet).
② TIMELINE JESTİ EN AZ ÜÇ KEZ TEKRARLAR, her vuruş zaman damgalı:
   "0.0s stroke one · 3.0s stroke two · 6.0s stroke three" — tek fiil, tek
   nesne; klipte jestten başka hiçbir eylem yazılmaz.
③ ALET-JEST SAHNESİ ÜRETİM KAPISIDIR [D144 biçimi]: kabul ölçütü sayılır —
   "fırça 10/10 saniyede elde ve görünür · vuruş ≥3 kez okunur"; geçmeden
   komşu/ayna sahneler üretilmez.
```

> 🔗 Ders 139 (yokluk kilidi görünen yüzeyde POZİTİF tarife çevrilir — bu ders
> onu JESTE uygular) · Ders 42/58 (varlık sürekliliği) · Ders 144 (kapı biçimi) ·
> Ders 141/151 (vuruş kanıtı — teslim tarafı).

---

## 🔴 DERS 153: EŞ KADRAJ ÇİFTİ AYNI METİNLE AYNI SETİ ÜRETMİYOR — KELİMESİ KELİMESİNE AYNI ÜS PARAGRAFI İKİ UÇTA FARKLI MİMARİ; "LOOSE FOLDS" TARİFİ AYRI BİR BRANDA NESNESİ DOĞURDU

**Kaynak:** THE FROST LINE (31.08.2026) — S0 ve S24 imaj promptlarında ÜS+GEMİ
paragrafı birebir aynıydı; karelerde (t4 ↔ t222) yerleşim sınıfı aynı (gemi
solda · çanaklı düğüm · panel tarlası) ama modül dizilimi/sayısı ve panel
yerleşimi farklı — ② ve ⑤ kaymayı bağımsız yazdı. Daha ağırı: S24'ün "its film
fallen in loose folds over the shapes of the beds, crusted white with frost"
tarifi, kırağılı çökük TÜNEL FİLMİ yerine tünelin üstüne atılmış ayrı bir GRİ
ÖRTÜ/BRANDA üretti — dört mercek finali "pulling a massive tarp" diye okudu ·
`FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_FROST_LINE.md`
**Sorun:** 1 film ölçüldü; eş kadraj çifti kullanan her filmde aynı risk
(SKYLIGHT S0↔S24 çifti üretimde bu gözle ölçülmedi).

Mekanizma: metin tarifi, serbestlik derecelerini (dizilim, sayı, ölçek, kıvrım)
her üretimde YENİDEN atar; "aynı kadraj" vaadi metinle taşınamaz. Malzeme
tarifi de en yakın eğitim-verisi nesnesine yuvarlanır: "loose folds of film" →
tarp [D128 akrabası — metafor değil, düz tarif bile dönüşüyor].

**ÇÖZÜM — ayna sahnesinin imajı, kaynak sahnenin ONAYLI karesinden türetilir:**

```
① ÜRETİM SIRASI: önce S0 üretilir ve ONAYLANIR; S24'ün imajı S0'ın onaylı
   karesini referans/başlangıç görseli alarak üretilir (image-edit).
② FARK LİSTESİ ≤3 MADDE, yalnız FARKLAR yazılır: "same frame as the approved
   S0 still; ONLY these change: the jet is gone · the far third of the tunnel
   film has sagged onto the bed frames — the SAME translucent milk-white film,
   now crusted white, NOT a separate cover, NOT a tarp, nothing was thrown
   over the tunnel · the man now stands mid-stroke with the same brush."
③ DEĞİŞEN MALZEME KENDİ ADIYLA + "ayrı nesne değil" negatifiyle yazılır;
   arka plan seti (üs · gemi · panel) fark listesine GİRMEZ = aynen kalır.
```

> 🔗 Ders 58 (tekrarlayan varlık kimliği) · Ders 128 (malzeme tarifi başka
> nesneye yuvarlanır) · Ders 139 · Ders 154 (aynı mekanizmanın OLAY hâli) ·
> SAHNE_DEVAMLILIK_KILAVUZU (karakter çapalama — bu ders SETİ çapalar).

---

---

## 🔴 DERS 175: MÜHRÜ D169'UN KENDİ CÜMLESİ DELDİ — "THROUGH THE GLOVE" MODELE DERİYİ ÇİZDİRDİ, VE ÇIPLAK-DERİ YASAĞI YALNIZ YAKANIN ÜSTÜNÜ KAPATIYORDU

**KAPI:** BETİK · `prompt_kontrol.py` MÜHÜR KAPISI — mühürlü giysili filmde
her prompt taranır: gövde adı (`forearm` · `wrist` · `arm` · `neck` · `ankle`
· `shoulder`) geçen her cümlede **±12 kelime içinde** bir örtü adı
(`sleeve` · `cuff` · `suit` · `glove` · `seal`) ZORUNLU; ayrıca çıplak-deri
negatifi **üç bölge birden** yazılmadan geçmez (`above the collar` +
`at the wrist` + `at the ankle`). Tek bölge yazan negatif BLOCK.
**TEKRAR:** 0 · 04.09.2026 THE UPWARD FALL

**Kaynak:** THE UPWARD FALL · ⑪ ölçüm kapısı, 195-198 s'nin dört karesi
(`kol_195..198.jpg`) — S22 FIVE CUTS, filmin **MERKEZİ SEÇİM** sahnesi.
**Sorun:** 3,2 atm solunamaz atmosferde, kaskı 25/25 kapalı bir adamın
**önkolu bilekten yukarısı çıplak deri** olarak üretildi. Sekiz merceğin
sekizi de gördü ve hiçbiri yazmadı — ① rubriğinin `SEAL COUNT` maddesi
("report any bare skin that appears with the second it appears") o sahnede
hiç işletilmedi; ① aynı kareye yalnız "el bıçak sapıyla eriyor" yazdı.

⭐ **MEKANİZMA — DERSİN KENDİ REÇETESİ ARIZAYI ÜRETTİ.** [[D169]] efor
kanalı sözlüğünün ÖNKOL satırı şudur ve S22'de **birebir** kullanıldı:

```
D169 · ÖNKOL kanalı:   "the forearm tendons stand out through the glove"
S22 video promptu:     "the forearm tendons stand out through the glove"
```

`through the glove` bir eldiven tarifi değil, bir **saydamlık** tarifidir.
Model tendonu görünür kılmak için eldiveni değil DERİYİ çizdi. Yanına da
görsel promptun şu iki cümlesi düştü:

```
"In this frame only his two gloved hands and forearms are in shot."
      → `gloved` yalnız HANDS'e bağlı; `forearms` örtüsüz kaldı
"the left forearm carries a thin pale scratch along its outer side"
      → YIPRANMA KİLİDİ gövdeye yazıldı. Çizik bir DERİ işaretidir;
        giysi yüzeyine yazılsaydı ("a thin pale scratch on the left
        SLEEVE of the suit") aynı kilit mühre dokunmazdı.
```

Üç cümle de tek başına masum; üçü bir arada mühürsüz bir kol tarif ediyor.

⛔ **VE YASAK NEDEN TUTMADI:** depodaki çıplak-deri negatifi tek bölgeliydi —
`no bare skin above the collar`. İhlal **bilekte** oldu. Bu [[D171]]'in
mekanizmasının ekipman tarafındaki hâlidir: *"şu yerlere iyi bak" diyen
kilit, ihlali o yerlerin dışında gizler.*

**ÇÖZÜM — ÜÇ SATIR:**

```
① D169'un ÖNKOL kanal cümlesi mühürlü filmde DEĞİŞİR — zorlanma
   ELDİVENİN ÜSTÜNDE okunur, derinin üstünde değil:
      ✗  "the forearm tendons stand out through the glove"
      ✅ "the glove's ribbed segments tighten and lift over the tendons"
      ✅ "the sleeve's fabric draws taut along the forearm on each stroke"

② YIPRANMA KİLİDİ GİYSİ YÜZEYİNE YAZILIR, GÖVDEYE DEĞİL:
      ✗  "a thin pale scratch on the left forearm"
      ✅ "a thin pale scratch on the left forearm SLEEVE of the suit"

③ ÇIPLAK-DERİ NEGATİFİ ÜÇ BÖLGELİDİR, her insanlı promptta:
      NEGATIVE: no bare skin anywhere — none above the collar, none at
      the wrists between glove and sleeve, none at the ankles between
      boot and leg; every seam is closed and every seal ring is visible.
```

---

## 🔴 DERS 196: NESNE İLE TEMAS MORFLAŞMASI — ELDİVEN VEYA PARMAKLAR TUTULAN NESNEYLE ERİYOR VEYA YAPISINI KAYBEDEDİYOR

**Kaynak:** THE GREEN CEILING QA (10.09.2026) — ① KARE (0:04, 3:10) `Contact morphing: fingers merge into case handles`, `gloves lose structural integrity upon touching the case lock`.

**Sorun:** Eldiven giymiş astronot/mürettebat elle bir çanta kulpunu, kilit mekanizmasını veya donanımı tuttuğu anda model el dokusunu nesne ile erimekte, eldiven sınırlarını kaybetmekte veya parmak ağını nesnenin malzemesine karıştırmaktadır.

**ÇÖZÜM — PROMPT VE İMAJ SEÇİMİ:**

1. İmaj promptunda dokunma/kavrama anı seçiliyorsa temas doğrudan nesnenin içine batan el olarak değil, nesne yüzeyine oturan belirgin eldiven sınırları ile yazılır.
2. Video promptuna pozitif sınır kilitleri eklenir:
   ```
   crisp glove mesh boundaries, no finger merging into handle, solid metallic handle shape, rigid glove structure upon contact
   ```


---

## 🔴 DERS 208: KİMLİK DİZİSİ İLAN EDİLMEDİ — YÜZ, GİYSİ RENGİ, AMBLEM KONUMU, KASK DURUMU VE KİR SAHNEDEN SAHNEYE BAŞKA BİR AKTÖRE GEÇTİ

**FREKANS:** 4 film · THE AMBER LATTICE (② — S2 erkek yüz / S6 kadın yüz) · THE CRACKED HELMET (② 2,0 — siyah↔beyaz giysi 12 sahnede 5 kez; amblem omuz→sırt; 4,0 — tamir edilen vizör çatlağı finalde sıfır) · THE RING WALKER (② 7,4 — amblem sol omuzdan sağa aynalandı S11) · LOW_POWER (② 5,1 — S2/S10/S24/S29 dört yüz; kask S18-S24 takılı/çıkık flicker; kir S14'te temizlendi; ① 5,4 — göğüste parmak erimesi)
**DEĞİŞEN SATIR:** `<FILM>_QA_SPEC.md` C bloğu **KİMLİK DİZİSİ** satırı — sahne başına `K/A` kask dizisi · amblem konumu (SOL/SAĞ omuz) · giysi rengi · kir bölgesi + başlangıç sahnesi; ② DEVAMLILIK'in CHARACTER PASSPORT'u bu satırı okur, ilan edilmeyen özellik ihlal yazılamaz, ilan edilen tek sapmada 🔴
**KAPI:** LİSTE · `FILM_KLASOR_SABLONU/FILM_QA_SPEC.md` C bloğu KİMLİK DİZİSİ (eklendi 14.09.2026) · REFERANS_PAKETI T1/T2
**TEKRAR:** 1 · 15.09.2026 MARS_SON_CIKIS (mod V · KANAL İLAN EDİLDİ, YİNE KAYDI: SPEC C `KİMLİK DİZİSİ … Aras (Oksit Turuncu + Sol Kol Askısı S14-S36)` + S20 promptu `securing his injured left arm` → ② B2 🔴 askı S20-S34 SAĞ kolda, S36'da SOL · ② B1 🟠 turuncu omuz yaması S1 sol omuz → S9 sağ omuz · ② B2 🟠 kadın giysisinde yalnız S33'te lacivert göğüs plakası; satırın yazılı olması tutmaya yetmedi)

**Kaynak:** THE CRACKED HELMET QA (10.09.2026) — ② `0:00 (S1) black suit vs 0:20 (S3) white suit, patches migrate between shoulders and backpack`. Zincir ADAY-16 · 29 · 30 · 47 · 60 · 61 · 62.

**Örüntü:** Dört filmde kimlik beş ayrı kanalda kaydı (yüz · renk · amblem · kask durumu · kir) ve dördünde de kayan kanal SPEC'te **sayı olarak** ilan edilmemişti — ② bunu ancak "değişti" diye yazabildi, "S3'te ilan edilenden saptı" diye değil. D79/D146 vizörü, D42 yıpranmayı, D8 kıyafeti tek tek kilitledi; beşinin **dizisi** hiçbir yerde tek satır değildi.

**ÇÖZÜM — BEŞ KANAL TEK SATIR:**
```
KİMLİK DİZİSİ   kask K K K A A K … (sahne sayısı kadar) · amblem SOL omuz · giysi slate-grey ·
                kir sağ yanak S7'den itibaren · vizör hasarı S8'den itibaren (geri dönmez)
```
1. Satır SPEC C bloğunda, PLAN Character Bible ile birebir.
2. Dizideki K→A geçişi sahne haritasında bir OLAY'dır (kask çıkarma sahnesi yazılır); yazılmamış geçiş üretilmez.
3. Referans paketi varsa (T1 kask · T2 biçim kilidi) sayfa numarası dizinin yanına.

🔗 [[D8]] · [[D37]] · [[D42]] · [[D79]] · [[D146]] · [[D167]] · [[D196]] (temas morfu)
