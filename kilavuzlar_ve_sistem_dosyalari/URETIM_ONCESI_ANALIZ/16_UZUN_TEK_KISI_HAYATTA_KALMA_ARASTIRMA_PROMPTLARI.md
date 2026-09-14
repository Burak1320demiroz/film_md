# 🔬 16 — UZUN FORM TEK KİŞİLİK HAYATTA KALMA ARAŞTIRMA PROMPTLARI (07.09.2026)

> **Ne bu dosya:** sahibin 07.09.2026 kararıyla açılan yeni yatay filmin —
> **Mars'ta mahsur kalan tek adam, `The Martian` ekseni, 15 faz × 12 sahne
> × 10 s, replikli** — plan yazılmadan önce kapatılması gereken dört açık
> sorusu için hazırlanmış dört derin araştırma promptu. Her biri **altı
> cümledir** ve **salt prompt** çalışır — kopyala, araştırma aracına
> yapıştır, başka hiçbir şey verme.
>
> **Neden dosyada duruyor:** sistem bilgisi sohbette yaşayamaz. Aynı prompt
> ileride yeniden koşulacaksa **aynı metin** koşulmalı; yoksa iki turun
> sonucu karşılaştırılamaz (07-15'in gerekçesiyle aynı).
>
> **KOŞU KAYDI:** ⚠️ 07.09.2026 — 1·2·3 koşuldu, **4 (metinsiz geçen zaman
> merdiveni) KOŞULMADI** (`TUR13_HAM_RAPORLAR/00_KUNYE.md`). Süzme:
> `04_ARASTIRMA_BULGULARI.md` §TUR 13. Ham metinler klasöre birebir
> kopyalanmadı — künye "bekliyor" der. 4. promptun aynı metni
> `19_…` §1 olarak yeniden koşulacak; raporu `TUR13_HAM_RAPORLAR/`'a iner.
> *(Bu satır 11.09.2026'ya kadar "koşulmadı" diyordu — künyeyle hizalandı.)*
>
> 🔗 **KARDEŞ DOSYA `17_THE_MARTIAN_EKSEN_FILMI_ARASTIRMA_PROMPTLARI.md` (TUR 14):**
> 16 TÜRÜ sorar (çoğul örnek, genel mekanizma), 17 EKSEN FİLMİ söker
> (tek yapım, zaman damgası). Sekiz raporun süzmesi çapraz okunur —
> 17·1 ↔ 16·3 ve 17·2 ↔ 16·2 çelişirse hiçbiri inmez.
> ⛔ PLAN, sekizinin de süzmesi bitmeden yazılmaz.

---

## 🧾 FİLMİN KÜNYESİ (sahip kararı 07.09.2026) — ve üç açık çelişki

```
Referans eksen : The Martian (YERÇEKİMİ'nin Gravity ekseni gibi)
Yapı           : 15 faz × 12 sahne × 10 s = 180 sahne = 1.800 s = 30:00
Motor          : OMNI 1.1 Flash ("Osmi")
Öncelik        : ① HOOK  ② DİYALOG
```

⚠️ **ÇELİŞKİ 1 — BANT TAVANI AŞILIYOR.** `yatay_10_20_dk_filmler/README.md`
10 saniyelik sahne varyantı için **faz tavanını 10 (120 sahne · 20:00)**
yazar; 11 faz "❌ formatı aşar" satırındadır. 15 faz tavanın **%50
üstüdür** ve **12 fazın üstünde PERDE kuralı yoktur** — 3 perde en fazla
4-4-4 dağıtır. Bu bir hata değil, **karar**: ya bant kartı yeniden
yazılır (yeni üst katman + yeni süre satırı), ya faz 10'a iner.
⭐ **3 numaralı prompt tam olarak bu boşluğu kapatmak için yazıldı** —
15 birimlik yapının üstünde hangi katman durur, dışarıdan sorulur.

⚠️ **ÇELİŞKİ 2 — THE MARTIAN'IN ZAMAN SAYACI EKRAN YAZISIDIR.** O film
geçen zamanı `SOL 18` ara yazılarıyla ve video günlüğünün sözlü tarih
bildirimiyle taşır. Bu hatta **okunur metin, ara yazı, başlık kartı ve
altyazı YOKTUR**. Yani referans filmin zaman motoru **bize kapalı** ve
30 dakikada aylar geçecek. ⭐ **4 numaralı prompt bunun için yazıldı.**

⚠️ **ÇELİŞKİ 3 — OMNI, ÜRETİM DURDURAN MOTORDUR.** `POLITIKA §6`: Omni
"kesintisiz zincir · ilk/son kare · stil devamı" için **doğru** motordur —
180 sahnelik bir zincirin ihtiyacı tam budur. Ama aynı tablo Omni'nin
"ünlü kişi" yanlış-pozitifini **Veo'dan AĞIR** yazar ve `09_URETIM_RED_DEFTERI`
**vaka 15** bir filmi yarıda öldürdü (THE SINKING STAKE · 25/14 sahne ·
doruk hiç üretilmedi). Tetikleyici ölçüldü: kişi başına yedi kimlik
özniteliği [D167 → kapı ⑲]. ⛔ Karakter bloğu yazılırken kapı ⑲ koşar.
⚠️ Ayrıca `VEO_3_1_FAST_DIYALOG` kılavuzunun tamamı **Veo'ya özeldir**
(çift akışlı difüzyon, tırnak sentaksı); Omni'nin replik/lip-sync
davranışı bu depoda **hiç ölçülmedi**. ⭐ **2 numaralı promptun dördüncü
cümlesi bunu dışarıdan sorar.**

---

```
⛔ ÇIKTI DOĞRUDAN KILAVUZA VE PLANA GİRMEZ.
   Sıra: araştırma → 04_ARASTIRMA_BULGULARI.md §TUR 13 (süzme kaydı) →
         ancak oradan HOOK_VE_ILK_SAHNE · SES_VE_DIYALOG_URETIM ·
         KURGU_RITMI_VE_IHRAC · SAHNE_DEVAMLILIK · yatay bant kartı ·
         03_PLAN_ONCESI. Süzme kaydı İKİ liste tutar: NEYİN GİRDİĞİ ve
         NEYİN GİRMEDİĞİ + NEDEN.

⛔ BU ARAŞTIRMA "THE MARTIAN NASIL YAPILDI" DERLEMESİ DEĞİLDİR.
   Aranan şey hayranlık değil MEKANİZMA + ZAMAN DAMGASI. Referans film
   bir ÖRNEKTİR, kopyalanacak bir şablon değil [MESHUR_SAHNE §4: film
   adı, marka ve tescilli tasarım adı hiçbir üretim promptuna yazılmaz;
   bulgu GEOMETRİYE ve MEKANİZMAYA çevrilerek iner].

⛔ SAYI ÜÇ ETİKETLE GELİR, ETİKETSİZ İNMEZ.
   (a) filmden ÖLÇÜLMÜŞ zaman damgası · (b) PLATFORM istatistiği
   (örneklem + tarih ile) · (c) raporun kendi TASARIM ÖNERİSİ.
   Örneklemsiz (b) TUR 1'deki muameleyi görür: DÜŞER.

⛔ ÖNCEKİ TURLARLA ÇAKIŞMA — yeniden istenmeyenler.
   • Dikey ilk-3-saniye tutundurma yüzdeleri (TUR 1) → 1 yalnız
     20-35 dk bandını ister.
   • Açılış planı ilk-imge doktrini, kapanış tipolojisi, açılış-kapanış
     çifti, 10-20 dk band bütçesi (TUR 10) → 1 bunları TEKRARLAMAZ;
     yalnız 20-35 dk bandını ve HAYATTA KALMA türünü sorar.
   • Replik kalitesi ölçütleri, alt metin, konuşma İngilizcesi sözcük
     dağarcığı, hakem güvenilirliği (TUR 6) → 2 bunları istemez;
     2'nin konusu MUHATAP ve ÜRETİLEBİLİRLİKTİR.
   • Repliğin varlığı/yeri, ağız ekranda mı (TUR 4 · 3) → istenmez.
   • Çıkarılabilir an, sözsüz istek-hasım, az replikli senaryo (08) →
     istenmez.
   • Referans/kimlik adaptörü matrisi (15 · TUR 12) → istenmez.
   Rapor yine getirirse süzme kaydı "ZATEN VAR" etiketiyle geçer,
   kılavuza ikinci kez İNMEZ.

⛔ DEPONUN HİPOTEZLERİ PROMPTLARA GÖMÜLMEZ.
   "Az replik iyidir", "sessizlik gerilim kurar", "prosedürel sürükler"
   bu deponun uygulamalarıdır, kanıtlanmış yasa değil — sorular İKİ
   YÖNLÜ sorulur (monologun sıktığı vakalar, prosedürelin görev
   listesine döndüğü vakalar, uzun açılışın terk ürettiği vakalar da
   istenir). Üretim kısıtları hipotez değil FİLTREDİR ve promptlara
   açıkça yazılır.

⛔ RAPORLAR ÇAPRAZ OKUNUR — üç çift.
   1 ↔ 3 : 1'in ölçtüğü ilk dramatik hamle saniyesi ile 3'ün birinci
           biriminin bittiği yer aynı filmde tutmalı.
   2 ↔ 4 : 2'nin konuşma yoğunluğu ile 4'ün zaman merdiveni aynı
           sahnede çakışıyorsa (replik zamanı söylüyorsa) çelişki değil
           İKAME'dir — hangisi taşıyıcı, rapor söylesin.
   3 ↔ 4 : 3'ün başarısızlık aralığı ile 4'ün gövde/mekân kademeleri
           aynı birimlere düşüyor mu; düşmüyorsa yükselme görünmez.
```

**Hangi prompt hangi açık soruyu kapatır:**

| # | Konu | Deponun açık sorusu | Besleyeceği yer |
|:--:|---|---|---|
| 1 | **Uzun formda tek kişilik hayatta kalma açılışı** | HOOK çalışmasının tamamı DİKEY ve KISA; 20-35 dk bandının terk eğrisi ve açılış sözleşmesi hiçbir kılavuzda yok; §0③ kanca skoru hâlâ PLATO | `HOOK_VE_ILK_SAHNE` §1 · §2 · §4 · yatay bant kartı · `03_PLAN_ONCESI` |
| 2 | **Yalnız adamın muhatabı + 10 s klipte replik üretimi** | `FINAL` muhatabı yalnız SON kare için tanımlar; 30 dakika boyunca kime konuşulduğu yazılı değil. Omni'nin replik/lip-sync davranışı ölçülmedi; kılavuz Veo'ya özel | `SES_VE_DIYALOG_URETIM` · `VEO_3_1_FAST_DIYALOG` (motor bölümü) · `PROMPT_KONTROL/DIALOGUE_CRITIQUE` |
| 3 | **15 birimlik prosedürel: problem zinciri ve fazların üstündeki katman** | Bant kartı 12 fazda biter, 15 faz için ÜST KATMAN kuralı YOK. `06_HIKAYE_HATTI_TESHISI`: ilerleme ölçülmüş biçimde yok — sahip ifadesi *"ne mantıklı ilerleme var ne sahneler arası devamlılık"* | yatay bant kartı (yeni süre + katman satırı) · `KURGU_RITMI_VE_IHRAC` · `06` §4 · `03_PLAN_ONCESI` |
| 4 | **Metinsiz geçen zaman: gövde ve mekân merdiveni** | Okunur metin yasak, referans filmin zaman motoru ara yazı. Depoda yalnız "kir merdiveni" var [D147/D155] ve o da tek eksen; aylar süren değişimin kademe boyu hiç ölçülmedi | `SAHNE_DEVAMLILIK` · `REFERANS_PAKETI_KILAVUZU` · `FAZ_DOSYASI_SABLONU` (§kilitler) · `02_RISK_KARTLARI` |

---

# 1️⃣ AÇILIŞ — UZUN FORMDA TEK KİŞİLİK HAYATTA KALMA FİLMİNİN İLK DAKİKALARI

```
Yirmi ile otuz beş dakika arasındaki tek karakterli hayatta kalma anlatılarının açılışını mekanizma düzeyinde sök: felaketi kadrajda gösteren açılışlar ile felaketten SONRA uyanışla başlayan açılışlar arasındaki farkı, her iki kalıbın izleyiciye "bu insan mahsur ve yalnız" bilgisini kaç saniyede verdiğini, bilgiyi hangi kanalla (görüntü, ses, karakterin bir işi yapıyor olması, replik) taşıdığını ve ilk geri dönülmez eylemin kaç saniyede geldiğini ölçülmüş örneklerle (The Martian, Cast Away, All Is Lost, Moon, Buried, 127 Hours, Oxygen, Stowaway, Gravity ve ödüllü uzay kısa filmleri) zaman damgasıyla belgele. Yirmi-otuz beş dakikalık bandın terk eğrisini ayrı ölç: uzun form video platformlarında bu uzunlukta ilk otuz saniyede, ilk iki dakikada ve beşinci dakikada görülen düşüşler nedir, izleyicinin "bırakma" modundan "izliyorum" moduna geçtiği belgelenmiş bir eşik var mı, tek karakterli ve az olaylı içeriğin eğrisi çok karakterli içerikten nasıl ayrışır ve her sayıyı örneklem büyüklüğü, tarihi ve kaynağıyla ver. Açılışın kurduğu SÖZLEŞMEYİ çıkar: ilk dakikada izleyiciye verilen vaadin (kurtulacak mı, ne kadar zamanı var, engel tam olarak ne) hangi somut öğelerle kurulduğunu, kalan kaynağın ya da sürenin görünür kılınmasının bağlılığı ölçülmüş biçimde artırıp artırmadığını, karakterin ilk repliğinin kaç saniyede geldiğini ve o ilk repliğin işlevinin ne olduğunu (durum bildirme, kendine seslenme, olmayan birine seslenme, mizah) tek tek belgele. Aynı soruları ters yönden de sor: hangi vakalarda uzun ve sakin açılış terk üretti, felaketi öne alan açılış filmin en güçlü imgesini ilk dakikada harcayıp geri kalanı düz mü bıraktı, prosedürel ve sakin açılışın çok karakterli bir açılıştan daha iyi tuttuğu ölçülmüş vakalar hangileridir ve festival programcılarıyla platform editörlerinin ilk iki dakikada eleme yaptığına dair belgelenmiş ifadeler ile hangi açılış hatasının eleme sebebi sayıldığını topla. Kritik kısıt: hedef film otuz dakikadır ve kadrajda tek insan vardır, her sahne kesmesiz ON SANİYELİK tek plandır ve image-to-video zinciriyle üretilir, başlık kartı, jenerik, ara yazı, okunur metin ve altyazı yoktur, replik yalnız İngilizcedir, yüz yalnız basınçlı iç mekânda görünür (dışarıda vizör kapalıdır ve konuşma telsiz sesidir) ve ilk kare aynı zamanda akıştaki kapak karesidir — bu yüzden ara yazıya, montaj sekansına, ikinci karaktere, dış sesli anlatıcıya ve hızlı kesmeye dayanan açılışları işaretleyip ele, tek figürle ve tek planla kurulanları öncelikle. Çıktıyı iki tablo olarak ver: (a) film, açılış kalıbı, "mahsur" bilgisinin saniyesi ve kanalı, ilk repliğin saniyesi ve işlevi, ilk geri dönülmez eylemin saniyesi, ilk kesmenin saniyesi ve tek planda uygulanabilirlik notu; (b) yirmi-otuz beş dakikalık bant için açılış bütçesi — ilk dramatik hamlenin EN GEÇ hangi saniyede ve kaçıncı on saniyelik sahnede olması gerektiği, kaynağı ve etiketi (ÖLÇÜLMÜŞ / PLATFORM / ÖNERİ) ile birlikte; ayrıca ilk on iki sahnelik açılış birimi için doldurulacak bir "açılış sözleşmesi kartı" şablonu ekle (hangi bilgi hangi sahnede verilir, hangisi ertelenir, hangi soru açık bırakılır).
```

---

# 2️⃣ YALNIZ ADAM KİME KONUŞUR — MUHATAP SİSTEMİ VE ON SANİYELİK KLİPTE REPLİK

```
Tek karakterli anlatılarda karakterin sesli konuşmasını meşru kılan MUHATAP çözümlerinin tipolojisini çıkar: kayıt cihazına konuşma (video günlüğü, ses kaydı, kara kutu), uzaktaki ve cevap vermeyen bir alıcıya konuşma (telsiz, merkez, kurtarma ekibi), bir nesneye ya da hayvana konuşma, ölmüş ya da yokta olan birine konuşma, kendine konuşma ve doğrudan kameraya konuşma — her tipin hangi filmde nasıl kurulduğunu, kurulumun kaç saniye sürdüğünü, izleyicinin bunu "yapay" bulmadan kabul etmesi için hangi gerekçenin (kayıt zorunluluğu, prosedür, delilik, alışkanlık) sahnede kurulduğunu ve tipin film boyunca değişip değişmediğini örneklerle belgele. Konuşma yoğunluğunu SAYIYLA ölç: bu filmlerde dakikaya düşen replik saniyesi ve kelime sayısı nedir, en uzun kesintisiz sessizlik ne kadardır, karakter ilk kez kaçıncı dakikada konuşur, konuşma yoğunluğu filmin başından sonuna doğru artar mı azalır mı ve bu eğri hikâyenin yalnızlık derecesiyle ilişkilendirilmiş midir — her sayıyı filmden ölçülmüş olarak, kaynağıyla ver. Monologun NEDEN çalıştığını ve nerede çöktüğünü iki yönlü araştır: seyircinin sesli düşünmeyi kabul ettiği koşullar ile "kendi kendine konuşuyor" diye yapay bulduğu koşullar arasındaki farkı ayıran dramaturji kaynaklarını ve eleştiri kanıtını topla, bilgiyi izleyiciye taşımak için söylenen açıklayıcı repliğin (kendi durumunu kendine anlatan karakter) hangi vakalarda kabul edilip hangilerinde alay konusu olduğunu belgele, ve tek kişilik filmlerin sessiz kalmayı seçtiği vakalarda bilginin hangi kanalla taşındığını yaz. Üretim tarafını ayrı ve somut sor: bugün çalışan video üretim motorlarında (Google Veo 3.x ailesi, Gemini Omni / Flash video, Kling, Runway, Hailuo, Sora ve ses-güdümlü konuşan-insan modelleri) bir görselden başlatılan ON SANİYELİK tek klipte senkron replik üretmek için hangi sözdizimi kullanılır, on saniyeye rahatça sığan kelime sayısı ölçülmüş olarak kaçtır, dudak senkronu hangi kadraj ölçeğinin altında bozulur, yüz kapalı bir kask vizörünün ardındayken ya da konuşma telsizden gelirken model sesi yine de üretir mi, sesi klip içinde üretmek ile sessiz üretip sonradan seslendirmek arasındaki fark hangi ölçütlerde (senkron, ton, tekrar üretilebilirlik, maliyet, politika reddi) belgelenmiştir ve motorlar arasında replikli üretimde reddedilme davranışı nasıl ayrışır. Kritik kısıt: hedef film otuz dakika ve yüz seksen sahnedir, kadrajda tek insan vardır ve ikinci bir insan sesi ya da görüntüsü hiçbir sahnede bulunamaz, her sahne kesmesiz on saniyelik tek plandır, okunur metin ve altyazı yoktur, replik tamamen İngilizcedir, yüz yalnız basınçlı iç mekânda çıplaktır ve dış mekânda vizör kapalıdır — bu yüzden karşılıklı diyaloga, ikinci sese, telefon konuşmasına, geri dönüşe ve dış sesli anlatıcıya dayanan çözümleri işaretleyip ele, tek sesle ve cevapsız muhatapla kurulanları öncelikle. Çıktıyı iki tablo olarak ver: (a) muhatap tipi, film örneği, kurulum sahnesi ve süresi, meşrulaştırıcı gerekçe, film boyunca değişimi, tek insan kısıtı altında uygulanabilirliği ve tek satırlık İngilizce sahne ifadesi; (b) motor adı, on saniyelik klipte replik sözdizimi, sığan kelime sayısı, dudak senkronu için gereken en dar kadraj ölçeği, vizör ardında ve telsiz sesinde davranışı, klip içi ses mi sonradan seslendirme mi önerildiği, kaynağı ve tarihi; ayrıca yüz seksen sahnelik bir filme yayılacak "konuşma yoğunluğu eğrisi" için faz başına replik saniyesi öneren bir şablon ekle ve her sayıya ÖLÇÜLMÜŞ, PLATFORM ya da ÖNERİ etiketini koy.
```

---

# 3️⃣ ON BEŞ BİRİMLİK PROSEDÜREL — PROBLEM ZİNCİRİ, BAŞARISIZLIK ARALIĞI VE ÜST KATMAN

```
Hayatta kalma prosedürellerinin problem zincirini anatomik olarak sök: bir karakterin arka arkaya sorun çözerek ilerlediği anlatılarda (The Martian, Apollo 13, Cast Away, All Is Lost, Gravity, 127 Hours, Moon, Arctic, The Revenant) filmin tamamında kaç ayrı problem kurulur, her problem kaç dakika sürer, çözüm ile yeni problemin doğuşu arasında kaç saniye geçer, problemler birbirinden bağımsız mıdır yoksa bir öncekinin çözümü bir sonrakini mi doğurur ve bu zincirin halkalarını zaman damgasıyla listele. Başarısızlığın aralığını ölç: bu filmlerde denemelerin yüzde kaçı başarısızlıkla biter, ilk başarısızlık kaçıncı dakikada gelir, en büyük kayıp (yapılanın yıkılması, kaynağın yok olması, planın çökmesi) toplam sürenin yüzde kaçında yer alır, art arda kaç başarı geldiğinde izleyici gerilimi kaybeder ve tersine art arda kaç başarısızlık geldiğinde umutsuzluk terk üretir — kuram, yapım notları ve eleştiri kanıtıyla, sayıları ölçülmüş olarak ver. On beş birimden oluşan uzun anlatıların ÜST KATMANINI araştır: on beş bölümlük, on beş sekanslı ya da benzeri çok birimli yapılarda birimlerin üstünde hangi katman kurulur (perde, kısım, hareket, bölüm kümesi), on beş birim üç perdeye hangi oranlarla dağıtılır, orta nokta ve "her şey bitti" anı hangi birime düşer, birimlerin kendi içinde tekrarlayan bir iç yapısı (kur-dene-başarısız ol-bedel öde) var mıdır ve otuz dakikalık bir işin on beş birime bölünmesi izleyici tarafında ölçülmüş bir avantaj mı yoksa parçalanma riski mi üretir. Prosedürelin nerede sıkıcı bir görev listesine döndüğünü iki yönlü sor: hangi vakalarda teknik süreç anlatısı izleyiciyi kaybetti ve eleştiri bunu nasıl tarif etti, süreci sürükleyici kılan somut değişkenler nelerdir (görünür bahis, sayılabilir kaynak, sıkışan takvim, karakterin kişiliğinin işe sızması, seyircinin karakterden önce tehlikeyi görmesi), aynı görevin tekrarlanmasının bıktırdığı ile ritim kurduğu vakalar hangi farkla ayrışır ve tek karakterli anlatıda çatışmanın "insan karşıtı" olmaması ölçülmüş bir dezavantaj mıdır. Kritik kısıt: hedef film on beş fazdır, her faz kesmesiz on saniyelik on iki sabit plandan kuruludur ve toplam yüz seksen sahne ile otuz dakikadır, kadrajda tek insan vardır, ara yazı ve okunur metin yoktur, geriye dönüş ve paralel kurgu kullanılamaz (ikinci mekân ve ikinci karakter yok) ve her sahne kendi başına tek bir plan olduğu için sahne içi kesmeyle hızlanma mümkün değildir — bu yüzden montaj sekansına, paralel kurguya, ikinci hikâye hattına ve dış sesli özetlemeye dayanan yapı çözümlerini işaretleyip ele, tek hat ve sabit plan altında çalışanları öncelikle. Çıktıyı üç yapıda ver: filmlerin problem zincirini gösteren bir tablo (film, problem numarası, başlangıç ve bitiş zaman damgası, sonuç, doğurduğu yeni problem, ödenen bedel); on beş birimlik bir yapı için birim birim doldurulmuş bir defter şablonu (birim numarası, üst katman, problem, deneme, sonuç, kaynak durumundaki değişim, süre baskısındaki değişim, izleyiciye açılan yeni soru); ve otuz dakikalık tek karakterli iş için orta nokta, en büyük kayıp ve doruğun hangi birime düşmesi gerektiğini gerekçesiyle söyleyen bir öneri satırı — her sayıya ÖLÇÜLMÜŞ, PLATFORM ya da ÖNERİ etiketini koy ve on beş birimi tavsiye etmiyorsan hangi birim sayısını neden önerdiğini yaz.
```

---

# 4️⃣ METİNSİZ GEÇEN ZAMAN — GÖVDE, GİYSİ VE MEKÂN MERDİVENİ

```
Uzun süre geçtiğini yazı, ara yazı, sayaç ve dış sesli anlatıcı KULLANMADAN gösteren filmleri sistemli olarak sök: haftaların, ayların ya da yılların geçtiği tek mekânlı ve tek karakterli anlatılarda (Cast Away, The Martian, Moon, Robinson uyarlamaları, Le Trou ve hapishane filmleri, Arctic, The Revenant, Silent Running) zamanı taşıyan kanalları tek tek ayır — gövde, giysi, mekânın birikmesi, kaynağın azalması, ışık ve mevsim, tekrarlanan ritüelin değişmesi — ve her kanalın filmde hangi dakikalarda hangi kademelerle ilerlediğini zaman damgasıyla belgele. Gövde merdivenini sayıyla çıkar: sakalın, saçın, tırnağın ve yaraların gerçek hayatta hangi hızla değiştiği ile filmlerin bunları hangi hızla gösterdiği arasındaki farkı, karakterin kilo kaybının makyaj, protez ya da fiziksel dönüşümle nasıl kademelendirildiğini, yapım notlarında kaç ayrı "gövde durumu" tasarlandığını ve iki ardışık durum arasındaki farkın izleyici tarafından fark edilmesi için ne kadar büyük olması gerektiğini kaynaklarıyla ver. Mekân ve kaynak merdivenini aynı titizlikle ölç: kapalı bir yaşam alanında zaman geçtiğini gösteren birikmeler (eşyanın dağılması, toz, onarım izleri, çizik ve yama sayısı, duvara işlenen izler, bitkinin büyümesi, erzağın azalması, çöpün artması) hangi filmlerde hangi kademelerle kullanılmıştır, bir kademenin fark edilir olması için kadrajın yüzde kaçını kaplaması gerektiğine dair algı çalışması ya da yapım kararı var mıdır, ve fazla hızlı ilerleyen bir merdivenin (bir sahnede sakal, ötekinde tıraş) devamlılık hatası olarak okunduğu vakaları belgele. Aynı soruyu ters yönden de sor: hangi vakalarda izleyici geçen zamanı hiç fark etmedi ve eleştiri bunu "zaman duygusu yok" diye yazdı, hangi filmler zamanı taşımak için sonunda ara yazıya ya da sözlü tarih bildirimine mecbur kaldı ve bu mecburiyetin sebebi neydi, metinsiz zaman geçişinin izleyiciyi kaybettiği eşik belgelenmiş midir ve tek mekânlı bir işte zamanın hiç geçmiyor hissi hangi somut eksiklikten doğar. Kritik kısıt: hedef film otuz dakikadır ve on beş fazın her biri on iki sahnelik kapalı bir birimdir, sahneler kesmesiz on saniyelik tek planlardır ve her sahne bir önceki karesinden zincirlenerek yapay zekâyla üretilir — bu zincir kir, aşınma, yaralanma ve dağınıklık gibi birikimli durumları KENDİLİĞİNDEN SIFIRLAR ve her kademenin sahne sahne yazılı olarak taşınması gerekir; ayrıca okunur metin, ara yazı, takvim, sayaç ve dış sesli anlatıcı yoktur, kadrajda tek insan vardır ve yüz yalnız basınçlı iç mekânda görünür — bu yüzden ara yazıya, montaj sekansına, mevsim geçişine ve ikinci karakterin tepkisine dayanan çözümleri işaretleyip ele, tek figür ve tek mekânla çalışanları öncelikle. Çıktıyı iki tablo ve bir şablon olarak ver: (a) zaman kanalı, film örneği, kademe sayısı, kademeler arası gerçek süre karşılığı, kadrajdaki görünürlüğü ve tek planda kurulabilirliği; (b) fark edilirlik eşiği — hangi kanal ne kadar değişirse izleyici zamanı okur, kaynağı ve etiketi ile; ve on beş fazlık bir film için doldurulacak bir "ZAMAN MERDİVENİ" şablonu — faz numarası, o fazda hangi kanalın kaç kademe ilerlediği, kademenin İngilizce tek satırlık kadraj ifadesi ve o kademenin hangi sahnede ilk kez görüneceği; ayrıca aynı anda kaç kanalın birden ilerlemesinin fazla olduğunu ve hangi kanalın ana taşıyıcı seçilmesi gerektiğini gerekçesiyle söyle.
```

---

# 📥 KOŞU SONRASI — dört adım, atlanmaz

```
1. Dört rapor HAM hâliyle saklanır: TUR13_HAM_RAPORLAR/ (düzeltilmez,
   kısaltılmaz — kaynak listeleri dâhil). Prompt metinleri her ham
   dosyanın başına birebir kopyalanır (Tur 7 usulü).
2. 04_ARASTIRMA_BULGULARI.md'ye §TUR 13 açılır ve İKİ liste yazılır:
   GİRDİ (bulgu · hangi dosyaya · tipi) ve GİRMEDİ (bulgu · NEDEN).
   Her sayı ÜÇ etiketten birini taşır: ÖLÇÜLMÜŞ · PLATFORM · ÖNERİ.
   TUR 1/4/6/10/12'de zaten inen bulgular "ZATEN VAR" etiketiyle geçer.
3. ⛔ Raporlar ÇAPRAZ OKUNUR (1↔3 · 2↔4 · 3↔4). Tutmayan sayı kılavuza
   İNMEZ, çelişki kayda geçer.
4. Ancak ondan sonra: HOOK §1/§2/§4 · SES_VE_DIYALOG §2a · yatay bant
   kartının süre tablosu ve üst katman satırı (⚠️ ÇELİŞKİ 1 burada
   kapanır) · SAHNE_DEVAMLILIK zaman merdiveni · 03_PLAN_ONCESI.
   ⛔ PLAN, bu dört süzme yapılmadan YAZILMAZ.
```

⬜ **VE BU DOSYANIN KENDİ SINIRI:** dört prompt da DIŞ bilgi getirir.
Örneklerin tamamı çok karakterli, kesmeli ve insan eliyle çekilmiş
yapımlardır; tek insan, kesmesiz on saniyelik plan, metinsiz kapanış ve
yapay zekâ zinciri kısıtı altında hiçbir bulgu üretimde test edilmeden
bağlayıcı değildir. 2 numaralı promptun motor tablosu en hızlı bayatlayan
kısımdır ve `04`'ün TUR 12 kaydı sağlayıcı tarihlerinin yanlış geldiğini
zaten ölçtü — bu turda da tarih hücresi ayrı şüpheyle okunur.
