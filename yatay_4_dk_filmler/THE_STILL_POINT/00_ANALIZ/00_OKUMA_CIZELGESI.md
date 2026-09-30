# 📖 THE_STILL_POINT — OKUMA ÇİZELGESİ

> Üretildi: `bash kilavuzlar_ve_sistem_dosyalari/okuma_cizelgesi.sh <film klasörü>` · 20.09.2026 23:35
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
| ✅ | `DERSLER/00_YASAYAN_DERSLER.md` — tablo + giriş/çıkış defteri | hepsi | Yaşayan ders havuzundan tavanı aşmayan ≤20 kilit PLAN ve QA_SPEC'e aktarılır. |
| ✅ | `DERSLER/00_DERS_YAZIM_KONTRATI.md` §2b — FREKANS · DEĞİŞEN SATIR ne demek | hepsi | Ders kilitleri somut üretim emirlerine dönüştürülür, etiket adları prompta girmez. |
| ✅ | D1 · TEK ÇEKİM — AI kesiyor · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | Her sahne bağımsız tek plandır, klip içi kesme yapılmaz, kurguda birleştirilir. |
| ✅ | D16 · YÜZ MORPH — kask arkasında yüz değişir · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | — |
| ✅ | D34 · JENERİK METNİ — model başlık kartı ekliyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Promptlarda ve negatif blokta metin yasağı vurgulanır; jenerik kartı üretilmez. |
| ✅ | D42 · YIPRANMA her karede yeniden üretiliyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | hepsi | Nora'nın giysisindeki mat beyaz paneller ve turuncu kol şeridindeki aşınma sabittir. |
| ✅ | D45 · PROMPT İSKELETİ ekrana sızıyor · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Prompt gövdesine şablon başlıkları, D-numaraları veya Türkçe talimatlar sızmaz. |
| ✅ | D62 · MONTAJDA EN ÇOK DÜŞEN SAHNE FİNAL · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S23 final sahnesi (kapsül içi ve sakinleşen anahtar) üretim sırasının başında üretilir. |
| ✅ | D70 · ÜRETİM KİLİTLERİ KURGUYU BAĞLAMIYOR — jenerik kartı geri geldi · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Kurguda ek başlık/kart eklenmez, net süre 24 sahne × 10s = 240s olarak korunur. |
| ✅ | D78 · SAHNELER ARASI ANLATIM OKUNMUYOR — sayaç tek karede kanıtlanmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Arabanın ters sürüşü ve teğet hızın sıfırlanması merkez modül referansıyla kanıtlanır. |
| ✅ | D138 · METİN YASAĞI KOSTÜME, ÖLÇÜ ZEMİNE YAZILDI · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Metin yasağı sadece negatif bloktadır; hız göstergesi basit analog kadranla tarif edilir. |
| ✅ | D139 · DÜZ SIRT KİLİDİ yalnız sırt görünmezken tutuyor · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Sırt açılarında sırt ünitesi tek parça kompakt koyu gri panel olarak pozitif tarif edilir. |
| ✅ | D141 · KLİP VAR, VURUŞ YOK — twist ve döngü ekranda yoktu · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S17 Durgun Nokta anı net bir görsel zıtlıkla (dönen halka vs sabit merkez) kurulur. |
| ✅ | D146 · "SEAMLESS VISOR" kubbe davetiyesi — vizör biçimi sayıyla yazılmadı ⛔ · `DERSLER/02_KARAKTER_VE_CANLI.md` | kask | Vizör küresel kubbe değil; kask kalkanına gömülü opak parlak siyah dışbükey vizördür. |
| ✅ | D157 · NOVUMUN TAŞIYICISI TEK KARE testini geçmiyordu · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | Bakım arabasının rayda ters yönde hızlanışı ve hız göstergesi tek karede okunur. |
| ✅ | D167 · YEDİ KİMLİK ÖZNİTELİĞİ üst üste = ünlü tarifi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Karakter kimliği 3 ana unsura indirgenir: koyu gri giysi, beyaz göğüs, turuncu kol şeridi. |
| ✅ | D169 · ZORLANMA SÖZLÜĞÜ tek sahnede vardı · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | Nora'nın eforu omuz gerginliği, eldiven sıkması ve ayak sabitleme ile bedende gösterilir. |
| ✅ | D172 · TAŞIYICIYI ASAN KORDON mekanizma sanıldı · `DERSLER/07_KURGU_VE_ANLATI.md` | novum | — |
| ✅ | D174 · "SCREEN-RIGHT" modelde referans değil — yön kadrajdaki nesneyle · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | Yönler istasyonun merkez modülü, halka yayı ve araba rayı üzerinden verilir. |
| ✅ | D175 · "THROUGH THE GLOVE" deriyi çizdirdi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Tutuşlar eldiven boğumları ve kauçuk parmak yüzeyleri üzerinden tarif edilir. |
| ✅ | D176 · KONTRAST GARANTİSİ zemini ikinci kez tarif etti · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | Nora'nın koyu giysisi açık renk istasyon iç panelleri ve Satürn'ün parlak halkalarıyla ayrışır. |
| ✅ | D179 · İMAJ PROMPTU DEĞİŞİMİN SONRASINI yazdı — I2V'de imaj t=0 · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | İmaj promptları t=0 anının durağan karesini kurar; eylemin kendisi videoda başlar. |
| ✅ | D180 · PLANLI MUTLAK SESSİZLİK modelden istendi ⛔ · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | Modelden mutlak sessizlik istenmez; düşük frekanslı titreşim ve soluk sesi tanımlanır. |
| ✅ | D192 · 1 NUMARALI RİSK tarif kilidiyle korundu · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | Ters sürüşte dönüş yönünün karışma riski sabit dış uzay fonu ve merkez aks ile engellenir. |
| ✅ | D193 · IŞIK TAKVİMİ ölçülmedi — şeritler klip içinde geri yandı · `DERSLER/04_ISIK_VE_CEVRE.md` | hepsi | İstasyon aydınlatması ve dış Güneş açısı sahneler arasında sabit yönlü tutulur. |
| ✅ | D198 · SIFIR-G nesne eksensel momentum · `DERSLER/03_FIZIK_VE_HAREKET.md` | düşük-g | Boşluktaki serbest süzülmede (S15-S19) hareket düzlemsel ve sabit hızda tutulur. |
| ✅ | D200 · TEK KADRAJDA İKİ YERÇEKİMİ · `DERSLER/03_FIZIK_VE_HAREKET.md` | hepsi | Dönen halka (0.065g) ve sabit merkez (0g) aynı kadrajda bağımsız fizik bölgeleridir. |
| ✅ | D201 · VAKUMDA GÜNEŞ AÇISI komşu sahnede flip · `DERSLER/04_ISIK_VE_CEVRE.md` | vakum | Sert Güneş ışığı ve mutlak siyah gölgeler komşu açılarda 180 derece ters dönmez. |
| ✅ | D202 · MERKEZÎ SEÇİM VE BEDEL bedende okunmuyor · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | S12'de arabanın bırakılması Nora'nın aracı iki elle boşluğa itip ayrılmasıyla netleşir. |
| ✅ | D203 · REPLİK ENVANTERİ prompta geçmedi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | replik | — |
| ✅ | D206 · BEDEL BEDENDE ÖDENMİYOR — 7 film · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | Nora'nın son itişte tüm bedenini yay gibi gerip boşluğa fırlatması fiziksel bedeldir. |
| ✅ | D207 · ŞOK/YORGUNLUK kesmede sıfırlanıyor · `DERSLER/02_KARAKTER_VE_CANLI.md` | hepsi | Süzülme ve kenetlenme anlarında gövdedeki gerginlik ve yorgunluk ardışık sahnelerde sürer. |
| ✅ | D208 · KİMLİK DİZİSİ ilan edilmedi · `DERSLER/05_EKIPMAN_VE_VARLIK_SUREKLILIGI.md` | kask | Giysi bileşenleri (opak siyah vizör, beyaz göğüs, turuncu kol bandı) her sahnede kilitlidir. |
| ✅ | D209 · DÜNYA ÇAPASI yok — gök/ufuk/yer imi her sahnede başka · `DERSLER/04_ISIK_VE_CEVRE.md` | dış-mekân | Arka plandaki dev Satürn diski ve halkaları değişmez birincil dünya çapasıdır. |
| ✅ | D210 · KAFİYE ÇİFTİ ve LOCKOFF niyette kaldı · `DERSLER/01_KAMERA_VE_KESME.md` | hepsi | S00'da fırlayan anahtar ile S23'te sakin süzülen anahtar görsel kafiye çifti oluşturur. |
| ✅ | D211 · İLK 10 s SORU YOK, SON 10 s ÇIKIŞ YOK · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | İlk 10 saniyede savrulan alet tehlike sorusunu açar; son 10 saniyede kapsül mühürlenir. |
| ✅ | D212 · AYNI VURUŞ ardışık, AYNI KLİP iki kez · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Hızlanma, arabayı bırakma, boşlukta süzülme ve yakalama vuruşları birbirini tekrar etmez. |
| ✅ | D213 · AKSİYON ELİPSİ — temas/değişim/sonuç kadraj dışı · `DERSLER/07_KURGU_VE_ANLATI.md` | hepsi | Arabanın bırakılması ve kapsül demirine tutunma temasları tam kadraj içinde gerçekleşir. |
| ✅ | D214 · KADRAJDA OLMAYAN BEDEN tarif edildi · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | Promptun ilk satırındaki IN FRAME listesi neyi içeriyorsa yalnızca o kısımlar yazılır. |
| ✅ | D215 · EKRAN METNİ/FİLİGRAN/AĞIZ araç ayarı · `DERSLER/06_METIN_VE_PROMPT_DILI.md` | hepsi | — |
| ✅ | D216 · SES MİKSİ yazılmadı · `DERSLER/07_KURGU_VE_ANLATI.md` | ses | Kask içi soluk ve mekanik temas seslerinin miks seviyeleri ses belgesinde belirtilir. |
| ✅ | D217 · REPLİK EKRANDA OLANI SÖYLÜYOR · `DERSLER/07_KURGU_VE_ANLATI.md` | replik | — |

### TUR 2/3 · ÇEKİRDEK KILAVUZLAR — `FILM_KLASOR_SABLONU/00_ANALIZ/OKUMA_CEKIRDEGI.txt` manifesti

> Liste dosya sisteminin tamamı değil, MANİFESTTİR (14.09.2026). Etiketli satır
> ([kask] [replik] [iki-insan] [referans]) filme uymuyorsa **"—"** ile geçilir.
> Manifest dışı kılavuzlar havuzdur: `KILAVUZ_REHBERI` §1 tablosu tür/ortama göre
> ek dosya gösterir; açtığın ek dosyayı bu tablonun SONUNA `havuzdan açıldı` notuyla
> elle ekleyebilirsin — çizelgenin tek elle-satır istisnası budur.

| ⬜/✅ | dosya | satır | etiket · ne için | bu filme düşen kilit |
|:--:|---|--:|---|---|
| ✅ | `URETIM_ONCESI_ANALIZ/02_RISK_KARTLARI.md` | 590 | 12 kart · PLAN'dan önce · 5+ risk → kilit tavanı ≤ 20 (㉕) | Kart 3 (kask), 5 (sayaç), 8 (kamera lockoff), 13 (yapı ölçeği) aktiftir; tavan ≤ 20. |
| ✅ | `URETIM_ONCESI_ANALIZ/03_PLAN_ONCESI_KONTROL_LISTESI.md` | 540 | A kapı listesi (hikâye onayı A0 dâhil) · B5 dörtlüsü · §D | A0 onaylı hikaye, B5 omurgası ve C sayısal kilitleri eksiksiz plana işlenir. |
| ✅ | `URETIM_ONCESI_ANALIZ/06_HIKAYE_HATTI_TESHISI.md` | 710 | B5'in kaynağı · "umursamadım"ın üç sebebi | İstek (kapsüle ulaşmak), Engel (teğet hız), Bedel (aracı bırakmak) net ayrılır. |
| ✅ | `KILAVUZ_REHBERI.md` | 2400 | §1 okuma tablosu · §2.x FORMAT kartı · §3 ORTAM kartı · §4 TÜR · §5 negatif çekirdek (8 cümle) · §6 akış · §7 tuzaklar | Yatay 4 dk kartı (24 sahne, 2 bölüm), negatif çekirdek kuralları harfiyen uygulanır. |
| ✅ | `IMAGE_VIDEO_PROMPT_TEMPLATES.md` | 427 | V3 iskelet: IN FRAME · tek kilit üçüncü satır · START FRAME · bütçe | V3 şablonu kullanılır; ilk satır IN FRAME, üçüncü satır sahnenin tek kilididir. |
| ✅ | `ONERME_VE_NOVUM_KILAVUZU.md` | 276 | novum kapısı · TEK KARE cümlesi taşıyıcı nesne adıyla [D157] | Teğet hızın ters sürüşle sıfırlanması novumu bakım arabası üzerinden tek karede test edilir. |
| ✅ | `TEMA_MUHENDISLIGI_KILAVUZU.md` | 314 | §3 sekizli → §5 matris → §9 · TANIM cümlesi (TAKAS değil) | "Korku içinde doğru hareketi bulmak" teması S07, S12 ve S17 sahnelerine bağlanır. |
| ✅ | `HOOK_VE_ILK_SAHNE_KILAVUZU.md` | 571 | hook mimarisi · S0 · ilk 3 saniye | S00'da boşluğa fırlayan turuncu anahtar dönüşün öldürücü hızını ilk 3 saniyede kurar. |
| ✅ | `ACI_YAYI_VE_SEKANS_KILAVUZU.md` | 386 | §3 güvenli bant (≥1 ölçek VE ≥45°) · §4 kurulum sayısı · açı tipi ≥3 | Güvenli bant kuralları korunur; kurulum sayısı bütçesi içinde dönüşler planlanır. |
| ✅ | `SENARYO_VE_VIRAL_KAMERA_KILAVUZU.md` | 239 | ⭐VİRAL ölçütü (YÜZ + HAREKET) · §2.4 | S17 Durgun Nokta karesi arkada dönen dev istasyon zıtlığıyla viral doruk noktasıdır. |
| ✅ | `KURGU_RITMI_VE_IHRAC_KILAVUZU.md` | 317 | §2 örüntü kırıcı · kurgu kapısı · süre = sahne × klip | 24 sahne × 10.0s = 240.0s net süre; kırpma payları ve ritmik geçişler kilitlenir. |
| ✅ | `KARAKTER_KARTI_VE_DAVRANIS_KILAVUZU.md` | 400 | §1 sekiz satırlık kart · §3 karar mimarisi · §4 davranış şeridi · §10 kart bağı | Nora'nın soğukkanlı, ölçülü, paniksiz beden dili davranış şeridinde kilitlenir. |
| ✅ | `OYUNCULUK_YAZIM_KILAVUZU.md` | 465 | §1 izleyici cümlesi · §2 gövde fiili · §3 niyet kanalı · §4 tempo · §8 çapa üçlüsü | Her sahnede izleyici cümlesi Nora'nın net niyetini ve fiziksel aksiyonunu açıklar. |
| ✅ | `SAHNE_DOLULUGU_KILAVUZU.md` | 438 | §1 kilit fiili SÜREÇ · §2 üç evre / TIMELINE ≤3 satır, son satır sürdürme · §6 ölü sahne 5 soru (15.09.2026 · TUR 19 · ⬜ sahip vetosu: manifest satır hedefini aşar) | Her sahne 3 evreli zaman akışı taşır; son 2 saniye sonraki sahneye bağlanan sürdürmedir. |
| ✅ | `POLITIKA_VE_URETILEBILIRLIK_KILAVUZU.md` | 543 | red sözlüğü · nötr tarif · ⑯ politika kapısı | Yasaklı kelimeler kullanılmaz; fırlatma ve itiş eylemleri teknik mühendislik diliyle verilir. |
| ✅ | `PROMPT_HATA_ONLEME_KILAVUZU.md` | 411 | §1 on kilit · §2 ORTAM CÜMLELERİ (kopyala-yapıştır) · §3 15 hata sınıfı · §4 promptun kapatamadığı üç sınıf · §5 novum kilidi · §7 --kilit ölçümü (19.09.2026 · 31 film / 688 bulgu) | Vakum ve dönüş ortam cümleleri hazır bloklardan birebir aktarılır. |
| ✅ | `IKI_KISI_VE_AYRILIK_KILAVUZU.md` | 384 | **[iki-insan]** · §2 istek çaprazı · §5 ayrılık kartı · §6 konum kilidi · §8 faz farkı | — |
| ✅ | `DIYALOG_SAHNESI_VE_MUHATAP_KILAVUZU.md` | 386 | **[replik]** · §2-§3 değiş-tokuş tablosu · §4 dinleyen bedeni · §5-§7 değişim satırı | — |
| ✅ | `SES_VE_DIYALOG_URETIM_KILAVUZU.md` | 427 | **[replik]** · §1a kadraj dışı ses · §2a register · replik tablosu İŞLEV sütunu | — |
| ✅ | `ASTRONOT_DONANIM_VE_KIMLIK_KILAVUZU.md` | 380 | **[kask]** · §9 kimlik · Character Bible yazılmadan ÖNCE | Opak siyah vizör, mat beyaz göğüs zırhı, turuncu sağ önkol şeridi, kompakt sırt ünitesi. |
| ✅ | `UZAY_GIYSISI_SINEMATIK_TASARIM_KILAVUZU.md` | 539 | **[kask]** · §5 sırt · §8 vizör · §11 görünüş — arketip seçimi | Ağır endüstriyel arketip; kask içi ışık yok, dışbükey opak siyah vizör yüzeyi. |
| ✅ | `REFERANS_PAKETI_KILAVUZU.md` | 421 | **[referans]** · §1 tetikleyici · paket yazılacaksa kapı 0 | Kask, giysi, ORISON istasyonu ve turuncu anahtar için referans sayfaları tanımlanır. |

### TUR 4 · QA RAPORLARI — ölçülmüş arıza kaydı

| ⬜/✅ | dosya | satır | bu filme düşen kilit |
|:--:|---|--:|---|
| ✅ | `FILM_QA_RAPORLARI/00_INDEX.md` | 1266 | Depo kalite standartları ve geçmiş arıza örüntüleri incelendi. |
| ✅ | `FILM_QA_RAPORLARI/09_URETIM_RED_DEFTERI.md` | 214 | Kask ve uzay giysisinde red tetikleyici formlardan kaçınılır. |
| ✅ | `FILM_QA_RAPORLARI/03_HIKAYE_KALITE_TABLOSU.md` | 360 | İstek ve bedel dengesi kurularak novum gösterisi tuzağı aşılır. |
| ✅ | `FILM_QA_RAPORLARI/04_MANTIK_KALITE_TABLOSU.md` | 322 | Teğet hızın sıfırlanması ve bağıl hareketsizlik mantık hatasız korunur. |
| ✅ | `FILM_QA_RAPORLARI/05_SHORTS_KALITE_TABLOSU.md` | 86 | — |
| ✅ | `FILM_QA_RAPORLARI/06_KARAKTER_KALITE_TABLOSU.md` | 209 | Karakter eylemleri rasyonel fizik mühendisliği kararlarına dayanır. |
| ✅ | `FILM_QA_RAPORLARI/07_SES_KALITE_TABLOSU.md` | 122 | Vakum ses fiziği (yalnız temasla iletilen boğuk sesler) uygulanır. |
| ✅ | `FILM_QA_RAPORLARI/08_YAYIN_PERFORMANS_TABLOSU.md` | 126 | Paketleme vaadi ile ilk 30 saniye kurgu ritmi uyumlu tutulur. |
| ✅ | `FILM_QA_RAPORLARI/T10_OYUNCULUK_KALITE.md` | 48 | Vizör kapalı olduğundan vücut postürü ve el hareketleri okunur olmalıdır. |
| ✅ | `FILM_QA_RAPORLARI/T11_ISIK_KALITE.md` | 48 | Tek sert ışık kaynağı (Güneş) ve Satürn yansımaları sahneler arası tutarlıdır. |
| ✅ | `FILM_QA_RAPORLARI/T12_HOOK_KALITE.md` | 48 | S00'da fırlayan anahtar ve kopan köprü net tehlike oluşturur. |
| ✅ | `FILM_QA_RAPORLARI/T13_UYUM_KALITE.md` | 104 | Sahne promptu ile üretilen görsel arasında ölçek uyumu korunur. |
| ✅ | `FILM_QA_RAPORLARI/T14_HAREKET_KALITE.md` | 64 | Süzülme ve itiş vektörleri tutarlı fizik yönü takip eder. |
| ✅ | `FILM_QA_RAPORLARI/T15_YON_KALITE.md` | 64 | Arabanın ters gidişi ve merkeze itiş yönü kadrajda tutarlı kalır. |
| ✅ | `FILM_QA_RAPORLARI/T1_KARE_KALITE.md` | 91 | Kompozisyonlarda uzuv deformasyonu ve anomaliler önlenir. |
| ✅ | `FILM_QA_RAPORLARI/T2_DEVAMLILIK_KALITE.md` | 126 | Turuncu kol bandı ve turuncu anahtar devamlılığı her sahnede izlenir. |
| ✅ | `FILM_QA_RAPORLARI/T3_SES_KALITE.md` | 104 | — |
| ✅ | `FILM_QA_RAPORLARI/T4_HIKAYE_KALITE.md` | 93 | Çözümün bedeli olan arabanın bırakılması net hissettirilir. |
| ✅ | `FILM_QA_RAPORLARI/T5_ARKA_PLAN_KALITE.md` | 111 | Satürn halkaları ve ORISON istasyonunun dönüş geometrisi sabit tutulur. |
| ✅ | `FILM_QA_RAPORLARI/T6_FIZIK_KALITE.md` | 95 | Dönen halka ve serbest süzülme fiziği matematiksel değerlerle uyuşur. |
| ✅ | `FILM_QA_RAPORLARI/T7_AKSIYON_KALITE.md` | 77 | Eylemler ağır çekim süzülme değil, gerçek kütle aktarımı olarak işlenir. |
| ✅ | `FILM_QA_RAPORLARI/T8_EFOR_KALITE.md` | 77 | Ayak sabitleme ve fırlatma anında gerçek fiziksel güç harcanışı görünür. |
| ✅ | `FILM_QA_RAPORLARI/T9_KADRAJ_KALITE.md` | 47 | Kadraj kenarlarında uzuv kesilmesi veya anlamsız boşluk bırakılmaz. |

### TUR 5 · FİLM KAYITLARI — `01_FILM_RAPORLARI/` (70 dosya · 16957 satır)

> ⛔ **Hepsi okunmaz — SEÇİLİR ve seçim GEREKÇELENİR.** Bu deponun
> ölçülmüş arızaları kayıtların içindedir ve en pahalıları BENZER
> filmlerde tekrar eder. En az **beş** kayıt açılır:
> ① aynı formatta son yazılan film · ② aynı ORTAM kartını kullanan film
> ③ aynı TEMA etiketini taşıyan film · ④ en düşük skorlu kayıt
> ⑤ bu filmin konseptine en yakın kayıt.

| ⬜/✅ | film kaydı | neden seçildi | bu filme düşen kilit |
|:--:|---|---|---|
| ✅ | `THE_COUNTED_TURN` | ① aynı format | 24/25 sahne yatay 4 dk yapısı, döner istasyon fiziği ve kilit tavanı dengesi. |
| ✅ | `THE_HOLLOW_COUNT` | ② aynı ortam kartı | Dış uzay vakum fiziği, sert güneş ışığı ve mutlak sessizlik kuralları. |
| ✅ | `THE_FIRST_DRIFT` | ③ aynı tema | Korku anında soğukkanlılık, boşlukta serbest süzülme ve tutunma mekaniği. |
| ✅ | `THE_LAST_SHIFT` | ④ en düşük skor | Sırt ünitesi tutarsızlıkları ve kask içi parlama hatalarının önlenmesi. |
| ✅ | `THE_LEANING_ROOM` | ⑤ en yakın konsept | Merkezkaç ivmesi ile teğet hız arasındaki karmaşanın doğru çözülmesi. |

Tam liste: `ls kilavuzlar_ve_sistem_dosyalari/FILM_QA_RAPORLARI/01_FILM_RAPORLARI/`

---

## 📊 ÇİZELGE ÖZETİ

```
YAŞAYAN DERS:    40  (TUR 1 · tavan 40)
MANİFEST DOSYA:  22  (TUR 2/3 · hedef ≤ 30 dosya / ≤ 10.000 satır)
ZORUNLU DOSYA:   47
ZORUNLU SATIR:   15535
SEÇMELİ KAYIT:   5 / 70  (TUR 5)
```

⭐ 14.09.2026: bu çizelge KÜÇÜK olsun diye küçüktür. Her satırdan kilit
çıkmaz; "—" yazmak meşrudur ve `prompt_kontrol.py` ㉘ sıfır "—" görürse
çizelgeyi SAHTE sayar (BLOCK). ⬜ kalan satır varken KONSEPT yazılmaz (FIX).
