# ⚠️ THE_GREEN_CEILING — UYARI NOTLARI

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
| 1 | **S0 · S5 · S9 · S20 · S24** | THE IRON SLOPE ④ 2,6 — *"THE ONE THING NOTHING ELSE DOES: none found"*; ölçüm novumun ekrana hiç gelmediğini doğruladı (serbest parça sabit ~0,15 m/s süzüldü, kilit 3. saniyede 9,7 m istiyordu) | Novum ekrana gelmezse film 4 dakika boyunca "ormanda koşan iki kişi" olur | Kilit İVMEYE değil **KADRAJI TERK ETME SÜRESİNE** yazılır [D127]: *"the plate leaves the top of the frame within three seconds, at a steady climb, never pausing"*. S0 İPTAL KAPISIDIR ve KABUL/RET/YABANCI GÖZ/SONUÇ satırı taşır [D144] | ✅ 03 §7'de yazıldı |
| 2 | **S12 (kapak) · S23 (temas)** | D69 klon sıcak noktası üç kez tuttu: STONE SKY 1:40 araçtan iniş · STARLESS CIRCLE 2:10 gemiye biniş; ikisinde de Sayı-Ayrışma **1/10**. D77: ders yazıldıktan bir gün sonra yasakladığı sahne plana eklendi | Bu filmde İKİ biniş var ve İKİ figür — deponun ölçülmüş en yüksek klon riski | ⛔ Biniş/iniş hareketi **0 kare**. S12'de kapak kapanır ve **ikisi de kadrajda DEĞİLDİR**; S23'te kenetlenme var, geçiş yok. Her klibin ilk 0,6 s'si 10 fps şeritle taranır [D140] | ✅ 03 §2'de yazıldı |
| 3 | **her sahne (25/25)** | THE COUNTED TURN ② **3,0 · IDENTITY BREAK** — tek karakterli filmde S12/S14'te yüz erkekten kadına döndü, S13'te uzay giysisi deri cekete döndü | İki figürlü filmde aynı arıza iki kat yüzey bulur | Character Bible KELİMESİ KELİMESİNE 25/25 promptta; ayrım DÖRT eksende ve **RENK DEĞİL GEOMETRİ öncelikli** (rol şeridinin KOLU · sırt silueti · göğüs paketi · bilek düzeni); MCU'da bile rol şeridi kadrajda kalacak kadraj seçilir | ✅ 02 §5'te yazıldı |
| 4 | **S0-S24 · özellikle S13 · S15 · S19** | THE BLACK CRADLE: raporlar iki figürü "AYRI SAHNELERDE AYRI KİŞİLER" okudu; ayrım turkuaz↔amber RENKTEYDİ ve giysiyi biri "off-white/grey" biri "dark matte" gördü | Ayrım renge yazılırsa karanlık ve yağmurlu sahnede OKUNMAZ [ASTRONOT_DONANIM §2 ışık kısıtı] | ⛔ Renk İKİNCİL kanaldır. Birincil kanal: **sırt silueti** (komutan düz sırt + tek dikey omurga dikişi · mühendis U-profilli sırt bloğu) — uzak planda ve karanlıkta okunan tek fark budur | ✅ |
| 5 | **S19** | YERÇEKİMİ F1 S8: kelimeler TEMİZDİ, tetikleyici KOMPOZİSYONDU (yan yana iki ön kol + tepeden makro + yüzsüz izolasyon); önce sözcükler değişti YETMEDİ, **sahne İPTAL edildi** — deponun tek çözülemeyen red vakası | S19 aynı kompozisyonu üç imzayla birden taşıyor (① yüzsüz izolasyon+kısıtlanmış uzuv · ⑥ yüzü kapatan ekipman · ⑦ kırmızı + yakın plan) | Kamera **kol hizasına** alınır (tepeden DEĞİL); iki el **ARD ARDA ve farklı derinlikte**, aralarında bir kol boyu; kadrajda uzak gri duvar (çevresel çapa); kırmızı TEK şeride bağlanır ve uzak duvara ULAŞMAZ. ⛔ Sözcük çözümü bu sınıfa UYGULANMAZ | ✅ 02 §6'da nötr tarif yazıldı |
| 6 | **S4 · S6 · S9 · S17 · S21** | D192: filmin 1 numaralı riski TARİF kilidiyle korundu — 25 sahnenin negatifinde `no lightning bolt` yazılıyken doruk ŞİMŞEK geldi; pozitif biçimin SAYISI yoktu. D193: ışık takvimi yazıldı, ölçülmedi; sönen şeritler aynı klipte geri yandı | Şimşek bu filmin 1 numaralı riski ve tek baskın ışık kaynağı | A5 satırı SAYIYLA yazıldı (adet 1 · dallanma 0 · genişlik < bilek · süre < 0,2 s · artık ışık 0,4 s · yön saat 12, kanopinin ÜSTÜ). Işık takvimi `olcum_kapisi.sh` IŞIK TAKVİMİ İZİYLE ölçülür (↑ geri sardı · ⟳ klip içinde geri yandı) | ✅ 02 §5 A5'te yazıldı |
| 7 | **25/25 prompt** | UPWARD FALL: WORLD bloğu *"deep dry mat of fallen fibre"*, LIGHT bloğu *"the pale grey floor"* — aynı promptta iki cümle zemine iki renk verdi ve **film ortasında biyom değişti** [D176] | Orman zemini bu filmin en çok tekrarlanan yüzeyi | ⛔ Zemin **TEK CÜMLEDE, TEK RENKTE** tanımlanır ve 25/25 promptta BİREBİR aynıdır. Prompt yazımı bitince `grep -c` ile sayılır: **tam 25 eşleşme** | ✅ **KAPANDI 10.09.2026** — ㉒ yüzey renk kapısı ilk koşuda S19'da 1 BLOCK verdi (IŞIK bloğu *"far wall … grey"* diyordu); renk ENVIRONMENT'a bırakıldı, IŞIK bloğu yalnız ışığı tarif ediyor. Klasör modunda ㉒ sessiz. |
| 8 | **S14 (kalkış)** | D148: kalkış klibinde "bacaklar katlanır" yazıldı; bacak alevin İÇİNDEN geçti, "şeffaf" alev OPAK çıktı | Kalkış bu filmin zorunlu vuruşu | ⛔ Bacak **HİÇ HAREKET ETMEZ**; alev bacakların ARASINDA ve **arkası GÖRÜNÜR**. İniş takımı katlanması kadraja alınmaz.<br>⚠️ 10.09.2026: kadraj araç DIŞINA çıktı (kurulum K) — bacakların **hepsi** kadrajda, uyarının yüzeyi büyüdü; prompta "not one of them folds" cümlesi eklendi | ✅ 03 §2'de yazıldı |
| 9 | **S0 · S24 (çift)** | UPWARD FALL: ilk kare 40 m'lik pürüzsüz gövdeler + KAHVERENGİ lif zemini ↔ son kare İNCE ÇAM + GRİ/KÜL zemin — **"jest tuttu, DÜNYA tutmadı"**; iki kare iki ayrı ormanda geçiyor | Bizim çiftimiz de bir jest (açık avuç) üstüne kurulu | ÇİFT KARTI PLAN'a sahne haritasından ÖNCE doldurulur; **KONUM KİLİDİ** (figür her iki karede sol alt üçte bir) ve **DEĞİŞEN TEK DEĞİŞKEN** (② nesne: levha ulaşılabilir → ulaşılamaz) yazılı; ilk ve son karenin DÜNYASI aynı cümlelerle tarif edilir | ✅ 03 §1'de yazıldı |
| 10 | **S19 · S20 · S21 · S23 · S24** | UPWARD FALL: planın 25 sahnesinden 22'si teslim edildi ve **eksik üçün biri S24 = DORUK + TWIST + KAPAK KARESİ**. BORROWED WEIGHT: kuyrukta iki sahne eksik ve S24 twist'i yok. RING WALKER: doruk hiç monte edilmedi | Bu depoda filmin SONU sistematik olarak ekrana gelmiyor | ÜRETİM SIRASI dramatik sıra DEĞİL: **S0 (novum) → S21 (doruk) → S19 → S24 → S23 → kalanı**. Kurgu kapısında PLAN↔KURGU eşlemesi ELLE yapılır ve **SON ÜÇ KLİP ayrıca doğrulanır** [D81 · D118] | ✅ 03 §7'de yazıldı |
| 11 | **her prompt (50/50)** | D45: THE INVERSION 2:12-2:21 — kadrajda lens grafiği + *"Dr. Kaya Uçan..."* isim etiketi; film metni DÖRT ayrı yerde yasaklamıştı. D138: metin yasağı kostüme yazıldı, model ÖLÇÜYÜ ZEMİNE bastı. D155: promptun kendi defter etiketi giysiye basıldı | Bu filmin promptları ölçü, faz ve iki karakter adı taşımaya açık | ⛔ Karakter ADI gövdeye yazılmaz · `CAMERA: 75mm, f/5.6` dizilimi riskli sahnelerde CÜMLEYE çevrilir · nesne ÖLÇÜSÜ gövdeye girmez (kamera MESAFESİ muaf) · faz satırı ve kısaltma prompttan çıkar · negatife: `HUD overlay, lens data, focal length text, camera metadata, name label, subtitle, lower third, annotation` | ✅ **KAPANDI 10.09.2026** — 50/50 promptta ölçüldü: karakter özel adı 0 · nesne ÖLÇÜSÜ gövdede 0 (kamera mesafesi muaf) · faz/kısaltma satırı 0 · `focal length text` biçiminde dizilim 0. Negatife etiket ailesi yazılı (`no HUD overlay, no lens data, no name label, no subtitle, no lower third`) ve metin yasağı §5 KAPSAMINA çevrildi: *on any display, surface, patch or sign* [D138]. |
| 12 | **S10 · S11 · S19 · S23** | THE COUNTED TURN ① — on bir 🔴 blocker'ın **YEDİSİ el-nesne penetrasyonu** (parmak-kayış erimesi ×2 · başparmak-karabiner ×2 · kayış-eldiven ×2 · kayış-pin ×1); ⑦ Temas okunabilirliği **4/10** | Bu filmde kelepçe, kayış, kulp ve tutamak var | Negatif çekirdeğe İKİ CÜMLE: `Solid objects maintain strict collision boundaries; hands push against surfaces without penetrating them.` + `Fabric straps rest on top of gloves and metal pins, obeying physical collision.` Ayrıca **serbest uçlu kayış/kordon sayısı 0** [ASTRONOT_DONANIM §7 YÜKSEK risk] | ✅ **KAPANDI 10.09.2026** — iki çarpışma cümlesi insanlı 34 promptun 34'ünde birebir: *Solid objects maintain strict collision boundaries; hands push against surfaces without penetrating them* + *Fabric straps rest on top of gloves and metal pins, obeying physical collision*. Serbest uçlu kayış/kordon sayısı 0 (`no loose hose, cord or cable on either figure`, 34/34). |
| 13 | **film geneli · 25 sahne** | THE COUNTED TURN ⑧ **0.0 · NOBODY PAYS** — altı iş olayının altısında da bedende karşılık YOK. D169: 25 sahnelik fiziksel iş filminde zorlanma sözlüğü TEK SAHNEDE vardı | Bu film koşu, taşıma, tırmanma ve kelepçe üstüne kurulu | `05_SAHNE_CALISMALARI`'nda sahne başına **COST hanesi (0-9)** yazılır ve her DÜŞÜŞ RESET LOG'da gerekçelenir. GÖRÜNÜR NEFES (omuz + göğüs kafesinin periyodik yükselişi) S7-S12 ve S19'da zorunlu satır. ⛔ *"0,42 g'de kolay olur"* bir mazerettir, BULGUDUR | ✅ **KAPANDI 10.09.2026** — ⑳ zorlanma kapısı 4 promptta ateşledi; üçünde fiil NESNEYE aitti (S5 pim kendi kalkıyor · S6 kazık kendi çıkıyor · S16 yaprak levhaları, insansız kadraj), biri GERÇEKTİ: **S19 merkezî seçim**. O sahneye sayı taşıyan gövde tepkisi yazıldı (parmak eklemleri kumaşın altından belirir · tam bir saniye hareketsizlik · ikinci çekiş birincisinden YAVAŞ · omuz bir kademe düşer). Kalan üç satır ⑩ OYUNCULUK'a değil ⑥ FİZİĞE aittir ve kaydı burada. |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S0 · S2 · S4 · S6 · S9 · S17 · S21 | D50 · D78: 13 filmin 11'inde sayaç N/A; DÖRT filmde sayaç PLANLIYDI ve ekranda okunmadı. Tek çalışan vaka THIRD DUNE 10/10 — sayaç UFKU KAPLAYAN BİR DUVARDI | Kanopi ışığı sayacı okunmayabilir | Sayaç THIRD DUNE reçetesiyle: **ölçeğin İKİ UCU her karede birlikte** (kanopi tavanı + zemin aynı kadrajda). Leke sayısı 15→8→3→1→0 monotonik; ⑪ IŞIK cat.4 ölçer | ⚠️ izlenecek |
| 2 | S4 · S9 · S16 · S17 · S21 | D145 · D126: alçak açı ufku kadrajdan attı ve model boşluğu DUVARLA doldurdu; ⑤ envanteri altı sahnede "black space, star field" yazarken kadrajda GEZEGEN vardı | Bu filmin beş sahnesi ALT AÇI (D kurulumu) | Her dış prompt **EN BÜYÜK ARKA PLAN NESNESİNİ ADLANDIRIR**; ormanda ufuk kapalı olduğu için kilit **"KANOPİ TAVANI"** olarak yazılır ve her D sahnesinde birebir tekrarlanır | ⚠️ |
| 3 | S1-S24 | D147 · BORROWED WEIGHT (2:50 kirli diz → 3:20 TEMİZ diz) | Islaklık kabinde sıfırlanabilir | Islaklık MERDİVENİ K0→K1→K2, **MONOTONİK ve kabinde sıfırlanmaz**; faz satırı her prompta, faz ADI yazılmaz [D155] | ⚠️ |
| 4 | S22 · S23 | THE BLACK CRADLE: filmin novumu *"kör KIÇ ÖNDE yanaşma"*ydı ve raporun okumasında o olay HİÇ GEÇMİYOR; final "kapalı HANGAR" okundu, plan "AÇIK YUVA" diyordu | Yanaşma sahnesi model tarafından varsayılana çevriliyor | ⭐V5: **kamera HEDEFTE, araç kameraya gelir**; temas anı sahnenin İÇİNDE ve saniyesi yazılı; imza **DURGUNLUK (0,2 m/s)**. FİNAL VURUŞ KANITI: 238 s'de tam **DÖRT kelepçe** kapalı [D141] | ⚠️ |
| 5 | S22 | UZAY_USSU §5.2: 1000 m'de hedef 1080 satırlık karede ~10 pikseldir — **bu bir SAHNE DEĞİLDİR** | V1 hedef reveal fazla uzak olursa gemi okunmaz | Kesir §5.2'den türetilir; ön planda iniş aracı **ölçek şahidi ①** olarak durur ve gemi kadrajın en az %4'ünü kaplar (≈200 m · 32mm) | ⚠️ |
| 6 | S13 · S15 | KARAKTER_VE_DUYGU §4.3: doruk anında YÜZ ayırt edici DEĞİL — duygu yükü omuz/gövde/el. A1 dersi: kötü haberi SIRTTAN çek, ≥20 s tut, o sahnede tepki yakın planı YOK | İki figürün en yüklü anları kabin içinde | S13 ve S15 arkadan omuz (G); ⛔ o iki sahnede tepki yakın planı YOK. Duygu: omuz hattı + görünür nefes + kavrayışın sıkılaşması | ⚠️ |
| 7 | S10 · S12 · S22 · S23 · S24 | UZAY_USSU §8: ölçüler SPEC'te METRE, promptta GÖVDE BOYU; prompt gövdesinde tek bir metre/derece/f-sayısı GEÇMEZ | İki araç ve bir orman ölçek taşıyor | İniş aracı 7,0 m = **3,7 H** → *"a lander a little under four body-lengths tall"*; kapak 0,81 m = 0,43 H → *"a square opening she has to crouch through"*. ⛔ Kenetlenme kapağı 0,80 m'den giysili gövde GEÇMEZ — S23'te geçiş YOK, yalnız kenet | ⚠️ |
| 8 | S21 → S22 | ⑥ FİZİK: **TWO GRAVITIES verdikti her skoru EZER ve satırın ilk kelimesi olur** | Bu filmde iki ortam kartı var | ORTAM SINIRI PLAN'da ilan edilir: §3.4 → S0-S21 · §3.1 → S22-S24; **S21'de §3.4 geçerlidir**. İki kartın satırları hiçbir promptta karışmaz | ✅ 03 §0'da yazıldı |
| 9 | S7 · S8 | D104 · D174: en parlak ışık YÖN MIKNATISIDIR; gövde yönelimi yazılmayınca koşucu IŞIĞA döndü. "screen-right" modelde bir referans DEĞİLDİR | Koşu sahnelerinde şimşek en parlak kaynak | Gövde YÖNELİMİ ayrı cümlede; yön KADRAJDAKİ NESNEYE bağlanır (*"toward the lander's lit hatch, which stays in the right third"*); ⛔ şimşeğin yönü koşu yönüyle ÇAKIŞTIRILMAZ (şimşek saat 12, koşu yatay) | ⚠️ |
| 10 | S9 · S16 · S20 | §3.4 kartı: kaldırma GERÇEK ama negatif çekirdeğin `never hovering` yasağıyla ÇAKIŞIR | Yükselen nesneler "hovering" okunabilir | Yasak toz/enkaz için KORUNUR; yükselen nesneler POZİTİF hareketle yazılır: *"each object climbs steadily at about one metre per second, never pausing, never hovering"* | ⚠️ |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| **D167 · red defteri #15** (SINKING STAKE · OMNI: *"can't depict some public figures"*) | Tek kişide yedi kimlik özniteliği red üretti; bizde İKİ kişi × 25 prompt ve referans paketi YOK | ⛔ Tek pencerede **EN ÇOK 3 kişi özniteliği**. Kesin boy → GÖRELİ boy; ten rengi, saç rengi ve yaş prompt gövdesinden ÇIKAR ve PLAN'da kalır |
| **D79 · D95 · D146** | Vizör kilidi metinle tutulmuyor; ters yönde tamamen görünmez vizör "kask çıkarılmış" okunuyor | Vizör GEOMETRİYLE: kabuk + ön cam + **GÖRÜNÜR ÇERÇEVE/CONTA**; `optically clear, zero tint, no mirror coating, face fully readable at every head angle` negatif ÇEKİRDEKTE. ⛔ `seamless` 0 geçiş |
| **D123 · D59 · D67** | Yasak, yasakladığı kavramı prompta SOKAR | Sahneye-özel yasak listesi NEGATIVE'e yazılmaz; alev/duman/tehlike POZİTİF tarif edilir. `explosion`, `blast`, `fire`, `smoke`, `danger`, `panic` 0 geçiş |
| **D70 · D72 · D34 · COUNTED TURN 4:10** | Jenerik/başlık kartı ALTI vakada geri geldi | Promptlardan `title card`, `cinematic titles`, `ending text`, `end credits` TEMİZLENİR; kurgu kapısında ekran metni **0,0 s** ölçülür (kapak çıktısı dâhil) |
| **D83 · D180** | Ortam yatağı klip sınırında ölüyor; planlı mutlak sessizlik video modelinden istenince doruk kayboluyor | Kurguya TEK PARÇA ortam yatağı; sessizlik **kurguda hard mute** ile yapılır ve SPEC E'ye komut olarak yazılır. Planlı tek sessizlik: S21'in son 1,5 saniyesi |
| **D150 · UPWARD FALL** | Üretici filigranı 225/225 saniyede durdu, sekiz mercek görmedi | Teslimde **köşe testi** koşulur; filigran bir rapor bulgusu değil TESLİM KUSURUDUR |
| **D165 · D129 · D117** | SPEC plana gömülü kalınca mod D hiç koşulmuyor; paket hazırken bile çıplak rubrik yapıştırıldı | `<FILM>_QA_SPEC.md` AYRI DOSYA; SPEC yazılır yazılmaz `rubrik_paketle.sh` koşulur (PAKET_1..12) |
| **DIKEY_MIKRO_DRAMA §6.1** | Film "kırılgan insan duygusu + fotogerçekçi insan" kutusunda — AI algısının CEZALANDIRDIĞI kutu | Negatif çekirdeğin `photorealistic skin pores, sweat, scars and fatigue retained, no smoothed skin` satırı **KISALTILMAZ** — estetik tercih değil, damga önlemi. Açıklamaya fizik dayanağı yazılır, AI beyanı gizlenmez |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | ⛔ **VAR ve YÜKSEK** — iki kask, iki figür, 25 sahne, referans paketi YOK | Vizör SAYIYLA ve GEOMETRİYLE: kabuk + tek parça ön cam + görünür çerçeve/conta; `seamless` 0 geçiş; D79 cümlesi negatif ÇEKİRDEKTE (bible'da değil) |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | ⛔ **VAR** — kayış, örtü, giysi katmanı | `fabric`/`cloth`/`blanket` 0 geçiş; yerine POZİTİF ve KATI ad: *"taut woven strap"*, *"rigid panelled shell"*. ⚠️ İSTİSNA: yükselen orman döküntüsü kumaş DEĞİL, `broad flat leaf plates` |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | ⛔ **RİSK VAR** — 400 m'lik gövdeler, 320 m'lik kanopi, 7 m'lik araç, uzaktaki gemi aynı filmde | Her sahne çalışması **optik aritmetiği** satırı taşır: kadraj eni = (mesafe × sensör dikeyi) ÷ odak; ana nesne ≥100 px. 16:9 sensör dikeyi **20,25 mm** [UZAY_USSU §5.2] |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | ⛔ **VAR** — S9'da yükselen nesneler ve S22'de gemi | S9'da yükselen nesneler ≥100 px kalacak mesafeden çekilir; S22'de gemi kadrajın ≥%4'ü. ⭐ Bedel nesnesi (S20 levha) kısa kenarın **≥1/8'i** |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | ⛔ **VAR ve BU FİLMİN 1 NUMARALI DEVAMLILIK RİSKİ** — kanopi altı karanlık + yağmur | Birincil ayrım **SIRT SİLUETİ** (düz sırt ↔ U-profilli sırt bloğu); renk şeridi İKİNCİL. Karanlık sahnede silüet devralır |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | ⛔ **VAR** — iki araç + 400 m'lik gövdeler maket okunmaya açık | `no tilt-shift look, no miniature or toy-model read, no vertical band of blur across the frame; the far end of the hull is as sharp as the near end` — ⛔ çıplak `no shallow depth of field` YAZILMAZ, yalnız `on the structure` |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | ✅ **KAPALI** — ENTROPİ · sahne indeksi **S1 · S9 · S19 · S24** (≥3) | Motif kanalları da yazılı: nesne (bırakılan/yükselen şeyler) · kinesik (AÇIK AVUÇ) · ışık (kanopi ışığı) |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | ✅ **KAPALI** — BEDEL **S19**, bedel EKRANDA **S20**'de görülür | B2a/B2b de yazıldı: bedelden sonra bir seçim ve bir BAŞARISIZ deneme (S23) |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | ⛔ **RİSK VAR** — fırtına, kalkış, acil durum | Sahneye-özel yasak listesi YOK. Tehlike ALETTEN okunur, kuvvet NESNEYE taşınır. `no gore/no danger/no explosion` biçiminde tek cümle bile yazılmaz |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | ⛔ **RİSK VAR** — el aleti, pim, kelepçe kolu | Aletler FORMLA yazılır: *"a plain grey hand tool with a single straight edge and a ribbed grip"*; ⛔ `weapon/gun/blade/knife` 0 geçiş |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | ✅ **YOK** — film **0 REPLİK** (KART 7 tasarımla kapatıldı) | Gerekçe 03 §5'te; ses durumu **STATE B — sessiz, TASARIMLI** (ses kanalı VAR ve dolu) |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | ⛔ **VAR** — ıslaklık merdiveni, kanopi ışığı sayacı, fırtına | ⛔ Durum değişimi klibe DEĞİL **SINIRA** yazılır: ıslaklık K0/K1/K2 sahne SINIRINDA değişir, klip içinde SABİT kalır; kanopi leke sayısı klip içinde değişmez |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | ⛔ **RİSK VAR** — iki karakter bloğu uzun | Her prompt self-contained; `[CHARACTER BIBLE]` gibi köşeli parantez etiketi 0 geçiş [D45]. Uzunluk bandı aşılırsa KATMAN ATILIR, cümle KISALTILMAZ |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | ⛔ **RİSK VAR** — SPEC E bloğu yazılacak | SPEC'teki her makine kapısı KURU KOŞUYLA doğrulanır: `ffmpeg -hide_banner -filters \| grep -q " <filtre> "`; her kapı KOMUT · DOĞRULANDI (sürüm·tarih) · İKAME satırı taşır |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | ⛔ **VAR** — UPWARD FALL'da 195-199 s'de ÇIPLAK ÖNKOL çıktı, aynı ortam kartında | Çıplak-deri negatifi **ÜÇ BÖLGELİ** yazılır (yaka üstü · bilek · bel) ve tek satırda tutulur; `through the glove` gibi deriyi çağıran cümle 0 geçiş |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | ✅ **KAPALI** — 1 numaralı risk **ŞİMŞEK**, A5 satırı altı sayıyla yazıldı | adet 1 · dallanma 0 · genişlik < bilek · süre < 0,2 s · artık ışık 0,4 s · yön saat 12 |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
✅ 🔴 ⛔ satırlarının 13'ü de yazıldı; yazım aşamasında 8'i KAPALIYDI,
   5'i prompt yazımı/sahne çalışması aşamasına bırakılmıştı (⬜)
   ⭐ 10.09.2026 · PROMPTLAR BİTTİ → **beşinin beşi de KAPANDI** ve her biri
     ÖLÇÜLEN kanıt taşıyor (satırların kendi hücrelerinde yazılı):
       7  → ㉒ yüzey renk kapısı · S19'un IŞIK bloğu düzeltildi
       11 → 50/50 promptta ad 0 · ölçü 0 · faz satırı 0 · §5 metin kapsamı
       12 → iki çarpışma cümlesi 34/34 · serbest uçlu kayış 0
       13 → ⑳ zorlanma kanalı S19'a sayıyla yazıldı
       (beşincisi bu tabloda 🔴 değil ⛔ satırıydı ve aynı koşuda kapandı)
   ⛔ Bu blok artık BOŞ ⬜ TAŞIMAZ: dosyada kalan tek ⬜ bu cümlenin kendisidir.
✅ 🟡 ⚠️ satırlarının 10'u yazıldı ve QA_SPEC'e ölçüm olarak taşınacak
   şekilde işaretlendi (her biri ÖLÇEN merceği taşıyor)
✅ tekrar eden arıza tablosunun 16 satırının 16'sı cevaplandı —
   4'ü ✅ KAPALI, 12'si önlemli ⛔/⚠️; "bu filmde yok" diyen tek satır (11)
   GEREKÇESİYLE yazıldı
→ üçü de ✅ → 05_SAHNE_CALISMALARI/ açılabilir
```
