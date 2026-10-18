# THE_PLANET_THIEF

KAYNAK: `ODA/HAM_QA_RAPORU.md` dört bölümün hepsi var — 1 Anlatım Testi (8 madde + A1 tablosu 5 satır) · 2 İzleme Formu (A: sahibin 8 sorusu + 17 ayrıntı maddesi; B: dış izleyici, AI simülasyonu) · 3 Süreklilik (ne olmalı + 24 kesmelik liste + 34 bulgu) · 4 Tarama (ne olmalı + 24 bulgu + temiz aralıklar). İzlenen dosya `THE_PLANET_THIEF.mp4`, yaklaşık 4:05, 25 parça (C01-C24 ve C25 başlık kartı).
Bulgu satırı **89**: tablo 63 (AN-A1 5 · SÜ 34 · TA 24), İZ-A ayrıntı 17, İZ-B 5, Anlatım §2/§5/§7 3, SÜ "sorun bulunmayan" listesindeki K20 notu 1. A'nın 8 sorusu ayrıntı maddeleriyle aynı anları verdiği için ayrıca sayılmadı. Birleştirmeden sonra **tekil 66**.
Kısaltmalar: AN-A1#n anlatım sorunları tablosu · AN§n anlatım maddesi · İZ-A / İZ-B izleme formu A / B · SÜ#n süreklilik · TA#n tarama · K n kesme no.

PROMPT SÜRÜMÜ: **sürüm: ?** Doğrudan kayıt yok: NOTLAR DENEMELER ve İŞARETLEME'de yalnız şablon satırı var, `~/film_medya/THE_PLANET_THIEF/{ref,kare,ham}` boş, `timeline.json` şablon (`FILM_ADI`). Aday iki: `PROMPTLAR/G01-G03.md` (G0x, F5 çevirisi) ve `ODA/SAHIP_PLANI.md` (Plan, sahibin GPT Image + Omni paketi). Görsel içerik iki metinde büyük ölçüde aynı, çünkü G0x planın biçim çevirisi.
- G0x lehine (görüntü ipuçları): C06'da tavanda soket ve dikey şaft görülüyor; G01 "socket sits in the canyon's upper wall, overhead at frame-right" der, Plan K06 "on a recessed side wall at frame-right" der. C14'te figür kadrajdan çıkıyor; bu G02'nin "dolly forward toward the panoramic glass" hareketine uyar, Plan K14'ün "dolly outward"una uymaz. C20'deki hilal arma yalnız G03 C20 metninde yazılı (zayıf ipucu: göğsü önden gösteren tek çekim bu).
- Plan lehine (ses ve araç ipuçları): her klipte model sesi duruyor ve klipler 10,0 s. Planın aracı Omni 10 s; G0x iş emri ise Flow ve "Return silent videos AÇIK" diyor, P14 hiç koşulmadı. Duyulan sesler planın "Audio:" satırlarıyla örtüşüyor: C02, C09, C19 ve C20'de nefes, C10'da elektrik uğultusu, C08'de kenetlenme vuruşu, C14'te müzik ("Let the music added later open here"), C18'de derin ton. Bunlar modelin varsayılan sesi de olabilir.
→ Sınıflar G0x'e göre verildi. Plan metniyle sınıfı değişen 17 bulgu "(Plan: …)" diye yazıldı. Alıntılarda önek yoksa metin G0x'tendir; (Gö) Görsel, (Vi) Video demektir.

Yöntem notları:
- Montajın kesme listesi (SÜ ①) plan sırasıyla birebir aynı ve her bulgunun içeriği o çekimin promptuna uydu. Komşu çekime kaydırma gerekmedi, "çapa: içerik" notu yok. `kurgu.py` kullanılamadı (timeline şablon); zaman → çekim eşlemesi rapordaki Cxx ile içerikten yapıldı.
- Kesme bulgusunda kusurun hangi yanda olduğu promptlara bakılarak seçildi (örnekler: #4 C03, #20 C07, #34 C11, #63 C24). Tek satırda iki ayrı nesne varsa satır bölündü: SÜ#19 → #28 + #29, SÜ#26 → #43/#44/#45, SÜ#27 → #49/#50, SÜ#31 → #57/#58, SÜ#33 → #62/#63.
- Kesmedeki ses sıçramasının (S7) tür listesinde karşılığı yok; "replik tekrarı/ses" altına yazıldı. G0x'te ses tarifi bilerek yazılmadı (FILM §6 "model sesi kullanılmaz"). Ağaç gereği bu satırlar 🅑 çıkıyor ama müdahale yeri kurgu; bu yüzden özet oranı iki biçimde verildi.
- İnsan doğrulaması: ? Hiçbir satır doğrulanmadı (NOTLAR'da hepsi "doğrulanacak"); sınıflar geçicidir.
- Raporlar arası çelişkiler:
  - C14'te figür TA#12'ye göre "sola", İZ-A 4'e göre "sağa" kayıyor.
  - C20'de AN 03:15 "bileğindeki cihaza bakıyor" der; İZ-A 4 "gözleri saate değil kameraya" der.
  - K20, "sorun bulunmayan" listesinde olduğu hâlde içinde değişiklik yazıyor.
- QA_DEGERLENDIRME'deki "kök neden" cümleleri kanıt sayılmadı.

## BULGULAR

| # | çekim | rapor (bölüm · zaman) | bulgu (≤15 kelime) | tür | sınıf | promptta ne yazıyor — Görsel / Video (≤25 kelime birebir alıntı ya da "YOK") | doğduğu yer | not (≤15 kelime) |
|:--:|:--:|---|---|---|:--:|---|:--:|---|
| 1 | C01 | TA#1 · İZ-A ses · 00:00 | Dış vakumda rüzgâr, elektrik cızırtısı, derin bas | ortama aykırı ses | 🅑 (Plan: 🅐) | YOK · Plan (Vi) "Audio: a low cinematic tonal pressure sound, treated as score-like design rather than sound travelling in vacuum." | ses | Derin bas FILM §6 S1 tasarımı (🅒 kısmı); müdahale kurguda |
| 2 | C01 | TA#2 (LIKELY) · 00:03 | Amber yaylar yıldırım gibi kıvrılıp Dünya yüzeyine çarpıyor | diğer | 🅑 | (Gö) "broad translucent amber tractor arcs surround the planet" · (Vi) "the amber tractor arcs around it begin to strengthen" | hareket | Mesafe yalnız ref 4 sayfasında; kıvrılma kurmaca alan tasarımı |
| 3 | K1 C01→C02 | SÜ#1 · İZ-A ses "her 10 sn" · 00:10 | Kesmede uzay uğultusu sıfırlanıyor, bip+nefes başlıyor | replik tekrarı/ses | 🅑 | YOK (G0x ses yazmaz) | kurgu | Klip sesi montajda kalmış; yatak ve geçiş kurgunun işi |
| 4 | C03 (K2) | SÜ#2 · 00:20 | C02 şeffaf fanus kask+kemer → C03 kapalı kabuk, kemer yok | giysi/işaret/arma/bant | 🅐 | C03 (Gö) "His ivory helmet, the burnt-orange stripe on his upper arm and the dark seat harness occupy the lower-left foreground" · C02 "a round ivory helmet" | kare | Şeridin tarafı yazılmamış ("on his upper arm") — 🅑 kısmı |
| 5 | C03 (K2) | SÜ#3 · 00:20 | C02'de sağdan sıcak ışık → C03 karanlık, yalnız mavi | ışık | 🅑 | C03 YOK — anahtar ışık yönü yok; yalnız kapanış "cold steel-blue shadows and warm amber practical light" | kare | C02'deki "amber reflection … from frame-right" C03'e taşınmamış |
| 6 | C02 (K2) | SÜ#4 · 00:20 | C02 penceresinde istasyon iç duvarı; C03'te gemi uzakta | dünya/arka plan | 🅑 | (Gö) "A broad amber reflection from the unseen ark enters from frame-right" · "The canopy and its dark window mullions frame the view at frame-right" | kare | Camın ötesi tarif edilmemiş; "unseen" çapa sayılmaz |
| 7 | C03 | TA#3 · 00:20 | Eller lövyede hareketsiz, dışarıda istasyon hızla dönüyor | el-nesne | 🅑+ | (Vi) "the massive ribs outside start to slide gently past the canopy while the pilot stays braced in his seat" · "The approach quickens a little" | hareket | Araç manevra yaparken pilot pasif yazılmış; hızlanma kalıbı |
| 8 | C03 | TA#4 · 00:22 | İstasyon dönerken perspektifi bükülüyor; Dünya sabit | dünya/arka plan | 🅐 | (Vi) "Earth's globe stays whole at frame-left and the amber intake stays rigid at frame-right" | hareket | Uzak Dünya'nın sabit kalması doğru fizik (🅒 kısmı) |
| 9 | C04 (K3) | SÜ#5 (LIKELY) · 00:30 | Kavisli konsol → düz masada büyük monitör, turuncu ışıklar | ekipman/nesne biçimi | 🅑+ | (Gö) "The screen bezel is graphite, lit by cyan console glow" ↔ kapanış "cold steel-blue shadows and warm amber practical light"; "small" YOK | kare | Plan K04 aynı kapanışla 🅑+; 100 mm ek plan ekranı büyütür |
| 10 | K3 C03→C04 | SÜ#6 · 00:30 | Bas uğultu kesiliyor, tik-tak ritim ve yeni müzik | replik tekrarı/ses | 🅑 (Plan: 🅑+) | YOK · Plan K03 "Audio: interior engine vibration and a short harness creak." ↔ K04 "Audio: a brief low warning chime over ventilation." | kurgu | Planda aynı kokpite iki farklı ses yatağı |
| 11 | C05 | TA#5 · SÜ#7 · İZ-A ses · 00:40 | Vakumda jet motoru, rüzgâr; C04 müziği kesmede kesiliyor | ortama aykırı ses | 🅑 (Plan: 🅐) | YOK · Plan (Vi) "Audio: non-diegetic low tension texture only." | ses | Müdahale kurgu: klip sesi kapatılır (BILINEN §B3) |
| 12 | C05 | AN-A1#1 (LIKELY) · İZ-B kayıt · 00:40 | Gemide mi istasyonda mı, yaklaşma yönü karışıyor | hikâye/anlatım | 🅑 | (Gö) "The frame holds only the craft and the hull." | anlatım | C03'teki giriş/Dünya çapası C05'e bilerek alınmamış |
| 13 | C05 (K5) | SÜ#8 · 00:50 | Mekik: düz sırt, çift dikey kuyruk → kapak, yan podlar | ekipman/nesne biçimi | 🅑+ | C05 (Gö) "Its two fixed short graphite fins, burnt-orange flank stripe and recessed rear thrusters with a dim blue-white glow are clearly readable." | kare | "fins" kuyruk kanadını çağırıyor; sırt halkası C05'te yok |
| 14 | C06 | SÜ#9 · TA#6 · 00:50 | Dikey şaftta yükseliyor, ekseninde dönüyor, itici yok | yerçekimi/fizik | 🅐 | (Vi) "glides forward in a slow straight line, nose pointing ahead and fins level … the craft keeping its level attitude" · Plan "it does not spin or roll" | hareket | İtici yazılmamış (🅑 kısmı); tavan soketi dikey okumayı besliyor |
| 15 | K5 C05→C06 | SÜ#10 · 00:50 | Motor uğultusu kesilip sakin hangar uğultusu | replik tekrarı/ses | 🅑 | YOK | kurgu | — |
| 16 | C07 (K6) | SÜ#11 · 01:00 | Kanatlı mekik → kanatsız mermi gövde, siyah konik burun | ekipman/nesne biçimi | 🅑 | (Gö) "take the ivory wedge fuselage, the burnt-orange flank stripe and the cylindrical dark-grey dorsal docking collar from it" — kanat ve burun YOK | kare | Araç biçim cümlesi çekimden çekime kısalıyor |
| 17 | C07 (K6) | SÜ#12 · 01:00 | Arkada açık uzay; tavan soketi çok katmanlı dev kubbe | dünya/arka plan | 🅐 | (Gö) "directly beneath the ark's fixed round docking socket on the berth ceiling … Its dorsal cylindrical docking collar is aligned vertically with the matching socket" | kare | Açık uzay dış kanyon tasarımına uygun; asıl sapma C06'nın kapalı görünmesi |
| 18 | C07 | TA#7 · 01:00 | Motor sönük, itici yokken tavana yükseliyor | yerçekimi/fizik | 🅑 | (Vi) "the rescue craft begins to rise very slowly in a straight vertical line beneath the fixed socket" | hareket | İtki ipucu yok; RCS görünmez de olabilir, QA katı olabilir |
| 19 | C08 (K7) | SÜ#13 · 01:10 | Halka pürüzsüz/yatay ışıklı → dikey turuncu ışıklı, boyası dökük | ekipman/nesne biçimi | 🅑 | C07 "Small amber alignment lamps are glowing." · C08 "the scratched ivory ceramic paint … small amber alignment lamps glow beside the interface" | kare | Lamba yeri sabitlenmemiş; aşınma kelimesi yalnız C08'de |
| 20 | C07 (K7) | SÜ#14 · 01:10 | C07 gölge/üstten turuncu → C08 soldan sert beyaz gün ışığı | ışık | 🅐 (Plan: 🅑) | C07 = C08 (Gö) "Cold white sunlight from the upper left, deep steel-blue shadows, warm amber light from the ark's rim, seams and lamps." | kare | İki çekimde aynı ışık cümlesi; C07 karesi uymamış |
| 21 | K7 C07→C08 | SÜ#15 · 01:10 | Bas uğultu kayboluyor, tiz türbin ıslığı başlıyor | replik tekrarı/ses | 🅑 | YOK | kurgu | — |
| 22 | C08 | TA#8 · 01:12 | İki çatallı kıskaç temasta eriyip yatay şeride dönüşüyor | ekipman/nesne biçimi | 🅐 | (Gö) "One broad mechanical clamp is open beside the interface" · (Vi) "the one visible rigid clamp starts to rotate very slowly on its hinge" | hareket | Temas anı; müdahale kadraj/kesme (BILINEN §B1) |
| 23 | C08 | TA#9 · İZ-A ses · 01:15 | Kilit sesi kıskaç kapandıktan 2 s sonra geliyor | replik tekrarı/ses | 🅑 | YOK · Plan (Vi) "Audio: one deep docking thud and one short metallic latch" | ses | Senkron kurguda kurulur; prompt işi değil |
| 24 | C05-C08 | İZ-A tempo · İZ-B 7 · 00:40-01:19 | Kenetlenme dört çekim sürüyor, tempo düşüyor | hikâye/anlatım | 🅒 | — (tasarım: plan K05-K08, "yanaşmayı iki plana böldüm") | — | Sahip için tempo verisi; prompt dışı |
| 25 | C09 | SÜ#16 (LIKELY) · 01:20 | Vizör küçük, sırtta büyük çanta, şerit yalnız sol kolda | giysi/işaret/arma/bant | 🅐 (Plan: 🅑) | (Gö) "a burnt-orange stripe on each upper arm, white gloves, black boots and a compact ivory life-support pack" | kare | Çanta tasarımda var (🅒 kısmı); sağ kolda şerit eksik |
| 26 | C10 (K9) | SÜ#17 · 01:30 | Astronot kayboluyor, koridor sonu sekizgen odaya dönüşüyor | dünya/arka plan | 🅒 | (Gö) "The corridor stands empty and leads directly into the maintenance observation chamber, whose matching vertical amber conduit glows at the far end." | — | İnsansız ek plan ve uçtaki bölme tasarım |
| 27 | K9 C09→C10 | SÜ#18 · 01:30 | Piyano/nefes kesiliyor, yüksek elektrik uğultusu | replik tekrarı/ses | 🅑 (Plan: 🅑+) | YOK · Plan K09 "Audio: hollow pressure-system ventilation, breathing and a low structural vibration." ↔ K10 "Audio: a resonant electrical hum rising gently." | kurgu | Planda aynı koridora iki farklı ses yatağı |
| 28 | C11 | SÜ#19 · AN-A1#2 · İZ-A 2 · İZ-B 6 · AN§2 · 01:40 | Yüz, sakal ve kask yan bağlantısı C02'den farklı | yüz/kimlik | 🅑 | (Gö) "Reference 1 (man): take his face, helmet and pressure suit from it, using the right-side full-length panel." — sakal ve saç YOK | kare | Kimlik yığını bilerek yazılmamış; yüz tam boy panelden alınıyor |
| 29 | C09→C11 | SÜ#19 · İZ-A 3 · İZ-B 6 · 01:40 | Alet: C09 çift namlulu kutu → C11 ince uçlu matkap | ekipman/nesne biçimi | 🅑 | C11 (Gö) "He holds the compact matte-black plasma cutter in both gloved hands, its rigid short nozzle dark" | kare | Kabza ve silindir biçimi yalnız ref 8 sayfasında |
| 30 | C11 | TA#10 · İZ-A 3 · 01:40 | Matkap ucu yuvaya değmeden havada dönüyor | el-nesne | 🅐 | (Gö) "its rigid short nozzle dark and aimed toward the bracket from a short distance; the tool's single power light glows dim orange" · Plan "never activates the cutter" | hareket | Temassızlık tasarım (🅒 kısmı); dönme/çalışma modelin |
| 31 | C11 | TA#11 · İZ-A 4 · 01:40 | Aletin ağırlığı ya da titreşimi kollara yansımıyor | el-nesne | 🅑 | (Vi) "with both gloved hands he raises the already-held cutter by only a few centimetres" | hareket | Alet kapalı tasarlandı; ağırlık ipucu yok; kök #30 |
| 32 | C11 | AN-A1#2 · İZ-A 1 · İZ-B 2 · AN§3 · 01:40 | Tamir mi sabotaj mı anlaşılmıyor | hikâye/anlatım | 🅑+ | (Vi) "its dark nozzle settling its aim on the fixed service bracket" | anlatım | Hedef hat değil braket, bakım gibi okunuyor; R10 kaydı da yok |
| 33 | K10 C10→C11 | SÜ#20 · 01:40 | Elektrik uğultusu kesilip sessiz alt uğultuya geçiyor | replik tekrarı/ses | 🅑 | YOK | kurgu | — |
| 34 | C11 (K11) | SÜ#21 · 01:50 | C11'de sol bilek çıplak, C12'de tarayıcı beliriyor | ekipman/nesne biçimi | 🅑 | C11 YOK — giysi listesinde tarayıcı yok | kare | Tarayıcı yalnız C12 ve C20 promptunda yazılı |
| 35 | C14 (K13) | SÜ#22 (LIKELY) · 02:10 | Korkulukta sol bilekte cihaz görünmüyor | ekipman/nesne biçimi | 🅑 | (Gö) "a tiny helmeted figure in an ivory pressure suit … the matte-black cutter low in his right hand" | kare | Küçük siluet; düşük öncelik |
| 36 | C14 | TA#12 · İZ-A 4 · 02:10 | Adım atmadan kayıp kadrajdan çıkıyor; tepki yok | kamera/kadraj | 🅑+ (Plan: 🅐) | (Vi) "the heavy window frame and railing starting to slide outward past the edges of the picture while the small figure stays standing at the railing" | hareket | Yön çelişkisi: TA "sola", İZ "sağa"; tepkisizlik tasarım |
| 37 | C15 (K14) | SÜ#23 · 02:20 | Işık C14'te sağdan, C15'te sol üstten geliyor | ışık | 🅑 | (Gö) "Its dusk terminator crosses the middle of the globe" · "Warm golden light on the day side" — ışık kaynağının yönü YOK | kare | Işık yönü kasa düzenine bağlanmamış |
| 38 | K14 C14→C15 | SÜ#24 · 02:20 | Yaylı çalgı müziği kesmede kesiliyor | replik tekrarı/ses | 🅑 (Plan: 🅑+) | YOK · Plan K14 (Vi) "Let the music added later open here." | kurgu | Plan metni klibe müzik çağırıyor |
| 39 | C16 (K15) | SÜ#25 · 02:30 | Simetrik düzen → sağda dev kızıl gezegen, solda iki küçük | dünya/arka plan | 🅒 | (Gö) "The rust desert world occupies the right foreground … Two of the other rescued worlds are small distant spheres at frame-left." | — | İstenen açı; yalnız kafes farkı 🅐 olabilir |
| 40 | C14-C16 | İZ-A tempo · 02:10-02:39 | 30 s yeni aksiyon olmadan sergileme | hikâye/anlatım | 🅒 | — (tasarım: plan K14-K16) | — | Tempo verisi; prompt dışı |
| 41 | C17 | TA#13 · 02:40 | Kara kütle vakumda baca dumanı, kül gibi kabarıyor | parçacık/duman/alev/sıvı | 🅑+ (Plan: 🅑) | (Gö) "The front is an irregular dark mass with a ragged outline" · (Vi) "the advance quickens and the front sweeps over" | hareket | Ref 9 metni de "a ragged, formless mass of absolute darkness" |
| 42 | C18 | TA#14 · 02:50 | Vakum dış çekimde derin, yankılı uğultu | ortama aykırı ses | 🅒 | — · Plan (Vi) "Audio: a deep low pressure tone treated as non-diegetic design." | — | FILM §6 S18 tasarımı; QA tasarımı kusur saymış |
| 43 | C19 | SÜ#26 · AN-A1#3 · İZ-A 2 · İZ-B 6 · AN§2 · 03:00 | Sakalsız başka yüz, alnında yara | yüz/kimlik | 🅑 | (Gö) "An adult man in an elegant ivory-white pressure suit … a small old scar through his right eyebrow is visible through the visor" | kare | Sakal yazılmamış; yaranın yeri yazılı (🅐 kısmı) |
| 44 | C19 | SÜ#26 · SÜ#27 · 03:00 | Tarayıcı sağ bileğe/ön kola geçmiş, kare ekranlı | ekipman/nesne biçimi | 🅑 | (Gö) "Reference 8 (cutter and wrist scanner): take the matte-black plasma cutter from it." — tarayıcı ve tarafı YOK | kare | İki nesneli ref sayfası ekli; tarayıcı serbest kalmış |
| 45 | C19 | SÜ#26 · AN-A1#3 · İZ-A 2 · İZ-B 6 · 03:00 | Alet çift uçlu büyük silaha dönüşüyor | ekipman/nesne biçimi | 🅑+ (Plan: 🅑) | (Gö) "He holds the compact matte-black plasma cutter in both gloved hands at chest height, its short nozzle dark and pointed forward" | kare | İki el + göğüs hizası + ileri = tüfek duruşu |
| 46 | C19 | TA#15 (LIKELY) · 03:00 | Ağır silahı ağırlıksız, boş kutu gibi taşıyor | el-nesne | 🅑 | (Vi) "in one slow, deliberate motion the cutter sinks from chest height past his belt" | hareket | Kök #45; ağırlık ipucu yok |
| 47 | C19 | AN-A1#3 · İZ-A 1 · AN§5 · İZ-B 3 · 03:00 | Ne yapacağı, neden beklediği, kararı belirsiz | hikâye/anlatım | 🅑+ | (Gö) "a full arm's length from the bracket … his expression has shifted from urgent determination to shaken understanding" | anlatım | Kare zaten nişansız; zihinsel değişim tek karede gösterilemez; R17 yok |
| 48 | C20 | SÜ#28 · SÜ#29 · AN-A1#4 · İZ-A 3 · İZ-B 6 · 03:10 | Arkada bulut, dağ, teras; doğal gün doğumu ışığı | dünya/arka plan | 🅑+ | (Gö) "Warm artificial sunlight from the panoramic window on the far wall lights the frame-right side of his face and suit" · Plan aynı | kare | Camın ötesi yazılmamış; "sunlight" + "window" dış manzara çağırıyor |
| 49 | C20 | SÜ#27 · TA#16 · İZ-A 2 · 03:10 | Göğsün iki yanında hilal-yıldız armalar | istenmeyen yazı/bayrak | 🅑+ (Plan: 🅑) | (Gö) "a single circular blue-and-gold mission badge on his left chest showing an abstract crescent" | kare | "crescent" hilal-yıldızı çağırdı; "single/left" yazılı ama ikiye çıktı |
| 50 | C20 | SÜ#27 · 03:10 | Tarayıcı sol bilekte yuvarlak saate dönüşüyor | ekipman/nesne biçimi | 🅐 (Plan: 🅑) | (Gö) "the ivory rectangular wrist scanner with a black glass face and a broad dark strap sits on his left wrist" | kare | — |
| 51 | K19 C19→C20 | SÜ#30 · 03:10 | Alet kayboluyor, boş sol el göğse kalkıyor | durum sıfırlanması (kesmede) | 🅒 | (Gö) "His right hand and the lowered cutter are below the frame." | — | Kesicinin kadraj dışında kalması tasarım |
| 52 | C20 | TA#17 · İZ-A 3 · 03:14.5 | Bıyığa mavi ışık lekesi yapışıp kalıyor | ışık | 🅑+ (Plan: 🅑) | (Vi) "the warm light on his face and visor shifts slightly with the glow of the ring" | hareket | Halka ışığı prompta yüze bağlanmış |
| 53 | C20 | İZ-A 4 · 03:15 | Saati yüzüne yaklaştırıyor ama kameraya bakıyor | kamera/kadraj | 🅑+ | (Gö) "Frontal medium close-up … his eyes look straight ahead with urgent conviction" · (Vi) "his eyes facing forward" | hareket | Önden yakın planda "straight ahead" merceğe bakış olur; kolu kaldırmak modelin |
| 54 | C20 | İZ-A 1 · AN§5 · 03:15 | Neyi tetiklediği görünmüyor; basış yok | hikâye/anlatım | 🅑 (Plan: 🅐) | (Vi) "the cyan ring on the wrist scanner brightens from dim to bright" — basış YOK · Plan "Elias makes one small thumb press" | anlatım | F5 basışı kesmeye aldı; ışık sebepsiz yanıyor; R18 yok |
| 55 | C21 (K20) | SÜ "sorun bulunmayan" K20 notu · 03:20 | C18'de kararan Dünya C21'de aydınlanmış, kıta yönü değişmiş | ışık | 🅑+ | (Gö) "the familiar African landmass and the white clouds clearly readable" ↔ "leaving most of Earth and the rigid black hull in blue-black shadow" | kare | Aynı Görsel'de zıt istek; Plan'da da "clearly readable" var |
| 56 | C21 | TA#18 · 03:20 | Vakumda rüzgâr ve bas uğultusu | ortama aykırı ses | 🅑 | YOK · Plan (Vi) "Audio: a rising deep designed resonance, no explosion." | ses | Bas tasarım (FILM §6 S21); rüzgâr değil |
| 57 | C22 | TA#19 · SÜ#31-32 · AN-A1#5 · İZ-A 3 · İZ-B 6 · 03:30 | İstasyon ağzından vakumda siyah duman; ark uzaklaşıyor | parçacık/duman/alev/sıvı | 🅑+ (Plan: 🅑) | (Vi) "where the Sun was only the lightless front remains, spreading very slightly across the dark" ↔ (Gö) "the empty space around the intake holds only stars" | hareket | QA dumanı cepheyle karıştırıyor; kilitli kamerada ark hareketi 🅐 |
| 58 | C22 (K21) | SÜ#31 · 03:30 | C22'de Dünya ve halkalar kayboluyor | dünya/arka plan | 🅒 | (Gö) "the empty space around the intake holds only stars" | — | Dünya artık içeride; tasarım |
| 59 | C22 | TA#20 · 03:30 | Vakumda rüzgâr ve gök gürültüsü | ortama aykırı ses | 🅑 | YOK · Plan (Vi) "leaving a low sustained tone" | ses | Alçak ton tasarım; gök gürültüsü değil |
| 60 | C23 | TA#21 · İZ-A ses · 03:41 | Okyanus dalgası, kıyı sesi | ortama aykırı ses | 🅑+ | (Vi) "golden light from the artificial sun gradually spreads across the clouds and the ocean horizon" | ses | "ocean" kelimesi sesi çağırmış; Plan'da aynı cümle var |
| 61 | C23 | TA#22 · 03:42 | Dünya'nın arkasında yarı saydam hayalet ikinci küre | diğer | 🅐 | (Vi) "Earth stays a rigid sphere in the cradle" | hareket | Şafak çizgisi atmosferi ayırmış olabilir |
| 62 | C23 (K23) | SÜ#33 · 03:50 | Gezegenler tek sırada; Satürn benzeri halkalı gezegen var | dünya/arka plan | 🅑 | (Gö) "shines between the six other rescued worlds, each at its own depth and held by thin amber arcs" | kare | Altı dünya adlı değil, dizilim yok; halkalı gezegen tasarımda yok |
| 63 | C24 (K23) | SÜ#33 · 03:50 | Dünya Afrika yerine Amerika'yı gösteriyor | dünya/arka plan | 🅑+ (Plan: 🅑) | (Gö) "The last attached image gives only the composition and Earth's seat in the cradle; take only those from it." | kare | Kıta yazılmamış; kaynak kare kıta bilgisinden dışlanmış |
| 64 | K23 C23→C24 | SÜ#34 · 03:50 | Dalga sesi kesilip sakin ambiyansa geçiyor | replik tekrarı/ses | 🅑 | YOK | kurgu | — |
| 65 | C25 | TA#23 · TA#24 · 04:00 | Kapanışta "THE PLANET THIEF" başlık kartı | istenmeyen yazı/bayrak | 🅒 | — (post'ta eklenen başlık; plan: "Film adı … kurguda bu görüntünün üstüne eklenir") | — | Sahip ayrı kart eklemiş; plan son 2 s bindirme diyordu |
| 66 | film | AN§7 · İZ-A 5 · İZ-B 5 | Hiç replik yok, yalnız nefes; 21 replik eksik | replik tekrarı/ses | 🅑 (Plan: 🅑+) | YOK (FILM §5 kaynak kurgu) · Plan kapanış "Generate only the described ambience and effects; no dialogue and no music." | kurgu | #32 #47 #54'ün ortak kökü; kayıt yapılmadı |

## ÖZET

**Sınıf (tekil 66, G0x'e göre):** 🅐 10 · 🅑 32 · 🅑+ 16 · 🅒 8 · 🅓 0.

**🅑 oranı** (sözleşme v1.0, sınıf sütunu, payda 🅐+🅑+🅑+):
- Tümü: (🅑 32 + 🅑+ 16) / (🅐 10 + 32 + 16) = 48/58 = **%82,8**.
- Ses/kurgu kökenli 15 satır çıkarılınca: (🅑 18 + 🅑+ 15) / (🅐 10 + 18 + 15) = 33/43 = **%76,7**. Bu satırlarda ses tarifi kural gereği yazılmamıştı; müdahale yeri kurgu.
- Plan metniyle okunursa: 🅐 11 · 🅑 34 · 🅑+ 13 · 🅒 8 → 47/58 = %81,0. Sürüm belirsizliği oranı değiştirmiyor.

**En sık 5 tür:**

| Tür | Bulgu |
|---|:--:|
| ekipman/nesne biçimi | 11 |
| replik tekrarı/ses (8'i kesmedeki ses sıçraması) | 10 |
| dünya/arka plan | 9 |
| ortama aykırı ses | 6 |
| hikâye/anlatım | 6 |

Sonra ışık 5, el-nesne 4 gelir.

**Doğduğu yer:**

| Yer | Bulgu |
|---|:--:|
| kare | 24 |
| hareket | 15 |
| kurgu | 9 |
| ses | 6 |
| anlatım | 4 |
| seçim | 0 |
| araç | 0 |
| — (🅒) | 8 |

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız; G01-G03'ün 24 çekiminin hepsi ve referans promptları baştan sona okundu)

1. **Video içinde çelişki.** C14: "the heavy window frame and railing starting to slide outward past the edges of the picture while the small figure stays standing at the railing in the lower left", 8-10 s'de de "the small figure still at the railing".
   - Figür, kadrajdan çıkan korkuluğa bağlanmış. İkisi birlikte gerçekleşemez; model ya figürü kaydırır ya korkuluğu tutar (#36).
2. **Aynı Görsel'de zıt ışık.** C21: "the familiar African landmass and the white clouds clearly readable" ↔ "leaving most of Earth and the rigid black hull in blue-black shadow".
   - C18'de aynı yapı var: "Earth shows deep blue oceans, the familiar African landmass and white clouds. The outer sunlight is dim and cold from the left, leaving most of Earth … in blue-black shadow." Okunurluk isteği karanlığı yener (#55).
3. **Mekâna aykırı ortak stil kapanışı.** Kokpit çekimleri C02-C04'te tasarım yalnız camgöbeği ışık ister, ama hepsi "cold steel-blue shadows and warm amber practical light" ile kapanıyor.
   - C04 aynı blokta hem "lit by cyan console glow" hem "warm amber practical light" diyor (#9).
4. **Kimlik ve giysi cümlesi çekimden çekime değişiyor.** C09 ve C11 birebir aynı: "He wears an ivory-white pressure suit with rigid ivory chest armor, graphite shoulder panels and joint seals, a burnt-orange stripe on each upper arm, white gloves, black boots and a compact ivory life-support pack, and a round ivory helmet with a completely clear closed visor." Diğerleri farklı:
   - C19: "**An adult man in an elegant** ivory-white … on each upper arm **and white gloves**." Bot ve yaşam desteği paketi düşmüş.
   - C20: aynısı, artı "**a single circular blue-and-gold mission badge on his left chest showing an abstract crescent**".
   - C24: "… **wearing** a round ivory helmet …" ve "the burnt-orange stripe **on his sleeves**".
   - C02: "the pilot in an ivory-white pressure suit and a round ivory helmet …" Zırh ve şerit yok.
   - C03: "the burnt-orange stripe on **his upper arm**" — tekil, taraf yok.
   - C14: "a tiny helmeted figure in an **ivory pressure suit**".
   - Öznenin adı dörde bölünmüş: "the pilot" (C02, C03) · "an orbital rescue pilot" (C09, C11) · "An adult man" (C19, C20, C24) · "a tiny helmeted figure" (C14).
   - Yüz parçaları (stubble, hair, eyes) hiçbir çekimde yok. G02 başlığı bunu kural yapmış: "kimlik yığını … çekim promptlarında tekrarlanmaz" (#28 #43).
5. **Sayısız ya da belirsiz tarif.**
   - C05: "Its two fixed short graphite fins". Ref'te "side fins", planın Türkçesinde "iki kısa sabit kanat"; "fins" kanat mı kuyruk mu belirsiz (#13).
   - C03: "the burnt-orange stripe on his upper arm".
   - C23: "the six other rescued worlds" — ad ve dizilim yok (#62).
   - C16: "Two of the other rescued worlds" — hangileri olduğu yazılmamış.
   - Her çekimde "the compact matte-black plasma cutter" geçiyor ama biçimi tarif edilmiyor; kabza, silindir nozul ve güç ışığı yalnız ref 8'de (#29 #45).
6. **Tarafın yazılmaması.** Tarayıcının tarafı yalnız iki çekimde yazılı: C12 "on his left forearm" ve C20 "on his left wrist".
   - C11, C14, C19 ve C24'te tarayıcı hiç anılmıyor.
   - C19'a iki nesneli ref 8 ekli ama metin yalnız "take the matte-black plasma cutter from it" diyor; tarayıcı serbest kaldı ve sağ bileğe geçti (#44).
   - Kesicinin eli tutarlı: C09, C14 ve C24'te "right hand", C11 ve C19'da "both gloved hands".
7. **Mimari çapa yok.**
   - C20: "Warm artificial sunlight from the panoramic window on the far wall" — camın ötesi tarif edilmemiş (#48).
   - C02: "The canopy and its dark window mullions frame the view at frame-right" — dışarısı yazılmamış (#6).
   - C05: "The frame holds only the craft and the hull." — yön çapası bilerek dışarıda (#12).
   - C15: ışık kaynağının yönü yok (#37).
8. **Ekran ya da yazı daveti.**
   - C20'de "showing an abstract crescent" bir sembol adı ve yanında "the only marking" kilidi yok (#49).
   - G01'in sekiz Görsel'inde olumlu yazı kilidi "plain unmarked surfaces" var; G02 ve G03'ün 16 Görsel'inde düşmüş.
   - İyi örnek: C04 ekranı yalnız resim taşıyor ("a plain full-frame picture of the orange-yellow Sun"); yazı bulgusu çıkmadı.
9. **Vakumda duman ya da ses çağıran kelime.**
   - Ref 9: "a ragged, formless mass of absolute darkness".
   - C17: "an irregular dark mass with a ragged outline" ve "the front sweeps over" (#41).
   - C22: "spreading very slightly across the dark" (#57).
   - C01: "the amber tractor arcs … begin to strengthen" — enerji yıldırım gibi okunuyor (#2).
   - C23: "the ocean horizon" — dalga sesi (#60).
   - Plan sürümünün "Audio:" satırları vakumda uğultu istiyor ("a low cinematic tonal pressure sound", "a deep low pressure tone").
10. **Tekdüze hızlanma kalıbı.** 13/24 video promptunda orta vuruş hızlanıyor (F5 kararı 12 "hız farkı"):
    - C01 "Earth's drift picks up slightly" · C03 "The approach quickens a little" · C04 "a little faster" · C05 "The craft gains a little speed" · C06 "slides a little faster sideways".
    - C07 "continues a little quicker" · C08 "a little quicker mid-swing" · C10 "the track quickens slightly" · C13 "gathers a little speed" · C14 "carries on a little faster".
    - C15 "the push quickens a little" · C17 "the advance quickens" · C18 "the drift gathers a little speed".
    - Rijit yapılar ve gezegenler çekimin ortasında ivmeleniyor. C03'teki hızlı dönme (#7) ve C17'deki kabarma (#41) bu kalıplı çekimlerde çıktı.
11. **Meta dil.** G0x gövdelerinde Cxx ya da Scene etiketi yok.
    - "The last attached image gives only …" kalıbı altı çekimde kullanılıyor (C15, C17, C18, C21, C23, C24). C24'te Dünya'nın görünüşünü dışlıyor (#63).
    - Plan sürümünde çekimlere atıf var: K08 "from the end of the preceding shot", K17 "introduced earlier", K19 "used earlier", K23 "formerly empty". G0x'te temizlenmiş.
12. **Uzunluk sorun değil.** En uzun Görsel C09 (1.689 kr), C19 (1.679) ve C14 (1.657); en uzun Video C14 (643 kr). Hepsi 4.300 sınırının çok altında.
13. **Zihinsel ifade.** C19: "his expression has shifted from urgent determination to shaken understanding" — tek kareye zaman içinde bir değişim yazılmış (#47). C20: "with urgent conviction" (#53).
14. **Görünmeyen şeye atıf.**
    - C02: "from the unseen ark", Video'da "toward the enormous object outside at frame-right".
    - C14: "holds only open space, mostly behind the left window frame".
    - C20: "the panoramic window on the far wall" — önden yakın planda pencerenin kadrajda olup olmadığı belirsiz.
15. **Referans anahtarı ile rol uyuşmuyor.**
    - C18 ve C23 "Reference 4 (black ark): take … Earth … from it" diyor; Dünya'nın kaynağı "ark" rolündeki sayfa.
    - C19'da ref 8'in rolü "cutter and wrist scanner" ama sayfadan yalnız kesici alınıyor.
    - C20'de "Reference 6 (observation chamber): take the black ribbed walls and the vertical amber lights from it" — bölmenin penceresi ve kasa çapası referanstan alınmıyor.

## HAT KURALLARI BU FİLMDE

| Kural | Kaç çekimde yazılı | Yine de bulgu çıktı mı (kaç) |
|---|---|---|
| ORTAK GÖRÜNÜM cümlesi birebir | 0/24. FILM §3'te ORTAK GÖRÜNÜM yok: kural 12.10'da geldi, F5 11.10'da kapanmıştı. Giysi cümlesi yalnız C09 = C11'de birebir (2/9 Elias çekimi); kalanında 6 farklı sürüm var | Evet: yüz/giysi/arma 5 (#4 #25 #28 #43 #49), aksesuar 6 (#29 #34 #35 #44 #45 #50) |
| "Reference <No>" anahtarı | 24/24 Görsel. Yüklendiği kayıtlı değil (DENEMELER boş) | Evet: kimlik/biçim 16 (yüz 2 · giysi/arma 3 · nesne biçimi 11) |
| Asimetrik işaret (hangi kol, kaç bant) | Şerit "on each upper arm" 5/9 Elias çekiminde (C09 C11 C19 C20 C24); C03'te taraf yok. Rozet "on his left chest" 1 (C20). Tarayıcının tarafı 2 (C12 C20) | Evet, 6: #4 (C03 şerit) · #25 (C09 tek kol) · #49 (arma ikiye çıktı) · #34 #35 #44 (tarayıcı) |
| Koltuk / taraf | Tek karakter, koltuk sorunu yok. Kadraj tarafı 21/24 çekimde yazılı (C08, C13, C15'te yok) | Yön/180° bulgusu 1 (#14 C06); taraf yazılı çekimde |
| 10 s vuruş planı | 24/24 (2-4 vuruş, 0-10 boşluksuz) | Hareket kaynaklı 15 bulgu; 13 çekimde orta vuruşta hızlanma kalıbı |
| Model sesi / replik satırı | 0/24. FILM §5'te kaynak kurgu (kadraj dışı/telsiz); kurala uygun | Evet: #66 (21 replik montajda yok), bağlı anlatım bulgusu 3 (#32 #47 #54) |
| Vakum ses / parçacık kuralı | Ses tarifi 0/24 (kurala uygun). "Return silent videos AÇIK" 3/3 iş emrinde. Vakumda olumlu kilit 1 (C22 "the empty space around the intake holds only stars") | Evet: ortama aykırı ses 5 gerçek (+1 🅒), kesmede ses sıçraması 8, duman 2 (#41 #57; kilitli C22'de de çıktı) |
| Yazı/bayrak olumlu kilidi ("the only marking") | "the only marking" 0/24. "plain unmarked surfaces" 8/24 (G01, C01-C08); G02-G03'te 0/16 | Kilitli 8 çekimde 0 yazı/arma; kilitsiz 16 çekimde 1 (#49, C20). #65 başlık kartı tasarım |

## DERS ADAYLARI (en çok 8)

1. **Prompt yazarken:** kadrajdaki aksesuarın ve aracın biçim cümlesini ve tarafını her çekimde birebir yaz. Örnek: kesici "thick simple handle, rigid short cylindrical nozzle, one small dim orange power light"; tarayıcı "ivory rectangular … on his left wrist"; mekik "two short side wings". "the cutter" demek ya da ref sayfasını eklemek biçimi taşımıyor.
   - Dayanak: #13 #16 #19 #29 #34 #35 #44 #45. Bu filmde 8 bulguyu kapatırdı.
   - Hat kuralı mı: kısmen. goruntu-yonetmeni.md'deki "birebir aynı kelimeler" kuralı yalnız karakter için; "Asimetrik işaret hangi taraftaysa yazılır" kuralı var. Nesne ve araç biçim cümlesi yeni.
2. **Prompt yazarken:** yüz okunan çekimde (C02, C11, C19, C20) görünen kimlik parçalarını kısa ve birebir yaz ("close dark stubble, short dark hair slightly grey at the temples"). Karakteri "An adult man" diye yeniden tanıtma, yüzü tam boy panelden alma.
   - Dayanak: #28 #43. 2 bulguyu kapatırdı.
   - Hat kuralı mı: çatışıyor. KIMLIK_VE_REFERANS_KILAVUZU §1 (16.10, commit yok) kimlik cümlesini her promptta birebir ister; F5 kararı 11 ve BILINEN §A HİPOTEZ yığını söker. Karar sahibin.
3. **Prompt yazarken:** iç mekânda pencere varsa camın ötesini mimari çapayla yaz (örnek: "the window looks into the enclosed refuge: black ribs, the artificial sun in its three rings"). İç ışığa "sunlight" deme, "golden light from the artificial sun" de.
   - Dayanak: #48 #6. 2 bulguyu kapatırdı.
   - Hat kuralı mı: kısmen. GPT_IMAGE_OMNI_KILAVUZU §5 sabit mimari çapayı yalnız sol/sağ için ister; pencerenin ötesi için yeni.
4. **Prompt yazarken:** kurgusal karanlığı ve enerjiyi katı, keskin kenarlı yaz (örnek: "a sharp-edged field of absolute black whose edge stays crisp"). "mass", "formless", "spreading", "sweeps", "strengthen" gibi akışkan kelimeleri kullanma.
   - Dayanak: #41 #57 (+#2). 2-3 bulguyu kapatırdı.
   - Hat kuralı mı: ilke UZAY_FIZIGI_GORUNTU_KILAVUZU §3'te var ("ışıksız keskin bir sınır", 16.10, commit yok). Kelime listesi yeni.
5. **Prompt yazarken:** hikâyenin kararını taşıyan eylemi kadrajda görünür yaz. Nişan hattın kendisine yönelsin; C19'un başlangıç karesi hâlâ nişanda olsun; basış ya da indiriş tek ve net bir eylem olsun. Kararı zihinsel ifadeye ("shaken understanding") ya da kesmeye bırakma.
   - Dayanak: #32 #47 #54. 3 bulguyu kısmen kapatırdı; asıl taşıyıcı eksik replik kaydı (#66).
   - Hat kuralı mı: BILINEN §B1 ile çatışıyor ("temas anı gösterilmez", F5 basışı bu yüzden kesmeye aldı). Karar sahibin.
6. **Prompt yazarken:** ortak stil kapanışındaki ışık cümlesini mekânın gerçek ışığıyla değiştir; kokpitte "warm amber practical light" yerine "dim cyan console light" yaz. Her çekimde ana ışığın yönünü de yaz.
   - Dayanak: #5 #9 #37. 3 bulguyu kapatırdı.
   - Hat kuralı mı: goruntu-yonetmeni "Dünya ve ışık cümlesi her dış çekimde birebir" diyor; iç mekân ve kapanış için yeni.
7. **Prompt yazarken:** kaynak kareyi kısıtlıyorsan gezegenin kimliğini çekimde ayrıca yaz (örnek: "Africa faces the camera, lit from the left"). Aynı Görsel'de "clearly readable" ile "most of Earth in blue-black shadow"u birlikte isteme.
   - Dayanak: #55 #63. 2 bulguyu kapatırdı.
   - Hat kuralı mı: zaten var, uygulanmamış. goruntu-yonetmeni "Aynı promptta zıt iki istek" yasağı ve GPT_IMAGE_OMNI §5 "Dev gezegen yerleşimi tek kez sabitlenir".
8. **Prompt yazarken:** işaretli bir öğe (rozet) yazıyorsan sembol adı ("crescent") yerine biçim yaz ve "the only marking on the suit" kilidini ekle. G01'deki "plain unmarked surfaces" kapanışını bütün gruplara taşı.
   - Dayanak: #49. 1 bulguyu kapatırdı.
   - Hat kuralı mı: KIMLIK_VE_REFERANS_KILAVUZU §4'te var (16.10, commit yok).

Not: 🅐 olan 10 satıra "prompta ekle" yazılmaz; müdahale yerleri şöyle:
- Kare kabulü (KIMLIK §9, devamlilik kare modu): #4 #17 #20 #25 #50.
- İkinci deneme ya da temiz aralık seçimi: #8 #14 #30 #61.
- Temas anını kesmeye almak: #22.

Ses ve kurgu kökenli 15 satırın müdahale yeri kurgudur: klip sesi atılır, FILM §6 yatağı ve geçişleri kurulur, replikler kaydedilir. Bu kural zaten var (BILINEN §B3, AGENTS §2 "Model sesi KAPALI: taslakta atılır"), bu filmde uygulanmadı.
