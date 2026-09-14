# 🧾 THE_COUNTED_TURN — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu — 107 satır, 107'si ✅.
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.
>
> ⛔ **D187 — HER TAŞIYICI KİLİDİN YANINA ONU ÖLÇECEK MERCEĞİN ADI YAZILIR.**
> Mercek adı taşımayan kilit ölçülmemiş sayılır: on iki rapor onu görmeden döner.
> Mercek adları: ① KARE · ② DEVAMLILIK · ③ SES · ④ HİKAYE · ⑤ ARKA PLAN ·
> ⑥ FİZİK · ⑦ AKSİYON · ⑧ EFOR · ⑨ KADRAJ · ⑩ OYUNCULUK · ⑪ IŞIK · ⑫ HOOK ·
> ⑪ÖLÇ = `olcum_kapisi.sh` (makine) · PK = `prompt_kontrol.py` (üretimden önce).

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

### 1a · ORTAM VE NOVUM — §3.7'nin doğrudan çarptığı yer

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D174** | THE LEANING ROOM: plan "yatma 12/12 SCREEN-RIGHT" dedi, ekranda S7'de lamba SCREEN-LEFT'e yattı — **model yönü okumuyor, yön bir nesneye bağlanmadıkça yuvarlanıyor** | Dönme yönü ekran-yönü kelimesiyle DEĞİL, **kadrajdaki ADI KONMUŞ bir nesneye** bağlanır ve **ikinci bir gövde aynı yönü teyit eder**: yıldız alanı korkuluğun üst kenarını ADIM ADIM geçer + güvertedeki düz kenar aynı yöne eğilir. Yön cümlesi 25/25 promptta BİREBİR aynı kelimelerle. | 25/25 · özellikle geniş kurulumlar → ÖLÇEN: ⑥ FİZİK cat.7 (hız/zamanlama) + ⑨ KADRAJ cat.7 (ekran geometrisi) |
| **D127** | THE IRON SLOPE: Motion Bible "3. saniyede 9,7 m" diyordu, ölçüm serbest panelin **sabit ~0,15 m/s** süzüldüğünü gösterdi; kilitli değer kadrajın 2,5 katıydı → **novum ekrana hiç gelmedi** | Hiçbir harekete İVME yazılmaz. Her hareket **"kadrajı N saniyede terk eder"** ya da **"N saniyede M gövde boyu yol alır"** biçiminde SÜREYLE yazılır. Yana savrulan cisim: **t = 0,97 s'de 0,62 m** → prompta "leaves the frame edge in one second" olarak iner. | S ile başlayan her fizik kanıtı sahnesi → ÖLÇEN: ⑥ FİZİK cat.1 + cat.7 |
| **D166** | THE LEANING ROOM: ⑥ FİZİK'in PREMISE GATE'i koştu ve **ORTAMI kaydetti ("Earth-normal 1g"), KURALI kaydetmedi** → üç mercek filmin novum'unu 🔴 BLOCKER saydı | SPEC'in PREMISE REGISTER satırı ortamı değil **KURALI** yazar: *"ağırlık yalnız dönmeden gelir · dönme ekseni boyunca ağırlık YOKTUR · yönü X · değeri Y m/s²"* — üç cümle, üç sayı. | SPEC C bloğu · 25/25 promptun PHYSICS satırı → ÖLÇEN: ⑥ FİZİK STEP 0 |
| **D183** | THE OPEN CIRCUIT: novum'un SINIR cümlesi ("boşalma tek, ince, düz, sönümlü") yazılıydı, ekranda kalın dallanan şimşek çıktı | Novumun **SINIR CÜMLESİ** ayrı bir satır olarak yazılır ve neyin İMKÂNSIZ olduğunu söyler: *eksen boyunca hiçbir cisim ağırlık kazanmaz; eksene dik her cisim kazanır.* | SPEC C · 04_UYARI 🔴 satırı → ÖLÇEN: ⑥ FİZİK cat.1 |
| **D192** | THE OPEN CIRCUIT: filmin 1 numaralı riski **TARİF kilidiyle** korundu ve doruk yanlış üretildi | Filmin 1 numaralı riski (dönme yönü) **SAYIYLA** kilitlenir: RPM · °/s · bir tam turun SÜRESİ · yıldız alanının kadrajı geçme süresi. Tarif kilidi yedek, sayı kilidi asıl. | PLAN sayısal kilitler · SPEC C → ÖLÇEN: ⑥ FİZİK cat.6-7 |
| **D193** | THE OPEN CIRCUIT: ışık takvimi yazıldı, ölçülmedi; sönen şeritler aynı klibin sonunda geri yandı | §3.7'nin bedava kazancı **YAZIYA GEÇER**: dönme eksenine paralel kaynak dönmeyle değişmez → **IŞIK TAKVİMİ YAPISAL SABİTTİR**, 25 sahnede anahtar ışık yönü DEĞİŞMEZ ve bu SPEC'e sayıyla (saat konumu) yazılır. | 25/25 LIGHTING satırı → ÖLÇEN: ⑪ IŞIK cat.1 + ⑪ÖLÇ IŞIK TAKVİMİ İZİ |
| **D23** | Sıfır-g katılığı dersi — süzülen beden rijit çıkıyor | ⛔ **BU ORTAMDA TETİKLENEMEZ**: §3.7'de hiçbir kare sıfır-g değil. Ders ELENİR ve elendiği PLAN'a yazılır (gerekmediğini yazmak da kapının parçasıdır). | — → ÖLÇEN: yok (elenmiş) |
| **D59** | THE HOLDING FIELD: "hiçbir şey yükselmez" kuralı 28 promptun 28'inde yasak olarak yazıldı ve TUTMADI; kök neden pozitif betimlemedeki isim seçimiydi (`hang/suspended/floating` × 24) | `float · hang · hover · weightless · drift` kökleri gövdede **HİÇ** geçmez; yalnız negatif blokta. Ağırlığın azaldığı an **pozitif tarifle** yazılır: *"the step takes longer to come down than it should"*. | eksene yaklaşan her sahne → ÖLÇEN: PK yasak kelime + ⑥ FİZİK cat.1 |
| **D30 · D143** | Parçacık yerçekimi kilidi + toz şelalesi: SAYISIZ pozitif cümle perde üretiyor | Zerre **SAYISI + HIZI** yazılır: *"no more than a few dozen separate points, each falling at about half a metre per second; the far rail stays visible through them"*. Zerreler tek tek sayılamıyorsa RET. | zerrenin yönü taşıdığı sahneler → ÖLÇEN: ⑥ FİZİK cat.5 + ① KARE Parçacık |
| **D39** | `swirl` → toz sıvı gibi akıyor | `swirl · flow · stream · curl` YOK. Vakumda zerre **doğrusal** gider: *"straight lines, no curl"*. | aynı sahneler → ÖLÇEN: ⑥ FİZİK cat.5 |
| **D26** | Halat fiziği: gergin halat düz, katı cisim çarpışmasına uyar | Halat/kordon **gergin ve DÜZ**; duvardan/korkuluktan geçmez; **nerede bittiği** her promptta yazılı. | halatın göründüğü her sahne → ÖLÇEN: ② DEVAMLILIK cat.6 + ⑥ FİZİK cat.3 |
| **D172** | THE LEANING ROOM: taşıyıcının kordonu **ayrı bir çekme halatına döndü**; sekiz merceğin sekizi filmi "halat çekerek manzarayı değiştiren kadın" diye okudu | Kordon **lambada/askıda BİTER** ve **el ona ULAŞMAZ**: *"the cord ends at the bracket; her hands stay on the rail and never reach it"*. Asılı duran şey ÇEKMEYE davet eder — davet PROMPTLA kapatılır. | halatın göründüğü her sahne → ÖLÇEN: ⑦ AKSİYON cat.4 (temas okunabilirliği) |

### 1b · SAYAÇ — bu filmin adı ve en büyük riski

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D50 · D78** | THE TIDAL HUNT: sayaç ekrana HİÇ çıkmadı, filmin omurgası kayboldu. "Sayacı çevreye bağla" çözümü ÜÇ kez uygulandı, ÜÇÜNDE DE okunmadı; 13 filmin 11'inde sayaç `N/A` | Sayaç **METİN OLMAZ**; dünyada okunur. Ve **tek uçlu sayaç okunmuyor** → her sayaç karesinde **ölçeğin İKİ UCU birden** görünür. | her sayaç sahnesi → ÖLÇEN: ② DEVAMLILIK cat.7 (Sayaç) |
| **Third Dune 10/10** | Deponun ÇALIŞAN tek çevresel sayacı: *"sayaç ufku kaplayan bir DUVAR — ölçeğin iki ucu her karede birlikte görünüyor"* ve ilerleme MONOTONİK okundu | Bu filmin sayacı aynı kalıpta kurulur: **başlangıç işareti kadrajda KALIR**, şimdiki değer onun yanında okunur. İki uç aynı karede. | 25/25 → ÖLÇEN: ② DEVAMLILIK cat.7 |
| **T2 verdict** | ⛔ **SAYAÇ TERSİNMESİ diğer bütün skorları EZER: geri giden sayaç bir devamlılık kayması değil, ÖNERMENİN ÇÖKÜŞÜDÜR** | 25 sahnenin sayaç değerleri **MONOTONİK** ve `03_SAHNE_SIRALAMASI`'nda **sayı sayı** yazılı olur. Geri giden tek bir kare = film üretilmez. | 25/25 → ÖLÇEN: ② DEVAMLILIK cat.7 · İPTAL KAPISI |
| **D134** | THE ROSE COAT: rapor `no counter present` yazdı; filmde ÜÇ metinsiz sayaç vardı, biri filmin ANA MEKANİZMASIYDI | Rapor "sayaç yok" derse bu **ölçüm boşluğudur**, sayaç yokluğu değil — bulgu FLAGS'e taşınır ve KAREYLE kapanır. | QA sonrası → ÖLÇEN: ② + ⑪ÖLÇ kare çıkarma |
| **D163** | THE OPEN CIRCUIT: 25/25 sahne insanlı → insan şeridi SABİT (`111…`) ve **SIRA eksenini ölçemez**; S2↔S3 yer değiştirmesini şerit göremedi | Bu film de tek karakterli → şerit ölçmeyecek. Sıra ekseninin ÜÇÜNCÜ çapası kurulur: **her sahnenin sayaç değeri SPEC'e yazılır ve sıra ondan okunur.** | SPEC B → ÖLÇEN: ⑪ÖLÇ kesme ızgarası + ② cat.7 |
| **D154** | Tekrar eden olay bir ENTİTEDİR; "her klip kendi yerçekimini atar" | Sayacın taşıyıcısı **tekrar eden bir olay** → ilk onaylı kare REFERANS olur ve kabul kriterleri **HER sahneye kopyalanır**. | sayaç taşıyıcısının geçtiği her sahne → ÖLÇEN: ② cat.4 + REFERANS PAKETİ KAPI 0 |

### 1c · EFOR VE BEDEN — D169'un tekrarını önleyen blok

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D169** | THE SINKING STAKE: 25 sahnelik bir FİZİKSEL İŞ filminde zorlanma sözlüğü **1 sahnede** göründü; ⑧ EFOR **1,6/10 "NOBODY PAYS"** — 4 efor olayının 4'ünde de `STRAIN SHOWN: none` | Her efor sahnesinin TIMELINE satırında **EN AZ İKİ beden kanalı**: kavrama titremesi · önkol/omuz yüklenmesi · nefes ritmi · duruş kayması. Kanal sayısı SPEC'e yazılır. | efor geçen her sahne → ÖLÇEN: ⑧ EFOR cat.1-2-6 |
| **⑧ EFOR rubriği** | ⛔ **DÜŞÜK YERÇEKİMİ DÜŞÜK EFOR DEĞİLDİR: ağırlık azalır, KÜTLE ve ATALET AZALMAZ. "Düşük g'de kolay olur" mazereti BULGUDUR** | Ağırlığın azaldığı yerde **atalet** yazılır: cisim yavaş kalkar ama **durdurulması aynı derecede zordur**; başlatmak kolay, DURDURMAK zor. | her taşıma/itme/tutma sahnesi → ÖLÇEN: ⑧ EFOR cat.4 |
| **⑧ pattern ⑭** | Ters hata da cezalanır: **sebepsiz gelen yorgunluk, ödenmeyen fatura kadar sahtedir** | Efor eğrisi (COST CURVE, sahne başına 0-9) SPEC'e yazılır ve **her DÜŞÜŞ gerekçelenir** (dinlenme · yardım · yükün bırakılması). | SPEC C → ÖLÇEN: ⑧ EFOR cat.9 |
| **D175** | THE UPWARD FALL: `the forearm tendons stand out through the glove` cümlesi **çıplak deri** ürettirdi (195-198 s, dört kare) | Zorlanma **ELDİVEN YÜZEYİNE** yazılır, deriye değil: *"the glove's knuckle ridges deepen; the cuff seam pulls tight"*. Çıplak-deri negatifi **üç bölgeli** yazılır (yaka üstü · el · bilek). | efor geçen her sahne → ÖLÇEN: ① KARE Karakter + ② cat.2 |
| **D90** | Milimetrik olay üretilmez: sayısal kilit olayı güvenli yaparken GÖRÜNMEZ de yapıyor | Ölçülebilir her olayın kadrajında **ölçüm kenarı** bulunur (korkuluk parmaklığı, güverte dikişi) ve olayın büyüklüğü o kenara göre okunur. | fizik kanıtı sahneleri → ÖLÇEN: ⑥ FİZİK cat.6 |
| **D179** | Kaydın kuralı: imaj promptu **t=0**'dır; değişim ≥1/8 kısa kenar | Değişimi taşıyan sahnede imaj promptu **başlangıç durumunu** yazar; değişim video promptunda ve **kısa kenarın ≥1/8'i** kadar yer kaplar. Bedel sahnesi ASLA en geniş kurulumda yazılmaz. | doruk · bedel · sayaç sahneleri → ÖLÇEN: ① KARE Kare Çapası |

### 1d · METİN · KİMLİK · EKİPMAN

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D138** | Depodaki filmlerin TAMAMI metin yasağını kısaltıp ÖZNESİNİ değiştirdi ("suit carries no lettering" kostümü korur, ZEMİNİ korumaz); bir filmde model çatlağın iç yayına **"11 metres" + gradasyon çentiği** yazdı ve altı mercek görmedi | Metin yasağı **KAPSAMLI** yazılır ve araya kelime SOKULMAZ: *"No readable text, digits, letters or symbols on any display, surface, patch or sign … nothing in this world has been measured, labelled or marked out by anyone."* | 25/25 → ÖLÇEN: PK metin yasağı KAPSAM denetimi + ① KARE Negatif |
| **D138b** | Ölçü prompt gövdesinde durmaz: yüzey işaretine bitişik yazılan ölçü, o işaretin ÜSTÜNE basılan ETİKET olarak çizilebiliyor | Ölçüler **SPEC'in kilit listesinde** yaşar; gövde NESNE GÖRELİ ölçek yazar (*"about four body-lengths along the deck"*). | 25/25 → ÖLÇEN: PK + ① KARE |
| **D34 · D45 · D155** | Karakter özel adı → jenerik halüsinasyonu · prompt iskeleti ekrana sızıyor · **"Wear state: PHASE 1" etiketi GİYSİYE BASILDI** | Prompt gövdesinde **hiçbir iç etiket** (faz adı, kilit adı, sahne adı) ve **karakterin adı** geçmez. Köşeli parantez etiketi ve "CAMERA:" başlıklı sayı-harf satırı yasak. | 25/25 → ÖLÇEN: PK + ① KARE |
| **D70 · D72** | Ekran metni 0,0 sn kilidi **on üç vakada** kurguda çiğnendi; kuyruk kartı klip zincirine karıştı | Kurgu kapısı: **klip sayısı 25 · süre 249,0 ± 2 s · ekran metni 0,0 sn (kart DÂHİL)**. Kart varsa teslim reddedilir. | KURGU → ÖLÇEN: ⑪ÖLÇ freezedetect + son kare |
| **D79 · D139** | Bible'ın olumsuz kostüm kilidi negatif çekirdeğe girmedikçe tutmuyor; **kamera arkaya geçtiği tek sahnede** altın sırt ünitesi doğdu ve 10 saniye kaldı | Sırt **POZİTİF YÜZEY** olarak tarif edilir: *"one continuous smooth panel from collar to hip, unbroken, carrying nothing"*. Kurulum azimutu arkadan/tepeden ise bu cümle o sahnede ZORUNLU. | arka/tepe azimutlu her sahne → ÖLÇEN: ② DEVAMLILIK cat.4 |
| **D95 · D146** | Renksiz + yansımasız + çerçevesiz vizör ekranda "vizör YOK"tan ayırt edilemiyor; "seamless/bubble/dome" kask geometrisini serbest bırakıyor | Vizör **ÖLÇÜLÜ ve ÇERÇEVELİ**: düz ön pencere, görünür metal çerçeve, ölçüsü Character Bible'da. `seamless · bubble · dome` YOK. | 25/25 → ÖLÇEN: ② cat.4 + ① KARE Karakter |
| **D37 · D57 · D84** | Ekipman durum geçişi ve yıpranma **sayısal takvimle bile** tutmuyor (Third Dune: 3 kademeli toz takvimi vardı, 2:29 kumlu suit 2:40'ta tertemiz) | ⛔ **YIPRANMA BU FİLMDE SAYAÇ OLARAK KULLANILMAZ.** Ekipman durumu 25/25 sahnede DEĞİŞMEZ; tek istisna yoksa "durum değişimi 0 kare" yazılır. | 25/25 → ÖLÇEN: ② cat.3-4 |
| **D69 · D77** | Klon sıcak noktası ÜÇ filmde de aynı yerde: **araca biniş / araçtan iniş / eşikten geçiş**. Karşı kanıt: bu hareketi PLANDA HİÇ AÇMAYAN iki film klonsuz çıktı | ⛔ **Biniş · iniş · eşikten geçiş hareketi KADRAJA ALINMAZ** (0 sahne). Geçiş sahne SINIRINDA olur, kadrajda değil. | sahne haritası → ÖLÇEN: ② cat.1 (Kimlik) |
| **Red defteri #15** | Tek kişide üst üste **yedi kimlik özniteliği** (kesin boy cm · gövde · ten · saç rengi · saç biçimi · yüz işareti · yaş) 25 promptta tekrarlanınca sınıflandırıcı "belirli bir gerçek kişiyi tarif ederek isteme" kalıbı sandı ve REDDETTİ | Kimlik yığını **prompt gövdesinden çıkar**: kesin boy → göreli boy · ten/saç rengi ve yaş → PLAN ve referans paketi. Prompta yalnız **siluet** iner. Milliyet YAZILMAZ. | 25/25 → ÖLÇEN: PK ⑯ politika sözlüğü |

### 1e · KAMERA · IŞIK · KADRAJ

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D1 · D68** | Kesme, deponun 8/8 filminde tekrarlayan en dirençli hatası; kesme promptun İÇİNDE tutmadı — planlı kesme çıkmadı, plansız kesme sızdı | 25/25 **tek kesintisiz çekim**; kesme yalnız klip ARALARINDA. `cut to · then we see · montage` YOK. | 25/25 → ÖLÇEN: ① KARE Kamera + ⑪ÖLÇ kesme ızgarası |
| **D104** | Işık mıknatısı: kadrajda TEK baskın kaynak varken model hareketli özneyi ona DÖNDÜRÜYOR — dört kanal yazılıyken bile iki kez battı; kaçış basamağı kamerayı HEDEFE taşımak | Yön çatışması riski olan sahnelerde dört kanal birden: hedef-dilim + omuz hattı + **ışığa göre poz** + yön negatifi. İki yenilgiden sonra kamera hedefe taşınır. | yönlü hareket sahneleri → ÖLÇEN: ⑨ KADRAJ cat.7 + ⑪ IŞIK cat.1 |
| **D145** | Alçak açı = boş üst alan = model DOLDURUR (düz ovadaki gemi, kanyon duvarlarıyla çıktı) | Alçak açılı her kadrajda **HORIZON LOCK** + *"above the rail there is only the star field"* + kadrajdaki **en büyük arka plan nesnesi** adlandırılır. | alçak açılı sahneler → ÖLÇEN: ⑤ ARKA PLAN cat.4 + cat.8 |
| **D126** | ⑤ ARKA PLAN merceği altı sahnenin altısına "black space, star field" yazdı; kadrajın alt üçte birini kaplayan GEZEGENİ görmedi | Her sahne çalışmasında **"kadrajdaki en büyük arka plan nesnesi"** satırı doldurulur. | 25/25 → ÖLÇEN: ⑤ ARKA PLAN cat.4 |
| **D29 · D33** | `glowing/ethereal/radiant/shimmering` → bloom · `cinematic lighting` → mumsu cilt | Bu sözcükler HİÇ geçmez; parlaklık **highlight roll-off** diliyle yazılır: *"highlights roll off smoothly and retain texture instead of clipping to flat white"*. | 25/25 → ÖLÇEN: ① KARE Işık + PK yasak kelime |
| **D128** | THE LEANING ROOM: "düz pirinç el çarkı" arketipine çöktü (parmaklıklı gemi dümeni) — **malzeme/nesne tarifi en yakın eğitim nesnesine yuvarlanır** | Sayaç taşıyıcısı ve halka donanımı **ayırt edici** tarif edilir; arketipe yakın hiçbir nesne jenerik adıyla bırakılmaz. | taşıyıcının geçtiği sahneler → ÖLÇEN: ② cat.10 (dünya propu) |
| **D153 · D59** | THE OPEN CIRCUIT denetimi: `fabric` 17× · `cloth` 24× — model onları kumaş sanıp DALGALANDIRIR | `fabric · cloth` YOK; *"woven webbing band"* gibi ayırt edici karşılık kullanılır. | 25/25 → ÖLÇEN: PK yasak kelime |
| **§16.2 ölçek yayı** | Overview'un gücü, doruğun YAKIN çekiminden sonra ANİDEN geniş açıya dönmesinden gelir; ölçek yayı olmadan Overview sadece MANZARA olur | Ölçek yayı: baş geniş/derin odak → orta → doruk yakın/sığ → **Overview ÇOK GENİŞ** → final geniş held frame. Overview TAM BİR ADET. | sahne haritası → ÖLÇEN: ⑨ KADRAJ cat.6 |
| **§9 Super 35** | Aşırı sığ alan derinliği, karakterin karenin 1/12'si olduğu ve arkadaki yapının OKUNMASI gereken kadrajda anlatıyı yok eder; YouTube kodlayıcısı geniş bokeh'i çamurlu kodluyor | `Super 35 field of view` varsayılan; large format yalnız kapalı/kokpit yakın çekiminde. | 25/25 → ÖLÇEN: ① KARE Kamera |
| **§11 lens** | Vakumda anamorfik YATAY PARLAMA hem yasak hem fiziksel olarak yanlış | `spherical lens rendering, circular bokeh, no lens flare`. Basınçlı iç hacim sahnesi varsa lens satırı orada AYRI yazılır. | 25/25 → ÖLÇEN: ① KARE Kamera |

### 1f · YAPI · ANLATI · TESLİM

| ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|---|---|---|---|
| **D157** | THE PAYLOAD: novum taşıyıcısı **tek kare testini kendisi geçmiyordu** — bir el genişliğinde bant, 40 s arayla iki sahnede, aynı promptta RAKİP bir olayla (düşen toz) birlikte; hiçbir mercek anmadı | Novum taşıyıcısı: kadrajın **≥1/10'u** · değişim **TEK klip içinde** · aynı karede **RAKİP OLAY YOK** · TEK KARE cümlesi taşıyıcının **ADINI** içerir. | novum sahneleri → ÖLÇEN: ④ HİKAYE Önerme + ① KARE Kare Çapası |
| **D158** | THE PAYLOAD: 24 sahnede kahramanın denediği ve TUTMAYAN hiçbir şey yok; bedelden sonra 13 sahne 0 seçim — **tema edilgenliği SAKLAR** | Sahne haritasına **EN AZ BİR BAŞARISIZ DENEME** (ilk yarı) ve **bedelden sonra EN AZ BİR SEÇİM** yazılır. | sahne haritası → ÖLÇEN: ④ HİKAYE Karakter + ⑩ OYUNCULUK cat.6 |
| **§9.1 etkinlik** | Üç ölçülen filmde de Karakter **4/10** — yapısal. Kamera-taşıyıcı testi: "bu karakteri drone ile değiştirsem ne kaybederim?" | Üç etkinlik çapası ZORUNLU: **TERCİH** (bakış→tereddüt→hareket) · **TEPKİ** (her olayın karşısında bedensel cevap prompta yazılı) · **BAŞLANGIÇ AMACI** (ilk 3 sn'de nereye gittiği görünür). | S00 · her olay sahnesi → ÖLÇEN: ⑩ OYUNCULUK cat.3-6 |
| **D141** | Final vuruş kanıtı: **tek karede BULUNAN ya da BULUNMAYAN, SAYILABİLİR ve ADI KONABİLİR** bir nesne + saniyesi + kaç tane. LEANING ROOM'da "iki ezik" vardı ve dört mercek anmadı | SPEC B bloğuna FİNAL VURUŞ KANITI: nesne · saniye · adet. Sayılamayan kanıt yazılmaz. | S24 → ÖLÇEN: ④ HİKAYE Final + ⑨ KADRAJ cat.3 |
| **D168** | THE SINKING STAKE: üretilen malzeme planın ilk ~%60'ı; MERKEZÎ SEÇİM · DORUK · TWIST hiç üretilmedi ve eksik 11 sahne ARDIŞIK, filmin SONUYDU | ÜRETİM SIRASI: **referans paketi → DORUK → merkezî seçim → kapanış imajı → S0 → kalanı.** PLAN'a yazılır ve üretim koşu tablosu operatörün eline sırayla verilir. | PLAN → ÖLÇEN: ⑪ÖLÇ klip sayımı + ①.9 TESLİM KAPISI [D188] |
| **D188** | THE OPEN CIRCUIT: plan 25 sahne, makarada 23 klip → parti geçersiz; eksik iki sahnenin biri filmin DORUĞUYDU ve ⑫ ona "peak 9/10" verdi | TESLİM KAPISI: **plan sahne sayısı = makara klip sayısı**, aksi hâlde hiçbir mercek koşulmaz. | teslim → ÖLÇEN: ⑪ÖLÇ + rapor_kontrol `--olcum-sahne` |
| **D156** | THE PAYLOAD: **planın "VAR" dediği her şey geldi, "SIFIR" dediği her şey düştü** — sıfırı kimse ölçmüyor | Her SIFIR kilidi SPEC'te **ayrı ölçüm satırı** olur: replik 0 · ekran metni 0,0 sn · insan sayısı 1 · sessizlik penceresi n saniye · kesme 0. | SPEC B/E → ÖLÇEN: ⑪ÖLÇ + ③ SES + ① KARE |
| **D122** | Replik zamanları ve doruk saati HESAPLANMAZ, HESAPLATILIR | Zaman kodları formülle üretilir: `t(S_n) = 9 + (n−1) × 10`. Doruk başlangıcı = 9 + (doruk−1) × 10. Yazılan her kayıt formülle doğrulanır. | SPEC B → ÖLÇEN: rapor_kontrol hizalama |
| **D74** | Kayıtsız kapı, koşulmamış kapıdır | Her bilinçli sapma PLAN'a **tek satır gerekçe** ile yazılır: sabit ASL ızgarası · referans paketi kararı · viral ara sayısı. | PLAN → ÖLÇEN: PK ⑩ tema/sapma satırı |
| **D117 · D129 · D165** | SPEC planın İÇİNDE olunca dokuz filmde bir kez bile koşulmadı; QA paketi olmayınca operatörün elinde çıplak rubrik kalıyor ve **mod V** koşuyor (SPEC hazırken mod V koşulan film sayısı 16) | SPEC **AYRI DOSYA** + `rubrik_paketle.sh` SPEC yazılır yazılmaz koşulur; QA paketi klasörü olmadan film "yazımı tamam" değildir. | 9b/9c → ÖLÇEN: — (süreç kapısı) |
| **D142** | Bir SPEC'in kamera kapısı KURULU OLMAYAN bir filtreye yazılmıştı ve sessizce hiç koşmadı | E bloğundaki her makine kapısı **kuru koşuyla** doğrulanır; her kapı üç satır taşır: KOMUT · DOĞRULANDI (ffmpeg sürümü·tarih) · İKAME. | SPEC E → ÖLÇEN: kendisi |
| **D180** | Planlı HARD MUTE teslimde hiç uygulanmadı (3. vaka, ⛔ ÇALIŞMIYOR) | Sessizlik penceresi SPEC'e **saniye aralığıyla** yazılır ve `silencedetect` ile ölçülür. | SPEC E → ÖLÇEN: ⑪ÖLÇ silencedetect |
| **D150 · D177** | Üretici filigranı 225/225 ve 230/230 saniyede duruyordu; sekiz ve on iki merceğin HİÇBİRİ görmedi | Teslim öncesi **köşe testi** koşulur; filigranlı master master değildir. | teslim → ÖLÇEN: ⑪ÖLÇ köşe testi |
| **D100 · D101** | Kurgu kapısı ÜÇ BİRİM sayar (klip · çekim · sahne); süre tek başına ALDATIR; değişken süre varsa KIRPMA BÜTÇESİ zorunlu | Sabit 10 s ızgara → kırpma bütçesi yalnız hook için (10 → 9 s) ve PLAN'a yazılır. | KURGU → ÖLÇEN: ⑪ÖLÇ |

---

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen beş kayıttan (TUR 5). ⛔ "skor düşüktü" yazılmaz; **hangi kare,
> hangi ölçüm, hangi sebep** yazılır — tekrar etmemesi için.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE OPEN CIRCUIT | ⑪ÖLÇ | **İki sahne makarada YOK (S17 · S22); S22 filmin DORUĞU ve İPTAL KAPISI.** Kanıt: yuva eşlemesi + iki repliğin hiçbir raporda geçmemesi | Üretim sırası doruktan başlar [D168]; teslimde `plan sahne = makara klip` kapısı koşar [D188]; her sahnenin ayırt edici görsel çapası SPEC'e yazılır |
| THE OPEN CIRCUIT | ⑫ HOOK | **Var olmayan doruğa "peak placement 9/10 — lands perfectly" verildi**; 3:40'ta izlenen sahne S24'tü | ⑨-⑫ mercekleri **mod V'de KOŞULMAZ** [D190]; paket `PAKET_1..12` ile mod D |
| THE OPEN CIRCUIT | ⑪ÖLÇ | **S2 ↔ S3 yer değiştirmiş; insan şeridi göremedi** (25/25 insanlı → şerit sabit) | Sıra ekseni sayaç değerinden okunur; SPEC B'ye sahne başına sayaç değeri yazılır |
| THE OPEN CIRCUIT | ⑪ÖLÇ | **Filigran 230/230 saniyede · kart 5 s · −16,6 LUFS / 0,0 dBFS · planlı 2 s sessizlik hiç uygulanmamış** — 0/12 mercek gördü | ⑪ ölçüm kapısı teslimden ÖNCE; dört kusur ayrı ayrı SPEC E'de kapı olur |
| THE OPEN CIRCUIT | ⑥ FİZİK | **Doruk boşalması ŞİMŞEK üretildi** (kalın, dallanan) — her promptun NEGATIVE'i "no lightning bolt" diyordu; ⑥ ölçtü, **yönünü ters yazdı ve 10/10 verdi** | Novumun sınır cümlesi + SAYI kilidi [D183 · D192]; mercek raporuna değil KAREYE bakılır |
| THE OPEN CIRCUIT | ⑪ IŞIK | **Işık takvimi geri yandı** — S19'da sönen şeritler aynı klibin sonunda geri geldi (YAVG 183:58,8 → 189:47,5) | Işık takvimi YAPISAL SABİT ilan edilir ve `olcum_kapisi.sh` IŞIK TAKVİMİ İZİ ile ölçülür [D193] |
| THE LEANING ROOM | ①②⑤⑥ | **Kordon lambada bitmiyor, konsola iniyor ve elde** → 8/8 mercek filmi "halat çeken kadın" diye okudu | Halatın BİTTİĞİ yer ve elin ona ULAŞMADIĞI her promptta yazılı [D172] |
| THE LEANING ROOM | kare | **Novumun YÖNÜ ters** — plan SCREEN-RIGHT, ekran SCREEN-LEFT | Yön adı konmuş nesneye bağlanır + ikinci gövdeyle teyit [D174] |
| THE LEANING ROOM | ①③⑥ | **Üç mercek filmin novum'unu 🔴 BLOCKER saydı**; ⑥'nın PREMISE REGISTER'ı ortamı yazdı, kuralı değil | PREMISE REGISTER kuralı yazar (üç cümle, üç sayı) [D166] |
| THE LEANING ROOM | 8/8 | **Sekiz mercek 24 fps varsaydı, dosya 30 fps** → bütün süre ve g hesapları %25 kaymış | ⑪ ölçüm kapısı fps'i yazar ve SPEC künyesine girer |
| THE LEANING ROOM | ⑤ çapraz | **Çoğunluk (4 mercek) yanıldı, tek başına ① KARE haklıydı** [D173] | Uyuşma doğrulama sayılmaz; hakem ÖLÇÜMDÜR |
| THE PAYLOAD | ①②③④⑥ | **Plan "replik 0" dedi, teslimde 4 replik var; "ekran metni 0" dedi, kart + "PHASE 1" + "EVA" geldi; "insan 1" dedi, 1:40'ta klon var** — planın SIFIRLARI düştü | Her SIFIR kilidi SPEC'te ayrı ölçüm satırı [D156]; iç etiket gövdeye girmez [D155]; biniş/iniş kadraja alınmaz [D69] |
| THE PAYLOAD | ②④ | **Novum taşıyıcısı (amortisör bandı) hiçbir mercek tarafından anılmadı**; iki taşıyıcı sahne "aynı olay iki kez" sayılıp kesme listesine yazıldı | Taşıyıcı ≥1/10 kadraj · rakip olay yok · TEK KARE cümlesi taşıyıcının adını içerir [D157] |
| THE PAYLOAD | ④ | **Karakter 2 · Yay 2 · Tema 2 · "no peak located" · "shareable moment: none"** — sahip de "hikayesi berbattı" dedi | Fatura ikiye ayrılır (üretimin kaybettirdiği ↔ planın kusuru); plan tarafına başarısız deneme + ikinci yarıya seçim eklenir [D158] |
| THE IRON SLOPE | ⑥ FİZİK | **TWO GRAVITIES** — serbest parça sabit ~0,15 m/s süzülüyor, kilit 3. saniyede 9,7 m istiyordu → novum ekrana GELMEDİ | Hareket süreyle yazılır [D127]; §3.7'nin iki farklı yönlü ağırlığı SPEC'te "tasarımdır, iki değer de kilitli" satırıyla ilan edilir |
| THE IRON SLOPE | ③ SES | **"S4 tamamen dijital sessizlik" — silencedetect SIFIR sonuç, S4 −19,7…−22,8 dB → RAPOR UYDURDU** [D125] | Ses bulgusu ölçülmeden kabul edilmez; SPEC E'ye silencedetect + RMS kapıları |
| THE IRON SLOPE | 6/6 | **Altı raporun altısı AYNI ve AYNI ÖLÇÜDE YANLIŞ kesme ızgarasını verdi** (gerçek ızgara düzgün 10 s) → tek raporun altı kopyası [D110] | Her mercek TEMİZ OTURUMDA koşulur; ızgara ⑪ÖLÇ'ten okunur |
| THE IRON SLOPE | ① KARE | **Kamera 10/10 verildi; ölçüm S2'de kamera kaymasını gösteriyor** — lockoff 6/6 değildi | Lockoff kilidi ⑨ KADRAJ cat.2 ile ölçülür; ⑪ÖLÇ kamera sabitliği kapısı yazılır |
| THE IRON SLOPE | ⑤ ARKA PLAN | **Altı sahnenin altısına "black space, star field" yazıldı; S2'de kadrajın alt üçte birini GEZEGEN kaplıyordu ve 12/12 promptta yasaklıydı** | Her sahne çalışmasına "en büyük arka plan nesnesi" satırı [D126] |
| THE SINKING STAKE | ⑧ EFOR | **1,6/10 "NOBODY PAYS"** — 4 efor olayının 4'ünde `STRAIN SHOWN: none`; 25 sahnelik fiziksel iş filminde zorlanma 1 sahnede | Her efor sahnesinde ≥2 beden kanalı, TIMELINE satırında, eldiven yüzeyinde [D169 · D175] |
| THE SINKING STAKE | ①②④⑥⑦ | **Dört mercek filmin KURALINI (kazık kısalıyor) en büyük kusuru olarak puanladı**; ⑥'nın PREMISE REGISTER'ı boştu | Sayacın DEĞİŞTİĞİ PREMISE REGISTER'da ilan edilir [D166] |
| THE SINKING STAKE | ② DEVAMLILIK | **Göğüs paketi tasarımı S13'te değişti** — referans paketi tam bunu önlemek için yazılmıştı ve HİÇ ÜRETİLMEDİ | Referans paketi KAPI 0; onaysız sayfanın varlığı geçtiği sahne üretilmez [D168] |
| THE SINKING STAKE | ⑤ ARKA PLAN | **S4 ve S10'da ağır dairesel YILDIZ İZLERİ** — sabit kamerada fiziksel olarak imkânsız, saf üretim halüsinasyonu | ⚠️ Bu filmde yıldız alanı YÖN TAŞIYICISI → iz çıkarsa taşıyıcı ölür; "no star trails, individual points" negatifi + ⑤ mercek kapısı |
| THE SINKING STAKE | ⑥ FİZİK | **İki yerçekimi: kar ~1,0 m/s² ↔ döküntü ~0,2 m/s²** — "her klip kendi yerçekimini atar" [D154]; panzehir uygulanmamıştı çünkü referans zinciri kurulmadı | İlk onaylı kare referans olur; kabul kriterleri HER sahneye kopyalanır |

---

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| **PK** | **Kimlik yığını** — tek kişide kesin boy (cm) + ten rengi + saç rengi + saç biçimi + yüz işareti + yaş, tüm promptlarda tekrarlanınca "belirli bir gerçek kişi" kalıbı okunuyor (vaka 15, OMNI) | ⬜ önerilen (henüz sınanmadı): boy GÖRELİ · ten/saç/yaş plana ve referans paketine · yüz tarifi yalnız yüzün KONU olduğu sahnelerde · ayırt etme yükü GEOMETRİDE | Character Bible'ın 25 promptta tekrarlanan bloğu — **tek karakterli olmak riski yarıya indirir, kaldırmaz** |
| **PK** | **Milliyet ifadesi** — doğrulanmış red tetikleyicisi; hâlâ canlı promptlarda ve kaynağı bir KILAVUZ örneği | milliyet satırı SİLİNİR, yalnız fiziksel tarif kalır (GEÇTİ) | Character Bible — kılavuz örneği körü körüne kopyalanmayacak |
| **PK** | **Yasak listesi tuzağı** — NEGATIVE bloğuna yazılan yasak, yasakladığı kavramı PROMPTUN İÇİNE SOKAR; sınıflandırıcı "no" önekini değil KELİMEYİ okur | yasak SİLİNİR, malzeme TARİF edilir [D123 · D59] (GEÇTİ) | Bu filmde şiddet/tehlike sözlüğü zaten yok; **kontrol edilecek: efor ve zorlanma cümlelerinin yaralanma sözlüğüne kaymaması** |
| **PB** | **Kompozisyon reddi** — kelimeler temizken kadraj reddedildi: yan yana iki ön kol + tepeden makro + yüzsüz izolasyon (YERÇEKİMİ S8) | ① önce sözcük değişti → **YETMEDİ** ② kadraj değişti (ray hizası, nesneler ard arda) → sahne yine de İPTAL | Makro temas/efor kadrajları bu profile yaklaşmayacak; el yakın planları **çevreyle birlikte** kadrajlanacak |
| **YR** | **Yapısal red** — İNSANSIZ sahne + uzun `NEGATIVE:` bloğu + "Exactly 0 human figures" kalıbı; yokluk listesi istek olarak okunamıyor | `NEGATIVE:` tamamen kaldırılır → tek pozitif `Style:` satırına inilir (GEÇTİ, ilk denemede) | **Overview ve kapanış imajı insansızsa** bu profile girer → o sahnelerin negatif bloğu tek satıra indirilir |
| **TK** | **0 BAŞARI deseni** — aynı oturumda hiç geçen prompt yoksa sayı promptu değil ÜRETİM TARAFINI işaret eder | üçüncü yeniden yazımdan ÖNCE 3 satırlık PROB koşulur; prob da hata veriyorsa hesap/oturum tarafı | Üretim gününde geçerli; PLAN'ın üretim koşu tablosuna satır olarak yazılır |
| **MÇ** | **Maskeli çıktı reddi** — üretim GÖRÜNÜR şekilde ilerleyip sonda düşerse teknik değil ÇIKTI reddidir; tekrar denemek işe yaramaz | MOTOR ve İLERLEDİ sütunları **ANINDA** yazılır (dosya oluşmadığı için meta veriden okunamaz) | Üretim günü; red gelirse satır O GÜN açılır |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
⛔ SINIF ÖNCE, ÇÖZÜM SONRA: kelime reddi SÖZLÜKLE çözülür ve her seferinde
   çözüldü; KOMPOZİSYON reddi sözlükle ÇÖZÜLMEZ. Sözcük çözümünü kompozisyon
   reddine uygulamak bu deponun ölçülmüş TEK boşa emeğidir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        47 adet  (1a ortam/novum 12 · 1b sayaç 6 · 1c efor 6 ·
                              1d metin/kimlik 9 · 1e kamera/ışık 10 · 1f yapı 14)
QA ARIZASI:         24 adet  (OPEN CIRCUIT 6 · LEANING ROOM 5 · PAYLOAD 4 ·
                              IRON SLOPE 5 · SINKING STAKE 4)
RED SINIFI:         7 adet   (PK 3 · PB 1 · YR 1 · TK 1 · MÇ 1)

⛔ EN PAHALI ÜÇÜ — 04_UYARI_NOTLARI'nda ⛔ satırı olacak:

  ① SAYAÇ GÖRÜNMEZ KALIR VEYA TERSİNİR
     [D50 · D78 · D134 · T2 verdict] — 13 filmin 11'inde sayaç N/A;
     dört filmde sayaç PLANLIYDI ve ekranda okunmadı. Bu filmin ADI sayaç.
     Ve tersinme, devamlılık kayması değil ÖNERMENİN ÇÖKÜŞÜDÜR.

  ② DÖNME YÖNÜ YUVARLANIR — NOVUM EKRANA GELMEZ
     [D174 · D127 · D166 · D192] — LEANING ROOM'da yön ters çıktı ve
     üç mercek novum'u BLOCKER saydı; IRON SLOPE'ta novum hiç gelmedi
     ve T4 2,6 aldı ("THE ONE THING NOTHING ELSE DOES: none found").

  ③ EFOR FATURASI ÖDENMEZ
     [D169 · D175 · ⑧ rubriği] — SINKING STAKE 1,6/10 "NOBODY PAYS";
     25 sahnelik fiziksel iş filminde zorlanma 1 sahnede göründü.
     Düşük yerçekimi düşük efor DEĞİLDİR: ağırlık azalır, atalet azalmaz.
```

> ⛔ Bu üç satır `04_UYARI_NOTLARI.md`'de sahne numarasıyla ve ölçen
> merceğin adıyla tekrar yazılır [D187]; sahne çalışması açılmadan
> kapanmazlar.
