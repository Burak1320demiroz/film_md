# 🎬 DEAD_LAST — Sonuncunun Dünyası

```
FILM           DEAD_LAST
FORMAT         yatay 16:9
HEDEF_SURE     8:00
KLIP_SURESI    ölçülmedi
REPLIK         var
MUZIK          var
FIZIK_IDDIASI  yok
MEDYA          ~/film_medya/DEAD_LAST/
URETIM         sahip planı: başlangıç görseli → aynı kare video 10 s · replikler videoda oyunculuk ve ağız ipucu, temiz replik ayrı kayıt, kurguda (plan ortak hareket: "Dialogue is the assigned performance text, not a claim that the selected video model produces audio … Sound and clean dialogue may be added in editing.") · QA Gemini uygulaması
```

> Durum, tur ve bütçe `ODA/DURUM.md`'dedir. Bu dosya filmin kendisidir; ajanların ham
> çıktıları `ODA/`'da, promptlar `PROMPTLAR/`'da durur.
> `KLIP_SURESI` = aracın verdiği klip süresi (saniye), Flow'dan ölçülür; zincir varsa zorunlu.
> Her çekim **10 s** (sahip kararı 08.10.2026): çekim sayısı = HEDEF_SURE / 10. Zincir için KLIP_SURESI ≥ 10 gerekir (SMOKE P14).
> `REPLIK` · `MUZIK` · `FIZIK_IDDIASI` = **var | yok**. Koşullu ajanlar
> (diyalog-yazari · besteci · bilim-danismani) yalnız `var` ise çağrılır.
> `REPLIK` ve `MUZIK` varsayılan **var**: filmlerde akıcı diyalog, ses ve efekt olur (sahip kararı, 06.10.2026).
> `yok` yalnız hikâye bunu istiyorsa, gerekçesi §5'in altına yazılarak.
> Başlıkları ve sütun sırasını değiştirme: `film_dogrula.py` bunlara bakar.
>
> **KAYNAK: `DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md` (sahibin verdiği plan, 19.10.2026, birebir; düzenlenmez).**
> **Varsayılan (sahip 18.10.2026, BLACK_ACCORD: "plandan asla dışarı çıkma"; aksi söylenmedikçe sonraki planlarda da geçerli):** olay, sıra,
> kadraj, özne, eylem, nesne ve hasar durumu, 50 replik, ses davranışı, kapak ve yayın metni **planın kendisidir**. Fable'ın eklediği yalnız biçimdir:
> sütunlar, referans numaraları (plan R01-R07 · V01-V06 · M01-M06 · V01D V02D V04D → 1-22), C07-C48 referans/sektör eşlemesi (plan tablosundaki
> özne, araç, sektör sırası ve hasar tablosundan), §5 saniye/süre tahmini, kaynak sütunu (plan "ekran dışı iletişim"), §6 tablo düzeni.
> Hat kuralıyla plan çatışırsa: SÖZLEŞME/ARAÇ (film_dogrula M) yalnız biçim olarak uygulanır; HİPOTEZ/TERCİH plan lehine bırakılır
> (`NOTLAR.md` KARARLAR); plan içi çelişki sahibe sorulur (`ODA/DURUM.md` SAHİP CEVAPLARI).
> Faz 1-3 ajan turu açılmadı (plan = seçim, tretman, çekim listesi; RAIN_THIEF · BLACK_ACCORD yolu; `ODA/DURUM.md` AŞILAN KAPILAR).

---

## 1. HİKÂYE

```
LOGLINE   Beş uzaylı pilot kendi dünyalarını kurtarmak için yarışır; sonuncunun gezegeni, bir sonraki yarışın yakıtına çevrilecektir. En hızlı pilotlardan biri rakibini kurtardığında, iki düşman bitiş çizgisine saldırıp hasat mekanizmasını durdurmayı seçer.
AMAÇ      Raka önce kendi dünyası için sonuncu olmamak ister (C06: "Then I won't come last."); C24'ten sonra hasat kapısının iki beslemesini aynı darbede durdurmak (C24: "We end the race."; C20 "Two feeds. One cell in each. Same pulse.").
ENGEL     Thren'in sert manevrası, kırılan sol ön fren kanadı (C09-C10) · iki bağımsız besleme, aynı darbe (C20) · dış kapak araçlar kaçmadan kapanır (C21) · hücreler neredeyse boş (C22) · Kalix'in teklifi ve takip dronları (C27-C30) · Thren'in bozuk sağ arka motoru (C14 → C39).
KARAR     C15 — Raka sağdaki boş şeritten geçebilecekken geçmez, Fang'in önüne yerleşip akış izi açar ("No. He's rolling.") · C24 ortak kanal · C40 sağlam sağ fren kanadını açıp Thren'in hızına düşer ("Then I match yours.").
SONUÇ     C41-C43 iki hücre aynı anda bırakılır, iki besleme söner, beş dünyanın kilit çemberleri açılır; C48 beş yarış aracı + Axi'nin gri servis römorkörü kararmış hasat kapısından birlikte uzaklaşır.
BEDEL     yarışı kazanmak (C24) · Raka'nın ve Thren'in mavi hücreleri (C41, geri gelmez) · Korv'un sağ arka motoru (C29) · Axi'nin dünyası geri gelmez (C43) · sahne 41 · 43
TEK SORU  Raka ve Thren, iki hücreyi aynı darbede iki besleme kilidine ulaştırıp beş dünyayı kurtarabilecek mi?
SEÇİM     sahip planı (F1 aday turu yok) · 19.10.2026 · gerekçe: DEAD_LAST_8DK_48_KLIP_FILM_PLANI.md
SAHİP     ONAY (planın kendisi) · 19.10.2026
```

## 2. TRETMAN

<!-- sahne başına bir satır; her satır öncekinden doğar (seçim ya da başarısız deneme) -->
| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Bir saniye: Axi'nin eski yarış kokpitinde yakın portresi; arka camda mavi gezegen çatlamaktadır. İlk karede felaket başlamıştır. | PREVIOUS RACE yazısı ilk iki saniyede sonradan eklenir. Eski yarış; bu gezegen sonradan geri gelmez. |
| S2 | 0:10–0:20 | Yakıt: Gezegenden çekilen mavi enerji, beyaz arena halkasının depolarına akar; tüketilen dünyanın şehir ışıkları söner. | Axi'nin dünyası. Grafik şiddet veya ceset yok. Tek büyük çevre hareketi. |
| S3 | 0:20–0:30 | Bir sonraki yarış: Güncel hazırlık alanında Raka'nın beyaz-mavi aracının sırtına tek mavi yarış hücresi kilitlenir. | NEXT RACE yazısı kurguda. Mavi hücre yalnız hızlandırıcıyı besler; ana manevra motoru ayrı sistemdir. |
| S4 | 0:30–0:40 | Kaybedenler gitmez: Raka kokpitten yakındaki gri servis römorkörüne bakar; Axi'nin sesi iletişimden gelir. | Axi güncel sahnelerde servis römorküründedir; hâlâ arena işçisidir. |
| S5 | 0:40–0:50 | Beş dünya: Kalix'in altın yüzlü yayını; derinlikte beş renkli yarış şeridi, beş dünya işareti ve farklı uzaylı seyirciler. | Güncel yarışta beş pilot, beş aktif dünya kilidi. Axi bu beş pilotun içinde değildir. |
| S6 | 0:50–1:00 | Başla: Raka tek kişilik yarış koltuğunda kemerini gerer; kobalt ışık altın gözlerine yansır. | Kahramanın ilk hedefi kendi dünyasını koruyacak kadar hızlı olmaktır. Tanıtım logosu eklenmez. |
| S7 | 1:00–1:10 | Beş araç: Beş araç, manyetik şeritten dev asılı bitki kökleri arasına fırlar. İki araç önde ayrıntılı, diğerleri uzakta küçük silüet. | Beyaz-mavi Needle, kızıl-bronz Fang, altın Halo, hardal Bastion, gümüş-mor Sickle. Beş adet. |
| S8 | 1:10–1:20 | Yan yana: Thren'in bakır yüzüne yakın; Raka'nın beyaz aracı yan camda aynı yönde akar. | Thren görünür konuşan; Raka yanıtı ekran dışından. Dört turkuaz göz aynı 2×2 dizilimde. |
| S9 | 1:20–1:30 | Dar geçit: İki araç kök kemerinin dar boğazına yan yana yaklaşır; Thren çizgisini içeri kapatır. | Yarış yönü geniş dış planlarda soldan sağa. Araçlar ağaca dönüşmez. |
| S10 | 1:30–1:40 | Sol fren kanadı: Fang'in yan koruması Needle'ın sol ön fren kanadına vurur; beyaz kanadın ucu kopar. | Raka'nın yalnız sol ön fren kanadı hasarlanır. Sağ fren kanadı ve ana motorları sağlam. |
| S11 | 1:40–1:50 | Düşüş ihtimali: Raka kokpitinde aracın yana yatmasını düzeltmeye çalışır; arka planda kökler eğilir. | Acil hücre bırakma özelliği finalden çok önce kurulur. Hücre şu anda bırakılmaz. |
| S12 | 1:50–2:00 | Sağ kanat: Needle'ın sağlam sağ fren kanadı bir kez açılır; araç kontrollü biçimde düz şeride oturur. | Tek düzeltme. Sol ön kırık kanat geri gelmez. Sağ kanatla hız azaltma finalin hazırlığıdır. |
| S13 | 2:00–2:10 | Başlarının üstünde deniz: Yarış yolu, yerçekimi zarında asılı duran dev bir okyanusun altına girer; yukarıda dalgalar kırılır. | Aynı arenanın ayrı çevre bölümü; başka gezegene portal geçişi yok. |
| S14 | 2:10–2:20 | Dış motor: Thren'in sağ arka hız motoru, su kenarından kopan yoğun buharın içinden geçerken arızalanır; tek kısa kıvılcım. | Yalnız Thren'in sağ arka motoru arızalanır. Araç havada kalabilir ama tam hızını tutamaz. |
| S15 | 2:20–2:30 | Geçebilirdi: Raka önündeki yalpalayan Fang'e bakar; açık boş şerit sağda görünür. | Seçim Raka'ya ait; Axi emir vermez. Thren ekran dışı. |
| S16 | 2:30–2:40 | Akış izi: Needle, Fang'in hemen önüne geçerek kararlı mavi bir manyetik akış izi oluşturur; Fang bu izde dengelenir. | Yakın takipte öndeki aracın izi arkadakinin dengesini ve enerji tasarrufunu destekler. Yeni bir çekme kablosu yok. |
| S17 | 2:40–2:50 | Rakip: Thren kokpitinde nefesini toplar; Raka'nın sesi açık iletişim kanalından gelir. | Raka'nın sol fren hasarı, Thren'in sağ motor arızası devam eder. |
| S18 | 2:50–3:00 | Kapının altı: Axi'nin gri servis römorkörü, yarış kapısının altındaki bakım güzergâhında ağır ağır ilerler. | Axi'nin bakım erişimi ve hareketli servis gemisi açıkça gösterilir. Sonradan ışınlanmaz. |
| S19 | 3:00–3:10 | Tetik: Kapının altındaki gerçek kontrol yapısında beş dünya bağlantısı ve iki paralel enerji beslemesi görülür. | Bunlar beş uzak dünyanın bağlantı göstergeleri; gerçek gezegenler avuç büyüklüğünde fiziksel toplar değildir. |
| S20 | 3:10–3:20 | İki besleme: Axi servis kokpitinde iki enerji hattının basit şemasını işaret eder. | Sol hat amber, sağ hat camgöbeği. Şema ve ikonlar kurguda; modelden okunur yazı istenmez. |
| S21 | 3:20–3:30 | Kapak: Thren'in yakın portresi; iletişim yanıtı Axi'den ekran dışı gelir. | Ayrı iki besleme kanalına tek ortak bakım ağzından girilir. Dış kapak fiziksel engeldir. |
| S22 | 3:30–3:40 | Son hızlandırma: Raka'nın sırt hücresinin ışığı zayıflar; kokpitte kısa göstergesine bakar. | Hücreler hızlandırıcı yakıtıdır. Bırakılınca ana manevra motorları düşük güçte çalışmaya devam edebilir. |
| S23 | 3:40–3:50 | Üçüncü ses: Amber saydam yüzlü Sael, altın aracıyla iletişime katılır. | Sael'e ilk ayrıntılı portre. Akış izi kuralı C16'nın devamıdır; yakıt ışını icat edilmez. |
| S24 | 3:50–4:00 | Yarışı bitirmek: Raka kameraya yakın kokpit portresinde ortak kanalı açar. | Yeni hedef anlaşılır. Yarışın sonucu değil, hasat kapısının iki beslemesi durdurulacak. |
| S25 | 4:00–4:10 | Veli: Gümüş tüylü mor yüzlü Veli, ince hilal aracını alt bakım rotasına doğru yatırır. | Veli'nin aracı canlı bir yaratık değildir. Pilot mor, araç gümüş-mor. |
| S26 | 4:10–4:20 | Korv: Geniş mantar plakalı yüzü olan Korv, ağır hardal aracında kararsızdır. | Korv'un kaygısı kendi dünyasıdır; karikatür kötü değildir. |
| S27 | 4:20–4:30 | Ödül teklifi: Kalix'in altın yüzünde sakin bir gülümseme; parmaklarını gözlemci balkonunun korkuluğuna koyar. | Beyaz araç Raka'nın Needle'ıdır. Emir açıkça Korv'a gelir. |
| S28 | 4:30–4:40 | Seçim: Bastion, Raka'nın aracına çarpmak yerine takip dronlarıyla onun arasına girer. | Bu tek manevra Korv'un tarafını açıklar. Yakın planda iki araçtan fazlasını oynatma. |
| S29 | 4:40–4:50 | Bedel: Takip dronunun kısa atışı Bastion'un sağ arka motorunu devre dışı bırakır; diğer iki motor çalışır. | Korv'un üç motorundan yalnız sağ arka olanı kararır. Korv hayatta, araç uçabilir. |
| S30 | 4:50–5:00 | Takipçileri çekmek: Veli gümüş aracını dronların önünden geçirip onları kıvrılan metal fırtınası şeridine çeker. | Dronlar Veli'nin peşine döner; başka bir dekor veya yeni silah eklenmez. |
| S31 | 5:00–5:10 | Demir yağmuru: Sael önde, Raka ve Thren arkasında; manyetik demir yaprakların arasından kararlı akış izinde geçerler. | Öndeki Sael'in hızlandırıcısı çalışır. Raka ve Thren kendi yarış hücrelerini korur. Geniş planda yüz yok. |
| S32 | 5:10–5:20 | Kimin enerjisi: Raka kabinin camındaki mavi enerji izine bakar. | Axi'ye konuşur. Bu, filmin açılışına bilinçli dönüş. |
| S33 | 5:20–5:30 | Axi'nin cevabı: Axi servis kokpitinde çatlak olmayan ama yorgun yüzüyle cevap verir. | Axi'nin kaybı geri alınmaz. Kahramanlık duygusu kaybı silmekten değil, tekrarını önlemekten gelir. |
| S34 | 5:30–5:40 | Koridor açılır: Veli son iki dronu birbirine yaklaşan metal yaprakların dar aralığına yönlendirip alt rotaya kaçar. | Dronlar rotadan düşer. Veli yeni bir araçta veya yerde belirmez; alt şeride döner. |
| S35 | 5:40–5:50 | Kapak tutucu: Ağır Bastion, ortak bakım ağzının dış kapağına burnunu dayar; iki sağlam motoru itişi dengeler. | Korv kapıyı patlatmaz; aracıyla kapanmasını engeller. Motor hasarı hâlâ görünür. |
| S36 | 5:50–6:00 | Açılma anı: Axi servis kolunu kullanarak bakım temizleme çevrimini başlatır; ana beslemeler kapanmaz, giriş kapağı açılmaya başlar. | Axi'nin bakımdan gelen erişimi yalnız kapağı açar. Dünya kilitlerini tek başına kapatamaz. |
| S37 | 6:00–6:10 | İki yol: Ortak bakım ağzının içinde iki besleme kanalı ayrılır: Raka soldaki amber, Thren sağdaki camgöbeği hatta girer. | Dışarıdan arkalarından bakılır: Raka sol, Thren sağ. Bu yön final boyunca değişmez. |
| S38 | 6:10–6:20 | Raka'nın hattı: Needle dar sol kanalda ilerler; sırtındaki tek mavi hücre ve kırık sol fren kanadı aynı anda okunur. | Ana gövde ve hücre sağlam. Yarış hücresi hâlâ takılı. |
| S39 | 6:20–6:30 | Thren yetişemiyor: Fang sağ kanalda yavaş kalır; sağ arka motoru karanlık. | Hasar final için korunmuştu. Thren mucizevi biçimde hızlanmaz. |
| S40 | 6:30–6:40 | Eşit hız: Raka sağlam sağ fren kanadını kontrollü açarak hızını Thren'inkine düşürür. | C12'de kurulan sağ fren hareketi. Yarış kazanma içgüdüsünün yerine ortak zamanlama gelir. |
| S41 | 6:40–6:50 | Aynı darbe: Dıştan simetrik geniş planda iki mavi sırt hücresi aynı anda serbest kalır; araçlar yan çıkışlara süzülür. | İki hücre toplam: biri solda, biri sağda. Hücreler hareketlerini sürdürerek besleme halkalarına gider. Araçlar düşük güçlü ana motorla yan çıkışa devam eder. |
| S42 | 6:50–7:00 | Beslemeler söner: İki hücre kendi besleme kilitlerine aynı anda ulaşır; iki ışık birlikte aşırı yük darbesiyle söner. | Mekanizma kurgu teknolojisidir. Bütün arena veya gezegenler patlamaz; hasat beslemeleri ve kontrol kilitleri çöker. |
| S43 | 7:00–7:10 | Beş bağlantı: Kontrol yapısındaki beş dünya görüntüsü yerinde kalır; onları çevreleyen kilit çemberleri açılır ve hasat bağlantıları söner. | Beş güncel dünyanın renkli görüntüleri korunur. Sönenler kilitler ve hasat hatlarıdır. Axi'nin eski dünyası geri gelmez. |
| S44 | 7:10–7:20 | Birlikte çıkış: Korv, gücü kesilen kapaktan aracını geri alır. Sael'in izinde Raka ve Thren yan çıkışlardan güvenli rotaya ulaşır. | Geniş planda en fazla iki araç ayrıntılı, diğerleri küçük silüet. Korv, Raka ve Thren'in hasarları sürer; iki bırakılan hücre geri gelmez. |
| S45 | 7:20–7:30 | Axi ayrılıyor: Axi gri servis römorkörünün bağlantı kelepçesini açar; kokpit camından özgür rotaya yönelen araçlar görülür. | Axi de fiziksel olarak arenadan ayrılır. Hâlâ servis gemisindedir. |
| S46 | 7:30–7:40 | Seyirciler: Farklı türlerden uzaylılar tribünde suskunluk sonrası ayağa kalkar; Kalix'in yayını arka planda kararır. | Altı arka plan türü farklı silüetlerle görünür. Kalix'in yayını kararır; sonucun odağı dünya kilitlerinin kalkmasıdır. |
| S47 | 7:40–7:50 | Yeni yön: Raka düşük güçlü Needle kokpitinde Axi'nin servis gemisine yan gözle bakar. | Yarış bitmiştir, beş dünya kurtulmuştur. Bu bir yeni tehdit veya devam filmi düğümü değildir. |
| S48 | 7:50–8:00 | Altı araç: Beş yarış aracı ve Axi'nin gri servis römorkörü, kararmış hasat kapısından birlikte uzaklaşır. | Tam altı araç; altıncı yarışçı değil, servis gemisi. DEAD LAST son 1,5 saniyede kurguda eklenebilir. Süreye ek kart yok. |

## 3. GÖRSEL KİMLİK — onay dosyaya bağlıdır

| No | Referans | Dosya (`ref/`) | Sürüm | SHA-256 (ilk 12) | Onay | Kullanan çekimler |
|:--:|---|---|:--:|---|:--:|---|
| 1 | Raka — ana pilot (plan R01) | `1.RAKA_v1.png` | v1 | | ⬜ | C04 C06 C11 C15 C22 C24 C32 C47 |
| 2 | Thren — rakip (plan R02) | `2.THREN_v1.png` | v1 | | ⬜ | C08 C17 C21 |
| 3 | Axi — önceki yarışın kaybedeni (plan R03) | `3.AXI_v1.png` | v1 | | ⬜ | C01 C20 C33 C45 |
| 4 | Sael — akış izini açan pilot (plan R04) | `4.SAEL_v1.png` | v1 | | ⬜ | C23 |
| 5 | Korv — ağır aracın pilotu (plan R05) | `5.KORV_v1.png` | v1 | | ⬜ | C26 |
| 6 | Veli — takipçileri uzaklaştıran pilot (plan R06) | `6.VELI_v1.png` | v1 | | ⬜ | C25 |
| 7 | Kalix — yarışı yöneten (plan R07) | `7.KALIX_v1.png` | v1 | | ⬜ | C05 C27 C46 |
| 8 | Needle — Raka'nın aracı, sağlam (plan V01) | `8.NEEDLE_v1.png` | v1 | | ⬜ | C03 C04 C06 C07 C08 C09 C10 |
| 9 | Fang — Thren'in aracı, sağlam (plan V02) | `9.FANG_v1.png` | v1 | | ⬜ | C07 C09 C10 C14 |
| 10 | Halo — Sael'in aracı (plan V03) | `10.HALO_v1.png` | v1 | | ⬜ | C23 C31 C44 |
| 11 | Bastion — Korv'un aracı, sağlam (plan V04) | `11.BASTION_v1.png` | v1 | | ⬜ | C26 C28 C29 |
| 12 | Sickle — Veli'nin aracı (plan V05) | `12.SICKLE_v1.png` | v1 | | ⬜ | C25 C30 C34 |
| 13 | Axi'nin servis römorkörü (plan V06) | `13.ROMORKOR_v1.png` | v1 | | ⬜ | C04 C18 C20 C33 C36 C45 C47 C48 |
| 14 | Axi'nin eski dünyası (plan M01) | `14.ESKI_DUNYA_v1.png` | v1 | | ⬜ | C01 C02 |
| 15 | Hazırlık alanı (plan M02) | `15.HAZIRLIK_v1.png` | v1 | | ⬜ | C03 C05 |
| 16 | Asılı kökler bölümü (plan M03) | `16.KOKLER_v1.png` | v1 | | ⬜ | C07 C08 C09 C10 C11 C12 |
| 17 | Gökteki okyanus (plan M04) | `17.OKYANUS_v1.png` | v1 | | ⬜ | C13 C14 C15 C16 C17 C21 C22 C23 C24 C25 C26 C28 C29 |
| 18 | Metal fırtınası ve hasat kapısı (plan M05) | `18.HASAT_KAPISI_v1.png` | v1 | | ⬜ | C18 C19 C30 C31 C32 C34 C35 C36 C37 C38 C39 C40 C41 C42 C43 C44 C45 C48 |
| 19 | Uzaylı tribünü (plan M06) | `19.TRIBUN_v1.png` | v1 | | ⬜ | C05 C27 C46 |
| 20 | Needle — C10 sonrası hasar varyantı (plan V01D; 8'in düzenlemesi, yalnız sol ön fren kanadının ucu kopuk) · SAHİP İSTİSNASI (RAIN_THIEF 19.10.2026 "Plan geçerli" emsali: plan ayrı dosya ister) | `20.NEEDLE_HASAR_v1.png` | v1 | | ⬜ | C11 C12 C15 C16 C22 C24 C28 C31 C32 C37 C38 C40 C41 C47 C48 |
| 21 | Fang — C14 sonrası hasar varyantı (plan V02D; 9'un düzenlemesi, sağ arka dış motor karanlık) · SAHİP İSTİSNASI (aynı emsal) | `21.FANG_HASAR_v1.png` | v1 | | ⬜ | C15 C16 C31 C37 C39 C41 C48 |
| 22 | Bastion — C29 sonrası hasar varyantı (plan V04D; 11'in düzenlemesi, yalnız sağ motor karanlık) · SAHİP İSTİSNASI (aynı emsal) | `22.BASTION_HASAR_v1.png` | v1 | | ⬜ | C35 C44 |

```
Plan dosya adları → hat adları: R01 → 1.RAKA · R02 → 2.THREN · R03 → 3.AXI · R04 → 4.SAEL · R05 → 5.KORV · R06 → 6.VELI · R07 → 7.KALIX · V01 → 8.NEEDLE · V02 → 9.FANG · V03 → 10.HALO · V04 → 11.BASTION · V05 → 12.SICKLE · V06 → 13.ROMORKOR · M01 → 14.ESKI_DUNYA · M02 → 15.HAZIRLIK · M03 → 16.KOKLER · M04 → 17.OKYANUS · M05 → 18.HASAT_KAPISI · M06 → 19.TRIBUN · V01D → 20.NEEDLE_HASAR · V02D → 21.FANG_HASAR · V04D → 22.BASTION_HASAR.
Plan: "Raka, Thren ve Korv'un hasar varyantları ilgili sağlam araç görselinden düzenlenerek üretilir. Hasarlı aracı bağımsız başka bir tasarıma
dönüştürme." → önce 8 · 9 · 11, sonra onların düzenlemesiyle 20 · 21 · 22. "Her çekimde yalnız ilgili karakter, araç ve mekân referanslarını kullan."
Hasar tarifinde sol/sağ aracın kendi yönüne göredir; C37'deki besleme hatlarının sol/sağı arkadan bakan kamera yönüdür (plan).
SHA-256: shasum -a 256 ~/film_medya/DEAD_LAST/ref/<dosya> | cut -c1-12
Referans değişirse sürüm artar; "kullanan çekimler"in başlangıç kareleri yeniden üretilir.
No (sahip kararı 10.10.2026): film geneli, sabit; dosya adı <No>.<AD>_v<k>.png; §4 Referans sütunu "<No>.<AD>";
promptta "Reference <No> (<rol>)" anahtarı. Yeni özne sona, sıradaki numarayla; yeniden numaralama yok.
ÖZNE BAŞINA TEK SAYFA: bir karakterin açıları, yüz yakını ve durum değişimleri aynı görselde paneldir; "SELA_yuz",
"SELA_arka" gibi ikinci dosya açılmaz (film_dogrula hata). Yeni panel gerekirse sayfa yeniden üretilir, sürüm artar.
```

### KİMLİK CÜMLELERİ (16.10.2026 · F3p'de goruntu-yonetmeni yazar, pilot yoksa F5 G01 · Görsel promptta BİREBİR)

| No | Parça | Cümle (İngilizce, birebir) |
|:--:|---|---|
| 1 | Raka · tür | Raka, an adult nonhuman female-voiced racing pilot. |
| 1 | Raka · yüz | Chalk-white matte skin with fine dark branching veins, two wide horizontal gold eyes, low flat nose, a fixed low black cranial ridge, no hair or human ears. |
| 1 | Raka · giysi | Plain cobalt flight suit with an ivory neck seal, no helmet, empty hands. |
| 1 | Raka · giysi (elde tutuş kadrajı) † | Plain cobalt flight suit with an ivory neck seal, no helmet. |
| 1 | Raka · kollar | Two arms and two legs. |
| 1 | Raka · ifade | Alert resolute expression. |
| 2 | Thren · tür | Thren, an adult nonhuman racing pilot. |
| 2 | Thren · yüz † | Copper-brown living carapace, four small turquoise eyes permanently in a two-by-two arrangement, two rigid triangular cheek plates, one narrow horizontal mouth, no hair or human ears. |
| 2 | Thren · giysi | Dark crimson flight suit with a simple bronze restraint harness, no helmet, empty hands. |
| 2 | Thren · ifade | Proud controlled expression. |
| 3 | Axi · tür | Axi, an adult nonhuman former racing pilot now forced to work as a mechanic. |
| 3 | Axi · yüz | Soft smoke-gray face with two amber eyes and exactly four short fixed cheek sensory tendrils, compact head, no human ears or hair. |
| 3 | Axi · giysi | Plain worn charcoal utility flight suit, simple collar, no helmet or tools in hands. |
| 3 | Axi · ifade | Restrained grief and practical intelligence. |
| 4 | Sael · yüz + tür | Sael, an adult nonhuman pilot with a translucent warm-amber living face, two dark vertical eye slits and one small horizontal mouth. |
| 4 | Sael · kafatası | No visible human skull, no hair, no tentacles. |
| 4 | Sael · giysi | A fixed black support collar and a pale sage-gray flight suit, two gloved arms and two legs. |
| 4 | Sael · ifade | Calm compassionate demeanor. |
| 5 | Korv · tür | Korv, an adult nonhuman heavy racing pilot. |
| 5 | Korv · yüz † | Broad pale-green face formed from layered firm fungal plates, two dark crescent eyes, two short rigid feelers above the brow and one wide mouth seam. |
| 5 | Korv · giysi | Dark plum flight suit with practical plain shoulder padding. |
| 5 | Korv · ifade | Anxious strength rather than comedy, no helmet, empty hands. |
| 6 | Veli · tür | Veli, an adult nonhuman racing pilot. |
| 6 | Veli · yüz | Violet skin, short swept-back rigid silver cranial quills, two glossy black eyes and a small horizontal mouth. |
| 6 | Veli · baş | No recognizable terrestrial bird beak, no human hair or ears. |
| 6 | Veli · giysi | Two arms and legs, simple off-white flight suit, empty hands, no helmet. |
| 6 | Veli · ifade | Agile confident posture and a dry mischievous expression. |
| 7 | Kalix · tür | Kalix, an adult nonhuman arena ruler. |
| 7 | Kalix · yüz | Smooth living golden skin, exactly one vertical black eye centered high on the face and one small dark mouth below it. |
| 7 | Kalix · giysi + omuz şeridi | Matte black ceremonial clothing with one restrained crimson shoulder sash, no crown or weapon. |
| 7 | Kalix · ifade | Calm proprietary composure, never a robot. |
| 8 | Needle · gövde | Needle, a compact enclosed alien racing craft with a slim ivory hull, cobalt accents, exactly two short forward magnetic brake fins and two small rear maneuvering engines. |
| 8 | Needle · hücre | One detachable blue booster fuel cell is fixed lengthwise on the dorsal spine in a visible emergency latch cradle. |
| 8 | Needle · burun + kabin | Reinforced narrow nose, one pilot canopy, no weapons or wheels. |
| 9 | Fang · gövde | Fang, an enclosed long wedge-shaped alien racer, dark crimson hull with bronze side bumper rails. |
| 9 | Fang · motorlar | Exactly two prominent rear outer speed engines, one on each side, and discreet low-power maneuvering jets. |
| 9 | Fang · hücre | One blue dorsal detachable booster cell in a standard emergency cradle. |
| 9 | Fang · kabin | Single compact pilot canopy, no weapon. |
| 10 | Halo · gövde | Halo, a compact enclosed oval alien racing craft, warm-gold hull, one strong central rear drive and two short fixed stabilizer blades. |
| 10 | Halo · hücre + kabin | One single blue detachable booster cell on its dorsal spine, standard latch cradle, narrow one-pilot canopy. |
| 10 | Halo · siluet | Clean forward silhouette with no wings that flap, no weapons or wheels. |
| 11 | Bastion · gövde | Bastion, a broad heavy enclosed alien racer with a mustard-ochre hull and a reinforced flat nose bumper. |
| 11 | Bastion · motorlar † | Exactly three rear engines in a left-center-right row; all three active. |
| 11 | Bastion · hücre + kabin | One blue detachable booster cell on the dorsal spine, standard cradle, compact one-pilot canopy. |
| 11 | Bastion · tür | Heavy but clearly a racing vehicle, no gun or wheels. |
| 12 | Sickle · gövde | Sickle, a thin silver crescent-shaped enclosed alien racing craft with a violet central cockpit and one central rear engine. |
| 12 | Sickle · hücre | One blue dorsal detachable booster fuel cell in the same standard cradle system. |
| 12 | Sickle · geometri | Fixed rigid crescent geometry, not an animal and no flapping surfaces. |
| 13 | Römorkör · gövde | One small gray alien maintenance tug with a compact glazed pilot cabin, two short folded service arms beneath the hull and modest rear thrusters. |
| 13 | Römorkör · yüzey | Functional worn metal with a restrained amber work light, no blue racing booster cell, no weapon, no racing fins. |
| 13 | Römorkör · bağlantı | An identifiable docking clamp and service-control panel beside the cockpit. |
| 14 | Eski dünya · gezegen † | An inhabited blue ocean planet seen from orbit, thin white cloud bands and tiny city-light clusters on the dark limb. |
| 14 | Eski dünya · halka | A single vast artificial white harvester ring lies distant off to one side. |
| 14 | Eski dünya · gök | No other populated planet in the same sky. |
| 14 | Eski dünya · hâl | Photoreal science-fiction visual, not a scientific diagram. |
| 15 | Hazırlık · genel † | An alien orbital race preparation dock, matte white architecture, five distinct starting lanes and a separate gray maintenance berth. |
| 15 | Hazırlık · şerit | One continuous black magnetic race ribbon leaves the dock toward immense botanical structures in the distance. |
| 15 | Hazırlık · ışık | Hard violet space light with warm amber work lamps. |
| 15 | Hazırlık · ekipman † | Clear paths and compact service equipment. |
| 16 | Kökler · arena † | A single enormous engineered orbital racing arena. |
| 16 | Kökler · şerit + kemerler | A black magnetic track ribbon curves between giant hanging botanical root arches, with a visible safe travel line and vast depth below. |
| 16 | Kökler · kökler | Roots are stationary living scenery, not attacking monsters. |
| 16 | Kökler · destekler | Distant matte-white arena support structures maintain spatial continuity. |
| 16 | Kökler · doku † | Copper-green organic texture and violet-black space. |
| 17 | Okyanus · genel † | An engineered suspended ocean inside the same orbital race arena. |
| 17 | Okyanus · su | Huge dark-teal water masses and waves hang above a thin black race ribbon under a subtle gravity membrane. |
| 17 | Okyanus · şeritler | Two parallel racing lanes curve beneath the water canopy; white support pylons match the root sector. |
| 17 | Okyanus · hâl | Liquid water, no ice, no portal, no inhabited planet surface. |
| 18 | Hasat kapısı · sektör † | The final sector of one orbital race arena, floating iron-leaf structures framing a massive white finish arch. |
| 18 | Hasat kapısı · kapak + kanallar | Under the race deck is one broad maintenance shutter leading to two clearly separated energy-feed channels: amber on viewer-left, cyan on viewer-right. |
| 18 | Hasat kapısı · kilitler | Each feed has one vulnerable lock ring and a visible lateral exit passage before the lock. |
| 18 | Hasat kapısı · göstergeler | Five abstract distant-world link indicators form a row above the service core. |
| 19 | Tribün · genel † | A spectator stand populated entirely by nonhuman alien adults. |
| 19 | Tribün · türler | Six distinct background species with turquoise elongated heads, burgundy shell armor, frosted-violet crystalline faces, bronze fan-shaped heads, pale-green spherical glass-like heads, and white branching coral crowns. |
| 19 | Tribün · derinlik | Layered crowd depth, at most two detailed faces in focus, others in silhouette or soft focus. |
| 19 | Tribün · mimari | Matte white arena balconies, violet and amber light. |
| 20 | Needle hasar · sol kanat † | The outer tip of the craft's LEFT forward magnetic brake fin is removed, leaving a clear chipped broken edge. |
| 20 | Needle hasar · sağ kanat | The RIGHT forward brake fin remains complete. |
| 20 | Needle hasar · sınır | No extra damage, no fire, no new part. |
| 21 | Fang hasar · sağ motor | The craft's RIGHT rear outer engine is dark, lightly scorched and inactive. |
| 21 | Fang hasar · sol motor | The LEFT rear engine remains functional. |
| 21 | Fang hasar · hücre + kabin | Keep the single blue booster cell attached, same canopy and side rails, no missing pilot cabin or new weapon. |
| 22 | Bastion hasar · sağ motor | Of the three rear engines, only the craft's RIGHT engine is dark, lightly scorched and inactive; CENTER and LEFT remain functional. |
| 22 | Bastion hasar · sınır | No other new damage or geometry change, same reference camera and scale. |
| — | (F5 G01 `PROMPTLAR/G01.md` KİMLİK CÜMLELERİ'nden birebir, 20.10.2026; † notları orada) | — |
```
ORTAK GÖRÜNÜM (plan "Görsel üretim dili", birebir; plan: Görsel istemlerinin BAŞINA):
  Horizontal 16:9 cinematic science-fiction, photoreal nonhuman creature design, tactile practical-looking spacecraft, clear silhouette and consistent scale, deep violet space with cold cobalt and warm amber accents, restrained 35mm grain, readable dark areas, no human cast, no readable text, no logos or watermarks. Use only the supplied relevant character and craft references. Preserve exact eye count, head shape, costume, craft geometry and active damage state.
ORTAK HAREKET (plan, birebir; plan: video istemlerinin BAŞINA):
  Ten-second single continuous shot, at most one main physical action and one restrained camera move. Preserve the supplied starting-frame identity and geometry. One detailed speaking face at a time; other replies may be off-screen communications. Dialogue is the assigned performance text, not a claim that the selected video model produces audio. Do not add in-shot captions, random extra characters, extra fuel cells, extra engines or spontaneous repairs. Sound and clean dialogue may be added in editing.
SAHNE DÜZENİ (plan "Yarışın kurgu kuralları"): tek uzun parkur — kökler (M03), asılı okyanus (M04), metal fırtınası (M05) aynı yörünge arenasının üç bölümü;
  portal geçişi yok · yarış yönü geniş dış planlarda soldan sağa (C09) · bitiş bölgesine ilk kez sonda ulaşılır · hasat kapısının altında tek ortak bakım ağzı +
  dış kapak; içeride iki ayrı besleme: sol amber, sağ camgöbeği (arkadan bakan kamera), her hattın kilidinden önce yana açılan bakım çıkışı.
DÜNYA KURALLARI (plan): güncel yarışta beş pilot; Axi altıncı yarışçı değil, servis görevlisi · açılıştaki dünya gerçekten kaybedilir · yarış hücresi ≠ temel motor
  (hücre bırakılınca düşük güçlü manevra motorlarıyla çıkılır) · akış izi C16 gösterilir, C23 planlanır, C31 ve C44 kullanılır · iki besleme birlikte durmalı ·
  Axi yalnız kapak çevrimini başlatır · Korv dış kapağı tutar · bilimkurgu mekaniği, gerçek fizik iddiası değil.
DEVAMLILIK (plan "Hasar ve nesne devamlılığı" tablosu esastır): Needle sol ön fren kanadı C10'da kırılır, C11-C48 ucu eksik (C12 ve C40 SAĞ kanat) ·
  Fang sağ arka motor C14'te arızalanır, C15-C48 karanlık · Bastion sağ arka motor C29, diğer ikisi çalışır · Raka'nın hücresi C03 takılır, C04-C40 sırtta,
  C41 bırakılır, C42 sol beslemeye · Thren'in hücresi C41 bırakılır, C42 sağ beslemeye · Sael, Korv, Veli hücreleri araçta kalır · beş dünya işareti hep beş ·
  Axi'nin eski dünyası geri gelmez · Axi güncel sahnelerde gri servis römorköründe · finalde beş yarış aracı + bir servis gemisi = altı.
Kadrajda görünen her parça çekimin Görsel promptuna kelime kelime girer; kısaltılmaz, özne yeniden adlandırılmaz (5/5 filmde
kimlik kayması, ARASTIRMA/16 Y1-Y3). İşaret: sayı + taraf + konum + "the only marking". Nesne: biçim + ölçü + taraf.
film_dogrula DERS Y2: referansı eklenen çekimde hiçbir parçası birebir geçmeyen özneyi gösterir (uyarı).
ORTAK GÖRÜNÜM cümlesi (varsa) yalnız film boyu değişmeyeni taşır: kimlik + doku/stil. Işık, su, gezegen, ses mekân ya da çekim
cümlesine gider (DERS Y6).
```

## 4. ÇEKİM LİSTESİ

| No | Anlatacağı TEK bilgi | Ekranda görünen | Kadraj · kamera | Taraf / yön | Süre | Flow modu | Risk → nasıl gösterilir | Referans | Grup | Durum | Zincir | Baş. karesi | Bitiş karesi |
|:--:|---|---|---|---|:--:|---|---|---|:--:|:--:|:--:|:--:|:--:|
| C01 | Bir saniye: BİR DÜNYANIN BEDELİ bölümü | Axi'nin eski yarış kokpitinde yakın portresi; arka camda mavi gezegen çatlamaktadır. İlk karede felaket başlamıştır. | Horizontal cinematic frame inside a plain dark alien racing cockpit during a previous race. (prompt ilk cümlesi) | M01 Axi'nin eski dünyası (yörünge) · PREVIOUS RACE yazısı ilk iki saniyede sonradan eklenir. Eski yarış; bu gezegen sonradan geri gelmez. | 10 | Frames to Video | plan pilotu 1: aynı karede yüz ile gezegen kaybı okunuyor mu (plan "Önce denenmesi gereken üç çekim") | 3.AXI · 14.ESKI_DUNYA | G01 | ⬜ | — | — | — |
| C02 | Yakıt: BİR DÜNYANIN BEDELİ bölümü | Gezegenden çekilen mavi enerji, beyaz arena halkasının depolarına akar; tüketilen dünyanın şehir ışıkları söner. | Wide orbital view of the same already fractured inhabited blue world, with one distant artificial white harvester ring. (prompt ilk cümlesi) | M01 Axi'nin eski dünyası (yörünge) · Axi'nin dünyası. Grafik şiddet veya ceset yok. Tek büyük çevre hareketi. | 10 | Frames to Video | tek dünya, tek hasat halkası; grafik şiddet/ceset yok (plan) | 14.ESKI_DUNYA | G01 | ⬜ | — | — | — |
| C03 | Bir sonraki yarış: BİR DÜNYANIN BEDELİ bölümü | Güncel hazırlık alanında Raka'nın beyaz-mavi aracının sırtına tek mavi yarış hücresi kilitlenir. | Current-race preparation dock. (prompt ilk cümlesi) | M02 hazırlık alanı · NEXT RACE yazısı kurguda. Mavi hücre yalnız hızlandırıcıyı besler; ana manevra motoru ayrı sistemdir. | 10 | Frames to Video | tek hücre, iki sağlam ön fren kanadı (plan) | 8.NEEDLE · 15.HAZIRLIK | G01 | ⬜ | — | — | — |
| C04 | Kaybedenler gitmez: BİR DÜNYANIN BEDELİ bölümü | Raka kokpitten yakındaki gri servis römorkörüne bakar; Axi'nin sesi iletişimden gelir. | Inside Needle's compact one-pilot canopy. (prompt ilk cümlesi) | M02 hazırlık alanı · Axi güncel sahnelerde servis römorküründedir; hâlâ arena işçisidir. | 10 | Frames to Video | — | 1.RAKA · 8.NEEDLE · 13.ROMORKOR | G01 | ⬜ | — | — | — |
| C05 | Beş dünya: BİR DÜNYANIN BEDELİ bölümü | Kalix'in altın yüzlü yayını; derinlikte beş renkli yarış şeridi, beş dünya işareti ve farklı uzaylı seyirciler. | Kalix's exact smooth living-gold face with one vertical black eye and small dark mouth dominates a broadcast portrait above the white starting dock. (prompt ilk cümlesi) | M02 hazırlık alanı · Güncel yarışta beş pilot, beş aktif dünya kilidi. Axi bu beş pilotun içinde değildir. | 10 | Frames to Video | — | 7.KALIX · 15.HAZIRLIK · 19.TRIBUN | G01 | ⬜ | — | — | — |
| C06 | Başla: BİR DÜNYANIN BEDELİ bölümü | Raka tek kişilik yarış koltuğunda kemerini gerer; kobalt ışık altın gözlerine yansır. | Tight front three-quarter portrait of Raka inside the same Needle cockpit. (prompt ilk cümlesi) | M02 hazırlık alanı · Kahramanın ilk hedefi kendi dünyasını koruyacak kadar hızlı olmaktır. Tanıtım logosu eklenmez. | 10 | Frames to Video | — | 1.RAKA · 8.NEEDLE | G01 | ⬜ | — | — | — |
| C07 | Beş araç: KÖKLERİN ALTINDA bölümü | Beş araç, manyetik şeritten dev asılı bitki kökleri arasına fırlar. İki araç önde ayrıntılı, diğerleri uzakta küçük silüet. | Five alien racing craft are at the moment of launch on the black magnetic ribbon at the entrance of the giant hanging plant roots, noses pointing to screen righ (prompt ilk cümlesi) | M03 asılı kökler · Beyaz-mavi Needle, kızıl-bronz Fang, altın Halo, hardal Bastion, gümüş-mor Sickle. Beş adet. | 10 | Frames to Video | beş araç: iki önde ayrıntılı (Needle + Fang: Fable türetmesi, C08-C10 ikilisi), üçü küçük silüet (plan) | 8.NEEDLE · 9.FANG · 16.KOKLER | G01 | ⬜ | — | — | — |
| C08 | Yan yana: KÖKLERİN ALTINDA bölümü | Thren'in bakır yüzüne yakın; Raka'nın beyaz aracı yan camda aynı yönde akar. | Close portrait of Thren's copper face in three-quarter view inside the cockpit. (prompt ilk cümlesi) | M03 asılı kökler · Thren görünür konuşan; Raka yanıtı ekran dışından. Dört turkuaz göz aynı 2×2 dizilimde. | 10 | Frames to Video | — | 2.THREN · 8.NEEDLE · 16.KOKLER | G01 | ⬜ | — | — | — |
| C09 | Dar geçit: KÖKLERİN ALTINDA bölümü | İki araç kök kemerinin dar boğazına yan yana yaklaşır; Thren çizgisini içeri kapatır. | Wide exterior view from above and the side, race direction from left to right. (prompt ilk cümlesi) | M03 asılı kökler · Yarış yönü geniş dış planlarda soldan sağa. Araçlar ağaca dönüşmez. | 10 | Frames to Video | — | 8.NEEDLE · 9.FANG · 16.KOKLER | G02 | ⬜ | — | — | — |
| C10 | Sol fren kanadı: KÖKLERİN ALTINDA bölümü | Fang'in yan koruması Needle'ın sol ön fren kanadına vurur; beyaz kanadın ucu kopar. | Medium exterior view seen from high above (about 60 degrees down), race direction from left to right, the craft's right sides toward the camera, so the far left (prompt ilk cümlesi) | M03 asılı kökler · Raka'nın yalnız sol ön fren kanadı hasarlanır. Sağ fren kanadı ve ana motorları sağlam. | 10 | Frames to Video | yalnız sol ön fren kanadının ucu kopar; sağ kanat ve motorlar sağlam (plan) | 8.NEEDLE · 9.FANG · 16.KOKLER | G02 | ⬜ | — | — | — |
| C11 | Düşüş ihtimali: KÖKLERİN ALTINDA bölümü | Raka kokpitinde aracın yana yatmasını düzeltmeye çalışır; arka planda kökler eğilir. | Medium three-quarter side view from Raka's right, inside Needle's compact one-pilot canopy, race direction from left to right. (prompt ilk cümlesi) | M03 asılı kökler · Acil hücre bırakma özelliği finalden çok önce kurulur. Hücre şu anda bırakılmaz. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 16.KOKLER | G02 | ⬜ | — | — | — |
| C12 | Sağ kanat: KÖKLERİN ALTINDA bölümü | Needle'ın sağlam sağ fren kanadı bir kez açılır; araç kontrollü biçimde düz şeride oturur. | Medium exterior view from above and the side, race direction from left to right, Needle's right side toward the camera. (prompt ilk cümlesi) | M03 asılı kökler · Tek düzeltme. Sol ön kırık kanat geri gelmez. Sağ kanatla hız azaltma finalin hazırlığıdır. | 10 | Frames to Video | — | 20.NEEDLE_HASAR · 16.KOKLER | G02 | ⬜ | — | — | — |
| C13 | Başlarının üstünde deniz: GÖĞÜN OKYANUSU bölümü | Yarış yolu, yerçekimi zarında asılı duran dev bir okyanusun altına girer; yukarıda dalgalar kırılır. | Wide low exterior view along the thin black race ribbon, which runs from left to right and is about to pass beneath a vast engineered ocean that hangs in a grav (prompt ilk cümlesi) | M04 gökteki okyanus · Aynı arenanın ayrı çevre bölümü; başka gezegene portal geçişi yok. | 10 | Frames to Video | — | 17.OKYANUS | G02 | ⬜ | — | — | — |
| C14 | Dış motor: GÖĞÜN OKYANUSU bölümü | Thren'in sağ arka hız motoru, su kenarından kopan yoğun buharın içinden geçerken arızalanır; tek kısa kıvılcım. | Medium exterior view from the side and slightly above, race direction from left to right, Fang's right side toward the camera so its right rear outer engine is  (prompt ilk cümlesi) | M04 gökteki okyanus · Yalnız Thren'in sağ arka motoru arızalanır. Araç havada kalabilir ama tam hızını tutamaz. | 10 | Frames to Video | yalnız sağ arka motor; tek kısa kıvılcım (plan) | 9.FANG · 17.OKYANUS | G02 | ⬜ | — | — | — |
| C15 | Geçebilirdi: GÖĞÜN OKYANUSU bölümü | Raka önündeki yalpalayan Fang'e bakar; açık boş şerit sağda görünür. | Medium three-quarter side view from Raka's right, inside Needle's compact one-pilot canopy, race direction from left to right. (prompt ilk cümlesi) | M04 gökteki okyanus · Seçim Raka'ya ait; Axi emir vermez. Thren ekran dışı. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 21.FANG_HASAR · 17.OKYANUS | G02 | ⬜ | — | — | — |
| C16 | Akış izi: GÖĞÜN OKYANUSU bölümü | Needle, Fang'in hemen önüne geçerek kararlı mavi bir manyetik akış izi oluşturur; Fang bu izde dengelenir. | Wide exterior view seen from high above (about 60 degrees down), race direction from left to right, the craft's right sides toward the camera, so the far left f (prompt ilk cümlesi) | M04 gökteki okyanus · Yakın takipte öndeki aracın izi arkadakinin dengesini ve enerji tasarrufunu destekler. Yeni bir çekme kablosu yok. | 10 | Frames to Video | plan pilotu 2: iki aracın akış izinde dengelenmesi kimlik değişmeden okunuyor mu (plan) | 20.NEEDLE_HASAR · 21.FANG_HASAR · 17.OKYANUS | G02 | ⬜ | — | — | — |
| C17 | Rakip: GÖĞÜN OKYANUSU bölümü | Thren kokpitinde nefesini toplar; Raka'nın sesi açık iletişim kanalından gelir. | Close portrait of Thren in his cockpit, three-quarter view, facing screen right, catching his breath. (prompt ilk cümlesi) | M04 gökteki okyanus · Raka'nın sol fren hasarı, Thren'in sağ motor arızası devam eder. | 10 | Frames to Video | — | 2.THREN · 17.OKYANUS | G03 | ⬜ | — | — | — |
| C18 | Kapının altı: GÖĞÜN OKYANUSU bölümü | Axi'nin gri servis römorkörü, yarış kapısının altındaki bakım güzergâhında ağır ağır ilerler. | Wide exterior view, race direction from left to right: Axi's small gray maintenance tug moves heavily along its maintenance route beneath the race gate, under t (prompt ilk cümlesi) | M05 hasat kapısının altı (bakım güzergâhı) · Axi'nin bakım erişimi ve hareketli servis gemisi açıkça gösterilir. Sonradan ışınlanmaz. | 10 | Frames to Video | — | 13.ROMORKOR · 18.HASAT_KAPISI | G03 | ⬜ | — | — | — |
| C19 | Tetik: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Kapının altındaki gerçek kontrol yapısında beş dünya bağlantısı ve iki paralel enerji beslemesi görülür. | Wide view of the real control structure beneath the harvest gate, seen from the maintenance route under the race deck, with the white finish arch and the floati (prompt ilk cümlesi) | M05 hasat kapısının altı (bakım güzergâhı) · Bunlar beş uzak dünyanın bağlantı göstergeleri; gerçek gezegenler avuç büyüklüğünde fiziksel toplar değildir. | 10 | Frames to Video | — | 18.HASAT_KAPISI | G03 | ⬜ | — | — | — |
| C20 | İki besleme: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Axi servis kokpitinde iki enerji hattının basit şemasını işaret eder. | Medium shot inside the glazed pilot cabin of the gray maintenance tug, Axi facing screen right. (prompt ilk cümlesi) | M05 hasat kapısının altı (bakım güzergâhı) · Sol hat amber, sağ hat camgöbeği. Şema ve ikonlar kurguda; modelden okunur yazı istenmez. | 10 | Frames to Video | şema ve ikonlar kurguda; modelden okunur yazı yok (plan) | 3.AXI · 13.ROMORKOR | G03 | ⬜ | — | — | — |
| C21 | Kapak: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Thren'in yakın portresi; iletişim yanıtı Axi'den ekran dışı gelir. | Close portrait of Thren inside his cockpit, facing screen right, his copper face dominating the frame, listening toward an off-screen communication. (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Ayrı iki besleme kanalına tek ortak bakım ağzından girilir. Dış kapak fiziksel engeldir. | 10 | Frames to Video | — | 2.THREN · 17.OKYANUS | G03 | ⬜ | — | — | — |
| C22 | Son hızlandırma: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Raka'nın sırt hücresinin ışığı zayıflar; kokpitte kısa göstergesine bakar. | Medium close-up of Raka inside Needle's compact one-pilot canopy, facing screen right, the cool-blue glow of her dorsal booster cell still steady on her face an (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Hücreler hızlandırıcı yakıtıdır. Bırakılınca ana manevra motorları düşük güçte çalışmaya devam edebilir. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 17.OKYANUS | G03 | ⬜ | — | — | — |
| C23 | Üçüncü ses: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Amber saydam yüzlü Sael, altın aracıyla iletişime katılır. | First detailed portrait of Sael in three-quarter view, facing screen right, inside the narrow one-pilot canopy of the warm-gold craft Halo, joining the shared c (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Sael'e ilk ayrıntılı portre. Akış izi kuralı C16'nın devamıdır; yakıt ışını icat edilmez. | 10 | Frames to Video | — | 4.SAEL · 10.HALO · 17.OKYANUS | G03 | ⬜ | — | — | — |
| C24 | Yarışı bitirmek: BİTİŞ ÇİZGİSİNİN İÇİ bölümü | Raka kameraya yakın kokpit portresinde ortak kanalı açar. | Close cockpit portrait of Raka near the camera inside Needle's compact one-pilot canopy, her face filling the frame, facing screen right, her two gold eyes set  (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Yeni hedef anlaşılır. Yarışın sonucu değil, hasat kapısının iki beslemesi durdurulacak. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 17.OKYANUS | G03 | ⬜ | — | — | — |
| C25 | Veli: BAŞKA BİR CELLAT BUL bölümü | Gümüş tüylü mor yüzlü Veli, ince hilal aracını alt bakım rotasına doğru yatırır. | Medium close three-quarter portrait of Veli, the violet-faced pilot with silver cranial quills, seated in the violet central cockpit of her thin silver crescent (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Veli'nin aracı canlı bir yaratık değildir. Pilot mor, araç gümüş-mor. | 10 | Frames to Video | — | 6.VELI · 12.SICKLE · 17.OKYANUS | G04 | ⬜ | — | — | — |
| C26 | Korv: BAŞKA BİR CELLAT BUL bölümü | Geniş mantar plakalı yüzü olan Korv, ağır hardal aracında kararsızdır. | Inside Bastion's compact one-pilot canopy. (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Korv'un kaygısı kendi dünyasıdır; karikatür kötü değildir. | 10 | Frames to Video | — | 5.KORV · 11.BASTION · 17.OKYANUS | G04 | ⬜ | — | — | — |
| C27 | Ödül teklifi: BAŞKA BİR CELLAT BUL bölümü | Kalix'in altın yüzünde sakin bir gülümseme; parmaklarını gözlemci balkonunun korkuluğuna koyar. | Medium close-up of Kalix's golden face with a calm smile on the arena's observer balcony, his one vertical black eye looking out past the railing toward the rac (prompt ilk cümlesi) | M06 gözlemci balkonu · Beyaz araç Raka'nın Needle'ıdır. Emir açıkça Korv'a gelir. | 10 | Frames to Video | — | 7.KALIX · 19.TRIBUN | G04 | ⬜ | — | — | — |
| C28 | Seçim: BAŞKA BİR CELLAT BUL bölümü | Bastion, Raka'nın aracına çarpmak yerine takip dronlarıyla onun arasına girer. | Wide exterior view seen from high above (about 60 degrees down) and the side, race direction from left to right, the craft's right sides toward the camera so th (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Bu tek manevra Korv'un tarafını açıklar. Yakın planda iki araçtan fazlasını oynatma. | 10 | Frames to Video | yakın planda iki araçtan fazlası oynamaz (plan); dron tasarımının referansı planda yok | 11.BASTION · 20.NEEDLE_HASAR · 17.OKYANUS | G04 | ⬜ | — | — | — |
| C29 | Bedel: BAŞKA BİR CELLAT BUL bölümü | Takip dronunun kısa atışı Bastion'un sağ arka motorunu devre dışı bırakır; diğer iki motor çalışır. | Rear three-quarter view from behind and slightly above of heavy mustard-ochre Bastion flying away along the black race ribbon beneath the hanging ocean. (prompt ilk cümlesi) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) · Korv'un üç motorundan yalnız sağ arka olanı kararır. Korv hayatta, araç uçabilir. | 10 | Frames to Video | üç motordan yalnız sağ arka kararır; Korv hayatta (plan) | 11.BASTION · 17.OKYANUS | G04 | ⬜ | — | — | — |
| C30 | Takipçileri çekmek: BAŞKA BİR CELLAT BUL bölümü | Veli gümüş aracını dronların önünden geçirip onları kıvrılan metal fırtınası şeridine çeker. | Wide exterior view, race direction from left to right. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Dronlar Veli'nin peşine döner; başka bir dekor veya yeni silah eklenmez. | 10 | Frames to Video | — | 12.SICKLE · 18.HASAT_KAPISI | G04 | ⬜ | — | — | — |
| C31 | Demir yağmuru: SON YAKIT bölümü | Sael önde, Raka ve Thren arkasında; manyetik demir yaprakların arasından kararlı akış izinde geçerler. | Wide exterior view from behind and slightly above, the three craft in single file travelling away toward the right of the frame between floating magnetic iron-l (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Öndeki Sael'in hızlandırıcısı çalışır. Raka ve Thren kendi yarış hücrelerini korur. Geniş planda yüz yok. | 10 | Frames to Video | — | 10.HALO · 20.NEEDLE_HASAR · 21.FANG_HASAR · 18.HASAT_KAPISI | G04 | ⬜ | — | — | — |
| C32 | Kimin enerjisi: SON YAKIT bölümü | Raka kabinin camındaki mavi enerji izine bakar. | Inside Needle's compact one-pilot canopy. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Axi'ye konuşur. Bu, filmin açılışına bilinçli dönüş. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 18.HASAT_KAPISI | G04 | ⬜ | — | — | — |
| C33 | Axi'nin cevabı: SON YAKIT bölümü | Axi servis kokpitinde çatlak olmayan ama yorgun yüzüyle cevap verir. | Medium close-up of Axi inside the service cockpit of his gray maintenance tug, three-quarter view facing screen right, his tired face calm and unbroken. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Axi'nin kaybı geri alınmaz. Kahramanlık duygusu kaybı silmekten değil, tekrarını önlemekten gelir. | 10 | Frames to Video | — | 3.AXI · 13.ROMORKOR | G05 | ⬜ | — | — | — |
| C34 | Koridor açılır: SON YAKIT bölümü | Veli son iki dronu birbirine yaklaşan metal yaprakların dar aralığına yönlendirip alt rotaya kaçar. | Wide exterior view from the side, race direction from left to right. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Dronlar rotadan düşer. Veli yeni bir araçta veya yerde belirmez; alt şeride döner. | 10 | Frames to Video | — | 12.SICKLE · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C35 | Kapak tutucu: SON YAKIT bölümü | Ağır Bastion, ortak bakım ağzının dış kapağına burnunu dayar; iki sağlam motoru itişi dengeler. | Rear three-quarter elevated view of Korv's Bastion approaching the outer shutter of the common maintenance mouth beneath the race deck. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Korv kapıyı patlatmaz; aracıyla kapanmasını engeller. Motor hasarı hâlâ görünür. | 10 | Frames to Video | — | 22.BASTION_HASAR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C36 | Açılma anı: SON YAKIT bölümü | Axi servis kolunu kullanarak bakım temizleme çevrimini başlatır; ana beslemeler kapanmaz, giriş kapağı açılmaya başlar. | Medium-wide exterior view from behind and slightly above the tug, looking toward the shutter, beneath the race deck of the final sector. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Axi'nin bakımdan gelen erişimi yalnız kapağı açar. Dünya kilitlerini tek başına kapatamaz. | 10 | Frames to Video | — | 13.ROMORKOR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C37 | İki yol: KAZANMAK İÇİN YAVAŞLA bölümü | Ortak bakım ağzının içinde iki besleme kanalı ayrılır: Raka soldaki amber, Thren sağdaki camgöbeği hatta girer. | View from behind and slightly above, looking toward the common maintenance mouth beneath the race deck as they approach it, its two energy-feed channels still j (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Dışarıdan arkalarından bakılır: Raka sol, Thren sağ. Bu yön final boyunca değişmez. | 10 | Frames to Video | — | 20.NEEDLE_HASAR · 21.FANG_HASAR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C38 | Raka'nın hattı: KAZANMAK İÇİN YAVAŞLA bölümü | Needle dar sol kanalda ilerler; sırtındaki tek mavi hücre ve kırık sol fren kanadı aynı anda okunur. | View from behind-left and slightly above of Raka's Needle moving along the narrow amber energy-feed channel on viewer-left. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Ana gövde ve hücre sağlam. Yarış hücresi hâlâ takılı. | 10 | Frames to Video | — | 20.NEEDLE_HASAR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C39 | Thren yetişemiyor: KAZANMAK İÇİN YAVAŞLA bölümü | Fang sağ kanalda yavaş kalır; sağ arka motoru karanlık. | View from behind and slightly above of Thren's Fang flying along the energy-feed channel on viewer-right, the cyan channel. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Hasar final için korunmuştu. Thren mucizevi biçimde hızlanmaz. | 10 | Frames to Video | — | 21.FANG_HASAR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C40 | Eşit hız: KAZANMAK İÇİN YAVAŞLA bölümü | Raka sağlam sağ fren kanadını kontrollü açarak hızını Thren'inkine düşürür. | View from behind-right and slightly above of Raka's Needle running along its narrow energy-feed channel at racing pace. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · C12'de kurulan sağ fren hareketi. Yarış kazanma içgüdüsünün yerine ortak zamanlama gelir. | 10 | Frames to Video | — | 20.NEEDLE_HASAR · 18.HASAT_KAPISI | G05 | ⬜ | — | — | — |
| C41 | Aynı darbe: KAZANMAK İÇİN YAVAŞLA bölümü | Dıştan simetrik geniş planda iki mavi sırt hücresi aynı anda serbest kalır; araçlar yan çıkışlara süzülür. | Symmetric wide exterior view from behind and slightly above, centered between two feed channels under the harvest gate. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · İki hücre toplam: biri solda, biri sağda. Hücreler hareketlerini sürdürerek besleme halkalarına gider. Araçlar düşük güçlü ana motorla yan çıkışa devam eder. | 10 | Frames to Video | plan pilotu 3: iki araç, iki hücre, iki çıkış doğru yönde mi; plan yedeği: bozulursa aynı 10 s birimde sol kilit · sağ kilit · genel görünüm ayrı kaynak çekimlerden (plan) | 20.NEEDLE_HASAR · 21.FANG_HASAR · 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |
| C42 | Beslemeler söner: KAZANMAK İÇİN YAVAŞLA bölümü | İki hücre kendi besleme kilitlerine aynı anda ulaşır; iki ışık birlikte aşırı yük darbesiyle söner. | Symmetric wide interior view looking down the two energy-feed channels under the harvest gate, the amber channel on viewer-left and the cyan channel on viewer-r (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Mekanizma kurgu teknolojisidir. Bütün arena veya gezegenler patlamaz; hasat beslemeleri ve kontrol kilitleri çöker. | 10 | Frames to Video | arena ve gezegenler patlamaz; yalnız beslemeler ve kilitler (plan) | 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |
| C43 | Beş bağlantı: ÇİZGİNİN ÖTESİNDE bölümü | Kontrol yapısındaki beş dünya görüntüsü yerinde kalır; onları çevreleyen kilit çemberleri açılır ve hasat bağlantıları söner. | Wide view of the control structure under the harvest gate. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Beş güncel dünyanın renkli görüntüleri korunur. Sönenler kilitler ve hasat hatlarıdır. Axi'nin eski dünyası geri gelmez. | 10 | Frames to Video | — | 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |
| C44 | Birlikte çıkış: ÇİZGİNİN ÖTESİNDE bölümü | Korv, gücü kesilen kapaktan aracını geri alır. Sael'in izinde Raka ve Thren yan çıkışlardan güvenli rotaya ulaşır. | Wide exterior view, race direction from left to right. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Geniş planda en fazla iki araç ayrıntılı, diğerleri küçük silüet. Korv, Raka ve Thren'in hasarları sürer; iki bırakılan hücre geri gelmez. | 10 | Frames to Video | en fazla iki araç ayrıntılı, diğerleri küçük silüet (plan) | 10.HALO · 22.BASTION_HASAR · 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |
| C45 | Axi ayrılıyor: ÇİZGİNİN ÖTESİNDE bölümü | Axi gri servis römorkörünün bağlantı kelepçesini açar; kokpit camından özgür rotaya yönelen araçlar görülür. | Medium three-quarter view of Axi inside the compact glazed pilot cabin of the gray maintenance tug. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Axi de fiziksel olarak arenadan ayrılır. Hâlâ servis gemisindedir. | 10 | Frames to Video | — | 3.AXI · 13.ROMORKOR · 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |
| C46 | Seyirciler: ÇİZGİNİN ÖTESİNDE bölümü | Farklı türlerden uzaylılar tribünde suskunluk sonrası ayağa kalkar; Kalix'in yayını arka planda kararır. | Wide view of the alien spectator stand, slightly from below, the crowd still seated in a quiet moment after the race, six different species in different silhoue (prompt ilk cümlesi) | M06 tribün · Altı arka plan türü farklı silüetlerle görünür. Kalix'in yayını kararır; sonucun odağı dünya kilitlerinin kalkmasıdır. | 10 | Frames to Video | — | 19.TRIBUN · 7.KALIX | G06 | ⬜ | — | — | — |
| C47 | Yeni yön: ÇİZGİNİN ÖTESİNDE bölümü | Raka düşük güçlü Needle kokpitinde Axi'nin servis gemisine yan gözle bakar. | Inside Needle's compact one-pilot canopy, medium close-up of Raka facing screen right, her eyes turned sideways toward a small gray maintenance tug outside the  (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Yarış bitmiştir, beş dünya kurtulmuştur. Bu bir yeni tehdit veya devam filmi düğümü değildir. | 10 | Frames to Video | — | 1.RAKA · 20.NEEDLE_HASAR · 13.ROMORKOR | G06 | ⬜ | — | — | — |
| C48 | Altı araç: ÇİZGİNİN ÖTESİNDE bölümü | Beş yarış aracı ve Axi'nin gri servis römorkörü, kararmış hasat kapısından birlikte uzaklaşır. | Wide exterior view, race direction from left to right. (prompt ilk cümlesi) | M05 metal fırtınası ve hasat kapısı · Tam altı araç; altıncı yarışçı değil, servis gemisi. DEAD LAST son 1,5 saniyede kurguda eklenebilir. Süreye ek kart yok. | 10 | Frames to Video | tam altı araç (plan) | 20.NEEDLE_HASAR · 21.FANG_HASAR · 13.ROMORKOR · 18.HASAT_KAPISI | G06 | ⬜ | — | — | — |

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
| 0-10 | C01 | İlk karede Axi'nin dünyası çatlamaya başlamıştır (plan); kokpit camında mavi gezegen çatlıyor. | yüz: Axi (yakın portre) | AXI: "Please. My family's still there." · PREVIOUS RACE ilk iki saniyede kurguda (plan) | çatlayan tek mavi dünya (plan kapağı) | evet: yüz + çatlak |
| 10-20 | C02 | Dünyanın enerjisi yarış deposuna çekilir, şehir ışıkları söner (plan). | yok | SYSTEM: "Conversion complete. Booster fuel ready." · yok | aynı dünya | evet: enerji akışı + sönen ışıklar |
| 20-30 | C03 | Raka'nın aracına mavi hücre takılır; Axi'nin sesi (plan: "Dünya yıkımı ile küçük fiziksel hücre arasındaki bağlantı ilk yarım dakikada anlaşılır"). | el: yükleyicinin eldivenli elleri | AXI: "That's my world in your booster." · NEXT RACE kurguda (plan) | Needle (kapakta) | kısmen: bağ replikle kurulur |

```
Plan: giriş logosu yok · PREVIOUS RACE / NEXT RACE yazıları kurguda · tanıtım logosu eklenmez (C06) · DEAD LAST son 1,5 s'de kurguda, süreye ek kart yok (C48).
İlk 60 saniye (plan): Kalix kuralı (C05) · "Then I won't come last." / "Everybody says that." (C06) · tam birinci dakikada beş araç fırlar (C07).
ILK_30 sapması (plan korundu): C01'de yazı katmanı (PREVIOUS RACE) ilk iki saniyede; C02 insan yok, saf yörünge planı — planın kendisi.
```

## 5. REPLİKLER

<!-- REPLIK yok ise tablo boş kalır -->
| No | Çekim | Saniye | Konuşan | Kaynak | Kayıt | Metin (İngilizce) | Süre |
|:--:|:--:|:--:|---|---|:--:|---|:--:|
| R01 | C01 | 2.2 | Axi | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Please. My family's still there. | 2.0 |
| R02 | C02 | 3.0 | System | makine — sistem sesi, görüntünün üstüne, kurguda (plan: "no speaking face") | MACHINE | Conversion complete. Booster fuel ready. | 2.0 |
| R03 | C03 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | That's my world in your booster. | 2.5 |
| R04 | C04 | 1.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Why are you still here? | 2.0 |
| R05 | C04 | 3.8 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | They don't let losers leave. | 2.0 |
| R06 | C05 | 1.0 | Kalix | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Five racers. Last place feeds the next race. | 3.0 |
| R07 | C06 | 1.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Then I won't come last. | 2.0 |
| R08 | C06 | 3.8 | Kalix | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Everybody says that. | 1.5 |
| R09 | C08 | 1.0 | Thren | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Stay behind me. | 1.5 |
| R10 | C08 | 3.3 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | That's the plan you brought? | 2.0 |
| R11 | C09 | 1.0 | Thren | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Your planet isn't my problem. | 2.0 |
| R12 | C09 | 3.8 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | It will be if you hit me. | 3.0 |
| R13 | C11 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | If you roll, eject the cell. Don't let it take the ship. | 4.5 |
| R14 | C11 | 6.3 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Not yet. | 1.0 |
| R15 | C14 | 1.0 | Thren | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Outer engine's failing. | 1.5 |
| R16 | C14 | 3.3 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Hold the lower lane. | 1.5 |
| R17 | C15 | 1.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | I can pass him. | 1.5 |
| R18 | C15 | 3.3 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Yes. You can. | 1.5 |
| R19 | C15 | 5.6 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | No. He's rolling. | 1.5 |
| R20 | C17 | 1.0 | Thren | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Why save me? That was your chance. | 3.0 |
| R21 | C17 | 4.8 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | I'm racing you. Not burying you. | 2.5 |
| R22 | C18 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | That gate isn't just timing you. Look beneath the finish lights. | 4.0 |
| R23 | C19 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Crossing the finish arms the harvester. It already has your coordinates. | 4.0 |
| R24 | C20 | 4.5 | Axi | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Two feeds. One cell in each. Same pulse. | 3.0 |
| R25 | C21 | 1.0 | Thren | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | They'll seal before we get clear. | 2.5 |
| R26 | C21 | 4.3 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Unless someone holds the outer shutter. | 2.5 |
| R27 | C22 | 1.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Our cells are nearly dry. | 2.0 |
| R28 | C22 | 3.8 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Enough for the locks. Don't waste another burn. | 3.0 |
| R29 | C23 | 1.0 | Sael | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Ride my wake. Save your last burn. I've got the lead. | 4.0 |
| R30 | C24 | 1.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Nobody crosses the line. We end the race. All five worlds stay alive. | 5.0 |
| R31 | C25 | 1.0 | Veli | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Tell me where to fly. I'm tired of losing people. | 4.0 |
| R32 | C26 | 1.0 | Korv | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | You'll kill us before he does. My world is waiting for me. | 4.5 |
| R33 | C27 | 1.0 | Kalix | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Ram the white ship. Your world goes free. Don't make me ask twice. | 5.0 |
| R34 | C28 | 1.0 | Korv | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Find another executioner. I'm a pilot. | 2.5 |
| R35 | C30 | 1.0 | Veli | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Keep your eyes on me. I'm the interesting one. | 3.5 |
| R36 | C32 | 4.0 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | We're still burning your world. I feel it every time I boost. | 4.5 |
| R37 | C33 | 1.0 | Axi | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Then make it the last world they ever burn. Don't waste it. | 4.5 |
| R38 | C34 | 6.0 | Veli | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | You're welcome. Try surviving it. | 2.0 |
| R39 | C35 | 1.0 | Korv | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Go. I'm holding the door. Don't make me do this twice. | 4.0 |
| R40 | C36 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Purge in ten. Both feeds together. No second attempt. | 3.5 |
| R41 | C38 | 5.5 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | I'm in position. Thren, where are you? | 3.0 |
| R42 | C39 | 1.0 | Thren | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Can't match your speed. Outer engine's gone. I won't make the pulse. | 4.5 |
| R43 | C40 | 1.0 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Then I match yours. Nobody gets left behind this time. | 4.0 |
| R44 | C41 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Now. | 1.0 |
| R45 | C42 | 1.0 | Kalix | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Stop them! I gave you worlds! | 2.5 |
| R46 | C44 | 1.0 | Sael | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Stay in my wake. All of you. Keep those engines low. | 4.0 |
| R47 | C45 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Tell me your world is still there. | 3.0 |
| R48 | C45 | 4.8 | Raka | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | All five. Axi, you're clear. | 2.0 |
| R49 | C47 | 1.0 | Axi | telsiz — kadraj dışı, dudak oynamaz; kurguda (plan: ekran dışı iletişim) | HUMAN | Where do we go? | 1.5 |
| R50 | C47 | 3.3 | Raka | ağız kadrajda — temiz replik ayrı kayıt, kurguda (plan: model sesi varsayılmaz) | HUMAN | Somewhere without a finish line. | 2.0 |

```
Kaynak: telsiz · kadraj dışı · kask içi · makine · kayıt → ses kurguda eklenir, ≤ 8 s
        ağız kadrajda (son çare) → model dudak senkronu, ≤ 5 s, sayı yok, video promptunda tırnak içinde birebir
        model sesi (telsiz | voice-over | ağız kadrajda) → replik video promptuna BİREBİR yazılır, Omni konuşmayı videoda
        üretir (sahip kararı 12.10.2026); ≤ 8 s (ağız kadrajda ≤ 5 s); klip sesi filme girer (timeline klip_sesi), kurgu kaydı yedek
Kayıt: HUMAN | MACHINE · bant: 2 dk 6-12 · 4 dk 12-24 · 8 dk 20-40 · 16 dk 40-70 replik
Konuşma ve ses profilleri (plan referans satırları + "Ses, kamera ve ritim"): Raka kararlı yetişkin kadın sesi, hızlı ama anlaşılır · Thren kontrollü
  tok erkek sesi, hızlı ama anlaşılır · Axi sakin, yorgun, ince erkek sesi · Sael sıcak, androjen · Korv düşük, sert ama anlaşılır · Veli hızlı, kuru
  mizahlı kadın sesi · Kalix sunucu gibi sakin ve tehditkâr erkek sesi (ilk yarıda profesyonel sunucu kadar rahat; C42 ilk gerçek kontrol kaybı) · SYSTEM düz.
  Saniye ve süre Fable tahmini (2,8 kelime/s), F8'de kayıtla kesinleşir. Kayıt: HUMAN varsayılan — ses kaynağını sahip seçer.
50 replik (352 sözcük, plan) — 8 dk bandı 20-40'ın üstünde: plan "Toplam 50 İngilizce konuşma sırası"; plan korundu.
Kaynak: plan yalnız C04 C06 C08 C15 C21'de ekran dışı cevabı yazar; diğer satırlarda plan görüntüsünde yüzü tarif edilen konuşan "ağız kadrajda",
  dış plan/araç/yapı görüntüsündeki konuşan "telsiz" (plan: "Ekran dışı iletişim, ikinci yüzü aynı klipte oynatma ihtiyacını azaltır.").
```

## 6. SES PLANI — model sesi kullanılmaz (istisna: §5 Kaynak = model sesi, yalnız replik)

| Sahne | Katmanlar (≤4) | Kesmede köprü (J/L) | Not |
|:--:|---|---|---|
| S1 (C01) | replik (§5) · Plan: ilk gezegen kaybında kısa bir düşük frekans boşluğu ve küçük bir nefes; büyük patlama sesi Axi'nin cümlesini örtmez | — (F4/F8) | M01 Axi'nin eski dünyası (yörünge) |
| S2 (C02) | replik (§5) · Plan: ilk gezegen kaybında kısa bir düşük frekans boşluğu ve küçük bir nefes; büyük patlama sesi Axi'nin cümlesini örtmez | — (F4/F8) | M01 Axi'nin eski dünyası (yörünge) |
| S3 (C03) | replik (§5) · Plan: şehir ışıklarının sönmesi ↔ hücre kilidinin klik sesi bağlanabilir (C02→C03); hazırlık alanı | — (F4/F8) | M02 hazırlık alanı |
| S4 (C04) | replik (§5) · Plan: şehir ışıklarının sönmesi ↔ hücre kilidinin klik sesi bağlanabilir (C02→C03); hazırlık alanı | — (F4/F8) | M02 hazırlık alanı |
| S5 (C05) | replik (§5) · Plan: şehir ışıklarının sönmesi ↔ hücre kilidinin klik sesi bağlanabilir (C02→C03); hazırlık alanı | — (F4/F8) | M02 hazırlık alanı |
| S6 (C06) | replik (§5) · Plan: şehir ışıklarının sönmesi ↔ hücre kilidinin klik sesi bağlanabilir (C02→C03); hazırlık alanı | — (F4/F8) | M02 hazırlık alanı |
| S7 (C07) | Ortam ve müzik (plan) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S8 (C08) | replik (§5) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S9 (C09) | replik (§5) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S10 (C10) | Ortam ve müzik (plan) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S11 (C11) | replik (§5) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S12 (C12) | Ortam ve müzik (plan) · Plan: köklerde tok geçiş ve motor yankıları | — (F4/F8) | M03 asılı kökler |
| S13 (C13) | Ortam ve müzik (plan) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus |
| S14 (C14) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus |
| S15 (C15) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus |
| S16 (C16) | Ortam ve müzik (plan) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus |
| S17 (C17) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus |
| S18 (C18) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 hasat kapısının altı (bakım güzergâhı) |
| S19 (C19) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 hasat kapısının altı (bakım güzergâhı) |
| S20 (C20) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 hasat kapısının altı (bakım güzergâhı) |
| S21 (C21) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S22 (C22) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S23 (C23) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S24 (C24) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S25 (C25) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S26 (C26) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S27 (C27) | replik (§5) · tribün (plan: kalabalık hissi derinlik, silüet ve ortam sesinden) | — (F4/F8) | M06 gözlemci balkonu |
| S28 (C28) | replik (§5) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S29 (C29) | Ortam ve müzik (plan) · Plan: asılı okyanusta basınçlı su ve boğuk uğultu | — (F4/F8) | M04 gökteki okyanus (Fable türetmesi: planın üç sektörü; metal fırtınası C30'da başlar) |
| S30 (C30) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S31 (C31) | Ortam ve müzik (plan) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S32 (C32) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S33 (C33) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S34 (C34) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S35 (C35) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S36 (C36) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S37 (C37) | Ortam ve müzik (plan) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S38 (C38) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S39 (C39) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S40 (C40) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S41 (C41) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S42 (C42) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S43 (C43) | Ortam ve müzik (plan) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S44 (C44) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S45 (C45) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S46 (C46) | Ortam ve müzik (plan) · tribün (plan: kalabalık hissi derinlik, silüet ve ortam sesinden) | — (F4/F8) | M06 tribün |
| S47 (C47) | replik (§5) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |
| S48 (C48) | Ortam ve müzik (plan) · Plan: metal fırtınasında küçük metal geçişleri ve keskin yakın sürtünmeler | — (F4/F8) | M05 metal fırtınası ve hasat kapısı |

```
Ortam: plan "Uzay dış planlarının sesleri sinemasal ses tasarımıdır; gerçek boşluk akustiği diye sunulmaz." → dış planlarda da sinemasal ses;
       kokpit içi hava taşır. Model sesi kullanılmaz (plan ortak hareket) → klip sesi atılır; replik + efekt + ortam + müzik kurguda.
       Üç sektör ayrı işitsel kimlik: kökler · asılı okyanus · metal fırtınası (plan).
Teslim: −14 LUFS · −1 dBTP · stereo 48 kHz → kurgu.py yukseklik <taslak> [--uygula -o final.mp4]
Kayıt + efekt listesi + ortam yatağı: ODA/F4_ses-tasarimcisi_<n>.md (her çekim en az bir efekt satırı)
```

<!-- 12.10.2026 sahip kararı: klipler arası keskin kesme ve kesmede komple değişen arka ses → uretim_hatti/GECIS_VE_SES_SUREKLILIGI.md.
     Yatak mekân başına TEK dosya, klip sınırlarını aşar (timeline.json yataklar). Geçiş kesme başına: kesme | karisim 0,3-0,8 s | karartma 0,5-1,5 s. -->
### ORTAM YATAĞI — mekân başına kesintisiz, klipleri aşar

<!-- F4 ses-tasarimcisi (ODA/F4_ses-tasarimcisi_1.md) birebir, 20.10.2026 -->
| Yatak | Mekân | Çekimler | Ne (İngilizce üretim/arama cümlesi) | Seviye | Dosya (`ses/`) |
|:--:|---|---|---|:--:|---|
| Y1 | M01 Axi'nin eski dünyası (yörünge) — eski yarış kokpiti ve yörünge | C01-C02 | `deep low continuous drone of a sealed alien cockpit blending into vast empty space, soft air circulation hum, steady, no rhythm, no music, close and dry` | −21 LUFS (replik altında −23; C02 0,0-1,2 s'de −30) | `ses/yatak_eski_yaris.wav` (≥ 45 s) |
| Y2 | M02 hazırlık alanı | C03-C06 | `low steady hum of a large white orbital race dock, soft air handling, faint work-lamp electrical buzz, very distant muffled crowd, no rhythm, no music` | −20 LUFS | `ses/yatak_hazirlik.wav` (≥ 60 s) |
| Y3 | M03 asılı kökler (sektör 1: tok geçiş ve motor yankıları) | C07-C12 | `deep low steady resonance of a vast arena between giant hanging roots, heavy soft engine echoes far away, warm and wide, no rhythm, no music` | −19 LUFS | `ses/yatak_kokler.wav` (≥ 85 s) |
| Y4 | M04 gökteki okyanus (sektör 2: basınçlı su ve boğuk uğultu) | C13-C17 · C21-C26 · C28-C29 (üç aralık, arada Y5/Y6) | `deep pressurized water hum with a muffled low drone, a vast body of water hanging overhead heard through a hull, slow, steady, no rhythm, no music` | −21 LUFS (replik altında −23) | `ses/yatak_okyanus.wav` (≥ 200 s; sonraki aralıklarda dosyanın ilerleyen kısmı okunur, kesintisiz süren yatak hissi) |
| Y5 | M05 metal fırtınası ve hasat kapısı (sektör 3: küçük metal geçişleri ve keskin yakın sürtünmeler) | C18-C20 · C30-C45 · C47-C48 (üç aralık, arada Y4/Y6) | `fine steady shimmer of countless thin iron leaves drifting in a magnetic field, a low metallic hum with sharp thin edges, steady, no rhythm, no music` | −20 LUFS (replik altında −22; C44 sonrası −22) | `ses/yatak_hasat_kapisi.wav` (≥ 250 s) |
| Y6 | M06 uzaylı tribünü ve gözlemci balkonu | C27 · C46 | `large open stadium hall air with a vast quiet crowd of many alien species murmuring softly, rustles and low non-verbal hums, no words, no cheering, no rhythm, no music` | −22 LUFS (C46 0,0-2,5 s'de −26) | `ses/yatak_tribun.wav` (≥ 45 s) |

### GEÇİŞ — kesme başına (F4 taslak · F8 kesin, `timeline.json` gecis)

<!-- F4 ses-tasarimcisi birebir; F8'de kurgucu kesinleştirir -->
| Kesme | Tür | Ses köprüsü | Gerekçe |
|:--:|:--:|---|---|
| C01→C02 | kesme | Y1 kesintisiz; C01 çatlak gerilimi L 0,5 s sönerken Y1 −30'a iner (plan: C02 0,0-1,2 s düşük frekans boşluğu); müzik yok | aynı dünya; kokpit içi yakın → yörünge geniş, felaketin sürmesi |
| C02→C03 | kesme | Y1→Y2 çapraz 1,5 s (Y2 J 1,0 s); C02 ≈9,3 s ışık-sönme tıkı ↔ C03 ≈4,2 s hücre kilidi kliği (KLİK ailesi); tık kuyruğu L 0,8 s | plan: ışıkların sönmesi ile kilit kliği birbirine bağlanır; önceki yarış → sıradaki yarış; siyah ekran yok |
| C03→C04 | kesme | Y2 sürer; eldiven/kilit kuyruğu L 0,5 s | aynı hazırlık alanı; sırt ve eller → Raka kokpit yakın, ölçek farkı |
| C04→C05 | kesme | Y2 sürer; yayın uğultusu ve uzak kalabalık dokusu J 1,0 s | kokpit → Kalix yayın portresi; yayın sesi önden girer |
| C05→C06 | kesme | Y2 sürer; son şerit ışığı tıkı L 0,5 s; kalabalık dokusu L 0,8 s'de kısılır | yayın → Raka kemer; ses yayın odasından kokpit yakınlığına geçer |
| C06→C07 | kesme | Y2→Y3 çapraz 1,0 s; kalkış titreşimi C07 0,0 s ateşleme darbesine J 1,5 s ile yükselir; müzik kesintisiz yükselir | bölüm 1→2, "tam birinci dakikada beş araç fırlıyor"; titreşim → fırlayış hareket üstünde; sert yatak kesmesi yok |
| C07→C08 | kesme | Y3 sürer; motor yankısı L 0,8 s; Fang kokpit uğultusu J 0,5 s | geniş fırlayış → Thren yakın; aynı yön akışı |
| C08→C09 | kesme | Y3 sürer; yan motor drone'u L 0,5 s; boğaz yankısı sıkışması J 1,0 s | yan yana → dar geçit; ölçek değişir |
| C09→C10 | kesme | Y3 sürer; motor perdesi sapması J 0,5 s | Thren çizgiyi kapatır → temas; darbe C10 içindedir (≈4,0 s), kesmeye düşmez |
| C10→C11 | kesme | Y3 sürer; gövde gerilmesi L 1,0 s; kemer gıcırtısı J 0,5 s | geniş hasar → Raka kokpit; neden-sonuç |
| C11→C12 | kesme | Y3 sürer; gerilme gıcırtısı L 1,0 s, C12 kanat sesiyle çözülür | kokpit → dış; tek düzeltme hareketi |
| C12→C13 | karisim 0,6 | Y3→Y4 çapraz 1,5 s (Y4 J 1,5 s: su basıncı uğultusu C12'nin son saniyesinde başlar; Y3 L 1,5 s su altına geçer) | bölüm 2→3, kök sektöründen okyanus altına; bakır-yeşil → koyu turkuaz renk/ışık sıçraması yumuşatılır |
| C13→C14 | kesme | Y4 sürer; dalga kuyruğu L 1,0 s; buhar J 0,8 s | geniş → Thren motoru, aynı sektör |
| C14→C15 | kesme | Y4 sürer; arızalı motor vınlaması L 0,8 s (C15'te yalpalayan Fang sesine bağlanır) | motor arızası → Raka'nın tepkisi; Fang'in sesi kesmeyi köprüler |
| C15→C16 | kesme | Y4 sürer; Fang vınlaması L 0,8 s; Needle motoru yükselişi J 0,8 s | karar → eylem; Needle öne geçer |
| C16→C17 | kesme | Y4 sürer; AKIŞ İZİ L 1,5 s (C17'de Fang'in dengelenmiş motoru altında kalır) | iz içinde dengelenme → Thren yakın |
| C17→C18 | karisim 0,5 | Y4→Y5 çapraz 1,5 s; Axi squelch tıkı J 0,8 s + Y5 metal dokusu J 1,0 s | bölüm 3 sonu; okyanus → kapı altı bakım güzergâhı, mekân ve ışık sıçraması yumuşatılır |
| C18→C19 | kesme | Y5 sürer; römorkör itişi L 1,0 s; BESLEME drone'u J 1,0 s | aynı mekân (kapı altı); römorkör → kontrol yapısı |
| C19→C20 | kesme | Y5 sürer; BESLEME L 1,0 s (kabin içinde kısık) | yapı geniş → Axi kabini; şema |
| C20→C21 | kesme | Y5→Y4 çapraz 1,0 s (ortak taban); Fang vınlaması J 0,8 s | diyalog sürekliliği Axi → Thren; mekân yatağı değişir, taban aynı |
| C21→C22 | kesme | Y4 sürer; vınlama L 0,5 s; hücre perde alçalışı J 0,5 s | Thren → Raka, paralel kokpitler |
| C22→C23 | kesme | Y4 sürer; alçalan hücre tonu L 0,8 s; Halo motoru J 1,0 s | Raka'nın kuru hücresi → Sael'in "Save your last burn" |
| C23→C24 | kesme | Y4 sürer; kanal-açık tıkı J 0,3 s; Halo motoru L 0,5 s | Sael → Raka ortak kanal |
| C24→C25 | kesme | Y4 sürer; taşıyıcı hışırtı L 0,8 s; Sickle vınlaması J 0,8 s | bölüm 4→5; karar → Veli'nin cevabı |
| C25→C26 | kesme | Y4 sürer; yatış süpürmesi L 0,5 s; Bastion homurtusu J 1,0 s | Veli → Korv; ölçek/renk farkı |
| C26→C27 | kesme | Y4→Y6 çapraz 1,0 s; yayın uğultusu J 1,0 s; Bastion homurtusu L 0,8 s | Korv'un kaygısı → Kalix teklifi; diyalog sürüyor |
| C27→C28 | kesme | Y6→Y4 çapraz 1,0 s; Bastion yanal itişi J 1,0 s | emir → seçim; hareket üstünde |
| C28→C29 | kesme | Y4 sürer; dron vınlaması L 0,8 s | seçim → bedel; dronlar sürer |
| C29→C30 | kesme | Y4→Y5 çapraz 1,0 s (ortak taban); dron vınlaması L 1,2 s Y5'e taşar | bedel → dronları çekmek; dron sesi köprü |
| C30→C31 | kesme | Y5 sürer; Sickle/dron geçişi L 0,8 s; AKIŞ İZİ J 1,0 s | bölüm 5→6; iki geniş plan art arda (jump cut riski, F8 dikiş ölçümü): ses köprüsü akış izi |
| C31→C32 | kesme | Y5 sürer; AKIŞ İZİ L 0,8 s cam parıltısına dönüşür | geniş → Raka kokpit yakın |
| C32→C33 | kesme | Y5 sürer; cam parıltısı L 0,5 s; kabin taşıyıcı J 0,5 s | Raka'nın sözü → Axi'nin cevabı |
| C33→C34 | kesme | Y5 sürer; kabin hum L 0,5 s; Sickle geçişi J 0,8 s | Axi'nin cevabı → Veli aksiyonu; ölçek |
| C34→C35 | kesme | Y5 sürer; yaprak gıcırtısı L 1,0 s; Bastion itişi J 1,0 s | Veli kurtuldu → Korv kapıyı tutuyor |
| C35→C36 | kesme | Y5 sürer; Bastion itişi L 1,0 s (kapı baskısı); servis kolu J 0,5 s | Korv tutuyor → Axi çevrimi başlatır; neden-sonuç |
| C36→C37 | kesme | Y5 sürer; çevrim yükselişi ve kapak gıcırtısı L 1,0 s BESLEME drone'una dönüşür; müzik kesintisiz | bölüm 6→7; kapak açıldı → ağız içi |
| C37→C38 | kesme | Y5 sürer; sol amber besleme (sol hoparlör) J 0,8 s | iki yol → Raka'nın sol hattı |
| C38→C39 | kesme | Y5 sürer; Thren squelch tıkı J 0,5 s | Raka'nın çağrısı → Thren'in cevabı (R41 → R42) |
| C39→C40 | kesme | Y5 sürer; Fang öksürüğü L 0,5 s; KANAT sesi C40 ≈1,5 s | Thren yetişemiyor → Raka yavaşlar |
| C40→C41 | kesme | Y5 sürer; eşit perde (tek ton) L 1,0 s hücre perdelerine geçer | eşitlenen hız → simetrik bırakma, hareket üstünde |
| C41→C42 | kesme | Y5 sürer; iki hücre perdeleri kesintisiz süzülür | aynı eylemin sürmesi (bırakma → varış) |
| C42→C43 | kesme | Y5 sürer; BESLEME ≈6,5 s'de kalıcı kesilir (planlı sert kesme); kilit çemberi açılışı J 0,5 s | bölüm 7→8; ışıklar söndü → kilitler açılıyor |
| C43→C44 | kesme | Y5 sürer; son çember kuyruğu L 0,8 s | kilitler açık → çıkış |
| C44→C45 | kesme | Y5 sürer; AKIŞ İZİ L 0,8 s | Sael'in izi → Axi'nin ayrılışı |
| C45→C46 | karisim 0,6 | Y5→Y6 çapraz 1,5 s; römorkör itici sesleri L 1,0 s tribün suskunluğuna erir | mekân sıçraması (römorkör → tribün); ışık/renk yumuşatılır |
| C46→C47 | kesme | Y6→Y5 çapraz 1,0 s; yayın sönme kuyruğu L 1,0 s; kokpit nefesi J 0,5 s | tribün → Raka; yarışın bittiği ses sakinliğiyle |
| C47→C48 | kesme | Y5 sürer; kokpit hum L 1,0 s; altı araç uğultusu J 1,0 s | yakın → geniş altı araç |

## 7. MÜZİK PLANI

<!-- F4 besteci (ODA/F4_besteci_1.md §2) birebir, 20.10.2026 -->
```
OKUMA        İzleyici bu filmi, bir dünyanın kaybıyla başlayıp düşmanları ortak kurtuluşa çeviren, hızı üstte yası altta taşıyan karanlık bir uzay yarışı aksiyonu olarak okumalı (plan Ton: gösterişli yarış aksiyonu, karanlık kural, güçlü ortak kurtuluş).
MÜZİKSİZ     0:00–0:24 (C01 gezegen kaybı + C02 boşluk + C03 hücre kliği; plan: düşük frekans boşluğu, müzik yerine) · 6:50–7:00 (C42 beslemeler söner, Kalix "ilk gerçek kontrol kaybı"; doruk sessizliği, F4 önerisi, soru 3)
VURUŞ/SUSMA  ~0:24 tek alçak nota (C03, Axi cümlesinden sonra) · ~0:55 hafif alçak nabız (C06, kalkış titreşimi) · 1:00 ana tema + sürücü nabız (C06→C07 kesme, "tam birinci dakikada beş araç fırlar") · ~1:35 tek armonik dönüş (C10 sol kanat, vuruş değil) · 1:50–2:00 yavaşlama figürü kurulur (C12 sağ kanat) · 2:00 basınçlı alçak zemin (C13) · 2:30 sıcak sabit akor (C16 akış izi) · 3:50 hedef değişir (C24 "We end the race") · ~4:43 tek koyu vurgu (C29) · 5:00 geniş tema (C31 Sael önde) · 5:10–5:30 çıplak, tek alçak çello notası (C32-C33 duygusal merkez) · 6:00–6:30 iki nabız ayrılır (C37-C39) · 6:30–6:40 hızlı nabız yavaşlayıp ikisi tek nabızda kilitlenir (C40) · 6:40–6:50 zirve (C41) · ~6:50 müzik durur (C41→C42 kesmesi; F8'de gerçek ışık-sönme anından 1-2 s önce) · 7:00 geri dönüş tek notayla (C43 kilitler açılır) · 7:50–8:00 son açıklama, kadanssız · 8:00 çözülmemiş asılı akorda kesme, fade-out yok — faz 8'de gerçek kesme noktalarıyla kesinleşir
FLOW MUSIC   faz 8'de: ODA/F8_besteci_<n>.md
```

### MÜZİK PROMPTU — Flow Music'e yapıştırılır (F4 taslak, 20.10.2026; kesme noktaları yaklaşık, F8'de kesin)
```text
Instrumental cinematic sci-fi space-racing score, one continuous piece, 8:00 total. Dark, glossy, tense, ending open. [Instrumental]
Palette: low bowed strings, one solo low cello, dark analog synth bass pulse, low plucked ostinato, soft brass-like pad. Two pulses: one around 100 BPM, one around 92 BPM.
0:00-0:24 silence, no music at all. At 0:24 one single low note enters (about 100 Hz with its octave above, audible on a phone speaker), thin dark drone, very quiet, sparse until 0:55.
0:55 a gentle low pulse begins. At 1:00 the main theme and driving 100 BPM pulse hit at full power: bold, fast, dark racing energy. From 1:10 a second 92 BPM pulse runs against the first, a rivalry.
About 1:35 one sharp harmonic turn, then by 1:55 a slowing descending figure that settles and holds.
2:00-2:30 deep pressurized low pad, muffled, no high frequencies. 2:30-2:40 warm steady stable chords.
2:40-4:00 quiet restless low ostinato with very sparse midrange so dialogue stays clear; warmer at 3:40; rising resolve by 3:57.
4:00-5:00 cold flat tension, one dark accent near 4:43, then light dry staccato plucks.
5:00-5:10 wide powerful steady theme. 5:10-5:30 almost bare: one sustained low cello note, grief.
5:30-6:00 rising heavy low ostinato, pulse steadies. 6:00-6:30 the two pulses drift apart.
6:30-6:40 the faster pulse slows to 92 BPM and both lock into ONE shared pulse. 6:40-6:50 that single pulse builds to the loudest peak, then stops dead at 6:50.
6:50-7:00 total silence. At 7:00 one single warm note returns, the only full resolution, opening into a soft warm theme until 7:40.
7:40-7:50 thins to almost nothing. 7:50-8:00 last theme statement rising, never cadencing, hard cut at 8:00 on an unresolved suspended chord. No fade-out.
No vocals, no drums, no riser, no whoosh. Nothing below 60 Hz. Dry, no big reverb.
```
