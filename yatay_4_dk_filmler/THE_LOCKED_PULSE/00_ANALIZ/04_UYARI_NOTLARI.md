# ⚠️ THE_LOCKED_PULSE — UYARI NOTLARI

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
| 1 | S2 · S15 | IRON SLOPE ⑥ (serbest panel 0,15 m/s süzüldü, kilit 9,7 m/3 s; 12/12 promptta ivme yazılıydı) · D127 · D192 A5 | NOVUM EKRANA GELMİYOR — anahtar/levye düz düşer, süzülür ya da sağa iner | promptta ivme/derece YOK; süre + yön + mesafe: "leaves the glove at chest height and is on the deck before the hand closes … a palm's width to the LEFT … and stays where it lands"; S2 = İPTAL KAPISI (3 deneme, üçüncüde PROB_KOSUSU); ⑥ FİZİK mod D kilidi t < 1,0 s / < 0,5 s · sapma ≥ 0,05 m · yön SOL; S2'de kayış KADRAJ DIŞI (rakip hareket yok, D157) | ✅ 03 §8 + 05/S02 · S15 |
| 2 | S12 · S14 · S22 · S23 | red defteri vaka 13 (YERCEKIMI S8 ×2 red — kelimeler temizdi; yan yana iki ön kol + tepeden makro + yüzsüz izolasyon → SAHNE İPTAL) · POLİTİKA imza ① · ADAY-6b | bilek kilidi kompozisyonu POLİTİKA REDDİ | kurulum D: kamera YAKA HİZASINDA YANDAN (300°, 0,75 m), TEK bilek, kask+omuz kadrajda; tepeden makro 0 kare; ikinci ön kol kadrajda 0; sözlük: seats/latch/click/stays — crush/trapped/stuck 0; 2 red → kamera C'ye taşınır (iki yenilgi), 3. sözcük denemesi yok; red günü DEFTER satırı + MOTOR | ✅ 02 §6 + 05/S12 · S14 · S22 · S23 |
| 3 | S7 · S11 · S15 · S16 · S20 · S21 · S22 | COUNTED_TURN ⑧ EFOR 0,0 NOBODY PAYS (6 iş olayının altısında beden yorulmadı) · ⑩ 3,4 THE CHOICE IS INVISIBLE (S20 manken postürü) · PAYLOAD D158 (bedelden sonra 0 seçim) · ADAY-11/12/24/41 | bedel bedende OKUNMUYOR; seçim görünmüyor | COST CURVE 25 hane PLAN'da (1 → 9, tek reset S5 gerekçeli); her iş sahnesinde TIMELINE'da ≥1 bedel fiili (omuz iner · adım kısalır · levye elden kayar · diz kırılır · tek elle iş); ÇAPA ÜÇLÜSÜ SPEC'e: CHOICE S20 (el bir avuç önde 2 s durur, açılır, geri) · COST S22 (çıplak el eldivenden çıkar, eldiven kalır) · FINAL S24 (çıplak el göğüs plakasında, tek eldiven) — BEFORE/AFTER aynı kanalda; seçimden önce 4 başarısız deneme (S3 · S4 · S14 · S15), sonra ikinci seçim (S22) | ✅ 02 §8 + 03 §2b + 05 |
| 4 | 25/25 (özellikle C · J MS/MCU) | COUNTED_TURN ② 3,0 KİMLİK KIRILMASI (S12/S14 MCU'da sakallı erkek ↔ kadın yüzü; S13 deri ceket) · D16 · ADAY-16 · SINKING STAKE vaka 15 (7 öznitelik ×25 → kişi tanımlama reddi) | vizör ardında yüz/cinsiyet değişimi; ya da kimlik yığını reddi | yüz cümlesi TEK cümle (yüz biçimi + kaş kemiği sapması + ten değeri = ≤3 öznitelik gövdede) + "a man" + giysi bloğu 50 promptta kelimesi kelimesine, MCU/CU dâhil; kesin boy/yaş sayısı PLAN'da; RK1 vizör-ardı yüz CU paneli KAPI 0; "readable at every angle" YAZILMAZ; D16 morph bloğu ayrı | ✅ PLAN Bible + 05 |
| 5 | 24/25 iç sahne | D146 ×4 (SKYLIGHT 3 kask · YERÇEKİMİ F2 · STANDING WIRE kubbe) · D139 ×3 sırt ünitesi · D95 görünmez kilit · STATIC_SHADOW ② kask S1'de yok / vizör şeffaf↔opak | kask/vizör/sırt biçim kilidi METİNLE TUTULMUYOR | kask cümlesi 25/25 aynı: "a rounded hard shell seated in a wide bronze collar ring, a single flat front pane inside a thick dark rim, the rim visible at every head angle, the pane optically clear"; sırt "one continuous ribbed surface from collar to hip, closed and smooth" her sırt gören prompta (B · G · E); REFERANS PAKETİ RK1 4-6 kare (ön · 3/4 · profil · ARKA · kask makro · vizör ardı CU) ONAYLI + seed → KAPI 0 | ✅ REFERANS_PAKETI + Bible |
| 6 | S1 · S6 · S9 · S12 · S13 · S18 | STATIC_SHADOW D203 (7 replik prompta hiç girmedi, tırnak 0) · COLD BURN D82 (telsiz repliği ekrandaki ağza yapıştı) · ADAY-64 · PAYLOAD (4 replik "gördüğümüzü anlatıyor") | replikler prompta girmez / yanlış bedene yapışır / on-the-nose | 6 MACHINE repliği bölüm promptlarında TIRNAKLA (`grep -c '"'` ≥ 6, ㉓); her replikli promptta "a flat synthetic voice from the ceiling speaker says: "…"" + "lips closed behind the visor, no mouth movement"; konuşan kaynak kadraj DIŞI; klip SESSİZ üretilir, ses post'ta; insan repliği 0; sayı yalnız makinede; SPEC DIALOGUE LINES formülle | ✅ 03 §5 + BOLUM |
| 7 | S24 · S0 | HARD_DOCK ⑨ 2/10 (S24 kurulumu B iken S0 A — kafiye kırık) · UPWARD FALL (S24 hiç üretilmedi, döngü kırık) · D141 | kapanış kafiyesi kırılır / final teslim edilmez | S24 = kurulum A, kamera cümlesi S0 ile BİREBİR + "the same fixed framing as Scene 0."; tek değişken nesne (eldiven yakada · 7 lamba · kayış 2 s · oturmuş); FİNAL VURUŞ KANITI SPEC B: 249,0 s'de tam 7 yanık lamba · 1 eldiven yakada · 0 el çarkta; üretim sırası S24 üçüncü halka; KESİLEMEZ | ✅ 03 §1 + SPEC |
| 8 | 25/25 | D13 · D50 · D155 (PAYLOAD "PHASE 1" göğüste) · D45 (Inversion "Dr. Kaya Uçan" ekranda) · STATIC_SHADOW/UPWARD FALL kart + filigran | ekran metni / etiket / kart / filigran | prompt gövdesinde etiket 0 (PHASE/EVA/STATE/köşeli parantez 0), özel ad 0; NEGATIVE tam kapsam cümlesi "no text, no lettering, no numerals on any display, surface, patch or sign"; kurgu kapısı: kart 0,0 s · filigran köşe testi · freezedetect (SPEC E/F) | ✅ Bible NEGATIVE + SPEC |

## 2. 🟡 ⚠️ SATIRLARI — yazılırken izlenir, üretimde ölçülür

| # | sahne | kaynak | risk | ne yapılacak | durum |
|:--:|---|---|---|---|:--:|
| 1 | S3 · S8 · S10 | D36/D39/D143 (jet girdaplandı) · D154 (tekrar eden olay = varlık) · KART 6 | buhar jeti döner/dağılır/klip içinde birikir | "a thin white vapour jet, straight as a ruler, a hand-span long, from the open port collar, its edge sharp" — swirl/billow/cloud 0; S8 "half that length by the end, never gone"; S10 "stops at once at the sixth second, no trailing wisp"; RO paneli (3-4 kare) | ✅ 05 |
| 2 | S0 · S7 · S21 · S24 | COUNTED_TURN ⑥ 02:50 kayış lastik gibi dalgalandı (Material Amnesia) · D59 (hang/float → süzüldü) · D153 'fabric/cloth' | kayış dalgalanır ya da süzülür | "a stiff woven webbing strap clipped at the top, it swings as one straight line, never ripples"; hang/dangle/float/fabric/cloth 0; salınım SÜREYLE ("one full swing in four seconds"); ⑥ mod D kilidi: periyot 4,0 / 2,0 s ± %25 | ✅ 05 |
| 3 | S13 (iç 0) | T5 COUNTED_TURN düz-plaka paralaks (yıldız + kemer aynı hızda) · IRON SLOPE yasaklı gezegen · DUNYA_GORUNUSU | iç kadrajda pencere/yıldız → paralaks arızası; dış kadrajda gezegen | halka içinde PENCERE YOK (13.09 kararı: lomboz A/C kadrajlarına da düşerdi); yıldız yalnız S13 dış, kamera hub'a kilitli, süreyle ("cross the frame in about three seconds"); gezegen/ay 0; ⑥ kilidi 24 °/s ± %20 | ✅ 05/S13 |
| 4 | S5 · S6 · S7 | D12/D44 (yavaş çekim hissi) · COUNTED_TURN 1:17 kalkış rijit/mekanik · OYUNCULUK §8 hazırlık önce | yürüyüş/kalkış slow-motion ya da manken | "real time, normal human pace"; kalkış "weight goes onto the left boot first, then he rises"; adım KADANSI S5 8 adım / 10 s, S7 7; Coriolis 0 (adım genişliği dışında) | ✅ 05 |
| 5 | S13 | KART 10 (insansız + uzun NEGATIVE = yapısal red, COLD BURN S8 V2) · KART 13 · HARD_DOCK ① dış dönüş açısı 45° sıçradı · STATIC_SHADOW ölçek 1:6 / dönüş 1,5°/s | tek dış sahne: yapısal red, ölçek/dönüş kayması | NEGATIVE kısa (yörünge bloğu 3 cümle); insan yokluğu pozitif kadrajla; anatomi kartı: halka 1 · spoke 4 · hub 1 — sayı promptta "four spokes"; dönüş SÜREYLE ("the stars cross the frame in about three seconds, in one steady direction"); metre 0 ("the ring's far side is a thin line"); tek sert güneş, gölge mutlak siyah; RX paneli | ✅ 05/S13 |
| 6 | S9 · S11 · S15 · S16 | HARD_DOCK ⑪ 5,5 (S8→S9 renk sıcaklığı sıçradı) · COUNTED_TURN ⑪ KEY WALKS (MCU'da ışık 3→9 saat) · ADAY-17/27 · D193 | ışık yönü/renk kurulumdan kuruluma zıplar; alarm takvimi geri sarar | KEY DIRECTION STRING kurulum harfine bağlı (A/C/D/J: tavan paneli yukarıdan-soldan; B: yukarıdan-arkadan; G: tepeden; H: yukarı); kask içi fill cümlesi 25/25 aynı, Kelvin PLAN'da; alarm periyodu yalnız S5\|S6 ve S13\|S14'te değişir; SPEC IŞIK TAKVİMİ; ⑪ mod D | ✅ Lighting Bible |
| 7 | S22-S24 | D175 (UPWARD FALL 'forearm tendons through the glove' → çıplak deri) · ㉑ üç bölge | çıplak sağ el PLANLI (S22+) ama negatif "no bare skin" onu yasaklar; ya da çıplak deri erken doğar | S0-S21: negatif tam üç bölge ("no bare skin above the collar, at either wrist, or anywhere the suit meets the gloves"); S22-S24: negatif DARALTILIR ("no bare skin above the collar or at the left wrist"), sağ el pozitif ("his bare right hand, deep brown skin with visible pores"); 'through the glove' 0; ㉑ klasör modunda satır sayımı | ✅ 05/S22-S24 |
| 8 | S2 · S7 · S10 · S12 · S20 · S22 | COUNTED_TURN ① kayış/karabiner eldiven içinden geçti ×7 · ⑦ temas 4/10 · D196 | el-nesne penetrasyonu | temas cümlesi kalıbı: "the glove closes around the rim; the rim stays outside the glove"; kayışa hiç dokunulmaz; karabiner 0; temas sahnesi ≤6; ① mod D bakar | ✅ 05 |
| 9 | S4 · S10 · S17 · S22 | SENARYO_VE_VIRAL §2.4 (ölçütsüz ⭐ düşer) · KARAKTER_VE_DUYGU göz bütçesi | ⭐VİRAL etiketi YÜZ/HAREKET satırsız | dört viral sahnede YÜZ (vizör ardı değişim + saniye) + HAREKET satırı 05'te dolu; göz görünürlüğü ≥%12 (S4 · S10 · S17 · S22 = 4 sahne ✓) | ✅ 05 |
| 10 | S23 · S10 · S12 | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 · D179 | klip içi durum değişimi (lamba yanar · jet biter · kilit kapanır) yarım/erimiş çıkar | her biri tek anlık olay + ARA DURUM YASAĞI ("at once, no flicker" / "no slow closing" / "no trailing wisp") + TIMELINE saniyesi; imaj = BEFORE (lamba sönük · jet var · yaka açık); Plan B: tutmazsa değişim SINIRA taşınır (S23 son kare → S24 ilk kare) | ✅ 05 |
| 11 | S6 → S7 | TEK_CEKIM mekân-süre (8 m yürüyüş kesmede) · D118 sıra | zaman atlaması okunmaz, "ışınlandı" hissi | S7 imajı: levye elinde, diz çökmüş, sırt eğik (yürüyüş bitmiş); S6 son kare levye elde dolapta; sert olmayan düz kesme, fan yatağı köprü; MESAFE sütunu PLAN'a | ✅ 03 §7 |
| 12 | 25/25 | ADAY-40/82 · IRON SLOPE S2 kamera kaydı (6/6 lockoff tutmadı) · SPEC E vidstabdetect (D142) | lockoff'ta kamera kayar | "fixed lockoff, absolutely zero camera movement" cümle BAŞI ve SONU; SPEC E kamera sabitliği kapısı — `vidstabdetect` kuruluysa, değilse İKAME (kenar farkı ölçümü) DOĞRULANDI satırıyla | ✅ SPEC E |

## 3. 🧯 FİLM GENELİ — tek sahneye bağlanmayanlar

| kaynak | risk | filmin tamamında ne yapılacak |
|---|---|---|
| D129 ×17 (SPEC hazırken mod V) · D204 ㉔ · D165 ÇALIŞMIYOR | SPEC yazılıp verilmez / kabuk kalır | QA_SPEC yedi makine çapası DOLU + dosyanın başında "rubriğin BAŞINA yapıştır" talimatı + §HANGİ RUBRİĞE NE VERİLİR tablosu (②③ tasarım gereği mod V) |
| D168 ×3 ÇALIŞMIYOR (SINKING STAKE · UPWARD FALL · STATIC_SHADOW) | üretim baştan başlar, doruk üretilmez | URETIM_DEFTERI §4 İLK KABUL = S20; üretim sırası PLAN'da; defter boş doğar, alanlar adlı |
| D124 (araç 10 s üretti) | ızgara yanlış varsayılır | PLAN'a "KLİP SÜRESİ = ____ ffprobe" satırı; replik/doruk saniyeleri formülle, ölçüm gelince yeniden hesaplanır |
| D74 ×n (kapı yazıldı, koşulmadı) | üretim kapıları kayıtsız kalır | her kapı KABUL / RET / YABANCI GÖZ / SONUÇ alanlı; SONUÇ ⬜ kalırsa üretim ilerlemez |
| D83 · D180 ×3 (yatak kesmede öldü · sessizlik modelden istendi) | ses yatağı delik; doruk sessizliği yok | fan cümlesi 24 promptta aynı; kurguda tek yatak; HARD MUTE 203,0-205,0 SPEC E'de; müzik 197,5'te biter |
| D110 ×6 (mercekler aynı oturumda) · D161 | QA partisi kopya | SPEC'e "her mercek TEMİZ oturumda, aynı master" satırı (yazım tarafı hatırlatması) |
| KART 12 · ⑯ | politika sözlüğü sızar | klasör modunda ⑯ 0 tetikleyici hedefi; 'leak' T2 çıkarsa "coolant loss"; milliyet 0 |
| D138 · D32 | ölçü nesnenin üstüne basılır | metre yalnız SPEC/PLAN; prompt gövdesinde gövde boyu ve el ölçüleri (palm's width · hand-span · body-length) |
| D176 | zemin iki blokta iki türlü | zemin cümlesi WORLD'de tek: "a dark grey ribbed deck"; LIGHTING kontrast cümlesi zemini yeniden tarif etmez |
| SAHNE_DEVAMLILIK §2.1 | eşanlamlı yeniden yazım | Bible blokları bayt-aynı (shasum) 50 promptta; kısaltma gerekirse KATMAN atılır |

---

## 4. 📋 BU DEPONUN TEKRAR EDEN ARIZALARI — her filmde tek tek cevaplanır

> ⛔ **"Bu filmde yok" cevabı GEREKÇE ister.** Boş bırakılan satır
> "bakılmadı" demektir.

| # | tekrar eden arıza | kaynak | bu filmde durumu | önlem |
|:--:|---|---|---|---|
| 1 | Biçim kilidi METİNLE tutulmuyor (kask/vizör/varlık kare kare değişiyor) | D146 · SKYLIGHT · STANDING WIRE | VAR — kask 24/25, vizör berrak, sırt B/G/E'de görünür; bilek halkası/port yakası 8 sahnede | REFERANS PAKETİ RK1 (kask makro + arka + vizör ardı CU) · RP (yaka + bilek halkası) KAPI 0; kask/sırt cümlesi bayt-aynı; ⛔ #5 |
| 2 | Yasak kelime kumaş sanılıp DALGALANDIRILIYOR (`fabric` · `cloth`) | D59 · D153 · OPEN CIRCUIT 17+24 geçiş | VAR — kayış (webbing) + kapitone giysi | 'fabric/cloth/canvas' 0 geçiş → "quilted padding", "woven webbing strap … as one straight line"; hang/float/billow 0; ⚠️ #2 |
| 3 | Optik aritmetiği hiç yapılmamış — lens nesneyi kadraja ALAMIYOR | OPEN CIRCUIT denetimi · §5.2 | YAPILDI — 10 kurulumun 10'u 03 §4b'de hesaplı (kadraj eni/boyu, nesne px) | D ve M'de çark/fren çarkı TAŞAR — bilinçli, kayıtlı; X'te halka taşar (ölçek şahidi) |
| 4 | Uzak nesne ~60 piksel — ekranda okunmuyor | D179 | A'da lamba 26 px (sayılır ama okunmaz) · H'de alarm lambası 43 px | lamba SAYIMI B (86 px) ve C (89 px)'de okunur; A'da yalnız dizi varlığı; 7. lambanın yanışı S23 C'de (89 px) — A'da (S24) tekrar; alarm H'de kaynak olarak ışığıyla okunur |
| 5 | Ayrım RENKLE kuruldu, gece sahnesinde iki koyu gövde ayrılmıyor | BLIND BERTH · ASTRONOT_DONANIM §2 | YOK — tek insan; ayrım gereken çift yok. Gerekçe: KART 4 ikinci figür 0, kriyo kapsülleri kadraj dışı | figür ↔ zemin kontrastı: koyu arduvaz gövde ↔ soluk tavan paneli + gri panel (SPEC E kontrast kapısı YMAX−YMIN ≥ 110 A/C'de) |
| 6 | Ortam kartının NEGATİF bloğu prompta hiç girmemiş (maket/tilt-shift okuması) | UZAY_USSU §6 · OPEN CIRCUIT ④ | VAR — S13 dış (yörünge bloğu) + iç halka (§3.7 negatifi) | S13: "no tilt-shift look, no miniature or toy-model read, no free-floating debris, no atmospheric haze"; iç: 'no free-floating debris' YAZILMAZ (g var), yerine "nothing drifts; what is dropped falls"; ⚠️ #5 |
| 7 | Tema yazıldı ama sahne indeksi yok → tema dekoratif | KALEIDA CRASH | VAR — İNSAN-MAKİNE | sahne indeksi ≥3: S2 · S10 · S12 · S18 · S22 · S24 (02 §4); PLAN'a taşınır; B2 çapraz: bedel S22 listede ✓ |
| 8 | Bedel var ama sahne numarası yok → bedel boş | 03_PLAN_ONCESI B5 | VAR | BEDEL S22 · 224,0 s (mühür açılır, eldiven kalır); kalıcı iz S23-S24; ÇAPA ÜÇLÜSÜ SPEC'te; ⛔ #3 |
| 9 | Yasak cümlesi yazıldı ("never drawn/aimed") ve model onu ÜRETTİ | D123 | RİSK — fren çarkı "never pulled", kask "never removed" yazma eğilimi | yasak fiil cümlesi 0; POZİTİF kilit: "the small wheel stays where it is; his hand returns to his knee" · "the helmet stays sealed, the rim visible" |
| 10 | Politika: nesne ADLANDIRILDI (formu tarif edilmedi) | D67 · red defteri | RİSK — 'brake valve' · 'emergency lamp' · 'trapped wrist' | fren çarkı "a second, smaller wheel with a yellow-and-black band at floor level"; alarm "a red lamp above the bay"; bilek "seated / latched"; ⛔ #2 |
| 11 | Replik zamanı ELLE yazıldı, ızgara formülüyle çelişti | D122 | VAR — 6 replik | saniyeler 03 §5'te formülle (9 + (n−1)×10 + ofset); SPEC aynı formül; ⑤ SÜRE 249,0 |
| 12 | Klip içi durum değişimi — ölçülmüş EN ZAYIF eksen | T2V-CompBench 0,0687 · SAHNE_ZINCIRI §1 | VAR — S8 jet yarıya · S10 jet biter · S12 kilit · S22 mühür · S23 lamba | 5 sahnede ARA DURUM YASAĞI + TIMELINE saniyesi; diğer bütün durum değişimleri SINIRA (alarm · RPM · eldiven S21\|S22 hazırlığı); ⚠️ #10 |
| 13 | Prompt "BIBLE'a bak" diyor — self-contained değil | kural ③ | RİSK | her prompt Bible bloklarını TAŞIR (bayt-aynı); "see bible / as before / same as scene" atfı 0 — küme/dönüş işareti bile tam kamera cümlesiyle birlikte |
| 14 | Makine kapısı KURULU OLMAYAN ffmpeg filtresine yazıldı, sessizce koşmadı | D142 · `vidstabdetect` | RİSK — E bloğu ≥6 kapı | 9. adımda `ffmpeg -hide_banner -filters` kuru koşu; her kapı KOMUT · DOĞRULANDI (sürüm · 13.09.2026) · İKAME; vidstabdetect yoksa kenar-farkı ikamesi |
| 15 | Çıplak deri negatifi bölge saymıyor (satır sonunda bölünme) | D175 · ㉑ | VAR — üstelik S22-S24'te çıplak sağ el PLANLI | S0-S21 negatif üç bölge tek satırda; S22-S24 daraltılmış negatif + pozitif çıplak el cümlesi; ㉑ klasör modunda her promptta satır sayımı; ⚠️ #7 |
| 16 | Filmin 1 NUMARALI riski yalnız SIFATLA korunmuş, sayı yok | 🆕 D192 · OPEN CIRCUIT · `03_PLAN_ONCESI` A5 | VAR — 1 numaralı risk: düşen aletin yana inmesi | A5 02 §5: süre < 1,0 / < 0,5 s · sapma bir avuç (0,11 / 0,08 m) · yön SOL · nesne 0,30 / 0,50 m; SPEC göz kapısı aynı sayıları tekrarlar; ⛔ #1 |

⭐ **Bu tablo BÜYÜR.** Yeni bir tam denetim yeni bir tekrar eden arıza
bulursa satır buraya eklenir — şablona, tek filme değil.

---

## ✅ KAPI

```
☑ 🔴 ⛔ satırlarının hepsi kapatıldı (8/8 — her biri 02/03/05 ya da PLAN/SPEC'te adresli)
☑ 🟡 ⚠️ satırları QA_SPEC'e ölçüm olarak taşınacak şekilde işaretlendi (⑥ ② ⑪ ① ⑧ ⑬ mercekleri)
☑ tekrar eden arıza tablosunun HER satırı cevaplandı (16/16 — "yok" olan tek satır #5 gerekçeli)
→ 05_SAHNE_CALISMALARI/ açılabilir
```
