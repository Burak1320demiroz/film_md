# ⚠️ THE_COUNTED_TURN — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.
> ⛔ Her satır ayrıca ONU ÖLÇECEK MERCEĞİN adını taşır [D187].

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | ÖLÇEN | durum |
|:--:|---|---|---|---|---|:--:|
| 1 | **25/25** | D174 · THE LEANING ROOM: plan "yatma 12/12 SCREEN-RIGHT" dedi, ekranda ters çıktı; üç mercek novum'u BLOCKER saydı | **Dönme yönü yuvarlanır** — model ekran-yönü kelimesini okumuyor | Yön İKİ NESNEYE bağlanır ve İKİSİ de her promptta: ① yıldız alanı **korkuluğun üst kenarını** hep aynı uçtan geçer ② güverte dikişi aynı yöne eğilir. Yön cümlesi 25/25 promptta **BİREBİR** aynı kelimelerle. Ekran-yönü kelimesi (left/right) tek başına asla kullanılmaz. | ⑥ FİZİK c.7 · ⑨ KADRAJ c.7 | ✅ kapandı (03 §6 KANAL 2 + iskelet birebir kopya kuralı) |
| 2 | **S0 · S23** | D127 · THE IRON SLOPE: Motion Bible "3. s'de 9,7 m" dedi, ölçüm sabit 0,15 m/s süzülme gösterdi → novum ekrana HİÇ gelmedi, T4 2,6 | **İvme yazılırsa hareket üretilmez** | Hiçbir yere ivme yazılmaz. S0: *"the bolt leaves the palm and is beside the seam within a couple of heartbeats — about a hand-span and a half out from straight down"* · S23: aynı yer, **daha erken**. Sayılar (t = 1,69 s → 1,03 s · sapma 0,52 m sabit) SPEC'in kilit listesinde yaşar, gövdede DEĞİL [D138]. | ⑥ FİZİK c.1+c.7 | ✅ kapandı (03 §6 üçüncü kanıt) |
| 3 | **S2 S5 S14 S16 S23 S24** | D50 · TIDAL HUNT (sayaç ekrana HİÇ çıkmadı) · D78 (üç kez uygulandı, üçünde de okunmadı) · D134 · T2 verdict | **Sayaç görünmez kalır veya TERSİNİR** — tersinme önermenin çöküşüdür | ① Sayaç **ölçeğin İKİ UCUNU** her karede birlikte gösterir (sabit pim + kablo) — Third Dune 10/10 kalıbı. ② İkinci kanal (yıldız süpürme hızı) aynı bilgiyi bağımsız verir [D78 çift kanal]. ③ 25 sahnenin sarkma değeri SPEC'e **sayı sayı** yazılır ve MONOTONİKTİR. ④ Tek bir karede bile geri giderse film üretilmez. | ② DEVAMLILIK c.7 | ✅ kapandı (03 §6) |
| 4 | **S8 S9 S18 S19 S20 S21** | D169 · THE SINKING STAKE: 25 sahnelik fiziksel iş filminde ⑧ EFOR **1,6/10 "NOBODY PAYS"** — 4 efor olayının 4'ünde `STRAIN SHOWN: none` | **Efor faturası ödenmez** | Her efor sahnesinin TIMELINE satırında **EN AZ İKİ beden kanalı**: eldiven boğum sırtlarının derinleşmesi · manşet dikişinin gerilmesi · omuz hattının düşüp DÜŞÜK KALMASI · nefes ritminin ağırlaşması. ⛔ **Düşük yerçekimi düşük efor DEĞİLDİR: ağırlık azalır, ATALET AZALMAZ** — bant yavaş kalkar ama DURDURULMASI aynı derecede zordur. | ⑧ EFOR c.1-2-4-6 | ✅ kapandı |
| 5 | **S8 S9 S18 S19 S21** | D175 · THE UPWARD FALL: `forearm tendons stand out through the glove` cümlesi 195-198 s'de **çıplak deri** ürettirdi | **Zorlanma deriye yazılırsa deri üretilir** | Zorlanma yalnız **ELDİVEN YÜZEYİNE** yazılır. Çıplak-deri negatifi **ÜÇ BÖLGELİ**: yaka üstü · el ve bilek · manşet. Satır sonunda bölünmez, tek cümlede yazılır. | ① KARE Karakter · ② c.2 | ✅ kapandı |
| 6 | **S2 S5 S14 S16 S23** | D172 · THE LEANING ROOM: sarkan kordon **ayrı bir çekme halatına döndü**; 8/8 mercek filmi "halat çeken kadın" diye okudu | **Asılı duran şey ÇEKMEYE davet eder** | Sayaç olarak okunan sarkma **her zaman ARKADA, zaten oturtulmuş açıklıktadır** ve elleri ASLA orada değildir. Her promptta: *"the span ends on the two seated pins; her hands are on the working end, well clear of it."* Çalışılan uç ile ölçülen açıklık **AYNI KAREDE ELLE TEMAS ETMEZ**. | ⑦ AKSİYON c.4 | ✅ kapandı |
| 7 | **S6 S16 S24** | Red defteri vaka 2 (YR) · COLD BURN S8: insansız sahne + uzun `NEGATIVE:` + "Exactly 0 human figures" → **YAPISAL RED** | **İnsansız sahne yapısal red profili** | Bu üç sahnede `NEGATIVE:` bloğu tamamen kaldırılır ve **tek pozitif `Style:` satırına** indirilir (red defterinde bu çözüm İLK denemede GEÇTİ). Boş kadraj VARLIK olarak tarif edilir: *"the deck around it is empty and unlit"* [D59]. | — (üretim kapısı) | ✅ kapandı |
| 8 | **25/25** | Red defteri vaka 15 (PK · OMNI) · THE SINKING STAKE: tek kişide yedi kimlik özniteliği 25 promptta tekrarlanınca "belirli bir gerçek kişi" kalıbı okundu ve REDDEDİLDİ | **Kimlik yığını politika reddi üretir** | Prompt gövdesinde: kesin boy (cm) **YOK** → göreli boy · ten rengi **YOK** · saç rengi/biçimi **YOK** · yaş **YOK** · milliyet **YOK** (doğrulanmış tetikleyici). Bunların hepsi PLAN'da ve RA referans sayfasında yaşar. Gövdeye yalnız **siluet + giysi kesiti** iner; ayırt etme yükü GEOMETRİDEDİR. | PK ⑯ politika sözlüğü | ✅ kapandı (02 §6) |
| 9 | **S20** | Red defteri vaka 13 (PB) · YERÇEKİMİ S8: kelimeler temizken **kadraj** reddedildi (yan yana iki ön kol + tepeden makro + yüzsüz izolasyon) | **Kompozisyon reddi — sözlükle çözülmez** | S20 en ağır çekiştir ama kadrajı **MS (50 mm · 4,0 m · göz hizası)** tutulur, makro değil. Bütün eldiven makrolarında (E) kadrajda **daima korkuluk ya da pim görünür** — çevresiz izolasyon kurulmaz. | — (insan gözü · PROMPT_QA §3) | ✅ kapandı |
| 10 | **S22** | D183 · D192 · THE OPEN CIRCUIT: 1 numaralı risk yalnız SIFATLA korundu, doruk ŞİMŞEK geldi; her promptta "no lightning bolt" yazılıyken | **Doruk sıfatla korunursa model boşluğu doldurur** | S22'nin olayı **temas ve ses**tir, ışık değil: klips pime oturur, çan bir kez vurur ve kuyruk sönerken kesilir. Sayısal kilit: **klips sayısı 2 · çan vuruşu 1 · sessizlik penceresi 2,0 s**. Işık olayı 0 kare — §3.7'de ışık dönmeyle DEĞİŞMEZ, bu sahnede de değişmez. | ⑥ FİZİK · ⑪ IŞIK c.6 | ✅ kapandı |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | ÖLÇEN | durum |
|:--:|---|---|---|---|---|:--:|
| 1 | **S11 S13** | D179 · optik aritmetiği | Üst güvertedeki kablo hattı **50 mm · 24 m'de ~39 px** — sınırda | Okunurluk BOYUTTAN değil **KONTRASTTAN** gelir: koyu dokuma bant ↔ parlak alüminyum güverte. QA_SPEC E bloğuna **KONTRAST KAPISI** yazılır (`signalstats` YMAX−YMIN eşiği · THE UPWARD FALL KAPI ⑦ emsali). | ⑤ ARKA PLAN c.5 · ⑪ IŞIK | 🟡 SPEC'e taşınacak |
| 2 | **S12** | D179 | Omuz üstü kadrajda uzak pimler ~21 px — okunmaz | S12'de okunması gereken şey **pim değil**, kablo hattının kesintisiz ÇİZGİSİ ve güverte eğrisinin yükselmesidir. Prompta pim SAYISI yazılmaz; "the band runs away along the seam and lifts out of frame with the curve" yazılır. | ⑤ ARKA PLAN c.5 | 🟡 |
| 3 | **S6 S11 S13 S16** | D145 · SKYLIGHT S26: alçak açı = boş üst alan = model DOLDURUR (düz ova kanyon duvarıyla çıktı) | Alttan-yukarı ve insansız kadrajlarda model boşluğa yapı ekler | Her birinde **HORIZON LOCK** + kadrajdaki **en büyük arka plan nesnesi ADLANDIRILIR** [D126] + *"beyond the rail there is only the star field; nothing else is built there."* | ⑤ ARKA PLAN c.4+c.8 | 🟡 |
| 4 | **S1 S12 S22 S23** | §3.7 ses kuralı · D83 · THE COLD BURN 20 s dijital sıfır | Çan vuruşunun kuyruğu klip sınırında ölür | Ortam yatağı (suit içi nefes + fan) kurgu boyunca **TEK PARÇA** serilir, klip sınırında kesilmez. Çan kuyruğu sahne İÇİNDE sönümlenir. Teslimden önce sessizlik bölgesi **kulakla** dinlenir. | ③ SES c.6 · ⑪ÖLÇ silencedetect | 🟡 |
| 5 | **S22** | D180 (⛔ ÇALIŞMIYOR · 3. vaka) · THE OPEN CIRCUIT: planlı 2 s HARD MUTE teslime hiç girmedi | Planlı sessizlik uygulanmaz | Sessizlik **video modelinden İSTENMEZ** — KURGUDA uygulanır ve SPEC E bloğuna saniye aralığıyla yazılır: **HARD MUTE 226,0-228,0 s**. `silencedetect` ile ölçülür. | ⑪ÖLÇ silencedetect | 🟡 |
| 6 | **S8 S9 · S18 S19 · S22 S23 S24** | ACI_YAYI §7⑥ | KÜME kurulumlarının kamera metni birebir kopyalanmazsa ⑨ mercek dönüşü göremez | Küme sahnelerinin CAMERA satırı **birebir kopyalanır** + işaret satırı: *"continues the previous clip from its exact last frame — the same position, height and lens as Scene N."* | ⑨ KADRAJ c.5 | 🟡 |
| 7 | **S13** | UZAY_SENARYO §8 · YERÇEKİMİ S68 emsali | Overview'un "karakter 1/20" maddesi iç mekânda uygulanamaz | Karşıtlık **GÖVDE ↔ KAPANAN HALKA** olarak kurulur ve bu sapma PLAN'a tek satır yazılır [D74]. Diğer dört madde birebir: hareketsizlik · sessizlik · geriye bakış · tam bir sahne. | ④ HİKAYE · ⑨ KADRAJ c.6 | 🟡 |
| 8 | **film geneli** | D146 (⛔ ÇALIŞMIYOR · 4 vaka) | Kask/vizör biçimi metinle tutulmuyor; `seamless/bubble/dome` kubbe üretiyor | Vizör **ÖLÇÜLÜ ve GÖRÜNÜR ÇERÇEVELİ DÜZ pencere**; ölçüsü RA sayfasında. `seamless · bubble · dome` 0 geçiş. ⭐ Ayrıca D95: renksiz+yansımasız+çerçevesiz vizör ekranda "vizör yok"tan ayırt edilemiyor → çerçeve OKUNUR olmak zorunda. | ② DEVAMLILIK c.4 | 🟡 |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak | ÖLÇEN |
|---|---|---|---|
| D1 · D68 · 8/8 filmde tekrarlayan en dirençli hata | Model kesme atıyor / plansız kesme sızıyor | 25/25 **tek kesintisiz çekim** · klip içi kesme 0 · `cut to · then we see · montage` 0 geçiş · kesme yalnız klip ARALARINDA | ① KARE Kamera · ⑪ÖLÇ kesme ızgarası |
| D138 (metin yasağının KAPSAMI) | Yasak kısaltılınca öznesi değişiyor; model zemine/yüzeye ölçü yazıyor | Kapsam cümlesi **araya kelime sokulmadan** birebir: *"No readable text, digits, letters or symbols on any display, surface, patch or sign … nothing in this world has been measured, labelled or marked out by anyone."* ⛔ Bu film sayaç filmidir → risk azamidir | PK metin kapsamı · ① KARE |
| D34 · D45 · D155 | Karakterin adı / iç etiket / künye satırı ekrana basılıyor ("PHASE 1" göğse basıldı) | Prompt gövdesinde karakterin adı, köşeli parantez etiketi, "CAMERA:" başlıklı sayı-harf satırı ve hiçbir iç kilit adı geçmez | PK · ① KARE |
| D79 · D139 (5 vaka) | Sırt ünitesi yokluk kilidine rağmen doğuyor; kamera arkaya geçen sahnede | Sırt **POZİTİF YÜZEY**: *"one continuous smooth panel from collar to hip, unbroken, carrying nothing."* S12 (omuz üstü) ve S11/S13 (alttan) bu cümleyi ZORUNLU taşır | ② DEVAMLILIK c.4 |
| D37 · D57 · D84 (Third Dune: 3 kademeli sayısal toz takvimi bile tutmadı) | Ekipman durumu ve yıpranma sahneler arasında kayıyor | ⛔ **Yıpranma bu filmde SAYAÇ OLARAK KULLANILMAZ.** Ekipman durumu 25/25 sahnede DEĞİŞMEZ; SPEC'e "durum değişimi 0 kare" yazılır | ② DEVAMLILIK c.3-4 |
| D69 · D77 (klon sıcak noktası 3 filmde aynı yerde) | Biniş/iniş/eşikten geçiş hareketinde klon doğuyor | ⛔ Biniş · iniş · eşikten geçiş hareketi **0 sahne**; geçiş sahne SINIRINDA olur, kadrajda değil. (Karşı kanıt: bu hareketi planda hiç açmayan iki film klonsuz çıktı) | ② DEVAMLILIK c.1 |
| D29 · D33 · §15 | `glowing/ethereal/radiant/shimmering` bloom · `cinematic lighting` mumsu cilt | Bu sözcükler 0 geçiş; parlaklık **highlight roll-off** diliyle: *"highlights roll off smoothly and retain texture instead of clipping to flat white"* | PK · ① KARE Işık |
| D30 · D39 · D143 | Zerre sayısız yazılırsa perde olur; `swirl` sıvı üretir | §3.7'de toz **0 kare**. Yıldızlar zerre değil sabit noktadır: *"individual separate points, no trails, no streaks"* ⭐ THE SINKING STAKE'te dairesel **yıldız izleri** üretildi ve bu filmde yıldız alanı YÖN TAŞIYICISIDIR — iz çıkarsa taşıyıcı ölür | ⑥ FİZİK c.5 · ⑤ ARKA PLAN c.8 |
| D59 · D123 · D153 | Yasak, yasakladığı kavramı prompta sokar; `fabric/cloth` dalgalanır | `float · hang · hover · weightless · drift` yalnız NEGATIVE'te · `fabric · cloth` 0 geçiş → **"woven webbing band"** · şiddet/yaralanma sözlüğü 0 geçiş ve yasak cümlesi de yazılmaz | PK yasak kelime + ⑯ |
| D104 · KART 9 | Işık mıknatısı özneyi kaynağa döndürür | ⭐ Yapısal panzehir: ışık **dönme eksenine paralel**, yönlü hareketin tamamı **ÇEVRESEL** → kaynak hiçbir sahnede hareketin önünde/arkasında değil. Yine de dört kanal yazılır (hedef-dilim + omuz hattı + ışığa göre poz + yön negatifi) | ⑪ IŞIK c.1 · ⑨ KADRAJ |
| §3.7 coğrafya kuralı · KART 4 | Üst banttaki ikinci güverte modeli oraya İNSAN koymaya çağırır | 25/25 promptta: *"Exactly one human"* + **"no one is standing on it"** (kartın bu ortamdaki zorunlu hâli) | ② DEVAMLILIK c.12 (nicelik+sayı) |
| D154 · THE SINKING STAKE iki yerçekimi | Tekrar eden olay her klipte kendi fiziğini atıyor | Bırakılan cismin ve sarkmanın **İLK ONAYLI KARESİ referans olur**; kabul kriterleri (sapma 0,52 m · yön · süre) **HER sahneye kopyalanır** | ⑥ FİZİK · REFERANS PAKETİ KAPI 0 |
| D150 (⛔ ÇALIŞMIYOR · 6 vaka) · D70/D72 (13 vaka) | Filigran ve kuyruk kartı 12 mercekten geçiyor | Teslimden ÖNCE `olcum_kapisi.sh`: köşe testi · freezedetect · son kare · LUFS. **Filigranlı master master değildir**; ekran metni 0,0 sn (kart DÂHİL) | ⑪ÖLÇ |
| D129 · D165 (⛔ ÇALIŞMIYOR · 3 vaka · 16 film) | SPEC ve paket varken operatör çıplak rubriği yapıştırıyor → mod V | SPEC **ayrı dosya** [D117] + `rubrik_paketle.sh` SPEC yazılır yazılmaz koşulur. ⑨-⑫ mercekleri mod V'de **KOŞULMAZ** [D190] | rapor_kontrol.py |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | 🔴 **VAR** — 25/25 sahnede vizör; ayrıca tekrar eden pim/klips birimi | Vizör **ölçülü + görünür çerçeveli DÜZ pencere**, ölçüsü RA sayfasında; `seamless/bubble/dome` 0 geçiş. Pim+klips **RB sayfası** + sayısal ölçü tablosu. Referans paketi **KAPI 0** — onaysız sayfanın sahnesi üretilmez |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | 🔴 **VAR** — filmin ana nesnesi bir **dokuma bant** | `fabric` ve `cloth` **0 geçiş**; karşılık **"woven webbing band"**. Ayrıca banda "gergin ve düz" fiziği yazılır [D26] — dalgalanma değil GERİLİM |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ✅ **YAPILDI** — sekiz kurulumun sekizi hesaplandı (Super 35, 24,89 mm): A 85/0,7 → 20,5 cm · C 50/4,0 → 1,99 m · G 50/2,5 → 1,24 m · F 50/6,0 → 2,99 m · B 32/14,0 → 10,89 m · E 85/1,2 → 35,1 cm · D 50/3,0 (özne 24 m'de) → 11,9 m · H 35/1,5 → 1,07 m | ⭐ **BİR KURULUM DÜZELTİLDİ:** D önce 32 mm yazılmıştı; üst güvertedeki bant 24 m'de ~24 px kalıyordu → **50 mm**'ye çekildi, ~39 px oldu ve kalan açık `signalstats` KONTRAST KAPISI'na bağlandı (🟡 satır 1) |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | 🟡 **KISMEN** — S11/S13'te üst güverte bandı ~39 px, S12'de uzak pimler ~21 px | S11/S13: okunurluk KONTRASTA bağlandı + SPEC kapısı. S12: pim **okunması gereken nesne değil**; okunan şey kablo hattının kesintisiz ÇİZGİSİ. Prompta pim sayısı yazılmaz |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | ✅ **YOK — ve gerekçesi var:** filmde **tek insan** var; ayırt edilecek ikinci gövde yok. Ayrıca mimari kutup **DISCOVERY** (parlak, temiz metal) → figür koyu / zemin açık, kontrast doğal | Yine de tek renk kanalına yaslanılmıyor: giysi ile güverte arasındaki fark **MALZEME** (mat dokuma ↔ parlak işlenmiş alüminyum), renk değil |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | 🔴 **VAR** — kadrajda büyük bir YAPI (halka) sürekli var → KART 13 | UZAY_USSU'nun **iki ayrı negatif bloğu** (ölçek/maket + yapı) 25/25 prompta girer; ölçek şahidi (insan gövdesi ya da pim aralığı) her geniş kadrajda bulunur; anatomi kartı + mesafe kesir tablosu PLAN'a yazılır |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ✅ **KAPALI** — TEMA satırı ≥3 sahne indeksi taşıyacak: **S3 · S11 · S20 · S24** (nesne · kamera/ışık · kinesik · ifşa) | PLAN'da TEMA satırı bu dört numarayı taşır; `prompt_kontrol` ⑩ tema+sahne indeksi kapısı bunu okur |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ✅ **KAPALI** — BEDEL **S21** (kalça sırası boşalır) ve bedel nesnesi siluet testinden geçiyor: dolu hâli S3/S8'de, boş hâli S21'de kadrajda | B5 dörtlüsü 02_KONSEPT §7'de tam; ⑰ B5 kapısı PLAN'da okuyacak satırı bulacak |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | 🟡 **RİSK VAR** — efor sahnelerinde yaralanma sözlüğüne kayma riski | Yasak cümlesi yazılmaz; **pozitif kilit** yazılır: *"the band comes off the deck by a hand's width and holds there; her hands stay on the working end."* `strain · injury · hurt · wound · danger · trapped · crushed · pain` **0 geçiş** |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | ✅ **YOK — gerekçesi:** filmde politika sözlüğüne giren adlandırılacak bir nesne yok (silah/araç/tehlike ekipmanı 0). Riskli olan **kompozisyon** ekseni ve **kimlik yığını** ekseni, ikisi de 🔴 satır 8-9'da kapatıldı | Yine de her el makrosunda çevre (korkuluk/pim) kadrajda tutulur — çevresiz izolasyon kurulmaz |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ✅ **YOK — gerekçesi: replik 0.** Ama formül YİNE koşuyor: sahne başlangıçları `9 + (n−1) × 10` ile üretildi ve SPEC'in bütün zaman kodları (sessizlik penceresi 226,0-228,0 s dâhil) bu formülden hesaplatıldı | Klip süresi ffprobe ile ölçülünce **bütün kodlar yeniden hesaplanır** [D124] |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | 🔴 **VAR ve filmin merkezinde** — sayaç bir DURUM DEĞİŞİMİDİR | ⛔ **Sayaç değeri klip İÇİNDE değişmez; SINIRDA değişir.** Her sahne sarkmanın TEK bir değerini gösterir; değişim iki sahne ARASINDA okunur. Tek istisna S0 ve S23 (cıvatanın düşüşü) — orası bir HAREKETTİR, nitelik değişimi değil. Klip içi değişim yazılan tek yer S8→S9 ve S18→S19 kümeleridir ve orada da **hareket** değişir, nitelik değil |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | ✅ **KAPALI (yazım kuralı)** — 25 promptun 25'i self-contained; karakter çapa bloğu birebir tekrarlanır, `[BIBLE]` / `[CHARACTER BIBLE]` etiketi 0 geçiş | `prompt_kontrol` çekirdek imzası + etiket denetimi |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | 🟡 **AÇIK — SPEC yazılırken kapanacak** | QA_SPEC E bloğundaki **her kapı kuru koşuyla doğrulanır** ve üç satır taşır: KOMUT · DOĞRULANDI (ffmpeg sürümü·tarih) · İKAME. `vidstabdetect` kurulu değilse kapı YAZILMAZ, ikame konur (THE OPEN CIRCUIT emsali) |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | 🔴 **VAR** — efor filmi, eldiven makroları 5 sahnede | Negatif **ÜÇ BÖLGEYİ** tek cümlede sayar: yaka üstü · el ve bilek · manşet. Satır sonunda bölünmez. Zorlanma yalnız eldiven YÜZEYİNE yazılır |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | ✅ **KAPALI** — 1 numaralı risk (dönme yönü + sayaç) **SAYIYLA** yazıldı: R 12,00 m · T 20,0 → 12,0 s · 3,0 → 5,0 RPM · süpürme 18 → 30 °/s · sapma 0,52 m sabit · düşüş 1,69 → 1,03 s · sarkma 4,46 → 11,12 cm | 02_KONSEPT §5 A5 bloğu + 03 §6 sayaç kanalları; sayılar SPEC kilit listesinde, prompt GÖVDESİNDE değil [D138] |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (10 satır · durum ✅)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (8 satır)
☑ film geneli 14 satır yazıldı, her biri kaynak + mercek taşıyor
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 · "yok" diyen
  dört satır GEREKÇE taşıyor)
☑ ⭐ Bu adımda BİR GERÇEK HATA YAKALANDI ve düzeltildi: D kurulumunun lensi
  32 → 50 mm (üst güverte bandı 24 px → 39 px) — optik aritmetiği tam da bunun
  için var [OPEN CIRCUIT: beş kurulumun beşi tutmuyordu]
→ dördü de ✅ ise 05_SAHNE_CALISMALARI/ açılabilir
```
