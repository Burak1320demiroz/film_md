# THE_MAYDAY_SEA
KAYNAK: `ODA/HAM_QA_RAPORU.md` dört bölümün hepsi var: Anlatım Testi (1-8 + A tablosu 6 satır) · İzleme Formu (A sahibin 8 sorusu + B1 dış izleyici; KAYIT tablosu A/B1'in kopyası, sayılmadı) · Süreklilik (22 kesme, 13 bulgu) · Teknik Tarama (19 bulgu). İzlenen dosya `the mayday sea.mp4`, 03:54.2 (23 film klibi + 5,8 s başlık kartı). **Bulgu satırı n = 63** (Anlatım 6 + İzleme A 19 + B1 6 + Süreklilik 13 + Tarama 19) → **tekil n = 47** (45 rapor satırından + 2 türev: #2 transkriptten, #45 kesme listesi/COULD NOT CHECK'ten; rapor bu ikisini kusur saymadı).

PROMPT SÜRÜMÜ: `PROMPTLAR/G01.md · G02.md · G03.md` (12.10.2026 F5 kapanış sürümü, hat biçimi, replikler video promptunda). **Kanıt dolaylı, kesin değil:**
(1) 18/18 replik klip sesinde duyuluyor ve model sesi kusurları taşıyor (takılma, ikileme, alıcı seste aralık dudak); `ODA/SAHIP_PLANI.md` video promptlarının hepsi "No dialogue or music; generate only the specified effects and ambience. All spoken lines will be added in the edit." der → plan promptuyla Omni konuşma üretmezdi.
(2) mont. C19 (= hat C20) "eldivenli sağ el": güncel G03 "A right white glove is already wrapped around the orange grip"; önceki sürüm `ODA/F5_goruntu-yonetmeni_1_G03.md` ve plan K20 "left white glove" (Gemini'nin "sağ"ı kadraj sağı da olabilir).
(3) NOTLAR DENEMELER yalnız şablon satırları; `~/film_medya/THE_MAYDAY_SEA/` altında ref · kare · ham boş → hangi deneme, hangi referans yüklendi kaydı yok; sahibin kendi düzenlemesi dışlanamaz.
Sınıflamayı taşıyan alıntılar önceki sürümde de aynı: C14 "Small old wrecks lie caught against that same network" · C08 "hesitant voice" · C19 "droplets shaking loose".

Yöntem notları:
- **Montaj hat sırasından bir kaymış:** hat C05 (kelepçe kapanır) montajda YOK. Rapordaki C01-C04 = hat C01-C04; rapordaki C05…C23 = hat C06…C24; rapordaki C24 = başlık kartı. Eşleme içerikle ve replik zamanlarıyla yapıldı (R06 00:45 · R07 00:55 · R08 01:04 · R09 01:34 · R10 01:44 · R11 01:55 · R12 02:13 · R13 02:22 · R14 02:43 · R15 02:53 · R16 03:23 · R17 03:32 · R18 03:43: hepsi "çapa: içerik"). Tabloda **çekim = hat numarası**, rapor sütununda montaj numarası `mont.` diye.
- `timeline.json` boş şablon (`FILM_ADI`) → `kurgu.py` ile eşleme yapılamadı; zaman aritmetiği yok.
- Montaja bakan iki belge de (`ODA/QA_DEGERLENDIRME…` ve NOTLAR KARARLAR) montaj numarasını hat numarası sanıyor. Aynı kayma 16.10 kılavuz taslaklarında da var: UZAY_FIZIGI_GORUNTU §0 "MAYDAY C06/C18/C19/C20" = hat C07/C19/C20/C21; GPT_IMAGE_OMNI §6 "MAYDAY C11 kablo" = hat C12. Hat C12'nin promptunda kablo yok, `narrow dark teal liquid ribbon` var (#25).
- 🅓 bu dosyada yalnız **prompt dışı** bulgular için kullanıldı: müzik, miks ve tempo, ki hiçbiri bir promptun ürünü değil. QA_OKUMA bu sınıfta doğduğu yere "—" yazdırıyor; müdahale yeri kaybolmasın diye burada "kurgu" yazıldı. Bu satırlar paydada yok.
- Raporlar arası çelişki: C23 03:32'de Anlatım A6 "dudaklar hafif aralık" diyor, İzleme A4 "ağız ve çenede tepki yok" diyor. İki ayrı satır olarak yazıldı (#43, #44). Video izlenmedi, bütün satırlarda **insan doğrulaması: ?**.
- Rapor kusur saymadı ama prompttan sapan iki şey var:
  - mont. C05 (= hat C06) "koridorun sonundaki pencereye doğru yürümektedir"; prompt "she stands planted … her boots still planted" diyor.
  - R01 transkriptte 00:03'te; prompt "Starting within the first second" diyor.

## BULGULAR
| # | çekim | rapor (bölüm · zaman) | bulgu (≤15 kelime) | tür | sınıf | promptta ne yazıyor — Görsel / Video (≤25 kelime birebir alıntı ya da "YOK") | doğduğu yer | not (≤15 kelime) |
|:--:|:--:|---|---|---|:--:|---|:--:|---|
| 1 | C01 | Tarama #1 · 00:04.5 | Vakum dış planında okyanus dalgalanma, su çalkalanma sesi | ortama aykırı ses | 🅐 | V: "The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static." | ses | Görünür dalga sesi çekmiş olabilir; FILM §6 vakum penceresi montajda uygulanmadı |
| 2 | C02 | Anlatım §7 transkript · 00:15 (türev) | Mara "Rescue vessel. Rescue vessel, I hear you." — hitap ikilendi | replik tekrarı/ses | 🅐 | V: "she says in an adult woman's voice, warm and low, professional: Rescue vessel. I hear you." | ses | C12/C23 taklitleri tek "Rescue vessel": "aynı cümle" vaadi kırıldı |
| 3 | C02 | Süreklilik #10 · 02:38.4 ("C02'de arma yok") | Sol göğüs rozeti yok | giysi/işaret/arma/bant | 🅐 | G: "a single circular gold-and-blue mission badge with an abstract triangle on her left chest sits at the lower right of the frame" | kare | İstendi, çıkmadı; ref yüklendiği bilinmiyor |
| 4 | C03 | Anlatım A1 · 00:24 · İzleme A1 · B1-5 · B1-6 | AI sesi kazazede çağrısıyla aynı tonda; konuşan belirsiz | replik tekrarı/ses | 🅑 | V: "a calm adult man's voice, even and unhurried, over the comms" / C02: "a tired man's voice, softened by a light radio filter" | anlatım | İki erkek telsiz sesi yalnız sıfatla ayrılıyor; "gemi AI'ı" kimliği hiçbir promptta yok |
| 5 | C03 | Tarama #2 · 00:19.2 | Vakum dış planında su vurma, çalkalanma sesi | ortama aykırı ses | 🅐 | V: "The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static." | ses | "small ripples ring the submerged halves" görünür hareket; kurgu penceresi yok |
| 6 | C03→C04 | Süreklilik #1 · 00:29.2 (k3) | C03'te iki dev kıskaç kolu, C04'te dört küçük kıvrık parça | ekipman/nesne biçimi | 🅑+ | G C03: "a single hinged clamp open beside it" / G C04: "The station's single hinged clamp stands open." | kare | "clamp" iki çene çağırır, biçim yok; C04'teki parçalar muhtemelen "four short rigid mounts" |
| 7 | C04 | Anlatım A2 · 00:34 | "Dock above the waterline" küçük hareketsiz pilot figürüyle örtüşmüyor | hikâye/anlatım | 🅑 | V: "a calm adult man's voice, even and unhurried, over the comms says: Dock above the waterline." | anlatım | Kadraj dışındaki erkek ses, kadrajdaki kadın pilota yamanıyor; AI kurulmadı (#4) |
| 8 | C04 | Tarama #3 · 00:29.2 | Vakumda metal kenetlenme tıkırtısı, su/motor uğultusu | ortama aykırı ses | 🅐 | V: "The only ambient sound is a low, steady, non-diegetic pressure tone with a faint bed of radio static." | ses | Temas bu çekimde yok ("thin gap left"); tık sesi modelin |
| 9 | C06 | Süreklilik #2 · 00:39.2 (k4, mont. C05) · İzleme A2 00:40 | Omuz zırhı lacivertten beyaza döndü | giysi/işaret/arma/bant | 🅐 | G: "an adult woman in an ivory-white pressure suit with graphite joint seals and dark navy shoulder armor" | kare | Kimlik tabanı birebir; tam boy 24 mm geniş planda kaydı |
| 10 | C06 | Süreklilik #2 · İzleme A2 00:40 | Kolların üst ve alt kısmında turuncu şeritler beliriyor | giysi/işaret/arma/bant | 🅐 | G: "with narrow burnt-orange forearm bands, white gloves and black boots" | kare | Ön kol bandı tasarım (C02'de kol kadraj dışı); üst kol sapma; sayı yok |
| 11 | C06 | Süreklilik #2 · İzleme A2 00:40 | Kask yan bağlantısı yuvarlak siyah yuva; vizör çerçevesi değişti | giysi/işaret/arma/bant | 🅑 | G: "a round ivory helmet with a completely clear closed visor" — kask donanımı YOK | kare | Vizör çerçevesi, yan bağlantı, üst parça 24 promptun hiçbirinde tanımlı değil |
| 12 | C06 | Süreklilik #2 · 00:39.2 | Göğüs askıları kayboldu | giysi/işaret/arma/bant | 🅒 | C02 G: "strapped into the pilot seat of a small rescue pod" | — | C02'deki askı koltuk kemeri; koridorda olmaması doğru |
| 13 | C06→C07 | Süreklilik #3 · 00:49.2 (k5) | Dolapta önce gri çanta/raf, sonra paslı verici kutusu | dünya/arka plan | 🅑 | G C06: "the hinged service cabinet on the left wall stands open" — içerik YOK | kare | İçerik yalnız ref 6 panelinde; C06 metni adlandırmıyor |
| 14 | C07 | Tarama #4 · 00:50.0 (mont. C06) · İzleme A3 00:50 | Çekik fişin ucundan sürekli su damlıyor | parçacık/duman/alev/sıvı | 🅑+ | G: "one small drop clings to the cabinet's lower edge" / V: "The drop slides down the cabinet edge and falls" | hareket | Ortam cümlesi "sparse distant water drips" de damla çağırıyor; kaynak fişe kaydı |
| 15 | C08 | Süreklilik #4 · 00:59.2 (k6, mont. C07) | Lacivert omuzluk geri döndü | giysi/işaret/arma/bant | 🅒 | G: "an adult woman in an ivory-white pressure suit with graphite joint seals and dark navy shoulder armor" | — | C08 istenen hâlde; sapma C06'da (#9) |
| 16 | C08 | Süreklilik #4 · 00:59.2 | Koridorda siyah göğüs askıları | giysi/işaret/arma/bant | 🅑 | YOK (askı ya da sırt paketi kayışı tarifi yok) | kare | Ref 1'deki "compact life-support pack" kayışı olabilir; tanımsız |
| 17 | C08 | Süreklilik #4 · 00:59.2 | Sağ yanakta "yeni" çizik ve yaralar | yüz/kimlik | 🅒 | G: "Her grey eyes and the small pale scar on her right cheekbone are plainly visible behind the clear visor." | — | Sağ elmacık yarası tasarım; çoğul yaraysa 🅐, insan doğrulaması ? |
| 18 | C07→C08 | Süreklilik #5 · 00:59.2 (k6) | Siyah verici yerine beyaz şalterler ve kırmızı şeritli kablo | ekipman/nesne biçimi | 🅐 | G C08: "the transmitter module with its hanging grey plug" / "The cabinet edge and the hanging grey plug are soft in the background behind her." | kare | Modül yalnız Reference satırında; gövdede yok, arka plan bulanık |
| 19 | C08 | Anlatım A3 · 01:04 · Tarama #5 · İzleme A5 · B1-5 | "Then who is call— is calling?" takılma | replik tekrarı/ses | 🅑+ | V: "she says in an adult woman's voice, warm and low, hesitant: Then who is calling?" | ses | "hesitant" duraksama ve yeniden başlama çağırır; insan doğrulaması ? |
| 20 | C09 | Tarama #6 · 01:08.8 (mont. C08) | Boş, su dolu kasktan sürekli hava kabarcığı | parçacık/duman/alev/sıvı | 🅑+ | G: "a few tiny bubbles rise beside it" / V: "the tiny bubbles beside it beginning to rise in a thin trail" | hareket | Kabarcık istendi; model kaynağı kaska bağladı, sürekli yaptı |
| 21 | C09–C11 | İzleme A6 · 01:12–01:39 | Gerilime uymayan hızlı tempolu synth müzik | diğer | 🅓 | YOK (müzik kurguda eklendi) | kurgu | Prompt dışı; müzik üç klibi aşıyor |
| 22 | C10 · C17 | İzleme A7 · 01:19 + 02:29 · B1-7 | İki benzer yavaş sıvı planı tempoyu düşürüyor | hikâye/anlatım | 🅓 | V C10: "The ribbon creeps a little higher at a slowing pace" | kurgu | Prompt dışı tempo; yavaşlık plan tasarımı, kırpma kurguda |
| 23 | C11 | Tarama #7 · 01:28.4 (mont. C10) | Ağır gemiler suda ne batıyor ne yükseliyor | yerçekimi/fizik | 🅒 | G: "The dark water beyond the glass holds wrecks at separate depths" / V: "every hull stays rigid and separate" | — | Tasarım: alanda asılı filo. "Savaş uçağı" = "short swept wings" okuması olası |
| 24 | C11→C12 | Süreklilik #6 · 01:38.4 (k10) · Tarama #8 · İzleme A6 01:39 | Müzik kesmede bıçak gibi kesiliyor | diğer | 🅓 | YOK (müzik promptta yok) | kurgu | Prompt dışı; SECIM_VE_KURGU "müzik kesmede kesilmez" |
| 25 | C12 | Tarama #9 · 01:44.0 (mont. C11) | Camgöbeği "kablo" yoktan belirip sağa uzuyor | parçacık/duman/alev/sıvı | 🅐 (geçici) | G: "A narrow dark teal liquid ribbon lies along the console's rear edge behind the receiver" / V: "makes one small ripple that keeps its shape" | hareket | Şerit mi kablo mu? Kabloysa 🅑; insan doğrulaması ? |
| 26 | C13 | Süreklilik #7 · 01:48.4 (k11, mont. C12) · İzleme A2 01:49 | Kask aniden çizik, kirli, boyası dökük; üst siyah parça yok | giysi/işaret/arma/bant | 🅑 | G: "a round ivory helmet with a completely clear closed visor" — temiz ya da yıpranmamış hâl YOK | kare | Kaskın yüzey durumu ve donanımı tanımsız (#11 ile aynı boşluk) |
| 27 | C13 | Süreklilik #7 · İzleme A2 01:49 | İki yanakta belirgin yara izi | yüz/kimlik | 🅐 | G: "her right cheekbone with its small pale scar and her grey eyes show plainly behind the clear visor" | kare | Taraf yazılı; model yarayı iki yanağa çoğalttı |
| 28 | C13 | Süreklilik #8 · 01:48.4 (k11) | Pencere ardında turkuaz deniz tabanı, mercan sütunları, kablolar | dünya/arka plan | 🅑 | G: "Behind her the broad window carries a soft cyan water reflection" — pencere içeriği YOK | kare | FILM §3 "kara/deniz tabanı yok" bu çekime yazılmadı |
| 29 | C14 | Anlatım A4 · 01:59 · Tarama #10 · Süreklilik #9 · İzleme A1/A3 · B1-6 | Okyanusta fenerli ahşap yelkenli kalyonlar | dünya/arka plan | 🅑+ | G: "Small old wrecks lie caught against that same network." | kare | C01'deki "old spacecraft wrecks" ifadesinden "spacecraft" düşmüş → deniz batığı |
| 30 | C18 | Süreklilik #10 · 02:38.4 (k16, mont. C17) · İzleme A2 02:39 | Sol göğüste yuvarlak lacivert-sarı arma beliriyor | giysi/işaret/arma/bant | 🅒 | G: "A single circular gold-and-blue mission badge with an abstract triangle on her left chest marks her suit." | — | Tasarım rozeti; asıl kusur C02'de yokluğu (#3) |
| 31 | C18 | İzleme A4 + A5 · 02:43 | "Emergency separation. Now." fazla sakin, yüz tepkisiz | replik tekrarı/ses | 🅑+ | V: "draws one controlled breath" / "says firmly in an adult woman's voice, warm and low" / "close, calm breathing inside the helmet" | ses | Acil repliği sakinlik kelimeleri sarıyor; Mara sesinin sabit tarifi "warm and low" |
| 32 | C19 | Tarama #11 · 02:48.4 (mont. C18) · İzleme A6 02:49 | Vakumda sıvı akışı ve su damlama sesleri | ortama aykırı ses | 🅑+ | V: "a few small droplets shake loose on the station side" / "The only ambient sound is a low, steady, non-diegetic pressure tone" | ses | Damla olayını hat ekledi (plan "stay"); ses kilidi tutmadı |
| 33 | C19 | Tarama #12 · 02:55.0 · İzleme A3 02:55 | Halkadaki sıvıdan yerçekimiyle aşağı damlalar kopuyor | parçacık/duman/alev/sıvı | 🅑+ | V: "a few small droplets shake loose on the station side" | hareket | Plan "Small droplets stay on the station side" demişti; fiil değişti |
| 34 | C20 | Tarama #13 · 02:58.4 (mont. C19) | Kapalı kokpitte panele yağmur gibi su damlıyor | parçacık/duman/alev/sıvı | 🅑+ | G: "The light is cool blue water reflections from the canopy at frame-left" / ortak: "realistic metal and wet-surface detail" | hareket | C20'de "cabin is dry" yok (C02/C18/C23'te var); kanopi kadrajda değil |
| 35 | C20 | Tarama #14 · 02:58.4 · İzleme A4 02:59 | Kol birkaç cm oynuyor, el titriyor, efor yok | el-nesne | 🅑+ | V: "the lever starting to rock out of its upright rest on its hinge" / "pulls it in one smooth, firm arc" | hareket | "rock" sallanma, "smooth" eforsuzluk çağırır; ama "reaches the mechanical stop" de yazılı |
| 36 | C21 | Tarama #15 · 03:08.4 (mont. C20) · İzleme A3 03:09 | Arka iticiler sağa ateşlerken kapsül sağa kayıyor | yerçekimi/fizik | 🅑+ | G: "its two vertically stacked blue-white rear thrusters at the far right" / V: "begins to slide slowly to the right, away from the station" | hareket | Geri çekilmede itki kaynağı yazılmamış; "blue-white" yanan itici okunur |
| 37 | C21 | Tarama #16 · 03:14.0 | Dört bağlantı çubuğu halkanın deliksiz düz yüzünden çıkıyor | ekipman/nesne biçimi | 🅑 | G: "a narrow new gap has just opened between this ring and the pod's four short rigid mounts" — arayüz YOK | hareket | Bağlantıların halkaya nasıl oturduğu (yuva) yazılmamış; LIKELY |
| 38 | C21 | Süreklilik #12 · 03:18.4 (k20) | Kapsül penceresiz kısa silindir; C22'de kanopi beliriyor | ekipman/nesne biçimi | 🅑 | G: "take the wingless ivory-and-graphite hull, the burnt-orange nose band, the four short bare mounts" — kanopi YOK | kare | "broad dark canopy" yalnız C22 metninde |
| 39 | C22 | Süreklilik #12 · 03:18.4 (mont. C21) | Okyanusu köşeli kirişler yerine dairesel halka çerçeve sarıyor | dünya/arka plan | 🅐 | G: "the enormous flat oval ocean hangs within its three black rectangular frames" | kare | Sayı ve biçim yazılıydı |
| 40 | C22 | Süreklilik #11 · 03:18.4 (k20) | Kapsül sağ üstteki istasyondan sol alta, kameraya uzaklaşıyor | yön/180°/koltuk | 🅐 | G: "its nose pointing toward frame-right and away from the camera" / "At frame-left, behind the pod, the enormous flat oval ocean" | kare | C21 sağa çekiliyor; C22'de ekran yönü ters döndü |
| 41 | C22 | Tarama #17 · 03:18.4 | Vakumda güçlü motor ve itici uğultusu | ortama aykırı ses | 🅐 | V: "its two rear thrusters keeping their shape" / "The only ambient sound is a low, steady, non-diegetic pressure tone" | ses | "glow/accelerate" bilerek yazılmadı; FILM §6 motor sesini öngörmüştü |
| 42 | C22 | Anlatım A5 · 03:23 · İzleme A6 03:23 · B1-5 | "We're clear of the field" müzik altında boğuk | replik tekrarı/ses | 🅓 | YOK (miks kurguda) | kurgu | Prompt dışı; #41'deki motor uğultusu da maskeliyor |
| 43 | C23 | Anlatım A6 · 03:32 (mont. C22) | Ses alıcıdan gelirken dudaklar aralık; kim konuşuyor belirsiz | replik tekrarı/ses | 🅐 | G: "her lips are closed" / V: "her mouth stays closed and her eyes lower toward the toggle while the receiver at frame-right plays" | hareket | REPLIK §1'de bilinen risk; ağzın kapalı kaldığı aralık seçilir |
| 44 | C23 | İzleme A4 · 03:32 | Kendi sesini duyunca ağız ve çenede tepki yok | diğer | 🅒 | V: "her breath eases out slowly and her shoulders settle as she looks at the dark indicator, her mouth still closed" | — | Sakin karar tasarımı; göz tepkisi kadraj dışında (#45) |
| 45 | C23 | Süreklilik kesme listesi 21 · Tarama COULD NOT CHECK · Anlatım A6 (türev) | Kadraj burun hizasından kesik; gözler ve kask üstü yok | kamera/kadraj | 🅐 | G: "Her grey eyes and the small pale scar on her right cheekbone are plainly visible behind the clear visor" | kare | Rapor kusur saymadı; #44'teki "tepkisiz" algısının olası nedeni |
| 46 | C23 | Süreklilik #13 · 03:28.4 (k21, mont. C22) | Omuzluk, arma ve sol kolda iki turuncu şerit birlikte | giysi/işaret/arma/bant | 🅒 | G: "She wears narrow burnt-orange forearm bands, white gloves and a single circular gold-and-blue mission badge" | — | Tasarım ekleri; C18'de ön kol kadraj dışı. "İki" bant: sayı yazılmamış |
| 47 | kart (hat dışı) | Tarama #18 + #19 · 03:48.4 (mont. C24) | Sonda sabit afiş/başlık kartı ve "THE MAYDAY SEA" yazısı | istenmeyen yazı/bayrak | 🅒 | YOK (kart montajda eklendi) | — | Post başlık kartı (QA_OKUMA §1); planda 2 s, montajda 5,8 s |

## ÖZET
- **Sınıf (tekil 47):** 🅐 15 (türev 2 dahil) · 🅑 9 · 🅑+ 11 · 🅒 8 · 🅓 4 (dördü de prompt dışı: müzik ×2, tempo, miks).
- **🅑 oranı** (sözleşme v1.0, sınıf sütunu, payda 🅐+🅑+🅑+): (9 + 11) / (15 + 9 + 11) = 20 / 35 = **%57**. Türevler hariç: 20 / 33 = %61.
- **En sık 5 tür:**

  | Tür | Bulgu |
  |---|:--:|
  | giysi/işaret/arma/bant | 10 |
  | replik tekrarı/ses | 6 |
  | ortama aykırı ses | 5 |
  | parçacık/duman/alev/sıvı | 5 |
  | ekipman/nesne biçimi | 4 (dünya/arka plan da 4) |

- **Doğduğu yer:** kare 16 · hareket 9 · ses 8 · kurgu 4 · anlatım 2 · — 8.

  | Sınıf | Doğduğu yer |
  |:--:|---|
  | 🅐 | kare 8 · ses 5 · hareket 2 |
  | 🅑+ | hareket 6 · ses 3 · kare 2 |
  | 🅑 | kare 6 · anlatım 2 · hareket 1 |

- Vakum seslerinin beşi (#1 #5 #8 #41 🅐, #32 🅑+) klip sesinde doğdu; finale ulaşmalarının nedeni kurgu. FILM §6 kuralı "dış kliplerde klip sesi yalnız replik penceresinde" diyor; montajda uygulanmamış.

## PROMPT METNİNİN KENDİ KUSURLARI (bulgudan bağımsız; 24 çekimin tamamı okundu)

**Su kelimesi her yere sızıyor**
1. **Islaklık ortak cümlede.** ORTAK GÖRÜNÜM 48/48 promptun sonunda "realistic metal and wet-surface detail" der. Kuru kokpitte (C02 C18 C20 C23) ve vakumda da aynı cümle var. C02 aynı promptta "the cabin is dry" der: ıslak yüzey isteği ile kuru kabin kilidi çatışıyor (#34).
2. **Kokpit ışığı su anıyor.** KOKPİT MEKÂN IŞIĞI 4/4 kokpit görselinde "The light is cool blue water reflections from the canopy at frame-left".
   - C23 aynı Görsel'de "Through the canopy only distant stars and one small faint blue glow of the distant containment field remain." der: dışarıda su yokken su yansıması. Görsel kendi içinde çelişiyor.
   - C20 tight insert'tir, kanopi kadrajda değil, "dry" kilidi de yok (#34).
3. **İstasyon ortam sesi damla imgesi taşıyor.** 9 video promptunda (C06-C13, C17) "The only ambient sound is a low, steady pressure-system ventilation hum with sparse distant water drips." var. C07'de "The drop slides down the cabinet edge and falls" ile birleşince fişten sürekli damlama doğdu (#14).
4. **Görünmeyen şeye atıf.** İSTASYON IŞIĞI "cool cyan light from the wet floor and the window" C06, C07, C08, C10 ve C17'de yazılı; bu koridor/dolap kadrajlarında pencere yok. G03 C17 notu da bunu kabul ediyor.

**Ses ve görüntü çelişkisi**
5. **Vakumdaki kameraya su altı sesi.** C14 Görsel "the camera in open space beneath the floating ocean" der, Video "The only ambient sound is a deep, slow waterborne resonance with no rhythm." der. Kamera vakumda, ses su içinden geliyor. Devamlilik B17 bunu "tasarım" diye geçti.

**Aynı nesne çekimden çekime farklı kelimeyle**
6. **Enkaz.**
   - C01: "Two old spacecraft wrecks are readable just below the near surface."
   - C14: "Small old wrecks lie caught against that same network." (ref 4 `underside panel` da "small old wrecks")
   - C15: "old wrecks lie below the surface"
   - C24: "many old spacecraft of different sizes and eras"
   - C11: "a small white shuttle with short swept wings"

   "spacecraft" iki çekimde düşüyor; C14'te bu yelkenli kalyon olarak çıktı (#29). "Swept wings" savaş uçağı okumasına açık.
7. **Kapsül.**
   - C04: "the wingless ivory-and-graphite hull, the burnt-orange nose band, the dark docking ring on its four short rigid mounts"
   - C21: "the wingless ivory-and-graphite hull, the burnt-orange nose band, the four short bare mounts"
   - C22: "the wingless boat-shaped graphite hull with its curved ivory armor panels, the burnt-orange band, the broad dark canopy"

   Kanopi ve "boat-shaped" yalnız C22'de. C21 kapsülü penceresiz silindir oldu (#38).
8. **Kelepçe biçimsiz.** C03 "a single hinged clamp open beside it" · C04 "The station's single hinged clamp stands open." · C05/C19/C21 "single broad (rigid) hinged clamp". Sayı kilitli ama biçim yok: "clamp" iki çeneli kıskaç çağırıyor (#6).

**Kimlik ekleri eksik tanımlı**
9. Kimlik tabanı 6/6 Mara çekiminde birebir (C02 C06 C08 C13 C18 C23). Ama ekler sayısız ve biçimsiz:
   - "narrow burnt-orange forearm bands" (C06 C20 C23): kaç bant olduğu yazılmamış.
   - Kask "a round ivory helmet with a completely clear closed visor": vizör çerçevesi, yan bağlantı ve üst parça tanımsız.
   - Rozet cümlesi Mara çekimlerinin yalnız 3/7'sinde.
   - "the only marking on the suit" kilidi 0/24.

   Sonuç: omuz, bant, kask, askı ve rozet her karede yeniden icat edildi (#9-#12, #16, #26, #30, #46).

**Replik ve ses tarifleri**
10. **İki erkek telsiz sesi yalnız ruh hâliyle ayrılıyor.**
    - AI: "a calm adult man's voice, even and unhurried, over the comms" (8 çekim)
    - Çağrı: "a tired man's voice, softened by a light radio filter" (C02 C07)

    İkisi de erkek, ikisi de telsizden; konuşanın "gemi bilgisayarı" olduğu hiçbir promptta yok (#4, #7).
11. **Aynı cümle birden çok promptta.** "Mayday. Please. Come closer." C02 ve C07'de; "Rescue vessel. I hear you." C02, C12 ve C23'te. Bu tasarım gereği.
    - Omni sesi klipten klibe taşımıyor. FILM §5 kurguda yedek yöntem yazmıştı (C02 sesi C07/C12/C23'e); montajda uygulanmadı.
    - Model C02'deki asıl cümleyi ikiledi ("Rescue vessel. Rescue vessel, I hear you."), taklitler tek kaldı. Kaynak ile kopya artık aynı cümle değil (#2).
12. **Mara'nın ses tarifi sabit, sıfatlar teslimi bozuyor.** "an adult woman's voice, warm and low" + tek sıfat bütün repliklerde var.
    - C08 "hesitant" takılma çağırıyor (#19).
    - C18'de acil replik sakinlik kelimeleriyle çevrili: "draws one controlled breath" · "says firmly in an adult woman's voice, warm and low" · "her breathing steady" · ortam "close, calm breathing inside the helmet" (#31).

**Hareket fiilleri istenmeyen fiziği çağırıyor**
13. Dört örnek:
    - C19 "a few small droplets shake loose on the station side" (plan "Small droplets stay on the station side" idi)
    - C09 "the tiny bubbles beside it beginning to rise in a thin trail"
    - C20 "the lever starting to rock out of its upright rest on its hinge" + "one smooth, firm arc"
    - C21 geri çekilen kapsülde "two vertically stacked blue-white rear thrusters at the far right"

    Bunlar #20, #33, #35 ve #36'yı çağırdı.

**Daha küçük kusurlar**
14. **Zihinsel ve soyut ifade:** C02 "grey eyes attentive with cautious concern" · C12 "as if the receiver were picking up a signal". Küçük kusur; bulguya bağlanmadı.
15. **Uzunluk sorun değil.** Görsel 1.194-1.960 karakter (en uzunlar C23 1.960, C21 1.943, C19 1.921), Video 807-1.192. ORTAK GÖRÜNÜM her promptta 212 karakter; hepsi 4.300 sınırının altında.
16. **Meta etiket ve referans rolleri temiz.**
    - Prompt gövdelerinde meta etiket yok: 48/48 blokta Cxx, Scene, Clip, Rxx, Kxx sıfır.
    - `Reference <No> (<rol>)` anahtarı 49 kez geçiyor, rol adları film boyu tutarlı (1 woman · 2 rescue pod · … · 9 living water).
    - Ancak `ref/` klasörü boş. Referans yüklenmediyse "take X from it, using the Y panel" cümlesi hiçbir şeye bağlanmıyor; bu da görünmeyen şeye atıf olur.

## HAT KURALLARI BU FİLMDE (her biri: kaç çekimde yazılı · yine de bulgu çıktı mı, kaç)
| Kural | Kaç çekimde yazılı | Yine de çıkan bulgu |
|---|---|---|
| **ORTAK GÖRÜNÜM birebir** | 48/48 (24 Görsel + 24 Video) | Stil cümlesi kimlik ya da dünya kilidi değil. İçindeki "wet-surface detail" #34'e (ve #14'e) katkı. |
| **"Reference <No>" anahtarı** | 24/24 Görsel, 49 anahtar; Mara'nın 7 çekiminde Reference 1 | Mara çekimlerinde 7 gerçek kimlik bulgusu (🅐 4: #3 #9 #10 #27 · 🅑 3: #11 #16 #26). Referansın yüklendiği doğrulanamıyor. |
| **Asimetrik işaret** | Rozet "on her left chest" 3 çekim (C02 C18 C23) · yara "right cheekbone" 5 (C02 C08 C13 C18 C23) · bant "forearm" 3 (C06 C20 C23; taraf ve sayı yok) | 3: #3 rozet yok · #27 yara iki yanakta · #10 üst kolda şerit. Ayrıca 3 🅒 (#17 #30 #46): QA tasarımı kusur sandı. |
| **Koltuk/taraf (K2)** | 3/3 kokpit (C18 "beside her right shoulder" · C20 "A right white glove" · C23 "her left white glove") | 0. QA C20'de "sağ el" gördü. |
| **10 s vuruş planı** | 24/24 Video | 17/18 replik kendi vuruşunda duyuldu (transkript saniyesi, montaj başına göre). R01 ≈2 s geç (00:03; "Starting within the first second"). Ayrı bulgu çıkmadı. |
| **Model sesi / replik satırı** | 18 replik, 17 Video promptunda birebir (`says:` / `plays …:`) | 18/18 duyuldu, metin doğru. Yine de 6 ses bulgusu: #2 ikileme · #19 takılma · #31 ton · #4 #7 ses kimliği · #43 dudak. Aynı-ses yedeği (FILM §5) uygulanmadı. |
| **Vakum ses/parçacık kuralı** | DIŞ UZAY ortam cümlesi 9/9 dış Video (C01 C03 C04 C05 C15 C19 C21 C22 C24) · FILM §6 klip sesi penceresi (kurgu) · kokpit "dry" 3/4 Görsel (C20 yok) | Ses 5 (#1 #5 #8 #32 #41) · parçacık/sıvı 4 (#14 #20 #33 #34) · ters itki 1 (#36). Cümle kilidi tutmuyor; kurgu kuralı montajda uygulanmadı. |
| **Yazı/bayrak olumlu kilidi ("the only marking")** | 0/24 (yerine "plain unmarked surfaces/controls/shapes") | Çekim içinde yazı 0. Kart (#47) 🅒. |

## DERS ADAYLARI (en çok 8)
1. **Prompt yazarken:** kuru mekânın ortak ve mekân cümlelerinde su kelimesi kullanma (ORTAK GÖRÜNÜM'de "wet-surface", kokpit ışığında "water reflections", istasyon ortam sesinde "water drips"); kokpit ışığını kaynağıyla yaz ve her kokpit görseline "the cabin is dry" ekle.
   - Dayanak: #34, #14.
   - Bu filmde kapatırdı: 1-2.
   - Hat kuralı mı: kısmen. UZAY_FIZIGI_GORUNTU §3 (16.10 taslak, commit yok) "kokpitte damla yazılmaz" diyor, ama ortak cümlelerdeki su kelimesini görmüyor. Ortak cümle kısmı yeni.
2. **Prompt yazarken:** istenmeyen fiziği çağıran fiil yazma ("droplets shake loose", "bubbles … rise in a thin trail", "drop … falls", "rock out of its rest", "smooth arc", geri çekilen gemide "blue-white rear thrusters"); hedef hâli olumlu yaz (sıvı tek parça ve yüzeye yapışık, arka itici sönük, kolda direnç).
   - Dayanak: #14, #20, #33, #35, #36 (+#32 sesi).
   - Bu filmde kapatırdı: 5-6.
   - Hat kuralı mı: kısmen. UZAY_FIZIGI §3-§5 taslak (damla, ters itki, efor). "bubbles", "rock" ve "blue-white" yeni.
3. **Prompt yazarken:** nesneyi işlev adıyla değil biçim ve tam adla yaz, ve tasarım kelimesini her çekimde tekrarla ("old spacecraft wrecks"; "clamp" yerine "one curved latch arm hinged at its top"; kapsülün "broad dark canopy" ifadesi her kapsül çekiminde).
   - Dayanak: #6, #29, #38.
   - Bu filmde kapatırdı: 3.
   - Hat kuralı mı: yeni. KIMLIK_VE_REFERANS §4 sayılı ve biçimli tarifi yalnız giysi için istiyor.
4. **Prompt yazarken:** replik sıfatını söyleyişi bozmayacak şekilde seç ("hesitant" takılma çağırır) ve acil replikte o çekimden sakinlik kelimelerini çıkar ("controlled breath", "breathing steady", ortam cümlesindeki "calm breathing").
   - Dayanak: #19, #31.
   - Bu filmde kapatırdı: 2.
   - Hat kuralı mı: yeni. REPLIK_VE_KLIP_SESI §3 takılmayı risk sayar ama sıfatı değil. Film içi K7 "sabit ses tarifi + tek duygu sıfatı" bu kusuru çağırdı.
5. **Prompt yazarken:** aynı cinsiyetten iki telsiz sesi varsa konuşanın kimliğini promptta yaz ("the pod's onboard computer voice" ↔ "a distant survivor's voice"). Ama asıl müdahale kayıt ya da filtre, çünkü metin tarifi ses kimliğini kilitlemiyor.
   - Dayanak: #4, #7.
   - Bu filmde kapatırdı: 2 (anlatım).
   - Hat kuralı mı: zaten taslakta. REPLIK §2 madde 4 ve GPT_IMAGE_OMNI satır 285-286 (16.10, commit yok).
6. **Prompt yazarken:** kimlik eklerini sayı, konum ve donanımla yaz ("one narrow burnt-orange band around each forearm", kask kabuğu ve vizör çerçevesi tek cümleyle, "the only marking on the suit").
   - Dayanak: #11, #16, #26 (🅑).
   - Bu filmde kapatırdı: 3.
   - #10 🅐'dır ("forearm" yazılıydı); oraya müdahale kare onayı, prompta ekleme değil.
   - Hat kuralı mı: zaten taslakta. KIMLIK_VE_REFERANS §4 (16.10, commit yok).
7. **Prompt yazarken:** kadrajda görünecek pencere ve dolap içini her çekimde adıyla yaz ("open dark water with distant wreck silhouettes, no seabed"; "the black transmitter module with its grey plug hanging out"). FILM §3'teki sabit tasarım cümlesi çekime inmezse modele ulaşmıyor.
   - Dayanak: #13, #28 (+#18 🅐: modül yalnız Reference satırındaydı).
   - Bu filmde kapatırdı: 2.
   - Hat kuralı mı: yeni hatta yazılı değil. Eski hattın 19.09 sınıfı 🅑8 (dünya çapası) bunu söylüyordu.
8. **Prompt yazarken değil kurguda ve kare onayında:** kilit cümle zaten birebir yazılı olduğu hâlde model tutmadı.
   - Vakum sesi (#1 #5 #8 #41): klip sesi dış çekimlerde yalnız replik penceresinde açılır (FILM §6 · REPLIK §2 m.6 · §4).
   - Kimlik ve geometri (#3 #9 #27 #39 #40 #45): kare onayı, devamlilik kare modu ve kadraj seçimi (KIMLIK §5 · AGENTS F7).
   - Bu filmde kapatırdı: 10 (prompt dışında).
   - Hat kuralı mı: zaten hat kuralı. Bu montajda uygulanmamış.
