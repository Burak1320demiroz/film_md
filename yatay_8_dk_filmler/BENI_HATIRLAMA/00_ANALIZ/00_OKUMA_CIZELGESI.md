# 📖 BENI_HATIRLAMA — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 17.09.2026 00:03
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 38/40 ders etikette düşer; D198/D201 dışarıda (çıkarımlar A1) |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | kilit = PLAN sütunu/prompt satırı/SPEC satırı; "dikkat edilir" yazılmaz |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 48 klip × tek çekim; S10→S11 ısı görüşü geçişi KESMEDE |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | baba yüzü ≤3 öznitelik aynı cümle; yüz yalnız S1·S36-S38·S44 okunur |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | başlık/jenerik kartı 0; S47 "take ends on the held frame"; film adı prompta 0 |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | kir 4 faz F1 düzlük→F2 mağara→F3 fırtına→F4 kokpit, yeri sabit, geri temizlenmez |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | özel ad (kız/baba) + [etiket] + lens verisi prompta 0; kamera cümle |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S47 finali üretim sırasında 3. — kesilemez listesi S0·S11·S30·S36-S39·S47 |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | kurgu kapısı: klip=sahne=48 · ekran metni 0 s · jenerik 0 |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | bilek lamba halkası 5→4→3→1→0 tek karede sayılır; ışık seviyesi ardışık 2 sahnede |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | metin yasağı giysiye/cihaza/ısı görüşüne kapsamla; ölçü yüzeye yazılmaz |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | arkadan görünen her sahnede (S12·S41·S42) pozitif düz sırt cümlesi |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | FİNAL VURUŞ KANITI S47: yellow scarf ×1 + amber light ×2 |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | 🔴 ref paketi yok → kask biçim kayması S36-S38 doruğunu vurur; 04_UYARI + D74 gerekçe |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | TEK KARE S15/S33: saydam kadın görüntüsü + altında sönen canlı ışığı aynı karede |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | kadın yüzü HİÇ tarif edilmez; baba ≤3 öznitelik |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | efor sahneleri S19·S25·S27·S41·S42·S44 gövde tepkisi aynı satırda |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | — |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | yön nesneyle: "toward the crevice / the vehicle hatch"; baba hep sol, kadın sağ |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | bare-skin negatifi "on the suited man" öznesine bağlı (kadın kasksız) |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | zemin tek cümle tek renk; kontrast öznenin kendisiyle |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IMAGE t=0: S13 çökmüş başlar · S30 atkı elde açık · S37 kadın hâlâ var |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | S37 sessizlik bıçağı KURGUDA hard mute; video AUDIO boş istenmez |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | 1 no. risk kadın görüntüsü: pozitif saydamlık cetveli + "never a second one" |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | iki takvim: dış ışık monotonik kararır · canlı ışığı eğri, sahne başına ulaşım mesafesi |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | — |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | tek ihlal görüntüye ait: gerçek kum/atkı rüzgârla aynı yöne, tek g |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | — |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ÇAPA ÜÇLÜSÜ: SEÇİM S36 · BEDEL S30 · FİNAL S45 önce/sonra beden |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | Türkçe replikler POST; promptta tırnaksız ses olayı + "Intended line (timing only)" |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | bedel bedende: S30 eller boş avuç yukarı · S41 omuz düşük tırmanış |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | yorgunluk 0-6 sahne sütunu, kesmede ≤1 kademe düşer |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | SPEC C KİMLİK DİZİSİ: kask K×48 · atkı · kadın saç/atkı/saydamlık |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | DÜNYA ÇAPASI 3 cümle birebir: kahverengi-gri bulut tavanı · koyu kum düzlüğü · kaya çıkıntısı+araç |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | kafiye çifti S0↔S47 kamera cümlesi birebir; her CAMERA lockoff |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ilk 10 s soru: kasksız kadın fırtına önünde; son kare adlandırılmış |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S20-S22 üç ayrı fiil (tara·bul·dokun); aynı klip iki kez yok |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S1·S30·S34·S36 temas-değişim-sonuç aynı klipte, merkez üçte birde |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IN FRAME ilk satır; ısı görüşü sahnelerinde baba kadrajda değilse tarif yok |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | üretim defteri 3 kutu: altyazı kapalı · filigran yok · konuşan ağız 0 |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | 3 ses yatağı (düzlük rüzgârı · mağara uğultusu · kokpit), katman ≤4 |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | iki kayıt cümlesi görüneni söylemez; baba hiç konuşmaz |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | 12/14 risk → KİLİT TAVANI ≤20; K2 yakın plan yürüyen canlı YOK (S18 geniş · S46 parça) |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 540 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A4: S9 gölge yokluğu ikincil, pozitif olay kum geçişi · A5 saydamlık sayıyla · B6 en riskli kare S13 |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | İLİŞKİ novumu (fizik değil) · diyalog merdiveni basamak 1-2 · MUHATAP geçmiş karar + kalıcı ağ |
| ✅ | `KILAVUZ_REHBERI.md` | 2288 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | ortam 3.4 kalın atmosfer · 4×12 dosya / QA 2 yarım · çekirdek ② iki-figür varyantı · değişen nitelik S37 |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 427 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3: IN FRAME + figür/canlı eki · "father/daughter" 0 · TIMELINE ≤3 |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | TEK KARE S15 (saydam kadın + sönen canlı) · başlık "Close Your Eyes, Dad" · kural 7 sahne 3 nesne |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 305 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | FEDAKÂRLIK · TANIM cümlesi (takas kalıbı değil) · motif S4·S29·S30·S36·S45 |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | yanlışlık kompozisyonu S0 · katalizör S6 %12,5 · dramatik ironi S33 · ilk 2 sn rüzgâr |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | kümeler S21-22 · S31-32 · S36-37 · S39-40 · alt açı yalnız S23/S46 · dönüş ≥20 sahne |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | orta nokta S24-25 sahte zafer · ⭐VİRAL S1·S42·S44 (YÜZ+HAREKET) · match cut S13→S14 |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | ASL 10 s sabit + gerekçe · sert kesme S10→11·S37→38·S43→44 · S37 dijital sıfır YOK |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | KONTROL EDER · cep bastırma S5·S16·S19 → kırılma S29 · TEL bilek halkasını örter |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | ÇAPA S36 omuz+başparmak · S30 eller · S45 cep · en büyük jest S36 · anti-RESET S13·S31·S38·S42 |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 438 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | 12 tutulan sahneye dış saat (atkı ucu·kum çizgisi·ışık kenarı) · "SON 3 s" sütunu |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | yara/ölüm sözlüğü 0 · S34 kayış açık başlar · çocuk sesi dalı → replik post · kırmızı yok, gri kaya çapası |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | görüntüye uyarlandı: AYRILIK S7 · tersinmiş S33-36 · KONUM KİLİDİ adam sol/kadın sağ · temas 0 |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | değiş-tokuş 6 kullanım · S8 cevabı ≤0,3 s (sahtelik) · dinleyen kadrajı S8·S36·S38 |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | 6 replik MACHINE (kayıt bandı) · bedenleştirme YOK · ilk replik S2 ≈22 s · yatak envanteri 4 |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | SOL pazu/uyluk arduvaz bant · SAĞ bilek 5 lamba · SOL bilek cihaz · eşya 2 (atkı+cihaz) |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | arketip E + kaş 2 lamba · kemik beyazı (kum rengi değil) · kir 3 kademe global · sırt heykelsi |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | 5/6 tetikleyici doğru, sahip reddetti → D74 satırı + 🔴 · Scene Foundation telafisi |
| ✅ | `UZAYLI_VARLIK_TASARIM_KILAVUZU.md` | 376 | havuzdan açıldı · insan-dışı canlı — PLAN önce zorunlu | EMPATİ→HUŞU · fok yavrusu + 6 bacak + deri altı ışık · K4 yalnız S11 ve S39-40 · sayı K0-K3'te yok |
| ✅ | `SAHNE_ZINCIRI_VE_SINIR_KILAVUZU.md` | 436 | havuzdan açıldı · durum değişimi sınıra | ışık değişimi ilerleyen kenar (hareket) · S37 ilk+son kare önerisi ⬜ · 47 sınır satırı |
| ✅ | `OMNI_1_1_FLASH_I2V_URETIM_KILAVUZU.md` | 414 | havuzdan açıldı · motor OMNI | "In a single continuous shot." · "No dialogue. No music." · S29 atkı yüzü kapatmaz · ses post-dub |
| ✅ | `DUNYA_GORUNUSU_KILAVUZU.md` | 341 | havuzdan açıldı · World Bible | arketip F · gök cismi yok · araç sol/çıkıntı sağ · 3 biyom, değişim yalnız sınırda |
| ✅ | `ISIK_SENARYOSU_KILAVUZU.md` | 322 | havuzdan açıldı · Lighting Bible | kaş lambaları S19-24 yanık/S25 söner/S41 yanar · uzun gölge YOK (difüz) · light shafts yok |
| ✅ | `YUZ_VE_KAST_KILAVUZU.md` | 293 | havuzdan açıldı · yüz yarısı | sapma kaş kemiği · 50'lerin sonu · kadın yüzü YOK, saç tek satır |
| ✅ | `ACILIS_KAPANIS_CIFTI_KILAVUZU.md` | 260 | havuzdan açıldı · çift kartı | KAFİYE · atkı sağ üçte bir S0↔S47 · değişen: atkının taşıyıcısı (+mekân gerekçeli) |
| ✅ | `FINAL_VE_PAYLASIM_KILAVUZU.md` | 420 | havuzdan açıldı · final tipi | MUĞLAK + erken twist · tohum S5 kehribar nokta 2 s · paylaşım HUŞU S32 · kapanış %6,25 |
| ✅ | `KARAKTER_VE_DUYGU_KILAVUZU.md` | 462 | havuzdan açıldı · bağ bütçeleri | göz ≥6 sahne · el ≥7 · yürüyüş ≥5 · Kuleshov ≥16 · görünür nefes · S37 müzik kesilir nefes kalır |
| ✅ | `PAKETLEME_VE_VAAT_KILAVUZU.md` | 241 | havuzdan açıldı · kapak anı | KAPAK ANI S0 ≈0:04 · 4 yüzeyde canlı/ısı görüşü 0 · vaat S8'de teslim |
| ✅ | `KAMERA_ACISI_PSIKOLOJISI_KILAVUZU.md` | 205 | havuzdan açıldı · vuruş→açı | keşif OTS · yenilgi üst açı 15-30° · epifani profil MS · dutch yok · sünger kum/atkı, toz değil |
| ✅ | `KURGU_VE_TESLIM_KILAVUZU.md` | 225 | havuzdan açıldı · kurgu kapısı | Çehov kurulum listesi 7 halka · bozulma karesi damar ağında · son üç klip elle |
| ✅ | `UZAMSAL_HARITA_VE_EKRAN_YONU_KILAVUZU.md` | 1269 | havuzdan açıldı · sabit hedefe hareket | SPATIAL MAP · S12 geri yürüyüş ters yönelim açık yazılır · S16 ışık mıknatısı 4 kanal · S1 master |
| ✅ | `UZAY_USSU_VE_ISTASYON_MIMARISI_KILAVUZU.md` | 604 | havuzdan açıldı · iniş aracı büyük yapı | araç ≈4 gövde boyu · kapak eğilerek geçilir · ölçek merdiveni S1→S43 · Ay/Mars negatif bloğu YOK |
| ✅ | `SAHNE_DEVAMLILIK_KILAVUZU.md` | 386 | havuzdan açıldı · çapalama | Scene Foundation: boş mağara master + 4 ışık durumu · seed OMNI'de belgesiz |
| ✅ | `TEK_CEKIM_VE_GIZLI_GECIS_KILAVUZU.md` | 480 | havuzdan açıldı · sahne sınırı | omurga 35 mm · gizli geçiş S19→20 perde · S41→42 kum · S29→30/S34→35 hareket eşleşmesi |
| ✅ | `MESHUR_SAHNE_KALIPLARI_KILAVUZU.md` | 306 | havuzdan açıldı · kalıplar | K12 fırtınaya karşı S42 (perdesiz) · K16 karanlığa fener S19/20 (huzmesiz) · K11 ufukta duvar S0/S6 |
| ✅ | `UZAY_SENARYO_KILAVUZU.md` | 795 | havuzdan açıldı · tür senaryosu | yumuşak bs · ısı görüşü lensi S1'den kurulur (deus ex machina yok) · Overview S43 · 3. aynı jest yok |
| ✅ | `VEO_3_1_FAST_DIYALOG_VE_VIDEO_URETIM_KILAVUZU.md` | 228 | havuzdan açıldı · yedek motor | concept bleed: atkı rengi ile kehribar ışık ayrı cümle |
| ✅ | `GOOGLE_FLOW_MUSIC_URETIM_KILAVUZU.md` | 580 | havuzdan açıldı · MUZIK | 72 BPM · tek çözülme S46 · S15→S31 yarım cümle · S37 müziksiz · [No Vocals] |
| ✅ | `KAPAK_FOTOGRAFI_MIMARISI_KILAVUZU.md` | 155 | havuzdan açıldı · KAPAK | koyu zemin+sarı atkı · sağ alt kör nokta boş · Plan B vizör yüzü |
| ✅ | `VIRAL_BASLIK_VE_ACIKLAMA_PROMPT.md` | 388 | havuzdan açıldı · YAYIN | durum kancası başlık · twist adı yok · AI beyanı tek satır · spoilersız bölüm adları |
| ✅ | `SERI_VE_KANAL_STRATEJI_KILAVUZU.md` | 366 | havuzdan açıldı · §3 | — |
| ✅ | `YAYIN_VE_PERFORMANS_KILAVUZU.md` | 370 | havuzdan açıldı · §2.2 | — |
| ✅ | `SINEMATOGRAFIK_TEKNIK_KILAVUZ.md` | 759 | havuzdan açıldı · §17 | küresel lens · highlight roll-off dili · anamorfik parlama yok |
| ✅ | `FRAGMAN_KILAVUZU.md` · `DIKEY_MIKRO_DRAMA_KILAVUZU.md` · `SHORTS_SISTEM_PROMPTU.md` · `5_FAZ_MIMARISI.md` · `FAZ_DOSYASI_SABLONU.md` · `YANASMA_VE_KENETLENME_KILAVUZU.md` · `SAVAS_SENARYO_KILAVUZU.md` · `DIS_REFERANS_OLCUMU.md` | — | havuzdan açıldı · başlık tarandı, etiket filme uymuyor | — |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1227 | 8 dk hattının ilk filmi · 4×12 dosya ↔ QA yarısı ①.9 alarmı (MARS emsali) → QA birimi sahip kararı |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | #15 kimlik yığını → yüz yalnız face promptta · #13 yan yana iki kol → S27 yan açı · MOTOR/İLERLEDİ/AŞAMA |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | — |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | — |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | IDENTITY BREAK üç film → adamın yüz kilidi + erkek çapası |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | — |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 125 | — |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | CHOICE INVISIBLE → S36 omuz+başparmak çapası |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | KEY WALKS + yüzde renk sıçraması → S35-S38 tek ışık kurulumu |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | plato "leaves at 00:25" → mağara bloğunda 3-4 sahnede makro kırıcı |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 85 | — |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 63 | — |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 63 | — |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | jenerik kartı + eldiven/kayış penetrasyonu → kart 0 · atkı/kayış "rests on top of the glove" |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | erkek↔kadın yüz kırılması → adam yüzü ile kadın figürü aynı yüz kadrajında YOK |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | MACHINE register düz okuma tasarım → 6 kayıt kullanımı |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | — |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 110 | SUBJECT DUPLICATE (yansıma) → vizörde yansıma yok, görüntü ayrı tarifli |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 94 | — |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 76 | darbe kesmede elips (Hard Dock B4) → S30/S36 temas klip içinde |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 76 | NOBODY PAYS / WEIGHTLESS → S19·S27·S41·S42·S44 gövde tepkisi aynı satırda |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | kafiye kurulum kayması → S47 harfi ve kamera cümlesi = S0 |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (70 dosya · 16957 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | **MARS_SON_CIKIS** (6 dk bölümlü, 8 dk'da film yok) · **THE_HARD_DOCK** (24-sahne modülü, 12 mercek) | ① aynı format | durum taşıma (önceki sahnenin son durumu imajda) · ①.9 yapı alarmı · S47=S0 kurulumu |
| ✅ | **THE_HERD** (§3.4 kalın atmosfer referans filmi) | ② aynı ortam kartı | kask baloncuğu takvime rağmen kayboldu (🔴 D146) · Çehov nesnesi kenarda okunmaz → atkı merkez |
| ✅ | **LOW_POWER** (fedakârlık/devretme + kayıt sesi) | ③ aynı tema | replikte yanık altyazı → post + heard only · tırmanış eforu S41 · kafiye dutch ile çöktü |
| ✅ | **THE_COUNTED_TURN** (mod D · ② 3,0 · ⑧ 0,0 · ⑩ 3,4) | ④ en düşük skor | erkek↔kadın yüz kırılması → kavram sızması kilidi · kayış/eldiven penetrasyonu |
| ✅ | **THE_ROSE_COAT** (iki figür, temassız) · **THE_HEALING_GROUND** (uzaylı varlık + bedel sahnesi) | ⑤ en yakın konsept | iki ayrı şerit · temas yok TASARIM SPEC'te · biniş yerine merdiven tırmanışı riski · bedel imajı ÖNCE hâli (D179) |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  21  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   46
ZORUNLU SATIR:   14938
SEÇMELİ KAYIT:   5 / 70  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
