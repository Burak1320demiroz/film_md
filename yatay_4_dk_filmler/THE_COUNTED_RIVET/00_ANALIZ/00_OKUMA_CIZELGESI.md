# 📖 THE_COUNTED_RIVET — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 25.09.2026 06:44
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 40 dersin 35'i bu filme düştü; replik (D203 · D217) · vakum (D201) · düşük-g (D198) etiketli satırlar ve kontrat dosyası `—` ile geçildi |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | — |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 24 video promptunun CAMERA satırı `single unbroken take` + `absolutely zero camera movement`; her klip ayrı üretilir, sahne içi kesme yok |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | vizör arkasındaki yüz TEK blok cümle; yüz yalnız K19'da kadrajda — kalanında vizör `optically clear` der ve durur [D167 ④] |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | SPEC B `SCREEN TEXT: 0 s`; film adı ve karakter adı promptta 0 kez — karakter yalnız fiziksel tarifle çapalanır; S7'nin son klibine `no title card, the shot simply ends` |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | SPEC C YIPRANMA: 2 sabit bölge (sağ eldiven avucu · sol dirsek), başlangıç S1; asit lekesi S5'ten itibaren MONOTONİK artar, hiç sıfırlanmaz [D147] |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | gövdede köşeli parantez ve etiket yok; kamera satırı düz cümle (`shot on a 35mm lens from a fixed position two metres away`) — sayı-harf dizisi yazılmaz |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | PLAN `KESİLEMEZ LİSTESİ`: S5'in üç klibi (bedel) + S7'nin son iki klibi (dokuz mandalın kesilmesi · yükselme). Montaj kontrolü SONDAN başlar |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | kurgu kapısı: klip 24 = 24 · süre 240,0 s ±2 s · ekran metni 0,0 s (kapak çıktısı dâhil, kurgu klasörüne girmez) |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | ÖLÇEK sayacı TEK KAREDE iki ucunu gösterir: S3'ün bir klibinde eldiven ve perçin başı AYNI karede (perçin omuzdan geniş). Karşılaştırma karesi plana yazılır, yoksa sayaç yoktur |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | metin yasağı KAPSAMLI yazılır (giysi + plaka + perçin + mandal + şerit); ölçüler SPEC D'de ve fizik defterinde kalır, prompt gövdesi gövde-göreli konuşur (`wider than her shoulders`, `a glove's thickness`). ⛔ şeride ÇENTİK/gradasyon yazılmaz — ölçü aleti en yüksek riskli yüzey |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | kamera sırtı gören her klipte yokluk kilidi POZİTİF tarife çevrilir: `the back of the suit is one continuous panel from collar to hip and it carries nothing` |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | SPEC B `FİNAL VURUŞ KANITI`: kesilmiş DOKUZ mandal ucu, S7'nin son klibinde, sayılabilir 9 adet; yoksa final teslim edilmemiştir |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | vizör tek DÜZ panel + görünür koyu çerçeve; `seamless · bubble · dome · sphere` 0 kez. ⚠️ referans paketi sahip kararıyla YAZILMIYOR → bu dersin tek ölçülmüş aracı (üretilmiş panel) kapalı; risk 04_UYARI_NOTLARI'na ⛔ olarak yazılır |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | `TEK KARE` cümlesi taşıyıcı nesnelerin ADINI taşır: gergin ÖLÇÜ ŞERİDİ + PERÇİN BAŞI. Taşıyıcı kadrajın ≥1/10'unu kaplar ve o klipte başka hiçbir şey hareket etmez |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | prompt gövdesinde en çok 3 kimlik özniteliği; boy göreli yazılır, ten rengi · yaş · saç yazılmaz. Ayırt etme yükü GEOMETRİDE (mandal kolu · şerit) |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | 0,904 g Dünya gibidir — `normal human pace, real time` yazılır [D44]. Efor kanalı ELDİVENİN ÜSTÜNDE okunur (`the glove's ribbed segments tighten over the tendons`), derinin üstünde DEĞİL [D175] |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | mandal halatı ve şerit NEREDE BİTTİĞİNİ söyler ve sarkan uç bırakmaz; şeridin iki ucu iki elde. ⛔ sarkan hiçbir şey yok — sarkmak çekilmeyi davet eder |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | yön cümlesi hedef nesneyi aynı cümlede adlandırır (`toward the rivet head`); yalnız `screen-right` yazılmaz. ⚠️ ufuk ve gölge YOK → kadrajdaki tek yön referansı perçin başı ve mandal çenesidir |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | çıplak-deri negatifi ÜÇ BÖLGE birden (yaka · bilekler · ayak bilekleri) 24/24 promptta; `through the glove` 0 kez; yıpranma izi giysi YÜZEYİNE yazılır |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | kontrast garantisi ÖZNEYİ tarif eder, yüzeye renk atamaz. Plakanın rengi TEK cümlede (WORLD bloğu) ve SPEC C'de aynı cümleyle durur |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | S5'in IMAGE promptu dikişin KAPALI hâlini yazar (t=0), VIDEO 2,0 s'de söker — iki prompt aynı anı anlatır. Bedel kadrajın kısa kenarının ≥1/8'ini kaplar → S5 yakın plandır, filmin en geniş kurulumuna YAZILMAZ |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | planlı mutlak sessizlik YOK; 24 klibin AUDIO satırı boş bırakılmaz — yoğun CO₂ yatağı sürekli, tınılar alçak [kart §3.6] |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | filmin 1 numaralı riski = şeridin DÜZ olduğunun okunmaması. Pozitif biçim sayıyla: `the tape lies flat along the surface; nowhere along its length is there a gap wider than the glove is thick` — yasak cümlesi biçim değildir |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | ⚠️ kart gölgeyi ve güneş diskini kaldırıyor → takvim yön+K yerine TEK PARLAKLIK dizisi olur: kubbe sabit, S6'dan itibaren asit cephesi kubbeyi bir kademe kısar ve GERİ AÇILMAZ (monotonik) |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | — |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | SPEC C tek g: 0,904 g. Nötr yüzerlik POZİTİF kuralla yazılır (`the platform floats in neutral buoyancy and is settling at a constant rate; it never hovers, never hangs motionless, never rises`); bırakılan nesne saniyeli düşüş satırı taşır |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | — |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ÇAPA ÜÇLÜSÜ: SEÇİM S5 (dikişi sökme) · BEDEL S5 (asit içeri) · FİNAL S7 (dokuz mandalı kesme) — her satırda BEFORE/AFTER beden çifti + saniye; dolgu jesti yazılmaz |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | — |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | her efor klibinde ≥1 ödeme satırı, saniyeli (`4,0 s — the right glove locks and the clamp handle stops for half a second`); PLAN BEDEL EĞRİSİ hücresi `<kanal> @ <saniye>` |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | yorgunluk 0-6, sahne başına tek sayı; ardışık düşüş ≤1 kademe. S5'ten sonra ≥3 → sonraki her IMAGE'ın SUBJECT satırı önceki klibin SON bedeninden kopyalanır |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | SPEC C KİMLİK DİZİSİ: kask 24/24 K (hiç açılmaz) · amblem YOK, 0 yama · giysi soluk okra-gri · asit lekesi sol göğüste S5'ten itibaren, geri dönmez |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | ⚠️ SAPMA — kart ufku ve zemini KALDIRIYOR (§3.6: ikisi de yok). Üç çapa yeniden tanımlandı: ① gök = üstte kaynaksız parlak kubbe, güneş diski 0 kare ② aşağı = okra derinlik, ufuk çizgisi YOK ③ yer imi = plakanın kendisi + bir perçin başı. Gerekçe 02_KONSEPT'e yazılır [D74] |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | kurulum iskeletinin ilk ve son harfi AYNI ve cümlesi BİREBİR; her video TIMELINE'ının son satırı `hold — the frame does not move` |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S1 (tek klip) soruyu sorar: mandal kapanıyor, içindeki yüzey kavis yapmıyor. İlk 30 s'de kurulum sahnesi ≤2; son kare adlandırılmış nesne (kesilmiş son mandal ucu), statik siyah 0 s |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | vuruş sütununda ardışık tekrar 0. `ölçer` vuruşu üç sahnede var (S3 · S5 · S6) ama araya çakma (S2) ve sürükleme (S4) giriyor; aynı klip kurguda 0 kez tekrar |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | her temaslı klipte üç satır aynı klipte: TEMAS · DEĞİŞİM · SONUÇ (≥1 s kadrajda); temas noktası kadrajın dış üçte-birinde YASAK — mandal, şerit ve dikiş jestlerinin hepsi bu kurala girer |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | her promptun ilk satırı `IN FRAME:`; SUBJECT yalnız kadrajdakini tarif eder. Kelime bandı IMAGE 100-250 / VIDEO 120-300 |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | ÜRETİM DEFTERİ'ne üç kutu: altyazı/caption KAPALI · filigran YOK · konuşan ağız kadraj dışı (replik 0 olduğu için üçüncüsü yapısal olarak kapalı). NEGATIVE'e bu konuda yeni cümle EKLENMEZ |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | MUZIK katman tablosu: sahne başına aktif katman ≤4 · her kesmede CO₂ oda tonu köprüsü ≥0,2 s · kesmede dijital sıfır 0 kare [D83] |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | — |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | RİSK SAYISI **7/14** → KİLİT TAVANI ≤20 devrede (malzeme azaltılmaz). Açılan kartlar: 3 kask · 4 ikinci figür · 5 ekran/sayaç (iki yönlü!) · 6 parçacık (asit cephesi perde riski) · 6b katmanlı dünya (derinlik→parlaklık) · 12 politika · 13 yapı ölçeği (plaka = filmin KONUSU) |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 542 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | 18 madde `06_URETIM_ONCESI_KONTROL`'e ölçüyle inecek. A5 1 no'lu risk = battenin DÜZ okunmaması, pozitif biçim sayıyla. B5 dörtlüsü dolu · B5b `—` (tek insan) · B6 politika satırı S5 · C altı sayısal kilit · E QA SPEC bloğu |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | MUHATAP satırı 79 filmin 79'unda YOKTU: burada **ortamın KALICI değişen parçası** (sökülen bağ + asit izi) + bağlama otomasyonu. BEDEL sahne numarası taşıyor (S5 · S7). İSTEK/ENGEL/BEDEL üçü de yazılı (depoda 8/2/28 film) |
| ✅ | `KILAVUZ_REHBERI.md` | 2528 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.3 24 klip · 240 s · 2 bölüm · §3.6 bulut bandı kartı (toz YOK · gölge YOK · ufuk-zemin YOK · kaldırma GERÇEK · 0,904 g · vizör %100 kapalı) · §4.1 bilimkurgu · §5.1 çekirdek 8/7 cümle · §7 tuzaklar. ⚠️ §3.6'nın İngilizce PHYSICS/AUDIO karşılığı PROMPT_HATA §2'de YOK — bu filmde yazılacak |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 437 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3-S iskeleti: `IN FRAME:` · `Clip n of 24.` · 2.+ klipte `CONTINUOUS ACTION:` · üçüncü satır sahnenin TEK kilidi (süreç fiili) · `START FRAME:` yalnız BU klibin imajı · bant IMAGE 100-250 / VIDEO 120-300 · CAMERA düz cümle |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | NOVUM TAŞIYICISI: **çelik batten × yüzeye yatırma jesti → boyunca hiçbir yerde ışık sızmıyor** (ölçek). İhlal sayısı 1. Üç kapı ✅ (tek kare · kinetik bağımsızlık · ≤5 kelime başlık). Kural 3 sahnede 2 nesnede kanıtlanır: batten S5 · perçin S3/S6 · sürüklenme süresi S4 |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 314 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | TEMA **İNSAN-MAKİNE** — §4 süre-tatmin yatayda bu dörtlüyü yasallaştırıyor, depoda en az işleneni (5). §5 satırı UYARLANDI: parazit/glitch bu ortamda yok → makine ritmi mandal lambasının SABİT periyodu; nesne indeksi çene ↔ batten aynı karede; ⛔ 'boyun damarları' yazılmaz [D175] |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | HOOK TİPİ **yanlışlık kompozisyonu** · S0 sorusu plana yazıldı · açılış bütçesi %12,5 (katalizör 30 s, band 24-36 s) · BİLGİ ASİMETRİSİ: DRAMATİK İRONİ, taşıyıcı ④ CETVEL İZLEYİCİDE · ilk 2 s tek diegetik ses (müzik 0:00'da girmez) · 120 px testi |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 396 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | kurulum tavanı ≤12 (24 klibin yarısı) · DÖNÜŞ ≥%40 → ≥10 klip · KÜME ARANMAZ (㉜) · her dönüşün kamera metni BİREBİR + işaret satırı · ardışık çift ≥1 kademe + ≥45° · açı tipi ≥3 |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | vuruş haritası yüzdeyle: katalizör %12,5 · orta nokta %50 (S4 sonu, sahte yenilgi) · her şeyin kaybı %75 (S6) · final %85-99 (S7) · kapanış imajı K24 ↔ K01. ⭐VİRAL **2 klip** (YÜZ + HAREKET ikisi de dolu); kartın 4 adedinden sapma D74 ile gerekçeli |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 324 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | `TARGET ASL BAND: 10,0 s (sabit ızgara — eğri yok)` + gerekçe satırı ZORUNLU · MİKRO kırıcı her kesmede ölçek/kurulum · MAKRO 3-4 klipte bir · ambiyans 0 kesinti · J/L-cut ≥%60 · sert kesme ≤3 · ihraç 1440p+ · −14 LUFS · −1,0 dBTP |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | 8 satırlık kart yazılacak. ALIŞKANLIK: her mandalı kapatmadan önce çeneyi iki parmakla iki kez yoklamak (S2 · S3 · S6), KIRILMA S5'te. DAVRANIŞ ŞERİDİ 24 hane, G ≤%50, K'dan sonra B/R. İLK↔SON: mandalı kapatan el ↔ mandalı kesen el |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | İZLEYİCİ CÜMLESİ her sahneye · ÇAPA ÜÇLÜSÜ CHOICE S5 · COST S5 · FINAL S7, BEFORE/AFTER **aynı kanalda** (iki eldiven) · fark ≥ kısa kenarın 1/8'i → S5 ve S7 yakın plan · TEMPO sütunu · dolgu jesti (eldiven/kask/omuz) 0 |
| ✅ | `COK_KLIPLI_SAHNE_KILAVUZU.md` | 403 | **[cok-klip]** · yatay film: sahne 2-6 klip · §2 kapsama şablonu · §3 CONTINUOUS ACTION · §4 sahne kilidi · zincir yok · ㉜ (PLAN'da SAHNE PLANI yoksa "—") | **SAHNE PLANI: 1 3 4 4 3 4 5** · kapsama şablonları klip rolüne · `CONTINUOUS ACTION:` 17 klipte (24−7) hem IMAGE hem VIDEO · LIGHT/PHYSICS/AUDIO-ilk-cümle sahne içinde BİREBİR · zincir dili 0 · sahne başına ≥2 kurulum · klip sonu SÜREN hareketle biter |
| ✅ | `FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` | 243 | **[efor]** · §1 destek·gövde·işaret·duraksama · §1.5 saydamlık tuzağı [D175] · §2 düşük g'de düşüş dili · çarpma üç evre (efor/düşüş yoksa "—") | DESTEK + GÖVDE + 2-3 aynı yöne işaret + DURAKSAMA. Efor **eldivenin/kumaşın yüzeyinde** okunur [D175]. 0,904 g → `normal human pace, real time` [D44]. `falls fast / plummets` yazılmaz. Direnç sıfatı NESNEDE: `the laced hem is bound tight` |
| ✅ | `POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md` | 167 | **[darbe]** · §1 toparlanma merdiveni = D207 · §2 hasar düz cümle + referans sayfası · §3 kadro sayı kilidi (darbe/hasar/kadro çıkışı yoksa "—") | Darbe/düşme yok → toparlanma merdiveni koşmaz. Ama HASAR HAFIZASI koşar: açılan bağ deliği + asit izi S5'ten sonra 3 sahne sürüyor, konumlu düz cümleyle ve her klipte birebir. ⚠️ §2.2 bunun için referans sayfası istiyor — paket yazılmıyor, risk 04_UYARI'da |
| ✅ | `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md` | 181 | §1 mikro→makro · §2 yürüme platosu · §3 temas iki klibe · §4 filigran = araç · tripod ADAY-98 | ⚠️ parmak ucu işi YASAK: 'dikişi sökmek' → **iki elle kalın bağı çekmek** (makro, ödemeli). Yürüme klibi ≤1. Alet tek rijit parça: `a flat steel batten as long as her arm`. CAMERA satırında `tripod` kelimesi YOK (ADAY-98). Eşya envanteri pozitif cümleyle |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 444 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | kilit fiili ETKİNLİK/TAMAMLAMA (`works the lacing out of the hem`) · TIMELINE ≤3 satır, her satırda gövde fiili · son satır SÜRDÜRME (`settles/holds/then stops` YASAK) · sahne başına BİR çevre saati = mandal lambasının sabit periyodu · zemin bağı cümlesi |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | ⚠️ **EN KRİTİK KİLİT.** §3 imza ② 'bedenden bir şeyin çıkarılması' = 3 ölçülmüş red (COLD BURN S28). S5 bu yüzden GİYSİDEN PLATFORMA taşındı ve kesme yok, bağ ÇEKİLİYOR. B6 satırı + ÖNLEM/MALİYET/TELAFİ üçlüsü yazılacak. NEGATIVE'de şiddet/tehlike sözlüğü 0. Milliyet/kurum/ad 0 |
| ✅ | `PROMPT_HATA_ONLEME_KILAVUZU.md` | 433 | §1 on kilit · §2 ORTAM CÜMLELERİ (kopyala-yapıştır) · §3 15 hata sınıfı · §4 promptun kapatamadığı üç sınıf · §5 novum kilidi · §7 --kilit ölçümü (19.09.2026 · 31 film / 688 bulgu) | ON KİLİT: 8 negatif cümle + gövdede `PHYSICS:` ve `AUDIO:`. ⚠️ §2'de **§3.6 için hazır cümle YOK** → bu filmde yazılacak. §3b ① temas ilk 2 s'de kurulu · ② pozitif ara katman = parlak çelik batten eldivenle plaka arasında · ④ temas cümlesi İKİ YÖNLÜ · §6 büyük harfli jeton 0 |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | — |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | — |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | — |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | dört katman: ROL ŞERİDİ tek renk (güvenlik turuncusu, SOL pazu + SOL uyluk, 360° sarılı) · SIRT C DÜMDÜZ'ün heykelsi hâli · BİLEKTEN 1 öğe (SAĞ bilekte analog basınç göstergesi, rakam tarif edilmez) · KİŞİSEL EŞYA 0 (bilinçli, kartta '—') · serbest uçlu kordon YOK |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | arketip **I AĞIR ENDÜSTRİYEL** (en düşük oyun-görünümü riski; ton: endüstriyel emek). Renk ORTAM KARTINDAN: okra kubbede kaybolmaması için arduvaz grisi kapitone kanvas + üst göğüste tek güvenlik turuncusu bandı. Kask: yuvarlak sert kabuk + TEK DÜZ pane + kalın koyu çerçeve + derin bronz yaka + 4500K nötr iç dolgu. Kir GLOBAL bitiş |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | ⚠️ altı tetikleyiciden **BEŞİ** doğru: T1 kask · T2 mandal çenesi ve vizör biçimi · T3 plakanın oranı (filmin KONUSU) · T5 asit cephesi · T6 perçin başı üç sahnede. Sahip kararı YAZILMASIN → PLAN'a tek satır gerekçe [D74] + 04_UYARI'ya ⛔ açık risk |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1331 | matris satırı + rapor satırları adım 11'de eklenecek; ⚠️ sayaç MATRİS UYUM 5 eksik / 4 hayalet diyor (bu filmle ilgisiz, devralınan borç) |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | vaka 3 (COLD BURN S28 · **kask ÇIKARMA** · PB) çözümü: 'nesne sahneye ZATEN çıkmış girer' → S5 buna göre yazıldı · vaka 15: kimlik yığını ≤3 öznitelik · vaka 12: milliyet 0 · vaka 2: insansız sahne + uzun NEGATIVE = yapısal red → bu filmde insansız klip 0 |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | — |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | — |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | — |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | — |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 127 | — |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | ⑩ üç çapa vuruşta önce/sonra karesi dondurulur; `THE CHOICE IS INVISIBLE` 4 filmde çıktı → SPEC'e ANCHOR BEATS satırı, BEFORE/AFTER aynı kanalda |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | ⑪ her kesmede 'ışıkta ne değişti'. ⚠️ bu ortamda gölge ve güneş diski YOK ve bu MEŞRUDUR → SPEC'e açık satır, yoksa mercek bunu bulgu yazar (LOSS_OF_LIFT'te tam bu bulgu DÜŞTÜ) |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | ⑫ DROP-OFF PREDICTION saniye söyler, kesme önermez · son kare ilk kareye dönüyor mu · başlık kartı 0 s |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 104 | ⑬ sahne ↔ prompt; 🅑 oranı hedefi %20 altı · `prompt_hata_analizi.py --kilit` ÜRETİMDEN ÖNCE koşulur, `HİÇ YOK` satırı varsa üretime girilmez |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 64 | ⑭ AMAÇ CÜMLESİ her harekete ('battenı gölgesiz kubbeye karşı kaldırır, altından ışık geçip geçmediğini görmek için'); PURPOSE STRING 24 hane; yürüme platosu riski [MIKRO_AKSIYON §2] |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 64 | ⑮ VEKTÖR CÜMLESİ. ⚠️ ufuk, gölge ve güneş yok → kadrajdaki TEK yön referansı perçin başı ve mandal çenesi; 180° çizgisi sahne İÇİNDE aşılmaz |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 92 | ① Motion Quality 24 filmde düşük; klip başı ilk 0,6 s klon taraması [D140]; insan sayısı RAKAMLA (`Exactly one human character`) |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 128 | ② CHARACTER PASSPORT SPEC C `KİMLİK DİZİSİ`ni okur; SPEC'e **sahne içi kesmeler** listesi girer (㉜'nin ilk film ölçümü buradan gelir); WEAR TIMELINE |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 106 | ③ LAYER COUNT ≤4 · AMBIENCE HOLE LOG · `SPOKEN LINES: 0` ↔ SPEC `DIALOGUE LINES: 0` (D203'ün tersi: 0 ilan edip 0 vermek doğrudur) |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 94 | ④ kesme listesi planın omurgasını hedefliyor (LOSS_OF_LIFT'te 4/4 madde) → PLAN'a KESİLEMEZ LİSTESİ; `ENDS OR STOPS` hükmü |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 113 | ⑤ en büyük arka plan nesnesi ADLANDIRILIR ve kadraj payı yazılır (plaka: kadrajın sağ yarısı); filigran köşe testi [D150] |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 96 | ⑥ GRAVITY TABLE tek değer 0,904 g; bırakılan eldiven ilk saniyede ~4,4 m [LOSS_OF_LIFT emsali]; nötr yüzerlik POZİTİF cümleyle yazılırsa 'hovering' bulgusu DÜŞER |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 78 | ⑦ ANLATIM CÜMLESİ her vuruşta, 'sanırım'sız bitmeli; TEMAS · DEĞİŞİM · SONUÇ üç satır aynı klipte, sonuç ≥1 s kadrajda |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 78 | ⑧ FATURA CÜMLESİ: 'bu işten SONRA bedende ne değişti'. NOBODY PAYS 7 filmde → her efor klibinde saniyeli ödeme satırı, ödeme sonraki klibe taşınır |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | ⑨ SETUP STRING ↔ KURULUM İSKELETİ yan yana; kafiye çifti K01 ↔ K24 birebir aynı kamera cümlesi; LOCKOFF HELD 24/24 |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (72 dosya · 18170 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_LOCKED_PULSE` (14.09.2026) | ① aynı format — yatay 4 dk'da son yazılan film | 12 mercek 🚨 GEÇERSİZ; ders şu: SPEC vardı ve mod V koşuldu → SPEC **ayrı dosya** olacak [D117] ve kesme yayılımı için master ölçülecek. Ayrıca bu film reformun gerekçesi: 126/126 sahte kilit, 747 KB klasör, üretim 0 kare → kilit tavanı ve kısa çizelge |
| ✅ | `LOSS_OF_LIFT` (21.08.2026) | ② aynı ortam kartı — §3.6 bulut bandının TEK filmi | ⭐ ölçülmüş zayıflık: **sayaç semantiği geç kuruluyor** — pirinç yay S2'de bir kez oynadı, S17'ye kadar hiç; izleyici çentiğin ne demek olduğunu doruğa kadar öğrenmedi. Bu filmde ölçek sayacı üç klipte ilerler. ✅ Düşen bulgular: nötr yüzerlik POZİTİF cümleyle yazılıydı · gölgesizlik ortam kartından · 0,904 g 'ordinary Earth pace'. ⛔ Başlık kartı 8. vaka |
| ✅ | `THE_STATIC_SHADOW` (13.09.2026) | ③ aynı tema — makine sesi/otomasyon muhataplı film | SPEC 7 makine repliği ilan etti, 30 promptun hiçbirinde tırnak yoktu (D203 · ㉓). Bu filmde SPEC `DIALOGUE LINES: 0` yazar ve promptlar 0 replik taşır — ilan ile gövde birbirini tutar. Ayrıca SPEC'in 7 makine çapası korunur (D204 · ㉔) |
| ✅ | `THE_CRACKED_HELMET` (10.09.2026) | ④ en düşük skor — ⑩ 2,0 · ⑨ 2,1 · ⑧ 1,0 · ② 2,0 | dört dip aynı kökten: ⑩ 'THE CHOICE IS INVISIBLE' (S9 ölüm-kalım kararı sıfır tereddüt) · ⑨ kafiye çifti kırıldı + 6/11 klipte plansız kayma · ⑧ 5/5 efor olayında sıfır ödeme · ② siyah↔beyaz giysi 5 kez. Karşılığı: ÇAPA ÜÇLÜSÜ + K01↔K24 birebir kamera cümlesi + `absolutely zero camera movement` + ödeme satırı + SPEC C KİMLİK DİZİSİ |
| ✅ | `THE_DRY_ANCHOR` (11.09.2026) | ⑤ en yakın konsept — çapa çakan, tutmayan zemin filmi | ⭐ SPEC'in **12 maddelik GÖZ KAPISI** biçimi alınacak: her madde TEK KAREYLE kapanır ve saniyesi yazılır ('64,0 s'de BİR çizgi · 84,0 s'de İKİNCİ · 114,0 s'de birleşmiş'). Sayaç okunurluğunun çözümü budur. ⚠️ 12/12 mercek GEÇERSİZ: master olmadan hiçbir skor tabloya girmez [D188] |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  26  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   51
ZORUNLU SATIR:   16791
SEÇMELİ KAYIT:   5 / 72  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
