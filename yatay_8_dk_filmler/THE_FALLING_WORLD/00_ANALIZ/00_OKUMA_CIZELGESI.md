# 📖 THE_FALLING_WORLD — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 18.09.2026 10:13
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 40 dersin 34'ü bu filme düşüyor; `vakum` · `dikey` · `faz` etiketli satırlar `—`. Kilit tavanı ㉕: PLAN'da en çok 20. |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | Kilit olarak dersin DEĞİŞEN SATIR sütunu alınır, ders metni kopyalanmaz. |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 48 video CAMERA satırı `In a single continuous shot.` ile biter; sahne = klip, sahne içi kesme yok. |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask · ETİKET UYMUYOR: vizör tasarım gereği tamamen opak, morph yüzeyi fiziken kapalı | — |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | SPEC B `SCREEN TEXT: 0`; özel ad promptta yok; araç ayarı kutusu üretim defterinde [D215]. |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | SPEC C YIPRANMA: BEYAZ 3 sabit bölge (sol manşet · sağ diz · sırt altı), TURUNCU 2 (iki diz); başlangıç S00. |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Prompta `[LESSON n]`, etiket, künye, Türkçe başlık girmez; gövde yalnız sahneyi yazar. |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | PLAN KESİLEMEZ LİSTESİ: S41 doruk · S42 seçim · S45 kalkış · S47 final + 8 nefes sahnesi. |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Kurgu kapısı: süre = 48 × ölçülen klip süresi; jenerik/başlık kartı 0 s. |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Çöküşün ilerlemesi TEK KAREDE kanıtlanır: yarık genişliği gövde-göreli ölçülür (S00 bir eldiven · S19 bir gövde boyu). |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Promptta metre yok: ölçü gövde boyu · eldiven eni · kol boyu. Metre yalnız PLAN ve SPEC'te. |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | `IN FRAME: back` olan promptta pozitif sırt cümlesi; iki sırt ünitesi POZİTİF ayrışır (köşeli geniş ↔ dar). |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | SPEC B FİNAL VURUŞ KANITI: S47'de iki kabin ışığı sayılır (2) ve gemi kadraj eninin ⅓'ünü geçmez. |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | Vizör biçimi sayıyla: tek düz ön pane + kalın koyu çerçeve. `seamless` · `dome` · `bubble` yasak. Pane OPAK — D79 sapması ayrı kayıtta. |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | TEK KARE cümlesi taşıyıcının ADINI taşır: sarı emniyet halatı. |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Prompt gövdesinde figür başına ≤3 öznitelik (renk · omuz · sırt); yaş · boy · ten PLAN'da kalır, prompta inmez. |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | Efor sahneleri S20-S24 (direk) · S27-S28 (çekiş) · S34-S35 (manuel kol): her birinde gövde tepkisi cümlesi. |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Sarı halat mekanizma değil emniyet hattı okunur: her sahnede İKİ UCU da adlandırılır (kimin kemeri ↔ hangi nokta). |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | Yön cümlesi nesne-göreli: `toward the ridge where the ship stands`; pusula ve ekran koordinatı yok. |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Mühür korunur: `through/under the glove` yazılmaz; hasar eldiven/manşet YÜZEYİNDE tarif edilir, anatomi değil. |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | Zemin tek cümle tek renk: kırık yerlerinde kül grisi siyah bazalt; ikinci bir zemin tarifi yazılmaz. |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | İmaj = ÇAPA'nın BEFORE'u. ⭐ DÜŞÜŞ ANI KAREDE YOKTUR — kare her zaman tutuşun yük aldığı andır (OMNI §3②). |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | Mutlak sessizlik modelden istenmez; ince atmosferin boğuk zemini her klibin AUDIO satırında. |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | 1 numaralı risk S42: kesilen hattın HANGİSİ olduğu. Pozitif biçim + sayı — kesik uç bir kol boyu serbest savrulur, bir saniyenin altında. |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | SPEC C IŞIK TAKVİMİ: tek güneş film boyu aynı saat yönünde; ardışık sahne farkı ≤30° / ≤500 K. |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | 0,30 g yazılır: düşen nesne ilk saniyede ~0,15 m; kopan parça kazandığı dönme eksenini sürdürür. |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | Tek g: kabin içi de 0,30 g (basınçlı iç hacim kartının 0 g satırından sapma — 02_KONSEPT D74). |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum · ETİKET UYMUYOR: ortam ince atmosfer, güneş yönü kilidi D209 + D193'te | — |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ÇAPA ÜÇLÜSÜ: CHOICE S41 · COST S16 · FINAL S47 — her biri aynı kanalda BEFORE/AFTER gövde çiftiyle. |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | SPEC `DIALOGUE LINES: 8` = promptların AUDIO satırındaki post-dub telsiz replikleri; gövdede tırnak yok. |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | BEDEL EĞRİSİ: sol kol S16'dan S47'ye hiçbir karede yük taşımaz; hücreler `<kanal> @ <saniye>` yazılır. |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | Yorgunluk 0-6, ardışık düşüş ≤1; S25 düşüşünün kalıntısı S26-S28'in 0,0 s satırında taşınır. |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | SPEC C KİMLİK DİZİSİ: kask biçimi · omuz rengi · sırt ünitesi · kir kademesi · sol manşet hasarı. |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | World Bible ÜÇ cümle birebir: zemin · ufuk · gökteki merceklenmiş diskin yönü. SPEC C DÜNYA ÇAPASI 3/3. |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | İskelet A…A: S00 ile S47 aynı kurulum ailesi; her CAMERA satırı `absolutely zero camera movement` taşır. |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S00'ın soru cümlesi PLAN'da yazılı; S47'nin son karesi adlandırılmış; ilk 30 s'de ≤2 kurulum. |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Sahne haritasının VURUŞ sütununda ardışık tekrar 0; 48 klipte birebir tekrar eden klip 0. |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | TEMAS · DEĞİŞİM · SONUÇ aynı klipte: S02 (kayış ayrılır → sandık düşer → Turuncu yukarı gelir) ve S42. |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Her promptun ilk satırı `IN FRAME:`; yalnız kadrajdaki tarif edilir, Bible'ın kalanı yazılmaz. |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Üretim defterinde üç araç-ayarı kutusu; NEGATIVE'e bu yüzden cümle EKLENMEZ. |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | MUZIK: katman ≤4 · köprü ≥0,2 s · telsiz filtresi · −14 LUFS / −1,0 dBTP. |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | 8 repliğin İŞLEV hücresi görünmeyeni taşır; `Durum bilgisi` / `Ölçüm` yazan replik silinir. |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | RİSK SAYISI 11/14 → KİLİT TAVANI ≤20. Açılan kartlar 3·4·5·6·6b·7·8·9·10·12·13; KART 12 tavanın dışında. |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 540 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A0-E on sekiz madde 02_KONSEPT ve PLAN'a dağıtıldı. A4 üç yasaklı sahne tipi tetikledi: S04/S12/S43 biniş-iniş, S14 loş mekâna giriş. |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | Depoda replikli film 0/79, pozitif ikinci insanı olan 15. Bu film üç boşluğu da kapatıyor: İSTEK · BEDEL · MUHATAP dolu, muhatap ikinci insan. |
| ✅ | `KILAVUZ_REHBERI.md` | 2290 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.7 8 dk kartı (48 × 10 s · viral ara 8) · §3.2 ince atmosfer + §3.10 basınçlı iç hacim · §4.1 bilimkurgu · §5.1 çekirdek negatif · §7 D143/D145/D150 tuzakları. |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 427 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3 iskeleti: IN FRAME · `Scene n of 48` · START FRAME · üçüncü satır tek kilit · TIMELINE ≤3 satır · NEGATIVE 7/8 cümle. |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | NOVUM TİPİ = İLİŞKİ (üçüncü tercih, gerekçe plana). Taşıyıcı: sarı halat × Beyaz'ın kesişi ↔ Turuncu'nun kesişi → kim kimi kurtarıyor ters döner. |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | TEMA GÜVEN — §3 sekizlisinde yok, §3b'ye üçüncü aday satır. §5 matrisine bu filme özgü satır yazıldı (motif: uzatılan el / gerilen hat). |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | HOOK TİPİ in medias res; S00 soru cümlesi + S01 ikinci bilgi; katalizör S07 = 1:10-1:20 = %14,6 (bant %10-15 ✅). BİLGİ ASİMETRİSİ: dramatik ironi, taşıyıcı ①, an 6:00. |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | 48 sahne · kurulum tavanı 24 · DÖNÜŞ ≥%40 (≥20) · KÜME ≥2. Küme, sahibin 'her 10 saniyede yeni olay başlamasın' kuralının depo karşılığıdır. |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | ⭐VİRAL etiketi DÜŞÜRÜLDÜ: YÜZ kanalı opak vizörle fiziksel olarak kapalı. 8 ara sahne yalnız HAREKET taşır ve etiketsiz yazılır. |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | Sabit ızgara: `TARGET ASL BAND: 10,0 s` + gerekçe satırı. Örüntü kırıcı: ardışık iki sahne aynı ölçek+palet+ses dokusunda değil; her 3-4 sahnede mekân/tempo değişimi. |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | İKİ kart, ≥3 davranış satırında ayrışır. ALIŞKANLIK: Beyaz kesiciyi kullanmadan önce sol önkoldaki yuvaya iki parmakla vurur (S01 · S15 · S34), kırılma S39. |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | Her sahnede İZLEYİCİ CÜMLESİ + ≤2 niyet kanalı; TASK ONLY ≤24. Hazırlık sırası bakış → ağırlık → el, çapa sahnelerinde zorunlu. |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 438 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | 48 birimin kilidi ETKİNLİK/TAMAMLAMA fiili; TIMELINE ≤3 satır, son satır SÜRDÜRME; sahne başına tek çevre saati + zemin bağı cümlesi. |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | Üç yüzey: kesici (S01·S02·S39·S42) · düşme/kol hasarı (S16·S25·S37) · kimlik yığını. §3 imza ⑥ (yüzü kapatan ekipman) panzehirsiz → her kadrajda çevresel çapa cümlesi. |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | KONUM KİLİDİ BEYAZ sol / TURUNCU sağ · faz farkı (aynı saniyede aynı fiil yok) · AYRILIK S40 · tersinmiş ikinci ayrılık S24 · TEMAS ENVANTERİ 5 sahne (D74 sapması). |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | Muhatap: ikinci insan, KADRAJ DIŞI SES (merdiven basamak 1). Her replik DEĞİŞ-TOKUŞ tablosunda; dinleyen klibinde replik metni yok, gövdesi var. |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | 8 replik: register HUMAN, kanal telsiz, hepsi <5 s. Sayı söyleyen replik yok (insanda sayı yasağı). İlk replik S07 — öncesinde 70 s kesintisiz sözsüzlük. |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | İki figür DÖRT eksende ayrışır: renk · omuz parçası · sırt ünitesi · bilek. Metinsiz, amblemsiz, markasız; serbest uçlu hortum yok. |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | İki figür de arketip E (belgesel/tarihsel). Kask: tek düz ön pane + kalın koyu çerçeve; kask içi ışık YOK (pane opak) — §4'ün üç düzeneği bu filmde kapalı. |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | Paket YAZILIYOR, 4 sayfa: R1 BEYAZ · R2 TURUNCU · R3 HAT AİLESİ · R4 ARAÇ VE GEMİ. Sayfası olmayan RD (dış mekân) World Bible'ın üç cümlesine devredildi. |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1238 | Tamlık matrisi /4; 8 dk hattında iki film var, ikisi de eksik ölçülü. Bu film bölüm başına 12 mercek × 4 bölüm mü 2 yarım mı — K1 sahip kararı. |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | 14 vaka: 6 kelime · 4 kompozisyon · 1 yapısal. Bu filme düşen sınıflar PK (şiddet/tehlike sözlüğü) ve PB (yüzsüz izolasyon + kısıtlanmış uzuv, YERCEKIMI S8 — ÇÖZÜLEMEDİ). |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | ⛔ kapalı tablo, eğilim göstergesi: 13 satırın 7'sinde Tema ≤5 ve gerekçe hep 'bedel yok'. Bu filmde bedel dört sahnede numaralı. |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | ⛔ kapalı; Kostüm sütunu üç filmde 2-3/10 (Inversion · Kaleida · Tidal Hunt) — kask/vizör hattın ölçülmüş en net başarısızlığı, referans paketinin gerekçesi. |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 · ETİKET UYMUYOR: dikey hat tablosu, bu film yatay 8 dk | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | ⛔ kapalı; Karakter sütunu dokuz filmde 2-4 ve iki kayıtta gerekçe aynı: 'tepki veriyor, seçim yapmıyor'. Karar mimarisi S41-S42'de iki seçenekli yazıldı. |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | ⛔ kapalı; ses atama hatası sınıfı (yanlış bedenden çıkan replik) bu filmde post-dub ile yapısal olarak kapalı. |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | Kart Y satırı YÜKLEMEDEN ÖNCE açılır; tek değişken kilidi (kapak VEYA başlık) YAYIN_PAKETI'ne yazıldı. |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | ⑩ on filmde 2,0-6,3; dördünde `THE CHOICE IS INVISIBLE`. Panzehir ÇAPA ÜÇLÜSÜ ve niyet kanalı sözlüğü — S41/S16/S47. |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | Ölçülmüş desen: aynı mekânda renk sıcaklığı sıçraması ve güneş yönü dönmesi. Kilit: tek güneş, sabit saat yönü, SPEC C ışık takvimi. |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | Ölçülmüş plato: KRONOS B1 `LEAVES AT 02:15`, B2 `LEAVES AT 00:48` — ikisi de peş peşe konsol/şalter sahneleri. Bu filmde orta bölüm kesintisiz aksiyon. |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 85 | ⑬ sahne sahne koşar ve bölümden etkilenmez; KRONOS'ta iki bölümde de `INPUT MISSING` — SPEC ve promptlar rubriğe VERİLECEK. |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 63 | Amaçsız hareket ve zemin kayması sınıfı; panzehir zemin bağı cümlesi (`both boots stay planted…`) her sahnede. |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 63 | Hedef vektörü sınıfı: KRONOS'ta iki 🔴 FLIP. Kilit: hedef her sahnede nesne-göreli yazılır, kim solda kilidi film boyu sabit. |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | Ölçüm sapması ±1,3 puan; 1,5'ten küçük fark fark değildir. Bu filmin kendi satırı üretimden sonra açılır. |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | 13 satırın ölçülmüş en zayıf sütunları: Kostüm · Ekipman · Nicelik+Sayı (1-3/10). Sayılabilir öğe sayısı minimuma indirildi ve SPEC'e kilitlendi. |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | MACHINE register'ın düz okuması tasarımdır, ceza değil. Bu filmde makine repliği yok; 8 replik HUMAN, telsiz filtreli. |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | Canlı sistemde 5 satır; en yüksek THE_HARD_DOCK 8,1 (aynı yazım hattı, 24 × 10 s). Hedef bant o satır. |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 110 | Derin tarama; ikinci figür ve katmanlı dünya riski taşıyan filme koşulur — bu film ikisini de taşıyor, koşu planlanacak. |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 94 | Mod D'de SPEC'in sayısal kilitleri tek tek doğrulanır; PLAN'ın g · düşüş · halat gerilme sayıları NUMERIC LOCK LIST'e girecek biçimde yazıldı. |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 76 | Vuruş okunurluğu: KRONOS'ta 11/11 ve 15/18. Bu filmde 48 vuruşun her biri sahne tablosunda tek satırla adlandırıldı. |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 76 | `NOBODY PAYS` ve `WEIGHTLESS WORK` sınıfı — basınçlı giyside sıfır efor. Kilit D169: her efor sahnesinde gövde tepkisi + kadans cümlesi. |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | `RHYME BROKEN` sınıfı: KRONOS'un iki bölümünde de açılış-kapanış kafiyesi kurulmamış. S00 ↔ S47 çifti PLAN'da yazılı. |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (70 dosya · 16957 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `01_FILM_RAPORLARI/KRONOS_SON_SINYAL.md` | ① aynı format | Aynı hat, 8 dk, iki bölüm, 30 mercek. Ölçülmüş arızalar: çift karakter spawn (2 vaka) · vakumda ses · NOBODY PAYS · RHYME BROKEN · kilitli kamerada creep · her karede filigran · orta bölümde konsol sahneleri. |
| ✅ | `01_FILM_RAPORLARI/THE_SKYLIGHT.md` | ② aynı ortam kartı (§3.2 ince atmosfer) | D143-D150'nin kaynağı: toz şelalesi · alçak açıda uydurulan kanyon duvarları · bir filmde üç kask · kir merdiveninin sıfırlanması · filigran. Beşi de bu filmin ortamında tekrar edebilir. |
| ✅ | `01_FILM_RAPORLARI/THE_ROSE_COAT.md` | ③ iki figürlü emsal (tema karşılığı yok — GÜVEN ilk kez) | Deponun 12 sahne boyunca iki figürü kadraj kilidiyle tutan tek filmi (§4.1 emsali). Bedeli: SPEC yanındaydı, verilmedi → beş merceğin beşi ön koşu. |
| ✅ | `01_FILM_RAPORLARI/THE_COUNTED_TURN.md` | ④ en düşük skor | ② DEVAMLILIK 3,0 · ⑩ OYUNCULUK 3,4 `THE CHOICE IS INVISIBLE`. Kimlik ve kostüm sütunları 1/10. Referans paketi ve kimlik dizisi bu satır yüzünden yazılıyor. |
| ✅ | `01_FILM_RAPORLARI/THE_LAST_SPAN.md` | ⑤ en yakın konsept (uçurum · geçit · kurtarma · politika yüzeyi) | İki aksiyon doruğu politika reddi aldı; sebep NEGATIVE bloğuna yazılmış yasak sözlüğüydü (gore 29 · blood 26). Bu filmin kesici ve kol hasarı sahneleri aynı sınıfta. |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  21  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   46
ZORUNLU SATIR:   14951
SEÇMELİ KAYIT:   5 / 70  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
