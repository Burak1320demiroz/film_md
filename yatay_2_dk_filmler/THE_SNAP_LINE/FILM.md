# 🎬 THE_SNAP_LINE — Kopma Hattı

```
FILM           THE_SNAP_LINE
FORMAT         yatay 16:9
HEDEF_SURE     2:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  var
MEDYA          ~/film_medya/THE_SNAP_LINE/
DIYALOG        model sesi
URETIM         Google Flow (web) · QA Gemini uygulaması
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `DIYALOG` = **model sesi** (sahip kararı 21.10.2026): diyalog kurguda eklenmez; her replik videoda model sesiyle üretilir (film_dogrula M).
> `REPLIK` ve `MUZIK` varsayılan **var**: filmlerde akıcı diyalog, ses ve efekt olur (sahip kararı, 06.10.2026).
> `yok` yalnız hikâye bunu istiyorsa, gerekçesi §5'in altına yazılarak.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.

---

## 1. HİKÂYE

```
LOGLINE   Arızalanan dalış çanı kendisini hızla yukarı çekerken, bir doygunluk dalgıcı ölümcül dekompresyondan kaçınmak için kendi yaşam hattını kesip zifiri karanlık tabana düşer.
AMAÇ      Gerilen göbek kordonunu hidrolik makasla kesip tabandaki acil durum sığınağına ulaşmak.
ENGEL     Çanın kilitlenen vinci 500 kg çekme gücüyle kordonu gerer; dalgıcın gövdesi tabandan metrelerce yukarı savrulur.
KARAR     Telsizdeki fren arızası uyarısıyla kordon kesme tetiğini sıkar · sahne 8
SONUÇ     Kablo patlayarak kopar; dalgıç tabandaki sarı çamurun içine sertçe düşer, acil durum tüpünün vanasını açar ve karanlıkta tek başına yatar.
BEDEL     Ana oksijen, sıcak su ve iletişim kordonunu kaybeder; sol omzu askı yükünden ezilir · sahne 10
TEK SORU  Miller kabloyu kesip karanlığa düşmeyi göze alabilecek mi?
SEÇİM     Fable: aday A · 22.10.2026 · gerekçe: ODA/F1_secim.md
SAHİP     ONAY (Aday A) · 22.10.2026
```

### KARAKTER — MILLER (Doygunluk Dalgıcı)
- **İSTEK:** Çanın vinci kopmadan acil durum kordonunu kesip tabanda sabit kalmak — boru flanşı C04'te, hidrolik makas C07'de kadrajda. (KANITLI)
- **BASKI TEPKİSİ:** Kontrol eder: her engelde göğsündeki analog derinlik saatine bakar, hamle yapmadan bir an durur (C02 · C04 · C06). (HİPOTEZ)
- **ALIŞKANLIK:** Göğüs hava valfine sağ eldiveniyle iki kez vurur (C02 · C04 · C06'da birebir aynı; C08'de kesme mandalını tutarken başlar ama tamamlayamaz, jest kırılır). (HİPOTEZ)
- **ZAAF:** Sol omzundaki eski tendon hasarı; gerilim arttıkça sol kolu yükü taşıyamaz, aşağı doğru sarkar ve titrer (C04 · C06 · C10). (HİPOTEZ)
- **İLK ↔ SON:** C01'de yüzeye bağlı ana kordona tutunur · C12'de taban çamurunda tek başına yatarak kendi acil durum tüp vanasını tutar. (HİPOTEZ)

## 2. TRETMAN

<!-- sahne başına bir satır; her satır öncekinden doğar (seçim ya da başarısız deneme) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Kuzey Denizi 310 m okyanus tabanında, petrol boru flanşındaki analog basınç manometresinin ibresi kırmızı banda dayanır; flanş contasından şiddetli beyaz kabarcık fışkırır ve çelik boru inler. | Düzenli çalışma bozulur; sistemik basınç alarmı başlar. |
| S2 | 0:10–0:20 | Ağır sarı dalgıç kaskının vizörüne yakın planda sarı acil durum ikaz ışığı yanar; camın içindeki buğulanan solukta Miller'ın gözleri büyür; sağ eldiveniyle göğüs valfine iki kez vurur. | Tehlike insana geçer; Miller sorunu algılar ve panik kontrolü yapar. |
| S3 | 0:20–0:30 | Miller'ın sırt askısından yukarı uzanan kalın sarı göbek kordonu (umbilical) aniden gerilerek yay gibi geriye fırlar; Miller'ın çizmeleri taban çamurundan 1 metre yukarı havalanır. | Sorun lokal sızıntıdan ölümcül yukarı çekilme krizine dönüşür (kapak anı). |
| S4 | 0:30–0:40 | Miller havada savrulurken sağ eliyle boru flanşının emniyet halkasını yakalar; gerilen kordon sol omzunu geriye doğru çekerken kask telsizine bağırır; göğüs valfine iki kez vurur. | Miller zemin temasını kaybeder; kordon ile boru arasında mekanik olarak sıkışır. |
| S5 | 0:40–0:50 | Çan vinç tamburunun su altındaki dişlilerinde sarı kılavuz kablosu çapraz sarılarak kilitlenir; hidrolik fren balatasından kıvılcım ve buhar kabarcıkları fışkırarak tambur kontrolsüzce dönmeyi sürdürür. | Yüzeyden vinci durdurma ihtimali tamamen biter; mekanik kilitlenme kesinleşir. |
| S6 | 0:50–1:00 | Kask içi manometrede derinlik ibresi 310'dan 270 metreye hızla tırmanır; telsizden kontrolörün uyarısı duyulurken Miller sol omzunun acısıyla bükülür; göğüs valfine iki kez vurur. | Vurgun (dekompresyon) sınırına yaklaşılır; kalan süre 40 saniyeye iner. |
| S7 | 1:00–1:10 | Miller flanş halkasını bırakıp sağ bacağındaki acil durum kılıfından ağır çelik hidrolik makası çeker; kask fenerini gerilen sarı kordona çevirir. | Pasif tutunma terk edilir; kordonu kesme eylemi başlatılır. |
| S8 | 1:10–1:20 | Telsizdeki son uyarı gelir; Miller hidrolik makasın çenelerini sarı kordonun üzerine yerleştirir; göğsüne vurma alışkanlığı başlar ama tamamlamadan makasın kesme mandalını sıkar (KARAR). | Karar verilir; alışkanlık kırılır ve geri dönüşsüz kesme işlemi başlar. |
| S9 | 1:20–1:30 | Makasın hidrolik bıçakları kordonun kauçuk ve çelik örgüsünü ezer; delinen sıcak su ve oksijen hortumlarından fışkıran beyaz gaz sütunu fenerin ışığında dev bir girdap oluşturur. | Ana yaşam desteği fiziksel olarak parçalanır; kadraj beyaz girdapla perdelenir. |
| S10 | 1:30–1:40 | Kordon büyük bir patlama kabarcığıyla kopar (BEDEL); kopan üst uç hızla yukarı fırlar; sol omzu askı kopmasından geriye savrulan Miller okyanus karanlığına dikey serbest düşüşe geçer. | Bütün yüzey bağlantısı kopar; dalgıç yerçekimiyle zifiri karanlığa düşer. |
| S11 | 1:40–1:50 | Düşüş sırasında Miller sol eliyle göğsünü tutup sağ eliyle sırtındaki bağımsız acil tüpün vanasını sonuna kadar çevirir; kaskın içine soğuk gaz tıslaması dolar. | Boğulma engellenir; 10 dakikalık bağımsız acil hava devresi çalışır. |
| S12 | 1:50–2:00 | Miller 310 m okyanus tabanındaki sarı silt çamuruna sertçe çarparak sırtüstü durur (SONUÇ); kask feneri yukarıdaki karanlık suyu aydınlatır; acil durum tüp saati 10 dakikayı sayarken tek başına yatar. | Film biter: Yaşam kordonu feda edilmiş, ölümcül dekompresyon durdurulmuş, tabanda sınırlı havayla hayatta kalınmıştır. |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Karakter (MILLER) — TEK SAYFA: önden tam boy sarı dalgıç kıyafeti · yandan · arkadan · vizör yakın ¾ · durum: acil ışık altında buğulu kask içi | `1.MILLER_v1.png` | v1 | `4bdf14e932a0` | ⬜ | C02, C03, C04, C06, C07, C08, C10, C11, C12 |
| 2 | Mekân (SUALTI_TABAN) — TEK SAYFA: 310 m okyanus tabanı silt çamuru · çelik petrol boru flanşı · manometre · zifiri karanlık su | `2.MEKAN_v1.png` | v1 | `e151d23eed54` | ⬜ | C01, C03, C04, C05, C10, C12 |
| 3 | Araç (HIDROLIK_MAKAS) — TEK SAYFA: ağır çelik endüstriyel kablo kesici çeneler · sarı basınç hortumu · emniyet tetiği | `3.MAKAS_v1.png` | v1 | `fefc7bc60449` | ⬜ | C07, C08, C09 |

```
SHA-256: shasum -a 256 ~/film_medya/THE_SNAP_LINE/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: bir karakterin açıları, yüz yakını ve durum değişimleri aynı görselde paneldir; "SELA_yuz",
"SELA_arka" gibi ikinci dosya açılmaz (film_dogrula hata). Yeni panel gerekirse sayfa yeniden üretilir, sürüm artar.
```

### KİMLİK CÜMLELERİ (16.10.2026 · F3p'de goruntu-yonetmeni yazar, pilot yoksa F5 G01 · Görsel promptta BİREBİR)

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | yüz | a hardened commercial saturation diver in his forties with exhausted eyes and stubble visible through a condensation-fogged helmet visor |
| 1 | giysi + işaret | a bulky deep-sea yellow diving suit with one thick black chevron band across the left shoulder, the only marking on the suit |
| 2 | nesne | a massive industrial subsea pipeline flange covered in dark marine silt with an analog brass pressure gauge mounted on its top seam |
| 3 | araç | a heavy hydraulic steel umbilical cable-cutter with dual forged serrated shearing jaws and a reinforced rubberized trigger grip |

```
Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (5/5 filmde
kimlik kayması, ARASTIRMA/16 Y1-Y3). İşaret: sayı + taraf + konum + "the only marking". Nesne: biçim + ölçü + taraf.
film_dogrula DERS Y2: referansı eklenen çekimde hiçbir parçası birebir geçmeyen özneyi gösterir (uyarı).
ORTAK GÖRÜNÜM cümlesi (varsa) yalnız film boyu değişmeyeni taşır: kimlik + doku/stil. Işık, su, gezegen, ses mekân ya da çekim
cümlesine gider (DERS Y6).
```

## 4. ÇEKİM LİSTESİ

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Okyanus tabanındaki boru flanşında kritik basınç anomalisi başlar. | Zifiri karanlık su altında dev çelik boru flanşı üzerindeki analog basınç saatinin ibresi titreyerek kırmızı bölgeye vurur; flanş contasından beyaz kabarcık jeti fışkırır. | Orta-yakın plan, sabit kamera | Boru soldan sağa, ibre saat yönünde | 10 | Frames to Video | Gaz jeti tutarlılığı → karanlık arka planda net sınırla tutulur | 2.MEKAN | G01 | ⬜ | — | — | — |
| C02 | Dalgıç arızayı tespit eder ve telsizden ilk bildirimini yapar. | Sarı dalgıç kaskının vizörüne yakın planda sarı ikaz ışığı parlar; camın içindeki buğulanmada Miller'ın gözleri açılır; sağ eldiveniyle göğüs valfine iki kez vurur. | Yakın yüz/vizör planı, hafif alttan açı | Kask cepheden, bakış sol manometreye | 10 | Frames to Video | Yüz detayı ve buğu → model sesi repliği video içinde üretilir | 1.MILLER | G01 | ⬜ | — | — | — |
| C03 | Dalış kordonu kilitlenip dalgıcı kontrolsüz yukarı çekmeye başlar. | Dalgıcın sırt askısından yukarı uzanan kalın sarı göbek kordonu yay gibi gerilip titrer; dalgıcın çizmeleri taban çamurundan koparak metrelerce yukarı havalanır. | Geniş plan, dikey tilt yukarı | Dalgıç tabandan dikey yukarı çekilir | 10 | Frames to Video | Hızlı dikey savrulma → dalgıcın gövdesi kadraj merkezinde tutulur | 1.MILLER · 2.MEKAN | G01 | ⬜ | — | — | — |
| C04 | Dalgıç boruya tutunmaya çalışır ancak gerilim omzunu ezer. | Havada asılı kalan Miller sağ eliyle çelik boru flanşının emniyet halkasını kavrar; gerilen sarı kordon sol omzunu geriye bükerken göğüs valfine iki kez vurur. | Orta plan, açılı yan profil | Miller sağa uzanır, kordon sola yukarı çeker | 10 | Frames to Video | El-flanş teması → el halkayı zaten kavramış başlangıç karesiyle girilir | 1.MILLER · 2.MEKAN | G01 | ⬜ | — | — | — |
| C05 | Çanın vinç tamburundaki kilitlenme yüzey yardımını imkansız kılar. | Çan vinç tamburundaki çelik kablo çapraz sarılarak kilitlenir; hidrolik fren kampanasından beyaz buhar kabarcıkları fışkırarak tambur zorlanarak dönmeyi sürdürür. | Yakın detay planı, hafif yukarı açı | Tambur dikey eksende döner | 10 | Frames to Video | Tambur dişlileri → tek nesneye odaklanmış basit mekanik hareket | 2.MEKAN | G01 | ⬜ | — | — | — |
| C06 | Hızlı yükseliş dalgıcı ölümcül dekompresyon sınırına yaklaştırır. | Miller'ın kask içi derinlik göstergesinde ibre 310'dan 270 metreye hızla tırmanır; Miller acıyla iki büklüm olur, sol kolu askı yükünden aşağı sarkar. | Göğüs ve kask yakın planı, sarsıntılı kamera | Gövde hafif sola eğik | 10 | Frames to Video | İbre hareketi ve beden gerilimi → sol koldaki zaaf sarkması görünür | 1.MILLER | G01 | ⬜ | — | — | — |
| C07 | Dalgıç pasif tutunmayı bırakıp kordonu kesmek için makası çeker. | Miller flanş halkasını bırakır; sağ elini bacağına uzatarak ağır çelik hidrolik makası kılıfından çıkarır ve kask fenerini gergin sarı kordona yöneltir. | Orta-yakın bel planı, hafif alttan | Sağ el bacağa iner, makas yukarı kalkar | 10 | Frames to Video | Alet çekme teması → makas kılıftan çıkmış elde başlar | 1.MILLER · 3.MAKAS | G01 | ⬜ | — | — | — |
| C08 | Dalgıç makasın çenelerini kordona geçirir ve mandalı sıkar (KARAR). | Miller hidrolik makasın çelik çenelerini sarı kordonun üzerine yerleştirir; göğsüne vurma alışkanlığı başlar ama tamamlamadan makasın kesme mandalını sıkar. | Yakın plan, alet ve kordon odaklı | Makas soldan sağa kordonu kavrar | 10 | Frames to Video | Makas-kablo kaynaşması (BT §A) → çeneler oturmuş başlar | 1.MILLER · 3.MAKAS | G01 | ⬜ | — | — | — |
| C09 | Bıçaklar kordonu ezer; fışkıran basınçlı gaz görüntüyü perdeler. | Makasın hidrolik bıçakları kalın kordonu ezerken delinen hortumlardan yüksek basınçlı beyaz gaz ve sıcak su püskürür; fener ışığında devasa bir kabarcık girdabı kadrajı kaplar. | Yakın detay planı | Gaz jeti merkezden dışarı doğru patlar | 10 | Frames to Video | Akışkan perdeleme → beyaz kabarcık jeti kesme anının temasını gizler | 3.MAKAS | G01 | ⬜ | — | — | — |
| C10 | Kordon kopar; omuzu çıkan dalgıç karanlığa serbest düşer (BEDEL). | Sarı kordon büyük bir kabarcık patlamasıyla ikiye ayrılır; kopan üst uç hızla yukarı fırlar; sol omuz bağı kopan Miller yerçekimiyle okyanus tabanına doğru dikey düşer. | Geniş plan, dikey takip | Kopan kablo yukarı, Miller aşağı dikey düşer | 10 | Frames to Video | Kopma anı → kablo iki parça halinde başlar, aradaki mesafe açılır | 1.MILLER · 2.MEKAN | G01 | ⬜ | — | — | — |
| C11 | Dalgıç düşüş sırasında sırtındaki bağımsız acil tüpün vanasını açar. | Karanlıkta aşağı süzülen Miller sol eliyle göğsünü bastırırken sağ eliyle sırtındaki acil durum tüpünün vanasını yakalayıp sonuna kadar çevirir; kask içine beyaz soğuk gaz dolar. | Orta-yakın göğüs planı, düşüş açısı | Miller sırtüstü dikey iner, sağ el geriye uzanır | 10 | Frames to Video | Sırt vanası çevirme → el zaten vana üstünde başlar | 1.MILLER | G01 | ⬜ | — | — | — |
| C12 | Dalgıç okyanus tabanına çakılır; acil durum sayacıyla bekler (SONUÇ). | Miller 310 m okyanus tabanındaki sarı silt çamuruna çarparak sırtüstü durur; kask feneri yukarıdaki karanlık suyu aydınlatır; acil hava manometresi 10 dakikayı sayarken tek başına yatar. | Geniş taban planı, yavaş geri çekilme | Miller kadraj merkezinde hareketsiz yatar | 10 | Frames to Video | Çamur sıçraması → darbe anı ve yavaşça durulma | 1.MILLER · 2.MEKAN | G01 | ⬜ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE.
  Ritim süreyle değil çekim içi hareket ve kadraj/ölçek değişimiyle kurulur (ARIZA H10).
Flow modu: Frames to Video · Ingredients to Video · Text to Video (yalnız kimliksiz çekim).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir" (örn. T01 → temas kadraj dışı, sonrası C05).
Grup: PROMPTLAR/<Grup>.md (8-12 çekim). Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Zincir · Baş. karesi · Bitiş karesi: yönetmen "—" bırakır; sahneleme odası (§F3b) doldurur.
  Zincirli çekim: Zincir = Z1 · Baş. = Z1.0 · Bitiş = Z1.1 (B) — ya da Baş. = "son:C02" (A) / "t:C02@4.2" (A′).
  Zincirli çekim de 10 s'dir → zincir yalnız KLIP_SURESI ≥ 10 ölçülürse kurulur; zincir en çok 4 halka; her halka yeni bir bilgi taşır.
DELTA BÜTÇESİ (her halka, Zk.n → Zk.n+1): aynı objektif · ışık · set │ en çok bir basit kamera
  hareketi │ özne yalnız ulaşabileceği mesafede │ kadraja nesne/kişi girip çıkmaz │ el-nesne
  teması değişmez │ durum değişimi küçük ve tek. Aşılırsa model iki kareyi eritir (morf).
```

### AÇILIŞ — ilk 30 saniye (`uretim_hatti/ILK_30_SANIYE_KILAVUZU.md` §2 · yonetmen F3'te doldurur)

| Saniye | Çekim | Sorun ya da beklenmedik hareket | İnsan (beden · el · yüz) | Replik · ekran yazısı | Kapak bağı | Sesi kapalı okunur mu |
|---|:--:|---|---|---|---|:--:|
| 0-10 | C01 | Flanştaki manometre ibresi kırmızıya vurur, contadan beyaz kabarcık jeti fışkırır. | yok | yok | vaadin dünyası: 310 m okyanus tabanı, basınç tehlikesi, çelik boru | evet |
| 10-20 | C02 | Sarı kask vizöründe acil ikaz ışığı; camın içinde gözler büyür, göğsüne iki kez vurur. | yüz · el | "Bell, confirm tension on my umbilical. I've got drift." | — | evet |
| 20-30 | C03 | Kordon yay gibi gerilip çeker; dalgıcın gövdesi taban çamurundan havaya savrulur. | beden · ayaklar | yok | kapak anı: gerilen sarı kordon ve boşlukta savrulan dalgıç | evet |

```
İlk 30 s'de yok: logo · "sunar" kartı · siyah ekran · karartmadan açılma · saf manzara · görüntüde yazı ·
  kalabalık · hızlı kamera · karmaşık el-nesne teması · kusurlu ama "gerekli" çekim.
Sapma serbest; gerekçesi bu tablonun altına tek satır yazılır.
```

## 5. REPLİKLER

<!-- REPLIK yok ise tablo boş kalır -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R1 | C02 | 0:14 | Miller | model sesi (kask içi) | HUMAN | "Bell, confirm tension on my umbilical. I've got drift." | 4.0 s |
| R2 | C04 | 0:33 | Deck Control | model sesi (telsiz) | HUMAN | "Miller, winch hydraulic brake just blew. It's on free spool!" | 5.0 s |
| R3 | C06 | 0:52 | Deck Control | model sesi (telsiz) | HUMAN | "Pressure delta is critical! You hit the bends in forty seconds!" | 5.0 s |
| R4 | C06 | 0:56 | Miller | model sesi (kask içi) | HUMAN | "Cut the topside power! CUT IT!" | 3.0 s |
| R5 | C08 | 1:12 | Deck Control | model sesi (telsiz) | HUMAN | "She won't trip, Miller! You have to cut away!" | 4.0 s |
| R6 | C11 | 1:44 | Miller | model sesi (kask içi) | HUMAN | "Severed... on bailout air... going down." | 4.0 s |

```
Kaynak: model sesi (telsiz | kadraj dışı | kask içi | makine | kayıt | ağız kadrajda) — diyalog kurguda eklenmez (sahip kararı 21.10.2026)
        → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda üretir; ≤ 8 s (ağız kadrajda ≤ 5 s, sayı yok);
        klip sesi yalnız replik için filme girer (timeline klip_sesi), yatak planda
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik
Konuşma ve ses profilleri: ODA/F2_diyalog-yazari_<n>.md
```

## 6. SES PLANI — klibin sesi kullanılmaz, yalnız §5 replikleri klipten gelir

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| C01 | Ortam (Y1) · SFX (E01, E02) | J-cut (C02 nefesi 0.8 s önce) | Manometre ve kabarcık jeti |
| C02 | Ortam (Y1) · Replik R1 · SFX (E03, E04) | L-cut (telsiz tıkırtısı) | Kask içi vizör buğusu |
| C03 | Ortam (Y1, Y2) · SFX (E05) | — | Kordon yay gibi gerilir |
| C04 | Ortam (Y1, Y2) · Replik R2 · SFX (E06, E07) | J-cut (vinç gıcırtısı) | Flanşa tutunma |
| C05 | Ortam (Y1, Y2) · SFX (E08) | L-cut (mekanik inilti) | Vinç tamburu kilitlenir |
| C06 | Ortam (Y1, Y2) · Replik R3, R4 · SFX (E09, E10) | L-cut (nefes/inilti) | İrtifa tırmanışı, omuz hasarı |
| C07 | Ortam (Y1, Y2) · SFX (E11) | — | Makas kılıftan çekilir |
| C08 | Ortam (Y1, Y2) · Replik R5 · SFX (E12, E13) | — | Makas kordona takılır |
| C09 | Ortam (Y1, Y2) · SFX (E14, E15) | Ani patlama | Tazyikli gaz perdesi |
| C10 | Ortam (Y1) · SFX (E16, E17) | MÜZİKSİZ AN · 1.5 s boşluk | Kordon kopar, serbest düşüş |
| C11 | Ortam (Y1) · Replik R6 · SFX (E18, E19) | J-cut (soğuk gaz tıslaması) | Acil tüp açılır |
| C12 | Ortam (Y1) · SFX (E20, E21) | L-cut (soluk yatağa akar) | Silt çamuruna çarpış, bekleme |

```
Ortam: 310 m okyanus tabanı kütlesel su basıncı · hava taşımaz, kask içi ve telsiz sesi taşır
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_1.md
```

### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | Sualtı Taban | C01–C12 | Continuous deep ocean sub-bass ambient rumble at 310 meters with distant muffled metallic pipe groans | −18 dB | `yatak_sualti_taban.wav` |
| Y2 | Kordon Gerilim | C03–C09 | Strained taut steel wire hum and hydraulic winch motor whine slowly rising in acoustic pitch | −22 dB | `yatak_kordon_gerilim.wav` |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01 → C02 | kesme | J-cut (0.8 s nefes) | Manometreden kask içine geçerken Miller'ın soluğu kesmeden önce girer |
| C02 → C03 | kesme | L-cut (0.5 s telsiz) | Kask telsiz mandal sesi gerilen kordon planına akar |
| C03 → C04 | kesme | — | Dalgıcın savrulması ile flanşı yakalaması sert kesmeyle vurulur |
| C04 → C05 | kesme | J-cut (0.6 s vinç gıcırtısı) | Tamburun arıza iniltisi dalgıç planının sonunda duyulmaya başlar |
| C05 → C06 | kesme | L-cut (0.5 s mekanik inilti) | Vinç tambur sesi derinlik saatine akar |
| C06 → C07 | kesme | L-cut (0.4 s nefes) | Miller'ın acı iniltisi makasa uzanışa sarkar |
| C07 → C08 | kesme | — | Makasın kordona oturması mekanik sert vuruşla kesilir |
| C08 → C09 | kesme | — | Tetiğin sıkılması anında kabarcık patlamasına ani geçiş |
| C09 → C10 | kesme | ani patlama ardından 1.5 s boşluk | Kordon koptuğunda hava/su patlaması ve hemen ardından derin düşüş sessizliği |
| C10 → C11 | kesme | J-cut (0.5 s gaz tıslaması) | Acil durum tüpünün devreye girişi düşüş planında başlar |
| C11 → C12 | karisim (0.5 s) | L-cut (0.8 s düzenli soluk) | Acil havanın tıslaması taban çamuruna çarpışa ve finale akar |

## 7. MÜZİK PLANI

```
OKUMA        İzleyici bu filmi 310 metre derinlikte insan yapımı devasa makinelerin çöküşü karşısında tek başına alınan ölümcül bir karar olarak okumalı.
MÜZİKSİZ     C10 (1:30–1:40) kordonun koptuğu an müzik tamamen susar; kopma şok dalgası ve derin okyanus sessizliği tek başına bırakılır.
VURUŞ/SUSMA  0:00 drone başlar · 0:20 nabız vuruşu girer · 1:10 doruk noktası tırmanışı · 1:30 tam susma · 1:40 soğuk drone geri dönüşü
FLOW MUSIC   faz 8'de: ODA/F8_besteci_1.md
```

### MÜZİK PROMPTU — Flow Music'e yapıştırılır
```text
A dark, claustrophobic industrial ambient score for a deep-sea saturation diving crisis, exactly 120 seconds in length. The piece opens with an ominous 35 Hz sub-bass drone and distant metallic resonance simulating massive oceanic water pressure. At 20 seconds, a cold, tense mechanical pulse enters, mimicking an accelerating heartbeat mixed with hydraulic strain, steadily building in acoustic tension and frequency through 70 seconds. At 90 seconds, the distortion and pressure reach a terrifying industrial climax before cutting instantly to complete dead silence at 90 to 100 seconds, leaving only ambient ocean void. At 100 seconds, a hollow, frozen synth pad and isolated, fading sub-bass pulse re-emerge, closing into a solitary, breathless resolve at 120 seconds. Heavy, visceral, no orchestral sweeps, minimalist analog tension.
```
