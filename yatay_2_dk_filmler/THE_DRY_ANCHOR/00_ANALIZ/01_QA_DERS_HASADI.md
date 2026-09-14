# 🧾 THE_DRY_ANCHOR — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| D69 | THE STONE SKY 1:40 araçtan iniş · THE STARLESS CIRCLE 2:10 gemiye biniş — iki IDENTITY BREAK, ikisi de KLON, ikisi de aynı sahne tipinde. THE RING LIGHT'ta biniş hareketi planda HİÇ AÇILMADI ve klon çıkmadı (Sayı 10/10). | ⛔ İNİŞ/BİNİŞ HAREKETİ 0 KARE. Astronot ya gemidedir ya zemindedir; rampadan inme hareketi hiçbir klipte kadraja alınmaz. Geçiş SAHNE SINIRINDA atlanır ve boşluk FİZİKSEL işaretle kanıtlanır: açık kapak · sarkan kayış · basamakta duran toz izi. Kamera gemiden inen figürü TAKİP ETMEZ. | S1 → S2 sınırı (gemi → zemin) · S2 · S13 |
| D148 | THE THIRD DUNE kalkışında bacak alevin içinden geçti; şeffaf yazılan alev opak çıktı. | ⛔ İNİŞ KLİBİNDE BACAKLAR HİÇ HAREKET ETMEZ — katlanma/açılma 0 kare. Püskürtü hiçbir karede bir bacakla 2B olarak ÇAKIŞMAZ: alev bacakların ARASINDAN çıkar ve arkası görünür kalır. | S0 · S1 (iniş) · varsa kalkış kodası |
| D145 | Alçak açı ufku kadrajdan attı, model kapanan ufku DUVARLA doldurdu — ovadaki gemi kanyona girdi. | Her dış sahne HORIZON LOCK cümlesi taşır (ufuk çizgisinin kadrajdaki dikey yeri) + EN BÜYÜK ARKA PLAN NESNESİ ADIYLA ve kadraj payıyla yazılır. Dev gemiyi alçak açıdan gösteren sahnede ufuk kadrajın alt üçte birinde SABİT tutulur. | dev gemiyi alçaktan gören her sahne · S0 · S4 · S9 |
| D32 · D138 | Gemi/yapı oranları sahneler arası değişiyor (Cold Burn 65 m gemi lander boyunda okundu). Karşı taraf: ölçü prompt gövdesine inince model onu nesnenin ÜSTÜNE bastı (THE THIN ROOF, halkanın içine `11 metres`). | İKİ AYRI YER, İKİ AYRI DİL: metre YALNIZ QA_SPEC D bloğu ve PLAN fizik defterinde; prompt gövdesinde GÖVDE BOYU (1H = 1,90 m kasklı figür). Gemi için: `the hull's long axis reads about N body-lengths of the figure standing beside it`. ⛔ Prompt gövdesinde tek bir metre/derece/f-sayısı bile yok (kamera MESAFESİ muaf). | 14 sahnenin 14'ü · özellikle gemi görünen her kadraj |
| D147 · D155 | Üç sabit aşınma izi tozlu odada tutmadı: mağarada kir birikti, kabinde SIFIRLANDI. Ve promptun kendi defter etiketi giysiye basıldı (`PHASE 1` göğüste). | TOZ MONOTONİK MERDİVEN: K0 → K1 → K2, geri dönüş 0 kare; her sahne kendi kademesini POZİTİF TARİFLE taşır (hangi yüzeyde, ne kadar alan). ⛔ Faz ADI/ETİKETİ prompt gövdesine GİRMEZ — `PHASE`, `K2`, `EVA` gibi kısaltma yazılmaz. | S2 sonrası her sahne (iniş tozu ilk kademe) · S6 · S10 · S13 |
| D143 | `Sürekli düşüş` toz cümlesi yoğunluk sayısı taşımıyordu; ışık sütunu TOZ ŞELALESİ oldu. | Her toz cümlesi ZERRE YOĞUNLUĞU + DÜŞÜŞ HIZI taşır ve perde/şelale/duvar benzetmesi kullanmaz. İnce atmosfer kilidi: toz YAVAŞ ama KESİN çöker ve yere OTURUR — havada asılı kalmaz. | toz görünen her sahne · S1 · S2 · S7 |
| D127 | `Her saniye +2,16 m/s` 12 promptun 12'sinde yazılıydı; parça sabit ~0,15 m/s süzüldü. İVME PROMPTA YAZILIR, EKRANA GELMEZ. | Düşen/atılan hiçbir cismin İVMESİ yazılmaz; kilit KADRAJI TERK ETME SÜRESİNE yazılır (`leaves the frame in under one second`). g = 3,721 m/s² SPEC'te durur, prompta girmez. | düşen/bırakılan nesne olan her sahne |
| D174 · D104 | `screen-right` modelde bir referans değildir; yön bir KOORDİNATA değil kadrajdaki bir NESNEYE bağlanır. Ve kadrajın en parlak öğesi yön mıknatısıdır — koşucular hedefe değil IŞIĞA koştu. | Her yön cümlesi kadrajdaki bir NESNEYİ adlandırır ve hedefin EKRAN DİLİMİ aynı cümlede yazılır. Alçak güneş bu filmde baskın ışıktır → yönlü hareket içeren her sahnede IŞIĞA GÖRE POZ cümlesi (`her back is to the low sun; the warm band rims her back silhouette`) ve YÖN NEGATİFİ eklenir. | yürüyüş/yönelim içeren her sahne · S3 · S5 · S8 · S11 |
| D146 · D95 | `seamless visor` kubbe davetiyesidir — bir filmde ÜÇ farklı kask çıktı. Ters yönde: renksiz+yansımasız+çerçevesiz vizör ekranda `KASK YOK` okundu. | Vizör GEOMETRİYLE yazılır: kabuk + DÜZ ön cam + GÖRÜNÜR METAL ÇERÇEVE + yaka mührü + tek spekülar çizgi; `seamless`/`domed`/`bubble` yazılmaz. ⚠️ REFERANS PAKETİ YAZILMAYACAK → bu kilit tamamen METİNLE taşınacak ve 14 promptta BİREBİR tekrarlanacak; risk PLAN'a açıkça yazılır [D74]. | 14 sahnenin 14'ü |
| D79 · D139 | Bible'daki OLUMSUZ kostüm kilidi negatif çekirdeğe girmedikçe tutmuyor — sırt ünitesi BEŞ filmde geri geldi; ve düz sırt kilidi yalnız sırt GÖRÜNMEZKEN tutuyor (kamera arkaya geçen tek sahnede sırt çantası doğdu). | Sırt POZİTİF TARİFLE yazılır (`a flat back panel flush with the shoulders, seams and two recessed grooves the only relief`) ve yokluk cümlesi negatif çekirdeğe de girer. Kamera arkaya geçen sahnede pozitif tarif GENİŞLETİLİR. | sırtın göründüğü her sahne · S3 · S8 · S13 |
| D140 | Klon klibin İLK 0,5 saniyesinde doğup kayboluyor (0,30 s) — normal hızda kesme titremesi gibi okunur. | Üretim sonrası her klibin İLK 0,6 SANİYESİ 10 fps şeritle taranır; kapı üretim kapıları listesine KABUL/RET satırıyla yazılır. | teslim listesi · 14 klibin 14'ü |
| D168 | THE SINKING STAKE: 25 sahnenin 14'ü üretildi ve eksik 11'i ARDIŞIK ve filmin SONUYDU. Ayrıca THE UPWARD FALL'da üretim sırası plana YAZILMIŞTI ve yine teslim edilmedi. | ÜRETİM SIRASI: DORUK → merkezî seçim → kapanış imajı → S0 → kalanı. Sıra PLAN'a yazılır VE teslim listesine ayrı satır olarak geçer (liste planı bağlar, teslimi bağlamaz — ikisi ayrı yazılır). | PLAN · teslim listesi |
| D141 · D182 | Klip var, VURUŞ yok: kurgu kapısının üç satırı da geçti ve filmin twist'i ekranda değildi. THE BENT GRASS'ta eksik sahne tam da final vuruş kanıtını taşıyordu. | QA_SPEC B bloğuna FİNAL VURUŞ KANITI: tek karede BULUNAN ya da BULUNMAYAN, SAYILABİLİR ve İNGİLİZCE ADI OLAN bir nesne + saniyesi + kaç tane. | QA_SPEC · S13 |
| D175 · D169 | Mührü D169'un kendi cümlesi deldi: `the forearm tendons stand out through the glove` ÇIPLAK DERİ ürettirdi; çıplak-deri yasağı yalnız yakanın üstünü kapatıyordu. Ve 25 sahnelik fiziksel iş filminde zorlanma sözlüğü TEK sahnede vardı. | Her efor sahnesinde İKİ ZORLANMA KANALI (eldiven/kol yüzeyinde gerilme + gövde duruşu) ve ⛔ zorlanma DERİDE değil MALZEMEDE okunur. Negatif üç bölgeli: yaka üstü · bilek/eldiven · bel/kalça. | fiziksel iş içeren her sahne · S5 · S9 · S12 |
| D157 · D73 | Novum taşıyıcısı TEK KARE testini KENDİSİ geçmiyordu (kapı BAŞKA nesneyle yazılmıştı) ve kural hiç gelmedi. THE WRONG SHADOW'da türetilmiş fenoneme yüklenen novum BİRİNCİL NESNEYE transfer oldu. | TEK KARE cümlesi taşıyıcı NESNENİN ADINI içerir ve taşıyıcı SOMUT bir nesnedir — atmosferik/optik fenomen DEĞİL. Üretimden önce S0'ın imaj promptu TEK BAŞINA koşulur; novum karede okunmuyorsa video üretimine geçilmez. | 02_KONSEPT · S0 · üretim KAPI 1 |
| D48 · D176 | Sahne arası biyom sıçraması; ve kontrast garantisi ZEMİNİ İKİNCİ KEZ tarif edince model ilk yarıda birine ikinci yarıda ötekine sadık kaldı — kalite kapısının kendisi devamlılık kusuru üretti. | BİYOM SABİTİ her promptun İLK çevre cümlesidir ve 14 promptta birebir aynıdır. ⛔ Zemin TEK YERDE tarif edilir; kontrast cümlesi ÖZNEYİ tarif eder, zemine ikinci renk vermez. | 14 sahnenin 14'ü |
| D84 · D153 | Üç çapa kilidi de promptta yazılıydı ve üçü de kırıldı — metin kilidi sahne İÇİNDE tutuyor, sahneler ARASINDA tutmuyor. Eş kadraj çifti aynı metinle aynı seti üretmedi. | Kademe DEĞİŞMEYEN komşu sahneler onaylı imajdan ZİNCİRLE üretilir; kademe DEĞİŞEN sahne master'dan yeni çapa alır. Eş kadraj çifti (S0 ↔ S13) kaynağın ONAYLI KARESİNDEN türetilir ve fark listesi ≤3 madde. | S0 ↔ S13 · toz kademesi değişen sınırlar |
| D70 · D72 · D120 | Yanık başlık kartı ON BİR vakada tekrarladı; kaynağı KAPAK dosyasının başlık katmanı ve kurgunun sonuna ekleniyor. | EKRAN METNİ 0,0 s — kapak çıktısı DAHİL. Kapak AYRI dosyadır ve klip zincirine KARIŞMAZ; kurgu kapısında madde madde sayılır. | teslim listesi · kurgu kapısı |
| D150 · D177 | Üretici filigranı 315/315 saniyede duruyordu ve ALTI merceğin altısı görmedi; suskunluk kapısı SIFIR iddiada ateşlenmiyor. | Teslim listesine KÖŞE TESTİ satırı: master filigransız ihraç edilir ve `olcum_kapisi.sh` ile ÖLÇÜLÜR — mercek raporlarının 0 yazması ölçüm değildir. | teslim listesi |
| D180 · D122 | Planlı MUTLAK SESSİZLİK video modelinden istendi ve İKİ film üst üste doruğunu kaybetti; sessizlik doruktan BEŞ SANİYE SONRA geldi. | Planlı sessizlik KURGUDA HARD MUTE ile kesilir, promptta istenmez. Sessizliğin saniyesi ızgara formülüyle HESAPLATILIR: `t = hook + (n−1) × klip`. | QA_SPEC · MUZIK · kurgu kapısı |
| D124 | Plan 8 saniyeye yazıldı, araç 10 saniye üretti — ÜÇ filmde üç kez; dikey hatta üç teslim 64/64/65 s geldi. | KLİP SÜRESİ araçtan ÖLÇÜLÜR (`ffprobe`) ve PLAN'a o sayı yazılır; 10,0 s varsayılan olarak kabul edilmez, ölçüm satırı plana konur. | PLAN §0 · QA_SPEC |
| D123 · D67 · D167 | 0 kare gore taşıyan film `gore` kelimesini 29 kez yazdı ve iki sahne red aldı. Yedi kimlik özniteliği üst üste `ünlü kişiyi tarif ederek isteme` kalıbı oldu. | ⛔ Yasak yazma, MALZEMEYİ TARİF ET; ve yasak cümlesinin kendisi de yazılmaz. Karakter tanımında tek pencerede EN ÇOK 3 öznitelik; kesin boy → GÖRELİ boy; ten/saç rengi ve yaş PLAN'da kalır. ⛔ MİLLİYET 0 geçiş. | 14 promptun 14'ü · Character Bible |
| D163 · D115 | İnsan şeridi tek figürlü filmde SABİTTİR ve sıra eksenini ölçemez — THE OPEN CIRCUIT'te S2↔S3 takası şeritten geçti. | Bu film TEK ASTRONOTLU → şerit KÖRDÜR. Sıra doğrulaması SAHNE IZGARASI + ölçülen kesme saniyeleriyle yapılır; QA_SPEC'e `İNSAN ŞERİDİ ÖLÇMEZ` şerhi yazılır [D163]. | QA_SPEC · kurgu kapısı |
| D188 | THE BENT GRASS: plan 14 sahne, makara 13 → ON BİR rapor GEÇERSİZ. THE OPEN CIRCUIT: plan 25, makara 23 → ON İKİ rapor GEÇERSİZ. | TESLİM KAPISI: plan SAHNE SAYISI ↔ makara KLİP SAYISI teslimden önce ölçülür; eksik sahne ADIYLA saptanır. 14 sahnenin 14'ü teslim listesinde tek tek işaretlenir. | teslim listesi · kurgu kapısı |
| D129 · D165 | SPEC ve FILME_OZEL paketi HAZIRKEN operatör çıplak rubriği açtı — ON ALTI vaka; THE OPEN CIRCUIT'te on iki merceğin on ikisi mod V koştu. | QA_SPEC ve `rubrik_paketle.sh` çıktısı YAZIMLA BİRLİKTE üretilir ve teslim notunda `MOD D koşulacak` satırı bulunur. Paketin varlığı mod D'yi GARANTİ ETMEZ — bu bir kayıt, kapı değil. | 9. adım · teslim notu |
| D191 · D187 | SPEC'in 12 GÖZ KAPISININ BEŞİ ekranda ihlal edildi ve on iki mercekte 0 bulgu. Ve planın `en ucuz ve en kesin göstergesi` dediği kilit ON İKİ merceğin arasından düştü — hiçbirinin kapsamına girmiyordu. | QA_SPEC F bloğuna göz kapıları ⬜ listesi olarak yazılır VE her taşıyıcı kilidin yanına ONU ÖLÇEN MERCEĞİN ADI yazılır (`→ ÖLÇEN: ② DEVAMLILIK cat.3`). Mercek adı taşımayan kilit ÖLÇÜLMEMİŞ sayılır. | QA_SPEC · 04_UYARI_NOTLARI |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| `THE_BENT_GRASS` | on bir mercek · ①.9 TESLİM KAPISI | Plan 14 sahne, makara 13; eksik olan S12 filmin FİNAL VURUŞ KANITINI taşıyordu ve on bir mercekten yalnız BİRİ (⑦) yazdı. Master verilmedi → ⑪ ölçüm kapısı hiç koşmadı, hakem yok. | 14 sahnenin 14'ü teslim listesinde ADIYLA sayılacak; FİNAL VURUŞ KANITI sahne no + saniye + nesne adıyla SPEC'e yazılacak; master ölçülmeden hiçbir mercek koşulmayacak. |
| `THE_BENT_GRASS` | ⑤ çapraz kapı · D110 | Mercekler İKİ OTURUM hâlinde koştu ve öbekler AYNI defteri paylaştı; iki öbek aynı dosya için iki farklı kart uzunluğu ve iki farklı ses durumu bildirdi. Sıfır replikli filmde iki mercek DÖRT İngilizce cümle transkript etti. | Her mercek TEMİZ OTURUMDA koşulacak; QA_SPEC'e `DIALOGUE LINES: 0 · AUDIO bloğu: ortam yatağı` açıkça yazılacak ki transkript uydurması ölçümle çelişsin. |
| `THE_OPEN_CIRCUIT` | on iki mercek · ölçüm kapısı | Filigran 23/23 klipte · kuyrukta 5 s başlık kartı · −16,6 LUFS / 0,0 dBFS · planlı 2 s HARD MUTE hiç uygulanmamış. Ve iki sahne (S17 · ⭐DORUK S22) makarada yok; on iki mercek de göremedi, ⑫ eksik doruğun yerine geçen sahneye 9/10 verdi. | Teslim listesi dört maddeli: filigransız · kartsız · −14 LUFS / −1,0 dBTP · planlı sessizlik KURGUDA hard mute. Sıra doğrulaması sahne ızgarasıyla yapılacak (şerit tek figürlü filmde kör). |
| `THE_OPEN_CIRCUIT` | ⑥ FİZİK · D192 | 25 sahnenin negatifinde `no lightning bolt` yazıyordu ve doruk boşalması ŞİMŞEK olarak geldi. Filmin 1 numaralı riski TARİF KİLİDİYLE korunmuştu. | Bu filmin 1 numaralı riski (iniş püskürtüsü + toz cephesi) POZİTİF BİÇİMİN SAYISIYLA yazılacak: süre · genişlik · yayılma yönü · artık toz; yalnız negatifle korunmayacak [03_PLAN_ONCESI A5]. |
| `THE_AMBER_LATTICE` | ② DEVAMLILIK · ADAY-16 | Vizör ardında S2'de erkek yüzü, S6'da kadın yüzü — aynı giysi içinde kimlik değişti (Kimlik 2/10). | Karakter bloğu 14 promptta KELİMESİ KELİMESİNE aynı; vizör GÖRÜNÜR ÇERÇEVELİ ve yüz her kafa açısında okunur [D79]; öznitelik sayısı ≤3 [D167]. |
| `THE_AMBER_LATTICE` | ⑥ FİZİK · ADAY-22 | Monolitin taban genişliği L1/L4'te ~25 m iken L7'de astronota göre ~80 m'ye fırladı — ÖLÇEK YENİDEN ÜRETİMİ 8/10. | DEV GEMİNİN kesir merdiveni FORMÜLLE çapalanacak (kesir = nesne yüksekliği × odak ÷ (mesafe × 20,25 mm)); tüm kesirler AYNI nesneyi ve AYNI ekseni ölçecek; her sahnede ÖLÇEK ŞAHİDİ bulunacak. |
| `THE_AMBER_LATTICE` | ⑨ KADRAJ · ADAY-25 | Kapanış karesi açılış kurulumuna dönmedi, yeni bir kurulum kullandı ve DÖNGÜYÜ KIRDI (Kafiye çifti 4/10). | AÇILIŞ-KAPANIŞ ÇİFT KARTI sahne haritasından ÖNCE yazılacak: S0 ↔ S13 aynı kurulum harfi, TEK DEĞİŞKEN, konum kilidi. |
| `THE_AMBER_LATTICE` | ⑫ HOOK · ADAY-28 | İzleyici 00:21'de terk ediyor; sebep S2-S7 arası DURAĞAN konsol sahneleri (tempo düzleşmesi). | 14 sahnede BOŞ VURUŞ 0; her sahne kendi mini krizini taşıyacak; katalizör ≤0:15 [SENARYO_VE_VIRAL §2.2]. |
| `THE_WRONG_SHADOW` | 📖 SENARYO 3,0/10 · D73 | Filmin var olma sebebi ekrana hiç girmedi — iki mercek 64 s'de tek çift gölge görmedi; dönme hareketi gölgeden JALONLARA transfer oldu. `Dead scene` denilen S3-S5 planın en yüklü sahneleriydi. | Novum SOMUT NESNEYE bağlanacak, türetilmiş fenomene değil. TEK KARE FİZİBİLİTE KAPISI: S0 imaj promptu tek başına koşulacak; novum okunmuyorsa video üretimine HİÇ geçilmeyecek. Kapı sonucu tarih + GEÇTİ/BATTI olarak yazılacak [D74]. |
| `THE_THIRD_DUNE` | 🧍 KARAKTER + 🧩 MANTIK · D84 | Üç çapa kilidi de promptta yazılıydı ve üçü de kırıldı: sırt ünitesi (42/42 promptta yasak, yine çıktı) · bant rengi (16× yazılı, kayboldu) · TOZ SEVİYESİ (3 kademeli sayısal takvim, 2:29 kumlu → 2:40 tertemiz). | Toz merdiveni METİNLE DEĞİL ÜRETİM ZİNCİRİYLE taşınacak: kademe değişmeyen komşu sahneler onaylı imajdan zincirle; kademe değişen sahne master'dan yeni çapa. Sırt POZİTİF tarifle yazılacak. |
| `THE_THIRD_DUNE` | 🧩 MANTIK · SPATIAL LOCK | Dört SAYILABİLİR sabit 25/25 sahnede TUTTU (araç sağ üçte bir · yürüyüş sola-sağa · kum sürüklenmesi sola-sağa · fırtına ve güneş solda). Kilidin SÖYLEMEDİĞİ şey bozuldu. | SPATIAL LOCK dört sabitle yazılacak (gemi ekran dilimi · yürüyüş yönü · toz sürüklenme yönü · güneş tarafı) ve KONUM ≠ YÖNELİM ≠ HAREKET üç satırı ayrı ayrı yazılacak. |
| `THE_THIRD_DUNE` | 📖 SENARYO · mod V kesme listesi | İki kesme önerisi de KESİLEMEZ viral ara sahneye giriyordu, biri filmin ORTA NOKTA REVEAL'ini siliyordu; bir replik önerisi cümlenin ikinci yarısını atlamıştı ve filmin ÖNERMESİ oradaydı. | QA_SPEC'e KESİLEMEZ listesi açıkça yazılacak: viral aralar + doruk + kapak karesi + FİNAL VURUŞ sahnesi. |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PB | BEDENDEN BİR ŞEYİN ÇIKARILMASI — kask çıkarma eylemi (COLD BURN S28, İKİ kez reddedildi). | Sahne baştan yazıldı: kasklar EN BAŞTAN rafta, kimse bir şey çıkarmıyor; dramatik vuruş başka bir nesneye taşındı. | ⛔ Bu filmde astronot gemiden inip keşfe çıkıyor — kask/eldiven/kayış ÇIKARMA eylemi HİÇBİR sahnede yazılmayacak; nesne sahneye `zaten çıkmış` olarak girer. |
| PK | MİLLİYET İFADESİ (`Israeli-American` · `Turkish woman`) — DOĞRULANMIŞ red tetikleyicisi; hâlâ üç filmin canlı promptunda duruyor. | Milliyet satırı silindi, yalnız FİZİKSEL TANIM bırakıldı. | Character Bible yalnız fiziksel tanımla yazılacak; `prompt_kontrol ⑯` BLOCK verir → 14 promptta 0 geçiş. |
| PK | YEDİ KİMLİK ÖZNİTELİĞİ ÜST ÜSTE = `gerçek kişiyi tarif ederek isteme` kalıbı (SINKING STAKE, OMNI reddi). D79'un açık vizör kilidi bu kalıbı BÜYÜTÜYOR. | ⬜ Önerilen (henüz sınanmadı): kimlik yığını sökülür, kesin boy → GÖRELİ boy, ten/saç rengi ve yaş PLAN'da kalır; ayırt etme yükü GEOMETRİYE taşınır. | Tek pencerede EN ÇOK 3 kişi özniteliği; yüz tarifi yalnız yüzün KONU olduğu sahnelerde; diğerlerinde vizör `optically clear` der ve durur. |
| PK | TEHLİKE VE HASAR SÖZLÜĞÜ — `wounded ship` · `dangerous` · `damaged hull` (COLD BURN S26). | Sözlük ayıklandı; hasar MALZEME SONUCU olarak tarif edildi (`a hull opened along one seam, the edges cold and torn`). | İniş/toz/arıza sahnelerinde tehlike ALET TEPKİSİNDEN okunur (`the needle sits hard against its stop`), sıfatla değil. |
| YR | YAPISAL RED — insansız sahne + uzun `NEGATIVE:` bloğu; yokluk listesi İSTEK olarak okunamıyor. | `NEGATIVE:` bloğu kaldırıldı, tek POZİTİF `Style:` satırına indirildi → GEÇTİ. | Bu filmde insansız kadraj varsa (gemi tek başına / iz / boş çöl) o sahnenin negatif bloğu KISALTILIR ve boş kadraj VARLIK olarak tarif edilir. |
| PB | YÜZÜ KAPATAN EKİPMAN = ANONİMLİK İMZASI (POLİTİKA §3 imza ⑥) — kask/vizör her filmde var, yani VARSAYILAN durum. | D79 kilidi (`optically clear, zero tint, face fully readable`) bu işi zaten yapıyor — artık yalnız devamlılık değil ÜRETİLEBİLİRLİK kilidi. | 14 promptun 14'ünde D79 cümlesi; vizör kapalı/aynalı yazılmaz. |
| PB | KIRMIZI TON YOĞUNLUĞU + YAKIN PLAN (POLİTİKA §3 imza ⑦) — kadrajın çoğu kızıl/ten dokusu ise gore/NSFW skoru yükseliyor. | Kırmızı KAYNAĞA bağlanır ve çevrelenir; kadrajda gri/mavi referans yüzey bırakılır. | ⛔ TEKDÜZE KIZIL ÇÖL bu filmin varsayılan paletidir → her CU/ECU sahnesine ÇEVRESEL ÇAPA cümlesi + beyaz giysi ve cyan pratik ışık karşıt renk olarak konur [04_ARASTIRMA TUR 14]. |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        26 adet
QA ARIZASI:         12 adet
RED SINIFI:         7 adet
⛔ EN PAHALI ÜÇÜ:
   ① D69 İNİŞ/BİNİŞ HAREKETİ — bu filmin KONUSU bir iniştir ve deponun
      ölçülmüş iki IDENTITY BREAK'inin ikisi de tam bu sahne tipinde çıktı.
      Karar: hareket 0 kare, geçiş sahne SINIRINDA.
   ② D188 TESLİM KAPISI + D141 FİNAL VURUŞ KANITI — son iki partide
      (BENT GRASS · OPEN CIRCUIT) eksik teslim edilen sahne tam da filmin
      vuruşunu taşıyordu ve YİRMİ ÜÇ mercek bunu göremedi.
      Karar: 14 sahne teslimde tek tek sayılır, vuruş kanıtı SPEC'te.
   ③ D32/D138 + ÖLÇEK — DEV GEMİ bu filmin baş varlığı; ölçek kayması
      (AMBER LATTICE 25 m → 80 m) ve metre sızıntısı (THIN ROOF) iki ayrı
      ölçülmüş arıza. Karar: metre SPEC'te, gövde boyu promptta, kesir
      merdiveni FORMÜLLE.
```
