# 📖 THE_LAST_TOW — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 28.09.2026 10:35
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | 40 dersin 31'i bu filme düşüyor; 9'u "—" (replik/iki-insan/dikey etiketli) |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | — |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | 48 klibin 48'i tek çekim; NEGATIVE ① film boyu birebir |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | yüz yalnız 6 klipte konu; kalan 42'de vizör berrak + kimlik dizisi 4 öznitelik |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | ⛔ hiçbir promptta başlık/jenerik yok · araç ayarı kutusu ÜRETİM DEFTERİ'nde |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | kir/çizik takvimi SAHNE SINIRINA yazılır, klip içinde sabit (㉜⑥) |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | [LESSON n] etiketi gövdeye yazılmaz; kilitler cümle olarak girer |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S12 (K46-K48) final; kuyruk kartı YOK, son 10 s çıkış sorusu taşır |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | — |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | metinsiz sayaç ÜÇ kanal: ışık çizgisinin mesafesi · dikişteki açıklık mm · kesici VAR/YOK |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | ⭐ bu filmin 1 numaralı metin riski: zemin İŞLENMİŞ METAL. Pozitif karşı cümle: bilgi taşıyan tek şey dikiş, perçin ve göktaşı çukuru |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | sırt görünen 9 klipte tek sürekli yüzey cümlesi + sırt ünitesi yasağı |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | kafiye çifti K01↔K48 (aynı kurulum, resif) SPEC B'ye yazıldı — KRONOS ⑨ RHYME BROKEN emsali |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | ⛔ vizör SAYIYLA: düz tek pane + kalın koyu gri çerçeve; referans paketi YAZILMADIĞI için ilk iki klipte elle biçim kontrolü |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | TEK KARE cümlesi: "levhanın üstünde DİK duran çelik anahtar" (nesnenin adı var) |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | kimlik 4 öznitelik, aynı sırada; boy/ten/saç/yaş 0 promptta (red defteri #15) |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | efor 11 klipte: 0,30 g'de gövde destek + duraksama; sözlük tek sahnede kalmıyor |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | kesici kafası kordonla ASILMAZ — kemerdeki yuvaya oturur, mekanizma sanılmasın |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | yön anatomik uzuv + kadrajdaki yer birlikte; 180° çizgisi sahne içinde aşılmaz |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | ⛔ saydamlık yok; çıplak deri 0 kare — ㉑ için her uzuv adının ±12 kelimesinde örtü adı |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | zemin bir kez tarif edilir (LIGHT satırında değil gövdede) |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IMAGE = t=0; durum satırı IMAGE'a da yazılır (㉜④) |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | ⛔ modelden sessizlik İSTENMEZ: her klipte AUDIO dolu, sessizlik KURGUDA (MUZIK dosyası) |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | 1 numaralı risk = metal zemine basılan metin [D138]; tarif kilidiyle korunuyor |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | ⭐ bu filmin omurgası: ışık çizgisi 12 sahnede tek yönde ilerler, GERİ YANMAZ — sahne başına mesafe yazılı |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | — |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | tek rejim: 0,30 g vakum · 48/48 promptta aynı PHYSICS satırı |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | ⭐ yıldız yüksekliği ÇOK ALÇAK ve ARTIYOR — sahne başına derece yazılı, komşu sahnede flip yasak |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | seçim K43'te bedende okunur: kesici elden BIRAKILIR ve kadrajda kalır |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | — |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | bedel bedende ödenir: K43'ten sonra sağ elin kemer yuvası BOŞ, 5 klipte görünür |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | yorgunluk sahne sınırında artar, klip içinde sıfırlanmaz; CONTINUOUS ACTION satırı bunu taşır |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | kimlik dizisi PLAN'da ilan edilir, 48 promptta aynı sırayla |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | üç çapa cümlesi: GÖK (boş siyah) · UFUK (regolit sırtı) · İM (resifin sırtı) |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | K01↔K48 lockoff çifti planda VE SPEC'te; niyette bırakılmıyor |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | K01 soru: dik duran anahtar neden düşmüyor · K48 çıkış: resifte yeni işaret |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | ardışık iki klip aynı vuruşu taşımaz; TEMPO şeridi 12 sahne için yazılı |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | temas·değişim·sonuç kadrajda; temas iki klibe bölünür (§3.6) |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | IN FRAME dışındaki beden tarif edilmez — 48 promptta ilk satır IN FRAME |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | üç kutu ÜRETİM DEFTERİ'nde: altyazı KAPALI · filigran YOK · konuşan ağız yok (KRONOS ⑤ filigran emsali) |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | MUZIK dosyasına LUFS/dBTP + hard mute noktası yazılır |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | — |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | 12 kartın 6'sı tetikliyor (3·4·5·9·12 + metin) → kilit tavanı 20'de tutulacak |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 542 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | 18 maddelik kapı listesi adım 10'da koşacak; B5 dörtlüsü 02_KONSEPT'e yazıldı |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | "umursamadım"ın üç sebebi: istek=açmak/göndermek · bedel=kesici K43 · muhatap=resif |
| ✅ | `KILAVUZ_REHBERI.md` | 2568 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | §2.7 8 dk kartı · §3.8 SOĞUK KAYNAK · §4.1 bilimkurgu · §5.1 negatif çekirdek 8 cümle |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 437 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3 iskelet: IN FRAME · Clip n of 48 · tek kilit 3. satır · START FRAME |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | tip = FİZİKSEL YASA (birinci tercih); TEK KARE cümlesi anahtarın adını taşıyor |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 314 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | YALNIZLIK (depoda 3) · tanım cümlesi TAKAS kalıbı DEĞİL · motif: ayrı tutulan iki yüzey |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | K01 hook: insansız kadraj + dik duran anahtar; ilk 3 s'de kural görünür |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 396 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | §3 güvenli bant ≥1 ölçek + ≥45° · açı tipi ≥3 · DÖNÜŞ ≥%40 · KÜME aranmaz (㉜) |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | ⭐viral ölçütü YÜZ + HAREKET; 48 klipte bant 0-3 (28.09 ölçümü) — aday K07 · K40 · K43 |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 324 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | örüntü kırıcı sahneler ARASINDA; süre 48 × 10 s = 480 s; ses köprüsü sahne içinde kesilmez |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | sekiz satır + İLK↔SON: K01'de hiçbir şeye dokunmayan el, K43'te bilerek yapıştıran el |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | çapa üçlüsü her klipte: bakış · ağırlık · nefes; gövde fiili efor cümlesiyle |
| ✅ | `COK_KLIPLI_SAHNE_KILAVUZU.md` | 403 | **[cok-klip]** · yatay film: sahne 2-6 klip · §2 kapsama şablonu · §3 CONTINUOUS ACTION · §4 sahne kilidi · zincir yok · ㉜ (PLAN'da SAHNE PLANI yoksa "—") | ⭐ rejim dosyası: 12 sahne 3-5 klip · CONTINUOUS ACTION 36 klipte · sahne kilidi birebir · zincir dili 0 |
| ✅ | `FIZIKSEL_EFOR_VE_YERCEKIMI_KILAVUZU.md` | 243 | **[efor]** · §1 destek·gövde·işaret·duraksama · §1.5 saydamlık tuzağı [D175] · §2 düşük g'de düşüş dili · çarpma üç evre (efor/düşüş yoksa "—") | 0,30 g'de düşüş dili: mesafe+süre yazılır, ivme yazılmaz [D127]; gövdeyi taşıma üç evre |
| ✅ | `POST_TRAVMA_VE_DURUM_HAFIZASI_KILAVUZU.md` | 167 | **[darbe]** · §1 toparlanma merdiveni = D207 · §2 hasar düz cümle + referans sayfası · §3 kadro sayı kilidi (darbe/hasar/kadro çıkışı yoksa "—") | toparlanma merdiveni K40'tan sonra: gövde yükü omuzda, 3 klip boyunca düşmez |
| ✅ | `MIKRO_AKSIYON_VE_HALUSINASYON_KILAVUZU.md` | 181 | §1 mikro→makro · §2 yürüme platosu · §3 temas iki klibe · §4 filigran = araç · tripod ADAY-98 | temas iki klibe bölünür · yürüme platosu 4 sahnede kırılır · ⛔ tripod kelimesi yok (ADAY-98) |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 444 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | ⭐ 48 klibin her biri SÜREÇ fiili taşır; TIMELINE ≤3 satır, son satır SÜRDÜRME |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | ⚠️ iki riskli yüzey: gövdeyi taşımak (red #8-#9 sözlüğü) ve yakın-makro yüzsüz uzuv (#13) |
| ✅ | `PROMPT_HATA_ONLEME_KILAVUZU.md` | 519 | §1 on kilit · §2 ORTAM CÜMLELERİ (kopyala-yapıştır) · §3 15 hata sınıfı · §4 promptun kapatamadığı üç sınıf · §5 novum kilidi · §7 --kilit ölçümü (19.09.2026 · 31 film / 688 bulgu) | ⛔ §2'de §3.8 için HAZIR CÜMLE YOK — bu film yazacak (adım 11 · §3.9 emsali) |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | — |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | — |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | — |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | §9 kimlik: 4 öznitelik · Character Bible bundan sonra yazıldı |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | §5 sırt tek sürekli yüzey · §8 vizör düz pane + kalın çerçeve · arketip E BELGESEL |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | T1·T2·T6 tetikliyor AMA sahip YAZILMASIN dedi (28.09) → PLAN'a gerekçe + ilk iki klipte elle biçim kontrolü |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1343 | 116 film · 101'i ölçülmemiş; SPEC verilmeden mod V koşulan film sayısı 9 → SPEC operatöre VERİLECEK |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | ⚠️ #2 YR (insansız klip + uzun negatif) K01-K02'de · #8/#9 PK (gövde sözlüğü) K40-K46'da · #13 PB (yüzsüz makro uzuv) K43'te |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | final ve tutundurma en düşük iki sütun → K46-K48 bekleyiş süresi planda yazılı |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | kural ihlali sayısı: bu filmde 1 kurmaca kural (kaynak) + 1 sonucu (ışık kopartır) — maya eşiği |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | bedel bedende okunma hücresi 7 filmde düştü [D206] → kemer yuvası boşluğu 5 klipte |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | AUDIO STATE beyanı ölçüm değildir → SPEC E bloğuna ffprobe satırı |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 127 | — |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | — |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | renk sıcaklığı sıçraması ölçülmüş arıza → 12 sahne için tek yıldız, tek renk, yükseklik yazılı |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | ⭐ KRONOS ⑫ "LEAVES AT 00:48" — 8 dk'nın ölçülmüş arızası ORTA BÖLÜM; S4-S6 prosedür riski |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 104 | ⑬ üretim defteri olmadan koşmaz → defter klip başına satırla açıldı |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 64 | 0,30 g'de bisiklet pedallama/nötr duruş arızası → her klipte destek noktası adlandırılıyor |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 64 | hedef vektörü FLIP en sık arıza → ekran yönü sahne içinde sabit |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 92 | — |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 128 | nicelik sürüklenmesi (kir, hasar) metinle tutulamıyor [D84] → sahne sınırına yazıldı |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 106 | vakumda havadan ses en sık 🔴 → AUDIO satırı "duyulan her şey temastır" ile açılıyor |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 94 | en düşük iki film yapı ve duygu yayında düştü; 12 sahnenin her biri seçim ya da başarısız deneme |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 113 | filigran 15/15 sahnede ölçülmüş → araç ayarı kutusu ZORUNLU |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 96 | cetvelsiz ölçek bulgusu düşer → kesici 46 cm, anahtar 56 cm, kapak bir kol boyu: tek ölçü |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 78 | 11/11 vuruş okunurluğu iyi örnek; kesme noktası hareketin içinde |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 78 | WEIGHTLESS WORK en ağır 🔴 → gövdeyi tutan 3 klipte nefes/omuz/titreme yazılı |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | lockoff creep ölçülmüş → "locked-off" her CAMERA satırında |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (72 dosya · 18170 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `KRONOS_SON_SINYAL` — yatay 8 dk, 2 bölüm × 24, 30 ham rapor | ① aynı format | ⭐ ⑫ HOOK **"LEAVES AT 00:48"**: art arda prosedür sahneleri orta bölümü düşürdü. Bu filmde S4-S6 tam o risk → S5'e TERSLİK, S6'ya BEDEL konuldu. Ayrıca ⑨ RHYME BROKEN (ilk/son kare kafiyesiz) → K01↔K48 lockoff çifti |
| ✅ | `THE_COLD_WELD` — §3.8'in tek filmi (yatay 2 dk · 15 sahne) | ② aynı ortam kartı | ⭐⭐ **PARK EDİLMİŞ DERS ADAYI: "yoklukla kanıtlanan kural ekranda okunmuyor"** — altı merceğin altısı novumu adlandıramadı, çünkü bütün kanıtlar YOKLUKtu (düşmeyen anahtar · kalkmayan avuç · kaymayan levha). Bu film kuralı **POZİTİF OLAYLA** kanıtlar: dikiş KOPAR · botlar KOPAR · açıklık KAPANIR · kesici YAPIŞIR. İkinci ders: filmin ana sayacı (kararan avuç diskleri) hiçbir mercekte görünmedi → sayaç küçük prop değil, kadrajın KONUSU olacak |
| ✅ | `THE_FROST_LINE` — yalnızlık etiketli, iki QA partisi | ③ aynı tema | üç novum vuruşu EKRANDAYDI ve mercekler üçünü de göremedi/ters okudu [D151-D154]; ayrıca iki sahne EKSİK üretildi ve kuyrukta kayboldu → ÜRETİM DEFTERİ klip başına satır + teslim satırı ZORUNLU |
| ✅ | `THE_ROSE_COAT` — ④ HİKAYE 2,3 (yatay, T4'ün en düşüğü) | ④ en düşük skor | duygu yayı 1/10: 13 sahne olay taşıyordu ama seçim taşımıyordu. Karşı önlem: 12 sahnenin 12'si ya SEÇİM ya BAŞARISIZ DENEME (S4 ve S9 bilerek başarısız) |
| ✅ | `THE_BORROWED_WEIGHT` — enkazdan yük taşıma + yalnız kurtarıcı | ⑤ en yakın konsept | taşınan yükün KONUMU cümlede yoktu, yalnız varlığı vardı → prop çapası: kızağın ve gövdenin yeri her klipte aynı kelimelerle yazılır |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  26  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   51
ZORUNLU SATIR:   16929
SEÇMELİ KAYIT:   5 / 72  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür (eski çizelge 126 dosya /
~42.000 satırdı ve 126/126 satırdan sahte kilit çıkmıştı). Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).

⚠️ Okuma yarıda kalırsa çizelge nerede kalındığını taşır; kaldığı satırdan
devam edilir. ⛔ Okuma bitmeden sahne sıralaması yazılmaz.
