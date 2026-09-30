# 📖 SUSMAYAN_NOBETCI — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 17.09.2026 14:58
> ⛔ **ELLE SATIR EKLENMEZ/SİLİNMEZ** — yeni kılavuz eklenirse betik yeniden koşulur.
>
> **Kural:** her satır okununca `⬜` → `✅` yapılır ve son sütuna
> **bu filme düşen kilit** yazılır. Kilit çıkmadıysa `—` yazılır; boş
> bırakılmaz — boş hücre "okudum" ile "atladım" arasını ayırt ettirmez.
>
> ⭐ Son sütunda yazılan her kilit `01_QA_DERS_HASADI.md` tablosuna taşınır.
> ⛔ ⬜ kalan satır varken `02_KONSEPT_VE_RISK.md` yazılmaz.
> ⛔ 14.09.2026: her satırdan kilit ÇIKMAZ. "—" yazmak meşrudur; sıfır "—"
> çizelgeyi sahte yapar (`prompt_kontrol.py` ㉘ · LOCKED_PULSE 126/126 ölçümü).

### TUR 1 · YAŞAYAN DERSLER — `DERSLER/00_YASAYAN_DERSLER.md` (14.09.2026)

> Film dersi havuzu bu listedir; ders metni ETİKET filme uyuyorsa açılır. ETİKET
> uymuyorsa (`kask` etiketli ders kasksız filmde) satır **"—"** ile geçilir — bu
> "okumadım" değil "bu filme düşmüyor" demektir ve ㉘ kapısı tam bunu bekler.

| ⬜/✅ | ders | ETİKET | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 40 dersin 40'ı etikette düşer (vakum · düşük-g · kask · replik · dış-mekân hepsi doğru); 00_OKUMA_CIKARIMLARI A1 |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | kilit = PLAN sütunu / prompt satırı / SPEC satırı; 'dikkat edilir' yazılmaz |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 48 klip × tek çekim; uydu atışı ve kopma KESMEDE değil klibin içinde (ateşle→vuruş 3 s aynı klip) |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | pilot yüzü vizörde ≤3 öznitelik tek blok; yüz okunan sahneler IN FRAME face ile sınırlı; S46 kasksız yüz tek sahne |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | başlık/jenerik kartı 0; S47 'take ends on the held frame'; film adı ve 'sentry' kelimesi prompta 0 |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | giysi kiri yok (yörünge); DEĞİŞEN yıpranma = S40-S42 dış çıkış sonrası sağ eldiven avucunda metal parlak sürtünme, S42'den sonra sabit |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | özel ad/rol etiketi (pilot · sentry · evac) + lens verisi prompta cümle olarak; [etiket] 0 |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | KESİLEMEZ: S0 · S15 · S30 · S44-S45 · S47; S47 üretim sırasında 3. |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | kurgu kapısı: klip = sahne = 48 · 480 s · ekran metni 0 s · jenerik 0 |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | üç sayaç tek karede sayılır: penceredeki fener 3→2→1→0 · soğuk gaz ibresi · uydu kanadı açık/kapalı; gezegen kenarı-uydu ışığı mesafesi aynı kadrajda |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | metin yasağı kokpit ekranı/ibre/gövde/uydu kapsamıyla; ibre RAKAMSIZ; 'üç saniye' promptta süre olarak TIMELINE'da, ekranda sayaç yok |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | S40-S42 dış çıkış sırttan görünür → pozitif sırt cümlesi (tek düz yaşam destek kutusu, ölçüsüyle) — 'no backpack' değil |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | FİNAL VURUŞ KANITI S47: boş kapsül yuvası ×1 + kurtarma gemisi motor ışığı ×1 + uydu ışığı ×1 aynı karede |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | 🔴 ref paketi YOK (sahip) → vizör biçimi metinle tutmaz; kask yalnız sırttan/profil + S46 kask açık; D74 gerekçe + 04_UYARI |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | TEK KARE: 'motoru yanan nesne vurulur, soğutma kanatları açıkken vurulmaz' — S3 aynı karede kanatlar açık + yanan arka yarı |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | pilot ≤3 öznitelik; tahliyedekiler (ses + S46 tek el) tarif 0 |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | efor sahneleri S20-S21 halat · S38 kelepçe · S40-S42 dış çıkış · S44 G yüklemesi → gövde tepkisi cümlesi |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | halat (S20-S21) ve hava hortumu (S43) ASKI değil eylem nesnesi; kadrajda başka sarkan kablo yok |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | yön nesneyle: 'toward the evacuation ship's ring' · 'toward the planet's edge' · uydu hep gezegen kenarının ÜSTÜNDE |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | mühürlü giysi: 'through the glove' 0; çıplak deri negatifi üç bölge; S46 kask açık → yalnız yüz/boyun açık, eldiven takılı |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | gezegen/uzay/gövde rengi tek cümle tek renk; kontrast öznenin kendi ışığıyla |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IMAGE t=0: S15 motor henüz yanmıyor · S30 kapsül hâlâ yuvada · S45 motor bölümü hâlâ bağlı · S16 enkaz henüz geçmedi |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | vakum sessizliği modelden istenmez; S45 kopma sonrası sessizlik KURGUDA; AUDIO satırı kokpit içi sesle dolu |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | 1 no. risk = UYDU ATIŞI GÖRÜNÜŞÜ: ışın/lazer/alev/ateş topu yerine pozitif biçim + sayı (tek beyaz çakma ≤4 kare + dikişten ayrılma + buz kristali konisi) |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | SPEC C IŞIK TAKVİMİ: güneş tek yön sabit (saat + K) · pratik: tahliye fener sayısı monotonik azalır · kokpit ışığı S45 sonrası kısık |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | 0 g: enkaz/kapsül parçası/motor bölümü dönme ekseni + derece/s yazılır; hiç yüzen nesne donuk değil |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | tek g = 0; soğuk gaz püfü düz saydam koni ≤0,25 s, KIVRILMAZ (MARS_SON_CIKIS RCS buhar vakası); duman/bloom yok; kabinde de her şey süzülür |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | güneş yönü gezegene göre sabit ('from beyond the planet's lit limb'); ardışık sahnede aynı |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ÇAPA ÜÇLÜSÜ: SEÇİM S30 el ayırma kolunda · BEDEL S45 · FİNAL S46; S5/S23 tereddüt kanalı el durur |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | replikler telsiz/kadraj dışı → SPEC DIALOGUE LINES ↔ prompt tırnakları eşit; OMNI kuralıyla post-dub kararı 02_KONSEPT'te |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | BEDEL EĞRİSİ hücresi <kanal @ saniye>: S30 omuz düşer · S40 tek el tutunma ön kol · S44 G ile gövde koltuğa |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | yorgunluk 0-6: S0=1 → S29=4 → S42=6 → S46=5; ardışık düşüş ≤1; SON = sonraki BAŞ |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | SPEC C KİMLİK DİZİSİ: kask K×47 + S46 A · giysi rengi · sol omuz bant · eldiven sürtünmesi S42+ |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | DÜNYA ÇAPASI 3 cümle: gezegen yarım diski + kenarı · tek güneş · uydu ışığı; her dış kadrajda BİREBİR |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | kafiye S0 ↔ S47: kokpit penceresinden aynı kurulum (motor ateşleyen gemi → vurulan / vurulmayan); CAMERA birebir + hold |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S0 soru: 'neden vuruldu?' ilk 3 s; ilk 30 s ≤2 kurulum (S0-S2); son kare adlandırılmış |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | vuruş sütununda ardışık tekrar 0; S31-S35 yaklaşma her sahnede başka koşul (sahibin 'hangi koşul değişti' testi) |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | TEMAS·DEĞİŞİM·SONUÇ aynı klip: S15 · S30 · S36 · S37 · S42 · S45; ateş→vuruş 3 s, sonuç ≥1 s merkez üçte birde |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IN FRAME ilk satır; gemi/uydu kadrajlarında (none) insan tarifi 0; eldiven insertte yüz yok |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | üretim defteri 3 kutu; telsiz konuşanı kadrajda yok; pilotun 'Yapma' repliği sırttan/kask içi, ağız görünmez |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | 3 ses yatağı (kokpit uğultusu · giysi içi nefes · gövde titreşimi); vakumda dış ses yok; telsiz band-pass EVET; katman ≤4 |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | ⚠️ S2 'Yanımızdan geçiyorsun' görüneni söylüyor → SAPMA önerisi; diğer 6 replik karar/kadraj dışı bilgi taşıyor |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | 11/14 risk (kask · 2. figür · gösterge · parçacık/kopma · replik · lockoff · ışık mıknatısı · insansız · politika · yapı · bölgeli iç/dış) → KİLİT TAVANI ≤20; KART 10: insansız sahnede NEGATIVE <900 karakter; KART 13: gemi/uydu ANATOMİ KARTI + ölçek merdiveni |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 540 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A4 🔴 binme/inme tipi 4 sahne (S25 kapsüle · S40 dışarı · S42 içeri · S46 bölmeye) → geçiş kadraj dışı, sahne ÖNCE/SONRA tarafta başlar · A5 1 no. risk uydu atışı sayıyla · B5c ilk üretim S44-S45 |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | MUHATAP = kadraj dışı ikinci insan (telsizdeki ses) + kendi geçmiş kararı (kapsül) · diyalog merdiveni BASAMAK 1 (kadraj dışı telsiz) · Character Bible ≠ karakter → KARAKTER KARTI ayrı |
| ✅ | `KILAVUZ_REHBERI.md` | 2289 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.7 8 dk kartı 2×24 der, sahip 4×12 → D74 · §3.1 VAKUM (egzoz düz koni kıvrılmaz · gölge mutlak siyah · dolgu yok · dış ses yok) + §3.10 kokpit iç · §4.1 bilimkurgu yetkinlik kuralı · §5.1 çekirdek 8 cümle · §7 DEĞİŞEN NİTELİK: fener sönmesi sınıra, kopma HAREKET · YAPISAL RED insansız profil |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 427 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3: IN FRAME ilk satır · 3. satır tek kilit sayıyla · START FRAME tek satır · pozitif 100-250 / 120-300 kelime · OMNI katmanı; insansız kadraj IN FRAME: none |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | novum tipi FİZİKSEL YASA (makine kuralı: yanan motor 3 s'de vurulur · soğutma kanatları açıkken vurulmaz) · TAŞIYICI motor kolu × egzoz konisi · TEK KARE S0 · kural tekrarı 6 nesne (mekik · arka yarı · tahliye · kapsül · çekici · kurtarma gemisi) · başlık şeması 'Don't Light the Engine' |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | İNSAN-MAKİNE (yatay süreç teması ✅) · TANIM: 'Savaş, onu başlatanlar gittikten sonra da makinelerin içinde sürer.' · motif sentetik ritim: uydu sensörünün sabit tarama ritmi ↔ pilotun düzensiz nefesi · final payoff: makine taramayı sürdürür, insan seçimi görünür (boş kapsül yuvası) |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | HOOK TİPİ in medias res · S0 soru 'mekik neden vuruldu, pilot o kola basacak mı?' · ilk 2 s tek diegetik ses (kokpit uğultusu + telsiz cızırtısı), müzik 0:00'da YOK · açılış bütçesi %10-15 = S5-S7 katalizör (hat kaçar) · bilgi asimetrisi: izleyici kanat kuralını S3-S4'te öğrenir |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | ardışık çift ≥1 ölçek + ≥45° · KÜME ≥2 işaretli · DÖNÜŞ ≥%40 (≤3 sahne ara) · dönen sahne CAMERA metni birebir + işaret · şok bandı 2 kez (S30 ECU→EWS kapsül vurulur · S45) · tema tehdit: alt açı uyduya, pilota değil |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | ⭐VİRAL S30 (YÜZ: vizörde gözler kapanır 1 s + HAREKET: kapsül ayrılır ve vurulur) · S45 (YÜZ: G altında çene kasılır + HAREKET: motor bölümü kopup döner) · orta nokta S24 sahte zafer DEĞİL, karar · açılış-kapanış çifti S0↔S47 aynı pencere kadrajı |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | TARGET ASL 10,0 s sabit ızgara + gerekçe · her kesme örüntü kırıcı (ölçek/ışık/ses: kokpit içi ↔ dış uzay ↔ uydu ekranı) · makro kırıcı her 3-4 sahnede · sert kesme ≤3 planda (S0 vuruş · S30 · S45) |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | KART: ROL çekici pilotu S0 · İSTEK yanaş+hava paylaş S10 · BASKI TEPKİSİ KONTROL EDER (S5 bekler) · ALIŞKANLIK sol başparmak kapsül ayırma kapağına iki kez vurur S6·S10·S17 → KIRILMA S29 · SINIR motoru ateşlemez S5 → S44 · ZAAF gaz ibresi S12-S33 + eldiven sürtünmesi S42 · TEL nefes tutma S13·S38 · İLK↔SON S0 el kolda donar ↔ S44 el kolu sonuna iter · KARAR MİMARİSİ S30 kapsül kolu ↔ reddedilen: dönüş rotası (kapsül yuvası kadrajda boş kalır) |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | ÇAPA: CHOICE S30 (BEFORE sol el kapakta iki vuruş hazır, omuz kalkık → AFTER el kolu çeker, omuz iner) · COST S45 (BEFORE gövde koltuğa bastırılmış → AFTER kemer gevşer, gövde öne süzülür) · FINAL S46 (BEFORE sağ eldiven dizde kapalı → AFTER omzundaki eli tutar) · TEMPO ≥3 değişim, S30 en yavaş, S44 en hızlı · anti-RESET S16/S31/S46 |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 438 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | kilit fiili süreç (works the valve · feeds the tether · matches the spin) · TIMELINE ≤3 satır son satır SÜRDÜRME · çevre saati tek: uydu sensör ışığının tarama ritmi / dönen gemi penceresi / ibre · ⛔ klip içi durum değişimi: motor YANMA sınırda başlar (imaj t=0 koni yanıyor), vuruş = kopma HAREKETİ · SON 3 s sütunu |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | silah ADLANDIRILMAZ (weapon/cannon/laser/beam 0; uydu 'long rail housing') · vuruş = §4.1 ① kütle-hız + ② malzeme sonucu ('the thruster cluster separates along its seam and keeps the spin') · 'explosion/fire/damaged' 0 · §3 ② bedenden çıkarma: S46 kask sahneye ZATEN AÇIK girer · ⑥ yüzü kapatan ekipman → vizör berrak · en riskli kare S15/S16 (insanlı gemi vurulur, içeride kimse kadrajda değil) |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | ikinci insan KADRAJ DIŞI ses + S46 tek el → iki kart ≥3 satır ayrışır (tahliye sesi ACELE EDER ↔ pilot KONTROL EDER) · İSTEK ÇAPRAZI nesne = kapsül · AYRILIK S7 (pilot çekilir, 'Geri dön' ret gecikmesi ≥0,7 s) · TERSİNMİŞ S27↔S28 ('Kapsülünle git' ↔ pilot kapsülü kapatır) · MESAFE EĞRİSİ gemiler arası metre · KİM SOLDA: çekici SOL, tahliye gemisi SAĞ |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | muhatap İKİNCİ İNSAN KADRAJ DIŞI (telsiz) · DEĞİŞ-TOKUŞ tablosu 7 replik + S1/S29 ışıkla cevap (eylemle cevap) · DİNLEYEN KADRAJI pilot MS/MCU sırttan/profil · son replik S27 doruğun ÖNÜNDE; S46 ses kelimesiz ya da tek kelime · sessizlik cevabı hışırtı + gövde |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | register: tahliye sesi HUMAN telsiz band-pass, pilot HUMAN kask içi · bedenleştirme S46 (ses ilk kez telsizsiz = doruğun sonrası, bilinçli) · ilk replik S1 ~12 s · sayı söyleyen replik 0 (sayı ibrede) · ⛔ 'Yanımızdan geçiyorsun' görüneni söyler (D217) · İngilizce doğallık: kısaltma + kısa parça |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | tek pilot: rol şeridi SOL pazu + SOL uyluk güvenlik turuncusu bant · sırt C heykelsi kapalı · bilek: SOL kolda kapsül ayırma uzaktan kumandası YOK (kumanda kokpitte) → bilek bare · kişisel eşya 0 (kapsül yuvası eşya işini görür) · ⛔ serbest hortum yok: hava hortumu iki ucu adlı (çekici göğüs soketi → tahliye kapağı) |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | arketip I ENDÜSTRİYEL (çekici işçisi) · kask yuvarlak sert kabuk + tek düz ön pane + kalın koyu çerçeve + derin yaka halkası + kaşta iki kare lamba · kask içi 4500K rim fill (yüz okunur, 'glow' yok) · renk: kırık beyaz kanvas + turuncu bant (vakum siyahına kontrast) · kir: global mat sürtünme, S42 sonrası eldiven avucu parlak metal izi · sırt 'one continuous ribbed surface' |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | 5/6 tetikleyici doğru (T1 kask · T2 uydu/çekici/tahliye biçimi · T3 çekici↔tahliye oranı 1H · T5 tekrar eden vuruş/kopma · T6 uydu 9+ sahne) — sahip 'YAZILMASIN' → PLAN'a D74 satırı + 🔴 04_UYARI + telafi: ANATOMİ KARTI sayıları (lüle/kanat/pencere adedi) + Scene Foundation ana kareleri |
| ✅ | `YANASMA_VE_KENETLENME_KILAVUZU.md` | 220 | havuzdan açıldı · yanaşma sekansı ZORUNLU | V1-V6 seti: temas V5 kamera HEDEFTE, çekici kameraya gelir (S36-S37) · V3 oran karesi — sahip 'birkaç kontrollü geniş plan' istedi → 4 oran karesi, her biri oran + hangi uç önde + kesir cümlesiyle (D74) · V2 çift kadraj hiza bozuk (S2) ↔ oturmuş (S35) · temasın sesi YOK, nefes yarım saniye tutulur · sayı replik 0 |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | havuzdan açıldı · sabit hedefe hareket + araç kartı | SPATIAL MAP: gezegen kadrajın altı, uydu ışığı gezegen kenarının üstünde SAĞ üst, tahliye gemisi SAĞ, çekici SOL; kamera tarafı film boyu aynı · YÖN DEFTERİ 48 satır · §5.3.1 fren alevi GİDİLEN yöne · dönen gemi 'yaws … and holds' başlangıç+bitiş saati · negatif eklentisi mirrored/direction reversal |
| ✅ | `OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md` | 414 | havuzdan açıldı · motor OMNI | CAMERA '… In a single continuous shot.' · AUDIO her klipte, telsiz sözü klipte ÜRETİLMEZ (post-dub, 'one short burst of radio static') · tırnak 0 · kare dengede · §3 ④ kadraj dışı nesne GİRMEZ → yaklaşan çekici t=0'da kadrajda · zincir modu ① tek kare (sahip kararı ⬜ K2) |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 436 | havuzdan açıldı · durum değişimi sınıra | fener sönmesi · buğu · kanat kapanması SINIRDA; kopma/savrulma HAREKET klip içinde · 47 sınır satırı + açık soru tipi ①-⑤ / cevap tipi ⓐ-ⓓ · ardışık iki sınırda aynı cevap tipi YOK · düz cevap ≤6 |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | havuzdan açıldı · gemi/uydu ölçeği | 1H = 1,90 m: prompta gövde boyu · ANATOMİ KARTI (çekici · tahliye gemisi · uydu · kapsül: kanat/lüle/pencere adedi TEK sayı) · kesir = yükseklik×odak ÷ (mesafe×20,25) · ölçek şahidi (figür / tekrar eden birim / taşan kenar) · dönen gemi kanıtı: yıldızsız sahnede gezegen kenarının süpürmesi · maket etkisi 'no miniature read' |
| ✅ | `DUNYA_GORUNUSU_KILAVUZU.md` | 341 | havuzdan açıldı · World Bible | arketip V VAKUM: 'a flat black sky' · TEK gök cismi = gezegen (kadrajın altında, kıvrık aydınlık kenarı) · güneş kadraj DIŞI · yıldız yok (güneşliyken 'starfield' tetikleyici) · DÜNYA ÇAPASI 3 cümle birebir |
| ✅ | `ISIK_SENARYOSU_KILAVUZU.md` | 322 | havuzdan açıldı · Lighting Bible | KAYNAK tek güneş (dünya kadranı 2, yüksek) + gezegen parıltısı soğuk ikincil + kokpit 4500K panel + kask içi 4500K rim fill · gölge tarafı pure black · PRATİKLER sayılı: tahliye penceresinde fener 3→0 (sınırda), uydu sensör ışığı 1, çekici kaş lambası 2 · 'glow/volumetric/lens flare' 0 |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | havuzdan açıldı · final tipi | FİNAL TİPİ MUĞLAK (kurtuluş kapalı, uydu tarıyor açık) · kapanış bütçesi 7-9 dk %5-7 → sahip S46-S47 (%4,2, D74) · TOHUM S5-S6 kapsül ayırma kapağı ≤2 s, S47'de boş yuvaya döner · PAYLAŞIM HUŞU S44-S45 · SON PLAN TİPİ nesne eki (boş kapsül yuvası) |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | havuzdan açıldı · çift kartı | ÇİFT TİPİ KAFİYE (7-9 dk) · değişken ② NESNE+olay: motoru yanan gemi vurulur (S0) ↔ motoru yanan gemi vurulmaz (S47) · ⚠️ sahip S0 kokpit / S47 dış geniş tarif etti → aynı kamera değil; kurulum kafiyesi S8↔S47 (D74) |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | havuzdan açıldı · bağ bütçeleri | 48 sahnede: göz ≥6 (S1·S14·S22·S29·S30·S46) · tepki planı ≥12 · el ≥7 · tutunarak ilerleme ≥5 · eşya ≥3 (kapsül ayırma kapağı) · Kuleshov ≥16 · görünür nefes omuzda · doruk yükü omuz/el |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | havuzdan açıldı · sahne sınırı | omurga lens 35mm · gizli geçiş S30→S31 (kapsül parçası kadrajı keser) · S44→S45 hareket eşleşmesi · sert kesmeler S0 vuruş · S16 dönme başlangıcı · S36 temas |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | havuzdan açıldı · tür senaryosu | antagonist = MAKİNE rasyonalitesi (HAL kalıbı) + değer çatışması: kural ↔ insan · ÇEHOV halkaları: kapsül S5→S30 · kanat S3→S31/S44 · ibre S12→S33 · hortum S10→S43 · manivela S10→S41 · gezegen kenarı S8→S47 · deus ex machina 0 |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | havuzdan açıldı · kalıplar | K2 boşluktaki nokta (S8 uydu ışığı) · K19 süzülen enkaz (S13, karakter sabit) · K3 vizörde gezegen (S30 yüz planı) · homage adı prompta 0 |
| ✅ | `YUZ_VE_KAST_KILAVUZU.md` | 293 | havuzdan açıldı · pilot yüzü | kadın, kırklarının ortası · sapma ÇENE (geniş kare çene) · yaş dokusu set lines at rest · ten deep brown · promptta ≤3 öznitelik aynı pencerede [D167] · yüz yalnız S14·S22·S29·S30·S45·S46 |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 386 | havuzdan açıldı · çapalama | Scene Foundation: boş kokpit master + dış uzay master (gezegen + uydu ışığı) ana kareleri üretimden önce · karakter çapası cümlesi kelimesi kelimesine · seed OMNI'de belgesiz |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | havuzdan açıldı · vuruş→açı | tehdit alt açı UYDUYA (S3·S4 ekran) · yenilgi üst açı S21 (savrulan çekici) · epifani profil MS S22 · hiçlik zenit S32 (motorsuz süzülen çekici) · dutch yok |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | havuzdan açıldı · kurgu kapısı | 10 madde: klip 48 · 480 s ±2 · ekran metni 0 s · CENTRAL CHOICE S30 ekranda · doruk S36-S45 · plan↔kurgu eşlemesi · son üç klip elle · Çehov kurulum listesi 7 halka |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | havuzdan açıldı · kapak anı | KAPAK ANI S0 ≈0:04 — mekik ikiye ayrılırken pencere çerçevesinde pilotun motor kolunda donan eli · vaat 'motor = ölüm' S0'da teslim · spoiler: kapsül feda ve S45 kopma kapakta YOK |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1228 | 8 dk bölümünde BENI_HATIRLAMA (B1)/(B2) 0/4 — QA birimi K1 açık → bu film de aynı iki satırla açılır; bulgu 9: kurgu plana iki yönden sapıyor → kurgu kapısı 48 klip · 480 s |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | #2 COLD BURN S8 YR: insansız + uzun NEGATIVE → V3 Style satırı GEÇTİ (insansız gemi sahnelerinin reçetesi) · #3 kask ÇIKARMA PB → S46 kask sahneye açık girer · #4 'wounded ship'+'dull orange glow' PK+PB · #15 OMNI kimlik yığını → pilot ≤3 öznitelik · motor sütunu ZORUNLU |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | (kapalı tablo) COLD BURN 4,0 ve RING LIGHT 6,0 düşüklüğünün kökü KURGU kaybı + jenerik kartı → KESİLEMEZ listesi + kart 0 s |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | (kapalı) COLD BURN mantık 7,0 · sayaç N/A (D78) → bu filmde sayaçlar (fener · ibre · kanat) tek karede sayılır |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | (kapalı) klon araçtan iniş/binişte 2/2 (Stone Sky · Starless Circle) → A4 geçişleri kadraj dışı · COLD BURN iki giyside sırt ünitesi doğdu → S40-S41 sırt pozitif |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | (kapalı) BLACK CRADLE vakumda ses + dudak senkronu → dış kadrajda ses yalnız gövdeden/kask içi; COLD BURN miks 4 |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | — |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | HARD DOCK 7,4: S13-S16 dış (insansız) dizi duygusal inşayı kesti → ardışık insansız sahne ≤2 · COUNTED TURN THE CHOICE IS INVISIBLE → S30 çapa çifti |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | HARD DOCK 5,5: S8→S9 yüzde sıcak→soğuk sıçrama → kask içi fill 4500K SABİT; COUNTED TURN KEY WALKS → güneş yönü nesneye bağlı sabit |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | HARD DOCK LEAVES AT 00:25 · kokpit↔dış plato 00:10-00:40 → S0-S4 her kesmede yeni bilgi (fener · kanat · ikinci vuruş); çıkış 4 → son 10 s adlandırılmış kare |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 85 | — |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 63 | — |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 63 | — |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | HARD DOCK kamera 6 · karakter 8 → ölçülmüş yanaşma filminde kare 7,4; kamera zaafı D210 kafiye |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | LOCKED PULSE kimlik 3 · ekipman 3 · nicelik 2 → KİMLİK DİZİSİ + ANATOMİ KARTI sayıları; HARD DOCK 9,1 (devamlılık tutan tek yanaşma filmi) |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | HARD DOCK SFX senk 9 · miks 9 (A durumu) → gövdeden iletilen metal sesi emsali |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | HARD DOCK 8,1 (en yüksek) — bedelli yanaşma kararı işledi; özgünlük 7 → novum kural tekrarı |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 110 | HARD DOCK ufuk 5 FIELD DRIFTS → DÜNYA ÇAPASI (gezegen kenarı konumu) birebir; SOLAR MIRROR SUBJECT DUPLICATE → insansız kadrajda figür yok |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 94 | HARD DOCK balistik 8,5 momentum 8 MINOR SLIPS → kopan parça dönüşü sürdürür (derece/s yazılır) |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 76 | HARD DOCK 'B4 docking impact elided by cut to cockpit' → S36 temas klibin içinde, kesme temastan SONRA |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 76 | HARD DOCK 6,6 'no tremor in E10' · SOLAR MIRROR WEIGHTLESS WORK → S38-S42 dış çıkış efor kanalı saniyeyle |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | HARD DOCK kafiye 2: S24 kapanış kurulumu açılışla uyuşmadı → S0↔S47 CAMERA metni birebir |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (70 dosya · 16957 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `KRONOS_SON_SINYAL.md` | ① aynı format — tek ölçülmüş 8 dk film (30 mercek, vakum istasyonu, ayrılma/patlama) | vakumda ayrılma/kopma SESİ 3 🔴 → dış kadrajda dış ses 0, yalnız kask içi/gövde · 0g'de yürüme/pedal → pilot hep kemerli ya da tutunur · S1↔S24 kafiye kırık · dijital sayaç bozuldu → sayaç ibre/ışık · peş peşe konsol sahneleri plato (LEAVES AT 00:48) · ayrılma anı tek karelik kesmeyle kaçtı → D213 |
| ✅ | `THE_HARD_DOCK.md` | ② aynı ortam kartı (§3.1 vakum + §3.10 kokpit) + en yakın yanaşma emsali | 1:10 dış yönelim ile pencere perspektifi 45° çelişti → dış kurulumlar kokpit penceresinin gördüğü yönle aynı · panel kopmasında recoil yok → her vuruşta gövde tepki dönüşü · cıvata 8→10 → ANATOMİ sayıları · temas kesmeyle gizlendi → S36 · kokpit↔dış plato → her kesmede koşul değişir |
| ✅ | `THE_PAYLOAD.md` | ③ aynı tema İNSAN-MAKİNE (yatay 3-5 dk) | novum taşıyıcısı okunmadı, iki taşıyıcı sahne 'tekrar' sayılıp kesilmeye önerildi [D157] → uydu kuralının her tekrarı FARKLI nesne + farklı sonuç · ekranda 'PHASE 1' yazısı [D155] → gövde/panel yazısı 0 · seçim lojistiğe döndü, sürtünmesiz kenet [D158] → S36-S42 dirençli kenet |
| ✅ | `THE_COUNTED_TURN.md` | ④ en düşük skor (⑧ 0,0 · ⑩ 3,4 · ② 3,0) | NOBODY PAYS + THE CHOICE IS INVISIBLE + yüz/giysi kimlik kırılması → ÇAPA ÜÇLÜSÜ + efor kanalları + KİMLİK DİZİSİ; KEY WALKS 3→9 saat → güneş sabit |
| ✅ | `THE_COLD_BURN.md` | ⑤ en yakın konsept (buzdan kaç → yanan gemiye yanaş, 3-5 dk) | D82 sayı replikleri insan ağzına geçti → sayı yalnız ibrede · D83 ortam yatağı klip sınırında öldü → MUZIK köprü ≥0,2 s · D79 sırt ünitesi 32 negatife rağmen geldi → S40-S42 pozitif sırt · alevli patlama planın ihlali 🔴 → vuruşta alev 0, ayrılma + buz kristali · kurgu kapısı 4 madde ihlal |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  21  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   46
ZORUNLU SATIR:   14940
SEÇMELİ KAYIT:   5 / 70  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
