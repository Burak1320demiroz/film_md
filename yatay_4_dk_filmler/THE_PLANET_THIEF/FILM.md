# 🎬 THE_PLANET_THIEF — Gezegen Hırsızı

```
FILM           THE_PLANET_THIEF
FORMAT         yatay 16:9
HEDEF_SURE     4:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/THE_PLANET_THIEF/
URETIM         Google Flow (web) · QA Gemini uygulaması — sahip planı: görseller GPT Image, videolar Gemini Omni 1.1 Flash 10 s (ODA/SAHIP_PLANI.md "Süre ve araç seçimi")
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `FIZIK_IDDIASI yok`: plan "gezegen taşıma alanı, yapay güneş ve yıldız söndüren cephe kurmaca teknolojilerdir; belgesel fizik anlatımı hedeflenmez" der.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `ODA/SAHIP_PLANI.md` (sahibin verdiği plan, 10.10.2026, birebir).** §1-§7 oradan yerleştirildi; faz 1-4 ajan turu açılmadı
> (sahip talimatı: "plana sadık kal ve bu filmi yap"). Fable'ın plandan türettiği tek şey biçim çevirisidir (sütunlar, numaralar, süreler);
> olay, kompozisyon, replik ve tasarım planın kendisidir. Replik saniye ve süreleri Fable tahminidir, F4 ses planında kesinleşir.

---

## 1. HİKÂYE

```
LOGLINE   Dünya'yı çeken dev kara gemiyi sabote etmeye giden kurtarma pilotu, geminin gezegenleri sönen Güneş'ten kurtardığını görür ve kesmekten vazgeçer.
AMAÇ      Elias Rook gemiye yanaşıp Dünya'yı çeken alanı besleyen enerji hattını kesmeye gider (sahne 3 karar, sahne 11 kesici hatta doğrultulur).
ENGEL     Bilek tarayıcısı milyarlarca yaşam belirtisi verir (sahne 12); dar pencerede Dünya olmayan mavi gezegen (13); içeride altı gezegen ve yapay güneş (14); dışarıda Güneş'i söndüren karanlık cephe (4, 17).
KARAR     Sahne 19: Elias kesiciyi indirir, hattı kesmekten vazgeçer. Sahne 20: Dünya komutasına "Earth command. Do not attack. This is an evacuation."
SONUÇ     Dünya giriş halkasından geçer (21); gerçek Güneş söner (22); içerideki Dünya'nın ufkunda yapay güneş doğar (23); Elias'ın arkasında yedi dünya (24).
BEDEL     Dünya kendi yörüngesini ve gerçek Güneş'ini kaybeder; dışarıda dönülecek bir ev kalmaz · sahne 22
TEK SORU  "Elias hattı kesmeden önce gerçeği görecek mi; Dünya kurtulacak mı?"
SEÇİM     Fable: sahip planı (tek aday, aday turu açılmadı) · 10.10.2026 · gerekçe: ODA/SAHIP_PLANI.md + ODA/DURUM.md SAHİP CEVAPLARI
SAHİP     ONAY (planı kendisi verdi: "plana sadık kal ve bu filmi yap") · 10.10.2026
```

Merak zinciri (plan): Dünya'yı kim çekiyor? → Bu geminin içinde ne var? → Dünya kurtulacak mı?

## 2. TRETMAN

<!-- kaynak: SAHIP_PLANI "24 klip — tek bakışta" Ana olay sütunu birebir; "Ne değişir" plandaki dönüş noktaları ve prompt tariflerinden -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | İlk karede Dünya, kendisinden büyük kara geminin açık ağzına çekilmektedir. | Dünya, gemi ve çekim alanı aynı karede; Dünya tamamen dışarıda. İlk cümle: "Something was taking the Earth." |
| S2 | 0:10–0:20 | Elias kokpitte dev gemiye bakar; soğukkanlılığını korumaya çalışır. | Pilot ve kaskına vuran amber ışık görünür; AI alanın gezegeni taşıdığını söyler. |
| S3 | 0:20–0:30 | Pilotun omzu üzerinden Dünya ile dev gemiyi aynı planda görürüz; Elias gemiye girmeye karar verir. | Kurtarma gemisi gövde boyunca ileri gider; hedef kurulur: "I can cut the tractor field." |
| S4 | 0:30–0:40 | Geminin ekranında Güneş'in kenarındaki açıklanamayan karanlığı görürüz. | Güneş'teki karanlık ilk kez görünür; final tehdidi ekilir. |
| S5 | 0:40–0:50 | Küçük kurtarma gemisi, kara geminin yüzeyi boyunca uçar. | Ölçek kurulur; AI: Dünya komutası saldırı hazırlıyor. |
| S6 | 0:50–1:00 | Gemi, dev gövde içindeki küçük bakım noktasına yaklaşır. | İnsan ölçeğinde bir soket bulunur. |
| S7 | 1:00–1:10 | İnsan gemisinin üst bağlantısı, dev geminin sabit soketiyle hizalanır. | Yanaşma başlar; temas yok. Replik yok. |
| S8 | 1:10–1:20 | Bağlantı halkası yerine oturur ve dış kelepçe kapanır. | Yanaşma kilitlenir; araştırma başlar. |
| S9 | 1:20–1:30 | Elias açık hava kilidinin içinde durur; karanlık koridorla ilk kez karşılaşır. | Gemi boş: "No guards. No crew." Kesici elde, kapalı. |
| S10 | 1:30–1:40 | Koridorun sağındaki enerji hattı, derindeki kavşağa doğru ışık taşır. | Hedef somutlaşır: hat çekimi besliyor. |
| S11 | 1:40–1:50 | Elias kavşakta kesiciyi enerji hattına doğrultur; cihaz henüz çalışmaz. | Sabotaj eşiği: "One cut. We get our world back." |
| S12 | 1:50–2:00 | Bilek tarayıcısı uyarı verir; içeride beklenmedik yaşam belirtileri vardır. | Görev kesilir: "Wait. Life signs. Billions." |
| S13 | 2:00–2:10 | Dar gözlem açıklığında mavi bir gezegen belirir; kıtaları Dünya'ya ait değildir. | İçeride başka bir dünya var. |
| S14 | 2:10–2:20 | Geniş açı, kara geminin içinde korunan altı gezegeni ve yapay güneşi açığa çıkarır. | Kasa tamamen açığa çıkar; Dünya yuvası boş. Replik yok. |
| S15 | 2:20–2:30 | Kurtarılan gezegenin gece yüzünde düzenli şehir ışıkları görülür. | Gezegenler yaşıyor. |
| S16 | 2:30–2:40 | Yapay güneşin halkaları ile ışık alan gezegenlerden biri aynı planda görülür. | Çözüm görünür: gemi yeni güneş vermiş. |
| S17 | 2:40–2:50 | Dışarıda ışığı yok eden karanlık cephe Güneş'in büyük bölümünü kaplamıştır. | Dış Güneş'in yok olduğu anlaşılır. |
| S18 | 2:50–3:00 | Dünya artık dev geminin ağzına çok yaklaşmıştır; dış Güneş'in ışığı zayıflar. | Seçimin bedeli açık: "Stop the pull, and Earth stays outside." |
| S19 | 3:00–3:10 | Elias kesiciyi indirir; çekim sistemini kesmekten vazgeçer. | Sabotaj durur: "I almost cut our only way out." |
| S20 | 3:10–3:20 | Elias haberleşme kanalını açar ve saldırının durdurulmasını ister. | Dünya uyarılır: "Do not attack. This is an evacuation." |
| S21 | 3:20–3:30 | Dünya açık giriş halkasının eşiğini geçer; yok olmadan içeride gözden kaybolur. | Dünya gemiye girer; bütün kalır. Replik yok. |
| S22 | 3:30–3:40 | Güneş'in son parçası söner; Dünya artık o yörüngede değildir. | Müzik kesilir; geminin amber ışıkları kalır. |
| S23 | 3:40–3:50 | İçerideki Dünya'nın ufku yapay güneşle aydınlanır; gezegen kurtulmuştur. | Boş yuva doldu; yeni şafak. |
| S24 | 3:50–4:00 | Elias'ın arkasından Dünya ve diğer kurtarılmış dünyaları görürüz; öykü tamamlanır. | Yedi dünya, yapay güneş: "We called it a thief. It was carrying the survivors." |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

<!-- kaynak: SAHIP_PLANI R01-R09, numaralandı (sahip kararı 10.10.2026: <No>.<AD>, özne başına tek sayfa). Prompt metinleri SAHIP_PLANI'nda ve PROMPTLAR/G01.md REFERANS PROMPTLARI'nda -->
| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Elias Rook — TEK SAYFA (plan R01 + F5 panel): önden tam boy · arkadan tam boy · baş-omuz portre · sağdan tam boy (F5 devamlilik B3/teknik B8, Fable KABUL); kapalı şeffaf vizör, fildişi giysi, kol üstünde yanık turuncu şerit, sol göğüste mavi-altın rozet, sağ kaşta eski yara | `1.ELIAS_v1.png` | v1 | | ⬜ | C02 · C03 · C09 · C11 · C12 · C14 · C19 · C20 · C24 |
| 2 | İnsan kurtarma gemisi — TEK SAYFA (plan R02 + F5 paneller, denetçi F5.7): ¾ dış Dünya üstünde · tam yan görünüm araç seviyesinden · önden ve sırtın biraz üstünden, yanaşma halkası görünür; fildişi kama gövde, turuncu yan şerit, iki kısa grafit kanat | `2.KURTARMA_GEMISI_v1.png` | v1 | | ⬜ | C05 · C06 · C07 · C08 |
| 3 | Kokpit (plan R03): tek koltuk, üç dikmeli kanopi, camgöbeği soyut gösterge ışıkları, sağda küçük dikdörtgen ekran (kapalı) | `3.KOKPIT_v1.png` | v1 | | ⬜ | C02 · C03 · C04 |
| 4 | Dev gemi / ark dış — TEK SAYFA (plan R04 + F5 panel): ana panel kara silindir, boyuna kaburgalar, açık dairesel giriş, ince amber kenar, Dünya tamamen dışarıda, amber çekim yayları · ikinci panel ¾ giriş ve amber kenar (F5 devamlilik B5) | `4.ARK_v1.png` | v1 | | ⬜ | C01 · C03 · C05 · C06 · C18 · C21 · C22 · C23 |
| 5 | Yanaşma noktası + koridor — TEK SAYFA (plan R05 + F5 panel): iç hol ve dar kaburgalı koridor, sağ duvarda amber enerji silindiri ve eşit aralıklı siyah braketler, açık dikdörtgen kapı · ikinci panel dış bakım kuyusu, TAVANDA yuvarlak soket (F5: soket tek konum = tavan; devamlilik B2 · teknik B3) | `5.YANASMA_KORIDOR_v1.png` | v1 | | ⬜ | C06 · C07 · C08 · C09 · C10 |
| 6 | Enerji kavşağı + gözlem bölmesi (plan R06, F5'te AYNALANDI: koridorun sağ duvarındaki hat bölmede de sağda): SAĞDA dikey amber hat ve servis braketi, SOLDA dar cam yarık, alçak korkuluk, panoramik pencere (teknik B9) | `6.GOZLEM_BOLMESI_v1.png` | v1 | | ⬜ | C10 · C11 · C13 · C19 · C20 |
| 7 | Gezegen kasası — TEK SAYFA (plan R07 + F5 paneller): ana panel üç halka içinde yapay altın güneş, altı farklı gezegen (yeşim/mor adalı · pas çöl · soluk buz · turkuaz · gri-yeşil · çivit), sol önde boş büyük yuva · yakın paneller: yeşim dünya (gündüz + alacakaranlık sınırı) · pas çöl dünyası (devamlilik B5) | `7.KASA_v1.png` | v1 | | ⬜ | C13 · C14 · C15 · C16 · C23 · C24 |
| 8 | Aksesuarlar (plan R08, tek sayfa, iki nesne): mat siyah plazma kesici (kapalı, ışınsız) · fildişi bilek tarayıcı (tek camgöbeği halka ışık) | `8.AKSESUARLAR_v1.png` | v1 | | ⬜ | C09 · C11 · C12 · C19 · C20 |
| 9 | Kararan Güneş (plan R09): turuncu-sarı Güneş, soldan ilerleyen düzensiz ışıksız cephe, ince koyu kızıl kenar | `9.GUNES_v1.png` | v1 | | ⬜ | C04 · C17 · C22 |

```
SHA-256: shasum -a 256 ~/film_medya/THE_PLANET_THIEF/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: plan R01 üç görünüşlü sayfadır; F5 eleştirisi profil çekimleri (C11 · C19) için dördüncü panel (sağdan tam boy) ekletti; 4 · 5 · 7 sayfalarına da yakın/ikinci paneller eklendi (Fable KABUL, 10.10.2026). Panel listeleri PROMPTLAR/G01.md REFERANS PROMPTLARI'nda.
Plan ayrıca bazı çekimlerde ÖNCEKİ ÇEKİMİN KARESİNİ görsel kaynak olarak kullanır (C15←C13 · C17←C04 yalnız cephe yönü ·
C18←C01 · C21←C18 · C23←C21 · C24←C23; C08←C07 F5'te kaldırıldı: temas kesmede, C08 tek başına üretilir): bu zincir değildir, başlangıç karesi üretiminde kompozisyon kaynağıdır (§4 Risk sütunu).
Sabit tasarım ve devamlılık maddeleri: ODA/SAHIP_PLANI.md "Sabit tasarım ve devamlılık" (Elias kaskı hiç çıkmaz · kesici hiç çalışmaz ·
Dünya küçülmez/erimez/parçalanmaz · cephe soldan · iç mekân basınçlı, iki ayak yerde · Elias tek erkek ses, AI tek sakin kadın ses).
```

## 4. ÇEKİM LİSTESİ

<!-- kaynak: SAHIP_PLANI K01-K24; "Ekranda görünen" Image/Video prompt tariflerinden görünen dille; hepsi görüntüden video (plan: GPT Image kare → Gemini/Flow) -->
| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Dünya, kendisinden büyük kara geminin açık ağzına çekiliyor | Solda Dünya (üçte bir), sağda devasa açık dairesel giriş ve amber kenar; şeffaf amber çekim yayları gezegeni sarıyor; gövde yanında toz gibi fildişi bir araç. Dünya sağa, girişe doğru ağır kayar; ön kenarı dışarıda kalır; yaylar biraz güçlenir. | aşırı geniş dış plan, sabit uzak kamera | Dünya solda, giriş sağda; Dünya sağa | 10 | Frames to Video | Dünya bütün ve rijit, giriş plandan büyük; Güneş Dünya'nın sol kenarını aydınlatır. Plan: logo yok, ilk saniyede VO | 4.ARK | G01 | ✍️ | — | — | — |
| C02 | Pilot dev gemiye bakıyor | Yakın-orta plan: Elias pilot koltuğunda, kapalı şeffaf vizör ardında yıpranmış yüz; sağdan gelen geniş amber yansıma vizörü geçer; eller kadraj dışı; kanopi ve koyu dikmeler sağdaki bakışı çerçeveler, camgöbeği konsol ışığı kadrajın altından parlar. Tek kontrollü nefes, bakış hafif yukarı sağa; yansıma vizörde kayar. | yakın-orta, yavaş itiş | bakış sağa (kanopiye) | 10 | Frames to Video | T16 yüz yakın: kimlik 1.ELIAS portre paneli; ağız hareketi istenmez (replik AI, telsiz) | 1.ELIAS · 3.KOKPIT | G01 | ✍️ | — | — | — |
| C03 | Dünya ile gemi aynı planda; kurtarma gemisi gövdeye doğru ilerliyor | Omuz üstünden geniş plan: sol altta fildişi kask, turuncu kol şeridi, koyu kemer; kanopiden solda Dünya amber girişin dışında, sağa doğru devasa kaburgalı gövde; konsolda yalnız soyut camgöbeği ışık. Kurtarma gemisi gövde boyunca ileri gider; kaburgalar kanopiden yavaş kayar; Elias koltukta sabit. | geniş omuz üstü, araç ileri | Dünya solda, giriş sağda | 10 | Frames to Video | T06 ekran: yalnız soyut ışık, yazı yok. Dünya bütün, giriş rijit | 1.ELIAS · 3.KOKPIT · 4.ARK | G01 | ✍️ | — | — | — |
| C04 | Güneş'in kenarına karanlık yayılıyor | Konsolun sağındaki dikdörtgen ekrana sıkı ek plan: ekranda turuncu-sarı Güneş'in sade teleskop görüntüsü, sol kenardan giren küçük düzensiz ışıksız leke; grafit çerçeve, camgöbeği parıltı; arka kokpit yumuşak bulanık. Leke Güneş'in küçük bir bölümünü daha örter; konsolda camgöbeği durum ışığı yanıp söner; ekran düzeni değişmez. | sıkı ek plan, sabit | cephe soldan | 10 | Frames to Video | T06 okunacak ekran: etiket/harf/rakam yok, yalnız görüntü. Plan: tutarsız çıkarsa 9.GUNES tabanlı görüntü kurguda ekrana oturtulur | 3.KOKPIT · 9.GUNES | G01 | ✍️ | — | — | — |
| C05 | Küçük gemi, dev gövde boyunca uçuyor | Geniş dış takip: fildişi kurtarma gemisi, iki kısa grafit kanat, turuncu yan şerit, mavi-beyaz arka iticiler; arkasında kara geminin katmanlı gövdesi uçsuz bir duvar gibi, tek amber dikiş ileride küçük bir yuvaya uzanır; Dünya kadrajda değil. Araç sağa doğru sabit hızla gider, gövde kaburgaları arkasından yavaş geçer. | geniş dış, yandan takip | araç sağa | 10 | Frames to Video | Araç geometrisi rijit, iticiler sabit loş mavi-beyaz | 2.KURTARMA_GEMISI · 4.ARK | G01 | ✍️ | — | — | — |
| C06 | Gövdede insan ölçeğinde bir yanaşma noktası var | Aracın hemen önünden ve üstünden ileri bakış: sol altta aracın küt burnu ve sırtındaki yanaşma halkası; iki devasa kaburga arasında, kanyonun üst duvarında (tavan, sağda) küçük yuvarlak açık soket; amber ışıklar yuvayı çizer. Araç düz, hafif yana kayarak soketin altına doğru yaklaşır; kaburgalar kadrajda büyür. | ileri bakışlı dış, yavaş yaklaşma | soket tepede sağda (kanyonun üst duvarı) | 10 | Frames to Video | Araç dönmez, yalpalamaz. 5.YANASMA_KORIDOR soketi, 4.ARK dokuyu tanımlar; tek görsel | 2.KURTARMA_GEMISI · 4.ARK · 5.YANASMA_KORIDOR | G01 | ✍️ | — | — | — |
| C07 | Araç soketle hizalanıyor, temas yok | Orta dış yan plan: araç düz, tavandaki sabit yuvarlak soketin tam altında; sırt halkası soketle dikey hizada, arada kısa boşluk; alt yarı araç, üst yarı kara duvar; küçük amber hizalama lambaları yanıyor. Araç düz çizgide çok yavaş yükselir, boşluğun çoğu kapanır; burun sağa bakar; temas olmadan biter. | orta dış yan, sabit kamera | burun sağa; yükselme | 10 | Frames to Video | T01 temas kadraj içinde ama BU çekimde olmaz; halka ölçüleri değişmez. Replik yok | 2.KURTARMA_GEMISI · 5.YANASMA_KORIDOR | G01 | ✍️ | — | — | — |
| C08 | Halka oturur, kelepçe kapanır: yanaşma tamam | Yakın dış ek plan: aynı sırt halkası ve soket, iki rijit silindirik halka OTURMUŞ (boşluk yok; temas C07→C08 kesmesinde); arayüzün yanında tek geniş mekanik kelepçe açık, menteşesi görünür; yalnız halka, kelepçe ve çizik fildişi/kara gövde. Görünen tek kelepçe kendi menteşesinde yavaş döner, 7-8 s'de halkaya yaslanır; son vuruşta hizalama lambaları sabit yanar. | yakın ek plan, sabit | kelepçe menteşesinde döner | 10 | Frames to Video | T01 temas kesmeye alındı (F5 teknik B4, Fable KABUL): tek hareket kelepçe, yeni donanım açılmaz. C07 son karesi bağımlılığı kaldırıldı; C08 tek başına öncelikli önizleme | 2.KURTARMA_GEMISI · 5.YANASMA_KORIDOR | G01 | ✍️ | — | — | — |
| C09 | Elias içeride; gemi boş, koridor karanlık | Geniş göz hizası koridor: sol önde Elias açık dikdörtgen hava kilidi kapısının içinde, iki bot düz zeminde, kapalı vizörlü kask, fildişi giysi; sağ elinde alçakta mat siyah kapalı kesici; sağ duvarda amber hat karanlığa uzanır; kapı çerçevesi tam ve rijit. Kamera kapı arkasından Elias'a ve koridora yavaş dolly; Elias yerinde, kaskı hafif sağ duvara döner; kapı kanatları açık ve sabit. | geniş, göz hizası, yavaş dolly | koridor derinliğe; baş sağa | 10 | Frames to Video | Yürüme yok (plan); iki ayak yerde (basınçlı iç mekân). Kesici elde, tutan kadrajda | 1.ELIAS · 5.YANASMA_KORIDOR · 8.AKSESUARLAR | G02 | ✍️ | — | — | — |
| C10 | Enerji hattı derindeki kavşağa ışık taşıyor | Sağ duvardaki kalın şeffaf enerji silindiri boyunca alçak yakın perspektif: içinde ayrı geniş amber ışık darbeleri; eşit aralıklı siyah braketler, düz zemin; koridor aynı gözlem bölmesine açılır, uçta dikey hat; kimse yok. Kamera silindire paralel ileri kayar; tek geniş amber darbe kameradan uzaklaşıp bölmeye gider; braketler ve çap korunur. | alçak yakın, ileri kayma | ışık kameradan uzağa, derinliğe | 10 | Frames to Video | İnsansız ek plan; promptta kişiye gönderme yok | 5.YANASMA_KORIDOR · 6.GOZLEM_BOLMESI | G02 | ✍️ | — | — | — |
| C11 | Kesici hatta doğrultulmuş, henüz çalışmıyor | Gözlem bölmesinde orta yan plan: solda Elias iki ayak yerde, şeffaf vizör ve sağ kaş yarası görünür; sağda dikey amber hat ve önünde sade servis braketi; iki eldivenli elde mat siyah kesici, ağzı brakete kısa mesafeden yönelik; güç ışığı loş, ışın yok; arkada dar cam yarık karanlık. Çok hafif itiş; Elias tuttuğu kesiciyi birkaç santim kaldırır, braketi nişanlar; hatta dokunmaz, kesici çalışmaz; vizörde amber ışık hafif oynar. | orta yan, çok hafif itiş | Elias solda, hat sağda | 10 | Frames to Video | T01 el-nesne: kesici zaten elde, hatta temas yok; ışın/ateşleme hiç yok (plan) | 1.ELIAS · 6.GOZLEM_BOLMESI · 8.AKSESUARLAR | G02 | ✍️ | — | — | — |
| C12 | Bilek tarayıcısı yaşam uyarısı veriyor | Sol kol üstündeki fildişi bilek tarayıcısına sıkı ek plan: siyah cam yüzde tek camgöbeği halka ışık parlamaya başlıyor; eldiven manşeti, koyu kayış ve sağda kadrajda duran kesicinin kenarı görünür (kavrama yok); kamera sol omuz üstünden, sol kol sol kenardan girer; cama amber bölme ışığı yansır; yazı/rakam yok. Halka parlar, iki kez nabız atar; bilek nefesten gelen hafif titremeyle neredeyse sabit; cihaz biçimi ve kayış sabit. | sıkı ek plan, sol omuz üstünden, sabit | sol kol sol kenardan | 10 | Frames to Video | T06 cihaz ekranı: tek halka ışık, yazı yok. Tutan kadrajda (kol manşeti). Plan: dönüm noktası sesle (AI) | 1.ELIAS · 8.AKSESUARLAR | G02 | ✍️ | — | — | — |
| C13 | Dar yarıkta Dünya olmayan mavi bir gezegen | Dar uzun gözlem yarığından sıkı bakış, iki yanda siyah cam çerçeve; camın ötesinde yeşim okyanuslu, mor ada kıtalı gezegen, küresel, bulutlu, ince parlak atmosfer; yanında tek amber tutma yayı; yalnız bu gezegen görünür. Kamera cam boyunca yavaş yana kayar, paralaksla gezegenin daha çoğu açılır; gezegen gözle seçilmez hızda döner, kıtalar aynı; yay yuvasına göre sabit. | sıkı, yana kayma | kamera yana | 10 | Frames to Video | Kıtalar 7.KASA yeşim/mor dünyası ile aynı; Dünya'nın Afrika biçimi bu gezegene girmez (plan) | 6.GOZLEM_BOLMESI · 7.KASA | G02 | ✍️ | — | — | — |
| C14 | Geminin içinde altı gezegen ve yapay güneş var | Panoramik pencereden aşırı geniş: sol altta korkulukta küçük kasklı Elias silueti; altı kayalık dünya ayrı derinliklerde, her biri ince amber yaylarla; merkez uzakta üç rijit halka içinde yapay altın güneş; devasa kara kaburgalar; sol ön büyük yuva boş. Başlangıç karesinde pencere çerçevesi ve korkuluk kadraj kenarlarında, dünyalar çerçeveyle kısmen kırpılmış; kamera cama doğru yavaş ileri dolly, çerçeve dışarı kayar ve altı dünya düzeni 7-8 s'de tamamen açılır; Elias korkulukta sabit; gezegen konumları ve yapılar sabit, bulutlar hafif kayar. | aşırı geniş, cama doğru ileri dolly (plan 'geri dolly' optik olarak açılmaz; F5 devamlilik B1 · teknik B2, Fable KABUL) | — | 10 | Frames to Video | T15 tek figür, silüet. Boş yuva okunur (Dünya henüz yok). Replik yok; müzik burada açılır | 1.ELIAS · 7.KASA | G02 | ✍️ | — | — | — |
| C15 | Kurtarılan gezegenin gece yüzünde şehir ışıkları | Yeşim okyanuslu mor adalı dünyaya daha yakın bakış, ark içinden; alacakaranlık sınırı kürenin ortasından geçer; koyu mor karalarda sıcak şehir ışığı kümeleri dallanan düzenlerde; ince atmosfer ve aynı amber yayın parçası; uzak kenarda kara kaburga. Kamera gece yüzüne yavaş iter; ışık kümeleri hafif parlar, ince bulutlar üstlerinden kayar; kıtalar, küre boyu, ışık düzeni sabit. | yakın gezegen planı, yavaş itiş | — | 10 | Frames to Video | Gezegen kameradan bağımsız büyümez/biçim değiştirmez. Başlangıç karesi kaynağı: C13 karesi | 7.KASA | G02 | ✍️ | — | — | — |
| C16 | Yapay güneş gezegenleri aydınlatıyor | Kasa içinde geniş alçak açı: üç devasa sabit halka içinde yapay altın güneş; sağ önde pas rengi çöl dünyası, atmosfer kenarı serin ve sönük, zayıf sıcak iz; solda iki küçük uzak küre; arkada kara kaburgalar; güneş açıkça yapılmış bir makinenin parçası. Kamera yana yavaş kayar, ön dünya ile uzak güneş arasında paralaks; üç halka rijit; altın kaynak bir kez hafif nabız atar, çöl dünyasının atmosferinde şafak çizgisi 6-10 s'de belirir. | geniş alçak açı, yana kayma | — | 10 | Frames to Video | Halkalar sabit; tek nabız | 7.KASA | G02 | ✍️ | — | — | — |
| C17 | Dışarıdaki karanlık Güneş'in üçte ikisini kapladı | Teleskop gibi geniş dış: aynı Güneş ve düzensiz ışıksız cephe, soldan diskin neredeyse üçte ikisi örtülü; kalan parlak bölüm yırtık hilal, çok ince koyu kızıl kenar; derin kara uzay; yuvarlak örten gezegen, canavar ya da araç yok. Sabit uzak kamera; cephe Güneş'in dar bir şeridini daha örter, hilal küçülür; Güneş'in yuvarlak silueti ve cephenin yönü korunur. | geniş uzak, sabit | cephe soldan sağa | 10 | Frames to Video | Tutulma değil, kurmaca cephe (plan); patlama/girdap yok. Başlangıç karesi kaynağı: C04 ekranındaki Güneş | 9.GUNES | G03 | ✍️ | — | — | — |
| C18 | Dünya girişe çok yakın; dış Güneş ışığı zayıf | Açılışla aynı yön: solda Dünya, sağda tamamen açık dairesel giriş; Dünya'nın ön kenarı giriş düzleminin hemen gerisinde; aynı şeffaf amber yaylar amber kenara yönlendirir; dış güneş ışığı belirgin loş, Dünya ve kara gövdenin çoğu mavi-siyah gölgede; kıtalar aynı. Sabit uzak kamera; Dünya sabit girişe biraz daha yaklaşır, düzlemi geçmez; kalan güneş ışığı hafif söner, amber kenar sabit; gezegen bütün. | aşırı geniş dış, sabit | Dünya solda → sağa | 10 | Frames to Video | T11 yön C01 ile aynı; Dünya kimliği (Afrika) korunur. Başlangıç karesi kaynağı: C01 karesi | 4.ARK | G03 | ✍️ | — | — | — |
| C19 | Elias kesiciyi indiriyor | Dikey amber hattın yanında Elias'a yakın-orta yan plan, aynı bölme ve braket; kesici iki elde ama artık brakete yakın değil; yüz kapalı şeffaf vizörden net; arkadaki dar yarıkta yumuşak altın ışık; ışın yok. Sabit kamera, çok hafif itiş; Elias tuttuğu kesiciyi tek yavaş hareketle bel hizasına indirir; parmaklar kabzada; hat sağlam, parlamayı sürdürür. | yakın-orta yan, çok hafif itiş | kesici aşağı | 10 | Frames to Video | T01: araç elden bırakılmaz, düşürülmez; T16 yüz yakın profil: 1.ELIAS sağdan tam boy paneli | 1.ELIAS · 6.GOZLEM_BOLMESI · 8.AKSESUARLAR | G03 | ✍️ | — | — | — |
| C20 | Elias haberleşme kanalını açıyor | Gözlem bölmesinde önden yakın-orta: eldivenli sol el göğüs hizasında, el sırtı kameraya dönük, bilek tarayıcısının halkası LOŞ; sağ el ve indirilmiş kesici kadraj dışı; şeffaf vizörden gözler öne; yüzün bir yanı panoramik pencereden sıcak yapay güneş ışığı, diğer yanı çelik mavisi gölge. Hafif yavaş itiş; halka 5-8 s'de loştan parlağa geçer ve sabit kalır (basış C19→C20 kesmesinde); duruş korunur; ağız kapalı ve sabit. | önden yakın-orta, hafif itiş | — | 10 | Frames to Video | T01 basış kesmeye alındı (F5 devamlilik B7 · teknik B6, Fable KABUL); replik telsiz filtresiyle kurguda, dudak senkronu yok (plan); T16 yüz yakın | 1.ELIAS · 6.GOZLEM_BOLMESI · 8.AKSESUARLAR | G03 | ✍️ | — | — | — |
| C21 | Dünya giriş halkasının eşiğinden geçiyor, bütün | Kara arkın sabit dairesel girişine ¾ dış bakış: ilk karede Dünya açıklıktan kısmen geçmiş, ön yarısı açıklığın içinde (yakın kenarın ötesinde görünür), arka yarıküre dışarıda, kavisli hat ve tanıdık kıtalar okunur; ön amber kenar kürenin küçük bir kısmını örter; açıklık çapı Dünya'dan görünür büyük; kara gövde girişi sarar. Sabit kamera, ark geometrisi rijit; küresel Dünya açıklıktan yavaş derine kayar, arka yarıkürenin çoğu ön kenarla örtülür; erime, küçülme, parçalanma yok; yaylar geçişe dek sürekli. | ¾ dış, sabit | Dünya derinliğe (sağa-içe) | 10 | Frames to Video | En kritik hareket (plan): gezegen bütün, kenar önden örter. Bitiş karesi kare/C21_bitis.png (kare/C21.png'den düzenleme) üretilir; iki deneme: d1 başlangıç+bitiş · d2 yalnız başlangıç, karşılaştırma NOTLAR'a (F5 teknik B7, Fable KABUL; zincir değil, tek çekim). Açıklık kameraya ve sola bakar. Başlangıç karesi kaynağı: C18 | 4.ARK | G03 | ✍️ | — | — | — |
| C22 | Güneş'in son parçası sönüyor; Dünya o yörüngede değil | Çok uzak geniş uzay: solda Güneş düzensiz cepheyle neredeyse tamamen örtülü, küçücük yırtık turuncu hilal; sağda, kameraya çok daha yakın, kara silindirik ark siluet, amber giriş kenarı hafif yanar, dışında Dünya yok; derin kara uzay ikisini ayırır. Sabit kamera; son hilal söner ve cephenin altında kaybolur, arkın ince amber ışıkları sabit kalır; ark bütün, dönüşmez; şok dalgası yok. | çok uzak geniş, sabit | Güneş solda, ark sağda | 10 | Frames to Video | Ölçek: Güneş uzak ve küçük, arka bitişik değil (plan). Müzik burada kesilir | 9.GUNES · 4.ARK | G03 | ✍️ | — | — | — |
| C23 | İçerideki Dünya'nın ufkunda yapay güneş doğuyor | Kasa içinde geniş: sol ön büyük yuvada artık Dünya, bütün, mavi okyanuslar, tanıdık Afrika, beyaz bulut sistemleri; ince amber yaylar tutar; arkada üç halkalı aynı yapay altın güneş diğer altı dünyanın arasında; kara kaburgalar ve uzak bölme duvarı; Dünya'nın karanlık ufkunda sıcak şafak çizgisi başlıyor. Kamera Dünya'nın atmosfer kenarına çok yavaş iter; altın ışık aynı bulutlara ve okyanus ufkuna yayılır; Dünya yuvada rijit küre. | geniş, çok yavaş itiş | — | 10 | Frames to Video | Yeni kıta/gezegen üretilmez; C14'teki boş yuva artık dolu. Başlangıç karesi kaynağı: C21 | 7.KASA · 4.ARK | G03 | ✍️ | — | — | — |
| C24 | Elias'ın arkasında yedi dünya ve yapay güneş | Gözlem balkonunda Elias'ın arkasından final aşırı geniş: alt ortada küçük fildişi giysili figür, sol eldiven alçak korkulukta, sağ elde aşağıda kesici; sol önde yuvada Dünya, derinde diğer altı dünya; merkez uzakta üç halkalı yapay altın güneş; devasa kara kaburgalar; sıcak ışık fildişi kaskı ve turuncu kol şeridini yakalar. Yavaş ölçülü geri çekilme, ölçek büyür, Elias korkulukta sabit; yedi dünya, yayları ve güneş sabit konumda; yeni tehdit yok. | aşırı geniş arkadan, yavaş geri çekilme | — | 10 | Frames to Video | T15 tek figür arkadan (1.ELIAS arkadan panel). Film adı istenirse son 2 s'de kurguda bindirilir (plan). Başlangıç karesi kaynağı: C23 | 1.ELIAS · 7.KASA | G03 | ✍️ | — | — | — |

```
Süre: her çekim 10 (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10; toplam = HEDEF_SURE (24 × 10 = 240 s).
Flow modu: plan bütün çekimleri "üretilen tek sahne görseli → görüntüden video" kurar → hepsi Frames to Video (başlangıç karesi kare/Cxx.png).
  Flow'da Veo 8 s verir; 10 s yolu SMOKE P14'te ölçülür (plan: Gemini Omni 1.1 Flash 10 s; Veo kalırsa 24 × 8 = 3:12, plan süreyi ayrıca ister).
Risk: ARIZA_LISTESI T kodu → "nasıl gösterilir"; "Başlangıç karesi kaynağı: Cxx" = planın önceki görüntü/son kare kullanımı (zincir değil).
Grup: G01 C01-C08 · G02 C09-C16 · G03 C17-C24 → PROMPTLAR/G0n.md. Durum: ⬜ · ✍️ prompt · 🖼️ kare onaylı · 🎥 deneme · ✅ seçildi.
Zincir · Baş. karesi · Bitiş karesi: plan zincir kurmaz ("konum değişimleri plan kesmeleriyle"); sahneleme adımı açılmadı (sahip planı).
  C21 için planın "ilk/son kareyle üret" önerisi tek çekim içinde başlangıç+bitiş karesidir; Flow iş emrinde satır notu olur.
Öncelikli önizleme (plan): C01 · C08 · C14 · C21 önce üretilir ve sınanır; F7 iş emri bu sırayla başlar.
```

## 5. REPLİKLER

<!-- kaynak: SAHIP_PLANI "Seslendirme — İngilizce tek liste" birebir (21 replik). Saniye ve süre Fable tahmini (≈2,5 kelime/s), F4 ses planında kesinleşir. Kaynak: voice-over → kadraj dışı · comms → telsiz; hiçbiri ağız kadrajda değil (plan: canlı konuşma yüklenmez, dudak senkronu yok). Kayıt: Elias HUMAN · AI MACHINE (dar bant filtreli sakin kadın ses; plan kayıt türünü belirtmez, Fable varsayımı) -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 0.5 | Elias | kadraj dışı (voice-over) | HUMAN | Something was taking the Earth. | 2.5 |
| R02 | C02 | 3.0 | AI | telsiz (comms) | MACHINE | Its field is moving the entire planet. | 3.0 |
| R03 | C03 | 3.0 | Elias | kadraj dışı (voice-over) | HUMAN | Get me inside. I can cut the tractor field. | 3.5 |
| R04 | C04 | 4.0 | AI | telsiz (comms) | MACHINE | The solar feed is losing light. | 2.5 |
| R05 | C05 | 3.0 | AI | telsiz (comms) | MACHINE | Earth command is preparing a strike. | 2.5 |
| R06 | C06 | 4.0 | AI | telsiz (comms) | MACHINE | There. A maintenance berth. | 2.0 |
| R07 | C08 | 7.0 | AI | telsiz (comms) | MACHINE | Docking seal confirmed. | 1.5 |
| R08 | C09 | 4.0 | Elias | kadraj dışı (voice-over) | HUMAN | No guards. No crew. | 2.0 |
| R09 | C10 | 4.0 | AI | telsiz (comms) | MACHINE | That conduit powers the pull. | 2.5 |
| R10 | C11 | 5.0 | Elias | kadraj dışı (voice-over) | HUMAN | One cut. We get our world back. | 3.0 |
| R11 | C12 | 4.5 | AI | telsiz (comms) | MACHINE | Wait. Life signs. Billions. | 2.5 |
| R12 | C13 | 5.0 | Elias | kadraj dışı (voice-over) | HUMAN | That isn't Earth. | 1.5 |
| R13 | C15 | 4.0 | AI | telsiz (comms) | MACHINE | Cities. Oceans. They're alive. | 2.5 |
| R14 | C16 | 5.0 | Elias | kadraj dışı (voice-over) | HUMAN | It gave them a new sun. | 2.5 |
| R15 | C17 | 4.0 | AI | telsiz (comms) | MACHINE | That front is killing our sun. | 2.5 |
| R16 | C18 | 4.0 | AI | telsiz (comms) | MACHINE | Stop the pull, and Earth stays outside. | 3.0 |
| R17 | C19 | 5.5 | Elias | kadraj dışı (voice-over) | HUMAN | I almost cut our only way out. | 3.0 |
| R18 | C20 | 4.0 | Elias | telsiz (filtered comms, kurguda) | HUMAN | Earth command. Do not attack. This is an evacuation. | 4.0 |
| R19 | C22 | 6.0 | AI | telsiz (comms) | MACHINE | The solar feed is gone. | 2.0 |
| R20 | C23 | 5.0 | Elias | kadraj dışı (voice-over) | HUMAN | Earth had a sunrise again. | 2.5 |
| R21 | C24 | 3.0 | Elias | kadraj dışı (voice-over) | HUMAN | We called it a thief. It was carrying the survivors. | 4.0 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik → 21 replik, bant içinde.
Plan kuralları: C07 · C14 · C21'de replik yok (görsel hareket taşır). Elias tek erkek ses; AI tek sakin kadın ses, dar bant haberleşme filtresi.
Elias'ın ilk cümleleri anlık anlatım, son cümleleri geriye dönük değerlendirme gibi okunur. Konuşma ve ses profilleri: ODA/SAHIP_PLANI.md "Sabit tasarım" + "Seslendirme".
```

## 6. SES PLANI — model sesi kullanılmaz

<!-- kaynak: SAHIP_PLANI her klibin "Audio:" satırı (planda video promptundaydı; hatta ses kurguda kurulur, promptta ses tarifi yazılmaz) + "Seslendirme" notları -->
| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 | alçak sinematik tonal basınç (skor benzeri tasarım) · VO R01 | — | vakumda yayılan ses değil, tasarım |
| S2 | kapalı kabin havalandırması · yakın kask nefesi · AI R02 | S1 tonu kabin içine iner | |
| S3 | iç motor titreşimi · kısa kemer gıcırtısı · VO R03 | | |
| S4 | kısa alçak uyarı çanı · havalandırma · AI R04 | | |
| S5 | yalnız diegetik olmayan alçak gerilim dokusu · AI R05 | | dış uzay: motor gümbürtüsü yok |
| S6 | bastırılmış mekanik gerilim tasarımı · AI R06 | | vakumda motor kükremesi yok |
| S7 | zayıf elektronik hizalama tonu (pilotun telsiz perspektifi) | | replik yok |
| S8 | tek derin yanaşma vuruşu · tek kısa metalik kilit (bağlı gövdeden iletilen) · AI R07 | kilit sesi S9 havalandırmasına J | |
| S9 | boş basınç sistemi havalandırması · nefes · alçak yapısal titreşim · VO R08 | | iç mekân basınçlı: hava var |
| S10 | yavaş yükselen rezonanslı elektrik uğultusu · AI R09 | | |
| S11 | kontrollü nefes · hat uğultusu · VO R10 | | |
| S12 | iki net kısa tarayıcı bipi · sabit hat uğultusu · AI R11 | | dönüm noktası sesle |
| S13 | bölme uğultusu · hafif tonal kabarma · VO R12 | | |
| S14 | geniş derin mimari rezonans · müzik burada açılır | müzik girişi S14 başı | replik yok |
| S15 | yumuşak yükselen hayret tonu · AI R13 | | |
| S16 | sabit derin jeneratör rezonansı · VO R14 | | |
| S17 | alçak inen gerilim tonu · AI R15 | | |
| S18 | derin alçak basınç tonu (diegetik değil) · AI R16 | | |
| S19 | tek uzun kontrollü nefes verme · sabit güç uğultusu · VO R17 | | |
| S20 | tek yumuşak telsiz tıkırtısı · nefes · R18 telsiz filtreli | | dudak senkronu yok |
| S21 | yükselen derin tasarım rezonansı · patlama yok | | replik yok |
| S22 | müzik kesilir · alçak sürekli ton kalır · AI R19 | müzik S22'de düşer | plan: belirgin müzik boşluğu |
| S23 | sıcak alçak jeneratör uğultusu · umut teması geri gelir · VO R20 | tema S23 ile girer | |
| S24 | sakin havalandırma · tek yumuşak nefes · final müzik · VO R21 | | |

```
Ortam: dış uzay çekimlerinde (S1 S5 S6 S7 S8 S17 S18 S21 S22) dış ses yok; alçak tonlar sinematik tasarım · iç hacim (S2-S4 kokpit, S9-S16 S19 S20 S23 S24 ark içi) hava taşır.
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_<n>.md (F4 açılırsa; şimdilik kaynak SAHIP_PLANI "Audio" satırları). Model sesi: promptlarda ses tarifi yazılmaz, bütün ses kurguda.
```

## 7. MÜZİK PLANI

<!-- kaynak: SAHIP_PLANI "Müzik ve kurgu" birebir -->
```
OKUMA        İzleyici bu filmi korku, ilk temas ve bir kurtarmayı işgal sanmanın bedeli olarak okumalı (plan açıklaması).
MÜZİKSİZ     00:00–02:10 yalnız düşük frekanslı gerilim/nabız ve metalik doku (skor benzeri tasarım, tema yok); müzik S14'te (02:10) açılır.
             03:30 Güneş sönerken belirgin boşluk (S22): müzik kesilir, alçak sürekli ton kalır.
VURUŞ/SUSMA  00:00–01:10 düşük frekanslı gerilim, seyrek nabız · 01:10–02:00 metalik mekân dokusu · 02:00–02:40 keşifle açılan yaylılar ·
             02:40–03:30 yeniden yükselen tehdit · 03:30 boşluk · 03:40–04:00 sıcak ve ağır umut teması — faz 8'de gerçek kesme noktalarıyla kesinleşir.
FLOW MUSIC   faz 8: ODA/F8_besteci_<n>.md. Plan promptu (kaynak): "Create a four-minute original cinematic science-fiction score for a lone rescue
             pilot boarding a planet-sized alien vessel. Begin immediately with ominous low strings, sparse deep pulses and restrained metallic textures.
             Build curiosity rather than continuous action. Around the middle, expand into a vast, solemn sense of discovery with sustained strings and a
             restrained wordless choir. Return to urgent low tension in the third minute. Near the final half-minute, create a sudden dramatic drop into
             near silence, then a warm, slow theme of survival for the ending. Dark orchestral-electronic palette, no lyrics, no spoken words, no imitation
             of any named soundtrack. Keep the score unobtrusive under short voice-over lines."
             Plan notu: üreticinin hassas zamanlarına bel bağlanmaz; yükselişler, 03:30 boşluğu ve son tema kurguda yerleştirilir; ses konuşmayı örtmez.
```

<!-- 12.10.2026 sahip kararı (her filmde müzik promptu §7'de): planın promptu birebir, F4 taslağı sayılır; F8'de besteci gerçek kesme noktalarıyla kesin sürümü altına yazar. -->
### MÜZİK PROMPTU — Flow Music'e yapıştırılır (plan taslağı, 12.10.2026)
```text
Create a four-minute original cinematic science-fiction score for a lone rescue pilot boarding a planet-sized alien vessel. Begin immediately with ominous low strings, sparse deep pulses and restrained metallic textures. Build curiosity rather than continuous action. Around the middle, expand into a vast, solemn sense of discovery with sustained strings and a restrained wordless choir. Return to urgent low tension in the third minute. Near the final half-minute, create a sudden dramatic drop into near silence, then a warm, slow theme of survival for the ending. Dark orchestral-electronic palette, no lyrics, no spoken words, no imitation of any named soundtrack. Keep the score unobtrusive under short voice-over lines.
```
