# 🌍 DÜNYA GÖRÜNÜŞÜ KILAVUZU — World Bible'ın Yazım Kılavuzu

> **Ne zaman okunur:** Yeni film yazılırken, **World Bible yazılmadan
> ÖNCE**, ortam kartı (`KILAVUZ_REHBERI` §3) seçildikten SONRA. Kadrajda
> gökyüzü, ufuk ya da gezegen yüzeyi görünen her filmde zorunlu; yalnız iç
> hacimde geçen filmde pencereden görünen parça için okunur.
> **İş bölümü:** ortam kartı dünyanın **fiziğini** (toz, gölge kenarı, dolgu,
> ses, rüzgâr) kilitler; bu kılavuz dünyanın **görünüşünü** (gökyüzü
> gradyanı · tek gök cismi · ufuk · üç katman arazi · atmosferik perspektif
> kararı · film boyu sabitlik) yazar. Güneşin yönü ve ışık takvimi
> `ISIK_SENARYOSU_KILAVUZU.md`'de; burada yalnız "hangi yanda" satırı var.
> **Ne işe yarar:** "flat black sky" boşluğunu doldurur. Depoda en sık yazılan
> görsel özne (sky · horizon · terrain) tek sıfatla yazılıyordu; bu kılavuz
> onu deponun grameriyle (D48 biyom sabit · D145 ufuk kilidi · D176 zemin tek
> cümle · D138 sayı yok · yasak listesi tuzağı yok) yazılabilir hâle getirir.
> **Kaynak:** TUR 18 dış araştırması (12.09.2026) —
> `URETIM_ONCESI_ANALIZ/04_ARASTIRMA_BULGULARI.md` §TUR 18 (T18.2 #1-9 ·
> T18.3). Ham: `URETIM_ONCESI_ANALIZ/TUR18_HAM_RAPORLAR/TUR18_1_…`. Kural
> buradan okunur, bulgunun nereden geldiği oradan.
>
> ⚠️ **DÜRÜST SINIR:** raporun kaynak listesi gelmedi; eşik ve yüzde katmanı
> çürük çıktı (T18.4). Bu kılavuz **sayısız** yazıldı — "yüzde", "derece",
> "metre" satırı yoktur; ölçek gövdeyle ve sözle yazılır. Hiçbir arketip
> henüz depoda bu kılavuzla üretilmedi; ilk uygulamada ① KARE · ⑤ ARKA PLAN ·
> ② DEVAMLILIK skorları sınavdır (§7).

---

# 0. ⛔ DEĞİŞMEYEN KARARLAR — bu kılavuz TARİF BİÇİMİNİ yazar, fiziği değil

```
① ORTAM KARTI FİZİĞİ DEĞİŞMEZ [KILAVUZ_REHBERI §3]. Toz, gölge kenarı,
   dolgu, ses, rüzgâr satırları karttan gelir; bu kılavuz onların
   GÖRÜNÜŞÜNÜ yazar (§3 perspektif tablosu kartın fonksiyonudur).
② BİYOM SAHNELER ARASINDA DEĞİŞMEZ [D48]. Her promptun ENVIRONMENT
   bloğunun İLK cümlesi biyom cümlesidir ve film boyunca aynıdır.
③ ALÇAK AÇIDA UFUK KİLİDİ [D145]. Her dış mekân promptu en büyük arka
   plan nesnesini ADLANDIRIR ve ufkun kadrajdaki yerini yazar.
④ GÜNEŞ FİLM BOYUNCA EKRANIN BİR YANINDA, GERİ DÖNMEZ [D201 · D47 ·
   ISIK_SENARYOSU §2]. Bu kılavuz yalnız "hangi yanda" satırını taşır.
⑤ ZEMİN TEK CÜMLEDE TEK RENK [D176]. Kontrast garantisi ÖZNEYİ tarif
   eder, zemini ikinci kez tarif etmez.
⑥ DERECE, METRE, YÜZDE PROMPT GÖVDESİNE YAZILMAZ [D138]. Ölçek gövdeyle
   ve sözle: "fist-sized" · "ankle-high" · "a third of the way up the
   frame" [UZAY_USSU §1 usulü].
⑦ YASAK LİSTESİ TUZAĞI [REHBER §7]: "no haze", "no stars", "no
   vegetation" ENVIRONMENT bloğuna YAZILMAZ — sınıflandırıcı kelimeyi
   okur. Yokluk NEGATIVE bloğundadır; ENVIRONMENT yalnız VAR OLANI yazar
   ("a flat black sky" vardır; "no stars" yoktur).
⑧ GÖKYÜZÜNDE YAZI, HUD, GERÇEK DÜNYA COĞRAFYASI ADI YOK [D34 · D45 ·
   POLİTİKA §2].
⑨ KOPYA SINIRI [MESHUR_SAHNE §4]: film adı prompta girmez; arketipler
   film adsızdır, eşleme yalnız 04 §T18.3'te durur.
⑩ PUS KARTLARINDA NEGATİF ÇEKİRDEK DEĞİŞMEZ: "no dreamy haze" satırı
   BLOOM'u yasaklar [D41: yumuşak ışık ≠ bloom]; ENVIRONMENT'a yazılan
   "a uniform amber haze" ORTAMDIR, post efekti değil. İkisi birlikte durur.
```

---

# 1. 🩺 NEDEN DÜZ GÖRÜNÜYOR — teşhis ve cevabı

**Depo teşhisi (ölç: `cat yatay_*/*/*.md dikey_shorts_filmler/*/*.md |
grep -ohiE "[a-z-]+ [a-z-]+ sky\b" | sort | uniq -c | sort -rn`):** gökyüzü,
ufuk ve arazi deponun en sık görsel özneleri; en sık gökyüzü cümlesi tek
sıfat + isim ("flat black sky" · "pale x-beige sky"). Gök cismi sayısı ve
konumu, ufuk yüksekliği, arazi katmanı, perspektif kararı çoğu bible'da
YOK. Gözlem defteri kapısız beş aday biriktirdi: gök cismi değişimi
(ADAY-31) · topoloji ve atmosfer sıçraması (32) · karton paralaks (50) ·
kar → çöl (70) · atmosferik perspektif tersi (71). Dersler D6 · D48 · D145
aynı yere vuruyor.

**Cevap (T18.0 ①):** "flat black sky" yanlış değil, EKSİK. Vakumda gökyüzü
gerçekten düz siyahtır; düz görünen şey gökyüzü değil, gök cismi, ufuk ve
arazi katmanı yazılmadığı için modelin boşluğu her klipte başka şeyle
doldurmasıdır. Çözüm çok öğe değil, **az öğe, her öğe somut**:

```
KURAL 1 — DÖRT CÜMLE, HER FİLMDE AYNI: gökyüzü gradyanı · TEK gök cismi
          (konumla) · ufuk (yükseklik + en büyük arka plan nesnesi) ·
          arazi ÜÇ KATMAN (yakın · orta · uzak). Dördü World Bible'da
          bir kez yazılır, ENVIRONMENT bloğuna kelimesi kelimesine iner.
KURAL 2 — PERSPEKTİF KARARI KARTTAN ÇIKAR: vakumda uzak sırt yakın taş
          kadar keskin; ince atmosferde yalnız çok uzakta solar; kalın
          atmosfer ve pusta orta plandan itibaren silüete çöker (§3).
KURAL 3 — SABİT KAMERADA DERİNLİK ÖRTÜŞMEYLE YAZILIR: paralaks yok
          (Cutting & Vishton 1995 — manzara alanında derinlik atmosferik
          perspektif + ufuk yüksekliği + örtüşmeden okunur). Bir yakın
          öğe bir uzak öğenin ÖNÜNDEN geçer; cümle bunu söyler.
```

---

# 2. 🌍 ALTI ARKETİP — film adsız, ortam kartına bağlı

Kaynak: T18.2 #1 · T18.3. Ortam kartı sütunu bu kılavuzun kapısıdır: kartı
olmayan arketip (K · B) yalnız KAYIT'tır, kart açılmadan yazılmaz.

| Kod | Arketip | Gökyüzü | Gök cismi (TEK) | Ufuk · arazi üç katman | Perspektif | Hikâye tonu | Ortam kartı · depo uyumu |
|:--:|---|---|---|---|---|---|---|
| **V** | VAKUM SİYAHI | düz siyah, gradyansız | bir büyük soluk gezegen diski YA DA hiç (güneş kadraj dışı) | alçak keskin ufuk; yakın sivri taş · orta ince gri toz · uzak krater sırtı | YOK — uzak sırt yakın taş kadar keskin | tecrit, sessizlik, tehdit | §3.1 · §3.5 · §3.7 · §3.8 ✅ **ilk seçim** (depo çoğunluğu) |
| **İ** | İNCE TOZ DÜZLÜĞÜ | tereyağı sarısından ufukta soluk somona; gün batımında güneşin çevresi mavi (kart) | bir küçük soluk güneş | düz orta yükseklikte ufuk; yakın yumruk boyu koyu taş · orta pas rengi ince toz · uzak alçak sırt hafif solmuş | HAFİF — yalnız çok uzak sırt zeminden bir ton açık | keşif, hayatta kalma, yalnızlık | §3.2 ✅ |
| **P** | MONOKROM PUS | tek renk pus zeminden göğe (amber · okra · kül); gradyan yok | güneş yalnız parlak bir leke YA DA hiç | ufuk gizli; yakın yuvarlak çakıl/kırağı · orta düz silüet · uzak pusa erimiş | AŞIRI — orta plandan itibaren silüet | boğulma, yön kaybı, kadim çürüme | §3.9 kriyojenik (amber, N₂+CH₄) · §3.6 bulut bandı (ufuk/zemin YOK — yalnız gök yarısı) ✅ |
| **F** | FIRTINALI KAYALIK | koyu arduvazdan kül grisine; alçak bulut tabanı | hiç (bulut) | yüksek karanlık ufuk; yakın ıslak siyah bazalt · orta sivri kayalık · uzak sisli geçit | YÜKSEK — orta plandan yumuşar | dehşet, bilinmeyen, klostrofobi | §3.4 kalın atmosfer ✅ koşullu — ⚠️ hareketli bulut on saniyede sürüklenir; bulut "low and still" yazılır |
| **K** | AĞARTILMIŞ KUM | ağartılmış krem-bej, tepede sert beyaz ışıkla yıkanmış | bir sert beyaz güneş, yüksekte | bükük alçak ufuk; yakın ince çakıl ve dalga izi · orta kum sırtı · uzak silik tepe | ORTA — ısı titreşimi ve toz saçılımı uzak tepeyi soldurur | ezici kuraklık, anıtsallık | §3.3 DÜNYA ATMOSFERİ ⏸️ rafta → yalnız KAYIT; kart açılırsa yazılır |
| **B** | BUZ VE SOĞUK GRİ | soluk camgöbeği-gri örtü, güneşsiz | hiç | dik katmanlı ufuk; yakın cam gibi buz çatlağı · orta sıkışmış kar · uzak donmuş bulut kütlesi | ORTA — uzak yapı soğuk maviye kayar | çaresizlik, donmuş zaman | kart yok — §3.4'ün soğuk varyantı olarak ⬜; kart açılmadan yazılmaz |

**Novum düzeyi gök cisimleri** (dev bükülmüş disk, halka arkı, ikinci güneş):
TEK gök cismi kuralının varyantıdır — biri yazılır, ikincisi yazılmaz. Halka:
"one luminous ring arch rising from the horizon on the right". Kural
ONERME_VE_NOVUM'a tabidir; bu kılavuz yalnız gök cisminin tek ve konumlu
olmasını ister.

**Seçim ölçütü (sırayla):**
```
1. Ortam kartı hangisi? → satır kendiliğinden çıkar (V · İ · P · F).
2. Hikâye tonu kartla çelişiyorsa TON DEĞİL KART kazanır; ton ışıkla ve
   ufuk yüksekliğiyle kurulur (alçak ufuk = yalnızlık, yüksek ufuk = baskı).
3. Gök cismi: filmde sayaç/zaman işlevi görecekse (yükselen disk =
   geçen zaman) SAHNE_ZINCIRI §1 durum değişimi kuralına bağlanır —
   değişim yalnız planlı sınırda.
```

---

# 3. 📐 "GERÇEK YER" DEĞİŞKENLERİ — ne yazınca fon levhası, ne yazınca yer

Kaynak: T18.2 #2-#5 (eşikler İNMEDİ, T18.4). Sayısız.

| Değişken | Gerçek yer okunur | Fon levhası / oyun haritası okunur | Nasıl yazılır |
|---|---|---|---|
| Atmosferik perspektif | kartın söylediği kadar: vakumda sıfır, pusta tam | vakumda pus, pusta keskin uzak plan; uzak planda saf siyah gölge (atmosferli dünyada) | §3 perspektif tablosu — ortam kartına göre TEK cümle |
| Derinlik ipucu (sabit kamera) | ÖRTÜŞME: yakın öğe uzak öğenin önünden geçer; ufuk yüksekliği kamera açısıyla uyumlu | katmanlar yan yana, hiçbiri ötekini kesmiyor; ufuk kamera yüksekliğine uymuyor | "a low ridge crossing in front of the far crater wall" · ufuk satırı (§4) |
| Arazi doku hiyerarşisi | yakın: gövde-göreli boyutlu taş; orta: çakıl/kum; uzak: yalnız ton | tüm planlarda aynı doku yoğunluğu; tekrar eden desen | üç katman kalıbı (§4) — her katman FARKLI isim ve boy |
| Tekrar eden doku | rastgele dağılım | ızgara gibi yinelenen kum/taş | "scattered" · "uneven" · tek bir büyük tekil taş çapa |
| Gök cismi ölçeği | tek, sabit boy, kadraja göre yazılmış | dev ay + küçük ay + yıldız alanı; her klipte başka boy | "one small pale sun" / "one large pale planet disc filling a hand's width of sky" |
| Ufuk yüksekliği | kamera açısıyla tutarlı; her sahnede planlı | alçak açıda ufuk kaybolur ve model duvar/kanyon doldurur [D145] | "the horizon a third of the way up the frame" + en büyük arka plan nesnesi |
| Zemin ↔ gök ışık bağı | gölge rengi gök rengidir (atmosferli); vakumda gölge siyah | gölge rengi gökten bağımsız | "the shadows tinted the colour of the sky" / "pure black shadows" |

**Perspektif = ortam kartının fonksiyonu:**
```
§3.1 · §3.5 · §3.7 · §3.8 VAKUM      "the far rim as sharp as the nearest rocks"
§3.2 İNCE ATMOSFER                  "the far ridge a shade paler than the ground before it"
§3.4 KALIN · F                      "the middle distance already softened, the far pass a flat grey silhouette"
§3.9 KRİYOJENİK PUS · P             "the ground beyond a few body-lengths dissolved into the haze"
§3.6 BULUT BANDI                    ufuk ve zemin YOK — yukarısı parlak kubbe, aşağısı okra uçurum (kart)
§3.10 İÇ HACİM                      bu kılavuz yalnız PENCEREDEN görünen parçayı yazar — pencere
                                    çerçevesi + dışarıdaki tek gök cismi; ARAC_VE_IC_HACIM §4
```

---

# 4. ✍️ KALIPLAR — dört cümle ve kelime listeleri

**Gökyüzü (gradyan, tek renk çifti):**
```
"a flat black sky"                                        V
"a pale butterscotch sky fading to salmon at the horizon" İ
"a uniform amber haze filling the sky from the ground up" P
"a dark slate sky under a low, still cloud deck"          F
```
**Gök cismi (TEK, konum EKRAN-uzayında — UZAMSAL §4.4 sözlüğü):**
```
"one small pale sun low on the right"
"one large pale planet disc fixed high on the left, its lit edge facing the sun"
"one luminous ring arch rising from the horizon on the right"
⛔ "moons" · "twin suns" · "a sky full of stars" (güneşliyken) · "nebula" · "aurora"
```
**Ufuk (yükseklik + en büyük arka plan nesnesi [D145]):**
```
"the horizon a third of the way up the frame, a low crater rim running across it"
"the horizon high in the frame, a black ridge line closing the top third"
"the horizon hidden in haze; the nearest boulder is the largest thing in frame"
```
**Arazi üç katman (boy gövdeye göre; her katman farklı isim):**
```
YAKIN  "fist-sized dark rocks on fine grey dust"
ORTA   "a field of ankle-high rubble" · "ripple sand" · "wet black basalt slabs"
UZAK   "a low rim" · "soft pale dunes" · "a flat grey silhouette of a pass"
+ ÖRTÜŞME: "a low ridge crossing in front of the far crater wall"
```
**Işık bağı (ISIK_SENARYOSU §5 ile aynı hizada, burada tek cümle):**
```
"pure black shadows with hard edges"                      V
"soft-edged weak shadows tinted the colour of the sky"     İ · F
"shallow soft shadows filled from every side by the orange air"  P
```

**Tetikleyici kelimeler (yazılmaz — levha / oyun / stok render okutur):**
```
epic vista · alien landscape · sci-fi planet · otherworldly · dramatic sky ·
nebula · aurora · starfield (güneş varken) · twin moons · volumetric haze ·
mist rolling · god rays · lush · glowing crystals · matte painting
```
**Geri çekici kelimeler (ENVIRONMENT bloğunda):**
```
fine grey dust · fist-sized rocks · ripple sand · wet black basalt · a flat
black sky · one small pale sun · a low rim · as sharp as the nearest rocks ·
a shade paler · tinted the colour of the sky
```

---

# 5. 📋 WORLD BIBLE SATIRLARI — plan belgesinde ne durur

Kaynak: T18.2 #6-#7 (araç adları inmedi; kavramlar indi). PLAN'daki World
Bible altı satır taşır; ENVIRONMENT bloğu ilk dördünü kelimesi kelimesine alır.

```
BIOME        tek cümle, film boyunca aynı, ENVIRONMENT'ın İLK cümlesi [D48]
SKY          gradyan cümlesi (§4)
BODY         TEK gök cismi + ekran konumu; yoksa "none" (plana; prompta yazılmaz)
HORIZON      yükseklik + en büyük arka plan nesnesi [D145]
GROUND ×3    yakın · orta · uzak (§4); yakın taş boyu gövde-göreli
PERSPECTIVE  ortam kartına göre tek cümle (§3)
SUN SIDE     ekranın hangi yanı (ISIK_SENARYOSU §2'ye işaret; yön kilidi orada)
CHANGE       gök cismi/gökyüzü/biyom DEĞİŞİYORSA hangi sahne sınırında —
             SAHNE_ZINCIRI §1: durum değişimi klibe değil SINIRA yazılır;
             bilerek değiştirilen gökyüzü anlatı aracıdır (T18.2 #7),
             istemsiz değişim "sahte yer" okutur
```

⛔ Sky chart, biome map, matte painting bible gibi yapım belgeleri fiziksel
sette ayrı dosyalardır; depoda hepsi bu sekiz satırdır. Ayrı dosya AÇILMAZ.

---

# 6. 📉 SÜRÜKLENME SIRASI VE KISALTMA SIRASI (⬜ hipotez, sayısız)

Kaynak: T18.2 #8-#9 (rapor kendi hipotez dedi) + deponun aday defteri.

| Sıra | Dünya öğesi | Depo vakası | Önleyen tarif biçimi |
|:--:|---|---|---|
| 1 | gök cismi SAYISI ve KONUMU | ADAY-31 | "one … fixed high on the right" — TEK, konumlu |
| 2 | pus / sis yoğunluğu | ADAY-32 · ADAY-71 | perspektif cümlesi karttan; pus ya her yerde ya hiç |
| 3 | biyom ve doku hiyerarşisi | ADAY-70 · D48 | ilk cümle biyom; üç katman farklı isim |
| 4 | ufuk yüksekliği | D145 | ufuk satırı + en büyük arka plan nesnesi |
| 5 | gökyüzü rengi (EN SON) | — | gradyan cümlesi malzemesiz tek renk çifti |

**Kısaltma sırası (ENVIRONMENT banda sığmıyorsa):**
```
1. uzak katman cümlesi        → atılır (ufuk satırı uzak planı zaten taşır)
2. ışık bağı cümlesi          → LIGHTING bloğu taşır, buradan çıkar
3. orta katman                → kısalır ("a field of ankle-high rubble" → "rubble")
4. örtüşme cümlesi            → atılır (yalnız derinlik hissi kaybolur)
5. BİYOM · GÖKYÜZÜ · GÖK CİSMİ · YAKIN KATMAN · UFUK → ASLA
⛔ Cümle KISALTILMAZ, katman ATILIR — kelimesi kelimesine kural
   (SAHNE_DEVAMLILIK §2.1) katmanı değil cümleyi korur.
```

**⬜ A/B (ilk filmde):** aynı sahne, ENVIRONMENT'ta üç katman ↔ tek katman;
⑤ ARKA PLAN ve ② DEVAMLILIK karşılaştırılır. Rapor "sade tarif daha kararlı"
dedi (hipotez); TUR 17 "az ama büyük" dedi. İkisi aynı şeyse üç katman
"üç büyük öğe"dir, "otuz küçük öğe" değil.

---

# 7. 🔍 ÖLÇÜM — bu kılavuzun sınavı

```
⑤ ARKA PLAN merceği (özne-dışı alan, derin tarama) zaten var: gök cismi
   sayısı/konumu · biyom · ufuk yüksekliği klipten klibe okunur.
② DEVAMLILIK: dünya + gövde — gökyüzü rengi ve gök cismi değişimi buraya.
⬜ ⑭ TASARIM SADAKATİ merceğinin DÜNYA satırı (kart G, yazılmadı): R
   paneli ↔ klip: gök cismi tek mi · ufuk planlı yerde mi · uzak plan kartın
   dediği kadar keskin mi · yakın taş boyu gövdeye göre mi.
⬜ prompt_kontrol KAPI ADAYI: ENVIRONMENT bloğunda "sky" geçiyor ama gök
   cismi cümlesi ("one … sun/moon/disc") ya da "flat black" yoksa NOT;
   "moons" / "twin suns" / "starfield" varsa FIX. Kalibre edilmeden yazılmaz.
```

---

# 8. 📝 WORLD BIBLE'A İNDİRME REÇETESİ — altı adım, üç örnek

```
1. ORTAM KARTI seç (REHBERİ §3) → §2 satırı çıkar (V · İ · P · F)
2. BIOME cümlesi — tek, film boyu aynı, ENVIRONMENT'ın ilk cümlesi
3. SKY + BODY — gradyan + TEK gök cismi + ekran konumu (§4)
4. HORIZON — yükseklik + en büyük arka plan nesnesi
5. GROUND ×3 + ÖRTÜŞME — yakın (gövde-göreli boy) · orta · uzak
6. PERSPECTIVE + ışık bağı — karttan tek cümle; güneş yanı ISIK §2'den
   → PLAN'a sekiz satır (§5) → ENVIRONMENT bloğuna kelimesi kelimesine
   → prompt_kontrol (Kart P) → sığmıyorsa §6 sırası
   → yokluklar ("no stars" · "no haze" · "no vegetation") NEGATIVE bloğuna
```

**Örnek V — VAKUM (§3.1 · Ay yüzeyi) ⭐ ilk seçim:**
```
ENVIRONMENT:
A grey plain of fine dust under a flat black sky, fist-sized dark rocks
scattered near the camera thinning to bare dust farther out, a low
crater rim running across the frame a third of the way up with its edge
as sharp as the nearest rocks, a single boulder the height of her knee
standing in front of the rim on the left; one large pale planet disc
hangs fixed high on the right, its lit edge facing the sun on the left.
The shadows on the ground are pure black with hard edges.
```
Kısaltma sırası: uzak (rim keskinliği) → ışık bağı → orta → örtüşme (boulder)
→ BIOME/SKY/BODY/YAKIN/UFUK asla.

**Örnek İ — İNCE ATMOSFER (§3.2 · Mars):**
```
ENVIRONMENT:
A flat plain of fine rust-red dust under a pale butterscotch sky fading
to a dusty salmon band at the horizon, one small pale sun low on the
right; fist-sized dark basalt rocks near the camera, a field of
ankle-high rubble across the middle distance, and a low ridge on the far
left a shade paler than the ground in front of it. The shadows are
soft-edged and weak, tinted the colour of the sky.
```

**Örnek P — KRİYOJENİK PUS (§3.9):**
```
ENVIRONMENT:
A plain of dark rounded pebbles under a thin frost, a uniform amber haze
filling the sky from the ground up, the sun a brighter smear high on the
left; the middle distance already softened to a flat orange silhouette
and the ground beyond a few body-lengths dissolved into the haze, one
rounded boulder the height of his waist the largest thing in frame. The
shadows are shallow and soft, filled from every side by the orange air.
```
⚠️ NEGATIVE bloğunda "no dreamy haze" satırı KALIR (§0 ⑩): pus ortam,
bloom post efekt.

---

# 9. 🔗 ÇAPRAZ REFERANSLAR

```
KILAVUZ_REHBERI §3                    ortam kartları — fizik buradan, görünüş bu kılavuzdan
ISIK_SENARYOSU_KILAVUZU §2 · §5       güneş yönü kilidi · gölge cümlesi (ışık bağı burada tek satır)
UZAMSAL_HARITA §4.4 · §4.6            ekran-uzayı sözlüğü · ölçek kilidi (gök cismi konumu bu sözlükle)
UZAY_USSU §1 · §5                     ölçek birimi (gövde) · ölçek şahidi · maket etkisi
SAHNE_ZINCIRI §1                      gökyüzü/gök cismi değişimi = SINIRA yazılır
ARAC_VE_IC_HACIM §4                   iç hacimden pencere: bu kılavuz yalnız pencere dışını yazar
ONERME_VE_NOVUM                       novum düzeyi gök cismi (dev disk · halka) — tek cisim kuralı
IMAGE_VIDEO_PROMPT_TEMPLATES          ENVIRONMENT bloğunun yeri (V2 iskeleti)
DERSLER: D6 · D48 · D145 · D176       çevre morph · biyom sabit · ufuk kilidi · zemin tek cümle
04_ARASTIRMA_BULGULARI §TUR 18        bu kılavuzun kaynak ve süzme kaydı
```
