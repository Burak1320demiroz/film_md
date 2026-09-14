# ⚠️ THE_DRY_ANCHOR — UYARI NOTLARI

> **Girdi:** `01_QA_DERS_HASADI.md` (ne bozulmuş) × `03_SAHNE_SIRALAMASI.md`
> (bu filmde ne var). **Çıktı:** sahne sahne, ölçülmüş arızaya bağlı uyarı.
>
> ⛔ Bu dosya genel tavsiye taşımaz. Her satır ÜÇ şeyi birden taşır:
> **hangi sahne · hangi ölçülmüş kayıt · ne yapılacak.** Üçünden biri
> yoksa satır yazılmamıştır.
> ⛔ Kaynağı olmayan uyarı yazılmaz — "dikkat edilmeli" bir uyarı değildir.

---

## 1. 🔴 ⛔ SATIRLARI — kapatılmadan prompt yazılmaz

| # | sahne | ölçülmüş kayıt (ders / film / red) | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S0 · S1 · S4 · S9 · S13 | D69 · THE STONE SKY 1:40 (araçtan iniş) · THE STARLESS CIRCLE 2:10 (gemiye biniş) — iki IDENTITY BREAK, ikisi de KLON | Astronotun gemiyle arasındaki geçiş hareketi kadraja girerse klon riski deponun ölçülmüş en yüksek noktasına çıkar. | ⛔ İNİŞ/BİNİŞ HAREKETİ 0 KARE. Astronot filmin başında ZATEN yerdedir ve sonunda da yerdedir; gemiye hiç yaklaşmaz. A kurulumunda figür ile gövde arasında hiçbir karede temas yoktur. ⛔ Kamera gemiden inen/çıkan hiçbir şeyi TAKİP ETMEZ. | ✅ tasarımla kapandı |
| 2 | S0 | D148 · THE THIRD DUNE kalkışı — bacak alevin içinden geçti, şeffaf yazılan alev opak çıktı | İniş klibi bu filmin tek alev sahnesidir ve bacakların hemen yanında geçer. | ⛔ Bacaklar HİÇ HAREKET ETMEZ (katlanma/açılma 0 kare). ⛔ Püskürtü hiçbir karede bir bacakla 2B ÇAKIŞMAZ: alev bacakların ARASINDAN iner ve bacağın arkası her karede görünür kalır. Kalkış sahnesi FİLMDE YOK — D148'in ikinci yarısı hiç koşmuyor. | ✅ kilitlendi |
| 3 | S0 · S4 · S13 (A kurulumu) | D145 · alçak açı ufku kadrajdan attı, model kapanan ufku DUVARLA doldurdu (ovadaki gemi kanyona girdi) | A kurulumu kamerayı yere indiriyor; ufuk kaybolursa model boşluğu kanyon duvarıyla doldurur ve biyom değişir. | ⛔ HORIZON LOCK: ufuk çizgisi kadrajın ALT ÜÇTE BİRİNDE sabittir ve üç sahnede de AYNI yüksekliktedir. ⛔ EN BÜYÜK ARKA PLAN NESNESİ adıyla ve kadraj payıyla yazılır: alçak koyu sırt, ufkun sağ yarısında, kadraj yüksekliğinin onda biri. | ✅ kilitlendi |
| 4 | S0 · S1 · S4 · S6 · S8 · S12 · S13 | D32 · COLD BURN 65 m gemi lander boyunda okundu · AMBER LATTICE monolit 25 m → 80 m fırladı [ADAY-22] | Dev gemi altı sahnede görünüyor; ölçek iki sahne arasında kayarsa filmin tek büyük varlığı çöker. | ⛔ Kesir merdiveni FORMÜLLE hesaplanır (kesir = nesne yüksekliği × odak ÷ (mesafe × 20,25 mm)) ve ELLE seçilmez. ⛔ Tüm kesirler AYNI nesneyi (gövde yüksekliği) ve AYNI ekseni (kare yüksekliği) ölçer. ⛔ Her yapı kadrajında EN AZ BİR ÖLÇEK ŞAHİDİ: A'da ön planda figür · D'de pabuç (bilinen ölçü) · S4'te dört ayağın perspektifte küçülen dizisi. | ✅ kilitlendi |
| 5 | 14 sahnenin 14'ü | D138 · THE THIN ROOF S2 — halkanın iç yayına `11 metres` + gradasyon çentikleri BASILDI | Ölçü prompt gövdesine inince model onu nesnenin ÜSTÜNE yazıyor. | ⛔ Prompt gövdesinde METRE · SANTİM · DERECE · f-SAYISI SIFIR. Ölçü yalnız PLAN fizik defterinde ve QA_SPEC D bloğunda; gövdede GÖVDE BOYU birimi (1H = 1,90 m). ✅ Kamera MESAFESİ muaftır (`from twenty-two metres away` yazılabilir — kadrajdaki bir nesneye bitişik değil). | ✅ kilitlendi |
| 6 | S1 · S3 · S6 · S7 · S8 · S10 · S12 | D143 · toz cümlesi yoğunluk sayısı taşımıyordu, ışık sütunu TOZ ŞELALESİ oldu · D39 · toz SÜZÜLDÜ | Toz bu filmin novum'unu taşıyan malzeme; yanlış yazılırsa novum ekrandan düşer. | ⛔ Her toz cümlesi ZERRE YOĞUNLUĞU + DÜŞÜŞ HIZI taşır. ⛔ `curtain · waterfall · wall · sheet · swirl · billow` YASAK. ⛔ `hang · float · suspended · drift` kökleri YALNIZ negatif blokta [D59]. ✅ Pozitif kilit: toz DÜŞER ve YERE OTURUR; oturduktan sonra havada zerre YOK; düşme hızı yürüyüş temposundadır. | ✅ kilitlendi |
| 7 | S3 · S7 · S10 · S11 | D123 · LAST SPAN 29× `gore` yazan 0 kare gore'lu film reddedildi · RISING SNOW S2 `hammer` + `blows` REDDEDİLDİ | Filmin dört sahnesinde bir alet zemine iniyor; ölçülmüş red kalıbı tam burada. | ⛔ `hammer · blows · strike · smash · slam` YAZILMAZ. ✅ GEÇEN çözüm birebir kopyalanır: `the flat of the tool comes down on the collar, once, then again`. ⛔ Yasak cümlesi de YAZILMAZ (`no violence` D123 tuzağıdır) — karşılığı POZİTİF kilittir. | ✅ kilitlendi |
| 8 | S9 | 03_PLAN_ONCESI B5 · 06_HIKAYE_HATTI §4 — 79 filmde İSTEK 8, ENGEL 2; bedel sahne numarası taşımayan film 'umursamadım' alıyor | Bedel yazılıp sahneye çapalanmazsa merkezî seçim ekranda okunmaz (THE COUNTED TURN ⑩ 3,4/10 — THE CHOICE IS INVISIBLE). | ⛔ BEDEL = ÖRNEK KASASI · S9 ve AYNI KAREDE görünür: kasa toza iner, kayış hatta gider. ⛔ S9'un promptu ÖNCE/SONRA beden farkını AÇIKÇA yazar (kayışı sökerken duraklama · kasayı bırakırken elin bir an kalması). ⭐ ÖLÇEN MERCEK: ⑩ OYUNCULUK cat.6 (merkezî seçim bedende). | ✅ kilitlendi |
| 9 | S3 (KAPI 1) | D73 · THE WRONG SHADOW — novum türetilmiş fenomene yüklendi, dönme hareketi JALONLARA sıçradı, novum ekranda 0 kare, hikâye 3,0/10 | Novum bu filmde SOMUT bir nesnede (çelik kazık) yaşıyor ama S3 tutmazsa film bir ortam turudur. | ⛔ TEK KARE FİZİBİLİTE KAPISI: S3'ün IMAGE promptu TEK BAŞINA üretilir; bilezik toz seviyesinin ALTINDA ve vurulacak baş YOK okunmuyorsa VİDEO ÜRETİMİNE HİÇ GEÇİLMEZ. ⛔ KABUL/RET/YABANCI GÖZ/SONUÇ satırları PLAN'da; SONUÇ tarih + GEÇTİ/BATTI olarak doldurulmadan S4 üretilmez [D74]. | ✅ kapı yazıldı |
| 10 | 14 sahnenin 14'ü | D146 · SKYLIGHT (1 filmde 3 kask) · YERÇEKİMİ F2 (vizör geometrisi 9 promptta ölçüyle yazılıydı, 6 klibin 5'inde tam tarif vardı ve altısı da KUBBE çıktı) · STANDING WIRE (24 klibin çoğunda kubbe) | ⚠️ REFERANS PAKETİ YAZILMIYOR — biçim kilidinin TEK taşıyıcısı metindir ve metin bu nesnede üç kez ölçülerek TUTMADI. | ⛔ Vizör GEOMETRİYLE yazılır: kabuk + DÜZ ön pencere + GÖRÜNÜR METAL ÇERÇEVE + yaka mührü + tek spekülar çizgi. ⛔ `seamless · domed · bubble · visor-less` YAZILMAZ. ⛔ Blok 14 promptta BİREBİR kopyalanır (tek kelime değişmez). ⭐ ÖLÇEN MERCEK: ② DEVAMLILIK cat.4 (ekipman). ⚠️ KABUL EDİLMİŞ RİSK — PLAN'da D74 satırıyla yazılı. | ⚠️ kabul edilmiş risk |
| 11 | S0 · S1 · S4 · S9 · S13 (A kurulumu) | ACILIS_KAPANIS_CIFTI §5 · ADAY-25 (AMBER LATTICE: kapanış karesi açılış kurulumuna DÖNMEDİ, döngü kırıldı) · D153 (eş kadraj çifti aynı metinle aynı seti üretmedi) | A kurulumu beş sahnede kullanılıyor; kamera üç adım kayarsa kafiye çöker ve iki ayrı yer okunur. | ⛔ KONUM KİLİDİ: A'nın kamera metni beş sahnede BİREBİR kopyalanır ve dönüş işaret satırını taşır: `— the same position, height and lens as Scene 0.` ⛔ Eş kadraj çifti (S0 ↔ S13) kaynağın ONAYLI KARESİNDEN türetilir ve fark listesi ≤3 maddedir. ⭐ ÖLÇEN MERCEK: ⑨ KADRAJ cat.3 (kafiye çifti). | ✅ kilitlendi |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S2 · S5 · S8 · S10 (hedefe yönelim) | KART 9 · D104 · BLACK CRADLE S4 — dört kanallı kilide rağmen koşucular ışığa ve kameraya döndü | Alçak güneş kadrajın en parlak öğesi; koyu yama silik bir hedef olursa yön mıknatısı devreye girer. | DÖRT KANALLI KİLİT zorunlu: ① hedefin EKRAN DİLİMİ ve yön AYNI cümlede ② omuz hattı derecesi ③ IŞIĞA GÖRE POZ (`her back is to the low sun; the warm band rims her back silhouette`) ④ yön negatifi. ⛔ Hedef hiçbir sahnede SİLİK değildir: koyu yama soluk toza karşı SERT KENARLI ve her karede AYNI ekran diliminde, ADIYLA yazılı. ⭐ ÖLÇEN MERCEK: ⑪ IŞIK cat.1 | ⚠️ üretimde ölçülür |
| 2 | S1 · S6 · S8 · S12 (toz halkası) | D147 · üç sabit aşınma izi tozlu odada tutmadı, kabinde SIFIRLANDI · D84 · THE THIRD DUNE 2:29 kumlu → 2:40 tertemiz | Sayaç METİNLE taşınırsa sahneler arasında sıfırlanır — bu deponun ölçülmüş en inatçı arızası. | Kademe DEĞİŞMEYEN komşu sahneler onaylı imajdan ZİNCİRLE üretilir; kademe DEĞİŞEN sahne master'dan YENİ ÇAPA alır. ⛔ Geri dönüş 0 kare. ⛔ Faz ADI/ETİKETİ gövdeye girmez [D155]. ⭐ ÖLÇEN MERCEK: ② DEVAMLILIK cat.7 (sayaç) | ⚠️ üretim zinciri kararı |
| 3 | S3 · S7 · S10 · S11 | D175 · D169 — `the forearm tendons stand out through the glove` ÇIPLAK DERİ ürettirdi; çıplak-deri yasağı yalnız YAKANIN ÜSTÜNÜ kapatıyordu | Bu filmde efor eldiven ve kolda okunuyor; D169'un kendi cümlesi mührü delebilir. | ⛔ Zorlanma DERİDE değil MALZEMEDE okunur: eldivenin sırtındaki kumaş gerilir, bilek bileziği döner, omuz düşer. ⛔ ÜÇ BÖLGELİ çıplak-deri negatifi: yaka üstü · bilek/eldiven · bel/kalça. ⭐ İKİ ZORLANMA KANALI her efor sahnesinde (malzeme + duruş). ⭐ ÖLÇEN MERCEK: ⑧ EFOR cat.1 ve cat.6 | ⚠️ üretimde ölçülür |
| 4 | S4 · S12 (metinsiz sayaç okuması) | D134 · THE ROSE COAT — rapor `no counter present` yazdı, filmde ÜÇ metinsiz sayaç vardı ve biri filmin ana mekanizmasıydı | Sayaç SPEC'e yazılmazsa mercek onu göremez ve ölçüm boşluğu bulgu yokluğu sanılır. | İKİ SAYAÇ da QA_SPEC'e ADIYLA ve kademeleriyle yazılır (toz halkası yüksekliği · kalça yuvası doluluğu). ⭐ ÖLÇEN MERCEK: ② DEVAMLILIK cat.7 | ⚠️ SPEC'e taşınacak |
| 5 | S11 (doruk) | D180 · planlı MUTLAK SESSİZLİK video modelinden istendi ve İKİ film üst üste doruğunu kaybetti — sessizlik doruktan BEŞ SANİYE SONRA geldi | Doruğun sessizliği bu filmin tek ses vuruşudur. | ⛔ Sessizlik KURGUDA HARD MUTE ile kesilir, promptta İSTENMEZ. Saniyesi ızgara formülüyle HESAPLATILIR: `t = 0 + (11 × 10,0) = 110,0 s`; müzik S10'un İÇİNDE susar (110,0'dan 1-2 s önce). ⭐ ÖLÇEN: `olcum_kapisi.sh` silencedetect | ⚠️ kurgu kararı |
| 6 | 14 sahnenin 14'ü | D150 · üretici filigranı 315/315 saniyede duruyordu ve ALTI merceğin altısı görmedi · D177 · suskunluk kapısı sıfır iddiada ateşlenmiyor | Son üç partide (UPWARD FALL · HEALING GROUND · OPEN CIRCUIT) filigran aynı biçimde geçti. | Teslim listesine KÖŞE TESTİ satırı; master FİLİGRANSIZ ihraç edilir ve `olcum_kapisi.sh` ile ÖLÇÜLÜR. ⛔ Mercek raporlarının 0 yazması ölçüm DEĞİLDİR. | ⚠️ teslim kapısı |
| 7 | S12 · S13 | D141 · D182 — klip var, VURUŞ yok; THE BENT GRASS'ta eksik sahne tam da final vuruş kanıtını taşıyordu | Vuruş kanıtı yazılmazsa kurgu kapısının üç satırı da geçer ve film yine vuruşsuz teslim edilir. | QA_SPEC B bloğuna: `FINAL BEAT PROOF — 132,0 s · in one frame: exactly FOUR landing pads, THREE standing on the surface and ONE sunk to its rim; exactly ONE taut line crossing the frame; exactly ONE case resting on the dust.` ⭐ Sayılabilir, adı konabilir, EWS ölçeğinde okunur. | ⚠️ SPEC'e taşınacak |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D48 · D176 — biyom sıçraması; ve kontrast garantisi ZEMİNİ İKİNCİ KEZ tarif edince model ilk yarıda birine ikinci yarıda ötekine sadık kaldı | Tekdüze kızıl bir ovada 14 sahne geçiyor; zemin iki kez tarif edilirse film ortasında biyom değiştirir. | BİYOM SABİTİ her promptun İLK çevre cümlesidir ve 14 promptta BİREBİR aynıdır. ⛔ Zemin TEK YERDE tarif edilir; kontrast cümlesi ÖZNEYİ tarif eder, zemine ikinci renk VERMEZ. |
| KART 12 · POLİTİKA §3.2 — kadraj genişliği bir politika değişkenidir; daralan kadrajda sınıflandırıcı bağlamı kaybeder ve yalnız DOKUYA bakar | Filmin paleti tekdüze KIZIL ve üç sahnesi CU/MS. `⑦ kırmızı ton + yakın plan` imzası varsayılan durumdur. | Her CU/MS sahnesine ÇEVRESEL ÇAPA cümlesi: `behind the hands the pale ground runs back to a low dark ridge, and the far ridge stays in frame`. ⭐ Ve karşıt renk kadrajda tutulur: BEYAZ giysi + CYAN pratik ışık [TUR 14 derinlik reçetesi]. |
| D34 · D45 · D155 — film adı, karakter adı, kısaltma ve defter etiketi giysiye/gövdeye BASILIYOR | Filmin adı bir NESNE adıdır (çapa) ve gemi adı yazılırsa model gövdeye tabela basar. | ⛔ Film adı · karakter adı · gemi adı · `PHASE n` · `EVA` · `K2` prompt gövdesine GİRMEZ. ⛔ D138 kapsam kalıbı BİREBİR: `no readable text, digits, letters or symbols on any display, surface, patch or sign` — araya kelime SOKULMAZ. |
| D56 — `dalış` sözlüğü su üretti: atmosfer okyanusa döndü | ⚠️ BU FİLMİN TAŞIYICISI BİR ÇAPADIR ve `anchor · moor · sea · seabed` kelimeleri suyu çağırır. | ⛔ İngilizce prompt gövdesinde `anchor · moor · mooring · sea · tide · dive · wave · dune sea` SIFIR geçiş. Nesne yalnız GEOMETRİSİYLE anılır: `a steel pin with a broad collar`. Film adı yalnız platform başlığında yaşar. |
| D83 · D136 — ortam yatağı klip sınırında öldü (20 s dijital sessizlik) ve `AUDIO ABSENT` ile `hiç koşulmadı` kayıtta aynı göründü | 0 replikli film sessiz dosya sanılabilir. | 14 sahnenin 14'ü AUDIO cümlesi taşır; ortam yatağı kurgu boyunca TEK PARÇA serilir. Yatak envanteri: ince atmosfer rüzgârı (yüksek frekanssız) + giysi içi fan + nefes. ⛔ Teslimden önce `ffprobe` ile ses kanalı doğrulanır. |
| KURGU_VE_TESLIM §2 — BOZULMA KARESİ sütunu SABİT IZGARALI FİLMDE DE doldurulur | Model çöküşü ızgaradan bağımsızdır; kırılganlık sırası: ince çizgi/tekrar eden birim → yüz ve el → kumaş/toz/duman. | 14 klibin 14'ü için BOZULMA KARESİ elle işaretlenir. ⚠️ Bu filmde en kırılgan öğeler: hat (ince çizgi) · dört ayağın dizisi (tekrar eden birim) · eldiven. Toz `dayanıklı` sınıftadır ama KENDİ ayrı arızasını taşır [D143 · D39] — bu satır yüzünden güvenli sayılmaz. |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | ⚠️ VAR ve en yüksek risk — kask/vizör 14/14 sahnede; **referans paketi YAZILMIYOR** (sahip kararı), yani kilit tamamen metinde. | Vizör GEOMETRİYLE yazılır (kabuk + DÜZ ön pencere + GÖRÜNÜR ÇERÇEVE + yaka mührü + tek spekülar çizgi); `seamless/domed/bubble` yasak; blok 14 promptta BİREBİR. Kabul edilmiş risk PLAN'da D74 satırıyla yazılı. ⭐ ÖLÇEN: ② DEVAMLILIK cat.4 |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | ⚠️ RİSKLİ — giysi, eldiven, kayış ve kızak örtüsü kumaş çağrışımı taşıyor. | ⛔ `fabric · cloth · blanket · loose folds` prompt gövdesinde SIFIR. Pozitif ve KATI adla: `taut foil-skinned insulation panels` · `a flat woven webbing band, drum-tight`. ⛔ Hiçbir yüzey DALGALANMAZ (rüzgâr 9 Pa). |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ⚠️ YAPILDI ve bir kurulum bu yüzden değişti. | Beş kurulumun beşi için kesir hesaplandı (16:9 sensör dikeyi 20,25 mm): A 24 mm/110 m → gövde ~%52, ön plandaki figür 6 m'de ~%37 · B 35 mm/6 m · C 50 mm/1,2 m · D 35 mm/22 m → pabuç ~%33 · E 35 mm/3 m → kazık bileziği ~%14 (≈155 px). ⛔ Hiçbir kurulum konusunu kadraj dışında bırakmıyor. |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | ⚠️ VAR — S4'te ölçek şahidi olarak kullanılan dört ayak dizisi ve S13'teki kasa uzak bantta. | E kurulumunda kazık bileziği ≈155 px ✅. S13'te kasa 6 m'de ve ön planda — 24 mm'de yaklaşık %11 kadraj yüksekliği (≈120 px) ✅. ⛔ 110 m'deki hiçbir ayrıntı ANLAM TAŞIMAZ: o bantta yalnız SİLUET ve SAYIM okunur (dört pabuç). |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | ❌ YOK — tek figür ve gündüz filmi; iki koyu gövde sorunu doğmuyor. | Yine de karşıt renk kilidi yazılır: BEYAZ giysi + CYAN pratik ışık, tekdüze kızıl zemine karşı [TUR 14]. Ayrım RENGE değil aynı zamanda GEOMETRİYE de bağlı: düz sırt paneli + kalçadaki iki yuva. |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | ⚠️ RİSKLİ — dört yapı kadrajı var (A ×5, D ×4). | ⛔ [YÜZEY ÜSSÜ · MARS] negatif bloğu 14 promptun 14'üne girer. ⛔ AY bloğu KULLANILMAZ (`no atmospheric haze` + `shadows absolutely black` burada FİZİK HATASI yazdırır). ⭐ En pahalı satır MAKET OKUMASI: `no tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame, no shallow depth of field on the structure`. |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ❌ YOK — tema sahne indeksi YAZILDI. | İNSAN-MAKİNE SINIRI · sahne indeksi S3 · S4 · S9 · S11 · S13 (≥3 ✅ · S9 = bedel sahnesi, B3 çapraz kapısı). Motif dört kanalda dağıtıldı (nesne · kinesik · kamera · ışık) ve 02_KONSEPT §4'te yazılı. |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ❌ YOK — bedel sahne numarası TAŞIYOR. | BEDEL = ÖRNEK KASASI · **S9**, ve aynı karede görünür. Ayrıca ⑩ OYUNCULUK'un üç çapa vuruşundan biri olarak ÖNCE/SONRA beden farkıyla yazılır. |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | ⚠️ RİSKLİ — dört sahnede alet zemine iniyor ve refleks olarak `no violence` yazma eğilimi var. | ⛔ Yasak cümlesi YAZILMAZ. Karşılığı POZİTİF kilit: `the flat of the tool comes down on the collar, once, then again` · `the case stays closed and flat on the dust`. ⛔ `gore · blood · wound · danger · panic` 14 promptta SIFIR geçiş. |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | ⚠️ RİSKLİ — hem sürücü hem kazık adlandırılabilir nesneler. | ⛔ `hammer` YAZILMAZ → `a short weighted driver`. ⛔ `anchor` YAZILMAZ → `a steel pin with a broad collar` [D56 · D67]. Nesne FORMUYLA anılır, adıyla değil. |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ❌ YOK — replik 0. | İlgili tek formül SESSİZLİK saatidir ve HESAPLATILDI: doruk başlangıcı = 0 + (11 × 10,0) = 110,0 s; hard mute penceresi 110,0-112,0 s. ⛔ Elle yazılmadı [D122]. |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | ⚠️ VAR — SEKİZ sahnede klip içi durum değişimi (toz oturması · kazığın inmesi · kolun girmesi · hattın gerilmesi). | ÜÇÜ SINIRA TAŞINDI (S0→S1 tozun oturması · S8→S9 kasanın inmesi · S11→S12 hattın gerilmesi). KALAN BEŞİNE ARA DURUM YASAĞI yazılır: `the collar is already below the surface when the clip begins and does not move again` biçiminde — durum klibin İÇİNDE değil BAŞINDA ya da SONUNDA sabittir. ⭐ ÖLÇEN: ⑥ FİZİK cat.7 |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | ❌ YOK — 28 promptun 28'i self-contained yazılacak. | ⛔ `[CHARACTER BIBLE]` · `[WORLD BIBLE]` · `bkz.` · köşeli parantezli etiket SIFIR [D45]. Karakter ve gemi blokları her prompta TAM yazılır. |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | ⚠️ RİSKLİ — QA_SPEC E bloğunda dört makine kapısı planlanıyor. | ⛔ Her kapı KURU KOŞUYLA doğrulanır: `ffmpeg -hide_banner -filters | grep -q " <filtre> "`. Her kapı ÜÇ satır taşır: KOMUT · DOĞRULANDI (ffmpeg sürümü + tarih) · İKAME. ⚠️ `vidstabdetect` bu makinede KURULU DEĞİL — o kapı YAZILMAZ, ikamesi konur. |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | ⚠️ VAR — D169'un zorlanma cümlesi tam bu filmde kullanılacak. | ⛔ ÜÇ BÖLGELİ negatif TEK SATIRDA ve satır sonunda BÖLÜNMEDEN: `no bare skin above the collar, no bare skin at the wrists or hands, no bare skin at the waist or hips`. ⛔ `through the glove` kalıbı YAZILMAZ [D175]. |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | ❌ YOK — 1 numaralı risk SAYIYLA yazıldı. | KART 6 · İNİŞ PÜSKÜRTÜSÜNÜN TOZU. Pozitif biçim: halka gövde genişliğinin İKİ katı · SEKİZ saniyede kapanır · sonrasında havada zerre SIFIR · oturan katman BİR PARMAK · zerreler DÜŞER, dönmez. 02_KONSEPT §5 A5 bloğunda tam yazılı. |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı
   11 satırın 10'u ✅ (tasarımla kapandı / kilitlendi / kapı yazıldı)
   1 satır ⚠️ KABUL EDİLMİŞ RİSK — #10 vizör biçim kilidi: referans paketi
   sahip kararıyla yazılmıyor ve kilit tamamen metinde. ⛔ Bu bir "açık
   satır" değil, YAZILI VE GEREKÇELİ bir kabuldür [D74]; PLAN'a tek satır
   olarak taşınır ve ölçen merceği (② DEVAMLILIK cat.4) yanında yazılıdır.

☑ 🟡 ⚠️ satırlarının 7'si de QA_SPEC'e taşınacak biçimde işaretlendi
   (ölçen mercek adı yazılı — mercek adı taşımayan kilit ÖLÇÜLMEMİŞ
    sayılır [D187])

☑ tekrar eden arıza tablosunun 16 satırının 16'sı cevaplandı
   ⚠️ VAR/RİSKLİ: 1 · 2 · 3 · 4 · 6 · 9 · 10 · 12 · 14 · 15  (10 satır)
   ❌ YOK (gerekçeli):  5 · 7 · 8 · 11 · 13 · 16              (6 satır)

→ üçü de ✅ → 05_SAHNE_CALISMALARI/ açılabilir
```
