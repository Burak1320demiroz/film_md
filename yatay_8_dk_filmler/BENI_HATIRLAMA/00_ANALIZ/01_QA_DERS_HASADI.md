# 🧾 BENI_HATIRLAMA — QA + DERS HASADI

> **Girdi:** `00_OKUMA_CIZELGESI.md`'nin "bu filme düşen kilit" sütunu + gerekçeleri
> `00_OKUMA_CIKARIMLARI.md` (A · B · C bölümleri — satır sonundaki `[A7]` gibi işaretler oraya
> gönderir).
> **Çıktı:** aşağıdaki üç tablo — ve bu tabloların her satırı `04_UYARI_NOTLARI.md`
> ile `05_SAHNE_CALISMALARI/` içinde EN AZ BİR yere düşer.
>
> ⛔ **Sıfır satırla bir sonraki dosyaya geçilmez.** Bu depoda 189+ ders ve
> 52 film kaydı var; hiçbir konsept bunların hiçbirini tetiklemez diyen
> hasat, yapılmamış hasattır.

---

## 1. 🔒 DERS KİLİTLERİ — okunan derslerden bu filme düşenler (⛔ tavan 20 — fazlası §1b'ye)

> 14.09.2026: kaynak `00_YASAYAN_DERSLER.md` (≤ 40); bu filme düşen ≤ 20 kilit PLAN'a taşınır,
> geri kalanı §1b'de gerekçeyle bekler. Etiketi filme uymayan ders çizelgede "—" alır.
> Risk sayımı 12/14 (`02_KONSEPT_VE_RISK` §3) → **KİLİT TAVANI ≤ 20**. Satır başına TEK ders
> numarası (㉕ farklı D-numarası sayar); akraba derslerin içeriği satıra katlanır, numarası §1b'de.

> Ders metni kopyalanmaz; **bu filmde ne yapılacağı** yazılır.
> Kilit prompta ETİKETSİZ taşınır — `[LESSON n]` gövdeye girmez [D45].

| # | ders | ölçülmüş arıza | bu filmde kilit cümlesi | hangi sahnelere düşecek |
|:--:|---|---|---|---|
| 1 | D20 | tek karakterli filmde model ikinci insan çiziyor; loş iç mekânda ve biniş anında en sık | İki figürlü her promptta sayı İKİ ayrı cümle: "Exactly one person in a pressure suit and one semi-transparent woman figure, and no third figure." Kadının olmadığı mağara sahnesinde boş alan POZİTİF yazılır ("the rock wall behind him is bare"). Biniş kadrajda yok. [A3 · C2 · C7] | S1-S9 · S12-S13 · S15-S18 · S28 · S33-S37 · mağara S20-S41 · S43-S44 |
| 2 | D16 | vizör ardında yüz değişiyor; üç filmde erkek→kadın/genç yüz kayması | Adamın yüzü yalnız `IN FRAME: face` promptunda, tek cümle: "a man in his late fifties with a broad square face, a heavy brow ridge over deep-set grey eyes, short grey stubble along his jaw". Kadın figürü ile adamın yüzü aynı yüz kadrajında YOK. [B27 · C2 · C7] | yüz kurulumları C · P · V: S1 · S6 · S8 · S35 · S38 · S44 (+ S36-S37 X profil) |
| 3 | D146 | "seamless visor" kubbe davetiyesi; kask biçimi metinle tutmadı (3 vaka), referans paneli yok | Kask cümlesi film boyu birebir: "a hard off-white shell with a single flat front pane set inside a thick dark-grey rim, seated deep into a raised brushed-steel collar ring, two small square lamps set into the brow". Paket yok → 🔴 uyarı; ilk onaylı yüz karesi sonraki kask karelerine görsel girdi. [A3 · B22 · B23] | 48 sahnenin adamlı hepsi · en kritik S36-S38 |
| 4 | D157 | novumun taşıyıcısı tek karede yoktu | TEK KARE S15: saydam kadın figürü ve dizlerinin dibinde ışığı sönen canlı AYNI karede, ikisi ayrı bölgede; aynı kural S33'te ikinci kez. [A8 · B6] | S15 · S33 (kanıt S11 ısı görüşü) |
| 5 | D179 | bedel sahnesinin imaj promptu değişimin SONRASINI yazdı, bedel ekrana gelmedi | İmaj t=0 = ÖNCE hâli: S13 kadın zaten diz çökmüş · S30 atkı iki elde açık, canlının üstünde havada · S34 kayış zaten açık, cihaz bilekte · S36 başparmak düğmenin yarım avuç önünde · S37 kadın hâlâ var · S45 cihaz avuçta. [A7 · C5] | S13 · S30 · S34 · S36 · S37 · S45 |
| 6 | D213 | temas/değişim/sonuç kadraj dışında kaldı | S1 kutu elden kuma · S30 atkı canlının üstüne iner ve eller çekilir · S34 cihaz avuca · S36 düğme-ses-göz kapanması: üçü de AYNI klipte, merkez üçte birde, ≥1 s sonuç. [A8] | S1 · S30 · S34 · S36 · S40 |
| 7 | D203 | replik envanteri prompta geçmedi / fazlası üretildi | Altı kayıt kullanımı (S2 · S8 ×2 · S12 · S36 · S38) klipte ÜRETİLMEZ, post-dub; promptta tırnak YOK, AUDIO "a soft click from the recorder under his thumb" + zamanlama notu; SPEC DIALOGUE LINES post satırı olarak 6. [A7 · B17 · B20] | S2 · S8 · S12 · S36 · S38 |
| 8 | D35 | ekranda konuşan ağız lip-sync + AI damgası açar | Konuşan ağız 0 kare: kadının yüzü replik anlarında kadraj dışı ya da sırtı dönük ("no mouth is visible"); kaynak cümlesi her replikli promptta (bilek cihazı / kadının yönü). [A3 · B19] | S2 · S8 · S12 · S36 · S38 |
| 9 | D193 | ışık takvimi ölçülmedi, şeritler klip içinde geri yandı | İki takvim PLAN'da sayıyla: yüzey ışığı MONOTONİK kararır (S0 → S19 → S42) · canlı ışığı EĞRİ (sahne başına ulaşım mesafesi), seviye değişimi yalnız SINIRDA, klip içinde yalnız ilerleyen kenar. SPEC'te eğri İLAN edilir. [A5 · B26] | S0-S19 · S14-S47 · S42-S43 |
| 10 | D50 | "no text" yasağı sayacı ekrandan sildi | Kalkış penceresi metinsiz: SAĞ bilekte beş küçük kehribar lamba 5 → 4 (S6) → 3 (S26) → 1 (S35) → 0 (S44); sönme KESMEDE, hiç geri yanmaz, kayıt cihazının ekranı yok. [A7 · B21] | S0 · S3 · S6 · S26 · S35 · S44 |
| 11 | D56 | kelime ortamı değiştirdi (dalış kelimesi su çizdi) | "ağ" + "altı bacak" = örümcek kümesi → promptta web/net/spider/insect 0: damar ağı "branching amber veins set into the rock like roots", canlı "a low rounded body like a seal pup" + altı kısa eklemli bacak. [A7 · B24] | S11 · S14-S47 canlı ve ağ sahneleri |
| 12 | D67 | görüntünün kendisi hayalet/korku kümesini tetikledi | Saydam kadın = hayalet kümesi → "she is lit by the same flat grey daylight as the sand; her skin, hair and sweater have ordinary colour and texture; the dunes behind her show through her at half strength" · ghost/spirit/ethereal/glowing 0. [A7 · B6] | S0-S9 · S12-S13 · S15-S18 · S28 · S33-S37 |
| 13 | D29 | parlama sözlüğü bloom üretti | glowing/luminescent/bioluminescent/radiant/shimmering 0; kehribar ışık KAYNAK + ULAŞTIĞI YÜZEY ile: "amber light from patches under its hide lights the rock a hand's width around it, and the lit rock keeps its texture". [A7 · B26 · C7] | S14-S47 canlı/ağ · S43 · S46-S47 |
| 14 | D89 | çıkarma eylemi yanlış şeyi çıkardı (kask/eldiven) | Üç çıkarma sahnesinde TEK MÜHÜR sayımı: "exactly one thing leaves his suit in this shot: the scarf from the chest pocket; both gloves stay on, the helmet stays sealed at the collar" (S4 · S29) · S34 kayış açık başlar. [A6 · B16] | S4 · S29 · S34 |
| 15 | D168 | baştan üretilen film sonunda durdu, elde kurulum kaldı | ÜRETİM SIRASI (03 §7): K3 probu + Scene Foundation master kareleri → S37 → S36 → S47 → S0 → S15 · S30 · S11 · S44 → bölüm blokları sondan başa (B4 → B1); üretim defterinin ilk KABUL'ü S37 değilse ikinci klip üretilmez. [A10] | tüm film · URETIM_DEFTERI |
| 16 | D202 | merkezî seçim ve bedel bedende okunmadı | ÇAPA ÜÇLÜSÜ SPEC'te önce/sonra aynı kanalda: SEÇİM S36 omuz + başparmak · BEDEL S30 eller (dolu→boş) · FİNAL S45 el (avuç→cep kapağı). [A8 · B13] | S30 · S36 · S45 |
| 17 | D210 | kafiye çifti ve lockoff niyette kaldı | S0 ↔ S47 aynı kurulum harfi ve karakter karakter aynı CAMERA cümlesi; sarı atkı iki karede de sağ üçte birde; her CAMERA "absolutely zero camera movement … In a single continuous shot." [A2 · B28 · C2] | S0 · S47 |
| 18 | D209 | dünya çapası yoktu, gök/ufuk her sahnede başka | DÜNYA ÇAPASI üç cümle birebir her dış promptta: "a dark sand plain under a low, still cloud deck" · iniş aracı ve arkasında ufuktaki uzun koyu fırtına duvarı ekranın SOLUNDA · kaya çıkıntısı (yarık) SAĞINDA. (B25 taslağının "fırtına sağda"sı B33 uzam haritasıyla düzeltildi — 17.09.2026.) [A5 · B25 · B33] | S0-S19 · S42-S43 |
| 19 | D123 | yasak olarak yazılmış şiddet sözcüğü redde yol açtı | yara/ölüm/hayalet sözlüğü NEGATIVE dahil 0: "wound · injured · dying · dead · ghost · grave · corpse · blood" yerine "a dark cold patch where its light is absent" · "she kneels low, sitting back on her heels". [A7 · B16] | S11 · S13 · S14-S15 · S23 · S27 · S33 |
| 20 | D180 | planlı mutlak sessizlik modelden istendi, gelmedi | S37 sessizliği KURGUDA: müzik S35 sonunda (360 s) biter — 03 §2 ve SES §6 ile hizalandı 17.09.2026, yatak + kask içi nefes −35/−40 dB kalır (dijital sıfır YOK); video AUDIO boş istenmez. MUZIK dosyasına saniyeli satır. [A8 · B11 · B30] | S36 · S37 · MUZIK |

### 1b. ⛔ UYGULANMAYAN KİLİTLER — tavanı aşanlar (PLAN'daki blokla aynı)

> ⚠️ "Uygulanmayan" = PLAN'ın 20 satırlık PROMPT KİLİDİ bloğunda ayrı satır almadı. Çoğunun
> içeriği yine de yazılır — ama kilit olarak değil, **sahne tablosu sütunu / SPEC satırı / üretim
> defteri kutusu** olarak. Hangisinin nereye gittiği sağdaki sütunda.

| ders | neden bu filmde prompt kilidi olarak uygulanmadı · içeriği nerede |
|---|---|
| D69 · D140 | klon sıcak noktaları (loş iç mekân · klip başı 0,6 s) — içerik #1'e katlandı; klip başı taraması kurgu kapısında |
| D82 | ses kaynağı kilidi — #8'e katlandı |
| D95 · D79 | berrak vizör "kask yok" okunur · sırt pozitif — Character Bible + §5.2 ekleri (her promptta değil, IN FRAME'e göre) |
| D175 | çıplak deri negatifi kadın figürüyle çelişir → negatif "on the suited man" öznesine bağlı; Negative Bible satırı |
| D42 · D147 | kir 3 kademe global, sınırda artar — sahne tablosu "kir" sütunu + SPEC C KİMLİK DİZİSİ |
| D207 · D169 · D206 | yorgunluk 0-6 · efor gövde tepkisi · bedel bedende — sahne tablosu "yorgunluk/efor" sütunu, TIMELINE satırı |
| D59 | still/frozen/holds tek başına yazılmaz — prompt_kontrol ⑧ zaten sayar; SAHNE_DOLULUGU §4 ⑥ |
| D76 | yokluk novumu (gölge yok) → S9 birincil kanıt pozitif olay (kum içinden geçer) — sahne çalışması S9 |
| D88 | sınırlı izin tam izin — saydamlık "at half strength" karşılaştırmalı cümle #12'ye katlandı |
| D128 | metaforun fiziği — S37 "like breath fading from cold glass" (toz metaforu yok), sahne çalışması S37 |
| D43 · D28 | temasla değişim eritir · biyolüminesan temas — geometri sabit, yalnız ışık kenarı hareket eder; adam canlıya dokunmaz (#6 ve SPEC SIFIR KİLİDİ Z7) |
| D90 | milimetrik olay — S22/S24 düğüm ışığı "bir avuç" ulaşım mesafesiyle; sahne tablosu |
| D127 | ivme yerine süre — S1 kutu düşüşü süreyle; sahne çalışması S1 |
| D143 · D39 | toz şelalesi / swirl — S23 bacadan kum "a few dozen grains at a time"; sahne çalışması S23 |
| D154 | tekrar eden doğa olayı VARLIK — fırtına tek sayılı cümle + takvim; World Bible CHANGE satırı |
| D192 | 1 no. risk sayıyla — saydamlık "half strength" + S37 süre cümlesi; SPEC F göz kapısı |
| D200 | tek kadrajda iki yerçekimi — ihlal yalnız görüntüye ait; Physics Bible tek g |
| D141 | FİNAL VURUŞ KANITI S47 (atkı ×1 · kehribar ışık ×2) — SPEC B satırı (prompt kilidi değil) |
| D211 · D212 | ilk 10 s soru / ardışık aynı vuruş — 03_SAHNE_SIRALAMASI vuruş tablosu |
| D138 · D155 | ölçü yüzeye yazılmaz · kapital kısaltma yok — prompt_kontrol ㉑ zaten sayar |
| D167 | kimlik ≤3 öznitelik — #2'nin yüz cümlesi bu sınıra göre yazıldı |
| D174 · D86 | yön nesneyle · kim solda — SPATIAL MAP + KONUM KİLİDİ (IKI_KISI §6) sahne tablosunda |
| D214 · D215 | IN FRAME · araç ayarı — V3 iskeletinin kendisi / üretim defteri üç kutu |
| D216 · D217 · D83 | ses miksi · replik görüneni söylemez · yatak — MUZIK + SPEC; replikler zaten görünmeyeni taşır |
| D122 · D124 · D135 · D204 | saniyeler hesaplatılır · klip süresi ffprobe · iki şerit · SPEC 7 çapa — PLAN künyesi + QA_SPEC |
| D158 · D172 · D176 · D208 | seçim sonrası seçimler · sarkan taşıyıcı yok · zemin tek cümle · kimlik dizisi — sıralama + SPEC |
| D198 · D201 | etiket filme uymuyor (sıfır-g · vakum) — "—" |

## 2. 🚨 QA KAYITLARINDAN GELEN ARIZALAR — `01_FILM_RAPORLARI/`

> Seçilen kayıtlardan (TUR 5 · 7 kayıt) + T tabloları ve ham rapor taraması (C2 · C7).
> ⛔ "skor düşüktü" yazılmaz; **hangi kare, hangi ölçüm, hangi sebep** yazılır.

| film kaydı | mercek | bulgu (ölçülmüş) | bu filmde nasıl önlenecek |
|---|---|---|---|
| THE_COUNTED_TURN | ② 🔴 | S12 (1:50) · S14 (2:10) MCU'da sakallı erkek yüzü → pürüzsüz KADIN yüzü; S13 giysi deri cekete döndü | adam yüzü + kadın figürü aynı yüz kadrajında yok · erkek çapası (stubble) · SPEC F "yüz cinsiyeti S1=S36=S38=S44" |
| THE_GRAVITY_ANCHOR (ham) | ② | "across a direct cut … changes to a Caucasian female face" | aynı kural; üretim defterine yüzlü klip başı karesi |
| THE_COUNTED_TURN | ① 🔴 ×9 | kayış eldiven ayasından ve pinden geçiyor, parmaklar karabinerle kaynaşıyor (0:27 · 0:35 · 1:26 · 1:44 · 3:25) | S29/S30 atkı ve S34 kayış: "the wool rests on top of the glove and never passes through it" · el-nesne teması tek yerde |
| THE_HEALING_GROUND | ⑪ ölçüm | S11 bedel sahnesinin imajı değişimin sonrasını dondurdu (kare 111 ↔ 119, göğüs kapağı hiç açılmadı) · bedel 40 m EWS'de 3 piksel | S30 imajı atkı ELDE (D179) · S30 MS, fark ≥⅛ kısa kenar |
| THE_HEALING_GROUND | ⑪ ses profili | planlı 2 s mutlak sessizlik doruğun sesli anına düştü (−20,4 dB) | S37 sessizlik kurguda (kilit #20) |
| THE_HEALING_GROUND | ② | kolu yazılmayan eldiven zeminde sahipsiz "ikinci insanın eşyası" okundu | S27 · S40 · S34 el insertlerinde "the forearm and sleeve continuing out of frame to his shoulder" |
| THE_HERD | MANTIK 🚨 | kask baloncuğu sayısal takvime rağmen S5-S11'de kayboldu ve geri geldi (kalın atmosfer filmi) | 🔴 paketsiz kask riski (uyarı) · kask cümlesi sahne başına birebir · ilk onaylı kask karesi görsel girdi |
| THE_HERD | belge kontrolü | Çehov nesnesi (fener) kadraj kenarında → kurulum okunmadı · final S11 montajda yok | atkı S4'te merkez üçte bir, ≥⅛ · S47 üretim sırasında 3. ve KESİLEMEZ |
| THE_ROSE_COAT | ④ ① ② ⑤ | final yerine planın yasakladığı merdiven tırmanışı geldi (2:00-2:09) · belgesiz mercek novumu 🔴 BLOCKER yazdı · insan şeridi "2" ölçülemedi | S43 "his boots stay on the sand, one glove on the lowest rung" · SPEC NOVUM "KUSUR DEĞİL" · İKİ ayrı şerit (adam / görüntü) |
| THE_HARD_DOCK | ⑨ Kafiye 2 | S24 kapanış kurulumu B, açılış A → kafiye kırıldı | S47 kurulum harfi ve CAMERA cümlesi S0 ile karakter karakter aynı |
| THE_HARD_DOCK | ⑪ | S8→S9 yüzde renk sıcaklığı sıcaktan nötre sıçradı | S35-S38 aynı ışık kurulumu, kask içi dolgu cümlesi sabit |
| THE_HARD_DOCK | ⑫ | "LEAVES AT 00:25" · kokpit-dış tekrar platosu | mağara bloğunda (22 sahne) her 3-4 sahnede makro kırıcı |
| MARS_SON_CIKIS | ② 🔴 | kask S33 elde → S34 takılı · askı SOL ilan SAĞ üretildi · is S15'te sıfırlandı — promptlar önceki durumu yazmıyordu | her sahne imajı önceki sahnenin SON durumunu yazar (atkı cepte/elde/canlıda · cihaz bilekte/avuçta/cepte · kir kademesi · lamba sayısı) |
| MARS_SON_CIKIS | betik ①.9 | plan 3 dosya × 12 ↔ QA 2 yarım × 18 → her koşuda yanlış teslim alarmı | 4 × 12 dosya ↔ QA birimi: sahip kararı (öneri 4 çeyrek `--bolum n/4`) |
| MARS_SON_CIKIS | ① ⑤ 🔴 | promptta tırnaklı gösterge yazısı ("HARD LOCK") ve sayı ekrana basıldı | kayıt cihazı ekransız · bilek lambası sayı değil doluluk · replik tırnaksız |
| LOW_POWER | ① ③ | voiceover başlayınca yanık anlamsız altyazı · kapalı ağız üstüne replik · kesmede dijital sessizlik çukuru | replik post + "heard only — never shown as text" · ağız kadrajda yok · yatak tek parça |
| LOW_POWER | ⑧ ⑨ | merdiven tırmanışı eforsuz · kafiye 10° dutch ile çöktü | S41 tırmanışta ikinci çekiş birinciden yavaş · dutch yok |
| THE_STILL_SWARM · THE_HOLDING_FIELD (ham) | ① ② | "duplicate character phases out of structure behind main subject" · "phantom second astronaut appears and vanishes" | mağarada boş alan pozitif · figür sayısı iki ayrı cümle |
| THE_SILENT_PERIHELION (ham) | ① ⑤ | vizörde "OPTICAL RECORDING: ERROR" yanık HUD yazısı | ısı görüşü TAM KARE renk alanı, vizör HUD'u değil; "recording" kelimesi 0 |
| LOOK_UP (ham) | ⑤ | yaratık siyah formdan "pale fleshy humanoid"e kaydı | S15'te canlı ve kadın ayrı bölgede · anatomi kilidi her canlı promptunda |
| THE_RESONANT_STRAND (ham) | ① | biyolüminesan canlı çevresine yayılan AI bloom · fırtınada kanyon duvarında doku yüzmesi | kehribar ışık düşüş mesafesiyle · S42 arka planda kaya duvarı yok |
| THE_SKYLIGHT | ⑪ ölçüm | tavanı açık mağarada ışık sütununda toz şelalesi · beyaz "ışık gölü" · karanlık filmde kesme dedektörü kör | S23 kum "a few dozen grains" · S47 "one soft patch" · SPEC E: kesme ızgarası klip listesiyle |

## 3. 🚫 RED DEFTERİNDEN — `09_URETIM_RED_DEFTERI.md`

> Deponun politika/red konusundaki TEK sayacı. ⛔ Bu tabloya red SAYISI
> yazılmaz (kural ①) — yalnız SINIF · TETİKLEYİCİ · GEÇEN ÇÖZÜM yazılır.

| sınıf (PK/PB/YR/MÇ/TK/KT) | tetikleyici | GEÇEN çözüm | bu filmde riskli kare |
|---|---|---|---|
| PK | şiddet/ölüm sözlüğü yasak olarak bile yazılmış (dead · body · wound · corpse) | sözlük tamamen arındırıldı, malzeme TARİF edildi | S11 · S13 · S14-S15 (yaralı canlı · çökmüş kadın) |
| PK | OMNI "can't depict some public figures" — tek kişide yedi kimlik özniteliği + her promptta "face fully readable" | ⬜ önerilen: kimlik yığını sökülür, yüz yalnız konu olduğu sahnede | S1 · S36 · S38 · S44 (yüzlü) · kadın figürü öznitelik yığını |
| PK | milliyet ifadesi | yalnız fiziksel tanım | tüm promptlar (0) |
| PB | bedenden bir şeyin ÇIKARILMASI (kask) | nesne sahneye zaten çıkmış girer | S34 kayıt cihazı kayışı · S4/S29 atkı cepten |
| PB | yan yana iki ön kol + tepeden makro + yüzsüz izolasyon | kadraj değişti (nesne hizası, ard arda) — sözcük değişimi YETMEDİ | S27 eller siper · S34 bilek |
| PK+PB | replik + tehlike çerçevesi aynı promptta | replik değişti, tehlike sözlüğü ayıklandı | S26 · S35 (uyarı + kayıt) — replik klipte yok |
| YR | insansız sahne + uzun NEGATIVE bloğu + "exactly 0 human figures" | NEGATIVE tek pozitif `Style:` satırı | S14 · S31-S32 · S39 · S46 · S47 |
| TK / MÇ | aynı oturumda 0 başarı · üretim ilerleyip sonda düşme | 3 satırlık PROB önce · kamera hedefe | her ilk üretim günü — defter İLERLEDİ sütunu |

```
⛔ POLİTİKA KURALI [D67 · D59 · D123]: nesne ADLANDIRILMAZ, FORMU tarif edilir;
   ve yasak cümlesi de YAZILMAZ ("never drawn/aimed" D123 tuzağıdır) —
   karşılığı POZİTİF kilittir.
```

---

## 📌 HASAT ÖZETİ

```
DERS KİLİDİ:        20 adet (tavan 20 · 1b'de 40+ ders gerekçeyle, içerikleri sütun/SPEC olarak)
QA ARIZASI:         22 adet (7 film kaydı + 5 ham rapor taraması + T tabloları)
RED SINIFI:         8 adet (PK ×4 · PB ×2 · YR · TK/MÇ)
⛔ EN PAHALI ÜÇÜ:   ① KADIN FİGÜRÜNÜN KAVRAM SIZMASI — klon + adamın yüzünün kadına kayması
                       (D20 · D16 · COUNTED_TURN · GRAVITY_ANCHOR)
                    ② PAKETSİZ KASK BİÇİMİ — doruk yüzde (S36-S38), kalın atmosferde kask
                       baloncuğu takvime rağmen kayboldu (D146 · THE_HERD)
                    ③ S37 DAĞILMA — klip içi nitelik değişimi, ölçülmüş en zayıf eksen; filmin
                       doruğu (REHBER §7 · SAHNE_ZİNCİRİ §1 · D179 · D180)
   (bunlar 04_UYARI_NOTLARI'nda ⛔ satırı olur)
```
