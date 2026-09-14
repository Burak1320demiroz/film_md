# 🧾 THE_GREEN_CEILING — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu
> (102 zorunlu dosya · 5 film kaydı · **0 ⬜ · 107 ✅**).
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 195 ders ve
> 56 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.
>
> ⚠️ **SAHNE NUMARALARI BU DOSYADA BAND OLARAK YAZILIR.** Kesin sahne
> ataması `03_SAHNE_SIRALAMASI.md`'nin işidir; buradaki `S0` · `açılış bandı`
> · `kaçış bandı` · `kalkış bandı` · `yanaşma bandı` · `S24` etiketleri
> sıralama yazılınca kesin numaraya çevrilir. Bandların tanımı:
>
> ```
> S0              HOOK (9 s)
> AÇILIŞ BANDI    S1-S5    orman yüzeyi · rutin iş · dünyanın kuralı
> EŞİK            S6       (Hauge %25 · SAVAS §14) fırtına cephesi görünür
> KAÇIŞ BANDI     S7-S12   araca koşu · BÖLÜM 1 sınırı S12'de
> KALKIŞ BANDI    S13-S18  biniş (kadraj dışı) · kalkış · kanopiyi delme
> GERİLEME        S19      (Hauge %75) plan çöker
> YANAŞMA BANDI   S20-S23  yıldızlararası gemiye yanaşma + kenetlenme
> S24             FİNAL + çift kartının ödemesi
> ```

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D69 · D77 · D140** | Klon sıcak noktası biniş/iniş sahnesinde üç kez tuttu (STONE SKY 1:40 araçtan iniş · STARLESS CIRCLE 2:10 gemiye biniş); Sayı-Ayrışma her ikisinde 1/10. D77: ders yazıldıktan bir gün sonra yasakladığı sahne plana eklendi | ⛔ **BİNİŞ VE İNİŞ HAREKETİ KADRAJA ALINMAZ.** Karakterler bir kabine girerken/çıkarken gösterilmez; sahne ya kapının dışında biter ya kabinin içinde başlar. Kadraj dışı geçiş PLANA gerekçesiyle yazılır. Her klibin ilk 0,6 saniyesi 10 fps şeritle taranır [D140] | KAÇIŞ BANDI sonu (araca biniş) · YANAŞMA BANDI sonu (gemiye geçiş) — bu filmin İKİ sıcak noktası |
| **D20 · D86 · D134** | İKİ figürlü kadrajda "kim solda" kilidi yok; ekran yönü kilidi DİZİLİMİ kapsamıyor. ROSE COAT'ta iki figürü ayıran bot rengi "kostüm sürüklenmesi" diye YANLIŞ ETİKETLENDİ | **DİZİLİM KİLİDİ**: komutan her kadrajda screen-LEFT, mühendis screen-RIGHT; ters açı gerekiyorsa dizilim PLANA yazılarak bir kez ve tek sahnede terslenir. İki figürü ayıran ÜÇ KANAL plana ADIYLA yazılır ki mercek onları kusur sanmasın | iki figürün birlikte olduğu HER sahne (≈%80) |
| **D79 · D95 · D146** | Bible'ın OLUMSUZ kostüm kilidi negatif çekirdeğe girmedikçe tutmuyor: sırt ünitesi ve aynalı vizör iki filmde üst üste geri geldi. "seamless visor" KUBBE DAVETİYESİ — bir filmde üç kask. Ters yönde: vizör tamamen görünmez olunca iki mercek "kask çıkarılmış" okudu | Vizör GEOMETRİYLE yazılır: **kabuk + ön cam + GÖRÜNÜR ÇERÇEVE/CONTA**; `optically clear, zero tint, no mirror coating, face fully readable at every head angle` cümlesi 25/25 promptun NEGATİF ÇEKİRDEĞİNDE durur. ⛔ `seamless` kelimesi hiçbir promptta geçmez | 25/25 sahne |
| **D139 · D175** | Düz sırt kilidi yalnız sırt görünmezken tuttu; kamera arkaya geçen tek sahnede sırt çantası DOĞDU (5/6). "through the glove" cümlesi modele DERİYİ çizdirdi | Yokluk kilidi GÖRÜNEN YÜZEYDE POZİTİF tarife çevrilir: "flat back with a single vertical spine seam" (yokluk değil BİÇİM). Çıplak-deri negatifi ÜÇ BÖLGELİ yazılır (yaka üstü · bilek · bel) | kameranın arkaya geçtiği her sahne · eldivenli her temas |
| **D167** | SINKING STAKE: tek kişide YEDİ kimlik özniteliği (kesin boy·gövde·ten·saç rengi·saç biçimi·yüz işareti·yaş), İKİ kişide ve 25/25 promptta → OMNI "can't depict some public figures" reddi | ⛔ **TEK PENCEREDE EN ÇOK 3 KİŞİ ÖZNİTELİĞİ.** Kesin boy → GÖRELİ boy; ten rengi, saç rengi ve yaş prompt gövdesinden ÇIKAR, PLAN'da kalır. Ayırt etme yükü GEOMETRİDEDİR (rol şeridi kolu · sırt silueti · göğüs paketi) | 25/25 imaj promptu |
| **D45 · D138 · D155** | Prompt iskeleti ekrana sızdı (THE INVERSION 2:12: lens grafiği + isim etiketi); metin yasağı kostüme yazıldı, model ÖLÇÜYÜ ZEMİNE bastı ("11 metres" + gradasyon çentikleri); promptun kendi defter etiketi giysiye basıldı ("PHASE 1" göğüste) | ⛔ Karakterin ADI prompt gövdesine YAZILMAZ · `CAMERA: 75mm, f/5.6` dizilimi riskli sahnelerde CÜMLEYE çevrilir · nesne ÖLÇÜSÜ gövdeye girmez (yalnız kamera MESAFESİ) · FAZ SATIRI ve kısaltma prompttan çıkar · negatife ikinci savunma: `HUD overlay, lens data, name label, subtitle, lower third` | 50/50 prompt (25 imaj + 25 video) |
| **D124 · D122** | Plan 8 saniyeye yazıldı, araç 10 saniye üretti — üç filmde üç kez; dikey hatta üç teslim 63-65 s geldi. UPWARD FALL'da 9 s hook planlandı, 10 s teslim edildi | Izgara ARAÇTAN: **9 s hook + 24 × 10 s = 249 s = 4:09**. Replik ve doruk saatleri HESAPLANMAZ, HESAPLATILIR: `başlangıç(S_n) = 9 + (n−1) × 10`. Kurguda hook 9 s'ye KIRPILIR (COUNTED TURN'de kırpılmadı ve ⑫ gördü) | PLAN · QA_SPEC · kurgu kapısı |
| **D157 · D172 · D73** | Novumun TAŞIYICISI tek kare testini kendisi geçmiyordu; taşıyıcıyı asan kordon novumun yerine geçti; türetilmiş optik fenomene yüklenen novum 64 saniyede 0 kare çıktı | TEK KARE cümlesi taşıyıcı nesnenin ADINI içerir ve testi O NESNEYLE koşulur. Taşıyıcı: fiziksel, tek, sayılabilir, kadrajın ortasında; askı/kordon/duman gibi yardımcı düzenek taşıyıcı OLAMAZ | 02_KONSEPT novum kapısı · taşıyıcının geçtiği ≥3 sahne |
| **D192 · D193** | Filmin 1 numaralı riski TARİF kilidiyle korundu: "no lightning bolt" 25 sahnenin negatifinde yazılıydı ve doruk ŞİMŞEK geldi — pozitif biçimin SAYISI yoktu. Işık takvimi yazıldı ama ölçülmedi; sönen şeritler aynı klipte geri yandı | ⛔ **ŞİMŞEK POZİTİF BİÇİMLE VE SAYIYLA YAZILIR**: süre · genişlik · DAL SAYISI · artık ışık süresi (plan öncesi liste A5). Işık takvimi `olcum_kapisi.sh` IŞIK TAKVİMİ İZİYLE ölçülür (↑ geri sardı · ⟳ klip içinde geri yandı) | fırtına bandının HER sahnesi · A5 satırı |
| **D104 · D174** | En parlak ışık YÖN MIKNATISIDIR: hedef-dilim + yön yetmedi, gövde yönelimi yazılmayınca koşucu IŞIĞA döndü. "screen-right" modelde bir referans DEĞİLDİR — yön bir koordinata değil KADRAJDAKİ BİR NESNEYE bağlanır | Koşu sahnelerinde gövde YÖNELİMİ ayrı cümleyle yazılır ve yön hedef NESNEYE bağlanır ("toward the lander's lit hatch, which stays in the right third"). Şimşek en parlak kaynak olduğu için koşu yönüyle ÇAKIŞTIRILMAZ | KAÇIŞ BANDI'nın tamamı |
| **D148** | Kalkış klibinde "bacaklar katlanır" yazıldı; bacak alevin İÇİNDEN geçti, "şeffaf" alev opak çıktı | ⛔ Kalkışta **BACAK HİÇ HAREKET ETMEZ**; alev bacakların ARASINDA ve arkası GÖRÜNÜR. İniş takımı katlanması kadraja alınmaz | KALKIŞ BANDI |
| **D36 · D10 · D30 · D39** | Vakumda atmosferik duman kıvrıldı; partiküller donmuş/süzülen çıktı; toz sıvı gibi aktı — ortama göre TERS davranıyor | Egzoz ve partikül davranışı ORTAM KARTINDAN yazılır ve iki perde AYRI: **yüzey (§3.4 kalın atm.) = kısa ve KALIN egzoz, toz çok hızlı çöker ve KÜMELENİR, dolgu ışığı çok güçlü** · **yörünge (§3.1 vakum) = DÜZ KONİ, süzülme yok, mutlak siyah gölge, dolgu YOK**. Yağmur damlası sayısı ve hızı POZİTİF yazılır [D143 kalıbı] | yüzey sahneleri ↔ yörünge sahneleri sınırı |
| **D143** | "Sürekli düşüş" toz cümlesi YOĞUNLUK SAYISI taşımıyordu; ışık sütunu toz şelalesi oldu | Yağmur/damla/yaprak cümlesi **zerre sayısı + hız** taşır ("a thin curtain of large slow drops, roughly forty visible at once, each falling about two metres per second") | orman sahnelerinin tamamı |
| **D169** | 25 sahnelik fiziksel iş filminde zorlanma sözlüğü TEK SAHNEDE vardı; düşük yerçekimi AĞIRLIĞI azaltır, ATALETİ azaltmaz | ⛔ Zorlanma sözlüğü 25 sahneye DAĞITILIR ve `05_SAHNE_CALISMALARI`'nda sahne başına bir COST hanesi yazılır. 0,42 g'de kütle ve atalet Dünya'daki gibi davranır | koşu · tırmanma · kapı · kemer sahneleri |
| **D147 · D42 · D84** | Üç sabit aşınma izi tozlu odada tutmadı: mağarada kir birikti, kabinde SIFIRLANDI. Üç çapa da 42/42 promptta yazılıydı, üçü de kırıldı | **ISLAKLIK/ÇAMUR MONOTONİK SAYAÇTIR**: K0 kuru → K1 nemli → K2 sırılsıklam+çamurlu; ⛔ kabinde SIFIRLANMAZ, geri dönmez. Faz satırı her prompta yazılır, faz ADI yazılmaz [D155] | S0'dan S24'e kadar her sahne |
| **D89** | Sahnenin eylemi bir ÇIKARMA ise model EN YAKIN ÇIKARILABİLİRİ çıkarır (tek mühür sayımı) | ⛔ Bu filmde hiçbir sahnenin eylemi "çıkarmak" DEĞİLDİR: kask, eldiven, kemer takma/çıkarma kadraja alınmaz; nesneler sahneye ZATEN TAKILI girer [POLITIKA §3 imza ②] | 25/25 sahne |
| **D1 · D68** | Tek çekim kuralı 8/8 filmde tetiklendi; kesme promptun İÇİNDE tutmadı — planlı kesme çıkmadı, plansız kesme sızdı | Bu film SABİT IZGARALI: sahne = çekim = klip, `no cuts` cümlesi 25/25 video promptunda AYNEN durur. ⛔ `cut to`, `then we see`, `montage` yasak. Kesme klip ARALARINDA yaşar | 25/25 video promptu |
| **D70 · D72 · D61a · D34** | Üretim kilitleri kurguyu bağlamıyor: jenerik/başlık kartı ALTI vakada geri geldi; son sahne jenerik kartına harcandı | ⛔ **EKRAN METNİ 0,0 s** — jenerik, başlık kartı ve KAPAK ÇIKTISI dâhil. Promptlardan `title card`, `cinematic titles`, `ending text`, `end credits` ifadeleri TEMİZLENİR (COUNTED TURN'ün reçetesi) | 50/50 prompt · kurgu kapısı madde ③ |
| **D83** | Ortam yatağı klip sınırında öldü — COLD BURN'de 20 saniyelik MUTLAK DİJİTAL SESSİZLİK | Kurguya TEK PARÇA ortam yatağı serilir; "müziksiz sahne" SESSİZ sahne değildir. Planlı tek sessizlik anı doruğun HEMEN ÖNCESİNDEDİR ve orada bile nefes + giysi fanı sürer | kurgu · MUZIK dosyası |
| **D180** | Planlı MUTLAK SESSİZLİK video modelinden istendi; iki film üst üste doruğunu kaybetti (sessizlik doruktan BEŞ SANİYE SONRA geldi) | ⛔ Sessizlik VİDEO MODELİNDEN İSTENMEZ; **kurguda hard mute** ile yapılır ve SPEC'in E bloğuna komut olarak yazılır | doruk sahnesi · QA_SPEC E |
| **D82 · D113** | Ses mimarisi üretimde TERSİNE döndü: gövdesiz AI silindi, telsiz replikleri ekrandaki AĞIZLARA devredildi. Repliksiz film bir KISITTIR, eksik değil | Replik varsa **REGISTER HARİTASI** plana yazılır (hangi replik HUMAN, hangisi MACHINE, hangisi gövdesiz) ve ⛔ ağız kadraj dışında tutulur. İki figür AYNI ANDA konuşmaz — sıra alma prompta yazılır (lip-sync başarısı %40'ın altına düşüyor) | replikli her sahne · MUZIK/SES kararı |
| **D50 · D78 · D134** | Sayaç ekranda okunmadı: 13 filmin 11'inde N/A, DÖRT filmde sayaç PLANLIYDI ve görünmedi. Tek çalışan vaka THIRD DUNE 10/10 — fırtına cephesi UFKU KAPLAYAN BİR DUVARDI, ölçeğin iki ucu her karede birlikte görünüyordu | ⭐ **FIRTINA SAYACI THIRD DUNE REÇETESİYLE KURULUR**: cephe her sahnede ufku daha çok kaplar, monotonik, ve ölçeğin İKİ UCU (kanopi tavanı + cephe) aynı karede durur. Sayaç sayısı ≤2 tutulur; her sayaç SPEC C'ye yazılır | açılış bandından doruğa kadar her dış sahne |
| **D145 · D126 · D176** | Alçak açı ufku kadrajdan attı, model boşluğu DUVARLA doldurdu. ⑤ envanteri altı sahnede "black space, star field" yazarken kadrajda GEZEGEN vardı. Kontrast garantisi zemini İKİNCİ KEZ tarif etti ve film ortasında biyom değişti | Her dış prompt **EN BÜYÜK ARKA PLAN NESNESİNİ ADLANDIRIR** + ufuk kilidi taşır; ormanda ufuk kapalıdır, kilit "KANOPİ TAVANI" olarak yazılır. ⛔ ZEMİN TEK CÜMLEDE, TEK RENKTE tanımlanır ve o cümle 25/25 promptta birebir aynıdır | 25/25 imaj promptu |
| **D179** | İmaj promptu değişimin SONRASINI yazdı; I2V'de imaj t=0'dır ve model söndüremediği tüyü başka yere koyup onu söndürdü — filmin bedeli hiç ekrana gelmedi | Değişim içeren sahnenin başlangıç karesi değişimin ÖNCESİDİR. **Bedel sahnesi EN GENİŞ kuruluma yazılmaz** — taşıyıcı nesne kısa kenarın ≥1/8'i olur | bedel sahnesi · değişim taşıyan her sahne |
| **D127** | İvme prompta yazıldı, ekrana gelmedi: "her saniye +2,16 m/s" 12 promptun 12'sindeydi, parça sabit ~0,15 m/s süzüldü | ⛔ Kilit İVMEYE değil **KADRAJI TERK ETME SÜRESİNE** yazılır ("the dropped tool leaves the bottom of the frame within one and a half seconds") | düşen/atılan her nesne |
| **D158** | Bedel ödendikten sonra 13 sahne 0 seçim · 0 başarısız deneme; plan bunu TEMAYLA gerekçelendirmişti — "tema edilgenliğin saklandığı yerdir" | Plan kontrolüne **B2a (seçim sonrası seçim) ve B2b (başarısız deneme) SAYIMI** yazılır: bedelden sonra en az bir seçim ve en az bir BAŞARISIZ deneme kadraja girer | GERİLEME · YANAŞMA BANDI |
| **D168** | Üretim sırası dramatik sırayla aynıysa yarıda kalan film kendini savunamaz — SINKING STAKE 25 sahnenin 14'ünü üretti, eksik 11'i ARDIŞIK ve filmin SONUYDU | ⭐ ÜRETİM SIRASI: **DORUK → merkezî seçim → kapanış imajı → S0 → kalanı**. Referans paketi yazılmadığı için ilk halka DORUK'tur | PLAN ÜRETİM SIRASI bloğu |
| **D141 · D156** | Klip var, vuruş yok: kurgu kapısının üç satırı da geçti ve filmin TWIST'i ile döngüsü ekranda yoktu. "Sıfır" denen beş şeyin beşi de düştü — SIFIRI KİMSE ARAMIYOR | SPEC B'ye **FİNAL VURUŞ KANITI** (tek karede bulunan/bulunmayan, sayılabilir, adı konabilir nesne + saniyesi + adedi) ve **SIFIR KİLİTLERİ BLOĞU** (replik · metin · klon · sayı · sessizlik) yazılır; her sıfır kilidinin yanına ölçüm KOMUTU konur | QA_SPEC B · ⑪ ölçüm kapısı |
| **D187** | Planın "en ucuz ve en kesin göstergesi" dediği kilit on iki merceğin arasından DÜŞTÜ — hiçbirinin kapsamına girmiyordu (ağırlığın üç kanıtı: 0/3) | ⛔ Her taşıyıcı kilidin yanına **ÖLÇEN MERCEĞİN ADI** yazılır (`→ ÖLÇEN: ② DEVAMLILIK cat.3`); mercek adı taşımayan kilit ÖLÇÜLMEMİŞ sayılır | PLAN sayısal kilitler bloğu |
| **D123 · D59 · D67** | Yasak, yasakladığı kavramı prompta SOKAR: 0 gore taşıyan film "gore" kelimesini 29 kez yazdı ve iki sahne red aldı. Yasak değil İSİM kazanıyor; istenen görüntünün KENDİSİ tetikleyici olabiliyor | Sahneye-özel yasak listesi NEGATIVE'e yazılmaz; malzeme POZİTİF tarif edilir. Tehlike ALETTEN okunur ("the needle sits hard against its stop"), kuvvet NESNEYE taşınır | fırtına · kalkış · acil durum sahneleri |
| **D165 · D129 · D117** | Araç yazıldı, koşacak kart yoktu: paket üretilmedi ve sekiz mercek mod V koştu. SPEC planın içinde gömülü kaldıkça mod D hiç koşulmuyor — **SPEC BÖLÜM DEĞİL DOSYADIR** | `<FILM>_QA_SPEC.md` AYRI DOSYA olarak yazılır ve SPEC yazılır yazılmaz `rubrik_paketle.sh` koşulur (PAKET_1..12). Paket klasörü yoksa film "yazımı tamam" DEĞİLDİR | 9. adım |
| **D74** | Kayıtsız kapı, koşulmamış kapıdır — "üretim S4'ten başlar, bozuksa film üretilmez" yazılıydı ve novumsuz teslim iki QA merceğine kadar geldi | Atlanan her kapı PLANA TEK SATIR gerekçeyle yazılır. **Bu filmde referans paketi YAZILMIYOR** → PLAN'a tek satır gerekçe (tetikleyici 6'nın 5'i doğru, maliyet üstlenildi) | PLAN §REFERANS PAKETİ satırı |
| **D186 · D131** | "Kusur bulamadım" hücresine 7/10 yazıldı; kaynaksızlık ÖDÜLLENDİRİLİYORDU (çöken film 4,3'ten 7,2'ye çıktı) | Bu filmin QA koşusunda `rapor_kontrol.py` ZORUNLU; kaynaksız hücre `—`'ye çekilir ve düzeltilmiş ortalama yazılır | 10. adım · QA koşusu |
| **D150** | Üretici filigranı 315/315 saniyede duruyordu, altı mercek görmedi (⑤ "EDGES: CLEAN" ×31) | Teslimde **köşe testi** koşulur; filigran bir RAPOR bulgusu değil TESLİM KUSURUDUR | ihraç listesi |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_COUNTED_TURN | ① KARE + ⑦ AKSİYON | 🔴 ×7 **EL-NESNE PENETRASYONU**: 0:27 parmaklar kayışla eriyor · 0:35 başparmak karabinerin içinden geçiyor · 1:26 kayış eldiven ayasının içinden · 1:44 kayış pinin içinden · 2:44 karabiner rayın içinden · 3:05 kayış eldivene gömülüyor · 3:25 parmaklar karabinerle kaynaşıyor. ⑦ Temas okunabilirliği **4/10** | Negatif çekirdeğe İKİ CÜMLE eklenir: `Solid objects maintain strict collision boundaries; hands push against surfaces without penetrating them.` + `Fabric straps rest on top of gloves and metal pins, obeying physical collision.` ⭐ Ayrıca **kayış/kordon sayısı MİNİMUMA indirilir** — ASTRONOT_DONANIM §7 zaten serbest uçlu hortumu YÜKSEK riskli sayıyor |
| THE_COUNTED_TURN | ② DEVAMLILIK **3,0 · IDENTITY BREAK** | S12 (1:50) sakallı erkek → pürüzsüz KADIN yüzü · S13 (2:00) beyaz uzay giysisi → KOYU DERİ CEKET · S14 (2:10) kadın yüzü devam, turuncu klipsler KAYIP · S19 (3:00) erkek geri dönüyor. Kimlik 1 · Kostüm 1 | ⛔ **Tek karakterli filmde kimlik kırıldı; bizde İKİ karakter var.** Character Bible KELİMESİ KELİMESİNE kopyalanır; iki figür DÖRT eksende ayrışır (rol şeridi rengi+KOLU · sırt silueti · göğüs paketi · bilek düzeni); MCU'larda da rol şeridi kadrajda kalacak şekilde kadraj seçilir |
| THE_COUNTED_TURN | ⑧ EFOR **0.0 · NOBODY PAYS** | 6 iş olayının altısında da bedende karşılık YOK: zorlanma 0 · nefes 0 · yorgunluk 0 · kavrama 0 | `05_SAHNE_CALISMALARI`'nda sahne başına **COST hanesi (0-9)** yazılır; her düşüş RESET LOG'da gerekçelenir. GÖRÜNÜR NEFES (omuz ve göğüs kafesinin periyodik yükselişi) kaçış ve tırmanma bandında zorunlu satır |
| THE_COUNTED_TURN | ⑩ OYUNCULUK **3,4 · THE CHOICE IS INVISIBLE** | Dokuz hücrenin sekizi 3.0; merkezî seçim bedende OKUNMUYOR | Film repliksiz/az replikli gidiyorsa merkezî seçim **EL · DURUŞ · BAKIŞ YÖNÜ · TEMPO** dördünden okunmak zorunda. PLAN'a "CENTRAL CHOICE bedende nasıl okunur" satırı + `THE CHOICE ON THE BODY` üç önce/sonra kaydı |
| THE_COUNTED_TURN | ⑪ IŞIK **6,8 · KEY WALKS** | S12 (1:50) ve S14 (2:10) MCU'larda ana ışık yönü saat **3'ten 9'a** yürüdü | Sahne başına **ANAHTAR IŞIK SAATİ** plana yazılır (UZAMSAL §4.2 kadranı) ve ⑪'in KEY DIRECTION STRING'i o listeden okunur. Şimşek tek baskın kaynak olduğu için yönü her fırtına sahnesinde AYNI yazılır |
| THE_COUNTED_TURN | ⑫ HOOK | **S1 hook KIRPILMAMIŞ — 10 s teslim edildi, bütçe 9 s'ydi**; kuyrukta 4:10-4:15 başlık kartı | Kurgu kapısına iki satır: hook tam **9,0 s**'ye kırpıldı mı · ekran metni 0,0 s mi (kart dâhil) |
| THE_UPWARD_FALL | ⑪ ÖLÇÜM KAPISI | **Planın 25 sahnesinden 22'si teslim edildi; eksik üçün biri S24 = DORUK + TWIST + KAPAK KARESİ.** Süre −29 s ≈ 3 klip. Film bitmedi, DURDU | ⭐ ÜRETİM SIRASI DORUKTAN BAŞLAR [D168]; kurgu kapısında PLAN↔KURGU EŞLEMESİ tablosu elle yapılır ve **SON ÜÇ KLİP ayrıca doğrulanır** [D81/D118] |
| THE_UPWARD_FALL | ⑪ + ② | **DÖNGÜ/ÇİFT KIRIK**: ilk kare 40 m'lik pürüzsüz gövdeler + KAHVERENGİ lif zemini ↔ son kare İNCE ÇAM + GRİ/KÜL zemin. "Jest tuttu, DÜNYA tutmadı" | ÇİFT KARTI (ACILIS_KAPANIS §5) PLAN'a sahne haritasından ÖNCE doldurulur; ⛔ ilk ve son karenin DÜNYASI aynı cümlelerle yazılır ve **konum kilidi** (figürün kadraj koordinatı) korunur |
| THE_UPWARD_FALL | ② + prompt denetimi | **ZEMİN ÇELİŞKİSİ PROMPTUN İÇİNDEYDİ**: WORLD bloğu "deep dry mat of fallen fibre", LIGHT bloğu "the pale grey floor" — aynı promptta iki cümle zemine iki renk verdi, film ortasında biyom değişti | Orman zemini **TEK CÜMLEDE, TEK RENKTE** tanımlanır ve o cümle 25/25 promptta birebir aynıdır. Prompt yazımından sonra `grep` ile zemin cümlesi sayılır: 25 tam eşleşme |
| THE_UPWARD_FALL | ⑪ kare kontrolü | **ÇIPLAK ÖNKOL (195-199 s)**: bilekten yukarısı deri, sadece eldiven var — 3,2 atm solunamaz ortamda sızdırmaz giysi kilidi delindi | Çıplak-deri negatifi ÜÇ BÖLGELİ yazılır ve `through the glove` gibi deriyi çağıran cümleler promptta geçmez [D175] |
| THE_UPWARD_FALL | teslim ölçümü | **ÜÇ TESLİM KUSURU**: üretici filigranı 225/225 s · kuyrukta 4,98 s başlık kartı · −16,1 LUFS / 0,0 dBFS | İhraç listesi SPEC E'ye yazılır: 1440p+ · BT.709 · 48 kHz · **−14 LUFS · −1,0 dBTP** · köşe testi · kuyruk kartı 0 kare |
| THE_UPWARD_FALL | sekiz merceğin sekizi | Paket HAZIRDI, operatör yine çıplak rubriği yapıştırdı → sekizi de mod V; sekizi de filigranı, çıplak önkolu, kırık döngüyü ve VAR OLAN ses yatağını kaçırdı | QA_SPEC + `rubrik_paketle.sh` çıktısı (PAKET_1..12) film klasörüyle birlikte teslim edilir; koşu MOD D olmadan T tablolarına satır yazılmaz [D129] |
| THE_BLACK_CRADLE | ⑤ ÇAPRAZ SAYIM | 🔧 21 kesme saydı, diğer DÖRT mercek "4 sahne" dedi ve 85 s'lik bir "sahne" uydurdu — hattın klip tavanı 10 s, öyle bir sahne bu boru hattında ÜRETİLEMEZ | ⑪ ölçüm kapısı ÖNCE koşulur; sahne/kesme sayısı MASTER'dan alınır, rapordan değil. Çapraz sayım kapısı parti geçerliliğinin ön şartıdır |
| THE_BLACK_CRADLE | 🧍 + 🧩 | **İki figürün ayrımı ekranda çöktü**: raporlar "yüzeyde kadın, kokpitte erkek, AYRI kişiler" okudu; oysa ikisi yüzeyde BİRLİKTE ve tek kabinde solda pilot, sağda mühendis. Ayrım RENGEYDİ (turkuaz ↔ amber) | ⛔ **AYRIM RENGE DEĞİL GEOMETRİYE YAZILIR**: gövde oranı · sırt teçhizatı · rol şeridinin KOLU · göğüs paketi. Renk yalnız İKİNCİL kanaldır ve karanlık/yağmurlu sahnede okunmaz [ASTRONOT_DONANIM §2 ışık kısıtı] |
| THE_BLACK_CRADLE | 🔊 SES | Gövdesiz AI'nin (MİRA) repliği EKRANDAKİ KADINA atfedildi; ters yönde HUMAN replik MACHINE yazıldı. Rapor 2 replik duydu, plan 14 diyordu | Replik varsa REGISTER HARİTASI plana yazılır ve **gövdesiz sesin kaynağı en az bir karede GÖSTERİLİR** (BORROWED_WEIGHT'in "Speaker Attribution" dersi) |
| THE_BLACK_CRADLE | 🔧 + kadraj | 0:30 ve 1:09'da **AĞIZ GÖRÜNDÜ VE OYNADI**; plan insanlı 13 sahnede kask KAPALI, kokpit ARKADAN diyordu | Ağız kadraj dışında tutulur; bu bir miks işi DEĞİL kadraj kararıdır. Geniş çekimde replik varsa `off-screen / comms audio, no lip-sync required` yazılır |
| THE_BLACK_CRADLE | 🧩 + plan | Filmin novumu **kör KIÇ ÖNDE yanaşma**ydı ve raporun okumasında o olay HİÇ GEÇMİYOR; final "kapalı HANGAR" okundu, plan "AÇIK YUVA" diyordu | Yanaşma vuruş seti (V1-V6) plana AÇIKÇA yazılır; ⭐V5 TEMAS'ta **kamera HEDEFTE, araç kameraya gelir** ve temasın imzası DURGUNLUKTUR (0,2 m/s). Novum bir yanaşma davranışıysa TEK KARE testi o davranışla koşulur |
| THE_BORROWED_WEIGHT | kurgu aritmetiği | Planın 25 sahnesi yerine **26 yuva**: ilk perdede +3 FAZLA KLİP, kuyrukta −2 EKSİK SAHNE, sonda yasaklı başlık kartı. Aynı replik 0:23 ve 0:33'te iki kez duyuldu = duplike klip | Kurgu kapısına: klip sayısı = 25 · süre 249 ± 2 s · **İNSAN ŞERİDİ** (bu filmde iki figürlü olduğu için `2`/`1`/`-` üç haneli yazılır) · son üç klip elle doğrulanır |
| THE_BORROWED_WEIGHT | 🔗 DEVAMLILIK | 2:50 kirli diz → 3:20 TEMİZ diz (yıpranma SIFIRLANDI) · 1:10 ↔ 1:50 yüz kemik yapısı değişti | Islaklık/çamur MONOTONİK sayaç olarak yazılır ve kabinde sıfırlanmaz; yüz tarifi kısa ve az öznitelikli tutulur (D167 ile aynı yere bakıyor) |
| THE_IRON_SLOPE | ④ HİKAYE **2,6** | **"THE ONE THING NOTHING ELSE DOES: none found."** Filmin bütün varlık sebebi novumdu; novum ekrana gelmedi ve izleyici 60 saniye "merdiven çıkan adam" gördü | ⛔ Novum kapısı 02_KONSEPT'te SERT koşulur: taşıyıcı NESNE + JEST, tek kare testi, ve novumun ekranda kanıtlandığı ≥3 sahne PLANA yazılır. Novum yoksa konsept REDDEDİLİR |
| THE_IRON_SLOPE | ⑥ FİZİK **3/10** | Kilit 3. saniyede 9,7 m istiyordu; serbest parça sabit ~0,15 m/s süzüldü — ivme prompta yazıldı, ekrana gelmedi | Sayısal kilitler KADRAJI TERK ETME SÜRESİNE yazılır ve QA_SPEC'in NUMERIC LOCK LIST'ine kopyalanır |
| THE_IRON_SLOPE | altı merceğin altısı | Kadrajda bir GEZEGEN vardı, 12 negatif bloğun 12'sinde `no planet, no moon` yazılıydı — **altısı da görmedi**; biri HİÇ VAR OLMAYAN sessizlikten 🔴 BLOCKER üretti | Her dış prompt EN BÜYÜK ARKA PLAN NESNESİNİ adlandırır; makineyle ölçülebilen sayı MODELE SORULMAZ — `olcum_kapisi.sh` teslimden önce koşar |
| THE_IRON_SLOPE | ⑩ ÖNERME KAPISI | Dört bulgu düştü ve dördü de TASARIMI kusur sanmıştı (0,220 g'de ağır gövde · planlı anten latisi · berrak vizördeki turuncu yansıma) | ⭐ **PLAN TASARIM KARARLARINI AÇIKÇA İLAN EDER**: 0,42 g'de ağır adım · kalın atmosferde yumuşak-derin gölge · berrak vizörde şimşek yansıması — üçü de PLANA "bu bir tasarımdır, kusur değildir" satırıyla yazılır |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **PB** kompozisyon | **Bedenden bir şeyin ÇIKARILMASI** eylemi (kask çıkarma) — "I can't make that type of video" ×2 | ✅ Sahne baştan yazıldı: nesneler en baştan sahnede, kimse bir şey çıkarmıyor; vuruş BAŞKA bir nesneye taşındı | Kabin içi sahneler — kask/eldiven/kemer takma-çıkarma cazibesi yüksek. ⛔ Hiçbir sahnenin eylemi "çıkarmak" olmayacak |
| **PB** kompozisyon | **Yüzsüz izolasyon + kısıtlanmış uzuv + tepeden makro** (yan yana iki ön kol) — deponun TEK çözülemeyen vakası, SAHNE İPTAL | ✅ Yalnızca kadraj değişince geçti: kamera nesne HİZASINA alındı, uzuvlar ARD ARDA ve farklı derinlikte dizildi. ⛔ Sözcük çözümü bu sınıfa UYGULANMAZ | Kemer/kayış bağlama, kol tutma, iki figürün ellerinin yan yana geldiği makro kareler |
| **PK** kelime | **Kişi tanımlama yüzeyi**: tek kişide yedi kimlik özniteliği üst üste, iki kişide ve 25/25 promptta + D79'un "face fully readable" kilidi yüz yüzeyini azamiye çıkarıyor | ⬜ ÖNERİLEN, henüz sınanmadı: kimlik yığını sökülür (kesin boy → göreli boy; ten/saç rengi ve yaş PLAN'da kalır), yüz tarifi yalnız yüzün KONU olduğu sahnelerde | ⛔ **BU FİLMİN 1 NUMARALI RED RİSKİ** — iki figür × 25 sahne ve referans paketi YOK. Karakter bloğu yazılırken öznitelik ÜÇTE tutulur |
| **PK** kelime | **MİLLİYET İFADESİ** — doğrulanmış tek red tetikleyicisi (`Israeli-American`); ⑯ açılış ölçümünde canlı promptlarda hâlâ 32 geçiş var ve KAYNAĞI bir kılavuz örneği | ✅ Milliyet satırı SİLİNDİ, yalnız fiziksel tanım kaldı | Character Bible — ⛔ bu filmde milliyet, ülke, ajans, kurum ve marka SIFIR |
| **PK** kelime | **Tehlike/şiddet sözlüğü NEGATİF blokta bile tetikliyor**: `gore/blood/wounds/corpse` yasak olarak yazıldığında bile promptu kategoriye sokuyor; `dangerous`, `panic`, `explosion`, `fire`, `smoke` aynı aile | ✅ Yasak satırı SİLİNDİ, malzeme POZİTİF tarif edildi: alev → `a faint dull-orange heat tint on the bars only` · duman → `a thin grey haze that thins as it rises and never curls` · panik → `she stops moving entirely for one second` | Fırtına, kalkış egzozu, acil durum ışıkları — sahneye-özel yasak listesi YAZILMAYACAK |
| **YR** yapısal | **İnsansız sahne + uzun `NEGATIVE:` bloğu + "Exactly 0 human figures"** — "I'm having a hard time fulfilling your request" | ✅ `NEGATIVE:` bloğu KALDIRILDI, tek pozitif `Style:` satırına indi | İnsansız sahneler (KART 10) — orman/kanopi/gezegen manzarası kareleri |
| **PB** kompozisyon (imza ⑥+⑦) | **Yüzü kapatan ekipman** (kask+vizör = "silahlı maskeli figür" okuması) ve **kırmızı ton yoğunluğu + yakın plan** — ikisi de bu deponun VARSAYILAN malzemesi ve hiçbir kapıda sayılmıyordu | ✅ ⑥'nın karşılığı D79 kilidinin kendisidir (yüz okunur) · ⑦ için kırmızı KAYNAĞA bağlanır ve kadrajda gri/mavi referans yüzey bırakılır | Acil durum kırmızısı taşıyan kabin ve kalkış kareleri; ECU/CU basamağına **çevresel çapa cümlesi** eklenir |
| **MÇ / TK** | **0 BAŞARI kuralı**: aynı oturumda hiç geçen prompt yoksa sayı promptu değil ÜRETİM TARAFINI işaret eder; "üretim ilerledi sonra düştü" ise maskeli çıktı reddidir ve tekrar denemek İŞE YARAMAZ | ✅ PROB KOŞUSU üçüncü yeniden yazımdan ÖNCE koşulur; MOTOR ve İLERLEDİ sütunları ANINDA elle yazılır (sonradan kurtarılamaz — engellenen üretimde dosya OLUŞMAZ) | Üretim aşaması — bu film için kayıt disiplini kuralı |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        34 satır
QA ARIZASI:         23 satır  (5 film kaydından)
RED SINIFI:          8 satır  (PB ×3 · PK ×3 · YR ×1 · MÇ/TK ×1)

⛔ EN PAHALI ÜÇÜ — bunlar 04_UYARI_NOTLARI'nda ⛔ satırı olur:

① İKİ FİGÜRÜN KİMLİĞİ VE AYRIMI
   COUNTED TURN tek karakterle kimliğini kaybetti (② 3,0 IDENTITY BREAK);
   BLACK CRADLE iki figürü RENKLE ayırdı ve beş merceğin beşi de "ayrı
   sahnelerde ayrı kişiler" okudu; SINKING STAKE'in yedi öznitelikli
   karakter bloğu POLİTİKA REDDİ aldı. Üçü aynı yere bakıyor: ayrım
   GEOMETRİDE olacak, öznitelik ÜÇTE kalacak, dizilim kilidi PLANDA olacak.
   → ⑤ TUR seçiminin üç kaydı da bu satırı besliyor.

② PLANIN SONU EKRANA GELMİYOR
   UPWARD FALL S24'ü (doruk + twist + kapak karesi) teslim etmedi ·
   BORROWED WEIGHT kuyrukta iki sahne eksik ve S24 twist'i yok ·
   RING WALKER doruğunu monte etmedi · BANDED DEEP finalsiz kurguya
   "Ending 8.0" aldı. Kök: üretim sırası dramatik sırayla aynı [D168]
   ve kurgu kapısı SIRAYI doğrulamıyor [D118].
   → ÜRETİM SIRASI DORUKTAN başlar; PLAN↔KURGU eşlemesi elle yapılır.

③ EL-NESNE TEMASI VE EFOR
   COUNTED TURN'ün on bir 🔴 blocker'ının YEDİSİ el/kayış/karabiner
   penetrasyonu; ⑦ Temas 4/10; ⑧ EFOR 0.0 NOBODY PAYS. Bu film koşu,
   tırmanma, kemer ve tutamak üstüne kurulu — aynı yüzeye basıyor.
   → çarpışma cümleleri negatif çekirdeğe · kayış sayısı minimuma ·
     sahne başına COST hanesi.
```
