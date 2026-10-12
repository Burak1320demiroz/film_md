# THE_WRONG_BURN — F2 · diyalog-yazarı · tur 1

```
GİRDİ      ODA/F2_senarist_1.md (tretman A "Arkanı Dön", §2 · §3 · §6 replik ihtiyacı)
OKUNDU     uretim_hatti/BILINEN_TUZAKLAR.md · ARIZA_LISTESI H09 · DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU §1-§6 ·
           SES_VE_DIYALOG_URETIM_KILAVUZU §1-§2a · PROMPT_KONTROL/DIALOGUE_CRITIQUE_PROMPT.md · FILM.md §5
HEDEF      2:00 = 12 çekim × 10 s · bant 6-12 · YAZILAN 11 replik (Bram 8 · Sela 3)
KAYNAK     hepsi kurguda eklenir: Bram = telsiz · Sela = kask içi. Ağız kadrajda replik YOK.
SAHNE=ÇEKİM  S1-S12 = C01-C12 (senarist künyesi)
```

---

## 1. REPLİK TABLOSU — FILM.md §5'e olduğu gibi taşınır

`Saniye` = çekim içindeki başlangıç saniyesi. `Süre` = sesli okunarak ölçüldü, nefes ve tire duraklaması dahil.

| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| 1 | C01 | 3,0 | Bram | telsiz | HUMAN | Lost my jets. | 1,1 |
| 2 | C02 | 2,5 | Bram | telsiz | HUMAN | No, no— don't burn at me! | 1,6 |
| 3 | C03 | 2,5 | Bram | telsiz | HUMAN | Cut it. You're climbing. | 1,8 |
| 4 | C04 | 1,0 | Bram | telsiz | HUMAN | Turn your back on me— and brake. | 2,3 |
| 5 | C04 | 3,9 | Sela | kask içi | HUMAN | Negative. I can see you. | 1,6 |
| 6 | C04 | 6,5 | Bram | telsiz | HUMAN | Sunrise, I'm right in front of you. | 1,9 |
| 7 | C05 | 0,8 | Bram | telsiz | HUMAN | One burn gets you home. Both— might get us home. Your call. | 4,6 |
| 8 | C06 | 1,2 | Sela | kask içi | HUMAN | Sunrise. You be there. | 1,8 |
| 9 | C07 | 1,5 | Sela | kask içi | HUMAN | Bram? | 0,6 |
| 10 | C10 | 4,0 | Bram | telsiz | HUMAN | I heard you. | 1,0 |
| 11 | C11 | 5,0 | Bram | telsiz | HUMAN | Good call. | 0,8 |

```
Sessiz çekimler: C08 · C09 · C12 (yalnız nefes). C07'deki çağrı cevapsız kalır.
Bant: 11 / 6-12 ✅. Söz dengesi bilinçli olarak Bram'dan yana (8/3): filmin teması "göz mü, ses mi" ve
  Bram filmdeki ses. Sela cevaplarını çoğunlukla bedeniyle veriyor: C02 durmaz, C03 ateşi keser,
  C05 başını çevirir, C07 yumruk yapar, C09 elini uzatır, C11 ateşler.
Filmde tek bir isim söylenir: "Bram" (C07). "Sela" adı hiç söylenmez. Bu bilinçli bir protokol
  kırılmasıdır (§4).
⚠ FILM.md'ye taşırken Kaynak sütununa "ağız" kelimesi yazılmaz. film_dogrula.py o kelimeyi görünce
  satırı dudak senkronu sayar (AGIZ regex'i).
⚠ Replik metni hiçbir imaj ya da video promptuna girmez. Özellikle "Sunrise" ve "Bram" kelimeleri
  kadraja yazı olarak basılabilir (BILINEN_TUZAKLAR §C).
```

### NEDEN — her alışverişte ne değişiyor

- **A1 · C01 (1)** — **bilgi:** Bram kendini kurtaramaz, gaz yalnız Sela'da. Sela cevabını sözle değil eylemle verir: C02'de kanca gövdeden çözülmüş, boşta süzülüyor.
- **A2 · C02 (2)** — **ilişki:** göz ile ses ilk kez ayrılıyor. Çaylak, kıdemlinin emrini ateşlemeyi sürdürerek reddediyor.
- **A3 · C03 (3)** — **bilgi:** neden ters gittiği öğreniliyor ("climbing"). Sela isteksizce uyuyor: tıslama replik bittikten 0,8 s sonra kesiliyor.
- **A4 · C04 (4-5-6)** — **karar zemini + ilişki:** sezgiye ters bir talimat geliyor. "Turn your back on me" deyimi bir an "beni bırak" diye duyuluyor; tretmandaki "veda gibi duyulur" engeli kelimenin içinde. Göz ilk kez sesli itiraz ediyor ("I can see you"). Bram tartışmıyor, göze bir görüntü vaat ediyor ("Sunrise").
- **A5 · C05 (7)** — **karar:** Bram eve dönüş yolunu açıyor, bedeli dürüstçe adlandırıyor ("might") ve kararı Sela'ya bırakıyor ("Your call"). Cevap 5,8 s'lik sessizlik ve istasyona dönen baş.
- **A6 · C06 (8)** — **karar:** Sela takası değil sözü cevaplıyor. Eve dönüş seçeneğine hiç değinmeden vaadi geri okuyor ve kıdemliye ilk emrini veriyor. Böylece görüntünün "eve gidiyor" okuması kapanıyor.
- **A7 · C07 (9)** — **ilişki:** protokol çöküyor, filmde söylenen tek isim bu. Cevapsızlık ikinci sınavı başlatıyor: el kumandaya gidiyor ve duruyor.
- **A8 · C10 (10)** — **bilgi + ilişki:** Bram yaşıyor ve gece boyunca duyuyordu. C07'nin cevabı 32 s geç geliyor. "I can see you" (göz, C04) ile "I heard you" (kulak, C10) eşleşmesi temayı adını koymadan kapatıyor.
- **A9 · C11 (11)** — **ilişki:** roller değişiyor; kararı çaylak verdi, kıdemli onaylıyor. C05'teki "Your call" bir yüktü, burada "Good call" takdire dönüşüyor. Yan bilgi olarak, gözün "yanlış yön" dediği itişin doğru olduğu da teyit ediliyor.

---

## 2. ALIŞVERİŞ VE GECİKME TABLOSU (ses tasarımcısı ve kurgu için)

| Alışveriş | Film zamanı | Hamle | Cevap (kanal · içerik) | Gecikme | Okunuş |
|---|:--:|---|---|:--:|---|
| A1 | 0:03,0 | Bram: jets | eylem: kanca boşta (C02) | kesme üstünden | "ben gelirim" |
| A2 | 0:12,5 | Bram: emir | eylem: tıslama sürer, ışık büyür | — | ret |
| A3 | 0:22,5 | Bram: emir + sebep | eylem: tıslama 0:25,1'de kesilir | 0,8 s | isteksiz uyma |
| A4a | 0:31,0 | Bram: talimat | söz: "Negative…" 0:33,9 | 0,6 s | beklenen ret |
| A4b | 0:33,9 | Sela: itiraz | söz: vaat 0:36,5 | 1,0 s | Bram bir nefes alıyor, tartışmıyor |
| A4c | 0:38,4 | Bram: vaat | sessizlik (kesmeyi kapsar) | 2,4 s | açık ret ya da şok → Bram taktik değiştirir |
| A5 | 0:40,8 | Bram: takas + "Your call." | sessizlik + beden: baş istasyona döner | 5,8 s (kesmeyi kapsar) | tartı; beden hareketli olduğu için donma değil |
| A6 | 0:51,2 | Sela: "Sunrise. You be there." | eylem: Sela ateşler 0:53,7 · Bram'dan söz yok | 0,7 s | söz eylemle mühürlenir |
| A7 | 1:01,5 | Sela: "Bram?" | sessizlik: hışırtı + ağır nefes 1:03,0 | 0,9 s → cevapsız | ret değil yokluk |
| A8 | 1:34,0 | Bram: A7'nin cevabı | Sela'nın nefesi takılır 1:35,3 | 32 s / 0,3 s | geç cevap · Sela'nın tepkisi anında |
| A9 | 1:42,5 | Sela: ateşler (Bram'ın nefes aldığı anda) | söz: "Good call." 1:45,0 | 1,0 s (tıslama bitiminden) | onay |

```
SES İPİ — replik değil, ses tasarımına (tretman §6 ile uyumlu)
C01  ~2,0 s  Bram'ın telsizde acılı tek nefesi; replik onun üstüne biner.
C02  Sela'nın kask içi hızlı nefesi ateşleme boyunca. Filmde ilk kez onun bedenini duyuyoruz, sesi henüz yok.
C03  Bram'ın nefesi C02'den ağır; repliğin iki cümlesi arasında nefes var.
C05  Bram'ın nefesi "home." ile "Both—" arasında. Tire bir duraklama değil, alınamayan nefes.
C07  Bram'ın hattı açık: tıkırtı yok, yalnız ağır nefes. Diğer iletimlerinde başta ve sonda tek yumuşak tıkırtı var.
C11  ~2,0 s  Bram'ın konuşmadan önce aldığı nefes duyulur; Sela 0,5 s sonra ateşler. "Bram konuşamadan" anı
     kelimesiz kurulur, "Turn your back" söylenmeden geri döner.
C12  Yalnız Sela'nın titrek nefesi.
MÜZİK  C04-C07 arası replikler ve sessizlikler müzikle doldurulmaz. C05'in 4,6 s'lik sessizliği ve C07'nin
       cevapsız hışırtısı anlamın kendisi.
```

---

## 3. F3'E KADRAJ ŞARTLARI — replik ağızla çakışmasın

Kaynak "kask içi" ise ağız okunmamalı. Tretman §3'teki üç çekimde Sela'nın yüzü görünebiliyor:

| Çekim | Ölçek | Replik | Risk | Önerilen çözüm (F3 · yönetmen) |
|:--:|---|---|---|---|
| C05 | yakın, yüz | Bram konuşuyor, Sela dinliyor | düşük | Dinleyenin ağzı kapalı kalır, video promptuna yazılır ("lips closed, no mouth movement while the radio voice plays"). Baş dönüşü "Your call"un son hecesinde başlar (DIYALOG §4: dinleyenin cevabı replik bitmeden bedende başlar). |
| C06 | orta | 8 · Sela | orta | Sela alçak güneşe dönük, güneş solda. Vizördeki güneş parlaması yüzün alt yarısını örter. Profil çekimde ağız okunuyorsa replik yeri değişmez, kadraj değişir. |
| C07 | yakın, yüz + el | 9 · Sela | **yüksek** | Önerim: ay ışığı yalnız göz hizasına ve bir yanağa düşer, vizörün alt yarısı gece Dünyası'nın şehir ışıklarını yansıtır. Ağız okunmazsa "Bram?" kask içi kalır. **Okunursa:** "ağız kadrajda"ya çevirmek önerilmez. Merkez an değil (merkez C06), ayrıca Sela'nın sesi modele geçer ve C04/C06'daki kayıtlı sesle kimliği tutmaz (BILINEN_TUZAKLAR B11). Kadraj değişir. |
| C10 | yakın, kanca | 10 · Bram | düşük | Bram'ın vizörü kadraj dışında kalır ya da kehribar lamba parlaması yüzünü örter. |

C04 omuz üstünden ve C11 geniş planda çekildiği için risk yok. C08, C09 ve C12'de replik yok.

---

## 4. KONUŞMA PROFİLLERİ

### BRAM — kıdemli EVA ortağı (telsiz)
```
CÜMLE     2-6 kelime, özne düşer ("Lost my jets."). Nefes repliği ikiye böler. C01'den C05'e her replik
          biraz daha ağır ve yavaş (tretman: çarpmanın etkisi). Tek bağırış C02'de.
SÖZCÜK    Sade dil, az jargon (burn · brake · climbing · call). Protokol kalıbı kullanmaz (copy ve negative
          yok) çünkü kuralı içselleştirmiş. Kimseye adıyla seslenmez.
ALIŞKANLIK  Geleceği şimdiki zamanla söyler; kesinlik böyle duyulur ("Sunrise, I'm right in front of you.").
          Kırıldığı iki an tasarımın parçası: C05 "might", filmdeki tek belirsizliği (dürüstlük = bedel).
          C10 "I heard you", öznesiz konuşan adamın ilk kez "I" demesi.
```
**SES PROFİLİ**
```
YAŞ       52 civarı
TINI      alçak bariton, pürüzlü. Göğüs darbesinden sonra her cümle nefese mal oluyor; hafif hırıltı.
AKSAN     General American, düz Upper-Midwest ünlüleri
HIZ       yavaş-orta (~2,5 kelime/s). C02 tek hızlı replik. C05'te cümle içi nefes molaları.
BENZETME  "a mountain guide with cracked ribs, talking his client down the last pitch"
KAYIT ARACI (EN)  Male, early fifties, low gravelly baritone, flat Midwestern American. Calm and dry,
          short on breath from a chest injury: every sentence costs him air. Never raises his voice
          except once. Understates everything.
```

### SELA — çaylak (kask içi)
```
CÜMLE     Eğitimde öğrendiği tam kalıplar, baskı altında kısalıyor: 5 kelime (C04) → 4 (C06) → 1 (C07).
SÖZCÜK    Kitaptan telsiz dili (Negative · readback). Protokol onun zırhı; kısaltmalar doğal.
ALIŞKANLIK  Geri okuma (readback): duyduğu talimatın anahtar kelimesini tekrarlar ("Sunrise." ← C04).
          Kırılma C07'de: protokol düşer, filmde söylenen tek isim "Bram?" olur.
```
**SES PROFİLİ**
```
YAŞ       29 civarı
TINI      berrak orta alto. Gerildiğinde üst perdede daralıyor; kask içinde yakın ve kuru, filtresiz.
AKSAN     nötr General American, keskin ünsüzler (eğitimli telsiz diksiyonu)
HIZ       C04'te hızlı ve kesik. C06'da yavaşlıyor ve her kelimeyi ayrı koyuyor. C07'de fısıltıya yakın.
BENZETME  "a rookie paramedic holding her voice level on the radio during her first bad call"
KAYIT ARACI (EN)  Female, late twenties, clear mid-range alto, neutral American with crisp radio
          diction. Holds procedure like a handrail; the steadiness is effort you can hear. Close,
          dry, inside-the-helmet sound.
```

**Swap testi:** iki konuşanın adları silindiğinde de replikler ayırt ediliyor. "Negative" ve readback yalnız Sela'da var. Öznesiz emir ve şimdiki zamanla verilen söz yalnız Bram'da. Tek bağırış ve tek isim de ayrı ağızlarda.

### Okuma notları (kayıt)
- **2** "No, no—" nefessiz ve üst üste söylenir. İkinci "no" birinciden yüksek çıkar.
- **4** Tire bir nefes kadar sürer. "Turn your back on me" önce "beni bırak" gibi duyulur, "and brake" anlamı düzeltir. Duraklama kısaltılmaz.
- **5** "Negative" hızlı ve resmî söylenir. "I can see you" bir ton aşağıda, neredeyse yalvarır gibi.
- **7** Tire alınamayan bir nefestir, efekt için konmuş bir duraklama değil. "might" vurgulanmaz, düz söylenir. "Your call." konuyu kapatır, soru tonuyla bitmez.
- **8** "Sunrise." readback düzlüğünde. "You be there." titrek ama emir kipinde; filmin doruktaki tek doğrudan cümlesi (CLIMAX-DIRECT, C06).
- **9** Yarı sesli; telsizin açık olduğunu bilen ama cevap beklemeyen biri gibi.
- **10** Uzun bir nefesin ucunda söylenir. "I" hafif vurgulu.
- **11** Kuru söylenir. Altında tek bir nefes-gülüş olabilir; gülüş kelimelerin üstüne çıkmaz.

---

## 5. TRETMANDAN FARKLAR (senaristin taslak anlamı → replik)

| No | Tretman | Replik | Neden |
|:--:|---|---|---|
| 1 | "Jetlerim gitti." | Lost my jets. | Anlam aynı. Bram'ın öznesiz ve hafife alan sesiyle söylenmiş hâli. |
| 3 | "Dur. Yükseliyorsun." | Cut it. You're climbing. | "Stop", C02'deki "No, no" ile aynı emri tekrarlardı. "Cut it" ateşi kesme emri ve yeni bir emir. |
| 4-6 | talimat + söz tek replik, sonra "Seni görüyorum." | talimat → itiraz → söz | Tek replikte iki bilgi vardı (T3 OVERLOADED). Söz artık itiraza verilen cevap: göze bir görüntü vaat ediliyor. Böylece "I can see you" ile "I heard you" eşleşmesi kuruluyor. Bant içinde +1 replik. |
| 7 | "…İkisi beni alır ve ikimizi eve getirir. Yedeksiz." | …Both— might get us home. Your call. | "Yedeksiz" yerine tek kelimelik risk geldi: "might". Kararın devredildiği "Your call" söylendi ve C11'e geri dönüş bağı kuruldu. "One burn" bir sayım, kesin veri değil; görsel eşi C03'teki göstergede (2/2). Eleştirmen MISPLACED-NUMBER derse yedek: "This gets you home. All of it— might get us home. Your call." |
| 8 | "Önümde ol." | Sunrise. You be there. | "Be in front of me" çeviri kokuyor. Readback hem Sela'nın alışkanlığı hem söze verilen cevap; eve dönüş seçeneğini hiç anmaması seçimin kendisi. |
| 10 | "Dönmedin." | I heard you. | H09: "dönmedin" C08'de görüleni söylüyordu. Yeni replik görünmeyeni taşıyor (Bram uyanıktı ve duyuyordu) ve C07'deki cevapsız çağrıyı cevaplıyor. |
| 11 | "Ben de tam bunu diyecektim." | Good call. | Kısa ve kuru onay. C05'teki "Your call" anlam değiştirerek geri dönüyor. "Bram konuşamadan" anı kelimeyle değil, C11'de duyulan nefesle kuruluyor. |

**Silme testi — düşen adaylar:** C08'de "There you are." (görüneni söylüyor, H09). C10'da Sela'nın "Copy." cevabı (hiçbir şey değiştirmiyor; nefesin takılması daha çok taşıyor). C12'de "Sunrise" ile kapanış (görüneni söylüyor; doruk sessiz kalıyor). C02'de Sela'nın sesli itirazı (göz ile sesin ilk sesli çatışması C04'e ait, dramaturg B15). Kalan 11 replik testi geçti: hiçbiri ekrandakini söylemiyor, her biri bilgi, ilişki ya da karardan birini değiştiriyor, hiçbir bilgi iki kez geçmiyor.

**Geri dönüş zincirleri:**
- "Sunrise" (C04 söz → C06 readback → C08 görüntüyle ödenir → C12 ikinci gün doğumu, sessiz)
- "Your call" → "Good call" (C05 → C11)
- "Bram?" → "I heard you" (C07 → C10)
- "I can see you" ↔ "I heard you" (göz ↔ kulak)
- "Turn your back on me" (C04) → C11'de söylenmeden, C12'de ikisi istasyona sırtları dönük varıyor
