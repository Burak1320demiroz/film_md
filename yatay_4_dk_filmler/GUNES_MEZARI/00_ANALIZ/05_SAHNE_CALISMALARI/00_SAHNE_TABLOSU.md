# 🧮 GUNES_MEZARI — SAHNE TABLOSU (sahne başına BİR satır)

> ⭐ **14.09.2026 · reform FAZ 8** (`TODO_AKIS_VE_DERS_REFORMU.md`). Sahne sayısı
> 8'i geçen filmde sahne başına ayrı 120 satırlık dosya yazılmaz; **bu tablo**
> yazılır (THE_LOCKED_PULSE: 25 sahne × 120 satır çalışma → film 747 KB, üretim
> 0 kare). Yalnız **5 kilit sahne** ayrı dosya alır — HOOK · NOVUM · DORUK ·
> BEDEL · FINAL — `film_klasoru_ac.sh --kilit-sahne <FMT> GUNES_MEZARI S<nn> <ROL>`
> ile damgalanır (`S<nn>_<ROL>.md`, tam şablon). ≤ 8 sahnelik filmde (dikey)
> bu dosya yoktur, her sahne dosya alır.
>
> Kapı: `prompt_kontrol.py` ㉚ — satır sayısı = bölüm dosyalarındaki sahne
> sayısı · beş rol dosyası var. Satırlar betik damgalar (`| S00 |` …); elle
> satır eklenmez/silinmez, sahne sayısı değişirse `--sahne-guncelle`.
>
> 🆕 **22.09.2026 · ÇOK KLİPLİ SAHNE** (`--sahne-plani` ile açılan yatay film): satır
> KLİP başınadır; betik başlığa iki sütun ekler ve satırları `| K07 | S03 | 2/3 · ⬜ |`
> biçiminde damgalar. **ROL n/N** sütununa kapsama şablonundaki rol yazılır (KURULUM ·
> EYLEM · TEPKİ · BELİRİŞ · MÜCADELE · TERSLİK · KARAR · BEDEL · DÖNÜŞ). Klibin
> `OLAY BAŞ → SON` hücresinin SON yarısı, aynı sahnedeki bir sonraki klibin
> `CONTINUOUS ACTION:` satırına kelimesi kelimesine iner [D207]. Aynı sahnenin
> `IŞIK · SES · FİZİK` hücreleri birebir aynıdır (sahne kilidi); "öncekiyle AYNI olamaz"
> kuralı yalnız SAHNELER ARASINDA geçerlidir. ㉚ SAHNE sütununu SAHNE PLANI'yla
> karşılaştırır. Kural: `COK_KLIPLI_SAHNE_KILAVUZU.md`.
>
> ⛔ Bu klasörde `## … SAHNE <n>` başlığı ve 📸/🎥 prompt başlığı YAZILMAZ
> (kapı betiği o desenleri sahne/prompt sanar). Prompt yalnız bölüm dosyasında.

## Sütunlar — her hücre TEK satır, boş hücre yok ("—" yazılır)

| sütun | ne yazılır | kaynak |
|---|---|---|
| **S** | sahne no (betik damgalar) | `03_SAHNE_SIRALAMASI` |
| **OLAY BAŞ → SON** | ne değişiyor: `<başta> → <sonda>`; klip içi değişim varsa `⚠️ARA` | çalışma şablonu 🎬 |
| **B5** | İSTEK / ENGEL / BEDEL / MUHATAP / AYRILIK — bu sahne hangi satırı taşıyor | `02_KONSEPT_VE_RISK` |
| **KURULUM** | harf + işaret (`B · dönüş S3`) · lens · mesafe · ölçek · açı tipi | `ACI_YAYI` §3-§4 |
| **OPTİK** | kadraj eni (m) · ana nesne (px) — ⛔ ≥100 px [D179]; sığmıyorsa `⛔` | `KILAVUZ` §5.2 hesabı |
| **IN FRAME** | face · hands · torso · legs · full body · back · none — promptun ilk satırı olur [㉖] | `IMAGE_VIDEO_PROMPT_TEMPLATES` V3 |
| **TAŞIYICI** | devamlılık: giren/çıkan/taşınan nesne + önceki/sonraki sahne | çalışma şablonu 👤 |
| **IŞIK · SES · FİZİK** | üçü tek hücrede `·` ile; palet/ses dokusu öncekiyle AYNI olamaz | ortam kartı · `KURGU_RITMI` §2 |
| **REPLİK** | `—` ya da `<saniye> · konuşan · İŞLEV · ağız okunuyor/okunmuyor` | `DIYALOG_SAHNESI` §2-§3 |
| **KİLİT / UYARI** | bu sahneye düşen kilit(ler) D-no ile + `04_UYARI_NOTLARI` satır no; en çok 3 | `01_QA_DERS_HASADI` |
| **İZLEYİCİ CÜMLESİ** | "bu figür ne istiyor" — seems/probably YASAK; ⭐VİRAL ise `YÜZ:` + `HAREKET:` | `OYUNCULUK_YAZIM` §1 · §3 |
| **KAPI** | ⬜ → ✅ satır tam ve optik tutuyor; ✅ olmadan o sahnenin promptu yazılmaz | — |

Doldurulmuş satır nasıl görünür (örnek; gerçek satırlar aşağıda betik damgalıdır):

```
S03 · glove closes on wheel → wheel stopped, strap slack ·  ENGEL  ·  B · dönüş S1 · 35mm · 1,6 m · MCU · eye level
    · 1,1 m · 340 px  ·  hands, torso  ·  strap in (S02) / out (S05)  ·  neutral ceiling · hum + warble · 0,25 g
    · —  ·  D200 · D216 · U-4  ·  he wants the wheel to move, not to understand it  ·  ✅
```

---

## 📋 TABLO

| K | SAHNE | ROL n/N | OLAY BAŞ → SON | B5 | KURULUM | OPTİK (eni m · px) | IN FRAME | TAŞIYICI | IŞIK · SES · FİZİK | REPLİK | KİLİT / UYARI | İZLEYİCİ CÜMLESİ | KAPI |
|:--:|:--:|---|---|:--:|---|---|---|---|---|---|---|---|:--:|
| K01 | S01 | 1/3 · KURULUM | kısık küre yavaş dönüyor → aynı hızda dönmeye devam ediyor, metalin inlemesi bir kez daha yükseliyor | — | C · 35mm · 2,2 m · h1,60 · MS · üst açı | 2,26 m · küre kadrajı doldurur | none | küre giriyor (film başı) / K02'ye taşınır | kafesteki kürenin altından gelen koyu kızıl-altın, başka kaynak yok · gövde içinden alçak yapısal uğultu · 0,38 g · mühürlü soğuk gövde | — | D192 · D59 · U1-3 | Bu şeyi bir yere götürüyorlar. | ✅ |
| K02 | S01 | 2/3 · EYLEM | küre üç halkanın odağında → aynı yerde, gemi şehrin üstünden geçmeye devam ediyor | — | I · 24mm · 25,0 m · h12,0 · WS · göz hizası | 37,50 m · küre 922 px · pencere 205 px | none | küre (K01) / gemi ve pencere K04'e | kafesteki kürenin altından gelen koyu kızıl-altın, başka kaynak yok · gövde içinden alçak yapısal uğultu · 0,38 g · mühürlü soğuk gövde | — | D78 · D157 · U1 | Bu ışığı taşıyan şey buraya geliyor. | ✅ |
| K03 | S01 | 3/3 · TEPKİ | iki eldiven konsol rayında kapalı, omuzlar yüksek → aynı tutuş, çağrı sürerken kask bir derece iniyor | MUHATAP | C · 35mm · 2,2 m · h1,60 · MS · üst açı · dönüş K01 | 2,26 m · yüz 374 px | face · hands · torso | kask ve zırh giriyor / eldivenler K08'e | kafesteki kürenin altından gelen koyu kızıl-altın, başka kaynak yok · gövde içinden alçak yapısal uğultu · 0,38 g · mühürlü soğuk gövde | 26,0 s · kayıt · görünmeyeni taşır (çocuklar) · ağız konuşmuyor | D95 · D146 · D217 | Sesi tanıyor ve şaşırmıyor. | ✅ |
| K04 | S02 | 1/6 · KURULUM | gemi inmiş, kızak gövdenin yanında → aynı yerde, kızağın kayışı sarkmaya devam ediyor | İSTEK | I · 24mm · 25,0 m · h12,0 · WS · göz hizası · dönüş K02 | 37,50 m · kaide kemeri 6,0 m · 615 px | none | gemi (K02) / kızak K18'e · kaide K13'e | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D209 · U-3-5 | Buraya iş için gelmiş. | ✅ |
| K05 | S02 | 2/6 · YOL | gövde heykelin bacakları arasında, ağırlık ön botta → aynı adım ritmi, pelerin kendi savrulmasını sürdürüyor | — | F · 35mm · 1,5 m · h0,95 · MS · alt açı | 1,54 m · gövde MS · yüz 546 px | full body · legs | pelerin ve kırağı pası başlıyor / K06'ya | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D147 · U-2-5 | Yolu biliyor, aramıyor. | ✅ |
| K06 | S02 | 3/6 · EYLEM | omuz yarı açık kapıda, tabanlar kilitli → kapı bir el genişliği açık, omuz hâlâ kapıda | — | G · 35mm · 4,0 m · h1,30 · WS · OTS | 4,11 m · gövde 1589 px · kapı 2,0 m | back · full body | pelerin arkadan görünür / kapı K06'da kalır | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D139 · D213 · U-6-5 | İçinde kimse var mı diye bakıyor. | ✅ |
| K07 | S02 | 4/6 · TERSLİK | diz zeminde, avuç oyuğun kenarında → aynı üç temas noktası, buhar yakası dik kalmaya devam ediyor | — | F · 35mm · 1,5 m · h0,95 · MS · alt açı · dönüş K05 | 1,54 m · oyuk 0,40 m · 993 px | hands · torso · legs | oyuk giriyor / K24'e taşınır ⭐ | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D90 · U-5 | Sıcak bir şey buldu ve dokunmuyor. | ✅ |
| K08 | S02 | 5/6 · KARAR | sol avuç kazınmış güneşin üstünde düz → avuç aynı yerde, hilal yanık izi kadrajda kalıyor | MUHATAP | D · 50mm · 1,3 m · h1,40 · CU · göz hizası | 0,94 m · eldiven 1019 px · hilal iz 163 px | hands | hilal yanık izi giriyor ⭐ / K11'de kanıt olur | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D91 · D213 · U8 | Bu çizimi tanıyor. | ✅ |
| K09 | S02 | 6/6 · BEDEL | diz zeminde, fener yerde, duvar boyunca çizimler → aynı duruş, omuzlar bir kez daha nefesle kalkıyor | — | C · 35mm · 2,2 m · h1,60 · MS · üst açı | 2,26 m · kazınmış güneş 510 px | full body · hands | fener yere konuyor (alışkanlık 1/3) / K14'e | göğüs hizasındaki kendi feneri + parçalanmış ay, sert kenarlı, dolgu yok · zeminde kuru tane sürükleyen ince rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D169 · D206 · U-5 | Kaç tane olduğunu sayıyor. | ✅ |
| K10 | S03 | 1/3 · KURULUM | salon boş, sıralar devrilmiş, tek lamba yanıp sönüyor → aynı boşluk, lamba aynı ritimde sönüp yanıyor | ENGEL | A · 24mm · 6,0 m · h1,50 · WS · göz hizası | 9,00 m · devrilmiş sıra 213 px | full body | çağrı en yüksek / K11'e | salonda yanıp sönen tek ölü lamba + kendi feneri · döngüdeki makara ve salonun ölü düz havası · 95 K · 0,90 bar · 0,38 g | 92,0 s · kayıt · aynı işlev · ağız kadrajda değil | D50 · D209 · U-5 | Sesin nereden geldiğini biliyor. | ✅ |
| K11 | S03 | 2/3 · EYLEM | levhada döngü sürüyor, hilal yanıklı eldiven kolu çekiyor → aynı döngü bir kez daha başa dönüyor | MUHATAP | C · 35mm · 2,2 m · h1,60 · MS · üst açı | 2,26 m · levha 478 px · resimdeki eldiven 204 px | none | hilal iz (K08) kanıta dönüşüyor ⭐ / K12'ye | salonda yanıp sönen tek ölü lamba + kendi feneri · döngüdeki makara ve salonun ölü düz havası · 95 K · 0,90 bar · 0,38 g | — | D138 · D50 · U6 | (insansız) İzleyici burada öğreniyor. | ✅ |
| K12 | S03 | 3/3 · TEPKİ | eldiven levhanın yüzüne düz iniyor, görüntü altında ölüyor → avuç levhada, kask bir derece iniyor, ses kesik | MUHATAP | D · 50mm · 1,3 m · h1,40 · CU · göz hizası | 0,94 m · yüz 902 px | face · hands | avuç basma alışkanlığı 2/3 / K19'a | salonda yanıp sönen tek ölü lamba + kendi feneri · döngüdeki makara ve salonun ölü düz havası · 95 K · 0,90 bar · 0,38 g | — | D202 · D213 · U-4 | Bunu yıllardır biliyordu. | ✅ |
| K13 | S04 | 1/2 · KURULUM | iki eldiven kaidenin kolunda, ağırlık geride → kol sonuna kadar inmiş, yuva ölü, omuzlar düşük | ENGEL | C · 35mm · 2,2 m · h1,60 · MS · üst açı | 2,26 m · yuva 0,60 m · 1020 px | hands · torso | kaide (K04) yakına giriyor / K19'a | yuvanın içine konmuş feneri, taşta tek koni · kaidenin kemerlerinde rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D206 · D213 · U-2 | Çalışmasını istiyor, çalışmıyor. | ✅ |
| K14 | S04 | 2/2 · SONUÇ | fener yuvanın ağzında, avuç taşta → fener yuvanın içinde, ölçü tuttu, el kenarda kalıyor | İSTEK | D · 50mm · 1,3 m · h1,40 · CU · göz hizası · dönüş K12 | 0,94 m · yuva ağzı kadrajın %64'ü | hands | fener (alışkanlık 3/3) / K20'de bırakılır ⭐ | yuvanın içine konmuş feneri, taşta tek koni · kaidenin kemerlerinde rüzgâr · 95 K · 0,90 bar · 0,38 g | — | D90 · U-5 | Hangi silindir olduğunu biliyor. | ✅ |
| K15 | S05 | 1/3 · KURULUM | çekirdek yatakta çalışıyor, rampa ovaya açık → aynı nabız, ışıklar altı yanık kalıyor | ENGEL | F · 35mm · 1,5 m · h0,95 · MS · alt açı | 1,54 m · çekirdek 1,20 m · %78 | full body · torso | çekirdek ve kalkış kolu giriyor / K16'ya | geminin kendi iç lambaları ve güverte ızgarasından yükselen donuk kızıl-altın · çekirdeğin düzenli alçak nabzı · 95 K · 0,90 bar · 0,38 g · gövde içi de mühürlü ve soğuk | — | D50 · U-2 | Gitmek elinde. | ✅ |
| K16 | S05 | 2/3 · EYLEM | eldiven kalkış kolunda kapalı, ağırlık öne → kol yerinde, eldiven açılıp koldan ayrılıyor, omuzlar düşüyor | BEDEL | H · 50mm · 0,8 m · h1,10 · CU · profil | 0,58 m · eldiven %43 · yüz profil 1467 px | face · hands | kalkış kolu K17-K18'de kadrajda KALIR / K17'ye | geminin kendi iç lambaları ve güverte ızgarasından yükselen donuk kızıl-altın · çekirdeğin düzenli alçak nabzı · 95 K · 0,90 bar · 0,38 g · gövde içi de mühürlü ve soğuk | — | D202 · D179 · U-2 | Gitmemeyi seçiyor. | ✅ |
| K17 | S05 | 3/3 · BEDEL | iki avuç mühür halkalarında, botlar yatak çerçevesinde → çekirdek yataktan çıkmış, üç ışık sönmüş, omuzlar aşağıda | BEDEL | F · 35mm · 1,5 m · h0,95 · MS · alt açı · dönüş K15 | 1,54 m · çekirdek %78 · yüz 546 px | face · hands · torso | çekirdek çıkıyor / K18'e · ışık sayacı 6→3 | geminin kendi iç lambaları ve güverte ızgarasından yükselen donuk kızıl-altın · çekirdeğin düzenli alçak nabzı · 95 K · 0,90 bar · 0,38 g · gövde içi de mühürlü ve soğuk | — | D89 · D206 · U2 | Geri dönüşü kendi elleriyle kapatıyor. | ✅ |
| K18 | S06 | 1/4 · BELİRİŞ | eldiven çeki kayışında kapalı, ağırlık geride → aynı çekiş, arkadaki tek pencere karanlık kalıyor | BEDEL | H · 50mm · 0,8 m · h1,10 · CU · profil · dönüş K16 | 0,58 m · kayış %30 · uzak pencere 267 px | hands | çekirdek kızakta / ışık sayacı 3→1 · pencere K02'nin aynası ⭐ | buzun üstünde feneri + oturduktan sonra yuvanın ışığı + geminin altındaki kısık kürenin kızıl-altını · kızak paletlerinin buzdaki sesi, taşın aldığı alçak nota · 95 K · 0,90 bar · 0,38 g | — | D206 · D78 · U-6 | Ağır ve tek başına. | ✅ |
| K19 | S06 | 2/4 · MÜCADELE | çekirdek yuvanın ağzında, avuç üstünde → çekirdek oturmuş ve kilitlenmiş, taşın içinde ışık var | İSTEK | F · 35mm · 1,5 m · h0,95 · MS · alt açı · dönüş K17 | 1,54 m · çekirdek %78 · yuva 0,60 m | hands · torso | avuç basma alışkanlığı 3/3 / K20'de KIRILIR ⭐ | buzun üstünde feneri + oturduktan sonra yuvanın ışığı + geminin altındaki kısık kürenin kızıl-altını · kızak paletlerinin buzdaki sesi, taşın aldığı alçak nota · 95 K · 0,90 bar · 0,38 g | — | D213 · D206 · U6 | İlk denemede tutmadı, ikincide tutuyor. | ✅ |
| K20 | S06 | 3/4 · KARAR | anahtar çubuğu kilidin ağzında, omuz arkasında → çubuk yutulmuş, kilit dönmüş, el boş kalıyor | BEDEL | D · 50mm · 1,3 m · h1,40 · CU · göz hizası | 0,94 m · çubuk %48 | hands · torso | anahtar çubuğu KAYBOLUYOR / fener yerde kalıyor ⭐ (alışkanlık kırılması) | buzun üstünde feneri + oturduktan sonra yuvanın ışığı + geminin altındaki kısık kürenin kızıl-altını · kızak paletlerinin buzdaki sesi, taşın aldığı alçak nota · 95 K · 0,90 bar · 0,38 g | — | D89 · D202 · U-1 | Saklayabilirdi, saklamıyor. | ✅ |
| K21 | S06 | 4/4 · DORUK | halkalar kapalı, kaide ışık almış → halkalar dışa açık ve gevşek, küre kadrajın üstünden çıkmış | İSTEK | I · 24mm · 25,0 m · h12,0 · WS · göz hizası | 37,50 m · halkalar %29 · küre 922 px | none | küre gemiden ayrılıyor / ışık sayacı 1→0 | buzun üstünde feneri + oturduktan sonra yuvanın ışığı + geminin altındaki kısık kürenin kızıl-altını · kızak paletlerinin buzdaki sesi, taşın aldığı alçak nota · 95 K · 0,90 bar · 0,38 g | — | D127 · D192 · U4 | (insansız) Sıra tuttu. | ✅ |
| K22 | S07 | 1/3 · KURULUM | ışığın sert kenarı duvarın üstünde → kenar kaldırıma inmiş ve botlarına ulaşmış, inmeye devam ediyor | — | C · 35mm · 2,2 m · h1,60 · MS · üst açı | 2,26 m · ışık kenarı kadrajı geçer | legs · torso | aydınlanmış alan sayacı: duvar → kaldırım | yeni güneş: tek sert alçak kaynak, uzun gölgeler, dolgu yok · ilk sabah yatağı: ısınan taşın tik sesi · 95 K · 0,90 bar · 0,38 g · küre kaideye bağlı | — | D90 · D193 · U3 | Geliyor. | ✅ |
| K23 | S07 | 2/3 · EYLEM | iki eldiven açık ve boş, yanlarda → aynı duruş, omuzlar bir kez daha nefesle iniyor, sokak boş kalıyor | BEDEL | A · 24mm · 6,0 m · h1,50 · WS · göz hizası | 9,00 m · gövde 726 px | full body | eldivenler K03'ün aynası ⭐ (çapa FINAL) | yeni güneş: tek sert alçak kaynak, uzun gölgeler, dolgu yok · ilk sabah yatağı: ısınan taşın tik sesi · 95 K · 0,90 bar · 0,38 g · küre kaideye bağlı | — | D202 · D211 · U3 | Birinin çıkmasını bekliyor. | ✅ |
| K24 | S07 | 3/3 · TEPKİ | oyuk ışıkta, içinde filiz → aynı kadraj, filiz ışıkta kalıyor, kırağı kenarda duruyor | — | C · 35mm · 2,2 m · h1,60 · MS · üst açı · dönüş K22 + KAFİYE K01 | 2,26 m · oyuk 0,40 m · filiz 136 px | none | oyuk (K07) ödeniyor ⭐ / film biter | yeni güneş: tek sert alçak kaynak, uzun gölgeler, dolgu yok · ilk sabah yatağı: ısınan taşın tik sesi · 95 K · 0,90 bar · 0,38 g · küre kaideye bağlı | — | D141 · D34 · U-3 | (insansız) Burada bir şey kalmış. | ✅ |


---

## ✅ TABLO KAPISI

```
□ 24 klip satırının 24'ü dolu, boş hücre yok ✅
□ her klibin OPTİK hücresinde ana nesne ≥100 px ✅ (en küçük: filiz 136 px)
□ aynı sahnenin IŞIK·SES·FİZİK hücreleri BİREBİR aynı ✅ (sahne kilidi · ㉜⑥)
□ bir klibin SON'u, aynı sahnedeki sonraki klibin CONTINUOUS ACTION'ı ✅
□ ROL n/N sütunu kapsama şablonundan ✅
□ SAHNE sütunu SAHNE PLANI ile tutuyor: 3 6 3 2 3 4 3 ✅
□ 5 kilit klip dosyası: K01 HOOK · K02 NOVUM · K21 DORUK · K17 BEDEL · K24 FINAL ✅
```

## 📌 SON 3 s HÜCRESİ — her klibin 7-10. saniyesi (SAHNE_DOLULUGU §6)

```
K01 küre aynı hızda dönüyor, metal bir kez daha inliyor
K02 gemi kadrajı geçmeye devam ediyor, küre halkaların odağında kalıyor
K03 kask bir derece iniyor, eldivenler rayda kalıyor, çağrı sürüyor
K04 kızağın kayışı sarkmaya devam ediyor, kuru tane zeminde sürükleniyor
K05 adım ritmi aynı, pelerin savrulmasını sürdürüyor
K06 omuz kapıda, kapı aralıkta duruyor, menteşe kırağısı dökülmeye devam ediyor
K07 buhar yakası dik kalıyor, avuç oyuğun kenarında bekliyor
K08 avuç çizimin üstünde, omuzlar bir kez daha nefesle kalkıyor
K09 diz zeminde, bakış duvarda soldan sağa ilerlemeye devam ediyor
K10 lamba aynı ritimde sönüp yanıyor, çağrı döngüsü başa dönüyor
K11 döngü bir kez daha başa dönüyor, levhanın ışığı aynı kalıyor
K12 avuç levhada, kask bir derece inmiş, hiçbir ses yok
K13 kol sonuna kadar inmiş, omuzlar düşük, yuva karanlık kalıyor
K14 fener yuvanın içinde, el kenarda, ışık koni olarak duruyor
K15 çekirdeğin nabzı aynı, altı ışık yanık kalıyor
K16 eldiven koldan ayrılmış ve açık kalıyor, omuzlar aşağıda
K17 çekirdek kollarında, üç ışık sönmüş, göğüs hızlı inip kalkmaya devam ediyor
K18 çekiş aynı oranda sürüyor, uzak pencere karanlık kalıyor
K19 avuç çekirdeğin üstünde, taşın alçak notası yükselmeye devam ediyor
K20 el boş, kilit dönmüş, omuz çubuğun bıraktığı yerde duruyor
K21 küre kadrajın üstünde yok, halkalar gevşek sallanmaya devam ediyor
K22 ışığın kenarı inmeye devam ediyor, botların üstünden geçiyor
K23 omuzlar bir kez daha iniyor, sokak boş kalıyor
K24 filiz ışıkta duruyor, kırağı kenarda çekilmeden kalıyor
```
