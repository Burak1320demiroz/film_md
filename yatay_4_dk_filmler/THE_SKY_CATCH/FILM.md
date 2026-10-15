# 🎬 THE_SKY_CATCH — Gökyüzü Yakalayışı

```
FILM           THE_SKY_CATCH
FORMAT         yatay 16:9
HEDEF_SURE     4:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/THE_SKY_CATCH/
URETIM         GPT Image (başlangıç kareleri) → Gemini video (10 s klipler) / Google Flow · seslendirme ayrı (post-prodüksiyon) · kurgu
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; sahibin orijinal planı `ODA/SAHIP_PLANI.md`'de ve `THE_SKY_CATCH.md`'de birebir durur.
> Promptlar `PROMPTLAR/`'dadır.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10 = 24 çekim; toplam süre tam 04:00.
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `ODA/SAHIP_PLANI.md` (sahibin verdiği tam üretim paketi, 14 Ekim 2026, birebir).**
> §1-§7 doğrudan sahibin üretim planından aktarılmıştır; olay örgüsü, 10 tasarım referansı, 24 sahne ve diyaloglar eksiksiz korunmuştur.
> Replikler post prodüksiyonda kurguda eklenen ses olarak uygulanır; video promptlarında dudak senkronu veya yapay zekâ konuşma üretimi zorlanmaz.

---

## 1. HİKÂYE

```
LOGLINE   Dünya'ya düşen uzay asansörünün 48 yolculu son kabinini yakalamaya gelen iki kurtarıcı, ana bağlantı halkasının kopmuş olduğunu görünce, mühendis aynı hızla düşen araçlar arasındaki uzay boşluğunu geçip yedek acil çekme kolunu elle açarak ölümcül inişi durdurur.
AMAÇ      Pilot Dane ve mühendis Sana, Dünya'ya doğru kontrolsüz alçalan asansör kabinine yanaşıp standart yakalama halkasından kenetlenerek kabini güvenli irtifaya çıkarmayı amaçlar (sahne 1-3).
ENGEL     Ana yakalama halkası parçalanmıştır ve standart yanaşma imkânsızdır (sahne 4-5); kurtarma için tek yol dış servis kapağındaki manuel acil çekme koludur; iki araç aynı düşüş hızındayken Sana uzay boşluğuna çıkmak zorundadır (sahne 6-10); Dünya'nın atmosferi ve irtifa hızla tükenmektedir (sahne 15); Sana henüz içeri girmeden kurtarma motorları ateşlenemez (sahne 18).
KARAR     Sana acil çekme kolunu açmak için emniyet bağıyla boşluğu geçip manyetik botlarıyla kabinin dış servis platformuna kilitlenmeye karar verir (sahne 6, 9-11); mandalı elle çevirir (sahne 13); Dane, kilit tamamlandıktan sonra Sana güvenle hava kilidine dönene kadar motor ateşlemesini bekletir (sahne 18).
SONUÇ     Yedek çekme kolu KITE'ın burnundaki tek çeneli C çerçeveye oturup kilitlenir (sahne 16-17); Sana içeri girip hava kilidi kapandıktan sonra kurtarma motorları ateşlenir (sahne 19-21); iki aracın düşüşü durur ve 48 yolcunun tamamı kurtarılır (sahne 22-24).
BEDEL     Sana, düşen iki aracın arasındaki ölümcül uzay boşluğunu geçerek hayatını riske atar; Dane irtifa tükenirken Sana'nın içeri dönüşünü beklemek zorunda kalır · sahne 10 · 18
TEK SORU  "Dane ve Sana, ana halkası kopmuş kabini Dünya'ya çarpmadan önce elle açılan acil çekme koluyla yakalayabilecek mi?"
SEÇİM     Sahip planı (tek ve kesin üretim paketi, 14.10.2026) · gerekçe: ODA/SAHIP_PLANI.md
SAHİP     ONAY (tam üretim paketini kendisi verdi: "o plandan dışarı çıkamadan o filmi yapacak planı hazırla") · 14.10.2026
```

İlk 10 saniyenin hook'u (sahip planı): *"The last elevator car was falling to Earth. We had one ship to catch it."*  
Kapanış cümlesi: *"Let's give them a gentler ride home."*  
İzleyici merak zinciri: Küçük kurtarma gemisi devasa Dünya'ya düşen kabini yakalayabilecek mi? → Ana halka kopmuşsa nasıl tutacaklar? → Sana düşüş sırasında boşluğu geçip kolu açabilecek mi? → Dünya yaklaşırken bağlantı kilitlenecek mi? → Sana geri dönemeden ateşleme yapmak zorunda kalacaklar mı? → 48 yolcunun hepsi güvende mi?

---

## 2. TRETMAN

<!-- kaynak: SAHIP_PLANI §5 "24 kliplik kesin zaman çizelgesi" birebir (sahne = klip) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Kabin dev Dünya'ya doğru düşüyor; KITE uzaktan yetişmeye çalışıyor. Açılış iç sesi. | Olay ve tehlike ilk karede doğrudan kurulur; vaat karşılanır. |
| S2 | 0:10–0:20 | Kokpitte Sana içeride 48 kişinin olduğunu ve kabin basıncının stabil kaldığını doğrular. | Yolcu sayısı ve kurtarılacak insan hayatı somutlaşır. |
| S3 | 0:20–0:30 | Dane standart kurtarma planı için kabinin üst ana bağlantı halkasına doğru yanaşır. | Standart yakalama girişimi başlar. |
| S4 | 0:30–0:40 | Yakın planda ana yakalama halkasının kopmuş ve parçalanmış olduğu görülür. | İlk plan çöker; fiziksel engel ortaya çıkar. |
| S5 | 0:40–0:50 | KITE çarpışmayı önlemek için hasarlı bağlantıdan geri çekilir; kabin düşmeyi sürdürür. | Çözümsüzlük anı ve acil alternatif arayışı. |
| S6 | 0:50–1:00 | Sana dış servis platformundaki elle açılan acil çekme kolunu bulur ve dışarı çıkacağını bildirir. | Yeni çözüm belirlenir: insan müdahalesi gereklidir. |
| S7 | 1:00–1:10 | KITE kabinin sol servis hizasına geçer; iki araç aynı düşüş çizgisine hizalanır. | İki aracın konumu geçiş için uygun hale getirilir. |
| S8 | 1:10–1:20 | Dane göreli düşüş hızını eşitler; iki araç uzayda sabit bir aralıkla kilitlenir. | Geçiş için güvenli fiziksel pencere açılır. |
| S9 | 1:20–1:30 | KITE'ın yan hava kilidi açık; Sana emniyet bağı kuşanmış halde eşikte durur. | EVA hazırlığı tamamlanır. |
| S10 | 1:30–1:40 | Sana iki araç arasındaki boşlukta ayakları önde kontrollü bir süzülüşle ilerler. | En tehlikeli boşluk geçişi gerçekleşir. |
| S11 | 1:40–1:50 | Sana manyetik botlarını kabinin alt sol dış servis platformuna kilitler. | Karakter hedefe ulaşır ve sabitlenir. |
| S12 | 1:50–2:00 | Sana basınçsız dış servis mekanizmasının kapağını tek menteşesinden yukarı açar. | Katlı mekanizma görünür hale gelir; basınçlı kabin kapalıdır. |
| S13 | 2:00–2:10 | Sana servis bölmesindeki sıkışmış geniş bırakma mandalını çeyrek tur çevirir. | Mekanik kilit çözülür. |
| S14 | 2:10–2:20 | Kalın dikdörtgen çekme kolu tek alt menteşesinden 90 derece dışarı açılır. | Yakalanabilir yapısal kol hazır hale gelir. |
| S15 | 2:20–2:30 | Dünya kadrajı devasa bir eğriyle doldurur; kritik irtifa uyarısı gelir. | Zaman baskısı doruğa çıkar; tehlike yaklaşır. |
| S16 | 2:30–2:40 | KITE'ın burnundaki açık C yakalama çerçevesi çekme kolunun kare ucuna oturur. | İlk temas kurulur; çene henüz açıktır. |
| S17 | 2:40–2:50 | Çerçevenin tek menteşeli çenesi kolun etrafında kapanır ve kilitlenir: sert yakalama. | İki araç yapısal olarak birbirine bağlanır. |
| S18 | 2:50–3:00 | Dane motorları ateşlemeye hazırlanır ama Sana geri geçişe başlamıştır; ateşleme ertelenir. | Kurtarıcının hayatı ile görev arasındaki gerilim. |
| S19 | 3:00–3:10 | Sana KITE'ın hava kilidine girmiştir; dış kapak kapanır ve kilitlenir. | Sana tamamen içeridedir; dışarıda kimse kalmaz. |
| S20 | 3:10–3:20 | İkisi kokpitte kemerli ve güvene alınmıştır; Dane itici kolunu aktif konuma iter. | Ateşleme öncesi tam iç güvenlik sağlanır. |
| S21 | 3:20–3:30 | KITE'ın alttaki sabit kurtarma iticileri Dünya yönüne güçlü alevle ateşlenir. | Karşı itki başlar; iki araç birlikte kaldırılır. |
| S22 | 3:30–3:40 | Bağlı düzenin Dünya'ya doğru düşüşü durur; iki araç yükselmeye başlar. | Düşüş tehdidi bertaraf edilir. |
| S23 | 3:40–3:50 | Sana durum ekranından doğrular: 48 yolcunun sinyali stabil ve güvendedir. | Kurtarmanın başarısı teyit edilir; rahatlama. |
| S24 | 3:50–4:00 | Kurtarılan kabin ve KITE, dev Dünya'nın üzerinden sakin uzaya doğru uzaklaşır. Kapanış. | Hikâye huzurlu ve asil bir finalle noktalanır. |

---

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

<!-- kaynak: SAHIP_PLANI §4 R01-R10, numaralandı (sahip kararı 10.10.2026: <No>.<AD>, özne başına tek sayfa). Prompt metinleri SAHIP_PLANI'nda ve PROMPTLAR/G01.md REFERANS PROMPTLARI'nda -->
| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Dane Hart — kurtarma pilotu (plan R01): 38 yaş, kısa koyu saç, kahverengi göz, dar yüz, hafif sakal; fildişi basınç takımı, turuncu üst kol bantları, yuvarlak mavi-altın yazısız görev rozeti, kapalı şeffaf vizör. | `1.DANE_v1.png` | v1 | | ⬜ | C02 · C08 · C20 · C23 |
| 2 | Sana Cruz — kurtarma mühendisi (plan R02): 33 yaş, sıcak kahverengi ten, koyu gözler, kask içinde toplanmış siyah saç; inci beyazı takım, turkuaz üst kol bantları, üçgen turkuaz-gümüş yazısız mühendis rozeti, manyetik botlar, tek emniyet bağı, kapalı şeffaf vizör. | `2.SANA_v1.png` | v1 | | ⬜ | C02 · C06 · C09 · C10 · C11 · C12 · C13 · C14 · C18 · C19 · C20 · C23 |
| 3 | KITE kurtarma gemisi dış (plan R03): kompakt grafit/fildişi gövde, mavi iki kişilik kanopi, burunda C biçimli yakalama çerçevesi ve tek menteşeli çene, çerçevenin üstünde küçük yan hava kilidi, altta iki sabit ventral kurtarma iticisi (egzoz Dünya yönüne). | `3.KITE_v1.png` | v1 | | ⬜ | C01 · C03 · C05 · C07 · C09 · C10 · C15 · C16 · C17 · C18 · C19 · C21 · C22 · C24 |
| 4 | Düşen yolcu kabini dış (plan R04): sert dikdörtgen fildişi/grafit gövde, yüz göstermeyen kehribar opak camlar, kısa kırık üst kılavuz parçası ve hasarlı ana halka, sol alt dış platformda servis kapağı. Basınçlı gövde tamamen kapalı. | `4.KABIN_v1.png` | v1 | | ⬜ | C01 · C03 · C05 · C07 · C10 · C15 · C21 · C22 · C24 |
| 5 | KITE kokpit içi (plan R05): kompakt iki kişilik grafit kokpit; solda Dane, sağda Sana; mavi kavisli kanopi, kehribar iç ışıklar, fiziksel anahtarlar, karanlık okunaksız ekranlar, dev eğri mavi Dünya kanopiden görünür. | `5.KOKPIT_v1.png` | v1 | | ⬜ | C02 · C06 · C08 · C20 · C23 |
| 6 | Hasarlı ana halka detay (plan R06): kabinin kısa kırık üst kılavuzu ve yırtılmış ana yakalama halkası; iki kalın sabit kırılma kenarı, kablo/parça uçuşması yok, altındaki basınçlı gövde sağlam. | `6.HALKA_v1.png` | v1 | | ⬜ | C04 |
| 7 | Servis kapağı kapalı (plan R07): kabinin sol alt dış servis çıkıntısı; dikdörtgen basınçsız dış servis kapağı tek üst menteşeyle tamamen kapalı, altındaki gövde sızdırmaz. | `7.SERVIS_v1.png` | v1 | | ⬜ | C07 · C11 · C12 |
| 8 | Kapak açık ve kol katlı (plan R08): aynı servis çıkıntısı; tek menteşeli kapak tamamen açık; kalın dikdörtgen grafit çekme kolu omurga braketine dikey katlı, tek alt mafsal ve geniş çeyrek tur mandal görünür. | `8.MANDAL_v1.png` | v1 | | ⬜ | C13 · C14 |
| 9 | Çekme kolu açık (plan R09): aynı çıkıntı; servis kapağı açık; kalın dikdörtgen çekme kolu tek alt mafsalından 90 derece dışarı açılmış; ucunda kare yakalama çıkıntısı sabit durur. | `9.CEKMEKOLU_v1.png` | v1 | | ⬜ | C15 · C16 · C17 |
| 10 | Kilitli kurtarma düzeni (plan R10): KITE solda, kabin sağda; açılmış çekme kolu KITE'ın C çerçevesi içine oturmuş, tek çene tamamen kilitli; rijit birleşik yapı; alttaki iki ventral itici Dünya yönüne bakar ve kabini temizler. | `10.DUZEN_v1.png` | v1 | | ⬜ | C18 · C21 · C22 · C24 |

```
SHA-256: shasum -a 256 ~/film_medya/THE_SKY_CATCH/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla.

ORTAK GÖRÜNÜM (GECIS_VE_SES_SUREKLILIGI §1 — her görsel ve video promptunun sonunda birebir; plan "ortak stil" cümlesinden):
  Photoreal live-action cinematic science-fiction image with restrained anamorphic lens character, fine 35 mm film grain, cool blue Earth light and restrained amber practical lights, readable blacks, and realistic metal detail.
MEKÂN IŞIĞI (birebir, mekân başına):
  DIŞ UZAY (DÜNYA YÖRÜNGESİ) — cool blue reflected light from enormous Earth below, stark directional sunlight skimming ivory hull edges, deep space shadows with sparse stars.
  KOKPİT — cool blue Earth reflections across the forward canopy, restrained warm amber console illumination from below.
  HAVA KİLİDİ VE SERVİS PLATFORMU — stark cool Earth illumination on metal plating, crisp geometric shadows, faint amber service indicators.
ORTAM SESİ (kurguda eklenecek yataklar için tarif — video promptunda sessiz taban):
  DIŞ UZAY — The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static.
  KOKPİT — The only ambient sound is soft cabin ventilation and close, calm breathing inside the helmet.
  SERVİS PLATFORMU — The only ambient sound is close suit breathing and faint mechanical hull vibration.
Sabit tasarım (plan §2): Dünya tek gezegen, büyük eğri ufuk aşağıda · KITE solda, kabin sağda · iki astronotun vizörleri kapalı ve şeffaf · rozetler ve kol bantları sabit ·
hasarlı ana halka ilk görünüşten itibaren kırıktır · çekme kolu açıldıktan sonra açık kalır · servis kapağı dış mekanizmadır, yolcu kabinini açmaz · yolcu pencereleri kehribar opak kalır, yüz görünmez.
```

---

## 4. ÇEKİM LİSTESİ

<!-- kaynak: SAHIP_PLANI §5 ve §6 K01-K24; "Ekranda görünen" zihinsel fiilsiz objektif dille; hepsi Frames to Video (GPT Image başlangıç karesi → Gemini video). Grup: G01 C01-C08 · G02 C09-C16 · G03 C17-C24 -->
| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Uzay asansörü kabini Dünya'ya düşerken KITE yetişmeye çalışır | Geniş dış plan: sağda kırık kılavuz parçası görülen fildişi yolcu kabini devasa eğri Dünya üzerinde alçalır; sol üstte KITE küçük bir siluet olarak yaklaşır. Kamera yavaş yanal kayar; iki araç arasında ölçek farkı ve Dünya ufku görünür. | geniş dış kurtarma açısı, sabit / hafif kayma | KITE sol üstte; kabin sağda; Dünya altta | 10 | Frames to Video | Atmosfer alevi veya çarpışma yok; Dünya ufku eğri ve devasa; model sesi yok, dış ses kurguda | 3.KITE · 4.KABIN | G01 | ✍️ | — | — | — |
| C02 | İçeride 48 kişi vardır ve kabin basıncı korunmaktadır | Kokpit orta ikili plan: solda Dane kumandada, sağda Sana karanlık yolcu durumu göstergesine bakar; kavisli kanopi ardında Dünya ufku kayar. Sabit kamera; Sana bakışını göstergeden Dane'e çevirir; kask vizörleri kapalı ve şeffaftır. | orta ikili kokpit planı, sabit | Dane solda; Sana sağda | 10 | Frames to Video | Ağız hareketi üretilmez; ekranlarda yazı yok, kurguda bindirilir | 1.DANE · 2.SANA · 5.KOKPIT | G01 | ✍️ | — | — | — |
| C03 | KITE standart kurtarma için kabinin ana yakalama halkasına yaklaşır | Yakın dış yaklaşma planı: KITE'ın açık C çerçevesi kabinin üst kılavuzuna doğru yaklaşır; iki araç arasında yaklaşık bir araç boyu mesafe kalır. Sabit dış kamera; KITE düz çizgide yavaşça yaklaşır ve temas etmeden durur. | yakın dış yaklaşma, sabit | KITE solda; kabin sağda | 10 | Frames to Video | Bu çekimde temas ve kilitlenme yok; çene açık kalır; yalpa yok | 3.KITE · 4.KABIN | G01 | ✍️ | — | — | — |
| C04 | Kabinin ana yakalama halkası tamamen parçalanmıştır | Aşırı yakın detay planı: kabinin kısa kılavuz sapı üzerindeki parçalanmış ana halka; iki kalın sabit kırık metal kenarı, arkada sağlam basınçlı gövde. Sabit mekanik kamera; sabit kırık kenarlara çok hafif yaklaşma hareketi. | aşırı yakın detay, hafif itiş | kırık halka merkezde | 10 | Frames to Video | Yeni kırılma, kıvılcım veya uçuşan kablo yok; hasar sabittir | 6.HALKA | G01 | ✍️ | — | — | — |
| C05 | KITE çarpışmayı önlemek için hasarlı bağlantıdan geri çekilir | Orta-geniş dış plan: KITE hasarlı halkanın solunda, burnu açık; iki gövde arasında net bir boşluk açılır; kabin arka planda sabit düşüşünü sürdürür. Sabit kamera; KITE ters yönde kontrollü geri çekilme hareketi yapar. | orta-geniş dış, sabit | KITE sola çekilir; kabin sağda | 10 | Frames to Video | Gövdeler arasında güvenli boşluk korunur; temas veya darbe yok | 3.KITE · 4.KABIN | G01 | ✍️ | — | — | — |
| C06 | Sana elle açılan yedek acil çekme kolunu tespit eder | Kokpit yakın plan: Sana sağ koltukta oturur, bir eldivenli eli konsol korkuluğunda; kapalı şeffaf vizöründe Dünya yansıması. Sabit kamera; Sana bakışını karanlık servis ekranından arkadaki hava kilidine doğru çevirir; ağız kapalıdır. | kokpit yakın plan, sabit | Sana sağda; hava kilidine bakar | 10 | Frames to Video | Ekranda metin yok; dudak senkronu yok; vizör kapalı ve berraktır | 2.SANA · 5.KOKPIT | G01 | ✍️ | — | — | — |
| C07 | KITE kabinin servis platformu tarafına hizalanır | Geniş dış plan: KITE kabinin soluna, alt servis çıkıntısının karşısına yerleşir; iki gövde arasında kısa bir geçiş boşluğu kalır; servis kapağı kapalıdır. Kabini takip eden kamera; KITE küçük yanal hareketle hizada sabitlenir. | geniş dış takip planı | KITE solda; kabin sağda | 10 | Frames to Video | Kenetlenme yok; iki araç düşüşte aynı göreli hıza gelir | 3.KITE · 4.KABIN · 7.SERVIS | G01 | ✍️ | — | — | — |
| C08 | Pilot düşüş hızını eşitler; iki araç göreli olarak sabitlenir | Kokpit yakın plan: Dane'in eldivenli elleri kumanda kollarında; kanopinin yanından kabin sabit bir noktada durur. Sabit kamera; Dane kumandada küçük bir düzeltme hareketi yapar; kabin kanopide sabit kalırken Dünya arkada akar. | kokpit yakın plan, sabit | Dane merkezde; kabin kanopide | 10 | Frames to Video | Ekranlarda yazı yok; dudak hareketi yok; kabin konumu sabit | 1.DANE · 5.KOKPIT | G01 | ✍️ | — | — | — |
| C09 | Sana açık hava kilidinin eşiğinde geçiş için hazırlanır | KITE yan hava kilidi eşik planı: Sana eşikte durur, manyetik botları basamakta, tek ince emniyet bağı beline ve içerideki kancaya takılıdır. Sabit kamera; Sana ağırlığını açık kapıya doğru hafifçe kaydırır; dışarı atlamaz. | hava kilidi eşik planı, sabit | Sana eşikte; kabin karşıda | 10 | Frames to Video | Kapı zaten açıktır; bu çekimde çıkış tamamlanmaz | 2.SANA · 3.KITE | G02 | ✍️ | — | — | — |
| C10 | Sana iki araç arasındaki boşluğu süzülerek geçer | Orta-geniş dış plan: Sana KITE'ın açık hava kilidi ile kabinin servis platformu arasındaki boşlukta ayakları önde süzülür; tek emniyet bağı arkasından uzanır. Sana'yı takip eden kamera; Sana platforma doğru yavaşça ilerler, dokunmadan biter. | orta-geniş dış takip | Sana soldan sağa süzülür | 10 | Frames to Video | Ani savrulma yok; iki araç birbirine göre sabit kalır | 2.SANA · 3.KITE · 4.KABIN | G02 | ✍️ | — | — | — |
| C11 | Manyetik botlar servis platformuna kilitlenir | Alçak yakın dış plan: Sana'nın inci beyazı botları kabinin küçük dış servis platformuna temas eder; tek emniyet bağı geride uzanır. Sabit alçak kamera; botlar metal platform üzerinde hafifçe yerine oturur ve manyetik kilitlenme sağlar. | alçak yakın detay, sabit | botlar platform üzerinde | 10 | Frames to Video | Yürüme veya sıçrama yok; servis kapağı kapalı kalır | 2.SANA · 7.SERVIS | G02 | ✍️ | — | — | — |
| C12 | Sana dış servis kapağını yukarı doğru açar | Orta-yakın dış plan: Sana platformda dengelenmiş, bir eli korkulukta, diğer eli kapalı servis kapağının kenarında. Sabit kamera; Sana tek üst menteşeli kapağı yukarı doğru açar; katlı çekme kolu ve mandal görünür hale gelir. | orta-yakın dış plan, sabit | kapak aşağıdan yukarı açılır | 10 | Frames to Video | Basınçlı yolcu gövdesi sağlam ve kapalı kalır; kol katlıdır | 2.SANA · 7.SERVIS | G02 | ✍️ | — | — | — |
| C13 | Sana sıkışmış bırakma mandalını çevirir | Sıkı mekanik detay planı: açık servis bölmesinde katlı çekme kolu ve geniş bırakma mandalı; Sana'nın eldiveni mandalı tutar. Sabit mekanik kamera; eldivenli el mandalı tam çeyrek tur çevirir ve durur; kol henüz katlıdır. | sıkı mekanik detay, sabit | mandal döner | 10 | Frames to Video | Kol bu çekimde açılmaz; tek mandal hareketi; eldiven sabit | 2.SANA · 8.MANDAL | G02 | ✍️ | — | — | — |
| C14 | Çekme kolu 90 derece dışarı açılır | Üç çeyrek dış servis planı: Sana korkulukta güvene alınmış, mandal bırakılmış; kalın dikdörtgen çekme kolu tek alt mafsalından sola dışarı döner. Sabit kamera; kol doksan derece açıya gelene kadar döner ve durdurucuda sabitlenir. | üç çeyrek dış plan, sabit | kol dışarı sola döner | 10 | Frames to Video | Teleskopik uzama veya kablo yok; kol tek parça sert metaldir | 2.SANA · 8.MANDAL | G02 | ✍️ | — | — | — |
| C15 | Dünya kadrajı doldurur; kritik irtifa seviyesine inilir | Dramatik geniş dış plan: solda KITE, sağda kabin, çekme kolu açık, Sana platformda küçük bir figür; aşağıdaki devasa Dünya bulut ufku belirgin biçimde yaklaşmıştır. Yavaş aşağı eğilen kamera; ufuk çizgisi yükselirken araçlar mesafeyi korur. | dramatik geniş dış, aşağı eğilme | Dünya altta yaklaşır | 10 | Frames to Video | Sana dışarıdayken atmosfer alevi veya duman üretilmez | 3.KITE · 4.KABIN · 9.CEKMEKOLU | G02 | ✍️ | — | — | — |
| C16 | KITE'ın açık yakalama çerçevesi kolun ucuna yanaşır | Yakın dış plan: KITE'ın açık C yakalama çerçevesi çekme kolunun kare ucuna birkaç santimetre kalana kadar hizalanır. Sabit kamera; KITE çok kısa düz bir ileri hareket yapar ve kol ucu çerçevenin içine oturur; çene henüz açıktır. | yakın dış plan, sabit | KITE soldan sağa yanaşır | 10 | Frames to Video | Bu çekimde çene kapanmaz; çarpışma veya sekme yoktur | 3.KITE · 9.CEKMEKOLU | G02 | ✍️ | — | — | — |
| C17 | Yakalama çerçevesinin tek çenesi kapanır ve kilitlenir | Aşırı yakın mekanik plan: çerçeve içine oturmuş kol ucu; tek menteşeli çene kolun etrafında aşağı doğru kapanır. Sabit mekanik kamera; tek çene sertçe kapanır ve mandallanır; kol ve gövde rijit bir bağlantıya dönüşür. | aşırı yakın mekanik, sabit | çene yukarıdan aşağı kapanır | 10 | Frames to Video | Tek çene hareketi; metal parçalanması veya kıvılcım yok | 3.KITE · 9.CEKMEKOLU | G03 | ✍️ | — | — | — |
| C18 | Kilit tamamlanmıştır; Sana dönüş için platformdan ayrılır | Orta dış plan: kilitli çekme kolunun üzerinde Sana platformdan ayrılmış, KITE'ın açık hava kilidine doğru kontrollü geri süzülüşe başlamıştır. Sana'yı takip eden kamera; Sana hava kilidine yaklaşır ama henüz içeri girmez. | orta dış takip planı | Sana sağdan sola süzülür | 10 | Frames to Video | İtici ateşi yok; Sana dışarıdayken motor çalıştırılmaz | 2.SANA · 3.KITE · 10.DUZEN | G03 | ✍️ | — | — | — |
| C19 | Sana tamamen hava kilidinin içindedir ve dış kapak kapanır | KITE hava kilidi iç planı: Sana tamamen içeri girmiş, emniyet bağı içeride toplanmış, ayakları eşikten temizlenmiştir. Sabit iç kamera; tek menteşeli dış kapak kapanır ve tam sızdırmazlıkla yerine oturur. | hava kilidi iç planı, sabit | dış kapak kapanır | 10 | Frames to Video | Sana'nın hiçbir uzvu veya bağı kapı aralığında kalmaz | 2.SANA · 3.KITE | G03 | ✍️ | — | — | — |
| C20 | İki karakter kokpitte kemerlidir; itici kolu açılır | Kokpit orta ikili plan: Dane solda, Sana sağda kemerli ve güvene alınmış; vizörler kapalı. Sabit kamera; Dane geniş kurtarma itici kolunu rölantiden ileri aktif dayanağa doğru iter; kabin sarsıntısız ve güvenlidir. | orta ikili kokpit planı, sabit | Dane itici kolunu iter | 10 | Frames to Video | Dudak hareketi yok; aşırı şiddetli sarsıntı veya panik yok | 1.DANE · 2.SANA · 5.KOKPIT | G03 | ✍️ | — | — | — |
| C21 | KITE'ın altındaki sabit kurtarma iticileri ateşlenir | Geniş dış plan: kilitli rijit düzen; KITE solda, kabin sağda; KITE'ın altındaki iki sabit ventral itici Dünya yönüne doğru parlak sürekli alevle ateşlenir. Düzeni takip eden kamera; bağlı iki araç birlikte kademeli olarak yukarı ivmelenir. | geniş dış takip planı | egzoz Dünya'ya doğru aşağı | 10 | Frames to Video | Egzoz kabine çarpmaz; gövdeler rijit ve esnemesizdir | 3.KITE · 4.KABIN · 10.DUZEN | G03 | ✍️ | — | — | — |
| C22 | İki aracın düşüşü durur ve Dünya'dan uzaklaşmaya başlarlar | Orta-geniş dış plan: iki ventral itici düzenli ateşlemeyi sürdürür; Dünya ufku yavaşça kadrajda geriler ve küçülür. Düzenle sabit hızda hareket eden kamera; birleşik gövde stabil biçimde Dünya'dan uzaklaşır. | orta-geniş dış takip | Dünya ufku geriye çekilir | 10 | Frames to Video | Kilitli düzen bozulmaz; servis kapağı açık kalır | 3.KITE · 4.KABIN · 10.DUZEN | G03 | ✍️ | — | — | — |
| C23 | Sana ekranı kontrol eder: 48 yolcunun sinyali de stabildir | Kokpit orta ikili plan: Dane ve Sana koltuklarında; Sana karanlık durum ekranına bakar ve rahatlamayla Dane'e doğru hafifçe başını sallar; Dane sakin bir rahatlamayla karşılık verir. Sabit kamera; sakin teyit anı. | orta ikili kokpit planı, sabit | Sana ve Dane rahatlar | 10 | Frames to Video | Kask çıkarma veya sarılma yok; ölçülü profesyonel rahatlama | 1.DANE · 2.SANA · 5.KOKPIT | G03 | ✍️ | — | — | — |
| C24 | Kurtarılan kabin KITE ile beraber sakin uzaya doğru yükselir | Final geniş kompozisyon planı: KITE ve kilitli asansör kabini devasa mavi Dünya'nın üzerinden uzaklaşır; iki itici yumuşak ışık verir. Çok yavaş geri çekilen kamera; kurtarılan kabin güvenle KITE'a bağlı kalır; sakin final. | geniş final çekimi, yavaş geri çekilme | araçlar yukarı uzaklaşır | 10 | Frames to Video | Yeni gemi veya tehdit yok; sakin ve eksiksiz kurtarma | 3.KITE · 4.KABIN · 10.DUZEN | G03 | ✍️ | — | — | — |

```
Süre: her çekim 10 s (sahip kararı 08.10.2026). Çekim sayısı = HEDEF_SURE / 10 = 24; toplam = 4:00.
Flow modu: hepsi Frames to Video (sahip planı: GPT Image başlangıç karesi → Gemini video 10 s).
Zincir: Bu filmde ardışık sahneler ayrı kesmelerle ilerler; zincir dili kullanılmaz (Zincir = —).
Grup: PROMPTLAR/G01.md C01–C08 · G02.md C09–C16 · G03.md C17–C24. Durum: ✍️ prompt hazır.
Öncelikli kareler (sahip planı §3 durum geçişleri): C12 (kapak açılır, R07→R08) · C14 (kol açılır, R08→R09) · C17 (çene kilitlenir, R09→R10).
```

---

## 5. REPLİKLER

<!-- kaynak: SAHIP_PLANI §5 ve §7 "Tek parça İngilizce ses kaydı metni" birebir (24 replik).
     Saniye ve süre değerleri kurgu ve seslendirme başlangıç taslağıdır; her replik <= 8 s.
     Kurguda eklenen ses: post prodüksiyonda eklenir; video promptunda yapay zekâ ağız senkronu zorlanmaz. -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 0.8 | Dane (VO) | kurguda eklenen ses (voice-over) | HUMAN | The last elevator car was falling to Earth. We had one ship to catch it. | 5.5 |
| R02 | C02 | 1.0 | Sana | kurguda eklenen ses (kask içi) | HUMAN | Forty-eight people inside. Cabin pressure is holding. | 2.8 |
| R03 | C03 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | I'll take the main collar. Keep them steady. | 3.0 |
| R04 | C04 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Stop. The main collar's torn off. | 2.4 |
| R05 | C05 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | Backing off. Find me another way to grab it. | 3.5 |
| R06 | C06 | 1.0 | Sana | kurguda eklenen ses (kask içi) | HUMAN | Emergency tow bar. Manual release. I'll have to go outside. | 4.0 |
| R07 | C07 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | I'll match the fall. You cross when we're steady. | 3.5 |
| R08 | C08 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | Relative motion matched. I've got you. | 2.5 |
| R09 | C09 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Tether secure. Keep that gap. | 2.0 |
| R10 | C10 | 1.0 | Dane | kurguda eklenen ses (telsiz) | HUMAN | Easy. I'll hold the line. | 2.0 |
| R11 | C11 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Boots locked. I'm on the service ledge. | 2.8 |
| R12 | C12 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Opening the service cover. Passenger cabin stays sealed. | 3.2 |
| R13 | C13 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Release is stiff. Turning it now. | 2.4 |
| R14 | C14 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Tow bar deploying. Bring your nose down to me. | 3.6 |
| R15 | C15 | 1.0 | Dane | kurguda eklenen ses (telsiz) | HUMAN | We're running out of sky. Stay on the rail. | 3.6 |
| R16 | C16 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Straight ahead. You're on the tow bar. | 2.8 |
| R17 | C17 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | Hard lock. I've got the car. | 2.4 |
| R18 | C18 | 1.0 | Sana | kurguda eklenen ses (telsiz) | HUMAN | Don't burn yet. I'm coming back. | 2.4 |
| R19 | C19 | 1.0 | Sana | kurguda eklenen ses (kask içi) | HUMAN | I'm inside. Seal it. | 1.8 |
| R20 | C20 | 1.0 | Sana | kurguda eklenen ses (kask içi) | HUMAN | All sealed. Get us out of here. | 2.4 |
| R21 | C21 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | Come on, KITE. Lift us. | 2.0 |
| R22 | C22 | 1.0 | Dane | kurguda eklenen ses (kask içi) | HUMAN | Descent stopped. We're climbing. | 1.8 |
| R23 | C23 | 1.0 | Sana | kurguda eklenen ses (kask içi) | HUMAN | Forty-eight signals. All stable. We got them. | 2.8 |
| R24 | C24 | 1.0 | Dane (VO) | kurguda eklenen ses (voice-over) | HUMAN | Let's give them a gentler ride home. | 2.8 |

```
Toplam replik: 24 replik (4 dk için bant 12-24, tam uyumlu).
Ses karakterleri: Dane olgun, sakin, orta-alt tonda Amerikan İngilizcesi erkek ses;
                 Sana net, kararlı, orta tonda Amerikan İngilizcesi kadın ses.
Kurgu kuralı: Replik çoğunlukla klip başlangıcından 0,8–1,2 saniye sonra girer; mekanik seslere ve müziğe alan bırakılır.
```

---

## 6. SES PLANI — ortam yatağı, efektler ve geçişler

<!-- kaynak: SAHIP_PLANI her klibin "Ses / müzik" notları ve §7 "Dört dakikalık ses yayı" -->
| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 | Y1 dış basınç tonu · motor uğultusu ve bas darbesi · R01 (VO) · müzik alçak nabız | S2 telsiz J 0,5 s | İlk karede ağır metal vurgu; vakumda tasarım sesi |
| S2 | Y2 kabin havalandırması · iki düşük nabız darbesi · R02 · müzik gergin | — | Yolculardan ses gelmez; kabin içi kuru akustik |
| S3 | Y1 · yönlendirme iticileri sesi (gemi içi perspektif) · R03 · müzik kısa yükseliş | — | Yaklaşma iticileri |
| S4 | Y1 · müzik incelir · R04 · tek hafif metal uyarısı | — | Halka hasarı fark edilince müzik geri çekilir |
| S5 | Y1 · kontrollü ters itici darbesi · R05 · müzik nabzı geri gelir | — | Geri çekilme darbesi |
| S6 | Y2 · nefes · R06 · müzikte ince kararlı ritim | S7'ye L 0,5 s | Son cümleden sonra kısa nefes boşluğu |
| S7 | Y1 · iki kısa itici darbesi ve kapanış · R07 · müzik stabil | — | Hız eşleme manevrası |
| S8 | Y2 · metalin hafif titreşimi · R08 · güven veren sakin ton | S9 kilit tıkı J | Göreli hareket durur |
| S9 | Y3 hava kilidi eşiği · kask içi nefes · metal kilit tıkı · R09 | S10 nefes L 1 s | Dış uzay patlama sesi yok |
| S10 | Y1 · takım içi kumaş sürtünmesi ve nefes · R10 · müzik nabzı | — | Boşluk geçişi sessizliği |
| S11 | Y3 · tek tok manyetik kilit sesi · R11 | — | Manyetik botların platforma oturması |
| S12 | Y3 · kapak menteşesinde metal sürtünmesi · R12 | — | Dış kapak açılır; yolcu sesi duyulmaz |
| S13 | Y3 · dirençli metal sürtünmesi ve mandal tıkı · R13 | — | Çeyrek tur dönüş mandalı |
| S14 | Y3 · ağır metal açılma ve durdurucu çarpması · R14 | S15 alarm J 0,5 s | Kolun 90 derecede oturması |
| S15 | Y1 · iki kısa alçak irtifa uyarısı · R15 · hızlanan ritim | — | Yaklaşan Dünya tehlikesi |
| S16 | Y1 · iki küçük itici düzeltmesi · yumuşak mekanik temas · R16 | — | Çerçevenin kola oturması |
| S17 | Y1 · güçlü tek sert kilit sesi · R17 · müzik cevap vurgusu | S18 nefes J | Tek çene kapanması |
| S18 | Y1 · kask içi nefes sesi · R18 · müzik bir vuruş geri çekilir | — | Motor ateşlemesi ertelenir |
| S19 | Y3 · hava kilidi dış kapısının oturma sesi ve tıslama · R19 | — | Basınç dengeleme ve kilit |
| S20 | Y2 · itici kolunun mekanik tıkı · R20 · motor alttan yükselir | S21 ateşleme J 0,5 s | Kokpitte hazır olma |
| S21 | Y1 · iki sabit ventral iticinin derin kükremesi · R21 · müzik teması açılır | — | Güçlü kurtarma itişi |
| S22 | Y1 · itici sesi düzenli hale gelir · R22 · müzik genişler | — | İrtifa uyarısı susar; yükseliş |
| S23 | Y2 · rahat nefes · R23 · gergin ritim çözülür, sıcak ton | — | 48/48 stabil doğrulaması |
| S24 | Y1 · yumuşak itici uğultusu · R24 (VO) · müzik sakin kapanır | — | Son 3 saniye görsel ve işitsel nefes |

### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | dış uzay yörünge | C01 · C03-C05 · C07 · C10 · C15-C18 · C21-C22 · C24 | low steady non-diegetic space pressure tone with a faint continuous bed of radio static and distant planetary rumble | −20 LUFS | yatak_uzay.wav |
| Y2 | KITE kokpit içi | C02 · C06 · C08 · C20 · C23 | soft steady cockpit ventilation hum, dry cabin acoustics, faint avionics bed, no rhythm | −18 LUFS | yatak_kokpit.wav |
| Y3 | servis platformu ve hava kilidi | C09 · C11-C14 · C19 | close helmet breathing, subtle hull conduction and metallic friction resonance, clear vacuum acoustic | −18 LUFS | yatak_servis.wav |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1→Y2 çapraz 1 s; telsiz J 0,5 s | dış uzay → kokpit; hareket üstünde kesme |
| C02→C03 | kesme | Y2→Y1 çapraz 1 s | kokpit → dış uzay |
| C03→C04 | kesme | Y1 sürer | aynı dış mekân, ölçek geniş → aşırı yakın |
| C04→C05 | kesme | Y1 sürer | aşırı yakın → orta-geniş |
| C05→C06 | kesme | Y1→Y2 çapraz 1 s | dış → kokpit |
| C06→C07 | kesme | Y2→Y1 çapraz 1 s | kokpit → dış |
| C07→C08 | kesme | Y1→Y2 çapraz 1 s | dış → kokpit |
| C08→C09 | kesme | Y2→Y3 çapraz 1 s; hava kilidi kilit sesi J | kokpit → hava kilidi eşiği |
| C09→C10 | kesme | Y3 sürer | hava kilidi eşiği → iki araç arası boşluk |
| C10→C11 | kesme | Y3 sürer; manyetik bot kilidi tıkı | boşluk → platform teması |
| C11→C12 | kesme | Y3 sürer | aynı platform, botlar → servis kapağı |
| C12→C13 | kesme | Y3 sürer | kapak açıldı → mandal detayı |
| C13→C14 | kesme | Y3 sürer | mandal çevrildi → kol açılması |
| C14→C15 | kesme | Y3→Y1 çapraz 1 s; irtifa alarmı J 0,5 s | platform yakını → dev Dünya geniş açısı |
| C15→C16 | kesme | Y1 sürer | geniş dış → yakalama çerçevesi teması |
| C16→C17 | kesme | Y1 sürer | temas → tek çenenin kilitlenmesi |
| C17→C18 | kesme | Y1 sürer | sert kilit → Sana'nın geri dönüşü |
| C18→C19 | kesme | Y1→Y3 çapraz 1 s | dış boşluk → hava kilidi içi |
| C19→C20 | kesme | Y3→Y2 çapraz 1 s | hava kilidi kapandı → kokpit ikili plan |
| C20→C21 | kesme | Y2→Y1 çapraz 1 s; itici kükremesi J 0,5 s | itici kolu çekildi → motorların ateşlenmesi |
| C21→C22 | kesme | Y1 sürer | ateşleme devam ederken düşüşün durması |
| C22→C23 | kesme | Y1→Y2 çapraz 1 s | dış yükseliş → kokpit rahatlama |
| C23→C24 | karisim 0,8 | Y2→Y1 çapraz 1 s; sıcak müzik tonu sürer | kokpit teyidi → sakin final uzaklaşması |

---

## 7. MÜZİK PLANI

<!-- kaynak: SAHIP_PLANI §7 "Dört dakikalık ses yayı" -->
```
OKUMA        İzleyici filmi yüksek gerilimli ama kontrollü ve gerçekçi bir uzay kurtarması olarak okumalıdır; panik çığlıkları yerine profesyonel odaklanma, mekanik engeller ve zaman baskısı gerilimi taşır.
MÜZİKSİZ     00:30–00:40 (S4) bozuk halka görüldüğünde müzik incelir ve susar · 01:30–01:40 (S10) EVA geçişi sırasında takım içi nefes ve sessizlik öne çıkar · 02:50–03:00 (S18) Sana geri geçerken ateşleme bekletilir, müzik geri çekilir.
VURUŞ/SUSMA  00:00–00:30 tek ağır metal vurgusu ve alçak nabız (düşüşün büyüklüğü) · 00:30–01:00 bozuk halkada duraksama, alternatif bulunurken ritmin geri gelişi ·
             01:00–02:20 adım adım yükselen kısa ritmik mekanik doku (bot kilidi, kapak, mandal, kol açılışı) ·
             02:20–03:20 en sıkışık bölüm; irtifa uyarısı, temas, tek çene kilidi; diyaloglardan sonra kısa vurucu boşluklar ·
             03:20–03:40 motor ateşlemesiyle birlikte güçlü, yükselen kurtarma teması ·
             03:40–04:00 rahatlama; 48/48 teyidiyle birlikte daha az vuruş ve sıcak asil ton; son 3 saniye çözülmüş sakin kapanış.
FLOW MUSIC   Müzik Flow Music veya eşdeğer orkestral synthesizer ile üretilir; konuşma ve telsiz diyaloglarının altına dengeli mikslenir.
```

### MÜZİK PROMPTU — Flow Music'e yapıştırılır (sahip planı, 14.10.2026)
```text
Original cinematic score for a four-minute hard science-fiction rescue film. Low pulsing sub-bass, restrained analog synthesizers, deep cello drones and delicate metallic acoustic textures, strictly no vocals, no recognizable blockbuster motifs. Begin with cold dread and massive planetary descent weight, thin out into sparse quiet tension when the docking collar breaks, then build an intricate rhythmic pulse for a manual spacewalk and latch release. Climax into an urgent driving crescendo as Earth looms close and the single jaw locks, hold a breathless suspended beat while the engineer returns through the airlock, and finally burst into an expansive heroic ascent theme driven by low brass and warm sustained strings as thrusters ignite and arrest the fall. End with a gentle unresolved chord fading into deep space stillness.
```
