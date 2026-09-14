# 🎬 UZAY GİYSİSİ SİNEMATİK TASARIM KILAVUZU — Giysinin Görünüşü

> **Ne zaman okunur:** Yeni uzay filmi yazılırken, **Character Bible
> yazılmadan ÖNCE**, `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` ile BİRLİKTE.
> İş bölümü: DONANIM kılavuzu giysinin **kimliğini** (rol şeridi · amblem ·
> bilek/saat · eşya · sırt silueti A/B/C) kurar; bu kılavuz giysinin
> **görünüşünü** (arketip · kask mimarisi · malzeme · renk · kir · sırtın
> tarif biçimi · bütçe) kurar. İkisi tek İngilizce bloğa iner.
> **Ne işe yarar:** "white pressure suit" boşluğunu doldurur. Beş siluet
> arketipini deponun grameriyle (D79 vizör berrak · D139 sırt tek yüzey ·
> D146 çerçevesiz vizör yok · metin/marka yok · yasak listesi tuzağı yok)
> yazılabilir hâle getirir; sert kabuğu oyun-görünümünden korur.
> **Kaynak:** TUR 17 dış araştırması (12.09.2026) —
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 17. Ham raporlar:
> `URETIM_ONCESI_ANALIZ/TUR17_HAM_RAPORLAR/`. Kural buradan okunur,
> bulgunun nereden geldiği oradan.
>
> ⚠️ **DÜRÜST SINIR:** Üç raporun da kaynak listesi gelmedi; sayı katmanı
> çürük çıktı (04 §T17.4). Bu kılavuz **sayısız** yazıldı — "yüzde", "oran",
> "eşik" satırı yoktur, olanlar ⬜ HİPOTEZ etiketlidir. Hiçbir arketip
> henüz depoda üretilmedi; "havalı" olup olmadığını bu belge ölçemez.
> Ölçen şey: ilk uygulamada sahibin gözü + R1 paneli + ① KARE / ②
> DEVAMLILIK + ⬜ ⑭ tasarım sadakati merceği (§12).

---

# 0. ⛔ DEĞİŞMEYEN KARARLAR — bu kılavuz TARİF BİÇİMİNİ değiştirir, kararı değil

```
① VİZÖR BERRAK, YÜZ HER KAREDE OKUNUR [D79 · D95 · T11.5③ sahip kararı].
   Aynalı / opak / altın / dar pencereli vizör yazılmaz. Yüzü kapatan
   yoğuşma yazılmaz (buğu yalnız vizör KENARINDA — DONANIM §5).
② SIRT SAHNEDEN SAHNEYE KAYMAZ [D79 · D139]. Sırt her sahnede TEK,
   KAPALI, aynı cümleyle tarif edilen yüzeydir. Bu kılavuz "düz ve boş"
   yerine "heykelsi ve kapalı" yazmayı önerir (§8) — kaymazlık kararı aynı.
③ OKUNUR METİN, BAYRAK, LOGO, MARKA YOK [D34 · D45 · D138 · DONANIM §0①].
④ SERBEST HORTUM / KABLO / KORDON YOK [DONANIM §0③ · §7 yüksek risk].
⑤ NEGATİF ÇEKİRDEK SABİT [KILAVUZ_REHBERI §5]: "no CGI aesthetic, no video
   game aesthetic, photorealistic with 35mm film grain" her promptta.
   Bu kılavuz o cümleyle ÇEKİŞMEYEN pozitif tarif yazmayı öğretir (§5).
⑥ YASAK LİSTESİ TUZAĞI [REHBER §7]: pozitif tarifin İÇİNE "no hose",
   "no backpack", "not a bubble" yazılmaz — sınıflandırıcı kelimeyi okur.
   Yokluk NEGATIVE bibledadır; SUBJECT bloğu yalnız VAR OLANI yazar.
⑦ ÇERÇEVESİZ VİZÖR YAZILMAZ [D146 · REFERANS_PAKETI §4.1]: "seamless",
   "bubble", "dome" kubbe davetiyesidir. Pane + GÖRÜNÜR çerçeve yazılır.
⑧ KOPYA SINIRI [MESHUR_SAHNE §4]: film, karakter, tasarımcı, marka adı
   prompta girmez. Bu kılavuzun arketipleri film adsızdır; kaynak
   eşlemesi yalnız 04 §T17.3'te durur.
```

Sinemanın rutin sapmaları (ince bel, esnek eklem, sırt ünitesiz gövde,
kask içinden gelen yüz ışığı) genel izleyicide fark edilmez, uzman
izleyicide "sahte" okunur (T17.2 #8). Depo bu sapmaları D79 gereği
**bilinçli** yapar; sapma kayda geçer, savunulmaz.

---

# 1. 🩺 NEDEN KÖTÜ GÖRÜNÜYOR — teşhis ve cevabı

**Depo teşhisi (ölç: `grep -rhoiE "(white|grey|navy|orange)[a-z -]{0,40}(pressure|eva|space) suit" yatay_* dikey_* | sort | uniq -c | sort -rn`):**
film klasörlerindeki en sık giysi cümlesi tek sıfat + "pressure suit".
Biçim, halka, doku, kir, kask çerçevesi hiçbir bible'da yazılı değil.
Model boşluğu kendi varsayılanıyla dolduruyor; varsayılan stok ajans
giysisi. Üstüne D79/139 bloğu ("flat back, carrying nothing, zero
reflection") geliyor — devamlılık için doğru, ama geriye beyaz balon +
akvaryum kalıyor.

**Araştırmanın cevabı (T17.0 ①):** kötü görünen şey belgesel arketip
değil, **tarifsiz** arketip. Aynı beyaz giysi, görünür yaka ve bilek
halkası, dokulu kırık beyaz naylon, kumaş kıvrımı ve hafif aşınma
yazıldığında "viseral, otantik, güvenilir" okunuyor (T17.2 #2). Ters vaka
da kayıtlı: kısıtsız sade tarif ("sade siyah tişört") de kayar — model
boşluğu doldurur (T17.2 #21).

```
KURAL 1  ARKETİP DEĞİŞTİRMEDEN ÖNCE MEVCUT ARKETİPİ DOLDUR.
         Beyaz giysi kalabilir; halka + doku + kıvrım + global aşınma +
         görünür kask çerçevesi + heykelsi kapalı sırt YAZILIR (§11 örnek A).
KURAL 2  SADE ≠ BOŞ. Az öğe, ama her öğe yazılı. "Az ama büyük" öğe
         (DONANIM §1: BÜYÜK · GEOMETRİK · SAYILABİLİR) — "çok ama küçük"
         öğe hem kayar hem bütçe yer (§9).
KURAL 3  SERT KABUK ÜÇ KELİMEYLE YAZILIR: mat · aşınmış kenar · tekstil
         eklem. Biri eksikse kabuk yazılmaz (§5).
```

---

# 2. 🧍 BEŞ ARKETİP — film adsız geometri, hikâye tonu, depo uyumu

Kaynak: T17.2 #1 · geometriye çevirme T17.3. Sertlik dağılımı YÖN olarak
verilir (sayı yok). Her arketipin İngilizce bloğu §11'de, kısaltma sırası
§9'da.

| Kod | Arketip | Adsız geometri | Sertlik | Kask | Renk mantığı | Hikâye tonu | İzleyici okuması | Depo uyumu |
|:--:|---|---|---|---|---|---|---|---|
| **E** | **BELGESEL / TARİHSEL** | bol, kırışıklı gövde; omuz ≈ bel; dıştan görünür metal yaka ve bilek halkaları; körüklü dirsek/diz | ağırlıkla yumuşak çok katmanlı naylon, halkalarda metal | sert kabuk, elips/düz pane, GÖRÜNÜR yaka halkası | mat kırık beyaz / krem / toprak; gümüş halka | belgesel gerçekçilik · mekanik tehlike · insani kırılganlık · yorgun bürokrasi | otantik · viseral · güvenilir | ✅ **deponun mevcut giysisinin doldurulmuş hâli** — ilk seçim |
| **I** | **AĞIR ENDÜSTRİYEL** | geniş kapaklı omuz pedi; dikey kapitone gövde ve uyluk; ağır bilezikli bot/eldiven; bronz/pirinç yaka halkası | ped + kapitone kumaş + eklem plakası, dengeli | yuvarlak sert kabuk, geniş bronz yaka, kaşta SAYILI lamba | doygunluğu düşük sarı / taba / haki; koyu eklem kilitleri; global toz | endüstriyel emek · yıpranmış teknoloji · klostrofobik iş · sömürü | ağır · işlevsel · baskılayıcı | ✅ **en düşük oyun-görünümü riski** (kapitone + mat + kir) |
| **T** | **TEKNOKRATİK FORM-FİT** | vücuda oturan nervürlü teknik kumaş; omuz > bel (atletik); kompozit göğüs + omuz plakası; gömülü sırt paneli | ağırlıkla yumuşak, göğüs/omuzda kompozit | alçak sert kabuk, **düz veya hafif kavisli pane + görünür çerçeve** (küre DEĞİL), çerçeve içi ışık | iki tonlu koyu (arduvaz/lacivert) + tek aksan | kurumsal keşif · lüks teknoloji · biyolojik kırılganlık | zarif · pahalı · kırılgan | ✅ koşullu: plakalar "matte scuffed" + kumaş eklemle yazılır (§5) |
| **K** | **TAKTİK / YÜKSEK-G** | keskin köşeli omuz hattı; entegre boyun çemberi; modüler göğüs; gömülü bağlantılar; segmentli eklem | sert plaka ile mukavemetli kumaş yarı yarıya | çok yüzlü DÜZ panelli vizör, görünür çerçeve | mat füme / zeytin; parlak yüzey yok | askerî disiplin · sistemik çatışma · işlevsel sertlik | tehditkâr · disiplinli | ⚠️ **risk etiketli** (T17.1): mat + aşınmış kenar + tekstil eklem ÜÇÜ zorunlu; uzay operası yasağı sürer (UZAYLI §0) — ordu/filo yok, tek figür |
| **M** | **MONOLİTİK YALNIZLIK** | çan biçimli dev kask, yekpare dikey gövde, omuz eğimi yok, dar yatay pencere | neredeyse tamamen sert döküm | çan başlık, dar yatay izleme yarığı | monokrom mat altın/pirinç | mutlak yalnızlık · huşu · aşırı çevre tehdidi | korkutucu · insanüstü · yabancılaştırıcı | ⛔ **KULLANILMAZ** — dar pencere yüzü kapatır (D79), tamamen sert kabuk oyun-görünümü (T17.1 1↔2). Kayıt için tutulur |

```
SEÇİM ÖLÇÜTÜ (öncelik sırası):
 1. Hikâye tonu → satır (tablonun 7. sütunu). Tema ve tür kartı karar verir
    (TEMA_MUHENDISLIGI · UZAY_SENARYO). Ton uymuyorsa görünüş değil, plan
    yanlıştır.
 2. Ortam kartı → renk (§6 zemin tablosu). Mars'ta beyaz giysi ARKETİP
    kararı değil, kontrast kararıdır.
 3. Kamera mesafesi → doku kelimesi (§5 ölçek sütunu). 12 m lockoff'ta
    nervür yazmak boşa karakter harcar.
 4. Bütçe → kısaltma sırası (§9). Blok banda sığmıyorsa arketip değişmez,
    katman atılır.
 5. İki karakter varsa: AYNI arketip, TUR 5 rol şeridi + sırt A/B/C ile
    ayrışır; iki farklı arketip aynı kadraja girmez (kavram sızması, §10).
```

---

# 3. 📐 SİNEMATİK OKUMA DEĞİŞKENLERİ — ne yazınca ne okunur

Kaynak: T17.2 #3-4-7 · sayılar İNMEDİ (T17.4). Her satırın "yazım
karşılığı" sütunu bu kılavuzun asıl çıktısıdır.

| Değişken | Sinematik yön | Belgesel yön | Devrildiği yer (⬜ yön, sayı yok) | Yazım karşılığı |
|---|---|---|---|---|
| **Siluet okunurluğu** (tek renk gölgede duruş/kütle/rol okunur mu) | belirgin omuz hattı · kaskın gövdeden net ayrılması (görünür yaka) · TEK asimetrik büyük öğe | homojen torba, odak yok | omuz abartısı → "süper kahraman kostümü" | omuz: "broad padded shoulder caps" / "squared shoulder line"; yaka: "a visible … neck ring where the helmet locks to the collar" |
| **Sertlik kontrastı** | sert plaka ile yumuşak dokuma YAN YANA | tümü yumuşak, yalnız halkalar sert | sert kabuk baskınlaşınca oyuncak / oyun zırhı | plaka + eklem çifti hep birlikte: "matte scuffed composite chest plate … edged in worn rubber where it meets the ribbed fabric" |
| **Parça sayısı** | az sayıda büyük mimari blok, ritmik dikiş | çok küçük cep, kayış, dağınık kırışık | işlevsiz kablo/hortum → görsel gürültü (zaten yasak) | SAYILABİLİR ve BÜYÜK: "two shallow recessed panels", "two small square lamps" |
| **Yüzey parlaklığı** | mat-saten kumaş + yalnız plakalarda bölgesel parıltı | tamamen mat | tüm gövde parlak plastik → kostüm partisi | "matte" varsayılan; "brushed" yalnız metal halkalarda; "glossy/high-gloss" hiç |
| **Vizör alanı** | geniş berrak pane, yüz tam okunur | dar mekanik pencere | aynalı/opak → empati kesilir (D79 zaten yasak) | "a single flat front pane set inside a visible dark rim, the face fully readable through it" |
| **Kask içi ışık** | difüz gizli kaynak, yüz 3/4 aydınlık | yok, yalnız ortam ışığı | iç ışık ortam ışığını bastırırsa "sahte" | "a soft warm fill from inside the chin of the helmet on her face" — LIGHTING bloğunun ana ışığından ZAYIF yazılır; ⛔ "glow/glowing" D29 yasak kelimesi |

**Gölge testi (⭐ öneri, T17.2 #4):** R1 ön ve arka kareleri siyah silüete
indirilir (`ffmpeg -i R1.png -vf "format=gray,lutyuv=y='if(gt(val,40),255,0)'" sil.png`
ya da göz). Omuz hattı, yaka ayrımı ve sırt profili hâlâ okunuyorsa siluet
geçer; okunmuyorsa giysi değil, siluet yazılmamıştır.

---

# 4. 🪖 KASK MİMARİSİ VE KASK İÇİ IŞIK — berrak vizörle heybet

Kaynak: T17.2 #5-7-14. D79 vizörü berrak tutar; heybet kaybı kaskın
KABUĞU ve YAKASIYLA telafi edilir, vizörle değil.

**Dört kask tipi → depo karşılığı:**

| Tip | Sinemadaki okuması | Depoda yazımı |
|---|---|---|
| Küresel kubbe | panoramik, yüz kesintisiz | ⛔ "bubble / dome / seamless" YAZILMAZ (D146). Yerine: "a rounded hard shell with a wide clear front pane set inside a visible rim" |
| Düz pane + görünür çerçeve | mekanik, belgesel, güvenilir | ✅ varsayılan: "a hard shell with a single flat front pane set inside a visible dark-grey rim" (THE HARD DOCK emsali) |
| Çok yüzlü düz paneller | askerî, endüstriyel | ✅ K/I arketipi: "a faceted hard shell, the front pane flat, two narrow side panes angled back, all inside one visible dark rim" |
| Dar pencere | izole, tehdit | ⛔ yüzü kapatır (D79) |

**Heybet telafisi (berrak vizör sabitken):**
```
· ÇERÇEVE KALINLIĞI   "a thick dark-grey rim" — ince çerçeve kubbeye kayar
· YAKA DERİNLİĞİ      "the helmet seated deep into a raised collar ring"
· OMUZ HATTI          "broad padded shoulder caps rising to the collar"
· MAT SERT DOKU       kabuk "matte", asla "glossy"
· SAYILI LAMBA        "two small square lamps set into the brow" (DONANIM §7:
                      orta risk — sayı kilitlenir)
```

**Kask içi ışık — üç düzenek (T17.2 #14 · fiziksel olarak sahte, D79 gereği
bilinçli):**

| Düzenek | Yön | Sıcaklık | Okuma | İngilizce kalıp |
|---|---|---|---|---|
| Çene çift kaynak | alttan yukarı | sıcak (~3200K) | klostrofobik, dramatik, yüz okunur | `a soft warm 3200K fill from inside the chin of the helmet on her face, the face fully readable through the clear pane` |
| Çerçeve halka difüzör | önden, homojen | nötr (~4500K) | gölgesiz netlik, göz pırıltısı | `a soft neutral 4500K fill from inside the visor rim on her face, even and shadowless, a small catchlight in each eye` |
| Yanak soğuk ışık | çapraz yandan | soğuk camgöbeği (~5600K) | kask içi gösterge illüzyonu (metinsiz) | `a faint cool 5600K cyan cast on her cheeks from inside the helmet` |

```
□ ⛔ "glow" / "glowing" YAZILMAZ — D29 bloom yasağı, `prompt_kontrol.py`
  YASAK sözlüğünde. Kask içi ışık "fill", "cast", "lamp light" ile yazılır.
  (⬜ DONANIM §3/§5'teki "glowing" kalıpları aynı betiğe takılır — kart G işi.)
□ Kask içi ışık SUBJECT bloğuna yazılır, LIGHTING bloğundaki tek ana
  ışıktan ZAYIF ("soft", "faint") — ortam ışığını bastırırsa "sahte"
  okunur (§3 son satır) ve gece sahnesinde yüzü fener gibi yakar.
□ ⛔ "glowing display / HUD / readout" YAZILMAZ — metin yasağı; yalnız
  renkli ışık soyutlaması ("a faint cyan cast on the cheeks").
□ REFERANS_PAKETI §4.1 "kask içi lokal ışık" satırının gerekçesi budur;
  R1 vizör-ardı yüz CU karesi bu ışıkla üretilir.
□ Yansıma: D79 "zero reflection of the environment" korunur; kask içi ışık
  vizörde iç yansıma YAZMAZ.
```

---

# 5. 🧵 MALZEME SÖZLÜĞÜ — kamerada ne okunur, motorda ne tutar

Kaynak: T17.2 #6-9-10-15. Motor sütunu ⭐ öneri — Nano Banana Pro/2 ·
Veo 3.1 · Omni'de A/B ÖLÇÜLMEDİ (T17.8).

| İngilizce kelime | Kamerada okunma ölçeği | Motor güvenilirliği (⬜) | Oyun-görünümü riski | Kullanım notu |
|---|---|---|---|---|
| `textured multilayer nylon` / `matte ballistic nylon` | MCU'da doku, WS'de kütle | yüksek | çok düşük | E arketipi gövdesi; "creased at the elbows" ile kıvrım eklenir |
| `quilted padding` (dikey/yatay) | ECU-MCU'da dikiş çukuru, WS'de hacim | yüksek | düşük | I arketipi; "vertical quilted padding down the torso" |
| `ribbed technical textile` | MCU'da çizgi, WS'de düz renge çöker | orta | düşük | T arketipi; uzak lockoff'ta YAZMA (boşa karakter) |
| `brushed steel` / `dark bronze` (halkalar) | MCU'da çizgisel parıltı | yüksek | orta (parlama artarsa) | yalnız yaka/bilek halkası; "brushed", asla "polished/chrome" |
| `matte scuffed composite plate` | MCU-WS'de plaka hattı ve siluet | yüksek | ⚠️ YÜKSEK yalın yazılırsa | ⛔ KURAL 3: "matte" + "scuffed" + kumaş eklemle ("edged in worn rubber where it meets the fabric") — üçü birden |
| `anodized aluminium` | MCU'da satensi metalik | yüksek | orta | yalnız küçük parçada (toka, halka iç yüzü) |
| `worn distressed leather` | ECU-MCU'da mikro çatlak | yüksek | çok düşük | kayış/kabza; uzay giysisinde nadir |
| `satin finish fabric` | MCU'da sheen | orta | orta | ⬜ yalnız kabin içi yumuşak ışıkta; sert güneşte parıltı şeridi doku öldürür |
| `heavy segmented gloves` / `articulated knee joints` | MCU'da segment | yüksek | düşük | eklem sözlüğü: `bellows` (retro) · `ring bearing` (mekanik) · `overlapping segments` (modern) |

**Oyun-görünümü TETİKLEYİCİ kelimeler (yazılmaz):**
```
unreal engine render · hard composite shell (yalın, aşınmasız) · glowing
strips · light strips · torso screen · chest display · glossy finish ·
high-gloss · chrome · polished armor · sleek armor · neon
```
**GERİ ÇEKİCİ kelimeler (SUBJECT bloğunda, negatif çekirdeğin yanında):**
```
matte · scuffed edges · worn rubber · creased fabric · micro-fabric weave ·
even dusting of … grit · practical light · 35mm film grain (çekirdekte zaten)
```
⛔ "sweat and condensation inside visor" rapor 2'nin listesindeydi, depoda
YAZILMAZ — T11.5③ yüzü kapatan yoğuşma yasağı.

---

# 6. 🎨 RENK BLOĞU, ZEMİN KONTRASTI, POZLAMA

Kaynak: T17.2 #11-12-16. ⛔ Renk SAYISINA/ORANINA tavan yazılmadı (T12.1
kararı — "60-30-10" kılavuza oran olarak inmedi). Depo ilkesi BAĞ'dır:
aksan rengi kadrajda kaç yere bağlı, o sayı SPEC'e yazılır.

**Hiyerarşi (oran değil, sıra):** ANA renk gövde+bacak kütlesi · İKİNCİL
renk eklem/kol · AKSAN tek yüksek doygunluklu renk, tek yerde.

**Aksanın yeri:** üst gövde merkezi (yaka altı, üst göğüs, omuz birleşimi)
— bakışı kaska çeker. Ekstremite ucunda (eldiven, bot) siluet parçalanır.
TUR 5 rol şeridi (kol/uyluk, 360° sarılı) ile çakışmaz: **ROL şeridi
uzuvda, AKSAN üst gövdede.** Tek karakterli filmde ikisi tek renkte
birleşebilir (YERÇEKİMİ ORANGE emsali).

**Zemin → giysi değeri (ORTAM KARTI ile eşle — KILAVUZ_REHBERI §3):**

| Zemin | Sorun | Giysi ana değeri | Aksan | Kalıp |
|---|---|---|---|---|
| Siyah uzay / koyu istasyon dışı | koyu giysi fonda erir | mat kemik beyazı · fırtına grisi | turuncu / sarı | `matte bone-white multilayer nylon` |
| Kızıl-turuncu toprak (Mars) | zeminle aynı ton kaybolur | arduvaz grisi · koyu lacivert | güvenlik turuncusu (tek yer) | `slate-grey ribbed textile … a single band of safety-orange textile` |
| Beyaz buz / kar | açık giysi patlar | grafit · koyu bordo | soğuk mavi | `matte graphite composite … deep maroon quilted panels` |
| Gri metal iç mekân | nötr ton, ayrışmaz | orta-koyu gövde | tuğla kırmızısı · yanık turuncu | `dark slate suit, a brick-red textile band across the upper chest` |

**Renk = malzeme + renk adı** (ZATEN VAR, T12.3): "orange" değil `safety-
orange textile`, "grey" değil `slate-grey ribbed textile`. Çıplak renk adı
zemine sızar; bileşik ad yüzeye bağlanır (⬜ mekanizma, T17.2 #16).

**Pozlama kelimeleri (SUBJECT bloğuna, LIGHTING'e değil):**
```
beyaz giysi sert güneşte patlıyor  → "off-white bone fabric" (saf "white" yazma)
koyu giysi siyah fonda eriyor      → "textured matte charcoal finish" +
                                     LIGHTING'de "a thin rim light separating
                                     the shoulders from the black"
```
⛔ Renk adı tuzağı [REHBER §7 · HEAVY SIDE vakası]: "oxblood" gibi yasak
kelime içeren renk adı yazılmaz; "deep maroon" yazılır.

---

# 7. 🧹 KİR VE YIPRANMA — global bitiş, konumlu leke değil

Kaynak: T17.0 ③ (2↔3 çelişkisinin çözümü) · T17.2 #13 · D42.

```
Rapor 2: temiz giysi "steril, oyuncak, tiyatro kostümü" okunur; yıpranma
         fotogerçekçiliğe çeker.
Rapor 3: kir/leke DAĞILIMI klipler arasında İLK kayan öğe, bütçeden ilk
         atılan katman.
ÇÖZÜM:   kir GLOBAL BİTİŞ olarak yazılır, KONUMLU LEKE olarak yazılmaz.
```

| Yazılır (global) | Yazılmaz (konumlu) |
|---|---|
| `the whole suit carries an even matte dusting of grey grit` | `a dark oil stain on the left thigh` |
| `scuffed edges at the wrist rings and shoulder caps` | `three scratches across the chest plate` |
| `the fabric creased at the elbows and hips` | `mud caked on the right boot` |

```
□ Kir bölge haritası (yüksek: bot tabanı · bilek · diz · dirsek · manşet ·
  yaka içi / orta: dikiş, eklem / düşük: sırt ortası, üst göğüs) yalnız
  REFERANS PANELİNDE kilitlenir — görselde tutulur, prompta inmez (T12.3
  dokunsal → görsel).
□ Kir KİMLİK bilgisi taşıyacaksa (merdiven: temiz → tozlu → aşınmış) bu
  bir DURUM DEĞİŞİMİDİR: klibe değil SINIRA yazılır (SAHNE_ZINCIRI §1),
  kademe sayısı SPEC'e (THE SCOURED GLASS KİLİT 4 emsali).
□ Yıpranma yeri göç etmez [D42]; global yazım bunu kendiliğinden sağlar.
□ ⛔ "Prometheus/2001 tipi bilinçli steril" seçim de meşrudur: o zaman
  "clean" YAZILMAZ, kir cümlesi ATLANIR (yokluk yazılmaz).
```

---

# 8. 🎒 SIRT — üç tarif biçimi, ⬜ hipotez, ilk filmde sınanır

Kaynak: T17.0 ④ · D79 · D139 · T17.2 #22. **Karar değişmedi:** sırt her
sahnede tek, kapalı, aynı yüzeydir ve kamera arkaya geçtiğinde POZİTİF
yazılır (D139). Değişen, pozitif cümlenin ne dediği.

| Biçim | Örnek | Deponun kanıtı | Sorun |
|---|---|---|---|
| Yokluk | "no backpack, no tank, no hose" | D139: 6 sahnenin 5'inde tuttu, kamera arkaya geçince düştü | boş sırtı model DOLDURUR; pozitif tarifin içinde yasak-liste tuzağı |
| Düz pozitif | "one continuous smooth panel from collar to hip, carrying nothing" | THE HARD DOCK bible (üretilmedi) | tutar ama hacmi öldürür — "kumaş levha" |
| **Heykelsi pozitif** ⬜ | "one continuous sculpted surface from collar to hip, low-profile, with two shallow recessed panels, closed and smooth" | HİPOTEZ — rapor 3'ün §3'ü "ölçüldü", §8'i "ölçülmedi" diyor (T17.0 ④) | ilk filmde R1 ARKA paneli + ② ile sınanır |

```
KALIP (E · T arketipi):
  the back of the suit is one continuous sculpted surface from collar to
  hip, low-profile, with two shallow recessed panels, closed and smooth
KALIP (I · K arketipi):
  the back is one continuous ribbed surface from collar to hip, closed and
  smooth, the two shoulder caps wrapping over its upper edge
⚙️ İki kalıp da `prompt_kontrol.py` SIRT_POZITIF desenine ("one continuous …
   surface") uyar — kamera arkaya geçen sahnede ⑮ kapısı bunu arar [D139].
   "shell" yerine "surface" bu yüzden; kelime değiştirilirse kapı düşer.
```
```
□ Negatif kelime YOK ("no hose" çıkarıldı — §0⑥). Yokluk NEGATIVE bible +
  D79 zorunlu bloğunda zaten duruyor; SUBJECT yalnız var olanı yazar.
□ "two shallow recessed panels" SAYILABİLİR çapadır: ① mercek sayar,
  ② mercek sahneler arası karşılaştırır. Panel sayısı ikiden fazla yazılmaz
  (T17.2 #19: panel sayısı orta-sıra kayan öğe).
□ DONANIM §4 sırt A/B/C (itki çerçevesi / yuvarlak modül / DÜMDÜZ) kimlik
  ayrımı içindir; bu kılavuzun kalıbı "C DÜMDÜZ"ün heykelsi hâlidir.
  İki karakterli filmde A/B için DONANIM §4 kalıbı kullanılır, üçüncü
  karakterde bu kalıp.
□ ⛔ İLK FİLMDE A/B YAPILMADAN "TUTTU" DENMEZ: aynı sahne düz pozitif ve
  heykelsi pozitifle iki kez üretilir, ② skoru ve arka-açı klibi karşılaştırılır.
```

---

# 9. 📉 SÜRÜKLENME SIRASI, KISALTMA SIRASI, BÜTÇE YÖNÜ

Kaynak: T17.2 #17-19-20-21. Sayılar İNMEDİ; sıra ⬜ HİPOTEZ, deponun
kendi vakalarıyla desteklenir.

**Sürüklenme sırası (önce kayan → en son kayan):**

| Sıra | Giysi öğesi | Depo vakası | Önleyen tarif biçimi |
|:--:|---|---|---|
| 1 | kir / leke DAĞILIMI | D42 (yıpranma göç etti) | global bitiş (§7) |
| 2 | küçük aksesuar (toka, rozet, küçük yama) | D58 (eşya kayboldu) · DONANIM §7 orta/yüksek | büyük + sayılı; küçük yama yazılmaz |
| 3 | şerit KONUMU (sol/sağ, kol/uyluk) | TUR 5 asimetri ↔ rapor 3 sızma (T17.0 ⑥ AÇIK) | 360° sarılı BÜYÜK bant; R1 3/4 ve arka karesinde görünür |
| 4 | eldiven / bilek detayı | — | "one piece with the sleeve at the wrist" |
| 5 | panel sayısı, dikiş | — | ≤2 panel, sayı yazılır |
| 6 | sırt yüzeyi | D79 · D139 | §8 kalıbı |
| 7 | ana renk tonu ve siluet (EN SON) | — | malzeme + renk adı; siluet asla kısaltılmaz |

**Kısaltma sırası (blok banda sığmıyorsa):**
```
1. kir/yıpranma cümlesi           → atılır (referans paneli taşır)
2. mikro aksesuar, toka, sayılar  → atılır (zaten yazılmamalı)
3. malzeme dokusu kelimeleri      → kısalır ("textured multilayer" → "matte")
   — doku REFERANS PANELİNDE kilitlidir (T12.3), metinden çıkabilir
4. ikincil renk / ikincil şerit   → atılır (ana renk + tek aksan kalır)
5. SİLÜET (kabuk · pane · çerçeve · yaka halkası · sırt) → ASLA
⛔ Cümle KISALTILMAZ, katman ATILIR — kelimesi kelimesine kural
   (SAHNE_DEVAMLILIK §2.1) katmanı değil cümleyi korur.
```

**Bütçe:** karakter bloğu VIDEO/IMAGE bandının içinden pay alır; band
KILAVUZ_REHBERI §7'dedir, buraya yazılmaz. Blok yazıldıktan sonra
`prompt_kontrol.py` (Kart P) ölçer; sığmıyorsa yukarıdaki sıra.

**Bütçenin yönü (⬜ çıkarım, T17.0 ⑤):** izleyici kesimde kostüm
değişimini çoğunlukla fark etmiyor (değişim körlüğü — ÖLÇÜLMÜŞ);
devamlılığı mercek yakalıyor, izleyici değil. Giysi bütçesinin devamlılık
için harcanan payı TASARIMA kaydırılabilir — mercek yine yakalar.
Bu bir ölçüm değil çıkarımdır; kural değil yön.

**⬜ Kapı adayı (TODO):** rapor 3 "Lost in the Middle"ı (dil modeli
ölçümü) prompt kodlayıcısına taşıdı — V2 iskeletinde SUBJECT bloğu
ORTADADIR (SCENE → ENVIRONMENT → SUBJECT → CAMERA …). Ölçülmeden iskelet
değişmez; ilk filmde aynı sahne SUBJECT önde/ortada iki kez üretilip ②
karşılaştırılabilir.

---

# 10. 🖼️ REFERANS PANELİ İLE METNİN İŞ BÖLÜMÜ — kostüm için

Kaynak: T17.2 #18-23-24 · genel ilke TUR 12 (T12.3) — burada yalnız
KOSTÜME uygulanır, ilke yeniden yazılmaz.

| Bilgi | Nerede kilitlenir | Kostüm örneği |
|---|---|---|
| biçim / kesim hattı / plaka geometrisi | GÖRSEL (R1) + metinde tek cümle | kompozit göğüs plakasının kavisi |
| malzeme dokusu, kumaş sıklığı, kıvrım | GÖRSEL | nervür sıklığı, naylon dokusu |
| kir DAĞILIMI | GÖRSEL | bilek/diz yoğunluğu (§7) |
| SAYI (panel, lamba, halka adedi) | METİN | "two shallow recessed panels" |
| KONUM (sol/sağ, üst göğüs) | METİN | rol şeridi tarafı, aksan yeri |
| YOKLUK (hortum yok, metin yok) | METİN — NEGATIVE bible | D79 bloğu |
| kask içi ışık | İKİSİ: R1 vizör-ardı CU + SUBJECT cümlesi | §4 |

```
□ R1 sayfası (REFERANS_PAKETI §4.1): ön · 3/4 · profil · ARKA · (kask makro)
  · (vizör ardı yüz CU). Bu kılavuzun eklediği şey YOK; ARKA karesi §8'in,
  vizör-ardı CU §4'ün sınav yeridir.
□ ⚠️ REFERANS IŞIĞI ↔ SAHNE IŞIĞI (T17.2 #23 ⬜): R1 nötr ışıkta üretilir
  (T12.3 kimlik varlığı kuralı). Filmin ana ışığı SERT tek güneşse (vakum,
  Mars) kostüm parlaklık haritası sahneye taşınabilir → R1'e ek olarak
  "sahne ışığında tek kare" üretilir ve KOŞULLU görünüm olarak sayfaya
  girer; panel kanonunu değiştirmez.
□ ⚠️ REFERANS POZU ↔ SAHNE POZU: R1 ayakta; sahnede çömelme/eğilme varsa
  eklem dokusu yırtılabilir → o sahne ÜRETİM SIRASI'nda erkene alınır.
□ İKİ FİGÜR: aynı giysili iki karakterde ayırıcı fark öteki figüre
  SIZABİLİR (kavram sızması — ÖLÇÜLMÜŞ olgu, oran yok). Çözüm motor içi
  (erişilemez). Depo çözümü: fark BÜYÜK (360° bant, sırt A/B/C), R1'de
  iki figür AYRI karede (REFERANS_PAKETI §4.2 ③), IKI_KISI_VE_AYRILIK
  kartı. TUR 5 asimetri kararı SÜRER; küçük asimetrik yama YAZILMAZ.
□ Kostüm kitabı zorunlu alanları (T17.2 #18) RK kaydına iki satır olarak
  önerilir: "kir düzeyi (global)" · "eklem durumu (halka/körük/segment)".
  ⬜ REFERANS_PAKETI §2 tablosuna girmesi kart G işi.
```

---

# 11. 📝 BIBLE'A İNDİRME REÇETESİ — yedi adım, üç örnek

```
1. ARKETİP seç — §2 tablosu (E varsayılan; ton → satır)
2. KASK yaz — §4: kabuk + düz pane + görünür çerçeve + yaka halkası +
   kask içi ışık (bir düzenek)
3. GÖVDE yaz — §5: ana kumaş (malzeme + renk) + varsa plaka (mat · aşınmış ·
   tekstil eklem) + eklem tipi + eldiven/bot
4. SIRT yaz — §8 kalıbı (heykelsi pozitif, negatif kelimesiz)
5. RENK bağla — §6: ORTAM KARTINA göre ana değer; tek aksan üst gövdede;
   iki karakterde TUR 5 rol şeridi (uzuvda)
6. KİR yaz — §7 global bitiş (ya da bilinçli steril: cümle atlanır)
7. KİMLİK ekle — DONANIM §9 reçetesi (şerit · sırt A/B/C · bilek · eşya)
   → tek İngilizce blok → prompt_kontrol (Kart P) → sığmıyorsa §9 sırası
   → D79 zorunlu bloğu AYRI (NEGATIVE) — SUBJECT'e karışmaz
```

**Örnek A — E BELGESEL (deponun beyaz giysisi, doldurulmuş) ⭐ ilk seçim:**
```
She wears an off-white pressure suit of textured multilayer nylon, the
fabric creased at the elbows and hips, a visible brushed-steel neck ring
where the helmet locks to the raised collar and matching steel rings at
both wrists, heavy segmented dark-grey gloves one piece with the sleeves;
the helmet is a hard off-white shell with a single flat front pane set
inside a thick dark-grey rim, a soft warm 3200K fill from inside the chin
of the helmet on her face, her face fully readable through the clear
pane; the back of the suit is one continuous sculpted surface from collar
to hip, low-profile, with two shallow recessed panels, closed and smooth;
the whole suit carries an even matte dusting of grey grit and
scuffed edges at the wrist rings.
```
Kısaltma sırası: dusting/scuffed → "textured multilayer / creased" →
bilek halkaları (yaka halkası kalır) → SİLÜET asla.

**Örnek B — I ENDÜSTRİYEL:**
```
He wears a heavy industrial pressure suit of muted mustard-yellow canvas
with vertical quilted padding down the torso and thighs, broad padded
shoulder caps rising to the collar, dark bronze joint rings at the elbows
and knees, heavy segmented dark-grey gloves and boots; the helmet is a
rounded hard shell seated deep into a wide bronze collar ring, two small
square lamps set into the brow, a single flat front pane inside a thick
dark rim, a soft neutral 4500K fill from inside the rim on his face, even
and shadowless; the back is one continuous ribbed surface from collar to
hip, closed and smooth, the two shoulder caps wrapping over its upper edge; the whole
suit carries an even matte dusting of grey grit and worn edges at the
shoulder caps.
```
Kısaltma sırası: dusting/worn → lamba sayısı (ya hiç ya "two") → "vertical
quilted" → "muted" → SİLÜET (omuz kapağı · bronz yaka · sırt) asla.

**Örnek C — T TEKNOKRATİK FORM-FİT (Mars zemini):**
```
She wears a close-fitting technical pressure suit of slate-grey ribbed
textile with a matte scuffed composite chest plate and matching shoulder
plates, the plates edged in worn dark-grey rubber where they meet the
fabric, a visible brushed-steel neck ring, slim dark gloves one piece with
the sleeves; the helmet is a low hard shell with a single flat front pane
set inside a thick dark rim, a soft neutral 4500K fill from inside the rim
on her face, fully readable through the clear pane; the back of the suit
is one continuous sculpted surface from collar to hip, low-profile, with
two shallow recessed panels, closed and smooth; a single band of safety-orange textile
wraps the upper chest just below the neck ring.
```
Kısaltma sırası: (kir yok — bilinçli) → "ribbed" (uzak lockoff'ta zaten
çöker) → "worn dark-grey rubber" ("edged in rubber" kalır — KURAL 3
bozulmaz) → SİLÜET + aksan asla.

```
□ Üç blokta da: negatif kelime yok · "seamless/bubble/dome" yok · metin yok
  · "glow" yok (D29) · sırt cümlesi SIRT_POZITIF desenine uyar · Kelvin var
  (depo pratiği) · sayı yalnız sayılabilir öğede ("two")
□ D79 zorunlu bloğu ("The suit has NO back-mounted unit …") NEGATIVE
  bible'da AYRI durur — bu bloklar onun yerine geçmez, yanında durur.
□ Blok uzunluğu prompt_kontrol ile ölçülür; band KILAVUZ_REHBERI §7.
□ İki karakterli filmde A ve B AYNI arketip; ayrım TUR 5 (şerit rengi +
  tarafı · sırt A/B/C · bilek) ile; DONANIM §9 örneği bu blokların üstüne
  bindirilir.
```

---

# 12. 🔍 ÖLÇÜM — devamlılık ≠ tasarım sadakati (⬜ mercek adayı ⑭)

Kaynak: T17.2 #25. Gerçek benchmark'lar (VBench/VBench++ · GenEval ·
ViStoryBench) "tutarlılık" ile "estetik/görsel kalite"yi AYRI eksende
puanlar. Depoda ② DEVAMLILIK "aynı kaldı mı" ölçer; "tasarlandığı gibi
mi" ve "sinematik okunuyor mu" ölçen mercek YOK — sahibin gözü ilk
ölçümdü.

```
⬜ ⑭ TASARIM SADAKATİ merceği (QA mercek serisi — ⑬ UYUM'dan sonraki numara;
   prompt_kontrol kapı serisi ㉑㉒ DEĞİL · kart G işi — bu turda YAZILMADI):
   · girdi: R1 sayfası + üretilmiş klip
   · sorular: siluet R1 ile örtüşüyor mu (gölge testi §3) · kask
     çerçevesi görünür mü · sırt §8 kalıbıyla aynı mı · sert kabuk
     oyun-görünümü verdi mi (§5 tetikleyici listesi) · aksan tek yerde mi
   · çıktı: ② skorundan AYRI satır; ①/② ile toplanmaz
   · kapı: ⬜ betik yok — göz + kontrol listesi
⛔ Bu mercek yazılana kadar "havalı oldu" cümlesi T tablosuna girmez;
   yalnız sahibin kararı olarak film dosyasına yazılır.
```

---

# 13. 🔗 ÇAPRAZ REFERANSLAR

```
ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU   kimlik katmanı (şerit · amblem · bilek · eşya ·
                                      sırt A/B/C) — bu kılavuzla TEK bloğa iner (§11 adım 7)
SAHNE_DEVAMLILIK_KILAVUZU §2.1        kelimesi kelimesine kural — katman atılır, cümle kısalmaz
REFERANS_PAKETI_KILAVUZU §2 · §4.1    RK kaydı · sayfa kanonu · kask içi lokal ışık (gerekçe §4)
KILAVUZ_REHBERI §3 · §5 · §7          ortam kartı (renk §6) · negatif çekirdek · uzunluk bandı +
                                      yasak listesi tuzağı
IKI_KISI_VE_AYRILIK_KILAVUZU          iki figür (kavram sızması §10)
SAHNE_ZINCIRI_VE_SINIR_KILAVUZU §1    kir merdiveni durum değişimi = sınıra (§7)
MESHUR_SAHNE_KALIPLARI §4             kopya sınırı (§0⑧ · 04 §T17.3)
POLITIKA_VE_URETILEBILIRLIK §2 · §6   kelime sözlüğü · motor listesi
04_ARASTIRMA_BULGULARI §TUR 17        bu kılavuzun kaynak ve süzme kaydı
```
