# MOONMOTHER — F2 · senarist · tur 1 · tretman (sahip planı, aday turu yok)

```
BRİF       sahibin planı (yalnız uzaylılar: Khev · Oru · Anne; diyalogsuz) · yatay 16:9 · 4:00 = 24 çekim x 10 s · 3 karakter
KAYNAK     ODA/SAHIP_PLANI.md (BLOK 1 + BLOK 2, sahip onaylı). Olaylar ve sıra planın C01-C24'üdür; S<n> = C<n>.
BU DOSYA   §1 → FILM.md §1 (7 alan, BEDEL satırı "sahne N" taşır) · §2 → FILM.md §2 birebir · §3 yazarın kontrolü ·
           §4 PLANDAN SAPMA ÖNERİSİ (sahibe gider) · §5 REPLİK İHTİYACI. SEÇİM ve SAHİP satırlarını Fable doldurur.
OKUNDU     uretim_hatti/BILINEN_TUZAKLAR.md · ARIZA_LISTESI.md (H ve T) · ILK_30_SANIYE_KILAVUZU.md (tamamı) ·
           UZAY_FIZIGI_GORUNTU_KILAVUZU.md (§1 tam, §2-§8 tarandı) · GPT_IMAGE_OMNI_KILAVUZU.md (§0 §2 tam, §3-§7 tarandı) ·
           GOSTERIM_COZUMLERI.md · GECIS_VE_SES_SUREKLILIGI.md §0-§2 · KAPAK_VE_BASLIK_KILAVUZU.md §7 ·
           REPLIK_VE_KLIP_SESI_KILAVUZU.md §0-§4 · KIMLIK_VE_REFERANS_KILAVUZU.md §0-§3 · SECIM_VE_KURGU_KILAVUZU.md §4-§6 ·
           PROMPT_HATA_ATLASI.md (A01-A05) · KABUL_LISTELERI.md F2 · film_dogrula.py (§1 alan denetimi) ·
           FILM.md · ODA/DURUM.md · biçim örneği: THE_MAYDAY_SEA/FILM.md §2, THE_WRONG_BURN/ODA/F2_senarist_3.md.
           Okunmadı: FLOW_GERCEKLERI · IZLEYICI_VERISI · QA_OKUMA_KILAVUZU · ELESTIRI_PROTOKOLU (hikâye kararına girdi vermiyor).
KARAKTER   Khev (yalnız uzaylı; fildişi kitin, indigo deri, siyah yan gözler; iki kol, iki digitigrad bacak; sol kaval zırhı S14'e dek sağlam) ·
           Oru (35 cm yavru gök mantası; sol yüzgeçte V çentik; sol gözün altında üç amber oval) ·
           Anne (Oru'nun dev erişkini; çukurlu gümüş-gri baş zırhı = "ay"; aynı üç ışık; kâse biçimli sol yüzgeç).
PLAN SADAKATİ  Olay ve sıra değişmedi. Beş yerde planın boşluğunu yorumla doldurdum (§3.7); dört yerde değişiklik öneriyorum
               (§4, hepsi kadraj ya da kurgu düzeyinde).
```

---

## 1. HİKÂYE KARTI — FILM.md §1'e birebir

```
LOGLINE   Yalnız Khev, yaralı yavru Oru'yu ay sanılan dev annesine ulaştırmak için taş sığınağı bırakıp aşağıdaki kayaya atlar; dalga gelirken anne de onu bırakmaz.
AMAÇ      Khev, yaralı Oru'yu taş kemerin sığınağından çıkarıp kıyıdan annesine ulaştırmaya çalışır (taşımak): S9 açık geçide yürür · S13 aşağıdaki çıkıntıya atlar · S15 Oru'yu yeniden kucağına alır · S17 Oru'yu gökyüzüne kaldırıp anneyi çağırır.
ENGEL     Ölçek (S7): anne gelemiyor, çünkü gövdesi yaklaştıkça suyu kıyıya iter; yavru ona gitmek zorunda. Yol (S10): geçidin uç taşı denize düşüyor. Yavru (S11-S12): yaralı sol yüzgeç taşımıyor, Oru alt çıkıntıya iniyor. Beden (S14-S16): atlayışta sol kaval zırhı çatlıyor, dik arka duvar çıkılamıyor. Saat (S7-S22): tek dalga sırtı S7'de doğuyor, S16'da yakın, S22'de çıkıntıya varıyor.
KARAR     Sahne 13: elinin altındaki taş kemer ile aşağıdaki yavru arasında Khev yavruyu seçer; kemere bir kez, Oru'ya bir kez bakar ve kenardan atlar. Yan kararlar: sahne 9 (sığınağı ilk kez bırakıp açık geçide çıkar) · sahne 17 (çağrıyı kendisi için değil, yavruyu görünür kılmak için açar).
SONUÇ     Sahne 20: Oru annenin yüzgecine geçer (istek alındı). Sahne 21: Khev da aynı yüzgece çıkar. Sahne 22: dalga boş çıkıntıyı yutar. Sahne 24: anne ikisini yüzgecinde taşıyarak halkalı gezegenin altında bulutların üstüne yükselir.
BEDEL     Khev'in sol kaval zırhı çatlar ve film sonuna dek iyileşmez; taş kemerin güvenliği ve kendi başına geri dönüş yolu gider · sahne 13 · 14 · 16
TEK SORU  Khev, çatlak zırhlı bacağıyla Oru'yu dalga gelmeden annesine ulaştırıp kendini de o kayadan kurtarabilecek mi?
```

**Ek alanlar (FILM.md'ye taşınmaz; F3-F6'ya girdi)**

```
GERİLİM   Khev, Oru'yu annesine ulaştırmak istiyor, ama aradaki geçit çöküyor ve Oru'nun yaralı yüzgeci taşımıyor, çünkü anne ne kadar
          dikkatli olsa yaklaşması suyu kıyıya iter.
KURAL     ölçek (film içi; FIZIK_IDDIASI yok, yayında gerçek fizik iddiası yapılmaz): çok büyük bir kütle yaklaşınca çevresini iter,
          yani anne ya yaklaşıp kıyıyı yıkar ya uzakta durup bekler (S7). Çözüm yaklaşmak değil, sıfıra yakın hızda alçak temastır:
          yüzgeç, denizle aynı seviyedeki alt çıkıntıya yavaşça oturur (S19). Film bu kuralı konuşmadan gösterir: önce yaklaşmanın
          bedeli (S7, S10), sonra dikkatin ödülü (S19-S21).
BİTİŞ     Yüksekten çok geniş kare: gümüş-gri çukurlu başlı olgun manta alçak mor bulut tepelerinin üstünde; kâse sol yüzgecinde iki küçük,
          ayrı siluet (iki ayaklı Khev, kompakt Oru); siyah kıyı aşağıda küçük; halkalı gaz devi sağ üstte; ufukta ince sıcak şafak kenarı.
DUYGU     ferahlatıcı şükran (korkulan dev koruyucu çıktı) + buruk gurur (Khev'in zırhı çatlak kalıyor; yalnızlığı bitiyor ama bedelini taşıyor)
ÜRETİM    (1) Taşıyıcı an el-nesne değil, kucak teması: Khev'in ön kolları + 35 cm'lik Oru (S1 S2 S4 S8 S9 S15 S17 S19 S23). Renk ayrımı
NOTU      (teal Oru / indigo deri / fildişi kitin) ve Oru'nun her ayrılışta kolun bir karış üstünde başlaması (S11, S20) kaynaşmayı önler.
          S15 ve S21 temaslı: kollar baştan yerleşik, çekim yalnız küçük bir kalkış ya da çekiş taşır.
          (2) Okunacak ekran ve yazı yok. Dil = üç amber ışık. Risk: ışık sayısı (model 2 ya da 4 yapar): her ışıklı karede sayım
          (S1 S2 S5 S6 S12 S17 S18 S20 S23).
          (3) Vakumda toz/duman yok: atmosferli deniz dünyası. Risk sıvı ölçeği: dev ölçekte su küçük ölçek fiziğiyle akar (maket görünümü);
          su yavaş ve geniş, ufuk/uzak adalar/bulut katmanı ölçek ipucu (S3 S7 S22 S24).
          (4) S2'de Khev'in yüzü açılış kare kapısına girer (ILK_30 §6: yüz bozulması, göz asimetrisi). Geçemezse S2 omuz ve baş ¾ arkadan
          kurulur; bilgi (korunan yavru, Oru'nun gökle konuşması) değişmez.
          (5) S20'nin bilgisi "Oru kolda değil, yüzgeçte; Khev'in kolları boş". Süzülüş tutmazsa Oru'nun yüzgeçte yerleştiği yakın kesme
          aynı bilgiyi taşır (planın kendi yedeği); tretman buna izin verir.
          (6) F5'e: plan promptları gövdede büyük harfli etiket (KHEV, ORU, MOTHER_EYE) ve "body" kullanıyor; BILINEN_TUZAKLAR §C ve §A
          ("body" kelime reddi) → "Reference <No> (rol)" ve küçük harfli nesne adı.
```

---

## 2. TRETMAN — FILM.md §2'ye birebir

<!-- Her satır öncekinden doğar; neden-sonuç zinciri §3.1'de. Ses/müzik ayrıntısı F4'ün; plandaki "Sound" satırları buraya taşınmadı. -->

| Sahne | Süre | Ne olur (olay dili) | Ne değişir |
|:--:|:--:|---|---|
| S1 | 0:00–0:10 | Siyah bir kıyıda, arkadan görülen küçücük Khev, kucağındaki yaralı Oru'yu göğsüne bastırmış duruyor. Gökte kraterli bir ay gibi asılı gümüş-gri yüzeyin ince bir aralığında amber bir göz bebeği seçiliyor ve göz kapağı açılmaya başlıyor. Khev'in omuzları kasılıp hareketi kesiliyor, kolları Oru'yu daha sıkı sarıyor. Oru'nun ince, üç notalı çağrısına gökten tek, devasa, alçak bir nefes cevap veriyor. | "Ay" bir ay değil: baştan beri orada olan bir göz açılıyor (H08; tek karede okunur). Ölçek kuruluyor, Khev gözün yanında bir nokta. Khev kaçmıyor, Oru'yu sıkıştırıyor: korku ve koruma aynı karede. Açık soru: gökteki şey ne? |
| S2 | 0:10–0:20 | Orta-yakın planda Khev'in ön kolları Oru'yu güvenli bir beşik gibi sarıyor, siyah gözleri yukarıda. Oru küçük başını gökyüzüne çeviriyor, çentikli sol yüzgeci titriyor, gözünün altındaki üç amber ışık sırayla yanıp sönüyor. Khev önce Oru'ya bakıyor, sonra onun baktığı yöne, göğe; beşiği gevşetmiyor. | Karakterin gövdesi ve yüzü yakında (en geç ikinci çekim). Korunan şey kuruluyor: 35 cm'lik yavru, eski V çentik, üç ışık = Oru'nun dili. Oru gökle konuşuyor, Khev yalnız dinliyor: gökteki şeyle Oru arasında bir bağ şüphesi doğuyor. |
| S3 | 0:20–0:30 | Oru'nun çağrısının ardından ufukta, denizin üstünde aynı açık gözlü baş duruyor; başın arkasındaki bulut yığınından devasa bir yüzgeç yükseliyor ve eğri kenarıyla yıldız alanını dağ silsilesi gibi örtüyor. Aşağıda solda kıyının küçük siyah kalıntıları ölçeği veriyor. Gövdenin geri kalanı bulutun arkasında kalıyor. | İkinci büyük görüntü, 30. saniyeden önce: ay sandığımız şeyin bir uzvu var, yani canlı ve hareketli. Soru "bu ne"den "bu kadar büyük şey buraya neden geliyor, yavruyla ilgisi ne"ye kayıyor. Karakter yok; tehdit hareketiyle yük taşıyor. |
| S4 | 0:30–0:40 | Yüzgeç yıldızları örtmeyi sürdürürken Khev, yüzü ve göğsü denize dönük kalarak yana tek dikkatli adımla taş kemerin korumasına giriyor; ayakları bazalta basıyor, omuzları kalkık. Ön kollarını Oru'nun çevresine kalkan gibi kıvırıyor. Oru'dan küçük, korkmuş bir ıslık çıkıyor; uzaktan dev varlığın uğultusu sürüyor. | Khev'in işi görünür: kaçarken bile gövdesini Oru ile deniz arasına koyuyor (koruma). Taş kemer sığınak olarak kuruluyor; Khev onun içine kendi adımıyla giriyor. Dev varlığı hâlâ tehdit sayıyor. |
| S5 | 0:40–0:50 | Seyrek yüksek bulut şeritlerinin ardında devasa amber gözün yakın planı. Gözün altındaki üç oval ışık önce sönük; sonra Oru'nun çağrısının aynı üç parçalı sırasıyla tek tek yanıyor. Göz bebeği tek ve kasıtlı bir hareketle aşağı, kıyıya doğru iniyor. | Aynı üç ışık, aynı sıra: Oru'nun korku ıslığına dev varlık cevap veriyor. S1'deki "nefes" tehdit değil cevapmış; "canavar" okuması "arayan biri" okumasına dönüyor. Anne–yavru bağı sözsüz kuruluyor. |
| S6 | 0:50–1:00 | Üst terastan çok geniş ve alçak planda sol alt köşede Khev ile Oru'nun küçük siluetleri. Bulut yığını çekiliyor ve yetişkin mantanın bütün gövdesi çıkıyor: hilal alın çıkıntısı, dev göz, iki geniş yüzgeç, ince kuyruk; "ay" sandığımız yuvarlak, çukurlu gümüş-gri baş zırhı. Anne yüzgeçlerini denizin üstünde dikkatle tutuyor, Oru küçük yüzgeçlerini kaldırıp aynısını yapıyor. İki çağrı üst üste biniyor, sonra rüzgâra ve dalgaya boşluk kalıyor. | 60. saniye ödülü: ay anne. Aynı alın, aynı yüzgeçler, aynı üç ışık. Korku keşfe dönüyor. İzleyicinin sorusu değişiyor: Oru ona nasıl ulaşacak? |
| S7 | 1:00–1:10 | Anne yavruya doğru bir parça süzülüyor; dev başı ve sol yüzgeci yine de kalıntılardan bilerek uzakta, denizin üstünde kalıyor. Altındaki karanlık su kıyıya doğru yürüyen tek geniş bir sırt hâlinde kabarıyor; sprey, kıyıda gevşek taşların takırtısı. Anne yüzgecini kıyıdan çekiyor, daha fazla yaklaşmıyor. | Ölçeğin bedeli: anne saldırmıyor ama yaklaşması kıyıyı yıkar. Saat başlıyor: bu sırt film boyunca büyüyecek. Anne gelemiyor; yavru ona gitmek zorunda. |
| S8 | 1:10–1:20 | Taş kemerin altından yüksek, geniş planda Khev Oru'yu göğsüne bastırmış duruyor. Bakışı üst terasın üstünden dar geçidin açık ucuna, oradan dört metre aşağıdaki geniş kuru kaya çıkıntısına ve denize iniyor. Sörf çıkıntının kenarına S7'dekinden yakın vuruyor. Oru küçük bir çağrı yapıyor; Khev hâlâ kemerin altında. | Üç seviye okunuyor: yüksek taş kemer (güvenli), açık geçit (tek yol), alçak çıkıntı (denizle aynı seviye, dik arka duvar). Khev'in işi "saklanmak"tan "ulaştırmak"a dönüyor; tetik Oru'nun çağrısı ve yükselen su. Alçak çıkıntı S19'un zemini olarak şimdiden kuruluyor. |
| S9 | 1:20–1:30 | Oru'nun çağrısının ardından Khev taş kemerin gölgesinden çıkıp üst terasın sol ucundan açık geçide iki ağır adım atıyor; Oru kollarında. Yandan: gövdesi, bakışı ve ayak parmakları sağa, denize dönük; arkada kemer küçülüyor. Her adımda ayak kalkıyor, ilerliyor ve basıyor; sörf sesi yükseliyor. | İlk riskli adım Khev'in kendi seçimi: sığınağı bırakıp denize çıplak çıkıyor. Yön kuruluyor: soldan sağa, kemerden denize (sol bacak sağlam). Yürüyüş iki adımda kesiliyor; sonuç bir sonraki çekimin engelinde. |
| S10 | 1:30–1:40 | Geçidin deniz ucu alçak, yakın planda: enine derin bir çatlak, ötesinde açık deniz. Enine uç taş gıcırdayarak eğiliyor ve denize düşüyor; altında su sıçrıyor. Geriye geçidin sağlam yakın kısmı ve ana teras kalıyor, ötesinde açık bir boşluk. Çekimde yaratık yok. | Annenin yaklaşmasının fiziksel sonucu: geçit kısalıyor, denize giden yol kapanıyor; Khev'in Oru'yu elden annesine götürmesi artık olmaz. Sebep S7'deki sırtın öncü darbesi (§4 SAPMA 1 kabul edilirse darbe kadrajda görünür). Boşluk sonraki geniş planlarda kalıyor. |
| S11 | 1:40–1:50 | Yol kapanınca Khev geçidin sağlam yakın ucunda yüzü denize dönük duruyor, kolları hafifçe dışa açık; Oru kolların bir karış üstünde süzülüyor, iki yüzgeci açık. Oru kollardan ayrılıp annesine doğru, denizin ve alt çıkıntının yönünde kısa bir ileri süzülüş yapıyor; yaralı sol yüzgeci kaldırmasını yitiriyor, süzülüş aşağı kıvrılıyor. Khev açık elleriyle ardından uzanıyor ama terasta kalıyor; elleri boşluğu tutuyor. | Yolun kapanmasından doğan başarısız deneme #1, Oru'dan geliyor: kendi başına annesine uçmaya çalışıyor. S2'de titreyen yaralı yüzgeç şimdi önem kazanıyor. Khev'in elleri bir an geç kalıyor. |
| S12 | 1:50–2:00 | Dört metre aşağıdaki geniş kuru çıkıntıda Oru yatıyor; çentikli sol yüzgeç garip ama sağlam bir açıda. Üç amber ışığı zayıf, karnındaki mavi ışık soluk; yüzgecini bir kez kaldırmaya çalışıp geri yatıyor. Arkasında dik bazalt yüz yükseliyor; denizin spreyi kadrajın kenarına ulaşıyor ama Oru kuru kalıyor. Khev kadraj dışında. | Süzülüşün sonucu: tehlike artık yavruda. Oru kıyının en alçak ve en açık yerinde, dik duvarın dibinde, tek başına. Aşağı atlamanın nedeni görünür. Soluk ışık geri sayım duygusu veriyor. |
| S13 | 2:00–2:10 | Geniş planda Khev üst terasın deniz kenarında çömelmiş, elleri boş; dört metre aşağıda çıkıntıdaki küçük Oru'ya bakıyor. Arkasında solda yüksek taş kemer, uzanma mesafesinde. Bir kez kemere, bir kez Oru'ya bakıyor; kenarda dengesini kuruyor ve çekimin sonuna doğru ayağıyla itip alt kadrajın dışına, çıkıntıya doğru düşüyor. İniş sonraki çekimde. | DORUK. Taş kemerin güvenliği ile aşağıdaki yavru arasında yavruyu seçiyor. Kemer motifi kapanıyor: S4'te içine girdi, S9'da bıraktı, şimdi son kez bakıp arkasını dönüyor. Atlayış görünür, iniş kesmede. |
| S14 | 2:10–2:20 | Sert inişin hemen sonrası, alçak orta-boy planda Khev ağırlığını sağ bacağına vermiş çömelmiş, bir eli kayada. Sol kaval zırhında yeni bir çapraz çatlak, içinden hafif amber ışık. Sol bacağına yük vermeyi bir kez deniyor, acıyla geri çekiliyor; sağ bacağını sabit tutup Oru'ya dönüyor. Arkasında dört metrelik dik bazalt duvar. | BEDEL: çatlak kalıcı, film sonuna dek iyileşmiyor (S23'te hâlâ görünür). Geri çıkamamanın nedeni gösteriliyor: sol bacak yük vermiyor. Ağrı beden dilinde: sarsılma, geri çekilme. |
| S15 | 2:20–2:30 | Khev sağ yanına çökmüş, ön kolları zaten Oru'nun gövdesinin altında. Kendi bacağına bakmadan Oru'yu bütün gövdesinden destekleyip, yaralı yüzgecinden tutmadan taştan kısa bir mesafe kaldırıyor ve eski beşiğe alıyor. Ağırlığını yaralı sol bacaktan uzak tutuyor. Kadrajın alt kenarında çatlak görünüyor. | Öncelik sırası görünür: önce yavru, sonra kendi bacağı. Bedeli ödemiş karakter yine koruyucu. Oru kucakta, ışığı S12'den bir kademe canlı. |
| S16 | 2:30–2:40 | Yandan geniş planda Khev alt çıkıntıda Oru'yu tutarak sağ bacağında bir kez doğrulmayı deniyor, dik arka duvara bakıyor; yaralı sol bacak yük vermeyince geri çöküyor. Duvarın üstünde taş kemer ve geçidin kopuk ucu görünüyor. Sağda çıkıntının ötesinde dalga sırtı artık belirgin biçimde yakın ve yaklaşmayı sürdürüyor; kuru çıkıntı su çizgisinin hemen üstünde. | Başarısız deneme #2: çıkış yok. Geri yol dik duvar, ileri yol dalga. Saat yaklaştı. Kurtuluş yalnız denizin ötesinden gelebilir: annenin dikkatini çekmekten başka yol kalmıyor. |
| S17 | 2:40–2:50 | Orta-alçak planda Khev çıkıntıda diz çökmüş, Oru'yu göğüs hizasında alttan destekleyerek açık göğe doğru hafifçe yükseltiyor; Oru'nun yüzü, hilal alnı ve üç ışığı açık. Oru üç parçalı amber atımını eksiksiz yapıyor ve S12'dekinden net, parlak üç notalı çağrısını sörfün üstüne duyuruyor. Khev kıpırdamadan bekliyor; kısa bir dinleme boşluğu. | Çıkış yok → yardım çağrısı. Khev kendisi için değil, Oru'yu görünür kılmak için çağırıyor: yavruyu yukarı kaldıran o. Zayıf çağrı (S12) tam çağrıya dönüyor. Kurtuluşun tek adresi: Anne. |
| S18 | 2:50–3:00 | Annenin sol gözü yakın planda, ince sprey ve bulut içinden. Göz bebeği önce üst kıyıya, artık boş olan terasa dönük; sonra yavaş ve kasıtlı biçimde aşağı, alt çıkıntıya iniyor ve orada duruyor. Gözün altındaki üç ışık Oru'nun ritmiyle yanıyor; göz kapağı yumuşuyor. | Muhatap: çağrı cevap alıyor, kurtuluş tesadüfen gelmiyor. Anne yavruyu yukarıda arıyordu (S7'den beri terasa bakıyordu); çağrı bakışını aşağı indiriyor. S5'ten farkı: orada cevap genişti, burada cevap konum ve bakış. |
| S19 | 3:00–3:10 | Alt çıkıntı boyunca alçak geniş planda solda Khev diz çökmüş, Oru'yu tutuyor. Sağda annenin devasa, kâse biçimli sol yüzgeç ucu çıkıntı yüksekliğine alçalıp kayanın yanında neredeyse aynı seviyeye oturuyor, araya dar bir boşluk bırakıyor. Yüzgeçteki amber damarlar parlıyor; kimseye değmiyor, altta su yıkıyor. | Dev ölçek ilk kez tehdit yerine destek: S3'te yıldızları örten aynı sol yüzgeç. Neden burası: S8'deki alçak çıkıntı denizle aynı seviyede tek yüzey, yüzgeç kıyıyı yıkmadan oraya oturabiliyor. Köprü kurulu, geçiş henüz yok. |
| S20 | 3:10–3:20 | Yandan orta planda Khev çıkıntıda oturuyor, Oru kollarının bir karış üstünde süzülüyor; annenin yüzgeci sağda kayayla neredeyse aynı seviyede, bir metreden az ötede. Oru kısa ve yumuşak bir süzülüşle kollardan boşluğu aşıp kâse yüzeye konuyor; çağrısı parlak, anne alçak bir uğultuyla karşılıyor. Khev kollarını açık tutuyor, ayağa kalkamıyor. | Birinci iş alındı: Oru annesinde. Khev'in kolları boş; kendi tehlikesi hâlâ açık. Yavru, Khev ve dev yüzgeç üç ayrı beden kalıyor. Yedek: süzülüş üretilemezse yüzgeçte konmuş Oru + boş kollar yakın kesmesi aynı bilgiyi taşır. |
| S21 | 3:20–3:30 | Anne yüzgecini sabit tutuyor. Khev'in ön kolları çekimin başında kâse yüzeye yerleşmiş, sağ bacağı kayada dayalı, yaralı sol bacağı arkada korunuyor; tek kısa çekişle gövdesini taştan canlı yüzeye geçiriyor. Oru birkaç adım ileride dinleniyor. | Khev'in seçimine karşılık: anne onu geride bırakmıyor, yüzgeç tamamen sabit (S7'deki dikkatli duruşun karşılığı). Zemin taştan canlı membrana dönüyor. Birinci iş Oru'nundu, ikincisi Khev'in kendi kurtuluşu. |
| S22 | 3:30–3:40 | Anne yüzgecini kaldırıyor; Khev ve Oru kâse yüzeyin ön planında. Altlarında alt çıkıntı boş; karanlık dalga cephesi kayaya çarpıp çıkıntıyı su ve sprey altında bırakıyor. İkisi yüzgeçte yerlerinde, düşme ve yeni geçiş yok; yükselirken taş kemer sprey arkasında uzakta. | Zamanlama ödeniyor: dalga yalnız ikisi güvenli yüzeye geçtikten sonra boş kayayı yutuyor. S7'de doğan sırtın sonu; S12 ve S16'nın saati kapanıyor. Gerideki tehlike bitiyor. |
| S23 | 3:40–3:50 | Yüzgeçte deniz sisinin üstünde yakın-orta planda Khev yaralı sol bacağı uzatılmış oturuyor; çatlak zırh görünür. Oru başını birkaç santim yaklaştırıp Khev'in ön koluna yaslıyor, üç ışığı sabit yanıyor. Khev'in omuzlarındaki koruma duruşu gevşiyor; yüzgeç damarlarının sıcak ışığı yanağındaki fildişi plakalara vuruyor. | Korkunun yerini güven alıyor: küçük canlı kurtarıcısına yaklaşıyor, ilk çekimdeki kasılı omuz çözülüyor. Yara iyileşmiyor, bedel görünür kalıyor. Oru'nun çağrısı tamamlanmış bir ifadeye dönüyor. |
| S24 | 3:50–4:00 | Yüksekten çok geniş planda anne alçak mor bulut tepelerinin üstüne yükseliyor, sol yüzgecini düz tutuyor; kâse yüzeyde iki küçük, ayrı siluet: iki ayaklı Khev ve kompakt Oru. Siyah kıyı aşağıda küçülüyor; halkalı gaz devi sağ üstte, ufukta ince sıcak şafak kenarı. Kamera yavaşça açılıyor; yeni bir tehdit yok. | SONUÇ: kurtarma tamam. Korkutucu ilk görüntü ("ay") koruyucu bir anneye dönüştü; başlıktaki vaat teslim edildi. Yalnız Khev artık taşınıyor, atmosferin içinde (boş uzay yolculuğu yok). |

---

## 3. KONTROL (yazarın kendi taraması; FILM.md'ye taşınmaz)

### 3.1 Neden-sonuç zinciri (F2.1: her sahne öncekinden doğar)

| Geçiş | Tür | Bağ |
|:--:|---|---|
| S1 → S2 | sonuç | göz açıldı; Khev yavruya, sonra göğe bakar |
| S2 → S3 | cevap | Oru'nun çağrısı gökteki varlığın yüzgecini çıkarır |
| S3 → S4 | seçim | tehdit büyüdü; Khev kemerin altına çekilir |
| S4 → S5 | cevap | korku ıslığına aynı üç ışık yanıt verir |
| S5 → S6 | sonuç | cevap bulutu açar; gövde görünür |
| S6 → S7 | yan etki | anne yavruya doğru süzülür; deniz kabarır |
| S7 → S8 | seçim | anne gelemiyor; Khev yolu gözle ölçer ve işini "saklanmak"tan "ulaştırmak"a çevirir |
| S8 → S9 | seçim | Oru'nun çağrısı ve yükselen su; Khev kemerden çıkar |
| S9 → S10 | engel | açık geçide çıkış; S7'nin sırtı geçidin ucunu düşürür |
| S10 → S11 | başarısız deneme | yol kapandı; Oru kendi başına dener |
| S11 → S12 | sonuç | yaralı yüzgeç taşımadı; Oru alt çıkıntıda |
| S12 → S13 | seçim (doruk) | yavru aşağıda; Khev kemeri bırakıp atlar |
| S13 → S14 | bedel | atlayışın inişi zırhı çatlatır |
| S14 → S15 | öncelik | çatlağa rağmen önce Oru |
| S15 → S16 | başarısız deneme | Oru kucakta; Khev çıkmayı dener, çıkamaz |
| S16 → S17 | seçim | çıkış yok; Oru'yu göğe kaldırır |
| S17 → S18 | cevap | tam çağrı annenin bakışını aşağı indirir |
| S18 → S19 | eylem | bakış yüzgeci çıkıntıya indirir |
| S19 → S20 | hedef 1 | köprü kuruldu; Oru geçer |
| S20 → S21 | hedef 2 | Oru güvende; sıra Khev'de |
| S21 → S22 | bedel ödenir | ikisi yüzgeçte; anne kalkar, dalga boş kayaya |
| S22 → S23 | sonuç | tehlike kapandı; Oru yaklaşır |
| S23 → S24 | kapanış | güven kuruldu; anne yükselir |

### 3.2 Ayna çiftleri (H01: tekrar gibi görünen çiftlerin her birinde tersine dönen şey)

| Çift | İlk | Son | Tersine dönen |
|:--:|---|---|---|
| S1 ↔ S24 | "ay" göz açıyor (korku) | "ay" ikisini taşıyor (güven) | aynı görüntü yeni anlam |
| S2 ↔ S17 | Oru'nun titrek çağrısı, Khev dinler | tam çağrı, Khev Oru'yu yukarı kaldırır | umut → bilerek yapılmış yardım isteği |
| S3 ↔ S19 | sol yüzgeç yıldızları örter | aynı sol yüzgeç çıkıntıya iner | tehdit → destek |
| S4 ↔ S13 | Khev kemerin korumasına girer | Khev kemere bakıp arkasını döner | kaçış → fedakârlık |
| S5 ↔ S18 | genel cevap: ışıklar, bakış kıyıya | konum cevabı: bakış çıkıntıya iner | duymak → görmek |
| S7 ↔ S22 | sırt doğuyor (anne yaklaştı) | sırt boş kayayı yutuyor (anne yükseldi) | tehlike → ödenmiş saat |

Farklılık talimatı: S5 ve S18 ikisi de göz yakın planı. S5'te kıyıya doğru geniş bir bakış ve yüksek bulut şeritleri, S18'de önce boş terasa sonra çıkıntıda duran bakış, sprey ve alt göz kapağı. Üç ışığın parlama sırası aynı kalır (çağrı kodu), kadraj ve bakış yönü değişir.

### 3.3 Saat (dalga sırtı), kemer motifi, çağrı ilerleyişi

- **Saat:** S7 doğuyor, uzak, tek geniş sırt · S8 sörf çıkıntıya yakın · S10 öncü darbe geçidin ucunu düşürür · S12 sprey çıkıntının kenarında, Oru kuru · S16 sırt belirgin yakın, çıkıntı su çizgisinin hemen üstünde · S17 sörf sesi artar · S22 sırt çıkıntıya varır. Plan tek sırt der; ben onu öncü darbeli tek sırt olarak yazdım (yorum kararı 1).
- **Kemer:** S4 girer · S6 ağzında · S8 altında durur · S9 ilk kez bırakır · S13 son kez bakıp bırakır · S16 duvarın üstünde ulaşılamaz · S22 sprey arkasında uzak.
- **Üç ışık / üç nota ilerleyişi:** S1 üç ıslık + dev nefes (belirsiz) · S2 üç ışık sırayla · S4 korkmuş tek ıslık · S5 anne aynı üç parça · S6 çağrılar üst üste · S8 küçük çağrı · S11 umutlu yükseliş → zayıf iniş · S12 kırılgan tek atım · S15 zayıf ıslık, ışık bir kademe canlı · S17 eksiksiz üç parça, parlak · S18 anne üç notalı cevap · S20 Oru daha parlak, anne alçak cevap · S23 tamamlanmış ifade · S24 anne motifi tamamlar.

### 3.4 Arıza taraması

- **H01:** her çekim yeni bilgi: S1 göz · S2 Oru'nun dili · S3 uzuv · S4 koruma · S5 cevap · S6 anne · S7 ölçeğin bedeli · S8 harita ve yeni iş · S9 ilk risk · S10 engel · S11 yavrunun denemesi · S12 tehlike yavruda · S13 doruk · S14 bedel · S15 öncelik · S16 kapan · S17 çağrı · S18 cevap · S19 köprü · S20 hedef 1 · S21 hedef 2 · S22 ödeme · S23 güven · S24 kapanış. Ayna çiftleri §3.2'de.
- **H02:** S24 bir SONUÇ gösteriyor: yavru annesinde, Khev taşınıyor, tehlike kapalı.
- **H03 / H04:** S9 (iki adım), S15 (kaldırma), S21 (çekiş) birer isteğe hizmet ediyor ve sonucu bir sonraki çekimde görünüyor (S10 engel, S17 çağrı, S22 kalkış).
- **H05:** geçidin düşüşünün sebebi S7'de doğan sırt; atlayışın sebebi S12; çıkamamanın sebebi S14; annenin bakışını çeviren S17.
- **H06:** AMAÇ bir iş (taşımak), BEDEL sahne numaralı (13 · 14 · 16).
- **H07:** merkez seçim S13. Öncesi (S8-S12) ona hazırlar; sonrası (S14-S22) sonucunu öder.
- **H08:** S1 ilk karede imkânsız görüntü.
- **H10:** ölçek dizisi: çok geniş · orta-yakın · çok geniş · orta-geniş · yakın (göz) · çok geniş · geniş · geniş-yüksek · orta-geniş yan · yakın insert · orta yan · yakın alçak · geniş · alçak orta · yakın-orta · geniş yan · orta-alçak · yakın (göz) · geniş alçak · orta yan · orta yan · geniş alçak · yakın-orta · çok geniş. Ardışık aynı ölçek-aynı açı çiftleri S6-S7 ve S20-S21 (§4 SAPMA 2 ve 3).
- **H12:** Khev ister (taşımak), kaybeder (kemer, zırh, geri dönüş) ve bunu bedeniyle gösterir: kalkık omuz, iki ağır adım, boşluğu tutan eller, iki bakış ve atlayış, geri çekilme, geri çöküş, kıpırdamadan bekleyiş, açık kollar, tek çekiş, gevşeyen omuz. Oru'nun da isteği var (S11).

### 3.5 İlk 30 saniye ön kontrolü (F3 AÇILIŞ tablosuna girdi)

- **S1:** sorun = "ay" göz açıyor (tek kare). Beden ilk karede: Khev arkadan, küçük, kolları Oru'da. Replik ve yazı yok. Vaadin dünyası ilk karede (siyah kıyı, kraterli gök, indigo gece, amber). Sesi kapalı okunur: göz + Khev'in kasılması.
- **S2:** karakter yüzü ve kolları yakında; sorun büyüyor (Oru gökle konuşuyor). Sesi kapalı okunur: üç ışık sırayla.
- **S3:** cevapsız soru + tehdit hareketi (yüzgeç yıldızları örtüyor); karakter yok, gerekçe: ölçek ve hareket çekimi, saf mekân değil. Kapak anı S3'te değil S1-S2'de (Khev + Oru + açık göz): ILK_30 §3 "tercihen C03" der, ama vaadin gözü S1'de zaten teslim edilmiş; kapak ayrı kompozisyon olabilir, kapaktaki her varlık filmde (KAPAK_VE_BASLIK §7).
- Müzik S1'de girmez. İlk 2 saniyede insan sesi yok (insan ve diyalog yok). Logo, siyah açılış, kart yok (plan da ekstra kart eklemiyor).

### 3.6 Kılavuz kontrolü (sahip: "kılavuzların hepsi")

- **UZAY_FIZIGI §1:** (1) fizik kareden başlıyor: plan "zaten" kalıbını kullanıyor (göz zaten aralık, yüzgeç zaten çıkmış, uç taş zaten ayrılmış, yüzgeç zaten seviyede). (2) olumlu tarif, sayı yok. (3) gösterilemeyen kesmede: S13 atlayış → S14 iniş; S10 insert; S20 yedeği. Vakum yok (atmosferli deniz dünyası); S24 atmosfer içinde kalır.
- **GPT_IMAGE_OMNI §0:** kimlik kayması riski üç özne ile sınırlı (çekim başına en çok üç referans, plan uyumlu); vakumda ses/duman yok; replik yok. §2 pilot: plan C01 · C06 · C20'yi öneriyor, kılavuz açılış filmlerinde C01-C03 diyor → F3p kararı Fable'ın.
- **GECIS §1.5, GOSTERIM ilke 1-2-7, BT §B1/§B10:** §4'teki kadraj önerilerinin dayanağı.
- **Ekran yönü (T11), F3 kontrolü:** deniz film boyunca kadrajın sağında. S22'de plan "sea-facing" der ama kemerin sprey arkasında görünmesini ister; denize bakan kamera arkasındaki kemeri göremez → kıyıya paralel kadraj gerekir. S24'te plan annenin başını sola dönük tarif ediyor; ayrılış yönü (kıyıdan uzaklaşma) okunur olmalı.

### 3.7 Plan yorumları (olay ve sıra aynı; planın boşluğunu doldurdum)

1. **Tek sırt, öncü darbelerle (S7-S22).** Plan S10'daki sarsıntı ile S22'deki dalga arasında iki dakika bırakıyor; bunu öncü darbeli tek yavaş sırt olarak okudum (iki ayrı dalga değil).
2. **Alçak çıkıntı = kurtarma zemini (S8 → S19).** Plan S8'de "aşağıdaki çıkıntı"yı haritaya koyar ve S19'da yüzgeci oraya indirir; aradaki mantığı (yüzgeç yalnız denizle aynı seviyedeki yüzeye kıyıyı yıkmadan oturabilir) S8'in "ne değişir"ine yazdım.
3. **Annenin bakışı S7'den S17'ye üst terasta (S18).** Plan S18'in başlangıç karesinde göz bebeğini üst kıyıya bakar tarif ediyor; bunu "yavruyu yukarıda arıyordu, Oru alt çıkıntıda olduğu için göremedi" olarak okudum. Annenin S11-S16 arasında neden yardım etmediği sorusunun cevabı bu.
4. **Khev S6'da hâlâ kemerin ağzında (S4'te girdi, S8'de altında).** S9'a dek kemeri bırakmıyor; keşif onun davranışını hemen değiştirmiyor, S7'nin bedeli değiştiriyor.
5. **Oru kendi isteğiyle ayrılıyor (S11).** Plan "kucaktan ayrılır" der; Khev'in onu fırlatmadığını, elinin geç kaldığını yazdım (suçluluk okuması önlenir, H12).

---

## 4. PLANDAN SAPMA ÖNERİSİ — sahibe gider

Olay ve sıra bu dört önerinin hiçbirinde değişmiyor; hepsi kadraj ya da kurgu düzeyinde. Sahibin onayı gelene kadar tretman plan metniyle uyumlu yazıldı.

| No | Sahne | Plan metni | Öneri | Neden |
|:--:|:--:|---|---|---|
| 1 | S10 | "Hold the close camera. The one already detached crosswise end slab slowly tilts away, then drops into the sea … Water splashes below the gap." | Taş eğilmeden önce, çekimin ilk 2-3 saniyesinde sırtın öncü dalgası taşın altına vuruyor (su yükselip alt kenarı yalıyor, sprey); sonra taş eğilip düşüyor. Kare aynı, video promptuna tek cümle. | H05 / T14: düşüşün sebebi kadrajda değilse izleyici çöküşü Khev'in adımlarına (S9) ya da sebepsize bağlar. Plan S7'deki sırtla S10'daki düşüşü görsel olarak bağlamıyor; öneri bağı kuruyor. |
| 2 | S7 | "Wide seaward view … adult's colossal head and left fin hover above the ocean at screen right … black arch and upper terrace remain at screen left." | S6'dan en az 30° farklı açı: kıyıya paralel yan görünüş. Anne bir kenarda, sırt ortada, kıyı alt kenarda. | S6 ile S7 aynı mekân ve neredeyse aynı kompozisyon (anne sağda, teras ve kemer solda). GECIS_VE_SES_SUREKLILIGI §1.5: aynı mekân + benzer kadraj kesmesi jump cut gibi okunur; S7'nin yeni bilgisi (sırt) küçük ayrıntıda kalır. |
| 3 | S21 | "Medium side view of Khev at the ledge edge, his upper body leaning over the almost flush living surface …" | S20'den farklı kadraj: omuz üstü ya da arkadan ¾. Khev'in sırtı ve yerleşik ön kolları kameraya yakın, yüzgeç yüzeyi ve Oru karşıda. | S20 ve S21 aynı mekân, aynı özne, aynı ölçek ve yön (GECIS §1.5, H10). Ayrıca geniş beden-yüzey teması riski (BT §B1/§B10): GOSTERIM ilke 7, temas çizgisi bir gövdenin arkasında, kamera boş taraftan ¾. |
| 4 | S3 / S24 | "Film adı gerekirse son görüntünün üzerine yerleştirilir; süreye eklenmez." | Başlık yeri F8'de sahip kararı: ILK_30_SANIYE §2 başlığın S3'ün son 2-3 saniyesinde yazı katmanı olmasını söylüyor. S3 kareleri yıldız alanını yüzgeçle doldurduğu için yazı yeri kare onayında seçilir. İsteğe bağlı, hikâye etkisi yok. Kapak yazısı (plan: "MOONMOTHER") F6'da KAPAK_VE_BASLIK §6 ile yeniden bakılır (ad kapakta yazılmaz; soru ya da durum yazısı). | Plan ile kılavuz farklı yer söylüyor; seçim sahibin. |

---

## 5. REPLİK İHTİYACI

```
REPLİK İHTİYACI  yok · 0 replik
NEDEN            (1) Sahip planı "yalnızca uzaylılar, diyalogsuz"; FILM.md künyesi REPLIK yok. §5 tablosu boş kalır.
                 (2) Hiçbir sahne söze muhtaç değil: amaç (taşımak), engel (sırt, geçit, duvar, dalga), karar (S13 iki bakış + atlayış) ve cevap
                     (üç ışık) görüntüde okunuyor. Sesi kapalı S1-S3 anlaşılıyor (§3.5).
                 (3) Replik bandı 4 dk için 12-24; sıfır gerekçeli (F2.3 "bantta ya da gerekçeli"). Altyazı dosyası gerekmez.
                 (4) Oru ve Annenin üç notalı çağrısı konuşma değil hayvan sesi; kodu ışık taşır, ses pekiştirir. Çağrının tek kaynaktan
                     gelmesi (plan: "iyi kaydı sonraki karşılıklarda aynı kayıt olarak kullanmak") F4'ün kararı. Not: FILM.md künyesi "ses
                     kurguda, model sesi KAPALI" diyor; plan promptlarındaki "Sound:" satırları Omni içindi → F5'te video promptlarına ses tarifi
                     yazılıp yazılmayacağı Fable'ın kararı.
                 (5) Annenin S12-S16 arası "arayan" sesi (çağrıya cevap vermeyen, uzaktan) ses tasarımı önerisi olarak F4'e bırakıldı:
                     S18'deki cevabı hazırlar, annenin yavruyu aradığını sessiz okuyan izleyiciye değil kulağa verir.
```
