<!-- devamlilik (sonnet) F5 tur 1 G01 — cevabı AYNEN (alt ajan transkriptinden), 20.10.2026 -->

DEAD_LAST · PROMPTLAR/G01.md · devamlılık eleştirisi (Faz 5, tur 1, v2 biçimi)

## 8 soru tablosu (C01-C08)
Hücre: ✅ · ❌ (ilgili bulgu) · — (bu çekimde yok)

| Çekim | 1 işaret | 2 kimlik birebir | 3 ortak cümle | 4 açıklığın ardı | 5 akışkan | 6 ekran + kilit | 7 referans rolü | 8 ses · zıt istek |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| C01 | ❌ B9 | ❌ B14 | ✅ | ✅ | ❌ B12 | ✅ | ✅ | ✅ |
| C02 | — | ✅ | ✅ | ✅ | ✅ | ❌ B5 | ✅ | ❌ B5 |
| C03 | — | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ B2 | ✅ |
| C04 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ B1 | ❌ B6 |
| C05 | ❌ B8 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| C06 | ❌ B7 | ❌ B13 | ✅ | ✅ | ✅ | ✅ | ❌ B1 | ❌ B6 |
| C07 | — | ❌ B11 | ✅ | ✅ | ✅ | ✅ | ❌ B11 | ❌ B15 |
| C08 | ✅ | ❌ B11 | ✅ | ✅ | ✅ | ✅ | ✅ | ❌ B6 |

Q3 notu: ORTAK GÖRÜNÜM'ün 8/8 Görsel'de FILM.md:233 ile birebir olduğunu Grep ile sayarak doğruladım (8 eşleşme). ORTAK HAREKET 5/8 tam (C01 C04 C05 C06 C08) ve 3/8 kısaltılmış (C02 C03 C07). Kısaltma, F5_yazim_karari.md:73-76'ya uygun. ORTAK GÖRÜNÜM Video'larda yok (B20).

Q4: pencere ya da açıklık ardı 8/8'de yazılı (C01 gezegen · C04 römorkör + dock · C06 dock · C08 kökler). Açıklık arkası eksik çekim yok, bulgu yok.

Q6: yazı kilidi Görsel'lerde ORTAK GÖRÜNÜM'de (`no readable text, no logos or watermarks`). C01, C04 ve C06'da ayrıca ekran kilidi var.

Metin gövdesinde çekim ya da plan kodu taraması: 8 çekim bloğunda temiz. Kod yalnız `PANELLER` ve `KAYNAK` satırlarında geçiyor. Referans promptlarının gövdesi için B19'a bak.

Referans anahtarı: 8/8'de `Reference <No> (<rol>)` cümleleri EKLE sırası ve FILM §3 numarasıyla aynı. Rol sözlüğü tutarlı (8 hep "Needle intact", 15 "preparation dock", 16 "hanging-root sector").

---

### B1 · CİDDİ · Referans sayfaları tek açılı; çekimlerin istediği paneller yok
YER       G01:85-125 (ref 8, 9, 11, 12) · G01:197-217 (ref 20-22) · C03 G01:376 · C04 G01:399 · C06 G01:452
KANIT     ref 9: `Three-quarter elevated hangar view` · ref 11: `Three-quarter elevated hangar view` (ön mü arka mı yazılı değil). Aynı promptlar ise `Exactly two prominent rear outer speed engines` ve `Exactly three rear engines in a left-center-right row` istiyor. Hasar sayfası 21: `RIGHT rear outer engine is dark … Same reference angle and scale.` C03: `Close elevated rear-quarter view`. C04/C06: `Inside Needle's compact one-pilot canopy` ve `take the shape of the one-pilot canopy from it`.
ETKİ      Hasarın kendisi (arka motor) ön üç-çeyrek açıda görünmeyebilir. Needle'ın arka motorları, sırt beşiği ve kabin içi hiçbir panelde yok. C03, C04, C06 ve sonraki ~10 kokpit çekiminde kimlik boşta kalır.
DOĞDUĞU   metin (referans promptu)
KURAL     FILM.md:140-141 ÖZNE BAŞINA TEK SAYFA, açılar paneldir [SÖZLEŞME]. Plan R/V/M istemleri tek görünüştür; G01 not satırı bunu "panel kalıbı uygulanmadı" diye açıkça kabul ediyor.
ARIZA     T04 / T05
DÜZELTME  Sahibe sor (plan çatışması). Sayfa promptlarına şunlar eklenir:
          - 8: `Three-quarter view from slightly above` → `Two panels on one sheet: front three-quarter from slightly above, and rear three-quarter from slightly above showing the dorsal cradle and both rear engines`.
          - 9 ve 11: aynı iki panel.
          - 8: üçüncü panel olarak boş beşikli sırt (B2).
          - Kokpit içi için ayrı panel, ya da C04/C06 anahtarından "take the shape of the one-pilot canopy" çıkarılır.
          Yaparsan 20-22 `Same reference angle` cümlesi iki paneli kapsar.

### B2 · CİDDİ · C03: ref 8 hücreyi takılı gösteriyor, kare "beşik boş" diyor
YER       C03 Görsel G01:376 · ref 8 G01:88
KANIT     C03: `take … the dorsal latch cradle from it; the cradle is still empty in this frame` + `Exactly one cell`. Ref 8: `One detachable blue booster fuel cell is fixed lengthwise on the dorsal spine`.
ETKİ      Açılış karesinde hücre iki kez çıkabilir (elde + beşikte) ya da el hücre tutmaz. "Tek hücre" kare kapısı düşer, video "kilitleme" eylemini atlar.
DOĞDUĞU   metin + referans
KURAL     film_dogrula DERS Y2 / FILM.md:246 · AÇILIŞ ILK_30 §6 [SÖZLEŞME]
ARIZA     T09
DÜZELTME  Sayfaya boş beşikli panel ekle (B1). Metinde: `the cradle is still empty in this frame` → `the cradle is empty and holds no cell; the only cell is the one held above it`.

### B3 · CİDDİ · C03 (açılış): yükleyici elleri tasarımsız, temas gösteriliyor
YER       C03 Görsel G01:376 · Video G01:385 · FILM.md:331 (ILK_30 sapması listesinde yalnız C01 ve C02 var)
KANIT     `An alien loader's plain gloved hands hold one blue booster cell directly over the dorsal latch cradle` · Video: `lower the single blue cell into the existing dorsal cradle, lock it with one clear click and withdraw`.
ETKİ      Parmak sayısı ve eldiven yapısı hiçbir yerde yazılı değil ("no human cast" ile çelişen insan eli çıkabilir). Temas anı kadrajda. İlk 30 saniyede el kaynaşması ve fazla parmak "açılışta kullanılamaz" kapısına takılır.
DOĞDUĞU   metin (plan)
KURAL     BILINEN_TUZAKLAR §B satır 47 (sıra 1, en sık hata) · ILK_30 §6 :105 "karmaşık el-nesne teması" kaçınılır [HİPOTEZ]
ARIZA     T01
DÜZELTME  Plan metni olduğu için sahibe sor. En küçük değişiklik: Video `lock it with one clear click and withdraw` → `let it settle into the cradle, then withdraw`. Yedek: C03 açılıştan çıkarılıp C02 sonrası sabit yükleyici planıyla değiştirilir. FILM.md:331'e C03 sapması işlenir.

### B4 · CİDDİ · Işık cümlesi mekân başına birebir değil; "same …" atıfı
YER       C04 G01:399 · C06 G01:452 · C07 G01:479-481 · C08 G01:502-504
KANIT     C03 ve C05 (dock): `Hard violet space light with warm amber work lamps.` var. C04: `Dark controls without readable text, same pit light.` C06: `inside the same Needle cockpit. … Cool-blue light from the newly installed booster status reflection` (ana ışık yok). C07 ve C08 (kökler): ışık cümlesi hiç yok.
ETKİ      Aynı mekânın (M02) iki yüz çekimi başka ışıkla üretilir. "same pit light" ve "same Needle cockpit" modelin görmediği bir önceki çekime atıf; boş kalır. M03 yarısında (C07-C12) ana ışık yönü her çekimde "icat edilir".
DOĞDUĞU   metin
KURAL     GECIS_VE_SES_SUREKLILIGI.md §1 madde 2 (mekân başına ışık cümlesi birebir) [TERCİH] · AGENTS T18
ARIZA     T18 / T04
DÜZELTME  - C04: `same pit light` → `lit by hard violet space light with warm amber work lamps`.
          - C06: `inside the same Needle cockpit` → `inside the Needle cockpit`, ve ek paragrafa M02 ışık cümlesi (FILM kimlik 15·ışık, birebir) eklenir.
          - M03 için ışık cümlesi plan dışı (ref 16 promptunda yok). Ref 16 onaylanınca ışık yönü okunup KİMLİK tablosuna yazılır ve C07-C12 hepsine girer.

### B5 · CİDDİ · C02 Video: "yazı eklenir" ↔ "in-shot caption ekleme"
YER       C02 Video G01:360-362 (açılış)
KANIT     `Do not add in-shot captions …` (ORTAK HAREKET) ile aynı promptta `The flat system line is added over the image; no speaking face.`
ETKİ      Model "system line"ı ekran yazısı ya da altyazı olarak çizebilir. Açılış karesine yazı girer; B2/T06. Aynı cümle ses mi yazı mı belirsiz.
DOĞDUĞU   metin (plan cümlesi)
KURAL     BILINEN_TUZAKLAR §B sıra 2 · FILM.md:340 R02 MACHINE, kurguda [SÖZLEŞME]
ARIZA     T06
DÜZELTME  Plan metni; sahibe sor. Minimal: `The flat system line is added over the image; no speaking face.` → `No speaking face and no text on screen.` (R02 kurguda zaten eklenir).

### B6 · CİDDİ · C04, C06, C08: kadraj dışı telsiz satırı Dialogue bloğunda
YER       C04 G01:410-413 · C06 G01:463-466 · C08 G01:513-516
KANIT     C04: `RAKA: "Why are you still here?"` / `AXI: "They don't let losers leave."` · C06: `KALIX: "Everybody says that."` · C08: `RAKA: "That's the plan you brought?"`. FILM.md:341-343 ve 346: bu satırların Kaynak'ı `telsiz — kadraj dışı, dudak oynamaz; kurguda`.
ETKİ      Kadrajdaki tek yüz (C04'te Raka) telsiz satırının ağzını da oynatabilir. Kendi promptundaki `Do not make Raka mouth Axi's words` cümlesiyle aynı blokta karşıt istek. Tuzak B11 (ses ve ağız kimliği).
DOĞDUĞU   metin
KURAL     FILM.md:391 "telsiz · kadraj dışı … → ses kurguda eklenir" [SÖZLEŞME]. F5_yazim_karari.md:81 (bütün replikler) ile :89 (telsiz yalnız kurguda) birbiriyle çelişiyor. C02 ve C03'te telsiz satırı Video'dan çıkarılmış, C04/C06/C08'de kalmış: uygulama tutarsız.
ARIZA     yeni
DÜZELTME  Üç bloktan telsiz satırı silinir (`AXI: "They don't let losers leave."`, `KALIX: "Everybody says that."`, `RAKA: "That's the plan you brought?"`). Vuruş cümleleri ("while Axi answers from the communication channel") kalır. Plan Dialogue bloğunu aynen taşıdığı için sahibe sor.

### B7 · CİDDİ · C06: göğüs kemerini kim, hangi elle çekiyor?
YER       C06 Görsel G01:452 · Video G01:461
KANIT     `one simple chest restraint being pulled taut` (tutan yok) · Video `Raka gives the restraint one final tightening pull`. Kimlik satırı `Plain cobalt flight suit with an ivory neck seal, no helmet.` (elde tutuş sürümü; `empty hands` düşmüş, el tarifi yerine konmamış).
ETKİ      Eller kadrajda mı değil mi belli değil. Raka'nın parmak yapısı hiçbir kimlik cümlesinde yok. Kemerin yolu (hangi omuzdan, hangi kalçaya) ve tarafı yazılı değil. Hayali kavrama ya da el-kemer kaynaşması.
DOĞDUĞU   metin
KURAL     devamlilik "Tutan ve bağlantı" · BILINEN_TUZAKLAR §B sıra 1 · FILM.md:246-247 (işaret: sayı + taraf + konum) [SÖZLEŞME]
ARIZA     T01
DÜZELTME  Görsel: `one simple chest restraint being pulled taut` → `one simple chest restraint running diagonally from her right shoulder across the chest, held taut by her own hand at the lower frame edge` (taraf ref 1 onayında doğrulanır). Video: çekme hareketini omuz hareketine çevirmek plan değişikliğidir; sahibe sor.

### B8 · CİDDİ · C05: Kalix omuz şeridinin tarafı yok
YER       C05 Görsel G01:426 ve 428 · FILM.md §3 kimlik 7
KANIT     `one restrained crimson shoulder sash` (iki yerde). Tarafı, konumu ve "the only marking" ifadesi yok.
ETKİ      Kalix C05, C27, C46'da (G04 ve G06) görünür. Şerit her seferinde başka omuza düşer; ilk kare sabitleyemez.
DOĞDUĞU   metin
KURAL     FILM.md:246-247 "İşaret: sayı + taraf + konum + 'the only marking'" [SÖZLEŞME]. G01 not satırı bunu bilerek ertelemiş ("F7 kare onayında seçilir").
ARIZA     T16 / T09
DÜZELTME  Ref 7 üretilip tarafı okunur okunmaz hem KİMLİK tablosundaki hem de C05 promptundaki `one restrained crimson shoulder sash` → `one restrained crimson sash over the <left|right> shoulder, the only marking on the garment`. Ref 7 onaylanmadan C05 karesi üretilmez (iş emrine ekle).

### B9 · CİDDİ · C01: Axi'nin yanak uzantıları dağılımı yok, kare kapısı sayımı çelişiyor
YER       C01 Görsel G01:327 · FILM-iş emri kare kapısı G01:526
KANIT     `exactly four short fixed cheek sensory tendrils`; yüz `turned toward a broad side window`. Kare kapısı: `yanak uzantısı 4, göz 2`.
ETKİ      Yüz sola ya da sağa dönükken dörtlü dağılım (2+2 mi, 4+0 mı) yazılı değil. Model dördünü tek yanağa dizerse kapı "geçti" sayar; Axi'nin C20, C33, C45 yüzleri 2+2 gelir. Kimlik sayımı görülemez.
DOĞDUĞU   metin
KURAL     FILM.md:246-247 (sayı + taraf + konum) [SÖZLEŞME]
ARIZA     T16
DÜZELTME  Ref 3 onayında dağılım okunur. 2+2 ise kimlik hücresi `exactly four short fixed cheek sensory tendrils` → `exactly four short fixed cheek sensory tendrils, two on each cheek` olur ve C01 yüzü üç-çeyrek (dört uzantı da seçilebilir) kalır.

### B10 · CİDDİ · Needle-Fang yan sırası C07-C08'de yazılmamış; C10'un sol-kanat vuruşuna bağlı
YER       C07 Görsel G01:479 · C08 Görsel G01:502 · FILM.md:64 (S10) ve :266 (C10)
KANIT     C07: `Two craft are in front and detailed` (sıra ve yan yok). C08: `Through the side window, Raka's white craft glides in the same direction as Thren's craft` (hangi pencere belli değil). Plan C10: `Fang'in yan koruması Needle'ın sol ön fren kanadına vurur` (FILM.md:135 sol/sağ aracın kendi yönüne göre).
ETKİ      Fang, Needle'ın solunda olmalıdır (Needle, Fang'ın sağında). C07-C08 rastgele bir yan kurarsa C09-C10 geçiş ters kurulur: sağ kanat kırılır ya da yan ters çıkar. Filmin tek asimetrik hasar zinciri bu yan bilgisine bağlı.
DOĞDUĞU   metin
KURAL     FILM.md §4 "Taraf / yön" sütunu (T11) · FILM.md:135 [SÖZLEŞME]
ARIZA     T11
DÜZELTME  - C07 Görsel: `Two craft are in front and detailed` → `Two craft are in front and detailed, Fang on the left of Needle`.
          - C08: `Through the side window` → `Through the right-hand side window`, hasar tarafıyla çelişmeyecek şekilde. G02 C09-C10 ile birlikte kontrol edilsin (G02 bu eleştiriye verilmedi).
          - C04: römorkörün Raka'nın hangi tarafında olduğu da yazılmamış (`outside the side window`); C47 ile aynı yan seçilmeli.

### B11 · CİDDİ · C07 / C08: Halo, Bastion, Sickle referanssız, kimlik cümleleri kısmi
YER       C07 Görsel G01:479-481 · C08 G01:504 · FILM.md:117-119 (§3 "Kullanan çekimler")
KANIT     Halo/Sickle/Bastion için ref eklenmemiş; Halo: `Halo, a compact enclosed oval alien racing craft, warm-gold hull, one strong central rear drive and two short fixed stabilizer blades` var ama `Clean forward silhouette with no wings that flap, no weapons or wheels` yok. Sickle'da `Fixed rigid crescent geometry, not an animal and no flapping surfaces` yok. Bastion `Exactly three rear engines in a left-center-right row` yerine `with all three rear engines active`. Needle'da `Reinforced narrow nose, one pilot canopy, no weapons or wheels` yok. Fang'da `Single compact pilot canopy, no weapon` yok. C08'de Needle hücresi parafraz (`one blue booster cell on its dorsal spine`). §3'te 10, 11, 12 için C07 "kullanan çekimler"de yok.
ETKİ      Üç araç ilk kez, yalnız metinle ve hareket halinde çıkıyor. Kanat çırpan ya da hayvan biçimli hilal en olası kayma. Üç araç sonra ayrıntılı çıktığında (C23, C25-C26, C44) renk ve biçim tutmayabilir.
DOĞDUĞU   metin + referans seçimi
KURAL     FILM.md:246 "Kadrajda görünen her parça … kelime kelime girer; kısaltılmaz" [SÖZLEŞME] · film_dogrula Y2
ARIZA     T16 / T05
DÜZELTME  - Atlanan koruma cümleleri (Halo siluet, Sickle geometri, Bastion motor, Needle burun ve kabin, Fang kabin) KİMLİK tablosundan birebir eklenir (C07 ek paragrafı ~+350 karakter, tavan 4.300 altında).
          - 10, 11, 12 için "kullanan çekimler"e C07 işlenir.
          - Referans eklemek plan dışı olduğu için sahibe sor.

### B12 · KÜÇÜK · "smoke-gray" renk adı C01'de yazıldığı hâlde 8 SORU "smoke yok" diyor
YER       C01 Görsel G01:327 (3 kez) · 8 SORU Q5 G01:574
KANIT     `Axi's smoke-gray face` · `Soft smoke-gray face` · 8 SORU: `plume · smoke · steam … yok`. Aynı kimlik cümlesi ref 3 promptunda, FILM.md §3 tablosunda ve C20, C33, C45'te de geçecek.
ETKİ      Renk adı, film_dogrula AKISKAN listesinde (`smoke`). Model yüzün çevresine duman çizebilir (BILINEN_TUZAKLAR §C: renk adı kadraja basılıyor). 8 SORU cevabı doğru değil.
DOĞDUĞU   metin
KURAL     film_dogrula DERS Y5 [ARAÇ]
ARIZA     T03 / T06
DÜZELTME  Ref 3 henüz üretilmedi, değişim ucuz: `Soft smoke-gray face` → `Soft slate-gray face` (plan R03 metni; sahibe not). Q5 satırı düzeltilir.

### B13 · KÜÇÜK · C06 aynı promptta "ivory collar" ve "ivory neck seal"
YER       C06 Görsel G01:452 ve 454
KANIT     `cobalt suit and ivory collar` (plan) ve `Plain cobalt flight suit with an ivory neck seal` (kimlik). C04'te yalnız `ivory neck seal`.
ETKİ      Model iki ayrı yaka parçası çizebilir ya da ikisini birleştirir.
DOĞDUĞU   metin (plan)
KURAL     FILM.md:246 [SÖZLEŞME]
ARIZA     T16
DÜZELTME  `cobalt suit and ivory collar` → `cobalt suit and ivory neck seal`.

### B14 · KÜÇÜK · C01: Axi'nin tür ve ifade cümleleri promptta yok
YER       C01 Görsel G01:327-329
KANIT     Kimlik 3·tür (`Axi, an adult nonhuman former racing pilot now forced …`) ve 3·ifade (`Restrained grief and practical intelligence.`) yok. Yerine plan: `restrained grief and disbelief`.
ETKİ      "Yetişkin, insan olmayan" bilgisi yalnız ORTAK GÖRÜNÜM'deki `nonhuman creature design` ile korunuyor. Axi'nin ifadesi C20, C33, C45'ten farklı kurulur.
DOĞDUĞU   metin
KURAL     FILM.md §3 kimlik 3 [SÖZLEŞME]
ARIZA     T16
DÜZELTME  Ek paragrafın başına `Axi, an adult nonhuman racing pilot.` ("former … mechanic" kasıtlı atıldığı için kısaltılmış sürüm; kimlik tablosuna † olarak işlenir).

### B15 · KÜÇÜK · C07: "far behind" ↔ "all five stay in view" + kamera yanında takip
YER       C07 Video G01:488
KANIT     `with the camera tracking steadily alongside` · `run far behind as small silhouettes, and all five craft stay in view`.
ETKİ      Öndeki ikiliyi izleyen kamera, "uzakta" üç aracı kadrajda tutmaz. Beşinin görünmesi için ya kamera geri çekilir (iki ayrıntılı araç küçülür) ya da sayı tutmaz.
DOĞDUĞU   metin (plan)
KURAL     —
ARIZA     yeni
DÜZELTME  `with the camera tracking steadily alongside` → `with the camera tracking steadily alongside the group from slightly behind`.

### B16 · KÜÇÜK · Vuruş planı: C03 ve C04 son vuruş donuyor; dört çekim aynı iskelet
YER       C03 Video G01:385 · C04 G01:408 · C04, C06, C07, C08
KANIT     C03 `7-10 s: One single installation action, no new shot. The single blue cell sits locked …` (0-7 s'de de `withdraw`, 7-10'da yine `leave the frame`). C04 `7-10 s: Preserve her exact face … Her eyes stay on the maintenance tug … to the end`. C04, C06, C07, C08: hepsi 0-3 · 3-7 · 7-10.
ETKİ      Son 3 s hareketsiz tutuş: bir sonraki kesmeye "fotoğraf" olarak girer. C03'te çekilme eylemi iki vuruşa yayılmış.
DOĞDUĞU   metin
KURAL     devamlilik "10 s planı" · GECIS_VE_SES_SUREKLILIGI.md §1 madde 4 [TERCİH]
ARIZA     H10
DÜZELTME  - C03: 0-7'den `and withdraw` çıkar (çekilme yalnız 7-10'da).
          - C04 7-10: `Her eyes stay on the maintenance tug … to the end of the shot` → `The camera creeps in a touch closer on her eyes as they stay on the tug to the end of the shot`.

### B17 · KÜÇÜK · Görsel ↔ Video başlangıç durumu: C04 ve C05
YER       C04 Görsel G01:399 vs Video G01:408 · C05 Görsel G01:426 vs Video G01:435
KANIT     C04 Görsel `Raka looks toward a softly blurred gray maintenance tug`; Video `0-3 s: Raka turns her eyes slightly toward the maintenance tug`. C05 Görsel `five colored race-lane lights` (yanık/sönük yazılı değil); Video `The five background lane lights illuminate sequentially once`.
ETKİ      Bakış zaten dönükse "dön" eylemi iki kez yapılır ya da atlanır. Işıklar kareden yanıksa "yanma" anı hareketsiz kalır.
DOĞDUĞU   metin (plan)
KURAL     devamlilik "Görsel ↔ video"
ARIZA     H05
DÜZELTME  C04 Video: `turns her eyes slightly toward` → `holds her eyes on`. C05 Görsel: `five colored race-lane lights` → `five colored race-lane lights, still dark`.

### B18 · KÜÇÜK · C08 7-10 s: yön cümlesi birbirine dolanmış
YER       C08 Video G01:511
KANIT     `Raka's white Needle keeps gliding past the window in the same direction as the roots outside stream by in one direction`
ETKİ      "Needle kökler gibi aynı yöne akıyor" okunabilir: yan yana gidiş yerine geride kalış. 0-3 s'deki `glides past the side window` da "önünden geçiyor" demek, planın "yan yana" ifadesi değil.
DOĞDUĞU   metin
KURAL     FILM.md:62 (S8 "aynı yönde akar")
ARIZA     T11
DÜZELTME  `keeps gliding past the window in the same direction as the roots outside stream by in one direction` → `keeps pace beside Thren's craft while the roots outside stream past in the opposite direction`. 0-3 s'de `glides past` → `keeps pace beside`.

### B19 · KÜÇÜK · Referans promptlarında plan kodu: V01, V02, V04
YER       G01:197, 207, 217 (ref 20, 21, 22)
KANIT     `Edit the supplied intact V01 Needle reference` · `V02 Fang` · `V04 Bastion`
ETKİ      Kısa büyük harfli etiket kadraja basılabilir (V01 yazısı gövdeye).
DOĞDUĞU   metin (plan)
KURAL     BILINEN_TUZAKLAR §C (referans kodu prompta yazılmaz) [ARAÇ]
ARIZA     T06
DÜZELTME  `intact V01 Needle reference` → `intact Needle reference` (V02 ve V04 için aynı).

### B20 · KÜÇÜK · ORTAK GÖRÜNÜM Video promptlarında yok; Görsel'de başta, Video'da yok
YER       Bütün Video blokları (G01:334, 360, 383, 406, 433, 459, 486, 509)
KANIT     GECIS §1.1: "her görsel ve video promptunun sonunda birebir". G01'de Görsel'de anahtarlardan sonra (F5_yazim_karari.md:61); Video'da hiç yok (planın "ORTAK HAREKET" kuralı).
ETKİ      Karelerle videoların renk ve doku dili ayrı; 8 klibin kesme sıçraması riski.
DOĞDUĞU   metin
KURAL     GECIS_VE_SES_SUREKLILIGI.md §1 [TERCİH]. Plan lehine bırakılabilir.
ARIZA     T04
DÜZELTME  Sahip kararı; istenirse her Video'nun sonuna `Restrained 35mm grain, deep violet space with cold cobalt and warm amber accents.` (ORTAK GÖRÜNÜM'ün renk ve grain parçası) eklenir.

### B21 · KÜÇÜK · FILM.md §4 Kadraj sütunu 48 satırda aynı yer tutucu
YER       FILM.md:257-304 (Kadraj · kamera)
KANIT     C07'den C48'e kadar her satır: `plan tablosu (C01-C06 plan istemi)`. Gerçek kadraj C07 ve C08 için yalnız G01 not satırlarında ("yazar seçimi").
ETKİ      Ardışık aynı-mekân çekimlerinde ölçek ve açı farkı §4'ten okunamaz. G01 içinde C04→C06 (orta yakın → sıkı üç-çeyrek) ve C07→C08 (geniş → yakın) prompt metninden kontrol edildi: fark var.
DOĞDUĞU   metin
KURAL     devamlilik "Kesme sürekliliği" [TERCİH]
ARIZA     yeni
DÜZELTME  §4 Kadraj hücreleri C07-C48 için gerçek kadrajla doldurulur (örn. C07 `geniş yan, soldan sağa`).

---

KORU: Kimlik cümleleri C04, C05, C06, C08'de KİMLİK tablosundan kelime kelime (Raka 4 parça, Kalix 4 parça, Thren 4 parça). G01 ve FILM.md §3 tabloları satır satır aynı. C03'te hücre durumu Needle kimlik hücresinin yerine bilerek yeniden kurulmuş ve nedeni yazılı.
KORU: ORTAK GÖRÜNÜM 8/8 Görsel'de birebir; ORTAK HAREKET 5 tam + 3 kısaltılmış, kısaltma yalnız ağız kadrajda replik olmayan çekimlerde.

ÖZET     ÖLÜMCÜL 0 · CİDDİ 11 · KÜÇÜK 10
KARAR    TUR KAPANABİLİR. ÖLÜMCÜL yok. Ancak CİDDİ bulguların çoğu (B1, B3, B5, B6, B7, B11) plan metninden doğuyor; "plandan asla dışarı çıkma" kuralı gereği düzeltme için sahip onayı gerekir. Plan dışı kalanlar (B4, B8, B9, B10) F7'de ref onayından sonra işlenebilir.
GİRDİ    ELESTIRI_PROTOKOLU.md · BILINEN_TUZAKLAR.md §B-C · .claude/agents/devamlilik.md · GECIS_VE_SES_SUREKLILIGI.md §1 (başı) · ILK_30_SANIYE_KILAVUZU.md §6 · ARIZA_LISTESI.md (H01-H12, T01-T19) · yatay_8_dk_filmler/DEAD_LAST/FILM.md (§1-§5 tamamı, kimlik tablosu, ORTAK GÖRÜNÜM/HAREKET, §4 C01-C48, §5 R01-R50) · PROMPTLAR/G01.md (tamamı, 589 satır) · ODA/F5_yazim_karari.md · film_dogrula.py (AKISKAN, ortak_gorunum). Grep ile ORTAK GÖRÜNÜM ve ORTAK HAREKET sayımı, meta kod taraması, akışkan ve şiddet sözcük taraması yapıldı.
YAPILMADI  film_dogrula.py çalıştırılamadı (shell yok). Kare dosyaları verilmedi, kare denetimi (C01-C03 açılış ölçütleri dahil) yapılmadı. G02-G06 ve plan dosyası (DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md) açılmadı; B10 ve B11'in G02+ yönü ayrıca doğrulanmalı. KAPSAM DIŞI: FILM.md §4 "Anlatacağı TEK bilgi" sütunundaki `Bi̇r Dünyanin Bedeli̇` gibi bozuk büyük-harf (i̇) dizgesi.
