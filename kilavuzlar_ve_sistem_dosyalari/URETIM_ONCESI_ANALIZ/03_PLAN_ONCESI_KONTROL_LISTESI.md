# ✅ PLAN ÖNCESİ KONTROL LİSTESİ

> **Ne zaman:** Plan ve Bible yazıldı, **tek kare üretilmedi.**
> **Süre:** ~20 dakika. Maliyeti sıfır.
> **Neden:** Aşağıdaki 18 maddenin **12'si gerçek filmlerde gerçekten oldu** ve
> hepsi üretimden SONRA, para harcandıktan sonra bulundu.
> **26.08.2026:** B3 (tema indeksi) ve B4 (açı yayı) eklendi — ikisi de
> yazılı kuralı olan ama hiçbir kapıda ölçülmeyen alanlardı; liste 12'den
> 14 maddeye çıktı.
> **01.09.2026:** B6 (politika satırı) eklendi → 15.
> **02.09.2026:** B5 (İSTEK/ENGEL/BEDEL) eklendi → 16; aynı gün dış
> araştırma turuyla B5b (AYRILIK) ayrıldı → 17. B5'in dördüncü satırı
> HASIM'dan MUHATAP'a düzeltildi ve "ORTAM hasım değildir" kapısı
> **geri çekildi** — gerekçe `04_ARASTIRMA_BULGULARI.md` T4.0.
> Teşhis: `06_HIKAYE_HATTI_TESHISI.md` §3.1.
> **14.09.2026:** A0 (HİKÂYE ONAYI) eklendi → 18. THE_LOCKED_PULSE 17/17 maddeyle
> geçti, hikâyesi vana tamiriydi; hiçbir madde "sahip bu hikâyeyi gördü mü"
> diye sormuyordu. Reform: `TODO_AKIS_VE_DERS_REFORMU.md` FAZ 9 · kapı
> `prompt_kontrol.py` ㉙ (yalnız 00_HIKAYE_ONAYI.md taşıyan klasörlerde).
> **Ek katman (06.08.2026):** `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` §7'nin
> 6 senaryo/kamera maddesi bu listeyle BİRLİKTE koşulur — bu listenin
> yerine geçmez, üstüne eklenir.

---

# 🔴 A. PLAN KENDİ İÇİNDE ÇELİŞİYOR MU

### A0 — HİKÂYE ONAYI VAR MI ⭐ 🆕 14.09.2026 · ⛔ A1'DEN ÖNCE, HER ŞEYDEN ÖNCE

```
□ 00_ANALIZ/00_HIKAYE_ONAYI.md var ve ONAY: satırı TARİHLİ (⬜ değil)
□ sahne satırı sayısı = PLAN'daki sahne sayısı (S0 … Sn)
□ SAHNELER bölümünde jargon yok: D-numarası · "novum" · kurulum harfi · "kilit"
□ PLAN'ın sahne haritası onaylı satırlardan sapıyorsa SAPMA bölümü dolu ve
  yeniden onaylı — sapma sessizce yapılmamış [D74]
□ LOGLINE ≤ 25 kelime · NEDEN İZLENİR tek soru · BEDEL sahne numaralı
□ ADAYLAR bloğu dolu (B, C: logline + neden elendi) ve 02_KONSEPT §0⑥ fikir
  turu kaydı + §5 ÖN-OTOPSİ KARAR satırı yazılı (21.09.2026 · HIKAYE_FIKIR_TURU §9)
```

**Neden ilk madde:** 17 maddenin 17'si kapıya bakar, hiçbiri hikâyeye bakmaz.
THE_LOCKED_PULSE (13.09.2026) hepsinden geçti; hikâyesi bir vana tamiriydi ve
sahip onu yazım bittikten sonra gördü. Bu liste PLAN'ı denetler; A0, PLAN'ın
denetlenmeye değer olup olmadığını denetler. Onay, dosya okunmadan sohbette
alınır (`yeni-film` adım 0.7 · AGENTS Kart A HİKÂYE); bu madde yalnız onun
kaydının yerinde olduğunu doğrular. Kaynak: reform ölçümü, 14.09.2026.

### A1 — Yasak ↔ anlatım çelişkisi ⭐ EN PAHALI HATA

```
□ Plan dosyasında "no text / NEVER text" yazan bir satır var mı?
□ Aynı dosyada bir ekranın/göstergenin İÇERİĞİ tarif ediliyor mu?
   ("the countdown reads 6:00:00", "the display shows 47%")

İKİSİ BİRDEN VARSA → PLAN BOZUK. Model her zaman YASAĞI seçer,
anlatım sessizce ölür ve QA'da görünmez (ekranda yanlış bir şey yoktur,
sadece bir şey yoktur).
```

> 🚨 **Gerçek olay:** The Tidal Hunt. Satır 285 `NEVER text`, satır 338
> `the countdown reads 6:00:00`. Sayaç ekrana hiç çıkmadı; "6 saatte geç"
> filminden geriye "bir kadın koşuyor" kaldı. → Ders 50

**Düzeltme:** Bilgiyi metinsiz kanala taşı — kapanan halka, su çizgisi,
gölge boyu. `02_RISK_KARTLARI.md` KART 5.

### A2 — Sahne sayısı tutuyor mu

```
□ Başlıkta yazan sahne sayısı ile dosyadaki sahne bloğu sayısı aynı mı?
□ Numaralarda atlama var mı? (S2 → S3.5 gibi)
□ Prompt gövdelerindeki "Scene N of X" ifadesi doğru X'i mi söylüyor?
```

> 🚨 **Gerçek olay:** The Kaleida Crash "13 SAHNE" diyor, dosyada 12 blok var,
> SAHNE 3 hiç yok, 12 promptun 12'si "Scene N of 13" diyor.

### A3 — Süre tutuyor mu

```
□ sahne sayısı × klip süresi = iddia edilen toplam süre?
   (12 × 10s = 120s.  "4:14" yazıyorsa bir yerde hata var)
```

### A4 — Yasaklı sahne tipi var mı ⭐ [DERS 77 · 06.08.2026]

> 🚨 **Gerçek olay:** DERS 69 (05.08) *"biniş/iniş hareketi hiçbir segmentte
> kadraja alınmaz — 0 kez"* diyordu. **Ertesi gün** THE STARLESS CIRCLE'ın
> planına S14 BİNİŞ sahnesi eklendi ("yedi basamak + eşikte son bakış") ve
> klon tam o sahnede çıktı (Nicelik 1/10 · Sayı-Ayrışma 1/10). Ders
> LESSONS_LEARNED'da duruyordu, iki rubriğe işlenmişti, plana hiç ulaşmadı.
> Dersler üretim ve QA kanallarına akıyor; **karar kanalına akmıyor.**

```
□ Plandaki HER sahne için sor — aşağıdaki tiplerden biri mi?
     · araç / kapak / airlock BİNİŞ-İNİŞ hareketi        [D69]  3 vaka
     · tek ışıklı loş iç mekâna GİRİŞ                    [D69]  1 vaka
     · aynalı-yansıtıcı yüzey önünde tek karakter        [D20 · D69]
     · novum'u TÜRETİLMİŞ optik fenomen taşıyor
       (gölge · yansıma · kostik · parlama deseni)       [D73]
     · novum'u bir YOKLUK taşıyor (boşluk, delik,
       "olmayan" bir şey)                                [D76]
     · jenerik / başlık kartı ya da kapak çıktısı        [D34 · D70 · D72]
□ VARSA: sahne ya çıkarılır ya dersin öngördüğü biçime dönüştürülür —
  ve karar plan dosyasına TEK SATIR olarak yazılır:
     "S14: biniş hareketi kadraj dışı — D69 ① gereği (06.08)"
□ Satır yoksa denetim YAPILMAMIŞ sayılır (D74 mantığı: kaydı olmayan kapı).
```

### A5 — FİLMİN 1 NUMARALI RİSKİ SAYIYLA MI YAZILDI ⭐ 🆕 08.09.2026 [D192]

> 🚨 **Gerçek olay:** THE OPEN CIRCUIT. Plan kendi 1 numaralı riskini adıyla
> ilan etmişti (KIVILCIM) ve onu **yalnız sıfatla** korudu: *"çizgi TEK, İNCE,
> DÜZ ve SÖNÜMLÜ"*. Aynı planda ölçülebilir yazılmış her şey ölçülebilir kaldı
> (koni "BİR SANİYEDEN AZ", toz halkası "iki saniyede oturur"). Ekranda doruğun
> boşalması **en az 0,5 s süren, dallanan, kadraja ışık bırakan bir ŞİMŞEK**
> olarak geldi — her sahnenin NEGATIVE bloğunda *"no lightning bolt"* yazılıyken.
> Negatif cümle yasağı söyler, **biçimi söylemez**; model boşluğu doldurur.

```
□ Plan kendi 1 numaralı riskini ADIYLA yazdı mı? (risk kartı / göz kapısı)
□ O riskin POZİTİF biçimi SAYI taşıyor mu — süre · uzunluk · genişlik · adet?
     ✗  "çizgi TEK, İNCE, DÜZ ve SÖNÜMLÜ"
     ✅ "tek çizgi · ≤0,3 s · genişliği eldiven kalınlığından az ·
         söndükten sonra 0 kare artık ışık"
□ SPEC'in göz kapısı o sayıyı ölçülebilir cümleyle tekrarlıyor mu?
□ Yalnız NEGATIVE cümlesi varsa denetim YAPILMAMIŞ sayılır: yasak, biçim değildir.
```

> **Kural:** sayısal kilit %100, tarif kilidi %0 tuttu
> (`01_DERS_ETKINLIK_RAPORU.md` §4). Filmin en pahalı vuruşu, tarif kilidiyle
> korunan tek vuruş olmamalıdır.

---

---

# 🔴 B. FİLMİN DORUĞU YAZILMIŞ MI

### B1 — Doruk anı bir sahnenin İÇİNDE mi

```
□ Filmin en yüksek gerilim anını hangi sahne TAŞIYOR? S___
□ O sahnenin video promptunda o an gerçekten TARİF EDİLİYOR mu?
□ Yoksa iki sahnenin ARASINA mı düşüyor?
```

> 🚨 **Gerçek olay:** The Tidal Hunt. S8 `"begins to climb as the wave closes"`
> → S9 `"the wave has passed"`. **Dalganın çarptığı an hiçbir sahnede
> yazılmamış.** Doruk iki sahne arasında. Kurguyla kapatılamaz.

**Test:** Sahne listesini oku, her geçişte sor — *"burada ekranda görülmeyen
ama olması gereken bir şey var mı?"*

### B1b — Katmanlı dünya ise ışık takvimi var mı

```
□ Film irtifa/bölge/derinlik gibi bir eksende ilerliyor mu?
□ Öyleyse her sahnenin katmanı ve o katmanın ışığı TABLO halinde yazılı mı?
□ Sahneleri eksene göre sıralayıp ışığı okuduğunda monotonik mi?
   (parlak → karanlık → parlak = plan ya da üretim yanlış)
```

> 🚨 **Gerçek olay:** The Canopy World, 7 katman, 3.000m'den 0m'ye kesintisiz
> iniş. Kurgu sırası plana birebir uygun — ama Kök Labirenti sahnesi
> `"cold blue-white light"` yerine parlak güneşli üretilmiş. Mantık QA'sı
> ışık salınımını gördü ama sebebi kurguda sandı; belge kontrolünde
> üretim hatası olduğu çıktı.

### B2 — Bedelli seçim var mı

```
□ Karakter bir ŞEY seçiyor mu, yoksa olaylara tepki mi veriyor?
□ Seçtiğinde neyi KAYBEDİYOR?
□ Kaybı hangi sahnede GÖRÜLÜYOR? S___
```

> 🚨 **Gerçek olay:** İki bağımsız senaryo QA'sı, iki farklı filme aynı
> gerekçeyle Karakter 4/10 verdi: Ring Walker ve Kaleida Crash.
> Kaleida: çakılıyor → yürüyor → sinyal gönderiyor → bekliyor. Bedel yok.
> Karşı örnek: Low Power S20 — anahtarı çeviriyor, kendi hayatını veriyor.

### B3 — Tema hangi sahnede EKRANA çıkıyor ⭐ 🆕 26.08.2026

```
□ Planda TEMA satırı var mı — tek kelime
   (TEMA_MUHENDISLIGI_KILAVUZU.md §3'ün sekiz temasından biri)
□ Tema, novum kelimesi geçmeden tek cümleyle söylenebiliyor mu?
   "bu film ___ hakkında"                              [TEMA §9 son madde]
□ ⭐ ASIL MADDE — tema hangi sahnelerde MOTİFE dönüşüyor:
   S___ , S___ , S___     (en az 3 sahne numarası · TEMA §5 matrisi)
   Her sahnede en az BİR 3. derece indeks: kamera · ışık · nesne · kinesik
□ B2 ile çapraz oku: bedelli seçimin yaşandığı sahne bu listede mi?
   Değilse tema olay örgüsüne bağlı DEĞİL, süslemedir.
```

> 🚨 **Gerçek olay:** THE KALEIDA CRASH · film kaydının tema satırı:
> **"bedel yok → tema dekoratif kalıyor" (Tema 5/10)** — aynı kayıtta
> Karakter 4/10 "tepki veriyor, seçim yapmıyor". Yani tema düşüşü B2'nin
> (bedelli seçim) doğrudan sonucu; iki madde aynı boşluğu iki yerden ölçüyor.
>
> ⚠️ **ÖLÇEK DÜRÜSTÇE:** "tema yaygın olarak zayıf" iddiasının tek veri
> tabanı ⛔ KAPALI `03_HIKAYE_KALITE_TABLOSU.md`'dir: geçerli 13 satırın
> **7'sinde Tema ≤5** (tam 4 olan 2 film: Stone Sky · Blind Return).
> O tablo 22.08'de kapatıldı ve AGENTS §1'e göre yeni tablolarla
> KARŞILAŞTIRILAMAZ — eğilim göstergesidir, kanıt değil. Canlı T4'te
> bugün yalnız 2 film var. Bu madde bir eğilime karşı yazıldı; eğilimin
> doğrulanması E fazının (pilot + mod D ölçümü) işidir.
>
> ⚠️ Cold Burn FRAGMAN kaydında aynı cümle geçer ama orada **bulgu
> DÜŞÜRÜLDÜ** (fragman merceği + önerme kapısı). Kanıt sayılmaz.

**Düzeltme:** `TEMA_MUHENDISLIGI_KILAVUZU.md` §5 matrisinden temanın
satırını al, motifi sahne sahne dağıt. Betik tarafı:
`prompt_kontrol.py` TEMA satırını ve sahne indekslerini arar.

### B4 — Açı yayı yazıldı mı ⭐ 🆕 26.08.2026

```
□ SAHNE-KURULUM DİZİSİ yazılı mı?   (örn. A · C · A · C · B · A)
   kurulum = açı + ölçek + kamera konumu       [ACI_YAYI §4]
□ Ardışık HER çift güvenli bandı tutuyor mu?   [ACI_YAYI §3]
   ≥1 tam ölçek kademesi  VE  ≥45° açı farkı
   (bilinçli ŞOK ise işaretli — filmde en fazla 2)
□ Kurulum SAYISI bandın içinde mi?             [ACI_YAYI §4]
   6 sahne → en az 3 · 12 sahne → en fazla 5-6 · uzun formatta
   kurulum sayısı sahne sayısının yarısını geçmez
□ ⭐ AÇI TİPİ sayısı ≥3 mü?                     [KAMERA_ACISI §2]
   (alt · üst · tepe · eğik · göz hizası · OTS · profil · POV)
   Üç kurulumun üçü de alttan bakıyorsa kurulum çeşitliliği YOK,
   yalnız mesafe çeşitliliği vardır.
□ Derece yazan her satır abartı bandında mı?   [KAMERA_ACISI §5]
   dutch 5-15° ideal · 15-30° meşru · 35°+ ⛔ kiç
   alt açı 15-30° meşru · 45°+ ⛔ · üst açı 15-30° · 45-60° ⛔ ölü bölge
□ Doruk sahnesi en yüksek kontrast sıçramasını taşıyor mu? [ACI_YAYI §9]
□ 🆕 KURULUM İSKELETİ satırı PLAN'da yazılı mı?  [ACI_YAYI §4b · 05.09.2026]
   Bu satır kapıyı AÇAR: prompt_kontrol ⑩④ yalnız onu beyan eden
   dosyada koşar. Harf sayısı sahne sayısına eşit olmak zorunda.
□ 🆕 12+ sahne: KÜME ≥2 mü?                      [ACI_YAYI §3 🕰️]
   Küme = tek vuruş sürerken ardışık 2-3 klip aynı kurulumda.
   Sahne sayısını ve süreyi DEĞİŞTİRMEZ, kesme sayısını düşürür.
   6-11 sahne ve dikey shorts MUAF.
□ 🆕 12+ sahne: DÖNÜŞ oranı ≥%40 mı?             [ACI_YAYI §4b]
   Dönüş = kaynağından EN ÇOK 3 sahne sonra gelen tekrar. Daha
   uzağı yeniden tanıtımdır ve sayılmaz. ⛔ Üst banda uymak yetmez:
   A B C D E F A B C D E F tavana uygundur, dönüş oranı %0'dır.
□ 🆕 Her dönüş/küme kamera metnini BİREBİR kopyalıyor + işaret
   satırını taşıyor mu?                          [ACI_YAYI §7 ⑥]
   Model harf iskeletini GÖRMEZ, yalnız metni görür.
```

> 🚨 **Gerçek olay:** THE BRIGHT TETHER (26.08.2026, deponun en yeni filmi).
> 6 sahne, 3 kurulum — `ACI_YAYI §4` bandının **içinde** ve dosya bunu
> kendi kontrol bloğunda doğru şekilde ilan ediyor. Ama 6 video promptunun
> kamera satırından yalnız **3'ü benzersiz**: S0·S2·S5 birebir aynı cümle,
> S1·S3 birebir aynı cümle. Üç kurulumun üçü de yerden bakıyor (0.90 m ·
> 0.35 m · 0.20 m), lens 6/6 sahnede 24mm. Yani bant ASGARİYİ ölçüyor,
> hiçbir kapı asgarinin üstüne itmiyordu — ve açı TİPİ hiç sayılmıyordu.

**Düzeltme:** Bu maddenin dört sayısı da betikte ölçülüyor
(`prompt_kontrol.py` · kurulum çeşitliliği · açı sözlüğü · abartı eşiği).
Liste maddesi betiğin göremediği tek şeyi sorar: dizinin VURUŞLA eşleşmesi
(`KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` §3 vuruş→açı tablosu).

> ⛔ **KLİP İÇİ lockoff bu maddeyle ÇELİŞMEZ.** Kamera klip içinde hiç
> hareket etmez (KART 8); değişen tek şey sahneler ARASINDA kurulumdur.
> Sahneler zaten ayrı kliplerde üretiliyor — farklı açıdan çekmenin
> gizli kesme riski sıfır (`02_RISK_KARTLARI.md` KART 8 kapsam bloğu).

---

### B5 — İSTEK · ENGEL · BEDEL · MUHATAP ⭐ 🆕 02.09.2026 · ✏️ aynı gün düzeltildi

> **Gerekçe (TUR 4 ile DEĞİŞTİ):** madde ilk olarak `05_DIKEY_HAT_TESHISI`
> §5①'den geldi. Dış araştırma turu, maddenin ÜÇ satırını kaynakladı ve
> DÖRDÜNCÜ satırın gerekçesini düşürdü — ikisi birden aşağıda.
>
> ✅ **Kaynaklanan:** izleyicinin *"hiçbir şey olmuyor / umursamadım"*
> tepkisinin **üç belgelenmiş sebebi** vardır ve üçü bu maddenin üç
> satırıdır: **isteğin yokluğu · bedelin yokluğu · muhatabın yokluğu**
> [`04_ARASTIRMA_BULGULARI.md` TUR 4 · T4.1 satır 6].

```
□ İSTEK:   karakter buraya NE YAPMAYA geldi — film BAŞLAMADAN önce
□ ENGEL:   bu isteği NE engelliyor
□ BEDEL:   isteğini alırsa neyi kaybediyor    ⭐ ASIL SATIR — aşağıya bak
□ MUHATAP: eylemin yankısı NEREDE görünüyor
           □ ikinci insan (kadrajda VEYA kadraj dışında)
           □ karakterin film başlamadan verdiği kendi kararı
           □ karakterin kendi bedeni / dayanma sınırı
           □ ortamın KALICI olarak değişen bir parçası

⛔ KAPI 1 — "anlamak", "görmek", "fark etmek" İSTEK DEĞİLDİR.
   İstek, film başlamasa da var olan bir iştir.                [05 §5①]
⛔ KAPI 2 — BEDEL bir SAHNE numarası taşımak zorundadır (B2 ile çapraz).
   Bedeli görünmeyen istek, izleyicide "güzel ama boş" karşılığı buluyor
   ve bu şikâyet kalıbı yorum korpusunda ölçüldü.       [TUR 4 · T4.1/13]
```

> ✏️ **GERİ ÇEKİLEN MADDE — 02.09.2026, yazıldığı gün** (kayıt:
> `04_ARASTIRMA_BULGULARI.md` T4.0):
>
> Bu maddenin ilk hâlinde bir KAPI 2 vardı: *"ORTAM bir hasım değildir…
> fizik kuralı hiçbir şey istemez."* **Geri çekildi.** İki bağımsız rapor
> çapraz okundu: insan-hasım ile doğa-hasım arasında izleyici
> tutundurması veya hatırlanma açısından **belgelenmiş nicel bir fark
> YOK**; fark çatışmanın türünden değil **bedelin büyüklüğünden** geliyor
> (Raskin · McKee/Cowgill kıyaslaması + DUST yorum korpusu). Ortam meşru
> bir karşı güçtür. Değişmeyen şey **BEDEL** satırıdır — ölçülmüş olan o.
>
> 🚨 **Gerçek olay (bu satırlar duruyor):** THE THIN ROOF'ta kadın *"bir
> çukura bakmaya"* gelmişti — bu seyirdir, istek değil; ④ merceği
> `ENDS OR STOPS: Stops` yazdı. THE SINKING STAKE (02.09) 25 sahne boyunca
> iki insanı yan yana tuttu ve merkezî seçimi *"biri onaylar, öteki karar
> verir"* oldu — **iki gövde, tek kişi.**
>
> ⚠️ **DÜRÜST KAYIT:** bu maddeyle yazılmış bir filmin skoru henüz YOK.
> Ölçülmüş boşluk: İSTEK 8/79 · ENGEL 2/79 (`06` §1.1).

### B5b — AYRILIK (yalnız iki insanlı planlarda)

```
□ İki figürün AYNI FİKİRDE OLMADIĞI sahne = S___
  · farkı taşıyan kanal: jest / duraklama / yön / temas reddi
  · ⛔ ikisi de aynı anda aynı şeyi yapıyorsa satır BOŞTUR
```

> **Kaynak:** kısa filmde çatışma ZORUNLU değildir [Raskin] — ama iki kişi
> kadraja girdiyse aralarındaki fark **etkileşimin kendisidir**, ve
> etkileşimin yokluğu "umursamadım"ın üçüncü sebebidir [TUR 4 · T4.1/6].

---

### B5c — ÜRETİM SIRASI ⭐ 🆕 05.09.2026 [D168]

```
□ ÜRETİM SIRASI plana yazıldı ve DRAMATİK SIRA DEĞİL:
  referans paketi → DORUK → merkezî seçim → kapanış imajı → S0 → kalanı
□ Üretilecek İLK sahne = S___   (doruk ya da merkezî seçim olmalı)
□ ⛔ Sıra S0'dan başlıyorsa satır GEÇMEZ.
```

> **Gerekçe:** yarıda kalma bir olasılık değil, bu hattın NORMALİDİR —
> üretim red alır, kota biter, motor değişir, gün biter (depoda 15 red
> vakası). Soru "film biterse nasıl görünür" değil, **"film HERHANGİ BİR
> NOKTADA durursa elde ne kalır"**dır. Baştan üretirsen elde hep KURULUM
> kalır ve kurulum, tanımı gereği, kendini savunamayan malzemedir.
>
> **Vaka:** THE SINKING STAKE (02.09.2026) — 25 sahnenin ~14'ü üretildi,
> sırası planla birebir, ve eksik 11 sahne ARDIŞIKTIR ve filmin SONUDUR
> (merkezî seçim S19 · doruk S21 · ikinci seçim S22 · final S24).
> Sahibin değerlendirmesi: *"ne bir mantıklı ilerleme var ne de sahneler
> arası devamlılık"* — ilerleme yok çünkü ilerleme VAR OLMAYAN kısımda.
>
> ⚠️ **Bu madde PLANI bağlar, ÜRETİMİ bağlamaz** [D168 · 2. vaka]:
> THE UPWARD FALL'da ÜRETİM SIRASI plana YAZILMIŞTI ("1. DORUK S24") ve
> S24 yine teslim edilmedi. Teslim tarafının ölçüm aleti ④ KURGU
> KAPISI'nın **FİNAL VURUŞ KANITI** satırıdır [D141].
>
> ⛔ **3. vaka THE STATIC SHADOW (13.09.2026) → ⛔ ÇALIŞMIYOR, araca çevrildi:** sıra plana
> yazılıydı (S14 → S12 → S15 → S01), makara S01-S10 tam, S11 · S12 · S13/S14 yok. Kapı artık
> üretim tarafında: `<FILM>_URETIM_DEFTERI.md` §4 — ilk KABUL satırı sıranın ilk halkası
> değilse ikinci klip üretilmez (AGENTS kart B). Bu madde plan tarafında KALIR, tek başına yetmez.

---

### B6 — POLİTİKA SATIRI ve ANLAM MALİYETİ ⭐ 🆕 01.09.2026

> **Gerekçe:** depoda 14 üretim reddi var (`FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md`)
> ve biri bir sahneyi **iptal ettirdi**. Bunu ÖNCEDEN yazan tek film
> YERCEKIMI'dir (00_PLAN risk ④ + F2 KİLİT 8) — ve redleri önceden gören
> tek film odur. Maliyeti sıfır, iki satır.

```
□ POLİTİKA SATIRI yazıldı mı?
     "Bu filmin en red-riskli karesi S___; nötr tarifi: ______________"
     ⛔ "riskli sahne yok" cevabı geçerli DEĞİLDİR — en riskli kare
        her filmde vardır, sıralamanın en üstündeki karedir.

□ Filmde şunlardan biri varsa KART 12 açılmış mı?
     gövdeye değen kuvvet · kalabalık + kaçan kişi · ateş/duman ·
     tehlike çerçevesi · bedenden bir şey çıkarma · yüzsüz izolasyon +
     kısıtlanmış uzuv · konuşan yüz + kapital kimlik bloğu

□ Alınan HER politika önlemi üç satır taşıyor mu?  [POLİTİKA §4.3]
     ÖNLEM:   ______________  (ne kaldırıldı)
     MALİYET: ______________  (hikâyeden ne gitti)
     TELAFİ:  ______________  (hangi kanala taşındı — §4.1'in dördü:
                               kütle-hız · malzeme sonucu · alet tepkisi ·
                               temassız gövde tepkisi)
     ⛔ TELAFİ boşsa önlem ALINMAMIŞTIR, film KISALTILMIŞTIR.

□ Milliyet · gerçek kurum · gerçek kişi adı planın hiçbir yerinde yok mu?
     ⛔ §7'de DOĞRULANMIŞ red. Ve şu an üç filmin CANLI promptlarında
        duruyor (defter §3) — kopyalayarak yayılıyor.
```

> 🚨 **Gerçek olay:** THE LAST SPAN (25.08.2026). Film tasarımı gereği
> **0 kare** yara/kan/ceset taşıyordu ve dosya bunu satır satır yazıyordu.
> Ama o sıfırı KORUMAK için `NEGATIVE:` bloğuna `gore` 29 · `blood` 26 ·
> `wounds` 26 · `corpse` 18 kez yazılmıştı. **İki aksiyon doruğu
> reddedildi.** Yasak, yasakladığı kavramı prompta sokar [D123].

**Düzeltme:** Kelime ekseni artık betikte ölçülüyor
(`prompt_kontrol.py` ⑯ · NEGATIVE bloğu DÂHİL). Bu liste maddesi betiğin
göremediği iki şeyi sorar: **kompozisyon riski** ve **anlam maliyeti**.

---

# 🟠 C. SAYISAL KİLİTLER YAZILDI MI

> Ölçülmüş tek gerçek: **tarif kilidi %0 tuttu, sayısal kilit %100 tuttu.**
> Aşağıdakilerin hepsi SAYI içermeli. İçermiyorsa tutmayacak.

```
□ İNSAN SAYISI      "tam 1 insan, 13 sahnenin 13'ünde"
                    ❌ "she is alone"          ✅ HUMAN COUNT LOCK: 1 × 13

□ KASK TAKVİMİ      "kapalı S0-S12, açık 0 sahne"
                    ❌ "visor ALWAYS VISIBLE"  ✅ HELMET STATE SCHEDULE

□ ÖLÇÜ              "gemi 140 m, bacak 20 m, viewport 1 m"
                    ❌ "massive ship"          ✅ sayı + referans nesne

□ YERÇEKİMİ         "0.38g — düşen nesne 1 saniyede 1.9 m"
                    ❌ "low gravity"           ✅ sayı + sonuç

□ SIVI TEMASI       "sıvıya dokunulan sahne: 2 (S6, S9). Diğer 11'de arka plan"
                    ❌ "she touches the water" ✅ sahne sayımı

□ CANLI ANATOMİSİ   "4 bacak, 1 baş, 1 kuyruk — 13 sahnenin hepsinde"
                    ❌ "creature anatomy fixed" ✅ parça sayımı
```

---

# 🟠 D. RİSK SAYIMI

```
□ 02_RISK_KARTLARI.md açıldı ve malzeme listesi işaretlendi
□ RİSK SAYISI: ___ / ___    ← payda 02_RISK_KARTLARI RİSK TOPLAMI'ndaki
                               soru sayısıdır (26.08.2026'da 12). Buraya
                               sabit sayı yazma, oradan oku.

  0-2 risk  → sistem bu filmi taşır
  3-4 risk  → dikkat, en riskli malzemeyi bir sahneye hapset
  5+ risk   → ⭐ 14.09.2026: KİLİT TAVANI — filme uygulanan ders kilidi ≤ 20
              (`prompt_kontrol.py` KILIT_TAVANI · ㉕). Malzeme AZALTILMAZ;
              tavanı aşan kilitler PLAN `### ⛔ UYGULANMAYAN KİLİTLER`
              bloğuna gerekçeyle yazılır. (Eski kural "malzeme azalt"
              geri alındı — 02_RISK_KARTLARI §RİSK TOPLAMI'ndaki ölçüm.
              Kamera 2→8 kanıtı KLİP İÇİ kamera hareketi talebiydi; sahneler
              ARASI açı değişimi B4 ile ayrıca zorunludur — ACI_YAYI §3.)
```

---

# 🟡 E. QA'YA HAZIRLIK — üretimden önce yazılır

Bu blok plan dosyasının sonuna eklenir. Üretim bitince QA promptlarının
SPEC bloğuna **doğrudan kopyalanır.** Yazılmazsa QA künyesi elle
hatırlanır ve bozulur — projede 4 rapor bu yüzden şartlı/geçersiz oldu.

```
□ QA SPEC BLOĞU plan dosyasına yazıldı:

  FILM:                 ___
  FORMAT:               ___
  SCENE COUNT:          ___     ← dosyadaki blok sayısıyla doğrulandı
  RUNTIME:              ___ s   ← sahne × klip süresi ile doğrulandı
  DIALOGUE LINES:       ___     ← konuşmalı sahne numaraları: ___
  SILENT SCENES:        ___
  VIRAL INTERSTITIALS:  ___     ← S___, S___  (bunlar KESİLEMEZ)
  PROTAGONIST:          ___     ← ad + meslek
  CENTRAL CHOICE:       S___    ← bedelin görüldüğü sahne
```

> 🚨 **VIRAL INTERSTITIALS satırı neden kritik:** Kaleida Crash'in senaryo
> QA'sı bu alan boş olduğu için iki viral ara sahneyi "gereksiz geçiş"
> sanıp kesme listesine yazdı. Filmin paylaşılabilir iki anıydı.

---

# 📋 TEK SAYFALIK ÖZET — kopyala, plan dosyasının sonuna yapıştır

```
ÜRETİM ÖNCESİ KONTROL — <FİLM ADI>            tarih: __________

A0 □ HİKÂYE ONAYI: ONAY __.__.____ · TUR _/3 · satır ___ = sahne ___ ·
     jargon yok · SAPMA: □ yok □ yeniden onaylı            [㉙ · 14.09.2026]
A1 □ "no text" ile ekran içeriği aynı dosyada YOK
A2 □ sahne sayısı: başlık ___ = blok ___ = "Scene N of X" ___
A3 □ süre: ___ sahne × ___ s = ___ s = iddia edilen süre
A4 □ yasaklı sahne tipi taraması yapıldı (biniş-iniş · loş mekâna giriş ·
     ayna · türetilmiş fenomen novum · yokluk novum · jenerik kartı)
     bulunan sahne + karar satırı: ______________________ [D77]
B1 □ doruk anı S___ içinde tarif edildi, sahne arasına düşmüyor
B2 □ bedelli seçim S___, kayıp S___ sahnesinde görülüyor
B3 □ TEMA: ___________ · motife döndüğü sahneler: S___, S___, S___
     (≥3 sahne · B2'nin bedel sahnesi bu listede mi?)          [TEMA §5/§9]
B4 □ kurulum dizisi: _______________ · kurulum sayısı ___ · açı tipi ___
     ardışık çiftler güvenli bantta (≥1 kademe + ≥45°) · şok sayısı ___/2
     derece satırları abartı bandında               [ACI_YAYI §3-4 · KAMERA §5]
     🆕 KURULUM İSKELETİ: ______________ · küme ___/2 · dönüş %___/40
     🆕 dönüş+küme satırları birebir kopya + işaret taşıyor  [ACI_YAYI §4b · §7 ⑥]
B5 □ İSTEK: ______________ (anlamak/görmek/fark etmek DEĞİL)
     ENGEL: ______________ · BEDEL: ____________ S___ ⭐ (B2 ile çapraz)
     MUHATAP: □ ikinci insan  □ kendi geçmiş kararı  □ kendi bedeni
              □ ortamın KALICI değişen parçası
     ⛔ BEDEL sahne numarası taşımıyorsa madde BOŞ    [05 §5① · TUR 4 T4.1]
B5b □ iki insanlı plansa → AYRILIK sahnesi S___ (aynı fikirde OLMADIKLARI an)
B6 □ POLİTİKA SATIRI: en red-riskli kare S___ · nötr tarifi yazıldı
     her önlem ÖNLEM/MALİYET/TELAFİ üçlüsü taşıyor · TELAFİ boş DEĞİL
     milliyet · gerçek kurum · gerçek kişi adı planda YOK   [POLİTİKA §4.3 · KART 12]
C  □ 6 sayısal kilit yazıldı (insan · kask · ölçü · yerçekimi · sıvı · canlı)
D  □ risk sayımı yapıldı: ___/___  (payda: 02_RISK_KARTLARI soru sayısı)
E  □ QA SPEC bloğu plan dosyasına yazıldı

İMZA: bu 18 madde işaretlenmeden üretim başlamaz (A0 · 14.09.2026: 17 → 18).
✅ B5 İNDİ (02.09.2026) — 05_DIKEY_HAT_TESHISI §5① üç gün "ayrılmış"
   kaldı; teşhis 06_HIKAYE_HATTI_TESHISI §3.1'de.
```

---

# 🔗 KAYNAK

Bu listedeki her madde bir gerçek olaydan çıktı:

| Madde | Kaynak film | Nerede belgelendi |
|---|---|---|
| A0 | The Locked Pulse (14.09.2026) | 17/17 madde ✅, hikâye vana tamiri, sahip en sonda gördü · `../../yatay_4_dk_filmler/THE_LOCKED_PULSE/00_ANALIZ/` (çizelge 126/126 sahte kilit) · kapı `../PROMPT_KONTROL/prompt_kontrol.py` ㉙ |
| A1 | The Tidal Hunt | Ders 50 · `../FILM_QA_RAPORLARI/02_HAM_RAPORLAR/THE_TIDAL_HUNT/THE_TIDAL_HUNT_MANTIK_HAM.md` |
| A2 | The Kaleida Crash | `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md` |
| B1 | The Tidal Hunt | aynı ham rapor · "dalga atlaması planda da var" |
| B2 | Kaleida · Ring Walker | `../FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` |
| B3 | The Kaleida Crash | `../FILM_QA_RAPORLARI/01_FILM_RAPORLARI/THE_KALEIDA_CRASH.md` · Tema 5/10 "bedel yok → tema dekoratif kalıyor" · eğilim: ⛔ KAPALI `03_HIKAYE_KALITE_TABLOSU.md` 7/13 ≤5 · kural: `../TEMA_MUHENDISLIGI_KILAVUZU.md` §5/§9 |
| B4 | The Bright Tether (26.08.2026) | 6 kamera satırının 3'ü benzersiz · `../ACI_YAYI_VE_SEKANS_KILAVUZU.md` §3-4 · `../KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` §2/§5 |
| B5 | The Thin Roof · The Sinking Stake | `05_DIKEY_HAT_TESHISI.md` §5① (İSTEK 2/18 · `ENDS OR STOPS: Stops`) · `06_HIKAYE_HATTI_TESHISI.md` §1.1 (İSTEK 8/79 · ENGEL 2/79) · §1.5 (iki gövde, tek kişi) · §3.2 (hasım yok) |
| B6 | The Last Span · Cold Burn · Yerçekimi F1 S8 | 14 üretim reddi · `../FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` · kural: `../POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` · kart: `02_RISK_KARTLARI.md` KART 12 |
| C | Slow Stone vs Inversion/Kaleida | `01_DERS_ETKINLIK_RAPORU.md` §4 |
| E | Low Power · Ring Walker · Kaleida | 4 şartlı/geçersiz QA raporu |
