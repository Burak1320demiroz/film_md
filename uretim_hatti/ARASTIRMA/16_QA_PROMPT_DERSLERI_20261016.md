# 🧪 16 — QA × PROMPT DERSLERİ · yeni hattın beş filmi (16.10.2026)

> **Girdi:** `qa_prompt_analizi_20261016/`. Beş film, 390 ham satır → 269 tekil bulgu. Her bulgu o çekimin Görsel ve Video promptuyla birebir alıntılanarak karşılaştırıldı.
> **Yöntem:** `GOREV.md` · sınıflama `QA_OKUMA_KILAVUZU.md` §1 v1.0 · 🅐 model sapması · 🅑 prompt boşluğu · 🅑+ prompt daveti · 🅒 QA yanıldı · 🅓 eşlenemedi.
> **Bu dosya kural yazmaz.**
> - §B dersleri prompt yazarının okuyacağı adaylardır.
> - Atlasa, ajan dosyasına ya da `film_dogrula`'ya girmeleri sahip kararıdır (§F, AGENTS §1 ④).
> **Atıf biçimi:** `SKY #49` = `qa_prompt_analizi_20261016/THE_SKY_CATCH.md` BULGULAR satırı 49. Çekim numaraları hat/plan numarasıdır, QA montaj numarası değil.

---

## A · Sayılar

| Film | Tekil | 🅐 | 🅑 | 🅑+ | 🅒 | 🅓 | 🅑 oranı |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| WRONG_BURN | 48 | 14 | 14 | 7 | 12 | 1 | %60 |
| PLANET_THIEF | 66 | 10 | 32 | 16 | 8 | 0 | %83 |
| MAYDAY_SEA | 47 | 15 | 9 | 11 | 8 | 4 | %57 |
| SKY_CATCH | 64 | 14 | 21 | 19 | 6 | 4 | %74 |
| FURNACE_GATE (C25-C48) | 44 | 9 | 18 | 5 | 12 | 0 | %72 |
| **toplam** | **269** | **62** | **94** | **58** | **46** | **9** | **152/214 = %71** |

- **Gerçek kusurların %71'inde prompt ya eksikti (🅑) ya da kusuru çağırdı (🅑+).**
  - Eski hattın 06.10 analizinde bu oran %56'ydı (248/443). Sözleşme aynı, ama film kümesi ve kaynak geçerliliği farklı; iki sayı yan yana konur, karşılaştırılmaz.
  - Yeni hat negatif bloğu ve meta etiketi temizledi: 5 filmde Cxx/Scene etiketi 0 ve prompt uzunluğu sorunu 0. Boşluk başka yere kaydı (§B).
- **Doğduğu yer:**

  | Yer | Bulgu |
  |---|:--:|
  | kare | 109 |
  | hareket | 55 |
  | ses | 33 |
  | kurgu | 17 |
  | anlatım | 8 |
  | — (🅒/🅓) | 47 |

  Kusurların yarıya yakını **başlangıç karesinde zaten vardı**. Görsel promptu ve kare kabulü, video promptundan daha önemli.
- **Tür × sınıf** (en sık 12; film = kaç filmde görüldü):

| Tür | n | film | 🅐 | 🅑 | 🅑+ | 🅒 | Prompta bağlı |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| giysi/işaret/arma/bant | 32 | 5 | 10 | **18** | 0 | 4 | 18/28 |
| dünya/arka plan | 32 | 5 | 7 | 9 | 9 | 7 | 18/25 |
| ekipman/nesne biçimi | 31 | 5 | 7 | **15** | 8 | 0 | 23/30 |
| replik/ses (kesmede ses sıçraması dahil) | 26 | 5 | 6 | 15 | 2 | 1 | 17/23 ¹ |
| ortama aykırı ses | 23 | 5 | 6 | 9 | 6 | 2 | 15/21 ¹ |
| hikâye/anlatım | 22 | 5 | 0 | 4 | 6 | 9 | 10/10 |
| yerçekimi/fizik | 17 | 5 | 5 | 3 | 4 | 5 | 7/12 |
| istenmeyen yazı/bayrak | 11 | 4 | **0** | 3 | 4 | 4 | **7/7** |
| ışık | 11 | 4 | 3 | 3 | 4 | 1 | 7/10 |
| yön/180°/koltuk | 11 | 4 | 3 | 2 | 0 | **5** | 2/5 |
| parçacık/duman/alev/sıvı | 10 | 4 | 1 | 0 | **9** | 0 | **9/10** |
| yüz/kimlik | 9 | 4 | 3 | 4 | 1 | 1 | 5/8 |

¹ Bu satırlarda prompt ses tarifini kurala uyarak yazmamıştı; müdahale yeri kurgu (klip sesi kapalı, yatak kurulur). Sınıf 🅑 ama ders prompt yazımı değil (§B Y13).

- **Üç keskin sinyal:**
  - **Duman, alev, sıvı:** 10 bulgunun 9'u 🅑+. Bu türde kusuru neredeyse her zaman promptun kendi kelimesi çağırdı.
  - **İstenmeyen yazı ve bayrak:** 7 gerçek bulgunun 7'si prompta bağlı, 🅐 sıfır. Yazı kilidi yazılı olan hiçbir çekimde yazı çıkmadı.
  - **Giysi ve işaret:** 🅑 18'e karşı 🅑+ 0. Prompt yanlış bir şey istemedi, yeterince söylemedi.

---

## B · Prompt yazımı için 13 ders

Her ders: yazılmayan (✗, gerçek alıntı) → yazılan (✓) · kanıt · durum. **Durum** sütunu dersin bugün nerede yazılı olduğunu söyler. 🅐 olan bulguda "prompta ekle" denmez, müdahale yeri yazılır.

### Y1 · İşaret: sayı + taraf + konum + tek işaret kilidi, kolun ya da göğsün göründüğü HER çekimde — 5/5 film
- ✗ `teal upper-arm bands` · `an orange band on each shoulder` · `a blue-gold geometric-sun badge` (konumsuz) · `burnt-orange arm bands`
- ✓ `one narrow muted-teal band around each upper arm` · `a round blue-and-gold sun badge on her left chest, the only marking on the suit`
- **Kanıt:**
  - FURNACE (`G03` ↔ `G04`): rozet konumu yazılı 4 çekimde rozet kayması 0; konum yazılmayan 12 çekimde 4 (#25 #27 #29 #21). Bant kol+sayıyla yalnız C39'da yazılı, orada bant kayması yok.
  - PLANET: `plain unmarked surfaces` yazılı 8 çekimde (G01) yazı/arma 0; yazılı olmayan 16 çekimde 1 (#49).
  - Toplam: 🅑 18 bulgu. Diğer kayıtlar: WRONG #9 #16 · MAYDAY #11 #16 #26 · SKY #2 #9 #14 #19 #32 #40 #44 #56.
  - `the only marking` beş filmin promptlarında **0** kez geçiyor.
- **🅐 10:** yazılıyken de kaydı (MAYDAY #10 ön kol bandı, WRONG #44, FURNACE #18). Müdahale yeri kare kabulüdür (KIMLIK §9).
- **Durum:** kural **var, uygulanmadı**. `goruntu-yonetmeni.md:38` (12.10): "Asimetrik işaret hangi taraftaysa yazılır … Sayılabilir öğe rakamla yazılır". KIMLIK §4 (16.10). F5 devamlılık raporu FURNACE'ta yokluğu çelişki saymadı.

### Y2 · Kimlik cümlesi kaynaktan kelime kelime gelir; çekimde kısalmaz, özne yeniden adlandırılmaz — 5/5 film
- ✗ Aynı kişi için beş farklı ad (PLANET): `the pilot` · `an orbital rescue pilot` · `An adult man in an elegant…` · `a tiny helmeted figure`
- ✗ Kayan kelimeler:
  - FURNACE: referans sayfası `narrow burnt-orange bands on both upper arms` → çekim `orange upper-arm bands`
  - SKY: referans anahtarındaki yedi farklı "take … from it" listesi
  - WRONG: vizör üç biçimde yazılmış
- ✓ FILM §3'teki tek cümle her çekimde aynı kelimelerle. Yüzün okunduğu çekimde görünen yüz parçaları da yazılır (`close dark stubble, short dark hair`).
- **Kanıt:** PLANET #28 #43 (C19'da sakalsız başka yüz; sakal hiçbir promptta yok) · SKY #15 #32 #40 #45 (yüz yalnız `take Sana's face … from it` ile) · WRONG #19 #22.
- **Durum:** **çatışma.**
  - PLANET `G02` başlığı: "kimlik yığını çekim promptlarında tekrarlanmaz" (BILINEN §A HİPOTEZ, F5 kararı 11).
  - KIMLIK §1 (16.10): "kimlik cümlesi her promptta birebir".
  - Bu ders **Görsel** promptu içindir. K9 (videoda yeniden tarif etmemek) ayrı soru.
  - → sahip, §F S3.

### Y3 · Nesnenin ve aracın da kimlik cümlesi olur — 5/5 film, 31 bulgu
- ✗ İşlev adı tek başına yazılınca model biçimi kendi seçti:

  | Promptta | Ekranda |
  |---|---|
  | `the compact matte-black plasma cutter` | kutu, matkap, tüfek (PLANET #29 #45) |
  | `a single hinged clamp` | iki çene (MAYDAY #6) |
  | `two fixed short graphite fins` | kuyruk (PLANET #13) |
  | `the sealed elevator car` | yumurta (SKY #53) |
  | `short front emitter` | namlu (FURNACE #7) |
  | `the compact graphite core` (ölçüsüz) | büyük kutu ↔ küçük modül (FURNACE #3 #11) |

- ✓ Biçim + ölçü + taraf her çekimde birebir:
  - `a thick plain handle and a short rigid cylindrical nozzle with one small dim orange power light`
  - `one curved latch arm hinged at its top`
  - `a rigid rectangular ivory capsule`
  - `the core, the size of a shoebox, on her chest`
- Göğüs kadrajdaysa taşınan nesnenin durumu yazılır, yüz ya da profil paneli seçilse bile (FURNACE #24 #38: çekirdek kayboldu).
- **Kanıt:** 🅑 15 · 🅑+ 8. Diğer kayıtlar: SKY #8 #18 #31 #59 · MAYDAY #38 · PLANET #16 #19 #34 #35 #44.
- **Durum:** **yeni.** Hat kuralı "birebir aynı kelimeler"i yalnız karakter için istiyor.

### Y4 · Tek bir çağrışımlı kelime yanlış nesneyi getirir: sembol adı, kişi adı, gündelik kelime — 5/5 film

| Promptta | Ekranda | Bulgu |
|---|---|---|
| `showing an abstract crescent` | göğsün iki yanında hilal-yıldız | PLANET #49 |
| `the beacon lamp of a distant man` | figür + kaskta dev ışık küresi | WRONG #13 |
| `Small old wrecks` (C01'deki `spacecraft` düşmüş) | fenerli ahşap kalyonlar | MAYDAY #29 (hat C14) |
| `the ocean horizon` | dalga sesi | PLANET #60 |
| `Two thick fixed fracture edges` | kırık beton/taş | SKY #8 |
| `clipped to his belt` (×3) | "kemer tokası"; anlam taşıyan nesne (tether) okunmuyor | FURNACE #31 |
| `the red lamp above the doorway pulses slowly over it` | dronun üstünde polis sireni | FURNACE #13 |

- ✓ Sembol yerine biçim (`a plain gold triangle`); kişi yerine boyut (`a tiny amber point, no bigger than a star`). Tasarım kelimesi her çekimde tam (`old spacecraft wrecks`). Anlam taşıyan nesne kendi adıyla (`the anchor block of his safety tether`).
- Işık kaynağı öznenin üstüne ya da konuşan ağzın önüne konmaz (FURNACE #13 #22).
- **Durum:** **yeni.** Atlas A11 yalnız kelimenin yazıya basılmasını anlatıyor; burada sorun kelimenin anlamı.

### Y5 · Vakumda ve kuru kabinde akışkan, ateş ya da su çağıran kelime yazılmaz; hedef hâl katı ve olumlu yazılır — 4/5 film, 10 bulgunun 9'u 🅑+

| ✗ yazılan | Ekranda | ✓ yazılacak |
|---|---|---|
| `sustained bright exhaust plumes` · `soft engine plumes` · `warm exhaust ignition glow` (SKY #49 #58) | dumanlı kamp ateşi, gri duman bulutu | `a short bright core at each nozzle and a pale translucent plume that fades within a second` |
| `swells in place … washes across the underside` (FURNACE #33) | gövdede atmosferik alev ve duman | `the trench glows steady orange; the hull edges catch the light, nothing burns` |
| `an irregular dark mass with a ragged outline` · `spreading` · `sweeps over` (PLANET #41 #57) | baca dumanı, kül | `a sharp-edged field of absolute black whose edge stays crisp` |
| `droplets shake loose` · `bubbles … rise in a thin trail` · `The drop … falls` (MAYDAY #14 #20 #33) | sürekli damlama, kabarcık | `the liquid stays in one piece, clinging to the ring` |
| `realistic metal and wet-surface detail` · `cool blue water reflections` (kokpitte) (MAYDAY #34) | kapalı kokpitte yağmur | `the cabin is dry`; ışık kaynağıyla (`cool light from the canopy`) |

- **Durum:** ilke `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` §2-§3'te (16.10, bu filmlerden sonra yazıldı); kelime listesi yeni. Atlas A12'nin genişlemesi.

### Y6 · Ortak cümleye çekime bağlı öğe konmaz — 4/5 film
- **Kanıt:**
  - MAYDAY: `wet-surface detail` 48/48 promptta, kuru kokpitte de (#34).
  - PLANET: kapanış `warm amber practical light` camgöbeği kokpitte; C04 aynı blokta `lit by cyan console glow` diyor (#9).
  - WRONG: ortak dünya cümlesi Dünya'yı kadraj dışı çekime çağırdı. C05: `which lies below the frame` ↔ aynı promptta `planet Earth with a thin blue atmospheric rim` (#20).
  - SKY: video promptlarındaki ortak cümle FILM §3'ün farklı bir varyantı; buna ek olarak 24/24 promptta ses cümlesi var.
- ✓ Ortak cümle yalnız film boyu değişmeyeni taşır: kimlik + doku/stil. Işık, su, gezegen, ses mekân cümlesine ya da çekim cümlesine gider. Mekân cümlesi o mekânın her çekiminde birebir kalır.
- **Durum:** **yeni.** 12.10 ORTAK GÖRÜNÜM kuralının içeriği tanımsız → sahip, §F S4.

### Y7 · Görünen her açıklığın ardı ve kişinin arkası her çekimde yazılır; komşu çekimde yazılı olması yetmez — 5/5 film
- ✗ ve sonucu:
  - PLANET #48: `Warm artificial sunlight from the panoramic window on the far wall` → bulut, dağ, teras.
  - FURNACE #6: `just beyond the open doorway` (ardı yok; C28'de yazılıydı) → kayalık gezegen yüzeyi.
  - MAYDAY #28 (hat C13): `the broad window carries a soft cyan water reflection` → mercanlı deniz tabanı.
  - SKY #35: `KITE remains at left` (ne referans ne tarif var) → başka bir uydu.
- ✓ İki biçim:
  - Açıklığın ardı: `the window looks into the enclosed refuge: black ribs and the artificial sun in its three rings`.
  - Kişinin arkası: `behind her the vault's graphite wall with one vertical amber light strip`.
- **Kanıt:** dünya/arka plan 32 bulgu (🅑 9 · 🅑+ 9). Diğer kayıtlar: PLANET #6 #37 · MAYDAY #13 · SKY #10 #25 #28 · FURNACE #5 #9 · WRONG #14 #28 #38.
- **Durum:** kısmen var: `GPT_IMAGE_OMNI_KILAVUZU` §5 mimari çapa (16.10) · atlas A13. "Açıklığın ardı" yeni.

### Y8 · Ekran ya da gösterge adıyla kadraja konmaz; her Görsel'de yazı kilidi bulunur — 4/5 film, 7/7 prompta bağlı
- ✗ `beside a dark passenger-status display` · `as the status indicators confirm full pressure stability` (SKY #1 #11 #57)
- ✗ `its face still turned toward her` (FURNACE C37: bilek cihazı ekran gibi okundu)
- ✓ `a plain dark glass panel with one thin amber light bar` + `plain unmarked surfaces`
- Kilitli çekimlerde yazı bulgusu 0 (PLANET G01). SKY'da çekim Görsel'lerinde yazı kilidi 0/24 (yalnız referans promptlarında var) → bayrak, logo, yazı (SKY #16 #42 #52).
- **Durum:** var (BILINEN §B2 · §C), uygulanmadı. Olumsuz dışlama satırı (`No text, logos or flags.`) K2 ile sahibi bekliyor.

### Y9 · 0 g'de 1 g fiili ve heykel pozu yazılmaz; eforun beden işareti yazılır — 4/5 film
- ✗ `shifts her weight slightly forward … checking her footing` (SKY #17) · `lifts it upward` (SKY #26)
- ✗ `upright, arms at his sides, legs together` (iple çekilen beden, WRONG #40)
- ✗ `the lever starting to rock out of its upright rest` + `one smooth, firm arc` (MAYDAY #35)
- ✓ `one glove locked on the rail, her body drifting a hand's width as she pulls` · `his shoulders jerk a beat after the rope tightens` · `the lever resists; her elbow locks and her helmet dips with the effort`
- Omuz üstünde açık avuç selam gibi okunur (WRONG #36).
- **Durum:** atlas KARANTİNA'da "Mikrogravitede 1g deyimi" LAST_GATE'ten tek vaka olarak duruyor. SKY ikinci film → **girdiye çıkma adayı** (§F S1). UZAY_FIZIGI §4 (16.10).

### Y10 · Son vuruş donmaz; "slow" ve "still" birikmez; vuruşa tek taşıyıcı olay — 4/5 film
- ✗ SKY:
  - `until the separation gap becomes completely stationary` · `The tilt settles` (#6 #37 🅑+)
  - 24/24 çekim aynı `0-5 s / 5-10 s` ızgarası
- ✗ FURNACE:
  - C43'te `slow` dört kez (#23)
  - C46'da iki sıralı işaret + 5 s'lik replik aynı vuruşta (#40)
- ✗ PLANET: 13/24 çekimde aynı orta vuruş kalıbı (`quickens a little`, `a little faster`), rijit yapılar ivmeleniyor.
- WRONG'daki `perfectly still` 🅒'dir (tasarım). Ama dört ayrı izleyici tepkisi "sahte, kıpırtısız" diyor → mikro hareket (nefes, baş takibi).
- **Durum:** kural var ("son vuruş donmaz", `goruntu-yonetmeni`). Atlas KARANTİNA'daki "3-4-3 TIMELINE + hold bitişi" (LAST_GATE) ikinci filmini buldu → **girdiye çıkma adayı**.

### Y11 · "Reference n (rol): take X from it" yalnız o sayfada görüneni ister; özel ad referansı ya da tarifi olmadan yazılmaz — 2/5 film
- ✗ SKY:
  - `Reference 5 (cockpit): take … side view of the capsule from it` (kokpit sayfasında kabin yok → yanlış istasyon, #4 #5).
  - `take Sana's pearl-white magnetic boots … from it` (bel üstü portreden bot istiyor).
  - 12 çekimde aynı türden istek var.
- ✗ PLANET:
  - `Reference 4 (black ark): take … Earth` (Dünya "ark" sayfasından).
  - C19: iki nesneli sayfadan yalnız kesici alındı; tarayıcı serbest kaldı ve sağ bileğe geçti (#44).
- ✓ Sayfada olmayan şey metinle tarif edilir. Çok nesneli sayfada her nesne ayrı adlandırılır.
- **Durum:** kısmen var ("Ekli olmayan referans anılmaz"). "Referansta olmayan istenmez" kısmı yeni.

### Y12 · Aynı promptta zıt istek — 5/5 film; atlasta var (A05/A06), hâlâ çıkıyor

| Film · çekim | Bir taraf | Öbür taraf | Bulgu |
|---|---|---|---|
| WRONG C02 | `the whole suit moves steadily toward the right` | `she holds her place in the frame` | — |
| PLANET C14 | korkuluk `slide outward past the edges of the picture` | `the small figure stays standing at the railing` | #36 |
| PLANET C21 | `the familiar African landmass … clearly readable` | `most of Earth … in blue-black shadow` | #55 |
| MAYDAY C23 | `cool blue water reflections` | `Through the canopy only distant stars` | — |
| MAYDAY C14 | kamera vakumda | `deep, slow waterborne resonance` (su altı sesi) | — |

- **Durum:** var, uygulanmadı. F5 devamlılık çağrıları bunları yakalamadı.

### Y13 · Ses: model sesi kapalıysa video promptunda ses yok; açıksa sıfat ve vuruş söyleyişi bozmasın
- **Kapalı film:**
  - SKY'da 24/24 video promptunda `The only ambient sound is close suit breathing and faint mechanical hull vibration` var → vakumda yankılı metal sesleri, gülmeye benzer insan sesi (#24 #27 #30 #34, 🅑+).
  - Kural `goruntu-yonetmeni.md:65`: "Model sesi KAPALI filmde ses tarifi yazılmaz." Uygulanmadı.
- **Açık film** (MAYDAY, FURNACE):
  - `hesitant` takılma çağırdı ("Then who is call— is calling?", MAYDAY #19).
  - Acil replik `controlled breath` · `warm and low` · `calm breathing` ile sarıldı → düz okuma (#31).
  - Kadrajda tek kişi varken kadraj dışı replik yazıldı → replik ikilendi (FURNACE #1 #30).
  - Bunlar çoğunlukla 🅐. Müdahale yeri deneme seçimi ve kurgudur: `REPLIK_VE_KLIP_SESI_KILAVUZU` §1-§3.
- **5/5 montajda klip sesi açık kaldı:** vakum sesi ve kesmede ses sıçraması (≈40 bulgu). Bu prompt dersi değil; kurgu kuralı var, montaj hat dışında yapıldı.

---

## C · Kural vardı, uygulanmadı — boşluk yazımda değil denetimde

| Yazılı kural | Nerede | Çiğnendiği yer | Neden yakalanmadı |
|---|---|---|---|
| İşaret tarafı ve sayısı | `goruntu-yonetmeni.md:38` (12.10) | 5/5 film; FURNACE `G04` 0/12 | devamlılık F5 "tutarlı" dedi, yokluğu çelişki saymadı |
| Model sesi kapalı → ses tarifi yok | `goruntu-yonetmeni.md:65` | SKY 24/24 | F5 devamlılık ve denetçi bakmadı; `film_dogrula`'da kontrol yok |
| Son vuruş donmaz | `goruntu-yonetmeni` | SKY 6 çekim | mekanik kontrol yok |
| Aynı promptta zıt istek yok | `goruntu-yonetmeni` · atlas A05 | 5/5 film | devamlılık okumasına bağlı |
| Ekli olmayan referans anılmaz | `goruntu-yonetmeni` | SKY C14 · C15 | — |
| Klip sesi kurguda kapalı | AGENTS §2 · BILINEN §B3 | 5/5 montaj | montaj hat dışında, `kurgu.py` kullanılmadı |

**Sahibin paketi ↔ hattın çevirisi (SKY):**
- Sahibin `THE_SKY_CATCH.md` paketi rozetleri satır içinde yazıyordu, `No lettering, numbers, subtitles, logos` kilidi koyuyordu ve video önsözünde `No speech … dialogue and sound are added in editing` diyordu.
- Hattın F5 çevirisi (`G01-G03`) üçünü de düşürdü. Paket kullanılsaydı 13 bulgu 🅑'den 🅐'ya geçerdi: oran %74 → %50.
- Bu yalnız sınıf değişimidir; "o zaman kusur çıkmazdı" demek değildir. 🅐 da kusurdur.
- Yön açık ama: ajanlı çeviri sahibin kilitlerini koruyacağına attı. PLANET `G02` başlığındaki "kimlik yığını tekrarlanmaz" kararı da aynı yönde.
- → ajan eleştirisine girdi (`goruntu-yonetmeni` · `devamlilik` F5).

**Adalet notu:** Y3, Y4, Y5, Y7 ve Y11 bu filmler yazıldıktan sonra kılavuza girdi (16.10) ya da hiç yazılı değil. Bu dersler için "uygulanmadı" denemez.

---

## D · QA ve kayıt — analizi bulandıran, prompt dışı bulgular

1. **Kayıt yok (5/5):**
   - NOTLAR DENEMELER boş, `~/film_medya/<FILM>/{ref,kare,ham}` boş.
   - Hangi referansın yüklendiği bilinmediği için yüz ve giysi 🅐'ları koşullu: "model mi tutmadı, referans mı yüklenmedi" ayrılamıyor.
   - KIMLIK §1'in üçüncü katmanı (kayıt) bu yüzden ilk iştir.
2. **Numara kaymaları:**
   - MAYDAY: montajda hat C05 yok, rapordaki C05… = hat C06…. Hem `QA_DEGERLENDIRME` hem NOTLAR KARARLAR montaj numarasını hat numarası sanıyor.
   - SKY: QA numaraları Gemini'nin kesme sayımı. C05 ve C18 montajda yok; C01, C16 ve C22 büyük olasılıkla yok.
   - WRONG: C07 3 + 7 s'ye bölünmüş, sonda plansız başlık kartı var.
3. **Promptsuz yazılmış hükümler çürüdü:**
   - **WRONG C11 "yanlış klip seçildi" değil.** `G01` C11 tam da istasyondan uzaklaşmayı istiyor (`The small station at the right edge slowly shrinks.`). C11→C12 çelişkisinin kaynakları: tasarım + filme girmeyen kural replikleri + C11'deki çarpışma sapması (WRONG #39 #43).
   - **PLANET "kök neden: ref yerine bağımsız prompt":** kanıtsız (11_SUZME'de de not edildi).
   - **FURNACE NOTLAR KARARLAR (16.10) madde 6:** "C37-C47 koltuk değiştirmesi" diyor. Altı satırın 4'ü K19'un tasarladığı ön ↔ arka ¾ ters açı; tek gerçek hata C42 (FURNACE #20 #26 #37 #41 · #28).
4. **Geçersiz kaynak** (QA_OKUMA §4):
   - SKY'nin dört raporu 2:41'lik tek dosyada video modunda koşuldu (>90 s).
   - FURNACE'ın Süreklilik ve Tarama raporları 240 s ve "ne olmalı" boş. Giysi, arma ve koltuk bulgularının hepsi bu kaynaktan.
5. **🅒 46 bulgunun ikiye ayrılışı:**
   - Yaklaşık yarısı klasik yanılgı: tasarımı kusur saymak, başlık kartı, doğru fizik.
   - Kalanı **tasarımın izleyicideki gerçek bedeli**: kıpırtısızlık "sahte", boş kasa planı "kafa karıştırıyor", kilitli dış plan "sıkıcı" (WRONG #3 #12 #15 #30 · FURNACE #4 #17 · PLANET #24 #40).
   - Bunlar prompt dersi değil, çekim listesi dersi → F3'e geri besleme.
6. **İnsan doğrulaması 0/269.** Bu dosyadaki her sayı geçicidir.

---

## E · Bugünkü (16.10) dosyalarda düzeltilen atıflar

16.10 kılavuz taslakları ve 11/13/15 süzmeleri QA numaralarını hat numarası saymıştı. Atıflar silinmedi; yanlarına hat/plan numarası eklendi ("→ hat Cxx").

| Dosya | Eski atıf | Doğrusu |
|---|---|---|
| `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` §0, §3, §5 | MAYDAY C06/C18/C19/C20 | hat C07/C19/C20/C21 |
| `UZAY_FIZIGI_GORUNTU_KILAVUZU.md` §0, §5 | SKY C07/C08/C10/C11/C16 · C19 · C20/C24 | plan C09/C09/C11/C12/C19 · C20 · C21/C24 |
| `GPT_IMAGE_OMNI_KILAVUZU.md` §6 | "MAYDAY C11 kablo, SKY C09" | hat C12'de istenen sıvı şeritti, kablo değil. SKY plan C10'da bağ gevşek istenmiş, sert çıkmıştı (tersi) → **film kanıtı bu satırı desteklemiyor**; satır dış kaynağa dayanır |
| `GPT_IMAGE_OMNI_KILAVUZU.md` §9 · §10 | SKY C05→C06, C11→C12 · C07/C08/C16 | plan C04→C06, C12→C13 · C09/C09/C19 |
| `GPT_IMAGE_OMNI_KILAVUZU.md` §12 · `SECIM_VE_KURGU_KILAVUZU.md` başlık + §2 | WRONG C11↔C12 "yanlış deneme seçildi" | seçim değil, tasarım (§D 3) |
| `SECIM_VE_KURGU_KILAVUZU.md` başlık + §4 | SKY C05→C06 · C11→C12 · C17→C18 / C18 ters el | plan C04→C06 · C12→C13 · C20 → planda olmayan insert |
| `11_SUZME` · `13_SUZME` · `15_SUZME` | aynı atıflar | aynı düzeltme, satır içinde |

---

## F · Sahibe sorular

| # | Soru | Öneri |
|---|---|---|
| **S1** | `PROMPT_HATA_ATLASI.md`'ye yeni girdi (iki film şartı sağlanıyor) | **A15** işaret sayı/taraf (Y1, 5 film) · **A16** nesne kimlik cümlesi (Y3, 5 film) · **A17** çağrışımlı kelime (Y4, 5 film) · **A18** ortak cümlede çekime bağlı öğe (Y6, 4 film) · A12'ye Y5 kelime listesi · A13'e "açıklığın ardı" (Y7) · KARANTİNA'dan girdiye: 1 g deyimi (Y9, LAST_GATE + SKY) ve hold bitişi (Y10, LAST_GATE + SKY/FURNACE) |
| **S2** | `goruntu-yonetmeni` ve `devamlilik` (F5) için "yazdıktan sonra 8 soru" | kimlikli her çekimde işaret cümlesi var mı · ortak cümlede su/ışık/gezegen var mı · görünen açıklığın ardı yazılı mı · nesne biçim cümlesi birebir mi · vakumda akışkan/ateş kelimesi var mı · ekran adı var mı · referans rolü sayfada görüneni mi istiyor · model sesi kapalıysa video'da ses kelimesi var mı |
| **S3** | Görsel promptunda kimlik cümlesi her çekimde tam mı (Y2)? | **Evet.** PLANET `G02`'deki "kimlik yığını tekrarlanmaz" kararı yeni filmlerde uygulanmaz. Video promptu ayrı soru (K9). |
| **S4** | ORTAK GÖRÜNÜM'ün içeriği sınırlansın mı (Y6)? | Yalnız kimlik + doku/stil; ışık, su, gezegen ve ses mekân cümlesine. |
| **S5** | `film_dogrula`'ya mekanik kontrol (13 §D A2 ile birlikte) | (a) kimlik bloğu olan çekimde `left/right` + sayı + `the only marking` · (b) model sesi kapalıysa video promptunda `sound`/`breathing`/`hum` yok · (c) dış çekimde `plume`/`smoke`/`drip`/`wet` uyarısı. Uyarı olarak, ret değil. |
| **S6** | FURNACE NOTLAR KARARLAR madde 6 (koltuk) | Çalışma kopyası sahibin; dokunulmadı. C37-C47'nin 4'ü tasarım, yalnız C42 yeniden üretilir. |
| **S7** | Altın set: 269 bulgudan rastgele 40-50'sine insan gözü (QA_OKUMA §3) | Medya `~/film_medya/<FILM>/`'ye konunca. |
