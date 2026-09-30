# 📖 GUNES_MEZARI — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 25.09.2026 14:09
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 40 satırın 38'i bu filme düşüyor; DEĞİŞEN SATIR sütunu doğrudan hasat tablosuna taşındı |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | — |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 24/24 video CAMERA satırı `single unbroken take` + `absolutely zero camera movement`; sahne içi kesme 0 (kesme klipler ARASINDA) |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | yüz tek blokta, yalnız IN FRAME face olan 4 klipte (K03·K12·K16·K23); vizör optik berrak + KİMLİK DİZİSİ satırı |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | SPEC B `SCREEN TEXT: 0 s`; film adı ve özel ad promptta YOK; K24'e `the take ends on the held frame` cümlesi |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | SPEC C YIPRANMA: kırağı pası GLOBAL bitiş, 3 kademe (S1 yok · S2'den itibaren K1 · S5'ten K2), geri dönmez |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | köşeli parantez/etiket YOK · kamera satırı düz cümle · `S04`/`PHASE n` gibi büyük harfli jeton YOK |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | PLAN KESİLEMEZ LİSTESİ: K01 · K11 · K12 · K17 · K20 · K21 · K23 · K24 |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | kurgu kapısı ④: süre 240,0 s = 24 klip × 10,0 s · kuyruk kartı 0,0 s (KEPT_LIGHT'ta 5,0 s geldi) |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | ⭐ novumun TEK KARE kanıtı K02: küre + kapı boyundaki tek aydınlık pencere AYNI karede — ölçek iki uçlu okunur |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | metin yasağı KAPSAMLI yazılır (giysi+ekipman+zemin+doğal yüzey); metre SPEC'te, promptta gövde boyu |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | kamera arkayı gören 2 klipte (K05 · K18) pozitif sırt cümlesi: `one continuous ribbed surface … a long worn cloak hanging from the shoulder caps` |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | SPEC B FİNAL VURUŞ KANITI: K24 · 236,0 s · oyukta TEK filiz, 1 adet, sayılabilir |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | ⛔ `seamless/bubble/dome` 0 kez · tek DÜZ ön pane + KALIN koyu çerçeve + yaka halkası · referans paketi T1/T2 yazıldı |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | TEK KARE cümlesi taşıyıcıyı ADIYLA taşır: üç halkanın arasındaki kafesli güneş; K21'de kadrajda ikinci olay YOK |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | kimlik yığını promptta ≤3; kesin boy YOK, ten/saç/yaş YOK — PLAN'da kalır; yüz yalnız 4 klipte |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | 8 efor klibinde DESTEK+GÖVDE+2 işaret+DURAKSAMA; ödeme satırı saniyeli (K13·K16·K17·K18·K19·K20) |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | üç halkanın nerede BİTTİĞİ her klipte yazılı: `run from the spine down around it and end there; nothing else hangs from them` |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | yön cümlesi hep NESNEYE bağlı (`toward the cradle's middle arch`); ekran koordinatı tek başına yazılmaz |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | zorlanma GİYSİ YÜZEYİNDE (`the sleeves pull tight at the elbows`) · çıplak-deri negatifi ÜÇ BÖLGELİ |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | zemin rengi TEK yerde (World Bible); kontrast ÖZNEDE: kırağı pası omuzda figürü ayırır — zemine renk atanmaz |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | her IMAGE promptu ÇAPA'nın BEFORE'u; K17/K20'nin imajı değişimin ÖNCESİ; bedel klibi WS DEĞİL (fark ≥1/8 kısa kenar) |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | K12 sonu tam sessizlik KURGUDA HARD MUTE (119,0-120,0 s); video AUDIO satırı boş bırakılmaz |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | ⭐ 1 numaralı risk KÜRE; pozitif biçimi SAYIYLA (kenar keskin · korona 0 kare · hücre 4 s'de bir genişlik) |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | IŞIK TAKVİMİ 7 satır; K01-K20 tek değer (fener+ay), K21-K24 ARTAN ve bu bir OLAY olarak yazılı — monotonik değil, ilan edilmiş |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | — |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | SPEC C tek g + düşüş tablosu; küre DESTEKLİ (kafes/kaide) ve bu her PHYSICS satırında mekanik sebebe bağlı |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | — |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ÇAPA ÜÇLÜSÜ: CHOICE K16 · COST K17 · FINAL K23; her satırda aynı kanalda BEFORE/AFTER beden çifti |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | SPEC A `DIALOGUE LINES: 2` = promptta tırnaklı geçiş sayısı (K03 · K10); aynı tek kayıt cümlesi |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | PLAN BEDEL EĞRİSİ: kanal @ saniye; 6 efor klibinin her birinde ≥1 saniyeli ödeme satırı |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | YORGUNLUK 0-6 dizisi; ardışık düşüş ≤1; sahne içi 2.+ klipte CONTINUOUS ACTION bedeni taşır |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | SPEC C KİMLİK DİZİSİ: kask K×24 · amblem YOK (hiç) · grafit · kırağı pası S2'den · anahtar çubuğu K15-K20 sonra YOK |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | World Bible ÜÇ cümle birebir: gök (parçalanmış ay 18°) · ufuk (bazalt kule hattı) · yer imi (kaidenin üç taş kemeri) |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | iskelet ilk ve son harf AYNI (A … A); K24'ün CAMERA metni K01'in metniyle BİREBİR; TIMELINE son satırı sürdürme |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | K01 soru sorar (kafeste ne var); ilk 30 s'de kurulum klibi 1; son 10 s adlandırılmış nesne (filiz) |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | vuruş sütununda ardışık tekrar 0; 24 klibin 24'ü ayrı vuruş adı taşır |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | temaslı 7 klipte TEMAS/DEĞİŞİM/SONUÇ üç satır aynı klipte; temas noktası merkez üçte birde; temas ilk 2 s'de kurulu |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IN FRAME satırı 48/48; yüz yalnız 4 klipte; insansız 4 klipte `none` |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | üretim defterinde üç kutu; üçüncüsü yapısal: kadrajda konuşan ağız 0 klip (tek replik CİHAZDAN) |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | MUZIK katman ≤4 · köprü ≥0,2 s · kayıt sesi bant-limitli · efor klibinde zorlanmış nefes |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | tek repliğin İŞLEVİ görünmeyeni taşır: ÇOCUKLAR (ekranda hiç yok) ve artık cevaplanamayacak bir RİCA |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | 10 kart tetikleniyor: 3 kask · 4 ikinci figür · 5 ekran/metin (K11 arşiv levhası) · 6 parçacık · 6b katmanlı dünya · 7 diyalog · 9 baskın ışık · **10 insansız sahne** · 12 politika · 13 yapı ölçeği → 5+ risk, KİLİT TAVANI ≤20 |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 542 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A4 yasaklı sahne tipi: iniş/biniş + loş mekâna giriş hareketi 3 sınırda KADRAJ DIŞI (K04→K05 · K09→K10 · K17→K18); A5 1 numaralı risk KÜRE sayıyla; B5c üretim sırası K21'den başlar |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | B5 dörtlüsü doldu; İSTEK bir İŞ (çekirdeği bağlamak), BEDEL sahne numaralı (S5·K17 + S6·K20), MUHATAP kendi geçmiş kararı |
| ✅ | `KILAVUZ_REHBERI.md` | 2545 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.3 24 klip/2 bölüm · §3.9 ortam kartı + KURU-BERRAK alt bandı (3 sapma D74) · §4.1 tür · §5.1 çekirdek 8/7 cümle · §5.1b PHYSICS+AUDIO |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 437 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3-S iskeleti birebir: IN FRAME · Clip n of 24 · CONTINUOUS ACTION · üçüncü satır TEK KİLİT · START FRAME tek satır · bant 100-250/120-300 |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | NOVUM TAŞIYICISI: anahtar çubuğu × halka kilidine sokup çevirme → üç halka açılır, güneş aralarından yükselir (tip ÖLÇEK, tablonun 2. tercihi) |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 314 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | TEMA FEDAKÂRLIK (§3 sekizlisinden); TANIM cümlesi TAKAS kalıbı DEĞİL: *Bir şeyi geri veren, geri veremediklerinin önünde bekler.* |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | HOOK TİPİ ölçek şoku · K01 0. kare 120 px'te okunur · S1 ikinci bilgi K02 · katalizör 0:20-0:30 (bant 24-36 s) · BİLGİ ASİMETRİSİ satırı TERS İRONİ olarak yazıldı |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 396 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | ardışık çift ≥1 kademe + ≥45° · kurulum ≤12 · DÖNÜŞ ≥%40 (küme ARANMAZ) · ŞOK ≤2 · dönüş işareti `— the same position, height and lens as Clip N.` |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | ⭐VİRAL kapısı iki kanal ister; 3 aday ölçülecek (K12 · K17 · K21) — hedef değil ÖLÇÜM; §2.3 açılış-kapanış çifti K01↔K24 |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 324 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | sabit ızgara gerekçe satırı ZORUNLU · MİKRO kırıcı sahne içi her kesmede ölçek · MAKRO 3-4 klipte mekân/tempo · ihraç −14 LUFS / −1,0 dBTP / 1440p+ |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | 8 satırlık kart yazıldı (BASKI TEPKİSİ: KONTROL EDER) · ALIŞKANLIK avucu yüzeye basmak ×3 + K20'de kırılma · DAVRANIŞ ŞERİDİ 24 harf, G %30 |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | İZLEYİCİ CÜMLESİ her klipte · ÇAPA ÜÇLÜSÜ K16/K17/K23 · niyet kanalı ≤2 · dolgu jesti (eldiven/kask kontrolü) 0 · TEMPO sütunu |
| ✅ | `COK_KLIPLI_SAHNE_KILAVUZU.md` | 403 | **[cok-klip]** · yatay film: sahne 2-6 klip · §2 kapsama şablonu · §3 CONTINUOUS ACTION · §4 sahne kilidi · zincir yok · ㉜ (PLAN'da SAHNE PLANI yoksa "—") | SAHNE PLANI 3 6 3 2 3 4 3 · kapsama şablonu her sahneye · CONTINUOUS ACTION 17 klipte (IMAGE+VIDEO) · sahne kilidi birebir · zincir dili 0 · §3.6 temas iki klibe bölünür |
| ✅ | `FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` | 243 | **[efor]** · §1 destek·gövde·işaret·duraksama · §1.5 saydamlık tuzağı [D175] · §2 düşük g'de düşüş dili · çarpma üç evre (efor/düşüş yoksa "—") | DESTEK+GÖVDE+2 işaret+DURAKSAMA; direnç NESNEDE (`the socket seat bound by frost`); `slowly` yok; `free fall/plummets` yok; ödeme sonraki klibe taşınır |
| ✅ | `POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md` | 167 | **[darbe]** · §1 toparlanma merdiveni = D207 · §2 hasar düz cümle + referans sayfası · §3 kadro sayı kilidi (darbe/hasar/kadro çıkışı yoksa "—") | — |
| ✅ | `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md` | 181 | §1 mikro→makro · §2 yürüme platosu · §3 temas iki klibe · §4 filigran = araç · tripod ADAY-98 | ⭐ mikro→makro: anahtar DİSK değil ÖN KOL BOYUNDA ÇUBUK, iki elle sürülüp omuzla çevrilir; levhayı kapatma avuçla; CAMERA satırında `tripod` yok; yol klibi sahne başına 1 |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 444 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | kilit fiili SÜREÇ (24/24) · TIMELINE ≤3 satır · son satır SÜRDÜRME · sahne başına tek çevre saati (kırağı tüyü / kaidedeki ışık) · zemin bağı cümlesi |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | yasak SİLİNİR malzeme TARİF edilir; `wounded/dying ship` ve `dull orange glow` YAZILMAZ (red defteri #4); en red-riskli kare K21, nötr tarifi yazıldı |
| ✅ | `PROMPT_HATA_ONLEME_KILAVUZU.md` | 456 | §1 on kilit · §2 ORTAM CÜMLELERİ (kopyala-yapıştır) · §3 15 hata sınıfı · §4 promptun kapatamadığı üç sınıf · §5 novum kilidi · §7 --kilit ölçümü (19.09.2026 · 31 film / 688 bulgu) | §2'de §3.9 için hazır cümle YOK → bu film yazacak · §3b temas ilk 2 s · §5b efor beden+duraksama · §6 jeton sızıntısı (büyük harfli dizge yok) |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | — |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | tek replik bir CİHAZDAN; muhatap kadraj dışı ve ARTIK YOK; dinleyen bedeni K10'da yazılı; replik klibi sahne başına ≤1 |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | kaynak kilidi + kadraj kilidi + negatif üçlüsü (D82); BEDENLEŞTİRME yok ve yapısal olarak İMKÂNSIZ; sessiz 22 klipte `no speech of any kind` tam listesi (D99) |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | §3 metinsiz amblem: bu filmde amblem HİÇ YOK — imparatorluk yalnız BİÇİM (kaburga + üç halka); §4 sırt C DÜMDÜZ; §8 kişisel eşya: fener |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | arketip **K** (üç hafifletmeyle: matte+scuffed+tekstil eklem) · kask tipi 2 (düz pane + KALIN çerçeve) · çene içi 3200K · ⛔ M arketipi (dar pencere) KULLANILMADI |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | T1·T2·T3·T6 doğru → paket YAZILACAK; 6 kayıt (RK1 zırh · RA gemi · RB kaide · RO küre 2 hâl · RP çekirdek+çubuk · RD şehir) · sayfada 0 yazı |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1333 | tamlık matrisi satırı 0/4 olarak eklenecek; 4 dk başlığı 24 → 25 film |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | ⭐ #2 YAPISAL RED: insansız sahne + uzun NEGATIVE + `Exactly 0 human` → GEÇEN çözüm: NEGATIVE tek pozitif satıra indi. #3 kask ÇIKARMA = PB red → anahtar GEMİDE, gövdede değil. #4 `wounded ship` + `dull orange glow` = PK+PB |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | Karakter sütunu dokuz filmde 2-4 — kırılmayan darboğaz; kamera-taşıyıcı testi her klipte koşuldu |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | kapandı (T2'ye katıldı); sayaç mantığı maddesi okundu — küre durumu sahne başına tek yönde ilerler, geri dönmez |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | kapandı (T2'ye katıldı); pasaport kalıbı SPEC C KİMLİK DİZİSİ satırına çevrildi |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | kapandı (T3'e katıldı); register haritası ↔ SPEC replik envanteri karşılaştırması D82'nin aracı |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 127 | yayınlanmış film 0 → ⭐viral ve loop iddiaları ÖLÇÜM değil; Content Loudness satırı yayından sonra yazılır |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | COUNTED_TURN 3,4 `THE CHOICE IS INVISIBLE` — merkezî kararda tereddüt/ağırlık sıçraması yok; ÇAPA ÜÇLÜSÜ bu yüzden BEFORE/AFTER beden çiftiyle yazıldı |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | COUNTED_TURN 6,8 `KEY WALKS` (ışık 3→9 saat) · HARD_DOCK 5,5 renk sıcaklığı sıçraması → ⚠️ bu filmde ana ışık ELDE TAŞINAN FENER; yön saatle değil KAYNAKLA kilitlendi, YANLIŞ-POZİTİF DUVARINA yazılacak |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | HARD_DOCK `LEAVES AT 00:25` kokpit-dış platosu · COUNTED_TURN ızgara platosu → S2'nin 6 klibi plato riski, her klipte beden başka işte (MIKRO §2) |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 104 | ⑬ gönderilen promptla ölçer → ÜRETİM DEFTERİ boş doğdu, üretimde satır satır dolacak; defter olmadan ⑬ koşulmaz |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 64 | AMAÇ CÜMLESİ: her klipte bedenin neden o hareketi yaptığı ekranda; amaçsız hareket 0 (FALLING_WORLD 7,8) |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 64 | yönelmiş her eylem nesneye bağlı (D174); FALLING_WORLD 8,2 · bakış hedefi TIMELINE'da nesne |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 92 | ölçüm sapması ±1,3 puan — 1,5'ten küçük fark FARK DEĞİLDİR; HARD_DOCK 7,4 mod D emsali |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 128 | GÖVDE 1-6 / DÜNYA 7-13 ayrımı: bu mercek tasarım gereği mod V; SPEC'in `sahne içi kesmeler` listesi ona hangi kesmelerin eşleşmesi gerektiğini söyler |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 106 | STEP 0 ses varlık kapısı: sessiz film ≠ sesi ihraç edilmemiş dosya; register şerhi — kayıt sesi MACHINE değil RECORDED HUMAN |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 94 | IRON_SLOPE 2,6 · COUNTED_TURN 5,6 — en düşük hücreler hep Bedel ve Final; ④'ün kesme listesi doruğu kesmeyi önerebilir (KEPT_LIGHT vakası) → KESİLEMEZ listesi yazıldı |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 113 | STILL_SWARM 4,3 `FIELD COLLAPSES` · SOLAR_MIRROR `SUBJECT DUPLICATE IN FIELD` → arka plan envanteri kurulum harfiyle BİREBİR döner (sınıf 11) |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 96 | IRON_SLOPE `TWO GRAVITIES` · mod V'de kilit tablosu yok → SPEC'e kilit tablosu yazıldı (tek g, düşüş süresi, küre iki hâl) |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 78 | COUNTED_TURN 4 temas penetrasyonu + `S21 eylemsiz beat` · HARD_DOCK `docking impact elided by cut` → temas üç satır aynı klipte (D213) |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 78 | ⭐ deponun EN DÜŞÜK ekseni: COUNTED_TURN 0,0 · RESONANT_STRAND 1,0 · SOLAR_MIRROR 2,9 `WEIGHTLESS WORK` → 6 efor klibinin her birinde saniyeli ödeme satırı |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | HARD_DOCK 8,7 ama kafiye kategorisi 2/10 (`S24 closing setup mismatch B vs A`) → K24'ün CAMERA metni K01'den BİREBİR kopyalanacak |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (72 dosya · 18170 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_KEPT_LIGHT` | ① aynı format — yatay_4_dk · 25 klip · fener bekçisi | ⛔ KAFİYE ÇİFTİ BAŞARISIZ: S0 tepeden CU ↔ S24 alttan alt açı — *aynı kurulum değil, kameranın YERİ de değişti*. + kuyruk kartı 5,0 s · filigran 6/6 · planlı sessizlik gelmedi · −16,4 LUFS / +0,9 dBTP. ⭐ NOVUMUN SINIRI SIZDI: kural ağzın altındaydı, kurgu onu ağzın ÜSTÜNDEKİ havaya da verdi — sınır kareyle sınanmadı |
| ✅ | `THE_HEALING_GROUND` | ② aynı ortam kartı — §3.9 kriyojenik orta basınç kartının REFERANS filmi | kart 4,99 s ve kartın GÖRSELİ filmin dünyası değil (turuncu gök + dev gezegen ↔ filmin soluk kum paleti) · SPEC + paket VARDI, operatör çıplak rubrik yapıştırdı → 13. mod V filmi · ④ 3,0 |
| ✅ | `THE_COUNTED_TURN` | ③ aynı tema — fedakârlık/bedel hattı · 25 klip | ⑧ EFOR **0,0 NOBODY PAYS** (6 iş olayının 6'sında beden ödemiyor) · ⑩ **3,4 CHOICE INVISIBLE** · ⑪ **KEY WALKS** · temas cümlesi 22/25'te yazılıydı ve 7 🔴 geldi → cümle değil KADRAJ kararı |
| ✅ | `THE_CRACKED_HELMET` | ④ en düşük skor — ⑧ 1,0 · ⑨ 2,1 · ⑩ 2,0 — üç eksende dip | kostüm siyah↔beyaz 12 sahnede 5 kez · amblem omuz↔sırt ışınlanıyor · S7'de vizör KAYBOLDU · göğüs kutusuna `ORION` yazıldı · S12'de açıklamasız ikili gün batımı → tek giysi DEĞERİ, amblem HİÇ YOK, vizör 24/24, ışık olayı İLAN EDİLDİ |
| ✅ | `THE_SOLAR_MIRROR` | ⑤ en yakın konsept — güneş/ayna filmi · jeton sızıntısı vakası | ⭐ `S04` SAHNE ETİKETİ hava kilidi gövdesine BASILDI (metin yasağı 12/12'de yazılıyken) → promptta büyük harfli hiçbir jeton yok · ⑧ 2,9 WEIGHTLESS WORK · ⑪ `LIT FROM NOWHERE` |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  26  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   51
ZORUNLU SATIR:   16833
SEÇMELİ KAYIT:   5 / 72  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

## 📝 "—" SATIRLARININ GEREKÇESİ — kilit çıkmayan satırlar

> ⛔ Çizelgenin son hücresi kapı tarafından TAM `—` olarak okunur (㉘); gerekçe
> bu bloğa yazılır. "—" MEŞRUDUR: her dosyadan kilit çıkmaz.

- **DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS** → (kontrat yazım kuralı; bu film ders YAZMIYOR, ders UYGULUYOR)
- **D198** → (hiçbir kare 0 g'de değil; film boyunca tek g = 0,38)
- **D201** → (vakum sahnesi yok; S1 gezegenin gece havasında 2 km'de geçer — tek ortam kartı §3.9)
- **POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md** → (darbe · hasar · kadro çıkışı YOK; kimse düşmüyor, çarpmıyor, yaralanmıyor — travma merdiveni tetiklenmiyor)
- **IKI_KISI_VE_AYRILIK_KILAVUZU.md** → (tek insan; ikinci figür 0 klipte — kart 4 riski negatif çekirdekle kapatılıyor)
- **FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md** → (dikey hat tablosu; bu film yatay)

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
